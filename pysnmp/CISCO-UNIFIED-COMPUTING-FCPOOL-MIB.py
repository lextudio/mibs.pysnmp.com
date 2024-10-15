# SNMP MIB module (CISCO-UNIFIED-COMPUTING-FCPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-FCPOOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:31 2024
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

(CucsAddressWWNMask,
 CucsFcpoolBootTargetType,
 CucsFcpoolInitiatorEpPurpose,
 CucsFcpoolInitiatorPurpose,
 CucsFcpoolInitiatorsAssignmentOrder,
 CucsFcpoolInitiatorsMaxPortsPerNode,
 CucsFcpoolInitiatorsPurpose,
 CucsPolicyPolicyOwner,
 CucsPoolElementOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsAddressWWNMask",
    "CucsFcpoolBootTargetType",
    "CucsFcpoolInitiatorEpPurpose",
    "CucsFcpoolInitiatorPurpose",
    "CucsFcpoolInitiatorsAssignmentOrder",
    "CucsFcpoolInitiatorsMaxPortsPerNode",
    "CucsFcpoolInitiatorsPurpose",
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

cucsFcpoolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsFcpoolAddrTable_Object = MibTable
cucsFcpoolAddrTable = _CucsFcpoolAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1)
)
if mibBuilder.loadTexts:
    cucsFcpoolAddrTable.setStatus("current")
_CucsFcpoolAddrEntry_Object = MibTableRow
cucsFcpoolAddrEntry = _CucsFcpoolAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1)
)
cucsFcpoolAddrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcpoolAddrEntry.setStatus("current")
_CucsFcpoolAddrInstanceId_Type = CucsManagedObjectId
_CucsFcpoolAddrInstanceId_Object = MibTableColumn
cucsFcpoolAddrInstanceId = _CucsFcpoolAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 1),
    _CucsFcpoolAddrInstanceId_Type()
)
cucsFcpoolAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcpoolAddrInstanceId.setStatus("current")
_CucsFcpoolAddrDn_Type = CucsManagedObjectDn
_CucsFcpoolAddrDn_Object = MibTableColumn
cucsFcpoolAddrDn = _CucsFcpoolAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 2),
    _CucsFcpoolAddrDn_Type()
)
cucsFcpoolAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolAddrDn.setStatus("current")
_CucsFcpoolAddrRn_Type = SnmpAdminString
_CucsFcpoolAddrRn_Object = MibTableColumn
cucsFcpoolAddrRn = _CucsFcpoolAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 3),
    _CucsFcpoolAddrRn_Type()
)
cucsFcpoolAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolAddrRn.setStatus("current")
_CucsFcpoolAddrAssigned_Type = TruthValue
_CucsFcpoolAddrAssigned_Object = MibTableColumn
cucsFcpoolAddrAssigned = _CucsFcpoolAddrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 4),
    _CucsFcpoolAddrAssigned_Type()
)
cucsFcpoolAddrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolAddrAssigned.setStatus("current")
_CucsFcpoolAddrAssignedToDn_Type = SnmpAdminString
_CucsFcpoolAddrAssignedToDn_Object = MibTableColumn
cucsFcpoolAddrAssignedToDn = _CucsFcpoolAddrAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 5),
    _CucsFcpoolAddrAssignedToDn_Type()
)
cucsFcpoolAddrAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolAddrAssignedToDn.setStatus("current")
_CucsFcpoolAddrId_Type = Unsigned64
_CucsFcpoolAddrId_Object = MibTableColumn
cucsFcpoolAddrId = _CucsFcpoolAddrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 6),
    _CucsFcpoolAddrId_Type()
)
cucsFcpoolAddrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolAddrId.setStatus("current")
_CucsFcpoolAddrOwner_Type = CucsPoolElementOwner
_CucsFcpoolAddrOwner_Object = MibTableColumn
cucsFcpoolAddrOwner = _CucsFcpoolAddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 7),
    _CucsFcpoolAddrOwner_Type()
)
cucsFcpoolAddrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolAddrOwner.setStatus("current")
_CucsFcpoolAddrGlobalAssignedCnt_Type = Gauge32
_CucsFcpoolAddrGlobalAssignedCnt_Object = MibTableColumn
cucsFcpoolAddrGlobalAssignedCnt = _CucsFcpoolAddrGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 8),
    _CucsFcpoolAddrGlobalAssignedCnt_Type()
)
cucsFcpoolAddrGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolAddrGlobalAssignedCnt.setStatus("current")
_CucsFcpoolAddrGlobalDefinedCnt_Type = Gauge32
_CucsFcpoolAddrGlobalDefinedCnt_Object = MibTableColumn
cucsFcpoolAddrGlobalDefinedCnt = _CucsFcpoolAddrGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 9),
    _CucsFcpoolAddrGlobalDefinedCnt_Type()
)
cucsFcpoolAddrGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolAddrGlobalDefinedCnt.setStatus("current")
_CucsFcpoolBlockTable_Object = MibTable
cucsFcpoolBlockTable = _CucsFcpoolBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 2)
)
if mibBuilder.loadTexts:
    cucsFcpoolBlockTable.setStatus("current")
