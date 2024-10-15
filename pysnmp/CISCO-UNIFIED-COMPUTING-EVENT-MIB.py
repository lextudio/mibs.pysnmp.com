# SNMP MIB module (CISCO-UNIFIED-COMPUTING-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-EVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:24 2024
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

(CucsConditionActionIndicator,
 CucsConditionCause,
 CucsConditionCode,
 CucsConditionRule,
 CucsConditionSeverity,
 CucsConditionTag,
 CucsConditionType,
 CucsEventEpCtrlLevel,
 CucsPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionActionIndicator",
    "CucsConditionCause",
    "CucsConditionCode",
    "CucsConditionRule",
    "CucsConditionSeverity",
    "CucsConditionTag",
    "CucsConditionType",
    "CucsEventEpCtrlLevel",
    "CucsPolicyPolicyOwner")

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

cucsEventObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsEventEpCtrlTable_Object = MibTable
cucsEventEpCtrlTable = _CucsEventEpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 1)
)
if mibBuilder.loadTexts:
    cucsEventEpCtrlTable.setStatus("current")
_CucsEventEpCtrlEntry_Object = MibTableRow
cucsEventEpCtrlEntry = _CucsEventEpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 1, 1)
)
cucsEventEpCtrlEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EVENT-MIB", "cucsEventEpCtrlInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEventEpCtrlEntry.setStatus("current")
_CucsEventEpCtrlInstanceId_Type = CucsManagedObjectId
_CucsEventEpCtrlInstanceId_Object = MibTableColumn
cucsEventEpCtrlInstanceId = _CucsEventEpCtrlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 1, 1, 1),
    _CucsEventEpCtrlInstanceId_Type()
)
cucsEventEpCtrlInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEventEpCtrlInstanceId.setStatus("current")
_CucsEventEpCtrlDn_Type = CucsManagedObjectDn
_CucsEventEpCtrlDn_Object = MibTableColumn
cucsEventEpCtrlDn = _CucsEventEpCtrlDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 1, 1, 2),
    _CucsEventEpCtrlDn_Type()
)
cucsEventEpCtrlDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventEpCtrlDn.setStatus("current")
_CucsEventEpCtrlRn_Type = SnmpAdminString
_CucsEventEpCtrlRn_Object = MibTableColumn
cucsEventEpCtrlRn = _CucsEventEpCtrlRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 1, 1, 3),
    _CucsEventEpCtrlRn_Type()
)
cucsEventEpCtrlRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventEpCtrlRn.setStatus("current")
_CucsEventEpCtrlLevel_Type = CucsEventEpCtrlLevel
_CucsEventEpCtrlLevel_Object = MibTableColumn
cucsEventEpCtrlLevel = _CucsEventEpCtrlLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 1, 1, 4),
    _CucsEventEpCtrlLevel_Type()
)
cucsEventEpCtrlLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventEpCtrlLevel.setStatus("current")
_CucsEventEpCtrlRevertTimeout_Type = TimeIntervalSec
_CucsEventEpCtrlRevertTimeout_Object = MibTableColumn
cucsEventEpCtrlRevertTimeout = _CucsEventEpCtrlRevertTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 1, 1, 5),
    _CucsEventEpCtrlRevertTimeout_Type()
)
cucsEventEpCtrlRevertTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventEpCtrlRevertTimeout.setStatus("current")
_CucsEventHolderTable_Object = MibTable
cucsEventHolderTable = _CucsEventHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 2)
)
if mibBuilder.loadTexts:
    cucsEventHolderTable.setStatus("current")
_CucsEventHolderEntry_Object = MibTableRow
cucsEventHolderEntry = _CucsEventHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 2, 1)
)
cucsEventHolderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EVENT-MIB", "cucsEventHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEventHolderEntry.setStatus("current")
_CucsEventHolderInstanceId_Type = CucsManagedObjectId
_CucsEventHolderInstanceId_Object = MibTableColumn
cucsEventHolderInstanceId = _CucsEventHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 2, 1, 1),
    _CucsEventHolderInstanceId_Type()
)
cucsEventHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEventHolderInstanceId.setStatus("current")
_CucsEventHolderDn_Type = CucsManagedObjectDn
_CucsEventHolderDn_Object = MibTableColumn
cucsEventHolderDn = _CucsEventHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 2, 1, 2),
    _CucsEventHolderDn_Type()
)
cucsEventHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventHolderDn.setStatus("current")
_CucsEventHolderRn_Type = SnmpAdminString
_CucsEventHolderRn_Object = MibTableColumn
cucsEventHolderRn = _CucsEventHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 2, 1, 3),
    _CucsEventHolderRn_Type()
)
cucsEventHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventHolderRn.setStatus("current")
_CucsEventHolderName_Type = SnmpAdminString
_CucsEventHolderName_Object = MibTableColumn
cucsEventHolderName = _CucsEventHolderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 2, 1, 4),
    _CucsEventHolderName_Type()
)
cucsEventHolderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventHolderName.setStatus("current")
_CucsEventInstTable_Object = MibTable
cucsEventInstTable = _CucsEventInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 3)
)
if mibBuilder.loadTexts:
    cucsEventInstTable.setStatus("current")
