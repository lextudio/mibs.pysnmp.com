# SNMP MIB module (CISCO-UNIFIED-COMPUTING-MACPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-MACPOOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:55 2024
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

(CucsAddressMACMask,
 CucsMacpoolPoolAssignmentOrder,
 CucsPolicyPolicyOwner,
 CucsPoolElementOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsAddressMACMask",
    "CucsMacpoolPoolAssignmentOrder",
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

cucsMacpoolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsMacpoolAddrTable_Object = MibTable
cucsMacpoolAddrTable = _CucsMacpoolAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 1)
)
if mibBuilder.loadTexts:
    cucsMacpoolAddrTable.setStatus("current")
_CucsMacpoolAddrEntry_Object = MibTableRow
cucsMacpoolAddrEntry = _CucsMacpoolAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 1, 1)
)
cucsMacpoolAddrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MACPOOL-MIB", "cucsMacpoolAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMacpoolAddrEntry.setStatus("current")
_CucsMacpoolAddrInstanceId_Type = CucsManagedObjectId
_CucsMacpoolAddrInstanceId_Object = MibTableColumn
cucsMacpoolAddrInstanceId = _CucsMacpoolAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 1, 1, 1),
    _CucsMacpoolAddrInstanceId_Type()
)
cucsMacpoolAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMacpoolAddrInstanceId.setStatus("current")
_CucsMacpoolAddrDn_Type = CucsManagedObjectDn
_CucsMacpoolAddrDn_Object = MibTableColumn
cucsMacpoolAddrDn = _CucsMacpoolAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 1, 1, 2),
    _CucsMacpoolAddrDn_Type()
)
cucsMacpoolAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolAddrDn.setStatus("current")
_CucsMacpoolAddrRn_Type = SnmpAdminString
_CucsMacpoolAddrRn_Object = MibTableColumn
cucsMacpoolAddrRn = _CucsMacpoolAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 1, 1, 3),
    _CucsMacpoolAddrRn_Type()
)
cucsMacpoolAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolAddrRn.setStatus("current")
_CucsMacpoolAddrAssigned_Type = TruthValue
_CucsMacpoolAddrAssigned_Object = MibTableColumn
cucsMacpoolAddrAssigned = _CucsMacpoolAddrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 1, 1, 4),
    _CucsMacpoolAddrAssigned_Type()
)
cucsMacpoolAddrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolAddrAssigned.setStatus("current")
_CucsMacpoolAddrAssignedToDn_Type = SnmpAdminString
_CucsMacpoolAddrAssignedToDn_Object = MibTableColumn
cucsMacpoolAddrAssignedToDn = _CucsMacpoolAddrAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 1, 1, 5),
    _CucsMacpoolAddrAssignedToDn_Type()
)
cucsMacpoolAddrAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolAddrAssignedToDn.setStatus("current")
_CucsMacpoolAddrId_Type = MacAddress
_CucsMacpoolAddrId_Object = MibTableColumn
cucsMacpoolAddrId = _CucsMacpoolAddrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 1, 1, 6),
    _CucsMacpoolAddrId_Type()
)
cucsMacpoolAddrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolAddrId.setStatus("current")
_CucsMacpoolAddrOwner_Type = CucsPoolElementOwner
_CucsMacpoolAddrOwner_Object = MibTableColumn
cucsMacpoolAddrOwner = _CucsMacpoolAddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 1, 1, 7),
    _CucsMacpoolAddrOwner_Type()
)
cucsMacpoolAddrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolAddrOwner.setStatus("current")
_CucsMacpoolAddrGlobalAssignedCnt_Type = Gauge32
_CucsMacpoolAddrGlobalAssignedCnt_Object = MibTableColumn
cucsMacpoolAddrGlobalAssignedCnt = _CucsMacpoolAddrGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 1, 1, 8),
    _CucsMacpoolAddrGlobalAssignedCnt_Type()
)
cucsMacpoolAddrGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolAddrGlobalAssignedCnt.setStatus("current")
_CucsMacpoolAddrGlobalDefinedCnt_Type = Gauge32
_CucsMacpoolAddrGlobalDefinedCnt_Object = MibTableColumn
cucsMacpoolAddrGlobalDefinedCnt = _CucsMacpoolAddrGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 1, 1, 9),
    _CucsMacpoolAddrGlobalDefinedCnt_Type()
)
cucsMacpoolAddrGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolAddrGlobalDefinedCnt.setStatus("current")
_CucsMacpoolBlockTable_Object = MibTable
cucsMacpoolBlockTable = _CucsMacpoolBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 2)
)
if mibBuilder.loadTexts:
    cucsMacpoolBlockTable.setStatus("current")
