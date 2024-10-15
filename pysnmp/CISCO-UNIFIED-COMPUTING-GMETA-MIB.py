# SNMP MIB module (CISCO-UNIFIED-COMPUTING-GMETA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-GMETA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:37 2024
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
 CucsExtpolConnType,
 CucsFsmCompletion,
 CucsFsmFsmStageStatus,
 CucsGmetaCategory,
 CucsGmetaHolderFsmCurrentFsm,
 CucsGmetaHolderFsmStageName,
 CucsGmetaHolderFsmTaskFlags,
 CucsGmetaHolderFsmTaskItem,
 CucsGmetaInventoryStatus,
 CucsGmetaPollInterval,
 CucsGmetaVersion,
 CucsMoMoClassId) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsExtpolConnType",
    "CucsFsmCompletion",
    "CucsFsmFsmStageStatus",
    "CucsGmetaCategory",
    "CucsGmetaHolderFsmCurrentFsm",
    "CucsGmetaHolderFsmStageName",
    "CucsGmetaHolderFsmTaskFlags",
    "CucsGmetaHolderFsmTaskItem",
    "CucsGmetaInventoryStatus",
    "CucsGmetaPollInterval",
    "CucsGmetaVersion",
    "CucsMoMoClassId")

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

cucsGmetaObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsGmetaClassTable_Object = MibTable
cucsGmetaClassTable = _CucsGmetaClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1)
)
if mibBuilder.loadTexts:
    cucsGmetaClassTable.setStatus("current")
_CucsGmetaClassEntry_Object = MibTableRow
cucsGmetaClassEntry = _CucsGmetaClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1)
)
cucsGmetaClassEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaClassInstanceId"),
)
if mibBuilder.loadTexts:
    cucsGmetaClassEntry.setStatus("current")
_CucsGmetaClassInstanceId_Type = CucsManagedObjectId
_CucsGmetaClassInstanceId_Object = MibTableColumn
cucsGmetaClassInstanceId = _CucsGmetaClassInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1, 1),
    _CucsGmetaClassInstanceId_Type()
)
cucsGmetaClassInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsGmetaClassInstanceId.setStatus("current")
_CucsGmetaClassDn_Type = CucsManagedObjectDn
_CucsGmetaClassDn_Object = MibTableColumn
cucsGmetaClassDn = _CucsGmetaClassDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1, 2),
    _CucsGmetaClassDn_Type()
)
cucsGmetaClassDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaClassDn.setStatus("current")
_CucsGmetaClassRn_Type = SnmpAdminString
_CucsGmetaClassRn_Object = MibTableColumn
cucsGmetaClassRn = _CucsGmetaClassRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1, 3),
    _CucsGmetaClassRn_Type()
)
cucsGmetaClassRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaClassRn.setStatus("current")
_CucsGmetaClassAdminPropMask_Type = Unsigned64
_CucsGmetaClassAdminPropMask_Object = MibTableColumn
cucsGmetaClassAdminPropMask = _CucsGmetaClassAdminPropMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1, 4),
    _CucsGmetaClassAdminPropMask_Type()
)
cucsGmetaClassAdminPropMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaClassAdminPropMask.setStatus("current")
_CucsGmetaClassEpClassId_Type = CucsMoMoClassId
_CucsGmetaClassEpClassId_Object = MibTableColumn
cucsGmetaClassEpClassId = _CucsGmetaClassEpClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1, 5),
    _CucsGmetaClassEpClassId_Type()
)
cucsGmetaClassEpClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaClassEpClassId.setStatus("current")
_CucsGmetaClassId_Type = Gauge32
_CucsGmetaClassId_Object = MibTableColumn
cucsGmetaClassId = _CucsGmetaClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1, 6),
    _CucsGmetaClassId_Type()
)
cucsGmetaClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaClassId.setStatus("current")
_CucsGmetaClassName_Type = SnmpAdminString
_CucsGmetaClassName_Object = MibTableColumn
cucsGmetaClassName = _CucsGmetaClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1, 7),
    _CucsGmetaClassName_Type()
)
cucsGmetaClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaClassName.setStatus("current")
_CucsGmetaClassOperPropMask_Type = Unsigned64
_CucsGmetaClassOperPropMask_Object = MibTableColumn
cucsGmetaClassOperPropMask = _CucsGmetaClassOperPropMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 1, 1, 8),
    _CucsGmetaClassOperPropMask_Type()
)
cucsGmetaClassOperPropMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaClassOperPropMask.setStatus("current")
_CucsGmetaEpTable_Object = MibTable
cucsGmetaEpTable = _CucsGmetaEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 2)
)
if mibBuilder.loadTexts:
    cucsGmetaEpTable.setStatus("current")
