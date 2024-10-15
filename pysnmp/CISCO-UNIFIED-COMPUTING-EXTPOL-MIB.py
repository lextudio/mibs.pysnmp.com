# SNMP MIB module (CISCO-UNIFIED-COMPUTING-EXTPOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-EXTPOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:26 2024
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
 CucsExtpolAppCapability,
 CucsExtpolConnProtocol,
 CucsExtpolConnType,
 CucsExtpolConnectorOperState,
 CucsExtpolEpFsmCurrentFsm,
 CucsExtpolEpFsmStageName,
 CucsExtpolEpFsmTaskItem,
 CucsExtpolProviderFsmCurrentFsm,
 CucsExtpolProviderFsmStageName,
 CucsExtpolProviderFsmTaskItem,
 CucsExtpolRegistryFsmCurrentFsm,
 CucsExtpolRegistryFsmStageName,
 CucsExtpolRegistryFsmTaskItem,
 CucsExtpolState,
 CucsExtpolSuspendState,
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsExtpolAppCapability",
    "CucsExtpolConnProtocol",
    "CucsExtpolConnType",
    "CucsExtpolConnectorOperState",
    "CucsExtpolEpFsmCurrentFsm",
    "CucsExtpolEpFsmStageName",
    "CucsExtpolEpFsmTaskItem",
    "CucsExtpolProviderFsmCurrentFsm",
    "CucsExtpolProviderFsmStageName",
    "CucsExtpolProviderFsmTaskItem",
    "CucsExtpolRegistryFsmCurrentFsm",
    "CucsExtpolRegistryFsmStageName",
    "CucsExtpolRegistryFsmTaskItem",
    "CucsExtpolState",
    "CucsExtpolSuspendState",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus")

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

cucsExtpolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsExtpolClientTable_Object = MibTable
cucsExtpolClientTable = _CucsExtpolClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1)
)
if mibBuilder.loadTexts:
    cucsExtpolClientTable.setStatus("current")
_CucsExtpolClientEntry_Object = MibTableRow
cucsExtpolClientEntry = _CucsExtpolClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1)
)
cucsExtpolClientEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolClientInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolClientEntry.setStatus("current")
_CucsExtpolClientInstanceId_Type = CucsManagedObjectId
_CucsExtpolClientInstanceId_Object = MibTableColumn
cucsExtpolClientInstanceId = _CucsExtpolClientInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 1),
    _CucsExtpolClientInstanceId_Type()
)
cucsExtpolClientInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolClientInstanceId.setStatus("current")
_CucsExtpolClientDn_Type = CucsManagedObjectDn
_CucsExtpolClientDn_Object = MibTableColumn
cucsExtpolClientDn = _CucsExtpolClientDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 2),
    _CucsExtpolClientDn_Type()
)
cucsExtpolClientDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientDn.setStatus("current")
_CucsExtpolClientRn_Type = SnmpAdminString
_CucsExtpolClientRn_Object = MibTableColumn
cucsExtpolClientRn = _CucsExtpolClientRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 3),
    _CucsExtpolClientRn_Type()
)
cucsExtpolClientRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientRn.setStatus("current")
_CucsExtpolClientCapability_Type = CucsExtpolAppCapability
_CucsExtpolClientCapability_Object = MibTableColumn
cucsExtpolClientCapability = _CucsExtpolClientCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 4),
    _CucsExtpolClientCapability_Type()
)
cucsExtpolClientCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientCapability.setStatus("current")
_CucsExtpolClientDescr_Type = SnmpAdminString
_CucsExtpolClientDescr_Object = MibTableColumn
cucsExtpolClientDescr = _CucsExtpolClientDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 5),
    _CucsExtpolClientDescr_Type()
)
cucsExtpolClientDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientDescr.setStatus("current")
_CucsExtpolClientGuid_Type = SnmpAdminString
_CucsExtpolClientGuid_Object = MibTableColumn
cucsExtpolClientGuid = _CucsExtpolClientGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 6),
    _CucsExtpolClientGuid_Type()
)
cucsExtpolClientGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientGuid.setStatus("current")
_CucsExtpolClientHost_Type = SnmpAdminString
_CucsExtpolClientHost_Object = MibTableColumn
cucsExtpolClientHost = _CucsExtpolClientHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 7),
    _CucsExtpolClientHost_Type()
)
cucsExtpolClientHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientHost.setStatus("current")
_CucsExtpolClientId_Type = Gauge32
_CucsExtpolClientId_Object = MibTableColumn
cucsExtpolClientId = _CucsExtpolClientId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 8),
    _CucsExtpolClientId_Type()
)
cucsExtpolClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientId.setStatus("current")
_CucsExtpolClientInterest_Type = CucsExtpolAppCapability
_CucsExtpolClientInterest_Object = MibTableColumn
cucsExtpolClientInterest = _CucsExtpolClientInterest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 9),
    _CucsExtpolClientInterest_Type()
)
cucsExtpolClientInterest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientInterest.setStatus("current")
_CucsExtpolClientIp_Type = InetAddressIPv4
_CucsExtpolClientIp_Object = MibTableColumn
cucsExtpolClientIp = _CucsExtpolClientIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 10),
    _CucsExtpolClientIp_Type()
)
cucsExtpolClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientIp.setStatus("current")
_CucsExtpolClientLastPollTs_Type = DateAndTime
_CucsExtpolClientLastPollTs_Object = MibTableColumn
cucsExtpolClientLastPollTs = _CucsExtpolClientLastPollTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 11),
    _CucsExtpolClientLastPollTs_Type()
)
cucsExtpolClientLastPollTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientLastPollTs.setStatus("current")
_CucsExtpolClientName_Type = SnmpAdminString
_CucsExtpolClientName_Object = MibTableColumn
cucsExtpolClientName = _CucsExtpolClientName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 12),
    _CucsExtpolClientName_Type()
)
cucsExtpolClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientName.setStatus("current")
_CucsExtpolClientOperState_Type = CucsExtpolConnectorOperState
_CucsExtpolClientOperState_Object = MibTableColumn
cucsExtpolClientOperState = _CucsExtpolClientOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 13),
    _CucsExtpolClientOperState_Type()
)
cucsExtpolClientOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientOperState.setStatus("current")
_CucsExtpolClientOwner_Type = SnmpAdminString
_CucsExtpolClientOwner_Object = MibTableColumn
cucsExtpolClientOwner = _CucsExtpolClientOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 14),
    _CucsExtpolClientOwner_Type()
)
cucsExtpolClientOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientOwner.setStatus("current")
_CucsExtpolClientSite_Type = SnmpAdminString
_CucsExtpolClientSite_Object = MibTableColumn
cucsExtpolClientSite = _CucsExtpolClientSite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 15),
    _CucsExtpolClientSite_Type()
)
cucsExtpolClientSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientSite.setStatus("current")
_CucsExtpolClientSuspendState_Type = CucsExtpolSuspendState
_CucsExtpolClientSuspendState_Object = MibTableColumn
cucsExtpolClientSuspendState = _CucsExtpolClientSuspendState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 16),
    _CucsExtpolClientSuspendState_Type()
)
cucsExtpolClientSuspendState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientSuspendState.setStatus("current")
_CucsExtpolClientType_Type = CucsExtpolConnType
_CucsExtpolClientType_Object = MibTableColumn
cucsExtpolClientType = _CucsExtpolClientType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 17),
    _CucsExtpolClientType_Type()
)
cucsExtpolClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientType.setStatus("current")
_CucsExtpolClientVersion_Type = SnmpAdminString
_CucsExtpolClientVersion_Object = MibTableColumn
cucsExtpolClientVersion = _CucsExtpolClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 18),
    _CucsExtpolClientVersion_Type()
)
cucsExtpolClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientVersion.setStatus("current")
_CucsExtpolClientGracePeriodUsed_Type = Unsigned64
_CucsExtpolClientGracePeriodUsed_Object = MibTableColumn
cucsExtpolClientGracePeriodUsed = _CucsExtpolClientGracePeriodUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 19),
    _CucsExtpolClientGracePeriodUsed_Type()
)
cucsExtpolClientGracePeriodUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientGracePeriodUsed.setStatus("current")
_CucsExtpolClientLicState_Type = CucsExtpolState
_CucsExtpolClientLicState_Object = MibTableColumn
cucsExtpolClientLicState = _CucsExtpolClientLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 20),
    _CucsExtpolClientLicState_Type()
)
cucsExtpolClientLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientLicState.setStatus("current")
_CucsExtpolClientConnProtocol_Type = CucsExtpolConnProtocol
_CucsExtpolClientConnProtocol_Object = MibTableColumn
cucsExtpolClientConnProtocol = _CucsExtpolClientConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 21),
    _CucsExtpolClientConnProtocol_Type()
)
cucsExtpolClientConnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientConnProtocol.setStatus("current")
_CucsExtpolClientIpv6_Type = InetAddressIPv6
_CucsExtpolClientIpv6_Object = MibTableColumn
cucsExtpolClientIpv6 = _CucsExtpolClientIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 1, 1, 22),
    _CucsExtpolClientIpv6_Type()
)
cucsExtpolClientIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientIpv6.setStatus("current")
_CucsExtpolClientContTable_Object = MibTable
cucsExtpolClientContTable = _CucsExtpolClientContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 2)
)
if mibBuilder.loadTexts:
    cucsExtpolClientContTable.setStatus("current")
_CucsExtpolClientContEntry_Object = MibTableRow
cucsExtpolClientContEntry = _CucsExtpolClientContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 2, 1)
)
cucsExtpolClientContEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolClientContInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolClientContEntry.setStatus("current")
_CucsExtpolClientContInstanceId_Type = CucsManagedObjectId
_CucsExtpolClientContInstanceId_Object = MibTableColumn
cucsExtpolClientContInstanceId = _CucsExtpolClientContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 2, 1, 1),
    _CucsExtpolClientContInstanceId_Type()
)
cucsExtpolClientContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolClientContInstanceId.setStatus("current")
_CucsExtpolClientContDn_Type = CucsManagedObjectDn
_CucsExtpolClientContDn_Object = MibTableColumn
cucsExtpolClientContDn = _CucsExtpolClientContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 2, 1, 2),
    _CucsExtpolClientContDn_Type()
)
cucsExtpolClientContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientContDn.setStatus("current")
_CucsExtpolClientContRn_Type = SnmpAdminString
_CucsExtpolClientContRn_Object = MibTableColumn
cucsExtpolClientContRn = _CucsExtpolClientContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 2, 1, 3),
    _CucsExtpolClientContRn_Type()
)
cucsExtpolClientContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientContRn.setStatus("current")
_CucsExtpolClientContGenNum_Type = Gauge32
_CucsExtpolClientContGenNum_Object = MibTableColumn
cucsExtpolClientContGenNum = _CucsExtpolClientContGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 2, 1, 4),
    _CucsExtpolClientContGenNum_Type()
)
cucsExtpolClientContGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolClientContGenNum.setStatus("current")
_CucsExtpolControllerTable_Object = MibTable
cucsExtpolControllerTable = _CucsExtpolControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 3)
)
if mibBuilder.loadTexts:
    cucsExtpolControllerTable.setStatus("current")
