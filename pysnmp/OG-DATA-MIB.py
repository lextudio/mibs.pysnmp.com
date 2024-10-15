# SNMP MIB module (OG-DATA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OG-DATA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:47 2024
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

ogDataMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17)
)
ogDataMib.setRevisions(
        ("2013-08-11 00:00",
         "2011-01-30 21:10")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OgDataMibNotificationPrefix_ObjectIdentity = ObjectIdentity
ogDataMibNotificationPrefix = _OgDataMibNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 2)
)
_OgdataMibNotifications_ObjectIdentity = ObjectIdentity
ogdataMibNotifications = _OgdataMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 2, 0)
)
_OgDataMibConformance_ObjectIdentity = ObjectIdentity
ogDataMibConformance = _OgDataMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 3)
)
_OgDataMibCompliances_ObjectIdentity = ObjectIdentity
ogDataMibCompliances = _OgDataMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 3, 1)
)
_OgDataMibGroups_ObjectIdentity = ObjectIdentity
ogDataMibGroups = _OgDataMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 3, 2)
)
_OgDataMibObjects_ObjectIdentity = ObjectIdentity
ogDataMibObjects = _OgDataMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 10)
)
_OgdataEvent_ObjectIdentity = ObjectIdentity
ogdataEvent = _OgdataEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 10, 1)
)
_OgdataEventTable_Object = MibTable
ogdataEventTable = _OgdataEventTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 10, 1, 1)
)
if mibBuilder.loadTexts:
    ogdataEventTable.setStatus("current")
_OgdataEventEntry_Object = MibTableRow
ogdataEventEntry = _OgdataEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 10, 1, 1, 1)
)
ogdataEventEntry.setIndexNames(
    (0, "OG-DATA-MIB", "ogdataEventIndex"),
)
if mibBuilder.loadTexts:
    ogdataEventEntry.setStatus("current")


class _OgdataEventIndex_Type(Integer32):
    """Custom type ogdataEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OgdataEventIndex_Type.__name__ = "Integer32"
_OgdataEventIndex_Object = MibTableColumn
ogdataEventIndex = _OgdataEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 10, 1, 1, 1, 1),
    _OgdataEventIndex_Type()
)
ogdataEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogdataEventIndex.setStatus("current")
_OgdataEventBytes_Type = Integer32
_OgdataEventBytes_Object = MibTableColumn
ogdataEventBytes = _OgdataEventBytes_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 10, 1, 1, 1, 10),
    _OgdataEventBytes_Type()
)
ogdataEventBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogdataEventBytes.setStatus("current")
_OgdataEventSeconds_Type = Integer32
_OgdataEventSeconds_Object = MibTableColumn
ogdataEventSeconds = _OgdataEventSeconds_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 10, 1, 1, 1, 11),
    _OgdataEventSeconds_Type()
)
ogdataEventSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogdataEventSeconds.setStatus("current")
_OgdataEventDevice_Type = DisplayString
_OgdataEventDevice_Object = MibTableColumn
ogdataEventDevice = _OgdataEventDevice_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 10, 1, 1, 1, 12),
    _OgdataEventDevice_Type()
)
ogdataEventDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogdataEventDevice.setStatus("current")


class _OgdataEventState_Type(Integer32):
    """Custom type ogdataEventState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OgdataEventState_Type.__name__ = "Integer32"
_OgdataEventState_Object = MibTableColumn
ogdataEventState = _OgdataEventState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 10, 1, 1, 1, 13),
    _OgdataEventState_Type()
)
ogdataEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogdataEventState.setStatus("current")

# Managed Objects groups

ogDataMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 3, 2, 1)
)
ogDataMibGroup.setObjects(
      *(("OG-DATA-MIB", "ogdataEventBytes"),
        ("OG-DATA-MIB", "ogdataEventSeconds"),
        ("OG-DATA-MIB", "ogdataEventDevice"),
        ("OG-DATA-MIB", "ogdataEventState"))
)
if mibBuilder.loadTexts:
    ogDataMibGroup.setStatus("current")


# Notification objects

ogdataEventOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 2, 0, 200)
)
ogdataEventOccurred.setObjects(
      *(("OG-DATA-MIB", "ogdataEventBytes"),
        ("OG-DATA-MIB", "ogdataEventSeconds"),
        ("OG-DATA-MIB", "ogdataEventDevice"),
        ("OG-DATA-MIB", "ogdataEventState"))
)
if mibBuilder.loadTexts:
    ogdataEventOccurred.setStatus(
        "current"
    )


# Notifications groups

ogdataNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 3, 2, 2)
)
ogdataNotificationsGroup.setObjects(
    ("OG-DATA-MIB", "ogdataEventOccurred")
)
if mibBuilder.loadTexts:
    ogdataNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ogDataMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25049, 10, 17, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ogDataMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OG-DATA-MIB",
    **{"ogDataMib": ogDataMib,
       "ogDataMibNotificationPrefix": ogDataMibNotificationPrefix,
       "ogdataMibNotifications": ogdataMibNotifications,
       "ogdataEventOccurred": ogdataEventOccurred,
       "ogDataMibConformance": ogDataMibConformance,
       "ogDataMibCompliances": ogDataMibCompliances,
       "ogDataMibCompliance": ogDataMibCompliance,
       "ogDataMibGroups": ogDataMibGroups,
       "ogDataMibGroup": ogDataMibGroup,
       "ogdataNotificationsGroup": ogdataNotificationsGroup,
       "ogDataMibObjects": ogDataMibObjects,
       "ogdataEvent": ogdataEvent,
       "ogdataEventTable": ogdataEventTable,
       "ogdataEventEntry": ogdataEventEntry,
       "ogdataEventIndex": ogdataEventIndex,
       "ogdataEventBytes": ogdataEventBytes,
       "ogdataEventSeconds": ogdataEventSeconds,
       "ogdataEventDevice": ogdataEventDevice,
       "ogdataEventState": ogdataEventState}
)
