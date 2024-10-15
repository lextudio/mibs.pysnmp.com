# SNMP MIB module (AC-PM-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AC-PM-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:31 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

acPMAtm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AudioCodes_ObjectIdentity = ObjectIdentity
audioCodes = _AudioCodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003)
)
_AcRegistrations_ObjectIdentity = ObjectIdentity
acRegistrations = _AcRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 7)
)
_AcGeneric_ObjectIdentity = ObjectIdentity
acGeneric = _AcGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8)
)
_AcProducts_ObjectIdentity = ObjectIdentity
acProducts = _AcProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9)
)
_AcPerformance_ObjectIdentity = ObjectIdentity
acPerformance = _AcPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10)
)
_AcPMAtmConfiguration_ObjectIdentity = ObjectIdentity
acPMAtmConfiguration = _AcPMAtmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 1)
)


class _AcPMAtmConfigurationPeriodLength_Type(Integer32):
    """Custom type acPMAtmConfigurationPeriodLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 894780),
    )


_AcPMAtmConfigurationPeriodLength_Type.__name__ = "Integer32"
_AcPMAtmConfigurationPeriodLength_Object = MibScalar
acPMAtmConfigurationPeriodLength = _AcPMAtmConfigurationPeriodLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 1, 1),
    _AcPMAtmConfigurationPeriodLength_Type()
)
acPMAtmConfigurationPeriodLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMAtmConfigurationPeriodLength.setStatus("current")


class _AcPMAtmConfigurationResetTotalCounters_Type(Integer32):
    """Custom type acPMAtmConfigurationResetTotalCounters based on Integer32"""
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


_AcPMAtmConfigurationResetTotalCounters_Type.__name__ = "Integer32"
_AcPMAtmConfigurationResetTotalCounters_Object = MibScalar
acPMAtmConfigurationResetTotalCounters = _AcPMAtmConfigurationResetTotalCounters_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 1, 2),
    _AcPMAtmConfigurationResetTotalCounters_Type()
)
acPMAtmConfigurationResetTotalCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMAtmConfigurationResetTotalCounters.setStatus("current")
_AcPMAtmCellAttributes_ObjectIdentity = ObjectIdentity
acPMAtmCellAttributes = _AcPMAtmCellAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 1, 31)
)


class _AcPMAtmCellAttributesTxHighThreshold_Type(Integer32):
    """Custom type acPMAtmCellAttributesTxHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3000),
    )


_AcPMAtmCellAttributesTxHighThreshold_Type.__name__ = "Integer32"
_AcPMAtmCellAttributesTxHighThreshold_Object = MibScalar
acPMAtmCellAttributesTxHighThreshold = _AcPMAtmCellAttributesTxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 1, 31, 1),
    _AcPMAtmCellAttributesTxHighThreshold_Type()
)
acPMAtmCellAttributesTxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMAtmCellAttributesTxHighThreshold.setStatus("current")


class _AcPMAtmCellAttributesTxLowThreshold_Type(Integer32):
    """Custom type acPMAtmCellAttributesTxLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3000),
    )


_AcPMAtmCellAttributesTxLowThreshold_Type.__name__ = "Integer32"
_AcPMAtmCellAttributesTxLowThreshold_Object = MibScalar
acPMAtmCellAttributesTxLowThreshold = _AcPMAtmCellAttributesTxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 1, 31, 2),
    _AcPMAtmCellAttributesTxLowThreshold_Type()
)
acPMAtmCellAttributesTxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMAtmCellAttributesTxLowThreshold.setStatus("current")


class _AcPMAtmCellAttributesRxHighThreshold_Type(Integer32):
    """Custom type acPMAtmCellAttributesRxHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3000),
    )


_AcPMAtmCellAttributesRxHighThreshold_Type.__name__ = "Integer32"
_AcPMAtmCellAttributesRxHighThreshold_Object = MibScalar
acPMAtmCellAttributesRxHighThreshold = _AcPMAtmCellAttributesRxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 1, 31, 3),
    _AcPMAtmCellAttributesRxHighThreshold_Type()
)
acPMAtmCellAttributesRxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMAtmCellAttributesRxHighThreshold.setStatus("current")


