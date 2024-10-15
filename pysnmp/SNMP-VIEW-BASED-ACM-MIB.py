# SNMP MIB module (SNMP-VIEW-BASED-ACM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMP-VIEW-BASED-ACM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:38 2024
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

(SnmpAdminString,
 SnmpSecurityLevel,
 SnmpSecurityModel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpSecurityLevel",
    "SnmpSecurityModel")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

snmpVacmMIB = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 16)
)
snmpVacmMIB.setRevisions(
        ("2002-10-16 00:00",
         "1999-01-20 00:00",
         "1997-11-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VacmMIBObjects_ObjectIdentity = ObjectIdentity
vacmMIBObjects = _VacmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 16, 1)
)
_VacmContextTable_Object = MibTable
vacmContextTable = _VacmContextTable_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 1)
)
if mibBuilder.loadTexts:
    vacmContextTable.setStatus("current")
_VacmContextEntry_Object = MibTableRow
vacmContextEntry = _VacmContextEntry_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 1, 1)
)
vacmContextEntry.setIndexNames(
    (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmContextName"),
)
if mibBuilder.loadTexts:
    vacmContextEntry.setStatus("current")


class _VacmContextName_Type(SnmpAdminString):
    """Custom type vacmContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VacmContextName_Type.__name__ = "SnmpAdminString"
_VacmContextName_Object = MibTableColumn
vacmContextName = _VacmContextName_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 1, 1, 1),
    _VacmContextName_Type()
)
vacmContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vacmContextName.setStatus("current")
_VacmSecurityToGroupTable_Object = MibTable
vacmSecurityToGroupTable = _VacmSecurityToGroupTable_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 2)
)
if mibBuilder.loadTexts:
    vacmSecurityToGroupTable.setStatus("current")
_VacmSecurityToGroupEntry_Object = MibTableRow
vacmSecurityToGroupEntry = _VacmSecurityToGroupEntry_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 2, 1)
)
vacmSecurityToGroupEntry.setIndexNames(
    (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityModel"),
    (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityName"),
)
if mibBuilder.loadTexts:
    vacmSecurityToGroupEntry.setStatus("current")


class _VacmSecurityModel_Type(SnmpSecurityModel):
    """Custom type vacmSecurityModel based on SnmpSecurityModel"""
    subtypeSpec = SnmpSecurityModel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VacmSecurityModel_Type.__name__ = "SnmpSecurityModel"
_VacmSecurityModel_Object = MibTableColumn
vacmSecurityModel = _VacmSecurityModel_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 1),
    _VacmSecurityModel_Type()
)
vacmSecurityModel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vacmSecurityModel.setStatus("current")


class _VacmSecurityName_Type(SnmpAdminString):
    """Custom type vacmSecurityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VacmSecurityName_Type.__name__ = "SnmpAdminString"
_VacmSecurityName_Object = MibTableColumn
vacmSecurityName = _VacmSecurityName_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 2),
    _VacmSecurityName_Type()
)
vacmSecurityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vacmSecurityName.setStatus("current")


class _VacmGroupName_Type(SnmpAdminString):
    """Custom type vacmGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VacmGroupName_Type.__name__ = "SnmpAdminString"
_VacmGroupName_Object = MibTableColumn
vacmGroupName = _VacmGroupName_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 3),
    _VacmGroupName_Type()
)
vacmGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmGroupName.setStatus("current")


class _VacmSecurityToGroupStorageType_Type(StorageType):
    """Custom type vacmSecurityToGroupStorageType based on StorageType"""


_VacmSecurityToGroupStorageType_Object = MibTableColumn
vacmSecurityToGroupStorageType = _VacmSecurityToGroupStorageType_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 4),
    _VacmSecurityToGroupStorageType_Type()
)
vacmSecurityToGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmSecurityToGroupStorageType.setStatus("current")
_VacmSecurityToGroupStatus_Type = RowStatus
_VacmSecurityToGroupStatus_Object = MibTableColumn
vacmSecurityToGroupStatus = _VacmSecurityToGroupStatus_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 5),
    _VacmSecurityToGroupStatus_Type()
)
vacmSecurityToGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmSecurityToGroupStatus.setStatus("current")
_VacmAccessTable_Object = MibTable
vacmAccessTable = _VacmAccessTable_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 4)
)
if mibBuilder.loadTexts:
    vacmAccessTable.setStatus("current")
_VacmAccessEntry_Object = MibTableRow
vacmAccessEntry = _VacmAccessEntry_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 4, 1)
)
vacmAccessEntry.setIndexNames(
    (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmGroupName"),
    (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessContextPrefix"),
    (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessSecurityModel"),
    (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessSecurityLevel"),
)
if mibBuilder.loadTexts:
    vacmAccessEntry.setStatus("current")


class _VacmAccessContextPrefix_Type(SnmpAdminString):
    """Custom type vacmAccessContextPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VacmAccessContextPrefix_Type.__name__ = "SnmpAdminString"