_CucsFcpoolBlockEntry_Object = MibTableRow
cucsFcpoolBlockEntry = _CucsFcpoolBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 2, 1)
)
cucsFcpoolBlockEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolBlockInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcpoolBlockEntry.setStatus("current")
_CucsFcpoolBlockInstanceId_Type = CucsManagedObjectId
_CucsFcpoolBlockInstanceId_Object = MibTableColumn
cucsFcpoolBlockInstanceId = _CucsFcpoolBlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 2, 1, 1),
    _CucsFcpoolBlockInstanceId_Type()
)
cucsFcpoolBlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcpoolBlockInstanceId.setStatus("current")
_CucsFcpoolBlockDn_Type = CucsManagedObjectDn
_CucsFcpoolBlockDn_Object = MibTableColumn
cucsFcpoolBlockDn = _CucsFcpoolBlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 2, 1, 2),
    _CucsFcpoolBlockDn_Type()
)
cucsFcpoolBlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolBlockDn.setStatus("current")
_CucsFcpoolBlockRn_Type = SnmpAdminString
_CucsFcpoolBlockRn_Object = MibTableColumn
cucsFcpoolBlockRn = _CucsFcpoolBlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 2, 1, 3),
    _CucsFcpoolBlockRn_Type()
)
cucsFcpoolBlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolBlockRn.setStatus("current")
_CucsFcpoolBlockFrom_Type = Unsigned64
_CucsFcpoolBlockFrom_Object = MibTableColumn
cucsFcpoolBlockFrom = _CucsFcpoolBlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 2, 1, 4),
    _CucsFcpoolBlockFrom_Type()
)
cucsFcpoolBlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolBlockFrom.setStatus("current")
_CucsFcpoolBlockTo_Type = Unsigned64
_CucsFcpoolBlockTo_Object = MibTableColumn
cucsFcpoolBlockTo = _CucsFcpoolBlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 2, 1, 5),
    _CucsFcpoolBlockTo_Type()
)
cucsFcpoolBlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolBlockTo.setStatus("current")
_CucsFcpoolBootTargetTable_Object = MibTable
cucsFcpoolBootTargetTable = _CucsFcpoolBootTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 3)
)
if mibBuilder.loadTexts:
    cucsFcpoolBootTargetTable.setStatus("current")
_CucsFcpoolBootTargetEntry_Object = MibTableRow
cucsFcpoolBootTargetEntry = _CucsFcpoolBootTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 3, 1)
)
cucsFcpoolBootTargetEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolBootTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcpoolBootTargetEntry.setStatus("current")
_CucsFcpoolBootTargetInstanceId_Type = CucsManagedObjectId
_CucsFcpoolBootTargetInstanceId_Object = MibTableColumn
cucsFcpoolBootTargetInstanceId = _CucsFcpoolBootTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 3, 1, 1),
    _CucsFcpoolBootTargetInstanceId_Type()
)
cucsFcpoolBootTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcpoolBootTargetInstanceId.setStatus("current")
_CucsFcpoolBootTargetDn_Type = CucsManagedObjectDn
_CucsFcpoolBootTargetDn_Object = MibTableColumn
cucsFcpoolBootTargetDn = _CucsFcpoolBootTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 3, 1, 2),
    _CucsFcpoolBootTargetDn_Type()
)
cucsFcpoolBootTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolBootTargetDn.setStatus("current")
_CucsFcpoolBootTargetRn_Type = SnmpAdminString
_CucsFcpoolBootTargetRn_Object = MibTableColumn
cucsFcpoolBootTargetRn = _CucsFcpoolBootTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 3, 1, 3),
    _CucsFcpoolBootTargetRn_Type()
)
cucsFcpoolBootTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolBootTargetRn.setStatus("current")
_CucsFcpoolBootTargetLun_Type = SnmpAdminString
_CucsFcpoolBootTargetLun_Object = MibTableColumn
cucsFcpoolBootTargetLun = _CucsFcpoolBootTargetLun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 3, 1, 4),
    _CucsFcpoolBootTargetLun_Type()
)
cucsFcpoolBootTargetLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolBootTargetLun.setStatus("current")
_CucsFcpoolBootTargetType_Type = CucsFcpoolBootTargetType
_CucsFcpoolBootTargetType_Object = MibTableColumn
cucsFcpoolBootTargetType = _CucsFcpoolBootTargetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 3, 1, 5),
    _CucsFcpoolBootTargetType_Type()
)
cucsFcpoolBootTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolBootTargetType.setStatus("current")
_CucsFcpoolBootTargetWwn_Type = Unsigned64
_CucsFcpoolBootTargetWwn_Object = MibTableColumn
cucsFcpoolBootTargetWwn = _CucsFcpoolBootTargetWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 3, 1, 6),
    _CucsFcpoolBootTargetWwn_Type()
)
cucsFcpoolBootTargetWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolBootTargetWwn.setStatus("current")
_CucsFcpoolFormatTable_Object = MibTable
cucsFcpoolFormatTable = _CucsFcpoolFormatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 4)
)
if mibBuilder.loadTexts:
    cucsFcpoolFormatTable.setStatus("current")
