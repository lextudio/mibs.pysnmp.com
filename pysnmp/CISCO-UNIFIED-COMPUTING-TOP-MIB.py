# SNMP MIB module (CISCO-UNIFIED-COMPUTING-TOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-TOP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:26 2024
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

(CucsPolicyPolicyOwner,
 CucsTopInfoPolicyState,
 CucsTopInfoSyncPolicyState,
 CucsTopMode) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsPolicyPolicyOwner",
    "CucsTopInfoPolicyState",
    "CucsTopInfoSyncPolicyState",
    "CucsTopMode")

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

cucsTopObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsTopMetaInfTable_Object = MibTable
cucsTopMetaInfTable = _CucsTopMetaInfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 1)
)
if mibBuilder.loadTexts:
    cucsTopMetaInfTable.setStatus("current")
_CucsTopMetaInfEntry_Object = MibTableRow
cucsTopMetaInfEntry = _CucsTopMetaInfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 1, 1)
)
cucsTopMetaInfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-TOP-MIB", "cucsTopMetaInfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsTopMetaInfEntry.setStatus("current")
_CucsTopMetaInfInstanceId_Type = CucsManagedObjectId
_CucsTopMetaInfInstanceId_Object = MibTableColumn
cucsTopMetaInfInstanceId = _CucsTopMetaInfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 1, 1, 1),
    _CucsTopMetaInfInstanceId_Type()
)
cucsTopMetaInfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsTopMetaInfInstanceId.setStatus("current")
_CucsTopMetaInfDn_Type = CucsManagedObjectDn
_CucsTopMetaInfDn_Object = MibTableColumn
cucsTopMetaInfDn = _CucsTopMetaInfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 1, 1, 2),
    _CucsTopMetaInfDn_Type()
)
cucsTopMetaInfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopMetaInfDn.setStatus("current")
_CucsTopMetaInfRn_Type = SnmpAdminString
_CucsTopMetaInfRn_Object = MibTableColumn
cucsTopMetaInfRn = _CucsTopMetaInfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 1, 1, 3),
    _CucsTopMetaInfRn_Type()
)
cucsTopMetaInfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopMetaInfRn.setStatus("current")
_CucsTopMetaInfEcode_Type = SnmpAdminString
_CucsTopMetaInfEcode_Object = MibTableColumn
cucsTopMetaInfEcode = _CucsTopMetaInfEcode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 1, 1, 4),
    _CucsTopMetaInfEcode_Type()
)
cucsTopMetaInfEcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopMetaInfEcode.setStatus("current")
_CucsTopMetaInfName_Type = SnmpAdminString
_CucsTopMetaInfName_Object = MibTableColumn
cucsTopMetaInfName = _CucsTopMetaInfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 1, 1, 5),
    _CucsTopMetaInfName_Type()
)
cucsTopMetaInfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopMetaInfName.setStatus("current")
_CucsTopRootTable_Object = MibTable
cucsTopRootTable = _CucsTopRootTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 2)
)
if mibBuilder.loadTexts:
    cucsTopRootTable.setStatus("current")
_CucsTopRootEntry_Object = MibTableRow
cucsTopRootEntry = _CucsTopRootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 2, 1)
)
cucsTopRootEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-TOP-MIB", "cucsTopRootInstanceId"),
)
if mibBuilder.loadTexts:
    cucsTopRootEntry.setStatus("current")
_CucsTopRootInstanceId_Type = CucsManagedObjectId
_CucsTopRootInstanceId_Object = MibTableColumn
cucsTopRootInstanceId = _CucsTopRootInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 2, 1, 1),
    _CucsTopRootInstanceId_Type()
)
cucsTopRootInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsTopRootInstanceId.setStatus("current")
_CucsTopRootDn_Type = CucsManagedObjectDn
_CucsTopRootDn_Object = MibTableColumn
cucsTopRootDn = _CucsTopRootDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 2, 1, 2),
    _CucsTopRootDn_Type()
)
cucsTopRootDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopRootDn.setStatus("current")
_CucsTopRootRn_Type = SnmpAdminString
_CucsTopRootRn_Object = MibTableColumn
cucsTopRootRn = _CucsTopRootRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 2, 1, 3),
    _CucsTopRootRn_Type()
)
cucsTopRootRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopRootRn.setStatus("current")
_CucsTopSystemTable_Object = MibTable
cucsTopSystemTable = _CucsTopSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3)
)
if mibBuilder.loadTexts:
    cucsTopSystemTable.setStatus("current")
