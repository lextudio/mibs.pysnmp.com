# SNMP MIB module (HUAWEI-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-POE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:32 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwPoeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwPoeGlobalObjects_ObjectIdentity = ObjectIdentity
hwPoeGlobalObjects = _HwPoeGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 1)
)
_HwPoePower_Type = Integer32
_HwPoePower_Object = MibScalar
hwPoePower = _HwPoePower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 1, 1),
    _HwPoePower_Type()
)
hwPoePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoePower.setStatus("current")
_HwPoePowerRsvPercent_Type = Integer32
_HwPoePowerRsvPercent_Object = MibScalar
hwPoePowerRsvPercent = _HwPoePowerRsvPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 1, 4),
    _HwPoePowerRsvPercent_Type()
)
hwPoePowerRsvPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPoePowerRsvPercent.setStatus("current")
_HwPoePowerUtilizationThreshold_Type = Integer32
_HwPoePowerUtilizationThreshold_Object = MibScalar
hwPoePowerUtilizationThreshold = _HwPoePowerUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 1, 5),
    _HwPoePowerUtilizationThreshold_Type()
)
hwPoePowerUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPoePowerUtilizationThreshold.setStatus("current")
_HwPoeSlotTable_Object = MibTable
hwPoeSlotTable = _HwPoeSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2)
)
if mibBuilder.loadTexts:
    hwPoeSlotTable.setStatus("current")
_HwPoeSlotEntry_Object = MibTableRow
hwPoeSlotEntry = _HwPoeSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1)
)
hwPoeSlotEntry.setIndexNames(
    (0, "HUAWEI-POE-MIB", "hwPoeSlotId"),
)
if mibBuilder.loadTexts:
    hwPoeSlotEntry.setStatus("current")


class _HwPoeSlotId_Type(Integer32):
    """Custom type hwPoeSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwPoeSlotId_Type.__name__ = "Integer32"
_HwPoeSlotId_Object = MibTableColumn
hwPoeSlotId = _HwPoeSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 1),
    _HwPoeSlotId_Type()
)
hwPoeSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPoeSlotId.setStatus("current")


class _HwPoeSlotMaximumPower_Type(Integer32):
    """Custom type hwPoeSlotMaximumPower based on Integer32"""
    defaultHexValue = 1776000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1600000),
    )


_HwPoeSlotMaximumPower_Type.__name__ = "Integer32"
_HwPoeSlotMaximumPower_Object = MibTableColumn
hwPoeSlotMaximumPower = _HwPoeSlotMaximumPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 2),
    _HwPoeSlotMaximumPower_Type()
)
hwPoeSlotMaximumPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPoeSlotMaximumPower.setStatus("current")
if mibBuilder.loadTexts:
    hwPoeSlotMaximumPower.setUnits("mW")
_HwPoeSlotAvailablePower_Type = Integer32
_HwPoeSlotAvailablePower_Object = MibTableColumn
hwPoeSlotAvailablePower = _HwPoeSlotAvailablePower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 3),
    _HwPoeSlotAvailablePower_Type()
)
hwPoeSlotAvailablePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoeSlotAvailablePower.setStatus("current")
_HwPoeSlotReferencePower_Type = Integer32
_HwPoeSlotReferencePower_Object = MibTableColumn
hwPoeSlotReferencePower = _HwPoeSlotReferencePower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 4),
    _HwPoeSlotReferencePower_Type()
)
hwPoeSlotReferencePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoeSlotReferencePower.setStatus("current")
_HwPoeSlotConsumingPower_Type = Integer32
_HwPoeSlotConsumingPower_Object = MibTableColumn
hwPoeSlotConsumingPower = _HwPoeSlotConsumingPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 5),
    _HwPoeSlotConsumingPower_Type()
)
hwPoeSlotConsumingPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoeSlotConsumingPower.setStatus("current")
_HwPoeSlotPeakPower_Type = Integer32
_HwPoeSlotPeakPower_Object = MibTableColumn
hwPoeSlotPeakPower = _HwPoeSlotPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 6),
    _HwPoeSlotPeakPower_Type()
)
hwPoeSlotPeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoeSlotPeakPower.setStatus("current")


class _HwPoeSlotLegacyDetect_Type(EnabledStatus):
    """Custom type hwPoeSlotLegacyDetect based on EnabledStatus"""


_HwPoeSlotLegacyDetect_Object = MibTableColumn
hwPoeSlotLegacyDetect = _HwPoeSlotLegacyDetect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 7),
    _HwPoeSlotLegacyDetect_Type()
)
hwPoeSlotLegacyDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPoeSlotLegacyDetect.setStatus("current")


class _HwPoeSlotPowerManagementManner_Type(Integer32):
    """Custom type hwPoeSlotPowerManagementManner based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("manual", 1))
    )


