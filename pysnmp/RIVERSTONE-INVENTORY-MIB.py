# SNMP MIB module (RIVERSTONE-INVENTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-INVENTORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:46 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(riverstoneMibs,) = mibBuilder.importSymbols(
    "RIVERSTONE-SMI-MIB",
    "riverstoneMibs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rsInventoryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40)
)
rsInventoryMIB.setRevisions(
        ("2001-08-22 00:00",
         "2001-06-19 00:00",
         "2001-06-11 00:00",
         "2001-06-01 00:00",
         "2001-05-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RSMemorySize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class RSModuleServiceString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_RsInventoryMIBObjects_ObjectIdentity = ObjectIdentity
rsInventoryMIBObjects = _RsInventoryMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1)
)
_RsInventoryOther_ObjectIdentity = ObjectIdentity
rsInventoryOther = _RsInventoryOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 1)
)
_RsInventoryUnknown_ObjectIdentity = ObjectIdentity
rsInventoryUnknown = _RsInventoryUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 2)
)
_RsInventoryChassis_ObjectIdentity = ObjectIdentity
rsInventoryChassis = _RsInventoryChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 3)
)
_RsInventoryChassisTable_Object = MibTable
rsInventoryChassisTable = _RsInventoryChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rsInventoryChassisTable.setStatus("current")
_RsInventoryChassisEntry_Object = MibTableRow
rsInventoryChassisEntry = _RsInventoryChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 3, 1, 1)
)
rsInventoryChassisEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    rsInventoryChassisEntry.setStatus("current")
_RsInventoryChassisId_Type = SnmpAdminString
_RsInventoryChassisId_Object = MibTableColumn
rsInventoryChassisId = _RsInventoryChassisId_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 3, 1, 1, 1),
    _RsInventoryChassisId_Type()
)
rsInventoryChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsInventoryChassisId.setStatus("current")


class _RsInventoryChassisAssetCLEI_Type(SnmpAdminString):
    """Custom type rsInventoryChassisAssetCLEI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 10),
    )


_RsInventoryChassisAssetCLEI_Type.__name__ = "SnmpAdminString"
_RsInventoryChassisAssetCLEI_Object = MibTableColumn
rsInventoryChassisAssetCLEI = _RsInventoryChassisAssetCLEI_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 3, 1, 1, 2),
    _RsInventoryChassisAssetCLEI_Type()
)
rsInventoryChassisAssetCLEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsInventoryChassisAssetCLEI.setStatus("current")
_RsInventoryBackplane_ObjectIdentity = ObjectIdentity
rsInventoryBackplane = _RsInventoryBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 4)
)
_RsInventoryPowerSupply_ObjectIdentity = ObjectIdentity
rsInventoryPowerSupply = _RsInventoryPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 6)
)
_RsInventoryPowerSupplyTable_Object = MibTable
rsInventoryPowerSupplyTable = _RsInventoryPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 6, 1)
)
if mibBuilder.loadTexts:
    rsInventoryPowerSupplyTable.setStatus("current")
_RsInventoryPowerSupplyEntry_Object = MibTableRow
rsInventoryPowerSupplyEntry = _RsInventoryPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 6, 1, 1)
)
rsInventoryPowerSupplyEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    rsInventoryPowerSupplyEntry.setStatus("current")


class _RsInventoryPowerSupplyAssetCLEI_Type(SnmpAdminString):
    """Custom type rsInventoryPowerSupplyAssetCLEI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 10),
    )


