# SNMP MIB module (CISCO-UNIFIED-COMPUTING-EXTMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-EXTMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:25 2024
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

(CucsAaaConfigState,
 CucsExtmgmtArpTargetsMaxDeadlineTimeout,
 CucsExtmgmtArpTargetsNumberOfArpRequests,
 CucsExtmgmtGatewayPingMaxDeadlineTimeout,
 CucsExtmgmtGatewayPingNumberOfPingRequests,
 CucsExtmgmtIfMonPolicyAdminState,
 CucsExtmgmtIfMonPolicyMonitorMechanism,
 CucsExtmgmtMiiStatusMaxRetryCount,
 CucsExtmgmtMiiStatusRetryInterval,
 CucsExtmgmtNdiscTargetsMaxDeadlineTimeout,
 CucsExtmgmtNdiscTargetsNumberOfNdiscRequests,
 CucsNetworkConnectionType,
 CucsNetworkIfStatus,
 CucsNetworkLocale,
 CucsNetworkPortRole,
 CucsNetworkPortType,
 CucsNetworkSwitchId,
 CucsNetworkTransport,
 CucsPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsAaaConfigState",
    "CucsExtmgmtArpTargetsMaxDeadlineTimeout",
    "CucsExtmgmtArpTargetsNumberOfArpRequests",
    "CucsExtmgmtGatewayPingMaxDeadlineTimeout",
    "CucsExtmgmtGatewayPingNumberOfPingRequests",
    "CucsExtmgmtIfMonPolicyAdminState",
    "CucsExtmgmtIfMonPolicyMonitorMechanism",
    "CucsExtmgmtMiiStatusMaxRetryCount",
    "CucsExtmgmtMiiStatusRetryInterval",
    "CucsExtmgmtNdiscTargetsMaxDeadlineTimeout",
    "CucsExtmgmtNdiscTargetsNumberOfNdiscRequests",
    "CucsNetworkConnectionType",
    "CucsNetworkIfStatus",
    "CucsNetworkLocale",
    "CucsNetworkPortRole",
    "CucsNetworkPortType",
    "CucsNetworkSwitchId",
    "CucsNetworkTransport",
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

cucsExtmgmtObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsExtmgmtArpTargetsTable_Object = MibTable
cucsExtmgmtArpTargetsTable = _CucsExtmgmtArpTargetsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 1)
)
if mibBuilder.loadTexts:
    cucsExtmgmtArpTargetsTable.setStatus("current")
