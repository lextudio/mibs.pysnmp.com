# SNMP MIB module (CISCO-UNIFIED-COMPUTING-IQNPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-IQNPOOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:47 2024
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

(CucsIqnpoolBlockFrom,
 CucsIqnpoolBlockTo,
 CucsIqnpoolPoolAssignmentOrder,
 CucsIqnpoolTransportBlockFrom,
 CucsIqnpoolTransportBlockTo,
 CucsPolicyPolicyOwner,
 CucsPoolElementOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsIqnpoolBlockFrom",
    "CucsIqnpoolBlockTo",
    "CucsIqnpoolPoolAssignmentOrder",
    "CucsIqnpoolTransportBlockFrom",
    "CucsIqnpoolTransportBlockTo",
    "CucsPolicyPolicyOwner",
    "CucsPoolElementOwner")

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

cucsIqnpoolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsIqnpoolAddrTable_Object = MibTable
cucsIqnpoolAddrTable = _CucsIqnpoolAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 1)
)
if mibBuilder.loadTexts:
    cucsIqnpoolAddrTable.setStatus("current")
_CucsIqnpoolAddrEntry_Object = MibTableRow
cucsIqnpoolAddrEntry = _CucsIqnpoolAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 1, 1)
)
cucsIqnpoolAddrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IQNPOOL-MIB", "cucsIqnpoolAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIqnpoolAddrEntry.setStatus("current")
_CucsIqnpoolAddrInstanceId_Type = CucsManagedObjectId
_CucsIqnpoolAddrInstanceId_Object = MibTableColumn
cucsIqnpoolAddrInstanceId = _CucsIqnpoolAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 1, 1, 1),
    _CucsIqnpoolAddrInstanceId_Type()
)
cucsIqnpoolAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIqnpoolAddrInstanceId.setStatus("current")
_CucsIqnpoolAddrDn_Type = CucsManagedObjectDn
_CucsIqnpoolAddrDn_Object = MibTableColumn
cucsIqnpoolAddrDn = _CucsIqnpoolAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 1, 1, 2),
    _CucsIqnpoolAddrDn_Type()
)
cucsIqnpoolAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolAddrDn.setStatus("current")
_CucsIqnpoolAddrRn_Type = SnmpAdminString
_CucsIqnpoolAddrRn_Object = MibTableColumn
cucsIqnpoolAddrRn = _CucsIqnpoolAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 1, 1, 3),
    _CucsIqnpoolAddrRn_Type()
)
cucsIqnpoolAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolAddrRn.setStatus("current")
_CucsIqnpoolAddrAssigned_Type = TruthValue
_CucsIqnpoolAddrAssigned_Object = MibTableColumn
cucsIqnpoolAddrAssigned = _CucsIqnpoolAddrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 1, 1, 4),
    _CucsIqnpoolAddrAssigned_Type()
)
cucsIqnpoolAddrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolAddrAssigned.setStatus("current")
_CucsIqnpoolAddrAssignedToDn_Type = SnmpAdminString
_CucsIqnpoolAddrAssignedToDn_Object = MibTableColumn
cucsIqnpoolAddrAssignedToDn = _CucsIqnpoolAddrAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 1, 1, 5),
    _CucsIqnpoolAddrAssignedToDn_Type()
)
cucsIqnpoolAddrAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolAddrAssignedToDn.setStatus("current")
_CucsIqnpoolAddrName_Type = SnmpAdminString
_CucsIqnpoolAddrName_Object = MibTableColumn
cucsIqnpoolAddrName = _CucsIqnpoolAddrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 1, 1, 6),
    _CucsIqnpoolAddrName_Type()
)
cucsIqnpoolAddrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolAddrName.setStatus("current")
_CucsIqnpoolAddrOwner_Type = CucsPoolElementOwner
_CucsIqnpoolAddrOwner_Object = MibTableColumn
cucsIqnpoolAddrOwner = _CucsIqnpoolAddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 1, 1, 7),
    _CucsIqnpoolAddrOwner_Type()
)
cucsIqnpoolAddrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolAddrOwner.setStatus("current")
_CucsIqnpoolAddrGlobalAssignedCnt_Type = Gauge32
_CucsIqnpoolAddrGlobalAssignedCnt_Object = MibTableColumn
cucsIqnpoolAddrGlobalAssignedCnt = _CucsIqnpoolAddrGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 1, 1, 8),
    _CucsIqnpoolAddrGlobalAssignedCnt_Type()
)
cucsIqnpoolAddrGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolAddrGlobalAssignedCnt.setStatus("current")
_CucsIqnpoolAddrGlobalDefinedCnt_Type = Gauge32
_CucsIqnpoolAddrGlobalDefinedCnt_Object = MibTableColumn
cucsIqnpoolAddrGlobalDefinedCnt = _CucsIqnpoolAddrGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 1, 1, 9),
    _CucsIqnpoolAddrGlobalDefinedCnt_Type()
)
cucsIqnpoolAddrGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolAddrGlobalDefinedCnt.setStatus("current")
_CucsIqnpoolBlockTable_Object = MibTable
cucsIqnpoolBlockTable = _CucsIqnpoolBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 2)
)
if mibBuilder.loadTexts:
    cucsIqnpoolBlockTable.setStatus("current")
