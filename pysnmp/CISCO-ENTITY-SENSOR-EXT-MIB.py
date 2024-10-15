# SNMP MIB module (CISCO-ENTITY-SENSOR-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-SENSOR-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:43 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalDescr,
 entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalDescr",
    "entPhysicalIndex",
    "entPhysicalName")

(EntitySensorValue,
 entPhySensorType,
 entPhySensorValue) = mibBuilder.importSymbols(
    "ENTITY-SENSOR-MIB",
    "EntitySensorValue",
    "entPhySensorType",
    "entPhySensorValue")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoEntitySensorExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 745)
)
ciscoEntitySensorExtMIB.setRevisions(
        ("2010-06-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoSensorThresholdSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("critical", 30),
          ("major", 20),
          ("minor", 10),
          ("other", 1))
    )



class CiscoSensorThresholdRelation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("equalTo", 5),
          ("greaterOrEqual", 4),
          ("greaterThan", 3),
          ("lessOrEqual", 2),
          ("lessThan", 1),
          ("notEqualTo", 6))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoEntitySensorExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoEntitySensorExtMIBNotifs = _CiscoEntitySensorExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 0)
)
_CiscoEntitySensorExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEntitySensorExtMIBObjects = _CiscoEntitySensorExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 1)
)
_CeSensorExtThresholdTable_Object = MibTable
ceSensorExtThresholdTable = _CeSensorExtThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1)
)
if mibBuilder.loadTexts:
    ceSensorExtThresholdTable.setStatus("current")
_CeSensorExtThresholdEntry_Object = MibTableRow
ceSensorExtThresholdEntry = _CeSensorExtThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1)
)
ceSensorExtThresholdEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdIndex"),
)
if mibBuilder.loadTexts:
    ceSensorExtThresholdEntry.setStatus("current")


class _CeSensorExtThresholdIndex_Type(Unsigned32):
    """Custom type ceSensorExtThresholdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CeSensorExtThresholdIndex_Type.__name__ = "Unsigned32"
_CeSensorExtThresholdIndex_Object = MibTableColumn
ceSensorExtThresholdIndex = _CeSensorExtThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 1),
    _CeSensorExtThresholdIndex_Type()
)
ceSensorExtThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceSensorExtThresholdIndex.setStatus("current")
_CeSensorExtThresholdSeverity_Type = CiscoSensorThresholdSeverity
_CeSensorExtThresholdSeverity_Object = MibTableColumn
ceSensorExtThresholdSeverity = _CeSensorExtThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 2),
    _CeSensorExtThresholdSeverity_Type()
)
ceSensorExtThresholdSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceSensorExtThresholdSeverity.setStatus("current")
_CeSensorExtThresholdRelation_Type = CiscoSensorThresholdRelation
_CeSensorExtThresholdRelation_Object = MibTableColumn
ceSensorExtThresholdRelation = _CeSensorExtThresholdRelation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 3),
    _CeSensorExtThresholdRelation_Type()
)
ceSensorExtThresholdRelation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceSensorExtThresholdRelation.setStatus("current")
_CeSensorExtThresholdValue_Type = EntitySensorValue
_CeSensorExtThresholdValue_Object = MibTableColumn
ceSensorExtThresholdValue = _CeSensorExtThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 4),
    _CeSensorExtThresholdValue_Type()
)
ceSensorExtThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceSensorExtThresholdValue.setStatus("current")
_CeSensorExtThresholdEvaluation_Type = TruthValue
_CeSensorExtThresholdEvaluation_Object = MibTableColumn
ceSensorExtThresholdEvaluation = _CeSensorExtThresholdEvaluation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 5),
    _CeSensorExtThresholdEvaluation_Type()
)
ceSensorExtThresholdEvaluation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceSensorExtThresholdEvaluation.setStatus("current")


class _CeSensorExtThresholdNotifEnable_Type(Integer32):
    """Custom type ceSensorExtThresholdNotifEnable based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("transparent", 3))
    )


_CeSensorExtThresholdNotifEnable_Type.__name__ = "Integer32"
_CeSensorExtThresholdNotifEnable_Object = MibTableColumn
ceSensorExtThresholdNotifEnable = _CeSensorExtThresholdNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 6),
    _CeSensorExtThresholdNotifEnable_Type()
)
ceSensorExtThresholdNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceSensorExtThresholdNotifEnable.setStatus("current")
_CiscoEntSensorExtGlobalObjects_ObjectIdentity = ObjectIdentity
ciscoEntSensorExtGlobalObjects = _CiscoEntSensorExtGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 2)
)


