# SNMP MIB module (CISCO-UNIFIED-COMPUTING-VNIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-VNIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:31 2024
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

(CucsAdaptorPurpose,
 CucsConditionRemoteInvRslt,
 CucsDpsecForgedTransmit,
 CucsFabricHostPortId,
 CucsFabricVlanSharingType,
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus,
 CucsLsConfigState,
 CucsLsOwner,
 CucsNetworkSwitchId,
 CucsNwctrlAdminState,
 CucsNwctrlLinkFailAction,
 CucsNwctrlLldpAdminStateBitmask,
 CucsNwctrlRegistrationMode,
 CucsPolicyPolicyOwner,
 CucsVmMgmtPlane,
 CucsVnicAEtherIfType,
 CucsVnicAFcIfSwitchId,
 CucsVnicAFcIfType,
 CucsVnicAIpcIfType,
 CucsVnicAScsiIfType,
 CucsVnicCdnSource,
 CucsVnicConfigIssues,
 CucsVnicConnectionOwner,
 CucsVnicConnectionType,
 CucsVnicDefBehType,
 CucsVnicDefaultAction,
 CucsVnicDynamicConReqProtection,
 CucsVnicEtherBaseIfSwitchId,
 CucsVnicEtherBaseSwitchId,
 CucsVnicEtherType,
 CucsVnicExternalMgmtIPMode,
 CucsVnicFcBasePersBind,
 CucsVnicFcBaseType,
 CucsVnicFcNodeOwner,
 CucsVnicHostNwIOPerfPref,
 CucsVnicIPv4DnsPref,
 CucsVnicIScsiIfDefType,
 CucsVnicIScsiNodeOwner,
 CucsVnicIfOperState,
 CucsVnicInstantiation,
 CucsVnicIpPoolType,
 CucsVnicIpcType,
 CucsVnicLanConnTemplSwitchId,
 CucsVnicLunId,
 CucsVnicPortProfileType,
 CucsVnicProfileConfigQualifier,
 CucsVnicProfileSetFsmCurrentFsm,
 CucsVnicProfileSetFsmStageName,
 CucsVnicProfileSetFsmTaskItem,
 CucsVnicSanConnTemplTarget,
 CucsVnicScsiType,
 CucsVnicTemplateTarget,
 CucsVnicTemplateType,
 CucsVnicVhbaBehPolicyType,
 CucsVnicVirtualizationPreferenceType,
 CucsVnicVlanGroupUpdate,
 CucsVnicVnicBehPolicyType,
 CucsVnicVnicBootDev,
 CucsVnicVnicOperHostPort) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsAdaptorPurpose",
    "CucsConditionRemoteInvRslt",
    "CucsDpsecForgedTransmit",
    "CucsFabricHostPortId",
    "CucsFabricVlanSharingType",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsLsConfigState",
    "CucsLsOwner",
    "CucsNetworkSwitchId",
    "CucsNwctrlAdminState",
    "CucsNwctrlLinkFailAction",
    "CucsNwctrlLldpAdminStateBitmask",
    "CucsNwctrlRegistrationMode",
    "CucsPolicyPolicyOwner",
    "CucsVmMgmtPlane",
    "CucsVnicAEtherIfType",
    "CucsVnicAFcIfSwitchId",
    "CucsVnicAFcIfType",
    "CucsVnicAIpcIfType",
    "CucsVnicAScsiIfType",
    "CucsVnicCdnSource",
    "CucsVnicConfigIssues",
    "CucsVnicConnectionOwner",
    "CucsVnicConnectionType",
    "CucsVnicDefBehType",
    "CucsVnicDefaultAction",
    "CucsVnicDynamicConReqProtection",
    "CucsVnicEtherBaseIfSwitchId",
    "CucsVnicEtherBaseSwitchId",
    "CucsVnicEtherType",
    "CucsVnicExternalMgmtIPMode",
    "CucsVnicFcBasePersBind",
    "CucsVnicFcBaseType",
    "CucsVnicFcNodeOwner",
    "CucsVnicHostNwIOPerfPref",
    "CucsVnicIPv4DnsPref",
    "CucsVnicIScsiIfDefType",
    "CucsVnicIScsiNodeOwner",
    "CucsVnicIfOperState",
    "CucsVnicInstantiation",
    "CucsVnicIpPoolType",
    "CucsVnicIpcType",
    "CucsVnicLanConnTemplSwitchId",
    "CucsVnicLunId",
    "CucsVnicPortProfileType",
    "CucsVnicProfileConfigQualifier",
    "CucsVnicProfileSetFsmCurrentFsm",
    "CucsVnicProfileSetFsmStageName",
    "CucsVnicProfileSetFsmTaskItem",
    "CucsVnicSanConnTemplTarget",
    "CucsVnicScsiType",
    "CucsVnicTemplateTarget",
    "CucsVnicTemplateType",
    "CucsVnicVhbaBehPolicyType",
    "CucsVnicVirtualizationPreferenceType",
    "CucsVnicVlanGroupUpdate",
    "CucsVnicVnicBehPolicyType",
    "CucsVnicVnicBootDev",
    "CucsVnicVnicOperHostPort")

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

cucsVnicObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsVnicBootTargetTable_Object = MibTable
cucsVnicBootTargetTable = _CucsVnicBootTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 1)
)
if mibBuilder.loadTexts:
    cucsVnicBootTargetTable.setStatus("current")
_CucsVnicBootTargetEntry_Object = MibTableRow
cucsVnicBootTargetEntry = _CucsVnicBootTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 1, 1)
)
cucsVnicBootTargetEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicBootTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicBootTargetEntry.setStatus("current")
_CucsVnicBootTargetInstanceId_Type = CucsManagedObjectId
_CucsVnicBootTargetInstanceId_Object = MibTableColumn
cucsVnicBootTargetInstanceId = _CucsVnicBootTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 1, 1, 1),
    _CucsVnicBootTargetInstanceId_Type()
)
cucsVnicBootTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicBootTargetInstanceId.setStatus("current")
_CucsVnicBootTargetDn_Type = CucsManagedObjectDn
_CucsVnicBootTargetDn_Object = MibTableColumn
cucsVnicBootTargetDn = _CucsVnicBootTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 1, 1, 2),
    _CucsVnicBootTargetDn_Type()
)
cucsVnicBootTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicBootTargetDn.setStatus("current")
_CucsVnicBootTargetRn_Type = SnmpAdminString
_CucsVnicBootTargetRn_Object = MibTableColumn
cucsVnicBootTargetRn = _CucsVnicBootTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 1, 1, 3),
    _CucsVnicBootTargetRn_Type()
)
cucsVnicBootTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicBootTargetRn.setStatus("current")
_CucsVnicBootTargetLun_Type = SnmpAdminString
_CucsVnicBootTargetLun_Object = MibTableColumn
cucsVnicBootTargetLun = _CucsVnicBootTargetLun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 1, 1, 4),
    _CucsVnicBootTargetLun_Type()
)
cucsVnicBootTargetLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicBootTargetLun.setStatus("current")
_CucsVnicBootTargetWwn_Type = Unsigned64
_CucsVnicBootTargetWwn_Object = MibTableColumn
cucsVnicBootTargetWwn = _CucsVnicBootTargetWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 1, 1, 5),
    _CucsVnicBootTargetWwn_Type()
)
cucsVnicBootTargetWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicBootTargetWwn.setStatus("current")
_CucsVnicDefBehTable_Object = MibTable
cucsVnicDefBehTable = _CucsVnicDefBehTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 2)
)
if mibBuilder.loadTexts:
    cucsVnicDefBehTable.setStatus("current")
_CucsVnicDefBehEntry_Object = MibTableRow
cucsVnicDefBehEntry = _CucsVnicDefBehEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 2, 1)
)
cucsVnicDefBehEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicDefBehInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicDefBehEntry.setStatus("current")
_CucsVnicDefBehInstanceId_Type = CucsManagedObjectId
_CucsVnicDefBehInstanceId_Object = MibTableColumn
cucsVnicDefBehInstanceId = _CucsVnicDefBehInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 2, 1, 1),
    _CucsVnicDefBehInstanceId_Type()
)
cucsVnicDefBehInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicDefBehInstanceId.setStatus("current")
_CucsVnicDefBehDn_Type = CucsManagedObjectDn
_CucsVnicDefBehDn_Object = MibTableColumn
cucsVnicDefBehDn = _CucsVnicDefBehDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 2, 1, 2),
    _CucsVnicDefBehDn_Type()
)
cucsVnicDefBehDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDefBehDn.setStatus("current")
_CucsVnicDefBehRn_Type = SnmpAdminString
_CucsVnicDefBehRn_Object = MibTableColumn
cucsVnicDefBehRn = _CucsVnicDefBehRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 2, 1, 3),
    _CucsVnicDefBehRn_Type()
)
cucsVnicDefBehRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDefBehRn.setStatus("current")
_CucsVnicDefBehAction_Type = CucsVnicDefaultAction
_CucsVnicDefBehAction_Object = MibTableColumn
cucsVnicDefBehAction = _CucsVnicDefBehAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 2, 1, 4),
    _CucsVnicDefBehAction_Type()
)
cucsVnicDefBehAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDefBehAction.setStatus("current")
_CucsVnicDefBehNwTemplName_Type = SnmpAdminString
_CucsVnicDefBehNwTemplName_Object = MibTableColumn
cucsVnicDefBehNwTemplName = _CucsVnicDefBehNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 2, 1, 5),
    _CucsVnicDefBehNwTemplName_Type()
)
cucsVnicDefBehNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDefBehNwTemplName.setStatus("current")
_CucsVnicDefBehType_Type = CucsVnicDefBehType
_CucsVnicDefBehType_Object = MibTableColumn
cucsVnicDefBehType = _CucsVnicDefBehType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 2, 1, 6),
    _CucsVnicDefBehType_Type()
)
cucsVnicDefBehType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDefBehType.setStatus("current")
_CucsVnicDefBehDescr_Type = SnmpAdminString
_CucsVnicDefBehDescr_Object = MibTableColumn
cucsVnicDefBehDescr = _CucsVnicDefBehDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 2, 1, 7),
    _CucsVnicDefBehDescr_Type()
)
cucsVnicDefBehDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDefBehDescr.setStatus("current")
_CucsVnicDefBehIntId_Type = SnmpAdminString
_CucsVnicDefBehIntId_Object = MibTableColumn
cucsVnicDefBehIntId = _CucsVnicDefBehIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 2, 1, 8),
    _CucsVnicDefBehIntId_Type()
)
cucsVnicDefBehIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDefBehIntId.setStatus("current")
_CucsVnicDefBehName_Type = SnmpAdminString
_CucsVnicDefBehName_Object = MibTableColumn
cucsVnicDefBehName = _CucsVnicDefBehName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 2, 1, 9),
    _CucsVnicDefBehName_Type()
)
cucsVnicDefBehName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDefBehName.setStatus("current")
_CucsVnicDefBehPolicyLevel_Type = Gauge32
_CucsVnicDefBehPolicyLevel_Object = MibTableColumn
cucsVnicDefBehPolicyLevel = _CucsVnicDefBehPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 2, 1, 10),
    _CucsVnicDefBehPolicyLevel_Type()
)
cucsVnicDefBehPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDefBehPolicyLevel.setStatus("current")
_CucsVnicDefBehPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicDefBehPolicyOwner_Object = MibTableColumn
cucsVnicDefBehPolicyOwner = _CucsVnicDefBehPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 2, 1, 11),
    _CucsVnicDefBehPolicyOwner_Type()
)
cucsVnicDefBehPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDefBehPolicyOwner.setStatus("current")
_CucsVnicDynamicConTable_Object = MibTable
cucsVnicDynamicConTable = _CucsVnicDynamicConTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 3)
)
if mibBuilder.loadTexts:
    cucsVnicDynamicConTable.setStatus("current")
_CucsVnicDynamicConEntry_Object = MibTableRow
cucsVnicDynamicConEntry = _CucsVnicDynamicConEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 3, 1)
)
cucsVnicDynamicConEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicDynamicConInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicDynamicConEntry.setStatus("current")
_CucsVnicDynamicConInstanceId_Type = CucsManagedObjectId
_CucsVnicDynamicConInstanceId_Object = MibTableColumn
cucsVnicDynamicConInstanceId = _CucsVnicDynamicConInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 3, 1, 1),
    _CucsVnicDynamicConInstanceId_Type()
)
cucsVnicDynamicConInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicDynamicConInstanceId.setStatus("current")
_CucsVnicDynamicConDn_Type = CucsManagedObjectDn
_CucsVnicDynamicConDn_Object = MibTableColumn
cucsVnicDynamicConDn = _CucsVnicDynamicConDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 3, 1, 2),
    _CucsVnicDynamicConDn_Type()
)
cucsVnicDynamicConDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConDn.setStatus("current")
_CucsVnicDynamicConRn_Type = SnmpAdminString
_CucsVnicDynamicConRn_Object = MibTableColumn
cucsVnicDynamicConRn = _CucsVnicDynamicConRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 3, 1, 3),
    _CucsVnicDynamicConRn_Type()
)
cucsVnicDynamicConRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConRn.setStatus("current")
_CucsVnicDynamicConAdaptorProfileName_Type = SnmpAdminString
_CucsVnicDynamicConAdaptorProfileName_Object = MibTableColumn
cucsVnicDynamicConAdaptorProfileName = _CucsVnicDynamicConAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 3, 1, 4),
    _CucsVnicDynamicConAdaptorProfileName_Type()
)
cucsVnicDynamicConAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConAdaptorProfileName.setStatus("current")
_CucsVnicDynamicConDescr_Type = SnmpAdminString
_CucsVnicDynamicConDescr_Object = MibTableColumn
cucsVnicDynamicConDescr = _CucsVnicDynamicConDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 3, 1, 5),
    _CucsVnicDynamicConDescr_Type()
)
cucsVnicDynamicConDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConDescr.setStatus("current")
_CucsVnicDynamicConDynamicEth_Type = Gauge32
_CucsVnicDynamicConDynamicEth_Object = MibTableColumn
cucsVnicDynamicConDynamicEth = _CucsVnicDynamicConDynamicEth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 3, 1, 6),
    _CucsVnicDynamicConDynamicEth_Type()
)
cucsVnicDynamicConDynamicEth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConDynamicEth.setStatus("current")
_CucsVnicDynamicConIntId_Type = SnmpAdminString
_CucsVnicDynamicConIntId_Object = MibTableColumn
cucsVnicDynamicConIntId = _CucsVnicDynamicConIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 3, 1, 7),
    _CucsVnicDynamicConIntId_Type()
)
cucsVnicDynamicConIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConIntId.setStatus("current")
_CucsVnicDynamicConMtu_Type = Gauge32
_CucsVnicDynamicConMtu_Object = MibTableColumn
cucsVnicDynamicConMtu = _CucsVnicDynamicConMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 3, 1, 8),
    _CucsVnicDynamicConMtu_Type()
)
cucsVnicDynamicConMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConMtu.setStatus("current")
_CucsVnicDynamicConName_Type = SnmpAdminString
_CucsVnicDynamicConName_Object = MibTableColumn
cucsVnicDynamicConName = _CucsVnicDynamicConName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 3, 1, 9),
    _CucsVnicDynamicConName_Type()
)
cucsVnicDynamicConName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConName.setStatus("current")
_CucsVnicDynamicConNamingPrefix_Type = SnmpAdminString
_CucsVnicDynamicConNamingPrefix_Object = MibTableColumn
cucsVnicDynamicConNamingPrefix = _CucsVnicDynamicConNamingPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 3, 1, 10),
    _CucsVnicDynamicConNamingPrefix_Type()
)
cucsVnicDynamicConNamingPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConNamingPrefix.setStatus("current")
_CucsVnicDynamicConProtection_Type = CucsVnicDynamicConReqProtection
_CucsVnicDynamicConProtection_Object = MibTableColumn
cucsVnicDynamicConProtection = _CucsVnicDynamicConProtection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 3, 1, 11),
    _CucsVnicDynamicConProtection_Type()
)
cucsVnicDynamicConProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConProtection.setStatus("current")
_CucsVnicDynamicConPolicyLevel_Type = Gauge32
_CucsVnicDynamicConPolicyLevel_Object = MibTableColumn
cucsVnicDynamicConPolicyLevel = _CucsVnicDynamicConPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 3, 1, 12),
    _CucsVnicDynamicConPolicyLevel_Type()
)
cucsVnicDynamicConPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyLevel.setStatus("current")
_CucsVnicDynamicConPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicDynamicConPolicyOwner_Object = MibTableColumn
cucsVnicDynamicConPolicyOwner = _CucsVnicDynamicConPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 3, 1, 13),
    _CucsVnicDynamicConPolicyOwner_Type()
)
cucsVnicDynamicConPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyOwner.setStatus("current")
_CucsVnicDynamicConPolicyTable_Object = MibTable
cucsVnicDynamicConPolicyTable = _CucsVnicDynamicConPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 4)
)
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyTable.setStatus("current")
_CucsVnicDynamicConPolicyEntry_Object = MibTableRow
cucsVnicDynamicConPolicyEntry = _CucsVnicDynamicConPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 4, 1)
)
cucsVnicDynamicConPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicDynamicConPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyEntry.setStatus("current")
_CucsVnicDynamicConPolicyInstanceId_Type = CucsManagedObjectId
_CucsVnicDynamicConPolicyInstanceId_Object = MibTableColumn
cucsVnicDynamicConPolicyInstanceId = _CucsVnicDynamicConPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 4, 1, 1),
    _CucsVnicDynamicConPolicyInstanceId_Type()
)
cucsVnicDynamicConPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyInstanceId.setStatus("current")
_CucsVnicDynamicConPolicyDn_Type = CucsManagedObjectDn
_CucsVnicDynamicConPolicyDn_Object = MibTableColumn
cucsVnicDynamicConPolicyDn = _CucsVnicDynamicConPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 4, 1, 2),
    _CucsVnicDynamicConPolicyDn_Type()
)
cucsVnicDynamicConPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyDn.setStatus("current")
_CucsVnicDynamicConPolicyRn_Type = SnmpAdminString
_CucsVnicDynamicConPolicyRn_Object = MibTableColumn
cucsVnicDynamicConPolicyRn = _CucsVnicDynamicConPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 4, 1, 3),
    _CucsVnicDynamicConPolicyRn_Type()
)
cucsVnicDynamicConPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyRn.setStatus("current")
_CucsVnicDynamicConPolicyAdaptorProfileName_Type = SnmpAdminString
_CucsVnicDynamicConPolicyAdaptorProfileName_Object = MibTableColumn
cucsVnicDynamicConPolicyAdaptorProfileName = _CucsVnicDynamicConPolicyAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 4, 1, 4),
    _CucsVnicDynamicConPolicyAdaptorProfileName_Type()
)
cucsVnicDynamicConPolicyAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyAdaptorProfileName.setStatus("current")
_CucsVnicDynamicConPolicyDescr_Type = SnmpAdminString
_CucsVnicDynamicConPolicyDescr_Object = MibTableColumn
cucsVnicDynamicConPolicyDescr = _CucsVnicDynamicConPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 4, 1, 5),
    _CucsVnicDynamicConPolicyDescr_Type()
)
cucsVnicDynamicConPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyDescr.setStatus("current")
_CucsVnicDynamicConPolicyDynamicEth_Type = Gauge32
_CucsVnicDynamicConPolicyDynamicEth_Object = MibTableColumn
cucsVnicDynamicConPolicyDynamicEth = _CucsVnicDynamicConPolicyDynamicEth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 4, 1, 6),
    _CucsVnicDynamicConPolicyDynamicEth_Type()
)
cucsVnicDynamicConPolicyDynamicEth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyDynamicEth.setStatus("current")
_CucsVnicDynamicConPolicyIntId_Type = SnmpAdminString
_CucsVnicDynamicConPolicyIntId_Object = MibTableColumn
cucsVnicDynamicConPolicyIntId = _CucsVnicDynamicConPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 4, 1, 7),
    _CucsVnicDynamicConPolicyIntId_Type()
)
cucsVnicDynamicConPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyIntId.setStatus("current")
_CucsVnicDynamicConPolicyMtu_Type = Gauge32
_CucsVnicDynamicConPolicyMtu_Object = MibTableColumn
cucsVnicDynamicConPolicyMtu = _CucsVnicDynamicConPolicyMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 4, 1, 8),
    _CucsVnicDynamicConPolicyMtu_Type()
)
cucsVnicDynamicConPolicyMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyMtu.setStatus("current")
_CucsVnicDynamicConPolicyName_Type = SnmpAdminString
_CucsVnicDynamicConPolicyName_Object = MibTableColumn
cucsVnicDynamicConPolicyName = _CucsVnicDynamicConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 4, 1, 9),
    _CucsVnicDynamicConPolicyName_Type()
)
cucsVnicDynamicConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyName.setStatus("current")
_CucsVnicDynamicConPolicyNamingPrefix_Type = SnmpAdminString
_CucsVnicDynamicConPolicyNamingPrefix_Object = MibTableColumn
cucsVnicDynamicConPolicyNamingPrefix = _CucsVnicDynamicConPolicyNamingPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 4, 1, 10),
    _CucsVnicDynamicConPolicyNamingPrefix_Type()
)
cucsVnicDynamicConPolicyNamingPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyNamingPrefix.setStatus("current")
_CucsVnicDynamicConPolicyProtection_Type = CucsVnicDynamicConReqProtection
_CucsVnicDynamicConPolicyProtection_Object = MibTableColumn
cucsVnicDynamicConPolicyProtection = _CucsVnicDynamicConPolicyProtection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 4, 1, 11),
    _CucsVnicDynamicConPolicyProtection_Type()
)
cucsVnicDynamicConPolicyProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyProtection.setStatus("current")
_CucsVnicDynamicConPolicyPolicyLevel_Type = Gauge32
_CucsVnicDynamicConPolicyPolicyLevel_Object = MibTableColumn
cucsVnicDynamicConPolicyPolicyLevel = _CucsVnicDynamicConPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 4, 1, 12),
    _CucsVnicDynamicConPolicyPolicyLevel_Type()
)
cucsVnicDynamicConPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyPolicyLevel.setStatus("current")
_CucsVnicDynamicConPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicDynamicConPolicyPolicyOwner_Object = MibTableColumn
cucsVnicDynamicConPolicyPolicyOwner = _CucsVnicDynamicConPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 4, 1, 13),
    _CucsVnicDynamicConPolicyPolicyOwner_Type()
)
cucsVnicDynamicConPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyPolicyOwner.setStatus("current")
_CucsVnicDynamicIdUniverseTable_Object = MibTable
cucsVnicDynamicIdUniverseTable = _CucsVnicDynamicIdUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 5)
)
if mibBuilder.loadTexts:
    cucsVnicDynamicIdUniverseTable.setStatus("current")
_CucsVnicDynamicIdUniverseEntry_Object = MibTableRow
cucsVnicDynamicIdUniverseEntry = _CucsVnicDynamicIdUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 5, 1)
)
cucsVnicDynamicIdUniverseEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicDynamicIdUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicDynamicIdUniverseEntry.setStatus("current")
_CucsVnicDynamicIdUniverseInstanceId_Type = CucsManagedObjectId
_CucsVnicDynamicIdUniverseInstanceId_Object = MibTableColumn
cucsVnicDynamicIdUniverseInstanceId = _CucsVnicDynamicIdUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 5, 1, 1),
    _CucsVnicDynamicIdUniverseInstanceId_Type()
)
cucsVnicDynamicIdUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicDynamicIdUniverseInstanceId.setStatus("current")
_CucsVnicDynamicIdUniverseDn_Type = CucsManagedObjectDn
_CucsVnicDynamicIdUniverseDn_Object = MibTableColumn
cucsVnicDynamicIdUniverseDn = _CucsVnicDynamicIdUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 5, 1, 2),
    _CucsVnicDynamicIdUniverseDn_Type()
)
cucsVnicDynamicIdUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicIdUniverseDn.setStatus("current")
_CucsVnicDynamicIdUniverseRn_Type = SnmpAdminString
_CucsVnicDynamicIdUniverseRn_Object = MibTableColumn
cucsVnicDynamicIdUniverseRn = _CucsVnicDynamicIdUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 5, 1, 3),
    _CucsVnicDynamicIdUniverseRn_Type()
)
cucsVnicDynamicIdUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicIdUniverseRn.setStatus("current")
_CucsVnicDynamicIdUniverseDescr_Type = SnmpAdminString
_CucsVnicDynamicIdUniverseDescr_Object = MibTableColumn
cucsVnicDynamicIdUniverseDescr = _CucsVnicDynamicIdUniverseDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 5, 1, 4),
    _CucsVnicDynamicIdUniverseDescr_Type()
)
cucsVnicDynamicIdUniverseDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicIdUniverseDescr.setStatus("current")
_CucsVnicDynamicIdUniverseIntId_Type = SnmpAdminString
_CucsVnicDynamicIdUniverseIntId_Object = MibTableColumn
cucsVnicDynamicIdUniverseIntId = _CucsVnicDynamicIdUniverseIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 5, 1, 5),
    _CucsVnicDynamicIdUniverseIntId_Type()
)
cucsVnicDynamicIdUniverseIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicIdUniverseIntId.setStatus("current")
_CucsVnicDynamicIdUniverseName_Type = SnmpAdminString
_CucsVnicDynamicIdUniverseName_Object = MibTableColumn
cucsVnicDynamicIdUniverseName = _CucsVnicDynamicIdUniverseName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 5, 1, 6),
    _CucsVnicDynamicIdUniverseName_Type()
)
cucsVnicDynamicIdUniverseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicIdUniverseName.setStatus("current")
_CucsVnicDynamicIdUniversePolicyLevel_Type = Gauge32
_CucsVnicDynamicIdUniversePolicyLevel_Object = MibTableColumn
cucsVnicDynamicIdUniversePolicyLevel = _CucsVnicDynamicIdUniversePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 5, 1, 7),
    _CucsVnicDynamicIdUniversePolicyLevel_Type()
)
cucsVnicDynamicIdUniversePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicIdUniversePolicyLevel.setStatus("current")
_CucsVnicDynamicIdUniversePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicDynamicIdUniversePolicyOwner_Object = MibTableColumn
cucsVnicDynamicIdUniversePolicyOwner = _CucsVnicDynamicIdUniversePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 5, 1, 8),
    _CucsVnicDynamicIdUniversePolicyOwner_Type()
)
cucsVnicDynamicIdUniversePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicIdUniversePolicyOwner.setStatus("current")
_CucsVnicDynamicProviderTable_Object = MibTable
cucsVnicDynamicProviderTable = _CucsVnicDynamicProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 6)
)
if mibBuilder.loadTexts:
    cucsVnicDynamicProviderTable.setStatus("current")
_CucsVnicDynamicProviderEntry_Object = MibTableRow
cucsVnicDynamicProviderEntry = _CucsVnicDynamicProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 6, 1)
)
cucsVnicDynamicProviderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicDynamicProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicDynamicProviderEntry.setStatus("current")
_CucsVnicDynamicProviderInstanceId_Type = CucsManagedObjectId
_CucsVnicDynamicProviderInstanceId_Object = MibTableColumn
cucsVnicDynamicProviderInstanceId = _CucsVnicDynamicProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 6, 1, 1),
    _CucsVnicDynamicProviderInstanceId_Type()
)
cucsVnicDynamicProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicDynamicProviderInstanceId.setStatus("current")
_CucsVnicDynamicProviderDn_Type = CucsManagedObjectDn
_CucsVnicDynamicProviderDn_Object = MibTableColumn
cucsVnicDynamicProviderDn = _CucsVnicDynamicProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 6, 1, 2),
    _CucsVnicDynamicProviderDn_Type()
)
cucsVnicDynamicProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicProviderDn.setStatus("current")
_CucsVnicDynamicProviderRn_Type = SnmpAdminString
_CucsVnicDynamicProviderRn_Object = MibTableColumn
cucsVnicDynamicProviderRn = _CucsVnicDynamicProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 6, 1, 3),
    _CucsVnicDynamicProviderRn_Type()
)
cucsVnicDynamicProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicProviderRn.setStatus("current")
_CucsVnicDynamicProviderName_Type = SnmpAdminString
_CucsVnicDynamicProviderName_Object = MibTableColumn
cucsVnicDynamicProviderName = _CucsVnicDynamicProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 6, 1, 4),
    _CucsVnicDynamicProviderName_Type()
)
cucsVnicDynamicProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicProviderName.setStatus("current")
_CucsVnicDynamicProviderEpTable_Object = MibTable
cucsVnicDynamicProviderEpTable = _CucsVnicDynamicProviderEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 7)
)
if mibBuilder.loadTexts:
    cucsVnicDynamicProviderEpTable.setStatus("current")
_CucsVnicDynamicProviderEpEntry_Object = MibTableRow
cucsVnicDynamicProviderEpEntry = _CucsVnicDynamicProviderEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 7, 1)
)
cucsVnicDynamicProviderEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicDynamicProviderEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicDynamicProviderEpEntry.setStatus("current")
_CucsVnicDynamicProviderEpInstanceId_Type = CucsManagedObjectId
_CucsVnicDynamicProviderEpInstanceId_Object = MibTableColumn
cucsVnicDynamicProviderEpInstanceId = _CucsVnicDynamicProviderEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 7, 1, 1),
    _CucsVnicDynamicProviderEpInstanceId_Type()
)
cucsVnicDynamicProviderEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicDynamicProviderEpInstanceId.setStatus("current")
_CucsVnicDynamicProviderEpDn_Type = CucsManagedObjectDn
_CucsVnicDynamicProviderEpDn_Object = MibTableColumn
cucsVnicDynamicProviderEpDn = _CucsVnicDynamicProviderEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 7, 1, 2),
    _CucsVnicDynamicProviderEpDn_Type()
)
cucsVnicDynamicProviderEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicProviderEpDn.setStatus("current")
_CucsVnicDynamicProviderEpRn_Type = SnmpAdminString
_CucsVnicDynamicProviderEpRn_Object = MibTableColumn
cucsVnicDynamicProviderEpRn = _CucsVnicDynamicProviderEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 7, 1, 3),
    _CucsVnicDynamicProviderEpRn_Type()
)
cucsVnicDynamicProviderEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicProviderEpRn.setStatus("current")
_CucsVnicDynamicProviderEpChassisId_Type = Gauge32
_CucsVnicDynamicProviderEpChassisId_Object = MibTableColumn
cucsVnicDynamicProviderEpChassisId = _CucsVnicDynamicProviderEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 7, 1, 4),
    _CucsVnicDynamicProviderEpChassisId_Type()
)
cucsVnicDynamicProviderEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicProviderEpChassisId.setStatus("current")
_CucsVnicDynamicProviderEpPortId_Type = Gauge32
_CucsVnicDynamicProviderEpPortId_Object = MibTableColumn
cucsVnicDynamicProviderEpPortId = _CucsVnicDynamicProviderEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 7, 1, 5),
    _CucsVnicDynamicProviderEpPortId_Type()
)
cucsVnicDynamicProviderEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicProviderEpPortId.setStatus("current")
_CucsVnicDynamicProviderEpSlotId_Type = Gauge32
_CucsVnicDynamicProviderEpSlotId_Object = MibTableColumn
cucsVnicDynamicProviderEpSlotId = _CucsVnicDynamicProviderEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 7, 1, 6),
    _CucsVnicDynamicProviderEpSlotId_Type()
)
cucsVnicDynamicProviderEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicProviderEpSlotId.setStatus("current")
_CucsVnicDynamicProviderEpSwitchId_Type = CucsNetworkSwitchId
_CucsVnicDynamicProviderEpSwitchId_Object = MibTableColumn
cucsVnicDynamicProviderEpSwitchId = _CucsVnicDynamicProviderEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 7, 1, 7),
    _CucsVnicDynamicProviderEpSwitchId_Type()
)
cucsVnicDynamicProviderEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicProviderEpSwitchId.setStatus("current")
_CucsVnicEthLifTable_Object = MibTable
cucsVnicEthLifTable = _CucsVnicEthLifTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 8)
)
if mibBuilder.loadTexts:
    cucsVnicEthLifTable.setStatus("current")
_CucsVnicEthLifEntry_Object = MibTableRow
cucsVnicEthLifEntry = _CucsVnicEthLifEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 8, 1)
)
cucsVnicEthLifEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicEthLifInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicEthLifEntry.setStatus("current")
_CucsVnicEthLifInstanceId_Type = CucsManagedObjectId
_CucsVnicEthLifInstanceId_Object = MibTableColumn
cucsVnicEthLifInstanceId = _CucsVnicEthLifInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 8, 1, 1),
    _CucsVnicEthLifInstanceId_Type()
)
cucsVnicEthLifInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicEthLifInstanceId.setStatus("current")
_CucsVnicEthLifDn_Type = CucsManagedObjectDn
_CucsVnicEthLifDn_Object = MibTableColumn
cucsVnicEthLifDn = _CucsVnicEthLifDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 8, 1, 2),
    _CucsVnicEthLifDn_Type()
)
cucsVnicEthLifDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthLifDn.setStatus("current")
_CucsVnicEthLifRn_Type = SnmpAdminString
_CucsVnicEthLifRn_Object = MibTableColumn
cucsVnicEthLifRn = _CucsVnicEthLifRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 8, 1, 3),
    _CucsVnicEthLifRn_Type()
)
cucsVnicEthLifRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthLifRn.setStatus("current")
_CucsVnicEthLifAddr_Type = MacAddress
_CucsVnicEthLifAddr_Object = MibTableColumn
cucsVnicEthLifAddr = _CucsVnicEthLifAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 8, 1, 4),
    _CucsVnicEthLifAddr_Type()
)
cucsVnicEthLifAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthLifAddr.setStatus("current")
_CucsVnicEthLifName_Type = SnmpAdminString
_CucsVnicEthLifName_Object = MibTableColumn
cucsVnicEthLifName = _CucsVnicEthLifName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 8, 1, 5),
    _CucsVnicEthLifName_Type()
)
cucsVnicEthLifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthLifName.setStatus("current")
_CucsVnicEthLifNicDn_Type = SnmpAdminString
_CucsVnicEthLifNicDn_Object = MibTableColumn
cucsVnicEthLifNicDn = _CucsVnicEthLifNicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 8, 1, 6),
    _CucsVnicEthLifNicDn_Type()
)
cucsVnicEthLifNicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthLifNicDn.setStatus("current")
_CucsVnicEthLifOwner_Type = CucsVnicConnectionOwner
_CucsVnicEthLifOwner_Object = MibTableColumn
cucsVnicEthLifOwner = _CucsVnicEthLifOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 8, 1, 7),
    _CucsVnicEthLifOwner_Type()
)
cucsVnicEthLifOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthLifOwner.setStatus("current")
_CucsVnicEthLifSwitchId_Type = CucsNetworkSwitchId
_CucsVnicEthLifSwitchId_Object = MibTableColumn
cucsVnicEthLifSwitchId = _CucsVnicEthLifSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 8, 1, 8),
    _CucsVnicEthLifSwitchId_Type()
)
cucsVnicEthLifSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthLifSwitchId.setStatus("current")
_CucsVnicEthLifType_Type = CucsVnicConnectionType
_CucsVnicEthLifType_Object = MibTableColumn
cucsVnicEthLifType = _CucsVnicEthLifType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 8, 1, 9),
    _CucsVnicEthLifType_Type()
)
cucsVnicEthLifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthLifType.setStatus("current")
_CucsVnicEthLifVnicDn_Type = SnmpAdminString
_CucsVnicEthLifVnicDn_Object = MibTableColumn
cucsVnicEthLifVnicDn = _CucsVnicEthLifVnicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 8, 1, 10),
    _CucsVnicEthLifVnicDn_Type()
)
cucsVnicEthLifVnicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthLifVnicDn.setStatus("current")
_CucsVnicEtherTable_Object = MibTable
cucsVnicEtherTable = _CucsVnicEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9)
)
if mibBuilder.loadTexts:
    cucsVnicEtherTable.setStatus("current")
_CucsVnicEtherEntry_Object = MibTableRow
cucsVnicEtherEntry = _CucsVnicEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1)
)
cucsVnicEtherEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicEtherInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicEtherEntry.setStatus("current")
_CucsVnicEtherInstanceId_Type = CucsManagedObjectId
_CucsVnicEtherInstanceId_Object = MibTableColumn
cucsVnicEtherInstanceId = _CucsVnicEtherInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 1),
    _CucsVnicEtherInstanceId_Type()
)
cucsVnicEtherInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicEtherInstanceId.setStatus("current")
_CucsVnicEtherDn_Type = CucsManagedObjectDn
_CucsVnicEtherDn_Object = MibTableColumn
cucsVnicEtherDn = _CucsVnicEtherDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 2),
    _CucsVnicEtherDn_Type()
)
cucsVnicEtherDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherDn.setStatus("current")
_CucsVnicEtherRn_Type = SnmpAdminString
_CucsVnicEtherRn_Object = MibTableColumn
cucsVnicEtherRn = _CucsVnicEtherRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 3),
    _CucsVnicEtherRn_Type()
)
cucsVnicEtherRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherRn.setStatus("current")
_CucsVnicEtherAdaptorProfileName_Type = SnmpAdminString
_CucsVnicEtherAdaptorProfileName_Object = MibTableColumn
cucsVnicEtherAdaptorProfileName = _CucsVnicEtherAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 4),
    _CucsVnicEtherAdaptorProfileName_Type()
)
cucsVnicEtherAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherAdaptorProfileName.setStatus("current")
_CucsVnicEtherAddr_Type = MacAddress
_CucsVnicEtherAddr_Object = MibTableColumn
cucsVnicEtherAddr = _CucsVnicEtherAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 5),
    _CucsVnicEtherAddr_Type()
)
cucsVnicEtherAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherAddr.setStatus("current")
_CucsVnicEtherAdminVcon_Type = SnmpAdminString
_CucsVnicEtherAdminVcon_Object = MibTableColumn
cucsVnicEtherAdminVcon = _CucsVnicEtherAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 6),
    _CucsVnicEtherAdminVcon_Type()
)
cucsVnicEtherAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherAdminVcon.setStatus("current")
_CucsVnicEtherBootDev_Type = CucsVnicVnicBootDev
_CucsVnicEtherBootDev_Object = MibTableColumn
cucsVnicEtherBootDev = _CucsVnicEtherBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 7),
    _CucsVnicEtherBootDev_Type()
)
cucsVnicEtherBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherBootDev.setStatus("current")
_CucsVnicEtherConfigState_Type = CucsLsConfigState
_CucsVnicEtherConfigState_Object = MibTableColumn
cucsVnicEtherConfigState = _CucsVnicEtherConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 8),
    _CucsVnicEtherConfigState_Type()
)
cucsVnicEtherConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherConfigState.setStatus("current")
_CucsVnicEtherEquipmentDn_Type = SnmpAdminString
_CucsVnicEtherEquipmentDn_Object = MibTableColumn
cucsVnicEtherEquipmentDn = _CucsVnicEtherEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 9),
    _CucsVnicEtherEquipmentDn_Type()
)
cucsVnicEtherEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherEquipmentDn.setStatus("current")
_CucsVnicEtherFltAggr_Type = Unsigned64
_CucsVnicEtherFltAggr_Object = MibTableColumn
cucsVnicEtherFltAggr = _CucsVnicEtherFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 10),
    _CucsVnicEtherFltAggr_Type()
)
cucsVnicEtherFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherFltAggr.setStatus("current")
_CucsVnicEtherIdentPoolName_Type = SnmpAdminString
_CucsVnicEtherIdentPoolName_Object = MibTableColumn
cucsVnicEtherIdentPoolName = _CucsVnicEtherIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 11),
    _CucsVnicEtherIdentPoolName_Type()
)
cucsVnicEtherIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIdentPoolName.setStatus("current")
_CucsVnicEtherInstType_Type = CucsVnicInstantiation
_CucsVnicEtherInstType_Object = MibTableColumn
cucsVnicEtherInstType = _CucsVnicEtherInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 12),
    _CucsVnicEtherInstType_Type()
)
cucsVnicEtherInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherInstType.setStatus("current")
_CucsVnicEtherMtu_Type = Gauge32
_CucsVnicEtherMtu_Object = MibTableColumn
cucsVnicEtherMtu = _CucsVnicEtherMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 13),
    _CucsVnicEtherMtu_Type()
)
cucsVnicEtherMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherMtu.setStatus("current")
_CucsVnicEtherName_Type = SnmpAdminString
_CucsVnicEtherName_Object = MibTableColumn
cucsVnicEtherName = _CucsVnicEtherName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 14),
    _CucsVnicEtherName_Type()
)
cucsVnicEtherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherName.setStatus("current")
_CucsVnicEtherNwCtrlPolicyName_Type = SnmpAdminString
_CucsVnicEtherNwCtrlPolicyName_Object = MibTableColumn
cucsVnicEtherNwCtrlPolicyName = _CucsVnicEtherNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 15),
    _CucsVnicEtherNwCtrlPolicyName_Type()
)
cucsVnicEtherNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherNwCtrlPolicyName.setStatus("current")
_CucsVnicEtherNwTemplName_Type = SnmpAdminString
_CucsVnicEtherNwTemplName_Object = MibTableColumn
cucsVnicEtherNwTemplName = _CucsVnicEtherNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 16),
    _CucsVnicEtherNwTemplName_Type()
)
cucsVnicEtherNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherNwTemplName.setStatus("current")
_CucsVnicEtherOperAdaptorProfileName_Type = SnmpAdminString
_CucsVnicEtherOperAdaptorProfileName_Object = MibTableColumn
cucsVnicEtherOperAdaptorProfileName = _CucsVnicEtherOperAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 17),
    _CucsVnicEtherOperAdaptorProfileName_Type()
)
cucsVnicEtherOperAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherOperAdaptorProfileName.setStatus("current")
_CucsVnicEtherOperIdentPoolName_Type = SnmpAdminString
_CucsVnicEtherOperIdentPoolName_Object = MibTableColumn
cucsVnicEtherOperIdentPoolName = _CucsVnicEtherOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 18),
    _CucsVnicEtherOperIdentPoolName_Type()
)
cucsVnicEtherOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherOperIdentPoolName.setStatus("current")
_CucsVnicEtherOperNwCtrlPolicyName_Type = SnmpAdminString
_CucsVnicEtherOperNwCtrlPolicyName_Object = MibTableColumn
cucsVnicEtherOperNwCtrlPolicyName = _CucsVnicEtherOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 19),
    _CucsVnicEtherOperNwCtrlPolicyName_Type()
)
cucsVnicEtherOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherOperNwCtrlPolicyName.setStatus("current")
_CucsVnicEtherOperNwTemplName_Type = SnmpAdminString
_CucsVnicEtherOperNwTemplName_Object = MibTableColumn
cucsVnicEtherOperNwTemplName = _CucsVnicEtherOperNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 20),
    _CucsVnicEtherOperNwTemplName_Type()
)
cucsVnicEtherOperNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherOperNwTemplName.setStatus("current")
_CucsVnicEtherOperOrder_Type = Gauge32
_CucsVnicEtherOperOrder_Object = MibTableColumn
cucsVnicEtherOperOrder = _CucsVnicEtherOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 21),
    _CucsVnicEtherOperOrder_Type()
)
cucsVnicEtherOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherOperOrder.setStatus("current")
_CucsVnicEtherOperQosPolicyName_Type = SnmpAdminString
_CucsVnicEtherOperQosPolicyName_Object = MibTableColumn
cucsVnicEtherOperQosPolicyName = _CucsVnicEtherOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 22),
    _CucsVnicEtherOperQosPolicyName_Type()
)
cucsVnicEtherOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherOperQosPolicyName.setStatus("current")
_CucsVnicEtherOperSpeed_Type = Gauge32
_CucsVnicEtherOperSpeed_Object = MibTableColumn
cucsVnicEtherOperSpeed = _CucsVnicEtherOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 23),
    _CucsVnicEtherOperSpeed_Type()
)
cucsVnicEtherOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherOperSpeed.setStatus("current")
_CucsVnicEtherOperStatsPolicyName_Type = SnmpAdminString
_CucsVnicEtherOperStatsPolicyName_Object = MibTableColumn
cucsVnicEtherOperStatsPolicyName = _CucsVnicEtherOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 24),
    _CucsVnicEtherOperStatsPolicyName_Type()
)
cucsVnicEtherOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherOperStatsPolicyName.setStatus("current")
_CucsVnicEtherOperVcon_Type = SnmpAdminString
_CucsVnicEtherOperVcon_Object = MibTableColumn
cucsVnicEtherOperVcon = _CucsVnicEtherOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 25),
    _CucsVnicEtherOperVcon_Type()
)
cucsVnicEtherOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherOperVcon.setStatus("current")
_CucsVnicEtherOrder_Type = Gauge32
_CucsVnicEtherOrder_Object = MibTableColumn
cucsVnicEtherOrder = _CucsVnicEtherOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 26),
    _CucsVnicEtherOrder_Type()
)
cucsVnicEtherOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherOrder.setStatus("current")
_CucsVnicEtherOwner_Type = CucsVnicConnectionOwner
_CucsVnicEtherOwner_Object = MibTableColumn
cucsVnicEtherOwner = _CucsVnicEtherOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 27),
    _CucsVnicEtherOwner_Type()
)
cucsVnicEtherOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherOwner.setStatus("current")
_CucsVnicEtherPinToGroupName_Type = SnmpAdminString
_CucsVnicEtherPinToGroupName_Object = MibTableColumn
cucsVnicEtherPinToGroupName = _CucsVnicEtherPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 28),
    _CucsVnicEtherPinToGroupName_Type()
)
cucsVnicEtherPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherPinToGroupName.setStatus("current")
_CucsVnicEtherQosPolicyName_Type = SnmpAdminString
_CucsVnicEtherQosPolicyName_Object = MibTableColumn
cucsVnicEtherQosPolicyName = _CucsVnicEtherQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 29),
    _CucsVnicEtherQosPolicyName_Type()
)
cucsVnicEtherQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherQosPolicyName.setStatus("current")
_CucsVnicEtherStatsPolicyName_Type = SnmpAdminString
_CucsVnicEtherStatsPolicyName_Object = MibTableColumn
cucsVnicEtherStatsPolicyName = _CucsVnicEtherStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 30),
    _CucsVnicEtherStatsPolicyName_Type()
)
cucsVnicEtherStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherStatsPolicyName.setStatus("current")
_CucsVnicEtherSwitchId_Type = CucsVnicEtherBaseSwitchId
_CucsVnicEtherSwitchId_Object = MibTableColumn
cucsVnicEtherSwitchId = _CucsVnicEtherSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 31),
    _CucsVnicEtherSwitchId_Type()
)
cucsVnicEtherSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherSwitchId.setStatus("current")
_CucsVnicEtherType_Type = CucsVnicEtherType
_CucsVnicEtherType_Object = MibTableColumn
cucsVnicEtherType = _CucsVnicEtherType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 32),
    _CucsVnicEtherType_Type()
)
cucsVnicEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherType.setStatus("current")
_CucsVnicEtherOperPinToGroupName_Type = SnmpAdminString
_CucsVnicEtherOperPinToGroupName_Object = MibTableColumn
cucsVnicEtherOperPinToGroupName = _CucsVnicEtherOperPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 33),
    _CucsVnicEtherOperPinToGroupName_Type()
)
cucsVnicEtherOperPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherOperPinToGroupName.setStatus("current")
_CucsVnicEtherConfigQualifier_Type = CucsVnicConfigIssues
_CucsVnicEtherConfigQualifier_Object = MibTableColumn
cucsVnicEtherConfigQualifier = _CucsVnicEtherConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 34),
    _CucsVnicEtherConfigQualifier_Type()
)
cucsVnicEtherConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherConfigQualifier.setStatus("current")
_CucsVnicEtherDynamicId_Type = Gauge32
_CucsVnicEtherDynamicId_Object = MibTableColumn
cucsVnicEtherDynamicId = _CucsVnicEtherDynamicId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 35),
    _CucsVnicEtherDynamicId_Type()
)
cucsVnicEtherDynamicId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherDynamicId.setStatus("current")
_CucsVnicEtherPfDn_Type = SnmpAdminString
_CucsVnicEtherPfDn_Object = MibTableColumn
cucsVnicEtherPfDn = _CucsVnicEtherPfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 36),
    _CucsVnicEtherPfDn_Type()
)
cucsVnicEtherPfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherPfDn.setStatus("current")
_CucsVnicEtherVirtualizationPreference_Type = CucsVnicVirtualizationPreferenceType
_CucsVnicEtherVirtualizationPreference_Object = MibTableColumn
cucsVnicEtherVirtualizationPreference = _CucsVnicEtherVirtualizationPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 37),
    _CucsVnicEtherVirtualizationPreference_Type()
)
cucsVnicEtherVirtualizationPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherVirtualizationPreference.setStatus("current")
_CucsVnicEtherAdminHostPort_Type = CucsFabricHostPortId
_CucsVnicEtherAdminHostPort_Object = MibTableColumn
cucsVnicEtherAdminHostPort = _CucsVnicEtherAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 39),
    _CucsVnicEtherAdminHostPort_Type()
)
cucsVnicEtherAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherAdminHostPort.setStatus("current")
_CucsVnicEtherOperHostPort_Type = CucsVnicVnicOperHostPort
_CucsVnicEtherOperHostPort_Object = MibTableColumn
cucsVnicEtherOperHostPort = _CucsVnicEtherOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 40),
    _CucsVnicEtherOperHostPort_Type()
)
cucsVnicEtherOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherOperHostPort.setStatus("current")
_CucsVnicEtherPropAcl_Type = Unsigned64
_CucsVnicEtherPropAcl_Object = MibTableColumn
cucsVnicEtherPropAcl = _CucsVnicEtherPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 41),
    _CucsVnicEtherPropAcl_Type()
)
cucsVnicEtherPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherPropAcl.setStatus("current")
_CucsVnicEtherPurpose_Type = CucsAdaptorPurpose
_CucsVnicEtherPurpose_Object = MibTableColumn
cucsVnicEtherPurpose = _CucsVnicEtherPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 42),
    _CucsVnicEtherPurpose_Type()
)
cucsVnicEtherPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherPurpose.setStatus("current")
_CucsVnicEtherAdminCdnName_Type = SnmpAdminString
_CucsVnicEtherAdminCdnName_Object = MibTableColumn
cucsVnicEtherAdminCdnName = _CucsVnicEtherAdminCdnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 43),
    _CucsVnicEtherAdminCdnName_Type()
)
cucsVnicEtherAdminCdnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherAdminCdnName.setStatus("current")
_CucsVnicEtherOperCdnName_Type = SnmpAdminString
_CucsVnicEtherOperCdnName_Object = MibTableColumn
cucsVnicEtherOperCdnName = _CucsVnicEtherOperCdnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 44),
    _CucsVnicEtherOperCdnName_Type()
)
cucsVnicEtherOperCdnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherOperCdnName.setStatus("current")
_CucsVnicEtherCdnSource_Type = CucsVnicCdnSource
_CucsVnicEtherCdnSource_Object = MibTableColumn
cucsVnicEtherCdnSource = _CucsVnicEtherCdnSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 45),
    _CucsVnicEtherCdnSource_Type()
)
cucsVnicEtherCdnSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherCdnSource.setStatus("current")
_CucsVnicEtherCdnPropInSync_Type = TruthValue
_CucsVnicEtherCdnPropInSync_Object = MibTableColumn
cucsVnicEtherCdnPropInSync = _CucsVnicEtherCdnPropInSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 9, 1, 46),
    _CucsVnicEtherCdnPropInSync_Type()
)
cucsVnicEtherCdnPropInSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherCdnPropInSync.setStatus("current")
_CucsVnicEtherIfTable_Object = MibTable
cucsVnicEtherIfTable = _CucsVnicEtherIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10)
)
if mibBuilder.loadTexts:
    cucsVnicEtherIfTable.setStatus("current")
_CucsVnicEtherIfEntry_Object = MibTableRow
cucsVnicEtherIfEntry = _CucsVnicEtherIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1)
)
cucsVnicEtherIfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicEtherIfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicEtherIfEntry.setStatus("current")
_CucsVnicEtherIfInstanceId_Type = CucsManagedObjectId
_CucsVnicEtherIfInstanceId_Object = MibTableColumn
cucsVnicEtherIfInstanceId = _CucsVnicEtherIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 1),
    _CucsVnicEtherIfInstanceId_Type()
)
cucsVnicEtherIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicEtherIfInstanceId.setStatus("current")
_CucsVnicEtherIfDn_Type = CucsManagedObjectDn
_CucsVnicEtherIfDn_Object = MibTableColumn
cucsVnicEtherIfDn = _CucsVnicEtherIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 2),
    _CucsVnicEtherIfDn_Type()
)
cucsVnicEtherIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfDn.setStatus("current")
_CucsVnicEtherIfRn_Type = SnmpAdminString
_CucsVnicEtherIfRn_Object = MibTableColumn
cucsVnicEtherIfRn = _CucsVnicEtherIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 3),
    _CucsVnicEtherIfRn_Type()
)
cucsVnicEtherIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfRn.setStatus("current")
_CucsVnicEtherIfAddr_Type = MacAddress
_CucsVnicEtherIfAddr_Object = MibTableColumn
cucsVnicEtherIfAddr = _CucsVnicEtherIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 4),
    _CucsVnicEtherIfAddr_Type()
)
cucsVnicEtherIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfAddr.setStatus("current")
_CucsVnicEtherIfDefaultNet_Type = TruthValue
_CucsVnicEtherIfDefaultNet_Object = MibTableColumn
cucsVnicEtherIfDefaultNet = _CucsVnicEtherIfDefaultNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 5),
    _CucsVnicEtherIfDefaultNet_Type()
)
cucsVnicEtherIfDefaultNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfDefaultNet.setStatus("current")
_CucsVnicEtherIfName_Type = SnmpAdminString
_CucsVnicEtherIfName_Object = MibTableColumn
cucsVnicEtherIfName = _CucsVnicEtherIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 6),
    _CucsVnicEtherIfName_Type()
)
cucsVnicEtherIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfName.setStatus("current")
_CucsVnicEtherIfOperState_Type = CucsVnicIfOperState
_CucsVnicEtherIfOperState_Object = MibTableColumn
cucsVnicEtherIfOperState = _CucsVnicEtherIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 7),
    _CucsVnicEtherIfOperState_Type()
)
cucsVnicEtherIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfOperState.setStatus("current")
_CucsVnicEtherIfOwner_Type = CucsVnicConnectionOwner
_CucsVnicEtherIfOwner_Object = MibTableColumn
cucsVnicEtherIfOwner = _CucsVnicEtherIfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 8),
    _CucsVnicEtherIfOwner_Type()
)
cucsVnicEtherIfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfOwner.setStatus("current")
_CucsVnicEtherIfSwitchId_Type = CucsVnicEtherBaseIfSwitchId
_CucsVnicEtherIfSwitchId_Object = MibTableColumn
cucsVnicEtherIfSwitchId = _CucsVnicEtherIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 9),
    _CucsVnicEtherIfSwitchId_Type()
)
cucsVnicEtherIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfSwitchId.setStatus("current")
_CucsVnicEtherIfType_Type = CucsVnicAEtherIfType
_CucsVnicEtherIfType_Object = MibTableColumn
cucsVnicEtherIfType = _CucsVnicEtherIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 10),
    _CucsVnicEtherIfType_Type()
)
cucsVnicEtherIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfType.setStatus("current")
_CucsVnicEtherIfVnet_Type = Gauge32
_CucsVnicEtherIfVnet_Object = MibTableColumn
cucsVnicEtherIfVnet = _CucsVnicEtherIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 11),
    _CucsVnicEtherIfVnet_Type()
)
cucsVnicEtherIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfVnet.setStatus("current")
_CucsVnicEtherIfOperVnetDn_Type = SnmpAdminString
_CucsVnicEtherIfOperVnetDn_Object = MibTableColumn
cucsVnicEtherIfOperVnetDn = _CucsVnicEtherIfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 12),
    _CucsVnicEtherIfOperVnetDn_Type()
)
cucsVnicEtherIfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfOperVnetDn.setStatus("current")
_CucsVnicEtherIfOperVnetName_Type = SnmpAdminString
_CucsVnicEtherIfOperVnetName_Object = MibTableColumn
cucsVnicEtherIfOperVnetName = _CucsVnicEtherIfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 13),
    _CucsVnicEtherIfOperVnetName_Type()
)
cucsVnicEtherIfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfOperVnetName.setStatus("current")
_CucsVnicEtherIfConfigQualifier_Type = CucsVnicConfigIssues
_CucsVnicEtherIfConfigQualifier_Object = MibTableColumn
cucsVnicEtherIfConfigQualifier = _CucsVnicEtherIfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 14),
    _CucsVnicEtherIfConfigQualifier_Type()
)
cucsVnicEtherIfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfConfigQualifier.setStatus("current")
_CucsVnicEtherIfFltAggr_Type = Unsigned64
_CucsVnicEtherIfFltAggr_Object = MibTableColumn
cucsVnicEtherIfFltAggr = _CucsVnicEtherIfFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 15),
    _CucsVnicEtherIfFltAggr_Type()
)
cucsVnicEtherIfFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfFltAggr.setStatus("current")
_CucsVnicEtherIfPubNwId_Type = Gauge32
_CucsVnicEtherIfPubNwId_Object = MibTableColumn
cucsVnicEtherIfPubNwId = _CucsVnicEtherIfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 17),
    _CucsVnicEtherIfPubNwId_Type()
)
cucsVnicEtherIfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfPubNwId.setStatus("current")
_CucsVnicEtherIfSharing_Type = CucsFabricVlanSharingType
_CucsVnicEtherIfSharing_Object = MibTableColumn
cucsVnicEtherIfSharing = _CucsVnicEtherIfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 18),
    _CucsVnicEtherIfSharing_Type()
)
cucsVnicEtherIfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfSharing.setStatus("current")
_CucsVnicEtherIfPropAcl_Type = Unsigned64
_CucsVnicEtherIfPropAcl_Object = MibTableColumn
cucsVnicEtherIfPropAcl = _CucsVnicEtherIfPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 19),
    _CucsVnicEtherIfPropAcl_Type()
)
cucsVnicEtherIfPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfPropAcl.setStatus("current")
_CucsVnicEtherIfOperPrimaryVnetDn_Type = SnmpAdminString
_CucsVnicEtherIfOperPrimaryVnetDn_Object = MibTableColumn
cucsVnicEtherIfOperPrimaryVnetDn = _CucsVnicEtherIfOperPrimaryVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 20),
    _CucsVnicEtherIfOperPrimaryVnetDn_Type()
)
cucsVnicEtherIfOperPrimaryVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfOperPrimaryVnetDn.setStatus("current")
_CucsVnicEtherIfOperPrimaryVnetName_Type = SnmpAdminString
_CucsVnicEtherIfOperPrimaryVnetName_Object = MibTableColumn
cucsVnicEtherIfOperPrimaryVnetName = _CucsVnicEtherIfOperPrimaryVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 10, 1, 21),
    _CucsVnicEtherIfOperPrimaryVnetName_Type()
)
cucsVnicEtherIfOperPrimaryVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEtherIfOperPrimaryVnetName.setStatus("current")
_CucsVnicFcTable_Object = MibTable
cucsVnicFcTable = _CucsVnicFcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11)
)
if mibBuilder.loadTexts:
    cucsVnicFcTable.setStatus("current")
_CucsVnicFcEntry_Object = MibTableRow
cucsVnicFcEntry = _CucsVnicFcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1)
)
cucsVnicFcEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicFcInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicFcEntry.setStatus("current")
_CucsVnicFcInstanceId_Type = CucsManagedObjectId
_CucsVnicFcInstanceId_Object = MibTableColumn
cucsVnicFcInstanceId = _CucsVnicFcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 1),
    _CucsVnicFcInstanceId_Type()
)
cucsVnicFcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicFcInstanceId.setStatus("current")
_CucsVnicFcDn_Type = CucsManagedObjectDn
_CucsVnicFcDn_Object = MibTableColumn
cucsVnicFcDn = _CucsVnicFcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 2),
    _CucsVnicFcDn_Type()
)
cucsVnicFcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcDn.setStatus("current")
_CucsVnicFcRn_Type = SnmpAdminString
_CucsVnicFcRn_Object = MibTableColumn
cucsVnicFcRn = _CucsVnicFcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 3),
    _CucsVnicFcRn_Type()
)
cucsVnicFcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcRn.setStatus("current")
_CucsVnicFcAdaptorProfileName_Type = SnmpAdminString
_CucsVnicFcAdaptorProfileName_Object = MibTableColumn
cucsVnicFcAdaptorProfileName = _CucsVnicFcAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 4),
    _CucsVnicFcAdaptorProfileName_Type()
)
cucsVnicFcAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcAdaptorProfileName.setStatus("current")
_CucsVnicFcAddr_Type = Unsigned64
_CucsVnicFcAddr_Object = MibTableColumn
cucsVnicFcAddr = _CucsVnicFcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 5),
    _CucsVnicFcAddr_Type()
)
cucsVnicFcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcAddr.setStatus("current")
_CucsVnicFcAdminVcon_Type = SnmpAdminString
_CucsVnicFcAdminVcon_Object = MibTableColumn
cucsVnicFcAdminVcon = _CucsVnicFcAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 6),
    _CucsVnicFcAdminVcon_Type()
)
cucsVnicFcAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcAdminVcon.setStatus("current")
_CucsVnicFcBootDev_Type = CucsVnicVnicBootDev
_CucsVnicFcBootDev_Object = MibTableColumn
cucsVnicFcBootDev = _CucsVnicFcBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 7),
    _CucsVnicFcBootDev_Type()
)
cucsVnicFcBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcBootDev.setStatus("current")
_CucsVnicFcConfigState_Type = CucsLsConfigState
_CucsVnicFcConfigState_Object = MibTableColumn
cucsVnicFcConfigState = _CucsVnicFcConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 8),
    _CucsVnicFcConfigState_Type()
)
cucsVnicFcConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcConfigState.setStatus("current")
_CucsVnicFcEquipmentDn_Type = SnmpAdminString
_CucsVnicFcEquipmentDn_Object = MibTableColumn
cucsVnicFcEquipmentDn = _CucsVnicFcEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 9),
    _CucsVnicFcEquipmentDn_Type()
)
cucsVnicFcEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcEquipmentDn.setStatus("current")
_CucsVnicFcFltAggr_Type = Unsigned64
_CucsVnicFcFltAggr_Object = MibTableColumn
cucsVnicFcFltAggr = _CucsVnicFcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 10),
    _CucsVnicFcFltAggr_Type()
)
cucsVnicFcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcFltAggr.setStatus("current")
_CucsVnicFcIdentPoolName_Type = SnmpAdminString
_CucsVnicFcIdentPoolName_Object = MibTableColumn
cucsVnicFcIdentPoolName = _CucsVnicFcIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 11),
    _CucsVnicFcIdentPoolName_Type()
)
cucsVnicFcIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcIdentPoolName.setStatus("current")
_CucsVnicFcInstType_Type = CucsVnicInstantiation
_CucsVnicFcInstType_Object = MibTableColumn
cucsVnicFcInstType = _CucsVnicFcInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 12),
    _CucsVnicFcInstType_Type()
)
cucsVnicFcInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcInstType.setStatus("current")
_CucsVnicFcMaxDataFieldSize_Type = Gauge32
_CucsVnicFcMaxDataFieldSize_Object = MibTableColumn
cucsVnicFcMaxDataFieldSize = _CucsVnicFcMaxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 13),
    _CucsVnicFcMaxDataFieldSize_Type()
)
cucsVnicFcMaxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcMaxDataFieldSize.setStatus("current")
_CucsVnicFcName_Type = SnmpAdminString
_CucsVnicFcName_Object = MibTableColumn
cucsVnicFcName = _CucsVnicFcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 14),
    _CucsVnicFcName_Type()
)
cucsVnicFcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcName.setStatus("current")
_CucsVnicFcNdAddr_Type = Unsigned64
_CucsVnicFcNdAddr_Object = MibTableColumn
cucsVnicFcNdAddr = _CucsVnicFcNdAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 15),
    _CucsVnicFcNdAddr_Type()
)
cucsVnicFcNdAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcNdAddr.setStatus("current")
_CucsVnicFcNwTemplName_Type = SnmpAdminString
_CucsVnicFcNwTemplName_Object = MibTableColumn
cucsVnicFcNwTemplName = _CucsVnicFcNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 16),
    _CucsVnicFcNwTemplName_Type()
)
cucsVnicFcNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcNwTemplName.setStatus("current")
_CucsVnicFcOperAdaptorProfileName_Type = SnmpAdminString
_CucsVnicFcOperAdaptorProfileName_Object = MibTableColumn
cucsVnicFcOperAdaptorProfileName = _CucsVnicFcOperAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 17),
    _CucsVnicFcOperAdaptorProfileName_Type()
)
cucsVnicFcOperAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOperAdaptorProfileName.setStatus("current")
_CucsVnicFcOperIdentPoolName_Type = SnmpAdminString
_CucsVnicFcOperIdentPoolName_Object = MibTableColumn
cucsVnicFcOperIdentPoolName = _CucsVnicFcOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 18),
    _CucsVnicFcOperIdentPoolName_Type()
)
cucsVnicFcOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOperIdentPoolName.setStatus("current")
_CucsVnicFcOperNwTemplName_Type = SnmpAdminString
_CucsVnicFcOperNwTemplName_Object = MibTableColumn
cucsVnicFcOperNwTemplName = _CucsVnicFcOperNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 19),
    _CucsVnicFcOperNwTemplName_Type()
)
cucsVnicFcOperNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOperNwTemplName.setStatus("current")
_CucsVnicFcOperOrder_Type = Gauge32
_CucsVnicFcOperOrder_Object = MibTableColumn
cucsVnicFcOperOrder = _CucsVnicFcOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 20),
    _CucsVnicFcOperOrder_Type()
)
cucsVnicFcOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOperOrder.setStatus("current")
_CucsVnicFcOperQosPolicyName_Type = SnmpAdminString
_CucsVnicFcOperQosPolicyName_Object = MibTableColumn
cucsVnicFcOperQosPolicyName = _CucsVnicFcOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 21),
    _CucsVnicFcOperQosPolicyName_Type()
)
cucsVnicFcOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOperQosPolicyName.setStatus("current")
_CucsVnicFcOperSpeed_Type = Gauge32
_CucsVnicFcOperSpeed_Object = MibTableColumn
cucsVnicFcOperSpeed = _CucsVnicFcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 22),
    _CucsVnicFcOperSpeed_Type()
)
cucsVnicFcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOperSpeed.setStatus("current")
_CucsVnicFcOperStatsPolicyName_Type = SnmpAdminString
_CucsVnicFcOperStatsPolicyName_Object = MibTableColumn
cucsVnicFcOperStatsPolicyName = _CucsVnicFcOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 23),
    _CucsVnicFcOperStatsPolicyName_Type()
)
cucsVnicFcOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOperStatsPolicyName.setStatus("current")
_CucsVnicFcOperVcon_Type = SnmpAdminString
_CucsVnicFcOperVcon_Object = MibTableColumn
cucsVnicFcOperVcon = _CucsVnicFcOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 24),
    _CucsVnicFcOperVcon_Type()
)
cucsVnicFcOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOperVcon.setStatus("current")
_CucsVnicFcOrder_Type = Gauge32
_CucsVnicFcOrder_Object = MibTableColumn
cucsVnicFcOrder = _CucsVnicFcOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 25),
    _CucsVnicFcOrder_Type()
)
cucsVnicFcOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOrder.setStatus("current")
_CucsVnicFcOwner_Type = CucsVnicConnectionOwner
_CucsVnicFcOwner_Object = MibTableColumn
cucsVnicFcOwner = _CucsVnicFcOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 26),
    _CucsVnicFcOwner_Type()
)
cucsVnicFcOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOwner.setStatus("current")
_CucsVnicFcPersBind_Type = CucsVnicFcBasePersBind
_CucsVnicFcPersBind_Object = MibTableColumn
cucsVnicFcPersBind = _CucsVnicFcPersBind_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 27),
    _CucsVnicFcPersBind_Type()
)
cucsVnicFcPersBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcPersBind.setStatus("current")
_CucsVnicFcPersBindClear_Type = TruthValue
_CucsVnicFcPersBindClear_Object = MibTableColumn
cucsVnicFcPersBindClear = _CucsVnicFcPersBindClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 28),
    _CucsVnicFcPersBindClear_Type()
)
cucsVnicFcPersBindClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcPersBindClear.setStatus("current")
_CucsVnicFcPinToGroupName_Type = SnmpAdminString
_CucsVnicFcPinToGroupName_Object = MibTableColumn
cucsVnicFcPinToGroupName = _CucsVnicFcPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 29),
    _CucsVnicFcPinToGroupName_Type()
)
cucsVnicFcPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcPinToGroupName.setStatus("current")
_CucsVnicFcQosPolicyName_Type = SnmpAdminString
_CucsVnicFcQosPolicyName_Object = MibTableColumn
cucsVnicFcQosPolicyName = _CucsVnicFcQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 30),
    _CucsVnicFcQosPolicyName_Type()
)
cucsVnicFcQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcQosPolicyName.setStatus("current")
_CucsVnicFcStatsPolicyName_Type = SnmpAdminString
_CucsVnicFcStatsPolicyName_Object = MibTableColumn
cucsVnicFcStatsPolicyName = _CucsVnicFcStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 31),
    _CucsVnicFcStatsPolicyName_Type()
)
cucsVnicFcStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcStatsPolicyName.setStatus("current")
_CucsVnicFcSwitchId_Type = CucsNetworkSwitchId
_CucsVnicFcSwitchId_Object = MibTableColumn
cucsVnicFcSwitchId = _CucsVnicFcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 32),
    _CucsVnicFcSwitchId_Type()
)
cucsVnicFcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcSwitchId.setStatus("current")
_CucsVnicFcType_Type = CucsVnicFcBaseType
_CucsVnicFcType_Object = MibTableColumn
cucsVnicFcType = _CucsVnicFcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 33),
    _CucsVnicFcType_Type()
)
cucsVnicFcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcType.setStatus("current")
_CucsVnicFcOperPinToGroupName_Type = SnmpAdminString
_CucsVnicFcOperPinToGroupName_Object = MibTableColumn
cucsVnicFcOperPinToGroupName = _CucsVnicFcOperPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 34),
    _CucsVnicFcOperPinToGroupName_Type()
)
cucsVnicFcOperPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOperPinToGroupName.setStatus("current")
_CucsVnicFcConfigQualifier_Type = CucsVnicConfigIssues
_CucsVnicFcConfigQualifier_Object = MibTableColumn
cucsVnicFcConfigQualifier = _CucsVnicFcConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 35),
    _CucsVnicFcConfigQualifier_Type()
)
cucsVnicFcConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcConfigQualifier.setStatus("current")
_CucsVnicFcAdminHostPort_Type = CucsFabricHostPortId
_CucsVnicFcAdminHostPort_Object = MibTableColumn
cucsVnicFcAdminHostPort = _CucsVnicFcAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 37),
    _CucsVnicFcAdminHostPort_Type()
)
cucsVnicFcAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcAdminHostPort.setStatus("current")
_CucsVnicFcOperHostPort_Type = CucsVnicVnicOperHostPort
_CucsVnicFcOperHostPort_Object = MibTableColumn
cucsVnicFcOperHostPort = _CucsVnicFcOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 38),
    _CucsVnicFcOperHostPort_Type()
)
cucsVnicFcOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOperHostPort.setStatus("current")
_CucsVnicFcAdminCdnName_Type = SnmpAdminString
_CucsVnicFcAdminCdnName_Object = MibTableColumn
cucsVnicFcAdminCdnName = _CucsVnicFcAdminCdnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 39),
    _CucsVnicFcAdminCdnName_Type()
)
cucsVnicFcAdminCdnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcAdminCdnName.setStatus("current")
_CucsVnicFcOperCdnName_Type = SnmpAdminString
_CucsVnicFcOperCdnName_Object = MibTableColumn
cucsVnicFcOperCdnName = _CucsVnicFcOperCdnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 40),
    _CucsVnicFcOperCdnName_Type()
)
cucsVnicFcOperCdnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOperCdnName.setStatus("current")
_CucsVnicFcCdnSource_Type = CucsVnicCdnSource
_CucsVnicFcCdnSource_Object = MibTableColumn
cucsVnicFcCdnSource = _CucsVnicFcCdnSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 41),
    _CucsVnicFcCdnSource_Type()
)
cucsVnicFcCdnSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcCdnSource.setStatus("current")
_CucsVnicFcCdnPropInSync_Type = TruthValue
_CucsVnicFcCdnPropInSync_Object = MibTableColumn
cucsVnicFcCdnPropInSync = _CucsVnicFcCdnPropInSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 11, 1, 42),
    _CucsVnicFcCdnPropInSync_Type()
)
cucsVnicFcCdnPropInSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcCdnPropInSync.setStatus("current")
_CucsVnicFcIfTable_Object = MibTable
cucsVnicFcIfTable = _CucsVnicFcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12)
)
if mibBuilder.loadTexts:
    cucsVnicFcIfTable.setStatus("current")
_CucsVnicFcIfEntry_Object = MibTableRow
cucsVnicFcIfEntry = _CucsVnicFcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1)
)
cucsVnicFcIfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicFcIfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicFcIfEntry.setStatus("current")
_CucsVnicFcIfInstanceId_Type = CucsManagedObjectId
_CucsVnicFcIfInstanceId_Object = MibTableColumn
cucsVnicFcIfInstanceId = _CucsVnicFcIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1, 1),
    _CucsVnicFcIfInstanceId_Type()
)
cucsVnicFcIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicFcIfInstanceId.setStatus("current")
_CucsVnicFcIfDn_Type = CucsManagedObjectDn
_CucsVnicFcIfDn_Object = MibTableColumn
cucsVnicFcIfDn = _CucsVnicFcIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1, 2),
    _CucsVnicFcIfDn_Type()
)
cucsVnicFcIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcIfDn.setStatus("current")
_CucsVnicFcIfRn_Type = SnmpAdminString
_CucsVnicFcIfRn_Object = MibTableColumn
cucsVnicFcIfRn = _CucsVnicFcIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1, 3),
    _CucsVnicFcIfRn_Type()
)
cucsVnicFcIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcIfRn.setStatus("current")
_CucsVnicFcIfInitiator_Type = Unsigned64
_CucsVnicFcIfInitiator_Object = MibTableColumn
cucsVnicFcIfInitiator = _CucsVnicFcIfInitiator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1, 4),
    _CucsVnicFcIfInitiator_Type()
)
cucsVnicFcIfInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcIfInitiator.setStatus("current")
_CucsVnicFcIfName_Type = SnmpAdminString
_CucsVnicFcIfName_Object = MibTableColumn
cucsVnicFcIfName = _CucsVnicFcIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1, 5),
    _CucsVnicFcIfName_Type()
)
cucsVnicFcIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcIfName.setStatus("current")
_CucsVnicFcIfOperState_Type = CucsVnicIfOperState
_CucsVnicFcIfOperState_Object = MibTableColumn
cucsVnicFcIfOperState = _CucsVnicFcIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1, 6),
    _CucsVnicFcIfOperState_Type()
)
cucsVnicFcIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcIfOperState.setStatus("current")
_CucsVnicFcIfOwner_Type = CucsVnicConnectionOwner
_CucsVnicFcIfOwner_Object = MibTableColumn
cucsVnicFcIfOwner = _CucsVnicFcIfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1, 7),
    _CucsVnicFcIfOwner_Type()
)
cucsVnicFcIfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcIfOwner.setStatus("current")
_CucsVnicFcIfSwitchId_Type = CucsVnicAFcIfSwitchId
_CucsVnicFcIfSwitchId_Object = MibTableColumn
cucsVnicFcIfSwitchId = _CucsVnicFcIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1, 8),
    _CucsVnicFcIfSwitchId_Type()
)
cucsVnicFcIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcIfSwitchId.setStatus("current")
_CucsVnicFcIfType_Type = CucsVnicAFcIfType
_CucsVnicFcIfType_Object = MibTableColumn
cucsVnicFcIfType = _CucsVnicFcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1, 9),
    _CucsVnicFcIfType_Type()
)
cucsVnicFcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcIfType.setStatus("current")
_CucsVnicFcIfVnet_Type = Gauge32
_CucsVnicFcIfVnet_Object = MibTableColumn
cucsVnicFcIfVnet = _CucsVnicFcIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1, 10),
    _CucsVnicFcIfVnet_Type()
)
cucsVnicFcIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcIfVnet.setStatus("current")
_CucsVnicFcIfOperVnetDn_Type = SnmpAdminString
_CucsVnicFcIfOperVnetDn_Object = MibTableColumn
cucsVnicFcIfOperVnetDn = _CucsVnicFcIfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1, 11),
    _CucsVnicFcIfOperVnetDn_Type()
)
cucsVnicFcIfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcIfOperVnetDn.setStatus("current")
_CucsVnicFcIfOperVnetName_Type = SnmpAdminString
_CucsVnicFcIfOperVnetName_Object = MibTableColumn
cucsVnicFcIfOperVnetName = _CucsVnicFcIfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1, 12),
    _CucsVnicFcIfOperVnetName_Type()
)
cucsVnicFcIfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcIfOperVnetName.setStatus("current")
_CucsVnicFcIfConfigQualifier_Type = CucsVnicConfigIssues
_CucsVnicFcIfConfigQualifier_Object = MibTableColumn
cucsVnicFcIfConfigQualifier = _CucsVnicFcIfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1, 13),
    _CucsVnicFcIfConfigQualifier_Type()
)
cucsVnicFcIfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcIfConfigQualifier.setStatus("current")
_CucsVnicFcIfPubNwId_Type = Gauge32
_CucsVnicFcIfPubNwId_Object = MibTableColumn
cucsVnicFcIfPubNwId = _CucsVnicFcIfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1, 15),
    _CucsVnicFcIfPubNwId_Type()
)
cucsVnicFcIfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcIfPubNwId.setStatus("current")
_CucsVnicFcIfSharing_Type = CucsFabricVlanSharingType
_CucsVnicFcIfSharing_Object = MibTableColumn
cucsVnicFcIfSharing = _CucsVnicFcIfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1, 16),
    _CucsVnicFcIfSharing_Type()
)
cucsVnicFcIfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcIfSharing.setStatus("current")
_CucsVnicFcIfOperPrimaryVnetDn_Type = SnmpAdminString
_CucsVnicFcIfOperPrimaryVnetDn_Object = MibTableColumn
cucsVnicFcIfOperPrimaryVnetDn = _CucsVnicFcIfOperPrimaryVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1, 17),
    _CucsVnicFcIfOperPrimaryVnetDn_Type()
)
cucsVnicFcIfOperPrimaryVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcIfOperPrimaryVnetDn.setStatus("current")
_CucsVnicFcIfOperPrimaryVnetName_Type = SnmpAdminString
_CucsVnicFcIfOperPrimaryVnetName_Object = MibTableColumn
cucsVnicFcIfOperPrimaryVnetName = _CucsVnicFcIfOperPrimaryVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 12, 1, 18),
    _CucsVnicFcIfOperPrimaryVnetName_Type()
)
cucsVnicFcIfOperPrimaryVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcIfOperPrimaryVnetName.setStatus("current")
_CucsVnicFcLifTable_Object = MibTable
cucsVnicFcLifTable = _CucsVnicFcLifTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 13)
)
if mibBuilder.loadTexts:
    cucsVnicFcLifTable.setStatus("current")
_CucsVnicFcLifEntry_Object = MibTableRow
cucsVnicFcLifEntry = _CucsVnicFcLifEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 13, 1)
)
cucsVnicFcLifEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicFcLifInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicFcLifEntry.setStatus("current")
_CucsVnicFcLifInstanceId_Type = CucsManagedObjectId
_CucsVnicFcLifInstanceId_Object = MibTableColumn
cucsVnicFcLifInstanceId = _CucsVnicFcLifInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 13, 1, 1),
    _CucsVnicFcLifInstanceId_Type()
)
cucsVnicFcLifInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicFcLifInstanceId.setStatus("current")
_CucsVnicFcLifDn_Type = CucsManagedObjectDn
_CucsVnicFcLifDn_Object = MibTableColumn
cucsVnicFcLifDn = _CucsVnicFcLifDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 13, 1, 2),
    _CucsVnicFcLifDn_Type()
)
cucsVnicFcLifDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcLifDn.setStatus("current")
_CucsVnicFcLifRn_Type = SnmpAdminString
_CucsVnicFcLifRn_Object = MibTableColumn
cucsVnicFcLifRn = _CucsVnicFcLifRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 13, 1, 3),
    _CucsVnicFcLifRn_Type()
)
cucsVnicFcLifRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcLifRn.setStatus("current")
_CucsVnicFcLifAddr_Type = Unsigned64
_CucsVnicFcLifAddr_Object = MibTableColumn
cucsVnicFcLifAddr = _CucsVnicFcLifAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 13, 1, 4),
    _CucsVnicFcLifAddr_Type()
)
cucsVnicFcLifAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcLifAddr.setStatus("current")
_CucsVnicFcLifName_Type = SnmpAdminString
_CucsVnicFcLifName_Object = MibTableColumn
cucsVnicFcLifName = _CucsVnicFcLifName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 13, 1, 5),
    _CucsVnicFcLifName_Type()
)
cucsVnicFcLifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcLifName.setStatus("current")
_CucsVnicFcLifNicDn_Type = SnmpAdminString
_CucsVnicFcLifNicDn_Object = MibTableColumn
cucsVnicFcLifNicDn = _CucsVnicFcLifNicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 13, 1, 6),
    _CucsVnicFcLifNicDn_Type()
)
cucsVnicFcLifNicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcLifNicDn.setStatus("current")
_CucsVnicFcLifOwner_Type = CucsVnicConnectionOwner
_CucsVnicFcLifOwner_Object = MibTableColumn
cucsVnicFcLifOwner = _CucsVnicFcLifOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 13, 1, 7),
    _CucsVnicFcLifOwner_Type()
)
cucsVnicFcLifOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcLifOwner.setStatus("current")
_CucsVnicFcLifSwitchId_Type = CucsNetworkSwitchId
_CucsVnicFcLifSwitchId_Object = MibTableColumn
cucsVnicFcLifSwitchId = _CucsVnicFcLifSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 13, 1, 8),
    _CucsVnicFcLifSwitchId_Type()
)
cucsVnicFcLifSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcLifSwitchId.setStatus("current")
_CucsVnicFcLifType_Type = CucsVnicConnectionType
_CucsVnicFcLifType_Object = MibTableColumn
cucsVnicFcLifType = _CucsVnicFcLifType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 13, 1, 9),
    _CucsVnicFcLifType_Type()
)
cucsVnicFcLifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcLifType.setStatus("current")
_CucsVnicFcLifVnicDn_Type = SnmpAdminString
_CucsVnicFcLifVnicDn_Object = MibTableColumn
cucsVnicFcLifVnicDn = _CucsVnicFcLifVnicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 13, 1, 10),
    _CucsVnicFcLifVnicDn_Type()
)
cucsVnicFcLifVnicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcLifVnicDn.setStatus("current")
_CucsVnicFcNodeTable_Object = MibTable
cucsVnicFcNodeTable = _CucsVnicFcNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 14)
)
if mibBuilder.loadTexts:
    cucsVnicFcNodeTable.setStatus("current")
_CucsVnicFcNodeEntry_Object = MibTableRow
cucsVnicFcNodeEntry = _CucsVnicFcNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 14, 1)
)
cucsVnicFcNodeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicFcNodeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicFcNodeEntry.setStatus("current")
_CucsVnicFcNodeInstanceId_Type = CucsManagedObjectId
_CucsVnicFcNodeInstanceId_Object = MibTableColumn
cucsVnicFcNodeInstanceId = _CucsVnicFcNodeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 14, 1, 1),
    _CucsVnicFcNodeInstanceId_Type()
)
cucsVnicFcNodeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicFcNodeInstanceId.setStatus("current")
_CucsVnicFcNodeDn_Type = CucsManagedObjectDn
_CucsVnicFcNodeDn_Object = MibTableColumn
cucsVnicFcNodeDn = _CucsVnicFcNodeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 14, 1, 2),
    _CucsVnicFcNodeDn_Type()
)
cucsVnicFcNodeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcNodeDn.setStatus("current")
_CucsVnicFcNodeRn_Type = SnmpAdminString
_CucsVnicFcNodeRn_Object = MibTableColumn
cucsVnicFcNodeRn = _CucsVnicFcNodeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 14, 1, 3),
    _CucsVnicFcNodeRn_Type()
)
cucsVnicFcNodeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcNodeRn.setStatus("current")
_CucsVnicFcNodeAddr_Type = Unsigned64
_CucsVnicFcNodeAddr_Object = MibTableColumn
cucsVnicFcNodeAddr = _CucsVnicFcNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 14, 1, 4),
    _CucsVnicFcNodeAddr_Type()
)
cucsVnicFcNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcNodeAddr.setStatus("current")
_CucsVnicFcNodeFltAggr_Type = Unsigned64
_CucsVnicFcNodeFltAggr_Object = MibTableColumn
cucsVnicFcNodeFltAggr = _CucsVnicFcNodeFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 14, 1, 5),
    _CucsVnicFcNodeFltAggr_Type()
)
cucsVnicFcNodeFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcNodeFltAggr.setStatus("current")
_CucsVnicFcNodeIdentPoolName_Type = SnmpAdminString
_CucsVnicFcNodeIdentPoolName_Object = MibTableColumn
cucsVnicFcNodeIdentPoolName = _CucsVnicFcNodeIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 14, 1, 6),
    _CucsVnicFcNodeIdentPoolName_Type()
)
cucsVnicFcNodeIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcNodeIdentPoolName.setStatus("current")
_CucsVnicFcNodeOperIdentPoolName_Type = SnmpAdminString
_CucsVnicFcNodeOperIdentPoolName_Object = MibTableColumn
cucsVnicFcNodeOperIdentPoolName = _CucsVnicFcNodeOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 14, 1, 7),
    _CucsVnicFcNodeOperIdentPoolName_Type()
)
cucsVnicFcNodeOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcNodeOperIdentPoolName.setStatus("current")
_CucsVnicFcNodeMaxDerivableWWPN_Type = Gauge32
_CucsVnicFcNodeMaxDerivableWWPN_Object = MibTableColumn
cucsVnicFcNodeMaxDerivableWWPN = _CucsVnicFcNodeMaxDerivableWWPN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 14, 1, 8),
    _CucsVnicFcNodeMaxDerivableWWPN_Type()
)
cucsVnicFcNodeMaxDerivableWWPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcNodeMaxDerivableWWPN.setStatus("current")
_CucsVnicFcNodeOwner_Type = CucsVnicFcNodeOwner
_CucsVnicFcNodeOwner_Object = MibTableColumn
cucsVnicFcNodeOwner = _CucsVnicFcNodeOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 14, 1, 9),
    _CucsVnicFcNodeOwner_Type()
)
cucsVnicFcNodeOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcNodeOwner.setStatus("current")
_CucsVnicFcOEIfTable_Object = MibTable
cucsVnicFcOEIfTable = _CucsVnicFcOEIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15)
)
if mibBuilder.loadTexts:
    cucsVnicFcOEIfTable.setStatus("current")
_CucsVnicFcOEIfEntry_Object = MibTableRow
cucsVnicFcOEIfEntry = _CucsVnicFcOEIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1)
)
cucsVnicFcOEIfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicFcOEIfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicFcOEIfEntry.setStatus("current")
_CucsVnicFcOEIfInstanceId_Type = CucsManagedObjectId
_CucsVnicFcOEIfInstanceId_Object = MibTableColumn
cucsVnicFcOEIfInstanceId = _CucsVnicFcOEIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1, 1),
    _CucsVnicFcOEIfInstanceId_Type()
)
cucsVnicFcOEIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicFcOEIfInstanceId.setStatus("current")
_CucsVnicFcOEIfDn_Type = CucsManagedObjectDn
_CucsVnicFcOEIfDn_Object = MibTableColumn
cucsVnicFcOEIfDn = _CucsVnicFcOEIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1, 2),
    _CucsVnicFcOEIfDn_Type()
)
cucsVnicFcOEIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOEIfDn.setStatus("current")
_CucsVnicFcOEIfRn_Type = SnmpAdminString
_CucsVnicFcOEIfRn_Object = MibTableColumn
cucsVnicFcOEIfRn = _CucsVnicFcOEIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1, 3),
    _CucsVnicFcOEIfRn_Type()
)
cucsVnicFcOEIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOEIfRn.setStatus("current")
_CucsVnicFcOEIfInitiator_Type = Unsigned64
_CucsVnicFcOEIfInitiator_Object = MibTableColumn
cucsVnicFcOEIfInitiator = _CucsVnicFcOEIfInitiator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1, 4),
    _CucsVnicFcOEIfInitiator_Type()
)
cucsVnicFcOEIfInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOEIfInitiator.setStatus("current")
_CucsVnicFcOEIfName_Type = SnmpAdminString
_CucsVnicFcOEIfName_Object = MibTableColumn
cucsVnicFcOEIfName = _CucsVnicFcOEIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1, 5),
    _CucsVnicFcOEIfName_Type()
)
cucsVnicFcOEIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOEIfName.setStatus("current")
_CucsVnicFcOEIfOperState_Type = CucsVnicIfOperState
_CucsVnicFcOEIfOperState_Object = MibTableColumn
cucsVnicFcOEIfOperState = _CucsVnicFcOEIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1, 6),
    _CucsVnicFcOEIfOperState_Type()
)
cucsVnicFcOEIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOEIfOperState.setStatus("current")
_CucsVnicFcOEIfOwner_Type = CucsVnicConnectionOwner
_CucsVnicFcOEIfOwner_Object = MibTableColumn
cucsVnicFcOEIfOwner = _CucsVnicFcOEIfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1, 7),
    _CucsVnicFcOEIfOwner_Type()
)
cucsVnicFcOEIfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOEIfOwner.setStatus("current")
_CucsVnicFcOEIfSwitchId_Type = CucsVnicAFcIfSwitchId
_CucsVnicFcOEIfSwitchId_Object = MibTableColumn
cucsVnicFcOEIfSwitchId = _CucsVnicFcOEIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1, 8),
    _CucsVnicFcOEIfSwitchId_Type()
)
cucsVnicFcOEIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOEIfSwitchId.setStatus("current")
_CucsVnicFcOEIfType_Type = CucsVnicAFcIfType
_CucsVnicFcOEIfType_Object = MibTableColumn
cucsVnicFcOEIfType = _CucsVnicFcOEIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1, 9),
    _CucsVnicFcOEIfType_Type()
)
cucsVnicFcOEIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOEIfType.setStatus("current")
_CucsVnicFcOEIfVnet_Type = Gauge32
_CucsVnicFcOEIfVnet_Object = MibTableColumn
cucsVnicFcOEIfVnet = _CucsVnicFcOEIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1, 10),
    _CucsVnicFcOEIfVnet_Type()
)
cucsVnicFcOEIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOEIfVnet.setStatus("current")
_CucsVnicFcOEIfConfigQualifier_Type = CucsVnicConfigIssues
_CucsVnicFcOEIfConfigQualifier_Object = MibTableColumn
cucsVnicFcOEIfConfigQualifier = _CucsVnicFcOEIfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1, 11),
    _CucsVnicFcOEIfConfigQualifier_Type()
)
cucsVnicFcOEIfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOEIfConfigQualifier.setStatus("current")
_CucsVnicFcOEIfOperVnetDn_Type = SnmpAdminString
_CucsVnicFcOEIfOperVnetDn_Object = MibTableColumn
cucsVnicFcOEIfOperVnetDn = _CucsVnicFcOEIfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1, 13),
    _CucsVnicFcOEIfOperVnetDn_Type()
)
cucsVnicFcOEIfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOEIfOperVnetDn.setStatus("current")
_CucsVnicFcOEIfOperVnetName_Type = SnmpAdminString
_CucsVnicFcOEIfOperVnetName_Object = MibTableColumn
cucsVnicFcOEIfOperVnetName = _CucsVnicFcOEIfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1, 14),
    _CucsVnicFcOEIfOperVnetName_Type()
)
cucsVnicFcOEIfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOEIfOperVnetName.setStatus("current")
_CucsVnicFcOEIfPubNwId_Type = Gauge32
_CucsVnicFcOEIfPubNwId_Object = MibTableColumn
cucsVnicFcOEIfPubNwId = _CucsVnicFcOEIfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1, 15),
    _CucsVnicFcOEIfPubNwId_Type()
)
cucsVnicFcOEIfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOEIfPubNwId.setStatus("current")
_CucsVnicFcOEIfSharing_Type = CucsFabricVlanSharingType
_CucsVnicFcOEIfSharing_Object = MibTableColumn
cucsVnicFcOEIfSharing = _CucsVnicFcOEIfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1, 16),
    _CucsVnicFcOEIfSharing_Type()
)
cucsVnicFcOEIfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOEIfSharing.setStatus("current")
_CucsVnicFcOEIfOperPrimaryVnetDn_Type = SnmpAdminString
_CucsVnicFcOEIfOperPrimaryVnetDn_Object = MibTableColumn
cucsVnicFcOEIfOperPrimaryVnetDn = _CucsVnicFcOEIfOperPrimaryVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1, 17),
    _CucsVnicFcOEIfOperPrimaryVnetDn_Type()
)
cucsVnicFcOEIfOperPrimaryVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOEIfOperPrimaryVnetDn.setStatus("current")
_CucsVnicFcOEIfOperPrimaryVnetName_Type = SnmpAdminString
_CucsVnicFcOEIfOperPrimaryVnetName_Object = MibTableColumn
cucsVnicFcOEIfOperPrimaryVnetName = _CucsVnicFcOEIfOperPrimaryVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 15, 1, 18),
    _CucsVnicFcOEIfOperPrimaryVnetName_Type()
)
cucsVnicFcOEIfOperPrimaryVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcOEIfOperPrimaryVnetName.setStatus("current")
_CucsVnicIPv4DhcpTable_Object = MibTable
cucsVnicIPv4DhcpTable = _CucsVnicIPv4DhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 16)
)
if mibBuilder.loadTexts:
    cucsVnicIPv4DhcpTable.setStatus("current")
_CucsVnicIPv4DhcpEntry_Object = MibTableRow
cucsVnicIPv4DhcpEntry = _CucsVnicIPv4DhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 16, 1)
)
cucsVnicIPv4DhcpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIPv4DhcpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIPv4DhcpEntry.setStatus("current")
_CucsVnicIPv4DhcpInstanceId_Type = CucsManagedObjectId
_CucsVnicIPv4DhcpInstanceId_Object = MibTableColumn
cucsVnicIPv4DhcpInstanceId = _CucsVnicIPv4DhcpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 16, 1, 1),
    _CucsVnicIPv4DhcpInstanceId_Type()
)
cucsVnicIPv4DhcpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIPv4DhcpInstanceId.setStatus("current")
_CucsVnicIPv4DhcpDn_Type = CucsManagedObjectDn
_CucsVnicIPv4DhcpDn_Object = MibTableColumn
cucsVnicIPv4DhcpDn = _CucsVnicIPv4DhcpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 16, 1, 2),
    _CucsVnicIPv4DhcpDn_Type()
)
cucsVnicIPv4DhcpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4DhcpDn.setStatus("current")
_CucsVnicIPv4DhcpRn_Type = SnmpAdminString
_CucsVnicIPv4DhcpRn_Object = MibTableColumn
cucsVnicIPv4DhcpRn = _CucsVnicIPv4DhcpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 16, 1, 3),
    _CucsVnicIPv4DhcpRn_Type()
)
cucsVnicIPv4DhcpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4DhcpRn.setStatus("current")
_CucsVnicIPv4DhcpAddr_Type = InetAddressIPv4
_CucsVnicIPv4DhcpAddr_Object = MibTableColumn
cucsVnicIPv4DhcpAddr = _CucsVnicIPv4DhcpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 16, 1, 4),
    _CucsVnicIPv4DhcpAddr_Type()
)
cucsVnicIPv4DhcpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4DhcpAddr.setStatus("current")
_CucsVnicIPv4DhcpDefGw_Type = InetAddressIPv4
_CucsVnicIPv4DhcpDefGw_Object = MibTableColumn
cucsVnicIPv4DhcpDefGw = _CucsVnicIPv4DhcpDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 16, 1, 5),
    _CucsVnicIPv4DhcpDefGw_Type()
)
cucsVnicIPv4DhcpDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4DhcpDefGw.setStatus("current")
_CucsVnicIPv4DhcpSubnet_Type = InetAddressIPv4
_CucsVnicIPv4DhcpSubnet_Object = MibTableColumn
cucsVnicIPv4DhcpSubnet = _CucsVnicIPv4DhcpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 16, 1, 6),
    _CucsVnicIPv4DhcpSubnet_Type()
)
cucsVnicIPv4DhcpSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4DhcpSubnet.setStatus("current")
_CucsVnicIPv4DnsTable_Object = MibTable
cucsVnicIPv4DnsTable = _CucsVnicIPv4DnsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 17)
)
if mibBuilder.loadTexts:
    cucsVnicIPv4DnsTable.setStatus("current")
_CucsVnicIPv4DnsEntry_Object = MibTableRow
cucsVnicIPv4DnsEntry = _CucsVnicIPv4DnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 17, 1)
)
cucsVnicIPv4DnsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIPv4DnsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIPv4DnsEntry.setStatus("current")
_CucsVnicIPv4DnsInstanceId_Type = CucsManagedObjectId
_CucsVnicIPv4DnsInstanceId_Object = MibTableColumn
cucsVnicIPv4DnsInstanceId = _CucsVnicIPv4DnsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 17, 1, 1),
    _CucsVnicIPv4DnsInstanceId_Type()
)
cucsVnicIPv4DnsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIPv4DnsInstanceId.setStatus("current")
_CucsVnicIPv4DnsDn_Type = CucsManagedObjectDn
_CucsVnicIPv4DnsDn_Object = MibTableColumn
cucsVnicIPv4DnsDn = _CucsVnicIPv4DnsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 17, 1, 2),
    _CucsVnicIPv4DnsDn_Type()
)
cucsVnicIPv4DnsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4DnsDn.setStatus("current")
_CucsVnicIPv4DnsRn_Type = SnmpAdminString
_CucsVnicIPv4DnsRn_Object = MibTableColumn
cucsVnicIPv4DnsRn = _CucsVnicIPv4DnsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 17, 1, 3),
    _CucsVnicIPv4DnsRn_Type()
)
cucsVnicIPv4DnsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4DnsRn.setStatus("current")
_CucsVnicIPv4DnsAddr_Type = InetAddressIPv4
_CucsVnicIPv4DnsAddr_Object = MibTableColumn
cucsVnicIPv4DnsAddr = _CucsVnicIPv4DnsAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 17, 1, 4),
    _CucsVnicIPv4DnsAddr_Type()
)
cucsVnicIPv4DnsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4DnsAddr.setStatus("current")
_CucsVnicIPv4DnsDefGw_Type = InetAddressIPv4
_CucsVnicIPv4DnsDefGw_Object = MibTableColumn
cucsVnicIPv4DnsDefGw = _CucsVnicIPv4DnsDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 17, 1, 5),
    _CucsVnicIPv4DnsDefGw_Type()
)
cucsVnicIPv4DnsDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4DnsDefGw.setStatus("current")
_CucsVnicIPv4DnsPref_Type = CucsVnicIPv4DnsPref
_CucsVnicIPv4DnsPref_Object = MibTableColumn
cucsVnicIPv4DnsPref = _CucsVnicIPv4DnsPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 17, 1, 6),
    _CucsVnicIPv4DnsPref_Type()
)
cucsVnicIPv4DnsPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4DnsPref.setStatus("current")
_CucsVnicIPv4DnsSubnet_Type = InetAddressIPv4
_CucsVnicIPv4DnsSubnet_Object = MibTableColumn
cucsVnicIPv4DnsSubnet = _CucsVnicIPv4DnsSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 17, 1, 7),
    _CucsVnicIPv4DnsSubnet_Type()
)
cucsVnicIPv4DnsSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4DnsSubnet.setStatus("current")
_CucsVnicIPv4IfTable_Object = MibTable
cucsVnicIPv4IfTable = _CucsVnicIPv4IfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18)
)
if mibBuilder.loadTexts:
    cucsVnicIPv4IfTable.setStatus("current")
_CucsVnicIPv4IfEntry_Object = MibTableRow
cucsVnicIPv4IfEntry = _CucsVnicIPv4IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1)
)
cucsVnicIPv4IfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIPv4IfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIPv4IfEntry.setStatus("current")
_CucsVnicIPv4IfInstanceId_Type = CucsManagedObjectId
_CucsVnicIPv4IfInstanceId_Object = MibTableColumn
cucsVnicIPv4IfInstanceId = _CucsVnicIPv4IfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 1),
    _CucsVnicIPv4IfInstanceId_Type()
)
cucsVnicIPv4IfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfInstanceId.setStatus("current")
_CucsVnicIPv4IfDn_Type = CucsManagedObjectDn
_CucsVnicIPv4IfDn_Object = MibTableColumn
cucsVnicIPv4IfDn = _CucsVnicIPv4IfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 2),
    _CucsVnicIPv4IfDn_Type()
)
cucsVnicIPv4IfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfDn.setStatus("current")
_CucsVnicIPv4IfRn_Type = SnmpAdminString
_CucsVnicIPv4IfRn_Object = MibTableColumn
cucsVnicIPv4IfRn = _CucsVnicIPv4IfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 3),
    _CucsVnicIPv4IfRn_Type()
)
cucsVnicIPv4IfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfRn.setStatus("current")
_CucsVnicIPv4IfAddr_Type = InetAddressIPv4
_CucsVnicIPv4IfAddr_Object = MibTableColumn
cucsVnicIPv4IfAddr = _CucsVnicIPv4IfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 4),
    _CucsVnicIPv4IfAddr_Type()
)
cucsVnicIPv4IfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfAddr.setStatus("current")
_CucsVnicIPv4IfName_Type = SnmpAdminString
_CucsVnicIPv4IfName_Object = MibTableColumn
cucsVnicIPv4IfName = _CucsVnicIPv4IfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 5),
    _CucsVnicIPv4IfName_Type()
)
cucsVnicIPv4IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfName.setStatus("current")
_CucsVnicIPv4IfOperState_Type = CucsVnicIfOperState
_CucsVnicIPv4IfOperState_Object = MibTableColumn
cucsVnicIPv4IfOperState = _CucsVnicIPv4IfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 6),
    _CucsVnicIPv4IfOperState_Type()
)
cucsVnicIPv4IfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfOperState.setStatus("current")
_CucsVnicIPv4IfOwner_Type = CucsVnicConnectionOwner
_CucsVnicIPv4IfOwner_Object = MibTableColumn
cucsVnicIPv4IfOwner = _CucsVnicIPv4IfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 7),
    _CucsVnicIPv4IfOwner_Type()
)
cucsVnicIPv4IfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfOwner.setStatus("current")
_CucsVnicIPv4IfSwitchId_Type = CucsNetworkSwitchId
_CucsVnicIPv4IfSwitchId_Object = MibTableColumn
cucsVnicIPv4IfSwitchId = _CucsVnicIPv4IfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 8),
    _CucsVnicIPv4IfSwitchId_Type()
)
cucsVnicIPv4IfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfSwitchId.setStatus("current")
_CucsVnicIPv4IfType_Type = CucsVnicConnectionType
_CucsVnicIPv4IfType_Object = MibTableColumn
cucsVnicIPv4IfType = _CucsVnicIPv4IfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 9),
    _CucsVnicIPv4IfType_Type()
)
cucsVnicIPv4IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfType.setStatus("current")
_CucsVnicIPv4IfVnet_Type = Gauge32
_CucsVnicIPv4IfVnet_Object = MibTableColumn
cucsVnicIPv4IfVnet = _CucsVnicIPv4IfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 10),
    _CucsVnicIPv4IfVnet_Type()
)
cucsVnicIPv4IfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfVnet.setStatus("current")
_CucsVnicIPv4IfConfigQualifier_Type = CucsVnicConfigIssues
_CucsVnicIPv4IfConfigQualifier_Object = MibTableColumn
cucsVnicIPv4IfConfigQualifier = _CucsVnicIPv4IfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 11),
    _CucsVnicIPv4IfConfigQualifier_Type()
)
cucsVnicIPv4IfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfConfigQualifier.setStatus("current")
_CucsVnicIPv4IfOperVnetDn_Type = SnmpAdminString
_CucsVnicIPv4IfOperVnetDn_Object = MibTableColumn
cucsVnicIPv4IfOperVnetDn = _CucsVnicIPv4IfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 13),
    _CucsVnicIPv4IfOperVnetDn_Type()
)
cucsVnicIPv4IfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfOperVnetDn.setStatus("current")
_CucsVnicIPv4IfOperVnetName_Type = SnmpAdminString
_CucsVnicIPv4IfOperVnetName_Object = MibTableColumn
cucsVnicIPv4IfOperVnetName = _CucsVnicIPv4IfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 14),
    _CucsVnicIPv4IfOperVnetName_Type()
)
cucsVnicIPv4IfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfOperVnetName.setStatus("current")
_CucsVnicIPv4IfPubNwId_Type = Gauge32
_CucsVnicIPv4IfPubNwId_Object = MibTableColumn
cucsVnicIPv4IfPubNwId = _CucsVnicIPv4IfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 15),
    _CucsVnicIPv4IfPubNwId_Type()
)
cucsVnicIPv4IfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfPubNwId.setStatus("current")
_CucsVnicIPv4IfSharing_Type = CucsFabricVlanSharingType
_CucsVnicIPv4IfSharing_Object = MibTableColumn
cucsVnicIPv4IfSharing = _CucsVnicIPv4IfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 16),
    _CucsVnicIPv4IfSharing_Type()
)
cucsVnicIPv4IfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfSharing.setStatus("current")
_CucsVnicIPv4IfPropAcl_Type = Unsigned64
_CucsVnicIPv4IfPropAcl_Object = MibTableColumn
cucsVnicIPv4IfPropAcl = _CucsVnicIPv4IfPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 17),
    _CucsVnicIPv4IfPropAcl_Type()
)
cucsVnicIPv4IfPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfPropAcl.setStatus("current")
_CucsVnicIPv4IfOperPrimaryVnetDn_Type = SnmpAdminString
_CucsVnicIPv4IfOperPrimaryVnetDn_Object = MibTableColumn
cucsVnicIPv4IfOperPrimaryVnetDn = _CucsVnicIPv4IfOperPrimaryVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 18),
    _CucsVnicIPv4IfOperPrimaryVnetDn_Type()
)
cucsVnicIPv4IfOperPrimaryVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfOperPrimaryVnetDn.setStatus("current")
_CucsVnicIPv4IfOperPrimaryVnetName_Type = SnmpAdminString
_CucsVnicIPv4IfOperPrimaryVnetName_Object = MibTableColumn
cucsVnicIPv4IfOperPrimaryVnetName = _CucsVnicIPv4IfOperPrimaryVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 18, 1, 19),
    _CucsVnicIPv4IfOperPrimaryVnetName_Type()
)
cucsVnicIPv4IfOperPrimaryVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IfOperPrimaryVnetName.setStatus("current")
_CucsVnicIPv4StaticRouteTable_Object = MibTable
cucsVnicIPv4StaticRouteTable = _CucsVnicIPv4StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 19)
)
if mibBuilder.loadTexts:
    cucsVnicIPv4StaticRouteTable.setStatus("current")
_CucsVnicIPv4StaticRouteEntry_Object = MibTableRow
cucsVnicIPv4StaticRouteEntry = _CucsVnicIPv4StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 19, 1)
)
cucsVnicIPv4StaticRouteEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIPv4StaticRouteInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIPv4StaticRouteEntry.setStatus("current")
_CucsVnicIPv4StaticRouteInstanceId_Type = CucsManagedObjectId
_CucsVnicIPv4StaticRouteInstanceId_Object = MibTableColumn
cucsVnicIPv4StaticRouteInstanceId = _CucsVnicIPv4StaticRouteInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 19, 1, 1),
    _CucsVnicIPv4StaticRouteInstanceId_Type()
)
cucsVnicIPv4StaticRouteInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIPv4StaticRouteInstanceId.setStatus("current")
_CucsVnicIPv4StaticRouteDn_Type = CucsManagedObjectDn
_CucsVnicIPv4StaticRouteDn_Object = MibTableColumn
cucsVnicIPv4StaticRouteDn = _CucsVnicIPv4StaticRouteDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 19, 1, 2),
    _CucsVnicIPv4StaticRouteDn_Type()
)
cucsVnicIPv4StaticRouteDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4StaticRouteDn.setStatus("current")
_CucsVnicIPv4StaticRouteRn_Type = SnmpAdminString
_CucsVnicIPv4StaticRouteRn_Object = MibTableColumn
cucsVnicIPv4StaticRouteRn = _CucsVnicIPv4StaticRouteRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 19, 1, 3),
    _CucsVnicIPv4StaticRouteRn_Type()
)
cucsVnicIPv4StaticRouteRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4StaticRouteRn.setStatus("current")
_CucsVnicIPv4StaticRouteAddr_Type = InetAddressIPv4
_CucsVnicIPv4StaticRouteAddr_Object = MibTableColumn
cucsVnicIPv4StaticRouteAddr = _CucsVnicIPv4StaticRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 19, 1, 4),
    _CucsVnicIPv4StaticRouteAddr_Type()
)
cucsVnicIPv4StaticRouteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4StaticRouteAddr.setStatus("current")
_CucsVnicIPv4StaticRouteDefGw_Type = InetAddressIPv4
_CucsVnicIPv4StaticRouteDefGw_Object = MibTableColumn
cucsVnicIPv4StaticRouteDefGw = _CucsVnicIPv4StaticRouteDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 19, 1, 5),
    _CucsVnicIPv4StaticRouteDefGw_Type()
)
cucsVnicIPv4StaticRouteDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4StaticRouteDefGw.setStatus("current")
_CucsVnicIPv4StaticRouteGwAddr_Type = InetAddressIPv4
_CucsVnicIPv4StaticRouteGwAddr_Object = MibTableColumn
cucsVnicIPv4StaticRouteGwAddr = _CucsVnicIPv4StaticRouteGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 19, 1, 6),
    _CucsVnicIPv4StaticRouteGwAddr_Type()
)
cucsVnicIPv4StaticRouteGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4StaticRouteGwAddr.setStatus("current")
_CucsVnicIPv4StaticRouteGwSubnet_Type = InetAddressIPv4
_CucsVnicIPv4StaticRouteGwSubnet_Object = MibTableColumn
cucsVnicIPv4StaticRouteGwSubnet = _CucsVnicIPv4StaticRouteGwSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 19, 1, 7),
    _CucsVnicIPv4StaticRouteGwSubnet_Type()
)
cucsVnicIPv4StaticRouteGwSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4StaticRouteGwSubnet.setStatus("current")
_CucsVnicIPv4StaticRouteSubnet_Type = InetAddressIPv4
_CucsVnicIPv4StaticRouteSubnet_Object = MibTableColumn
cucsVnicIPv4StaticRouteSubnet = _CucsVnicIPv4StaticRouteSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 19, 1, 8),
    _CucsVnicIPv4StaticRouteSubnet_Type()
)
cucsVnicIPv4StaticRouteSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4StaticRouteSubnet.setStatus("current")
_CucsVnicIpV4PooledAddrTable_Object = MibTable
cucsVnicIpV4PooledAddrTable = _CucsVnicIpV4PooledAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 20)
)
if mibBuilder.loadTexts:
    cucsVnicIpV4PooledAddrTable.setStatus("current")
_CucsVnicIpV4PooledAddrEntry_Object = MibTableRow
cucsVnicIpV4PooledAddrEntry = _CucsVnicIpV4PooledAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 20, 1)
)
cucsVnicIpV4PooledAddrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIpV4PooledAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIpV4PooledAddrEntry.setStatus("current")
_CucsVnicIpV4PooledAddrInstanceId_Type = CucsManagedObjectId
_CucsVnicIpV4PooledAddrInstanceId_Object = MibTableColumn
cucsVnicIpV4PooledAddrInstanceId = _CucsVnicIpV4PooledAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 20, 1, 1),
    _CucsVnicIpV4PooledAddrInstanceId_Type()
)
cucsVnicIpV4PooledAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIpV4PooledAddrInstanceId.setStatus("current")
_CucsVnicIpV4PooledAddrDn_Type = CucsManagedObjectDn
_CucsVnicIpV4PooledAddrDn_Object = MibTableColumn
cucsVnicIpV4PooledAddrDn = _CucsVnicIpV4PooledAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 20, 1, 2),
    _CucsVnicIpV4PooledAddrDn_Type()
)
cucsVnicIpV4PooledAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4PooledAddrDn.setStatus("current")
_CucsVnicIpV4PooledAddrRn_Type = SnmpAdminString
_CucsVnicIpV4PooledAddrRn_Object = MibTableColumn
cucsVnicIpV4PooledAddrRn = _CucsVnicIpV4PooledAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 20, 1, 3),
    _CucsVnicIpV4PooledAddrRn_Type()
)
cucsVnicIpV4PooledAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4PooledAddrRn.setStatus("current")
_CucsVnicIpV4PooledAddrAddr_Type = InetAddressIPv4
_CucsVnicIpV4PooledAddrAddr_Object = MibTableColumn
cucsVnicIpV4PooledAddrAddr = _CucsVnicIpV4PooledAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 20, 1, 4),
    _CucsVnicIpV4PooledAddrAddr_Type()
)
cucsVnicIpV4PooledAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4PooledAddrAddr.setStatus("current")
_CucsVnicIpV4PooledAddrDefGw_Type = InetAddressIPv4
_CucsVnicIpV4PooledAddrDefGw_Object = MibTableColumn
cucsVnicIpV4PooledAddrDefGw = _CucsVnicIpV4PooledAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 20, 1, 5),
    _CucsVnicIpV4PooledAddrDefGw_Type()
)
cucsVnicIpV4PooledAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4PooledAddrDefGw.setStatus("current")
_CucsVnicIpV4PooledAddrName_Type = SnmpAdminString
_CucsVnicIpV4PooledAddrName_Object = MibTableColumn
cucsVnicIpV4PooledAddrName = _CucsVnicIpV4PooledAddrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 20, 1, 6),
    _CucsVnicIpV4PooledAddrName_Type()
)
cucsVnicIpV4PooledAddrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4PooledAddrName.setStatus("current")
_CucsVnicIpV4PooledAddrSubnet_Type = InetAddressIPv4
_CucsVnicIpV4PooledAddrSubnet_Object = MibTableColumn
cucsVnicIpV4PooledAddrSubnet = _CucsVnicIpV4PooledAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 20, 1, 7),
    _CucsVnicIpV4PooledAddrSubnet_Type()
)
cucsVnicIpV4PooledAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4PooledAddrSubnet.setStatus("current")
_CucsVnicIpV4PooledAddrOperName_Type = SnmpAdminString
_CucsVnicIpV4PooledAddrOperName_Object = MibTableColumn
cucsVnicIpV4PooledAddrOperName = _CucsVnicIpV4PooledAddrOperName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 20, 1, 8),
    _CucsVnicIpV4PooledAddrOperName_Type()
)
cucsVnicIpV4PooledAddrOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4PooledAddrOperName.setStatus("current")
_CucsVnicIpV4PooledAddrPrimDns_Type = InetAddressIPv4
_CucsVnicIpV4PooledAddrPrimDns_Object = MibTableColumn
cucsVnicIpV4PooledAddrPrimDns = _CucsVnicIpV4PooledAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 20, 1, 9),
    _CucsVnicIpV4PooledAddrPrimDns_Type()
)
cucsVnicIpV4PooledAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4PooledAddrPrimDns.setStatus("current")
_CucsVnicIpV4PooledAddrSecDns_Type = InetAddressIPv4
_CucsVnicIpV4PooledAddrSecDns_Object = MibTableColumn
cucsVnicIpV4PooledAddrSecDns = _CucsVnicIpV4PooledAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 20, 1, 10),
    _CucsVnicIpV4PooledAddrSecDns_Type()
)
cucsVnicIpV4PooledAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4PooledAddrSecDns.setStatus("current")
_CucsVnicIpV4ProfDerivedAddrTable_Object = MibTable
cucsVnicIpV4ProfDerivedAddrTable = _CucsVnicIpV4ProfDerivedAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 21)
)
if mibBuilder.loadTexts:
    cucsVnicIpV4ProfDerivedAddrTable.setStatus("current")
_CucsVnicIpV4ProfDerivedAddrEntry_Object = MibTableRow
cucsVnicIpV4ProfDerivedAddrEntry = _CucsVnicIpV4ProfDerivedAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 21, 1)
)
cucsVnicIpV4ProfDerivedAddrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIpV4ProfDerivedAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIpV4ProfDerivedAddrEntry.setStatus("current")
_CucsVnicIpV4ProfDerivedAddrInstanceId_Type = CucsManagedObjectId
_CucsVnicIpV4ProfDerivedAddrInstanceId_Object = MibTableColumn
cucsVnicIpV4ProfDerivedAddrInstanceId = _CucsVnicIpV4ProfDerivedAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 21, 1, 1),
    _CucsVnicIpV4ProfDerivedAddrInstanceId_Type()
)
cucsVnicIpV4ProfDerivedAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIpV4ProfDerivedAddrInstanceId.setStatus("current")
_CucsVnicIpV4ProfDerivedAddrDn_Type = CucsManagedObjectDn
_CucsVnicIpV4ProfDerivedAddrDn_Object = MibTableColumn
cucsVnicIpV4ProfDerivedAddrDn = _CucsVnicIpV4ProfDerivedAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 21, 1, 2),
    _CucsVnicIpV4ProfDerivedAddrDn_Type()
)
cucsVnicIpV4ProfDerivedAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4ProfDerivedAddrDn.setStatus("current")
_CucsVnicIpV4ProfDerivedAddrRn_Type = SnmpAdminString
_CucsVnicIpV4ProfDerivedAddrRn_Object = MibTableColumn
cucsVnicIpV4ProfDerivedAddrRn = _CucsVnicIpV4ProfDerivedAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 21, 1, 3),
    _CucsVnicIpV4ProfDerivedAddrRn_Type()
)
cucsVnicIpV4ProfDerivedAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4ProfDerivedAddrRn.setStatus("current")
_CucsVnicIpV4ProfDerivedAddrAddr_Type = InetAddressIPv4
_CucsVnicIpV4ProfDerivedAddrAddr_Object = MibTableColumn
cucsVnicIpV4ProfDerivedAddrAddr = _CucsVnicIpV4ProfDerivedAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 21, 1, 4),
    _CucsVnicIpV4ProfDerivedAddrAddr_Type()
)
cucsVnicIpV4ProfDerivedAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4ProfDerivedAddrAddr.setStatus("current")
_CucsVnicIpV4ProfDerivedAddrDefGw_Type = InetAddressIPv4
_CucsVnicIpV4ProfDerivedAddrDefGw_Object = MibTableColumn
cucsVnicIpV4ProfDerivedAddrDefGw = _CucsVnicIpV4ProfDerivedAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 21, 1, 5),
    _CucsVnicIpV4ProfDerivedAddrDefGw_Type()
)
cucsVnicIpV4ProfDerivedAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4ProfDerivedAddrDefGw.setStatus("current")
_CucsVnicIpV4ProfDerivedAddrSubnet_Type = InetAddressIPv4
_CucsVnicIpV4ProfDerivedAddrSubnet_Object = MibTableColumn
cucsVnicIpV4ProfDerivedAddrSubnet = _CucsVnicIpV4ProfDerivedAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 21, 1, 6),
    _CucsVnicIpV4ProfDerivedAddrSubnet_Type()
)
cucsVnicIpV4ProfDerivedAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4ProfDerivedAddrSubnet.setStatus("current")
_CucsVnicIpV4StaticAddrTable_Object = MibTable
cucsVnicIpV4StaticAddrTable = _CucsVnicIpV4StaticAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 22)
)
if mibBuilder.loadTexts:
    cucsVnicIpV4StaticAddrTable.setStatus("current")
_CucsVnicIpV4StaticAddrEntry_Object = MibTableRow
cucsVnicIpV4StaticAddrEntry = _CucsVnicIpV4StaticAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 22, 1)
)
cucsVnicIpV4StaticAddrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIpV4StaticAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIpV4StaticAddrEntry.setStatus("current")
_CucsVnicIpV4StaticAddrInstanceId_Type = CucsManagedObjectId
_CucsVnicIpV4StaticAddrInstanceId_Object = MibTableColumn
cucsVnicIpV4StaticAddrInstanceId = _CucsVnicIpV4StaticAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 22, 1, 1),
    _CucsVnicIpV4StaticAddrInstanceId_Type()
)
cucsVnicIpV4StaticAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIpV4StaticAddrInstanceId.setStatus("current")
_CucsVnicIpV4StaticAddrDn_Type = CucsManagedObjectDn
_CucsVnicIpV4StaticAddrDn_Object = MibTableColumn
cucsVnicIpV4StaticAddrDn = _CucsVnicIpV4StaticAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 22, 1, 2),
    _CucsVnicIpV4StaticAddrDn_Type()
)
cucsVnicIpV4StaticAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4StaticAddrDn.setStatus("current")
_CucsVnicIpV4StaticAddrRn_Type = SnmpAdminString
_CucsVnicIpV4StaticAddrRn_Object = MibTableColumn
cucsVnicIpV4StaticAddrRn = _CucsVnicIpV4StaticAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 22, 1, 3),
    _CucsVnicIpV4StaticAddrRn_Type()
)
cucsVnicIpV4StaticAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4StaticAddrRn.setStatus("current")
_CucsVnicIpV4StaticAddrAddr_Type = InetAddressIPv4
_CucsVnicIpV4StaticAddrAddr_Object = MibTableColumn
cucsVnicIpV4StaticAddrAddr = _CucsVnicIpV4StaticAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 22, 1, 4),
    _CucsVnicIpV4StaticAddrAddr_Type()
)
cucsVnicIpV4StaticAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4StaticAddrAddr.setStatus("current")
_CucsVnicIpV4StaticAddrDefGw_Type = InetAddressIPv4
_CucsVnicIpV4StaticAddrDefGw_Object = MibTableColumn
cucsVnicIpV4StaticAddrDefGw = _CucsVnicIpV4StaticAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 22, 1, 5),
    _CucsVnicIpV4StaticAddrDefGw_Type()
)
cucsVnicIpV4StaticAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4StaticAddrDefGw.setStatus("current")
_CucsVnicIpV4StaticAddrSubnet_Type = InetAddressIPv4
_CucsVnicIpV4StaticAddrSubnet_Object = MibTableColumn
cucsVnicIpV4StaticAddrSubnet = _CucsVnicIpV4StaticAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 22, 1, 6),
    _CucsVnicIpV4StaticAddrSubnet_Type()
)
cucsVnicIpV4StaticAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4StaticAddrSubnet.setStatus("current")
_CucsVnicIpV4StaticAddrPrimDns_Type = InetAddressIPv4
_CucsVnicIpV4StaticAddrPrimDns_Object = MibTableColumn
cucsVnicIpV4StaticAddrPrimDns = _CucsVnicIpV4StaticAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 22, 1, 7),
    _CucsVnicIpV4StaticAddrPrimDns_Type()
)
cucsVnicIpV4StaticAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4StaticAddrPrimDns.setStatus("current")
_CucsVnicIpV4StaticAddrSecDns_Type = InetAddressIPv4
_CucsVnicIpV4StaticAddrSecDns_Object = MibTableColumn
cucsVnicIpV4StaticAddrSecDns = _CucsVnicIpV4StaticAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 22, 1, 8),
    _CucsVnicIpV4StaticAddrSecDns_Type()
)
cucsVnicIpV4StaticAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4StaticAddrSecDns.setStatus("current")
_CucsVnicIpcTable_Object = MibTable
cucsVnicIpcTable = _CucsVnicIpcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23)
)
if mibBuilder.loadTexts:
    cucsVnicIpcTable.setStatus("current")
_CucsVnicIpcEntry_Object = MibTableRow
cucsVnicIpcEntry = _CucsVnicIpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1)
)
cucsVnicIpcEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIpcInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIpcEntry.setStatus("current")
_CucsVnicIpcInstanceId_Type = CucsManagedObjectId
_CucsVnicIpcInstanceId_Object = MibTableColumn
cucsVnicIpcInstanceId = _CucsVnicIpcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 1),
    _CucsVnicIpcInstanceId_Type()
)
cucsVnicIpcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIpcInstanceId.setStatus("current")
_CucsVnicIpcDn_Type = CucsManagedObjectDn
_CucsVnicIpcDn_Object = MibTableColumn
cucsVnicIpcDn = _CucsVnicIpcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 2),
    _CucsVnicIpcDn_Type()
)
cucsVnicIpcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcDn.setStatus("current")
_CucsVnicIpcRn_Type = SnmpAdminString
_CucsVnicIpcRn_Object = MibTableColumn
cucsVnicIpcRn = _CucsVnicIpcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 3),
    _CucsVnicIpcRn_Type()
)
cucsVnicIpcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcRn.setStatus("current")
_CucsVnicIpcAdaptorProfileName_Type = SnmpAdminString
_CucsVnicIpcAdaptorProfileName_Object = MibTableColumn
cucsVnicIpcAdaptorProfileName = _CucsVnicIpcAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 4),
    _CucsVnicIpcAdaptorProfileName_Type()
)
cucsVnicIpcAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcAdaptorProfileName.setStatus("current")
_CucsVnicIpcAddr_Type = MacAddress
_CucsVnicIpcAddr_Object = MibTableColumn
cucsVnicIpcAddr = _CucsVnicIpcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 5),
    _CucsVnicIpcAddr_Type()
)
cucsVnicIpcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcAddr.setStatus("current")
_CucsVnicIpcAdminVcon_Type = SnmpAdminString
_CucsVnicIpcAdminVcon_Object = MibTableColumn
cucsVnicIpcAdminVcon = _CucsVnicIpcAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 6),
    _CucsVnicIpcAdminVcon_Type()
)
cucsVnicIpcAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcAdminVcon.setStatus("current")
_CucsVnicIpcBootDev_Type = CucsVnicVnicBootDev
_CucsVnicIpcBootDev_Object = MibTableColumn
cucsVnicIpcBootDev = _CucsVnicIpcBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 7),
    _CucsVnicIpcBootDev_Type()
)
cucsVnicIpcBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcBootDev.setStatus("current")
_CucsVnicIpcConfigState_Type = CucsLsConfigState
_CucsVnicIpcConfigState_Object = MibTableColumn
cucsVnicIpcConfigState = _CucsVnicIpcConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 8),
    _CucsVnicIpcConfigState_Type()
)
cucsVnicIpcConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcConfigState.setStatus("current")
_CucsVnicIpcEquipmentDn_Type = SnmpAdminString
_CucsVnicIpcEquipmentDn_Object = MibTableColumn
cucsVnicIpcEquipmentDn = _CucsVnicIpcEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 9),
    _CucsVnicIpcEquipmentDn_Type()
)
cucsVnicIpcEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcEquipmentDn.setStatus("current")
_CucsVnicIpcIdentPoolName_Type = SnmpAdminString
_CucsVnicIpcIdentPoolName_Object = MibTableColumn
cucsVnicIpcIdentPoolName = _CucsVnicIpcIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 10),
    _CucsVnicIpcIdentPoolName_Type()
)
cucsVnicIpcIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIdentPoolName.setStatus("current")
_CucsVnicIpcInstType_Type = CucsVnicInstantiation
_CucsVnicIpcInstType_Object = MibTableColumn
cucsVnicIpcInstType = _CucsVnicIpcInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 11),
    _CucsVnicIpcInstType_Type()
)
cucsVnicIpcInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcInstType.setStatus("current")
_CucsVnicIpcMtu_Type = Gauge32
_CucsVnicIpcMtu_Object = MibTableColumn
cucsVnicIpcMtu = _CucsVnicIpcMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 12),
    _CucsVnicIpcMtu_Type()
)
cucsVnicIpcMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcMtu.setStatus("current")
_CucsVnicIpcName_Type = SnmpAdminString
_CucsVnicIpcName_Object = MibTableColumn
cucsVnicIpcName = _CucsVnicIpcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 13),
    _CucsVnicIpcName_Type()
)
cucsVnicIpcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcName.setStatus("current")
_CucsVnicIpcNwCtrlPolicyName_Type = SnmpAdminString
_CucsVnicIpcNwCtrlPolicyName_Object = MibTableColumn
cucsVnicIpcNwCtrlPolicyName = _CucsVnicIpcNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 14),
    _CucsVnicIpcNwCtrlPolicyName_Type()
)
cucsVnicIpcNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcNwCtrlPolicyName.setStatus("current")
_CucsVnicIpcNwTemplName_Type = SnmpAdminString
_CucsVnicIpcNwTemplName_Object = MibTableColumn
cucsVnicIpcNwTemplName = _CucsVnicIpcNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 15),
    _CucsVnicIpcNwTemplName_Type()
)
cucsVnicIpcNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcNwTemplName.setStatus("current")
_CucsVnicIpcOperAdaptorProfileName_Type = SnmpAdminString
_CucsVnicIpcOperAdaptorProfileName_Object = MibTableColumn
cucsVnicIpcOperAdaptorProfileName = _CucsVnicIpcOperAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 16),
    _CucsVnicIpcOperAdaptorProfileName_Type()
)
cucsVnicIpcOperAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcOperAdaptorProfileName.setStatus("current")
_CucsVnicIpcOperIdentPoolName_Type = SnmpAdminString
_CucsVnicIpcOperIdentPoolName_Object = MibTableColumn
cucsVnicIpcOperIdentPoolName = _CucsVnicIpcOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 17),
    _CucsVnicIpcOperIdentPoolName_Type()
)
cucsVnicIpcOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcOperIdentPoolName.setStatus("current")
_CucsVnicIpcOperNwCtrlPolicyName_Type = SnmpAdminString
_CucsVnicIpcOperNwCtrlPolicyName_Object = MibTableColumn
cucsVnicIpcOperNwCtrlPolicyName = _CucsVnicIpcOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 18),
    _CucsVnicIpcOperNwCtrlPolicyName_Type()
)
cucsVnicIpcOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcOperNwCtrlPolicyName.setStatus("current")
_CucsVnicIpcOperNwTemplName_Type = SnmpAdminString
_CucsVnicIpcOperNwTemplName_Object = MibTableColumn
cucsVnicIpcOperNwTemplName = _CucsVnicIpcOperNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 19),
    _CucsVnicIpcOperNwTemplName_Type()
)
cucsVnicIpcOperNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcOperNwTemplName.setStatus("current")
_CucsVnicIpcOperOrder_Type = Gauge32
_CucsVnicIpcOperOrder_Object = MibTableColumn
cucsVnicIpcOperOrder = _CucsVnicIpcOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 20),
    _CucsVnicIpcOperOrder_Type()
)
cucsVnicIpcOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcOperOrder.setStatus("current")
_CucsVnicIpcOperQosPolicyName_Type = SnmpAdminString
_CucsVnicIpcOperQosPolicyName_Object = MibTableColumn
cucsVnicIpcOperQosPolicyName = _CucsVnicIpcOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 21),
    _CucsVnicIpcOperQosPolicyName_Type()
)
cucsVnicIpcOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcOperQosPolicyName.setStatus("current")
_CucsVnicIpcOperSpeed_Type = Gauge32
_CucsVnicIpcOperSpeed_Object = MibTableColumn
cucsVnicIpcOperSpeed = _CucsVnicIpcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 22),
    _CucsVnicIpcOperSpeed_Type()
)
cucsVnicIpcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcOperSpeed.setStatus("current")
_CucsVnicIpcOperStatsPolicyName_Type = SnmpAdminString
_CucsVnicIpcOperStatsPolicyName_Object = MibTableColumn
cucsVnicIpcOperStatsPolicyName = _CucsVnicIpcOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 23),
    _CucsVnicIpcOperStatsPolicyName_Type()
)
cucsVnicIpcOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcOperStatsPolicyName.setStatus("current")
_CucsVnicIpcOperVcon_Type = SnmpAdminString
_CucsVnicIpcOperVcon_Object = MibTableColumn
cucsVnicIpcOperVcon = _CucsVnicIpcOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 24),
    _CucsVnicIpcOperVcon_Type()
)
cucsVnicIpcOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcOperVcon.setStatus("current")
_CucsVnicIpcOrder_Type = Gauge32
_CucsVnicIpcOrder_Object = MibTableColumn
cucsVnicIpcOrder = _CucsVnicIpcOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 25),
    _CucsVnicIpcOrder_Type()
)
cucsVnicIpcOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcOrder.setStatus("current")
_CucsVnicIpcOwner_Type = CucsVnicConnectionOwner
_CucsVnicIpcOwner_Object = MibTableColumn
cucsVnicIpcOwner = _CucsVnicIpcOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 26),
    _CucsVnicIpcOwner_Type()
)
cucsVnicIpcOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcOwner.setStatus("current")
_CucsVnicIpcPinToGroupName_Type = SnmpAdminString
_CucsVnicIpcPinToGroupName_Object = MibTableColumn
cucsVnicIpcPinToGroupName = _CucsVnicIpcPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 27),
    _CucsVnicIpcPinToGroupName_Type()
)
cucsVnicIpcPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcPinToGroupName.setStatus("current")
_CucsVnicIpcQosPolicyName_Type = SnmpAdminString
_CucsVnicIpcQosPolicyName_Object = MibTableColumn
cucsVnicIpcQosPolicyName = _CucsVnicIpcQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 28),
    _CucsVnicIpcQosPolicyName_Type()
)
cucsVnicIpcQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcQosPolicyName.setStatus("current")
_CucsVnicIpcStatsPolicyName_Type = SnmpAdminString
_CucsVnicIpcStatsPolicyName_Object = MibTableColumn
cucsVnicIpcStatsPolicyName = _CucsVnicIpcStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 29),
    _CucsVnicIpcStatsPolicyName_Type()
)
cucsVnicIpcStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcStatsPolicyName.setStatus("current")
_CucsVnicIpcSwitchId_Type = CucsVnicEtherBaseSwitchId
_CucsVnicIpcSwitchId_Object = MibTableColumn
cucsVnicIpcSwitchId = _CucsVnicIpcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 30),
    _CucsVnicIpcSwitchId_Type()
)
cucsVnicIpcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcSwitchId.setStatus("current")
_CucsVnicIpcType_Type = CucsVnicIpcType
_CucsVnicIpcType_Object = MibTableColumn
cucsVnicIpcType = _CucsVnicIpcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 31),
    _CucsVnicIpcType_Type()
)
cucsVnicIpcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcType.setStatus("current")
_CucsVnicIpcOperPinToGroupName_Type = SnmpAdminString
_CucsVnicIpcOperPinToGroupName_Object = MibTableColumn
cucsVnicIpcOperPinToGroupName = _CucsVnicIpcOperPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 32),
    _CucsVnicIpcOperPinToGroupName_Type()
)
cucsVnicIpcOperPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcOperPinToGroupName.setStatus("current")
_CucsVnicIpcConfigQualifier_Type = CucsVnicConfigIssues
_CucsVnicIpcConfigQualifier_Object = MibTableColumn
cucsVnicIpcConfigQualifier = _CucsVnicIpcConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 33),
    _CucsVnicIpcConfigQualifier_Type()
)
cucsVnicIpcConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcConfigQualifier.setStatus("current")
_CucsVnicIpcAdminHostPort_Type = CucsFabricHostPortId
_CucsVnicIpcAdminHostPort_Object = MibTableColumn
cucsVnicIpcAdminHostPort = _CucsVnicIpcAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 35),
    _CucsVnicIpcAdminHostPort_Type()
)
cucsVnicIpcAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcAdminHostPort.setStatus("current")
_CucsVnicIpcOperHostPort_Type = CucsVnicVnicOperHostPort
_CucsVnicIpcOperHostPort_Object = MibTableColumn
cucsVnicIpcOperHostPort = _CucsVnicIpcOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 36),
    _CucsVnicIpcOperHostPort_Type()
)
cucsVnicIpcOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcOperHostPort.setStatus("current")
_CucsVnicIpcPurpose_Type = CucsAdaptorPurpose
_CucsVnicIpcPurpose_Object = MibTableColumn
cucsVnicIpcPurpose = _CucsVnicIpcPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 37),
    _CucsVnicIpcPurpose_Type()
)
cucsVnicIpcPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcPurpose.setStatus("current")
_CucsVnicIpcAdminCdnName_Type = SnmpAdminString
_CucsVnicIpcAdminCdnName_Object = MibTableColumn
cucsVnicIpcAdminCdnName = _CucsVnicIpcAdminCdnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 38),
    _CucsVnicIpcAdminCdnName_Type()
)
cucsVnicIpcAdminCdnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcAdminCdnName.setStatus("current")
_CucsVnicIpcOperCdnName_Type = SnmpAdminString
_CucsVnicIpcOperCdnName_Object = MibTableColumn
cucsVnicIpcOperCdnName = _CucsVnicIpcOperCdnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 39),
    _CucsVnicIpcOperCdnName_Type()
)
cucsVnicIpcOperCdnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcOperCdnName.setStatus("current")
_CucsVnicIpcCdnPropInSync_Type = TruthValue
_CucsVnicIpcCdnPropInSync_Object = MibTableColumn
cucsVnicIpcCdnPropInSync = _CucsVnicIpcCdnPropInSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 40),
    _CucsVnicIpcCdnPropInSync_Type()
)
cucsVnicIpcCdnPropInSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcCdnPropInSync.setStatus("current")
_CucsVnicIpcCdnSource_Type = CucsVnicCdnSource
_CucsVnicIpcCdnSource_Object = MibTableColumn
cucsVnicIpcCdnSource = _CucsVnicIpcCdnSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 23, 1, 41),
    _CucsVnicIpcCdnSource_Type()
)
cucsVnicIpcCdnSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcCdnSource.setStatus("current")
_CucsVnicIpcIfTable_Object = MibTable
cucsVnicIpcIfTable = _CucsVnicIpcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24)
)
if mibBuilder.loadTexts:
    cucsVnicIpcIfTable.setStatus("current")
_CucsVnicIpcIfEntry_Object = MibTableRow
cucsVnicIpcIfEntry = _CucsVnicIpcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1)
)
cucsVnicIpcIfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIpcIfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIpcIfEntry.setStatus("current")
_CucsVnicIpcIfInstanceId_Type = CucsManagedObjectId
_CucsVnicIpcIfInstanceId_Object = MibTableColumn
cucsVnicIpcIfInstanceId = _CucsVnicIpcIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 1),
    _CucsVnicIpcIfInstanceId_Type()
)
cucsVnicIpcIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIpcIfInstanceId.setStatus("current")
_CucsVnicIpcIfDn_Type = CucsManagedObjectDn
_CucsVnicIpcIfDn_Object = MibTableColumn
cucsVnicIpcIfDn = _CucsVnicIpcIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 2),
    _CucsVnicIpcIfDn_Type()
)
cucsVnicIpcIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIfDn.setStatus("current")
_CucsVnicIpcIfRn_Type = SnmpAdminString
_CucsVnicIpcIfRn_Object = MibTableColumn
cucsVnicIpcIfRn = _CucsVnicIpcIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 3),
    _CucsVnicIpcIfRn_Type()
)
cucsVnicIpcIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIfRn.setStatus("current")
_CucsVnicIpcIfAddr_Type = MacAddress
_CucsVnicIpcIfAddr_Object = MibTableColumn
cucsVnicIpcIfAddr = _CucsVnicIpcIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 4),
    _CucsVnicIpcIfAddr_Type()
)
cucsVnicIpcIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIfAddr.setStatus("current")
_CucsVnicIpcIfDefaultNet_Type = TruthValue
_CucsVnicIpcIfDefaultNet_Object = MibTableColumn
cucsVnicIpcIfDefaultNet = _CucsVnicIpcIfDefaultNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 5),
    _CucsVnicIpcIfDefaultNet_Type()
)
cucsVnicIpcIfDefaultNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIfDefaultNet.setStatus("current")
_CucsVnicIpcIfName_Type = SnmpAdminString
_CucsVnicIpcIfName_Object = MibTableColumn
cucsVnicIpcIfName = _CucsVnicIpcIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 6),
    _CucsVnicIpcIfName_Type()
)
cucsVnicIpcIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIfName.setStatus("current")
_CucsVnicIpcIfOperState_Type = CucsVnicIfOperState
_CucsVnicIpcIfOperState_Object = MibTableColumn
cucsVnicIpcIfOperState = _CucsVnicIpcIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 7),
    _CucsVnicIpcIfOperState_Type()
)
cucsVnicIpcIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIfOperState.setStatus("current")
_CucsVnicIpcIfOwner_Type = CucsVnicConnectionOwner
_CucsVnicIpcIfOwner_Object = MibTableColumn
cucsVnicIpcIfOwner = _CucsVnicIpcIfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 8),
    _CucsVnicIpcIfOwner_Type()
)
cucsVnicIpcIfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIfOwner.setStatus("current")
_CucsVnicIpcIfSwitchId_Type = CucsVnicEtherBaseIfSwitchId
_CucsVnicIpcIfSwitchId_Object = MibTableColumn
cucsVnicIpcIfSwitchId = _CucsVnicIpcIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 9),
    _CucsVnicIpcIfSwitchId_Type()
)
cucsVnicIpcIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIfSwitchId.setStatus("current")
_CucsVnicIpcIfType_Type = CucsVnicAIpcIfType
_CucsVnicIpcIfType_Object = MibTableColumn
cucsVnicIpcIfType = _CucsVnicIpcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 10),
    _CucsVnicIpcIfType_Type()
)
cucsVnicIpcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIfType.setStatus("current")
_CucsVnicIpcIfVnet_Type = Gauge32
_CucsVnicIpcIfVnet_Object = MibTableColumn
cucsVnicIpcIfVnet = _CucsVnicIpcIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 11),
    _CucsVnicIpcIfVnet_Type()
)
cucsVnicIpcIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIfVnet.setStatus("current")
_CucsVnicIpcIfConfigQualifier_Type = CucsVnicConfigIssues
_CucsVnicIpcIfConfigQualifier_Object = MibTableColumn
cucsVnicIpcIfConfigQualifier = _CucsVnicIpcIfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 12),
    _CucsVnicIpcIfConfigQualifier_Type()
)
cucsVnicIpcIfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIfConfigQualifier.setStatus("current")
_CucsVnicIpcIfOperVnetDn_Type = SnmpAdminString
_CucsVnicIpcIfOperVnetDn_Object = MibTableColumn
cucsVnicIpcIfOperVnetDn = _CucsVnicIpcIfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 14),
    _CucsVnicIpcIfOperVnetDn_Type()
)
cucsVnicIpcIfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIfOperVnetDn.setStatus("current")
_CucsVnicIpcIfOperVnetName_Type = SnmpAdminString
_CucsVnicIpcIfOperVnetName_Object = MibTableColumn
cucsVnicIpcIfOperVnetName = _CucsVnicIpcIfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 15),
    _CucsVnicIpcIfOperVnetName_Type()
)
cucsVnicIpcIfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIfOperVnetName.setStatus("current")
_CucsVnicIpcIfPubNwId_Type = Gauge32
_CucsVnicIpcIfPubNwId_Object = MibTableColumn
cucsVnicIpcIfPubNwId = _CucsVnicIpcIfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 16),
    _CucsVnicIpcIfPubNwId_Type()
)
cucsVnicIpcIfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIfPubNwId.setStatus("current")
_CucsVnicIpcIfSharing_Type = CucsFabricVlanSharingType
_CucsVnicIpcIfSharing_Object = MibTableColumn
cucsVnicIpcIfSharing = _CucsVnicIpcIfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 17),
    _CucsVnicIpcIfSharing_Type()
)
cucsVnicIpcIfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIfSharing.setStatus("current")
_CucsVnicIpcIfOperPrimaryVnetDn_Type = SnmpAdminString
_CucsVnicIpcIfOperPrimaryVnetDn_Object = MibTableColumn
cucsVnicIpcIfOperPrimaryVnetDn = _CucsVnicIpcIfOperPrimaryVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 18),
    _CucsVnicIpcIfOperPrimaryVnetDn_Type()
)
cucsVnicIpcIfOperPrimaryVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIfOperPrimaryVnetDn.setStatus("current")
_CucsVnicIpcIfOperPrimaryVnetName_Type = SnmpAdminString
_CucsVnicIpcIfOperPrimaryVnetName_Object = MibTableColumn
cucsVnicIpcIfOperPrimaryVnetName = _CucsVnicIpcIfOperPrimaryVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 24, 1, 19),
    _CucsVnicIpcIfOperPrimaryVnetName_Type()
)
cucsVnicIpcIfOperPrimaryVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpcIfOperPrimaryVnetName.setStatus("current")
_CucsVnicLanConnTemplTable_Object = MibTable
cucsVnicLanConnTemplTable = _CucsVnicLanConnTemplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25)
)
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplTable.setStatus("current")
_CucsVnicLanConnTemplEntry_Object = MibTableRow
cucsVnicLanConnTemplEntry = _CucsVnicLanConnTemplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1)
)
cucsVnicLanConnTemplEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicLanConnTemplInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplEntry.setStatus("current")
_CucsVnicLanConnTemplInstanceId_Type = CucsManagedObjectId
_CucsVnicLanConnTemplInstanceId_Object = MibTableColumn
cucsVnicLanConnTemplInstanceId = _CucsVnicLanConnTemplInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 1),
    _CucsVnicLanConnTemplInstanceId_Type()
)
cucsVnicLanConnTemplInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplInstanceId.setStatus("current")
_CucsVnicLanConnTemplDn_Type = CucsManagedObjectDn
_CucsVnicLanConnTemplDn_Object = MibTableColumn
cucsVnicLanConnTemplDn = _CucsVnicLanConnTemplDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 2),
    _CucsVnicLanConnTemplDn_Type()
)
cucsVnicLanConnTemplDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplDn.setStatus("current")
_CucsVnicLanConnTemplRn_Type = SnmpAdminString
_CucsVnicLanConnTemplRn_Object = MibTableColumn
cucsVnicLanConnTemplRn = _CucsVnicLanConnTemplRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 3),
    _CucsVnicLanConnTemplRn_Type()
)
cucsVnicLanConnTemplRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplRn.setStatus("current")
_CucsVnicLanConnTemplDescr_Type = SnmpAdminString
_CucsVnicLanConnTemplDescr_Object = MibTableColumn
cucsVnicLanConnTemplDescr = _CucsVnicLanConnTemplDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 4),
    _CucsVnicLanConnTemplDescr_Type()
)
cucsVnicLanConnTemplDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplDescr.setStatus("current")
_CucsVnicLanConnTemplIdentPoolName_Type = SnmpAdminString
_CucsVnicLanConnTemplIdentPoolName_Object = MibTableColumn
cucsVnicLanConnTemplIdentPoolName = _CucsVnicLanConnTemplIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 5),
    _CucsVnicLanConnTemplIdentPoolName_Type()
)
cucsVnicLanConnTemplIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplIdentPoolName.setStatus("current")
_CucsVnicLanConnTemplIntId_Type = SnmpAdminString
_CucsVnicLanConnTemplIntId_Object = MibTableColumn
cucsVnicLanConnTemplIntId = _CucsVnicLanConnTemplIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 6),
    _CucsVnicLanConnTemplIntId_Type()
)
cucsVnicLanConnTemplIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplIntId.setStatus("current")
_CucsVnicLanConnTemplMtu_Type = Gauge32
_CucsVnicLanConnTemplMtu_Object = MibTableColumn
cucsVnicLanConnTemplMtu = _CucsVnicLanConnTemplMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 7),
    _CucsVnicLanConnTemplMtu_Type()
)
cucsVnicLanConnTemplMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplMtu.setStatus("current")
_CucsVnicLanConnTemplName_Type = SnmpAdminString
_CucsVnicLanConnTemplName_Object = MibTableColumn
cucsVnicLanConnTemplName = _CucsVnicLanConnTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 8),
    _CucsVnicLanConnTemplName_Type()
)
cucsVnicLanConnTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplName.setStatus("current")
_CucsVnicLanConnTemplNwCtrlPolicyName_Type = SnmpAdminString
_CucsVnicLanConnTemplNwCtrlPolicyName_Object = MibTableColumn
cucsVnicLanConnTemplNwCtrlPolicyName = _CucsVnicLanConnTemplNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 9),
    _CucsVnicLanConnTemplNwCtrlPolicyName_Type()
)
cucsVnicLanConnTemplNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplNwCtrlPolicyName.setStatus("current")
_CucsVnicLanConnTemplOperIdentPoolName_Type = SnmpAdminString
_CucsVnicLanConnTemplOperIdentPoolName_Object = MibTableColumn
cucsVnicLanConnTemplOperIdentPoolName = _CucsVnicLanConnTemplOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 10),
    _CucsVnicLanConnTemplOperIdentPoolName_Type()
)
cucsVnicLanConnTemplOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplOperIdentPoolName.setStatus("current")
_CucsVnicLanConnTemplOperNwCtrlPolicyName_Type = SnmpAdminString
_CucsVnicLanConnTemplOperNwCtrlPolicyName_Object = MibTableColumn
cucsVnicLanConnTemplOperNwCtrlPolicyName = _CucsVnicLanConnTemplOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 11),
    _CucsVnicLanConnTemplOperNwCtrlPolicyName_Type()
)
cucsVnicLanConnTemplOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplOperNwCtrlPolicyName.setStatus("current")
_CucsVnicLanConnTemplOperQosPolicyName_Type = SnmpAdminString
_CucsVnicLanConnTemplOperQosPolicyName_Object = MibTableColumn
cucsVnicLanConnTemplOperQosPolicyName = _CucsVnicLanConnTemplOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 12),
    _CucsVnicLanConnTemplOperQosPolicyName_Type()
)
cucsVnicLanConnTemplOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplOperQosPolicyName.setStatus("current")
_CucsVnicLanConnTemplOperStatsPolicyName_Type = SnmpAdminString
_CucsVnicLanConnTemplOperStatsPolicyName_Object = MibTableColumn
cucsVnicLanConnTemplOperStatsPolicyName = _CucsVnicLanConnTemplOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 13),
    _CucsVnicLanConnTemplOperStatsPolicyName_Type()
)
cucsVnicLanConnTemplOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplOperStatsPolicyName.setStatus("current")
_CucsVnicLanConnTemplPinToGroupName_Type = SnmpAdminString
_CucsVnicLanConnTemplPinToGroupName_Object = MibTableColumn
cucsVnicLanConnTemplPinToGroupName = _CucsVnicLanConnTemplPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 14),
    _CucsVnicLanConnTemplPinToGroupName_Type()
)
cucsVnicLanConnTemplPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplPinToGroupName.setStatus("current")
_CucsVnicLanConnTemplQosPolicyName_Type = SnmpAdminString
_CucsVnicLanConnTemplQosPolicyName_Object = MibTableColumn
cucsVnicLanConnTemplQosPolicyName = _CucsVnicLanConnTemplQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 15),
    _CucsVnicLanConnTemplQosPolicyName_Type()
)
cucsVnicLanConnTemplQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplQosPolicyName.setStatus("current")
_CucsVnicLanConnTemplStatsPolicyName_Type = SnmpAdminString
_CucsVnicLanConnTemplStatsPolicyName_Object = MibTableColumn
cucsVnicLanConnTemplStatsPolicyName = _CucsVnicLanConnTemplStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 16),
    _CucsVnicLanConnTemplStatsPolicyName_Type()
)
cucsVnicLanConnTemplStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplStatsPolicyName.setStatus("current")
_CucsVnicLanConnTemplSwitchId_Type = CucsVnicLanConnTemplSwitchId
_CucsVnicLanConnTemplSwitchId_Object = MibTableColumn
cucsVnicLanConnTemplSwitchId = _CucsVnicLanConnTemplSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 17),
    _CucsVnicLanConnTemplSwitchId_Type()
)
cucsVnicLanConnTemplSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplSwitchId.setStatus("current")
_CucsVnicLanConnTemplTarget_Type = CucsVnicTemplateTarget
_CucsVnicLanConnTemplTarget_Object = MibTableColumn
cucsVnicLanConnTemplTarget = _CucsVnicLanConnTemplTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 18),
    _CucsVnicLanConnTemplTarget_Type()
)
cucsVnicLanConnTemplTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplTarget.setStatus("current")
_CucsVnicLanConnTemplTemplType_Type = CucsVnicTemplateType
_CucsVnicLanConnTemplTemplType_Object = MibTableColumn
cucsVnicLanConnTemplTemplType = _CucsVnicLanConnTemplTemplType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 19),
    _CucsVnicLanConnTemplTemplType_Type()
)
cucsVnicLanConnTemplTemplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplTemplType.setStatus("current")
_CucsVnicLanConnTemplPolicyLevel_Type = Gauge32
_CucsVnicLanConnTemplPolicyLevel_Object = MibTableColumn
cucsVnicLanConnTemplPolicyLevel = _CucsVnicLanConnTemplPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 20),
    _CucsVnicLanConnTemplPolicyLevel_Type()
)
cucsVnicLanConnTemplPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplPolicyLevel.setStatus("current")
_CucsVnicLanConnTemplPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicLanConnTemplPolicyOwner_Object = MibTableColumn
cucsVnicLanConnTemplPolicyOwner = _CucsVnicLanConnTemplPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 21),
    _CucsVnicLanConnTemplPolicyOwner_Type()
)
cucsVnicLanConnTemplPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplPolicyOwner.setStatus("current")
_CucsVnicLanConnTemplAdminCdnName_Type = SnmpAdminString
_CucsVnicLanConnTemplAdminCdnName_Object = MibTableColumn
cucsVnicLanConnTemplAdminCdnName = _CucsVnicLanConnTemplAdminCdnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 22),
    _CucsVnicLanConnTemplAdminCdnName_Type()
)
cucsVnicLanConnTemplAdminCdnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplAdminCdnName.setStatus("current")
_CucsVnicLanConnTemplCdnSource_Type = CucsVnicCdnSource
_CucsVnicLanConnTemplCdnSource_Object = MibTableColumn
cucsVnicLanConnTemplCdnSource = _CucsVnicLanConnTemplCdnSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 25, 1, 23),
    _CucsVnicLanConnTemplCdnSource_Type()
)
cucsVnicLanConnTemplCdnSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnTemplCdnSource.setStatus("current")
_CucsVnicLifVlanTable_Object = MibTable
cucsVnicLifVlanTable = _CucsVnicLifVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26)
)
if mibBuilder.loadTexts:
    cucsVnicLifVlanTable.setStatus("current")
_CucsVnicLifVlanEntry_Object = MibTableRow
cucsVnicLifVlanEntry = _CucsVnicLifVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1)
)
cucsVnicLifVlanEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicLifVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicLifVlanEntry.setStatus("current")
_CucsVnicLifVlanInstanceId_Type = CucsManagedObjectId
_CucsVnicLifVlanInstanceId_Object = MibTableColumn
cucsVnicLifVlanInstanceId = _CucsVnicLifVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 1),
    _CucsVnicLifVlanInstanceId_Type()
)
cucsVnicLifVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicLifVlanInstanceId.setStatus("current")
_CucsVnicLifVlanDn_Type = CucsManagedObjectDn
_CucsVnicLifVlanDn_Object = MibTableColumn
cucsVnicLifVlanDn = _CucsVnicLifVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 2),
    _CucsVnicLifVlanDn_Type()
)
cucsVnicLifVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanDn.setStatus("current")
_CucsVnicLifVlanRn_Type = SnmpAdminString
_CucsVnicLifVlanRn_Object = MibTableColumn
cucsVnicLifVlanRn = _CucsVnicLifVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 3),
    _CucsVnicLifVlanRn_Type()
)
cucsVnicLifVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanRn.setStatus("current")
_CucsVnicLifVlanAddr_Type = MacAddress
_CucsVnicLifVlanAddr_Object = MibTableColumn
cucsVnicLifVlanAddr = _CucsVnicLifVlanAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 4),
    _CucsVnicLifVlanAddr_Type()
)
cucsVnicLifVlanAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanAddr.setStatus("current")
_CucsVnicLifVlanDefaultNet_Type = TruthValue
_CucsVnicLifVlanDefaultNet_Object = MibTableColumn
cucsVnicLifVlanDefaultNet = _CucsVnicLifVlanDefaultNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 5),
    _CucsVnicLifVlanDefaultNet_Type()
)
cucsVnicLifVlanDefaultNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanDefaultNet.setStatus("current")
_CucsVnicLifVlanName_Type = SnmpAdminString
_CucsVnicLifVlanName_Object = MibTableColumn
cucsVnicLifVlanName = _CucsVnicLifVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 6),
    _CucsVnicLifVlanName_Type()
)
cucsVnicLifVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanName.setStatus("current")
_CucsVnicLifVlanOperState_Type = CucsVnicIfOperState
_CucsVnicLifVlanOperState_Object = MibTableColumn
cucsVnicLifVlanOperState = _CucsVnicLifVlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 7),
    _CucsVnicLifVlanOperState_Type()
)
cucsVnicLifVlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanOperState.setStatus("current")
_CucsVnicLifVlanOwner_Type = CucsVnicConnectionOwner
_CucsVnicLifVlanOwner_Object = MibTableColumn
cucsVnicLifVlanOwner = _CucsVnicLifVlanOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 8),
    _CucsVnicLifVlanOwner_Type()
)
cucsVnicLifVlanOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanOwner.setStatus("current")
_CucsVnicLifVlanSwitchId_Type = CucsVnicEtherBaseIfSwitchId
_CucsVnicLifVlanSwitchId_Object = MibTableColumn
cucsVnicLifVlanSwitchId = _CucsVnicLifVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 9),
    _CucsVnicLifVlanSwitchId_Type()
)
cucsVnicLifVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanSwitchId.setStatus("current")
_CucsVnicLifVlanType_Type = CucsVnicAEtherIfType
_CucsVnicLifVlanType_Object = MibTableColumn
cucsVnicLifVlanType = _CucsVnicLifVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 10),
    _CucsVnicLifVlanType_Type()
)
cucsVnicLifVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanType.setStatus("current")
_CucsVnicLifVlanVnet_Type = Gauge32
_CucsVnicLifVlanVnet_Object = MibTableColumn
cucsVnicLifVlanVnet = _CucsVnicLifVlanVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 11),
    _CucsVnicLifVlanVnet_Type()
)
cucsVnicLifVlanVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanVnet.setStatus("current")
_CucsVnicLifVlanConfigQualifier_Type = CucsVnicConfigIssues
_CucsVnicLifVlanConfigQualifier_Object = MibTableColumn
cucsVnicLifVlanConfigQualifier = _CucsVnicLifVlanConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 12),
    _CucsVnicLifVlanConfigQualifier_Type()
)
cucsVnicLifVlanConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanConfigQualifier.setStatus("current")
_CucsVnicLifVlanOperVnetDn_Type = SnmpAdminString
_CucsVnicLifVlanOperVnetDn_Object = MibTableColumn
cucsVnicLifVlanOperVnetDn = _CucsVnicLifVlanOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 14),
    _CucsVnicLifVlanOperVnetDn_Type()
)
cucsVnicLifVlanOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanOperVnetDn.setStatus("current")
_CucsVnicLifVlanOperVnetName_Type = SnmpAdminString
_CucsVnicLifVlanOperVnetName_Object = MibTableColumn
cucsVnicLifVlanOperVnetName = _CucsVnicLifVlanOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 15),
    _CucsVnicLifVlanOperVnetName_Type()
)
cucsVnicLifVlanOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanOperVnetName.setStatus("current")
_CucsVnicLifVlanPubNwId_Type = Gauge32
_CucsVnicLifVlanPubNwId_Object = MibTableColumn
cucsVnicLifVlanPubNwId = _CucsVnicLifVlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 16),
    _CucsVnicLifVlanPubNwId_Type()
)
cucsVnicLifVlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanPubNwId.setStatus("current")
_CucsVnicLifVlanSharing_Type = CucsFabricVlanSharingType
_CucsVnicLifVlanSharing_Object = MibTableColumn
cucsVnicLifVlanSharing = _CucsVnicLifVlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 17),
    _CucsVnicLifVlanSharing_Type()
)
cucsVnicLifVlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanSharing.setStatus("current")
_CucsVnicLifVlanPropAcl_Type = Unsigned64
_CucsVnicLifVlanPropAcl_Object = MibTableColumn
cucsVnicLifVlanPropAcl = _CucsVnicLifVlanPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 18),
    _CucsVnicLifVlanPropAcl_Type()
)
cucsVnicLifVlanPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanPropAcl.setStatus("current")
_CucsVnicLifVlanOperPrimaryVnetDn_Type = SnmpAdminString
_CucsVnicLifVlanOperPrimaryVnetDn_Object = MibTableColumn
cucsVnicLifVlanOperPrimaryVnetDn = _CucsVnicLifVlanOperPrimaryVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 19),
    _CucsVnicLifVlanOperPrimaryVnetDn_Type()
)
cucsVnicLifVlanOperPrimaryVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanOperPrimaryVnetDn.setStatus("current")
_CucsVnicLifVlanOperPrimaryVnetName_Type = SnmpAdminString
_CucsVnicLifVlanOperPrimaryVnetName_Object = MibTableColumn
cucsVnicLifVlanOperPrimaryVnetName = _CucsVnicLifVlanOperPrimaryVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 26, 1, 20),
    _CucsVnicLifVlanOperPrimaryVnetName_Type()
)
cucsVnicLifVlanOperPrimaryVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVlanOperPrimaryVnetName.setStatus("current")
_CucsVnicLifVsanTable_Object = MibTable
cucsVnicLifVsanTable = _CucsVnicLifVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27)
)
if mibBuilder.loadTexts:
    cucsVnicLifVsanTable.setStatus("current")
_CucsVnicLifVsanEntry_Object = MibTableRow
cucsVnicLifVsanEntry = _CucsVnicLifVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1)
)
cucsVnicLifVsanEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicLifVsanInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicLifVsanEntry.setStatus("current")
_CucsVnicLifVsanInstanceId_Type = CucsManagedObjectId
_CucsVnicLifVsanInstanceId_Object = MibTableColumn
cucsVnicLifVsanInstanceId = _CucsVnicLifVsanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1, 1),
    _CucsVnicLifVsanInstanceId_Type()
)
cucsVnicLifVsanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicLifVsanInstanceId.setStatus("current")
_CucsVnicLifVsanDn_Type = CucsManagedObjectDn
_CucsVnicLifVsanDn_Object = MibTableColumn
cucsVnicLifVsanDn = _CucsVnicLifVsanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1, 2),
    _CucsVnicLifVsanDn_Type()
)
cucsVnicLifVsanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVsanDn.setStatus("current")
_CucsVnicLifVsanRn_Type = SnmpAdminString
_CucsVnicLifVsanRn_Object = MibTableColumn
cucsVnicLifVsanRn = _CucsVnicLifVsanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1, 3),
    _CucsVnicLifVsanRn_Type()
)
cucsVnicLifVsanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVsanRn.setStatus("current")
_CucsVnicLifVsanInitiator_Type = Unsigned64
_CucsVnicLifVsanInitiator_Object = MibTableColumn
cucsVnicLifVsanInitiator = _CucsVnicLifVsanInitiator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1, 4),
    _CucsVnicLifVsanInitiator_Type()
)
cucsVnicLifVsanInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVsanInitiator.setStatus("current")
_CucsVnicLifVsanName_Type = SnmpAdminString
_CucsVnicLifVsanName_Object = MibTableColumn
cucsVnicLifVsanName = _CucsVnicLifVsanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1, 5),
    _CucsVnicLifVsanName_Type()
)
cucsVnicLifVsanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVsanName.setStatus("current")
_CucsVnicLifVsanOperState_Type = CucsVnicIfOperState
_CucsVnicLifVsanOperState_Object = MibTableColumn
cucsVnicLifVsanOperState = _CucsVnicLifVsanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1, 6),
    _CucsVnicLifVsanOperState_Type()
)
cucsVnicLifVsanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVsanOperState.setStatus("current")
_CucsVnicLifVsanOwner_Type = CucsVnicConnectionOwner
_CucsVnicLifVsanOwner_Object = MibTableColumn
cucsVnicLifVsanOwner = _CucsVnicLifVsanOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1, 7),
    _CucsVnicLifVsanOwner_Type()
)
cucsVnicLifVsanOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVsanOwner.setStatus("current")
_CucsVnicLifVsanSwitchId_Type = CucsVnicAFcIfSwitchId
_CucsVnicLifVsanSwitchId_Object = MibTableColumn
cucsVnicLifVsanSwitchId = _CucsVnicLifVsanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1, 8),
    _CucsVnicLifVsanSwitchId_Type()
)
cucsVnicLifVsanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVsanSwitchId.setStatus("current")
_CucsVnicLifVsanType_Type = CucsVnicAFcIfType
_CucsVnicLifVsanType_Object = MibTableColumn
cucsVnicLifVsanType = _CucsVnicLifVsanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1, 9),
    _CucsVnicLifVsanType_Type()
)
cucsVnicLifVsanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVsanType.setStatus("current")
_CucsVnicLifVsanVnet_Type = Gauge32
_CucsVnicLifVsanVnet_Object = MibTableColumn
cucsVnicLifVsanVnet = _CucsVnicLifVsanVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1, 10),
    _CucsVnicLifVsanVnet_Type()
)
cucsVnicLifVsanVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVsanVnet.setStatus("current")
_CucsVnicLifVsanConfigQualifier_Type = CucsVnicConfigIssues
_CucsVnicLifVsanConfigQualifier_Object = MibTableColumn
cucsVnicLifVsanConfigQualifier = _CucsVnicLifVsanConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1, 11),
    _CucsVnicLifVsanConfigQualifier_Type()
)
cucsVnicLifVsanConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVsanConfigQualifier.setStatus("current")
_CucsVnicLifVsanOperVnetDn_Type = SnmpAdminString
_CucsVnicLifVsanOperVnetDn_Object = MibTableColumn
cucsVnicLifVsanOperVnetDn = _CucsVnicLifVsanOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1, 13),
    _CucsVnicLifVsanOperVnetDn_Type()
)
cucsVnicLifVsanOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVsanOperVnetDn.setStatus("current")
_CucsVnicLifVsanOperVnetName_Type = SnmpAdminString
_CucsVnicLifVsanOperVnetName_Object = MibTableColumn
cucsVnicLifVsanOperVnetName = _CucsVnicLifVsanOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1, 14),
    _CucsVnicLifVsanOperVnetName_Type()
)
cucsVnicLifVsanOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVsanOperVnetName.setStatus("current")
_CucsVnicLifVsanPubNwId_Type = Gauge32
_CucsVnicLifVsanPubNwId_Object = MibTableColumn
cucsVnicLifVsanPubNwId = _CucsVnicLifVsanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1, 15),
    _CucsVnicLifVsanPubNwId_Type()
)
cucsVnicLifVsanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVsanPubNwId.setStatus("current")
_CucsVnicLifVsanSharing_Type = CucsFabricVlanSharingType
_CucsVnicLifVsanSharing_Object = MibTableColumn
cucsVnicLifVsanSharing = _CucsVnicLifVsanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1, 16),
    _CucsVnicLifVsanSharing_Type()
)
cucsVnicLifVsanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVsanSharing.setStatus("current")
_CucsVnicLifVsanOperPrimaryVnetDn_Type = SnmpAdminString
_CucsVnicLifVsanOperPrimaryVnetDn_Object = MibTableColumn
cucsVnicLifVsanOperPrimaryVnetDn = _CucsVnicLifVsanOperPrimaryVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1, 17),
    _CucsVnicLifVsanOperPrimaryVnetDn_Type()
)
cucsVnicLifVsanOperPrimaryVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVsanOperPrimaryVnetDn.setStatus("current")
_CucsVnicLifVsanOperPrimaryVnetName_Type = SnmpAdminString
_CucsVnicLifVsanOperPrimaryVnetName_Object = MibTableColumn
cucsVnicLifVsanOperPrimaryVnetName = _CucsVnicLifVsanOperPrimaryVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 27, 1, 18),
    _CucsVnicLifVsanOperPrimaryVnetName_Type()
)
cucsVnicLifVsanOperPrimaryVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLifVsanOperPrimaryVnetName.setStatus("current")
_CucsVnicProfileTable_Object = MibTable
cucsVnicProfileTable = _CucsVnicProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28)
)
if mibBuilder.loadTexts:
    cucsVnicProfileTable.setStatus("current")
_CucsVnicProfileEntry_Object = MibTableRow
cucsVnicProfileEntry = _CucsVnicProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1)
)
cucsVnicProfileEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicProfileEntry.setStatus("current")
_CucsVnicProfileInstanceId_Type = CucsManagedObjectId
_CucsVnicProfileInstanceId_Object = MibTableColumn
cucsVnicProfileInstanceId = _CucsVnicProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 1),
    _CucsVnicProfileInstanceId_Type()
)
cucsVnicProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicProfileInstanceId.setStatus("current")
_CucsVnicProfileDn_Type = CucsManagedObjectDn
_CucsVnicProfileDn_Object = MibTableColumn
cucsVnicProfileDn = _CucsVnicProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 2),
    _CucsVnicProfileDn_Type()
)
cucsVnicProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileDn.setStatus("current")
_CucsVnicProfileRn_Type = SnmpAdminString
_CucsVnicProfileRn_Object = MibTableColumn
cucsVnicProfileRn = _CucsVnicProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 3),
    _CucsVnicProfileRn_Type()
)
cucsVnicProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileRn.setStatus("current")
_CucsVnicProfileCdp_Type = CucsNwctrlAdminState
_CucsVnicProfileCdp_Object = MibTableColumn
cucsVnicProfileCdp = _CucsVnicProfileCdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 5),
    _CucsVnicProfileCdp_Type()
)
cucsVnicProfileCdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileCdp.setStatus("current")
_CucsVnicProfileCos_Type = Gauge32
_CucsVnicProfileCos_Object = MibTableColumn
cucsVnicProfileCos = _CucsVnicProfileCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 6),
    _CucsVnicProfileCos_Type()
)
cucsVnicProfileCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileCos.setStatus("current")
_CucsVnicProfileDescr_Type = SnmpAdminString
_CucsVnicProfileDescr_Object = MibTableColumn
cucsVnicProfileDescr = _CucsVnicProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 7),
    _CucsVnicProfileDescr_Type()
)
cucsVnicProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileDescr.setStatus("current")
_CucsVnicProfileForgeMac_Type = CucsDpsecForgedTransmit
_CucsVnicProfileForgeMac_Object = MibTableColumn
cucsVnicProfileForgeMac = _CucsVnicProfileForgeMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 8),
    _CucsVnicProfileForgeMac_Type()
)
cucsVnicProfileForgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileForgeMac.setStatus("current")
_CucsVnicProfileIntId_Type = SnmpAdminString
_CucsVnicProfileIntId_Object = MibTableColumn
cucsVnicProfileIntId = _CucsVnicProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 9),
    _CucsVnicProfileIntId_Type()
)
cucsVnicProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileIntId.setStatus("current")
_CucsVnicProfileMaxPorts_Type = Gauge32
_CucsVnicProfileMaxPorts_Object = MibTableColumn
cucsVnicProfileMaxPorts = _CucsVnicProfileMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 10),
    _CucsVnicProfileMaxPorts_Type()
)
cucsVnicProfileMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileMaxPorts.setStatus("current")
_CucsVnicProfileName_Type = SnmpAdminString
_CucsVnicProfileName_Object = MibTableColumn
cucsVnicProfileName = _CucsVnicProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 11),
    _CucsVnicProfileName_Type()
)
cucsVnicProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileName.setStatus("current")
_CucsVnicProfileNwCtrlPolicyName_Type = SnmpAdminString
_CucsVnicProfileNwCtrlPolicyName_Object = MibTableColumn
cucsVnicProfileNwCtrlPolicyName = _CucsVnicProfileNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 12),
    _CucsVnicProfileNwCtrlPolicyName_Type()
)
cucsVnicProfileNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileNwCtrlPolicyName.setStatus("current")
_CucsVnicProfileOperNwCtrlPolicyName_Type = SnmpAdminString
_CucsVnicProfileOperNwCtrlPolicyName_Object = MibTableColumn
cucsVnicProfileOperNwCtrlPolicyName = _CucsVnicProfileOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 13),
    _CucsVnicProfileOperNwCtrlPolicyName_Type()
)
cucsVnicProfileOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileOperNwCtrlPolicyName.setStatus("current")
_CucsVnicProfileOperQosPolicyName_Type = SnmpAdminString
_CucsVnicProfileOperQosPolicyName_Object = MibTableColumn
cucsVnicProfileOperQosPolicyName = _CucsVnicProfileOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 14),
    _CucsVnicProfileOperQosPolicyName_Type()
)
cucsVnicProfileOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileOperQosPolicyName.setStatus("current")
_CucsVnicProfilePinToGroupName_Type = SnmpAdminString
_CucsVnicProfilePinToGroupName_Object = MibTableColumn
cucsVnicProfilePinToGroupName = _CucsVnicProfilePinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 15),
    _CucsVnicProfilePinToGroupName_Type()
)
cucsVnicProfilePinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfilePinToGroupName.setStatus("current")
_CucsVnicProfileQosPolicyId_Type = SnmpAdminString
_CucsVnicProfileQosPolicyId_Object = MibTableColumn
cucsVnicProfileQosPolicyId = _CucsVnicProfileQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 16),
    _CucsVnicProfileQosPolicyId_Type()
)
cucsVnicProfileQosPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileQosPolicyId.setStatus("current")
_CucsVnicProfileQosPolicyName_Type = SnmpAdminString
_CucsVnicProfileQosPolicyName_Object = MibTableColumn
cucsVnicProfileQosPolicyName = _CucsVnicProfileQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 17),
    _CucsVnicProfileQosPolicyName_Type()
)
cucsVnicProfileQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileQosPolicyName.setStatus("current")
_CucsVnicProfileSwABorderPort_Type = Gauge32
_CucsVnicProfileSwABorderPort_Object = MibTableColumn
cucsVnicProfileSwABorderPort = _CucsVnicProfileSwABorderPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 19),
    _CucsVnicProfileSwABorderPort_Type()
)
cucsVnicProfileSwABorderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSwABorderPort.setStatus("current")
_CucsVnicProfileSwABorderSlot_Type = Gauge32
_CucsVnicProfileSwABorderSlot_Object = MibTableColumn
cucsVnicProfileSwABorderSlot = _CucsVnicProfileSwABorderSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 20),
    _CucsVnicProfileSwABorderSlot_Type()
)
cucsVnicProfileSwABorderSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSwABorderSlot.setStatus("current")
_CucsVnicProfileSwBBorderPort_Type = Gauge32
_CucsVnicProfileSwBBorderPort_Object = MibTableColumn
cucsVnicProfileSwBBorderPort = _CucsVnicProfileSwBBorderPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 21),
    _CucsVnicProfileSwBBorderPort_Type()
)
cucsVnicProfileSwBBorderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSwBBorderPort.setStatus("current")
_CucsVnicProfileSwBBorderSlot_Type = Gauge32
_CucsVnicProfileSwBBorderSlot_Object = MibTableColumn
cucsVnicProfileSwBBorderSlot = _CucsVnicProfileSwBBorderSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 22),
    _CucsVnicProfileSwBBorderSlot_Type()
)
cucsVnicProfileSwBBorderSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSwBBorderSlot.setStatus("current")
_CucsVnicProfileUplinkFailAction_Type = CucsNwctrlLinkFailAction
_CucsVnicProfileUplinkFailAction_Object = MibTableColumn
cucsVnicProfileUplinkFailAction = _CucsVnicProfileUplinkFailAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 23),
    _CucsVnicProfileUplinkFailAction_Type()
)
cucsVnicProfileUplinkFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileUplinkFailAction.setStatus("current")
_CucsVnicProfileHostNwIOPerf_Type = CucsVnicHostNwIOPerfPref
_CucsVnicProfileHostNwIOPerf_Object = MibTableColumn
cucsVnicProfileHostNwIOPerf = _CucsVnicProfileHostNwIOPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 24),
    _CucsVnicProfileHostNwIOPerf_Type()
)
cucsVnicProfileHostNwIOPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileHostNwIOPerf.setStatus("current")
_CucsVnicProfilePrimaryVlanId_Type = Gauge32
_CucsVnicProfilePrimaryVlanId_Object = MibTableColumn
cucsVnicProfilePrimaryVlanId = _CucsVnicProfilePrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 25),
    _CucsVnicProfilePrimaryVlanId_Type()
)
cucsVnicProfilePrimaryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfilePrimaryVlanId.setStatus("current")
_CucsVnicProfileQosPolicyDn_Type = SnmpAdminString
_CucsVnicProfileQosPolicyDn_Object = MibTableColumn
cucsVnicProfileQosPolicyDn = _CucsVnicProfileQosPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 26),
    _CucsVnicProfileQosPolicyDn_Type()
)
cucsVnicProfileQosPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileQosPolicyDn.setStatus("current")
_CucsVnicProfileConfigQualifier_Type = CucsVnicProfileConfigQualifier
_CucsVnicProfileConfigQualifier_Object = MibTableColumn
cucsVnicProfileConfigQualifier = _CucsVnicProfileConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 27),
    _CucsVnicProfileConfigQualifier_Type()
)
cucsVnicProfileConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileConfigQualifier.setStatus("current")
_CucsVnicProfileMacRegisterMode_Type = CucsNwctrlRegistrationMode
_CucsVnicProfileMacRegisterMode_Object = MibTableColumn
cucsVnicProfileMacRegisterMode = _CucsVnicProfileMacRegisterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 28),
    _CucsVnicProfileMacRegisterMode_Type()
)
cucsVnicProfileMacRegisterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileMacRegisterMode.setStatus("current")
_CucsVnicProfilePolicyLevel_Type = Gauge32
_CucsVnicProfilePolicyLevel_Object = MibTableColumn
cucsVnicProfilePolicyLevel = _CucsVnicProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 29),
    _CucsVnicProfilePolicyLevel_Type()
)
cucsVnicProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfilePolicyLevel.setStatus("current")
_CucsVnicProfilePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicProfilePolicyOwner_Object = MibTableColumn
cucsVnicProfilePolicyOwner = _CucsVnicProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 30),
    _CucsVnicProfilePolicyOwner_Type()
)
cucsVnicProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfilePolicyOwner.setStatus("current")
_CucsVnicProfilePortProfileUuid_Type = SnmpAdminString
_CucsVnicProfilePortProfileUuid_Object = MibTableColumn
cucsVnicProfilePortProfileUuid = _CucsVnicProfilePortProfileUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 31),
    _CucsVnicProfilePortProfileUuid_Type()
)
cucsVnicProfilePortProfileUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfilePortProfileUuid.setStatus("current")
_CucsVnicProfileType_Type = CucsVnicPortProfileType
_CucsVnicProfileType_Object = MibTableColumn
cucsVnicProfileType = _CucsVnicProfileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 32),
    _CucsVnicProfileType_Type()
)
cucsVnicProfileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileType.setStatus("current")
_CucsVnicProfileSwABorderAggrPort_Type = Gauge32
_CucsVnicProfileSwABorderAggrPort_Object = MibTableColumn
cucsVnicProfileSwABorderAggrPort = _CucsVnicProfileSwABorderAggrPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 33),
    _CucsVnicProfileSwABorderAggrPort_Type()
)
cucsVnicProfileSwABorderAggrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSwABorderAggrPort.setStatus("current")
_CucsVnicProfileSwBBorderAggrPort_Type = Gauge32
_CucsVnicProfileSwBBorderAggrPort_Object = MibTableColumn
cucsVnicProfileSwBBorderAggrPort = _CucsVnicProfileSwBBorderAggrPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 34),
    _CucsVnicProfileSwBBorderAggrPort_Type()
)
cucsVnicProfileSwBBorderAggrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSwBBorderAggrPort.setStatus("current")
_CucsVnicProfileLldp_Type = CucsNwctrlLldpAdminStateBitmask
_CucsVnicProfileLldp_Object = MibTableColumn
cucsVnicProfileLldp = _CucsVnicProfileLldp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 28, 1, 35),
    _CucsVnicProfileLldp_Type()
)
cucsVnicProfileLldp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileLldp.setStatus("current")
_CucsVnicProfileAliasTable_Object = MibTable
cucsVnicProfileAliasTable = _CucsVnicProfileAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 29)
)
if mibBuilder.loadTexts:
    cucsVnicProfileAliasTable.setStatus("current")
_CucsVnicProfileAliasEntry_Object = MibTableRow
cucsVnicProfileAliasEntry = _CucsVnicProfileAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 29, 1)
)
cucsVnicProfileAliasEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicProfileAliasInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicProfileAliasEntry.setStatus("current")
_CucsVnicProfileAliasInstanceId_Type = CucsManagedObjectId
_CucsVnicProfileAliasInstanceId_Object = MibTableColumn
cucsVnicProfileAliasInstanceId = _CucsVnicProfileAliasInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 29, 1, 1),
    _CucsVnicProfileAliasInstanceId_Type()
)
cucsVnicProfileAliasInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicProfileAliasInstanceId.setStatus("current")
_CucsVnicProfileAliasDn_Type = CucsManagedObjectDn
_CucsVnicProfileAliasDn_Object = MibTableColumn
cucsVnicProfileAliasDn = _CucsVnicProfileAliasDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 29, 1, 2),
    _CucsVnicProfileAliasDn_Type()
)
cucsVnicProfileAliasDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileAliasDn.setStatus("current")
_CucsVnicProfileAliasRn_Type = SnmpAdminString
_CucsVnicProfileAliasRn_Object = MibTableColumn
cucsVnicProfileAliasRn = _CucsVnicProfileAliasRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 29, 1, 3),
    _CucsVnicProfileAliasRn_Type()
)
cucsVnicProfileAliasRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileAliasRn.setStatus("current")
_CucsVnicProfileAliasAlias_Type = SnmpAdminString
_CucsVnicProfileAliasAlias_Object = MibTableColumn
cucsVnicProfileAliasAlias = _CucsVnicProfileAliasAlias_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 29, 1, 4),
    _CucsVnicProfileAliasAlias_Type()
)
cucsVnicProfileAliasAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileAliasAlias.setStatus("current")
_CucsVnicProfileAliasSwUuid_Type = SnmpAdminString
_CucsVnicProfileAliasSwUuid_Object = MibTableColumn
cucsVnicProfileAliasSwUuid = _CucsVnicProfileAliasSwUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 29, 1, 5),
    _CucsVnicProfileAliasSwUuid_Type()
)
cucsVnicProfileAliasSwUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileAliasSwUuid.setStatus("current")
_CucsVnicProfileSetTable_Object = MibTable
cucsVnicProfileSetTable = _CucsVnicProfileSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30)
)
if mibBuilder.loadTexts:
    cucsVnicProfileSetTable.setStatus("current")
_CucsVnicProfileSetEntry_Object = MibTableRow
cucsVnicProfileSetEntry = _CucsVnicProfileSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30, 1)
)
cucsVnicProfileSetEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicProfileSetInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicProfileSetEntry.setStatus("current")
_CucsVnicProfileSetInstanceId_Type = CucsManagedObjectId
_CucsVnicProfileSetInstanceId_Object = MibTableColumn
cucsVnicProfileSetInstanceId = _CucsVnicProfileSetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30, 1, 1),
    _CucsVnicProfileSetInstanceId_Type()
)
cucsVnicProfileSetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicProfileSetInstanceId.setStatus("current")
_CucsVnicProfileSetDn_Type = CucsManagedObjectDn
_CucsVnicProfileSetDn_Object = MibTableColumn
cucsVnicProfileSetDn = _CucsVnicProfileSetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30, 1, 2),
    _CucsVnicProfileSetDn_Type()
)
cucsVnicProfileSetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetDn.setStatus("current")
_CucsVnicProfileSetRn_Type = SnmpAdminString
_CucsVnicProfileSetRn_Object = MibTableColumn
cucsVnicProfileSetRn = _CucsVnicProfileSetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30, 1, 3),
    _CucsVnicProfileSetRn_Type()
)
cucsVnicProfileSetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetRn.setStatus("current")
_CucsVnicProfileSetFsmDescr_Type = SnmpAdminString
_CucsVnicProfileSetFsmDescr_Object = MibTableColumn
cucsVnicProfileSetFsmDescr = _CucsVnicProfileSetFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30, 1, 4),
    _CucsVnicProfileSetFsmDescr_Type()
)
cucsVnicProfileSetFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmDescr.setStatus("current")
_CucsVnicProfileSetFsmPrev_Type = SnmpAdminString
_CucsVnicProfileSetFsmPrev_Object = MibTableColumn
cucsVnicProfileSetFsmPrev = _CucsVnicProfileSetFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30, 1, 5),
    _CucsVnicProfileSetFsmPrev_Type()
)
cucsVnicProfileSetFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmPrev.setStatus("current")
_CucsVnicProfileSetFsmProgr_Type = Gauge32
_CucsVnicProfileSetFsmProgr_Object = MibTableColumn
cucsVnicProfileSetFsmProgr = _CucsVnicProfileSetFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30, 1, 6),
    _CucsVnicProfileSetFsmProgr_Type()
)
cucsVnicProfileSetFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmProgr.setStatus("current")
_CucsVnicProfileSetFsmRmtInvErrCode_Type = Gauge32
_CucsVnicProfileSetFsmRmtInvErrCode_Object = MibTableColumn
cucsVnicProfileSetFsmRmtInvErrCode = _CucsVnicProfileSetFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30, 1, 7),
    _CucsVnicProfileSetFsmRmtInvErrCode_Type()
)
cucsVnicProfileSetFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmRmtInvErrCode.setStatus("current")
_CucsVnicProfileSetFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsVnicProfileSetFsmRmtInvErrDescr_Object = MibTableColumn
cucsVnicProfileSetFsmRmtInvErrDescr = _CucsVnicProfileSetFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30, 1, 8),
    _CucsVnicProfileSetFsmRmtInvErrDescr_Type()
)
cucsVnicProfileSetFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmRmtInvErrDescr.setStatus("current")
_CucsVnicProfileSetFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsVnicProfileSetFsmRmtInvRslt_Object = MibTableColumn
cucsVnicProfileSetFsmRmtInvRslt = _CucsVnicProfileSetFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30, 1, 9),
    _CucsVnicProfileSetFsmRmtInvRslt_Type()
)
cucsVnicProfileSetFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmRmtInvRslt.setStatus("current")
_CucsVnicProfileSetFsmStageDescr_Type = SnmpAdminString
_CucsVnicProfileSetFsmStageDescr_Object = MibTableColumn
cucsVnicProfileSetFsmStageDescr = _CucsVnicProfileSetFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30, 1, 10),
    _CucsVnicProfileSetFsmStageDescr_Type()
)
cucsVnicProfileSetFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmStageDescr.setStatus("current")
_CucsVnicProfileSetFsmStamp_Type = DateAndTime
_CucsVnicProfileSetFsmStamp_Object = MibTableColumn
cucsVnicProfileSetFsmStamp = _CucsVnicProfileSetFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30, 1, 11),
    _CucsVnicProfileSetFsmStamp_Type()
)
cucsVnicProfileSetFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmStamp.setStatus("current")
_CucsVnicProfileSetFsmStatus_Type = SnmpAdminString
_CucsVnicProfileSetFsmStatus_Object = MibTableColumn
cucsVnicProfileSetFsmStatus = _CucsVnicProfileSetFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30, 1, 12),
    _CucsVnicProfileSetFsmStatus_Type()
)
cucsVnicProfileSetFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmStatus.setStatus("current")
_CucsVnicProfileSetFsmTry_Type = Gauge32
_CucsVnicProfileSetFsmTry_Object = MibTableColumn
cucsVnicProfileSetFsmTry = _CucsVnicProfileSetFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30, 1, 13),
    _CucsVnicProfileSetFsmTry_Type()
)
cucsVnicProfileSetFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmTry.setStatus("current")
_CucsVnicProfileSetFltAggr_Type = Unsigned64
_CucsVnicProfileSetFltAggr_Object = MibTableColumn
cucsVnicProfileSetFltAggr = _CucsVnicProfileSetFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30, 1, 14),
    _CucsVnicProfileSetFltAggr_Type()
)
cucsVnicProfileSetFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFltAggr.setStatus("current")
_CucsVnicProfileSetGenNum_Type = Gauge32
_CucsVnicProfileSetGenNum_Object = MibTableColumn
cucsVnicProfileSetGenNum = _CucsVnicProfileSetGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30, 1, 15),
    _CucsVnicProfileSetGenNum_Type()
)
cucsVnicProfileSetGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetGenNum.setStatus("current")
_CucsVnicProfileSetVlanGroupUpdate_Type = CucsVnicVlanGroupUpdate
_CucsVnicProfileSetVlanGroupUpdate_Object = MibTableColumn
cucsVnicProfileSetVlanGroupUpdate = _CucsVnicProfileSetVlanGroupUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 30, 1, 16),
    _CucsVnicProfileSetVlanGroupUpdate_Type()
)
cucsVnicProfileSetVlanGroupUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetVlanGroupUpdate.setStatus("current")
_CucsVnicProfileSetFsmTaskTable_Object = MibTable
cucsVnicProfileSetFsmTaskTable = _CucsVnicProfileSetFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 31)
)
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmTaskTable.setStatus("current")
_CucsVnicProfileSetFsmTaskEntry_Object = MibTableRow
cucsVnicProfileSetFsmTaskEntry = _CucsVnicProfileSetFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 31, 1)
)
cucsVnicProfileSetFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicProfileSetFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmTaskEntry.setStatus("current")
_CucsVnicProfileSetFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsVnicProfileSetFsmTaskInstanceId_Object = MibTableColumn
cucsVnicProfileSetFsmTaskInstanceId = _CucsVnicProfileSetFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 31, 1, 1),
    _CucsVnicProfileSetFsmTaskInstanceId_Type()
)
cucsVnicProfileSetFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmTaskInstanceId.setStatus("current")
_CucsVnicProfileSetFsmTaskDn_Type = CucsManagedObjectDn
_CucsVnicProfileSetFsmTaskDn_Object = MibTableColumn
cucsVnicProfileSetFsmTaskDn = _CucsVnicProfileSetFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 31, 1, 2),
    _CucsVnicProfileSetFsmTaskDn_Type()
)
cucsVnicProfileSetFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmTaskDn.setStatus("current")
_CucsVnicProfileSetFsmTaskRn_Type = SnmpAdminString
_CucsVnicProfileSetFsmTaskRn_Object = MibTableColumn
cucsVnicProfileSetFsmTaskRn = _CucsVnicProfileSetFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 31, 1, 3),
    _CucsVnicProfileSetFsmTaskRn_Type()
)
cucsVnicProfileSetFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmTaskRn.setStatus("current")
_CucsVnicProfileSetFsmTaskCompletion_Type = CucsFsmCompletion
_CucsVnicProfileSetFsmTaskCompletion_Object = MibTableColumn
cucsVnicProfileSetFsmTaskCompletion = _CucsVnicProfileSetFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 31, 1, 4),
    _CucsVnicProfileSetFsmTaskCompletion_Type()
)
cucsVnicProfileSetFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmTaskCompletion.setStatus("current")
_CucsVnicProfileSetFsmTaskFlags_Type = CucsFsmFlags
_CucsVnicProfileSetFsmTaskFlags_Object = MibTableColumn
cucsVnicProfileSetFsmTaskFlags = _CucsVnicProfileSetFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 31, 1, 5),
    _CucsVnicProfileSetFsmTaskFlags_Type()
)
cucsVnicProfileSetFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmTaskFlags.setStatus("current")
_CucsVnicProfileSetFsmTaskItem_Type = CucsVnicProfileSetFsmTaskItem
_CucsVnicProfileSetFsmTaskItem_Object = MibTableColumn
cucsVnicProfileSetFsmTaskItem = _CucsVnicProfileSetFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 31, 1, 6),
    _CucsVnicProfileSetFsmTaskItem_Type()
)
cucsVnicProfileSetFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmTaskItem.setStatus("current")
_CucsVnicProfileSetFsmTaskSeqId_Type = Gauge32
_CucsVnicProfileSetFsmTaskSeqId_Object = MibTableColumn
cucsVnicProfileSetFsmTaskSeqId = _CucsVnicProfileSetFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 31, 1, 7),
    _CucsVnicProfileSetFsmTaskSeqId_Type()
)
cucsVnicProfileSetFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmTaskSeqId.setStatus("current")
_CucsVnicSanConnTemplTable_Object = MibTable
cucsVnicSanConnTemplTable = _CucsVnicSanConnTemplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32)
)
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplTable.setStatus("current")
_CucsVnicSanConnTemplEntry_Object = MibTableRow
cucsVnicSanConnTemplEntry = _CucsVnicSanConnTemplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1)
)
cucsVnicSanConnTemplEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicSanConnTemplInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplEntry.setStatus("current")
_CucsVnicSanConnTemplInstanceId_Type = CucsManagedObjectId
_CucsVnicSanConnTemplInstanceId_Object = MibTableColumn
cucsVnicSanConnTemplInstanceId = _CucsVnicSanConnTemplInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 1),
    _CucsVnicSanConnTemplInstanceId_Type()
)
cucsVnicSanConnTemplInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplInstanceId.setStatus("current")
_CucsVnicSanConnTemplDn_Type = CucsManagedObjectDn
_CucsVnicSanConnTemplDn_Object = MibTableColumn
cucsVnicSanConnTemplDn = _CucsVnicSanConnTemplDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 2),
    _CucsVnicSanConnTemplDn_Type()
)
cucsVnicSanConnTemplDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplDn.setStatus("current")
_CucsVnicSanConnTemplRn_Type = SnmpAdminString
_CucsVnicSanConnTemplRn_Object = MibTableColumn
cucsVnicSanConnTemplRn = _CucsVnicSanConnTemplRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 3),
    _CucsVnicSanConnTemplRn_Type()
)
cucsVnicSanConnTemplRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplRn.setStatus("current")
_CucsVnicSanConnTemplDescr_Type = SnmpAdminString
_CucsVnicSanConnTemplDescr_Object = MibTableColumn
cucsVnicSanConnTemplDescr = _CucsVnicSanConnTemplDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 4),
    _CucsVnicSanConnTemplDescr_Type()
)
cucsVnicSanConnTemplDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplDescr.setStatus("current")
_CucsVnicSanConnTemplIdentPoolName_Type = SnmpAdminString
_CucsVnicSanConnTemplIdentPoolName_Object = MibTableColumn
cucsVnicSanConnTemplIdentPoolName = _CucsVnicSanConnTemplIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 5),
    _CucsVnicSanConnTemplIdentPoolName_Type()
)
cucsVnicSanConnTemplIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplIdentPoolName.setStatus("current")
_CucsVnicSanConnTemplIntId_Type = SnmpAdminString
_CucsVnicSanConnTemplIntId_Object = MibTableColumn
cucsVnicSanConnTemplIntId = _CucsVnicSanConnTemplIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 6),
    _CucsVnicSanConnTemplIntId_Type()
)
cucsVnicSanConnTemplIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplIntId.setStatus("current")
_CucsVnicSanConnTemplMaxDataFieldSize_Type = Gauge32
_CucsVnicSanConnTemplMaxDataFieldSize_Object = MibTableColumn
cucsVnicSanConnTemplMaxDataFieldSize = _CucsVnicSanConnTemplMaxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 7),
    _CucsVnicSanConnTemplMaxDataFieldSize_Type()
)
cucsVnicSanConnTemplMaxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplMaxDataFieldSize.setStatus("current")
_CucsVnicSanConnTemplName_Type = SnmpAdminString
_CucsVnicSanConnTemplName_Object = MibTableColumn
cucsVnicSanConnTemplName = _CucsVnicSanConnTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 8),
    _CucsVnicSanConnTemplName_Type()
)
cucsVnicSanConnTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplName.setStatus("current")
_CucsVnicSanConnTemplNwCtrlPolicyName_Type = SnmpAdminString
_CucsVnicSanConnTemplNwCtrlPolicyName_Object = MibTableColumn
cucsVnicSanConnTemplNwCtrlPolicyName = _CucsVnicSanConnTemplNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 9),
    _CucsVnicSanConnTemplNwCtrlPolicyName_Type()
)
cucsVnicSanConnTemplNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplNwCtrlPolicyName.setStatus("current")
_CucsVnicSanConnTemplOperIdentPoolName_Type = SnmpAdminString
_CucsVnicSanConnTemplOperIdentPoolName_Object = MibTableColumn
cucsVnicSanConnTemplOperIdentPoolName = _CucsVnicSanConnTemplOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 10),
    _CucsVnicSanConnTemplOperIdentPoolName_Type()
)
cucsVnicSanConnTemplOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplOperIdentPoolName.setStatus("current")
_CucsVnicSanConnTemplOperQosPolicyName_Type = SnmpAdminString
_CucsVnicSanConnTemplOperQosPolicyName_Object = MibTableColumn
cucsVnicSanConnTemplOperQosPolicyName = _CucsVnicSanConnTemplOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 11),
    _CucsVnicSanConnTemplOperQosPolicyName_Type()
)
cucsVnicSanConnTemplOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplOperQosPolicyName.setStatus("current")
_CucsVnicSanConnTemplOperStatsPolicyName_Type = SnmpAdminString
_CucsVnicSanConnTemplOperStatsPolicyName_Object = MibTableColumn
cucsVnicSanConnTemplOperStatsPolicyName = _CucsVnicSanConnTemplOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 12),
    _CucsVnicSanConnTemplOperStatsPolicyName_Type()
)
cucsVnicSanConnTemplOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplOperStatsPolicyName.setStatus("current")
_CucsVnicSanConnTemplPinToGroupName_Type = SnmpAdminString
_CucsVnicSanConnTemplPinToGroupName_Object = MibTableColumn
cucsVnicSanConnTemplPinToGroupName = _CucsVnicSanConnTemplPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 13),
    _CucsVnicSanConnTemplPinToGroupName_Type()
)
cucsVnicSanConnTemplPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplPinToGroupName.setStatus("current")
_CucsVnicSanConnTemplQosPolicyName_Type = SnmpAdminString
_CucsVnicSanConnTemplQosPolicyName_Object = MibTableColumn
cucsVnicSanConnTemplQosPolicyName = _CucsVnicSanConnTemplQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 14),
    _CucsVnicSanConnTemplQosPolicyName_Type()
)
cucsVnicSanConnTemplQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplQosPolicyName.setStatus("current")
_CucsVnicSanConnTemplStatsPolicyName_Type = SnmpAdminString
_CucsVnicSanConnTemplStatsPolicyName_Object = MibTableColumn
cucsVnicSanConnTemplStatsPolicyName = _CucsVnicSanConnTemplStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 15),
    _CucsVnicSanConnTemplStatsPolicyName_Type()
)
cucsVnicSanConnTemplStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplStatsPolicyName.setStatus("current")
_CucsVnicSanConnTemplSwitchId_Type = CucsNetworkSwitchId
_CucsVnicSanConnTemplSwitchId_Object = MibTableColumn
cucsVnicSanConnTemplSwitchId = _CucsVnicSanConnTemplSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 16),
    _CucsVnicSanConnTemplSwitchId_Type()
)
cucsVnicSanConnTemplSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplSwitchId.setStatus("current")
_CucsVnicSanConnTemplTarget_Type = CucsVnicSanConnTemplTarget
_CucsVnicSanConnTemplTarget_Object = MibTableColumn
cucsVnicSanConnTemplTarget = _CucsVnicSanConnTemplTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 17),
    _CucsVnicSanConnTemplTarget_Type()
)
cucsVnicSanConnTemplTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplTarget.setStatus("current")
_CucsVnicSanConnTemplTemplType_Type = CucsVnicTemplateType
_CucsVnicSanConnTemplTemplType_Object = MibTableColumn
cucsVnicSanConnTemplTemplType = _CucsVnicSanConnTemplTemplType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 18),
    _CucsVnicSanConnTemplTemplType_Type()
)
cucsVnicSanConnTemplTemplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplTemplType.setStatus("current")
_CucsVnicSanConnTemplPolicyLevel_Type = Gauge32
_CucsVnicSanConnTemplPolicyLevel_Object = MibTableColumn
cucsVnicSanConnTemplPolicyLevel = _CucsVnicSanConnTemplPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 19),
    _CucsVnicSanConnTemplPolicyLevel_Type()
)
cucsVnicSanConnTemplPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplPolicyLevel.setStatus("current")
_CucsVnicSanConnTemplPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicSanConnTemplPolicyOwner_Object = MibTableColumn
cucsVnicSanConnTemplPolicyOwner = _CucsVnicSanConnTemplPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 32, 1, 20),
    _CucsVnicSanConnTemplPolicyOwner_Type()
)
cucsVnicSanConnTemplPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnTemplPolicyOwner.setStatus("current")
_CucsVnicScsiTable_Object = MibTable
cucsVnicScsiTable = _CucsVnicScsiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33)
)
if mibBuilder.loadTexts:
    cucsVnicScsiTable.setStatus("current")
_CucsVnicScsiEntry_Object = MibTableRow
cucsVnicScsiEntry = _CucsVnicScsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1)
)
cucsVnicScsiEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicScsiInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicScsiEntry.setStatus("current")
_CucsVnicScsiInstanceId_Type = CucsManagedObjectId
_CucsVnicScsiInstanceId_Object = MibTableColumn
cucsVnicScsiInstanceId = _CucsVnicScsiInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 1),
    _CucsVnicScsiInstanceId_Type()
)
cucsVnicScsiInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicScsiInstanceId.setStatus("current")
_CucsVnicScsiDn_Type = CucsManagedObjectDn
_CucsVnicScsiDn_Object = MibTableColumn
cucsVnicScsiDn = _CucsVnicScsiDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 2),
    _CucsVnicScsiDn_Type()
)
cucsVnicScsiDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiDn.setStatus("current")
_CucsVnicScsiRn_Type = SnmpAdminString
_CucsVnicScsiRn_Object = MibTableColumn
cucsVnicScsiRn = _CucsVnicScsiRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 3),
    _CucsVnicScsiRn_Type()
)
cucsVnicScsiRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiRn.setStatus("current")
_CucsVnicScsiAdaptorProfileName_Type = SnmpAdminString
_CucsVnicScsiAdaptorProfileName_Object = MibTableColumn
cucsVnicScsiAdaptorProfileName = _CucsVnicScsiAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 4),
    _CucsVnicScsiAdaptorProfileName_Type()
)
cucsVnicScsiAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiAdaptorProfileName.setStatus("current")
_CucsVnicScsiAdminVcon_Type = SnmpAdminString
_CucsVnicScsiAdminVcon_Object = MibTableColumn
cucsVnicScsiAdminVcon = _CucsVnicScsiAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 5),
    _CucsVnicScsiAdminVcon_Type()
)
cucsVnicScsiAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiAdminVcon.setStatus("current")
_CucsVnicScsiBootDev_Type = CucsVnicVnicBootDev
_CucsVnicScsiBootDev_Object = MibTableColumn
cucsVnicScsiBootDev = _CucsVnicScsiBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 6),
    _CucsVnicScsiBootDev_Type()
)
cucsVnicScsiBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiBootDev.setStatus("current")
_CucsVnicScsiConfigState_Type = CucsLsConfigState
_CucsVnicScsiConfigState_Object = MibTableColumn
cucsVnicScsiConfigState = _CucsVnicScsiConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 7),
    _CucsVnicScsiConfigState_Type()
)
cucsVnicScsiConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiConfigState.setStatus("current")
_CucsVnicScsiEquipmentDn_Type = SnmpAdminString
_CucsVnicScsiEquipmentDn_Object = MibTableColumn
cucsVnicScsiEquipmentDn = _CucsVnicScsiEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 8),
    _CucsVnicScsiEquipmentDn_Type()
)
cucsVnicScsiEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiEquipmentDn.setStatus("current")
_CucsVnicScsiIdentPoolName_Type = SnmpAdminString
_CucsVnicScsiIdentPoolName_Object = MibTableColumn
cucsVnicScsiIdentPoolName = _CucsVnicScsiIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 9),
    _CucsVnicScsiIdentPoolName_Type()
)
cucsVnicScsiIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiIdentPoolName.setStatus("current")
_CucsVnicScsiInstType_Type = CucsVnicInstantiation
_CucsVnicScsiInstType_Object = MibTableColumn
cucsVnicScsiInstType = _CucsVnicScsiInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 10),
    _CucsVnicScsiInstType_Type()
)
cucsVnicScsiInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiInstType.setStatus("current")
_CucsVnicScsiName_Type = SnmpAdminString
_CucsVnicScsiName_Object = MibTableColumn
cucsVnicScsiName = _CucsVnicScsiName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 11),
    _CucsVnicScsiName_Type()
)
cucsVnicScsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiName.setStatus("current")
_CucsVnicScsiNwTemplName_Type = SnmpAdminString
_CucsVnicScsiNwTemplName_Object = MibTableColumn
cucsVnicScsiNwTemplName = _CucsVnicScsiNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 12),
    _CucsVnicScsiNwTemplName_Type()
)
cucsVnicScsiNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiNwTemplName.setStatus("current")
_CucsVnicScsiOperOrder_Type = Gauge32
_CucsVnicScsiOperOrder_Object = MibTableColumn
cucsVnicScsiOperOrder = _CucsVnicScsiOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 13),
    _CucsVnicScsiOperOrder_Type()
)
cucsVnicScsiOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiOperOrder.setStatus("current")
_CucsVnicScsiOperSpeed_Type = Gauge32
_CucsVnicScsiOperSpeed_Object = MibTableColumn
cucsVnicScsiOperSpeed = _CucsVnicScsiOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 14),
    _CucsVnicScsiOperSpeed_Type()
)
cucsVnicScsiOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiOperSpeed.setStatus("current")
_CucsVnicScsiOperStatsPolicyName_Type = SnmpAdminString
_CucsVnicScsiOperStatsPolicyName_Object = MibTableColumn
cucsVnicScsiOperStatsPolicyName = _CucsVnicScsiOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 15),
    _CucsVnicScsiOperStatsPolicyName_Type()
)
cucsVnicScsiOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiOperStatsPolicyName.setStatus("current")
_CucsVnicScsiOperVcon_Type = SnmpAdminString
_CucsVnicScsiOperVcon_Object = MibTableColumn
cucsVnicScsiOperVcon = _CucsVnicScsiOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 16),
    _CucsVnicScsiOperVcon_Type()
)
cucsVnicScsiOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiOperVcon.setStatus("current")
_CucsVnicScsiOrder_Type = Gauge32
_CucsVnicScsiOrder_Object = MibTableColumn
cucsVnicScsiOrder = _CucsVnicScsiOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 17),
    _CucsVnicScsiOrder_Type()
)
cucsVnicScsiOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiOrder.setStatus("current")
_CucsVnicScsiOwner_Type = CucsVnicConnectionOwner
_CucsVnicScsiOwner_Object = MibTableColumn
cucsVnicScsiOwner = _CucsVnicScsiOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 18),
    _CucsVnicScsiOwner_Type()
)
cucsVnicScsiOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiOwner.setStatus("current")
_CucsVnicScsiPinToGroupName_Type = SnmpAdminString
_CucsVnicScsiPinToGroupName_Object = MibTableColumn
cucsVnicScsiPinToGroupName = _CucsVnicScsiPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 19),
    _CucsVnicScsiPinToGroupName_Type()
)
cucsVnicScsiPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiPinToGroupName.setStatus("current")
_CucsVnicScsiQosPolicyName_Type = SnmpAdminString
_CucsVnicScsiQosPolicyName_Object = MibTableColumn
cucsVnicScsiQosPolicyName = _CucsVnicScsiQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 20),
    _CucsVnicScsiQosPolicyName_Type()
)
cucsVnicScsiQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiQosPolicyName.setStatus("current")
_CucsVnicScsiStatsPolicyName_Type = SnmpAdminString
_CucsVnicScsiStatsPolicyName_Object = MibTableColumn
cucsVnicScsiStatsPolicyName = _CucsVnicScsiStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 21),
    _CucsVnicScsiStatsPolicyName_Type()
)
cucsVnicScsiStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiStatsPolicyName.setStatus("current")
_CucsVnicScsiSwitchId_Type = CucsNetworkSwitchId
_CucsVnicScsiSwitchId_Object = MibTableColumn
cucsVnicScsiSwitchId = _CucsVnicScsiSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 22),
    _CucsVnicScsiSwitchId_Type()
)
cucsVnicScsiSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiSwitchId.setStatus("current")
_CucsVnicScsiType_Type = CucsVnicScsiType
_CucsVnicScsiType_Object = MibTableColumn
cucsVnicScsiType = _CucsVnicScsiType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 23),
    _CucsVnicScsiType_Type()
)
cucsVnicScsiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiType.setStatus("current")
_CucsVnicScsiConfigQualifier_Type = CucsVnicConfigIssues
_CucsVnicScsiConfigQualifier_Object = MibTableColumn
cucsVnicScsiConfigQualifier = _CucsVnicScsiConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 25),
    _CucsVnicScsiConfigQualifier_Type()
)
cucsVnicScsiConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiConfigQualifier.setStatus("current")
_CucsVnicScsiAdminHostPort_Type = CucsFabricHostPortId
_CucsVnicScsiAdminHostPort_Object = MibTableColumn
cucsVnicScsiAdminHostPort = _CucsVnicScsiAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 27),
    _CucsVnicScsiAdminHostPort_Type()
)
cucsVnicScsiAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiAdminHostPort.setStatus("current")
_CucsVnicScsiOperHostPort_Type = CucsVnicVnicOperHostPort
_CucsVnicScsiOperHostPort_Object = MibTableColumn
cucsVnicScsiOperHostPort = _CucsVnicScsiOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 28),
    _CucsVnicScsiOperHostPort_Type()
)
cucsVnicScsiOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiOperHostPort.setStatus("current")
_CucsVnicScsiAdminCdnName_Type = SnmpAdminString
_CucsVnicScsiAdminCdnName_Object = MibTableColumn
cucsVnicScsiAdminCdnName = _CucsVnicScsiAdminCdnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 29),
    _CucsVnicScsiAdminCdnName_Type()
)
cucsVnicScsiAdminCdnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiAdminCdnName.setStatus("current")
_CucsVnicScsiOperCdnName_Type = SnmpAdminString
_CucsVnicScsiOperCdnName_Object = MibTableColumn
cucsVnicScsiOperCdnName = _CucsVnicScsiOperCdnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 30),
    _CucsVnicScsiOperCdnName_Type()
)
cucsVnicScsiOperCdnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiOperCdnName.setStatus("current")
_CucsVnicScsiCdnPropInSync_Type = TruthValue
_CucsVnicScsiCdnPropInSync_Object = MibTableColumn
cucsVnicScsiCdnPropInSync = _CucsVnicScsiCdnPropInSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 31),
    _CucsVnicScsiCdnPropInSync_Type()
)
cucsVnicScsiCdnPropInSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiCdnPropInSync.setStatus("current")
_CucsVnicScsiCdnSource_Type = CucsVnicCdnSource
_CucsVnicScsiCdnSource_Object = MibTableColumn
cucsVnicScsiCdnSource = _CucsVnicScsiCdnSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 33, 1, 32),
    _CucsVnicScsiCdnSource_Type()
)
cucsVnicScsiCdnSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiCdnSource.setStatus("current")
_CucsVnicScsiIfTable_Object = MibTable
cucsVnicScsiIfTable = _CucsVnicScsiIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34)
)
if mibBuilder.loadTexts:
    cucsVnicScsiIfTable.setStatus("current")
_CucsVnicScsiIfEntry_Object = MibTableRow
cucsVnicScsiIfEntry = _CucsVnicScsiIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1)
)
cucsVnicScsiIfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicScsiIfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicScsiIfEntry.setStatus("current")
_CucsVnicScsiIfInstanceId_Type = CucsManagedObjectId
_CucsVnicScsiIfInstanceId_Object = MibTableColumn
cucsVnicScsiIfInstanceId = _CucsVnicScsiIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1, 1),
    _CucsVnicScsiIfInstanceId_Type()
)
cucsVnicScsiIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicScsiIfInstanceId.setStatus("current")
_CucsVnicScsiIfDn_Type = CucsManagedObjectDn
_CucsVnicScsiIfDn_Object = MibTableColumn
cucsVnicScsiIfDn = _CucsVnicScsiIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1, 2),
    _CucsVnicScsiIfDn_Type()
)
cucsVnicScsiIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiIfDn.setStatus("current")
_CucsVnicScsiIfRn_Type = SnmpAdminString
_CucsVnicScsiIfRn_Object = MibTableColumn
cucsVnicScsiIfRn = _CucsVnicScsiIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1, 3),
    _CucsVnicScsiIfRn_Type()
)
cucsVnicScsiIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiIfRn.setStatus("current")
_CucsVnicScsiIfAddr_Type = Unsigned64
_CucsVnicScsiIfAddr_Object = MibTableColumn
cucsVnicScsiIfAddr = _CucsVnicScsiIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1, 4),
    _CucsVnicScsiIfAddr_Type()
)
cucsVnicScsiIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiIfAddr.setStatus("current")
_CucsVnicScsiIfName_Type = SnmpAdminString
_CucsVnicScsiIfName_Object = MibTableColumn
cucsVnicScsiIfName = _CucsVnicScsiIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1, 5),
    _CucsVnicScsiIfName_Type()
)
cucsVnicScsiIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiIfName.setStatus("current")
_CucsVnicScsiIfOperState_Type = CucsVnicIfOperState
_CucsVnicScsiIfOperState_Object = MibTableColumn
cucsVnicScsiIfOperState = _CucsVnicScsiIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1, 6),
    _CucsVnicScsiIfOperState_Type()
)
cucsVnicScsiIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiIfOperState.setStatus("current")
_CucsVnicScsiIfOwner_Type = CucsVnicConnectionOwner
_CucsVnicScsiIfOwner_Object = MibTableColumn
cucsVnicScsiIfOwner = _CucsVnicScsiIfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1, 7),
    _CucsVnicScsiIfOwner_Type()
)
cucsVnicScsiIfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiIfOwner.setStatus("current")
_CucsVnicScsiIfSwitchId_Type = CucsNetworkSwitchId
_CucsVnicScsiIfSwitchId_Object = MibTableColumn
cucsVnicScsiIfSwitchId = _CucsVnicScsiIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1, 8),
    _CucsVnicScsiIfSwitchId_Type()
)
cucsVnicScsiIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiIfSwitchId.setStatus("current")
_CucsVnicScsiIfType_Type = CucsVnicAScsiIfType
_CucsVnicScsiIfType_Object = MibTableColumn
cucsVnicScsiIfType = _CucsVnicScsiIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1, 9),
    _CucsVnicScsiIfType_Type()
)
cucsVnicScsiIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiIfType.setStatus("current")
_CucsVnicScsiIfVnet_Type = Gauge32
_CucsVnicScsiIfVnet_Object = MibTableColumn
cucsVnicScsiIfVnet = _CucsVnicScsiIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1, 10),
    _CucsVnicScsiIfVnet_Type()
)
cucsVnicScsiIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiIfVnet.setStatus("current")
_CucsVnicScsiIfConfigQualifier_Type = CucsVnicConfigIssues
_CucsVnicScsiIfConfigQualifier_Object = MibTableColumn
cucsVnicScsiIfConfigQualifier = _CucsVnicScsiIfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1, 11),
    _CucsVnicScsiIfConfigQualifier_Type()
)
cucsVnicScsiIfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiIfConfigQualifier.setStatus("current")
_CucsVnicScsiIfOperVnetDn_Type = SnmpAdminString
_CucsVnicScsiIfOperVnetDn_Object = MibTableColumn
cucsVnicScsiIfOperVnetDn = _CucsVnicScsiIfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1, 13),
    _CucsVnicScsiIfOperVnetDn_Type()
)
cucsVnicScsiIfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiIfOperVnetDn.setStatus("current")
_CucsVnicScsiIfOperVnetName_Type = SnmpAdminString
_CucsVnicScsiIfOperVnetName_Object = MibTableColumn
cucsVnicScsiIfOperVnetName = _CucsVnicScsiIfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1, 14),
    _CucsVnicScsiIfOperVnetName_Type()
)
cucsVnicScsiIfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiIfOperVnetName.setStatus("current")
_CucsVnicScsiIfPubNwId_Type = Gauge32
_CucsVnicScsiIfPubNwId_Object = MibTableColumn
cucsVnicScsiIfPubNwId = _CucsVnicScsiIfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1, 15),
    _CucsVnicScsiIfPubNwId_Type()
)
cucsVnicScsiIfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiIfPubNwId.setStatus("current")
_CucsVnicScsiIfSharing_Type = CucsFabricVlanSharingType
_CucsVnicScsiIfSharing_Object = MibTableColumn
cucsVnicScsiIfSharing = _CucsVnicScsiIfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1, 16),
    _CucsVnicScsiIfSharing_Type()
)
cucsVnicScsiIfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiIfSharing.setStatus("current")
_CucsVnicScsiIfOperPrimaryVnetDn_Type = SnmpAdminString
_CucsVnicScsiIfOperPrimaryVnetDn_Object = MibTableColumn
cucsVnicScsiIfOperPrimaryVnetDn = _CucsVnicScsiIfOperPrimaryVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1, 17),
    _CucsVnicScsiIfOperPrimaryVnetDn_Type()
)
cucsVnicScsiIfOperPrimaryVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiIfOperPrimaryVnetDn.setStatus("current")
_CucsVnicScsiIfOperPrimaryVnetName_Type = SnmpAdminString
_CucsVnicScsiIfOperPrimaryVnetName_Object = MibTableColumn
cucsVnicScsiIfOperPrimaryVnetName = _CucsVnicScsiIfOperPrimaryVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 34, 1, 18),
    _CucsVnicScsiIfOperPrimaryVnetName_Type()
)
cucsVnicScsiIfOperPrimaryVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicScsiIfOperPrimaryVnetName.setStatus("current")
_CucsVnicBootIpPolicyTable_Object = MibTable
cucsVnicBootIpPolicyTable = _CucsVnicBootIpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 35)
)
if mibBuilder.loadTexts:
    cucsVnicBootIpPolicyTable.setStatus("current")
_CucsVnicBootIpPolicyEntry_Object = MibTableRow
cucsVnicBootIpPolicyEntry = _CucsVnicBootIpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 35, 1)
)
cucsVnicBootIpPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicBootIpPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicBootIpPolicyEntry.setStatus("current")
_CucsVnicBootIpPolicyInstanceId_Type = CucsManagedObjectId
_CucsVnicBootIpPolicyInstanceId_Object = MibTableColumn
cucsVnicBootIpPolicyInstanceId = _CucsVnicBootIpPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 35, 1, 1),
    _CucsVnicBootIpPolicyInstanceId_Type()
)
cucsVnicBootIpPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicBootIpPolicyInstanceId.setStatus("current")
_CucsVnicBootIpPolicyDn_Type = CucsManagedObjectDn
_CucsVnicBootIpPolicyDn_Object = MibTableColumn
cucsVnicBootIpPolicyDn = _CucsVnicBootIpPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 35, 1, 2),
    _CucsVnicBootIpPolicyDn_Type()
)
cucsVnicBootIpPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicBootIpPolicyDn.setStatus("current")
_CucsVnicBootIpPolicyRn_Type = SnmpAdminString
_CucsVnicBootIpPolicyRn_Object = MibTableColumn
cucsVnicBootIpPolicyRn = _CucsVnicBootIpPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 35, 1, 3),
    _CucsVnicBootIpPolicyRn_Type()
)
cucsVnicBootIpPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicBootIpPolicyRn.setStatus("current")
_CucsVnicBootIpPolicyDescr_Type = SnmpAdminString
_CucsVnicBootIpPolicyDescr_Object = MibTableColumn
cucsVnicBootIpPolicyDescr = _CucsVnicBootIpPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 35, 1, 4),
    _CucsVnicBootIpPolicyDescr_Type()
)
cucsVnicBootIpPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicBootIpPolicyDescr.setStatus("current")
_CucsVnicBootIpPolicyIntId_Type = SnmpAdminString
_CucsVnicBootIpPolicyIntId_Object = MibTableColumn
cucsVnicBootIpPolicyIntId = _CucsVnicBootIpPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 35, 1, 5),
    _CucsVnicBootIpPolicyIntId_Type()
)
cucsVnicBootIpPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicBootIpPolicyIntId.setStatus("current")
_CucsVnicBootIpPolicyName_Type = SnmpAdminString
_CucsVnicBootIpPolicyName_Object = MibTableColumn
cucsVnicBootIpPolicyName = _CucsVnicBootIpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 35, 1, 6),
    _CucsVnicBootIpPolicyName_Type()
)
cucsVnicBootIpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicBootIpPolicyName.setStatus("current")
_CucsVnicBootIpPolicyPoolName_Type = SnmpAdminString
_CucsVnicBootIpPolicyPoolName_Object = MibTableColumn
cucsVnicBootIpPolicyPoolName = _CucsVnicBootIpPolicyPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 35, 1, 7),
    _CucsVnicBootIpPolicyPoolName_Type()
)
cucsVnicBootIpPolicyPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicBootIpPolicyPoolName.setStatus("current")
_CucsVnicBootIpPolicyPolicyLevel_Type = Gauge32
_CucsVnicBootIpPolicyPolicyLevel_Object = MibTableColumn
cucsVnicBootIpPolicyPolicyLevel = _CucsVnicBootIpPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 35, 1, 8),
    _CucsVnicBootIpPolicyPolicyLevel_Type()
)
cucsVnicBootIpPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicBootIpPolicyPolicyLevel.setStatus("current")
_CucsVnicBootIpPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicBootIpPolicyPolicyOwner_Object = MibTableColumn
cucsVnicBootIpPolicyPolicyOwner = _CucsVnicBootIpPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 35, 1, 9),
    _CucsVnicBootIpPolicyPolicyOwner_Type()
)
cucsVnicBootIpPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicBootIpPolicyPolicyOwner.setStatus("current")
_CucsVnicIPv4IscsiAddrTable_Object = MibTable
cucsVnicIPv4IscsiAddrTable = _CucsVnicIPv4IscsiAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 36)
)
if mibBuilder.loadTexts:
    cucsVnicIPv4IscsiAddrTable.setStatus("current")
_CucsVnicIPv4IscsiAddrEntry_Object = MibTableRow
cucsVnicIPv4IscsiAddrEntry = _CucsVnicIPv4IscsiAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 36, 1)
)
cucsVnicIPv4IscsiAddrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIPv4IscsiAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIPv4IscsiAddrEntry.setStatus("current")
_CucsVnicIPv4IscsiAddrInstanceId_Type = CucsManagedObjectId
_CucsVnicIPv4IscsiAddrInstanceId_Object = MibTableColumn
cucsVnicIPv4IscsiAddrInstanceId = _CucsVnicIPv4IscsiAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 36, 1, 1),
    _CucsVnicIPv4IscsiAddrInstanceId_Type()
)
cucsVnicIPv4IscsiAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIPv4IscsiAddrInstanceId.setStatus("current")
_CucsVnicIPv4IscsiAddrDn_Type = CucsManagedObjectDn
_CucsVnicIPv4IscsiAddrDn_Object = MibTableColumn
cucsVnicIPv4IscsiAddrDn = _CucsVnicIPv4IscsiAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 36, 1, 2),
    _CucsVnicIPv4IscsiAddrDn_Type()
)
cucsVnicIPv4IscsiAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IscsiAddrDn.setStatus("current")
_CucsVnicIPv4IscsiAddrRn_Type = SnmpAdminString
_CucsVnicIPv4IscsiAddrRn_Object = MibTableColumn
cucsVnicIPv4IscsiAddrRn = _CucsVnicIPv4IscsiAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 36, 1, 3),
    _CucsVnicIPv4IscsiAddrRn_Type()
)
cucsVnicIPv4IscsiAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IscsiAddrRn.setStatus("current")
_CucsVnicIPv4IscsiAddrAddr_Type = InetAddressIPv4
_CucsVnicIPv4IscsiAddrAddr_Object = MibTableColumn
cucsVnicIPv4IscsiAddrAddr = _CucsVnicIPv4IscsiAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 36, 1, 4),
    _CucsVnicIPv4IscsiAddrAddr_Type()
)
cucsVnicIPv4IscsiAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IscsiAddrAddr.setStatus("current")
_CucsVnicIPv4IscsiAddrDefGw_Type = InetAddressIPv4
_CucsVnicIPv4IscsiAddrDefGw_Object = MibTableColumn
cucsVnicIPv4IscsiAddrDefGw = _CucsVnicIPv4IscsiAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 36, 1, 5),
    _CucsVnicIPv4IscsiAddrDefGw_Type()
)
cucsVnicIPv4IscsiAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IscsiAddrDefGw.setStatus("current")
_CucsVnicIPv4IscsiAddrPrimDns_Type = InetAddressIPv4
_CucsVnicIPv4IscsiAddrPrimDns_Object = MibTableColumn
cucsVnicIPv4IscsiAddrPrimDns = _CucsVnicIPv4IscsiAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 36, 1, 6),
    _CucsVnicIPv4IscsiAddrPrimDns_Type()
)
cucsVnicIPv4IscsiAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IscsiAddrPrimDns.setStatus("current")
_CucsVnicIPv4IscsiAddrSecDns_Type = InetAddressIPv4
_CucsVnicIPv4IscsiAddrSecDns_Object = MibTableColumn
cucsVnicIPv4IscsiAddrSecDns = _CucsVnicIPv4IscsiAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 36, 1, 7),
    _CucsVnicIPv4IscsiAddrSecDns_Type()
)
cucsVnicIPv4IscsiAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IscsiAddrSecDns.setStatus("current")
_CucsVnicIPv4IscsiAddrSubnet_Type = InetAddressIPv4
_CucsVnicIPv4IscsiAddrSubnet_Object = MibTableColumn
cucsVnicIPv4IscsiAddrSubnet = _CucsVnicIPv4IscsiAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 36, 1, 8),
    _CucsVnicIPv4IscsiAddrSubnet_Type()
)
cucsVnicIPv4IscsiAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4IscsiAddrSubnet.setStatus("current")
_CucsVnicIPv4PooledIscsiAddrTable_Object = MibTable
cucsVnicIPv4PooledIscsiAddrTable = _CucsVnicIPv4PooledIscsiAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 37)
)
if mibBuilder.loadTexts:
    cucsVnicIPv4PooledIscsiAddrTable.setStatus("current")
_CucsVnicIPv4PooledIscsiAddrEntry_Object = MibTableRow
cucsVnicIPv4PooledIscsiAddrEntry = _CucsVnicIPv4PooledIscsiAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 37, 1)
)
cucsVnicIPv4PooledIscsiAddrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIPv4PooledIscsiAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIPv4PooledIscsiAddrEntry.setStatus("current")
_CucsVnicIPv4PooledIscsiAddrInstanceId_Type = CucsManagedObjectId
_CucsVnicIPv4PooledIscsiAddrInstanceId_Object = MibTableColumn
cucsVnicIPv4PooledIscsiAddrInstanceId = _CucsVnicIPv4PooledIscsiAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 37, 1, 1),
    _CucsVnicIPv4PooledIscsiAddrInstanceId_Type()
)
cucsVnicIPv4PooledIscsiAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIPv4PooledIscsiAddrInstanceId.setStatus("current")
_CucsVnicIPv4PooledIscsiAddrDn_Type = CucsManagedObjectDn
_CucsVnicIPv4PooledIscsiAddrDn_Object = MibTableColumn
cucsVnicIPv4PooledIscsiAddrDn = _CucsVnicIPv4PooledIscsiAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 37, 1, 2),
    _CucsVnicIPv4PooledIscsiAddrDn_Type()
)
cucsVnicIPv4PooledIscsiAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4PooledIscsiAddrDn.setStatus("current")
_CucsVnicIPv4PooledIscsiAddrRn_Type = SnmpAdminString
_CucsVnicIPv4PooledIscsiAddrRn_Object = MibTableColumn
cucsVnicIPv4PooledIscsiAddrRn = _CucsVnicIPv4PooledIscsiAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 37, 1, 3),
    _CucsVnicIPv4PooledIscsiAddrRn_Type()
)
cucsVnicIPv4PooledIscsiAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4PooledIscsiAddrRn.setStatus("current")
_CucsVnicIPv4PooledIscsiAddrAddr_Type = InetAddressIPv4
_CucsVnicIPv4PooledIscsiAddrAddr_Object = MibTableColumn
cucsVnicIPv4PooledIscsiAddrAddr = _CucsVnicIPv4PooledIscsiAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 37, 1, 4),
    _CucsVnicIPv4PooledIscsiAddrAddr_Type()
)
cucsVnicIPv4PooledIscsiAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4PooledIscsiAddrAddr.setStatus("current")
_CucsVnicIPv4PooledIscsiAddrDefGw_Type = InetAddressIPv4
_CucsVnicIPv4PooledIscsiAddrDefGw_Object = MibTableColumn
cucsVnicIPv4PooledIscsiAddrDefGw = _CucsVnicIPv4PooledIscsiAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 37, 1, 5),
    _CucsVnicIPv4PooledIscsiAddrDefGw_Type()
)
cucsVnicIPv4PooledIscsiAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4PooledIscsiAddrDefGw.setStatus("current")
_CucsVnicIPv4PooledIscsiAddrIdentPoolName_Type = SnmpAdminString
_CucsVnicIPv4PooledIscsiAddrIdentPoolName_Object = MibTableColumn
cucsVnicIPv4PooledIscsiAddrIdentPoolName = _CucsVnicIPv4PooledIscsiAddrIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 37, 1, 6),
    _CucsVnicIPv4PooledIscsiAddrIdentPoolName_Type()
)
cucsVnicIPv4PooledIscsiAddrIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4PooledIscsiAddrIdentPoolName.setStatus("current")
_CucsVnicIPv4PooledIscsiAddrOperIdentPoolName_Type = SnmpAdminString
_CucsVnicIPv4PooledIscsiAddrOperIdentPoolName_Object = MibTableColumn
cucsVnicIPv4PooledIscsiAddrOperIdentPoolName = _CucsVnicIPv4PooledIscsiAddrOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 37, 1, 7),
    _CucsVnicIPv4PooledIscsiAddrOperIdentPoolName_Type()
)
cucsVnicIPv4PooledIscsiAddrOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4PooledIscsiAddrOperIdentPoolName.setStatus("current")
_CucsVnicIPv4PooledIscsiAddrPrimDns_Type = InetAddressIPv4
_CucsVnicIPv4PooledIscsiAddrPrimDns_Object = MibTableColumn
cucsVnicIPv4PooledIscsiAddrPrimDns = _CucsVnicIPv4PooledIscsiAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 37, 1, 8),
    _CucsVnicIPv4PooledIscsiAddrPrimDns_Type()
)
cucsVnicIPv4PooledIscsiAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4PooledIscsiAddrPrimDns.setStatus("current")
_CucsVnicIPv4PooledIscsiAddrSecDns_Type = InetAddressIPv4
_CucsVnicIPv4PooledIscsiAddrSecDns_Object = MibTableColumn
cucsVnicIPv4PooledIscsiAddrSecDns = _CucsVnicIPv4PooledIscsiAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 37, 1, 9),
    _CucsVnicIPv4PooledIscsiAddrSecDns_Type()
)
cucsVnicIPv4PooledIscsiAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4PooledIscsiAddrSecDns.setStatus("current")
_CucsVnicIPv4PooledIscsiAddrSubnet_Type = InetAddressIPv4
_CucsVnicIPv4PooledIscsiAddrSubnet_Object = MibTableColumn
cucsVnicIPv4PooledIscsiAddrSubnet = _CucsVnicIPv4PooledIscsiAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 37, 1, 10),
    _CucsVnicIPv4PooledIscsiAddrSubnet_Type()
)
cucsVnicIPv4PooledIscsiAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv4PooledIscsiAddrSubnet.setStatus("current")
_CucsVnicIScsiTable_Object = MibTable
cucsVnicIScsiTable = _CucsVnicIScsiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38)
)
if mibBuilder.loadTexts:
    cucsVnicIScsiTable.setStatus("current")
_CucsVnicIScsiEntry_Object = MibTableRow
cucsVnicIScsiEntry = _CucsVnicIScsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1)
)
cucsVnicIScsiEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIScsiInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIScsiEntry.setStatus("current")
_CucsVnicIScsiInstanceId_Type = CucsManagedObjectId
_CucsVnicIScsiInstanceId_Object = MibTableColumn
cucsVnicIScsiInstanceId = _CucsVnicIScsiInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 1),
    _CucsVnicIScsiInstanceId_Type()
)
cucsVnicIScsiInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIScsiInstanceId.setStatus("current")
_CucsVnicIScsiDn_Type = CucsManagedObjectDn
_CucsVnicIScsiDn_Object = MibTableColumn
cucsVnicIScsiDn = _CucsVnicIScsiDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 2),
    _CucsVnicIScsiDn_Type()
)
cucsVnicIScsiDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiDn.setStatus("current")
_CucsVnicIScsiRn_Type = SnmpAdminString
_CucsVnicIScsiRn_Object = MibTableColumn
cucsVnicIScsiRn = _CucsVnicIScsiRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 3),
    _CucsVnicIScsiRn_Type()
)
cucsVnicIScsiRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiRn.setStatus("current")
_CucsVnicIScsiAdaptorProfileName_Type = SnmpAdminString
_CucsVnicIScsiAdaptorProfileName_Object = MibTableColumn
cucsVnicIScsiAdaptorProfileName = _CucsVnicIScsiAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 4),
    _CucsVnicIScsiAdaptorProfileName_Type()
)
cucsVnicIScsiAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiAdaptorProfileName.setStatus("current")
_CucsVnicIScsiAddr_Type = MacAddress
_CucsVnicIScsiAddr_Object = MibTableColumn
cucsVnicIScsiAddr = _CucsVnicIScsiAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 5),
    _CucsVnicIScsiAddr_Type()
)
cucsVnicIScsiAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiAddr.setStatus("current")
_CucsVnicIScsiAdminVcon_Type = SnmpAdminString
_CucsVnicIScsiAdminVcon_Object = MibTableColumn
cucsVnicIScsiAdminVcon = _CucsVnicIScsiAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 6),
    _CucsVnicIScsiAdminVcon_Type()
)
cucsVnicIScsiAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiAdminVcon.setStatus("current")
_CucsVnicIScsiAuthProfileName_Type = SnmpAdminString
_CucsVnicIScsiAuthProfileName_Object = MibTableColumn
cucsVnicIScsiAuthProfileName = _CucsVnicIScsiAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 7),
    _CucsVnicIScsiAuthProfileName_Type()
)
cucsVnicIScsiAuthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiAuthProfileName.setStatus("current")
_CucsVnicIScsiBootDev_Type = CucsVnicVnicBootDev
_CucsVnicIScsiBootDev_Object = MibTableColumn
cucsVnicIScsiBootDev = _CucsVnicIScsiBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 8),
    _CucsVnicIScsiBootDev_Type()
)
cucsVnicIScsiBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootDev.setStatus("current")
_CucsVnicIScsiConfigState_Type = CucsLsConfigState
_CucsVnicIScsiConfigState_Object = MibTableColumn
cucsVnicIScsiConfigState = _CucsVnicIScsiConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 10),
    _CucsVnicIScsiConfigState_Type()
)
cucsVnicIScsiConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiConfigState.setStatus("current")
_CucsVnicIScsiEquipmentDn_Type = SnmpAdminString
_CucsVnicIScsiEquipmentDn_Object = MibTableColumn
cucsVnicIScsiEquipmentDn = _CucsVnicIScsiEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 11),
    _CucsVnicIScsiEquipmentDn_Type()
)
cucsVnicIScsiEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiEquipmentDn.setStatus("current")
_CucsVnicIScsiEthEpDn_Type = SnmpAdminString
_CucsVnicIScsiEthEpDn_Object = MibTableColumn
cucsVnicIScsiEthEpDn = _CucsVnicIScsiEthEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 12),
    _CucsVnicIScsiEthEpDn_Type()
)
cucsVnicIScsiEthEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiEthEpDn.setStatus("current")
_CucsVnicIScsiExtIPState_Type = CucsVnicExternalMgmtIPMode
_CucsVnicIScsiExtIPState_Object = MibTableColumn
cucsVnicIScsiExtIPState = _CucsVnicIScsiExtIPState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 13),
    _CucsVnicIScsiExtIPState_Type()
)
cucsVnicIScsiExtIPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiExtIPState.setStatus("current")
_CucsVnicIScsiFltAggr_Type = Unsigned64
_CucsVnicIScsiFltAggr_Object = MibTableColumn
cucsVnicIScsiFltAggr = _CucsVnicIScsiFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 14),
    _CucsVnicIScsiFltAggr_Type()
)
cucsVnicIScsiFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiFltAggr.setStatus("current")
_CucsVnicIScsiIdentPoolName_Type = SnmpAdminString
_CucsVnicIScsiIdentPoolName_Object = MibTableColumn
cucsVnicIScsiIdentPoolName = _CucsVnicIScsiIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 15),
    _CucsVnicIScsiIdentPoolName_Type()
)
cucsVnicIScsiIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiIdentPoolName.setStatus("current")
_CucsVnicIScsiInitiatorName_Type = SnmpAdminString
_CucsVnicIScsiInitiatorName_Object = MibTableColumn
cucsVnicIScsiInitiatorName = _CucsVnicIScsiInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 16),
    _CucsVnicIScsiInitiatorName_Type()
)
cucsVnicIScsiInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiInitiatorName.setStatus("current")
_CucsVnicIScsiInstType_Type = CucsVnicInstantiation
_CucsVnicIScsiInstType_Object = MibTableColumn
cucsVnicIScsiInstType = _CucsVnicIScsiInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 17),
    _CucsVnicIScsiInstType_Type()
)
cucsVnicIScsiInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiInstType.setStatus("current")
_CucsVnicIScsiIqnIdentPoolName_Type = SnmpAdminString
_CucsVnicIScsiIqnIdentPoolName_Object = MibTableColumn
cucsVnicIScsiIqnIdentPoolName = _CucsVnicIScsiIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 18),
    _CucsVnicIScsiIqnIdentPoolName_Type()
)
cucsVnicIScsiIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiIqnIdentPoolName.setStatus("current")
_CucsVnicIScsiName_Type = SnmpAdminString
_CucsVnicIScsiName_Object = MibTableColumn
cucsVnicIScsiName = _CucsVnicIScsiName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 19),
    _CucsVnicIScsiName_Type()
)
cucsVnicIScsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiName.setStatus("current")
_CucsVnicIScsiNwTemplName_Type = SnmpAdminString
_CucsVnicIScsiNwTemplName_Object = MibTableColumn
cucsVnicIScsiNwTemplName = _CucsVnicIScsiNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 20),
    _CucsVnicIScsiNwTemplName_Type()
)
cucsVnicIScsiNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiNwTemplName.setStatus("current")
_CucsVnicIScsiOperAdaptorProfileName_Type = SnmpAdminString
_CucsVnicIScsiOperAdaptorProfileName_Object = MibTableColumn
cucsVnicIScsiOperAdaptorProfileName = _CucsVnicIScsiOperAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 21),
    _CucsVnicIScsiOperAdaptorProfileName_Type()
)
cucsVnicIScsiOperAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiOperAdaptorProfileName.setStatus("current")
_CucsVnicIScsiOperAuthProfileName_Type = SnmpAdminString
_CucsVnicIScsiOperAuthProfileName_Object = MibTableColumn
cucsVnicIScsiOperAuthProfileName = _CucsVnicIScsiOperAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 22),
    _CucsVnicIScsiOperAuthProfileName_Type()
)
cucsVnicIScsiOperAuthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiOperAuthProfileName.setStatus("current")
_CucsVnicIScsiOperIqnIdentPoolName_Type = SnmpAdminString
_CucsVnicIScsiOperIqnIdentPoolName_Object = MibTableColumn
cucsVnicIScsiOperIqnIdentPoolName = _CucsVnicIScsiOperIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 24),
    _CucsVnicIScsiOperIqnIdentPoolName_Type()
)
cucsVnicIScsiOperIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiOperIqnIdentPoolName.setStatus("current")
_CucsVnicIScsiOperOrder_Type = Gauge32
_CucsVnicIScsiOperOrder_Object = MibTableColumn
cucsVnicIScsiOperOrder = _CucsVnicIScsiOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 25),
    _CucsVnicIScsiOperOrder_Type()
)
cucsVnicIScsiOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiOperOrder.setStatus("current")
_CucsVnicIScsiOperSpeed_Type = Gauge32
_CucsVnicIScsiOperSpeed_Object = MibTableColumn
cucsVnicIScsiOperSpeed = _CucsVnicIScsiOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 27),
    _CucsVnicIScsiOperSpeed_Type()
)
cucsVnicIScsiOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiOperSpeed.setStatus("current")
_CucsVnicIScsiOperStatsPolicyName_Type = SnmpAdminString
_CucsVnicIScsiOperStatsPolicyName_Object = MibTableColumn
cucsVnicIScsiOperStatsPolicyName = _CucsVnicIScsiOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 28),
    _CucsVnicIScsiOperStatsPolicyName_Type()
)
cucsVnicIScsiOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiOperStatsPolicyName.setStatus("current")
_CucsVnicIScsiOperVcon_Type = SnmpAdminString
_CucsVnicIScsiOperVcon_Object = MibTableColumn
cucsVnicIScsiOperVcon = _CucsVnicIScsiOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 29),
    _CucsVnicIScsiOperVcon_Type()
)
cucsVnicIScsiOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiOperVcon.setStatus("current")
_CucsVnicIScsiOrder_Type = Gauge32
_CucsVnicIScsiOrder_Object = MibTableColumn
cucsVnicIScsiOrder = _CucsVnicIScsiOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 30),
    _CucsVnicIScsiOrder_Type()
)
cucsVnicIScsiOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiOrder.setStatus("current")
_CucsVnicIScsiOwner_Type = CucsVnicConnectionOwner
_CucsVnicIScsiOwner_Object = MibTableColumn
cucsVnicIScsiOwner = _CucsVnicIScsiOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 31),
    _CucsVnicIScsiOwner_Type()
)
cucsVnicIScsiOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiOwner.setStatus("current")
_CucsVnicIScsiPinToGroupName_Type = SnmpAdminString
_CucsVnicIScsiPinToGroupName_Object = MibTableColumn
cucsVnicIScsiPinToGroupName = _CucsVnicIScsiPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 32),
    _CucsVnicIScsiPinToGroupName_Type()
)
cucsVnicIScsiPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiPinToGroupName.setStatus("current")
_CucsVnicIScsiQosPolicyName_Type = SnmpAdminString
_CucsVnicIScsiQosPolicyName_Object = MibTableColumn
cucsVnicIScsiQosPolicyName = _CucsVnicIScsiQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 33),
    _CucsVnicIScsiQosPolicyName_Type()
)
cucsVnicIScsiQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiQosPolicyName.setStatus("current")
_CucsVnicIScsiStatsPolicyName_Type = SnmpAdminString
_CucsVnicIScsiStatsPolicyName_Object = MibTableColumn
cucsVnicIScsiStatsPolicyName = _CucsVnicIScsiStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 34),
    _CucsVnicIScsiStatsPolicyName_Type()
)
cucsVnicIScsiStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiStatsPolicyName.setStatus("current")
_CucsVnicIScsiSwitchId_Type = CucsNetworkSwitchId
_CucsVnicIScsiSwitchId_Object = MibTableColumn
cucsVnicIScsiSwitchId = _CucsVnicIScsiSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 35),
    _CucsVnicIScsiSwitchId_Type()
)
cucsVnicIScsiSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiSwitchId.setStatus("current")
_CucsVnicIScsiType_Type = CucsVnicConnectionType
_CucsVnicIScsiType_Object = MibTableColumn
cucsVnicIScsiType = _CucsVnicIScsiType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 36),
    _CucsVnicIScsiType_Type()
)
cucsVnicIScsiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiType.setStatus("current")
_CucsVnicIScsiVnicDefType_Type = CucsVnicIScsiIfDefType
_CucsVnicIScsiVnicDefType_Object = MibTableColumn
cucsVnicIScsiVnicDefType = _CucsVnicIScsiVnicDefType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 37),
    _CucsVnicIScsiVnicDefType_Type()
)
cucsVnicIScsiVnicDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiVnicDefType.setStatus("current")
_CucsVnicIScsiVnicName_Type = SnmpAdminString
_CucsVnicIScsiVnicName_Object = MibTableColumn
cucsVnicIScsiVnicName = _CucsVnicIScsiVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 38),
    _CucsVnicIScsiVnicName_Type()
)
cucsVnicIScsiVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiVnicName.setStatus("current")
_CucsVnicIScsiConfigQualifier_Type = CucsVnicConfigIssues
_CucsVnicIScsiConfigQualifier_Object = MibTableColumn
cucsVnicIScsiConfigQualifier = _CucsVnicIScsiConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 39),
    _CucsVnicIScsiConfigQualifier_Type()
)
cucsVnicIScsiConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiConfigQualifier.setStatus("current")
_CucsVnicIScsiInitNameSuffix_Type = SnmpAdminString
_CucsVnicIScsiInitNameSuffix_Object = MibTableColumn
cucsVnicIScsiInitNameSuffix = _CucsVnicIScsiInitNameSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 40),
    _CucsVnicIScsiInitNameSuffix_Type()
)
cucsVnicIScsiInitNameSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiInitNameSuffix.setStatus("current")
_CucsVnicIScsiOperIdentPoolName_Type = SnmpAdminString
_CucsVnicIScsiOperIdentPoolName_Object = MibTableColumn
cucsVnicIScsiOperIdentPoolName = _CucsVnicIScsiOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 41),
    _CucsVnicIScsiOperIdentPoolName_Type()
)
cucsVnicIScsiOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiOperIdentPoolName.setStatus("current")
_CucsVnicIScsiAdminHostPort_Type = CucsFabricHostPortId
_CucsVnicIScsiAdminHostPort_Object = MibTableColumn
cucsVnicIScsiAdminHostPort = _CucsVnicIScsiAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 43),
    _CucsVnicIScsiAdminHostPort_Type()
)
cucsVnicIScsiAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiAdminHostPort.setStatus("current")
_CucsVnicIScsiOperHostPort_Type = CucsVnicVnicOperHostPort
_CucsVnicIScsiOperHostPort_Object = MibTableColumn
cucsVnicIScsiOperHostPort = _CucsVnicIScsiOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 44),
    _CucsVnicIScsiOperHostPort_Type()
)
cucsVnicIScsiOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiOperHostPort.setStatus("current")
_CucsVnicIScsiPropAcl_Type = Unsigned64
_CucsVnicIScsiPropAcl_Object = MibTableColumn
cucsVnicIScsiPropAcl = _CucsVnicIScsiPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 45),
    _CucsVnicIScsiPropAcl_Type()
)
cucsVnicIScsiPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiPropAcl.setStatus("current")
_CucsVnicIScsiAdminCdnName_Type = SnmpAdminString
_CucsVnicIScsiAdminCdnName_Object = MibTableColumn
cucsVnicIScsiAdminCdnName = _CucsVnicIScsiAdminCdnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 47),
    _CucsVnicIScsiAdminCdnName_Type()
)
cucsVnicIScsiAdminCdnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiAdminCdnName.setStatus("current")
_CucsVnicIScsiOperCdnName_Type = SnmpAdminString
_CucsVnicIScsiOperCdnName_Object = MibTableColumn
cucsVnicIScsiOperCdnName = _CucsVnicIScsiOperCdnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 48),
    _CucsVnicIScsiOperCdnName_Type()
)
cucsVnicIScsiOperCdnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiOperCdnName.setStatus("current")
_CucsVnicIScsiCdnSource_Type = CucsVnicCdnSource
_CucsVnicIScsiCdnSource_Object = MibTableColumn
cucsVnicIScsiCdnSource = _CucsVnicIScsiCdnSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 49),
    _CucsVnicIScsiCdnSource_Type()
)
cucsVnicIScsiCdnSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiCdnSource.setStatus("current")
_CucsVnicIScsiCdnPropInSync_Type = TruthValue
_CucsVnicIScsiCdnPropInSync_Object = MibTableColumn
cucsVnicIScsiCdnPropInSync = _CucsVnicIScsiCdnPropInSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 38, 1, 50),
    _CucsVnicIScsiCdnPropInSync_Type()
)
cucsVnicIScsiCdnPropInSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiCdnPropInSync.setStatus("current")
_CucsVnicIScsiAutoTargetIfTable_Object = MibTable
cucsVnicIScsiAutoTargetIfTable = _CucsVnicIScsiAutoTargetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 39)
)
if mibBuilder.loadTexts:
    cucsVnicIScsiAutoTargetIfTable.setStatus("current")
_CucsVnicIScsiAutoTargetIfEntry_Object = MibTableRow
cucsVnicIScsiAutoTargetIfEntry = _CucsVnicIScsiAutoTargetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 39, 1)
)
cucsVnicIScsiAutoTargetIfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIScsiAutoTargetIfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIScsiAutoTargetIfEntry.setStatus("current")
_CucsVnicIScsiAutoTargetIfInstanceId_Type = CucsManagedObjectId
_CucsVnicIScsiAutoTargetIfInstanceId_Object = MibTableColumn
cucsVnicIScsiAutoTargetIfInstanceId = _CucsVnicIScsiAutoTargetIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 39, 1, 1),
    _CucsVnicIScsiAutoTargetIfInstanceId_Type()
)
cucsVnicIScsiAutoTargetIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIScsiAutoTargetIfInstanceId.setStatus("current")
_CucsVnicIScsiAutoTargetIfDn_Type = CucsManagedObjectDn
_CucsVnicIScsiAutoTargetIfDn_Object = MibTableColumn
cucsVnicIScsiAutoTargetIfDn = _CucsVnicIScsiAutoTargetIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 39, 1, 2),
    _CucsVnicIScsiAutoTargetIfDn_Type()
)
cucsVnicIScsiAutoTargetIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiAutoTargetIfDn.setStatus("current")
_CucsVnicIScsiAutoTargetIfRn_Type = SnmpAdminString
_CucsVnicIScsiAutoTargetIfRn_Object = MibTableColumn
cucsVnicIScsiAutoTargetIfRn = _CucsVnicIScsiAutoTargetIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 39, 1, 3),
    _CucsVnicIScsiAutoTargetIfRn_Type()
)
cucsVnicIScsiAutoTargetIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiAutoTargetIfRn.setStatus("current")
_CucsVnicIScsiAutoTargetIfDhcpVendorId_Type = SnmpAdminString
_CucsVnicIScsiAutoTargetIfDhcpVendorId_Object = MibTableColumn
cucsVnicIScsiAutoTargetIfDhcpVendorId = _CucsVnicIScsiAutoTargetIfDhcpVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 39, 1, 4),
    _CucsVnicIScsiAutoTargetIfDhcpVendorId_Type()
)
cucsVnicIScsiAutoTargetIfDhcpVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiAutoTargetIfDhcpVendorId.setStatus("current")
_CucsVnicIScsiNodeTable_Object = MibTable
cucsVnicIScsiNodeTable = _CucsVnicIScsiNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 40)
)
if mibBuilder.loadTexts:
    cucsVnicIScsiNodeTable.setStatus("current")
_CucsVnicIScsiNodeEntry_Object = MibTableRow
cucsVnicIScsiNodeEntry = _CucsVnicIScsiNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 40, 1)
)
cucsVnicIScsiNodeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIScsiNodeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIScsiNodeEntry.setStatus("current")
_CucsVnicIScsiNodeInstanceId_Type = CucsManagedObjectId
_CucsVnicIScsiNodeInstanceId_Object = MibTableColumn
cucsVnicIScsiNodeInstanceId = _CucsVnicIScsiNodeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 40, 1, 1),
    _CucsVnicIScsiNodeInstanceId_Type()
)
cucsVnicIScsiNodeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIScsiNodeInstanceId.setStatus("current")
_CucsVnicIScsiNodeDn_Type = CucsManagedObjectDn
_CucsVnicIScsiNodeDn_Object = MibTableColumn
cucsVnicIScsiNodeDn = _CucsVnicIScsiNodeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 40, 1, 2),
    _CucsVnicIScsiNodeDn_Type()
)
cucsVnicIScsiNodeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiNodeDn.setStatus("current")
_CucsVnicIScsiNodeRn_Type = SnmpAdminString
_CucsVnicIScsiNodeRn_Object = MibTableColumn
cucsVnicIScsiNodeRn = _CucsVnicIScsiNodeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 40, 1, 3),
    _CucsVnicIScsiNodeRn_Type()
)
cucsVnicIScsiNodeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiNodeRn.setStatus("current")
_CucsVnicIScsiNodeFltAggr_Type = Unsigned64
_CucsVnicIScsiNodeFltAggr_Object = MibTableColumn
cucsVnicIScsiNodeFltAggr = _CucsVnicIScsiNodeFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 40, 1, 4),
    _CucsVnicIScsiNodeFltAggr_Type()
)
cucsVnicIScsiNodeFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiNodeFltAggr.setStatus("current")
_CucsVnicIScsiNodeInitiatorName_Type = SnmpAdminString
_CucsVnicIScsiNodeInitiatorName_Object = MibTableColumn
cucsVnicIScsiNodeInitiatorName = _CucsVnicIScsiNodeInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 40, 1, 5),
    _CucsVnicIScsiNodeInitiatorName_Type()
)
cucsVnicIScsiNodeInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiNodeInitiatorName.setStatus("current")
_CucsVnicIScsiNodeOwner_Type = CucsVnicIScsiNodeOwner
_CucsVnicIScsiNodeOwner_Object = MibTableColumn
cucsVnicIScsiNodeOwner = _CucsVnicIScsiNodeOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 40, 1, 6),
    _CucsVnicIScsiNodeOwner_Type()
)
cucsVnicIScsiNodeOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiNodeOwner.setStatus("current")
_CucsVnicIScsiNodeInitNameSuffix_Type = SnmpAdminString
_CucsVnicIScsiNodeInitNameSuffix_Object = MibTableColumn
cucsVnicIScsiNodeInitNameSuffix = _CucsVnicIScsiNodeInitNameSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 40, 1, 7),
    _CucsVnicIScsiNodeInitNameSuffix_Type()
)
cucsVnicIScsiNodeInitNameSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiNodeInitNameSuffix.setStatus("current")
_CucsVnicIScsiNodeIqnIdentPoolName_Type = SnmpAdminString
_CucsVnicIScsiNodeIqnIdentPoolName_Object = MibTableColumn
cucsVnicIScsiNodeIqnIdentPoolName = _CucsVnicIScsiNodeIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 40, 1, 8),
    _CucsVnicIScsiNodeIqnIdentPoolName_Type()
)
cucsVnicIScsiNodeIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiNodeIqnIdentPoolName.setStatus("current")
_CucsVnicIScsiNodeOperIqnIdentPoolName_Type = SnmpAdminString
_CucsVnicIScsiNodeOperIqnIdentPoolName_Object = MibTableColumn
cucsVnicIScsiNodeOperIqnIdentPoolName = _CucsVnicIScsiNodeOperIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 40, 1, 9),
    _CucsVnicIScsiNodeOperIqnIdentPoolName_Type()
)
cucsVnicIScsiNodeOperIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiNodeOperIqnIdentPoolName.setStatus("current")
_CucsVnicIScsiNodeInitiatorPolicyName_Type = SnmpAdminString
_CucsVnicIScsiNodeInitiatorPolicyName_Object = MibTableColumn
cucsVnicIScsiNodeInitiatorPolicyName = _CucsVnicIScsiNodeInitiatorPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 40, 1, 10),
    _CucsVnicIScsiNodeInitiatorPolicyName_Type()
)
cucsVnicIScsiNodeInitiatorPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiNodeInitiatorPolicyName.setStatus("current")
_CucsVnicIScsiNodeOperInitiatorPolicyName_Type = SnmpAdminString
_CucsVnicIScsiNodeOperInitiatorPolicyName_Object = MibTableColumn
cucsVnicIScsiNodeOperInitiatorPolicyName = _CucsVnicIScsiNodeOperInitiatorPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 40, 1, 11),
    _CucsVnicIScsiNodeOperInitiatorPolicyName_Type()
)
cucsVnicIScsiNodeOperInitiatorPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiNodeOperInitiatorPolicyName.setStatus("current")
_CucsVnicIScsiNodePropAcl_Type = Unsigned64
_CucsVnicIScsiNodePropAcl_Object = MibTableColumn
cucsVnicIScsiNodePropAcl = _CucsVnicIScsiNodePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 40, 1, 12),
    _CucsVnicIScsiNodePropAcl_Type()
)
cucsVnicIScsiNodePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiNodePropAcl.setStatus("current")
_CucsVnicIScsiStaticTargetIfTable_Object = MibTable
cucsVnicIScsiStaticTargetIfTable = _CucsVnicIScsiStaticTargetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 41)
)
if mibBuilder.loadTexts:
    cucsVnicIScsiStaticTargetIfTable.setStatus("current")
_CucsVnicIScsiStaticTargetIfEntry_Object = MibTableRow
cucsVnicIScsiStaticTargetIfEntry = _CucsVnicIScsiStaticTargetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 41, 1)
)
cucsVnicIScsiStaticTargetIfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIScsiStaticTargetIfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIScsiStaticTargetIfEntry.setStatus("current")
_CucsVnicIScsiStaticTargetIfInstanceId_Type = CucsManagedObjectId
_CucsVnicIScsiStaticTargetIfInstanceId_Object = MibTableColumn
cucsVnicIScsiStaticTargetIfInstanceId = _CucsVnicIScsiStaticTargetIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 41, 1, 1),
    _CucsVnicIScsiStaticTargetIfInstanceId_Type()
)
cucsVnicIScsiStaticTargetIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIScsiStaticTargetIfInstanceId.setStatus("current")
_CucsVnicIScsiStaticTargetIfDn_Type = CucsManagedObjectDn
_CucsVnicIScsiStaticTargetIfDn_Object = MibTableColumn
cucsVnicIScsiStaticTargetIfDn = _CucsVnicIScsiStaticTargetIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 41, 1, 2),
    _CucsVnicIScsiStaticTargetIfDn_Type()
)
cucsVnicIScsiStaticTargetIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiStaticTargetIfDn.setStatus("current")
_CucsVnicIScsiStaticTargetIfRn_Type = SnmpAdminString
_CucsVnicIScsiStaticTargetIfRn_Object = MibTableColumn
cucsVnicIScsiStaticTargetIfRn = _CucsVnicIScsiStaticTargetIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 41, 1, 3),
    _CucsVnicIScsiStaticTargetIfRn_Type()
)
cucsVnicIScsiStaticTargetIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiStaticTargetIfRn.setStatus("current")
_CucsVnicIScsiStaticTargetIfAuthProfileName_Type = SnmpAdminString
_CucsVnicIScsiStaticTargetIfAuthProfileName_Object = MibTableColumn
cucsVnicIScsiStaticTargetIfAuthProfileName = _CucsVnicIScsiStaticTargetIfAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 41, 1, 4),
    _CucsVnicIScsiStaticTargetIfAuthProfileName_Type()
)
cucsVnicIScsiStaticTargetIfAuthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiStaticTargetIfAuthProfileName.setStatus("current")
_CucsVnicIScsiStaticTargetIfIpAddress_Type = InetAddressIPv4
_CucsVnicIScsiStaticTargetIfIpAddress_Object = MibTableColumn
cucsVnicIScsiStaticTargetIfIpAddress = _CucsVnicIScsiStaticTargetIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 41, 1, 5),
    _CucsVnicIScsiStaticTargetIfIpAddress_Type()
)
cucsVnicIScsiStaticTargetIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiStaticTargetIfIpAddress.setStatus("current")
_CucsVnicIScsiStaticTargetIfName_Type = SnmpAdminString
_CucsVnicIScsiStaticTargetIfName_Object = MibTableColumn
cucsVnicIScsiStaticTargetIfName = _CucsVnicIScsiStaticTargetIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 41, 1, 6),
    _CucsVnicIScsiStaticTargetIfName_Type()
)
cucsVnicIScsiStaticTargetIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiStaticTargetIfName.setStatus("current")
_CucsVnicIScsiStaticTargetIfOperAuthProfileName_Type = SnmpAdminString
_CucsVnicIScsiStaticTargetIfOperAuthProfileName_Object = MibTableColumn
cucsVnicIScsiStaticTargetIfOperAuthProfileName = _CucsVnicIScsiStaticTargetIfOperAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 41, 1, 7),
    _CucsVnicIScsiStaticTargetIfOperAuthProfileName_Type()
)
cucsVnicIScsiStaticTargetIfOperAuthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiStaticTargetIfOperAuthProfileName.setStatus("current")
_CucsVnicIScsiStaticTargetIfPort_Type = Gauge32
_CucsVnicIScsiStaticTargetIfPort_Object = MibTableColumn
cucsVnicIScsiStaticTargetIfPort = _CucsVnicIScsiStaticTargetIfPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 41, 1, 8),
    _CucsVnicIScsiStaticTargetIfPort_Type()
)
cucsVnicIScsiStaticTargetIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiStaticTargetIfPort.setStatus("current")
_CucsVnicIScsiStaticTargetIfPriority_Type = Gauge32
_CucsVnicIScsiStaticTargetIfPriority_Object = MibTableColumn
cucsVnicIScsiStaticTargetIfPriority = _CucsVnicIScsiStaticTargetIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 41, 1, 9),
    _CucsVnicIScsiStaticTargetIfPriority_Type()
)
cucsVnicIScsiStaticTargetIfPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiStaticTargetIfPriority.setStatus("current")
_CucsVnicIScsiStaticTargetIfPropAcl_Type = Unsigned64
_CucsVnicIScsiStaticTargetIfPropAcl_Object = MibTableColumn
cucsVnicIScsiStaticTargetIfPropAcl = _CucsVnicIScsiStaticTargetIfPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 41, 1, 11),
    _CucsVnicIScsiStaticTargetIfPropAcl_Type()
)
cucsVnicIScsiStaticTargetIfPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiStaticTargetIfPropAcl.setStatus("current")
_CucsVnicInternalProfileTable_Object = MibTable
cucsVnicInternalProfileTable = _CucsVnicInternalProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 42)
)
if mibBuilder.loadTexts:
    cucsVnicInternalProfileTable.setStatus("current")
_CucsVnicInternalProfileEntry_Object = MibTableRow
cucsVnicInternalProfileEntry = _CucsVnicInternalProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 42, 1)
)
cucsVnicInternalProfileEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicInternalProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicInternalProfileEntry.setStatus("current")
_CucsVnicInternalProfileInstanceId_Type = CucsManagedObjectId
_CucsVnicInternalProfileInstanceId_Object = MibTableColumn
cucsVnicInternalProfileInstanceId = _CucsVnicInternalProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 42, 1, 1),
    _CucsVnicInternalProfileInstanceId_Type()
)
cucsVnicInternalProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicInternalProfileInstanceId.setStatus("current")
_CucsVnicInternalProfileDn_Type = CucsManagedObjectDn
_CucsVnicInternalProfileDn_Object = MibTableColumn
cucsVnicInternalProfileDn = _CucsVnicInternalProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 42, 1, 2),
    _CucsVnicInternalProfileDn_Type()
)
cucsVnicInternalProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicInternalProfileDn.setStatus("current")
_CucsVnicInternalProfileRn_Type = SnmpAdminString
_CucsVnicInternalProfileRn_Object = MibTableColumn
cucsVnicInternalProfileRn = _CucsVnicInternalProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 42, 1, 3),
    _CucsVnicInternalProfileRn_Type()
)
cucsVnicInternalProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicInternalProfileRn.setStatus("current")
_CucsVnicInternalProfileDescr_Type = SnmpAdminString
_CucsVnicInternalProfileDescr_Object = MibTableColumn
cucsVnicInternalProfileDescr = _CucsVnicInternalProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 42, 1, 4),
    _CucsVnicInternalProfileDescr_Type()
)
cucsVnicInternalProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicInternalProfileDescr.setStatus("current")
_CucsVnicInternalProfileIntId_Type = SnmpAdminString
_CucsVnicInternalProfileIntId_Object = MibTableColumn
cucsVnicInternalProfileIntId = _CucsVnicInternalProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 42, 1, 5),
    _CucsVnicInternalProfileIntId_Type()
)
cucsVnicInternalProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicInternalProfileIntId.setStatus("current")
_CucsVnicInternalProfileMaxPorts_Type = Gauge32
_CucsVnicInternalProfileMaxPorts_Object = MibTableColumn
cucsVnicInternalProfileMaxPorts = _CucsVnicInternalProfileMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 42, 1, 6),
    _CucsVnicInternalProfileMaxPorts_Type()
)
cucsVnicInternalProfileMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicInternalProfileMaxPorts.setStatus("current")
_CucsVnicInternalProfileName_Type = SnmpAdminString
_CucsVnicInternalProfileName_Object = MibTableColumn
cucsVnicInternalProfileName = _CucsVnicInternalProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 42, 1, 7),
    _CucsVnicInternalProfileName_Type()
)
cucsVnicInternalProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicInternalProfileName.setStatus("current")
_CucsVnicInternalProfilePolicyLevel_Type = Gauge32
_CucsVnicInternalProfilePolicyLevel_Object = MibTableColumn
cucsVnicInternalProfilePolicyLevel = _CucsVnicInternalProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 42, 1, 8),
    _CucsVnicInternalProfilePolicyLevel_Type()
)
cucsVnicInternalProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicInternalProfilePolicyLevel.setStatus("current")
_CucsVnicInternalProfilePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicInternalProfilePolicyOwner_Object = MibTableColumn
cucsVnicInternalProfilePolicyOwner = _CucsVnicInternalProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 42, 1, 9),
    _CucsVnicInternalProfilePolicyOwner_Type()
)
cucsVnicInternalProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicInternalProfilePolicyOwner.setStatus("current")
_CucsVnicLunTable_Object = MibTable
cucsVnicLunTable = _CucsVnicLunTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 43)
)
if mibBuilder.loadTexts:
    cucsVnicLunTable.setStatus("current")
_CucsVnicLunEntry_Object = MibTableRow
cucsVnicLunEntry = _CucsVnicLunEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 43, 1)
)
cucsVnicLunEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicLunInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicLunEntry.setStatus("current")
_CucsVnicLunInstanceId_Type = CucsManagedObjectId
_CucsVnicLunInstanceId_Object = MibTableColumn
cucsVnicLunInstanceId = _CucsVnicLunInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 43, 1, 1),
    _CucsVnicLunInstanceId_Type()
)
cucsVnicLunInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicLunInstanceId.setStatus("current")
_CucsVnicLunDn_Type = CucsManagedObjectDn
_CucsVnicLunDn_Object = MibTableColumn
cucsVnicLunDn = _CucsVnicLunDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 43, 1, 2),
    _CucsVnicLunDn_Type()
)
cucsVnicLunDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLunDn.setStatus("current")
_CucsVnicLunRn_Type = SnmpAdminString
_CucsVnicLunRn_Object = MibTableColumn
cucsVnicLunRn = _CucsVnicLunRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 43, 1, 3),
    _CucsVnicLunRn_Type()
)
cucsVnicLunRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLunRn.setStatus("current")
_CucsVnicLunBootable_Type = TruthValue
_CucsVnicLunBootable_Object = MibTableColumn
cucsVnicLunBootable = _CucsVnicLunBootable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 43, 1, 4),
    _CucsVnicLunBootable_Type()
)
cucsVnicLunBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLunBootable.setStatus("current")
_CucsVnicLunId_Type = CucsVnicLunId
_CucsVnicLunId_Object = MibTableColumn
cucsVnicLunId = _CucsVnicLunId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 43, 1, 5),
    _CucsVnicLunId_Type()
)
cucsVnicLunId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLunId.setStatus("current")
_CucsVnicOProfileAliasTable_Object = MibTable
cucsVnicOProfileAliasTable = _CucsVnicOProfileAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 44)
)
if mibBuilder.loadTexts:
    cucsVnicOProfileAliasTable.setStatus("current")
_CucsVnicOProfileAliasEntry_Object = MibTableRow
cucsVnicOProfileAliasEntry = _CucsVnicOProfileAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 44, 1)
)
cucsVnicOProfileAliasEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicOProfileAliasInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicOProfileAliasEntry.setStatus("current")
_CucsVnicOProfileAliasInstanceId_Type = CucsManagedObjectId
_CucsVnicOProfileAliasInstanceId_Object = MibTableColumn
cucsVnicOProfileAliasInstanceId = _CucsVnicOProfileAliasInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 44, 1, 1),
    _CucsVnicOProfileAliasInstanceId_Type()
)
cucsVnicOProfileAliasInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicOProfileAliasInstanceId.setStatus("current")
_CucsVnicOProfileAliasDn_Type = CucsManagedObjectDn
_CucsVnicOProfileAliasDn_Object = MibTableColumn
cucsVnicOProfileAliasDn = _CucsVnicOProfileAliasDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 44, 1, 2),
    _CucsVnicOProfileAliasDn_Type()
)
cucsVnicOProfileAliasDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicOProfileAliasDn.setStatus("current")
_CucsVnicOProfileAliasRn_Type = SnmpAdminString
_CucsVnicOProfileAliasRn_Object = MibTableColumn
cucsVnicOProfileAliasRn = _CucsVnicOProfileAliasRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 44, 1, 3),
    _CucsVnicOProfileAliasRn_Type()
)
cucsVnicOProfileAliasRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicOProfileAliasRn.setStatus("current")
_CucsVnicOProfileAliasAlias_Type = SnmpAdminString
_CucsVnicOProfileAliasAlias_Object = MibTableColumn
cucsVnicOProfileAliasAlias = _CucsVnicOProfileAliasAlias_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 44, 1, 4),
    _CucsVnicOProfileAliasAlias_Type()
)
cucsVnicOProfileAliasAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicOProfileAliasAlias.setStatus("current")
_CucsVnicOProfileAliasMgmtPlane_Type = CucsVmMgmtPlane
_CucsVnicOProfileAliasMgmtPlane_Object = MibTableColumn
cucsVnicOProfileAliasMgmtPlane = _CucsVnicOProfileAliasMgmtPlane_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 44, 1, 5),
    _CucsVnicOProfileAliasMgmtPlane_Type()
)
cucsVnicOProfileAliasMgmtPlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicOProfileAliasMgmtPlane.setStatus("current")
_CucsVnicOProfileAliasVSwitchId_Type = SnmpAdminString
_CucsVnicOProfileAliasVSwitchId_Object = MibTableColumn
cucsVnicOProfileAliasVSwitchId = _CucsVnicOProfileAliasVSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 44, 1, 6),
    _CucsVnicOProfileAliasVSwitchId_Type()
)
cucsVnicOProfileAliasVSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicOProfileAliasVSwitchId.setStatus("current")
_CucsVnicOProfileAliasVSwitchName_Type = SnmpAdminString
_CucsVnicOProfileAliasVSwitchName_Object = MibTableColumn
cucsVnicOProfileAliasVSwitchName = _CucsVnicOProfileAliasVSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 44, 1, 7),
    _CucsVnicOProfileAliasVSwitchName_Type()
)
cucsVnicOProfileAliasVSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicOProfileAliasVSwitchName.setStatus("current")
_CucsVnicVlanTable_Object = MibTable
cucsVnicVlanTable = _CucsVnicVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45)
)
if mibBuilder.loadTexts:
    cucsVnicVlanTable.setStatus("current")
_CucsVnicVlanEntry_Object = MibTableRow
cucsVnicVlanEntry = _CucsVnicVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1)
)
cucsVnicVlanEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicVlanEntry.setStatus("current")
_CucsVnicVlanInstanceId_Type = CucsManagedObjectId
_CucsVnicVlanInstanceId_Object = MibTableColumn
cucsVnicVlanInstanceId = _CucsVnicVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 1),
    _CucsVnicVlanInstanceId_Type()
)
cucsVnicVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicVlanInstanceId.setStatus("current")
_CucsVnicVlanDn_Type = CucsManagedObjectDn
_CucsVnicVlanDn_Object = MibTableColumn
cucsVnicVlanDn = _CucsVnicVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 2),
    _CucsVnicVlanDn_Type()
)
cucsVnicVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVlanDn.setStatus("current")
_CucsVnicVlanRn_Type = SnmpAdminString
_CucsVnicVlanRn_Object = MibTableColumn
cucsVnicVlanRn = _CucsVnicVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 3),
    _CucsVnicVlanRn_Type()
)
cucsVnicVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVlanRn.setStatus("current")
_CucsVnicVlanFltAggr_Type = Unsigned64
_CucsVnicVlanFltAggr_Object = MibTableColumn
cucsVnicVlanFltAggr = _CucsVnicVlanFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 4),
    _CucsVnicVlanFltAggr_Type()
)
cucsVnicVlanFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVlanFltAggr.setStatus("current")
_CucsVnicVlanName_Type = SnmpAdminString
_CucsVnicVlanName_Object = MibTableColumn
cucsVnicVlanName = _CucsVnicVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 5),
    _CucsVnicVlanName_Type()
)
cucsVnicVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVlanName.setStatus("current")
_CucsVnicVlanOperState_Type = CucsVnicIfOperState
_CucsVnicVlanOperState_Object = MibTableColumn
cucsVnicVlanOperState = _CucsVnicVlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 6),
    _CucsVnicVlanOperState_Type()
)
cucsVnicVlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVlanOperState.setStatus("current")
_CucsVnicVlanOwner_Type = CucsVnicConnectionOwner
_CucsVnicVlanOwner_Object = MibTableColumn
cucsVnicVlanOwner = _CucsVnicVlanOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 7),
    _CucsVnicVlanOwner_Type()
)
cucsVnicVlanOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVlanOwner.setStatus("current")
_CucsVnicVlanSwitchId_Type = CucsNetworkSwitchId
_CucsVnicVlanSwitchId_Object = MibTableColumn
cucsVnicVlanSwitchId = _CucsVnicVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 8),
    _CucsVnicVlanSwitchId_Type()
)
cucsVnicVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVlanSwitchId.setStatus("current")
_CucsVnicVlanType_Type = CucsVnicConnectionType
_CucsVnicVlanType_Object = MibTableColumn
cucsVnicVlanType = _CucsVnicVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 9),
    _CucsVnicVlanType_Type()
)
cucsVnicVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVlanType.setStatus("current")
_CucsVnicVlanVlanName_Type = SnmpAdminString
_CucsVnicVlanVlanName_Object = MibTableColumn
cucsVnicVlanVlanName = _CucsVnicVlanVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 10),
    _CucsVnicVlanVlanName_Type()
)
cucsVnicVlanVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVlanVlanName.setStatus("current")
_CucsVnicVlanVnet_Type = Gauge32
_CucsVnicVlanVnet_Object = MibTableColumn
cucsVnicVlanVnet = _CucsVnicVlanVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 11),
    _CucsVnicVlanVnet_Type()
)
cucsVnicVlanVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVlanVnet.setStatus("current")
_CucsVnicVlanConfigQualifier_Type = CucsVnicConfigIssues
_CucsVnicVlanConfigQualifier_Object = MibTableColumn
cucsVnicVlanConfigQualifier = _CucsVnicVlanConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 12),
    _CucsVnicVlanConfigQualifier_Type()
)
cucsVnicVlanConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVlanConfigQualifier.setStatus("current")
_CucsVnicVlanOperVnetDn_Type = SnmpAdminString
_CucsVnicVlanOperVnetDn_Object = MibTableColumn
cucsVnicVlanOperVnetDn = _CucsVnicVlanOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 14),
    _CucsVnicVlanOperVnetDn_Type()
)
cucsVnicVlanOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVlanOperVnetDn.setStatus("current")
_CucsVnicVlanOperVnetName_Type = SnmpAdminString
_CucsVnicVlanOperVnetName_Object = MibTableColumn
cucsVnicVlanOperVnetName = _CucsVnicVlanOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 15),
    _CucsVnicVlanOperVnetName_Type()
)
cucsVnicVlanOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVlanOperVnetName.setStatus("current")
_CucsVnicVlanPubNwId_Type = Gauge32
_CucsVnicVlanPubNwId_Object = MibTableColumn
cucsVnicVlanPubNwId = _CucsVnicVlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 16),
    _CucsVnicVlanPubNwId_Type()
)
cucsVnicVlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVlanPubNwId.setStatus("current")
_CucsVnicVlanSharing_Type = CucsFabricVlanSharingType
_CucsVnicVlanSharing_Object = MibTableColumn
cucsVnicVlanSharing = _CucsVnicVlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 17),
    _CucsVnicVlanSharing_Type()
)
cucsVnicVlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVlanSharing.setStatus("current")
_CucsVnicVlanOperPrimaryVnetDn_Type = SnmpAdminString
_CucsVnicVlanOperPrimaryVnetDn_Object = MibTableColumn
cucsVnicVlanOperPrimaryVnetDn = _CucsVnicVlanOperPrimaryVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 18),
    _CucsVnicVlanOperPrimaryVnetDn_Type()
)
cucsVnicVlanOperPrimaryVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVlanOperPrimaryVnetDn.setStatus("current")
_CucsVnicVlanOperPrimaryVnetName_Type = SnmpAdminString
_CucsVnicVlanOperPrimaryVnetName_Object = MibTableColumn
cucsVnicVlanOperPrimaryVnetName = _CucsVnicVlanOperPrimaryVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 45, 1, 19),
    _CucsVnicVlanOperPrimaryVnetName_Type()
)
cucsVnicVlanOperPrimaryVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVlanOperPrimaryVnetName.setStatus("current")
_CucsVnicConnDefTable_Object = MibTable
cucsVnicConnDefTable = _CucsVnicConnDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 46)
)
if mibBuilder.loadTexts:
    cucsVnicConnDefTable.setStatus("current")
_CucsVnicConnDefEntry_Object = MibTableRow
cucsVnicConnDefEntry = _CucsVnicConnDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 46, 1)
)
cucsVnicConnDefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicConnDefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicConnDefEntry.setStatus("current")
_CucsVnicConnDefInstanceId_Type = CucsManagedObjectId
_CucsVnicConnDefInstanceId_Object = MibTableColumn
cucsVnicConnDefInstanceId = _CucsVnicConnDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 46, 1, 1),
    _CucsVnicConnDefInstanceId_Type()
)
cucsVnicConnDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicConnDefInstanceId.setStatus("current")
_CucsVnicConnDefDn_Type = CucsManagedObjectDn
_CucsVnicConnDefDn_Object = MibTableColumn
cucsVnicConnDefDn = _CucsVnicConnDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 46, 1, 2),
    _CucsVnicConnDefDn_Type()
)
cucsVnicConnDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicConnDefDn.setStatus("current")
_CucsVnicConnDefRn_Type = SnmpAdminString
_CucsVnicConnDefRn_Object = MibTableColumn
cucsVnicConnDefRn = _CucsVnicConnDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 46, 1, 3),
    _CucsVnicConnDefRn_Type()
)
cucsVnicConnDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicConnDefRn.setStatus("current")
_CucsVnicConnDefFltAggr_Type = Unsigned64
_CucsVnicConnDefFltAggr_Object = MibTableColumn
cucsVnicConnDefFltAggr = _CucsVnicConnDefFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 46, 1, 4),
    _CucsVnicConnDefFltAggr_Type()
)
cucsVnicConnDefFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicConnDefFltAggr.setStatus("current")
_CucsVnicConnDefLanConnPolicyName_Type = SnmpAdminString
_CucsVnicConnDefLanConnPolicyName_Object = MibTableColumn
cucsVnicConnDefLanConnPolicyName = _CucsVnicConnDefLanConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 46, 1, 5),
    _CucsVnicConnDefLanConnPolicyName_Type()
)
cucsVnicConnDefLanConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicConnDefLanConnPolicyName.setStatus("current")
_CucsVnicConnDefOperLanConnPolicyName_Type = SnmpAdminString
_CucsVnicConnDefOperLanConnPolicyName_Object = MibTableColumn
cucsVnicConnDefOperLanConnPolicyName = _CucsVnicConnDefOperLanConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 46, 1, 6),
    _CucsVnicConnDefOperLanConnPolicyName_Type()
)
cucsVnicConnDefOperLanConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicConnDefOperLanConnPolicyName.setStatus("current")
_CucsVnicConnDefOperSanConnPolicyName_Type = SnmpAdminString
_CucsVnicConnDefOperSanConnPolicyName_Object = MibTableColumn
cucsVnicConnDefOperSanConnPolicyName = _CucsVnicConnDefOperSanConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 46, 1, 7),
    _CucsVnicConnDefOperSanConnPolicyName_Type()
)
cucsVnicConnDefOperSanConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicConnDefOperSanConnPolicyName.setStatus("current")
_CucsVnicConnDefSanConnPolicyName_Type = SnmpAdminString
_CucsVnicConnDefSanConnPolicyName_Object = MibTableColumn
cucsVnicConnDefSanConnPolicyName = _CucsVnicConnDefSanConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 46, 1, 8),
    _CucsVnicConnDefSanConnPolicyName_Type()
)
cucsVnicConnDefSanConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicConnDefSanConnPolicyName.setStatus("current")
_CucsVnicConnDefPropAcl_Type = Unsigned64
_CucsVnicConnDefPropAcl_Object = MibTableColumn
cucsVnicConnDefPropAcl = _CucsVnicConnDefPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 46, 1, 9),
    _CucsVnicConnDefPropAcl_Type()
)
cucsVnicConnDefPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicConnDefPropAcl.setStatus("current")
_CucsVnicDynamicConPolicyRefTable_Object = MibTable
cucsVnicDynamicConPolicyRefTable = _CucsVnicDynamicConPolicyRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 47)
)
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyRefTable.setStatus("current")
_CucsVnicDynamicConPolicyRefEntry_Object = MibTableRow
cucsVnicDynamicConPolicyRefEntry = _CucsVnicDynamicConPolicyRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 47, 1)
)
cucsVnicDynamicConPolicyRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicDynamicConPolicyRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyRefEntry.setStatus("current")
_CucsVnicDynamicConPolicyRefInstanceId_Type = CucsManagedObjectId
_CucsVnicDynamicConPolicyRefInstanceId_Object = MibTableColumn
cucsVnicDynamicConPolicyRefInstanceId = _CucsVnicDynamicConPolicyRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 47, 1, 1),
    _CucsVnicDynamicConPolicyRefInstanceId_Type()
)
cucsVnicDynamicConPolicyRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyRefInstanceId.setStatus("current")
_CucsVnicDynamicConPolicyRefDn_Type = CucsManagedObjectDn
_CucsVnicDynamicConPolicyRefDn_Object = MibTableColumn
cucsVnicDynamicConPolicyRefDn = _CucsVnicDynamicConPolicyRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 47, 1, 2),
    _CucsVnicDynamicConPolicyRefDn_Type()
)
cucsVnicDynamicConPolicyRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyRefDn.setStatus("current")
_CucsVnicDynamicConPolicyRefRn_Type = SnmpAdminString
_CucsVnicDynamicConPolicyRefRn_Object = MibTableColumn
cucsVnicDynamicConPolicyRefRn = _CucsVnicDynamicConPolicyRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 47, 1, 3),
    _CucsVnicDynamicConPolicyRefRn_Type()
)
cucsVnicDynamicConPolicyRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyRefRn.setStatus("current")
_CucsVnicDynamicConPolicyRefConPolicyName_Type = SnmpAdminString
_CucsVnicDynamicConPolicyRefConPolicyName_Object = MibTableColumn
cucsVnicDynamicConPolicyRefConPolicyName = _CucsVnicDynamicConPolicyRefConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 47, 1, 4),
    _CucsVnicDynamicConPolicyRefConPolicyName_Type()
)
cucsVnicDynamicConPolicyRefConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyRefConPolicyName.setStatus("current")
_CucsVnicDynamicConPolicyRefOperConPolicyName_Type = SnmpAdminString
_CucsVnicDynamicConPolicyRefOperConPolicyName_Object = MibTableColumn
cucsVnicDynamicConPolicyRefOperConPolicyName = _CucsVnicDynamicConPolicyRefOperConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 47, 1, 5),
    _CucsVnicDynamicConPolicyRefOperConPolicyName_Type()
)
cucsVnicDynamicConPolicyRefOperConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicDynamicConPolicyRefOperConPolicyName.setStatus("current")
_CucsVnicFcGroupDefTable_Object = MibTable
cucsVnicFcGroupDefTable = _CucsVnicFcGroupDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48)
)
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefTable.setStatus("current")
_CucsVnicFcGroupDefEntry_Object = MibTableRow
cucsVnicFcGroupDefEntry = _CucsVnicFcGroupDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1)
)
cucsVnicFcGroupDefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicFcGroupDefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefEntry.setStatus("current")
_CucsVnicFcGroupDefInstanceId_Type = CucsManagedObjectId
_CucsVnicFcGroupDefInstanceId_Object = MibTableColumn
cucsVnicFcGroupDefInstanceId = _CucsVnicFcGroupDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1, 1),
    _CucsVnicFcGroupDefInstanceId_Type()
)
cucsVnicFcGroupDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefInstanceId.setStatus("current")
_CucsVnicFcGroupDefDn_Type = CucsManagedObjectDn
_CucsVnicFcGroupDefDn_Object = MibTableColumn
cucsVnicFcGroupDefDn = _CucsVnicFcGroupDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1, 2),
    _CucsVnicFcGroupDefDn_Type()
)
cucsVnicFcGroupDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefDn.setStatus("current")
_CucsVnicFcGroupDefRn_Type = SnmpAdminString
_CucsVnicFcGroupDefRn_Object = MibTableColumn
cucsVnicFcGroupDefRn = _CucsVnicFcGroupDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1, 3),
    _CucsVnicFcGroupDefRn_Type()
)
cucsVnicFcGroupDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefRn.setStatus("current")
_CucsVnicFcGroupDefAdaptorProfileName_Type = SnmpAdminString
_CucsVnicFcGroupDefAdaptorProfileName_Object = MibTableColumn
cucsVnicFcGroupDefAdaptorProfileName = _CucsVnicFcGroupDefAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1, 4),
    _CucsVnicFcGroupDefAdaptorProfileName_Type()
)
cucsVnicFcGroupDefAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefAdaptorProfileName.setStatus("current")
_CucsVnicFcGroupDefDescr_Type = SnmpAdminString
_CucsVnicFcGroupDefDescr_Object = MibTableColumn
cucsVnicFcGroupDefDescr = _CucsVnicFcGroupDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1, 5),
    _CucsVnicFcGroupDefDescr_Type()
)
cucsVnicFcGroupDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefDescr.setStatus("current")
_CucsVnicFcGroupDefIdentPoolName_Type = SnmpAdminString
_CucsVnicFcGroupDefIdentPoolName_Object = MibTableColumn
cucsVnicFcGroupDefIdentPoolName = _CucsVnicFcGroupDefIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1, 6),
    _CucsVnicFcGroupDefIdentPoolName_Type()
)
cucsVnicFcGroupDefIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefIdentPoolName.setStatus("current")
_CucsVnicFcGroupDefIntId_Type = SnmpAdminString
_CucsVnicFcGroupDefIntId_Object = MibTableColumn
cucsVnicFcGroupDefIntId = _CucsVnicFcGroupDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1, 7),
    _CucsVnicFcGroupDefIntId_Type()
)
cucsVnicFcGroupDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefIntId.setStatus("current")
_CucsVnicFcGroupDefMaxDataFieldSize_Type = Gauge32
_CucsVnicFcGroupDefMaxDataFieldSize_Object = MibTableColumn
cucsVnicFcGroupDefMaxDataFieldSize = _CucsVnicFcGroupDefMaxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1, 8),
    _CucsVnicFcGroupDefMaxDataFieldSize_Type()
)
cucsVnicFcGroupDefMaxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefMaxDataFieldSize.setStatus("current")
_CucsVnicFcGroupDefName_Type = SnmpAdminString
_CucsVnicFcGroupDefName_Object = MibTableColumn
cucsVnicFcGroupDefName = _CucsVnicFcGroupDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1, 9),
    _CucsVnicFcGroupDefName_Type()
)
cucsVnicFcGroupDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefName.setStatus("current")
_CucsVnicFcGroupDefNwTemplName_Type = SnmpAdminString
_CucsVnicFcGroupDefNwTemplName_Object = MibTableColumn
cucsVnicFcGroupDefNwTemplName = _CucsVnicFcGroupDefNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1, 10),
    _CucsVnicFcGroupDefNwTemplName_Type()
)
cucsVnicFcGroupDefNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefNwTemplName.setStatus("current")
_CucsVnicFcGroupDefOperStatsPolicyName_Type = SnmpAdminString
_CucsVnicFcGroupDefOperStatsPolicyName_Object = MibTableColumn
cucsVnicFcGroupDefOperStatsPolicyName = _CucsVnicFcGroupDefOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1, 11),
    _CucsVnicFcGroupDefOperStatsPolicyName_Type()
)
cucsVnicFcGroupDefOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefOperStatsPolicyName.setStatus("current")
_CucsVnicFcGroupDefOperStorageConnPolicyName_Type = SnmpAdminString
_CucsVnicFcGroupDefOperStorageConnPolicyName_Object = MibTableColumn
cucsVnicFcGroupDefOperStorageConnPolicyName = _CucsVnicFcGroupDefOperStorageConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1, 12),
    _CucsVnicFcGroupDefOperStorageConnPolicyName_Type()
)
cucsVnicFcGroupDefOperStorageConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefOperStorageConnPolicyName.setStatus("current")
_CucsVnicFcGroupDefPolicyLevel_Type = Gauge32
_CucsVnicFcGroupDefPolicyLevel_Object = MibTableColumn
cucsVnicFcGroupDefPolicyLevel = _CucsVnicFcGroupDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1, 13),
    _CucsVnicFcGroupDefPolicyLevel_Type()
)
cucsVnicFcGroupDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefPolicyLevel.setStatus("current")
_CucsVnicFcGroupDefPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicFcGroupDefPolicyOwner_Object = MibTableColumn
cucsVnicFcGroupDefPolicyOwner = _CucsVnicFcGroupDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1, 14),
    _CucsVnicFcGroupDefPolicyOwner_Type()
)
cucsVnicFcGroupDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefPolicyOwner.setStatus("current")
_CucsVnicFcGroupDefQosPolicyName_Type = SnmpAdminString
_CucsVnicFcGroupDefQosPolicyName_Object = MibTableColumn
cucsVnicFcGroupDefQosPolicyName = _CucsVnicFcGroupDefQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1, 15),
    _CucsVnicFcGroupDefQosPolicyName_Type()
)
cucsVnicFcGroupDefQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefQosPolicyName.setStatus("current")
_CucsVnicFcGroupDefStatsPolicyName_Type = SnmpAdminString
_CucsVnicFcGroupDefStatsPolicyName_Object = MibTableColumn
cucsVnicFcGroupDefStatsPolicyName = _CucsVnicFcGroupDefStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1, 16),
    _CucsVnicFcGroupDefStatsPolicyName_Type()
)
cucsVnicFcGroupDefStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefStatsPolicyName.setStatus("current")
_CucsVnicFcGroupDefStorageConnPolicyName_Type = SnmpAdminString
_CucsVnicFcGroupDefStorageConnPolicyName_Object = MibTableColumn
cucsVnicFcGroupDefStorageConnPolicyName = _CucsVnicFcGroupDefStorageConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 48, 1, 17),
    _CucsVnicFcGroupDefStorageConnPolicyName_Type()
)
cucsVnicFcGroupDefStorageConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupDefStorageConnPolicyName.setStatus("current")
_CucsVnicFcGroupTemplTable_Object = MibTable
cucsVnicFcGroupTemplTable = _CucsVnicFcGroupTemplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49)
)
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplTable.setStatus("current")
_CucsVnicFcGroupTemplEntry_Object = MibTableRow
cucsVnicFcGroupTemplEntry = _CucsVnicFcGroupTemplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1)
)
cucsVnicFcGroupTemplEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicFcGroupTemplInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplEntry.setStatus("current")
_CucsVnicFcGroupTemplInstanceId_Type = CucsManagedObjectId
_CucsVnicFcGroupTemplInstanceId_Object = MibTableColumn
cucsVnicFcGroupTemplInstanceId = _CucsVnicFcGroupTemplInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 1),
    _CucsVnicFcGroupTemplInstanceId_Type()
)
cucsVnicFcGroupTemplInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplInstanceId.setStatus("current")
_CucsVnicFcGroupTemplDn_Type = CucsManagedObjectDn
_CucsVnicFcGroupTemplDn_Object = MibTableColumn
cucsVnicFcGroupTemplDn = _CucsVnicFcGroupTemplDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 2),
    _CucsVnicFcGroupTemplDn_Type()
)
cucsVnicFcGroupTemplDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplDn.setStatus("current")
_CucsVnicFcGroupTemplRn_Type = SnmpAdminString
_CucsVnicFcGroupTemplRn_Object = MibTableColumn
cucsVnicFcGroupTemplRn = _CucsVnicFcGroupTemplRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 3),
    _CucsVnicFcGroupTemplRn_Type()
)
cucsVnicFcGroupTemplRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplRn.setStatus("current")
_CucsVnicFcGroupTemplAdaptorProfileName_Type = SnmpAdminString
_CucsVnicFcGroupTemplAdaptorProfileName_Object = MibTableColumn
cucsVnicFcGroupTemplAdaptorProfileName = _CucsVnicFcGroupTemplAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 4),
    _CucsVnicFcGroupTemplAdaptorProfileName_Type()
)
cucsVnicFcGroupTemplAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplAdaptorProfileName.setStatus("current")
_CucsVnicFcGroupTemplDescr_Type = SnmpAdminString
_CucsVnicFcGroupTemplDescr_Object = MibTableColumn
cucsVnicFcGroupTemplDescr = _CucsVnicFcGroupTemplDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 5),
    _CucsVnicFcGroupTemplDescr_Type()
)
cucsVnicFcGroupTemplDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplDescr.setStatus("current")
_CucsVnicFcGroupTemplIdentPoolName_Type = SnmpAdminString
_CucsVnicFcGroupTemplIdentPoolName_Object = MibTableColumn
cucsVnicFcGroupTemplIdentPoolName = _CucsVnicFcGroupTemplIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 6),
    _CucsVnicFcGroupTemplIdentPoolName_Type()
)
cucsVnicFcGroupTemplIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplIdentPoolName.setStatus("current")
_CucsVnicFcGroupTemplIntId_Type = SnmpAdminString
_CucsVnicFcGroupTemplIntId_Object = MibTableColumn
cucsVnicFcGroupTemplIntId = _CucsVnicFcGroupTemplIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 7),
    _CucsVnicFcGroupTemplIntId_Type()
)
cucsVnicFcGroupTemplIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplIntId.setStatus("current")
_CucsVnicFcGroupTemplMaxDataFieldSize_Type = Gauge32
_CucsVnicFcGroupTemplMaxDataFieldSize_Object = MibTableColumn
cucsVnicFcGroupTemplMaxDataFieldSize = _CucsVnicFcGroupTemplMaxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 8),
    _CucsVnicFcGroupTemplMaxDataFieldSize_Type()
)
cucsVnicFcGroupTemplMaxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplMaxDataFieldSize.setStatus("current")
_CucsVnicFcGroupTemplName_Type = SnmpAdminString
_CucsVnicFcGroupTemplName_Object = MibTableColumn
cucsVnicFcGroupTemplName = _CucsVnicFcGroupTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 9),
    _CucsVnicFcGroupTemplName_Type()
)
cucsVnicFcGroupTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplName.setStatus("current")
_CucsVnicFcGroupTemplNwTemplName_Type = SnmpAdminString
_CucsVnicFcGroupTemplNwTemplName_Object = MibTableColumn
cucsVnicFcGroupTemplNwTemplName = _CucsVnicFcGroupTemplNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 10),
    _CucsVnicFcGroupTemplNwTemplName_Type()
)
cucsVnicFcGroupTemplNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplNwTemplName.setStatus("current")
_CucsVnicFcGroupTemplOperStatsPolicyName_Type = SnmpAdminString
_CucsVnicFcGroupTemplOperStatsPolicyName_Object = MibTableColumn
cucsVnicFcGroupTemplOperStatsPolicyName = _CucsVnicFcGroupTemplOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 11),
    _CucsVnicFcGroupTemplOperStatsPolicyName_Type()
)
cucsVnicFcGroupTemplOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplOperStatsPolicyName.setStatus("current")
_CucsVnicFcGroupTemplOperStorageConnPolicyName_Type = SnmpAdminString
_CucsVnicFcGroupTemplOperStorageConnPolicyName_Object = MibTableColumn
cucsVnicFcGroupTemplOperStorageConnPolicyName = _CucsVnicFcGroupTemplOperStorageConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 12),
    _CucsVnicFcGroupTemplOperStorageConnPolicyName_Type()
)
cucsVnicFcGroupTemplOperStorageConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplOperStorageConnPolicyName.setStatus("current")
_CucsVnicFcGroupTemplPolicyLevel_Type = Gauge32
_CucsVnicFcGroupTemplPolicyLevel_Object = MibTableColumn
cucsVnicFcGroupTemplPolicyLevel = _CucsVnicFcGroupTemplPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 13),
    _CucsVnicFcGroupTemplPolicyLevel_Type()
)
cucsVnicFcGroupTemplPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplPolicyLevel.setStatus("current")
_CucsVnicFcGroupTemplPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicFcGroupTemplPolicyOwner_Object = MibTableColumn
cucsVnicFcGroupTemplPolicyOwner = _CucsVnicFcGroupTemplPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 14),
    _CucsVnicFcGroupTemplPolicyOwner_Type()
)
cucsVnicFcGroupTemplPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplPolicyOwner.setStatus("current")
_CucsVnicFcGroupTemplQosPolicyName_Type = SnmpAdminString
_CucsVnicFcGroupTemplQosPolicyName_Object = MibTableColumn
cucsVnicFcGroupTemplQosPolicyName = _CucsVnicFcGroupTemplQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 15),
    _CucsVnicFcGroupTemplQosPolicyName_Type()
)
cucsVnicFcGroupTemplQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplQosPolicyName.setStatus("current")
_CucsVnicFcGroupTemplStatsPolicyName_Type = SnmpAdminString
_CucsVnicFcGroupTemplStatsPolicyName_Object = MibTableColumn
cucsVnicFcGroupTemplStatsPolicyName = _CucsVnicFcGroupTemplStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 16),
    _CucsVnicFcGroupTemplStatsPolicyName_Type()
)
cucsVnicFcGroupTemplStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplStatsPolicyName.setStatus("current")
_CucsVnicFcGroupTemplStorageConnPolicyName_Type = SnmpAdminString
_CucsVnicFcGroupTemplStorageConnPolicyName_Object = MibTableColumn
cucsVnicFcGroupTemplStorageConnPolicyName = _CucsVnicFcGroupTemplStorageConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 17),
    _CucsVnicFcGroupTemplStorageConnPolicyName_Type()
)
cucsVnicFcGroupTemplStorageConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplStorageConnPolicyName.setStatus("current")
_CucsVnicFcGroupTemplTemplType_Type = CucsVnicTemplateType
_CucsVnicFcGroupTemplTemplType_Object = MibTableColumn
cucsVnicFcGroupTemplTemplType = _CucsVnicFcGroupTemplTemplType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 49, 1, 18),
    _CucsVnicFcGroupTemplTemplType_Type()
)
cucsVnicFcGroupTemplTemplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicFcGroupTemplTemplType.setStatus("current")
_CucsVnicIScsiBootParamsTable_Object = MibTable
cucsVnicIScsiBootParamsTable = _CucsVnicIScsiBootParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 50)
)
if mibBuilder.loadTexts:
    cucsVnicIScsiBootParamsTable.setStatus("current")
_CucsVnicIScsiBootParamsEntry_Object = MibTableRow
cucsVnicIScsiBootParamsEntry = _CucsVnicIScsiBootParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 50, 1)
)
cucsVnicIScsiBootParamsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIScsiBootParamsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIScsiBootParamsEntry.setStatus("current")
_CucsVnicIScsiBootParamsInstanceId_Type = CucsManagedObjectId
_CucsVnicIScsiBootParamsInstanceId_Object = MibTableColumn
cucsVnicIScsiBootParamsInstanceId = _CucsVnicIScsiBootParamsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 50, 1, 1),
    _CucsVnicIScsiBootParamsInstanceId_Type()
)
cucsVnicIScsiBootParamsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootParamsInstanceId.setStatus("current")
_CucsVnicIScsiBootParamsDn_Type = CucsManagedObjectDn
_CucsVnicIScsiBootParamsDn_Object = MibTableColumn
cucsVnicIScsiBootParamsDn = _CucsVnicIScsiBootParamsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 50, 1, 2),
    _CucsVnicIScsiBootParamsDn_Type()
)
cucsVnicIScsiBootParamsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootParamsDn.setStatus("current")
_CucsVnicIScsiBootParamsRn_Type = SnmpAdminString
_CucsVnicIScsiBootParamsRn_Object = MibTableColumn
cucsVnicIScsiBootParamsRn = _CucsVnicIScsiBootParamsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 50, 1, 3),
    _CucsVnicIScsiBootParamsRn_Type()
)
cucsVnicIScsiBootParamsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootParamsRn.setStatus("current")
_CucsVnicIScsiBootParamsDescr_Type = SnmpAdminString
_CucsVnicIScsiBootParamsDescr_Object = MibTableColumn
cucsVnicIScsiBootParamsDescr = _CucsVnicIScsiBootParamsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 50, 1, 4),
    _CucsVnicIScsiBootParamsDescr_Type()
)
cucsVnicIScsiBootParamsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootParamsDescr.setStatus("current")
_CucsVnicIScsiBootParamsIntId_Type = SnmpAdminString
_CucsVnicIScsiBootParamsIntId_Object = MibTableColumn
cucsVnicIScsiBootParamsIntId = _CucsVnicIScsiBootParamsIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 50, 1, 5),
    _CucsVnicIScsiBootParamsIntId_Type()
)
cucsVnicIScsiBootParamsIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootParamsIntId.setStatus("current")
_CucsVnicIScsiBootParamsName_Type = SnmpAdminString
_CucsVnicIScsiBootParamsName_Object = MibTableColumn
cucsVnicIScsiBootParamsName = _CucsVnicIScsiBootParamsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 50, 1, 6),
    _CucsVnicIScsiBootParamsName_Type()
)
cucsVnicIScsiBootParamsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootParamsName.setStatus("current")
_CucsVnicIScsiBootParamsPolicyLevel_Type = Gauge32
_CucsVnicIScsiBootParamsPolicyLevel_Object = MibTableColumn
cucsVnicIScsiBootParamsPolicyLevel = _CucsVnicIScsiBootParamsPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 50, 1, 7),
    _CucsVnicIScsiBootParamsPolicyLevel_Type()
)
cucsVnicIScsiBootParamsPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootParamsPolicyLevel.setStatus("current")
_CucsVnicIScsiBootParamsPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicIScsiBootParamsPolicyOwner_Object = MibTableColumn
cucsVnicIScsiBootParamsPolicyOwner = _CucsVnicIScsiBootParamsPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 50, 1, 8),
    _CucsVnicIScsiBootParamsPolicyOwner_Type()
)
cucsVnicIScsiBootParamsPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootParamsPolicyOwner.setStatus("current")
_CucsVnicIScsiBootParamsOwner_Type = CucsLsOwner
_CucsVnicIScsiBootParamsOwner_Object = MibTableColumn
cucsVnicIScsiBootParamsOwner = _CucsVnicIScsiBootParamsOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 50, 1, 9),
    _CucsVnicIScsiBootParamsOwner_Type()
)
cucsVnicIScsiBootParamsOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootParamsOwner.setStatus("current")
_CucsVnicIScsiBootParamsPropAcl_Type = Unsigned64
_CucsVnicIScsiBootParamsPropAcl_Object = MibTableColumn
cucsVnicIScsiBootParamsPropAcl = _CucsVnicIScsiBootParamsPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 50, 1, 10),
    _CucsVnicIScsiBootParamsPropAcl_Type()
)
cucsVnicIScsiBootParamsPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootParamsPropAcl.setStatus("current")
_CucsVnicIScsiBootVnicTable_Object = MibTable
cucsVnicIScsiBootVnicTable = _CucsVnicIScsiBootVnicTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 51)
)
if mibBuilder.loadTexts:
    cucsVnicIScsiBootVnicTable.setStatus("current")
_CucsVnicIScsiBootVnicEntry_Object = MibTableRow
cucsVnicIScsiBootVnicEntry = _CucsVnicIScsiBootVnicEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 51, 1)
)
cucsVnicIScsiBootVnicEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIScsiBootVnicInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIScsiBootVnicEntry.setStatus("current")
_CucsVnicIScsiBootVnicInstanceId_Type = CucsManagedObjectId
_CucsVnicIScsiBootVnicInstanceId_Object = MibTableColumn
cucsVnicIScsiBootVnicInstanceId = _CucsVnicIScsiBootVnicInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 51, 1, 1),
    _CucsVnicIScsiBootVnicInstanceId_Type()
)
cucsVnicIScsiBootVnicInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootVnicInstanceId.setStatus("current")
_CucsVnicIScsiBootVnicDn_Type = CucsManagedObjectDn
_CucsVnicIScsiBootVnicDn_Object = MibTableColumn
cucsVnicIScsiBootVnicDn = _CucsVnicIScsiBootVnicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 51, 1, 2),
    _CucsVnicIScsiBootVnicDn_Type()
)
cucsVnicIScsiBootVnicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootVnicDn.setStatus("current")
_CucsVnicIScsiBootVnicRn_Type = SnmpAdminString
_CucsVnicIScsiBootVnicRn_Object = MibTableColumn
cucsVnicIScsiBootVnicRn = _CucsVnicIScsiBootVnicRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 51, 1, 3),
    _CucsVnicIScsiBootVnicRn_Type()
)
cucsVnicIScsiBootVnicRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootVnicRn.setStatus("current")
_CucsVnicIScsiBootVnicAuthProfileName_Type = SnmpAdminString
_CucsVnicIScsiBootVnicAuthProfileName_Object = MibTableColumn
cucsVnicIScsiBootVnicAuthProfileName = _CucsVnicIScsiBootVnicAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 51, 1, 4),
    _CucsVnicIScsiBootVnicAuthProfileName_Type()
)
cucsVnicIScsiBootVnicAuthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootVnicAuthProfileName.setStatus("current")
_CucsVnicIScsiBootVnicDescr_Type = SnmpAdminString
_CucsVnicIScsiBootVnicDescr_Object = MibTableColumn
cucsVnicIScsiBootVnicDescr = _CucsVnicIScsiBootVnicDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 51, 1, 5),
    _CucsVnicIScsiBootVnicDescr_Type()
)
cucsVnicIScsiBootVnicDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootVnicDescr.setStatus("current")
_CucsVnicIScsiBootVnicInitiatorName_Type = SnmpAdminString
_CucsVnicIScsiBootVnicInitiatorName_Object = MibTableColumn
cucsVnicIScsiBootVnicInitiatorName = _CucsVnicIScsiBootVnicInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 51, 1, 6),
    _CucsVnicIScsiBootVnicInitiatorName_Type()
)
cucsVnicIScsiBootVnicInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootVnicInitiatorName.setStatus("current")
_CucsVnicIScsiBootVnicIntId_Type = SnmpAdminString
_CucsVnicIScsiBootVnicIntId_Object = MibTableColumn
cucsVnicIScsiBootVnicIntId = _CucsVnicIScsiBootVnicIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 51, 1, 7),
    _CucsVnicIScsiBootVnicIntId_Type()
)
cucsVnicIScsiBootVnicIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootVnicIntId.setStatus("current")
_CucsVnicIScsiBootVnicIqnIdentPoolName_Type = SnmpAdminString
_CucsVnicIScsiBootVnicIqnIdentPoolName_Object = MibTableColumn
cucsVnicIScsiBootVnicIqnIdentPoolName = _CucsVnicIScsiBootVnicIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 51, 1, 8),
    _CucsVnicIScsiBootVnicIqnIdentPoolName_Type()
)
cucsVnicIScsiBootVnicIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootVnicIqnIdentPoolName.setStatus("current")
_CucsVnicIScsiBootVnicName_Type = SnmpAdminString
_CucsVnicIScsiBootVnicName_Object = MibTableColumn
cucsVnicIScsiBootVnicName = _CucsVnicIScsiBootVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 51, 1, 9),
    _CucsVnicIScsiBootVnicName_Type()
)
cucsVnicIScsiBootVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootVnicName.setStatus("current")
_CucsVnicIScsiBootVnicOperAuthProfileName_Type = SnmpAdminString
_CucsVnicIScsiBootVnicOperAuthProfileName_Object = MibTableColumn
cucsVnicIScsiBootVnicOperAuthProfileName = _CucsVnicIScsiBootVnicOperAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 51, 1, 10),
    _CucsVnicIScsiBootVnicOperAuthProfileName_Type()
)
cucsVnicIScsiBootVnicOperAuthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootVnicOperAuthProfileName.setStatus("current")
_CucsVnicIScsiBootVnicOperIqnIdentPoolName_Type = SnmpAdminString
_CucsVnicIScsiBootVnicOperIqnIdentPoolName_Object = MibTableColumn
cucsVnicIScsiBootVnicOperIqnIdentPoolName = _CucsVnicIScsiBootVnicOperIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 51, 1, 11),
    _CucsVnicIScsiBootVnicOperIqnIdentPoolName_Type()
)
cucsVnicIScsiBootVnicOperIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootVnicOperIqnIdentPoolName.setStatus("current")
_CucsVnicIScsiBootVnicPolicyLevel_Type = Gauge32
_CucsVnicIScsiBootVnicPolicyLevel_Object = MibTableColumn
cucsVnicIScsiBootVnicPolicyLevel = _CucsVnicIScsiBootVnicPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 51, 1, 12),
    _CucsVnicIScsiBootVnicPolicyLevel_Type()
)
cucsVnicIScsiBootVnicPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootVnicPolicyLevel.setStatus("current")
_CucsVnicIScsiBootVnicPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicIScsiBootVnicPolicyOwner_Object = MibTableColumn
cucsVnicIScsiBootVnicPolicyOwner = _CucsVnicIScsiBootVnicPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 51, 1, 13),
    _CucsVnicIScsiBootVnicPolicyOwner_Type()
)
cucsVnicIScsiBootVnicPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiBootVnicPolicyOwner.setStatus("current")
_CucsVnicIScsiLCPTable_Object = MibTable
cucsVnicIScsiLCPTable = _CucsVnicIScsiLCPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52)
)
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPTable.setStatus("current")
_CucsVnicIScsiLCPEntry_Object = MibTableRow
cucsVnicIScsiLCPEntry = _CucsVnicIScsiLCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1)
)
cucsVnicIScsiLCPEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIScsiLCPInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPEntry.setStatus("current")
_CucsVnicIScsiLCPInstanceId_Type = CucsManagedObjectId
_CucsVnicIScsiLCPInstanceId_Object = MibTableColumn
cucsVnicIScsiLCPInstanceId = _CucsVnicIScsiLCPInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 1),
    _CucsVnicIScsiLCPInstanceId_Type()
)
cucsVnicIScsiLCPInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPInstanceId.setStatus("current")
_CucsVnicIScsiLCPDn_Type = CucsManagedObjectDn
_CucsVnicIScsiLCPDn_Object = MibTableColumn
cucsVnicIScsiLCPDn = _CucsVnicIScsiLCPDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 2),
    _CucsVnicIScsiLCPDn_Type()
)
cucsVnicIScsiLCPDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPDn.setStatus("current")
_CucsVnicIScsiLCPRn_Type = SnmpAdminString
_CucsVnicIScsiLCPRn_Object = MibTableColumn
cucsVnicIScsiLCPRn = _CucsVnicIScsiLCPRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 3),
    _CucsVnicIScsiLCPRn_Type()
)
cucsVnicIScsiLCPRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPRn.setStatus("current")
_CucsVnicIScsiLCPAdaptorProfileName_Type = SnmpAdminString
_CucsVnicIScsiLCPAdaptorProfileName_Object = MibTableColumn
cucsVnicIScsiLCPAdaptorProfileName = _CucsVnicIScsiLCPAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 4),
    _CucsVnicIScsiLCPAdaptorProfileName_Type()
)
cucsVnicIScsiLCPAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPAdaptorProfileName.setStatus("current")
_CucsVnicIScsiLCPAddr_Type = MacAddress
_CucsVnicIScsiLCPAddr_Object = MibTableColumn
cucsVnicIScsiLCPAddr = _CucsVnicIScsiLCPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 5),
    _CucsVnicIScsiLCPAddr_Type()
)
cucsVnicIScsiLCPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPAddr.setStatus("current")
_CucsVnicIScsiLCPAdminVcon_Type = SnmpAdminString
_CucsVnicIScsiLCPAdminVcon_Object = MibTableColumn
cucsVnicIScsiLCPAdminVcon = _CucsVnicIScsiLCPAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 6),
    _CucsVnicIScsiLCPAdminVcon_Type()
)
cucsVnicIScsiLCPAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPAdminVcon.setStatus("current")
_CucsVnicIScsiLCPBootDev_Type = CucsVnicVnicBootDev
_CucsVnicIScsiLCPBootDev_Object = MibTableColumn
cucsVnicIScsiLCPBootDev = _CucsVnicIScsiLCPBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 7),
    _CucsVnicIScsiLCPBootDev_Type()
)
cucsVnicIScsiLCPBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPBootDev.setStatus("current")
_CucsVnicIScsiLCPConfigQualifier_Type = CucsVnicConfigIssues
_CucsVnicIScsiLCPConfigQualifier_Object = MibTableColumn
cucsVnicIScsiLCPConfigQualifier = _CucsVnicIScsiLCPConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 8),
    _CucsVnicIScsiLCPConfigQualifier_Type()
)
cucsVnicIScsiLCPConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPConfigQualifier.setStatus("current")
_CucsVnicIScsiLCPConfigState_Type = CucsLsConfigState
_CucsVnicIScsiLCPConfigState_Object = MibTableColumn
cucsVnicIScsiLCPConfigState = _CucsVnicIScsiLCPConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 9),
    _CucsVnicIScsiLCPConfigState_Type()
)
cucsVnicIScsiLCPConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPConfigState.setStatus("current")
_CucsVnicIScsiLCPEquipmentDn_Type = SnmpAdminString
_CucsVnicIScsiLCPEquipmentDn_Object = MibTableColumn
cucsVnicIScsiLCPEquipmentDn = _CucsVnicIScsiLCPEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 10),
    _CucsVnicIScsiLCPEquipmentDn_Type()
)
cucsVnicIScsiLCPEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPEquipmentDn.setStatus("current")
_CucsVnicIScsiLCPFltAggr_Type = Unsigned64
_CucsVnicIScsiLCPFltAggr_Object = MibTableColumn
cucsVnicIScsiLCPFltAggr = _CucsVnicIScsiLCPFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 11),
    _CucsVnicIScsiLCPFltAggr_Type()
)
cucsVnicIScsiLCPFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPFltAggr.setStatus("current")
_CucsVnicIScsiLCPIdentPoolName_Type = SnmpAdminString
_CucsVnicIScsiLCPIdentPoolName_Object = MibTableColumn
cucsVnicIScsiLCPIdentPoolName = _CucsVnicIScsiLCPIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 12),
    _CucsVnicIScsiLCPIdentPoolName_Type()
)
cucsVnicIScsiLCPIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPIdentPoolName.setStatus("current")
_CucsVnicIScsiLCPInstType_Type = CucsVnicInstantiation
_CucsVnicIScsiLCPInstType_Object = MibTableColumn
cucsVnicIScsiLCPInstType = _CucsVnicIScsiLCPInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 13),
    _CucsVnicIScsiLCPInstType_Type()
)
cucsVnicIScsiLCPInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPInstType.setStatus("current")
_CucsVnicIScsiLCPName_Type = SnmpAdminString
_CucsVnicIScsiLCPName_Object = MibTableColumn
cucsVnicIScsiLCPName = _CucsVnicIScsiLCPName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 14),
    _CucsVnicIScsiLCPName_Type()
)
cucsVnicIScsiLCPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPName.setStatus("current")
_CucsVnicIScsiLCPNwTemplName_Type = SnmpAdminString
_CucsVnicIScsiLCPNwTemplName_Object = MibTableColumn
cucsVnicIScsiLCPNwTemplName = _CucsVnicIScsiLCPNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 15),
    _CucsVnicIScsiLCPNwTemplName_Type()
)
cucsVnicIScsiLCPNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPNwTemplName.setStatus("current")
_CucsVnicIScsiLCPOperAdaptorProfileName_Type = SnmpAdminString
_CucsVnicIScsiLCPOperAdaptorProfileName_Object = MibTableColumn
cucsVnicIScsiLCPOperAdaptorProfileName = _CucsVnicIScsiLCPOperAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 16),
    _CucsVnicIScsiLCPOperAdaptorProfileName_Type()
)
cucsVnicIScsiLCPOperAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPOperAdaptorProfileName.setStatus("current")
_CucsVnicIScsiLCPOperIdentPoolName_Type = SnmpAdminString
_CucsVnicIScsiLCPOperIdentPoolName_Object = MibTableColumn
cucsVnicIScsiLCPOperIdentPoolName = _CucsVnicIScsiLCPOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 17),
    _CucsVnicIScsiLCPOperIdentPoolName_Type()
)
cucsVnicIScsiLCPOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPOperIdentPoolName.setStatus("current")
_CucsVnicIScsiLCPOperOrder_Type = Gauge32
_CucsVnicIScsiLCPOperOrder_Object = MibTableColumn
cucsVnicIScsiLCPOperOrder = _CucsVnicIScsiLCPOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 18),
    _CucsVnicIScsiLCPOperOrder_Type()
)
cucsVnicIScsiLCPOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPOperOrder.setStatus("current")
_CucsVnicIScsiLCPOperSpeed_Type = Gauge32
_CucsVnicIScsiLCPOperSpeed_Object = MibTableColumn
cucsVnicIScsiLCPOperSpeed = _CucsVnicIScsiLCPOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 19),
    _CucsVnicIScsiLCPOperSpeed_Type()
)
cucsVnicIScsiLCPOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPOperSpeed.setStatus("current")
_CucsVnicIScsiLCPOperStatsPolicyName_Type = SnmpAdminString
_CucsVnicIScsiLCPOperStatsPolicyName_Object = MibTableColumn
cucsVnicIScsiLCPOperStatsPolicyName = _CucsVnicIScsiLCPOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 20),
    _CucsVnicIScsiLCPOperStatsPolicyName_Type()
)
cucsVnicIScsiLCPOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPOperStatsPolicyName.setStatus("current")
_CucsVnicIScsiLCPOperVcon_Type = SnmpAdminString
_CucsVnicIScsiLCPOperVcon_Object = MibTableColumn
cucsVnicIScsiLCPOperVcon = _CucsVnicIScsiLCPOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 21),
    _CucsVnicIScsiLCPOperVcon_Type()
)
cucsVnicIScsiLCPOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPOperVcon.setStatus("current")
_CucsVnicIScsiLCPOrder_Type = Gauge32
_CucsVnicIScsiLCPOrder_Object = MibTableColumn
cucsVnicIScsiLCPOrder = _CucsVnicIScsiLCPOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 22),
    _CucsVnicIScsiLCPOrder_Type()
)
cucsVnicIScsiLCPOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPOrder.setStatus("current")
_CucsVnicIScsiLCPOwner_Type = CucsVnicConnectionOwner
_CucsVnicIScsiLCPOwner_Object = MibTableColumn
cucsVnicIScsiLCPOwner = _CucsVnicIScsiLCPOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 23),
    _CucsVnicIScsiLCPOwner_Type()
)
cucsVnicIScsiLCPOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPOwner.setStatus("current")
_CucsVnicIScsiLCPPinToGroupName_Type = SnmpAdminString
_CucsVnicIScsiLCPPinToGroupName_Object = MibTableColumn
cucsVnicIScsiLCPPinToGroupName = _CucsVnicIScsiLCPPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 24),
    _CucsVnicIScsiLCPPinToGroupName_Type()
)
cucsVnicIScsiLCPPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPPinToGroupName.setStatus("current")
_CucsVnicIScsiLCPQosPolicyName_Type = SnmpAdminString
_CucsVnicIScsiLCPQosPolicyName_Object = MibTableColumn
cucsVnicIScsiLCPQosPolicyName = _CucsVnicIScsiLCPQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 25),
    _CucsVnicIScsiLCPQosPolicyName_Type()
)
cucsVnicIScsiLCPQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPQosPolicyName.setStatus("current")
_CucsVnicIScsiLCPStatsPolicyName_Type = SnmpAdminString
_CucsVnicIScsiLCPStatsPolicyName_Object = MibTableColumn
cucsVnicIScsiLCPStatsPolicyName = _CucsVnicIScsiLCPStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 26),
    _CucsVnicIScsiLCPStatsPolicyName_Type()
)
cucsVnicIScsiLCPStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPStatsPolicyName.setStatus("current")
_CucsVnicIScsiLCPSwitchId_Type = CucsNetworkSwitchId
_CucsVnicIScsiLCPSwitchId_Object = MibTableColumn
cucsVnicIScsiLCPSwitchId = _CucsVnicIScsiLCPSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 27),
    _CucsVnicIScsiLCPSwitchId_Type()
)
cucsVnicIScsiLCPSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPSwitchId.setStatus("current")
_CucsVnicIScsiLCPType_Type = CucsVnicConnectionType
_CucsVnicIScsiLCPType_Object = MibTableColumn
cucsVnicIScsiLCPType = _CucsVnicIScsiLCPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 28),
    _CucsVnicIScsiLCPType_Type()
)
cucsVnicIScsiLCPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPType.setStatus("current")
_CucsVnicIScsiLCPVnicName_Type = SnmpAdminString
_CucsVnicIScsiLCPVnicName_Object = MibTableColumn
cucsVnicIScsiLCPVnicName = _CucsVnicIScsiLCPVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 29),
    _CucsVnicIScsiLCPVnicName_Type()
)
cucsVnicIScsiLCPVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPVnicName.setStatus("current")
_CucsVnicIScsiLCPAdminHostPort_Type = CucsFabricHostPortId
_CucsVnicIScsiLCPAdminHostPort_Object = MibTableColumn
cucsVnicIScsiLCPAdminHostPort = _CucsVnicIScsiLCPAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 31),
    _CucsVnicIScsiLCPAdminHostPort_Type()
)
cucsVnicIScsiLCPAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPAdminHostPort.setStatus("current")
_CucsVnicIScsiLCPOperHostPort_Type = CucsVnicVnicOperHostPort
_CucsVnicIScsiLCPOperHostPort_Object = MibTableColumn
cucsVnicIScsiLCPOperHostPort = _CucsVnicIScsiLCPOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 32),
    _CucsVnicIScsiLCPOperHostPort_Type()
)
cucsVnicIScsiLCPOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPOperHostPort.setStatus("current")
_CucsVnicIScsiLCPAdminCdnName_Type = SnmpAdminString
_CucsVnicIScsiLCPAdminCdnName_Object = MibTableColumn
cucsVnicIScsiLCPAdminCdnName = _CucsVnicIScsiLCPAdminCdnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 33),
    _CucsVnicIScsiLCPAdminCdnName_Type()
)
cucsVnicIScsiLCPAdminCdnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPAdminCdnName.setStatus("current")
_CucsVnicIScsiLCPOperCdnName_Type = SnmpAdminString
_CucsVnicIScsiLCPOperCdnName_Object = MibTableColumn
cucsVnicIScsiLCPOperCdnName = _CucsVnicIScsiLCPOperCdnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 34),
    _CucsVnicIScsiLCPOperCdnName_Type()
)
cucsVnicIScsiLCPOperCdnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPOperCdnName.setStatus("current")
_CucsVnicIScsiLCPCdnSource_Type = CucsVnicCdnSource
_CucsVnicIScsiLCPCdnSource_Object = MibTableColumn
cucsVnicIScsiLCPCdnSource = _CucsVnicIScsiLCPCdnSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 35),
    _CucsVnicIScsiLCPCdnSource_Type()
)
cucsVnicIScsiLCPCdnSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPCdnSource.setStatus("current")
_CucsVnicIScsiLCPCdnPropInSync_Type = TruthValue
_CucsVnicIScsiLCPCdnPropInSync_Object = MibTableColumn
cucsVnicIScsiLCPCdnPropInSync = _CucsVnicIScsiLCPCdnPropInSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 52, 1, 36),
    _CucsVnicIScsiLCPCdnPropInSync_Type()
)
cucsVnicIScsiLCPCdnPropInSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiLCPCdnPropInSync.setStatus("current")
_CucsVnicLanConnPolicyTable_Object = MibTable
cucsVnicLanConnPolicyTable = _CucsVnicLanConnPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 53)
)
if mibBuilder.loadTexts:
    cucsVnicLanConnPolicyTable.setStatus("current")
_CucsVnicLanConnPolicyEntry_Object = MibTableRow
cucsVnicLanConnPolicyEntry = _CucsVnicLanConnPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 53, 1)
)
cucsVnicLanConnPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicLanConnPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicLanConnPolicyEntry.setStatus("current")
_CucsVnicLanConnPolicyInstanceId_Type = CucsManagedObjectId
_CucsVnicLanConnPolicyInstanceId_Object = MibTableColumn
cucsVnicLanConnPolicyInstanceId = _CucsVnicLanConnPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 53, 1, 1),
    _CucsVnicLanConnPolicyInstanceId_Type()
)
cucsVnicLanConnPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicLanConnPolicyInstanceId.setStatus("current")
_CucsVnicLanConnPolicyDn_Type = CucsManagedObjectDn
_CucsVnicLanConnPolicyDn_Object = MibTableColumn
cucsVnicLanConnPolicyDn = _CucsVnicLanConnPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 53, 1, 2),
    _CucsVnicLanConnPolicyDn_Type()
)
cucsVnicLanConnPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnPolicyDn.setStatus("current")
_CucsVnicLanConnPolicyRn_Type = SnmpAdminString
_CucsVnicLanConnPolicyRn_Object = MibTableColumn
cucsVnicLanConnPolicyRn = _CucsVnicLanConnPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 53, 1, 3),
    _CucsVnicLanConnPolicyRn_Type()
)
cucsVnicLanConnPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnPolicyRn.setStatus("current")
_CucsVnicLanConnPolicyDescr_Type = SnmpAdminString
_CucsVnicLanConnPolicyDescr_Object = MibTableColumn
cucsVnicLanConnPolicyDescr = _CucsVnicLanConnPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 53, 1, 4),
    _CucsVnicLanConnPolicyDescr_Type()
)
cucsVnicLanConnPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnPolicyDescr.setStatus("current")
_CucsVnicLanConnPolicyFltAggr_Type = Unsigned64
_CucsVnicLanConnPolicyFltAggr_Object = MibTableColumn
cucsVnicLanConnPolicyFltAggr = _CucsVnicLanConnPolicyFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 53, 1, 5),
    _CucsVnicLanConnPolicyFltAggr_Type()
)
cucsVnicLanConnPolicyFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnPolicyFltAggr.setStatus("current")
_CucsVnicLanConnPolicyIntId_Type = SnmpAdminString
_CucsVnicLanConnPolicyIntId_Object = MibTableColumn
cucsVnicLanConnPolicyIntId = _CucsVnicLanConnPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 53, 1, 6),
    _CucsVnicLanConnPolicyIntId_Type()
)
cucsVnicLanConnPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnPolicyIntId.setStatus("current")
_CucsVnicLanConnPolicyName_Type = SnmpAdminString
_CucsVnicLanConnPolicyName_Object = MibTableColumn
cucsVnicLanConnPolicyName = _CucsVnicLanConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 53, 1, 7),
    _CucsVnicLanConnPolicyName_Type()
)
cucsVnicLanConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnPolicyName.setStatus("current")
_CucsVnicLanConnPolicyPolicyLevel_Type = Gauge32
_CucsVnicLanConnPolicyPolicyLevel_Object = MibTableColumn
cucsVnicLanConnPolicyPolicyLevel = _CucsVnicLanConnPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 53, 1, 8),
    _CucsVnicLanConnPolicyPolicyLevel_Type()
)
cucsVnicLanConnPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnPolicyPolicyLevel.setStatus("current")
_CucsVnicLanConnPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicLanConnPolicyPolicyOwner_Object = MibTableColumn
cucsVnicLanConnPolicyPolicyOwner = _CucsVnicLanConnPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 53, 1, 9),
    _CucsVnicLanConnPolicyPolicyOwner_Type()
)
cucsVnicLanConnPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicLanConnPolicyPolicyOwner.setStatus("current")
_CucsVnicProfileSetFsmTable_Object = MibTable
cucsVnicProfileSetFsmTable = _CucsVnicProfileSetFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 54)
)
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmTable.setStatus("current")
_CucsVnicProfileSetFsmEntry_Object = MibTableRow
cucsVnicProfileSetFsmEntry = _CucsVnicProfileSetFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 54, 1)
)
cucsVnicProfileSetFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicProfileSetFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmEntry.setStatus("current")
_CucsVnicProfileSetFsmInstanceId_Type = CucsManagedObjectId
_CucsVnicProfileSetFsmInstanceId_Object = MibTableColumn
cucsVnicProfileSetFsmInstanceId = _CucsVnicProfileSetFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 54, 1, 1),
    _CucsVnicProfileSetFsmInstanceId_Type()
)
cucsVnicProfileSetFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmInstanceId.setStatus("current")
_CucsVnicProfileSetFsmDn_Type = CucsManagedObjectDn
_CucsVnicProfileSetFsmDn_Object = MibTableColumn
cucsVnicProfileSetFsmDn = _CucsVnicProfileSetFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 54, 1, 2),
    _CucsVnicProfileSetFsmDn_Type()
)
cucsVnicProfileSetFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmDn.setStatus("current")
_CucsVnicProfileSetFsmRn_Type = SnmpAdminString
_CucsVnicProfileSetFsmRn_Object = MibTableColumn
cucsVnicProfileSetFsmRn = _CucsVnicProfileSetFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 54, 1, 3),
    _CucsVnicProfileSetFsmRn_Type()
)
cucsVnicProfileSetFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmRn.setStatus("current")
_CucsVnicProfileSetFsmCompletionTime_Type = DateAndTime
_CucsVnicProfileSetFsmCompletionTime_Object = MibTableColumn
cucsVnicProfileSetFsmCompletionTime = _CucsVnicProfileSetFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 54, 1, 4),
    _CucsVnicProfileSetFsmCompletionTime_Type()
)
cucsVnicProfileSetFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmCompletionTime.setStatus("current")
_CucsVnicProfileSetFsmCurrentFsm_Type = CucsVnicProfileSetFsmCurrentFsm
_CucsVnicProfileSetFsmCurrentFsm_Object = MibTableColumn
cucsVnicProfileSetFsmCurrentFsm = _CucsVnicProfileSetFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 54, 1, 5),
    _CucsVnicProfileSetFsmCurrentFsm_Type()
)
cucsVnicProfileSetFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmCurrentFsm.setStatus("current")
_CucsVnicProfileSetFsmDescrData_Type = SnmpAdminString
_CucsVnicProfileSetFsmDescrData_Object = MibTableColumn
cucsVnicProfileSetFsmDescrData = _CucsVnicProfileSetFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 54, 1, 6),
    _CucsVnicProfileSetFsmDescrData_Type()
)
cucsVnicProfileSetFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmDescrData.setStatus("current")
_CucsVnicProfileSetFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsVnicProfileSetFsmFsmStatus_Object = MibTableColumn
cucsVnicProfileSetFsmFsmStatus = _CucsVnicProfileSetFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 54, 1, 7),
    _CucsVnicProfileSetFsmFsmStatus_Type()
)
cucsVnicProfileSetFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmFsmStatus.setStatus("current")
_CucsVnicProfileSetFsmProgress_Type = Gauge32
_CucsVnicProfileSetFsmProgress_Object = MibTableColumn
cucsVnicProfileSetFsmProgress = _CucsVnicProfileSetFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 54, 1, 8),
    _CucsVnicProfileSetFsmProgress_Type()
)
cucsVnicProfileSetFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmProgress.setStatus("current")
_CucsVnicProfileSetFsmRmtErrCode_Type = Gauge32
_CucsVnicProfileSetFsmRmtErrCode_Object = MibTableColumn
cucsVnicProfileSetFsmRmtErrCode = _CucsVnicProfileSetFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 54, 1, 9),
    _CucsVnicProfileSetFsmRmtErrCode_Type()
)
cucsVnicProfileSetFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmRmtErrCode.setStatus("current")
_CucsVnicProfileSetFsmRmtErrDescr_Type = SnmpAdminString
_CucsVnicProfileSetFsmRmtErrDescr_Object = MibTableColumn
cucsVnicProfileSetFsmRmtErrDescr = _CucsVnicProfileSetFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 54, 1, 10),
    _CucsVnicProfileSetFsmRmtErrDescr_Type()
)
cucsVnicProfileSetFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmRmtErrDescr.setStatus("current")
_CucsVnicProfileSetFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsVnicProfileSetFsmRmtRslt_Object = MibTableColumn
cucsVnicProfileSetFsmRmtRslt = _CucsVnicProfileSetFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 54, 1, 11),
    _CucsVnicProfileSetFsmRmtRslt_Type()
)
cucsVnicProfileSetFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmRmtRslt.setStatus("current")
_CucsVnicProfileSetFsmStageTable_Object = MibTable
cucsVnicProfileSetFsmStageTable = _CucsVnicProfileSetFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 55)
)
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmStageTable.setStatus("current")
_CucsVnicProfileSetFsmStageEntry_Object = MibTableRow
cucsVnicProfileSetFsmStageEntry = _CucsVnicProfileSetFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 55, 1)
)
cucsVnicProfileSetFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicProfileSetFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmStageEntry.setStatus("current")
_CucsVnicProfileSetFsmStageInstanceId_Type = CucsManagedObjectId
_CucsVnicProfileSetFsmStageInstanceId_Object = MibTableColumn
cucsVnicProfileSetFsmStageInstanceId = _CucsVnicProfileSetFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 55, 1, 1),
    _CucsVnicProfileSetFsmStageInstanceId_Type()
)
cucsVnicProfileSetFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmStageInstanceId.setStatus("current")
_CucsVnicProfileSetFsmStageDn_Type = CucsManagedObjectDn
_CucsVnicProfileSetFsmStageDn_Object = MibTableColumn
cucsVnicProfileSetFsmStageDn = _CucsVnicProfileSetFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 55, 1, 2),
    _CucsVnicProfileSetFsmStageDn_Type()
)
cucsVnicProfileSetFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmStageDn.setStatus("current")
_CucsVnicProfileSetFsmStageRn_Type = SnmpAdminString
_CucsVnicProfileSetFsmStageRn_Object = MibTableColumn
cucsVnicProfileSetFsmStageRn = _CucsVnicProfileSetFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 55, 1, 3),
    _CucsVnicProfileSetFsmStageRn_Type()
)
cucsVnicProfileSetFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmStageRn.setStatus("current")
_CucsVnicProfileSetFsmStageDescrData_Type = SnmpAdminString
_CucsVnicProfileSetFsmStageDescrData_Object = MibTableColumn
cucsVnicProfileSetFsmStageDescrData = _CucsVnicProfileSetFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 55, 1, 4),
    _CucsVnicProfileSetFsmStageDescrData_Type()
)
cucsVnicProfileSetFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmStageDescrData.setStatus("current")
_CucsVnicProfileSetFsmStageLastUpdateTime_Type = DateAndTime
_CucsVnicProfileSetFsmStageLastUpdateTime_Object = MibTableColumn
cucsVnicProfileSetFsmStageLastUpdateTime = _CucsVnicProfileSetFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 55, 1, 5),
    _CucsVnicProfileSetFsmStageLastUpdateTime_Type()
)
cucsVnicProfileSetFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmStageLastUpdateTime.setStatus("current")
_CucsVnicProfileSetFsmStageName_Type = CucsVnicProfileSetFsmStageName
_CucsVnicProfileSetFsmStageName_Object = MibTableColumn
cucsVnicProfileSetFsmStageName = _CucsVnicProfileSetFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 55, 1, 6),
    _CucsVnicProfileSetFsmStageName_Type()
)
cucsVnicProfileSetFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmStageName.setStatus("current")
_CucsVnicProfileSetFsmStageOrder_Type = Gauge32
_CucsVnicProfileSetFsmStageOrder_Object = MibTableColumn
cucsVnicProfileSetFsmStageOrder = _CucsVnicProfileSetFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 55, 1, 7),
    _CucsVnicProfileSetFsmStageOrder_Type()
)
cucsVnicProfileSetFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmStageOrder.setStatus("current")
_CucsVnicProfileSetFsmStageRetry_Type = Gauge32
_CucsVnicProfileSetFsmStageRetry_Object = MibTableColumn
cucsVnicProfileSetFsmStageRetry = _CucsVnicProfileSetFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 55, 1, 8),
    _CucsVnicProfileSetFsmStageRetry_Type()
)
cucsVnicProfileSetFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmStageRetry.setStatus("current")
_CucsVnicProfileSetFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsVnicProfileSetFsmStageStageStatus_Object = MibTableColumn
cucsVnicProfileSetFsmStageStageStatus = _CucsVnicProfileSetFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 55, 1, 9),
    _CucsVnicProfileSetFsmStageStageStatus_Type()
)
cucsVnicProfileSetFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileSetFsmStageStageStatus.setStatus("current")
_CucsVnicRackServerDiscoveryProfileTable_Object = MibTable
cucsVnicRackServerDiscoveryProfileTable = _CucsVnicRackServerDiscoveryProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 56)
)
if mibBuilder.loadTexts:
    cucsVnicRackServerDiscoveryProfileTable.setStatus("current")
_CucsVnicRackServerDiscoveryProfileEntry_Object = MibTableRow
cucsVnicRackServerDiscoveryProfileEntry = _CucsVnicRackServerDiscoveryProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 56, 1)
)
cucsVnicRackServerDiscoveryProfileEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicRackServerDiscoveryProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicRackServerDiscoveryProfileEntry.setStatus("current")
_CucsVnicRackServerDiscoveryProfileInstanceId_Type = CucsManagedObjectId
_CucsVnicRackServerDiscoveryProfileInstanceId_Object = MibTableColumn
cucsVnicRackServerDiscoveryProfileInstanceId = _CucsVnicRackServerDiscoveryProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 56, 1, 1),
    _CucsVnicRackServerDiscoveryProfileInstanceId_Type()
)
cucsVnicRackServerDiscoveryProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicRackServerDiscoveryProfileInstanceId.setStatus("current")
_CucsVnicRackServerDiscoveryProfileDn_Type = CucsManagedObjectDn
_CucsVnicRackServerDiscoveryProfileDn_Object = MibTableColumn
cucsVnicRackServerDiscoveryProfileDn = _CucsVnicRackServerDiscoveryProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 56, 1, 2),
    _CucsVnicRackServerDiscoveryProfileDn_Type()
)
cucsVnicRackServerDiscoveryProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicRackServerDiscoveryProfileDn.setStatus("current")
_CucsVnicRackServerDiscoveryProfileRn_Type = SnmpAdminString
_CucsVnicRackServerDiscoveryProfileRn_Object = MibTableColumn
cucsVnicRackServerDiscoveryProfileRn = _CucsVnicRackServerDiscoveryProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 56, 1, 3),
    _CucsVnicRackServerDiscoveryProfileRn_Type()
)
cucsVnicRackServerDiscoveryProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicRackServerDiscoveryProfileRn.setStatus("current")
_CucsVnicRackServerDiscoveryProfileDescr_Type = SnmpAdminString
_CucsVnicRackServerDiscoveryProfileDescr_Object = MibTableColumn
cucsVnicRackServerDiscoveryProfileDescr = _CucsVnicRackServerDiscoveryProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 56, 1, 4),
    _CucsVnicRackServerDiscoveryProfileDescr_Type()
)
cucsVnicRackServerDiscoveryProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicRackServerDiscoveryProfileDescr.setStatus("current")
_CucsVnicRackServerDiscoveryProfileIntId_Type = SnmpAdminString
_CucsVnicRackServerDiscoveryProfileIntId_Object = MibTableColumn
cucsVnicRackServerDiscoveryProfileIntId = _CucsVnicRackServerDiscoveryProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 56, 1, 5),
    _CucsVnicRackServerDiscoveryProfileIntId_Type()
)
cucsVnicRackServerDiscoveryProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicRackServerDiscoveryProfileIntId.setStatus("current")
_CucsVnicRackServerDiscoveryProfileMaxPorts_Type = Gauge32
_CucsVnicRackServerDiscoveryProfileMaxPorts_Object = MibTableColumn
cucsVnicRackServerDiscoveryProfileMaxPorts = _CucsVnicRackServerDiscoveryProfileMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 56, 1, 6),
    _CucsVnicRackServerDiscoveryProfileMaxPorts_Type()
)
cucsVnicRackServerDiscoveryProfileMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicRackServerDiscoveryProfileMaxPorts.setStatus("current")
_CucsVnicRackServerDiscoveryProfileName_Type = SnmpAdminString
_CucsVnicRackServerDiscoveryProfileName_Object = MibTableColumn
cucsVnicRackServerDiscoveryProfileName = _CucsVnicRackServerDiscoveryProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 56, 1, 7),
    _CucsVnicRackServerDiscoveryProfileName_Type()
)
cucsVnicRackServerDiscoveryProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicRackServerDiscoveryProfileName.setStatus("current")
_CucsVnicRackServerDiscoveryProfilePolicyLevel_Type = Gauge32
_CucsVnicRackServerDiscoveryProfilePolicyLevel_Object = MibTableColumn
cucsVnicRackServerDiscoveryProfilePolicyLevel = _CucsVnicRackServerDiscoveryProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 56, 1, 8),
    _CucsVnicRackServerDiscoveryProfilePolicyLevel_Type()
)
cucsVnicRackServerDiscoveryProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicRackServerDiscoveryProfilePolicyLevel.setStatus("current")
_CucsVnicRackServerDiscoveryProfilePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicRackServerDiscoveryProfilePolicyOwner_Object = MibTableColumn
cucsVnicRackServerDiscoveryProfilePolicyOwner = _CucsVnicRackServerDiscoveryProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 56, 1, 9),
    _CucsVnicRackServerDiscoveryProfilePolicyOwner_Type()
)
cucsVnicRackServerDiscoveryProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicRackServerDiscoveryProfilePolicyOwner.setStatus("current")
_CucsVnicSanConnPolicyTable_Object = MibTable
cucsVnicSanConnPolicyTable = _CucsVnicSanConnPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 57)
)
if mibBuilder.loadTexts:
    cucsVnicSanConnPolicyTable.setStatus("current")
_CucsVnicSanConnPolicyEntry_Object = MibTableRow
cucsVnicSanConnPolicyEntry = _CucsVnicSanConnPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 57, 1)
)
cucsVnicSanConnPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicSanConnPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicSanConnPolicyEntry.setStatus("current")
_CucsVnicSanConnPolicyInstanceId_Type = CucsManagedObjectId
_CucsVnicSanConnPolicyInstanceId_Object = MibTableColumn
cucsVnicSanConnPolicyInstanceId = _CucsVnicSanConnPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 57, 1, 1),
    _CucsVnicSanConnPolicyInstanceId_Type()
)
cucsVnicSanConnPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicSanConnPolicyInstanceId.setStatus("current")
_CucsVnicSanConnPolicyDn_Type = CucsManagedObjectDn
_CucsVnicSanConnPolicyDn_Object = MibTableColumn
cucsVnicSanConnPolicyDn = _CucsVnicSanConnPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 57, 1, 2),
    _CucsVnicSanConnPolicyDn_Type()
)
cucsVnicSanConnPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnPolicyDn.setStatus("current")
_CucsVnicSanConnPolicyRn_Type = SnmpAdminString
_CucsVnicSanConnPolicyRn_Object = MibTableColumn
cucsVnicSanConnPolicyRn = _CucsVnicSanConnPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 57, 1, 3),
    _CucsVnicSanConnPolicyRn_Type()
)
cucsVnicSanConnPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnPolicyRn.setStatus("current")
_CucsVnicSanConnPolicyDescr_Type = SnmpAdminString
_CucsVnicSanConnPolicyDescr_Object = MibTableColumn
cucsVnicSanConnPolicyDescr = _CucsVnicSanConnPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 57, 1, 4),
    _CucsVnicSanConnPolicyDescr_Type()
)
cucsVnicSanConnPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnPolicyDescr.setStatus("current")
_CucsVnicSanConnPolicyFltAggr_Type = Unsigned64
_CucsVnicSanConnPolicyFltAggr_Object = MibTableColumn
cucsVnicSanConnPolicyFltAggr = _CucsVnicSanConnPolicyFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 57, 1, 5),
    _CucsVnicSanConnPolicyFltAggr_Type()
)
cucsVnicSanConnPolicyFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnPolicyFltAggr.setStatus("current")
_CucsVnicSanConnPolicyIntId_Type = SnmpAdminString
_CucsVnicSanConnPolicyIntId_Object = MibTableColumn
cucsVnicSanConnPolicyIntId = _CucsVnicSanConnPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 57, 1, 6),
    _CucsVnicSanConnPolicyIntId_Type()
)
cucsVnicSanConnPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnPolicyIntId.setStatus("current")
_CucsVnicSanConnPolicyName_Type = SnmpAdminString
_CucsVnicSanConnPolicyName_Object = MibTableColumn
cucsVnicSanConnPolicyName = _CucsVnicSanConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 57, 1, 7),
    _CucsVnicSanConnPolicyName_Type()
)
cucsVnicSanConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnPolicyName.setStatus("current")
_CucsVnicSanConnPolicyPolicyLevel_Type = Gauge32
_CucsVnicSanConnPolicyPolicyLevel_Object = MibTableColumn
cucsVnicSanConnPolicyPolicyLevel = _CucsVnicSanConnPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 57, 1, 8),
    _CucsVnicSanConnPolicyPolicyLevel_Type()
)
cucsVnicSanConnPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnPolicyPolicyLevel.setStatus("current")
_CucsVnicSanConnPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicSanConnPolicyPolicyOwner_Object = MibTableColumn
cucsVnicSanConnPolicyPolicyOwner = _CucsVnicSanConnPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 57, 1, 9),
    _CucsVnicSanConnPolicyPolicyOwner_Type()
)
cucsVnicSanConnPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicSanConnPolicyPolicyOwner.setStatus("current")
_CucsVnicVhbaBehPolicyTable_Object = MibTable
cucsVnicVhbaBehPolicyTable = _CucsVnicVhbaBehPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 58)
)
if mibBuilder.loadTexts:
    cucsVnicVhbaBehPolicyTable.setStatus("current")
_CucsVnicVhbaBehPolicyEntry_Object = MibTableRow
cucsVnicVhbaBehPolicyEntry = _CucsVnicVhbaBehPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 58, 1)
)
cucsVnicVhbaBehPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicVhbaBehPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicVhbaBehPolicyEntry.setStatus("current")
_CucsVnicVhbaBehPolicyInstanceId_Type = CucsManagedObjectId
_CucsVnicVhbaBehPolicyInstanceId_Object = MibTableColumn
cucsVnicVhbaBehPolicyInstanceId = _CucsVnicVhbaBehPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 58, 1, 1),
    _CucsVnicVhbaBehPolicyInstanceId_Type()
)
cucsVnicVhbaBehPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicVhbaBehPolicyInstanceId.setStatus("current")
_CucsVnicVhbaBehPolicyDn_Type = CucsManagedObjectDn
_CucsVnicVhbaBehPolicyDn_Object = MibTableColumn
cucsVnicVhbaBehPolicyDn = _CucsVnicVhbaBehPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 58, 1, 2),
    _CucsVnicVhbaBehPolicyDn_Type()
)
cucsVnicVhbaBehPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVhbaBehPolicyDn.setStatus("current")
_CucsVnicVhbaBehPolicyRn_Type = SnmpAdminString
_CucsVnicVhbaBehPolicyRn_Object = MibTableColumn
cucsVnicVhbaBehPolicyRn = _CucsVnicVhbaBehPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 58, 1, 3),
    _CucsVnicVhbaBehPolicyRn_Type()
)
cucsVnicVhbaBehPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVhbaBehPolicyRn.setStatus("current")
_CucsVnicVhbaBehPolicyAction_Type = CucsVnicDefaultAction
_CucsVnicVhbaBehPolicyAction_Object = MibTableColumn
cucsVnicVhbaBehPolicyAction = _CucsVnicVhbaBehPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 58, 1, 4),
    _CucsVnicVhbaBehPolicyAction_Type()
)
cucsVnicVhbaBehPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVhbaBehPolicyAction.setStatus("current")
_CucsVnicVhbaBehPolicyDescr_Type = SnmpAdminString
_CucsVnicVhbaBehPolicyDescr_Object = MibTableColumn
cucsVnicVhbaBehPolicyDescr = _CucsVnicVhbaBehPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 58, 1, 5),
    _CucsVnicVhbaBehPolicyDescr_Type()
)
cucsVnicVhbaBehPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVhbaBehPolicyDescr.setStatus("current")
_CucsVnicVhbaBehPolicyIntId_Type = SnmpAdminString
_CucsVnicVhbaBehPolicyIntId_Object = MibTableColumn
cucsVnicVhbaBehPolicyIntId = _CucsVnicVhbaBehPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 58, 1, 6),
    _CucsVnicVhbaBehPolicyIntId_Type()
)
cucsVnicVhbaBehPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVhbaBehPolicyIntId.setStatus("current")
_CucsVnicVhbaBehPolicyName_Type = SnmpAdminString
_CucsVnicVhbaBehPolicyName_Object = MibTableColumn
cucsVnicVhbaBehPolicyName = _CucsVnicVhbaBehPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 58, 1, 7),
    _CucsVnicVhbaBehPolicyName_Type()
)
cucsVnicVhbaBehPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVhbaBehPolicyName.setStatus("current")
_CucsVnicVhbaBehPolicyNwTemplName_Type = SnmpAdminString
_CucsVnicVhbaBehPolicyNwTemplName_Object = MibTableColumn
cucsVnicVhbaBehPolicyNwTemplName = _CucsVnicVhbaBehPolicyNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 58, 1, 8),
    _CucsVnicVhbaBehPolicyNwTemplName_Type()
)
cucsVnicVhbaBehPolicyNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVhbaBehPolicyNwTemplName.setStatus("current")
_CucsVnicVhbaBehPolicyPolicyLevel_Type = Gauge32
_CucsVnicVhbaBehPolicyPolicyLevel_Object = MibTableColumn
cucsVnicVhbaBehPolicyPolicyLevel = _CucsVnicVhbaBehPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 58, 1, 9),
    _CucsVnicVhbaBehPolicyPolicyLevel_Type()
)
cucsVnicVhbaBehPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVhbaBehPolicyPolicyLevel.setStatus("current")
_CucsVnicVhbaBehPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicVhbaBehPolicyPolicyOwner_Object = MibTableColumn
cucsVnicVhbaBehPolicyPolicyOwner = _CucsVnicVhbaBehPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 58, 1, 10),
    _CucsVnicVhbaBehPolicyPolicyOwner_Type()
)
cucsVnicVhbaBehPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVhbaBehPolicyPolicyOwner.setStatus("current")
_CucsVnicVhbaBehPolicyType_Type = CucsVnicVhbaBehPolicyType
_CucsVnicVhbaBehPolicyType_Object = MibTableColumn
cucsVnicVhbaBehPolicyType = _CucsVnicVhbaBehPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 58, 1, 11),
    _CucsVnicVhbaBehPolicyType_Type()
)
cucsVnicVhbaBehPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVhbaBehPolicyType.setStatus("current")
_CucsVnicVnicBehPolicyTable_Object = MibTable
cucsVnicVnicBehPolicyTable = _CucsVnicVnicBehPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 59)
)
if mibBuilder.loadTexts:
    cucsVnicVnicBehPolicyTable.setStatus("current")
_CucsVnicVnicBehPolicyEntry_Object = MibTableRow
cucsVnicVnicBehPolicyEntry = _CucsVnicVnicBehPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 59, 1)
)
cucsVnicVnicBehPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicVnicBehPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicVnicBehPolicyEntry.setStatus("current")
_CucsVnicVnicBehPolicyInstanceId_Type = CucsManagedObjectId
_CucsVnicVnicBehPolicyInstanceId_Object = MibTableColumn
cucsVnicVnicBehPolicyInstanceId = _CucsVnicVnicBehPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 59, 1, 1),
    _CucsVnicVnicBehPolicyInstanceId_Type()
)
cucsVnicVnicBehPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicVnicBehPolicyInstanceId.setStatus("current")
_CucsVnicVnicBehPolicyDn_Type = CucsManagedObjectDn
_CucsVnicVnicBehPolicyDn_Object = MibTableColumn
cucsVnicVnicBehPolicyDn = _CucsVnicVnicBehPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 59, 1, 2),
    _CucsVnicVnicBehPolicyDn_Type()
)
cucsVnicVnicBehPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVnicBehPolicyDn.setStatus("current")
_CucsVnicVnicBehPolicyRn_Type = SnmpAdminString
_CucsVnicVnicBehPolicyRn_Object = MibTableColumn
cucsVnicVnicBehPolicyRn = _CucsVnicVnicBehPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 59, 1, 3),
    _CucsVnicVnicBehPolicyRn_Type()
)
cucsVnicVnicBehPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVnicBehPolicyRn.setStatus("current")
_CucsVnicVnicBehPolicyAction_Type = CucsVnicDefaultAction
_CucsVnicVnicBehPolicyAction_Object = MibTableColumn
cucsVnicVnicBehPolicyAction = _CucsVnicVnicBehPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 59, 1, 4),
    _CucsVnicVnicBehPolicyAction_Type()
)
cucsVnicVnicBehPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVnicBehPolicyAction.setStatus("current")
_CucsVnicVnicBehPolicyDescr_Type = SnmpAdminString
_CucsVnicVnicBehPolicyDescr_Object = MibTableColumn
cucsVnicVnicBehPolicyDescr = _CucsVnicVnicBehPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 59, 1, 5),
    _CucsVnicVnicBehPolicyDescr_Type()
)
cucsVnicVnicBehPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVnicBehPolicyDescr.setStatus("current")
_CucsVnicVnicBehPolicyIntId_Type = SnmpAdminString
_CucsVnicVnicBehPolicyIntId_Object = MibTableColumn
cucsVnicVnicBehPolicyIntId = _CucsVnicVnicBehPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 59, 1, 6),
    _CucsVnicVnicBehPolicyIntId_Type()
)
cucsVnicVnicBehPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVnicBehPolicyIntId.setStatus("current")
_CucsVnicVnicBehPolicyName_Type = SnmpAdminString
_CucsVnicVnicBehPolicyName_Object = MibTableColumn
cucsVnicVnicBehPolicyName = _CucsVnicVnicBehPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 59, 1, 7),
    _CucsVnicVnicBehPolicyName_Type()
)
cucsVnicVnicBehPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVnicBehPolicyName.setStatus("current")
_CucsVnicVnicBehPolicyNwTemplName_Type = SnmpAdminString
_CucsVnicVnicBehPolicyNwTemplName_Object = MibTableColumn
cucsVnicVnicBehPolicyNwTemplName = _CucsVnicVnicBehPolicyNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 59, 1, 8),
    _CucsVnicVnicBehPolicyNwTemplName_Type()
)
cucsVnicVnicBehPolicyNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVnicBehPolicyNwTemplName.setStatus("current")
_CucsVnicVnicBehPolicyPolicyLevel_Type = Gauge32
_CucsVnicVnicBehPolicyPolicyLevel_Object = MibTableColumn
cucsVnicVnicBehPolicyPolicyLevel = _CucsVnicVnicBehPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 59, 1, 9),
    _CucsVnicVnicBehPolicyPolicyLevel_Type()
)
cucsVnicVnicBehPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVnicBehPolicyPolicyLevel.setStatus("current")
_CucsVnicVnicBehPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicVnicBehPolicyPolicyOwner_Object = MibTableColumn
cucsVnicVnicBehPolicyPolicyOwner = _CucsVnicVnicBehPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 59, 1, 10),
    _CucsVnicVnicBehPolicyPolicyOwner_Type()
)
cucsVnicVnicBehPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVnicBehPolicyPolicyOwner.setStatus("current")
_CucsVnicVnicBehPolicyType_Type = CucsVnicVnicBehPolicyType
_CucsVnicVnicBehPolicyType_Object = MibTableColumn
cucsVnicVnicBehPolicyType = _CucsVnicVnicBehPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 59, 1, 11),
    _CucsVnicVnicBehPolicyType_Type()
)
cucsVnicVnicBehPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVnicBehPolicyType.setStatus("current")
_CucsVnicIpV4HistoryTable_Object = MibTable
cucsVnicIpV4HistoryTable = _CucsVnicIpV4HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 60)
)
if mibBuilder.loadTexts:
    cucsVnicIpV4HistoryTable.setStatus("current")
_CucsVnicIpV4HistoryEntry_Object = MibTableRow
cucsVnicIpV4HistoryEntry = _CucsVnicIpV4HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 60, 1)
)
cucsVnicIpV4HistoryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIpV4HistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIpV4HistoryEntry.setStatus("current")
_CucsVnicIpV4HistoryInstanceId_Type = CucsManagedObjectId
_CucsVnicIpV4HistoryInstanceId_Object = MibTableColumn
cucsVnicIpV4HistoryInstanceId = _CucsVnicIpV4HistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 60, 1, 1),
    _CucsVnicIpV4HistoryInstanceId_Type()
)
cucsVnicIpV4HistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIpV4HistoryInstanceId.setStatus("current")
_CucsVnicIpV4HistoryDn_Type = CucsManagedObjectDn
_CucsVnicIpV4HistoryDn_Object = MibTableColumn
cucsVnicIpV4HistoryDn = _CucsVnicIpV4HistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 60, 1, 2),
    _CucsVnicIpV4HistoryDn_Type()
)
cucsVnicIpV4HistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4HistoryDn.setStatus("current")
_CucsVnicIpV4HistoryRn_Type = SnmpAdminString
_CucsVnicIpV4HistoryRn_Object = MibTableColumn
cucsVnicIpV4HistoryRn = _CucsVnicIpV4HistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 60, 1, 3),
    _CucsVnicIpV4HistoryRn_Type()
)
cucsVnicIpV4HistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4HistoryRn.setStatus("current")
_CucsVnicIpV4HistoryOldIpV4Addr_Type = InetAddressIPv4
_CucsVnicIpV4HistoryOldIpV4Addr_Object = MibTableColumn
cucsVnicIpV4HistoryOldIpV4Addr = _CucsVnicIpV4HistoryOldIpV4Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 60, 1, 4),
    _CucsVnicIpV4HistoryOldIpV4Addr_Type()
)
cucsVnicIpV4HistoryOldIpV4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4HistoryOldIpV4Addr.setStatus("current")
_CucsVnicIqnHistoryTable_Object = MibTable
cucsVnicIqnHistoryTable = _CucsVnicIqnHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 61)
)
if mibBuilder.loadTexts:
    cucsVnicIqnHistoryTable.setStatus("current")
_CucsVnicIqnHistoryEntry_Object = MibTableRow
cucsVnicIqnHistoryEntry = _CucsVnicIqnHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 61, 1)
)
cucsVnicIqnHistoryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIqnHistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIqnHistoryEntry.setStatus("current")
_CucsVnicIqnHistoryInstanceId_Type = CucsManagedObjectId
_CucsVnicIqnHistoryInstanceId_Object = MibTableColumn
cucsVnicIqnHistoryInstanceId = _CucsVnicIqnHistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 61, 1, 1),
    _CucsVnicIqnHistoryInstanceId_Type()
)
cucsVnicIqnHistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIqnHistoryInstanceId.setStatus("current")
_CucsVnicIqnHistoryDn_Type = CucsManagedObjectDn
_CucsVnicIqnHistoryDn_Object = MibTableColumn
cucsVnicIqnHistoryDn = _CucsVnicIqnHistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 61, 1, 2),
    _CucsVnicIqnHistoryDn_Type()
)
cucsVnicIqnHistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIqnHistoryDn.setStatus("current")
_CucsVnicIqnHistoryRn_Type = SnmpAdminString
_CucsVnicIqnHistoryRn_Object = MibTableColumn
cucsVnicIqnHistoryRn = _CucsVnicIqnHistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 61, 1, 3),
    _CucsVnicIqnHistoryRn_Type()
)
cucsVnicIqnHistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIqnHistoryRn.setStatus("current")
_CucsVnicIqnHistoryOldInitiatorName_Type = SnmpAdminString
_CucsVnicIqnHistoryOldInitiatorName_Object = MibTableColumn
cucsVnicIqnHistoryOldInitiatorName = _CucsVnicIqnHistoryOldInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 61, 1, 4),
    _CucsVnicIqnHistoryOldInitiatorName_Type()
)
cucsVnicIqnHistoryOldInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIqnHistoryOldInitiatorName.setStatus("current")
_CucsVnicMacHistoryTable_Object = MibTable
cucsVnicMacHistoryTable = _CucsVnicMacHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 62)
)
if mibBuilder.loadTexts:
    cucsVnicMacHistoryTable.setStatus("current")
_CucsVnicMacHistoryEntry_Object = MibTableRow
cucsVnicMacHistoryEntry = _CucsVnicMacHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 62, 1)
)
cucsVnicMacHistoryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicMacHistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicMacHistoryEntry.setStatus("current")
_CucsVnicMacHistoryInstanceId_Type = CucsManagedObjectId
_CucsVnicMacHistoryInstanceId_Object = MibTableColumn
cucsVnicMacHistoryInstanceId = _CucsVnicMacHistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 62, 1, 1),
    _CucsVnicMacHistoryInstanceId_Type()
)
cucsVnicMacHistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicMacHistoryInstanceId.setStatus("current")
_CucsVnicMacHistoryDn_Type = CucsManagedObjectDn
_CucsVnicMacHistoryDn_Object = MibTableColumn
cucsVnicMacHistoryDn = _CucsVnicMacHistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 62, 1, 2),
    _CucsVnicMacHistoryDn_Type()
)
cucsVnicMacHistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicMacHistoryDn.setStatus("current")
_CucsVnicMacHistoryRn_Type = SnmpAdminString
_CucsVnicMacHistoryRn_Object = MibTableColumn
cucsVnicMacHistoryRn = _CucsVnicMacHistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 62, 1, 3),
    _CucsVnicMacHistoryRn_Type()
)
cucsVnicMacHistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicMacHistoryRn.setStatus("current")
_CucsVnicMacHistoryOldaddr_Type = MacAddress
_CucsVnicMacHistoryOldaddr_Object = MibTableColumn
cucsVnicMacHistoryOldaddr = _CucsVnicMacHistoryOldaddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 62, 1, 4),
    _CucsVnicMacHistoryOldaddr_Type()
)
cucsVnicMacHistoryOldaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicMacHistoryOldaddr.setStatus("current")
_CucsVnicWwnnHistoryTable_Object = MibTable
cucsVnicWwnnHistoryTable = _CucsVnicWwnnHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 63)
)
if mibBuilder.loadTexts:
    cucsVnicWwnnHistoryTable.setStatus("current")
_CucsVnicWwnnHistoryEntry_Object = MibTableRow
cucsVnicWwnnHistoryEntry = _CucsVnicWwnnHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 63, 1)
)
cucsVnicWwnnHistoryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicWwnnHistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicWwnnHistoryEntry.setStatus("current")
_CucsVnicWwnnHistoryInstanceId_Type = CucsManagedObjectId
_CucsVnicWwnnHistoryInstanceId_Object = MibTableColumn
cucsVnicWwnnHistoryInstanceId = _CucsVnicWwnnHistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 63, 1, 1),
    _CucsVnicWwnnHistoryInstanceId_Type()
)
cucsVnicWwnnHistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicWwnnHistoryInstanceId.setStatus("current")
_CucsVnicWwnnHistoryDn_Type = CucsManagedObjectDn
_CucsVnicWwnnHistoryDn_Object = MibTableColumn
cucsVnicWwnnHistoryDn = _CucsVnicWwnnHistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 63, 1, 2),
    _CucsVnicWwnnHistoryDn_Type()
)
cucsVnicWwnnHistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicWwnnHistoryDn.setStatus("current")
_CucsVnicWwnnHistoryRn_Type = SnmpAdminString
_CucsVnicWwnnHistoryRn_Object = MibTableColumn
cucsVnicWwnnHistoryRn = _CucsVnicWwnnHistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 63, 1, 3),
    _CucsVnicWwnnHistoryRn_Type()
)
cucsVnicWwnnHistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicWwnnHistoryRn.setStatus("current")
_CucsVnicWwnnHistoryOldwwnn_Type = Unsigned64
_CucsVnicWwnnHistoryOldwwnn_Object = MibTableColumn
cucsVnicWwnnHistoryOldwwnn = _CucsVnicWwnnHistoryOldwwnn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 63, 1, 4),
    _CucsVnicWwnnHistoryOldwwnn_Type()
)
cucsVnicWwnnHistoryOldwwnn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicWwnnHistoryOldwwnn.setStatus("current")
_CucsVnicWwpnHistoryTable_Object = MibTable
cucsVnicWwpnHistoryTable = _CucsVnicWwpnHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 64)
)
if mibBuilder.loadTexts:
    cucsVnicWwpnHistoryTable.setStatus("current")
_CucsVnicWwpnHistoryEntry_Object = MibTableRow
cucsVnicWwpnHistoryEntry = _CucsVnicWwpnHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 64, 1)
)
cucsVnicWwpnHistoryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicWwpnHistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicWwpnHistoryEntry.setStatus("current")
_CucsVnicWwpnHistoryInstanceId_Type = CucsManagedObjectId
_CucsVnicWwpnHistoryInstanceId_Object = MibTableColumn
cucsVnicWwpnHistoryInstanceId = _CucsVnicWwpnHistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 64, 1, 1),
    _CucsVnicWwpnHistoryInstanceId_Type()
)
cucsVnicWwpnHistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicWwpnHistoryInstanceId.setStatus("current")
_CucsVnicWwpnHistoryDn_Type = CucsManagedObjectDn
_CucsVnicWwpnHistoryDn_Object = MibTableColumn
cucsVnicWwpnHistoryDn = _CucsVnicWwpnHistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 64, 1, 2),
    _CucsVnicWwpnHistoryDn_Type()
)
cucsVnicWwpnHistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicWwpnHistoryDn.setStatus("current")
_CucsVnicWwpnHistoryRn_Type = SnmpAdminString
_CucsVnicWwpnHistoryRn_Object = MibTableColumn
cucsVnicWwpnHistoryRn = _CucsVnicWwpnHistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 64, 1, 3),
    _CucsVnicWwpnHistoryRn_Type()
)
cucsVnicWwpnHistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicWwpnHistoryRn.setStatus("current")
_CucsVnicWwpnHistoryOldaddr_Type = Unsigned64
_CucsVnicWwpnHistoryOldaddr_Object = MibTableColumn
cucsVnicWwpnHistoryOldaddr = _CucsVnicWwpnHistoryOldaddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 64, 1, 4),
    _CucsVnicWwpnHistoryOldaddr_Type()
)
cucsVnicWwpnHistoryOldaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicWwpnHistoryOldaddr.setStatus("current")
_CucsVnicIpV4MgmtPooledAddrTable_Object = MibTable
cucsVnicIpV4MgmtPooledAddrTable = _CucsVnicIpV4MgmtPooledAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 65)
)
if mibBuilder.loadTexts:
    cucsVnicIpV4MgmtPooledAddrTable.setStatus("current")
_CucsVnicIpV4MgmtPooledAddrEntry_Object = MibTableRow
cucsVnicIpV4MgmtPooledAddrEntry = _CucsVnicIpV4MgmtPooledAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 65, 1)
)
cucsVnicIpV4MgmtPooledAddrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIpV4MgmtPooledAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIpV4MgmtPooledAddrEntry.setStatus("current")
_CucsVnicIpV4MgmtPooledAddrInstanceId_Type = CucsManagedObjectId
_CucsVnicIpV4MgmtPooledAddrInstanceId_Object = MibTableColumn
cucsVnicIpV4MgmtPooledAddrInstanceId = _CucsVnicIpV4MgmtPooledAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 65, 1, 1),
    _CucsVnicIpV4MgmtPooledAddrInstanceId_Type()
)
cucsVnicIpV4MgmtPooledAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIpV4MgmtPooledAddrInstanceId.setStatus("current")
_CucsVnicIpV4MgmtPooledAddrDn_Type = CucsManagedObjectDn
_CucsVnicIpV4MgmtPooledAddrDn_Object = MibTableColumn
cucsVnicIpV4MgmtPooledAddrDn = _CucsVnicIpV4MgmtPooledAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 65, 1, 2),
    _CucsVnicIpV4MgmtPooledAddrDn_Type()
)
cucsVnicIpV4MgmtPooledAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4MgmtPooledAddrDn.setStatus("current")
_CucsVnicIpV4MgmtPooledAddrRn_Type = SnmpAdminString
_CucsVnicIpV4MgmtPooledAddrRn_Object = MibTableColumn
cucsVnicIpV4MgmtPooledAddrRn = _CucsVnicIpV4MgmtPooledAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 65, 1, 3),
    _CucsVnicIpV4MgmtPooledAddrRn_Type()
)
cucsVnicIpV4MgmtPooledAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4MgmtPooledAddrRn.setStatus("current")
_CucsVnicIpV4MgmtPooledAddrAddr_Type = InetAddressIPv4
_CucsVnicIpV4MgmtPooledAddrAddr_Object = MibTableColumn
cucsVnicIpV4MgmtPooledAddrAddr = _CucsVnicIpV4MgmtPooledAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 65, 1, 4),
    _CucsVnicIpV4MgmtPooledAddrAddr_Type()
)
cucsVnicIpV4MgmtPooledAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4MgmtPooledAddrAddr.setStatus("current")
_CucsVnicIpV4MgmtPooledAddrDefGw_Type = InetAddressIPv4
_CucsVnicIpV4MgmtPooledAddrDefGw_Object = MibTableColumn
cucsVnicIpV4MgmtPooledAddrDefGw = _CucsVnicIpV4MgmtPooledAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 65, 1, 5),
    _CucsVnicIpV4MgmtPooledAddrDefGw_Type()
)
cucsVnicIpV4MgmtPooledAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4MgmtPooledAddrDefGw.setStatus("current")
_CucsVnicIpV4MgmtPooledAddrName_Type = SnmpAdminString
_CucsVnicIpV4MgmtPooledAddrName_Object = MibTableColumn
cucsVnicIpV4MgmtPooledAddrName = _CucsVnicIpV4MgmtPooledAddrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 65, 1, 6),
    _CucsVnicIpV4MgmtPooledAddrName_Type()
)
cucsVnicIpV4MgmtPooledAddrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4MgmtPooledAddrName.setStatus("current")
_CucsVnicIpV4MgmtPooledAddrOperName_Type = SnmpAdminString
_CucsVnicIpV4MgmtPooledAddrOperName_Object = MibTableColumn
cucsVnicIpV4MgmtPooledAddrOperName = _CucsVnicIpV4MgmtPooledAddrOperName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 65, 1, 7),
    _CucsVnicIpV4MgmtPooledAddrOperName_Type()
)
cucsVnicIpV4MgmtPooledAddrOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4MgmtPooledAddrOperName.setStatus("current")
_CucsVnicIpV4MgmtPooledAddrSubnet_Type = InetAddressIPv4
_CucsVnicIpV4MgmtPooledAddrSubnet_Object = MibTableColumn
cucsVnicIpV4MgmtPooledAddrSubnet = _CucsVnicIpV4MgmtPooledAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 65, 1, 8),
    _CucsVnicIpV4MgmtPooledAddrSubnet_Type()
)
cucsVnicIpV4MgmtPooledAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4MgmtPooledAddrSubnet.setStatus("current")
_CucsVnicIpV4MgmtPooledAddrPrimDns_Type = InetAddressIPv4
_CucsVnicIpV4MgmtPooledAddrPrimDns_Object = MibTableColumn
cucsVnicIpV4MgmtPooledAddrPrimDns = _CucsVnicIpV4MgmtPooledAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 65, 1, 9),
    _CucsVnicIpV4MgmtPooledAddrPrimDns_Type()
)
cucsVnicIpV4MgmtPooledAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4MgmtPooledAddrPrimDns.setStatus("current")
_CucsVnicIpV4MgmtPooledAddrSecDns_Type = InetAddressIPv4
_CucsVnicIpV4MgmtPooledAddrSecDns_Object = MibTableColumn
cucsVnicIpV4MgmtPooledAddrSecDns = _CucsVnicIpV4MgmtPooledAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 65, 1, 10),
    _CucsVnicIpV4MgmtPooledAddrSecDns_Type()
)
cucsVnicIpV4MgmtPooledAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV4MgmtPooledAddrSecDns.setStatus("current")
_CucsVnicIpV6MgmtPooledAddrTable_Object = MibTable
cucsVnicIpV6MgmtPooledAddrTable = _CucsVnicIpV6MgmtPooledAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 66)
)
if mibBuilder.loadTexts:
    cucsVnicIpV6MgmtPooledAddrTable.setStatus("current")
_CucsVnicIpV6MgmtPooledAddrEntry_Object = MibTableRow
cucsVnicIpV6MgmtPooledAddrEntry = _CucsVnicIpV6MgmtPooledAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 66, 1)
)
cucsVnicIpV6MgmtPooledAddrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIpV6MgmtPooledAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIpV6MgmtPooledAddrEntry.setStatus("current")
_CucsVnicIpV6MgmtPooledAddrInstanceId_Type = CucsManagedObjectId
_CucsVnicIpV6MgmtPooledAddrInstanceId_Object = MibTableColumn
cucsVnicIpV6MgmtPooledAddrInstanceId = _CucsVnicIpV6MgmtPooledAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 66, 1, 1),
    _CucsVnicIpV6MgmtPooledAddrInstanceId_Type()
)
cucsVnicIpV6MgmtPooledAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIpV6MgmtPooledAddrInstanceId.setStatus("current")
_CucsVnicIpV6MgmtPooledAddrDn_Type = CucsManagedObjectDn
_CucsVnicIpV6MgmtPooledAddrDn_Object = MibTableColumn
cucsVnicIpV6MgmtPooledAddrDn = _CucsVnicIpV6MgmtPooledAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 66, 1, 2),
    _CucsVnicIpV6MgmtPooledAddrDn_Type()
)
cucsVnicIpV6MgmtPooledAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6MgmtPooledAddrDn.setStatus("current")
_CucsVnicIpV6MgmtPooledAddrRn_Type = SnmpAdminString
_CucsVnicIpV6MgmtPooledAddrRn_Object = MibTableColumn
cucsVnicIpV6MgmtPooledAddrRn = _CucsVnicIpV6MgmtPooledAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 66, 1, 3),
    _CucsVnicIpV6MgmtPooledAddrRn_Type()
)
cucsVnicIpV6MgmtPooledAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6MgmtPooledAddrRn.setStatus("current")
_CucsVnicIpV6MgmtPooledAddrAddr_Type = InetAddressIPv6
_CucsVnicIpV6MgmtPooledAddrAddr_Object = MibTableColumn
cucsVnicIpV6MgmtPooledAddrAddr = _CucsVnicIpV6MgmtPooledAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 66, 1, 4),
    _CucsVnicIpV6MgmtPooledAddrAddr_Type()
)
cucsVnicIpV6MgmtPooledAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6MgmtPooledAddrAddr.setStatus("current")
_CucsVnicIpV6MgmtPooledAddrDefGw_Type = InetAddressIPv6
_CucsVnicIpV6MgmtPooledAddrDefGw_Object = MibTableColumn
cucsVnicIpV6MgmtPooledAddrDefGw = _CucsVnicIpV6MgmtPooledAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 66, 1, 5),
    _CucsVnicIpV6MgmtPooledAddrDefGw_Type()
)
cucsVnicIpV6MgmtPooledAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6MgmtPooledAddrDefGw.setStatus("current")
_CucsVnicIpV6MgmtPooledAddrName_Type = SnmpAdminString
_CucsVnicIpV6MgmtPooledAddrName_Object = MibTableColumn
cucsVnicIpV6MgmtPooledAddrName = _CucsVnicIpV6MgmtPooledAddrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 66, 1, 6),
    _CucsVnicIpV6MgmtPooledAddrName_Type()
)
cucsVnicIpV6MgmtPooledAddrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6MgmtPooledAddrName.setStatus("current")
_CucsVnicIpV6MgmtPooledAddrOperName_Type = SnmpAdminString
_CucsVnicIpV6MgmtPooledAddrOperName_Object = MibTableColumn
cucsVnicIpV6MgmtPooledAddrOperName = _CucsVnicIpV6MgmtPooledAddrOperName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 66, 1, 7),
    _CucsVnicIpV6MgmtPooledAddrOperName_Type()
)
cucsVnicIpV6MgmtPooledAddrOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6MgmtPooledAddrOperName.setStatus("current")
_CucsVnicIpV6MgmtPooledAddrPrefix_Type = Gauge32
_CucsVnicIpV6MgmtPooledAddrPrefix_Object = MibTableColumn
cucsVnicIpV6MgmtPooledAddrPrefix = _CucsVnicIpV6MgmtPooledAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 66, 1, 8),
    _CucsVnicIpV6MgmtPooledAddrPrefix_Type()
)
cucsVnicIpV6MgmtPooledAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6MgmtPooledAddrPrefix.setStatus("current")
_CucsVnicIpV6MgmtPooledAddrPrimDns_Type = InetAddressIPv6
_CucsVnicIpV6MgmtPooledAddrPrimDns_Object = MibTableColumn
cucsVnicIpV6MgmtPooledAddrPrimDns = _CucsVnicIpV6MgmtPooledAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 66, 1, 9),
    _CucsVnicIpV6MgmtPooledAddrPrimDns_Type()
)
cucsVnicIpV6MgmtPooledAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6MgmtPooledAddrPrimDns.setStatus("current")
_CucsVnicIpV6MgmtPooledAddrSecDns_Type = InetAddressIPv6
_CucsVnicIpV6MgmtPooledAddrSecDns_Object = MibTableColumn
cucsVnicIpV6MgmtPooledAddrSecDns = _CucsVnicIpV6MgmtPooledAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 66, 1, 10),
    _CucsVnicIpV6MgmtPooledAddrSecDns_Type()
)
cucsVnicIpV6MgmtPooledAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6MgmtPooledAddrSecDns.setStatus("current")
_CucsVnicIpV6StaticAddrTable_Object = MibTable
cucsVnicIpV6StaticAddrTable = _CucsVnicIpV6StaticAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 67)
)
if mibBuilder.loadTexts:
    cucsVnicIpV6StaticAddrTable.setStatus("current")
_CucsVnicIpV6StaticAddrEntry_Object = MibTableRow
cucsVnicIpV6StaticAddrEntry = _CucsVnicIpV6StaticAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 67, 1)
)
cucsVnicIpV6StaticAddrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIpV6StaticAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIpV6StaticAddrEntry.setStatus("current")
_CucsVnicIpV6StaticAddrInstanceId_Type = CucsManagedObjectId
_CucsVnicIpV6StaticAddrInstanceId_Object = MibTableColumn
cucsVnicIpV6StaticAddrInstanceId = _CucsVnicIpV6StaticAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 67, 1, 1),
    _CucsVnicIpV6StaticAddrInstanceId_Type()
)
cucsVnicIpV6StaticAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIpV6StaticAddrInstanceId.setStatus("current")
_CucsVnicIpV6StaticAddrDn_Type = CucsManagedObjectDn
_CucsVnicIpV6StaticAddrDn_Object = MibTableColumn
cucsVnicIpV6StaticAddrDn = _CucsVnicIpV6StaticAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 67, 1, 2),
    _CucsVnicIpV6StaticAddrDn_Type()
)
cucsVnicIpV6StaticAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6StaticAddrDn.setStatus("current")
_CucsVnicIpV6StaticAddrRn_Type = SnmpAdminString
_CucsVnicIpV6StaticAddrRn_Object = MibTableColumn
cucsVnicIpV6StaticAddrRn = _CucsVnicIpV6StaticAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 67, 1, 3),
    _CucsVnicIpV6StaticAddrRn_Type()
)
cucsVnicIpV6StaticAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6StaticAddrRn.setStatus("current")
_CucsVnicIpV6StaticAddrAddr_Type = InetAddressIPv6
_CucsVnicIpV6StaticAddrAddr_Object = MibTableColumn
cucsVnicIpV6StaticAddrAddr = _CucsVnicIpV6StaticAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 67, 1, 4),
    _CucsVnicIpV6StaticAddrAddr_Type()
)
cucsVnicIpV6StaticAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6StaticAddrAddr.setStatus("current")
_CucsVnicIpV6StaticAddrDefGw_Type = InetAddressIPv6
_CucsVnicIpV6StaticAddrDefGw_Object = MibTableColumn
cucsVnicIpV6StaticAddrDefGw = _CucsVnicIpV6StaticAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 67, 1, 5),
    _CucsVnicIpV6StaticAddrDefGw_Type()
)
cucsVnicIpV6StaticAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6StaticAddrDefGw.setStatus("current")
_CucsVnicIpV6StaticAddrPrefix_Type = Gauge32
_CucsVnicIpV6StaticAddrPrefix_Object = MibTableColumn
cucsVnicIpV6StaticAddrPrefix = _CucsVnicIpV6StaticAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 67, 1, 6),
    _CucsVnicIpV6StaticAddrPrefix_Type()
)
cucsVnicIpV6StaticAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6StaticAddrPrefix.setStatus("current")
_CucsVnicIpV6StaticAddrPrimDns_Type = InetAddressIPv6
_CucsVnicIpV6StaticAddrPrimDns_Object = MibTableColumn
cucsVnicIpV6StaticAddrPrimDns = _CucsVnicIpV6StaticAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 67, 1, 7),
    _CucsVnicIpV6StaticAddrPrimDns_Type()
)
cucsVnicIpV6StaticAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6StaticAddrPrimDns.setStatus("current")
_CucsVnicIpV6StaticAddrSecDns_Type = InetAddressIPv6
_CucsVnicIpV6StaticAddrSecDns_Object = MibTableColumn
cucsVnicIpV6StaticAddrSecDns = _CucsVnicIpV6StaticAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 67, 1, 8),
    _CucsVnicIpV6StaticAddrSecDns_Type()
)
cucsVnicIpV6StaticAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6StaticAddrSecDns.setStatus("current")
_CucsVnicProfileRefTable_Object = MibTable
cucsVnicProfileRefTable = _CucsVnicProfileRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 68)
)
if mibBuilder.loadTexts:
    cucsVnicProfileRefTable.setStatus("current")
_CucsVnicProfileRefEntry_Object = MibTableRow
cucsVnicProfileRefEntry = _CucsVnicProfileRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 68, 1)
)
cucsVnicProfileRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicProfileRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicProfileRefEntry.setStatus("current")
_CucsVnicProfileRefInstanceId_Type = CucsManagedObjectId
_CucsVnicProfileRefInstanceId_Object = MibTableColumn
cucsVnicProfileRefInstanceId = _CucsVnicProfileRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 68, 1, 1),
    _CucsVnicProfileRefInstanceId_Type()
)
cucsVnicProfileRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicProfileRefInstanceId.setStatus("current")
_CucsVnicProfileRefDn_Type = CucsManagedObjectDn
_CucsVnicProfileRefDn_Object = MibTableColumn
cucsVnicProfileRefDn = _CucsVnicProfileRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 68, 1, 2),
    _CucsVnicProfileRefDn_Type()
)
cucsVnicProfileRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileRefDn.setStatus("current")
_CucsVnicProfileRefRn_Type = SnmpAdminString
_CucsVnicProfileRefRn_Object = MibTableColumn
cucsVnicProfileRefRn = _CucsVnicProfileRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 68, 1, 3),
    _CucsVnicProfileRefRn_Type()
)
cucsVnicProfileRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileRefRn.setStatus("current")
_CucsVnicProfileRefName_Type = SnmpAdminString
_CucsVnicProfileRefName_Object = MibTableColumn
cucsVnicProfileRefName = _CucsVnicProfileRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 68, 1, 4),
    _CucsVnicProfileRefName_Type()
)
cucsVnicProfileRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileRefName.setStatus("current")
_CucsVnicProfileRefSourceDn_Type = SnmpAdminString
_CucsVnicProfileRefSourceDn_Object = MibTableColumn
cucsVnicProfileRefSourceDn = _CucsVnicProfileRefSourceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 68, 1, 5),
    _CucsVnicProfileRefSourceDn_Type()
)
cucsVnicProfileRefSourceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicProfileRefSourceDn.setStatus("current")
_CucsVnicUsnicConPolicyTable_Object = MibTable
cucsVnicUsnicConPolicyTable = _CucsVnicUsnicConPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 69)
)
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyTable.setStatus("current")
_CucsVnicUsnicConPolicyEntry_Object = MibTableRow
cucsVnicUsnicConPolicyEntry = _CucsVnicUsnicConPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 69, 1)
)
cucsVnicUsnicConPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicUsnicConPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyEntry.setStatus("current")
_CucsVnicUsnicConPolicyInstanceId_Type = CucsManagedObjectId
_CucsVnicUsnicConPolicyInstanceId_Object = MibTableColumn
cucsVnicUsnicConPolicyInstanceId = _CucsVnicUsnicConPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 69, 1, 1),
    _CucsVnicUsnicConPolicyInstanceId_Type()
)
cucsVnicUsnicConPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyInstanceId.setStatus("current")
_CucsVnicUsnicConPolicyDn_Type = CucsManagedObjectDn
_CucsVnicUsnicConPolicyDn_Object = MibTableColumn
cucsVnicUsnicConPolicyDn = _CucsVnicUsnicConPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 69, 1, 2),
    _CucsVnicUsnicConPolicyDn_Type()
)
cucsVnicUsnicConPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyDn.setStatus("current")
_CucsVnicUsnicConPolicyRn_Type = SnmpAdminString
_CucsVnicUsnicConPolicyRn_Object = MibTableColumn
cucsVnicUsnicConPolicyRn = _CucsVnicUsnicConPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 69, 1, 3),
    _CucsVnicUsnicConPolicyRn_Type()
)
cucsVnicUsnicConPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyRn.setStatus("current")
_CucsVnicUsnicConPolicyAdaptorProfileName_Type = SnmpAdminString
_CucsVnicUsnicConPolicyAdaptorProfileName_Object = MibTableColumn
cucsVnicUsnicConPolicyAdaptorProfileName = _CucsVnicUsnicConPolicyAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 69, 1, 4),
    _CucsVnicUsnicConPolicyAdaptorProfileName_Type()
)
cucsVnicUsnicConPolicyAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyAdaptorProfileName.setStatus("current")
_CucsVnicUsnicConPolicyDescr_Type = SnmpAdminString
_CucsVnicUsnicConPolicyDescr_Object = MibTableColumn
cucsVnicUsnicConPolicyDescr = _CucsVnicUsnicConPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 69, 1, 5),
    _CucsVnicUsnicConPolicyDescr_Type()
)
cucsVnicUsnicConPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyDescr.setStatus("current")
_CucsVnicUsnicConPolicyIntId_Type = SnmpAdminString
_CucsVnicUsnicConPolicyIntId_Object = MibTableColumn
cucsVnicUsnicConPolicyIntId = _CucsVnicUsnicConPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 69, 1, 6),
    _CucsVnicUsnicConPolicyIntId_Type()
)
cucsVnicUsnicConPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyIntId.setStatus("current")
_CucsVnicUsnicConPolicyName_Type = SnmpAdminString
_CucsVnicUsnicConPolicyName_Object = MibTableColumn
cucsVnicUsnicConPolicyName = _CucsVnicUsnicConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 69, 1, 7),
    _CucsVnicUsnicConPolicyName_Type()
)
cucsVnicUsnicConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyName.setStatus("current")
_CucsVnicUsnicConPolicyPolicyLevel_Type = Gauge32
_CucsVnicUsnicConPolicyPolicyLevel_Object = MibTableColumn
cucsVnicUsnicConPolicyPolicyLevel = _CucsVnicUsnicConPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 69, 1, 8),
    _CucsVnicUsnicConPolicyPolicyLevel_Type()
)
cucsVnicUsnicConPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyPolicyLevel.setStatus("current")
_CucsVnicUsnicConPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicUsnicConPolicyPolicyOwner_Object = MibTableColumn
cucsVnicUsnicConPolicyPolicyOwner = _CucsVnicUsnicConPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 69, 1, 9),
    _CucsVnicUsnicConPolicyPolicyOwner_Type()
)
cucsVnicUsnicConPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyPolicyOwner.setStatus("current")
_CucsVnicUsnicConPolicyUsnicCount_Type = Gauge32
_CucsVnicUsnicConPolicyUsnicCount_Object = MibTableColumn
cucsVnicUsnicConPolicyUsnicCount = _CucsVnicUsnicConPolicyUsnicCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 69, 1, 10),
    _CucsVnicUsnicConPolicyUsnicCount_Type()
)
cucsVnicUsnicConPolicyUsnicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyUsnicCount.setStatus("current")
_CucsVnicUsnicConPolicyRefTable_Object = MibTable
cucsVnicUsnicConPolicyRefTable = _CucsVnicUsnicConPolicyRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 70)
)
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyRefTable.setStatus("current")
_CucsVnicUsnicConPolicyRefEntry_Object = MibTableRow
cucsVnicUsnicConPolicyRefEntry = _CucsVnicUsnicConPolicyRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 70, 1)
)
cucsVnicUsnicConPolicyRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicUsnicConPolicyRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyRefEntry.setStatus("current")
_CucsVnicUsnicConPolicyRefInstanceId_Type = CucsManagedObjectId
_CucsVnicUsnicConPolicyRefInstanceId_Object = MibTableColumn
cucsVnicUsnicConPolicyRefInstanceId = _CucsVnicUsnicConPolicyRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 70, 1, 1),
    _CucsVnicUsnicConPolicyRefInstanceId_Type()
)
cucsVnicUsnicConPolicyRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyRefInstanceId.setStatus("current")
_CucsVnicUsnicConPolicyRefDn_Type = CucsManagedObjectDn
_CucsVnicUsnicConPolicyRefDn_Object = MibTableColumn
cucsVnicUsnicConPolicyRefDn = _CucsVnicUsnicConPolicyRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 70, 1, 2),
    _CucsVnicUsnicConPolicyRefDn_Type()
)
cucsVnicUsnicConPolicyRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyRefDn.setStatus("current")
_CucsVnicUsnicConPolicyRefRn_Type = SnmpAdminString
_CucsVnicUsnicConPolicyRefRn_Object = MibTableColumn
cucsVnicUsnicConPolicyRefRn = _CucsVnicUsnicConPolicyRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 70, 1, 3),
    _CucsVnicUsnicConPolicyRefRn_Type()
)
cucsVnicUsnicConPolicyRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyRefRn.setStatus("current")
_CucsVnicUsnicConPolicyRefConPolicyName_Type = SnmpAdminString
_CucsVnicUsnicConPolicyRefConPolicyName_Object = MibTableColumn
cucsVnicUsnicConPolicyRefConPolicyName = _CucsVnicUsnicConPolicyRefConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 70, 1, 4),
    _CucsVnicUsnicConPolicyRefConPolicyName_Type()
)
cucsVnicUsnicConPolicyRefConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyRefConPolicyName.setStatus("current")
_CucsVnicUsnicConPolicyRefOperConPolicyName_Type = SnmpAdminString
_CucsVnicUsnicConPolicyRefOperConPolicyName_Object = MibTableColumn
cucsVnicUsnicConPolicyRefOperConPolicyName = _CucsVnicUsnicConPolicyRefOperConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 70, 1, 5),
    _CucsVnicUsnicConPolicyRefOperConPolicyName_Type()
)
cucsVnicUsnicConPolicyRefOperConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicUsnicConPolicyRefOperConPolicyName.setStatus("current")
_CucsVnicVmqConPolicyTable_Object = MibTable
cucsVnicVmqConPolicyTable = _CucsVnicVmqConPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 71)
)
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyTable.setStatus("current")
_CucsVnicVmqConPolicyEntry_Object = MibTableRow
cucsVnicVmqConPolicyEntry = _CucsVnicVmqConPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 71, 1)
)
cucsVnicVmqConPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicVmqConPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyEntry.setStatus("current")
_CucsVnicVmqConPolicyInstanceId_Type = CucsManagedObjectId
_CucsVnicVmqConPolicyInstanceId_Object = MibTableColumn
cucsVnicVmqConPolicyInstanceId = _CucsVnicVmqConPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 71, 1, 1),
    _CucsVnicVmqConPolicyInstanceId_Type()
)
cucsVnicVmqConPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyInstanceId.setStatus("current")
_CucsVnicVmqConPolicyDn_Type = CucsManagedObjectDn
_CucsVnicVmqConPolicyDn_Object = MibTableColumn
cucsVnicVmqConPolicyDn = _CucsVnicVmqConPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 71, 1, 2),
    _CucsVnicVmqConPolicyDn_Type()
)
cucsVnicVmqConPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyDn.setStatus("current")
_CucsVnicVmqConPolicyRn_Type = SnmpAdminString
_CucsVnicVmqConPolicyRn_Object = MibTableColumn
cucsVnicVmqConPolicyRn = _CucsVnicVmqConPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 71, 1, 3),
    _CucsVnicVmqConPolicyRn_Type()
)
cucsVnicVmqConPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyRn.setStatus("current")
_CucsVnicVmqConPolicyDescr_Type = SnmpAdminString
_CucsVnicVmqConPolicyDescr_Object = MibTableColumn
cucsVnicVmqConPolicyDescr = _CucsVnicVmqConPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 71, 1, 4),
    _CucsVnicVmqConPolicyDescr_Type()
)
cucsVnicVmqConPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyDescr.setStatus("current")
_CucsVnicVmqConPolicyIntId_Type = SnmpAdminString
_CucsVnicVmqConPolicyIntId_Object = MibTableColumn
cucsVnicVmqConPolicyIntId = _CucsVnicVmqConPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 71, 1, 5),
    _CucsVnicVmqConPolicyIntId_Type()
)
cucsVnicVmqConPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyIntId.setStatus("current")
_CucsVnicVmqConPolicyIntrCount_Type = Gauge32
_CucsVnicVmqConPolicyIntrCount_Object = MibTableColumn
cucsVnicVmqConPolicyIntrCount = _CucsVnicVmqConPolicyIntrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 71, 1, 6),
    _CucsVnicVmqConPolicyIntrCount_Type()
)
cucsVnicVmqConPolicyIntrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyIntrCount.setStatus("current")
_CucsVnicVmqConPolicyName_Type = SnmpAdminString
_CucsVnicVmqConPolicyName_Object = MibTableColumn
cucsVnicVmqConPolicyName = _CucsVnicVmqConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 71, 1, 7),
    _CucsVnicVmqConPolicyName_Type()
)
cucsVnicVmqConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyName.setStatus("current")
_CucsVnicVmqConPolicyPolicyLevel_Type = Gauge32
_CucsVnicVmqConPolicyPolicyLevel_Object = MibTableColumn
cucsVnicVmqConPolicyPolicyLevel = _CucsVnicVmqConPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 71, 1, 8),
    _CucsVnicVmqConPolicyPolicyLevel_Type()
)
cucsVnicVmqConPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyPolicyLevel.setStatus("current")
_CucsVnicVmqConPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicVmqConPolicyPolicyOwner_Object = MibTableColumn
cucsVnicVmqConPolicyPolicyOwner = _CucsVnicVmqConPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 71, 1, 9),
    _CucsVnicVmqConPolicyPolicyOwner_Type()
)
cucsVnicVmqConPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyPolicyOwner.setStatus("current")
_CucsVnicVmqConPolicyVmqCount_Type = Gauge32
_CucsVnicVmqConPolicyVmqCount_Object = MibTableColumn
cucsVnicVmqConPolicyVmqCount = _CucsVnicVmqConPolicyVmqCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 71, 1, 10),
    _CucsVnicVmqConPolicyVmqCount_Type()
)
cucsVnicVmqConPolicyVmqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyVmqCount.setStatus("current")
_CucsVnicVmqConPolicyRefTable_Object = MibTable
cucsVnicVmqConPolicyRefTable = _CucsVnicVmqConPolicyRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 72)
)
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyRefTable.setStatus("current")
_CucsVnicVmqConPolicyRefEntry_Object = MibTableRow
cucsVnicVmqConPolicyRefEntry = _CucsVnicVmqConPolicyRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 72, 1)
)
cucsVnicVmqConPolicyRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicVmqConPolicyRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyRefEntry.setStatus("current")
_CucsVnicVmqConPolicyRefInstanceId_Type = CucsManagedObjectId
_CucsVnicVmqConPolicyRefInstanceId_Object = MibTableColumn
cucsVnicVmqConPolicyRefInstanceId = _CucsVnicVmqConPolicyRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 72, 1, 1),
    _CucsVnicVmqConPolicyRefInstanceId_Type()
)
cucsVnicVmqConPolicyRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyRefInstanceId.setStatus("current")
_CucsVnicVmqConPolicyRefDn_Type = CucsManagedObjectDn
_CucsVnicVmqConPolicyRefDn_Object = MibTableColumn
cucsVnicVmqConPolicyRefDn = _CucsVnicVmqConPolicyRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 72, 1, 2),
    _CucsVnicVmqConPolicyRefDn_Type()
)
cucsVnicVmqConPolicyRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyRefDn.setStatus("current")
_CucsVnicVmqConPolicyRefRn_Type = SnmpAdminString
_CucsVnicVmqConPolicyRefRn_Object = MibTableColumn
cucsVnicVmqConPolicyRefRn = _CucsVnicVmqConPolicyRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 72, 1, 3),
    _CucsVnicVmqConPolicyRefRn_Type()
)
cucsVnicVmqConPolicyRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyRefRn.setStatus("current")
_CucsVnicVmqConPolicyRefConPolicyName_Type = SnmpAdminString
_CucsVnicVmqConPolicyRefConPolicyName_Object = MibTableColumn
cucsVnicVmqConPolicyRefConPolicyName = _CucsVnicVmqConPolicyRefConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 72, 1, 4),
    _CucsVnicVmqConPolicyRefConPolicyName_Type()
)
cucsVnicVmqConPolicyRefConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyRefConPolicyName.setStatus("current")
_CucsVnicVmqConPolicyRefOperConPolicyName_Type = SnmpAdminString
_CucsVnicVmqConPolicyRefOperConPolicyName_Object = MibTableColumn
cucsVnicVmqConPolicyRefOperConPolicyName = _CucsVnicVmqConPolicyRefOperConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 72, 1, 5),
    _CucsVnicVmqConPolicyRefOperConPolicyName_Type()
)
cucsVnicVmqConPolicyRefOperConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicVmqConPolicyRefOperConPolicyName.setStatus("current")
_CucsVnicIpV6HistoryTable_Object = MibTable
cucsVnicIpV6HistoryTable = _CucsVnicIpV6HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 73)
)
if mibBuilder.loadTexts:
    cucsVnicIpV6HistoryTable.setStatus("current")
_CucsVnicIpV6HistoryEntry_Object = MibTableRow
cucsVnicIpV6HistoryEntry = _CucsVnicIpV6HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 73, 1)
)
cucsVnicIpV6HistoryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIpV6HistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIpV6HistoryEntry.setStatus("current")
_CucsVnicIpV6HistoryInstanceId_Type = CucsManagedObjectId
_CucsVnicIpV6HistoryInstanceId_Object = MibTableColumn
cucsVnicIpV6HistoryInstanceId = _CucsVnicIpV6HistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 73, 1, 1),
    _CucsVnicIpV6HistoryInstanceId_Type()
)
cucsVnicIpV6HistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIpV6HistoryInstanceId.setStatus("current")
_CucsVnicIpV6HistoryDn_Type = CucsManagedObjectDn
_CucsVnicIpV6HistoryDn_Object = MibTableColumn
cucsVnicIpV6HistoryDn = _CucsVnicIpV6HistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 73, 1, 2),
    _CucsVnicIpV6HistoryDn_Type()
)
cucsVnicIpV6HistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6HistoryDn.setStatus("current")
_CucsVnicIpV6HistoryRn_Type = SnmpAdminString
_CucsVnicIpV6HistoryRn_Object = MibTableColumn
cucsVnicIpV6HistoryRn = _CucsVnicIpV6HistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 73, 1, 3),
    _CucsVnicIpV6HistoryRn_Type()
)
cucsVnicIpV6HistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6HistoryRn.setStatus("current")
_CucsVnicIpV6HistoryOldIpV6Addr_Type = InetAddressIPv6
_CucsVnicIpV6HistoryOldIpV6Addr_Object = MibTableColumn
cucsVnicIpV6HistoryOldIpV6Addr = _CucsVnicIpV6HistoryOldIpV6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 73, 1, 4),
    _CucsVnicIpV6HistoryOldIpV6Addr_Type()
)
cucsVnicIpV6HistoryOldIpV6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIpV6HistoryOldIpV6Addr.setStatus("current")
_CucsVnicEthConfigTable_Object = MibTable
cucsVnicEthConfigTable = _CucsVnicEthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 74)
)
if mibBuilder.loadTexts:
    cucsVnicEthConfigTable.setStatus("current")
_CucsVnicEthConfigEntry_Object = MibTableRow
cucsVnicEthConfigEntry = _CucsVnicEthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 74, 1)
)
cucsVnicEthConfigEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicEthConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicEthConfigEntry.setStatus("current")
_CucsVnicEthConfigInstanceId_Type = CucsManagedObjectId
_CucsVnicEthConfigInstanceId_Object = MibTableColumn
cucsVnicEthConfigInstanceId = _CucsVnicEthConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 74, 1, 1),
    _CucsVnicEthConfigInstanceId_Type()
)
cucsVnicEthConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicEthConfigInstanceId.setStatus("current")
_CucsVnicEthConfigDn_Type = CucsManagedObjectDn
_CucsVnicEthConfigDn_Object = MibTableColumn
cucsVnicEthConfigDn = _CucsVnicEthConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 74, 1, 2),
    _CucsVnicEthConfigDn_Type()
)
cucsVnicEthConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthConfigDn.setStatus("current")
_CucsVnicEthConfigRn_Type = SnmpAdminString
_CucsVnicEthConfigRn_Object = MibTableColumn
cucsVnicEthConfigRn = _CucsVnicEthConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 74, 1, 3),
    _CucsVnicEthConfigRn_Type()
)
cucsVnicEthConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthConfigRn.setStatus("current")
_CucsVnicEthConfigAdaptorProfileName_Type = SnmpAdminString
_CucsVnicEthConfigAdaptorProfileName_Object = MibTableColumn
cucsVnicEthConfigAdaptorProfileName = _CucsVnicEthConfigAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 74, 1, 4),
    _CucsVnicEthConfigAdaptorProfileName_Type()
)
cucsVnicEthConfigAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthConfigAdaptorProfileName.setStatus("current")
_CucsVnicEthConfigMacPoolName_Type = SnmpAdminString
_CucsVnicEthConfigMacPoolName_Object = MibTableColumn
cucsVnicEthConfigMacPoolName = _CucsVnicEthConfigMacPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 74, 1, 5),
    _CucsVnicEthConfigMacPoolName_Type()
)
cucsVnicEthConfigMacPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthConfigMacPoolName.setStatus("current")
_CucsVnicEthConfigNwCtrlPolicyName_Type = SnmpAdminString
_CucsVnicEthConfigNwCtrlPolicyName_Object = MibTableColumn
cucsVnicEthConfigNwCtrlPolicyName = _CucsVnicEthConfigNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 74, 1, 6),
    _CucsVnicEthConfigNwCtrlPolicyName_Type()
)
cucsVnicEthConfigNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthConfigNwCtrlPolicyName.setStatus("current")
_CucsVnicEthConfigOperAdaptorProfileName_Type = SnmpAdminString
_CucsVnicEthConfigOperAdaptorProfileName_Object = MibTableColumn
cucsVnicEthConfigOperAdaptorProfileName = _CucsVnicEthConfigOperAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 74, 1, 7),
    _CucsVnicEthConfigOperAdaptorProfileName_Type()
)
cucsVnicEthConfigOperAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthConfigOperAdaptorProfileName.setStatus("current")
_CucsVnicEthConfigOperMacPoolName_Type = SnmpAdminString
_CucsVnicEthConfigOperMacPoolName_Object = MibTableColumn
cucsVnicEthConfigOperMacPoolName = _CucsVnicEthConfigOperMacPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 74, 1, 8),
    _CucsVnicEthConfigOperMacPoolName_Type()
)
cucsVnicEthConfigOperMacPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthConfigOperMacPoolName.setStatus("current")
_CucsVnicEthConfigOperNwCtrlPolicyName_Type = SnmpAdminString
_CucsVnicEthConfigOperNwCtrlPolicyName_Object = MibTableColumn
cucsVnicEthConfigOperNwCtrlPolicyName = _CucsVnicEthConfigOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 74, 1, 9),
    _CucsVnicEthConfigOperNwCtrlPolicyName_Type()
)
cucsVnicEthConfigOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthConfigOperNwCtrlPolicyName.setStatus("current")
_CucsVnicEthConfigOperStatsPolicyName_Type = SnmpAdminString
_CucsVnicEthConfigOperStatsPolicyName_Object = MibTableColumn
cucsVnicEthConfigOperStatsPolicyName = _CucsVnicEthConfigOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 74, 1, 10),
    _CucsVnicEthConfigOperStatsPolicyName_Type()
)
cucsVnicEthConfigOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthConfigOperStatsPolicyName.setStatus("current")
_CucsVnicEthConfigStatsPolicyName_Type = SnmpAdminString
_CucsVnicEthConfigStatsPolicyName_Object = MibTableColumn
cucsVnicEthConfigStatsPolicyName = _CucsVnicEthConfigStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 74, 1, 11),
    _CucsVnicEthConfigStatsPolicyName_Type()
)
cucsVnicEthConfigStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicEthConfigStatsPolicyName.setStatus("current")
_CucsVnicIPv6IfTable_Object = MibTable
cucsVnicIPv6IfTable = _CucsVnicIPv6IfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75)
)
if mibBuilder.loadTexts:
    cucsVnicIPv6IfTable.setStatus("current")
_CucsVnicIPv6IfEntry_Object = MibTableRow
cucsVnicIPv6IfEntry = _CucsVnicIPv6IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1)
)
cucsVnicIPv6IfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIPv6IfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIPv6IfEntry.setStatus("current")
_CucsVnicIPv6IfInstanceId_Type = CucsManagedObjectId
_CucsVnicIPv6IfInstanceId_Object = MibTableColumn
cucsVnicIPv6IfInstanceId = _CucsVnicIPv6IfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1, 1),
    _CucsVnicIPv6IfInstanceId_Type()
)
cucsVnicIPv6IfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIPv6IfInstanceId.setStatus("current")
_CucsVnicIPv6IfDn_Type = CucsManagedObjectDn
_CucsVnicIPv6IfDn_Object = MibTableColumn
cucsVnicIPv6IfDn = _CucsVnicIPv6IfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1, 2),
    _CucsVnicIPv6IfDn_Type()
)
cucsVnicIPv6IfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv6IfDn.setStatus("current")
_CucsVnicIPv6IfRn_Type = SnmpAdminString
_CucsVnicIPv6IfRn_Object = MibTableColumn
cucsVnicIPv6IfRn = _CucsVnicIPv6IfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1, 3),
    _CucsVnicIPv6IfRn_Type()
)
cucsVnicIPv6IfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv6IfRn.setStatus("current")
_CucsVnicIPv6IfAddr_Type = InetAddressIPv6
_CucsVnicIPv6IfAddr_Object = MibTableColumn
cucsVnicIPv6IfAddr = _CucsVnicIPv6IfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1, 4),
    _CucsVnicIPv6IfAddr_Type()
)
cucsVnicIPv6IfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv6IfAddr.setStatus("current")
_CucsVnicIPv6IfConfigQualifier_Type = CucsVnicConfigIssues
_CucsVnicIPv6IfConfigQualifier_Object = MibTableColumn
cucsVnicIPv6IfConfigQualifier = _CucsVnicIPv6IfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1, 5),
    _CucsVnicIPv6IfConfigQualifier_Type()
)
cucsVnicIPv6IfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv6IfConfigQualifier.setStatus("current")
_CucsVnicIPv6IfName_Type = SnmpAdminString
_CucsVnicIPv6IfName_Object = MibTableColumn
cucsVnicIPv6IfName = _CucsVnicIPv6IfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1, 6),
    _CucsVnicIPv6IfName_Type()
)
cucsVnicIPv6IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv6IfName.setStatus("current")
_CucsVnicIPv6IfOperState_Type = CucsVnicIfOperState
_CucsVnicIPv6IfOperState_Object = MibTableColumn
cucsVnicIPv6IfOperState = _CucsVnicIPv6IfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1, 7),
    _CucsVnicIPv6IfOperState_Type()
)
cucsVnicIPv6IfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv6IfOperState.setStatus("current")
_CucsVnicIPv6IfOperVnetDn_Type = SnmpAdminString
_CucsVnicIPv6IfOperVnetDn_Object = MibTableColumn
cucsVnicIPv6IfOperVnetDn = _CucsVnicIPv6IfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1, 8),
    _CucsVnicIPv6IfOperVnetDn_Type()
)
cucsVnicIPv6IfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv6IfOperVnetDn.setStatus("current")
_CucsVnicIPv6IfOperVnetName_Type = SnmpAdminString
_CucsVnicIPv6IfOperVnetName_Object = MibTableColumn
cucsVnicIPv6IfOperVnetName = _CucsVnicIPv6IfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1, 9),
    _CucsVnicIPv6IfOperVnetName_Type()
)
cucsVnicIPv6IfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv6IfOperVnetName.setStatus("current")
_CucsVnicIPv6IfOwner_Type = CucsVnicConnectionOwner
_CucsVnicIPv6IfOwner_Object = MibTableColumn
cucsVnicIPv6IfOwner = _CucsVnicIPv6IfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1, 10),
    _CucsVnicIPv6IfOwner_Type()
)
cucsVnicIPv6IfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv6IfOwner.setStatus("current")
_CucsVnicIPv6IfPubNwId_Type = Gauge32
_CucsVnicIPv6IfPubNwId_Object = MibTableColumn
cucsVnicIPv6IfPubNwId = _CucsVnicIPv6IfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1, 11),
    _CucsVnicIPv6IfPubNwId_Type()
)
cucsVnicIPv6IfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv6IfPubNwId.setStatus("current")
_CucsVnicIPv6IfSharing_Type = CucsFabricVlanSharingType
_CucsVnicIPv6IfSharing_Object = MibTableColumn
cucsVnicIPv6IfSharing = _CucsVnicIPv6IfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1, 12),
    _CucsVnicIPv6IfSharing_Type()
)
cucsVnicIPv6IfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv6IfSharing.setStatus("current")
_CucsVnicIPv6IfSwitchId_Type = CucsNetworkSwitchId
_CucsVnicIPv6IfSwitchId_Object = MibTableColumn
cucsVnicIPv6IfSwitchId = _CucsVnicIPv6IfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1, 13),
    _CucsVnicIPv6IfSwitchId_Type()
)
cucsVnicIPv6IfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv6IfSwitchId.setStatus("current")
_CucsVnicIPv6IfType_Type = CucsVnicConnectionType
_CucsVnicIPv6IfType_Object = MibTableColumn
cucsVnicIPv6IfType = _CucsVnicIPv6IfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1, 14),
    _CucsVnicIPv6IfType_Type()
)
cucsVnicIPv6IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv6IfType.setStatus("current")
_CucsVnicIPv6IfVnet_Type = Gauge32
_CucsVnicIPv6IfVnet_Object = MibTableColumn
cucsVnicIPv6IfVnet = _CucsVnicIPv6IfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1, 15),
    _CucsVnicIPv6IfVnet_Type()
)
cucsVnicIPv6IfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv6IfVnet.setStatus("current")
_CucsVnicIPv6IfOperPrimaryVnetDn_Type = SnmpAdminString
_CucsVnicIPv6IfOperPrimaryVnetDn_Object = MibTableColumn
cucsVnicIPv6IfOperPrimaryVnetDn = _CucsVnicIPv6IfOperPrimaryVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1, 16),
    _CucsVnicIPv6IfOperPrimaryVnetDn_Type()
)
cucsVnicIPv6IfOperPrimaryVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv6IfOperPrimaryVnetDn.setStatus("current")
_CucsVnicIPv6IfOperPrimaryVnetName_Type = SnmpAdminString
_CucsVnicIPv6IfOperPrimaryVnetName_Object = MibTableColumn
cucsVnicIPv6IfOperPrimaryVnetName = _CucsVnicIPv6IfOperPrimaryVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 75, 1, 17),
    _CucsVnicIPv6IfOperPrimaryVnetName_Type()
)
cucsVnicIPv6IfOperPrimaryVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIPv6IfOperPrimaryVnetName.setStatus("current")
_CucsVnicIScsiConfigTable_Object = MibTable
cucsVnicIScsiConfigTable = _CucsVnicIScsiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 76)
)
if mibBuilder.loadTexts:
    cucsVnicIScsiConfigTable.setStatus("current")
_CucsVnicIScsiConfigEntry_Object = MibTableRow
cucsVnicIScsiConfigEntry = _CucsVnicIScsiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 76, 1)
)
cucsVnicIScsiConfigEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIScsiConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIScsiConfigEntry.setStatus("current")
_CucsVnicIScsiConfigInstanceId_Type = CucsManagedObjectId
_CucsVnicIScsiConfigInstanceId_Object = MibTableColumn
cucsVnicIScsiConfigInstanceId = _CucsVnicIScsiConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 76, 1, 1),
    _CucsVnicIScsiConfigInstanceId_Type()
)
cucsVnicIScsiConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIScsiConfigInstanceId.setStatus("current")
_CucsVnicIScsiConfigDn_Type = CucsManagedObjectDn
_CucsVnicIScsiConfigDn_Object = MibTableColumn
cucsVnicIScsiConfigDn = _CucsVnicIScsiConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 76, 1, 2),
    _CucsVnicIScsiConfigDn_Type()
)
cucsVnicIScsiConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiConfigDn.setStatus("current")
_CucsVnicIScsiConfigRn_Type = SnmpAdminString
_CucsVnicIScsiConfigRn_Object = MibTableColumn
cucsVnicIScsiConfigRn = _CucsVnicIScsiConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 76, 1, 3),
    _CucsVnicIScsiConfigRn_Type()
)
cucsVnicIScsiConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiConfigRn.setStatus("current")
_CucsVnicIScsiConfigAdaptorProfileName_Type = SnmpAdminString
_CucsVnicIScsiConfigAdaptorProfileName_Object = MibTableColumn
cucsVnicIScsiConfigAdaptorProfileName = _CucsVnicIScsiConfigAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 76, 1, 4),
    _CucsVnicIScsiConfigAdaptorProfileName_Type()
)
cucsVnicIScsiConfigAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiConfigAdaptorProfileName.setStatus("current")
_CucsVnicIScsiConfigIpPoolName_Type = SnmpAdminString
_CucsVnicIScsiConfigIpPoolName_Object = MibTableColumn
cucsVnicIScsiConfigIpPoolName = _CucsVnicIScsiConfigIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 76, 1, 5),
    _CucsVnicIScsiConfigIpPoolName_Type()
)
cucsVnicIScsiConfigIpPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiConfigIpPoolName.setStatus("current")
_CucsVnicIScsiConfigIpPoolNameFabricB_Type = SnmpAdminString
_CucsVnicIScsiConfigIpPoolNameFabricB_Object = MibTableColumn
cucsVnicIScsiConfigIpPoolNameFabricB = _CucsVnicIScsiConfigIpPoolNameFabricB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 76, 1, 6),
    _CucsVnicIScsiConfigIpPoolNameFabricB_Type()
)
cucsVnicIScsiConfigIpPoolNameFabricB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiConfigIpPoolNameFabricB.setStatus("current")
_CucsVnicIScsiConfigIpPoolType_Type = CucsVnicIpPoolType
_CucsVnicIScsiConfigIpPoolType_Object = MibTableColumn
cucsVnicIScsiConfigIpPoolType = _CucsVnicIScsiConfigIpPoolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 76, 1, 7),
    _CucsVnicIScsiConfigIpPoolType_Type()
)
cucsVnicIScsiConfigIpPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiConfigIpPoolType.setStatus("current")
_CucsVnicIScsiConfigIqnPoolName_Type = SnmpAdminString
_CucsVnicIScsiConfigIqnPoolName_Object = MibTableColumn
cucsVnicIScsiConfigIqnPoolName = _CucsVnicIScsiConfigIqnPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 76, 1, 8),
    _CucsVnicIScsiConfigIqnPoolName_Type()
)
cucsVnicIScsiConfigIqnPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiConfigIqnPoolName.setStatus("current")
_CucsVnicIScsiConfigOperAdaptorProfileName_Type = SnmpAdminString
_CucsVnicIScsiConfigOperAdaptorProfileName_Object = MibTableColumn
cucsVnicIScsiConfigOperAdaptorProfileName = _CucsVnicIScsiConfigOperAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 76, 1, 9),
    _CucsVnicIScsiConfigOperAdaptorProfileName_Type()
)
cucsVnicIScsiConfigOperAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiConfigOperAdaptorProfileName.setStatus("current")
_CucsVnicIScsiConfigOperIpPoolName_Type = SnmpAdminString
_CucsVnicIScsiConfigOperIpPoolName_Object = MibTableColumn
cucsVnicIScsiConfigOperIpPoolName = _CucsVnicIScsiConfigOperIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 76, 1, 10),
    _CucsVnicIScsiConfigOperIpPoolName_Type()
)
cucsVnicIScsiConfigOperIpPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiConfigOperIpPoolName.setStatus("current")
_CucsVnicIScsiConfigOperIpPoolNameFabricB_Type = SnmpAdminString
_CucsVnicIScsiConfigOperIpPoolNameFabricB_Object = MibTableColumn
cucsVnicIScsiConfigOperIpPoolNameFabricB = _CucsVnicIScsiConfigOperIpPoolNameFabricB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 76, 1, 11),
    _CucsVnicIScsiConfigOperIpPoolNameFabricB_Type()
)
cucsVnicIScsiConfigOperIpPoolNameFabricB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiConfigOperIpPoolNameFabricB.setStatus("current")
_CucsVnicIScsiConfigOperIqnPoolName_Type = SnmpAdminString
_CucsVnicIScsiConfigOperIqnPoolName_Object = MibTableColumn
cucsVnicIScsiConfigOperIqnPoolName = _CucsVnicIScsiConfigOperIqnPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 76, 1, 12),
    _CucsVnicIScsiConfigOperIqnPoolName_Type()
)
cucsVnicIScsiConfigOperIqnPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiConfigOperIqnPoolName.setStatus("current")
_CucsVnicIScsiInitAutoConfigPolicyTable_Object = MibTable
cucsVnicIScsiInitAutoConfigPolicyTable = _CucsVnicIScsiInitAutoConfigPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 77)
)
if mibBuilder.loadTexts:
    cucsVnicIScsiInitAutoConfigPolicyTable.setStatus("current")
_CucsVnicIScsiInitAutoConfigPolicyEntry_Object = MibTableRow
cucsVnicIScsiInitAutoConfigPolicyEntry = _CucsVnicIScsiInitAutoConfigPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 77, 1)
)
cucsVnicIScsiInitAutoConfigPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VNIC-MIB", "cucsVnicIScsiInitAutoConfigPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVnicIScsiInitAutoConfigPolicyEntry.setStatus("current")
_CucsVnicIScsiInitAutoConfigPolicyInstanceId_Type = CucsManagedObjectId
_CucsVnicIScsiInitAutoConfigPolicyInstanceId_Object = MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyInstanceId = _CucsVnicIScsiInitAutoConfigPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 77, 1, 1),
    _CucsVnicIScsiInitAutoConfigPolicyInstanceId_Type()
)
cucsVnicIScsiInitAutoConfigPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVnicIScsiInitAutoConfigPolicyInstanceId.setStatus("current")
_CucsVnicIScsiInitAutoConfigPolicyDn_Type = CucsManagedObjectDn
_CucsVnicIScsiInitAutoConfigPolicyDn_Object = MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyDn = _CucsVnicIScsiInitAutoConfigPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 77, 1, 2),
    _CucsVnicIScsiInitAutoConfigPolicyDn_Type()
)
cucsVnicIScsiInitAutoConfigPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiInitAutoConfigPolicyDn.setStatus("current")
_CucsVnicIScsiInitAutoConfigPolicyRn_Type = SnmpAdminString
_CucsVnicIScsiInitAutoConfigPolicyRn_Object = MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyRn = _CucsVnicIScsiInitAutoConfigPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 77, 1, 3),
    _CucsVnicIScsiInitAutoConfigPolicyRn_Type()
)
cucsVnicIScsiInitAutoConfigPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiInitAutoConfigPolicyRn.setStatus("current")
_CucsVnicIScsiInitAutoConfigPolicyDescr_Type = SnmpAdminString
_CucsVnicIScsiInitAutoConfigPolicyDescr_Object = MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyDescr = _CucsVnicIScsiInitAutoConfigPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 77, 1, 4),
    _CucsVnicIScsiInitAutoConfigPolicyDescr_Type()
)
cucsVnicIScsiInitAutoConfigPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiInitAutoConfigPolicyDescr.setStatus("current")
_CucsVnicIScsiInitAutoConfigPolicyFabricPath_Type = SnmpAdminString
_CucsVnicIScsiInitAutoConfigPolicyFabricPath_Object = MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyFabricPath = _CucsVnicIScsiInitAutoConfigPolicyFabricPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 77, 1, 5),
    _CucsVnicIScsiInitAutoConfigPolicyFabricPath_Type()
)
cucsVnicIScsiInitAutoConfigPolicyFabricPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiInitAutoConfigPolicyFabricPath.setStatus("current")
_CucsVnicIScsiInitAutoConfigPolicyIntId_Type = SnmpAdminString
_CucsVnicIScsiInitAutoConfigPolicyIntId_Object = MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyIntId = _CucsVnicIScsiInitAutoConfigPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 77, 1, 6),
    _CucsVnicIScsiInitAutoConfigPolicyIntId_Type()
)
cucsVnicIScsiInitAutoConfigPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiInitAutoConfigPolicyIntId.setStatus("current")
_CucsVnicIScsiInitAutoConfigPolicyName_Type = SnmpAdminString
_CucsVnicIScsiInitAutoConfigPolicyName_Object = MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyName = _CucsVnicIScsiInitAutoConfigPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 77, 1, 7),
    _CucsVnicIScsiInitAutoConfigPolicyName_Type()
)
cucsVnicIScsiInitAutoConfigPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiInitAutoConfigPolicyName.setStatus("current")
_CucsVnicIScsiInitAutoConfigPolicyPolicyLevel_Type = Gauge32
_CucsVnicIScsiInitAutoConfigPolicyPolicyLevel_Object = MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyPolicyLevel = _CucsVnicIScsiInitAutoConfigPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 77, 1, 8),
    _CucsVnicIScsiInitAutoConfigPolicyPolicyLevel_Type()
)
cucsVnicIScsiInitAutoConfigPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiInitAutoConfigPolicyPolicyLevel.setStatus("current")
_CucsVnicIScsiInitAutoConfigPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsVnicIScsiInitAutoConfigPolicyPolicyOwner_Object = MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyPolicyOwner = _CucsVnicIScsiInitAutoConfigPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 53, 77, 1, 9),
    _CucsVnicIScsiInitAutoConfigPolicyPolicyOwner_Type()
)
cucsVnicIScsiInitAutoConfigPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVnicIScsiInitAutoConfigPolicyPolicyOwner.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-VNIC-MIB",
    **{"cucsVnicObjects": cucsVnicObjects,
       "cucsVnicBootTargetTable": cucsVnicBootTargetTable,
       "cucsVnicBootTargetEntry": cucsVnicBootTargetEntry,
       "cucsVnicBootTargetInstanceId": cucsVnicBootTargetInstanceId,
       "cucsVnicBootTargetDn": cucsVnicBootTargetDn,
       "cucsVnicBootTargetRn": cucsVnicBootTargetRn,
       "cucsVnicBootTargetLun": cucsVnicBootTargetLun,
       "cucsVnicBootTargetWwn": cucsVnicBootTargetWwn,
       "cucsVnicDefBehTable": cucsVnicDefBehTable,
       "cucsVnicDefBehEntry": cucsVnicDefBehEntry,
       "cucsVnicDefBehInstanceId": cucsVnicDefBehInstanceId,
       "cucsVnicDefBehDn": cucsVnicDefBehDn,
       "cucsVnicDefBehRn": cucsVnicDefBehRn,
       "cucsVnicDefBehAction": cucsVnicDefBehAction,
       "cucsVnicDefBehNwTemplName": cucsVnicDefBehNwTemplName,
       "cucsVnicDefBehType": cucsVnicDefBehType,
       "cucsVnicDefBehDescr": cucsVnicDefBehDescr,
       "cucsVnicDefBehIntId": cucsVnicDefBehIntId,
       "cucsVnicDefBehName": cucsVnicDefBehName,
       "cucsVnicDefBehPolicyLevel": cucsVnicDefBehPolicyLevel,
       "cucsVnicDefBehPolicyOwner": cucsVnicDefBehPolicyOwner,
       "cucsVnicDynamicConTable": cucsVnicDynamicConTable,
       "cucsVnicDynamicConEntry": cucsVnicDynamicConEntry,
       "cucsVnicDynamicConInstanceId": cucsVnicDynamicConInstanceId,
       "cucsVnicDynamicConDn": cucsVnicDynamicConDn,
       "cucsVnicDynamicConRn": cucsVnicDynamicConRn,
       "cucsVnicDynamicConAdaptorProfileName": cucsVnicDynamicConAdaptorProfileName,
       "cucsVnicDynamicConDescr": cucsVnicDynamicConDescr,
       "cucsVnicDynamicConDynamicEth": cucsVnicDynamicConDynamicEth,
       "cucsVnicDynamicConIntId": cucsVnicDynamicConIntId,
       "cucsVnicDynamicConMtu": cucsVnicDynamicConMtu,
       "cucsVnicDynamicConName": cucsVnicDynamicConName,
       "cucsVnicDynamicConNamingPrefix": cucsVnicDynamicConNamingPrefix,
       "cucsVnicDynamicConProtection": cucsVnicDynamicConProtection,
       "cucsVnicDynamicConPolicyLevel": cucsVnicDynamicConPolicyLevel,
       "cucsVnicDynamicConPolicyOwner": cucsVnicDynamicConPolicyOwner,
       "cucsVnicDynamicConPolicyTable": cucsVnicDynamicConPolicyTable,
       "cucsVnicDynamicConPolicyEntry": cucsVnicDynamicConPolicyEntry,
       "cucsVnicDynamicConPolicyInstanceId": cucsVnicDynamicConPolicyInstanceId,
       "cucsVnicDynamicConPolicyDn": cucsVnicDynamicConPolicyDn,
       "cucsVnicDynamicConPolicyRn": cucsVnicDynamicConPolicyRn,
       "cucsVnicDynamicConPolicyAdaptorProfileName": cucsVnicDynamicConPolicyAdaptorProfileName,
       "cucsVnicDynamicConPolicyDescr": cucsVnicDynamicConPolicyDescr,
       "cucsVnicDynamicConPolicyDynamicEth": cucsVnicDynamicConPolicyDynamicEth,
       "cucsVnicDynamicConPolicyIntId": cucsVnicDynamicConPolicyIntId,
       "cucsVnicDynamicConPolicyMtu": cucsVnicDynamicConPolicyMtu,
       "cucsVnicDynamicConPolicyName": cucsVnicDynamicConPolicyName,
       "cucsVnicDynamicConPolicyNamingPrefix": cucsVnicDynamicConPolicyNamingPrefix,
       "cucsVnicDynamicConPolicyProtection": cucsVnicDynamicConPolicyProtection,
       "cucsVnicDynamicConPolicyPolicyLevel": cucsVnicDynamicConPolicyPolicyLevel,
       "cucsVnicDynamicConPolicyPolicyOwner": cucsVnicDynamicConPolicyPolicyOwner,
       "cucsVnicDynamicIdUniverseTable": cucsVnicDynamicIdUniverseTable,
       "cucsVnicDynamicIdUniverseEntry": cucsVnicDynamicIdUniverseEntry,
       "cucsVnicDynamicIdUniverseInstanceId": cucsVnicDynamicIdUniverseInstanceId,
       "cucsVnicDynamicIdUniverseDn": cucsVnicDynamicIdUniverseDn,
       "cucsVnicDynamicIdUniverseRn": cucsVnicDynamicIdUniverseRn,
       "cucsVnicDynamicIdUniverseDescr": cucsVnicDynamicIdUniverseDescr,
       "cucsVnicDynamicIdUniverseIntId": cucsVnicDynamicIdUniverseIntId,
       "cucsVnicDynamicIdUniverseName": cucsVnicDynamicIdUniverseName,
       "cucsVnicDynamicIdUniversePolicyLevel": cucsVnicDynamicIdUniversePolicyLevel,
       "cucsVnicDynamicIdUniversePolicyOwner": cucsVnicDynamicIdUniversePolicyOwner,
       "cucsVnicDynamicProviderTable": cucsVnicDynamicProviderTable,
       "cucsVnicDynamicProviderEntry": cucsVnicDynamicProviderEntry,
       "cucsVnicDynamicProviderInstanceId": cucsVnicDynamicProviderInstanceId,
       "cucsVnicDynamicProviderDn": cucsVnicDynamicProviderDn,
       "cucsVnicDynamicProviderRn": cucsVnicDynamicProviderRn,
       "cucsVnicDynamicProviderName": cucsVnicDynamicProviderName,
       "cucsVnicDynamicProviderEpTable": cucsVnicDynamicProviderEpTable,
       "cucsVnicDynamicProviderEpEntry": cucsVnicDynamicProviderEpEntry,
       "cucsVnicDynamicProviderEpInstanceId": cucsVnicDynamicProviderEpInstanceId,
       "cucsVnicDynamicProviderEpDn": cucsVnicDynamicProviderEpDn,
       "cucsVnicDynamicProviderEpRn": cucsVnicDynamicProviderEpRn,
       "cucsVnicDynamicProviderEpChassisId": cucsVnicDynamicProviderEpChassisId,
       "cucsVnicDynamicProviderEpPortId": cucsVnicDynamicProviderEpPortId,
       "cucsVnicDynamicProviderEpSlotId": cucsVnicDynamicProviderEpSlotId,
       "cucsVnicDynamicProviderEpSwitchId": cucsVnicDynamicProviderEpSwitchId,
       "cucsVnicEthLifTable": cucsVnicEthLifTable,
       "cucsVnicEthLifEntry": cucsVnicEthLifEntry,
       "cucsVnicEthLifInstanceId": cucsVnicEthLifInstanceId,
       "cucsVnicEthLifDn": cucsVnicEthLifDn,
       "cucsVnicEthLifRn": cucsVnicEthLifRn,
       "cucsVnicEthLifAddr": cucsVnicEthLifAddr,
       "cucsVnicEthLifName": cucsVnicEthLifName,
       "cucsVnicEthLifNicDn": cucsVnicEthLifNicDn,
       "cucsVnicEthLifOwner": cucsVnicEthLifOwner,
       "cucsVnicEthLifSwitchId": cucsVnicEthLifSwitchId,
       "cucsVnicEthLifType": cucsVnicEthLifType,
       "cucsVnicEthLifVnicDn": cucsVnicEthLifVnicDn,
       "cucsVnicEtherTable": cucsVnicEtherTable,
       "cucsVnicEtherEntry": cucsVnicEtherEntry,
       "cucsVnicEtherInstanceId": cucsVnicEtherInstanceId,
       "cucsVnicEtherDn": cucsVnicEtherDn,
       "cucsVnicEtherRn": cucsVnicEtherRn,
       "cucsVnicEtherAdaptorProfileName": cucsVnicEtherAdaptorProfileName,
       "cucsVnicEtherAddr": cucsVnicEtherAddr,
       "cucsVnicEtherAdminVcon": cucsVnicEtherAdminVcon,
       "cucsVnicEtherBootDev": cucsVnicEtherBootDev,
       "cucsVnicEtherConfigState": cucsVnicEtherConfigState,
       "cucsVnicEtherEquipmentDn": cucsVnicEtherEquipmentDn,
       "cucsVnicEtherFltAggr": cucsVnicEtherFltAggr,
       "cucsVnicEtherIdentPoolName": cucsVnicEtherIdentPoolName,
       "cucsVnicEtherInstType": cucsVnicEtherInstType,
       "cucsVnicEtherMtu": cucsVnicEtherMtu,
       "cucsVnicEtherName": cucsVnicEtherName,
       "cucsVnicEtherNwCtrlPolicyName": cucsVnicEtherNwCtrlPolicyName,
       "cucsVnicEtherNwTemplName": cucsVnicEtherNwTemplName,
       "cucsVnicEtherOperAdaptorProfileName": cucsVnicEtherOperAdaptorProfileName,
       "cucsVnicEtherOperIdentPoolName": cucsVnicEtherOperIdentPoolName,
       "cucsVnicEtherOperNwCtrlPolicyName": cucsVnicEtherOperNwCtrlPolicyName,
       "cucsVnicEtherOperNwTemplName": cucsVnicEtherOperNwTemplName,
       "cucsVnicEtherOperOrder": cucsVnicEtherOperOrder,
       "cucsVnicEtherOperQosPolicyName": cucsVnicEtherOperQosPolicyName,
       "cucsVnicEtherOperSpeed": cucsVnicEtherOperSpeed,
       "cucsVnicEtherOperStatsPolicyName": cucsVnicEtherOperStatsPolicyName,
       "cucsVnicEtherOperVcon": cucsVnicEtherOperVcon,
       "cucsVnicEtherOrder": cucsVnicEtherOrder,
       "cucsVnicEtherOwner": cucsVnicEtherOwner,
       "cucsVnicEtherPinToGroupName": cucsVnicEtherPinToGroupName,
       "cucsVnicEtherQosPolicyName": cucsVnicEtherQosPolicyName,
       "cucsVnicEtherStatsPolicyName": cucsVnicEtherStatsPolicyName,
       "cucsVnicEtherSwitchId": cucsVnicEtherSwitchId,
       "cucsVnicEtherType": cucsVnicEtherType,
       "cucsVnicEtherOperPinToGroupName": cucsVnicEtherOperPinToGroupName,
       "cucsVnicEtherConfigQualifier": cucsVnicEtherConfigQualifier,
       "cucsVnicEtherDynamicId": cucsVnicEtherDynamicId,
       "cucsVnicEtherPfDn": cucsVnicEtherPfDn,
       "cucsVnicEtherVirtualizationPreference": cucsVnicEtherVirtualizationPreference,
       "cucsVnicEtherAdminHostPort": cucsVnicEtherAdminHostPort,
       "cucsVnicEtherOperHostPort": cucsVnicEtherOperHostPort,
       "cucsVnicEtherPropAcl": cucsVnicEtherPropAcl,
       "cucsVnicEtherPurpose": cucsVnicEtherPurpose,
       "cucsVnicEtherAdminCdnName": cucsVnicEtherAdminCdnName,
       "cucsVnicEtherOperCdnName": cucsVnicEtherOperCdnName,
       "cucsVnicEtherCdnSource": cucsVnicEtherCdnSource,
       "cucsVnicEtherCdnPropInSync": cucsVnicEtherCdnPropInSync,
       "cucsVnicEtherIfTable": cucsVnicEtherIfTable,
       "cucsVnicEtherIfEntry": cucsVnicEtherIfEntry,
       "cucsVnicEtherIfInstanceId": cucsVnicEtherIfInstanceId,
       "cucsVnicEtherIfDn": cucsVnicEtherIfDn,
       "cucsVnicEtherIfRn": cucsVnicEtherIfRn,
       "cucsVnicEtherIfAddr": cucsVnicEtherIfAddr,
       "cucsVnicEtherIfDefaultNet": cucsVnicEtherIfDefaultNet,
       "cucsVnicEtherIfName": cucsVnicEtherIfName,
       "cucsVnicEtherIfOperState": cucsVnicEtherIfOperState,
       "cucsVnicEtherIfOwner": cucsVnicEtherIfOwner,
       "cucsVnicEtherIfSwitchId": cucsVnicEtherIfSwitchId,
       "cucsVnicEtherIfType": cucsVnicEtherIfType,
       "cucsVnicEtherIfVnet": cucsVnicEtherIfVnet,
       "cucsVnicEtherIfOperVnetDn": cucsVnicEtherIfOperVnetDn,
       "cucsVnicEtherIfOperVnetName": cucsVnicEtherIfOperVnetName,
       "cucsVnicEtherIfConfigQualifier": cucsVnicEtherIfConfigQualifier,
       "cucsVnicEtherIfFltAggr": cucsVnicEtherIfFltAggr,
       "cucsVnicEtherIfPubNwId": cucsVnicEtherIfPubNwId,
       "cucsVnicEtherIfSharing": cucsVnicEtherIfSharing,
       "cucsVnicEtherIfPropAcl": cucsVnicEtherIfPropAcl,
       "cucsVnicEtherIfOperPrimaryVnetDn": cucsVnicEtherIfOperPrimaryVnetDn,
       "cucsVnicEtherIfOperPrimaryVnetName": cucsVnicEtherIfOperPrimaryVnetName,
       "cucsVnicFcTable": cucsVnicFcTable,
       "cucsVnicFcEntry": cucsVnicFcEntry,
       "cucsVnicFcInstanceId": cucsVnicFcInstanceId,
       "cucsVnicFcDn": cucsVnicFcDn,
       "cucsVnicFcRn": cucsVnicFcRn,
       "cucsVnicFcAdaptorProfileName": cucsVnicFcAdaptorProfileName,
       "cucsVnicFcAddr": cucsVnicFcAddr,
       "cucsVnicFcAdminVcon": cucsVnicFcAdminVcon,
       "cucsVnicFcBootDev": cucsVnicFcBootDev,
       "cucsVnicFcConfigState": cucsVnicFcConfigState,
       "cucsVnicFcEquipmentDn": cucsVnicFcEquipmentDn,
       "cucsVnicFcFltAggr": cucsVnicFcFltAggr,
       "cucsVnicFcIdentPoolName": cucsVnicFcIdentPoolName,
       "cucsVnicFcInstType": cucsVnicFcInstType,
       "cucsVnicFcMaxDataFieldSize": cucsVnicFcMaxDataFieldSize,
       "cucsVnicFcName": cucsVnicFcName,
       "cucsVnicFcNdAddr": cucsVnicFcNdAddr,
       "cucsVnicFcNwTemplName": cucsVnicFcNwTemplName,
       "cucsVnicFcOperAdaptorProfileName": cucsVnicFcOperAdaptorProfileName,
       "cucsVnicFcOperIdentPoolName": cucsVnicFcOperIdentPoolName,
       "cucsVnicFcOperNwTemplName": cucsVnicFcOperNwTemplName,
       "cucsVnicFcOperOrder": cucsVnicFcOperOrder,
       "cucsVnicFcOperQosPolicyName": cucsVnicFcOperQosPolicyName,
       "cucsVnicFcOperSpeed": cucsVnicFcOperSpeed,
       "cucsVnicFcOperStatsPolicyName": cucsVnicFcOperStatsPolicyName,
       "cucsVnicFcOperVcon": cucsVnicFcOperVcon,
       "cucsVnicFcOrder": cucsVnicFcOrder,
       "cucsVnicFcOwner": cucsVnicFcOwner,
       "cucsVnicFcPersBind": cucsVnicFcPersBind,
       "cucsVnicFcPersBindClear": cucsVnicFcPersBindClear,
       "cucsVnicFcPinToGroupName": cucsVnicFcPinToGroupName,
       "cucsVnicFcQosPolicyName": cucsVnicFcQosPolicyName,
       "cucsVnicFcStatsPolicyName": cucsVnicFcStatsPolicyName,
       "cucsVnicFcSwitchId": cucsVnicFcSwitchId,
       "cucsVnicFcType": cucsVnicFcType,
       "cucsVnicFcOperPinToGroupName": cucsVnicFcOperPinToGroupName,
       "cucsVnicFcConfigQualifier": cucsVnicFcConfigQualifier,
       "cucsVnicFcAdminHostPort": cucsVnicFcAdminHostPort,
       "cucsVnicFcOperHostPort": cucsVnicFcOperHostPort,
       "cucsVnicFcAdminCdnName": cucsVnicFcAdminCdnName,
       "cucsVnicFcOperCdnName": cucsVnicFcOperCdnName,
       "cucsVnicFcCdnSource": cucsVnicFcCdnSource,
       "cucsVnicFcCdnPropInSync": cucsVnicFcCdnPropInSync,
       "cucsVnicFcIfTable": cucsVnicFcIfTable,
       "cucsVnicFcIfEntry": cucsVnicFcIfEntry,
       "cucsVnicFcIfInstanceId": cucsVnicFcIfInstanceId,
       "cucsVnicFcIfDn": cucsVnicFcIfDn,
       "cucsVnicFcIfRn": cucsVnicFcIfRn,
       "cucsVnicFcIfInitiator": cucsVnicFcIfInitiator,
       "cucsVnicFcIfName": cucsVnicFcIfName,
       "cucsVnicFcIfOperState": cucsVnicFcIfOperState,
       "cucsVnicFcIfOwner": cucsVnicFcIfOwner,
       "cucsVnicFcIfSwitchId": cucsVnicFcIfSwitchId,
       "cucsVnicFcIfType": cucsVnicFcIfType,
       "cucsVnicFcIfVnet": cucsVnicFcIfVnet,
       "cucsVnicFcIfOperVnetDn": cucsVnicFcIfOperVnetDn,
       "cucsVnicFcIfOperVnetName": cucsVnicFcIfOperVnetName,
       "cucsVnicFcIfConfigQualifier": cucsVnicFcIfConfigQualifier,
       "cucsVnicFcIfPubNwId": cucsVnicFcIfPubNwId,
       "cucsVnicFcIfSharing": cucsVnicFcIfSharing,
       "cucsVnicFcIfOperPrimaryVnetDn": cucsVnicFcIfOperPrimaryVnetDn,
       "cucsVnicFcIfOperPrimaryVnetName": cucsVnicFcIfOperPrimaryVnetName,
       "cucsVnicFcLifTable": cucsVnicFcLifTable,
       "cucsVnicFcLifEntry": cucsVnicFcLifEntry,
       "cucsVnicFcLifInstanceId": cucsVnicFcLifInstanceId,
       "cucsVnicFcLifDn": cucsVnicFcLifDn,
       "cucsVnicFcLifRn": cucsVnicFcLifRn,
       "cucsVnicFcLifAddr": cucsVnicFcLifAddr,
       "cucsVnicFcLifName": cucsVnicFcLifName,
       "cucsVnicFcLifNicDn": cucsVnicFcLifNicDn,
       "cucsVnicFcLifOwner": cucsVnicFcLifOwner,
       "cucsVnicFcLifSwitchId": cucsVnicFcLifSwitchId,
       "cucsVnicFcLifType": cucsVnicFcLifType,
       "cucsVnicFcLifVnicDn": cucsVnicFcLifVnicDn,
       "cucsVnicFcNodeTable": cucsVnicFcNodeTable,
       "cucsVnicFcNodeEntry": cucsVnicFcNodeEntry,
       "cucsVnicFcNodeInstanceId": cucsVnicFcNodeInstanceId,
       "cucsVnicFcNodeDn": cucsVnicFcNodeDn,
       "cucsVnicFcNodeRn": cucsVnicFcNodeRn,
       "cucsVnicFcNodeAddr": cucsVnicFcNodeAddr,
       "cucsVnicFcNodeFltAggr": cucsVnicFcNodeFltAggr,
       "cucsVnicFcNodeIdentPoolName": cucsVnicFcNodeIdentPoolName,
       "cucsVnicFcNodeOperIdentPoolName": cucsVnicFcNodeOperIdentPoolName,
       "cucsVnicFcNodeMaxDerivableWWPN": cucsVnicFcNodeMaxDerivableWWPN,
       "cucsVnicFcNodeOwner": cucsVnicFcNodeOwner,
       "cucsVnicFcOEIfTable": cucsVnicFcOEIfTable,
       "cucsVnicFcOEIfEntry": cucsVnicFcOEIfEntry,
       "cucsVnicFcOEIfInstanceId": cucsVnicFcOEIfInstanceId,
       "cucsVnicFcOEIfDn": cucsVnicFcOEIfDn,
       "cucsVnicFcOEIfRn": cucsVnicFcOEIfRn,
       "cucsVnicFcOEIfInitiator": cucsVnicFcOEIfInitiator,
       "cucsVnicFcOEIfName": cucsVnicFcOEIfName,
       "cucsVnicFcOEIfOperState": cucsVnicFcOEIfOperState,
       "cucsVnicFcOEIfOwner": cucsVnicFcOEIfOwner,
       "cucsVnicFcOEIfSwitchId": cucsVnicFcOEIfSwitchId,
       "cucsVnicFcOEIfType": cucsVnicFcOEIfType,
       "cucsVnicFcOEIfVnet": cucsVnicFcOEIfVnet,
       "cucsVnicFcOEIfConfigQualifier": cucsVnicFcOEIfConfigQualifier,
       "cucsVnicFcOEIfOperVnetDn": cucsVnicFcOEIfOperVnetDn,
       "cucsVnicFcOEIfOperVnetName": cucsVnicFcOEIfOperVnetName,
       "cucsVnicFcOEIfPubNwId": cucsVnicFcOEIfPubNwId,
       "cucsVnicFcOEIfSharing": cucsVnicFcOEIfSharing,
       "cucsVnicFcOEIfOperPrimaryVnetDn": cucsVnicFcOEIfOperPrimaryVnetDn,
       "cucsVnicFcOEIfOperPrimaryVnetName": cucsVnicFcOEIfOperPrimaryVnetName,
       "cucsVnicIPv4DhcpTable": cucsVnicIPv4DhcpTable,
       "cucsVnicIPv4DhcpEntry": cucsVnicIPv4DhcpEntry,
       "cucsVnicIPv4DhcpInstanceId": cucsVnicIPv4DhcpInstanceId,
       "cucsVnicIPv4DhcpDn": cucsVnicIPv4DhcpDn,
       "cucsVnicIPv4DhcpRn": cucsVnicIPv4DhcpRn,
       "cucsVnicIPv4DhcpAddr": cucsVnicIPv4DhcpAddr,
       "cucsVnicIPv4DhcpDefGw": cucsVnicIPv4DhcpDefGw,
       "cucsVnicIPv4DhcpSubnet": cucsVnicIPv4DhcpSubnet,
       "cucsVnicIPv4DnsTable": cucsVnicIPv4DnsTable,
       "cucsVnicIPv4DnsEntry": cucsVnicIPv4DnsEntry,
       "cucsVnicIPv4DnsInstanceId": cucsVnicIPv4DnsInstanceId,
       "cucsVnicIPv4DnsDn": cucsVnicIPv4DnsDn,
       "cucsVnicIPv4DnsRn": cucsVnicIPv4DnsRn,
       "cucsVnicIPv4DnsAddr": cucsVnicIPv4DnsAddr,
       "cucsVnicIPv4DnsDefGw": cucsVnicIPv4DnsDefGw,
       "cucsVnicIPv4DnsPref": cucsVnicIPv4DnsPref,
       "cucsVnicIPv4DnsSubnet": cucsVnicIPv4DnsSubnet,
       "cucsVnicIPv4IfTable": cucsVnicIPv4IfTable,
       "cucsVnicIPv4IfEntry": cucsVnicIPv4IfEntry,
       "cucsVnicIPv4IfInstanceId": cucsVnicIPv4IfInstanceId,
       "cucsVnicIPv4IfDn": cucsVnicIPv4IfDn,
       "cucsVnicIPv4IfRn": cucsVnicIPv4IfRn,
       "cucsVnicIPv4IfAddr": cucsVnicIPv4IfAddr,
       "cucsVnicIPv4IfName": cucsVnicIPv4IfName,
       "cucsVnicIPv4IfOperState": cucsVnicIPv4IfOperState,
       "cucsVnicIPv4IfOwner": cucsVnicIPv4IfOwner,
       "cucsVnicIPv4IfSwitchId": cucsVnicIPv4IfSwitchId,
       "cucsVnicIPv4IfType": cucsVnicIPv4IfType,
       "cucsVnicIPv4IfVnet": cucsVnicIPv4IfVnet,
       "cucsVnicIPv4IfConfigQualifier": cucsVnicIPv4IfConfigQualifier,
       "cucsVnicIPv4IfOperVnetDn": cucsVnicIPv4IfOperVnetDn,
       "cucsVnicIPv4IfOperVnetName": cucsVnicIPv4IfOperVnetName,
       "cucsVnicIPv4IfPubNwId": cucsVnicIPv4IfPubNwId,
       "cucsVnicIPv4IfSharing": cucsVnicIPv4IfSharing,
       "cucsVnicIPv4IfPropAcl": cucsVnicIPv4IfPropAcl,
       "cucsVnicIPv4IfOperPrimaryVnetDn": cucsVnicIPv4IfOperPrimaryVnetDn,
       "cucsVnicIPv4IfOperPrimaryVnetName": cucsVnicIPv4IfOperPrimaryVnetName,
       "cucsVnicIPv4StaticRouteTable": cucsVnicIPv4StaticRouteTable,
       "cucsVnicIPv4StaticRouteEntry": cucsVnicIPv4StaticRouteEntry,
       "cucsVnicIPv4StaticRouteInstanceId": cucsVnicIPv4StaticRouteInstanceId,
       "cucsVnicIPv4StaticRouteDn": cucsVnicIPv4StaticRouteDn,
       "cucsVnicIPv4StaticRouteRn": cucsVnicIPv4StaticRouteRn,
       "cucsVnicIPv4StaticRouteAddr": cucsVnicIPv4StaticRouteAddr,
       "cucsVnicIPv4StaticRouteDefGw": cucsVnicIPv4StaticRouteDefGw,
       "cucsVnicIPv4StaticRouteGwAddr": cucsVnicIPv4StaticRouteGwAddr,
       "cucsVnicIPv4StaticRouteGwSubnet": cucsVnicIPv4StaticRouteGwSubnet,
       "cucsVnicIPv4StaticRouteSubnet": cucsVnicIPv4StaticRouteSubnet,
       "cucsVnicIpV4PooledAddrTable": cucsVnicIpV4PooledAddrTable,
       "cucsVnicIpV4PooledAddrEntry": cucsVnicIpV4PooledAddrEntry,
       "cucsVnicIpV4PooledAddrInstanceId": cucsVnicIpV4PooledAddrInstanceId,
       "cucsVnicIpV4PooledAddrDn": cucsVnicIpV4PooledAddrDn,
       "cucsVnicIpV4PooledAddrRn": cucsVnicIpV4PooledAddrRn,
       "cucsVnicIpV4PooledAddrAddr": cucsVnicIpV4PooledAddrAddr,
       "cucsVnicIpV4PooledAddrDefGw": cucsVnicIpV4PooledAddrDefGw,
       "cucsVnicIpV4PooledAddrName": cucsVnicIpV4PooledAddrName,
       "cucsVnicIpV4PooledAddrSubnet": cucsVnicIpV4PooledAddrSubnet,
       "cucsVnicIpV4PooledAddrOperName": cucsVnicIpV4PooledAddrOperName,
       "cucsVnicIpV4PooledAddrPrimDns": cucsVnicIpV4PooledAddrPrimDns,
       "cucsVnicIpV4PooledAddrSecDns": cucsVnicIpV4PooledAddrSecDns,
       "cucsVnicIpV4ProfDerivedAddrTable": cucsVnicIpV4ProfDerivedAddrTable,
       "cucsVnicIpV4ProfDerivedAddrEntry": cucsVnicIpV4ProfDerivedAddrEntry,
       "cucsVnicIpV4ProfDerivedAddrInstanceId": cucsVnicIpV4ProfDerivedAddrInstanceId,
       "cucsVnicIpV4ProfDerivedAddrDn": cucsVnicIpV4ProfDerivedAddrDn,
       "cucsVnicIpV4ProfDerivedAddrRn": cucsVnicIpV4ProfDerivedAddrRn,
       "cucsVnicIpV4ProfDerivedAddrAddr": cucsVnicIpV4ProfDerivedAddrAddr,
       "cucsVnicIpV4ProfDerivedAddrDefGw": cucsVnicIpV4ProfDerivedAddrDefGw,
       "cucsVnicIpV4ProfDerivedAddrSubnet": cucsVnicIpV4ProfDerivedAddrSubnet,
       "cucsVnicIpV4StaticAddrTable": cucsVnicIpV4StaticAddrTable,
       "cucsVnicIpV4StaticAddrEntry": cucsVnicIpV4StaticAddrEntry,
       "cucsVnicIpV4StaticAddrInstanceId": cucsVnicIpV4StaticAddrInstanceId,
       "cucsVnicIpV4StaticAddrDn": cucsVnicIpV4StaticAddrDn,
       "cucsVnicIpV4StaticAddrRn": cucsVnicIpV4StaticAddrRn,
       "cucsVnicIpV4StaticAddrAddr": cucsVnicIpV4StaticAddrAddr,
       "cucsVnicIpV4StaticAddrDefGw": cucsVnicIpV4StaticAddrDefGw,
       "cucsVnicIpV4StaticAddrSubnet": cucsVnicIpV4StaticAddrSubnet,
       "cucsVnicIpV4StaticAddrPrimDns": cucsVnicIpV4StaticAddrPrimDns,
       "cucsVnicIpV4StaticAddrSecDns": cucsVnicIpV4StaticAddrSecDns,
       "cucsVnicIpcTable": cucsVnicIpcTable,
       "cucsVnicIpcEntry": cucsVnicIpcEntry,
       "cucsVnicIpcInstanceId": cucsVnicIpcInstanceId,
       "cucsVnicIpcDn": cucsVnicIpcDn,
       "cucsVnicIpcRn": cucsVnicIpcRn,
       "cucsVnicIpcAdaptorProfileName": cucsVnicIpcAdaptorProfileName,
       "cucsVnicIpcAddr": cucsVnicIpcAddr,
       "cucsVnicIpcAdminVcon": cucsVnicIpcAdminVcon,
       "cucsVnicIpcBootDev": cucsVnicIpcBootDev,
       "cucsVnicIpcConfigState": cucsVnicIpcConfigState,
       "cucsVnicIpcEquipmentDn": cucsVnicIpcEquipmentDn,
       "cucsVnicIpcIdentPoolName": cucsVnicIpcIdentPoolName,
       "cucsVnicIpcInstType": cucsVnicIpcInstType,
       "cucsVnicIpcMtu": cucsVnicIpcMtu,
       "cucsVnicIpcName": cucsVnicIpcName,
       "cucsVnicIpcNwCtrlPolicyName": cucsVnicIpcNwCtrlPolicyName,
       "cucsVnicIpcNwTemplName": cucsVnicIpcNwTemplName,
       "cucsVnicIpcOperAdaptorProfileName": cucsVnicIpcOperAdaptorProfileName,
       "cucsVnicIpcOperIdentPoolName": cucsVnicIpcOperIdentPoolName,
       "cucsVnicIpcOperNwCtrlPolicyName": cucsVnicIpcOperNwCtrlPolicyName,
       "cucsVnicIpcOperNwTemplName": cucsVnicIpcOperNwTemplName,
       "cucsVnicIpcOperOrder": cucsVnicIpcOperOrder,
       "cucsVnicIpcOperQosPolicyName": cucsVnicIpcOperQosPolicyName,
       "cucsVnicIpcOperSpeed": cucsVnicIpcOperSpeed,
       "cucsVnicIpcOperStatsPolicyName": cucsVnicIpcOperStatsPolicyName,
       "cucsVnicIpcOperVcon": cucsVnicIpcOperVcon,
       "cucsVnicIpcOrder": cucsVnicIpcOrder,
       "cucsVnicIpcOwner": cucsVnicIpcOwner,
       "cucsVnicIpcPinToGroupName": cucsVnicIpcPinToGroupName,
       "cucsVnicIpcQosPolicyName": cucsVnicIpcQosPolicyName,
       "cucsVnicIpcStatsPolicyName": cucsVnicIpcStatsPolicyName,
       "cucsVnicIpcSwitchId": cucsVnicIpcSwitchId,
       "cucsVnicIpcType": cucsVnicIpcType,
       "cucsVnicIpcOperPinToGroupName": cucsVnicIpcOperPinToGroupName,
       "cucsVnicIpcConfigQualifier": cucsVnicIpcConfigQualifier,
       "cucsVnicIpcAdminHostPort": cucsVnicIpcAdminHostPort,
       "cucsVnicIpcOperHostPort": cucsVnicIpcOperHostPort,
       "cucsVnicIpcPurpose": cucsVnicIpcPurpose,
       "cucsVnicIpcAdminCdnName": cucsVnicIpcAdminCdnName,
       "cucsVnicIpcOperCdnName": cucsVnicIpcOperCdnName,
       "cucsVnicIpcCdnPropInSync": cucsVnicIpcCdnPropInSync,
       "cucsVnicIpcCdnSource": cucsVnicIpcCdnSource,
       "cucsVnicIpcIfTable": cucsVnicIpcIfTable,
       "cucsVnicIpcIfEntry": cucsVnicIpcIfEntry,
       "cucsVnicIpcIfInstanceId": cucsVnicIpcIfInstanceId,
       "cucsVnicIpcIfDn": cucsVnicIpcIfDn,
       "cucsVnicIpcIfRn": cucsVnicIpcIfRn,
       "cucsVnicIpcIfAddr": cucsVnicIpcIfAddr,
       "cucsVnicIpcIfDefaultNet": cucsVnicIpcIfDefaultNet,
       "cucsVnicIpcIfName": cucsVnicIpcIfName,
       "cucsVnicIpcIfOperState": cucsVnicIpcIfOperState,
       "cucsVnicIpcIfOwner": cucsVnicIpcIfOwner,
       "cucsVnicIpcIfSwitchId": cucsVnicIpcIfSwitchId,
       "cucsVnicIpcIfType": cucsVnicIpcIfType,
       "cucsVnicIpcIfVnet": cucsVnicIpcIfVnet,
       "cucsVnicIpcIfConfigQualifier": cucsVnicIpcIfConfigQualifier,
       "cucsVnicIpcIfOperVnetDn": cucsVnicIpcIfOperVnetDn,
       "cucsVnicIpcIfOperVnetName": cucsVnicIpcIfOperVnetName,
       "cucsVnicIpcIfPubNwId": cucsVnicIpcIfPubNwId,
       "cucsVnicIpcIfSharing": cucsVnicIpcIfSharing,
       "cucsVnicIpcIfOperPrimaryVnetDn": cucsVnicIpcIfOperPrimaryVnetDn,
       "cucsVnicIpcIfOperPrimaryVnetName": cucsVnicIpcIfOperPrimaryVnetName,
       "cucsVnicLanConnTemplTable": cucsVnicLanConnTemplTable,
       "cucsVnicLanConnTemplEntry": cucsVnicLanConnTemplEntry,
       "cucsVnicLanConnTemplInstanceId": cucsVnicLanConnTemplInstanceId,
       "cucsVnicLanConnTemplDn": cucsVnicLanConnTemplDn,
       "cucsVnicLanConnTemplRn": cucsVnicLanConnTemplRn,
       "cucsVnicLanConnTemplDescr": cucsVnicLanConnTemplDescr,
       "cucsVnicLanConnTemplIdentPoolName": cucsVnicLanConnTemplIdentPoolName,
       "cucsVnicLanConnTemplIntId": cucsVnicLanConnTemplIntId,
       "cucsVnicLanConnTemplMtu": cucsVnicLanConnTemplMtu,
       "cucsVnicLanConnTemplName": cucsVnicLanConnTemplName,
       "cucsVnicLanConnTemplNwCtrlPolicyName": cucsVnicLanConnTemplNwCtrlPolicyName,
       "cucsVnicLanConnTemplOperIdentPoolName": cucsVnicLanConnTemplOperIdentPoolName,
       "cucsVnicLanConnTemplOperNwCtrlPolicyName": cucsVnicLanConnTemplOperNwCtrlPolicyName,
       "cucsVnicLanConnTemplOperQosPolicyName": cucsVnicLanConnTemplOperQosPolicyName,
       "cucsVnicLanConnTemplOperStatsPolicyName": cucsVnicLanConnTemplOperStatsPolicyName,
       "cucsVnicLanConnTemplPinToGroupName": cucsVnicLanConnTemplPinToGroupName,
       "cucsVnicLanConnTemplQosPolicyName": cucsVnicLanConnTemplQosPolicyName,
       "cucsVnicLanConnTemplStatsPolicyName": cucsVnicLanConnTemplStatsPolicyName,
       "cucsVnicLanConnTemplSwitchId": cucsVnicLanConnTemplSwitchId,
       "cucsVnicLanConnTemplTarget": cucsVnicLanConnTemplTarget,
       "cucsVnicLanConnTemplTemplType": cucsVnicLanConnTemplTemplType,
       "cucsVnicLanConnTemplPolicyLevel": cucsVnicLanConnTemplPolicyLevel,
       "cucsVnicLanConnTemplPolicyOwner": cucsVnicLanConnTemplPolicyOwner,
       "cucsVnicLanConnTemplAdminCdnName": cucsVnicLanConnTemplAdminCdnName,
       "cucsVnicLanConnTemplCdnSource": cucsVnicLanConnTemplCdnSource,
       "cucsVnicLifVlanTable": cucsVnicLifVlanTable,
       "cucsVnicLifVlanEntry": cucsVnicLifVlanEntry,
       "cucsVnicLifVlanInstanceId": cucsVnicLifVlanInstanceId,
       "cucsVnicLifVlanDn": cucsVnicLifVlanDn,
       "cucsVnicLifVlanRn": cucsVnicLifVlanRn,
       "cucsVnicLifVlanAddr": cucsVnicLifVlanAddr,
       "cucsVnicLifVlanDefaultNet": cucsVnicLifVlanDefaultNet,
       "cucsVnicLifVlanName": cucsVnicLifVlanName,
       "cucsVnicLifVlanOperState": cucsVnicLifVlanOperState,
       "cucsVnicLifVlanOwner": cucsVnicLifVlanOwner,
       "cucsVnicLifVlanSwitchId": cucsVnicLifVlanSwitchId,
       "cucsVnicLifVlanType": cucsVnicLifVlanType,
       "cucsVnicLifVlanVnet": cucsVnicLifVlanVnet,
       "cucsVnicLifVlanConfigQualifier": cucsVnicLifVlanConfigQualifier,
       "cucsVnicLifVlanOperVnetDn": cucsVnicLifVlanOperVnetDn,
       "cucsVnicLifVlanOperVnetName": cucsVnicLifVlanOperVnetName,
       "cucsVnicLifVlanPubNwId": cucsVnicLifVlanPubNwId,
       "cucsVnicLifVlanSharing": cucsVnicLifVlanSharing,
       "cucsVnicLifVlanPropAcl": cucsVnicLifVlanPropAcl,
       "cucsVnicLifVlanOperPrimaryVnetDn": cucsVnicLifVlanOperPrimaryVnetDn,
       "cucsVnicLifVlanOperPrimaryVnetName": cucsVnicLifVlanOperPrimaryVnetName,
       "cucsVnicLifVsanTable": cucsVnicLifVsanTable,
       "cucsVnicLifVsanEntry": cucsVnicLifVsanEntry,
       "cucsVnicLifVsanInstanceId": cucsVnicLifVsanInstanceId,
       "cucsVnicLifVsanDn": cucsVnicLifVsanDn,
       "cucsVnicLifVsanRn": cucsVnicLifVsanRn,
       "cucsVnicLifVsanInitiator": cucsVnicLifVsanInitiator,
       "cucsVnicLifVsanName": cucsVnicLifVsanName,
       "cucsVnicLifVsanOperState": cucsVnicLifVsanOperState,
       "cucsVnicLifVsanOwner": cucsVnicLifVsanOwner,
       "cucsVnicLifVsanSwitchId": cucsVnicLifVsanSwitchId,
       "cucsVnicLifVsanType": cucsVnicLifVsanType,
       "cucsVnicLifVsanVnet": cucsVnicLifVsanVnet,
       "cucsVnicLifVsanConfigQualifier": cucsVnicLifVsanConfigQualifier,
       "cucsVnicLifVsanOperVnetDn": cucsVnicLifVsanOperVnetDn,
       "cucsVnicLifVsanOperVnetName": cucsVnicLifVsanOperVnetName,
       "cucsVnicLifVsanPubNwId": cucsVnicLifVsanPubNwId,
       "cucsVnicLifVsanSharing": cucsVnicLifVsanSharing,
       "cucsVnicLifVsanOperPrimaryVnetDn": cucsVnicLifVsanOperPrimaryVnetDn,
       "cucsVnicLifVsanOperPrimaryVnetName": cucsVnicLifVsanOperPrimaryVnetName,
       "cucsVnicProfileTable": cucsVnicProfileTable,
       "cucsVnicProfileEntry": cucsVnicProfileEntry,
       "cucsVnicProfileInstanceId": cucsVnicProfileInstanceId,
       "cucsVnicProfileDn": cucsVnicProfileDn,
       "cucsVnicProfileRn": cucsVnicProfileRn,
       "cucsVnicProfileCdp": cucsVnicProfileCdp,
       "cucsVnicProfileCos": cucsVnicProfileCos,
       "cucsVnicProfileDescr": cucsVnicProfileDescr,
       "cucsVnicProfileForgeMac": cucsVnicProfileForgeMac,
       "cucsVnicProfileIntId": cucsVnicProfileIntId,
       "cucsVnicProfileMaxPorts": cucsVnicProfileMaxPorts,
       "cucsVnicProfileName": cucsVnicProfileName,
       "cucsVnicProfileNwCtrlPolicyName": cucsVnicProfileNwCtrlPolicyName,
       "cucsVnicProfileOperNwCtrlPolicyName": cucsVnicProfileOperNwCtrlPolicyName,
       "cucsVnicProfileOperQosPolicyName": cucsVnicProfileOperQosPolicyName,
       "cucsVnicProfilePinToGroupName": cucsVnicProfilePinToGroupName,
       "cucsVnicProfileQosPolicyId": cucsVnicProfileQosPolicyId,
       "cucsVnicProfileQosPolicyName": cucsVnicProfileQosPolicyName,
       "cucsVnicProfileSwABorderPort": cucsVnicProfileSwABorderPort,
       "cucsVnicProfileSwABorderSlot": cucsVnicProfileSwABorderSlot,
       "cucsVnicProfileSwBBorderPort": cucsVnicProfileSwBBorderPort,
       "cucsVnicProfileSwBBorderSlot": cucsVnicProfileSwBBorderSlot,
       "cucsVnicProfileUplinkFailAction": cucsVnicProfileUplinkFailAction,
       "cucsVnicProfileHostNwIOPerf": cucsVnicProfileHostNwIOPerf,
       "cucsVnicProfilePrimaryVlanId": cucsVnicProfilePrimaryVlanId,
       "cucsVnicProfileQosPolicyDn": cucsVnicProfileQosPolicyDn,
       "cucsVnicProfileConfigQualifier": cucsVnicProfileConfigQualifier,
       "cucsVnicProfileMacRegisterMode": cucsVnicProfileMacRegisterMode,
       "cucsVnicProfilePolicyLevel": cucsVnicProfilePolicyLevel,
       "cucsVnicProfilePolicyOwner": cucsVnicProfilePolicyOwner,
       "cucsVnicProfilePortProfileUuid": cucsVnicProfilePortProfileUuid,
       "cucsVnicProfileType": cucsVnicProfileType,
       "cucsVnicProfileSwABorderAggrPort": cucsVnicProfileSwABorderAggrPort,
       "cucsVnicProfileSwBBorderAggrPort": cucsVnicProfileSwBBorderAggrPort,
       "cucsVnicProfileLldp": cucsVnicProfileLldp,
       "cucsVnicProfileAliasTable": cucsVnicProfileAliasTable,
       "cucsVnicProfileAliasEntry": cucsVnicProfileAliasEntry,
       "cucsVnicProfileAliasInstanceId": cucsVnicProfileAliasInstanceId,
       "cucsVnicProfileAliasDn": cucsVnicProfileAliasDn,
       "cucsVnicProfileAliasRn": cucsVnicProfileAliasRn,
       "cucsVnicProfileAliasAlias": cucsVnicProfileAliasAlias,
       "cucsVnicProfileAliasSwUuid": cucsVnicProfileAliasSwUuid,
       "cucsVnicProfileSetTable": cucsVnicProfileSetTable,
       "cucsVnicProfileSetEntry": cucsVnicProfileSetEntry,
       "cucsVnicProfileSetInstanceId": cucsVnicProfileSetInstanceId,
       "cucsVnicProfileSetDn": cucsVnicProfileSetDn,
       "cucsVnicProfileSetRn": cucsVnicProfileSetRn,
       "cucsVnicProfileSetFsmDescr": cucsVnicProfileSetFsmDescr,
       "cucsVnicProfileSetFsmPrev": cucsVnicProfileSetFsmPrev,
       "cucsVnicProfileSetFsmProgr": cucsVnicProfileSetFsmProgr,
       "cucsVnicProfileSetFsmRmtInvErrCode": cucsVnicProfileSetFsmRmtInvErrCode,
       "cucsVnicProfileSetFsmRmtInvErrDescr": cucsVnicProfileSetFsmRmtInvErrDescr,
       "cucsVnicProfileSetFsmRmtInvRslt": cucsVnicProfileSetFsmRmtInvRslt,
       "cucsVnicProfileSetFsmStageDescr": cucsVnicProfileSetFsmStageDescr,
       "cucsVnicProfileSetFsmStamp": cucsVnicProfileSetFsmStamp,
       "cucsVnicProfileSetFsmStatus": cucsVnicProfileSetFsmStatus,
       "cucsVnicProfileSetFsmTry": cucsVnicProfileSetFsmTry,
       "cucsVnicProfileSetFltAggr": cucsVnicProfileSetFltAggr,
       "cucsVnicProfileSetGenNum": cucsVnicProfileSetGenNum,
       "cucsVnicProfileSetVlanGroupUpdate": cucsVnicProfileSetVlanGroupUpdate,
       "cucsVnicProfileSetFsmTaskTable": cucsVnicProfileSetFsmTaskTable,
       "cucsVnicProfileSetFsmTaskEntry": cucsVnicProfileSetFsmTaskEntry,
       "cucsVnicProfileSetFsmTaskInstanceId": cucsVnicProfileSetFsmTaskInstanceId,
       "cucsVnicProfileSetFsmTaskDn": cucsVnicProfileSetFsmTaskDn,
       "cucsVnicProfileSetFsmTaskRn": cucsVnicProfileSetFsmTaskRn,
       "cucsVnicProfileSetFsmTaskCompletion": cucsVnicProfileSetFsmTaskCompletion,
       "cucsVnicProfileSetFsmTaskFlags": cucsVnicProfileSetFsmTaskFlags,
       "cucsVnicProfileSetFsmTaskItem": cucsVnicProfileSetFsmTaskItem,
       "cucsVnicProfileSetFsmTaskSeqId": cucsVnicProfileSetFsmTaskSeqId,
       "cucsVnicSanConnTemplTable": cucsVnicSanConnTemplTable,
       "cucsVnicSanConnTemplEntry": cucsVnicSanConnTemplEntry,
       "cucsVnicSanConnTemplInstanceId": cucsVnicSanConnTemplInstanceId,
       "cucsVnicSanConnTemplDn": cucsVnicSanConnTemplDn,
       "cucsVnicSanConnTemplRn": cucsVnicSanConnTemplRn,
       "cucsVnicSanConnTemplDescr": cucsVnicSanConnTemplDescr,
       "cucsVnicSanConnTemplIdentPoolName": cucsVnicSanConnTemplIdentPoolName,
       "cucsVnicSanConnTemplIntId": cucsVnicSanConnTemplIntId,
       "cucsVnicSanConnTemplMaxDataFieldSize": cucsVnicSanConnTemplMaxDataFieldSize,
       "cucsVnicSanConnTemplName": cucsVnicSanConnTemplName,
       "cucsVnicSanConnTemplNwCtrlPolicyName": cucsVnicSanConnTemplNwCtrlPolicyName,
       "cucsVnicSanConnTemplOperIdentPoolName": cucsVnicSanConnTemplOperIdentPoolName,
       "cucsVnicSanConnTemplOperQosPolicyName": cucsVnicSanConnTemplOperQosPolicyName,
       "cucsVnicSanConnTemplOperStatsPolicyName": cucsVnicSanConnTemplOperStatsPolicyName,
       "cucsVnicSanConnTemplPinToGroupName": cucsVnicSanConnTemplPinToGroupName,
       "cucsVnicSanConnTemplQosPolicyName": cucsVnicSanConnTemplQosPolicyName,
       "cucsVnicSanConnTemplStatsPolicyName": cucsVnicSanConnTemplStatsPolicyName,
       "cucsVnicSanConnTemplSwitchId": cucsVnicSanConnTemplSwitchId,
       "cucsVnicSanConnTemplTarget": cucsVnicSanConnTemplTarget,
       "cucsVnicSanConnTemplTemplType": cucsVnicSanConnTemplTemplType,
       "cucsVnicSanConnTemplPolicyLevel": cucsVnicSanConnTemplPolicyLevel,
       "cucsVnicSanConnTemplPolicyOwner": cucsVnicSanConnTemplPolicyOwner,
       "cucsVnicScsiTable": cucsVnicScsiTable,
       "cucsVnicScsiEntry": cucsVnicScsiEntry,
       "cucsVnicScsiInstanceId": cucsVnicScsiInstanceId,
       "cucsVnicScsiDn": cucsVnicScsiDn,
       "cucsVnicScsiRn": cucsVnicScsiRn,
       "cucsVnicScsiAdaptorProfileName": cucsVnicScsiAdaptorProfileName,
       "cucsVnicScsiAdminVcon": cucsVnicScsiAdminVcon,
       "cucsVnicScsiBootDev": cucsVnicScsiBootDev,
       "cucsVnicScsiConfigState": cucsVnicScsiConfigState,
       "cucsVnicScsiEquipmentDn": cucsVnicScsiEquipmentDn,
       "cucsVnicScsiIdentPoolName": cucsVnicScsiIdentPoolName,
       "cucsVnicScsiInstType": cucsVnicScsiInstType,
       "cucsVnicScsiName": cucsVnicScsiName,
       "cucsVnicScsiNwTemplName": cucsVnicScsiNwTemplName,
       "cucsVnicScsiOperOrder": cucsVnicScsiOperOrder,
       "cucsVnicScsiOperSpeed": cucsVnicScsiOperSpeed,
       "cucsVnicScsiOperStatsPolicyName": cucsVnicScsiOperStatsPolicyName,
       "cucsVnicScsiOperVcon": cucsVnicScsiOperVcon,
       "cucsVnicScsiOrder": cucsVnicScsiOrder,
       "cucsVnicScsiOwner": cucsVnicScsiOwner,
       "cucsVnicScsiPinToGroupName": cucsVnicScsiPinToGroupName,
       "cucsVnicScsiQosPolicyName": cucsVnicScsiQosPolicyName,
       "cucsVnicScsiStatsPolicyName": cucsVnicScsiStatsPolicyName,
       "cucsVnicScsiSwitchId": cucsVnicScsiSwitchId,
       "cucsVnicScsiType": cucsVnicScsiType,
       "cucsVnicScsiConfigQualifier": cucsVnicScsiConfigQualifier,
       "cucsVnicScsiAdminHostPort": cucsVnicScsiAdminHostPort,
       "cucsVnicScsiOperHostPort": cucsVnicScsiOperHostPort,
       "cucsVnicScsiAdminCdnName": cucsVnicScsiAdminCdnName,
       "cucsVnicScsiOperCdnName": cucsVnicScsiOperCdnName,
       "cucsVnicScsiCdnPropInSync": cucsVnicScsiCdnPropInSync,
       "cucsVnicScsiCdnSource": cucsVnicScsiCdnSource,
       "cucsVnicScsiIfTable": cucsVnicScsiIfTable,
       "cucsVnicScsiIfEntry": cucsVnicScsiIfEntry,
       "cucsVnicScsiIfInstanceId": cucsVnicScsiIfInstanceId,
       "cucsVnicScsiIfDn": cucsVnicScsiIfDn,
       "cucsVnicScsiIfRn": cucsVnicScsiIfRn,
       "cucsVnicScsiIfAddr": cucsVnicScsiIfAddr,
       "cucsVnicScsiIfName": cucsVnicScsiIfName,
       "cucsVnicScsiIfOperState": cucsVnicScsiIfOperState,
       "cucsVnicScsiIfOwner": cucsVnicScsiIfOwner,
       "cucsVnicScsiIfSwitchId": cucsVnicScsiIfSwitchId,
       "cucsVnicScsiIfType": cucsVnicScsiIfType,
       "cucsVnicScsiIfVnet": cucsVnicScsiIfVnet,
       "cucsVnicScsiIfConfigQualifier": cucsVnicScsiIfConfigQualifier,
       "cucsVnicScsiIfOperVnetDn": cucsVnicScsiIfOperVnetDn,
       "cucsVnicScsiIfOperVnetName": cucsVnicScsiIfOperVnetName,
       "cucsVnicScsiIfPubNwId": cucsVnicScsiIfPubNwId,
       "cucsVnicScsiIfSharing": cucsVnicScsiIfSharing,
       "cucsVnicScsiIfOperPrimaryVnetDn": cucsVnicScsiIfOperPrimaryVnetDn,
       "cucsVnicScsiIfOperPrimaryVnetName": cucsVnicScsiIfOperPrimaryVnetName,
       "cucsVnicBootIpPolicyTable": cucsVnicBootIpPolicyTable,
       "cucsVnicBootIpPolicyEntry": cucsVnicBootIpPolicyEntry,
       "cucsVnicBootIpPolicyInstanceId": cucsVnicBootIpPolicyInstanceId,
       "cucsVnicBootIpPolicyDn": cucsVnicBootIpPolicyDn,
       "cucsVnicBootIpPolicyRn": cucsVnicBootIpPolicyRn,
       "cucsVnicBootIpPolicyDescr": cucsVnicBootIpPolicyDescr,
       "cucsVnicBootIpPolicyIntId": cucsVnicBootIpPolicyIntId,
       "cucsVnicBootIpPolicyName": cucsVnicBootIpPolicyName,
       "cucsVnicBootIpPolicyPoolName": cucsVnicBootIpPolicyPoolName,
       "cucsVnicBootIpPolicyPolicyLevel": cucsVnicBootIpPolicyPolicyLevel,
       "cucsVnicBootIpPolicyPolicyOwner": cucsVnicBootIpPolicyPolicyOwner,
       "cucsVnicIPv4IscsiAddrTable": cucsVnicIPv4IscsiAddrTable,
       "cucsVnicIPv4IscsiAddrEntry": cucsVnicIPv4IscsiAddrEntry,
       "cucsVnicIPv4IscsiAddrInstanceId": cucsVnicIPv4IscsiAddrInstanceId,
       "cucsVnicIPv4IscsiAddrDn": cucsVnicIPv4IscsiAddrDn,
       "cucsVnicIPv4IscsiAddrRn": cucsVnicIPv4IscsiAddrRn,
       "cucsVnicIPv4IscsiAddrAddr": cucsVnicIPv4IscsiAddrAddr,
       "cucsVnicIPv4IscsiAddrDefGw": cucsVnicIPv4IscsiAddrDefGw,
       "cucsVnicIPv4IscsiAddrPrimDns": cucsVnicIPv4IscsiAddrPrimDns,
       "cucsVnicIPv4IscsiAddrSecDns": cucsVnicIPv4IscsiAddrSecDns,
       "cucsVnicIPv4IscsiAddrSubnet": cucsVnicIPv4IscsiAddrSubnet,
       "cucsVnicIPv4PooledIscsiAddrTable": cucsVnicIPv4PooledIscsiAddrTable,
       "cucsVnicIPv4PooledIscsiAddrEntry": cucsVnicIPv4PooledIscsiAddrEntry,
       "cucsVnicIPv4PooledIscsiAddrInstanceId": cucsVnicIPv4PooledIscsiAddrInstanceId,
       "cucsVnicIPv4PooledIscsiAddrDn": cucsVnicIPv4PooledIscsiAddrDn,
       "cucsVnicIPv4PooledIscsiAddrRn": cucsVnicIPv4PooledIscsiAddrRn,
       "cucsVnicIPv4PooledIscsiAddrAddr": cucsVnicIPv4PooledIscsiAddrAddr,
       "cucsVnicIPv4PooledIscsiAddrDefGw": cucsVnicIPv4PooledIscsiAddrDefGw,
       "cucsVnicIPv4PooledIscsiAddrIdentPoolName": cucsVnicIPv4PooledIscsiAddrIdentPoolName,
       "cucsVnicIPv4PooledIscsiAddrOperIdentPoolName": cucsVnicIPv4PooledIscsiAddrOperIdentPoolName,
       "cucsVnicIPv4PooledIscsiAddrPrimDns": cucsVnicIPv4PooledIscsiAddrPrimDns,
       "cucsVnicIPv4PooledIscsiAddrSecDns": cucsVnicIPv4PooledIscsiAddrSecDns,
       "cucsVnicIPv4PooledIscsiAddrSubnet": cucsVnicIPv4PooledIscsiAddrSubnet,
       "cucsVnicIScsiTable": cucsVnicIScsiTable,
       "cucsVnicIScsiEntry": cucsVnicIScsiEntry,
       "cucsVnicIScsiInstanceId": cucsVnicIScsiInstanceId,
       "cucsVnicIScsiDn": cucsVnicIScsiDn,
       "cucsVnicIScsiRn": cucsVnicIScsiRn,
       "cucsVnicIScsiAdaptorProfileName": cucsVnicIScsiAdaptorProfileName,
       "cucsVnicIScsiAddr": cucsVnicIScsiAddr,
       "cucsVnicIScsiAdminVcon": cucsVnicIScsiAdminVcon,
       "cucsVnicIScsiAuthProfileName": cucsVnicIScsiAuthProfileName,
       "cucsVnicIScsiBootDev": cucsVnicIScsiBootDev,
       "cucsVnicIScsiConfigState": cucsVnicIScsiConfigState,
       "cucsVnicIScsiEquipmentDn": cucsVnicIScsiEquipmentDn,
       "cucsVnicIScsiEthEpDn": cucsVnicIScsiEthEpDn,
       "cucsVnicIScsiExtIPState": cucsVnicIScsiExtIPState,
       "cucsVnicIScsiFltAggr": cucsVnicIScsiFltAggr,
       "cucsVnicIScsiIdentPoolName": cucsVnicIScsiIdentPoolName,
       "cucsVnicIScsiInitiatorName": cucsVnicIScsiInitiatorName,
       "cucsVnicIScsiInstType": cucsVnicIScsiInstType,
       "cucsVnicIScsiIqnIdentPoolName": cucsVnicIScsiIqnIdentPoolName,
       "cucsVnicIScsiName": cucsVnicIScsiName,
       "cucsVnicIScsiNwTemplName": cucsVnicIScsiNwTemplName,
       "cucsVnicIScsiOperAdaptorProfileName": cucsVnicIScsiOperAdaptorProfileName,
       "cucsVnicIScsiOperAuthProfileName": cucsVnicIScsiOperAuthProfileName,
       "cucsVnicIScsiOperIqnIdentPoolName": cucsVnicIScsiOperIqnIdentPoolName,
       "cucsVnicIScsiOperOrder": cucsVnicIScsiOperOrder,
       "cucsVnicIScsiOperSpeed": cucsVnicIScsiOperSpeed,
       "cucsVnicIScsiOperStatsPolicyName": cucsVnicIScsiOperStatsPolicyName,
       "cucsVnicIScsiOperVcon": cucsVnicIScsiOperVcon,
       "cucsVnicIScsiOrder": cucsVnicIScsiOrder,
       "cucsVnicIScsiOwner": cucsVnicIScsiOwner,
       "cucsVnicIScsiPinToGroupName": cucsVnicIScsiPinToGroupName,
       "cucsVnicIScsiQosPolicyName": cucsVnicIScsiQosPolicyName,
       "cucsVnicIScsiStatsPolicyName": cucsVnicIScsiStatsPolicyName,
       "cucsVnicIScsiSwitchId": cucsVnicIScsiSwitchId,
       "cucsVnicIScsiType": cucsVnicIScsiType,
       "cucsVnicIScsiVnicDefType": cucsVnicIScsiVnicDefType,
       "cucsVnicIScsiVnicName": cucsVnicIScsiVnicName,
       "cucsVnicIScsiConfigQualifier": cucsVnicIScsiConfigQualifier,
       "cucsVnicIScsiInitNameSuffix": cucsVnicIScsiInitNameSuffix,
       "cucsVnicIScsiOperIdentPoolName": cucsVnicIScsiOperIdentPoolName,
       "cucsVnicIScsiAdminHostPort": cucsVnicIScsiAdminHostPort,
       "cucsVnicIScsiOperHostPort": cucsVnicIScsiOperHostPort,
       "cucsVnicIScsiPropAcl": cucsVnicIScsiPropAcl,
       "cucsVnicIScsiAdminCdnName": cucsVnicIScsiAdminCdnName,
       "cucsVnicIScsiOperCdnName": cucsVnicIScsiOperCdnName,
       "cucsVnicIScsiCdnSource": cucsVnicIScsiCdnSource,
       "cucsVnicIScsiCdnPropInSync": cucsVnicIScsiCdnPropInSync,
       "cucsVnicIScsiAutoTargetIfTable": cucsVnicIScsiAutoTargetIfTable,
       "cucsVnicIScsiAutoTargetIfEntry": cucsVnicIScsiAutoTargetIfEntry,
       "cucsVnicIScsiAutoTargetIfInstanceId": cucsVnicIScsiAutoTargetIfInstanceId,
       "cucsVnicIScsiAutoTargetIfDn": cucsVnicIScsiAutoTargetIfDn,
       "cucsVnicIScsiAutoTargetIfRn": cucsVnicIScsiAutoTargetIfRn,
       "cucsVnicIScsiAutoTargetIfDhcpVendorId": cucsVnicIScsiAutoTargetIfDhcpVendorId,
       "cucsVnicIScsiNodeTable": cucsVnicIScsiNodeTable,
       "cucsVnicIScsiNodeEntry": cucsVnicIScsiNodeEntry,
       "cucsVnicIScsiNodeInstanceId": cucsVnicIScsiNodeInstanceId,
       "cucsVnicIScsiNodeDn": cucsVnicIScsiNodeDn,
       "cucsVnicIScsiNodeRn": cucsVnicIScsiNodeRn,
       "cucsVnicIScsiNodeFltAggr": cucsVnicIScsiNodeFltAggr,
       "cucsVnicIScsiNodeInitiatorName": cucsVnicIScsiNodeInitiatorName,
       "cucsVnicIScsiNodeOwner": cucsVnicIScsiNodeOwner,
       "cucsVnicIScsiNodeInitNameSuffix": cucsVnicIScsiNodeInitNameSuffix,
       "cucsVnicIScsiNodeIqnIdentPoolName": cucsVnicIScsiNodeIqnIdentPoolName,
       "cucsVnicIScsiNodeOperIqnIdentPoolName": cucsVnicIScsiNodeOperIqnIdentPoolName,
       "cucsVnicIScsiNodeInitiatorPolicyName": cucsVnicIScsiNodeInitiatorPolicyName,
       "cucsVnicIScsiNodeOperInitiatorPolicyName": cucsVnicIScsiNodeOperInitiatorPolicyName,
       "cucsVnicIScsiNodePropAcl": cucsVnicIScsiNodePropAcl,
       "cucsVnicIScsiStaticTargetIfTable": cucsVnicIScsiStaticTargetIfTable,
       "cucsVnicIScsiStaticTargetIfEntry": cucsVnicIScsiStaticTargetIfEntry,
       "cucsVnicIScsiStaticTargetIfInstanceId": cucsVnicIScsiStaticTargetIfInstanceId,
       "cucsVnicIScsiStaticTargetIfDn": cucsVnicIScsiStaticTargetIfDn,
       "cucsVnicIScsiStaticTargetIfRn": cucsVnicIScsiStaticTargetIfRn,
       "cucsVnicIScsiStaticTargetIfAuthProfileName": cucsVnicIScsiStaticTargetIfAuthProfileName,
       "cucsVnicIScsiStaticTargetIfIpAddress": cucsVnicIScsiStaticTargetIfIpAddress,
       "cucsVnicIScsiStaticTargetIfName": cucsVnicIScsiStaticTargetIfName,
       "cucsVnicIScsiStaticTargetIfOperAuthProfileName": cucsVnicIScsiStaticTargetIfOperAuthProfileName,
       "cucsVnicIScsiStaticTargetIfPort": cucsVnicIScsiStaticTargetIfPort,
       "cucsVnicIScsiStaticTargetIfPriority": cucsVnicIScsiStaticTargetIfPriority,
       "cucsVnicIScsiStaticTargetIfPropAcl": cucsVnicIScsiStaticTargetIfPropAcl,
       "cucsVnicInternalProfileTable": cucsVnicInternalProfileTable,
       "cucsVnicInternalProfileEntry": cucsVnicInternalProfileEntry,
       "cucsVnicInternalProfileInstanceId": cucsVnicInternalProfileInstanceId,
       "cucsVnicInternalProfileDn": cucsVnicInternalProfileDn,
       "cucsVnicInternalProfileRn": cucsVnicInternalProfileRn,
       "cucsVnicInternalProfileDescr": cucsVnicInternalProfileDescr,
       "cucsVnicInternalProfileIntId": cucsVnicInternalProfileIntId,
       "cucsVnicInternalProfileMaxPorts": cucsVnicInternalProfileMaxPorts,
       "cucsVnicInternalProfileName": cucsVnicInternalProfileName,
       "cucsVnicInternalProfilePolicyLevel": cucsVnicInternalProfilePolicyLevel,
       "cucsVnicInternalProfilePolicyOwner": cucsVnicInternalProfilePolicyOwner,
       "cucsVnicLunTable": cucsVnicLunTable,
       "cucsVnicLunEntry": cucsVnicLunEntry,
       "cucsVnicLunInstanceId": cucsVnicLunInstanceId,
       "cucsVnicLunDn": cucsVnicLunDn,
       "cucsVnicLunRn": cucsVnicLunRn,
       "cucsVnicLunBootable": cucsVnicLunBootable,
       "cucsVnicLunId": cucsVnicLunId,
       "cucsVnicOProfileAliasTable": cucsVnicOProfileAliasTable,
       "cucsVnicOProfileAliasEntry": cucsVnicOProfileAliasEntry,
       "cucsVnicOProfileAliasInstanceId": cucsVnicOProfileAliasInstanceId,
       "cucsVnicOProfileAliasDn": cucsVnicOProfileAliasDn,
       "cucsVnicOProfileAliasRn": cucsVnicOProfileAliasRn,
       "cucsVnicOProfileAliasAlias": cucsVnicOProfileAliasAlias,
       "cucsVnicOProfileAliasMgmtPlane": cucsVnicOProfileAliasMgmtPlane,
       "cucsVnicOProfileAliasVSwitchId": cucsVnicOProfileAliasVSwitchId,
       "cucsVnicOProfileAliasVSwitchName": cucsVnicOProfileAliasVSwitchName,
       "cucsVnicVlanTable": cucsVnicVlanTable,
       "cucsVnicVlanEntry": cucsVnicVlanEntry,
       "cucsVnicVlanInstanceId": cucsVnicVlanInstanceId,
       "cucsVnicVlanDn": cucsVnicVlanDn,
       "cucsVnicVlanRn": cucsVnicVlanRn,
       "cucsVnicVlanFltAggr": cucsVnicVlanFltAggr,
       "cucsVnicVlanName": cucsVnicVlanName,
       "cucsVnicVlanOperState": cucsVnicVlanOperState,
       "cucsVnicVlanOwner": cucsVnicVlanOwner,
       "cucsVnicVlanSwitchId": cucsVnicVlanSwitchId,
       "cucsVnicVlanType": cucsVnicVlanType,
       "cucsVnicVlanVlanName": cucsVnicVlanVlanName,
       "cucsVnicVlanVnet": cucsVnicVlanVnet,
       "cucsVnicVlanConfigQualifier": cucsVnicVlanConfigQualifier,
       "cucsVnicVlanOperVnetDn": cucsVnicVlanOperVnetDn,
       "cucsVnicVlanOperVnetName": cucsVnicVlanOperVnetName,
       "cucsVnicVlanPubNwId": cucsVnicVlanPubNwId,
       "cucsVnicVlanSharing": cucsVnicVlanSharing,
       "cucsVnicVlanOperPrimaryVnetDn": cucsVnicVlanOperPrimaryVnetDn,
       "cucsVnicVlanOperPrimaryVnetName": cucsVnicVlanOperPrimaryVnetName,
       "cucsVnicConnDefTable": cucsVnicConnDefTable,
       "cucsVnicConnDefEntry": cucsVnicConnDefEntry,
       "cucsVnicConnDefInstanceId": cucsVnicConnDefInstanceId,
       "cucsVnicConnDefDn": cucsVnicConnDefDn,
       "cucsVnicConnDefRn": cucsVnicConnDefRn,
       "cucsVnicConnDefFltAggr": cucsVnicConnDefFltAggr,
       "cucsVnicConnDefLanConnPolicyName": cucsVnicConnDefLanConnPolicyName,
       "cucsVnicConnDefOperLanConnPolicyName": cucsVnicConnDefOperLanConnPolicyName,
       "cucsVnicConnDefOperSanConnPolicyName": cucsVnicConnDefOperSanConnPolicyName,
       "cucsVnicConnDefSanConnPolicyName": cucsVnicConnDefSanConnPolicyName,
       "cucsVnicConnDefPropAcl": cucsVnicConnDefPropAcl,
       "cucsVnicDynamicConPolicyRefTable": cucsVnicDynamicConPolicyRefTable,
       "cucsVnicDynamicConPolicyRefEntry": cucsVnicDynamicConPolicyRefEntry,
       "cucsVnicDynamicConPolicyRefInstanceId": cucsVnicDynamicConPolicyRefInstanceId,
       "cucsVnicDynamicConPolicyRefDn": cucsVnicDynamicConPolicyRefDn,
       "cucsVnicDynamicConPolicyRefRn": cucsVnicDynamicConPolicyRefRn,
       "cucsVnicDynamicConPolicyRefConPolicyName": cucsVnicDynamicConPolicyRefConPolicyName,
       "cucsVnicDynamicConPolicyRefOperConPolicyName": cucsVnicDynamicConPolicyRefOperConPolicyName,
       "cucsVnicFcGroupDefTable": cucsVnicFcGroupDefTable,
       "cucsVnicFcGroupDefEntry": cucsVnicFcGroupDefEntry,
       "cucsVnicFcGroupDefInstanceId": cucsVnicFcGroupDefInstanceId,
       "cucsVnicFcGroupDefDn": cucsVnicFcGroupDefDn,
       "cucsVnicFcGroupDefRn": cucsVnicFcGroupDefRn,
       "cucsVnicFcGroupDefAdaptorProfileName": cucsVnicFcGroupDefAdaptorProfileName,
       "cucsVnicFcGroupDefDescr": cucsVnicFcGroupDefDescr,
       "cucsVnicFcGroupDefIdentPoolName": cucsVnicFcGroupDefIdentPoolName,
       "cucsVnicFcGroupDefIntId": cucsVnicFcGroupDefIntId,
       "cucsVnicFcGroupDefMaxDataFieldSize": cucsVnicFcGroupDefMaxDataFieldSize,
       "cucsVnicFcGroupDefName": cucsVnicFcGroupDefName,
       "cucsVnicFcGroupDefNwTemplName": cucsVnicFcGroupDefNwTemplName,
       "cucsVnicFcGroupDefOperStatsPolicyName": cucsVnicFcGroupDefOperStatsPolicyName,
       "cucsVnicFcGroupDefOperStorageConnPolicyName": cucsVnicFcGroupDefOperStorageConnPolicyName,
       "cucsVnicFcGroupDefPolicyLevel": cucsVnicFcGroupDefPolicyLevel,
       "cucsVnicFcGroupDefPolicyOwner": cucsVnicFcGroupDefPolicyOwner,
       "cucsVnicFcGroupDefQosPolicyName": cucsVnicFcGroupDefQosPolicyName,
       "cucsVnicFcGroupDefStatsPolicyName": cucsVnicFcGroupDefStatsPolicyName,
       "cucsVnicFcGroupDefStorageConnPolicyName": cucsVnicFcGroupDefStorageConnPolicyName,
       "cucsVnicFcGroupTemplTable": cucsVnicFcGroupTemplTable,
       "cucsVnicFcGroupTemplEntry": cucsVnicFcGroupTemplEntry,
       "cucsVnicFcGroupTemplInstanceId": cucsVnicFcGroupTemplInstanceId,
       "cucsVnicFcGroupTemplDn": cucsVnicFcGroupTemplDn,
       "cucsVnicFcGroupTemplRn": cucsVnicFcGroupTemplRn,
       "cucsVnicFcGroupTemplAdaptorProfileName": cucsVnicFcGroupTemplAdaptorProfileName,
       "cucsVnicFcGroupTemplDescr": cucsVnicFcGroupTemplDescr,
       "cucsVnicFcGroupTemplIdentPoolName": cucsVnicFcGroupTemplIdentPoolName,
       "cucsVnicFcGroupTemplIntId": cucsVnicFcGroupTemplIntId,
       "cucsVnicFcGroupTemplMaxDataFieldSize": cucsVnicFcGroupTemplMaxDataFieldSize,
       "cucsVnicFcGroupTemplName": cucsVnicFcGroupTemplName,
       "cucsVnicFcGroupTemplNwTemplName": cucsVnicFcGroupTemplNwTemplName,
       "cucsVnicFcGroupTemplOperStatsPolicyName": cucsVnicFcGroupTemplOperStatsPolicyName,
       "cucsVnicFcGroupTemplOperStorageConnPolicyName": cucsVnicFcGroupTemplOperStorageConnPolicyName,
       "cucsVnicFcGroupTemplPolicyLevel": cucsVnicFcGroupTemplPolicyLevel,
       "cucsVnicFcGroupTemplPolicyOwner": cucsVnicFcGroupTemplPolicyOwner,
       "cucsVnicFcGroupTemplQosPolicyName": cucsVnicFcGroupTemplQosPolicyName,
       "cucsVnicFcGroupTemplStatsPolicyName": cucsVnicFcGroupTemplStatsPolicyName,
       "cucsVnicFcGroupTemplStorageConnPolicyName": cucsVnicFcGroupTemplStorageConnPolicyName,
       "cucsVnicFcGroupTemplTemplType": cucsVnicFcGroupTemplTemplType,
       "cucsVnicIScsiBootParamsTable": cucsVnicIScsiBootParamsTable,
       "cucsVnicIScsiBootParamsEntry": cucsVnicIScsiBootParamsEntry,
       "cucsVnicIScsiBootParamsInstanceId": cucsVnicIScsiBootParamsInstanceId,
       "cucsVnicIScsiBootParamsDn": cucsVnicIScsiBootParamsDn,
       "cucsVnicIScsiBootParamsRn": cucsVnicIScsiBootParamsRn,
       "cucsVnicIScsiBootParamsDescr": cucsVnicIScsiBootParamsDescr,
       "cucsVnicIScsiBootParamsIntId": cucsVnicIScsiBootParamsIntId,
       "cucsVnicIScsiBootParamsName": cucsVnicIScsiBootParamsName,
       "cucsVnicIScsiBootParamsPolicyLevel": cucsVnicIScsiBootParamsPolicyLevel,
       "cucsVnicIScsiBootParamsPolicyOwner": cucsVnicIScsiBootParamsPolicyOwner,
       "cucsVnicIScsiBootParamsOwner": cucsVnicIScsiBootParamsOwner,
       "cucsVnicIScsiBootParamsPropAcl": cucsVnicIScsiBootParamsPropAcl,
       "cucsVnicIScsiBootVnicTable": cucsVnicIScsiBootVnicTable,
       "cucsVnicIScsiBootVnicEntry": cucsVnicIScsiBootVnicEntry,
       "cucsVnicIScsiBootVnicInstanceId": cucsVnicIScsiBootVnicInstanceId,
       "cucsVnicIScsiBootVnicDn": cucsVnicIScsiBootVnicDn,
       "cucsVnicIScsiBootVnicRn": cucsVnicIScsiBootVnicRn,
       "cucsVnicIScsiBootVnicAuthProfileName": cucsVnicIScsiBootVnicAuthProfileName,
       "cucsVnicIScsiBootVnicDescr": cucsVnicIScsiBootVnicDescr,
       "cucsVnicIScsiBootVnicInitiatorName": cucsVnicIScsiBootVnicInitiatorName,
       "cucsVnicIScsiBootVnicIntId": cucsVnicIScsiBootVnicIntId,
       "cucsVnicIScsiBootVnicIqnIdentPoolName": cucsVnicIScsiBootVnicIqnIdentPoolName,
       "cucsVnicIScsiBootVnicName": cucsVnicIScsiBootVnicName,
       "cucsVnicIScsiBootVnicOperAuthProfileName": cucsVnicIScsiBootVnicOperAuthProfileName,
       "cucsVnicIScsiBootVnicOperIqnIdentPoolName": cucsVnicIScsiBootVnicOperIqnIdentPoolName,
       "cucsVnicIScsiBootVnicPolicyLevel": cucsVnicIScsiBootVnicPolicyLevel,
       "cucsVnicIScsiBootVnicPolicyOwner": cucsVnicIScsiBootVnicPolicyOwner,
       "cucsVnicIScsiLCPTable": cucsVnicIScsiLCPTable,
       "cucsVnicIScsiLCPEntry": cucsVnicIScsiLCPEntry,
       "cucsVnicIScsiLCPInstanceId": cucsVnicIScsiLCPInstanceId,
       "cucsVnicIScsiLCPDn": cucsVnicIScsiLCPDn,
       "cucsVnicIScsiLCPRn": cucsVnicIScsiLCPRn,
       "cucsVnicIScsiLCPAdaptorProfileName": cucsVnicIScsiLCPAdaptorProfileName,
       "cucsVnicIScsiLCPAddr": cucsVnicIScsiLCPAddr,
       "cucsVnicIScsiLCPAdminVcon": cucsVnicIScsiLCPAdminVcon,
       "cucsVnicIScsiLCPBootDev": cucsVnicIScsiLCPBootDev,
       "cucsVnicIScsiLCPConfigQualifier": cucsVnicIScsiLCPConfigQualifier,
       "cucsVnicIScsiLCPConfigState": cucsVnicIScsiLCPConfigState,
       "cucsVnicIScsiLCPEquipmentDn": cucsVnicIScsiLCPEquipmentDn,
       "cucsVnicIScsiLCPFltAggr": cucsVnicIScsiLCPFltAggr,
       "cucsVnicIScsiLCPIdentPoolName": cucsVnicIScsiLCPIdentPoolName,
       "cucsVnicIScsiLCPInstType": cucsVnicIScsiLCPInstType,
       "cucsVnicIScsiLCPName": cucsVnicIScsiLCPName,
       "cucsVnicIScsiLCPNwTemplName": cucsVnicIScsiLCPNwTemplName,
       "cucsVnicIScsiLCPOperAdaptorProfileName": cucsVnicIScsiLCPOperAdaptorProfileName,
       "cucsVnicIScsiLCPOperIdentPoolName": cucsVnicIScsiLCPOperIdentPoolName,
       "cucsVnicIScsiLCPOperOrder": cucsVnicIScsiLCPOperOrder,
       "cucsVnicIScsiLCPOperSpeed": cucsVnicIScsiLCPOperSpeed,
       "cucsVnicIScsiLCPOperStatsPolicyName": cucsVnicIScsiLCPOperStatsPolicyName,
       "cucsVnicIScsiLCPOperVcon": cucsVnicIScsiLCPOperVcon,
       "cucsVnicIScsiLCPOrder": cucsVnicIScsiLCPOrder,
       "cucsVnicIScsiLCPOwner": cucsVnicIScsiLCPOwner,
       "cucsVnicIScsiLCPPinToGroupName": cucsVnicIScsiLCPPinToGroupName,
       "cucsVnicIScsiLCPQosPolicyName": cucsVnicIScsiLCPQosPolicyName,
       "cucsVnicIScsiLCPStatsPolicyName": cucsVnicIScsiLCPStatsPolicyName,
       "cucsVnicIScsiLCPSwitchId": cucsVnicIScsiLCPSwitchId,
       "cucsVnicIScsiLCPType": cucsVnicIScsiLCPType,
       "cucsVnicIScsiLCPVnicName": cucsVnicIScsiLCPVnicName,
       "cucsVnicIScsiLCPAdminHostPort": cucsVnicIScsiLCPAdminHostPort,
       "cucsVnicIScsiLCPOperHostPort": cucsVnicIScsiLCPOperHostPort,
       "cucsVnicIScsiLCPAdminCdnName": cucsVnicIScsiLCPAdminCdnName,
       "cucsVnicIScsiLCPOperCdnName": cucsVnicIScsiLCPOperCdnName,
       "cucsVnicIScsiLCPCdnSource": cucsVnicIScsiLCPCdnSource,
       "cucsVnicIScsiLCPCdnPropInSync": cucsVnicIScsiLCPCdnPropInSync,
       "cucsVnicLanConnPolicyTable": cucsVnicLanConnPolicyTable,
       "cucsVnicLanConnPolicyEntry": cucsVnicLanConnPolicyEntry,
       "cucsVnicLanConnPolicyInstanceId": cucsVnicLanConnPolicyInstanceId,
       "cucsVnicLanConnPolicyDn": cucsVnicLanConnPolicyDn,
       "cucsVnicLanConnPolicyRn": cucsVnicLanConnPolicyRn,
       "cucsVnicLanConnPolicyDescr": cucsVnicLanConnPolicyDescr,
       "cucsVnicLanConnPolicyFltAggr": cucsVnicLanConnPolicyFltAggr,
       "cucsVnicLanConnPolicyIntId": cucsVnicLanConnPolicyIntId,
       "cucsVnicLanConnPolicyName": cucsVnicLanConnPolicyName,
       "cucsVnicLanConnPolicyPolicyLevel": cucsVnicLanConnPolicyPolicyLevel,
       "cucsVnicLanConnPolicyPolicyOwner": cucsVnicLanConnPolicyPolicyOwner,
       "cucsVnicProfileSetFsmTable": cucsVnicProfileSetFsmTable,
       "cucsVnicProfileSetFsmEntry": cucsVnicProfileSetFsmEntry,
       "cucsVnicProfileSetFsmInstanceId": cucsVnicProfileSetFsmInstanceId,
       "cucsVnicProfileSetFsmDn": cucsVnicProfileSetFsmDn,
       "cucsVnicProfileSetFsmRn": cucsVnicProfileSetFsmRn,
       "cucsVnicProfileSetFsmCompletionTime": cucsVnicProfileSetFsmCompletionTime,
       "cucsVnicProfileSetFsmCurrentFsm": cucsVnicProfileSetFsmCurrentFsm,
       "cucsVnicProfileSetFsmDescrData": cucsVnicProfileSetFsmDescrData,
       "cucsVnicProfileSetFsmFsmStatus": cucsVnicProfileSetFsmFsmStatus,
       "cucsVnicProfileSetFsmProgress": cucsVnicProfileSetFsmProgress,
       "cucsVnicProfileSetFsmRmtErrCode": cucsVnicProfileSetFsmRmtErrCode,
       "cucsVnicProfileSetFsmRmtErrDescr": cucsVnicProfileSetFsmRmtErrDescr,
       "cucsVnicProfileSetFsmRmtRslt": cucsVnicProfileSetFsmRmtRslt,
       "cucsVnicProfileSetFsmStageTable": cucsVnicProfileSetFsmStageTable,
       "cucsVnicProfileSetFsmStageEntry": cucsVnicProfileSetFsmStageEntry,
       "cucsVnicProfileSetFsmStageInstanceId": cucsVnicProfileSetFsmStageInstanceId,
       "cucsVnicProfileSetFsmStageDn": cucsVnicProfileSetFsmStageDn,
       "cucsVnicProfileSetFsmStageRn": cucsVnicProfileSetFsmStageRn,
       "cucsVnicProfileSetFsmStageDescrData": cucsVnicProfileSetFsmStageDescrData,
       "cucsVnicProfileSetFsmStageLastUpdateTime": cucsVnicProfileSetFsmStageLastUpdateTime,
       "cucsVnicProfileSetFsmStageName": cucsVnicProfileSetFsmStageName,
       "cucsVnicProfileSetFsmStageOrder": cucsVnicProfileSetFsmStageOrder,
       "cucsVnicProfileSetFsmStageRetry": cucsVnicProfileSetFsmStageRetry,
       "cucsVnicProfileSetFsmStageStageStatus": cucsVnicProfileSetFsmStageStageStatus,
       "cucsVnicRackServerDiscoveryProfileTable": cucsVnicRackServerDiscoveryProfileTable,
       "cucsVnicRackServerDiscoveryProfileEntry": cucsVnicRackServerDiscoveryProfileEntry,
       "cucsVnicRackServerDiscoveryProfileInstanceId": cucsVnicRackServerDiscoveryProfileInstanceId,
       "cucsVnicRackServerDiscoveryProfileDn": cucsVnicRackServerDiscoveryProfileDn,
       "cucsVnicRackServerDiscoveryProfileRn": cucsVnicRackServerDiscoveryProfileRn,
       "cucsVnicRackServerDiscoveryProfileDescr": cucsVnicRackServerDiscoveryProfileDescr,
       "cucsVnicRackServerDiscoveryProfileIntId": cucsVnicRackServerDiscoveryProfileIntId,
       "cucsVnicRackServerDiscoveryProfileMaxPorts": cucsVnicRackServerDiscoveryProfileMaxPorts,
       "cucsVnicRackServerDiscoveryProfileName": cucsVnicRackServerDiscoveryProfileName,
       "cucsVnicRackServerDiscoveryProfilePolicyLevel": cucsVnicRackServerDiscoveryProfilePolicyLevel,
       "cucsVnicRackServerDiscoveryProfilePolicyOwner": cucsVnicRackServerDiscoveryProfilePolicyOwner,
       "cucsVnicSanConnPolicyTable": cucsVnicSanConnPolicyTable,
       "cucsVnicSanConnPolicyEntry": cucsVnicSanConnPolicyEntry,
       "cucsVnicSanConnPolicyInstanceId": cucsVnicSanConnPolicyInstanceId,
       "cucsVnicSanConnPolicyDn": cucsVnicSanConnPolicyDn,
       "cucsVnicSanConnPolicyRn": cucsVnicSanConnPolicyRn,
       "cucsVnicSanConnPolicyDescr": cucsVnicSanConnPolicyDescr,
       "cucsVnicSanConnPolicyFltAggr": cucsVnicSanConnPolicyFltAggr,
       "cucsVnicSanConnPolicyIntId": cucsVnicSanConnPolicyIntId,
       "cucsVnicSanConnPolicyName": cucsVnicSanConnPolicyName,
       "cucsVnicSanConnPolicyPolicyLevel": cucsVnicSanConnPolicyPolicyLevel,
       "cucsVnicSanConnPolicyPolicyOwner": cucsVnicSanConnPolicyPolicyOwner,
       "cucsVnicVhbaBehPolicyTable": cucsVnicVhbaBehPolicyTable,
       "cucsVnicVhbaBehPolicyEntry": cucsVnicVhbaBehPolicyEntry,
       "cucsVnicVhbaBehPolicyInstanceId": cucsVnicVhbaBehPolicyInstanceId,
       "cucsVnicVhbaBehPolicyDn": cucsVnicVhbaBehPolicyDn,
       "cucsVnicVhbaBehPolicyRn": cucsVnicVhbaBehPolicyRn,
       "cucsVnicVhbaBehPolicyAction": cucsVnicVhbaBehPolicyAction,
       "cucsVnicVhbaBehPolicyDescr": cucsVnicVhbaBehPolicyDescr,
       "cucsVnicVhbaBehPolicyIntId": cucsVnicVhbaBehPolicyIntId,
       "cucsVnicVhbaBehPolicyName": cucsVnicVhbaBehPolicyName,
       "cucsVnicVhbaBehPolicyNwTemplName": cucsVnicVhbaBehPolicyNwTemplName,
       "cucsVnicVhbaBehPolicyPolicyLevel": cucsVnicVhbaBehPolicyPolicyLevel,
       "cucsVnicVhbaBehPolicyPolicyOwner": cucsVnicVhbaBehPolicyPolicyOwner,
       "cucsVnicVhbaBehPolicyType": cucsVnicVhbaBehPolicyType,
       "cucsVnicVnicBehPolicyTable": cucsVnicVnicBehPolicyTable,
       "cucsVnicVnicBehPolicyEntry": cucsVnicVnicBehPolicyEntry,
       "cucsVnicVnicBehPolicyInstanceId": cucsVnicVnicBehPolicyInstanceId,
       "cucsVnicVnicBehPolicyDn": cucsVnicVnicBehPolicyDn,
       "cucsVnicVnicBehPolicyRn": cucsVnicVnicBehPolicyRn,
       "cucsVnicVnicBehPolicyAction": cucsVnicVnicBehPolicyAction,
       "cucsVnicVnicBehPolicyDescr": cucsVnicVnicBehPolicyDescr,
       "cucsVnicVnicBehPolicyIntId": cucsVnicVnicBehPolicyIntId,
       "cucsVnicVnicBehPolicyName": cucsVnicVnicBehPolicyName,
       "cucsVnicVnicBehPolicyNwTemplName": cucsVnicVnicBehPolicyNwTemplName,
       "cucsVnicVnicBehPolicyPolicyLevel": cucsVnicVnicBehPolicyPolicyLevel,
       "cucsVnicVnicBehPolicyPolicyOwner": cucsVnicVnicBehPolicyPolicyOwner,
       "cucsVnicVnicBehPolicyType": cucsVnicVnicBehPolicyType,
       "cucsVnicIpV4HistoryTable": cucsVnicIpV4HistoryTable,
       "cucsVnicIpV4HistoryEntry": cucsVnicIpV4HistoryEntry,
       "cucsVnicIpV4HistoryInstanceId": cucsVnicIpV4HistoryInstanceId,
       "cucsVnicIpV4HistoryDn": cucsVnicIpV4HistoryDn,
       "cucsVnicIpV4HistoryRn": cucsVnicIpV4HistoryRn,
       "cucsVnicIpV4HistoryOldIpV4Addr": cucsVnicIpV4HistoryOldIpV4Addr,
       "cucsVnicIqnHistoryTable": cucsVnicIqnHistoryTable,
       "cucsVnicIqnHistoryEntry": cucsVnicIqnHistoryEntry,
       "cucsVnicIqnHistoryInstanceId": cucsVnicIqnHistoryInstanceId,
       "cucsVnicIqnHistoryDn": cucsVnicIqnHistoryDn,
       "cucsVnicIqnHistoryRn": cucsVnicIqnHistoryRn,
       "cucsVnicIqnHistoryOldInitiatorName": cucsVnicIqnHistoryOldInitiatorName,
       "cucsVnicMacHistoryTable": cucsVnicMacHistoryTable,
       "cucsVnicMacHistoryEntry": cucsVnicMacHistoryEntry,
       "cucsVnicMacHistoryInstanceId": cucsVnicMacHistoryInstanceId,
       "cucsVnicMacHistoryDn": cucsVnicMacHistoryDn,
       "cucsVnicMacHistoryRn": cucsVnicMacHistoryRn,
       "cucsVnicMacHistoryOldaddr": cucsVnicMacHistoryOldaddr,
       "cucsVnicWwnnHistoryTable": cucsVnicWwnnHistoryTable,
       "cucsVnicWwnnHistoryEntry": cucsVnicWwnnHistoryEntry,
       "cucsVnicWwnnHistoryInstanceId": cucsVnicWwnnHistoryInstanceId,
       "cucsVnicWwnnHistoryDn": cucsVnicWwnnHistoryDn,
       "cucsVnicWwnnHistoryRn": cucsVnicWwnnHistoryRn,
       "cucsVnicWwnnHistoryOldwwnn": cucsVnicWwnnHistoryOldwwnn,
       "cucsVnicWwpnHistoryTable": cucsVnicWwpnHistoryTable,
       "cucsVnicWwpnHistoryEntry": cucsVnicWwpnHistoryEntry,
       "cucsVnicWwpnHistoryInstanceId": cucsVnicWwpnHistoryInstanceId,
       "cucsVnicWwpnHistoryDn": cucsVnicWwpnHistoryDn,
       "cucsVnicWwpnHistoryRn": cucsVnicWwpnHistoryRn,
       "cucsVnicWwpnHistoryOldaddr": cucsVnicWwpnHistoryOldaddr,
       "cucsVnicIpV4MgmtPooledAddrTable": cucsVnicIpV4MgmtPooledAddrTable,
       "cucsVnicIpV4MgmtPooledAddrEntry": cucsVnicIpV4MgmtPooledAddrEntry,
       "cucsVnicIpV4MgmtPooledAddrInstanceId": cucsVnicIpV4MgmtPooledAddrInstanceId,
       "cucsVnicIpV4MgmtPooledAddrDn": cucsVnicIpV4MgmtPooledAddrDn,
       "cucsVnicIpV4MgmtPooledAddrRn": cucsVnicIpV4MgmtPooledAddrRn,
       "cucsVnicIpV4MgmtPooledAddrAddr": cucsVnicIpV4MgmtPooledAddrAddr,
       "cucsVnicIpV4MgmtPooledAddrDefGw": cucsVnicIpV4MgmtPooledAddrDefGw,
       "cucsVnicIpV4MgmtPooledAddrName": cucsVnicIpV4MgmtPooledAddrName,
       "cucsVnicIpV4MgmtPooledAddrOperName": cucsVnicIpV4MgmtPooledAddrOperName,
       "cucsVnicIpV4MgmtPooledAddrSubnet": cucsVnicIpV4MgmtPooledAddrSubnet,
       "cucsVnicIpV4MgmtPooledAddrPrimDns": cucsVnicIpV4MgmtPooledAddrPrimDns,
       "cucsVnicIpV4MgmtPooledAddrSecDns": cucsVnicIpV4MgmtPooledAddrSecDns,
       "cucsVnicIpV6MgmtPooledAddrTable": cucsVnicIpV6MgmtPooledAddrTable,
       "cucsVnicIpV6MgmtPooledAddrEntry": cucsVnicIpV6MgmtPooledAddrEntry,
       "cucsVnicIpV6MgmtPooledAddrInstanceId": cucsVnicIpV6MgmtPooledAddrInstanceId,
       "cucsVnicIpV6MgmtPooledAddrDn": cucsVnicIpV6MgmtPooledAddrDn,
       "cucsVnicIpV6MgmtPooledAddrRn": cucsVnicIpV6MgmtPooledAddrRn,
       "cucsVnicIpV6MgmtPooledAddrAddr": cucsVnicIpV6MgmtPooledAddrAddr,
       "cucsVnicIpV6MgmtPooledAddrDefGw": cucsVnicIpV6MgmtPooledAddrDefGw,
       "cucsVnicIpV6MgmtPooledAddrName": cucsVnicIpV6MgmtPooledAddrName,
       "cucsVnicIpV6MgmtPooledAddrOperName": cucsVnicIpV6MgmtPooledAddrOperName,
       "cucsVnicIpV6MgmtPooledAddrPrefix": cucsVnicIpV6MgmtPooledAddrPrefix,
       "cucsVnicIpV6MgmtPooledAddrPrimDns": cucsVnicIpV6MgmtPooledAddrPrimDns,
       "cucsVnicIpV6MgmtPooledAddrSecDns": cucsVnicIpV6MgmtPooledAddrSecDns,
       "cucsVnicIpV6StaticAddrTable": cucsVnicIpV6StaticAddrTable,
       "cucsVnicIpV6StaticAddrEntry": cucsVnicIpV6StaticAddrEntry,
       "cucsVnicIpV6StaticAddrInstanceId": cucsVnicIpV6StaticAddrInstanceId,
       "cucsVnicIpV6StaticAddrDn": cucsVnicIpV6StaticAddrDn,
       "cucsVnicIpV6StaticAddrRn": cucsVnicIpV6StaticAddrRn,
       "cucsVnicIpV6StaticAddrAddr": cucsVnicIpV6StaticAddrAddr,
       "cucsVnicIpV6StaticAddrDefGw": cucsVnicIpV6StaticAddrDefGw,
       "cucsVnicIpV6StaticAddrPrefix": cucsVnicIpV6StaticAddrPrefix,
       "cucsVnicIpV6StaticAddrPrimDns": cucsVnicIpV6StaticAddrPrimDns,
       "cucsVnicIpV6StaticAddrSecDns": cucsVnicIpV6StaticAddrSecDns,
       "cucsVnicProfileRefTable": cucsVnicProfileRefTable,
       "cucsVnicProfileRefEntry": cucsVnicProfileRefEntry,
       "cucsVnicProfileRefInstanceId": cucsVnicProfileRefInstanceId,
       "cucsVnicProfileRefDn": cucsVnicProfileRefDn,
       "cucsVnicProfileRefRn": cucsVnicProfileRefRn,
       "cucsVnicProfileRefName": cucsVnicProfileRefName,
       "cucsVnicProfileRefSourceDn": cucsVnicProfileRefSourceDn,
       "cucsVnicUsnicConPolicyTable": cucsVnicUsnicConPolicyTable,
       "cucsVnicUsnicConPolicyEntry": cucsVnicUsnicConPolicyEntry,
       "cucsVnicUsnicConPolicyInstanceId": cucsVnicUsnicConPolicyInstanceId,
       "cucsVnicUsnicConPolicyDn": cucsVnicUsnicConPolicyDn,
       "cucsVnicUsnicConPolicyRn": cucsVnicUsnicConPolicyRn,
       "cucsVnicUsnicConPolicyAdaptorProfileName": cucsVnicUsnicConPolicyAdaptorProfileName,
       "cucsVnicUsnicConPolicyDescr": cucsVnicUsnicConPolicyDescr,
       "cucsVnicUsnicConPolicyIntId": cucsVnicUsnicConPolicyIntId,
       "cucsVnicUsnicConPolicyName": cucsVnicUsnicConPolicyName,
       "cucsVnicUsnicConPolicyPolicyLevel": cucsVnicUsnicConPolicyPolicyLevel,
       "cucsVnicUsnicConPolicyPolicyOwner": cucsVnicUsnicConPolicyPolicyOwner,
       "cucsVnicUsnicConPolicyUsnicCount": cucsVnicUsnicConPolicyUsnicCount,
       "cucsVnicUsnicConPolicyRefTable": cucsVnicUsnicConPolicyRefTable,
       "cucsVnicUsnicConPolicyRefEntry": cucsVnicUsnicConPolicyRefEntry,
       "cucsVnicUsnicConPolicyRefInstanceId": cucsVnicUsnicConPolicyRefInstanceId,
       "cucsVnicUsnicConPolicyRefDn": cucsVnicUsnicConPolicyRefDn,
       "cucsVnicUsnicConPolicyRefRn": cucsVnicUsnicConPolicyRefRn,
       "cucsVnicUsnicConPolicyRefConPolicyName": cucsVnicUsnicConPolicyRefConPolicyName,
       "cucsVnicUsnicConPolicyRefOperConPolicyName": cucsVnicUsnicConPolicyRefOperConPolicyName,
       "cucsVnicVmqConPolicyTable": cucsVnicVmqConPolicyTable,
       "cucsVnicVmqConPolicyEntry": cucsVnicVmqConPolicyEntry,
       "cucsVnicVmqConPolicyInstanceId": cucsVnicVmqConPolicyInstanceId,
       "cucsVnicVmqConPolicyDn": cucsVnicVmqConPolicyDn,
       "cucsVnicVmqConPolicyRn": cucsVnicVmqConPolicyRn,
       "cucsVnicVmqConPolicyDescr": cucsVnicVmqConPolicyDescr,
       "cucsVnicVmqConPolicyIntId": cucsVnicVmqConPolicyIntId,
       "cucsVnicVmqConPolicyIntrCount": cucsVnicVmqConPolicyIntrCount,
       "cucsVnicVmqConPolicyName": cucsVnicVmqConPolicyName,
       "cucsVnicVmqConPolicyPolicyLevel": cucsVnicVmqConPolicyPolicyLevel,
       "cucsVnicVmqConPolicyPolicyOwner": cucsVnicVmqConPolicyPolicyOwner,
       "cucsVnicVmqConPolicyVmqCount": cucsVnicVmqConPolicyVmqCount,
       "cucsVnicVmqConPolicyRefTable": cucsVnicVmqConPolicyRefTable,
       "cucsVnicVmqConPolicyRefEntry": cucsVnicVmqConPolicyRefEntry,
       "cucsVnicVmqConPolicyRefInstanceId": cucsVnicVmqConPolicyRefInstanceId,
       "cucsVnicVmqConPolicyRefDn": cucsVnicVmqConPolicyRefDn,
       "cucsVnicVmqConPolicyRefRn": cucsVnicVmqConPolicyRefRn,
       "cucsVnicVmqConPolicyRefConPolicyName": cucsVnicVmqConPolicyRefConPolicyName,
       "cucsVnicVmqConPolicyRefOperConPolicyName": cucsVnicVmqConPolicyRefOperConPolicyName,
       "cucsVnicIpV6HistoryTable": cucsVnicIpV6HistoryTable,
       "cucsVnicIpV6HistoryEntry": cucsVnicIpV6HistoryEntry,
       "cucsVnicIpV6HistoryInstanceId": cucsVnicIpV6HistoryInstanceId,
       "cucsVnicIpV6HistoryDn": cucsVnicIpV6HistoryDn,
       "cucsVnicIpV6HistoryRn": cucsVnicIpV6HistoryRn,
       "cucsVnicIpV6HistoryOldIpV6Addr": cucsVnicIpV6HistoryOldIpV6Addr,
       "cucsVnicEthConfigTable": cucsVnicEthConfigTable,
       "cucsVnicEthConfigEntry": cucsVnicEthConfigEntry,
       "cucsVnicEthConfigInstanceId": cucsVnicEthConfigInstanceId,
       "cucsVnicEthConfigDn": cucsVnicEthConfigDn,
       "cucsVnicEthConfigRn": cucsVnicEthConfigRn,
       "cucsVnicEthConfigAdaptorProfileName": cucsVnicEthConfigAdaptorProfileName,
       "cucsVnicEthConfigMacPoolName": cucsVnicEthConfigMacPoolName,
       "cucsVnicEthConfigNwCtrlPolicyName": cucsVnicEthConfigNwCtrlPolicyName,
       "cucsVnicEthConfigOperAdaptorProfileName": cucsVnicEthConfigOperAdaptorProfileName,
       "cucsVnicEthConfigOperMacPoolName": cucsVnicEthConfigOperMacPoolName,
       "cucsVnicEthConfigOperNwCtrlPolicyName": cucsVnicEthConfigOperNwCtrlPolicyName,
       "cucsVnicEthConfigOperStatsPolicyName": cucsVnicEthConfigOperStatsPolicyName,
       "cucsVnicEthConfigStatsPolicyName": cucsVnicEthConfigStatsPolicyName,
       "cucsVnicIPv6IfTable": cucsVnicIPv6IfTable,
       "cucsVnicIPv6IfEntry": cucsVnicIPv6IfEntry,
       "cucsVnicIPv6IfInstanceId": cucsVnicIPv6IfInstanceId,
       "cucsVnicIPv6IfDn": cucsVnicIPv6IfDn,
       "cucsVnicIPv6IfRn": cucsVnicIPv6IfRn,
       "cucsVnicIPv6IfAddr": cucsVnicIPv6IfAddr,
       "cucsVnicIPv6IfConfigQualifier": cucsVnicIPv6IfConfigQualifier,
       "cucsVnicIPv6IfName": cucsVnicIPv6IfName,
       "cucsVnicIPv6IfOperState": cucsVnicIPv6IfOperState,
       "cucsVnicIPv6IfOperVnetDn": cucsVnicIPv6IfOperVnetDn,
       "cucsVnicIPv6IfOperVnetName": cucsVnicIPv6IfOperVnetName,
       "cucsVnicIPv6IfOwner": cucsVnicIPv6IfOwner,
       "cucsVnicIPv6IfPubNwId": cucsVnicIPv6IfPubNwId,
       "cucsVnicIPv6IfSharing": cucsVnicIPv6IfSharing,
       "cucsVnicIPv6IfSwitchId": cucsVnicIPv6IfSwitchId,
       "cucsVnicIPv6IfType": cucsVnicIPv6IfType,
       "cucsVnicIPv6IfVnet": cucsVnicIPv6IfVnet,
       "cucsVnicIPv6IfOperPrimaryVnetDn": cucsVnicIPv6IfOperPrimaryVnetDn,
       "cucsVnicIPv6IfOperPrimaryVnetName": cucsVnicIPv6IfOperPrimaryVnetName,
       "cucsVnicIScsiConfigTable": cucsVnicIScsiConfigTable,
       "cucsVnicIScsiConfigEntry": cucsVnicIScsiConfigEntry,
       "cucsVnicIScsiConfigInstanceId": cucsVnicIScsiConfigInstanceId,
       "cucsVnicIScsiConfigDn": cucsVnicIScsiConfigDn,
       "cucsVnicIScsiConfigRn": cucsVnicIScsiConfigRn,
       "cucsVnicIScsiConfigAdaptorProfileName": cucsVnicIScsiConfigAdaptorProfileName,
       "cucsVnicIScsiConfigIpPoolName": cucsVnicIScsiConfigIpPoolName,
       "cucsVnicIScsiConfigIpPoolNameFabricB": cucsVnicIScsiConfigIpPoolNameFabricB,
       "cucsVnicIScsiConfigIpPoolType": cucsVnicIScsiConfigIpPoolType,
       "cucsVnicIScsiConfigIqnPoolName": cucsVnicIScsiConfigIqnPoolName,
       "cucsVnicIScsiConfigOperAdaptorProfileName": cucsVnicIScsiConfigOperAdaptorProfileName,
       "cucsVnicIScsiConfigOperIpPoolName": cucsVnicIScsiConfigOperIpPoolName,
       "cucsVnicIScsiConfigOperIpPoolNameFabricB": cucsVnicIScsiConfigOperIpPoolNameFabricB,
       "cucsVnicIScsiConfigOperIqnPoolName": cucsVnicIScsiConfigOperIqnPoolName,
       "cucsVnicIScsiInitAutoConfigPolicyTable": cucsVnicIScsiInitAutoConfigPolicyTable,
       "cucsVnicIScsiInitAutoConfigPolicyEntry": cucsVnicIScsiInitAutoConfigPolicyEntry,
       "cucsVnicIScsiInitAutoConfigPolicyInstanceId": cucsVnicIScsiInitAutoConfigPolicyInstanceId,
       "cucsVnicIScsiInitAutoConfigPolicyDn": cucsVnicIScsiInitAutoConfigPolicyDn,
       "cucsVnicIScsiInitAutoConfigPolicyRn": cucsVnicIScsiInitAutoConfigPolicyRn,
       "cucsVnicIScsiInitAutoConfigPolicyDescr": cucsVnicIScsiInitAutoConfigPolicyDescr,
       "cucsVnicIScsiInitAutoConfigPolicyFabricPath": cucsVnicIScsiInitAutoConfigPolicyFabricPath,
       "cucsVnicIScsiInitAutoConfigPolicyIntId": cucsVnicIScsiInitAutoConfigPolicyIntId,
       "cucsVnicIScsiInitAutoConfigPolicyName": cucsVnicIScsiInitAutoConfigPolicyName,
       "cucsVnicIScsiInitAutoConfigPolicyPolicyLevel": cucsVnicIScsiInitAutoConfigPolicyPolicyLevel,
       "cucsVnicIScsiInitAutoConfigPolicyPolicyOwner": cucsVnicIScsiInitAutoConfigPolicyPolicyOwner}
)
