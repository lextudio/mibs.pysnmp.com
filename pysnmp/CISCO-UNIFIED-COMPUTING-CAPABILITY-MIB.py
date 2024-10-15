# SNMP MIB module (CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:06 2024
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

(CucsCapabilityAdminState,
 CucsCapabilityCatalogueFsmCurrentFsm,
 CucsCapabilityCatalogueFsmStageName,
 CucsCapabilityCatalogueFsmTaskItem,
 CucsCapabilityFeatureStatus,
 CucsCapabilityMgmtExtensionFsmCurrentFsm,
 CucsCapabilityMgmtExtensionFsmStageName,
 CucsCapabilityMgmtExtensionFsmTaskItem,
 CucsCapabilityOperStatus,
 CucsCapabilityPlatform,
 CucsCapabilityUpdaterFsmCurrentFsm,
 CucsCapabilityUpdaterFsmStageName,
 CucsCapabilityUpdaterFsmTaskItem,
 CucsConditionRemoteInvRslt,
 CucsFirmwareTransport,
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsCapabilityAdminState",
    "CucsCapabilityCatalogueFsmCurrentFsm",
    "CucsCapabilityCatalogueFsmStageName",
    "CucsCapabilityCatalogueFsmTaskItem",
    "CucsCapabilityFeatureStatus",
    "CucsCapabilityMgmtExtensionFsmCurrentFsm",
    "CucsCapabilityMgmtExtensionFsmStageName",
    "CucsCapabilityMgmtExtensionFsmTaskItem",
    "CucsCapabilityOperStatus",
    "CucsCapabilityPlatform",
    "CucsCapabilityUpdaterFsmCurrentFsm",
    "CucsCapabilityUpdaterFsmStageName",
    "CucsCapabilityUpdaterFsmTaskItem",
    "CucsConditionRemoteInvRslt",
    "CucsFirmwareTransport",
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

cucsCapabilityObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsCapabilityCatalogueTable_Object = MibTable
cucsCapabilityCatalogueTable = _CucsCapabilityCatalogueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueTable.setStatus("current")
_CucsCapabilityCatalogueEntry_Object = MibTableRow
cucsCapabilityCatalogueEntry = _CucsCapabilityCatalogueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1)
)
cucsCapabilityCatalogueEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilityCatalogueInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueEntry.setStatus("current")
_CucsCapabilityCatalogueInstanceId_Type = CucsManagedObjectId
_CucsCapabilityCatalogueInstanceId_Object = MibTableColumn
cucsCapabilityCatalogueInstanceId = _CucsCapabilityCatalogueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 1),
    _CucsCapabilityCatalogueInstanceId_Type()
)
cucsCapabilityCatalogueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueInstanceId.setStatus("current")
_CucsCapabilityCatalogueDn_Type = CucsManagedObjectDn
_CucsCapabilityCatalogueDn_Object = MibTableColumn
cucsCapabilityCatalogueDn = _CucsCapabilityCatalogueDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 2),
    _CucsCapabilityCatalogueDn_Type()
)
cucsCapabilityCatalogueDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueDn.setStatus("current")
_CucsCapabilityCatalogueRn_Type = SnmpAdminString
_CucsCapabilityCatalogueRn_Object = MibTableColumn
cucsCapabilityCatalogueRn = _CucsCapabilityCatalogueRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 3),
    _CucsCapabilityCatalogueRn_Type()
)
cucsCapabilityCatalogueRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueRn.setStatus("current")
_CucsCapabilityCatalogueFsmDescr_Type = SnmpAdminString
_CucsCapabilityCatalogueFsmDescr_Object = MibTableColumn
cucsCapabilityCatalogueFsmDescr = _CucsCapabilityCatalogueFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 4),
    _CucsCapabilityCatalogueFsmDescr_Type()
)
cucsCapabilityCatalogueFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmDescr.setStatus("current")
_CucsCapabilityCatalogueFsmPrev_Type = SnmpAdminString
_CucsCapabilityCatalogueFsmPrev_Object = MibTableColumn
cucsCapabilityCatalogueFsmPrev = _CucsCapabilityCatalogueFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 5),
    _CucsCapabilityCatalogueFsmPrev_Type()
)
cucsCapabilityCatalogueFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmPrev.setStatus("current")
_CucsCapabilityCatalogueFsmProgr_Type = Gauge32
_CucsCapabilityCatalogueFsmProgr_Object = MibTableColumn
cucsCapabilityCatalogueFsmProgr = _CucsCapabilityCatalogueFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 6),
    _CucsCapabilityCatalogueFsmProgr_Type()
)
cucsCapabilityCatalogueFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmProgr.setStatus("current")
_CucsCapabilityCatalogueFsmRmtInvErrCode_Type = Gauge32
_CucsCapabilityCatalogueFsmRmtInvErrCode_Object = MibTableColumn
cucsCapabilityCatalogueFsmRmtInvErrCode = _CucsCapabilityCatalogueFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 7),
    _CucsCapabilityCatalogueFsmRmtInvErrCode_Type()
)
cucsCapabilityCatalogueFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmRmtInvErrCode.setStatus("current")
_CucsCapabilityCatalogueFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsCapabilityCatalogueFsmRmtInvErrDescr_Object = MibTableColumn
cucsCapabilityCatalogueFsmRmtInvErrDescr = _CucsCapabilityCatalogueFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 8),
    _CucsCapabilityCatalogueFsmRmtInvErrDescr_Type()
)
cucsCapabilityCatalogueFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmRmtInvErrDescr.setStatus("current")
_CucsCapabilityCatalogueFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsCapabilityCatalogueFsmRmtInvRslt_Object = MibTableColumn
cucsCapabilityCatalogueFsmRmtInvRslt = _CucsCapabilityCatalogueFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 9),
    _CucsCapabilityCatalogueFsmRmtInvRslt_Type()
)
cucsCapabilityCatalogueFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmRmtInvRslt.setStatus("current")
_CucsCapabilityCatalogueFsmStageDescr_Type = SnmpAdminString
_CucsCapabilityCatalogueFsmStageDescr_Object = MibTableColumn
cucsCapabilityCatalogueFsmStageDescr = _CucsCapabilityCatalogueFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 10),
    _CucsCapabilityCatalogueFsmStageDescr_Type()
)
cucsCapabilityCatalogueFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmStageDescr.setStatus("current")
_CucsCapabilityCatalogueFsmStamp_Type = DateAndTime
_CucsCapabilityCatalogueFsmStamp_Object = MibTableColumn
cucsCapabilityCatalogueFsmStamp = _CucsCapabilityCatalogueFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 11),
    _CucsCapabilityCatalogueFsmStamp_Type()
)
cucsCapabilityCatalogueFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmStamp.setStatus("current")
_CucsCapabilityCatalogueFsmStatus_Type = SnmpAdminString
_CucsCapabilityCatalogueFsmStatus_Object = MibTableColumn
cucsCapabilityCatalogueFsmStatus = _CucsCapabilityCatalogueFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 12),
    _CucsCapabilityCatalogueFsmStatus_Type()
)
cucsCapabilityCatalogueFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmStatus.setStatus("current")
_CucsCapabilityCatalogueFsmTry_Type = Gauge32
_CucsCapabilityCatalogueFsmTry_Object = MibTableColumn
cucsCapabilityCatalogueFsmTry = _CucsCapabilityCatalogueFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 13),
    _CucsCapabilityCatalogueFsmTry_Type()
)
cucsCapabilityCatalogueFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmTry.setStatus("current")
_CucsCapabilityCatalogueVersion_Type = SnmpAdminString
_CucsCapabilityCatalogueVersion_Object = MibTableColumn
cucsCapabilityCatalogueVersion = _CucsCapabilityCatalogueVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 14),
    _CucsCapabilityCatalogueVersion_Type()
)
cucsCapabilityCatalogueVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueVersion.setStatus("current")
_CucsCapabilityCatalogueFileParseFailures_Type = Gauge32
_CucsCapabilityCatalogueFileParseFailures_Object = MibTableColumn
cucsCapabilityCatalogueFileParseFailures = _CucsCapabilityCatalogueFileParseFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 15),
    _CucsCapabilityCatalogueFileParseFailures_Type()
)
cucsCapabilityCatalogueFileParseFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFileParseFailures.setStatus("current")
_CucsCapabilityCatalogueFilesParsed_Type = Gauge32
_CucsCapabilityCatalogueFilesParsed_Object = MibTableColumn
cucsCapabilityCatalogueFilesParsed = _CucsCapabilityCatalogueFilesParsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 16),
    _CucsCapabilityCatalogueFilesParsed_Type()
)
cucsCapabilityCatalogueFilesParsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFilesParsed.setStatus("current")
_CucsCapabilityCatalogueLoadErrors_Type = Gauge32
_CucsCapabilityCatalogueLoadErrors_Object = MibTableColumn
cucsCapabilityCatalogueLoadErrors = _CucsCapabilityCatalogueLoadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 17),
    _CucsCapabilityCatalogueLoadErrors_Type()
)
cucsCapabilityCatalogueLoadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueLoadErrors.setStatus("current")
_CucsCapabilityCatalogueLoadWarnings_Type = Gauge32
_CucsCapabilityCatalogueLoadWarnings_Object = MibTableColumn
cucsCapabilityCatalogueLoadWarnings = _CucsCapabilityCatalogueLoadWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 18),
    _CucsCapabilityCatalogueLoadWarnings_Type()
)
cucsCapabilityCatalogueLoadWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueLoadWarnings.setStatus("current")
_CucsCapabilityCatalogueProviderLoadFailures_Type = Gauge32
_CucsCapabilityCatalogueProviderLoadFailures_Object = MibTableColumn
cucsCapabilityCatalogueProviderLoadFailures = _CucsCapabilityCatalogueProviderLoadFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 19),
    _CucsCapabilityCatalogueProviderLoadFailures_Type()
)
cucsCapabilityCatalogueProviderLoadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueProviderLoadFailures.setStatus("current")
_CucsCapabilityCatalogueProvidersLoaded_Type = Gauge32
_CucsCapabilityCatalogueProvidersLoaded_Object = MibTableColumn
cucsCapabilityCatalogueProvidersLoaded = _CucsCapabilityCatalogueProvidersLoaded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 1, 1, 20),
    _CucsCapabilityCatalogueProvidersLoaded_Type()
)
cucsCapabilityCatalogueProvidersLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueProvidersLoaded.setStatus("current")
_CucsCapabilityCatalogueFsmTaskTable_Object = MibTable
cucsCapabilityCatalogueFsmTaskTable = _CucsCapabilityCatalogueFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 2)
)
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmTaskTable.setStatus("current")
_CucsCapabilityCatalogueFsmTaskEntry_Object = MibTableRow
cucsCapabilityCatalogueFsmTaskEntry = _CucsCapabilityCatalogueFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 2, 1)
)
cucsCapabilityCatalogueFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilityCatalogueFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmTaskEntry.setStatus("current")
_CucsCapabilityCatalogueFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsCapabilityCatalogueFsmTaskInstanceId_Object = MibTableColumn
cucsCapabilityCatalogueFsmTaskInstanceId = _CucsCapabilityCatalogueFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 2, 1, 1),
    _CucsCapabilityCatalogueFsmTaskInstanceId_Type()
)
cucsCapabilityCatalogueFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmTaskInstanceId.setStatus("current")
_CucsCapabilityCatalogueFsmTaskDn_Type = CucsManagedObjectDn
_CucsCapabilityCatalogueFsmTaskDn_Object = MibTableColumn
cucsCapabilityCatalogueFsmTaskDn = _CucsCapabilityCatalogueFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 2, 1, 2),
    _CucsCapabilityCatalogueFsmTaskDn_Type()
)
cucsCapabilityCatalogueFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmTaskDn.setStatus("current")
_CucsCapabilityCatalogueFsmTaskRn_Type = SnmpAdminString
_CucsCapabilityCatalogueFsmTaskRn_Object = MibTableColumn
cucsCapabilityCatalogueFsmTaskRn = _CucsCapabilityCatalogueFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 2, 1, 3),
    _CucsCapabilityCatalogueFsmTaskRn_Type()
)
cucsCapabilityCatalogueFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmTaskRn.setStatus("current")
_CucsCapabilityCatalogueFsmTaskCompletion_Type = CucsFsmCompletion
_CucsCapabilityCatalogueFsmTaskCompletion_Object = MibTableColumn
cucsCapabilityCatalogueFsmTaskCompletion = _CucsCapabilityCatalogueFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 2, 1, 4),
    _CucsCapabilityCatalogueFsmTaskCompletion_Type()
)
cucsCapabilityCatalogueFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmTaskCompletion.setStatus("current")
_CucsCapabilityCatalogueFsmTaskFlags_Type = CucsFsmFlags
_CucsCapabilityCatalogueFsmTaskFlags_Object = MibTableColumn
cucsCapabilityCatalogueFsmTaskFlags = _CucsCapabilityCatalogueFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 2, 1, 5),
    _CucsCapabilityCatalogueFsmTaskFlags_Type()
)
cucsCapabilityCatalogueFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmTaskFlags.setStatus("current")
_CucsCapabilityCatalogueFsmTaskItem_Type = CucsCapabilityCatalogueFsmTaskItem
_CucsCapabilityCatalogueFsmTaskItem_Object = MibTableColumn
cucsCapabilityCatalogueFsmTaskItem = _CucsCapabilityCatalogueFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 2, 1, 6),
    _CucsCapabilityCatalogueFsmTaskItem_Type()
)
cucsCapabilityCatalogueFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmTaskItem.setStatus("current")
_CucsCapabilityCatalogueFsmTaskSeqId_Type = Gauge32
_CucsCapabilityCatalogueFsmTaskSeqId_Object = MibTableColumn
cucsCapabilityCatalogueFsmTaskSeqId = _CucsCapabilityCatalogueFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 2, 1, 7),
    _CucsCapabilityCatalogueFsmTaskSeqId_Type()
)
cucsCapabilityCatalogueFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmTaskSeqId.setStatus("current")
_CucsCapabilityEpTable_Object = MibTable
cucsCapabilityEpTable = _CucsCapabilityEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 3)
)
if mibBuilder.loadTexts:
    cucsCapabilityEpTable.setStatus("current")
