# SNMP MIB module (CISCO-UNIFIED-COMPUTING-IPPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-IPPOOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:45 2024
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

(CucsIppoolDHCPMode,
 CucsIppoolManagementMode,
 CucsIppoolNetBIOSMode,
 CucsIppoolPoolAssignmentOrder,
 CucsPolicyPolicyOwner,
 CucsPoolElementOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsIppoolDHCPMode",
    "CucsIppoolManagementMode",
    "CucsIppoolNetBIOSMode",
    "CucsIppoolPoolAssignmentOrder",
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

cucsIppoolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsIppoolAddrTable_Object = MibTable
cucsIppoolAddrTable = _CucsIppoolAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 1)
)
if mibBuilder.loadTexts:
    cucsIppoolAddrTable.setStatus("current")
_CucsIppoolAddrEntry_Object = MibTableRow
cucsIppoolAddrEntry = _CucsIppoolAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 1, 1)
)
cucsIppoolAddrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IPPOOL-MIB", "cucsIppoolAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIppoolAddrEntry.setStatus("current")
_CucsIppoolAddrInstanceId_Type = CucsManagedObjectId
_CucsIppoolAddrInstanceId_Object = MibTableColumn
cucsIppoolAddrInstanceId = _CucsIppoolAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 1, 1, 1),
    _CucsIppoolAddrInstanceId_Type()
)
cucsIppoolAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIppoolAddrInstanceId.setStatus("current")
_CucsIppoolAddrDn_Type = CucsManagedObjectDn
_CucsIppoolAddrDn_Object = MibTableColumn
cucsIppoolAddrDn = _CucsIppoolAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 1, 1, 2),
    _CucsIppoolAddrDn_Type()
)
cucsIppoolAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolAddrDn.setStatus("current")
_CucsIppoolAddrRn_Type = SnmpAdminString
_CucsIppoolAddrRn_Object = MibTableColumn
cucsIppoolAddrRn = _CucsIppoolAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 1, 1, 3),
    _CucsIppoolAddrRn_Type()
)
cucsIppoolAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolAddrRn.setStatus("current")
_CucsIppoolAddrAssigned_Type = TruthValue
_CucsIppoolAddrAssigned_Object = MibTableColumn
cucsIppoolAddrAssigned = _CucsIppoolAddrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 1, 1, 4),
    _CucsIppoolAddrAssigned_Type()
)
cucsIppoolAddrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolAddrAssigned.setStatus("current")
_CucsIppoolAddrAssignedToDn_Type = SnmpAdminString
_CucsIppoolAddrAssignedToDn_Object = MibTableColumn
cucsIppoolAddrAssignedToDn = _CucsIppoolAddrAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 1, 1, 5),
    _CucsIppoolAddrAssignedToDn_Type()
)
cucsIppoolAddrAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolAddrAssignedToDn.setStatus("current")
_CucsIppoolAddrId_Type = InetAddressIPv4
_CucsIppoolAddrId_Object = MibTableColumn
cucsIppoolAddrId = _CucsIppoolAddrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 1, 1, 6),
    _CucsIppoolAddrId_Type()
)
cucsIppoolAddrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolAddrId.setStatus("current")
_CucsIppoolAddrOwner_Type = CucsPoolElementOwner
_CucsIppoolAddrOwner_Object = MibTableColumn
cucsIppoolAddrOwner = _CucsIppoolAddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 1, 1, 7),
    _CucsIppoolAddrOwner_Type()
)
cucsIppoolAddrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolAddrOwner.setStatus("current")
_CucsIppoolAddrGlobalAssignedCnt_Type = Gauge32
_CucsIppoolAddrGlobalAssignedCnt_Object = MibTableColumn
cucsIppoolAddrGlobalAssignedCnt = _CucsIppoolAddrGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 1, 1, 8),
    _CucsIppoolAddrGlobalAssignedCnt_Type()
)
cucsIppoolAddrGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolAddrGlobalAssignedCnt.setStatus("current")
_CucsIppoolAddrGlobalDefinedCnt_Type = Gauge32
_CucsIppoolAddrGlobalDefinedCnt_Object = MibTableColumn
cucsIppoolAddrGlobalDefinedCnt = _CucsIppoolAddrGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 1, 1, 9),
    _CucsIppoolAddrGlobalDefinedCnt_Type()
)
cucsIppoolAddrGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolAddrGlobalDefinedCnt.setStatus("current")
_CucsIppoolBlockTable_Object = MibTable
cucsIppoolBlockTable = _CucsIppoolBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 2)
)
if mibBuilder.loadTexts:
    cucsIppoolBlockTable.setStatus("current")