_RsInventoryPowerSupplyAssetCLEI_Type.__name__ = "SnmpAdminString"
_RsInventoryPowerSupplyAssetCLEI_Object = MibTableColumn
rsInventoryPowerSupplyAssetCLEI = _RsInventoryPowerSupplyAssetCLEI_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 6, 1, 1, 1),
    _RsInventoryPowerSupplyAssetCLEI_Type()
)
rsInventoryPowerSupplyAssetCLEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsInventoryPowerSupplyAssetCLEI.setStatus("current")
_RsInventoryFan_ObjectIdentity = ObjectIdentity
rsInventoryFan = _RsInventoryFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 7)
)
_RsInventoryFanTable_Object = MibTable
rsInventoryFanTable = _RsInventoryFanTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 7, 1)
)
if mibBuilder.loadTexts:
    rsInventoryFanTable.setStatus("current")
_RsInventoryFanEntry_Object = MibTableRow
rsInventoryFanEntry = _RsInventoryFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 7, 1, 1)
)
rsInventoryFanEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    rsInventoryFanEntry.setStatus("current")


class _RsInventoryFanAssetCLEI_Type(SnmpAdminString):
    """Custom type rsInventoryFanAssetCLEI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 10),
    )


_RsInventoryFanAssetCLEI_Type.__name__ = "SnmpAdminString"
_RsInventoryFanAssetCLEI_Object = MibTableColumn
rsInventoryFanAssetCLEI = _RsInventoryFanAssetCLEI_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 7, 1, 1, 1),
    _RsInventoryFanAssetCLEI_Type()
)
rsInventoryFanAssetCLEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsInventoryFanAssetCLEI.setStatus("current")
_RsInventorySensor_ObjectIdentity = ObjectIdentity
rsInventorySensor = _RsInventorySensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 8)
)
_RsInventoryModule_ObjectIdentity = ObjectIdentity
rsInventoryModule = _RsInventoryModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 9)
)
_RsInventoryModuleTable_Object = MibTable
rsInventoryModuleTable = _RsInventoryModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 9, 1)
)
if mibBuilder.loadTexts:
    rsInventoryModuleTable.setStatus("current")
_RsInventoryModuleEntry_Object = MibTableRow
rsInventoryModuleEntry = _RsInventoryModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 9, 1, 1)
)
rsInventoryModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    rsInventoryModuleEntry.setStatus("current")
_RsInventoryModuleMemorySize_Type = RSMemorySize
_RsInventoryModuleMemorySize_Object = MibTableColumn
rsInventoryModuleMemorySize = _RsInventoryModuleMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 9, 1, 1, 1),
    _RsInventoryModuleMemorySize_Type()
)
rsInventoryModuleMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsInventoryModuleMemorySize.setStatus("current")
_RsInventoryModuleServiceString_Type = RSModuleServiceString
_RsInventoryModuleServiceString_Object = MibTableColumn
rsInventoryModuleServiceString = _RsInventoryModuleServiceString_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 9, 1, 1, 2),
    _RsInventoryModuleServiceString_Type()
)
rsInventoryModuleServiceString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsInventoryModuleServiceString.setStatus("current")


class _RsInventoryModuleAssetCLEI_Type(SnmpAdminString):
    """Custom type rsInventoryModuleAssetCLEI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 10),
    )


_RsInventoryModuleAssetCLEI_Type.__name__ = "SnmpAdminString"
_RsInventoryModuleAssetCLEI_Object = MibTableColumn
rsInventoryModuleAssetCLEI = _RsInventoryModuleAssetCLEI_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 9, 1, 1, 3),
    _RsInventoryModuleAssetCLEI_Type()
)
rsInventoryModuleAssetCLEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsInventoryModuleAssetCLEI.setStatus("current")
_RsInventoryPort_ObjectIdentity = ObjectIdentity
rsInventoryPort = _RsInventoryPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 10)
)
_RsInventoryStack_ObjectIdentity = ObjectIdentity
rsInventoryStack = _RsInventoryStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 1, 11)
)
_RsInventoryConformance_ObjectIdentity = ObjectIdentity
rsInventoryConformance = _RsInventoryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 3)
)
_RsInventoryCompliances_ObjectIdentity = ObjectIdentity
rsInventoryCompliances = _RsInventoryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 3, 1)
)
_RsInventoryGroups_ObjectIdentity = ObjectIdentity
rsInventoryGroups = _RsInventoryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 3, 2)
)

