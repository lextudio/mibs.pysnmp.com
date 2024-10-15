# SNMP MIB module (EXTREME-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:19 2024
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

(PortList,
 extremeAgent) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "PortList",
    "extremeAgent")

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

extremeSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeSystemCommon_ObjectIdentity = ObjectIdentity
extremeSystemCommon = _ExtremeSystemCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1)
)


class _ExtremeSaveConfiguration_Type(Integer32):
    """Custom type extremeSaveConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("saveToPrimary", 1),
          ("saveToSecondary", 2))
    )


_ExtremeSaveConfiguration_Type.__name__ = "Integer32"
_ExtremeSaveConfiguration_Object = MibScalar
extremeSaveConfiguration = _ExtremeSaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 3),
    _ExtremeSaveConfiguration_Type()
)
extremeSaveConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeSaveConfiguration.setStatus("current")


class _ExtremeSaveStatus_Type(Integer32):
    """Custom type extremeSaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("saveInProgress", 1),
          ("saveNotInProgress", 2))
    )


_ExtremeSaveStatus_Type.__name__ = "Integer32"
_ExtremeSaveStatus_Object = MibScalar
extremeSaveStatus = _ExtremeSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 4),
    _ExtremeSaveStatus_Type()
)
extremeSaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSaveStatus.setStatus("current")


class _ExtremeCurrentConfigInUse_Type(Integer32):
    """Custom type extremeCurrentConfigInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_ExtremeCurrentConfigInUse_Type.__name__ = "Integer32"
_ExtremeCurrentConfigInUse_Object = MibScalar
extremeCurrentConfigInUse = _ExtremeCurrentConfigInUse_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 5),
    _ExtremeCurrentConfigInUse_Type()
)
extremeCurrentConfigInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCurrentConfigInUse.setStatus("current")


class _ExtremeConfigToUseOnReboot_Type(Integer32):
    """Custom type extremeConfigToUseOnReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_ExtremeConfigToUseOnReboot_Type.__name__ = "Integer32"
_ExtremeConfigToUseOnReboot_Object = MibScalar
extremeConfigToUseOnReboot = _ExtremeConfigToUseOnReboot_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 6),
    _ExtremeConfigToUseOnReboot_Type()
)
extremeConfigToUseOnReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeConfigToUseOnReboot.setStatus("current")
_ExtremeOverTemperatureAlarm_Type = TruthValue
_ExtremeOverTemperatureAlarm_Object = MibScalar
extremeOverTemperatureAlarm = _ExtremeOverTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 7),
    _ExtremeOverTemperatureAlarm_Type()
)
extremeOverTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeOverTemperatureAlarm.setStatus("current")


class _ExtremeCurrentTemperature_Type(Integer32):
    """Custom type extremeCurrentTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ExtremeCurrentTemperature_Type.__name__ = "Integer32"
_ExtremeCurrentTemperature_Object = MibScalar
extremeCurrentTemperature = _ExtremeCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 8),
    _ExtremeCurrentTemperature_Type()
)
extremeCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCurrentTemperature.setStatus("current")
_ExtremeFanStatusTable_Object = MibTable
extremeFanStatusTable = _ExtremeFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    extremeFanStatusTable.setStatus("current")
_ExtremeFanStatusEntry_Object = MibTableRow
extremeFanStatusEntry = _ExtremeFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 9, 1)
)
extremeFanStatusEntry.setIndexNames(
    (0, "EXTREME-SYSTEM-MIB", "extremeFanNumber"),
)
if mibBuilder.loadTexts:
    extremeFanStatusEntry.setStatus("current")
_ExtremeFanNumber_Type = Integer32
_ExtremeFanNumber_Object = MibTableColumn
extremeFanNumber = _ExtremeFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 9, 1, 1),
    _ExtremeFanNumber_Type()
)
extremeFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeFanNumber.setStatus("current")
_ExtremeFanOperational_Type = TruthValue
_ExtremeFanOperational_Object = MibTableColumn
extremeFanOperational = _ExtremeFanOperational_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 9, 1, 2),
    _ExtremeFanOperational_Type()
)
extremeFanOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeFanOperational.setStatus("current")
_ExtremeFanEntPhysicalIndex_Type = Integer32
_ExtremeFanEntPhysicalIndex_Object = MibTableColumn
extremeFanEntPhysicalIndex = _ExtremeFanEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 9, 1, 3),
    _ExtremeFanEntPhysicalIndex_Type()
)
extremeFanEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeFanEntPhysicalIndex.setStatus("current")
_ExtremePrimaryPowerOperational_Type = TruthValue
_ExtremePrimaryPowerOperational_Object = MibScalar
extremePrimaryPowerOperational = _ExtremePrimaryPowerOperational_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 10),
    _ExtremePrimaryPowerOperational_Type()
)
extremePrimaryPowerOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePrimaryPowerOperational.setStatus("current")


class _ExtremeRedundantPowerStatus_Type(Integer32):
    """Custom type extremeRedundantPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("presentNotOK", 3),
          ("presentOK", 2))
    )


_ExtremeRedundantPowerStatus_Type.__name__ = "Integer32"
_ExtremeRedundantPowerStatus_Object = MibScalar
extremeRedundantPowerStatus = _ExtremeRedundantPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 11),
    _ExtremeRedundantPowerStatus_Type()
)
extremeRedundantPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeRedundantPowerStatus.setStatus("current")
_ExtremeRedundantPowerAlarm_Type = TruthValue
_ExtremeRedundantPowerAlarm_Object = MibScalar
extremeRedundantPowerAlarm = _ExtremeRedundantPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 12),
    _ExtremeRedundantPowerAlarm_Type()
)
extremeRedundantPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeRedundantPowerAlarm.setStatus("current")


