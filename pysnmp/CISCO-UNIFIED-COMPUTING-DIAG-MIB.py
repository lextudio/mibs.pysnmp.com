# SNMP MIB module (CISCO-UNIFIED-COMPUTING-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-DIAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:16 2024
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

(CucsDiagAdminState,
 CucsDiagBladeTestType,
 CucsDiagFailureAction,
 CucsDiagNetworkTestType,
 CucsDiagSrvCtrlType,
 CucsDiagStatus,
 CucsDiagStatusIssues,
 CucsDiagSuccessAction,
 CucsDiagTestOrder,
 CucsNetworkSwitchId,
 CucsPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsDiagAdminState",
    "CucsDiagBladeTestType",
    "CucsDiagFailureAction",
    "CucsDiagNetworkTestType",
    "CucsDiagSrvCtrlType",
    "CucsDiagStatus",
    "CucsDiagStatusIssues",
    "CucsDiagSuccessAction",
    "CucsDiagTestOrder",
    "CucsNetworkSwitchId",
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

cucsDiagObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsDiagBladeTestTable_Object = MibTable
cucsDiagBladeTestTable = _CucsDiagBladeTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 1)
)
if mibBuilder.loadTexts:
    cucsDiagBladeTestTable.setStatus("current")
_CucsDiagBladeTestEntry_Object = MibTableRow
cucsDiagBladeTestEntry = _CucsDiagBladeTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 1, 1)
)
cucsDiagBladeTestEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DIAG-MIB", "cucsDiagBladeTestInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDiagBladeTestEntry.setStatus("current")
_CucsDiagBladeTestInstanceId_Type = CucsManagedObjectId
_CucsDiagBladeTestInstanceId_Object = MibTableColumn
cucsDiagBladeTestInstanceId = _CucsDiagBladeTestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 1, 1, 1),
    _CucsDiagBladeTestInstanceId_Type()
)
cucsDiagBladeTestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDiagBladeTestInstanceId.setStatus("current")
_CucsDiagBladeTestDn_Type = CucsManagedObjectDn
_CucsDiagBladeTestDn_Object = MibTableColumn
cucsDiagBladeTestDn = _CucsDiagBladeTestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 1, 1, 2),
    _CucsDiagBladeTestDn_Type()
)
cucsDiagBladeTestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagBladeTestDn.setStatus("current")
_CucsDiagBladeTestRn_Type = SnmpAdminString
_CucsDiagBladeTestRn_Object = MibTableColumn
cucsDiagBladeTestRn = _CucsDiagBladeTestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 1, 1, 3),
    _CucsDiagBladeTestRn_Type()
)
cucsDiagBladeTestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagBladeTestRn.setStatus("current")
_CucsDiagBladeTestLength_Type = Gauge32
_CucsDiagBladeTestLength_Object = MibTableColumn
cucsDiagBladeTestLength = _CucsDiagBladeTestLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 1, 1, 4),
    _CucsDiagBladeTestLength_Type()
)
cucsDiagBladeTestLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagBladeTestLength.setStatus("current")
_CucsDiagBladeTestOrder_Type = CucsDiagTestOrder
_CucsDiagBladeTestOrder_Object = MibTableColumn
cucsDiagBladeTestOrder = _CucsDiagBladeTestOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 1, 1, 5),
    _CucsDiagBladeTestOrder_Type()
)
cucsDiagBladeTestOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagBladeTestOrder.setStatus("current")
_CucsDiagBladeTestType_Type = CucsDiagBladeTestType
_CucsDiagBladeTestType_Object = MibTableColumn
cucsDiagBladeTestType = _CucsDiagBladeTestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 1, 1, 6),
    _CucsDiagBladeTestType_Type()
)
cucsDiagBladeTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagBladeTestType.setStatus("current")
_CucsDiagNetworkTestTable_Object = MibTable
cucsDiagNetworkTestTable = _CucsDiagNetworkTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 2)
)
if mibBuilder.loadTexts:
    cucsDiagNetworkTestTable.setStatus("current")
