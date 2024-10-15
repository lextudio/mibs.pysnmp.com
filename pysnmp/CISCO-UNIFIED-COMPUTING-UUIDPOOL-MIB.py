# SNMP MIB module (CISCO-UNIFIED-COMPUTING-UUIDPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-UUIDPOOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:28 2024
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

(CucsAddressUIDSuffxMask,
 CucsPolicyPolicyOwner,
 CucsPoolElementOwner,
 CucsUuidpoolPoolAssignmentOrder) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsAddressUIDSuffxMask",
    "CucsPolicyPolicyOwner",
    "CucsPoolElementOwner",
    "CucsUuidpoolPoolAssignmentOrder")

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

cucsUuidpoolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsUuidpoolAddrTable_Object = MibTable
cucsUuidpoolAddrTable = _CucsUuidpoolAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 1)
)
if mibBuilder.loadTexts:
    cucsUuidpoolAddrTable.setStatus("current")
_CucsUuidpoolAddrEntry_Object = MibTableRow
cucsUuidpoolAddrEntry = _CucsUuidpoolAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 1, 1)
)
cucsUuidpoolAddrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-UUIDPOOL-MIB", "cucsUuidpoolAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsUuidpoolAddrEntry.setStatus("current")
_CucsUuidpoolAddrInstanceId_Type = CucsManagedObjectId
_CucsUuidpoolAddrInstanceId_Object = MibTableColumn
cucsUuidpoolAddrInstanceId = _CucsUuidpoolAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 1, 1, 1),
    _CucsUuidpoolAddrInstanceId_Type()
)
cucsUuidpoolAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsUuidpoolAddrInstanceId.setStatus("current")
_CucsUuidpoolAddrDn_Type = CucsManagedObjectDn
_CucsUuidpoolAddrDn_Object = MibTableColumn
cucsUuidpoolAddrDn = _CucsUuidpoolAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 1, 1, 2),
    _CucsUuidpoolAddrDn_Type()
)
cucsUuidpoolAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolAddrDn.setStatus("current")
_CucsUuidpoolAddrRn_Type = SnmpAdminString
_CucsUuidpoolAddrRn_Object = MibTableColumn
cucsUuidpoolAddrRn = _CucsUuidpoolAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 1, 1, 3),
    _CucsUuidpoolAddrRn_Type()
)
cucsUuidpoolAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolAddrRn.setStatus("current")
_CucsUuidpoolAddrAssigned_Type = TruthValue
_CucsUuidpoolAddrAssigned_Object = MibTableColumn
cucsUuidpoolAddrAssigned = _CucsUuidpoolAddrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 1, 1, 4),
    _CucsUuidpoolAddrAssigned_Type()
)
cucsUuidpoolAddrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolAddrAssigned.setStatus("current")
_CucsUuidpoolAddrAssignedToDn_Type = SnmpAdminString
_CucsUuidpoolAddrAssignedToDn_Object = MibTableColumn
cucsUuidpoolAddrAssignedToDn = _CucsUuidpoolAddrAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 1, 1, 5),
    _CucsUuidpoolAddrAssignedToDn_Type()
)
cucsUuidpoolAddrAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolAddrAssignedToDn.setStatus("current")
_CucsUuidpoolAddrId_Type = SnmpAdminString
_CucsUuidpoolAddrId_Object = MibTableColumn
cucsUuidpoolAddrId = _CucsUuidpoolAddrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 1, 1, 6),
    _CucsUuidpoolAddrId_Type()
)
cucsUuidpoolAddrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolAddrId.setStatus("current")
_CucsUuidpoolAddrOwner_Type = CucsPoolElementOwner
_CucsUuidpoolAddrOwner_Object = MibTableColumn
cucsUuidpoolAddrOwner = _CucsUuidpoolAddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 1, 1, 7),
    _CucsUuidpoolAddrOwner_Type()
)
cucsUuidpoolAddrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolAddrOwner.setStatus("current")
_CucsUuidpoolAddrGlobalAssignedCnt_Type = Gauge32
_CucsUuidpoolAddrGlobalAssignedCnt_Object = MibTableColumn
cucsUuidpoolAddrGlobalAssignedCnt = _CucsUuidpoolAddrGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 1, 1, 8),
    _CucsUuidpoolAddrGlobalAssignedCnt_Type()
)
cucsUuidpoolAddrGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolAddrGlobalAssignedCnt.setStatus("current")
_CucsUuidpoolAddrGlobalDefinedCnt_Type = Gauge32
_CucsUuidpoolAddrGlobalDefinedCnt_Object = MibTableColumn
cucsUuidpoolAddrGlobalDefinedCnt = _CucsUuidpoolAddrGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 1, 1, 9),
    _CucsUuidpoolAddrGlobalDefinedCnt_Type()
)
cucsUuidpoolAddrGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolAddrGlobalDefinedCnt.setStatus("current")
_CucsUuidpoolBlockTable_Object = MibTable
cucsUuidpoolBlockTable = _CucsUuidpoolBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 2)
)
if mibBuilder.loadTexts:
    cucsUuidpoolBlockTable.setStatus("current")
