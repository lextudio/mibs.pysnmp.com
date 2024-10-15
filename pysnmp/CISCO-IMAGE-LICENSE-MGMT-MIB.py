# SNMP MIB module (CISCO-IMAGE-LICENSE-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IMAGE-LICENSE-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:26 2024
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

ciscoImageLicenseMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 640)
)
ciscoImageLicenseMgmtMIB.setRevisions(
        ("2007-10-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BootImageLevel(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class LicenseNameList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoImageLicenseMgmtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoImageLicenseMgmtMIBNotifs = _CiscoImageLicenseMgmtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 0)
)
_CiscoImageLicenseMgmtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoImageLicenseMgmtMIBObjects = _CiscoImageLicenseMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1)
)
_CilmBootImageLevelTable_Object = MibTable
cilmBootImageLevelTable = _CilmBootImageLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1)
)
if mibBuilder.loadTexts:
    cilmBootImageLevelTable.setStatus("current")
_CilmBootImageLevelEntry_Object = MibTableRow
cilmBootImageLevelEntry = _CilmBootImageLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1)
)
cilmBootImageLevelEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmModuleName"),
)
if mibBuilder.loadTexts:
    cilmBootImageLevelEntry.setStatus("current")
_CilmModuleName_Type = SnmpAdminString
_CilmModuleName_Object = MibTableColumn
cilmModuleName = _CilmModuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 1),
    _CilmModuleName_Type()
)
cilmModuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cilmModuleName.setStatus("current")
_CilmCurrentImageLevel_Type = BootImageLevel
_CilmCurrentImageLevel_Object = MibTableColumn
cilmCurrentImageLevel = _CilmCurrentImageLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 2),
    _CilmCurrentImageLevel_Type()
)
cilmCurrentImageLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cilmCurrentImageLevel.setStatus("current")
_CilmConfiguredBootImageLevel_Type = BootImageLevel
_CilmConfiguredBootImageLevel_Object = MibTableColumn
cilmConfiguredBootImageLevel = _CilmConfiguredBootImageLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 3),
    _CilmConfiguredBootImageLevel_Type()
)
cilmConfiguredBootImageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cilmConfiguredBootImageLevel.setStatus("current")
_CilmNextBootImageLevel_Type = BootImageLevel
_CilmNextBootImageLevel_Object = MibTableColumn
cilmNextBootImageLevel = _CilmNextBootImageLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 4),
    _CilmNextBootImageLevel_Type()
)
cilmNextBootImageLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cilmNextBootImageLevel.setStatus("current")
_CilmCurrentLicenseStoreIndex_Type = Unsigned32
_CilmCurrentLicenseStoreIndex_Object = MibTableColumn
cilmCurrentLicenseStoreIndex = _CilmCurrentLicenseStoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 5),
    _CilmCurrentLicenseStoreIndex_Type()
)
cilmCurrentLicenseStoreIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cilmCurrentLicenseStoreIndex.setStatus("current")
_CilmCurrentLicenseIndex_Type = Unsigned32
_CilmCurrentLicenseIndex_Object = MibTableColumn
cilmCurrentLicenseIndex = _CilmCurrentLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 6),
    _CilmCurrentLicenseIndex_Type()
)
cilmCurrentLicenseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cilmCurrentLicenseIndex.setStatus("current")
_CilmNextBootLicenseStoreIndex_Type = Unsigned32
_CilmNextBootLicenseStoreIndex_Object = MibTableColumn
cilmNextBootLicenseStoreIndex = _CilmNextBootLicenseStoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 7),
    _CilmNextBootLicenseStoreIndex_Type()
)
cilmNextBootLicenseStoreIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cilmNextBootLicenseStoreIndex.setStatus("current")
_CilmNextBootLicenseIndex_Type = Unsigned32
_CilmNextBootLicenseIndex_Object = MibTableColumn
cilmNextBootLicenseIndex = _CilmNextBootLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 8),
    _CilmNextBootLicenseIndex_Type()
)
cilmNextBootLicenseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cilmNextBootLicenseIndex.setStatus("current")
_CilmImageLevelToLicenseMapTable_Object = MibTable
cilmImageLevelToLicenseMapTable = _CilmImageLevelToLicenseMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2)
)
if mibBuilder.loadTexts:
    cilmImageLevelToLicenseMapTable.setStatus("current")
_CilmImageLevelToLicenseMapEntry_Object = MibTableRow
cilmImageLevelToLicenseMapEntry = _CilmImageLevelToLicenseMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1)
)
cilmImageLevelToLicenseMapEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmModuleName"),
    (0, "CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLicenseMapIndex"),
)
if mibBuilder.loadTexts:
    cilmImageLevelToLicenseMapEntry.setStatus("current")
_CilmImageLicenseMapIndex_Type = Unsigned32
_CilmImageLicenseMapIndex_Object = MibTableColumn
cilmImageLicenseMapIndex = _CilmImageLicenseMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1, 1),
    _CilmImageLicenseMapIndex_Type()
)
cilmImageLicenseMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cilmImageLicenseMapIndex.setStatus("current")
_CilmImageLicenseImageLevel_Type = BootImageLevel
_CilmImageLicenseImageLevel_Object = MibTableColumn
cilmImageLicenseImageLevel = _CilmImageLicenseImageLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1, 2),
    _CilmImageLicenseImageLevel_Type()
)
cilmImageLicenseImageLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cilmImageLicenseImageLevel.setStatus("current")
_CilmImageLicenseName_Type = LicenseNameList
_CilmImageLicenseName_Object = MibTableColumn
cilmImageLicenseName = _CilmImageLicenseName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1, 3),
    _CilmImageLicenseName_Type()
)
cilmImageLicenseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cilmImageLicenseName.setStatus("current")


