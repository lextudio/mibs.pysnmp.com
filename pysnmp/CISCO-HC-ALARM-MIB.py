# SNMP MIB module (CISCO-HC-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-HC-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:12 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(OwnerString,
 rmonEventGroup) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString",
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

ciscoHcAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 93)
)
ciscoHcAlarmMIB.setRevisions(
        ("2002-10-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CHcValueStatus(Integer32, TextualConvention):
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

_CHcAlarmObjects_ObjectIdentity = ObjectIdentity
cHcAlarmObjects = _CHcAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1)
)
_CHcAlarmControlObjects_ObjectIdentity = ObjectIdentity
cHcAlarmControlObjects = _CHcAlarmControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1)
)
_CHcAlarmTable_Object = MibTable
cHcAlarmTable = _CHcAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cHcAlarmTable.setStatus("current")
_CHcAlarmEntry_Object = MibTableRow
cHcAlarmEntry = _CHcAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1)
)
cHcAlarmEntry.setIndexNames(
    (0, "CISCO-HC-ALARM-MIB", "cHcAlarmIndex"),
)
if mibBuilder.loadTexts:
    cHcAlarmEntry.setStatus("current")


class _CHcAlarmIndex_Type(Integer32):
    """Custom type cHcAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CHcAlarmIndex_Type.__name__ = "Integer32"
_CHcAlarmIndex_Object = MibTableColumn
cHcAlarmIndex = _CHcAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 1),
    _CHcAlarmIndex_Type()
)
cHcAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cHcAlarmIndex.setStatus("current")


class _CHcAlarmInterval_Type(Integer32):
    """Custom type cHcAlarmInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CHcAlarmInterval_Type.__name__ = "Integer32"
_CHcAlarmInterval_Object = MibTableColumn
cHcAlarmInterval = _CHcAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 2),
    _CHcAlarmInterval_Type()
)
cHcAlarmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHcAlarmInterval.setStatus("current")
if mibBuilder.loadTexts:
    cHcAlarmInterval.setUnits("seconds")
_CHcAlarmVariable_Type = VariablePointer
_CHcAlarmVariable_Object = MibTableColumn
cHcAlarmVariable = _CHcAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 3),
    _CHcAlarmVariable_Type()
)
cHcAlarmVariable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHcAlarmVariable.setStatus("current")


class _CHcAlarmSampleType_Type(Integer32):
    """Custom type cHcAlarmSampleType based on Integer32"""
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


_CHcAlarmSampleType_Type.__name__ = "Integer32"
_CHcAlarmSampleType_Object = MibTableColumn
cHcAlarmSampleType = _CHcAlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 4),
    _CHcAlarmSampleType_Type()
)
cHcAlarmSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHcAlarmSampleType.setStatus("current")
_CHcAlarmAbsValue_Type = CounterBasedGauge64
_CHcAlarmAbsValue_Object = MibTableColumn
cHcAlarmAbsValue = _CHcAlarmAbsValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 5),
    _CHcAlarmAbsValue_Type()
)
cHcAlarmAbsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHcAlarmAbsValue.setStatus("current")
_CHcAlarmValueStatus_Type = CHcValueStatus
_CHcAlarmValueStatus_Object = MibTableColumn
cHcAlarmValueStatus = _CHcAlarmValueStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 6),
    _CHcAlarmValueStatus_Type()
)
cHcAlarmValueStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHcAlarmValueStatus.setStatus("current")


class _CHcAlarmStartupAlarm_Type(Integer32):
    """Custom type cHcAlarmStartupAlarm based on Integer32"""
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