_CucsGmetaEpEntry_Object = MibTableRow
cucsGmetaEpEntry = _CucsGmetaEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 2, 1)
)
cucsGmetaEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsGmetaEpEntry.setStatus("current")
_CucsGmetaEpInstanceId_Type = CucsManagedObjectId
_CucsGmetaEpInstanceId_Object = MibTableColumn
cucsGmetaEpInstanceId = _CucsGmetaEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 2, 1, 1),
    _CucsGmetaEpInstanceId_Type()
)
cucsGmetaEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsGmetaEpInstanceId.setStatus("current")
_CucsGmetaEpDn_Type = CucsManagedObjectDn
_CucsGmetaEpDn_Object = MibTableColumn
cucsGmetaEpDn = _CucsGmetaEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 2, 1, 2),
    _CucsGmetaEpDn_Type()
)
cucsGmetaEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaEpDn.setStatus("current")
_CucsGmetaEpRn_Type = SnmpAdminString
_CucsGmetaEpRn_Object = MibTableColumn
cucsGmetaEpRn = _CucsGmetaEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 2, 1, 3),
    _CucsGmetaEpRn_Type()
)
cucsGmetaEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaEpRn.setStatus("current")
_CucsGmetaHolderTable_Object = MibTable
cucsGmetaHolderTable = _CucsGmetaHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3)
)
if mibBuilder.loadTexts:
    cucsGmetaHolderTable.setStatus("current")
