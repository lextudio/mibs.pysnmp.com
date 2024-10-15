# SNMP MIB module (CISCO-UNIFIED-COMPUTING-OS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-OS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:06 2024
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

(CucsHostagAction,
 CucsHostagAgentType,
 CucsHostagEvent,
 CucsNetworkConnectionType,
 CucsNetworkTransport,
 CucsOsCarrierQueryMethod,
 CucsOsEthBondModeActiveBackupType,
 CucsOsEthBondModeBalancedRRType,
 CucsOsEthBondModeBroadcastType,
 CucsOsEthBondModeLBType,
 CucsOsEthBondModeLBXmitHashType,
 CucsOsLBType,
 CucsOsMacFailOverPolicy,
 CucsOsOsType,
 CucsOsPrimaryReselection,
 CucsVnicIfOperState) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsHostagAction",
    "CucsHostagAgentType",
    "CucsHostagEvent",
    "CucsNetworkConnectionType",
    "CucsNetworkTransport",
    "CucsOsCarrierQueryMethod",
    "CucsOsEthBondModeActiveBackupType",
    "CucsOsEthBondModeBalancedRRType",
    "CucsOsEthBondModeBroadcastType",
    "CucsOsEthBondModeLBType",
    "CucsOsEthBondModeLBXmitHashType",
    "CucsOsLBType",
    "CucsOsMacFailOverPolicy",
    "CucsOsOsType",
    "CucsOsPrimaryReselection",
    "CucsVnicIfOperState")

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

cucsOsObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsOsAgentTable_Object = MibTable
cucsOsAgentTable = _CucsOsAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 1)
)
if mibBuilder.loadTexts:
    cucsOsAgentTable.setStatus("current")
_CucsOsAgentEntry_Object = MibTableRow
cucsOsAgentEntry = _CucsOsAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 1, 1)
)
cucsOsAgentEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OS-MIB", "cucsOsAgentInstanceId"),
)
if mibBuilder.loadTexts:
    cucsOsAgentEntry.setStatus("current")
_CucsOsAgentInstanceId_Type = CucsManagedObjectId
_CucsOsAgentInstanceId_Object = MibTableColumn
cucsOsAgentInstanceId = _CucsOsAgentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 1, 1, 1),
    _CucsOsAgentInstanceId_Type()
)
cucsOsAgentInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsOsAgentInstanceId.setStatus("current")
_CucsOsAgentDn_Type = CucsManagedObjectDn
_CucsOsAgentDn_Object = MibTableColumn
cucsOsAgentDn = _CucsOsAgentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 1, 1, 2),
    _CucsOsAgentDn_Type()
)
cucsOsAgentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsAgentDn.setStatus("current")
_CucsOsAgentRn_Type = SnmpAdminString
_CucsOsAgentRn_Object = MibTableColumn
cucsOsAgentRn = _CucsOsAgentRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 1, 1, 3),
    _CucsOsAgentRn_Type()
)
cucsOsAgentRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsAgentRn.setStatus("current")
_CucsOsAgentLastCmd_Type = CucsHostagAction
_CucsOsAgentLastCmd_Object = MibTableColumn
cucsOsAgentLastCmd = _CucsOsAgentLastCmd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 1, 1, 4),
    _CucsOsAgentLastCmd_Type()
)
cucsOsAgentLastCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsAgentLastCmd.setStatus("current")
_CucsOsAgentLastEvt_Type = CucsHostagEvent
_CucsOsAgentLastEvt_Object = MibTableColumn
cucsOsAgentLastEvt = _CucsOsAgentLastEvt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 1, 1, 5),
    _CucsOsAgentLastEvt_Type()
)
cucsOsAgentLastEvt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsAgentLastEvt.setStatus("current")
_CucsOsAgentLastEvtTs_Type = DateAndTime
_CucsOsAgentLastEvtTs_Object = MibTableColumn
cucsOsAgentLastEvtTs = _CucsOsAgentLastEvtTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 1, 1, 6),
    _CucsOsAgentLastEvtTs_Type()
)
cucsOsAgentLastEvtTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsAgentLastEvtTs.setStatus("current")
_CucsOsAgentPrevCmd_Type = CucsHostagAction
_CucsOsAgentPrevCmd_Object = MibTableColumn
cucsOsAgentPrevCmd = _CucsOsAgentPrevCmd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 1, 1, 7),
    _CucsOsAgentPrevCmd_Type()
)
cucsOsAgentPrevCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsAgentPrevCmd.setStatus("current")
_CucsOsAgentPrevEvt_Type = CucsHostagEvent
_CucsOsAgentPrevEvt_Object = MibTableColumn
cucsOsAgentPrevEvt = _CucsOsAgentPrevEvt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 1, 1, 8),
    _CucsOsAgentPrevEvt_Type()
)
cucsOsAgentPrevEvt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsAgentPrevEvt.setStatus("current")
_CucsOsAgentType_Type = CucsHostagAgentType
_CucsOsAgentType_Object = MibTableColumn
cucsOsAgentType = _CucsOsAgentType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 1, 1, 9),
    _CucsOsAgentType_Type()
)
cucsOsAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsAgentType.setStatus("current")
_CucsOsAgentVendor_Type = SnmpAdminString
_CucsOsAgentVendor_Object = MibTableColumn
cucsOsAgentVendor = _CucsOsAgentVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 1, 1, 10),
    _CucsOsAgentVendor_Type()
)
cucsOsAgentVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsAgentVendor.setStatus("current")
_CucsOsAgentVersion_Type = SnmpAdminString
_CucsOsAgentVersion_Object = MibTableColumn
cucsOsAgentVersion = _CucsOsAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 1, 1, 11),
    _CucsOsAgentVersion_Type()
)
cucsOsAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsAgentVersion.setStatus("current")
_CucsOsInstanceTable_Object = MibTable
cucsOsInstanceTable = _CucsOsInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 2)
)
if mibBuilder.loadTexts:
    cucsOsInstanceTable.setStatus("current")
_CucsOsInstanceEntry_Object = MibTableRow
cucsOsInstanceEntry = _CucsOsInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 2, 1)
)
cucsOsInstanceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OS-MIB", "cucsOsInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cucsOsInstanceEntry.setStatus("current")
_CucsOsInstanceInstanceId_Type = CucsManagedObjectId
_CucsOsInstanceInstanceId_Object = MibTableColumn
cucsOsInstanceInstanceId = _CucsOsInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 2, 1, 1),
    _CucsOsInstanceInstanceId_Type()
)
cucsOsInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsOsInstanceInstanceId.setStatus("current")
_CucsOsInstanceDn_Type = CucsManagedObjectDn
_CucsOsInstanceDn_Object = MibTableColumn
cucsOsInstanceDn = _CucsOsInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 2, 1, 2),
    _CucsOsInstanceDn_Type()
)
cucsOsInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsInstanceDn.setStatus("current")
_CucsOsInstanceRn_Type = SnmpAdminString
_CucsOsInstanceRn_Object = MibTableColumn
cucsOsInstanceRn = _CucsOsInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 2, 1, 3),
    _CucsOsInstanceRn_Type()
)
cucsOsInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsInstanceRn.setStatus("current")
_CucsOsInstanceHostname_Type = SnmpAdminString
_CucsOsInstanceHostname_Object = MibTableColumn
cucsOsInstanceHostname = _CucsOsInstanceHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 2, 1, 4),
    _CucsOsInstanceHostname_Type()
)
cucsOsInstanceHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsInstanceHostname.setStatus("current")
_CucsOsInstanceKernelName_Type = SnmpAdminString
_CucsOsInstanceKernelName_Object = MibTableColumn
cucsOsInstanceKernelName = _CucsOsInstanceKernelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 2, 1, 5),
    _CucsOsInstanceKernelName_Type()
)
cucsOsInstanceKernelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsInstanceKernelName.setStatus("current")
_CucsOsInstanceKernelRelease_Type = SnmpAdminString
_CucsOsInstanceKernelRelease_Object = MibTableColumn
cucsOsInstanceKernelRelease = _CucsOsInstanceKernelRelease_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 2, 1, 6),
    _CucsOsInstanceKernelRelease_Type()
)
cucsOsInstanceKernelRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsInstanceKernelRelease.setStatus("current")
_CucsOsInstanceKernelVersion_Type = SnmpAdminString
_CucsOsInstanceKernelVersion_Object = MibTableColumn
cucsOsInstanceKernelVersion = _CucsOsInstanceKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 2, 1, 7),
    _CucsOsInstanceKernelVersion_Type()
)
cucsOsInstanceKernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsInstanceKernelVersion.setStatus("current")
_CucsOsInstanceName_Type = SnmpAdminString
_CucsOsInstanceName_Object = MibTableColumn
cucsOsInstanceName = _CucsOsInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 2, 1, 8),
    _CucsOsInstanceName_Type()
)
cucsOsInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsInstanceName.setStatus("current")
_CucsOsInstanceType_Type = CucsOsOsType
_CucsOsInstanceType_Object = MibTableColumn
cucsOsInstanceType = _CucsOsInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 2, 1, 9),
    _CucsOsInstanceType_Type()
)
cucsOsInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsInstanceType.setStatus("current")
_CucsOsARPLinkMonitoringPolicyTable_Object = MibTable
cucsOsARPLinkMonitoringPolicyTable = _CucsOsARPLinkMonitoringPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 3)
)
if mibBuilder.loadTexts:
    cucsOsARPLinkMonitoringPolicyTable.setStatus("current")
