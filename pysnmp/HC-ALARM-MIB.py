# SNMP MIB module (HC-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HC-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:02 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(OwnerString,
 rmon,
 rmonEventGroup) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString",
    "rmon",
    "rmonEventGroup")

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
 RowStatus,
 StorageType,
 TextualConvention,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "VariablePointer")


# MODULE-IDENTITY

hcAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 16, 29)
)
hcAlarmMIB.setRevisions(
        ("2002-12-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HcValueStatus(Integer32, TextualConvention):
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
        *(("valueNegative", 3),
          ("valueNotAvailable", 1),
          ("valuePositive", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HcAlarmObjects_ObjectIdentity = ObjectIdentity
hcAlarmObjects = _HcAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 29, 1)
)
_HcAlarmControlObjects_ObjectIdentity = ObjectIdentity
hcAlarmControlObjects = _HcAlarmControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1)
)
_HcAlarmTable_Object = MibTable
hcAlarmTable = _HcAlarmTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hcAlarmTable.setStatus("current")
_HcAlarmEntry_Object = MibTableRow
hcAlarmEntry = _HcAlarmEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1)
)
hcAlarmEntry.setIndexNames(
    (0, "HC-ALARM-MIB", "hcAlarmIndex"),
)
if mibBuilder.loadTexts:
    hcAlarmEntry.setStatus("current")


class _HcAlarmIndex_Type(Integer32):
    """Custom type hcAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HcAlarmIndex_Type.__name__ = "Integer32"
_HcAlarmIndex_Object = MibTableColumn
hcAlarmIndex = _HcAlarmIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 1),
    _HcAlarmIndex_Type()
)
hcAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hcAlarmIndex.setStatus("current")


class _HcAlarmInterval_Type(Integer32):
    """Custom type hcAlarmInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HcAlarmInterval_Type.__name__ = "Integer32"
_HcAlarmInterval_Object = MibTableColumn
hcAlarmInterval = _HcAlarmInterval_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 2),
    _HcAlarmInterval_Type()
)
hcAlarmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcAlarmInterval.setStatus("current")
if mibBuilder.loadTexts:
    hcAlarmInterval.setUnits("seconds")
_HcAlarmVariable_Type = VariablePointer
_HcAlarmVariable_Object = MibTableColumn
hcAlarmVariable = _HcAlarmVariable_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 3),
    _HcAlarmVariable_Type()
)
hcAlarmVariable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcAlarmVariable.setStatus("current")


class _HcAlarmSampleType_Type(Integer32):
    """Custom type hcAlarmSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_HcAlarmSampleType_Type.__name__ = "Integer32"
_HcAlarmSampleType_Object = MibTableColumn
hcAlarmSampleType = _HcAlarmSampleType_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 4),
    _HcAlarmSampleType_Type()
)
hcAlarmSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcAlarmSampleType.setStatus("current")
_HcAlarmAbsValue_Type = CounterBasedGauge64
_HcAlarmAbsValue_Object = MibTableColumn
hcAlarmAbsValue = _HcAlarmAbsValue_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 5),
    _HcAlarmAbsValue_Type()
)
hcAlarmAbsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcAlarmAbsValue.setStatus("current")
_HcAlarmValueStatus_Type = HcValueStatus
_HcAlarmValueStatus_Object = MibTableColumn
hcAlarmValueStatus = _HcAlarmValueStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 6),
    _HcAlarmValueStatus_Type()
)
hcAlarmValueStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcAlarmValueStatus.setStatus("current")


class _HcAlarmStartupAlarm_Type(Integer32):
    """Custom type hcAlarmStartupAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fallingAlarm", 2),
          ("risingAlarm", 1),
          ("risingOrFallingAlarm", 3))
    )