_CucsUuidpoolBlockEntry_Object = MibTableRow
cucsUuidpoolBlockEntry = _CucsUuidpoolBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 2, 1)
)
cucsUuidpoolBlockEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-UUIDPOOL-MIB", "cucsUuidpoolBlockInstanceId"),
)
if mibBuilder.loadTexts:
    cucsUuidpoolBlockEntry.setStatus("current")
_CucsUuidpoolBlockInstanceId_Type = CucsManagedObjectId
_CucsUuidpoolBlockInstanceId_Object = MibTableColumn
cucsUuidpoolBlockInstanceId = _CucsUuidpoolBlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 2, 1, 1),
    _CucsUuidpoolBlockInstanceId_Type()
)
cucsUuidpoolBlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsUuidpoolBlockInstanceId.setStatus("current")
_CucsUuidpoolBlockDn_Type = CucsManagedObjectDn
_CucsUuidpoolBlockDn_Object = MibTableColumn
cucsUuidpoolBlockDn = _CucsUuidpoolBlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 2, 1, 2),
    _CucsUuidpoolBlockDn_Type()
)
cucsUuidpoolBlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolBlockDn.setStatus("current")
_CucsUuidpoolBlockRn_Type = SnmpAdminString
_CucsUuidpoolBlockRn_Object = MibTableColumn
cucsUuidpoolBlockRn = _CucsUuidpoolBlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 2, 1, 3),
    _CucsUuidpoolBlockRn_Type()
)
cucsUuidpoolBlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolBlockRn.setStatus("current")
_CucsUuidpoolBlockFrom_Type = Unsigned64
_CucsUuidpoolBlockFrom_Object = MibTableColumn
cucsUuidpoolBlockFrom = _CucsUuidpoolBlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 2, 1, 4),
    _CucsUuidpoolBlockFrom_Type()
)
cucsUuidpoolBlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolBlockFrom.setStatus("current")
_CucsUuidpoolBlockTo_Type = Unsigned64
_CucsUuidpoolBlockTo_Object = MibTableColumn
cucsUuidpoolBlockTo = _CucsUuidpoolBlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 2, 1, 5),
    _CucsUuidpoolBlockTo_Type()
)
cucsUuidpoolBlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolBlockTo.setStatus("current")
_CucsUuidpoolFormatTable_Object = MibTable
cucsUuidpoolFormatTable = _CucsUuidpoolFormatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 3)
)
if mibBuilder.loadTexts:
    cucsUuidpoolFormatTable.setStatus("current")
_CucsUuidpoolFormatEntry_Object = MibTableRow
cucsUuidpoolFormatEntry = _CucsUuidpoolFormatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 3, 1)
)
cucsUuidpoolFormatEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-UUIDPOOL-MIB", "cucsUuidpoolFormatInstanceId"),
)
if mibBuilder.loadTexts:
    cucsUuidpoolFormatEntry.setStatus("current")
