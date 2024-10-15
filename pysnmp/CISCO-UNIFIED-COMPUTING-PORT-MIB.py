# SNMP MIB module (CISCO-UNIFIED-COMPUTING-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:10 2024
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

(CucsConditionRemoteInvRslt,
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus,
 CucsLicenseState,
 CucsNetworkConnectionType,
 CucsNetworkLocale,
 CucsNetworkPortRole,
 CucsNetworkPortType,
 CucsNetworkSwitchId,
 CucsNetworkTransport,
 CucsPortGroupType,
 CucsPortPIoFsmCurrentFsm,
 CucsPortPIoFsmStageName,
 CucsPortPIoFsmTaskItem,
 CucsPortSubGroupConfigState,
 CucsPortSubGroupSlotId,
 CucsPortTrust) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsLicenseState",
    "CucsNetworkConnectionType",
    "CucsNetworkLocale",
    "CucsNetworkPortRole",
    "CucsNetworkPortType",
    "CucsNetworkSwitchId",
    "CucsNetworkTransport",
    "CucsPortGroupType",
    "CucsPortPIoFsmCurrentFsm",
    "CucsPortPIoFsmStageName",
    "CucsPortPIoFsmTaskItem",
    "CucsPortSubGroupConfigState",
    "CucsPortSubGroupSlotId",
    "CucsPortTrust")

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

cucsPortObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsPortDomainEpTable_Object = MibTable
cucsPortDomainEpTable = _CucsPortDomainEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1)
)
if mibBuilder.loadTexts:
    cucsPortDomainEpTable.setStatus("current")
_CucsPortDomainEpEntry_Object = MibTableRow
cucsPortDomainEpEntry = _CucsPortDomainEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1)
)
cucsPortDomainEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PORT-MIB", "cucsPortDomainEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPortDomainEpEntry.setStatus("current")
_CucsPortDomainEpInstanceId_Type = CucsManagedObjectId
_CucsPortDomainEpInstanceId_Object = MibTableColumn
cucsPortDomainEpInstanceId = _CucsPortDomainEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 1),
    _CucsPortDomainEpInstanceId_Type()
)
cucsPortDomainEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPortDomainEpInstanceId.setStatus("current")
_CucsPortDomainEpDn_Type = CucsManagedObjectDn
_CucsPortDomainEpDn_Object = MibTableColumn
cucsPortDomainEpDn = _CucsPortDomainEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 2),
    _CucsPortDomainEpDn_Type()
)
cucsPortDomainEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortDomainEpDn.setStatus("current")
_CucsPortDomainEpRn_Type = SnmpAdminString
_CucsPortDomainEpRn_Object = MibTableColumn
cucsPortDomainEpRn = _CucsPortDomainEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 3),
    _CucsPortDomainEpRn_Type()
)
cucsPortDomainEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortDomainEpRn.setStatus("current")
_CucsPortDomainEpEpDn_Type = SnmpAdminString
_CucsPortDomainEpEpDn_Object = MibTableColumn
cucsPortDomainEpEpDn = _CucsPortDomainEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 4),
    _CucsPortDomainEpEpDn_Type()
)
cucsPortDomainEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortDomainEpEpDn.setStatus("current")
_CucsPortDomainEpIfRole_Type = CucsNetworkPortRole
_CucsPortDomainEpIfRole_Object = MibTableColumn
cucsPortDomainEpIfRole = _CucsPortDomainEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 5),
    _CucsPortDomainEpIfRole_Type()
)
cucsPortDomainEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortDomainEpIfRole.setStatus("current")
_CucsPortDomainEpIfType_Type = CucsNetworkPortType
_CucsPortDomainEpIfType_Object = MibTableColumn
cucsPortDomainEpIfType = _CucsPortDomainEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 6),
    _CucsPortDomainEpIfType_Type()
)
cucsPortDomainEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortDomainEpIfType.setStatus("current")
_CucsPortDomainEpLocale_Type = CucsNetworkLocale
_CucsPortDomainEpLocale_Object = MibTableColumn
cucsPortDomainEpLocale = _CucsPortDomainEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 7),
    _CucsPortDomainEpLocale_Type()
)
cucsPortDomainEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortDomainEpLocale.setStatus("current")
_CucsPortDomainEpName_Type = SnmpAdminString
_CucsPortDomainEpName_Object = MibTableColumn
cucsPortDomainEpName = _CucsPortDomainEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 8),
    _CucsPortDomainEpName_Type()
)
cucsPortDomainEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortDomainEpName.setStatus("current")
_CucsPortDomainEpPeerDn_Type = SnmpAdminString
_CucsPortDomainEpPeerDn_Object = MibTableColumn
cucsPortDomainEpPeerDn = _CucsPortDomainEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 9),
    _CucsPortDomainEpPeerDn_Type()
)
cucsPortDomainEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortDomainEpPeerDn.setStatus("current")
_CucsPortDomainEpTransport_Type = CucsNetworkTransport
_CucsPortDomainEpTransport_Object = MibTableColumn
cucsPortDomainEpTransport = _CucsPortDomainEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 10),
    _CucsPortDomainEpTransport_Type()
)
cucsPortDomainEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortDomainEpTransport.setStatus("current")
_CucsPortDomainEpType_Type = CucsNetworkConnectionType
_CucsPortDomainEpType_Object = MibTableColumn
cucsPortDomainEpType = _CucsPortDomainEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 11),
    _CucsPortDomainEpType_Type()
)
cucsPortDomainEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortDomainEpType.setStatus("current")
_CucsPortGroupTable_Object = MibTable
cucsPortGroupTable = _CucsPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2)
)
if mibBuilder.loadTexts:
    cucsPortGroupTable.setStatus("current")
