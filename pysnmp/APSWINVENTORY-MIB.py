# SNMP MIB module (APSWINVENTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APSWINVENTORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:01 2024
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

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

apSwInventoryModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApSwInventoryMIBObjects_ObjectIdentity = ObjectIdentity
apSwInventoryMIBObjects = _ApSwInventoryMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 1)
)
_ApSwInventoryBootObjects_ObjectIdentity = ObjectIdentity
apSwInventoryBootObjects = _ApSwInventoryBootObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1)
)
_ApSwBootTable_Object = MibTable
apSwBootTable = _ApSwBootTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    apSwBootTable.setStatus("current")
_ApSwBootEntry_Object = MibTableRow
apSwBootEntry = _ApSwBootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1, 1)
)
apSwBootEntry.setIndexNames(
    (0, "APSWINVENTORY-MIB", "apSwBootIndex"),
)
if mibBuilder.loadTexts:
    apSwBootEntry.setStatus("current")


class _ApSwBootIndex_Type(Integer32):
    """Custom type apSwBootIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApSwBootIndex_Type.__name__ = "Integer32"
_ApSwBootIndex_Object = MibTableColumn
apSwBootIndex = _ApSwBootIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1, 1, 1),
    _ApSwBootIndex_Type()
)
apSwBootIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apSwBootIndex.setStatus("current")


class _ApSwBootDescr_Type(DisplayString):
    """Custom type apSwBootDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ApSwBootDescr_Type.__name__ = "DisplayString"
_ApSwBootDescr_Object = MibTableColumn
apSwBootDescr = _ApSwBootDescr_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1, 1, 2),
    _ApSwBootDescr_Type()
)
apSwBootDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSwBootDescr.setStatus("current")


class _ApSwBootType_Type(Integer32):
    """Custom type apSwBootType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootImage", 1),
          ("bootLoader", 2))
    )


_ApSwBootType_Type.__name__ = "Integer32"
_ApSwBootType_Object = MibTableColumn
apSwBootType = _ApSwBootType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1, 1, 3),
    _ApSwBootType_Type()
)
apSwBootType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSwBootType.setStatus("current")


class _ApSwBootStatus_Type(Integer32):
    """Custom type apSwBootStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currentUsing", 1),
          ("previousUsed", 2))
    )


_ApSwBootStatus_Type.__name__ = "Integer32"
_ApSwBootStatus_Object = MibTableColumn
apSwBootStatus = _ApSwBootStatus_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1, 1, 4),
    _ApSwBootStatus_Type()
)
apSwBootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSwBootStatus.setStatus("current")
_ApSwInventoryCfgObjects_ObjectIdentity = ObjectIdentity
apSwInventoryCfgObjects = _ApSwInventoryCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2)
)


class _ApSwCfgCurrentVersion_Type(Integer32):
    """Custom type apSwCfgCurrentVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApSwCfgCurrentVersion_Type.__name__ = "Integer32"
_ApSwCfgCurrentVersion_Object = MibScalar
apSwCfgCurrentVersion = _ApSwCfgCurrentVersion_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 1),
    _ApSwCfgCurrentVersion_Type()
)
apSwCfgCurrentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSwCfgCurrentVersion.setStatus("current")


class _ApSwCfgRunningVersion_Type(Integer32):
    """Custom type apSwCfgRunningVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApSwCfgRunningVersion_Type.__name__ = "Integer32"
_ApSwCfgRunningVersion_Object = MibScalar
apSwCfgRunningVersion = _ApSwCfgRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 2),
    _ApSwCfgRunningVersion_Type()
)
apSwCfgRunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSwCfgRunningVersion.setStatus("current")
_ApSwCfgBackuptable_Object = MibTable
apSwCfgBackuptable = _ApSwCfgBackuptable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    apSwCfgBackuptable.setStatus("current")
_ApSwCfgBackupEntry_Object = MibTableRow
apSwCfgBackupEntry = _ApSwCfgBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 3, 1)
)
apSwCfgBackupEntry.setIndexNames(
    (0, "APSWINVENTORY-MIB", "apSwCfgBackupIndex"),
)
if mibBuilder.loadTexts:
    apSwCfgBackupEntry.setStatus("current")


class _ApSwCfgBackupIndex_Type(Integer32):
    """Custom type apSwCfgBackupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApSwCfgBackupIndex_Type.__name__ = "Integer32"
_ApSwCfgBackupIndex_Object = MibTableColumn
apSwCfgBackupIndex = _ApSwCfgBackupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 3, 1, 1),
    _ApSwCfgBackupIndex_Type()
)
apSwCfgBackupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apSwCfgBackupIndex.setStatus("current")


class _ApSwCfgBackupName_Type(DisplayString):
    """Custom type apSwCfgBackupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSwCfgBackupName_Type.__name__ = "DisplayString"
_ApSwCfgBackupName_Object = MibTableColumn
apSwCfgBackupName = _ApSwCfgBackupName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 3, 1, 2),
    _ApSwCfgBackupName_Type()
)
apSwCfgBackupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSwCfgBackupName.setStatus("current")
_ApSwInventoryNotificationObjects_ObjectIdentity = ObjectIdentity
apSwInventoryNotificationObjects = _ApSwInventoryNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 2)
)
_ApSwCfgNotificationObjects_ObjectIdentity = ObjectIdentity
apSwCfgNotificationObjects = _ApSwCfgNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 2, 1)
)