_CucsExtpolControllerEntry_Object = MibTableRow
cucsExtpolControllerEntry = _CucsExtpolControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 3, 1)
)
cucsExtpolControllerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolControllerEntry.setStatus("current")
_CucsExtpolControllerInstanceId_Type = CucsManagedObjectId
_CucsExtpolControllerInstanceId_Object = MibTableColumn
cucsExtpolControllerInstanceId = _CucsExtpolControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 3, 1, 1),
    _CucsExtpolControllerInstanceId_Type()
)
cucsExtpolControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolControllerInstanceId.setStatus("current")
_CucsExtpolControllerDn_Type = CucsManagedObjectDn
_CucsExtpolControllerDn_Object = MibTableColumn
cucsExtpolControllerDn = _CucsExtpolControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 3, 1, 2),
    _CucsExtpolControllerDn_Type()
)
cucsExtpolControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolControllerDn.setStatus("current")
_CucsExtpolControllerRn_Type = SnmpAdminString
_CucsExtpolControllerRn_Object = MibTableColumn
cucsExtpolControllerRn = _CucsExtpolControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 3, 1, 3),
    _CucsExtpolControllerRn_Type()
)
cucsExtpolControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolControllerRn.setStatus("current")
_CucsExtpolControllerCapability_Type = CucsExtpolAppCapability
_CucsExtpolControllerCapability_Object = MibTableColumn
cucsExtpolControllerCapability = _CucsExtpolControllerCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 3, 1, 4),
    _CucsExtpolControllerCapability_Type()
)
cucsExtpolControllerCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolControllerCapability.setStatus("current")
_CucsExtpolControllerHost_Type = SnmpAdminString
_CucsExtpolControllerHost_Object = MibTableColumn
cucsExtpolControllerHost = _CucsExtpolControllerHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 3, 1, 5),
    _CucsExtpolControllerHost_Type()
)
cucsExtpolControllerHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolControllerHost.setStatus("current")
_CucsExtpolControllerId_Type = Gauge32
_CucsExtpolControllerId_Object = MibTableColumn
cucsExtpolControllerId = _CucsExtpolControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 3, 1, 6),
    _CucsExtpolControllerId_Type()
)
cucsExtpolControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolControllerId.setStatus("current")
_CucsExtpolControllerInterest_Type = CucsExtpolAppCapability
_CucsExtpolControllerInterest_Object = MibTableColumn
cucsExtpolControllerInterest = _CucsExtpolControllerInterest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 3, 1, 7),
    _CucsExtpolControllerInterest_Type()
)
cucsExtpolControllerInterest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolControllerInterest.setStatus("current")
_CucsExtpolControllerIp_Type = InetAddressIPv4
_CucsExtpolControllerIp_Object = MibTableColumn
cucsExtpolControllerIp = _CucsExtpolControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 3, 1, 8),
    _CucsExtpolControllerIp_Type()
)
cucsExtpolControllerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolControllerIp.setStatus("current")
_CucsExtpolControllerLastPollTs_Type = DateAndTime
_CucsExtpolControllerLastPollTs_Object = MibTableColumn
cucsExtpolControllerLastPollTs = _CucsExtpolControllerLastPollTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 3, 1, 9),
    _CucsExtpolControllerLastPollTs_Type()
)
cucsExtpolControllerLastPollTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolControllerLastPollTs.setStatus("current")
_CucsExtpolControllerName_Type = SnmpAdminString
_CucsExtpolControllerName_Object = MibTableColumn
cucsExtpolControllerName = _CucsExtpolControllerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 3, 1, 10),
    _CucsExtpolControllerName_Type()
)
cucsExtpolControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolControllerName.setStatus("current")
_CucsExtpolControllerOperState_Type = CucsExtpolConnectorOperState
_CucsExtpolControllerOperState_Object = MibTableColumn
cucsExtpolControllerOperState = _CucsExtpolControllerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 3, 1, 11),
    _CucsExtpolControllerOperState_Type()
)
cucsExtpolControllerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolControllerOperState.setStatus("current")
_CucsExtpolControllerType_Type = CucsExtpolConnType
_CucsExtpolControllerType_Object = MibTableColumn
cucsExtpolControllerType = _CucsExtpolControllerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 3, 1, 12),
    _CucsExtpolControllerType_Type()
)
cucsExtpolControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolControllerType.setStatus("current")
_CucsExtpolControllerVersion_Type = SnmpAdminString
_CucsExtpolControllerVersion_Object = MibTableColumn
cucsExtpolControllerVersion = _CucsExtpolControllerVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 3, 1, 13),
    _CucsExtpolControllerVersion_Type()
)
cucsExtpolControllerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolControllerVersion.setStatus("current")
_CucsExtpolControllerConnProtocol_Type = CucsExtpolConnProtocol
_CucsExtpolControllerConnProtocol_Object = MibTableColumn
cucsExtpolControllerConnProtocol = _CucsExtpolControllerConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 3, 1, 14),
    _CucsExtpolControllerConnProtocol_Type()
)
cucsExtpolControllerConnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolControllerConnProtocol.setStatus("current")
_CucsExtpolControllerIpv6_Type = InetAddressIPv6
_CucsExtpolControllerIpv6_Object = MibTableColumn
cucsExtpolControllerIpv6 = _CucsExtpolControllerIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 3, 1, 15),
    _CucsExtpolControllerIpv6_Type()
)
cucsExtpolControllerIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolControllerIpv6.setStatus("current")
_CucsExtpolControllerContTable_Object = MibTable
cucsExtpolControllerContTable = _CucsExtpolControllerContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 4)
)
if mibBuilder.loadTexts:
    cucsExtpolControllerContTable.setStatus("current")
_CucsExtpolControllerContEntry_Object = MibTableRow
cucsExtpolControllerContEntry = _CucsExtpolControllerContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 4, 1)
)
cucsExtpolControllerContEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolControllerContInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolControllerContEntry.setStatus("current")
_CucsExtpolControllerContInstanceId_Type = CucsManagedObjectId
_CucsExtpolControllerContInstanceId_Object = MibTableColumn
cucsExtpolControllerContInstanceId = _CucsExtpolControllerContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 4, 1, 1),
    _CucsExtpolControllerContInstanceId_Type()
)
cucsExtpolControllerContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolControllerContInstanceId.setStatus("current")
_CucsExtpolControllerContDn_Type = CucsManagedObjectDn
_CucsExtpolControllerContDn_Object = MibTableColumn
cucsExtpolControllerContDn = _CucsExtpolControllerContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 4, 1, 2),
    _CucsExtpolControllerContDn_Type()
)
cucsExtpolControllerContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolControllerContDn.setStatus("current")
_CucsExtpolControllerContRn_Type = SnmpAdminString
_CucsExtpolControllerContRn_Object = MibTableColumn
cucsExtpolControllerContRn = _CucsExtpolControllerContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 4, 1, 3),
    _CucsExtpolControllerContRn_Type()
)
cucsExtpolControllerContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolControllerContRn.setStatus("current")
_CucsExtpolControllerContGenNum_Type = Gauge32
_CucsExtpolControllerContGenNum_Object = MibTableColumn
cucsExtpolControllerContGenNum = _CucsExtpolControllerContGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 4, 1, 4),
    _CucsExtpolControllerContGenNum_Type()
)
cucsExtpolControllerContGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolControllerContGenNum.setStatus("current")
_CucsExtpolEpTable_Object = MibTable
cucsExtpolEpTable = _CucsExtpolEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 5)
)
if mibBuilder.loadTexts:
    cucsExtpolEpTable.setStatus("current")
_CucsExtpolEpEntry_Object = MibTableRow
cucsExtpolEpEntry = _CucsExtpolEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 5, 1)
)
cucsExtpolEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolEpEntry.setStatus("current")
_CucsExtpolEpInstanceId_Type = CucsManagedObjectId
_CucsExtpolEpInstanceId_Object = MibTableColumn
cucsExtpolEpInstanceId = _CucsExtpolEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 5, 1, 1),
    _CucsExtpolEpInstanceId_Type()
)
cucsExtpolEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolEpInstanceId.setStatus("current")
_CucsExtpolEpDn_Type = CucsManagedObjectDn
_CucsExtpolEpDn_Object = MibTableColumn
cucsExtpolEpDn = _CucsExtpolEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 5, 1, 2),
    _CucsExtpolEpDn_Type()
)
cucsExtpolEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpDn.setStatus("current")
_CucsExtpolEpRn_Type = SnmpAdminString
_CucsExtpolEpRn_Object = MibTableColumn
cucsExtpolEpRn = _CucsExtpolEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 5, 1, 3),
    _CucsExtpolEpRn_Type()
)
cucsExtpolEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpRn.setStatus("current")
_CucsExtpolEpFsmDescr_Type = SnmpAdminString
_CucsExtpolEpFsmDescr_Object = MibTableColumn
cucsExtpolEpFsmDescr = _CucsExtpolEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 5, 1, 4),
    _CucsExtpolEpFsmDescr_Type()
)
cucsExtpolEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmDescr.setStatus("current")
_CucsExtpolEpFsmPrev_Type = SnmpAdminString
_CucsExtpolEpFsmPrev_Object = MibTableColumn
cucsExtpolEpFsmPrev = _CucsExtpolEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 5, 1, 5),
    _CucsExtpolEpFsmPrev_Type()
)
cucsExtpolEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmPrev.setStatus("current")
_CucsExtpolEpFsmProgr_Type = Gauge32
_CucsExtpolEpFsmProgr_Object = MibTableColumn
cucsExtpolEpFsmProgr = _CucsExtpolEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 5, 1, 6),
    _CucsExtpolEpFsmProgr_Type()
)
cucsExtpolEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmProgr.setStatus("current")
_CucsExtpolEpFsmRmtInvErrCode_Type = Gauge32
_CucsExtpolEpFsmRmtInvErrCode_Object = MibTableColumn
cucsExtpolEpFsmRmtInvErrCode = _CucsExtpolEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 5, 1, 7),
    _CucsExtpolEpFsmRmtInvErrCode_Type()
)
cucsExtpolEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmRmtInvErrCode.setStatus("current")
_CucsExtpolEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsExtpolEpFsmRmtInvErrDescr_Object = MibTableColumn
cucsExtpolEpFsmRmtInvErrDescr = _CucsExtpolEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 5, 1, 8),
    _CucsExtpolEpFsmRmtInvErrDescr_Type()
)
cucsExtpolEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmRmtInvErrDescr.setStatus("current")
_CucsExtpolEpFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsExtpolEpFsmRmtInvRslt_Object = MibTableColumn
cucsExtpolEpFsmRmtInvRslt = _CucsExtpolEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 5, 1, 9),
    _CucsExtpolEpFsmRmtInvRslt_Type()
)
cucsExtpolEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmRmtInvRslt.setStatus("current")
_CucsExtpolEpFsmStageDescr_Type = SnmpAdminString
_CucsExtpolEpFsmStageDescr_Object = MibTableColumn
cucsExtpolEpFsmStageDescr = _CucsExtpolEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 5, 1, 10),
    _CucsExtpolEpFsmStageDescr_Type()
)
cucsExtpolEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmStageDescr.setStatus("current")
_CucsExtpolEpFsmStamp_Type = DateAndTime
_CucsExtpolEpFsmStamp_Object = MibTableColumn
cucsExtpolEpFsmStamp = _CucsExtpolEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 5, 1, 11),
    _CucsExtpolEpFsmStamp_Type()
)
cucsExtpolEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmStamp.setStatus("current")
_CucsExtpolEpFsmStatus_Type = SnmpAdminString
_CucsExtpolEpFsmStatus_Object = MibTableColumn
cucsExtpolEpFsmStatus = _CucsExtpolEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 5, 1, 12),
    _CucsExtpolEpFsmStatus_Type()
)
cucsExtpolEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmStatus.setStatus("current")
_CucsExtpolEpFsmTry_Type = Gauge32
_CucsExtpolEpFsmTry_Object = MibTableColumn
cucsExtpolEpFsmTry = _CucsExtpolEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 5, 1, 13),
    _CucsExtpolEpFsmTry_Type()
)
cucsExtpolEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmTry.setStatus("current")
_CucsExtpolEpFsmTable_Object = MibTable
cucsExtpolEpFsmTable = _CucsExtpolEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 6)
)
if mibBuilder.loadTexts:
    cucsExtpolEpFsmTable.setStatus("current")
_CucsExtpolEpFsmEntry_Object = MibTableRow
cucsExtpolEpFsmEntry = _CucsExtpolEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 6, 1)
)
cucsExtpolEpFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolEpFsmEntry.setStatus("current")
_CucsExtpolEpFsmInstanceId_Type = CucsManagedObjectId
_CucsExtpolEpFsmInstanceId_Object = MibTableColumn
cucsExtpolEpFsmInstanceId = _CucsExtpolEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 6, 1, 1),
    _CucsExtpolEpFsmInstanceId_Type()
)
cucsExtpolEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmInstanceId.setStatus("current")
_CucsExtpolEpFsmDn_Type = CucsManagedObjectDn
_CucsExtpolEpFsmDn_Object = MibTableColumn
cucsExtpolEpFsmDn = _CucsExtpolEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 6, 1, 2),
    _CucsExtpolEpFsmDn_Type()
)
cucsExtpolEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmDn.setStatus("current")
_CucsExtpolEpFsmRn_Type = SnmpAdminString
_CucsExtpolEpFsmRn_Object = MibTableColumn
cucsExtpolEpFsmRn = _CucsExtpolEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 6, 1, 3),
    _CucsExtpolEpFsmRn_Type()
)
cucsExtpolEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmRn.setStatus("current")
_CucsExtpolEpFsmCompletionTime_Type = DateAndTime
_CucsExtpolEpFsmCompletionTime_Object = MibTableColumn
cucsExtpolEpFsmCompletionTime = _CucsExtpolEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 6, 1, 4),
    _CucsExtpolEpFsmCompletionTime_Type()
)
cucsExtpolEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmCompletionTime.setStatus("current")
_CucsExtpolEpFsmCurrentFsm_Type = CucsExtpolEpFsmCurrentFsm
_CucsExtpolEpFsmCurrentFsm_Object = MibTableColumn
cucsExtpolEpFsmCurrentFsm = _CucsExtpolEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 6, 1, 5),
    _CucsExtpolEpFsmCurrentFsm_Type()
)
cucsExtpolEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmCurrentFsm.setStatus("current")
_CucsExtpolEpFsmDescrData_Type = SnmpAdminString
_CucsExtpolEpFsmDescrData_Object = MibTableColumn
cucsExtpolEpFsmDescrData = _CucsExtpolEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 6, 1, 6),
    _CucsExtpolEpFsmDescrData_Type()
)
cucsExtpolEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmDescrData.setStatus("current")
_CucsExtpolEpFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsExtpolEpFsmFsmStatus_Object = MibTableColumn
cucsExtpolEpFsmFsmStatus = _CucsExtpolEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 6, 1, 7),
    _CucsExtpolEpFsmFsmStatus_Type()
)
cucsExtpolEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmFsmStatus.setStatus("current")
_CucsExtpolEpFsmProgress_Type = Gauge32
_CucsExtpolEpFsmProgress_Object = MibTableColumn
cucsExtpolEpFsmProgress = _CucsExtpolEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 6, 1, 8),
    _CucsExtpolEpFsmProgress_Type()
)
cucsExtpolEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmProgress.setStatus("current")
_CucsExtpolEpFsmRmtErrCode_Type = Gauge32
_CucsExtpolEpFsmRmtErrCode_Object = MibTableColumn
cucsExtpolEpFsmRmtErrCode = _CucsExtpolEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 6, 1, 9),
    _CucsExtpolEpFsmRmtErrCode_Type()
)
cucsExtpolEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmRmtErrCode.setStatus("current")
_CucsExtpolEpFsmRmtErrDescr_Type = SnmpAdminString
_CucsExtpolEpFsmRmtErrDescr_Object = MibTableColumn
cucsExtpolEpFsmRmtErrDescr = _CucsExtpolEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 6, 1, 10),
    _CucsExtpolEpFsmRmtErrDescr_Type()
)
cucsExtpolEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmRmtErrDescr.setStatus("current")
_CucsExtpolEpFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsExtpolEpFsmRmtRslt_Object = MibTableColumn
cucsExtpolEpFsmRmtRslt = _CucsExtpolEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 6, 1, 11),
    _CucsExtpolEpFsmRmtRslt_Type()
)
cucsExtpolEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmRmtRslt.setStatus("current")
_CucsExtpolEpFsmStageTable_Object = MibTable
cucsExtpolEpFsmStageTable = _CucsExtpolEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 7)
)
if mibBuilder.loadTexts:
    cucsExtpolEpFsmStageTable.setStatus("current")
