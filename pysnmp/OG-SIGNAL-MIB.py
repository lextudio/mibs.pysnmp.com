# SNMP MIB module (OG-SIGNAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OG-SIGNAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:51 2024
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

ogSignalMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11)
)
ogSignalMib.setRevisions(
        ("2013-08-11 00:00",
         "2010-03-22 11:27",
         "2008-11-27 11:40")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OgSignalMibNotificationPrefix_ObjectIdentity = ObjectIdentity
ogSignalMibNotificationPrefix = _OgSignalMibNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 2)
)
_OgsgnlMibNotifications_ObjectIdentity = ObjectIdentity
ogsgnlMibNotifications = _OgsgnlMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 2, 0)
)
_OgSignalMibConformance_ObjectIdentity = ObjectIdentity
ogSignalMibConformance = _OgSignalMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 3)
)
_OgSignalMibCompliances_ObjectIdentity = ObjectIdentity
ogSignalMibCompliances = _OgSignalMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 3, 1)
)
_OgSignalMibGroups_ObjectIdentity = ObjectIdentity
ogSignalMibGroups = _OgSignalMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 3, 2)
)
_OgSignalMibObjects_ObjectIdentity = ObjectIdentity
ogSignalMibObjects = _OgSignalMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 10)
)
_OgsgnlEvent_ObjectIdentity = ObjectIdentity
ogsgnlEvent = _OgsgnlEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 10, 1)
)
_OgsgnlEventTable_Object = MibTable
ogsgnlEventTable = _OgsgnlEventTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 10, 1, 1)
)
if mibBuilder.loadTexts:
    ogsgnlEventTable.setStatus("current")
_OgsgnlEventEntry_Object = MibTableRow
ogsgnlEventEntry = _OgsgnlEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 10, 1, 1, 1)
)
ogsgnlEventEntry.setIndexNames(
    (0, "OG-SIGNAL-MIB", "ogsgnlEventIndex"),
)
if mibBuilder.loadTexts:
    ogsgnlEventEntry.setStatus("current")


class _OgsgnlEventIndex_Type(Integer32):
    """Custom type ogsgnlEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OgsgnlEventIndex_Type.__name__ = "Integer32"
_OgsgnlEventIndex_Object = MibTableColumn
ogsgnlEventIndex = _OgsgnlEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 10, 1, 1, 1, 1),
    _OgsgnlEventIndex_Type()
)
ogsgnlEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogsgnlEventIndex.setStatus("current")
_OgsgnlEventType_Type = DisplayString
_OgsgnlEventType_Object = MibTableColumn
ogsgnlEventType = _OgsgnlEventType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 10, 1, 1, 1, 10),
    _OgsgnlEventType_Type()
)
ogsgnlEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogsgnlEventType.setStatus("current")
_OgsgnlEventState_Type = DisplayString
_OgsgnlEventState_Object = MibTableColumn
ogsgnlEventState = _OgsgnlEventState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 10, 1, 1, 1, 11),
    _OgsgnlEventState_Type()
)
ogsgnlEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogsgnlEventState.setStatus("current")
_OgsgnlEventPortNumber_Type = Integer32
_OgsgnlEventPortNumber_Object = MibTableColumn
ogsgnlEventPortNumber = _OgsgnlEventPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 10, 1, 1, 1, 12),
    _OgsgnlEventPortNumber_Type()
)
ogsgnlEventPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogsgnlEventPortNumber.setStatus("current")
_OgsgnlEventPortLabel_Type = DisplayString
_OgsgnlEventPortLabel_Object = MibTableColumn
ogsgnlEventPortLabel = _OgsgnlEventPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 10, 1, 1, 1, 13),
    _OgsgnlEventPortLabel_Type()
)
ogsgnlEventPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogsgnlEventPortLabel.setStatus("current")

# Managed Objects groups

ogSignalMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 3, 2, 1)
)
ogSignalMibGroup.setObjects(
      *(("OG-SIGNAL-MIB", "ogsgnlEventType"),
        ("OG-SIGNAL-MIB", "ogsgnlEventState"),
        ("OG-SIGNAL-MIB", "ogsgnlEventPortNumber"),
        ("OG-SIGNAL-MIB", "ogsgnlEventPortLabel"))
)
if mibBuilder.loadTexts:
    ogSignalMibGroup.setStatus("current")


# Notification objects

ogsgnlEventOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 2, 0, 200)
)
ogsgnlEventOccurred.setObjects(
      *(("OG-SIGNAL-MIB", "ogsgnlEventType"),
        ("OG-SIGNAL-MIB", "ogsgnlEventState"),
        ("OG-SIGNAL-MIB", "ogsgnlEventPortNumber"),
        ("OG-SIGNAL-MIB", "ogsgnlEventPortLabel"))
)
if mibBuilder.loadTexts:
    ogsgnlEventOccurred.setStatus(
        "current"
    )


# Notifications groups

ogsgnlNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 3, 2, 2)
)
ogsgnlNotificationsGroup.setObjects(
    ("OG-SIGNAL-MIB", "ogsgnlEventOccurred")
)
if mibBuilder.loadTexts:
    ogsgnlNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ogSignalMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25049, 10, 11, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ogSignalMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OG-SIGNAL-MIB",
    **{"ogSignalMib": ogSignalMib,
       "ogSignalMibNotificationPrefix": ogSignalMibNotificationPrefix,
       "ogsgnlMibNotifications": ogsgnlMibNotifications,
       "ogsgnlEventOccurred": ogsgnlEventOccurred,
       "ogSignalMibConformance": ogSignalMibConformance,
       "ogSignalMibCompliances": ogSignalMibCompliances,
       "ogSignalMibCompliance": ogSignalMibCompliance,
       "ogSignalMibGroups": ogSignalMibGroups,
       "ogSignalMibGroup": ogSignalMibGroup,
       "ogsgnlNotificationsGroup": ogsgnlNotificationsGroup,
       "ogSignalMibObjects": ogSignalMibObjects,
       "ogsgnlEvent": ogsgnlEvent,
       "ogsgnlEventTable": ogsgnlEventTable,
       "ogsgnlEventEntry": ogsgnlEventEntry,
       "ogsgnlEventIndex": ogsgnlEventIndex,
       "ogsgnlEventType": ogsgnlEventType,
       "ogsgnlEventState": ogsgnlEventState,
       "ogsgnlEventPortNumber": ogsgnlEventPortNumber,
       "ogsgnlEventPortLabel": ogsgnlEventPortLabel}
)