_CHcAlarmStartupAlarm_Type.__name__ = "Integer32"
_CHcAlarmStartupAlarm_Object = MibTableColumn
cHcAlarmStartupAlarm = _CHcAlarmStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 7),
    _CHcAlarmStartupAlarm_Type()
)
cHcAlarmStartupAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHcAlarmStartupAlarm.setStatus("current")
_CHcAlarmRisingThreshAbsValueLo_Type = Unsigned32
_CHcAlarmRisingThreshAbsValueLo_Object = MibTableColumn
cHcAlarmRisingThreshAbsValueLo = _CHcAlarmRisingThreshAbsValueLo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 8),
    _CHcAlarmRisingThreshAbsValueLo_Type()
)
cHcAlarmRisingThreshAbsValueLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHcAlarmRisingThreshAbsValueLo.setStatus("current")
_CHcAlarmRisingThreshAbsValueHi_Type = Unsigned32
_CHcAlarmRisingThreshAbsValueHi_Object = MibTableColumn
cHcAlarmRisingThreshAbsValueHi = _CHcAlarmRisingThreshAbsValueHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 9),
    _CHcAlarmRisingThreshAbsValueHi_Type()
)
cHcAlarmRisingThreshAbsValueHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHcAlarmRisingThreshAbsValueHi.setStatus("current")
_CHcAlarmRisingThresholdValStatus_Type = CHcValueStatus
_CHcAlarmRisingThresholdValStatus_Object = MibTableColumn
cHcAlarmRisingThresholdValStatus = _CHcAlarmRisingThresholdValStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 10),
    _CHcAlarmRisingThresholdValStatus_Type()
)
cHcAlarmRisingThresholdValStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHcAlarmRisingThresholdValStatus.setStatus("current")
_CHcAlarmFallingThreshAbsValueLo_Type = Unsigned32
_CHcAlarmFallingThreshAbsValueLo_Object = MibTableColumn
cHcAlarmFallingThreshAbsValueLo = _CHcAlarmFallingThreshAbsValueLo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 11),
    _CHcAlarmFallingThreshAbsValueLo_Type()
)
cHcAlarmFallingThreshAbsValueLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHcAlarmFallingThreshAbsValueLo.setStatus("current")
_CHcAlarmFallingThreshAbsValueHi_Type = Unsigned32
_CHcAlarmFallingThreshAbsValueHi_Object = MibTableColumn
cHcAlarmFallingThreshAbsValueHi = _CHcAlarmFallingThreshAbsValueHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 12),
    _CHcAlarmFallingThreshAbsValueHi_Type()
)
cHcAlarmFallingThreshAbsValueHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHcAlarmFallingThreshAbsValueHi.setStatus("current")
_CHcAlarmFallingThrsholdValStatus_Type = CHcValueStatus
_CHcAlarmFallingThrsholdValStatus_Object = MibTableColumn
cHcAlarmFallingThrsholdValStatus = _CHcAlarmFallingThrsholdValStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 13),
    _CHcAlarmFallingThrsholdValStatus_Type()
)
cHcAlarmFallingThrsholdValStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHcAlarmFallingThrsholdValStatus.setStatus("current")


class _CHcAlarmRisingEventIndex_Type(Integer32):
    """Custom type cHcAlarmRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CHcAlarmRisingEventIndex_Type.__name__ = "Integer32"
_CHcAlarmRisingEventIndex_Object = MibTableColumn
cHcAlarmRisingEventIndex = _CHcAlarmRisingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 14),
    _CHcAlarmRisingEventIndex_Type()
)
cHcAlarmRisingEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHcAlarmRisingEventIndex.setStatus("current")


class _CHcAlarmFallingEventIndex_Type(Integer32):
    """Custom type cHcAlarmFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CHcAlarmFallingEventIndex_Type.__name__ = "Integer32"