_CucsGmetaHolderEntry_Object = MibTableRow
cucsGmetaHolderEntry = _CucsGmetaHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1)
)
cucsGmetaHolderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsGmetaHolderEntry.setStatus("current")
_CucsGmetaHolderInstanceId_Type = CucsManagedObjectId
_CucsGmetaHolderInstanceId_Object = MibTableColumn
cucsGmetaHolderInstanceId = _CucsGmetaHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 1),
    _CucsGmetaHolderInstanceId_Type()
)
cucsGmetaHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsGmetaHolderInstanceId.setStatus("current")
_CucsGmetaHolderDn_Type = CucsManagedObjectDn
_CucsGmetaHolderDn_Object = MibTableColumn
cucsGmetaHolderDn = _CucsGmetaHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 2),
    _CucsGmetaHolderDn_Type()
)
cucsGmetaHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderDn.setStatus("current")
_CucsGmetaHolderRn_Type = SnmpAdminString
_CucsGmetaHolderRn_Object = MibTableColumn
cucsGmetaHolderRn = _CucsGmetaHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 3),
    _CucsGmetaHolderRn_Type()
)
cucsGmetaHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderRn.setStatus("current")
_CucsGmetaHolderCategory_Type = CucsGmetaCategory
_CucsGmetaHolderCategory_Object = MibTableColumn
cucsGmetaHolderCategory = _CucsGmetaHolderCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 4),
    _CucsGmetaHolderCategory_Type()
)
cucsGmetaHolderCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderCategory.setStatus("current")
_CucsGmetaHolderFsmDescr_Type = SnmpAdminString
_CucsGmetaHolderFsmDescr_Object = MibTableColumn
cucsGmetaHolderFsmDescr = _CucsGmetaHolderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 5),
    _CucsGmetaHolderFsmDescr_Type()
)
cucsGmetaHolderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmDescr.setStatus("current")
_CucsGmetaHolderFsmFlags_Type = SnmpAdminString
_CucsGmetaHolderFsmFlags_Object = MibTableColumn
cucsGmetaHolderFsmFlags = _CucsGmetaHolderFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 6),
    _CucsGmetaHolderFsmFlags_Type()
)
cucsGmetaHolderFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmFlags.setStatus("current")
_CucsGmetaHolderFsmPrev_Type = SnmpAdminString
_CucsGmetaHolderFsmPrev_Object = MibTableColumn
cucsGmetaHolderFsmPrev = _CucsGmetaHolderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 7),
    _CucsGmetaHolderFsmPrev_Type()
)
cucsGmetaHolderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmPrev.setStatus("current")
_CucsGmetaHolderFsmProgr_Type = Gauge32
_CucsGmetaHolderFsmProgr_Object = MibTableColumn
cucsGmetaHolderFsmProgr = _CucsGmetaHolderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 8),
    _CucsGmetaHolderFsmProgr_Type()
)
cucsGmetaHolderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmProgr.setStatus("current")
_CucsGmetaHolderFsmRmtInvErrCode_Type = Gauge32
_CucsGmetaHolderFsmRmtInvErrCode_Object = MibTableColumn
cucsGmetaHolderFsmRmtInvErrCode = _CucsGmetaHolderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 9),
    _CucsGmetaHolderFsmRmtInvErrCode_Type()
)
cucsGmetaHolderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmRmtInvErrCode.setStatus("current")
_CucsGmetaHolderFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsGmetaHolderFsmRmtInvErrDescr_Object = MibTableColumn
cucsGmetaHolderFsmRmtInvErrDescr = _CucsGmetaHolderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 10),
    _CucsGmetaHolderFsmRmtInvErrDescr_Type()
)
cucsGmetaHolderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmRmtInvErrDescr.setStatus("current")
_CucsGmetaHolderFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsGmetaHolderFsmRmtInvRslt_Object = MibTableColumn
cucsGmetaHolderFsmRmtInvRslt = _CucsGmetaHolderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 11),
    _CucsGmetaHolderFsmRmtInvRslt_Type()
)
cucsGmetaHolderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmRmtInvRslt.setStatus("current")
_CucsGmetaHolderFsmStageDescr_Type = SnmpAdminString
_CucsGmetaHolderFsmStageDescr_Object = MibTableColumn
cucsGmetaHolderFsmStageDescr = _CucsGmetaHolderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 12),
    _CucsGmetaHolderFsmStageDescr_Type()
)
cucsGmetaHolderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmStageDescr.setStatus("current")
_CucsGmetaHolderFsmStamp_Type = DateAndTime
_CucsGmetaHolderFsmStamp_Object = MibTableColumn
cucsGmetaHolderFsmStamp = _CucsGmetaHolderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 13),
    _CucsGmetaHolderFsmStamp_Type()
)
cucsGmetaHolderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmStamp.setStatus("current")
_CucsGmetaHolderFsmStatus_Type = SnmpAdminString
_CucsGmetaHolderFsmStatus_Object = MibTableColumn
cucsGmetaHolderFsmStatus = _CucsGmetaHolderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 14),
    _CucsGmetaHolderFsmStatus_Type()
)
cucsGmetaHolderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmStatus.setStatus("current")
_CucsGmetaHolderFsmTry_Type = Gauge32
_CucsGmetaHolderFsmTry_Object = MibTableColumn
cucsGmetaHolderFsmTry = _CucsGmetaHolderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 15),
    _CucsGmetaHolderFsmTry_Type()
)
cucsGmetaHolderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmTry.setStatus("current")
_CucsGmetaHolderInventoryStatus_Type = CucsGmetaInventoryStatus
_CucsGmetaHolderInventoryStatus_Object = MibTableColumn
cucsGmetaHolderInventoryStatus = _CucsGmetaHolderInventoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 16),
    _CucsGmetaHolderInventoryStatus_Type()
)
cucsGmetaHolderInventoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderInventoryStatus.setStatus("current")
_CucsGmetaHolderPollInterval_Type = CucsGmetaPollInterval
_CucsGmetaHolderPollInterval_Object = MibTableColumn
cucsGmetaHolderPollInterval = _CucsGmetaHolderPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 17),
    _CucsGmetaHolderPollInterval_Type()
)
cucsGmetaHolderPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderPollInterval.setStatus("current")
_CucsGmetaHolderProvider_Type = CucsExtpolConnType
_CucsGmetaHolderProvider_Object = MibTableColumn
cucsGmetaHolderProvider = _CucsGmetaHolderProvider_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 18),
    _CucsGmetaHolderProvider_Type()
)
cucsGmetaHolderProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderProvider.setStatus("current")
_CucsGmetaHolderInventoryVersion_Type = CucsGmetaVersion
_CucsGmetaHolderInventoryVersion_Object = MibTableColumn
cucsGmetaHolderInventoryVersion = _CucsGmetaHolderInventoryVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 19),
    _CucsGmetaHolderInventoryVersion_Type()
)
cucsGmetaHolderInventoryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderInventoryVersion.setStatus("current")
_CucsGmetaHolderGenNum_Type = Gauge32
_CucsGmetaHolderGenNum_Object = MibTableColumn
cucsGmetaHolderGenNum = _CucsGmetaHolderGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 3, 1, 20),
    _CucsGmetaHolderGenNum_Type()
)
cucsGmetaHolderGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderGenNum.setStatus("current")
_CucsGmetaHolderFsmTable_Object = MibTable
cucsGmetaHolderFsmTable = _CucsGmetaHolderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4)
)
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmTable.setStatus("current")
_CucsGmetaHolderFsmEntry_Object = MibTableRow
cucsGmetaHolderFsmEntry = _CucsGmetaHolderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1)
)
cucsGmetaHolderFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaHolderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmEntry.setStatus("current")
_CucsGmetaHolderFsmInstanceId_Type = CucsManagedObjectId
_CucsGmetaHolderFsmInstanceId_Object = MibTableColumn
cucsGmetaHolderFsmInstanceId = _CucsGmetaHolderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 1),
    _CucsGmetaHolderFsmInstanceId_Type()
)
cucsGmetaHolderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmInstanceId.setStatus("current")
_CucsGmetaHolderFsmDn_Type = CucsManagedObjectDn
_CucsGmetaHolderFsmDn_Object = MibTableColumn
cucsGmetaHolderFsmDn = _CucsGmetaHolderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 2),
    _CucsGmetaHolderFsmDn_Type()
)
cucsGmetaHolderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmDn.setStatus("current")
_CucsGmetaHolderFsmRn_Type = SnmpAdminString
_CucsGmetaHolderFsmRn_Object = MibTableColumn
cucsGmetaHolderFsmRn = _CucsGmetaHolderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 3),
    _CucsGmetaHolderFsmRn_Type()
)
cucsGmetaHolderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmRn.setStatus("current")
_CucsGmetaHolderFsmCompletionTime_Type = DateAndTime
_CucsGmetaHolderFsmCompletionTime_Object = MibTableColumn
cucsGmetaHolderFsmCompletionTime = _CucsGmetaHolderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 4),
    _CucsGmetaHolderFsmCompletionTime_Type()
)
cucsGmetaHolderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmCompletionTime.setStatus("current")
_CucsGmetaHolderFsmCurrentFsm_Type = CucsGmetaHolderFsmCurrentFsm
_CucsGmetaHolderFsmCurrentFsm_Object = MibTableColumn
cucsGmetaHolderFsmCurrentFsm = _CucsGmetaHolderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 5),
    _CucsGmetaHolderFsmCurrentFsm_Type()
)
cucsGmetaHolderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmCurrentFsm.setStatus("current")
_CucsGmetaHolderFsmDescrData_Type = SnmpAdminString
_CucsGmetaHolderFsmDescrData_Object = MibTableColumn
cucsGmetaHolderFsmDescrData = _CucsGmetaHolderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 6),
    _CucsGmetaHolderFsmDescrData_Type()
)
cucsGmetaHolderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmDescrData.setStatus("current")
_CucsGmetaHolderFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsGmetaHolderFsmFsmStatus_Object = MibTableColumn
cucsGmetaHolderFsmFsmStatus = _CucsGmetaHolderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 7),
    _CucsGmetaHolderFsmFsmStatus_Type()
)
cucsGmetaHolderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmFsmStatus.setStatus("current")
_CucsGmetaHolderFsmProgress_Type = Gauge32
_CucsGmetaHolderFsmProgress_Object = MibTableColumn
cucsGmetaHolderFsmProgress = _CucsGmetaHolderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 8),
    _CucsGmetaHolderFsmProgress_Type()
)
cucsGmetaHolderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmProgress.setStatus("current")
_CucsGmetaHolderFsmRmtErrCode_Type = Gauge32
_CucsGmetaHolderFsmRmtErrCode_Object = MibTableColumn
cucsGmetaHolderFsmRmtErrCode = _CucsGmetaHolderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 9),
    _CucsGmetaHolderFsmRmtErrCode_Type()
)
cucsGmetaHolderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmRmtErrCode.setStatus("current")
_CucsGmetaHolderFsmRmtErrDescr_Type = SnmpAdminString
_CucsGmetaHolderFsmRmtErrDescr_Object = MibTableColumn
cucsGmetaHolderFsmRmtErrDescr = _CucsGmetaHolderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 10),
    _CucsGmetaHolderFsmRmtErrDescr_Type()
)
cucsGmetaHolderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmRmtErrDescr.setStatus("current")
_CucsGmetaHolderFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsGmetaHolderFsmRmtRslt_Object = MibTableColumn
cucsGmetaHolderFsmRmtRslt = _CucsGmetaHolderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 4, 1, 11),
    _CucsGmetaHolderFsmRmtRslt_Type()
)
cucsGmetaHolderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmRmtRslt.setStatus("current")
_CucsGmetaHolderFsmStageTable_Object = MibTable
cucsGmetaHolderFsmStageTable = _CucsGmetaHolderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5)
)
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmStageTable.setStatus("current")
_CucsGmetaHolderFsmStageEntry_Object = MibTableRow
cucsGmetaHolderFsmStageEntry = _CucsGmetaHolderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1)
)
cucsGmetaHolderFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaHolderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmStageEntry.setStatus("current")
_CucsGmetaHolderFsmStageInstanceId_Type = CucsManagedObjectId
_CucsGmetaHolderFsmStageInstanceId_Object = MibTableColumn
cucsGmetaHolderFsmStageInstanceId = _CucsGmetaHolderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 1),
    _CucsGmetaHolderFsmStageInstanceId_Type()
)
cucsGmetaHolderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmStageInstanceId.setStatus("current")
_CucsGmetaHolderFsmStageDn_Type = CucsManagedObjectDn
_CucsGmetaHolderFsmStageDn_Object = MibTableColumn
cucsGmetaHolderFsmStageDn = _CucsGmetaHolderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 2),
    _CucsGmetaHolderFsmStageDn_Type()
)
cucsGmetaHolderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmStageDn.setStatus("current")
_CucsGmetaHolderFsmStageRn_Type = SnmpAdminString
_CucsGmetaHolderFsmStageRn_Object = MibTableColumn
cucsGmetaHolderFsmStageRn = _CucsGmetaHolderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 3),
    _CucsGmetaHolderFsmStageRn_Type()
)
cucsGmetaHolderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmStageRn.setStatus("current")
_CucsGmetaHolderFsmStageDescrData_Type = SnmpAdminString
_CucsGmetaHolderFsmStageDescrData_Object = MibTableColumn
cucsGmetaHolderFsmStageDescrData = _CucsGmetaHolderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 4),
    _CucsGmetaHolderFsmStageDescrData_Type()
)
cucsGmetaHolderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmStageDescrData.setStatus("current")
_CucsGmetaHolderFsmStageLastUpdateTime_Type = DateAndTime
_CucsGmetaHolderFsmStageLastUpdateTime_Object = MibTableColumn
cucsGmetaHolderFsmStageLastUpdateTime = _CucsGmetaHolderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 5),
    _CucsGmetaHolderFsmStageLastUpdateTime_Type()
)
cucsGmetaHolderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmStageLastUpdateTime.setStatus("current")
_CucsGmetaHolderFsmStageName_Type = CucsGmetaHolderFsmStageName
_CucsGmetaHolderFsmStageName_Object = MibTableColumn
cucsGmetaHolderFsmStageName = _CucsGmetaHolderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 6),
    _CucsGmetaHolderFsmStageName_Type()
)
cucsGmetaHolderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmStageName.setStatus("current")
_CucsGmetaHolderFsmStageOrder_Type = Gauge32
_CucsGmetaHolderFsmStageOrder_Object = MibTableColumn
cucsGmetaHolderFsmStageOrder = _CucsGmetaHolderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 7),
    _CucsGmetaHolderFsmStageOrder_Type()
)
cucsGmetaHolderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmStageOrder.setStatus("current")
_CucsGmetaHolderFsmStageRetry_Type = Gauge32
_CucsGmetaHolderFsmStageRetry_Object = MibTableColumn
cucsGmetaHolderFsmStageRetry = _CucsGmetaHolderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 8),
    _CucsGmetaHolderFsmStageRetry_Type()
)
cucsGmetaHolderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmStageRetry.setStatus("current")
_CucsGmetaHolderFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsGmetaHolderFsmStageStageStatus_Object = MibTableColumn
cucsGmetaHolderFsmStageStageStatus = _CucsGmetaHolderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 5, 1, 9),
    _CucsGmetaHolderFsmStageStageStatus_Type()
)
cucsGmetaHolderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmStageStageStatus.setStatus("current")
_CucsGmetaHolderFsmTaskTable_Object = MibTable
cucsGmetaHolderFsmTaskTable = _CucsGmetaHolderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6)
)
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmTaskTable.setStatus("current")
_CucsGmetaHolderFsmTaskEntry_Object = MibTableRow
cucsGmetaHolderFsmTaskEntry = _CucsGmetaHolderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6, 1)
)
cucsGmetaHolderFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaHolderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmTaskEntry.setStatus("current")
_CucsGmetaHolderFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsGmetaHolderFsmTaskInstanceId_Object = MibTableColumn
cucsGmetaHolderFsmTaskInstanceId = _CucsGmetaHolderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6, 1, 1),
    _CucsGmetaHolderFsmTaskInstanceId_Type()
)
cucsGmetaHolderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmTaskInstanceId.setStatus("current")
_CucsGmetaHolderFsmTaskDn_Type = CucsManagedObjectDn
_CucsGmetaHolderFsmTaskDn_Object = MibTableColumn
cucsGmetaHolderFsmTaskDn = _CucsGmetaHolderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6, 1, 2),
    _CucsGmetaHolderFsmTaskDn_Type()
)
cucsGmetaHolderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmTaskDn.setStatus("current")
_CucsGmetaHolderFsmTaskRn_Type = SnmpAdminString
_CucsGmetaHolderFsmTaskRn_Object = MibTableColumn
cucsGmetaHolderFsmTaskRn = _CucsGmetaHolderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6, 1, 3),
    _CucsGmetaHolderFsmTaskRn_Type()
)
cucsGmetaHolderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmTaskRn.setStatus("current")
_CucsGmetaHolderFsmTaskCompletion_Type = CucsFsmCompletion
_CucsGmetaHolderFsmTaskCompletion_Object = MibTableColumn
cucsGmetaHolderFsmTaskCompletion = _CucsGmetaHolderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6, 1, 4),
    _CucsGmetaHolderFsmTaskCompletion_Type()
)
cucsGmetaHolderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmTaskCompletion.setStatus("current")
_CucsGmetaHolderFsmTaskFlags_Type = CucsGmetaHolderFsmTaskFlags
_CucsGmetaHolderFsmTaskFlags_Object = MibTableColumn
cucsGmetaHolderFsmTaskFlags = _CucsGmetaHolderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6, 1, 5),
    _CucsGmetaHolderFsmTaskFlags_Type()
)
cucsGmetaHolderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmTaskFlags.setStatus("current")
_CucsGmetaHolderFsmTaskItem_Type = CucsGmetaHolderFsmTaskItem
_CucsGmetaHolderFsmTaskItem_Object = MibTableColumn
cucsGmetaHolderFsmTaskItem = _CucsGmetaHolderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6, 1, 6),
    _CucsGmetaHolderFsmTaskItem_Type()
)
cucsGmetaHolderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmTaskItem.setStatus("current")
_CucsGmetaHolderFsmTaskSeqId_Type = Gauge32
_CucsGmetaHolderFsmTaskSeqId_Object = MibTableColumn
cucsGmetaHolderFsmTaskSeqId = _CucsGmetaHolderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 6, 1, 7),
    _CucsGmetaHolderFsmTaskSeqId_Type()
)
cucsGmetaHolderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaHolderFsmTaskSeqId.setStatus("current")
_CucsGmetaPolicyMapElementTable_Object = MibTable
cucsGmetaPolicyMapElementTable = _CucsGmetaPolicyMapElementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 7)
)
if mibBuilder.loadTexts:
    cucsGmetaPolicyMapElementTable.setStatus("current")
