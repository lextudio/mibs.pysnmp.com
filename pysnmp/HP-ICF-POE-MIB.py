# SNMP MIB module (HP-ICF-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-POE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:59 2024
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

(hpicfCommon,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfCommon")

(pethMainPseEntry,
 pethPsePortEntry) = mibBuilder.importSymbols(
    "POWER-ETHERNET-MIB",
    "pethMainPseEntry",
    "pethPsePortEntry")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfPoe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1)
)
hpicfPoe.setRevisions(
        ("2017-01-30 00:00",
         "2016-09-12 00:00",
         "2016-05-02 00:00",
         "2016-02-12 00:00",
         "2015-07-14 00:00",
         "2013-06-16 00:00",
         "2012-04-27 00:00",
         "2012-03-02 00:00",
         "2010-05-26 10:36",
         "2009-11-18 00:00",
         "2007-02-01 00:00",
         "2005-06-06 00:00",
         "2004-07-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfPOE_ObjectIdentity = ObjectIdentity
hpicfPOE = _HpicfPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9)
)
_HpicfPoePethPsePortTable_Object = MibTable
hpicfPoePethPsePortTable = _HpicfPoePethPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfPoePethPsePortTable.setStatus("current")
_HpicfPoePethPsePortEntry_Object = MibTableRow
hpicfPoePethPsePortEntry = _HpicfPoePethPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfPoePethPsePortEntry.setStatus("current")


class _HpicfPoePethPsePortCurrent_Type(Integer32):
    """Custom type hpicfPoePethPsePortCurrent based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfPoePethPsePortCurrent_Type.__name__ = "Integer32"
_HpicfPoePethPsePortCurrent_Object = MibTableColumn
hpicfPoePethPsePortCurrent = _HpicfPoePethPsePortCurrent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1, 1, 1),
    _HpicfPoePethPsePortCurrent_Type()
)
hpicfPoePethPsePortCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortCurrent.setStatus("current")


class _HpicfPoePethPsePortVoltage_Type(Integer32):
    """Custom type hpicfPoePethPsePortVoltage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfPoePethPsePortVoltage_Type.__name__ = "Integer32"
_HpicfPoePethPsePortVoltage_Object = MibTableColumn
hpicfPoePethPsePortVoltage = _HpicfPoePethPsePortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1, 1, 2),
    _HpicfPoePethPsePortVoltage_Type()
)
hpicfPoePethPsePortVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortVoltage.setStatus("current")


class _HpicfPoePethPsePortPower_Type(Integer32):
    """Custom type hpicfPoePethPsePortPower based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfPoePethPsePortPower_Type.__name__ = "Integer32"
_HpicfPoePethPsePortPower_Object = MibTableColumn
hpicfPoePethPsePortPower = _HpicfPoePethPsePortPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1, 1, 3),
    _HpicfPoePethPsePortPower_Type()
)
hpicfPoePethPsePortPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortPower.setStatus("current")


class _HpicfPoePethPsePortPowerAllocateBy_Type(Integer32):
    """Custom type hpicfPoePethPsePortPowerAllocateBy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("class", 2),
          ("usage", 1),
          ("value", 3))
    )


_HpicfPoePethPsePortPowerAllocateBy_Type.__name__ = "Integer32"
_HpicfPoePethPsePortPowerAllocateBy_Object = MibTableColumn
hpicfPoePethPsePortPowerAllocateBy = _HpicfPoePethPsePortPowerAllocateBy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1, 1, 4),
    _HpicfPoePethPsePortPowerAllocateBy_Type()
)
hpicfPoePethPsePortPowerAllocateBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortPowerAllocateBy.setStatus("current")


class _HpicfPoePethPsePortPowerValue_Type(Integer32):
    """Custom type hpicfPoePethPsePortPowerValue based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 17),
    )


_HpicfPoePethPsePortPowerValue_Type.__name__ = "Integer32"
_HpicfPoePethPsePortPowerValue_Object = MibTableColumn
hpicfPoePethPsePortPowerValue = _HpicfPoePethPsePortPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1, 1, 5),
    _HpicfPoePethPsePortPowerValue_Type()
)
hpicfPoePethPsePortPowerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortPowerValue.setStatus("current")


class _HpicfPoePethPsePortLLDPDetect_Type(Integer32):
    """Custom type hpicfPoePethPsePortLLDPDetect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HpicfPoePethPsePortLLDPDetect_Type.__name__ = "Integer32"
_HpicfPoePethPsePortLLDPDetect_Object = MibTableColumn
hpicfPoePethPsePortLLDPDetect = _HpicfPoePethPsePortLLDPDetect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1, 1, 6),
    _HpicfPoePethPsePortLLDPDetect_Type()
)
hpicfPoePethPsePortLLDPDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortLLDPDetect.setStatus("current")


