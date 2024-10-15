# SNMP MIB module (LM-SENSORS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LM-SENSORS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:13 2024
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

(ucdExperimental,) = mibBuilder.importSymbols(
    "UCD-SNMP-MIB",
    "ucdExperimental")


# MODULE-IDENTITY

lmSensorsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 1)
)
lmSensorsMIB.setRevisions(
        ("2000-11-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LmSensors_ObjectIdentity = ObjectIdentity
lmSensors = _LmSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16)
)
_LmTempSensorsTable_Object = MibTable
lmTempSensorsTable = _LmTempSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 2)
)
if mibBuilder.loadTexts:
    lmTempSensorsTable.setStatus("current")
_LmTempSensorsEntry_Object = MibTableRow
lmTempSensorsEntry = _LmTempSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 2, 1)
)
lmTempSensorsEntry.setIndexNames(
    (0, "LM-SENSORS-MIB", "lmTempSensorsIndex"),
)
if mibBuilder.loadTexts:
    lmTempSensorsEntry.setStatus("current")


class _LmTempSensorsIndex_Type(Integer32):
    """Custom type lmTempSensorsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LmTempSensorsIndex_Type.__name__ = "Integer32"
_LmTempSensorsIndex_Object = MibTableColumn
lmTempSensorsIndex = _LmTempSensorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 2, 1, 1),
    _LmTempSensorsIndex_Type()
)
lmTempSensorsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmTempSensorsIndex.setStatus("current")
_LmTempSensorsDevice_Type = DisplayString
_LmTempSensorsDevice_Object = MibTableColumn
lmTempSensorsDevice = _LmTempSensorsDevice_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 2, 1, 2),
    _LmTempSensorsDevice_Type()
)
lmTempSensorsDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmTempSensorsDevice.setStatus("current")
_LmTempSensorsValue_Type = Gauge32
_LmTempSensorsValue_Object = MibTableColumn
lmTempSensorsValue = _LmTempSensorsValue_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 2, 1, 3),
    _LmTempSensorsValue_Type()
)
lmTempSensorsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmTempSensorsValue.setStatus("current")
_LmFanSensorsTable_Object = MibTable
lmFanSensorsTable = _LmFanSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 3)
)
if mibBuilder.loadTexts:
    lmFanSensorsTable.setStatus("current")
_LmFanSensorsEntry_Object = MibTableRow
lmFanSensorsEntry = _LmFanSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 3, 1)
)
lmFanSensorsEntry.setIndexNames(
    (0, "LM-SENSORS-MIB", "lmFanSensorsIndex"),
)
if mibBuilder.loadTexts:
    lmFanSensorsEntry.setStatus("current")


class _LmFanSensorsIndex_Type(Integer32):
    """Custom type lmFanSensorsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LmFanSensorsIndex_Type.__name__ = "Integer32"
_LmFanSensorsIndex_Object = MibTableColumn
lmFanSensorsIndex = _LmFanSensorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 3, 1, 1),
    _LmFanSensorsIndex_Type()
)
lmFanSensorsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmFanSensorsIndex.setStatus("current")
_LmFanSensorsDevice_Type = DisplayString
_LmFanSensorsDevice_Object = MibTableColumn
lmFanSensorsDevice = _LmFanSensorsDevice_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 3, 1, 2),
    _LmFanSensorsDevice_Type()
)
lmFanSensorsDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmFanSensorsDevice.setStatus("current")
_LmFanSensorsValue_Type = Gauge32
_LmFanSensorsValue_Object = MibTableColumn
lmFanSensorsValue = _LmFanSensorsValue_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 3, 1, 3),
    _LmFanSensorsValue_Type()
)
lmFanSensorsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmFanSensorsValue.setStatus("current")
_LmVoltSensorsTable_Object = MibTable
lmVoltSensorsTable = _LmVoltSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 4)
)
if mibBuilder.loadTexts:
    lmVoltSensorsTable.setStatus("current")
_LmVoltSensorsEntry_Object = MibTableRow
lmVoltSensorsEntry = _LmVoltSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 4, 1)
)
lmVoltSensorsEntry.setIndexNames(
    (0, "LM-SENSORS-MIB", "lmVoltSensorsIndex"),
)
if mibBuilder.loadTexts:
    lmVoltSensorsEntry.setStatus("current")


