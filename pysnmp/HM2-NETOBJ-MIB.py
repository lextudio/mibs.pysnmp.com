# SNMP MIB module (HM2-NETOBJ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-NETOBJ-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:09 2024
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

(hm2ConfigurationMibs,) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "hm2ConfigurationMibs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hm2NetobjMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 60)
)
hm2NetobjMib.setRevisions(
        ("2011-10-20 00:00",
         "2011-07-01 00:00",
         "2011-05-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2NetobjNotifications_ObjectIdentity = ObjectIdentity
hm2NetobjNotifications = _Hm2NetobjNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 0)
)
_Hm2NetobjObjects_ObjectIdentity = ObjectIdentity
hm2NetobjObjects = _Hm2NetobjObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 1)
)
_Hm2NetobjectsObjects_ObjectIdentity = ObjectIdentity
hm2NetobjectsObjects = _Hm2NetobjectsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 1, 1)
)


class _Hm2NetobjectsCount_Type(Integer32):
    """Custom type hm2NetobjectsCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Hm2NetobjectsCount_Type.__name__ = "Integer32"
_Hm2NetobjectsCount_Object = MibScalar
hm2NetobjectsCount = _Hm2NetobjectsCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 1, 1, 1),
    _Hm2NetobjectsCount_Type()
)
hm2NetobjectsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetobjectsCount.setStatus("current")
_Hm2NetobjectsDataTableEntriesCount_Type = Integer32
_Hm2NetobjectsDataTableEntriesCount_Object = MibScalar
hm2NetobjectsDataTableEntriesCount = _Hm2NetobjectsDataTableEntriesCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 1, 1, 2),
    _Hm2NetobjectsDataTableEntriesCount_Type()
)
hm2NetobjectsDataTableEntriesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetobjectsDataTableEntriesCount.setStatus("current")
_Hm2NetobjectsTables_ObjectIdentity = ObjectIdentity
hm2NetobjectsTables = _Hm2NetobjectsTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 1, 2)
)
_Hm2NetobjectsTable_Object = MibTable
hm2NetobjectsTable = _Hm2NetobjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hm2NetobjectsTable.setStatus("current")
_Hm2NetobjectsTableEntry_Object = MibTableRow
hm2NetobjectsTableEntry = _Hm2NetobjectsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 1, 2, 1, 1)
)
hm2NetobjectsTableEntry.setIndexNames(
    (0, "HM2-NETOBJ-MIB", "hm2NetobjectsIndex"),
)
if mibBuilder.loadTexts:
    hm2NetobjectsTableEntry.setStatus("current")


class _Hm2NetobjectsIndex_Type(Integer32):
    """Custom type hm2NetobjectsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hm2NetobjectsIndex_Type.__name__ = "Integer32"
_Hm2NetobjectsIndex_Object = MibTableColumn
hm2NetobjectsIndex = _Hm2NetobjectsIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 1, 2, 1, 1, 1),
    _Hm2NetobjectsIndex_Type()
)
hm2NetobjectsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2NetobjectsIndex.setStatus("current")


class _Hm2NetobjectsName_Type(DisplayString):
    """Custom type hm2NetobjectsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_Hm2NetobjectsName_Type.__name__ = "DisplayString"
_Hm2NetobjectsName_Object = MibTableColumn
hm2NetobjectsName = _Hm2NetobjectsName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 1, 2, 1, 1, 2),
    _Hm2NetobjectsName_Type()
)
hm2NetobjectsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2NetobjectsName.setStatus("current")
_Hm2NetobjectsDataEntriesCount_Type = Integer32
_Hm2NetobjectsDataEntriesCount_Object = MibTableColumn
hm2NetobjectsDataEntriesCount = _Hm2NetobjectsDataEntriesCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 1, 2, 1, 1, 3),
    _Hm2NetobjectsDataEntriesCount_Type()
)
hm2NetobjectsDataEntriesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2NetobjectsDataEntriesCount.setStatus("current")
_Hm2NetobjectsRowStatus_Type = RowStatus
_Hm2NetobjectsRowStatus_Object = MibTableColumn
hm2NetobjectsRowStatus = _Hm2NetobjectsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 1, 2, 1, 1, 4),
    _Hm2NetobjectsRowStatus_Type()
)
hm2NetobjectsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2NetobjectsRowStatus.setStatus("current")
_Hm2NetobjectsDataTable_Object = MibTable
hm2NetobjectsDataTable = _Hm2NetobjectsDataTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hm2NetobjectsDataTable.setStatus("current")
_Hm2NetobjectsDataTableEntry_Object = MibTableRow
hm2NetobjectsDataTableEntry = _Hm2NetobjectsDataTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 1, 2, 2, 1)
)
hm2NetobjectsDataTableEntry.setIndexNames(
    (0, "HM2-NETOBJ-MIB", "hm2NetobjectsDataTableIndex"),
)
if mibBuilder.loadTexts:
    hm2NetobjectsDataTableEntry.setStatus("current")


class _Hm2NetobjectsDataTableIndex_Type(Integer32):
    """Custom type hm2NetobjectsDataTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hm2NetobjectsDataTableIndex_Type.__name__ = "Integer32"