_CucsGmetaPolicyMapElementEntry_Object = MibTableRow
cucsGmetaPolicyMapElementEntry = _CucsGmetaPolicyMapElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 7, 1)
)
cucsGmetaPolicyMapElementEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaPolicyMapElementInstanceId"),
)
if mibBuilder.loadTexts:
    cucsGmetaPolicyMapElementEntry.setStatus("current")
_CucsGmetaPolicyMapElementInstanceId_Type = CucsManagedObjectId
_CucsGmetaPolicyMapElementInstanceId_Object = MibTableColumn
cucsGmetaPolicyMapElementInstanceId = _CucsGmetaPolicyMapElementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 7, 1, 1),
    _CucsGmetaPolicyMapElementInstanceId_Type()
)
cucsGmetaPolicyMapElementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsGmetaPolicyMapElementInstanceId.setStatus("current")
_CucsGmetaPolicyMapElementDn_Type = CucsManagedObjectDn
_CucsGmetaPolicyMapElementDn_Object = MibTableColumn
cucsGmetaPolicyMapElementDn = _CucsGmetaPolicyMapElementDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 7, 1, 2),
    _CucsGmetaPolicyMapElementDn_Type()
)
cucsGmetaPolicyMapElementDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaPolicyMapElementDn.setStatus("current")
_CucsGmetaPolicyMapElementRn_Type = SnmpAdminString
_CucsGmetaPolicyMapElementRn_Object = MibTableColumn
cucsGmetaPolicyMapElementRn = _CucsGmetaPolicyMapElementRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 7, 1, 3),
    _CucsGmetaPolicyMapElementRn_Type()
)
cucsGmetaPolicyMapElementRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaPolicyMapElementRn.setStatus("current")
_CucsGmetaPolicyMapElementName_Type = SnmpAdminString
_CucsGmetaPolicyMapElementName_Object = MibTableColumn
cucsGmetaPolicyMapElementName = _CucsGmetaPolicyMapElementName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 7, 1, 4),
    _CucsGmetaPolicyMapElementName_Type()
)
cucsGmetaPolicyMapElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaPolicyMapElementName.setStatus("current")
_CucsGmetaPolicyMapHolderTable_Object = MibTable
cucsGmetaPolicyMapHolderTable = _CucsGmetaPolicyMapHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 8)
)
if mibBuilder.loadTexts:
    cucsGmetaPolicyMapHolderTable.setStatus("current")
