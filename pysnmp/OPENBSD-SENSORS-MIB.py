# SNMP MIB module (OPENBSD-SENSORS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPENBSD-SENSORS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:20 2024
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

(openBSD,) = mibBuilder.importSymbols(
    "OPENBSD-BASE-MIB",
    "openBSD")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

sensorsMIBObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 2)
)
sensorsMIBObjects.setRevisions(
        ("2012-09-20 00:00",
         "2012-01-31 00:00",
         "2008-12-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1)
)
_SensorNumber_Type = Integer32
_SensorNumber_Object = MibScalar
sensorNumber = _SensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 1),
    _SensorNumber_Type()
)
sensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorNumber.setStatus("current")
_SensorTable_Object = MibTable
sensorTable = _SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2)
)
if mibBuilder.loadTexts:
    sensorTable.setStatus("current")
_SensorEntry_Object = MibTableRow
sensorEntry = _SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1)
)
sensorEntry.setIndexNames(
    (0, "OPENBSD-SENSORS-MIB", "sensorIndex"),
)
if mibBuilder.loadTexts:
    sensorEntry.setStatus("current")


class _SensorIndex_Type(Integer32):
    """Custom type sensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SensorIndex_Type.__name__ = "Integer32"
_SensorIndex_Object = MibTableColumn
sensorIndex = _SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 1),
    _SensorIndex_Type()
)
sensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorIndex.setStatus("current")
_SensorDescr_Type = OctetString
_SensorDescr_Object = MibTableColumn
sensorDescr = _SensorDescr_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 2),
    _SensorDescr_Type()
)
sensorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorDescr.setStatus("current")


class _SensorType_Type(Integer32):
    """Custom type sensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("accel", 20),
          ("amphour", 8),
          ("angle", 17),
          ("current", 6),
          ("distance", 18),
          ("drive", 13),
          ("fan", 1),
          ("freq", 16),
          ("humidity", 15),
          ("illuminance", 12),
          ("indicator", 9),
          ("percent", 11),
          ("power", 5),
          ("pressure", 19),
          ("raw", 10),
          ("resistance", 4),
          ("temperature", 0),
          ("timedelta", 14),
          ("voltsac", 3),
          ("voltsdc", 2),
          ("watthour", 7))
    )


_SensorType_Type.__name__ = "Integer32"
_SensorType_Object = MibTableColumn
sensorType = _SensorType_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 3),
    _SensorType_Type()
)
sensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorType.setStatus("current")
_SensorDevice_Type = OctetString
_SensorDevice_Object = MibTableColumn
sensorDevice = _SensorDevice_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 4),
    _SensorDevice_Type()
)
sensorDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorDevice.setStatus("current")
_SensorValue_Type = OctetString
_SensorValue_Object = MibTableColumn
sensorValue = _SensorValue_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 5),
    _SensorValue_Type()
)
sensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorValue.setStatus("current")
_SensorUnits_Type = OctetString
_SensorUnits_Object = MibTableColumn
sensorUnits = _SensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 6),
    _SensorUnits_Type()
)
sensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorUnits.setStatus("current")


class _SensorStatus_Type(Integer32):
    """Custom type sensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("ok", 1),
          ("unknown", 4),
          ("unspecified", 0),
          ("warn", 2))
    )


_SensorStatus_Type.__name__ = "Integer32"
_SensorStatus_Object = MibTableColumn
sensorStatus = _SensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 7),
    _SensorStatus_Type()
)
sensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPENBSD-SENSORS-MIB",
    **{"sensorsMIBObjects": sensorsMIBObjects,
       "sensors": sensors,
       "sensorNumber": sensorNumber,
       "sensorTable": sensorTable,
       "sensorEntry": sensorEntry,
       "sensorIndex": sensorIndex,
       "sensorDescr": sensorDescr,
       "sensorType": sensorType,
       "sensorDevice": sensorDevice,
       "sensorValue": sensorValue,
       "sensorUnits": sensorUnits,
       "sensorStatus": sensorStatus}
)