class _AcPMAtmCellAttributesRxLowThreshold_Type(Integer32):
    """Custom type acPMAtmCellAttributesRxLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3000),
    )


_AcPMAtmCellAttributesRxLowThreshold_Type.__name__ = "Integer32"
_AcPMAtmCellAttributesRxLowThreshold_Object = MibScalar
acPMAtmCellAttributesRxLowThreshold = _AcPMAtmCellAttributesRxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 1, 31, 4),
    _AcPMAtmCellAttributesRxLowThreshold_Type()
)
acPMAtmCellAttributesRxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMAtmCellAttributesRxLowThreshold.setStatus("current")
_AcPMAtmData_ObjectIdentity = ObjectIdentity
acPMAtmData = _AcPMAtmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2)
)


class _AcPMAtmDataAcPMAtmTimeFromStartOfInterval_Type(Integer32):
    """Custom type acPMAtmDataAcPMAtmTimeFromStartOfInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMAtmDataAcPMAtmTimeFromStartOfInterval_Type.__name__ = "Integer32"
_AcPMAtmDataAcPMAtmTimeFromStartOfInterval_Object = MibScalar
acPMAtmDataAcPMAtmTimeFromStartOfInterval = _AcPMAtmDataAcPMAtmTimeFromStartOfInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 1),
    _AcPMAtmDataAcPMAtmTimeFromStartOfInterval_Type()
)
acPMAtmDataAcPMAtmTimeFromStartOfInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmDataAcPMAtmTimeFromStartOfInterval.setStatus("current")
_AcPMAtmCellTxTable_Object = MibTable
acPMAtmCellTxTable = _AcPMAtmCellTxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21)
)
if mibBuilder.loadTexts:
    acPMAtmCellTxTable.setStatus("current")
_AcPMAtmCellTxEntry_Object = MibTableRow
acPMAtmCellTxEntry = _AcPMAtmCellTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1)
)
acPMAtmCellTxEntry.setIndexNames(
    (0, "AC-PM-ATM-MIB", "acPMAtmCellTxInterface"),
    (0, "AC-PM-ATM-MIB", "acPMAtmCellTxInterval"),
)
if mibBuilder.loadTexts:
    acPMAtmCellTxEntry.setStatus("current")


class _AcPMAtmCellTxInterface_Type(Integer32):
    """Custom type acPMAtmCellTxInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMAtmCellTxInterface_Type.__name__ = "Integer32"
_AcPMAtmCellTxInterface_Object = MibTableColumn
acPMAtmCellTxInterface = _AcPMAtmCellTxInterface_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 1),
    _AcPMAtmCellTxInterface_Type()
)
acPMAtmCellTxInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMAtmCellTxInterface.setStatus("current")


class _AcPMAtmCellTxInterval_Type(Integer32):
    """Custom type acPMAtmCellTxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMAtmCellTxInterval_Type.__name__ = "Integer32"
_AcPMAtmCellTxInterval_Object = MibTableColumn
acPMAtmCellTxInterval = _AcPMAtmCellTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 2),
    _AcPMAtmCellTxInterval_Type()
)
acPMAtmCellTxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMAtmCellTxInterval.setStatus("current")


class _AcPMAtmCellTxAverage_Type(Integer32):
    """Custom type acPMAtmCellTxAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMAtmCellTxAverage_Type.__name__ = "Integer32"
_AcPMAtmCellTxAverage_Object = MibTableColumn
acPMAtmCellTxAverage = _AcPMAtmCellTxAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 3),
    _AcPMAtmCellTxAverage_Type()
)
acPMAtmCellTxAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmCellTxAverage.setStatus("current")


class _AcPMAtmCellTxMax_Type(Integer32):
    """Custom type acPMAtmCellTxMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMAtmCellTxMax_Type.__name__ = "Integer32"
_AcPMAtmCellTxMax_Object = MibTableColumn
acPMAtmCellTxMax = _AcPMAtmCellTxMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 4),
    _AcPMAtmCellTxMax_Type()
)
acPMAtmCellTxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmCellTxMax.setStatus("current")