_CucsIqnpoolBlockEntry_Object = MibTableRow
cucsIqnpoolBlockEntry = _CucsIqnpoolBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 2, 1)
)
cucsIqnpoolBlockEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IQNPOOL-MIB", "cucsIqnpoolBlockInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIqnpoolBlockEntry.setStatus("current")
_CucsIqnpoolBlockInstanceId_Type = CucsManagedObjectId
_CucsIqnpoolBlockInstanceId_Object = MibTableColumn
cucsIqnpoolBlockInstanceId = _CucsIqnpoolBlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 2, 1, 1),
    _CucsIqnpoolBlockInstanceId_Type()
)
cucsIqnpoolBlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIqnpoolBlockInstanceId.setStatus("current")
_CucsIqnpoolBlockDn_Type = CucsManagedObjectDn
_CucsIqnpoolBlockDn_Object = MibTableColumn
cucsIqnpoolBlockDn = _CucsIqnpoolBlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 2, 1, 2),
    _CucsIqnpoolBlockDn_Type()
)
cucsIqnpoolBlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolBlockDn.setStatus("current")
_CucsIqnpoolBlockRn_Type = SnmpAdminString
_CucsIqnpoolBlockRn_Object = MibTableColumn
cucsIqnpoolBlockRn = _CucsIqnpoolBlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 2, 1, 3),
    _CucsIqnpoolBlockRn_Type()
)
cucsIqnpoolBlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolBlockRn.setStatus("current")
_CucsIqnpoolBlockFrom_Type = CucsIqnpoolBlockFrom
_CucsIqnpoolBlockFrom_Object = MibTableColumn
cucsIqnpoolBlockFrom = _CucsIqnpoolBlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 2, 1, 4),
    _CucsIqnpoolBlockFrom_Type()
)
cucsIqnpoolBlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolBlockFrom.setStatus("current")
_CucsIqnpoolBlockSuffix_Type = SnmpAdminString
_CucsIqnpoolBlockSuffix_Object = MibTableColumn
cucsIqnpoolBlockSuffix = _CucsIqnpoolBlockSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 2, 1, 6),
    _CucsIqnpoolBlockSuffix_Type()
)
cucsIqnpoolBlockSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolBlockSuffix.setStatus("current")
_CucsIqnpoolBlockTo_Type = CucsIqnpoolBlockTo
_CucsIqnpoolBlockTo_Object = MibTableColumn
cucsIqnpoolBlockTo = _CucsIqnpoolBlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 2, 1, 7),
    _CucsIqnpoolBlockTo_Type()
)
cucsIqnpoolBlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolBlockTo.setStatus("current")
_CucsIqnpoolFormatTable_Object = MibTable
cucsIqnpoolFormatTable = _CucsIqnpoolFormatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 3)
)
if mibBuilder.loadTexts:
    cucsIqnpoolFormatTable.setStatus("current")