_CucsExtmgmtArpTargetsEntry_Object = MibTableRow
cucsExtmgmtArpTargetsEntry = _CucsExtmgmtArpTargetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 1, 1)
)
cucsExtmgmtArpTargetsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTMGMT-MIB", "cucsExtmgmtArpTargetsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtmgmtArpTargetsEntry.setStatus("current")
_CucsExtmgmtArpTargetsInstanceId_Type = CucsManagedObjectId
_CucsExtmgmtArpTargetsInstanceId_Object = MibTableColumn
cucsExtmgmtArpTargetsInstanceId = _CucsExtmgmtArpTargetsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 1, 1, 1),
    _CucsExtmgmtArpTargetsInstanceId_Type()
)
cucsExtmgmtArpTargetsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtmgmtArpTargetsInstanceId.setStatus("current")
_CucsExtmgmtArpTargetsDn_Type = CucsManagedObjectDn
_CucsExtmgmtArpTargetsDn_Object = MibTableColumn
cucsExtmgmtArpTargetsDn = _CucsExtmgmtArpTargetsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 1, 1, 2),
    _CucsExtmgmtArpTargetsDn_Type()
)
cucsExtmgmtArpTargetsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtArpTargetsDn.setStatus("current")
_CucsExtmgmtArpTargetsRn_Type = SnmpAdminString
_CucsExtmgmtArpTargetsRn_Object = MibTableColumn
cucsExtmgmtArpTargetsRn = _CucsExtmgmtArpTargetsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 1, 1, 3),
    _CucsExtmgmtArpTargetsRn_Type()
)
cucsExtmgmtArpTargetsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtArpTargetsRn.setStatus("current")
_CucsExtmgmtArpTargetsMaxDeadlineTimeout_Type = CucsExtmgmtArpTargetsMaxDeadlineTimeout
_CucsExtmgmtArpTargetsMaxDeadlineTimeout_Object = MibTableColumn
cucsExtmgmtArpTargetsMaxDeadlineTimeout = _CucsExtmgmtArpTargetsMaxDeadlineTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 1, 1, 4),
    _CucsExtmgmtArpTargetsMaxDeadlineTimeout_Type()
)
cucsExtmgmtArpTargetsMaxDeadlineTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtArpTargetsMaxDeadlineTimeout.setStatus("current")
_CucsExtmgmtArpTargetsNumberOfArpRequests_Type = CucsExtmgmtArpTargetsNumberOfArpRequests
_CucsExtmgmtArpTargetsNumberOfArpRequests_Object = MibTableColumn
cucsExtmgmtArpTargetsNumberOfArpRequests = _CucsExtmgmtArpTargetsNumberOfArpRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 1, 1, 5),
    _CucsExtmgmtArpTargetsNumberOfArpRequests_Type()
)
cucsExtmgmtArpTargetsNumberOfArpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtArpTargetsNumberOfArpRequests.setStatus("current")
_CucsExtmgmtArpTargetsTargetIp1_Type = InetAddressIPv4
_CucsExtmgmtArpTargetsTargetIp1_Object = MibTableColumn
cucsExtmgmtArpTargetsTargetIp1 = _CucsExtmgmtArpTargetsTargetIp1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 1, 1, 6),
    _CucsExtmgmtArpTargetsTargetIp1_Type()
)
cucsExtmgmtArpTargetsTargetIp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtArpTargetsTargetIp1.setStatus("current")
_CucsExtmgmtArpTargetsTargetIp2_Type = InetAddressIPv4
_CucsExtmgmtArpTargetsTargetIp2_Object = MibTableColumn
cucsExtmgmtArpTargetsTargetIp2 = _CucsExtmgmtArpTargetsTargetIp2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 1, 1, 7),
    _CucsExtmgmtArpTargetsTargetIp2_Type()
)
cucsExtmgmtArpTargetsTargetIp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtArpTargetsTargetIp2.setStatus("current")
_CucsExtmgmtArpTargetsTargetIp3_Type = InetAddressIPv4
_CucsExtmgmtArpTargetsTargetIp3_Object = MibTableColumn
cucsExtmgmtArpTargetsTargetIp3 = _CucsExtmgmtArpTargetsTargetIp3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 1, 1, 8),
    _CucsExtmgmtArpTargetsTargetIp3_Type()
)
cucsExtmgmtArpTargetsTargetIp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtArpTargetsTargetIp3.setStatus("current")
_CucsExtmgmtArpTargetsConfigState_Type = CucsAaaConfigState
_CucsExtmgmtArpTargetsConfigState_Object = MibTableColumn
cucsExtmgmtArpTargetsConfigState = _CucsExtmgmtArpTargetsConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 1, 1, 9),
    _CucsExtmgmtArpTargetsConfigState_Type()
)
cucsExtmgmtArpTargetsConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtArpTargetsConfigState.setStatus("current")
_CucsExtmgmtArpTargetsConfigStatusMessage_Type = SnmpAdminString
_CucsExtmgmtArpTargetsConfigStatusMessage_Object = MibTableColumn
cucsExtmgmtArpTargetsConfigStatusMessage = _CucsExtmgmtArpTargetsConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 1, 1, 10),
    _CucsExtmgmtArpTargetsConfigStatusMessage_Type()
)
cucsExtmgmtArpTargetsConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtArpTargetsConfigStatusMessage.setStatus("current")
_CucsExtmgmtGatewayPingTable_Object = MibTable
cucsExtmgmtGatewayPingTable = _CucsExtmgmtGatewayPingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 2)
)
if mibBuilder.loadTexts:
    cucsExtmgmtGatewayPingTable.setStatus("current")
_CucsExtmgmtGatewayPingEntry_Object = MibTableRow
cucsExtmgmtGatewayPingEntry = _CucsExtmgmtGatewayPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 2, 1)
)
cucsExtmgmtGatewayPingEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTMGMT-MIB", "cucsExtmgmtGatewayPingInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtmgmtGatewayPingEntry.setStatus("current")
_CucsExtmgmtGatewayPingInstanceId_Type = CucsManagedObjectId
_CucsExtmgmtGatewayPingInstanceId_Object = MibTableColumn
cucsExtmgmtGatewayPingInstanceId = _CucsExtmgmtGatewayPingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 2, 1, 1),
    _CucsExtmgmtGatewayPingInstanceId_Type()
)
cucsExtmgmtGatewayPingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtmgmtGatewayPingInstanceId.setStatus("current")
_CucsExtmgmtGatewayPingDn_Type = CucsManagedObjectDn
_CucsExtmgmtGatewayPingDn_Object = MibTableColumn
cucsExtmgmtGatewayPingDn = _CucsExtmgmtGatewayPingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 2, 1, 2),
    _CucsExtmgmtGatewayPingDn_Type()
)
cucsExtmgmtGatewayPingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtGatewayPingDn.setStatus("current")
_CucsExtmgmtGatewayPingRn_Type = SnmpAdminString
_CucsExtmgmtGatewayPingRn_Object = MibTableColumn
cucsExtmgmtGatewayPingRn = _CucsExtmgmtGatewayPingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 2, 1, 3),
    _CucsExtmgmtGatewayPingRn_Type()
)
cucsExtmgmtGatewayPingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtGatewayPingRn.setStatus("current")
_CucsExtmgmtGatewayPingMaxDeadlineTimeout_Type = CucsExtmgmtGatewayPingMaxDeadlineTimeout
_CucsExtmgmtGatewayPingMaxDeadlineTimeout_Object = MibTableColumn
cucsExtmgmtGatewayPingMaxDeadlineTimeout = _CucsExtmgmtGatewayPingMaxDeadlineTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 2, 1, 4),
    _CucsExtmgmtGatewayPingMaxDeadlineTimeout_Type()
)
cucsExtmgmtGatewayPingMaxDeadlineTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtGatewayPingMaxDeadlineTimeout.setStatus("current")
_CucsExtmgmtGatewayPingNumberOfPingRequests_Type = CucsExtmgmtGatewayPingNumberOfPingRequests
_CucsExtmgmtGatewayPingNumberOfPingRequests_Object = MibTableColumn
cucsExtmgmtGatewayPingNumberOfPingRequests = _CucsExtmgmtGatewayPingNumberOfPingRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 2, 1, 5),
    _CucsExtmgmtGatewayPingNumberOfPingRequests_Type()
)
cucsExtmgmtGatewayPingNumberOfPingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtGatewayPingNumberOfPingRequests.setStatus("current")
_CucsExtmgmtIfTable_Object = MibTable
cucsExtmgmtIfTable = _CucsExtmgmtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3)
)
if mibBuilder.loadTexts:
    cucsExtmgmtIfTable.setStatus("current")