_CucsOsARPLinkMonitoringPolicyEntry_Object = MibTableRow
cucsOsARPLinkMonitoringPolicyEntry = _CucsOsARPLinkMonitoringPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 3, 1)
)
cucsOsARPLinkMonitoringPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OS-MIB", "cucsOsARPLinkMonitoringPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsOsARPLinkMonitoringPolicyEntry.setStatus("current")
_CucsOsARPLinkMonitoringPolicyInstanceId_Type = CucsManagedObjectId
_CucsOsARPLinkMonitoringPolicyInstanceId_Object = MibTableColumn
cucsOsARPLinkMonitoringPolicyInstanceId = _CucsOsARPLinkMonitoringPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 3, 1, 1),
    _CucsOsARPLinkMonitoringPolicyInstanceId_Type()
)
cucsOsARPLinkMonitoringPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsOsARPLinkMonitoringPolicyInstanceId.setStatus("current")
_CucsOsARPLinkMonitoringPolicyDn_Type = CucsManagedObjectDn
_CucsOsARPLinkMonitoringPolicyDn_Object = MibTableColumn
cucsOsARPLinkMonitoringPolicyDn = _CucsOsARPLinkMonitoringPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 3, 1, 2),
    _CucsOsARPLinkMonitoringPolicyDn_Type()
)
cucsOsARPLinkMonitoringPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsARPLinkMonitoringPolicyDn.setStatus("current")
_CucsOsARPLinkMonitoringPolicyRn_Type = SnmpAdminString
_CucsOsARPLinkMonitoringPolicyRn_Object = MibTableColumn
cucsOsARPLinkMonitoringPolicyRn = _CucsOsARPLinkMonitoringPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 3, 1, 3),
    _CucsOsARPLinkMonitoringPolicyRn_Type()
)
cucsOsARPLinkMonitoringPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsARPLinkMonitoringPolicyRn.setStatus("current")
_CucsOsARPLinkMonitoringPolicyFrequency_Type = Gauge32
_CucsOsARPLinkMonitoringPolicyFrequency_Object = MibTableColumn
cucsOsARPLinkMonitoringPolicyFrequency = _CucsOsARPLinkMonitoringPolicyFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 3, 1, 4),
    _CucsOsARPLinkMonitoringPolicyFrequency_Type()
)
cucsOsARPLinkMonitoringPolicyFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsARPLinkMonitoringPolicyFrequency.setStatus("current")
_CucsOsARPLinkMonitoringPolicyName_Type = SnmpAdminString
_CucsOsARPLinkMonitoringPolicyName_Object = MibTableColumn
cucsOsARPLinkMonitoringPolicyName = _CucsOsARPLinkMonitoringPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 3, 1, 5),
    _CucsOsARPLinkMonitoringPolicyName_Type()
)
cucsOsARPLinkMonitoringPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsARPLinkMonitoringPolicyName.setStatus("current")
_CucsOsARPLinkMonitoringPolicyUseAllARPTargets_Type = TruthValue
_CucsOsARPLinkMonitoringPolicyUseAllARPTargets_Object = MibTableColumn
cucsOsARPLinkMonitoringPolicyUseAllARPTargets = _CucsOsARPLinkMonitoringPolicyUseAllARPTargets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 3, 1, 6),
    _CucsOsARPLinkMonitoringPolicyUseAllARPTargets_Type()
)
cucsOsARPLinkMonitoringPolicyUseAllARPTargets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsARPLinkMonitoringPolicyUseAllARPTargets.setStatus("current")
_CucsOsARPTargetTable_Object = MibTable
cucsOsARPTargetTable = _CucsOsARPTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 4)
)
if mibBuilder.loadTexts:
    cucsOsARPTargetTable.setStatus("current")
_CucsOsARPTargetEntry_Object = MibTableRow
cucsOsARPTargetEntry = _CucsOsARPTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 4, 1)
)
cucsOsARPTargetEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OS-MIB", "cucsOsARPTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cucsOsARPTargetEntry.setStatus("current")
_CucsOsARPTargetInstanceId_Type = CucsManagedObjectId
_CucsOsARPTargetInstanceId_Object = MibTableColumn
cucsOsARPTargetInstanceId = _CucsOsARPTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 4, 1, 1),
    _CucsOsARPTargetInstanceId_Type()
)
cucsOsARPTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsOsARPTargetInstanceId.setStatus("current")
_CucsOsARPTargetDn_Type = CucsManagedObjectDn
_CucsOsARPTargetDn_Object = MibTableColumn
cucsOsARPTargetDn = _CucsOsARPTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 4, 1, 2),
    _CucsOsARPTargetDn_Type()
)
cucsOsARPTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsARPTargetDn.setStatus("current")
_CucsOsARPTargetRn_Type = SnmpAdminString
_CucsOsARPTargetRn_Object = MibTableColumn
cucsOsARPTargetRn = _CucsOsARPTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 4, 1, 3),
    _CucsOsARPTargetRn_Type()
)
cucsOsARPTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsARPTargetRn.setStatus("current")
_CucsOsARPTargetHostName_Type = SnmpAdminString
_CucsOsARPTargetHostName_Object = MibTableColumn
cucsOsARPTargetHostName = _CucsOsARPTargetHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 4, 1, 4),
    _CucsOsARPTargetHostName_Type()
)
cucsOsARPTargetHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsARPTargetHostName.setStatus("current")
_CucsOsARPTargetName_Type = SnmpAdminString
_CucsOsARPTargetName_Object = MibTableColumn
cucsOsARPTargetName = _CucsOsARPTargetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 4, 1, 5),
    _CucsOsARPTargetName_Type()
)
cucsOsARPTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsARPTargetName.setStatus("current")
_CucsOsEthBondIntfTable_Object = MibTable
cucsOsEthBondIntfTable = _CucsOsEthBondIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 9)
)
if mibBuilder.loadTexts:
    cucsOsEthBondIntfTable.setStatus("current")