_CucsMacpoolBlockEntry_Object = MibTableRow
cucsMacpoolBlockEntry = _CucsMacpoolBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 2, 1)
)
cucsMacpoolBlockEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MACPOOL-MIB", "cucsMacpoolBlockInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMacpoolBlockEntry.setStatus("current")
_CucsMacpoolBlockInstanceId_Type = CucsManagedObjectId
_CucsMacpoolBlockInstanceId_Object = MibTableColumn
cucsMacpoolBlockInstanceId = _CucsMacpoolBlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 2, 1, 1),
    _CucsMacpoolBlockInstanceId_Type()
)
cucsMacpoolBlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMacpoolBlockInstanceId.setStatus("current")
_CucsMacpoolBlockDn_Type = CucsManagedObjectDn
_CucsMacpoolBlockDn_Object = MibTableColumn
cucsMacpoolBlockDn = _CucsMacpoolBlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 2, 1, 2),
    _CucsMacpoolBlockDn_Type()
)
cucsMacpoolBlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolBlockDn.setStatus("current")
_CucsMacpoolBlockRn_Type = SnmpAdminString
_CucsMacpoolBlockRn_Object = MibTableColumn
cucsMacpoolBlockRn = _CucsMacpoolBlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 2, 1, 3),
    _CucsMacpoolBlockRn_Type()
)
cucsMacpoolBlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolBlockRn.setStatus("current")
_CucsMacpoolBlockFrom_Type = MacAddress
_CucsMacpoolBlockFrom_Object = MibTableColumn
cucsMacpoolBlockFrom = _CucsMacpoolBlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 2, 1, 4),
    _CucsMacpoolBlockFrom_Type()
)
cucsMacpoolBlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolBlockFrom.setStatus("current")
_CucsMacpoolBlockTo_Type = MacAddress
_CucsMacpoolBlockTo_Object = MibTableColumn
cucsMacpoolBlockTo = _CucsMacpoolBlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 2, 1, 5),
    _CucsMacpoolBlockTo_Type()
)
cucsMacpoolBlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolBlockTo.setStatus("current")
_CucsMacpoolFormatTable_Object = MibTable
cucsMacpoolFormatTable = _CucsMacpoolFormatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 3)
)
if mibBuilder.loadTexts:
    cucsMacpoolFormatTable.setStatus("current")
_CucsMacpoolFormatEntry_Object = MibTableRow
cucsMacpoolFormatEntry = _CucsMacpoolFormatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 3, 1)
)
cucsMacpoolFormatEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MACPOOL-MIB", "cucsMacpoolFormatInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMacpoolFormatEntry.setStatus("current")
_CucsMacpoolFormatInstanceId_Type = CucsManagedObjectId
_CucsMacpoolFormatInstanceId_Object = MibTableColumn
cucsMacpoolFormatInstanceId = _CucsMacpoolFormatInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 3, 1, 1),
    _CucsMacpoolFormatInstanceId_Type()
)
cucsMacpoolFormatInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMacpoolFormatInstanceId.setStatus("current")
_CucsMacpoolFormatDn_Type = CucsManagedObjectDn
_CucsMacpoolFormatDn_Object = MibTableColumn
cucsMacpoolFormatDn = _CucsMacpoolFormatDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 3, 1, 2),
    _CucsMacpoolFormatDn_Type()
)
cucsMacpoolFormatDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolFormatDn.setStatus("current")
_CucsMacpoolFormatRn_Type = SnmpAdminString
_CucsMacpoolFormatRn_Object = MibTableColumn
cucsMacpoolFormatRn = _CucsMacpoolFormatRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 3, 1, 3),
    _CucsMacpoolFormatRn_Type()
)
cucsMacpoolFormatRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolFormatRn.setStatus("current")
_CucsMacpoolFormatFormat_Type = MacAddress
_CucsMacpoolFormatFormat_Object = MibTableColumn
cucsMacpoolFormatFormat = _CucsMacpoolFormatFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 3, 1, 4),
    _CucsMacpoolFormatFormat_Type()
)
cucsMacpoolFormatFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolFormatFormat.setStatus("current")
_CucsMacpoolFormatMask_Type = CucsAddressMACMask
_CucsMacpoolFormatMask_Object = MibTableColumn
cucsMacpoolFormatMask = _CucsMacpoolFormatMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 3, 1, 5),
    _CucsMacpoolFormatMask_Type()
)
cucsMacpoolFormatMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolFormatMask.setStatus("current")
_CucsMacpoolPoolTable_Object = MibTable
cucsMacpoolPoolTable = _CucsMacpoolPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 4)
)
if mibBuilder.loadTexts:
    cucsMacpoolPoolTable.setStatus("current")
