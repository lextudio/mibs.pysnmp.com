# SNMP MIB module (T11-FC-SP-ZONING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T11-FC-SP-ZONING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:38 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(T11FcSpHashCalculationStatus,
 T11FcSpPolicyHashFormat,
 T11FcSpPolicyHashValue) = mibBuilder.importSymbols(
    "T11-FC-SP-TC-MIB",
    "T11FcSpHashCalculationStatus",
    "T11FcSpPolicyHashFormat",
    "T11FcSpPolicyHashValue")

(t11ZsFabricIndex,
 t11ZsNotifyControlEntry,
 t11ZsServerEntry,
 t11ZsStatsEntry) = mibBuilder.importSymbols(
    "T11-FC-ZONE-SERVER-MIB",
    "t11ZsFabricIndex",
    "t11ZsNotifyControlEntry",
    "t11ZsServerEntry",
    "t11ZsStatsEntry")


# MODULE-IDENTITY

t11FcSpZoningMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 177)
)
t11FcSpZoningMIB.setRevisions(
        ("2008-08-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_T11FcSpZsMIBNotifications_ObjectIdentity = ObjectIdentity
t11FcSpZsMIBNotifications = _T11FcSpZsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 177, 0)
)
_T11FcSpZsMIBObjects_ObjectIdentity = ObjectIdentity
t11FcSpZsMIBObjects = _T11FcSpZsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 177, 1)
)
_T11FcSpZsConfiguration_ObjectIdentity = ObjectIdentity
t11FcSpZsConfiguration = _T11FcSpZsConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 177, 1, 1)
)
_T11FcSpZsServerTable_Object = MibTable
t11FcSpZsServerTable = _T11FcSpZsServerTable_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcSpZsServerTable.setStatus("current")
_T11FcSpZsServerEntry_Object = MibTableRow
t11FcSpZsServerEntry = _T11FcSpZsServerEntry_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcSpZsServerEntry.setStatus("current")


class _T11FcSpZsServerCapabilityObject_Type(Bits):
    """Custom type t11FcSpZsServerCapabilityObject based on Bits"""
    namedValues = NamedValues(
        ("fcSpZoning", 0)
    )

_T11FcSpZsServerCapabilityObject_Type.__name__ = "Bits"
_T11FcSpZsServerCapabilityObject_Object = MibTableColumn
t11FcSpZsServerCapabilityObject = _T11FcSpZsServerCapabilityObject_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 1, 1, 1, 1),
    _T11FcSpZsServerCapabilityObject_Type()
)
t11FcSpZsServerCapabilityObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpZsServerCapabilityObject.setStatus("current")
_T11FcSpZsServerEnabled_Type = TruthValue
_T11FcSpZsServerEnabled_Object = MibTableColumn
t11FcSpZsServerEnabled = _T11FcSpZsServerEnabled_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 1, 1, 1, 2),
    _T11FcSpZsServerEnabled_Type()
)
t11FcSpZsServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpZsServerEnabled.setStatus("current")


class _T11FcSpZoneSetHashStatus_Type(T11FcSpHashCalculationStatus):
    """Custom type t11FcSpZoneSetHashStatus based on T11FcSpHashCalculationStatus"""


