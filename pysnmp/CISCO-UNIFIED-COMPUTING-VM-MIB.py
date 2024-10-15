# SNMP MIB module (CISCO-UNIFIED-COMPUTING-VM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-VM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:30 2024
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

(CucsAdaptorLinkState,
 CucsConditionRemoteInvRslt,
 CucsDcxOperState,
 CucsExtvmmOwnership,
 CucsFabricAVlanAssocPrimaryVlanSwitchId,
 CucsFabricAVlanSharing,
 CucsFabricAVlanTransport,
 CucsFabricAVlanType,
 CucsFabricAVsanTransport,
 CucsFabricAVsanType,
 CucsFabricVlanAssocPrimaryVlanState,
 CucsFabricVlanOperState,
 CucsFabricVlanOverlapState,
 CucsFabricVnetEpIfRole,
 CucsFabricVnetEpLocale,
 CucsFabricVnetEpPolicyOwner,
 CucsFabricVsanOperState,
 CucsFabricZoningState,
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus,
 CucsNetworkSwitchId,
 CucsNetworkVnetEpIfType,
 CucsOsOsType,
 CucsPolicyPolicyOwner,
 CucsVmAdaptorOwner,
 CucsVmComputeEpClInstType,
 CucsVmHbaType,
 CucsVmHvClInstType,
 CucsVmHvType,
 CucsVmInstType,
 CucsVmLifeCyclePolicyFsmCurrentFsm,
 CucsVmLifeCyclePolicyFsmStageName,
 CucsVmLifeCyclePolicyFsmTaskItem,
 CucsVmMgmtPlane,
 CucsVmNicType,
 CucsVmOsHvVendor,
 CucsVmStatus,
 CucsVmSwitchAdminState,
 CucsVmSwitchVendor,
 CucsVnicPortProfileType) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsAdaptorLinkState",
    "CucsConditionRemoteInvRslt",
    "CucsDcxOperState",
    "CucsExtvmmOwnership",
    "CucsFabricAVlanAssocPrimaryVlanSwitchId",
    "CucsFabricAVlanSharing",
    "CucsFabricAVlanTransport",
    "CucsFabricAVlanType",
    "CucsFabricAVsanTransport",
    "CucsFabricAVsanType",
    "CucsFabricVlanAssocPrimaryVlanState",
    "CucsFabricVlanOperState",
    "CucsFabricVlanOverlapState",
    "CucsFabricVnetEpIfRole",
    "CucsFabricVnetEpLocale",
    "CucsFabricVnetEpPolicyOwner",
    "CucsFabricVsanOperState",
    "CucsFabricZoningState",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsNetworkSwitchId",
    "CucsNetworkVnetEpIfType",
    "CucsOsOsType",
    "CucsPolicyPolicyOwner",
    "CucsVmAdaptorOwner",
    "CucsVmComputeEpClInstType",
    "CucsVmHbaType",
    "CucsVmHvClInstType",
    "CucsVmHvType",
    "CucsVmInstType",
    "CucsVmLifeCyclePolicyFsmCurrentFsm",
    "CucsVmLifeCyclePolicyFsmStageName",
    "CucsVmLifeCyclePolicyFsmTaskItem",
    "CucsVmMgmtPlane",
    "CucsVmNicType",
    "CucsVmOsHvVendor",
    "CucsVmStatus",
    "CucsVmSwitchAdminState",
    "CucsVmSwitchVendor",
    "CucsVnicPortProfileType")

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

cucsVmObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsVmDCTable_Object = MibTable
cucsVmDCTable = _CucsVmDCTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 1)
)
if mibBuilder.loadTexts:
    cucsVmDCTable.setStatus("current")
_CucsVmDCEntry_Object = MibTableRow
cucsVmDCEntry = _CucsVmDCEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 1, 1)
)
cucsVmDCEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmDCInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmDCEntry.setStatus("current")
_CucsVmDCInstanceId_Type = CucsManagedObjectId
_CucsVmDCInstanceId_Object = MibTableColumn
cucsVmDCInstanceId = _CucsVmDCInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 1, 1, 1),
    _CucsVmDCInstanceId_Type()
)
cucsVmDCInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmDCInstanceId.setStatus("current")
_CucsVmDCDn_Type = CucsManagedObjectDn
_CucsVmDCDn_Object = MibTableColumn
cucsVmDCDn = _CucsVmDCDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 1, 1, 2),
    _CucsVmDCDn_Type()
)
cucsVmDCDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCDn.setStatus("current")
_CucsVmDCRn_Type = SnmpAdminString
_CucsVmDCRn_Object = MibTableColumn
cucsVmDCRn = _CucsVmDCRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 1, 1, 3),
    _CucsVmDCRn_Type()
)
cucsVmDCRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCRn.setStatus("current")
_CucsVmDCDescr_Type = SnmpAdminString
_CucsVmDCDescr_Object = MibTableColumn
cucsVmDCDescr = _CucsVmDCDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 1, 1, 4),
    _CucsVmDCDescr_Type()
)
cucsVmDCDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCDescr.setStatus("current")
_CucsVmDCIntId_Type = SnmpAdminString
_CucsVmDCIntId_Object = MibTableColumn
cucsVmDCIntId = _CucsVmDCIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 1, 1, 5),
    _CucsVmDCIntId_Type()
)
cucsVmDCIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCIntId.setStatus("current")
_CucsVmDCName_Type = SnmpAdminString
_CucsVmDCName_Object = MibTableColumn
cucsVmDCName = _CucsVmDCName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 1, 1, 6),
    _CucsVmDCName_Type()
)
cucsVmDCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCName.setStatus("current")
_CucsVmDCOwn_Type = CucsExtvmmOwnership
_CucsVmDCOwn_Object = MibTableColumn
cucsVmDCOwn = _CucsVmDCOwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 1, 1, 7),
    _CucsVmDCOwn_Type()
)
cucsVmDCOwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCOwn.setStatus("current")
_CucsVmDCUuid_Type = SnmpAdminString
_CucsVmDCUuid_Object = MibTableColumn
cucsVmDCUuid = _CucsVmDCUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 1, 1, 8),
    _CucsVmDCUuid_Type()
)
cucsVmDCUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCUuid.setStatus("current")
_CucsVmDCPolicyLevel_Type = Gauge32
_CucsVmDCPolicyLevel_Object = MibTableColumn
cucsVmDCPolicyLevel = _CucsVmDCPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 1, 1, 9),
    _CucsVmDCPolicyLevel_Type()
)
cucsVmDCPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCPolicyLevel.setStatus("current")
_CucsVmDCPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVmDCPolicyOwner_Object = MibTableColumn
cucsVmDCPolicyOwner = _CucsVmDCPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 1, 1, 10),
    _CucsVmDCPolicyOwner_Type()
)
cucsVmDCPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCPolicyOwner.setStatus("current")
_CucsVmDCOrgTable_Object = MibTable
cucsVmDCOrgTable = _CucsVmDCOrgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 2)
)
if mibBuilder.loadTexts:
    cucsVmDCOrgTable.setStatus("current")
_CucsVmDCOrgEntry_Object = MibTableRow
cucsVmDCOrgEntry = _CucsVmDCOrgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 2, 1)
)
cucsVmDCOrgEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmDCOrgInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmDCOrgEntry.setStatus("current")
_CucsVmDCOrgInstanceId_Type = CucsManagedObjectId
_CucsVmDCOrgInstanceId_Object = MibTableColumn
cucsVmDCOrgInstanceId = _CucsVmDCOrgInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 2, 1, 1),
    _CucsVmDCOrgInstanceId_Type()
)
cucsVmDCOrgInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmDCOrgInstanceId.setStatus("current")
_CucsVmDCOrgDn_Type = CucsManagedObjectDn
_CucsVmDCOrgDn_Object = MibTableColumn
cucsVmDCOrgDn = _CucsVmDCOrgDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 2, 1, 2),
    _CucsVmDCOrgDn_Type()
)
cucsVmDCOrgDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCOrgDn.setStatus("current")
_CucsVmDCOrgRn_Type = SnmpAdminString
_CucsVmDCOrgRn_Object = MibTableColumn
cucsVmDCOrgRn = _CucsVmDCOrgRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 2, 1, 3),
    _CucsVmDCOrgRn_Type()
)
cucsVmDCOrgRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCOrgRn.setStatus("current")
_CucsVmDCOrgDescr_Type = SnmpAdminString
_CucsVmDCOrgDescr_Object = MibTableColumn
cucsVmDCOrgDescr = _CucsVmDCOrgDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 2, 1, 4),
    _CucsVmDCOrgDescr_Type()
)
cucsVmDCOrgDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCOrgDescr.setStatus("current")
_CucsVmDCOrgIntId_Type = SnmpAdminString
_CucsVmDCOrgIntId_Object = MibTableColumn
cucsVmDCOrgIntId = _CucsVmDCOrgIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 2, 1, 5),
    _CucsVmDCOrgIntId_Type()
)
cucsVmDCOrgIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCOrgIntId.setStatus("current")
_CucsVmDCOrgName_Type = SnmpAdminString
_CucsVmDCOrgName_Object = MibTableColumn
cucsVmDCOrgName = _CucsVmDCOrgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 2, 1, 6),
    _CucsVmDCOrgName_Type()
)
cucsVmDCOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCOrgName.setStatus("current")
_CucsVmDCOrgOwn_Type = CucsExtvmmOwnership
_CucsVmDCOrgOwn_Object = MibTableColumn
cucsVmDCOrgOwn = _CucsVmDCOrgOwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 2, 1, 7),
    _CucsVmDCOrgOwn_Type()
)
cucsVmDCOrgOwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCOrgOwn.setStatus("current")
_CucsVmDCOrgUuid_Type = SnmpAdminString
_CucsVmDCOrgUuid_Object = MibTableColumn
cucsVmDCOrgUuid = _CucsVmDCOrgUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 2, 1, 8),
    _CucsVmDCOrgUuid_Type()
)
cucsVmDCOrgUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCOrgUuid.setStatus("current")
_CucsVmDCOrgPolicyLevel_Type = Gauge32
_CucsVmDCOrgPolicyLevel_Object = MibTableColumn
cucsVmDCOrgPolicyLevel = _CucsVmDCOrgPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 2, 1, 9),
    _CucsVmDCOrgPolicyLevel_Type()
)
cucsVmDCOrgPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCOrgPolicyLevel.setStatus("current")
_CucsVmDCOrgPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVmDCOrgPolicyOwner_Object = MibTableColumn
cucsVmDCOrgPolicyOwner = _CucsVmDCOrgPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 2, 1, 10),
    _CucsVmDCOrgPolicyOwner_Type()
)
cucsVmDCOrgPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmDCOrgPolicyOwner.setStatus("current")
_CucsVmEpTable_Object = MibTable
cucsVmEpTable = _CucsVmEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 3)
)
if mibBuilder.loadTexts:
    cucsVmEpTable.setStatus("current")
_CucsVmEpEntry_Object = MibTableRow
cucsVmEpEntry = _CucsVmEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 3, 1)
)
cucsVmEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmEpEntry.setStatus("current")
_CucsVmEpInstanceId_Type = CucsManagedObjectId
_CucsVmEpInstanceId_Object = MibTableColumn
cucsVmEpInstanceId = _CucsVmEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 3, 1, 1),
    _CucsVmEpInstanceId_Type()
)
cucsVmEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmEpInstanceId.setStatus("current")
_CucsVmEpDn_Type = CucsManagedObjectDn
_CucsVmEpDn_Object = MibTableColumn
cucsVmEpDn = _CucsVmEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 3, 1, 2),
    _CucsVmEpDn_Type()
)
cucsVmEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmEpDn.setStatus("current")
_CucsVmEpRn_Type = SnmpAdminString
_CucsVmEpRn_Object = MibTableColumn
cucsVmEpRn = _CucsVmEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 3, 1, 3),
    _CucsVmEpRn_Type()
)
cucsVmEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmEpRn.setStatus("current")
_CucsVmHbaTable_Object = MibTable
cucsVmHbaTable = _CucsVmHbaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4)
)
if mibBuilder.loadTexts:
    cucsVmHbaTable.setStatus("current")
_CucsVmHbaEntry_Object = MibTableRow
cucsVmHbaEntry = _CucsVmHbaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1)
)
cucsVmHbaEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmHbaInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmHbaEntry.setStatus("current")
_CucsVmHbaInstanceId_Type = CucsManagedObjectId
_CucsVmHbaInstanceId_Object = MibTableColumn
cucsVmHbaInstanceId = _CucsVmHbaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 1),
    _CucsVmHbaInstanceId_Type()
)
cucsVmHbaInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmHbaInstanceId.setStatus("current")
_CucsVmHbaDn_Type = CucsManagedObjectDn
_CucsVmHbaDn_Object = MibTableColumn
cucsVmHbaDn = _CucsVmHbaDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 2),
    _CucsVmHbaDn_Type()
)
cucsVmHbaDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaDn.setStatus("current")
_CucsVmHbaRn_Type = SnmpAdminString
_CucsVmHbaRn_Object = MibTableColumn
cucsVmHbaRn = _CucsVmHbaRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 3),
    _CucsVmHbaRn_Type()
)
cucsVmHbaRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaRn.setStatus("current")
_CucsVmHbaDvsPortId_Type = Gauge32
_CucsVmHbaDvsPortId_Object = MibTableColumn
cucsVmHbaDvsPortId = _CucsVmHbaDvsPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 4),
    _CucsVmHbaDvsPortId_Type()
)
cucsVmHbaDvsPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaDvsPortId.setStatus("current")
_CucsVmHbaDvsSwitchId_Type = Gauge32
_CucsVmHbaDvsSwitchId_Object = MibTableColumn
cucsVmHbaDvsSwitchId = _CucsVmHbaDvsSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 5),
    _CucsVmHbaDvsSwitchId_Type()
)
cucsVmHbaDvsSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaDvsSwitchId.setStatus("current")
_CucsVmHbaHostIfDn_Type = SnmpAdminString
_CucsVmHbaHostIfDn_Object = MibTableColumn
cucsVmHbaHostIfDn = _CucsVmHbaHostIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 6),
    _CucsVmHbaHostIfDn_Type()
)
cucsVmHbaHostIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaHostIfDn.setStatus("current")
_CucsVmHbaName_Type = SnmpAdminString
_CucsVmHbaName_Object = MibTableColumn
cucsVmHbaName = _CucsVmHbaName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 7),
    _CucsVmHbaName_Type()
)
cucsVmHbaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaName.setStatus("current")
_CucsVmHbaOwner_Type = CucsVmAdaptorOwner
_CucsVmHbaOwner_Object = MibTableColumn
cucsVmHbaOwner = _CucsVmHbaOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 8),
    _CucsVmHbaOwner_Type()
)
cucsVmHbaOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaOwner.setStatus("current")
_CucsVmHbaPhSwitchId_Type = CucsNetworkSwitchId
_CucsVmHbaPhSwitchId_Object = MibTableColumn
cucsVmHbaPhSwitchId = _CucsVmHbaPhSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 9),
    _CucsVmHbaPhSwitchId_Type()
)
cucsVmHbaPhSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaPhSwitchId.setStatus("current")
_CucsVmHbaProfileId_Type = Gauge32
_CucsVmHbaProfileId_Object = MibTableColumn
cucsVmHbaProfileId = _CucsVmHbaProfileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 10),
    _CucsVmHbaProfileId_Type()
)
cucsVmHbaProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaProfileId.setStatus("current")
_CucsVmHbaProfileName_Type = SnmpAdminString
_CucsVmHbaProfileName_Object = MibTableColumn
cucsVmHbaProfileName = _CucsVmHbaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 11),
    _CucsVmHbaProfileName_Type()
)
cucsVmHbaProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaProfileName.setStatus("current")
_CucsVmHbaStatusChangeTs_Type = DateAndTime
_CucsVmHbaStatusChangeTs_Object = MibTableColumn
cucsVmHbaStatusChangeTs = _CucsVmHbaStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 12),
    _CucsVmHbaStatusChangeTs_Type()
)
cucsVmHbaStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaStatusChangeTs.setStatus("current")
_CucsVmHbaSwitchId_Type = CucsNetworkSwitchId
_CucsVmHbaSwitchId_Object = MibTableColumn
cucsVmHbaSwitchId = _CucsVmHbaSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 13),
    _CucsVmHbaSwitchId_Type()
)
cucsVmHbaSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaSwitchId.setStatus("current")
_CucsVmHbaType_Type = CucsVmHbaType
_CucsVmHbaType_Object = MibTableColumn
cucsVmHbaType = _CucsVmHbaType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 14),
    _CucsVmHbaType_Type()
)
cucsVmHbaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaType.setStatus("current")
_CucsVmHbaUuid_Type = SnmpAdminString
_CucsVmHbaUuid_Object = MibTableColumn
cucsVmHbaUuid = _CucsVmHbaUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 15),
    _CucsVmHbaUuid_Type()
)
cucsVmHbaUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaUuid.setStatus("current")
_CucsVmHbaVStatus_Type = CucsVmStatus
_CucsVmHbaVStatus_Object = MibTableColumn
cucsVmHbaVStatus = _CucsVmHbaVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 16),
    _CucsVmHbaVStatus_Type()
)
cucsVmHbaVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaVStatus.setStatus("current")
_CucsVmHbaVcDn_Type = SnmpAdminString
_CucsVmHbaVcDn_Object = MibTableColumn
cucsVmHbaVcDn = _CucsVmHbaVcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 17),
    _CucsVmHbaVcDn_Type()
)
cucsVmHbaVcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaVcDn.setStatus("current")
_CucsVmHbaVifId_Type = Gauge32
_CucsVmHbaVifId_Object = MibTableColumn
cucsVmHbaVifId = _CucsVmHbaVifId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 18),
    _CucsVmHbaVifId_Type()
)
cucsVmHbaVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaVifId.setStatus("current")
_CucsVmHbaVnicDn_Type = SnmpAdminString
_CucsVmHbaVnicDn_Object = MibTableColumn
cucsVmHbaVnicDn = _CucsVmHbaVnicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 19),
    _CucsVmHbaVnicDn_Type()
)
cucsVmHbaVnicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaVnicDn.setStatus("current")
_CucsVmHbaWwnn_Type = Unsigned64
_CucsVmHbaWwnn_Object = MibTableColumn
cucsVmHbaWwnn = _CucsVmHbaWwnn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 20),
    _CucsVmHbaWwnn_Type()
)
cucsVmHbaWwnn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaWwnn.setStatus("current")
_CucsVmHbaWwpn_Type = Unsigned64
_CucsVmHbaWwpn_Object = MibTableColumn
cucsVmHbaWwpn = _CucsVmHbaWwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 21),
    _CucsVmHbaWwpn_Type()
)
cucsVmHbaWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaWwpn.setStatus("current")
_CucsVmHbaDvsGenPortId_Type = SnmpAdminString
_CucsVmHbaDvsGenPortId_Object = MibTableColumn
cucsVmHbaDvsGenPortId = _CucsVmHbaDvsGenPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 22),
    _CucsVmHbaDvsGenPortId_Type()
)
cucsVmHbaDvsGenPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaDvsGenPortId.setStatus("current")
_CucsVmHbaVmndGuid_Type = SnmpAdminString
_CucsVmHbaVmndGuid_Object = MibTableColumn
cucsVmHbaVmndGuid = _CucsVmHbaVmndGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 24),
    _CucsVmHbaVmndGuid_Type()
)
cucsVmHbaVmndGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaVmndGuid.setStatus("current")
_CucsVmHbaVmndName_Type = SnmpAdminString
_CucsVmHbaVmndName_Object = MibTableColumn
cucsVmHbaVmndName = _CucsVmHbaVmndName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 4, 1, 25),
    _CucsVmHbaVmndName_Type()
)
cucsVmHbaVmndName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHbaVmndName.setStatus("current")
_CucsVmHvTable_Object = MibTable
cucsVmHvTable = _CucsVmHvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5)
)
if mibBuilder.loadTexts:
    cucsVmHvTable.setStatus("current")
