# SNMP MIB module (CISCO-CONTEXT-MAPPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CONTEXT-MAPPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:47 2024
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

(CiscoBridgeDomain,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoBridgeDomain")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoContextMappingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 468)
)
ciscoContextMappingMIB.setRevisions(
        ("2008-11-22 00:00",
         "2008-05-30 00:00",
         "2008-02-01 00:00",
         "2005-03-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CContextMappingMIBObjects_ObjectIdentity = ObjectIdentity
cContextMappingMIBObjects = _CContextMappingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1)
)
_CContextMappingTable_Object = MibTable
cContextMappingTable = _CContextMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 1)
)
if mibBuilder.loadTexts:
    cContextMappingTable.setStatus("current")
_CContextMappingEntry_Object = MibTableRow
cContextMappingEntry = _CContextMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 1, 1)
)
cContextMappingEntry.setIndexNames(
    (0, "CISCO-CONTEXT-MAPPING-MIB", "cContextMappingVacmContextName"),
)
if mibBuilder.loadTexts:
    cContextMappingEntry.setStatus("current")


class _CContextMappingVacmContextName_Type(SnmpAdminString):
    """Custom type cContextMappingVacmContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CContextMappingVacmContextName_Type.__name__ = "SnmpAdminString"
_CContextMappingVacmContextName_Object = MibTableColumn
cContextMappingVacmContextName = _CContextMappingVacmContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 1, 1, 1),
    _CContextMappingVacmContextName_Type()
)
cContextMappingVacmContextName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cContextMappingVacmContextName.setStatus("current")


class _CContextMappingVrfName_Type(SnmpAdminString):
    """Custom type cContextMappingVrfName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CContextMappingVrfName_Type.__name__ = "SnmpAdminString"
_CContextMappingVrfName_Object = MibTableColumn
cContextMappingVrfName = _CContextMappingVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 1, 1, 2),
    _CContextMappingVrfName_Type()
)
cContextMappingVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cContextMappingVrfName.setStatus("current")


class _CContextMappingTopologyName_Type(SnmpAdminString):
    """Custom type cContextMappingTopologyName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CContextMappingTopologyName_Type.__name__ = "SnmpAdminString"
_CContextMappingTopologyName_Object = MibTableColumn
cContextMappingTopologyName = _CContextMappingTopologyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 1, 1, 3),
    _CContextMappingTopologyName_Type()
)
cContextMappingTopologyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cContextMappingTopologyName.setStatus("current")


class _CContextMappingProtoInstName_Type(SnmpAdminString):
    """Custom type cContextMappingProtoInstName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CContextMappingProtoInstName_Type.__name__ = "SnmpAdminString"
_CContextMappingProtoInstName_Object = MibTableColumn
cContextMappingProtoInstName = _CContextMappingProtoInstName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 1, 1, 4),
    _CContextMappingProtoInstName_Type()
)
cContextMappingProtoInstName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cContextMappingProtoInstName.setStatus("current")


class _CContextMappingStorageType_Type(StorageType):
    """Custom type cContextMappingStorageType based on StorageType"""


_CContextMappingStorageType_Object = MibTableColumn
cContextMappingStorageType = _CContextMappingStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 1, 1, 5),
    _CContextMappingStorageType_Type()
)
cContextMappingStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cContextMappingStorageType.setStatus("current")
_CContextMappingRowStatus_Type = RowStatus
_CContextMappingRowStatus_Object = MibTableColumn
cContextMappingRowStatus = _CContextMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 1, 1, 6),
    _CContextMappingRowStatus_Type()
)
cContextMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cContextMappingRowStatus.setStatus("current")
_CContextMappingBridgeDomainTable_Object = MibTable
cContextMappingBridgeDomainTable = _CContextMappingBridgeDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 2)
)
if mibBuilder.loadTexts:
    cContextMappingBridgeDomainTable.setStatus("current")
