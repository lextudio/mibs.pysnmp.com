# SNMP MIB module (LC-ENTITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LC-ENTITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:32 2024
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

(lancastMibModulesA,
 lancastTraps) = mibBuilder.importSymbols(
    "LANCAST-MIB",
    "lancastMibModulesA",
    "lancastTraps")

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

(AutonomousType,
 DisplayString,
 RowPointer,
 TAddress,
 TDomain,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowPointer",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

entityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5)
)
entityMIB.setRevisions(
        ("1999-03-03 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PhysicalIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class PhysicalClass(Integer32, TextualConvention):
    status = "current"
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("backplane", 4),
          ("chassis", 3),
          ("container", 5),
          ("fan", 7),
          ("module", 9),
          ("other", 1),
          ("port", 10),
          ("powerSupply", 6),
          ("sensor", 8),
          ("unknown", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EntityMIBObjects_ObjectIdentity = ObjectIdentity
entityMIBObjects = _EntityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1)
)
_EntityPhysical_ObjectIdentity = ObjectIdentity
entityPhysical = _EntityPhysical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 1)
)
_EntPhysicalTable_Object = MibTable
entPhysicalTable = _EntPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    entPhysicalTable.setStatus("current")
_EntPhysicalEntry_Object = MibTableRow
entPhysicalEntry = _EntPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 1, 1, 1)
)
entPhysicalEntry.setIndexNames(
    (0, "LC-ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    entPhysicalEntry.setStatus("current")
_EntPhysicalIndex_Type = PhysicalIndex
_EntPhysicalIndex_Object = MibTableColumn
entPhysicalIndex = _EntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 1, 1, 1, 1),
    _EntPhysicalIndex_Type()
)
entPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhysicalIndex.setStatus("current")
_EntPhysicalDescr_Type = DisplayString
_EntPhysicalDescr_Object = MibTableColumn
entPhysicalDescr = _EntPhysicalDescr_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 1, 1, 1, 2),
    _EntPhysicalDescr_Type()
)
entPhysicalDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhysicalDescr.setStatus("current")
_EntPhysicalVendorType_Type = AutonomousType
_EntPhysicalVendorType_Object = MibTableColumn
entPhysicalVendorType = _EntPhysicalVendorType_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 1, 1, 1, 3),
    _EntPhysicalVendorType_Type()
)
entPhysicalVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhysicalVendorType.setStatus("current")


class _EntPhysicalContainedIn_Type(Integer32):
    """Custom type entPhysicalContainedIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EntPhysicalContainedIn_Type.__name__ = "Integer32"
_EntPhysicalContainedIn_Object = MibTableColumn
entPhysicalContainedIn = _EntPhysicalContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 1, 1, 1, 4),
    _EntPhysicalContainedIn_Type()
)
entPhysicalContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhysicalContainedIn.setStatus("current")
_EntPhysicalClass_Type = PhysicalClass
_EntPhysicalClass_Object = MibTableColumn
entPhysicalClass = _EntPhysicalClass_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 1, 1, 1, 5),
    _EntPhysicalClass_Type()
)
entPhysicalClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhysicalClass.setStatus("current")


class _EntPhysicalParentRelPos_Type(Integer32):
    """Custom type entPhysicalParentRelPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_EntPhysicalParentRelPos_Type.__name__ = "Integer32"
_EntPhysicalParentRelPos_Object = MibTableColumn
entPhysicalParentRelPos = _EntPhysicalParentRelPos_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 1, 1, 1, 6),
    _EntPhysicalParentRelPos_Type()
)
entPhysicalParentRelPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhysicalParentRelPos.setStatus("current")
_EntPhysicalName_Type = DisplayString
_EntPhysicalName_Object = MibTableColumn
entPhysicalName = _EntPhysicalName_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 1, 1, 1, 7),
    _EntPhysicalName_Type()
)
entPhysicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhysicalName.setStatus("current")
_EntityLogical_ObjectIdentity = ObjectIdentity
entityLogical = _EntityLogical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 2)
)
_EntLogicalTable_Object = MibTable
entLogicalTable = _EntLogicalTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    entLogicalTable.setStatus("current")
_EntLogicalEntry_Object = MibTableRow
entLogicalEntry = _EntLogicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 2, 1, 1)
)
entLogicalEntry.setIndexNames(
    (0, "LC-ENTITY-MIB", "entLogicalIndex"),
)
if mibBuilder.loadTexts:
    entLogicalEntry.setStatus("current")


class _EntLogicalIndex_Type(Integer32):
    """Custom type entLogicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EntLogicalIndex_Type.__name__ = "Integer32"
_EntLogicalIndex_Object = MibTableColumn
entLogicalIndex = _EntLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 2, 1, 1, 1),
    _EntLogicalIndex_Type()
)
entLogicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entLogicalIndex.setStatus("current")
_EntLogicalDescr_Type = DisplayString
_EntLogicalDescr_Object = MibTableColumn
entLogicalDescr = _EntLogicalDescr_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 2, 1, 1, 2),
    _EntLogicalDescr_Type()
)
entLogicalDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entLogicalDescr.setStatus("current")
_EntLogicalType_Type = AutonomousType
_EntLogicalType_Object = MibTableColumn
entLogicalType = _EntLogicalType_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 2, 1, 1, 3),
    _EntLogicalType_Type()
)
entLogicalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entLogicalType.setStatus("current")


class _EntLogicalCommunity_Type(OctetString):
    """Custom type entLogicalCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_EntLogicalCommunity_Type.__name__ = "OctetString"
