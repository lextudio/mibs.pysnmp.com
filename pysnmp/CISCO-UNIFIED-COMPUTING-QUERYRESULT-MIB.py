# SNMP MIB module (CISCO-UNIFIED-COMPUTING-QUERYRESULT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-QUERYRESULT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:16 2024
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

cucsQueryresultObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsQueryresultDependencyTable_Object = MibTable
cucsQueryresultDependencyTable = _CucsQueryresultDependencyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1)
)
if mibBuilder.loadTexts:
    cucsQueryresultDependencyTable.setStatus("current")
_CucsQueryresultDependencyEntry_Object = MibTableRow
cucsQueryresultDependencyEntry = _CucsQueryresultDependencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1)
)
cucsQueryresultDependencyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-QUERYRESULT-MIB", "cucsQueryresultDependencyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsQueryresultDependencyEntry.setStatus("current")
_CucsQueryresultDependencyInstanceId_Type = CucsManagedObjectId
_CucsQueryresultDependencyInstanceId_Object = MibTableColumn
cucsQueryresultDependencyInstanceId = _CucsQueryresultDependencyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 1),
    _CucsQueryresultDependencyInstanceId_Type()
)
cucsQueryresultDependencyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsQueryresultDependencyInstanceId.setStatus("current")
_CucsQueryresultDependencyDn_Type = CucsManagedObjectDn
_CucsQueryresultDependencyDn_Object = MibTableColumn
cucsQueryresultDependencyDn = _CucsQueryresultDependencyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 2),
    _CucsQueryresultDependencyDn_Type()
)
cucsQueryresultDependencyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQueryresultDependencyDn.setStatus("current")
_CucsQueryresultDependencyRn_Type = SnmpAdminString
_CucsQueryresultDependencyRn_Object = MibTableColumn
cucsQueryresultDependencyRn = _CucsQueryresultDependencyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 3),
    _CucsQueryresultDependencyRn_Type()
)
cucsQueryresultDependencyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQueryresultDependencyRn.setStatus("current")
_CucsQueryresultDependencyClassType_Type = SnmpAdminString
_CucsQueryresultDependencyClassType_Object = MibTableColumn
cucsQueryresultDependencyClassType = _CucsQueryresultDependencyClassType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 4),
    _CucsQueryresultDependencyClassType_Type()
)
cucsQueryresultDependencyClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQueryresultDependencyClassType.setStatus("current")
_CucsQueryresultDependencyIsImportable_Type = TruthValue
_CucsQueryresultDependencyIsImportable_Object = MibTableColumn
cucsQueryresultDependencyIsImportable = _CucsQueryresultDependencyIsImportable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 5),
    _CucsQueryresultDependencyIsImportable_Type()
)
cucsQueryresultDependencyIsImportable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQueryresultDependencyIsImportable.setStatus("current")
_CucsQueryresultDependencyPolicyOwner_Type = SnmpAdminString
_CucsQueryresultDependencyPolicyOwner_Object = MibTableColumn
cucsQueryresultDependencyPolicyOwner = _CucsQueryresultDependencyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 6),
    _CucsQueryresultDependencyPolicyOwner_Type()
)
cucsQueryresultDependencyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQueryresultDependencyPolicyOwner.setStatus("current")
_CucsQueryresultDependencyRefConvertedDn_Type = SnmpAdminString
_CucsQueryresultDependencyRefConvertedDn_Object = MibTableColumn
cucsQueryresultDependencyRefConvertedDn = _CucsQueryresultDependencyRefConvertedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 7),
    _CucsQueryresultDependencyRefConvertedDn_Type()
)
cucsQueryresultDependencyRefConvertedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQueryresultDependencyRefConvertedDn.setStatus("current")
_CucsQueryresultDependencyRefDn_Type = SnmpAdminString
_CucsQueryresultDependencyRefDn_Object = MibTableColumn
cucsQueryresultDependencyRefDn = _CucsQueryresultDependencyRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 8),
    _CucsQueryresultDependencyRefDn_Type()
)
cucsQueryresultDependencyRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQueryresultDependencyRefDn.setStatus("current")
_CucsQueryresultDependencyRefName_Type = SnmpAdminString
_CucsQueryresultDependencyRefName_Object = MibTableColumn
cucsQueryresultDependencyRefName = _CucsQueryresultDependencyRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 9),
    _CucsQueryresultDependencyRefName_Type()
)
cucsQueryresultDependencyRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQueryresultDependencyRefName.setStatus("current")
_CucsQueryresultUsageTable_Object = MibTable
cucsQueryresultUsageTable = _CucsQueryresultUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2)
)
if mibBuilder.loadTexts:
    cucsQueryresultUsageTable.setStatus("current")