_CContextMappingBridgeDomainEntry_Object = MibTableRow
cContextMappingBridgeDomainEntry = _CContextMappingBridgeDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 2, 1)
)
cContextMappingBridgeDomainEntry.setIndexNames(
    (0, "CISCO-CONTEXT-MAPPING-MIB", "cContextMappingVacmContextName"),
)
if mibBuilder.loadTexts:
    cContextMappingBridgeDomainEntry.setStatus("current")
_CContextMappingBridgeDomainIdentifier_Type = CiscoBridgeDomain
_CContextMappingBridgeDomainIdentifier_Object = MibTableColumn
cContextMappingBridgeDomainIdentifier = _CContextMappingBridgeDomainIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 2, 1, 1),
    _CContextMappingBridgeDomainIdentifier_Type()
)
cContextMappingBridgeDomainIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cContextMappingBridgeDomainIdentifier.setStatus("current")


class _CContextMappingBridgeDomainStorageType_Type(StorageType):
    """Custom type cContextMappingBridgeDomainStorageType based on StorageType"""


_CContextMappingBridgeDomainStorageType_Object = MibTableColumn
cContextMappingBridgeDomainStorageType = _CContextMappingBridgeDomainStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 2, 1, 2),
    _CContextMappingBridgeDomainStorageType_Type()
)
cContextMappingBridgeDomainStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cContextMappingBridgeDomainStorageType.setStatus("current")
_CContextMappingBridgeDomainRowStatus_Type = RowStatus
_CContextMappingBridgeDomainRowStatus_Object = MibTableColumn
cContextMappingBridgeDomainRowStatus = _CContextMappingBridgeDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 2, 1, 3),
    _CContextMappingBridgeDomainRowStatus_Type()
)
cContextMappingBridgeDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cContextMappingBridgeDomainRowStatus.setStatus("current")
_CContextMappingBridgeInstanceTable_Object = MibTable
cContextMappingBridgeInstanceTable = _CContextMappingBridgeInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 3)
)
if mibBuilder.loadTexts:
    cContextMappingBridgeInstanceTable.setStatus("current")
_CContextMappingBridgeInstanceEntry_Object = MibTableRow
cContextMappingBridgeInstanceEntry = _CContextMappingBridgeInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 3, 1)
)
cContextMappingBridgeInstanceEntry.setIndexNames(
    (0, "CISCO-CONTEXT-MAPPING-MIB", "cContextMappingVacmContextName"),
)
if mibBuilder.loadTexts:
    cContextMappingBridgeInstanceEntry.setStatus("current")
_CContextMappingBridgeInstName_Type = SnmpAdminString
_CContextMappingBridgeInstName_Object = MibTableColumn
cContextMappingBridgeInstName = _CContextMappingBridgeInstName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 3, 1, 1),
    _CContextMappingBridgeInstName_Type()
)
cContextMappingBridgeInstName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cContextMappingBridgeInstName.setStatus("current")


class _CContextMappingBridgeInstStorageType_Type(StorageType):
    """Custom type cContextMappingBridgeInstStorageType based on StorageType"""


_CContextMappingBridgeInstStorageType_Object = MibTableColumn
cContextMappingBridgeInstStorageType = _CContextMappingBridgeInstStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 3, 1, 2),
    _CContextMappingBridgeInstStorageType_Type()
)
cContextMappingBridgeInstStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cContextMappingBridgeInstStorageType.setStatus("current")
_CContextMappingBridgeInstRowStatus_Type = RowStatus
_CContextMappingBridgeInstRowStatus_Object = MibTableColumn
cContextMappingBridgeInstRowStatus = _CContextMappingBridgeInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 3, 1, 3),
    _CContextMappingBridgeInstRowStatus_Type()
)
cContextMappingBridgeInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cContextMappingBridgeInstRowStatus.setStatus("current")
_CContextMappingLicenseGroupTable_Object = MibTable
cContextMappingLicenseGroupTable = _CContextMappingLicenseGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 4)
)
if mibBuilder.loadTexts:
    cContextMappingLicenseGroupTable.setStatus("current")