class _ApSwCfgTrapPreviousVersion_Type(Integer32):
    """Custom type apSwCfgTrapPreviousVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApSwCfgTrapPreviousVersion_Type.__name__ = "Integer32"
_ApSwCfgTrapPreviousVersion_Object = MibScalar
apSwCfgTrapPreviousVersion = _ApSwCfgTrapPreviousVersion_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 2, 1, 1),
    _ApSwCfgTrapPreviousVersion_Type()
)
apSwCfgTrapPreviousVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSwCfgTrapPreviousVersion.setStatus("current")


class _ApSwCfgTrapCurrentVersion_Type(Integer32):
    """Custom type apSwCfgTrapCurrentVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApSwCfgTrapCurrentVersion_Type.__name__ = "Integer32"
_ApSwCfgTrapCurrentVersion_Object = MibScalar
apSwCfgTrapCurrentVersion = _ApSwCfgTrapCurrentVersion_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 2, 1, 2),
    _ApSwCfgTrapCurrentVersion_Type()
)
apSwCfgTrapCurrentVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSwCfgTrapCurrentVersion.setStatus("current")
_ApSwInventoryNotificationPrefix_ObjectIdentity = ObjectIdentity
apSwInventoryNotificationPrefix = _ApSwInventoryNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 3)
)
_ApSwInventoryNotifications_ObjectIdentity = ObjectIdentity
apSwInventoryNotifications = _ApSwInventoryNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 3, 0)
)
_ApSwInventoryConformance_ObjectIdentity = ObjectIdentity
apSwInventoryConformance = _ApSwInventoryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 4)
)
_ApSwInventoryCompliances_ObjectIdentity = ObjectIdentity
apSwInventoryCompliances = _ApSwInventoryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 1)
)
_ApSwInventoryGroups_ObjectIdentity = ObjectIdentity
apSwInventoryGroups = _ApSwInventoryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 2)
)
_ApSwInventoryNotificationsGroups_ObjectIdentity = ObjectIdentity
apSwInventoryNotificationsGroups = _ApSwInventoryNotificationsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 3)
)

# Managed Objects groups

apSwBootObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 2, 1)
)
apSwBootObjectsGroup.setObjects(
      *(("APSWINVENTORY-MIB", "apSwBootDescr"),
        ("APSWINVENTORY-MIB", "apSwBootType"),
        ("APSWINVENTORY-MIB", "apSwBootStatus"))
)
if mibBuilder.loadTexts:
    apSwBootObjectsGroup.setStatus("current")

apSwCfgObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 2, 2)
)
apSwCfgObjectsGroup.setObjects(
      *(("APSWINVENTORY-MIB", "apSwCfgCurrentVersion"),
        ("APSWINVENTORY-MIB", "apSwCfgRunningVersion"),
        ("APSWINVENTORY-MIB", "apSwCfgBackupName"))
)
if mibBuilder.loadTexts:
    apSwCfgObjectsGroup.setStatus("current")


# Notification objects

apSwCfgActivateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 3, 0, 1)
)
apSwCfgActivateNotification.setObjects(
      *(("APSWINVENTORY-MIB", "apSwCfgTrapPreviousVersion"),
        ("APSWINVENTORY-MIB", "apSwCfgTrapCurrentVersion"))
)
if mibBuilder.loadTexts:
    apSwCfgActivateNotification.setStatus(
        "current"
    )


# Notifications groups

apSwInventoryNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 3, 1)
)
apSwInventoryNotificationsGroup.setObjects(
    ("APSWINVENTORY-MIB", "apSwCfgActivateNotification")
)
if mibBuilder.loadTexts:
    apSwInventoryNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APSWINVENTORY-MIB",
    **{"apSwInventoryModule": apSwInventoryModule,
       "apSwInventoryMIBObjects": apSwInventoryMIBObjects,
       "apSwInventoryBootObjects": apSwInventoryBootObjects,
       "apSwBootTable": apSwBootTable,
       "apSwBootEntry": apSwBootEntry,
       "apSwBootIndex": apSwBootIndex,
       "apSwBootDescr": apSwBootDescr,
       "apSwBootType": apSwBootType,
       "apSwBootStatus": apSwBootStatus,
       "apSwInventoryCfgObjects": apSwInventoryCfgObjects,
       "apSwCfgCurrentVersion": apSwCfgCurrentVersion,
       "apSwCfgRunningVersion": apSwCfgRunningVersion,
       "apSwCfgBackuptable": apSwCfgBackuptable,
       "apSwCfgBackupEntry": apSwCfgBackupEntry,
       "apSwCfgBackupIndex": apSwCfgBackupIndex,
       "apSwCfgBackupName": apSwCfgBackupName,
       "apSwInventoryNotificationObjects": apSwInventoryNotificationObjects,
       "apSwCfgNotificationObjects": apSwCfgNotificationObjects,
       "apSwCfgTrapPreviousVersion": apSwCfgTrapPreviousVersion,
       "apSwCfgTrapCurrentVersion": apSwCfgTrapCurrentVersion,
       "apSwInventoryNotificationPrefix": apSwInventoryNotificationPrefix,
       "apSwInventoryNotifications": apSwInventoryNotifications,
       "apSwCfgActivateNotification": apSwCfgActivateNotification,
       "apSwInventoryConformance": apSwInventoryConformance,
       "apSwInventoryCompliances": apSwInventoryCompliances,
       "apSwInventoryGroups": apSwInventoryGroups,
       "apSwBootObjectsGroup": apSwBootObjectsGroup,
       "apSwCfgObjectsGroup": apSwCfgObjectsGroup,
       "apSwInventoryNotificationsGroups": apSwInventoryNotificationsGroups,
       "apSwInventoryNotificationsGroup": apSwInventoryNotificationsGroup}
)
