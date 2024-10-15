# SNMP MIB module (CISCO-UNIFIED-COMPUTING-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:11 2024
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
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsConfigImpactResponseState,
 CucsConfigSorterDirection,
 CucsLsConfigIssues,
 CucsLsConfigState,
 CucsMoMoClassId,
 CucsTrigAckChanges,
 CucsTrigAckMode) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConfigImpactResponseState",
    "CucsConfigSorterDirection",
    "CucsLsConfigIssues",
    "CucsLsConfigState",
    "CucsMoMoClassId",
    "CucsTrigAckChanges",
    "CucsTrigAckMode")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cucsConfigObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsConfigSorterTable_Object = MibTable
cucsConfigSorterTable = _CucsConfigSorterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 1)
)
if mibBuilder.loadTexts:
    cucsConfigSorterTable.setStatus("current")
_CucsConfigSorterEntry_Object = MibTableRow
cucsConfigSorterEntry = _CucsConfigSorterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 1, 1)
)
cucsConfigSorterEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CONFIG-MIB", "cucsConfigSorterInstanceId"),
)
if mibBuilder.loadTexts:
    cucsConfigSorterEntry.setStatus("current")
_CucsConfigSorterInstanceId_Type = CucsManagedObjectId
_CucsConfigSorterInstanceId_Object = MibTableColumn
cucsConfigSorterInstanceId = _CucsConfigSorterInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 1, 1, 1),
    _CucsConfigSorterInstanceId_Type()
)
cucsConfigSorterInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsConfigSorterInstanceId.setStatus("current")
_CucsConfigSorterDn_Type = CucsManagedObjectDn
_CucsConfigSorterDn_Object = MibTableColumn
cucsConfigSorterDn = _CucsConfigSorterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 1, 1, 2),
    _CucsConfigSorterDn_Type()
)
cucsConfigSorterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigSorterDn.setStatus("current")
_CucsConfigSorterRn_Type = SnmpAdminString
_CucsConfigSorterRn_Object = MibTableColumn
cucsConfigSorterRn = _CucsConfigSorterRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 1, 1, 3),
    _CucsConfigSorterRn_Type()
)
cucsConfigSorterRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigSorterRn.setStatus("current")
_CucsConfigSorterDirection_Type = CucsConfigSorterDirection
_CucsConfigSorterDirection_Object = MibTableColumn
cucsConfigSorterDirection = _CucsConfigSorterDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 1, 1, 4),
    _CucsConfigSorterDirection_Type()
)
cucsConfigSorterDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigSorterDirection.setStatus("current")
_CucsConfigSorterSortClass_Type = CucsMoMoClassId
_CucsConfigSorterSortClass_Object = MibTableColumn
cucsConfigSorterSortClass = _CucsConfigSorterSortClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 1, 1, 5),
    _CucsConfigSorterSortClass_Type()
)
cucsConfigSorterSortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigSorterSortClass.setStatus("current")
_CucsConfigSorterSortProp_Type = SnmpAdminString
_CucsConfigSorterSortProp_Object = MibTableColumn
cucsConfigSorterSortProp = _CucsConfigSorterSortProp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 1, 1, 6),
    _CucsConfigSorterSortProp_Type()
)
cucsConfigSorterSortProp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigSorterSortProp.setStatus("current")
_CucsConfigImpactTable_Object = MibTable
cucsConfigImpactTable = _CucsConfigImpactTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 2)
)
if mibBuilder.loadTexts:
    cucsConfigImpactTable.setStatus("current")
_CucsConfigImpactEntry_Object = MibTableRow
cucsConfigImpactEntry = _CucsConfigImpactEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 2, 1)
)
cucsConfigImpactEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CONFIG-MIB", "cucsConfigImpactInstanceId"),
)
if mibBuilder.loadTexts:
    cucsConfigImpactEntry.setStatus("current")
