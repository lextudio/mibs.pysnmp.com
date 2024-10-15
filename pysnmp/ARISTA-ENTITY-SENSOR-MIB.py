# SNMP MIB module (ARISTA-ENTITY-SENSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARISTA-ENTITY-SENSOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:20 2024
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

(entPhysicalDescr,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalDescr",
    "entPhysicalIndex")

(EntitySensorValue,
 entPhySensorValue) = mibBuilder.importSymbols(
    "ENTITY-SENSOR-MIB",
    "EntitySensorValue",
    "entPhySensorValue")

(entStateAlarm,) = mibBuilder.importSymbols(
    "ENTITY-STATE-MIB",
    "entStateAlarm")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

aristaEntSensorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 12)
)
aristaEntSensorMIB.setRevisions(
        ("2014-08-15 00:00",
         "2013-05-09 09:50")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaEntSensorMibNotifications_ObjectIdentity = ObjectIdentity
aristaEntSensorMibNotifications = _AristaEntSensorMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 12, 0)
)
_AristaEntSensorMibObjects_ObjectIdentity = ObjectIdentity
aristaEntSensorMibObjects = _AristaEntSensorMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 12, 1)
)
_AristaEntSensorThresholdTable_Object = MibTable
aristaEntSensorThresholdTable = _AristaEntSensorThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 12, 1, 1)
)
if mibBuilder.loadTexts:
    aristaEntSensorThresholdTable.setStatus("current")
_AristaEntSensorThresholdEntry_Object = MibTableRow
aristaEntSensorThresholdEntry = _AristaEntSensorThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 12, 1, 1, 1)
)
aristaEntSensorThresholdEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    aristaEntSensorThresholdEntry.setStatus("current")
_AristaEntSensorThresholdLowWarning_Type = EntitySensorValue
_AristaEntSensorThresholdLowWarning_Object = MibTableColumn
aristaEntSensorThresholdLowWarning = _AristaEntSensorThresholdLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 12, 1, 1, 1, 1),
    _AristaEntSensorThresholdLowWarning_Type()
)
aristaEntSensorThresholdLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaEntSensorThresholdLowWarning.setStatus("current")
_AristaEntSensorThresholdLowCritical_Type = EntitySensorValue
_AristaEntSensorThresholdLowCritical_Object = MibTableColumn
aristaEntSensorThresholdLowCritical = _AristaEntSensorThresholdLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 12, 1, 1, 1, 2),
    _AristaEntSensorThresholdLowCritical_Type()
)
aristaEntSensorThresholdLowCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaEntSensorThresholdLowCritical.setStatus("current")
_AristaEntSensorThresholdHighWarning_Type = EntitySensorValue
_AristaEntSensorThresholdHighWarning_Object = MibTableColumn
aristaEntSensorThresholdHighWarning = _AristaEntSensorThresholdHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 12, 1, 1, 1, 3),
    _AristaEntSensorThresholdHighWarning_Type()
)
aristaEntSensorThresholdHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaEntSensorThresholdHighWarning.setStatus("current")
_AristaEntSensorThresholdHighCritical_Type = EntitySensorValue
_AristaEntSensorThresholdHighCritical_Object = MibTableColumn
aristaEntSensorThresholdHighCritical = _AristaEntSensorThresholdHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 12, 1, 1, 1, 4),
    _AristaEntSensorThresholdHighCritical_Type()
)
aristaEntSensorThresholdHighCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaEntSensorThresholdHighCritical.setStatus("current")
_AristaEntSensorStatusDescr_Type = SnmpAdminString
_AristaEntSensorStatusDescr_Object = MibTableColumn
aristaEntSensorStatusDescr = _AristaEntSensorStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 12, 1, 1, 1, 5),
    _AristaEntSensorStatusDescr_Type()
)
aristaEntSensorStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaEntSensorStatusDescr.setStatus("current")
_AristaEntSensorMibConformance_ObjectIdentity = ObjectIdentity
aristaEntSensorMibConformance = _AristaEntSensorMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 12, 2)
)
_AristaEntSensorMibCompliances_ObjectIdentity = ObjectIdentity
aristaEntSensorMibCompliances = _AristaEntSensorMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 12, 2, 1)
)
_AristaEntSensorMibGroups_ObjectIdentity = ObjectIdentity
aristaEntSensorMibGroups = _AristaEntSensorMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 12, 2, 2)
)

# Managed Objects groups

aristaEntSensorThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 12, 2, 2, 1)
)
aristaEntSensorThresholdGroup.setObjects(
      *(("ARISTA-ENTITY-SENSOR-MIB", "aristaEntSensorThresholdLowWarning"),
        ("ARISTA-ENTITY-SENSOR-MIB", "aristaEntSensorThresholdLowCritical"),
        ("ARISTA-ENTITY-SENSOR-MIB", "aristaEntSensorThresholdHighWarning"),
        ("ARISTA-ENTITY-SENSOR-MIB", "aristaEntSensorThresholdHighCritical"),
        ("ARISTA-ENTITY-SENSOR-MIB", "aristaEntSensorStatusDescr"))
)
if mibBuilder.loadTexts:
    aristaEntSensorThresholdGroup.setStatus("current")


# Notification objects

aristaEntSensorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 3, 12, 0, 1)
)
aristaEntSensorAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("ENTITY-STATE-MIB", "entStateAlarm"))
)
if mibBuilder.loadTexts:
    aristaEntSensorAlarm.setStatus(
        "current"
    )


# Notifications groups

aristaEntSensorNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 12, 2, 2, 2)
)
aristaEntSensorNotificationsGroup.setObjects(
    ("ARISTA-ENTITY-SENSOR-MIB", "aristaEntSensorAlarm")
)
if mibBuilder.loadTexts:
    aristaEntSensorNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aristaEntSensorMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 12, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aristaEntSensorMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-ENTITY-SENSOR-MIB",
    **{"aristaEntSensorMIB": aristaEntSensorMIB,
       "aristaEntSensorMibNotifications": aristaEntSensorMibNotifications,
       "aristaEntSensorAlarm": aristaEntSensorAlarm,
       "aristaEntSensorMibObjects": aristaEntSensorMibObjects,
       "aristaEntSensorThresholdTable": aristaEntSensorThresholdTable,
       "aristaEntSensorThresholdEntry": aristaEntSensorThresholdEntry,
       "aristaEntSensorThresholdLowWarning": aristaEntSensorThresholdLowWarning,
       "aristaEntSensorThresholdLowCritical": aristaEntSensorThresholdLowCritical,
       "aristaEntSensorThresholdHighWarning": aristaEntSensorThresholdHighWarning,
       "aristaEntSensorThresholdHighCritical": aristaEntSensorThresholdHighCritical,
       "aristaEntSensorStatusDescr": aristaEntSensorStatusDescr,
       "aristaEntSensorMibConformance": aristaEntSensorMibConformance,
       "aristaEntSensorMibCompliances": aristaEntSensorMibCompliances,
       "aristaEntSensorMibCompliance": aristaEntSensorMibCompliance,
       "aristaEntSensorMibGroups": aristaEntSensorMibGroups,
       "aristaEntSensorThresholdGroup": aristaEntSensorThresholdGroup,
       "aristaEntSensorNotificationsGroup": aristaEntSensorNotificationsGroup}
)