_CucsCapabilityEpEntry_Object = MibTableRow
cucsCapabilityEpEntry = _CucsCapabilityEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 3, 1)
)
cucsCapabilityEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilityEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilityEpEntry.setStatus("current")
_CucsCapabilityEpInstanceId_Type = CucsManagedObjectId
_CucsCapabilityEpInstanceId_Object = MibTableColumn
cucsCapabilityEpInstanceId = _CucsCapabilityEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 3, 1, 1),
    _CucsCapabilityEpInstanceId_Type()
)
cucsCapabilityEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilityEpInstanceId.setStatus("current")
_CucsCapabilityEpDn_Type = CucsManagedObjectDn
_CucsCapabilityEpDn_Object = MibTableColumn
cucsCapabilityEpDn = _CucsCapabilityEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 3, 1, 2),
    _CucsCapabilityEpDn_Type()
)
cucsCapabilityEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityEpDn.setStatus("current")
_CucsCapabilityEpRn_Type = SnmpAdminString
_CucsCapabilityEpRn_Object = MibTableColumn
cucsCapabilityEpRn = _CucsCapabilityEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 3, 1, 3),
    _CucsCapabilityEpRn_Type()
)
cucsCapabilityEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityEpRn.setStatus("current")
_CucsCapabilityMgmtExtensionTable_Object = MibTable
cucsCapabilityMgmtExtensionTable = _CucsCapabilityMgmtExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 4)
)
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionTable.setStatus("current")
_CucsCapabilityMgmtExtensionEntry_Object = MibTableRow
cucsCapabilityMgmtExtensionEntry = _CucsCapabilityMgmtExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 4, 1)
)
cucsCapabilityMgmtExtensionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilityMgmtExtensionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionEntry.setStatus("current")
_CucsCapabilityMgmtExtensionInstanceId_Type = CucsManagedObjectId
_CucsCapabilityMgmtExtensionInstanceId_Object = MibTableColumn
cucsCapabilityMgmtExtensionInstanceId = _CucsCapabilityMgmtExtensionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 4, 1, 1),
    _CucsCapabilityMgmtExtensionInstanceId_Type()
)
cucsCapabilityMgmtExtensionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionInstanceId.setStatus("current")
_CucsCapabilityMgmtExtensionDn_Type = CucsManagedObjectDn
_CucsCapabilityMgmtExtensionDn_Object = MibTableColumn
cucsCapabilityMgmtExtensionDn = _CucsCapabilityMgmtExtensionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 4, 1, 2),
    _CucsCapabilityMgmtExtensionDn_Type()
)
cucsCapabilityMgmtExtensionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionDn.setStatus("current")
_CucsCapabilityMgmtExtensionRn_Type = SnmpAdminString
_CucsCapabilityMgmtExtensionRn_Object = MibTableColumn
cucsCapabilityMgmtExtensionRn = _CucsCapabilityMgmtExtensionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 4, 1, 3),
    _CucsCapabilityMgmtExtensionRn_Type()
)
cucsCapabilityMgmtExtensionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionRn.setStatus("current")
_CucsCapabilityMgmtExtensionFsmDescr_Type = SnmpAdminString
_CucsCapabilityMgmtExtensionFsmDescr_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmDescr = _CucsCapabilityMgmtExtensionFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 4, 1, 4),
    _CucsCapabilityMgmtExtensionFsmDescr_Type()
)
cucsCapabilityMgmtExtensionFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmDescr.setStatus("current")
_CucsCapabilityMgmtExtensionFsmPrev_Type = SnmpAdminString
_CucsCapabilityMgmtExtensionFsmPrev_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmPrev = _CucsCapabilityMgmtExtensionFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 4, 1, 5),
    _CucsCapabilityMgmtExtensionFsmPrev_Type()
)
cucsCapabilityMgmtExtensionFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmPrev.setStatus("current")
_CucsCapabilityMgmtExtensionFsmProgr_Type = Gauge32
_CucsCapabilityMgmtExtensionFsmProgr_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmProgr = _CucsCapabilityMgmtExtensionFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 4, 1, 6),
    _CucsCapabilityMgmtExtensionFsmProgr_Type()
)
cucsCapabilityMgmtExtensionFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmProgr.setStatus("current")
_CucsCapabilityMgmtExtensionFsmRmtInvErrCode_Type = Gauge32
_CucsCapabilityMgmtExtensionFsmRmtInvErrCode_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmRmtInvErrCode = _CucsCapabilityMgmtExtensionFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 4, 1, 7),
    _CucsCapabilityMgmtExtensionFsmRmtInvErrCode_Type()
)
cucsCapabilityMgmtExtensionFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmRmtInvErrCode.setStatus("current")
_CucsCapabilityMgmtExtensionFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsCapabilityMgmtExtensionFsmRmtInvErrDescr_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmRmtInvErrDescr = _CucsCapabilityMgmtExtensionFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 4, 1, 8),
    _CucsCapabilityMgmtExtensionFsmRmtInvErrDescr_Type()
)
cucsCapabilityMgmtExtensionFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmRmtInvErrDescr.setStatus("current")
_CucsCapabilityMgmtExtensionFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsCapabilityMgmtExtensionFsmRmtInvRslt_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmRmtInvRslt = _CucsCapabilityMgmtExtensionFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 4, 1, 9),
    _CucsCapabilityMgmtExtensionFsmRmtInvRslt_Type()
)
cucsCapabilityMgmtExtensionFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmRmtInvRslt.setStatus("current")
_CucsCapabilityMgmtExtensionFsmStageDescr_Type = SnmpAdminString
_CucsCapabilityMgmtExtensionFsmStageDescr_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmStageDescr = _CucsCapabilityMgmtExtensionFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 4, 1, 10),
    _CucsCapabilityMgmtExtensionFsmStageDescr_Type()
)
cucsCapabilityMgmtExtensionFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmStageDescr.setStatus("current")
_CucsCapabilityMgmtExtensionFsmStamp_Type = DateAndTime
_CucsCapabilityMgmtExtensionFsmStamp_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmStamp = _CucsCapabilityMgmtExtensionFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 4, 1, 11),
    _CucsCapabilityMgmtExtensionFsmStamp_Type()
)
cucsCapabilityMgmtExtensionFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmStamp.setStatus("current")
_CucsCapabilityMgmtExtensionFsmStatus_Type = SnmpAdminString
_CucsCapabilityMgmtExtensionFsmStatus_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmStatus = _CucsCapabilityMgmtExtensionFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 4, 1, 12),
    _CucsCapabilityMgmtExtensionFsmStatus_Type()
)
cucsCapabilityMgmtExtensionFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmStatus.setStatus("current")
_CucsCapabilityMgmtExtensionFsmTry_Type = Gauge32
_CucsCapabilityMgmtExtensionFsmTry_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmTry = _CucsCapabilityMgmtExtensionFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 4, 1, 13),
    _CucsCapabilityMgmtExtensionFsmTry_Type()
)
cucsCapabilityMgmtExtensionFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmTry.setStatus("current")
_CucsCapabilityMgmtExtensionFsmTaskTable_Object = MibTable
cucsCapabilityMgmtExtensionFsmTaskTable = _CucsCapabilityMgmtExtensionFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 5)
)
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmTaskTable.setStatus("current")
_CucsCapabilityMgmtExtensionFsmTaskEntry_Object = MibTableRow
cucsCapabilityMgmtExtensionFsmTaskEntry = _CucsCapabilityMgmtExtensionFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 5, 1)
)
cucsCapabilityMgmtExtensionFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilityMgmtExtensionFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmTaskEntry.setStatus("current")
_CucsCapabilityMgmtExtensionFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsCapabilityMgmtExtensionFsmTaskInstanceId_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmTaskInstanceId = _CucsCapabilityMgmtExtensionFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 5, 1, 1),
    _CucsCapabilityMgmtExtensionFsmTaskInstanceId_Type()
)
cucsCapabilityMgmtExtensionFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmTaskInstanceId.setStatus("current")
_CucsCapabilityMgmtExtensionFsmTaskDn_Type = CucsManagedObjectDn
_CucsCapabilityMgmtExtensionFsmTaskDn_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmTaskDn = _CucsCapabilityMgmtExtensionFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 5, 1, 2),
    _CucsCapabilityMgmtExtensionFsmTaskDn_Type()
)
cucsCapabilityMgmtExtensionFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmTaskDn.setStatus("current")
_CucsCapabilityMgmtExtensionFsmTaskRn_Type = SnmpAdminString
_CucsCapabilityMgmtExtensionFsmTaskRn_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmTaskRn = _CucsCapabilityMgmtExtensionFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 5, 1, 3),
    _CucsCapabilityMgmtExtensionFsmTaskRn_Type()
)
cucsCapabilityMgmtExtensionFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmTaskRn.setStatus("current")
_CucsCapabilityMgmtExtensionFsmTaskCompletion_Type = CucsFsmCompletion
_CucsCapabilityMgmtExtensionFsmTaskCompletion_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmTaskCompletion = _CucsCapabilityMgmtExtensionFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 5, 1, 4),
    _CucsCapabilityMgmtExtensionFsmTaskCompletion_Type()
)
cucsCapabilityMgmtExtensionFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmTaskCompletion.setStatus("current")
_CucsCapabilityMgmtExtensionFsmTaskFlags_Type = CucsFsmFlags
_CucsCapabilityMgmtExtensionFsmTaskFlags_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmTaskFlags = _CucsCapabilityMgmtExtensionFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 5, 1, 5),
    _CucsCapabilityMgmtExtensionFsmTaskFlags_Type()
)
cucsCapabilityMgmtExtensionFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmTaskFlags.setStatus("current")
_CucsCapabilityMgmtExtensionFsmTaskItem_Type = CucsCapabilityMgmtExtensionFsmTaskItem
_CucsCapabilityMgmtExtensionFsmTaskItem_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmTaskItem = _CucsCapabilityMgmtExtensionFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 5, 1, 6),
    _CucsCapabilityMgmtExtensionFsmTaskItem_Type()
)
cucsCapabilityMgmtExtensionFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmTaskItem.setStatus("current")
_CucsCapabilityMgmtExtensionFsmTaskSeqId_Type = Gauge32
_CucsCapabilityMgmtExtensionFsmTaskSeqId_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmTaskSeqId = _CucsCapabilityMgmtExtensionFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 5, 1, 7),
    _CucsCapabilityMgmtExtensionFsmTaskSeqId_Type()
)
cucsCapabilityMgmtExtensionFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmTaskSeqId.setStatus("current")
_CucsCapabilityUpdateTable_Object = MibTable
cucsCapabilityUpdateTable = _CucsCapabilityUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 6)
)
if mibBuilder.loadTexts:
    cucsCapabilityUpdateTable.setStatus("current")