_CucsIppoolBlockEntry_Object = MibTableRow
cucsIppoolBlockEntry = _CucsIppoolBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 2, 1)
)
cucsIppoolBlockEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IPPOOL-MIB", "cucsIppoolBlockInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIppoolBlockEntry.setStatus("current")
_CucsIppoolBlockInstanceId_Type = CucsManagedObjectId
_CucsIppoolBlockInstanceId_Object = MibTableColumn
cucsIppoolBlockInstanceId = _CucsIppoolBlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 2, 1, 1),
    _CucsIppoolBlockInstanceId_Type()
)
cucsIppoolBlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIppoolBlockInstanceId.setStatus("current")
_CucsIppoolBlockDn_Type = CucsManagedObjectDn
_CucsIppoolBlockDn_Object = MibTableColumn
cucsIppoolBlockDn = _CucsIppoolBlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 2, 1, 2),
    _CucsIppoolBlockDn_Type()
)
cucsIppoolBlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolBlockDn.setStatus("current")
_CucsIppoolBlockRn_Type = SnmpAdminString
_CucsIppoolBlockRn_Object = MibTableColumn
cucsIppoolBlockRn = _CucsIppoolBlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 2, 1, 3),
    _CucsIppoolBlockRn_Type()
)
cucsIppoolBlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolBlockRn.setStatus("current")
_CucsIppoolBlockDefGw_Type = InetAddressIPv4
_CucsIppoolBlockDefGw_Object = MibTableColumn
cucsIppoolBlockDefGw = _CucsIppoolBlockDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 2, 1, 4),
    _CucsIppoolBlockDefGw_Type()
)
cucsIppoolBlockDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolBlockDefGw.setStatus("current")
_CucsIppoolBlockFrom_Type = InetAddressIPv4
_CucsIppoolBlockFrom_Object = MibTableColumn
cucsIppoolBlockFrom = _CucsIppoolBlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 2, 1, 5),
    _CucsIppoolBlockFrom_Type()
)
cucsIppoolBlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolBlockFrom.setStatus("current")
_CucsIppoolBlockSubnet_Type = InetAddressIPv4
_CucsIppoolBlockSubnet_Object = MibTableColumn
cucsIppoolBlockSubnet = _CucsIppoolBlockSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 2, 1, 6),
    _CucsIppoolBlockSubnet_Type()
)
cucsIppoolBlockSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolBlockSubnet.setStatus("current")
_CucsIppoolBlockTo_Type = InetAddressIPv4
_CucsIppoolBlockTo_Object = MibTableColumn
cucsIppoolBlockTo = _CucsIppoolBlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 2, 1, 7),
    _CucsIppoolBlockTo_Type()
)
cucsIppoolBlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolBlockTo.setStatus("current")
_CucsIppoolBlockPrimDns_Type = InetAddressIPv4
_CucsIppoolBlockPrimDns_Object = MibTableColumn
cucsIppoolBlockPrimDns = _CucsIppoolBlockPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 2, 1, 8),
    _CucsIppoolBlockPrimDns_Type()
)
cucsIppoolBlockPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolBlockPrimDns.setStatus("current")
_CucsIppoolBlockSecDns_Type = InetAddressIPv4
_CucsIppoolBlockSecDns_Object = MibTableColumn
cucsIppoolBlockSecDns = _CucsIppoolBlockSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 2, 1, 9),
    _CucsIppoolBlockSecDns_Type()
)
cucsIppoolBlockSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolBlockSecDns.setStatus("current")
_CucsIppoolPoolTable_Object = MibTable
cucsIppoolPoolTable = _CucsIppoolPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3)
)
if mibBuilder.loadTexts:
    cucsIppoolPoolTable.setStatus("current")
_CucsIppoolPoolEntry_Object = MibTableRow
cucsIppoolPoolEntry = _CucsIppoolPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1)
)
cucsIppoolPoolEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IPPOOL-MIB", "cucsIppoolPoolInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIppoolPoolEntry.setStatus("current")
_CucsIppoolPoolInstanceId_Type = CucsManagedObjectId
_CucsIppoolPoolInstanceId_Object = MibTableColumn
cucsIppoolPoolInstanceId = _CucsIppoolPoolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 1),
    _CucsIppoolPoolInstanceId_Type()
)
cucsIppoolPoolInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIppoolPoolInstanceId.setStatus("current")
_CucsIppoolPoolDn_Type = CucsManagedObjectDn
_CucsIppoolPoolDn_Object = MibTableColumn
cucsIppoolPoolDn = _CucsIppoolPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 2),
    _CucsIppoolPoolDn_Type()
)
cucsIppoolPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolDn.setStatus("current")
_CucsIppoolPoolRn_Type = SnmpAdminString
_CucsIppoolPoolRn_Object = MibTableColumn
cucsIppoolPoolRn = _CucsIppoolPoolRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 3),
    _CucsIppoolPoolRn_Type()
)
cucsIppoolPoolRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolRn.setStatus("current")
_CucsIppoolPoolAssigned_Type = Gauge32
_CucsIppoolPoolAssigned_Object = MibTableColumn
cucsIppoolPoolAssigned = _CucsIppoolPoolAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 4),
    _CucsIppoolPoolAssigned_Type()
)
cucsIppoolPoolAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolAssigned.setStatus("current")
_CucsIppoolPoolDescr_Type = SnmpAdminString
_CucsIppoolPoolDescr_Object = MibTableColumn
cucsIppoolPoolDescr = _CucsIppoolPoolDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 5),
    _CucsIppoolPoolDescr_Type()
)
cucsIppoolPoolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolDescr.setStatus("current")
_CucsIppoolPoolIntId_Type = SnmpAdminString
_CucsIppoolPoolIntId_Object = MibTableColumn
cucsIppoolPoolIntId = _CucsIppoolPoolIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 6),
    _CucsIppoolPoolIntId_Type()
)
cucsIppoolPoolIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolIntId.setStatus("current")
_CucsIppoolPoolName_Type = SnmpAdminString
_CucsIppoolPoolName_Object = MibTableColumn
cucsIppoolPoolName = _CucsIppoolPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 7),
    _CucsIppoolPoolName_Type()
)
cucsIppoolPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolName.setStatus("current")
_CucsIppoolPoolSize_Type = Gauge32
_CucsIppoolPoolSize_Object = MibTableColumn
cucsIppoolPoolSize = _CucsIppoolPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 8),
    _CucsIppoolPoolSize_Type()
)
cucsIppoolPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolSize.setStatus("current")
_CucsIppoolPoolAssignmentOrder_Type = CucsIppoolPoolAssignmentOrder
_CucsIppoolPoolAssignmentOrder_Object = MibTableColumn
cucsIppoolPoolAssignmentOrder = _CucsIppoolPoolAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 9),
    _CucsIppoolPoolAssignmentOrder_Type()
)
cucsIppoolPoolAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolAssignmentOrder.setStatus("current")
_CucsIppoolPoolPolicyLevel_Type = Gauge32
_CucsIppoolPoolPolicyLevel_Object = MibTableColumn
cucsIppoolPoolPolicyLevel = _CucsIppoolPoolPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 10),
    _CucsIppoolPoolPolicyLevel_Type()
)
cucsIppoolPoolPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolPolicyLevel.setStatus("current")
_CucsIppoolPoolPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsIppoolPoolPolicyOwner_Object = MibTableColumn
cucsIppoolPoolPolicyOwner = _CucsIppoolPoolPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 11),
    _CucsIppoolPoolPolicyOwner_Type()
)
cucsIppoolPoolPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolPolicyOwner.setStatus("current")
_CucsIppoolPoolExtManaged_Type = CucsIppoolManagementMode
_CucsIppoolPoolExtManaged_Object = MibTableColumn
cucsIppoolPoolExtManaged = _CucsIppoolPoolExtManaged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 12),
    _CucsIppoolPoolExtManaged_Type()
)
cucsIppoolPoolExtManaged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolExtManaged.setStatus("current")
_CucsIppoolPoolGuid_Type = SnmpAdminString
_CucsIppoolPoolGuid_Object = MibTableColumn
cucsIppoolPoolGuid = _CucsIppoolPoolGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 13),
    _CucsIppoolPoolGuid_Type()
)
cucsIppoolPoolGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolGuid.setStatus("current")
_CucsIppoolPoolIsNetBIOSEnabled_Type = CucsIppoolNetBIOSMode
_CucsIppoolPoolIsNetBIOSEnabled_Object = MibTableColumn
cucsIppoolPoolIsNetBIOSEnabled = _CucsIppoolPoolIsNetBIOSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 14),
    _CucsIppoolPoolIsNetBIOSEnabled_Type()
)
cucsIppoolPoolIsNetBIOSEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolIsNetBIOSEnabled.setStatus("current")
_CucsIppoolPoolSupportsDHCP_Type = CucsIppoolDHCPMode
_CucsIppoolPoolSupportsDHCP_Object = MibTableColumn
cucsIppoolPoolSupportsDHCP = _CucsIppoolPoolSupportsDHCP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 15),
    _CucsIppoolPoolSupportsDHCP_Type()
)
cucsIppoolPoolSupportsDHCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolSupportsDHCP.setStatus("current")
_CucsIppoolPoolV4Assigned_Type = Gauge32
_CucsIppoolPoolV4Assigned_Object = MibTableColumn
cucsIppoolPoolV4Assigned = _CucsIppoolPoolV4Assigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 16),
    _CucsIppoolPoolV4Assigned_Type()
)
cucsIppoolPoolV4Assigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolV4Assigned.setStatus("current")
_CucsIppoolPoolV4Size_Type = Gauge32
_CucsIppoolPoolV4Size_Object = MibTableColumn
cucsIppoolPoolV4Size = _CucsIppoolPoolV4Size_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 17),
    _CucsIppoolPoolV4Size_Type()
)
cucsIppoolPoolV4Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolV4Size.setStatus("current")
_CucsIppoolPoolV6Assigned_Type = Gauge32
_CucsIppoolPoolV6Assigned_Object = MibTableColumn
cucsIppoolPoolV6Assigned = _CucsIppoolPoolV6Assigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 18),
    _CucsIppoolPoolV6Assigned_Type()
)
cucsIppoolPoolV6Assigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolV6Assigned.setStatus("current")
_CucsIppoolPoolV6Size_Type = Gauge32
_CucsIppoolPoolV6Size_Object = MibTableColumn
cucsIppoolPoolV6Size = _CucsIppoolPoolV6Size_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 19),
    _CucsIppoolPoolV6Size_Type()
)
cucsIppoolPoolV6Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolV6Size.setStatus("current")
_CucsIppoolPoolPropAcl_Type = Unsigned64
_CucsIppoolPoolPropAcl_Object = MibTableColumn
cucsIppoolPoolPropAcl = _CucsIppoolPoolPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 3, 1, 20),
    _CucsIppoolPoolPropAcl_Type()
)
cucsIppoolPoolPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolPropAcl.setStatus("current")
_CucsIppoolPoolableTable_Object = MibTable
cucsIppoolPoolableTable = _CucsIppoolPoolableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 4)
)
if mibBuilder.loadTexts:
    cucsIppoolPoolableTable.setStatus("current")