_VacmAccessContextPrefix_Object = MibTableColumn
vacmAccessContextPrefix = _VacmAccessContextPrefix_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 1),
    _VacmAccessContextPrefix_Type()
)
vacmAccessContextPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vacmAccessContextPrefix.setStatus("current")
_VacmAccessSecurityModel_Type = SnmpSecurityModel
_VacmAccessSecurityModel_Object = MibTableColumn
vacmAccessSecurityModel = _VacmAccessSecurityModel_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 2),
    _VacmAccessSecurityModel_Type()
)
vacmAccessSecurityModel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vacmAccessSecurityModel.setStatus("current")
_VacmAccessSecurityLevel_Type = SnmpSecurityLevel
_VacmAccessSecurityLevel_Object = MibTableColumn
vacmAccessSecurityLevel = _VacmAccessSecurityLevel_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 3),
    _VacmAccessSecurityLevel_Type()
)
vacmAccessSecurityLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vacmAccessSecurityLevel.setStatus("current")


class _VacmAccessContextMatch_Type(Integer32):
    """Custom type vacmAccessContextMatch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exact", 1),
          ("prefix", 2))
    )


_VacmAccessContextMatch_Type.__name__ = "Integer32"
_VacmAccessContextMatch_Object = MibTableColumn
vacmAccessContextMatch = _VacmAccessContextMatch_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 4),
    _VacmAccessContextMatch_Type()
)
vacmAccessContextMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmAccessContextMatch.setStatus("current")


class _VacmAccessReadViewName_Type(SnmpAdminString):
    """Custom type vacmAccessReadViewName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VacmAccessReadViewName_Type.__name__ = "SnmpAdminString"
_VacmAccessReadViewName_Object = MibTableColumn
vacmAccessReadViewName = _VacmAccessReadViewName_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 5),
    _VacmAccessReadViewName_Type()
)
vacmAccessReadViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmAccessReadViewName.setStatus("current")


class _VacmAccessWriteViewName_Type(SnmpAdminString):
    """Custom type vacmAccessWriteViewName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VacmAccessWriteViewName_Type.__name__ = "SnmpAdminString"
_VacmAccessWriteViewName_Object = MibTableColumn
vacmAccessWriteViewName = _VacmAccessWriteViewName_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 6),
    _VacmAccessWriteViewName_Type()
)
vacmAccessWriteViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmAccessWriteViewName.setStatus("current")


class _VacmAccessNotifyViewName_Type(SnmpAdminString):
    """Custom type vacmAccessNotifyViewName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VacmAccessNotifyViewName_Type.__name__ = "SnmpAdminString"
_VacmAccessNotifyViewName_Object = MibTableColumn
vacmAccessNotifyViewName = _VacmAccessNotifyViewName_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 7),
    _VacmAccessNotifyViewName_Type()
)
vacmAccessNotifyViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmAccessNotifyViewName.setStatus("current")


class _VacmAccessStorageType_Type(StorageType):
    """Custom type vacmAccessStorageType based on StorageType"""


