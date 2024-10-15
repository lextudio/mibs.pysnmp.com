# SNMP MIB module (APH323-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APH323-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:22 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetVersion,
 InetZoneIndex) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetVersion",
    "InetZoneIndex")

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

apH323Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10)
)
apH323Module.setRevisions(
        ("2012-07-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApH323MIBObjects_ObjectIdentity = ObjectIdentity
apH323MIBObjects = _ApH323MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10, 1)
)
_ApH323StackTable_Object = MibTable
apH323StackTable = _ApH323StackTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10, 1, 1)
)
if mibBuilder.loadTexts:
    apH323StackTable.setStatus("current")
_ApH323StackEntry_Object = MibTableRow
apH323StackEntry = _ApH323StackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10, 1, 1, 1)
)
apH323StackEntry.setIndexNames(
    (1, "APH323-MIB", "apH323StackName"),
)
if mibBuilder.loadTexts:
    apH323StackEntry.setStatus("current")


class _ApH323StackName_Type(DisplayString):
    """Custom type apH323StackName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApH323StackName_Type.__name__ = "DisplayString"
_ApH323StackName_Object = MibTableColumn
apH323StackName = _ApH323StackName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10, 1, 1, 1, 1),
    _ApH323StackName_Type()
)
apH323StackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323StackName.setStatus("current")
_ApH323StackCurrentCalls_Type = Unsigned32
_ApH323StackCurrentCalls_Object = MibTableColumn
apH323StackCurrentCalls = _ApH323StackCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10, 1, 1, 1, 2),
    _ApH323StackCurrentCalls_Type()
)
apH323StackCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323StackCurrentCalls.setStatus("current")
_ApH323NotificationObjects_ObjectIdentity = ObjectIdentity
apH323NotificationObjects = _ApH323NotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10, 2)
)
_ApH323StackMaxCalls_Type = Unsigned32
_ApH323StackMaxCalls_Object = MibScalar
apH323StackMaxCalls = _ApH323StackMaxCalls_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10, 2, 1),
    _ApH323StackMaxCalls_Type()
)
apH323StackMaxCalls.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apH323StackMaxCalls.setStatus("current")
_ApH323StackMaxCallsThreshold_Type = Unsigned32
_ApH323StackMaxCallsThreshold_Object = MibScalar
apH323StackMaxCallsThreshold = _ApH323StackMaxCallsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10, 2, 2),
    _ApH323StackMaxCallsThreshold_Type()
)
apH323StackMaxCallsThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apH323StackMaxCallsThreshold.setStatus("current")
_ApH323NotificationPrefix_ObjectIdentity = ObjectIdentity
apH323NotificationPrefix = _ApH323NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10, 3)
)
_ApH323Notifications_ObjectIdentity = ObjectIdentity
apH323Notifications = _ApH323Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10, 3, 0)
)
_ApH323Conformance_ObjectIdentity = ObjectIdentity
apH323Conformance = _ApH323Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10, 4)
)
_ApH323Groups_ObjectIdentity = ObjectIdentity
apH323Groups = _ApH323Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10, 4, 1)
)
_ApH323NotificationGroups_ObjectIdentity = ObjectIdentity
apH323NotificationGroups = _ApH323NotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10, 4, 2)
)

# Managed Objects groups

apH323StackObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10, 4, 1, 1)
)
apH323StackObjectsGroup.setObjects(
      *(("APH323-MIB", "apH323StackName"),
        ("APH323-MIB", "apH323StackCurrentCalls"))
)
if mibBuilder.loadTexts:
    apH323StackObjectsGroup.setStatus("current")


# Notification objects

apH323StackMaxCallThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10, 3, 0, 1)
)
apH323StackMaxCallThresholdTrap.setObjects(
      *(("APH323-MIB", "apH323StackName"),
        ("APH323-MIB", "apH323StackMaxCalls"),
        ("APH323-MIB", "apH323StackMaxCallsThreshold"),
        ("APH323-MIB", "apH323StackCurrentCalls"))
)
if mibBuilder.loadTexts:
    apH323StackMaxCallThresholdTrap.setStatus(
        "current"
    )

apH323StackMaxCallThresholdClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10, 3, 0, 2)
)
apH323StackMaxCallThresholdClearTrap.setObjects(
      *(("APH323-MIB", "apH323StackName"),
        ("APH323-MIB", "apH323StackMaxCalls"),
        ("APH323-MIB", "apH323StackMaxCallsThreshold"),
        ("APH323-MIB", "apH323StackCurrentCalls"))
)
if mibBuilder.loadTexts:
    apH323StackMaxCallThresholdClearTrap.setStatus(
        "current"
    )


# Notifications groups

apH323StackNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 10, 4, 2, 1)
)
apH323StackNotificationsGroup.setObjects(
      *(("APH323-MIB", "apH323StackMaxCallThresholdTrap"),
        ("APH323-MIB", "apH323StackMaxCallThresholdClearTrap"))
)
if mibBuilder.loadTexts:
    apH323StackNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APH323-MIB",
    **{"apH323Module": apH323Module,
       "apH323MIBObjects": apH323MIBObjects,
       "apH323StackTable": apH323StackTable,
       "apH323StackEntry": apH323StackEntry,
       "apH323StackName": apH323StackName,
       "apH323StackCurrentCalls": apH323StackCurrentCalls,
       "apH323NotificationObjects": apH323NotificationObjects,
       "apH323StackMaxCalls": apH323StackMaxCalls,
       "apH323StackMaxCallsThreshold": apH323StackMaxCallsThreshold,
       "apH323NotificationPrefix": apH323NotificationPrefix,
       "apH323Notifications": apH323Notifications,
       "apH323StackMaxCallThresholdTrap": apH323StackMaxCallThresholdTrap,
       "apH323StackMaxCallThresholdClearTrap": apH323StackMaxCallThresholdClearTrap,
       "apH323Conformance": apH323Conformance,
       "apH323Groups": apH323Groups,
       "apH323StackObjectsGroup": apH323StackObjectsGroup,
       "apH323NotificationGroups": apH323NotificationGroups,
       "apH323StackNotificationsGroup": apH323StackNotificationsGroup}
)
