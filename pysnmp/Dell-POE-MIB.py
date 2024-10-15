# SNMP MIB module (Dell-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Dell-POE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:34:43 2024
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

(rnd,) = mibBuilder.importSymbols(
    "Dell-MIB",
    "rnd")

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

rlPoe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 108)
)
rlPoe.setRevisions(
        ("2010-06-02 00:00",
         "2009-11-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlPethPsePortTable_Object = MibTable
rlPethPsePortTable = _RlPethPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 1)
)
if mibBuilder.loadTexts:
    rlPethPsePortTable.setStatus("current")
_RlPethPsePortEntry_Object = MibTableRow
rlPethPsePortEntry = _RlPethPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 1, 1)
)
rlPethPsePortEntry.setIndexNames(
    (0, "Dell-POE-MIB", "rlPethPsePortGroupIndex"),
    (0, "Dell-POE-MIB", "rlPethPsePortIndex"),
)
if mibBuilder.loadTexts:
    rlPethPsePortEntry.setStatus("current")


class _RlPethPsePortGroupIndex_Type(Integer32):
    """Custom type rlPethPsePortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlPethPsePortGroupIndex_Type.__name__ = "Integer32"
_RlPethPsePortGroupIndex_Object = MibTableColumn
rlPethPsePortGroupIndex = _RlPethPsePortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 1, 1, 1),
    _RlPethPsePortGroupIndex_Type()
)
rlPethPsePortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPethPsePortGroupIndex.setStatus("current")


class _RlPethPsePortIndex_Type(Integer32):
    """Custom type rlPethPsePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlPethPsePortIndex_Type.__name__ = "Integer32"
_RlPethPsePortIndex_Object = MibTableColumn
rlPethPsePortIndex = _RlPethPsePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 1, 1, 2),
    _RlPethPsePortIndex_Type()
)
rlPethPsePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPethPsePortIndex.setStatus("current")


class _RlPethPsePortOutputVoltage_Type(Integer32):
    """Custom type rlPethPsePortOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPethPsePortOutputVoltage_Type.__name__ = "Integer32"
_RlPethPsePortOutputVoltage_Object = MibTableColumn
rlPethPsePortOutputVoltage = _RlPethPsePortOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 1, 1, 3),
    _RlPethPsePortOutputVoltage_Type()
)
rlPethPsePortOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPsePortOutputVoltage.setStatus("current")


class _RlPethPsePortOutputCurrent_Type(Integer32):
    """Custom type rlPethPsePortOutputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPethPsePortOutputCurrent_Type.__name__ = "Integer32"
_RlPethPsePortOutputCurrent_Object = MibTableColumn
rlPethPsePortOutputCurrent = _RlPethPsePortOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 1, 1, 4),
    _RlPethPsePortOutputCurrent_Type()
)
rlPethPsePortOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPsePortOutputCurrent.setStatus("current")


class _RlPethPsePortOutputPower_Type(Integer32):
    """Custom type rlPethPsePortOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPethPsePortOutputPower_Type.__name__ = "Integer32"
_RlPethPsePortOutputPower_Object = MibTableColumn
rlPethPsePortOutputPower = _RlPethPsePortOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 1, 1, 5),
    _RlPethPsePortOutputPower_Type()
)
rlPethPsePortOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPsePortOutputPower.setStatus("current")


class _RlPethPsePortPowerLimit_Type(Integer32):
    """Custom type rlPethPsePortPowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPethPsePortPowerLimit_Type.__name__ = "Integer32"
_RlPethPsePortPowerLimit_Object = MibTableColumn
rlPethPsePortPowerLimit = _RlPethPsePortPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 1, 1, 6),
    _RlPethPsePortPowerLimit_Type()
)
rlPethPsePortPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPethPsePortPowerLimit.setStatus("current")


class _RlPethPsePortStatus_Type(Integer32):
    """Custom type rlPethPsePortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPethPsePortStatus_Type.__name__ = "Integer32"
_RlPethPsePortStatus_Object = MibTableColumn
rlPethPsePortStatus = _RlPethPsePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 1, 1, 7),
    _RlPethPsePortStatus_Type()
)
rlPethPsePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPsePortStatus.setStatus("current")


class _RlPethPsePortStatusDescription_Type(DisplayString):
    """Custom type rlPethPsePortStatusDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RlPethPsePortStatusDescription_Type.__name__ = "DisplayString"
_RlPethPsePortStatusDescription_Object = MibTableColumn
rlPethPsePortStatusDescription = _RlPethPsePortStatusDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 1, 1, 8),
    _RlPethPsePortStatusDescription_Type()
)
rlPethPsePortStatusDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPsePortStatusDescription.setStatus("current")