class _HpicfPoePethPsePortPoePlusPowerValue_Type(Integer32):
    """Custom type hpicfPoePethPsePortPoePlusPowerValue based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfPoePethPsePortPoePlusPowerValue_Type.__name__ = "Integer32"
_HpicfPoePethPsePortPoePlusPowerValue_Object = MibTableColumn
hpicfPoePethPsePortPoePlusPowerValue = _HpicfPoePethPsePortPoePlusPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1, 1, 7),
    _HpicfPoePethPsePortPoePlusPowerValue_Type()
)
hpicfPoePethPsePortPoePlusPowerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortPoePlusPowerValue.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortPoePlusPowerValue.setUnits("Watts")


class _HpicfPoePethPsePortActualPower_Type(Integer32):
    """Custom type hpicfPoePethPsePortActualPower based on Integer32"""
    defaultValue = 0


_HpicfPoePethPsePortActualPower_Object = MibTableColumn
hpicfPoePethPsePortActualPower = _HpicfPoePethPsePortActualPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1, 1, 8),
    _HpicfPoePethPsePortActualPower_Type()
)
hpicfPoePethPsePortActualPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortActualPower.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortActualPower.setUnits("milli-watts")


class _HpicfPoePethPsePortOperStatus_Type(Integer32):
    """Custom type hpicfPoePethPsePortOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("off", 2),
          ("on", 3))
    )


_HpicfPoePethPsePortOperStatus_Type.__name__ = "Integer32"
_HpicfPoePethPsePortOperStatus_Object = MibTableColumn
hpicfPoePethPsePortOperStatus = _HpicfPoePethPsePortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1, 1, 9),
    _HpicfPoePethPsePortOperStatus_Type()
)
hpicfPoePethPsePortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortOperStatus.setStatus("current")


class _HpicfPoePethPsePortPowerMode_Type(Integer32):
    """Custom type hpicfPoePethPsePortPowerMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("disableWithFiber", 6),
          ("enable", 1))
    )


_HpicfPoePethPsePortPowerMode_Type.__name__ = "Integer32"
_HpicfPoePethPsePortPowerMode_Object = MibTableColumn
hpicfPoePethPsePortPowerMode = _HpicfPoePethPsePortPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1, 1, 10),
    _HpicfPoePethPsePortPowerMode_Type()
)
hpicfPoePethPsePortPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortPowerMode.setStatus("current")


class _HpicfPoePethPsePortAveragePower_Type(Integer32):
    """Custom type hpicfPoePethPsePortAveragePower based on Integer32"""
    defaultValue = 0


_HpicfPoePethPsePortAveragePower_Object = MibTableColumn
hpicfPoePethPsePortAveragePower = _HpicfPoePethPsePortAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1, 1, 11),
    _HpicfPoePethPsePortAveragePower_Type()
)
hpicfPoePethPsePortAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortAveragePower.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortAveragePower.setUnits("watts")


class _HpicfPoePethPsePortPeakPower_Type(Integer32):
    """Custom type hpicfPoePethPsePortPeakPower based on Integer32"""
    defaultValue = 0


_HpicfPoePethPsePortPeakPower_Object = MibTableColumn
hpicfPoePethPsePortPeakPower = _HpicfPoePethPsePortPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1, 1, 12),
    _HpicfPoePethPsePortPeakPower_Type()
)
hpicfPoePethPsePortPeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortPeakPower.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortPeakPower.setUnits("watts")


class _HpicfPoePethPsePortPreStdDetect_Type(Integer32):
    """Custom type hpicfPoePethPsePortPreStdDetect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HpicfPoePethPsePortPreStdDetect_Type.__name__ = "Integer32"
_HpicfPoePethPsePortPreStdDetect_Object = MibTableColumn
hpicfPoePethPsePortPreStdDetect = _HpicfPoePethPsePortPreStdDetect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1, 1, 13),
    _HpicfPoePethPsePortPreStdDetect_Type()
)
hpicfPoePethPsePortPreStdDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortPreStdDetect.setStatus("current")


class _HpicfPoePethPsePortLowPriority_Type(Integer32):
    """Custom type hpicfPoePethPsePortLowPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_HpicfPoePethPsePortLowPriority_Type.__name__ = "Integer32"
_HpicfPoePethPsePortLowPriority_Object = MibTableColumn
hpicfPoePethPsePortLowPriority = _HpicfPoePethPsePortLowPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1, 1, 14),
    _HpicfPoePethPsePortLowPriority_Type()
)
hpicfPoePethPsePortLowPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortLowPriority.setStatus("current")


class _HpicfPoePethPsePortResetState_Type(Integer32):
    """Custom type hpicfPoePethPsePortResetState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 0),
          ("reset", 1))
    )


_HpicfPoePethPsePortResetState_Type.__name__ = "Integer32"
_HpicfPoePethPsePortResetState_Object = MibTableColumn
hpicfPoePethPsePortResetState = _HpicfPoePethPsePortResetState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1, 1, 15),
    _HpicfPoePethPsePortResetState_Type()
)
hpicfPoePethPsePortResetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortResetState.setStatus("current")