class _LmVoltSensorsIndex_Type(Integer32):
    """Custom type lmVoltSensorsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LmVoltSensorsIndex_Type.__name__ = "Integer32"
_LmVoltSensorsIndex_Object = MibTableColumn
lmVoltSensorsIndex = _LmVoltSensorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 4, 1, 1),
    _LmVoltSensorsIndex_Type()
)
lmVoltSensorsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmVoltSensorsIndex.setStatus("current")
_LmVoltSensorsDevice_Type = DisplayString
_LmVoltSensorsDevice_Object = MibTableColumn
lmVoltSensorsDevice = _LmVoltSensorsDevice_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 4, 1, 2),
    _LmVoltSensorsDevice_Type()
)
lmVoltSensorsDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmVoltSensorsDevice.setStatus("current")
_LmVoltSensorsValue_Type = Gauge32
_LmVoltSensorsValue_Object = MibTableColumn
lmVoltSensorsValue = _LmVoltSensorsValue_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 4, 1, 3),
    _LmVoltSensorsValue_Type()
)
lmVoltSensorsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmVoltSensorsValue.setStatus("current")
_LmMiscSensorsTable_Object = MibTable
lmMiscSensorsTable = _LmMiscSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 5)
)
if mibBuilder.loadTexts:
    lmMiscSensorsTable.setStatus("current")
_LmMiscSensorsEntry_Object = MibTableRow
lmMiscSensorsEntry = _LmMiscSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 5, 1)
)
lmMiscSensorsEntry.setIndexNames(
    (0, "LM-SENSORS-MIB", "lmMiscSensorsIndex"),
)
if mibBuilder.loadTexts:
    lmMiscSensorsEntry.setStatus("current")


class _LmMiscSensorsIndex_Type(Integer32):
    """Custom type lmMiscSensorsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LmMiscSensorsIndex_Type.__name__ = "Integer32"
_LmMiscSensorsIndex_Object = MibTableColumn
lmMiscSensorsIndex = _LmMiscSensorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 5, 1, 1),
    _LmMiscSensorsIndex_Type()
)
lmMiscSensorsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmMiscSensorsIndex.setStatus("current")
_LmMiscSensorsDevice_Type = DisplayString
_LmMiscSensorsDevice_Object = MibTableColumn
lmMiscSensorsDevice = _LmMiscSensorsDevice_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 5, 1, 2),
    _LmMiscSensorsDevice_Type()
)
lmMiscSensorsDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmMiscSensorsDevice.setStatus("current")
_LmMiscSensorsValue_Type = Gauge32
_LmMiscSensorsValue_Object = MibTableColumn
lmMiscSensorsValue = _LmMiscSensorsValue_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 16, 5, 1, 3),
    _LmMiscSensorsValue_Type()
)
lmMiscSensorsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmMiscSensorsValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LM-SENSORS-MIB",
    **{"lmSensors": lmSensors,
       "lmSensorsMIB": lmSensorsMIB,
       "lmTempSensorsTable": lmTempSensorsTable,
       "lmTempSensorsEntry": lmTempSensorsEntry,
       "lmTempSensorsIndex": lmTempSensorsIndex,
       "lmTempSensorsDevice": lmTempSensorsDevice,
       "lmTempSensorsValue": lmTempSensorsValue,
       "lmFanSensorsTable": lmFanSensorsTable,
       "lmFanSensorsEntry": lmFanSensorsEntry,
       "lmFanSensorsIndex": lmFanSensorsIndex,
       "lmFanSensorsDevice": lmFanSensorsDevice,
       "lmFanSensorsValue": lmFanSensorsValue,
       "lmVoltSensorsTable": lmVoltSensorsTable,
       "lmVoltSensorsEntry": lmVoltSensorsEntry,
       "lmVoltSensorsIndex": lmVoltSensorsIndex,
       "lmVoltSensorsDevice": lmVoltSensorsDevice,
       "lmVoltSensorsValue": lmVoltSensorsValue,
       "lmMiscSensorsTable": lmMiscSensorsTable,
       "lmMiscSensorsEntry": lmMiscSensorsEntry,
       "lmMiscSensorsIndex": lmMiscSensorsIndex,
       "lmMiscSensorsDevice": lmMiscSensorsDevice,
       "lmMiscSensorsValue": lmMiscSensorsValue}
)
