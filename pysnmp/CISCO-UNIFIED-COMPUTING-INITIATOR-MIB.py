# SNMP MIB module (CISCO-UNIFIED-COMPUTING-INITIATOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-INITIATOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:43 2024
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

(CucsFsmLifecycle,
 CucsInitiatorFcInitiatorEpProt,
 CucsInitiatorGroupType,
 CucsInitiatorIScsiInitiatorEpProt,
 CucsInitiatorInitiatorEpPref,
 CucsStorageAllocState,
 CucsStoragePathHA,
 CucsStorageProtocol) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsFsmLifecycle",
    "CucsInitiatorFcInitiatorEpProt",
    "CucsInitiatorGroupType",
    "CucsInitiatorIScsiInitiatorEpProt",
    "CucsInitiatorInitiatorEpPref",
    "CucsStorageAllocState",
    "CucsStoragePathHA",
    "CucsStorageProtocol")

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

cucsInitiatorObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsInitiatorFcInitiatorEpTable_Object = MibTable
cucsInitiatorFcInitiatorEpTable = _CucsInitiatorFcInitiatorEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 1)
)
if mibBuilder.loadTexts:
    cucsInitiatorFcInitiatorEpTable.setStatus("current")
_CucsInitiatorFcInitiatorEpEntry_Object = MibTableRow
cucsInitiatorFcInitiatorEpEntry = _CucsInitiatorFcInitiatorEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 1, 1)
)
cucsInitiatorFcInitiatorEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-INITIATOR-MIB", "cucsInitiatorFcInitiatorEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsInitiatorFcInitiatorEpEntry.setStatus("current")
_CucsInitiatorFcInitiatorEpInstanceId_Type = CucsManagedObjectId
_CucsInitiatorFcInitiatorEpInstanceId_Object = MibTableColumn
cucsInitiatorFcInitiatorEpInstanceId = _CucsInitiatorFcInitiatorEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 1, 1, 1),
    _CucsInitiatorFcInitiatorEpInstanceId_Type()
)
cucsInitiatorFcInitiatorEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsInitiatorFcInitiatorEpInstanceId.setStatus("current")
_CucsInitiatorFcInitiatorEpDn_Type = CucsManagedObjectDn
_CucsInitiatorFcInitiatorEpDn_Object = MibTableColumn
cucsInitiatorFcInitiatorEpDn = _CucsInitiatorFcInitiatorEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 1, 1, 2),
    _CucsInitiatorFcInitiatorEpDn_Type()
)
cucsInitiatorFcInitiatorEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorFcInitiatorEpDn.setStatus("current")
_CucsInitiatorFcInitiatorEpRn_Type = SnmpAdminString
_CucsInitiatorFcInitiatorEpRn_Object = MibTableColumn
cucsInitiatorFcInitiatorEpRn = _CucsInitiatorFcInitiatorEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 1, 1, 3),
    _CucsInitiatorFcInitiatorEpRn_Type()
)
cucsInitiatorFcInitiatorEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorFcInitiatorEpRn.setStatus("current")
_CucsInitiatorFcInitiatorEpEpDn_Type = SnmpAdminString
_CucsInitiatorFcInitiatorEpEpDn_Object = MibTableColumn
cucsInitiatorFcInitiatorEpEpDn = _CucsInitiatorFcInitiatorEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 1, 1, 4),
    _CucsInitiatorFcInitiatorEpEpDn_Type()
)
cucsInitiatorFcInitiatorEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorFcInitiatorEpEpDn.setStatus("current")
_CucsInitiatorFcInitiatorEpId_Type = Unsigned64
_CucsInitiatorFcInitiatorEpId_Object = MibTableColumn
cucsInitiatorFcInitiatorEpId = _CucsInitiatorFcInitiatorEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 1, 1, 5),
    _CucsInitiatorFcInitiatorEpId_Type()
)
cucsInitiatorFcInitiatorEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorFcInitiatorEpId.setStatus("current")
_CucsInitiatorFcInitiatorEpName_Type = SnmpAdminString
_CucsInitiatorFcInitiatorEpName_Object = MibTableColumn
cucsInitiatorFcInitiatorEpName = _CucsInitiatorFcInitiatorEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 1, 1, 6),
    _CucsInitiatorFcInitiatorEpName_Type()
)
cucsInitiatorFcInitiatorEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorFcInitiatorEpName.setStatus("current")
_CucsInitiatorFcInitiatorEpPref_Type = CucsInitiatorInitiatorEpPref
_CucsInitiatorFcInitiatorEpPref_Object = MibTableColumn
cucsInitiatorFcInitiatorEpPref = _CucsInitiatorFcInitiatorEpPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 1, 1, 7),
    _CucsInitiatorFcInitiatorEpPref_Type()
)
cucsInitiatorFcInitiatorEpPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorFcInitiatorEpPref.setStatus("current")
_CucsInitiatorFcInitiatorEpProt_Type = CucsInitiatorFcInitiatorEpProt
_CucsInitiatorFcInitiatorEpProt_Object = MibTableColumn
cucsInitiatorFcInitiatorEpProt = _CucsInitiatorFcInitiatorEpProt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 1, 1, 8),
    _CucsInitiatorFcInitiatorEpProt_Type()
)
cucsInitiatorFcInitiatorEpProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorFcInitiatorEpProt.setStatus("current")
_CucsInitiatorFcInitiatorEpWwpn_Type = Unsigned64
_CucsInitiatorFcInitiatorEpWwpn_Object = MibTableColumn
cucsInitiatorFcInitiatorEpWwpn = _CucsInitiatorFcInitiatorEpWwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 1, 1, 9),
    _CucsInitiatorFcInitiatorEpWwpn_Type()
)
cucsInitiatorFcInitiatorEpWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorFcInitiatorEpWwpn.setStatus("current")
_CucsInitiatorGroupEpTable_Object = MibTable
cucsInitiatorGroupEpTable = _CucsInitiatorGroupEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 2)
)
if mibBuilder.loadTexts:
    cucsInitiatorGroupEpTable.setStatus("current")
