# SNMP MIB module (JUNIPER-EX-MAC-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-EX-MAC-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:59 2024
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

(jnxMacNotificationRoot,) = mibBuilder.importSymbols(
    "JUNIPER-EX-SMI",
    "jnxMacNotificationRoot")

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


# MODULE-IDENTITY

jnxMacNotificationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 1)
)
jnxMacNotificationMIB.setRevisions(
        ("2009-01-20 00:00",
         "2009-05-27 00:00",
         "2010-02-09 00:00",
         "2010-04-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMacNotificationMIBObjects_ObjectIdentity = ObjectIdentity
jnxMacNotificationMIBObjects = _JnxMacNotificationMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 1, 1)
)
_JnxMacNotificationMIBGlobalObjects_ObjectIdentity = ObjectIdentity
jnxMacNotificationMIBGlobalObjects = _JnxMacNotificationMIBGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 1, 1, 1)
)
_JnxMacGlobalFeatureEnabled_Type = TruthValue
_JnxMacGlobalFeatureEnabled_Object = MibScalar
jnxMacGlobalFeatureEnabled = _JnxMacGlobalFeatureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 1, 1, 1, 1),
    _JnxMacGlobalFeatureEnabled_Type()
)
jnxMacGlobalFeatureEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMacGlobalFeatureEnabled.setStatus("current")


class _JnxMacNotificationInterval_Type(Unsigned32):
    """Custom type jnxMacNotificationInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxMacNotificationInterval_Type.__name__ = "Unsigned32"
_JnxMacNotificationInterval_Object = MibScalar
jnxMacNotificationInterval = _JnxMacNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 1, 1, 1, 2),
    _JnxMacNotificationInterval_Type()
)
jnxMacNotificationInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMacNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    jnxMacNotificationInterval.setUnits("seconds")
_JnxMacAddressesLearnt_Type = Counter64
_JnxMacAddressesLearnt_Object = MibScalar
jnxMacAddressesLearnt = _JnxMacAddressesLearnt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 1, 1, 1, 3),
    _JnxMacAddressesLearnt_Type()
)
jnxMacAddressesLearnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMacAddressesLearnt.setStatus("current")
_JnxMacAddressesRemoved_Type = Counter64
_JnxMacAddressesRemoved_Object = MibScalar
jnxMacAddressesRemoved = _JnxMacAddressesRemoved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 1, 1, 1, 4),
    _JnxMacAddressesRemoved_Type()
)
jnxMacAddressesRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMacAddressesRemoved.setStatus("current")


class _JnxMacNotificationsEnabled_Type(TruthValue):
    """Custom type jnxMacNotificationsEnabled based on TruthValue"""


_JnxMacNotificationsEnabled_Object = MibScalar
jnxMacNotificationsEnabled = _JnxMacNotificationsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 1, 1, 1, 5),
    _JnxMacNotificationsEnabled_Type()
)
jnxMacNotificationsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMacNotificationsEnabled.setStatus("current")
_JnxMacNotificationsSent_Type = Counter64
_JnxMacNotificationsSent_Object = MibScalar
jnxMacNotificationsSent = _JnxMacNotificationsSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 1, 1, 1, 6),
    _JnxMacNotificationsSent_Type()
)
jnxMacNotificationsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMacNotificationsSent.setStatus("current")


class _JnxMacHistTableMaxLength_Type(Unsigned32):
    """Custom type jnxMacHistTableMaxLength based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_JnxMacHistTableMaxLength_Type.__name__ = "Unsigned32"
_JnxMacHistTableMaxLength_Object = MibScalar
jnxMacHistTableMaxLength = _JnxMacHistTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 1, 1, 1, 7),
    _JnxMacHistTableMaxLength_Type()
)
jnxMacHistTableMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMacHistTableMaxLength.setStatus("current")
if mibBuilder.loadTexts:
    jnxMacHistTableMaxLength.setUnits("entries")
_JnxMacHistoryTable_Object = MibTable
jnxMacHistoryTable = _JnxMacHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    jnxMacHistoryTable.setStatus("current")
_JnxMacHistoryEntry_Object = MibTableRow
jnxMacHistoryEntry = _JnxMacHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 1, 1, 1, 8, 1)
)
jnxMacHistoryEntry.setIndexNames(
    (0, "JUNIPER-EX-MAC-NOTIFICATION-MIB", "jnxHistIndex"),
)
if mibBuilder.loadTexts:
    jnxMacHistoryEntry.setStatus("current")