_CucsExtpolEpFsmStageEntry_Object = MibTableRow
cucsExtpolEpFsmStageEntry = _CucsExtpolEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 7, 1)
)
cucsExtpolEpFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolEpFsmStageEntry.setStatus("current")
_CucsExtpolEpFsmStageInstanceId_Type = CucsManagedObjectId
_CucsExtpolEpFsmStageInstanceId_Object = MibTableColumn
cucsExtpolEpFsmStageInstanceId = _CucsExtpolEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 7, 1, 1),
    _CucsExtpolEpFsmStageInstanceId_Type()
)
cucsExtpolEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmStageInstanceId.setStatus("current")
_CucsExtpolEpFsmStageDn_Type = CucsManagedObjectDn
_CucsExtpolEpFsmStageDn_Object = MibTableColumn
cucsExtpolEpFsmStageDn = _CucsExtpolEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 7, 1, 2),
    _CucsExtpolEpFsmStageDn_Type()
)
cucsExtpolEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmStageDn.setStatus("current")
_CucsExtpolEpFsmStageRn_Type = SnmpAdminString
_CucsExtpolEpFsmStageRn_Object = MibTableColumn
cucsExtpolEpFsmStageRn = _CucsExtpolEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 7, 1, 3),
    _CucsExtpolEpFsmStageRn_Type()
)
cucsExtpolEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmStageRn.setStatus("current")
_CucsExtpolEpFsmStageDescrData_Type = SnmpAdminString
_CucsExtpolEpFsmStageDescrData_Object = MibTableColumn
cucsExtpolEpFsmStageDescrData = _CucsExtpolEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 7, 1, 4),
    _CucsExtpolEpFsmStageDescrData_Type()
)
cucsExtpolEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmStageDescrData.setStatus("current")
_CucsExtpolEpFsmStageLastUpdateTime_Type = DateAndTime
_CucsExtpolEpFsmStageLastUpdateTime_Object = MibTableColumn
cucsExtpolEpFsmStageLastUpdateTime = _CucsExtpolEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 7, 1, 5),
    _CucsExtpolEpFsmStageLastUpdateTime_Type()
)
cucsExtpolEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmStageLastUpdateTime.setStatus("current")
_CucsExtpolEpFsmStageName_Type = CucsExtpolEpFsmStageName
_CucsExtpolEpFsmStageName_Object = MibTableColumn
cucsExtpolEpFsmStageName = _CucsExtpolEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 7, 1, 6),
    _CucsExtpolEpFsmStageName_Type()
)
cucsExtpolEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmStageName.setStatus("current")
_CucsExtpolEpFsmStageOrder_Type = Gauge32
_CucsExtpolEpFsmStageOrder_Object = MibTableColumn
cucsExtpolEpFsmStageOrder = _CucsExtpolEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 7, 1, 7),
    _CucsExtpolEpFsmStageOrder_Type()
)
cucsExtpolEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmStageOrder.setStatus("current")
_CucsExtpolEpFsmStageRetry_Type = Gauge32
_CucsExtpolEpFsmStageRetry_Object = MibTableColumn
cucsExtpolEpFsmStageRetry = _CucsExtpolEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 7, 1, 8),
    _CucsExtpolEpFsmStageRetry_Type()
)
cucsExtpolEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmStageRetry.setStatus("current")
_CucsExtpolEpFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsExtpolEpFsmStageStageStatus_Object = MibTableColumn
cucsExtpolEpFsmStageStageStatus = _CucsExtpolEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 7, 1, 9),
    _CucsExtpolEpFsmStageStageStatus_Type()
)
cucsExtpolEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmStageStageStatus.setStatus("current")
_CucsExtpolEpFsmTaskTable_Object = MibTable
cucsExtpolEpFsmTaskTable = _CucsExtpolEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 8)
)
if mibBuilder.loadTexts:
    cucsExtpolEpFsmTaskTable.setStatus("current")
_CucsExtpolEpFsmTaskEntry_Object = MibTableRow
cucsExtpolEpFsmTaskEntry = _CucsExtpolEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 8, 1)
)
cucsExtpolEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolEpFsmTaskEntry.setStatus("current")
_CucsExtpolEpFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsExtpolEpFsmTaskInstanceId_Object = MibTableColumn
cucsExtpolEpFsmTaskInstanceId = _CucsExtpolEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 8, 1, 1),
    _CucsExtpolEpFsmTaskInstanceId_Type()
)
cucsExtpolEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmTaskInstanceId.setStatus("current")
_CucsExtpolEpFsmTaskDn_Type = CucsManagedObjectDn
_CucsExtpolEpFsmTaskDn_Object = MibTableColumn
cucsExtpolEpFsmTaskDn = _CucsExtpolEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 8, 1, 2),
    _CucsExtpolEpFsmTaskDn_Type()
)
cucsExtpolEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmTaskDn.setStatus("current")
_CucsExtpolEpFsmTaskRn_Type = SnmpAdminString
_CucsExtpolEpFsmTaskRn_Object = MibTableColumn
cucsExtpolEpFsmTaskRn = _CucsExtpolEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 8, 1, 3),
    _CucsExtpolEpFsmTaskRn_Type()
)
cucsExtpolEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmTaskRn.setStatus("current")
_CucsExtpolEpFsmTaskCompletion_Type = CucsFsmCompletion
_CucsExtpolEpFsmTaskCompletion_Object = MibTableColumn
cucsExtpolEpFsmTaskCompletion = _CucsExtpolEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 8, 1, 4),
    _CucsExtpolEpFsmTaskCompletion_Type()
)
cucsExtpolEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmTaskCompletion.setStatus("current")
_CucsExtpolEpFsmTaskFlags_Type = CucsFsmFlags
_CucsExtpolEpFsmTaskFlags_Object = MibTableColumn
cucsExtpolEpFsmTaskFlags = _CucsExtpolEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 8, 1, 5),
    _CucsExtpolEpFsmTaskFlags_Type()
)
cucsExtpolEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmTaskFlags.setStatus("current")
_CucsExtpolEpFsmTaskItem_Type = CucsExtpolEpFsmTaskItem
_CucsExtpolEpFsmTaskItem_Object = MibTableColumn
cucsExtpolEpFsmTaskItem = _CucsExtpolEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 8, 1, 6),
    _CucsExtpolEpFsmTaskItem_Type()
)
cucsExtpolEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmTaskItem.setStatus("current")
_CucsExtpolEpFsmTaskSeqId_Type = Gauge32
_CucsExtpolEpFsmTaskSeqId_Object = MibTableColumn
cucsExtpolEpFsmTaskSeqId = _CucsExtpolEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 8, 1, 7),
    _CucsExtpolEpFsmTaskSeqId_Type()
)
cucsExtpolEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolEpFsmTaskSeqId.setStatus("current")
_CucsExtpolProviderTable_Object = MibTable
cucsExtpolProviderTable = _CucsExtpolProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9)
)
if mibBuilder.loadTexts:
    cucsExtpolProviderTable.setStatus("current")
_CucsExtpolProviderEntry_Object = MibTableRow
cucsExtpolProviderEntry = _CucsExtpolProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1)
)
cucsExtpolProviderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolProviderEntry.setStatus("current")
_CucsExtpolProviderInstanceId_Type = CucsManagedObjectId
_CucsExtpolProviderInstanceId_Object = MibTableColumn
cucsExtpolProviderInstanceId = _CucsExtpolProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 1),
    _CucsExtpolProviderInstanceId_Type()
)
cucsExtpolProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolProviderInstanceId.setStatus("current")
_CucsExtpolProviderDn_Type = CucsManagedObjectDn
_CucsExtpolProviderDn_Object = MibTableColumn
cucsExtpolProviderDn = _CucsExtpolProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 2),
    _CucsExtpolProviderDn_Type()
)
cucsExtpolProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderDn.setStatus("current")
_CucsExtpolProviderRn_Type = SnmpAdminString
_CucsExtpolProviderRn_Object = MibTableColumn
cucsExtpolProviderRn = _CucsExtpolProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 3),
    _CucsExtpolProviderRn_Type()
)
cucsExtpolProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderRn.setStatus("current")
_CucsExtpolProviderCapability_Type = CucsExtpolAppCapability
_CucsExtpolProviderCapability_Object = MibTableColumn
cucsExtpolProviderCapability = _CucsExtpolProviderCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 4),
    _CucsExtpolProviderCapability_Type()
)
cucsExtpolProviderCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderCapability.setStatus("current")
_CucsExtpolProviderHost_Type = SnmpAdminString
_CucsExtpolProviderHost_Object = MibTableColumn
cucsExtpolProviderHost = _CucsExtpolProviderHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 5),
    _CucsExtpolProviderHost_Type()
)
cucsExtpolProviderHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderHost.setStatus("current")
_CucsExtpolProviderId_Type = Gauge32
_CucsExtpolProviderId_Object = MibTableColumn
cucsExtpolProviderId = _CucsExtpolProviderId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 6),
    _CucsExtpolProviderId_Type()
)
cucsExtpolProviderId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderId.setStatus("current")
_CucsExtpolProviderInterest_Type = CucsExtpolAppCapability
_CucsExtpolProviderInterest_Object = MibTableColumn
cucsExtpolProviderInterest = _CucsExtpolProviderInterest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 7),
    _CucsExtpolProviderInterest_Type()
)
cucsExtpolProviderInterest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderInterest.setStatus("current")
_CucsExtpolProviderIp_Type = InetAddressIPv4
_CucsExtpolProviderIp_Object = MibTableColumn
cucsExtpolProviderIp = _CucsExtpolProviderIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 8),
    _CucsExtpolProviderIp_Type()
)
cucsExtpolProviderIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderIp.setStatus("current")
_CucsExtpolProviderLastPollTs_Type = DateAndTime
_CucsExtpolProviderLastPollTs_Object = MibTableColumn
cucsExtpolProviderLastPollTs = _CucsExtpolProviderLastPollTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 9),
    _CucsExtpolProviderLastPollTs_Type()
)
cucsExtpolProviderLastPollTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderLastPollTs.setStatus("current")
_CucsExtpolProviderName_Type = SnmpAdminString
_CucsExtpolProviderName_Object = MibTableColumn
cucsExtpolProviderName = _CucsExtpolProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 10),
    _CucsExtpolProviderName_Type()
)
cucsExtpolProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderName.setStatus("current")
_CucsExtpolProviderOperState_Type = CucsExtpolConnectorOperState
_CucsExtpolProviderOperState_Object = MibTableColumn
cucsExtpolProviderOperState = _CucsExtpolProviderOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 11),
    _CucsExtpolProviderOperState_Type()
)
cucsExtpolProviderOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderOperState.setStatus("current")
_CucsExtpolProviderType_Type = CucsExtpolConnType
_CucsExtpolProviderType_Object = MibTableColumn
cucsExtpolProviderType = _CucsExtpolProviderType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 12),
    _CucsExtpolProviderType_Type()
)
cucsExtpolProviderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderType.setStatus("current")
_CucsExtpolProviderVersion_Type = SnmpAdminString
_CucsExtpolProviderVersion_Object = MibTableColumn
cucsExtpolProviderVersion = _CucsExtpolProviderVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 13),
    _CucsExtpolProviderVersion_Type()
)
cucsExtpolProviderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderVersion.setStatus("current")
_CucsExtpolProviderFsmDescr_Type = SnmpAdminString
_CucsExtpolProviderFsmDescr_Object = MibTableColumn
cucsExtpolProviderFsmDescr = _CucsExtpolProviderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 14),
    _CucsExtpolProviderFsmDescr_Type()
)
cucsExtpolProviderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmDescr.setStatus("current")
_CucsExtpolProviderFsmPrev_Type = SnmpAdminString
_CucsExtpolProviderFsmPrev_Object = MibTableColumn
cucsExtpolProviderFsmPrev = _CucsExtpolProviderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 15),
    _CucsExtpolProviderFsmPrev_Type()
)
cucsExtpolProviderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmPrev.setStatus("current")
_CucsExtpolProviderFsmProgr_Type = Gauge32
_CucsExtpolProviderFsmProgr_Object = MibTableColumn
cucsExtpolProviderFsmProgr = _CucsExtpolProviderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 16),
    _CucsExtpolProviderFsmProgr_Type()
)
cucsExtpolProviderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmProgr.setStatus("current")
_CucsExtpolProviderFsmRmtInvErrCode_Type = Gauge32
_CucsExtpolProviderFsmRmtInvErrCode_Object = MibTableColumn
cucsExtpolProviderFsmRmtInvErrCode = _CucsExtpolProviderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 17),
    _CucsExtpolProviderFsmRmtInvErrCode_Type()
)
cucsExtpolProviderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmRmtInvErrCode.setStatus("current")
_CucsExtpolProviderFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsExtpolProviderFsmRmtInvErrDescr_Object = MibTableColumn
cucsExtpolProviderFsmRmtInvErrDescr = _CucsExtpolProviderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 18),
    _CucsExtpolProviderFsmRmtInvErrDescr_Type()
)
cucsExtpolProviderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmRmtInvErrDescr.setStatus("current")
_CucsExtpolProviderFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsExtpolProviderFsmRmtInvRslt_Object = MibTableColumn
cucsExtpolProviderFsmRmtInvRslt = _CucsExtpolProviderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 19),
    _CucsExtpolProviderFsmRmtInvRslt_Type()
)
cucsExtpolProviderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmRmtInvRslt.setStatus("current")
_CucsExtpolProviderFsmStageDescr_Type = SnmpAdminString
_CucsExtpolProviderFsmStageDescr_Object = MibTableColumn
cucsExtpolProviderFsmStageDescr = _CucsExtpolProviderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 20),
    _CucsExtpolProviderFsmStageDescr_Type()
)
cucsExtpolProviderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmStageDescr.setStatus("current")
_CucsExtpolProviderFsmStamp_Type = DateAndTime
_CucsExtpolProviderFsmStamp_Object = MibTableColumn
cucsExtpolProviderFsmStamp = _CucsExtpolProviderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 21),
    _CucsExtpolProviderFsmStamp_Type()
)
cucsExtpolProviderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmStamp.setStatus("current")
_CucsExtpolProviderFsmStatus_Type = SnmpAdminString
_CucsExtpolProviderFsmStatus_Object = MibTableColumn
cucsExtpolProviderFsmStatus = _CucsExtpolProviderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 22),
    _CucsExtpolProviderFsmStatus_Type()
)
cucsExtpolProviderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmStatus.setStatus("current")
_CucsExtpolProviderFsmTry_Type = Gauge32
_CucsExtpolProviderFsmTry_Object = MibTableColumn
cucsExtpolProviderFsmTry = _CucsExtpolProviderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 23),
    _CucsExtpolProviderFsmTry_Type()
)
cucsExtpolProviderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmTry.setStatus("current")
_CucsExtpolProviderConnProtocol_Type = CucsExtpolConnProtocol
_CucsExtpolProviderConnProtocol_Object = MibTableColumn
cucsExtpolProviderConnProtocol = _CucsExtpolProviderConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 24),
    _CucsExtpolProviderConnProtocol_Type()
)
cucsExtpolProviderConnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderConnProtocol.setStatus("current")
_CucsExtpolProviderIpv6_Type = InetAddressIPv6
_CucsExtpolProviderIpv6_Object = MibTableColumn
cucsExtpolProviderIpv6 = _CucsExtpolProviderIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 9, 1, 25),
    _CucsExtpolProviderIpv6_Type()
)
cucsExtpolProviderIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderIpv6.setStatus("current")
_CucsExtpolProviderContTable_Object = MibTable
cucsExtpolProviderContTable = _CucsExtpolProviderContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 10)
)
if mibBuilder.loadTexts:
    cucsExtpolProviderContTable.setStatus("current")
