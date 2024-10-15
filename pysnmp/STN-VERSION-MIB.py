# SNMP MIB module (STN-VERSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-VERSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:20 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(stnNotification,
 stnSystems) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnNotification",
    "stnSystems")

(StnHardwareModuleType,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-TC",
    "StnHardwareModuleType")

(stnEngineCpu,
 stnEngineIndex,
 stnEngineSlot) = mibBuilder.importSymbols(
    "STN-CHASSIS-MIB",
    "stnEngineCpu",
    "stnEngineIndex",
    "stnEngineSlot")


# MODULE-IDENTITY

stnVersion = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnVersionObjects_ObjectIdentity = ObjectIdentity
stnVersionObjects = _StnVersionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1)
)
_StnSwVersions_ObjectIdentity = ObjectIdentity
stnSwVersions = _StnSwVersions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 1)
)
_StnSwVersionTable_Object = MibTable
stnSwVersionTable = _StnSwVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    stnSwVersionTable.setStatus("current")
_StnSwVersionEntry_Object = MibTableRow
stnSwVersionEntry = _StnSwVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 1, 1, 1)
)
stnSwVersionEntry.setIndexNames(
    (0, "STN-VERSION-MIB", "stnSwImage"),
)
if mibBuilder.loadTexts:
    stnSwVersionEntry.setStatus("current")


class _StnSwImage_Type(Integer32):
    """Custom type stnSwImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("atmOC12Golden", 24),
          ("atmOC3Stone", 21),
          ("bootstrap", 1),
          ("cpmBlue", 9),
          ("cpmHermit", 10),
          ("cpmKing", 8),
          ("cpmRoute", 3),
          ("cpmRouteRecv", 6),
          ("cpmRpePipeline", 12),
          ("cpmSand", 14),
          ("cpmSpider", 13),
          ("cpmSwcPipeline", 11),
          ("cpmSwitch", 2),
          ("cpmSwitchRecv", 5),
          ("ds3Green", 25),
          ("enetMud", 22),
          ("rmFiddler", 23),
          ("swfmHorseshoe", 20),
          ("tsmBlue", 15),
          ("tsmBridge", 18),
          ("tsmECF", 4),
          ("tsmECFRecv", 7),
          ("tsmHermit", 16),
          ("tsmPipeline", 17),
          ("tsmSoldier", 19))
    )


_StnSwImage_Type.__name__ = "Integer32"
_StnSwImage_Object = MibTableColumn
stnSwImage = _StnSwImage_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 1, 1, 1, 1),
    _StnSwImage_Type()
)
stnSwImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSwImage.setStatus("current")


class _StnSwVersionPrefix_Type(DisplayString):
    """Custom type stnSwVersionPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_StnSwVersionPrefix_Type.__name__ = "DisplayString"
_StnSwVersionPrefix_Object = MibTableColumn
stnSwVersionPrefix = _StnSwVersionPrefix_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 1, 1, 1, 2),
    _StnSwVersionPrefix_Type()
)
stnSwVersionPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSwVersionPrefix.setStatus("current")
_StnSwMajorVersion_Type = Integer32
_StnSwMajorVersion_Object = MibTableColumn
stnSwMajorVersion = _StnSwMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 1, 1, 1, 3),
    _StnSwMajorVersion_Type()
)
stnSwMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSwMajorVersion.setStatus("current")
_StnSwMinorVersion_Type = Integer32
_StnSwMinorVersion_Object = MibTableColumn
stnSwMinorVersion = _StnSwMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 1, 1, 1, 4),
    _StnSwMinorVersion_Type()
)
stnSwMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSwMinorVersion.setStatus("current")
_StnSwMaintenanceVersion_Type = Integer32
_StnSwMaintenanceVersion_Object = MibTableColumn
stnSwMaintenanceVersion = _StnSwMaintenanceVersion_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 1, 1, 1, 5),
    _StnSwMaintenanceVersion_Type()
)
stnSwMaintenanceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSwMaintenanceVersion.setStatus("current")
_StnSwPatchVersion_Type = Integer32
_StnSwPatchVersion_Object = MibTableColumn
stnSwPatchVersion = _StnSwPatchVersion_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 1, 1, 1, 6),
    _StnSwPatchVersion_Type()
)
stnSwPatchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSwPatchVersion.setStatus("current")
_StnSwVersionDescr_Type = DisplayString
_StnSwVersionDescr_Object = MibTableColumn
stnSwVersionDescr = _StnSwVersionDescr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 1, 1, 1, 7),
    _StnSwVersionDescr_Type()
)
stnSwVersionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSwVersionDescr.setStatus("current")
_StnHwVersions_ObjectIdentity = ObjectIdentity
stnHwVersions = _StnHwVersions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 2)
)
_StnHwVersionTable_Object = MibTable
stnHwVersionTable = _StnHwVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    stnHwVersionTable.setStatus("current")
_StnHwVersionEntry_Object = MibTableRow
stnHwVersionEntry = _StnHwVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 2, 1, 1)
)
stnHwVersionEntry.setIndexNames(
    (0, "STN-VERSION-MIB", "stnHwSlotIndex"),
)
if mibBuilder.loadTexts:
    stnHwVersionEntry.setStatus("current")
