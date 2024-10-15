# SNMP MIB module (ENERGY-OBJECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENERGY-OBJECT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:32 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(PowerStateSet,) = mibBuilder.importSymbols(
    "IANAPowerStateSet-MIB",
    "PowerStateSet")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

energyObjectMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 229)
)
energyObjectMib.setRevisions(
        ("2015-02-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UnitMultiplier(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-24,
              -21,
              -18,
              -15,
              -12,
              -9,
              -6,
              -3,
              0,
              3,
              6,
              9,
              12,
              15,
              18,
              21,
              24)
        )
    )
    namedValues = NamedValues(
        *(("atto", -18),
          ("exa", 18),
          ("femto", -15),
          ("giga", 9),
          ("kilo", 3),
          ("mega", 6),
          ("micro", -6),
          ("milli", -3),
          ("nano", -9),
          ("peta", 15),
          ("pico", -12),
          ("tera", 12),
          ("units", 0),
          ("yocto", -24),
          ("yotta", 24),
          ("zepto", -21),
          ("zetta", 21))
    )



# MIB Managed Objects in the order of their OIDs

_EnergyObjectMibNotifs_ObjectIdentity = ObjectIdentity
energyObjectMibNotifs = _EnergyObjectMibNotifs_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 229, 0)
)


class _EoPowerEnableStatusNotification_Type(TruthValue):
    """Custom type eoPowerEnableStatusNotification based on TruthValue"""


_EoPowerEnableStatusNotification_Object = MibScalar
eoPowerEnableStatusNotification = _EoPowerEnableStatusNotification_Object(
    (1, 3, 6, 1, 2, 1, 229, 0, 1),
    _EoPowerEnableStatusNotification_Type()
)
eoPowerEnableStatusNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoPowerEnableStatusNotification.setStatus("current")
_EnergyObjectMibObjects_ObjectIdentity = ObjectIdentity
energyObjectMibObjects = _EnergyObjectMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 229, 1)
)
_EoMeterCapabilitiesTable_Object = MibTable
eoMeterCapabilitiesTable = _EoMeterCapabilitiesTable_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 1)
)
if mibBuilder.loadTexts:
    eoMeterCapabilitiesTable.setStatus("current")
_EoMeterCapabilitiesEntry_Object = MibTableRow
eoMeterCapabilitiesEntry = _EoMeterCapabilitiesEntry_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 1, 1)
)
eoMeterCapabilitiesEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    eoMeterCapabilitiesEntry.setStatus("current")


class _EoMeterCapability_Type(Bits):
    """Custom type eoMeterCapability based on Bits"""
    namedValues = NamedValues(
        *(("energymetering", 2),
          ("none", 0),
          ("powerattributes", 3),
          ("powermetering", 1))
    )

_EoMeterCapability_Type.__name__ = "Bits"
_EoMeterCapability_Object = MibTableColumn
eoMeterCapability = _EoMeterCapability_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 1, 1, 1),
    _EoMeterCapability_Type()
)
eoMeterCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoMeterCapability.setStatus("current")
_EoPowerTable_Object = MibTable
eoPowerTable = _EoPowerTable_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 2)
)
if mibBuilder.loadTexts:
    eoPowerTable.setStatus("current")
_EoPowerEntry_Object = MibTableRow
eoPowerEntry = _EoPowerEntry_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 2, 1)
)
eoPowerEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    eoPowerEntry.setStatus("current")
_EoPower_Type = Integer32
_EoPower_Object = MibTableColumn
eoPower = _EoPower_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 2, 1, 1),
    _EoPower_Type()
)
eoPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoPower.setStatus("current")
if mibBuilder.loadTexts:
    eoPower.setUnits("watts")
_EoPowerNameplate_Type = Unsigned32
_EoPowerNameplate_Object = MibTableColumn
eoPowerNameplate = _EoPowerNameplate_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 2, 1, 2),
    _EoPowerNameplate_Type()
)
eoPowerNameplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoPowerNameplate.setStatus("current")
if mibBuilder.loadTexts:
    eoPowerNameplate.setUnits("watts")