# Managed Objects groups

rsChassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 3, 2, 1)
)
rsChassisGroup.setObjects(
      *(("RIVERSTONE-INVENTORY-MIB", "rsInventoryChassisId"),
        ("RIVERSTONE-INVENTORY-MIB", "rsInventoryChassisAssetCLEI"))
)
if mibBuilder.loadTexts:
    rsChassisGroup.setStatus("current")

rsModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 3, 2, 2)
)
rsModuleGroup.setObjects(
      *(("RIVERSTONE-INVENTORY-MIB", "rsInventoryModuleMemorySize"),
        ("RIVERSTONE-INVENTORY-MIB", "rsInventoryModuleServiceString"),
        ("RIVERSTONE-INVENTORY-MIB", "rsInventoryModuleAssetCLEI"))
)
if mibBuilder.loadTexts:
    rsModuleGroup.setStatus("current")

rsEnvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 3, 2, 3)
)
rsEnvGroup.setObjects(
      *(("RIVERSTONE-INVENTORY-MIB", "rsInventoryPowerSupplyAssetCLEI"),
        ("RIVERSTONE-INVENTORY-MIB", "rsInventoryFanAssetCLEI"))
)
if mibBuilder.loadTexts:
    rsEnvGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsInventoryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 40, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rsInventoryCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-INVENTORY-MIB",
    **{"RSMemorySize": RSMemorySize,
       "RSModuleServiceString": RSModuleServiceString,
       "rsInventoryMIB": rsInventoryMIB,
       "rsInventoryMIBObjects": rsInventoryMIBObjects,
       "rsInventoryOther": rsInventoryOther,
       "rsInventoryUnknown": rsInventoryUnknown,
       "rsInventoryChassis": rsInventoryChassis,
       "rsInventoryChassisTable": rsInventoryChassisTable,
       "rsInventoryChassisEntry": rsInventoryChassisEntry,
       "rsInventoryChassisId": rsInventoryChassisId,
       "rsInventoryChassisAssetCLEI": rsInventoryChassisAssetCLEI,
       "rsInventoryBackplane": rsInventoryBackplane,
       "rsInventoryPowerSupply": rsInventoryPowerSupply,
       "rsInventoryPowerSupplyTable": rsInventoryPowerSupplyTable,
       "rsInventoryPowerSupplyEntry": rsInventoryPowerSupplyEntry,
       "rsInventoryPowerSupplyAssetCLEI": rsInventoryPowerSupplyAssetCLEI,
       "rsInventoryFan": rsInventoryFan,
       "rsInventoryFanTable": rsInventoryFanTable,
       "rsInventoryFanEntry": rsInventoryFanEntry,
       "rsInventoryFanAssetCLEI": rsInventoryFanAssetCLEI,
       "rsInventorySensor": rsInventorySensor,
       "rsInventoryModule": rsInventoryModule,
       "rsInventoryModuleTable": rsInventoryModuleTable,
       "rsInventoryModuleEntry": rsInventoryModuleEntry,
       "rsInventoryModuleMemorySize": rsInventoryModuleMemorySize,
       "rsInventoryModuleServiceString": rsInventoryModuleServiceString,
       "rsInventoryModuleAssetCLEI": rsInventoryModuleAssetCLEI,
       "rsInventoryPort": rsInventoryPort,
       "rsInventoryStack": rsInventoryStack,
       "rsInventoryConformance": rsInventoryConformance,
       "rsInventoryCompliances": rsInventoryCompliances,
       "rsInventoryCompliance": rsInventoryCompliance,
       "rsInventoryGroups": rsInventoryGroups,
       "rsChassisGroup": rsChassisGroup,
       "rsModuleGroup": rsModuleGroup,
       "rsEnvGroup": rsEnvGroup}
)