_CucsExtpolProviderContEntry_Object = MibTableRow
cucsExtpolProviderContEntry = _CucsExtpolProviderContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 10, 1)
)
cucsExtpolProviderContEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolProviderContInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolProviderContEntry.setStatus("current")
_CucsExtpolProviderContInstanceId_Type = CucsManagedObjectId
_CucsExtpolProviderContInstanceId_Object = MibTableColumn
cucsExtpolProviderContInstanceId = _CucsExtpolProviderContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 10, 1, 1),
    _CucsExtpolProviderContInstanceId_Type()
)
cucsExtpolProviderContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolProviderContInstanceId.setStatus("current")
_CucsExtpolProviderContDn_Type = CucsManagedObjectDn
_CucsExtpolProviderContDn_Object = MibTableColumn
cucsExtpolProviderContDn = _CucsExtpolProviderContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 10, 1, 2),
    _CucsExtpolProviderContDn_Type()
)
cucsExtpolProviderContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderContDn.setStatus("current")
_CucsExtpolProviderContRn_Type = SnmpAdminString
_CucsExtpolProviderContRn_Object = MibTableColumn
cucsExtpolProviderContRn = _CucsExtpolProviderContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 10, 1, 3),
    _CucsExtpolProviderContRn_Type()
)
cucsExtpolProviderContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderContRn.setStatus("current")
_CucsExtpolProviderContGenNum_Type = Gauge32
_CucsExtpolProviderContGenNum_Object = MibTableColumn
cucsExtpolProviderContGenNum = _CucsExtpolProviderContGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 10, 1, 4),
    _CucsExtpolProviderContGenNum_Type()
)
cucsExtpolProviderContGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderContGenNum.setStatus("current")
_CucsExtpolRegistryTable_Object = MibTable
cucsExtpolRegistryTable = _CucsExtpolRegistryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11)
)
if mibBuilder.loadTexts:
    cucsExtpolRegistryTable.setStatus("current")