_StnHwSlotIndex_Type = Integer32
_StnHwSlotIndex_Object = MibTableColumn
stnHwSlotIndex = _StnHwSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 2, 1, 1, 1),
    _StnHwSlotIndex_Type()
)
stnHwSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnHwSlotIndex.setStatus("current")
_StnHwType_Type = StnHardwareModuleType
_StnHwType_Object = MibTableColumn
stnHwType = _StnHwType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 2, 1, 1, 2),
    _StnHwType_Type()
)
stnHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnHwType.setStatus("current")
_StnHwMajorVersion_Type = Integer32
_StnHwMajorVersion_Object = MibTableColumn
stnHwMajorVersion = _StnHwMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 2, 1, 1, 3),
    _StnHwMajorVersion_Type()
)
stnHwMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnHwMajorVersion.setStatus("current")
_StnHwMinorVersion_Type = Integer32
_StnHwMinorVersion_Object = MibTableColumn
stnHwMinorVersion = _StnHwMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 2, 1, 1, 4),
    _StnHwMinorVersion_Type()
)
stnHwMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnHwMinorVersion.setStatus("current")
_StnHwVersionDescr_Type = DisplayString
_StnHwVersionDescr_Object = MibTableColumn
stnHwVersionDescr = _StnHwVersionDescr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 2, 1, 1, 5),
    _StnHwVersionDescr_Type()
)
stnHwVersionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnHwVersionDescr.setStatus("current")
_StnHwSerialNumber_Type = DisplayString
_StnHwSerialNumber_Object = MibTableColumn
stnHwSerialNumber = _StnHwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 1, 2, 1, 1, 6),
    _StnHwSerialNumber_Type()
)
stnHwSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnHwSerialNumber.setStatus("current")
_StnVersionMibConformance_ObjectIdentity = ObjectIdentity
stnVersionMibConformance = _StnVersionMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 2, 2)
)

# Managed Objects groups


# Notification objects

stnSwImageUpgraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 51)
)
stnSwImageUpgraded.setObjects(
    ("STN-VERSION-MIB", "stnSwImage")
)
if mibBuilder.loadTexts:
    stnSwImageUpgraded.setStatus(
        "current"
    )

stnSwImageUpgradeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 52)
)
stnSwImageUpgradeFailure.setObjects(
      *(("STN-VERSION-MIB", "stnSwImage"),
        ("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"))
)
if mibBuilder.loadTexts:
    stnSwImageUpgradeFailure.setStatus(
        "current"
    )

stnSwImageNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 53)
)
stnSwImageNotFound.setObjects(
    ("STN-VERSION-MIB", "stnSwImage")
)
if mibBuilder.loadTexts:
    stnSwImageNotFound.setStatus(
        "current"
    )

stnSwImageAutoDowngraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 54)
)
stnSwImageAutoDowngraded.setObjects(
      *(("STN-VERSION-MIB", "stnSwImage"),
        ("STN-VERSION-MIB", "stnSwVersionDescr"),
        ("STN-VERSION-MIB", "stnSwVersionDescr"))
)
if mibBuilder.loadTexts:
    stnSwImageAutoDowngraded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-VERSION-MIB",
    **{"stnVersion": stnVersion,
       "stnVersionObjects": stnVersionObjects,
       "stnSwVersions": stnSwVersions,
       "stnSwVersionTable": stnSwVersionTable,
       "stnSwVersionEntry": stnSwVersionEntry,
       "stnSwImage": stnSwImage,
       "stnSwVersionPrefix": stnSwVersionPrefix,
       "stnSwMajorVersion": stnSwMajorVersion,
       "stnSwMinorVersion": stnSwMinorVersion,
       "stnSwMaintenanceVersion": stnSwMaintenanceVersion,
       "stnSwPatchVersion": stnSwPatchVersion,
       "stnSwVersionDescr": stnSwVersionDescr,
       "stnHwVersions": stnHwVersions,
       "stnHwVersionTable": stnHwVersionTable,
       "stnHwVersionEntry": stnHwVersionEntry,
       "stnHwSlotIndex": stnHwSlotIndex,
       "stnHwType": stnHwType,
       "stnHwMajorVersion": stnHwMajorVersion,
       "stnHwMinorVersion": stnHwMinorVersion,
       "stnHwVersionDescr": stnHwVersionDescr,
       "stnHwSerialNumber": stnHwSerialNumber,
       "stnVersionMibConformance": stnVersionMibConformance,
       "stnSwImageUpgraded": stnSwImageUpgraded,
       "stnSwImageUpgradeFailure": stnSwImageUpgradeFailure,
       "stnSwImageNotFound": stnSwImageNotFound,
       "stnSwImageAutoDowngraded": stnSwImageAutoDowngraded}
)