_CucsCapabilityUpdateEntry_Object = MibTableRow
cucsCapabilityUpdateEntry = _CucsCapabilityUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 6, 1)
)
cucsCapabilityUpdateEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilityUpdateInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilityUpdateEntry.setStatus("current")
_CucsCapabilityUpdateInstanceId_Type = CucsManagedObjectId
_CucsCapabilityUpdateInstanceId_Object = MibTableColumn
cucsCapabilityUpdateInstanceId = _CucsCapabilityUpdateInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 6, 1, 1),
    _CucsCapabilityUpdateInstanceId_Type()
)
cucsCapabilityUpdateInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilityUpdateInstanceId.setStatus("current")
_CucsCapabilityUpdateDn_Type = CucsManagedObjectDn
_CucsCapabilityUpdateDn_Object = MibTableColumn
cucsCapabilityUpdateDn = _CucsCapabilityUpdateDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 6, 1, 2),
    _CucsCapabilityUpdateDn_Type()
)
cucsCapabilityUpdateDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdateDn.setStatus("current")
_CucsCapabilityUpdateRn_Type = SnmpAdminString
_CucsCapabilityUpdateRn_Object = MibTableColumn
cucsCapabilityUpdateRn = _CucsCapabilityUpdateRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 6, 1, 3),
    _CucsCapabilityUpdateRn_Type()
)
cucsCapabilityUpdateRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdateRn.setStatus("current")
_CucsCapabilityUpdateImageName_Type = SnmpAdminString
_CucsCapabilityUpdateImageName_Object = MibTableColumn
cucsCapabilityUpdateImageName = _CucsCapabilityUpdateImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 6, 1, 4),
    _CucsCapabilityUpdateImageName_Type()
)
cucsCapabilityUpdateImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdateImageName.setStatus("current")
_CucsCapabilityUpdateUpdateTs_Type = DateAndTime
_CucsCapabilityUpdateUpdateTs_Object = MibTableColumn
cucsCapabilityUpdateUpdateTs = _CucsCapabilityUpdateUpdateTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 6, 1, 5),
    _CucsCapabilityUpdateUpdateTs_Type()
)
cucsCapabilityUpdateUpdateTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdateUpdateTs.setStatus("current")
_CucsCapabilityUpdateVersion_Type = SnmpAdminString
_CucsCapabilityUpdateVersion_Object = MibTableColumn
cucsCapabilityUpdateVersion = _CucsCapabilityUpdateVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 6, 1, 6),
    _CucsCapabilityUpdateVersion_Type()
)
cucsCapabilityUpdateVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdateVersion.setStatus("current")
_CucsCapabilityUpdaterTable_Object = MibTable
cucsCapabilityUpdaterTable = _CucsCapabilityUpdaterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7)
)
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterTable.setStatus("current")
_CucsCapabilityUpdaterEntry_Object = MibTableRow
cucsCapabilityUpdaterEntry = _CucsCapabilityUpdaterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1)
)
cucsCapabilityUpdaterEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilityUpdaterInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterEntry.setStatus("current")
_CucsCapabilityUpdaterInstanceId_Type = CucsManagedObjectId
_CucsCapabilityUpdaterInstanceId_Object = MibTableColumn
cucsCapabilityUpdaterInstanceId = _CucsCapabilityUpdaterInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 1),
    _CucsCapabilityUpdaterInstanceId_Type()
)
cucsCapabilityUpdaterInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterInstanceId.setStatus("current")
_CucsCapabilityUpdaterDn_Type = CucsManagedObjectDn
_CucsCapabilityUpdaterDn_Object = MibTableColumn
cucsCapabilityUpdaterDn = _CucsCapabilityUpdaterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 2),
    _CucsCapabilityUpdaterDn_Type()
)
cucsCapabilityUpdaterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterDn.setStatus("current")
_CucsCapabilityUpdaterRn_Type = SnmpAdminString
_CucsCapabilityUpdaterRn_Object = MibTableColumn
cucsCapabilityUpdaterRn = _CucsCapabilityUpdaterRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 3),
    _CucsCapabilityUpdaterRn_Type()
)
cucsCapabilityUpdaterRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterRn.setStatus("current")
_CucsCapabilityUpdaterAdminState_Type = CucsCapabilityAdminState
_CucsCapabilityUpdaterAdminState_Object = MibTableColumn
cucsCapabilityUpdaterAdminState = _CucsCapabilityUpdaterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 4),
    _CucsCapabilityUpdaterAdminState_Type()
)
cucsCapabilityUpdaterAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterAdminState.setStatus("current")
_CucsCapabilityUpdaterFileName_Type = SnmpAdminString
_CucsCapabilityUpdaterFileName_Object = MibTableColumn
cucsCapabilityUpdaterFileName = _CucsCapabilityUpdaterFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 5),
    _CucsCapabilityUpdaterFileName_Type()
)
cucsCapabilityUpdaterFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFileName.setStatus("current")
_CucsCapabilityUpdaterFsmDescr_Type = SnmpAdminString
_CucsCapabilityUpdaterFsmDescr_Object = MibTableColumn
cucsCapabilityUpdaterFsmDescr = _CucsCapabilityUpdaterFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 6),
    _CucsCapabilityUpdaterFsmDescr_Type()
)
cucsCapabilityUpdaterFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmDescr.setStatus("current")
_CucsCapabilityUpdaterFsmPrev_Type = SnmpAdminString
_CucsCapabilityUpdaterFsmPrev_Object = MibTableColumn
cucsCapabilityUpdaterFsmPrev = _CucsCapabilityUpdaterFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 7),
    _CucsCapabilityUpdaterFsmPrev_Type()
)
cucsCapabilityUpdaterFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmPrev.setStatus("current")
_CucsCapabilityUpdaterFsmProgr_Type = Gauge32
_CucsCapabilityUpdaterFsmProgr_Object = MibTableColumn
cucsCapabilityUpdaterFsmProgr = _CucsCapabilityUpdaterFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 8),
    _CucsCapabilityUpdaterFsmProgr_Type()
)
cucsCapabilityUpdaterFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmProgr.setStatus("current")
_CucsCapabilityUpdaterFsmRmtInvErrCode_Type = Gauge32
_CucsCapabilityUpdaterFsmRmtInvErrCode_Object = MibTableColumn
cucsCapabilityUpdaterFsmRmtInvErrCode = _CucsCapabilityUpdaterFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 9),
    _CucsCapabilityUpdaterFsmRmtInvErrCode_Type()
)
cucsCapabilityUpdaterFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmRmtInvErrCode.setStatus("current")
_CucsCapabilityUpdaterFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsCapabilityUpdaterFsmRmtInvErrDescr_Object = MibTableColumn
cucsCapabilityUpdaterFsmRmtInvErrDescr = _CucsCapabilityUpdaterFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 10),
    _CucsCapabilityUpdaterFsmRmtInvErrDescr_Type()
)
cucsCapabilityUpdaterFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmRmtInvErrDescr.setStatus("current")
_CucsCapabilityUpdaterFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsCapabilityUpdaterFsmRmtInvRslt_Object = MibTableColumn
cucsCapabilityUpdaterFsmRmtInvRslt = _CucsCapabilityUpdaterFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 11),
    _CucsCapabilityUpdaterFsmRmtInvRslt_Type()
)
cucsCapabilityUpdaterFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmRmtInvRslt.setStatus("current")
_CucsCapabilityUpdaterFsmStageDescr_Type = SnmpAdminString
_CucsCapabilityUpdaterFsmStageDescr_Object = MibTableColumn
cucsCapabilityUpdaterFsmStageDescr = _CucsCapabilityUpdaterFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 12),
    _CucsCapabilityUpdaterFsmStageDescr_Type()
)
cucsCapabilityUpdaterFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmStageDescr.setStatus("current")
_CucsCapabilityUpdaterFsmStamp_Type = DateAndTime
_CucsCapabilityUpdaterFsmStamp_Object = MibTableColumn
cucsCapabilityUpdaterFsmStamp = _CucsCapabilityUpdaterFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 13),
    _CucsCapabilityUpdaterFsmStamp_Type()
)
cucsCapabilityUpdaterFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmStamp.setStatus("current")
_CucsCapabilityUpdaterFsmStatus_Type = SnmpAdminString
_CucsCapabilityUpdaterFsmStatus_Object = MibTableColumn
cucsCapabilityUpdaterFsmStatus = _CucsCapabilityUpdaterFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 14),
    _CucsCapabilityUpdaterFsmStatus_Type()
)
cucsCapabilityUpdaterFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmStatus.setStatus("current")
_CucsCapabilityUpdaterFsmTry_Type = Gauge32
_CucsCapabilityUpdaterFsmTry_Object = MibTableColumn
cucsCapabilityUpdaterFsmTry = _CucsCapabilityUpdaterFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 15),
    _CucsCapabilityUpdaterFsmTry_Type()
)
cucsCapabilityUpdaterFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmTry.setStatus("current")
_CucsCapabilityUpdaterImageName_Type = SnmpAdminString
_CucsCapabilityUpdaterImageName_Object = MibTableColumn
cucsCapabilityUpdaterImageName = _CucsCapabilityUpdaterImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 16),
    _CucsCapabilityUpdaterImageName_Type()
)
cucsCapabilityUpdaterImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterImageName.setStatus("current")
_CucsCapabilityUpdaterOperState_Type = CucsCapabilityOperStatus
_CucsCapabilityUpdaterOperState_Object = MibTableColumn
cucsCapabilityUpdaterOperState = _CucsCapabilityUpdaterOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 17),
    _CucsCapabilityUpdaterOperState_Type()
)
cucsCapabilityUpdaterOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterOperState.setStatus("current")
_CucsCapabilityUpdaterProtocol_Type = CucsFirmwareTransport
_CucsCapabilityUpdaterProtocol_Object = MibTableColumn
cucsCapabilityUpdaterProtocol = _CucsCapabilityUpdaterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 18),
    _CucsCapabilityUpdaterProtocol_Type()
)
cucsCapabilityUpdaterProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterProtocol.setStatus("current")
_CucsCapabilityUpdaterPwd_Type = SnmpAdminString
_CucsCapabilityUpdaterPwd_Object = MibTableColumn
cucsCapabilityUpdaterPwd = _CucsCapabilityUpdaterPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 19),
    _CucsCapabilityUpdaterPwd_Type()
)
cucsCapabilityUpdaterPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterPwd.setStatus("current")
_CucsCapabilityUpdaterRemotePath_Type = SnmpAdminString
_CucsCapabilityUpdaterRemotePath_Object = MibTableColumn
cucsCapabilityUpdaterRemotePath = _CucsCapabilityUpdaterRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 20),
    _CucsCapabilityUpdaterRemotePath_Type()
)
cucsCapabilityUpdaterRemotePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterRemotePath.setStatus("current")
_CucsCapabilityUpdaterServer_Type = SnmpAdminString
_CucsCapabilityUpdaterServer_Object = MibTableColumn
cucsCapabilityUpdaterServer = _CucsCapabilityUpdaterServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 21),
    _CucsCapabilityUpdaterServer_Type()
)
cucsCapabilityUpdaterServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterServer.setStatus("current")
_CucsCapabilityUpdaterUser_Type = SnmpAdminString
_CucsCapabilityUpdaterUser_Object = MibTableColumn
cucsCapabilityUpdaterUser = _CucsCapabilityUpdaterUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 22),
    _CucsCapabilityUpdaterUser_Type()
)
cucsCapabilityUpdaterUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterUser.setStatus("current")
_CucsCapabilityUpdaterVersion_Type = SnmpAdminString
_CucsCapabilityUpdaterVersion_Object = MibTableColumn
cucsCapabilityUpdaterVersion = _CucsCapabilityUpdaterVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 7, 1, 23),
    _CucsCapabilityUpdaterVersion_Type()
)
cucsCapabilityUpdaterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterVersion.setStatus("current")
_CucsCapabilityUpdaterFsmTaskTable_Object = MibTable
cucsCapabilityUpdaterFsmTaskTable = _CucsCapabilityUpdaterFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 8)
)
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmTaskTable.setStatus("current")
_CucsCapabilityUpdaterFsmTaskEntry_Object = MibTableRow
cucsCapabilityUpdaterFsmTaskEntry = _CucsCapabilityUpdaterFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 8, 1)
)
cucsCapabilityUpdaterFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilityUpdaterFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmTaskEntry.setStatus("current")
_CucsCapabilityUpdaterFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsCapabilityUpdaterFsmTaskInstanceId_Object = MibTableColumn
cucsCapabilityUpdaterFsmTaskInstanceId = _CucsCapabilityUpdaterFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 8, 1, 1),
    _CucsCapabilityUpdaterFsmTaskInstanceId_Type()
)
cucsCapabilityUpdaterFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmTaskInstanceId.setStatus("current")
_CucsCapabilityUpdaterFsmTaskDn_Type = CucsManagedObjectDn
_CucsCapabilityUpdaterFsmTaskDn_Object = MibTableColumn
cucsCapabilityUpdaterFsmTaskDn = _CucsCapabilityUpdaterFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 8, 1, 2),
    _CucsCapabilityUpdaterFsmTaskDn_Type()
)
cucsCapabilityUpdaterFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmTaskDn.setStatus("current")
_CucsCapabilityUpdaterFsmTaskRn_Type = SnmpAdminString
_CucsCapabilityUpdaterFsmTaskRn_Object = MibTableColumn
cucsCapabilityUpdaterFsmTaskRn = _CucsCapabilityUpdaterFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 8, 1, 3),
    _CucsCapabilityUpdaterFsmTaskRn_Type()
)
cucsCapabilityUpdaterFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmTaskRn.setStatus("current")
_CucsCapabilityUpdaterFsmTaskCompletion_Type = CucsFsmCompletion
_CucsCapabilityUpdaterFsmTaskCompletion_Object = MibTableColumn
cucsCapabilityUpdaterFsmTaskCompletion = _CucsCapabilityUpdaterFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 8, 1, 4),
    _CucsCapabilityUpdaterFsmTaskCompletion_Type()
)
cucsCapabilityUpdaterFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmTaskCompletion.setStatus("current")
_CucsCapabilityUpdaterFsmTaskFlags_Type = CucsFsmFlags
_CucsCapabilityUpdaterFsmTaskFlags_Object = MibTableColumn
cucsCapabilityUpdaterFsmTaskFlags = _CucsCapabilityUpdaterFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 8, 1, 5),
    _CucsCapabilityUpdaterFsmTaskFlags_Type()
)
cucsCapabilityUpdaterFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmTaskFlags.setStatus("current")
_CucsCapabilityUpdaterFsmTaskItem_Type = CucsCapabilityUpdaterFsmTaskItem
_CucsCapabilityUpdaterFsmTaskItem_Object = MibTableColumn
cucsCapabilityUpdaterFsmTaskItem = _CucsCapabilityUpdaterFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 8, 1, 6),
    _CucsCapabilityUpdaterFsmTaskItem_Type()
)
cucsCapabilityUpdaterFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmTaskItem.setStatus("current")
_CucsCapabilityUpdaterFsmTaskSeqId_Type = Gauge32
_CucsCapabilityUpdaterFsmTaskSeqId_Object = MibTableColumn
cucsCapabilityUpdaterFsmTaskSeqId = _CucsCapabilityUpdaterFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 8, 1, 7),
    _CucsCapabilityUpdaterFsmTaskSeqId_Type()
)
cucsCapabilityUpdaterFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmTaskSeqId.setStatus("current")
_CucsCapabilityCatalogueFsmTable_Object = MibTable
cucsCapabilityCatalogueFsmTable = _CucsCapabilityCatalogueFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 9)
)
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmTable.setStatus("current")
_CucsCapabilityCatalogueFsmEntry_Object = MibTableRow
cucsCapabilityCatalogueFsmEntry = _CucsCapabilityCatalogueFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 9, 1)
)
cucsCapabilityCatalogueFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilityCatalogueFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmEntry.setStatus("current")
_CucsCapabilityCatalogueFsmInstanceId_Type = CucsManagedObjectId
_CucsCapabilityCatalogueFsmInstanceId_Object = MibTableColumn
cucsCapabilityCatalogueFsmInstanceId = _CucsCapabilityCatalogueFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 9, 1, 1),
    _CucsCapabilityCatalogueFsmInstanceId_Type()
)
cucsCapabilityCatalogueFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmInstanceId.setStatus("current")
_CucsCapabilityCatalogueFsmDn_Type = CucsManagedObjectDn
_CucsCapabilityCatalogueFsmDn_Object = MibTableColumn
cucsCapabilityCatalogueFsmDn = _CucsCapabilityCatalogueFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 9, 1, 2),
    _CucsCapabilityCatalogueFsmDn_Type()
)
cucsCapabilityCatalogueFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmDn.setStatus("current")
_CucsCapabilityCatalogueFsmRn_Type = SnmpAdminString
_CucsCapabilityCatalogueFsmRn_Object = MibTableColumn
cucsCapabilityCatalogueFsmRn = _CucsCapabilityCatalogueFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 9, 1, 3),
    _CucsCapabilityCatalogueFsmRn_Type()
)
cucsCapabilityCatalogueFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmRn.setStatus("current")
_CucsCapabilityCatalogueFsmCompletionTime_Type = DateAndTime
_CucsCapabilityCatalogueFsmCompletionTime_Object = MibTableColumn
cucsCapabilityCatalogueFsmCompletionTime = _CucsCapabilityCatalogueFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 9, 1, 4),
    _CucsCapabilityCatalogueFsmCompletionTime_Type()
)
cucsCapabilityCatalogueFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmCompletionTime.setStatus("current")
_CucsCapabilityCatalogueFsmCurrentFsm_Type = CucsCapabilityCatalogueFsmCurrentFsm
_CucsCapabilityCatalogueFsmCurrentFsm_Object = MibTableColumn
cucsCapabilityCatalogueFsmCurrentFsm = _CucsCapabilityCatalogueFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 9, 1, 5),
    _CucsCapabilityCatalogueFsmCurrentFsm_Type()
)
cucsCapabilityCatalogueFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmCurrentFsm.setStatus("current")
_CucsCapabilityCatalogueFsmDescrData_Type = SnmpAdminString
_CucsCapabilityCatalogueFsmDescrData_Object = MibTableColumn
cucsCapabilityCatalogueFsmDescrData = _CucsCapabilityCatalogueFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 9, 1, 6),
    _CucsCapabilityCatalogueFsmDescrData_Type()
)
cucsCapabilityCatalogueFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmDescrData.setStatus("current")
_CucsCapabilityCatalogueFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsCapabilityCatalogueFsmFsmStatus_Object = MibTableColumn
cucsCapabilityCatalogueFsmFsmStatus = _CucsCapabilityCatalogueFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 9, 1, 7),
    _CucsCapabilityCatalogueFsmFsmStatus_Type()
)
cucsCapabilityCatalogueFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmFsmStatus.setStatus("current")
_CucsCapabilityCatalogueFsmProgress_Type = Gauge32
_CucsCapabilityCatalogueFsmProgress_Object = MibTableColumn
cucsCapabilityCatalogueFsmProgress = _CucsCapabilityCatalogueFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 9, 1, 8),
    _CucsCapabilityCatalogueFsmProgress_Type()
)
cucsCapabilityCatalogueFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmProgress.setStatus("current")
_CucsCapabilityCatalogueFsmRmtErrCode_Type = Gauge32
_CucsCapabilityCatalogueFsmRmtErrCode_Object = MibTableColumn
cucsCapabilityCatalogueFsmRmtErrCode = _CucsCapabilityCatalogueFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 9, 1, 9),
    _CucsCapabilityCatalogueFsmRmtErrCode_Type()
)
cucsCapabilityCatalogueFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmRmtErrCode.setStatus("current")
_CucsCapabilityCatalogueFsmRmtErrDescr_Type = SnmpAdminString
_CucsCapabilityCatalogueFsmRmtErrDescr_Object = MibTableColumn
cucsCapabilityCatalogueFsmRmtErrDescr = _CucsCapabilityCatalogueFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 9, 1, 10),
    _CucsCapabilityCatalogueFsmRmtErrDescr_Type()
)
cucsCapabilityCatalogueFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmRmtErrDescr.setStatus("current")
_CucsCapabilityCatalogueFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsCapabilityCatalogueFsmRmtRslt_Object = MibTableColumn
cucsCapabilityCatalogueFsmRmtRslt = _CucsCapabilityCatalogueFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 9, 1, 11),
    _CucsCapabilityCatalogueFsmRmtRslt_Type()
)
cucsCapabilityCatalogueFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmRmtRslt.setStatus("current")
_CucsCapabilityCatalogueFsmStageTable_Object = MibTable
cucsCapabilityCatalogueFsmStageTable = _CucsCapabilityCatalogueFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 10)
)
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmStageTable.setStatus("current")
_CucsCapabilityCatalogueFsmStageEntry_Object = MibTableRow
cucsCapabilityCatalogueFsmStageEntry = _CucsCapabilityCatalogueFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 10, 1)
)
cucsCapabilityCatalogueFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilityCatalogueFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmStageEntry.setStatus("current")
_CucsCapabilityCatalogueFsmStageInstanceId_Type = CucsManagedObjectId
_CucsCapabilityCatalogueFsmStageInstanceId_Object = MibTableColumn
cucsCapabilityCatalogueFsmStageInstanceId = _CucsCapabilityCatalogueFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 10, 1, 1),
    _CucsCapabilityCatalogueFsmStageInstanceId_Type()
)
cucsCapabilityCatalogueFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmStageInstanceId.setStatus("current")
_CucsCapabilityCatalogueFsmStageDn_Type = CucsManagedObjectDn
_CucsCapabilityCatalogueFsmStageDn_Object = MibTableColumn
cucsCapabilityCatalogueFsmStageDn = _CucsCapabilityCatalogueFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 10, 1, 2),
    _CucsCapabilityCatalogueFsmStageDn_Type()
)
cucsCapabilityCatalogueFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmStageDn.setStatus("current")
_CucsCapabilityCatalogueFsmStageRn_Type = SnmpAdminString
_CucsCapabilityCatalogueFsmStageRn_Object = MibTableColumn
cucsCapabilityCatalogueFsmStageRn = _CucsCapabilityCatalogueFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 10, 1, 3),
    _CucsCapabilityCatalogueFsmStageRn_Type()
)
cucsCapabilityCatalogueFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmStageRn.setStatus("current")
_CucsCapabilityCatalogueFsmStageDescrData_Type = SnmpAdminString
_CucsCapabilityCatalogueFsmStageDescrData_Object = MibTableColumn
cucsCapabilityCatalogueFsmStageDescrData = _CucsCapabilityCatalogueFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 10, 1, 4),
    _CucsCapabilityCatalogueFsmStageDescrData_Type()
)
cucsCapabilityCatalogueFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmStageDescrData.setStatus("current")
_CucsCapabilityCatalogueFsmStageLastUpdateTime_Type = DateAndTime
_CucsCapabilityCatalogueFsmStageLastUpdateTime_Object = MibTableColumn
cucsCapabilityCatalogueFsmStageLastUpdateTime = _CucsCapabilityCatalogueFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 10, 1, 5),
    _CucsCapabilityCatalogueFsmStageLastUpdateTime_Type()
)
cucsCapabilityCatalogueFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmStageLastUpdateTime.setStatus("current")
_CucsCapabilityCatalogueFsmStageName_Type = CucsCapabilityCatalogueFsmStageName
_CucsCapabilityCatalogueFsmStageName_Object = MibTableColumn
cucsCapabilityCatalogueFsmStageName = _CucsCapabilityCatalogueFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 10, 1, 6),
    _CucsCapabilityCatalogueFsmStageName_Type()
)
cucsCapabilityCatalogueFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmStageName.setStatus("current")
_CucsCapabilityCatalogueFsmStageOrder_Type = Gauge32
_CucsCapabilityCatalogueFsmStageOrder_Object = MibTableColumn
cucsCapabilityCatalogueFsmStageOrder = _CucsCapabilityCatalogueFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 10, 1, 7),
    _CucsCapabilityCatalogueFsmStageOrder_Type()
)
cucsCapabilityCatalogueFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmStageOrder.setStatus("current")
_CucsCapabilityCatalogueFsmStageRetry_Type = Gauge32
_CucsCapabilityCatalogueFsmStageRetry_Object = MibTableColumn
cucsCapabilityCatalogueFsmStageRetry = _CucsCapabilityCatalogueFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 10, 1, 8),
    _CucsCapabilityCatalogueFsmStageRetry_Type()
)
cucsCapabilityCatalogueFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmStageRetry.setStatus("current")
_CucsCapabilityCatalogueFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsCapabilityCatalogueFsmStageStageStatus_Object = MibTableColumn
cucsCapabilityCatalogueFsmStageStageStatus = _CucsCapabilityCatalogueFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 10, 1, 9),
    _CucsCapabilityCatalogueFsmStageStageStatus_Type()
)
cucsCapabilityCatalogueFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityCatalogueFsmStageStageStatus.setStatus("current")
_CucsCapabilityFeatureLimitsTable_Object = MibTable
cucsCapabilityFeatureLimitsTable = _CucsCapabilityFeatureLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 11)
)
if mibBuilder.loadTexts:
    cucsCapabilityFeatureLimitsTable.setStatus("current")
