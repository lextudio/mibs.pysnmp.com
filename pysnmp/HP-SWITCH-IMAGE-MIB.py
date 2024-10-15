# SNMP MIB module (HP-SWITCH-IMAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SWITCH-IMAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:03 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpSwitchImage = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59)
)
hpSwitchImage.setRevisions(
        ("2013-04-01 00:00",
         "2008-12-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpSwitchImageObject_ObjectIdentity = ObjectIdentity
hpSwitchImageObject = _HpSwitchImageObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1)
)


class _HpSwitchDefaultBoot_Type(Integer32):
    """Custom type hpSwitchDefaultBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_HpSwitchDefaultBoot_Type.__name__ = "Integer32"
_HpSwitchDefaultBoot_Object = MibScalar
hpSwitchDefaultBoot = _HpSwitchDefaultBoot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 1),
    _HpSwitchDefaultBoot_Type()
)
hpSwitchDefaultBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDefaultBoot.setStatus("current")
_HpSwitchBootRomVersion_Type = DisplayString
_HpSwitchBootRomVersion_Object = MibScalar
hpSwitchBootRomVersion = _HpSwitchBootRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 2),
    _HpSwitchBootRomVersion_Type()
)
hpSwitchBootRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchBootRomVersion.setStatus("current")
_HpSwitchFlashImageTable_Object = MibTable
hpSwitchFlashImageTable = _HpSwitchFlashImageTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 3)
)
if mibBuilder.loadTexts:
    hpSwitchFlashImageTable.setStatus("current")
_HpSwitchFlashImageEntry_Object = MibTableRow
hpSwitchFlashImageEntry = _HpSwitchFlashImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 3, 1)
)
hpSwitchFlashImageEntry.setIndexNames(
    (0, "HP-SWITCH-IMAGE-MIB", "hpSwitchFlashImageType"),
)
if mibBuilder.loadTexts:
    hpSwitchFlashImageEntry.setStatus("current")


class _HpSwitchFlashImageType_Type(Integer32):
    """Custom type hpSwitchFlashImageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_HpSwitchFlashImageType_Type.__name__ = "Integer32"
_HpSwitchFlashImageType_Object = MibTableColumn
hpSwitchFlashImageType = _HpSwitchFlashImageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 3, 1, 1),
    _HpSwitchFlashImageType_Type()
)
hpSwitchFlashImageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchFlashImageType.setStatus("current")
_HpSwitchFlashImageSize_Type = Unsigned32
_HpSwitchFlashImageSize_Object = MibTableColumn
hpSwitchFlashImageSize = _HpSwitchFlashImageSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 3, 1, 2),
    _HpSwitchFlashImageSize_Type()
)
hpSwitchFlashImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFlashImageSize.setStatus("current")
if mibBuilder.loadTexts:
    hpSwitchFlashImageSize.setUnits("Bytes")
_HpSwitchFlashImageBuildDate_Type = DisplayString
_HpSwitchFlashImageBuildDate_Object = MibTableColumn
hpSwitchFlashImageBuildDate = _HpSwitchFlashImageBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 3, 1, 3),
    _HpSwitchFlashImageBuildDate_Type()
)
hpSwitchFlashImageBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFlashImageBuildDate.setStatus("current")
_HpSwitchFlashImageVersion_Type = DisplayString
_HpSwitchFlashImageVersion_Object = MibTableColumn
hpSwitchFlashImageVersion = _HpSwitchFlashImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 3, 1, 4),
    _HpSwitchFlashImageVersion_Type()
)
hpSwitchFlashImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFlashImageVersion.setStatus("current")
_HpSwitchFlashImageBuildNumber_Type = DisplayString
_HpSwitchFlashImageBuildNumber_Object = MibTableColumn
hpSwitchFlashImageBuildNumber = _HpSwitchFlashImageBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 3, 1, 5),
    _HpSwitchFlashImageBuildNumber_Type()
)
hpSwitchFlashImageBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFlashImageBuildNumber.setStatus("current")
_HpSwitchMgmtModuleVersionTable_Object = MibTable
hpSwitchMgmtModuleVersionTable = _HpSwitchMgmtModuleVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 4)
)
if mibBuilder.loadTexts:
    hpSwitchMgmtModuleVersionTable.setStatus("current")
_HpSwitchMgmtModuleVersionEntry_Object = MibTableRow
hpSwitchMgmtModuleVersionEntry = _HpSwitchMgmtModuleVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 4, 1)
)
hpSwitchMgmtModuleVersionEntry.setIndexNames(
    (0, "HP-SWITCH-IMAGE-MIB", "hpSwitchMgmtModuleID"),
)
if mibBuilder.loadTexts:
    hpSwitchMgmtModuleVersionEntry.setStatus("current")