_CucsIqnpoolFormatEntry_Object = MibTableRow
cucsIqnpoolFormatEntry = _CucsIqnpoolFormatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 3, 1)
)
cucsIqnpoolFormatEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IQNPOOL-MIB", "cucsIqnpoolFormatInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIqnpoolFormatEntry.setStatus("current")
_CucsIqnpoolFormatInstanceId_Type = CucsManagedObjectId
_CucsIqnpoolFormatInstanceId_Object = MibTableColumn
cucsIqnpoolFormatInstanceId = _CucsIqnpoolFormatInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 3, 1, 1),
    _CucsIqnpoolFormatInstanceId_Type()
)
cucsIqnpoolFormatInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIqnpoolFormatInstanceId.setStatus("current")
_CucsIqnpoolFormatDn_Type = CucsManagedObjectDn
_CucsIqnpoolFormatDn_Object = MibTableColumn
cucsIqnpoolFormatDn = _CucsIqnpoolFormatDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 3, 1, 2),
    _CucsIqnpoolFormatDn_Type()
)
cucsIqnpoolFormatDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolFormatDn.setStatus("current")
_CucsIqnpoolFormatRn_Type = SnmpAdminString
_CucsIqnpoolFormatRn_Object = MibTableColumn
cucsIqnpoolFormatRn = _CucsIqnpoolFormatRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 3, 1, 3),
    _CucsIqnpoolFormatRn_Type()
)
cucsIqnpoolFormatRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolFormatRn.setStatus("current")
_CucsIqnpoolFormatFormat_Type = SnmpAdminString
_CucsIqnpoolFormatFormat_Object = MibTableColumn
cucsIqnpoolFormatFormat = _CucsIqnpoolFormatFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 3, 1, 4),
    _CucsIqnpoolFormatFormat_Type()
)
cucsIqnpoolFormatFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolFormatFormat.setStatus("current")
_CucsIqnpoolPoolTable_Object = MibTable
cucsIqnpoolPoolTable = _CucsIqnpoolPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 4)
)
if mibBuilder.loadTexts:
    cucsIqnpoolPoolTable.setStatus("current")