class _ExtremePrimarySoftwareRev_Type(DisplayString):
    """Custom type extremePrimarySoftwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ExtremePrimarySoftwareRev_Type.__name__ = "DisplayString"
_ExtremePrimarySoftwareRev_Object = MibScalar
extremePrimarySoftwareRev = _ExtremePrimarySoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 13),
    _ExtremePrimarySoftwareRev_Type()
)
extremePrimarySoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePrimarySoftwareRev.setStatus("current")


class _ExtremeSecondarySoftwareRev_Type(DisplayString):
    """Custom type extremeSecondarySoftwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ExtremeSecondarySoftwareRev_Type.__name__ = "DisplayString"
_ExtremeSecondarySoftwareRev_Object = MibScalar
extremeSecondarySoftwareRev = _ExtremeSecondarySoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 14),
    _ExtremeSecondarySoftwareRev_Type()
)
extremeSecondarySoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSecondarySoftwareRev.setStatus("current")


class _ExtremeImageToUseOnReboot_Type(Integer32):
    """Custom type extremeImageToUseOnReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_ExtremeImageToUseOnReboot_Type.__name__ = "Integer32"
_ExtremeImageToUseOnReboot_Object = MibScalar
extremeImageToUseOnReboot = _ExtremeImageToUseOnReboot_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 15),
    _ExtremeImageToUseOnReboot_Type()
)
extremeImageToUseOnReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeImageToUseOnReboot.setStatus("current")


class _ExtremeSystemID_Type(DisplayString):
    """Custom type extremeSystemID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_ExtremeSystemID_Type.__name__ = "DisplayString"
_ExtremeSystemID_Object = MibScalar
extremeSystemID = _ExtremeSystemID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 16),
    _ExtremeSystemID_Type()
)
extremeSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSystemID.setStatus("current")


class _ExtremeSystemBoardID_Type(DisplayString):
    """Custom type extremeSystemBoardID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_ExtremeSystemBoardID_Type.__name__ = "DisplayString"
_ExtremeSystemBoardID_Object = MibScalar
extremeSystemBoardID = _ExtremeSystemBoardID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 17),
    _ExtremeSystemBoardID_Type()
)
extremeSystemBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSystemBoardID.setStatus("current")


class _ExtremeSystemLeftBoardID_Type(DisplayString):
    """Custom type extremeSystemLeftBoardID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_ExtremeSystemLeftBoardID_Type.__name__ = "DisplayString"
_ExtremeSystemLeftBoardID_Object = MibScalar
extremeSystemLeftBoardID = _ExtremeSystemLeftBoardID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 18),
    _ExtremeSystemLeftBoardID_Type()
)
extremeSystemLeftBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSystemLeftBoardID.setStatus("current")


class _ExtremeSystemRightBoardID_Type(DisplayString):
    """Custom type extremeSystemRightBoardID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_ExtremeSystemRightBoardID_Type.__name__ = "DisplayString"
_ExtremeSystemRightBoardID_Object = MibScalar
extremeSystemRightBoardID = _ExtremeSystemRightBoardID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 19),
    _ExtremeSystemRightBoardID_Type()
)
extremeSystemRightBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSystemRightBoardID.setStatus("current")


class _ExtremeInputPowerVoltage_Type(Integer32):
    """Custom type extremeInputPowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v110", 1),
          ("v220", 2),
          ("v48DC", 3))
    )


_ExtremeInputPowerVoltage_Type.__name__ = "Integer32"
_ExtremeInputPowerVoltage_Object = MibScalar
extremeInputPowerVoltage = _ExtremeInputPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 20),
    _ExtremeInputPowerVoltage_Type()
)
extremeInputPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeInputPowerVoltage.setStatus("current")


class _ExtremePowerStatus_Type(Integer32):
    """Custom type extremePowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("presentNotOK", 3),
          ("presentOK", 2))
    )


_ExtremePowerStatus_Type.__name__ = "Integer32"
_ExtremePowerStatus_Object = MibScalar
extremePowerStatus = _ExtremePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 21),
    _ExtremePowerStatus_Type()
)
extremePowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePowerStatus.setStatus("current")
_ExtremePowerAlarm_Type = TruthValue
_ExtremePowerAlarm_Object = MibScalar
extremePowerAlarm = _ExtremePowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 22),
    _ExtremePowerAlarm_Type()
)
extremePowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePowerAlarm.setStatus("current")
_ExtremeRmonEnable_Type = TruthValue
_ExtremeRmonEnable_Object = MibScalar
extremeRmonEnable = _ExtremeRmonEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 23),
    _ExtremeRmonEnable_Type()
)
extremeRmonEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeRmonEnable.setStatus("current")


class _ExtremeBootROMVersion_Type(DisplayString):
    """Custom type extremeBootROMVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ExtremeBootROMVersion_Type.__name__ = "DisplayString"