_CucsInitiatorGroupEpEntry_Object = MibTableRow
cucsInitiatorGroupEpEntry = _CucsInitiatorGroupEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 2, 1)
)
cucsInitiatorGroupEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-INITIATOR-MIB", "cucsInitiatorGroupEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsInitiatorGroupEpEntry.setStatus("current")
_CucsInitiatorGroupEpInstanceId_Type = CucsManagedObjectId
_CucsInitiatorGroupEpInstanceId_Object = MibTableColumn
cucsInitiatorGroupEpInstanceId = _CucsInitiatorGroupEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 2, 1, 1),
    _CucsInitiatorGroupEpInstanceId_Type()
)
cucsInitiatorGroupEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsInitiatorGroupEpInstanceId.setStatus("current")
_CucsInitiatorGroupEpDn_Type = CucsManagedObjectDn
_CucsInitiatorGroupEpDn_Object = MibTableColumn
cucsInitiatorGroupEpDn = _CucsInitiatorGroupEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 2, 1, 2),
    _CucsInitiatorGroupEpDn_Type()
)
cucsInitiatorGroupEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorGroupEpDn.setStatus("current")
_CucsInitiatorGroupEpRn_Type = SnmpAdminString
_CucsInitiatorGroupEpRn_Object = MibTableColumn
cucsInitiatorGroupEpRn = _CucsInitiatorGroupEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 2, 1, 3),
    _CucsInitiatorGroupEpRn_Type()
)
cucsInitiatorGroupEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorGroupEpRn.setStatus("current")
_CucsInitiatorGroupEpEpDn_Type = SnmpAdminString
_CucsInitiatorGroupEpEpDn_Object = MibTableColumn
cucsInitiatorGroupEpEpDn = _CucsInitiatorGroupEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 2, 1, 4),
    _CucsInitiatorGroupEpEpDn_Type()
)
cucsInitiatorGroupEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorGroupEpEpDn.setStatus("current")
_CucsInitiatorGroupEpId_Type = Gauge32
_CucsInitiatorGroupEpId_Object = MibTableColumn
cucsInitiatorGroupEpId = _CucsInitiatorGroupEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 2, 1, 5),
    _CucsInitiatorGroupEpId_Type()
)
cucsInitiatorGroupEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorGroupEpId.setStatus("current")
_CucsInitiatorGroupEpLc_Type = CucsFsmLifecycle
_CucsInitiatorGroupEpLc_Object = MibTableColumn
cucsInitiatorGroupEpLc = _CucsInitiatorGroupEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 2, 1, 6),
    _CucsInitiatorGroupEpLc_Type()
)
cucsInitiatorGroupEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorGroupEpLc.setStatus("current")
_CucsInitiatorGroupEpName_Type = SnmpAdminString
_CucsInitiatorGroupEpName_Object = MibTableColumn
cucsInitiatorGroupEpName = _CucsInitiatorGroupEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 2, 1, 7),
    _CucsInitiatorGroupEpName_Type()
)
cucsInitiatorGroupEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorGroupEpName.setStatus("current")
_CucsInitiatorGroupEpPolName_Type = SnmpAdminString
_CucsInitiatorGroupEpPolName_Object = MibTableColumn
cucsInitiatorGroupEpPolName = _CucsInitiatorGroupEpPolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 2, 1, 8),
    _CucsInitiatorGroupEpPolName_Type()
)
cucsInitiatorGroupEpPolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorGroupEpPolName.setStatus("current")
_CucsInitiatorGroupEpRmtDiskCfgName_Type = SnmpAdminString
_CucsInitiatorGroupEpRmtDiskCfgName_Object = MibTableColumn
cucsInitiatorGroupEpRmtDiskCfgName = _CucsInitiatorGroupEpRmtDiskCfgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 2, 1, 9),
    _CucsInitiatorGroupEpRmtDiskCfgName_Type()
)
cucsInitiatorGroupEpRmtDiskCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorGroupEpRmtDiskCfgName.setStatus("current")
_CucsInitiatorIScsiInitiatorEpTable_Object = MibTable
cucsInitiatorIScsiInitiatorEpTable = _CucsInitiatorIScsiInitiatorEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 3)
)
if mibBuilder.loadTexts:
    cucsInitiatorIScsiInitiatorEpTable.setStatus("current")
