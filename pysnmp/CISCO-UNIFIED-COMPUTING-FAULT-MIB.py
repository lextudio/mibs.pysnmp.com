# SNMP MIB module (CISCO-UNIFIED-COMPUTING-FAULT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-FAULT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:13 2024
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

(CucsFaultCode,
 CucsFaultProbableCause,
 CucsFaultSeverity,
 CucsFaultType,
 CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsFaultCode",
    "CucsFaultProbableCause",
    "CucsFaultSeverity",
    "CucsFaultType",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsConditionAckAction,
 CucsConditionCause,
 CucsConditionLifecycle,
 CucsConditionRule,
 CucsConditionTag,
 CucsConditionType,
 CucsFaultBasePolicyClearAction,
 CucsFaultBasePolicySoakingSeverity,
 CucsMoMoClassId,
 CucsPolicyPolicyOwner,
 CucsTrigAdminState,
 CucsTrigTrigOperState) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionAckAction",
    "CucsConditionCause",
    "CucsConditionLifecycle",
    "CucsConditionRule",
    "CucsConditionTag",
    "CucsConditionType",
    "CucsFaultBasePolicyClearAction",
    "CucsFaultBasePolicySoakingSeverity",
    "CucsMoMoClassId",
    "CucsPolicyPolicyOwner",
    "CucsTrigAdminState",
    "CucsTrigTrigOperState")

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

cucsFaultObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsFaultTable_Object = MibTable
cucsFaultTable = _CucsFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cucsFaultTable.setStatus("current")
_CucsFaultEntry_Object = MibTableRow
cucsFaultEntry = _CucsFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1)
)
cucsFaultEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultIndex"),
)
if mibBuilder.loadTexts:
    cucsFaultEntry.setStatus("current")
