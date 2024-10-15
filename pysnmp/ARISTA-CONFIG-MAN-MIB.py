# SNMP MIB module (ARISTA-CONFIG-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARISTA-CONFIG-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:19 2024
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

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

aristaConfigManMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9)
)
aristaConfigManMIB.setRevisions(
        ("2014-08-15 00:00",
         "2014-05-06 13:00",
         "2012-08-23 13:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfigHistoryEventMedium(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("commandSource", 2),
          ("erase", 1),
          ("none", 0),
          ("running", 3),
          ("session", 6),
          ("startup", 4),
          ("url", 5))
    )



# MIB Managed Objects in the order of their OIDs

_AristaConfigManMIBObjects_ObjectIdentity = ObjectIdentity
aristaConfigManMIBObjects = _AristaConfigManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 1)
)
_AristaCmdHistory_ObjectIdentity = ObjectIdentity
aristaCmdHistory = _AristaCmdHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1)
)
_AristaCmdHistoryRunningLastChanged_Type = TimeTicks
_AristaCmdHistoryRunningLastChanged_Object = MibScalar
aristaCmdHistoryRunningLastChanged = _AristaCmdHistoryRunningLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 1),
    _AristaCmdHistoryRunningLastChanged_Type()
)
aristaCmdHistoryRunningLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaCmdHistoryRunningLastChanged.setStatus("current")
_AristaCmdHistoryEventTable_Object = MibTable
aristaCmdHistoryEventTable = _AristaCmdHistoryEventTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2)
)
if mibBuilder.loadTexts:
    aristaCmdHistoryEventTable.setStatus("current")
_AristaCmdHistoryEventEntry_Object = MibTableRow
aristaCmdHistoryEventEntry = _AristaCmdHistoryEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1)
)
aristaCmdHistoryEventEntry.setIndexNames(
    (0, "ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventIndex"),
)
if mibBuilder.loadTexts:
    aristaCmdHistoryEventEntry.setStatus("current")
_AristaCmdHistoryEventIndex_Type = Unsigned32
_AristaCmdHistoryEventIndex_Object = MibTableColumn
aristaCmdHistoryEventIndex = _AristaCmdHistoryEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 1),
    _AristaCmdHistoryEventIndex_Type()
)
aristaCmdHistoryEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaCmdHistoryEventIndex.setStatus("current")
_AristaCmdHistoryEventTime_Type = TimeTicks
_AristaCmdHistoryEventTime_Object = MibTableColumn
aristaCmdHistoryEventTime = _AristaCmdHistoryEventTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 2),
    _AristaCmdHistoryEventTime_Type()
)
aristaCmdHistoryEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaCmdHistoryEventTime.setStatus("current")


class _AristaCmdHistoryEventCommandSource_Type(Integer32):
    """Custom type aristaCmdHistoryEventCommandSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("commandLine", 0),
          ("snmp", 1))
    )


_AristaCmdHistoryEventCommandSource_Type.__name__ = "Integer32"
_AristaCmdHistoryEventCommandSource_Object = MibTableColumn
aristaCmdHistoryEventCommandSource = _AristaCmdHistoryEventCommandSource_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 3),
    _AristaCmdHistoryEventCommandSource_Type()
)
aristaCmdHistoryEventCommandSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaCmdHistoryEventCommandSource.setStatus("current")
_AristaCmdHistoryEventConfigSource_Type = ConfigHistoryEventMedium
_AristaCmdHistoryEventConfigSource_Object = MibTableColumn
aristaCmdHistoryEventConfigSource = _AristaCmdHistoryEventConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 4),
    _AristaCmdHistoryEventConfigSource_Type()
)
aristaCmdHistoryEventConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaCmdHistoryEventConfigSource.setStatus("current")
_AristaCmdHistoryEventConfigDestination_Type = ConfigHistoryEventMedium
_AristaCmdHistoryEventConfigDestination_Object = MibTableColumn
aristaCmdHistoryEventConfigDestination = _AristaCmdHistoryEventConfigDestination_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 5),
    _AristaCmdHistoryEventConfigDestination_Type()
)
aristaCmdHistoryEventConfigDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaCmdHistoryEventConfigDestination.setStatus("current")


class _AristaCmdHistoryEventConfigSourceURLScheme_Type(OctetString):
    """Custom type aristaCmdHistoryEventConfigSourceURLScheme based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AristaCmdHistoryEventConfigSourceURLScheme_Type.__name__ = "OctetString"
_AristaCmdHistoryEventConfigSourceURLScheme_Object = MibTableColumn
aristaCmdHistoryEventConfigSourceURLScheme = _AristaCmdHistoryEventConfigSourceURLScheme_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 6),
    _AristaCmdHistoryEventConfigSourceURLScheme_Type()
)
aristaCmdHistoryEventConfigSourceURLScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaCmdHistoryEventConfigSourceURLScheme.setStatus("current")