_CucsIppoolPoolableEntry_Object = MibTableRow
cucsIppoolPoolableEntry = _CucsIppoolPoolableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 4, 1)
)
cucsIppoolPoolableEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IPPOOL-MIB", "cucsIppoolPoolableInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIppoolPoolableEntry.setStatus("current")
_CucsIppoolPoolableInstanceId_Type = CucsManagedObjectId
_CucsIppoolPoolableInstanceId_Object = MibTableColumn
cucsIppoolPoolableInstanceId = _CucsIppoolPoolableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 4, 1, 1),
    _CucsIppoolPoolableInstanceId_Type()
)
cucsIppoolPoolableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIppoolPoolableInstanceId.setStatus("current")
_CucsIppoolPoolableDn_Type = CucsManagedObjectDn
_CucsIppoolPoolableDn_Object = MibTableColumn
cucsIppoolPoolableDn = _CucsIppoolPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 4, 1, 2),
    _CucsIppoolPoolableDn_Type()
)
cucsIppoolPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolableDn.setStatus("current")
_CucsIppoolPoolableRn_Type = SnmpAdminString
_CucsIppoolPoolableRn_Object = MibTableColumn
cucsIppoolPoolableRn = _CucsIppoolPoolableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 4, 1, 3),
    _CucsIppoolPoolableRn_Type()
)
cucsIppoolPoolableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolableRn.setStatus("current")
_CucsIppoolPoolableId_Type = Unsigned64
_CucsIppoolPoolableId_Object = MibTableColumn
cucsIppoolPoolableId = _CucsIppoolPoolableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 4, 1, 4),
    _CucsIppoolPoolableId_Type()
)
cucsIppoolPoolableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolableId.setStatus("current")
_CucsIppoolPoolablePoolDn_Type = SnmpAdminString
_CucsIppoolPoolablePoolDn_Object = MibTableColumn
cucsIppoolPoolablePoolDn = _CucsIppoolPoolablePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 4, 1, 5),
    _CucsIppoolPoolablePoolDn_Type()
)
cucsIppoolPoolablePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPoolablePoolDn.setStatus("current")
_CucsIppoolPooledTable_Object = MibTable
cucsIppoolPooledTable = _CucsIppoolPooledTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 5)
)
if mibBuilder.loadTexts:
    cucsIppoolPooledTable.setStatus("current")
