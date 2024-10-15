# SNMP MIB module (CISCO-UNIFIED-COMPUTING-FEATURE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-FEATURE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:32 2024
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

(CucsFeatureSupportabilityType,) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsFeatureSupportabilityType")

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

cucsFeatureObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsFeatureContextEpTable_Object = MibTable
cucsFeatureContextEpTable = _CucsFeatureContextEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 1)
)
if mibBuilder.loadTexts:
    cucsFeatureContextEpTable.setStatus("current")
_CucsFeatureContextEpEntry_Object = MibTableRow
cucsFeatureContextEpEntry = _CucsFeatureContextEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 1, 1)
)
cucsFeatureContextEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FEATURE-MIB", "cucsFeatureContextEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFeatureContextEpEntry.setStatus("current")
_CucsFeatureContextEpInstanceId_Type = CucsManagedObjectId
_CucsFeatureContextEpInstanceId_Object = MibTableColumn
cucsFeatureContextEpInstanceId = _CucsFeatureContextEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 1, 1, 1),
    _CucsFeatureContextEpInstanceId_Type()
)
cucsFeatureContextEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFeatureContextEpInstanceId.setStatus("current")
_CucsFeatureContextEpDn_Type = CucsManagedObjectDn
_CucsFeatureContextEpDn_Object = MibTableColumn
cucsFeatureContextEpDn = _CucsFeatureContextEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 1, 1, 2),
    _CucsFeatureContextEpDn_Type()
)
cucsFeatureContextEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureContextEpDn.setStatus("current")
_CucsFeatureContextEpRn_Type = SnmpAdminString
_CucsFeatureContextEpRn_Object = MibTableColumn
cucsFeatureContextEpRn = _CucsFeatureContextEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 1, 1, 3),
    _CucsFeatureContextEpRn_Type()
)
cucsFeatureContextEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureContextEpRn.setStatus("current")
_CucsFeatureDefinitionTable_Object = MibTable
cucsFeatureDefinitionTable = _CucsFeatureDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 2)
)
if mibBuilder.loadTexts:
    cucsFeatureDefinitionTable.setStatus("current")
_CucsFeatureDefinitionEntry_Object = MibTableRow
cucsFeatureDefinitionEntry = _CucsFeatureDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 2, 1)
)
cucsFeatureDefinitionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FEATURE-MIB", "cucsFeatureDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFeatureDefinitionEntry.setStatus("current")
_CucsFeatureDefinitionInstanceId_Type = CucsManagedObjectId
_CucsFeatureDefinitionInstanceId_Object = MibTableColumn
cucsFeatureDefinitionInstanceId = _CucsFeatureDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 2, 1, 1),
    _CucsFeatureDefinitionInstanceId_Type()
)
cucsFeatureDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionInstanceId.setStatus("current")
_CucsFeatureDefinitionDn_Type = CucsManagedObjectDn
_CucsFeatureDefinitionDn_Object = MibTableColumn
cucsFeatureDefinitionDn = _CucsFeatureDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 2, 1, 2),
    _CucsFeatureDefinitionDn_Type()
)
cucsFeatureDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionDn.setStatus("current")
_CucsFeatureDefinitionRn_Type = SnmpAdminString
_CucsFeatureDefinitionRn_Object = MibTableColumn
cucsFeatureDefinitionRn = _CucsFeatureDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 2, 1, 3),
    _CucsFeatureDefinitionRn_Type()
)
cucsFeatureDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionRn.setStatus("current")
_CucsFeatureDefinitionDescription_Type = SnmpAdminString
_CucsFeatureDefinitionDescription_Object = MibTableColumn
cucsFeatureDefinitionDescription = _CucsFeatureDefinitionDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 2, 1, 4),
    _CucsFeatureDefinitionDescription_Type()
)
cucsFeatureDefinitionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionDescription.setStatus("current")
_CucsFeatureDefinitionName_Type = SnmpAdminString
_CucsFeatureDefinitionName_Object = MibTableColumn
cucsFeatureDefinitionName = _CucsFeatureDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 2, 1, 5),
    _CucsFeatureDefinitionName_Type()
)
cucsFeatureDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionName.setStatus("current")
_CucsFeatureDefinitionRevision_Type = SnmpAdminString
_CucsFeatureDefinitionRevision_Object = MibTableColumn
cucsFeatureDefinitionRevision = _CucsFeatureDefinitionRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 2, 1, 6),
    _CucsFeatureDefinitionRevision_Type()
)
cucsFeatureDefinitionRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionRevision.setStatus("current")
_CucsFeatureDefinitionInstanceTable_Object = MibTable
cucsFeatureDefinitionInstanceTable = _CucsFeatureDefinitionInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 3)
)
if mibBuilder.loadTexts:
    cucsFeatureDefinitionInstanceTable.setStatus("current")
