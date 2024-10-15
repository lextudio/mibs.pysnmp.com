# SNMP MIB module (POWER-ATTRIBUTES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/POWER-ATTRIBUTES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:20 2024
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

(UnitMultiplier,) = mibBuilder.importSymbols(
    "ENERGY-OBJECT-MIB",
    "UnitMultiplier")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

powerAttributesMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 230)
)
powerAttributesMIB.setRevisions(
        ("2015-02-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PowerAttributesMIBConform_ObjectIdentity = ObjectIdentity
powerAttributesMIBConform = _PowerAttributesMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 230, 0)
)
_PowerAttributesMIBObjects_ObjectIdentity = ObjectIdentity
powerAttributesMIBObjects = _PowerAttributesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 230, 1)
)
_EoACPwrAttributesTable_Object = MibTable
eoACPwrAttributesTable = _EoACPwrAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 1)
)
if mibBuilder.loadTexts:
    eoACPwrAttributesTable.setStatus("current")
_EoACPwrAttributesEntry_Object = MibTableRow
eoACPwrAttributesEntry = _EoACPwrAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 1, 1)
)
eoACPwrAttributesEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    eoACPwrAttributesEntry.setStatus("current")


class _EoACPwrAttributesConfiguration_Type(Integer32):
    """Custom type eoACPwrAttributesConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("del", 2),
          ("sngl", 1),
          ("wye", 3))
    )


_EoACPwrAttributesConfiguration_Type.__name__ = "Integer32"
_EoACPwrAttributesConfiguration_Object = MibTableColumn
eoACPwrAttributesConfiguration = _EoACPwrAttributesConfiguration_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 1, 1, 1),
    _EoACPwrAttributesConfiguration_Type()
)
eoACPwrAttributesConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesConfiguration.setStatus("current")
_EoACPwrAttributesAvgVoltage_Type = Integer32
_EoACPwrAttributesAvgVoltage_Object = MibTableColumn
eoACPwrAttributesAvgVoltage = _EoACPwrAttributesAvgVoltage_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 1, 1, 2),
    _EoACPwrAttributesAvgVoltage_Type()
)
eoACPwrAttributesAvgVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesAvgVoltage.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesAvgVoltage.setUnits("0.1 Volt AC")
_EoACPwrAttributesAvgCurrent_Type = Unsigned32
_EoACPwrAttributesAvgCurrent_Object = MibTableColumn
eoACPwrAttributesAvgCurrent = _EoACPwrAttributesAvgCurrent_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 1, 1, 3),
    _EoACPwrAttributesAvgCurrent_Type()
)
eoACPwrAttributesAvgCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesAvgCurrent.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesAvgCurrent.setUnits("amperes")


class _EoACPwrAttributesFrequency_Type(Integer32):
    """Custom type eoACPwrAttributesFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4500, 6500),
    )


_EoACPwrAttributesFrequency_Type.__name__ = "Integer32"
_EoACPwrAttributesFrequency_Object = MibTableColumn
eoACPwrAttributesFrequency = _EoACPwrAttributesFrequency_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 1, 1, 4),
    _EoACPwrAttributesFrequency_Type()
)
eoACPwrAttributesFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesFrequency.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesFrequency.setUnits("0.01 hertz")
_EoACPwrAttributesPowerUnitMultiplier_Type = UnitMultiplier
_EoACPwrAttributesPowerUnitMultiplier_Object = MibTableColumn
eoACPwrAttributesPowerUnitMultiplier = _EoACPwrAttributesPowerUnitMultiplier_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 1, 1, 5),
    _EoACPwrAttributesPowerUnitMultiplier_Type()
)
eoACPwrAttributesPowerUnitMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesPowerUnitMultiplier.setStatus("current")