_T11FcSpZoneSetHashStatus_Object = MibTableColumn
t11FcSpZoneSetHashStatus = _T11FcSpZoneSetHashStatus_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 1, 1, 1, 3),
    _T11FcSpZoneSetHashStatus_Type()
)
t11FcSpZoneSetHashStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpZoneSetHashStatus.setStatus("current")
_T11FcSpActiveZoneSetHashType_Type = T11FcSpPolicyHashFormat
_T11FcSpActiveZoneSetHashType_Object = MibTableColumn
t11FcSpActiveZoneSetHashType = _T11FcSpActiveZoneSetHashType_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 1, 1, 1, 4),
    _T11FcSpActiveZoneSetHashType_Type()
)
t11FcSpActiveZoneSetHashType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpActiveZoneSetHashType.setStatus("current")
_T11FcSpActiveZoneSetHash_Type = T11FcSpPolicyHashValue
_T11FcSpActiveZoneSetHash_Object = MibTableColumn
t11FcSpActiveZoneSetHash = _T11FcSpActiveZoneSetHash_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 1, 1, 1, 5),
    _T11FcSpActiveZoneSetHash_Type()
)
t11FcSpActiveZoneSetHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpActiveZoneSetHash.setStatus("current")
_T11FcSpZoneSetDatabaseHashType_Type = T11FcSpPolicyHashFormat
_T11FcSpZoneSetDatabaseHashType_Object = MibTableColumn
t11FcSpZoneSetDatabaseHashType = _T11FcSpZoneSetDatabaseHashType_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 1, 1, 1, 6),
    _T11FcSpZoneSetDatabaseHashType_Type()
)
t11FcSpZoneSetDatabaseHashType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpZoneSetDatabaseHashType.setStatus("current")
_T11FcSpZoneSetDatabaseHash_Type = T11FcSpPolicyHashValue
_T11FcSpZoneSetDatabaseHash_Object = MibTableColumn
t11FcSpZoneSetDatabaseHash = _T11FcSpZoneSetDatabaseHash_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 1, 1, 1, 7),
    _T11FcSpZoneSetDatabaseHash_Type()
)
t11FcSpZoneSetDatabaseHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpZoneSetDatabaseHash.setStatus("current")
_T11FcSpZsNotifyControlTable_Object = MibTable
t11FcSpZsNotifyControlTable = _T11FcSpZsNotifyControlTable_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 1, 2)
)
if mibBuilder.loadTexts:
    t11FcSpZsNotifyControlTable.setStatus("current")
_T11FcSpZsNotifyControlEntry_Object = MibTableRow
t11FcSpZsNotifyControlEntry = _T11FcSpZsNotifyControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    t11FcSpZsNotifyControlEntry.setStatus("current")
_T11FcSpZsNotifyJoinSuccessEnable_Type = TruthValue
_T11FcSpZsNotifyJoinSuccessEnable_Object = MibTableColumn
t11FcSpZsNotifyJoinSuccessEnable = _T11FcSpZsNotifyJoinSuccessEnable_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 1, 2, 1, 1),
    _T11FcSpZsNotifyJoinSuccessEnable_Type()
)
t11FcSpZsNotifyJoinSuccessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpZsNotifyJoinSuccessEnable.setStatus("current")
_T11FcSpZsNotifyJoinFailureEnable_Type = TruthValue
_T11FcSpZsNotifyJoinFailureEnable_Object = MibTableColumn
t11FcSpZsNotifyJoinFailureEnable = _T11FcSpZsNotifyJoinFailureEnable_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 1, 2, 1, 2),
    _T11FcSpZsNotifyJoinFailureEnable_Type()
)
t11FcSpZsNotifyJoinFailureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpZsNotifyJoinFailureEnable.setStatus("current")
_T11FcSpZsStatistics_ObjectIdentity = ObjectIdentity
t11FcSpZsStatistics = _T11FcSpZsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 177, 1, 2)
)
_T11FcSpZsStatsTable_Object = MibTable
t11FcSpZsStatsTable = _T11FcSpZsStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 2, 1)
)
if mibBuilder.loadTexts:
    t11FcSpZsStatsTable.setStatus("current")