_EntLogicalCommunity_Object = MibTableColumn
entLogicalCommunity = _EntLogicalCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 2, 1, 1, 4),
    _EntLogicalCommunity_Type()
)
entLogicalCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entLogicalCommunity.setStatus("current")
_EntLogicalTAddress_Type = TAddress
_EntLogicalTAddress_Object = MibTableColumn
entLogicalTAddress = _EntLogicalTAddress_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 2, 1, 1, 5),
    _EntLogicalTAddress_Type()
)
entLogicalTAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entLogicalTAddress.setStatus("current")
_EntLogicalTDomain_Type = TDomain
_EntLogicalTDomain_Object = MibTableColumn
entLogicalTDomain = _EntLogicalTDomain_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 2, 1, 1, 6),
    _EntLogicalTDomain_Type()
)
entLogicalTDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entLogicalTDomain.setStatus("current")
_EntityMapping_ObjectIdentity = ObjectIdentity
entityMapping = _EntityMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 3)
)
_EntLPMappingTable_Object = MibTable
entLPMappingTable = _EntLPMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    entLPMappingTable.setStatus("current")
_EntLPMappingEntry_Object = MibTableRow
entLPMappingEntry = _EntLPMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 3, 1, 1)
)
entLPMappingEntry.setIndexNames(
    (0, "LC-ENTITY-MIB", "entLogicalIndex"),
    (0, "LC-ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    entLPMappingEntry.setStatus("current")
_EntLPPhysicalIndex_Type = PhysicalIndex
_EntLPPhysicalIndex_Object = MibTableColumn
entLPPhysicalIndex = _EntLPPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 3, 1, 1, 1),
    _EntLPPhysicalIndex_Type()
)
entLPPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entLPPhysicalIndex.setStatus("current")
_EntAliasMappingTable_Object = MibTable
entAliasMappingTable = _EntAliasMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    entAliasMappingTable.setStatus("current")
_EntAliasMappingEntry_Object = MibTableRow
entAliasMappingEntry = _EntAliasMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 3, 2, 1)
)
entAliasMappingEntry.setIndexNames(
    (0, "LC-ENTITY-MIB", "entPhysicalIndex"),
    (0, "LC-ENTITY-MIB", "entAliasLogicalIndexOrZero"),
)
if mibBuilder.loadTexts:
    entAliasMappingEntry.setStatus("current")