_CucsDiagNetworkTestEntry_Object = MibTableRow
cucsDiagNetworkTestEntry = _CucsDiagNetworkTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 2, 1)
)
cucsDiagNetworkTestEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DIAG-MIB", "cucsDiagNetworkTestInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDiagNetworkTestEntry.setStatus("current")
_CucsDiagNetworkTestInstanceId_Type = CucsManagedObjectId
_CucsDiagNetworkTestInstanceId_Object = MibTableColumn
cucsDiagNetworkTestInstanceId = _CucsDiagNetworkTestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 2, 1, 1),
    _CucsDiagNetworkTestInstanceId_Type()
)
cucsDiagNetworkTestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDiagNetworkTestInstanceId.setStatus("current")
_CucsDiagNetworkTestDn_Type = CucsManagedObjectDn
_CucsDiagNetworkTestDn_Object = MibTableColumn
cucsDiagNetworkTestDn = _CucsDiagNetworkTestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 2, 1, 2),
    _CucsDiagNetworkTestDn_Type()
)
cucsDiagNetworkTestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagNetworkTestDn.setStatus("current")
_CucsDiagNetworkTestRn_Type = SnmpAdminString
_CucsDiagNetworkTestRn_Object = MibTableColumn
cucsDiagNetworkTestRn = _CucsDiagNetworkTestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 2, 1, 3),
    _CucsDiagNetworkTestRn_Type()
)
cucsDiagNetworkTestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagNetworkTestRn.setStatus("current")
_CucsDiagNetworkTestLength_Type = Gauge32
_CucsDiagNetworkTestLength_Object = MibTableColumn
cucsDiagNetworkTestLength = _CucsDiagNetworkTestLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 2, 1, 4),
    _CucsDiagNetworkTestLength_Type()
)
cucsDiagNetworkTestLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagNetworkTestLength.setStatus("current")
_CucsDiagNetworkTestOrder_Type = CucsDiagTestOrder
_CucsDiagNetworkTestOrder_Object = MibTableColumn
cucsDiagNetworkTestOrder = _CucsDiagNetworkTestOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 2, 1, 5),
    _CucsDiagNetworkTestOrder_Type()
)
cucsDiagNetworkTestOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagNetworkTestOrder.setStatus("current")
_CucsDiagNetworkTestSwitchId_Type = CucsNetworkSwitchId
_CucsDiagNetworkTestSwitchId_Object = MibTableColumn
cucsDiagNetworkTestSwitchId = _CucsDiagNetworkTestSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 2, 1, 6),
    _CucsDiagNetworkTestSwitchId_Type()
)
cucsDiagNetworkTestSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagNetworkTestSwitchId.setStatus("current")
_CucsDiagNetworkTestType_Type = CucsDiagNetworkTestType
_CucsDiagNetworkTestType_Object = MibTableColumn
cucsDiagNetworkTestType = _CucsDiagNetworkTestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 2, 1, 7),
    _CucsDiagNetworkTestType_Type()
)
cucsDiagNetworkTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagNetworkTestType.setStatus("current")
_CucsDiagRsltTable_Object = MibTable
cucsDiagRsltTable = _CucsDiagRsltTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 3)
)
if mibBuilder.loadTexts:
    cucsDiagRsltTable.setStatus("current")