_T11FcSpZsStatsEntry_Object = MibTableRow
t11FcSpZsStatsEntry = _T11FcSpZsStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcSpZsStatsEntry.setStatus("current")
_T11FcSpZsSPCMITrequestsSent_Type = Counter32
_T11FcSpZsSPCMITrequestsSent_Object = MibTableColumn
t11FcSpZsSPCMITrequestsSent = _T11FcSpZsSPCMITrequestsSent_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1, 1),
    _T11FcSpZsSPCMITrequestsSent_Type()
)
t11FcSpZsSPCMITrequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpZsSPCMITrequestsSent.setStatus("current")
_T11FcSpZsSPCMITrequestsAccepted_Type = Counter32
_T11FcSpZsSPCMITrequestsAccepted_Object = MibTableColumn
t11FcSpZsSPCMITrequestsAccepted = _T11FcSpZsSPCMITrequestsAccepted_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1, 2),
    _T11FcSpZsSPCMITrequestsAccepted_Type()
)
t11FcSpZsSPCMITrequestsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpZsSPCMITrequestsAccepted.setStatus("current")
_T11FcSpZsSPCMITrequestsRejected_Type = Counter32
_T11FcSpZsSPCMITrequestsRejected_Object = MibTableColumn
t11FcSpZsSPCMITrequestsRejected = _T11FcSpZsSPCMITrequestsRejected_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1, 3),
    _T11FcSpZsSPCMITrequestsRejected_Type()
)
t11FcSpZsSPCMITrequestsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpZsSPCMITrequestsRejected.setStatus("current")
_T11FcSpZsZcpRequestsSent_Type = Counter32
_T11FcSpZsZcpRequestsSent_Object = MibTableColumn
t11FcSpZsZcpRequestsSent = _T11FcSpZsZcpRequestsSent_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1, 4),
    _T11FcSpZsZcpRequestsSent_Type()
)
t11FcSpZsZcpRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpZsZcpRequestsSent.setStatus("current")
_T11FcSpZsZcpRequestsAccepted_Type = Counter32
_T11FcSpZsZcpRequestsAccepted_Object = MibTableColumn
t11FcSpZsZcpRequestsAccepted = _T11FcSpZsZcpRequestsAccepted_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1, 5),
    _T11FcSpZsZcpRequestsAccepted_Type()
)
t11FcSpZsZcpRequestsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpZsZcpRequestsAccepted.setStatus("current")
_T11FcSpZsZcpRequestsRejected_Type = Counter32
_T11FcSpZsZcpRequestsRejected_Object = MibTableColumn
t11FcSpZsZcpRequestsRejected = _T11FcSpZsZcpRequestsRejected_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1, 6),
    _T11FcSpZsZcpRequestsRejected_Type()
)
t11FcSpZsZcpRequestsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpZsZcpRequestsRejected.setStatus("current")
_T11FcSpZsZirRequestsAccepted_Type = Counter32
_T11FcSpZsZirRequestsAccepted_Object = MibTableColumn
t11FcSpZsZirRequestsAccepted = _T11FcSpZsZirRequestsAccepted_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1, 7),
    _T11FcSpZsZirRequestsAccepted_Type()
)
t11FcSpZsZirRequestsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpZsZirRequestsAccepted.setStatus("current")
_T11FcSpZsZirRequestsRejected_Type = Counter32
_T11FcSpZsZirRequestsRejected_Object = MibTableColumn
t11FcSpZsZirRequestsRejected = _T11FcSpZsZirRequestsRejected_Object(
    (1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1, 8),
    _T11FcSpZsZirRequestsRejected_Type()
)
t11FcSpZsZirRequestsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpZsZirRequestsRejected.setStatus("current")
_T11FcSpZsMIBConformance_ObjectIdentity = ObjectIdentity
t11FcSpZsMIBConformance = _T11FcSpZsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 177, 2)
)
_T11FcSpZsMIBCompliances_ObjectIdentity = ObjectIdentity
t11FcSpZsMIBCompliances = _T11FcSpZsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 177, 2, 1)
)
_T11FcSpZsMIBGroups_ObjectIdentity = ObjectIdentity
t11FcSpZsMIBGroups = _T11FcSpZsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 177, 2, 2)
)
t11ZsServerEntry.registerAugmentions(
    ("T11-FC-SP-ZONING-MIB",
     "t11FcSpZsServerEntry")
)
t11FcSpZsServerEntry.setIndexNames(*t11ZsServerEntry.getIndexNames())
t11ZsNotifyControlEntry.registerAugmentions(
    ("T11-FC-SP-ZONING-MIB",
     "t11FcSpZsNotifyControlEntry")
)
t11FcSpZsNotifyControlEntry.setIndexNames(*t11ZsNotifyControlEntry.getIndexNames())
t11ZsStatsEntry.registerAugmentions(
    ("T11-FC-SP-ZONING-MIB",
     "t11FcSpZsStatsEntry")
)
t11FcSpZsStatsEntry.setIndexNames(*t11ZsStatsEntry.getIndexNames())