_CucsUuidpoolFormatInstanceId_Type = CucsManagedObjectId
_CucsUuidpoolFormatInstanceId_Object = MibTableColumn
cucsUuidpoolFormatInstanceId = _CucsUuidpoolFormatInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 3, 1, 1),
    _CucsUuidpoolFormatInstanceId_Type()
)
cucsUuidpoolFormatInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsUuidpoolFormatInstanceId.setStatus("current")
_CucsUuidpoolFormatDn_Type = CucsManagedObjectDn
_CucsUuidpoolFormatDn_Object = MibTableColumn
cucsUuidpoolFormatDn = _CucsUuidpoolFormatDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 3, 1, 2),
    _CucsUuidpoolFormatDn_Type()
)
cucsUuidpoolFormatDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolFormatDn.setStatus("current")
_CucsUuidpoolFormatRn_Type = SnmpAdminString
_CucsUuidpoolFormatRn_Object = MibTableColumn
cucsUuidpoolFormatRn = _CucsUuidpoolFormatRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 3, 1, 3),
    _CucsUuidpoolFormatRn_Type()
)
cucsUuidpoolFormatRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolFormatRn.setStatus("current")
_CucsUuidpoolFormatFormat_Type = Unsigned64
_CucsUuidpoolFormatFormat_Object = MibTableColumn
cucsUuidpoolFormatFormat = _CucsUuidpoolFormatFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 3, 1, 4),
    _CucsUuidpoolFormatFormat_Type()
)
cucsUuidpoolFormatFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolFormatFormat.setStatus("current")
_CucsUuidpoolFormatMask_Type = CucsAddressUIDSuffxMask
_CucsUuidpoolFormatMask_Object = MibTableColumn
cucsUuidpoolFormatMask = _CucsUuidpoolFormatMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 3, 1, 5),
    _CucsUuidpoolFormatMask_Type()
)
cucsUuidpoolFormatMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolFormatMask.setStatus("current")
_CucsUuidpoolPoolTable_Object = MibTable
cucsUuidpoolPoolTable = _CucsUuidpoolPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 4)
)
if mibBuilder.loadTexts:
    cucsUuidpoolPoolTable.setStatus("current")
_CucsUuidpoolPoolEntry_Object = MibTableRow
cucsUuidpoolPoolEntry = _CucsUuidpoolPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 4, 1)
)
cucsUuidpoolPoolEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-UUIDPOOL-MIB", "cucsUuidpoolPoolInstanceId"),
)
if mibBuilder.loadTexts:
    cucsUuidpoolPoolEntry.setStatus("current")