class _JnxHistIndex_Type(Unsigned32):
    """Custom type jnxHistIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JnxHistIndex_Type.__name__ = "Unsigned32"
_JnxHistIndex_Object = MibTableColumn
jnxHistIndex = _JnxHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 1, 1, 1, 8, 1, 1),
    _JnxHistIndex_Type()
)
jnxHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxHistIndex.setStatus("current")


class _JnxHistMacChangedMsg_Type(OctetString):
    """Custom type jnxHistMacChangedMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_JnxHistMacChangedMsg_Type.__name__ = "OctetString"
_JnxHistMacChangedMsg_Object = MibTableColumn
jnxHistMacChangedMsg = _JnxHistMacChangedMsg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 1, 1, 1, 8, 1, 2),
    _JnxHistMacChangedMsg_Type()
)
jnxHistMacChangedMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxHistMacChangedMsg.setStatus("current")
_JnxHistTimestamp_Type = TimeTicks
_JnxHistTimestamp_Object = MibTableColumn
jnxHistTimestamp = _JnxHistTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 1, 1, 1, 8, 1, 3),
    _JnxHistTimestamp_Type()
)
jnxHistTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxHistTimestamp.setStatus("current")
_JnxMacAddressesUpdated_Type = Counter64
_JnxMacAddressesUpdated_Object = MibScalar
jnxMacAddressesUpdated = _JnxMacAddressesUpdated_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 1, 1, 1, 9),
    _JnxMacAddressesUpdated_Type()
)
jnxMacAddressesUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMacAddressesUpdated.setStatus("current")
_JnxMacNotifications_ObjectIdentity = ObjectIdentity
jnxMacNotifications = _JnxMacNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 2)
)
_JnxMacNotificationsPrefix_ObjectIdentity = ObjectIdentity
jnxMacNotificationsPrefix = _JnxMacNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 2, 0)
)
if mibBuilder.loadTexts:
    jnxMacNotificationsPrefix.setStatus("current")

# Managed Objects groups


# Notification objects

jnxMacChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7, 2, 0, 1)
)
jnxMacChangedNotification.setObjects(
      *(("JUNIPER-EX-MAC-NOTIFICATION-MIB", "jnxHistMacChangedMsg"),
        ("JUNIPER-EX-MAC-NOTIFICATION-MIB", "jnxHistTimestamp"))
)
if mibBuilder.loadTexts:
    jnxMacChangedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-EX-MAC-NOTIFICATION-MIB",
    **{"jnxMacNotificationMIB": jnxMacNotificationMIB,
       "jnxMacNotificationMIBObjects": jnxMacNotificationMIBObjects,
       "jnxMacNotificationMIBGlobalObjects": jnxMacNotificationMIBGlobalObjects,
       "jnxMacGlobalFeatureEnabled": jnxMacGlobalFeatureEnabled,
       "jnxMacNotificationInterval": jnxMacNotificationInterval,
       "jnxMacAddressesLearnt": jnxMacAddressesLearnt,
       "jnxMacAddressesRemoved": jnxMacAddressesRemoved,
       "jnxMacNotificationsEnabled": jnxMacNotificationsEnabled,
       "jnxMacNotificationsSent": jnxMacNotificationsSent,
       "jnxMacHistTableMaxLength": jnxMacHistTableMaxLength,
       "jnxMacHistoryTable": jnxMacHistoryTable,
       "jnxMacHistoryEntry": jnxMacHistoryEntry,
       "jnxHistIndex": jnxHistIndex,
       "jnxHistMacChangedMsg": jnxHistMacChangedMsg,
       "jnxHistTimestamp": jnxHistTimestamp,
       "jnxMacAddressesUpdated": jnxMacAddressesUpdated,
       "jnxMacNotifications": jnxMacNotifications,
       "jnxMacNotificationsPrefix": jnxMacNotificationsPrefix,
       "jnxMacChangedNotification": jnxMacChangedNotification}
)