_CucsIqnpoolPoolEntry_Object = MibTableRow
cucsIqnpoolPoolEntry = _CucsIqnpoolPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 4, 1)
)
cucsIqnpoolPoolEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IQNPOOL-MIB", "cucsIqnpoolPoolInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIqnpoolPoolEntry.setStatus("current")
_CucsIqnpoolPoolInstanceId_Type = CucsManagedObjectId
_CucsIqnpoolPoolInstanceId_Object = MibTableColumn
cucsIqnpoolPoolInstanceId = _CucsIqnpoolPoolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 4, 1, 1),
    _CucsIqnpoolPoolInstanceId_Type()
)
cucsIqnpoolPoolInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIqnpoolPoolInstanceId.setStatus("current")
_CucsIqnpoolPoolDn_Type = CucsManagedObjectDn
_CucsIqnpoolPoolDn_Object = MibTableColumn
cucsIqnpoolPoolDn = _CucsIqnpoolPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 4, 1, 2),
    _CucsIqnpoolPoolDn_Type()
)
cucsIqnpoolPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPoolDn.setStatus("current")
_CucsIqnpoolPoolRn_Type = SnmpAdminString
_CucsIqnpoolPoolRn_Object = MibTableColumn
cucsIqnpoolPoolRn = _CucsIqnpoolPoolRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 4, 1, 3),
    _CucsIqnpoolPoolRn_Type()
)
cucsIqnpoolPoolRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPoolRn.setStatus("current")
_CucsIqnpoolPoolAssigned_Type = Gauge32
_CucsIqnpoolPoolAssigned_Object = MibTableColumn
cucsIqnpoolPoolAssigned = _CucsIqnpoolPoolAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 4, 1, 4),
    _CucsIqnpoolPoolAssigned_Type()
)
cucsIqnpoolPoolAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPoolAssigned.setStatus("current")
_CucsIqnpoolPoolDescr_Type = SnmpAdminString
_CucsIqnpoolPoolDescr_Object = MibTableColumn
cucsIqnpoolPoolDescr = _CucsIqnpoolPoolDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 4, 1, 5),
    _CucsIqnpoolPoolDescr_Type()
)
cucsIqnpoolPoolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPoolDescr.setStatus("current")
_CucsIqnpoolPoolIntId_Type = SnmpAdminString
_CucsIqnpoolPoolIntId_Object = MibTableColumn
cucsIqnpoolPoolIntId = _CucsIqnpoolPoolIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 4, 1, 6),
    _CucsIqnpoolPoolIntId_Type()
)
cucsIqnpoolPoolIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPoolIntId.setStatus("current")
_CucsIqnpoolPoolName_Type = SnmpAdminString
_CucsIqnpoolPoolName_Object = MibTableColumn
cucsIqnpoolPoolName = _CucsIqnpoolPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 4, 1, 7),
    _CucsIqnpoolPoolName_Type()
)
cucsIqnpoolPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPoolName.setStatus("current")
_CucsIqnpoolPoolPrefix_Type = SnmpAdminString
_CucsIqnpoolPoolPrefix_Object = MibTableColumn
cucsIqnpoolPoolPrefix = _CucsIqnpoolPoolPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 4, 1, 8),
    _CucsIqnpoolPoolPrefix_Type()
)
cucsIqnpoolPoolPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPoolPrefix.setStatus("current")
_CucsIqnpoolPoolSize_Type = Gauge32
_CucsIqnpoolPoolSize_Object = MibTableColumn
cucsIqnpoolPoolSize = _CucsIqnpoolPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 4, 1, 9),
    _CucsIqnpoolPoolSize_Type()
)
cucsIqnpoolPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPoolSize.setStatus("current")
_CucsIqnpoolPoolAssignmentOrder_Type = CucsIqnpoolPoolAssignmentOrder
_CucsIqnpoolPoolAssignmentOrder_Object = MibTableColumn
cucsIqnpoolPoolAssignmentOrder = _CucsIqnpoolPoolAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 4, 1, 10),
    _CucsIqnpoolPoolAssignmentOrder_Type()
)
cucsIqnpoolPoolAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPoolAssignmentOrder.setStatus("current")
_CucsIqnpoolPoolPolicyLevel_Type = Gauge32
_CucsIqnpoolPoolPolicyLevel_Object = MibTableColumn
cucsIqnpoolPoolPolicyLevel = _CucsIqnpoolPoolPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 4, 1, 11),
    _CucsIqnpoolPoolPolicyLevel_Type()
)
cucsIqnpoolPoolPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPoolPolicyLevel.setStatus("current")
_CucsIqnpoolPoolPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsIqnpoolPoolPolicyOwner_Object = MibTableColumn
cucsIqnpoolPoolPolicyOwner = _CucsIqnpoolPoolPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 4, 1, 12),
    _CucsIqnpoolPoolPolicyOwner_Type()
)
cucsIqnpoolPoolPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPoolPolicyOwner.setStatus("current")
_CucsIqnpoolPoolableTable_Object = MibTable
cucsIqnpoolPoolableTable = _CucsIqnpoolPoolableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 5)
)
if mibBuilder.loadTexts:
    cucsIqnpoolPoolableTable.setStatus("current")