_CucsExtmgmtIfEntry_Object = MibTableRow
cucsExtmgmtIfEntry = _CucsExtmgmtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3, 1)
)
cucsExtmgmtIfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTMGMT-MIB", "cucsExtmgmtIfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtmgmtIfEntry.setStatus("current")
_CucsExtmgmtIfInstanceId_Type = CucsManagedObjectId
_CucsExtmgmtIfInstanceId_Object = MibTableColumn
cucsExtmgmtIfInstanceId = _CucsExtmgmtIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3, 1, 1),
    _CucsExtmgmtIfInstanceId_Type()
)
cucsExtmgmtIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtmgmtIfInstanceId.setStatus("current")
_CucsExtmgmtIfDn_Type = CucsManagedObjectDn
_CucsExtmgmtIfDn_Object = MibTableColumn
cucsExtmgmtIfDn = _CucsExtmgmtIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3, 1, 2),
    _CucsExtmgmtIfDn_Type()
)
cucsExtmgmtIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfDn.setStatus("current")
_CucsExtmgmtIfRn_Type = SnmpAdminString
_CucsExtmgmtIfRn_Object = MibTableColumn
cucsExtmgmtIfRn = _CucsExtmgmtIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3, 1, 3),
    _CucsExtmgmtIfRn_Type()
)
cucsExtmgmtIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfRn.setStatus("current")
_CucsExtmgmtIfEpDn_Type = SnmpAdminString
_CucsExtmgmtIfEpDn_Object = MibTableColumn
cucsExtmgmtIfEpDn = _CucsExtmgmtIfEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3, 1, 4),
    _CucsExtmgmtIfEpDn_Type()
)
cucsExtmgmtIfEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfEpDn.setStatus("current")
_CucsExtmgmtIfFailReportCount_Type = Gauge32
_CucsExtmgmtIfFailReportCount_Object = MibTableColumn
cucsExtmgmtIfFailReportCount = _CucsExtmgmtIfFailReportCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3, 1, 5),
    _CucsExtmgmtIfFailReportCount_Type()
)
cucsExtmgmtIfFailReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfFailReportCount.setStatus("current")
_CucsExtmgmtIfFltAggr_Type = Unsigned64
_CucsExtmgmtIfFltAggr_Object = MibTableColumn
cucsExtmgmtIfFltAggr = _CucsExtmgmtIfFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3, 1, 6),
    _CucsExtmgmtIfFltAggr_Type()
)
cucsExtmgmtIfFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfFltAggr.setStatus("current")
_CucsExtmgmtIfId_Type = CucsNetworkSwitchId
_CucsExtmgmtIfId_Object = MibTableColumn
cucsExtmgmtIfId = _CucsExtmgmtIfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3, 1, 7),
    _CucsExtmgmtIfId_Type()
)
cucsExtmgmtIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfId.setStatus("current")
_CucsExtmgmtIfIfRole_Type = CucsNetworkPortRole
_CucsExtmgmtIfIfRole_Object = MibTableColumn
cucsExtmgmtIfIfRole = _CucsExtmgmtIfIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3, 1, 8),
    _CucsExtmgmtIfIfRole_Type()
)
cucsExtmgmtIfIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfIfRole.setStatus("current")
_CucsExtmgmtIfIfType_Type = CucsNetworkPortType
_CucsExtmgmtIfIfType_Object = MibTableColumn
cucsExtmgmtIfIfType = _CucsExtmgmtIfIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3, 1, 9),
    _CucsExtmgmtIfIfType_Type()
)
cucsExtmgmtIfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfIfType.setStatus("current")
_CucsExtmgmtIfLastOperStateReport_Type = CucsNetworkIfStatus
_CucsExtmgmtIfLastOperStateReport_Object = MibTableColumn
cucsExtmgmtIfLastOperStateReport = _CucsExtmgmtIfLastOperStateReport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3, 1, 10),
    _CucsExtmgmtIfLastOperStateReport_Type()
)
cucsExtmgmtIfLastOperStateReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfLastOperStateReport.setStatus("current")
_CucsExtmgmtIfLocale_Type = CucsNetworkLocale
_CucsExtmgmtIfLocale_Object = MibTableColumn
cucsExtmgmtIfLocale = _CucsExtmgmtIfLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3, 1, 11),
    _CucsExtmgmtIfLocale_Type()
)
cucsExtmgmtIfLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfLocale.setStatus("current")
_CucsExtmgmtIfName_Type = SnmpAdminString
_CucsExtmgmtIfName_Object = MibTableColumn
cucsExtmgmtIfName = _CucsExtmgmtIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3, 1, 12),
    _CucsExtmgmtIfName_Type()
)
cucsExtmgmtIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfName.setStatus("current")
_CucsExtmgmtIfOperState_Type = CucsNetworkIfStatus
_CucsExtmgmtIfOperState_Object = MibTableColumn
cucsExtmgmtIfOperState = _CucsExtmgmtIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3, 1, 13),
    _CucsExtmgmtIfOperState_Type()
)
cucsExtmgmtIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfOperState.setStatus("current")
_CucsExtmgmtIfPeerDn_Type = SnmpAdminString
_CucsExtmgmtIfPeerDn_Object = MibTableColumn
cucsExtmgmtIfPeerDn = _CucsExtmgmtIfPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3, 1, 14),
    _CucsExtmgmtIfPeerDn_Type()
)
cucsExtmgmtIfPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfPeerDn.setStatus("current")
_CucsExtmgmtIfTransport_Type = CucsNetworkTransport
_CucsExtmgmtIfTransport_Object = MibTableColumn
cucsExtmgmtIfTransport = _CucsExtmgmtIfTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3, 1, 15),
    _CucsExtmgmtIfTransport_Type()
)
cucsExtmgmtIfTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfTransport.setStatus("current")
_CucsExtmgmtIfType_Type = CucsNetworkConnectionType
_CucsExtmgmtIfType_Object = MibTableColumn
cucsExtmgmtIfType = _CucsExtmgmtIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 3, 1, 16),
    _CucsExtmgmtIfType_Type()
)
cucsExtmgmtIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfType.setStatus("current")
_CucsExtmgmtIfMonPolicyTable_Object = MibTable
cucsExtmgmtIfMonPolicyTable = _CucsExtmgmtIfMonPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 4)
)
if mibBuilder.loadTexts:
    cucsExtmgmtIfMonPolicyTable.setStatus("current")
