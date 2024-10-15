# SNMP MIB module (APNNC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APNNC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:25 2024
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

(apEMSModule,) = mibBuilder.importSymbols(
    "APEMS-MIB",
    "apEMSModule")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

apNNCModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5)
)
apNNCModule.setRevisions(
        ("2012-07-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApNNCMIBObjects_ObjectIdentity = ObjectIdentity
apNNCMIBObjects = _ApNNCMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 1)
)
_ApNNCNotificationObjects_ObjectIdentity = ObjectIdentity
apNNCNotificationObjects = _ApNNCNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2)
)
_ApNNCServerAddressRemote_Type = DisplayString
_ApNNCServerAddressRemote_Object = MibScalar
apNNCServerAddressRemote = _ApNNCServerAddressRemote_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 1),
    _ApNNCServerAddressRemote_Type()
)
apNNCServerAddressRemote.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCServerAddressRemote.setStatus("current")
_ApNNCServerNameRemote_Type = DisplayString
_ApNNCServerNameRemote_Object = MibScalar
apNNCServerNameRemote = _ApNNCServerNameRemote_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 2),
    _ApNNCServerNameRemote_Type()
)
apNNCServerNameRemote.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCServerNameRemote.setStatus("current")
_ApNNCServerAddressLocal_Type = DisplayString
_ApNNCServerAddressLocal_Object = MibScalar
apNNCServerAddressLocal = _ApNNCServerAddressLocal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 3),
    _ApNNCServerAddressLocal_Type()
)
apNNCServerAddressLocal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCServerAddressLocal.setStatus("current")
_ApNNCServerNameLocal_Type = DisplayString
_ApNNCServerNameLocal_Object = MibScalar
apNNCServerNameLocal = _ApNNCServerNameLocal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 2, 4),
    _ApNNCServerNameLocal_Type()
)
apNNCServerNameLocal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCServerNameLocal.setStatus("current")
_ApNNCNotifications_ObjectIdentity = ObjectIdentity
apNNCNotifications = _ApNNCNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3)
)
_ApNNCConfigNotificationsPrefix_ObjectIdentity = ObjectIdentity
apNNCConfigNotificationsPrefix = _ApNNCConfigNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1)
)
_ApNNCServerHealthNotificationsPrefix_ObjectIdentity = ObjectIdentity
apNNCServerHealthNotificationsPrefix = _ApNNCServerHealthNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1)
)
_ApNNCConfigNotifications_ObjectIdentity = ObjectIdentity
apNNCConfigNotifications = _ApNNCConfigNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0)
)
_ApNNCServerHealthNotifications_ObjectIdentity = ObjectIdentity
apNNCServerHealthNotifications = _ApNNCServerHealthNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0)
)
_ApNNCModuleConformance_ObjectIdentity = ObjectIdentity
apNNCModuleConformance = _ApNNCModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4)
)
_ApNNCGroups_ObjectIdentity = ObjectIdentity
apNNCGroups = _ApNNCGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 1)
)
_ApNNCNotificationsGroups_ObjectIdentity = ObjectIdentity
apNNCNotificationsGroups = _ApNNCNotificationsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 2)
)
_ApNNCNotificationObjectsGroups_ObjectIdentity = ObjectIdentity
apNNCNotificationObjectsGroups = _ApNNCNotificationObjectsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 3)
)

# Managed Objects groups

apNNCServerHealthObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 3, 1)
)
apNNCServerHealthObjectsGroup.setObjects(
      *(("APNNC-MIB", "apNNCServerAddressLocal"),
        ("APNNC-MIB", "apNNCServerNameLocal"),
        ("APNNC-MIB", "apNNCServerAddressRemote"),
        ("APNNC-MIB", "apNNCServerNameRemote"))
)
if mibBuilder.loadTexts:
    apNNCServerHealthObjectsGroup.setStatus("current")


# Notification objects

apNNCServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0, 1)
)
apNNCServerUnreachable.setObjects(
      *(("APNNC-MIB", "apNNCServerAddressLocal"),
        ("APNNC-MIB", "apNNCServerNameLocal"),
        ("APNNC-MIB", "apNNCServerAddressRemote"),
        ("APNNC-MIB", "apNNCServerNameRemote"))
)
if mibBuilder.loadTexts:
    apNNCServerUnreachable.setStatus(
        "current"
    )

apNNCServerUnreachableClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 3, 1, 0, 2)
)
apNNCServerUnreachableClear.setObjects(
      *(("APNNC-MIB", "apNNCServerAddressLocal"),
        ("APNNC-MIB", "apNNCServerNameLocal"),
        ("APNNC-MIB", "apNNCServerAddressRemote"),
        ("APNNC-MIB", "apNNCServerNameRemote"))
)
if mibBuilder.loadTexts:
    apNNCServerUnreachableClear.setStatus(
        "current"
    )


# Notifications groups

apNNCServerHealthNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 5, 4, 2, 1)
)
apNNCServerHealthNotificationsGroup.setObjects(
      *(("APNNC-MIB", "apNNCServerUnreachable"),
        ("APNNC-MIB", "apNNCServerUnreachableClear"))
)
if mibBuilder.loadTexts:
    apNNCServerHealthNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APNNC-MIB",
    **{"apNNCModule": apNNCModule,
       "apNNCMIBObjects": apNNCMIBObjects,
       "apNNCNotificationObjects": apNNCNotificationObjects,
       "apNNCServerAddressRemote": apNNCServerAddressRemote,
       "apNNCServerNameRemote": apNNCServerNameRemote,
       "apNNCServerAddressLocal": apNNCServerAddressLocal,
       "apNNCServerNameLocal": apNNCServerNameLocal,
       "apNNCNotifications": apNNCNotifications,
       "apNNCConfigNotificationsPrefix": apNNCConfigNotificationsPrefix,
       "apNNCServerHealthNotificationsPrefix": apNNCServerHealthNotificationsPrefix,
       "apNNCConfigNotifications": apNNCConfigNotifications,
       "apNNCServerHealthNotifications": apNNCServerHealthNotifications,
       "apNNCServerUnreachable": apNNCServerUnreachable,
       "apNNCServerUnreachableClear": apNNCServerUnreachableClear,
       "apNNCModuleConformance": apNNCModuleConformance,
       "apNNCGroups": apNNCGroups,
       "apNNCNotificationsGroups": apNNCNotificationsGroups,
       "apNNCServerHealthNotificationsGroup": apNNCServerHealthNotificationsGroup,
       "apNNCNotificationObjectsGroups": apNNCNotificationObjectsGroups,
       "apNNCServerHealthObjectsGroup": apNNCServerHealthObjectsGroup}
)