class _HpSwitchMgmtModuleID_Type(Integer32):
    """Custom type hpSwitchMgmtModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgmtModule1", 1),
          ("mgmtModule2", 2))
    )


_HpSwitchMgmtModuleID_Type.__name__ = "Integer32"
_HpSwitchMgmtModuleID_Object = MibTableColumn
hpSwitchMgmtModuleID = _HpSwitchMgmtModuleID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 4, 1, 1),
    _HpSwitchMgmtModuleID_Type()
)
hpSwitchMgmtModuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchMgmtModuleID.setStatus("current")


class _HpSwitchMgmtModuleStatus_Type(Integer32):
    """Custom type hpSwitchMgmtModuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("failed", 6),
          ("offline", 5),
          ("redundancyDisabled", 3),
          ("standby", 4),
          ("syncing", 7),
          ("unknown", 1))
    )


_HpSwitchMgmtModuleStatus_Type.__name__ = "Integer32"
_HpSwitchMgmtModuleStatus_Object = MibTableColumn
hpSwitchMgmtModuleStatus = _HpSwitchMgmtModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 4, 1, 2),
    _HpSwitchMgmtModuleStatus_Type()
)
hpSwitchMgmtModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchMgmtModuleStatus.setStatus("current")
_HpSwitchMgmtModuleDirectory_Type = DisplayString
_HpSwitchMgmtModuleDirectory_Object = MibTableColumn
hpSwitchMgmtModuleDirectory = _HpSwitchMgmtModuleDirectory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 4, 1, 3),
    _HpSwitchMgmtModuleDirectory_Type()
)
hpSwitchMgmtModuleDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchMgmtModuleDirectory.setStatus("current")
_HpSwitchMgmtModuleDate_Type = DisplayString
_HpSwitchMgmtModuleDate_Object = MibTableColumn
hpSwitchMgmtModuleDate = _HpSwitchMgmtModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 4, 1, 4),
    _HpSwitchMgmtModuleDate_Type()
)
hpSwitchMgmtModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchMgmtModuleDate.setStatus("current")
_HpSwitchMgmtModuleVersion_Type = DisplayString
_HpSwitchMgmtModuleVersion_Object = MibTableColumn
hpSwitchMgmtModuleVersion = _HpSwitchMgmtModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 4, 1, 5),
    _HpSwitchMgmtModuleVersion_Type()
)
hpSwitchMgmtModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchMgmtModuleVersion.setStatus("current")
_HpSwitchMgmtModuleBuildNumber_Type = DisplayString
_HpSwitchMgmtModuleBuildNumber_Object = MibTableColumn
hpSwitchMgmtModuleBuildNumber = _HpSwitchMgmtModuleBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 4, 1, 6),
    _HpSwitchMgmtModuleBuildNumber_Type()
)
hpSwitchMgmtModuleBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchMgmtModuleBuildNumber.setStatus("current")


class _HpSwitchMgmtModuleBootImage_Type(Integer32):
    """Custom type hpSwitchMgmtModuleBootImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 2),
          ("secondary", 3),
          ("unknown", 1))
    )


_HpSwitchMgmtModuleBootImage_Type.__name__ = "Integer32"
_HpSwitchMgmtModuleBootImage_Object = MibTableColumn
hpSwitchMgmtModuleBootImage = _HpSwitchMgmtModuleBootImage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 4, 1, 7),
    _HpSwitchMgmtModuleBootImage_Type()
)
hpSwitchMgmtModuleBootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchMgmtModuleBootImage.setStatus("current")


class _HpSwitchMgmtModuleBuildOptions_Type(Integer32):
    """Custom type hpSwitchMgmtModuleBuildOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("asicLogging", 5),
          ("debug", 4),
          ("hubmode", 3),
          ("qa", 2),
          ("unknown", 1))
    )


_HpSwitchMgmtModuleBuildOptions_Type.__name__ = "Integer32"
_HpSwitchMgmtModuleBuildOptions_Object = MibTableColumn
hpSwitchMgmtModuleBuildOptions = _HpSwitchMgmtModuleBuildOptions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 4, 1, 8),
    _HpSwitchMgmtModuleBuildOptions_Type()
)
hpSwitchMgmtModuleBuildOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchMgmtModuleBuildOptions.setStatus("current")