class _AcPMAtmCellTxMin_Type(Integer32):
    """Custom type acPMAtmCellTxMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMAtmCellTxMin_Type.__name__ = "Integer32"
_AcPMAtmCellTxMin_Object = MibTableColumn
acPMAtmCellTxMin = _AcPMAtmCellTxMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 5),
    _AcPMAtmCellTxMin_Type()
)
acPMAtmCellTxMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmCellTxMin.setStatus("current")
_AcPMAtmCellTxVolume_Type = Counter32
_AcPMAtmCellTxVolume_Object = MibTableColumn
acPMAtmCellTxVolume = _AcPMAtmCellTxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 6),
    _AcPMAtmCellTxVolume_Type()
)
acPMAtmCellTxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmCellTxVolume.setStatus("current")


class _AcPMAtmCellTxTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMAtmCellTxTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMAtmCellTxTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMAtmCellTxTimeBelowLowThreshold_Object = MibTableColumn
acPMAtmCellTxTimeBelowLowThreshold = _AcPMAtmCellTxTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 7),
    _AcPMAtmCellTxTimeBelowLowThreshold_Type()
)
acPMAtmCellTxTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmCellTxTimeBelowLowThreshold.setStatus("current")


class _AcPMAtmCellTxTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMAtmCellTxTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMAtmCellTxTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMAtmCellTxTimeBetweenThresholds_Object = MibTableColumn
acPMAtmCellTxTimeBetweenThresholds = _AcPMAtmCellTxTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 8),
    _AcPMAtmCellTxTimeBetweenThresholds_Type()
)
acPMAtmCellTxTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmCellTxTimeBetweenThresholds.setStatus("current")


class _AcPMAtmCellTxTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMAtmCellTxTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMAtmCellTxTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMAtmCellTxTimeAboveHighThreshold_Object = MibTableColumn
acPMAtmCellTxTimeAboveHighThreshold = _AcPMAtmCellTxTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 9),
    _AcPMAtmCellTxTimeAboveHighThreshold_Type()
)
acPMAtmCellTxTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmCellTxTimeAboveHighThreshold.setStatus("current")


class _AcPMAtmCellTxFullDayAverage_Type(Integer32):
    """Custom type acPMAtmCellTxFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMAtmCellTxFullDayAverage_Type.__name__ = "Integer32"
_AcPMAtmCellTxFullDayAverage_Object = MibTableColumn
acPMAtmCellTxFullDayAverage = _AcPMAtmCellTxFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 10),
    _AcPMAtmCellTxFullDayAverage_Type()
)
acPMAtmCellTxFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmCellTxFullDayAverage.setStatus("current")
_AcPMAtmCellRxTable_Object = MibTable
acPMAtmCellRxTable = _AcPMAtmCellRxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22)
)
if mibBuilder.loadTexts:
    acPMAtmCellRxTable.setStatus("current")
_AcPMAtmCellRxEntry_Object = MibTableRow
acPMAtmCellRxEntry = _AcPMAtmCellRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1)
)
acPMAtmCellRxEntry.setIndexNames(
    (0, "AC-PM-ATM-MIB", "acPMAtmCellRxInterface"),
    (0, "AC-PM-ATM-MIB", "acPMAtmCellRxInterval"),
)
if mibBuilder.loadTexts:
    acPMAtmCellRxEntry.setStatus("current")


class _AcPMAtmCellRxInterface_Type(Integer32):
    """Custom type acPMAtmCellRxInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMAtmCellRxInterface_Type.__name__ = "Integer32"
_AcPMAtmCellRxInterface_Object = MibTableColumn
acPMAtmCellRxInterface = _AcPMAtmCellRxInterface_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 1),
    _AcPMAtmCellRxInterface_Type()
)
acPMAtmCellRxInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMAtmCellRxInterface.setStatus("current")


class _AcPMAtmCellRxInterval_Type(Integer32):
    """Custom type acPMAtmCellRxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMAtmCellRxInterval_Type.__name__ = "Integer32"
_AcPMAtmCellRxInterval_Object = MibTableColumn
acPMAtmCellRxInterval = _AcPMAtmCellRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 2),
    _AcPMAtmCellRxInterval_Type()
)
acPMAtmCellRxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMAtmCellRxInterval.setStatus("current")


class _AcPMAtmCellRxAverage_Type(Integer32):
    """Custom type acPMAtmCellRxAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMAtmCellRxAverage_Type.__name__ = "Integer32"
_AcPMAtmCellRxAverage_Object = MibTableColumn
acPMAtmCellRxAverage = _AcPMAtmCellRxAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 3),
    _AcPMAtmCellRxAverage_Type()
)
acPMAtmCellRxAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmCellRxAverage.setStatus("current")


class _AcPMAtmCellRxMax_Type(Integer32):
    """Custom type acPMAtmCellRxMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMAtmCellRxMax_Type.__name__ = "Integer32"
_AcPMAtmCellRxMax_Object = MibTableColumn
acPMAtmCellRxMax = _AcPMAtmCellRxMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 4),
    _AcPMAtmCellRxMax_Type()
)
acPMAtmCellRxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmCellRxMax.setStatus("current")


