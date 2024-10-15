# SNMP MIB module (HP-ENTITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ENTITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:00 2024
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

(hp,
 icf) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hp",
    "icf")

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

hpEntityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9)
)
hpEntityMIB.setRevisions(
        ("2000-11-03 06:36",
         "1997-03-06 03:26",
         "1996-09-06 21:35")
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

_HpEntityMIBObjects_ObjectIdentity = ObjectIdentity
hpEntityMIBObjects = _HpEntityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1)
)
_HpEntityPhysical_ObjectIdentity = ObjectIdentity
hpEntityPhysical = _HpEntityPhysical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 1)
)
_HpEntPhysicalTable_Object = MibTable
hpEntPhysicalTable = _HpEntPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpEntPhysicalTable.setStatus("obsolete")
_HpEntPhysicalEntry_Object = MibTableRow
hpEntPhysicalEntry = _HpEntPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 1, 1, 1)
)
hpEntPhysicalEntry.setIndexNames(
    (0, "HP-ENTITY-MIB", "hpEntPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpEntPhysicalEntry.setStatus("obsolete")
_HpEntPhysicalIndex_Type = PhysicalIndex
_HpEntPhysicalIndex_Object = MibTableColumn
hpEntPhysicalIndex = _HpEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 1, 1, 1, 1),
    _HpEntPhysicalIndex_Type()
)
hpEntPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpEntPhysicalIndex.setStatus("obsolete")
_HpEntPhysicalDescr_Type = DisplayString
_HpEntPhysicalDescr_Object = MibTableColumn
hpEntPhysicalDescr = _HpEntPhysicalDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 1, 1, 1, 2),
    _HpEntPhysicalDescr_Type()
)
hpEntPhysicalDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntPhysicalDescr.setStatus("obsolete")
_HpEntPhysicalVendorType_Type = AutonomousType
_HpEntPhysicalVendorType_Object = MibTableColumn
hpEntPhysicalVendorType = _HpEntPhysicalVendorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 1, 1, 1, 3),
    _HpEntPhysicalVendorType_Type()
)
hpEntPhysicalVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntPhysicalVendorType.setStatus("obsolete")


class _HpEntPhysicalContainedIn_Type(Integer32):
    """Custom type hpEntPhysicalContainedIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpEntPhysicalContainedIn_Type.__name__ = "Integer32"
_HpEntPhysicalContainedIn_Object = MibTableColumn
hpEntPhysicalContainedIn = _HpEntPhysicalContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 1, 1, 1, 4),
    _HpEntPhysicalContainedIn_Type()
)
hpEntPhysicalContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntPhysicalContainedIn.setStatus("obsolete")
_HpEntPhysicalClass_Type = PhysicalClass
_HpEntPhysicalClass_Object = MibTableColumn
hpEntPhysicalClass = _HpEntPhysicalClass_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 1, 1, 1, 5),
    _HpEntPhysicalClass_Type()
)
hpEntPhysicalClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntPhysicalClass.setStatus("obsolete")


class _HpEntPhysicalParentRelPos_Type(Integer32):
    """Custom type hpEntPhysicalParentRelPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_HpEntPhysicalParentRelPos_Type.__name__ = "Integer32"
_HpEntPhysicalParentRelPos_Object = MibTableColumn
hpEntPhysicalParentRelPos = _HpEntPhysicalParentRelPos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 1, 1, 1, 6),
    _HpEntPhysicalParentRelPos_Type()
)
hpEntPhysicalParentRelPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntPhysicalParentRelPos.setStatus("obsolete")
_HpEntPhysicalName_Type = DisplayString
_HpEntPhysicalName_Object = MibTableColumn
hpEntPhysicalName = _HpEntPhysicalName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 1, 1, 1, 7),
    _HpEntPhysicalName_Type()
)
hpEntPhysicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntPhysicalName.setStatus("obsolete")
_HpEntityLogical_ObjectIdentity = ObjectIdentity
hpEntityLogical = _HpEntityLogical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 2)
)
_HpEntLogicalTable_Object = MibTable
hpEntLogicalTable = _HpEntLogicalTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpEntLogicalTable.setStatus("obsolete")
_HpEntLogicalEntry_Object = MibTableRow
hpEntLogicalEntry = _HpEntLogicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 2, 1, 1)
)
hpEntLogicalEntry.setIndexNames(
    (0, "HP-ENTITY-MIB", "hpEntLogicalIndex"),
)
if mibBuilder.loadTexts:
    hpEntLogicalEntry.setStatus("obsolete")