class _HpicfPoePethPsePortPowerType_Type(Integer32):
    """Custom type hpicfPoePethPsePortPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type0", -1),
          ("type1", 1),
          ("type2", 2))
    )


_HpicfPoePethPsePortPowerType_Type.__name__ = "Integer32"
_HpicfPoePethPsePortPowerType_Object = MibTableColumn
hpicfPoePethPsePortPowerType = _HpicfPoePethPsePortPowerType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 1, 1, 16),
    _HpicfPoePethPsePortPowerType_Type()
)
hpicfPoePethPsePortPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortPowerType.setStatus("current")
_HpicfPoeConformance_ObjectIdentity = ObjectIdentity
hpicfPoeConformance = _HpicfPoeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2)
)
_HpicfPoeCompliances_ObjectIdentity = ObjectIdentity
hpicfPoeCompliances = _HpicfPoeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 1)
)
_HpicfPoeGroups_ObjectIdentity = ObjectIdentity
hpicfPoeGroups = _HpicfPoeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 2)
)
_HpicfPoeAllowPreStdDetect_Type = TruthValue
_HpicfPoeAllowPreStdDetect_Object = MibScalar
hpicfPoeAllowPreStdDetect = _HpicfPoeAllowPreStdDetect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 3),
    _HpicfPoeAllowPreStdDetect_Type()
)
hpicfPoeAllowPreStdDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPoeAllowPreStdDetect.setStatus("deprecated")


class _HpicfPoePowerRedundancy_Type(Integer32):
    """Custom type hpicfPoePowerRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("nPlus1", 2),
          ("none", 1))
    )


_HpicfPoePowerRedundancy_Type.__name__ = "Integer32"
_HpicfPoePowerRedundancy_Object = MibScalar
hpicfPoePowerRedundancy = _HpicfPoePowerRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 4),
    _HpicfPoePowerRedundancy_Type()
)
hpicfPoePowerRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPoePowerRedundancy.setStatus("deprecated")


class _HpicfPoeExtPwrSupplyCount_Type(Integer32):
    """Custom type hpicfPoeExtPwrSupplyCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpicfPoeExtPwrSupplyCount_Type.__name__ = "Integer32"
_HpicfPoeExtPwrSupplyCount_Object = MibScalar
hpicfPoeExtPwrSupplyCount = _HpicfPoeExtPwrSupplyCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 5),
    _HpicfPoeExtPwrSupplyCount_Type()
)
hpicfPoeExtPwrSupplyCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPoeExtPwrSupplyCount.setStatus("deprecated")
_HpicfPseFeaturesTable_Object = MibTable
hpicfPseFeaturesTable = _HpicfPseFeaturesTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfPseFeaturesTable.setStatus("current")
_HpicfPseFeaturesEntry_Object = MibTableRow
hpicfPseFeaturesEntry = _HpicfPseFeaturesEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 6, 1)
)
hpicfPseFeaturesEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpicfPseFeaturesEntry.setStatus("current")
_HpicfPseAllowPreStdDetect_Type = TruthValue
_HpicfPseAllowPreStdDetect_Object = MibTableColumn
hpicfPseAllowPreStdDetect = _HpicfPseAllowPreStdDetect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 6, 1, 1),
    _HpicfPseAllowPreStdDetect_Type()
)
hpicfPseAllowPreStdDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPseAllowPreStdDetect.setStatus("deprecated")


class _HpicfPsePowerRedundancy_Type(Integer32):
    """Custom type hpicfPsePowerRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("nPlus1", 2),
          ("none", 1))
    )


_HpicfPsePowerRedundancy_Type.__name__ = "Integer32"
_HpicfPsePowerRedundancy_Object = MibTableColumn
hpicfPsePowerRedundancy = _HpicfPsePowerRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 6, 1, 2),
    _HpicfPsePowerRedundancy_Type()
)
hpicfPsePowerRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPsePowerRedundancy.setStatus("current")


class _HpicfPseExtPwrSupplyCount_Type(Integer32):
    """Custom type hpicfPseExtPwrSupplyCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpicfPseExtPwrSupplyCount_Type.__name__ = "Integer32"
_HpicfPseExtPwrSupplyCount_Object = MibTableColumn
hpicfPseExtPwrSupplyCount = _HpicfPseExtPwrSupplyCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 6, 1, 3),
    _HpicfPseExtPwrSupplyCount_Type()
)
hpicfPseExtPwrSupplyCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPseExtPwrSupplyCount.setStatus("current")


class _HpicfPseAvailablePower_Type(Integer32):
    """Custom type hpicfPseAvailablePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfPseAvailablePower_Type.__name__ = "Integer32"
_HpicfPseAvailablePower_Object = MibTableColumn
hpicfPseAvailablePower = _HpicfPseAvailablePower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 6, 1, 4),
    _HpicfPseAvailablePower_Type()
)
hpicfPseAvailablePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPseAvailablePower.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPseAvailablePower.setUnits("Watts")


class _HpicfPseUsedPower_Type(Integer32):
    """Custom type hpicfPseUsedPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfPseUsedPower_Type.__name__ = "Integer32"
_HpicfPseUsedPower_Object = MibTableColumn
hpicfPseUsedPower = _HpicfPseUsedPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 6, 1, 5),
    _HpicfPseUsedPower_Type()
)
hpicfPseUsedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPseUsedPower.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPseUsedPower.setUnits("Watts")


class _HpicfPseFailoverPower_Type(Integer32):
    """Custom type hpicfPseFailoverPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfPseFailoverPower_Type.__name__ = "Integer32"
