# SNMP MIB module (JUNIPER-CHASSIS-CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-CHASSIS-CLUSTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:52 2024
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

(jnxJsChassisCluster,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsChassisCluster")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxJsChassisClusterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1)
)
jnxJsChassisClusterMIB.setRevisions(
        ("2013-09-20 00:00",
         "2012-07-20 00:00",
         "2011-06-28 00:00",
         "2009-05-27 00:00",
         "2009-02-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsChassisClusterNotifications_ObjectIdentity = ObjectIdentity
jnxJsChassisClusterNotifications = _JnxJsChassisClusterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 0)
)
_JnxJsChassisClusterTrapObjects_ObjectIdentity = ObjectIdentity
jnxJsChassisClusterTrapObjects = _JnxJsChassisClusterTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1)
)
_JnxJsChClusterSwitchoverInfoRedundancyGroup_Type = DisplayString
_JnxJsChClusterSwitchoverInfoRedundancyGroup_Object = MibScalar
jnxJsChClusterSwitchoverInfoRedundancyGroup = _JnxJsChClusterSwitchoverInfoRedundancyGroup_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 1),
    _JnxJsChClusterSwitchoverInfoRedundancyGroup_Type()
)
jnxJsChClusterSwitchoverInfoRedundancyGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterSwitchoverInfoRedundancyGroup.setStatus("current")
_JnxJsChClusterSwitchoverInfoClusterId_Type = DisplayString
_JnxJsChClusterSwitchoverInfoClusterId_Object = MibScalar
jnxJsChClusterSwitchoverInfoClusterId = _JnxJsChClusterSwitchoverInfoClusterId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 2),
    _JnxJsChClusterSwitchoverInfoClusterId_Type()
)
jnxJsChClusterSwitchoverInfoClusterId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterSwitchoverInfoClusterId.setStatus("current")
_JnxJsChClusterSwitchoverInfoNodeId_Type = DisplayString
_JnxJsChClusterSwitchoverInfoNodeId_Object = MibScalar
jnxJsChClusterSwitchoverInfoNodeId = _JnxJsChClusterSwitchoverInfoNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 3),
    _JnxJsChClusterSwitchoverInfoNodeId_Type()
)
jnxJsChClusterSwitchoverInfoNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterSwitchoverInfoNodeId.setStatus("current")
_JnxJsChClusterSwitchoverInfoPreviousState_Type = DisplayString
_JnxJsChClusterSwitchoverInfoPreviousState_Object = MibScalar
jnxJsChClusterSwitchoverInfoPreviousState = _JnxJsChClusterSwitchoverInfoPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 4),
    _JnxJsChClusterSwitchoverInfoPreviousState_Type()
)
jnxJsChClusterSwitchoverInfoPreviousState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterSwitchoverInfoPreviousState.setStatus("current")
_JnxJsChClusterSwitchoverInfoCurrentState_Type = DisplayString
_JnxJsChClusterSwitchoverInfoCurrentState_Object = MibScalar
jnxJsChClusterSwitchoverInfoCurrentState = _JnxJsChClusterSwitchoverInfoCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 5),
    _JnxJsChClusterSwitchoverInfoCurrentState_Type()
)
jnxJsChClusterSwitchoverInfoCurrentState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterSwitchoverInfoCurrentState.setStatus("current")
_JnxJsChClusterSwitchoverInfoReason_Type = DisplayString
_JnxJsChClusterSwitchoverInfoReason_Object = MibScalar
jnxJsChClusterSwitchoverInfoReason = _JnxJsChClusterSwitchoverInfoReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 6),
    _JnxJsChClusterSwitchoverInfoReason_Type()
)
jnxJsChClusterSwitchoverInfoReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterSwitchoverInfoReason.setStatus("current")
_JnxJsChClusterIntfName_Type = DisplayString
_JnxJsChClusterIntfName_Object = MibScalar
jnxJsChClusterIntfName = _JnxJsChClusterIntfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 7),
    _JnxJsChClusterIntfName_Type()
)
jnxJsChClusterIntfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterIntfName.setStatus("current")
_JnxJsChClusterIntfState_Type = DisplayString
_JnxJsChClusterIntfState_Object = MibScalar
jnxJsChClusterIntfState = _JnxJsChClusterIntfState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 8),
    _JnxJsChClusterIntfState_Type()
)
jnxJsChClusterIntfState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterIntfState.setStatus("current")
_JnxJsChClusterIntfSeverity_Type = DisplayString
_JnxJsChClusterIntfSeverity_Object = MibScalar
jnxJsChClusterIntfSeverity = _JnxJsChClusterIntfSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 9),
    _JnxJsChClusterIntfSeverity_Type()
)
jnxJsChClusterIntfSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterIntfSeverity.setStatus("current")
_JnxJsChClusterIntfStateReason_Type = DisplayString
_JnxJsChClusterIntfStateReason_Object = MibScalar
jnxJsChClusterIntfStateReason = _JnxJsChClusterIntfStateReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 10),
    _JnxJsChClusterIntfStateReason_Type()
)
jnxJsChClusterIntfStateReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterIntfStateReason.setStatus("current")
_JnxJsChClusterNodeZeroId_Type = DisplayString
_JnxJsChClusterNodeZeroId_Object = MibScalar
jnxJsChClusterNodeZeroId = _JnxJsChClusterNodeZeroId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 11),
    _JnxJsChClusterNodeZeroId_Type()
)
jnxJsChClusterNodeZeroId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterNodeZeroId.setStatus("current")
_JnxJsChClusterNodeOneId_Type = DisplayString
_JnxJsChClusterNodeOneId_Object = MibScalar
jnxJsChClusterNodeOneId = _JnxJsChClusterNodeOneId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 12),
    _JnxJsChClusterNodeOneId_Type()
)
jnxJsChClusterNodeOneId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterNodeOneId.setStatus("current")
_JnxJsChClusterNodeZeroSpuCount_Type = DisplayString
_JnxJsChClusterNodeZeroSpuCount_Object = MibScalar
jnxJsChClusterNodeZeroSpuCount = _JnxJsChClusterNodeZeroSpuCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 13),
    _JnxJsChClusterNodeZeroSpuCount_Type()
)
jnxJsChClusterNodeZeroSpuCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterNodeZeroSpuCount.setStatus("current")
_JnxJsChClusterNodeOneSpuCount_Type = DisplayString
_JnxJsChClusterNodeOneSpuCount_Object = MibScalar
jnxJsChClusterNodeOneSpuCount = _JnxJsChClusterNodeOneSpuCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 14),
    _JnxJsChClusterNodeOneSpuCount_Type()
)
jnxJsChClusterNodeOneSpuCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterNodeOneSpuCount.setStatus("current")
_JnxJsChClusterClusterID_Type = DisplayString
_JnxJsChClusterClusterID_Object = MibScalar
jnxJsChClusterClusterID = _JnxJsChClusterClusterID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 15),
    _JnxJsChClusterClusterID_Type()
)
jnxJsChClusterClusterID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterClusterID.setStatus("current")
_JnxJsChClusterRedundancyGroupID_Type = DisplayString
_JnxJsChClusterRedundancyGroupID_Object = MibScalar
jnxJsChClusterRedundancyGroupID = _JnxJsChClusterRedundancyGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 16),
    _JnxJsChClusterRedundancyGroupID_Type()
)
jnxJsChClusterRedundancyGroupID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterRedundancyGroupID.setStatus("current")
_JnxJsChClusterNodeID_Type = DisplayString
_JnxJsChClusterNodeID_Object = MibScalar
jnxJsChClusterNodeID = _JnxJsChClusterNodeID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 17),
    _JnxJsChClusterNodeID_Type()
)
jnxJsChClusterNodeID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterNodeID.setStatus("current")
_JnxJsChClusterWeightHealthStatus_Type = DisplayString
_JnxJsChClusterWeightHealthStatus_Object = MibScalar
jnxJsChClusterWeightHealthStatus = _JnxJsChClusterWeightHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 18),
    _JnxJsChClusterWeightHealthStatus_Type()
)
jnxJsChClusterWeightHealthStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterWeightHealthStatus.setStatus("current")
_JnxJsChClusterWeightValue_Type = DisplayString
_JnxJsChClusterWeightValue_Object = MibScalar
jnxJsChClusterWeightValue = _JnxJsChClusterWeightValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 1, 19),
    _JnxJsChClusterWeightValue_Type()
)
jnxJsChClusterWeightValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChClusterWeightValue.setStatus("current")