_HwPoeSlotPowerManagementManner_Type.__name__ = "Integer32"
_HwPoeSlotPowerManagementManner_Object = MibTableColumn
hwPoeSlotPowerManagementManner = _HwPoeSlotPowerManagementManner_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 8),
    _HwPoeSlotPowerManagementManner_Type()
)
hwPoeSlotPowerManagementManner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPoeSlotPowerManagementManner.setStatus("current")
_HwPoeSlotIsPoeDevice_Type = OctetString
_HwPoeSlotIsPoeDevice_Object = MibTableColumn
hwPoeSlotIsPoeDevice = _HwPoeSlotIsPoeDevice_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 9),
    _HwPoeSlotIsPoeDevice_Type()
)
hwPoeSlotIsPoeDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoeSlotIsPoeDevice.setStatus("current")


class _HwPoeDimmId_Type(Integer32):
    """Custom type hwPoeDimmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwPoeDimmId_Type.__name__ = "Integer32"
_HwPoeDimmId_Object = MibTableColumn
hwPoeDimmId = _HwPoeDimmId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 10),
    _HwPoeDimmId_Type()
)
hwPoeDimmId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPoeDimmId.setStatus("current")
_HwPoeSlotPowerRsvPercent_Type = Integer32
_HwPoeSlotPowerRsvPercent_Object = MibTableColumn
hwPoeSlotPowerRsvPercent = _HwPoeSlotPowerRsvPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 11),
    _HwPoeSlotPowerRsvPercent_Type()
)
hwPoeSlotPowerRsvPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPoeSlotPowerRsvPercent.setStatus("current")
_HwPoeSlotPowerUtilizationThreshold_Type = Integer32
_HwPoeSlotPowerUtilizationThreshold_Object = MibTableColumn
hwPoeSlotPowerUtilizationThreshold = _HwPoeSlotPowerUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 12),
    _HwPoeSlotPowerUtilizationThreshold_Type()
)
hwPoeSlotPowerUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPoeSlotPowerUtilizationThreshold.setStatus("current")
_HwPoePortTable_Object = MibTable
hwPoePortTable = _HwPoePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3)
)
if mibBuilder.loadTexts:
    hwPoePortTable.setStatus("current")
_HwPoePortEntry_Object = MibTableRow
hwPoePortEntry = _HwPoePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1)
)
hwPoePortEntry.setIndexNames(
    (0, "HUAWEI-POE-MIB", "hwPoePortIfIndex"),
)
if mibBuilder.loadTexts:
    hwPoePortEntry.setStatus("current")
_HwPoePortIfIndex_Type = InterfaceIndex
_HwPoePortIfIndex_Object = MibTableColumn
hwPoePortIfIndex = _HwPoePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 1),
    _HwPoePortIfIndex_Type()
)
hwPoePortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPoePortIfIndex.setStatus("current")
_HwPoePortName_Type = OctetString
_HwPoePortName_Object = MibTableColumn
hwPoePortName = _HwPoePortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 2),
    _HwPoePortName_Type()
)
hwPoePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoePortName.setStatus("current")


class _HwPoePortEnable_Type(EnabledStatus):
    """Custom type hwPoePortEnable based on EnabledStatus"""


_HwPoePortEnable_Object = MibTableColumn
hwPoePortEnable = _HwPoePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 3),
    _HwPoePortEnable_Type()
)
hwPoePortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPoePortEnable.setStatus("current")


class _HwPoePortPriority_Type(Integer32):
    """Custom type hwPoePortPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 3))
    )


_HwPoePortPriority_Type.__name__ = "Integer32"
_HwPoePortPriority_Object = MibTableColumn
hwPoePortPriority = _HwPoePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 4),
    _HwPoePortPriority_Type()
)
hwPoePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPoePortPriority.setStatus("current")