_CucsDiagRsltEntry_Object = MibTableRow
cucsDiagRsltEntry = _CucsDiagRsltEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 3, 1)
)
cucsDiagRsltEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DIAG-MIB", "cucsDiagRsltInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDiagRsltEntry.setStatus("current")
_CucsDiagRsltInstanceId_Type = CucsManagedObjectId
_CucsDiagRsltInstanceId_Object = MibTableColumn
cucsDiagRsltInstanceId = _CucsDiagRsltInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 3, 1, 1),
    _CucsDiagRsltInstanceId_Type()
)
cucsDiagRsltInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDiagRsltInstanceId.setStatus("current")
_CucsDiagRsltDn_Type = CucsManagedObjectDn
_CucsDiagRsltDn_Object = MibTableColumn
cucsDiagRsltDn = _CucsDiagRsltDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 3, 1, 2),
    _CucsDiagRsltDn_Type()
)
cucsDiagRsltDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagRsltDn.setStatus("current")
_CucsDiagRsltRn_Type = SnmpAdminString
_CucsDiagRsltRn_Object = MibTableColumn
cucsDiagRsltRn = _CucsDiagRsltRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 3, 1, 3),
    _CucsDiagRsltRn_Type()
)
cucsDiagRsltRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagRsltRn.setStatus("current")
_CucsDiagRsltDescr_Type = SnmpAdminString
_CucsDiagRsltDescr_Object = MibTableColumn
cucsDiagRsltDescr = _CucsDiagRsltDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 3, 1, 4),
    _CucsDiagRsltDescr_Type()
)
cucsDiagRsltDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagRsltDescr.setStatus("current")
_CucsDiagRsltEndTs_Type = DateAndTime
_CucsDiagRsltEndTs_Object = MibTableColumn
cucsDiagRsltEndTs = _CucsDiagRsltEndTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 3, 1, 5),
    _CucsDiagRsltEndTs_Type()
)
cucsDiagRsltEndTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagRsltEndTs.setStatus("current")
_CucsDiagRsltId_Type = Gauge32
_CucsDiagRsltId_Object = MibTableColumn
cucsDiagRsltId = _CucsDiagRsltId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 3, 1, 6),
    _CucsDiagRsltId_Type()
)
cucsDiagRsltId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagRsltId.setStatus("current")
_CucsDiagRsltResult_Type = Gauge32
_CucsDiagRsltResult_Object = MibTableColumn
cucsDiagRsltResult = _CucsDiagRsltResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 3, 1, 7),
    _CucsDiagRsltResult_Type()
)
cucsDiagRsltResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagRsltResult.setStatus("current")
_CucsDiagRsltRsltStatus_Type = CucsDiagStatus
_CucsDiagRsltRsltStatus_Object = MibTableColumn
cucsDiagRsltRsltStatus = _CucsDiagRsltRsltStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 3, 1, 8),
    _CucsDiagRsltRsltStatus_Type()
)
cucsDiagRsltRsltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagRsltRsltStatus.setStatus("current")
_CucsDiagRsltStartTs_Type = DateAndTime
_CucsDiagRsltStartTs_Object = MibTableColumn
cucsDiagRsltStartTs = _CucsDiagRsltStartTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 3, 1, 9),
    _CucsDiagRsltStartTs_Type()
)
cucsDiagRsltStartTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagRsltStartTs.setStatus("current")
_CucsDiagRunPolicyTable_Object = MibTable
cucsDiagRunPolicyTable = _CucsDiagRunPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 4)
)
if mibBuilder.loadTexts:
    cucsDiagRunPolicyTable.setStatus("current")
_CucsDiagRunPolicyEntry_Object = MibTableRow
cucsDiagRunPolicyEntry = _CucsDiagRunPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 4, 1)
)
cucsDiagRunPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DIAG-MIB", "cucsDiagRunPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDiagRunPolicyEntry.setStatus("current")
_CucsDiagRunPolicyInstanceId_Type = CucsManagedObjectId
_CucsDiagRunPolicyInstanceId_Object = MibTableColumn
cucsDiagRunPolicyInstanceId = _CucsDiagRunPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 4, 1, 1),
    _CucsDiagRunPolicyInstanceId_Type()
)
cucsDiagRunPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDiagRunPolicyInstanceId.setStatus("current")
_CucsDiagRunPolicyDn_Type = CucsManagedObjectDn
_CucsDiagRunPolicyDn_Object = MibTableColumn
cucsDiagRunPolicyDn = _CucsDiagRunPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 4, 1, 2),
    _CucsDiagRunPolicyDn_Type()
)
cucsDiagRunPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagRunPolicyDn.setStatus("current")
_CucsDiagRunPolicyRn_Type = SnmpAdminString
_CucsDiagRunPolicyRn_Object = MibTableColumn
cucsDiagRunPolicyRn = _CucsDiagRunPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 4, 1, 3),
    _CucsDiagRunPolicyRn_Type()
)
cucsDiagRunPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagRunPolicyRn.setStatus("current")
_CucsDiagRunPolicyDescr_Type = SnmpAdminString
_CucsDiagRunPolicyDescr_Object = MibTableColumn
cucsDiagRunPolicyDescr = _CucsDiagRunPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 4, 1, 4),
    _CucsDiagRunPolicyDescr_Type()
)
cucsDiagRunPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagRunPolicyDescr.setStatus("current")
_CucsDiagRunPolicyFailureAction_Type = CucsDiagFailureAction
_CucsDiagRunPolicyFailureAction_Object = MibTableColumn
cucsDiagRunPolicyFailureAction = _CucsDiagRunPolicyFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 4, 1, 5),
    _CucsDiagRunPolicyFailureAction_Type()
)
cucsDiagRunPolicyFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagRunPolicyFailureAction.setStatus("current")
_CucsDiagRunPolicyIntId_Type = SnmpAdminString
_CucsDiagRunPolicyIntId_Object = MibTableColumn
cucsDiagRunPolicyIntId = _CucsDiagRunPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 4, 1, 6),
    _CucsDiagRunPolicyIntId_Type()
)
cucsDiagRunPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagRunPolicyIntId.setStatus("current")
_CucsDiagRunPolicyName_Type = SnmpAdminString
_CucsDiagRunPolicyName_Object = MibTableColumn
cucsDiagRunPolicyName = _CucsDiagRunPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 4, 1, 7),
    _CucsDiagRunPolicyName_Type()
)
cucsDiagRunPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagRunPolicyName.setStatus("current")
_CucsDiagRunPolicySuccessAction_Type = CucsDiagSuccessAction
_CucsDiagRunPolicySuccessAction_Object = MibTableColumn
cucsDiagRunPolicySuccessAction = _CucsDiagRunPolicySuccessAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 4, 1, 8),
    _CucsDiagRunPolicySuccessAction_Type()
)
cucsDiagRunPolicySuccessAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagRunPolicySuccessAction.setStatus("current")
_CucsDiagRunPolicyPolicyLevel_Type = Gauge32
_CucsDiagRunPolicyPolicyLevel_Object = MibTableColumn
cucsDiagRunPolicyPolicyLevel = _CucsDiagRunPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 4, 1, 9),
    _CucsDiagRunPolicyPolicyLevel_Type()
)
cucsDiagRunPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagRunPolicyPolicyLevel.setStatus("current")
_CucsDiagRunPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsDiagRunPolicyPolicyOwner_Object = MibTableColumn
cucsDiagRunPolicyPolicyOwner = _CucsDiagRunPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 4, 1, 10),
    _CucsDiagRunPolicyPolicyOwner_Type()
)
cucsDiagRunPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagRunPolicyPolicyOwner.setStatus("current")
_CucsDiagSrvCapProviderTable_Object = MibTable
cucsDiagSrvCapProviderTable = _CucsDiagSrvCapProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 5)
)
if mibBuilder.loadTexts:
    cucsDiagSrvCapProviderTable.setStatus("current")