_CucsExtmgmtIfMonPolicyEntry_Object = MibTableRow
cucsExtmgmtIfMonPolicyEntry = _CucsExtmgmtIfMonPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 4, 1)
)
cucsExtmgmtIfMonPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTMGMT-MIB", "cucsExtmgmtIfMonPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtmgmtIfMonPolicyEntry.setStatus("current")
_CucsExtmgmtIfMonPolicyInstanceId_Type = CucsManagedObjectId
_CucsExtmgmtIfMonPolicyInstanceId_Object = MibTableColumn
cucsExtmgmtIfMonPolicyInstanceId = _CucsExtmgmtIfMonPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 4, 1, 1),
    _CucsExtmgmtIfMonPolicyInstanceId_Type()
)
cucsExtmgmtIfMonPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtmgmtIfMonPolicyInstanceId.setStatus("current")
_CucsExtmgmtIfMonPolicyDn_Type = CucsManagedObjectDn
_CucsExtmgmtIfMonPolicyDn_Object = MibTableColumn
cucsExtmgmtIfMonPolicyDn = _CucsExtmgmtIfMonPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 4, 1, 2),
    _CucsExtmgmtIfMonPolicyDn_Type()
)
cucsExtmgmtIfMonPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfMonPolicyDn.setStatus("current")
_CucsExtmgmtIfMonPolicyRn_Type = SnmpAdminString
_CucsExtmgmtIfMonPolicyRn_Object = MibTableColumn
cucsExtmgmtIfMonPolicyRn = _CucsExtmgmtIfMonPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 4, 1, 3),
    _CucsExtmgmtIfMonPolicyRn_Type()
)
cucsExtmgmtIfMonPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfMonPolicyRn.setStatus("current")
_CucsExtmgmtIfMonPolicyAdminState_Type = CucsExtmgmtIfMonPolicyAdminState
_CucsExtmgmtIfMonPolicyAdminState_Object = MibTableColumn
cucsExtmgmtIfMonPolicyAdminState = _CucsExtmgmtIfMonPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 4, 1, 4),
    _CucsExtmgmtIfMonPolicyAdminState_Type()
)
cucsExtmgmtIfMonPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfMonPolicyAdminState.setStatus("current")
_CucsExtmgmtIfMonPolicyEnableHAFailover_Type = TruthValue
_CucsExtmgmtIfMonPolicyEnableHAFailover_Object = MibTableColumn
cucsExtmgmtIfMonPolicyEnableHAFailover = _CucsExtmgmtIfMonPolicyEnableHAFailover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 4, 1, 5),
    _CucsExtmgmtIfMonPolicyEnableHAFailover_Type()
)
cucsExtmgmtIfMonPolicyEnableHAFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfMonPolicyEnableHAFailover.setStatus("current")
_CucsExtmgmtIfMonPolicyMaxFailReportCount_Type = Gauge32
_CucsExtmgmtIfMonPolicyMaxFailReportCount_Object = MibTableColumn
cucsExtmgmtIfMonPolicyMaxFailReportCount = _CucsExtmgmtIfMonPolicyMaxFailReportCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 4, 1, 6),
    _CucsExtmgmtIfMonPolicyMaxFailReportCount_Type()
)
cucsExtmgmtIfMonPolicyMaxFailReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfMonPolicyMaxFailReportCount.setStatus("current")
_CucsExtmgmtIfMonPolicyMonitorMechanism_Type = CucsExtmgmtIfMonPolicyMonitorMechanism
_CucsExtmgmtIfMonPolicyMonitorMechanism_Object = MibTableColumn
cucsExtmgmtIfMonPolicyMonitorMechanism = _CucsExtmgmtIfMonPolicyMonitorMechanism_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 4, 1, 7),
    _CucsExtmgmtIfMonPolicyMonitorMechanism_Type()
)
cucsExtmgmtIfMonPolicyMonitorMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfMonPolicyMonitorMechanism.setStatus("current")
_CucsExtmgmtIfMonPolicyPollInterval_Type = Gauge32
_CucsExtmgmtIfMonPolicyPollInterval_Object = MibTableColumn
cucsExtmgmtIfMonPolicyPollInterval = _CucsExtmgmtIfMonPolicyPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 4, 1, 8),
    _CucsExtmgmtIfMonPolicyPollInterval_Type()
)
cucsExtmgmtIfMonPolicyPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfMonPolicyPollInterval.setStatus("current")
_CucsExtmgmtIfMonPolicyDescr_Type = SnmpAdminString
_CucsExtmgmtIfMonPolicyDescr_Object = MibTableColumn
cucsExtmgmtIfMonPolicyDescr = _CucsExtmgmtIfMonPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 4, 1, 9),
    _CucsExtmgmtIfMonPolicyDescr_Type()
)
cucsExtmgmtIfMonPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfMonPolicyDescr.setStatus("current")
_CucsExtmgmtIfMonPolicyIntId_Type = SnmpAdminString
_CucsExtmgmtIfMonPolicyIntId_Object = MibTableColumn
cucsExtmgmtIfMonPolicyIntId = _CucsExtmgmtIfMonPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 4, 1, 10),
    _CucsExtmgmtIfMonPolicyIntId_Type()
)
cucsExtmgmtIfMonPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfMonPolicyIntId.setStatus("current")
_CucsExtmgmtIfMonPolicyName_Type = SnmpAdminString
_CucsExtmgmtIfMonPolicyName_Object = MibTableColumn
cucsExtmgmtIfMonPolicyName = _CucsExtmgmtIfMonPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 4, 1, 11),
    _CucsExtmgmtIfMonPolicyName_Type()
)
cucsExtmgmtIfMonPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfMonPolicyName.setStatus("current")
_CucsExtmgmtIfMonPolicyPolicyLevel_Type = Gauge32
_CucsExtmgmtIfMonPolicyPolicyLevel_Object = MibTableColumn
cucsExtmgmtIfMonPolicyPolicyLevel = _CucsExtmgmtIfMonPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 4, 1, 12),
    _CucsExtmgmtIfMonPolicyPolicyLevel_Type()
)
cucsExtmgmtIfMonPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfMonPolicyPolicyLevel.setStatus("current")
_CucsExtmgmtIfMonPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsExtmgmtIfMonPolicyPolicyOwner_Object = MibTableColumn
cucsExtmgmtIfMonPolicyPolicyOwner = _CucsExtmgmtIfMonPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 4, 1, 13),
    _CucsExtmgmtIfMonPolicyPolicyOwner_Type()
)
cucsExtmgmtIfMonPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtIfMonPolicyPolicyOwner.setStatus("current")
_CucsExtmgmtMiiStatusTable_Object = MibTable
cucsExtmgmtMiiStatusTable = _CucsExtmgmtMiiStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 5)
)
if mibBuilder.loadTexts:
    cucsExtmgmtMiiStatusTable.setStatus("current")