_CucsIppoolPooledEntry_Object = MibTableRow
cucsIppoolPooledEntry = _CucsIppoolPooledEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 5, 1)
)
cucsIppoolPooledEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IPPOOL-MIB", "cucsIppoolPooledInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIppoolPooledEntry.setStatus("current")
_CucsIppoolPooledInstanceId_Type = CucsManagedObjectId
_CucsIppoolPooledInstanceId_Object = MibTableColumn
cucsIppoolPooledInstanceId = _CucsIppoolPooledInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 5, 1, 1),
    _CucsIppoolPooledInstanceId_Type()
)
cucsIppoolPooledInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIppoolPooledInstanceId.setStatus("current")
_CucsIppoolPooledDn_Type = CucsManagedObjectDn
_CucsIppoolPooledDn_Object = MibTableColumn
cucsIppoolPooledDn = _CucsIppoolPooledDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 5, 1, 2),
    _CucsIppoolPooledDn_Type()
)
cucsIppoolPooledDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPooledDn.setStatus("current")
_CucsIppoolPooledRn_Type = SnmpAdminString
_CucsIppoolPooledRn_Object = MibTableColumn
cucsIppoolPooledRn = _CucsIppoolPooledRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 5, 1, 3),
    _CucsIppoolPooledRn_Type()
)
cucsIppoolPooledRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPooledRn.setStatus("current")
_CucsIppoolPooledAssigned_Type = TruthValue
_CucsIppoolPooledAssigned_Object = MibTableColumn
cucsIppoolPooledAssigned = _CucsIppoolPooledAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 5, 1, 4),
    _CucsIppoolPooledAssigned_Type()
)
cucsIppoolPooledAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPooledAssigned.setStatus("current")
_CucsIppoolPooledAssignedToDn_Type = SnmpAdminString
_CucsIppoolPooledAssignedToDn_Object = MibTableColumn
cucsIppoolPooledAssignedToDn = _CucsIppoolPooledAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 5, 1, 5),
    _CucsIppoolPooledAssignedToDn_Type()
)
cucsIppoolPooledAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPooledAssignedToDn.setStatus("current")
_CucsIppoolPooledDefGw_Type = InetAddressIPv4
_CucsIppoolPooledDefGw_Object = MibTableColumn
cucsIppoolPooledDefGw = _CucsIppoolPooledDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 5, 1, 6),
    _CucsIppoolPooledDefGw_Type()
)
cucsIppoolPooledDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPooledDefGw.setStatus("current")
_CucsIppoolPooledId_Type = InetAddressIPv4
_CucsIppoolPooledId_Object = MibTableColumn
cucsIppoolPooledId = _CucsIppoolPooledId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 5, 1, 7),
    _CucsIppoolPooledId_Type()
)
cucsIppoolPooledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPooledId.setStatus("current")
_CucsIppoolPooledPoolableDn_Type = SnmpAdminString
_CucsIppoolPooledPoolableDn_Object = MibTableColumn
cucsIppoolPooledPoolableDn = _CucsIppoolPooledPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 5, 1, 8),
    _CucsIppoolPooledPoolableDn_Type()
)
cucsIppoolPooledPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPooledPoolableDn.setStatus("current")
_CucsIppoolPooledPrevAssignedToDn_Type = SnmpAdminString
_CucsIppoolPooledPrevAssignedToDn_Object = MibTableColumn
cucsIppoolPooledPrevAssignedToDn = _CucsIppoolPooledPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 5, 1, 9),
    _CucsIppoolPooledPrevAssignedToDn_Type()
)
cucsIppoolPooledPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPooledPrevAssignedToDn.setStatus("current")
_CucsIppoolPooledSubnet_Type = InetAddressIPv4
_CucsIppoolPooledSubnet_Object = MibTableColumn
cucsIppoolPooledSubnet = _CucsIppoolPooledSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 5, 1, 10),
    _CucsIppoolPooledSubnet_Type()
)
cucsIppoolPooledSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPooledSubnet.setStatus("current")
_CucsIppoolPooledPrimDns_Type = InetAddressIPv4
_CucsIppoolPooledPrimDns_Object = MibTableColumn
cucsIppoolPooledPrimDns = _CucsIppoolPooledPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 5, 1, 11),
    _CucsIppoolPooledPrimDns_Type()
)
cucsIppoolPooledPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPooledPrimDns.setStatus("current")
_CucsIppoolPooledSecDns_Type = InetAddressIPv4
_CucsIppoolPooledSecDns_Object = MibTableColumn
cucsIppoolPooledSecDns = _CucsIppoolPooledSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 5, 1, 12),
    _CucsIppoolPooledSecDns_Type()
)
cucsIppoolPooledSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolPooledSecDns.setStatus("current")
_CucsIppoolUniverseTable_Object = MibTable
cucsIppoolUniverseTable = _CucsIppoolUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 6)
)
if mibBuilder.loadTexts:
    cucsIppoolUniverseTable.setStatus("current")
_CucsIppoolUniverseEntry_Object = MibTableRow
cucsIppoolUniverseEntry = _CucsIppoolUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 6, 1)
)
cucsIppoolUniverseEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IPPOOL-MIB", "cucsIppoolUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIppoolUniverseEntry.setStatus("current")
_CucsIppoolUniverseInstanceId_Type = CucsManagedObjectId
_CucsIppoolUniverseInstanceId_Object = MibTableColumn
cucsIppoolUniverseInstanceId = _CucsIppoolUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 6, 1, 1),
    _CucsIppoolUniverseInstanceId_Type()
)
cucsIppoolUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIppoolUniverseInstanceId.setStatus("current")
_CucsIppoolUniverseDn_Type = CucsManagedObjectDn
_CucsIppoolUniverseDn_Object = MibTableColumn
cucsIppoolUniverseDn = _CucsIppoolUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 6, 1, 2),
    _CucsIppoolUniverseDn_Type()
)
cucsIppoolUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolUniverseDn.setStatus("current")
_CucsIppoolUniverseRn_Type = SnmpAdminString
_CucsIppoolUniverseRn_Object = MibTableColumn
cucsIppoolUniverseRn = _CucsIppoolUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 6, 1, 3),
    _CucsIppoolUniverseRn_Type()
)
cucsIppoolUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolUniverseRn.setStatus("current")
_CucsIppoolIpV6AddrTable_Object = MibTable
cucsIppoolIpV6AddrTable = _CucsIppoolIpV6AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 7)
)
if mibBuilder.loadTexts:
    cucsIppoolIpV6AddrTable.setStatus("current")