_ExtremeBootROMVersion_Object = MibScalar
extremeBootROMVersion = _ExtremeBootROMVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 25),
    _ExtremeBootROMVersion_Type()
)
extremeBootROMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBootROMVersion.setStatus("current")
_ExtremeDot1dTpFdbTableEnable_Type = TruthValue
_ExtremeDot1dTpFdbTableEnable_Object = MibScalar
extremeDot1dTpFdbTableEnable = _ExtremeDot1dTpFdbTableEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 26),
    _ExtremeDot1dTpFdbTableEnable_Type()
)
extremeDot1dTpFdbTableEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeDot1dTpFdbTableEnable.setStatus("current")
_ExtremePowerSupplyTable_Object = MibTable
extremePowerSupplyTable = _ExtremePowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 27)
)
if mibBuilder.loadTexts:
    extremePowerSupplyTable.setStatus("current")
_ExtremePowerSupplyEntry_Object = MibTableRow
extremePowerSupplyEntry = _ExtremePowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 27, 1)
)
extremePowerSupplyEntry.setIndexNames(
    (0, "EXTREME-SYSTEM-MIB", "extremePowerSupplyNumber"),
)
if mibBuilder.loadTexts:
    extremePowerSupplyEntry.setStatus("current")
_ExtremePowerSupplyNumber_Type = Integer32
_ExtremePowerSupplyNumber_Object = MibTableColumn
extremePowerSupplyNumber = _ExtremePowerSupplyNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 27, 1, 1),
    _ExtremePowerSupplyNumber_Type()
)
extremePowerSupplyNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremePowerSupplyNumber.setStatus("current")


class _ExtremePowerSupplyStatus_Type(Integer32):
    """Custom type extremePowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("presentNotOK", 3),
          ("presentOK", 2))
    )


_ExtremePowerSupplyStatus_Type.__name__ = "Integer32"
_ExtremePowerSupplyStatus_Object = MibTableColumn
extremePowerSupplyStatus = _ExtremePowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 27, 1, 2),
    _ExtremePowerSupplyStatus_Type()
)
extremePowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePowerSupplyStatus.setStatus("current")


class _ExtremePowerSupplyInputVoltage_Type(Integer32):
    """Custom type extremePowerSupplyInputVoltage based on Integer32"""
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
        *(("unknown", 4),
          ("v110", 1),
          ("v220", 2),
          ("v48DC", 3))
    )


_ExtremePowerSupplyInputVoltage_Type.__name__ = "Integer32"
_ExtremePowerSupplyInputVoltage_Object = MibTableColumn
extremePowerSupplyInputVoltage = _ExtremePowerSupplyInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 27, 1, 3),
    _ExtremePowerSupplyInputVoltage_Type()
)
extremePowerSupplyInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePowerSupplyInputVoltage.setStatus("current")


class _ExtremePowerSupplySerialNumber_Type(DisplayString):
    """Custom type extremePowerSupplySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_ExtremePowerSupplySerialNumber_Type.__name__ = "DisplayString"
_ExtremePowerSupplySerialNumber_Object = MibTableColumn
extremePowerSupplySerialNumber = _ExtremePowerSupplySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 27, 1, 4),
    _ExtremePowerSupplySerialNumber_Type()
)
extremePowerSupplySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePowerSupplySerialNumber.setStatus("current")
_ExtremePowerSupplyEntPhysicalIndex_Type = Integer32
_ExtremePowerSupplyEntPhysicalIndex_Object = MibTableColumn
extremePowerSupplyEntPhysicalIndex = _ExtremePowerSupplyEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 27, 1, 5),
    _ExtremePowerSupplyEntPhysicalIndex_Type()
)
extremePowerSupplyEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePowerSupplyEntPhysicalIndex.setStatus("current")
_ExtremeCpuAggregateUtilization_Type = Integer32
_ExtremeCpuAggregateUtilization_Object = MibScalar
extremeCpuAggregateUtilization = _ExtremeCpuAggregateUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 28),
    _ExtremeCpuAggregateUtilization_Type()
)
extremeCpuAggregateUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuAggregateUtilization.setStatus("current")
_ExtremeCpuTask2Table_Object = MibTable
extremeCpuTask2Table = _ExtremeCpuTask2Table_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 29)
)
if mibBuilder.loadTexts:
    extremeCpuTask2Table.setStatus("current")
_ExtremeCpuTask2Entry_Object = MibTableRow
extremeCpuTask2Entry = _ExtremeCpuTask2Entry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 29, 1)
)
extremeCpuTask2Entry.setIndexNames(
    (0, "EXTREME-SYSTEM-MIB", "extremeCpuTask2CpuId"),
    (0, "EXTREME-SYSTEM-MIB", "extremeCpuTask2Name"),
)
if mibBuilder.loadTexts:
    extremeCpuTask2Entry.setStatus("current")
_ExtremeCpuTask2CpuId_Type = Unsigned32
_ExtremeCpuTask2CpuId_Object = MibTableColumn
extremeCpuTask2CpuId = _ExtremeCpuTask2CpuId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 29, 1, 1),
    _ExtremeCpuTask2CpuId_Type()
)
extremeCpuTask2CpuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeCpuTask2CpuId.setStatus("current")


