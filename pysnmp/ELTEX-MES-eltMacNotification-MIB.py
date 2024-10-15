# SNMP MIB module (ELTEX-MES-eltMacNotification-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-eltMacNotification-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:13 2024
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

(eltMesMng,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMesMng")

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

eltMesMacNotificationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7)
)
eltMesMacNotificationMIB.setRevisions(
        ("2015-11-05 00:00",
         "2015-11-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesMacNotificationObjects_ObjectIdentity = ObjectIdentity
eltMesMacNotificationObjects = _EltMesMacNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1)
)
_EltMesMnFlappingObjects_ObjectIdentity = ObjectIdentity
eltMesMnFlappingObjects = _EltMesMnFlappingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1, 1)
)


class _EltMnFlappingFeatureEnabled_Type(TruthValue):
    """Custom type eltMnFlappingFeatureEnabled based on TruthValue"""


_EltMnFlappingFeatureEnabled_Object = MibScalar
eltMnFlappingFeatureEnabled = _EltMnFlappingFeatureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1, 1, 1),
    _EltMnFlappingFeatureEnabled_Type()
)
eltMnFlappingFeatureEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMnFlappingFeatureEnabled.setStatus("deprecated")


class _EltMnFlappingNotificationsEnabled_Type(TruthValue):
    """Custom type eltMnFlappingNotificationsEnabled based on TruthValue"""


_EltMnFlappingNotificationsEnabled_Object = MibScalar
eltMnFlappingNotificationsEnabled = _EltMnFlappingNotificationsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1, 1, 2),
    _EltMnFlappingNotificationsEnabled_Type()
)
eltMnFlappingNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMnFlappingNotificationsEnabled.setStatus("deprecated")
_EltMnFlappingAddress_Type = MacAddress
_EltMnFlappingAddress_Object = MibScalar
eltMnFlappingAddress = _EltMnFlappingAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1, 1, 3),
    _EltMnFlappingAddress_Type()
)
eltMnFlappingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMnFlappingAddress.setStatus("deprecated")
_EltMnFlappingVlanNumber_Type = VlanIndex
_EltMnFlappingVlanNumber_Object = MibScalar
eltMnFlappingVlanNumber = _EltMnFlappingVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1, 1, 4),
    _EltMnFlappingVlanNumber_Type()
)
eltMnFlappingVlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMnFlappingVlanNumber.setStatus("deprecated")


class _EltMnFlappingFirstPortId_Type(Integer32):
    """Custom type eltMnFlappingFirstPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EltMnFlappingFirstPortId_Type.__name__ = "Integer32"
_EltMnFlappingFirstPortId_Object = MibScalar
eltMnFlappingFirstPortId = _EltMnFlappingFirstPortId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1, 1, 5),
    _EltMnFlappingFirstPortId_Type()
)
eltMnFlappingFirstPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMnFlappingFirstPortId.setStatus("deprecated")


class _EltMnFlappingSecondPortId_Type(Integer32):
    """Custom type eltMnFlappingSecondPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EltMnFlappingSecondPortId_Type.__name__ = "Integer32"
_EltMnFlappingSecondPortId_Object = MibScalar
eltMnFlappingSecondPortId = _EltMnFlappingSecondPortId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1, 1, 6),
    _EltMnFlappingSecondPortId_Type()
)
eltMnFlappingSecondPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMnFlappingSecondPortId.setStatus("deprecated")
_EltMnFlappingTime_Type = TimeStamp
_EltMnFlappingTime_Object = MibScalar
eltMnFlappingTime = _EltMnFlappingTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1, 1, 7),
    _EltMnFlappingTime_Type()
)
eltMnFlappingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMnFlappingTime.setStatus("deprecated")
_EltMesMnNotificationPrefix_ObjectIdentity = ObjectIdentity
eltMesMnNotificationPrefix = _EltMesMnNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 2)
)
_EltMesMnNotifications_ObjectIdentity = ObjectIdentity
eltMesMnNotifications = _EltMesMnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 2, 0)
)

# Managed Objects groups


# Notification objects

eltMnFlappingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 2, 0, 1)
)
eltMnFlappingNotification.setObjects(
      *(("ELTEX-MES-eltMacNotification-MIB", "eltMnFlappingAddress"),
        ("ELTEX-MES-eltMacNotification-MIB", "eltMnFlappingVlanNumber"),
        ("ELTEX-MES-eltMacNotification-MIB", "eltMnFlappingFirstPortId"),
        ("ELTEX-MES-eltMacNotification-MIB", "eltMnFlappingSecondPortId"),
        ("ELTEX-MES-eltMacNotification-MIB", "eltMnFlappingTime"))
)
if mibBuilder.loadTexts:
    eltMnFlappingNotification.setStatus(
        "deprecated"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-eltMacNotification-MIB",
    **{"eltMesMacNotificationMIB": eltMesMacNotificationMIB,
       "eltMesMacNotificationObjects": eltMesMacNotificationObjects,
       "eltMesMnFlappingObjects": eltMesMnFlappingObjects,
       "eltMnFlappingFeatureEnabled": eltMnFlappingFeatureEnabled,
       "eltMnFlappingNotificationsEnabled": eltMnFlappingNotificationsEnabled,
       "eltMnFlappingAddress": eltMnFlappingAddress,
       "eltMnFlappingVlanNumber": eltMnFlappingVlanNumber,
       "eltMnFlappingFirstPortId": eltMnFlappingFirstPortId,
       "eltMnFlappingSecondPortId": eltMnFlappingSecondPortId,
       "eltMnFlappingTime": eltMnFlappingTime,
       "eltMesMnNotificationPrefix": eltMesMnNotificationPrefix,
       "eltMesMnNotifications": eltMesMnNotifications,
       "eltMnFlappingNotification": eltMnFlappingNotification}
)