_CucsInitiatorIScsiInitiatorEpEntry_Object = MibTableRow
cucsInitiatorIScsiInitiatorEpEntry = _CucsInitiatorIScsiInitiatorEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 3, 1)
)
cucsInitiatorIScsiInitiatorEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-INITIATOR-MIB", "cucsInitiatorIScsiInitiatorEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsInitiatorIScsiInitiatorEpEntry.setStatus("current")
_CucsInitiatorIScsiInitiatorEpInstanceId_Type = CucsManagedObjectId
_CucsInitiatorIScsiInitiatorEpInstanceId_Object = MibTableColumn
cucsInitiatorIScsiInitiatorEpInstanceId = _CucsInitiatorIScsiInitiatorEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 3, 1, 1),
    _CucsInitiatorIScsiInitiatorEpInstanceId_Type()
)
cucsInitiatorIScsiInitiatorEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsInitiatorIScsiInitiatorEpInstanceId.setStatus("current")
_CucsInitiatorIScsiInitiatorEpDn_Type = CucsManagedObjectDn
_CucsInitiatorIScsiInitiatorEpDn_Object = MibTableColumn
cucsInitiatorIScsiInitiatorEpDn = _CucsInitiatorIScsiInitiatorEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 3, 1, 2),
    _CucsInitiatorIScsiInitiatorEpDn_Type()
)
cucsInitiatorIScsiInitiatorEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorIScsiInitiatorEpDn.setStatus("current")
_CucsInitiatorIScsiInitiatorEpRn_Type = SnmpAdminString
_CucsInitiatorIScsiInitiatorEpRn_Object = MibTableColumn
cucsInitiatorIScsiInitiatorEpRn = _CucsInitiatorIScsiInitiatorEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 3, 1, 3),
    _CucsInitiatorIScsiInitiatorEpRn_Type()
)
cucsInitiatorIScsiInitiatorEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorIScsiInitiatorEpRn.setStatus("current")
_CucsInitiatorIScsiInitiatorEpEpDn_Type = SnmpAdminString
_CucsInitiatorIScsiInitiatorEpEpDn_Object = MibTableColumn
cucsInitiatorIScsiInitiatorEpEpDn = _CucsInitiatorIScsiInitiatorEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 3, 1, 4),
    _CucsInitiatorIScsiInitiatorEpEpDn_Type()
)
cucsInitiatorIScsiInitiatorEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorIScsiInitiatorEpEpDn.setStatus("current")
_CucsInitiatorIScsiInitiatorEpId_Type = Unsigned64
_CucsInitiatorIScsiInitiatorEpId_Object = MibTableColumn
cucsInitiatorIScsiInitiatorEpId = _CucsInitiatorIScsiInitiatorEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 3, 1, 5),
    _CucsInitiatorIScsiInitiatorEpId_Type()
)
cucsInitiatorIScsiInitiatorEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorIScsiInitiatorEpId.setStatus("current")
_CucsInitiatorIScsiInitiatorEpIqn_Type = SnmpAdminString
_CucsInitiatorIScsiInitiatorEpIqn_Object = MibTableColumn
cucsInitiatorIScsiInitiatorEpIqn = _CucsInitiatorIScsiInitiatorEpIqn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 3, 1, 6),
    _CucsInitiatorIScsiInitiatorEpIqn_Type()
)
cucsInitiatorIScsiInitiatorEpIqn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorIScsiInitiatorEpIqn.setStatus("current")
_CucsInitiatorIScsiInitiatorEpName_Type = SnmpAdminString
_CucsInitiatorIScsiInitiatorEpName_Object = MibTableColumn
cucsInitiatorIScsiInitiatorEpName = _CucsInitiatorIScsiInitiatorEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 3, 1, 7),
    _CucsInitiatorIScsiInitiatorEpName_Type()
)
cucsInitiatorIScsiInitiatorEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorIScsiInitiatorEpName.setStatus("current")
_CucsInitiatorIScsiInitiatorEpPref_Type = CucsInitiatorInitiatorEpPref
_CucsInitiatorIScsiInitiatorEpPref_Object = MibTableColumn
cucsInitiatorIScsiInitiatorEpPref = _CucsInitiatorIScsiInitiatorEpPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 3, 1, 8),
    _CucsInitiatorIScsiInitiatorEpPref_Type()
)
cucsInitiatorIScsiInitiatorEpPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorIScsiInitiatorEpPref.setStatus("current")
_CucsInitiatorIScsiInitiatorEpProt_Type = CucsInitiatorIScsiInitiatorEpProt
_CucsInitiatorIScsiInitiatorEpProt_Object = MibTableColumn
cucsInitiatorIScsiInitiatorEpProt = _CucsInitiatorIScsiInitiatorEpProt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 3, 1, 9),
    _CucsInitiatorIScsiInitiatorEpProt_Type()
)
cucsInitiatorIScsiInitiatorEpProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorIScsiInitiatorEpProt.setStatus("current")
_CucsInitiatorLunEpTable_Object = MibTable
cucsInitiatorLunEpTable = _CucsInitiatorLunEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 4)
)
if mibBuilder.loadTexts:
    cucsInitiatorLunEpTable.setStatus("current")
_CucsInitiatorLunEpEntry_Object = MibTableRow
cucsInitiatorLunEpEntry = _CucsInitiatorLunEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 4, 1)
)
cucsInitiatorLunEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-INITIATOR-MIB", "cucsInitiatorLunEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsInitiatorLunEpEntry.setStatus("current")
_CucsInitiatorLunEpInstanceId_Type = CucsManagedObjectId
_CucsInitiatorLunEpInstanceId_Object = MibTableColumn
cucsInitiatorLunEpInstanceId = _CucsInitiatorLunEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 4, 1, 1),
    _CucsInitiatorLunEpInstanceId_Type()
)
cucsInitiatorLunEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsInitiatorLunEpInstanceId.setStatus("current")
_CucsInitiatorLunEpDn_Type = CucsManagedObjectDn
_CucsInitiatorLunEpDn_Object = MibTableColumn
cucsInitiatorLunEpDn = _CucsInitiatorLunEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 4, 1, 2),
    _CucsInitiatorLunEpDn_Type()
)
cucsInitiatorLunEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorLunEpDn.setStatus("current")
_CucsInitiatorLunEpRn_Type = SnmpAdminString
_CucsInitiatorLunEpRn_Object = MibTableColumn
cucsInitiatorLunEpRn = _CucsInitiatorLunEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 4, 1, 3),
    _CucsInitiatorLunEpRn_Type()
)
cucsInitiatorLunEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorLunEpRn.setStatus("current")
_CucsInitiatorLunEpBootable_Type = TruthValue
_CucsInitiatorLunEpBootable_Object = MibTableColumn
cucsInitiatorLunEpBootable = _CucsInitiatorLunEpBootable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 4, 1, 4),
    _CucsInitiatorLunEpBootable_Type()
)
cucsInitiatorLunEpBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorLunEpBootable.setStatus("current")
_CucsInitiatorLunEpEpDn_Type = SnmpAdminString
_CucsInitiatorLunEpEpDn_Object = MibTableColumn
cucsInitiatorLunEpEpDn = _CucsInitiatorLunEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 4, 1, 5),
    _CucsInitiatorLunEpEpDn_Type()
)
cucsInitiatorLunEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorLunEpEpDn.setStatus("current")
_CucsInitiatorLunEpId_Type = Gauge32
_CucsInitiatorLunEpId_Object = MibTableColumn
cucsInitiatorLunEpId = _CucsInitiatorLunEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 4, 1, 6),
    _CucsInitiatorLunEpId_Type()
)
cucsInitiatorLunEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorLunEpId.setStatus("current")
_CucsInitiatorMemberEpTable_Object = MibTable
cucsInitiatorMemberEpTable = _CucsInitiatorMemberEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 5)
)
if mibBuilder.loadTexts:
    cucsInitiatorMemberEpTable.setStatus("current")
