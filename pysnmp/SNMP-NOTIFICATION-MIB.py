# SNMP MIB module (SNMP-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMP-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:34 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(SnmpTagValue,
 snmpTargetParamsName) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "SnmpTagValue",
    "snmpTargetParamsName")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

snmpNotificationMIB = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 13)
)
snmpNotificationMIB.setRevisions(
        ("2002-10-14 00:00",
         "1998-08-04 00:00",
         "1997-07-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpNotifyObjects_ObjectIdentity = ObjectIdentity
snmpNotifyObjects = _SnmpNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 13, 1)
)
_SnmpNotifyTable_Object = MibTable
snmpNotifyTable = _SnmpNotifyTable_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 1)
)
if mibBuilder.loadTexts:
    snmpNotifyTable.setStatus("current")
_SnmpNotifyEntry_Object = MibTableRow
snmpNotifyEntry = _SnmpNotifyEntry_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 1, 1)
)
snmpNotifyEntry.setIndexNames(
    (1, "SNMP-NOTIFICATION-MIB", "snmpNotifyName"),
)
if mibBuilder.loadTexts:
    snmpNotifyEntry.setStatus("current")


class _SnmpNotifyName_Type(SnmpAdminString):
    """Custom type snmpNotifyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpNotifyName_Type.__name__ = "SnmpAdminString"
_SnmpNotifyName_Object = MibTableColumn
snmpNotifyName = _SnmpNotifyName_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 1, 1, 1),
    _SnmpNotifyName_Type()
)
snmpNotifyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpNotifyName.setStatus("current")
_SnmpNotifyTag_Type = SnmpTagValue
_SnmpNotifyTag_Object = MibTableColumn
snmpNotifyTag = _SnmpNotifyTag_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 1, 1, 2),
    _SnmpNotifyTag_Type()
)
snmpNotifyTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpNotifyTag.setStatus("current")


class _SnmpNotifyType_Type(Integer32):
    """Custom type snmpNotifyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inform", 2),
          ("trap", 1))
    )


_SnmpNotifyType_Type.__name__ = "Integer32"
_SnmpNotifyType_Object = MibTableColumn
snmpNotifyType = _SnmpNotifyType_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 1, 1, 3),
    _SnmpNotifyType_Type()
)
snmpNotifyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpNotifyType.setStatus("current")


class _SnmpNotifyStorageType_Type(StorageType):
    """Custom type snmpNotifyStorageType based on StorageType"""


_SnmpNotifyStorageType_Object = MibTableColumn
snmpNotifyStorageType = _SnmpNotifyStorageType_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 1, 1, 4),
    _SnmpNotifyStorageType_Type()
)
snmpNotifyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpNotifyStorageType.setStatus("current")
_SnmpNotifyRowStatus_Type = RowStatus
_SnmpNotifyRowStatus_Object = MibTableColumn
snmpNotifyRowStatus = _SnmpNotifyRowStatus_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 1, 1, 5),
    _SnmpNotifyRowStatus_Type()
)
snmpNotifyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpNotifyRowStatus.setStatus("current")
_SnmpNotifyFilterProfileTable_Object = MibTable
snmpNotifyFilterProfileTable = _SnmpNotifyFilterProfileTable_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 2)
)
if mibBuilder.loadTexts:
    snmpNotifyFilterProfileTable.setStatus("current")
_SnmpNotifyFilterProfileEntry_Object = MibTableRow
snmpNotifyFilterProfileEntry = _SnmpNotifyFilterProfileEntry_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 2, 1)
)
snmpNotifyFilterProfileEntry.setIndexNames(
    (1, "SNMP-TARGET-MIB", "snmpTargetParamsName"),
)
if mibBuilder.loadTexts:
    snmpNotifyFilterProfileEntry.setStatus("current")


