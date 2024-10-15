# SNMP MIB module (JUNIPER-POWER-SUPPLY-UNIT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-POWER-SUPPLY-UNIT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:02 2024
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

(jnxContentsContainerIndex,
 jnxContentsL1Index,
 jnxContentsL2Index,
 jnxContentsL3Index) = mibBuilder.importSymbols(
    "JUNIPER-MIB",
    "jnxContentsContainerIndex",
    "jnxContentsL1Index",
    "jnxContentsL2Index",
    "jnxContentsL3Index")

(jnxPsuMIBRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxPsuMIBRoot")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxPsuMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1)
)
jnxPsuMIB.setRevisions(
        ("2010-01-27 00:00",
         "2010-05-13 00:00",
         "2010-10-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxPsuNotifications_ObjectIdentity = ObjectIdentity
jnxPsuNotifications = _JnxPsuNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 1)
)
_JnxPsuObjects_ObjectIdentity = ObjectIdentity
jnxPsuObjects = _JnxPsuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2)
)
_JnxPsuScalars_ObjectIdentity = ObjectIdentity
jnxPsuScalars = _JnxPsuScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1)
)
_JnxPsuAvailableDeviceCount_Type = Integer32
_JnxPsuAvailableDeviceCount_Object = MibScalar
jnxPsuAvailableDeviceCount = _JnxPsuAvailableDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 1),
    _JnxPsuAvailableDeviceCount_Type()
)
jnxPsuAvailableDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuAvailableDeviceCount.setStatus("current")
_JnxPsuAvailableAveragePowerSupply_Type = Integer32
_JnxPsuAvailableAveragePowerSupply_Object = MibScalar
jnxPsuAvailableAveragePowerSupply = _JnxPsuAvailableAveragePowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 2),
    _JnxPsuAvailableAveragePowerSupply_Type()
)
jnxPsuAvailableAveragePowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuAvailableAveragePowerSupply.setStatus("current")
_JnxPsuAvailableMaxPowerSupply_Type = Integer32
_JnxPsuAvailableMaxPowerSupply_Object = MibScalar
jnxPsuAvailableMaxPowerSupply = _JnxPsuAvailableMaxPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 3),
    _JnxPsuAvailableMaxPowerSupply_Type()
)
jnxPsuAvailableMaxPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuAvailableMaxPowerSupply.setStatus("current")