class _HpSwitchMgmtModuleWatchDog_Type(Integer32):
    """Custom type hpSwitchMgmtModuleWatchDog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("unknown", 1))
    )


_HpSwitchMgmtModuleWatchDog_Type.__name__ = "Integer32"
_HpSwitchMgmtModuleWatchDog_Object = MibTableColumn
hpSwitchMgmtModuleWatchDog = _HpSwitchMgmtModuleWatchDog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 1, 4, 1, 9),
    _HpSwitchMgmtModuleWatchDog_Type()
)
hpSwitchMgmtModuleWatchDog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchMgmtModuleWatchDog.setStatus("current")
_HpSwitchImageConformance_ObjectIdentity = ObjectIdentity
hpSwitchImageConformance = _HpSwitchImageConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 2)
)
_HpSwitchImageGroups_ObjectIdentity = ObjectIdentity
hpSwitchImageGroups = _HpSwitchImageGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 2, 1)
)
_HpSwitchImageCompliances_ObjectIdentity = ObjectIdentity
hpSwitchImageCompliances = _HpSwitchImageCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 2, 2)
)

# Managed Objects groups

hpSwitchFlashImagesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 2, 1, 1)
)
hpSwitchFlashImagesGroup.setObjects(
      *(("HP-SWITCH-IMAGE-MIB", "hpSwitchFlashImageSize"),
        ("HP-SWITCH-IMAGE-MIB", "hpSwitchFlashImageBuildDate"),
        ("HP-SWITCH-IMAGE-MIB", "hpSwitchFlashImageVersion"),
        ("HP-SWITCH-IMAGE-MIB", "hpSwitchBootRomVersion"),
        ("HP-SWITCH-IMAGE-MIB", "hpSwitchDefaultBoot"))
)
if mibBuilder.loadTexts:
    hpSwitchFlashImagesGroup.setStatus("current")

hpSwitchMgmtModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 2, 1, 2)
)
hpSwitchMgmtModuleGroup.setObjects(
      *(("HP-SWITCH-IMAGE-MIB", "hpSwitchMgmtModuleStatus"),
        ("HP-SWITCH-IMAGE-MIB", "hpSwitchMgmtModuleDirectory"),
        ("HP-SWITCH-IMAGE-MIB", "hpSwitchMgmtModuleDate"),
        ("HP-SWITCH-IMAGE-MIB", "hpSwitchMgmtModuleVersion"),
        ("HP-SWITCH-IMAGE-MIB", "hpSwitchMgmtModuleBootImage"))
)
if mibBuilder.loadTexts:
    hpSwitchMgmtModuleGroup.setStatus("current")

hpSwitchBuildGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 2, 1, 3)
)
hpSwitchBuildGroup.setObjects(
      *(("HP-SWITCH-IMAGE-MIB", "hpSwitchMgmtModuleBuildNumber"),
        ("HP-SWITCH-IMAGE-MIB", "hpSwitchFlashImageBuildNumber"),
        ("HP-SWITCH-IMAGE-MIB", "hpSwitchMgmtModuleBuildOptions"),
        ("HP-SWITCH-IMAGE-MIB", "hpSwitchMgmtModuleWatchDog"))
)
if mibBuilder.loadTexts:
    hpSwitchBuildGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpSwitchImageCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpSwitchImageCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SWITCH-IMAGE-MIB",
    **{"hpSwitchImage": hpSwitchImage,
       "hpSwitchImageObject": hpSwitchImageObject,
       "hpSwitchDefaultBoot": hpSwitchDefaultBoot,
       "hpSwitchBootRomVersion": hpSwitchBootRomVersion,
       "hpSwitchFlashImageTable": hpSwitchFlashImageTable,
       "hpSwitchFlashImageEntry": hpSwitchFlashImageEntry,
       "hpSwitchFlashImageType": hpSwitchFlashImageType,
       "hpSwitchFlashImageSize": hpSwitchFlashImageSize,
       "hpSwitchFlashImageBuildDate": hpSwitchFlashImageBuildDate,
       "hpSwitchFlashImageVersion": hpSwitchFlashImageVersion,
       "hpSwitchFlashImageBuildNumber": hpSwitchFlashImageBuildNumber,
       "hpSwitchMgmtModuleVersionTable": hpSwitchMgmtModuleVersionTable,
       "hpSwitchMgmtModuleVersionEntry": hpSwitchMgmtModuleVersionEntry,
       "hpSwitchMgmtModuleID": hpSwitchMgmtModuleID,
       "hpSwitchMgmtModuleStatus": hpSwitchMgmtModuleStatus,
       "hpSwitchMgmtModuleDirectory": hpSwitchMgmtModuleDirectory,
       "hpSwitchMgmtModuleDate": hpSwitchMgmtModuleDate,
       "hpSwitchMgmtModuleVersion": hpSwitchMgmtModuleVersion,
       "hpSwitchMgmtModuleBuildNumber": hpSwitchMgmtModuleBuildNumber,
       "hpSwitchMgmtModuleBootImage": hpSwitchMgmtModuleBootImage,
       "hpSwitchMgmtModuleBuildOptions": hpSwitchMgmtModuleBuildOptions,
       "hpSwitchMgmtModuleWatchDog": hpSwitchMgmtModuleWatchDog,
       "hpSwitchImageConformance": hpSwitchImageConformance,
       "hpSwitchImageGroups": hpSwitchImageGroups,
       "hpSwitchFlashImagesGroup": hpSwitchFlashImagesGroup,
       "hpSwitchMgmtModuleGroup": hpSwitchMgmtModuleGroup,
       "hpSwitchBuildGroup": hpSwitchBuildGroup,
       "hpSwitchImageCompliances": hpSwitchImageCompliances,
       "hpSwitchImageCompliance": hpSwitchImageCompliance}
)