_CucsExtpolRegistryEntry_Object = MibTableRow
cucsExtpolRegistryEntry = _CucsExtpolRegistryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1)
)
cucsExtpolRegistryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolRegistryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolRegistryEntry.setStatus("current")
_CucsExtpolRegistryInstanceId_Type = CucsManagedObjectId
_CucsExtpolRegistryInstanceId_Object = MibTableColumn
cucsExtpolRegistryInstanceId = _CucsExtpolRegistryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 1),
    _CucsExtpolRegistryInstanceId_Type()
)
cucsExtpolRegistryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolRegistryInstanceId.setStatus("current")
_CucsExtpolRegistryDn_Type = CucsManagedObjectDn
_CucsExtpolRegistryDn_Object = MibTableColumn
cucsExtpolRegistryDn = _CucsExtpolRegistryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 2),
    _CucsExtpolRegistryDn_Type()
)
cucsExtpolRegistryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryDn.setStatus("current")
_CucsExtpolRegistryRn_Type = SnmpAdminString
_CucsExtpolRegistryRn_Object = MibTableColumn
cucsExtpolRegistryRn = _CucsExtpolRegistryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 3),
    _CucsExtpolRegistryRn_Type()
)
cucsExtpolRegistryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryRn.setStatus("current")
_CucsExtpolRegistryCapability_Type = CucsExtpolAppCapability
_CucsExtpolRegistryCapability_Object = MibTableColumn
cucsExtpolRegistryCapability = _CucsExtpolRegistryCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 4),
    _CucsExtpolRegistryCapability_Type()
)
cucsExtpolRegistryCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryCapability.setStatus("current")
_CucsExtpolRegistryFsmDescr_Type = SnmpAdminString
_CucsExtpolRegistryFsmDescr_Object = MibTableColumn
cucsExtpolRegistryFsmDescr = _CucsExtpolRegistryFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 5),
    _CucsExtpolRegistryFsmDescr_Type()
)
cucsExtpolRegistryFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmDescr.setStatus("current")
_CucsExtpolRegistryFsmPrev_Type = SnmpAdminString
_CucsExtpolRegistryFsmPrev_Object = MibTableColumn
cucsExtpolRegistryFsmPrev = _CucsExtpolRegistryFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 6),
    _CucsExtpolRegistryFsmPrev_Type()
)
cucsExtpolRegistryFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmPrev.setStatus("current")
_CucsExtpolRegistryFsmProgr_Type = Gauge32
_CucsExtpolRegistryFsmProgr_Object = MibTableColumn
cucsExtpolRegistryFsmProgr = _CucsExtpolRegistryFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 7),
    _CucsExtpolRegistryFsmProgr_Type()
)
cucsExtpolRegistryFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmProgr.setStatus("current")
_CucsExtpolRegistryFsmRmtInvErrCode_Type = Gauge32
_CucsExtpolRegistryFsmRmtInvErrCode_Object = MibTableColumn
cucsExtpolRegistryFsmRmtInvErrCode = _CucsExtpolRegistryFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 8),
    _CucsExtpolRegistryFsmRmtInvErrCode_Type()
)
cucsExtpolRegistryFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmRmtInvErrCode.setStatus("current")
_CucsExtpolRegistryFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsExtpolRegistryFsmRmtInvErrDescr_Object = MibTableColumn
cucsExtpolRegistryFsmRmtInvErrDescr = _CucsExtpolRegistryFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 9),
    _CucsExtpolRegistryFsmRmtInvErrDescr_Type()
)
cucsExtpolRegistryFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmRmtInvErrDescr.setStatus("current")
_CucsExtpolRegistryFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsExtpolRegistryFsmRmtInvRslt_Object = MibTableColumn
cucsExtpolRegistryFsmRmtInvRslt = _CucsExtpolRegistryFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 10),
    _CucsExtpolRegistryFsmRmtInvRslt_Type()
)
cucsExtpolRegistryFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmRmtInvRslt.setStatus("current")
_CucsExtpolRegistryFsmStageDescr_Type = SnmpAdminString
_CucsExtpolRegistryFsmStageDescr_Object = MibTableColumn
cucsExtpolRegistryFsmStageDescr = _CucsExtpolRegistryFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 11),
    _CucsExtpolRegistryFsmStageDescr_Type()
)
cucsExtpolRegistryFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmStageDescr.setStatus("current")
_CucsExtpolRegistryFsmStamp_Type = DateAndTime
_CucsExtpolRegistryFsmStamp_Object = MibTableColumn
cucsExtpolRegistryFsmStamp = _CucsExtpolRegistryFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 12),
    _CucsExtpolRegistryFsmStamp_Type()
)
cucsExtpolRegistryFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmStamp.setStatus("current")
_CucsExtpolRegistryFsmStatus_Type = SnmpAdminString
_CucsExtpolRegistryFsmStatus_Object = MibTableColumn
cucsExtpolRegistryFsmStatus = _CucsExtpolRegistryFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 13),
    _CucsExtpolRegistryFsmStatus_Type()
)
cucsExtpolRegistryFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmStatus.setStatus("current")
_CucsExtpolRegistryFsmTry_Type = Gauge32
_CucsExtpolRegistryFsmTry_Object = MibTableColumn
cucsExtpolRegistryFsmTry = _CucsExtpolRegistryFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 14),
    _CucsExtpolRegistryFsmTry_Type()
)
cucsExtpolRegistryFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmTry.setStatus("current")
_CucsExtpolRegistryGenNum_Type = Gauge32
_CucsExtpolRegistryGenNum_Object = MibTableColumn
cucsExtpolRegistryGenNum = _CucsExtpolRegistryGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 15),
    _CucsExtpolRegistryGenNum_Type()
)
cucsExtpolRegistryGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryGenNum.setStatus("current")
_CucsExtpolRegistryGuid_Type = SnmpAdminString
_CucsExtpolRegistryGuid_Object = MibTableColumn
cucsExtpolRegistryGuid = _CucsExtpolRegistryGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 16),
    _CucsExtpolRegistryGuid_Type()
)
cucsExtpolRegistryGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryGuid.setStatus("current")
_CucsExtpolRegistryHost_Type = SnmpAdminString
_CucsExtpolRegistryHost_Object = MibTableColumn
cucsExtpolRegistryHost = _CucsExtpolRegistryHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 17),
    _CucsExtpolRegistryHost_Type()
)
cucsExtpolRegistryHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryHost.setStatus("current")
_CucsExtpolRegistryId_Type = Gauge32
_CucsExtpolRegistryId_Object = MibTableColumn
cucsExtpolRegistryId = _CucsExtpolRegistryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 18),
    _CucsExtpolRegistryId_Type()
)
cucsExtpolRegistryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryId.setStatus("current")
_CucsExtpolRegistryIdCount_Type = Gauge32
_CucsExtpolRegistryIdCount_Object = MibTableColumn
cucsExtpolRegistryIdCount = _CucsExtpolRegistryIdCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 19),
    _CucsExtpolRegistryIdCount_Type()
)
cucsExtpolRegistryIdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryIdCount.setStatus("current")
_CucsExtpolRegistryInterest_Type = CucsExtpolAppCapability
_CucsExtpolRegistryInterest_Object = MibTableColumn
cucsExtpolRegistryInterest = _CucsExtpolRegistryInterest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 20),
    _CucsExtpolRegistryInterest_Type()
)
cucsExtpolRegistryInterest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryInterest.setStatus("current")
_CucsExtpolRegistryIp_Type = InetAddressIPv4
_CucsExtpolRegistryIp_Object = MibTableColumn
cucsExtpolRegistryIp = _CucsExtpolRegistryIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 21),
    _CucsExtpolRegistryIp_Type()
)
cucsExtpolRegistryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryIp.setStatus("current")
_CucsExtpolRegistryLastPollTs_Type = DateAndTime
_CucsExtpolRegistryLastPollTs_Object = MibTableColumn
cucsExtpolRegistryLastPollTs = _CucsExtpolRegistryLastPollTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 22),
    _CucsExtpolRegistryLastPollTs_Type()
)
cucsExtpolRegistryLastPollTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryLastPollTs.setStatus("current")
_CucsExtpolRegistryName_Type = SnmpAdminString
_CucsExtpolRegistryName_Object = MibTableColumn
cucsExtpolRegistryName = _CucsExtpolRegistryName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 23),
    _CucsExtpolRegistryName_Type()
)
cucsExtpolRegistryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryName.setStatus("current")
_CucsExtpolRegistryOperState_Type = CucsExtpolConnectorOperState
_CucsExtpolRegistryOperState_Object = MibTableColumn
cucsExtpolRegistryOperState = _CucsExtpolRegistryOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 24),
    _CucsExtpolRegistryOperState_Type()
)
cucsExtpolRegistryOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryOperState.setStatus("current")
_CucsExtpolRegistryType_Type = CucsExtpolConnType
_CucsExtpolRegistryType_Object = MibTableColumn
cucsExtpolRegistryType = _CucsExtpolRegistryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 25),
    _CucsExtpolRegistryType_Type()
)
cucsExtpolRegistryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryType.setStatus("current")
_CucsExtpolRegistryVersion_Type = SnmpAdminString
_CucsExtpolRegistryVersion_Object = MibTableColumn
cucsExtpolRegistryVersion = _CucsExtpolRegistryVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 26),
    _CucsExtpolRegistryVersion_Type()
)
cucsExtpolRegistryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryVersion.setStatus("current")
_CucsExtpolRegistryConnProtocol_Type = CucsExtpolConnProtocol
_CucsExtpolRegistryConnProtocol_Object = MibTableColumn
cucsExtpolRegistryConnProtocol = _CucsExtpolRegistryConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 27),
    _CucsExtpolRegistryConnProtocol_Type()
)
cucsExtpolRegistryConnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryConnProtocol.setStatus("current")
_CucsExtpolRegistryIpv6_Type = InetAddressIPv6
_CucsExtpolRegistryIpv6_Object = MibTableColumn
cucsExtpolRegistryIpv6 = _CucsExtpolRegistryIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 11, 1, 28),
    _CucsExtpolRegistryIpv6_Type()
)
cucsExtpolRegistryIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryIpv6.setStatus("current")
_CucsExtpolRegistryFsmTable_Object = MibTable
cucsExtpolRegistryFsmTable = _CucsExtpolRegistryFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 12)
)
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmTable.setStatus("current")
_CucsExtpolRegistryFsmEntry_Object = MibTableRow
cucsExtpolRegistryFsmEntry = _CucsExtpolRegistryFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 12, 1)
)
cucsExtpolRegistryFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolRegistryFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmEntry.setStatus("current")
_CucsExtpolRegistryFsmInstanceId_Type = CucsManagedObjectId
_CucsExtpolRegistryFsmInstanceId_Object = MibTableColumn
cucsExtpolRegistryFsmInstanceId = _CucsExtpolRegistryFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 12, 1, 1),
    _CucsExtpolRegistryFsmInstanceId_Type()
)
cucsExtpolRegistryFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmInstanceId.setStatus("current")
_CucsExtpolRegistryFsmDn_Type = CucsManagedObjectDn
_CucsExtpolRegistryFsmDn_Object = MibTableColumn
cucsExtpolRegistryFsmDn = _CucsExtpolRegistryFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 12, 1, 2),
    _CucsExtpolRegistryFsmDn_Type()
)
cucsExtpolRegistryFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmDn.setStatus("current")
_CucsExtpolRegistryFsmRn_Type = SnmpAdminString
_CucsExtpolRegistryFsmRn_Object = MibTableColumn
cucsExtpolRegistryFsmRn = _CucsExtpolRegistryFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 12, 1, 3),
    _CucsExtpolRegistryFsmRn_Type()
)
cucsExtpolRegistryFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmRn.setStatus("current")
_CucsExtpolRegistryFsmCompletionTime_Type = DateAndTime
_CucsExtpolRegistryFsmCompletionTime_Object = MibTableColumn
cucsExtpolRegistryFsmCompletionTime = _CucsExtpolRegistryFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 12, 1, 4),
    _CucsExtpolRegistryFsmCompletionTime_Type()
)
cucsExtpolRegistryFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmCompletionTime.setStatus("current")
_CucsExtpolRegistryFsmCurrentFsm_Type = CucsExtpolRegistryFsmCurrentFsm
_CucsExtpolRegistryFsmCurrentFsm_Object = MibTableColumn
cucsExtpolRegistryFsmCurrentFsm = _CucsExtpolRegistryFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 12, 1, 5),
    _CucsExtpolRegistryFsmCurrentFsm_Type()
)
cucsExtpolRegistryFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmCurrentFsm.setStatus("current")
_CucsExtpolRegistryFsmDescrData_Type = SnmpAdminString
_CucsExtpolRegistryFsmDescrData_Object = MibTableColumn
cucsExtpolRegistryFsmDescrData = _CucsExtpolRegistryFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 12, 1, 6),
    _CucsExtpolRegistryFsmDescrData_Type()
)
cucsExtpolRegistryFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmDescrData.setStatus("current")
_CucsExtpolRegistryFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsExtpolRegistryFsmFsmStatus_Object = MibTableColumn
cucsExtpolRegistryFsmFsmStatus = _CucsExtpolRegistryFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 12, 1, 7),
    _CucsExtpolRegistryFsmFsmStatus_Type()
)
cucsExtpolRegistryFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmFsmStatus.setStatus("current")
_CucsExtpolRegistryFsmProgress_Type = Gauge32
_CucsExtpolRegistryFsmProgress_Object = MibTableColumn
cucsExtpolRegistryFsmProgress = _CucsExtpolRegistryFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 12, 1, 8),
    _CucsExtpolRegistryFsmProgress_Type()
)
cucsExtpolRegistryFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmProgress.setStatus("current")
_CucsExtpolRegistryFsmRmtErrCode_Type = Gauge32
_CucsExtpolRegistryFsmRmtErrCode_Object = MibTableColumn
cucsExtpolRegistryFsmRmtErrCode = _CucsExtpolRegistryFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 12, 1, 9),
    _CucsExtpolRegistryFsmRmtErrCode_Type()
)
cucsExtpolRegistryFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmRmtErrCode.setStatus("current")
_CucsExtpolRegistryFsmRmtErrDescr_Type = SnmpAdminString
_CucsExtpolRegistryFsmRmtErrDescr_Object = MibTableColumn
cucsExtpolRegistryFsmRmtErrDescr = _CucsExtpolRegistryFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 12, 1, 10),
    _CucsExtpolRegistryFsmRmtErrDescr_Type()
)
cucsExtpolRegistryFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmRmtErrDescr.setStatus("current")
_CucsExtpolRegistryFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsExtpolRegistryFsmRmtRslt_Object = MibTableColumn
cucsExtpolRegistryFsmRmtRslt = _CucsExtpolRegistryFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 12, 1, 11),
    _CucsExtpolRegistryFsmRmtRslt_Type()
)
cucsExtpolRegistryFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmRmtRslt.setStatus("current")
_CucsExtpolRegistryFsmStageTable_Object = MibTable
cucsExtpolRegistryFsmStageTable = _CucsExtpolRegistryFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 13)
)
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmStageTable.setStatus("current")
_CucsExtpolRegistryFsmStageEntry_Object = MibTableRow
cucsExtpolRegistryFsmStageEntry = _CucsExtpolRegistryFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 13, 1)
)
cucsExtpolRegistryFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolRegistryFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmStageEntry.setStatus("current")
_CucsExtpolRegistryFsmStageInstanceId_Type = CucsManagedObjectId
_CucsExtpolRegistryFsmStageInstanceId_Object = MibTableColumn
cucsExtpolRegistryFsmStageInstanceId = _CucsExtpolRegistryFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 13, 1, 1),
    _CucsExtpolRegistryFsmStageInstanceId_Type()
)
cucsExtpolRegistryFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmStageInstanceId.setStatus("current")
_CucsExtpolRegistryFsmStageDn_Type = CucsManagedObjectDn
_CucsExtpolRegistryFsmStageDn_Object = MibTableColumn
cucsExtpolRegistryFsmStageDn = _CucsExtpolRegistryFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 13, 1, 2),
    _CucsExtpolRegistryFsmStageDn_Type()
)
cucsExtpolRegistryFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmStageDn.setStatus("current")
_CucsExtpolRegistryFsmStageRn_Type = SnmpAdminString
_CucsExtpolRegistryFsmStageRn_Object = MibTableColumn
cucsExtpolRegistryFsmStageRn = _CucsExtpolRegistryFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 13, 1, 3),
    _CucsExtpolRegistryFsmStageRn_Type()
)
cucsExtpolRegistryFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmStageRn.setStatus("current")
_CucsExtpolRegistryFsmStageDescrData_Type = SnmpAdminString
_CucsExtpolRegistryFsmStageDescrData_Object = MibTableColumn
cucsExtpolRegistryFsmStageDescrData = _CucsExtpolRegistryFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 13, 1, 4),
    _CucsExtpolRegistryFsmStageDescrData_Type()
)
cucsExtpolRegistryFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmStageDescrData.setStatus("current")
_CucsExtpolRegistryFsmStageLastUpdateTime_Type = DateAndTime
_CucsExtpolRegistryFsmStageLastUpdateTime_Object = MibTableColumn
cucsExtpolRegistryFsmStageLastUpdateTime = _CucsExtpolRegistryFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 13, 1, 5),
    _CucsExtpolRegistryFsmStageLastUpdateTime_Type()
)
cucsExtpolRegistryFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmStageLastUpdateTime.setStatus("current")
_CucsExtpolRegistryFsmStageName_Type = CucsExtpolRegistryFsmStageName
_CucsExtpolRegistryFsmStageName_Object = MibTableColumn
cucsExtpolRegistryFsmStageName = _CucsExtpolRegistryFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 13, 1, 6),
    _CucsExtpolRegistryFsmStageName_Type()
)
cucsExtpolRegistryFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmStageName.setStatus("current")
_CucsExtpolRegistryFsmStageOrder_Type = Gauge32
_CucsExtpolRegistryFsmStageOrder_Object = MibTableColumn
cucsExtpolRegistryFsmStageOrder = _CucsExtpolRegistryFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 13, 1, 7),
    _CucsExtpolRegistryFsmStageOrder_Type()
)
cucsExtpolRegistryFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmStageOrder.setStatus("current")
_CucsExtpolRegistryFsmStageRetry_Type = Gauge32
_CucsExtpolRegistryFsmStageRetry_Object = MibTableColumn
cucsExtpolRegistryFsmStageRetry = _CucsExtpolRegistryFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 13, 1, 8),
    _CucsExtpolRegistryFsmStageRetry_Type()
)
cucsExtpolRegistryFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmStageRetry.setStatus("current")
_CucsExtpolRegistryFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsExtpolRegistryFsmStageStageStatus_Object = MibTableColumn
cucsExtpolRegistryFsmStageStageStatus = _CucsExtpolRegistryFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 13, 1, 9),
    _CucsExtpolRegistryFsmStageStageStatus_Type()
)
cucsExtpolRegistryFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmStageStageStatus.setStatus("current")
_CucsExtpolRegistryFsmTaskTable_Object = MibTable
cucsExtpolRegistryFsmTaskTable = _CucsExtpolRegistryFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 14)
)
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmTaskTable.setStatus("current")
_CucsExtpolRegistryFsmTaskEntry_Object = MibTableRow
cucsExtpolRegistryFsmTaskEntry = _CucsExtpolRegistryFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 14, 1)
)
cucsExtpolRegistryFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolRegistryFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmTaskEntry.setStatus("current")
_CucsExtpolRegistryFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsExtpolRegistryFsmTaskInstanceId_Object = MibTableColumn
cucsExtpolRegistryFsmTaskInstanceId = _CucsExtpolRegistryFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 14, 1, 1),
    _CucsExtpolRegistryFsmTaskInstanceId_Type()
)
cucsExtpolRegistryFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmTaskInstanceId.setStatus("current")
_CucsExtpolRegistryFsmTaskDn_Type = CucsManagedObjectDn
_CucsExtpolRegistryFsmTaskDn_Object = MibTableColumn
cucsExtpolRegistryFsmTaskDn = _CucsExtpolRegistryFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 14, 1, 2),
    _CucsExtpolRegistryFsmTaskDn_Type()
)
cucsExtpolRegistryFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmTaskDn.setStatus("current")
_CucsExtpolRegistryFsmTaskRn_Type = SnmpAdminString
_CucsExtpolRegistryFsmTaskRn_Object = MibTableColumn
cucsExtpolRegistryFsmTaskRn = _CucsExtpolRegistryFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 14, 1, 3),
    _CucsExtpolRegistryFsmTaskRn_Type()
)
cucsExtpolRegistryFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmTaskRn.setStatus("current")
_CucsExtpolRegistryFsmTaskCompletion_Type = CucsFsmCompletion
_CucsExtpolRegistryFsmTaskCompletion_Object = MibTableColumn
cucsExtpolRegistryFsmTaskCompletion = _CucsExtpolRegistryFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 14, 1, 4),
    _CucsExtpolRegistryFsmTaskCompletion_Type()
)
cucsExtpolRegistryFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmTaskCompletion.setStatus("current")
_CucsExtpolRegistryFsmTaskFlags_Type = CucsFsmFlags
_CucsExtpolRegistryFsmTaskFlags_Object = MibTableColumn
cucsExtpolRegistryFsmTaskFlags = _CucsExtpolRegistryFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 14, 1, 5),
    _CucsExtpolRegistryFsmTaskFlags_Type()
)
cucsExtpolRegistryFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmTaskFlags.setStatus("current")
_CucsExtpolRegistryFsmTaskItem_Type = CucsExtpolRegistryFsmTaskItem
_CucsExtpolRegistryFsmTaskItem_Object = MibTableColumn
cucsExtpolRegistryFsmTaskItem = _CucsExtpolRegistryFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 14, 1, 6),
    _CucsExtpolRegistryFsmTaskItem_Type()
)
cucsExtpolRegistryFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmTaskItem.setStatus("current")
_CucsExtpolRegistryFsmTaskSeqId_Type = Gauge32
_CucsExtpolRegistryFsmTaskSeqId_Object = MibTableColumn
cucsExtpolRegistryFsmTaskSeqId = _CucsExtpolRegistryFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 14, 1, 7),
    _CucsExtpolRegistryFsmTaskSeqId_Type()
)
cucsExtpolRegistryFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolRegistryFsmTaskSeqId.setStatus("current")
_CucsExtpolSystemContextTable_Object = MibTable
cucsExtpolSystemContextTable = _CucsExtpolSystemContextTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15)
)
if mibBuilder.loadTexts:
    cucsExtpolSystemContextTable.setStatus("current")