_CucsUuidpoolPoolInstanceId_Type = CucsManagedObjectId
_CucsUuidpoolPoolInstanceId_Object = MibTableColumn
cucsUuidpoolPoolInstanceId = _CucsUuidpoolPoolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 4, 1, 1),
    _CucsUuidpoolPoolInstanceId_Type()
)
cucsUuidpoolPoolInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsUuidpoolPoolInstanceId.setStatus("current")
_CucsUuidpoolPoolDn_Type = CucsManagedObjectDn
_CucsUuidpoolPoolDn_Object = MibTableColumn
cucsUuidpoolPoolDn = _CucsUuidpoolPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 4, 1, 2),
    _CucsUuidpoolPoolDn_Type()
)
cucsUuidpoolPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPoolDn.setStatus("current")
_CucsUuidpoolPoolRn_Type = SnmpAdminString
_CucsUuidpoolPoolRn_Object = MibTableColumn
cucsUuidpoolPoolRn = _CucsUuidpoolPoolRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 4, 1, 3),
    _CucsUuidpoolPoolRn_Type()
)
cucsUuidpoolPoolRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPoolRn.setStatus("current")
_CucsUuidpoolPoolAssigned_Type = Gauge32
_CucsUuidpoolPoolAssigned_Object = MibTableColumn
cucsUuidpoolPoolAssigned = _CucsUuidpoolPoolAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 4, 1, 4),
    _CucsUuidpoolPoolAssigned_Type()
)
cucsUuidpoolPoolAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPoolAssigned.setStatus("current")
_CucsUuidpoolPoolDescr_Type = SnmpAdminString
_CucsUuidpoolPoolDescr_Object = MibTableColumn
cucsUuidpoolPoolDescr = _CucsUuidpoolPoolDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 4, 1, 5),
    _CucsUuidpoolPoolDescr_Type()
)
cucsUuidpoolPoolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPoolDescr.setStatus("current")
_CucsUuidpoolPoolIntId_Type = SnmpAdminString
_CucsUuidpoolPoolIntId_Object = MibTableColumn
cucsUuidpoolPoolIntId = _CucsUuidpoolPoolIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 4, 1, 6),
    _CucsUuidpoolPoolIntId_Type()
)
cucsUuidpoolPoolIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPoolIntId.setStatus("current")
_CucsUuidpoolPoolName_Type = SnmpAdminString
_CucsUuidpoolPoolName_Object = MibTableColumn
cucsUuidpoolPoolName = _CucsUuidpoolPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 4, 1, 7),
    _CucsUuidpoolPoolName_Type()
)
cucsUuidpoolPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPoolName.setStatus("current")
_CucsUuidpoolPoolPrefix_Type = Unsigned64
_CucsUuidpoolPoolPrefix_Object = MibTableColumn
cucsUuidpoolPoolPrefix = _CucsUuidpoolPoolPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 4, 1, 8),
    _CucsUuidpoolPoolPrefix_Type()
)
cucsUuidpoolPoolPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPoolPrefix.setStatus("current")
_CucsUuidpoolPoolSize_Type = Gauge32
_CucsUuidpoolPoolSize_Object = MibTableColumn
cucsUuidpoolPoolSize = _CucsUuidpoolPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 4, 1, 9),
    _CucsUuidpoolPoolSize_Type()
)
cucsUuidpoolPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPoolSize.setStatus("current")
_CucsUuidpoolPoolAssignmentOrder_Type = CucsUuidpoolPoolAssignmentOrder
_CucsUuidpoolPoolAssignmentOrder_Object = MibTableColumn
cucsUuidpoolPoolAssignmentOrder = _CucsUuidpoolPoolAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 4, 1, 10),
    _CucsUuidpoolPoolAssignmentOrder_Type()
)
cucsUuidpoolPoolAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPoolAssignmentOrder.setStatus("current")
_CucsUuidpoolPoolPolicyLevel_Type = Gauge32
_CucsUuidpoolPoolPolicyLevel_Object = MibTableColumn
cucsUuidpoolPoolPolicyLevel = _CucsUuidpoolPoolPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 4, 1, 11),
    _CucsUuidpoolPoolPolicyLevel_Type()
)
cucsUuidpoolPoolPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPoolPolicyLevel.setStatus("current")
_CucsUuidpoolPoolPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsUuidpoolPoolPolicyOwner_Object = MibTableColumn
cucsUuidpoolPoolPolicyOwner = _CucsUuidpoolPoolPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 4, 1, 12),
    _CucsUuidpoolPoolPolicyOwner_Type()
)
cucsUuidpoolPoolPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPoolPolicyOwner.setStatus("current")
_CucsUuidpoolPoolableTable_Object = MibTable
cucsUuidpoolPoolableTable = _CucsUuidpoolPoolableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 5)
)
if mibBuilder.loadTexts:
    cucsUuidpoolPoolableTable.setStatus("current")
_CucsUuidpoolPoolableEntry_Object = MibTableRow
cucsUuidpoolPoolableEntry = _CucsUuidpoolPoolableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 5, 1)
)
cucsUuidpoolPoolableEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-UUIDPOOL-MIB", "cucsUuidpoolPoolableInstanceId"),
)
if mibBuilder.loadTexts:
    cucsUuidpoolPoolableEntry.setStatus("current")