class _HwPoePortMaximumPower_Type(Integer32):
    """Custom type hwPoePortMaximumPower based on Integer32"""
    defaultHexValue = 37000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_HwPoePortMaximumPower_Type.__name__ = "Integer32"
_HwPoePortMaximumPower_Object = MibTableColumn
hwPoePortMaximumPower = _HwPoePortMaximumPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 5),
    _HwPoePortMaximumPower_Type()
)
hwPoePortMaximumPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPoePortMaximumPower.setStatus("current")
if mibBuilder.loadTexts:
    hwPoePortMaximumPower.setUnits("mW")
_HwPoePortPowerOnStatus_Type = OctetString
_HwPoePortPowerOnStatus_Object = MibTableColumn
hwPoePortPowerOnStatus = _HwPoePortPowerOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 6),
    _HwPoePortPowerOnStatus_Type()
)
hwPoePortPowerOnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoePortPowerOnStatus.setStatus("current")
_HwPoePortPowerStatus_Type = OctetString
_HwPoePortPowerStatus_Object = MibTableColumn
hwPoePortPowerStatus = _HwPoePortPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 7),
    _HwPoePortPowerStatus_Type()
)
hwPoePortPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoePortPowerStatus.setStatus("current")


class _HwPoePortPdClass_Type(Integer32):
    """Custom type hwPoePortPdClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwPoePortPdClass_Type.__name__ = "Integer32"
_HwPoePortPdClass_Object = MibTableColumn
hwPoePortPdClass = _HwPoePortPdClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 8),
    _HwPoePortPdClass_Type()
)
hwPoePortPdClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoePortPdClass.setStatus("current")


class _HwPoePortReferencePower_Type(Integer32):
    """Custom type hwPoePortReferencePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_HwPoePortReferencePower_Type.__name__ = "Integer32"
_HwPoePortReferencePower_Object = MibTableColumn
hwPoePortReferencePower = _HwPoePortReferencePower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 9),
    _HwPoePortReferencePower_Type()
)
hwPoePortReferencePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoePortReferencePower.setStatus("current")


class _HwPoePortConsumingPower_Type(Integer32):
    """Custom type hwPoePortConsumingPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_HwPoePortConsumingPower_Type.__name__ = "Integer32"
_HwPoePortConsumingPower_Object = MibTableColumn
hwPoePortConsumingPower = _HwPoePortConsumingPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 10),
    _HwPoePortConsumingPower_Type()
)
hwPoePortConsumingPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoePortConsumingPower.setStatus("current")


class _HwPoePortPeakPower_Type(Integer32):
    """Custom type hwPoePortPeakPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_HwPoePortPeakPower_Type.__name__ = "Integer32"
_HwPoePortPeakPower_Object = MibTableColumn
hwPoePortPeakPower = _HwPoePortPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 11),
    _HwPoePortPeakPower_Type()
)
hwPoePortPeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoePortPeakPower.setStatus("current")


class _HwPoePortAveragePower_Type(Integer32):
    """Custom type hwPoePortAveragePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_HwPoePortAveragePower_Type.__name__ = "Integer32"
_HwPoePortAveragePower_Object = MibTableColumn
hwPoePortAveragePower = _HwPoePortAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 12),
    _HwPoePortAveragePower_Type()
)
hwPoePortAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoePortAveragePower.setStatus("current")
_HwPoePortCurrent_Type = OctetString
_HwPoePortCurrent_Object = MibTableColumn
hwPoePortCurrent = _HwPoePortCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 13),
    _HwPoePortCurrent_Type()
)
hwPoePortCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoePortCurrent.setStatus("current")
_HwPoePortVoltage_Type = OctetString
_HwPoePortVoltage_Object = MibTableColumn
hwPoePortVoltage = _HwPoePortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 14),
    _HwPoePortVoltage_Type()
)
hwPoePortVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoePortVoltage.setStatus("current")


class _HwPoePortManualOperation_Type(Integer32):
    """Custom type hwPoePortManualOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 1),
          ("powerOn", 2))
    )


_HwPoePortManualOperation_Type.__name__ = "Integer32"
_HwPoePortManualOperation_Object = MibTableColumn
hwPoePortManualOperation = _HwPoePortManualOperation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 15),
    _HwPoePortManualOperation_Type()
)
hwPoePortManualOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPoePortManualOperation.setStatus("current")
_HwPoeTrapObjects_ObjectIdentity = ObjectIdentity
hwPoeTrapObjects = _HwPoeTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39)
)