_CucsEventInstEntry_Object = MibTableRow
cucsEventInstEntry = _CucsEventInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 3, 1)
)
cucsEventInstEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EVENT-MIB", "cucsEventInstInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEventInstEntry.setStatus("current")
_CucsEventInstInstanceId_Type = CucsManagedObjectId
_CucsEventInstInstanceId_Object = MibTableColumn
cucsEventInstInstanceId = _CucsEventInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 3, 1, 1),
    _CucsEventInstInstanceId_Type()
)
cucsEventInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEventInstInstanceId.setStatus("current")
_CucsEventInstDn_Type = CucsManagedObjectDn
_CucsEventInstDn_Object = MibTableColumn
cucsEventInstDn = _CucsEventInstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 3, 1, 2),
    _CucsEventInstDn_Type()
)
cucsEventInstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventInstDn.setStatus("current")
_CucsEventInstRn_Type = SnmpAdminString
_CucsEventInstRn_Object = MibTableColumn
cucsEventInstRn = _CucsEventInstRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 3, 1, 3),
    _CucsEventInstRn_Type()
)
cucsEventInstRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventInstRn.setStatus("current")
_CucsEventInstCause_Type = CucsConditionCause
_CucsEventInstCause_Object = MibTableColumn
cucsEventInstCause = _CucsEventInstCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 3, 1, 4),
    _CucsEventInstCause_Type()
)
cucsEventInstCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventInstCause.setStatus("current")
_CucsEventInstChangeSet_Type = SnmpAdminString
_CucsEventInstChangeSet_Object = MibTableColumn
cucsEventInstChangeSet = _CucsEventInstChangeSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 3, 1, 5),
    _CucsEventInstChangeSet_Type()
)
cucsEventInstChangeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventInstChangeSet.setStatus("current")
_CucsEventInstCode_Type = CucsConditionCode
_CucsEventInstCode_Object = MibTableColumn
cucsEventInstCode = _CucsEventInstCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 3, 1, 6),
    _CucsEventInstCode_Type()
)
cucsEventInstCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventInstCode.setStatus("current")
_CucsEventInstCreated_Type = DateAndTime
_CucsEventInstCreated_Object = MibTableColumn
cucsEventInstCreated = _CucsEventInstCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 3, 1, 7),
    _CucsEventInstCreated_Type()
)
cucsEventInstCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventInstCreated.setStatus("current")
_CucsEventInstDescr_Type = SnmpAdminString
_CucsEventInstDescr_Object = MibTableColumn
cucsEventInstDescr = _CucsEventInstDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 3, 1, 8),
    _CucsEventInstDescr_Type()
)
cucsEventInstDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventInstDescr.setStatus("current")
_CucsEventInstId_Type = Unsigned64
_CucsEventInstId_Object = MibTableColumn
cucsEventInstId = _CucsEventInstId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 3, 1, 9),
    _CucsEventInstId_Type()
)
cucsEventInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventInstId.setStatus("current")
_CucsEventInstRule_Type = CucsConditionRule
_CucsEventInstRule_Object = MibTableColumn
cucsEventInstRule = _CucsEventInstRule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 3, 1, 10),
    _CucsEventInstRule_Type()
)
cucsEventInstRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventInstRule.setStatus("current")
_CucsEventInstSeverity_Type = CucsConditionSeverity
_CucsEventInstSeverity_Object = MibTableColumn
cucsEventInstSeverity = _CucsEventInstSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 3, 1, 11),
    _CucsEventInstSeverity_Type()
)
cucsEventInstSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventInstSeverity.setStatus("current")
_CucsEventInstTags_Type = CucsConditionTag
_CucsEventInstTags_Object = MibTableColumn
cucsEventInstTags = _CucsEventInstTags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 3, 1, 12),
    _CucsEventInstTags_Type()
)
cucsEventInstTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventInstTags.setStatus("current")
_CucsEventInstType_Type = CucsConditionType
_CucsEventInstType_Object = MibTableColumn
cucsEventInstType = _CucsEventInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 3, 1, 13),
    _CucsEventInstType_Type()
)
cucsEventInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventInstType.setStatus("current")
_CucsEventLogTable_Object = MibTable
cucsEventLogTable = _CucsEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 4)
)
if mibBuilder.loadTexts:
    cucsEventLogTable.setStatus("current")
