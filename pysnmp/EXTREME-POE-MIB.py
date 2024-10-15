# SNMP MIB module (EXTREME-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:20 2024
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

(extremeAgent,
 extremeV2Traps) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent",
    "extremeV2Traps")

(pethMainPseGroupIndex,
 pethPsePortGroupIndex,
 pethPsePortIndex) = mibBuilder.importSymbols(
    "POWER-ETHERNET-MIB",
    "pethMainPseGroupIndex",
    "pethPsePortGroupIndex",
    "pethPsePortIndex")

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

extremePoE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremePethMain_ObjectIdentity = ObjectIdentity
extremePethMain = _ExtremePethMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1)
)
_ExtremePethPseSlotTable_Object = MibTable
extremePethPseSlotTable = _ExtremePethPseSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1, 2)
)
if mibBuilder.loadTexts:
    extremePethPseSlotTable.setStatus("current")
_ExtremePethPseSlotEntry_Object = MibTableRow
extremePethPseSlotEntry = _ExtremePethPseSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1, 2, 1)
)
extremePethPseSlotEntry.setIndexNames(
    (0, "EXTREME-POE-MIB", "extremePethSlotNumber"),
)
if mibBuilder.loadTexts:
    extremePethPseSlotEntry.setStatus("current")
_ExtremePethSlotNumber_Type = Integer32
_ExtremePethSlotNumber_Object = MibTableColumn
extremePethSlotNumber = _ExtremePethSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1, 2, 1, 1),
    _ExtremePethSlotNumber_Type()
)
extremePethSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremePethSlotNumber.setStatus("current")
_ExtremePethSlotPowerLimit_Type = Integer32
_ExtremePethSlotPowerLimit_Object = MibTableColumn
extremePethSlotPowerLimit = _ExtremePethSlotPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1, 2, 1, 2),
    _ExtremePethSlotPowerLimit_Type()
)
extremePethSlotPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePethSlotPowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    extremePethSlotPowerLimit.setUnits("watts")
_ExtremePethSlotConsumptionPower_Type = Gauge32
_ExtremePethSlotConsumptionPower_Object = MibTableColumn
extremePethSlotConsumptionPower = _ExtremePethSlotConsumptionPower_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1, 2, 1, 3),
    _ExtremePethSlotConsumptionPower_Type()
)
extremePethSlotConsumptionPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePethSlotConsumptionPower.setStatus("current")
if mibBuilder.loadTexts:
    extremePethSlotConsumptionPower.setUnits("watts")


class _ExtremePethSlotClearConnectHistory_Type(Integer32):
    """Custom type extremePethSlotClearConnectHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("set", 1))
    )


_ExtremePethSlotClearConnectHistory_Type.__name__ = "Integer32"
_ExtremePethSlotClearConnectHistory_Object = MibTableColumn
extremePethSlotClearConnectHistory = _ExtremePethSlotClearConnectHistory_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1, 2, 1, 4),
    _ExtremePethSlotClearConnectHistory_Type()
)
extremePethSlotClearConnectHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePethSlotClearConnectHistory.setStatus("current")
_ExtremePethSlotReservedConsumptionPower_Type = Gauge32
_ExtremePethSlotReservedConsumptionPower_Object = MibTableColumn
extremePethSlotReservedConsumptionPower = _ExtremePethSlotReservedConsumptionPower_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1, 2, 1, 5),
    _ExtremePethSlotReservedConsumptionPower_Type()
)
extremePethSlotReservedConsumptionPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePethSlotReservedConsumptionPower.setStatus("current")
if mibBuilder.loadTexts:
    extremePethSlotReservedConsumptionPower.setUnits("Milliwatts")
_ExtremePethSlotCommonConsumptionPower_Type = Gauge32
_ExtremePethSlotCommonConsumptionPower_Object = MibTableColumn
extremePethSlotCommonConsumptionPower = _ExtremePethSlotCommonConsumptionPower_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1, 2, 1, 6),
    _ExtremePethSlotCommonConsumptionPower_Type()
)
extremePethSlotCommonConsumptionPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePethSlotCommonConsumptionPower.setStatus("current")
if mibBuilder.loadTexts:
    extremePethSlotCommonConsumptionPower.setUnits("Milliwatts")


class _ExtremePethSlotAdminEnable_Type(Integer32):
    """Custom type extremePethSlotAdminEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ExtremePethSlotAdminEnable_Type.__name__ = "Integer32"
_ExtremePethSlotAdminEnable_Object = MibTableColumn
extremePethSlotAdminEnable = _ExtremePethSlotAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1, 2, 1, 7),
    _ExtremePethSlotAdminEnable_Type()
)
extremePethSlotAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePethSlotAdminEnable.setStatus("current")


