# SNMP MIB module (CISCO-UNIFIED-COMPUTING-LSMAINT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-LSMAINT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:53 2024
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

(CucsLsConfigIssues,
 CucsLsmaintAckChangeDetails,
 CucsLsmaintAckChanges,
 CucsLsmaintAckDisr,
 CucsLsmaintChangeMode,
 CucsPolicyPolicyOwner,
 CucsTrigAckMode,
 CucsTrigAckOperState,
 CucsTrigAckPrevOperState,
 CucsTrigAdminState,
 CucsTrigTrigState,
 CucsTrigTrigger) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsLsConfigIssues",
    "CucsLsmaintAckChangeDetails",
    "CucsLsmaintAckChanges",
    "CucsLsmaintAckDisr",
    "CucsLsmaintChangeMode",
    "CucsPolicyPolicyOwner",
    "CucsTrigAckMode",
    "CucsTrigAckOperState",
    "CucsTrigAckPrevOperState",
    "CucsTrigAdminState",
    "CucsTrigTrigState",
    "CucsTrigTrigger")

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

cucsLsmaintObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsLsmaintAckTable_Object = MibTable
cucsLsmaintAckTable = _CucsLsmaintAckTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1)
)
if mibBuilder.loadTexts:
    cucsLsmaintAckTable.setStatus("current")