_CucsIppoolIpV6AddrEntry_Object = MibTableRow
cucsIppoolIpV6AddrEntry = _CucsIppoolIpV6AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 7, 1)
)
cucsIppoolIpV6AddrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IPPOOL-MIB", "cucsIppoolIpV6AddrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIppoolIpV6AddrEntry.setStatus("current")
_CucsIppoolIpV6AddrInstanceId_Type = CucsManagedObjectId
_CucsIppoolIpV6AddrInstanceId_Object = MibTableColumn
cucsIppoolIpV6AddrInstanceId = _CucsIppoolIpV6AddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 7, 1, 1),
    _CucsIppoolIpV6AddrInstanceId_Type()
)
cucsIppoolIpV6AddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIppoolIpV6AddrInstanceId.setStatus("current")
_CucsIppoolIpV6AddrDn_Type = CucsManagedObjectDn
_CucsIppoolIpV6AddrDn_Object = MibTableColumn
cucsIppoolIpV6AddrDn = _CucsIppoolIpV6AddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 7, 1, 2),
    _CucsIppoolIpV6AddrDn_Type()
)
cucsIppoolIpV6AddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6AddrDn.setStatus("current")
_CucsIppoolIpV6AddrRn_Type = SnmpAdminString
_CucsIppoolIpV6AddrRn_Object = MibTableColumn
cucsIppoolIpV6AddrRn = _CucsIppoolIpV6AddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 7, 1, 3),
    _CucsIppoolIpV6AddrRn_Type()
)
cucsIppoolIpV6AddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6AddrRn.setStatus("current")
_CucsIppoolIpV6AddrAssigned_Type = TruthValue
_CucsIppoolIpV6AddrAssigned_Object = MibTableColumn
cucsIppoolIpV6AddrAssigned = _CucsIppoolIpV6AddrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 7, 1, 4),
    _CucsIppoolIpV6AddrAssigned_Type()
)
cucsIppoolIpV6AddrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6AddrAssigned.setStatus("current")
_CucsIppoolIpV6AddrAssignedToDn_Type = SnmpAdminString
_CucsIppoolIpV6AddrAssignedToDn_Object = MibTableColumn
cucsIppoolIpV6AddrAssignedToDn = _CucsIppoolIpV6AddrAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 7, 1, 5),
    _CucsIppoolIpV6AddrAssignedToDn_Type()
)
cucsIppoolIpV6AddrAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6AddrAssignedToDn.setStatus("current")
_CucsIppoolIpV6AddrId_Type = InetAddressIPv6
_CucsIppoolIpV6AddrId_Object = MibTableColumn
cucsIppoolIpV6AddrId = _CucsIppoolIpV6AddrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 7, 1, 6),
    _CucsIppoolIpV6AddrId_Type()
)
cucsIppoolIpV6AddrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6AddrId.setStatus("current")
_CucsIppoolIpV6AddrOwner_Type = CucsPoolElementOwner
_CucsIppoolIpV6AddrOwner_Object = MibTableColumn
cucsIppoolIpV6AddrOwner = _CucsIppoolIpV6AddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 7, 1, 7),
    _CucsIppoolIpV6AddrOwner_Type()
)
cucsIppoolIpV6AddrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6AddrOwner.setStatus("current")
_CucsIppoolIpV6AddrGlobalAssignedCnt_Type = Gauge32
_CucsIppoolIpV6AddrGlobalAssignedCnt_Object = MibTableColumn
cucsIppoolIpV6AddrGlobalAssignedCnt = _CucsIppoolIpV6AddrGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 7, 1, 8),
    _CucsIppoolIpV6AddrGlobalAssignedCnt_Type()
)
cucsIppoolIpV6AddrGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6AddrGlobalAssignedCnt.setStatus("current")
_CucsIppoolIpV6AddrGlobalDefinedCnt_Type = Gauge32
_CucsIppoolIpV6AddrGlobalDefinedCnt_Object = MibTableColumn
cucsIppoolIpV6AddrGlobalDefinedCnt = _CucsIppoolIpV6AddrGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 7, 1, 9),
    _CucsIppoolIpV6AddrGlobalDefinedCnt_Type()
)
cucsIppoolIpV6AddrGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6AddrGlobalDefinedCnt.setStatus("current")
_CucsIppoolIpV6BlockTable_Object = MibTable
cucsIppoolIpV6BlockTable = _CucsIppoolIpV6BlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 8)
)
if mibBuilder.loadTexts:
    cucsIppoolIpV6BlockTable.setStatus("current")