_CucsEventLogEntry_Object = MibTableRow
cucsEventLogEntry = _CucsEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 4, 1)
)
cucsEventLogEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EVENT-MIB", "cucsEventLogInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEventLogEntry.setStatus("current")
_CucsEventLogInstanceId_Type = CucsManagedObjectId
_CucsEventLogInstanceId_Object = MibTableColumn
cucsEventLogInstanceId = _CucsEventLogInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 4, 1, 1),
    _CucsEventLogInstanceId_Type()
)
cucsEventLogInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEventLogInstanceId.setStatus("current")
_CucsEventLogDn_Type = CucsManagedObjectDn
_CucsEventLogDn_Object = MibTableColumn
cucsEventLogDn = _CucsEventLogDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 4, 1, 2),
    _CucsEventLogDn_Type()
)
cucsEventLogDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventLogDn.setStatus("current")
_CucsEventLogRn_Type = SnmpAdminString
_CucsEventLogRn_Object = MibTableColumn
cucsEventLogRn = _CucsEventLogRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 4, 1, 3),
    _CucsEventLogRn_Type()
)
cucsEventLogRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventLogRn.setStatus("current")
_CucsEventLogMaxSize_Type = Gauge32
_CucsEventLogMaxSize_Object = MibTableColumn
cucsEventLogMaxSize = _CucsEventLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 4, 1, 4),
    _CucsEventLogMaxSize_Type()
)
cucsEventLogMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventLogMaxSize.setStatus("current")
_CucsEventLogPurgeWindow_Type = Gauge32
_CucsEventLogPurgeWindow_Object = MibTableColumn
cucsEventLogPurgeWindow = _CucsEventLogPurgeWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 4, 1, 5),
    _CucsEventLogPurgeWindow_Type()
)
cucsEventLogPurgeWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventLogPurgeWindow.setStatus("current")
_CucsEventLogSize_Type = Gauge32
_CucsEventLogSize_Object = MibTableColumn
cucsEventLogSize = _CucsEventLogSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 4, 1, 6),
    _CucsEventLogSize_Type()
)
cucsEventLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventLogSize.setStatus("current")
_CucsEventPolicyTable_Object = MibTable
cucsEventPolicyTable = _CucsEventPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 5)
)
if mibBuilder.loadTexts:
    cucsEventPolicyTable.setStatus("current")
