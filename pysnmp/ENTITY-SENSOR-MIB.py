# SNMP MIB module (ENTITY-SENSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTITY-SENSOR-MIB
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

(entPhysicalIndex,
 entityPhysicalGroup) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entityPhysicalGroup")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

entitySensorMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 99)
)
entitySensorMIB.setRevisions(
        ("2002-12-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EntitySensorDataType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("amperes", 5),
          ("celsius", 8),
          ("cmm", 11),
          ("hertz", 7),
          ("other", 1),
          ("percentRH", 9),
          ("rpm", 10),
          ("truthvalue", 12),
          ("unknown", 2),
          ("voltsAC", 3),
          ("voltsDC", 4),
          ("watts", 6))
    )



class EntitySensorDataScale(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("atto", 3),
          ("exa", 14),
          ("femto", 4),
          ("giga", 12),
          ("kilo", 10),
          ("mega", 11),
          ("micro", 7),
          ("milli", 8),
          ("nano", 6),
          ("peta", 15),
          ("pico", 5),
          ("tera", 13),
          ("units", 9),
          ("yocto", 1),
          ("yotta", 17),
          ("zepto", 2),
          ("zetta", 16))
    )



class EntitySensorPrecision(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-8, 9),
    )



class EntitySensorValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )



class EntitySensorStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonoperational", 3),
          ("ok", 1),
          ("unavailable", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EntitySensorObjects_ObjectIdentity = ObjectIdentity
entitySensorObjects = _EntitySensorObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 99, 1)
)
_EntPhySensorTable_Object = MibTable
entPhySensorTable = _EntPhySensorTable_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1)
)
if mibBuilder.loadTexts:
    entPhySensorTable.setStatus("current")
_EntPhySensorEntry_Object = MibTableRow
entPhySensorEntry = _EntPhySensorEntry_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1)
)
entPhySensorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    entPhySensorEntry.setStatus("current")
_EntPhySensorType_Type = EntitySensorDataType
_EntPhySensorType_Object = MibTableColumn
entPhySensorType = _EntPhySensorType_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 1),
    _EntPhySensorType_Type()
)
entPhySensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorType.setStatus("current")
_EntPhySensorScale_Type = EntitySensorDataScale
_EntPhySensorScale_Object = MibTableColumn
entPhySensorScale = _EntPhySensorScale_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 2),
    _EntPhySensorScale_Type()
)
entPhySensorScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorScale.setStatus("current")
_EntPhySensorPrecision_Type = EntitySensorPrecision
_EntPhySensorPrecision_Object = MibTableColumn
entPhySensorPrecision = _EntPhySensorPrecision_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 3),
    _EntPhySensorPrecision_Type()
)
entPhySensorPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorPrecision.setStatus("current")
_EntPhySensorValue_Type = EntitySensorValue
_EntPhySensorValue_Object = MibTableColumn
entPhySensorValue = _EntPhySensorValue_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 4),
    _EntPhySensorValue_Type()
)
entPhySensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorValue.setStatus("current")
_EntPhySensorOperStatus_Type = EntitySensorStatus
_EntPhySensorOperStatus_Object = MibTableColumn
entPhySensorOperStatus = _EntPhySensorOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 5),
    _EntPhySensorOperStatus_Type()
)
entPhySensorOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorOperStatus.setStatus("current")
_EntPhySensorUnitsDisplay_Type = SnmpAdminString
_EntPhySensorUnitsDisplay_Object = MibTableColumn
entPhySensorUnitsDisplay = _EntPhySensorUnitsDisplay_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 6),
    _EntPhySensorUnitsDisplay_Type()
)
entPhySensorUnitsDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorUnitsDisplay.setStatus("current")
_EntPhySensorValueTimeStamp_Type = TimeStamp
_EntPhySensorValueTimeStamp_Object = MibTableColumn
entPhySensorValueTimeStamp = _EntPhySensorValueTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 7),
    _EntPhySensorValueTimeStamp_Type()
)
entPhySensorValueTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorValueTimeStamp.setStatus("current")
_EntPhySensorValueUpdateRate_Type = Unsigned32
_EntPhySensorValueUpdateRate_Object = MibTableColumn
entPhySensorValueUpdateRate = _EntPhySensorValueUpdateRate_Object(
    (1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 8),
    _EntPhySensorValueUpdateRate_Type()
)
entPhySensorValueUpdateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorValueUpdateRate.setStatus("current")
if mibBuilder.loadTexts:
    entPhySensorValueUpdateRate.setUnits("milliseconds")
_EntitySensorConformance_ObjectIdentity = ObjectIdentity
entitySensorConformance = _EntitySensorConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 99, 3)
)
_EntitySensorCompliances_ObjectIdentity = ObjectIdentity
entitySensorCompliances = _EntitySensorCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 99, 3, 1)
)
_EntitySensorGroups_ObjectIdentity = ObjectIdentity
entitySensorGroups = _EntitySensorGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 99, 3, 2)
)

# Managed Objects groups

entitySensorValueGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 99, 3, 2, 1)
)
entitySensorValueGroup.setObjects(
      *(("ENTITY-SENSOR-MIB", "entPhySensorType"),
        ("ENTITY-SENSOR-MIB", "entPhySensorScale"),
        ("ENTITY-SENSOR-MIB", "entPhySensorPrecision"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("ENTITY-SENSOR-MIB", "entPhySensorOperStatus"),
        ("ENTITY-SENSOR-MIB", "entPhySensorUnitsDisplay"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValueTimeStamp"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValueUpdateRate"))
)
if mibBuilder.loadTexts:
    entitySensorValueGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

entitySensorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 99, 3, 1, 1)
)
if mibBuilder.loadTexts:
    entitySensorCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTITY-SENSOR-MIB",
    **{"EntitySensorDataType": EntitySensorDataType,
       "EntitySensorDataScale": EntitySensorDataScale,
       "EntitySensorPrecision": EntitySensorPrecision,
       "EntitySensorValue": EntitySensorValue,
       "EntitySensorStatus": EntitySensorStatus,
       "entitySensorMIB": entitySensorMIB,
       "entitySensorObjects": entitySensorObjects,
       "entPhySensorTable": entPhySensorTable,
       "entPhySensorEntry": entPhySensorEntry,
       "entPhySensorType": entPhySensorType,
       "entPhySensorScale": entPhySensorScale,
       "entPhySensorPrecision": entPhySensorPrecision,
       "entPhySensorValue": entPhySensorValue,
       "entPhySensorOperStatus": entPhySensorOperStatus,
       "entPhySensorUnitsDisplay": entPhySensorUnitsDisplay,
       "entPhySensorValueTimeStamp": entPhySensorValueTimeStamp,
       "entPhySensorValueUpdateRate": entPhySensorValueUpdateRate,
       "entitySensorConformance": entitySensorConformance,
       "entitySensorCompliances": entitySensorCompliances,
       "entitySensorCompliance": entitySensorCompliance,
       "entitySensorGroups": entitySensorGroups,
       "entitySensorValueGroup": entitySensorValueGroup}
)