_CucsIppoolIpV6BlockEntry_Object = MibTableRow
cucsIppoolIpV6BlockEntry = _CucsIppoolIpV6BlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 8, 1)
)
cucsIppoolIpV6BlockEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IPPOOL-MIB", "cucsIppoolIpV6BlockInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIppoolIpV6BlockEntry.setStatus("current")
_CucsIppoolIpV6BlockInstanceId_Type = CucsManagedObjectId
_CucsIppoolIpV6BlockInstanceId_Object = MibTableColumn
cucsIppoolIpV6BlockInstanceId = _CucsIppoolIpV6BlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 8, 1, 1),
    _CucsIppoolIpV6BlockInstanceId_Type()
)
cucsIppoolIpV6BlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIppoolIpV6BlockInstanceId.setStatus("current")
_CucsIppoolIpV6BlockDn_Type = CucsManagedObjectDn
_CucsIppoolIpV6BlockDn_Object = MibTableColumn
cucsIppoolIpV6BlockDn = _CucsIppoolIpV6BlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 8, 1, 2),
    _CucsIppoolIpV6BlockDn_Type()
)
cucsIppoolIpV6BlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6BlockDn.setStatus("current")
_CucsIppoolIpV6BlockRn_Type = SnmpAdminString
_CucsIppoolIpV6BlockRn_Object = MibTableColumn
cucsIppoolIpV6BlockRn = _CucsIppoolIpV6BlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 8, 1, 3),
    _CucsIppoolIpV6BlockRn_Type()
)
cucsIppoolIpV6BlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6BlockRn.setStatus("current")
_CucsIppoolIpV6BlockDefGw_Type = InetAddressIPv6
_CucsIppoolIpV6BlockDefGw_Object = MibTableColumn
cucsIppoolIpV6BlockDefGw = _CucsIppoolIpV6BlockDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 8, 1, 4),
    _CucsIppoolIpV6BlockDefGw_Type()
)
cucsIppoolIpV6BlockDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6BlockDefGw.setStatus("current")
_CucsIppoolIpV6BlockFrom_Type = InetAddressIPv6
_CucsIppoolIpV6BlockFrom_Object = MibTableColumn
cucsIppoolIpV6BlockFrom = _CucsIppoolIpV6BlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 8, 1, 5),
    _CucsIppoolIpV6BlockFrom_Type()
)
cucsIppoolIpV6BlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6BlockFrom.setStatus("current")
_CucsIppoolIpV6BlockPrefix_Type = Gauge32
_CucsIppoolIpV6BlockPrefix_Object = MibTableColumn
cucsIppoolIpV6BlockPrefix = _CucsIppoolIpV6BlockPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 8, 1, 6),
    _CucsIppoolIpV6BlockPrefix_Type()
)
cucsIppoolIpV6BlockPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6BlockPrefix.setStatus("current")
_CucsIppoolIpV6BlockPrimDns_Type = InetAddressIPv6
_CucsIppoolIpV6BlockPrimDns_Object = MibTableColumn
cucsIppoolIpV6BlockPrimDns = _CucsIppoolIpV6BlockPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 8, 1, 7),
    _CucsIppoolIpV6BlockPrimDns_Type()
)
cucsIppoolIpV6BlockPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6BlockPrimDns.setStatus("current")
_CucsIppoolIpV6BlockSecDns_Type = InetAddressIPv6
_CucsIppoolIpV6BlockSecDns_Object = MibTableColumn
cucsIppoolIpV6BlockSecDns = _CucsIppoolIpV6BlockSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 8, 1, 8),
    _CucsIppoolIpV6BlockSecDns_Type()
)
cucsIppoolIpV6BlockSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6BlockSecDns.setStatus("current")
_CucsIppoolIpV6BlockTo_Type = InetAddressIPv6
_CucsIppoolIpV6BlockTo_Object = MibTableColumn
cucsIppoolIpV6BlockTo = _CucsIppoolIpV6BlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 8, 1, 9),
    _CucsIppoolIpV6BlockTo_Type()
)
cucsIppoolIpV6BlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6BlockTo.setStatus("current")
_CucsIppoolIpV6PooledTable_Object = MibTable
cucsIppoolIpV6PooledTable = _CucsIppoolIpV6PooledTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 9)
)
if mibBuilder.loadTexts:
    cucsIppoolIpV6PooledTable.setStatus("current")