_CHcAlarmFallingEventIndex_Object = MibTableColumn
cHcAlarmFallingEventIndex = _CHcAlarmFallingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 15),
    _CHcAlarmFallingEventIndex_Type()
)
cHcAlarmFallingEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHcAlarmFallingEventIndex.setStatus("current")
_CHcAlarmValueFailedAttempts_Type = Counter32
_CHcAlarmValueFailedAttempts_Object = MibTableColumn
cHcAlarmValueFailedAttempts = _CHcAlarmValueFailedAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 16),
    _CHcAlarmValueFailedAttempts_Type()
)
cHcAlarmValueFailedAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHcAlarmValueFailedAttempts.setStatus("current")
_CHcAlarmOwner_Type = OwnerString
_CHcAlarmOwner_Object = MibTableColumn
cHcAlarmOwner = _CHcAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 17),
    _CHcAlarmOwner_Type()
)
cHcAlarmOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHcAlarmOwner.setStatus("current")
_CHcAlarmStorageType_Type = StorageType
_CHcAlarmStorageType_Object = MibTableColumn
cHcAlarmStorageType = _CHcAlarmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 18),
    _CHcAlarmStorageType_Type()
)
cHcAlarmStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHcAlarmStorageType.setStatus("current")
_CHcAlarmStatus_Type = RowStatus
_CHcAlarmStatus_Object = MibTableColumn
cHcAlarmStatus = _CHcAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 1, 1, 1, 19),
    _CHcAlarmStatus_Type()
)
cHcAlarmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHcAlarmStatus.setStatus("current")
_CHcAlarmCapabilitiesObjects_ObjectIdentity = ObjectIdentity
cHcAlarmCapabilitiesObjects = _CHcAlarmCapabilitiesObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 2)
)