class _JnxPsuRedundancy_Type(Integer32):
    """Custom type jnxPsuRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nPlusNRedundancy", 1),
          ("nPlusOneRedundancy", 2),
          ("none", 3))
    )


_JnxPsuRedundancy_Type.__name__ = "Integer32"
_JnxPsuRedundancy_Object = MibScalar
jnxPsuRedundancy = _JnxPsuRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 4),
    _JnxPsuRedundancy_Type()
)
jnxPsuRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuRedundancy.setStatus("current")
_JnxPsuChassisPowerReserved_Type = Integer32
_JnxPsuChassisPowerReserved_Object = MibScalar
jnxPsuChassisPowerReserved = _JnxPsuChassisPowerReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 5),
    _JnxPsuChassisPowerReserved_Type()
)
jnxPsuChassisPowerReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuChassisPowerReserved.setStatus("current")
_JnxPsuChassisPowerAllocated_Type = Integer32
_JnxPsuChassisPowerAllocated_Object = MibScalar
jnxPsuChassisPowerAllocated = _JnxPsuChassisPowerAllocated_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 6),
    _JnxPsuChassisPowerAllocated_Type()
)
jnxPsuChassisPowerAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuChassisPowerAllocated.setStatus("current")
_JnxPsuRedundantPowerAvailable_Type = Integer32
_JnxPsuRedundantPowerAvailable_Object = MibScalar
jnxPsuRedundantPowerAvailable = _JnxPsuRedundantPowerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 7),
    _JnxPsuRedundantPowerAvailable_Type()
)
jnxPsuRedundantPowerAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuRedundantPowerAvailable.setStatus("current")
_JnxPsuTotalPowerAvailable_Type = Integer32
_JnxPsuTotalPowerAvailable_Object = MibScalar
jnxPsuTotalPowerAvailable = _JnxPsuTotalPowerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 8),
    _JnxPsuTotalPowerAvailable_Type()
)
jnxPsuTotalPowerAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuTotalPowerAvailable.setStatus("current")
_JnxPsuChassisPowerConsumed_Type = Integer32
_JnxPsuChassisPowerConsumed_Object = MibScalar
jnxPsuChassisPowerConsumed = _JnxPsuChassisPowerConsumed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 9),
    _JnxPsuChassisPowerConsumed_Type()
)
jnxPsuChassisPowerConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuChassisPowerConsumed.setStatus("current")
_JnxPsuTemperatureInflow_Type = Integer32
_JnxPsuTemperatureInflow_Object = MibScalar
jnxPsuTemperatureInflow = _JnxPsuTemperatureInflow_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 10),
    _JnxPsuTemperatureInflow_Type()
)
jnxPsuTemperatureInflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuTemperatureInflow.setStatus("current")
_JnxPsuTemperatureOutflow_Type = Integer32
_JnxPsuTemperatureOutflow_Object = MibScalar
jnxPsuTemperatureOutflow = _JnxPsuTemperatureOutflow_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 11),
    _JnxPsuTemperatureOutflow_Type()
)
jnxPsuTemperatureOutflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuTemperatureOutflow.setStatus("current")
_JnxPsuTemperatureInflowSamples_Type = Integer32
_JnxPsuTemperatureInflowSamples_Object = MibScalar
jnxPsuTemperatureInflowSamples = _JnxPsuTemperatureInflowSamples_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 12),
    _JnxPsuTemperatureInflowSamples_Type()
)
jnxPsuTemperatureInflowSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuTemperatureInflowSamples.setStatus("current")
_JnxPsuTemperatureOutflowSamples_Type = Integer32
_JnxPsuTemperatureOutflowSamples_Object = MibScalar
jnxPsuTemperatureOutflowSamples = _JnxPsuTemperatureOutflowSamples_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 13),
    _JnxPsuTemperatureOutflowSamples_Type()
)
jnxPsuTemperatureOutflowSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuTemperatureOutflowSamples.setStatus("current")
_JnxPsuTable_Object = MibTable
jnxPsuTable = _JnxPsuTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2)
)
if mibBuilder.loadTexts:
    jnxPsuTable.setStatus("current")
_JnxPsuEntry_Object = MibTableRow
jnxPsuEntry = _JnxPsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2, 1)
)
jnxPsuEntry.setIndexNames(
    (0, "JUNIPER-MIB", "jnxContentsContainerIndex"),
    (0, "JUNIPER-MIB", "jnxContentsL1Index"),
    (0, "JUNIPER-MIB", "jnxContentsL2Index"),
    (0, "JUNIPER-MIB", "jnxContentsL3Index"),
)
if mibBuilder.loadTexts:
    jnxPsuEntry.setStatus("current")
_JnxPsuAvgPower_Type = Integer32
_JnxPsuAvgPower_Object = MibTableColumn
jnxPsuAvgPower = _JnxPsuAvgPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2, 1, 1),
    _JnxPsuAvgPower_Type()
)
jnxPsuAvgPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuAvgPower.setStatus("current")
_JnxPsuMaxPower_Type = Integer32
_JnxPsuMaxPower_Object = MibTableColumn
jnxPsuMaxPower = _JnxPsuMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2, 1, 2),
    _JnxPsuMaxPower_Type()
)
jnxPsuMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuMaxPower.setStatus("current")


class _JnxPsuMode_Type(Integer32):
    """Custom type jnxPsuMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("single", 1),
          ("three", 3))
    )


_JnxPsuMode_Type.__name__ = "Integer32"
_JnxPsuMode_Object = MibTableColumn
jnxPsuMode = _JnxPsuMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2, 1, 3),
    _JnxPsuMode_Type()
)
jnxPsuMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuMode.setStatus("current")


class _JnxPsuOutletCount_Type(Integer32):
    """Custom type jnxPsuOutletCount based on Integer32"""
    defaultValue = 0


_JnxPsuOutletCount_Object = MibTableColumn
jnxPsuOutletCount = _JnxPsuOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2, 1, 4),
    _JnxPsuOutletCount_Type()
)
jnxPsuOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuOutletCount.setStatus("current")
_JnxPsuEnvironmentTable_Object = MibTable
jnxPsuEnvironmentTable = _JnxPsuEnvironmentTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 3)
)
if mibBuilder.loadTexts:
    jnxPsuEnvironmentTable.setStatus("current")
_JnxPsuEnvironmentEntry_Object = MibTableRow
jnxPsuEnvironmentEntry = _JnxPsuEnvironmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 3, 1)
)
jnxPsuEnvironmentEntry.setIndexNames(
    (0, "JUNIPER-MIB", "jnxContentsContainerIndex"),
    (0, "JUNIPER-MIB", "jnxContentsL1Index"),
    (0, "JUNIPER-MIB", "jnxContentsL2Index"),
    (0, "JUNIPER-MIB", "jnxContentsL3Index"),
)
if mibBuilder.loadTexts:
    jnxPsuEnvironmentEntry.setStatus("current")