_CucsIppoolIpV6PooledEntry_Object = MibTableRow
cucsIppoolIpV6PooledEntry = _CucsIppoolIpV6PooledEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 9, 1)
)
cucsIppoolIpV6PooledEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IPPOOL-MIB", "cucsIppoolIpV6PooledInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIppoolIpV6PooledEntry.setStatus("current")
_CucsIppoolIpV6PooledInstanceId_Type = CucsManagedObjectId
_CucsIppoolIpV6PooledInstanceId_Object = MibTableColumn
cucsIppoolIpV6PooledInstanceId = _CucsIppoolIpV6PooledInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 9, 1, 1),
    _CucsIppoolIpV6PooledInstanceId_Type()
)
cucsIppoolIpV6PooledInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIppoolIpV6PooledInstanceId.setStatus("current")
_CucsIppoolIpV6PooledDn_Type = CucsManagedObjectDn
_CucsIppoolIpV6PooledDn_Object = MibTableColumn
cucsIppoolIpV6PooledDn = _CucsIppoolIpV6PooledDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 9, 1, 2),
    _CucsIppoolIpV6PooledDn_Type()
)
cucsIppoolIpV6PooledDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6PooledDn.setStatus("current")
_CucsIppoolIpV6PooledRn_Type = SnmpAdminString
_CucsIppoolIpV6PooledRn_Object = MibTableColumn
cucsIppoolIpV6PooledRn = _CucsIppoolIpV6PooledRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 9, 1, 3),
    _CucsIppoolIpV6PooledRn_Type()
)
cucsIppoolIpV6PooledRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6PooledRn.setStatus("current")
_CucsIppoolIpV6PooledAssigned_Type = TruthValue
_CucsIppoolIpV6PooledAssigned_Object = MibTableColumn
cucsIppoolIpV6PooledAssigned = _CucsIppoolIpV6PooledAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 9, 1, 4),
    _CucsIppoolIpV6PooledAssigned_Type()
)
cucsIppoolIpV6PooledAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6PooledAssigned.setStatus("current")
_CucsIppoolIpV6PooledAssignedToDn_Type = SnmpAdminString
_CucsIppoolIpV6PooledAssignedToDn_Object = MibTableColumn
cucsIppoolIpV6PooledAssignedToDn = _CucsIppoolIpV6PooledAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 9, 1, 5),
    _CucsIppoolIpV6PooledAssignedToDn_Type()
)
cucsIppoolIpV6PooledAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6PooledAssignedToDn.setStatus("current")
_CucsIppoolIpV6PooledDefGw_Type = InetAddressIPv6
_CucsIppoolIpV6PooledDefGw_Object = MibTableColumn
cucsIppoolIpV6PooledDefGw = _CucsIppoolIpV6PooledDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 9, 1, 6),
    _CucsIppoolIpV6PooledDefGw_Type()
)
cucsIppoolIpV6PooledDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6PooledDefGw.setStatus("current")
_CucsIppoolIpV6PooledId_Type = InetAddressIPv6
_CucsIppoolIpV6PooledId_Object = MibTableColumn
cucsIppoolIpV6PooledId = _CucsIppoolIpV6PooledId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 9, 1, 7),
    _CucsIppoolIpV6PooledId_Type()
)
cucsIppoolIpV6PooledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6PooledId.setStatus("current")
_CucsIppoolIpV6PooledPoolableDn_Type = SnmpAdminString
_CucsIppoolIpV6PooledPoolableDn_Object = MibTableColumn
cucsIppoolIpV6PooledPoolableDn = _CucsIppoolIpV6PooledPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 9, 1, 8),
    _CucsIppoolIpV6PooledPoolableDn_Type()
)
cucsIppoolIpV6PooledPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6PooledPoolableDn.setStatus("current")
_CucsIppoolIpV6PooledPrefix_Type = Gauge32
_CucsIppoolIpV6PooledPrefix_Object = MibTableColumn
cucsIppoolIpV6PooledPrefix = _CucsIppoolIpV6PooledPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 9, 1, 9),
    _CucsIppoolIpV6PooledPrefix_Type()
)
cucsIppoolIpV6PooledPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6PooledPrefix.setStatus("current")
_CucsIppoolIpV6PooledPrevAssignedToDn_Type = SnmpAdminString
_CucsIppoolIpV6PooledPrevAssignedToDn_Object = MibTableColumn
cucsIppoolIpV6PooledPrevAssignedToDn = _CucsIppoolIpV6PooledPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 9, 1, 10),
    _CucsIppoolIpV6PooledPrevAssignedToDn_Type()
)
cucsIppoolIpV6PooledPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6PooledPrevAssignedToDn.setStatus("current")
_CucsIppoolIpV6PooledPrimDns_Type = InetAddressIPv6
_CucsIppoolIpV6PooledPrimDns_Object = MibTableColumn
cucsIppoolIpV6PooledPrimDns = _CucsIppoolIpV6PooledPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 9, 1, 11),
    _CucsIppoolIpV6PooledPrimDns_Type()
)
cucsIppoolIpV6PooledPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6PooledPrimDns.setStatus("current")
_CucsIppoolIpV6PooledSecDns_Type = InetAddressIPv6
_CucsIppoolIpV6PooledSecDns_Object = MibTableColumn
cucsIppoolIpV6PooledSecDns = _CucsIppoolIpV6PooledSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 24, 9, 1, 12),
    _CucsIppoolIpV6PooledSecDns_Type()
)
cucsIppoolIpV6PooledSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIppoolIpV6PooledSecDns.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-IPPOOL-MIB",
    **{"cucsIppoolObjects": cucsIppoolObjects,
       "cucsIppoolAddrTable": cucsIppoolAddrTable,
       "cucsIppoolAddrEntry": cucsIppoolAddrEntry,
       "cucsIppoolAddrInstanceId": cucsIppoolAddrInstanceId,
       "cucsIppoolAddrDn": cucsIppoolAddrDn,
       "cucsIppoolAddrRn": cucsIppoolAddrRn,
       "cucsIppoolAddrAssigned": cucsIppoolAddrAssigned,
       "cucsIppoolAddrAssignedToDn": cucsIppoolAddrAssignedToDn,
       "cucsIppoolAddrId": cucsIppoolAddrId,
       "cucsIppoolAddrOwner": cucsIppoolAddrOwner,
       "cucsIppoolAddrGlobalAssignedCnt": cucsIppoolAddrGlobalAssignedCnt,
       "cucsIppoolAddrGlobalDefinedCnt": cucsIppoolAddrGlobalDefinedCnt,
       "cucsIppoolBlockTable": cucsIppoolBlockTable,
       "cucsIppoolBlockEntry": cucsIppoolBlockEntry,
       "cucsIppoolBlockInstanceId": cucsIppoolBlockInstanceId,
       "cucsIppoolBlockDn": cucsIppoolBlockDn,
       "cucsIppoolBlockRn": cucsIppoolBlockRn,
       "cucsIppoolBlockDefGw": cucsIppoolBlockDefGw,
       "cucsIppoolBlockFrom": cucsIppoolBlockFrom,
       "cucsIppoolBlockSubnet": cucsIppoolBlockSubnet,
       "cucsIppoolBlockTo": cucsIppoolBlockTo,
       "cucsIppoolBlockPrimDns": cucsIppoolBlockPrimDns,
       "cucsIppoolBlockSecDns": cucsIppoolBlockSecDns,
       "cucsIppoolPoolTable": cucsIppoolPoolTable,
       "cucsIppoolPoolEntry": cucsIppoolPoolEntry,
       "cucsIppoolPoolInstanceId": cucsIppoolPoolInstanceId,
       "cucsIppoolPoolDn": cucsIppoolPoolDn,
       "cucsIppoolPoolRn": cucsIppoolPoolRn,
       "cucsIppoolPoolAssigned": cucsIppoolPoolAssigned,
       "cucsIppoolPoolDescr": cucsIppoolPoolDescr,
       "cucsIppoolPoolIntId": cucsIppoolPoolIntId,
       "cucsIppoolPoolName": cucsIppoolPoolName,
       "cucsIppoolPoolSize": cucsIppoolPoolSize,
       "cucsIppoolPoolAssignmentOrder": cucsIppoolPoolAssignmentOrder,
       "cucsIppoolPoolPolicyLevel": cucsIppoolPoolPolicyLevel,
       "cucsIppoolPoolPolicyOwner": cucsIppoolPoolPolicyOwner,
       "cucsIppoolPoolExtManaged": cucsIppoolPoolExtManaged,
       "cucsIppoolPoolGuid": cucsIppoolPoolGuid,
       "cucsIppoolPoolIsNetBIOSEnabled": cucsIppoolPoolIsNetBIOSEnabled,
       "cucsIppoolPoolSupportsDHCP": cucsIppoolPoolSupportsDHCP,
       "cucsIppoolPoolV4Assigned": cucsIppoolPoolV4Assigned,
       "cucsIppoolPoolV4Size": cucsIppoolPoolV4Size,
       "cucsIppoolPoolV6Assigned": cucsIppoolPoolV6Assigned,
       "cucsIppoolPoolV6Size": cucsIppoolPoolV6Size,
       "cucsIppoolPoolPropAcl": cucsIppoolPoolPropAcl,
       "cucsIppoolPoolableTable": cucsIppoolPoolableTable,
       "cucsIppoolPoolableEntry": cucsIppoolPoolableEntry,
       "cucsIppoolPoolableInstanceId": cucsIppoolPoolableInstanceId,
       "cucsIppoolPoolableDn": cucsIppoolPoolableDn,
       "cucsIppoolPoolableRn": cucsIppoolPoolableRn,
       "cucsIppoolPoolableId": cucsIppoolPoolableId,
       "cucsIppoolPoolablePoolDn": cucsIppoolPoolablePoolDn,
       "cucsIppoolPooledTable": cucsIppoolPooledTable,
       "cucsIppoolPooledEntry": cucsIppoolPooledEntry,
       "cucsIppoolPooledInstanceId": cucsIppoolPooledInstanceId,
       "cucsIppoolPooledDn": cucsIppoolPooledDn,
       "cucsIppoolPooledRn": cucsIppoolPooledRn,
       "cucsIppoolPooledAssigned": cucsIppoolPooledAssigned,
       "cucsIppoolPooledAssignedToDn": cucsIppoolPooledAssignedToDn,
       "cucsIppoolPooledDefGw": cucsIppoolPooledDefGw,
       "cucsIppoolPooledId": cucsIppoolPooledId,
       "cucsIppoolPooledPoolableDn": cucsIppoolPooledPoolableDn,
       "cucsIppoolPooledPrevAssignedToDn": cucsIppoolPooledPrevAssignedToDn,
       "cucsIppoolPooledSubnet": cucsIppoolPooledSubnet,
       "cucsIppoolPooledPrimDns": cucsIppoolPooledPrimDns,
       "cucsIppoolPooledSecDns": cucsIppoolPooledSecDns,
       "cucsIppoolUniverseTable": cucsIppoolUniverseTable,
       "cucsIppoolUniverseEntry": cucsIppoolUniverseEntry,
       "cucsIppoolUniverseInstanceId": cucsIppoolUniverseInstanceId,
       "cucsIppoolUniverseDn": cucsIppoolUniverseDn,
       "cucsIppoolUniverseRn": cucsIppoolUniverseRn,
       "cucsIppoolIpV6AddrTable": cucsIppoolIpV6AddrTable,
       "cucsIppoolIpV6AddrEntry": cucsIppoolIpV6AddrEntry,
       "cucsIppoolIpV6AddrInstanceId": cucsIppoolIpV6AddrInstanceId,
       "cucsIppoolIpV6AddrDn": cucsIppoolIpV6AddrDn,
       "cucsIppoolIpV6AddrRn": cucsIppoolIpV6AddrRn,
       "cucsIppoolIpV6AddrAssigned": cucsIppoolIpV6AddrAssigned,
       "cucsIppoolIpV6AddrAssignedToDn": cucsIppoolIpV6AddrAssignedToDn,
       "cucsIppoolIpV6AddrId": cucsIppoolIpV6AddrId,
       "cucsIppoolIpV6AddrOwner": cucsIppoolIpV6AddrOwner,
       "cucsIppoolIpV6AddrGlobalAssignedCnt": cucsIppoolIpV6AddrGlobalAssignedCnt,
       "cucsIppoolIpV6AddrGlobalDefinedCnt": cucsIppoolIpV6AddrGlobalDefinedCnt,
       "cucsIppoolIpV6BlockTable": cucsIppoolIpV6BlockTable,
       "cucsIppoolIpV6BlockEntry": cucsIppoolIpV6BlockEntry,
       "cucsIppoolIpV6BlockInstanceId": cucsIppoolIpV6BlockInstanceId,
       "cucsIppoolIpV6BlockDn": cucsIppoolIpV6BlockDn,
       "cucsIppoolIpV6BlockRn": cucsIppoolIpV6BlockRn,
       "cucsIppoolIpV6BlockDefGw": cucsIppoolIpV6BlockDefGw,
       "cucsIppoolIpV6BlockFrom": cucsIppoolIpV6BlockFrom,
       "cucsIppoolIpV6BlockPrefix": cucsIppoolIpV6BlockPrefix,
       "cucsIppoolIpV6BlockPrimDns": cucsIppoolIpV6BlockPrimDns,
       "cucsIppoolIpV6BlockSecDns": cucsIppoolIpV6BlockSecDns,
       "cucsIppoolIpV6BlockTo": cucsIppoolIpV6BlockTo,
       "cucsIppoolIpV6PooledTable": cucsIppoolIpV6PooledTable,
       "cucsIppoolIpV6PooledEntry": cucsIppoolIpV6PooledEntry,
       "cucsIppoolIpV6PooledInstanceId": cucsIppoolIpV6PooledInstanceId,
       "cucsIppoolIpV6PooledDn": cucsIppoolIpV6PooledDn,
       "cucsIppoolIpV6PooledRn": cucsIppoolIpV6PooledRn,
       "cucsIppoolIpV6PooledAssigned": cucsIppoolIpV6PooledAssigned,
       "cucsIppoolIpV6PooledAssignedToDn": cucsIppoolIpV6PooledAssignedToDn,
       "cucsIppoolIpV6PooledDefGw": cucsIppoolIpV6PooledDefGw,
       "cucsIppoolIpV6PooledId": cucsIppoolIpV6PooledId,
       "cucsIppoolIpV6PooledPoolableDn": cucsIppoolIpV6PooledPoolableDn,
       "cucsIppoolIpV6PooledPrefix": cucsIppoolIpV6PooledPrefix,
       "cucsIppoolIpV6PooledPrevAssignedToDn": cucsIppoolIpV6PooledPrevAssignedToDn,
       "cucsIppoolIpV6PooledPrimDns": cucsIppoolIpV6PooledPrimDns,
       "cucsIppoolIpV6PooledSecDns": cucsIppoolIpV6PooledSecDns}
)