class _ExtremeCpuTask2Name_Type(DisplayString):
    """Custom type extremeCpuTask2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ExtremeCpuTask2Name_Type.__name__ = "DisplayString"
_ExtremeCpuTask2Name_Object = MibTableColumn
extremeCpuTask2Name = _ExtremeCpuTask2Name_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 29, 1, 2),
    _ExtremeCpuTask2Name_Type()
)
extremeCpuTask2Name.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeCpuTask2Name.setStatus("current")
_ExtremeCpuTask2Id_Type = Unsigned32
_ExtremeCpuTask2Id_Object = MibTableColumn
extremeCpuTask2Id = _ExtremeCpuTask2Id_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 29, 1, 3),
    _ExtremeCpuTask2Id_Type()
)
extremeCpuTask2Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuTask2Id.setStatus("current")
_ExtremeCpuTask2Pc_Type = Unsigned32
_ExtremeCpuTask2Pc_Object = MibTableColumn
extremeCpuTask2Pc = _ExtremeCpuTask2Pc_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 29, 1, 4),
    _ExtremeCpuTask2Pc_Type()
)
extremeCpuTask2Pc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuTask2Pc.setStatus("current")
_ExtremeCpuTask2Status_Type = DisplayString
_ExtremeCpuTask2Status_Object = MibTableColumn
extremeCpuTask2Status = _ExtremeCpuTask2Status_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 29, 1, 5),
    _ExtremeCpuTask2Status_Type()
)
extremeCpuTask2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuTask2Status.setStatus("current")
_ExtremeCpuTask2Utilization_Type = Unsigned32
_ExtremeCpuTask2Utilization_Object = MibTableColumn
extremeCpuTask2Utilization = _ExtremeCpuTask2Utilization_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 29, 1, 6),
    _ExtremeCpuTask2Utilization_Type()
)
extremeCpuTask2Utilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCpuTask2Utilization.setStatus("current")
_ExtremeCpuTask2MaxUtilization_Type = Unsigned32
_ExtremeCpuTask2MaxUtilization_Object = MibTableColumn
extremeCpuTask2MaxUtilization = _ExtremeCpuTask2MaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 29, 1, 7),
    _ExtremeCpuTask2MaxUtilization_Type()
)
extremeCpuTask2MaxUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeCpuTask2MaxUtilization.setStatus("current")
_ExtremeAuthFailSrcAddr_Type = IpAddress
_ExtremeAuthFailSrcAddr_Object = MibScalar
extremeAuthFailSrcAddr = _ExtremeAuthFailSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 30),
    _ExtremeAuthFailSrcAddr_Type()
)
extremeAuthFailSrcAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeAuthFailSrcAddr.setStatus("current")


class _ExtremeCpuTransmitPriority_Type(Integer32):
    """Custom type extremeCpuTransmitPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("normal", 1))
    )


_ExtremeCpuTransmitPriority_Type.__name__ = "Integer32"
_ExtremeCpuTransmitPriority_Object = MibScalar
extremeCpuTransmitPriority = _ExtremeCpuTransmitPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 31),
    _ExtremeCpuTransmitPriority_Type()
)
extremeCpuTransmitPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeCpuTransmitPriority.setStatus("deprecated")


class _ExtremeImageBooted_Type(Integer32):
    """Custom type extremeImageBooted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_ExtremeImageBooted_Type.__name__ = "Integer32"
_ExtremeImageBooted_Object = MibScalar
extremeImageBooted = _ExtremeImageBooted_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 32),
    _ExtremeImageBooted_Type()
)
extremeImageBooted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeImageBooted.setStatus("current")


class _ExtremeMsmFailoverCause_Type(Integer32):
    """Custom type extremeMsmFailoverCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("admin", 2),
          ("exception", 3),
          ("hwFailure", 5),
          ("keepalive", 7),
          ("never", 1),
          ("removal", 4),
          ("watchdog", 6))
    )


_ExtremeMsmFailoverCause_Type.__name__ = "Integer32"
_ExtremeMsmFailoverCause_Object = MibScalar
extremeMsmFailoverCause = _ExtremeMsmFailoverCause_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 33),
    _ExtremeMsmFailoverCause_Type()
)
extremeMsmFailoverCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMsmFailoverCause.setStatus("current")
_ExtremeImageTable_Object = MibTable
extremeImageTable = _ExtremeImageTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 34)
)
if mibBuilder.loadTexts:
    extremeImageTable.setStatus("current")
_ExtremeImageEntry_Object = MibTableRow
extremeImageEntry = _ExtremeImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 34, 1)
)
extremeImageEntry.setIndexNames(
    (0, "EXTREME-SYSTEM-MIB", "extremeImageNumber"),
)
if mibBuilder.loadTexts:
    extremeImageEntry.setStatus("current")