_CucsFeatureDefinitionInstanceEntry_Object = MibTableRow
cucsFeatureDefinitionInstanceEntry = _CucsFeatureDefinitionInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 3, 1)
)
cucsFeatureDefinitionInstanceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FEATURE-MIB", "cucsFeatureDefinitionInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFeatureDefinitionInstanceEntry.setStatus("current")
_CucsFeatureDefinitionInstanceInstanceId_Type = CucsManagedObjectId
_CucsFeatureDefinitionInstanceInstanceId_Object = MibTableColumn
cucsFeatureDefinitionInstanceInstanceId = _CucsFeatureDefinitionInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 3, 1, 1),
    _CucsFeatureDefinitionInstanceInstanceId_Type()
)
cucsFeatureDefinitionInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionInstanceInstanceId.setStatus("current")
_CucsFeatureDefinitionInstanceDn_Type = CucsManagedObjectDn
_CucsFeatureDefinitionInstanceDn_Object = MibTableColumn
cucsFeatureDefinitionInstanceDn = _CucsFeatureDefinitionInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 3, 1, 2),
    _CucsFeatureDefinitionInstanceDn_Type()
)
cucsFeatureDefinitionInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionInstanceDn.setStatus("current")
_CucsFeatureDefinitionInstanceRn_Type = SnmpAdminString
_CucsFeatureDefinitionInstanceRn_Object = MibTableColumn
cucsFeatureDefinitionInstanceRn = _CucsFeatureDefinitionInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 3, 1, 3),
    _CucsFeatureDefinitionInstanceRn_Type()
)
cucsFeatureDefinitionInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionInstanceRn.setStatus("current")
_CucsFeatureDefinitionInstanceName_Type = SnmpAdminString
_CucsFeatureDefinitionInstanceName_Object = MibTableColumn
cucsFeatureDefinitionInstanceName = _CucsFeatureDefinitionInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 3, 1, 4),
    _CucsFeatureDefinitionInstanceName_Type()
)
cucsFeatureDefinitionInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionInstanceName.setStatus("current")
_CucsFeatureDefinitionInstanceRevision_Type = SnmpAdminString
_CucsFeatureDefinitionInstanceRevision_Object = MibTableColumn
cucsFeatureDefinitionInstanceRevision = _CucsFeatureDefinitionInstanceRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 3, 1, 5),
    _CucsFeatureDefinitionInstanceRevision_Type()
)
cucsFeatureDefinitionInstanceRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionInstanceRevision.setStatus("current")
_CucsFeatureDefinitionInstanceSupportability_Type = CucsFeatureSupportabilityType
_CucsFeatureDefinitionInstanceSupportability_Object = MibTableColumn
cucsFeatureDefinitionInstanceSupportability = _CucsFeatureDefinitionInstanceSupportability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 3, 1, 6),
    _CucsFeatureDefinitionInstanceSupportability_Type()
)
cucsFeatureDefinitionInstanceSupportability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionInstanceSupportability.setStatus("current")
_CucsFeatureDefinitionInstanceTargetDn_Type = SnmpAdminString
_CucsFeatureDefinitionInstanceTargetDn_Object = MibTableColumn
cucsFeatureDefinitionInstanceTargetDn = _CucsFeatureDefinitionInstanceTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 3, 1, 7),
    _CucsFeatureDefinitionInstanceTargetDn_Type()
)
cucsFeatureDefinitionInstanceTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionInstanceTargetDn.setStatus("current")
_CucsFeatureDefinitionRefTable_Object = MibTable
cucsFeatureDefinitionRefTable = _CucsFeatureDefinitionRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 4)
)
if mibBuilder.loadTexts:
    cucsFeatureDefinitionRefTable.setStatus("current")