# Managed Objects groups


# Notification objects

jnxJsChassisClusterSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 0, 1)
)
jnxJsChassisClusterSwitchover.setObjects(
      *(("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterSwitchoverInfoRedundancyGroup"),
        ("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterSwitchoverInfoClusterId"),
        ("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterSwitchoverInfoNodeId"),
        ("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterSwitchoverInfoPreviousState"),
        ("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterSwitchoverInfoCurrentState"),
        ("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterSwitchoverInfoReason"))
)
if mibBuilder.loadTexts:
    jnxJsChassisClusterSwitchover.setStatus(
        "current"
    )

jnxJsChClusterIntfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 0, 2)
)
jnxJsChClusterIntfTrap.setObjects(
      *(("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterSwitchoverInfoClusterId"),
        ("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterIntfName"),
        ("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterIntfState"),
        ("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterIntfSeverity"),
        ("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterIntfStateReason"))
)
if mibBuilder.loadTexts:
    jnxJsChClusterIntfTrap.setStatus(
        "current"
    )

jnxJsChClusterSpuMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 0, 3)
)
jnxJsChClusterSpuMismatchTrap.setObjects(
      *(("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterNodeZeroId"),
        ("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterNodeZeroSpuCount"),
        ("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterNodeOneId"),
        ("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterNodeOneSpuCount"))
)
if mibBuilder.loadTexts:
    jnxJsChClusterSpuMismatchTrap.setStatus(
        "current"
    )

jnxJsChClusterWeightTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14, 1, 0, 4)
)
jnxJsChClusterWeightTrap.setObjects(
      *(("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterClusterID"),
        ("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterRedundancyGroupID"),
        ("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterNodeID"),
        ("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterWeightHealthStatus"),
        ("JUNIPER-CHASSIS-CLUSTER-MIB", "jnxJsChClusterWeightValue"))
)
if mibBuilder.loadTexts:
    jnxJsChClusterWeightTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-CHASSIS-CLUSTER-MIB",
    **{"jnxJsChassisClusterMIB": jnxJsChassisClusterMIB,
       "jnxJsChassisClusterNotifications": jnxJsChassisClusterNotifications,
       "jnxJsChassisClusterSwitchover": jnxJsChassisClusterSwitchover,
       "jnxJsChClusterIntfTrap": jnxJsChClusterIntfTrap,
       "jnxJsChClusterSpuMismatchTrap": jnxJsChClusterSpuMismatchTrap,
       "jnxJsChClusterWeightTrap": jnxJsChClusterWeightTrap,
       "jnxJsChassisClusterTrapObjects": jnxJsChassisClusterTrapObjects,
       "jnxJsChClusterSwitchoverInfoRedundancyGroup": jnxJsChClusterSwitchoverInfoRedundancyGroup,
       "jnxJsChClusterSwitchoverInfoClusterId": jnxJsChClusterSwitchoverInfoClusterId,
       "jnxJsChClusterSwitchoverInfoNodeId": jnxJsChClusterSwitchoverInfoNodeId,
       "jnxJsChClusterSwitchoverInfoPreviousState": jnxJsChClusterSwitchoverInfoPreviousState,
       "jnxJsChClusterSwitchoverInfoCurrentState": jnxJsChClusterSwitchoverInfoCurrentState,
       "jnxJsChClusterSwitchoverInfoReason": jnxJsChClusterSwitchoverInfoReason,
       "jnxJsChClusterIntfName": jnxJsChClusterIntfName,
       "jnxJsChClusterIntfState": jnxJsChClusterIntfState,
       "jnxJsChClusterIntfSeverity": jnxJsChClusterIntfSeverity,
       "jnxJsChClusterIntfStateReason": jnxJsChClusterIntfStateReason,
       "jnxJsChClusterNodeZeroId": jnxJsChClusterNodeZeroId,
       "jnxJsChClusterNodeOneId": jnxJsChClusterNodeOneId,
       "jnxJsChClusterNodeZeroSpuCount": jnxJsChClusterNodeZeroSpuCount,
       "jnxJsChClusterNodeOneSpuCount": jnxJsChClusterNodeOneSpuCount,
       "jnxJsChClusterClusterID": jnxJsChClusterClusterID,
       "jnxJsChClusterRedundancyGroupID": jnxJsChClusterRedundancyGroupID,
       "jnxJsChClusterNodeID": jnxJsChClusterNodeID,
       "jnxJsChClusterWeightHealthStatus": jnxJsChClusterWeightHealthStatus,
       "jnxJsChClusterWeightValue": jnxJsChClusterWeightValue}
)