class _SnmpNotifyFilterProfileName_Type(SnmpAdminString):
    """Custom type snmpNotifyFilterProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpNotifyFilterProfileName_Type.__name__ = "SnmpAdminString"
_SnmpNotifyFilterProfileName_Object = MibTableColumn
snmpNotifyFilterProfileName = _SnmpNotifyFilterProfileName_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 2, 1, 1),
    _SnmpNotifyFilterProfileName_Type()
)
snmpNotifyFilterProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpNotifyFilterProfileName.setStatus("current")


class _SnmpNotifyFilterProfileStorType_Type(StorageType):
    """Custom type snmpNotifyFilterProfileStorType based on StorageType"""


_SnmpNotifyFilterProfileStorType_Object = MibTableColumn
snmpNotifyFilterProfileStorType = _SnmpNotifyFilterProfileStorType_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 2, 1, 2),
    _SnmpNotifyFilterProfileStorType_Type()
)
snmpNotifyFilterProfileStorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpNotifyFilterProfileStorType.setStatus("current")
_SnmpNotifyFilterProfileRowStatus_Type = RowStatus
_SnmpNotifyFilterProfileRowStatus_Object = MibTableColumn
snmpNotifyFilterProfileRowStatus = _SnmpNotifyFilterProfileRowStatus_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 2, 1, 3),
    _SnmpNotifyFilterProfileRowStatus_Type()
)
snmpNotifyFilterProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpNotifyFilterProfileRowStatus.setStatus("current")
_SnmpNotifyFilterTable_Object = MibTable
snmpNotifyFilterTable = _SnmpNotifyFilterTable_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 3)
)
if mibBuilder.loadTexts:
    snmpNotifyFilterTable.setStatus("current")
_SnmpNotifyFilterEntry_Object = MibTableRow
snmpNotifyFilterEntry = _SnmpNotifyFilterEntry_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 3, 1)
)
snmpNotifyFilterEntry.setIndexNames(
    (0, "SNMP-NOTIFICATION-MIB", "snmpNotifyFilterProfileName"),
    (1, "SNMP-NOTIFICATION-MIB", "snmpNotifyFilterSubtree"),
)
if mibBuilder.loadTexts:
    snmpNotifyFilterEntry.setStatus("current")
_SnmpNotifyFilterSubtree_Type = ObjectIdentifier
_SnmpNotifyFilterSubtree_Object = MibTableColumn
snmpNotifyFilterSubtree = _SnmpNotifyFilterSubtree_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 3, 1, 1),
    _SnmpNotifyFilterSubtree_Type()
)
snmpNotifyFilterSubtree.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpNotifyFilterSubtree.setStatus("current")


class _SnmpNotifyFilterMask_Type(OctetString):
    """Custom type snmpNotifyFilterMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SnmpNotifyFilterMask_Type.__name__ = "OctetString"
_SnmpNotifyFilterMask_Object = MibTableColumn
snmpNotifyFilterMask = _SnmpNotifyFilterMask_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 3, 1, 2),
    _SnmpNotifyFilterMask_Type()
)
snmpNotifyFilterMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpNotifyFilterMask.setStatus("current")


class _SnmpNotifyFilterType_Type(Integer32):
    """Custom type snmpNotifyFilterType based on Integer32"""
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


_SnmpNotifyFilterType_Type.__name__ = "Integer32"
_SnmpNotifyFilterType_Object = MibTableColumn
snmpNotifyFilterType = _SnmpNotifyFilterType_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 3, 1, 3),
    _SnmpNotifyFilterType_Type()
)
snmpNotifyFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpNotifyFilterType.setStatus("current")


class _SnmpNotifyFilterStorageType_Type(StorageType):
    """Custom type snmpNotifyFilterStorageType based on StorageType"""


_SnmpNotifyFilterStorageType_Object = MibTableColumn
snmpNotifyFilterStorageType = _SnmpNotifyFilterStorageType_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 3, 1, 4),
    _SnmpNotifyFilterStorageType_Type()
)
snmpNotifyFilterStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpNotifyFilterStorageType.setStatus("current")
_SnmpNotifyFilterRowStatus_Type = RowStatus
_SnmpNotifyFilterRowStatus_Object = MibTableColumn
snmpNotifyFilterRowStatus = _SnmpNotifyFilterRowStatus_Object(
    (1, 3, 6, 1, 6, 3, 13, 1, 3, 1, 5),
    _SnmpNotifyFilterRowStatus_Type()
)
snmpNotifyFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpNotifyFilterRowStatus.setStatus("current")
_SnmpNotifyConformance_ObjectIdentity = ObjectIdentity
snmpNotifyConformance = _SnmpNotifyConformance_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 13, 3)
)
_SnmpNotifyCompliances_ObjectIdentity = ObjectIdentity
snmpNotifyCompliances = _SnmpNotifyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 13, 3, 1)
)
_SnmpNotifyGroups_ObjectIdentity = ObjectIdentity
snmpNotifyGroups = _SnmpNotifyGroups_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 13, 3, 2)
)