_CContextMappingLicenseGroupEntry_Object = MibTableRow
cContextMappingLicenseGroupEntry = _CContextMappingLicenseGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 4, 1)
)
cContextMappingLicenseGroupEntry.setIndexNames(
    (0, "CISCO-CONTEXT-MAPPING-MIB", "cContextMappingVacmContextName"),
)
if mibBuilder.loadTexts:
    cContextMappingLicenseGroupEntry.setStatus("current")


class _CContextMappingLicenseGroupName_Type(SnmpAdminString):
    """Custom type cContextMappingLicenseGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CContextMappingLicenseGroupName_Type.__name__ = "SnmpAdminString"
_CContextMappingLicenseGroupName_Object = MibTableColumn
cContextMappingLicenseGroupName = _CContextMappingLicenseGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 4, 1, 1),
    _CContextMappingLicenseGroupName_Type()
)
cContextMappingLicenseGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cContextMappingLicenseGroupName.setStatus("current")


class _CContextMappingLicenseGroupStorageType_Type(StorageType):
    """Custom type cContextMappingLicenseGroupStorageType based on StorageType"""


_CContextMappingLicenseGroupStorageType_Object = MibTableColumn
cContextMappingLicenseGroupStorageType = _CContextMappingLicenseGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 4, 1, 2),
    _CContextMappingLicenseGroupStorageType_Type()
)
cContextMappingLicenseGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cContextMappingLicenseGroupStorageType.setStatus("current")
_CContextMappingLicenseGroupRowStatus_Type = RowStatus
_CContextMappingLicenseGroupRowStatus_Object = MibTableColumn
cContextMappingLicenseGroupRowStatus = _CContextMappingLicenseGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 1, 4, 1, 3),
    _CContextMappingLicenseGroupRowStatus_Type()
)
cContextMappingLicenseGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cContextMappingLicenseGroupRowStatus.setStatus("current")
_CContextMappingMIBConformance_ObjectIdentity = ObjectIdentity
cContextMappingMIBConformance = _CContextMappingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 2)
)
_CContextMappingMIBCompliances_ObjectIdentity = ObjectIdentity
cContextMappingMIBCompliances = _CContextMappingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 2, 1)
)
_CContextMappingMIBGroups_ObjectIdentity = ObjectIdentity
cContextMappingMIBGroups = _CContextMappingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 2, 2)
)

# Managed Objects groups

cContextMappingDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 2, 2, 1)
)
cContextMappingDataGroup.setObjects(
      *(("CISCO-CONTEXT-MAPPING-MIB", "cContextMappingVrfName"),
        ("CISCO-CONTEXT-MAPPING-MIB", "cContextMappingTopologyName"),
        ("CISCO-CONTEXT-MAPPING-MIB", "cContextMappingProtoInstName"),
        ("CISCO-CONTEXT-MAPPING-MIB", "cContextMappingStorageType"),
        ("CISCO-CONTEXT-MAPPING-MIB", "cContextMappingRowStatus"))
)
if mibBuilder.loadTexts:
    cContextMappingDataGroup.setStatus("current")

cContextMappingBridgeDomainDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 2, 2, 2)
)
cContextMappingBridgeDomainDataGroup.setObjects(
      *(("CISCO-CONTEXT-MAPPING-MIB", "cContextMappingBridgeDomainIdentifier"),
        ("CISCO-CONTEXT-MAPPING-MIB", "cContextMappingBridgeDomainStorageType"),
        ("CISCO-CONTEXT-MAPPING-MIB", "cContextMappingBridgeDomainRowStatus"))
)
if mibBuilder.loadTexts:
    cContextMappingBridgeDomainDataGroup.setStatus("current")

cContextMappingBridgeInstanceDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 2, 2, 3)
)
cContextMappingBridgeInstanceDataGroup.setObjects(
      *(("CISCO-CONTEXT-MAPPING-MIB", "cContextMappingBridgeInstName"),
        ("CISCO-CONTEXT-MAPPING-MIB", "cContextMappingBridgeInstStorageType"),
        ("CISCO-CONTEXT-MAPPING-MIB", "cContextMappingBridgeInstRowStatus"))
)
if mibBuilder.loadTexts:
    cContextMappingBridgeInstanceDataGroup.setStatus("current")

cContextMappingLicenseGroupDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 2, 2, 4)
)
cContextMappingLicenseGroupDataGroup.setObjects(
      *(("CISCO-CONTEXT-MAPPING-MIB", "cContextMappingLicenseGroupName"),
        ("CISCO-CONTEXT-MAPPING-MIB", "cContextMappingLicenseGroupStorageType"),
        ("CISCO-CONTEXT-MAPPING-MIB", "cContextMappingLicenseGroupStorageType"),
        ("CISCO-CONTEXT-MAPPING-MIB", "cContextMappingLicenseGroupRowStatus"))
)
if mibBuilder.loadTexts:
    cContextMappingLicenseGroupDataGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cContextMappingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cContextMappingMIBCompliance.setStatus(
        "deprecated"
    )

cContextMappingMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cContextMappingMIBComplianceRev1.setStatus(
        "deprecated"
    )

cContextMappingMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cContextMappingMIBComplianceRev2.setStatus(
        "deprecated"
    )

cContextMappingMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 468, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cContextMappingMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CONTEXT-MAPPING-MIB",
    **{"ciscoContextMappingMIB": ciscoContextMappingMIB,
       "cContextMappingMIBObjects": cContextMappingMIBObjects,
       "cContextMappingTable": cContextMappingTable,
       "cContextMappingEntry": cContextMappingEntry,
       "cContextMappingVacmContextName": cContextMappingVacmContextName,
       "cContextMappingVrfName": cContextMappingVrfName,
       "cContextMappingTopologyName": cContextMappingTopologyName,
       "cContextMappingProtoInstName": cContextMappingProtoInstName,
       "cContextMappingStorageType": cContextMappingStorageType,
       "cContextMappingRowStatus": cContextMappingRowStatus,
       "cContextMappingBridgeDomainTable": cContextMappingBridgeDomainTable,
       "cContextMappingBridgeDomainEntry": cContextMappingBridgeDomainEntry,
       "cContextMappingBridgeDomainIdentifier": cContextMappingBridgeDomainIdentifier,
       "cContextMappingBridgeDomainStorageType": cContextMappingBridgeDomainStorageType,
       "cContextMappingBridgeDomainRowStatus": cContextMappingBridgeDomainRowStatus,
       "cContextMappingBridgeInstanceTable": cContextMappingBridgeInstanceTable,
       "cContextMappingBridgeInstanceEntry": cContextMappingBridgeInstanceEntry,
       "cContextMappingBridgeInstName": cContextMappingBridgeInstName,
       "cContextMappingBridgeInstStorageType": cContextMappingBridgeInstStorageType,
       "cContextMappingBridgeInstRowStatus": cContextMappingBridgeInstRowStatus,
       "cContextMappingLicenseGroupTable": cContextMappingLicenseGroupTable,
       "cContextMappingLicenseGroupEntry": cContextMappingLicenseGroupEntry,
       "cContextMappingLicenseGroupName": cContextMappingLicenseGroupName,
       "cContextMappingLicenseGroupStorageType": cContextMappingLicenseGroupStorageType,
       "cContextMappingLicenseGroupRowStatus": cContextMappingLicenseGroupRowStatus,
       "cContextMappingMIBConformance": cContextMappingMIBConformance,
       "cContextMappingMIBCompliances": cContextMappingMIBCompliances,
       "cContextMappingMIBCompliance": cContextMappingMIBCompliance,
       "cContextMappingMIBComplianceRev1": cContextMappingMIBComplianceRev1,
       "cContextMappingMIBComplianceRev2": cContextMappingMIBComplianceRev2,
       "cContextMappingMIBComplianceRev3": cContextMappingMIBComplianceRev3,
       "cContextMappingMIBGroups": cContextMappingMIBGroups,
       "cContextMappingDataGroup": cContextMappingDataGroup,
       "cContextMappingBridgeDomainDataGroup": cContextMappingBridgeDomainDataGroup,
       "cContextMappingBridgeInstanceDataGroup": cContextMappingBridgeInstanceDataGroup,
       "cContextMappingLicenseGroupDataGroup": cContextMappingLicenseGroupDataGroup}
)