_CucsOsEthBondIntfEntry_Object = MibTableRow
cucsOsEthBondIntfEntry = _CucsOsEthBondIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 9, 1)
)
cucsOsEthBondIntfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OS-MIB", "cucsOsEthBondIntfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsOsEthBondIntfEntry.setStatus("current")
_CucsOsEthBondIntfInstanceId_Type = CucsManagedObjectId
_CucsOsEthBondIntfInstanceId_Object = MibTableColumn
cucsOsEthBondIntfInstanceId = _CucsOsEthBondIntfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 9, 1, 1),
    _CucsOsEthBondIntfInstanceId_Type()
)
cucsOsEthBondIntfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsOsEthBondIntfInstanceId.setStatus("current")
_CucsOsEthBondIntfDn_Type = CucsManagedObjectDn
_CucsOsEthBondIntfDn_Object = MibTableColumn
cucsOsEthBondIntfDn = _CucsOsEthBondIntfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 9, 1, 2),
    _CucsOsEthBondIntfDn_Type()
)
cucsOsEthBondIntfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondIntfDn.setStatus("current")
_CucsOsEthBondIntfRn_Type = SnmpAdminString
_CucsOsEthBondIntfRn_Object = MibTableColumn
cucsOsEthBondIntfRn = _CucsOsEthBondIntfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 9, 1, 3),
    _CucsOsEthBondIntfRn_Type()
)
cucsOsEthBondIntfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondIntfRn.setStatus("current")
_CucsOsEthBondIntfAddr_Type = MacAddress
_CucsOsEthBondIntfAddr_Object = MibTableColumn
cucsOsEthBondIntfAddr = _CucsOsEthBondIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 9, 1, 4),
    _CucsOsEthBondIntfAddr_Type()
)
cucsOsEthBondIntfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondIntfAddr.setStatus("current")
_CucsOsEthBondIntfMaxBonds_Type = Gauge32
_CucsOsEthBondIntfMaxBonds_Object = MibTableColumn
cucsOsEthBondIntfMaxBonds = _CucsOsEthBondIntfMaxBonds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 9, 1, 5),
    _CucsOsEthBondIntfMaxBonds_Type()
)
cucsOsEthBondIntfMaxBonds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondIntfMaxBonds.setStatus("current")
_CucsOsEthBondIntfMtu_Type = Gauge32
_CucsOsEthBondIntfMtu_Object = MibTableColumn
cucsOsEthBondIntfMtu = _CucsOsEthBondIntfMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 9, 1, 6),
    _CucsOsEthBondIntfMtu_Type()
)
cucsOsEthBondIntfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondIntfMtu.setStatus("current")
_CucsOsEthBondIntfName_Type = SnmpAdminString
_CucsOsEthBondIntfName_Object = MibTableColumn
cucsOsEthBondIntfName = _CucsOsEthBondIntfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 9, 1, 7),
    _CucsOsEthBondIntfName_Type()
)
cucsOsEthBondIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondIntfName.setStatus("current")
_CucsOsEthBondIntfOperState_Type = CucsVnicIfOperState
_CucsOsEthBondIntfOperState_Object = MibTableColumn
cucsOsEthBondIntfOperState = _CucsOsEthBondIntfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 9, 1, 8),
    _CucsOsEthBondIntfOperState_Type()
)
cucsOsEthBondIntfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondIntfOperState.setStatus("current")
_CucsOsEthBondIntfTransport_Type = CucsNetworkTransport
_CucsOsEthBondIntfTransport_Object = MibTableColumn
cucsOsEthBondIntfTransport = _CucsOsEthBondIntfTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 9, 1, 9),
    _CucsOsEthBondIntfTransport_Type()
)
cucsOsEthBondIntfTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondIntfTransport.setStatus("current")
_CucsOsEthBondIntfType_Type = CucsNetworkConnectionType
_CucsOsEthBondIntfType_Object = MibTableColumn
cucsOsEthBondIntfType = _CucsOsEthBondIntfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 9, 1, 10),
    _CucsOsEthBondIntfType_Type()
)
cucsOsEthBondIntfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondIntfType.setStatus("current")
_CucsOsEthBondModeActiveBackupTable_Object = MibTable
cucsOsEthBondModeActiveBackupTable = _CucsOsEthBondModeActiveBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 10)
)
if mibBuilder.loadTexts:
    cucsOsEthBondModeActiveBackupTable.setStatus("current")
_CucsOsEthBondModeActiveBackupEntry_Object = MibTableRow
cucsOsEthBondModeActiveBackupEntry = _CucsOsEthBondModeActiveBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 10, 1)
)
cucsOsEthBondModeActiveBackupEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OS-MIB", "cucsOsEthBondModeActiveBackupInstanceId"),
)
if mibBuilder.loadTexts:
    cucsOsEthBondModeActiveBackupEntry.setStatus("current")