_CucsInitiatorMemberEpEntry_Object = MibTableRow
cucsInitiatorMemberEpEntry = _CucsInitiatorMemberEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 5, 1)
)
cucsInitiatorMemberEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-INITIATOR-MIB", "cucsInitiatorMemberEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsInitiatorMemberEpEntry.setStatus("current")
_CucsInitiatorMemberEpInstanceId_Type = CucsManagedObjectId
_CucsInitiatorMemberEpInstanceId_Object = MibTableColumn
cucsInitiatorMemberEpInstanceId = _CucsInitiatorMemberEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 5, 1, 1),
    _CucsInitiatorMemberEpInstanceId_Type()
)
cucsInitiatorMemberEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsInitiatorMemberEpInstanceId.setStatus("current")
_CucsInitiatorMemberEpDn_Type = CucsManagedObjectDn
_CucsInitiatorMemberEpDn_Object = MibTableColumn
cucsInitiatorMemberEpDn = _CucsInitiatorMemberEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 5, 1, 2),
    _CucsInitiatorMemberEpDn_Type()
)
cucsInitiatorMemberEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorMemberEpDn.setStatus("current")
_CucsInitiatorMemberEpRn_Type = SnmpAdminString
_CucsInitiatorMemberEpRn_Object = MibTableColumn
cucsInitiatorMemberEpRn = _CucsInitiatorMemberEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 5, 1, 3),
    _CucsInitiatorMemberEpRn_Type()
)
cucsInitiatorMemberEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorMemberEpRn.setStatus("current")
_CucsInitiatorMemberEpEpDn_Type = SnmpAdminString
_CucsInitiatorMemberEpEpDn_Object = MibTableColumn
cucsInitiatorMemberEpEpDn = _CucsInitiatorMemberEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 5, 1, 4),
    _CucsInitiatorMemberEpEpDn_Type()
)
cucsInitiatorMemberEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorMemberEpEpDn.setStatus("current")
_CucsInitiatorMemberEpId_Type = Gauge32
_CucsInitiatorMemberEpId_Object = MibTableColumn
cucsInitiatorMemberEpId = _CucsInitiatorMemberEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 5, 1, 5),
    _CucsInitiatorMemberEpId_Type()
)
cucsInitiatorMemberEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorMemberEpId.setStatus("current")
_CucsInitiatorRequestorEpTable_Object = MibTable
cucsInitiatorRequestorEpTable = _CucsInitiatorRequestorEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 6)
)
if mibBuilder.loadTexts:
    cucsInitiatorRequestorEpTable.setStatus("current")
_CucsInitiatorRequestorEpEntry_Object = MibTableRow
cucsInitiatorRequestorEpEntry = _CucsInitiatorRequestorEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 6, 1)
)
cucsInitiatorRequestorEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-INITIATOR-MIB", "cucsInitiatorRequestorEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsInitiatorRequestorEpEntry.setStatus("current")
_CucsInitiatorRequestorEpInstanceId_Type = CucsManagedObjectId
_CucsInitiatorRequestorEpInstanceId_Object = MibTableColumn
cucsInitiatorRequestorEpInstanceId = _CucsInitiatorRequestorEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 6, 1, 1),
    _CucsInitiatorRequestorEpInstanceId_Type()
)
cucsInitiatorRequestorEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsInitiatorRequestorEpInstanceId.setStatus("current")
_CucsInitiatorRequestorEpDn_Type = CucsManagedObjectDn
_CucsInitiatorRequestorEpDn_Object = MibTableColumn
cucsInitiatorRequestorEpDn = _CucsInitiatorRequestorEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 6, 1, 2),
    _CucsInitiatorRequestorEpDn_Type()
)
cucsInitiatorRequestorEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorRequestorEpDn.setStatus("current")
_CucsInitiatorRequestorEpRn_Type = SnmpAdminString
_CucsInitiatorRequestorEpRn_Object = MibTableColumn
cucsInitiatorRequestorEpRn = _CucsInitiatorRequestorEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 6, 1, 3),
    _CucsInitiatorRequestorEpRn_Type()
)
cucsInitiatorRequestorEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorRequestorEpRn.setStatus("current")
_CucsInitiatorRequestorEpAllocState_Type = CucsStorageAllocState
_CucsInitiatorRequestorEpAllocState_Object = MibTableColumn
cucsInitiatorRequestorEpAllocState = _CucsInitiatorRequestorEpAllocState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 6, 1, 4),
    _CucsInitiatorRequestorEpAllocState_Type()
)
cucsInitiatorRequestorEpAllocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorRequestorEpAllocState.setStatus("current")
_CucsInitiatorRequestorEpEpDn_Type = SnmpAdminString
_CucsInitiatorRequestorEpEpDn_Object = MibTableColumn
cucsInitiatorRequestorEpEpDn = _CucsInitiatorRequestorEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 6, 1, 5),
    _CucsInitiatorRequestorEpEpDn_Type()
)
cucsInitiatorRequestorEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorRequestorEpEpDn.setStatus("current")
_CucsInitiatorRequestorEpId_Type = Gauge32
_CucsInitiatorRequestorEpId_Object = MibTableColumn
cucsInitiatorRequestorEpId = _CucsInitiatorRequestorEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 6, 1, 6),
    _CucsInitiatorRequestorEpId_Type()
)
cucsInitiatorRequestorEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorRequestorEpId.setStatus("current")
_CucsInitiatorRequestorEpSysId_Type = Gauge32
_CucsInitiatorRequestorEpSysId_Object = MibTableColumn
cucsInitiatorRequestorEpSysId = _CucsInitiatorRequestorEpSysId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 6, 1, 7),
    _CucsInitiatorRequestorEpSysId_Type()
)
cucsInitiatorRequestorEpSysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorRequestorEpSysId.setStatus("current")
_CucsInitiatorRequestorEpSysName_Type = SnmpAdminString
_CucsInitiatorRequestorEpSysName_Object = MibTableColumn
cucsInitiatorRequestorEpSysName = _CucsInitiatorRequestorEpSysName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 6, 1, 8),
    _CucsInitiatorRequestorEpSysName_Type()
)
cucsInitiatorRequestorEpSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorRequestorEpSysName.setStatus("current")
_CucsInitiatorRequestorGrpEpTable_Object = MibTable
cucsInitiatorRequestorGrpEpTable = _CucsInitiatorRequestorGrpEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 7)
)
if mibBuilder.loadTexts:
    cucsInitiatorRequestorGrpEpTable.setStatus("current")