_HpicfPseFailoverPower_Object = MibTableColumn
hpicfPseFailoverPower = _HpicfPseFailoverPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 6, 1, 6),
    _HpicfPseFailoverPower_Type()
)
hpicfPseFailoverPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPseFailoverPower.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPseFailoverPower.setUnits("Watts")


class _HpicfPseRedundantPower_Type(Integer32):
    """Custom type hpicfPseRedundantPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfPseRedundantPower_Type.__name__ = "Integer32"
_HpicfPseRedundantPower_Object = MibTableColumn
hpicfPseRedundantPower = _HpicfPseRedundantPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 6, 1, 7),
    _HpicfPseRedundantPower_Type()
)
hpicfPseRedundantPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPseRedundantPower.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPseRedundantPower.setUnits("Watts")


class _HpicfPseCurrentPowerDraw_Type(Integer32):
    """Custom type hpicfPseCurrentPowerDraw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfPseCurrentPowerDraw_Type.__name__ = "Integer32"
_HpicfPseCurrentPowerDraw_Object = MibTableColumn
hpicfPseCurrentPowerDraw = _HpicfPseCurrentPowerDraw_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 6, 1, 8),
    _HpicfPseCurrentPowerDraw_Type()
)
hpicfPseCurrentPowerDraw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPseCurrentPowerDraw.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPseCurrentPowerDraw.setUnits("Watts")
_HpicfPoePowerSupplyTable_Object = MibTable
hpicfPoePowerSupplyTable = _HpicfPoePowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 7)
)
if mibBuilder.loadTexts:
    hpicfPoePowerSupplyTable.setStatus("current")
_HpicfPoePowerSupplyEntry_Object = MibTableRow
hpicfPoePowerSupplyEntry = _HpicfPoePowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 7, 1)
)
hpicfPoePowerSupplyEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpicfPoePowerSupplyEntry.setStatus("current")


class _HpicfPoePowerSupplySourceType_Type(Integer32):
    """Custom type hpicfPoePowerSupplySourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_HpicfPoePowerSupplySourceType_Type.__name__ = "Integer32"
_HpicfPoePowerSupplySourceType_Object = MibTableColumn
hpicfPoePowerSupplySourceType = _HpicfPoePowerSupplySourceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 7, 1, 1),
    _HpicfPoePowerSupplySourceType_Type()
)
hpicfPoePowerSupplySourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePowerSupplySourceType.setStatus("current")


class _HpicfPoePowerSupplyType_Type(Integer32):
    """Custom type hpicfPoePowerSupplyType based on Integer32"""
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
        *(("auxFault", 5),
          ("fault", 4),
          ("notPresent", 3),
          ("poe", 1),
          ("poePlus", 2))
    )


_HpicfPoePowerSupplyType_Type.__name__ = "Integer32"
_HpicfPoePowerSupplyType_Object = MibTableColumn
hpicfPoePowerSupplyType = _HpicfPoePowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 7, 1, 2),
    _HpicfPoePowerSupplyType_Type()
)
hpicfPoePowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePowerSupplyType.setStatus("current")


class _HpicfPoePowerSupplyCapacity_Type(Integer32):
    """Custom type hpicfPoePowerSupplyCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfPoePowerSupplyCapacity_Type.__name__ = "Integer32"
_HpicfPoePowerSupplyCapacity_Object = MibTableColumn
hpicfPoePowerSupplyCapacity = _HpicfPoePowerSupplyCapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 7, 1, 3),
    _HpicfPoePowerSupplyCapacity_Type()
)
hpicfPoePowerSupplyCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePowerSupplyCapacity.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPoePowerSupplyCapacity.setUnits("Watts")


class _HpicfPoePowerSupplyAuxCapacity_Type(Integer32):
    """Custom type hpicfPoePowerSupplyAuxCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HpicfPoePowerSupplyAuxCapacity_Type.__name__ = "Integer32"
_HpicfPoePowerSupplyAuxCapacity_Object = MibTableColumn
hpicfPoePowerSupplyAuxCapacity = _HpicfPoePowerSupplyAuxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 7, 1, 4),
    _HpicfPoePowerSupplyAuxCapacity_Type()
)
hpicfPoePowerSupplyAuxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePowerSupplyAuxCapacity.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPoePowerSupplyAuxCapacity.setUnits("Watts")
_HpicfPoePethPseOperStateTable_Object = MibTable
hpicfPoePethPseOperStateTable = _HpicfPoePethPseOperStateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 8)
)
if mibBuilder.loadTexts:
    hpicfPoePethPseOperStateTable.setStatus("current")
_HpicfPoePethPseOperStateEntry_Object = MibTableRow
hpicfPoePethPseOperStateEntry = _HpicfPoePethPseOperStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 8, 1)
)
if mibBuilder.loadTexts:
    hpicfPoePethPseOperStateEntry.setStatus("current")


class _HpicfPoePethPseOperState_Type(Integer32):
    """Custom type hpicfPoePethPseOperState based on Integer32"""
    defaultValue = 1

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
        *(("fault", 4),
          ("off", 3),
          ("poeOn", 1),
          ("poePlusOn", 2))
    )


_HpicfPoePethPseOperState_Type.__name__ = "Integer32"
_HpicfPoePethPseOperState_Object = MibTableColumn
hpicfPoePethPseOperState = _HpicfPoePethPseOperState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 8, 1, 1),
    _HpicfPoePethPseOperState_Type()
)
hpicfPoePethPseOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePethPseOperState.setStatus("current")


class _HpicfPoePethPsePortNum_Type(Integer32):
    """Custom type hpicfPoePethPsePortNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfPoePethPsePortNum_Type.__name__ = "Integer32"