_CucsTopSystemEntry_Object = MibTableRow
cucsTopSystemEntry = _CucsTopSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1)
)
cucsTopSystemEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-TOP-MIB", "cucsTopSystemInstanceId"),
)
if mibBuilder.loadTexts:
    cucsTopSystemEntry.setStatus("current")
_CucsTopSystemInstanceId_Type = CucsManagedObjectId
_CucsTopSystemInstanceId_Object = MibTableColumn
cucsTopSystemInstanceId = _CucsTopSystemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 1),
    _CucsTopSystemInstanceId_Type()
)
cucsTopSystemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsTopSystemInstanceId.setStatus("current")
_CucsTopSystemDn_Type = CucsManagedObjectDn
_CucsTopSystemDn_Object = MibTableColumn
cucsTopSystemDn = _CucsTopSystemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 2),
    _CucsTopSystemDn_Type()
)
cucsTopSystemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopSystemDn.setStatus("current")
_CucsTopSystemRn_Type = SnmpAdminString
_CucsTopSystemRn_Object = MibTableColumn
cucsTopSystemRn = _CucsTopSystemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 3),
    _CucsTopSystemRn_Type()
)
cucsTopSystemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopSystemRn.setStatus("current")
_CucsTopSystemAddress_Type = InetAddressIPv4
_CucsTopSystemAddress_Object = MibTableColumn
cucsTopSystemAddress = _CucsTopSystemAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 4),
    _CucsTopSystemAddress_Type()
)
cucsTopSystemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopSystemAddress.setStatus("current")
_CucsTopSystemCurrentTime_Type = DateAndTime
_CucsTopSystemCurrentTime_Object = MibTableColumn
cucsTopSystemCurrentTime = _CucsTopSystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 5),
    _CucsTopSystemCurrentTime_Type()
)
cucsTopSystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopSystemCurrentTime.setStatus("current")
_CucsTopSystemMode_Type = CucsTopMode
_CucsTopSystemMode_Object = MibTableColumn
cucsTopSystemMode = _CucsTopSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 6),
    _CucsTopSystemMode_Type()
)
cucsTopSystemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopSystemMode.setStatus("current")
_CucsTopSystemName_Type = SnmpAdminString
_CucsTopSystemName_Object = MibTableColumn
cucsTopSystemName = _CucsTopSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 7),
    _CucsTopSystemName_Type()
)
cucsTopSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopSystemName.setStatus("current")
_CucsTopSystemSystemUpTime_Type = TimeIntervalSec
_CucsTopSystemSystemUpTime_Object = MibTableColumn
cucsTopSystemSystemUpTime = _CucsTopSystemSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 8),
    _CucsTopSystemSystemUpTime_Type()
)
cucsTopSystemSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopSystemSystemUpTime.setStatus("current")
_CucsTopSystemDescr_Type = SnmpAdminString
_CucsTopSystemDescr_Object = MibTableColumn
cucsTopSystemDescr = _CucsTopSystemDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 9),
    _CucsTopSystemDescr_Type()
)
cucsTopSystemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopSystemDescr.setStatus("current")
_CucsTopSystemOwner_Type = SnmpAdminString
_CucsTopSystemOwner_Object = MibTableColumn
cucsTopSystemOwner = _CucsTopSystemOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 10),
    _CucsTopSystemOwner_Type()
)
cucsTopSystemOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopSystemOwner.setStatus("current")
_CucsTopSystemSite_Type = SnmpAdminString
_CucsTopSystemSite_Object = MibTableColumn
cucsTopSystemSite = _CucsTopSystemSite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 11),
    _CucsTopSystemSite_Type()
)
cucsTopSystemSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopSystemSite.setStatus("current")
_CucsTopSystemIpv6Addr_Type = InetAddressIPv6
_CucsTopSystemIpv6Addr_Object = MibTableColumn
cucsTopSystemIpv6Addr = _CucsTopSystemIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 12),
    _CucsTopSystemIpv6Addr_Type()
)
cucsTopSystemIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopSystemIpv6Addr.setStatus("current")
_CucsTopSysDefaultsTable_Object = MibTable
cucsTopSysDefaultsTable = _CucsTopSysDefaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 4)
)
if mibBuilder.loadTexts:
    cucsTopSysDefaultsTable.setStatus("current")