_CucsInitiatorRequestorGrpEpEntry_Object = MibTableRow
cucsInitiatorRequestorGrpEpEntry = _CucsInitiatorRequestorGrpEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 7, 1)
)
cucsInitiatorRequestorGrpEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-INITIATOR-MIB", "cucsInitiatorRequestorGrpEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsInitiatorRequestorGrpEpEntry.setStatus("current")
_CucsInitiatorRequestorGrpEpInstanceId_Type = CucsManagedObjectId
_CucsInitiatorRequestorGrpEpInstanceId_Object = MibTableColumn
cucsInitiatorRequestorGrpEpInstanceId = _CucsInitiatorRequestorGrpEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 7, 1, 1),
    _CucsInitiatorRequestorGrpEpInstanceId_Type()
)
cucsInitiatorRequestorGrpEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsInitiatorRequestorGrpEpInstanceId.setStatus("current")
_CucsInitiatorRequestorGrpEpDn_Type = CucsManagedObjectDn
_CucsInitiatorRequestorGrpEpDn_Object = MibTableColumn
cucsInitiatorRequestorGrpEpDn = _CucsInitiatorRequestorGrpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 7, 1, 2),
    _CucsInitiatorRequestorGrpEpDn_Type()
)
cucsInitiatorRequestorGrpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorRequestorGrpEpDn.setStatus("current")
_CucsInitiatorRequestorGrpEpRn_Type = SnmpAdminString
_CucsInitiatorRequestorGrpEpRn_Object = MibTableColumn
cucsInitiatorRequestorGrpEpRn = _CucsInitiatorRequestorGrpEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 7, 1, 3),
    _CucsInitiatorRequestorGrpEpRn_Type()
)
cucsInitiatorRequestorGrpEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorRequestorGrpEpRn.setStatus("current")
_CucsInitiatorRequestorGrpEpAllocState_Type = CucsStorageAllocState
_CucsInitiatorRequestorGrpEpAllocState_Object = MibTableColumn
cucsInitiatorRequestorGrpEpAllocState = _CucsInitiatorRequestorGrpEpAllocState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 7, 1, 4),
    _CucsInitiatorRequestorGrpEpAllocState_Type()
)
cucsInitiatorRequestorGrpEpAllocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorRequestorGrpEpAllocState.setStatus("current")
_CucsInitiatorRequestorGrpEpEpDn_Type = SnmpAdminString
_CucsInitiatorRequestorGrpEpEpDn_Object = MibTableColumn
cucsInitiatorRequestorGrpEpEpDn = _CucsInitiatorRequestorGrpEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 7, 1, 5),
    _CucsInitiatorRequestorGrpEpEpDn_Type()
)
cucsInitiatorRequestorGrpEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorRequestorGrpEpEpDn.setStatus("current")
_CucsInitiatorRequestorGrpEpId_Type = Gauge32
_CucsInitiatorRequestorGrpEpId_Object = MibTableColumn
cucsInitiatorRequestorGrpEpId = _CucsInitiatorRequestorGrpEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 7, 1, 6),
    _CucsInitiatorRequestorGrpEpId_Type()
)
cucsInitiatorRequestorGrpEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorRequestorGrpEpId.setStatus("current")
_CucsInitiatorRequestorGrpEpLc_Type = CucsFsmLifecycle
_CucsInitiatorRequestorGrpEpLc_Object = MibTableColumn
cucsInitiatorRequestorGrpEpLc = _CucsInitiatorRequestorGrpEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 7, 1, 7),
    _CucsInitiatorRequestorGrpEpLc_Type()
)
cucsInitiatorRequestorGrpEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorRequestorGrpEpLc.setStatus("current")
_CucsInitiatorRequestorGrpEpPolDn_Type = SnmpAdminString
_CucsInitiatorRequestorGrpEpPolDn_Object = MibTableColumn
cucsInitiatorRequestorGrpEpPolDn = _CucsInitiatorRequestorGrpEpPolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 7, 1, 8),
    _CucsInitiatorRequestorGrpEpPolDn_Type()
)
cucsInitiatorRequestorGrpEpPolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorRequestorGrpEpPolDn.setStatus("current")
_CucsInitiatorRequestorGrpEpType_Type = CucsInitiatorGroupType
_CucsInitiatorRequestorGrpEpType_Object = MibTableColumn
cucsInitiatorRequestorGrpEpType = _CucsInitiatorRequestorGrpEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 7, 1, 9),
    _CucsInitiatorRequestorGrpEpType_Type()
)
cucsInitiatorRequestorGrpEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorRequestorGrpEpType.setStatus("current")
_CucsInitiatorStoreEpTable_Object = MibTable
cucsInitiatorStoreEpTable = _CucsInitiatorStoreEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 8)
)
if mibBuilder.loadTexts:
    cucsInitiatorStoreEpTable.setStatus("current")
