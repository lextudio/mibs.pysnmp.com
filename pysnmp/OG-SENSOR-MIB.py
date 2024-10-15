# SNMP MIB module (OG-SENSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OG-SENSOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:50 2024
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

ogSensorMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13)
)
ogSensorMib.setRevisions(
        ("2013-08-11 00:00",
         "2010-03-22 11:27",
         "2008-11-27 11:40")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OgSensorMibNotificationPrefix_ObjectIdentity = ObjectIdentity
ogSensorMibNotificationPrefix = _OgSensorMibNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 2)
)
_OgsensMibNotifications_ObjectIdentity = ObjectIdentity
ogsensMibNotifications = _OgsensMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 2, 0)
)
_OgSensorMibConformance_ObjectIdentity = ObjectIdentity
ogSensorMibConformance = _OgSensorMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 3)
)
_OgSensorMibCompliances_ObjectIdentity = ObjectIdentity
ogSensorMibCompliances = _OgSensorMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 1)
)
_OgSensorMibGroups_ObjectIdentity = ObjectIdentity
ogSensorMibGroups = _OgSensorMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 2)
)
_OgSensorMibObjects_ObjectIdentity = ObjectIdentity
ogSensorMibObjects = _OgSensorMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 10)
)
_OgsensStatus_ObjectIdentity = ObjectIdentity
ogsensStatus = _OgsensStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1)
)
_OgsensStatusTable_Object = MibTable
ogsensStatusTable = _OgsensStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3)
)
if mibBuilder.loadTexts:
    ogsensStatusTable.setStatus("current")
_OgsensStatusEntry_Object = MibTableRow
ogsensStatusEntry = _OgsensStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1)
)
ogsensStatusEntry.setIndexNames(
    (0, "OG-SENSOR-MIB", "ogsensStatusIndex"),
)
if mibBuilder.loadTexts:
    ogsensStatusEntry.setStatus("current")


class _OgsensStatusIndex_Type(Integer32):
    """Custom type ogsensStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OgsensStatusIndex_Type.__name__ = "Integer32"
_OgsensStatusIndex_Object = MibTableColumn
ogsensStatusIndex = _OgsensStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 1),
    _OgsensStatusIndex_Type()
)
ogsensStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogsensStatusIndex.setStatus("current")
_OgsensStatusName_Type = DisplayString
_OgsensStatusName_Object = MibTableColumn
ogsensStatusName = _OgsensStatusName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 10),
    _OgsensStatusName_Type()
)
ogsensStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogsensStatusName.setStatus("current")
_OgsensStatusDevType_Type = DisplayString
_OgsensStatusDevType_Object = MibTableColumn
ogsensStatusDevType = _OgsensStatusDevType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 11),
    _OgsensStatusDevType_Type()
)
ogsensStatusDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogsensStatusDevType.setStatus("current")
_OgsensStatusType_Type = DisplayString
_OgsensStatusType_Object = MibTableColumn
ogsensStatusType = _OgsensStatusType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 12),
    _OgsensStatusType_Type()
)
ogsensStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogsensStatusType.setStatus("current")
_OgsensStatusValue_Type = Integer32
_OgsensStatusValue_Object = MibTableColumn
ogsensStatusValue = _OgsensStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 13),
    _OgsensStatusValue_Type()
)
ogsensStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogsensStatusValue.setStatus("current")

# Managed Objects groups

ogSensorMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 2, 1)
)
ogSensorMibGroup.setObjects(
      *(("OG-SENSOR-MIB", "ogsensStatusName"),
        ("OG-SENSOR-MIB", "ogsensStatusDevType"),
        ("OG-SENSOR-MIB", "ogsensStatusType"),
        ("OG-SENSOR-MIB", "ogsensStatusValue"))
)
if mibBuilder.loadTexts:
    ogSensorMibGroup.setStatus("current")


# Notification objects

ogsensEventOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 2, 0, 200)
)
ogsensEventOccurred.setObjects(
      *(("OG-SENSOR-MIB", "ogsensStatusName"),
        ("OG-SENSOR-MIB", "ogsensStatusDevType"),
        ("OG-SENSOR-MIB", "ogsensStatusType"),
        ("OG-SENSOR-MIB", "ogsensStatusValue"))
)
if mibBuilder.loadTexts:
    ogsensEventOccurred.setStatus(
        "current"
    )


# Notifications groups

ogsensNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 2, 2)
)
ogsensNotificationsGroup.setObjects(
    ("OG-SENSOR-MIB", "ogsensEventOccurred")
)
if mibBuilder.loadTexts:
    ogsensNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ogSensorMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ogSensorMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OG-SENSOR-MIB",
    **{"ogSensorMib": ogSensorMib,
       "ogSensorMibNotificationPrefix": ogSensorMibNotificationPrefix,
       "ogsensMibNotifications": ogsensMibNotifications,
       "ogsensEventOccurred": ogsensEventOccurred,
       "ogSensorMibConformance": ogSensorMibConformance,
       "ogSensorMibCompliances": ogSensorMibCompliances,
       "ogSensorMibCompliance": ogSensorMibCompliance,
       "ogSensorMibGroups": ogSensorMibGroups,
       "ogSensorMibGroup": ogSensorMibGroup,
       "ogsensNotificationsGroup": ogsensNotificationsGroup,
       "ogSensorMibObjects": ogSensorMibObjects,
       "ogsensStatus": ogsensStatus,
       "ogsensStatusTable": ogsensStatusTable,
       "ogsensStatusEntry": ogsensStatusEntry,
       "ogsensStatusIndex": ogsensStatusIndex,
       "ogsensStatusName": ogsensStatusName,
       "ogsensStatusDevType": ogsensStatusDevType,
       "ogsensStatusType": ogsensStatusType,
       "ogsensStatusValue": ogsensStatusValue}
)
