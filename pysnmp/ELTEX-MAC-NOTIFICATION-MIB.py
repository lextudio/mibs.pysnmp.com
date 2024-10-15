# SNMP MIB module (ELTEX-MAC-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MAC-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:18 2024
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

(VlanIndex,) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "VlanIndex")

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

eltexMacNotificationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 33)
)
eltexMacNotificationMIB.setRevisions(
        ("2015-11-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltexMacNotificationObjects_ObjectIdentity = ObjectIdentity
eltexMacNotificationObjects = _EltexMacNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 33, 1)
)
_EltexMnFlappingObjects_ObjectIdentity = ObjectIdentity
eltexMnFlappingObjects = _EltexMnFlappingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 33, 1, 1)
)


class _EltexMnFlappingFeatureEnabled_Type(TruthValue):
    """Custom type eltexMnFlappingFeatureEnabled based on TruthValue"""


_EltexMnFlappingFeatureEnabled_Object = MibScalar
eltexMnFlappingFeatureEnabled = _EltexMnFlappingFeatureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 33, 1, 1, 1),
    _EltexMnFlappingFeatureEnabled_Type()
)
eltexMnFlappingFeatureEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMnFlappingFeatureEnabled.setStatus("current")


class _EltexMnFlappingNotificationsEnabled_Type(TruthValue):
    """Custom type eltexMnFlappingNotificationsEnabled based on TruthValue"""


_EltexMnFlappingNotificationsEnabled_Object = MibScalar
eltexMnFlappingNotificationsEnabled = _EltexMnFlappingNotificationsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 33, 1, 1, 2),
    _EltexMnFlappingNotificationsEnabled_Type()
)
eltexMnFlappingNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexMnFlappingNotificationsEnabled.setStatus("current")
_EltexMnFlappingAddress_Type = MacAddress
_EltexMnFlappingAddress_Object = MibScalar
eltexMnFlappingAddress = _EltexMnFlappingAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 33, 1, 1, 3),
    _EltexMnFlappingAddress_Type()
)
eltexMnFlappingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMnFlappingAddress.setStatus("current")
_EltexMnFlappingVlanNumber_Type = VlanIndex
_EltexMnFlappingVlanNumber_Object = MibScalar
eltexMnFlappingVlanNumber = _EltexMnFlappingVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 33, 1, 1, 4),
    _EltexMnFlappingVlanNumber_Type()
)
eltexMnFlappingVlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMnFlappingVlanNumber.setStatus("current")


class _EltexMnFlappingFirstPortId_Type(Integer32):
    """Custom type eltexMnFlappingFirstPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EltexMnFlappingFirstPortId_Type.__name__ = "Integer32"
_EltexMnFlappingFirstPortId_Object = MibScalar
eltexMnFlappingFirstPortId = _EltexMnFlappingFirstPortId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 33, 1, 1, 5),
    _EltexMnFlappingFirstPortId_Type()
)
eltexMnFlappingFirstPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMnFlappingFirstPortId.setStatus("current")


class _EltexMnFlappingSecondPortId_Type(Integer32):
    """Custom type eltexMnFlappingSecondPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EltexMnFlappingSecondPortId_Type.__name__ = "Integer32"
_EltexMnFlappingSecondPortId_Object = MibScalar
eltexMnFlappingSecondPortId = _EltexMnFlappingSecondPortId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 33, 1, 1, 6),
    _EltexMnFlappingSecondPortId_Type()
)
eltexMnFlappingSecondPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMnFlappingSecondPortId.setStatus("current")
_EltexMnFlappingTime_Type = TimeStamp
_EltexMnFlappingTime_Object = MibScalar
eltexMnFlappingTime = _EltexMnFlappingTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 33, 1, 1, 7),
    _EltexMnFlappingTime_Type()
)
eltexMnFlappingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexMnFlappingTime.setStatus("current")
_EltexMnNotificationPrefix_ObjectIdentity = ObjectIdentity
eltexMnNotificationPrefix = _EltexMnNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 33, 2)
)
_EltexMnNotifications_ObjectIdentity = ObjectIdentity
eltexMnNotifications = _EltexMnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 33, 2, 0)
)

# Managed Objects groups


# Notification objects

eltexMnFlappingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 33, 2, 0, 1)
)
eltexMnFlappingNotification.setObjects(
      *(("ELTEX-MAC-NOTIFICATION-MIB", "eltexMnFlappingAddress"),
        ("ELTEX-MAC-NOTIFICATION-MIB", "eltexMnFlappingVlanNumber"),
        ("ELTEX-MAC-NOTIFICATION-MIB", "eltexMnFlappingFirstPortId"),
        ("ELTEX-MAC-NOTIFICATION-MIB", "eltexMnFlappingSecondPortId"),
        ("ELTEX-MAC-NOTIFICATION-MIB", "eltexMnFlappingTime"))
)
if mibBuilder.loadTexts:
    eltexMnFlappingNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MAC-NOTIFICATION-MIB",
    **{"eltexMacNotificationMIB": eltexMacNotificationMIB,
       "eltexMacNotificationObjects": eltexMacNotificationObjects,
       "eltexMnFlappingObjects": eltexMnFlappingObjects,
       "eltexMnFlappingFeatureEnabled": eltexMnFlappingFeatureEnabled,
       "eltexMnFlappingNotificationsEnabled": eltexMnFlappingNotificationsEnabled,
       "eltexMnFlappingAddress": eltexMnFlappingAddress,
       "eltexMnFlappingVlanNumber": eltexMnFlappingVlanNumber,
       "eltexMnFlappingFirstPortId": eltexMnFlappingFirstPortId,
       "eltexMnFlappingSecondPortId": eltexMnFlappingSecondPortId,
       "eltexMnFlappingTime": eltexMnFlappingTime,
       "eltexMnNotificationPrefix": eltexMnNotificationPrefix,
       "eltexMnNotifications": eltexMnNotifications,
       "eltexMnFlappingNotification": eltexMnFlappingNotification}
)
