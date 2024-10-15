# SNMP MIB module (PDN-ENTITY-SENSOR-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-ENTITY-SENSOR-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:38 2024
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

(EntitySensorValue,
 entPhySensorEntry,
 entPhySensorValue) = mibBuilder.importSymbols(
    "ENTITY-SENSOR-MIB",
    "EntitySensorValue",
    "entPhySensorEntry",
    "entPhySensorValue")

(pdn_common,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-common")

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

pdnEntitySensorExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45)
)
pdnEntitySensorExtMIB.setRevisions(
        ("2003-06-06 00:00",
         "2003-04-24 00:00",
         "2003-04-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnEntitySensorExtNotifications_ObjectIdentity = ObjectIdentity
pdnEntitySensorExtNotifications = _PdnEntitySensorExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 0)
)
_PdnEntitySensorExtObjects_ObjectIdentity = ObjectIdentity
pdnEntitySensorExtObjects = _PdnEntitySensorExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 1)
)
_PdnEntPhySensorExtTable_Object = MibTable
pdnEntPhySensorExtTable = _PdnEntPhySensorExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 1, 1)
)
if mibBuilder.loadTexts:
    pdnEntPhySensorExtTable.setStatus("current")
_PdnEntPhySensorExtEntry_Object = MibTableRow
pdnEntPhySensorExtEntry = _PdnEntPhySensorExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pdnEntPhySensorExtEntry.setStatus("current")


class _PdnEntPhySensorExtNotificationEnable_Type(Bits):
    """Custom type pdnEntPhySensorExtNotificationEnable based on Bits"""
    namedValues = NamedValues(
        ("thresholdExceeded", 0)
    )

_PdnEntPhySensorExtNotificationEnable_Type.__name__ = "Bits"
_PdnEntPhySensorExtNotificationEnable_Object = MibTableColumn
pdnEntPhySensorExtNotificationEnable = _PdnEntPhySensorExtNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 1, 1, 1, 1),
    _PdnEntPhySensorExtNotificationEnable_Type()
)
pdnEntPhySensorExtNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnEntPhySensorExtNotificationEnable.setStatus("current")
_PdnEntPhySensorExtUpperThreshold_Type = EntitySensorValue
_PdnEntPhySensorExtUpperThreshold_Object = MibTableColumn
pdnEntPhySensorExtUpperThreshold = _PdnEntPhySensorExtUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 1, 1, 1, 2),
    _PdnEntPhySensorExtUpperThreshold_Type()
)
pdnEntPhySensorExtUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnEntPhySensorExtUpperThreshold.setStatus("current")
_PdnEntPhySensorExtLowerThreshold_Type = EntitySensorValue
_PdnEntPhySensorExtLowerThreshold_Object = MibTableColumn
pdnEntPhySensorExtLowerThreshold = _PdnEntPhySensorExtLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 1, 1, 1, 3),
    _PdnEntPhySensorExtLowerThreshold_Type()
)
pdnEntPhySensorExtLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnEntPhySensorExtLowerThreshold.setStatus("current")