_CucsFcpoolFormatEntry_Object = MibTableRow
cucsFcpoolFormatEntry = _CucsFcpoolFormatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 4, 1)
)
cucsFcpoolFormatEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolFormatInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcpoolFormatEntry.setStatus("current")
_CucsFcpoolFormatInstanceId_Type = CucsManagedObjectId
_CucsFcpoolFormatInstanceId_Object = MibTableColumn
cucsFcpoolFormatInstanceId = _CucsFcpoolFormatInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 4, 1, 1),
    _CucsFcpoolFormatInstanceId_Type()
)
cucsFcpoolFormatInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcpoolFormatInstanceId.setStatus("current")
_CucsFcpoolFormatDn_Type = CucsManagedObjectDn
_CucsFcpoolFormatDn_Object = MibTableColumn
cucsFcpoolFormatDn = _CucsFcpoolFormatDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 4, 1, 2),
    _CucsFcpoolFormatDn_Type()
)
cucsFcpoolFormatDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolFormatDn.setStatus("current")
_CucsFcpoolFormatRn_Type = SnmpAdminString
_CucsFcpoolFormatRn_Object = MibTableColumn
cucsFcpoolFormatRn = _CucsFcpoolFormatRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 4, 1, 3),
    _CucsFcpoolFormatRn_Type()
)
cucsFcpoolFormatRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolFormatRn.setStatus("current")
_CucsFcpoolFormatFormat_Type = Unsigned64
_CucsFcpoolFormatFormat_Object = MibTableColumn
cucsFcpoolFormatFormat = _CucsFcpoolFormatFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 4, 1, 4),
    _CucsFcpoolFormatFormat_Type()
)
cucsFcpoolFormatFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolFormatFormat.setStatus("current")
_CucsFcpoolFormatMask_Type = CucsAddressWWNMask
_CucsFcpoolFormatMask_Object = MibTableColumn
cucsFcpoolFormatMask = _CucsFcpoolFormatMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 4, 1, 5),
    _CucsFcpoolFormatMask_Type()
)
cucsFcpoolFormatMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolFormatMask.setStatus("current")
_CucsFcpoolInitiatorTable_Object = MibTable
cucsFcpoolInitiatorTable = _CucsFcpoolInitiatorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5)
)
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorTable.setStatus("current")
_CucsFcpoolInitiatorEntry_Object = MibTableRow
cucsFcpoolInitiatorEntry = _CucsFcpoolInitiatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1)
)
cucsFcpoolInitiatorEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolInitiatorInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorEntry.setStatus("current")
_CucsFcpoolInitiatorInstanceId_Type = CucsManagedObjectId
_CucsFcpoolInitiatorInstanceId_Object = MibTableColumn
cucsFcpoolInitiatorInstanceId = _CucsFcpoolInitiatorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 1),
    _CucsFcpoolInitiatorInstanceId_Type()
)
cucsFcpoolInitiatorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorInstanceId.setStatus("current")
_CucsFcpoolInitiatorDn_Type = CucsManagedObjectDn
_CucsFcpoolInitiatorDn_Object = MibTableColumn
cucsFcpoolInitiatorDn = _CucsFcpoolInitiatorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 2),
    _CucsFcpoolInitiatorDn_Type()
)
cucsFcpoolInitiatorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorDn.setStatus("current")
_CucsFcpoolInitiatorRn_Type = SnmpAdminString
_CucsFcpoolInitiatorRn_Object = MibTableColumn
cucsFcpoolInitiatorRn = _CucsFcpoolInitiatorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 3),
    _CucsFcpoolInitiatorRn_Type()
)
cucsFcpoolInitiatorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorRn.setStatus("current")
_CucsFcpoolInitiatorAssigned_Type = TruthValue
_CucsFcpoolInitiatorAssigned_Object = MibTableColumn
cucsFcpoolInitiatorAssigned = _CucsFcpoolInitiatorAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 4),
    _CucsFcpoolInitiatorAssigned_Type()
)
cucsFcpoolInitiatorAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorAssigned.setStatus("current")
_CucsFcpoolInitiatorAssignedToDn_Type = SnmpAdminString
_CucsFcpoolInitiatorAssignedToDn_Object = MibTableColumn
cucsFcpoolInitiatorAssignedToDn = _CucsFcpoolInitiatorAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 5),
    _CucsFcpoolInitiatorAssignedToDn_Type()
)
cucsFcpoolInitiatorAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorAssignedToDn.setStatus("current")
_CucsFcpoolInitiatorDescr_Type = SnmpAdminString
_CucsFcpoolInitiatorDescr_Object = MibTableColumn
cucsFcpoolInitiatorDescr = _CucsFcpoolInitiatorDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 6),
    _CucsFcpoolInitiatorDescr_Type()
)
cucsFcpoolInitiatorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorDescr.setStatus("current")
_CucsFcpoolInitiatorId_Type = Unsigned64
_CucsFcpoolInitiatorId_Object = MibTableColumn
cucsFcpoolInitiatorId = _CucsFcpoolInitiatorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 7),
    _CucsFcpoolInitiatorId_Type()
)
cucsFcpoolInitiatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorId.setStatus("current")
_CucsFcpoolInitiatorName_Type = SnmpAdminString
_CucsFcpoolInitiatorName_Object = MibTableColumn
cucsFcpoolInitiatorName = _CucsFcpoolInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 8),
    _CucsFcpoolInitiatorName_Type()
)
cucsFcpoolInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorName.setStatus("current")
_CucsFcpoolInitiatorPoolableDn_Type = SnmpAdminString
_CucsFcpoolInitiatorPoolableDn_Object = MibTableColumn
cucsFcpoolInitiatorPoolableDn = _CucsFcpoolInitiatorPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 9),
    _CucsFcpoolInitiatorPoolableDn_Type()
)
cucsFcpoolInitiatorPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorPoolableDn.setStatus("current")
_CucsFcpoolInitiatorPrevAssignedToDn_Type = SnmpAdminString
_CucsFcpoolInitiatorPrevAssignedToDn_Object = MibTableColumn
cucsFcpoolInitiatorPrevAssignedToDn = _CucsFcpoolInitiatorPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 10),
    _CucsFcpoolInitiatorPrevAssignedToDn_Type()
)
cucsFcpoolInitiatorPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorPrevAssignedToDn.setStatus("current")
_CucsFcpoolInitiatorPurpose_Type = CucsFcpoolInitiatorPurpose
_CucsFcpoolInitiatorPurpose_Object = MibTableColumn
cucsFcpoolInitiatorPurpose = _CucsFcpoolInitiatorPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 11),
    _CucsFcpoolInitiatorPurpose_Type()
)
cucsFcpoolInitiatorPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorPurpose.setStatus("current")
_CucsFcpoolInitiatorsTable_Object = MibTable
cucsFcpoolInitiatorsTable = _CucsFcpoolInitiatorsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6)
)
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorsTable.setStatus("current")
_CucsFcpoolInitiatorsEntry_Object = MibTableRow
cucsFcpoolInitiatorsEntry = _CucsFcpoolInitiatorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1)
)
cucsFcpoolInitiatorsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolInitiatorsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorsEntry.setStatus("current")
_CucsFcpoolInitiatorsInstanceId_Type = CucsManagedObjectId
_CucsFcpoolInitiatorsInstanceId_Object = MibTableColumn
cucsFcpoolInitiatorsInstanceId = _CucsFcpoolInitiatorsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 1),
    _CucsFcpoolInitiatorsInstanceId_Type()
)
cucsFcpoolInitiatorsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorsInstanceId.setStatus("current")
_CucsFcpoolInitiatorsDn_Type = CucsManagedObjectDn
_CucsFcpoolInitiatorsDn_Object = MibTableColumn
cucsFcpoolInitiatorsDn = _CucsFcpoolInitiatorsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 2),
    _CucsFcpoolInitiatorsDn_Type()
)
cucsFcpoolInitiatorsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorsDn.setStatus("current")
_CucsFcpoolInitiatorsRn_Type = SnmpAdminString
_CucsFcpoolInitiatorsRn_Object = MibTableColumn
cucsFcpoolInitiatorsRn = _CucsFcpoolInitiatorsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 3),
    _CucsFcpoolInitiatorsRn_Type()
)
cucsFcpoolInitiatorsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorsRn.setStatus("current")
_CucsFcpoolInitiatorsAssigned_Type = Gauge32
_CucsFcpoolInitiatorsAssigned_Object = MibTableColumn
cucsFcpoolInitiatorsAssigned = _CucsFcpoolInitiatorsAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 4),
    _CucsFcpoolInitiatorsAssigned_Type()
)
cucsFcpoolInitiatorsAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorsAssigned.setStatus("current")
_CucsFcpoolInitiatorsDescr_Type = SnmpAdminString
_CucsFcpoolInitiatorsDescr_Object = MibTableColumn
cucsFcpoolInitiatorsDescr = _CucsFcpoolInitiatorsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 5),
    _CucsFcpoolInitiatorsDescr_Type()
)
cucsFcpoolInitiatorsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorsDescr.setStatus("current")
_CucsFcpoolInitiatorsIntId_Type = SnmpAdminString
_CucsFcpoolInitiatorsIntId_Object = MibTableColumn
cucsFcpoolInitiatorsIntId = _CucsFcpoolInitiatorsIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 6),
    _CucsFcpoolInitiatorsIntId_Type()
)
cucsFcpoolInitiatorsIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorsIntId.setStatus("current")
_CucsFcpoolInitiatorsName_Type = SnmpAdminString
_CucsFcpoolInitiatorsName_Object = MibTableColumn
cucsFcpoolInitiatorsName = _CucsFcpoolInitiatorsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 7),
    _CucsFcpoolInitiatorsName_Type()
)
cucsFcpoolInitiatorsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorsName.setStatus("current")
_CucsFcpoolInitiatorsPurpose_Type = CucsFcpoolInitiatorsPurpose
_CucsFcpoolInitiatorsPurpose_Object = MibTableColumn
cucsFcpoolInitiatorsPurpose = _CucsFcpoolInitiatorsPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 8),
    _CucsFcpoolInitiatorsPurpose_Type()
)
cucsFcpoolInitiatorsPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorsPurpose.setStatus("current")
_CucsFcpoolInitiatorsSize_Type = Gauge32
_CucsFcpoolInitiatorsSize_Object = MibTableColumn
cucsFcpoolInitiatorsSize = _CucsFcpoolInitiatorsSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 9),
    _CucsFcpoolInitiatorsSize_Type()
)
cucsFcpoolInitiatorsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorsSize.setStatus("current")
_CucsFcpoolInitiatorsAssignmentOrder_Type = CucsFcpoolInitiatorsAssignmentOrder
_CucsFcpoolInitiatorsAssignmentOrder_Object = MibTableColumn
cucsFcpoolInitiatorsAssignmentOrder = _CucsFcpoolInitiatorsAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 10),
    _CucsFcpoolInitiatorsAssignmentOrder_Type()
)
cucsFcpoolInitiatorsAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorsAssignmentOrder.setStatus("current")
_CucsFcpoolInitiatorsMaxPortsPerNode_Type = CucsFcpoolInitiatorsMaxPortsPerNode
_CucsFcpoolInitiatorsMaxPortsPerNode_Object = MibTableColumn
cucsFcpoolInitiatorsMaxPortsPerNode = _CucsFcpoolInitiatorsMaxPortsPerNode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 11),
    _CucsFcpoolInitiatorsMaxPortsPerNode_Type()
)
cucsFcpoolInitiatorsMaxPortsPerNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorsMaxPortsPerNode.setStatus("current")
_CucsFcpoolInitiatorsPolicyLevel_Type = Gauge32
_CucsFcpoolInitiatorsPolicyLevel_Object = MibTableColumn
cucsFcpoolInitiatorsPolicyLevel = _CucsFcpoolInitiatorsPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 12),
    _CucsFcpoolInitiatorsPolicyLevel_Type()
)
cucsFcpoolInitiatorsPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorsPolicyLevel.setStatus("current")
_CucsFcpoolInitiatorsPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsFcpoolInitiatorsPolicyOwner_Object = MibTableColumn
cucsFcpoolInitiatorsPolicyOwner = _CucsFcpoolInitiatorsPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 13),
    _CucsFcpoolInitiatorsPolicyOwner_Type()
)
cucsFcpoolInitiatorsPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorsPolicyOwner.setStatus("current")
_CucsFcpoolPoolableTable_Object = MibTable
cucsFcpoolPoolableTable = _CucsFcpoolPoolableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 7)
)
if mibBuilder.loadTexts:
    cucsFcpoolPoolableTable.setStatus("current")
