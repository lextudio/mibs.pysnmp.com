# SNMP MIB module (WWP-SYSTEM-CONFIG-APPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-SYSTEM-CONFIG-APPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:25 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpSystemConfAppsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20)
)
wwpSystemConfAppsMIB.setRevisions(
        ("2001-04-03 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpSystemConfAppsMIBObjects_ObjectIdentity = ObjectIdentity
wwpSystemConfAppsMIBObjects = _WwpSystemConfAppsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 1)
)
_WwpSystemApps_ObjectIdentity = ObjectIdentity
wwpSystemApps = _WwpSystemApps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 1, 1)
)
_WwpSystemRunningApps_Type = DisplayString
_WwpSystemRunningApps_Object = MibScalar
wwpSystemRunningApps = _WwpSystemRunningApps_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 1, 1, 1),
    _WwpSystemRunningApps_Type()
)
wwpSystemRunningApps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpSystemRunningApps.setStatus("current")


class _WwpSystemAppsSwapActivate_Type(TruthValue):
    """Custom type wwpSystemAppsSwapActivate based on TruthValue"""


_WwpSystemAppsSwapActivate_Object = MibScalar
wwpSystemAppsSwapActivate = _WwpSystemAppsSwapActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 1, 1, 2),
    _WwpSystemAppsSwapActivate_Type()
)
wwpSystemAppsSwapActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSystemAppsSwapActivate.setStatus("current")
_WwpSystemAppsTable_Object = MibTable
wwpSystemAppsTable = _WwpSystemAppsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpSystemAppsTable.setStatus("current")
_WwpSystemAppsEntry_Object = MibTableRow
wwpSystemAppsEntry = _WwpSystemAppsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 1, 1, 3, 1)
)
wwpSystemAppsEntry.setIndexNames(
    (0, "WWP-SYSTEM-CONFIG-APPS-MIB", "wwpSystemAppsImage"),
)
if mibBuilder.loadTexts:
    wwpSystemAppsEntry.setStatus("current")


class _WwpSystemAppsImage_Type(Integer32):
    """Custom type wwpSystemAppsImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1))
    )


_WwpSystemAppsImage_Type.__name__ = "Integer32"
_WwpSystemAppsImage_Object = MibTableColumn
wwpSystemAppsImage = _WwpSystemAppsImage_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 1, 1, 3, 1, 1),
    _WwpSystemAppsImage_Type()
)
wwpSystemAppsImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpSystemAppsImage.setStatus("current")
_WwpSystemAppsName_Type = DisplayString
_WwpSystemAppsName_Object = MibTableColumn
wwpSystemAppsName = _WwpSystemAppsName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 1, 1, 3, 1, 2),
    _WwpSystemAppsName_Type()
)
wwpSystemAppsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpSystemAppsName.setStatus("current")


class _WwpSystemBackupNotifEnabled_Type(TruthValue):
    """Custom type wwpSystemBackupNotifEnabled based on TruthValue"""


_WwpSystemBackupNotifEnabled_Object = MibScalar
wwpSystemBackupNotifEnabled = _WwpSystemBackupNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 1, 1, 4),
    _WwpSystemBackupNotifEnabled_Type()
)
wwpSystemBackupNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSystemBackupNotifEnabled.setStatus("current")
_WwpSystemConf_ObjectIdentity = ObjectIdentity
wwpSystemConf = _WwpSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 1, 2)
)
_WwpSystemConfTable_Object = MibTable
wwpSystemConfTable = _WwpSystemConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpSystemConfTable.setStatus("current")
_WwpSystemConfEntry_Object = MibTableRow
wwpSystemConfEntry = _WwpSystemConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 1, 2, 1, 1)
)
wwpSystemConfEntry.setIndexNames(
    (0, "WWP-SYSTEM-CONFIG-APPS-MIB", "wwpSystemConfIndex"),
)
if mibBuilder.loadTexts:
    wwpSystemConfEntry.setStatus("current")


class _WwpSystemConfIndex_Type(Integer32):
    """Custom type wwpSystemConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpSystemConfIndex_Type.__name__ = "Integer32"