_CucsLsmaintAckEntry_Object = MibTableRow
cucsLsmaintAckEntry = _CucsLsmaintAckEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1)
)
cucsLsmaintAckEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSMAINT-MIB", "cucsLsmaintAckInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsmaintAckEntry.setStatus("current")
_CucsLsmaintAckInstanceId_Type = CucsManagedObjectId
_CucsLsmaintAckInstanceId_Object = MibTableColumn
cucsLsmaintAckInstanceId = _CucsLsmaintAckInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 1),
    _CucsLsmaintAckInstanceId_Type()
)
cucsLsmaintAckInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsmaintAckInstanceId.setStatus("current")
_CucsLsmaintAckDn_Type = CucsManagedObjectDn
_CucsLsmaintAckDn_Object = MibTableColumn
cucsLsmaintAckDn = _CucsLsmaintAckDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 2),
    _CucsLsmaintAckDn_Type()
)
cucsLsmaintAckDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckDn.setStatus("current")
_CucsLsmaintAckRn_Type = SnmpAdminString
_CucsLsmaintAckRn_Object = MibTableColumn
cucsLsmaintAckRn = _CucsLsmaintAckRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 3),
    _CucsLsmaintAckRn_Type()
)
cucsLsmaintAckRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckRn.setStatus("current")
_CucsLsmaintAckAcked_Type = DateAndTime
_CucsLsmaintAckAcked_Object = MibTableColumn
cucsLsmaintAckAcked = _CucsLsmaintAckAcked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 4),
    _CucsLsmaintAckAcked_Type()
)
cucsLsmaintAckAcked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckAcked.setStatus("current")
_CucsLsmaintAckAckedBy_Type = SnmpAdminString
_CucsLsmaintAckAckedBy_Object = MibTableColumn
cucsLsmaintAckAckedBy = _CucsLsmaintAckAckedBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 5),
    _CucsLsmaintAckAckedBy_Type()
)
cucsLsmaintAckAckedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckAckedBy.setStatus("current")
_CucsLsmaintAckAdminState_Type = CucsTrigAdminState
_CucsLsmaintAckAdminState_Object = MibTableColumn
cucsLsmaintAckAdminState = _CucsLsmaintAckAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 6),
    _CucsLsmaintAckAdminState_Type()
)
cucsLsmaintAckAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckAdminState.setStatus("current")
_CucsLsmaintAckChangeBy_Type = SnmpAdminString
_CucsLsmaintAckChangeBy_Object = MibTableColumn
cucsLsmaintAckChangeBy = _CucsLsmaintAckChangeBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 7),
    _CucsLsmaintAckChangeBy_Type()
)
cucsLsmaintAckChangeBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckChangeBy.setStatus("current")
_CucsLsmaintAckChanges_Type = CucsLsmaintAckChanges
_CucsLsmaintAckChanges_Object = MibTableColumn
cucsLsmaintAckChanges = _CucsLsmaintAckChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 8),
    _CucsLsmaintAckChanges_Type()
)
cucsLsmaintAckChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckChanges.setStatus("current")
_CucsLsmaintAckDescr_Type = SnmpAdminString
_CucsLsmaintAckDescr_Object = MibTableColumn
cucsLsmaintAckDescr = _CucsLsmaintAckDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 9),
    _CucsLsmaintAckDescr_Type()
)
cucsLsmaintAckDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckDescr.setStatus("current")
_CucsLsmaintAckDisr_Type = CucsLsmaintAckDisr
_CucsLsmaintAckDisr_Object = MibTableColumn
cucsLsmaintAckDisr = _CucsLsmaintAckDisr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 10),
    _CucsLsmaintAckDisr_Type()
)
cucsLsmaintAckDisr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckDisr.setStatus("current")
_CucsLsmaintAckIntId_Type = SnmpAdminString
_CucsLsmaintAckIntId_Object = MibTableColumn
cucsLsmaintAckIntId = _CucsLsmaintAckIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 11),
    _CucsLsmaintAckIntId_Type()
)
cucsLsmaintAckIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckIntId.setStatus("current")
_CucsLsmaintAckModified_Type = DateAndTime
_CucsLsmaintAckModified_Object = MibTableColumn
cucsLsmaintAckModified = _CucsLsmaintAckModified_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 12),
    _CucsLsmaintAckModified_Type()
)
cucsLsmaintAckModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckModified.setStatus("current")
_CucsLsmaintAckName_Type = SnmpAdminString
_CucsLsmaintAckName_Object = MibTableColumn
cucsLsmaintAckName = _CucsLsmaintAckName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 13),
    _CucsLsmaintAckName_Type()
)
cucsLsmaintAckName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckName.setStatus("current")
_CucsLsmaintAckOperState_Type = CucsTrigAckOperState
_CucsLsmaintAckOperState_Object = MibTableColumn
cucsLsmaintAckOperState = _CucsLsmaintAckOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 14),
    _CucsLsmaintAckOperState_Type()
)
cucsLsmaintAckOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckOperState.setStatus("current")
_CucsLsmaintAckScheduler_Type = SnmpAdminString
_CucsLsmaintAckScheduler_Object = MibTableColumn
cucsLsmaintAckScheduler = _CucsLsmaintAckScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 15),
    _CucsLsmaintAckScheduler_Type()
)
cucsLsmaintAckScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckScheduler.setStatus("current")
_CucsLsmaintAckChangeDetails_Type = CucsLsmaintAckChangeDetails
_CucsLsmaintAckChangeDetails_Object = MibTableColumn
cucsLsmaintAckChangeDetails = _CucsLsmaintAckChangeDetails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 16),
    _CucsLsmaintAckChangeDetails_Type()
)
cucsLsmaintAckChangeDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckChangeDetails.setStatus("current")
_CucsLsmaintAckChangeMode_Type = CucsLsmaintChangeMode
_CucsLsmaintAckChangeMode_Object = MibTableColumn
cucsLsmaintAckChangeMode = _CucsLsmaintAckChangeMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 17),
    _CucsLsmaintAckChangeMode_Type()
)
cucsLsmaintAckChangeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckChangeMode.setStatus("current")
_CucsLsmaintAckConfigIssues_Type = CucsLsConfigIssues
_CucsLsmaintAckConfigIssues_Object = MibTableColumn
cucsLsmaintAckConfigIssues = _CucsLsmaintAckConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 18),
    _CucsLsmaintAckConfigIssues_Type()
)
cucsLsmaintAckConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckConfigIssues.setStatus("current")
_CucsLsmaintAckOldPnDn_Type = SnmpAdminString
_CucsLsmaintAckOldPnDn_Object = MibTableColumn
cucsLsmaintAckOldPnDn = _CucsLsmaintAckOldPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 19),
    _CucsLsmaintAckOldPnDn_Type()
)
cucsLsmaintAckOldPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckOldPnDn.setStatus("current")
_CucsLsmaintAckDeploymentMode_Type = CucsTrigAckMode
_CucsLsmaintAckDeploymentMode_Object = MibTableColumn
cucsLsmaintAckDeploymentMode = _CucsLsmaintAckDeploymentMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 20),
    _CucsLsmaintAckDeploymentMode_Type()
)
cucsLsmaintAckDeploymentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckDeploymentMode.setStatus("current")
_CucsLsmaintAckAutoDelete_Type = TruthValue
_CucsLsmaintAckAutoDelete_Object = MibTableColumn
cucsLsmaintAckAutoDelete = _CucsLsmaintAckAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 21),
    _CucsLsmaintAckAutoDelete_Type()
)
cucsLsmaintAckAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckAutoDelete.setStatus("current")
_CucsLsmaintAckIgnoreCap_Type = TruthValue
_CucsLsmaintAckIgnoreCap_Object = MibTableColumn
cucsLsmaintAckIgnoreCap = _CucsLsmaintAckIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 22),
    _CucsLsmaintAckIgnoreCap_Type()
)
cucsLsmaintAckIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckIgnoreCap.setStatus("current")
_CucsLsmaintAckOperScheduler_Type = SnmpAdminString
_CucsLsmaintAckOperScheduler_Object = MibTableColumn
cucsLsmaintAckOperScheduler = _CucsLsmaintAckOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 23),
    _CucsLsmaintAckOperScheduler_Type()
)
cucsLsmaintAckOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckOperScheduler.setStatus("current")
_CucsLsmaintAckPolicyLevel_Type = Gauge32
_CucsLsmaintAckPolicyLevel_Object = MibTableColumn
cucsLsmaintAckPolicyLevel = _CucsLsmaintAckPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 24),
    _CucsLsmaintAckPolicyLevel_Type()
)
cucsLsmaintAckPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckPolicyLevel.setStatus("current")
_CucsLsmaintAckPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsLsmaintAckPolicyOwner_Object = MibTableColumn
cucsLsmaintAckPolicyOwner = _CucsLsmaintAckPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 25),
    _CucsLsmaintAckPolicyOwner_Type()
)
cucsLsmaintAckPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckPolicyOwner.setStatus("current")
_CucsLsmaintAckPrevOperState_Type = CucsTrigAckPrevOperState
_CucsLsmaintAckPrevOperState_Object = MibTableColumn
cucsLsmaintAckPrevOperState = _CucsLsmaintAckPrevOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 26),
    _CucsLsmaintAckPrevOperState_Type()
)
cucsLsmaintAckPrevOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckPrevOperState.setStatus("current")
_CucsLsmaintAckPropAcl_Type = Unsigned64
_CucsLsmaintAckPropAcl_Object = MibTableColumn
cucsLsmaintAckPropAcl = _CucsLsmaintAckPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 27),
    _CucsLsmaintAckPropAcl_Type()
)
cucsLsmaintAckPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckPropAcl.setStatus("current")
_CucsLsmaintAckTriggerConfigState_Type = CucsTrigTrigState
_CucsLsmaintAckTriggerConfigState_Object = MibTableColumn
cucsLsmaintAckTriggerConfigState = _CucsLsmaintAckTriggerConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 1, 1, 28),
    _CucsLsmaintAckTriggerConfigState_Type()
)
cucsLsmaintAckTriggerConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintAckTriggerConfigState.setStatus("current")
_CucsLsmaintMaintPolicyTable_Object = MibTable
cucsLsmaintMaintPolicyTable = _CucsLsmaintMaintPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 2)
)
if mibBuilder.loadTexts:
    cucsLsmaintMaintPolicyTable.setStatus("current")