_CucsPortGroupEntry_Object = MibTableRow
cucsPortGroupEntry = _CucsPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2, 1)
)
cucsPortGroupEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PORT-MIB", "cucsPortGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPortGroupEntry.setStatus("current")
_CucsPortGroupInstanceId_Type = CucsManagedObjectId
_CucsPortGroupInstanceId_Object = MibTableColumn
cucsPortGroupInstanceId = _CucsPortGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2, 1, 1),
    _CucsPortGroupInstanceId_Type()
)
cucsPortGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPortGroupInstanceId.setStatus("current")
_CucsPortGroupDn_Type = CucsManagedObjectDn
_CucsPortGroupDn_Object = MibTableColumn
cucsPortGroupDn = _CucsPortGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2, 1, 2),
    _CucsPortGroupDn_Type()
)
cucsPortGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortGroupDn.setStatus("current")
_CucsPortGroupRn_Type = SnmpAdminString
_CucsPortGroupRn_Object = MibTableColumn
cucsPortGroupRn = _CucsPortGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2, 1, 3),
    _CucsPortGroupRn_Type()
)
cucsPortGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortGroupRn.setStatus("current")
_CucsPortGroupLocale_Type = CucsNetworkLocale
_CucsPortGroupLocale_Object = MibTableColumn
cucsPortGroupLocale = _CucsPortGroupLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2, 1, 4),
    _CucsPortGroupLocale_Type()
)
cucsPortGroupLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortGroupLocale.setStatus("current")
_CucsPortGroupName_Type = SnmpAdminString
_CucsPortGroupName_Object = MibTableColumn
cucsPortGroupName = _CucsPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2, 1, 5),
    _CucsPortGroupName_Type()
)
cucsPortGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortGroupName.setStatus("current")
_CucsPortGroupTransport_Type = CucsNetworkTransport
_CucsPortGroupTransport_Object = MibTableColumn
cucsPortGroupTransport = _CucsPortGroupTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2, 1, 6),
    _CucsPortGroupTransport_Type()
)
cucsPortGroupTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortGroupTransport.setStatus("current")
_CucsPortGroupType_Type = CucsPortGroupType
_CucsPortGroupType_Object = MibTableColumn
cucsPortGroupType = _CucsPortGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2, 1, 7),
    _CucsPortGroupType_Type()
)
cucsPortGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortGroupType.setStatus("current")
_CucsPortTrustModeTable_Object = MibTable
cucsPortTrustModeTable = _CucsPortTrustModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 3)
)
if mibBuilder.loadTexts:
    cucsPortTrustModeTable.setStatus("current")