_CucsMacpoolPoolEntry_Object = MibTableRow
cucsMacpoolPoolEntry = _CucsMacpoolPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 4, 1)
)
cucsMacpoolPoolEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MACPOOL-MIB", "cucsMacpoolPoolInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMacpoolPoolEntry.setStatus("current")
_CucsMacpoolPoolInstanceId_Type = CucsManagedObjectId
_CucsMacpoolPoolInstanceId_Object = MibTableColumn
cucsMacpoolPoolInstanceId = _CucsMacpoolPoolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 4, 1, 1),
    _CucsMacpoolPoolInstanceId_Type()
)
cucsMacpoolPoolInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMacpoolPoolInstanceId.setStatus("current")
_CucsMacpoolPoolDn_Type = CucsManagedObjectDn
_CucsMacpoolPoolDn_Object = MibTableColumn
cucsMacpoolPoolDn = _CucsMacpoolPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 4, 1, 2),
    _CucsMacpoolPoolDn_Type()
)
cucsMacpoolPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPoolDn.setStatus("current")
_CucsMacpoolPoolRn_Type = SnmpAdminString
_CucsMacpoolPoolRn_Object = MibTableColumn
cucsMacpoolPoolRn = _CucsMacpoolPoolRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 4, 1, 3),
    _CucsMacpoolPoolRn_Type()
)
cucsMacpoolPoolRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPoolRn.setStatus("current")
_CucsMacpoolPoolAssigned_Type = Gauge32
_CucsMacpoolPoolAssigned_Object = MibTableColumn
cucsMacpoolPoolAssigned = _CucsMacpoolPoolAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 4, 1, 4),
    _CucsMacpoolPoolAssigned_Type()
)
cucsMacpoolPoolAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPoolAssigned.setStatus("current")
_CucsMacpoolPoolDescr_Type = SnmpAdminString
_CucsMacpoolPoolDescr_Object = MibTableColumn
cucsMacpoolPoolDescr = _CucsMacpoolPoolDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 4, 1, 5),
    _CucsMacpoolPoolDescr_Type()
)
cucsMacpoolPoolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPoolDescr.setStatus("current")
_CucsMacpoolPoolIntId_Type = SnmpAdminString
_CucsMacpoolPoolIntId_Object = MibTableColumn
cucsMacpoolPoolIntId = _CucsMacpoolPoolIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 4, 1, 6),
    _CucsMacpoolPoolIntId_Type()
)
cucsMacpoolPoolIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPoolIntId.setStatus("current")
_CucsMacpoolPoolName_Type = SnmpAdminString
_CucsMacpoolPoolName_Object = MibTableColumn
cucsMacpoolPoolName = _CucsMacpoolPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 4, 1, 7),
    _CucsMacpoolPoolName_Type()
)
cucsMacpoolPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPoolName.setStatus("current")
_CucsMacpoolPoolSize_Type = Gauge32
_CucsMacpoolPoolSize_Object = MibTableColumn
cucsMacpoolPoolSize = _CucsMacpoolPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 4, 1, 8),
    _CucsMacpoolPoolSize_Type()
)
cucsMacpoolPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPoolSize.setStatus("current")
_CucsMacpoolPoolAssignmentOrder_Type = CucsMacpoolPoolAssignmentOrder
_CucsMacpoolPoolAssignmentOrder_Object = MibTableColumn
cucsMacpoolPoolAssignmentOrder = _CucsMacpoolPoolAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 4, 1, 9),
    _CucsMacpoolPoolAssignmentOrder_Type()
)
cucsMacpoolPoolAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPoolAssignmentOrder.setStatus("current")
_CucsMacpoolPoolPolicyLevel_Type = Gauge32
_CucsMacpoolPoolPolicyLevel_Object = MibTableColumn
cucsMacpoolPoolPolicyLevel = _CucsMacpoolPoolPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 4, 1, 10),
    _CucsMacpoolPoolPolicyLevel_Type()
)
cucsMacpoolPoolPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPoolPolicyLevel.setStatus("current")
_CucsMacpoolPoolPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsMacpoolPoolPolicyOwner_Object = MibTableColumn
cucsMacpoolPoolPolicyOwner = _CucsMacpoolPoolPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 4, 1, 11),
    _CucsMacpoolPoolPolicyOwner_Type()
)
cucsMacpoolPoolPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPoolPolicyOwner.setStatus("current")
_CucsMacpoolPoolableTable_Object = MibTable
cucsMacpoolPoolableTable = _CucsMacpoolPoolableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 5)
)
if mibBuilder.loadTexts:
    cucsMacpoolPoolableTable.setStatus("current")