class _EoACPwrAttributesPowerAccuracy_Type(Integer32):
    """Custom type eoACPwrAttributesPowerAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EoACPwrAttributesPowerAccuracy_Type.__name__ = "Integer32"
_EoACPwrAttributesPowerAccuracy_Object = MibTableColumn
eoACPwrAttributesPowerAccuracy = _EoACPwrAttributesPowerAccuracy_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 1, 1, 6),
    _EoACPwrAttributesPowerAccuracy_Type()
)
eoACPwrAttributesPowerAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesPowerAccuracy.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesPowerAccuracy.setUnits("hundredths of percent")
_EoACPwrAttributesTotalActivePower_Type = Integer32
_EoACPwrAttributesTotalActivePower_Object = MibTableColumn
eoACPwrAttributesTotalActivePower = _EoACPwrAttributesTotalActivePower_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 1, 1, 7),
    _EoACPwrAttributesTotalActivePower_Type()
)
eoACPwrAttributesTotalActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesTotalActivePower.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesTotalActivePower.setUnits("watts")
_EoACPwrAttributesTotalReactivePower_Type = Integer32
_EoACPwrAttributesTotalReactivePower_Object = MibTableColumn
eoACPwrAttributesTotalReactivePower = _EoACPwrAttributesTotalReactivePower_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 1, 1, 8),
    _EoACPwrAttributesTotalReactivePower_Type()
)
eoACPwrAttributesTotalReactivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesTotalReactivePower.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesTotalReactivePower.setUnits("volt-amperes reactive")
_EoACPwrAttributesTotalApparentPower_Type = Integer32
_EoACPwrAttributesTotalApparentPower_Object = MibTableColumn
eoACPwrAttributesTotalApparentPower = _EoACPwrAttributesTotalApparentPower_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 1, 1, 9),
    _EoACPwrAttributesTotalApparentPower_Type()
)
eoACPwrAttributesTotalApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesTotalApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesTotalApparentPower.setUnits("volt-amperes")


class _EoACPwrAttributesTotalPowerFactor_Type(Integer32):
    """Custom type eoACPwrAttributesTotalPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_EoACPwrAttributesTotalPowerFactor_Type.__name__ = "Integer32"
_EoACPwrAttributesTotalPowerFactor_Object = MibTableColumn
eoACPwrAttributesTotalPowerFactor = _EoACPwrAttributesTotalPowerFactor_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 1, 1, 10),
    _EoACPwrAttributesTotalPowerFactor_Type()
)
eoACPwrAttributesTotalPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesTotalPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesTotalPowerFactor.setUnits("hundredths")


class _EoACPwrAttributesThdCurrent_Type(Integer32):
    """Custom type eoACPwrAttributesThdCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EoACPwrAttributesThdCurrent_Type.__name__ = "Integer32"
_EoACPwrAttributesThdCurrent_Object = MibTableColumn
eoACPwrAttributesThdCurrent = _EoACPwrAttributesThdCurrent_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 1, 1, 11),
    _EoACPwrAttributesThdCurrent_Type()
)
eoACPwrAttributesThdCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesThdCurrent.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesThdCurrent.setUnits("hundredths of percent")


class _EoACPwrAttributesThdVoltage_Type(Integer32):
    """Custom type eoACPwrAttributesThdVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EoACPwrAttributesThdVoltage_Type.__name__ = "Integer32"
_EoACPwrAttributesThdVoltage_Object = MibTableColumn
eoACPwrAttributesThdVoltage = _EoACPwrAttributesThdVoltage_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 1, 1, 12),
    _EoACPwrAttributesThdVoltage_Type()
)
eoACPwrAttributesThdVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesThdVoltage.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesThdVoltage.setUnits("hundredths of percent")
_EoACPwrAttributesDelPhaseTable_Object = MibTable
eoACPwrAttributesDelPhaseTable = _EoACPwrAttributesDelPhaseTable_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 2)
)
if mibBuilder.loadTexts:
    eoACPwrAttributesDelPhaseTable.setStatus("current")
_EoACPwrAttributesDelPhaseEntry_Object = MibTableRow
eoACPwrAttributesDelPhaseEntry = _EoACPwrAttributesDelPhaseEntry_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 2, 1)
)
eoACPwrAttributesDelPhaseEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "POWER-ATTRIBUTES-MIB", "eoACPwrAttributesDelPhaseIndex"),
)
if mibBuilder.loadTexts:
    eoACPwrAttributesDelPhaseEntry.setStatus("current")


class _EoACPwrAttributesDelPhaseIndex_Type(Integer32):
    """Custom type eoACPwrAttributesDelPhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 359),
    )


_EoACPwrAttributesDelPhaseIndex_Type.__name__ = "Integer32"
_EoACPwrAttributesDelPhaseIndex_Object = MibTableColumn
eoACPwrAttributesDelPhaseIndex = _EoACPwrAttributesDelPhaseIndex_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 2, 1, 1),
    _EoACPwrAttributesDelPhaseIndex_Type()
)
eoACPwrAttributesDelPhaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eoACPwrAttributesDelPhaseIndex.setStatus("current")
_EoACPwrAttributesDelPhaseToNextPhaseVoltage_Type = Integer32
_EoACPwrAttributesDelPhaseToNextPhaseVoltage_Object = MibTableColumn
eoACPwrAttributesDelPhaseToNextPhaseVoltage = _EoACPwrAttributesDelPhaseToNextPhaseVoltage_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 2, 1, 2),
    _EoACPwrAttributesDelPhaseToNextPhaseVoltage_Type()
)
eoACPwrAttributesDelPhaseToNextPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesDelPhaseToNextPhaseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesDelPhaseToNextPhaseVoltage.setUnits("0.1 Volt AC")


class _EoACPwrAttributesDelThdPhaseToNextPhaseVoltage_Type(Integer32):
    """Custom type eoACPwrAttributesDelThdPhaseToNextPhaseVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EoACPwrAttributesDelThdPhaseToNextPhaseVoltage_Type.__name__ = "Integer32"