class _RlPethPsePortOperPowerLimit_Type(Integer32):
    """Custom type rlPethPsePortOperPowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPethPsePortOperPowerLimit_Type.__name__ = "Integer32"
_RlPethPsePortOperPowerLimit_Object = MibTableColumn
rlPethPsePortOperPowerLimit = _RlPethPsePortOperPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 1, 1, 9),
    _RlPethPsePortOperPowerLimit_Type()
)
rlPethPsePortOperPowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPsePortOperPowerLimit.setStatus("current")
_RlPethPsePortSupportPoePlus_Type = TruthValue
_RlPethPsePortSupportPoePlus_Object = MibTableColumn
rlPethPsePortSupportPoePlus = _RlPethPsePortSupportPoePlus_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 1, 1, 10),
    _RlPethPsePortSupportPoePlus_Type()
)
rlPethPsePortSupportPoePlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPsePortSupportPoePlus.setStatus("current")


class _RlPethPsePortTimeRangeName_Type(DisplayString):
    """Custom type rlPethPsePortTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlPethPsePortTimeRangeName_Type.__name__ = "DisplayString"
_RlPethPsePortTimeRangeName_Object = MibTableColumn
rlPethPsePortTimeRangeName = _RlPethPsePortTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 1, 1, 11),
    _RlPethPsePortTimeRangeName_Type()
)
rlPethPsePortTimeRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPethPsePortTimeRangeName.setStatus("current")
_RlPethPsePortOperStatus_Type = TruthValue
_RlPethPsePortOperStatus_Object = MibTableColumn
rlPethPsePortOperStatus = _RlPethPsePortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 1, 1, 12),
    _RlPethPsePortOperStatus_Type()
)
rlPethPsePortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPsePortOperStatus.setStatus("current")


class _RlPethPsePortMaxPowerAllocAllowed_Type(Integer32):
    """Custom type rlPethPsePortMaxPowerAllocAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPethPsePortMaxPowerAllocAllowed_Type.__name__ = "Integer32"
_RlPethPsePortMaxPowerAllocAllowed_Object = MibTableColumn
rlPethPsePortMaxPowerAllocAllowed = _RlPethPsePortMaxPowerAllocAllowed_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 1, 1, 13),
    _RlPethPsePortMaxPowerAllocAllowed_Type()
)
rlPethPsePortMaxPowerAllocAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPsePortMaxPowerAllocAllowed.setStatus("current")
_RlPethPsePortSupportPoe_Type = TruthValue
_RlPethPsePortSupportPoe_Object = MibTableColumn
rlPethPsePortSupportPoe = _RlPethPsePortSupportPoe_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 1, 1, 14),
    _RlPethPsePortSupportPoe_Type()
)
rlPethPsePortSupportPoe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPsePortSupportPoe.setStatus("current")
_RlPethMainPseTable_Object = MibTable
rlPethMainPseTable = _RlPethMainPseTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 2)
)
if mibBuilder.loadTexts:
    rlPethMainPseTable.setStatus("current")
_RlPethMainPseEntry_Object = MibTableRow
rlPethMainPseEntry = _RlPethMainPseEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 2, 1)
)
rlPethMainPseEntry.setIndexNames(
    (0, "Dell-POE-MIB", "rlPethMainPseGroupIndex"),
)
if mibBuilder.loadTexts:
    rlPethMainPseEntry.setStatus("current")


class _RlPethMainPseGroupIndex_Type(Integer32):
    """Custom type rlPethMainPseGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlPethMainPseGroupIndex_Type.__name__ = "Integer32"
_RlPethMainPseGroupIndex_Object = MibTableColumn
rlPethMainPseGroupIndex = _RlPethMainPseGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 2, 1, 1),
    _RlPethMainPseGroupIndex_Type()
)
rlPethMainPseGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPethMainPseGroupIndex.setStatus("current")


class _RlPethMainPseSwVersion_Type(DisplayString):
    """Custom type rlPethMainPseSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlPethMainPseSwVersion_Type.__name__ = "DisplayString"
_RlPethMainPseSwVersion_Object = MibTableColumn
rlPethMainPseSwVersion = _RlPethMainPseSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 2, 1, 2),
    _RlPethMainPseSwVersion_Type()
)
rlPethMainPseSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethMainPseSwVersion.setStatus("current")


class _RlPethMainPseHwVersion_Type(DisplayString):
    """Custom type rlPethMainPseHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlPethMainPseHwVersion_Type.__name__ = "DisplayString"
_RlPethMainPseHwVersion_Object = MibTableColumn
rlPethMainPseHwVersion = _RlPethMainPseHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 2, 1, 3),
    _RlPethMainPseHwVersion_Type()
)
rlPethMainPseHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethMainPseHwVersion.setStatus("current")