_CucsFcpoolPoolableEntry_Object = MibTableRow
cucsFcpoolPoolableEntry = _CucsFcpoolPoolableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 7, 1)
)
cucsFcpoolPoolableEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolPoolableInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcpoolPoolableEntry.setStatus("current")
_CucsFcpoolPoolableInstanceId_Type = CucsManagedObjectId
_CucsFcpoolPoolableInstanceId_Object = MibTableColumn
cucsFcpoolPoolableInstanceId = _CucsFcpoolPoolableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 7, 1, 1),
    _CucsFcpoolPoolableInstanceId_Type()
)
cucsFcpoolPoolableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcpoolPoolableInstanceId.setStatus("current")
_CucsFcpoolPoolableDn_Type = CucsManagedObjectDn
_CucsFcpoolPoolableDn_Object = MibTableColumn
cucsFcpoolPoolableDn = _CucsFcpoolPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 7, 1, 2),
    _CucsFcpoolPoolableDn_Type()
)
cucsFcpoolPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolPoolableDn.setStatus("current")
_CucsFcpoolPoolableRn_Type = SnmpAdminString
_CucsFcpoolPoolableRn_Object = MibTableColumn
cucsFcpoolPoolableRn = _CucsFcpoolPoolableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 7, 1, 3),
    _CucsFcpoolPoolableRn_Type()
)
cucsFcpoolPoolableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolPoolableRn.setStatus("current")
_CucsFcpoolPoolableId_Type = Unsigned64
_CucsFcpoolPoolableId_Object = MibTableColumn
cucsFcpoolPoolableId = _CucsFcpoolPoolableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 7, 1, 4),
    _CucsFcpoolPoolableId_Type()
)
cucsFcpoolPoolableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolPoolableId.setStatus("current")
_CucsFcpoolPoolablePoolDn_Type = SnmpAdminString
_CucsFcpoolPoolablePoolDn_Object = MibTableColumn
cucsFcpoolPoolablePoolDn = _CucsFcpoolPoolablePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 7, 1, 5),
    _CucsFcpoolPoolablePoolDn_Type()
)
cucsFcpoolPoolablePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolPoolablePoolDn.setStatus("current")
_CucsFcpoolUniverseTable_Object = MibTable
cucsFcpoolUniverseTable = _CucsFcpoolUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 8)
)
if mibBuilder.loadTexts:
    cucsFcpoolUniverseTable.setStatus("current")