_EoACPwrAttributesDelThdPhaseToNextPhaseVoltage_Object = MibTableColumn
eoACPwrAttributesDelThdPhaseToNextPhaseVoltage = _EoACPwrAttributesDelThdPhaseToNextPhaseVoltage_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 2, 1, 3),
    _EoACPwrAttributesDelThdPhaseToNextPhaseVoltage_Type()
)
eoACPwrAttributesDelThdPhaseToNextPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesDelThdPhaseToNextPhaseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesDelThdPhaseToNextPhaseVoltage.setUnits("hundredths of percent")
_EoACPwrAttributesWyePhaseTable_Object = MibTable
eoACPwrAttributesWyePhaseTable = _EoACPwrAttributesWyePhaseTable_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 3)
)
if mibBuilder.loadTexts:
    eoACPwrAttributesWyePhaseTable.setStatus("current")
_EoACPwrAttributesWyePhaseEntry_Object = MibTableRow
eoACPwrAttributesWyePhaseEntry = _EoACPwrAttributesWyePhaseEntry_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 3, 1)
)
eoACPwrAttributesWyePhaseEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "POWER-ATTRIBUTES-MIB", "eoACPwrAttributesWyePhaseIndex"),
)
if mibBuilder.loadTexts:
    eoACPwrAttributesWyePhaseEntry.setStatus("current")


class _EoACPwrAttributesWyePhaseIndex_Type(Integer32):
    """Custom type eoACPwrAttributesWyePhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 359),
    )


_EoACPwrAttributesWyePhaseIndex_Type.__name__ = "Integer32"
_EoACPwrAttributesWyePhaseIndex_Object = MibTableColumn
eoACPwrAttributesWyePhaseIndex = _EoACPwrAttributesWyePhaseIndex_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 3, 1, 1),
    _EoACPwrAttributesWyePhaseIndex_Type()
)
eoACPwrAttributesWyePhaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eoACPwrAttributesWyePhaseIndex.setStatus("current")
_EoACPwrAttributesWyePhaseToNeutralVoltage_Type = Integer32
_EoACPwrAttributesWyePhaseToNeutralVoltage_Object = MibTableColumn
eoACPwrAttributesWyePhaseToNeutralVoltage = _EoACPwrAttributesWyePhaseToNeutralVoltage_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 3, 1, 2),
    _EoACPwrAttributesWyePhaseToNeutralVoltage_Type()
)
eoACPwrAttributesWyePhaseToNeutralVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesWyePhaseToNeutralVoltage.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesWyePhaseToNeutralVoltage.setUnits("0.1 Volt AC")
_EoACPwrAttributesWyeCurrent_Type = Integer32
_EoACPwrAttributesWyeCurrent_Object = MibTableColumn
eoACPwrAttributesWyeCurrent = _EoACPwrAttributesWyeCurrent_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 3, 1, 3),
    _EoACPwrAttributesWyeCurrent_Type()
)
eoACPwrAttributesWyeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesWyeCurrent.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesWyeCurrent.setUnits("0.1 amperes AC")
_EoACPwrAttributesWyeActivePower_Type = Integer32
_EoACPwrAttributesWyeActivePower_Object = MibTableColumn
eoACPwrAttributesWyeActivePower = _EoACPwrAttributesWyeActivePower_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 3, 1, 4),
    _EoACPwrAttributesWyeActivePower_Type()
)
eoACPwrAttributesWyeActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesWyeActivePower.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesWyeActivePower.setUnits("watts")
_EoACPwrAttributesWyeReactivePower_Type = Integer32
_EoACPwrAttributesWyeReactivePower_Object = MibTableColumn
eoACPwrAttributesWyeReactivePower = _EoACPwrAttributesWyeReactivePower_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 3, 1, 5),
    _EoACPwrAttributesWyeReactivePower_Type()
)
eoACPwrAttributesWyeReactivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesWyeReactivePower.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesWyeReactivePower.setUnits("volt-amperes reactive")
_EoACPwrAttributesWyeApparentPower_Type = Integer32
_EoACPwrAttributesWyeApparentPower_Object = MibTableColumn
eoACPwrAttributesWyeApparentPower = _EoACPwrAttributesWyeApparentPower_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 3, 1, 6),
    _EoACPwrAttributesWyeApparentPower_Type()
)
eoACPwrAttributesWyeApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesWyeApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesWyeApparentPower.setUnits("volt-amperes")


class _EoACPwrAttributesWyePowerFactor_Type(Integer32):
    """Custom type eoACPwrAttributesWyePowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_EoACPwrAttributesWyePowerFactor_Type.__name__ = "Integer32"