class _ExtremeImageNumber_Type(Integer32):
    """Custom type extremeImageNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cur", 0),
          ("pri", 1),
          ("sec", 2))
    )


_ExtremeImageNumber_Type.__name__ = "Integer32"
_ExtremeImageNumber_Object = MibTableColumn
extremeImageNumber = _ExtremeImageNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 34, 1, 1),
    _ExtremeImageNumber_Type()
)
extremeImageNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeImageNumber.setStatus("current")
_ExtremeMajorVersion_Type = Integer32
_ExtremeMajorVersion_Object = MibTableColumn
extremeMajorVersion = _ExtremeMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 34, 1, 2),
    _ExtremeMajorVersion_Type()
)
extremeMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMajorVersion.setStatus("current")
_ExtremeSubMajorVersion_Type = Integer32
_ExtremeSubMajorVersion_Object = MibTableColumn
extremeSubMajorVersion = _ExtremeSubMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 34, 1, 3),
    _ExtremeSubMajorVersion_Type()
)
extremeSubMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSubMajorVersion.setStatus("deprecated")
_ExtremeMinorVersion_Type = Integer32
_ExtremeMinorVersion_Object = MibTableColumn
extremeMinorVersion = _ExtremeMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 34, 1, 4),
    _ExtremeMinorVersion_Type()
)
extremeMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMinorVersion.setStatus("current")
_ExtremeBuildNumber_Type = Integer32
_ExtremeBuildNumber_Object = MibTableColumn
extremeBuildNumber = _ExtremeBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 34, 1, 5),
    _ExtremeBuildNumber_Type()
)
extremeBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBuildNumber.setStatus("current")
_ExtremeTechnologyReleaseNumber_Type = Integer32
_ExtremeTechnologyReleaseNumber_Object = MibTableColumn
extremeTechnologyReleaseNumber = _ExtremeTechnologyReleaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 34, 1, 6),
    _ExtremeTechnologyReleaseNumber_Type()
)
extremeTechnologyReleaseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTechnologyReleaseNumber.setStatus("current")
_ExtremeSustainingReleaseNumber_Type = Integer32
_ExtremeSustainingReleaseNumber_Object = MibTableColumn
extremeSustainingReleaseNumber = _ExtremeSustainingReleaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 34, 1, 7),
    _ExtremeSustainingReleaseNumber_Type()
)
extremeSustainingReleaseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSustainingReleaseNumber.setStatus("current")
_ExtremeBranchRevisionNumber_Type = Integer32
_ExtremeBranchRevisionNumber_Object = MibTableColumn
extremeBranchRevisionNumber = _ExtremeBranchRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 34, 1, 8),
    _ExtremeBranchRevisionNumber_Type()
)
extremeBranchRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBranchRevisionNumber.setStatus("current")


class _ExtremeImageType_Type(Integer32):
    """Custom type extremeImageType based on Integer32"""
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
        *(("beta", 4),
          ("branch", 1),
          ("patch", 2),
          ("technology", 3),
          ("trunk", 0))
    )


_ExtremeImageType_Type.__name__ = "Integer32"
_ExtremeImageType_Object = MibTableColumn
extremeImageType = _ExtremeImageType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 34, 1, 9),
    _ExtremeImageType_Type()
)
extremeImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeImageType.setStatus("current")


class _ExtremeImageDescription_Type(DisplayString):
    """Custom type extremeImageDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_ExtremeImageDescription_Type.__name__ = "DisplayString"
_ExtremeImageDescription_Object = MibTableColumn
extremeImageDescription = _ExtremeImageDescription_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 34, 1, 10),
    _ExtremeImageDescription_Type()
)
extremeImageDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeImageDescription.setStatus("current")


class _ExtremeImageSecurity_Type(Integer32):
    """Custom type extremeImageSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nossh", 1),
          ("ssh", 2),
          ("unknown", 0))
    )


_ExtremeImageSecurity_Type.__name__ = "Integer32"
_ExtremeImageSecurity_Object = MibTableColumn
extremeImageSecurity = _ExtremeImageSecurity_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 34, 1, 11),
    _ExtremeImageSecurity_Type()
)
extremeImageSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeImageSecurity.setStatus("deprecated")
_ExtremePatchVersion_Type = Integer32
_ExtremePatchVersion_Object = MibTableColumn
extremePatchVersion = _ExtremePatchVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 34, 1, 12),
    _ExtremePatchVersion_Type()
)
extremePatchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePatchVersion.setStatus("current")
_ExtremeImageFeatureTable_Object = MibTable
extremeImageFeatureTable = _ExtremeImageFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 35)
)
if mibBuilder.loadTexts:
    extremeImageFeatureTable.setStatus("current")
_ExtremeImageFeatureEntry_Object = MibTableRow
extremeImageFeatureEntry = _ExtremeImageFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 35, 1)
)
extremeImageFeatureEntry.setIndexNames(
    (0, "EXTREME-SYSTEM-MIB", "extremeImageFeatureNumber"),
)
if mibBuilder.loadTexts:
    extremeImageFeatureEntry.setStatus("current")


class _ExtremeImageFeatureNumber_Type(Integer32):
    """Custom type extremeImageFeatureNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cur", 0),
          ("pri", 1),
          ("sec", 2))
    )


_ExtremeImageFeatureNumber_Type.__name__ = "Integer32"
_ExtremeImageFeatureNumber_Object = MibTableColumn
extremeImageFeatureNumber = _ExtremeImageFeatureNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 35, 1, 1),
    _ExtremeImageFeatureNumber_Type()
)
extremeImageFeatureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeImageFeatureNumber.setStatus("current")


class _ExtremeImageSshCapability_Type(Integer32):
    """Custom type extremeImageSshCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nossh", 1),
          ("ssh", 2),
          ("unknown", 0))
    )


_ExtremeImageSshCapability_Type.__name__ = "Integer32"
_ExtremeImageSshCapability_Object = MibTableColumn
extremeImageSshCapability = _ExtremeImageSshCapability_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 35, 1, 2),
    _ExtremeImageSshCapability_Type()
)
extremeImageSshCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeImageSshCapability.setStatus("current")


class _ExtremeImageUAACapability_Type(Integer32):
    """Custom type extremeImageUAACapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nouaa", 1),
          ("uaa", 2),
          ("unknown", 0))
    )