_CucsTopSysDefaultsEntry_Object = MibTableRow
cucsTopSysDefaultsEntry = _CucsTopSysDefaultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 4, 1)
)
cucsTopSysDefaultsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-TOP-MIB", "cucsTopSysDefaultsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsTopSysDefaultsEntry.setStatus("current")
_CucsTopSysDefaultsInstanceId_Type = CucsManagedObjectId
_CucsTopSysDefaultsInstanceId_Object = MibTableColumn
cucsTopSysDefaultsInstanceId = _CucsTopSysDefaultsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 4, 1, 1),
    _CucsTopSysDefaultsInstanceId_Type()
)
cucsTopSysDefaultsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsTopSysDefaultsInstanceId.setStatus("current")
_CucsTopSysDefaultsDn_Type = CucsManagedObjectDn
_CucsTopSysDefaultsDn_Object = MibTableColumn
cucsTopSysDefaultsDn = _CucsTopSysDefaultsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 4, 1, 2),
    _CucsTopSysDefaultsDn_Type()
)
cucsTopSysDefaultsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopSysDefaultsDn.setStatus("current")
_CucsTopSysDefaultsRn_Type = SnmpAdminString
_CucsTopSysDefaultsRn_Object = MibTableColumn
cucsTopSysDefaultsRn = _CucsTopSysDefaultsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 4, 1, 3),
    _CucsTopSysDefaultsRn_Type()
)
cucsTopSysDefaultsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopSysDefaultsRn.setStatus("current")
_CucsTopInfoPolicyTable_Object = MibTable
cucsTopInfoPolicyTable = _CucsTopInfoPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 5)
)
if mibBuilder.loadTexts:
    cucsTopInfoPolicyTable.setStatus("current")
_CucsTopInfoPolicyEntry_Object = MibTableRow
cucsTopInfoPolicyEntry = _CucsTopInfoPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 5, 1)
)
cucsTopInfoPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-TOP-MIB", "cucsTopInfoPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsTopInfoPolicyEntry.setStatus("current")
_CucsTopInfoPolicyInstanceId_Type = CucsManagedObjectId
_CucsTopInfoPolicyInstanceId_Object = MibTableColumn
cucsTopInfoPolicyInstanceId = _CucsTopInfoPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 5, 1, 1),
    _CucsTopInfoPolicyInstanceId_Type()
)
cucsTopInfoPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsTopInfoPolicyInstanceId.setStatus("current")
_CucsTopInfoPolicyDn_Type = CucsManagedObjectDn
_CucsTopInfoPolicyDn_Object = MibTableColumn
cucsTopInfoPolicyDn = _CucsTopInfoPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 5, 1, 2),
    _CucsTopInfoPolicyDn_Type()
)
cucsTopInfoPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopInfoPolicyDn.setStatus("current")
_CucsTopInfoPolicyRn_Type = SnmpAdminString
_CucsTopInfoPolicyRn_Object = MibTableColumn
cucsTopInfoPolicyRn = _CucsTopInfoPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 5, 1, 3),
    _CucsTopInfoPolicyRn_Type()
)
cucsTopInfoPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopInfoPolicyRn.setStatus("current")
_CucsTopInfoPolicyState_Type = CucsTopInfoPolicyState
_CucsTopInfoPolicyState_Object = MibTableColumn
cucsTopInfoPolicyState = _CucsTopInfoPolicyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 5, 1, 4),
    _CucsTopInfoPolicyState_Type()
)
cucsTopInfoPolicyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopInfoPolicyState.setStatus("current")
_CucsTopInfoSyncPolicyTable_Object = MibTable
cucsTopInfoSyncPolicyTable = _CucsTopInfoSyncPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6)
)
if mibBuilder.loadTexts:
    cucsTopInfoSyncPolicyTable.setStatus("current")