_CucsConfigImpactInstanceId_Type = CucsManagedObjectId
_CucsConfigImpactInstanceId_Object = MibTableColumn
cucsConfigImpactInstanceId = _CucsConfigImpactInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 2, 1, 1),
    _CucsConfigImpactInstanceId_Type()
)
cucsConfigImpactInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsConfigImpactInstanceId.setStatus("current")
_CucsConfigImpactDn_Type = CucsManagedObjectDn
_CucsConfigImpactDn_Object = MibTableColumn
cucsConfigImpactDn = _CucsConfigImpactDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 2, 1, 2),
    _CucsConfigImpactDn_Type()
)
cucsConfigImpactDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigImpactDn.setStatus("current")
_CucsConfigImpactRn_Type = SnmpAdminString
_CucsConfigImpactRn_Object = MibTableColumn
cucsConfigImpactRn = _CucsConfigImpactRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 2, 1, 3),
    _CucsConfigImpactRn_Type()
)
cucsConfigImpactRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigImpactRn.setStatus("current")
_CucsConfigImpactAffectedObj_Type = SnmpAdminString
_CucsConfigImpactAffectedObj_Object = MibTableColumn
cucsConfigImpactAffectedObj = _CucsConfigImpactAffectedObj_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 2, 1, 4),
    _CucsConfigImpactAffectedObj_Type()
)
cucsConfigImpactAffectedObj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigImpactAffectedObj.setStatus("current")
_CucsConfigImpactAffectedServer_Type = SnmpAdminString
_CucsConfigImpactAffectedServer_Object = MibTableColumn
cucsConfigImpactAffectedServer = _CucsConfigImpactAffectedServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 2, 1, 5),
    _CucsConfigImpactAffectedServer_Type()
)
cucsConfigImpactAffectedServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigImpactAffectedServer.setStatus("current")
_CucsConfigImpactChanges_Type = CucsTrigAckChanges
_CucsConfigImpactChanges_Object = MibTableColumn
cucsConfigImpactChanges = _CucsConfigImpactChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 2, 1, 6),
    _CucsConfigImpactChanges_Type()
)
cucsConfigImpactChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigImpactChanges.setStatus("current")
_CucsConfigImpactConfigIssues_Type = CucsLsConfigIssues
_CucsConfigImpactConfigIssues_Object = MibTableColumn
cucsConfigImpactConfigIssues = _CucsConfigImpactConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 2, 1, 7),
    _CucsConfigImpactConfigIssues_Type()
)
cucsConfigImpactConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigImpactConfigIssues.setStatus("current")
_CucsConfigImpactConfigQualifier_Type = CucsLsConfigIssues
_CucsConfigImpactConfigQualifier_Object = MibTableColumn
cucsConfigImpactConfigQualifier = _CucsConfigImpactConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 2, 1, 8),
    _CucsConfigImpactConfigQualifier_Type()
)
cucsConfigImpactConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigImpactConfigQualifier.setStatus("current")
_CucsConfigImpactConfigState_Type = CucsLsConfigState
_CucsConfigImpactConfigState_Object = MibTableColumn
cucsConfigImpactConfigState = _CucsConfigImpactConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 2, 1, 9),
    _CucsConfigImpactConfigState_Type()
)
cucsConfigImpactConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigImpactConfigState.setStatus("current")
_CucsConfigImpactDeploymentMode_Type = CucsTrigAckMode
_CucsConfigImpactDeploymentMode_Object = MibTableColumn
cucsConfigImpactDeploymentMode = _CucsConfigImpactDeploymentMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 2, 1, 10),
    _CucsConfigImpactDeploymentMode_Type()
)
cucsConfigImpactDeploymentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigImpactDeploymentMode.setStatus("current")
_CucsConfigImpactName_Type = SnmpAdminString
_CucsConfigImpactName_Object = MibTableColumn
cucsConfigImpactName = _CucsConfigImpactName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 2, 1, 11),
    _CucsConfigImpactName_Type()
)
cucsConfigImpactName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigImpactName.setStatus("current")
_CucsConfigImpactRebootRequired_Type = TruthValue
_CucsConfigImpactRebootRequired_Object = MibTableColumn
cucsConfigImpactRebootRequired = _CucsConfigImpactRebootRequired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 2, 1, 12),
    _CucsConfigImpactRebootRequired_Type()
)
cucsConfigImpactRebootRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigImpactRebootRequired.setStatus("current")
_CucsConfigManagedEpImpactResponseTable_Object = MibTable
cucsConfigManagedEpImpactResponseTable = _CucsConfigManagedEpImpactResponseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 3)
)
if mibBuilder.loadTexts:
    cucsConfigManagedEpImpactResponseTable.setStatus("current")
