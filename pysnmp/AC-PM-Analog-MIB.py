# SNMP MIB module (AC-PM-Analog-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AC-PM-Analog-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:32 2024
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

(acBoardMibs,
 acGeneric,
 acPerformance,
 acProducts,
 acRegistrations,
 audioCodes) = mibBuilder.importSymbols(
    "AUDIOCODES-TYPES-MIB",
    "acBoardMibs",
    "acGeneric",
    "acPerformance",
    "acProducts",
    "acRegistrations",
    "audioCodes")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

acPMAnalog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcPMAnalogConfiguration_ObjectIdentity = ObjectIdentity
acPMAnalogConfiguration = _AcPMAnalogConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 1)
)


class _AcPMAnalogConfigurationPeriodLength_Type(Unsigned32):
    """Custom type acPMAnalogConfigurationPeriodLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 894780),
    )


_AcPMAnalogConfigurationPeriodLength_Type.__name__ = "Unsigned32"
_AcPMAnalogConfigurationPeriodLength_Object = MibScalar
acPMAnalogConfigurationPeriodLength = _AcPMAnalogConfigurationPeriodLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 1, 1),
    _AcPMAnalogConfigurationPeriodLength_Type()
)
acPMAnalogConfigurationPeriodLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMAnalogConfigurationPeriodLength.setStatus("current")


class _AcPMAnalogConfigurationResetTotalCounters_Type(Integer32):
    """Custom type acPMAnalogConfigurationResetTotalCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resetCountersDone", 1),
          ("resetTotalCounters", 2))
    )


_AcPMAnalogConfigurationResetTotalCounters_Type.__name__ = "Integer32"
_AcPMAnalogConfigurationResetTotalCounters_Object = MibScalar
acPMAnalogConfigurationResetTotalCounters = _AcPMAnalogConfigurationResetTotalCounters_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 1, 2),
    _AcPMAnalogConfigurationResetTotalCounters_Type()
)
acPMAnalogConfigurationResetTotalCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMAnalogConfigurationResetTotalCounters.setStatus("current")
_AcPMAnalogUtilsAttributes_ObjectIdentity = ObjectIdentity
acPMAnalogUtilsAttributes = _AcPMAnalogUtilsAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 1, 31)
)


class _AcPMAnalogUtilsAttributesOffHookChannelsHighThreshold_Type(Unsigned32):
    """Custom type acPMAnalogUtilsAttributesOffHookChannelsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMAnalogUtilsAttributesOffHookChannelsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMAnalogUtilsAttributesOffHookChannelsHighThreshold_Object = MibScalar
acPMAnalogUtilsAttributesOffHookChannelsHighThreshold = _AcPMAnalogUtilsAttributesOffHookChannelsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 1, 31, 1),
    _AcPMAnalogUtilsAttributesOffHookChannelsHighThreshold_Type()
)
acPMAnalogUtilsAttributesOffHookChannelsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMAnalogUtilsAttributesOffHookChannelsHighThreshold.setStatus("current")


class _AcPMAnalogUtilsAttributesOffHookChannelsLowThreshold_Type(Unsigned32):
    """Custom type acPMAnalogUtilsAttributesOffHookChannelsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMAnalogUtilsAttributesOffHookChannelsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMAnalogUtilsAttributesOffHookChannelsLowThreshold_Object = MibScalar
acPMAnalogUtilsAttributesOffHookChannelsLowThreshold = _AcPMAnalogUtilsAttributesOffHookChannelsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 1, 31, 2),
    _AcPMAnalogUtilsAttributesOffHookChannelsLowThreshold_Type()
)
acPMAnalogUtilsAttributesOffHookChannelsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMAnalogUtilsAttributesOffHookChannelsLowThreshold.setStatus("current")
_AcPMAnalogData_ObjectIdentity = ObjectIdentity
acPMAnalogData = _AcPMAnalogData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 2)
)