_CucsPortTrustModeEntry_Object = MibTableRow
cucsPortTrustModeEntry = _CucsPortTrustModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 3, 1)
)
cucsPortTrustModeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PORT-MIB", "cucsPortTrustModeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPortTrustModeEntry.setStatus("current")
_CucsPortTrustModeInstanceId_Type = CucsManagedObjectId
_CucsPortTrustModeInstanceId_Object = MibTableColumn
cucsPortTrustModeInstanceId = _CucsPortTrustModeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 3, 1, 1),
    _CucsPortTrustModeInstanceId_Type()
)
cucsPortTrustModeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPortTrustModeInstanceId.setStatus("current")
_CucsPortTrustModeDn_Type = CucsManagedObjectDn
_CucsPortTrustModeDn_Object = MibTableColumn
cucsPortTrustModeDn = _CucsPortTrustModeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 3, 1, 2),
    _CucsPortTrustModeDn_Type()
)
cucsPortTrustModeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortTrustModeDn.setStatus("current")
_CucsPortTrustModeRn_Type = SnmpAdminString
_CucsPortTrustModeRn_Object = MibTableColumn
cucsPortTrustModeRn = _CucsPortTrustModeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 3, 1, 3),
    _CucsPortTrustModeRn_Type()
)
cucsPortTrustModeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortTrustModeRn.setStatus("current")
_CucsPortTrustModeState_Type = CucsPortTrust
_CucsPortTrustModeState_Object = MibTableColumn
cucsPortTrustModeState = _CucsPortTrustModeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 3, 1, 4),
    _CucsPortTrustModeState_Type()
)
cucsPortTrustModeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortTrustModeState.setStatus("current")
_CucsPortPIoFsmTaskTable_Object = MibTable
cucsPortPIoFsmTaskTable = _CucsPortPIoFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4)
)
if mibBuilder.loadTexts:
    cucsPortPIoFsmTaskTable.setStatus("current")
_CucsPortPIoFsmTaskEntry_Object = MibTableRow
cucsPortPIoFsmTaskEntry = _CucsPortPIoFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4, 1)
)
cucsPortPIoFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PORT-MIB", "cucsPortPIoFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPortPIoFsmTaskEntry.setStatus("current")
_CucsPortPIoFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsPortPIoFsmTaskInstanceId_Object = MibTableColumn
cucsPortPIoFsmTaskInstanceId = _CucsPortPIoFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4, 1, 1),
    _CucsPortPIoFsmTaskInstanceId_Type()
)
cucsPortPIoFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPortPIoFsmTaskInstanceId.setStatus("current")
_CucsPortPIoFsmTaskDn_Type = CucsManagedObjectDn
_CucsPortPIoFsmTaskDn_Object = MibTableColumn
cucsPortPIoFsmTaskDn = _CucsPortPIoFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4, 1, 2),
    _CucsPortPIoFsmTaskDn_Type()
)
cucsPortPIoFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmTaskDn.setStatus("current")
_CucsPortPIoFsmTaskRn_Type = SnmpAdminString
_CucsPortPIoFsmTaskRn_Object = MibTableColumn
cucsPortPIoFsmTaskRn = _CucsPortPIoFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4, 1, 3),
    _CucsPortPIoFsmTaskRn_Type()
)
cucsPortPIoFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmTaskRn.setStatus("current")
_CucsPortPIoFsmTaskCompletion_Type = CucsFsmCompletion
_CucsPortPIoFsmTaskCompletion_Object = MibTableColumn
cucsPortPIoFsmTaskCompletion = _CucsPortPIoFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4, 1, 4),
    _CucsPortPIoFsmTaskCompletion_Type()
)
cucsPortPIoFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmTaskCompletion.setStatus("current")
_CucsPortPIoFsmTaskFlags_Type = CucsFsmFlags
_CucsPortPIoFsmTaskFlags_Object = MibTableColumn
cucsPortPIoFsmTaskFlags = _CucsPortPIoFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4, 1, 5),
    _CucsPortPIoFsmTaskFlags_Type()
)
cucsPortPIoFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmTaskFlags.setStatus("current")
_CucsPortPIoFsmTaskItem_Type = CucsPortPIoFsmTaskItem
_CucsPortPIoFsmTaskItem_Object = MibTableColumn
cucsPortPIoFsmTaskItem = _CucsPortPIoFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4, 1, 6),
    _CucsPortPIoFsmTaskItem_Type()
)
cucsPortPIoFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmTaskItem.setStatus("current")
_CucsPortPIoFsmTaskSeqId_Type = Gauge32
_CucsPortPIoFsmTaskSeqId_Object = MibTableColumn
cucsPortPIoFsmTaskSeqId = _CucsPortPIoFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4, 1, 7),
    _CucsPortPIoFsmTaskSeqId_Type()
)
cucsPortPIoFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmTaskSeqId.setStatus("current")
_CucsPortPIoFsmTable_Object = MibTable
cucsPortPIoFsmTable = _CucsPortPIoFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5)
)
if mibBuilder.loadTexts:
    cucsPortPIoFsmTable.setStatus("current")