_CucsMacpoolPoolableEntry_Object = MibTableRow
cucsMacpoolPoolableEntry = _CucsMacpoolPoolableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 5, 1)
)
cucsMacpoolPoolableEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MACPOOL-MIB", "cucsMacpoolPoolableInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMacpoolPoolableEntry.setStatus("current")
_CucsMacpoolPoolableInstanceId_Type = CucsManagedObjectId
_CucsMacpoolPoolableInstanceId_Object = MibTableColumn
cucsMacpoolPoolableInstanceId = _CucsMacpoolPoolableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 5, 1, 1),
    _CucsMacpoolPoolableInstanceId_Type()
)
cucsMacpoolPoolableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMacpoolPoolableInstanceId.setStatus("current")
_CucsMacpoolPoolableDn_Type = CucsManagedObjectDn
_CucsMacpoolPoolableDn_Object = MibTableColumn
cucsMacpoolPoolableDn = _CucsMacpoolPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 5, 1, 2),
    _CucsMacpoolPoolableDn_Type()
)
cucsMacpoolPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPoolableDn.setStatus("current")
_CucsMacpoolPoolableRn_Type = SnmpAdminString
_CucsMacpoolPoolableRn_Object = MibTableColumn
cucsMacpoolPoolableRn = _CucsMacpoolPoolableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 5, 1, 3),
    _CucsMacpoolPoolableRn_Type()
)
cucsMacpoolPoolableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPoolableRn.setStatus("current")
_CucsMacpoolPoolableId_Type = Unsigned64
_CucsMacpoolPoolableId_Object = MibTableColumn
cucsMacpoolPoolableId = _CucsMacpoolPoolableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 5, 1, 4),
    _CucsMacpoolPoolableId_Type()
)
cucsMacpoolPoolableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPoolableId.setStatus("current")
_CucsMacpoolPoolablePoolDn_Type = SnmpAdminString
_CucsMacpoolPoolablePoolDn_Object = MibTableColumn
cucsMacpoolPoolablePoolDn = _CucsMacpoolPoolablePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 5, 1, 5),
    _CucsMacpoolPoolablePoolDn_Type()
)
cucsMacpoolPoolablePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPoolablePoolDn.setStatus("current")
_CucsMacpoolPooledTable_Object = MibTable
cucsMacpoolPooledTable = _CucsMacpoolPooledTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 6)
)
if mibBuilder.loadTexts:
    cucsMacpoolPooledTable.setStatus("current")
