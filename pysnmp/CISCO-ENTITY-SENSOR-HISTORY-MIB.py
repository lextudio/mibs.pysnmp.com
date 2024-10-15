# SNMP MIB module (CISCO-ENTITY-SENSOR-HISTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-SENSOR-HISTORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:44 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(EntitySensorValue,) = mibBuilder.importSymbols(
    "ENTITY-SENSOR-MIB",
    "EntitySensorValue")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoEntitySensorHistoryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 768)
)
ciscoEntitySensorHistoryMIB.setRevisions(
        ("2011-03-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SensorHistoryCollectionAlgorithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("algoSMA", 4),
          ("measured", 3),
          ("other", 1),
          ("unknown", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoEntitySensorHistoryMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEntitySensorHistoryMIBObjects = _CiscoEntitySensorHistoryMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 0)
)
_CeshCollectionTable_Object = MibTable
ceshCollectionTable = _CeshCollectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1)
)
if mibBuilder.loadTexts:
    ceshCollectionTable.setStatus("current")
_CeshCollectionEntry_Object = MibTableRow
ceshCollectionEntry = _CeshCollectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1)
)
ceshCollectionEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervalTime"),
)
if mibBuilder.loadTexts:
    ceshCollectionEntry.setStatus("current")


class _CeshCollectionIntervalTime_Type(Unsigned32):
    """Custom type ceshCollectionIntervalTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CeshCollectionIntervalTime_Type.__name__ = "Unsigned32"
_CeshCollectionIntervalTime_Object = MibTableColumn
ceshCollectionIntervalTime = _CeshCollectionIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 1),
    _CeshCollectionIntervalTime_Type()
)
ceshCollectionIntervalTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceshCollectionIntervalTime.setStatus("current")
if mibBuilder.loadTexts:
    ceshCollectionIntervalTime.setUnits("seconds")
_CeshCollectionIntervals_Type = Gauge32
_CeshCollectionIntervals_Object = MibTableColumn
ceshCollectionIntervals = _CeshCollectionIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 2),
    _CeshCollectionIntervals_Type()
)
ceshCollectionIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceshCollectionIntervals.setStatus("current")
if mibBuilder.loadTexts:
    ceshCollectionIntervals.setUnits("intervals")
_CeshCollectionInvalidIntervals_Type = Gauge32
_CeshCollectionInvalidIntervals_Object = MibTableColumn
ceshCollectionInvalidIntervals = _CeshCollectionInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 3),
    _CeshCollectionInvalidIntervals_Type()
)
ceshCollectionInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceshCollectionInvalidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    ceshCollectionInvalidIntervals.setUnits("intervals")


class _CeshCollectionMaxIntervals_Type(Unsigned32):
    """Custom type ceshCollectionMaxIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CeshCollectionMaxIntervals_Type.__name__ = "Unsigned32"
_CeshCollectionMaxIntervals_Object = MibTableColumn
ceshCollectionMaxIntervals = _CeshCollectionMaxIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 4),
    _CeshCollectionMaxIntervals_Type()
)
ceshCollectionMaxIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceshCollectionMaxIntervals.setStatus("current")
if mibBuilder.loadTexts:
    ceshCollectionMaxIntervals.setUnits("intervals")
_CeshCollectionElapsedTime_Type = Gauge32
_CeshCollectionElapsedTime_Object = MibTableColumn
ceshCollectionElapsedTime = _CeshCollectionElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 5),
    _CeshCollectionElapsedTime_Type()
)
ceshCollectionElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceshCollectionElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    ceshCollectionElapsedTime.setUnits("seconds")
_CeshCollectionAlgorithm_Type = SensorHistoryCollectionAlgorithm
_CeshCollectionAlgorithm_Object = MibTableColumn
ceshCollectionAlgorithm = _CeshCollectionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 6),
    _CeshCollectionAlgorithm_Type()
)
ceshCollectionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceshCollectionAlgorithm.setStatus("current")
_CeshCollectionIntervalTable_Object = MibTable
ceshCollectionIntervalTable = _CeshCollectionIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 2)
)
if mibBuilder.loadTexts:
    ceshCollectionIntervalTable.setStatus("current")
_CeshCollectionIntervalEntry_Object = MibTableRow
ceshCollectionIntervalEntry = _CeshCollectionIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 2, 1)
)
ceshCollectionIntervalEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervalTime"),
    (0, "CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervalNumber"),
)
if mibBuilder.loadTexts:
    ceshCollectionIntervalEntry.setStatus("current")