_CucsTopInfoSyncPolicyEntry_Object = MibTableRow
cucsTopInfoSyncPolicyEntry = _CucsTopInfoSyncPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1)
)
cucsTopInfoSyncPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-TOP-MIB", "cucsTopInfoSyncPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsTopInfoSyncPolicyEntry.setStatus("current")
_CucsTopInfoSyncPolicyInstanceId_Type = CucsManagedObjectId
_CucsTopInfoSyncPolicyInstanceId_Object = MibTableColumn
cucsTopInfoSyncPolicyInstanceId = _CucsTopInfoSyncPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 1),
    _CucsTopInfoSyncPolicyInstanceId_Type()
)
cucsTopInfoSyncPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsTopInfoSyncPolicyInstanceId.setStatus("current")
_CucsTopInfoSyncPolicyDn_Type = CucsManagedObjectDn
_CucsTopInfoSyncPolicyDn_Object = MibTableColumn
cucsTopInfoSyncPolicyDn = _CucsTopInfoSyncPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 2),
    _CucsTopInfoSyncPolicyDn_Type()
)
cucsTopInfoSyncPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopInfoSyncPolicyDn.setStatus("current")
_CucsTopInfoSyncPolicyRn_Type = SnmpAdminString
_CucsTopInfoSyncPolicyRn_Object = MibTableColumn
cucsTopInfoSyncPolicyRn = _CucsTopInfoSyncPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 3),
    _CucsTopInfoSyncPolicyRn_Type()
)
cucsTopInfoSyncPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopInfoSyncPolicyRn.setStatus("current")
_CucsTopInfoSyncPolicyDescr_Type = SnmpAdminString
_CucsTopInfoSyncPolicyDescr_Object = MibTableColumn
cucsTopInfoSyncPolicyDescr = _CucsTopInfoSyncPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 4),
    _CucsTopInfoSyncPolicyDescr_Type()
)
cucsTopInfoSyncPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopInfoSyncPolicyDescr.setStatus("current")
_CucsTopInfoSyncPolicyIntId_Type = SnmpAdminString
_CucsTopInfoSyncPolicyIntId_Object = MibTableColumn
cucsTopInfoSyncPolicyIntId = _CucsTopInfoSyncPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 5),
    _CucsTopInfoSyncPolicyIntId_Type()
)
cucsTopInfoSyncPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopInfoSyncPolicyIntId.setStatus("current")
_CucsTopInfoSyncPolicyName_Type = SnmpAdminString
_CucsTopInfoSyncPolicyName_Object = MibTableColumn
cucsTopInfoSyncPolicyName = _CucsTopInfoSyncPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 6),
    _CucsTopInfoSyncPolicyName_Type()
)
cucsTopInfoSyncPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopInfoSyncPolicyName.setStatus("current")
_CucsTopInfoSyncPolicyPolicyLevel_Type = Gauge32
_CucsTopInfoSyncPolicyPolicyLevel_Object = MibTableColumn
cucsTopInfoSyncPolicyPolicyLevel = _CucsTopInfoSyncPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 7),
    _CucsTopInfoSyncPolicyPolicyLevel_Type()
)
cucsTopInfoSyncPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopInfoSyncPolicyPolicyLevel.setStatus("current")
_CucsTopInfoSyncPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsTopInfoSyncPolicyPolicyOwner_Object = MibTableColumn
cucsTopInfoSyncPolicyPolicyOwner = _CucsTopInfoSyncPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 8),
    _CucsTopInfoSyncPolicyPolicyOwner_Type()
)
cucsTopInfoSyncPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopInfoSyncPolicyPolicyOwner.setStatus("current")
_CucsTopInfoSyncPolicyState_Type = CucsTopInfoSyncPolicyState
_CucsTopInfoSyncPolicyState_Object = MibTableColumn
cucsTopInfoSyncPolicyState = _CucsTopInfoSyncPolicyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 9),
    _CucsTopInfoSyncPolicyState_Type()
)
cucsTopInfoSyncPolicyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTopInfoSyncPolicyState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-TOP-MIB",
    **{"cucsTopObjects": cucsTopObjects,
       "cucsTopMetaInfTable": cucsTopMetaInfTable,
       "cucsTopMetaInfEntry": cucsTopMetaInfEntry,
       "cucsTopMetaInfInstanceId": cucsTopMetaInfInstanceId,
       "cucsTopMetaInfDn": cucsTopMetaInfDn,
       "cucsTopMetaInfRn": cucsTopMetaInfRn,
       "cucsTopMetaInfEcode": cucsTopMetaInfEcode,
       "cucsTopMetaInfName": cucsTopMetaInfName,
       "cucsTopRootTable": cucsTopRootTable,
       "cucsTopRootEntry": cucsTopRootEntry,
       "cucsTopRootInstanceId": cucsTopRootInstanceId,
       "cucsTopRootDn": cucsTopRootDn,
       "cucsTopRootRn": cucsTopRootRn,
       "cucsTopSystemTable": cucsTopSystemTable,
       "cucsTopSystemEntry": cucsTopSystemEntry,
       "cucsTopSystemInstanceId": cucsTopSystemInstanceId,
       "cucsTopSystemDn": cucsTopSystemDn,
       "cucsTopSystemRn": cucsTopSystemRn,
       "cucsTopSystemAddress": cucsTopSystemAddress,
       "cucsTopSystemCurrentTime": cucsTopSystemCurrentTime,
       "cucsTopSystemMode": cucsTopSystemMode,
       "cucsTopSystemName": cucsTopSystemName,
       "cucsTopSystemSystemUpTime": cucsTopSystemSystemUpTime,
       "cucsTopSystemDescr": cucsTopSystemDescr,
       "cucsTopSystemOwner": cucsTopSystemOwner,
       "cucsTopSystemSite": cucsTopSystemSite,
       "cucsTopSystemIpv6Addr": cucsTopSystemIpv6Addr,
       "cucsTopSysDefaultsTable": cucsTopSysDefaultsTable,
       "cucsTopSysDefaultsEntry": cucsTopSysDefaultsEntry,
       "cucsTopSysDefaultsInstanceId": cucsTopSysDefaultsInstanceId,
       "cucsTopSysDefaultsDn": cucsTopSysDefaultsDn,
       "cucsTopSysDefaultsRn": cucsTopSysDefaultsRn,
       "cucsTopInfoPolicyTable": cucsTopInfoPolicyTable,
       "cucsTopInfoPolicyEntry": cucsTopInfoPolicyEntry,
       "cucsTopInfoPolicyInstanceId": cucsTopInfoPolicyInstanceId,
       "cucsTopInfoPolicyDn": cucsTopInfoPolicyDn,
       "cucsTopInfoPolicyRn": cucsTopInfoPolicyRn,
       "cucsTopInfoPolicyState": cucsTopInfoPolicyState,
       "cucsTopInfoSyncPolicyTable": cucsTopInfoSyncPolicyTable,
       "cucsTopInfoSyncPolicyEntry": cucsTopInfoSyncPolicyEntry,
       "cucsTopInfoSyncPolicyInstanceId": cucsTopInfoSyncPolicyInstanceId,
       "cucsTopInfoSyncPolicyDn": cucsTopInfoSyncPolicyDn,
       "cucsTopInfoSyncPolicyRn": cucsTopInfoSyncPolicyRn,
       "cucsTopInfoSyncPolicyDescr": cucsTopInfoSyncPolicyDescr,
       "cucsTopInfoSyncPolicyIntId": cucsTopInfoSyncPolicyIntId,
       "cucsTopInfoSyncPolicyName": cucsTopInfoSyncPolicyName,
       "cucsTopInfoSyncPolicyPolicyLevel": cucsTopInfoSyncPolicyPolicyLevel,
       "cucsTopInfoSyncPolicyPolicyOwner": cucsTopInfoSyncPolicyPolicyOwner,
       "cucsTopInfoSyncPolicyState": cucsTopInfoSyncPolicyState}
)