_CucsOsEthBondModeActiveBackupInstanceId_Type = CucsManagedObjectId
_CucsOsEthBondModeActiveBackupInstanceId_Object = MibTableColumn
cucsOsEthBondModeActiveBackupInstanceId = _CucsOsEthBondModeActiveBackupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 10, 1, 1),
    _CucsOsEthBondModeActiveBackupInstanceId_Type()
)
cucsOsEthBondModeActiveBackupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsOsEthBondModeActiveBackupInstanceId.setStatus("current")
_CucsOsEthBondModeActiveBackupDn_Type = CucsManagedObjectDn
_CucsOsEthBondModeActiveBackupDn_Object = MibTableColumn
cucsOsEthBondModeActiveBackupDn = _CucsOsEthBondModeActiveBackupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 10, 1, 2),
    _CucsOsEthBondModeActiveBackupDn_Type()
)
cucsOsEthBondModeActiveBackupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeActiveBackupDn.setStatus("current")
_CucsOsEthBondModeActiveBackupRn_Type = SnmpAdminString
_CucsOsEthBondModeActiveBackupRn_Object = MibTableColumn
cucsOsEthBondModeActiveBackupRn = _CucsOsEthBondModeActiveBackupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 10, 1, 3),
    _CucsOsEthBondModeActiveBackupRn_Type()
)
cucsOsEthBondModeActiveBackupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeActiveBackupRn.setStatus("current")
_CucsOsEthBondModeActiveBackupMacAddressPolicy_Type = CucsOsMacFailOverPolicy
_CucsOsEthBondModeActiveBackupMacAddressPolicy_Object = MibTableColumn
cucsOsEthBondModeActiveBackupMacAddressPolicy = _CucsOsEthBondModeActiveBackupMacAddressPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 10, 1, 4),
    _CucsOsEthBondModeActiveBackupMacAddressPolicy_Type()
)
cucsOsEthBondModeActiveBackupMacAddressPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeActiveBackupMacAddressPolicy.setStatus("current")
_CucsOsEthBondModeActiveBackupName_Type = SnmpAdminString
_CucsOsEthBondModeActiveBackupName_Object = MibTableColumn
cucsOsEthBondModeActiveBackupName = _CucsOsEthBondModeActiveBackupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 10, 1, 5),
    _CucsOsEthBondModeActiveBackupName_Type()
)
cucsOsEthBondModeActiveBackupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeActiveBackupName.setStatus("current")
_CucsOsEthBondModeActiveBackupNumPeerNotifications_Type = Gauge32
_CucsOsEthBondModeActiveBackupNumPeerNotifications_Object = MibTableColumn
cucsOsEthBondModeActiveBackupNumPeerNotifications = _CucsOsEthBondModeActiveBackupNumPeerNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 10, 1, 6),
    _CucsOsEthBondModeActiveBackupNumPeerNotifications_Type()
)
cucsOsEthBondModeActiveBackupNumPeerNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeActiveBackupNumPeerNotifications.setStatus("current")
_CucsOsEthBondModeActiveBackupType_Type = CucsOsEthBondModeActiveBackupType
_CucsOsEthBondModeActiveBackupType_Object = MibTableColumn
cucsOsEthBondModeActiveBackupType = _CucsOsEthBondModeActiveBackupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 10, 1, 7),
    _CucsOsEthBondModeActiveBackupType_Type()
)
cucsOsEthBondModeActiveBackupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeActiveBackupType.setStatus("current")
_CucsOsEthBondModeBalancedALBTable_Object = MibTable
cucsOsEthBondModeBalancedALBTable = _CucsOsEthBondModeBalancedALBTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 11)
)
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedALBTable.setStatus("current")
_CucsOsEthBondModeBalancedALBEntry_Object = MibTableRow
cucsOsEthBondModeBalancedALBEntry = _CucsOsEthBondModeBalancedALBEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 11, 1)
)
cucsOsEthBondModeBalancedALBEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OS-MIB", "cucsOsEthBondModeBalancedALBInstanceId"),
)
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedALBEntry.setStatus("current")
_CucsOsEthBondModeBalancedALBInstanceId_Type = CucsManagedObjectId
_CucsOsEthBondModeBalancedALBInstanceId_Object = MibTableColumn
cucsOsEthBondModeBalancedALBInstanceId = _CucsOsEthBondModeBalancedALBInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 11, 1, 1),
    _CucsOsEthBondModeBalancedALBInstanceId_Type()
)
cucsOsEthBondModeBalancedALBInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedALBInstanceId.setStatus("current")
_CucsOsEthBondModeBalancedALBDn_Type = CucsManagedObjectDn
_CucsOsEthBondModeBalancedALBDn_Object = MibTableColumn
cucsOsEthBondModeBalancedALBDn = _CucsOsEthBondModeBalancedALBDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 11, 1, 2),
    _CucsOsEthBondModeBalancedALBDn_Type()
)
cucsOsEthBondModeBalancedALBDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedALBDn.setStatus("current")
_CucsOsEthBondModeBalancedALBRn_Type = SnmpAdminString
_CucsOsEthBondModeBalancedALBRn_Object = MibTableColumn
cucsOsEthBondModeBalancedALBRn = _CucsOsEthBondModeBalancedALBRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 11, 1, 3),
    _CucsOsEthBondModeBalancedALBRn_Type()
)
cucsOsEthBondModeBalancedALBRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedALBRn.setStatus("current")
_CucsOsEthBondModeBalancedALBLbType_Type = CucsOsLBType
_CucsOsEthBondModeBalancedALBLbType_Object = MibTableColumn
cucsOsEthBondModeBalancedALBLbType = _CucsOsEthBondModeBalancedALBLbType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 11, 1, 4),
    _CucsOsEthBondModeBalancedALBLbType_Type()
)
cucsOsEthBondModeBalancedALBLbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedALBLbType.setStatus("current")
_CucsOsEthBondModeBalancedALBName_Type = SnmpAdminString
_CucsOsEthBondModeBalancedALBName_Object = MibTableColumn
cucsOsEthBondModeBalancedALBName = _CucsOsEthBondModeBalancedALBName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 11, 1, 5),
    _CucsOsEthBondModeBalancedALBName_Type()
)
cucsOsEthBondModeBalancedALBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedALBName.setStatus("current")
_CucsOsEthBondModeBalancedALBType_Type = CucsOsEthBondModeLBType
_CucsOsEthBondModeBalancedALBType_Object = MibTableColumn
cucsOsEthBondModeBalancedALBType = _CucsOsEthBondModeBalancedALBType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 11, 1, 6),
    _CucsOsEthBondModeBalancedALBType_Type()
)
cucsOsEthBondModeBalancedALBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedALBType.setStatus("current")
_CucsOsEthBondModeBalancedALBXmitHashType_Type = CucsOsEthBondModeLBXmitHashType
_CucsOsEthBondModeBalancedALBXmitHashType_Object = MibTableColumn
cucsOsEthBondModeBalancedALBXmitHashType = _CucsOsEthBondModeBalancedALBXmitHashType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 11, 1, 7),
    _CucsOsEthBondModeBalancedALBXmitHashType_Type()
)
cucsOsEthBondModeBalancedALBXmitHashType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedALBXmitHashType.setStatus("current")
_CucsOsEthBondModeBalancedRRTable_Object = MibTable
cucsOsEthBondModeBalancedRRTable = _CucsOsEthBondModeBalancedRRTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 12)
)
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedRRTable.setStatus("current")
_CucsOsEthBondModeBalancedRREntry_Object = MibTableRow
cucsOsEthBondModeBalancedRREntry = _CucsOsEthBondModeBalancedRREntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 12, 1)
)
cucsOsEthBondModeBalancedRREntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OS-MIB", "cucsOsEthBondModeBalancedRRInstanceId"),
)
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedRREntry.setStatus("current")
_CucsOsEthBondModeBalancedRRInstanceId_Type = CucsManagedObjectId
_CucsOsEthBondModeBalancedRRInstanceId_Object = MibTableColumn
cucsOsEthBondModeBalancedRRInstanceId = _CucsOsEthBondModeBalancedRRInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 12, 1, 1),
    _CucsOsEthBondModeBalancedRRInstanceId_Type()
)
cucsOsEthBondModeBalancedRRInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedRRInstanceId.setStatus("current")
_CucsOsEthBondModeBalancedRRDn_Type = CucsManagedObjectDn
_CucsOsEthBondModeBalancedRRDn_Object = MibTableColumn
cucsOsEthBondModeBalancedRRDn = _CucsOsEthBondModeBalancedRRDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 12, 1, 2),
    _CucsOsEthBondModeBalancedRRDn_Type()
)
cucsOsEthBondModeBalancedRRDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedRRDn.setStatus("current")
_CucsOsEthBondModeBalancedRRRn_Type = SnmpAdminString
_CucsOsEthBondModeBalancedRRRn_Object = MibTableColumn
cucsOsEthBondModeBalancedRRRn = _CucsOsEthBondModeBalancedRRRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 12, 1, 3),
    _CucsOsEthBondModeBalancedRRRn_Type()
)
cucsOsEthBondModeBalancedRRRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedRRRn.setStatus("current")
_CucsOsEthBondModeBalancedRRIgmpResendCount_Type = Gauge32
_CucsOsEthBondModeBalancedRRIgmpResendCount_Object = MibTableColumn
cucsOsEthBondModeBalancedRRIgmpResendCount = _CucsOsEthBondModeBalancedRRIgmpResendCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 12, 1, 4),
    _CucsOsEthBondModeBalancedRRIgmpResendCount_Type()
)
cucsOsEthBondModeBalancedRRIgmpResendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedRRIgmpResendCount.setStatus("current")
_CucsOsEthBondModeBalancedRRName_Type = SnmpAdminString
_CucsOsEthBondModeBalancedRRName_Object = MibTableColumn
cucsOsEthBondModeBalancedRRName = _CucsOsEthBondModeBalancedRRName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 12, 1, 5),
    _CucsOsEthBondModeBalancedRRName_Type()
)
cucsOsEthBondModeBalancedRRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedRRName.setStatus("current")
_CucsOsEthBondModeBalancedRRPktsPerSlave_Type = Gauge32
_CucsOsEthBondModeBalancedRRPktsPerSlave_Object = MibTableColumn
cucsOsEthBondModeBalancedRRPktsPerSlave = _CucsOsEthBondModeBalancedRRPktsPerSlave_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 12, 1, 6),
    _CucsOsEthBondModeBalancedRRPktsPerSlave_Type()
)
cucsOsEthBondModeBalancedRRPktsPerSlave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedRRPktsPerSlave.setStatus("current")
_CucsOsEthBondModeBalancedRRType_Type = CucsOsEthBondModeBalancedRRType
_CucsOsEthBondModeBalancedRRType_Object = MibTableColumn
cucsOsEthBondModeBalancedRRType = _CucsOsEthBondModeBalancedRRType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 12, 1, 7),
    _CucsOsEthBondModeBalancedRRType_Type()
)
cucsOsEthBondModeBalancedRRType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedRRType.setStatus("current")
_CucsOsEthBondModeBalancedTLBTable_Object = MibTable
cucsOsEthBondModeBalancedTLBTable = _CucsOsEthBondModeBalancedTLBTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 13)
)
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedTLBTable.setStatus("current")
_CucsOsEthBondModeBalancedTLBEntry_Object = MibTableRow
cucsOsEthBondModeBalancedTLBEntry = _CucsOsEthBondModeBalancedTLBEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 13, 1)
)
cucsOsEthBondModeBalancedTLBEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OS-MIB", "cucsOsEthBondModeBalancedTLBInstanceId"),
)
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedTLBEntry.setStatus("current")
_CucsOsEthBondModeBalancedTLBInstanceId_Type = CucsManagedObjectId
_CucsOsEthBondModeBalancedTLBInstanceId_Object = MibTableColumn
cucsOsEthBondModeBalancedTLBInstanceId = _CucsOsEthBondModeBalancedTLBInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 13, 1, 1),
    _CucsOsEthBondModeBalancedTLBInstanceId_Type()
)
cucsOsEthBondModeBalancedTLBInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedTLBInstanceId.setStatus("current")
_CucsOsEthBondModeBalancedTLBDn_Type = CucsManagedObjectDn
_CucsOsEthBondModeBalancedTLBDn_Object = MibTableColumn
cucsOsEthBondModeBalancedTLBDn = _CucsOsEthBondModeBalancedTLBDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 13, 1, 2),
    _CucsOsEthBondModeBalancedTLBDn_Type()
)
cucsOsEthBondModeBalancedTLBDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedTLBDn.setStatus("current")
_CucsOsEthBondModeBalancedTLBRn_Type = SnmpAdminString
_CucsOsEthBondModeBalancedTLBRn_Object = MibTableColumn
cucsOsEthBondModeBalancedTLBRn = _CucsOsEthBondModeBalancedTLBRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 13, 1, 3),
    _CucsOsEthBondModeBalancedTLBRn_Type()
)
cucsOsEthBondModeBalancedTLBRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedTLBRn.setStatus("current")
_CucsOsEthBondModeBalancedTLBIgmpResendCount_Type = Gauge32
_CucsOsEthBondModeBalancedTLBIgmpResendCount_Object = MibTableColumn
cucsOsEthBondModeBalancedTLBIgmpResendCount = _CucsOsEthBondModeBalancedTLBIgmpResendCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 13, 1, 4),
    _CucsOsEthBondModeBalancedTLBIgmpResendCount_Type()
)
cucsOsEthBondModeBalancedTLBIgmpResendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedTLBIgmpResendCount.setStatus("current")
_CucsOsEthBondModeBalancedTLBLbType_Type = CucsOsLBType
_CucsOsEthBondModeBalancedTLBLbType_Object = MibTableColumn
cucsOsEthBondModeBalancedTLBLbType = _CucsOsEthBondModeBalancedTLBLbType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 13, 1, 5),
    _CucsOsEthBondModeBalancedTLBLbType_Type()
)
cucsOsEthBondModeBalancedTLBLbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedTLBLbType.setStatus("current")
_CucsOsEthBondModeBalancedTLBLpInterval_Type = Gauge32
_CucsOsEthBondModeBalancedTLBLpInterval_Object = MibTableColumn
cucsOsEthBondModeBalancedTLBLpInterval = _CucsOsEthBondModeBalancedTLBLpInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 13, 1, 6),
    _CucsOsEthBondModeBalancedTLBLpInterval_Type()
)
cucsOsEthBondModeBalancedTLBLpInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedTLBLpInterval.setStatus("current")
_CucsOsEthBondModeBalancedTLBName_Type = SnmpAdminString
_CucsOsEthBondModeBalancedTLBName_Object = MibTableColumn
cucsOsEthBondModeBalancedTLBName = _CucsOsEthBondModeBalancedTLBName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 13, 1, 7),
    _CucsOsEthBondModeBalancedTLBName_Type()
)
cucsOsEthBondModeBalancedTLBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedTLBName.setStatus("current")
_CucsOsEthBondModeBalancedTLBType_Type = CucsOsEthBondModeLBType
_CucsOsEthBondModeBalancedTLBType_Object = MibTableColumn
cucsOsEthBondModeBalancedTLBType = _CucsOsEthBondModeBalancedTLBType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 13, 1, 8),
    _CucsOsEthBondModeBalancedTLBType_Type()
)
cucsOsEthBondModeBalancedTLBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedTLBType.setStatus("current")
_CucsOsEthBondModeBalancedTLBXmitHashType_Type = CucsOsEthBondModeLBXmitHashType
_CucsOsEthBondModeBalancedTLBXmitHashType_Object = MibTableColumn
cucsOsEthBondModeBalancedTLBXmitHashType = _CucsOsEthBondModeBalancedTLBXmitHashType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 13, 1, 9),
    _CucsOsEthBondModeBalancedTLBXmitHashType_Type()
)
cucsOsEthBondModeBalancedTLBXmitHashType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedTLBXmitHashType.setStatus("current")
_CucsOsEthBondModeBalancedXORTable_Object = MibTable
cucsOsEthBondModeBalancedXORTable = _CucsOsEthBondModeBalancedXORTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 14)
)
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedXORTable.setStatus("current")
_CucsOsEthBondModeBalancedXOREntry_Object = MibTableRow
cucsOsEthBondModeBalancedXOREntry = _CucsOsEthBondModeBalancedXOREntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 14, 1)
)
cucsOsEthBondModeBalancedXOREntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OS-MIB", "cucsOsEthBondModeBalancedXORInstanceId"),
)
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedXOREntry.setStatus("current")
_CucsOsEthBondModeBalancedXORInstanceId_Type = CucsManagedObjectId
_CucsOsEthBondModeBalancedXORInstanceId_Object = MibTableColumn
cucsOsEthBondModeBalancedXORInstanceId = _CucsOsEthBondModeBalancedXORInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 14, 1, 1),
    _CucsOsEthBondModeBalancedXORInstanceId_Type()
)
cucsOsEthBondModeBalancedXORInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedXORInstanceId.setStatus("current")
_CucsOsEthBondModeBalancedXORDn_Type = CucsManagedObjectDn
_CucsOsEthBondModeBalancedXORDn_Object = MibTableColumn
cucsOsEthBondModeBalancedXORDn = _CucsOsEthBondModeBalancedXORDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 14, 1, 2),
    _CucsOsEthBondModeBalancedXORDn_Type()
)
cucsOsEthBondModeBalancedXORDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedXORDn.setStatus("current")
_CucsOsEthBondModeBalancedXORRn_Type = SnmpAdminString
_CucsOsEthBondModeBalancedXORRn_Object = MibTableColumn
cucsOsEthBondModeBalancedXORRn = _CucsOsEthBondModeBalancedXORRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 14, 1, 3),
    _CucsOsEthBondModeBalancedXORRn_Type()
)
cucsOsEthBondModeBalancedXORRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedXORRn.setStatus("current")
_CucsOsEthBondModeBalancedXORLbType_Type = CucsOsLBType
_CucsOsEthBondModeBalancedXORLbType_Object = MibTableColumn
cucsOsEthBondModeBalancedXORLbType = _CucsOsEthBondModeBalancedXORLbType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 14, 1, 4),
    _CucsOsEthBondModeBalancedXORLbType_Type()
)
cucsOsEthBondModeBalancedXORLbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedXORLbType.setStatus("current")
_CucsOsEthBondModeBalancedXORName_Type = SnmpAdminString
_CucsOsEthBondModeBalancedXORName_Object = MibTableColumn
cucsOsEthBondModeBalancedXORName = _CucsOsEthBondModeBalancedXORName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 14, 1, 5),
    _CucsOsEthBondModeBalancedXORName_Type()
)
cucsOsEthBondModeBalancedXORName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedXORName.setStatus("current")
_CucsOsEthBondModeBalancedXORType_Type = CucsOsEthBondModeLBType
_CucsOsEthBondModeBalancedXORType_Object = MibTableColumn
cucsOsEthBondModeBalancedXORType = _CucsOsEthBondModeBalancedXORType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 14, 1, 6),
    _CucsOsEthBondModeBalancedXORType_Type()
)
cucsOsEthBondModeBalancedXORType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedXORType.setStatus("current")
_CucsOsEthBondModeBalancedXORXmitHashType_Type = CucsOsEthBondModeLBXmitHashType
_CucsOsEthBondModeBalancedXORXmitHashType_Object = MibTableColumn
cucsOsEthBondModeBalancedXORXmitHashType = _CucsOsEthBondModeBalancedXORXmitHashType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 14, 1, 7),
    _CucsOsEthBondModeBalancedXORXmitHashType_Type()
)
cucsOsEthBondModeBalancedXORXmitHashType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBalancedXORXmitHashType.setStatus("current")
_CucsOsEthBondModeBroadcastTable_Object = MibTable
cucsOsEthBondModeBroadcastTable = _CucsOsEthBondModeBroadcastTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 15)
)
if mibBuilder.loadTexts:
    cucsOsEthBondModeBroadcastTable.setStatus("current")