_CucsDiagSrvCapProviderEntry_Object = MibTableRow
cucsDiagSrvCapProviderEntry = _CucsDiagSrvCapProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 5, 1)
)
cucsDiagSrvCapProviderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DIAG-MIB", "cucsDiagSrvCapProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDiagSrvCapProviderEntry.setStatus("current")
_CucsDiagSrvCapProviderInstanceId_Type = CucsManagedObjectId
_CucsDiagSrvCapProviderInstanceId_Object = MibTableColumn
cucsDiagSrvCapProviderInstanceId = _CucsDiagSrvCapProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 5, 1, 1),
    _CucsDiagSrvCapProviderInstanceId_Type()
)
cucsDiagSrvCapProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDiagSrvCapProviderInstanceId.setStatus("current")
_CucsDiagSrvCapProviderDn_Type = CucsManagedObjectDn
_CucsDiagSrvCapProviderDn_Object = MibTableColumn
cucsDiagSrvCapProviderDn = _CucsDiagSrvCapProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 5, 1, 2),
    _CucsDiagSrvCapProviderDn_Type()
)
cucsDiagSrvCapProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCapProviderDn.setStatus("current")
_CucsDiagSrvCapProviderRn_Type = SnmpAdminString
_CucsDiagSrvCapProviderRn_Object = MibTableColumn
cucsDiagSrvCapProviderRn = _CucsDiagSrvCapProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 5, 1, 3),
    _CucsDiagSrvCapProviderRn_Type()
)
cucsDiagSrvCapProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCapProviderRn.setStatus("current")
_CucsDiagSrvCapProviderDeprecated_Type = TruthValue
_CucsDiagSrvCapProviderDeprecated_Object = MibTableColumn
cucsDiagSrvCapProviderDeprecated = _CucsDiagSrvCapProviderDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 5, 1, 4),
    _CucsDiagSrvCapProviderDeprecated_Type()
)
cucsDiagSrvCapProviderDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCapProviderDeprecated.setStatus("current")
_CucsDiagSrvCapProviderGencount_Type = Gauge32
_CucsDiagSrvCapProviderGencount_Object = MibTableColumn
cucsDiagSrvCapProviderGencount = _CucsDiagSrvCapProviderGencount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 5, 1, 5),
    _CucsDiagSrvCapProviderGencount_Type()
)
cucsDiagSrvCapProviderGencount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCapProviderGencount.setStatus("current")
_CucsDiagSrvCapProviderMgmtPlaneVer_Type = SnmpAdminString
_CucsDiagSrvCapProviderMgmtPlaneVer_Object = MibTableColumn
cucsDiagSrvCapProviderMgmtPlaneVer = _CucsDiagSrvCapProviderMgmtPlaneVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 5, 1, 6),
    _CucsDiagSrvCapProviderMgmtPlaneVer_Type()
)
cucsDiagSrvCapProviderMgmtPlaneVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCapProviderMgmtPlaneVer.setStatus("current")
_CucsDiagSrvCapProviderModel_Type = SnmpAdminString
_CucsDiagSrvCapProviderModel_Object = MibTableColumn
cucsDiagSrvCapProviderModel = _CucsDiagSrvCapProviderModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 5, 1, 7),
    _CucsDiagSrvCapProviderModel_Type()
)
cucsDiagSrvCapProviderModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCapProviderModel.setStatus("current")
_CucsDiagSrvCapProviderRevision_Type = SnmpAdminString
_CucsDiagSrvCapProviderRevision_Object = MibTableColumn
cucsDiagSrvCapProviderRevision = _CucsDiagSrvCapProviderRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 5, 1, 8),
    _CucsDiagSrvCapProviderRevision_Type()
)
cucsDiagSrvCapProviderRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCapProviderRevision.setStatus("current")
_CucsDiagSrvCapProviderVendor_Type = SnmpAdminString
_CucsDiagSrvCapProviderVendor_Object = MibTableColumn
cucsDiagSrvCapProviderVendor = _CucsDiagSrvCapProviderVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 5, 1, 9),
    _CucsDiagSrvCapProviderVendor_Type()
)
cucsDiagSrvCapProviderVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCapProviderVendor.setStatus("current")
_CucsDiagSrvCapProviderPromCardType_Type = Gauge32
_CucsDiagSrvCapProviderPromCardType_Object = MibTableColumn
cucsDiagSrvCapProviderPromCardType = _CucsDiagSrvCapProviderPromCardType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 5, 1, 10),
    _CucsDiagSrvCapProviderPromCardType_Type()
)
cucsDiagSrvCapProviderPromCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCapProviderPromCardType.setStatus("current")
_CucsDiagSrvCapProviderDeleted_Type = TruthValue
_CucsDiagSrvCapProviderDeleted_Object = MibTableColumn
cucsDiagSrvCapProviderDeleted = _CucsDiagSrvCapProviderDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 5, 1, 11),
    _CucsDiagSrvCapProviderDeleted_Type()
)
cucsDiagSrvCapProviderDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCapProviderDeleted.setStatus("current")
_CucsDiagSrvCapProviderElementLoadFailures_Type = Gauge32
_CucsDiagSrvCapProviderElementLoadFailures_Object = MibTableColumn
cucsDiagSrvCapProviderElementLoadFailures = _CucsDiagSrvCapProviderElementLoadFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 5, 1, 12),
    _CucsDiagSrvCapProviderElementLoadFailures_Type()
)
cucsDiagSrvCapProviderElementLoadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCapProviderElementLoadFailures.setStatus("current")
_CucsDiagSrvCapProviderElementsLoaded_Type = Gauge32
_CucsDiagSrvCapProviderElementsLoaded_Object = MibTableColumn
cucsDiagSrvCapProviderElementsLoaded = _CucsDiagSrvCapProviderElementsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 5, 1, 13),
    _CucsDiagSrvCapProviderElementsLoaded_Type()
)
cucsDiagSrvCapProviderElementsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCapProviderElementsLoaded.setStatus("current")
_CucsDiagSrvCapProviderLoadErrors_Type = Gauge32
_CucsDiagSrvCapProviderLoadErrors_Object = MibTableColumn
cucsDiagSrvCapProviderLoadErrors = _CucsDiagSrvCapProviderLoadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 5, 1, 14),
    _CucsDiagSrvCapProviderLoadErrors_Type()
)
cucsDiagSrvCapProviderLoadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCapProviderLoadErrors.setStatus("current")
_CucsDiagSrvCapProviderLoadWarnings_Type = Gauge32
_CucsDiagSrvCapProviderLoadWarnings_Object = MibTableColumn
cucsDiagSrvCapProviderLoadWarnings = _CucsDiagSrvCapProviderLoadWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 5, 1, 15),
    _CucsDiagSrvCapProviderLoadWarnings_Type()
)
cucsDiagSrvCapProviderLoadWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCapProviderLoadWarnings.setStatus("current")
_CucsDiagSrvCtrlTable_Object = MibTable
cucsDiagSrvCtrlTable = _CucsDiagSrvCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 6)
)
if mibBuilder.loadTexts:
    cucsDiagSrvCtrlTable.setStatus("current")