class _CeSensorExtThresholdNotifGlobalEnable_Type(Integer32):
    """Custom type ceSensorExtThresholdNotifGlobalEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CeSensorExtThresholdNotifGlobalEnable_Type.__name__ = "Integer32"
_CeSensorExtThresholdNotifGlobalEnable_Object = MibScalar
ceSensorExtThresholdNotifGlobalEnable = _CeSensorExtThresholdNotifGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 2, 1),
    _CeSensorExtThresholdNotifGlobalEnable_Type()
)
ceSensorExtThresholdNotifGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceSensorExtThresholdNotifGlobalEnable.setStatus("current")
_CiscoEntitySensorExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoEntitySensorExtMIBConform = _CiscoEntitySensorExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 2)
)
_CiscoEntSensorExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEntSensorExtMIBCompliances = _CiscoEntSensorExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 1)
)
_CiscoEntSensorExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEntSensorExtMIBGroups = _CiscoEntSensorExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2)
)

# Managed Objects groups

ciscoEntSensorExtThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2, 1)
)
ciscoEntSensorExtThresholdGroup.setObjects(
      *(("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdSeverity"),
        ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdRelation"),
        ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdValue"),
        ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdEvaluation"),
        ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdNotifEnable"))
)
if mibBuilder.loadTexts:
    ciscoEntSensorExtThresholdGroup.setStatus("current")

ciscoEntSensorExtNotificationCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2, 3)
)
ciscoEntSensorExtNotificationCtrlGroup.setObjects(
    ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdNotifGlobalEnable")
)
if mibBuilder.loadTexts:
    ciscoEntSensorExtNotificationCtrlGroup.setStatus("current")


# Notification objects

ceSensorExtThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 0, 1)
)
ceSensorExtThresholdNotification.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("ENTITY-SENSOR-MIB", "entPhySensorType"),
        ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdValue"))
)
if mibBuilder.loadTexts:
    ceSensorExtThresholdNotification.setStatus(
        "current"
    )


# Notifications groups

ciscoEntSensorExtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2, 2)
)
ciscoEntSensorExtNotificationGroup.setObjects(
    ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdNotification")
)
if mibBuilder.loadTexts:
    ciscoEntSensorExtNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoEntSensorExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoEntSensorExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-SENSOR-EXT-MIB",
    **{"CiscoSensorThresholdSeverity": CiscoSensorThresholdSeverity,
       "CiscoSensorThresholdRelation": CiscoSensorThresholdRelation,
       "ciscoEntitySensorExtMIB": ciscoEntitySensorExtMIB,
       "ciscoEntitySensorExtMIBNotifs": ciscoEntitySensorExtMIBNotifs,
       "ceSensorExtThresholdNotification": ceSensorExtThresholdNotification,
       "ciscoEntitySensorExtMIBObjects": ciscoEntitySensorExtMIBObjects,
       "ceSensorExtThresholdTable": ceSensorExtThresholdTable,
       "ceSensorExtThresholdEntry": ceSensorExtThresholdEntry,
       "ceSensorExtThresholdIndex": ceSensorExtThresholdIndex,
       "ceSensorExtThresholdSeverity": ceSensorExtThresholdSeverity,
       "ceSensorExtThresholdRelation": ceSensorExtThresholdRelation,
       "ceSensorExtThresholdValue": ceSensorExtThresholdValue,
       "ceSensorExtThresholdEvaluation": ceSensorExtThresholdEvaluation,
       "ceSensorExtThresholdNotifEnable": ceSensorExtThresholdNotifEnable,
       "ciscoEntSensorExtGlobalObjects": ciscoEntSensorExtGlobalObjects,
       "ceSensorExtThresholdNotifGlobalEnable": ceSensorExtThresholdNotifGlobalEnable,
       "ciscoEntitySensorExtMIBConform": ciscoEntitySensorExtMIBConform,
       "ciscoEntSensorExtMIBCompliances": ciscoEntSensorExtMIBCompliances,
       "ciscoEntSensorExtMIBCompliance": ciscoEntSensorExtMIBCompliance,
       "ciscoEntSensorExtMIBGroups": ciscoEntSensorExtMIBGroups,
       "ciscoEntSensorExtThresholdGroup": ciscoEntSensorExtThresholdGroup,
       "ciscoEntSensorExtNotificationGroup": ciscoEntSensorExtNotificationGroup,
       "ciscoEntSensorExtNotificationCtrlGroup": ciscoEntSensorExtNotificationCtrlGroup}
)