_EoPowerUnitMultiplier_Type = UnitMultiplier
_EoPowerUnitMultiplier_Object = MibTableColumn
eoPowerUnitMultiplier = _EoPowerUnitMultiplier_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 2, 1, 3),
    _EoPowerUnitMultiplier_Type()
)
eoPowerUnitMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoPowerUnitMultiplier.setStatus("current")


class _EoPowerAccuracy_Type(Integer32):
    """Custom type eoPowerAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EoPowerAccuracy_Type.__name__ = "Integer32"
_EoPowerAccuracy_Object = MibTableColumn
eoPowerAccuracy = _EoPowerAccuracy_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 2, 1, 4),
    _EoPowerAccuracy_Type()
)
eoPowerAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoPowerAccuracy.setStatus("current")
if mibBuilder.loadTexts:
    eoPowerAccuracy.setUnits("hundredths of percent")


class _EoPowerMeasurementCaliber_Type(Integer32):
    """Custom type eoPowerMeasurementCaliber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("actual", 3),
          ("estimated", 4),
          ("static", 5),
          ("unavailable", 1),
          ("unknown", 2))
    )


_EoPowerMeasurementCaliber_Type.__name__ = "Integer32"
_EoPowerMeasurementCaliber_Object = MibTableColumn
eoPowerMeasurementCaliber = _EoPowerMeasurementCaliber_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 2, 1, 5),
    _EoPowerMeasurementCaliber_Type()
)
eoPowerMeasurementCaliber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoPowerMeasurementCaliber.setStatus("current")


class _EoPowerCurrentType_Type(Integer32):
    """Custom type eoPowerCurrentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2),
          ("unknown", 3))
    )


_EoPowerCurrentType_Type.__name__ = "Integer32"
_EoPowerCurrentType_Object = MibTableColumn
eoPowerCurrentType = _EoPowerCurrentType_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 2, 1, 6),
    _EoPowerCurrentType_Type()
)
eoPowerCurrentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoPowerCurrentType.setStatus("current")
_EoPowerMeasurementLocal_Type = TruthValue
_EoPowerMeasurementLocal_Object = MibTableColumn
eoPowerMeasurementLocal = _EoPowerMeasurementLocal_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 2, 1, 7),
    _EoPowerMeasurementLocal_Type()
)
eoPowerMeasurementLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoPowerMeasurementLocal.setStatus("current")
_EoPowerAdminState_Type = PowerStateSet
_EoPowerAdminState_Object = MibTableColumn
eoPowerAdminState = _EoPowerAdminState_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 2, 1, 8),
    _EoPowerAdminState_Type()
)
eoPowerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoPowerAdminState.setStatus("current")
_EoPowerOperState_Type = PowerStateSet
_EoPowerOperState_Object = MibTableColumn
eoPowerOperState = _EoPowerOperState_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 2, 1, 9),
    _EoPowerOperState_Type()
)
eoPowerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoPowerOperState.setStatus("current")
_EoPowerStateEnterReason_Type = OwnerString
_EoPowerStateEnterReason_Object = MibTableColumn
eoPowerStateEnterReason = _EoPowerStateEnterReason_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 2, 1, 10),
    _EoPowerStateEnterReason_Type()
)
eoPowerStateEnterReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoPowerStateEnterReason.setStatus("current")
_EoPowerStateTable_Object = MibTable
eoPowerStateTable = _EoPowerStateTable_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 3)
)
if mibBuilder.loadTexts:
    eoPowerStateTable.setStatus("current")
_EoPowerStateEntry_Object = MibTableRow
eoPowerStateEntry = _EoPowerStateEntry_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 3, 1)
)
eoPowerStateEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "ENERGY-OBJECT-MIB", "eoPowerStateIndex"),
)
if mibBuilder.loadTexts:
    eoPowerStateEntry.setStatus("current")
_EoPowerStateIndex_Type = PowerStateSet
_EoPowerStateIndex_Object = MibTableColumn
eoPowerStateIndex = _EoPowerStateIndex_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 3, 1, 1),
    _EoPowerStateIndex_Type()
)
eoPowerStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eoPowerStateIndex.setStatus("current")
_EoPowerStateMaxPower_Type = Integer32
_EoPowerStateMaxPower_Object = MibTableColumn
eoPowerStateMaxPower = _EoPowerStateMaxPower_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 3, 1, 2),
    _EoPowerStateMaxPower_Type()
)
eoPowerStateMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoPowerStateMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    eoPowerStateMaxPower.setUnits("watts")
_EoPowerStatePowerUnitMultiplier_Type = UnitMultiplier
_EoPowerStatePowerUnitMultiplier_Object = MibTableColumn
eoPowerStatePowerUnitMultiplier = _EoPowerStatePowerUnitMultiplier_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 3, 1, 3),
    _EoPowerStatePowerUnitMultiplier_Type()
)
eoPowerStatePowerUnitMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoPowerStatePowerUnitMultiplier.setStatus("current")
_EoPowerStateTotalTime_Type = TimeTicks
_EoPowerStateTotalTime_Object = MibTableColumn
eoPowerStateTotalTime = _EoPowerStateTotalTime_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 3, 1, 4),
    _EoPowerStateTotalTime_Type()
)
eoPowerStateTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoPowerStateTotalTime.setStatus("current")
_EoPowerStateEnterCount_Type = Counter32
_EoPowerStateEnterCount_Object = MibTableColumn
eoPowerStateEnterCount = _EoPowerStateEnterCount_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 3, 1, 5),
    _EoPowerStateEnterCount_Type()
)
eoPowerStateEnterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoPowerStateEnterCount.setStatus("current")
_EoEnergyParametersTable_Object = MibTable
eoEnergyParametersTable = _EoEnergyParametersTable_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 4)
)
if mibBuilder.loadTexts:
    eoEnergyParametersTable.setStatus("current")
_EoEnergyParametersEntry_Object = MibTableRow
eoEnergyParametersEntry = _EoEnergyParametersEntry_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 4, 1)
)
eoEnergyParametersEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "ENERGY-OBJECT-MIB", "eoEnergyParametersIndex"),
)
if mibBuilder.loadTexts:
    eoEnergyParametersEntry.setStatus("current")


class _EoEnergyParametersIndex_Type(Integer32):
    """Custom type eoEnergyParametersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EoEnergyParametersIndex_Type.__name__ = "Integer32"