class _HpEntLogicalIndex_Type(Integer32):
    """Custom type hpEntLogicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpEntLogicalIndex_Type.__name__ = "Integer32"
_HpEntLogicalIndex_Object = MibTableColumn
hpEntLogicalIndex = _HpEntLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 2, 1, 1, 1),
    _HpEntLogicalIndex_Type()
)
hpEntLogicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpEntLogicalIndex.setStatus("obsolete")
_HpEntLogicalDescr_Type = DisplayString
_HpEntLogicalDescr_Object = MibTableColumn
hpEntLogicalDescr = _HpEntLogicalDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 2, 1, 1, 2),
    _HpEntLogicalDescr_Type()
)
hpEntLogicalDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntLogicalDescr.setStatus("obsolete")
_HpEntLogicalType_Type = AutonomousType
_HpEntLogicalType_Object = MibTableColumn
hpEntLogicalType = _HpEntLogicalType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 2, 1, 1, 3),
    _HpEntLogicalType_Type()
)
hpEntLogicalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntLogicalType.setStatus("obsolete")


class _HpEntLogicalCommunity_Type(OctetString):
    """Custom type hpEntLogicalCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpEntLogicalCommunity_Type.__name__ = "OctetString"
_HpEntLogicalCommunity_Object = MibTableColumn
hpEntLogicalCommunity = _HpEntLogicalCommunity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 2, 1, 1, 4),
    _HpEntLogicalCommunity_Type()
)
hpEntLogicalCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntLogicalCommunity.setStatus("obsolete")
_HpEntLogicalTAddress_Type = TAddress
_HpEntLogicalTAddress_Object = MibTableColumn
hpEntLogicalTAddress = _HpEntLogicalTAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 2, 1, 1, 5),
    _HpEntLogicalTAddress_Type()
)
hpEntLogicalTAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntLogicalTAddress.setStatus("obsolete")
_HpEntLogicalTDomain_Type = TDomain
_HpEntLogicalTDomain_Object = MibTableColumn
hpEntLogicalTDomain = _HpEntLogicalTDomain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 2, 1, 1, 6),
    _HpEntLogicalTDomain_Type()
)
hpEntLogicalTDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntLogicalTDomain.setStatus("obsolete")
_HpEntityMapping_ObjectIdentity = ObjectIdentity
hpEntityMapping = _HpEntityMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 3)
)
_HpEntLPMappingTable_Object = MibTable
hpEntLPMappingTable = _HpEntLPMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpEntLPMappingTable.setStatus("obsolete")
_HpEntLPMappingEntry_Object = MibTableRow
hpEntLPMappingEntry = _HpEntLPMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 3, 1, 1)
)
hpEntLPMappingEntry.setIndexNames(
    (0, "HP-ENTITY-MIB", "hpEntLogicalIndex"),
    (0, "HP-ENTITY-MIB", "hpEntLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpEntLPMappingEntry.setStatus("obsolete")
_HpEntLPPhysicalIndex_Type = PhysicalIndex
_HpEntLPPhysicalIndex_Object = MibTableColumn
hpEntLPPhysicalIndex = _HpEntLPPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 3, 1, 1, 1),
    _HpEntLPPhysicalIndex_Type()
)
hpEntLPPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntLPPhysicalIndex.setStatus("obsolete")
_HpEntAliasMappingTable_Object = MibTable
hpEntAliasMappingTable = _HpEntAliasMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hpEntAliasMappingTable.setStatus("obsolete")
_HpEntAliasMappingEntry_Object = MibTableRow
hpEntAliasMappingEntry = _HpEntAliasMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 3, 2, 1)
)
hpEntAliasMappingEntry.setIndexNames(
    (0, "HP-ENTITY-MIB", "hpEntPhysicalIndex"),
    (0, "HP-ENTITY-MIB", "hpEntAliasLogicalIndexOrZero"),
)
if mibBuilder.loadTexts:
    hpEntAliasMappingEntry.setStatus("obsolete")