_HcAlarmStartupAlarm_Type.__name__ = "Integer32"
_HcAlarmStartupAlarm_Object = MibTableColumn
hcAlarmStartupAlarm = _HcAlarmStartupAlarm_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 7),
    _HcAlarmStartupAlarm_Type()
)
hcAlarmStartupAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcAlarmStartupAlarm.setStatus("current")
_HcAlarmRisingThreshAbsValueLo_Type = Unsigned32
_HcAlarmRisingThreshAbsValueLo_Object = MibTableColumn
hcAlarmRisingThreshAbsValueLo = _HcAlarmRisingThreshAbsValueLo_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 8),
    _HcAlarmRisingThreshAbsValueLo_Type()
)
hcAlarmRisingThreshAbsValueLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcAlarmRisingThreshAbsValueLo.setStatus("current")
_HcAlarmRisingThreshAbsValueHi_Type = Unsigned32
_HcAlarmRisingThreshAbsValueHi_Object = MibTableColumn
hcAlarmRisingThreshAbsValueHi = _HcAlarmRisingThreshAbsValueHi_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 9),
    _HcAlarmRisingThreshAbsValueHi_Type()
)
hcAlarmRisingThreshAbsValueHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcAlarmRisingThreshAbsValueHi.setStatus("current")
_HcAlarmRisingThresholdValStatus_Type = HcValueStatus
_HcAlarmRisingThresholdValStatus_Object = MibTableColumn
hcAlarmRisingThresholdValStatus = _HcAlarmRisingThresholdValStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 10),
    _HcAlarmRisingThresholdValStatus_Type()
)
hcAlarmRisingThresholdValStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcAlarmRisingThresholdValStatus.setStatus("current")
_HcAlarmFallingThreshAbsValueLo_Type = Unsigned32
_HcAlarmFallingThreshAbsValueLo_Object = MibTableColumn
hcAlarmFallingThreshAbsValueLo = _HcAlarmFallingThreshAbsValueLo_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 11),
    _HcAlarmFallingThreshAbsValueLo_Type()
)
hcAlarmFallingThreshAbsValueLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcAlarmFallingThreshAbsValueLo.setStatus("current")
_HcAlarmFallingThreshAbsValueHi_Type = Unsigned32
_HcAlarmFallingThreshAbsValueHi_Object = MibTableColumn
hcAlarmFallingThreshAbsValueHi = _HcAlarmFallingThreshAbsValueHi_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 12),
    _HcAlarmFallingThreshAbsValueHi_Type()
)
hcAlarmFallingThreshAbsValueHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcAlarmFallingThreshAbsValueHi.setStatus("current")
_HcAlarmFallingThresholdValStatus_Type = HcValueStatus
_HcAlarmFallingThresholdValStatus_Object = MibTableColumn
hcAlarmFallingThresholdValStatus = _HcAlarmFallingThresholdValStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 13),
    _HcAlarmFallingThresholdValStatus_Type()
)
hcAlarmFallingThresholdValStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcAlarmFallingThresholdValStatus.setStatus("current")


class _HcAlarmRisingEventIndex_Type(Integer32):
    """Custom type hcAlarmRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HcAlarmRisingEventIndex_Type.__name__ = "Integer32"
_HcAlarmRisingEventIndex_Object = MibTableColumn
hcAlarmRisingEventIndex = _HcAlarmRisingEventIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 14),
    _HcAlarmRisingEventIndex_Type()
)
hcAlarmRisingEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcAlarmRisingEventIndex.setStatus("current")


class _HcAlarmFallingEventIndex_Type(Integer32):
    """Custom type hcAlarmFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HcAlarmFallingEventIndex_Type.__name__ = "Integer32"
_HcAlarmFallingEventIndex_Object = MibTableColumn
hcAlarmFallingEventIndex = _HcAlarmFallingEventIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 15),
    _HcAlarmFallingEventIndex_Type()
)
hcAlarmFallingEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcAlarmFallingEventIndex.setStatus("current")
_HcAlarmValueFailedAttempts_Type = Counter32
_HcAlarmValueFailedAttempts_Object = MibTableColumn
hcAlarmValueFailedAttempts = _HcAlarmValueFailedAttempts_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 16),
    _HcAlarmValueFailedAttempts_Type()
)
hcAlarmValueFailedAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcAlarmValueFailedAttempts.setStatus("current")
_HcAlarmOwner_Type = OwnerString
_HcAlarmOwner_Object = MibTableColumn
hcAlarmOwner = _HcAlarmOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 17),
    _HcAlarmOwner_Type()
)
hcAlarmOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcAlarmOwner.setStatus("current")
_HcAlarmStorageType_Type = StorageType
_HcAlarmStorageType_Object = MibTableColumn
hcAlarmStorageType = _HcAlarmStorageType_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 18),
    _HcAlarmStorageType_Type()
)
hcAlarmStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcAlarmStorageType.setStatus("current")
_HcAlarmStatus_Type = RowStatus
_HcAlarmStatus_Object = MibTableColumn
hcAlarmStatus = _HcAlarmStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 19),
    _HcAlarmStatus_Type()
)
hcAlarmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcAlarmStatus.setStatus("current")
_HcAlarmCapabilitiesObjects_ObjectIdentity = ObjectIdentity
hcAlarmCapabilitiesObjects = _HcAlarmCapabilitiesObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 2)
)