_EoACPwrAttributesWyePowerFactor_Object = MibTableColumn
eoACPwrAttributesWyePowerFactor = _EoACPwrAttributesWyePowerFactor_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 3, 1, 7),
    _EoACPwrAttributesWyePowerFactor_Type()
)
eoACPwrAttributesWyePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesWyePowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesWyePowerFactor.setUnits("hundredths")


class _EoACPwrAttributesWyeThdCurrent_Type(Integer32):
    """Custom type eoACPwrAttributesWyeThdCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EoACPwrAttributesWyeThdCurrent_Type.__name__ = "Integer32"
_EoACPwrAttributesWyeThdCurrent_Object = MibTableColumn
eoACPwrAttributesWyeThdCurrent = _EoACPwrAttributesWyeThdCurrent_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 3, 1, 8),
    _EoACPwrAttributesWyeThdCurrent_Type()
)
eoACPwrAttributesWyeThdCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesWyeThdCurrent.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesWyeThdCurrent.setUnits("hundredths of percent")


class _EoACPwrAttributesWyeThdPhaseToNeutralVoltage_Type(Integer32):
    """Custom type eoACPwrAttributesWyeThdPhaseToNeutralVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EoACPwrAttributesWyeThdPhaseToNeutralVoltage_Type.__name__ = "Integer32"
_EoACPwrAttributesWyeThdPhaseToNeutralVoltage_Object = MibTableColumn
eoACPwrAttributesWyeThdPhaseToNeutralVoltage = _EoACPwrAttributesWyeThdPhaseToNeutralVoltage_Object(
    (1, 3, 6, 1, 2, 1, 230, 1, 3, 1, 9),
    _EoACPwrAttributesWyeThdPhaseToNeutralVoltage_Type()
)
eoACPwrAttributesWyeThdPhaseToNeutralVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoACPwrAttributesWyeThdPhaseToNeutralVoltage.setStatus("current")
if mibBuilder.loadTexts:
    eoACPwrAttributesWyeThdPhaseToNeutralVoltage.setUnits("hundredths of percent")
_PowerAttributesMIBCompliances_ObjectIdentity = ObjectIdentity
powerAttributesMIBCompliances = _PowerAttributesMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 230, 2)
)
_PowerAttributesMIBGroups_ObjectIdentity = ObjectIdentity
powerAttributesMIBGroups = _PowerAttributesMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 230, 3)
)

# Managed Objects groups

powerACPwrAttributesMIBTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 230, 3, 1)
)
powerACPwrAttributesMIBTableGroup.setObjects(
      *(("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesAvgVoltage"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesAvgCurrent"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesFrequency"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesPowerUnitMultiplier"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesPowerAccuracy"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesTotalActivePower"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesTotalReactivePower"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesTotalApparentPower"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesTotalPowerFactor"))
)
if mibBuilder.loadTexts:
    powerACPwrAttributesMIBTableGroup.setStatus("current")

powerACPwrAttributesOptionalMIBTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 230, 3, 2)
)
powerACPwrAttributesOptionalMIBTableGroup.setObjects(
      *(("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesConfiguration"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesThdCurrent"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesThdVoltage"))
)
if mibBuilder.loadTexts:
    powerACPwrAttributesOptionalMIBTableGroup.setStatus("current")

powerACPwrAttributesDelPhaseMIBTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 230, 3, 3)
)
powerACPwrAttributesDelPhaseMIBTableGroup.setObjects(
      *(("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesDelPhaseToNextPhaseVoltage"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesDelThdPhaseToNextPhaseVoltage"))
)
if mibBuilder.loadTexts:
    powerACPwrAttributesDelPhaseMIBTableGroup.setStatus("current")

powerACPwrAttributesWyePhaseMIBTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 230, 3, 4)
)
powerACPwrAttributesWyePhaseMIBTableGroup.setObjects(
      *(("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesWyePhaseToNeutralVoltage"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesWyeCurrent"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesWyeActivePower"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesWyeReactivePower"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesWyeApparentPower"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesWyePowerFactor"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesWyeThdPhaseToNeutralVoltage"),
        ("POWER-ATTRIBUTES-MIB", "eoACPwrAttributesWyeThdCurrent"))
)
if mibBuilder.loadTexts:
    powerACPwrAttributesWyePhaseMIBTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

powerAttributesMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 230, 2, 1)
)
if mibBuilder.loadTexts:
    powerAttributesMIBFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POWER-ATTRIBUTES-MIB",
    **{"powerAttributesMIB": powerAttributesMIB,
       "powerAttributesMIBConform": powerAttributesMIBConform,
       "powerAttributesMIBObjects": powerAttributesMIBObjects,
       "eoACPwrAttributesTable": eoACPwrAttributesTable,
       "eoACPwrAttributesEntry": eoACPwrAttributesEntry,
       "eoACPwrAttributesConfiguration": eoACPwrAttributesConfiguration,
       "eoACPwrAttributesAvgVoltage": eoACPwrAttributesAvgVoltage,
       "eoACPwrAttributesAvgCurrent": eoACPwrAttributesAvgCurrent,
       "eoACPwrAttributesFrequency": eoACPwrAttributesFrequency,
       "eoACPwrAttributesPowerUnitMultiplier": eoACPwrAttributesPowerUnitMultiplier,
       "eoACPwrAttributesPowerAccuracy": eoACPwrAttributesPowerAccuracy,
       "eoACPwrAttributesTotalActivePower": eoACPwrAttributesTotalActivePower,
       "eoACPwrAttributesTotalReactivePower": eoACPwrAttributesTotalReactivePower,
       "eoACPwrAttributesTotalApparentPower": eoACPwrAttributesTotalApparentPower,
       "eoACPwrAttributesTotalPowerFactor": eoACPwrAttributesTotalPowerFactor,
       "eoACPwrAttributesThdCurrent": eoACPwrAttributesThdCurrent,
       "eoACPwrAttributesThdVoltage": eoACPwrAttributesThdVoltage,
       "eoACPwrAttributesDelPhaseTable": eoACPwrAttributesDelPhaseTable,
       "eoACPwrAttributesDelPhaseEntry": eoACPwrAttributesDelPhaseEntry,
       "eoACPwrAttributesDelPhaseIndex": eoACPwrAttributesDelPhaseIndex,
       "eoACPwrAttributesDelPhaseToNextPhaseVoltage": eoACPwrAttributesDelPhaseToNextPhaseVoltage,
       "eoACPwrAttributesDelThdPhaseToNextPhaseVoltage": eoACPwrAttributesDelThdPhaseToNextPhaseVoltage,
       "eoACPwrAttributesWyePhaseTable": eoACPwrAttributesWyePhaseTable,
       "eoACPwrAttributesWyePhaseEntry": eoACPwrAttributesWyePhaseEntry,
       "eoACPwrAttributesWyePhaseIndex": eoACPwrAttributesWyePhaseIndex,
       "eoACPwrAttributesWyePhaseToNeutralVoltage": eoACPwrAttributesWyePhaseToNeutralVoltage,
       "eoACPwrAttributesWyeCurrent": eoACPwrAttributesWyeCurrent,
       "eoACPwrAttributesWyeActivePower": eoACPwrAttributesWyeActivePower,
       "eoACPwrAttributesWyeReactivePower": eoACPwrAttributesWyeReactivePower,
       "eoACPwrAttributesWyeApparentPower": eoACPwrAttributesWyeApparentPower,
       "eoACPwrAttributesWyePowerFactor": eoACPwrAttributesWyePowerFactor,
       "eoACPwrAttributesWyeThdCurrent": eoACPwrAttributesWyeThdCurrent,
       "eoACPwrAttributesWyeThdPhaseToNeutralVoltage": eoACPwrAttributesWyeThdPhaseToNeutralVoltage,
       "powerAttributesMIBCompliances": powerAttributesMIBCompliances,
       "powerAttributesMIBFullCompliance": powerAttributesMIBFullCompliance,
       "powerAttributesMIBGroups": powerAttributesMIBGroups,
       "powerACPwrAttributesMIBTableGroup": powerACPwrAttributesMIBTableGroup,
       "powerACPwrAttributesOptionalMIBTableGroup": powerACPwrAttributesOptionalMIBTableGroup,
       "powerACPwrAttributesDelPhaseMIBTableGroup": powerACPwrAttributesDelPhaseMIBTableGroup,
       "powerACPwrAttributesWyePhaseMIBTableGroup": powerACPwrAttributesWyePhaseMIBTableGroup}
)