_Hm2NetobjectsDataTableIndex_Object = MibTableColumn
hm2NetobjectsDataTableIndex = _Hm2NetobjectsDataTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 1, 2, 2, 1, 1),
    _Hm2NetobjectsDataTableIndex_Type()
)
hm2NetobjectsDataTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2NetobjectsDataTableIndex.setStatus("current")


class _Hm2NetobjectsDataTableObjIndex_Type(Integer32):
    """Custom type hm2NetobjectsDataTableObjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hm2NetobjectsDataTableObjIndex_Type.__name__ = "Integer32"
_Hm2NetobjectsDataTableObjIndex_Object = MibTableColumn
hm2NetobjectsDataTableObjIndex = _Hm2NetobjectsDataTableObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 1, 2, 2, 1, 2),
    _Hm2NetobjectsDataTableObjIndex_Type()
)
hm2NetobjectsDataTableObjIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2NetobjectsDataTableObjIndex.setStatus("current")


class _Hm2NetobjectsDataTableData_Type(DisplayString):
    """Custom type hm2NetobjectsDataTableData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_Hm2NetobjectsDataTableData_Type.__name__ = "DisplayString"
_Hm2NetobjectsDataTableData_Object = MibTableColumn
hm2NetobjectsDataTableData = _Hm2NetobjectsDataTableData_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 1, 2, 2, 1, 3),
    _Hm2NetobjectsDataTableData_Type()
)
hm2NetobjectsDataTableData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2NetobjectsDataTableData.setStatus("current")
_Hm2NetobjectsDataTableRowStatus_Type = RowStatus
_Hm2NetobjectsDataTableRowStatus_Object = MibTableColumn
hm2NetobjectsDataTableRowStatus = _Hm2NetobjectsDataTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 1, 2, 2, 1, 4),
    _Hm2NetobjectsDataTableRowStatus_Type()
)
hm2NetobjectsDataTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2NetobjectsDataTableRowStatus.setStatus("current")
_Hm2NetobjConformance_ObjectIdentity = ObjectIdentity
hm2NetobjConformance = _Hm2NetobjConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 2)
)
_Hm2NetobjCompliances_ObjectIdentity = ObjectIdentity
hm2NetobjCompliances = _Hm2NetobjCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 2, 1)
)
_Hm2NetobjGroups_ObjectIdentity = ObjectIdentity
hm2NetobjGroups = _Hm2NetobjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 2, 2)
)

# Managed Objects groups

hm2NetobjGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 2, 2, 1)
)
hm2NetobjGeneralGroup.setObjects(
      *(("HM2-NETOBJ-MIB", "hm2NetobjectsName"),
        ("HM2-NETOBJ-MIB", "hm2NetobjectsCount"),
        ("HM2-NETOBJ-MIB", "hm2NetobjectsDataEntriesCount"),
        ("HM2-NETOBJ-MIB", "hm2NetobjectsRowStatus"),
        ("HM2-NETOBJ-MIB", "hm2NetobjectsDataTableEntriesCount"),
        ("HM2-NETOBJ-MIB", "hm2NetobjectsDataTableObjIndex"),
        ("HM2-NETOBJ-MIB", "hm2NetobjectsDataTableData"),
        ("HM2-NETOBJ-MIB", "hm2NetobjectsDataTableRowStatus"))
)
if mibBuilder.loadTexts:
    hm2NetobjGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hm2NetobjCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 248, 11, 60, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hm2NetobjCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-NETOBJ-MIB",
    **{"hm2NetobjMib": hm2NetobjMib,
       "hm2NetobjNotifications": hm2NetobjNotifications,
       "hm2NetobjObjects": hm2NetobjObjects,
       "hm2NetobjectsObjects": hm2NetobjectsObjects,
       "hm2NetobjectsCount": hm2NetobjectsCount,
       "hm2NetobjectsDataTableEntriesCount": hm2NetobjectsDataTableEntriesCount,
       "hm2NetobjectsTables": hm2NetobjectsTables,
       "hm2NetobjectsTable": hm2NetobjectsTable,
       "hm2NetobjectsTableEntry": hm2NetobjectsTableEntry,
       "hm2NetobjectsIndex": hm2NetobjectsIndex,
       "hm2NetobjectsName": hm2NetobjectsName,
       "hm2NetobjectsDataEntriesCount": hm2NetobjectsDataEntriesCount,
       "hm2NetobjectsRowStatus": hm2NetobjectsRowStatus,
       "hm2NetobjectsDataTable": hm2NetobjectsDataTable,
       "hm2NetobjectsDataTableEntry": hm2NetobjectsDataTableEntry,
       "hm2NetobjectsDataTableIndex": hm2NetobjectsDataTableIndex,
       "hm2NetobjectsDataTableObjIndex": hm2NetobjectsDataTableObjIndex,
       "hm2NetobjectsDataTableData": hm2NetobjectsDataTableData,
       "hm2NetobjectsDataTableRowStatus": hm2NetobjectsDataTableRowStatus,
       "hm2NetobjConformance": hm2NetobjConformance,
       "hm2NetobjCompliances": hm2NetobjCompliances,
       "hm2NetobjCompliance": hm2NetobjCompliance,
       "hm2NetobjGroups": hm2NetobjGroups,
       "hm2NetobjGeneralGroup": hm2NetobjGeneralGroup}
)