_CucsInitiatorStoreEpEntry_Object = MibTableRow
cucsInitiatorStoreEpEntry = _CucsInitiatorStoreEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 8, 1)
)
cucsInitiatorStoreEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-INITIATOR-MIB", "cucsInitiatorStoreEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsInitiatorStoreEpEntry.setStatus("current")
_CucsInitiatorStoreEpInstanceId_Type = CucsManagedObjectId
_CucsInitiatorStoreEpInstanceId_Object = MibTableColumn
cucsInitiatorStoreEpInstanceId = _CucsInitiatorStoreEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 8, 1, 1),
    _CucsInitiatorStoreEpInstanceId_Type()
)
cucsInitiatorStoreEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsInitiatorStoreEpInstanceId.setStatus("current")
_CucsInitiatorStoreEpDn_Type = CucsManagedObjectDn
_CucsInitiatorStoreEpDn_Object = MibTableColumn
cucsInitiatorStoreEpDn = _CucsInitiatorStoreEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 8, 1, 2),
    _CucsInitiatorStoreEpDn_Type()
)
cucsInitiatorStoreEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorStoreEpDn.setStatus("current")
_CucsInitiatorStoreEpRn_Type = SnmpAdminString
_CucsInitiatorStoreEpRn_Object = MibTableColumn
cucsInitiatorStoreEpRn = _CucsInitiatorStoreEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 8, 1, 3),
    _CucsInitiatorStoreEpRn_Type()
)
cucsInitiatorStoreEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorStoreEpRn.setStatus("current")
_CucsInitiatorStoreEpEpDn_Type = SnmpAdminString
_CucsInitiatorStoreEpEpDn_Object = MibTableColumn
cucsInitiatorStoreEpEpDn = _CucsInitiatorStoreEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 8, 1, 4),
    _CucsInitiatorStoreEpEpDn_Type()
)
cucsInitiatorStoreEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorStoreEpEpDn.setStatus("current")
_CucsInitiatorStoreEpId_Type = Gauge32
_CucsInitiatorStoreEpId_Object = MibTableColumn
cucsInitiatorStoreEpId = _CucsInitiatorStoreEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 8, 1, 5),
    _CucsInitiatorStoreEpId_Type()
)
cucsInitiatorStoreEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorStoreEpId.setStatus("current")
_CucsInitiatorStoreEpType_Type = CucsInitiatorGroupType
_CucsInitiatorStoreEpType_Object = MibTableColumn
cucsInitiatorStoreEpType = _CucsInitiatorStoreEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 8, 1, 6),
    _CucsInitiatorStoreEpType_Type()
)
cucsInitiatorStoreEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorStoreEpType.setStatus("current")
_CucsInitiatorUnitEpTable_Object = MibTable
cucsInitiatorUnitEpTable = _CucsInitiatorUnitEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 9)
)
if mibBuilder.loadTexts:
    cucsInitiatorUnitEpTable.setStatus("current")