_CucsVmHvEntry_Object = MibTableRow
cucsVmHvEntry = _CucsVmHvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1)
)
cucsVmHvEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmHvInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmHvEntry.setStatus("current")
_CucsVmHvInstanceId_Type = CucsManagedObjectId
_CucsVmHvInstanceId_Object = MibTableColumn
cucsVmHvInstanceId = _CucsVmHvInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 1),
    _CucsVmHvInstanceId_Type()
)
cucsVmHvInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmHvInstanceId.setStatus("current")
_CucsVmHvDn_Type = CucsManagedObjectDn
_CucsVmHvDn_Object = MibTableColumn
cucsVmHvDn = _CucsVmHvDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 2),
    _CucsVmHvDn_Type()
)
cucsVmHvDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvDn.setStatus("current")
_CucsVmHvRn_Type = SnmpAdminString
_CucsVmHvRn_Object = MibTableColumn
cucsVmHvRn = _CucsVmHvRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 3),
    _CucsVmHvRn_Type()
)
cucsVmHvRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvRn.setStatus("current")
_CucsVmHvDescr_Type = SnmpAdminString
_CucsVmHvDescr_Object = MibTableColumn
cucsVmHvDescr = _CucsVmHvDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 4),
    _CucsVmHvDescr_Type()
)
cucsVmHvDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvDescr.setStatus("current")
_CucsVmHvDvsDn_Type = SnmpAdminString
_CucsVmHvDvsDn_Object = MibTableColumn
cucsVmHvDvsDn = _CucsVmHvDvsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 5),
    _CucsVmHvDvsDn_Type()
)
cucsVmHvDvsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvDvsDn.setStatus("current")
_CucsVmHvDvsName_Type = SnmpAdminString
_CucsVmHvDvsName_Object = MibTableColumn
cucsVmHvDvsName = _CucsVmHvDvsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 6),
    _CucsVmHvDvsName_Type()
)
cucsVmHvDvsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvDvsName.setStatus("current")
_CucsVmHvFltAggr_Type = Unsigned64
_CucsVmHvFltAggr_Object = MibTableColumn
cucsVmHvFltAggr = _CucsVmHvFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 7),
    _CucsVmHvFltAggr_Type()
)
cucsVmHvFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvFltAggr.setStatus("current")
_CucsVmHvIntId_Type = SnmpAdminString
_CucsVmHvIntId_Object = MibTableColumn
cucsVmHvIntId = _CucsVmHvIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 8),
    _CucsVmHvIntId_Type()
)
cucsVmHvIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvIntId.setStatus("current")
_CucsVmHvLsDn_Type = SnmpAdminString
_CucsVmHvLsDn_Object = MibTableColumn
cucsVmHvLsDn = _CucsVmHvLsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 9),
    _CucsVmHvLsDn_Type()
)
cucsVmHvLsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvLsDn.setStatus("current")
_CucsVmHvName_Type = SnmpAdminString
_CucsVmHvName_Object = MibTableColumn
cucsVmHvName = _CucsVmHvName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 10),
    _CucsVmHvName_Type()
)
cucsVmHvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvName.setStatus("current")
_CucsVmHvPnDn_Type = SnmpAdminString
_CucsVmHvPnDn_Object = MibTableColumn
cucsVmHvPnDn = _CucsVmHvPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 11),
    _CucsVmHvPnDn_Type()
)
cucsVmHvPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvPnDn.setStatus("current")
_CucsVmHvStatusChangeTs_Type = DateAndTime
_CucsVmHvStatusChangeTs_Object = MibTableColumn
cucsVmHvStatusChangeTs = _CucsVmHvStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 12),
    _CucsVmHvStatusChangeTs_Type()
)
cucsVmHvStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvStatusChangeTs.setStatus("current")
_CucsVmHvUuid_Type = SnmpAdminString
_CucsVmHvUuid_Object = MibTableColumn
cucsVmHvUuid = _CucsVmHvUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 13),
    _CucsVmHvUuid_Type()
)
cucsVmHvUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvUuid.setStatus("current")
_CucsVmHvVStatus_Type = CucsVmStatus
_CucsVmHvVStatus_Object = MibTableColumn
cucsVmHvVStatus = _CucsVmHvVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 14),
    _CucsVmHvVStatus_Type()
)
cucsVmHvVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvVStatus.setStatus("current")
_CucsVmHvClInstType_Type = CucsVmHvClInstType
_CucsVmHvClInstType_Object = MibTableColumn
cucsVmHvClInstType = _CucsVmHvClInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 15),
    _CucsVmHvClInstType_Type()
)
cucsVmHvClInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvClInstType.setStatus("current")
_CucsVmHvHvType_Type = CucsVmHvType
_CucsVmHvHvType_Object = MibTableColumn
cucsVmHvHvType = _CucsVmHvHvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 16),
    _CucsVmHvHvType_Type()
)
cucsVmHvHvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvHvType.setStatus("current")
_CucsVmHvModel_Type = CucsOsOsType
_CucsVmHvModel_Object = MibTableColumn
cucsVmHvModel = _CucsVmHvModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 17),
    _CucsVmHvModel_Type()
)
cucsVmHvModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvModel.setStatus("current")
_CucsVmHvVendor_Type = CucsVmOsHvVendor
_CucsVmHvVendor_Object = MibTableColumn
cucsVmHvVendor = _CucsVmHvVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 18),
    _CucsVmHvVendor_Type()
)
cucsVmHvVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvVendor.setStatus("current")
_CucsVmHvPolicyLevel_Type = Gauge32
_CucsVmHvPolicyLevel_Object = MibTableColumn
cucsVmHvPolicyLevel = _CucsVmHvPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 19),
    _CucsVmHvPolicyLevel_Type()
)
cucsVmHvPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvPolicyLevel.setStatus("current")
_CucsVmHvPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVmHvPolicyOwner_Object = MibTableColumn
cucsVmHvPolicyOwner = _CucsVmHvPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 5, 1, 20),
    _CucsVmHvPolicyOwner_Type()
)
cucsVmHvPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmHvPolicyOwner.setStatus("current")
_CucsVmInstanceTable_Object = MibTable
cucsVmInstanceTable = _CucsVmInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6)
)
if mibBuilder.loadTexts:
    cucsVmInstanceTable.setStatus("current")