_CucsPortPIoFsmEntry_Object = MibTableRow
cucsPortPIoFsmEntry = _CucsPortPIoFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1)
)
cucsPortPIoFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PORT-MIB", "cucsPortPIoFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPortPIoFsmEntry.setStatus("current")
_CucsPortPIoFsmInstanceId_Type = CucsManagedObjectId
_CucsPortPIoFsmInstanceId_Object = MibTableColumn
cucsPortPIoFsmInstanceId = _CucsPortPIoFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 1),
    _CucsPortPIoFsmInstanceId_Type()
)
cucsPortPIoFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPortPIoFsmInstanceId.setStatus("current")
_CucsPortPIoFsmDn_Type = CucsManagedObjectDn
_CucsPortPIoFsmDn_Object = MibTableColumn
cucsPortPIoFsmDn = _CucsPortPIoFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 2),
    _CucsPortPIoFsmDn_Type()
)
cucsPortPIoFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmDn.setStatus("current")
_CucsPortPIoFsmRn_Type = SnmpAdminString
_CucsPortPIoFsmRn_Object = MibTableColumn
cucsPortPIoFsmRn = _CucsPortPIoFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 3),
    _CucsPortPIoFsmRn_Type()
)
cucsPortPIoFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmRn.setStatus("current")
_CucsPortPIoFsmCompletionTime_Type = DateAndTime
_CucsPortPIoFsmCompletionTime_Object = MibTableColumn
cucsPortPIoFsmCompletionTime = _CucsPortPIoFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 4),
    _CucsPortPIoFsmCompletionTime_Type()
)
cucsPortPIoFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmCompletionTime.setStatus("current")
_CucsPortPIoFsmCurrentFsm_Type = CucsPortPIoFsmCurrentFsm
_CucsPortPIoFsmCurrentFsm_Object = MibTableColumn
cucsPortPIoFsmCurrentFsm = _CucsPortPIoFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 5),
    _CucsPortPIoFsmCurrentFsm_Type()
)
cucsPortPIoFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmCurrentFsm.setStatus("current")
_CucsPortPIoFsmDescr_Type = SnmpAdminString
_CucsPortPIoFsmDescr_Object = MibTableColumn
cucsPortPIoFsmDescr = _CucsPortPIoFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 6),
    _CucsPortPIoFsmDescr_Type()
)
cucsPortPIoFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmDescr.setStatus("current")
_CucsPortPIoFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsPortPIoFsmFsmStatus_Object = MibTableColumn
cucsPortPIoFsmFsmStatus = _CucsPortPIoFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 7),
    _CucsPortPIoFsmFsmStatus_Type()
)
cucsPortPIoFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmFsmStatus.setStatus("current")
_CucsPortPIoFsmProgress_Type = Gauge32
_CucsPortPIoFsmProgress_Object = MibTableColumn
cucsPortPIoFsmProgress = _CucsPortPIoFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 8),
    _CucsPortPIoFsmProgress_Type()
)
cucsPortPIoFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmProgress.setStatus("current")
_CucsPortPIoFsmRmtErrCode_Type = Gauge32
_CucsPortPIoFsmRmtErrCode_Object = MibTableColumn
cucsPortPIoFsmRmtErrCode = _CucsPortPIoFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 9),
    _CucsPortPIoFsmRmtErrCode_Type()
)
cucsPortPIoFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmRmtErrCode.setStatus("current")
_CucsPortPIoFsmRmtErrDescr_Type = SnmpAdminString
_CucsPortPIoFsmRmtErrDescr_Object = MibTableColumn
cucsPortPIoFsmRmtErrDescr = _CucsPortPIoFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 10),
    _CucsPortPIoFsmRmtErrDescr_Type()
)
cucsPortPIoFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmRmtErrDescr.setStatus("current")
_CucsPortPIoFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsPortPIoFsmRmtRslt_Object = MibTableColumn
cucsPortPIoFsmRmtRslt = _CucsPortPIoFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 11),
    _CucsPortPIoFsmRmtRslt_Type()
)
cucsPortPIoFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmRmtRslt.setStatus("current")
_CucsPortPIoFsmStageTable_Object = MibTable
cucsPortPIoFsmStageTable = _CucsPortPIoFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6)
)
if mibBuilder.loadTexts:
    cucsPortPIoFsmStageTable.setStatus("current")