_CucsFcpoolUniverseEntry_Object = MibTableRow
cucsFcpoolUniverseEntry = _CucsFcpoolUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 8, 1)
)
cucsFcpoolUniverseEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcpoolUniverseEntry.setStatus("current")
_CucsFcpoolUniverseInstanceId_Type = CucsManagedObjectId
_CucsFcpoolUniverseInstanceId_Object = MibTableColumn
cucsFcpoolUniverseInstanceId = _CucsFcpoolUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 8, 1, 1),
    _CucsFcpoolUniverseInstanceId_Type()
)
cucsFcpoolUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcpoolUniverseInstanceId.setStatus("current")
_CucsFcpoolUniverseDn_Type = CucsManagedObjectDn
_CucsFcpoolUniverseDn_Object = MibTableColumn
cucsFcpoolUniverseDn = _CucsFcpoolUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 8, 1, 2),
    _CucsFcpoolUniverseDn_Type()
)
cucsFcpoolUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolUniverseDn.setStatus("current")
_CucsFcpoolUniverseRn_Type = SnmpAdminString
_CucsFcpoolUniverseRn_Object = MibTableColumn
cucsFcpoolUniverseRn = _CucsFcpoolUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 8, 1, 3),
    _CucsFcpoolUniverseRn_Type()
)
cucsFcpoolUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolUniverseRn.setStatus("current")
_CucsFcpoolInitiatorEpTable_Object = MibTable
cucsFcpoolInitiatorEpTable = _CucsFcpoolInitiatorEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 9)
)
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorEpTable.setStatus("current")
_CucsFcpoolInitiatorEpEntry_Object = MibTableRow
cucsFcpoolInitiatorEpEntry = _CucsFcpoolInitiatorEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 9, 1)
)
cucsFcpoolInitiatorEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolInitiatorEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorEpEntry.setStatus("current")
_CucsFcpoolInitiatorEpInstanceId_Type = CucsManagedObjectId
_CucsFcpoolInitiatorEpInstanceId_Object = MibTableColumn
cucsFcpoolInitiatorEpInstanceId = _CucsFcpoolInitiatorEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 9, 1, 1),
    _CucsFcpoolInitiatorEpInstanceId_Type()
)
cucsFcpoolInitiatorEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorEpInstanceId.setStatus("current")
_CucsFcpoolInitiatorEpDn_Type = CucsManagedObjectDn
_CucsFcpoolInitiatorEpDn_Object = MibTableColumn
cucsFcpoolInitiatorEpDn = _CucsFcpoolInitiatorEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 9, 1, 2),
    _CucsFcpoolInitiatorEpDn_Type()
)
cucsFcpoolInitiatorEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorEpDn.setStatus("current")
_CucsFcpoolInitiatorEpRn_Type = SnmpAdminString
_CucsFcpoolInitiatorEpRn_Object = MibTableColumn
cucsFcpoolInitiatorEpRn = _CucsFcpoolInitiatorEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 9, 1, 3),
    _CucsFcpoolInitiatorEpRn_Type()
)
cucsFcpoolInitiatorEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorEpRn.setStatus("current")
_CucsFcpoolInitiatorEpId_Type = Unsigned64
_CucsFcpoolInitiatorEpId_Object = MibTableColumn
cucsFcpoolInitiatorEpId = _CucsFcpoolInitiatorEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 9, 1, 4),
    _CucsFcpoolInitiatorEpId_Type()
)
cucsFcpoolInitiatorEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorEpId.setStatus("current")
_CucsFcpoolInitiatorEpInitiatorDn_Type = SnmpAdminString
_CucsFcpoolInitiatorEpInitiatorDn_Object = MibTableColumn
cucsFcpoolInitiatorEpInitiatorDn = _CucsFcpoolInitiatorEpInitiatorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 9, 1, 5),
    _CucsFcpoolInitiatorEpInitiatorDn_Type()
)
cucsFcpoolInitiatorEpInitiatorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorEpInitiatorDn.setStatus("current")
_CucsFcpoolInitiatorEpPurpose_Type = CucsFcpoolInitiatorEpPurpose
_CucsFcpoolInitiatorEpPurpose_Object = MibTableColumn
cucsFcpoolInitiatorEpPurpose = _CucsFcpoolInitiatorEpPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 9, 1, 6),
    _CucsFcpoolInitiatorEpPurpose_Type()
)
cucsFcpoolInitiatorEpPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFcpoolInitiatorEpPurpose.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB",
    **{"cucsFcpoolObjects": cucsFcpoolObjects,
       "cucsFcpoolAddrTable": cucsFcpoolAddrTable,
       "cucsFcpoolAddrEntry": cucsFcpoolAddrEntry,
       "cucsFcpoolAddrInstanceId": cucsFcpoolAddrInstanceId,
       "cucsFcpoolAddrDn": cucsFcpoolAddrDn,
       "cucsFcpoolAddrRn": cucsFcpoolAddrRn,
       "cucsFcpoolAddrAssigned": cucsFcpoolAddrAssigned,
       "cucsFcpoolAddrAssignedToDn": cucsFcpoolAddrAssignedToDn,
       "cucsFcpoolAddrId": cucsFcpoolAddrId,
       "cucsFcpoolAddrOwner": cucsFcpoolAddrOwner,
       "cucsFcpoolAddrGlobalAssignedCnt": cucsFcpoolAddrGlobalAssignedCnt,
       "cucsFcpoolAddrGlobalDefinedCnt": cucsFcpoolAddrGlobalDefinedCnt,
       "cucsFcpoolBlockTable": cucsFcpoolBlockTable,
       "cucsFcpoolBlockEntry": cucsFcpoolBlockEntry,
       "cucsFcpoolBlockInstanceId": cucsFcpoolBlockInstanceId,
       "cucsFcpoolBlockDn": cucsFcpoolBlockDn,
       "cucsFcpoolBlockRn": cucsFcpoolBlockRn,
       "cucsFcpoolBlockFrom": cucsFcpoolBlockFrom,
       "cucsFcpoolBlockTo": cucsFcpoolBlockTo,
       "cucsFcpoolBootTargetTable": cucsFcpoolBootTargetTable,
       "cucsFcpoolBootTargetEntry": cucsFcpoolBootTargetEntry,
       "cucsFcpoolBootTargetInstanceId": cucsFcpoolBootTargetInstanceId,
       "cucsFcpoolBootTargetDn": cucsFcpoolBootTargetDn,
       "cucsFcpoolBootTargetRn": cucsFcpoolBootTargetRn,
       "cucsFcpoolBootTargetLun": cucsFcpoolBootTargetLun,
       "cucsFcpoolBootTargetType": cucsFcpoolBootTargetType,
       "cucsFcpoolBootTargetWwn": cucsFcpoolBootTargetWwn,
       "cucsFcpoolFormatTable": cucsFcpoolFormatTable,
       "cucsFcpoolFormatEntry": cucsFcpoolFormatEntry,
       "cucsFcpoolFormatInstanceId": cucsFcpoolFormatInstanceId,
       "cucsFcpoolFormatDn": cucsFcpoolFormatDn,
       "cucsFcpoolFormatRn": cucsFcpoolFormatRn,
       "cucsFcpoolFormatFormat": cucsFcpoolFormatFormat,
       "cucsFcpoolFormatMask": cucsFcpoolFormatMask,
       "cucsFcpoolInitiatorTable": cucsFcpoolInitiatorTable,
       "cucsFcpoolInitiatorEntry": cucsFcpoolInitiatorEntry,
       "cucsFcpoolInitiatorInstanceId": cucsFcpoolInitiatorInstanceId,
       "cucsFcpoolInitiatorDn": cucsFcpoolInitiatorDn,
       "cucsFcpoolInitiatorRn": cucsFcpoolInitiatorRn,
       "cucsFcpoolInitiatorAssigned": cucsFcpoolInitiatorAssigned,
       "cucsFcpoolInitiatorAssignedToDn": cucsFcpoolInitiatorAssignedToDn,
       "cucsFcpoolInitiatorDescr": cucsFcpoolInitiatorDescr,
       "cucsFcpoolInitiatorId": cucsFcpoolInitiatorId,
       "cucsFcpoolInitiatorName": cucsFcpoolInitiatorName,
       "cucsFcpoolInitiatorPoolableDn": cucsFcpoolInitiatorPoolableDn,
       "cucsFcpoolInitiatorPrevAssignedToDn": cucsFcpoolInitiatorPrevAssignedToDn,
       "cucsFcpoolInitiatorPurpose": cucsFcpoolInitiatorPurpose,
       "cucsFcpoolInitiatorsTable": cucsFcpoolInitiatorsTable,
       "cucsFcpoolInitiatorsEntry": cucsFcpoolInitiatorsEntry,
       "cucsFcpoolInitiatorsInstanceId": cucsFcpoolInitiatorsInstanceId,
       "cucsFcpoolInitiatorsDn": cucsFcpoolInitiatorsDn,
       "cucsFcpoolInitiatorsRn": cucsFcpoolInitiatorsRn,
       "cucsFcpoolInitiatorsAssigned": cucsFcpoolInitiatorsAssigned,
       "cucsFcpoolInitiatorsDescr": cucsFcpoolInitiatorsDescr,
       "cucsFcpoolInitiatorsIntId": cucsFcpoolInitiatorsIntId,
       "cucsFcpoolInitiatorsName": cucsFcpoolInitiatorsName,
       "cucsFcpoolInitiatorsPurpose": cucsFcpoolInitiatorsPurpose,
       "cucsFcpoolInitiatorsSize": cucsFcpoolInitiatorsSize,
       "cucsFcpoolInitiatorsAssignmentOrder": cucsFcpoolInitiatorsAssignmentOrder,
       "cucsFcpoolInitiatorsMaxPortsPerNode": cucsFcpoolInitiatorsMaxPortsPerNode,
       "cucsFcpoolInitiatorsPolicyLevel": cucsFcpoolInitiatorsPolicyLevel,
       "cucsFcpoolInitiatorsPolicyOwner": cucsFcpoolInitiatorsPolicyOwner,
       "cucsFcpoolPoolableTable": cucsFcpoolPoolableTable,
       "cucsFcpoolPoolableEntry": cucsFcpoolPoolableEntry,
       "cucsFcpoolPoolableInstanceId": cucsFcpoolPoolableInstanceId,
       "cucsFcpoolPoolableDn": cucsFcpoolPoolableDn,
       "cucsFcpoolPoolableRn": cucsFcpoolPoolableRn,
       "cucsFcpoolPoolableId": cucsFcpoolPoolableId,
       "cucsFcpoolPoolablePoolDn": cucsFcpoolPoolablePoolDn,
       "cucsFcpoolUniverseTable": cucsFcpoolUniverseTable,
       "cucsFcpoolUniverseEntry": cucsFcpoolUniverseEntry,
       "cucsFcpoolUniverseInstanceId": cucsFcpoolUniverseInstanceId,
       "cucsFcpoolUniverseDn": cucsFcpoolUniverseDn,
       "cucsFcpoolUniverseRn": cucsFcpoolUniverseRn,
       "cucsFcpoolInitiatorEpTable": cucsFcpoolInitiatorEpTable,
       "cucsFcpoolInitiatorEpEntry": cucsFcpoolInitiatorEpEntry,
       "cucsFcpoolInitiatorEpInstanceId": cucsFcpoolInitiatorEpInstanceId,
       "cucsFcpoolInitiatorEpDn": cucsFcpoolInitiatorEpDn,
       "cucsFcpoolInitiatorEpRn": cucsFcpoolInitiatorEpRn,
       "cucsFcpoolInitiatorEpId": cucsFcpoolInitiatorEpId,
       "cucsFcpoolInitiatorEpInitiatorDn": cucsFcpoolInitiatorEpInitiatorDn,
       "cucsFcpoolInitiatorEpPurpose": cucsFcpoolInitiatorEpPurpose}
)