_ExtremeImageUAACapability_Type.__name__ = "Integer32"
_ExtremeImageUAACapability_Object = MibTableColumn
extremeImageUAACapability = _ExtremeImageUAACapability_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 1, 35, 1, 3),
    _ExtremeImageUAACapability_Type()
)
extremeImageUAACapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeImageUAACapability.setStatus("current")
_ExtremeChassisGroup_ObjectIdentity = ObjectIdentity
extremeChassisGroup = _ExtremeChassisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 2)
)
_ExtremeMasterMSMSlot_Type = Integer32
_ExtremeMasterMSMSlot_Object = MibScalar
extremeMasterMSMSlot = _ExtremeMasterMSMSlot_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 2, 1),
    _ExtremeMasterMSMSlot_Type()
)
extremeMasterMSMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMasterMSMSlot.setStatus("current")
_ExtremeSlotTable_Object = MibTable
extremeSlotTable = _ExtremeSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    extremeSlotTable.setStatus("current")
_ExtremeSlotEntry_Object = MibTableRow
extremeSlotEntry = _ExtremeSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 2, 2, 1)
)
extremeSlotEntry.setIndexNames(
    (0, "EXTREME-SYSTEM-MIB", "extremeSlotNumber"),
)
if mibBuilder.loadTexts:
    extremeSlotEntry.setStatus("current")
_ExtremeSlotNumber_Type = Integer32
_ExtremeSlotNumber_Object = MibTableColumn
extremeSlotNumber = _ExtremeSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 2, 2, 1, 1),
    _ExtremeSlotNumber_Type()
)
extremeSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSlotNumber.setStatus("current")
_ExtremeSlotName_Type = DisplayString
_ExtremeSlotName_Object = MibTableColumn
extremeSlotName = _ExtremeSlotName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 2, 2, 1, 2),
    _ExtremeSlotName_Type()
)
extremeSlotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSlotName.setStatus("current")


class _ExtremeSlotModuleConfiguredType_Type(Integer32):
    """Custom type extremeSlotModuleConfiguredType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              10,
              11,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              50,
              51,
              52,
              53,
              54,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              200,
              201)
        )
    )
    namedValues = NamedValues(
        *(("a12c", 108),
          ("a3c", 107),
          ("arm", 103),
          ("f32fi", 31),
          ("f48ti", 7),
          ("f96ti", 29),
          ("fe32", 2),
          ("fe32fx", 5),
          ("fm16t3", 38),
          ("fm24f", 26),
          ("fm24sf", 27),
          ("fm24te", 28),
          ("fm32p", 39),
          ("fm32t", 21),
          ("fm8v", 50),
          ("g12sxi", 10),
          ("g12ti", 11),
          ("g16x3", 34),
          ("g24t3", 35),
          ("g4x", 3),
          ("g6x", 4),
          ("g8ti", 9),
          ("g8xi", 8),
          ("gm16t3", 37),
          ("gm16x3", 36),
          ("gm4sx", 23),
          ("gm4t", 24),
          ("gm4x", 22),
          ("mpls", 104),
          ("none", 1),
          ("p12c", 102),
          ("p3c", 101),
          ("p48c", 106),
          ("pxm", 200),
          ("s300fixed", 201),
          ("sma", 105),
          ("tenGigLR", 33),
          ("tenGx3", 32),
          ("wdm4", 30),
          ("wdm8", 25),
          ("wm1t3", 53),
          ("wm4e1", 54),
          ("wm4t1", 51),
          ("wm4t3", 52))
    )


_ExtremeSlotModuleConfiguredType_Type.__name__ = "Integer32"
_ExtremeSlotModuleConfiguredType_Object = MibTableColumn
extremeSlotModuleConfiguredType = _ExtremeSlotModuleConfiguredType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 2, 2, 1, 3),
    _ExtremeSlotModuleConfiguredType_Type()
)
extremeSlotModuleConfiguredType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeSlotModuleConfiguredType.setStatus("current")


class _ExtremeSlotModuleInsertedType_Type(Integer32):
    """Custom type extremeSlotModuleInsertedType based on Integer32"""
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
              10,
              11,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              50,
              51,
              52,
              53,
              54,
              55,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              200,
              201,
              202)
        )
    )
    namedValues = NamedValues(
        *(("a12c", 108),
          ("a3c", 107),
          ("alpine3802", 55),
          ("alpine3804", 20),
          ("alpine3808", 19),
          ("arm", 103),
          ("f32fi", 31),
          ("f48ti", 7),
          ("f96ti", 29),
          ("fe32", 2),
          ("fe32fx", 5),
          ("fm16t3", 38),
          ("fm24f", 26),
          ("fm24sf", 27),
          ("fm24te", 28),
          ("fm32p", 39),
          ("fm32t", 21),
          ("fm8v", 50),
          ("g12sxi", 10),
          ("g12ti", 11),
          ("g16x3", 34),
          ("g24t3", 35),
          ("g4x", 3),
          ("g6x", 4),
          ("g8ti", 9),
          ("g8xi", 8),
          ("gm16t3", 37),
          ("gm16x3", 36),
          ("gm4sx", 23),
          ("gm4t", 24),
          ("gm4x", 22),
          ("mpls", 104),
          ("msm", 6),
          ("msm3", 202),
          ("msm64i", 18),
          ("none", 1),
          ("p12c", 102),
          ("p3c", 101),
          ("p48c", 106),
          ("pxm", 200),
          ("s300fixed", 201),
          ("sma", 105),
          ("tenGigLR", 33),
          ("tenGx3", 32),
          ("wdm4", 30),
          ("wdm8", 25),
          ("wm1t3", 53),
          ("wm4e1", 54),
          ("wm4t1", 51),
          ("wm4t3", 52))
    )


_ExtremeSlotModuleInsertedType_Type.__name__ = "Integer32"
_ExtremeSlotModuleInsertedType_Object = MibTableColumn
extremeSlotModuleInsertedType = _ExtremeSlotModuleInsertedType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 2, 2, 1, 4),
    _ExtremeSlotModuleInsertedType_Type()
)
extremeSlotModuleInsertedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSlotModuleInsertedType.setStatus("current")


class _ExtremeSlotModuleState_Type(Integer32):
    """Custom type extremeSlotModuleState based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              100)
        )
    )
    namedValues = NamedValues(
        *(("booting", 12),
          ("downloading", 11),
          ("failed", 4),
          ("initializing", 14),
          ("invalid", 100),
          ("mismatch", 3),
          ("notPresent", 1),
          ("offline", 13),
          ("operational", 5),
          ("post", 10),
          ("powerdown", 6),
          ("poweron", 9),
          ("present", 8),
          ("testing", 2),
          ("unknown", 7))
    )