_CucsCapabilityFeatureLimitsEntry_Object = MibTableRow
cucsCapabilityFeatureLimitsEntry = _CucsCapabilityFeatureLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 11, 1)
)
cucsCapabilityFeatureLimitsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilityFeatureLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilityFeatureLimitsEntry.setStatus("current")
_CucsCapabilityFeatureLimitsInstanceId_Type = CucsManagedObjectId
_CucsCapabilityFeatureLimitsInstanceId_Object = MibTableColumn
cucsCapabilityFeatureLimitsInstanceId = _CucsCapabilityFeatureLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 11, 1, 1),
    _CucsCapabilityFeatureLimitsInstanceId_Type()
)
cucsCapabilityFeatureLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilityFeatureLimitsInstanceId.setStatus("current")
_CucsCapabilityFeatureLimitsDn_Type = CucsManagedObjectDn
_CucsCapabilityFeatureLimitsDn_Object = MibTableColumn
cucsCapabilityFeatureLimitsDn = _CucsCapabilityFeatureLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 11, 1, 2),
    _CucsCapabilityFeatureLimitsDn_Type()
)
cucsCapabilityFeatureLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityFeatureLimitsDn.setStatus("current")
_CucsCapabilityFeatureLimitsRn_Type = SnmpAdminString
_CucsCapabilityFeatureLimitsRn_Object = MibTableColumn
cucsCapabilityFeatureLimitsRn = _CucsCapabilityFeatureLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 11, 1, 3),
    _CucsCapabilityFeatureLimitsRn_Type()
)
cucsCapabilityFeatureLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityFeatureLimitsRn.setStatus("current")
_CucsCapabilityFeatureLimitsDescr_Type = SnmpAdminString
_CucsCapabilityFeatureLimitsDescr_Object = MibTableColumn
cucsCapabilityFeatureLimitsDescr = _CucsCapabilityFeatureLimitsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 11, 1, 4),
    _CucsCapabilityFeatureLimitsDescr_Type()
)
cucsCapabilityFeatureLimitsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityFeatureLimitsDescr.setStatus("current")
_CucsCapabilityFeatureLimitsFeatureStatus_Type = CucsCapabilityFeatureStatus
_CucsCapabilityFeatureLimitsFeatureStatus_Object = MibTableColumn
cucsCapabilityFeatureLimitsFeatureStatus = _CucsCapabilityFeatureLimitsFeatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 11, 1, 5),
    _CucsCapabilityFeatureLimitsFeatureStatus_Type()
)
cucsCapabilityFeatureLimitsFeatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityFeatureLimitsFeatureStatus.setStatus("current")
_CucsCapabilityFeatureLimitsLimit_Type = Gauge32
_CucsCapabilityFeatureLimitsLimit_Object = MibTableColumn
cucsCapabilityFeatureLimitsLimit = _CucsCapabilityFeatureLimitsLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 11, 1, 6),
    _CucsCapabilityFeatureLimitsLimit_Type()
)
cucsCapabilityFeatureLimitsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityFeatureLimitsLimit.setStatus("current")
_CucsCapabilityFeatureLimitsName_Type = SnmpAdminString
_CucsCapabilityFeatureLimitsName_Object = MibTableColumn
cucsCapabilityFeatureLimitsName = _CucsCapabilityFeatureLimitsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 11, 1, 7),
    _CucsCapabilityFeatureLimitsName_Type()
)
cucsCapabilityFeatureLimitsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityFeatureLimitsName.setStatus("current")
_CucsCapabilityFeatureLimitsPlatform_Type = CucsCapabilityPlatform
_CucsCapabilityFeatureLimitsPlatform_Object = MibTableColumn
cucsCapabilityFeatureLimitsPlatform = _CucsCapabilityFeatureLimitsPlatform_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 11, 1, 8),
    _CucsCapabilityFeatureLimitsPlatform_Type()
)
cucsCapabilityFeatureLimitsPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityFeatureLimitsPlatform.setStatus("current")
_CucsCapabilityMgmtExtensionFsmTable_Object = MibTable
cucsCapabilityMgmtExtensionFsmTable = _CucsCapabilityMgmtExtensionFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 12)
)
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmTable.setStatus("current")
_CucsCapabilityMgmtExtensionFsmEntry_Object = MibTableRow
cucsCapabilityMgmtExtensionFsmEntry = _CucsCapabilityMgmtExtensionFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 12, 1)
)
cucsCapabilityMgmtExtensionFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilityMgmtExtensionFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmEntry.setStatus("current")
_CucsCapabilityMgmtExtensionFsmInstanceId_Type = CucsManagedObjectId
_CucsCapabilityMgmtExtensionFsmInstanceId_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmInstanceId = _CucsCapabilityMgmtExtensionFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 12, 1, 1),
    _CucsCapabilityMgmtExtensionFsmInstanceId_Type()
)
cucsCapabilityMgmtExtensionFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmInstanceId.setStatus("current")
_CucsCapabilityMgmtExtensionFsmDn_Type = CucsManagedObjectDn
_CucsCapabilityMgmtExtensionFsmDn_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmDn = _CucsCapabilityMgmtExtensionFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 12, 1, 2),
    _CucsCapabilityMgmtExtensionFsmDn_Type()
)
cucsCapabilityMgmtExtensionFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmDn.setStatus("current")
_CucsCapabilityMgmtExtensionFsmRn_Type = SnmpAdminString
_CucsCapabilityMgmtExtensionFsmRn_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmRn = _CucsCapabilityMgmtExtensionFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 12, 1, 3),
    _CucsCapabilityMgmtExtensionFsmRn_Type()
)
cucsCapabilityMgmtExtensionFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmRn.setStatus("current")
_CucsCapabilityMgmtExtensionFsmCompletionTime_Type = DateAndTime
_CucsCapabilityMgmtExtensionFsmCompletionTime_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmCompletionTime = _CucsCapabilityMgmtExtensionFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 12, 1, 4),
    _CucsCapabilityMgmtExtensionFsmCompletionTime_Type()
)
cucsCapabilityMgmtExtensionFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmCompletionTime.setStatus("current")
_CucsCapabilityMgmtExtensionFsmCurrentFsm_Type = CucsCapabilityMgmtExtensionFsmCurrentFsm
_CucsCapabilityMgmtExtensionFsmCurrentFsm_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmCurrentFsm = _CucsCapabilityMgmtExtensionFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 12, 1, 5),
    _CucsCapabilityMgmtExtensionFsmCurrentFsm_Type()
)
cucsCapabilityMgmtExtensionFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmCurrentFsm.setStatus("current")
_CucsCapabilityMgmtExtensionFsmDescrData_Type = SnmpAdminString
_CucsCapabilityMgmtExtensionFsmDescrData_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmDescrData = _CucsCapabilityMgmtExtensionFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 12, 1, 6),
    _CucsCapabilityMgmtExtensionFsmDescrData_Type()
)
cucsCapabilityMgmtExtensionFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmDescrData.setStatus("current")
_CucsCapabilityMgmtExtensionFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsCapabilityMgmtExtensionFsmFsmStatus_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmFsmStatus = _CucsCapabilityMgmtExtensionFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 12, 1, 7),
    _CucsCapabilityMgmtExtensionFsmFsmStatus_Type()
)
cucsCapabilityMgmtExtensionFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmFsmStatus.setStatus("current")
_CucsCapabilityMgmtExtensionFsmProgress_Type = Gauge32
_CucsCapabilityMgmtExtensionFsmProgress_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmProgress = _CucsCapabilityMgmtExtensionFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 12, 1, 8),
    _CucsCapabilityMgmtExtensionFsmProgress_Type()
)
cucsCapabilityMgmtExtensionFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmProgress.setStatus("current")
_CucsCapabilityMgmtExtensionFsmRmtErrCode_Type = Gauge32
_CucsCapabilityMgmtExtensionFsmRmtErrCode_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmRmtErrCode = _CucsCapabilityMgmtExtensionFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 12, 1, 9),
    _CucsCapabilityMgmtExtensionFsmRmtErrCode_Type()
)
cucsCapabilityMgmtExtensionFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmRmtErrCode.setStatus("current")
_CucsCapabilityMgmtExtensionFsmRmtErrDescr_Type = SnmpAdminString
_CucsCapabilityMgmtExtensionFsmRmtErrDescr_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmRmtErrDescr = _CucsCapabilityMgmtExtensionFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 12, 1, 10),
    _CucsCapabilityMgmtExtensionFsmRmtErrDescr_Type()
)
cucsCapabilityMgmtExtensionFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmRmtErrDescr.setStatus("current")
_CucsCapabilityMgmtExtensionFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsCapabilityMgmtExtensionFsmRmtRslt_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmRmtRslt = _CucsCapabilityMgmtExtensionFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 12, 1, 11),
    _CucsCapabilityMgmtExtensionFsmRmtRslt_Type()
)
cucsCapabilityMgmtExtensionFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmRmtRslt.setStatus("current")
_CucsCapabilityMgmtExtensionFsmStageTable_Object = MibTable
cucsCapabilityMgmtExtensionFsmStageTable = _CucsCapabilityMgmtExtensionFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 13)
)
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmStageTable.setStatus("current")
_CucsCapabilityMgmtExtensionFsmStageEntry_Object = MibTableRow
cucsCapabilityMgmtExtensionFsmStageEntry = _CucsCapabilityMgmtExtensionFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 13, 1)
)
cucsCapabilityMgmtExtensionFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilityMgmtExtensionFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmStageEntry.setStatus("current")
_CucsCapabilityMgmtExtensionFsmStageInstanceId_Type = CucsManagedObjectId
_CucsCapabilityMgmtExtensionFsmStageInstanceId_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmStageInstanceId = _CucsCapabilityMgmtExtensionFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 13, 1, 1),
    _CucsCapabilityMgmtExtensionFsmStageInstanceId_Type()
)
cucsCapabilityMgmtExtensionFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmStageInstanceId.setStatus("current")
_CucsCapabilityMgmtExtensionFsmStageDn_Type = CucsManagedObjectDn
_CucsCapabilityMgmtExtensionFsmStageDn_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmStageDn = _CucsCapabilityMgmtExtensionFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 13, 1, 2),
    _CucsCapabilityMgmtExtensionFsmStageDn_Type()
)
cucsCapabilityMgmtExtensionFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmStageDn.setStatus("current")
_CucsCapabilityMgmtExtensionFsmStageRn_Type = SnmpAdminString
_CucsCapabilityMgmtExtensionFsmStageRn_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmStageRn = _CucsCapabilityMgmtExtensionFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 13, 1, 3),
    _CucsCapabilityMgmtExtensionFsmStageRn_Type()
)
cucsCapabilityMgmtExtensionFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmStageRn.setStatus("current")
_CucsCapabilityMgmtExtensionFsmStageDescrData_Type = SnmpAdminString
_CucsCapabilityMgmtExtensionFsmStageDescrData_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmStageDescrData = _CucsCapabilityMgmtExtensionFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 13, 1, 4),
    _CucsCapabilityMgmtExtensionFsmStageDescrData_Type()
)
cucsCapabilityMgmtExtensionFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmStageDescrData.setStatus("current")
_CucsCapabilityMgmtExtensionFsmStageLastUpdateTime_Type = DateAndTime
_CucsCapabilityMgmtExtensionFsmStageLastUpdateTime_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmStageLastUpdateTime = _CucsCapabilityMgmtExtensionFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 13, 1, 5),
    _CucsCapabilityMgmtExtensionFsmStageLastUpdateTime_Type()
)
cucsCapabilityMgmtExtensionFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmStageLastUpdateTime.setStatus("current")
_CucsCapabilityMgmtExtensionFsmStageName_Type = CucsCapabilityMgmtExtensionFsmStageName
_CucsCapabilityMgmtExtensionFsmStageName_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmStageName = _CucsCapabilityMgmtExtensionFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 13, 1, 6),
    _CucsCapabilityMgmtExtensionFsmStageName_Type()
)
cucsCapabilityMgmtExtensionFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmStageName.setStatus("current")
_CucsCapabilityMgmtExtensionFsmStageOrder_Type = Gauge32
_CucsCapabilityMgmtExtensionFsmStageOrder_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmStageOrder = _CucsCapabilityMgmtExtensionFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 13, 1, 7),
    _CucsCapabilityMgmtExtensionFsmStageOrder_Type()
)
cucsCapabilityMgmtExtensionFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmStageOrder.setStatus("current")
_CucsCapabilityMgmtExtensionFsmStageRetry_Type = Gauge32
_CucsCapabilityMgmtExtensionFsmStageRetry_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmStageRetry = _CucsCapabilityMgmtExtensionFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 13, 1, 8),
    _CucsCapabilityMgmtExtensionFsmStageRetry_Type()
)
cucsCapabilityMgmtExtensionFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmStageRetry.setStatus("current")
_CucsCapabilityMgmtExtensionFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsCapabilityMgmtExtensionFsmStageStageStatus_Object = MibTableColumn
cucsCapabilityMgmtExtensionFsmStageStageStatus = _CucsCapabilityMgmtExtensionFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 13, 1, 9),
    _CucsCapabilityMgmtExtensionFsmStageStageStatus_Type()
)
cucsCapabilityMgmtExtensionFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityMgmtExtensionFsmStageStageStatus.setStatus("current")
_CucsCapabilityNetworkLimitsTable_Object = MibTable
cucsCapabilityNetworkLimitsTable = _CucsCapabilityNetworkLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 14)
)
if mibBuilder.loadTexts:
    cucsCapabilityNetworkLimitsTable.setStatus("current")