_CucsMacpoolPooledEntry_Object = MibTableRow
cucsMacpoolPooledEntry = _CucsMacpoolPooledEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 6, 1)
)
cucsMacpoolPooledEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MACPOOL-MIB", "cucsMacpoolPooledInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMacpoolPooledEntry.setStatus("current")
_CucsMacpoolPooledInstanceId_Type = CucsManagedObjectId
_CucsMacpoolPooledInstanceId_Object = MibTableColumn
cucsMacpoolPooledInstanceId = _CucsMacpoolPooledInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 6, 1, 1),
    _CucsMacpoolPooledInstanceId_Type()
)
cucsMacpoolPooledInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMacpoolPooledInstanceId.setStatus("current")
_CucsMacpoolPooledDn_Type = CucsManagedObjectDn
_CucsMacpoolPooledDn_Object = MibTableColumn
cucsMacpoolPooledDn = _CucsMacpoolPooledDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 6, 1, 2),
    _CucsMacpoolPooledDn_Type()
)
cucsMacpoolPooledDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPooledDn.setStatus("current")
_CucsMacpoolPooledRn_Type = SnmpAdminString
_CucsMacpoolPooledRn_Object = MibTableColumn
cucsMacpoolPooledRn = _CucsMacpoolPooledRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 6, 1, 3),
    _CucsMacpoolPooledRn_Type()
)
cucsMacpoolPooledRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPooledRn.setStatus("current")
_CucsMacpoolPooledAssigned_Type = TruthValue
_CucsMacpoolPooledAssigned_Object = MibTableColumn
cucsMacpoolPooledAssigned = _CucsMacpoolPooledAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 6, 1, 4),
    _CucsMacpoolPooledAssigned_Type()
)
cucsMacpoolPooledAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPooledAssigned.setStatus("current")
_CucsMacpoolPooledAssignedToDn_Type = SnmpAdminString
_CucsMacpoolPooledAssignedToDn_Object = MibTableColumn
cucsMacpoolPooledAssignedToDn = _CucsMacpoolPooledAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 6, 1, 5),
    _CucsMacpoolPooledAssignedToDn_Type()
)
cucsMacpoolPooledAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPooledAssignedToDn.setStatus("current")
_CucsMacpoolPooledId_Type = MacAddress
_CucsMacpoolPooledId_Object = MibTableColumn
cucsMacpoolPooledId = _CucsMacpoolPooledId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 6, 1, 6),
    _CucsMacpoolPooledId_Type()
)
cucsMacpoolPooledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPooledId.setStatus("current")
_CucsMacpoolPooledPoolableDn_Type = SnmpAdminString
_CucsMacpoolPooledPoolableDn_Object = MibTableColumn
cucsMacpoolPooledPoolableDn = _CucsMacpoolPooledPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 6, 1, 7),
    _CucsMacpoolPooledPoolableDn_Type()
)
cucsMacpoolPooledPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPooledPoolableDn.setStatus("current")
_CucsMacpoolPooledPrevAssignedToDn_Type = SnmpAdminString
_CucsMacpoolPooledPrevAssignedToDn_Object = MibTableColumn
cucsMacpoolPooledPrevAssignedToDn = _CucsMacpoolPooledPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 6, 1, 8),
    _CucsMacpoolPooledPrevAssignedToDn_Type()
)
cucsMacpoolPooledPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolPooledPrevAssignedToDn.setStatus("current")
_CucsMacpoolUniverseTable_Object = MibTable
cucsMacpoolUniverseTable = _CucsMacpoolUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 7)
)
if mibBuilder.loadTexts:
    cucsMacpoolUniverseTable.setStatus("current")