_CucsPortPIoFsmStageEntry_Object = MibTableRow
cucsPortPIoFsmStageEntry = _CucsPortPIoFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1)
)
cucsPortPIoFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PORT-MIB", "cucsPortPIoFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPortPIoFsmStageEntry.setStatus("current")
_CucsPortPIoFsmStageInstanceId_Type = CucsManagedObjectId
_CucsPortPIoFsmStageInstanceId_Object = MibTableColumn
cucsPortPIoFsmStageInstanceId = _CucsPortPIoFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 1),
    _CucsPortPIoFsmStageInstanceId_Type()
)
cucsPortPIoFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPortPIoFsmStageInstanceId.setStatus("current")
_CucsPortPIoFsmStageDn_Type = CucsManagedObjectDn
_CucsPortPIoFsmStageDn_Object = MibTableColumn
cucsPortPIoFsmStageDn = _CucsPortPIoFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 2),
    _CucsPortPIoFsmStageDn_Type()
)
cucsPortPIoFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmStageDn.setStatus("current")
_CucsPortPIoFsmStageRn_Type = SnmpAdminString
_CucsPortPIoFsmStageRn_Object = MibTableColumn
cucsPortPIoFsmStageRn = _CucsPortPIoFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 3),
    _CucsPortPIoFsmStageRn_Type()
)
cucsPortPIoFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmStageRn.setStatus("current")
_CucsPortPIoFsmStageDescr_Type = SnmpAdminString
_CucsPortPIoFsmStageDescr_Object = MibTableColumn
cucsPortPIoFsmStageDescr = _CucsPortPIoFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 4),
    _CucsPortPIoFsmStageDescr_Type()
)
cucsPortPIoFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmStageDescr.setStatus("current")
_CucsPortPIoFsmStageLastUpdateTime_Type = DateAndTime
_CucsPortPIoFsmStageLastUpdateTime_Object = MibTableColumn
cucsPortPIoFsmStageLastUpdateTime = _CucsPortPIoFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 5),
    _CucsPortPIoFsmStageLastUpdateTime_Type()
)
cucsPortPIoFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmStageLastUpdateTime.setStatus("current")
_CucsPortPIoFsmStageName_Type = CucsPortPIoFsmStageName
_CucsPortPIoFsmStageName_Object = MibTableColumn
cucsPortPIoFsmStageName = _CucsPortPIoFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 6),
    _CucsPortPIoFsmStageName_Type()
)
cucsPortPIoFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmStageName.setStatus("current")
_CucsPortPIoFsmStageOrder_Type = Gauge32
_CucsPortPIoFsmStageOrder_Object = MibTableColumn
cucsPortPIoFsmStageOrder = _CucsPortPIoFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 7),
    _CucsPortPIoFsmStageOrder_Type()
)
cucsPortPIoFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmStageOrder.setStatus("current")
_CucsPortPIoFsmStageRetry_Type = Gauge32
_CucsPortPIoFsmStageRetry_Object = MibTableColumn
cucsPortPIoFsmStageRetry = _CucsPortPIoFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 8),
    _CucsPortPIoFsmStageRetry_Type()
)
cucsPortPIoFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmStageRetry.setStatus("current")
_CucsPortPIoFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsPortPIoFsmStageStageStatus_Object = MibTableColumn
cucsPortPIoFsmStageStageStatus = _CucsPortPIoFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 9),
    _CucsPortPIoFsmStageStageStatus_Type()
)
cucsPortPIoFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortPIoFsmStageStageStatus.setStatus("current")
_CucsPortSubGroupTable_Object = MibTable
cucsPortSubGroupTable = _CucsPortSubGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7)
)
if mibBuilder.loadTexts:
    cucsPortSubGroupTable.setStatus("current")