_CucsCapabilityNetworkLimitsEntry_Object = MibTableRow
cucsCapabilityNetworkLimitsEntry = _CucsCapabilityNetworkLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 14, 1)
)
cucsCapabilityNetworkLimitsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilityNetworkLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilityNetworkLimitsEntry.setStatus("current")
_CucsCapabilityNetworkLimitsInstanceId_Type = CucsManagedObjectId
_CucsCapabilityNetworkLimitsInstanceId_Object = MibTableColumn
cucsCapabilityNetworkLimitsInstanceId = _CucsCapabilityNetworkLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 14, 1, 1),
    _CucsCapabilityNetworkLimitsInstanceId_Type()
)
cucsCapabilityNetworkLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilityNetworkLimitsInstanceId.setStatus("current")
_CucsCapabilityNetworkLimitsDn_Type = CucsManagedObjectDn
_CucsCapabilityNetworkLimitsDn_Object = MibTableColumn
cucsCapabilityNetworkLimitsDn = _CucsCapabilityNetworkLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 14, 1, 2),
    _CucsCapabilityNetworkLimitsDn_Type()
)
cucsCapabilityNetworkLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityNetworkLimitsDn.setStatus("current")
_CucsCapabilityNetworkLimitsRn_Type = SnmpAdminString
_CucsCapabilityNetworkLimitsRn_Object = MibTableColumn
cucsCapabilityNetworkLimitsRn = _CucsCapabilityNetworkLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 14, 1, 3),
    _CucsCapabilityNetworkLimitsRn_Type()
)
cucsCapabilityNetworkLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityNetworkLimitsRn.setStatus("current")
_CucsCapabilityStorageLimitsTable_Object = MibTable
cucsCapabilityStorageLimitsTable = _CucsCapabilityStorageLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 15)
)
if mibBuilder.loadTexts:
    cucsCapabilityStorageLimitsTable.setStatus("current")