_CucsIqnpoolPoolableEntry_Object = MibTableRow
cucsIqnpoolPoolableEntry = _CucsIqnpoolPoolableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 5, 1)
)
cucsIqnpoolPoolableEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IQNPOOL-MIB", "cucsIqnpoolPoolableInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIqnpoolPoolableEntry.setStatus("current")
_CucsIqnpoolPoolableInstanceId_Type = CucsManagedObjectId
_CucsIqnpoolPoolableInstanceId_Object = MibTableColumn
cucsIqnpoolPoolableInstanceId = _CucsIqnpoolPoolableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 5, 1, 1),
    _CucsIqnpoolPoolableInstanceId_Type()
)
cucsIqnpoolPoolableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIqnpoolPoolableInstanceId.setStatus("current")
_CucsIqnpoolPoolableDn_Type = CucsManagedObjectDn
_CucsIqnpoolPoolableDn_Object = MibTableColumn
cucsIqnpoolPoolableDn = _CucsIqnpoolPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 5, 1, 2),
    _CucsIqnpoolPoolableDn_Type()
)
cucsIqnpoolPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPoolableDn.setStatus("current")
_CucsIqnpoolPoolableRn_Type = SnmpAdminString
_CucsIqnpoolPoolableRn_Object = MibTableColumn
cucsIqnpoolPoolableRn = _CucsIqnpoolPoolableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 5, 1, 3),
    _CucsIqnpoolPoolableRn_Type()
)
cucsIqnpoolPoolableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPoolableRn.setStatus("current")
_CucsIqnpoolPoolableId_Type = Unsigned64
_CucsIqnpoolPoolableId_Object = MibTableColumn
cucsIqnpoolPoolableId = _CucsIqnpoolPoolableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 5, 1, 4),
    _CucsIqnpoolPoolableId_Type()
)
cucsIqnpoolPoolableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPoolableId.setStatus("current")
_CucsIqnpoolPoolablePoolDn_Type = SnmpAdminString
_CucsIqnpoolPoolablePoolDn_Object = MibTableColumn
cucsIqnpoolPoolablePoolDn = _CucsIqnpoolPoolablePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 5, 1, 5),
    _CucsIqnpoolPoolablePoolDn_Type()
)
cucsIqnpoolPoolablePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPoolablePoolDn.setStatus("current")
_CucsIqnpoolPooledTable_Object = MibTable
cucsIqnpoolPooledTable = _CucsIqnpoolPooledTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 6)
)
if mibBuilder.loadTexts:
    cucsIqnpoolPooledTable.setStatus("current")
_CucsIqnpoolPooledEntry_Object = MibTableRow
cucsIqnpoolPooledEntry = _CucsIqnpoolPooledEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 6, 1)
)
cucsIqnpoolPooledEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IQNPOOL-MIB", "cucsIqnpoolPooledInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIqnpoolPooledEntry.setStatus("current")
_CucsIqnpoolPooledInstanceId_Type = CucsManagedObjectId
_CucsIqnpoolPooledInstanceId_Object = MibTableColumn
cucsIqnpoolPooledInstanceId = _CucsIqnpoolPooledInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 6, 1, 1),
    _CucsIqnpoolPooledInstanceId_Type()
)
cucsIqnpoolPooledInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIqnpoolPooledInstanceId.setStatus("current")
_CucsIqnpoolPooledDn_Type = CucsManagedObjectDn
_CucsIqnpoolPooledDn_Object = MibTableColumn
cucsIqnpoolPooledDn = _CucsIqnpoolPooledDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 6, 1, 2),
    _CucsIqnpoolPooledDn_Type()
)
cucsIqnpoolPooledDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPooledDn.setStatus("current")
_CucsIqnpoolPooledRn_Type = SnmpAdminString
_CucsIqnpoolPooledRn_Object = MibTableColumn
cucsIqnpoolPooledRn = _CucsIqnpoolPooledRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 6, 1, 3),
    _CucsIqnpoolPooledRn_Type()
)
cucsIqnpoolPooledRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPooledRn.setStatus("current")
_CucsIqnpoolPooledAssigned_Type = TruthValue
_CucsIqnpoolPooledAssigned_Object = MibTableColumn
cucsIqnpoolPooledAssigned = _CucsIqnpoolPooledAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 6, 1, 4),
    _CucsIqnpoolPooledAssigned_Type()
)
cucsIqnpoolPooledAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPooledAssigned.setStatus("current")
_CucsIqnpoolPooledAssignedToDn_Type = SnmpAdminString
_CucsIqnpoolPooledAssignedToDn_Object = MibTableColumn
cucsIqnpoolPooledAssignedToDn = _CucsIqnpoolPooledAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 6, 1, 5),
    _CucsIqnpoolPooledAssignedToDn_Type()
)
cucsIqnpoolPooledAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPooledAssignedToDn.setStatus("current")
_CucsIqnpoolPooledName_Type = SnmpAdminString
_CucsIqnpoolPooledName_Object = MibTableColumn
cucsIqnpoolPooledName = _CucsIqnpoolPooledName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 6, 1, 6),
    _CucsIqnpoolPooledName_Type()
)
cucsIqnpoolPooledName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPooledName.setStatus("current")
_CucsIqnpoolPooledPoolableDn_Type = SnmpAdminString
_CucsIqnpoolPooledPoolableDn_Object = MibTableColumn
cucsIqnpoolPooledPoolableDn = _CucsIqnpoolPooledPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 6, 1, 7),
    _CucsIqnpoolPooledPoolableDn_Type()
)
cucsIqnpoolPooledPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPooledPoolableDn.setStatus("current")
_CucsIqnpoolPooledPrevAssignedToDn_Type = SnmpAdminString
_CucsIqnpoolPooledPrevAssignedToDn_Object = MibTableColumn
cucsIqnpoolPooledPrevAssignedToDn = _CucsIqnpoolPooledPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 6, 1, 8),
    _CucsIqnpoolPooledPrevAssignedToDn_Type()
)
cucsIqnpoolPooledPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolPooledPrevAssignedToDn.setStatus("current")
_CucsIqnpoolUniverseTable_Object = MibTable
cucsIqnpoolUniverseTable = _CucsIqnpoolUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 7)
)
if mibBuilder.loadTexts:
    cucsIqnpoolUniverseTable.setStatus("current")