# Managed Objects groups

t11FcSpZsObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 177, 2, 2, 1)
)
t11FcSpZsObjectsGroup.setObjects(
      *(("T11-FC-SP-ZONING-MIB", "t11FcSpZsServerCapabilityObject"),
        ("T11-FC-SP-ZONING-MIB", "t11FcSpZsServerEnabled"),
        ("T11-FC-SP-ZONING-MIB", "t11FcSpZoneSetHashStatus"),
        ("T11-FC-SP-ZONING-MIB", "t11FcSpActiveZoneSetHashType"),
        ("T11-FC-SP-ZONING-MIB", "t11FcSpActiveZoneSetHash"),
        ("T11-FC-SP-ZONING-MIB", "t11FcSpZoneSetDatabaseHashType"),
        ("T11-FC-SP-ZONING-MIB", "t11FcSpZoneSetDatabaseHash"))
)
if mibBuilder.loadTexts:
    t11FcSpZsObjectsGroup.setStatus("current")

t11FcSpZsNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 177, 2, 2, 2)
)
t11FcSpZsNotificationControlGroup.setObjects(
      *(("T11-FC-SP-ZONING-MIB", "t11FcSpZsNotifyJoinSuccessEnable"),
        ("T11-FC-SP-ZONING-MIB", "t11FcSpZsNotifyJoinFailureEnable"))
)
if mibBuilder.loadTexts:
    t11FcSpZsNotificationControlGroup.setStatus("current")

t11FcSpZsStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 177, 2, 2, 3)
)
t11FcSpZsStatisticsGroup.setObjects(
      *(("T11-FC-SP-ZONING-MIB", "t11FcSpZsSPCMITrequestsSent"),
        ("T11-FC-SP-ZONING-MIB", "t11FcSpZsSPCMITrequestsAccepted"),
        ("T11-FC-SP-ZONING-MIB", "t11FcSpZsSPCMITrequestsRejected"),
        ("T11-FC-SP-ZONING-MIB", "t11FcSpZsZcpRequestsSent"),
        ("T11-FC-SP-ZONING-MIB", "t11FcSpZsZcpRequestsAccepted"),
        ("T11-FC-SP-ZONING-MIB", "t11FcSpZsZcpRequestsRejected"),
        ("T11-FC-SP-ZONING-MIB", "t11FcSpZsZirRequestsAccepted"),
        ("T11-FC-SP-ZONING-MIB", "t11FcSpZsZirRequestsRejected"))
)
if mibBuilder.loadTexts:
    t11FcSpZsStatisticsGroup.setStatus("current")


# Notification objects

t11FcSpZsFabricJoinSuccessNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 177, 0, 1)
)
t11FcSpZsFabricJoinSuccessNotify.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsFabricIndex"))
)
if mibBuilder.loadTexts:
    t11FcSpZsFabricJoinSuccessNotify.setStatus(
        "current"
    )

t11FcSpZsFabricJoinFailureNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 177, 0, 2)
)
t11FcSpZsFabricJoinFailureNotify.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsFabricIndex"))
)
if mibBuilder.loadTexts:
    t11FcSpZsFabricJoinFailureNotify.setStatus(
        "current"
    )


# Notifications groups

