# SNMP MIB module (OG-HOST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OG-HOST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:48 2024
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

(ogMgmt,) = mibBuilder.importSymbols(
    "OG-SMI-MIB",
    "ogMgmt")

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

ogHostMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14)
)
ogHostMib.setRevisions(
        ("2013-08-11 00:00",
         "2010-03-22 11:27",
         "2008-11-27 11:40")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OgHostMibNotificationPrefix_ObjectIdentity = ObjectIdentity
ogHostMibNotificationPrefix = _OgHostMibNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 2)
)
_OghostMibNotifications_ObjectIdentity = ObjectIdentity
oghostMibNotifications = _OghostMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 2, 0)
)
_OgHostMibConformance_ObjectIdentity = ObjectIdentity
ogHostMibConformance = _OgHostMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 3)
)
_OgHostMibCompliances_ObjectIdentity = ObjectIdentity
ogHostMibCompliances = _OgHostMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 1)
)
_OgHostMibGroups_ObjectIdentity = ObjectIdentity
ogHostMibGroups = _OgHostMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 2)
)
_OgHostMibObjects_ObjectIdentity = ObjectIdentity
ogHostMibObjects = _OgHostMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 10)
)
_OghostEvent_ObjectIdentity = ObjectIdentity
oghostEvent = _OghostEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1)
)
_OghostEventTable_Object = MibTable
oghostEventTable = _OghostEventTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1)
)
if mibBuilder.loadTexts:
    oghostEventTable.setStatus("current")
_OghostEventEntry_Object = MibTableRow
oghostEventEntry = _OghostEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1)
)
oghostEventEntry.setIndexNames(
    (0, "OG-HOST-MIB", "oghostEventIndex"),
)
if mibBuilder.loadTexts:
    oghostEventEntry.setStatus("current")


class _OghostEventIndex_Type(Integer32):
    """Custom type oghostEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OghostEventIndex_Type.__name__ = "Integer32"
_OghostEventIndex_Object = MibTableColumn
oghostEventIndex = _OghostEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 1),
    _OghostEventIndex_Type()
)
oghostEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oghostEventIndex.setStatus("current")
_OghostEventUsername_Type = DisplayString
_OghostEventUsername_Object = MibTableColumn
oghostEventUsername = _OghostEventUsername_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 10),
    _OghostEventUsername_Type()
)
oghostEventUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oghostEventUsername.setStatus("current")
_OghostEventType_Type = DisplayString
_OghostEventType_Object = MibTableColumn
oghostEventType = _OghostEventType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 11),
    _OghostEventType_Type()
)
oghostEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oghostEventType.setStatus("current")
_OghostEventAddress_Type = DisplayString
_OghostEventAddress_Object = MibTableColumn
oghostEventAddress = _OghostEventAddress_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 12),
    _OghostEventAddress_Type()
)
oghostEventAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oghostEventAddress.setStatus("current")
_OghostEventDescription_Type = DisplayString
_OghostEventDescription_Object = MibTableColumn
oghostEventDescription = _OghostEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 13),
    _OghostEventDescription_Type()
)
oghostEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oghostEventDescription.setStatus("current")
_OghostEventProtocol_Type = DisplayString
_OghostEventProtocol_Object = MibTableColumn
oghostEventProtocol = _OghostEventProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 14),
    _OghostEventProtocol_Type()
)
oghostEventProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oghostEventProtocol.setStatus("current")
_OghostEventPort_Type = Integer32
_OghostEventPort_Object = MibTableColumn
oghostEventPort = _OghostEventPort_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 15),
    _OghostEventPort_Type()
)
oghostEventPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oghostEventPort.setStatus("current")

# Managed Objects groups

ogHostMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 2, 1)
)
ogHostMibGroup.setObjects(
      *(("OG-HOST-MIB", "oghostEventUsername"),
        ("OG-HOST-MIB", "oghostEventType"),
        ("OG-HOST-MIB", "oghostEventAddress"),
        ("OG-HOST-MIB", "oghostEventDescription"),
        ("OG-HOST-MIB", "oghostEventProtocol"),
        ("OG-HOST-MIB", "oghostEventPort"))
)
if mibBuilder.loadTexts:
    ogHostMibGroup.setStatus("current")


# Notification objects

oghostEventOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 2, 0, 200)
)
oghostEventOccurred.setObjects(
      *(("OG-HOST-MIB", "oghostEventUsername"),
        ("OG-HOST-MIB", "oghostEventType"),
        ("OG-HOST-MIB", "oghostEventAddress"),
        ("OG-HOST-MIB", "oghostEventDescription"),
        ("OG-HOST-MIB", "oghostEventProtocol"),
        ("OG-HOST-MIB", "oghostEventPort"))
)
if mibBuilder.loadTexts:
    oghostEventOccurred.setStatus(
        "current"
    )


# Notifications groups

oghostNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 2, 2)
)
oghostNotificationsGroup.setObjects(
    ("OG-HOST-MIB", "oghostEventOccurred")
)
if mibBuilder.loadTexts:
    oghostNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ogHostMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ogHostMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OG-HOST-MIB",
    **{"ogHostMib": ogHostMib,
       "ogHostMibNotificationPrefix": ogHostMibNotificationPrefix,
       "oghostMibNotifications": oghostMibNotifications,
       "oghostEventOccurred": oghostEventOccurred,
       "ogHostMibConformance": ogHostMibConformance,
       "ogHostMibCompliances": ogHostMibCompliances,
       "ogHostMibCompliance": ogHostMibCompliance,
       "ogHostMibGroups": ogHostMibGroups,
       "ogHostMibGroup": ogHostMibGroup,
       "oghostNotificationsGroup": oghostNotificationsGroup,
       "ogHostMibObjects": ogHostMibObjects,
       "oghostEvent": oghostEvent,
       "oghostEventTable": oghostEventTable,
       "oghostEventEntry": oghostEventEntry,
       "oghostEventIndex": oghostEventIndex,
       "oghostEventUsername": oghostEventUsername,
       "oghostEventType": oghostEventType,
       "oghostEventAddress": oghostEventAddress,
       "oghostEventDescription": oghostEventDescription,
       "oghostEventProtocol": oghostEventProtocol,
       "oghostEventPort": oghostEventPort}
)