_JnxPsuThermalValue_Type = Integer32
_JnxPsuThermalValue_Object = MibTableColumn
jnxPsuThermalValue = _JnxPsuThermalValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 3, 1, 1),
    _JnxPsuThermalValue_Type()
)
jnxPsuThermalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuThermalValue.setStatus("current")
_JnxPsuHumidityValue_Type = Integer32
_JnxPsuHumidityValue_Object = MibTableColumn
jnxPsuHumidityValue = _JnxPsuHumidityValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 3, 1, 2),
    _JnxPsuHumidityValue_Type()
)
jnxPsuHumidityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuHumidityValue.setStatus("current")
_JnxPsuOutletTable_Object = MibTable
jnxPsuOutletTable = _JnxPsuOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4)
)
if mibBuilder.loadTexts:
    jnxPsuOutletTable.setStatus("current")
_JnxPsuOutletEntry_Object = MibTableRow
jnxPsuOutletEntry = _JnxPsuOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1)
)
jnxPsuOutletEntry.setIndexNames(
    (0, "JUNIPER-MIB", "jnxContentsContainerIndex"),
    (0, "JUNIPER-MIB", "jnxContentsL1Index"),
    (0, "JUNIPER-MIB", "jnxContentsL2Index"),
    (0, "JUNIPER-MIB", "jnxContentsL3Index"),
)
if mibBuilder.loadTexts:
    jnxPsuOutletEntry.setStatus("current")


class _JnxPsuOutletName_Type(DisplayString):
    """Custom type jnxPsuOutletName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_JnxPsuOutletName_Type.__name__ = "DisplayString"
_JnxPsuOutletName_Object = MibTableColumn
jnxPsuOutletName = _JnxPsuOutletName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 1),
    _JnxPsuOutletName_Type()
)
jnxPsuOutletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuOutletName.setStatus("current")


class _JnxPsuOutletDescription_Type(DisplayString):
    """Custom type jnxPsuOutletDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxPsuOutletDescription_Type.__name__ = "DisplayString"
_JnxPsuOutletDescription_Object = MibTableColumn
jnxPsuOutletDescription = _JnxPsuOutletDescription_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 2),
    _JnxPsuOutletDescription_Type()
)
jnxPsuOutletDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuOutletDescription.setStatus("current")
_JnxPsuOutletAvgPower_Type = Integer32
_JnxPsuOutletAvgPower_Object = MibTableColumn
jnxPsuOutletAvgPower = _JnxPsuOutletAvgPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 3),
    _JnxPsuOutletAvgPower_Type()
)
jnxPsuOutletAvgPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuOutletAvgPower.setStatus("current")
_JnxPsuOutletMaxPower_Type = Integer32
_JnxPsuOutletMaxPower_Object = MibTableColumn
jnxPsuOutletMaxPower = _JnxPsuOutletMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 4),
    _JnxPsuOutletMaxPower_Type()
)
jnxPsuOutletMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuOutletMaxPower.setStatus("current")
_JnxPsuOutletCurrent_Type = Integer32
_JnxPsuOutletCurrent_Object = MibTableColumn
jnxPsuOutletCurrent = _JnxPsuOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 5),
    _JnxPsuOutletCurrent_Type()
)
jnxPsuOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuOutletCurrent.setStatus("current")