_CucsIqnpoolUniverseEntry_Object = MibTableRow
cucsIqnpoolUniverseEntry = _CucsIqnpoolUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 7, 1)
)
cucsIqnpoolUniverseEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IQNPOOL-MIB", "cucsIqnpoolUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIqnpoolUniverseEntry.setStatus("current")
_CucsIqnpoolUniverseInstanceId_Type = CucsManagedObjectId
_CucsIqnpoolUniverseInstanceId_Object = MibTableColumn
cucsIqnpoolUniverseInstanceId = _CucsIqnpoolUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 7, 1, 1),
    _CucsIqnpoolUniverseInstanceId_Type()
)
cucsIqnpoolUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIqnpoolUniverseInstanceId.setStatus("current")
_CucsIqnpoolUniverseDn_Type = CucsManagedObjectDn
_CucsIqnpoolUniverseDn_Object = MibTableColumn
cucsIqnpoolUniverseDn = _CucsIqnpoolUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 7, 1, 2),
    _CucsIqnpoolUniverseDn_Type()
)
cucsIqnpoolUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolUniverseDn.setStatus("current")
_CucsIqnpoolUniverseRn_Type = SnmpAdminString
_CucsIqnpoolUniverseRn_Object = MibTableColumn
cucsIqnpoolUniverseRn = _CucsIqnpoolUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 7, 1, 3),
    _CucsIqnpoolUniverseRn_Type()
)
cucsIqnpoolUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolUniverseRn.setStatus("current")
_CucsIqnpoolTransportBlockTable_Object = MibTable
cucsIqnpoolTransportBlockTable = _CucsIqnpoolTransportBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 8)
)
if mibBuilder.loadTexts:
    cucsIqnpoolTransportBlockTable.setStatus("current")