_EoEnergyParametersIndex_Object = MibTableColumn
eoEnergyParametersIndex = _EoEnergyParametersIndex_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 4, 1, 2),
    _EoEnergyParametersIndex_Type()
)
eoEnergyParametersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eoEnergyParametersIndex.setStatus("current")


class _EoEnergyParametersIntervalLength_Type(TimeInterval):
    """Custom type eoEnergyParametersIntervalLength based on TimeInterval"""
    defaultValue = 90000


_EoEnergyParametersIntervalLength_Object = MibTableColumn
eoEnergyParametersIntervalLength = _EoEnergyParametersIntervalLength_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 4, 1, 3),
    _EoEnergyParametersIntervalLength_Type()
)
eoEnergyParametersIntervalLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eoEnergyParametersIntervalLength.setStatus("current")


class _EoEnergyParametersIntervalNumber_Type(Unsigned32):
    """Custom type eoEnergyParametersIntervalNumber based on Unsigned32"""
    defaultValue = 10


_EoEnergyParametersIntervalNumber_Object = MibTableColumn
eoEnergyParametersIntervalNumber = _EoEnergyParametersIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 4, 1, 4),
    _EoEnergyParametersIntervalNumber_Type()
)
eoEnergyParametersIntervalNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eoEnergyParametersIntervalNumber.setStatus("current")