_CucsCapabilityStorageLimitsEntry_Object = MibTableRow
cucsCapabilityStorageLimitsEntry = _CucsCapabilityStorageLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 15, 1)
)
cucsCapabilityStorageLimitsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilityStorageLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilityStorageLimitsEntry.setStatus("current")
_CucsCapabilityStorageLimitsInstanceId_Type = CucsManagedObjectId
_CucsCapabilityStorageLimitsInstanceId_Object = MibTableColumn
cucsCapabilityStorageLimitsInstanceId = _CucsCapabilityStorageLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 15, 1, 1),
    _CucsCapabilityStorageLimitsInstanceId_Type()
)
cucsCapabilityStorageLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilityStorageLimitsInstanceId.setStatus("current")
_CucsCapabilityStorageLimitsDn_Type = CucsManagedObjectDn
_CucsCapabilityStorageLimitsDn_Object = MibTableColumn
cucsCapabilityStorageLimitsDn = _CucsCapabilityStorageLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 15, 1, 2),
    _CucsCapabilityStorageLimitsDn_Type()
)
cucsCapabilityStorageLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityStorageLimitsDn.setStatus("current")
_CucsCapabilityStorageLimitsRn_Type = SnmpAdminString
_CucsCapabilityStorageLimitsRn_Object = MibTableColumn
cucsCapabilityStorageLimitsRn = _CucsCapabilityStorageLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 15, 1, 3),
    _CucsCapabilityStorageLimitsRn_Type()
)
cucsCapabilityStorageLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityStorageLimitsRn.setStatus("current")
_CucsCapabilitySystemLimitsTable_Object = MibTable
cucsCapabilitySystemLimitsTable = _CucsCapabilitySystemLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 16)
)
if mibBuilder.loadTexts:
    cucsCapabilitySystemLimitsTable.setStatus("current")