class _AcPMAnalogDataAcPMAnalogTimeFromStartOfInterval_Type(Unsigned32):
    """Custom type acPMAnalogDataAcPMAnalogTimeFromStartOfInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMAnalogDataAcPMAnalogTimeFromStartOfInterval_Type.__name__ = "Unsigned32"
_AcPMAnalogDataAcPMAnalogTimeFromStartOfInterval_Object = MibScalar
acPMAnalogDataAcPMAnalogTimeFromStartOfInterval = _AcPMAnalogDataAcPMAnalogTimeFromStartOfInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 1),
    _AcPMAnalogDataAcPMAnalogTimeFromStartOfInterval_Type()
)
acPMAnalogDataAcPMAnalogTimeFromStartOfInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAnalogDataAcPMAnalogTimeFromStartOfInterval.setStatus("current")
_AcPMAnalogUtils_ObjectIdentity = ObjectIdentity
acPMAnalogUtils = _AcPMAnalogUtils_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31)
)
_AcPMOffHookChannelsTable_Object = MibTable
acPMOffHookChannelsTable = _AcPMOffHookChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21)
)
if mibBuilder.loadTexts:
    acPMOffHookChannelsTable.setStatus("current")
_AcPMOffHookChannelsEntry_Object = MibTableRow
acPMOffHookChannelsEntry = _AcPMOffHookChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1)
)
acPMOffHookChannelsEntry.setIndexNames(
    (0, "AC-PM-Analog-MIB", "acPMOffHookChannelsInterval"),
)
if mibBuilder.loadTexts:
    acPMOffHookChannelsEntry.setStatus("current")


class _AcPMOffHookChannelsInterval_Type(Unsigned32):
    """Custom type acPMOffHookChannelsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMOffHookChannelsInterval_Type.__name__ = "Unsigned32"
_AcPMOffHookChannelsInterval_Object = MibTableColumn
acPMOffHookChannelsInterval = _AcPMOffHookChannelsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 1),
    _AcPMOffHookChannelsInterval_Type()
)
acPMOffHookChannelsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMOffHookChannelsInterval.setStatus("current")
_AcPMOffHookChannelsVal_Type = Gauge32
_AcPMOffHookChannelsVal_Object = MibTableColumn
acPMOffHookChannelsVal = _AcPMOffHookChannelsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 2),
    _AcPMOffHookChannelsVal_Type()
)
acPMOffHookChannelsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMOffHookChannelsVal.setStatus("current")


class _AcPMOffHookChannelsAverage_Type(Integer32):
    """Custom type acPMOffHookChannelsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMOffHookChannelsAverage_Type.__name__ = "Integer32"
_AcPMOffHookChannelsAverage_Object = MibTableColumn
acPMOffHookChannelsAverage = _AcPMOffHookChannelsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 3),
    _AcPMOffHookChannelsAverage_Type()
)
acPMOffHookChannelsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMOffHookChannelsAverage.setStatus("current")


class _AcPMOffHookChannelsMax_Type(Integer32):
    """Custom type acPMOffHookChannelsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMOffHookChannelsMax_Type.__name__ = "Integer32"
_AcPMOffHookChannelsMax_Object = MibTableColumn
acPMOffHookChannelsMax = _AcPMOffHookChannelsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 4),
    _AcPMOffHookChannelsMax_Type()
)
acPMOffHookChannelsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMOffHookChannelsMax.setStatus("current")


class _AcPMOffHookChannelsMin_Type(Integer32):
    """Custom type acPMOffHookChannelsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMOffHookChannelsMin_Type.__name__ = "Integer32"
_AcPMOffHookChannelsMin_Object = MibTableColumn
acPMOffHookChannelsMin = _AcPMOffHookChannelsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 5),
    _AcPMOffHookChannelsMin_Type()
)
acPMOffHookChannelsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMOffHookChannelsMin.setStatus("current")


class _AcPMOffHookChannelsVolume_Type(Integer32):
    """Custom type acPMOffHookChannelsVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMOffHookChannelsVolume_Type.__name__ = "Integer32"
_AcPMOffHookChannelsVolume_Object = MibTableColumn
acPMOffHookChannelsVolume = _AcPMOffHookChannelsVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 6),
    _AcPMOffHookChannelsVolume_Type()
)
acPMOffHookChannelsVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMOffHookChannelsVolume.setStatus("current")