class _CHcAlarmCapabilities_Type(Bits):
    """Custom type cHcAlarmCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("cHcAlarmCreation", 0),
          ("cHcAlarmNvStorage", 1))
    )

_CHcAlarmCapabilities_Type.__name__ = "Bits"
_CHcAlarmCapabilities_Object = MibScalar
cHcAlarmCapabilities = _CHcAlarmCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 1, 2, 1),
    _CHcAlarmCapabilities_Type()
)
cHcAlarmCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHcAlarmCapabilities.setStatus("current")
_CHcAlarmNotifications_ObjectIdentity = ObjectIdentity
cHcAlarmNotifications = _CHcAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 2)
)
_CHcAlarmNotifPrefix_ObjectIdentity = ObjectIdentity
cHcAlarmNotifPrefix = _CHcAlarmNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 2, 0)
)
_CHcAlarmConformance_ObjectIdentity = ObjectIdentity
cHcAlarmConformance = _CHcAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 3)
)
_CHcAlarmCompliances_ObjectIdentity = ObjectIdentity
cHcAlarmCompliances = _CHcAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 3, 1)
)
_CHcAlarmGroups_ObjectIdentity = ObjectIdentity
cHcAlarmGroups = _CHcAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 3, 2)
)

# Managed Objects groups

cHcAlarmControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 3, 2, 1)
)
cHcAlarmControlGroup.setObjects(
      *(("CISCO-HC-ALARM-MIB", "cHcAlarmInterval"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmVariable"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmSampleType"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmAbsValue"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmValueStatus"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmStartupAlarm"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmRisingThreshAbsValueLo"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmRisingThreshAbsValueHi"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmRisingThresholdValStatus"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmFallingThreshAbsValueLo"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmFallingThreshAbsValueHi"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmFallingThrsholdValStatus"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmRisingEventIndex"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmFallingEventIndex"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmValueFailedAttempts"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmOwner"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmStorageType"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmStatus"))
)
if mibBuilder.loadTexts:
    cHcAlarmControlGroup.setStatus("current")

cHcAlarmCapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 3, 2, 2)
)
cHcAlarmCapabilitiesGroup.setObjects(
    ("CISCO-HC-ALARM-MIB", "cHcAlarmCapabilities")
)
if mibBuilder.loadTexts:
    cHcAlarmCapabilitiesGroup.setStatus("current")


# Notification objects

cHcRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 2, 0, 1)
)
cHcRisingAlarm.setObjects(
      *(("CISCO-HC-ALARM-MIB", "cHcAlarmVariable"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmSampleType"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmAbsValue"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmValueStatus"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmRisingThreshAbsValueLo"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmRisingThreshAbsValueHi"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmRisingThresholdValStatus"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmRisingEventIndex"))
)
if mibBuilder.loadTexts:
    cHcRisingAlarm.setStatus(
        "current"
    )

cHcFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 2, 0, 2)
)
cHcFallingAlarm.setObjects(
      *(("CISCO-HC-ALARM-MIB", "cHcAlarmVariable"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmSampleType"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmAbsValue"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmValueStatus"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmFallingThreshAbsValueLo"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmFallingThreshAbsValueHi"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmFallingThrsholdValStatus"),
        ("CISCO-HC-ALARM-MIB", "cHcAlarmFallingEventIndex"))
)
if mibBuilder.loadTexts:
    cHcFallingAlarm.setStatus(
        "current"
    )


# Notifications groups

cHcAlarmNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 3, 2, 3)
)
cHcAlarmNotificationsGroup.setObjects(
      *(("CISCO-HC-ALARM-MIB", "cHcRisingAlarm"),
        ("CISCO-HC-ALARM-MIB", "cHcFallingAlarm"))
)
if mibBuilder.loadTexts:
    cHcAlarmNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cHcAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 93, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cHcAlarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-HC-ALARM-MIB",
    **{"CHcValueStatus": CHcValueStatus,
       "ciscoHcAlarmMIB": ciscoHcAlarmMIB,
       "cHcAlarmObjects": cHcAlarmObjects,
       "cHcAlarmControlObjects": cHcAlarmControlObjects,
       "cHcAlarmTable": cHcAlarmTable,
       "cHcAlarmEntry": cHcAlarmEntry,
       "cHcAlarmIndex": cHcAlarmIndex,
       "cHcAlarmInterval": cHcAlarmInterval,
       "cHcAlarmVariable": cHcAlarmVariable,
       "cHcAlarmSampleType": cHcAlarmSampleType,
       "cHcAlarmAbsValue": cHcAlarmAbsValue,
       "cHcAlarmValueStatus": cHcAlarmValueStatus,
       "cHcAlarmStartupAlarm": cHcAlarmStartupAlarm,
       "cHcAlarmRisingThreshAbsValueLo": cHcAlarmRisingThreshAbsValueLo,
       "cHcAlarmRisingThreshAbsValueHi": cHcAlarmRisingThreshAbsValueHi,
       "cHcAlarmRisingThresholdValStatus": cHcAlarmRisingThresholdValStatus,
       "cHcAlarmFallingThreshAbsValueLo": cHcAlarmFallingThreshAbsValueLo,
       "cHcAlarmFallingThreshAbsValueHi": cHcAlarmFallingThreshAbsValueHi,
       "cHcAlarmFallingThrsholdValStatus": cHcAlarmFallingThrsholdValStatus,
       "cHcAlarmRisingEventIndex": cHcAlarmRisingEventIndex,
       "cHcAlarmFallingEventIndex": cHcAlarmFallingEventIndex,
       "cHcAlarmValueFailedAttempts": cHcAlarmValueFailedAttempts,
       "cHcAlarmOwner": cHcAlarmOwner,
       "cHcAlarmStorageType": cHcAlarmStorageType,
       "cHcAlarmStatus": cHcAlarmStatus,
       "cHcAlarmCapabilitiesObjects": cHcAlarmCapabilitiesObjects,
       "cHcAlarmCapabilities": cHcAlarmCapabilities,
       "cHcAlarmNotifications": cHcAlarmNotifications,
       "cHcAlarmNotifPrefix": cHcAlarmNotifPrefix,
       "cHcRisingAlarm": cHcRisingAlarm,
       "cHcFallingAlarm": cHcFallingAlarm,
       "cHcAlarmConformance": cHcAlarmConformance,
       "cHcAlarmCompliances": cHcAlarmCompliances,
       "cHcAlarmCompliance": cHcAlarmCompliance,
       "cHcAlarmGroups": cHcAlarmGroups,
       "cHcAlarmControlGroup": cHcAlarmControlGroup,
       "cHcAlarmCapabilitiesGroup": cHcAlarmCapabilitiesGroup,
       "cHcAlarmNotificationsGroup": cHcAlarmNotificationsGroup}
)