class _ExtremePethSlotPoeStatus_Type(Integer32):
    """Custom type extremePethSlotPoeStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("calibrationRequired", 4),
          ("downloadFail", 3),
          ("initializing", 1),
          ("invalidDevice", 8),
          ("invalidFirmware", 5),
          ("mismatchVersion", 6),
          ("notOperational", 9),
          ("operational", 2),
          ("other", 10),
          ("updating", 7))
    )


_ExtremePethSlotPoeStatus_Type.__name__ = "Integer32"
_ExtremePethSlotPoeStatus_Object = MibTableColumn
extremePethSlotPoeStatus = _ExtremePethSlotPoeStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1, 2, 1, 8),
    _ExtremePethSlotPoeStatus_Type()
)
extremePethSlotPoeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePethSlotPoeStatus.setStatus("current")


class _ExtremePethSlotPoeResetSystem_Type(Integer32):
    """Custom type extremePethSlotPoeResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("set", 1))
    )


_ExtremePethSlotPoeResetSystem_Type.__name__ = "Integer32"
_ExtremePethSlotPoeResetSystem_Object = MibTableColumn
extremePethSlotPoeResetSystem = _ExtremePethSlotPoeResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1, 2, 1, 9),
    _ExtremePethSlotPoeResetSystem_Type()
)
extremePethSlotPoeResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePethSlotPoeResetSystem.setStatus("current")
_ExtremePethSlotMaxAvailPower_Type = Gauge32
_ExtremePethSlotMaxAvailPower_Object = MibTableColumn
extremePethSlotMaxAvailPower = _ExtremePethSlotMaxAvailPower_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1, 2, 1, 10),
    _ExtremePethSlotMaxAvailPower_Type()
)
extremePethSlotMaxAvailPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePethSlotMaxAvailPower.setStatus("current")
if mibBuilder.loadTexts:
    extremePethSlotMaxAvailPower.setUnits("watts")
_ExtremePethSlotMaxCapacity_Type = Gauge32
_ExtremePethSlotMaxCapacity_Object = MibTableColumn
extremePethSlotMaxCapacity = _ExtremePethSlotMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1, 2, 1, 11),
    _ExtremePethSlotMaxCapacity_Type()
)
extremePethSlotMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePethSlotMaxCapacity.setStatus("current")
if mibBuilder.loadTexts:
    extremePethSlotMaxCapacity.setUnits("watts")


class _ExtremePethSlotBackupPSU_Type(Integer32):
    """Custom type extremePethSlotBackupPSU based on Integer32"""
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
        *(("external", 3),
          ("internal", 2),
          ("none", 1),
          ("notApplicable", 4))
    )


_ExtremePethSlotBackupPSU_Type.__name__ = "Integer32"
_ExtremePethSlotBackupPSU_Object = MibTableColumn
extremePethSlotBackupPSU = _ExtremePethSlotBackupPSU_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1, 2, 1, 12),
    _ExtremePethSlotBackupPSU_Type()
)
extremePethSlotBackupPSU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePethSlotBackupPSU.setStatus("current")


class _ExtremePethSlotPSUActive_Type(Integer32):
    """Custom type extremePethSlotPSUActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("none", 1))
    )


_ExtremePethSlotPSUActive_Type.__name__ = "Integer32"
_ExtremePethSlotPSUActive_Object = MibTableColumn
extremePethSlotPSUActive = _ExtremePethSlotPSUActive_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1, 2, 1, 13),
    _ExtremePethSlotPSUActive_Type()
)
extremePethSlotPSUActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePethSlotPSUActive.setStatus("current")
_ExtremePethSlotMeasuredPower_Type = Gauge32
_ExtremePethSlotMeasuredPower_Object = MibTableColumn
extremePethSlotMeasuredPower = _ExtremePethSlotMeasuredPower_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1, 2, 1, 14),
    _ExtremePethSlotMeasuredPower_Type()
)
extremePethSlotMeasuredPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePethSlotMeasuredPower.setStatus("current")
if mibBuilder.loadTexts:
    extremePethSlotMeasuredPower.setUnits("milliwatts")
_ExtremePethSlotMainPseIndex_Type = Integer32
_ExtremePethSlotMainPseIndex_Object = MibTableColumn
extremePethSlotMainPseIndex = _ExtremePethSlotMainPseIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 1, 2, 1, 15),
    _ExtremePethSlotMainPseIndex_Type()
)
extremePethSlotMainPseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePethSlotMainPseIndex.setStatus("current")
_ExtremePethPort_ObjectIdentity = ObjectIdentity
extremePethPort = _ExtremePethPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 2)
)
_ExtremePethPsePortTable_Object = MibTable
extremePethPsePortTable = _ExtremePethPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 2, 1)
)
if mibBuilder.loadTexts:
    extremePethPsePortTable.setStatus("current")
_ExtremePethPsePortEntry_Object = MibTableRow
extremePethPsePortEntry = _ExtremePethPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 2, 1, 1)
)
extremePethPsePortEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethPsePortGroupIndex"),
    (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"),
)
if mibBuilder.loadTexts:
    extremePethPsePortEntry.setStatus("current")


class _ExtremePethPortOperatorLimit_Type(Integer32):
    """Custom type extremePethPortOperatorLimit based on Integer32"""
    defaultValue = 15400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3000, 20000),
    )


_ExtremePethPortOperatorLimit_Type.__name__ = "Integer32"
_ExtremePethPortOperatorLimit_Object = MibTableColumn
extremePethPortOperatorLimit = _ExtremePethPortOperatorLimit_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 2, 1, 1, 1),
    _ExtremePethPortOperatorLimit_Type()
)
extremePethPortOperatorLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePethPortOperatorLimit.setStatus("current")
if mibBuilder.loadTexts:
    extremePethPortOperatorLimit.setUnits("Milliwatts")


class _ExtremePethPortReservedBudget_Type(Integer32):
    """Custom type extremePethPortReservedBudget based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_ExtremePethPortReservedBudget_Type.__name__ = "Integer32"
