# SNMP MIB module (CISCO-LOCAL-AUTH-USER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LOCAL-AUTH-USER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:06 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLocalAuthUserMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 798)
)
ciscoLocalAuthUserMIB.setRevisions(
        ("2013-11-08 00:00",
         "2013-05-09 00:00",
         "2012-07-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLocalAuthUserMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLocalAuthUserMIBNotifs = _CiscoLocalAuthUserMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 0)
)
_CiscoLocalAuthUserMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLocalAuthUserMIBObjects = _CiscoLocalAuthUserMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1)
)


class _ClauNotifEnable_Type(TruthValue):
    """Custom type clauNotifEnable based on TruthValue"""


_ClauNotifEnable_Object = MibScalar
clauNotifEnable = _ClauNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 1),
    _ClauNotifEnable_Type()
)
clauNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clauNotifEnable.setStatus("current")
_ClauUserTable_Object = MibTable
clauUserTable = _ClauUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 2)
)
if mibBuilder.loadTexts:
    clauUserTable.setStatus("deprecated")
_ClauUserEntry_Object = MibTableRow
clauUserEntry = _ClauUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 2, 1)
)
clauUserEntry.setIndexNames(
    (0, "CISCO-LOCAL-AUTH-USER-MIB", "clauUserIndex"),
)
if mibBuilder.loadTexts:
    clauUserEntry.setStatus("deprecated")


class _ClauUserIndex_Type(Unsigned32):
    """Custom type clauUserIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ClauUserIndex_Type.__name__ = "Unsigned32"
_ClauUserIndex_Object = MibTableColumn
clauUserIndex = _ClauUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 2, 1, 1),
    _ClauUserIndex_Type()
)
clauUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clauUserIndex.setStatus("deprecated")
_ClauUserName_Type = SnmpAdminString
_ClauUserName_Object = MibTableColumn
clauUserName = _ClauUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 2, 1, 2),
    _ClauUserName_Type()
)
clauUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clauUserName.setStatus("deprecated")


class _ClauUserType_Type(Integer32):
    """Custom type clauUserType based on Integer32"""
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
        *(("defaultUser", 1),
          ("guestUser", 5),
          ("lobbyUser", 2),
          ("managementUser", 3),
          ("networkUser", 4))
    )


_ClauUserType_Type.__name__ = "Integer32"
_ClauUserType_Object = MibTableColumn
clauUserType = _ClauUserType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 2, 1, 3),
    _ClauUserType_Type()
)
clauUserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clauUserType.setStatus("deprecated")
_ClauUserCreationTime_Type = DateAndTime
_ClauUserCreationTime_Object = MibTableColumn
clauUserCreationTime = _ClauUserCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 2, 1, 4),
    _ClauUserCreationTime_Type()
)
clauUserCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clauUserCreationTime.setStatus("deprecated")
_ClauUserLifetime_Type = Unsigned32
_ClauUserLifetime_Object = MibTableColumn
clauUserLifetime = _ClauUserLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 2, 1, 5),
    _ClauUserLifetime_Type()
)
clauUserLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clauUserLifetime.setStatus("deprecated")
if mibBuilder.loadTexts:
    clauUserLifetime.setUnits("seconds")
_ClauUserConfigTable_Object = MibTable
clauUserConfigTable = _ClauUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 3)
)
if mibBuilder.loadTexts:
    clauUserConfigTable.setStatus("current")
_ClauUserConfigEntry_Object = MibTableRow
clauUserConfigEntry = _ClauUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 3, 1)
)
clauUserConfigEntry.setIndexNames(
    (0, "CISCO-LOCAL-AUTH-USER-MIB", "clauUserConfigName"),
)
if mibBuilder.loadTexts:
    clauUserConfigEntry.setStatus("current")


class _ClauUserConfigName_Type(OctetString):
    """Custom type clauUserConfigName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ClauUserConfigName_Type.__name__ = "OctetString"
_ClauUserConfigName_Object = MibTableColumn
clauUserConfigName = _ClauUserConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 3, 1, 1),
    _ClauUserConfigName_Type()
)
clauUserConfigName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clauUserConfigName.setStatus("current")


class _ClauUserConfigType_Type(Integer32):
    """Custom type clauUserConfigType based on Integer32"""
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
        *(("defaultUser", 1),
          ("guestUser", 5),
          ("lobbyUser", 2),
          ("managementUser", 3),
          ("networkUser", 4))
    )