_CucsFeatureDefinitionRefEntry_Object = MibTableRow
cucsFeatureDefinitionRefEntry = _CucsFeatureDefinitionRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 4, 1)
)
cucsFeatureDefinitionRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FEATURE-MIB", "cucsFeatureDefinitionRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFeatureDefinitionRefEntry.setStatus("current")
_CucsFeatureDefinitionRefInstanceId_Type = CucsManagedObjectId
_CucsFeatureDefinitionRefInstanceId_Object = MibTableColumn
cucsFeatureDefinitionRefInstanceId = _CucsFeatureDefinitionRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 4, 1, 1),
    _CucsFeatureDefinitionRefInstanceId_Type()
)
cucsFeatureDefinitionRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionRefInstanceId.setStatus("current")
_CucsFeatureDefinitionRefDn_Type = CucsManagedObjectDn
_CucsFeatureDefinitionRefDn_Object = MibTableColumn
cucsFeatureDefinitionRefDn = _CucsFeatureDefinitionRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 4, 1, 2),
    _CucsFeatureDefinitionRefDn_Type()
)
cucsFeatureDefinitionRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionRefDn.setStatus("current")
_CucsFeatureDefinitionRefRn_Type = SnmpAdminString
_CucsFeatureDefinitionRefRn_Object = MibTableColumn
cucsFeatureDefinitionRefRn = _CucsFeatureDefinitionRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 4, 1, 3),
    _CucsFeatureDefinitionRefRn_Type()
)
cucsFeatureDefinitionRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionRefRn.setStatus("current")
_CucsFeatureDefinitionRefName_Type = SnmpAdminString
_CucsFeatureDefinitionRefName_Object = MibTableColumn
cucsFeatureDefinitionRefName = _CucsFeatureDefinitionRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 4, 1, 4),
    _CucsFeatureDefinitionRefName_Type()
)
cucsFeatureDefinitionRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionRefName.setStatus("current")
_CucsFeatureDefinitionRefRevision_Type = SnmpAdminString
_CucsFeatureDefinitionRefRevision_Object = MibTableColumn
cucsFeatureDefinitionRefRevision = _CucsFeatureDefinitionRefRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 4, 1, 5),
    _CucsFeatureDefinitionRefRevision_Type()
)
cucsFeatureDefinitionRefRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionRefRevision.setStatus("current")
_CucsFeatureDefinitionRefSupportability_Type = CucsFeatureSupportabilityType
_CucsFeatureDefinitionRefSupportability_Object = MibTableColumn
cucsFeatureDefinitionRefSupportability = _CucsFeatureDefinitionRefSupportability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 4, 1, 6),
    _CucsFeatureDefinitionRefSupportability_Type()
)
cucsFeatureDefinitionRefSupportability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionRefSupportability.setStatus("current")
_CucsFeatureDefinitionRefTargetDn_Type = SnmpAdminString
_CucsFeatureDefinitionRefTargetDn_Object = MibTableColumn
cucsFeatureDefinitionRefTargetDn = _CucsFeatureDefinitionRefTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 4, 1, 7),
    _CucsFeatureDefinitionRefTargetDn_Type()
)
cucsFeatureDefinitionRefTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureDefinitionRefTargetDn.setStatus("current")
_CucsFeatureFruCapProviderInstanceTable_Object = MibTable
cucsFeatureFruCapProviderInstanceTable = _CucsFeatureFruCapProviderInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 5)
)
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderInstanceTable.setStatus("current")
_CucsFeatureFruCapProviderInstanceEntry_Object = MibTableRow
cucsFeatureFruCapProviderInstanceEntry = _CucsFeatureFruCapProviderInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 5, 1)
)
cucsFeatureFruCapProviderInstanceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FEATURE-MIB", "cucsFeatureFruCapProviderInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderInstanceEntry.setStatus("current")
_CucsFeatureFruCapProviderInstanceInstanceId_Type = CucsManagedObjectId
_CucsFeatureFruCapProviderInstanceInstanceId_Object = MibTableColumn
cucsFeatureFruCapProviderInstanceInstanceId = _CucsFeatureFruCapProviderInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 5, 1, 1),
    _CucsFeatureFruCapProviderInstanceInstanceId_Type()
)
cucsFeatureFruCapProviderInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderInstanceInstanceId.setStatus("current")
_CucsFeatureFruCapProviderInstanceDn_Type = CucsManagedObjectDn
_CucsFeatureFruCapProviderInstanceDn_Object = MibTableColumn
cucsFeatureFruCapProviderInstanceDn = _CucsFeatureFruCapProviderInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 5, 1, 2),
    _CucsFeatureFruCapProviderInstanceDn_Type()
)
cucsFeatureFruCapProviderInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderInstanceDn.setStatus("current")
_CucsFeatureFruCapProviderInstanceRn_Type = SnmpAdminString
_CucsFeatureFruCapProviderInstanceRn_Object = MibTableColumn
cucsFeatureFruCapProviderInstanceRn = _CucsFeatureFruCapProviderInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 5, 1, 3),
    _CucsFeatureFruCapProviderInstanceRn_Type()
)
cucsFeatureFruCapProviderInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderInstanceRn.setStatus("current")
_CucsFeatureFruCapProviderInstanceModel_Type = SnmpAdminString
_CucsFeatureFruCapProviderInstanceModel_Object = MibTableColumn
cucsFeatureFruCapProviderInstanceModel = _CucsFeatureFruCapProviderInstanceModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 5, 1, 4),
    _CucsFeatureFruCapProviderInstanceModel_Type()
)
cucsFeatureFruCapProviderInstanceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderInstanceModel.setStatus("current")
_CucsFeatureFruCapProviderInstanceRevision_Type = SnmpAdminString
_CucsFeatureFruCapProviderInstanceRevision_Object = MibTableColumn
cucsFeatureFruCapProviderInstanceRevision = _CucsFeatureFruCapProviderInstanceRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 5, 1, 5),
    _CucsFeatureFruCapProviderInstanceRevision_Type()
)
cucsFeatureFruCapProviderInstanceRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderInstanceRevision.setStatus("current")
_CucsFeatureFruCapProviderInstanceSupportability_Type = CucsFeatureSupportabilityType
_CucsFeatureFruCapProviderInstanceSupportability_Object = MibTableColumn
cucsFeatureFruCapProviderInstanceSupportability = _CucsFeatureFruCapProviderInstanceSupportability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 5, 1, 6),
    _CucsFeatureFruCapProviderInstanceSupportability_Type()
)
cucsFeatureFruCapProviderInstanceSupportability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderInstanceSupportability.setStatus("current")
_CucsFeatureFruCapProviderInstanceTargetDn_Type = SnmpAdminString
_CucsFeatureFruCapProviderInstanceTargetDn_Object = MibTableColumn
cucsFeatureFruCapProviderInstanceTargetDn = _CucsFeatureFruCapProviderInstanceTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 5, 1, 7),
    _CucsFeatureFruCapProviderInstanceTargetDn_Type()
)
cucsFeatureFruCapProviderInstanceTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderInstanceTargetDn.setStatus("current")
_CucsFeatureFruCapProviderInstanceVendor_Type = SnmpAdminString
_CucsFeatureFruCapProviderInstanceVendor_Object = MibTableColumn
cucsFeatureFruCapProviderInstanceVendor = _CucsFeatureFruCapProviderInstanceVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 5, 1, 8),
    _CucsFeatureFruCapProviderInstanceVendor_Type()
)
cucsFeatureFruCapProviderInstanceVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderInstanceVendor.setStatus("current")
_CucsFeatureFruCapProviderRefTable_Object = MibTable
cucsFeatureFruCapProviderRefTable = _CucsFeatureFruCapProviderRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 6)
)
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderRefTable.setStatus("current")
_CucsFeatureFruCapProviderRefEntry_Object = MibTableRow
cucsFeatureFruCapProviderRefEntry = _CucsFeatureFruCapProviderRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 6, 1)
)
cucsFeatureFruCapProviderRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FEATURE-MIB", "cucsFeatureFruCapProviderRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderRefEntry.setStatus("current")
_CucsFeatureFruCapProviderRefInstanceId_Type = CucsManagedObjectId
_CucsFeatureFruCapProviderRefInstanceId_Object = MibTableColumn
cucsFeatureFruCapProviderRefInstanceId = _CucsFeatureFruCapProviderRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 6, 1, 1),
    _CucsFeatureFruCapProviderRefInstanceId_Type()
)
cucsFeatureFruCapProviderRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderRefInstanceId.setStatus("current")
_CucsFeatureFruCapProviderRefDn_Type = CucsManagedObjectDn
_CucsFeatureFruCapProviderRefDn_Object = MibTableColumn
cucsFeatureFruCapProviderRefDn = _CucsFeatureFruCapProviderRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 6, 1, 2),
    _CucsFeatureFruCapProviderRefDn_Type()
)
cucsFeatureFruCapProviderRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderRefDn.setStatus("current")
_CucsFeatureFruCapProviderRefRn_Type = SnmpAdminString
_CucsFeatureFruCapProviderRefRn_Object = MibTableColumn
cucsFeatureFruCapProviderRefRn = _CucsFeatureFruCapProviderRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 6, 1, 3),
    _CucsFeatureFruCapProviderRefRn_Type()
)
cucsFeatureFruCapProviderRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderRefRn.setStatus("current")
_CucsFeatureFruCapProviderRefModel_Type = SnmpAdminString
_CucsFeatureFruCapProviderRefModel_Object = MibTableColumn
cucsFeatureFruCapProviderRefModel = _CucsFeatureFruCapProviderRefModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 6, 1, 4),
    _CucsFeatureFruCapProviderRefModel_Type()
)
cucsFeatureFruCapProviderRefModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderRefModel.setStatus("current")
_CucsFeatureFruCapProviderRefRevision_Type = SnmpAdminString
_CucsFeatureFruCapProviderRefRevision_Object = MibTableColumn
cucsFeatureFruCapProviderRefRevision = _CucsFeatureFruCapProviderRefRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 6, 1, 5),
    _CucsFeatureFruCapProviderRefRevision_Type()
)
cucsFeatureFruCapProviderRefRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderRefRevision.setStatus("current")
_CucsFeatureFruCapProviderRefSupportability_Type = CucsFeatureSupportabilityType
_CucsFeatureFruCapProviderRefSupportability_Object = MibTableColumn
cucsFeatureFruCapProviderRefSupportability = _CucsFeatureFruCapProviderRefSupportability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 6, 1, 6),
    _CucsFeatureFruCapProviderRefSupportability_Type()
)
cucsFeatureFruCapProviderRefSupportability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderRefSupportability.setStatus("current")
_CucsFeatureFruCapProviderRefTargetDn_Type = SnmpAdminString
_CucsFeatureFruCapProviderRefTargetDn_Object = MibTableColumn
cucsFeatureFruCapProviderRefTargetDn = _CucsFeatureFruCapProviderRefTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 6, 1, 7),
    _CucsFeatureFruCapProviderRefTargetDn_Type()
)
cucsFeatureFruCapProviderRefTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderRefTargetDn.setStatus("current")
_CucsFeatureFruCapProviderRefVendor_Type = SnmpAdminString
_CucsFeatureFruCapProviderRefVendor_Object = MibTableColumn
cucsFeatureFruCapProviderRefVendor = _CucsFeatureFruCapProviderRefVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 6, 1, 8),
    _CucsFeatureFruCapProviderRefVendor_Type()
)
cucsFeatureFruCapProviderRefVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureFruCapProviderRefVendor.setStatus("current")
_CucsFeatureProviderTable_Object = MibTable
cucsFeatureProviderTable = _CucsFeatureProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 7)
)
if mibBuilder.loadTexts:
    cucsFeatureProviderTable.setStatus("current")