_CucsVmInstanceEntry_Object = MibTableRow
cucsVmInstanceEntry = _CucsVmInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1)
)
cucsVmInstanceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmInstanceEntry.setStatus("current")
_CucsVmInstanceInstanceId_Type = CucsManagedObjectId
_CucsVmInstanceInstanceId_Object = MibTableColumn
cucsVmInstanceInstanceId = _CucsVmInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 1),
    _CucsVmInstanceInstanceId_Type()
)
cucsVmInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmInstanceInstanceId.setStatus("current")
_CucsVmInstanceDn_Type = CucsManagedObjectDn
_CucsVmInstanceDn_Object = MibTableColumn
cucsVmInstanceDn = _CucsVmInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 2),
    _CucsVmInstanceDn_Type()
)
cucsVmInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceDn.setStatus("current")
_CucsVmInstanceRn_Type = SnmpAdminString
_CucsVmInstanceRn_Object = MibTableColumn
cucsVmInstanceRn = _CucsVmInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 3),
    _CucsVmInstanceRn_Type()
)
cucsVmInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceRn.setStatus("current")
_CucsVmInstanceDescr_Type = SnmpAdminString
_CucsVmInstanceDescr_Object = MibTableColumn
cucsVmInstanceDescr = _CucsVmInstanceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 4),
    _CucsVmInstanceDescr_Type()
)
cucsVmInstanceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceDescr.setStatus("current")
_CucsVmInstanceDvsDn_Type = SnmpAdminString
_CucsVmInstanceDvsDn_Object = MibTableColumn
cucsVmInstanceDvsDn = _CucsVmInstanceDvsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 5),
    _CucsVmInstanceDvsDn_Type()
)
cucsVmInstanceDvsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceDvsDn.setStatus("current")
_CucsVmInstanceDvsName_Type = SnmpAdminString
_CucsVmInstanceDvsName_Object = MibTableColumn
cucsVmInstanceDvsName = _CucsVmInstanceDvsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 6),
    _CucsVmInstanceDvsName_Type()
)
cucsVmInstanceDvsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceDvsName.setStatus("current")
_CucsVmInstanceFltAggr_Type = Unsigned64
_CucsVmInstanceFltAggr_Object = MibTableColumn
cucsVmInstanceFltAggr = _CucsVmInstanceFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 7),
    _CucsVmInstanceFltAggr_Type()
)
cucsVmInstanceFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceFltAggr.setStatus("current")
_CucsVmInstanceHvDn_Type = SnmpAdminString
_CucsVmInstanceHvDn_Object = MibTableColumn
cucsVmInstanceHvDn = _CucsVmInstanceHvDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 8),
    _CucsVmInstanceHvDn_Type()
)
cucsVmInstanceHvDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceHvDn.setStatus("current")
_CucsVmInstanceHvUuid_Type = SnmpAdminString
_CucsVmInstanceHvUuid_Object = MibTableColumn
cucsVmInstanceHvUuid = _CucsVmInstanceHvUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 9),
    _CucsVmInstanceHvUuid_Type()
)
cucsVmInstanceHvUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceHvUuid.setStatus("current")
_CucsVmInstanceIntId_Type = SnmpAdminString
_CucsVmInstanceIntId_Object = MibTableColumn
cucsVmInstanceIntId = _CucsVmInstanceIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 10),
    _CucsVmInstanceIntId_Type()
)
cucsVmInstanceIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceIntId.setStatus("current")
_CucsVmInstanceLsDn_Type = SnmpAdminString
_CucsVmInstanceLsDn_Object = MibTableColumn
cucsVmInstanceLsDn = _CucsVmInstanceLsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 11),
    _CucsVmInstanceLsDn_Type()
)
cucsVmInstanceLsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceLsDn.setStatus("current")
_CucsVmInstanceName_Type = SnmpAdminString
_CucsVmInstanceName_Object = MibTableColumn
cucsVmInstanceName = _CucsVmInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 12),
    _CucsVmInstanceName_Type()
)
cucsVmInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceName.setStatus("current")
_CucsVmInstancePnDn_Type = SnmpAdminString
_CucsVmInstancePnDn_Object = MibTableColumn
cucsVmInstancePnDn = _CucsVmInstancePnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 13),
    _CucsVmInstancePnDn_Type()
)
cucsVmInstancePnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstancePnDn.setStatus("current")
_CucsVmInstanceStatusChangeTs_Type = DateAndTime
_CucsVmInstanceStatusChangeTs_Object = MibTableColumn
cucsVmInstanceStatusChangeTs = _CucsVmInstanceStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 14),
    _CucsVmInstanceStatusChangeTs_Type()
)
cucsVmInstanceStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceStatusChangeTs.setStatus("current")
_CucsVmInstanceUuid_Type = SnmpAdminString
_CucsVmInstanceUuid_Object = MibTableColumn
cucsVmInstanceUuid = _CucsVmInstanceUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 15),
    _CucsVmInstanceUuid_Type()
)
cucsVmInstanceUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceUuid.setStatus("current")
_CucsVmInstanceVStatus_Type = CucsVmStatus
_CucsVmInstanceVStatus_Object = MibTableColumn
cucsVmInstanceVStatus = _CucsVmInstanceVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 16),
    _CucsVmInstanceVStatus_Type()
)
cucsVmInstanceVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceVStatus.setStatus("current")
_CucsVmInstanceClInstType_Type = CucsVmInstType
_CucsVmInstanceClInstType_Object = MibTableColumn
cucsVmInstanceClInstType = _CucsVmInstanceClInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 17),
    _CucsVmInstanceClInstType_Type()
)
cucsVmInstanceClInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceClInstType.setStatus("current")
_CucsVmInstanceHvType_Type = CucsVmHvType
_CucsVmInstanceHvType_Object = MibTableColumn
cucsVmInstanceHvType = _CucsVmInstanceHvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 18),
    _CucsVmInstanceHvType_Type()
)
cucsVmInstanceHvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceHvType.setStatus("current")
_CucsVmInstanceModel_Type = CucsOsOsType
_CucsVmInstanceModel_Object = MibTableColumn
cucsVmInstanceModel = _CucsVmInstanceModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 19),
    _CucsVmInstanceModel_Type()
)
cucsVmInstanceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceModel.setStatus("current")
_CucsVmInstanceVendor_Type = CucsVmOsHvVendor
_CucsVmInstanceVendor_Object = MibTableColumn
cucsVmInstanceVendor = _CucsVmInstanceVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 20),
    _CucsVmInstanceVendor_Type()
)
cucsVmInstanceVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstanceVendor.setStatus("current")
_CucsVmInstancePolicyLevel_Type = Gauge32
_CucsVmInstancePolicyLevel_Object = MibTableColumn
cucsVmInstancePolicyLevel = _CucsVmInstancePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 21),
    _CucsVmInstancePolicyLevel_Type()
)
cucsVmInstancePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstancePolicyLevel.setStatus("current")
_CucsVmInstancePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVmInstancePolicyOwner_Object = MibTableColumn
cucsVmInstancePolicyOwner = _CucsVmInstancePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 6, 1, 22),
    _CucsVmInstancePolicyOwner_Type()
)
cucsVmInstancePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmInstancePolicyOwner.setStatus("current")
_CucsVmLifeCyclePolicyTable_Object = MibTable
cucsVmLifeCyclePolicyTable = _CucsVmLifeCyclePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7)
)
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyTable.setStatus("current")
_CucsVmLifeCyclePolicyEntry_Object = MibTableRow
cucsVmLifeCyclePolicyEntry = _CucsVmLifeCyclePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1)
)
cucsVmLifeCyclePolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmLifeCyclePolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyEntry.setStatus("current")
_CucsVmLifeCyclePolicyInstanceId_Type = CucsManagedObjectId
_CucsVmLifeCyclePolicyInstanceId_Object = MibTableColumn
cucsVmLifeCyclePolicyInstanceId = _CucsVmLifeCyclePolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 1),
    _CucsVmLifeCyclePolicyInstanceId_Type()
)
cucsVmLifeCyclePolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyInstanceId.setStatus("current")
_CucsVmLifeCyclePolicyDn_Type = CucsManagedObjectDn
_CucsVmLifeCyclePolicyDn_Object = MibTableColumn
cucsVmLifeCyclePolicyDn = _CucsVmLifeCyclePolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 2),
    _CucsVmLifeCyclePolicyDn_Type()
)
cucsVmLifeCyclePolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyDn.setStatus("current")
_CucsVmLifeCyclePolicyRn_Type = SnmpAdminString
_CucsVmLifeCyclePolicyRn_Object = MibTableColumn
cucsVmLifeCyclePolicyRn = _CucsVmLifeCyclePolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 3),
    _CucsVmLifeCyclePolicyRn_Type()
)
cucsVmLifeCyclePolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyRn.setStatus("current")
_CucsVmLifeCyclePolicyDescr_Type = SnmpAdminString
_CucsVmLifeCyclePolicyDescr_Object = MibTableColumn
cucsVmLifeCyclePolicyDescr = _CucsVmLifeCyclePolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 4),
    _CucsVmLifeCyclePolicyDescr_Type()
)
cucsVmLifeCyclePolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyDescr.setStatus("current")
_CucsVmLifeCyclePolicyIntId_Type = SnmpAdminString
_CucsVmLifeCyclePolicyIntId_Object = MibTableColumn
cucsVmLifeCyclePolicyIntId = _CucsVmLifeCyclePolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 5),
    _CucsVmLifeCyclePolicyIntId_Type()
)
cucsVmLifeCyclePolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyIntId.setStatus("current")
_CucsVmLifeCyclePolicyName_Type = SnmpAdminString
_CucsVmLifeCyclePolicyName_Object = MibTableColumn
cucsVmLifeCyclePolicyName = _CucsVmLifeCyclePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 6),
    _CucsVmLifeCyclePolicyName_Type()
)
cucsVmLifeCyclePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyName.setStatus("current")
_CucsVmLifeCyclePolicyVmRetention_Type = Gauge32
_CucsVmLifeCyclePolicyVmRetention_Object = MibTableColumn
cucsVmLifeCyclePolicyVmRetention = _CucsVmLifeCyclePolicyVmRetention_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 7),
    _CucsVmLifeCyclePolicyVmRetention_Type()
)
cucsVmLifeCyclePolicyVmRetention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyVmRetention.setStatus("current")
_CucsVmLifeCyclePolicyVnicRetention_Type = Gauge32
_CucsVmLifeCyclePolicyVnicRetention_Object = MibTableColumn
cucsVmLifeCyclePolicyVnicRetention = _CucsVmLifeCyclePolicyVnicRetention_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 8),
    _CucsVmLifeCyclePolicyVnicRetention_Type()
)
cucsVmLifeCyclePolicyVnicRetention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyVnicRetention.setStatus("current")
_CucsVmLifeCyclePolicyFsmDescr_Type = SnmpAdminString
_CucsVmLifeCyclePolicyFsmDescr_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmDescr = _CucsVmLifeCyclePolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 9),
    _CucsVmLifeCyclePolicyFsmDescr_Type()
)
cucsVmLifeCyclePolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmDescr.setStatus("current")
_CucsVmLifeCyclePolicyFsmPrev_Type = SnmpAdminString
_CucsVmLifeCyclePolicyFsmPrev_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmPrev = _CucsVmLifeCyclePolicyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 10),
    _CucsVmLifeCyclePolicyFsmPrev_Type()
)
cucsVmLifeCyclePolicyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmPrev.setStatus("current")
_CucsVmLifeCyclePolicyFsmProgr_Type = Gauge32
_CucsVmLifeCyclePolicyFsmProgr_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmProgr = _CucsVmLifeCyclePolicyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 11),
    _CucsVmLifeCyclePolicyFsmProgr_Type()
)
cucsVmLifeCyclePolicyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmProgr.setStatus("current")
_CucsVmLifeCyclePolicyFsmRmtInvErrCode_Type = Gauge32
_CucsVmLifeCyclePolicyFsmRmtInvErrCode_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmRmtInvErrCode = _CucsVmLifeCyclePolicyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 12),
    _CucsVmLifeCyclePolicyFsmRmtInvErrCode_Type()
)
cucsVmLifeCyclePolicyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmRmtInvErrCode.setStatus("current")
_CucsVmLifeCyclePolicyFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsVmLifeCyclePolicyFsmRmtInvErrDescr_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmRmtInvErrDescr = _CucsVmLifeCyclePolicyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 13),
    _CucsVmLifeCyclePolicyFsmRmtInvErrDescr_Type()
)
cucsVmLifeCyclePolicyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmRmtInvErrDescr.setStatus("current")
_CucsVmLifeCyclePolicyFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsVmLifeCyclePolicyFsmRmtInvRslt_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmRmtInvRslt = _CucsVmLifeCyclePolicyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 14),
    _CucsVmLifeCyclePolicyFsmRmtInvRslt_Type()
)
cucsVmLifeCyclePolicyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmRmtInvRslt.setStatus("current")
_CucsVmLifeCyclePolicyFsmStageDescr_Type = SnmpAdminString
_CucsVmLifeCyclePolicyFsmStageDescr_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmStageDescr = _CucsVmLifeCyclePolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 15),
    _CucsVmLifeCyclePolicyFsmStageDescr_Type()
)
cucsVmLifeCyclePolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmStageDescr.setStatus("current")
_CucsVmLifeCyclePolicyFsmStamp_Type = DateAndTime
_CucsVmLifeCyclePolicyFsmStamp_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmStamp = _CucsVmLifeCyclePolicyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 16),
    _CucsVmLifeCyclePolicyFsmStamp_Type()
)
cucsVmLifeCyclePolicyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmStamp.setStatus("current")
_CucsVmLifeCyclePolicyFsmStatus_Type = SnmpAdminString
_CucsVmLifeCyclePolicyFsmStatus_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmStatus = _CucsVmLifeCyclePolicyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 17),
    _CucsVmLifeCyclePolicyFsmStatus_Type()
)
cucsVmLifeCyclePolicyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmStatus.setStatus("current")
_CucsVmLifeCyclePolicyFsmTry_Type = Gauge32
_CucsVmLifeCyclePolicyFsmTry_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmTry = _CucsVmLifeCyclePolicyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 18),
    _CucsVmLifeCyclePolicyFsmTry_Type()
)
cucsVmLifeCyclePolicyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmTry.setStatus("current")
_CucsVmLifeCyclePolicyPolicyLevel_Type = Gauge32
_CucsVmLifeCyclePolicyPolicyLevel_Object = MibTableColumn
cucsVmLifeCyclePolicyPolicyLevel = _CucsVmLifeCyclePolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 19),
    _CucsVmLifeCyclePolicyPolicyLevel_Type()
)
cucsVmLifeCyclePolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyPolicyLevel.setStatus("current")
_CucsVmLifeCyclePolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVmLifeCyclePolicyPolicyOwner_Object = MibTableColumn
cucsVmLifeCyclePolicyPolicyOwner = _CucsVmLifeCyclePolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 7, 1, 20),
    _CucsVmLifeCyclePolicyPolicyOwner_Type()
)
cucsVmLifeCyclePolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyPolicyOwner.setStatus("current")
_CucsVmNicTable_Object = MibTable
cucsVmNicTable = _CucsVmNicTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8)
)
if mibBuilder.loadTexts:
    cucsVmNicTable.setStatus("current")
_CucsVmNicEntry_Object = MibTableRow
cucsVmNicEntry = _CucsVmNicEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1)
)
cucsVmNicEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmNicInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmNicEntry.setStatus("current")
_CucsVmNicInstanceId_Type = CucsManagedObjectId
_CucsVmNicInstanceId_Object = MibTableColumn
cucsVmNicInstanceId = _CucsVmNicInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 1),
    _CucsVmNicInstanceId_Type()
)
cucsVmNicInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmNicInstanceId.setStatus("current")
_CucsVmNicDn_Type = CucsManagedObjectDn
_CucsVmNicDn_Object = MibTableColumn
cucsVmNicDn = _CucsVmNicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 2),
    _CucsVmNicDn_Type()
)
cucsVmNicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicDn.setStatus("current")
_CucsVmNicRn_Type = SnmpAdminString
_CucsVmNicRn_Object = MibTableColumn
cucsVmNicRn = _CucsVmNicRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 3),
    _CucsVmNicRn_Type()
)
cucsVmNicRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicRn.setStatus("current")
_CucsVmNicDvsPortId_Type = Gauge32
_CucsVmNicDvsPortId_Object = MibTableColumn
cucsVmNicDvsPortId = _CucsVmNicDvsPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 4),
    _CucsVmNicDvsPortId_Type()
)
cucsVmNicDvsPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicDvsPortId.setStatus("current")
_CucsVmNicDvsSwitchId_Type = Gauge32
_CucsVmNicDvsSwitchId_Object = MibTableColumn
cucsVmNicDvsSwitchId = _CucsVmNicDvsSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 5),
    _CucsVmNicDvsSwitchId_Type()
)
cucsVmNicDvsSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicDvsSwitchId.setStatus("current")
_CucsVmNicHostIfDn_Type = SnmpAdminString
_CucsVmNicHostIfDn_Object = MibTableColumn
cucsVmNicHostIfDn = _CucsVmNicHostIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 6),
    _CucsVmNicHostIfDn_Type()
)
cucsVmNicHostIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicHostIfDn.setStatus("current")
_CucsVmNicMacAddr_Type = MacAddress
_CucsVmNicMacAddr_Object = MibTableColumn
cucsVmNicMacAddr = _CucsVmNicMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 7),
    _CucsVmNicMacAddr_Type()
)
cucsVmNicMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicMacAddr.setStatus("current")
_CucsVmNicName_Type = SnmpAdminString
_CucsVmNicName_Object = MibTableColumn
cucsVmNicName = _CucsVmNicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 8),
    _CucsVmNicName_Type()
)
cucsVmNicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicName.setStatus("current")
_CucsVmNicOwner_Type = CucsVmAdaptorOwner
_CucsVmNicOwner_Object = MibTableColumn
cucsVmNicOwner = _CucsVmNicOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 9),
    _CucsVmNicOwner_Type()
)
cucsVmNicOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicOwner.setStatus("current")
_CucsVmNicPhSwitchId_Type = CucsNetworkSwitchId
_CucsVmNicPhSwitchId_Object = MibTableColumn
cucsVmNicPhSwitchId = _CucsVmNicPhSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 10),
    _CucsVmNicPhSwitchId_Type()
)
cucsVmNicPhSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicPhSwitchId.setStatus("current")
_CucsVmNicProfileId_Type = Gauge32
_CucsVmNicProfileId_Object = MibTableColumn
cucsVmNicProfileId = _CucsVmNicProfileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 11),
    _CucsVmNicProfileId_Type()
)
cucsVmNicProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicProfileId.setStatus("current")
_CucsVmNicProfileName_Type = SnmpAdminString
_CucsVmNicProfileName_Object = MibTableColumn
cucsVmNicProfileName = _CucsVmNicProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 12),
    _CucsVmNicProfileName_Type()
)
cucsVmNicProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicProfileName.setStatus("current")
_CucsVmNicStatusChangeTs_Type = DateAndTime
_CucsVmNicStatusChangeTs_Object = MibTableColumn
cucsVmNicStatusChangeTs = _CucsVmNicStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 13),
    _CucsVmNicStatusChangeTs_Type()
)
cucsVmNicStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicStatusChangeTs.setStatus("current")
_CucsVmNicSwitchId_Type = CucsNetworkSwitchId
_CucsVmNicSwitchId_Object = MibTableColumn
cucsVmNicSwitchId = _CucsVmNicSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 14),
    _CucsVmNicSwitchId_Type()
)
cucsVmNicSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicSwitchId.setStatus("current")
_CucsVmNicType_Type = CucsVmNicType
_CucsVmNicType_Object = MibTableColumn
cucsVmNicType = _CucsVmNicType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 15),
    _CucsVmNicType_Type()
)
cucsVmNicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicType.setStatus("current")
_CucsVmNicUuid_Type = SnmpAdminString
_CucsVmNicUuid_Object = MibTableColumn
cucsVmNicUuid = _CucsVmNicUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 16),
    _CucsVmNicUuid_Type()
)
cucsVmNicUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicUuid.setStatus("current")
_CucsVmNicVStatus_Type = CucsVmStatus
_CucsVmNicVStatus_Object = MibTableColumn
cucsVmNicVStatus = _CucsVmNicVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 17),
    _CucsVmNicVStatus_Type()
)
cucsVmNicVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicVStatus.setStatus("current")
_CucsVmNicVcDn_Type = SnmpAdminString
_CucsVmNicVcDn_Object = MibTableColumn
cucsVmNicVcDn = _CucsVmNicVcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 18),
    _CucsVmNicVcDn_Type()
)
cucsVmNicVcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicVcDn.setStatus("current")
_CucsVmNicVifId_Type = Gauge32
_CucsVmNicVifId_Object = MibTableColumn
cucsVmNicVifId = _CucsVmNicVifId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 19),
    _CucsVmNicVifId_Type()
)
cucsVmNicVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicVifId.setStatus("current")
_CucsVmNicVnicDn_Type = SnmpAdminString
_CucsVmNicVnicDn_Object = MibTableColumn
cucsVmNicVnicDn = _CucsVmNicVnicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 20),
    _CucsVmNicVnicDn_Type()
)
cucsVmNicVnicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicVnicDn.setStatus("current")
_CucsVmNicDvsGenPortId_Type = SnmpAdminString
_CucsVmNicDvsGenPortId_Object = MibTableColumn
cucsVmNicDvsGenPortId = _CucsVmNicDvsGenPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 21),
    _CucsVmNicDvsGenPortId_Type()
)
cucsVmNicDvsGenPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicDvsGenPortId.setStatus("current")
_CucsVmNicVmndGuid_Type = SnmpAdminString
_CucsVmNicVmndGuid_Object = MibTableColumn
cucsVmNicVmndGuid = _CucsVmNicVmndGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 23),
    _CucsVmNicVmndGuid_Type()
)
cucsVmNicVmndGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicVmndGuid.setStatus("current")
_CucsVmNicVmndName_Type = SnmpAdminString
_CucsVmNicVmndName_Object = MibTableColumn
cucsVmNicVmndName = _CucsVmNicVmndName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 8, 1, 24),
    _CucsVmNicVmndName_Type()
)
cucsVmNicVmndName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmNicVmndName.setStatus("current")
_CucsVmOrgTable_Object = MibTable
cucsVmOrgTable = _CucsVmOrgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 9)
)
if mibBuilder.loadTexts:
    cucsVmOrgTable.setStatus("current")