class _HpEntAliasLogicalIndexOrZero_Type(Integer32):
    """Custom type hpEntAliasLogicalIndexOrZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpEntAliasLogicalIndexOrZero_Type.__name__ = "Integer32"
_HpEntAliasLogicalIndexOrZero_Object = MibTableColumn
hpEntAliasLogicalIndexOrZero = _HpEntAliasLogicalIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 3, 2, 1, 1),
    _HpEntAliasLogicalIndexOrZero_Type()
)
hpEntAliasLogicalIndexOrZero.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpEntAliasLogicalIndexOrZero.setStatus("obsolete")
_HpEntAliasMappingIdentifier_Type = RowPointer
_HpEntAliasMappingIdentifier_Object = MibTableColumn
hpEntAliasMappingIdentifier = _HpEntAliasMappingIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 3, 2, 1, 2),
    _HpEntAliasMappingIdentifier_Type()
)
hpEntAliasMappingIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntAliasMappingIdentifier.setStatus("obsolete")
_HpEntPhysicalContainsTable_Object = MibTable
hpEntPhysicalContainsTable = _HpEntPhysicalContainsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hpEntPhysicalContainsTable.setStatus("obsolete")
_HpEntPhysicalContainsEntry_Object = MibTableRow
hpEntPhysicalContainsEntry = _HpEntPhysicalContainsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 3, 3, 1)
)
hpEntPhysicalContainsEntry.setIndexNames(
    (0, "HP-ENTITY-MIB", "hpEntPhysicalIndex"),
    (0, "HP-ENTITY-MIB", "hpEntPhysicalChildIndex"),
)
if mibBuilder.loadTexts:
    hpEntPhysicalContainsEntry.setStatus("obsolete")
_HpEntPhysicalChildIndex_Type = PhysicalIndex
_HpEntPhysicalChildIndex_Object = MibTableColumn
hpEntPhysicalChildIndex = _HpEntPhysicalChildIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 3, 3, 1, 1),
    _HpEntPhysicalChildIndex_Type()
)
hpEntPhysicalChildIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntPhysicalChildIndex.setStatus("obsolete")
_HpEntityGeneral_ObjectIdentity = ObjectIdentity
hpEntityGeneral = _HpEntityGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 4)
)
_HpEntLastChangeTime_Type = TimeStamp
_HpEntLastChangeTime_Object = MibScalar
hpEntLastChangeTime = _HpEntLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 1, 4, 1),
    _HpEntLastChangeTime_Type()
)
hpEntLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEntLastChangeTime.setStatus("obsolete")
_HpEntityMIBTraps_ObjectIdentity = ObjectIdentity
hpEntityMIBTraps = _HpEntityMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 2)
)
_HpEntityMIBTrapPrefix_ObjectIdentity = ObjectIdentity
hpEntityMIBTrapPrefix = _HpEntityMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 2, 0)
)
_HpEntityConformance_ObjectIdentity = ObjectIdentity
hpEntityConformance = _HpEntityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 3)
)
_HpEntityCompliances_ObjectIdentity = ObjectIdentity
hpEntityCompliances = _HpEntityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 3, 1)
)
_HpEntityGroups_ObjectIdentity = ObjectIdentity
hpEntityGroups = _HpEntityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 3, 2)
)

# Managed Objects groups

hpEntityPhysicalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 3, 2, 1)
)
hpEntityPhysicalGroup.setObjects(
      *(("HP-ENTITY-MIB", "hpEntPhysicalDescr"),
        ("HP-ENTITY-MIB", "hpEntPhysicalVendorType"),
        ("HP-ENTITY-MIB", "hpEntPhysicalContainedIn"),
        ("HP-ENTITY-MIB", "hpEntPhysicalClass"),
        ("HP-ENTITY-MIB", "hpEntPhysicalParentRelPos"),
        ("HP-ENTITY-MIB", "hpEntPhysicalName"))
)
if mibBuilder.loadTexts:
    hpEntityPhysicalGroup.setStatus("obsolete")

hpEntityLogicalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 3, 2, 2)
)
hpEntityLogicalGroup.setObjects(
      *(("HP-ENTITY-MIB", "hpEntLogicalDescr"),
        ("HP-ENTITY-MIB", "hpEntLogicalType"),
        ("HP-ENTITY-MIB", "hpEntLogicalCommunity"),
        ("HP-ENTITY-MIB", "hpEntLogicalTAddress"),
        ("HP-ENTITY-MIB", "hpEntLogicalTDomain"))
)
if mibBuilder.loadTexts:
    hpEntityLogicalGroup.setStatus("obsolete")

hpEntityMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 3, 2, 3)
)
hpEntityMappingGroup.setObjects(
      *(("HP-ENTITY-MIB", "hpEntLPPhysicalIndex"),
        ("HP-ENTITY-MIB", "hpEntAliasMappingIdentifier"),
        ("HP-ENTITY-MIB", "hpEntPhysicalChildIndex"))
)
if mibBuilder.loadTexts:
    hpEntityMappingGroup.setStatus("obsolete")

hpEntityGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 3, 2, 4)
)
hpEntityGeneralGroup.setObjects(
    ("HP-ENTITY-MIB", "hpEntLastChangeTime")
)
if mibBuilder.loadTexts:
    hpEntityGeneralGroup.setStatus("obsolete")


# Notification objects

hpEntConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 2, 0, 1)
)
if mibBuilder.loadTexts:
    hpEntConfigChange.setStatus(
        "obsolete"
    )


# Notifications groups

hpEntityNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 3, 2, 5)
)
hpEntityNotificationsGroup.setObjects(
    ("HP-ENTITY-MIB", "hpEntConfigChange")
)
if mibBuilder.loadTexts:
    hpEntityNotificationsGroup.setStatus(
        "obsolete"
    )


# Agent capabilities


# Module compliance

hpEntityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpEntityCompliance.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ENTITY-MIB",
    **{"PhysicalIndex": PhysicalIndex,
       "PhysicalClass": PhysicalClass,
       "hpEntityMIB": hpEntityMIB,
       "hpEntityMIBObjects": hpEntityMIBObjects,
       "hpEntityPhysical": hpEntityPhysical,
       "hpEntPhysicalTable": hpEntPhysicalTable,
       "hpEntPhysicalEntry": hpEntPhysicalEntry,
       "hpEntPhysicalIndex": hpEntPhysicalIndex,
       "hpEntPhysicalDescr": hpEntPhysicalDescr,
       "hpEntPhysicalVendorType": hpEntPhysicalVendorType,
       "hpEntPhysicalContainedIn": hpEntPhysicalContainedIn,
       "hpEntPhysicalClass": hpEntPhysicalClass,
       "hpEntPhysicalParentRelPos": hpEntPhysicalParentRelPos,
       "hpEntPhysicalName": hpEntPhysicalName,
       "hpEntityLogical": hpEntityLogical,
       "hpEntLogicalTable": hpEntLogicalTable,
       "hpEntLogicalEntry": hpEntLogicalEntry,
       "hpEntLogicalIndex": hpEntLogicalIndex,
       "hpEntLogicalDescr": hpEntLogicalDescr,
       "hpEntLogicalType": hpEntLogicalType,
       "hpEntLogicalCommunity": hpEntLogicalCommunity,
       "hpEntLogicalTAddress": hpEntLogicalTAddress,
       "hpEntLogicalTDomain": hpEntLogicalTDomain,
       "hpEntityMapping": hpEntityMapping,
       "hpEntLPMappingTable": hpEntLPMappingTable,
       "hpEntLPMappingEntry": hpEntLPMappingEntry,
       "hpEntLPPhysicalIndex": hpEntLPPhysicalIndex,
       "hpEntAliasMappingTable": hpEntAliasMappingTable,
       "hpEntAliasMappingEntry": hpEntAliasMappingEntry,
       "hpEntAliasLogicalIndexOrZero": hpEntAliasLogicalIndexOrZero,
       "hpEntAliasMappingIdentifier": hpEntAliasMappingIdentifier,
       "hpEntPhysicalContainsTable": hpEntPhysicalContainsTable,
       "hpEntPhysicalContainsEntry": hpEntPhysicalContainsEntry,
       "hpEntPhysicalChildIndex": hpEntPhysicalChildIndex,
       "hpEntityGeneral": hpEntityGeneral,
       "hpEntLastChangeTime": hpEntLastChangeTime,
       "hpEntityMIBTraps": hpEntityMIBTraps,
       "hpEntityMIBTrapPrefix": hpEntityMIBTrapPrefix,
       "hpEntConfigChange": hpEntConfigChange,
       "hpEntityConformance": hpEntityConformance,
       "hpEntityCompliances": hpEntityCompliances,
       "hpEntityCompliance": hpEntityCompliance,
       "hpEntityGroups": hpEntityGroups,
       "hpEntityPhysicalGroup": hpEntityPhysicalGroup,
       "hpEntityLogicalGroup": hpEntityLogicalGroup,
       "hpEntityMappingGroup": hpEntityMappingGroup,
       "hpEntityGeneralGroup": hpEntityGeneralGroup,
       "hpEntityNotificationsGroup": hpEntityNotificationsGroup}
)