_CucsGmetaPolicyMapHolderEntry_Object = MibTableRow
cucsGmetaPolicyMapHolderEntry = _CucsGmetaPolicyMapHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 8, 1)
)
cucsGmetaPolicyMapHolderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaPolicyMapHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsGmetaPolicyMapHolderEntry.setStatus("current")
_CucsGmetaPolicyMapHolderInstanceId_Type = CucsManagedObjectId
_CucsGmetaPolicyMapHolderInstanceId_Object = MibTableColumn
cucsGmetaPolicyMapHolderInstanceId = _CucsGmetaPolicyMapHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 8, 1, 1),
    _CucsGmetaPolicyMapHolderInstanceId_Type()
)
cucsGmetaPolicyMapHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsGmetaPolicyMapHolderInstanceId.setStatus("current")
_CucsGmetaPolicyMapHolderDn_Type = CucsManagedObjectDn
_CucsGmetaPolicyMapHolderDn_Object = MibTableColumn
cucsGmetaPolicyMapHolderDn = _CucsGmetaPolicyMapHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 8, 1, 2),
    _CucsGmetaPolicyMapHolderDn_Type()
)
cucsGmetaPolicyMapHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaPolicyMapHolderDn.setStatus("current")
_CucsGmetaPolicyMapHolderRn_Type = SnmpAdminString
_CucsGmetaPolicyMapHolderRn_Object = MibTableColumn
cucsGmetaPolicyMapHolderRn = _CucsGmetaPolicyMapHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 8, 1, 3),
    _CucsGmetaPolicyMapHolderRn_Type()
)
cucsGmetaPolicyMapHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaPolicyMapHolderRn.setStatus("current")
_CucsGmetaPropTable_Object = MibTable
cucsGmetaPropTable = _CucsGmetaPropTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 9)
)
if mibBuilder.loadTexts:
    cucsGmetaPropTable.setStatus("current")