class _CeshCollectionIntervalNumber_Type(Unsigned32):
    """Custom type ceshCollectionIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CeshCollectionIntervalNumber_Type.__name__ = "Unsigned32"
_CeshCollectionIntervalNumber_Object = MibTableColumn
ceshCollectionIntervalNumber = _CeshCollectionIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 2, 1, 1),
    _CeshCollectionIntervalNumber_Type()
)
ceshCollectionIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceshCollectionIntervalNumber.setStatus("current")
_CeshCollectionIntervalSensorValue_Type = EntitySensorValue
_CeshCollectionIntervalSensorValue_Object = MibTableColumn
ceshCollectionIntervalSensorValue = _CeshCollectionIntervalSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 2, 1, 2),
    _CeshCollectionIntervalSensorValue_Type()
)
ceshCollectionIntervalSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceshCollectionIntervalSensorValue.setStatus("current")
_CeshCollectionIntervalTimeStamp_Type = TimeStamp
_CeshCollectionIntervalTimeStamp_Object = MibTableColumn
ceshCollectionIntervalTimeStamp = _CeshCollectionIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 2, 1, 3),
    _CeshCollectionIntervalTimeStamp_Type()
)
ceshCollectionIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceshCollectionIntervalTimeStamp.setStatus("current")
_CiscoEntitySensorHistoryMIBConform_ObjectIdentity = ObjectIdentity
ciscoEntitySensorHistoryMIBConform = _CiscoEntitySensorHistoryMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 1)
)
_CiscoEntitySensorHistoryMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEntitySensorHistoryMIBCompliances = _CiscoEntitySensorHistoryMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 1, 1)
)
_CiscoEntitySensorHistoryMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEntitySensorHistoryMIBGroups = _CiscoEntitySensorHistoryMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 1, 2)
)

# Managed Objects groups

ceshCollectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 1, 2, 1)
)
ceshCollectionGroup.setObjects(
      *(("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionElapsedTime"),
        ("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervals"),
        ("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionInvalidIntervals"),
        ("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionAlgorithm"),
        ("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionMaxIntervals"))
)
if mibBuilder.loadTexts:
    ceshCollectionGroup.setStatus("current")

ceshCollectionIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 1, 2, 2)
)
ceshCollectionIntervalGroup.setObjects(
      *(("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervalTimeStamp"),
        ("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervalSensorValue"))
)
if mibBuilder.loadTexts:
    ceshCollectionIntervalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoEntitySensorHistoryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 768, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoEntitySensorHistoryCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-SENSOR-HISTORY-MIB",
    **{"SensorHistoryCollectionAlgorithm": SensorHistoryCollectionAlgorithm,
       "ciscoEntitySensorHistoryMIB": ciscoEntitySensorHistoryMIB,
       "ciscoEntitySensorHistoryMIBObjects": ciscoEntitySensorHistoryMIBObjects,
       "ceshCollectionTable": ceshCollectionTable,
       "ceshCollectionEntry": ceshCollectionEntry,
       "ceshCollectionIntervalTime": ceshCollectionIntervalTime,
       "ceshCollectionIntervals": ceshCollectionIntervals,
       "ceshCollectionInvalidIntervals": ceshCollectionInvalidIntervals,
       "ceshCollectionMaxIntervals": ceshCollectionMaxIntervals,
       "ceshCollectionElapsedTime": ceshCollectionElapsedTime,
       "ceshCollectionAlgorithm": ceshCollectionAlgorithm,
       "ceshCollectionIntervalTable": ceshCollectionIntervalTable,
       "ceshCollectionIntervalEntry": ceshCollectionIntervalEntry,
       "ceshCollectionIntervalNumber": ceshCollectionIntervalNumber,
       "ceshCollectionIntervalSensorValue": ceshCollectionIntervalSensorValue,
       "ceshCollectionIntervalTimeStamp": ceshCollectionIntervalTimeStamp,
       "ciscoEntitySensorHistoryMIBConform": ciscoEntitySensorHistoryMIBConform,
       "ciscoEntitySensorHistoryMIBCompliances": ciscoEntitySensorHistoryMIBCompliances,
       "ciscoEntitySensorHistoryCompliance": ciscoEntitySensorHistoryCompliance,
       "ciscoEntitySensorHistoryMIBGroups": ciscoEntitySensorHistoryMIBGroups,
       "ceshCollectionGroup": ceshCollectionGroup,
       "ceshCollectionIntervalGroup": ceshCollectionIntervalGroup}
)