_CucsUuidpoolPoolableInstanceId_Type = CucsManagedObjectId
_CucsUuidpoolPoolableInstanceId_Object = MibTableColumn
cucsUuidpoolPoolableInstanceId = _CucsUuidpoolPoolableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 5, 1, 1),
    _CucsUuidpoolPoolableInstanceId_Type()
)
cucsUuidpoolPoolableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsUuidpoolPoolableInstanceId.setStatus("current")
_CucsUuidpoolPoolableDn_Type = CucsManagedObjectDn
_CucsUuidpoolPoolableDn_Object = MibTableColumn
cucsUuidpoolPoolableDn = _CucsUuidpoolPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 5, 1, 2),
    _CucsUuidpoolPoolableDn_Type()
)
cucsUuidpoolPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPoolableDn.setStatus("current")
_CucsUuidpoolPoolableRn_Type = SnmpAdminString
_CucsUuidpoolPoolableRn_Object = MibTableColumn
cucsUuidpoolPoolableRn = _CucsUuidpoolPoolableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 5, 1, 3),
    _CucsUuidpoolPoolableRn_Type()
)
cucsUuidpoolPoolableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPoolableRn.setStatus("current")
_CucsUuidpoolPoolableId_Type = Unsigned64
_CucsUuidpoolPoolableId_Object = MibTableColumn
cucsUuidpoolPoolableId = _CucsUuidpoolPoolableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 5, 1, 4),
    _CucsUuidpoolPoolableId_Type()
)
cucsUuidpoolPoolableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPoolableId.setStatus("current")
_CucsUuidpoolPoolablePoolDn_Type = SnmpAdminString
_CucsUuidpoolPoolablePoolDn_Object = MibTableColumn
cucsUuidpoolPoolablePoolDn = _CucsUuidpoolPoolablePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 5, 1, 5),
    _CucsUuidpoolPoolablePoolDn_Type()
)
cucsUuidpoolPoolablePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPoolablePoolDn.setStatus("current")
_CucsUuidpoolPooledTable_Object = MibTable
cucsUuidpoolPooledTable = _CucsUuidpoolPooledTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 6)
)
if mibBuilder.loadTexts:
    cucsUuidpoolPooledTable.setStatus("current")
_CucsUuidpoolPooledEntry_Object = MibTableRow
cucsUuidpoolPooledEntry = _CucsUuidpoolPooledEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 6, 1)
)
cucsUuidpoolPooledEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-UUIDPOOL-MIB", "cucsUuidpoolPooledInstanceId"),
)
if mibBuilder.loadTexts:
    cucsUuidpoolPooledEntry.setStatus("current")
_CucsUuidpoolPooledInstanceId_Type = CucsManagedObjectId
_CucsUuidpoolPooledInstanceId_Object = MibTableColumn
cucsUuidpoolPooledInstanceId = _CucsUuidpoolPooledInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 6, 1, 1),
    _CucsUuidpoolPooledInstanceId_Type()
)
cucsUuidpoolPooledInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsUuidpoolPooledInstanceId.setStatus("current")
_CucsUuidpoolPooledDn_Type = CucsManagedObjectDn
_CucsUuidpoolPooledDn_Object = MibTableColumn
cucsUuidpoolPooledDn = _CucsUuidpoolPooledDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 6, 1, 2),
    _CucsUuidpoolPooledDn_Type()
)
cucsUuidpoolPooledDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPooledDn.setStatus("current")
_CucsUuidpoolPooledRn_Type = SnmpAdminString
_CucsUuidpoolPooledRn_Object = MibTableColumn
cucsUuidpoolPooledRn = _CucsUuidpoolPooledRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 6, 1, 3),
    _CucsUuidpoolPooledRn_Type()
)
cucsUuidpoolPooledRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPooledRn.setStatus("current")
_CucsUuidpoolPooledAssigned_Type = TruthValue
_CucsUuidpoolPooledAssigned_Object = MibTableColumn
cucsUuidpoolPooledAssigned = _CucsUuidpoolPooledAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 6, 1, 4),
    _CucsUuidpoolPooledAssigned_Type()
)
cucsUuidpoolPooledAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPooledAssigned.setStatus("current")
_CucsUuidpoolPooledAssignedToDn_Type = SnmpAdminString
_CucsUuidpoolPooledAssignedToDn_Object = MibTableColumn
cucsUuidpoolPooledAssignedToDn = _CucsUuidpoolPooledAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 6, 1, 5),
    _CucsUuidpoolPooledAssignedToDn_Type()
)
cucsUuidpoolPooledAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPooledAssignedToDn.setStatus("current")
_CucsUuidpoolPooledId_Type = Unsigned64
_CucsUuidpoolPooledId_Object = MibTableColumn
cucsUuidpoolPooledId = _CucsUuidpoolPooledId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 6, 1, 6),
    _CucsUuidpoolPooledId_Type()
)
cucsUuidpoolPooledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPooledId.setStatus("current")
_CucsUuidpoolPooledPoolableDn_Type = SnmpAdminString
_CucsUuidpoolPooledPoolableDn_Object = MibTableColumn
cucsUuidpoolPooledPoolableDn = _CucsUuidpoolPooledPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 6, 1, 7),
    _CucsUuidpoolPooledPoolableDn_Type()
)
cucsUuidpoolPooledPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPooledPoolableDn.setStatus("current")
_CucsUuidpoolPooledPrevAssignedToDn_Type = SnmpAdminString
_CucsUuidpoolPooledPrevAssignedToDn_Object = MibTableColumn
cucsUuidpoolPooledPrevAssignedToDn = _CucsUuidpoolPooledPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 6, 1, 8),
    _CucsUuidpoolPooledPrevAssignedToDn_Type()
)
cucsUuidpoolPooledPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolPooledPrevAssignedToDn.setStatus("current")
_CucsUuidpoolUniverseTable_Object = MibTable
cucsUuidpoolUniverseTable = _CucsUuidpoolUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 7)
)
if mibBuilder.loadTexts:
    cucsUuidpoolUniverseTable.setStatus("current")