_ExtremePethPortReservedBudget_Object = MibTableColumn
extremePethPortReservedBudget = _ExtremePethPortReservedBudget_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 2, 1, 1, 2),
    _ExtremePethPortReservedBudget_Type()
)
extremePethPortReservedBudget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePethPortReservedBudget.setStatus("current")
if mibBuilder.loadTexts:
    extremePethPortReservedBudget.setUnits("Milliwatts")


class _ExtremePethPortViolationPrecedence_Type(Integer32):
    """Custom type extremePethPortViolationPrecedence based on Integer32"""
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
        *(("advertisedClass", 1),
          ("maxAdvertisedOperator", 3),
          ("none", 4),
          ("operatorLimit", 2))
    )


_ExtremePethPortViolationPrecedence_Type.__name__ = "Integer32"
_ExtremePethPortViolationPrecedence_Object = MibTableColumn
extremePethPortViolationPrecedence = _ExtremePethPortViolationPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 2, 1, 1, 3),
    _ExtremePethPortViolationPrecedence_Type()
)
extremePethPortViolationPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePethPortViolationPrecedence.setStatus("current")


class _ExtremePethPortClearFault_Type(Integer32):
    """Custom type extremePethPortClearFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("set", 1))
    )


_ExtremePethPortClearFault_Type.__name__ = "Integer32"
_ExtremePethPortClearFault_Object = MibTableColumn
extremePethPortClearFault = _ExtremePethPortClearFault_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 2, 1, 1, 4),
    _ExtremePethPortClearFault_Type()
)
extremePethPortClearFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePethPortClearFault.setStatus("current")


class _ExtremePethPortResetPower_Type(Integer32):
    """Custom type extremePethPortResetPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("set", 1))
    )


_ExtremePethPortResetPower_Type.__name__ = "Integer32"
_ExtremePethPortResetPower_Object = MibTableColumn
extremePethPortResetPower = _ExtremePethPortResetPower_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 2, 1, 1, 5),
    _ExtremePethPortResetPower_Type()
)
extremePethPortResetPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePethPortResetPower.setStatus("current")
_ExtremePethPortMeasuredPower_Type = Gauge32
_ExtremePethPortMeasuredPower_Object = MibTableColumn
extremePethPortMeasuredPower = _ExtremePethPortMeasuredPower_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 2, 1, 1, 6),
    _ExtremePethPortMeasuredPower_Type()
)
extremePethPortMeasuredPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePethPortMeasuredPower.setStatus("current")
if mibBuilder.loadTexts:
    extremePethPortMeasuredPower.setUnits("Milliwatts")
_ExtremePethSystem_ObjectIdentity = ObjectIdentity
extremePethSystem = _ExtremePethSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 4)
)


class _ExtremePethSystemAdminEnable_Type(Integer32):
    """Custom type extremePethSystemAdminEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ExtremePethSystemAdminEnable_Type.__name__ = "Integer32"
_ExtremePethSystemAdminEnable_Object = MibScalar
extremePethSystemAdminEnable = _ExtremePethSystemAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 4, 1),
    _ExtremePethSystemAdminEnable_Type()
)
extremePethSystemAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePethSystemAdminEnable.setStatus("current")


class _ExtremePethSystemDisconnectPrecedence_Type(Integer32):
    """Custom type extremePethSystemDisconnectPrecedence based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("denyPort", 2),
          ("lowestPriority", 1))
    )