class _CilmImageLicensePriority_Type(Unsigned32):
    """Custom type cilmImageLicensePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CilmImageLicensePriority_Type.__name__ = "Unsigned32"
_CilmImageLicensePriority_Object = MibTableColumn
cilmImageLicensePriority = _CilmImageLicensePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1, 4),
    _CilmImageLicensePriority_Type()
)
cilmImageLicensePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cilmImageLicensePriority.setStatus("current")


class _CilmEULAAccepted_Type(TruthValue):
    """Custom type cilmEULAAccepted based on TruthValue"""


_CilmEULAAccepted_Object = MibScalar
cilmEULAAccepted = _CilmEULAAccepted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 3),
    _CilmEULAAccepted_Type()
)
cilmEULAAccepted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cilmEULAAccepted.setStatus("current")
_CilmNotifCntl_ObjectIdentity = ObjectIdentity
cilmNotifCntl = _CilmNotifCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 4)
)


class _CilmImageLevelChangedNotif_Type(TruthValue):
    """Custom type cilmImageLevelChangedNotif based on TruthValue"""


_CilmImageLevelChangedNotif_Object = MibScalar
cilmImageLevelChangedNotif = _CilmImageLevelChangedNotif_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 4, 1),
    _CilmImageLevelChangedNotif_Type()
)
cilmImageLevelChangedNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cilmImageLevelChangedNotif.setStatus("current")
_CiscoImageLicenseMgmtMIBConform_ObjectIdentity = ObjectIdentity
ciscoImageLicenseMgmtMIBConform = _CiscoImageLicenseMgmtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 2)
)
_CilmModuleCompliances_ObjectIdentity = ObjectIdentity
cilmModuleCompliances = _CilmModuleCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 1)
)
_CilmModuleGroups_ObjectIdentity = ObjectIdentity
cilmModuleGroups = _CilmModuleGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 2)
)

# Managed Objects groups

cilmAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 2, 1)
)
cilmAdminGroup.setObjects(
      *(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmCurrentImageLevel"),
        ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmConfiguredBootImageLevel"),
        ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmNextBootImageLevel"),
        ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmCurrentLicenseStoreIndex"),
        ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmCurrentLicenseIndex"),
        ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmNextBootLicenseStoreIndex"),
        ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmNextBootLicenseIndex"),
        ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmEULAAccepted"),
        ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLevelChangedNotif"))
)
if mibBuilder.loadTexts:
    cilmAdminGroup.setStatus("current")

cilmOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 2, 2)
)
cilmOperGroup.setObjects(
      *(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLicenseImageLevel"),
        ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLicenseName"),
        ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLicensePriority"))
)
if mibBuilder.loadTexts:
    cilmOperGroup.setStatus("current")


# Notification objects

cilmBootImageLevelChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 0, 1)
)
cilmBootImageLevelChanged.setObjects(
      *(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmCurrentImageLevel"),
        ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmConfiguredBootImageLevel"))
)
if mibBuilder.loadTexts:
    cilmBootImageLevelChanged.setStatus(
        "current"
    )


# Notifications groups

cilmNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 2, 3)
)
cilmNotifGroup.setObjects(
    ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmBootImageLevelChanged")
)
if mibBuilder.loadTexts:
    cilmNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cilmModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cilmModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IMAGE-LICENSE-MGMT-MIB",
    **{"BootImageLevel": BootImageLevel,
       "LicenseNameList": LicenseNameList,
       "ciscoImageLicenseMgmtMIB": ciscoImageLicenseMgmtMIB,
       "ciscoImageLicenseMgmtMIBNotifs": ciscoImageLicenseMgmtMIBNotifs,
       "cilmBootImageLevelChanged": cilmBootImageLevelChanged,
       "ciscoImageLicenseMgmtMIBObjects": ciscoImageLicenseMgmtMIBObjects,
       "cilmBootImageLevelTable": cilmBootImageLevelTable,
       "cilmBootImageLevelEntry": cilmBootImageLevelEntry,
       "cilmModuleName": cilmModuleName,
       "cilmCurrentImageLevel": cilmCurrentImageLevel,
       "cilmConfiguredBootImageLevel": cilmConfiguredBootImageLevel,
       "cilmNextBootImageLevel": cilmNextBootImageLevel,
       "cilmCurrentLicenseStoreIndex": cilmCurrentLicenseStoreIndex,
       "cilmCurrentLicenseIndex": cilmCurrentLicenseIndex,
       "cilmNextBootLicenseStoreIndex": cilmNextBootLicenseStoreIndex,
       "cilmNextBootLicenseIndex": cilmNextBootLicenseIndex,
       "cilmImageLevelToLicenseMapTable": cilmImageLevelToLicenseMapTable,
       "cilmImageLevelToLicenseMapEntry": cilmImageLevelToLicenseMapEntry,
       "cilmImageLicenseMapIndex": cilmImageLicenseMapIndex,
       "cilmImageLicenseImageLevel": cilmImageLicenseImageLevel,
       "cilmImageLicenseName": cilmImageLicenseName,
       "cilmImageLicensePriority": cilmImageLicensePriority,
       "cilmEULAAccepted": cilmEULAAccepted,
       "cilmNotifCntl": cilmNotifCntl,
       "cilmImageLevelChangedNotif": cilmImageLevelChangedNotif,
       "ciscoImageLicenseMgmtMIBConform": ciscoImageLicenseMgmtMIBConform,
       "cilmModuleCompliances": cilmModuleCompliances,
       "cilmModuleCompliance": cilmModuleCompliance,
       "cilmModuleGroups": cilmModuleGroups,
       "cilmAdminGroup": cilmAdminGroup,
       "cilmOperGroup": cilmOperGroup,
       "cilmNotifGroup": cilmNotifGroup}
)
