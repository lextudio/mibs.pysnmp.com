# SNMP MIB module (CISCO-ENTITY-ASSET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-ASSET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:30 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoEntityAssetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 92)
)
ciscoEntityAssetMIB.setRevisions(
        ("2003-09-18 00:00",
         "2002-07-23 16:00",
         "1999-06-02 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoEntityAssetMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEntityAssetMIBObjects = _CiscoEntityAssetMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 1)
)
_CeAssetTable_Object = MibTable
ceAssetTable = _CeAssetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1)
)
if mibBuilder.loadTexts:
    ceAssetTable.setStatus("current")
_CeAssetEntry_Object = MibTableRow
ceAssetEntry = _CeAssetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1)
)
ceAssetEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ceAssetEntry.setStatus("current")
_CeAssetOEMString_Type = SnmpAdminString
_CeAssetOEMString_Object = MibTableColumn
ceAssetOEMString = _CeAssetOEMString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 1),
    _CeAssetOEMString_Type()
)
ceAssetOEMString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAssetOEMString.setStatus("deprecated")
_CeAssetSerialNumber_Type = SnmpAdminString
_CeAssetSerialNumber_Object = MibTableColumn
ceAssetSerialNumber = _CeAssetSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 2),
    _CeAssetSerialNumber_Type()
)
ceAssetSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAssetSerialNumber.setStatus("deprecated")
_CeAssetOrderablePartNumber_Type = SnmpAdminString
_CeAssetOrderablePartNumber_Object = MibTableColumn
ceAssetOrderablePartNumber = _CeAssetOrderablePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 3),
    _CeAssetOrderablePartNumber_Type()
)
ceAssetOrderablePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAssetOrderablePartNumber.setStatus("deprecated")
_CeAssetHardwareRevision_Type = SnmpAdminString
_CeAssetHardwareRevision_Object = MibTableColumn
ceAssetHardwareRevision = _CeAssetHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 4),
    _CeAssetHardwareRevision_Type()
)
ceAssetHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAssetHardwareRevision.setStatus("deprecated")
_CeAssetMfgAssyNumber_Type = SnmpAdminString
_CeAssetMfgAssyNumber_Object = MibTableColumn
ceAssetMfgAssyNumber = _CeAssetMfgAssyNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 5),
    _CeAssetMfgAssyNumber_Type()
)
ceAssetMfgAssyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAssetMfgAssyNumber.setStatus("current")
_CeAssetMfgAssyRevision_Type = SnmpAdminString
_CeAssetMfgAssyRevision_Object = MibTableColumn
ceAssetMfgAssyRevision = _CeAssetMfgAssyRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 6),
    _CeAssetMfgAssyRevision_Type()
)
ceAssetMfgAssyRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAssetMfgAssyRevision.setStatus("current")
_CeAssetFirmwareID_Type = SnmpAdminString
_CeAssetFirmwareID_Object = MibTableColumn
ceAssetFirmwareID = _CeAssetFirmwareID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 7),
    _CeAssetFirmwareID_Type()
)
ceAssetFirmwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAssetFirmwareID.setStatus("deprecated")
_CeAssetFirmwareRevision_Type = SnmpAdminString
_CeAssetFirmwareRevision_Object = MibTableColumn
ceAssetFirmwareRevision = _CeAssetFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 8),
    _CeAssetFirmwareRevision_Type()
)
ceAssetFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAssetFirmwareRevision.setStatus("deprecated")
_CeAssetSoftwareID_Type = SnmpAdminString
_CeAssetSoftwareID_Object = MibTableColumn
ceAssetSoftwareID = _CeAssetSoftwareID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 9),
    _CeAssetSoftwareID_Type()
)
ceAssetSoftwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAssetSoftwareID.setStatus("deprecated")
_CeAssetSoftwareRevision_Type = SnmpAdminString
_CeAssetSoftwareRevision_Object = MibTableColumn
ceAssetSoftwareRevision = _CeAssetSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 10),
    _CeAssetSoftwareRevision_Type()
)
ceAssetSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAssetSoftwareRevision.setStatus("deprecated")


class _CeAssetCLEI_Type(SnmpAdminString):
    """Custom type ceAssetCLEI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 10),
    )


_CeAssetCLEI_Type.__name__ = "SnmpAdminString"
_CeAssetCLEI_Object = MibTableColumn
ceAssetCLEI = _CeAssetCLEI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 11),
    _CeAssetCLEI_Type()
)
ceAssetCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAssetCLEI.setStatus("current")


class _CeAssetAlias_Type(SnmpAdminString):
    """Custom type ceAssetAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CeAssetAlias_Type.__name__ = "SnmpAdminString"
_CeAssetAlias_Object = MibTableColumn
ceAssetAlias = _CeAssetAlias_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 12),
    _CeAssetAlias_Type()
)
ceAssetAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceAssetAlias.setStatus("deprecated")