t11FcSpZsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 177, 2, 2, 4)
)
t11FcSpZsNotificationGroup.setObjects(
      *(("T11-FC-SP-ZONING-MIB", "t11FcSpZsFabricJoinSuccessNotify"),
        ("T11-FC-SP-ZONING-MIB", "t11FcSpZsFabricJoinFailureNotify"))
)
if mibBuilder.loadTexts:
    t11FcSpZsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

t11FcSpZsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 177, 2, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcSpZsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T11-FC-SP-ZONING-MIB",
    **{"t11FcSpZoningMIB": t11FcSpZoningMIB,
       "t11FcSpZsMIBNotifications": t11FcSpZsMIBNotifications,
       "t11FcSpZsFabricJoinSuccessNotify": t11FcSpZsFabricJoinSuccessNotify,
       "t11FcSpZsFabricJoinFailureNotify": t11FcSpZsFabricJoinFailureNotify,
       "t11FcSpZsMIBObjects": t11FcSpZsMIBObjects,
       "t11FcSpZsConfiguration": t11FcSpZsConfiguration,
       "t11FcSpZsServerTable": t11FcSpZsServerTable,
       "t11FcSpZsServerEntry": t11FcSpZsServerEntry,
       "t11FcSpZsServerCapabilityObject": t11FcSpZsServerCapabilityObject,
       "t11FcSpZsServerEnabled": t11FcSpZsServerEnabled,
       "t11FcSpZoneSetHashStatus": t11FcSpZoneSetHashStatus,
       "t11FcSpActiveZoneSetHashType": t11FcSpActiveZoneSetHashType,
       "t11FcSpActiveZoneSetHash": t11FcSpActiveZoneSetHash,
       "t11FcSpZoneSetDatabaseHashType": t11FcSpZoneSetDatabaseHashType,
       "t11FcSpZoneSetDatabaseHash": t11FcSpZoneSetDatabaseHash,
       "t11FcSpZsNotifyControlTable": t11FcSpZsNotifyControlTable,
       "t11FcSpZsNotifyControlEntry": t11FcSpZsNotifyControlEntry,
       "t11FcSpZsNotifyJoinSuccessEnable": t11FcSpZsNotifyJoinSuccessEnable,
       "t11FcSpZsNotifyJoinFailureEnable": t11FcSpZsNotifyJoinFailureEnable,
       "t11FcSpZsStatistics": t11FcSpZsStatistics,
       "t11FcSpZsStatsTable": t11FcSpZsStatsTable,
       "t11FcSpZsStatsEntry": t11FcSpZsStatsEntry,
       "t11FcSpZsSPCMITrequestsSent": t11FcSpZsSPCMITrequestsSent,
       "t11FcSpZsSPCMITrequestsAccepted": t11FcSpZsSPCMITrequestsAccepted,
       "t11FcSpZsSPCMITrequestsRejected": t11FcSpZsSPCMITrequestsRejected,
       "t11FcSpZsZcpRequestsSent": t11FcSpZsZcpRequestsSent,
       "t11FcSpZsZcpRequestsAccepted": t11FcSpZsZcpRequestsAccepted,
       "t11FcSpZsZcpRequestsRejected": t11FcSpZsZcpRequestsRejected,
       "t11FcSpZsZirRequestsAccepted": t11FcSpZsZirRequestsAccepted,
       "t11FcSpZsZirRequestsRejected": t11FcSpZsZirRequestsRejected,
       "t11FcSpZsMIBConformance": t11FcSpZsMIBConformance,
       "t11FcSpZsMIBCompliances": t11FcSpZsMIBCompliances,
       "t11FcSpZsMIBCompliance": t11FcSpZsMIBCompliance,
       "t11FcSpZsMIBGroups": t11FcSpZsMIBGroups,
       "t11FcSpZsObjectsGroup": t11FcSpZsObjectsGroup,
       "t11FcSpZsNotificationControlGroup": t11FcSpZsNotificationControlGroup,
       "t11FcSpZsStatisticsGroup": t11FcSpZsStatisticsGroup,
       "t11FcSpZsNotificationGroup": t11FcSpZsNotificationGroup}
)
