# SNMP MIB module (ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:11 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

etsysMgmtAuthNotificationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60)
)
etsysMgmtAuthNotificationMIB.setRevisions(
        ("2011-03-08 20:40",
         "2005-11-14 16:48")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EtsysMgmtAuthNotificationTypes(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_EtsysMgmtAuthObjects_ObjectIdentity = ObjectIdentity
etsysMgmtAuthObjects = _EtsysMgmtAuthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1)
)
_EtsysMgmtAuthNotificationBranch_ObjectIdentity = ObjectIdentity
etsysMgmtAuthNotificationBranch = _EtsysMgmtAuthNotificationBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0)
)
_EtsysMgmtAuthConfigBranch_ObjectIdentity = ObjectIdentity
etsysMgmtAuthConfigBranch = _EtsysMgmtAuthConfigBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 1)
)


class _EtsysMgmtAuthNotificationsSupported_Type(EtsysMgmtAuthNotificationTypes):
    """Custom type etsysMgmtAuthNotificationsSupported based on EtsysMgmtAuthNotificationTypes"""
    defaultBinValue = "0"


_EtsysMgmtAuthNotificationsSupported_Object = MibScalar
etsysMgmtAuthNotificationsSupported = _EtsysMgmtAuthNotificationsSupported_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 1, 1),
    _EtsysMgmtAuthNotificationsSupported_Type()
)
etsysMgmtAuthNotificationsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmtAuthNotificationsSupported.setStatus("current")


class _EtsysMgmtAuthNotificationEnabledStatus_Type(EtsysMgmtAuthNotificationTypes):
    """Custom type etsysMgmtAuthNotificationEnabledStatus based on EtsysMgmtAuthNotificationTypes"""
    defaultBinValue = "0"


_EtsysMgmtAuthNotificationEnabledStatus_Object = MibScalar
etsysMgmtAuthNotificationEnabledStatus = _EtsysMgmtAuthNotificationEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 1, 2),
    _EtsysMgmtAuthNotificationEnabledStatus_Type()
)
etsysMgmtAuthNotificationEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmtAuthNotificationEnabledStatus.setStatus("current")
_EtsysMgmtAuthAuthenticationBranch_ObjectIdentity = ObjectIdentity
etsysMgmtAuthAuthenticationBranch = _EtsysMgmtAuthAuthenticationBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2)
)
_EtsysMgmtAuthType_Type = EtsysMgmtAuthNotificationTypes
_EtsysMgmtAuthType_Object = MibScalar
etsysMgmtAuthType = _EtsysMgmtAuthType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 1),
    _EtsysMgmtAuthType_Type()
)
etsysMgmtAuthType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysMgmtAuthType.setStatus("current")
_EtsysMgmtAuthUserName_Type = DisplayString
_EtsysMgmtAuthUserName_Object = MibScalar
etsysMgmtAuthUserName = _EtsysMgmtAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 2),
    _EtsysMgmtAuthUserName_Type()
)
etsysMgmtAuthUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysMgmtAuthUserName.setStatus("current")
_EtsysMgmtAuthInetAddressType_Type = InetAddressType
_EtsysMgmtAuthInetAddressType_Object = MibScalar
etsysMgmtAuthInetAddressType = _EtsysMgmtAuthInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 3),
    _EtsysMgmtAuthInetAddressType_Type()
)
etsysMgmtAuthInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysMgmtAuthInetAddressType.setStatus("current")
_EtsysMgmtAuthInetAddress_Type = InetAddress
_EtsysMgmtAuthInetAddress_Object = MibScalar
etsysMgmtAuthInetAddress = _EtsysMgmtAuthInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 4),
    _EtsysMgmtAuthInetAddress_Type()
)
etsysMgmtAuthInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysMgmtAuthInetAddress.setStatus("current")
_EtsysMgmtAuthInIfIndex_Type = InterfaceIndexOrZero
_EtsysMgmtAuthInIfIndex_Object = MibScalar
etsysMgmtAuthInIfIndex = _EtsysMgmtAuthInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 5),
    _EtsysMgmtAuthInIfIndex_Type()
)
etsysMgmtAuthInIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysMgmtAuthInIfIndex.setStatus("current")
_EtsysMgmtAuthConformance_ObjectIdentity = ObjectIdentity
etsysMgmtAuthConformance = _EtsysMgmtAuthConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2)
)
_EtsysMgmtAuthGroups_ObjectIdentity = ObjectIdentity
etsysMgmtAuthGroups = _EtsysMgmtAuthGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1)
)
_EtsysMgmtAuthCompliances_ObjectIdentity = ObjectIdentity
etsysMgmtAuthCompliances = _EtsysMgmtAuthCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 2)
)

# Managed Objects groups

etsysMgmtAuthConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1, 1)
)
etsysMgmtAuthConfigGroup.setObjects(
      *(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthNotificationsSupported"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthNotificationEnabledStatus"))
)
if mibBuilder.loadTexts:
    etsysMgmtAuthConfigGroup.setStatus("current")

etsysMgmtAuthHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1, 2)
)
etsysMgmtAuthHistoryGroup.setObjects(
      *(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
)
if mibBuilder.loadTexts:
    etsysMgmtAuthHistoryGroup.setStatus("current")


# Notification objects

etsysMgmtAuthSuccessNotificiation = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 1)
)
etsysMgmtAuthSuccessNotificiation.setObjects(
      *(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
)
if mibBuilder.loadTexts:
    etsysMgmtAuthSuccessNotificiation.setStatus(
        "current"
    )

etsysMgmtAuthFailNotificiation = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 2)
)
etsysMgmtAuthFailNotificiation.setObjects(
      *(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
)
if mibBuilder.loadTexts:
    etsysMgmtAuthFailNotificiation.setStatus(
        "current"
    )

etsysMgmtAuthInactiveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 3)
)
etsysMgmtAuthInactiveNotification.setObjects(
      *(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
)
if mibBuilder.loadTexts:
    etsysMgmtAuthInactiveNotification.setStatus(
        "current"
    )

etsysMgmtAuthMaxAuthAttemptNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 4)
)
etsysMgmtAuthMaxAuthAttemptNotification.setObjects(
      *(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
)
if mibBuilder.loadTexts:
    etsysMgmtAuthMaxAuthAttemptNotification.setStatus(
        "current"
    )

etsysMgmtAuthMaxFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 5)
)
etsysMgmtAuthMaxFailNotification.setObjects(
      *(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
)
if mibBuilder.loadTexts:
    etsysMgmtAuthMaxFailNotification.setStatus(
        "current"
    )


# Notifications groups

etsysMgmtAuthNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1, 3)
)
etsysMgmtAuthNotificationGroup.setObjects(
      *(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthSuccessNotificiation"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthFailNotificiation"))
)
if mibBuilder.loadTexts:
    etsysMgmtAuthNotificationGroup.setStatus(
        "current"
    )

etsysMgmtAuthNotificationUserGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1, 4)
)
etsysMgmtAuthNotificationUserGroup.setObjects(
      *(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInactiveNotification"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthMaxAuthAttemptNotification"),
        ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthMaxFailNotification"))
)
if mibBuilder.loadTexts:
    etsysMgmtAuthNotificationUserGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysMgmtAuthCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysMgmtAuthCompliance.setStatus(
        "current"
    )

etsysMgmtAuthUserCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 2, 2)
)
if mibBuilder.loadTexts:
    etsysMgmtAuthUserCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB",
    **{"EtsysMgmtAuthNotificationTypes": EtsysMgmtAuthNotificationTypes,
       "etsysMgmtAuthNotificationMIB": etsysMgmtAuthNotificationMIB,
       "etsysMgmtAuthObjects": etsysMgmtAuthObjects,
       "etsysMgmtAuthNotificationBranch": etsysMgmtAuthNotificationBranch,
       "etsysMgmtAuthSuccessNotificiation": etsysMgmtAuthSuccessNotificiation,
       "etsysMgmtAuthFailNotificiation": etsysMgmtAuthFailNotificiation,
       "etsysMgmtAuthInactiveNotification": etsysMgmtAuthInactiveNotification,
       "etsysMgmtAuthMaxAuthAttemptNotification": etsysMgmtAuthMaxAuthAttemptNotification,
       "etsysMgmtAuthMaxFailNotification": etsysMgmtAuthMaxFailNotification,
       "etsysMgmtAuthConfigBranch": etsysMgmtAuthConfigBranch,
       "etsysMgmtAuthNotificationsSupported": etsysMgmtAuthNotificationsSupported,
       "etsysMgmtAuthNotificationEnabledStatus": etsysMgmtAuthNotificationEnabledStatus,
       "etsysMgmtAuthAuthenticationBranch": etsysMgmtAuthAuthenticationBranch,
       "etsysMgmtAuthType": etsysMgmtAuthType,
       "etsysMgmtAuthUserName": etsysMgmtAuthUserName,
       "etsysMgmtAuthInetAddressType": etsysMgmtAuthInetAddressType,
       "etsysMgmtAuthInetAddress": etsysMgmtAuthInetAddress,
       "etsysMgmtAuthInIfIndex": etsysMgmtAuthInIfIndex,
       "etsysMgmtAuthConformance": etsysMgmtAuthConformance,
       "etsysMgmtAuthGroups": etsysMgmtAuthGroups,
       "etsysMgmtAuthConfigGroup": etsysMgmtAuthConfigGroup,
       "etsysMgmtAuthHistoryGroup": etsysMgmtAuthHistoryGroup,
       "etsysMgmtAuthNotificationGroup": etsysMgmtAuthNotificationGroup,
       "etsysMgmtAuthNotificationUserGroup": etsysMgmtAuthNotificationUserGroup,
       "etsysMgmtAuthCompliances": etsysMgmtAuthCompliances,
       "etsysMgmtAuthCompliance": etsysMgmtAuthCompliance,
       "etsysMgmtAuthUserCompliance": etsysMgmtAuthUserCompliance}
)