# Managed Objects groups

snmpNotifyGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 13, 3, 2, 1)
)
snmpNotifyGroup.setObjects(
      *(("SNMP-NOTIFICATION-MIB", "snmpNotifyTag"),
        ("SNMP-NOTIFICATION-MIB", "snmpNotifyType"),
        ("SNMP-NOTIFICATION-MIB", "snmpNotifyStorageType"),
        ("SNMP-NOTIFICATION-MIB", "snmpNotifyRowStatus"))
)
if mibBuilder.loadTexts:
    snmpNotifyGroup.setStatus("current")

snmpNotifyFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 13, 3, 2, 2)
)
snmpNotifyFilterGroup.setObjects(
      *(("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterProfileName"),
        ("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterProfileStorType"),
        ("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterProfileRowStatus"),
        ("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterMask"),
        ("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterType"),
        ("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterStorageType"),
        ("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterRowStatus"))
)
if mibBuilder.loadTexts:
    snmpNotifyFilterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

snmpNotifyBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 13, 3, 1, 1)
)
if mibBuilder.loadTexts:
    snmpNotifyBasicCompliance.setStatus(
        "current"
    )

snmpNotifyBasicFiltersCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 13, 3, 1, 2)
)
if mibBuilder.loadTexts:
    snmpNotifyBasicFiltersCompliance.setStatus(
        "current"
    )

snmpNotifyFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 13, 3, 1, 3)
)
if mibBuilder.loadTexts:
    snmpNotifyFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-NOTIFICATION-MIB",
    **{"snmpNotificationMIB": snmpNotificationMIB,
       "snmpNotifyObjects": snmpNotifyObjects,
       "snmpNotifyTable": snmpNotifyTable,
       "snmpNotifyEntry": snmpNotifyEntry,
       "snmpNotifyName": snmpNotifyName,
       "snmpNotifyTag": snmpNotifyTag,
       "snmpNotifyType": snmpNotifyType,
       "snmpNotifyStorageType": snmpNotifyStorageType,
       "snmpNotifyRowStatus": snmpNotifyRowStatus,
       "snmpNotifyFilterProfileTable": snmpNotifyFilterProfileTable,
       "snmpNotifyFilterProfileEntry": snmpNotifyFilterProfileEntry,
       "snmpNotifyFilterProfileName": snmpNotifyFilterProfileName,
       "snmpNotifyFilterProfileStorType": snmpNotifyFilterProfileStorType,
       "snmpNotifyFilterProfileRowStatus": snmpNotifyFilterProfileRowStatus,
       "snmpNotifyFilterTable": snmpNotifyFilterTable,
       "snmpNotifyFilterEntry": snmpNotifyFilterEntry,
       "snmpNotifyFilterSubtree": snmpNotifyFilterSubtree,
       "snmpNotifyFilterMask": snmpNotifyFilterMask,
       "snmpNotifyFilterType": snmpNotifyFilterType,
       "snmpNotifyFilterStorageType": snmpNotifyFilterStorageType,
       "snmpNotifyFilterRowStatus": snmpNotifyFilterRowStatus,
       "snmpNotifyConformance": snmpNotifyConformance,
       "snmpNotifyCompliances": snmpNotifyCompliances,
       "snmpNotifyBasicCompliance": snmpNotifyBasicCompliance,
       "snmpNotifyBasicFiltersCompliance": snmpNotifyBasicFiltersCompliance,
       "snmpNotifyFullCompliance": snmpNotifyFullCompliance,
       "snmpNotifyGroups": snmpNotifyGroups,
       "snmpNotifyGroup": snmpNotifyGroup,
       "snmpNotifyFilterGroup": snmpNotifyFilterGroup}
)