class _AcPMAtmCellRxMin_Type(Integer32):
    """Custom type acPMAtmCellRxMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMAtmCellRxMin_Type.__name__ = "Integer32"
_AcPMAtmCellRxMin_Object = MibTableColumn
acPMAtmCellRxMin = _AcPMAtmCellRxMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 5),
    _AcPMAtmCellRxMin_Type()
)
acPMAtmCellRxMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmCellRxMin.setStatus("current")
_AcPMAtmCellRxVolume_Type = Counter32
_AcPMAtmCellRxVolume_Object = MibTableColumn
acPMAtmCellRxVolume = _AcPMAtmCellRxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 6),
    _AcPMAtmCellRxVolume_Type()
)
acPMAtmCellRxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmCellRxVolume.setStatus("current")


class _AcPMAtmCellRxTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMAtmCellRxTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMAtmCellRxTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMAtmCellRxTimeBelowLowThreshold_Object = MibTableColumn
acPMAtmCellRxTimeBelowLowThreshold = _AcPMAtmCellRxTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 7),
    _AcPMAtmCellRxTimeBelowLowThreshold_Type()
)
acPMAtmCellRxTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmCellRxTimeBelowLowThreshold.setStatus("current")


class _AcPMAtmCellRxTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMAtmCellRxTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMAtmCellRxTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMAtmCellRxTimeBetweenThresholds_Object = MibTableColumn
acPMAtmCellRxTimeBetweenThresholds = _AcPMAtmCellRxTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 8),
    _AcPMAtmCellRxTimeBetweenThresholds_Type()
)
acPMAtmCellRxTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmCellRxTimeBetweenThresholds.setStatus("current")


class _AcPMAtmCellRxTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMAtmCellRxTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMAtmCellRxTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMAtmCellRxTimeAboveHighThreshold_Object = MibTableColumn
acPMAtmCellRxTimeAboveHighThreshold = _AcPMAtmCellRxTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 9),
    _AcPMAtmCellRxTimeAboveHighThreshold_Type()
)
acPMAtmCellRxTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmCellRxTimeAboveHighThreshold.setStatus("current")


class _AcPMAtmCellRxFullDayAverage_Type(Integer32):
    """Custom type acPMAtmCellRxFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMAtmCellRxFullDayAverage_Type.__name__ = "Integer32"
_AcPMAtmCellRxFullDayAverage_Object = MibTableColumn
acPMAtmCellRxFullDayAverage = _AcPMAtmCellRxFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 10),
    _AcPMAtmCellRxFullDayAverage_Type()
)
acPMAtmCellRxFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmCellRxFullDayAverage.setStatus("current")
_AcPMAtmCellDiscardedTable_Object = MibTable
acPMAtmCellDiscardedTable = _AcPMAtmCellDiscardedTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 23)
)
if mibBuilder.loadTexts:
    acPMAtmCellDiscardedTable.setStatus("current")
_AcPMAtmCellDiscardedEntry_Object = MibTableRow
acPMAtmCellDiscardedEntry = _AcPMAtmCellDiscardedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 23, 1)
)
acPMAtmCellDiscardedEntry.setIndexNames(
    (0, "AC-PM-ATM-MIB", "acPMAtmCellDiscardedInterface"),
    (0, "AC-PM-ATM-MIB", "acPMAtmCellDiscardedInterval"),
)
if mibBuilder.loadTexts:
    acPMAtmCellDiscardedEntry.setStatus("current")


class _AcPMAtmCellDiscardedInterface_Type(Integer32):
    """Custom type acPMAtmCellDiscardedInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMAtmCellDiscardedInterface_Type.__name__ = "Integer32"
_AcPMAtmCellDiscardedInterface_Object = MibTableColumn
acPMAtmCellDiscardedInterface = _AcPMAtmCellDiscardedInterface_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 23, 1, 1),
    _AcPMAtmCellDiscardedInterface_Type()
)
acPMAtmCellDiscardedInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMAtmCellDiscardedInterface.setStatus("current")


class _AcPMAtmCellDiscardedInterval_Type(Integer32):
    """Custom type acPMAtmCellDiscardedInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMAtmCellDiscardedInterval_Type.__name__ = "Integer32"