_CucsDiagSrvCtrlEntry_Object = MibTableRow
cucsDiagSrvCtrlEntry = _CucsDiagSrvCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 6, 1)
)
cucsDiagSrvCtrlEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DIAG-MIB", "cucsDiagSrvCtrlInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDiagSrvCtrlEntry.setStatus("current")
_CucsDiagSrvCtrlInstanceId_Type = CucsManagedObjectId
_CucsDiagSrvCtrlInstanceId_Object = MibTableColumn
cucsDiagSrvCtrlInstanceId = _CucsDiagSrvCtrlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 6, 1, 1),
    _CucsDiagSrvCtrlInstanceId_Type()
)
cucsDiagSrvCtrlInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDiagSrvCtrlInstanceId.setStatus("current")
_CucsDiagSrvCtrlDn_Type = CucsManagedObjectDn
_CucsDiagSrvCtrlDn_Object = MibTableColumn
cucsDiagSrvCtrlDn = _CucsDiagSrvCtrlDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 6, 1, 2),
    _CucsDiagSrvCtrlDn_Type()
)
cucsDiagSrvCtrlDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCtrlDn.setStatus("current")
_CucsDiagSrvCtrlRn_Type = SnmpAdminString
_CucsDiagSrvCtrlRn_Object = MibTableColumn
cucsDiagSrvCtrlRn = _CucsDiagSrvCtrlRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 6, 1, 3),
    _CucsDiagSrvCtrlRn_Type()
)
cucsDiagSrvCtrlRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCtrlRn.setStatus("current")
_CucsDiagSrvCtrlAdminState_Type = CucsDiagAdminState
_CucsDiagSrvCtrlAdminState_Object = MibTableColumn
cucsDiagSrvCtrlAdminState = _CucsDiagSrvCtrlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 6, 1, 4),
    _CucsDiagSrvCtrlAdminState_Type()
)
cucsDiagSrvCtrlAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCtrlAdminState.setStatus("current")
_CucsDiagSrvCtrlImgLoc_Type = SnmpAdminString
_CucsDiagSrvCtrlImgLoc_Object = MibTableColumn
cucsDiagSrvCtrlImgLoc = _CucsDiagSrvCtrlImgLoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 6, 1, 5),
    _CucsDiagSrvCtrlImgLoc_Type()
)
cucsDiagSrvCtrlImgLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCtrlImgLoc.setStatus("current")
_CucsDiagSrvCtrlImgName_Type = SnmpAdminString
_CucsDiagSrvCtrlImgName_Object = MibTableColumn
cucsDiagSrvCtrlImgName = _CucsDiagSrvCtrlImgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 6, 1, 6),
    _CucsDiagSrvCtrlImgName_Type()
)
cucsDiagSrvCtrlImgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCtrlImgName.setStatus("current")
_CucsDiagSrvCtrlOperQualifier_Type = CucsDiagStatusIssues
_CucsDiagSrvCtrlOperQualifier_Object = MibTableColumn
cucsDiagSrvCtrlOperQualifier = _CucsDiagSrvCtrlOperQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 6, 1, 7),
    _CucsDiagSrvCtrlOperQualifier_Type()
)
cucsDiagSrvCtrlOperQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCtrlOperQualifier.setStatus("current")
_CucsDiagSrvCtrlOperState_Type = CucsDiagStatus
_CucsDiagSrvCtrlOperState_Object = MibTableColumn
cucsDiagSrvCtrlOperState = _CucsDiagSrvCtrlOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 6, 1, 8),
    _CucsDiagSrvCtrlOperState_Type()
)
cucsDiagSrvCtrlOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCtrlOperState.setStatus("current")
_CucsDiagSrvCtrlRunPolicyName_Type = SnmpAdminString
_CucsDiagSrvCtrlRunPolicyName_Object = MibTableColumn
cucsDiagSrvCtrlRunPolicyName = _CucsDiagSrvCtrlRunPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 6, 1, 9),
    _CucsDiagSrvCtrlRunPolicyName_Type()
)
cucsDiagSrvCtrlRunPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCtrlRunPolicyName.setStatus("current")
_CucsDiagSrvCtrlType_Type = CucsDiagSrvCtrlType
_CucsDiagSrvCtrlType_Object = MibTableColumn
cucsDiagSrvCtrlType = _CucsDiagSrvCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 6, 1, 10),
    _CucsDiagSrvCtrlType_Type()
)
cucsDiagSrvCtrlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCtrlType.setStatus("current")
_CucsDiagSrvCtrlEndTs_Type = DateAndTime
_CucsDiagSrvCtrlEndTs_Object = MibTableColumn
cucsDiagSrvCtrlEndTs = _CucsDiagSrvCtrlEndTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 6, 1, 11),
    _CucsDiagSrvCtrlEndTs_Type()
)
cucsDiagSrvCtrlEndTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCtrlEndTs.setStatus("current")
_CucsDiagSrvCtrlEndTsM_Type = Unsigned64
_CucsDiagSrvCtrlEndTsM_Object = MibTableColumn
cucsDiagSrvCtrlEndTsM = _CucsDiagSrvCtrlEndTsM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 6, 1, 12),
    _CucsDiagSrvCtrlEndTsM_Type()
)
cucsDiagSrvCtrlEndTsM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCtrlEndTsM.setStatus("current")
_CucsDiagSrvCtrlErrorDescr_Type = SnmpAdminString
_CucsDiagSrvCtrlErrorDescr_Object = MibTableColumn
cucsDiagSrvCtrlErrorDescr = _CucsDiagSrvCtrlErrorDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 6, 1, 13),
    _CucsDiagSrvCtrlErrorDescr_Type()
)
cucsDiagSrvCtrlErrorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCtrlErrorDescr.setStatus("current")
_CucsDiagSrvCtrlStartTs_Type = DateAndTime
_CucsDiagSrvCtrlStartTs_Object = MibTableColumn
cucsDiagSrvCtrlStartTs = _CucsDiagSrvCtrlStartTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 6, 1, 14),
    _CucsDiagSrvCtrlStartTs_Type()
)
cucsDiagSrvCtrlStartTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCtrlStartTs.setStatus("current")
_CucsDiagSrvCtrlStartTsM_Type = Unsigned64
_CucsDiagSrvCtrlStartTsM_Object = MibTableColumn
cucsDiagSrvCtrlStartTsM = _CucsDiagSrvCtrlStartTsM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 12, 6, 1, 15),
    _CucsDiagSrvCtrlStartTsM_Type()
)
cucsDiagSrvCtrlStartTsM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDiagSrvCtrlStartTsM.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-DIAG-MIB",
    **{"cucsDiagObjects": cucsDiagObjects,
       "cucsDiagBladeTestTable": cucsDiagBladeTestTable,
       "cucsDiagBladeTestEntry": cucsDiagBladeTestEntry,
       "cucsDiagBladeTestInstanceId": cucsDiagBladeTestInstanceId,
       "cucsDiagBladeTestDn": cucsDiagBladeTestDn,
       "cucsDiagBladeTestRn": cucsDiagBladeTestRn,
       "cucsDiagBladeTestLength": cucsDiagBladeTestLength,
       "cucsDiagBladeTestOrder": cucsDiagBladeTestOrder,
       "cucsDiagBladeTestType": cucsDiagBladeTestType,
       "cucsDiagNetworkTestTable": cucsDiagNetworkTestTable,
       "cucsDiagNetworkTestEntry": cucsDiagNetworkTestEntry,
       "cucsDiagNetworkTestInstanceId": cucsDiagNetworkTestInstanceId,
       "cucsDiagNetworkTestDn": cucsDiagNetworkTestDn,
       "cucsDiagNetworkTestRn": cucsDiagNetworkTestRn,
       "cucsDiagNetworkTestLength": cucsDiagNetworkTestLength,
       "cucsDiagNetworkTestOrder": cucsDiagNetworkTestOrder,
       "cucsDiagNetworkTestSwitchId": cucsDiagNetworkTestSwitchId,
       "cucsDiagNetworkTestType": cucsDiagNetworkTestType,
       "cucsDiagRsltTable": cucsDiagRsltTable,
       "cucsDiagRsltEntry": cucsDiagRsltEntry,
       "cucsDiagRsltInstanceId": cucsDiagRsltInstanceId,
       "cucsDiagRsltDn": cucsDiagRsltDn,
       "cucsDiagRsltRn": cucsDiagRsltRn,
       "cucsDiagRsltDescr": cucsDiagRsltDescr,
       "cucsDiagRsltEndTs": cucsDiagRsltEndTs,
       "cucsDiagRsltId": cucsDiagRsltId,
       "cucsDiagRsltResult": cucsDiagRsltResult,
       "cucsDiagRsltRsltStatus": cucsDiagRsltRsltStatus,
       "cucsDiagRsltStartTs": cucsDiagRsltStartTs,
       "cucsDiagRunPolicyTable": cucsDiagRunPolicyTable,
       "cucsDiagRunPolicyEntry": cucsDiagRunPolicyEntry,
       "cucsDiagRunPolicyInstanceId": cucsDiagRunPolicyInstanceId,
       "cucsDiagRunPolicyDn": cucsDiagRunPolicyDn,
       "cucsDiagRunPolicyRn": cucsDiagRunPolicyRn,
       "cucsDiagRunPolicyDescr": cucsDiagRunPolicyDescr,
       "cucsDiagRunPolicyFailureAction": cucsDiagRunPolicyFailureAction,
       "cucsDiagRunPolicyIntId": cucsDiagRunPolicyIntId,
       "cucsDiagRunPolicyName": cucsDiagRunPolicyName,
       "cucsDiagRunPolicySuccessAction": cucsDiagRunPolicySuccessAction,
       "cucsDiagRunPolicyPolicyLevel": cucsDiagRunPolicyPolicyLevel,
       "cucsDiagRunPolicyPolicyOwner": cucsDiagRunPolicyPolicyOwner,
       "cucsDiagSrvCapProviderTable": cucsDiagSrvCapProviderTable,
       "cucsDiagSrvCapProviderEntry": cucsDiagSrvCapProviderEntry,
       "cucsDiagSrvCapProviderInstanceId": cucsDiagSrvCapProviderInstanceId,
       "cucsDiagSrvCapProviderDn": cucsDiagSrvCapProviderDn,
       "cucsDiagSrvCapProviderRn": cucsDiagSrvCapProviderRn,
       "cucsDiagSrvCapProviderDeprecated": cucsDiagSrvCapProviderDeprecated,
       "cucsDiagSrvCapProviderGencount": cucsDiagSrvCapProviderGencount,
       "cucsDiagSrvCapProviderMgmtPlaneVer": cucsDiagSrvCapProviderMgmtPlaneVer,
       "cucsDiagSrvCapProviderModel": cucsDiagSrvCapProviderModel,
       "cucsDiagSrvCapProviderRevision": cucsDiagSrvCapProviderRevision,
       "cucsDiagSrvCapProviderVendor": cucsDiagSrvCapProviderVendor,
       "cucsDiagSrvCapProviderPromCardType": cucsDiagSrvCapProviderPromCardType,
       "cucsDiagSrvCapProviderDeleted": cucsDiagSrvCapProviderDeleted,
       "cucsDiagSrvCapProviderElementLoadFailures": cucsDiagSrvCapProviderElementLoadFailures,
       "cucsDiagSrvCapProviderElementsLoaded": cucsDiagSrvCapProviderElementsLoaded,
       "cucsDiagSrvCapProviderLoadErrors": cucsDiagSrvCapProviderLoadErrors,
       "cucsDiagSrvCapProviderLoadWarnings": cucsDiagSrvCapProviderLoadWarnings,
       "cucsDiagSrvCtrlTable": cucsDiagSrvCtrlTable,
       "cucsDiagSrvCtrlEntry": cucsDiagSrvCtrlEntry,
       "cucsDiagSrvCtrlInstanceId": cucsDiagSrvCtrlInstanceId,
       "cucsDiagSrvCtrlDn": cucsDiagSrvCtrlDn,
       "cucsDiagSrvCtrlRn": cucsDiagSrvCtrlRn,
       "cucsDiagSrvCtrlAdminState": cucsDiagSrvCtrlAdminState,
       "cucsDiagSrvCtrlImgLoc": cucsDiagSrvCtrlImgLoc,
       "cucsDiagSrvCtrlImgName": cucsDiagSrvCtrlImgName,
       "cucsDiagSrvCtrlOperQualifier": cucsDiagSrvCtrlOperQualifier,
       "cucsDiagSrvCtrlOperState": cucsDiagSrvCtrlOperState,
       "cucsDiagSrvCtrlRunPolicyName": cucsDiagSrvCtrlRunPolicyName,
       "cucsDiagSrvCtrlType": cucsDiagSrvCtrlType,
       "cucsDiagSrvCtrlEndTs": cucsDiagSrvCtrlEndTs,
       "cucsDiagSrvCtrlEndTsM": cucsDiagSrvCtrlEndTsM,
       "cucsDiagSrvCtrlErrorDescr": cucsDiagSrvCtrlErrorDescr,
       "cucsDiagSrvCtrlStartTs": cucsDiagSrvCtrlStartTs,
       "cucsDiagSrvCtrlStartTsM": cucsDiagSrvCtrlStartTsM}
)