_CucsVmOrgEntry_Object = MibTableRow
cucsVmOrgEntry = _CucsVmOrgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 9, 1)
)
cucsVmOrgEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmOrgInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmOrgEntry.setStatus("current")
_CucsVmOrgInstanceId_Type = CucsManagedObjectId
_CucsVmOrgInstanceId_Object = MibTableColumn
cucsVmOrgInstanceId = _CucsVmOrgInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 9, 1, 1),
    _CucsVmOrgInstanceId_Type()
)
cucsVmOrgInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmOrgInstanceId.setStatus("current")
_CucsVmOrgDn_Type = CucsManagedObjectDn
_CucsVmOrgDn_Object = MibTableColumn
cucsVmOrgDn = _CucsVmOrgDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 9, 1, 2),
    _CucsVmOrgDn_Type()
)
cucsVmOrgDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmOrgDn.setStatus("current")
_CucsVmOrgRn_Type = SnmpAdminString
_CucsVmOrgRn_Object = MibTableColumn
cucsVmOrgRn = _CucsVmOrgRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 9, 1, 3),
    _CucsVmOrgRn_Type()
)
cucsVmOrgRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmOrgRn.setStatus("current")
_CucsVmOrgDescr_Type = SnmpAdminString
_CucsVmOrgDescr_Object = MibTableColumn
cucsVmOrgDescr = _CucsVmOrgDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 9, 1, 4),
    _CucsVmOrgDescr_Type()
)
cucsVmOrgDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmOrgDescr.setStatus("current")
_CucsVmOrgIntId_Type = SnmpAdminString
_CucsVmOrgIntId_Object = MibTableColumn
cucsVmOrgIntId = _CucsVmOrgIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 9, 1, 5),
    _CucsVmOrgIntId_Type()
)
cucsVmOrgIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmOrgIntId.setStatus("current")
_CucsVmOrgName_Type = SnmpAdminString
_CucsVmOrgName_Object = MibTableColumn
cucsVmOrgName = _CucsVmOrgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 9, 1, 6),
    _CucsVmOrgName_Type()
)
cucsVmOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmOrgName.setStatus("current")
_CucsVmOrgOwn_Type = CucsExtvmmOwnership
_CucsVmOrgOwn_Object = MibTableColumn
cucsVmOrgOwn = _CucsVmOrgOwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 9, 1, 7),
    _CucsVmOrgOwn_Type()
)
cucsVmOrgOwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmOrgOwn.setStatus("current")
_CucsVmOrgUuid_Type = SnmpAdminString
_CucsVmOrgUuid_Object = MibTableColumn
cucsVmOrgUuid = _CucsVmOrgUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 9, 1, 8),
    _CucsVmOrgUuid_Type()
)
cucsVmOrgUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmOrgUuid.setStatus("current")
_CucsVmOrgPolicyLevel_Type = Gauge32
_CucsVmOrgPolicyLevel_Object = MibTableColumn
cucsVmOrgPolicyLevel = _CucsVmOrgPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 9, 1, 9),
    _CucsVmOrgPolicyLevel_Type()
)
cucsVmOrgPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmOrgPolicyLevel.setStatus("current")
_CucsVmOrgPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVmOrgPolicyOwner_Object = MibTableColumn
cucsVmOrgPolicyOwner = _CucsVmOrgPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 9, 1, 10),
    _CucsVmOrgPolicyOwner_Type()
)
cucsVmOrgPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmOrgPolicyOwner.setStatus("current")
_CucsVmSwitchTable_Object = MibTable
cucsVmSwitchTable = _CucsVmSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10)
)
if mibBuilder.loadTexts:
    cucsVmSwitchTable.setStatus("current")
_CucsVmSwitchEntry_Object = MibTableRow
cucsVmSwitchEntry = _CucsVmSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1)
)
cucsVmSwitchEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmSwitchInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmSwitchEntry.setStatus("current")
_CucsVmSwitchInstanceId_Type = CucsManagedObjectId
_CucsVmSwitchInstanceId_Object = MibTableColumn
cucsVmSwitchInstanceId = _CucsVmSwitchInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1, 1),
    _CucsVmSwitchInstanceId_Type()
)
cucsVmSwitchInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmSwitchInstanceId.setStatus("current")
_CucsVmSwitchDn_Type = CucsManagedObjectDn
_CucsVmSwitchDn_Object = MibTableColumn
cucsVmSwitchDn = _CucsVmSwitchDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1, 2),
    _CucsVmSwitchDn_Type()
)
cucsVmSwitchDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmSwitchDn.setStatus("current")
_CucsVmSwitchRn_Type = SnmpAdminString
_CucsVmSwitchRn_Object = MibTableColumn
cucsVmSwitchRn = _CucsVmSwitchRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1, 3),
    _CucsVmSwitchRn_Type()
)
cucsVmSwitchRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmSwitchRn.setStatus("current")
_CucsVmSwitchAdminState_Type = CucsVmSwitchAdminState
_CucsVmSwitchAdminState_Object = MibTableColumn
cucsVmSwitchAdminState = _CucsVmSwitchAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1, 4),
    _CucsVmSwitchAdminState_Type()
)
cucsVmSwitchAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmSwitchAdminState.setStatus("current")
_CucsVmSwitchDescr_Type = SnmpAdminString
_CucsVmSwitchDescr_Object = MibTableColumn
cucsVmSwitchDescr = _CucsVmSwitchDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1, 5),
    _CucsVmSwitchDescr_Type()
)
cucsVmSwitchDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmSwitchDescr.setStatus("current")
_CucsVmSwitchExtKey_Type = SnmpAdminString
_CucsVmSwitchExtKey_Object = MibTableColumn
cucsVmSwitchExtKey = _CucsVmSwitchExtKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1, 6),
    _CucsVmSwitchExtKey_Type()
)
cucsVmSwitchExtKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmSwitchExtKey.setStatus("current")
_CucsVmSwitchIntId_Type = SnmpAdminString
_CucsVmSwitchIntId_Object = MibTableColumn
cucsVmSwitchIntId = _CucsVmSwitchIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1, 7),
    _CucsVmSwitchIntId_Type()
)
cucsVmSwitchIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmSwitchIntId.setStatus("current")
_CucsVmSwitchKeyInst_Type = Gauge32
_CucsVmSwitchKeyInst_Object = MibTableColumn
cucsVmSwitchKeyInst = _CucsVmSwitchKeyInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1, 8),
    _CucsVmSwitchKeyInst_Type()
)
cucsVmSwitchKeyInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmSwitchKeyInst.setStatus("current")
_CucsVmSwitchName_Type = SnmpAdminString
_CucsVmSwitchName_Object = MibTableColumn
cucsVmSwitchName = _CucsVmSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1, 9),
    _CucsVmSwitchName_Type()
)
cucsVmSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmSwitchName.setStatus("current")
_CucsVmSwitchOwn_Type = CucsExtvmmOwnership
_CucsVmSwitchOwn_Object = MibTableColumn
cucsVmSwitchOwn = _CucsVmSwitchOwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1, 10),
    _CucsVmSwitchOwn_Type()
)
cucsVmSwitchOwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmSwitchOwn.setStatus("current")
_CucsVmSwitchUuid_Type = SnmpAdminString
_CucsVmSwitchUuid_Object = MibTableColumn
cucsVmSwitchUuid = _CucsVmSwitchUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1, 11),
    _CucsVmSwitchUuid_Type()
)
cucsVmSwitchUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmSwitchUuid.setStatus("current")
_CucsVmSwitchId_Type = SnmpAdminString
_CucsVmSwitchId_Object = MibTableColumn
cucsVmSwitchId = _CucsVmSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1, 12),
    _CucsVmSwitchId_Type()
)
cucsVmSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmSwitchId.setStatus("current")
_CucsVmSwitchManager_Type = CucsVmMgmtPlane
_CucsVmSwitchManager_Object = MibTableColumn
cucsVmSwitchManager = _CucsVmSwitchManager_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1, 13),
    _CucsVmSwitchManager_Type()
)
cucsVmSwitchManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmSwitchManager.setStatus("current")
_CucsVmSwitchPolicyLevel_Type = Gauge32
_CucsVmSwitchPolicyLevel_Object = MibTableColumn
cucsVmSwitchPolicyLevel = _CucsVmSwitchPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1, 14),
    _CucsVmSwitchPolicyLevel_Type()
)
cucsVmSwitchPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmSwitchPolicyLevel.setStatus("current")
_CucsVmSwitchPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVmSwitchPolicyOwner_Object = MibTableColumn
cucsVmSwitchPolicyOwner = _CucsVmSwitchPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1, 15),
    _CucsVmSwitchPolicyOwner_Type()
)
cucsVmSwitchPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmSwitchPolicyOwner.setStatus("current")
_CucsVmSwitchFltAggr_Type = Unsigned64
_CucsVmSwitchFltAggr_Object = MibTableColumn
cucsVmSwitchFltAggr = _CucsVmSwitchFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1, 16),
    _CucsVmSwitchFltAggr_Type()
)
cucsVmSwitchFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmSwitchFltAggr.setStatus("current")
_CucsVmSwitchVendor_Type = CucsVmSwitchVendor
_CucsVmSwitchVendor_Object = MibTableColumn
cucsVmSwitchVendor = _CucsVmSwitchVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 10, 1, 17),
    _CucsVmSwitchVendor_Type()
)
cucsVmSwitchVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmSwitchVendor.setStatus("current")
_CucsVmVifTable_Object = MibTable
cucsVmVifTable = _CucsVmVifTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11)
)
if mibBuilder.loadTexts:
    cucsVmVifTable.setStatus("current")
_CucsVmVifEntry_Object = MibTableRow
cucsVmVifEntry = _CucsVmVifEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1)
)
cucsVmVifEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmVifInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmVifEntry.setStatus("current")
_CucsVmVifInstanceId_Type = CucsManagedObjectId
_CucsVmVifInstanceId_Object = MibTableColumn
cucsVmVifInstanceId = _CucsVmVifInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 1),
    _CucsVmVifInstanceId_Type()
)
cucsVmVifInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmVifInstanceId.setStatus("current")
_CucsVmVifDn_Type = CucsManagedObjectDn
_CucsVmVifDn_Object = MibTableColumn
cucsVmVifDn = _CucsVmVifDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 2),
    _CucsVmVifDn_Type()
)
cucsVmVifDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifDn.setStatus("current")
_CucsVmVifRn_Type = SnmpAdminString
_CucsVmVifRn_Object = MibTableColumn
cucsVmVifRn = _CucsVmVifRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 3),
    _CucsVmVifRn_Type()
)
cucsVmVifRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifRn.setStatus("current")
_CucsVmVifCookie_Type = Gauge32
_CucsVmVifCookie_Object = MibTableColumn
cucsVmVifCookie = _CucsVmVifCookie_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 4),
    _CucsVmVifCookie_Type()
)
cucsVmVifCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifCookie.setStatus("current")
_CucsVmVifPhSwitchId_Type = CucsNetworkSwitchId
_CucsVmVifPhSwitchId_Object = MibTableColumn
cucsVmVifPhSwitchId = _CucsVmVifPhSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 5),
    _CucsVmVifPhSwitchId_Type()
)
cucsVmVifPhSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifPhSwitchId.setStatus("current")
_CucsVmVifPhsAccessCardId_Type = Gauge32
_CucsVmVifPhsAccessCardId_Object = MibTableColumn
cucsVmVifPhsAccessCardId = _CucsVmVifPhsAccessCardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 6),
    _CucsVmVifPhsAccessCardId_Type()
)
cucsVmVifPhsAccessCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifPhsAccessCardId.setStatus("current")
_CucsVmVifPhsAccessPortId_Type = Gauge32
_CucsVmVifPhsAccessPortId_Object = MibTableColumn
cucsVmVifPhsAccessPortId = _CucsVmVifPhsAccessPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 7),
    _CucsVmVifPhsAccessPortId_Type()
)
cucsVmVifPhsAccessPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifPhsAccessPortId.setStatus("current")
_CucsVmVifPhsBorderCardId_Type = Gauge32
_CucsVmVifPhsBorderCardId_Object = MibTableColumn
cucsVmVifPhsBorderCardId = _CucsVmVifPhsBorderCardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 8),
    _CucsVmVifPhsBorderCardId_Type()
)
cucsVmVifPhsBorderCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifPhsBorderCardId.setStatus("current")
_CucsVmVifPhsBorderPortId_Type = Gauge32
_CucsVmVifPhsBorderPortId_Object = MibTableColumn
cucsVmVifPhsBorderPortId = _CucsVmVifPhsBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 9),
    _CucsVmVifPhsBorderPortId_Type()
)
cucsVmVifPhsBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifPhsBorderPortId.setStatus("current")
_CucsVmVifStatusChangeTs_Type = DateAndTime
_CucsVmVifStatusChangeTs_Object = MibTableColumn
cucsVmVifStatusChangeTs = _CucsVmVifStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 10),
    _CucsVmVifStatusChangeTs_Type()
)
cucsVmVifStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifStatusChangeTs.setStatus("current")
_CucsVmVifVStatus_Type = CucsVmStatus
_CucsVmVifVStatus_Object = MibTableColumn
cucsVmVifVStatus = _CucsVmVifVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 11),
    _CucsVmVifVStatus_Type()
)
cucsVmVifVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifVStatus.setStatus("current")
_CucsVmVifVcDn_Type = SnmpAdminString
_CucsVmVifVcDn_Object = MibTableColumn
cucsVmVifVcDn = _CucsVmVifVcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 12),
    _CucsVmVifVcDn_Type()
)
cucsVmVifVcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifVcDn.setStatus("current")
_CucsVmVifVifId_Type = Gauge32
_CucsVmVifVifId_Object = MibTableColumn
cucsVmVifVifId = _CucsVmVifVifId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 13),
    _CucsVmVifVifId_Type()
)
cucsVmVifVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifVifId.setStatus("current")
_CucsVmVifAdpVifId_Type = Gauge32
_CucsVmVifAdpVifId_Object = MibTableColumn
cucsVmVifAdpVifId = _CucsVmVifAdpVifId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 14),
    _CucsVmVifAdpVifId_Type()
)
cucsVmVifAdpVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifAdpVifId.setStatus("current")
_CucsVmVifLinkState_Type = CucsAdaptorLinkState
_CucsVmVifLinkState_Object = MibTableColumn
cucsVmVifLinkState = _CucsVmVifLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 15),
    _CucsVmVifLinkState_Type()
)
cucsVmVifLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifLinkState.setStatus("current")
_CucsVmVifOperState_Type = CucsDcxOperState
_CucsVmVifOperState_Object = MibTableColumn
cucsVmVifOperState = _CucsVmVifOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 16),
    _CucsVmVifOperState_Type()
)
cucsVmVifOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifOperState.setStatus("current")
_CucsVmVifStateQual_Type = SnmpAdminString
_CucsVmVifStateQual_Object = MibTableColumn
cucsVmVifStateQual = _CucsVmVifStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 17),
    _CucsVmVifStateQual_Type()
)
cucsVmVifStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifStateQual.setStatus("current")
_CucsVmVifPhsAccessAggrPortId_Type = Gauge32
_CucsVmVifPhsAccessAggrPortId_Object = MibTableColumn
cucsVmVifPhsAccessAggrPortId = _CucsVmVifPhsAccessAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 18),
    _CucsVmVifPhsAccessAggrPortId_Type()
)
cucsVmVifPhsAccessAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifPhsAccessAggrPortId.setStatus("current")
_CucsVmVifPhsBorderAggrPortId_Type = Gauge32
_CucsVmVifPhsBorderAggrPortId_Object = MibTableColumn
cucsVmVifPhsBorderAggrPortId = _CucsVmVifPhsBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 11, 1, 19),
    _CucsVmVifPhsBorderAggrPortId_Type()
)
cucsVmVifPhsBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVifPhsBorderAggrPortId.setStatus("current")
_CucsVmVlanTable_Object = MibTable
cucsVmVlanTable = _CucsVmVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12)
)
if mibBuilder.loadTexts:
    cucsVmVlanTable.setStatus("current")