_CucsOsEthBondModeBroadcastEntry_Object = MibTableRow
cucsOsEthBondModeBroadcastEntry = _CucsOsEthBondModeBroadcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 15, 1)
)
cucsOsEthBondModeBroadcastEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OS-MIB", "cucsOsEthBondModeBroadcastInstanceId"),
)
if mibBuilder.loadTexts:
    cucsOsEthBondModeBroadcastEntry.setStatus("current")
_CucsOsEthBondModeBroadcastInstanceId_Type = CucsManagedObjectId
_CucsOsEthBondModeBroadcastInstanceId_Object = MibTableColumn
cucsOsEthBondModeBroadcastInstanceId = _CucsOsEthBondModeBroadcastInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 15, 1, 1),
    _CucsOsEthBondModeBroadcastInstanceId_Type()
)
cucsOsEthBondModeBroadcastInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBroadcastInstanceId.setStatus("current")
_CucsOsEthBondModeBroadcastDn_Type = CucsManagedObjectDn
_CucsOsEthBondModeBroadcastDn_Object = MibTableColumn
cucsOsEthBondModeBroadcastDn = _CucsOsEthBondModeBroadcastDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 15, 1, 2),
    _CucsOsEthBondModeBroadcastDn_Type()
)
cucsOsEthBondModeBroadcastDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBroadcastDn.setStatus("current")
_CucsOsEthBondModeBroadcastRn_Type = SnmpAdminString
_CucsOsEthBondModeBroadcastRn_Object = MibTableColumn
cucsOsEthBondModeBroadcastRn = _CucsOsEthBondModeBroadcastRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 15, 1, 3),
    _CucsOsEthBondModeBroadcastRn_Type()
)
cucsOsEthBondModeBroadcastRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBroadcastRn.setStatus("current")
_CucsOsEthBondModeBroadcastName_Type = SnmpAdminString
_CucsOsEthBondModeBroadcastName_Object = MibTableColumn
cucsOsEthBondModeBroadcastName = _CucsOsEthBondModeBroadcastName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 15, 1, 4),
    _CucsOsEthBondModeBroadcastName_Type()
)
cucsOsEthBondModeBroadcastName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBroadcastName.setStatus("current")
_CucsOsEthBondModeBroadcastType_Type = CucsOsEthBondModeBroadcastType
_CucsOsEthBondModeBroadcastType_Object = MibTableColumn
cucsOsEthBondModeBroadcastType = _CucsOsEthBondModeBroadcastType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 15, 1, 5),
    _CucsOsEthBondModeBroadcastType_Type()
)
cucsOsEthBondModeBroadcastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthBondModeBroadcastType.setStatus("current")
_CucsOsEthIntfTable_Object = MibTable
cucsOsEthIntfTable = _CucsOsEthIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 16)
)
if mibBuilder.loadTexts:
    cucsOsEthIntfTable.setStatus("current")