class _RlPethMainPseHwType_Type(Integer32):
    """Custom type rlPethMainPseHwType based on Integer32"""
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
        *(("auto", 3),
          ("enhanced", 1),
          ("enhancedPlus", 5),
          ("nonPoe", 4),
          ("plus", 2))
    )


_RlPethMainPseHwType_Type.__name__ = "Integer32"
_RlPethMainPseHwType_Object = MibTableColumn
rlPethMainPseHwType = _RlPethMainPseHwType_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 2, 1, 4),
    _RlPethMainPseHwType_Type()
)
rlPethMainPseHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethMainPseHwType.setStatus("current")


class _RlPethMainPsePowerGuardBand_Type(Integer32):
    """Custom type rlPethMainPsePowerGuardBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPethMainPsePowerGuardBand_Type.__name__ = "Integer32"
_RlPethMainPsePowerGuardBand_Object = MibTableColumn
rlPethMainPsePowerGuardBand = _RlPethMainPsePowerGuardBand_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 2, 1, 5),
    _RlPethMainPsePowerGuardBand_Type()
)
rlPethMainPsePowerGuardBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethMainPsePowerGuardBand.setStatus("current")
_RlPethPowerPseTable_Object = MibTable
rlPethPowerPseTable = _RlPethPowerPseTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 3)
)
if mibBuilder.loadTexts:
    rlPethPowerPseTable.setStatus("current")
_RlPethPowerPseEntry_Object = MibTableRow
rlPethPowerPseEntry = _RlPethPowerPseEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 3, 1)
)
rlPethPowerPseEntry.setIndexNames(
    (0, "Dell-POE-MIB", "rlPethPowerPseGroupIndex"),
)
if mibBuilder.loadTexts:
    rlPethPowerPseEntry.setStatus("current")


class _RlPethPowerPseGroupIndex_Type(Integer32):
    """Custom type rlPethPowerPseGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlPethPowerPseGroupIndex_Type.__name__ = "Integer32"
_RlPethPowerPseGroupIndex_Object = MibTableColumn
rlPethPowerPseGroupIndex = _RlPethPowerPseGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 3, 1, 1),
    _RlPethPowerPseGroupIndex_Type()
)
rlPethPowerPseGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPethPowerPseGroupIndex.setStatus("current")


class _RlPethPowerPsePower_Type(Integer32):
    """Custom type rlPethPowerPsePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ps1", 1),
          ("ps2", 2),
          ("ps3", 3))
    )


_RlPethPowerPsePower_Type.__name__ = "Integer32"
_RlPethPowerPsePower_Object = MibTableColumn
rlPethPowerPsePower = _RlPethPowerPsePower_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 3, 1, 2),
    _RlPethPowerPsePower_Type()
)
rlPethPowerPsePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPethPowerPsePower.setStatus("current")


class _RlPethPowerPseRpsPower_Type(Integer32):
    """Custom type rlPethPowerPseRpsPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rps1", 1),
          ("rps2", 2),
          ("rps3", 3))
    )


_RlPethPowerPseRpsPower_Type.__name__ = "Integer32"
_RlPethPowerPseRpsPower_Object = MibTableColumn
rlPethPowerPseRpsPower = _RlPethPowerPseRpsPower_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 3, 1, 3),
    _RlPethPowerPseRpsPower_Type()
)
rlPethPowerPseRpsPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPethPowerPseRpsPower.setStatus("current")


class _RlPethPowerPsePowerManagementMode_Type(Integer32):
    """Custom type rlPethPowerPsePowerManagementMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("classlimit", 5),
          ("maxlimit", 6),
          ("portlimit", 0))
    )


_RlPethPowerPsePowerManagementMode_Type.__name__ = "Integer32"
_RlPethPowerPsePowerManagementMode_Object = MibTableColumn
rlPethPowerPsePowerManagementMode = _RlPethPowerPsePowerManagementMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 3, 1, 4),
    _RlPethPowerPsePowerManagementMode_Type()
)
rlPethPowerPsePowerManagementMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPethPowerPsePowerManagementMode.setStatus("current")


class _RlPethPowerPsedisconnectMethod_Type(Integer32):
    """Custom type rlPethPowerPsedisconnectMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lowestpriority", 0),
          ("nextport", 1))
    )


_RlPethPowerPsedisconnectMethod_Type.__name__ = "Integer32"
_RlPethPowerPsedisconnectMethod_Object = MibTableColumn
rlPethPowerPsedisconnectMethod = _RlPethPowerPsedisconnectMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 3, 1, 5),
    _RlPethPowerPsedisconnectMethod_Type()
)
rlPethPowerPsedisconnectMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPethPowerPsedisconnectMethod.setStatus("current")