_CucsEventPolicyEntry_Object = MibTableRow
cucsEventPolicyEntry = _CucsEventPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 5, 1)
)
cucsEventPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EVENT-MIB", "cucsEventPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEventPolicyEntry.setStatus("current")
_CucsEventPolicyInstanceId_Type = CucsManagedObjectId
_CucsEventPolicyInstanceId_Object = MibTableColumn
cucsEventPolicyInstanceId = _CucsEventPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 5, 1, 1),
    _CucsEventPolicyInstanceId_Type()
)
cucsEventPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEventPolicyInstanceId.setStatus("current")
_CucsEventPolicyDn_Type = CucsManagedObjectDn
_CucsEventPolicyDn_Object = MibTableColumn
cucsEventPolicyDn = _CucsEventPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 5, 1, 2),
    _CucsEventPolicyDn_Type()
)
cucsEventPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventPolicyDn.setStatus("current")
_CucsEventPolicyRn_Type = SnmpAdminString
_CucsEventPolicyRn_Object = MibTableColumn
cucsEventPolicyRn = _CucsEventPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 5, 1, 3),
    _CucsEventPolicyRn_Type()
)
cucsEventPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventPolicyRn.setStatus("current")
_CucsEventPolicyDescr_Type = SnmpAdminString
_CucsEventPolicyDescr_Object = MibTableColumn
cucsEventPolicyDescr = _CucsEventPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 5, 1, 4),
    _CucsEventPolicyDescr_Type()
)
cucsEventPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventPolicyDescr.setStatus("current")
_CucsEventPolicyIntId_Type = SnmpAdminString
_CucsEventPolicyIntId_Object = MibTableColumn
cucsEventPolicyIntId = _CucsEventPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 5, 1, 5),
    _CucsEventPolicyIntId_Type()
)
cucsEventPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventPolicyIntId.setStatus("current")
_CucsEventPolicyName_Type = SnmpAdminString
_CucsEventPolicyName_Object = MibTableColumn
cucsEventPolicyName = _CucsEventPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 5, 1, 6),
    _CucsEventPolicyName_Type()
)
cucsEventPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventPolicyName.setStatus("current")
_CucsEventPolicyRetentionInterval_Type = TimeIntervalSec
_CucsEventPolicyRetentionInterval_Object = MibTableColumn
cucsEventPolicyRetentionInterval = _CucsEventPolicyRetentionInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 5, 1, 7),
    _CucsEventPolicyRetentionInterval_Type()
)
cucsEventPolicyRetentionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventPolicyRetentionInterval.setStatus("current")
_CucsEventPolicySizeLimit_Type = Gauge32
_CucsEventPolicySizeLimit_Object = MibTableColumn
cucsEventPolicySizeLimit = _CucsEventPolicySizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 5, 1, 8),
    _CucsEventPolicySizeLimit_Type()
)
cucsEventPolicySizeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventPolicySizeLimit.setStatus("current")
_CucsEventPolicyPolicyLevel_Type = Gauge32
_CucsEventPolicyPolicyLevel_Object = MibTableColumn
cucsEventPolicyPolicyLevel = _CucsEventPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 5, 1, 9),
    _CucsEventPolicyPolicyLevel_Type()
)
cucsEventPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventPolicyPolicyLevel.setStatus("current")
_CucsEventPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsEventPolicyPolicyOwner_Object = MibTableColumn
cucsEventPolicyPolicyOwner = _CucsEventPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 5, 1, 10),
    _CucsEventPolicyPolicyOwner_Type()
)
cucsEventPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventPolicyPolicyOwner.setStatus("current")
_CucsEventPolicyPinningExpirationInterval_Type = TimeIntervalSec
_CucsEventPolicyPinningExpirationInterval_Object = MibTableColumn
cucsEventPolicyPinningExpirationInterval = _CucsEventPolicyPinningExpirationInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 5, 1, 11),
    _CucsEventPolicyPinningExpirationInterval_Type()
)
cucsEventPolicyPinningExpirationInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventPolicyPinningExpirationInterval.setStatus("current")
_CucsEventRecordTable_Object = MibTable
cucsEventRecordTable = _CucsEventRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6)
)
if mibBuilder.loadTexts:
    cucsEventRecordTable.setStatus("current")