_CucsExtmgmtMiiStatusEntry_Object = MibTableRow
cucsExtmgmtMiiStatusEntry = _CucsExtmgmtMiiStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 5, 1)
)
cucsExtmgmtMiiStatusEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTMGMT-MIB", "cucsExtmgmtMiiStatusInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtmgmtMiiStatusEntry.setStatus("current")
_CucsExtmgmtMiiStatusInstanceId_Type = CucsManagedObjectId
_CucsExtmgmtMiiStatusInstanceId_Object = MibTableColumn
cucsExtmgmtMiiStatusInstanceId = _CucsExtmgmtMiiStatusInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 5, 1, 1),
    _CucsExtmgmtMiiStatusInstanceId_Type()
)
cucsExtmgmtMiiStatusInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtmgmtMiiStatusInstanceId.setStatus("current")
_CucsExtmgmtMiiStatusDn_Type = CucsManagedObjectDn
_CucsExtmgmtMiiStatusDn_Object = MibTableColumn
cucsExtmgmtMiiStatusDn = _CucsExtmgmtMiiStatusDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 5, 1, 2),
    _CucsExtmgmtMiiStatusDn_Type()
)
cucsExtmgmtMiiStatusDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtMiiStatusDn.setStatus("current")
_CucsExtmgmtMiiStatusRn_Type = SnmpAdminString
_CucsExtmgmtMiiStatusRn_Object = MibTableColumn
cucsExtmgmtMiiStatusRn = _CucsExtmgmtMiiStatusRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 5, 1, 3),
    _CucsExtmgmtMiiStatusRn_Type()
)
cucsExtmgmtMiiStatusRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtMiiStatusRn.setStatus("current")
_CucsExtmgmtMiiStatusMaxRetryCount_Type = CucsExtmgmtMiiStatusMaxRetryCount
_CucsExtmgmtMiiStatusMaxRetryCount_Object = MibTableColumn
cucsExtmgmtMiiStatusMaxRetryCount = _CucsExtmgmtMiiStatusMaxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 5, 1, 4),
    _CucsExtmgmtMiiStatusMaxRetryCount_Type()
)
cucsExtmgmtMiiStatusMaxRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtMiiStatusMaxRetryCount.setStatus("current")
_CucsExtmgmtMiiStatusRetryInterval_Type = CucsExtmgmtMiiStatusRetryInterval
_CucsExtmgmtMiiStatusRetryInterval_Object = MibTableColumn
cucsExtmgmtMiiStatusRetryInterval = _CucsExtmgmtMiiStatusRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 5, 1, 5),
    _CucsExtmgmtMiiStatusRetryInterval_Type()
)
cucsExtmgmtMiiStatusRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtMiiStatusRetryInterval.setStatus("current")
_CucsExtmgmtNdiscTargetsTable_Object = MibTable
cucsExtmgmtNdiscTargetsTable = _CucsExtmgmtNdiscTargetsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 6)
)
if mibBuilder.loadTexts:
    cucsExtmgmtNdiscTargetsTable.setStatus("current")