class _HwPoePdPriority_Type(Integer32):
    """Custom type hwPoePdPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 3))
    )


_HwPoePdPriority_Type.__name__ = "Integer32"
_HwPoePdPriority_Object = MibScalar
hwPoePdPriority = _HwPoePdPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 1),
    _HwPoePdPriority_Type()
)
hwPoePdPriority.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPoePdPriority.setStatus("current")
_HwPoeSlotNum_Type = Integer32
_HwPoeSlotNum_Object = MibScalar
hwPoeSlotNum = _HwPoeSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 2),
    _HwPoeSlotNum_Type()
)
hwPoeSlotNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPoeSlotNum.setStatus("current")
_HwPoeCurConsumPower_Type = Integer32
_HwPoeCurConsumPower_Object = MibScalar
hwPoeCurConsumPower = _HwPoeCurConsumPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 3),
    _HwPoeCurConsumPower_Type()
)
hwPoeCurConsumPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPoeCurConsumPower.setStatus("current")
_HwPoeConsumPowerThreshold_Type = Integer32
_HwPoeConsumPowerThreshold_Object = MibScalar
hwPoeConsumPowerThreshold = _HwPoeConsumPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 4),
    _HwPoeConsumPowerThreshold_Type()
)
hwPoeConsumPowerThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPoeConsumPowerThreshold.setStatus("current")
_HwPoeDeviceID_Type = Integer32
_HwPoeDeviceID_Object = MibScalar
hwPoeDeviceID = _HwPoeDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 5),
    _HwPoeDeviceID_Type()
)
hwPoeDeviceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPoeDeviceID.setStatus("current")
_HwFrameID_Type = Integer32
_HwFrameID_Object = MibScalar
hwFrameID = _HwFrameID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 6),
    _HwFrameID_Type()
)
hwFrameID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwFrameID.setStatus("current")
_HwPoeNotification_ObjectIdentity = ObjectIdentity
hwPoeNotification = _HwPoeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40)
)
_HwPoeConformance_ObjectIdentity = ObjectIdentity
hwPoeConformance = _HwPoeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100)
)
_HwPoeGroups_ObjectIdentity = ObjectIdentity
hwPoeGroups = _HwPoeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1)
)

# Managed Objects groups

hwPoeSlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1, 1)
)
hwPoeSlotGroup.setObjects(
      *(("HUAWEI-POE-MIB", "hwPoeSlotMaximumPower"),
        ("HUAWEI-POE-MIB", "hwPoeSlotReferencePower"),
        ("HUAWEI-POE-MIB", "hwPoeSlotConsumingPower"),
        ("HUAWEI-POE-MIB", "hwPoeSlotPeakPower"),
        ("HUAWEI-POE-MIB", "hwPoeSlotPowerManagementManner"),
        ("HUAWEI-POE-MIB", "hwPoeSlotIsPoeDevice"),
        ("HUAWEI-POE-MIB", "hwPoeSlotLegacyDetect"),
        ("HUAWEI-POE-MIB", "hwPoeSlotPowerRsvPercent"),
        ("HUAWEI-POE-MIB", "hwPoeSlotPowerUtilizationThreshold"),
        ("HUAWEI-POE-MIB", "hwPoeDimmId"),
        ("HUAWEI-POE-MIB", "hwPoeSlotAvailablePower"))
)
if mibBuilder.loadTexts:
    hwPoeSlotGroup.setStatus("current")

hwPoePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1, 2)
)
hwPoePortGroup.setObjects(
      *(("HUAWEI-POE-MIB", "hwPoePortEnable"),
        ("HUAWEI-POE-MIB", "hwPoePortPriority"),
        ("HUAWEI-POE-MIB", "hwPoePortMaximumPower"),
        ("HUAWEI-POE-MIB", "hwPoePortPowerOnStatus"),
        ("HUAWEI-POE-MIB", "hwPoePortPowerStatus"),
        ("HUAWEI-POE-MIB", "hwPoePortReferencePower"),
        ("HUAWEI-POE-MIB", "hwPoePortName"),
        ("HUAWEI-POE-MIB", "hwPoePortConsumingPower"),
        ("HUAWEI-POE-MIB", "hwPoePortPeakPower"),
        ("HUAWEI-POE-MIB", "hwPoePortAveragePower"),
        ("HUAWEI-POE-MIB", "hwPoePortCurrent"),
        ("HUAWEI-POE-MIB", "hwPoePortVoltage"),
        ("HUAWEI-POE-MIB", "hwPoePortManualOperation"),
        ("HUAWEI-POE-MIB", "hwPoePortPdClass"))
)
if mibBuilder.loadTexts:
    hwPoePortGroup.setStatus("current")

hwPoeGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1, 3)
)
hwPoeGlobalGroup.setObjects(
      *(("HUAWEI-POE-MIB", "hwPoePowerUtilizationThreshold"),
        ("HUAWEI-POE-MIB", "hwPoePowerRsvPercent"),
        ("HUAWEI-POE-MIB", "hwPoePower"))
)
if mibBuilder.loadTexts:
    hwPoeGlobalGroup.setStatus("current")

hwPoeTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1, 5)
)
hwPoeTrapObjectsGroup.setObjects(
      *(("HUAWEI-POE-MIB", "hwPoePdPriority"),
        ("HUAWEI-POE-MIB", "hwPoeSlotNum"),
        ("HUAWEI-POE-MIB", "hwPoeCurConsumPower"),
        ("HUAWEI-POE-MIB", "hwPoeConsumPowerThreshold"),
        ("HUAWEI-POE-MIB", "hwPoeDeviceID"),
        ("HUAWEI-POE-MIB", "hwFrameID"))
)
if mibBuilder.loadTexts:
    hwPoeTrapObjectsGroup.setStatus("current")


# Notification objects

hwPoeDimmError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 1)
)
hwPoeDimmError.setObjects(
      *(("HUAWEI-POE-MIB", "hwPoeSlotNum"),
        ("HUAWEI-POE-MIB", "hwPoeDimmId"))
)
if mibBuilder.loadTexts:
    hwPoeDimmError.setStatus(
        "current"
    )

hwPoePowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 2)
)
hwPoePowerOff.setObjects(
    ("HUAWEI-POE-MIB", "hwPoePortName")
)
if mibBuilder.loadTexts:
    hwPoePowerOff.setStatus(
        "current"
    )

hwPoePowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 3)
)
hwPoePowerOn.setObjects(
    ("HUAWEI-POE-MIB", "hwPoePortName")
)
if mibBuilder.loadTexts:
    hwPoePowerOn.setStatus(
        "current"
    )

hwPoeSlotPowerOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 4)
)
hwPoeSlotPowerOverload.setObjects(
      *(("HUAWEI-POE-MIB", "hwPoeSlotNum"),
        ("HUAWEI-POE-MIB", "hwPoeSlotConsumingPower"))
)
if mibBuilder.loadTexts:
    hwPoeSlotPowerOverload.setStatus(
        "current"
    )

hwPoeSlotPowerOverloadResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 5)
)
hwPoeSlotPowerOverloadResume.setObjects(
      *(("HUAWEI-POE-MIB", "hwPoeSlotNum"),
        ("HUAWEI-POE-MIB", "hwPoeSlotConsumingPower"))
)
if mibBuilder.loadTexts:
    hwPoeSlotPowerOverloadResume.setStatus(
        "current"
    )

hwPoePdPowerOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 6)
)
hwPoePdPowerOverload.setObjects(
      *(("HUAWEI-POE-MIB", "hwPoePortName"),
        ("HUAWEI-POE-MIB", "hwPoePortConsumingPower"),
        ("HUAWEI-POE-MIB", "hwPoePortMaximumPower"))
)
if mibBuilder.loadTexts:
    hwPoePdPowerOverload.setStatus(
        "current"
    )

hwPoePdPowerOverloadResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 7)
)
hwPoePdPowerOverloadResume.setObjects(
      *(("HUAWEI-POE-MIB", "hwPoePortName"),
        ("HUAWEI-POE-MIB", "hwPoePortConsumingPower"),
        ("HUAWEI-POE-MIB", "hwPoePortMaximumPower"))
)
if mibBuilder.loadTexts:
    hwPoePdPowerOverloadResume.setStatus(
        "current"
    )

hwPoePdConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 8)
)
hwPoePdConnected.setObjects(
    ("HUAWEI-POE-MIB", "hwPoePortName")
)
if mibBuilder.loadTexts:
    hwPoePdConnected.setStatus(
        "current"
    )

hwPoePdDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 9)
)
hwPoePdDisconnected.setObjects(
    ("HUAWEI-POE-MIB", "hwPoePortName")
)
if mibBuilder.loadTexts:
    hwPoePdDisconnected.setStatus(
        "current"
    )

hwPoePdClassInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 10)
)
hwPoePdClassInvalid.setObjects(
    ("HUAWEI-POE-MIB", "hwPoePortName")
)
if mibBuilder.loadTexts:
    hwPoePdClassInvalid.setStatus(
        "current"
    )

hwPoePdClassOvercurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 11)
)
hwPoePdClassOvercurrent.setObjects(
    ("HUAWEI-POE-MIB", "hwPoePortName")
)
if mibBuilder.loadTexts:
    hwPoePdClassOvercurrent.setStatus(
        "current"
    )

hwPoePdPowerOvercurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 12)
)
hwPoePdPowerOvercurrent.setObjects(
    ("HUAWEI-POE-MIB", "hwPoePortName")
)
if mibBuilder.loadTexts:
    hwPoePdPowerOvercurrent.setStatus(
        "current"
    )

hwPoePdPowerOvercurrentResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 13)
)
hwPoePdPowerOvercurrentResume.setObjects(
    ("HUAWEI-POE-MIB", "hwPoePortName")
)
if mibBuilder.loadTexts:
    hwPoePdPowerOvercurrentResume.setStatus(
        "current"
    )

hwPoePowerOnFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 14)
)
hwPoePowerOnFail.setObjects(
    ("HUAWEI-POE-MIB", "hwPoePortName")
)
if mibBuilder.loadTexts:
    hwPoePowerOnFail.setStatus(
        "current"
    )

hwPoePowerOffCurrentLimits = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 15)
)
hwPoePowerOffCurrentLimits.setObjects(
    ("HUAWEI-POE-MIB", "hwPoePortName")
)
if mibBuilder.loadTexts:
    hwPoePowerOffCurrentLimits.setStatus(
        "current"
    )

hwPoePdPriorityDifferent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 16)
)
hwPoePdPriorityDifferent.setObjects(
      *(("HUAWEI-POE-MIB", "hwPoePortName"),
        ("HUAWEI-POE-MIB", "hwPoePortPriority"),
        ("HUAWEI-POE-MIB", "hwPoePdPriority"))
)
if mibBuilder.loadTexts:
    hwPoePdPriorityDifferent.setStatus(
        "current"
    )

hwPoePowerOverUtilizationThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 17)
)
hwPoePowerOverUtilizationThreshold.setObjects(
      *(("HUAWEI-POE-MIB", "hwPoeDeviceID"),
        ("HUAWEI-POE-MIB", "hwPoeCurConsumPower"),
        ("HUAWEI-POE-MIB", "hwPoeConsumPowerThreshold"))
)
if mibBuilder.loadTexts:
    hwPoePowerOverUtilizationThreshold.setStatus(
        "current"
    )

hwPoePowerOverUtilizationThresholdResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 18)
)
hwPoePowerOverUtilizationThresholdResume.setObjects(
      *(("HUAWEI-POE-MIB", "hwPoeDeviceID"),
        ("HUAWEI-POE-MIB", "hwPoeCurConsumPower"),
        ("HUAWEI-POE-MIB", "hwPoeConsumPowerThreshold"))
)
if mibBuilder.loadTexts:
    hwPoePowerOverUtilizationThresholdResume.setStatus(
        "current"
    )

hwPoeBoardInsertedWrongFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 19)
)
hwPoeBoardInsertedWrongFrame.setObjects(
      *(("HUAWEI-POE-MIB", "hwFrameID"),
        ("HUAWEI-POE-MIB", "hwPoeSlotNum"))
)
if mibBuilder.loadTexts:
    hwPoeBoardInsertedWrongFrame.setStatus(
        "current"
    )

hwPoePowerAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 20)
)
hwPoePowerAbsent.setObjects(
      *(("HUAWEI-POE-MIB", "hwFrameID"),
        ("HUAWEI-POE-MIB", "hwPoeSlotNum"))
)
if mibBuilder.loadTexts:
    hwPoePowerAbsent.setStatus(
        "current"
    )

hwPoePowerAbsentResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 21)
)
hwPoePowerAbsentResume.setObjects(
      *(("HUAWEI-POE-MIB", "hwFrameID"),
        ("HUAWEI-POE-MIB", "hwPoeSlotNum"))
)
if mibBuilder.loadTexts:
    hwPoePowerAbsentResume.setStatus(
        "current"
    )

hwPoeRpsPowerOutputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 22)
)
hwPoeRpsPowerOutputAlarm.setObjects(
    ("HUAWEI-POE-MIB", "hwPoeSlotNum")
)
if mibBuilder.loadTexts:
    hwPoeRpsPowerOutputAlarm.setStatus(
        "current"
    )

hwPoeRpsPowerOutputAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 23)
)
hwPoeRpsPowerOutputAlarmResume.setObjects(
    ("HUAWEI-POE-MIB", "hwPoeSlotNum")
)
if mibBuilder.loadTexts:
    hwPoeRpsPowerOutputAlarmResume.setStatus(
        "current"
    )


# Notifications groups

hwPoeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1, 4)
)
hwPoeNotificationGroup.setObjects(
      *(("HUAWEI-POE-MIB", "hwPoeDimmError"),
        ("HUAWEI-POE-MIB", "hwPoePowerOff"),
        ("HUAWEI-POE-MIB", "hwPoePowerOn"),
        ("HUAWEI-POE-MIB", "hwPoePdPowerOverload"),
        ("HUAWEI-POE-MIB", "hwPoePdPowerOverloadResume"),
        ("HUAWEI-POE-MIB", "hwPoePdConnected"),
        ("HUAWEI-POE-MIB", "hwPoePdDisconnected"),
        ("HUAWEI-POE-MIB", "hwPoePdClassInvalid"),
        ("HUAWEI-POE-MIB", "hwPoePdClassOvercurrent"),
        ("HUAWEI-POE-MIB", "hwPoePdPowerOvercurrent"),
        ("HUAWEI-POE-MIB", "hwPoePdPowerOvercurrentResume"),
        ("HUAWEI-POE-MIB", "hwPoePowerOnFail"),
        ("HUAWEI-POE-MIB", "hwPoePowerOffCurrentLimits"),
        ("HUAWEI-POE-MIB", "hwPoePowerOverUtilizationThresholdResume"),
        ("HUAWEI-POE-MIB", "hwPoePowerOverUtilizationThreshold"),
        ("HUAWEI-POE-MIB", "hwPoePdPriorityDifferent"),
        ("HUAWEI-POE-MIB", "hwPoeSlotPowerOverload"),
        ("HUAWEI-POE-MIB", "hwPoeSlotPowerOverloadResume"),
        ("HUAWEI-POE-MIB", "hwPoeBoardInsertedWrongFrame"),
        ("HUAWEI-POE-MIB", "hwPoePowerAbsent"),
        ("HUAWEI-POE-MIB", "hwPoePowerAbsentResume"),
        ("HUAWEI-POE-MIB", "hwPoeRpsPowerOutputAlarm"),
        ("HUAWEI-POE-MIB", "hwPoeRpsPowerOutputAlarmResume"))
)
if mibBuilder.loadTexts:
    hwPoeNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-POE-MIB",
    **{"hwPoeMIB": hwPoeMIB,
       "hwPoeGlobalObjects": hwPoeGlobalObjects,
       "hwPoePower": hwPoePower,
       "hwPoePowerRsvPercent": hwPoePowerRsvPercent,
       "hwPoePowerUtilizationThreshold": hwPoePowerUtilizationThreshold,
       "hwPoeSlotTable": hwPoeSlotTable,
       "hwPoeSlotEntry": hwPoeSlotEntry,
       "hwPoeSlotId": hwPoeSlotId,
       "hwPoeSlotMaximumPower": hwPoeSlotMaximumPower,
       "hwPoeSlotAvailablePower": hwPoeSlotAvailablePower,
       "hwPoeSlotReferencePower": hwPoeSlotReferencePower,
       "hwPoeSlotConsumingPower": hwPoeSlotConsumingPower,
       "hwPoeSlotPeakPower": hwPoeSlotPeakPower,
       "hwPoeSlotLegacyDetect": hwPoeSlotLegacyDetect,
       "hwPoeSlotPowerManagementManner": hwPoeSlotPowerManagementManner,
       "hwPoeSlotIsPoeDevice": hwPoeSlotIsPoeDevice,
       "hwPoeDimmId": hwPoeDimmId,
       "hwPoeSlotPowerRsvPercent": hwPoeSlotPowerRsvPercent,
       "hwPoeSlotPowerUtilizationThreshold": hwPoeSlotPowerUtilizationThreshold,
       "hwPoePortTable": hwPoePortTable,
       "hwPoePortEntry": hwPoePortEntry,
       "hwPoePortIfIndex": hwPoePortIfIndex,
       "hwPoePortName": hwPoePortName,
       "hwPoePortEnable": hwPoePortEnable,
       "hwPoePortPriority": hwPoePortPriority,
       "hwPoePortMaximumPower": hwPoePortMaximumPower,
       "hwPoePortPowerOnStatus": hwPoePortPowerOnStatus,
       "hwPoePortPowerStatus": hwPoePortPowerStatus,
       "hwPoePortPdClass": hwPoePortPdClass,
       "hwPoePortReferencePower": hwPoePortReferencePower,
       "hwPoePortConsumingPower": hwPoePortConsumingPower,
       "hwPoePortPeakPower": hwPoePortPeakPower,
       "hwPoePortAveragePower": hwPoePortAveragePower,
       "hwPoePortCurrent": hwPoePortCurrent,
       "hwPoePortVoltage": hwPoePortVoltage,
       "hwPoePortManualOperation": hwPoePortManualOperation,
       "hwPoeTrapObjects": hwPoeTrapObjects,
       "hwPoePdPriority": hwPoePdPriority,
       "hwPoeSlotNum": hwPoeSlotNum,
       "hwPoeCurConsumPower": hwPoeCurConsumPower,
       "hwPoeConsumPowerThreshold": hwPoeConsumPowerThreshold,
       "hwPoeDeviceID": hwPoeDeviceID,
       "hwFrameID": hwFrameID,
       "hwPoeNotification": hwPoeNotification,
       "hwPoeDimmError": hwPoeDimmError,
       "hwPoePowerOff": hwPoePowerOff,
       "hwPoePowerOn": hwPoePowerOn,
       "hwPoeSlotPowerOverload": hwPoeSlotPowerOverload,
       "hwPoeSlotPowerOverloadResume": hwPoeSlotPowerOverloadResume,
       "hwPoePdPowerOverload": hwPoePdPowerOverload,
       "hwPoePdPowerOverloadResume": hwPoePdPowerOverloadResume,
       "hwPoePdConnected": hwPoePdConnected,
       "hwPoePdDisconnected": hwPoePdDisconnected,
       "hwPoePdClassInvalid": hwPoePdClassInvalid,
       "hwPoePdClassOvercurrent": hwPoePdClassOvercurrent,
       "hwPoePdPowerOvercurrent": hwPoePdPowerOvercurrent,
       "hwPoePdPowerOvercurrentResume": hwPoePdPowerOvercurrentResume,
       "hwPoePowerOnFail": hwPoePowerOnFail,
       "hwPoePowerOffCurrentLimits": hwPoePowerOffCurrentLimits,
       "hwPoePdPriorityDifferent": hwPoePdPriorityDifferent,
       "hwPoePowerOverUtilizationThreshold": hwPoePowerOverUtilizationThreshold,
       "hwPoePowerOverUtilizationThresholdResume": hwPoePowerOverUtilizationThresholdResume,
       "hwPoeBoardInsertedWrongFrame": hwPoeBoardInsertedWrongFrame,
       "hwPoePowerAbsent": hwPoePowerAbsent,
       "hwPoePowerAbsentResume": hwPoePowerAbsentResume,
       "hwPoeRpsPowerOutputAlarm": hwPoeRpsPowerOutputAlarm,
       "hwPoeRpsPowerOutputAlarmResume": hwPoeRpsPowerOutputAlarmResume,
       "hwPoeConformance": hwPoeConformance,
       "hwPoeGroups": hwPoeGroups,
       "hwPoeSlotGroup": hwPoeSlotGroup,
       "hwPoePortGroup": hwPoePortGroup,
       "hwPoeGlobalGroup": hwPoeGlobalGroup,
       "hwPoeNotificationGroup": hwPoeNotificationGroup,
       "hwPoeTrapObjectsGroup": hwPoeTrapObjectsGroup}
)