class _EoEnergyParametersIntervalMode_Type(Integer32):
    """Custom type eoEnergyParametersIntervalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("period", 1),
          ("sliding", 2),
          ("total", 3))
    )


_EoEnergyParametersIntervalMode_Type.__name__ = "Integer32"
_EoEnergyParametersIntervalMode_Object = MibTableColumn
eoEnergyParametersIntervalMode = _EoEnergyParametersIntervalMode_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 4, 1, 5),
    _EoEnergyParametersIntervalMode_Type()
)
eoEnergyParametersIntervalMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eoEnergyParametersIntervalMode.setStatus("current")
_EoEnergyParametersIntervalWindow_Type = TimeInterval
_EoEnergyParametersIntervalWindow_Object = MibTableColumn
eoEnergyParametersIntervalWindow = _EoEnergyParametersIntervalWindow_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 4, 1, 6),
    _EoEnergyParametersIntervalWindow_Type()
)
eoEnergyParametersIntervalWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eoEnergyParametersIntervalWindow.setStatus("current")


class _EoEnergyParametersSampleRate_Type(Unsigned32):
    """Custom type eoEnergyParametersSampleRate based on Unsigned32"""
    defaultValue = 1000


_EoEnergyParametersSampleRate_Object = MibTableColumn
eoEnergyParametersSampleRate = _EoEnergyParametersSampleRate_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 4, 1, 7),
    _EoEnergyParametersSampleRate_Type()
)
eoEnergyParametersSampleRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eoEnergyParametersSampleRate.setStatus("current")
if mibBuilder.loadTexts:
    eoEnergyParametersSampleRate.setUnits("Milliseconds")


class _EoEnergyParametersStorageType_Type(StorageType):
    """Custom type eoEnergyParametersStorageType based on StorageType"""


_EoEnergyParametersStorageType_Object = MibTableColumn
eoEnergyParametersStorageType = _EoEnergyParametersStorageType_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 4, 1, 8),
    _EoEnergyParametersStorageType_Type()
)
eoEnergyParametersStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eoEnergyParametersStorageType.setStatus("current")
_EoEnergyParametersStatus_Type = RowStatus
_EoEnergyParametersStatus_Object = MibTableColumn
eoEnergyParametersStatus = _EoEnergyParametersStatus_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 4, 1, 9),
    _EoEnergyParametersStatus_Type()
)
eoEnergyParametersStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eoEnergyParametersStatus.setStatus("current")
_EoEnergyTable_Object = MibTable
eoEnergyTable = _EoEnergyTable_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 5)
)
if mibBuilder.loadTexts:
    eoEnergyTable.setStatus("current")
_EoEnergyEntry_Object = MibTableRow
eoEnergyEntry = _EoEnergyEntry_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 5, 1)
)
eoEnergyEntry.setIndexNames(
    (0, "ENERGY-OBJECT-MIB", "eoEnergyParametersIndex"),
    (0, "ENERGY-OBJECT-MIB", "eoEnergyCollectionStartTime"),
)
if mibBuilder.loadTexts:
    eoEnergyEntry.setStatus("current")
_EoEnergyCollectionStartTime_Type = TimeTicks
_EoEnergyCollectionStartTime_Object = MibTableColumn
eoEnergyCollectionStartTime = _EoEnergyCollectionStartTime_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 5, 1, 1),
    _EoEnergyCollectionStartTime_Type()
)
eoEnergyCollectionStartTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eoEnergyCollectionStartTime.setStatus("current")
if mibBuilder.loadTexts:
    eoEnergyCollectionStartTime.setUnits("hundredths of a second")
_EoEnergyConsumed_Type = Unsigned32
_EoEnergyConsumed_Object = MibTableColumn
eoEnergyConsumed = _EoEnergyConsumed_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 5, 1, 2),
    _EoEnergyConsumed_Type()
)
eoEnergyConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoEnergyConsumed.setStatus("current")
if mibBuilder.loadTexts:
    eoEnergyConsumed.setUnits("Watt-hours")
_EoEnergyProvided_Type = Unsigned32
_EoEnergyProvided_Object = MibTableColumn
eoEnergyProvided = _EoEnergyProvided_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 5, 1, 3),
    _EoEnergyProvided_Type()
)
eoEnergyProvided.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoEnergyProvided.setStatus("current")
if mibBuilder.loadTexts:
    eoEnergyProvided.setUnits("Watt-hours")
_EoEnergyStored_Type = Unsigned32
_EoEnergyStored_Object = MibTableColumn
eoEnergyStored = _EoEnergyStored_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 5, 1, 4),
    _EoEnergyStored_Type()
)
eoEnergyStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoEnergyStored.setStatus("current")
if mibBuilder.loadTexts:
    eoEnergyStored.setUnits("Watt-hours")
_EoEnergyUnitMultiplier_Type = UnitMultiplier
_EoEnergyUnitMultiplier_Object = MibTableColumn
eoEnergyUnitMultiplier = _EoEnergyUnitMultiplier_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 5, 1, 5),
    _EoEnergyUnitMultiplier_Type()
)
eoEnergyUnitMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoEnergyUnitMultiplier.setStatus("current")


class _EoEnergyAccuracy_Type(Integer32):
    """Custom type eoEnergyAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EoEnergyAccuracy_Type.__name__ = "Integer32"