class _HcAlarmCapabilities_Type(Bits):
    """Custom type hcAlarmCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("hcAlarmCreation", 0),
          ("hcAlarmNvStorage", 1))
    )

_HcAlarmCapabilities_Type.__name__ = "Bits"
_HcAlarmCapabilities_Object = MibScalar
hcAlarmCapabilities = _HcAlarmCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 16, 29, 1, 2, 1),
    _HcAlarmCapabilities_Type()
)
hcAlarmCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcAlarmCapabilities.setStatus("current")
_HcAlarmNotifications_ObjectIdentity = ObjectIdentity
hcAlarmNotifications = _HcAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 29, 2)
)
_HcAlarmNotifPrefix_ObjectIdentity = ObjectIdentity
hcAlarmNotifPrefix = _HcAlarmNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 29, 2, 0)
)
_HcAlarmConformance_ObjectIdentity = ObjectIdentity
hcAlarmConformance = _HcAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 29, 3)
)
_HcAlarmCompliances_ObjectIdentity = ObjectIdentity
hcAlarmCompliances = _HcAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 29, 3, 1)
)
_HcAlarmGroups_ObjectIdentity = ObjectIdentity
hcAlarmGroups = _HcAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 29, 3, 2)
)

# Managed Objects groups

hcAlarmControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 29, 3, 2, 1)
)
hcAlarmControlGroup.setObjects(
      *(("HC-ALARM-MIB", "hcAlarmInterval"),
        ("HC-ALARM-MIB", "hcAlarmVariable"),
        ("HC-ALARM-MIB", "hcAlarmSampleType"),
        ("HC-ALARM-MIB", "hcAlarmAbsValue"),
        ("HC-ALARM-MIB", "hcAlarmValueStatus"),
        ("HC-ALARM-MIB", "hcAlarmStartupAlarm"),
        ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueLo"),
        ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueHi"),
        ("HC-ALARM-MIB", "hcAlarmRisingThresholdValStatus"),
        ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueLo"),
        ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueHi"),
        ("HC-ALARM-MIB", "hcAlarmFallingThresholdValStatus"),
        ("HC-ALARM-MIB", "hcAlarmRisingEventIndex"),
        ("HC-ALARM-MIB", "hcAlarmFallingEventIndex"),
        ("HC-ALARM-MIB", "hcAlarmValueFailedAttempts"),
        ("HC-ALARM-MIB", "hcAlarmOwner"),
        ("HC-ALARM-MIB", "hcAlarmStorageType"),
        ("HC-ALARM-MIB", "hcAlarmStatus"))
)
if mibBuilder.loadTexts:
    hcAlarmControlGroup.setStatus("current")

hcAlarmCapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 29, 3, 2, 2)
)
hcAlarmCapabilitiesGroup.setObjects(
    ("HC-ALARM-MIB", "hcAlarmCapabilities")
)
if mibBuilder.loadTexts:
    hcAlarmCapabilitiesGroup.setStatus("current")


# Notification objects

hcRisingAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 29, 2, 0, 1)
)
hcRisingAlarm.setObjects(
      *(("HC-ALARM-MIB", "hcAlarmVariable"),
        ("HC-ALARM-MIB", "hcAlarmSampleType"),
        ("HC-ALARM-MIB", "hcAlarmAbsValue"),
        ("HC-ALARM-MIB", "hcAlarmValueStatus"),
        ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueLo"),
        ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueHi"),
        ("HC-ALARM-MIB", "hcAlarmRisingThresholdValStatus"),
        ("HC-ALARM-MIB", "hcAlarmRisingEventIndex"))
)
if mibBuilder.loadTexts:
    hcRisingAlarm.setStatus(
        "current"
    )

hcFallingAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 29, 2, 0, 2)
)
hcFallingAlarm.setObjects(
      *(("HC-ALARM-MIB", "hcAlarmVariable"),
        ("HC-ALARM-MIB", "hcAlarmSampleType"),
        ("HC-ALARM-MIB", "hcAlarmAbsValue"),
        ("HC-ALARM-MIB", "hcAlarmValueStatus"),
        ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueLo"),
        ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueHi"),
        ("HC-ALARM-MIB", "hcAlarmFallingThresholdValStatus"),
        ("HC-ALARM-MIB", "hcAlarmFallingEventIndex"))
)
if mibBuilder.loadTexts:
    hcFallingAlarm.setStatus(
        "current"
    )


# Notifications groups

hcAlarmNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 16, 29, 3, 2, 3)
)
hcAlarmNotificationsGroup.setObjects(
      *(("HC-ALARM-MIB", "hcRisingAlarm"),
        ("HC-ALARM-MIB", "hcFallingAlarm"))
)
if mibBuilder.loadTexts:
    hcAlarmNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hcAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 29, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hcAlarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HC-ALARM-MIB",
    **{"HcValueStatus": HcValueStatus,
       "hcAlarmMIB": hcAlarmMIB,
       "hcAlarmObjects": hcAlarmObjects,
       "hcAlarmControlObjects": hcAlarmControlObjects,
       "hcAlarmTable": hcAlarmTable,
       "hcAlarmEntry": hcAlarmEntry,
       "hcAlarmIndex": hcAlarmIndex,
       "hcAlarmInterval": hcAlarmInterval,
       "hcAlarmVariable": hcAlarmVariable,
       "hcAlarmSampleType": hcAlarmSampleType,
       "hcAlarmAbsValue": hcAlarmAbsValue,
       "hcAlarmValueStatus": hcAlarmValueStatus,
       "hcAlarmStartupAlarm": hcAlarmStartupAlarm,
       "hcAlarmRisingThreshAbsValueLo": hcAlarmRisingThreshAbsValueLo,
       "hcAlarmRisingThreshAbsValueHi": hcAlarmRisingThreshAbsValueHi,
       "hcAlarmRisingThresholdValStatus": hcAlarmRisingThresholdValStatus,
       "hcAlarmFallingThreshAbsValueLo": hcAlarmFallingThreshAbsValueLo,
       "hcAlarmFallingThreshAbsValueHi": hcAlarmFallingThreshAbsValueHi,
       "hcAlarmFallingThresholdValStatus": hcAlarmFallingThresholdValStatus,
       "hcAlarmRisingEventIndex": hcAlarmRisingEventIndex,
       "hcAlarmFallingEventIndex": hcAlarmFallingEventIndex,
       "hcAlarmValueFailedAttempts": hcAlarmValueFailedAttempts,
       "hcAlarmOwner": hcAlarmOwner,
       "hcAlarmStorageType": hcAlarmStorageType,
       "hcAlarmStatus": hcAlarmStatus,
       "hcAlarmCapabilitiesObjects": hcAlarmCapabilitiesObjects,
       "hcAlarmCapabilities": hcAlarmCapabilities,
       "hcAlarmNotifications": hcAlarmNotifications,
       "hcAlarmNotifPrefix": hcAlarmNotifPrefix,
       "hcRisingAlarm": hcRisingAlarm,
       "hcFallingAlarm": hcFallingAlarm,
       "hcAlarmConformance": hcAlarmConformance,
       "hcAlarmCompliances": hcAlarmCompliances,
       "hcAlarmCompliance": hcAlarmCompliance,
       "hcAlarmGroups": hcAlarmGroups,
       "hcAlarmControlGroup": hcAlarmControlGroup,
       "hcAlarmCapabilitiesGroup": hcAlarmCapabilitiesGroup,
       "hcAlarmNotificationsGroup": hcAlarmNotificationsGroup}
)