_CucsLsmaintMaintPolicyEntry_Object = MibTableRow
cucsLsmaintMaintPolicyEntry = _CucsLsmaintMaintPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 2, 1)
)
cucsLsmaintMaintPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSMAINT-MIB", "cucsLsmaintMaintPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsmaintMaintPolicyEntry.setStatus("current")
_CucsLsmaintMaintPolicyInstanceId_Type = CucsManagedObjectId
_CucsLsmaintMaintPolicyInstanceId_Object = MibTableColumn
cucsLsmaintMaintPolicyInstanceId = _CucsLsmaintMaintPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 2, 1, 1),
    _CucsLsmaintMaintPolicyInstanceId_Type()
)
cucsLsmaintMaintPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsmaintMaintPolicyInstanceId.setStatus("current")
_CucsLsmaintMaintPolicyDn_Type = CucsManagedObjectDn
_CucsLsmaintMaintPolicyDn_Object = MibTableColumn
cucsLsmaintMaintPolicyDn = _CucsLsmaintMaintPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 2, 1, 2),
    _CucsLsmaintMaintPolicyDn_Type()
)
cucsLsmaintMaintPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintMaintPolicyDn.setStatus("current")
_CucsLsmaintMaintPolicyRn_Type = SnmpAdminString
_CucsLsmaintMaintPolicyRn_Object = MibTableColumn
cucsLsmaintMaintPolicyRn = _CucsLsmaintMaintPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 2, 1, 3),
    _CucsLsmaintMaintPolicyRn_Type()
)
cucsLsmaintMaintPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintMaintPolicyRn.setStatus("current")
_CucsLsmaintMaintPolicyUptimeDisr_Type = CucsTrigAckMode
_CucsLsmaintMaintPolicyUptimeDisr_Object = MibTableColumn
cucsLsmaintMaintPolicyUptimeDisr = _CucsLsmaintMaintPolicyUptimeDisr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 2, 1, 4),
    _CucsLsmaintMaintPolicyUptimeDisr_Type()
)
cucsLsmaintMaintPolicyUptimeDisr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintMaintPolicyUptimeDisr.setStatus("current")
_CucsLsmaintMaintPolicySchedName_Type = SnmpAdminString
_CucsLsmaintMaintPolicySchedName_Object = MibTableColumn
cucsLsmaintMaintPolicySchedName = _CucsLsmaintMaintPolicySchedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 2, 1, 5),
    _CucsLsmaintMaintPolicySchedName_Type()
)
cucsLsmaintMaintPolicySchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintMaintPolicySchedName.setStatus("current")
_CucsLsmaintMaintPolicyDescr_Type = SnmpAdminString
_CucsLsmaintMaintPolicyDescr_Object = MibTableColumn
cucsLsmaintMaintPolicyDescr = _CucsLsmaintMaintPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 2, 1, 6),
    _CucsLsmaintMaintPolicyDescr_Type()
)
cucsLsmaintMaintPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintMaintPolicyDescr.setStatus("current")
_CucsLsmaintMaintPolicyName_Type = SnmpAdminString
_CucsLsmaintMaintPolicyName_Object = MibTableColumn
cucsLsmaintMaintPolicyName = _CucsLsmaintMaintPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 2, 1, 7),
    _CucsLsmaintMaintPolicyName_Type()
)
cucsLsmaintMaintPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintMaintPolicyName.setStatus("current")
_CucsLsmaintMaintPolicyIntId_Type = SnmpAdminString
_CucsLsmaintMaintPolicyIntId_Object = MibTableColumn
cucsLsmaintMaintPolicyIntId = _CucsLsmaintMaintPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 2, 1, 8),
    _CucsLsmaintMaintPolicyIntId_Type()
)
cucsLsmaintMaintPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintMaintPolicyIntId.setStatus("current")
_CucsLsmaintMaintPolicyOperSchedName_Type = SnmpAdminString
_CucsLsmaintMaintPolicyOperSchedName_Object = MibTableColumn
cucsLsmaintMaintPolicyOperSchedName = _CucsLsmaintMaintPolicyOperSchedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 2, 1, 9),
    _CucsLsmaintMaintPolicyOperSchedName_Type()
)
cucsLsmaintMaintPolicyOperSchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintMaintPolicyOperSchedName.setStatus("current")
_CucsLsmaintMaintPolicyPolicyLevel_Type = Gauge32
_CucsLsmaintMaintPolicyPolicyLevel_Object = MibTableColumn
cucsLsmaintMaintPolicyPolicyLevel = _CucsLsmaintMaintPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 2, 1, 10),
    _CucsLsmaintMaintPolicyPolicyLevel_Type()
)
cucsLsmaintMaintPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintMaintPolicyPolicyLevel.setStatus("current")
_CucsLsmaintMaintPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsLsmaintMaintPolicyPolicyOwner_Object = MibTableColumn
cucsLsmaintMaintPolicyPolicyOwner = _CucsLsmaintMaintPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 2, 1, 11),
    _CucsLsmaintMaintPolicyPolicyOwner_Type()
)
cucsLsmaintMaintPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintMaintPolicyPolicyOwner.setStatus("current")
_CucsLsmaintMaintPolicyTriggerConfig_Type = CucsTrigTrigger
_CucsLsmaintMaintPolicyTriggerConfig_Object = MibTableColumn
cucsLsmaintMaintPolicyTriggerConfig = _CucsLsmaintMaintPolicyTriggerConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 28, 2, 1, 12),
    _CucsLsmaintMaintPolicyTriggerConfig_Type()
)
cucsLsmaintMaintPolicyTriggerConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsmaintMaintPolicyTriggerConfig.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-LSMAINT-MIB",
    **{"cucsLsmaintObjects": cucsLsmaintObjects,
       "cucsLsmaintAckTable": cucsLsmaintAckTable,
       "cucsLsmaintAckEntry": cucsLsmaintAckEntry,
       "cucsLsmaintAckInstanceId": cucsLsmaintAckInstanceId,
       "cucsLsmaintAckDn": cucsLsmaintAckDn,
       "cucsLsmaintAckRn": cucsLsmaintAckRn,
       "cucsLsmaintAckAcked": cucsLsmaintAckAcked,
       "cucsLsmaintAckAckedBy": cucsLsmaintAckAckedBy,
       "cucsLsmaintAckAdminState": cucsLsmaintAckAdminState,
       "cucsLsmaintAckChangeBy": cucsLsmaintAckChangeBy,
       "cucsLsmaintAckChanges": cucsLsmaintAckChanges,
       "cucsLsmaintAckDescr": cucsLsmaintAckDescr,
       "cucsLsmaintAckDisr": cucsLsmaintAckDisr,
       "cucsLsmaintAckIntId": cucsLsmaintAckIntId,
       "cucsLsmaintAckModified": cucsLsmaintAckModified,
       "cucsLsmaintAckName": cucsLsmaintAckName,
       "cucsLsmaintAckOperState": cucsLsmaintAckOperState,
       "cucsLsmaintAckScheduler": cucsLsmaintAckScheduler,
       "cucsLsmaintAckChangeDetails": cucsLsmaintAckChangeDetails,
       "cucsLsmaintAckChangeMode": cucsLsmaintAckChangeMode,
       "cucsLsmaintAckConfigIssues": cucsLsmaintAckConfigIssues,
       "cucsLsmaintAckOldPnDn": cucsLsmaintAckOldPnDn,
       "cucsLsmaintAckDeploymentMode": cucsLsmaintAckDeploymentMode,
       "cucsLsmaintAckAutoDelete": cucsLsmaintAckAutoDelete,
       "cucsLsmaintAckIgnoreCap": cucsLsmaintAckIgnoreCap,
       "cucsLsmaintAckOperScheduler": cucsLsmaintAckOperScheduler,
       "cucsLsmaintAckPolicyLevel": cucsLsmaintAckPolicyLevel,
       "cucsLsmaintAckPolicyOwner": cucsLsmaintAckPolicyOwner,
       "cucsLsmaintAckPrevOperState": cucsLsmaintAckPrevOperState,
       "cucsLsmaintAckPropAcl": cucsLsmaintAckPropAcl,
       "cucsLsmaintAckTriggerConfigState": cucsLsmaintAckTriggerConfigState,
       "cucsLsmaintMaintPolicyTable": cucsLsmaintMaintPolicyTable,
       "cucsLsmaintMaintPolicyEntry": cucsLsmaintMaintPolicyEntry,
       "cucsLsmaintMaintPolicyInstanceId": cucsLsmaintMaintPolicyInstanceId,
       "cucsLsmaintMaintPolicyDn": cucsLsmaintMaintPolicyDn,
       "cucsLsmaintMaintPolicyRn": cucsLsmaintMaintPolicyRn,
       "cucsLsmaintMaintPolicyUptimeDisr": cucsLsmaintMaintPolicyUptimeDisr,
       "cucsLsmaintMaintPolicySchedName": cucsLsmaintMaintPolicySchedName,
       "cucsLsmaintMaintPolicyDescr": cucsLsmaintMaintPolicyDescr,
       "cucsLsmaintMaintPolicyName": cucsLsmaintMaintPolicyName,
       "cucsLsmaintMaintPolicyIntId": cucsLsmaintMaintPolicyIntId,
       "cucsLsmaintMaintPolicyOperSchedName": cucsLsmaintMaintPolicyOperSchedName,
       "cucsLsmaintMaintPolicyPolicyLevel": cucsLsmaintMaintPolicyPolicyLevel,
       "cucsLsmaintMaintPolicyPolicyOwner": cucsLsmaintMaintPolicyPolicyOwner,
       "cucsLsmaintMaintPolicyTriggerConfig": cucsLsmaintMaintPolicyTriggerConfig}
)