_EoEnergyAccuracy_Object = MibTableColumn
eoEnergyAccuracy = _EoEnergyAccuracy_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 5, 1, 6),
    _EoEnergyAccuracy_Type()
)
eoEnergyAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoEnergyAccuracy.setStatus("current")
if mibBuilder.loadTexts:
    eoEnergyAccuracy.setUnits("hundredths of percent")
_EoEnergyMaxConsumed_Type = Unsigned32
_EoEnergyMaxConsumed_Object = MibTableColumn
eoEnergyMaxConsumed = _EoEnergyMaxConsumed_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 5, 1, 7),
    _EoEnergyMaxConsumed_Type()
)
eoEnergyMaxConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoEnergyMaxConsumed.setStatus("current")
if mibBuilder.loadTexts:
    eoEnergyMaxConsumed.setUnits("Watt-hours")
_EoEnergyMaxProduced_Type = Unsigned32
_EoEnergyMaxProduced_Object = MibTableColumn
eoEnergyMaxProduced = _EoEnergyMaxProduced_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 5, 1, 8),
    _EoEnergyMaxProduced_Type()
)
eoEnergyMaxProduced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoEnergyMaxProduced.setStatus("current")
if mibBuilder.loadTexts:
    eoEnergyMaxProduced.setUnits("Watt-hours")
_EoEnergyDiscontinuityTime_Type = TimeStamp
_EoEnergyDiscontinuityTime_Object = MibTableColumn
eoEnergyDiscontinuityTime = _EoEnergyDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 229, 1, 5, 1, 9),
    _EoEnergyDiscontinuityTime_Type()
)
eoEnergyDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoEnergyDiscontinuityTime.setStatus("current")
_EnergyObjectMibConform_ObjectIdentity = ObjectIdentity
energyObjectMibConform = _EnergyObjectMibConform_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 229, 2)
)
_EnergyObjectMibCompliances_ObjectIdentity = ObjectIdentity
energyObjectMibCompliances = _EnergyObjectMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 229, 2, 1)
)
_EnergyObjectMibGroups_ObjectIdentity = ObjectIdentity
energyObjectMibGroups = _EnergyObjectMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 229, 2, 2)
)

# Managed Objects groups

energyObjectMibTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 229, 2, 2, 1)
)
energyObjectMibTableGroup.setObjects(
      *(("ENERGY-OBJECT-MIB", "eoPower"),
        ("ENERGY-OBJECT-MIB", "eoPowerNameplate"),
        ("ENERGY-OBJECT-MIB", "eoPowerUnitMultiplier"),
        ("ENERGY-OBJECT-MIB", "eoPowerAccuracy"),
        ("ENERGY-OBJECT-MIB", "eoPowerMeasurementCaliber"),
        ("ENERGY-OBJECT-MIB", "eoPowerCurrentType"),
        ("ENERGY-OBJECT-MIB", "eoPowerMeasurementLocal"),
        ("ENERGY-OBJECT-MIB", "eoPowerAdminState"),
        ("ENERGY-OBJECT-MIB", "eoPowerOperState"),
        ("ENERGY-OBJECT-MIB", "eoPowerStateEnterReason"))
)
if mibBuilder.loadTexts:
    energyObjectMibTableGroup.setStatus("current")

energyObjectMibStateTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 229, 2, 2, 2)
)
energyObjectMibStateTableGroup.setObjects(
      *(("ENERGY-OBJECT-MIB", "eoPowerStateMaxPower"),
        ("ENERGY-OBJECT-MIB", "eoPowerStatePowerUnitMultiplier"),
        ("ENERGY-OBJECT-MIB", "eoPowerStateTotalTime"),
        ("ENERGY-OBJECT-MIB", "eoPowerStateEnterCount"))
)
if mibBuilder.loadTexts:
    energyObjectMibStateTableGroup.setStatus("current")

energyObjectMibEnergyParametersTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 229, 2, 2, 3)
)
energyObjectMibEnergyParametersTableGroup.setObjects(
      *(("ENERGY-OBJECT-MIB", "eoEnergyParametersIntervalLength"),
        ("ENERGY-OBJECT-MIB", "eoEnergyParametersIntervalNumber"),
        ("ENERGY-OBJECT-MIB", "eoEnergyParametersIntervalMode"),
        ("ENERGY-OBJECT-MIB", "eoEnergyParametersIntervalWindow"),
        ("ENERGY-OBJECT-MIB", "eoEnergyParametersSampleRate"),
        ("ENERGY-OBJECT-MIB", "eoEnergyParametersStorageType"),
        ("ENERGY-OBJECT-MIB", "eoEnergyParametersStatus"))
)
if mibBuilder.loadTexts:
    energyObjectMibEnergyParametersTableGroup.setStatus("current")

energyObjectMibEnergyTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 229, 2, 2, 4)
)
energyObjectMibEnergyTableGroup.setObjects(
      *(("ENERGY-OBJECT-MIB", "eoEnergyConsumed"),
        ("ENERGY-OBJECT-MIB", "eoEnergyProvided"),
        ("ENERGY-OBJECT-MIB", "eoEnergyStored"),
        ("ENERGY-OBJECT-MIB", "eoEnergyUnitMultiplier"),
        ("ENERGY-OBJECT-MIB", "eoEnergyAccuracy"),
        ("ENERGY-OBJECT-MIB", "eoEnergyMaxConsumed"),
        ("ENERGY-OBJECT-MIB", "eoEnergyMaxProduced"),
        ("ENERGY-OBJECT-MIB", "eoEnergyDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    energyObjectMibEnergyTableGroup.setStatus("current")

energyObjectMibMeterCapabilitiesTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 229, 2, 2, 5)
)
energyObjectMibMeterCapabilitiesTableGroup.setObjects(
    ("ENERGY-OBJECT-MIB", "eoMeterCapability")
)
if mibBuilder.loadTexts:
    energyObjectMibMeterCapabilitiesTableGroup.setStatus("current")

eoPowerEnableStatusNotificationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 229, 2, 2, 6)
)
eoPowerEnableStatusNotificationGroup.setObjects(
    ("ENERGY-OBJECT-MIB", "eoPowerEnableStatusNotification")
)
if mibBuilder.loadTexts:
    eoPowerEnableStatusNotificationGroup.setStatus("current")


# Notification objects

eoPowerStateChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 229, 0, 2)
)
eoPowerStateChange.setObjects(
      *(("ENERGY-OBJECT-MIB", "eoPowerAdminState"),
        ("ENERGY-OBJECT-MIB", "eoPowerOperState"),
        ("ENERGY-OBJECT-MIB", "eoPowerStateEnterReason"))
)
if mibBuilder.loadTexts:
    eoPowerStateChange.setStatus(
        "current"
    )


# Notifications groups

energyObjectMibNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 229, 2, 2, 7)
)
energyObjectMibNotifGroup.setObjects(
    ("ENERGY-OBJECT-MIB", "eoPowerStateChange")
)
if mibBuilder.loadTexts:
    energyObjectMibNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

energyObjectMibFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 229, 2, 1, 1)
)
if mibBuilder.loadTexts:
    energyObjectMibFullCompliance.setStatus(
        "current"
    )

energyObjectMibReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 229, 2, 1, 2)
)
if mibBuilder.loadTexts:
    energyObjectMibReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENERGY-OBJECT-MIB",
    **{"UnitMultiplier": UnitMultiplier,
       "energyObjectMib": energyObjectMib,
       "energyObjectMibNotifs": energyObjectMibNotifs,
       "eoPowerEnableStatusNotification": eoPowerEnableStatusNotification,
       "eoPowerStateChange": eoPowerStateChange,
       "energyObjectMibObjects": energyObjectMibObjects,
       "eoMeterCapabilitiesTable": eoMeterCapabilitiesTable,
       "eoMeterCapabilitiesEntry": eoMeterCapabilitiesEntry,
       "eoMeterCapability": eoMeterCapability,
       "eoPowerTable": eoPowerTable,
       "eoPowerEntry": eoPowerEntry,
       "eoPower": eoPower,
       "eoPowerNameplate": eoPowerNameplate,
       "eoPowerUnitMultiplier": eoPowerUnitMultiplier,
       "eoPowerAccuracy": eoPowerAccuracy,
       "eoPowerMeasurementCaliber": eoPowerMeasurementCaliber,
       "eoPowerCurrentType": eoPowerCurrentType,
       "eoPowerMeasurementLocal": eoPowerMeasurementLocal,
       "eoPowerAdminState": eoPowerAdminState,
       "eoPowerOperState": eoPowerOperState,
       "eoPowerStateEnterReason": eoPowerStateEnterReason,
       "eoPowerStateTable": eoPowerStateTable,
       "eoPowerStateEntry": eoPowerStateEntry,
       "eoPowerStateIndex": eoPowerStateIndex,
       "eoPowerStateMaxPower": eoPowerStateMaxPower,
       "eoPowerStatePowerUnitMultiplier": eoPowerStatePowerUnitMultiplier,
       "eoPowerStateTotalTime": eoPowerStateTotalTime,
       "eoPowerStateEnterCount": eoPowerStateEnterCount,
       "eoEnergyParametersTable": eoEnergyParametersTable,
       "eoEnergyParametersEntry": eoEnergyParametersEntry,
       "eoEnergyParametersIndex": eoEnergyParametersIndex,
       "eoEnergyParametersIntervalLength": eoEnergyParametersIntervalLength,
       "eoEnergyParametersIntervalNumber": eoEnergyParametersIntervalNumber,
       "eoEnergyParametersIntervalMode": eoEnergyParametersIntervalMode,
       "eoEnergyParametersIntervalWindow": eoEnergyParametersIntervalWindow,
       "eoEnergyParametersSampleRate": eoEnergyParametersSampleRate,
       "eoEnergyParametersStorageType": eoEnergyParametersStorageType,
       "eoEnergyParametersStatus": eoEnergyParametersStatus,
       "eoEnergyTable": eoEnergyTable,
       "eoEnergyEntry": eoEnergyEntry,
       "eoEnergyCollectionStartTime": eoEnergyCollectionStartTime,
       "eoEnergyConsumed": eoEnergyConsumed,
       "eoEnergyProvided": eoEnergyProvided,
       "eoEnergyStored": eoEnergyStored,
       "eoEnergyUnitMultiplier": eoEnergyUnitMultiplier,
       "eoEnergyAccuracy": eoEnergyAccuracy,
       "eoEnergyMaxConsumed": eoEnergyMaxConsumed,
       "eoEnergyMaxProduced": eoEnergyMaxProduced,
       "eoEnergyDiscontinuityTime": eoEnergyDiscontinuityTime,
       "energyObjectMibConform": energyObjectMibConform,
       "energyObjectMibCompliances": energyObjectMibCompliances,
       "energyObjectMibFullCompliance": energyObjectMibFullCompliance,
       "energyObjectMibReadOnlyCompliance": energyObjectMibReadOnlyCompliance,
       "energyObjectMibGroups": energyObjectMibGroups,
       "energyObjectMibTableGroup": energyObjectMibTableGroup,
       "energyObjectMibStateTableGroup": energyObjectMibStateTableGroup,
       "energyObjectMibEnergyParametersTableGroup": energyObjectMibEnergyParametersTableGroup,
       "energyObjectMibEnergyTableGroup": energyObjectMibEnergyTableGroup,
       "energyObjectMibMeterCapabilitiesTableGroup": energyObjectMibMeterCapabilitiesTableGroup,
       "eoPowerEnableStatusNotificationGroup": eoPowerEnableStatusNotificationGroup,
       "energyObjectMibNotifGroup": energyObjectMibNotifGroup}
)