_CucsExtpolSystemContextEntry_Object = MibTableRow
cucsExtpolSystemContextEntry = _CucsExtpolSystemContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15, 1)
)
cucsExtpolSystemContextEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolSystemContextInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolSystemContextEntry.setStatus("current")
_CucsExtpolSystemContextInstanceId_Type = CucsManagedObjectId
_CucsExtpolSystemContextInstanceId_Object = MibTableColumn
cucsExtpolSystemContextInstanceId = _CucsExtpolSystemContextInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15, 1, 1),
    _CucsExtpolSystemContextInstanceId_Type()
)
cucsExtpolSystemContextInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolSystemContextInstanceId.setStatus("current")
_CucsExtpolSystemContextDn_Type = CucsManagedObjectDn
_CucsExtpolSystemContextDn_Object = MibTableColumn
cucsExtpolSystemContextDn = _CucsExtpolSystemContextDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15, 1, 2),
    _CucsExtpolSystemContextDn_Type()
)
cucsExtpolSystemContextDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolSystemContextDn.setStatus("current")
_CucsExtpolSystemContextRn_Type = SnmpAdminString
_CucsExtpolSystemContextRn_Object = MibTableColumn
cucsExtpolSystemContextRn = _CucsExtpolSystemContextRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15, 1, 3),
    _CucsExtpolSystemContextRn_Type()
)
cucsExtpolSystemContextRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolSystemContextRn.setStatus("current")
_CucsExtpolSystemContextCapability_Type = CucsExtpolAppCapability
_CucsExtpolSystemContextCapability_Object = MibTableColumn
cucsExtpolSystemContextCapability = _CucsExtpolSystemContextCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15, 1, 4),
    _CucsExtpolSystemContextCapability_Type()
)
cucsExtpolSystemContextCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolSystemContextCapability.setStatus("current")
_CucsExtpolSystemContextDescr_Type = SnmpAdminString
_CucsExtpolSystemContextDescr_Object = MibTableColumn
cucsExtpolSystemContextDescr = _CucsExtpolSystemContextDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15, 1, 5),
    _CucsExtpolSystemContextDescr_Type()
)
cucsExtpolSystemContextDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolSystemContextDescr.setStatus("current")
_CucsExtpolSystemContextGuid_Type = SnmpAdminString
_CucsExtpolSystemContextGuid_Object = MibTableColumn
cucsExtpolSystemContextGuid = _CucsExtpolSystemContextGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15, 1, 6),
    _CucsExtpolSystemContextGuid_Type()
)
cucsExtpolSystemContextGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolSystemContextGuid.setStatus("current")
_CucsExtpolSystemContextId_Type = Gauge32
_CucsExtpolSystemContextId_Object = MibTableColumn
cucsExtpolSystemContextId = _CucsExtpolSystemContextId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15, 1, 7),
    _CucsExtpolSystemContextId_Type()
)
cucsExtpolSystemContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolSystemContextId.setStatus("current")
_CucsExtpolSystemContextInterest_Type = CucsExtpolAppCapability
_CucsExtpolSystemContextInterest_Object = MibTableColumn
cucsExtpolSystemContextInterest = _CucsExtpolSystemContextInterest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15, 1, 8),
    _CucsExtpolSystemContextInterest_Type()
)
cucsExtpolSystemContextInterest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolSystemContextInterest.setStatus("current")
_CucsExtpolSystemContextIp_Type = InetAddressIPv4
_CucsExtpolSystemContextIp_Object = MibTableColumn
cucsExtpolSystemContextIp = _CucsExtpolSystemContextIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15, 1, 9),
    _CucsExtpolSystemContextIp_Type()
)
cucsExtpolSystemContextIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolSystemContextIp.setStatus("current")
_CucsExtpolSystemContextName_Type = SnmpAdminString
_CucsExtpolSystemContextName_Object = MibTableColumn
cucsExtpolSystemContextName = _CucsExtpolSystemContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15, 1, 10),
    _CucsExtpolSystemContextName_Type()
)
cucsExtpolSystemContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolSystemContextName.setStatus("current")
_CucsExtpolSystemContextOwner_Type = SnmpAdminString
_CucsExtpolSystemContextOwner_Object = MibTableColumn
cucsExtpolSystemContextOwner = _CucsExtpolSystemContextOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15, 1, 11),
    _CucsExtpolSystemContextOwner_Type()
)
cucsExtpolSystemContextOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolSystemContextOwner.setStatus("current")
_CucsExtpolSystemContextSite_Type = SnmpAdminString
_CucsExtpolSystemContextSite_Object = MibTableColumn
cucsExtpolSystemContextSite = _CucsExtpolSystemContextSite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15, 1, 12),
    _CucsExtpolSystemContextSite_Type()
)
cucsExtpolSystemContextSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolSystemContextSite.setStatus("current")
_CucsExtpolSystemContextType_Type = CucsExtpolConnType
_CucsExtpolSystemContextType_Object = MibTableColumn
cucsExtpolSystemContextType = _CucsExtpolSystemContextType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15, 1, 13),
    _CucsExtpolSystemContextType_Type()
)
cucsExtpolSystemContextType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolSystemContextType.setStatus("current")
_CucsExtpolSystemContextVersion_Type = SnmpAdminString
_CucsExtpolSystemContextVersion_Object = MibTableColumn
cucsExtpolSystemContextVersion = _CucsExtpolSystemContextVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15, 1, 14),
    _CucsExtpolSystemContextVersion_Type()
)
cucsExtpolSystemContextVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolSystemContextVersion.setStatus("current")
_CucsExtpolSystemContextIpv6addr_Type = InetAddressIPv6
_CucsExtpolSystemContextIpv6addr_Object = MibTableColumn
cucsExtpolSystemContextIpv6addr = _CucsExtpolSystemContextIpv6addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15, 1, 15),
    _CucsExtpolSystemContextIpv6addr_Type()
)
cucsExtpolSystemContextIpv6addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolSystemContextIpv6addr.setStatus("current")
_CucsExtpolSystemContextModel_Type = SnmpAdminString
_CucsExtpolSystemContextModel_Object = MibTableColumn
cucsExtpolSystemContextModel = _CucsExtpolSystemContextModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 15, 1, 16),
    _CucsExtpolSystemContextModel_Type()
)
cucsExtpolSystemContextModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolSystemContextModel.setStatus("current")
_CucsExtpolProviderFsmTable_Object = MibTable
cucsExtpolProviderFsmTable = _CucsExtpolProviderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 16)
)
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmTable.setStatus("current")
_CucsExtpolProviderFsmEntry_Object = MibTableRow
cucsExtpolProviderFsmEntry = _CucsExtpolProviderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 16, 1)
)
cucsExtpolProviderFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolProviderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmEntry.setStatus("current")
_CucsExtpolProviderFsmInstanceId_Type = CucsManagedObjectId
_CucsExtpolProviderFsmInstanceId_Object = MibTableColumn
cucsExtpolProviderFsmInstanceId = _CucsExtpolProviderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 16, 1, 1),
    _CucsExtpolProviderFsmInstanceId_Type()
)
cucsExtpolProviderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmInstanceId.setStatus("current")
_CucsExtpolProviderFsmDn_Type = CucsManagedObjectDn
_CucsExtpolProviderFsmDn_Object = MibTableColumn
cucsExtpolProviderFsmDn = _CucsExtpolProviderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 16, 1, 2),
    _CucsExtpolProviderFsmDn_Type()
)
cucsExtpolProviderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmDn.setStatus("current")
_CucsExtpolProviderFsmRn_Type = SnmpAdminString
_CucsExtpolProviderFsmRn_Object = MibTableColumn
cucsExtpolProviderFsmRn = _CucsExtpolProviderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 16, 1, 3),
    _CucsExtpolProviderFsmRn_Type()
)
cucsExtpolProviderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmRn.setStatus("current")
_CucsExtpolProviderFsmCompletionTime_Type = DateAndTime
_CucsExtpolProviderFsmCompletionTime_Object = MibTableColumn
cucsExtpolProviderFsmCompletionTime = _CucsExtpolProviderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 16, 1, 4),
    _CucsExtpolProviderFsmCompletionTime_Type()
)
cucsExtpolProviderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmCompletionTime.setStatus("current")
_CucsExtpolProviderFsmCurrentFsm_Type = CucsExtpolProviderFsmCurrentFsm
_CucsExtpolProviderFsmCurrentFsm_Object = MibTableColumn
cucsExtpolProviderFsmCurrentFsm = _CucsExtpolProviderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 16, 1, 5),
    _CucsExtpolProviderFsmCurrentFsm_Type()
)
cucsExtpolProviderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmCurrentFsm.setStatus("current")
_CucsExtpolProviderFsmDescrData_Type = SnmpAdminString
_CucsExtpolProviderFsmDescrData_Object = MibTableColumn
cucsExtpolProviderFsmDescrData = _CucsExtpolProviderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 16, 1, 6),
    _CucsExtpolProviderFsmDescrData_Type()
)
cucsExtpolProviderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmDescrData.setStatus("current")
_CucsExtpolProviderFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsExtpolProviderFsmFsmStatus_Object = MibTableColumn
cucsExtpolProviderFsmFsmStatus = _CucsExtpolProviderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 16, 1, 7),
    _CucsExtpolProviderFsmFsmStatus_Type()
)
cucsExtpolProviderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmFsmStatus.setStatus("current")
_CucsExtpolProviderFsmProgress_Type = Gauge32
_CucsExtpolProviderFsmProgress_Object = MibTableColumn
cucsExtpolProviderFsmProgress = _CucsExtpolProviderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 16, 1, 8),
    _CucsExtpolProviderFsmProgress_Type()
)
cucsExtpolProviderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmProgress.setStatus("current")
_CucsExtpolProviderFsmRmtErrCode_Type = Gauge32
_CucsExtpolProviderFsmRmtErrCode_Object = MibTableColumn
cucsExtpolProviderFsmRmtErrCode = _CucsExtpolProviderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 16, 1, 9),
    _CucsExtpolProviderFsmRmtErrCode_Type()
)
cucsExtpolProviderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmRmtErrCode.setStatus("current")
_CucsExtpolProviderFsmRmtErrDescr_Type = SnmpAdminString
_CucsExtpolProviderFsmRmtErrDescr_Object = MibTableColumn
cucsExtpolProviderFsmRmtErrDescr = _CucsExtpolProviderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 16, 1, 10),
    _CucsExtpolProviderFsmRmtErrDescr_Type()
)
cucsExtpolProviderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmRmtErrDescr.setStatus("current")
_CucsExtpolProviderFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsExtpolProviderFsmRmtRslt_Object = MibTableColumn
cucsExtpolProviderFsmRmtRslt = _CucsExtpolProviderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 16, 1, 11),
    _CucsExtpolProviderFsmRmtRslt_Type()
)
cucsExtpolProviderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmRmtRslt.setStatus("current")
_CucsExtpolProviderFsmStageTable_Object = MibTable
cucsExtpolProviderFsmStageTable = _CucsExtpolProviderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 17)
)
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmStageTable.setStatus("current")
_CucsExtpolProviderFsmStageEntry_Object = MibTableRow
cucsExtpolProviderFsmStageEntry = _CucsExtpolProviderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 17, 1)
)
cucsExtpolProviderFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolProviderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmStageEntry.setStatus("current")
_CucsExtpolProviderFsmStageInstanceId_Type = CucsManagedObjectId
_CucsExtpolProviderFsmStageInstanceId_Object = MibTableColumn
cucsExtpolProviderFsmStageInstanceId = _CucsExtpolProviderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 17, 1, 1),
    _CucsExtpolProviderFsmStageInstanceId_Type()
)
cucsExtpolProviderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmStageInstanceId.setStatus("current")
_CucsExtpolProviderFsmStageDn_Type = CucsManagedObjectDn
_CucsExtpolProviderFsmStageDn_Object = MibTableColumn
cucsExtpolProviderFsmStageDn = _CucsExtpolProviderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 17, 1, 2),
    _CucsExtpolProviderFsmStageDn_Type()
)
cucsExtpolProviderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmStageDn.setStatus("current")
_CucsExtpolProviderFsmStageRn_Type = SnmpAdminString
_CucsExtpolProviderFsmStageRn_Object = MibTableColumn
cucsExtpolProviderFsmStageRn = _CucsExtpolProviderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 17, 1, 3),
    _CucsExtpolProviderFsmStageRn_Type()
)
cucsExtpolProviderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmStageRn.setStatus("current")
_CucsExtpolProviderFsmStageDescrData_Type = SnmpAdminString
_CucsExtpolProviderFsmStageDescrData_Object = MibTableColumn
cucsExtpolProviderFsmStageDescrData = _CucsExtpolProviderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 17, 1, 4),
    _CucsExtpolProviderFsmStageDescrData_Type()
)
cucsExtpolProviderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmStageDescrData.setStatus("current")
_CucsExtpolProviderFsmStageLastUpdateTime_Type = DateAndTime
_CucsExtpolProviderFsmStageLastUpdateTime_Object = MibTableColumn
cucsExtpolProviderFsmStageLastUpdateTime = _CucsExtpolProviderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 17, 1, 5),
    _CucsExtpolProviderFsmStageLastUpdateTime_Type()
)
cucsExtpolProviderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmStageLastUpdateTime.setStatus("current")
_CucsExtpolProviderFsmStageName_Type = CucsExtpolProviderFsmStageName
_CucsExtpolProviderFsmStageName_Object = MibTableColumn
cucsExtpolProviderFsmStageName = _CucsExtpolProviderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 17, 1, 6),
    _CucsExtpolProviderFsmStageName_Type()
)
cucsExtpolProviderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmStageName.setStatus("current")
_CucsExtpolProviderFsmStageOrder_Type = Gauge32
_CucsExtpolProviderFsmStageOrder_Object = MibTableColumn
cucsExtpolProviderFsmStageOrder = _CucsExtpolProviderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 17, 1, 7),
    _CucsExtpolProviderFsmStageOrder_Type()
)
cucsExtpolProviderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmStageOrder.setStatus("current")
_CucsExtpolProviderFsmStageRetry_Type = Gauge32
_CucsExtpolProviderFsmStageRetry_Object = MibTableColumn
cucsExtpolProviderFsmStageRetry = _CucsExtpolProviderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 17, 1, 8),
    _CucsExtpolProviderFsmStageRetry_Type()
)
cucsExtpolProviderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmStageRetry.setStatus("current")
_CucsExtpolProviderFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsExtpolProviderFsmStageStageStatus_Object = MibTableColumn
cucsExtpolProviderFsmStageStageStatus = _CucsExtpolProviderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 17, 1, 9),
    _CucsExtpolProviderFsmStageStageStatus_Type()
)
cucsExtpolProviderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmStageStageStatus.setStatus("current")
_CucsExtpolProviderFsmTaskTable_Object = MibTable
cucsExtpolProviderFsmTaskTable = _CucsExtpolProviderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 18)
)
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmTaskTable.setStatus("current")
_CucsExtpolProviderFsmTaskEntry_Object = MibTableRow
cucsExtpolProviderFsmTaskEntry = _CucsExtpolProviderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 18, 1)
)
cucsExtpolProviderFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB", "cucsExtpolProviderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmTaskEntry.setStatus("current")
_CucsExtpolProviderFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsExtpolProviderFsmTaskInstanceId_Object = MibTableColumn
cucsExtpolProviderFsmTaskInstanceId = _CucsExtpolProviderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 18, 1, 1),
    _CucsExtpolProviderFsmTaskInstanceId_Type()
)
cucsExtpolProviderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmTaskInstanceId.setStatus("current")
_CucsExtpolProviderFsmTaskDn_Type = CucsManagedObjectDn
_CucsExtpolProviderFsmTaskDn_Object = MibTableColumn
cucsExtpolProviderFsmTaskDn = _CucsExtpolProviderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 18, 1, 2),
    _CucsExtpolProviderFsmTaskDn_Type()
)
cucsExtpolProviderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmTaskDn.setStatus("current")
_CucsExtpolProviderFsmTaskRn_Type = SnmpAdminString
_CucsExtpolProviderFsmTaskRn_Object = MibTableColumn
cucsExtpolProviderFsmTaskRn = _CucsExtpolProviderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 18, 1, 3),
    _CucsExtpolProviderFsmTaskRn_Type()
)
cucsExtpolProviderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmTaskRn.setStatus("current")
_CucsExtpolProviderFsmTaskCompletion_Type = CucsFsmCompletion
_CucsExtpolProviderFsmTaskCompletion_Object = MibTableColumn
cucsExtpolProviderFsmTaskCompletion = _CucsExtpolProviderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 18, 1, 4),
    _CucsExtpolProviderFsmTaskCompletion_Type()
)
cucsExtpolProviderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmTaskCompletion.setStatus("current")
_CucsExtpolProviderFsmTaskFlags_Type = CucsFsmFlags
_CucsExtpolProviderFsmTaskFlags_Object = MibTableColumn
cucsExtpolProviderFsmTaskFlags = _CucsExtpolProviderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 18, 1, 5),
    _CucsExtpolProviderFsmTaskFlags_Type()
)
cucsExtpolProviderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmTaskFlags.setStatus("current")
_CucsExtpolProviderFsmTaskItem_Type = CucsExtpolProviderFsmTaskItem
_CucsExtpolProviderFsmTaskItem_Object = MibTableColumn
cucsExtpolProviderFsmTaskItem = _CucsExtpolProviderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 18, 1, 6),
    _CucsExtpolProviderFsmTaskItem_Type()
)
cucsExtpolProviderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmTaskItem.setStatus("current")
_CucsExtpolProviderFsmTaskSeqId_Type = Gauge32
_CucsExtpolProviderFsmTaskSeqId_Object = MibTableColumn
cucsExtpolProviderFsmTaskSeqId = _CucsExtpolProviderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 62, 18, 1, 7),
    _CucsExtpolProviderFsmTaskSeqId_Type()
)
cucsExtpolProviderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtpolProviderFsmTaskSeqId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-EXTPOL-MIB",
    **{"cucsExtpolObjects": cucsExtpolObjects,
       "cucsExtpolClientTable": cucsExtpolClientTable,
       "cucsExtpolClientEntry": cucsExtpolClientEntry,
       "cucsExtpolClientInstanceId": cucsExtpolClientInstanceId,
       "cucsExtpolClientDn": cucsExtpolClientDn,
       "cucsExtpolClientRn": cucsExtpolClientRn,
       "cucsExtpolClientCapability": cucsExtpolClientCapability,
       "cucsExtpolClientDescr": cucsExtpolClientDescr,
       "cucsExtpolClientGuid": cucsExtpolClientGuid,
       "cucsExtpolClientHost": cucsExtpolClientHost,
       "cucsExtpolClientId": cucsExtpolClientId,
       "cucsExtpolClientInterest": cucsExtpolClientInterest,
       "cucsExtpolClientIp": cucsExtpolClientIp,
       "cucsExtpolClientLastPollTs": cucsExtpolClientLastPollTs,
       "cucsExtpolClientName": cucsExtpolClientName,
       "cucsExtpolClientOperState": cucsExtpolClientOperState,
       "cucsExtpolClientOwner": cucsExtpolClientOwner,
       "cucsExtpolClientSite": cucsExtpolClientSite,
       "cucsExtpolClientSuspendState": cucsExtpolClientSuspendState,
       "cucsExtpolClientType": cucsExtpolClientType,
       "cucsExtpolClientVersion": cucsExtpolClientVersion,
       "cucsExtpolClientGracePeriodUsed": cucsExtpolClientGracePeriodUsed,
       "cucsExtpolClientLicState": cucsExtpolClientLicState,
       "cucsExtpolClientConnProtocol": cucsExtpolClientConnProtocol,
       "cucsExtpolClientIpv6": cucsExtpolClientIpv6,
       "cucsExtpolClientContTable": cucsExtpolClientContTable,
       "cucsExtpolClientContEntry": cucsExtpolClientContEntry,
       "cucsExtpolClientContInstanceId": cucsExtpolClientContInstanceId,
       "cucsExtpolClientContDn": cucsExtpolClientContDn,
       "cucsExtpolClientContRn": cucsExtpolClientContRn,
       "cucsExtpolClientContGenNum": cucsExtpolClientContGenNum,
       "cucsExtpolControllerTable": cucsExtpolControllerTable,
       "cucsExtpolControllerEntry": cucsExtpolControllerEntry,
       "cucsExtpolControllerInstanceId": cucsExtpolControllerInstanceId,
       "cucsExtpolControllerDn": cucsExtpolControllerDn,
       "cucsExtpolControllerRn": cucsExtpolControllerRn,
       "cucsExtpolControllerCapability": cucsExtpolControllerCapability,
       "cucsExtpolControllerHost": cucsExtpolControllerHost,
       "cucsExtpolControllerId": cucsExtpolControllerId,
       "cucsExtpolControllerInterest": cucsExtpolControllerInterest,
       "cucsExtpolControllerIp": cucsExtpolControllerIp,
       "cucsExtpolControllerLastPollTs": cucsExtpolControllerLastPollTs,
       "cucsExtpolControllerName": cucsExtpolControllerName,
       "cucsExtpolControllerOperState": cucsExtpolControllerOperState,
       "cucsExtpolControllerType": cucsExtpolControllerType,
       "cucsExtpolControllerVersion": cucsExtpolControllerVersion,
       "cucsExtpolControllerConnProtocol": cucsExtpolControllerConnProtocol,
       "cucsExtpolControllerIpv6": cucsExtpolControllerIpv6,
       "cucsExtpolControllerContTable": cucsExtpolControllerContTable,
       "cucsExtpolControllerContEntry": cucsExtpolControllerContEntry,
       "cucsExtpolControllerContInstanceId": cucsExtpolControllerContInstanceId,
       "cucsExtpolControllerContDn": cucsExtpolControllerContDn,
       "cucsExtpolControllerContRn": cucsExtpolControllerContRn,
       "cucsExtpolControllerContGenNum": cucsExtpolControllerContGenNum,
       "cucsExtpolEpTable": cucsExtpolEpTable,
       "cucsExtpolEpEntry": cucsExtpolEpEntry,
       "cucsExtpolEpInstanceId": cucsExtpolEpInstanceId,
       "cucsExtpolEpDn": cucsExtpolEpDn,
       "cucsExtpolEpRn": cucsExtpolEpRn,
       "cucsExtpolEpFsmDescr": cucsExtpolEpFsmDescr,
       "cucsExtpolEpFsmPrev": cucsExtpolEpFsmPrev,
       "cucsExtpolEpFsmProgr": cucsExtpolEpFsmProgr,
       "cucsExtpolEpFsmRmtInvErrCode": cucsExtpolEpFsmRmtInvErrCode,
       "cucsExtpolEpFsmRmtInvErrDescr": cucsExtpolEpFsmRmtInvErrDescr,
       "cucsExtpolEpFsmRmtInvRslt": cucsExtpolEpFsmRmtInvRslt,
       "cucsExtpolEpFsmStageDescr": cucsExtpolEpFsmStageDescr,
       "cucsExtpolEpFsmStamp": cucsExtpolEpFsmStamp,
       "cucsExtpolEpFsmStatus": cucsExtpolEpFsmStatus,
       "cucsExtpolEpFsmTry": cucsExtpolEpFsmTry,
       "cucsExtpolEpFsmTable": cucsExtpolEpFsmTable,
       "cucsExtpolEpFsmEntry": cucsExtpolEpFsmEntry,
       "cucsExtpolEpFsmInstanceId": cucsExtpolEpFsmInstanceId,
       "cucsExtpolEpFsmDn": cucsExtpolEpFsmDn,
       "cucsExtpolEpFsmRn": cucsExtpolEpFsmRn,
       "cucsExtpolEpFsmCompletionTime": cucsExtpolEpFsmCompletionTime,
       "cucsExtpolEpFsmCurrentFsm": cucsExtpolEpFsmCurrentFsm,
       "cucsExtpolEpFsmDescrData": cucsExtpolEpFsmDescrData,
       "cucsExtpolEpFsmFsmStatus": cucsExtpolEpFsmFsmStatus,
       "cucsExtpolEpFsmProgress": cucsExtpolEpFsmProgress,
       "cucsExtpolEpFsmRmtErrCode": cucsExtpolEpFsmRmtErrCode,
       "cucsExtpolEpFsmRmtErrDescr": cucsExtpolEpFsmRmtErrDescr,
       "cucsExtpolEpFsmRmtRslt": cucsExtpolEpFsmRmtRslt,
       "cucsExtpolEpFsmStageTable": cucsExtpolEpFsmStageTable,
       "cucsExtpolEpFsmStageEntry": cucsExtpolEpFsmStageEntry,
       "cucsExtpolEpFsmStageInstanceId": cucsExtpolEpFsmStageInstanceId,
       "cucsExtpolEpFsmStageDn": cucsExtpolEpFsmStageDn,
       "cucsExtpolEpFsmStageRn": cucsExtpolEpFsmStageRn,
       "cucsExtpolEpFsmStageDescrData": cucsExtpolEpFsmStageDescrData,
       "cucsExtpolEpFsmStageLastUpdateTime": cucsExtpolEpFsmStageLastUpdateTime,
       "cucsExtpolEpFsmStageName": cucsExtpolEpFsmStageName,
       "cucsExtpolEpFsmStageOrder": cucsExtpolEpFsmStageOrder,
       "cucsExtpolEpFsmStageRetry": cucsExtpolEpFsmStageRetry,
       "cucsExtpolEpFsmStageStageStatus": cucsExtpolEpFsmStageStageStatus,
       "cucsExtpolEpFsmTaskTable": cucsExtpolEpFsmTaskTable,
       "cucsExtpolEpFsmTaskEntry": cucsExtpolEpFsmTaskEntry,
       "cucsExtpolEpFsmTaskInstanceId": cucsExtpolEpFsmTaskInstanceId,
       "cucsExtpolEpFsmTaskDn": cucsExtpolEpFsmTaskDn,
       "cucsExtpolEpFsmTaskRn": cucsExtpolEpFsmTaskRn,
       "cucsExtpolEpFsmTaskCompletion": cucsExtpolEpFsmTaskCompletion,
       "cucsExtpolEpFsmTaskFlags": cucsExtpolEpFsmTaskFlags,
       "cucsExtpolEpFsmTaskItem": cucsExtpolEpFsmTaskItem,
       "cucsExtpolEpFsmTaskSeqId": cucsExtpolEpFsmTaskSeqId,
       "cucsExtpolProviderTable": cucsExtpolProviderTable,
       "cucsExtpolProviderEntry": cucsExtpolProviderEntry,
       "cucsExtpolProviderInstanceId": cucsExtpolProviderInstanceId,
       "cucsExtpolProviderDn": cucsExtpolProviderDn,
       "cucsExtpolProviderRn": cucsExtpolProviderRn,
       "cucsExtpolProviderCapability": cucsExtpolProviderCapability,
       "cucsExtpolProviderHost": cucsExtpolProviderHost,
       "cucsExtpolProviderId": cucsExtpolProviderId,
       "cucsExtpolProviderInterest": cucsExtpolProviderInterest,
       "cucsExtpolProviderIp": cucsExtpolProviderIp,
       "cucsExtpolProviderLastPollTs": cucsExtpolProviderLastPollTs,
       "cucsExtpolProviderName": cucsExtpolProviderName,
       "cucsExtpolProviderOperState": cucsExtpolProviderOperState,
       "cucsExtpolProviderType": cucsExtpolProviderType,
       "cucsExtpolProviderVersion": cucsExtpolProviderVersion,
       "cucsExtpolProviderFsmDescr": cucsExtpolProviderFsmDescr,
       "cucsExtpolProviderFsmPrev": cucsExtpolProviderFsmPrev,
       "cucsExtpolProviderFsmProgr": cucsExtpolProviderFsmProgr,
       "cucsExtpolProviderFsmRmtInvErrCode": cucsExtpolProviderFsmRmtInvErrCode,
       "cucsExtpolProviderFsmRmtInvErrDescr": cucsExtpolProviderFsmRmtInvErrDescr,
       "cucsExtpolProviderFsmRmtInvRslt": cucsExtpolProviderFsmRmtInvRslt,
       "cucsExtpolProviderFsmStageDescr": cucsExtpolProviderFsmStageDescr,
       "cucsExtpolProviderFsmStamp": cucsExtpolProviderFsmStamp,
       "cucsExtpolProviderFsmStatus": cucsExtpolProviderFsmStatus,
       "cucsExtpolProviderFsmTry": cucsExtpolProviderFsmTry,
       "cucsExtpolProviderConnProtocol": cucsExtpolProviderConnProtocol,
       "cucsExtpolProviderIpv6": cucsExtpolProviderIpv6,
       "cucsExtpolProviderContTable": cucsExtpolProviderContTable,
       "cucsExtpolProviderContEntry": cucsExtpolProviderContEntry,
       "cucsExtpolProviderContInstanceId": cucsExtpolProviderContInstanceId,
       "cucsExtpolProviderContDn": cucsExtpolProviderContDn,
       "cucsExtpolProviderContRn": cucsExtpolProviderContRn,
       "cucsExtpolProviderContGenNum": cucsExtpolProviderContGenNum,
       "cucsExtpolRegistryTable": cucsExtpolRegistryTable,
       "cucsExtpolRegistryEntry": cucsExtpolRegistryEntry,
       "cucsExtpolRegistryInstanceId": cucsExtpolRegistryInstanceId,
       "cucsExtpolRegistryDn": cucsExtpolRegistryDn,
       "cucsExtpolRegistryRn": cucsExtpolRegistryRn,
       "cucsExtpolRegistryCapability": cucsExtpolRegistryCapability,
       "cucsExtpolRegistryFsmDescr": cucsExtpolRegistryFsmDescr,
       "cucsExtpolRegistryFsmPrev": cucsExtpolRegistryFsmPrev,
       "cucsExtpolRegistryFsmProgr": cucsExtpolRegistryFsmProgr,
       "cucsExtpolRegistryFsmRmtInvErrCode": cucsExtpolRegistryFsmRmtInvErrCode,
       "cucsExtpolRegistryFsmRmtInvErrDescr": cucsExtpolRegistryFsmRmtInvErrDescr,
       "cucsExtpolRegistryFsmRmtInvRslt": cucsExtpolRegistryFsmRmtInvRslt,
       "cucsExtpolRegistryFsmStageDescr": cucsExtpolRegistryFsmStageDescr,
       "cucsExtpolRegistryFsmStamp": cucsExtpolRegistryFsmStamp,
       "cucsExtpolRegistryFsmStatus": cucsExtpolRegistryFsmStatus,
       "cucsExtpolRegistryFsmTry": cucsExtpolRegistryFsmTry,
       "cucsExtpolRegistryGenNum": cucsExtpolRegistryGenNum,
       "cucsExtpolRegistryGuid": cucsExtpolRegistryGuid,
       "cucsExtpolRegistryHost": cucsExtpolRegistryHost,
       "cucsExtpolRegistryId": cucsExtpolRegistryId,
       "cucsExtpolRegistryIdCount": cucsExtpolRegistryIdCount,
       "cucsExtpolRegistryInterest": cucsExtpolRegistryInterest,
       "cucsExtpolRegistryIp": cucsExtpolRegistryIp,
       "cucsExtpolRegistryLastPollTs": cucsExtpolRegistryLastPollTs,
       "cucsExtpolRegistryName": cucsExtpolRegistryName,
       "cucsExtpolRegistryOperState": cucsExtpolRegistryOperState,
       "cucsExtpolRegistryType": cucsExtpolRegistryType,
       "cucsExtpolRegistryVersion": cucsExtpolRegistryVersion,
       "cucsExtpolRegistryConnProtocol": cucsExtpolRegistryConnProtocol,
       "cucsExtpolRegistryIpv6": cucsExtpolRegistryIpv6,
       "cucsExtpolRegistryFsmTable": cucsExtpolRegistryFsmTable,
       "cucsExtpolRegistryFsmEntry": cucsExtpolRegistryFsmEntry,
       "cucsExtpolRegistryFsmInstanceId": cucsExtpolRegistryFsmInstanceId,
       "cucsExtpolRegistryFsmDn": cucsExtpolRegistryFsmDn,
       "cucsExtpolRegistryFsmRn": cucsExtpolRegistryFsmRn,
       "cucsExtpolRegistryFsmCompletionTime": cucsExtpolRegistryFsmCompletionTime,
       "cucsExtpolRegistryFsmCurrentFsm": cucsExtpolRegistryFsmCurrentFsm,
       "cucsExtpolRegistryFsmDescrData": cucsExtpolRegistryFsmDescrData,
       "cucsExtpolRegistryFsmFsmStatus": cucsExtpolRegistryFsmFsmStatus,
       "cucsExtpolRegistryFsmProgress": cucsExtpolRegistryFsmProgress,
       "cucsExtpolRegistryFsmRmtErrCode": cucsExtpolRegistryFsmRmtErrCode,
       "cucsExtpolRegistryFsmRmtErrDescr": cucsExtpolRegistryFsmRmtErrDescr,
       "cucsExtpolRegistryFsmRmtRslt": cucsExtpolRegistryFsmRmtRslt,
       "cucsExtpolRegistryFsmStageTable": cucsExtpolRegistryFsmStageTable,
       "cucsExtpolRegistryFsmStageEntry": cucsExtpolRegistryFsmStageEntry,
       "cucsExtpolRegistryFsmStageInstanceId": cucsExtpolRegistryFsmStageInstanceId,
       "cucsExtpolRegistryFsmStageDn": cucsExtpolRegistryFsmStageDn,
       "cucsExtpolRegistryFsmStageRn": cucsExtpolRegistryFsmStageRn,
       "cucsExtpolRegistryFsmStageDescrData": cucsExtpolRegistryFsmStageDescrData,
       "cucsExtpolRegistryFsmStageLastUpdateTime": cucsExtpolRegistryFsmStageLastUpdateTime,
       "cucsExtpolRegistryFsmStageName": cucsExtpolRegistryFsmStageName,
       "cucsExtpolRegistryFsmStageOrder": cucsExtpolRegistryFsmStageOrder,
       "cucsExtpolRegistryFsmStageRetry": cucsExtpolRegistryFsmStageRetry,
       "cucsExtpolRegistryFsmStageStageStatus": cucsExtpolRegistryFsmStageStageStatus,
       "cucsExtpolRegistryFsmTaskTable": cucsExtpolRegistryFsmTaskTable,
       "cucsExtpolRegistryFsmTaskEntry": cucsExtpolRegistryFsmTaskEntry,
       "cucsExtpolRegistryFsmTaskInstanceId": cucsExtpolRegistryFsmTaskInstanceId,
       "cucsExtpolRegistryFsmTaskDn": cucsExtpolRegistryFsmTaskDn,
       "cucsExtpolRegistryFsmTaskRn": cucsExtpolRegistryFsmTaskRn,
       "cucsExtpolRegistryFsmTaskCompletion": cucsExtpolRegistryFsmTaskCompletion,
       "cucsExtpolRegistryFsmTaskFlags": cucsExtpolRegistryFsmTaskFlags,
       "cucsExtpolRegistryFsmTaskItem": cucsExtpolRegistryFsmTaskItem,
       "cucsExtpolRegistryFsmTaskSeqId": cucsExtpolRegistryFsmTaskSeqId,
       "cucsExtpolSystemContextTable": cucsExtpolSystemContextTable,
       "cucsExtpolSystemContextEntry": cucsExtpolSystemContextEntry,
       "cucsExtpolSystemContextInstanceId": cucsExtpolSystemContextInstanceId,
       "cucsExtpolSystemContextDn": cucsExtpolSystemContextDn,
       "cucsExtpolSystemContextRn": cucsExtpolSystemContextRn,
       "cucsExtpolSystemContextCapability": cucsExtpolSystemContextCapability,
       "cucsExtpolSystemContextDescr": cucsExtpolSystemContextDescr,
       "cucsExtpolSystemContextGuid": cucsExtpolSystemContextGuid,
       "cucsExtpolSystemContextId": cucsExtpolSystemContextId,
       "cucsExtpolSystemContextInterest": cucsExtpolSystemContextInterest,
       "cucsExtpolSystemContextIp": cucsExtpolSystemContextIp,
       "cucsExtpolSystemContextName": cucsExtpolSystemContextName,
       "cucsExtpolSystemContextOwner": cucsExtpolSystemContextOwner,
       "cucsExtpolSystemContextSite": cucsExtpolSystemContextSite,
       "cucsExtpolSystemContextType": cucsExtpolSystemContextType,
       "cucsExtpolSystemContextVersion": cucsExtpolSystemContextVersion,
       "cucsExtpolSystemContextIpv6addr": cucsExtpolSystemContextIpv6addr,
       "cucsExtpolSystemContextModel": cucsExtpolSystemContextModel,
       "cucsExtpolProviderFsmTable": cucsExtpolProviderFsmTable,
       "cucsExtpolProviderFsmEntry": cucsExtpolProviderFsmEntry,
       "cucsExtpolProviderFsmInstanceId": cucsExtpolProviderFsmInstanceId,
       "cucsExtpolProviderFsmDn": cucsExtpolProviderFsmDn,
       "cucsExtpolProviderFsmRn": cucsExtpolProviderFsmRn,
       "cucsExtpolProviderFsmCompletionTime": cucsExtpolProviderFsmCompletionTime,
       "cucsExtpolProviderFsmCurrentFsm": cucsExtpolProviderFsmCurrentFsm,
       "cucsExtpolProviderFsmDescrData": cucsExtpolProviderFsmDescrData,
       "cucsExtpolProviderFsmFsmStatus": cucsExtpolProviderFsmFsmStatus,
       "cucsExtpolProviderFsmProgress": cucsExtpolProviderFsmProgress,
       "cucsExtpolProviderFsmRmtErrCode": cucsExtpolProviderFsmRmtErrCode,
       "cucsExtpolProviderFsmRmtErrDescr": cucsExtpolProviderFsmRmtErrDescr,
       "cucsExtpolProviderFsmRmtRslt": cucsExtpolProviderFsmRmtRslt,
       "cucsExtpolProviderFsmStageTable": cucsExtpolProviderFsmStageTable,
       "cucsExtpolProviderFsmStageEntry": cucsExtpolProviderFsmStageEntry,
       "cucsExtpolProviderFsmStageInstanceId": cucsExtpolProviderFsmStageInstanceId,
       "cucsExtpolProviderFsmStageDn": cucsExtpolProviderFsmStageDn,
       "cucsExtpolProviderFsmStageRn": cucsExtpolProviderFsmStageRn,
       "cucsExtpolProviderFsmStageDescrData": cucsExtpolProviderFsmStageDescrData,
       "cucsExtpolProviderFsmStageLastUpdateTime": cucsExtpolProviderFsmStageLastUpdateTime,
       "cucsExtpolProviderFsmStageName": cucsExtpolProviderFsmStageName,
       "cucsExtpolProviderFsmStageOrder": cucsExtpolProviderFsmStageOrder,
       "cucsExtpolProviderFsmStageRetry": cucsExtpolProviderFsmStageRetry,
       "cucsExtpolProviderFsmStageStageStatus": cucsExtpolProviderFsmStageStageStatus,
       "cucsExtpolProviderFsmTaskTable": cucsExtpolProviderFsmTaskTable,
       "cucsExtpolProviderFsmTaskEntry": cucsExtpolProviderFsmTaskEntry,
       "cucsExtpolProviderFsmTaskInstanceId": cucsExtpolProviderFsmTaskInstanceId,
       "cucsExtpolProviderFsmTaskDn": cucsExtpolProviderFsmTaskDn,
       "cucsExtpolProviderFsmTaskRn": cucsExtpolProviderFsmTaskRn,
       "cucsExtpolProviderFsmTaskCompletion": cucsExtpolProviderFsmTaskCompletion,
       "cucsExtpolProviderFsmTaskFlags": cucsExtpolProviderFsmTaskFlags,
       "cucsExtpolProviderFsmTaskItem": cucsExtpolProviderFsmTaskItem,
       "cucsExtpolProviderFsmTaskSeqId": cucsExtpolProviderFsmTaskSeqId}
)