_CucsMacpoolUniverseEntry_Object = MibTableRow
cucsMacpoolUniverseEntry = _CucsMacpoolUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 7, 1)
)
cucsMacpoolUniverseEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MACPOOL-MIB", "cucsMacpoolUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMacpoolUniverseEntry.setStatus("current")
_CucsMacpoolUniverseInstanceId_Type = CucsManagedObjectId
_CucsMacpoolUniverseInstanceId_Object = MibTableColumn
cucsMacpoolUniverseInstanceId = _CucsMacpoolUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 7, 1, 1),
    _CucsMacpoolUniverseInstanceId_Type()
)
cucsMacpoolUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMacpoolUniverseInstanceId.setStatus("current")
_CucsMacpoolUniverseDn_Type = CucsManagedObjectDn
_CucsMacpoolUniverseDn_Object = MibTableColumn
cucsMacpoolUniverseDn = _CucsMacpoolUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 7, 1, 2),
    _CucsMacpoolUniverseDn_Type()
)
cucsMacpoolUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolUniverseDn.setStatus("current")
_CucsMacpoolUniverseRn_Type = SnmpAdminString
_CucsMacpoolUniverseRn_Object = MibTableColumn
cucsMacpoolUniverseRn = _CucsMacpoolUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 29, 7, 1, 3),
    _CucsMacpoolUniverseRn_Type()
)
cucsMacpoolUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMacpoolUniverseRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-MACPOOL-MIB",
    **{"cucsMacpoolObjects": cucsMacpoolObjects,
       "cucsMacpoolAddrTable": cucsMacpoolAddrTable,
       "cucsMacpoolAddrEntry": cucsMacpoolAddrEntry,
       "cucsMacpoolAddrInstanceId": cucsMacpoolAddrInstanceId,
       "cucsMacpoolAddrDn": cucsMacpoolAddrDn,
       "cucsMacpoolAddrRn": cucsMacpoolAddrRn,
       "cucsMacpoolAddrAssigned": cucsMacpoolAddrAssigned,
       "cucsMacpoolAddrAssignedToDn": cucsMacpoolAddrAssignedToDn,
       "cucsMacpoolAddrId": cucsMacpoolAddrId,
       "cucsMacpoolAddrOwner": cucsMacpoolAddrOwner,
       "cucsMacpoolAddrGlobalAssignedCnt": cucsMacpoolAddrGlobalAssignedCnt,
       "cucsMacpoolAddrGlobalDefinedCnt": cucsMacpoolAddrGlobalDefinedCnt,
       "cucsMacpoolBlockTable": cucsMacpoolBlockTable,
       "cucsMacpoolBlockEntry": cucsMacpoolBlockEntry,
       "cucsMacpoolBlockInstanceId": cucsMacpoolBlockInstanceId,
       "cucsMacpoolBlockDn": cucsMacpoolBlockDn,
       "cucsMacpoolBlockRn": cucsMacpoolBlockRn,
       "cucsMacpoolBlockFrom": cucsMacpoolBlockFrom,
       "cucsMacpoolBlockTo": cucsMacpoolBlockTo,
       "cucsMacpoolFormatTable": cucsMacpoolFormatTable,
       "cucsMacpoolFormatEntry": cucsMacpoolFormatEntry,
       "cucsMacpoolFormatInstanceId": cucsMacpoolFormatInstanceId,
       "cucsMacpoolFormatDn": cucsMacpoolFormatDn,
       "cucsMacpoolFormatRn": cucsMacpoolFormatRn,
       "cucsMacpoolFormatFormat": cucsMacpoolFormatFormat,
       "cucsMacpoolFormatMask": cucsMacpoolFormatMask,
       "cucsMacpoolPoolTable": cucsMacpoolPoolTable,
       "cucsMacpoolPoolEntry": cucsMacpoolPoolEntry,
       "cucsMacpoolPoolInstanceId": cucsMacpoolPoolInstanceId,
       "cucsMacpoolPoolDn": cucsMacpoolPoolDn,
       "cucsMacpoolPoolRn": cucsMacpoolPoolRn,
       "cucsMacpoolPoolAssigned": cucsMacpoolPoolAssigned,
       "cucsMacpoolPoolDescr": cucsMacpoolPoolDescr,
       "cucsMacpoolPoolIntId": cucsMacpoolPoolIntId,
       "cucsMacpoolPoolName": cucsMacpoolPoolName,
       "cucsMacpoolPoolSize": cucsMacpoolPoolSize,
       "cucsMacpoolPoolAssignmentOrder": cucsMacpoolPoolAssignmentOrder,
       "cucsMacpoolPoolPolicyLevel": cucsMacpoolPoolPolicyLevel,
       "cucsMacpoolPoolPolicyOwner": cucsMacpoolPoolPolicyOwner,
       "cucsMacpoolPoolableTable": cucsMacpoolPoolableTable,
       "cucsMacpoolPoolableEntry": cucsMacpoolPoolableEntry,
       "cucsMacpoolPoolableInstanceId": cucsMacpoolPoolableInstanceId,
       "cucsMacpoolPoolableDn": cucsMacpoolPoolableDn,
       "cucsMacpoolPoolableRn": cucsMacpoolPoolableRn,
       "cucsMacpoolPoolableId": cucsMacpoolPoolableId,
       "cucsMacpoolPoolablePoolDn": cucsMacpoolPoolablePoolDn,
       "cucsMacpoolPooledTable": cucsMacpoolPooledTable,
       "cucsMacpoolPooledEntry": cucsMacpoolPooledEntry,
       "cucsMacpoolPooledInstanceId": cucsMacpoolPooledInstanceId,
       "cucsMacpoolPooledDn": cucsMacpoolPooledDn,
       "cucsMacpoolPooledRn": cucsMacpoolPooledRn,
       "cucsMacpoolPooledAssigned": cucsMacpoolPooledAssigned,
       "cucsMacpoolPooledAssignedToDn": cucsMacpoolPooledAssignedToDn,
       "cucsMacpoolPooledId": cucsMacpoolPooledId,
       "cucsMacpoolPooledPoolableDn": cucsMacpoolPooledPoolableDn,
       "cucsMacpoolPooledPrevAssignedToDn": cucsMacpoolPooledPrevAssignedToDn,
       "cucsMacpoolUniverseTable": cucsMacpoolUniverseTable,
       "cucsMacpoolUniverseEntry": cucsMacpoolUniverseEntry,
       "cucsMacpoolUniverseInstanceId": cucsMacpoolUniverseInstanceId,
       "cucsMacpoolUniverseDn": cucsMacpoolUniverseDn,
       "cucsMacpoolUniverseRn": cucsMacpoolUniverseRn}
)