_CucsOsEthIntfEntry_Object = MibTableRow
cucsOsEthIntfEntry = _CucsOsEthIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 16, 1)
)
cucsOsEthIntfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OS-MIB", "cucsOsEthIntfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsOsEthIntfEntry.setStatus("current")
_CucsOsEthIntfInstanceId_Type = CucsManagedObjectId
_CucsOsEthIntfInstanceId_Object = MibTableColumn
cucsOsEthIntfInstanceId = _CucsOsEthIntfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 16, 1, 1),
    _CucsOsEthIntfInstanceId_Type()
)
cucsOsEthIntfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsOsEthIntfInstanceId.setStatus("current")
_CucsOsEthIntfDn_Type = CucsManagedObjectDn
_CucsOsEthIntfDn_Object = MibTableColumn
cucsOsEthIntfDn = _CucsOsEthIntfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 16, 1, 2),
    _CucsOsEthIntfDn_Type()
)
cucsOsEthIntfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthIntfDn.setStatus("current")
_CucsOsEthIntfRn_Type = SnmpAdminString
_CucsOsEthIntfRn_Object = MibTableColumn
cucsOsEthIntfRn = _CucsOsEthIntfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 16, 1, 3),
    _CucsOsEthIntfRn_Type()
)
cucsOsEthIntfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthIntfRn.setStatus("current")
_CucsOsEthIntfAddr_Type = MacAddress
_CucsOsEthIntfAddr_Object = MibTableColumn
cucsOsEthIntfAddr = _CucsOsEthIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 16, 1, 4),
    _CucsOsEthIntfAddr_Type()
)
cucsOsEthIntfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthIntfAddr.setStatus("current")
_CucsOsEthIntfMtu_Type = Gauge32
_CucsOsEthIntfMtu_Object = MibTableColumn
cucsOsEthIntfMtu = _CucsOsEthIntfMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 16, 1, 5),
    _CucsOsEthIntfMtu_Type()
)
cucsOsEthIntfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthIntfMtu.setStatus("current")
_CucsOsEthIntfName_Type = SnmpAdminString
_CucsOsEthIntfName_Object = MibTableColumn
cucsOsEthIntfName = _CucsOsEthIntfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 16, 1, 6),
    _CucsOsEthIntfName_Type()
)
cucsOsEthIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthIntfName.setStatus("current")
_CucsOsEthIntfOperState_Type = CucsVnicIfOperState
_CucsOsEthIntfOperState_Object = MibTableColumn
cucsOsEthIntfOperState = _CucsOsEthIntfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 16, 1, 7),
    _CucsOsEthIntfOperState_Type()
)
cucsOsEthIntfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthIntfOperState.setStatus("current")
_CucsOsEthIntfTransport_Type = CucsNetworkTransport
_CucsOsEthIntfTransport_Object = MibTableColumn
cucsOsEthIntfTransport = _CucsOsEthIntfTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 16, 1, 8),
    _CucsOsEthIntfTransport_Type()
)
cucsOsEthIntfTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthIntfTransport.setStatus("current")
_CucsOsEthIntfType_Type = CucsNetworkConnectionType
_CucsOsEthIntfType_Object = MibTableColumn
cucsOsEthIntfType = _CucsOsEthIntfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 16, 1, 9),
    _CucsOsEthIntfType_Type()
)
cucsOsEthIntfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsEthIntfType.setStatus("current")
_CucsOsMiiLinkMonitoringPolicyTable_Object = MibTable
cucsOsMiiLinkMonitoringPolicyTable = _CucsOsMiiLinkMonitoringPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 18)
)
if mibBuilder.loadTexts:
    cucsOsMiiLinkMonitoringPolicyTable.setStatus("current")
_CucsOsMiiLinkMonitoringPolicyEntry_Object = MibTableRow
cucsOsMiiLinkMonitoringPolicyEntry = _CucsOsMiiLinkMonitoringPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 18, 1)
)
cucsOsMiiLinkMonitoringPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OS-MIB", "cucsOsMiiLinkMonitoringPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsOsMiiLinkMonitoringPolicyEntry.setStatus("current")
_CucsOsMiiLinkMonitoringPolicyInstanceId_Type = CucsManagedObjectId
_CucsOsMiiLinkMonitoringPolicyInstanceId_Object = MibTableColumn
cucsOsMiiLinkMonitoringPolicyInstanceId = _CucsOsMiiLinkMonitoringPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 18, 1, 1),
    _CucsOsMiiLinkMonitoringPolicyInstanceId_Type()
)
cucsOsMiiLinkMonitoringPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsOsMiiLinkMonitoringPolicyInstanceId.setStatus("current")
_CucsOsMiiLinkMonitoringPolicyDn_Type = CucsManagedObjectDn
_CucsOsMiiLinkMonitoringPolicyDn_Object = MibTableColumn
cucsOsMiiLinkMonitoringPolicyDn = _CucsOsMiiLinkMonitoringPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 18, 1, 2),
    _CucsOsMiiLinkMonitoringPolicyDn_Type()
)
cucsOsMiiLinkMonitoringPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsMiiLinkMonitoringPolicyDn.setStatus("current")
_CucsOsMiiLinkMonitoringPolicyRn_Type = SnmpAdminString
_CucsOsMiiLinkMonitoringPolicyRn_Object = MibTableColumn
cucsOsMiiLinkMonitoringPolicyRn = _CucsOsMiiLinkMonitoringPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 18, 1, 3),
    _CucsOsMiiLinkMonitoringPolicyRn_Type()
)
cucsOsMiiLinkMonitoringPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsMiiLinkMonitoringPolicyRn.setStatus("current")
_CucsOsMiiLinkMonitoringPolicyFrequency_Type = Gauge32
_CucsOsMiiLinkMonitoringPolicyFrequency_Object = MibTableColumn
cucsOsMiiLinkMonitoringPolicyFrequency = _CucsOsMiiLinkMonitoringPolicyFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 18, 1, 4),
    _CucsOsMiiLinkMonitoringPolicyFrequency_Type()
)
cucsOsMiiLinkMonitoringPolicyFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsMiiLinkMonitoringPolicyFrequency.setStatus("current")
_CucsOsMiiLinkMonitoringPolicyLinkDownDelay_Type = Gauge32
_CucsOsMiiLinkMonitoringPolicyLinkDownDelay_Object = MibTableColumn
cucsOsMiiLinkMonitoringPolicyLinkDownDelay = _CucsOsMiiLinkMonitoringPolicyLinkDownDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 18, 1, 5),
    _CucsOsMiiLinkMonitoringPolicyLinkDownDelay_Type()
)
cucsOsMiiLinkMonitoringPolicyLinkDownDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsMiiLinkMonitoringPolicyLinkDownDelay.setStatus("current")
_CucsOsMiiLinkMonitoringPolicyLinkStatusQueryType_Type = CucsOsCarrierQueryMethod
_CucsOsMiiLinkMonitoringPolicyLinkStatusQueryType_Object = MibTableColumn
cucsOsMiiLinkMonitoringPolicyLinkStatusQueryType = _CucsOsMiiLinkMonitoringPolicyLinkStatusQueryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 18, 1, 6),
    _CucsOsMiiLinkMonitoringPolicyLinkStatusQueryType_Type()
)
cucsOsMiiLinkMonitoringPolicyLinkStatusQueryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsMiiLinkMonitoringPolicyLinkStatusQueryType.setStatus("current")
_CucsOsMiiLinkMonitoringPolicyLinkUpDelay_Type = Gauge32
_CucsOsMiiLinkMonitoringPolicyLinkUpDelay_Object = MibTableColumn
cucsOsMiiLinkMonitoringPolicyLinkUpDelay = _CucsOsMiiLinkMonitoringPolicyLinkUpDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 18, 1, 7),
    _CucsOsMiiLinkMonitoringPolicyLinkUpDelay_Type()
)
cucsOsMiiLinkMonitoringPolicyLinkUpDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsMiiLinkMonitoringPolicyLinkUpDelay.setStatus("current")
_CucsOsMiiLinkMonitoringPolicyName_Type = SnmpAdminString
_CucsOsMiiLinkMonitoringPolicyName_Object = MibTableColumn
cucsOsMiiLinkMonitoringPolicyName = _CucsOsMiiLinkMonitoringPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 18, 1, 8),
    _CucsOsMiiLinkMonitoringPolicyName_Type()
)
cucsOsMiiLinkMonitoringPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsMiiLinkMonitoringPolicyName.setStatus("current")
_CucsOsPrimarySlaveTable_Object = MibTable
cucsOsPrimarySlaveTable = _CucsOsPrimarySlaveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 19)
)
if mibBuilder.loadTexts:
    cucsOsPrimarySlaveTable.setStatus("current")