_ExtremeSlotModuleState_Type.__name__ = "Integer32"
_ExtremeSlotModuleState_Object = MibTableColumn
extremeSlotModuleState = _ExtremeSlotModuleState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 2, 2, 1, 5),
    _ExtremeSlotModuleState_Type()
)
extremeSlotModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSlotModuleState.setStatus("current")
_ExtremeSlotModuleSerialNumber_Type = DisplayString
_ExtremeSlotModuleSerialNumber_Object = MibTableColumn
extremeSlotModuleSerialNumber = _ExtremeSlotModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 2, 2, 1, 6),
    _ExtremeSlotModuleSerialNumber_Type()
)
extremeSlotModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSlotModuleSerialNumber.setStatus("current")
_ExtremeChassisPortsPerSlot_Type = Integer32
_ExtremeChassisPortsPerSlot_Object = MibScalar
extremeChassisPortsPerSlot = _ExtremeChassisPortsPerSlot_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 2, 3),
    _ExtremeChassisPortsPerSlot_Type()
)
extremeChassisPortsPerSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeChassisPortsPerSlot.setStatus("current")
_ExtremeSystemHealthCheck_ObjectIdentity = ObjectIdentity
extremeSystemHealthCheck = _ExtremeSystemHealthCheck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 3)
)


class _ExtremeHealthCheckErrorType_Type(Integer32):
    """Custom type extremeHealthCheckErrorType based on Integer32"""
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
        *(("backplane", 3),
          ("cpuPacket", 2),
          ("hardwareFail", 4),
          ("pbusChecksum", 5),
          ("unknown", 1))
    )


_ExtremeHealthCheckErrorType_Type.__name__ = "Integer32"
_ExtremeHealthCheckErrorType_Object = MibScalar
extremeHealthCheckErrorType = _ExtremeHealthCheckErrorType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 3, 1),
    _ExtremeHealthCheckErrorType_Type()
)
extremeHealthCheckErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeHealthCheckErrorType.setStatus("current")


class _ExtremeHealthCheckAction_Type(Integer32):
    """Custom type extremeHealthCheckAction based on Integer32"""
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
        *(("autoRecovery", 5),
          ("healthCheckTrap", 2),
          ("ioModuleDown", 3),
          ("syslogOnly", 1),
          ("systemDown", 4))
    )


_ExtremeHealthCheckAction_Type.__name__ = "Integer32"
_ExtremeHealthCheckAction_Object = MibScalar
extremeHealthCheckAction = _ExtremeHealthCheckAction_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 3, 2),
    _ExtremeHealthCheckAction_Type()
)
extremeHealthCheckAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeHealthCheckAction.setStatus("current")
_ExtremeHealthCheckMaxRetries_Type = Integer32
_ExtremeHealthCheckMaxRetries_Object = MibScalar
extremeHealthCheckMaxRetries = _ExtremeHealthCheckMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 3, 3),
    _ExtremeHealthCheckMaxRetries_Type()
)
extremeHealthCheckMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeHealthCheckMaxRetries.setStatus("current")
_ExtremeSystemThresholds_ObjectIdentity = ObjectIdentity
extremeSystemThresholds = _ExtremeSystemThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 4)
)


