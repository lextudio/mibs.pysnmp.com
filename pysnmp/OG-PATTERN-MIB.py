# SNMP MIB module (OG-PATTERN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OG-PATTERN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:49 2024
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

ogPatternMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12)
)
ogPatternMib.setRevisions(
        ("2013-08-11 00:00",
         "2010-03-22 11:27",
         "2008-11-27 11:40")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OgPatternMibNotificationPrefix_ObjectIdentity = ObjectIdentity
ogPatternMibNotificationPrefix = _OgPatternMibNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 2)
)
_OgpatnMibNotifications_ObjectIdentity = ObjectIdentity
ogpatnMibNotifications = _OgpatnMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 2, 0)
)
_OgPatternMibConformance_ObjectIdentity = ObjectIdentity
ogPatternMibConformance = _OgPatternMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 3)
)
_OgPatternMibCompliances_ObjectIdentity = ObjectIdentity
ogPatternMibCompliances = _OgPatternMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 3, 1)
)
_OgPatternMibGroups_ObjectIdentity = ObjectIdentity
ogPatternMibGroups = _OgPatternMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 3, 2)
)
_OgPatternMibObjects_ObjectIdentity = ObjectIdentity
ogPatternMibObjects = _OgPatternMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 10)
)
_OgpatnEvent_ObjectIdentity = ObjectIdentity
ogpatnEvent = _OgpatnEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1)
)
_OgpatnEventTable_Object = MibTable
ogpatnEventTable = _OgpatnEventTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1)
)
if mibBuilder.loadTexts:
    ogpatnEventTable.setStatus("current")
_OgpatnEventEntry_Object = MibTableRow
ogpatnEventEntry = _OgpatnEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1)
)
ogpatnEventEntry.setIndexNames(
    (0, "OG-PATTERN-MIB", "ogpatnEventIndex"),
)
if mibBuilder.loadTexts:
    ogpatnEventEntry.setStatus("current")


class _OgpatnEventIndex_Type(Integer32):
    """Custom type ogpatnEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OgpatnEventIndex_Type.__name__ = "Integer32"
_OgpatnEventIndex_Object = MibTableColumn
ogpatnEventIndex = _OgpatnEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1, 1),
    _OgpatnEventIndex_Type()
)
ogpatnEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogpatnEventIndex.setStatus("current")
_OgpatnEventDescription_Type = DisplayString
_OgpatnEventDescription_Object = MibTableColumn
ogpatnEventDescription = _OgpatnEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1, 10),
    _OgpatnEventDescription_Type()
)
ogpatnEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogpatnEventDescription.setStatus("current")
_OgpatnEventText_Type = DisplayString
_OgpatnEventText_Object = MibTableColumn
ogpatnEventText = _OgpatnEventText_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1, 11),
    _OgpatnEventText_Type()
)
ogpatnEventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogpatnEventText.setStatus("current")
_OgpatnEventPortNumber_Type = Integer32
_OgpatnEventPortNumber_Object = MibTableColumn
ogpatnEventPortNumber = _OgpatnEventPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1, 12),
    _OgpatnEventPortNumber_Type()
)
ogpatnEventPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogpatnEventPortNumber.setStatus("current")
_OgpatnEventPortLabel_Type = DisplayString
_OgpatnEventPortLabel_Object = MibTableColumn
ogpatnEventPortLabel = _OgpatnEventPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1, 13),
    _OgpatnEventPortLabel_Type()
)
ogpatnEventPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogpatnEventPortLabel.setStatus("current")

# Managed Objects groups

ogPatternMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 3, 2, 1)
)
ogPatternMibGroup.setObjects(
      *(("OG-PATTERN-MIB", "ogpatnEventDescription"),
        ("OG-PATTERN-MIB", "ogpatnEventText"),
        ("OG-PATTERN-MIB", "ogpatnEventPortNumber"),
        ("OG-PATTERN-MIB", "ogpatnEventPortLabel"))
)
if mibBuilder.loadTexts:
    ogPatternMibGroup.setStatus("current")


# Notification objects

ogpatnEventOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 2, 0, 200)
)
ogpatnEventOccurred.setObjects(
      *(("OG-PATTERN-MIB", "ogpatnEventDescription"),
        ("OG-PATTERN-MIB", "ogpatnEventText"),
        ("OG-PATTERN-MIB", "ogpatnEventPortNumber"),
        ("OG-PATTERN-MIB", "ogpatnEventPortLabel"))
)
if mibBuilder.loadTexts:
    ogpatnEventOccurred.setStatus(
        "current"
    )


# Notifications groups

ogpatnNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 3, 2, 2)
)
ogpatnNotificationsGroup.setObjects(
    ("OG-PATTERN-MIB", "ogpatnEventOccurred")
)
if mibBuilder.loadTexts:
    ogpatnNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ogPatternMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25049, 10, 12, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ogPatternMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OG-PATTERN-MIB",
    **{"ogPatternMib": ogPatternMib,
       "ogPatternMibNotificationPrefix": ogPatternMibNotificationPrefix,
       "ogpatnMibNotifications": ogpatnMibNotifications,
       "ogpatnEventOccurred": ogpatnEventOccurred,
       "ogPatternMibConformance": ogPatternMibConformance,
       "ogPatternMibCompliances": ogPatternMibCompliances,
       "ogPatternMibCompliance": ogPatternMibCompliance,
       "ogPatternMibGroups": ogPatternMibGroups,
       "ogPatternMibGroup": ogPatternMibGroup,
       "ogpatnNotificationsGroup": ogpatnNotificationsGroup,
       "ogPatternMibObjects": ogPatternMibObjects,
       "ogpatnEvent": ogpatnEvent,
       "ogpatnEventTable": ogpatnEventTable,
       "ogpatnEventEntry": ogpatnEventEntry,
       "ogpatnEventIndex": ogpatnEventIndex,
       "ogpatnEventDescription": ogpatnEventDescription,
       "ogpatnEventText": ogpatnEventText,
       "ogpatnEventPortNumber": ogpatnEventPortNumber,
       "ogpatnEventPortLabel": ogpatnEventPortLabel}
)