_CucsFeatureProviderEntry_Object = MibTableRow
cucsFeatureProviderEntry = _CucsFeatureProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 7, 1)
)
cucsFeatureProviderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FEATURE-MIB", "cucsFeatureProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFeatureProviderEntry.setStatus("current")
_CucsFeatureProviderInstanceId_Type = CucsManagedObjectId
_CucsFeatureProviderInstanceId_Object = MibTableColumn
cucsFeatureProviderInstanceId = _CucsFeatureProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 7, 1, 1),
    _CucsFeatureProviderInstanceId_Type()
)
cucsFeatureProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFeatureProviderInstanceId.setStatus("current")
_CucsFeatureProviderDn_Type = CucsManagedObjectDn
_CucsFeatureProviderDn_Object = MibTableColumn
cucsFeatureProviderDn = _CucsFeatureProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 7, 1, 2),
    _CucsFeatureProviderDn_Type()
)
cucsFeatureProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureProviderDn.setStatus("current")
_CucsFeatureProviderRn_Type = SnmpAdminString
_CucsFeatureProviderRn_Object = MibTableColumn
cucsFeatureProviderRn = _CucsFeatureProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 7, 1, 3),
    _CucsFeatureProviderRn_Type()
)
cucsFeatureProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureProviderRn.setStatus("current")
_CucsFeatureProviderName_Type = SnmpAdminString
_CucsFeatureProviderName_Object = MibTableColumn
cucsFeatureProviderName = _CucsFeatureProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 7, 1, 4),
    _CucsFeatureProviderName_Type()
)
cucsFeatureProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureProviderName.setStatus("current")
_CucsFeatureProviderInstanceTable_Object = MibTable
cucsFeatureProviderInstanceTable = _CucsFeatureProviderInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 8)
)
if mibBuilder.loadTexts:
    cucsFeatureProviderInstanceTable.setStatus("current")