_CucsInitiatorUnitEpEntry_Object = MibTableRow
cucsInitiatorUnitEpEntry = _CucsInitiatorUnitEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 9, 1)
)
cucsInitiatorUnitEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-INITIATOR-MIB", "cucsInitiatorUnitEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsInitiatorUnitEpEntry.setStatus("current")
_CucsInitiatorUnitEpInstanceId_Type = CucsManagedObjectId
_CucsInitiatorUnitEpInstanceId_Object = MibTableColumn
cucsInitiatorUnitEpInstanceId = _CucsInitiatorUnitEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 9, 1, 1),
    _CucsInitiatorUnitEpInstanceId_Type()
)
cucsInitiatorUnitEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsInitiatorUnitEpInstanceId.setStatus("current")
_CucsInitiatorUnitEpDn_Type = CucsManagedObjectDn
_CucsInitiatorUnitEpDn_Object = MibTableColumn
cucsInitiatorUnitEpDn = _CucsInitiatorUnitEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 9, 1, 2),
    _CucsInitiatorUnitEpDn_Type()
)
cucsInitiatorUnitEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorUnitEpDn.setStatus("current")
_CucsInitiatorUnitEpRn_Type = SnmpAdminString
_CucsInitiatorUnitEpRn_Object = MibTableColumn
cucsInitiatorUnitEpRn = _CucsInitiatorUnitEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 9, 1, 3),
    _CucsInitiatorUnitEpRn_Type()
)
cucsInitiatorUnitEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorUnitEpRn.setStatus("current")
_CucsInitiatorUnitEpBoot_Type = TruthValue
_CucsInitiatorUnitEpBoot_Object = MibTableColumn
cucsInitiatorUnitEpBoot = _CucsInitiatorUnitEpBoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 9, 1, 4),
    _CucsInitiatorUnitEpBoot_Type()
)
cucsInitiatorUnitEpBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorUnitEpBoot.setStatus("current")
_CucsInitiatorUnitEpEpDn_Type = SnmpAdminString
_CucsInitiatorUnitEpEpDn_Object = MibTableColumn
cucsInitiatorUnitEpEpDn = _CucsInitiatorUnitEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 9, 1, 5),
    _CucsInitiatorUnitEpEpDn_Type()
)
cucsInitiatorUnitEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorUnitEpEpDn.setStatus("current")
_CucsInitiatorUnitEpHa_Type = CucsStoragePathHA
_CucsInitiatorUnitEpHa_Object = MibTableColumn
cucsInitiatorUnitEpHa = _CucsInitiatorUnitEpHa_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 9, 1, 6),
    _CucsInitiatorUnitEpHa_Type()
)
cucsInitiatorUnitEpHa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorUnitEpHa.setStatus("current")
_CucsInitiatorUnitEpId_Type = Gauge32
_CucsInitiatorUnitEpId_Object = MibTableColumn
cucsInitiatorUnitEpId = _CucsInitiatorUnitEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 9, 1, 7),
    _CucsInitiatorUnitEpId_Type()
)
cucsInitiatorUnitEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorUnitEpId.setStatus("current")
_CucsInitiatorUnitEpItemDn_Type = SnmpAdminString
_CucsInitiatorUnitEpItemDn_Object = MibTableColumn
cucsInitiatorUnitEpItemDn = _CucsInitiatorUnitEpItemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 9, 1, 8),
    _CucsInitiatorUnitEpItemDn_Type()
)
cucsInitiatorUnitEpItemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorUnitEpItemDn.setStatus("current")
_CucsInitiatorUnitEpLc_Type = CucsFsmLifecycle
_CucsInitiatorUnitEpLc_Object = MibTableColumn
cucsInitiatorUnitEpLc = _CucsInitiatorUnitEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 9, 1, 9),
    _CucsInitiatorUnitEpLc_Type()
)
cucsInitiatorUnitEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorUnitEpLc.setStatus("current")
_CucsInitiatorUnitEpPhyId_Type = Gauge32
_CucsInitiatorUnitEpPhyId_Object = MibTableColumn
cucsInitiatorUnitEpPhyId = _CucsInitiatorUnitEpPhyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 9, 1, 10),
    _CucsInitiatorUnitEpPhyId_Type()
)
cucsInitiatorUnitEpPhyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorUnitEpPhyId.setStatus("current")
_CucsInitiatorUnitEpProt_Type = CucsStorageProtocol
_CucsInitiatorUnitEpProt_Object = MibTableColumn
cucsInitiatorUnitEpProt = _CucsInitiatorUnitEpProt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 65, 9, 1, 11),
    _CucsInitiatorUnitEpProt_Type()
)
cucsInitiatorUnitEpProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsInitiatorUnitEpProt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-INITIATOR-MIB",
    **{"cucsInitiatorObjects": cucsInitiatorObjects,
       "cucsInitiatorFcInitiatorEpTable": cucsInitiatorFcInitiatorEpTable,
       "cucsInitiatorFcInitiatorEpEntry": cucsInitiatorFcInitiatorEpEntry,
       "cucsInitiatorFcInitiatorEpInstanceId": cucsInitiatorFcInitiatorEpInstanceId,
       "cucsInitiatorFcInitiatorEpDn": cucsInitiatorFcInitiatorEpDn,
       "cucsInitiatorFcInitiatorEpRn": cucsInitiatorFcInitiatorEpRn,
       "cucsInitiatorFcInitiatorEpEpDn": cucsInitiatorFcInitiatorEpEpDn,
       "cucsInitiatorFcInitiatorEpId": cucsInitiatorFcInitiatorEpId,
       "cucsInitiatorFcInitiatorEpName": cucsInitiatorFcInitiatorEpName,
       "cucsInitiatorFcInitiatorEpPref": cucsInitiatorFcInitiatorEpPref,
       "cucsInitiatorFcInitiatorEpProt": cucsInitiatorFcInitiatorEpProt,
       "cucsInitiatorFcInitiatorEpWwpn": cucsInitiatorFcInitiatorEpWwpn,
       "cucsInitiatorGroupEpTable": cucsInitiatorGroupEpTable,
       "cucsInitiatorGroupEpEntry": cucsInitiatorGroupEpEntry,
       "cucsInitiatorGroupEpInstanceId": cucsInitiatorGroupEpInstanceId,
       "cucsInitiatorGroupEpDn": cucsInitiatorGroupEpDn,
       "cucsInitiatorGroupEpRn": cucsInitiatorGroupEpRn,
       "cucsInitiatorGroupEpEpDn": cucsInitiatorGroupEpEpDn,
       "cucsInitiatorGroupEpId": cucsInitiatorGroupEpId,
       "cucsInitiatorGroupEpLc": cucsInitiatorGroupEpLc,
       "cucsInitiatorGroupEpName": cucsInitiatorGroupEpName,
       "cucsInitiatorGroupEpPolName": cucsInitiatorGroupEpPolName,
       "cucsInitiatorGroupEpRmtDiskCfgName": cucsInitiatorGroupEpRmtDiskCfgName,
       "cucsInitiatorIScsiInitiatorEpTable": cucsInitiatorIScsiInitiatorEpTable,
       "cucsInitiatorIScsiInitiatorEpEntry": cucsInitiatorIScsiInitiatorEpEntry,
       "cucsInitiatorIScsiInitiatorEpInstanceId": cucsInitiatorIScsiInitiatorEpInstanceId,
       "cucsInitiatorIScsiInitiatorEpDn": cucsInitiatorIScsiInitiatorEpDn,
       "cucsInitiatorIScsiInitiatorEpRn": cucsInitiatorIScsiInitiatorEpRn,
       "cucsInitiatorIScsiInitiatorEpEpDn": cucsInitiatorIScsiInitiatorEpEpDn,
       "cucsInitiatorIScsiInitiatorEpId": cucsInitiatorIScsiInitiatorEpId,
       "cucsInitiatorIScsiInitiatorEpIqn": cucsInitiatorIScsiInitiatorEpIqn,
       "cucsInitiatorIScsiInitiatorEpName": cucsInitiatorIScsiInitiatorEpName,
       "cucsInitiatorIScsiInitiatorEpPref": cucsInitiatorIScsiInitiatorEpPref,
       "cucsInitiatorIScsiInitiatorEpProt": cucsInitiatorIScsiInitiatorEpProt,
       "cucsInitiatorLunEpTable": cucsInitiatorLunEpTable,
       "cucsInitiatorLunEpEntry": cucsInitiatorLunEpEntry,
       "cucsInitiatorLunEpInstanceId": cucsInitiatorLunEpInstanceId,
       "cucsInitiatorLunEpDn": cucsInitiatorLunEpDn,
       "cucsInitiatorLunEpRn": cucsInitiatorLunEpRn,
       "cucsInitiatorLunEpBootable": cucsInitiatorLunEpBootable,
       "cucsInitiatorLunEpEpDn": cucsInitiatorLunEpEpDn,
       "cucsInitiatorLunEpId": cucsInitiatorLunEpId,
       "cucsInitiatorMemberEpTable": cucsInitiatorMemberEpTable,
       "cucsInitiatorMemberEpEntry": cucsInitiatorMemberEpEntry,
       "cucsInitiatorMemberEpInstanceId": cucsInitiatorMemberEpInstanceId,
       "cucsInitiatorMemberEpDn": cucsInitiatorMemberEpDn,
       "cucsInitiatorMemberEpRn": cucsInitiatorMemberEpRn,
       "cucsInitiatorMemberEpEpDn": cucsInitiatorMemberEpEpDn,
       "cucsInitiatorMemberEpId": cucsInitiatorMemberEpId,
       "cucsInitiatorRequestorEpTable": cucsInitiatorRequestorEpTable,
       "cucsInitiatorRequestorEpEntry": cucsInitiatorRequestorEpEntry,
       "cucsInitiatorRequestorEpInstanceId": cucsInitiatorRequestorEpInstanceId,
       "cucsInitiatorRequestorEpDn": cucsInitiatorRequestorEpDn,
       "cucsInitiatorRequestorEpRn": cucsInitiatorRequestorEpRn,
       "cucsInitiatorRequestorEpAllocState": cucsInitiatorRequestorEpAllocState,
       "cucsInitiatorRequestorEpEpDn": cucsInitiatorRequestorEpEpDn,
       "cucsInitiatorRequestorEpId": cucsInitiatorRequestorEpId,
       "cucsInitiatorRequestorEpSysId": cucsInitiatorRequestorEpSysId,
       "cucsInitiatorRequestorEpSysName": cucsInitiatorRequestorEpSysName,
       "cucsInitiatorRequestorGrpEpTable": cucsInitiatorRequestorGrpEpTable,
       "cucsInitiatorRequestorGrpEpEntry": cucsInitiatorRequestorGrpEpEntry,
       "cucsInitiatorRequestorGrpEpInstanceId": cucsInitiatorRequestorGrpEpInstanceId,
       "cucsInitiatorRequestorGrpEpDn": cucsInitiatorRequestorGrpEpDn,
       "cucsInitiatorRequestorGrpEpRn": cucsInitiatorRequestorGrpEpRn,
       "cucsInitiatorRequestorGrpEpAllocState": cucsInitiatorRequestorGrpEpAllocState,
       "cucsInitiatorRequestorGrpEpEpDn": cucsInitiatorRequestorGrpEpEpDn,
       "cucsInitiatorRequestorGrpEpId": cucsInitiatorRequestorGrpEpId,
       "cucsInitiatorRequestorGrpEpLc": cucsInitiatorRequestorGrpEpLc,
       "cucsInitiatorRequestorGrpEpPolDn": cucsInitiatorRequestorGrpEpPolDn,
       "cucsInitiatorRequestorGrpEpType": cucsInitiatorRequestorGrpEpType,
       "cucsInitiatorStoreEpTable": cucsInitiatorStoreEpTable,
       "cucsInitiatorStoreEpEntry": cucsInitiatorStoreEpEntry,
       "cucsInitiatorStoreEpInstanceId": cucsInitiatorStoreEpInstanceId,
       "cucsInitiatorStoreEpDn": cucsInitiatorStoreEpDn,
       "cucsInitiatorStoreEpRn": cucsInitiatorStoreEpRn,
       "cucsInitiatorStoreEpEpDn": cucsInitiatorStoreEpEpDn,
       "cucsInitiatorStoreEpId": cucsInitiatorStoreEpId,
       "cucsInitiatorStoreEpType": cucsInitiatorStoreEpType,
       "cucsInitiatorUnitEpTable": cucsInitiatorUnitEpTable,
       "cucsInitiatorUnitEpEntry": cucsInitiatorUnitEpEntry,
       "cucsInitiatorUnitEpInstanceId": cucsInitiatorUnitEpInstanceId,
       "cucsInitiatorUnitEpDn": cucsInitiatorUnitEpDn,
       "cucsInitiatorUnitEpRn": cucsInitiatorUnitEpRn,
       "cucsInitiatorUnitEpBoot": cucsInitiatorUnitEpBoot,
       "cucsInitiatorUnitEpEpDn": cucsInitiatorUnitEpEpDn,
       "cucsInitiatorUnitEpHa": cucsInitiatorUnitEpHa,
       "cucsInitiatorUnitEpId": cucsInitiatorUnitEpId,
       "cucsInitiatorUnitEpItemDn": cucsInitiatorUnitEpItemDn,
       "cucsInitiatorUnitEpLc": cucsInitiatorUnitEpLc,
       "cucsInitiatorUnitEpPhyId": cucsInitiatorUnitEpPhyId,
       "cucsInitiatorUnitEpProt": cucsInitiatorUnitEpProt}
)