_WwpSystemConfIndex_Object = MibTableColumn
wwpSystemConfIndex = _WwpSystemConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 1, 2, 1, 1, 1),
    _WwpSystemConfIndex_Type()
)
wwpSystemConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpSystemConfIndex.setStatus("current")
_WwpSystemConfName_Type = DisplayString
_WwpSystemConfName_Object = MibTableColumn
wwpSystemConfName = _WwpSystemConfName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 1, 2, 1, 1, 2),
    _WwpSystemConfName_Type()
)
wwpSystemConfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpSystemConfName.setStatus("current")
_WwpSystemBootConfName_Type = DisplayString
_WwpSystemBootConfName_Object = MibScalar
wwpSystemBootConfName = _WwpSystemBootConfName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 1, 2, 2),
    _WwpSystemBootConfName_Type()
)
wwpSystemBootConfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSystemBootConfName.setStatus("current")
_WwpSystemConfSaveName_Type = DisplayString
_WwpSystemConfSaveName_Object = MibScalar
wwpSystemConfSaveName = _WwpSystemConfSaveName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 1, 2, 3),
    _WwpSystemConfSaveName_Type()
)
wwpSystemConfSaveName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSystemConfSaveName.setStatus("current")
_WwpSystemConfAppsMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpSystemConfAppsMIBNotificationPrefix = _WwpSystemConfAppsMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 2)
)
_WwpSystemConfAppsMIBNotifications_ObjectIdentity = ObjectIdentity
wwpSystemConfAppsMIBNotifications = _WwpSystemConfAppsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 2, 0)
)
_WwpSystemConfAppsMIBConformance_ObjectIdentity = ObjectIdentity
wwpSystemConfAppsMIBConformance = _WwpSystemConfAppsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 3)
)
_WwpSystemConfAppsMIBCompliances_ObjectIdentity = ObjectIdentity
wwpSystemConfAppsMIBCompliances = _WwpSystemConfAppsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 3, 1)
)
_WwpSystemConfAppsMIBGroups_ObjectIdentity = ObjectIdentity
wwpSystemConfAppsMIBGroups = _WwpSystemConfAppsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpSystemLoadBackupAppNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 20, 2, 0, 1)
)
wwpSystemLoadBackupAppNotification.setObjects(
    ("WWP-SYSTEM-CONFIG-APPS-MIB", "wwpSystemAppsName")
)
if mibBuilder.loadTexts:
    wwpSystemLoadBackupAppNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-SYSTEM-CONFIG-APPS-MIB",
    **{"wwpSystemConfAppsMIB": wwpSystemConfAppsMIB,
       "wwpSystemConfAppsMIBObjects": wwpSystemConfAppsMIBObjects,
       "wwpSystemApps": wwpSystemApps,
       "wwpSystemRunningApps": wwpSystemRunningApps,
       "wwpSystemAppsSwapActivate": wwpSystemAppsSwapActivate,
       "wwpSystemAppsTable": wwpSystemAppsTable,
       "wwpSystemAppsEntry": wwpSystemAppsEntry,
       "wwpSystemAppsImage": wwpSystemAppsImage,
       "wwpSystemAppsName": wwpSystemAppsName,
       "wwpSystemBackupNotifEnabled": wwpSystemBackupNotifEnabled,
       "wwpSystemConf": wwpSystemConf,
       "wwpSystemConfTable": wwpSystemConfTable,
       "wwpSystemConfEntry": wwpSystemConfEntry,
       "wwpSystemConfIndex": wwpSystemConfIndex,
       "wwpSystemConfName": wwpSystemConfName,
       "wwpSystemBootConfName": wwpSystemBootConfName,
       "wwpSystemConfSaveName": wwpSystemConfSaveName,
       "wwpSystemConfAppsMIBNotificationPrefix": wwpSystemConfAppsMIBNotificationPrefix,
       "wwpSystemConfAppsMIBNotifications": wwpSystemConfAppsMIBNotifications,
       "wwpSystemLoadBackupAppNotification": wwpSystemLoadBackupAppNotification,
       "wwpSystemConfAppsMIBConformance": wwpSystemConfAppsMIBConformance,
       "wwpSystemConfAppsMIBCompliances": wwpSystemConfAppsMIBCompliances,
       "wwpSystemConfAppsMIBGroups": wwpSystemConfAppsMIBGroups}
)