_CucsPortSubGroupEntry_Object = MibTableRow
cucsPortSubGroupEntry = _CucsPortSubGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1)
)
cucsPortSubGroupEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PORT-MIB", "cucsPortSubGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPortSubGroupEntry.setStatus("current")
_CucsPortSubGroupInstanceId_Type = CucsManagedObjectId
_CucsPortSubGroupInstanceId_Object = MibTableColumn
cucsPortSubGroupInstanceId = _CucsPortSubGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 1),
    _CucsPortSubGroupInstanceId_Type()
)
cucsPortSubGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPortSubGroupInstanceId.setStatus("current")
_CucsPortSubGroupDn_Type = CucsManagedObjectDn
_CucsPortSubGroupDn_Object = MibTableColumn
cucsPortSubGroupDn = _CucsPortSubGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 2),
    _CucsPortSubGroupDn_Type()
)
cucsPortSubGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortSubGroupDn.setStatus("current")
_CucsPortSubGroupRn_Type = SnmpAdminString
_CucsPortSubGroupRn_Object = MibTableColumn
cucsPortSubGroupRn = _CucsPortSubGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 3),
    _CucsPortSubGroupRn_Type()
)
cucsPortSubGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortSubGroupRn.setStatus("current")
_CucsPortSubGroupAggrPortId_Type = Gauge32
_CucsPortSubGroupAggrPortId_Object = MibTableColumn
cucsPortSubGroupAggrPortId = _CucsPortSubGroupAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 4),
    _CucsPortSubGroupAggrPortId_Type()
)
cucsPortSubGroupAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortSubGroupAggrPortId.setStatus("current")
_CucsPortSubGroupConfigState_Type = CucsPortSubGroupConfigState
_CucsPortSubGroupConfigState_Object = MibTableColumn
cucsPortSubGroupConfigState = _CucsPortSubGroupConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 5),
    _CucsPortSubGroupConfigState_Type()
)
cucsPortSubGroupConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortSubGroupConfigState.setStatus("current")
_CucsPortSubGroupLicGP_Type = Unsigned64
_CucsPortSubGroupLicGP_Object = MibTableColumn
cucsPortSubGroupLicGP = _CucsPortSubGroupLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 6),
    _CucsPortSubGroupLicGP_Type()
)
cucsPortSubGroupLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortSubGroupLicGP.setStatus("current")
_CucsPortSubGroupLicState_Type = CucsLicenseState
_CucsPortSubGroupLicState_Object = MibTableColumn
cucsPortSubGroupLicState = _CucsPortSubGroupLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 7),
    _CucsPortSubGroupLicState_Type()
)
cucsPortSubGroupLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortSubGroupLicState.setStatus("current")
_CucsPortSubGroupLocale_Type = CucsNetworkLocale
_CucsPortSubGroupLocale_Object = MibTableColumn
cucsPortSubGroupLocale = _CucsPortSubGroupLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 8),
    _CucsPortSubGroupLocale_Type()
)
cucsPortSubGroupLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortSubGroupLocale.setStatus("current")
_CucsPortSubGroupName_Type = SnmpAdminString
_CucsPortSubGroupName_Object = MibTableColumn
cucsPortSubGroupName = _CucsPortSubGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 9),
    _CucsPortSubGroupName_Type()
)
cucsPortSubGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortSubGroupName.setStatus("current")
_CucsPortSubGroupSlotId_Type = CucsPortSubGroupSlotId
_CucsPortSubGroupSlotId_Object = MibTableColumn
cucsPortSubGroupSlotId = _CucsPortSubGroupSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 10),
    _CucsPortSubGroupSlotId_Type()
)
cucsPortSubGroupSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortSubGroupSlotId.setStatus("current")
_CucsPortSubGroupSwitchId_Type = CucsNetworkSwitchId
_CucsPortSubGroupSwitchId_Object = MibTableColumn
cucsPortSubGroupSwitchId = _CucsPortSubGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 11),
    _CucsPortSubGroupSwitchId_Type()
)
cucsPortSubGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortSubGroupSwitchId.setStatus("current")
_CucsPortSubGroupTransport_Type = CucsNetworkTransport
_CucsPortSubGroupTransport_Object = MibTableColumn
cucsPortSubGroupTransport = _CucsPortSubGroupTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 12),
    _CucsPortSubGroupTransport_Type()
)
cucsPortSubGroupTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortSubGroupTransport.setStatus("current")
_CucsPortSubGroupType_Type = CucsNetworkConnectionType
_CucsPortSubGroupType_Object = MibTableColumn
cucsPortSubGroupType = _CucsPortSubGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 13),
    _CucsPortSubGroupType_Type()
)
cucsPortSubGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPortSubGroupType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-PORT-MIB",
    **{"cucsPortObjects": cucsPortObjects,
       "cucsPortDomainEpTable": cucsPortDomainEpTable,
       "cucsPortDomainEpEntry": cucsPortDomainEpEntry,
       "cucsPortDomainEpInstanceId": cucsPortDomainEpInstanceId,
       "cucsPortDomainEpDn": cucsPortDomainEpDn,
       "cucsPortDomainEpRn": cucsPortDomainEpRn,
       "cucsPortDomainEpEpDn": cucsPortDomainEpEpDn,
       "cucsPortDomainEpIfRole": cucsPortDomainEpIfRole,
       "cucsPortDomainEpIfType": cucsPortDomainEpIfType,
       "cucsPortDomainEpLocale": cucsPortDomainEpLocale,
       "cucsPortDomainEpName": cucsPortDomainEpName,
       "cucsPortDomainEpPeerDn": cucsPortDomainEpPeerDn,
       "cucsPortDomainEpTransport": cucsPortDomainEpTransport,
       "cucsPortDomainEpType": cucsPortDomainEpType,
       "cucsPortGroupTable": cucsPortGroupTable,
       "cucsPortGroupEntry": cucsPortGroupEntry,
       "cucsPortGroupInstanceId": cucsPortGroupInstanceId,
       "cucsPortGroupDn": cucsPortGroupDn,
       "cucsPortGroupRn": cucsPortGroupRn,
       "cucsPortGroupLocale": cucsPortGroupLocale,
       "cucsPortGroupName": cucsPortGroupName,
       "cucsPortGroupTransport": cucsPortGroupTransport,
       "cucsPortGroupType": cucsPortGroupType,
       "cucsPortTrustModeTable": cucsPortTrustModeTable,
       "cucsPortTrustModeEntry": cucsPortTrustModeEntry,
       "cucsPortTrustModeInstanceId": cucsPortTrustModeInstanceId,
       "cucsPortTrustModeDn": cucsPortTrustModeDn,
       "cucsPortTrustModeRn": cucsPortTrustModeRn,
       "cucsPortTrustModeState": cucsPortTrustModeState,
       "cucsPortPIoFsmTaskTable": cucsPortPIoFsmTaskTable,
       "cucsPortPIoFsmTaskEntry": cucsPortPIoFsmTaskEntry,
       "cucsPortPIoFsmTaskInstanceId": cucsPortPIoFsmTaskInstanceId,
       "cucsPortPIoFsmTaskDn": cucsPortPIoFsmTaskDn,
       "cucsPortPIoFsmTaskRn": cucsPortPIoFsmTaskRn,
       "cucsPortPIoFsmTaskCompletion": cucsPortPIoFsmTaskCompletion,
       "cucsPortPIoFsmTaskFlags": cucsPortPIoFsmTaskFlags,
       "cucsPortPIoFsmTaskItem": cucsPortPIoFsmTaskItem,
       "cucsPortPIoFsmTaskSeqId": cucsPortPIoFsmTaskSeqId,
       "cucsPortPIoFsmTable": cucsPortPIoFsmTable,
       "cucsPortPIoFsmEntry": cucsPortPIoFsmEntry,
       "cucsPortPIoFsmInstanceId": cucsPortPIoFsmInstanceId,
       "cucsPortPIoFsmDn": cucsPortPIoFsmDn,
       "cucsPortPIoFsmRn": cucsPortPIoFsmRn,
       "cucsPortPIoFsmCompletionTime": cucsPortPIoFsmCompletionTime,
       "cucsPortPIoFsmCurrentFsm": cucsPortPIoFsmCurrentFsm,
       "cucsPortPIoFsmDescr": cucsPortPIoFsmDescr,
       "cucsPortPIoFsmFsmStatus": cucsPortPIoFsmFsmStatus,
       "cucsPortPIoFsmProgress": cucsPortPIoFsmProgress,
       "cucsPortPIoFsmRmtErrCode": cucsPortPIoFsmRmtErrCode,
       "cucsPortPIoFsmRmtErrDescr": cucsPortPIoFsmRmtErrDescr,
       "cucsPortPIoFsmRmtRslt": cucsPortPIoFsmRmtRslt,
       "cucsPortPIoFsmStageTable": cucsPortPIoFsmStageTable,
       "cucsPortPIoFsmStageEntry": cucsPortPIoFsmStageEntry,
       "cucsPortPIoFsmStageInstanceId": cucsPortPIoFsmStageInstanceId,
       "cucsPortPIoFsmStageDn": cucsPortPIoFsmStageDn,
       "cucsPortPIoFsmStageRn": cucsPortPIoFsmStageRn,
       "cucsPortPIoFsmStageDescr": cucsPortPIoFsmStageDescr,
       "cucsPortPIoFsmStageLastUpdateTime": cucsPortPIoFsmStageLastUpdateTime,
       "cucsPortPIoFsmStageName": cucsPortPIoFsmStageName,
       "cucsPortPIoFsmStageOrder": cucsPortPIoFsmStageOrder,
       "cucsPortPIoFsmStageRetry": cucsPortPIoFsmStageRetry,
       "cucsPortPIoFsmStageStageStatus": cucsPortPIoFsmStageStageStatus,
       "cucsPortSubGroupTable": cucsPortSubGroupTable,
       "cucsPortSubGroupEntry": cucsPortSubGroupEntry,
       "cucsPortSubGroupInstanceId": cucsPortSubGroupInstanceId,
       "cucsPortSubGroupDn": cucsPortSubGroupDn,
       "cucsPortSubGroupRn": cucsPortSubGroupRn,
       "cucsPortSubGroupAggrPortId": cucsPortSubGroupAggrPortId,
       "cucsPortSubGroupConfigState": cucsPortSubGroupConfigState,
       "cucsPortSubGroupLicGP": cucsPortSubGroupLicGP,
       "cucsPortSubGroupLicState": cucsPortSubGroupLicState,
       "cucsPortSubGroupLocale": cucsPortSubGroupLocale,
       "cucsPortSubGroupName": cucsPortSubGroupName,
       "cucsPortSubGroupSlotId": cucsPortSubGroupSlotId,
       "cucsPortSubGroupSwitchId": cucsPortSubGroupSwitchId,
       "cucsPortSubGroupTransport": cucsPortSubGroupTransport,
       "cucsPortSubGroupType": cucsPortSubGroupType}
)