_ExtremePethSystemDisconnectPrecedence_Type.__name__ = "Integer32"
_ExtremePethSystemDisconnectPrecedence_Object = MibScalar
extremePethSystemDisconnectPrecedence = _ExtremePethSystemDisconnectPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 4, 2),
    _ExtremePethSystemDisconnectPrecedence_Type()
)
extremePethSystemDisconnectPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePethSystemDisconnectPrecedence.setStatus("current")


class _ExtremePethSystemUsageThreshold_Type(Integer32):
    """Custom type extremePethSystemUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_ExtremePethSystemUsageThreshold_Type.__name__ = "Integer32"
_ExtremePethSystemUsageThreshold_Object = MibScalar
extremePethSystemUsageThreshold = _ExtremePethSystemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 4, 3),
    _ExtremePethSystemUsageThreshold_Type()
)
extremePethSystemUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePethSystemUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    extremePethSystemUsageThreshold.setUnits("%")


class _ExtremePethSystemPowerSupplyMode_Type(Integer32):
    """Custom type extremePethSystemPowerSupplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loadSharing", 2),
          ("notApplicable", 3),
          ("redundant", 1))
    )


_ExtremePethSystemPowerSupplyMode_Type.__name__ = "Integer32"
_ExtremePethSystemPowerSupplyMode_Object = MibScalar
extremePethSystemPowerSupplyMode = _ExtremePethSystemPowerSupplyMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 4, 4),
    _ExtremePethSystemPowerSupplyMode_Type()
)
extremePethSystemPowerSupplyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePethSystemPowerSupplyMode.setStatus("current")


class _ExtremePethSystemLegacyEnable_Type(Integer32):
    """Custom type extremePethSystemLegacyEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ExtremePethSystemLegacyEnable_Type.__name__ = "Integer32"
_ExtremePethSystemLegacyEnable_Object = MibScalar
extremePethSystemLegacyEnable = _ExtremePethSystemLegacyEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27, 4, 5),
    _ExtremePethSystemLegacyEnable_Type()
)
extremePethSystemLegacyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePethSystemLegacyEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-POE-MIB",
    **{"extremePoE": extremePoE,
       "extremePethMain": extremePethMain,
       "extremePethPseSlotTable": extremePethPseSlotTable,
       "extremePethPseSlotEntry": extremePethPseSlotEntry,
       "extremePethSlotNumber": extremePethSlotNumber,
       "extremePethSlotPowerLimit": extremePethSlotPowerLimit,
       "extremePethSlotConsumptionPower": extremePethSlotConsumptionPower,
       "extremePethSlotClearConnectHistory": extremePethSlotClearConnectHistory,
       "extremePethSlotReservedConsumptionPower": extremePethSlotReservedConsumptionPower,
       "extremePethSlotCommonConsumptionPower": extremePethSlotCommonConsumptionPower,
       "extremePethSlotAdminEnable": extremePethSlotAdminEnable,
       "extremePethSlotPoeStatus": extremePethSlotPoeStatus,
       "extremePethSlotPoeResetSystem": extremePethSlotPoeResetSystem,
       "extremePethSlotMaxAvailPower": extremePethSlotMaxAvailPower,
       "extremePethSlotMaxCapacity": extremePethSlotMaxCapacity,
       "extremePethSlotBackupPSU": extremePethSlotBackupPSU,
       "extremePethSlotPSUActive": extremePethSlotPSUActive,
       "extremePethSlotMeasuredPower": extremePethSlotMeasuredPower,
       "extremePethSlotMainPseIndex": extremePethSlotMainPseIndex,
       "extremePethPort": extremePethPort,
       "extremePethPsePortTable": extremePethPsePortTable,
       "extremePethPsePortEntry": extremePethPsePortEntry,
       "extremePethPortOperatorLimit": extremePethPortOperatorLimit,
       "extremePethPortReservedBudget": extremePethPortReservedBudget,
       "extremePethPortViolationPrecedence": extremePethPortViolationPrecedence,
       "extremePethPortClearFault": extremePethPortClearFault,
       "extremePethPortResetPower": extremePethPortResetPower,
       "extremePethPortMeasuredPower": extremePethPortMeasuredPower,
       "extremePethSystem": extremePethSystem,
       "extremePethSystemAdminEnable": extremePethSystemAdminEnable,
       "extremePethSystemDisconnectPrecedence": extremePethSystemDisconnectPrecedence,
       "extremePethSystemUsageThreshold": extremePethSystemUsageThreshold,
       "extremePethSystemPowerSupplyMode": extremePethSystemPowerSupplyMode,
       "extremePethSystemLegacyEnable": extremePethSystemLegacyEnable}
)