_CucsCapabilitySystemLimitsEntry_Object = MibTableRow
cucsCapabilitySystemLimitsEntry = _CucsCapabilitySystemLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 16, 1)
)
cucsCapabilitySystemLimitsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilitySystemLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilitySystemLimitsEntry.setStatus("current")
_CucsCapabilitySystemLimitsInstanceId_Type = CucsManagedObjectId
_CucsCapabilitySystemLimitsInstanceId_Object = MibTableColumn
cucsCapabilitySystemLimitsInstanceId = _CucsCapabilitySystemLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 16, 1, 1),
    _CucsCapabilitySystemLimitsInstanceId_Type()
)
cucsCapabilitySystemLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilitySystemLimitsInstanceId.setStatus("current")
_CucsCapabilitySystemLimitsDn_Type = CucsManagedObjectDn
_CucsCapabilitySystemLimitsDn_Object = MibTableColumn
cucsCapabilitySystemLimitsDn = _CucsCapabilitySystemLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 16, 1, 2),
    _CucsCapabilitySystemLimitsDn_Type()
)
cucsCapabilitySystemLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilitySystemLimitsDn.setStatus("current")
_CucsCapabilitySystemLimitsRn_Type = SnmpAdminString
_CucsCapabilitySystemLimitsRn_Object = MibTableColumn
cucsCapabilitySystemLimitsRn = _CucsCapabilitySystemLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 16, 1, 3),
    _CucsCapabilitySystemLimitsRn_Type()
)
cucsCapabilitySystemLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilitySystemLimitsRn.setStatus("current")
_CucsCapabilityUpdaterFsmTable_Object = MibTable
cucsCapabilityUpdaterFsmTable = _CucsCapabilityUpdaterFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 17)
)
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmTable.setStatus("current")
_CucsCapabilityUpdaterFsmEntry_Object = MibTableRow
cucsCapabilityUpdaterFsmEntry = _CucsCapabilityUpdaterFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 17, 1)
)
cucsCapabilityUpdaterFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilityUpdaterFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmEntry.setStatus("current")
_CucsCapabilityUpdaterFsmInstanceId_Type = CucsManagedObjectId
_CucsCapabilityUpdaterFsmInstanceId_Object = MibTableColumn
cucsCapabilityUpdaterFsmInstanceId = _CucsCapabilityUpdaterFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 17, 1, 1),
    _CucsCapabilityUpdaterFsmInstanceId_Type()
)
cucsCapabilityUpdaterFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmInstanceId.setStatus("current")
_CucsCapabilityUpdaterFsmDn_Type = CucsManagedObjectDn
_CucsCapabilityUpdaterFsmDn_Object = MibTableColumn
cucsCapabilityUpdaterFsmDn = _CucsCapabilityUpdaterFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 17, 1, 2),
    _CucsCapabilityUpdaterFsmDn_Type()
)
cucsCapabilityUpdaterFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmDn.setStatus("current")
_CucsCapabilityUpdaterFsmRn_Type = SnmpAdminString
_CucsCapabilityUpdaterFsmRn_Object = MibTableColumn
cucsCapabilityUpdaterFsmRn = _CucsCapabilityUpdaterFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 17, 1, 3),
    _CucsCapabilityUpdaterFsmRn_Type()
)
cucsCapabilityUpdaterFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmRn.setStatus("current")
_CucsCapabilityUpdaterFsmCompletionTime_Type = DateAndTime
_CucsCapabilityUpdaterFsmCompletionTime_Object = MibTableColumn
cucsCapabilityUpdaterFsmCompletionTime = _CucsCapabilityUpdaterFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 17, 1, 4),
    _CucsCapabilityUpdaterFsmCompletionTime_Type()
)
cucsCapabilityUpdaterFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmCompletionTime.setStatus("current")
_CucsCapabilityUpdaterFsmCurrentFsm_Type = CucsCapabilityUpdaterFsmCurrentFsm
_CucsCapabilityUpdaterFsmCurrentFsm_Object = MibTableColumn
cucsCapabilityUpdaterFsmCurrentFsm = _CucsCapabilityUpdaterFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 17, 1, 5),
    _CucsCapabilityUpdaterFsmCurrentFsm_Type()
)
cucsCapabilityUpdaterFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmCurrentFsm.setStatus("current")
_CucsCapabilityUpdaterFsmDescrData_Type = SnmpAdminString
_CucsCapabilityUpdaterFsmDescrData_Object = MibTableColumn
cucsCapabilityUpdaterFsmDescrData = _CucsCapabilityUpdaterFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 17, 1, 6),
    _CucsCapabilityUpdaterFsmDescrData_Type()
)
cucsCapabilityUpdaterFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmDescrData.setStatus("current")
_CucsCapabilityUpdaterFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsCapabilityUpdaterFsmFsmStatus_Object = MibTableColumn
cucsCapabilityUpdaterFsmFsmStatus = _CucsCapabilityUpdaterFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 17, 1, 7),
    _CucsCapabilityUpdaterFsmFsmStatus_Type()
)
cucsCapabilityUpdaterFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmFsmStatus.setStatus("current")
_CucsCapabilityUpdaterFsmProgress_Type = Gauge32
_CucsCapabilityUpdaterFsmProgress_Object = MibTableColumn
cucsCapabilityUpdaterFsmProgress = _CucsCapabilityUpdaterFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 17, 1, 8),
    _CucsCapabilityUpdaterFsmProgress_Type()
)
cucsCapabilityUpdaterFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmProgress.setStatus("current")
_CucsCapabilityUpdaterFsmRmtErrCode_Type = Gauge32
_CucsCapabilityUpdaterFsmRmtErrCode_Object = MibTableColumn
cucsCapabilityUpdaterFsmRmtErrCode = _CucsCapabilityUpdaterFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 17, 1, 9),
    _CucsCapabilityUpdaterFsmRmtErrCode_Type()
)
cucsCapabilityUpdaterFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmRmtErrCode.setStatus("current")
_CucsCapabilityUpdaterFsmRmtErrDescr_Type = SnmpAdminString
_CucsCapabilityUpdaterFsmRmtErrDescr_Object = MibTableColumn
cucsCapabilityUpdaterFsmRmtErrDescr = _CucsCapabilityUpdaterFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 17, 1, 10),
    _CucsCapabilityUpdaterFsmRmtErrDescr_Type()
)
cucsCapabilityUpdaterFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmRmtErrDescr.setStatus("current")
_CucsCapabilityUpdaterFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsCapabilityUpdaterFsmRmtRslt_Object = MibTableColumn
cucsCapabilityUpdaterFsmRmtRslt = _CucsCapabilityUpdaterFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 17, 1, 11),
    _CucsCapabilityUpdaterFsmRmtRslt_Type()
)
cucsCapabilityUpdaterFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmRmtRslt.setStatus("current")
_CucsCapabilityUpdaterFsmStageTable_Object = MibTable
cucsCapabilityUpdaterFsmStageTable = _CucsCapabilityUpdaterFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 18)
)
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmStageTable.setStatus("current")
_CucsCapabilityUpdaterFsmStageEntry_Object = MibTableRow
cucsCapabilityUpdaterFsmStageEntry = _CucsCapabilityUpdaterFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 18, 1)
)
cucsCapabilityUpdaterFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB", "cucsCapabilityUpdaterFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmStageEntry.setStatus("current")
_CucsCapabilityUpdaterFsmStageInstanceId_Type = CucsManagedObjectId
_CucsCapabilityUpdaterFsmStageInstanceId_Object = MibTableColumn
cucsCapabilityUpdaterFsmStageInstanceId = _CucsCapabilityUpdaterFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 18, 1, 1),
    _CucsCapabilityUpdaterFsmStageInstanceId_Type()
)
cucsCapabilityUpdaterFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmStageInstanceId.setStatus("current")
_CucsCapabilityUpdaterFsmStageDn_Type = CucsManagedObjectDn
_CucsCapabilityUpdaterFsmStageDn_Object = MibTableColumn
cucsCapabilityUpdaterFsmStageDn = _CucsCapabilityUpdaterFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 18, 1, 2),
    _CucsCapabilityUpdaterFsmStageDn_Type()
)
cucsCapabilityUpdaterFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmStageDn.setStatus("current")
_CucsCapabilityUpdaterFsmStageRn_Type = SnmpAdminString
_CucsCapabilityUpdaterFsmStageRn_Object = MibTableColumn
cucsCapabilityUpdaterFsmStageRn = _CucsCapabilityUpdaterFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 18, 1, 3),
    _CucsCapabilityUpdaterFsmStageRn_Type()
)
cucsCapabilityUpdaterFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmStageRn.setStatus("current")
_CucsCapabilityUpdaterFsmStageDescrData_Type = SnmpAdminString
_CucsCapabilityUpdaterFsmStageDescrData_Object = MibTableColumn
cucsCapabilityUpdaterFsmStageDescrData = _CucsCapabilityUpdaterFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 18, 1, 4),
    _CucsCapabilityUpdaterFsmStageDescrData_Type()
)
cucsCapabilityUpdaterFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmStageDescrData.setStatus("current")
_CucsCapabilityUpdaterFsmStageLastUpdateTime_Type = DateAndTime
_CucsCapabilityUpdaterFsmStageLastUpdateTime_Object = MibTableColumn
cucsCapabilityUpdaterFsmStageLastUpdateTime = _CucsCapabilityUpdaterFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 18, 1, 5),
    _CucsCapabilityUpdaterFsmStageLastUpdateTime_Type()
)
cucsCapabilityUpdaterFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmStageLastUpdateTime.setStatus("current")
_CucsCapabilityUpdaterFsmStageName_Type = CucsCapabilityUpdaterFsmStageName
_CucsCapabilityUpdaterFsmStageName_Object = MibTableColumn
cucsCapabilityUpdaterFsmStageName = _CucsCapabilityUpdaterFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 18, 1, 6),
    _CucsCapabilityUpdaterFsmStageName_Type()
)
cucsCapabilityUpdaterFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmStageName.setStatus("current")
_CucsCapabilityUpdaterFsmStageOrder_Type = Gauge32
_CucsCapabilityUpdaterFsmStageOrder_Object = MibTableColumn
cucsCapabilityUpdaterFsmStageOrder = _CucsCapabilityUpdaterFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 18, 1, 7),
    _CucsCapabilityUpdaterFsmStageOrder_Type()
)
cucsCapabilityUpdaterFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmStageOrder.setStatus("current")
_CucsCapabilityUpdaterFsmStageRetry_Type = Gauge32
_CucsCapabilityUpdaterFsmStageRetry_Object = MibTableColumn
cucsCapabilityUpdaterFsmStageRetry = _CucsCapabilityUpdaterFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 18, 1, 8),
    _CucsCapabilityUpdaterFsmStageRetry_Type()
)
cucsCapabilityUpdaterFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmStageRetry.setStatus("current")
_CucsCapabilityUpdaterFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsCapabilityUpdaterFsmStageStageStatus_Object = MibTableColumn
cucsCapabilityUpdaterFsmStageStageStatus = _CucsCapabilityUpdaterFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 7, 18, 1, 9),
    _CucsCapabilityUpdaterFsmStageStageStatus_Type()
)
cucsCapabilityUpdaterFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCapabilityUpdaterFsmStageStageStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB",
    **{"cucsCapabilityObjects": cucsCapabilityObjects,
       "cucsCapabilityCatalogueTable": cucsCapabilityCatalogueTable,
       "cucsCapabilityCatalogueEntry": cucsCapabilityCatalogueEntry,
       "cucsCapabilityCatalogueInstanceId": cucsCapabilityCatalogueInstanceId,
       "cucsCapabilityCatalogueDn": cucsCapabilityCatalogueDn,
       "cucsCapabilityCatalogueRn": cucsCapabilityCatalogueRn,
       "cucsCapabilityCatalogueFsmDescr": cucsCapabilityCatalogueFsmDescr,
       "cucsCapabilityCatalogueFsmPrev": cucsCapabilityCatalogueFsmPrev,
       "cucsCapabilityCatalogueFsmProgr": cucsCapabilityCatalogueFsmProgr,
       "cucsCapabilityCatalogueFsmRmtInvErrCode": cucsCapabilityCatalogueFsmRmtInvErrCode,
       "cucsCapabilityCatalogueFsmRmtInvErrDescr": cucsCapabilityCatalogueFsmRmtInvErrDescr,
       "cucsCapabilityCatalogueFsmRmtInvRslt": cucsCapabilityCatalogueFsmRmtInvRslt,
       "cucsCapabilityCatalogueFsmStageDescr": cucsCapabilityCatalogueFsmStageDescr,
       "cucsCapabilityCatalogueFsmStamp": cucsCapabilityCatalogueFsmStamp,
       "cucsCapabilityCatalogueFsmStatus": cucsCapabilityCatalogueFsmStatus,
       "cucsCapabilityCatalogueFsmTry": cucsCapabilityCatalogueFsmTry,
       "cucsCapabilityCatalogueVersion": cucsCapabilityCatalogueVersion,
       "cucsCapabilityCatalogueFileParseFailures": cucsCapabilityCatalogueFileParseFailures,
       "cucsCapabilityCatalogueFilesParsed": cucsCapabilityCatalogueFilesParsed,
       "cucsCapabilityCatalogueLoadErrors": cucsCapabilityCatalogueLoadErrors,
       "cucsCapabilityCatalogueLoadWarnings": cucsCapabilityCatalogueLoadWarnings,
       "cucsCapabilityCatalogueProviderLoadFailures": cucsCapabilityCatalogueProviderLoadFailures,
       "cucsCapabilityCatalogueProvidersLoaded": cucsCapabilityCatalogueProvidersLoaded,
       "cucsCapabilityCatalogueFsmTaskTable": cucsCapabilityCatalogueFsmTaskTable,
       "cucsCapabilityCatalogueFsmTaskEntry": cucsCapabilityCatalogueFsmTaskEntry,
       "cucsCapabilityCatalogueFsmTaskInstanceId": cucsCapabilityCatalogueFsmTaskInstanceId,
       "cucsCapabilityCatalogueFsmTaskDn": cucsCapabilityCatalogueFsmTaskDn,
       "cucsCapabilityCatalogueFsmTaskRn": cucsCapabilityCatalogueFsmTaskRn,
       "cucsCapabilityCatalogueFsmTaskCompletion": cucsCapabilityCatalogueFsmTaskCompletion,
       "cucsCapabilityCatalogueFsmTaskFlags": cucsCapabilityCatalogueFsmTaskFlags,
       "cucsCapabilityCatalogueFsmTaskItem": cucsCapabilityCatalogueFsmTaskItem,
       "cucsCapabilityCatalogueFsmTaskSeqId": cucsCapabilityCatalogueFsmTaskSeqId,
       "cucsCapabilityEpTable": cucsCapabilityEpTable,
       "cucsCapabilityEpEntry": cucsCapabilityEpEntry,
       "cucsCapabilityEpInstanceId": cucsCapabilityEpInstanceId,
       "cucsCapabilityEpDn": cucsCapabilityEpDn,
       "cucsCapabilityEpRn": cucsCapabilityEpRn,
       "cucsCapabilityMgmtExtensionTable": cucsCapabilityMgmtExtensionTable,
       "cucsCapabilityMgmtExtensionEntry": cucsCapabilityMgmtExtensionEntry,
       "cucsCapabilityMgmtExtensionInstanceId": cucsCapabilityMgmtExtensionInstanceId,
       "cucsCapabilityMgmtExtensionDn": cucsCapabilityMgmtExtensionDn,
       "cucsCapabilityMgmtExtensionRn": cucsCapabilityMgmtExtensionRn,
       "cucsCapabilityMgmtExtensionFsmDescr": cucsCapabilityMgmtExtensionFsmDescr,
       "cucsCapabilityMgmtExtensionFsmPrev": cucsCapabilityMgmtExtensionFsmPrev,
       "cucsCapabilityMgmtExtensionFsmProgr": cucsCapabilityMgmtExtensionFsmProgr,
       "cucsCapabilityMgmtExtensionFsmRmtInvErrCode": cucsCapabilityMgmtExtensionFsmRmtInvErrCode,
       "cucsCapabilityMgmtExtensionFsmRmtInvErrDescr": cucsCapabilityMgmtExtensionFsmRmtInvErrDescr,
       "cucsCapabilityMgmtExtensionFsmRmtInvRslt": cucsCapabilityMgmtExtensionFsmRmtInvRslt,
       "cucsCapabilityMgmtExtensionFsmStageDescr": cucsCapabilityMgmtExtensionFsmStageDescr,
       "cucsCapabilityMgmtExtensionFsmStamp": cucsCapabilityMgmtExtensionFsmStamp,
       "cucsCapabilityMgmtExtensionFsmStatus": cucsCapabilityMgmtExtensionFsmStatus,
       "cucsCapabilityMgmtExtensionFsmTry": cucsCapabilityMgmtExtensionFsmTry,
       "cucsCapabilityMgmtExtensionFsmTaskTable": cucsCapabilityMgmtExtensionFsmTaskTable,
       "cucsCapabilityMgmtExtensionFsmTaskEntry": cucsCapabilityMgmtExtensionFsmTaskEntry,
       "cucsCapabilityMgmtExtensionFsmTaskInstanceId": cucsCapabilityMgmtExtensionFsmTaskInstanceId,
       "cucsCapabilityMgmtExtensionFsmTaskDn": cucsCapabilityMgmtExtensionFsmTaskDn,
       "cucsCapabilityMgmtExtensionFsmTaskRn": cucsCapabilityMgmtExtensionFsmTaskRn,
       "cucsCapabilityMgmtExtensionFsmTaskCompletion": cucsCapabilityMgmtExtensionFsmTaskCompletion,
       "cucsCapabilityMgmtExtensionFsmTaskFlags": cucsCapabilityMgmtExtensionFsmTaskFlags,
       "cucsCapabilityMgmtExtensionFsmTaskItem": cucsCapabilityMgmtExtensionFsmTaskItem,
       "cucsCapabilityMgmtExtensionFsmTaskSeqId": cucsCapabilityMgmtExtensionFsmTaskSeqId,
       "cucsCapabilityUpdateTable": cucsCapabilityUpdateTable,
       "cucsCapabilityUpdateEntry": cucsCapabilityUpdateEntry,
       "cucsCapabilityUpdateInstanceId": cucsCapabilityUpdateInstanceId,
       "cucsCapabilityUpdateDn": cucsCapabilityUpdateDn,
       "cucsCapabilityUpdateRn": cucsCapabilityUpdateRn,
       "cucsCapabilityUpdateImageName": cucsCapabilityUpdateImageName,
       "cucsCapabilityUpdateUpdateTs": cucsCapabilityUpdateUpdateTs,
       "cucsCapabilityUpdateVersion": cucsCapabilityUpdateVersion,
       "cucsCapabilityUpdaterTable": cucsCapabilityUpdaterTable,
       "cucsCapabilityUpdaterEntry": cucsCapabilityUpdaterEntry,
       "cucsCapabilityUpdaterInstanceId": cucsCapabilityUpdaterInstanceId,
       "cucsCapabilityUpdaterDn": cucsCapabilityUpdaterDn,
       "cucsCapabilityUpdaterRn": cucsCapabilityUpdaterRn,
       "cucsCapabilityUpdaterAdminState": cucsCapabilityUpdaterAdminState,
       "cucsCapabilityUpdaterFileName": cucsCapabilityUpdaterFileName,
       "cucsCapabilityUpdaterFsmDescr": cucsCapabilityUpdaterFsmDescr,
       "cucsCapabilityUpdaterFsmPrev": cucsCapabilityUpdaterFsmPrev,
       "cucsCapabilityUpdaterFsmProgr": cucsCapabilityUpdaterFsmProgr,
       "cucsCapabilityUpdaterFsmRmtInvErrCode": cucsCapabilityUpdaterFsmRmtInvErrCode,
       "cucsCapabilityUpdaterFsmRmtInvErrDescr": cucsCapabilityUpdaterFsmRmtInvErrDescr,
       "cucsCapabilityUpdaterFsmRmtInvRslt": cucsCapabilityUpdaterFsmRmtInvRslt,
       "cucsCapabilityUpdaterFsmStageDescr": cucsCapabilityUpdaterFsmStageDescr,
       "cucsCapabilityUpdaterFsmStamp": cucsCapabilityUpdaterFsmStamp,
       "cucsCapabilityUpdaterFsmStatus": cucsCapabilityUpdaterFsmStatus,
       "cucsCapabilityUpdaterFsmTry": cucsCapabilityUpdaterFsmTry,
       "cucsCapabilityUpdaterImageName": cucsCapabilityUpdaterImageName,
       "cucsCapabilityUpdaterOperState": cucsCapabilityUpdaterOperState,
       "cucsCapabilityUpdaterProtocol": cucsCapabilityUpdaterProtocol,
       "cucsCapabilityUpdaterPwd": cucsCapabilityUpdaterPwd,
       "cucsCapabilityUpdaterRemotePath": cucsCapabilityUpdaterRemotePath,
       "cucsCapabilityUpdaterServer": cucsCapabilityUpdaterServer,
       "cucsCapabilityUpdaterUser": cucsCapabilityUpdaterUser,
       "cucsCapabilityUpdaterVersion": cucsCapabilityUpdaterVersion,
       "cucsCapabilityUpdaterFsmTaskTable": cucsCapabilityUpdaterFsmTaskTable,
       "cucsCapabilityUpdaterFsmTaskEntry": cucsCapabilityUpdaterFsmTaskEntry,
       "cucsCapabilityUpdaterFsmTaskInstanceId": cucsCapabilityUpdaterFsmTaskInstanceId,
       "cucsCapabilityUpdaterFsmTaskDn": cucsCapabilityUpdaterFsmTaskDn,
       "cucsCapabilityUpdaterFsmTaskRn": cucsCapabilityUpdaterFsmTaskRn,
       "cucsCapabilityUpdaterFsmTaskCompletion": cucsCapabilityUpdaterFsmTaskCompletion,
       "cucsCapabilityUpdaterFsmTaskFlags": cucsCapabilityUpdaterFsmTaskFlags,
       "cucsCapabilityUpdaterFsmTaskItem": cucsCapabilityUpdaterFsmTaskItem,
       "cucsCapabilityUpdaterFsmTaskSeqId": cucsCapabilityUpdaterFsmTaskSeqId,
       "cucsCapabilityCatalogueFsmTable": cucsCapabilityCatalogueFsmTable,
       "cucsCapabilityCatalogueFsmEntry": cucsCapabilityCatalogueFsmEntry,
       "cucsCapabilityCatalogueFsmInstanceId": cucsCapabilityCatalogueFsmInstanceId,
       "cucsCapabilityCatalogueFsmDn": cucsCapabilityCatalogueFsmDn,
       "cucsCapabilityCatalogueFsmRn": cucsCapabilityCatalogueFsmRn,
       "cucsCapabilityCatalogueFsmCompletionTime": cucsCapabilityCatalogueFsmCompletionTime,
       "cucsCapabilityCatalogueFsmCurrentFsm": cucsCapabilityCatalogueFsmCurrentFsm,
       "cucsCapabilityCatalogueFsmDescrData": cucsCapabilityCatalogueFsmDescrData,
       "cucsCapabilityCatalogueFsmFsmStatus": cucsCapabilityCatalogueFsmFsmStatus,
       "cucsCapabilityCatalogueFsmProgress": cucsCapabilityCatalogueFsmProgress,
       "cucsCapabilityCatalogueFsmRmtErrCode": cucsCapabilityCatalogueFsmRmtErrCode,
       "cucsCapabilityCatalogueFsmRmtErrDescr": cucsCapabilityCatalogueFsmRmtErrDescr,
       "cucsCapabilityCatalogueFsmRmtRslt": cucsCapabilityCatalogueFsmRmtRslt,
       "cucsCapabilityCatalogueFsmStageTable": cucsCapabilityCatalogueFsmStageTable,
       "cucsCapabilityCatalogueFsmStageEntry": cucsCapabilityCatalogueFsmStageEntry,
       "cucsCapabilityCatalogueFsmStageInstanceId": cucsCapabilityCatalogueFsmStageInstanceId,
       "cucsCapabilityCatalogueFsmStageDn": cucsCapabilityCatalogueFsmStageDn,
       "cucsCapabilityCatalogueFsmStageRn": cucsCapabilityCatalogueFsmStageRn,
       "cucsCapabilityCatalogueFsmStageDescrData": cucsCapabilityCatalogueFsmStageDescrData,
       "cucsCapabilityCatalogueFsmStageLastUpdateTime": cucsCapabilityCatalogueFsmStageLastUpdateTime,
       "cucsCapabilityCatalogueFsmStageName": cucsCapabilityCatalogueFsmStageName,
       "cucsCapabilityCatalogueFsmStageOrder": cucsCapabilityCatalogueFsmStageOrder,
       "cucsCapabilityCatalogueFsmStageRetry": cucsCapabilityCatalogueFsmStageRetry,
       "cucsCapabilityCatalogueFsmStageStageStatus": cucsCapabilityCatalogueFsmStageStageStatus,
       "cucsCapabilityFeatureLimitsTable": cucsCapabilityFeatureLimitsTable,
       "cucsCapabilityFeatureLimitsEntry": cucsCapabilityFeatureLimitsEntry,
       "cucsCapabilityFeatureLimitsInstanceId": cucsCapabilityFeatureLimitsInstanceId,
       "cucsCapabilityFeatureLimitsDn": cucsCapabilityFeatureLimitsDn,
       "cucsCapabilityFeatureLimitsRn": cucsCapabilityFeatureLimitsRn,
       "cucsCapabilityFeatureLimitsDescr": cucsCapabilityFeatureLimitsDescr,
       "cucsCapabilityFeatureLimitsFeatureStatus": cucsCapabilityFeatureLimitsFeatureStatus,
       "cucsCapabilityFeatureLimitsLimit": cucsCapabilityFeatureLimitsLimit,
       "cucsCapabilityFeatureLimitsName": cucsCapabilityFeatureLimitsName,
       "cucsCapabilityFeatureLimitsPlatform": cucsCapabilityFeatureLimitsPlatform,
       "cucsCapabilityMgmtExtensionFsmTable": cucsCapabilityMgmtExtensionFsmTable,
       "cucsCapabilityMgmtExtensionFsmEntry": cucsCapabilityMgmtExtensionFsmEntry,
       "cucsCapabilityMgmtExtensionFsmInstanceId": cucsCapabilityMgmtExtensionFsmInstanceId,
       "cucsCapabilityMgmtExtensionFsmDn": cucsCapabilityMgmtExtensionFsmDn,
       "cucsCapabilityMgmtExtensionFsmRn": cucsCapabilityMgmtExtensionFsmRn,
       "cucsCapabilityMgmtExtensionFsmCompletionTime": cucsCapabilityMgmtExtensionFsmCompletionTime,
       "cucsCapabilityMgmtExtensionFsmCurrentFsm": cucsCapabilityMgmtExtensionFsmCurrentFsm,
       "cucsCapabilityMgmtExtensionFsmDescrData": cucsCapabilityMgmtExtensionFsmDescrData,
       "cucsCapabilityMgmtExtensionFsmFsmStatus": cucsCapabilityMgmtExtensionFsmFsmStatus,
       "cucsCapabilityMgmtExtensionFsmProgress": cucsCapabilityMgmtExtensionFsmProgress,
       "cucsCapabilityMgmtExtensionFsmRmtErrCode": cucsCapabilityMgmtExtensionFsmRmtErrCode,
       "cucsCapabilityMgmtExtensionFsmRmtErrDescr": cucsCapabilityMgmtExtensionFsmRmtErrDescr,
       "cucsCapabilityMgmtExtensionFsmRmtRslt": cucsCapabilityMgmtExtensionFsmRmtRslt,
       "cucsCapabilityMgmtExtensionFsmStageTable": cucsCapabilityMgmtExtensionFsmStageTable,
       "cucsCapabilityMgmtExtensionFsmStageEntry": cucsCapabilityMgmtExtensionFsmStageEntry,
       "cucsCapabilityMgmtExtensionFsmStageInstanceId": cucsCapabilityMgmtExtensionFsmStageInstanceId,
       "cucsCapabilityMgmtExtensionFsmStageDn": cucsCapabilityMgmtExtensionFsmStageDn,
       "cucsCapabilityMgmtExtensionFsmStageRn": cucsCapabilityMgmtExtensionFsmStageRn,
       "cucsCapabilityMgmtExtensionFsmStageDescrData": cucsCapabilityMgmtExtensionFsmStageDescrData,
       "cucsCapabilityMgmtExtensionFsmStageLastUpdateTime": cucsCapabilityMgmtExtensionFsmStageLastUpdateTime,
       "cucsCapabilityMgmtExtensionFsmStageName": cucsCapabilityMgmtExtensionFsmStageName,
       "cucsCapabilityMgmtExtensionFsmStageOrder": cucsCapabilityMgmtExtensionFsmStageOrder,
       "cucsCapabilityMgmtExtensionFsmStageRetry": cucsCapabilityMgmtExtensionFsmStageRetry,
       "cucsCapabilityMgmtExtensionFsmStageStageStatus": cucsCapabilityMgmtExtensionFsmStageStageStatus,
       "cucsCapabilityNetworkLimitsTable": cucsCapabilityNetworkLimitsTable,
       "cucsCapabilityNetworkLimitsEntry": cucsCapabilityNetworkLimitsEntry,
       "cucsCapabilityNetworkLimitsInstanceId": cucsCapabilityNetworkLimitsInstanceId,
       "cucsCapabilityNetworkLimitsDn": cucsCapabilityNetworkLimitsDn,
       "cucsCapabilityNetworkLimitsRn": cucsCapabilityNetworkLimitsRn,
       "cucsCapabilityStorageLimitsTable": cucsCapabilityStorageLimitsTable,
       "cucsCapabilityStorageLimitsEntry": cucsCapabilityStorageLimitsEntry,
       "cucsCapabilityStorageLimitsInstanceId": cucsCapabilityStorageLimitsInstanceId,
       "cucsCapabilityStorageLimitsDn": cucsCapabilityStorageLimitsDn,
       "cucsCapabilityStorageLimitsRn": cucsCapabilityStorageLimitsRn,
       "cucsCapabilitySystemLimitsTable": cucsCapabilitySystemLimitsTable,
       "cucsCapabilitySystemLimitsEntry": cucsCapabilitySystemLimitsEntry,
       "cucsCapabilitySystemLimitsInstanceId": cucsCapabilitySystemLimitsInstanceId,
       "cucsCapabilitySystemLimitsDn": cucsCapabilitySystemLimitsDn,
       "cucsCapabilitySystemLimitsRn": cucsCapabilitySystemLimitsRn,
       "cucsCapabilityUpdaterFsmTable": cucsCapabilityUpdaterFsmTable,
       "cucsCapabilityUpdaterFsmEntry": cucsCapabilityUpdaterFsmEntry,
       "cucsCapabilityUpdaterFsmInstanceId": cucsCapabilityUpdaterFsmInstanceId,
       "cucsCapabilityUpdaterFsmDn": cucsCapabilityUpdaterFsmDn,
       "cucsCapabilityUpdaterFsmRn": cucsCapabilityUpdaterFsmRn,
       "cucsCapabilityUpdaterFsmCompletionTime": cucsCapabilityUpdaterFsmCompletionTime,
       "cucsCapabilityUpdaterFsmCurrentFsm": cucsCapabilityUpdaterFsmCurrentFsm,
       "cucsCapabilityUpdaterFsmDescrData": cucsCapabilityUpdaterFsmDescrData,
       "cucsCapabilityUpdaterFsmFsmStatus": cucsCapabilityUpdaterFsmFsmStatus,
       "cucsCapabilityUpdaterFsmProgress": cucsCapabilityUpdaterFsmProgress,
       "cucsCapabilityUpdaterFsmRmtErrCode": cucsCapabilityUpdaterFsmRmtErrCode,
       "cucsCapabilityUpdaterFsmRmtErrDescr": cucsCapabilityUpdaterFsmRmtErrDescr,
       "cucsCapabilityUpdaterFsmRmtRslt": cucsCapabilityUpdaterFsmRmtRslt,
       "cucsCapabilityUpdaterFsmStageTable": cucsCapabilityUpdaterFsmStageTable,
       "cucsCapabilityUpdaterFsmStageEntry": cucsCapabilityUpdaterFsmStageEntry,
       "cucsCapabilityUpdaterFsmStageInstanceId": cucsCapabilityUpdaterFsmStageInstanceId,
       "cucsCapabilityUpdaterFsmStageDn": cucsCapabilityUpdaterFsmStageDn,
       "cucsCapabilityUpdaterFsmStageRn": cucsCapabilityUpdaterFsmStageRn,
       "cucsCapabilityUpdaterFsmStageDescrData": cucsCapabilityUpdaterFsmStageDescrData,
       "cucsCapabilityUpdaterFsmStageLastUpdateTime": cucsCapabilityUpdaterFsmStageLastUpdateTime,
       "cucsCapabilityUpdaterFsmStageName": cucsCapabilityUpdaterFsmStageName,
       "cucsCapabilityUpdaterFsmStageOrder": cucsCapabilityUpdaterFsmStageOrder,
       "cucsCapabilityUpdaterFsmStageRetry": cucsCapabilityUpdaterFsmStageRetry,
       "cucsCapabilityUpdaterFsmStageStageStatus": cucsCapabilityUpdaterFsmStageStageStatus}
)