_ClauUserConfigType_Type.__name__ = "Integer32"
_ClauUserConfigType_Object = MibTableColumn
clauUserConfigType = _ClauUserConfigType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 3, 1, 2),
    _ClauUserConfigType_Type()
)
clauUserConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clauUserConfigType.setStatus("current")
_ClauUserConfigCreationTime_Type = DateAndTime
_ClauUserConfigCreationTime_Object = MibTableColumn
clauUserConfigCreationTime = _ClauUserConfigCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 3, 1, 3),
    _ClauUserConfigCreationTime_Type()
)
clauUserConfigCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clauUserConfigCreationTime.setStatus("current")
_ClauUserConfigLifetime_Type = Unsigned32
_ClauUserConfigLifetime_Object = MibTableColumn
clauUserConfigLifetime = _ClauUserConfigLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 3, 1, 4),
    _ClauUserConfigLifetime_Type()
)
clauUserConfigLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clauUserConfigLifetime.setStatus("current")
if mibBuilder.loadTexts:
    clauUserConfigLifetime.setUnits("seconds")
_ClauUserConfigPassword_Type = SnmpAdminString
_ClauUserConfigPassword_Object = MibTableColumn
clauUserConfigPassword = _ClauUserConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 3, 1, 5),
    _ClauUserConfigPassword_Type()
)
clauUserConfigPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clauUserConfigPassword.setStatus("current")
_ClauUserConfigDescription_Type = SnmpAdminString
_ClauUserConfigDescription_Object = MibTableColumn
clauUserConfigDescription = _ClauUserConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 3, 1, 6),
    _ClauUserConfigDescription_Type()
)
clauUserConfigDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clauUserConfigDescription.setStatus("current")
_ClauUserConfigStorageType_Type = StorageType
_ClauUserConfigStorageType_Object = MibTableColumn
clauUserConfigStorageType = _ClauUserConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 3, 1, 7),
    _ClauUserConfigStorageType_Type()
)
clauUserConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clauUserConfigStorageType.setStatus("current")
_ClauUserConfigRowStatus_Type = RowStatus
_ClauUserConfigRowStatus_Object = MibTableColumn
clauUserConfigRowStatus = _ClauUserConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 1, 3, 1, 8),
    _ClauUserConfigRowStatus_Type()
)
clauUserConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clauUserConfigRowStatus.setStatus("current")
_CiscoLocalAuthUserMIBConform_ObjectIdentity = ObjectIdentity
ciscoLocalAuthUserMIBConform = _CiscoLocalAuthUserMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 2)
)
_ClauMIBCompliances_ObjectIdentity = ObjectIdentity
clauMIBCompliances = _ClauMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 2, 1)
)
_ClauMIBGroups_ObjectIdentity = ObjectIdentity
clauMIBGroups = _ClauMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 2, 2)
)

# Managed Objects groups

clauMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 2, 2, 1)
)
clauMIBMainObjectGroup.setObjects(
      *(("CISCO-LOCAL-AUTH-USER-MIB", "clauNotifEnable"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserType"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserCreationTime"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserLifetime"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserName"))
)
if mibBuilder.loadTexts:
    clauMIBMainObjectGroup.setStatus("deprecated")

clauNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 2, 2, 4)
)
clauNotifControlGroup.setObjects(
    ("CISCO-LOCAL-AUTH-USER-MIB", "clauNotifEnable")
)
if mibBuilder.loadTexts:
    clauNotifControlGroup.setStatus("current")

clauUserInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 2, 2, 5)
)
clauUserInfoGroup.setObjects(
      *(("CISCO-LOCAL-AUTH-USER-MIB", "clauUserConfigType"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserConfigCreationTime"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserConfigLifetime"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserConfigPassword"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserConfigDescription"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserConfigStorageType"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserConfigRowStatus"))
)
if mibBuilder.loadTexts:
    clauUserInfoGroup.setStatus("current")


# Notification objects

clauUserAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 0, 1)
)
clauUserAdded.setObjects(
      *(("CISCO-LOCAL-AUTH-USER-MIB", "clauUserName"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserType"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserLifetime"))
)
if mibBuilder.loadTexts:
    clauUserAdded.setStatus(
        "deprecated"
    )

clauUserDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 0, 2)
)
clauUserDeleted.setObjects(
      *(("CISCO-LOCAL-AUTH-USER-MIB", "clauUserName"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserType"))
)
if mibBuilder.loadTexts:
    clauUserDeleted.setStatus(
        "deprecated"
    )

clauUserLoggedIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 0, 3)
)
clauUserLoggedIn.setObjects(
      *(("CISCO-LOCAL-AUTH-USER-MIB", "clauUserName"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserType"))
)
if mibBuilder.loadTexts:
    clauUserLoggedIn.setStatus(
        "deprecated"
    )

clauUserLoggedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 0, 4)
)
clauUserLoggedOut.setObjects(
      *(("CISCO-LOCAL-AUTH-USER-MIB", "clauUserName"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserType"))
)
if mibBuilder.loadTexts:
    clauUserLoggedOut.setStatus(
        "deprecated"
    )

clauUserAdded1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 0, 5)
)
clauUserAdded1.setObjects(
      *(("CISCO-LOCAL-AUTH-USER-MIB", "clauUserType"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserLifetime"))
)
if mibBuilder.loadTexts:
    clauUserAdded1.setStatus(
        "current"
    )

clauUserDeleted1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 0, 6)
)
clauUserDeleted1.setObjects(
    ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserType")
)
if mibBuilder.loadTexts:
    clauUserDeleted1.setStatus(
        "current"
    )