class _PdnEntPhySensorExtThresholdState_Type(Integer32):
    """Custom type pdnEntPhySensorExtThresholdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lowerThresholdExceeded", 3),
          ("noThresholdsExceeded", 1),
          ("upperThresholdExceeded", 2))
    )


_PdnEntPhySensorExtThresholdState_Type.__name__ = "Integer32"
_PdnEntPhySensorExtThresholdState_Object = MibTableColumn
pdnEntPhySensorExtThresholdState = _PdnEntPhySensorExtThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 1, 1, 1, 4),
    _PdnEntPhySensorExtThresholdState_Type()
)
pdnEntPhySensorExtThresholdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnEntPhySensorExtThresholdState.setStatus("current")
_PdnEntitySensorExtAFNs_ObjectIdentity = ObjectIdentity
pdnEntitySensorExtAFNs = _PdnEntitySensorExtAFNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 2)
)
_PdnEntitySensorExtConformance_ObjectIdentity = ObjectIdentity
pdnEntitySensorExtConformance = _PdnEntitySensorExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3)
)
_PdnEntitySensorExtCompliances_ObjectIdentity = ObjectIdentity
pdnEntitySensorExtCompliances = _PdnEntitySensorExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3, 1)
)
_PdnEntitySensorExtGroups_ObjectIdentity = ObjectIdentity
pdnEntitySensorExtGroups = _PdnEntitySensorExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3, 2)
)
_PdnEntitySensorExtObjGroups_ObjectIdentity = ObjectIdentity
pdnEntitySensorExtObjGroups = _PdnEntitySensorExtObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3, 2, 1)
)
_PdnEntitySensorExtAfnGroups_ObjectIdentity = ObjectIdentity
pdnEntitySensorExtAfnGroups = _PdnEntitySensorExtAfnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3, 2, 2)
)
_PdnEntitySensorExtNtfyGroups_ObjectIdentity = ObjectIdentity
pdnEntitySensorExtNtfyGroups = _PdnEntitySensorExtNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3, 2, 3)
)
entPhySensorEntry.registerAugmentions(
    ("PDN-ENTITY-SENSOR-EXT-MIB",
     "pdnEntPhySensorExtEntry")
)
pdnEntPhySensorExtEntry.setIndexNames(*entPhySensorEntry.getIndexNames())

# Managed Objects groups

pdnEntitySensorExtThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3, 2, 1, 1)
)
pdnEntitySensorExtThresholdGroup.setObjects(
      *(("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntPhySensorExtNotificationEnable"),
        ("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntPhySensorExtUpperThreshold"),
        ("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntPhySensorExtLowerThreshold"),
        ("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntPhySensorExtThresholdState"))
)
if mibBuilder.loadTexts:
    pdnEntitySensorExtThresholdGroup.setStatus("current")


# Notification objects

pdnEntPhySensorExtThresholdExceededSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 0, 1)
)
pdnEntPhySensorExtThresholdExceededSet.setObjects(
      *(("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntPhySensorExtThresholdState"))
)
if mibBuilder.loadTexts:
    pdnEntPhySensorExtThresholdExceededSet.setStatus(
        "current"
    )

pdnEntPhySensorExtThresholdExceededCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 0, 100)
)
pdnEntPhySensorExtThresholdExceededCleared.setObjects(
      *(("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntPhySensorExtThresholdState"))
)
if mibBuilder.loadTexts:
    pdnEntPhySensorExtThresholdExceededCleared.setStatus(
        "current"
    )


# Notifications groups

pdnEntitySensorExtThresholdNtfyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3, 2, 3, 1)
)
pdnEntitySensorExtThresholdNtfyGroup.setObjects(
      *(("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntPhySensorExtThresholdExceededSet"),
        ("PDN-ENTITY-SENSOR-EXT-MIB", "pdnEntPhySensorExtThresholdExceededCleared"))
)
if mibBuilder.loadTexts:
    pdnEntitySensorExtThresholdNtfyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pdnEntitySensorExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pdnEntitySensorExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-ENTITY-SENSOR-EXT-MIB",
    **{"pdnEntitySensorExtMIB": pdnEntitySensorExtMIB,
       "pdnEntitySensorExtNotifications": pdnEntitySensorExtNotifications,
       "pdnEntPhySensorExtThresholdExceededSet": pdnEntPhySensorExtThresholdExceededSet,
       "pdnEntPhySensorExtThresholdExceededCleared": pdnEntPhySensorExtThresholdExceededCleared,
       "pdnEntitySensorExtObjects": pdnEntitySensorExtObjects,
       "pdnEntPhySensorExtTable": pdnEntPhySensorExtTable,
       "pdnEntPhySensorExtEntry": pdnEntPhySensorExtEntry,
       "pdnEntPhySensorExtNotificationEnable": pdnEntPhySensorExtNotificationEnable,
       "pdnEntPhySensorExtUpperThreshold": pdnEntPhySensorExtUpperThreshold,
       "pdnEntPhySensorExtLowerThreshold": pdnEntPhySensorExtLowerThreshold,
       "pdnEntPhySensorExtThresholdState": pdnEntPhySensorExtThresholdState,
       "pdnEntitySensorExtAFNs": pdnEntitySensorExtAFNs,
       "pdnEntitySensorExtConformance": pdnEntitySensorExtConformance,
       "pdnEntitySensorExtCompliances": pdnEntitySensorExtCompliances,
       "pdnEntitySensorExtMIBCompliance": pdnEntitySensorExtMIBCompliance,
       "pdnEntitySensorExtGroups": pdnEntitySensorExtGroups,
       "pdnEntitySensorExtObjGroups": pdnEntitySensorExtObjGroups,
       "pdnEntitySensorExtThresholdGroup": pdnEntitySensorExtThresholdGroup,
       "pdnEntitySensorExtAfnGroups": pdnEntitySensorExtAfnGroups,
       "pdnEntitySensorExtNtfyGroups": pdnEntitySensorExtNtfyGroups,
       "pdnEntitySensorExtThresholdNtfyGroup": pdnEntitySensorExtThresholdNtfyGroup}
)