class _EntAliasLogicalIndexOrZero_Type(Integer32):
    """Custom type entAliasLogicalIndexOrZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EntAliasLogicalIndexOrZero_Type.__name__ = "Integer32"
_EntAliasLogicalIndexOrZero_Object = MibTableColumn
entAliasLogicalIndexOrZero = _EntAliasLogicalIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 3, 2, 1, 1),
    _EntAliasLogicalIndexOrZero_Type()
)
entAliasLogicalIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entAliasLogicalIndexOrZero.setStatus("current")
_EntAliasMappingIdentifier_Type = RowPointer
_EntAliasMappingIdentifier_Object = MibTableColumn
entAliasMappingIdentifier = _EntAliasMappingIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 3, 2, 1, 2),
    _EntAliasMappingIdentifier_Type()
)
entAliasMappingIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entAliasMappingIdentifier.setStatus("current")
_EntPhysicalContainsTable_Object = MibTable
entPhysicalContainsTable = _EntPhysicalContainsTable_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    entPhysicalContainsTable.setStatus("current")
_EntPhysicalContainsEntry_Object = MibTableRow
entPhysicalContainsEntry = _EntPhysicalContainsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 3, 3, 1)
)
entPhysicalContainsEntry.setIndexNames(
    (0, "LC-ENTITY-MIB", "entPhysicalIndex"),
    (0, "LC-ENTITY-MIB", "entPhysicalChildIndex"),
)
if mibBuilder.loadTexts:
    entPhysicalContainsEntry.setStatus("current")
_EntPhysicalChildIndex_Type = PhysicalIndex
_EntPhysicalChildIndex_Object = MibTableColumn
entPhysicalChildIndex = _EntPhysicalChildIndex_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 3, 3, 1, 1),
    _EntPhysicalChildIndex_Type()
)
entPhysicalChildIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhysicalChildIndex.setStatus("current")
_EntityGeneral_ObjectIdentity = ObjectIdentity
entityGeneral = _EntityGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 4)
)
_EntLastChangeTime_Type = TimeStamp
_EntLastChangeTime_Object = MibScalar
entLastChangeTime = _EntLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 1, 4, 1),
    _EntLastChangeTime_Type()
)
entLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entLastChangeTime.setStatus("current")
_EntityConformance_ObjectIdentity = ObjectIdentity
entityConformance = _EntityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 3)
)
_EntityCompliances_ObjectIdentity = ObjectIdentity
entityCompliances = _EntityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 3, 1)
)
_EntityGroups_ObjectIdentity = ObjectIdentity
entityGroups = _EntityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 3, 2)
)

# Managed Objects groups

entityPhysicalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 3, 2, 1)
)
entityPhysicalGroup.setObjects(
      *(("LC-ENTITY-MIB", "entPhysicalDescr"),
        ("LC-ENTITY-MIB", "entPhysicalVendorType"),
        ("LC-ENTITY-MIB", "entPhysicalContainedIn"),
        ("LC-ENTITY-MIB", "entPhysicalClass"),
        ("LC-ENTITY-MIB", "entPhysicalParentRelPos"),
        ("LC-ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    entityPhysicalGroup.setStatus("current")

entityLogicalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 3, 2, 2)
)
entityLogicalGroup.setObjects(
      *(("LC-ENTITY-MIB", "entLogicalDescr"),
        ("LC-ENTITY-MIB", "entLogicalType"),
        ("LC-ENTITY-MIB", "entLogicalCommunity"),
        ("LC-ENTITY-MIB", "entLogicalTAddress"),
        ("LC-ENTITY-MIB", "entLogicalTDomain"))
)
if mibBuilder.loadTexts:
    entityLogicalGroup.setStatus("current")

entityMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 3, 2, 3)
)
entityMappingGroup.setObjects(
      *(("LC-ENTITY-MIB", "entLPPhysicalIndex"),
        ("LC-ENTITY-MIB", "entAliasMappingIdentifier"),
        ("LC-ENTITY-MIB", "entPhysicalChildIndex"))
)
if mibBuilder.loadTexts:
    entityMappingGroup.setStatus("current")

entityGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 3, 2, 4)
)
entityGeneralGroup.setObjects(
    ("LC-ENTITY-MIB", "entLastChangeTime")
)
if mibBuilder.loadTexts:
    entityGeneralGroup.setStatus("current")


# Notification objects

entConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2745, 1, 0, 10)
)
entConfigChange.setObjects(
    ("LC-ENTITY-MIB", "entLastChangeTime")
)
if mibBuilder.loadTexts:
    entConfigChange.setStatus(
        "current"
    )


# Notifications groups

entityNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 3, 2, 5)
)
entityNotificationsGroup.setObjects(
    ("LC-ENTITY-MIB", "entConfigChange")
)
if mibBuilder.loadTexts:
    entityNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

entityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2745, 1, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    entityCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LC-ENTITY-MIB",
    **{"PhysicalIndex": PhysicalIndex,
       "PhysicalClass": PhysicalClass,
       "entConfigChange": entConfigChange,
       "entityMIB": entityMIB,
       "entityMIBObjects": entityMIBObjects,
       "entityPhysical": entityPhysical,
       "entPhysicalTable": entPhysicalTable,
       "entPhysicalEntry": entPhysicalEntry,
       "entPhysicalIndex": entPhysicalIndex,
       "entPhysicalDescr": entPhysicalDescr,
       "entPhysicalVendorType": entPhysicalVendorType,
       "entPhysicalContainedIn": entPhysicalContainedIn,
       "entPhysicalClass": entPhysicalClass,
       "entPhysicalParentRelPos": entPhysicalParentRelPos,
       "entPhysicalName": entPhysicalName,
       "entityLogical": entityLogical,
       "entLogicalTable": entLogicalTable,
       "entLogicalEntry": entLogicalEntry,
       "entLogicalIndex": entLogicalIndex,
       "entLogicalDescr": entLogicalDescr,
       "entLogicalType": entLogicalType,
       "entLogicalCommunity": entLogicalCommunity,
       "entLogicalTAddress": entLogicalTAddress,
       "entLogicalTDomain": entLogicalTDomain,
       "entityMapping": entityMapping,
       "entLPMappingTable": entLPMappingTable,
       "entLPMappingEntry": entLPMappingEntry,
       "entLPPhysicalIndex": entLPPhysicalIndex,
       "entAliasMappingTable": entAliasMappingTable,
       "entAliasMappingEntry": entAliasMappingEntry,
       "entAliasLogicalIndexOrZero": entAliasLogicalIndexOrZero,
       "entAliasMappingIdentifier": entAliasMappingIdentifier,
       "entPhysicalContainsTable": entPhysicalContainsTable,
       "entPhysicalContainsEntry": entPhysicalContainsEntry,
       "entPhysicalChildIndex": entPhysicalChildIndex,
       "entityGeneral": entityGeneral,
       "entLastChangeTime": entLastChangeTime,
       "entityConformance": entityConformance,
       "entityCompliances": entityCompliances,
       "entityCompliance": entityCompliance,
       "entityGroups": entityGroups,
       "entityPhysicalGroup": entityPhysicalGroup,
       "entityLogicalGroup": entityLogicalGroup,
       "entityMappingGroup": entityMappingGroup,
       "entityGeneralGroup": entityGeneralGroup,
       "entityNotificationsGroup": entityNotificationsGroup}
)