_CucsVmVlanEntry_Object = MibTableRow
cucsVmVlanEntry = _CucsVmVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1)
)
cucsVmVlanEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmVlanEntry.setStatus("current")
_CucsVmVlanInstanceId_Type = CucsManagedObjectId
_CucsVmVlanInstanceId_Object = MibTableColumn
cucsVmVlanInstanceId = _CucsVmVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 1),
    _CucsVmVlanInstanceId_Type()
)
cucsVmVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmVlanInstanceId.setStatus("current")
_CucsVmVlanDn_Type = CucsManagedObjectDn
_CucsVmVlanDn_Object = MibTableColumn
cucsVmVlanDn = _CucsVmVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 2),
    _CucsVmVlanDn_Type()
)
cucsVmVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanDn.setStatus("current")
_CucsVmVlanRn_Type = SnmpAdminString
_CucsVmVlanRn_Object = MibTableColumn
cucsVmVlanRn = _CucsVmVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 3),
    _CucsVmVlanRn_Type()
)
cucsVmVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanRn.setStatus("current")
_CucsVmVlanEpDn_Type = SnmpAdminString
_CucsVmVlanEpDn_Object = MibTableColumn
cucsVmVlanEpDn = _CucsVmVlanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 4),
    _CucsVmVlanEpDn_Type()
)
cucsVmVlanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanEpDn.setStatus("current")
_CucsVmVlanId_Type = Gauge32
_CucsVmVlanId_Object = MibTableColumn
cucsVmVlanId = _CucsVmVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 5),
    _CucsVmVlanId_Type()
)
cucsVmVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanId.setStatus("current")
_CucsVmVlanIfRole_Type = CucsFabricVnetEpIfRole
_CucsVmVlanIfRole_Object = MibTableColumn
cucsVmVlanIfRole = _CucsVmVlanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 6),
    _CucsVmVlanIfRole_Type()
)
cucsVmVlanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanIfRole.setStatus("current")
_CucsVmVlanIfType_Type = CucsNetworkVnetEpIfType
_CucsVmVlanIfType_Object = MibTableColumn
cucsVmVlanIfType = _CucsVmVlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 7),
    _CucsVmVlanIfType_Type()
)
cucsVmVlanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanIfType.setStatus("current")
_CucsVmVlanLocale_Type = CucsFabricVnetEpLocale
_CucsVmVlanLocale_Object = MibTableColumn
cucsVmVlanLocale = _CucsVmVlanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 8),
    _CucsVmVlanLocale_Type()
)
cucsVmVlanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanLocale.setStatus("current")
_CucsVmVlanName_Type = SnmpAdminString
_CucsVmVlanName_Object = MibTableColumn
cucsVmVlanName = _CucsVmVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 9),
    _CucsVmVlanName_Type()
)
cucsVmVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanName.setStatus("current")
_CucsVmVlanPeerDn_Type = SnmpAdminString
_CucsVmVlanPeerDn_Object = MibTableColumn
cucsVmVlanPeerDn = _CucsVmVlanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 10),
    _CucsVmVlanPeerDn_Type()
)
cucsVmVlanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanPeerDn.setStatus("current")
_CucsVmVlanPubNwDn_Type = SnmpAdminString
_CucsVmVlanPubNwDn_Object = MibTableColumn
cucsVmVlanPubNwDn = _CucsVmVlanPubNwDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 11),
    _CucsVmVlanPubNwDn_Type()
)
cucsVmVlanPubNwDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanPubNwDn.setStatus("current")
_CucsVmVlanPubNwId_Type = Gauge32
_CucsVmVlanPubNwId_Object = MibTableColumn
cucsVmVlanPubNwId = _CucsVmVlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 12),
    _CucsVmVlanPubNwId_Type()
)
cucsVmVlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanPubNwId.setStatus("current")
_CucsVmVlanPubNwName_Type = SnmpAdminString
_CucsVmVlanPubNwName_Object = MibTableColumn
cucsVmVlanPubNwName = _CucsVmVlanPubNwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 13),
    _CucsVmVlanPubNwName_Type()
)
cucsVmVlanPubNwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanPubNwName.setStatus("current")
_CucsVmVlanSharing_Type = CucsFabricAVlanSharing
_CucsVmVlanSharing_Object = MibTableColumn
cucsVmVlanSharing = _CucsVmVlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 14),
    _CucsVmVlanSharing_Type()
)
cucsVmVlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanSharing.setStatus("current")
_CucsVmVlanSwitchId_Type = CucsNetworkSwitchId
_CucsVmVlanSwitchId_Object = MibTableColumn
cucsVmVlanSwitchId = _CucsVmVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 15),
    _CucsVmVlanSwitchId_Type()
)
cucsVmVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanSwitchId.setStatus("current")
_CucsVmVlanTransport_Type = CucsFabricAVlanTransport
_CucsVmVlanTransport_Object = MibTableColumn
cucsVmVlanTransport = _CucsVmVlanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 16),
    _CucsVmVlanTransport_Type()
)
cucsVmVlanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanTransport.setStatus("current")
_CucsVmVlanType_Type = CucsFabricAVlanType
_CucsVmVlanType_Object = MibTableColumn
cucsVmVlanType = _CucsVmVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 17),
    _CucsVmVlanType_Type()
)
cucsVmVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanType.setStatus("current")
_CucsVmVlanOperState_Type = CucsFabricVlanOperState
_CucsVmVlanOperState_Object = MibTableColumn
cucsVmVlanOperState = _CucsVmVlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 18),
    _CucsVmVlanOperState_Type()
)
cucsVmVlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanOperState.setStatus("current")
_CucsVmVlanPolicyOwner_Type = CucsFabricVnetEpPolicyOwner
_CucsVmVlanPolicyOwner_Object = MibTableColumn
cucsVmVlanPolicyOwner = _CucsVmVlanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 20),
    _CucsVmVlanPolicyOwner_Type()
)
cucsVmVlanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanPolicyOwner.setStatus("current")
_CucsVmVlanAssocPrimaryVlanState_Type = CucsFabricVlanAssocPrimaryVlanState
_CucsVmVlanAssocPrimaryVlanState_Object = MibTableColumn
cucsVmVlanAssocPrimaryVlanState = _CucsVmVlanAssocPrimaryVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 21),
    _CucsVmVlanAssocPrimaryVlanState_Type()
)
cucsVmVlanAssocPrimaryVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanAssocPrimaryVlanState.setStatus("current")
_CucsVmVlanAssocPrimaryVlanSwitchId_Type = CucsFabricAVlanAssocPrimaryVlanSwitchId
_CucsVmVlanAssocPrimaryVlanSwitchId_Object = MibTableColumn
cucsVmVlanAssocPrimaryVlanSwitchId = _CucsVmVlanAssocPrimaryVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 22),
    _CucsVmVlanAssocPrimaryVlanSwitchId_Type()
)
cucsVmVlanAssocPrimaryVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanAssocPrimaryVlanSwitchId.setStatus("current")
_CucsVmVlanOverlapStateForA_Type = CucsFabricVlanOverlapState
_CucsVmVlanOverlapStateForA_Object = MibTableColumn
cucsVmVlanOverlapStateForA = _CucsVmVlanOverlapStateForA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 23),
    _CucsVmVlanOverlapStateForA_Type()
)
cucsVmVlanOverlapStateForA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanOverlapStateForA.setStatus("current")
_CucsVmVlanOverlapStateForB_Type = CucsFabricVlanOverlapState
_CucsVmVlanOverlapStateForB_Object = MibTableColumn
cucsVmVlanOverlapStateForB = _CucsVmVlanOverlapStateForB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 12, 1, 24),
    _CucsVmVlanOverlapStateForB_Type()
)
cucsVmVlanOverlapStateForB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVlanOverlapStateForB.setStatus("current")
_CucsVmVnicProfClTable_Object = MibTable
cucsVmVnicProfClTable = _CucsVmVnicProfClTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 13)
)
if mibBuilder.loadTexts:
    cucsVmVnicProfClTable.setStatus("current")
_CucsVmVnicProfClEntry_Object = MibTableRow
cucsVmVnicProfClEntry = _CucsVmVnicProfClEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 13, 1)
)
cucsVmVnicProfClEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmVnicProfClInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmVnicProfClEntry.setStatus("current")
_CucsVmVnicProfClInstanceId_Type = CucsManagedObjectId
_CucsVmVnicProfClInstanceId_Object = MibTableColumn
cucsVmVnicProfClInstanceId = _CucsVmVnicProfClInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 13, 1, 1),
    _CucsVmVnicProfClInstanceId_Type()
)
cucsVmVnicProfClInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmVnicProfClInstanceId.setStatus("current")
_CucsVmVnicProfClDn_Type = CucsManagedObjectDn
_CucsVmVnicProfClDn_Object = MibTableColumn
cucsVmVnicProfClDn = _CucsVmVnicProfClDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 13, 1, 2),
    _CucsVmVnicProfClDn_Type()
)
cucsVmVnicProfClDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfClDn.setStatus("current")
_CucsVmVnicProfClRn_Type = SnmpAdminString
_CucsVmVnicProfClRn_Object = MibTableColumn
cucsVmVnicProfClRn = _CucsVmVnicProfClRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 13, 1, 3),
    _CucsVmVnicProfClRn_Type()
)
cucsVmVnicProfClRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfClRn.setStatus("current")
_CucsVmVnicProfClDcName_Type = SnmpAdminString
_CucsVmVnicProfClDcName_Object = MibTableColumn
cucsVmVnicProfClDcName = _CucsVmVnicProfClDcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 13, 1, 4),
    _CucsVmVnicProfClDcName_Type()
)
cucsVmVnicProfClDcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfClDcName.setStatus("current")
_CucsVmVnicProfClDescr_Type = SnmpAdminString
_CucsVmVnicProfClDescr_Object = MibTableColumn
cucsVmVnicProfClDescr = _CucsVmVnicProfClDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 13, 1, 5),
    _CucsVmVnicProfClDescr_Type()
)
cucsVmVnicProfClDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfClDescr.setStatus("current")
_CucsVmVnicProfClIntId_Type = SnmpAdminString
_CucsVmVnicProfClIntId_Object = MibTableColumn
cucsVmVnicProfClIntId = _CucsVmVnicProfClIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 13, 1, 6),
    _CucsVmVnicProfClIntId_Type()
)
cucsVmVnicProfClIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfClIntId.setStatus("current")
_CucsVmVnicProfClName_Type = SnmpAdminString
_CucsVmVnicProfClName_Object = MibTableColumn
cucsVmVnicProfClName = _CucsVmVnicProfClName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 13, 1, 7),
    _CucsVmVnicProfClName_Type()
)
cucsVmVnicProfClName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfClName.setStatus("current")
_CucsVmVnicProfClOrgPath_Type = SnmpAdminString
_CucsVmVnicProfClOrgPath_Object = MibTableColumn
cucsVmVnicProfClOrgPath = _CucsVmVnicProfClOrgPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 13, 1, 8),
    _CucsVmVnicProfClOrgPath_Type()
)
cucsVmVnicProfClOrgPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfClOrgPath.setStatus("current")
_CucsVmVnicProfClSwName_Type = SnmpAdminString
_CucsVmVnicProfClSwName_Object = MibTableColumn
cucsVmVnicProfClSwName = _CucsVmVnicProfClSwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 13, 1, 9),
    _CucsVmVnicProfClSwName_Type()
)
cucsVmVnicProfClSwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfClSwName.setStatus("current")
_CucsVmVnicProfClPolicyLevel_Type = Gauge32
_CucsVmVnicProfClPolicyLevel_Object = MibTableColumn
cucsVmVnicProfClPolicyLevel = _CucsVmVnicProfClPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 13, 1, 10),
    _CucsVmVnicProfClPolicyLevel_Type()
)
cucsVmVnicProfClPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfClPolicyLevel.setStatus("current")
_CucsVmVnicProfClPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVmVnicProfClPolicyOwner_Object = MibTableColumn
cucsVmVnicProfClPolicyOwner = _CucsVmVnicProfClPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 13, 1, 11),
    _CucsVmVnicProfClPolicyOwner_Type()
)
cucsVmVnicProfClPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfClPolicyOwner.setStatus("current")
_CucsVmVnicProfInstTable_Object = MibTable
cucsVmVnicProfInstTable = _CucsVmVnicProfInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 14)
)
if mibBuilder.loadTexts:
    cucsVmVnicProfInstTable.setStatus("current")
_CucsVmVnicProfInstEntry_Object = MibTableRow
cucsVmVnicProfInstEntry = _CucsVmVnicProfInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 14, 1)
)
cucsVmVnicProfInstEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmVnicProfInstInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmVnicProfInstEntry.setStatus("current")
_CucsVmVnicProfInstInstanceId_Type = CucsManagedObjectId
_CucsVmVnicProfInstInstanceId_Object = MibTableColumn
cucsVmVnicProfInstInstanceId = _CucsVmVnicProfInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 14, 1, 1),
    _CucsVmVnicProfInstInstanceId_Type()
)
cucsVmVnicProfInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmVnicProfInstInstanceId.setStatus("current")
_CucsVmVnicProfInstDn_Type = CucsManagedObjectDn
_CucsVmVnicProfInstDn_Object = MibTableColumn
cucsVmVnicProfInstDn = _CucsVmVnicProfInstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 14, 1, 2),
    _CucsVmVnicProfInstDn_Type()
)
cucsVmVnicProfInstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfInstDn.setStatus("current")
_CucsVmVnicProfInstRn_Type = SnmpAdminString
_CucsVmVnicProfInstRn_Object = MibTableColumn
cucsVmVnicProfInstRn = _CucsVmVnicProfInstRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 14, 1, 3),
    _CucsVmVnicProfInstRn_Type()
)
cucsVmVnicProfInstRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfInstRn.setStatus("current")
_CucsVmVnicProfInstDescr_Type = SnmpAdminString
_CucsVmVnicProfInstDescr_Object = MibTableColumn
cucsVmVnicProfInstDescr = _CucsVmVnicProfInstDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 14, 1, 4),
    _CucsVmVnicProfInstDescr_Type()
)
cucsVmVnicProfInstDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfInstDescr.setStatus("current")
_CucsVmVnicProfInstIntId_Type = SnmpAdminString
_CucsVmVnicProfInstIntId_Object = MibTableColumn
cucsVmVnicProfInstIntId = _CucsVmVnicProfInstIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 14, 1, 5),
    _CucsVmVnicProfInstIntId_Type()
)
cucsVmVnicProfInstIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfInstIntId.setStatus("current")
_CucsVmVnicProfInstMaxPorts_Type = Gauge32
_CucsVmVnicProfInstMaxPorts_Object = MibTableColumn
cucsVmVnicProfInstMaxPorts = _CucsVmVnicProfInstMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 14, 1, 6),
    _CucsVmVnicProfInstMaxPorts_Type()
)
cucsVmVnicProfInstMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfInstMaxPorts.setStatus("current")
_CucsVmVnicProfInstName_Type = SnmpAdminString
_CucsVmVnicProfInstName_Object = MibTableColumn
cucsVmVnicProfInstName = _CucsVmVnicProfInstName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 14, 1, 7),
    _CucsVmVnicProfInstName_Type()
)
cucsVmVnicProfInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfInstName.setStatus("current")
_CucsVmVnicProfInstProfDn_Type = SnmpAdminString
_CucsVmVnicProfInstProfDn_Object = MibTableColumn
cucsVmVnicProfInstProfDn = _CucsVmVnicProfInstProfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 14, 1, 8),
    _CucsVmVnicProfInstProfDn_Type()
)
cucsVmVnicProfInstProfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfInstProfDn.setStatus("current")
_CucsVmVnicProfInstPolicyLevel_Type = Gauge32
_CucsVmVnicProfInstPolicyLevel_Object = MibTableColumn
cucsVmVnicProfInstPolicyLevel = _CucsVmVnicProfInstPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 14, 1, 9),
    _CucsVmVnicProfInstPolicyLevel_Type()
)
cucsVmVnicProfInstPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfInstPolicyLevel.setStatus("current")
_CucsVmVnicProfInstPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVmVnicProfInstPolicyOwner_Object = MibTableColumn
cucsVmVnicProfInstPolicyOwner = _CucsVmVnicProfInstPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 14, 1, 10),
    _CucsVmVnicProfInstPolicyOwner_Type()
)
cucsVmVnicProfInstPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfInstPolicyOwner.setStatus("current")
_CucsVmVnicProfInstProfileType_Type = CucsVnicPortProfileType
_CucsVmVnicProfInstProfileType_Object = MibTableColumn
cucsVmVnicProfInstProfileType = _CucsVmVnicProfInstProfileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 14, 1, 11),
    _CucsVmVnicProfInstProfileType_Type()
)
cucsVmVnicProfInstProfileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVnicProfInstProfileType.setStatus("current")
_CucsVmVsanTable_Object = MibTable
cucsVmVsanTable = _CucsVmVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15)
)
if mibBuilder.loadTexts:
    cucsVmVsanTable.setStatus("current")