class _CeAssetTag_Type(SnmpAdminString):
    """Custom type ceAssetTag based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CeAssetTag_Type.__name__ = "SnmpAdminString"
_CeAssetTag_Object = MibTableColumn
ceAssetTag = _CeAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 13),
    _CeAssetTag_Type()
)
ceAssetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceAssetTag.setStatus("deprecated")
_CeAssetIsFRU_Type = TruthValue
_CeAssetIsFRU_Object = MibTableColumn
ceAssetIsFRU = _CeAssetIsFRU_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 1, 1, 1, 14),
    _CeAssetIsFRU_Type()
)
ceAssetIsFRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAssetIsFRU.setStatus("deprecated")
_CiscoEntityAssetMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoEntityAssetMIBNotificationsPrefix = _CiscoEntityAssetMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 2)
)
_CiscoEntityAssetMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoEntityAssetMIBNotifications = _CiscoEntityAssetMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 2, 0)
)
_CiscoEntityAssetMIBConformance_ObjectIdentity = ObjectIdentity
ciscoEntityAssetMIBConformance = _CiscoEntityAssetMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 3)
)
_CiscoEntityAssetMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEntityAssetMIBCompliances = _CiscoEntityAssetMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 1)
)
_CiscoEntityAssetMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEntityAssetMIBGroups = _CiscoEntityAssetMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 2)
)

# Managed Objects groups

ceAssetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 2, 1)
)
ceAssetGroup.setObjects(
      *(("CISCO-ENTITY-ASSET-MIB", "ceAssetOEMString"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetSerialNumber"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetOrderablePartNumber"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetHardwareRevision"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetMfgAssyNumber"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetMfgAssyRevision"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetFirmwareID"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetFirmwareRevision"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetSoftwareID"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetSoftwareRevision"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetCLEI"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetAlias"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetTag"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetIsFRU"))
)
if mibBuilder.loadTexts:
    ceAssetGroup.setStatus("deprecated")

ceAssetGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 2, 2)
)
ceAssetGroupRev1.setObjects(
      *(("CISCO-ENTITY-ASSET-MIB", "ceAssetOEMString"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetMfgAssyNumber"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetMfgAssyRevision"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetFirmwareID"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetSoftwareID"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetCLEI"))
)
if mibBuilder.loadTexts:
    ceAssetGroupRev1.setStatus("deprecated")

ceAssetEntityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 2, 3)
)
ceAssetEntityGroup.setObjects(
      *(("CISCO-ENTITY-ASSET-MIB", "ceAssetOrderablePartNumber"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetSerialNumber"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetHardwareRevision"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetFirmwareRevision"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetSoftwareRevision"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetAlias"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetTag"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetIsFRU"))
)
if mibBuilder.loadTexts:
    ceAssetEntityGroup.setStatus("deprecated")

ceAssetGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 2, 4)
)
ceAssetGroupRev2.setObjects(
      *(("CISCO-ENTITY-ASSET-MIB", "ceAssetMfgAssyNumber"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetMfgAssyRevision"),
        ("CISCO-ENTITY-ASSET-MIB", "ceAssetCLEI"))
)
if mibBuilder.loadTexts:
    ceAssetGroupRev2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoEntityAssetMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoEntityAssetMIBCompliance.setStatus(
        "deprecated"
    )

ciscoEntityAssetMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoEntityAssetMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoEntityAssetMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 92, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoEntityAssetMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-ASSET-MIB",
    **{"ciscoEntityAssetMIB": ciscoEntityAssetMIB,
       "ciscoEntityAssetMIBObjects": ciscoEntityAssetMIBObjects,
       "ceAssetTable": ceAssetTable,
       "ceAssetEntry": ceAssetEntry,
       "ceAssetOEMString": ceAssetOEMString,
       "ceAssetSerialNumber": ceAssetSerialNumber,
       "ceAssetOrderablePartNumber": ceAssetOrderablePartNumber,
       "ceAssetHardwareRevision": ceAssetHardwareRevision,
       "ceAssetMfgAssyNumber": ceAssetMfgAssyNumber,
       "ceAssetMfgAssyRevision": ceAssetMfgAssyRevision,
       "ceAssetFirmwareID": ceAssetFirmwareID,
       "ceAssetFirmwareRevision": ceAssetFirmwareRevision,
       "ceAssetSoftwareID": ceAssetSoftwareID,
       "ceAssetSoftwareRevision": ceAssetSoftwareRevision,
       "ceAssetCLEI": ceAssetCLEI,
       "ceAssetAlias": ceAssetAlias,
       "ceAssetTag": ceAssetTag,
       "ceAssetIsFRU": ceAssetIsFRU,
       "ciscoEntityAssetMIBNotificationsPrefix": ciscoEntityAssetMIBNotificationsPrefix,
       "ciscoEntityAssetMIBNotifications": ciscoEntityAssetMIBNotifications,
       "ciscoEntityAssetMIBConformance": ciscoEntityAssetMIBConformance,
       "ciscoEntityAssetMIBCompliances": ciscoEntityAssetMIBCompliances,
       "ciscoEntityAssetMIBCompliance": ciscoEntityAssetMIBCompliance,
       "ciscoEntityAssetMIBComplianceRev1": ciscoEntityAssetMIBComplianceRev1,
       "ciscoEntityAssetMIBComplianceRev2": ciscoEntityAssetMIBComplianceRev2,
       "ciscoEntityAssetMIBGroups": ciscoEntityAssetMIBGroups,
       "ceAssetGroup": ceAssetGroup,
       "ceAssetGroupRev1": ceAssetGroupRev1,
       "ceAssetEntityGroup": ceAssetEntityGroup,
       "ceAssetGroupRev2": ceAssetGroupRev2}
)