_CucsUuidpoolUniverseEntry_Object = MibTableRow
cucsUuidpoolUniverseEntry = _CucsUuidpoolUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 7, 1)
)
cucsUuidpoolUniverseEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-UUIDPOOL-MIB", "cucsUuidpoolUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cucsUuidpoolUniverseEntry.setStatus("current")
_CucsUuidpoolUniverseInstanceId_Type = CucsManagedObjectId
_CucsUuidpoolUniverseInstanceId_Object = MibTableColumn
cucsUuidpoolUniverseInstanceId = _CucsUuidpoolUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 7, 1, 1),
    _CucsUuidpoolUniverseInstanceId_Type()
)
cucsUuidpoolUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsUuidpoolUniverseInstanceId.setStatus("current")
_CucsUuidpoolUniverseDn_Type = CucsManagedObjectDn
_CucsUuidpoolUniverseDn_Object = MibTableColumn
cucsUuidpoolUniverseDn = _CucsUuidpoolUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 7, 1, 2),
    _CucsUuidpoolUniverseDn_Type()
)
cucsUuidpoolUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolUniverseDn.setStatus("current")
_CucsUuidpoolUniverseRn_Type = SnmpAdminString
_CucsUuidpoolUniverseRn_Object = MibTableColumn
cucsUuidpoolUniverseRn = _CucsUuidpoolUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 51, 7, 1, 3),
    _CucsUuidpoolUniverseRn_Type()
)
cucsUuidpoolUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsUuidpoolUniverseRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-UUIDPOOL-MIB",
    **{"cucsUuidpoolObjects": cucsUuidpoolObjects,
       "cucsUuidpoolAddrTable": cucsUuidpoolAddrTable,
       "cucsUuidpoolAddrEntry": cucsUuidpoolAddrEntry,
       "cucsUuidpoolAddrInstanceId": cucsUuidpoolAddrInstanceId,
       "cucsUuidpoolAddrDn": cucsUuidpoolAddrDn,
       "cucsUuidpoolAddrRn": cucsUuidpoolAddrRn,
       "cucsUuidpoolAddrAssigned": cucsUuidpoolAddrAssigned,
       "cucsUuidpoolAddrAssignedToDn": cucsUuidpoolAddrAssignedToDn,
       "cucsUuidpoolAddrId": cucsUuidpoolAddrId,
       "cucsUuidpoolAddrOwner": cucsUuidpoolAddrOwner,
       "cucsUuidpoolAddrGlobalAssignedCnt": cucsUuidpoolAddrGlobalAssignedCnt,
       "cucsUuidpoolAddrGlobalDefinedCnt": cucsUuidpoolAddrGlobalDefinedCnt,
       "cucsUuidpoolBlockTable": cucsUuidpoolBlockTable,
       "cucsUuidpoolBlockEntry": cucsUuidpoolBlockEntry,
       "cucsUuidpoolBlockInstanceId": cucsUuidpoolBlockInstanceId,
       "cucsUuidpoolBlockDn": cucsUuidpoolBlockDn,
       "cucsUuidpoolBlockRn": cucsUuidpoolBlockRn,
       "cucsUuidpoolBlockFrom": cucsUuidpoolBlockFrom,
       "cucsUuidpoolBlockTo": cucsUuidpoolBlockTo,
       "cucsUuidpoolFormatTable": cucsUuidpoolFormatTable,
       "cucsUuidpoolFormatEntry": cucsUuidpoolFormatEntry,
       "cucsUuidpoolFormatInstanceId": cucsUuidpoolFormatInstanceId,
       "cucsUuidpoolFormatDn": cucsUuidpoolFormatDn,
       "cucsUuidpoolFormatRn": cucsUuidpoolFormatRn,
       "cucsUuidpoolFormatFormat": cucsUuidpoolFormatFormat,
       "cucsUuidpoolFormatMask": cucsUuidpoolFormatMask,
       "cucsUuidpoolPoolTable": cucsUuidpoolPoolTable,
       "cucsUuidpoolPoolEntry": cucsUuidpoolPoolEntry,
       "cucsUuidpoolPoolInstanceId": cucsUuidpoolPoolInstanceId,
       "cucsUuidpoolPoolDn": cucsUuidpoolPoolDn,
       "cucsUuidpoolPoolRn": cucsUuidpoolPoolRn,
       "cucsUuidpoolPoolAssigned": cucsUuidpoolPoolAssigned,
       "cucsUuidpoolPoolDescr": cucsUuidpoolPoolDescr,
       "cucsUuidpoolPoolIntId": cucsUuidpoolPoolIntId,
       "cucsUuidpoolPoolName": cucsUuidpoolPoolName,
       "cucsUuidpoolPoolPrefix": cucsUuidpoolPoolPrefix,
       "cucsUuidpoolPoolSize": cucsUuidpoolPoolSize,
       "cucsUuidpoolPoolAssignmentOrder": cucsUuidpoolPoolAssignmentOrder,
       "cucsUuidpoolPoolPolicyLevel": cucsUuidpoolPoolPolicyLevel,
       "cucsUuidpoolPoolPolicyOwner": cucsUuidpoolPoolPolicyOwner,
       "cucsUuidpoolPoolableTable": cucsUuidpoolPoolableTable,
       "cucsUuidpoolPoolableEntry": cucsUuidpoolPoolableEntry,
       "cucsUuidpoolPoolableInstanceId": cucsUuidpoolPoolableInstanceId,
       "cucsUuidpoolPoolableDn": cucsUuidpoolPoolableDn,
       "cucsUuidpoolPoolableRn": cucsUuidpoolPoolableRn,
       "cucsUuidpoolPoolableId": cucsUuidpoolPoolableId,
       "cucsUuidpoolPoolablePoolDn": cucsUuidpoolPoolablePoolDn,
       "cucsUuidpoolPooledTable": cucsUuidpoolPooledTable,
       "cucsUuidpoolPooledEntry": cucsUuidpoolPooledEntry,
       "cucsUuidpoolPooledInstanceId": cucsUuidpoolPooledInstanceId,
       "cucsUuidpoolPooledDn": cucsUuidpoolPooledDn,
       "cucsUuidpoolPooledRn": cucsUuidpoolPooledRn,
       "cucsUuidpoolPooledAssigned": cucsUuidpoolPooledAssigned,
       "cucsUuidpoolPooledAssignedToDn": cucsUuidpoolPooledAssignedToDn,
       "cucsUuidpoolPooledId": cucsUuidpoolPooledId,
       "cucsUuidpoolPooledPoolableDn": cucsUuidpoolPooledPoolableDn,
       "cucsUuidpoolPooledPrevAssignedToDn": cucsUuidpoolPooledPrevAssignedToDn,
       "cucsUuidpoolUniverseTable": cucsUuidpoolUniverseTable,
       "cucsUuidpoolUniverseEntry": cucsUuidpoolUniverseEntry,
       "cucsUuidpoolUniverseInstanceId": cucsUuidpoolUniverseInstanceId,
       "cucsUuidpoolUniverseDn": cucsUuidpoolUniverseDn,
       "cucsUuidpoolUniverseRn": cucsUuidpoolUniverseRn}
)