_CucsIqnpoolTransportBlockEntry_Object = MibTableRow
cucsIqnpoolTransportBlockEntry = _CucsIqnpoolTransportBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 8, 1)
)
cucsIqnpoolTransportBlockEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IQNPOOL-MIB", "cucsIqnpoolTransportBlockInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIqnpoolTransportBlockEntry.setStatus("current")
_CucsIqnpoolTransportBlockInstanceId_Type = CucsManagedObjectId
_CucsIqnpoolTransportBlockInstanceId_Object = MibTableColumn
cucsIqnpoolTransportBlockInstanceId = _CucsIqnpoolTransportBlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 8, 1, 1),
    _CucsIqnpoolTransportBlockInstanceId_Type()
)
cucsIqnpoolTransportBlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIqnpoolTransportBlockInstanceId.setStatus("current")
_CucsIqnpoolTransportBlockDn_Type = CucsManagedObjectDn
_CucsIqnpoolTransportBlockDn_Object = MibTableColumn
cucsIqnpoolTransportBlockDn = _CucsIqnpoolTransportBlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 8, 1, 2),
    _CucsIqnpoolTransportBlockDn_Type()
)
cucsIqnpoolTransportBlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolTransportBlockDn.setStatus("current")
_CucsIqnpoolTransportBlockRn_Type = SnmpAdminString
_CucsIqnpoolTransportBlockRn_Object = MibTableColumn
cucsIqnpoolTransportBlockRn = _CucsIqnpoolTransportBlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 8, 1, 3),
    _CucsIqnpoolTransportBlockRn_Type()
)
cucsIqnpoolTransportBlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolTransportBlockRn.setStatus("current")
_CucsIqnpoolTransportBlockFrom_Type = CucsIqnpoolTransportBlockFrom
_CucsIqnpoolTransportBlockFrom_Object = MibTableColumn
cucsIqnpoolTransportBlockFrom = _CucsIqnpoolTransportBlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 8, 1, 4),
    _CucsIqnpoolTransportBlockFrom_Type()
)
cucsIqnpoolTransportBlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolTransportBlockFrom.setStatus("current")
_CucsIqnpoolTransportBlockSuffix_Type = SnmpAdminString
_CucsIqnpoolTransportBlockSuffix_Object = MibTableColumn
cucsIqnpoolTransportBlockSuffix = _CucsIqnpoolTransportBlockSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 8, 1, 5),
    _CucsIqnpoolTransportBlockSuffix_Type()
)
cucsIqnpoolTransportBlockSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolTransportBlockSuffix.setStatus("current")
_CucsIqnpoolTransportBlockTo_Type = CucsIqnpoolTransportBlockTo
_CucsIqnpoolTransportBlockTo_Object = MibTableColumn
cucsIqnpoolTransportBlockTo = _CucsIqnpoolTransportBlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 59, 8, 1, 6),
    _CucsIqnpoolTransportBlockTo_Type()
)
cucsIqnpoolTransportBlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIqnpoolTransportBlockTo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-IQNPOOL-MIB",
    **{"cucsIqnpoolObjects": cucsIqnpoolObjects,
       "cucsIqnpoolAddrTable": cucsIqnpoolAddrTable,
       "cucsIqnpoolAddrEntry": cucsIqnpoolAddrEntry,
       "cucsIqnpoolAddrInstanceId": cucsIqnpoolAddrInstanceId,
       "cucsIqnpoolAddrDn": cucsIqnpoolAddrDn,
       "cucsIqnpoolAddrRn": cucsIqnpoolAddrRn,
       "cucsIqnpoolAddrAssigned": cucsIqnpoolAddrAssigned,
       "cucsIqnpoolAddrAssignedToDn": cucsIqnpoolAddrAssignedToDn,
       "cucsIqnpoolAddrName": cucsIqnpoolAddrName,
       "cucsIqnpoolAddrOwner": cucsIqnpoolAddrOwner,
       "cucsIqnpoolAddrGlobalAssignedCnt": cucsIqnpoolAddrGlobalAssignedCnt,
       "cucsIqnpoolAddrGlobalDefinedCnt": cucsIqnpoolAddrGlobalDefinedCnt,
       "cucsIqnpoolBlockTable": cucsIqnpoolBlockTable,
       "cucsIqnpoolBlockEntry": cucsIqnpoolBlockEntry,
       "cucsIqnpoolBlockInstanceId": cucsIqnpoolBlockInstanceId,
       "cucsIqnpoolBlockDn": cucsIqnpoolBlockDn,
       "cucsIqnpoolBlockRn": cucsIqnpoolBlockRn,
       "cucsIqnpoolBlockFrom": cucsIqnpoolBlockFrom,
       "cucsIqnpoolBlockSuffix": cucsIqnpoolBlockSuffix,
       "cucsIqnpoolBlockTo": cucsIqnpoolBlockTo,
       "cucsIqnpoolFormatTable": cucsIqnpoolFormatTable,
       "cucsIqnpoolFormatEntry": cucsIqnpoolFormatEntry,
       "cucsIqnpoolFormatInstanceId": cucsIqnpoolFormatInstanceId,
       "cucsIqnpoolFormatDn": cucsIqnpoolFormatDn,
       "cucsIqnpoolFormatRn": cucsIqnpoolFormatRn,
       "cucsIqnpoolFormatFormat": cucsIqnpoolFormatFormat,
       "cucsIqnpoolPoolTable": cucsIqnpoolPoolTable,
       "cucsIqnpoolPoolEntry": cucsIqnpoolPoolEntry,
       "cucsIqnpoolPoolInstanceId": cucsIqnpoolPoolInstanceId,
       "cucsIqnpoolPoolDn": cucsIqnpoolPoolDn,
       "cucsIqnpoolPoolRn": cucsIqnpoolPoolRn,
       "cucsIqnpoolPoolAssigned": cucsIqnpoolPoolAssigned,
       "cucsIqnpoolPoolDescr": cucsIqnpoolPoolDescr,
       "cucsIqnpoolPoolIntId": cucsIqnpoolPoolIntId,
       "cucsIqnpoolPoolName": cucsIqnpoolPoolName,
       "cucsIqnpoolPoolPrefix": cucsIqnpoolPoolPrefix,
       "cucsIqnpoolPoolSize": cucsIqnpoolPoolSize,
       "cucsIqnpoolPoolAssignmentOrder": cucsIqnpoolPoolAssignmentOrder,
       "cucsIqnpoolPoolPolicyLevel": cucsIqnpoolPoolPolicyLevel,
       "cucsIqnpoolPoolPolicyOwner": cucsIqnpoolPoolPolicyOwner,
       "cucsIqnpoolPoolableTable": cucsIqnpoolPoolableTable,
       "cucsIqnpoolPoolableEntry": cucsIqnpoolPoolableEntry,
       "cucsIqnpoolPoolableInstanceId": cucsIqnpoolPoolableInstanceId,
       "cucsIqnpoolPoolableDn": cucsIqnpoolPoolableDn,
       "cucsIqnpoolPoolableRn": cucsIqnpoolPoolableRn,
       "cucsIqnpoolPoolableId": cucsIqnpoolPoolableId,
       "cucsIqnpoolPoolablePoolDn": cucsIqnpoolPoolablePoolDn,
       "cucsIqnpoolPooledTable": cucsIqnpoolPooledTable,
       "cucsIqnpoolPooledEntry": cucsIqnpoolPooledEntry,
       "cucsIqnpoolPooledInstanceId": cucsIqnpoolPooledInstanceId,
       "cucsIqnpoolPooledDn": cucsIqnpoolPooledDn,
       "cucsIqnpoolPooledRn": cucsIqnpoolPooledRn,
       "cucsIqnpoolPooledAssigned": cucsIqnpoolPooledAssigned,
       "cucsIqnpoolPooledAssignedToDn": cucsIqnpoolPooledAssignedToDn,
       "cucsIqnpoolPooledName": cucsIqnpoolPooledName,
       "cucsIqnpoolPooledPoolableDn": cucsIqnpoolPooledPoolableDn,
       "cucsIqnpoolPooledPrevAssignedToDn": cucsIqnpoolPooledPrevAssignedToDn,
       "cucsIqnpoolUniverseTable": cucsIqnpoolUniverseTable,
       "cucsIqnpoolUniverseEntry": cucsIqnpoolUniverseEntry,
       "cucsIqnpoolUniverseInstanceId": cucsIqnpoolUniverseInstanceId,
       "cucsIqnpoolUniverseDn": cucsIqnpoolUniverseDn,
       "cucsIqnpoolUniverseRn": cucsIqnpoolUniverseRn,
       "cucsIqnpoolTransportBlockTable": cucsIqnpoolTransportBlockTable,
       "cucsIqnpoolTransportBlockEntry": cucsIqnpoolTransportBlockEntry,
       "cucsIqnpoolTransportBlockInstanceId": cucsIqnpoolTransportBlockInstanceId,
       "cucsIqnpoolTransportBlockDn": cucsIqnpoolTransportBlockDn,
       "cucsIqnpoolTransportBlockRn": cucsIqnpoolTransportBlockRn,
       "cucsIqnpoolTransportBlockFrom": cucsIqnpoolTransportBlockFrom,
       "cucsIqnpoolTransportBlockSuffix": cucsIqnpoolTransportBlockSuffix,
       "cucsIqnpoolTransportBlockTo": cucsIqnpoolTransportBlockTo}
)