_CucsGmetaPropEntry_Object = MibTableRow
cucsGmetaPropEntry = _CucsGmetaPropEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 9, 1)
)
cucsGmetaPropEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-GMETA-MIB", "cucsGmetaPropInstanceId"),
)
if mibBuilder.loadTexts:
    cucsGmetaPropEntry.setStatus("current")
_CucsGmetaPropInstanceId_Type = CucsManagedObjectId
_CucsGmetaPropInstanceId_Object = MibTableColumn
cucsGmetaPropInstanceId = _CucsGmetaPropInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 9, 1, 1),
    _CucsGmetaPropInstanceId_Type()
)
cucsGmetaPropInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsGmetaPropInstanceId.setStatus("current")
_CucsGmetaPropDn_Type = CucsManagedObjectDn
_CucsGmetaPropDn_Object = MibTableColumn
cucsGmetaPropDn = _CucsGmetaPropDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 9, 1, 2),
    _CucsGmetaPropDn_Type()
)
cucsGmetaPropDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaPropDn.setStatus("current")
_CucsGmetaPropRn_Type = SnmpAdminString
_CucsGmetaPropRn_Object = MibTableColumn
cucsGmetaPropRn = _CucsGmetaPropRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 9, 1, 3),
    _CucsGmetaPropRn_Type()
)
cucsGmetaPropRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaPropRn.setStatus("current")
_CucsGmetaPropName_Type = SnmpAdminString
_CucsGmetaPropName_Object = MibTableColumn
cucsGmetaPropName = _CucsGmetaPropName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 9, 1, 4),
    _CucsGmetaPropName_Type()
)
cucsGmetaPropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaPropName.setStatus("current")
_CucsGmetaPropOrder_Type = Gauge32
_CucsGmetaPropOrder_Object = MibTableColumn
cucsGmetaPropOrder = _CucsGmetaPropOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 9, 1, 5),
    _CucsGmetaPropOrder_Type()
)
cucsGmetaPropOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaPropOrder.setStatus("current")
_CucsGmetaPropPropId_Type = SnmpAdminString
_CucsGmetaPropPropId_Object = MibTableColumn
cucsGmetaPropPropId = _CucsGmetaPropPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 72, 9, 1, 6),
    _CucsGmetaPropPropId_Type()
)
cucsGmetaPropPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGmetaPropPropId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-GMETA-MIB",
    **{"cucsGmetaObjects": cucsGmetaObjects,
       "cucsGmetaClassTable": cucsGmetaClassTable,
       "cucsGmetaClassEntry": cucsGmetaClassEntry,
       "cucsGmetaClassInstanceId": cucsGmetaClassInstanceId,
       "cucsGmetaClassDn": cucsGmetaClassDn,
       "cucsGmetaClassRn": cucsGmetaClassRn,
       "cucsGmetaClassAdminPropMask": cucsGmetaClassAdminPropMask,
       "cucsGmetaClassEpClassId": cucsGmetaClassEpClassId,
       "cucsGmetaClassId": cucsGmetaClassId,
       "cucsGmetaClassName": cucsGmetaClassName,
       "cucsGmetaClassOperPropMask": cucsGmetaClassOperPropMask,
       "cucsGmetaEpTable": cucsGmetaEpTable,
       "cucsGmetaEpEntry": cucsGmetaEpEntry,
       "cucsGmetaEpInstanceId": cucsGmetaEpInstanceId,
       "cucsGmetaEpDn": cucsGmetaEpDn,
       "cucsGmetaEpRn": cucsGmetaEpRn,
       "cucsGmetaHolderTable": cucsGmetaHolderTable,
       "cucsGmetaHolderEntry": cucsGmetaHolderEntry,
       "cucsGmetaHolderInstanceId": cucsGmetaHolderInstanceId,
       "cucsGmetaHolderDn": cucsGmetaHolderDn,
       "cucsGmetaHolderRn": cucsGmetaHolderRn,
       "cucsGmetaHolderCategory": cucsGmetaHolderCategory,
       "cucsGmetaHolderFsmDescr": cucsGmetaHolderFsmDescr,
       "cucsGmetaHolderFsmFlags": cucsGmetaHolderFsmFlags,
       "cucsGmetaHolderFsmPrev": cucsGmetaHolderFsmPrev,
       "cucsGmetaHolderFsmProgr": cucsGmetaHolderFsmProgr,
       "cucsGmetaHolderFsmRmtInvErrCode": cucsGmetaHolderFsmRmtInvErrCode,
       "cucsGmetaHolderFsmRmtInvErrDescr": cucsGmetaHolderFsmRmtInvErrDescr,
       "cucsGmetaHolderFsmRmtInvRslt": cucsGmetaHolderFsmRmtInvRslt,
       "cucsGmetaHolderFsmStageDescr": cucsGmetaHolderFsmStageDescr,
       "cucsGmetaHolderFsmStamp": cucsGmetaHolderFsmStamp,
       "cucsGmetaHolderFsmStatus": cucsGmetaHolderFsmStatus,
       "cucsGmetaHolderFsmTry": cucsGmetaHolderFsmTry,
       "cucsGmetaHolderInventoryStatus": cucsGmetaHolderInventoryStatus,
       "cucsGmetaHolderPollInterval": cucsGmetaHolderPollInterval,
       "cucsGmetaHolderProvider": cucsGmetaHolderProvider,
       "cucsGmetaHolderInventoryVersion": cucsGmetaHolderInventoryVersion,
       "cucsGmetaHolderGenNum": cucsGmetaHolderGenNum,
       "cucsGmetaHolderFsmTable": cucsGmetaHolderFsmTable,
       "cucsGmetaHolderFsmEntry": cucsGmetaHolderFsmEntry,
       "cucsGmetaHolderFsmInstanceId": cucsGmetaHolderFsmInstanceId,
       "cucsGmetaHolderFsmDn": cucsGmetaHolderFsmDn,
       "cucsGmetaHolderFsmRn": cucsGmetaHolderFsmRn,
       "cucsGmetaHolderFsmCompletionTime": cucsGmetaHolderFsmCompletionTime,
       "cucsGmetaHolderFsmCurrentFsm": cucsGmetaHolderFsmCurrentFsm,
       "cucsGmetaHolderFsmDescrData": cucsGmetaHolderFsmDescrData,
       "cucsGmetaHolderFsmFsmStatus": cucsGmetaHolderFsmFsmStatus,
       "cucsGmetaHolderFsmProgress": cucsGmetaHolderFsmProgress,
       "cucsGmetaHolderFsmRmtErrCode": cucsGmetaHolderFsmRmtErrCode,
       "cucsGmetaHolderFsmRmtErrDescr": cucsGmetaHolderFsmRmtErrDescr,
       "cucsGmetaHolderFsmRmtRslt": cucsGmetaHolderFsmRmtRslt,
       "cucsGmetaHolderFsmStageTable": cucsGmetaHolderFsmStageTable,
       "cucsGmetaHolderFsmStageEntry": cucsGmetaHolderFsmStageEntry,
       "cucsGmetaHolderFsmStageInstanceId": cucsGmetaHolderFsmStageInstanceId,
       "cucsGmetaHolderFsmStageDn": cucsGmetaHolderFsmStageDn,
       "cucsGmetaHolderFsmStageRn": cucsGmetaHolderFsmStageRn,
       "cucsGmetaHolderFsmStageDescrData": cucsGmetaHolderFsmStageDescrData,
       "cucsGmetaHolderFsmStageLastUpdateTime": cucsGmetaHolderFsmStageLastUpdateTime,
       "cucsGmetaHolderFsmStageName": cucsGmetaHolderFsmStageName,
       "cucsGmetaHolderFsmStageOrder": cucsGmetaHolderFsmStageOrder,
       "cucsGmetaHolderFsmStageRetry": cucsGmetaHolderFsmStageRetry,
       "cucsGmetaHolderFsmStageStageStatus": cucsGmetaHolderFsmStageStageStatus,
       "cucsGmetaHolderFsmTaskTable": cucsGmetaHolderFsmTaskTable,
       "cucsGmetaHolderFsmTaskEntry": cucsGmetaHolderFsmTaskEntry,
       "cucsGmetaHolderFsmTaskInstanceId": cucsGmetaHolderFsmTaskInstanceId,
       "cucsGmetaHolderFsmTaskDn": cucsGmetaHolderFsmTaskDn,
       "cucsGmetaHolderFsmTaskRn": cucsGmetaHolderFsmTaskRn,
       "cucsGmetaHolderFsmTaskCompletion": cucsGmetaHolderFsmTaskCompletion,
       "cucsGmetaHolderFsmTaskFlags": cucsGmetaHolderFsmTaskFlags,
       "cucsGmetaHolderFsmTaskItem": cucsGmetaHolderFsmTaskItem,
       "cucsGmetaHolderFsmTaskSeqId": cucsGmetaHolderFsmTaskSeqId,
       "cucsGmetaPolicyMapElementTable": cucsGmetaPolicyMapElementTable,
       "cucsGmetaPolicyMapElementEntry": cucsGmetaPolicyMapElementEntry,
       "cucsGmetaPolicyMapElementInstanceId": cucsGmetaPolicyMapElementInstanceId,
       "cucsGmetaPolicyMapElementDn": cucsGmetaPolicyMapElementDn,
       "cucsGmetaPolicyMapElementRn": cucsGmetaPolicyMapElementRn,
       "cucsGmetaPolicyMapElementName": cucsGmetaPolicyMapElementName,
       "cucsGmetaPolicyMapHolderTable": cucsGmetaPolicyMapHolderTable,
       "cucsGmetaPolicyMapHolderEntry": cucsGmetaPolicyMapHolderEntry,
       "cucsGmetaPolicyMapHolderInstanceId": cucsGmetaPolicyMapHolderInstanceId,
       "cucsGmetaPolicyMapHolderDn": cucsGmetaPolicyMapHolderDn,
       "cucsGmetaPolicyMapHolderRn": cucsGmetaPolicyMapHolderRn,
       "cucsGmetaPropTable": cucsGmetaPropTable,
       "cucsGmetaPropEntry": cucsGmetaPropEntry,
       "cucsGmetaPropInstanceId": cucsGmetaPropInstanceId,
       "cucsGmetaPropDn": cucsGmetaPropDn,
       "cucsGmetaPropRn": cucsGmetaPropRn,
       "cucsGmetaPropName": cucsGmetaPropName,
       "cucsGmetaPropOrder": cucsGmetaPropOrder,
       "cucsGmetaPropPropId": cucsGmetaPropPropId}
)