class _RlPethPowerPseTemperatureSensor_Type(Integer32):
    """Custom type rlPethPowerPseTemperatureSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 200),
    )


_RlPethPowerPseTemperatureSensor_Type.__name__ = "Integer32"
_RlPethPowerPseTemperatureSensor_Object = MibTableColumn
rlPethPowerPseTemperatureSensor = _RlPethPowerPseTemperatureSensor_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 3, 1, 6),
    _RlPethPowerPseTemperatureSensor_Type()
)
rlPethPowerPseTemperatureSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPowerPseTemperatureSensor.setStatus("current")


class _RlPethPowerPseInrushTestEnabled_Type(Integer32):
    """Custom type rlPethPowerPseInrushTestEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_RlPethPowerPseInrushTestEnabled_Type.__name__ = "Integer32"
_RlPethPowerPseInrushTestEnabled_Object = MibTableColumn
rlPethPowerPseInrushTestEnabled = _RlPethPowerPseInrushTestEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 3, 1, 7),
    _RlPethPowerPseInrushTestEnabled_Type()
)
rlPethPowerPseInrushTestEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPethPowerPseInrushTestEnabled.setStatus("current")


class _RlPethPowerPseLegacyDisabled_Type(Integer32):
    """Custom type rlPethPowerPseLegacyDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_RlPethPowerPseLegacyDisabled_Type.__name__ = "Integer32"
_RlPethPowerPseLegacyDisabled_Object = MibTableColumn
rlPethPowerPseLegacyDisabled = _RlPethPowerPseLegacyDisabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 108, 3, 1, 8),
    _RlPethPowerPseLegacyDisabled_Type()
)
rlPethPowerPseLegacyDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPethPowerPseLegacyDisabled.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Dell-POE-MIB",
    **{"rlPoe": rlPoe,
       "rlPethPsePortTable": rlPethPsePortTable,
       "rlPethPsePortEntry": rlPethPsePortEntry,
       "rlPethPsePortGroupIndex": rlPethPsePortGroupIndex,
       "rlPethPsePortIndex": rlPethPsePortIndex,
       "rlPethPsePortOutputVoltage": rlPethPsePortOutputVoltage,
       "rlPethPsePortOutputCurrent": rlPethPsePortOutputCurrent,
       "rlPethPsePortOutputPower": rlPethPsePortOutputPower,
       "rlPethPsePortPowerLimit": rlPethPsePortPowerLimit,
       "rlPethPsePortStatus": rlPethPsePortStatus,
       "rlPethPsePortStatusDescription": rlPethPsePortStatusDescription,
       "rlPethPsePortOperPowerLimit": rlPethPsePortOperPowerLimit,
       "rlPethPsePortSupportPoePlus": rlPethPsePortSupportPoePlus,
       "rlPethPsePortTimeRangeName": rlPethPsePortTimeRangeName,
       "rlPethPsePortOperStatus": rlPethPsePortOperStatus,
       "rlPethPsePortMaxPowerAllocAllowed": rlPethPsePortMaxPowerAllocAllowed,
       "rlPethPsePortSupportPoe": rlPethPsePortSupportPoe,
       "rlPethMainPseTable": rlPethMainPseTable,
       "rlPethMainPseEntry": rlPethMainPseEntry,
       "rlPethMainPseGroupIndex": rlPethMainPseGroupIndex,
       "rlPethMainPseSwVersion": rlPethMainPseSwVersion,
       "rlPethMainPseHwVersion": rlPethMainPseHwVersion,
       "rlPethMainPseHwType": rlPethMainPseHwType,
       "rlPethMainPsePowerGuardBand": rlPethMainPsePowerGuardBand,
       "rlPethPowerPseTable": rlPethPowerPseTable,
       "rlPethPowerPseEntry": rlPethPowerPseEntry,
       "rlPethPowerPseGroupIndex": rlPethPowerPseGroupIndex,
       "rlPethPowerPsePower": rlPethPowerPsePower,
       "rlPethPowerPseRpsPower": rlPethPowerPseRpsPower,
       "rlPethPowerPsePowerManagementMode": rlPethPowerPsePowerManagementMode,
       "rlPethPowerPsedisconnectMethod": rlPethPowerPsedisconnectMethod,
       "rlPethPowerPseTemperatureSensor": rlPethPowerPseTemperatureSensor,
       "rlPethPowerPseInrushTestEnabled": rlPethPowerPseInrushTestEnabled,
       "rlPethPowerPseLegacyDisabled": rlPethPowerPseLegacyDisabled}
)