class _JnxPsuOutletStatus_Type(Integer32):
    """Custom type jnxPsuOutletStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_JnxPsuOutletStatus_Type.__name__ = "Integer32"
_JnxPsuOutletStatus_Object = MibTableColumn
jnxPsuOutletStatus = _JnxPsuOutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 8),
    _JnxPsuOutletStatus_Type()
)
jnxPsuOutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuOutletStatus.setStatus("current")
_JnxPsuOutletVoltage_Type = Integer32
_JnxPsuOutletVoltage_Object = MibTableColumn
jnxPsuOutletVoltage = _JnxPsuOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 9),
    _JnxPsuOutletVoltage_Type()
)
jnxPsuOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuOutletVoltage.setStatus("current")
_JnxPsuOutletPowerFactorValue_Type = Integer32
_JnxPsuOutletPowerFactorValue_Object = MibTableColumn
jnxPsuOutletPowerFactorValue = _JnxPsuOutletPowerFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 10),
    _JnxPsuOutletPowerFactorValue_Type()
)
jnxPsuOutletPowerFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuOutletPowerFactorValue.setStatus("current")
_JnxPsuOutletPowerConsumed_Type = Integer32
_JnxPsuOutletPowerConsumed_Object = MibTableColumn
jnxPsuOutletPowerConsumed = _JnxPsuOutletPowerConsumed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 11),
    _JnxPsuOutletPowerConsumed_Type()
)
jnxPsuOutletPowerConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuOutletPowerConsumed.setStatus("current")
_JnxPsuFpcPowerTable_Object = MibTable
jnxPsuFpcPowerTable = _JnxPsuFpcPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 5)
)
if mibBuilder.loadTexts:
    jnxPsuFpcPowerTable.setStatus("current")
_JnxPsuFpcPowerEntry_Object = MibTableRow
jnxPsuFpcPowerEntry = _JnxPsuFpcPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 5, 1)
)
jnxPsuFpcPowerEntry.setIndexNames(
    (0, "JUNIPER-MIB", "jnxContentsContainerIndex"),
    (0, "JUNIPER-MIB", "jnxContentsL1Index"),
    (0, "JUNIPER-MIB", "jnxContentsL2Index"),
    (0, "JUNIPER-MIB", "jnxContentsL3Index"),
)
if mibBuilder.loadTexts:
    jnxPsuFpcPowerEntry.setStatus("current")
_JnxPsuFpcPowerPriority_Type = Integer32
_JnxPsuFpcPowerPriority_Object = MibTableColumn
jnxPsuFpcPowerPriority = _JnxPsuFpcPowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 5, 1, 1),
    _JnxPsuFpcPowerPriority_Type()
)
jnxPsuFpcPowerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuFpcPowerPriority.setStatus("current")
_JnxPsuFpcPowerAllocated_Type = Integer32
_JnxPsuFpcPowerAllocated_Object = MibTableColumn
jnxPsuFpcPowerAllocated = _JnxPsuFpcPowerAllocated_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 5, 1, 2),
    _JnxPsuFpcPowerAllocated_Type()
)
jnxPsuFpcPowerAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPsuFpcPowerAllocated.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-POWER-SUPPLY-UNIT-MIB",
    **{"jnxPsuMIB": jnxPsuMIB,
       "jnxPsuNotifications": jnxPsuNotifications,
       "jnxPsuObjects": jnxPsuObjects,
       "jnxPsuScalars": jnxPsuScalars,
       "jnxPsuAvailableDeviceCount": jnxPsuAvailableDeviceCount,
       "jnxPsuAvailableAveragePowerSupply": jnxPsuAvailableAveragePowerSupply,
       "jnxPsuAvailableMaxPowerSupply": jnxPsuAvailableMaxPowerSupply,
       "jnxPsuRedundancy": jnxPsuRedundancy,
       "jnxPsuChassisPowerReserved": jnxPsuChassisPowerReserved,
       "jnxPsuChassisPowerAllocated": jnxPsuChassisPowerAllocated,
       "jnxPsuRedundantPowerAvailable": jnxPsuRedundantPowerAvailable,
       "jnxPsuTotalPowerAvailable": jnxPsuTotalPowerAvailable,
       "jnxPsuChassisPowerConsumed": jnxPsuChassisPowerConsumed,
       "jnxPsuTemperatureInflow": jnxPsuTemperatureInflow,
       "jnxPsuTemperatureOutflow": jnxPsuTemperatureOutflow,
       "jnxPsuTemperatureInflowSamples": jnxPsuTemperatureInflowSamples,
       "jnxPsuTemperatureOutflowSamples": jnxPsuTemperatureOutflowSamples,
       "jnxPsuTable": jnxPsuTable,
       "jnxPsuEntry": jnxPsuEntry,
       "jnxPsuAvgPower": jnxPsuAvgPower,
       "jnxPsuMaxPower": jnxPsuMaxPower,
       "jnxPsuMode": jnxPsuMode,
       "jnxPsuOutletCount": jnxPsuOutletCount,
       "jnxPsuEnvironmentTable": jnxPsuEnvironmentTable,
       "jnxPsuEnvironmentEntry": jnxPsuEnvironmentEntry,
       "jnxPsuThermalValue": jnxPsuThermalValue,
       "jnxPsuHumidityValue": jnxPsuHumidityValue,
       "jnxPsuOutletTable": jnxPsuOutletTable,
       "jnxPsuOutletEntry": jnxPsuOutletEntry,
       "jnxPsuOutletName": jnxPsuOutletName,
       "jnxPsuOutletDescription": jnxPsuOutletDescription,
       "jnxPsuOutletAvgPower": jnxPsuOutletAvgPower,
       "jnxPsuOutletMaxPower": jnxPsuOutletMaxPower,
       "jnxPsuOutletCurrent": jnxPsuOutletCurrent,
       "jnxPsuOutletStatus": jnxPsuOutletStatus,
       "jnxPsuOutletVoltage": jnxPsuOutletVoltage,
       "jnxPsuOutletPowerFactorValue": jnxPsuOutletPowerFactorValue,
       "jnxPsuOutletPowerConsumed": jnxPsuOutletPowerConsumed,
       "jnxPsuFpcPowerTable": jnxPsuFpcPowerTable,
       "jnxPsuFpcPowerEntry": jnxPsuFpcPowerEntry,
       "jnxPsuFpcPowerPriority": jnxPsuFpcPowerPriority,
       "jnxPsuFpcPowerAllocated": jnxPsuFpcPowerAllocated}
)