_CucsQueryresultUsageEntry_Object = MibTableRow
cucsQueryresultUsageEntry = _CucsQueryresultUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1)
)
cucsQueryresultUsageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-QUERYRESULT-MIB", "cucsQueryresultUsageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsQueryresultUsageEntry.setStatus("current")
_CucsQueryresultUsageInstanceId_Type = CucsManagedObjectId
_CucsQueryresultUsageInstanceId_Object = MibTableColumn
cucsQueryresultUsageInstanceId = _CucsQueryresultUsageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 1),
    _CucsQueryresultUsageInstanceId_Type()
)
cucsQueryresultUsageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsQueryresultUsageInstanceId.setStatus("current")
_CucsQueryresultUsageDn_Type = CucsManagedObjectDn
_CucsQueryresultUsageDn_Object = MibTableColumn
cucsQueryresultUsageDn = _CucsQueryresultUsageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 2),
    _CucsQueryresultUsageDn_Type()
)
cucsQueryresultUsageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQueryresultUsageDn.setStatus("current")
_CucsQueryresultUsageRn_Type = SnmpAdminString
_CucsQueryresultUsageRn_Object = MibTableColumn
cucsQueryresultUsageRn = _CucsQueryresultUsageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 3),
    _CucsQueryresultUsageRn_Type()
)
cucsQueryresultUsageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQueryresultUsageRn.setStatus("current")
_CucsQueryresultUsageClassType_Type = SnmpAdminString
_CucsQueryresultUsageClassType_Object = MibTableColumn
cucsQueryresultUsageClassType = _CucsQueryresultUsageClassType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 4),
    _CucsQueryresultUsageClassType_Type()
)
cucsQueryresultUsageClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQueryresultUsageClassType.setStatus("current")
_CucsQueryresultUsageIsServiceTemplate_Type = TruthValue
_CucsQueryresultUsageIsServiceTemplate_Object = MibTableColumn
cucsQueryresultUsageIsServiceTemplate = _CucsQueryresultUsageIsServiceTemplate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 5),
    _CucsQueryresultUsageIsServiceTemplate_Type()
)
cucsQueryresultUsageIsServiceTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQueryresultUsageIsServiceTemplate.setStatus("current")
_CucsQueryresultUsagePolicyOwner_Type = SnmpAdminString
_CucsQueryresultUsagePolicyOwner_Object = MibTableColumn
cucsQueryresultUsagePolicyOwner = _CucsQueryresultUsagePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 6),
    _CucsQueryresultUsagePolicyOwner_Type()
)
cucsQueryresultUsagePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQueryresultUsagePolicyOwner.setStatus("current")
_CucsQueryresultUsageRefConvertedDn_Type = SnmpAdminString
_CucsQueryresultUsageRefConvertedDn_Object = MibTableColumn
cucsQueryresultUsageRefConvertedDn = _CucsQueryresultUsageRefConvertedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 7),
    _CucsQueryresultUsageRefConvertedDn_Type()
)
cucsQueryresultUsageRefConvertedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQueryresultUsageRefConvertedDn.setStatus("current")
_CucsQueryresultUsageRefDn_Type = SnmpAdminString
_CucsQueryresultUsageRefDn_Object = MibTableColumn
cucsQueryresultUsageRefDn = _CucsQueryresultUsageRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 8),
    _CucsQueryresultUsageRefDn_Type()
)
cucsQueryresultUsageRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQueryresultUsageRefDn.setStatus("current")
_CucsQueryresultUsageRefName_Type = SnmpAdminString
_CucsQueryresultUsageRefName_Object = MibTableColumn
cucsQueryresultUsageRefName = _CucsQueryresultUsageRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 9),
    _CucsQueryresultUsageRefName_Type()
)
cucsQueryresultUsageRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQueryresultUsageRefName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-QUERYRESULT-MIB",
    **{"cucsQueryresultObjects": cucsQueryresultObjects,
       "cucsQueryresultDependencyTable": cucsQueryresultDependencyTable,
       "cucsQueryresultDependencyEntry": cucsQueryresultDependencyEntry,
       "cucsQueryresultDependencyInstanceId": cucsQueryresultDependencyInstanceId,
       "cucsQueryresultDependencyDn": cucsQueryresultDependencyDn,
       "cucsQueryresultDependencyRn": cucsQueryresultDependencyRn,
       "cucsQueryresultDependencyClassType": cucsQueryresultDependencyClassType,
       "cucsQueryresultDependencyIsImportable": cucsQueryresultDependencyIsImportable,
       "cucsQueryresultDependencyPolicyOwner": cucsQueryresultDependencyPolicyOwner,
       "cucsQueryresultDependencyRefConvertedDn": cucsQueryresultDependencyRefConvertedDn,
       "cucsQueryresultDependencyRefDn": cucsQueryresultDependencyRefDn,
       "cucsQueryresultDependencyRefName": cucsQueryresultDependencyRefName,
       "cucsQueryresultUsageTable": cucsQueryresultUsageTable,
       "cucsQueryresultUsageEntry": cucsQueryresultUsageEntry,
       "cucsQueryresultUsageInstanceId": cucsQueryresultUsageInstanceId,
       "cucsQueryresultUsageDn": cucsQueryresultUsageDn,
       "cucsQueryresultUsageRn": cucsQueryresultUsageRn,
       "cucsQueryresultUsageClassType": cucsQueryresultUsageClassType,
       "cucsQueryresultUsageIsServiceTemplate": cucsQueryresultUsageIsServiceTemplate,
       "cucsQueryresultUsagePolicyOwner": cucsQueryresultUsagePolicyOwner,
       "cucsQueryresultUsageRefConvertedDn": cucsQueryresultUsageRefConvertedDn,
       "cucsQueryresultUsageRefDn": cucsQueryresultUsageRefDn,
       "cucsQueryresultUsageRefName": cucsQueryresultUsageRefName}
)