_CucsOsPrimarySlaveEntry_Object = MibTableRow
cucsOsPrimarySlaveEntry = _CucsOsPrimarySlaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 19, 1)
)
cucsOsPrimarySlaveEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OS-MIB", "cucsOsPrimarySlaveInstanceId"),
)
if mibBuilder.loadTexts:
    cucsOsPrimarySlaveEntry.setStatus("current")
_CucsOsPrimarySlaveInstanceId_Type = CucsManagedObjectId
_CucsOsPrimarySlaveInstanceId_Object = MibTableColumn
cucsOsPrimarySlaveInstanceId = _CucsOsPrimarySlaveInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 19, 1, 1),
    _CucsOsPrimarySlaveInstanceId_Type()
)
cucsOsPrimarySlaveInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsOsPrimarySlaveInstanceId.setStatus("current")
_CucsOsPrimarySlaveDn_Type = CucsManagedObjectDn
_CucsOsPrimarySlaveDn_Object = MibTableColumn
cucsOsPrimarySlaveDn = _CucsOsPrimarySlaveDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 19, 1, 2),
    _CucsOsPrimarySlaveDn_Type()
)
cucsOsPrimarySlaveDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsPrimarySlaveDn.setStatus("current")
_CucsOsPrimarySlaveRn_Type = SnmpAdminString
_CucsOsPrimarySlaveRn_Object = MibTableColumn
cucsOsPrimarySlaveRn = _CucsOsPrimarySlaveRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 19, 1, 3),
    _CucsOsPrimarySlaveRn_Type()
)
cucsOsPrimarySlaveRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsPrimarySlaveRn.setStatus("current")
_CucsOsPrimarySlaveName_Type = SnmpAdminString
_CucsOsPrimarySlaveName_Object = MibTableColumn
cucsOsPrimarySlaveName = _CucsOsPrimarySlaveName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 19, 1, 4),
    _CucsOsPrimarySlaveName_Type()
)
cucsOsPrimarySlaveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsPrimarySlaveName.setStatus("current")
_CucsOsPrimarySlaveReselectPolicy_Type = CucsOsPrimaryReselection
_CucsOsPrimarySlaveReselectPolicy_Object = MibTableColumn
cucsOsPrimarySlaveReselectPolicy = _CucsOsPrimarySlaveReselectPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 35, 19, 1, 5),
    _CucsOsPrimarySlaveReselectPolicy_Type()
)
cucsOsPrimarySlaveReselectPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOsPrimarySlaveReselectPolicy.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-OS-MIB",
    **{"cucsOsObjects": cucsOsObjects,
       "cucsOsAgentTable": cucsOsAgentTable,
       "cucsOsAgentEntry": cucsOsAgentEntry,
       "cucsOsAgentInstanceId": cucsOsAgentInstanceId,
       "cucsOsAgentDn": cucsOsAgentDn,
       "cucsOsAgentRn": cucsOsAgentRn,
       "cucsOsAgentLastCmd": cucsOsAgentLastCmd,
       "cucsOsAgentLastEvt": cucsOsAgentLastEvt,
       "cucsOsAgentLastEvtTs": cucsOsAgentLastEvtTs,
       "cucsOsAgentPrevCmd": cucsOsAgentPrevCmd,
       "cucsOsAgentPrevEvt": cucsOsAgentPrevEvt,
       "cucsOsAgentType": cucsOsAgentType,
       "cucsOsAgentVendor": cucsOsAgentVendor,
       "cucsOsAgentVersion": cucsOsAgentVersion,
       "cucsOsInstanceTable": cucsOsInstanceTable,
       "cucsOsInstanceEntry": cucsOsInstanceEntry,
       "cucsOsInstanceInstanceId": cucsOsInstanceInstanceId,
       "cucsOsInstanceDn": cucsOsInstanceDn,
       "cucsOsInstanceRn": cucsOsInstanceRn,
       "cucsOsInstanceHostname": cucsOsInstanceHostname,
       "cucsOsInstanceKernelName": cucsOsInstanceKernelName,
       "cucsOsInstanceKernelRelease": cucsOsInstanceKernelRelease,
       "cucsOsInstanceKernelVersion": cucsOsInstanceKernelVersion,
       "cucsOsInstanceName": cucsOsInstanceName,
       "cucsOsInstanceType": cucsOsInstanceType,
       "cucsOsARPLinkMonitoringPolicyTable": cucsOsARPLinkMonitoringPolicyTable,
       "cucsOsARPLinkMonitoringPolicyEntry": cucsOsARPLinkMonitoringPolicyEntry,
       "cucsOsARPLinkMonitoringPolicyInstanceId": cucsOsARPLinkMonitoringPolicyInstanceId,
       "cucsOsARPLinkMonitoringPolicyDn": cucsOsARPLinkMonitoringPolicyDn,
       "cucsOsARPLinkMonitoringPolicyRn": cucsOsARPLinkMonitoringPolicyRn,
       "cucsOsARPLinkMonitoringPolicyFrequency": cucsOsARPLinkMonitoringPolicyFrequency,
       "cucsOsARPLinkMonitoringPolicyName": cucsOsARPLinkMonitoringPolicyName,
       "cucsOsARPLinkMonitoringPolicyUseAllARPTargets": cucsOsARPLinkMonitoringPolicyUseAllARPTargets,
       "cucsOsARPTargetTable": cucsOsARPTargetTable,
       "cucsOsARPTargetEntry": cucsOsARPTargetEntry,
       "cucsOsARPTargetInstanceId": cucsOsARPTargetInstanceId,
       "cucsOsARPTargetDn": cucsOsARPTargetDn,
       "cucsOsARPTargetRn": cucsOsARPTargetRn,
       "cucsOsARPTargetHostName": cucsOsARPTargetHostName,
       "cucsOsARPTargetName": cucsOsARPTargetName,
       "cucsOsEthBondIntfTable": cucsOsEthBondIntfTable,
       "cucsOsEthBondIntfEntry": cucsOsEthBondIntfEntry,
       "cucsOsEthBondIntfInstanceId": cucsOsEthBondIntfInstanceId,
       "cucsOsEthBondIntfDn": cucsOsEthBondIntfDn,
       "cucsOsEthBondIntfRn": cucsOsEthBondIntfRn,
       "cucsOsEthBondIntfAddr": cucsOsEthBondIntfAddr,
       "cucsOsEthBondIntfMaxBonds": cucsOsEthBondIntfMaxBonds,
       "cucsOsEthBondIntfMtu": cucsOsEthBondIntfMtu,
       "cucsOsEthBondIntfName": cucsOsEthBondIntfName,
       "cucsOsEthBondIntfOperState": cucsOsEthBondIntfOperState,
       "cucsOsEthBondIntfTransport": cucsOsEthBondIntfTransport,
       "cucsOsEthBondIntfType": cucsOsEthBondIntfType,
       "cucsOsEthBondModeActiveBackupTable": cucsOsEthBondModeActiveBackupTable,
       "cucsOsEthBondModeActiveBackupEntry": cucsOsEthBondModeActiveBackupEntry,
       "cucsOsEthBondModeActiveBackupInstanceId": cucsOsEthBondModeActiveBackupInstanceId,
       "cucsOsEthBondModeActiveBackupDn": cucsOsEthBondModeActiveBackupDn,
       "cucsOsEthBondModeActiveBackupRn": cucsOsEthBondModeActiveBackupRn,
       "cucsOsEthBondModeActiveBackupMacAddressPolicy": cucsOsEthBondModeActiveBackupMacAddressPolicy,
       "cucsOsEthBondModeActiveBackupName": cucsOsEthBondModeActiveBackupName,
       "cucsOsEthBondModeActiveBackupNumPeerNotifications": cucsOsEthBondModeActiveBackupNumPeerNotifications,
       "cucsOsEthBondModeActiveBackupType": cucsOsEthBondModeActiveBackupType,
       "cucsOsEthBondModeBalancedALBTable": cucsOsEthBondModeBalancedALBTable,
       "cucsOsEthBondModeBalancedALBEntry": cucsOsEthBondModeBalancedALBEntry,
       "cucsOsEthBondModeBalancedALBInstanceId": cucsOsEthBondModeBalancedALBInstanceId,
       "cucsOsEthBondModeBalancedALBDn": cucsOsEthBondModeBalancedALBDn,
       "cucsOsEthBondModeBalancedALBRn": cucsOsEthBondModeBalancedALBRn,
       "cucsOsEthBondModeBalancedALBLbType": cucsOsEthBondModeBalancedALBLbType,
       "cucsOsEthBondModeBalancedALBName": cucsOsEthBondModeBalancedALBName,
       "cucsOsEthBondModeBalancedALBType": cucsOsEthBondModeBalancedALBType,
       "cucsOsEthBondModeBalancedALBXmitHashType": cucsOsEthBondModeBalancedALBXmitHashType,
       "cucsOsEthBondModeBalancedRRTable": cucsOsEthBondModeBalancedRRTable,
       "cucsOsEthBondModeBalancedRREntry": cucsOsEthBondModeBalancedRREntry,
       "cucsOsEthBondModeBalancedRRInstanceId": cucsOsEthBondModeBalancedRRInstanceId,
       "cucsOsEthBondModeBalancedRRDn": cucsOsEthBondModeBalancedRRDn,
       "cucsOsEthBondModeBalancedRRRn": cucsOsEthBondModeBalancedRRRn,
       "cucsOsEthBondModeBalancedRRIgmpResendCount": cucsOsEthBondModeBalancedRRIgmpResendCount,
       "cucsOsEthBondModeBalancedRRName": cucsOsEthBondModeBalancedRRName,
       "cucsOsEthBondModeBalancedRRPktsPerSlave": cucsOsEthBondModeBalancedRRPktsPerSlave,
       "cucsOsEthBondModeBalancedRRType": cucsOsEthBondModeBalancedRRType,
       "cucsOsEthBondModeBalancedTLBTable": cucsOsEthBondModeBalancedTLBTable,
       "cucsOsEthBondModeBalancedTLBEntry": cucsOsEthBondModeBalancedTLBEntry,
       "cucsOsEthBondModeBalancedTLBInstanceId": cucsOsEthBondModeBalancedTLBInstanceId,
       "cucsOsEthBondModeBalancedTLBDn": cucsOsEthBondModeBalancedTLBDn,
       "cucsOsEthBondModeBalancedTLBRn": cucsOsEthBondModeBalancedTLBRn,
       "cucsOsEthBondModeBalancedTLBIgmpResendCount": cucsOsEthBondModeBalancedTLBIgmpResendCount,
       "cucsOsEthBondModeBalancedTLBLbType": cucsOsEthBondModeBalancedTLBLbType,
       "cucsOsEthBondModeBalancedTLBLpInterval": cucsOsEthBondModeBalancedTLBLpInterval,
       "cucsOsEthBondModeBalancedTLBName": cucsOsEthBondModeBalancedTLBName,
       "cucsOsEthBondModeBalancedTLBType": cucsOsEthBondModeBalancedTLBType,
       "cucsOsEthBondModeBalancedTLBXmitHashType": cucsOsEthBondModeBalancedTLBXmitHashType,
       "cucsOsEthBondModeBalancedXORTable": cucsOsEthBondModeBalancedXORTable,
       "cucsOsEthBondModeBalancedXOREntry": cucsOsEthBondModeBalancedXOREntry,
       "cucsOsEthBondModeBalancedXORInstanceId": cucsOsEthBondModeBalancedXORInstanceId,
       "cucsOsEthBondModeBalancedXORDn": cucsOsEthBondModeBalancedXORDn,
       "cucsOsEthBondModeBalancedXORRn": cucsOsEthBondModeBalancedXORRn,
       "cucsOsEthBondModeBalancedXORLbType": cucsOsEthBondModeBalancedXORLbType,
       "cucsOsEthBondModeBalancedXORName": cucsOsEthBondModeBalancedXORName,
       "cucsOsEthBondModeBalancedXORType": cucsOsEthBondModeBalancedXORType,
       "cucsOsEthBondModeBalancedXORXmitHashType": cucsOsEthBondModeBalancedXORXmitHashType,
       "cucsOsEthBondModeBroadcastTable": cucsOsEthBondModeBroadcastTable,
       "cucsOsEthBondModeBroadcastEntry": cucsOsEthBondModeBroadcastEntry,
       "cucsOsEthBondModeBroadcastInstanceId": cucsOsEthBondModeBroadcastInstanceId,
       "cucsOsEthBondModeBroadcastDn": cucsOsEthBondModeBroadcastDn,
       "cucsOsEthBondModeBroadcastRn": cucsOsEthBondModeBroadcastRn,
       "cucsOsEthBondModeBroadcastName": cucsOsEthBondModeBroadcastName,
       "cucsOsEthBondModeBroadcastType": cucsOsEthBondModeBroadcastType,
       "cucsOsEthIntfTable": cucsOsEthIntfTable,
       "cucsOsEthIntfEntry": cucsOsEthIntfEntry,
       "cucsOsEthIntfInstanceId": cucsOsEthIntfInstanceId,
       "cucsOsEthIntfDn": cucsOsEthIntfDn,
       "cucsOsEthIntfRn": cucsOsEthIntfRn,
       "cucsOsEthIntfAddr": cucsOsEthIntfAddr,
       "cucsOsEthIntfMtu": cucsOsEthIntfMtu,
       "cucsOsEthIntfName": cucsOsEthIntfName,
       "cucsOsEthIntfOperState": cucsOsEthIntfOperState,
       "cucsOsEthIntfTransport": cucsOsEthIntfTransport,
       "cucsOsEthIntfType": cucsOsEthIntfType,
       "cucsOsMiiLinkMonitoringPolicyTable": cucsOsMiiLinkMonitoringPolicyTable,
       "cucsOsMiiLinkMonitoringPolicyEntry": cucsOsMiiLinkMonitoringPolicyEntry,
       "cucsOsMiiLinkMonitoringPolicyInstanceId": cucsOsMiiLinkMonitoringPolicyInstanceId,
       "cucsOsMiiLinkMonitoringPolicyDn": cucsOsMiiLinkMonitoringPolicyDn,
       "cucsOsMiiLinkMonitoringPolicyRn": cucsOsMiiLinkMonitoringPolicyRn,
       "cucsOsMiiLinkMonitoringPolicyFrequency": cucsOsMiiLinkMonitoringPolicyFrequency,
       "cucsOsMiiLinkMonitoringPolicyLinkDownDelay": cucsOsMiiLinkMonitoringPolicyLinkDownDelay,
       "cucsOsMiiLinkMonitoringPolicyLinkStatusQueryType": cucsOsMiiLinkMonitoringPolicyLinkStatusQueryType,
       "cucsOsMiiLinkMonitoringPolicyLinkUpDelay": cucsOsMiiLinkMonitoringPolicyLinkUpDelay,
       "cucsOsMiiLinkMonitoringPolicyName": cucsOsMiiLinkMonitoringPolicyName,
       "cucsOsPrimarySlaveTable": cucsOsPrimarySlaveTable,
       "cucsOsPrimarySlaveEntry": cucsOsPrimarySlaveEntry,
       "cucsOsPrimarySlaveInstanceId": cucsOsPrimarySlaveInstanceId,
       "cucsOsPrimarySlaveDn": cucsOsPrimarySlaveDn,
       "cucsOsPrimarySlaveRn": cucsOsPrimarySlaveRn,
       "cucsOsPrimarySlaveName": cucsOsPrimarySlaveName,
       "cucsOsPrimarySlaveReselectPolicy": cucsOsPrimarySlaveReselectPolicy}
)