_AcPMAtmCellDiscardedInterval_Object = MibTableColumn
acPMAtmCellDiscardedInterval = _AcPMAtmCellDiscardedInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 23, 1, 2),
    _AcPMAtmCellDiscardedInterval_Type()
)
acPMAtmCellDiscardedInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMAtmCellDiscardedInterval.setStatus("current")
_AcPMAtmCellDiscardedVal_Type = Gauge32
_AcPMAtmCellDiscardedVal_Object = MibTableColumn
acPMAtmCellDiscardedVal = _AcPMAtmCellDiscardedVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 23, 1, 3),
    _AcPMAtmCellDiscardedVal_Type()
)
acPMAtmCellDiscardedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMAtmCellDiscardedVal.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AC-PM-ATM-MIB",
    **{"audioCodes": audioCodes,
       "acRegistrations": acRegistrations,
       "acGeneric": acGeneric,
       "acProducts": acProducts,
       "acPerformance": acPerformance,
       "acPMAtm": acPMAtm,
       "acPMAtmConfiguration": acPMAtmConfiguration,
       "acPMAtmConfigurationPeriodLength": acPMAtmConfigurationPeriodLength,
       "acPMAtmConfigurationResetTotalCounters": acPMAtmConfigurationResetTotalCounters,
       "acPMAtmCellAttributes": acPMAtmCellAttributes,
       "acPMAtmCellAttributesTxHighThreshold": acPMAtmCellAttributesTxHighThreshold,
       "acPMAtmCellAttributesTxLowThreshold": acPMAtmCellAttributesTxLowThreshold,
       "acPMAtmCellAttributesRxHighThreshold": acPMAtmCellAttributesRxHighThreshold,
       "acPMAtmCellAttributesRxLowThreshold": acPMAtmCellAttributesRxLowThreshold,
       "acPMAtmData": acPMAtmData,
       "acPMAtmDataAcPMAtmTimeFromStartOfInterval": acPMAtmDataAcPMAtmTimeFromStartOfInterval,
       "acPMAtmCellTxTable": acPMAtmCellTxTable,
       "acPMAtmCellTxEntry": acPMAtmCellTxEntry,
       "acPMAtmCellTxInterface": acPMAtmCellTxInterface,
       "acPMAtmCellTxInterval": acPMAtmCellTxInterval,
       "acPMAtmCellTxAverage": acPMAtmCellTxAverage,
       "acPMAtmCellTxMax": acPMAtmCellTxMax,
       "acPMAtmCellTxMin": acPMAtmCellTxMin,
       "acPMAtmCellTxVolume": acPMAtmCellTxVolume,
       "acPMAtmCellTxTimeBelowLowThreshold": acPMAtmCellTxTimeBelowLowThreshold,
       "acPMAtmCellTxTimeBetweenThresholds": acPMAtmCellTxTimeBetweenThresholds,
       "acPMAtmCellTxTimeAboveHighThreshold": acPMAtmCellTxTimeAboveHighThreshold,
       "acPMAtmCellTxFullDayAverage": acPMAtmCellTxFullDayAverage,
       "acPMAtmCellRxTable": acPMAtmCellRxTable,
       "acPMAtmCellRxEntry": acPMAtmCellRxEntry,
       "acPMAtmCellRxInterface": acPMAtmCellRxInterface,
       "acPMAtmCellRxInterval": acPMAtmCellRxInterval,
       "acPMAtmCellRxAverage": acPMAtmCellRxAverage,
       "acPMAtmCellRxMax": acPMAtmCellRxMax,
       "acPMAtmCellRxMin": acPMAtmCellRxMin,
       "acPMAtmCellRxVolume": acPMAtmCellRxVolume,
       "acPMAtmCellRxTimeBelowLowThreshold": acPMAtmCellRxTimeBelowLowThreshold,
       "acPMAtmCellRxTimeBetweenThresholds": acPMAtmCellRxTimeBetweenThresholds,
       "acPMAtmCellRxTimeAboveHighThreshold": acPMAtmCellRxTimeAboveHighThreshold,
       "acPMAtmCellRxFullDayAverage": acPMAtmCellRxFullDayAverage,
       "acPMAtmCellDiscardedTable": acPMAtmCellDiscardedTable,
       "acPMAtmCellDiscardedEntry": acPMAtmCellDiscardedEntry,
       "acPMAtmCellDiscardedInterface": acPMAtmCellDiscardedInterface,
       "acPMAtmCellDiscardedInterval": acPMAtmCellDiscardedInterval,
       "acPMAtmCellDiscardedVal": acPMAtmCellDiscardedVal}
)