_CucsEventRecordEntry_Object = MibTableRow
cucsEventRecordEntry = _CucsEventRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6, 1)
)
cucsEventRecordEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EVENT-MIB", "cucsEventRecordInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEventRecordEntry.setStatus("current")
_CucsEventRecordInstanceId_Type = CucsManagedObjectId
_CucsEventRecordInstanceId_Object = MibTableColumn
cucsEventRecordInstanceId = _CucsEventRecordInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6, 1, 1),
    _CucsEventRecordInstanceId_Type()
)
cucsEventRecordInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEventRecordInstanceId.setStatus("current")
_CucsEventRecordDn_Type = CucsManagedObjectDn
_CucsEventRecordDn_Object = MibTableColumn
cucsEventRecordDn = _CucsEventRecordDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6, 1, 2),
    _CucsEventRecordDn_Type()
)
cucsEventRecordDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventRecordDn.setStatus("current")
_CucsEventRecordRn_Type = SnmpAdminString
_CucsEventRecordRn_Object = MibTableColumn
cucsEventRecordRn = _CucsEventRecordRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6, 1, 3),
    _CucsEventRecordRn_Type()
)
cucsEventRecordRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventRecordRn.setStatus("current")
_CucsEventRecordAffected_Type = SnmpAdminString
_CucsEventRecordAffected_Object = MibTableColumn
cucsEventRecordAffected = _CucsEventRecordAffected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6, 1, 4),
    _CucsEventRecordAffected_Type()
)
cucsEventRecordAffected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventRecordAffected.setStatus("current")
_CucsEventRecordCause_Type = CucsConditionCause
_CucsEventRecordCause_Object = MibTableColumn
cucsEventRecordCause = _CucsEventRecordCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6, 1, 5),
    _CucsEventRecordCause_Type()
)
cucsEventRecordCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventRecordCause.setStatus("current")
_CucsEventRecordChangeSet_Type = SnmpAdminString
_CucsEventRecordChangeSet_Object = MibTableColumn
cucsEventRecordChangeSet = _CucsEventRecordChangeSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6, 1, 6),
    _CucsEventRecordChangeSet_Type()
)
cucsEventRecordChangeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventRecordChangeSet.setStatus("current")
_CucsEventRecordCode_Type = CucsConditionCode
_CucsEventRecordCode_Object = MibTableColumn
cucsEventRecordCode = _CucsEventRecordCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6, 1, 7),
    _CucsEventRecordCode_Type()
)
cucsEventRecordCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventRecordCode.setStatus("current")
_CucsEventRecordCreated_Type = DateAndTime
_CucsEventRecordCreated_Object = MibTableColumn
cucsEventRecordCreated = _CucsEventRecordCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6, 1, 8),
    _CucsEventRecordCreated_Type()
)
cucsEventRecordCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventRecordCreated.setStatus("current")
_CucsEventRecordDescr_Type = SnmpAdminString
_CucsEventRecordDescr_Object = MibTableColumn
cucsEventRecordDescr = _CucsEventRecordDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6, 1, 9),
    _CucsEventRecordDescr_Type()
)
cucsEventRecordDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventRecordDescr.setStatus("current")
_CucsEventRecordId_Type = Gauge32
_CucsEventRecordId_Object = MibTableColumn
cucsEventRecordId = _CucsEventRecordId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6, 1, 10),
    _CucsEventRecordId_Type()
)
cucsEventRecordId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventRecordId.setStatus("current")
_CucsEventRecordInd_Type = CucsConditionActionIndicator
_CucsEventRecordInd_Object = MibTableColumn
cucsEventRecordInd = _CucsEventRecordInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6, 1, 11),
    _CucsEventRecordInd_Type()
)
cucsEventRecordInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventRecordInd.setStatus("current")
_CucsEventRecordSeverity_Type = CucsConditionSeverity
_CucsEventRecordSeverity_Object = MibTableColumn
cucsEventRecordSeverity = _CucsEventRecordSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6, 1, 12),
    _CucsEventRecordSeverity_Type()
)
cucsEventRecordSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventRecordSeverity.setStatus("current")
_CucsEventRecordTrig_Type = Gauge32
_CucsEventRecordTrig_Object = MibTableColumn
cucsEventRecordTrig = _CucsEventRecordTrig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6, 1, 13),
    _CucsEventRecordTrig_Type()
)
cucsEventRecordTrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventRecordTrig.setStatus("current")
_CucsEventRecordTxId_Type = Unsigned64
_CucsEventRecordTxId_Object = MibTableColumn
cucsEventRecordTxId = _CucsEventRecordTxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6, 1, 14),
    _CucsEventRecordTxId_Type()
)
cucsEventRecordTxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventRecordTxId.setStatus("current")
_CucsEventRecordUser_Type = SnmpAdminString
_CucsEventRecordUser_Object = MibTableColumn
cucsEventRecordUser = _CucsEventRecordUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6, 1, 15),
    _CucsEventRecordUser_Type()
)
cucsEventRecordUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventRecordUser.setStatus("current")
_CucsEventRecordSessionId_Type = SnmpAdminString
_CucsEventRecordSessionId_Object = MibTableColumn
cucsEventRecordSessionId = _CucsEventRecordSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 17, 6, 1, 16),
    _CucsEventRecordSessionId_Type()
)
cucsEventRecordSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEventRecordSessionId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-EVENT-MIB",
    **{"cucsEventObjects": cucsEventObjects,
       "cucsEventEpCtrlTable": cucsEventEpCtrlTable,
       "cucsEventEpCtrlEntry": cucsEventEpCtrlEntry,
       "cucsEventEpCtrlInstanceId": cucsEventEpCtrlInstanceId,
       "cucsEventEpCtrlDn": cucsEventEpCtrlDn,
       "cucsEventEpCtrlRn": cucsEventEpCtrlRn,
       "cucsEventEpCtrlLevel": cucsEventEpCtrlLevel,
       "cucsEventEpCtrlRevertTimeout": cucsEventEpCtrlRevertTimeout,
       "cucsEventHolderTable": cucsEventHolderTable,
       "cucsEventHolderEntry": cucsEventHolderEntry,
       "cucsEventHolderInstanceId": cucsEventHolderInstanceId,
       "cucsEventHolderDn": cucsEventHolderDn,
       "cucsEventHolderRn": cucsEventHolderRn,
       "cucsEventHolderName": cucsEventHolderName,
       "cucsEventInstTable": cucsEventInstTable,
       "cucsEventInstEntry": cucsEventInstEntry,
       "cucsEventInstInstanceId": cucsEventInstInstanceId,
       "cucsEventInstDn": cucsEventInstDn,
       "cucsEventInstRn": cucsEventInstRn,
       "cucsEventInstCause": cucsEventInstCause,
       "cucsEventInstChangeSet": cucsEventInstChangeSet,
       "cucsEventInstCode": cucsEventInstCode,
       "cucsEventInstCreated": cucsEventInstCreated,
       "cucsEventInstDescr": cucsEventInstDescr,
       "cucsEventInstId": cucsEventInstId,
       "cucsEventInstRule": cucsEventInstRule,
       "cucsEventInstSeverity": cucsEventInstSeverity,
       "cucsEventInstTags": cucsEventInstTags,
       "cucsEventInstType": cucsEventInstType,
       "cucsEventLogTable": cucsEventLogTable,
       "cucsEventLogEntry": cucsEventLogEntry,
       "cucsEventLogInstanceId": cucsEventLogInstanceId,
       "cucsEventLogDn": cucsEventLogDn,
       "cucsEventLogRn": cucsEventLogRn,
       "cucsEventLogMaxSize": cucsEventLogMaxSize,
       "cucsEventLogPurgeWindow": cucsEventLogPurgeWindow,
       "cucsEventLogSize": cucsEventLogSize,
       "cucsEventPolicyTable": cucsEventPolicyTable,
       "cucsEventPolicyEntry": cucsEventPolicyEntry,
       "cucsEventPolicyInstanceId": cucsEventPolicyInstanceId,
       "cucsEventPolicyDn": cucsEventPolicyDn,
       "cucsEventPolicyRn": cucsEventPolicyRn,
       "cucsEventPolicyDescr": cucsEventPolicyDescr,
       "cucsEventPolicyIntId": cucsEventPolicyIntId,
       "cucsEventPolicyName": cucsEventPolicyName,
       "cucsEventPolicyRetentionInterval": cucsEventPolicyRetentionInterval,
       "cucsEventPolicySizeLimit": cucsEventPolicySizeLimit,
       "cucsEventPolicyPolicyLevel": cucsEventPolicyPolicyLevel,
       "cucsEventPolicyPolicyOwner": cucsEventPolicyPolicyOwner,
       "cucsEventPolicyPinningExpirationInterval": cucsEventPolicyPinningExpirationInterval,
       "cucsEventRecordTable": cucsEventRecordTable,
       "cucsEventRecordEntry": cucsEventRecordEntry,
       "cucsEventRecordInstanceId": cucsEventRecordInstanceId,
       "cucsEventRecordDn": cucsEventRecordDn,
       "cucsEventRecordRn": cucsEventRecordRn,
       "cucsEventRecordAffected": cucsEventRecordAffected,
       "cucsEventRecordCause": cucsEventRecordCause,
       "cucsEventRecordChangeSet": cucsEventRecordChangeSet,
       "cucsEventRecordCode": cucsEventRecordCode,
       "cucsEventRecordCreated": cucsEventRecordCreated,
       "cucsEventRecordDescr": cucsEventRecordDescr,
       "cucsEventRecordId": cucsEventRecordId,
       "cucsEventRecordInd": cucsEventRecordInd,
       "cucsEventRecordSeverity": cucsEventRecordSeverity,
       "cucsEventRecordTrig": cucsEventRecordTrig,
       "cucsEventRecordTxId": cucsEventRecordTxId,
       "cucsEventRecordUser": cucsEventRecordUser,
       "cucsEventRecordSessionId": cucsEventRecordSessionId}
)