_VacmAccessStorageType_Object = MibTableColumn
vacmAccessStorageType = _VacmAccessStorageType_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 8),
    _VacmAccessStorageType_Type()
)
vacmAccessStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmAccessStorageType.setStatus("current")
_VacmAccessStatus_Type = RowStatus
_VacmAccessStatus_Object = MibTableColumn
vacmAccessStatus = _VacmAccessStatus_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 9),
    _VacmAccessStatus_Type()
)
vacmAccessStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmAccessStatus.setStatus("current")
_VacmMIBViews_ObjectIdentity = ObjectIdentity
vacmMIBViews = _VacmMIBViews_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 16, 1, 5)
)
_VacmViewSpinLock_Type = TestAndIncr
_VacmViewSpinLock_Object = MibScalar
vacmViewSpinLock = _VacmViewSpinLock_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 5, 1),
    _VacmViewSpinLock_Type()
)
vacmViewSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vacmViewSpinLock.setStatus("current")
_VacmViewTreeFamilyTable_Object = MibTable
vacmViewTreeFamilyTable = _VacmViewTreeFamilyTable_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 5, 2)
)
if mibBuilder.loadTexts:
    vacmViewTreeFamilyTable.setStatus("current")
_VacmViewTreeFamilyEntry_Object = MibTableRow
vacmViewTreeFamilyEntry = _VacmViewTreeFamilyEntry_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1)
)
vacmViewTreeFamilyEntry.setIndexNames(
    (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyViewName"),
    (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilySubtree"),
)
if mibBuilder.loadTexts:
    vacmViewTreeFamilyEntry.setStatus("current")


class _VacmViewTreeFamilyViewName_Type(SnmpAdminString):
    """Custom type vacmViewTreeFamilyViewName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VacmViewTreeFamilyViewName_Type.__name__ = "SnmpAdminString"
_VacmViewTreeFamilyViewName_Object = MibTableColumn
vacmViewTreeFamilyViewName = _VacmViewTreeFamilyViewName_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 1),
    _VacmViewTreeFamilyViewName_Type()
)
vacmViewTreeFamilyViewName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vacmViewTreeFamilyViewName.setStatus("current")
_VacmViewTreeFamilySubtree_Type = ObjectIdentifier
_VacmViewTreeFamilySubtree_Object = MibTableColumn
vacmViewTreeFamilySubtree = _VacmViewTreeFamilySubtree_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 2),
    _VacmViewTreeFamilySubtree_Type()
)
vacmViewTreeFamilySubtree.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vacmViewTreeFamilySubtree.setStatus("current")


class _VacmViewTreeFamilyMask_Type(OctetString):
    """Custom type vacmViewTreeFamilyMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VacmViewTreeFamilyMask_Type.__name__ = "OctetString"
_VacmViewTreeFamilyMask_Object = MibTableColumn
vacmViewTreeFamilyMask = _VacmViewTreeFamilyMask_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 3),
    _VacmViewTreeFamilyMask_Type()
)
vacmViewTreeFamilyMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmViewTreeFamilyMask.setStatus("current")