_CucsFeatureProviderInstanceEntry_Object = MibTableRow
cucsFeatureProviderInstanceEntry = _CucsFeatureProviderInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 8, 1)
)
cucsFeatureProviderInstanceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FEATURE-MIB", "cucsFeatureProviderInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFeatureProviderInstanceEntry.setStatus("current")
_CucsFeatureProviderInstanceInstanceId_Type = CucsManagedObjectId
_CucsFeatureProviderInstanceInstanceId_Object = MibTableColumn
cucsFeatureProviderInstanceInstanceId = _CucsFeatureProviderInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 8, 1, 1),
    _CucsFeatureProviderInstanceInstanceId_Type()
)
cucsFeatureProviderInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFeatureProviderInstanceInstanceId.setStatus("current")
_CucsFeatureProviderInstanceDn_Type = CucsManagedObjectDn
_CucsFeatureProviderInstanceDn_Object = MibTableColumn
cucsFeatureProviderInstanceDn = _CucsFeatureProviderInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 8, 1, 2),
    _CucsFeatureProviderInstanceDn_Type()
)
cucsFeatureProviderInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureProviderInstanceDn.setStatus("current")
_CucsFeatureProviderInstanceRn_Type = SnmpAdminString
_CucsFeatureProviderInstanceRn_Object = MibTableColumn
cucsFeatureProviderInstanceRn = _CucsFeatureProviderInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 8, 1, 3),
    _CucsFeatureProviderInstanceRn_Type()
)
cucsFeatureProviderInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureProviderInstanceRn.setStatus("current")
_CucsFeatureProviderInstanceName_Type = SnmpAdminString
_CucsFeatureProviderInstanceName_Object = MibTableColumn
cucsFeatureProviderInstanceName = _CucsFeatureProviderInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 8, 1, 4),
    _CucsFeatureProviderInstanceName_Type()
)
cucsFeatureProviderInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureProviderInstanceName.setStatus("current")
_CucsFeatureProviderInstanceOperProviderDn_Type = SnmpAdminString
_CucsFeatureProviderInstanceOperProviderDn_Object = MibTableColumn
cucsFeatureProviderInstanceOperProviderDn = _CucsFeatureProviderInstanceOperProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 77, 8, 1, 5),
    _CucsFeatureProviderInstanceOperProviderDn_Type()
)
cucsFeatureProviderInstanceOperProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFeatureProviderInstanceOperProviderDn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-FEATURE-MIB",
    **{"cucsFeatureObjects": cucsFeatureObjects,
       "cucsFeatureContextEpTable": cucsFeatureContextEpTable,
       "cucsFeatureContextEpEntry": cucsFeatureContextEpEntry,
       "cucsFeatureContextEpInstanceId": cucsFeatureContextEpInstanceId,
       "cucsFeatureContextEpDn": cucsFeatureContextEpDn,
       "cucsFeatureContextEpRn": cucsFeatureContextEpRn,
       "cucsFeatureDefinitionTable": cucsFeatureDefinitionTable,
       "cucsFeatureDefinitionEntry": cucsFeatureDefinitionEntry,
       "cucsFeatureDefinitionInstanceId": cucsFeatureDefinitionInstanceId,
       "cucsFeatureDefinitionDn": cucsFeatureDefinitionDn,
       "cucsFeatureDefinitionRn": cucsFeatureDefinitionRn,
       "cucsFeatureDefinitionDescription": cucsFeatureDefinitionDescription,
       "cucsFeatureDefinitionName": cucsFeatureDefinitionName,
       "cucsFeatureDefinitionRevision": cucsFeatureDefinitionRevision,
       "cucsFeatureDefinitionInstanceTable": cucsFeatureDefinitionInstanceTable,
       "cucsFeatureDefinitionInstanceEntry": cucsFeatureDefinitionInstanceEntry,
       "cucsFeatureDefinitionInstanceInstanceId": cucsFeatureDefinitionInstanceInstanceId,
       "cucsFeatureDefinitionInstanceDn": cucsFeatureDefinitionInstanceDn,
       "cucsFeatureDefinitionInstanceRn": cucsFeatureDefinitionInstanceRn,
       "cucsFeatureDefinitionInstanceName": cucsFeatureDefinitionInstanceName,
       "cucsFeatureDefinitionInstanceRevision": cucsFeatureDefinitionInstanceRevision,
       "cucsFeatureDefinitionInstanceSupportability": cucsFeatureDefinitionInstanceSupportability,
       "cucsFeatureDefinitionInstanceTargetDn": cucsFeatureDefinitionInstanceTargetDn,
       "cucsFeatureDefinitionRefTable": cucsFeatureDefinitionRefTable,
       "cucsFeatureDefinitionRefEntry": cucsFeatureDefinitionRefEntry,
       "cucsFeatureDefinitionRefInstanceId": cucsFeatureDefinitionRefInstanceId,
       "cucsFeatureDefinitionRefDn": cucsFeatureDefinitionRefDn,
       "cucsFeatureDefinitionRefRn": cucsFeatureDefinitionRefRn,
       "cucsFeatureDefinitionRefName": cucsFeatureDefinitionRefName,
       "cucsFeatureDefinitionRefRevision": cucsFeatureDefinitionRefRevision,
       "cucsFeatureDefinitionRefSupportability": cucsFeatureDefinitionRefSupportability,
       "cucsFeatureDefinitionRefTargetDn": cucsFeatureDefinitionRefTargetDn,
       "cucsFeatureFruCapProviderInstanceTable": cucsFeatureFruCapProviderInstanceTable,
       "cucsFeatureFruCapProviderInstanceEntry": cucsFeatureFruCapProviderInstanceEntry,
       "cucsFeatureFruCapProviderInstanceInstanceId": cucsFeatureFruCapProviderInstanceInstanceId,
       "cucsFeatureFruCapProviderInstanceDn": cucsFeatureFruCapProviderInstanceDn,
       "cucsFeatureFruCapProviderInstanceRn": cucsFeatureFruCapProviderInstanceRn,
       "cucsFeatureFruCapProviderInstanceModel": cucsFeatureFruCapProviderInstanceModel,
       "cucsFeatureFruCapProviderInstanceRevision": cucsFeatureFruCapProviderInstanceRevision,
       "cucsFeatureFruCapProviderInstanceSupportability": cucsFeatureFruCapProviderInstanceSupportability,
       "cucsFeatureFruCapProviderInstanceTargetDn": cucsFeatureFruCapProviderInstanceTargetDn,
       "cucsFeatureFruCapProviderInstanceVendor": cucsFeatureFruCapProviderInstanceVendor,
       "cucsFeatureFruCapProviderRefTable": cucsFeatureFruCapProviderRefTable,
       "cucsFeatureFruCapProviderRefEntry": cucsFeatureFruCapProviderRefEntry,
       "cucsFeatureFruCapProviderRefInstanceId": cucsFeatureFruCapProviderRefInstanceId,
       "cucsFeatureFruCapProviderRefDn": cucsFeatureFruCapProviderRefDn,
       "cucsFeatureFruCapProviderRefRn": cucsFeatureFruCapProviderRefRn,
       "cucsFeatureFruCapProviderRefModel": cucsFeatureFruCapProviderRefModel,
       "cucsFeatureFruCapProviderRefRevision": cucsFeatureFruCapProviderRefRevision,
       "cucsFeatureFruCapProviderRefSupportability": cucsFeatureFruCapProviderRefSupportability,
       "cucsFeatureFruCapProviderRefTargetDn": cucsFeatureFruCapProviderRefTargetDn,
       "cucsFeatureFruCapProviderRefVendor": cucsFeatureFruCapProviderRefVendor,
       "cucsFeatureProviderTable": cucsFeatureProviderTable,
       "cucsFeatureProviderEntry": cucsFeatureProviderEntry,
       "cucsFeatureProviderInstanceId": cucsFeatureProviderInstanceId,
       "cucsFeatureProviderDn": cucsFeatureProviderDn,
       "cucsFeatureProviderRn": cucsFeatureProviderRn,
       "cucsFeatureProviderName": cucsFeatureProviderName,
       "cucsFeatureProviderInstanceTable": cucsFeatureProviderInstanceTable,
       "cucsFeatureProviderInstanceEntry": cucsFeatureProviderInstanceEntry,
       "cucsFeatureProviderInstanceInstanceId": cucsFeatureProviderInstanceInstanceId,
       "cucsFeatureProviderInstanceDn": cucsFeatureProviderInstanceDn,
       "cucsFeatureProviderInstanceRn": cucsFeatureProviderInstanceRn,
       "cucsFeatureProviderInstanceName": cucsFeatureProviderInstanceName,
       "cucsFeatureProviderInstanceOperProviderDn": cucsFeatureProviderInstanceOperProviderDn}
)