_CucsFaultIndex_Type = CucsManagedObjectId
_CucsFaultIndex_Object = MibTableColumn
cucsFaultIndex = _CucsFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 1),
    _CucsFaultIndex_Type()
)
cucsFaultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFaultIndex.setStatus("current")
_CucsFaultDn_Type = CucsManagedObjectDn
_CucsFaultDn_Object = MibTableColumn
cucsFaultDn = _CucsFaultDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 2),
    _CucsFaultDn_Type()
)
cucsFaultDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultDn.setStatus("current")
_CucsFaultRn_Type = SnmpAdminString
_CucsFaultRn_Object = MibTableColumn
cucsFaultRn = _CucsFaultRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 3),
    _CucsFaultRn_Type()
)
cucsFaultRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultRn.setStatus("current")
_CucsFaultAffectedObjectId_Type = RowPointer
_CucsFaultAffectedObjectId_Object = MibTableColumn
cucsFaultAffectedObjectId = _CucsFaultAffectedObjectId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 4),
    _CucsFaultAffectedObjectId_Type()
)
cucsFaultAffectedObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultAffectedObjectId.setStatus("current")
_CucsFaultAffectedObjectDn_Type = CucsManagedObjectDn
_CucsFaultAffectedObjectDn_Object = MibTableColumn
cucsFaultAffectedObjectDn = _CucsFaultAffectedObjectDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 5),
    _CucsFaultAffectedObjectDn_Type()
)
cucsFaultAffectedObjectDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultAffectedObjectDn.setStatus("current")
_CucsFaultAck_Type = TruthValue
_CucsFaultAck_Object = MibTableColumn
cucsFaultAck = _CucsFaultAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 6),
    _CucsFaultAck_Type()
)
cucsFaultAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultAck.setStatus("current")
_CucsFaultProbableCause_Type = CucsFaultProbableCause
_CucsFaultProbableCause_Object = MibTableColumn
cucsFaultProbableCause = _CucsFaultProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 7),
    _CucsFaultProbableCause_Type()
)
cucsFaultProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultProbableCause.setStatus("current")
_CucsFaultChangeSet_Type = SnmpAdminString
_CucsFaultChangeSet_Object = MibTableColumn
cucsFaultChangeSet = _CucsFaultChangeSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 8),
    _CucsFaultChangeSet_Type()
)
cucsFaultChangeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultChangeSet.setStatus("current")
_CucsFaultCode_Type = CucsFaultCode
_CucsFaultCode_Object = MibTableColumn
cucsFaultCode = _CucsFaultCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 9),
    _CucsFaultCode_Type()
)
cucsFaultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultCode.setStatus("current")
_CucsFaultCreationTime_Type = DateAndTime
_CucsFaultCreationTime_Object = MibTableColumn
cucsFaultCreationTime = _CucsFaultCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 10),
    _CucsFaultCreationTime_Type()
)
cucsFaultCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultCreationTime.setStatus("current")
_CucsFaultDescription_Type = SnmpAdminString
_CucsFaultDescription_Object = MibTableColumn
cucsFaultDescription = _CucsFaultDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 11),
    _CucsFaultDescription_Type()
)
cucsFaultDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultDescription.setStatus("current")
_CucsFaultHighestSeverity_Type = CucsFaultSeverity
_CucsFaultHighestSeverity_Object = MibTableColumn
cucsFaultHighestSeverity = _CucsFaultHighestSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 12),
    _CucsFaultHighestSeverity_Type()
)
cucsFaultHighestSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultHighestSeverity.setStatus("current")
_CucsFaultId_Type = Unsigned64
_CucsFaultId_Object = MibTableColumn
cucsFaultId = _CucsFaultId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 13),
    _CucsFaultId_Type()
)
cucsFaultId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultId.setStatus("current")
_CucsFaultLastModificationTime_Type = DateAndTime
_CucsFaultLastModificationTime_Object = MibTableColumn
cucsFaultLastModificationTime = _CucsFaultLastModificationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 14),
    _CucsFaultLastModificationTime_Type()
)
cucsFaultLastModificationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultLastModificationTime.setStatus("current")
_CucsFaultLc_Type = CucsConditionLifecycle
_CucsFaultLc_Object = MibTableColumn
cucsFaultLc = _CucsFaultLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 15),
    _CucsFaultLc_Type()
)
cucsFaultLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultLc.setStatus("current")
_CucsFaultOccur_Type = Counter32
_CucsFaultOccur_Object = MibTableColumn
cucsFaultOccur = _CucsFaultOccur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 16),
    _CucsFaultOccur_Type()
)
cucsFaultOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultOccur.setStatus("current")
_CucsFaultOrigSeverity_Type = CucsFaultSeverity
_CucsFaultOrigSeverity_Object = MibTableColumn
cucsFaultOrigSeverity = _CucsFaultOrigSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 17),
    _CucsFaultOrigSeverity_Type()
)
cucsFaultOrigSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultOrigSeverity.setStatus("current")
_CucsFaultPrevSeverity_Type = CucsFaultSeverity
_CucsFaultPrevSeverity_Object = MibTableColumn
cucsFaultPrevSeverity = _CucsFaultPrevSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 18),
    _CucsFaultPrevSeverity_Type()
)
cucsFaultPrevSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultPrevSeverity.setStatus("current")
_CucsFaultRule_Type = CucsConditionRule
_CucsFaultRule_Object = MibTableColumn
cucsFaultRule = _CucsFaultRule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 19),
    _CucsFaultRule_Type()
)
cucsFaultRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultRule.setStatus("current")
_CucsFaultSeverity_Type = CucsFaultSeverity
_CucsFaultSeverity_Object = MibTableColumn
cucsFaultSeverity = _CucsFaultSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 20),
    _CucsFaultSeverity_Type()
)
cucsFaultSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSeverity.setStatus("current")
_CucsFaultTags_Type = CucsConditionTag
_CucsFaultTags_Object = MibTableColumn
cucsFaultTags = _CucsFaultTags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 21),
    _CucsFaultTags_Type()
)
cucsFaultTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultTags.setStatus("current")
_CucsFaultType_Type = CucsFaultType
_CucsFaultType_Object = MibTableColumn
cucsFaultType = _CucsFaultType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 22),
    _CucsFaultType_Type()
)
cucsFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultType.setStatus("current")
_CucsFaultHolderTable_Object = MibTable
cucsFaultHolderTable = _CucsFaultHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cucsFaultHolderTable.setStatus("current")
_CucsFaultHolderEntry_Object = MibTableRow
cucsFaultHolderEntry = _CucsFaultHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 2, 1)
)
cucsFaultHolderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFaultHolderEntry.setStatus("current")
_CucsFaultHolderInstanceId_Type = CucsManagedObjectId
_CucsFaultHolderInstanceId_Object = MibTableColumn
cucsFaultHolderInstanceId = _CucsFaultHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 2, 1, 1),
    _CucsFaultHolderInstanceId_Type()
)
cucsFaultHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFaultHolderInstanceId.setStatus("current")
_CucsFaultHolderDn_Type = CucsManagedObjectDn
_CucsFaultHolderDn_Object = MibTableColumn
cucsFaultHolderDn = _CucsFaultHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 2, 1, 2),
    _CucsFaultHolderDn_Type()
)
cucsFaultHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultHolderDn.setStatus("current")
_CucsFaultHolderRn_Type = SnmpAdminString
_CucsFaultHolderRn_Object = MibTableColumn
cucsFaultHolderRn = _CucsFaultHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 2, 1, 3),
    _CucsFaultHolderRn_Type()
)
cucsFaultHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultHolderRn.setStatus("current")
_CucsFaultHolderName_Type = SnmpAdminString
_CucsFaultHolderName_Object = MibTableColumn
cucsFaultHolderName = _CucsFaultHolderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 2, 1, 4),
    _CucsFaultHolderName_Type()
)
cucsFaultHolderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultHolderName.setStatus("current")
_CucsFaultHolderTotalFaults_Type = Unsigned64
_CucsFaultHolderTotalFaults_Object = MibTableColumn
cucsFaultHolderTotalFaults = _CucsFaultHolderTotalFaults_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 2, 1, 5),
    _CucsFaultHolderTotalFaults_Type()
)
cucsFaultHolderTotalFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultHolderTotalFaults.setStatus("current")
_CucsFaultHolderIsPinningCleared_Type = TruthValue
_CucsFaultHolderIsPinningCleared_Object = MibTableColumn
cucsFaultHolderIsPinningCleared = _CucsFaultHolderIsPinningCleared_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 2, 1, 6),
    _CucsFaultHolderIsPinningCleared_Type()
)
cucsFaultHolderIsPinningCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultHolderIsPinningCleared.setStatus("current")
_CucsFaultHolderLastPinTime_Type = DateAndTime
_CucsFaultHolderLastPinTime_Object = MibTableColumn
cucsFaultHolderLastPinTime = _CucsFaultHolderLastPinTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 2, 1, 7),
    _CucsFaultHolderLastPinTime_Type()
)
cucsFaultHolderLastPinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultHolderLastPinTime.setStatus("current")
_CucsFaultPolicyTable_Object = MibTable
cucsFaultPolicyTable = _CucsFaultPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cucsFaultPolicyTable.setStatus("current")
_CucsFaultPolicyEntry_Object = MibTableRow
cucsFaultPolicyEntry = _CucsFaultPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1)
)
cucsFaultPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFaultPolicyEntry.setStatus("current")
_CucsFaultPolicyInstanceId_Type = CucsManagedObjectId
_CucsFaultPolicyInstanceId_Object = MibTableColumn
cucsFaultPolicyInstanceId = _CucsFaultPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1, 1),
    _CucsFaultPolicyInstanceId_Type()
)
cucsFaultPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFaultPolicyInstanceId.setStatus("current")
_CucsFaultPolicyDn_Type = CucsManagedObjectDn
_CucsFaultPolicyDn_Object = MibTableColumn
cucsFaultPolicyDn = _CucsFaultPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1, 2),
    _CucsFaultPolicyDn_Type()
)
cucsFaultPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultPolicyDn.setStatus("current")
_CucsFaultPolicyRn_Type = SnmpAdminString
_CucsFaultPolicyRn_Object = MibTableColumn
cucsFaultPolicyRn = _CucsFaultPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1, 3),
    _CucsFaultPolicyRn_Type()
)
cucsFaultPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultPolicyRn.setStatus("current")
_CucsFaultPolicyClearAction_Type = CucsFaultBasePolicyClearAction
_CucsFaultPolicyClearAction_Object = MibTableColumn
cucsFaultPolicyClearAction = _CucsFaultPolicyClearAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1, 4),
    _CucsFaultPolicyClearAction_Type()
)
cucsFaultPolicyClearAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultPolicyClearAction.setStatus("current")
_CucsFaultPolicyClearInterval_Type = TimeIntervalSec
_CucsFaultPolicyClearInterval_Object = MibTableColumn
cucsFaultPolicyClearInterval = _CucsFaultPolicyClearInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1, 5),
    _CucsFaultPolicyClearInterval_Type()
)
cucsFaultPolicyClearInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultPolicyClearInterval.setStatus("current")
_CucsFaultPolicyDescr_Type = SnmpAdminString
_CucsFaultPolicyDescr_Object = MibTableColumn
cucsFaultPolicyDescr = _CucsFaultPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1, 6),
    _CucsFaultPolicyDescr_Type()
)
cucsFaultPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultPolicyDescr.setStatus("current")
_CucsFaultPolicyFlapInterval_Type = Unsigned64
_CucsFaultPolicyFlapInterval_Object = MibTableColumn
cucsFaultPolicyFlapInterval = _CucsFaultPolicyFlapInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1, 7),
    _CucsFaultPolicyFlapInterval_Type()
)
cucsFaultPolicyFlapInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultPolicyFlapInterval.setStatus("current")
_CucsFaultPolicyIntId_Type = SnmpAdminString
_CucsFaultPolicyIntId_Object = MibTableColumn
cucsFaultPolicyIntId = _CucsFaultPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1, 8),
    _CucsFaultPolicyIntId_Type()
)
cucsFaultPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultPolicyIntId.setStatus("current")
_CucsFaultPolicyName_Type = SnmpAdminString
_CucsFaultPolicyName_Object = MibTableColumn
cucsFaultPolicyName = _CucsFaultPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1, 9),
    _CucsFaultPolicyName_Type()
)
cucsFaultPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultPolicyName.setStatus("current")
_CucsFaultPolicyRetentionInterval_Type = TimeIntervalSec
_CucsFaultPolicyRetentionInterval_Object = MibTableColumn
cucsFaultPolicyRetentionInterval = _CucsFaultPolicyRetentionInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1, 10),
    _CucsFaultPolicyRetentionInterval_Type()
)
cucsFaultPolicyRetentionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultPolicyRetentionInterval.setStatus("current")
_CucsFaultPolicySizeLimit_Type = Gauge32
_CucsFaultPolicySizeLimit_Object = MibTableColumn
cucsFaultPolicySizeLimit = _CucsFaultPolicySizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1, 11),
    _CucsFaultPolicySizeLimit_Type()
)
cucsFaultPolicySizeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultPolicySizeLimit.setStatus("current")
_CucsFaultPolicyAckAction_Type = CucsConditionAckAction
_CucsFaultPolicyAckAction_Object = MibTableColumn
cucsFaultPolicyAckAction = _CucsFaultPolicyAckAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1, 12),
    _CucsFaultPolicyAckAction_Type()
)
cucsFaultPolicyAckAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultPolicyAckAction.setStatus("current")
_CucsFaultPolicyPolicyLevel_Type = Gauge32
_CucsFaultPolicyPolicyLevel_Object = MibTableColumn
cucsFaultPolicyPolicyLevel = _CucsFaultPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1, 13),
    _CucsFaultPolicyPolicyLevel_Type()
)
cucsFaultPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultPolicyPolicyLevel.setStatus("current")
_CucsFaultPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsFaultPolicyPolicyOwner_Object = MibTableColumn
cucsFaultPolicyPolicyOwner = _CucsFaultPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1, 14),
    _CucsFaultPolicyPolicyOwner_Type()
)
cucsFaultPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultPolicyPolicyOwner.setStatus("current")
_CucsFaultPolicySoakInterval_Type = TimeIntervalSec
_CucsFaultPolicySoakInterval_Object = MibTableColumn
cucsFaultPolicySoakInterval = _CucsFaultPolicySoakInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1, 15),
    _CucsFaultPolicySoakInterval_Type()
)
cucsFaultPolicySoakInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultPolicySoakInterval.setStatus("current")
_CucsFaultPolicySoakingSeverity_Type = CucsFaultBasePolicySoakingSeverity
_CucsFaultPolicySoakingSeverity_Object = MibTableColumn
cucsFaultPolicySoakingSeverity = _CucsFaultPolicySoakingSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1, 16),
    _CucsFaultPolicySoakingSeverity_Type()
)
cucsFaultPolicySoakingSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultPolicySoakingSeverity.setStatus("current")
_CucsFaultPolicyPinningExpirationInterval_Type = TimeIntervalSec
_CucsFaultPolicyPinningExpirationInterval_Object = MibTableColumn
cucsFaultPolicyPinningExpirationInterval = _CucsFaultPolicyPinningExpirationInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 3, 1, 18),
    _CucsFaultPolicyPinningExpirationInterval_Type()
)
cucsFaultPolicyPinningExpirationInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultPolicyPinningExpirationInterval.setStatus("current")
_CucsFaultAffectedClassTable_Object = MibTable
cucsFaultAffectedClassTable = _CucsFaultAffectedClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cucsFaultAffectedClassTable.setStatus("current")
_CucsFaultAffectedClassEntry_Object = MibTableRow
cucsFaultAffectedClassEntry = _CucsFaultAffectedClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 4, 1)
)
cucsFaultAffectedClassEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedClassInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFaultAffectedClassEntry.setStatus("current")
_CucsFaultAffectedClassInstanceId_Type = CucsManagedObjectId
_CucsFaultAffectedClassInstanceId_Object = MibTableColumn
cucsFaultAffectedClassInstanceId = _CucsFaultAffectedClassInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 4, 1, 1),
    _CucsFaultAffectedClassInstanceId_Type()
)
cucsFaultAffectedClassInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFaultAffectedClassInstanceId.setStatus("current")
_CucsFaultAffectedClassDn_Type = CucsManagedObjectDn
_CucsFaultAffectedClassDn_Object = MibTableColumn
cucsFaultAffectedClassDn = _CucsFaultAffectedClassDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 4, 1, 2),
    _CucsFaultAffectedClassDn_Type()
)
cucsFaultAffectedClassDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultAffectedClassDn.setStatus("current")
_CucsFaultAffectedClassRn_Type = SnmpAdminString
_CucsFaultAffectedClassRn_Object = MibTableColumn
cucsFaultAffectedClassRn = _CucsFaultAffectedClassRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 4, 1, 3),
    _CucsFaultAffectedClassRn_Type()
)
cucsFaultAffectedClassRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultAffectedClassRn.setStatus("current")
_CucsFaultAffectedClassMoClassId_Type = CucsMoMoClassId
_CucsFaultAffectedClassMoClassId_Object = MibTableColumn
cucsFaultAffectedClassMoClassId = _CucsFaultAffectedClassMoClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 4, 1, 4),
    _CucsFaultAffectedClassMoClassId_Type()
)
cucsFaultAffectedClassMoClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultAffectedClassMoClassId.setStatus("current")
_CucsFaultLocalTypedHolderTable_Object = MibTable
cucsFaultLocalTypedHolderTable = _CucsFaultLocalTypedHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cucsFaultLocalTypedHolderTable.setStatus("current")
_CucsFaultLocalTypedHolderEntry_Object = MibTableRow
cucsFaultLocalTypedHolderEntry = _CucsFaultLocalTypedHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 6, 1)
)
cucsFaultLocalTypedHolderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultLocalTypedHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFaultLocalTypedHolderEntry.setStatus("current")
_CucsFaultLocalTypedHolderInstanceId_Type = CucsManagedObjectId
_CucsFaultLocalTypedHolderInstanceId_Object = MibTableColumn
cucsFaultLocalTypedHolderInstanceId = _CucsFaultLocalTypedHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 6, 1, 1),
    _CucsFaultLocalTypedHolderInstanceId_Type()
)
cucsFaultLocalTypedHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFaultLocalTypedHolderInstanceId.setStatus("current")
_CucsFaultLocalTypedHolderDn_Type = CucsManagedObjectDn
_CucsFaultLocalTypedHolderDn_Object = MibTableColumn
cucsFaultLocalTypedHolderDn = _CucsFaultLocalTypedHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 6, 1, 2),
    _CucsFaultLocalTypedHolderDn_Type()
)
cucsFaultLocalTypedHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultLocalTypedHolderDn.setStatus("current")
_CucsFaultLocalTypedHolderRn_Type = SnmpAdminString
_CucsFaultLocalTypedHolderRn_Object = MibTableColumn
cucsFaultLocalTypedHolderRn = _CucsFaultLocalTypedHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 6, 1, 3),
    _CucsFaultLocalTypedHolderRn_Type()
)
cucsFaultLocalTypedHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultLocalTypedHolderRn.setStatus("current")
_CucsFaultLocalTypedHolderName_Type = SnmpAdminString
_CucsFaultLocalTypedHolderName_Object = MibTableColumn
cucsFaultLocalTypedHolderName = _CucsFaultLocalTypedHolderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 6, 1, 4),
    _CucsFaultLocalTypedHolderName_Type()
)
cucsFaultLocalTypedHolderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultLocalTypedHolderName.setStatus("current")
_CucsFaultLocalTypedHolderTotalFaults_Type = Unsigned64
_CucsFaultLocalTypedHolderTotalFaults_Object = MibTableColumn
cucsFaultLocalTypedHolderTotalFaults = _CucsFaultLocalTypedHolderTotalFaults_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 6, 1, 5),
    _CucsFaultLocalTypedHolderTotalFaults_Type()
)
cucsFaultLocalTypedHolderTotalFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultLocalTypedHolderTotalFaults.setStatus("current")
_CucsFaultLocalTypedHolderType_Type = CucsConditionType
_CucsFaultLocalTypedHolderType_Object = MibTableColumn
cucsFaultLocalTypedHolderType = _CucsFaultLocalTypedHolderType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 6, 1, 6),
    _CucsFaultLocalTypedHolderType_Type()
)
cucsFaultLocalTypedHolderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultLocalTypedHolderType.setStatus("current")
_CucsFaultSuppressPolicyTable_Object = MibTable
cucsFaultSuppressPolicyTable = _CucsFaultSuppressPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyTable.setStatus("current")
_CucsFaultSuppressPolicyEntry_Object = MibTableRow
cucsFaultSuppressPolicyEntry = _CucsFaultSuppressPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 7, 1)
)
cucsFaultSuppressPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultSuppressPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyEntry.setStatus("current")
_CucsFaultSuppressPolicyInstanceId_Type = CucsManagedObjectId
_CucsFaultSuppressPolicyInstanceId_Object = MibTableColumn
cucsFaultSuppressPolicyInstanceId = _CucsFaultSuppressPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 7, 1, 1),
    _CucsFaultSuppressPolicyInstanceId_Type()
)
cucsFaultSuppressPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyInstanceId.setStatus("current")
_CucsFaultSuppressPolicyDn_Type = CucsManagedObjectDn
_CucsFaultSuppressPolicyDn_Object = MibTableColumn
cucsFaultSuppressPolicyDn = _CucsFaultSuppressPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 7, 1, 2),
    _CucsFaultSuppressPolicyDn_Type()
)
cucsFaultSuppressPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyDn.setStatus("current")
_CucsFaultSuppressPolicyRn_Type = SnmpAdminString
_CucsFaultSuppressPolicyRn_Object = MibTableColumn
cucsFaultSuppressPolicyRn = _CucsFaultSuppressPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 7, 1, 3),
    _CucsFaultSuppressPolicyRn_Type()
)
cucsFaultSuppressPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyRn.setStatus("current")
_CucsFaultSuppressPolicyDescr_Type = SnmpAdminString
_CucsFaultSuppressPolicyDescr_Object = MibTableColumn
cucsFaultSuppressPolicyDescr = _CucsFaultSuppressPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 7, 1, 4),
    _CucsFaultSuppressPolicyDescr_Type()
)
cucsFaultSuppressPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyDescr.setStatus("current")
_CucsFaultSuppressPolicyIntId_Type = SnmpAdminString
_CucsFaultSuppressPolicyIntId_Object = MibTableColumn
cucsFaultSuppressPolicyIntId = _CucsFaultSuppressPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 7, 1, 5),
    _CucsFaultSuppressPolicyIntId_Type()
)
cucsFaultSuppressPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyIntId.setStatus("current")
_CucsFaultSuppressPolicyName_Type = SnmpAdminString
_CucsFaultSuppressPolicyName_Object = MibTableColumn
cucsFaultSuppressPolicyName = _CucsFaultSuppressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 7, 1, 6),
    _CucsFaultSuppressPolicyName_Type()
)
cucsFaultSuppressPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyName.setStatus("current")
_CucsFaultSuppressPolicyPolicyLevel_Type = Gauge32
_CucsFaultSuppressPolicyPolicyLevel_Object = MibTableColumn
cucsFaultSuppressPolicyPolicyLevel = _CucsFaultSuppressPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 7, 1, 7),
    _CucsFaultSuppressPolicyPolicyLevel_Type()
)
cucsFaultSuppressPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyPolicyLevel.setStatus("current")
_CucsFaultSuppressPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsFaultSuppressPolicyPolicyOwner_Object = MibTableColumn
cucsFaultSuppressPolicyPolicyOwner = _CucsFaultSuppressPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 7, 1, 8),
    _CucsFaultSuppressPolicyPolicyOwner_Type()
)
cucsFaultSuppressPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyPolicyOwner.setStatus("current")
_CucsFaultSuppressPolicyItemTable_Object = MibTable
cucsFaultSuppressPolicyItemTable = _CucsFaultSuppressPolicyItemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyItemTable.setStatus("current")
_CucsFaultSuppressPolicyItemEntry_Object = MibTableRow
cucsFaultSuppressPolicyItemEntry = _CucsFaultSuppressPolicyItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 8, 1)
)
cucsFaultSuppressPolicyItemEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultSuppressPolicyItemInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyItemEntry.setStatus("current")
_CucsFaultSuppressPolicyItemInstanceId_Type = CucsManagedObjectId
_CucsFaultSuppressPolicyItemInstanceId_Object = MibTableColumn
cucsFaultSuppressPolicyItemInstanceId = _CucsFaultSuppressPolicyItemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 8, 1, 1),
    _CucsFaultSuppressPolicyItemInstanceId_Type()
)
cucsFaultSuppressPolicyItemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyItemInstanceId.setStatus("current")
_CucsFaultSuppressPolicyItemDn_Type = CucsManagedObjectDn
_CucsFaultSuppressPolicyItemDn_Object = MibTableColumn
cucsFaultSuppressPolicyItemDn = _CucsFaultSuppressPolicyItemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 8, 1, 2),
    _CucsFaultSuppressPolicyItemDn_Type()
)
cucsFaultSuppressPolicyItemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyItemDn.setStatus("current")
_CucsFaultSuppressPolicyItemRn_Type = SnmpAdminString
_CucsFaultSuppressPolicyItemRn_Object = MibTableColumn
cucsFaultSuppressPolicyItemRn = _CucsFaultSuppressPolicyItemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 8, 1, 3),
    _CucsFaultSuppressPolicyItemRn_Type()
)
cucsFaultSuppressPolicyItemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyItemRn.setStatus("current")
_CucsFaultSuppressPolicyItemCause_Type = CucsConditionCause
_CucsFaultSuppressPolicyItemCause_Object = MibTableColumn
cucsFaultSuppressPolicyItemCause = _CucsFaultSuppressPolicyItemCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 8, 1, 4),
    _CucsFaultSuppressPolicyItemCause_Type()
)
cucsFaultSuppressPolicyItemCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyItemCause.setStatus("current")
_CucsFaultSuppressPolicyItemDescr_Type = SnmpAdminString
_CucsFaultSuppressPolicyItemDescr_Object = MibTableColumn
cucsFaultSuppressPolicyItemDescr = _CucsFaultSuppressPolicyItemDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 8, 1, 5),
    _CucsFaultSuppressPolicyItemDescr_Type()
)
cucsFaultSuppressPolicyItemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyItemDescr.setStatus("current")
_CucsFaultSuppressPolicyItemType_Type = CucsConditionType
_CucsFaultSuppressPolicyItemType_Object = MibTableColumn
cucsFaultSuppressPolicyItemType = _CucsFaultSuppressPolicyItemType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 8, 1, 6),
    _CucsFaultSuppressPolicyItemType_Type()
)
cucsFaultSuppressPolicyItemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressPolicyItemType.setStatus("current")
_CucsFaultSuppressTaskTable_Object = MibTable
cucsFaultSuppressTaskTable = _CucsFaultSuppressTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskTable.setStatus("current")
_CucsFaultSuppressTaskEntry_Object = MibTableRow
cucsFaultSuppressTaskEntry = _CucsFaultSuppressTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9, 1)
)
cucsFaultSuppressTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultSuppressTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskEntry.setStatus("current")
_CucsFaultSuppressTaskInstanceId_Type = CucsManagedObjectId
_CucsFaultSuppressTaskInstanceId_Object = MibTableColumn
cucsFaultSuppressTaskInstanceId = _CucsFaultSuppressTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9, 1, 1),
    _CucsFaultSuppressTaskInstanceId_Type()
)
cucsFaultSuppressTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskInstanceId.setStatus("current")
_CucsFaultSuppressTaskDn_Type = CucsManagedObjectDn
_CucsFaultSuppressTaskDn_Object = MibTableColumn
cucsFaultSuppressTaskDn = _CucsFaultSuppressTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9, 1, 2),
    _CucsFaultSuppressTaskDn_Type()
)
cucsFaultSuppressTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskDn.setStatus("current")
_CucsFaultSuppressTaskRn_Type = SnmpAdminString
_CucsFaultSuppressTaskRn_Object = MibTableColumn
cucsFaultSuppressTaskRn = _CucsFaultSuppressTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9, 1, 3),
    _CucsFaultSuppressTaskRn_Type()
)
cucsFaultSuppressTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskRn.setStatus("current")
_CucsFaultSuppressTaskAdminState_Type = CucsTrigAdminState
_CucsFaultSuppressTaskAdminState_Object = MibTableColumn
cucsFaultSuppressTaskAdminState = _CucsFaultSuppressTaskAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9, 1, 4),
    _CucsFaultSuppressTaskAdminState_Type()
)
cucsFaultSuppressTaskAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskAdminState.setStatus("current")
_CucsFaultSuppressTaskAutoDelete_Type = TruthValue
_CucsFaultSuppressTaskAutoDelete_Object = MibTableColumn
cucsFaultSuppressTaskAutoDelete = _CucsFaultSuppressTaskAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9, 1, 5),
    _CucsFaultSuppressTaskAutoDelete_Type()
)
cucsFaultSuppressTaskAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskAutoDelete.setStatus("current")
_CucsFaultSuppressTaskDescr_Type = SnmpAdminString
_CucsFaultSuppressTaskDescr_Object = MibTableColumn
cucsFaultSuppressTaskDescr = _CucsFaultSuppressTaskDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9, 1, 6),
    _CucsFaultSuppressTaskDescr_Type()
)
cucsFaultSuppressTaskDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskDescr.setStatus("current")
_CucsFaultSuppressTaskIgnoreCap_Type = TruthValue
_CucsFaultSuppressTaskIgnoreCap_Object = MibTableColumn
cucsFaultSuppressTaskIgnoreCap = _CucsFaultSuppressTaskIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9, 1, 7),
    _CucsFaultSuppressTaskIgnoreCap_Type()
)
cucsFaultSuppressTaskIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskIgnoreCap.setStatus("current")
_CucsFaultSuppressTaskIntId_Type = SnmpAdminString
_CucsFaultSuppressTaskIntId_Object = MibTableColumn
cucsFaultSuppressTaskIntId = _CucsFaultSuppressTaskIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9, 1, 8),
    _CucsFaultSuppressTaskIntId_Type()
)
cucsFaultSuppressTaskIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskIntId.setStatus("current")
_CucsFaultSuppressTaskName_Type = SnmpAdminString
_CucsFaultSuppressTaskName_Object = MibTableColumn
cucsFaultSuppressTaskName = _CucsFaultSuppressTaskName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9, 1, 9),
    _CucsFaultSuppressTaskName_Type()
)
cucsFaultSuppressTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskName.setStatus("current")
_CucsFaultSuppressTaskOperScheduler_Type = SnmpAdminString
_CucsFaultSuppressTaskOperScheduler_Object = MibTableColumn
cucsFaultSuppressTaskOperScheduler = _CucsFaultSuppressTaskOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9, 1, 10),
    _CucsFaultSuppressTaskOperScheduler_Type()
)
cucsFaultSuppressTaskOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskOperScheduler.setStatus("current")
_CucsFaultSuppressTaskOperState_Type = CucsTrigTrigOperState
_CucsFaultSuppressTaskOperState_Object = MibTableColumn
cucsFaultSuppressTaskOperState = _CucsFaultSuppressTaskOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9, 1, 11),
    _CucsFaultSuppressTaskOperState_Type()
)
cucsFaultSuppressTaskOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskOperState.setStatus("current")
_CucsFaultSuppressTaskOperSuppressPolicyName_Type = SnmpAdminString
_CucsFaultSuppressTaskOperSuppressPolicyName_Object = MibTableColumn
cucsFaultSuppressTaskOperSuppressPolicyName = _CucsFaultSuppressTaskOperSuppressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9, 1, 12),
    _CucsFaultSuppressTaskOperSuppressPolicyName_Type()
)
cucsFaultSuppressTaskOperSuppressPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskOperSuppressPolicyName.setStatus("current")
_CucsFaultSuppressTaskPolicyLevel_Type = Gauge32
_CucsFaultSuppressTaskPolicyLevel_Object = MibTableColumn
cucsFaultSuppressTaskPolicyLevel = _CucsFaultSuppressTaskPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9, 1, 13),
    _CucsFaultSuppressTaskPolicyLevel_Type()
)
cucsFaultSuppressTaskPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskPolicyLevel.setStatus("current")
_CucsFaultSuppressTaskPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsFaultSuppressTaskPolicyOwner_Object = MibTableColumn
cucsFaultSuppressTaskPolicyOwner = _CucsFaultSuppressTaskPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9, 1, 14),
    _CucsFaultSuppressTaskPolicyOwner_Type()
)
cucsFaultSuppressTaskPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskPolicyOwner.setStatus("current")
_CucsFaultSuppressTaskScheduler_Type = SnmpAdminString
_CucsFaultSuppressTaskScheduler_Object = MibTableColumn
cucsFaultSuppressTaskScheduler = _CucsFaultSuppressTaskScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9, 1, 15),
    _CucsFaultSuppressTaskScheduler_Type()
)
cucsFaultSuppressTaskScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskScheduler.setStatus("current")
_CucsFaultSuppressTaskSuppressPolicyName_Type = SnmpAdminString
_CucsFaultSuppressTaskSuppressPolicyName_Object = MibTableColumn
cucsFaultSuppressTaskSuppressPolicyName = _CucsFaultSuppressTaskSuppressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 9, 1, 16),
    _CucsFaultSuppressTaskSuppressPolicyName_Type()
)
cucsFaultSuppressTaskSuppressPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFaultSuppressTaskSuppressPolicyName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-FAULT-MIB",
    **{"cucsFaultObjects": cucsFaultObjects,
       "cucsFaultTable": cucsFaultTable,
       "cucsFaultEntry": cucsFaultEntry,
       "cucsFaultIndex": cucsFaultIndex,
       "cucsFaultDn": cucsFaultDn,
       "cucsFaultRn": cucsFaultRn,
       "cucsFaultAffectedObjectId": cucsFaultAffectedObjectId,
       "cucsFaultAffectedObjectDn": cucsFaultAffectedObjectDn,
       "cucsFaultAck": cucsFaultAck,
       "cucsFaultProbableCause": cucsFaultProbableCause,
       "cucsFaultChangeSet": cucsFaultChangeSet,
       "cucsFaultCode": cucsFaultCode,
       "cucsFaultCreationTime": cucsFaultCreationTime,
       "cucsFaultDescription": cucsFaultDescription,
       "cucsFaultHighestSeverity": cucsFaultHighestSeverity,
       "cucsFaultId": cucsFaultId,
       "cucsFaultLastModificationTime": cucsFaultLastModificationTime,
       "cucsFaultLc": cucsFaultLc,
       "cucsFaultOccur": cucsFaultOccur,
       "cucsFaultOrigSeverity": cucsFaultOrigSeverity,
       "cucsFaultPrevSeverity": cucsFaultPrevSeverity,
       "cucsFaultRule": cucsFaultRule,
       "cucsFaultSeverity": cucsFaultSeverity,
       "cucsFaultTags": cucsFaultTags,
       "cucsFaultType": cucsFaultType,
       "cucsFaultHolderTable": cucsFaultHolderTable,
       "cucsFaultHolderEntry": cucsFaultHolderEntry,
       "cucsFaultHolderInstanceId": cucsFaultHolderInstanceId,
       "cucsFaultHolderDn": cucsFaultHolderDn,
       "cucsFaultHolderRn": cucsFaultHolderRn,
       "cucsFaultHolderName": cucsFaultHolderName,
       "cucsFaultHolderTotalFaults": cucsFaultHolderTotalFaults,
       "cucsFaultHolderIsPinningCleared": cucsFaultHolderIsPinningCleared,
       "cucsFaultHolderLastPinTime": cucsFaultHolderLastPinTime,
       "cucsFaultPolicyTable": cucsFaultPolicyTable,
       "cucsFaultPolicyEntry": cucsFaultPolicyEntry,
       "cucsFaultPolicyInstanceId": cucsFaultPolicyInstanceId,
       "cucsFaultPolicyDn": cucsFaultPolicyDn,
       "cucsFaultPolicyRn": cucsFaultPolicyRn,
       "cucsFaultPolicyClearAction": cucsFaultPolicyClearAction,
       "cucsFaultPolicyClearInterval": cucsFaultPolicyClearInterval,
       "cucsFaultPolicyDescr": cucsFaultPolicyDescr,
       "cucsFaultPolicyFlapInterval": cucsFaultPolicyFlapInterval,
       "cucsFaultPolicyIntId": cucsFaultPolicyIntId,
       "cucsFaultPolicyName": cucsFaultPolicyName,
       "cucsFaultPolicyRetentionInterval": cucsFaultPolicyRetentionInterval,
       "cucsFaultPolicySizeLimit": cucsFaultPolicySizeLimit,
       "cucsFaultPolicyAckAction": cucsFaultPolicyAckAction,
       "cucsFaultPolicyPolicyLevel": cucsFaultPolicyPolicyLevel,
       "cucsFaultPolicyPolicyOwner": cucsFaultPolicyPolicyOwner,
       "cucsFaultPolicySoakInterval": cucsFaultPolicySoakInterval,
       "cucsFaultPolicySoakingSeverity": cucsFaultPolicySoakingSeverity,
       "cucsFaultPolicyPinningExpirationInterval": cucsFaultPolicyPinningExpirationInterval,
       "cucsFaultAffectedClassTable": cucsFaultAffectedClassTable,
       "cucsFaultAffectedClassEntry": cucsFaultAffectedClassEntry,
       "cucsFaultAffectedClassInstanceId": cucsFaultAffectedClassInstanceId,
       "cucsFaultAffectedClassDn": cucsFaultAffectedClassDn,
       "cucsFaultAffectedClassRn": cucsFaultAffectedClassRn,
       "cucsFaultAffectedClassMoClassId": cucsFaultAffectedClassMoClassId,
       "cucsFaultLocalTypedHolderTable": cucsFaultLocalTypedHolderTable,
       "cucsFaultLocalTypedHolderEntry": cucsFaultLocalTypedHolderEntry,
       "cucsFaultLocalTypedHolderInstanceId": cucsFaultLocalTypedHolderInstanceId,
       "cucsFaultLocalTypedHolderDn": cucsFaultLocalTypedHolderDn,
       "cucsFaultLocalTypedHolderRn": cucsFaultLocalTypedHolderRn,
       "cucsFaultLocalTypedHolderName": cucsFaultLocalTypedHolderName,
       "cucsFaultLocalTypedHolderTotalFaults": cucsFaultLocalTypedHolderTotalFaults,
       "cucsFaultLocalTypedHolderType": cucsFaultLocalTypedHolderType,
       "cucsFaultSuppressPolicyTable": cucsFaultSuppressPolicyTable,
       "cucsFaultSuppressPolicyEntry": cucsFaultSuppressPolicyEntry,
       "cucsFaultSuppressPolicyInstanceId": cucsFaultSuppressPolicyInstanceId,
       "cucsFaultSuppressPolicyDn": cucsFaultSuppressPolicyDn,
       "cucsFaultSuppressPolicyRn": cucsFaultSuppressPolicyRn,
       "cucsFaultSuppressPolicyDescr": cucsFaultSuppressPolicyDescr,
       "cucsFaultSuppressPolicyIntId": cucsFaultSuppressPolicyIntId,
       "cucsFaultSuppressPolicyName": cucsFaultSuppressPolicyName,
       "cucsFaultSuppressPolicyPolicyLevel": cucsFaultSuppressPolicyPolicyLevel,
       "cucsFaultSuppressPolicyPolicyOwner": cucsFaultSuppressPolicyPolicyOwner,
       "cucsFaultSuppressPolicyItemTable": cucsFaultSuppressPolicyItemTable,
       "cucsFaultSuppressPolicyItemEntry": cucsFaultSuppressPolicyItemEntry,
       "cucsFaultSuppressPolicyItemInstanceId": cucsFaultSuppressPolicyItemInstanceId,
       "cucsFaultSuppressPolicyItemDn": cucsFaultSuppressPolicyItemDn,
       "cucsFaultSuppressPolicyItemRn": cucsFaultSuppressPolicyItemRn,
       "cucsFaultSuppressPolicyItemCause": cucsFaultSuppressPolicyItemCause,
       "cucsFaultSuppressPolicyItemDescr": cucsFaultSuppressPolicyItemDescr,
       "cucsFaultSuppressPolicyItemType": cucsFaultSuppressPolicyItemType,
       "cucsFaultSuppressTaskTable": cucsFaultSuppressTaskTable,
       "cucsFaultSuppressTaskEntry": cucsFaultSuppressTaskEntry,
       "cucsFaultSuppressTaskInstanceId": cucsFaultSuppressTaskInstanceId,
       "cucsFaultSuppressTaskDn": cucsFaultSuppressTaskDn,
       "cucsFaultSuppressTaskRn": cucsFaultSuppressTaskRn,
       "cucsFaultSuppressTaskAdminState": cucsFaultSuppressTaskAdminState,
       "cucsFaultSuppressTaskAutoDelete": cucsFaultSuppressTaskAutoDelete,
       "cucsFaultSuppressTaskDescr": cucsFaultSuppressTaskDescr,
       "cucsFaultSuppressTaskIgnoreCap": cucsFaultSuppressTaskIgnoreCap,
       "cucsFaultSuppressTaskIntId": cucsFaultSuppressTaskIntId,
       "cucsFaultSuppressTaskName": cucsFaultSuppressTaskName,
       "cucsFaultSuppressTaskOperScheduler": cucsFaultSuppressTaskOperScheduler,
       "cucsFaultSuppressTaskOperState": cucsFaultSuppressTaskOperState,
       "cucsFaultSuppressTaskOperSuppressPolicyName": cucsFaultSuppressTaskOperSuppressPolicyName,
       "cucsFaultSuppressTaskPolicyLevel": cucsFaultSuppressTaskPolicyLevel,
       "cucsFaultSuppressTaskPolicyOwner": cucsFaultSuppressTaskPolicyOwner,
       "cucsFaultSuppressTaskScheduler": cucsFaultSuppressTaskScheduler,
       "cucsFaultSuppressTaskSuppressPolicyName": cucsFaultSuppressTaskSuppressPolicyName}
)