class _VacmViewTreeFamilyType_Type(Integer32):
    """Custom type vacmViewTreeFamilyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 2),
          ("included", 1))
    )


_VacmViewTreeFamilyType_Type.__name__ = "Integer32"
_VacmViewTreeFamilyType_Object = MibTableColumn
vacmViewTreeFamilyType = _VacmViewTreeFamilyType_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 4),
    _VacmViewTreeFamilyType_Type()
)
vacmViewTreeFamilyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmViewTreeFamilyType.setStatus("current")


class _VacmViewTreeFamilyStorageType_Type(StorageType):
    """Custom type vacmViewTreeFamilyStorageType based on StorageType"""


_VacmViewTreeFamilyStorageType_Object = MibTableColumn
vacmViewTreeFamilyStorageType = _VacmViewTreeFamilyStorageType_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 5),
    _VacmViewTreeFamilyStorageType_Type()
)
vacmViewTreeFamilyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmViewTreeFamilyStorageType.setStatus("current")
_VacmViewTreeFamilyStatus_Type = RowStatus
_VacmViewTreeFamilyStatus_Object = MibTableColumn
vacmViewTreeFamilyStatus = _VacmViewTreeFamilyStatus_Object(
    (1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 6),
    _VacmViewTreeFamilyStatus_Type()
)
vacmViewTreeFamilyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vacmViewTreeFamilyStatus.setStatus("current")
_VacmMIBConformance_ObjectIdentity = ObjectIdentity
vacmMIBConformance = _VacmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 16, 2)
)
_VacmMIBCompliances_ObjectIdentity = ObjectIdentity
vacmMIBCompliances = _VacmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 16, 2, 1)
)
_VacmMIBGroups_ObjectIdentity = ObjectIdentity
vacmMIBGroups = _VacmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 16, 2, 2)
)

# Managed Objects groups

vacmBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 16, 2, 2, 1)
)
vacmBasicGroup.setObjects(
      *(("SNMP-VIEW-BASED-ACM-MIB", "vacmContextName"),
        ("SNMP-VIEW-BASED-ACM-MIB", "vacmGroupName"),
        ("SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityToGroupStorageType"),
        ("SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityToGroupStatus"),
        ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessContextMatch"),
        ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessReadViewName"),
        ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessWriteViewName"),
        ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessNotifyViewName"),
        ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessStorageType"),
        ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessStatus"),
        ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewSpinLock"),
        ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyMask"),
        ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyType"),
        ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyStorageType"),
        ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyStatus"))
)
if mibBuilder.loadTexts:
    vacmBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vacmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    vacmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-VIEW-BASED-ACM-MIB",
    **{"snmpVacmMIB": snmpVacmMIB,
       "vacmMIBObjects": vacmMIBObjects,
       "vacmContextTable": vacmContextTable,
       "vacmContextEntry": vacmContextEntry,
       "vacmContextName": vacmContextName,
       "vacmSecurityToGroupTable": vacmSecurityToGroupTable,
       "vacmSecurityToGroupEntry": vacmSecurityToGroupEntry,
       "vacmSecurityModel": vacmSecurityModel,
       "vacmSecurityName": vacmSecurityName,
       "vacmGroupName": vacmGroupName,
       "vacmSecurityToGroupStorageType": vacmSecurityToGroupStorageType,
       "vacmSecurityToGroupStatus": vacmSecurityToGroupStatus,
       "vacmAccessTable": vacmAccessTable,
       "vacmAccessEntry": vacmAccessEntry,
       "vacmAccessContextPrefix": vacmAccessContextPrefix,
       "vacmAccessSecurityModel": vacmAccessSecurityModel,
       "vacmAccessSecurityLevel": vacmAccessSecurityLevel,
       "vacmAccessContextMatch": vacmAccessContextMatch,
       "vacmAccessReadViewName": vacmAccessReadViewName,
       "vacmAccessWriteViewName": vacmAccessWriteViewName,
       "vacmAccessNotifyViewName": vacmAccessNotifyViewName,
       "vacmAccessStorageType": vacmAccessStorageType,
       "vacmAccessStatus": vacmAccessStatus,
       "vacmMIBViews": vacmMIBViews,
       "vacmViewSpinLock": vacmViewSpinLock,
       "vacmViewTreeFamilyTable": vacmViewTreeFamilyTable,
       "vacmViewTreeFamilyEntry": vacmViewTreeFamilyEntry,
       "vacmViewTreeFamilyViewName": vacmViewTreeFamilyViewName,
       "vacmViewTreeFamilySubtree": vacmViewTreeFamilySubtree,
       "vacmViewTreeFamilyMask": vacmViewTreeFamilyMask,
       "vacmViewTreeFamilyType": vacmViewTreeFamilyType,
       "vacmViewTreeFamilyStorageType": vacmViewTreeFamilyStorageType,
       "vacmViewTreeFamilyStatus": vacmViewTreeFamilyStatus,
       "vacmMIBConformance": vacmMIBConformance,
       "vacmMIBCompliances": vacmMIBCompliances,
       "vacmMIBCompliance": vacmMIBCompliance,
       "vacmMIBGroups": vacmMIBGroups,
       "vacmBasicGroup": vacmBasicGroup}
)