class _AcPMOffHookChannelsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMOffHookChannelsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMOffHookChannelsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMOffHookChannelsTimeBelowLowThreshold_Object = MibTableColumn
acPMOffHookChannelsTimeBelowLowThreshold = _AcPMOffHookChannelsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 7),
    _AcPMOffHookChannelsTimeBelowLowThreshold_Type()
)
acPMOffHookChannelsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMOffHookChannelsTimeBelowLowThreshold.setStatus("current")


class _AcPMOffHookChannelsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMOffHookChannelsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMOffHookChannelsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMOffHookChannelsTimeBetweenThresholds_Object = MibTableColumn
acPMOffHookChannelsTimeBetweenThresholds = _AcPMOffHookChannelsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 8),
    _AcPMOffHookChannelsTimeBetweenThresholds_Type()
)
acPMOffHookChannelsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMOffHookChannelsTimeBetweenThresholds.setStatus("current")


class _AcPMOffHookChannelsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMOffHookChannelsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMOffHookChannelsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMOffHookChannelsTimeAboveHighThreshold_Object = MibTableColumn
acPMOffHookChannelsTimeAboveHighThreshold = _AcPMOffHookChannelsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 9),
    _AcPMOffHookChannelsTimeAboveHighThreshold_Type()
)
acPMOffHookChannelsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMOffHookChannelsTimeAboveHighThreshold.setStatus("current")


class _AcPMOffHookChannelsFullDayAverage_Type(Integer32):
    """Custom type acPMOffHookChannelsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMOffHookChannelsFullDayAverage_Type.__name__ = "Integer32"
_AcPMOffHookChannelsFullDayAverage_Object = MibTableColumn
acPMOffHookChannelsFullDayAverage = _AcPMOffHookChannelsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 10),
    _AcPMOffHookChannelsFullDayAverage_Type()
)
acPMOffHookChannelsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMOffHookChannelsFullDayAverage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AC-PM-Analog-MIB",
    **{"acPMAnalog": acPMAnalog,
       "acPMAnalogConfiguration": acPMAnalogConfiguration,
       "acPMAnalogConfigurationPeriodLength": acPMAnalogConfigurationPeriodLength,
       "acPMAnalogConfigurationResetTotalCounters": acPMAnalogConfigurationResetTotalCounters,
       "acPMAnalogUtilsAttributes": acPMAnalogUtilsAttributes,
       "acPMAnalogUtilsAttributesOffHookChannelsHighThreshold": acPMAnalogUtilsAttributesOffHookChannelsHighThreshold,
       "acPMAnalogUtilsAttributesOffHookChannelsLowThreshold": acPMAnalogUtilsAttributesOffHookChannelsLowThreshold,
       "acPMAnalogData": acPMAnalogData,
       "acPMAnalogDataAcPMAnalogTimeFromStartOfInterval": acPMAnalogDataAcPMAnalogTimeFromStartOfInterval,
       "acPMAnalogUtils": acPMAnalogUtils,
       "acPMOffHookChannelsTable": acPMOffHookChannelsTable,
       "acPMOffHookChannelsEntry": acPMOffHookChannelsEntry,
       "acPMOffHookChannelsInterval": acPMOffHookChannelsInterval,
       "acPMOffHookChannelsVal": acPMOffHookChannelsVal,
       "acPMOffHookChannelsAverage": acPMOffHookChannelsAverage,
       "acPMOffHookChannelsMax": acPMOffHookChannelsMax,
       "acPMOffHookChannelsMin": acPMOffHookChannelsMin,
       "acPMOffHookChannelsVolume": acPMOffHookChannelsVolume,
       "acPMOffHookChannelsTimeBelowLowThreshold": acPMOffHookChannelsTimeBelowLowThreshold,
       "acPMOffHookChannelsTimeBetweenThresholds": acPMOffHookChannelsTimeBetweenThresholds,
       "acPMOffHookChannelsTimeAboveHighThreshold": acPMOffHookChannelsTimeAboveHighThreshold,
       "acPMOffHookChannelsFullDayAverage": acPMOffHookChannelsFullDayAverage}
)
