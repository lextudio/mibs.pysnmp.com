# SNMP MIB module (LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:44 2024
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

(lhnModules,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-GLOBAL-REG",
    "lhnModules")

(lhnNusCommonEvents,
 lhnNusCommonGroups,
 lhnNusCommonNotification) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-MIB",
    "lhnNusCommonEvents",
    "lhnNusCommonGroups",
    "lhnNusCommonNotification")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

lhnNusCommonNotificationModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NotificationMessageCount_Type = Integer32
_NotificationMessageCount_Object = MibScalar
notificationMessageCount = _NotificationMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 1),
    _NotificationMessageCount_Type()
)
notificationMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationMessageCount.setStatus("current")
_NotificationMessageTable_Object = MibTable
notificationMessageTable = _NotificationMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2)
)
if mibBuilder.loadTexts:
    notificationMessageTable.setStatus("current")
_NotificationMessageEntry_Object = MibTableRow
notificationMessageEntry = _NotificationMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1)
)
notificationMessageEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB", "notificationIndex"),
)
if mibBuilder.loadTexts:
    notificationMessageEntry.setStatus("current")
_NotificationIndex_Type = Integer32
_NotificationIndex_Object = MibTableColumn
notificationIndex = _NotificationIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1, 1),
    _NotificationIndex_Type()
)
notificationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationIndex.setStatus("current")
_NotificationMessage_Type = OctetString
_NotificationMessage_Object = MibTableColumn
notificationMessage = _NotificationMessage_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1, 2),
    _NotificationMessage_Type()
)
notificationMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationMessage.setStatus("current")
_NotificationTime_Type = DateAndTime
_NotificationTime_Object = MibTableColumn
notificationTime = _NotificationTime_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1, 3),
    _NotificationTime_Type()
)
notificationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notificationTime.setStatus("current")

# Managed Objects groups


# Notification objects

userNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 3, 1)
)
userNotification.setObjects(
    ("LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB", "notificationMessage")
)
if mibBuilder.loadTexts:
    userNotification.setStatus(
        "current"
    )


# Notifications groups

lhnNusCommonEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 1, 2)
)
lhnNusCommonEventGroup.setObjects(
    ("LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB", "userNotification")
)
if mibBuilder.loadTexts:
    lhnNusCommonEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB",
    **{"lhnNusCommonNotificationModule": lhnNusCommonNotificationModule,
       "lhnNusCommonEventGroup": lhnNusCommonEventGroup,
       "notificationMessageCount": notificationMessageCount,
       "notificationMessageTable": notificationMessageTable,
       "notificationMessageEntry": notificationMessageEntry,
       "notificationIndex": notificationIndex,
       "notificationMessage": notificationMessage,
       "notificationTime": notificationTime,
       "userNotification": userNotification}
)