_CucsConfigManagedEpImpactResponseEntry_Object = MibTableRow
cucsConfigManagedEpImpactResponseEntry = _CucsConfigManagedEpImpactResponseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 3, 1)
)
cucsConfigManagedEpImpactResponseEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CONFIG-MIB", "cucsConfigManagedEpImpactResponseInstanceId"),
)
if mibBuilder.loadTexts:
    cucsConfigManagedEpImpactResponseEntry.setStatus("current")
_CucsConfigManagedEpImpactResponseInstanceId_Type = CucsManagedObjectId
_CucsConfigManagedEpImpactResponseInstanceId_Object = MibTableColumn
cucsConfigManagedEpImpactResponseInstanceId = _CucsConfigManagedEpImpactResponseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 3, 1, 1),
    _CucsConfigManagedEpImpactResponseInstanceId_Type()
)
cucsConfigManagedEpImpactResponseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsConfigManagedEpImpactResponseInstanceId.setStatus("current")
_CucsConfigManagedEpImpactResponseDn_Type = CucsManagedObjectDn
_CucsConfigManagedEpImpactResponseDn_Object = MibTableColumn
cucsConfigManagedEpImpactResponseDn = _CucsConfigManagedEpImpactResponseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 3, 1, 2),
    _CucsConfigManagedEpImpactResponseDn_Type()
)
cucsConfigManagedEpImpactResponseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigManagedEpImpactResponseDn.setStatus("current")
_CucsConfigManagedEpImpactResponseRn_Type = SnmpAdminString
_CucsConfigManagedEpImpactResponseRn_Object = MibTableColumn
cucsConfigManagedEpImpactResponseRn = _CucsConfigManagedEpImpactResponseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 3, 1, 3),
    _CucsConfigManagedEpImpactResponseRn_Type()
)
cucsConfigManagedEpImpactResponseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigManagedEpImpactResponseRn.setStatus("current")
_CucsConfigManagedEpImpactResponseAffectedServers_Type = Gauge32
_CucsConfigManagedEpImpactResponseAffectedServers_Object = MibTableColumn
cucsConfigManagedEpImpactResponseAffectedServers = _CucsConfigManagedEpImpactResponseAffectedServers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 3, 1, 4),
    _CucsConfigManagedEpImpactResponseAffectedServers_Type()
)
cucsConfigManagedEpImpactResponseAffectedServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigManagedEpImpactResponseAffectedServers.setStatus("current")
_CucsConfigManagedEpImpactResponseAppConnectorId_Type = Gauge32
_CucsConfigManagedEpImpactResponseAppConnectorId_Object = MibTableColumn
cucsConfigManagedEpImpactResponseAppConnectorId = _CucsConfigManagedEpImpactResponseAppConnectorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 3, 1, 5),
    _CucsConfigManagedEpImpactResponseAppConnectorId_Type()
)
cucsConfigManagedEpImpactResponseAppConnectorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigManagedEpImpactResponseAppConnectorId.setStatus("current")
_CucsConfigManagedEpImpactResponseEpName_Type = SnmpAdminString
_CucsConfigManagedEpImpactResponseEpName_Object = MibTableColumn
cucsConfigManagedEpImpactResponseEpName = _CucsConfigManagedEpImpactResponseEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 3, 1, 6),
    _CucsConfigManagedEpImpactResponseEpName_Type()
)
cucsConfigManagedEpImpactResponseEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigManagedEpImpactResponseEpName.setStatus("current")
_CucsConfigManagedEpImpactResponseImpactAnalyzerId_Type = DateAndTime
_CucsConfigManagedEpImpactResponseImpactAnalyzerId_Object = MibTableColumn
cucsConfigManagedEpImpactResponseImpactAnalyzerId = _CucsConfigManagedEpImpactResponseImpactAnalyzerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 3, 1, 7),
    _CucsConfigManagedEpImpactResponseImpactAnalyzerId_Type()
)
cucsConfigManagedEpImpactResponseImpactAnalyzerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigManagedEpImpactResponseImpactAnalyzerId.setStatus("current")
_CucsConfigManagedEpImpactResponseRebootRequired_Type = TruthValue
_CucsConfigManagedEpImpactResponseRebootRequired_Object = MibTableColumn
cucsConfigManagedEpImpactResponseRebootRequired = _CucsConfigManagedEpImpactResponseRebootRequired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 3, 1, 8),
    _CucsConfigManagedEpImpactResponseRebootRequired_Type()
)
cucsConfigManagedEpImpactResponseRebootRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigManagedEpImpactResponseRebootRequired.setStatus("current")
_CucsConfigManagedEpImpactResponseSourceConnectorId_Type = Gauge32
_CucsConfigManagedEpImpactResponseSourceConnectorId_Object = MibTableColumn
cucsConfigManagedEpImpactResponseSourceConnectorId = _CucsConfigManagedEpImpactResponseSourceConnectorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 3, 1, 9),
    _CucsConfigManagedEpImpactResponseSourceConnectorId_Type()
)
cucsConfigManagedEpImpactResponseSourceConnectorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigManagedEpImpactResponseSourceConnectorId.setStatus("current")
_CucsConfigManagedEpImpactResponseState_Type = CucsConfigImpactResponseState
_CucsConfigManagedEpImpactResponseState_Object = MibTableColumn
cucsConfigManagedEpImpactResponseState = _CucsConfigManagedEpImpactResponseState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 61, 3, 1, 10),
    _CucsConfigManagedEpImpactResponseState_Type()
)
cucsConfigManagedEpImpactResponseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsConfigManagedEpImpactResponseState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-CONFIG-MIB",
    **{"cucsConfigObjects": cucsConfigObjects,
       "cucsConfigSorterTable": cucsConfigSorterTable,
       "cucsConfigSorterEntry": cucsConfigSorterEntry,
       "cucsConfigSorterInstanceId": cucsConfigSorterInstanceId,
       "cucsConfigSorterDn": cucsConfigSorterDn,
       "cucsConfigSorterRn": cucsConfigSorterRn,
       "cucsConfigSorterDirection": cucsConfigSorterDirection,
       "cucsConfigSorterSortClass": cucsConfigSorterSortClass,
       "cucsConfigSorterSortProp": cucsConfigSorterSortProp,
       "cucsConfigImpactTable": cucsConfigImpactTable,
       "cucsConfigImpactEntry": cucsConfigImpactEntry,
       "cucsConfigImpactInstanceId": cucsConfigImpactInstanceId,
       "cucsConfigImpactDn": cucsConfigImpactDn,
       "cucsConfigImpactRn": cucsConfigImpactRn,
       "cucsConfigImpactAffectedObj": cucsConfigImpactAffectedObj,
       "cucsConfigImpactAffectedServer": cucsConfigImpactAffectedServer,
       "cucsConfigImpactChanges": cucsConfigImpactChanges,
       "cucsConfigImpactConfigIssues": cucsConfigImpactConfigIssues,
       "cucsConfigImpactConfigQualifier": cucsConfigImpactConfigQualifier,
       "cucsConfigImpactConfigState": cucsConfigImpactConfigState,
       "cucsConfigImpactDeploymentMode": cucsConfigImpactDeploymentMode,
       "cucsConfigImpactName": cucsConfigImpactName,
       "cucsConfigImpactRebootRequired": cucsConfigImpactRebootRequired,
       "cucsConfigManagedEpImpactResponseTable": cucsConfigManagedEpImpactResponseTable,
       "cucsConfigManagedEpImpactResponseEntry": cucsConfigManagedEpImpactResponseEntry,
       "cucsConfigManagedEpImpactResponseInstanceId": cucsConfigManagedEpImpactResponseInstanceId,
       "cucsConfigManagedEpImpactResponseDn": cucsConfigManagedEpImpactResponseDn,
       "cucsConfigManagedEpImpactResponseRn": cucsConfigManagedEpImpactResponseRn,
       "cucsConfigManagedEpImpactResponseAffectedServers": cucsConfigManagedEpImpactResponseAffectedServers,
       "cucsConfigManagedEpImpactResponseAppConnectorId": cucsConfigManagedEpImpactResponseAppConnectorId,
       "cucsConfigManagedEpImpactResponseEpName": cucsConfigManagedEpImpactResponseEpName,
       "cucsConfigManagedEpImpactResponseImpactAnalyzerId": cucsConfigManagedEpImpactResponseImpactAnalyzerId,
       "cucsConfigManagedEpImpactResponseRebootRequired": cucsConfigManagedEpImpactResponseRebootRequired,
       "cucsConfigManagedEpImpactResponseSourceConnectorId": cucsConfigManagedEpImpactResponseSourceConnectorId,
       "cucsConfigManagedEpImpactResponseState": cucsConfigManagedEpImpactResponseState}
)