_CucsVmVsanEntry_Object = MibTableRow
cucsVmVsanEntry = _CucsVmVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1)
)
cucsVmVsanEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmVsanInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmVsanEntry.setStatus("current")
_CucsVmVsanInstanceId_Type = CucsManagedObjectId
_CucsVmVsanInstanceId_Object = MibTableColumn
cucsVmVsanInstanceId = _CucsVmVsanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1, 1),
    _CucsVmVsanInstanceId_Type()
)
cucsVmVsanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmVsanInstanceId.setStatus("current")
_CucsVmVsanDn_Type = CucsManagedObjectDn
_CucsVmVsanDn_Object = MibTableColumn
cucsVmVsanDn = _CucsVmVsanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1, 2),
    _CucsVmVsanDn_Type()
)
cucsVmVsanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVsanDn.setStatus("current")
_CucsVmVsanRn_Type = SnmpAdminString
_CucsVmVsanRn_Object = MibTableColumn
cucsVmVsanRn = _CucsVmVsanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1, 3),
    _CucsVmVsanRn_Type()
)
cucsVmVsanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVsanRn.setStatus("current")
_CucsVmVsanEpDn_Type = SnmpAdminString
_CucsVmVsanEpDn_Object = MibTableColumn
cucsVmVsanEpDn = _CucsVmVsanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1, 4),
    _CucsVmVsanEpDn_Type()
)
cucsVmVsanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVsanEpDn.setStatus("current")
_CucsVmVsanFcoeVlan_Type = Gauge32
_CucsVmVsanFcoeVlan_Object = MibTableColumn
cucsVmVsanFcoeVlan = _CucsVmVsanFcoeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1, 5),
    _CucsVmVsanFcoeVlan_Type()
)
cucsVmVsanFcoeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVsanFcoeVlan.setStatus("current")
_CucsVmVsanId_Type = Gauge32
_CucsVmVsanId_Object = MibTableColumn
cucsVmVsanId = _CucsVmVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1, 6),
    _CucsVmVsanId_Type()
)
cucsVmVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVsanId.setStatus("current")
_CucsVmVsanIfRole_Type = CucsFabricVnetEpIfRole
_CucsVmVsanIfRole_Object = MibTableColumn
cucsVmVsanIfRole = _CucsVmVsanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1, 7),
    _CucsVmVsanIfRole_Type()
)
cucsVmVsanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVsanIfRole.setStatus("current")
_CucsVmVsanIfType_Type = CucsNetworkVnetEpIfType
_CucsVmVsanIfType_Object = MibTableColumn
cucsVmVsanIfType = _CucsVmVsanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1, 8),
    _CucsVmVsanIfType_Type()
)
cucsVmVsanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVsanIfType.setStatus("current")
_CucsVmVsanLocale_Type = CucsFabricVnetEpLocale
_CucsVmVsanLocale_Object = MibTableColumn
cucsVmVsanLocale = _CucsVmVsanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1, 9),
    _CucsVmVsanLocale_Type()
)
cucsVmVsanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVsanLocale.setStatus("current")
_CucsVmVsanName_Type = SnmpAdminString
_CucsVmVsanName_Object = MibTableColumn
cucsVmVsanName = _CucsVmVsanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1, 10),
    _CucsVmVsanName_Type()
)
cucsVmVsanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVsanName.setStatus("current")
_CucsVmVsanPeerDn_Type = SnmpAdminString
_CucsVmVsanPeerDn_Object = MibTableColumn
cucsVmVsanPeerDn = _CucsVmVsanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1, 11),
    _CucsVmVsanPeerDn_Type()
)
cucsVmVsanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVsanPeerDn.setStatus("current")
_CucsVmVsanSwitchId_Type = CucsNetworkSwitchId
_CucsVmVsanSwitchId_Object = MibTableColumn
cucsVmVsanSwitchId = _CucsVmVsanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1, 12),
    _CucsVmVsanSwitchId_Type()
)
cucsVmVsanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVsanSwitchId.setStatus("current")
_CucsVmVsanTransport_Type = CucsFabricAVsanTransport
_CucsVmVsanTransport_Object = MibTableColumn
cucsVmVsanTransport = _CucsVmVsanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1, 13),
    _CucsVmVsanTransport_Type()
)
cucsVmVsanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVsanTransport.setStatus("current")
_CucsVmVsanType_Type = CucsFabricAVsanType
_CucsVmVsanType_Object = MibTableColumn
cucsVmVsanType = _CucsVmVsanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1, 14),
    _CucsVmVsanType_Type()
)
cucsVmVsanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVsanType.setStatus("current")
_CucsVmVsanOperState_Type = CucsFabricVsanOperState
_CucsVmVsanOperState_Object = MibTableColumn
cucsVmVsanOperState = _CucsVmVsanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1, 15),
    _CucsVmVsanOperState_Type()
)
cucsVmVsanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVsanOperState.setStatus("current")
_CucsVmVsanZoningState_Type = CucsFabricZoningState
_CucsVmVsanZoningState_Object = MibTableColumn
cucsVmVsanZoningState = _CucsVmVsanZoningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1, 16),
    _CucsVmVsanZoningState_Type()
)
cucsVmVsanZoningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVsanZoningState.setStatus("current")
_CucsVmVsanPolicyOwner_Type = CucsFabricVnetEpPolicyOwner
_CucsVmVsanPolicyOwner_Object = MibTableColumn
cucsVmVsanPolicyOwner = _CucsVmVsanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 15, 1, 18),
    _CucsVmVsanPolicyOwner_Type()
)
cucsVmVsanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmVsanPolicyOwner.setStatus("current")
_CucsVmComputeEpTable_Object = MibTable
cucsVmComputeEpTable = _CucsVmComputeEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16)
)
if mibBuilder.loadTexts:
    cucsVmComputeEpTable.setStatus("current")