_CucsExtmgmtNdiscTargetsEntry_Object = MibTableRow
cucsExtmgmtNdiscTargetsEntry = _CucsExtmgmtNdiscTargetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 6, 1)
)
cucsExtmgmtNdiscTargetsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTMGMT-MIB", "cucsExtmgmtNdiscTargetsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtmgmtNdiscTargetsEntry.setStatus("current")
_CucsExtmgmtNdiscTargetsInstanceId_Type = CucsManagedObjectId
_CucsExtmgmtNdiscTargetsInstanceId_Object = MibTableColumn
cucsExtmgmtNdiscTargetsInstanceId = _CucsExtmgmtNdiscTargetsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 6, 1, 1),
    _CucsExtmgmtNdiscTargetsInstanceId_Type()
)
cucsExtmgmtNdiscTargetsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtmgmtNdiscTargetsInstanceId.setStatus("current")
_CucsExtmgmtNdiscTargetsDn_Type = CucsManagedObjectDn
_CucsExtmgmtNdiscTargetsDn_Object = MibTableColumn
cucsExtmgmtNdiscTargetsDn = _CucsExtmgmtNdiscTargetsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 6, 1, 2),
    _CucsExtmgmtNdiscTargetsDn_Type()
)
cucsExtmgmtNdiscTargetsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtNdiscTargetsDn.setStatus("current")
_CucsExtmgmtNdiscTargetsRn_Type = SnmpAdminString
_CucsExtmgmtNdiscTargetsRn_Object = MibTableColumn
cucsExtmgmtNdiscTargetsRn = _CucsExtmgmtNdiscTargetsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 6, 1, 3),
    _CucsExtmgmtNdiscTargetsRn_Type()
)
cucsExtmgmtNdiscTargetsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtNdiscTargetsRn.setStatus("current")
_CucsExtmgmtNdiscTargetsConfigState_Type = CucsAaaConfigState
_CucsExtmgmtNdiscTargetsConfigState_Object = MibTableColumn
cucsExtmgmtNdiscTargetsConfigState = _CucsExtmgmtNdiscTargetsConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 6, 1, 4),
    _CucsExtmgmtNdiscTargetsConfigState_Type()
)
cucsExtmgmtNdiscTargetsConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtNdiscTargetsConfigState.setStatus("current")
_CucsExtmgmtNdiscTargetsConfigStatusMessage_Type = SnmpAdminString
_CucsExtmgmtNdiscTargetsConfigStatusMessage_Object = MibTableColumn
cucsExtmgmtNdiscTargetsConfigStatusMessage = _CucsExtmgmtNdiscTargetsConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 6, 1, 5),
    _CucsExtmgmtNdiscTargetsConfigStatusMessage_Type()
)
cucsExtmgmtNdiscTargetsConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtNdiscTargetsConfigStatusMessage.setStatus("current")
_CucsExtmgmtNdiscTargetsIpv6Target1_Type = InetAddressIPv6
_CucsExtmgmtNdiscTargetsIpv6Target1_Object = MibTableColumn
cucsExtmgmtNdiscTargetsIpv6Target1 = _CucsExtmgmtNdiscTargetsIpv6Target1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 6, 1, 6),
    _CucsExtmgmtNdiscTargetsIpv6Target1_Type()
)
cucsExtmgmtNdiscTargetsIpv6Target1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtNdiscTargetsIpv6Target1.setStatus("current")
_CucsExtmgmtNdiscTargetsIpv6Target2_Type = InetAddressIPv6
_CucsExtmgmtNdiscTargetsIpv6Target2_Object = MibTableColumn
cucsExtmgmtNdiscTargetsIpv6Target2 = _CucsExtmgmtNdiscTargetsIpv6Target2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 6, 1, 7),
    _CucsExtmgmtNdiscTargetsIpv6Target2_Type()
)
cucsExtmgmtNdiscTargetsIpv6Target2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtNdiscTargetsIpv6Target2.setStatus("current")
_CucsExtmgmtNdiscTargetsIpv6Target3_Type = InetAddressIPv6
_CucsExtmgmtNdiscTargetsIpv6Target3_Object = MibTableColumn
cucsExtmgmtNdiscTargetsIpv6Target3 = _CucsExtmgmtNdiscTargetsIpv6Target3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 6, 1, 8),
    _CucsExtmgmtNdiscTargetsIpv6Target3_Type()
)
cucsExtmgmtNdiscTargetsIpv6Target3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtNdiscTargetsIpv6Target3.setStatus("current")
_CucsExtmgmtNdiscTargetsMaxDeadlineTimeout_Type = CucsExtmgmtNdiscTargetsMaxDeadlineTimeout
_CucsExtmgmtNdiscTargetsMaxDeadlineTimeout_Object = MibTableColumn
cucsExtmgmtNdiscTargetsMaxDeadlineTimeout = _CucsExtmgmtNdiscTargetsMaxDeadlineTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 6, 1, 9),
    _CucsExtmgmtNdiscTargetsMaxDeadlineTimeout_Type()
)
cucsExtmgmtNdiscTargetsMaxDeadlineTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtNdiscTargetsMaxDeadlineTimeout.setStatus("current")
_CucsExtmgmtNdiscTargetsNumberOfNdiscRequests_Type = CucsExtmgmtNdiscTargetsNumberOfNdiscRequests
_CucsExtmgmtNdiscTargetsNumberOfNdiscRequests_Object = MibTableColumn
cucsExtmgmtNdiscTargetsNumberOfNdiscRequests = _CucsExtmgmtNdiscTargetsNumberOfNdiscRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 57, 6, 1, 10),
    _CucsExtmgmtNdiscTargetsNumberOfNdiscRequests_Type()
)
cucsExtmgmtNdiscTargetsNumberOfNdiscRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtmgmtNdiscTargetsNumberOfNdiscRequests.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-EXTMGMT-MIB",
    **{"cucsExtmgmtObjects": cucsExtmgmtObjects,
       "cucsExtmgmtArpTargetsTable": cucsExtmgmtArpTargetsTable,
       "cucsExtmgmtArpTargetsEntry": cucsExtmgmtArpTargetsEntry,
       "cucsExtmgmtArpTargetsInstanceId": cucsExtmgmtArpTargetsInstanceId,
       "cucsExtmgmtArpTargetsDn": cucsExtmgmtArpTargetsDn,
       "cucsExtmgmtArpTargetsRn": cucsExtmgmtArpTargetsRn,
       "cucsExtmgmtArpTargetsMaxDeadlineTimeout": cucsExtmgmtArpTargetsMaxDeadlineTimeout,
       "cucsExtmgmtArpTargetsNumberOfArpRequests": cucsExtmgmtArpTargetsNumberOfArpRequests,
       "cucsExtmgmtArpTargetsTargetIp1": cucsExtmgmtArpTargetsTargetIp1,
       "cucsExtmgmtArpTargetsTargetIp2": cucsExtmgmtArpTargetsTargetIp2,
       "cucsExtmgmtArpTargetsTargetIp3": cucsExtmgmtArpTargetsTargetIp3,
       "cucsExtmgmtArpTargetsConfigState": cucsExtmgmtArpTargetsConfigState,
       "cucsExtmgmtArpTargetsConfigStatusMessage": cucsExtmgmtArpTargetsConfigStatusMessage,
       "cucsExtmgmtGatewayPingTable": cucsExtmgmtGatewayPingTable,
       "cucsExtmgmtGatewayPingEntry": cucsExtmgmtGatewayPingEntry,
       "cucsExtmgmtGatewayPingInstanceId": cucsExtmgmtGatewayPingInstanceId,
       "cucsExtmgmtGatewayPingDn": cucsExtmgmtGatewayPingDn,
       "cucsExtmgmtGatewayPingRn": cucsExtmgmtGatewayPingRn,
       "cucsExtmgmtGatewayPingMaxDeadlineTimeout": cucsExtmgmtGatewayPingMaxDeadlineTimeout,
       "cucsExtmgmtGatewayPingNumberOfPingRequests": cucsExtmgmtGatewayPingNumberOfPingRequests,
       "cucsExtmgmtIfTable": cucsExtmgmtIfTable,
       "cucsExtmgmtIfEntry": cucsExtmgmtIfEntry,
       "cucsExtmgmtIfInstanceId": cucsExtmgmtIfInstanceId,
       "cucsExtmgmtIfDn": cucsExtmgmtIfDn,
       "cucsExtmgmtIfRn": cucsExtmgmtIfRn,
       "cucsExtmgmtIfEpDn": cucsExtmgmtIfEpDn,
       "cucsExtmgmtIfFailReportCount": cucsExtmgmtIfFailReportCount,
       "cucsExtmgmtIfFltAggr": cucsExtmgmtIfFltAggr,
       "cucsExtmgmtIfId": cucsExtmgmtIfId,
       "cucsExtmgmtIfIfRole": cucsExtmgmtIfIfRole,
       "cucsExtmgmtIfIfType": cucsExtmgmtIfIfType,
       "cucsExtmgmtIfLastOperStateReport": cucsExtmgmtIfLastOperStateReport,
       "cucsExtmgmtIfLocale": cucsExtmgmtIfLocale,
       "cucsExtmgmtIfName": cucsExtmgmtIfName,
       "cucsExtmgmtIfOperState": cucsExtmgmtIfOperState,
       "cucsExtmgmtIfPeerDn": cucsExtmgmtIfPeerDn,
       "cucsExtmgmtIfTransport": cucsExtmgmtIfTransport,
       "cucsExtmgmtIfType": cucsExtmgmtIfType,
       "cucsExtmgmtIfMonPolicyTable": cucsExtmgmtIfMonPolicyTable,
       "cucsExtmgmtIfMonPolicyEntry": cucsExtmgmtIfMonPolicyEntry,
       "cucsExtmgmtIfMonPolicyInstanceId": cucsExtmgmtIfMonPolicyInstanceId,
       "cucsExtmgmtIfMonPolicyDn": cucsExtmgmtIfMonPolicyDn,
       "cucsExtmgmtIfMonPolicyRn": cucsExtmgmtIfMonPolicyRn,
       "cucsExtmgmtIfMonPolicyAdminState": cucsExtmgmtIfMonPolicyAdminState,
       "cucsExtmgmtIfMonPolicyEnableHAFailover": cucsExtmgmtIfMonPolicyEnableHAFailover,
       "cucsExtmgmtIfMonPolicyMaxFailReportCount": cucsExtmgmtIfMonPolicyMaxFailReportCount,
       "cucsExtmgmtIfMonPolicyMonitorMechanism": cucsExtmgmtIfMonPolicyMonitorMechanism,
       "cucsExtmgmtIfMonPolicyPollInterval": cucsExtmgmtIfMonPolicyPollInterval,
       "cucsExtmgmtIfMonPolicyDescr": cucsExtmgmtIfMonPolicyDescr,
       "cucsExtmgmtIfMonPolicyIntId": cucsExtmgmtIfMonPolicyIntId,
       "cucsExtmgmtIfMonPolicyName": cucsExtmgmtIfMonPolicyName,
       "cucsExtmgmtIfMonPolicyPolicyLevel": cucsExtmgmtIfMonPolicyPolicyLevel,
       "cucsExtmgmtIfMonPolicyPolicyOwner": cucsExtmgmtIfMonPolicyPolicyOwner,
       "cucsExtmgmtMiiStatusTable": cucsExtmgmtMiiStatusTable,
       "cucsExtmgmtMiiStatusEntry": cucsExtmgmtMiiStatusEntry,
       "cucsExtmgmtMiiStatusInstanceId": cucsExtmgmtMiiStatusInstanceId,
       "cucsExtmgmtMiiStatusDn": cucsExtmgmtMiiStatusDn,
       "cucsExtmgmtMiiStatusRn": cucsExtmgmtMiiStatusRn,
       "cucsExtmgmtMiiStatusMaxRetryCount": cucsExtmgmtMiiStatusMaxRetryCount,
       "cucsExtmgmtMiiStatusRetryInterval": cucsExtmgmtMiiStatusRetryInterval,
       "cucsExtmgmtNdiscTargetsTable": cucsExtmgmtNdiscTargetsTable,
       "cucsExtmgmtNdiscTargetsEntry": cucsExtmgmtNdiscTargetsEntry,
       "cucsExtmgmtNdiscTargetsInstanceId": cucsExtmgmtNdiscTargetsInstanceId,
       "cucsExtmgmtNdiscTargetsDn": cucsExtmgmtNdiscTargetsDn,
       "cucsExtmgmtNdiscTargetsRn": cucsExtmgmtNdiscTargetsRn,
       "cucsExtmgmtNdiscTargetsConfigState": cucsExtmgmtNdiscTargetsConfigState,
       "cucsExtmgmtNdiscTargetsConfigStatusMessage": cucsExtmgmtNdiscTargetsConfigStatusMessage,
       "cucsExtmgmtNdiscTargetsIpv6Target1": cucsExtmgmtNdiscTargetsIpv6Target1,
       "cucsExtmgmtNdiscTargetsIpv6Target2": cucsExtmgmtNdiscTargetsIpv6Target2,
       "cucsExtmgmtNdiscTargetsIpv6Target3": cucsExtmgmtNdiscTargetsIpv6Target3,
       "cucsExtmgmtNdiscTargetsMaxDeadlineTimeout": cucsExtmgmtNdiscTargetsMaxDeadlineTimeout,
       "cucsExtmgmtNdiscTargetsNumberOfNdiscRequests": cucsExtmgmtNdiscTargetsNumberOfNdiscRequests}
)