clauUserLoggedIn1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 0, 7)
)
clauUserLoggedIn1.setObjects(
    ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserType")
)
if mibBuilder.loadTexts:
    clauUserLoggedIn1.setStatus(
        "current"
    )

clauUserLoggedOut1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 0, 8)
)
clauUserLoggedOut1.setObjects(
    ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserType")
)
if mibBuilder.loadTexts:
    clauUserLoggedOut1.setStatus(
        "current"
    )


# Notifications groups

clauMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 2, 2, 2)
)
clauMIBNotificationGroup.setObjects(
      *(("CISCO-LOCAL-AUTH-USER-MIB", "clauUserAdded"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserDeleted"))
)
if mibBuilder.loadTexts:
    clauMIBNotificationGroup.setStatus(
        "deprecated"
    )

clauMIBNotificationGroup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 2, 2, 3)
)
clauMIBNotificationGroup1.setObjects(
      *(("CISCO-LOCAL-AUTH-USER-MIB", "clauUserLoggedIn"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserLoggedOut"))
)
if mibBuilder.loadTexts:
    clauMIBNotificationGroup1.setStatus(
        "deprecated"
    )

clauMIBNotificationGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 2, 2, 6)
)
clauMIBNotificationGroup2.setObjects(
      *(("CISCO-LOCAL-AUTH-USER-MIB", "clauUserAdded1"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserDeleted1"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserLoggedIn1"),
        ("CISCO-LOCAL-AUTH-USER-MIB", "clauUserLoggedOut1"))
)
if mibBuilder.loadTexts:
    clauMIBNotificationGroup2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

clauMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 2, 1, 1)
)
if mibBuilder.loadTexts:
    clauMIBCompliance.setStatus(
        "deprecated"
    )

clauMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 2, 1, 2)
)
if mibBuilder.loadTexts:
    clauMIBCompliance1.setStatus(
        "deprecated"
    )

clauMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 798, 2, 1, 3)
)
if mibBuilder.loadTexts:
    clauMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LOCAL-AUTH-USER-MIB",
    **{"ciscoLocalAuthUserMIB": ciscoLocalAuthUserMIB,
       "ciscoLocalAuthUserMIBNotifs": ciscoLocalAuthUserMIBNotifs,
       "clauUserAdded": clauUserAdded,
       "clauUserDeleted": clauUserDeleted,
       "clauUserLoggedIn": clauUserLoggedIn,
       "clauUserLoggedOut": clauUserLoggedOut,
       "clauUserAdded1": clauUserAdded1,
       "clauUserDeleted1": clauUserDeleted1,
       "clauUserLoggedIn1": clauUserLoggedIn1,
       "clauUserLoggedOut1": clauUserLoggedOut1,
       "ciscoLocalAuthUserMIBObjects": ciscoLocalAuthUserMIBObjects,
       "clauNotifEnable": clauNotifEnable,
       "clauUserTable": clauUserTable,
       "clauUserEntry": clauUserEntry,
       "clauUserIndex": clauUserIndex,
       "clauUserName": clauUserName,
       "clauUserType": clauUserType,
       "clauUserCreationTime": clauUserCreationTime,
       "clauUserLifetime": clauUserLifetime,
       "clauUserConfigTable": clauUserConfigTable,
       "clauUserConfigEntry": clauUserConfigEntry,
       "clauUserConfigName": clauUserConfigName,
       "clauUserConfigType": clauUserConfigType,
       "clauUserConfigCreationTime": clauUserConfigCreationTime,
       "clauUserConfigLifetime": clauUserConfigLifetime,
       "clauUserConfigPassword": clauUserConfigPassword,
       "clauUserConfigDescription": clauUserConfigDescription,
       "clauUserConfigStorageType": clauUserConfigStorageType,
       "clauUserConfigRowStatus": clauUserConfigRowStatus,
       "ciscoLocalAuthUserMIBConform": ciscoLocalAuthUserMIBConform,
       "clauMIBCompliances": clauMIBCompliances,
       "clauMIBCompliance": clauMIBCompliance,
       "clauMIBCompliance1": clauMIBCompliance1,
       "clauMIBCompliance2": clauMIBCompliance2,
       "clauMIBGroups": clauMIBGroups,
       "clauMIBMainObjectGroup": clauMIBMainObjectGroup,
       "clauMIBNotificationGroup": clauMIBNotificationGroup,
       "clauMIBNotificationGroup1": clauMIBNotificationGroup1,
       "clauNotifControlGroup": clauNotifControlGroup,
       "clauUserInfoGroup": clauUserInfoGroup,
       "clauMIBNotificationGroup2": clauMIBNotificationGroup2}
)