_CucsVmComputeEpEntry_Object = MibTableRow
cucsVmComputeEpEntry = _CucsVmComputeEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1)
)
cucsVmComputeEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmComputeEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmComputeEpEntry.setStatus("current")
_CucsVmComputeEpInstanceId_Type = CucsManagedObjectId
_CucsVmComputeEpInstanceId_Object = MibTableColumn
cucsVmComputeEpInstanceId = _CucsVmComputeEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 1),
    _CucsVmComputeEpInstanceId_Type()
)
cucsVmComputeEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmComputeEpInstanceId.setStatus("current")
_CucsVmComputeEpDn_Type = CucsManagedObjectDn
_CucsVmComputeEpDn_Object = MibTableColumn
cucsVmComputeEpDn = _CucsVmComputeEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 2),
    _CucsVmComputeEpDn_Type()
)
cucsVmComputeEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpDn.setStatus("current")
_CucsVmComputeEpRn_Type = SnmpAdminString
_CucsVmComputeEpRn_Object = MibTableColumn
cucsVmComputeEpRn = _CucsVmComputeEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 3),
    _CucsVmComputeEpRn_Type()
)
cucsVmComputeEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpRn.setStatus("current")
_CucsVmComputeEpClInstType_Type = CucsVmComputeEpClInstType
_CucsVmComputeEpClInstType_Object = MibTableColumn
cucsVmComputeEpClInstType = _CucsVmComputeEpClInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 4),
    _CucsVmComputeEpClInstType_Type()
)
cucsVmComputeEpClInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpClInstType.setStatus("current")
_CucsVmComputeEpComputeEpVendor_Type = SnmpAdminString
_CucsVmComputeEpComputeEpVendor_Object = MibTableColumn
cucsVmComputeEpComputeEpVendor = _CucsVmComputeEpComputeEpVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 5),
    _CucsVmComputeEpComputeEpVendor_Type()
)
cucsVmComputeEpComputeEpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpComputeEpVendor.setStatus("current")
_CucsVmComputeEpDescr_Type = SnmpAdminString
_CucsVmComputeEpDescr_Object = MibTableColumn
cucsVmComputeEpDescr = _CucsVmComputeEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 6),
    _CucsVmComputeEpDescr_Type()
)
cucsVmComputeEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpDescr.setStatus("current")
_CucsVmComputeEpDvsDn_Type = SnmpAdminString
_CucsVmComputeEpDvsDn_Object = MibTableColumn
cucsVmComputeEpDvsDn = _CucsVmComputeEpDvsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 7),
    _CucsVmComputeEpDvsDn_Type()
)
cucsVmComputeEpDvsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpDvsDn.setStatus("current")
_CucsVmComputeEpDvsName_Type = SnmpAdminString
_CucsVmComputeEpDvsName_Object = MibTableColumn
cucsVmComputeEpDvsName = _CucsVmComputeEpDvsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 8),
    _CucsVmComputeEpDvsName_Type()
)
cucsVmComputeEpDvsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpDvsName.setStatus("current")
_CucsVmComputeEpHostName_Type = SnmpAdminString
_CucsVmComputeEpHostName_Object = MibTableColumn
cucsVmComputeEpHostName = _CucsVmComputeEpHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 9),
    _CucsVmComputeEpHostName_Type()
)
cucsVmComputeEpHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpHostName.setStatus("current")
_CucsVmComputeEpIntId_Type = SnmpAdminString
_CucsVmComputeEpIntId_Object = MibTableColumn
cucsVmComputeEpIntId = _CucsVmComputeEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 10),
    _CucsVmComputeEpIntId_Type()
)
cucsVmComputeEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpIntId.setStatus("current")
_CucsVmComputeEpLsDn_Type = SnmpAdminString
_CucsVmComputeEpLsDn_Object = MibTableColumn
cucsVmComputeEpLsDn = _CucsVmComputeEpLsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 11),
    _CucsVmComputeEpLsDn_Type()
)
cucsVmComputeEpLsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpLsDn.setStatus("current")
_CucsVmComputeEpModel_Type = CucsOsOsType
_CucsVmComputeEpModel_Object = MibTableColumn
cucsVmComputeEpModel = _CucsVmComputeEpModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 12),
    _CucsVmComputeEpModel_Type()
)
cucsVmComputeEpModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpModel.setStatus("current")
_CucsVmComputeEpName_Type = SnmpAdminString
_CucsVmComputeEpName_Object = MibTableColumn
cucsVmComputeEpName = _CucsVmComputeEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 13),
    _CucsVmComputeEpName_Type()
)
cucsVmComputeEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpName.setStatus("current")
_CucsVmComputeEpPnDn_Type = SnmpAdminString
_CucsVmComputeEpPnDn_Object = MibTableColumn
cucsVmComputeEpPnDn = _CucsVmComputeEpPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 14),
    _CucsVmComputeEpPnDn_Type()
)
cucsVmComputeEpPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpPnDn.setStatus("current")
_CucsVmComputeEpStatusChangeTs_Type = DateAndTime
_CucsVmComputeEpStatusChangeTs_Object = MibTableColumn
cucsVmComputeEpStatusChangeTs = _CucsVmComputeEpStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 15),
    _CucsVmComputeEpStatusChangeTs_Type()
)
cucsVmComputeEpStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpStatusChangeTs.setStatus("current")
_CucsVmComputeEpUuid_Type = SnmpAdminString
_CucsVmComputeEpUuid_Object = MibTableColumn
cucsVmComputeEpUuid = _CucsVmComputeEpUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 16),
    _CucsVmComputeEpUuid_Type()
)
cucsVmComputeEpUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpUuid.setStatus("current")
_CucsVmComputeEpVStatus_Type = CucsVmStatus
_CucsVmComputeEpVStatus_Object = MibTableColumn
cucsVmComputeEpVStatus = _CucsVmComputeEpVStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 17),
    _CucsVmComputeEpVStatus_Type()
)
cucsVmComputeEpVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpVStatus.setStatus("current")
_CucsVmComputeEpVendor_Type = CucsVmOsHvVendor
_CucsVmComputeEpVendor_Object = MibTableColumn
cucsVmComputeEpVendor = _CucsVmComputeEpVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 18),
    _CucsVmComputeEpVendor_Type()
)
cucsVmComputeEpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpVendor.setStatus("current")
_CucsVmComputeEpPolicyLevel_Type = Gauge32
_CucsVmComputeEpPolicyLevel_Object = MibTableColumn
cucsVmComputeEpPolicyLevel = _CucsVmComputeEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 19),
    _CucsVmComputeEpPolicyLevel_Type()
)
cucsVmComputeEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpPolicyLevel.setStatus("current")
_CucsVmComputeEpPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVmComputeEpPolicyOwner_Object = MibTableColumn
cucsVmComputeEpPolicyOwner = _CucsVmComputeEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 16, 1, 20),
    _CucsVmComputeEpPolicyOwner_Type()
)
cucsVmComputeEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmComputeEpPolicyOwner.setStatus("current")
_CucsVmLifeCyclePolicyFsmTaskTable_Object = MibTable
cucsVmLifeCyclePolicyFsmTaskTable = _CucsVmLifeCyclePolicyFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 17)
)
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmTaskTable.setStatus("current")
_CucsVmLifeCyclePolicyFsmTaskEntry_Object = MibTableRow
cucsVmLifeCyclePolicyFsmTaskEntry = _CucsVmLifeCyclePolicyFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 17, 1)
)
cucsVmLifeCyclePolicyFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmLifeCyclePolicyFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmTaskEntry.setStatus("current")
_CucsVmLifeCyclePolicyFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsVmLifeCyclePolicyFsmTaskInstanceId_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmTaskInstanceId = _CucsVmLifeCyclePolicyFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 17, 1, 1),
    _CucsVmLifeCyclePolicyFsmTaskInstanceId_Type()
)
cucsVmLifeCyclePolicyFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmTaskInstanceId.setStatus("current")
_CucsVmLifeCyclePolicyFsmTaskDn_Type = CucsManagedObjectDn
_CucsVmLifeCyclePolicyFsmTaskDn_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmTaskDn = _CucsVmLifeCyclePolicyFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 17, 1, 2),
    _CucsVmLifeCyclePolicyFsmTaskDn_Type()
)
cucsVmLifeCyclePolicyFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmTaskDn.setStatus("current")
_CucsVmLifeCyclePolicyFsmTaskRn_Type = SnmpAdminString
_CucsVmLifeCyclePolicyFsmTaskRn_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmTaskRn = _CucsVmLifeCyclePolicyFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 17, 1, 3),
    _CucsVmLifeCyclePolicyFsmTaskRn_Type()
)
cucsVmLifeCyclePolicyFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmTaskRn.setStatus("current")
_CucsVmLifeCyclePolicyFsmTaskCompletion_Type = CucsFsmCompletion
_CucsVmLifeCyclePolicyFsmTaskCompletion_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmTaskCompletion = _CucsVmLifeCyclePolicyFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 17, 1, 4),
    _CucsVmLifeCyclePolicyFsmTaskCompletion_Type()
)
cucsVmLifeCyclePolicyFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmTaskCompletion.setStatus("current")
_CucsVmLifeCyclePolicyFsmTaskFlags_Type = CucsFsmFlags
_CucsVmLifeCyclePolicyFsmTaskFlags_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmTaskFlags = _CucsVmLifeCyclePolicyFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 17, 1, 5),
    _CucsVmLifeCyclePolicyFsmTaskFlags_Type()
)
cucsVmLifeCyclePolicyFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmTaskFlags.setStatus("current")
_CucsVmLifeCyclePolicyFsmTaskItem_Type = CucsVmLifeCyclePolicyFsmTaskItem
_CucsVmLifeCyclePolicyFsmTaskItem_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmTaskItem = _CucsVmLifeCyclePolicyFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 17, 1, 6),
    _CucsVmLifeCyclePolicyFsmTaskItem_Type()
)
cucsVmLifeCyclePolicyFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmTaskItem.setStatus("current")
_CucsVmLifeCyclePolicyFsmTaskSeqId_Type = Gauge32
_CucsVmLifeCyclePolicyFsmTaskSeqId_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmTaskSeqId = _CucsVmLifeCyclePolicyFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 17, 1, 7),
    _CucsVmLifeCyclePolicyFsmTaskSeqId_Type()
)
cucsVmLifeCyclePolicyFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmTaskSeqId.setStatus("current")
_CucsVmLifeCyclePolicyFsmTable_Object = MibTable
cucsVmLifeCyclePolicyFsmTable = _CucsVmLifeCyclePolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 18)
)
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmTable.setStatus("current")
_CucsVmLifeCyclePolicyFsmEntry_Object = MibTableRow
cucsVmLifeCyclePolicyFsmEntry = _CucsVmLifeCyclePolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 18, 1)
)
cucsVmLifeCyclePolicyFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmLifeCyclePolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmEntry.setStatus("current")
_CucsVmLifeCyclePolicyFsmInstanceId_Type = CucsManagedObjectId
_CucsVmLifeCyclePolicyFsmInstanceId_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmInstanceId = _CucsVmLifeCyclePolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 18, 1, 1),
    _CucsVmLifeCyclePolicyFsmInstanceId_Type()
)
cucsVmLifeCyclePolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmInstanceId.setStatus("current")
_CucsVmLifeCyclePolicyFsmDn_Type = CucsManagedObjectDn
_CucsVmLifeCyclePolicyFsmDn_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmDn = _CucsVmLifeCyclePolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 18, 1, 2),
    _CucsVmLifeCyclePolicyFsmDn_Type()
)
cucsVmLifeCyclePolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmDn.setStatus("current")
_CucsVmLifeCyclePolicyFsmRn_Type = SnmpAdminString
_CucsVmLifeCyclePolicyFsmRn_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmRn = _CucsVmLifeCyclePolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 18, 1, 3),
    _CucsVmLifeCyclePolicyFsmRn_Type()
)
cucsVmLifeCyclePolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmRn.setStatus("current")
_CucsVmLifeCyclePolicyFsmCompletionTime_Type = DateAndTime
_CucsVmLifeCyclePolicyFsmCompletionTime_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmCompletionTime = _CucsVmLifeCyclePolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 18, 1, 4),
    _CucsVmLifeCyclePolicyFsmCompletionTime_Type()
)
cucsVmLifeCyclePolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmCompletionTime.setStatus("current")
_CucsVmLifeCyclePolicyFsmCurrentFsm_Type = CucsVmLifeCyclePolicyFsmCurrentFsm
_CucsVmLifeCyclePolicyFsmCurrentFsm_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmCurrentFsm = _CucsVmLifeCyclePolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 18, 1, 5),
    _CucsVmLifeCyclePolicyFsmCurrentFsm_Type()
)
cucsVmLifeCyclePolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmCurrentFsm.setStatus("current")
_CucsVmLifeCyclePolicyFsmDescrData_Type = SnmpAdminString
_CucsVmLifeCyclePolicyFsmDescrData_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmDescrData = _CucsVmLifeCyclePolicyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 18, 1, 6),
    _CucsVmLifeCyclePolicyFsmDescrData_Type()
)
cucsVmLifeCyclePolicyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmDescrData.setStatus("current")
_CucsVmLifeCyclePolicyFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsVmLifeCyclePolicyFsmFsmStatus_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmFsmStatus = _CucsVmLifeCyclePolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 18, 1, 7),
    _CucsVmLifeCyclePolicyFsmFsmStatus_Type()
)
cucsVmLifeCyclePolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmFsmStatus.setStatus("current")
_CucsVmLifeCyclePolicyFsmProgress_Type = Gauge32
_CucsVmLifeCyclePolicyFsmProgress_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmProgress = _CucsVmLifeCyclePolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 18, 1, 8),
    _CucsVmLifeCyclePolicyFsmProgress_Type()
)
cucsVmLifeCyclePolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmProgress.setStatus("current")
_CucsVmLifeCyclePolicyFsmRmtErrCode_Type = Gauge32
_CucsVmLifeCyclePolicyFsmRmtErrCode_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmRmtErrCode = _CucsVmLifeCyclePolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 18, 1, 9),
    _CucsVmLifeCyclePolicyFsmRmtErrCode_Type()
)
cucsVmLifeCyclePolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmRmtErrCode.setStatus("current")
_CucsVmLifeCyclePolicyFsmRmtErrDescr_Type = SnmpAdminString
_CucsVmLifeCyclePolicyFsmRmtErrDescr_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmRmtErrDescr = _CucsVmLifeCyclePolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 18, 1, 10),
    _CucsVmLifeCyclePolicyFsmRmtErrDescr_Type()
)
cucsVmLifeCyclePolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmRmtErrDescr.setStatus("current")
_CucsVmLifeCyclePolicyFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsVmLifeCyclePolicyFsmRmtRslt_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmRmtRslt = _CucsVmLifeCyclePolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 18, 1, 11),
    _CucsVmLifeCyclePolicyFsmRmtRslt_Type()
)
cucsVmLifeCyclePolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmRmtRslt.setStatus("current")
_CucsVmLifeCyclePolicyFsmStageTable_Object = MibTable
cucsVmLifeCyclePolicyFsmStageTable = _CucsVmLifeCyclePolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 19)
)
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmStageTable.setStatus("current")
_CucsVmLifeCyclePolicyFsmStageEntry_Object = MibTableRow
cucsVmLifeCyclePolicyFsmStageEntry = _CucsVmLifeCyclePolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 19, 1)
)
cucsVmLifeCyclePolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VM-MIB", "cucsVmLifeCyclePolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmStageEntry.setStatus("current")
_CucsVmLifeCyclePolicyFsmStageInstanceId_Type = CucsManagedObjectId
_CucsVmLifeCyclePolicyFsmStageInstanceId_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmStageInstanceId = _CucsVmLifeCyclePolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 19, 1, 1),
    _CucsVmLifeCyclePolicyFsmStageInstanceId_Type()
)
cucsVmLifeCyclePolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmStageInstanceId.setStatus("current")
_CucsVmLifeCyclePolicyFsmStageDn_Type = CucsManagedObjectDn
_CucsVmLifeCyclePolicyFsmStageDn_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmStageDn = _CucsVmLifeCyclePolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 19, 1, 2),
    _CucsVmLifeCyclePolicyFsmStageDn_Type()
)
cucsVmLifeCyclePolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmStageDn.setStatus("current")
_CucsVmLifeCyclePolicyFsmStageRn_Type = SnmpAdminString
_CucsVmLifeCyclePolicyFsmStageRn_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmStageRn = _CucsVmLifeCyclePolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 19, 1, 3),
    _CucsVmLifeCyclePolicyFsmStageRn_Type()
)
cucsVmLifeCyclePolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmStageRn.setStatus("current")
_CucsVmLifeCyclePolicyFsmStageDescrData_Type = SnmpAdminString
_CucsVmLifeCyclePolicyFsmStageDescrData_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmStageDescrData = _CucsVmLifeCyclePolicyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 19, 1, 4),
    _CucsVmLifeCyclePolicyFsmStageDescrData_Type()
)
cucsVmLifeCyclePolicyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmStageDescrData.setStatus("current")
_CucsVmLifeCyclePolicyFsmStageLastUpdateTime_Type = DateAndTime
_CucsVmLifeCyclePolicyFsmStageLastUpdateTime_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmStageLastUpdateTime = _CucsVmLifeCyclePolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 19, 1, 5),
    _CucsVmLifeCyclePolicyFsmStageLastUpdateTime_Type()
)
cucsVmLifeCyclePolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmStageLastUpdateTime.setStatus("current")
_CucsVmLifeCyclePolicyFsmStageName_Type = CucsVmLifeCyclePolicyFsmStageName
_CucsVmLifeCyclePolicyFsmStageName_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmStageName = _CucsVmLifeCyclePolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 19, 1, 6),
    _CucsVmLifeCyclePolicyFsmStageName_Type()
)
cucsVmLifeCyclePolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmStageName.setStatus("current")
_CucsVmLifeCyclePolicyFsmStageOrder_Type = Gauge32
_CucsVmLifeCyclePolicyFsmStageOrder_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmStageOrder = _CucsVmLifeCyclePolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 19, 1, 7),
    _CucsVmLifeCyclePolicyFsmStageOrder_Type()
)
cucsVmLifeCyclePolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmStageOrder.setStatus("current")
_CucsVmLifeCyclePolicyFsmStageRetry_Type = Gauge32
_CucsVmLifeCyclePolicyFsmStageRetry_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmStageRetry = _CucsVmLifeCyclePolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 19, 1, 8),
    _CucsVmLifeCyclePolicyFsmStageRetry_Type()
)
cucsVmLifeCyclePolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmStageRetry.setStatus("current")
_CucsVmLifeCyclePolicyFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsVmLifeCyclePolicyFsmStageStageStatus_Object = MibTableColumn
cucsVmLifeCyclePolicyFsmStageStageStatus = _CucsVmLifeCyclePolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 52, 19, 1, 9),
    _CucsVmLifeCyclePolicyFsmStageStageStatus_Type()
)
cucsVmLifeCyclePolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVmLifeCyclePolicyFsmStageStageStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-VM-MIB",
    **{"cucsVmObjects": cucsVmObjects,
       "cucsVmDCTable": cucsVmDCTable,
       "cucsVmDCEntry": cucsVmDCEntry,
       "cucsVmDCInstanceId": cucsVmDCInstanceId,
       "cucsVmDCDn": cucsVmDCDn,
       "cucsVmDCRn": cucsVmDCRn,
       "cucsVmDCDescr": cucsVmDCDescr,
       "cucsVmDCIntId": cucsVmDCIntId,
       "cucsVmDCName": cucsVmDCName,
       "cucsVmDCOwn": cucsVmDCOwn,
       "cucsVmDCUuid": cucsVmDCUuid,
       "cucsVmDCPolicyLevel": cucsVmDCPolicyLevel,
       "cucsVmDCPolicyOwner": cucsVmDCPolicyOwner,
       "cucsVmDCOrgTable": cucsVmDCOrgTable,
       "cucsVmDCOrgEntry": cucsVmDCOrgEntry,
       "cucsVmDCOrgInstanceId": cucsVmDCOrgInstanceId,
       "cucsVmDCOrgDn": cucsVmDCOrgDn,
       "cucsVmDCOrgRn": cucsVmDCOrgRn,
       "cucsVmDCOrgDescr": cucsVmDCOrgDescr,
       "cucsVmDCOrgIntId": cucsVmDCOrgIntId,
       "cucsVmDCOrgName": cucsVmDCOrgName,
       "cucsVmDCOrgOwn": cucsVmDCOrgOwn,
       "cucsVmDCOrgUuid": cucsVmDCOrgUuid,
       "cucsVmDCOrgPolicyLevel": cucsVmDCOrgPolicyLevel,
       "cucsVmDCOrgPolicyOwner": cucsVmDCOrgPolicyOwner,
       "cucsVmEpTable": cucsVmEpTable,
       "cucsVmEpEntry": cucsVmEpEntry,
       "cucsVmEpInstanceId": cucsVmEpInstanceId,
       "cucsVmEpDn": cucsVmEpDn,
       "cucsVmEpRn": cucsVmEpRn,
       "cucsVmHbaTable": cucsVmHbaTable,
       "cucsVmHbaEntry": cucsVmHbaEntry,
       "cucsVmHbaInstanceId": cucsVmHbaInstanceId,
       "cucsVmHbaDn": cucsVmHbaDn,
       "cucsVmHbaRn": cucsVmHbaRn,
       "cucsVmHbaDvsPortId": cucsVmHbaDvsPortId,
       "cucsVmHbaDvsSwitchId": cucsVmHbaDvsSwitchId,
       "cucsVmHbaHostIfDn": cucsVmHbaHostIfDn,
       "cucsVmHbaName": cucsVmHbaName,
       "cucsVmHbaOwner": cucsVmHbaOwner,
       "cucsVmHbaPhSwitchId": cucsVmHbaPhSwitchId,
       "cucsVmHbaProfileId": cucsVmHbaProfileId,
       "cucsVmHbaProfileName": cucsVmHbaProfileName,
       "cucsVmHbaStatusChangeTs": cucsVmHbaStatusChangeTs,
       "cucsVmHbaSwitchId": cucsVmHbaSwitchId,
       "cucsVmHbaType": cucsVmHbaType,
       "cucsVmHbaUuid": cucsVmHbaUuid,
       "cucsVmHbaVStatus": cucsVmHbaVStatus,
       "cucsVmHbaVcDn": cucsVmHbaVcDn,
       "cucsVmHbaVifId": cucsVmHbaVifId,
       "cucsVmHbaVnicDn": cucsVmHbaVnicDn,
       "cucsVmHbaWwnn": cucsVmHbaWwnn,
       "cucsVmHbaWwpn": cucsVmHbaWwpn,
       "cucsVmHbaDvsGenPortId": cucsVmHbaDvsGenPortId,
       "cucsVmHbaVmndGuid": cucsVmHbaVmndGuid,
       "cucsVmHbaVmndName": cucsVmHbaVmndName,
       "cucsVmHvTable": cucsVmHvTable,
       "cucsVmHvEntry": cucsVmHvEntry,
       "cucsVmHvInstanceId": cucsVmHvInstanceId,
       "cucsVmHvDn": cucsVmHvDn,
       "cucsVmHvRn": cucsVmHvRn,
       "cucsVmHvDescr": cucsVmHvDescr,
       "cucsVmHvDvsDn": cucsVmHvDvsDn,
       "cucsVmHvDvsName": cucsVmHvDvsName,
       "cucsVmHvFltAggr": cucsVmHvFltAggr,
       "cucsVmHvIntId": cucsVmHvIntId,
       "cucsVmHvLsDn": cucsVmHvLsDn,
       "cucsVmHvName": cucsVmHvName,
       "cucsVmHvPnDn": cucsVmHvPnDn,
       "cucsVmHvStatusChangeTs": cucsVmHvStatusChangeTs,
       "cucsVmHvUuid": cucsVmHvUuid,
       "cucsVmHvVStatus": cucsVmHvVStatus,
       "cucsVmHvClInstType": cucsVmHvClInstType,
       "cucsVmHvHvType": cucsVmHvHvType,
       "cucsVmHvModel": cucsVmHvModel,
       "cucsVmHvVendor": cucsVmHvVendor,
       "cucsVmHvPolicyLevel": cucsVmHvPolicyLevel,
       "cucsVmHvPolicyOwner": cucsVmHvPolicyOwner,
       "cucsVmInstanceTable": cucsVmInstanceTable,
       "cucsVmInstanceEntry": cucsVmInstanceEntry,
       "cucsVmInstanceInstanceId": cucsVmInstanceInstanceId,
       "cucsVmInstanceDn": cucsVmInstanceDn,
       "cucsVmInstanceRn": cucsVmInstanceRn,
       "cucsVmInstanceDescr": cucsVmInstanceDescr,
       "cucsVmInstanceDvsDn": cucsVmInstanceDvsDn,
       "cucsVmInstanceDvsName": cucsVmInstanceDvsName,
       "cucsVmInstanceFltAggr": cucsVmInstanceFltAggr,
       "cucsVmInstanceHvDn": cucsVmInstanceHvDn,
       "cucsVmInstanceHvUuid": cucsVmInstanceHvUuid,
       "cucsVmInstanceIntId": cucsVmInstanceIntId,
       "cucsVmInstanceLsDn": cucsVmInstanceLsDn,
       "cucsVmInstanceName": cucsVmInstanceName,
       "cucsVmInstancePnDn": cucsVmInstancePnDn,
       "cucsVmInstanceStatusChangeTs": cucsVmInstanceStatusChangeTs,
       "cucsVmInstanceUuid": cucsVmInstanceUuid,
       "cucsVmInstanceVStatus": cucsVmInstanceVStatus,
       "cucsVmInstanceClInstType": cucsVmInstanceClInstType,
       "cucsVmInstanceHvType": cucsVmInstanceHvType,
       "cucsVmInstanceModel": cucsVmInstanceModel,
       "cucsVmInstanceVendor": cucsVmInstanceVendor,
       "cucsVmInstancePolicyLevel": cucsVmInstancePolicyLevel,
       "cucsVmInstancePolicyOwner": cucsVmInstancePolicyOwner,
       "cucsVmLifeCyclePolicyTable": cucsVmLifeCyclePolicyTable,
       "cucsVmLifeCyclePolicyEntry": cucsVmLifeCyclePolicyEntry,
       "cucsVmLifeCyclePolicyInstanceId": cucsVmLifeCyclePolicyInstanceId,
       "cucsVmLifeCyclePolicyDn": cucsVmLifeCyclePolicyDn,
       "cucsVmLifeCyclePolicyRn": cucsVmLifeCyclePolicyRn,
       "cucsVmLifeCyclePolicyDescr": cucsVmLifeCyclePolicyDescr,
       "cucsVmLifeCyclePolicyIntId": cucsVmLifeCyclePolicyIntId,
       "cucsVmLifeCyclePolicyName": cucsVmLifeCyclePolicyName,
       "cucsVmLifeCyclePolicyVmRetention": cucsVmLifeCyclePolicyVmRetention,
       "cucsVmLifeCyclePolicyVnicRetention": cucsVmLifeCyclePolicyVnicRetention,
       "cucsVmLifeCyclePolicyFsmDescr": cucsVmLifeCyclePolicyFsmDescr,
       "cucsVmLifeCyclePolicyFsmPrev": cucsVmLifeCyclePolicyFsmPrev,
       "cucsVmLifeCyclePolicyFsmProgr": cucsVmLifeCyclePolicyFsmProgr,
       "cucsVmLifeCyclePolicyFsmRmtInvErrCode": cucsVmLifeCyclePolicyFsmRmtInvErrCode,
       "cucsVmLifeCyclePolicyFsmRmtInvErrDescr": cucsVmLifeCyclePolicyFsmRmtInvErrDescr,
       "cucsVmLifeCyclePolicyFsmRmtInvRslt": cucsVmLifeCyclePolicyFsmRmtInvRslt,
       "cucsVmLifeCyclePolicyFsmStageDescr": cucsVmLifeCyclePolicyFsmStageDescr,
       "cucsVmLifeCyclePolicyFsmStamp": cucsVmLifeCyclePolicyFsmStamp,
       "cucsVmLifeCyclePolicyFsmStatus": cucsVmLifeCyclePolicyFsmStatus,
       "cucsVmLifeCyclePolicyFsmTry": cucsVmLifeCyclePolicyFsmTry,
       "cucsVmLifeCyclePolicyPolicyLevel": cucsVmLifeCyclePolicyPolicyLevel,
       "cucsVmLifeCyclePolicyPolicyOwner": cucsVmLifeCyclePolicyPolicyOwner,
       "cucsVmNicTable": cucsVmNicTable,
       "cucsVmNicEntry": cucsVmNicEntry,
       "cucsVmNicInstanceId": cucsVmNicInstanceId,
       "cucsVmNicDn": cucsVmNicDn,
       "cucsVmNicRn": cucsVmNicRn,
       "cucsVmNicDvsPortId": cucsVmNicDvsPortId,
       "cucsVmNicDvsSwitchId": cucsVmNicDvsSwitchId,
       "cucsVmNicHostIfDn": cucsVmNicHostIfDn,
       "cucsVmNicMacAddr": cucsVmNicMacAddr,
       "cucsVmNicName": cucsVmNicName,
       "cucsVmNicOwner": cucsVmNicOwner,
       "cucsVmNicPhSwitchId": cucsVmNicPhSwitchId,
       "cucsVmNicProfileId": cucsVmNicProfileId,
       "cucsVmNicProfileName": cucsVmNicProfileName,
       "cucsVmNicStatusChangeTs": cucsVmNicStatusChangeTs,
       "cucsVmNicSwitchId": cucsVmNicSwitchId,
       "cucsVmNicType": cucsVmNicType,
       "cucsVmNicUuid": cucsVmNicUuid,
       "cucsVmNicVStatus": cucsVmNicVStatus,
       "cucsVmNicVcDn": cucsVmNicVcDn,
       "cucsVmNicVifId": cucsVmNicVifId,
       "cucsVmNicVnicDn": cucsVmNicVnicDn,
       "cucsVmNicDvsGenPortId": cucsVmNicDvsGenPortId,
       "cucsVmNicVmndGuid": cucsVmNicVmndGuid,
       "cucsVmNicVmndName": cucsVmNicVmndName,
       "cucsVmOrgTable": cucsVmOrgTable,
       "cucsVmOrgEntry": cucsVmOrgEntry,
       "cucsVmOrgInstanceId": cucsVmOrgInstanceId,
       "cucsVmOrgDn": cucsVmOrgDn,
       "cucsVmOrgRn": cucsVmOrgRn,
       "cucsVmOrgDescr": cucsVmOrgDescr,
       "cucsVmOrgIntId": cucsVmOrgIntId,
       "cucsVmOrgName": cucsVmOrgName,
       "cucsVmOrgOwn": cucsVmOrgOwn,
       "cucsVmOrgUuid": cucsVmOrgUuid,
       "cucsVmOrgPolicyLevel": cucsVmOrgPolicyLevel,
       "cucsVmOrgPolicyOwner": cucsVmOrgPolicyOwner,
       "cucsVmSwitchTable": cucsVmSwitchTable,
       "cucsVmSwitchEntry": cucsVmSwitchEntry,
       "cucsVmSwitchInstanceId": cucsVmSwitchInstanceId,
       "cucsVmSwitchDn": cucsVmSwitchDn,
       "cucsVmSwitchRn": cucsVmSwitchRn,
       "cucsVmSwitchAdminState": cucsVmSwitchAdminState,
       "cucsVmSwitchDescr": cucsVmSwitchDescr,
       "cucsVmSwitchExtKey": cucsVmSwitchExtKey,
       "cucsVmSwitchIntId": cucsVmSwitchIntId,
       "cucsVmSwitchKeyInst": cucsVmSwitchKeyInst,
       "cucsVmSwitchName": cucsVmSwitchName,
       "cucsVmSwitchOwn": cucsVmSwitchOwn,
       "cucsVmSwitchUuid": cucsVmSwitchUuid,
       "cucsVmSwitchId": cucsVmSwitchId,
       "cucsVmSwitchManager": cucsVmSwitchManager,
       "cucsVmSwitchPolicyLevel": cucsVmSwitchPolicyLevel,
       "cucsVmSwitchPolicyOwner": cucsVmSwitchPolicyOwner,
       "cucsVmSwitchFltAggr": cucsVmSwitchFltAggr,
       "cucsVmSwitchVendor": cucsVmSwitchVendor,
       "cucsVmVifTable": cucsVmVifTable,
       "cucsVmVifEntry": cucsVmVifEntry,
       "cucsVmVifInstanceId": cucsVmVifInstanceId,
       "cucsVmVifDn": cucsVmVifDn,
       "cucsVmVifRn": cucsVmVifRn,
       "cucsVmVifCookie": cucsVmVifCookie,
       "cucsVmVifPhSwitchId": cucsVmVifPhSwitchId,
       "cucsVmVifPhsAccessCardId": cucsVmVifPhsAccessCardId,
       "cucsVmVifPhsAccessPortId": cucsVmVifPhsAccessPortId,
       "cucsVmVifPhsBorderCardId": cucsVmVifPhsBorderCardId,
       "cucsVmVifPhsBorderPortId": cucsVmVifPhsBorderPortId,
       "cucsVmVifStatusChangeTs": cucsVmVifStatusChangeTs,
       "cucsVmVifVStatus": cucsVmVifVStatus,
       "cucsVmVifVcDn": cucsVmVifVcDn,
       "cucsVmVifVifId": cucsVmVifVifId,
       "cucsVmVifAdpVifId": cucsVmVifAdpVifId,
       "cucsVmVifLinkState": cucsVmVifLinkState,
       "cucsVmVifOperState": cucsVmVifOperState,
       "cucsVmVifStateQual": cucsVmVifStateQual,
       "cucsVmVifPhsAccessAggrPortId": cucsVmVifPhsAccessAggrPortId,
       "cucsVmVifPhsBorderAggrPortId": cucsVmVifPhsBorderAggrPortId,
       "cucsVmVlanTable": cucsVmVlanTable,
       "cucsVmVlanEntry": cucsVmVlanEntry,
       "cucsVmVlanInstanceId": cucsVmVlanInstanceId,
       "cucsVmVlanDn": cucsVmVlanDn,
       "cucsVmVlanRn": cucsVmVlanRn,
       "cucsVmVlanEpDn": cucsVmVlanEpDn,
       "cucsVmVlanId": cucsVmVlanId,
       "cucsVmVlanIfRole": cucsVmVlanIfRole,
       "cucsVmVlanIfType": cucsVmVlanIfType,
       "cucsVmVlanLocale": cucsVmVlanLocale,
       "cucsVmVlanName": cucsVmVlanName,
       "cucsVmVlanPeerDn": cucsVmVlanPeerDn,
       "cucsVmVlanPubNwDn": cucsVmVlanPubNwDn,
       "cucsVmVlanPubNwId": cucsVmVlanPubNwId,
       "cucsVmVlanPubNwName": cucsVmVlanPubNwName,
       "cucsVmVlanSharing": cucsVmVlanSharing,
       "cucsVmVlanSwitchId": cucsVmVlanSwitchId,
       "cucsVmVlanTransport": cucsVmVlanTransport,
       "cucsVmVlanType": cucsVmVlanType,
       "cucsVmVlanOperState": cucsVmVlanOperState,
       "cucsVmVlanPolicyOwner": cucsVmVlanPolicyOwner,
       "cucsVmVlanAssocPrimaryVlanState": cucsVmVlanAssocPrimaryVlanState,
       "cucsVmVlanAssocPrimaryVlanSwitchId": cucsVmVlanAssocPrimaryVlanSwitchId,
       "cucsVmVlanOverlapStateForA": cucsVmVlanOverlapStateForA,
       "cucsVmVlanOverlapStateForB": cucsVmVlanOverlapStateForB,
       "cucsVmVnicProfClTable": cucsVmVnicProfClTable,
       "cucsVmVnicProfClEntry": cucsVmVnicProfClEntry,
       "cucsVmVnicProfClInstanceId": cucsVmVnicProfClInstanceId,
       "cucsVmVnicProfClDn": cucsVmVnicProfClDn,
       "cucsVmVnicProfClRn": cucsVmVnicProfClRn,
       "cucsVmVnicProfClDcName": cucsVmVnicProfClDcName,
       "cucsVmVnicProfClDescr": cucsVmVnicProfClDescr,
       "cucsVmVnicProfClIntId": cucsVmVnicProfClIntId,
       "cucsVmVnicProfClName": cucsVmVnicProfClName,
       "cucsVmVnicProfClOrgPath": cucsVmVnicProfClOrgPath,
       "cucsVmVnicProfClSwName": cucsVmVnicProfClSwName,
       "cucsVmVnicProfClPolicyLevel": cucsVmVnicProfClPolicyLevel,
       "cucsVmVnicProfClPolicyOwner": cucsVmVnicProfClPolicyOwner,
       "cucsVmVnicProfInstTable": cucsVmVnicProfInstTable,
       "cucsVmVnicProfInstEntry": cucsVmVnicProfInstEntry,
       "cucsVmVnicProfInstInstanceId": cucsVmVnicProfInstInstanceId,
       "cucsVmVnicProfInstDn": cucsVmVnicProfInstDn,
       "cucsVmVnicProfInstRn": cucsVmVnicProfInstRn,
       "cucsVmVnicProfInstDescr": cucsVmVnicProfInstDescr,
       "cucsVmVnicProfInstIntId": cucsVmVnicProfInstIntId,
       "cucsVmVnicProfInstMaxPorts": cucsVmVnicProfInstMaxPorts,
       "cucsVmVnicProfInstName": cucsVmVnicProfInstName,
       "cucsVmVnicProfInstProfDn": cucsVmVnicProfInstProfDn,
       "cucsVmVnicProfInstPolicyLevel": cucsVmVnicProfInstPolicyLevel,
       "cucsVmVnicProfInstPolicyOwner": cucsVmVnicProfInstPolicyOwner,
       "cucsVmVnicProfInstProfileType": cucsVmVnicProfInstProfileType,
       "cucsVmVsanTable": cucsVmVsanTable,
       "cucsVmVsanEntry": cucsVmVsanEntry,
       "cucsVmVsanInstanceId": cucsVmVsanInstanceId,
       "cucsVmVsanDn": cucsVmVsanDn,
       "cucsVmVsanRn": cucsVmVsanRn,
       "cucsVmVsanEpDn": cucsVmVsanEpDn,
       "cucsVmVsanFcoeVlan": cucsVmVsanFcoeVlan,
       "cucsVmVsanId": cucsVmVsanId,
       "cucsVmVsanIfRole": cucsVmVsanIfRole,
       "cucsVmVsanIfType": cucsVmVsanIfType,
       "cucsVmVsanLocale": cucsVmVsanLocale,
       "cucsVmVsanName": cucsVmVsanName,
       "cucsVmVsanPeerDn": cucsVmVsanPeerDn,
       "cucsVmVsanSwitchId": cucsVmVsanSwitchId,
       "cucsVmVsanTransport": cucsVmVsanTransport,
       "cucsVmVsanType": cucsVmVsanType,
       "cucsVmVsanOperState": cucsVmVsanOperState,
       "cucsVmVsanZoningState": cucsVmVsanZoningState,
       "cucsVmVsanPolicyOwner": cucsVmVsanPolicyOwner,
       "cucsVmComputeEpTable": cucsVmComputeEpTable,
       "cucsVmComputeEpEntry": cucsVmComputeEpEntry,
       "cucsVmComputeEpInstanceId": cucsVmComputeEpInstanceId,
       "cucsVmComputeEpDn": cucsVmComputeEpDn,
       "cucsVmComputeEpRn": cucsVmComputeEpRn,
       "cucsVmComputeEpClInstType": cucsVmComputeEpClInstType,
       "cucsVmComputeEpComputeEpVendor": cucsVmComputeEpComputeEpVendor,
       "cucsVmComputeEpDescr": cucsVmComputeEpDescr,
       "cucsVmComputeEpDvsDn": cucsVmComputeEpDvsDn,
       "cucsVmComputeEpDvsName": cucsVmComputeEpDvsName,
       "cucsVmComputeEpHostName": cucsVmComputeEpHostName,
       "cucsVmComputeEpIntId": cucsVmComputeEpIntId,
       "cucsVmComputeEpLsDn": cucsVmComputeEpLsDn,
       "cucsVmComputeEpModel": cucsVmComputeEpModel,
       "cucsVmComputeEpName": cucsVmComputeEpName,
       "cucsVmComputeEpPnDn": cucsVmComputeEpPnDn,
       "cucsVmComputeEpStatusChangeTs": cucsVmComputeEpStatusChangeTs,
       "cucsVmComputeEpUuid": cucsVmComputeEpUuid,
       "cucsVmComputeEpVStatus": cucsVmComputeEpVStatus,
       "cucsVmComputeEpVendor": cucsVmComputeEpVendor,
       "cucsVmComputeEpPolicyLevel": cucsVmComputeEpPolicyLevel,
       "cucsVmComputeEpPolicyOwner": cucsVmComputeEpPolicyOwner,
       "cucsVmLifeCyclePolicyFsmTaskTable": cucsVmLifeCyclePolicyFsmTaskTable,
       "cucsVmLifeCyclePolicyFsmTaskEntry": cucsVmLifeCyclePolicyFsmTaskEntry,
       "cucsVmLifeCyclePolicyFsmTaskInstanceId": cucsVmLifeCyclePolicyFsmTaskInstanceId,
       "cucsVmLifeCyclePolicyFsmTaskDn": cucsVmLifeCyclePolicyFsmTaskDn,
       "cucsVmLifeCyclePolicyFsmTaskRn": cucsVmLifeCyclePolicyFsmTaskRn,
       "cucsVmLifeCyclePolicyFsmTaskCompletion": cucsVmLifeCyclePolicyFsmTaskCompletion,
       "cucsVmLifeCyclePolicyFsmTaskFlags": cucsVmLifeCyclePolicyFsmTaskFlags,
       "cucsVmLifeCyclePolicyFsmTaskItem": cucsVmLifeCyclePolicyFsmTaskItem,
       "cucsVmLifeCyclePolicyFsmTaskSeqId": cucsVmLifeCyclePolicyFsmTaskSeqId,
       "cucsVmLifeCyclePolicyFsmTable": cucsVmLifeCyclePolicyFsmTable,
       "cucsVmLifeCyclePolicyFsmEntry": cucsVmLifeCyclePolicyFsmEntry,
       "cucsVmLifeCyclePolicyFsmInstanceId": cucsVmLifeCyclePolicyFsmInstanceId,
       "cucsVmLifeCyclePolicyFsmDn": cucsVmLifeCyclePolicyFsmDn,
       "cucsVmLifeCyclePolicyFsmRn": cucsVmLifeCyclePolicyFsmRn,
       "cucsVmLifeCyclePolicyFsmCompletionTime": cucsVmLifeCyclePolicyFsmCompletionTime,
       "cucsVmLifeCyclePolicyFsmCurrentFsm": cucsVmLifeCyclePolicyFsmCurrentFsm,
       "cucsVmLifeCyclePolicyFsmDescrData": cucsVmLifeCyclePolicyFsmDescrData,
       "cucsVmLifeCyclePolicyFsmFsmStatus": cucsVmLifeCyclePolicyFsmFsmStatus,
       "cucsVmLifeCyclePolicyFsmProgress": cucsVmLifeCyclePolicyFsmProgress,
       "cucsVmLifeCyclePolicyFsmRmtErrCode": cucsVmLifeCyclePolicyFsmRmtErrCode,
       "cucsVmLifeCyclePolicyFsmRmtErrDescr": cucsVmLifeCyclePolicyFsmRmtErrDescr,
       "cucsVmLifeCyclePolicyFsmRmtRslt": cucsVmLifeCyclePolicyFsmRmtRslt,
       "cucsVmLifeCyclePolicyFsmStageTable": cucsVmLifeCyclePolicyFsmStageTable,
       "cucsVmLifeCyclePolicyFsmStageEntry": cucsVmLifeCyclePolicyFsmStageEntry,
       "cucsVmLifeCyclePolicyFsmStageInstanceId": cucsVmLifeCyclePolicyFsmStageInstanceId,
       "cucsVmLifeCyclePolicyFsmStageDn": cucsVmLifeCyclePolicyFsmStageDn,
       "cucsVmLifeCyclePolicyFsmStageRn": cucsVmLifeCyclePolicyFsmStageRn,
       "cucsVmLifeCyclePolicyFsmStageDescrData": cucsVmLifeCyclePolicyFsmStageDescrData,
       "cucsVmLifeCyclePolicyFsmStageLastUpdateTime": cucsVmLifeCyclePolicyFsmStageLastUpdateTime,
       "cucsVmLifeCyclePolicyFsmStageName": cucsVmLifeCyclePolicyFsmStageName,
       "cucsVmLifeCyclePolicyFsmStageOrder": cucsVmLifeCyclePolicyFsmStageOrder,
       "cucsVmLifeCyclePolicyFsmStageRetry": cucsVmLifeCyclePolicyFsmStageRetry,
       "cucsVmLifeCyclePolicyFsmStageStageStatus": cucsVmLifeCyclePolicyFsmStageStageStatus}
)