class _ExtremeCpuUtilRisingThreshold_Type(Integer32):
    """Custom type extremeCpuUtilRisingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ExtremeCpuUtilRisingThreshold_Type.__name__ = "Integer32"
_ExtremeCpuUtilRisingThreshold_Object = MibScalar
extremeCpuUtilRisingThreshold = _ExtremeCpuUtilRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 4, 1),
    _ExtremeCpuUtilRisingThreshold_Type()
)
extremeCpuUtilRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeCpuUtilRisingThreshold.setStatus("current")
_ExtremeCpuTaskUtilPair_Type = DisplayString
_ExtremeCpuTaskUtilPair_Object = MibScalar
extremeCpuTaskUtilPair = _ExtremeCpuTaskUtilPair_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1, 4, 2),
    _ExtremeCpuTaskUtilPair_Type()
)
extremeCpuTaskUtilPair.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeCpuTaskUtilPair.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-SYSTEM-MIB",
    **{"extremeSystem": extremeSystem,
       "extremeSystemCommon": extremeSystemCommon,
       "extremeSaveConfiguration": extremeSaveConfiguration,
       "extremeSaveStatus": extremeSaveStatus,
       "extremeCurrentConfigInUse": extremeCurrentConfigInUse,
       "extremeConfigToUseOnReboot": extremeConfigToUseOnReboot,
       "extremeOverTemperatureAlarm": extremeOverTemperatureAlarm,
       "extremeCurrentTemperature": extremeCurrentTemperature,
       "extremeFanStatusTable": extremeFanStatusTable,
       "extremeFanStatusEntry": extremeFanStatusEntry,
       "extremeFanNumber": extremeFanNumber,
       "extremeFanOperational": extremeFanOperational,
       "extremeFanEntPhysicalIndex": extremeFanEntPhysicalIndex,
       "extremePrimaryPowerOperational": extremePrimaryPowerOperational,
       "extremeRedundantPowerStatus": extremeRedundantPowerStatus,
       "extremeRedundantPowerAlarm": extremeRedundantPowerAlarm,
       "extremePrimarySoftwareRev": extremePrimarySoftwareRev,
       "extremeSecondarySoftwareRev": extremeSecondarySoftwareRev,
       "extremeImageToUseOnReboot": extremeImageToUseOnReboot,
       "extremeSystemID": extremeSystemID,
       "extremeSystemBoardID": extremeSystemBoardID,
       "extremeSystemLeftBoardID": extremeSystemLeftBoardID,
       "extremeSystemRightBoardID": extremeSystemRightBoardID,
       "extremeInputPowerVoltage": extremeInputPowerVoltage,
       "extremePowerStatus": extremePowerStatus,
       "extremePowerAlarm": extremePowerAlarm,
       "extremeRmonEnable": extremeRmonEnable,
       "extremeBootROMVersion": extremeBootROMVersion,
       "extremeDot1dTpFdbTableEnable": extremeDot1dTpFdbTableEnable,
       "extremePowerSupplyTable": extremePowerSupplyTable,
       "extremePowerSupplyEntry": extremePowerSupplyEntry,
       "extremePowerSupplyNumber": extremePowerSupplyNumber,
       "extremePowerSupplyStatus": extremePowerSupplyStatus,
       "extremePowerSupplyInputVoltage": extremePowerSupplyInputVoltage,
       "extremePowerSupplySerialNumber": extremePowerSupplySerialNumber,
       "extremePowerSupplyEntPhysicalIndex": extremePowerSupplyEntPhysicalIndex,
       "extremeCpuAggregateUtilization": extremeCpuAggregateUtilization,
       "extremeCpuTask2Table": extremeCpuTask2Table,
       "extremeCpuTask2Entry": extremeCpuTask2Entry,
       "extremeCpuTask2CpuId": extremeCpuTask2CpuId,
       "extremeCpuTask2Name": extremeCpuTask2Name,
       "extremeCpuTask2Id": extremeCpuTask2Id,
       "extremeCpuTask2Pc": extremeCpuTask2Pc,
       "extremeCpuTask2Status": extremeCpuTask2Status,
       "extremeCpuTask2Utilization": extremeCpuTask2Utilization,
       "extremeCpuTask2MaxUtilization": extremeCpuTask2MaxUtilization,
       "extremeAuthFailSrcAddr": extremeAuthFailSrcAddr,
       "extremeCpuTransmitPriority": extremeCpuTransmitPriority,
       "extremeImageBooted": extremeImageBooted,
       "extremeMsmFailoverCause": extremeMsmFailoverCause,
       "extremeImageTable": extremeImageTable,
       "extremeImageEntry": extremeImageEntry,
       "extremeImageNumber": extremeImageNumber,
       "extremeMajorVersion": extremeMajorVersion,
       "extremeSubMajorVersion": extremeSubMajorVersion,
       "extremeMinorVersion": extremeMinorVersion,
       "extremeBuildNumber": extremeBuildNumber,
       "extremeTechnologyReleaseNumber": extremeTechnologyReleaseNumber,
       "extremeSustainingReleaseNumber": extremeSustainingReleaseNumber,
       "extremeBranchRevisionNumber": extremeBranchRevisionNumber,
       "extremeImageType": extremeImageType,
       "extremeImageDescription": extremeImageDescription,
       "extremeImageSecurity": extremeImageSecurity,
       "extremePatchVersion": extremePatchVersion,
       "extremeImageFeatureTable": extremeImageFeatureTable,
       "extremeImageFeatureEntry": extremeImageFeatureEntry,
       "extremeImageFeatureNumber": extremeImageFeatureNumber,
       "extremeImageSshCapability": extremeImageSshCapability,
       "extremeImageUAACapability": extremeImageUAACapability,
       "extremeChassisGroup": extremeChassisGroup,
       "extremeMasterMSMSlot": extremeMasterMSMSlot,
       "extremeSlotTable": extremeSlotTable,
       "extremeSlotEntry": extremeSlotEntry,
       "extremeSlotNumber": extremeSlotNumber,
       "extremeSlotName": extremeSlotName,
       "extremeSlotModuleConfiguredType": extremeSlotModuleConfiguredType,
       "extremeSlotModuleInsertedType": extremeSlotModuleInsertedType,
       "extremeSlotModuleState": extremeSlotModuleState,
       "extremeSlotModuleSerialNumber": extremeSlotModuleSerialNumber,
       "extremeChassisPortsPerSlot": extremeChassisPortsPerSlot,
       "extremeSystemHealthCheck": extremeSystemHealthCheck,
       "extremeHealthCheckErrorType": extremeHealthCheckErrorType,
       "extremeHealthCheckAction": extremeHealthCheckAction,
       "extremeHealthCheckMaxRetries": extremeHealthCheckMaxRetries,
       "extremeSystemThresholds": extremeSystemThresholds,
       "extremeCpuUtilRisingThreshold": extremeCpuUtilRisingThreshold,
       "extremeCpuTaskUtilPair": extremeCpuTaskUtilPair}
)