_HpicfPoePethPsePortNum_Object = MibTableColumn
hpicfPoePethPsePortNum = _HpicfPoePethPsePortNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 8, 1, 2),
    _HpicfPoePethPsePortNum_Type()
)
hpicfPoePethPsePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePethPsePortNum.setStatus("current")


class _HpicfPoePethMainPsePdPowerDraw_Type(Integer32):
    """Custom type hpicfPoePethMainPsePdPowerDraw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfPoePethMainPsePdPowerDraw_Type.__name__ = "Integer32"
_HpicfPoePethMainPsePdPowerDraw_Object = MibTableColumn
hpicfPoePethMainPsePdPowerDraw = _HpicfPoePethMainPsePdPowerDraw_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 8, 1, 3),
    _HpicfPoePethMainPsePdPowerDraw_Type()
)
hpicfPoePethMainPsePdPowerDraw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePethMainPsePdPowerDraw.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPoePethMainPsePdPowerDraw.setUnits("Watts")
_HpicfPoeMaxGuaranteedPower_Type = Integer32
_HpicfPoeMaxGuaranteedPower_Object = MibScalar
hpicfPoeMaxGuaranteedPower = _HpicfPoeMaxGuaranteedPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 9),
    _HpicfPoeMaxGuaranteedPower_Type()
)
hpicfPoeMaxGuaranteedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoeMaxGuaranteedPower.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPoeMaxGuaranteedPower.setUnits("watts")
_HpicfPoeRemainingGuaranteedPower_Type = Integer32
_HpicfPoeRemainingGuaranteedPower_Object = MibScalar
hpicfPoeRemainingGuaranteedPower = _HpicfPoeRemainingGuaranteedPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 10),
    _HpicfPoeRemainingGuaranteedPower_Type()
)
hpicfPoeRemainingGuaranteedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoeRemainingGuaranteedPower.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPoeRemainingGuaranteedPower.setUnits("watts")
_HpicfPoePethPsePowerTable_Object = MibTable
hpicfPoePethPsePowerTable = _HpicfPoePethPsePowerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 11)
)
if mibBuilder.loadTexts:
    hpicfPoePethPsePowerTable.setStatus("current")
_HpicfPoePethPsePowerEntry_Object = MibTableRow
hpicfPoePethPsePowerEntry = _HpicfPoePethPsePowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 11, 1)
)
if mibBuilder.loadTexts:
    hpicfPoePethPsePowerEntry.setStatus("current")
_HpicfPoePethPsePeakPower_Type = Integer32
_HpicfPoePethPsePeakPower_Object = MibTableColumn
hpicfPoePethPsePeakPower = _HpicfPoePethPsePeakPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 11, 1, 1),
    _HpicfPoePethPsePeakPower_Type()
)
hpicfPoePethPsePeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePethPsePeakPower.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPoePethPsePeakPower.setUnits("Watts")
_HpicfPoePethPseAvgPower_Type = Integer32
_HpicfPoePethPseAvgPower_Object = MibTableColumn
hpicfPoePethPseAvgPower = _HpicfPoePethPseAvgPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 11, 1, 2),
    _HpicfPoePethPseAvgPower_Type()
)
hpicfPoePethPseAvgPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePethPseAvgPower.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPoePethPseAvgPower.setUnits("Watts")
_HpicfPoePethPseRemGrntPower_Type = Integer32
_HpicfPoePethPseRemGrntPower_Object = MibTableColumn
hpicfPoePethPseRemGrntPower = _HpicfPoePethPseRemGrntPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 11, 1, 3),
    _HpicfPoePethPseRemGrntPower_Type()
)
hpicfPoePethPseRemGrntPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPoePethPseRemGrntPower.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPoePethPseRemGrntPower.setUnits("Watts")
pethPsePortEntry.registerAugmentions(
    ("HP-ICF-POE-MIB",
     "hpicfPoePethPsePortEntry")
)
hpicfPoePethPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
pethMainPseEntry.registerAugmentions(
    ("HP-ICF-POE-MIB",
     "hpicfPoePethPseOperStateEntry")
)
hpicfPoePethPseOperStateEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
pethMainPseEntry.registerAugmentions(
    ("HP-ICF-POE-MIB",
     "hpicfPoePethPsePowerEntry")
)
hpicfPoePethPsePowerEntry.setIndexNames(*pethMainPseEntry.getIndexNames())

# Managed Objects groups

hpicfPoePethPsePortTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 2, 1)
)
hpicfPoePethPsePortTableGroup.setObjects(
      *(("HP-ICF-POE-MIB", "hpicfPoePethPsePortCurrent"),
        ("HP-ICF-POE-MIB", "hpicfPoePethPsePortVoltage"),
        ("HP-ICF-POE-MIB", "hpicfPoePethPsePortPower"),
        ("HP-ICF-POE-MIB", "hpicfPoePethPsePortPowerAllocateBy"),
        ("HP-ICF-POE-MIB", "hpicfPoePethPsePortPowerValue"),
        ("HP-ICF-POE-MIB", "hpicfPoePethPsePortLLDPDetect"),
        ("HP-ICF-POE-MIB", "hpicfPoePethPsePortPoePlusPowerValue"),
        ("HP-ICF-POE-MIB", "hpicfPoePethPsePortActualPower"),
        ("HP-ICF-POE-MIB", "hpicfPoePethPsePortOperStatus"),
        ("HP-ICF-POE-MIB", "hpicfPoePethPsePortPowerMode"),
        ("HP-ICF-POE-MIB", "hpicfPoePethPsePortAveragePower"),
        ("HP-ICF-POE-MIB", "hpicfPoePethPsePortPeakPower"))
)
if mibBuilder.loadTexts:
    hpicfPoePethPsePortTableGroup.setStatus("current")

hpicfPoeGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 2, 2)
)
hpicfPoeGlobalGroup.setObjects(
      *(("HP-ICF-POE-MIB", "hpicfPoeAllowPreStdDetect"),
        ("HP-ICF-POE-MIB", "hpicfPoePowerRedundancy"),
        ("HP-ICF-POE-MIB", "hpicfPoeExtPwrSupplyCount"))
)
if mibBuilder.loadTexts:
    hpicfPoeGlobalGroup.setStatus("deprecated")

hpicfPseFeaturesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 2, 3)
)
hpicfPseFeaturesGroup.setObjects(
      *(("HP-ICF-POE-MIB", "hpicfPseAllowPreStdDetect"),
        ("HP-ICF-POE-MIB", "hpicfPsePowerRedundancy"),
        ("HP-ICF-POE-MIB", "hpicfPseExtPwrSupplyCount"),
        ("HP-ICF-POE-MIB", "hpicfPseAvailablePower"),
        ("HP-ICF-POE-MIB", "hpicfPseUsedPower"),
        ("HP-ICF-POE-MIB", "hpicfPseFailoverPower"),
        ("HP-ICF-POE-MIB", "hpicfPseRedundantPower"))
)
if mibBuilder.loadTexts:
    hpicfPseFeaturesGroup.setStatus("deprecated")

hpicfPoePowerSupplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 2, 4)
)
hpicfPoePowerSupplyGroup.setObjects(
      *(("HP-ICF-POE-MIB", "hpicfPoePowerSupplySourceType"),
        ("HP-ICF-POE-MIB", "hpicfPoePowerSupplyType"),
        ("HP-ICF-POE-MIB", "hpicfPoePowerSupplyCapacity"))
)
if mibBuilder.loadTexts:
    hpicfPoePowerSupplyGroup.setStatus("current")

hpicfPoePethPseOperStateTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 2, 5)
)
hpicfPoePethPseOperStateTableGroup.setObjects(
      *(("HP-ICF-POE-MIB", "hpicfPoePethPseOperState"),
        ("HP-ICF-POE-MIB", "hpicfPoePethPsePortNum"))
)
if mibBuilder.loadTexts:
    hpicfPoePethPseOperStateTableGroup.setStatus("deprecated")

hpicfPoePethPsePowerTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 2, 6)
)
hpicfPoePethPsePowerTableGroup.setObjects(
      *(("HP-ICF-POE-MIB", "hpicfPoePethPsePeakPower"),
        ("HP-ICF-POE-MIB", "hpicfPoePethPseAvgPower"),
        ("HP-ICF-POE-MIB", "hpicfPoePethPseRemGrntPower"))
)
if mibBuilder.loadTexts:
    hpicfPoePethPsePowerTableGroup.setStatus("current")

hpicfPoePowerUsageGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 2, 7)
)
hpicfPoePowerUsageGlobalGroup.setObjects(
      *(("HP-ICF-POE-MIB", "hpicfPoeMaxGuaranteedPower"),
        ("HP-ICF-POE-MIB", "hpicfPoeRemainingGuaranteedPower"))
)
if mibBuilder.loadTexts:
    hpicfPoePowerUsageGlobalGroup.setStatus("current")

hpicfPseParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 2, 8)
)
hpicfPseParamsGroup.setObjects(
      *(("HP-ICF-POE-MIB", "hpicfPsePowerRedundancy"),
        ("HP-ICF-POE-MIB", "hpicfPseExtPwrSupplyCount"),
        ("HP-ICF-POE-MIB", "hpicfPseAvailablePower"),
        ("HP-ICF-POE-MIB", "hpicfPseUsedPower"),
        ("HP-ICF-POE-MIB", "hpicfPseFailoverPower"),
        ("HP-ICF-POE-MIB", "hpicfPseRedundantPower"))
)
if mibBuilder.loadTexts:
    hpicfPseParamsGroup.setStatus("deprecated")

hpicfPoePethPsePortPreStdDetectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 2, 9)
)
hpicfPoePethPsePortPreStdDetectGroup.setObjects(
    ("HP-ICF-POE-MIB", "hpicfPoePethPsePortPreStdDetect")
)
if mibBuilder.loadTexts:
    hpicfPoePethPsePortPreStdDetectGroup.setStatus("current")

hpicfPoeAuxPowerSupplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 2, 10)
)
hpicfPoeAuxPowerSupplyGroup.setObjects(
    ("HP-ICF-POE-MIB", "hpicfPoePowerSupplyAuxCapacity")
)
if mibBuilder.loadTexts:
    hpicfPoeAuxPowerSupplyGroup.setStatus("current")

hpicfPoeLowPowerPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 2, 11)
)
hpicfPoeLowPowerPortGroup.setObjects(
    ("HP-ICF-POE-MIB", "hpicfPoePethPsePortLowPriority")
)
if mibBuilder.loadTexts:
    hpicfPoeLowPowerPortGroup.setStatus("current")

hpicfPseParamsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 2, 12)
)
hpicfPseParamsGroup1.setObjects(
      *(("HP-ICF-POE-MIB", "hpicfPsePowerRedundancy"),
        ("HP-ICF-POE-MIB", "hpicfPseExtPwrSupplyCount"),
        ("HP-ICF-POE-MIB", "hpicfPseAvailablePower"),
        ("HP-ICF-POE-MIB", "hpicfPseUsedPower"),
        ("HP-ICF-POE-MIB", "hpicfPseFailoverPower"),
        ("HP-ICF-POE-MIB", "hpicfPseRedundantPower"),
        ("HP-ICF-POE-MIB", "hpicfPseCurrentPowerDraw"))
)
if mibBuilder.loadTexts:
    hpicfPseParamsGroup1.setStatus("current")

hpicfPoePethPsePortPowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 2, 13)
)
hpicfPoePethPsePortPowerGroup.setObjects(
    ("HP-ICF-POE-MIB", "hpicfPoePethPsePortPowerType")
)
if mibBuilder.loadTexts:
    hpicfPoePethPsePortPowerGroup.setStatus("current")

hpicfPoePethPseOperStateTableGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 2, 14)
)
hpicfPoePethPseOperStateTableGroup1.setObjects(
      *(("HP-ICF-POE-MIB", "hpicfPoePethPseOperState"),
        ("HP-ICF-POE-MIB", "hpicfPoePethPsePortNum"),
        ("HP-ICF-POE-MIB", "hpicfPoePethMainPsePdPowerDraw"))
)
if mibBuilder.loadTexts:
    hpicfPoePethPseOperStateTableGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfPoeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfPoeCompliance.setStatus(
        "deprecated"
    )

hpicfPoeCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfPoeCompliance1.setStatus(
        "deprecated"
    )

hpicfPoeCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfPoeCompliance2.setStatus(
        "deprecated"
    )

hpicfPoeCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfPoeCompliance3.setStatus(
        "deprecated"
    )

hpicfPoeCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfPoeCompliance4.setStatus(
        "deprecated"
    )

hpicfPoeCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfPoeCompliance5.setStatus(
        "current"
    )

hpicfPoeCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hpicfPoeCompliance6.setStatus(
        "current"
    )

hpicfPoeCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hpicfPoeCompliance7.setStatus(
        "current"
    )

hpicfPoeCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    hpicfPoeCompliance8.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-POE-MIB",
    **{"hpicfPOE": hpicfPOE,
       "hpicfPoe": hpicfPoe,
       "hpicfPoePethPsePortTable": hpicfPoePethPsePortTable,
       "hpicfPoePethPsePortEntry": hpicfPoePethPsePortEntry,
       "hpicfPoePethPsePortCurrent": hpicfPoePethPsePortCurrent,
       "hpicfPoePethPsePortVoltage": hpicfPoePethPsePortVoltage,
       "hpicfPoePethPsePortPower": hpicfPoePethPsePortPower,
       "hpicfPoePethPsePortPowerAllocateBy": hpicfPoePethPsePortPowerAllocateBy,
       "hpicfPoePethPsePortPowerValue": hpicfPoePethPsePortPowerValue,
       "hpicfPoePethPsePortLLDPDetect": hpicfPoePethPsePortLLDPDetect,
       "hpicfPoePethPsePortPoePlusPowerValue": hpicfPoePethPsePortPoePlusPowerValue,
       "hpicfPoePethPsePortActualPower": hpicfPoePethPsePortActualPower,
       "hpicfPoePethPsePortOperStatus": hpicfPoePethPsePortOperStatus,
       "hpicfPoePethPsePortPowerMode": hpicfPoePethPsePortPowerMode,
       "hpicfPoePethPsePortAveragePower": hpicfPoePethPsePortAveragePower,
       "hpicfPoePethPsePortPeakPower": hpicfPoePethPsePortPeakPower,
       "hpicfPoePethPsePortPreStdDetect": hpicfPoePethPsePortPreStdDetect,
       "hpicfPoePethPsePortLowPriority": hpicfPoePethPsePortLowPriority,
       "hpicfPoePethPsePortResetState": hpicfPoePethPsePortResetState,
       "hpicfPoePethPsePortPowerType": hpicfPoePethPsePortPowerType,
       "hpicfPoeConformance": hpicfPoeConformance,
       "hpicfPoeCompliances": hpicfPoeCompliances,
       "hpicfPoeCompliance": hpicfPoeCompliance,
       "hpicfPoeCompliance1": hpicfPoeCompliance1,
       "hpicfPoeCompliance2": hpicfPoeCompliance2,
       "hpicfPoeCompliance3": hpicfPoeCompliance3,
       "hpicfPoeCompliance4": hpicfPoeCompliance4,
       "hpicfPoeCompliance5": hpicfPoeCompliance5,
       "hpicfPoeCompliance6": hpicfPoeCompliance6,
       "hpicfPoeCompliance7": hpicfPoeCompliance7,
       "hpicfPoeCompliance8": hpicfPoeCompliance8,
       "hpicfPoeGroups": hpicfPoeGroups,
       "hpicfPoePethPsePortTableGroup": hpicfPoePethPsePortTableGroup,
       "hpicfPoeGlobalGroup": hpicfPoeGlobalGroup,
       "hpicfPseFeaturesGroup": hpicfPseFeaturesGroup,
       "hpicfPoePowerSupplyGroup": hpicfPoePowerSupplyGroup,
       "hpicfPoePethPseOperStateTableGroup": hpicfPoePethPseOperStateTableGroup,
       "hpicfPoePethPsePowerTableGroup": hpicfPoePethPsePowerTableGroup,
       "hpicfPoePowerUsageGlobalGroup": hpicfPoePowerUsageGlobalGroup,
       "hpicfPseParamsGroup": hpicfPseParamsGroup,
       "hpicfPoePethPsePortPreStdDetectGroup": hpicfPoePethPsePortPreStdDetectGroup,
       "hpicfPoeAuxPowerSupplyGroup": hpicfPoeAuxPowerSupplyGroup,
       "hpicfPoeLowPowerPortGroup": hpicfPoeLowPowerPortGroup,
       "hpicfPseParamsGroup1": hpicfPseParamsGroup1,
       "hpicfPoePethPsePortPowerGroup": hpicfPoePethPsePortPowerGroup,
       "hpicfPoePethPseOperStateTableGroup1": hpicfPoePethPseOperStateTableGroup1,
       "hpicfPoeAllowPreStdDetect": hpicfPoeAllowPreStdDetect,
       "hpicfPoePowerRedundancy": hpicfPoePowerRedundancy,
       "hpicfPoeExtPwrSupplyCount": hpicfPoeExtPwrSupplyCount,
       "hpicfPseFeaturesTable": hpicfPseFeaturesTable,
       "hpicfPseFeaturesEntry": hpicfPseFeaturesEntry,
       "hpicfPseAllowPreStdDetect": hpicfPseAllowPreStdDetect,
       "hpicfPsePowerRedundancy": hpicfPsePowerRedundancy,
       "hpicfPseExtPwrSupplyCount": hpicfPseExtPwrSupplyCount,
       "hpicfPseAvailablePower": hpicfPseAvailablePower,
       "hpicfPseUsedPower": hpicfPseUsedPower,
       "hpicfPseFailoverPower": hpicfPseFailoverPower,
       "hpicfPseRedundantPower": hpicfPseRedundantPower,
       "hpicfPseCurrentPowerDraw": hpicfPseCurrentPowerDraw,
       "hpicfPoePowerSupplyTable": hpicfPoePowerSupplyTable,
       "hpicfPoePowerSupplyEntry": hpicfPoePowerSupplyEntry,
       "hpicfPoePowerSupplySourceType": hpicfPoePowerSupplySourceType,
       "hpicfPoePowerSupplyType": hpicfPoePowerSupplyType,
       "hpicfPoePowerSupplyCapacity": hpicfPoePowerSupplyCapacity,
       "hpicfPoePowerSupplyAuxCapacity": hpicfPoePowerSupplyAuxCapacity,
       "hpicfPoePethPseOperStateTable": hpicfPoePethPseOperStateTable,
       "hpicfPoePethPseOperStateEntry": hpicfPoePethPseOperStateEntry,
       "hpicfPoePethPseOperState": hpicfPoePethPseOperState,
       "hpicfPoePethPsePortNum": hpicfPoePethPsePortNum,
       "hpicfPoePethMainPsePdPowerDraw": hpicfPoePethMainPsePdPowerDraw,
       "hpicfPoeMaxGuaranteedPower": hpicfPoeMaxGuaranteedPower,
       "hpicfPoeRemainingGuaranteedPower": hpicfPoeRemainingGuaranteedPower,
       "hpicfPoePethPsePowerTable": hpicfPoePethPsePowerTable,
       "hpicfPoePethPsePowerEntry": hpicfPoePethPsePowerEntry,
       "hpicfPoePethPsePeakPower": hpicfPoePethPsePeakPower,
       "hpicfPoePethPseAvgPower": hpicfPoePethPseAvgPower,
       "hpicfPoePethPseRemGrntPower": hpicfPoePethPseRemGrntPower}
)