class _AristaCmdHistoryEventConfigDestURLScheme_Type(OctetString):
    """Custom type aristaCmdHistoryEventConfigDestURLScheme based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AristaCmdHistoryEventConfigDestURLScheme_Type.__name__ = "OctetString"
_AristaCmdHistoryEventConfigDestURLScheme_Object = MibTableColumn
aristaCmdHistoryEventConfigDestURLScheme = _AristaCmdHistoryEventConfigDestURLScheme_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 7),
    _AristaCmdHistoryEventConfigDestURLScheme_Type()
)
aristaCmdHistoryEventConfigDestURLScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaCmdHistoryEventConfigDestURLScheme.setStatus("current")
_AristaConfigManMibConformance_ObjectIdentity = ObjectIdentity
aristaConfigManMibConformance = _AristaConfigManMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 2)
)
_AristaConfigManMibCompliances_ObjectIdentity = ObjectIdentity
aristaConfigManMibCompliances = _AristaConfigManMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 2, 1)
)
_AristaConfigManMibGroups_ObjectIdentity = ObjectIdentity
aristaConfigManMibGroups = _AristaConfigManMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 2, 1, 2)
)
_AristaConfigManMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
aristaConfigManMIBNotificationPrefix = _AristaConfigManMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 3)
)
_AristaConfigManMIBNotifications_ObjectIdentity = ObjectIdentity
aristaConfigManMIBNotifications = _AristaConfigManMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 3, 0)
)

# Managed Objects groups

aristaConfigEventDetailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 2, 1, 2, 1)
)
aristaConfigEventDetailGroup.setObjects(
      *(("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryRunningLastChanged"),
        ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventTime"),
        ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventCommandSource"),
        ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigSource"),
        ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigDestination"),
        ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigSourceURLScheme"),
        ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigDestURLScheme"))
)
if mibBuilder.loadTexts:
    aristaConfigEventDetailGroup.setStatus("current")


# Notification objects

aristaConfigManEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 3, 0, 1)
)
aristaConfigManEvent.setObjects(
      *(("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventCommandSource"),
        ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigSource"),
        ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigDestination"),
        ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigSourceURLScheme"),
        ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigDestURLScheme"))
)
if mibBuilder.loadTexts:
    aristaConfigManEvent.setStatus(
        "current"
    )


# Notifications groups

aristaConfigManMibNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 2, 1, 2, 2)
)
aristaConfigManMibNotificationsGroup.setObjects(
    ("ARISTA-CONFIG-MAN-MIB", "aristaConfigManEvent")
)
if mibBuilder.loadTexts:
    aristaConfigManMibNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aristaConfigManMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aristaConfigManMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-CONFIG-MAN-MIB",
    **{"ConfigHistoryEventMedium": ConfigHistoryEventMedium,
       "aristaConfigManMIB": aristaConfigManMIB,
       "aristaConfigManMIBObjects": aristaConfigManMIBObjects,
       "aristaCmdHistory": aristaCmdHistory,
       "aristaCmdHistoryRunningLastChanged": aristaCmdHistoryRunningLastChanged,
       "aristaCmdHistoryEventTable": aristaCmdHistoryEventTable,
       "aristaCmdHistoryEventEntry": aristaCmdHistoryEventEntry,
       "aristaCmdHistoryEventIndex": aristaCmdHistoryEventIndex,
       "aristaCmdHistoryEventTime": aristaCmdHistoryEventTime,
       "aristaCmdHistoryEventCommandSource": aristaCmdHistoryEventCommandSource,
       "aristaCmdHistoryEventConfigSource": aristaCmdHistoryEventConfigSource,
       "aristaCmdHistoryEventConfigDestination": aristaCmdHistoryEventConfigDestination,
       "aristaCmdHistoryEventConfigSourceURLScheme": aristaCmdHistoryEventConfigSourceURLScheme,
       "aristaCmdHistoryEventConfigDestURLScheme": aristaCmdHistoryEventConfigDestURLScheme,
       "aristaConfigManMibConformance": aristaConfigManMibConformance,
       "aristaConfigManMibCompliances": aristaConfigManMibCompliances,
       "aristaConfigManMibCompliance": aristaConfigManMibCompliance,
       "aristaConfigManMibGroups": aristaConfigManMibGroups,
       "aristaConfigEventDetailGroup": aristaConfigEventDetailGroup,
       "aristaConfigManMibNotificationsGroup": aristaConfigManMibNotificationsGroup,
       "aristaConfigManMIBNotificationPrefix": aristaConfigManMIBNotificationPrefix,
       "aristaConfigManMIBNotifications": aristaConfigManMIBNotifications,
       "aristaConfigManEvent": aristaConfigManEvent}
)
