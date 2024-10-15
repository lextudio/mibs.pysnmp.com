# SNMP MIB module (AC-PM-PSTN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AC-PM-PSTN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:35 2024
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

acPMPSTN = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcPMPSTNConfiguration_ObjectIdentity = ObjectIdentity
acPMPSTNConfiguration = _AcPMPSTNConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 1)
)


class _AcPMPSTNConfigurationPeriodLength_Type(Unsigned32):
    """Custom type acPMPSTNConfigurationPeriodLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 894780),
    )


_AcPMPSTNConfigurationPeriodLength_Type.__name__ = "Unsigned32"
_AcPMPSTNConfigurationPeriodLength_Object = MibScalar
acPMPSTNConfigurationPeriodLength = _AcPMPSTNConfigurationPeriodLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 1, 1),
    _AcPMPSTNConfigurationPeriodLength_Type()
)
acPMPSTNConfigurationPeriodLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMPSTNConfigurationPeriodLength.setStatus("current")


class _AcPMPSTNConfigurationResetTotalCounters_Type(Integer32):
    """Custom type acPMPSTNConfigurationResetTotalCounters based on Integer32"""
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


_AcPMPSTNConfigurationResetTotalCounters_Type.__name__ = "Integer32"
_AcPMPSTNConfigurationResetTotalCounters_Object = MibScalar
acPMPSTNConfigurationResetTotalCounters = _AcPMPSTNConfigurationResetTotalCounters_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 1, 2),
    _AcPMPSTNConfigurationResetTotalCounters_Type()
)
acPMPSTNConfigurationResetTotalCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMPSTNConfigurationResetTotalCounters.setStatus("current")
_AcPMTrunkUtilizationAttributes_ObjectIdentity = ObjectIdentity
acPMTrunkUtilizationAttributes = _AcPMTrunkUtilizationAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 1, 31)
)


class _AcPMTrunkUtilizationAttributesHighThreshold_Type(Unsigned32):
    """Custom type acPMTrunkUtilizationAttributesHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AcPMTrunkUtilizationAttributesHighThreshold_Type.__name__ = "Unsigned32"
_AcPMTrunkUtilizationAttributesHighThreshold_Object = MibScalar
acPMTrunkUtilizationAttributesHighThreshold = _AcPMTrunkUtilizationAttributesHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 1, 31, 1),
    _AcPMTrunkUtilizationAttributesHighThreshold_Type()
)
acPMTrunkUtilizationAttributesHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMTrunkUtilizationAttributesHighThreshold.setStatus("current")


class _AcPMTrunkUtilizationAttributesLowThreshold_Type(Unsigned32):
    """Custom type acPMTrunkUtilizationAttributesLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AcPMTrunkUtilizationAttributesLowThreshold_Type.__name__ = "Unsigned32"
_AcPMTrunkUtilizationAttributesLowThreshold_Object = MibScalar
acPMTrunkUtilizationAttributesLowThreshold = _AcPMTrunkUtilizationAttributesLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 1, 31, 2),
    _AcPMTrunkUtilizationAttributesLowThreshold_Type()
)
acPMTrunkUtilizationAttributesLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMTrunkUtilizationAttributesLowThreshold.setStatus("current")
_AcPMPSTNChannelsAttributes_ObjectIdentity = ObjectIdentity
acPMPSTNChannelsAttributes = _AcPMPSTNChannelsAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 1, 32)
)


class _AcPMPSTNChannelsAttributesInServiceHighThreshold_Type(Unsigned32):
    """Custom type acPMPSTNChannelsAttributesInServiceHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AcPMPSTNChannelsAttributesInServiceHighThreshold_Type.__name__ = "Unsigned32"
_AcPMPSTNChannelsAttributesInServiceHighThreshold_Object = MibScalar
acPMPSTNChannelsAttributesInServiceHighThreshold = _AcPMPSTNChannelsAttributesInServiceHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 1, 32, 1),
    _AcPMPSTNChannelsAttributesInServiceHighThreshold_Type()
)
acPMPSTNChannelsAttributesInServiceHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMPSTNChannelsAttributesInServiceHighThreshold.setStatus("current")


class _AcPMPSTNChannelsAttributesInServiceLowThreshold_Type(Unsigned32):
    """Custom type acPMPSTNChannelsAttributesInServiceLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AcPMPSTNChannelsAttributesInServiceLowThreshold_Type.__name__ = "Unsigned32"
_AcPMPSTNChannelsAttributesInServiceLowThreshold_Object = MibScalar
acPMPSTNChannelsAttributesInServiceLowThreshold = _AcPMPSTNChannelsAttributesInServiceLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 1, 32, 2),
    _AcPMPSTNChannelsAttributesInServiceLowThreshold_Type()
)
acPMPSTNChannelsAttributesInServiceLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMPSTNChannelsAttributesInServiceLowThreshold.setStatus("current")


class _AcPMPSTNChannelsAttributesOutOfServiceHighThreshold_Type(Unsigned32):
    """Custom type acPMPSTNChannelsAttributesOutOfServiceHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AcPMPSTNChannelsAttributesOutOfServiceHighThreshold_Type.__name__ = "Unsigned32"
_AcPMPSTNChannelsAttributesOutOfServiceHighThreshold_Object = MibScalar
acPMPSTNChannelsAttributesOutOfServiceHighThreshold = _AcPMPSTNChannelsAttributesOutOfServiceHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 1, 32, 3),
    _AcPMPSTNChannelsAttributesOutOfServiceHighThreshold_Type()
)
acPMPSTNChannelsAttributesOutOfServiceHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMPSTNChannelsAttributesOutOfServiceHighThreshold.setStatus("current")


class _AcPMPSTNChannelsAttributesOutOfServiceLowThreshold_Type(Unsigned32):
    """Custom type acPMPSTNChannelsAttributesOutOfServiceLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AcPMPSTNChannelsAttributesOutOfServiceLowThreshold_Type.__name__ = "Unsigned32"
_AcPMPSTNChannelsAttributesOutOfServiceLowThreshold_Object = MibScalar
acPMPSTNChannelsAttributesOutOfServiceLowThreshold = _AcPMPSTNChannelsAttributesOutOfServiceLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 1, 32, 4),
    _AcPMPSTNChannelsAttributesOutOfServiceLowThreshold_Type()
)
acPMPSTNChannelsAttributesOutOfServiceLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMPSTNChannelsAttributesOutOfServiceLowThreshold.setStatus("current")


class _AcPMPSTNChannelsAttributesInMaintenanceHighThreshold_Type(Unsigned32):
    """Custom type acPMPSTNChannelsAttributesInMaintenanceHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AcPMPSTNChannelsAttributesInMaintenanceHighThreshold_Type.__name__ = "Unsigned32"
_AcPMPSTNChannelsAttributesInMaintenanceHighThreshold_Object = MibScalar
acPMPSTNChannelsAttributesInMaintenanceHighThreshold = _AcPMPSTNChannelsAttributesInMaintenanceHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 1, 32, 5),
    _AcPMPSTNChannelsAttributesInMaintenanceHighThreshold_Type()
)
acPMPSTNChannelsAttributesInMaintenanceHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMPSTNChannelsAttributesInMaintenanceHighThreshold.setStatus("current")


class _AcPMPSTNChannelsAttributesInMaintenanceLowThreshold_Type(Unsigned32):
    """Custom type acPMPSTNChannelsAttributesInMaintenanceLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AcPMPSTNChannelsAttributesInMaintenanceLowThreshold_Type.__name__ = "Unsigned32"
_AcPMPSTNChannelsAttributesInMaintenanceLowThreshold_Object = MibScalar
acPMPSTNChannelsAttributesInMaintenanceLowThreshold = _AcPMPSTNChannelsAttributesInMaintenanceLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 1, 32, 6),
    _AcPMPSTNChannelsAttributesInMaintenanceLowThreshold_Type()
)
acPMPSTNChannelsAttributesInMaintenanceLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMPSTNChannelsAttributesInMaintenanceLowThreshold.setStatus("current")
_AcPMPSTNData_ObjectIdentity = ObjectIdentity
acPMPSTNData = _AcPMPSTNData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2)
)


class _AcPMPSTNDataAcPMPSTNTimeFromStartOfInterval_Type(Unsigned32):
    """Custom type acPMPSTNDataAcPMPSTNTimeFromStartOfInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMPSTNDataAcPMPSTNTimeFromStartOfInterval_Type.__name__ = "Unsigned32"
_AcPMPSTNDataAcPMPSTNTimeFromStartOfInterval_Object = MibScalar
acPMPSTNDataAcPMPSTNTimeFromStartOfInterval = _AcPMPSTNDataAcPMPSTNTimeFromStartOfInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 1),
    _AcPMPSTNDataAcPMPSTNTimeFromStartOfInterval_Type()
)
acPMPSTNDataAcPMPSTNTimeFromStartOfInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNDataAcPMPSTNTimeFromStartOfInterval.setStatus("current")
_AcPMTrunkUtilizationTable_Object = MibTable
acPMTrunkUtilizationTable = _AcPMTrunkUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 21)
)
if mibBuilder.loadTexts:
    acPMTrunkUtilizationTable.setStatus("current")
_AcPMTrunkUtilizationEntry_Object = MibTableRow
acPMTrunkUtilizationEntry = _AcPMTrunkUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 21, 1)
)
acPMTrunkUtilizationEntry.setIndexNames(
    (0, "AC-PM-PSTN-MIB", "acPMTrunkUtilizationTrunkNum"),
    (0, "AC-PM-PSTN-MIB", "acPMTrunkUtilizationInterval"),
)
if mibBuilder.loadTexts:
    acPMTrunkUtilizationEntry.setStatus("current")


class _AcPMTrunkUtilizationTrunkNum_Type(Unsigned32):
    """Custom type acPMTrunkUtilizationTrunkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMTrunkUtilizationTrunkNum_Type.__name__ = "Unsigned32"
_AcPMTrunkUtilizationTrunkNum_Object = MibTableColumn
acPMTrunkUtilizationTrunkNum = _AcPMTrunkUtilizationTrunkNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 21, 1, 1),
    _AcPMTrunkUtilizationTrunkNum_Type()
)
acPMTrunkUtilizationTrunkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMTrunkUtilizationTrunkNum.setStatus("current")


class _AcPMTrunkUtilizationInterval_Type(Unsigned32):
    """Custom type acPMTrunkUtilizationInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMTrunkUtilizationInterval_Type.__name__ = "Unsigned32"
_AcPMTrunkUtilizationInterval_Object = MibTableColumn
acPMTrunkUtilizationInterval = _AcPMTrunkUtilizationInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 21, 1, 2),
    _AcPMTrunkUtilizationInterval_Type()
)
acPMTrunkUtilizationInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMTrunkUtilizationInterval.setStatus("current")
_AcPMTrunkUtilizationVal_Type = Gauge32
_AcPMTrunkUtilizationVal_Object = MibTableColumn
acPMTrunkUtilizationVal = _AcPMTrunkUtilizationVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 21, 1, 3),
    _AcPMTrunkUtilizationVal_Type()
)
acPMTrunkUtilizationVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTrunkUtilizationVal.setStatus("current")


class _AcPMTrunkUtilizationAverage_Type(Integer32):
    """Custom type acPMTrunkUtilizationAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTrunkUtilizationAverage_Type.__name__ = "Integer32"
_AcPMTrunkUtilizationAverage_Object = MibTableColumn
acPMTrunkUtilizationAverage = _AcPMTrunkUtilizationAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 21, 1, 4),
    _AcPMTrunkUtilizationAverage_Type()
)
acPMTrunkUtilizationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTrunkUtilizationAverage.setStatus("current")


class _AcPMTrunkUtilizationMax_Type(Integer32):
    """Custom type acPMTrunkUtilizationMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTrunkUtilizationMax_Type.__name__ = "Integer32"
_AcPMTrunkUtilizationMax_Object = MibTableColumn
acPMTrunkUtilizationMax = _AcPMTrunkUtilizationMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 21, 1, 5),
    _AcPMTrunkUtilizationMax_Type()
)
acPMTrunkUtilizationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTrunkUtilizationMax.setStatus("current")


class _AcPMTrunkUtilizationMin_Type(Integer32):
    """Custom type acPMTrunkUtilizationMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTrunkUtilizationMin_Type.__name__ = "Integer32"
_AcPMTrunkUtilizationMin_Object = MibTableColumn
acPMTrunkUtilizationMin = _AcPMTrunkUtilizationMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 21, 1, 6),
    _AcPMTrunkUtilizationMin_Type()
)
acPMTrunkUtilizationMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTrunkUtilizationMin.setStatus("current")
_AcPMTrunkUtilizationVolume_Type = Counter32
_AcPMTrunkUtilizationVolume_Object = MibTableColumn
acPMTrunkUtilizationVolume = _AcPMTrunkUtilizationVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 21, 1, 7),
    _AcPMTrunkUtilizationVolume_Type()
)
acPMTrunkUtilizationVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTrunkUtilizationVolume.setStatus("current")


class _AcPMTrunkUtilizationTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMTrunkUtilizationTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTrunkUtilizationTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMTrunkUtilizationTimeBelowLowThreshold_Object = MibTableColumn
acPMTrunkUtilizationTimeBelowLowThreshold = _AcPMTrunkUtilizationTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 21, 1, 8),
    _AcPMTrunkUtilizationTimeBelowLowThreshold_Type()
)
acPMTrunkUtilizationTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTrunkUtilizationTimeBelowLowThreshold.setStatus("current")


class _AcPMTrunkUtilizationTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMTrunkUtilizationTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTrunkUtilizationTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMTrunkUtilizationTimeBetweenThresholds_Object = MibTableColumn
acPMTrunkUtilizationTimeBetweenThresholds = _AcPMTrunkUtilizationTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 21, 1, 9),
    _AcPMTrunkUtilizationTimeBetweenThresholds_Type()
)
acPMTrunkUtilizationTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTrunkUtilizationTimeBetweenThresholds.setStatus("current")


class _AcPMTrunkUtilizationTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMTrunkUtilizationTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTrunkUtilizationTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMTrunkUtilizationTimeAboveHighThreshold_Object = MibTableColumn
acPMTrunkUtilizationTimeAboveHighThreshold = _AcPMTrunkUtilizationTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 21, 1, 10),
    _AcPMTrunkUtilizationTimeAboveHighThreshold_Type()
)
acPMTrunkUtilizationTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTrunkUtilizationTimeAboveHighThreshold.setStatus("current")


class _AcPMTrunkUtilizationFullDayAverage_Type(Integer32):
    """Custom type acPMTrunkUtilizationFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTrunkUtilizationFullDayAverage_Type.__name__ = "Integer32"
_AcPMTrunkUtilizationFullDayAverage_Object = MibTableColumn
acPMTrunkUtilizationFullDayAverage = _AcPMTrunkUtilizationFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 21, 1, 11),
    _AcPMTrunkUtilizationFullDayAverage_Type()
)
acPMTrunkUtilizationFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTrunkUtilizationFullDayAverage.setStatus("current")


class _AcPMTrunkUtilizationTotal_Type(Integer32):
    """Custom type acPMTrunkUtilizationTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTrunkUtilizationTotal_Type.__name__ = "Integer32"
_AcPMTrunkUtilizationTotal_Object = MibTableColumn
acPMTrunkUtilizationTotal = _AcPMTrunkUtilizationTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 21, 1, 12),
    _AcPMTrunkUtilizationTotal_Type()
)
acPMTrunkUtilizationTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTrunkUtilizationTotal.setStatus("current")
_AcPMPSTNTrunkActivitySecondsTable_Object = MibTable
acPMPSTNTrunkActivitySecondsTable = _AcPMPSTNTrunkActivitySecondsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 22)
)
if mibBuilder.loadTexts:
    acPMPSTNTrunkActivitySecondsTable.setStatus("current")
_AcPMPSTNTrunkActivitySecondsEntry_Object = MibTableRow
acPMPSTNTrunkActivitySecondsEntry = _AcPMPSTNTrunkActivitySecondsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 22, 1)
)
acPMPSTNTrunkActivitySecondsEntry.setIndexNames(
    (0, "AC-PM-PSTN-MIB", "acPMPSTNTrunkActivitySecondsTrunkNum"),
    (0, "AC-PM-PSTN-MIB", "acPMPSTNTrunkActivitySecondsInterval"),
)
if mibBuilder.loadTexts:
    acPMPSTNTrunkActivitySecondsEntry.setStatus("current")


class _AcPMPSTNTrunkActivitySecondsTrunkNum_Type(Unsigned32):
    """Custom type acPMPSTNTrunkActivitySecondsTrunkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMPSTNTrunkActivitySecondsTrunkNum_Type.__name__ = "Unsigned32"
_AcPMPSTNTrunkActivitySecondsTrunkNum_Object = MibTableColumn
acPMPSTNTrunkActivitySecondsTrunkNum = _AcPMPSTNTrunkActivitySecondsTrunkNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 22, 1, 1),
    _AcPMPSTNTrunkActivitySecondsTrunkNum_Type()
)
acPMPSTNTrunkActivitySecondsTrunkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMPSTNTrunkActivitySecondsTrunkNum.setStatus("current")


class _AcPMPSTNTrunkActivitySecondsInterval_Type(Unsigned32):
    """Custom type acPMPSTNTrunkActivitySecondsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMPSTNTrunkActivitySecondsInterval_Type.__name__ = "Unsigned32"
_AcPMPSTNTrunkActivitySecondsInterval_Object = MibTableColumn
acPMPSTNTrunkActivitySecondsInterval = _AcPMPSTNTrunkActivitySecondsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 22, 1, 2),
    _AcPMPSTNTrunkActivitySecondsInterval_Type()
)
acPMPSTNTrunkActivitySecondsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMPSTNTrunkActivitySecondsInterval.setStatus("current")
_AcPMPSTNTrunkActivitySecondsVal_Type = Gauge32
_AcPMPSTNTrunkActivitySecondsVal_Object = MibTableColumn
acPMPSTNTrunkActivitySecondsVal = _AcPMPSTNTrunkActivitySecondsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 22, 1, 3),
    _AcPMPSTNTrunkActivitySecondsVal_Type()
)
acPMPSTNTrunkActivitySecondsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNTrunkActivitySecondsVal.setStatus("current")


class _AcPMPSTNTrunkActivitySecondsTotal_Type(Integer32):
    """Custom type acPMPSTNTrunkActivitySecondsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPSTNTrunkActivitySecondsTotal_Type.__name__ = "Integer32"
_AcPMPSTNTrunkActivitySecondsTotal_Object = MibTableColumn
acPMPSTNTrunkActivitySecondsTotal = _AcPMPSTNTrunkActivitySecondsTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 22, 1, 4),
    _AcPMPSTNTrunkActivitySecondsTotal_Type()
)
acPMPSTNTrunkActivitySecondsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNTrunkActivitySecondsTotal.setStatus("current")
_AcPMPSTNTrunkActivitySecondsVolume_Type = Counter32
_AcPMPSTNTrunkActivitySecondsVolume_Object = MibTableColumn
acPMPSTNTrunkActivitySecondsVolume = _AcPMPSTNTrunkActivitySecondsVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 22, 1, 5),
    _AcPMPSTNTrunkActivitySecondsVolume_Type()
)
acPMPSTNTrunkActivitySecondsVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNTrunkActivitySecondsVolume.setStatus("current")
_AcPMPSTNChannels_ObjectIdentity = ObjectIdentity
acPMPSTNChannels = _AcPMPSTNChannels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31)
)
_AcPMPSTNNumOfChannelsInServiceTable_Object = MibTable
acPMPSTNNumOfChannelsInServiceTable = _AcPMPSTNNumOfChannelsInServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 1)
)
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInServiceTable.setStatus("current")
_AcPMPSTNNumOfChannelsInServiceEntry_Object = MibTableRow
acPMPSTNNumOfChannelsInServiceEntry = _AcPMPSTNNumOfChannelsInServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 1, 1)
)
acPMPSTNNumOfChannelsInServiceEntry.setIndexNames(
    (0, "AC-PM-PSTN-MIB", "acPMPSTNNumOfChannelsInServiceTrunkNum"),
    (0, "AC-PM-PSTN-MIB", "acPMPSTNNumOfChannelsInServiceInterval"),
)
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInServiceEntry.setStatus("current")


class _AcPMPSTNNumOfChannelsInServiceTrunkNum_Type(Unsigned32):
    """Custom type acPMPSTNNumOfChannelsInServiceTrunkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMPSTNNumOfChannelsInServiceTrunkNum_Type.__name__ = "Unsigned32"
_AcPMPSTNNumOfChannelsInServiceTrunkNum_Object = MibTableColumn
acPMPSTNNumOfChannelsInServiceTrunkNum = _AcPMPSTNNumOfChannelsInServiceTrunkNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 1, 1, 1),
    _AcPMPSTNNumOfChannelsInServiceTrunkNum_Type()
)
acPMPSTNNumOfChannelsInServiceTrunkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInServiceTrunkNum.setStatus("current")


class _AcPMPSTNNumOfChannelsInServiceInterval_Type(Unsigned32):
    """Custom type acPMPSTNNumOfChannelsInServiceInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMPSTNNumOfChannelsInServiceInterval_Type.__name__ = "Unsigned32"
_AcPMPSTNNumOfChannelsInServiceInterval_Object = MibTableColumn
acPMPSTNNumOfChannelsInServiceInterval = _AcPMPSTNNumOfChannelsInServiceInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 1, 1, 2),
    _AcPMPSTNNumOfChannelsInServiceInterval_Type()
)
acPMPSTNNumOfChannelsInServiceInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInServiceInterval.setStatus("current")
_AcPMPSTNNumOfChannelsInServiceVal_Type = Gauge32
_AcPMPSTNNumOfChannelsInServiceVal_Object = MibTableColumn
acPMPSTNNumOfChannelsInServiceVal = _AcPMPSTNNumOfChannelsInServiceVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 1, 1, 3),
    _AcPMPSTNNumOfChannelsInServiceVal_Type()
)
acPMPSTNNumOfChannelsInServiceVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInServiceVal.setStatus("current")


class _AcPMPSTNNumOfChannelsInServiceAverage_Type(Integer32):
    """Custom type acPMPSTNNumOfChannelsInServiceAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPSTNNumOfChannelsInServiceAverage_Type.__name__ = "Integer32"
_AcPMPSTNNumOfChannelsInServiceAverage_Object = MibTableColumn
acPMPSTNNumOfChannelsInServiceAverage = _AcPMPSTNNumOfChannelsInServiceAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 1, 1, 4),
    _AcPMPSTNNumOfChannelsInServiceAverage_Type()
)
acPMPSTNNumOfChannelsInServiceAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInServiceAverage.setStatus("current")


class _AcPMPSTNNumOfChannelsInServiceMax_Type(Integer32):
    """Custom type acPMPSTNNumOfChannelsInServiceMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPSTNNumOfChannelsInServiceMax_Type.__name__ = "Integer32"
_AcPMPSTNNumOfChannelsInServiceMax_Object = MibTableColumn
acPMPSTNNumOfChannelsInServiceMax = _AcPMPSTNNumOfChannelsInServiceMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 1, 1, 5),
    _AcPMPSTNNumOfChannelsInServiceMax_Type()
)
acPMPSTNNumOfChannelsInServiceMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInServiceMax.setStatus("current")


class _AcPMPSTNNumOfChannelsInServiceMin_Type(Integer32):
    """Custom type acPMPSTNNumOfChannelsInServiceMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPSTNNumOfChannelsInServiceMin_Type.__name__ = "Integer32"
_AcPMPSTNNumOfChannelsInServiceMin_Object = MibTableColumn
acPMPSTNNumOfChannelsInServiceMin = _AcPMPSTNNumOfChannelsInServiceMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 1, 1, 6),
    _AcPMPSTNNumOfChannelsInServiceMin_Type()
)
acPMPSTNNumOfChannelsInServiceMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInServiceMin.setStatus("current")
_AcPMPSTNNumOfChannelsInServiceVolume_Type = Counter32
_AcPMPSTNNumOfChannelsInServiceVolume_Object = MibTableColumn
acPMPSTNNumOfChannelsInServiceVolume = _AcPMPSTNNumOfChannelsInServiceVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 1, 1, 7),
    _AcPMPSTNNumOfChannelsInServiceVolume_Type()
)
acPMPSTNNumOfChannelsInServiceVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInServiceVolume.setStatus("current")
_AcPMPSTNNumOfChannelsOutOfServiceTable_Object = MibTable
acPMPSTNNumOfChannelsOutOfServiceTable = _AcPMPSTNNumOfChannelsOutOfServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 2)
)
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsOutOfServiceTable.setStatus("current")
_AcPMPSTNNumOfChannelsOutOfServiceEntry_Object = MibTableRow
acPMPSTNNumOfChannelsOutOfServiceEntry = _AcPMPSTNNumOfChannelsOutOfServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 2, 1)
)
acPMPSTNNumOfChannelsOutOfServiceEntry.setIndexNames(
    (0, "AC-PM-PSTN-MIB", "acPMPSTNNumOfChannelsOutOfServiceTrunkNum"),
    (0, "AC-PM-PSTN-MIB", "acPMPSTNNumOfChannelsOutOfServiceInterval"),
)
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsOutOfServiceEntry.setStatus("current")


class _AcPMPSTNNumOfChannelsOutOfServiceTrunkNum_Type(Unsigned32):
    """Custom type acPMPSTNNumOfChannelsOutOfServiceTrunkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMPSTNNumOfChannelsOutOfServiceTrunkNum_Type.__name__ = "Unsigned32"
_AcPMPSTNNumOfChannelsOutOfServiceTrunkNum_Object = MibTableColumn
acPMPSTNNumOfChannelsOutOfServiceTrunkNum = _AcPMPSTNNumOfChannelsOutOfServiceTrunkNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 2, 1, 1),
    _AcPMPSTNNumOfChannelsOutOfServiceTrunkNum_Type()
)
acPMPSTNNumOfChannelsOutOfServiceTrunkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsOutOfServiceTrunkNum.setStatus("current")


class _AcPMPSTNNumOfChannelsOutOfServiceInterval_Type(Unsigned32):
    """Custom type acPMPSTNNumOfChannelsOutOfServiceInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMPSTNNumOfChannelsOutOfServiceInterval_Type.__name__ = "Unsigned32"
_AcPMPSTNNumOfChannelsOutOfServiceInterval_Object = MibTableColumn
acPMPSTNNumOfChannelsOutOfServiceInterval = _AcPMPSTNNumOfChannelsOutOfServiceInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 2, 1, 2),
    _AcPMPSTNNumOfChannelsOutOfServiceInterval_Type()
)
acPMPSTNNumOfChannelsOutOfServiceInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsOutOfServiceInterval.setStatus("current")
_AcPMPSTNNumOfChannelsOutOfServiceVal_Type = Gauge32
_AcPMPSTNNumOfChannelsOutOfServiceVal_Object = MibTableColumn
acPMPSTNNumOfChannelsOutOfServiceVal = _AcPMPSTNNumOfChannelsOutOfServiceVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 2, 1, 3),
    _AcPMPSTNNumOfChannelsOutOfServiceVal_Type()
)
acPMPSTNNumOfChannelsOutOfServiceVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsOutOfServiceVal.setStatus("current")


class _AcPMPSTNNumOfChannelsOutOfServiceAverage_Type(Integer32):
    """Custom type acPMPSTNNumOfChannelsOutOfServiceAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPSTNNumOfChannelsOutOfServiceAverage_Type.__name__ = "Integer32"
_AcPMPSTNNumOfChannelsOutOfServiceAverage_Object = MibTableColumn
acPMPSTNNumOfChannelsOutOfServiceAverage = _AcPMPSTNNumOfChannelsOutOfServiceAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 2, 1, 4),
    _AcPMPSTNNumOfChannelsOutOfServiceAverage_Type()
)
acPMPSTNNumOfChannelsOutOfServiceAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsOutOfServiceAverage.setStatus("current")


class _AcPMPSTNNumOfChannelsOutOfServiceMax_Type(Integer32):
    """Custom type acPMPSTNNumOfChannelsOutOfServiceMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPSTNNumOfChannelsOutOfServiceMax_Type.__name__ = "Integer32"
_AcPMPSTNNumOfChannelsOutOfServiceMax_Object = MibTableColumn
acPMPSTNNumOfChannelsOutOfServiceMax = _AcPMPSTNNumOfChannelsOutOfServiceMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 2, 1, 5),
    _AcPMPSTNNumOfChannelsOutOfServiceMax_Type()
)
acPMPSTNNumOfChannelsOutOfServiceMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsOutOfServiceMax.setStatus("current")


class _AcPMPSTNNumOfChannelsOutOfServiceMin_Type(Integer32):
    """Custom type acPMPSTNNumOfChannelsOutOfServiceMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPSTNNumOfChannelsOutOfServiceMin_Type.__name__ = "Integer32"
_AcPMPSTNNumOfChannelsOutOfServiceMin_Object = MibTableColumn
acPMPSTNNumOfChannelsOutOfServiceMin = _AcPMPSTNNumOfChannelsOutOfServiceMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 2, 1, 6),
    _AcPMPSTNNumOfChannelsOutOfServiceMin_Type()
)
acPMPSTNNumOfChannelsOutOfServiceMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsOutOfServiceMin.setStatus("current")
_AcPMPSTNNumOfChannelsOutOfServiceVolume_Type = Counter32
_AcPMPSTNNumOfChannelsOutOfServiceVolume_Object = MibTableColumn
acPMPSTNNumOfChannelsOutOfServiceVolume = _AcPMPSTNNumOfChannelsOutOfServiceVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 2, 1, 7),
    _AcPMPSTNNumOfChannelsOutOfServiceVolume_Type()
)
acPMPSTNNumOfChannelsOutOfServiceVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsOutOfServiceVolume.setStatus("current")
_AcPMPSTNNumOfChannelsInMaintenanceTable_Object = MibTable
acPMPSTNNumOfChannelsInMaintenanceTable = _AcPMPSTNNumOfChannelsInMaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 3)
)
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInMaintenanceTable.setStatus("current")
_AcPMPSTNNumOfChannelsInMaintenanceEntry_Object = MibTableRow
acPMPSTNNumOfChannelsInMaintenanceEntry = _AcPMPSTNNumOfChannelsInMaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 3, 1)
)
acPMPSTNNumOfChannelsInMaintenanceEntry.setIndexNames(
    (0, "AC-PM-PSTN-MIB", "acPMPSTNNumOfChannelsInMaintenanceTrunkNum"),
    (0, "AC-PM-PSTN-MIB", "acPMPSTNNumOfChannelsInMaintenanceInterval"),
)
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInMaintenanceEntry.setStatus("current")


class _AcPMPSTNNumOfChannelsInMaintenanceTrunkNum_Type(Unsigned32):
    """Custom type acPMPSTNNumOfChannelsInMaintenanceTrunkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMPSTNNumOfChannelsInMaintenanceTrunkNum_Type.__name__ = "Unsigned32"
_AcPMPSTNNumOfChannelsInMaintenanceTrunkNum_Object = MibTableColumn
acPMPSTNNumOfChannelsInMaintenanceTrunkNum = _AcPMPSTNNumOfChannelsInMaintenanceTrunkNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 3, 1, 1),
    _AcPMPSTNNumOfChannelsInMaintenanceTrunkNum_Type()
)
acPMPSTNNumOfChannelsInMaintenanceTrunkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInMaintenanceTrunkNum.setStatus("current")


class _AcPMPSTNNumOfChannelsInMaintenanceInterval_Type(Unsigned32):
    """Custom type acPMPSTNNumOfChannelsInMaintenanceInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMPSTNNumOfChannelsInMaintenanceInterval_Type.__name__ = "Unsigned32"
_AcPMPSTNNumOfChannelsInMaintenanceInterval_Object = MibTableColumn
acPMPSTNNumOfChannelsInMaintenanceInterval = _AcPMPSTNNumOfChannelsInMaintenanceInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 3, 1, 2),
    _AcPMPSTNNumOfChannelsInMaintenanceInterval_Type()
)
acPMPSTNNumOfChannelsInMaintenanceInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInMaintenanceInterval.setStatus("current")
_AcPMPSTNNumOfChannelsInMaintenanceVal_Type = Gauge32
_AcPMPSTNNumOfChannelsInMaintenanceVal_Object = MibTableColumn
acPMPSTNNumOfChannelsInMaintenanceVal = _AcPMPSTNNumOfChannelsInMaintenanceVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 3, 1, 3),
    _AcPMPSTNNumOfChannelsInMaintenanceVal_Type()
)
acPMPSTNNumOfChannelsInMaintenanceVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInMaintenanceVal.setStatus("current")


class _AcPMPSTNNumOfChannelsInMaintenanceAverage_Type(Integer32):
    """Custom type acPMPSTNNumOfChannelsInMaintenanceAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPSTNNumOfChannelsInMaintenanceAverage_Type.__name__ = "Integer32"
_AcPMPSTNNumOfChannelsInMaintenanceAverage_Object = MibTableColumn
acPMPSTNNumOfChannelsInMaintenanceAverage = _AcPMPSTNNumOfChannelsInMaintenanceAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 3, 1, 4),
    _AcPMPSTNNumOfChannelsInMaintenanceAverage_Type()
)
acPMPSTNNumOfChannelsInMaintenanceAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInMaintenanceAverage.setStatus("current")


class _AcPMPSTNNumOfChannelsInMaintenanceMax_Type(Integer32):
    """Custom type acPMPSTNNumOfChannelsInMaintenanceMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPSTNNumOfChannelsInMaintenanceMax_Type.__name__ = "Integer32"
_AcPMPSTNNumOfChannelsInMaintenanceMax_Object = MibTableColumn
acPMPSTNNumOfChannelsInMaintenanceMax = _AcPMPSTNNumOfChannelsInMaintenanceMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 3, 1, 5),
    _AcPMPSTNNumOfChannelsInMaintenanceMax_Type()
)
acPMPSTNNumOfChannelsInMaintenanceMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInMaintenanceMax.setStatus("current")


class _AcPMPSTNNumOfChannelsInMaintenanceMin_Type(Integer32):
    """Custom type acPMPSTNNumOfChannelsInMaintenanceMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPSTNNumOfChannelsInMaintenanceMin_Type.__name__ = "Integer32"
_AcPMPSTNNumOfChannelsInMaintenanceMin_Object = MibTableColumn
acPMPSTNNumOfChannelsInMaintenanceMin = _AcPMPSTNNumOfChannelsInMaintenanceMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 3, 1, 6),
    _AcPMPSTNNumOfChannelsInMaintenanceMin_Type()
)
acPMPSTNNumOfChannelsInMaintenanceMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInMaintenanceMin.setStatus("current")
_AcPMPSTNNumOfChannelsInMaintenanceVolume_Type = Counter32
_AcPMPSTNNumOfChannelsInMaintenanceVolume_Object = MibTableColumn
acPMPSTNNumOfChannelsInMaintenanceVolume = _AcPMPSTNNumOfChannelsInMaintenanceVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 10, 2, 31, 3, 1, 7),
    _AcPMPSTNNumOfChannelsInMaintenanceVolume_Type()
)
acPMPSTNNumOfChannelsInMaintenanceVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPSTNNumOfChannelsInMaintenanceVolume.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AC-PM-PSTN-MIB",
    **{"acPMPSTN": acPMPSTN,
       "acPMPSTNConfiguration": acPMPSTNConfiguration,
       "acPMPSTNConfigurationPeriodLength": acPMPSTNConfigurationPeriodLength,
       "acPMPSTNConfigurationResetTotalCounters": acPMPSTNConfigurationResetTotalCounters,
       "acPMTrunkUtilizationAttributes": acPMTrunkUtilizationAttributes,
       "acPMTrunkUtilizationAttributesHighThreshold": acPMTrunkUtilizationAttributesHighThreshold,
       "acPMTrunkUtilizationAttributesLowThreshold": acPMTrunkUtilizationAttributesLowThreshold,
       "acPMPSTNChannelsAttributes": acPMPSTNChannelsAttributes,
       "acPMPSTNChannelsAttributesInServiceHighThreshold": acPMPSTNChannelsAttributesInServiceHighThreshold,
       "acPMPSTNChannelsAttributesInServiceLowThreshold": acPMPSTNChannelsAttributesInServiceLowThreshold,
       "acPMPSTNChannelsAttributesOutOfServiceHighThreshold": acPMPSTNChannelsAttributesOutOfServiceHighThreshold,
       "acPMPSTNChannelsAttributesOutOfServiceLowThreshold": acPMPSTNChannelsAttributesOutOfServiceLowThreshold,
       "acPMPSTNChannelsAttributesInMaintenanceHighThreshold": acPMPSTNChannelsAttributesInMaintenanceHighThreshold,
       "acPMPSTNChannelsAttributesInMaintenanceLowThreshold": acPMPSTNChannelsAttributesInMaintenanceLowThreshold,
       "acPMPSTNData": acPMPSTNData,
       "acPMPSTNDataAcPMPSTNTimeFromStartOfInterval": acPMPSTNDataAcPMPSTNTimeFromStartOfInterval,
       "acPMTrunkUtilizationTable": acPMTrunkUtilizationTable,
       "acPMTrunkUtilizationEntry": acPMTrunkUtilizationEntry,
       "acPMTrunkUtilizationTrunkNum": acPMTrunkUtilizationTrunkNum,
       "acPMTrunkUtilizationInterval": acPMTrunkUtilizationInterval,
       "acPMTrunkUtilizationVal": acPMTrunkUtilizationVal,
       "acPMTrunkUtilizationAverage": acPMTrunkUtilizationAverage,
       "acPMTrunkUtilizationMax": acPMTrunkUtilizationMax,
       "acPMTrunkUtilizationMin": acPMTrunkUtilizationMin,
       "acPMTrunkUtilizationVolume": acPMTrunkUtilizationVolume,
       "acPMTrunkUtilizationTimeBelowLowThreshold": acPMTrunkUtilizationTimeBelowLowThreshold,
       "acPMTrunkUtilizationTimeBetweenThresholds": acPMTrunkUtilizationTimeBetweenThresholds,
       "acPMTrunkUtilizationTimeAboveHighThreshold": acPMTrunkUtilizationTimeAboveHighThreshold,
       "acPMTrunkUtilizationFullDayAverage": acPMTrunkUtilizationFullDayAverage,
       "acPMTrunkUtilizationTotal": acPMTrunkUtilizationTotal,
       "acPMPSTNTrunkActivitySecondsTable": acPMPSTNTrunkActivitySecondsTable,
       "acPMPSTNTrunkActivitySecondsEntry": acPMPSTNTrunkActivitySecondsEntry,
       "acPMPSTNTrunkActivitySecondsTrunkNum": acPMPSTNTrunkActivitySecondsTrunkNum,
       "acPMPSTNTrunkActivitySecondsInterval": acPMPSTNTrunkActivitySecondsInterval,
       "acPMPSTNTrunkActivitySecondsVal": acPMPSTNTrunkActivitySecondsVal,
       "acPMPSTNTrunkActivitySecondsTotal": acPMPSTNTrunkActivitySecondsTotal,
       "acPMPSTNTrunkActivitySecondsVolume": acPMPSTNTrunkActivitySecondsVolume,
       "acPMPSTNChannels": acPMPSTNChannels,
       "acPMPSTNNumOfChannelsInServiceTable": acPMPSTNNumOfChannelsInServiceTable,
       "acPMPSTNNumOfChannelsInServiceEntry": acPMPSTNNumOfChannelsInServiceEntry,
       "acPMPSTNNumOfChannelsInServiceTrunkNum": acPMPSTNNumOfChannelsInServiceTrunkNum,
       "acPMPSTNNumOfChannelsInServiceInterval": acPMPSTNNumOfChannelsInServiceInterval,
       "acPMPSTNNumOfChannelsInServiceVal": acPMPSTNNumOfChannelsInServiceVal,
       "acPMPSTNNumOfChannelsInServiceAverage": acPMPSTNNumOfChannelsInServiceAverage,
       "acPMPSTNNumOfChannelsInServiceMax": acPMPSTNNumOfChannelsInServiceMax,
       "acPMPSTNNumOfChannelsInServiceMin": acPMPSTNNumOfChannelsInServiceMin,
       "acPMPSTNNumOfChannelsInServiceVolume": acPMPSTNNumOfChannelsInServiceVolume,
       "acPMPSTNNumOfChannelsOutOfServiceTable": acPMPSTNNumOfChannelsOutOfServiceTable,
       "acPMPSTNNumOfChannelsOutOfServiceEntry": acPMPSTNNumOfChannelsOutOfServiceEntry,
       "acPMPSTNNumOfChannelsOutOfServiceTrunkNum": acPMPSTNNumOfChannelsOutOfServiceTrunkNum,
       "acPMPSTNNumOfChannelsOutOfServiceInterval": acPMPSTNNumOfChannelsOutOfServiceInterval,
       "acPMPSTNNumOfChannelsOutOfServiceVal": acPMPSTNNumOfChannelsOutOfServiceVal,
       "acPMPSTNNumOfChannelsOutOfServiceAverage": acPMPSTNNumOfChannelsOutOfServiceAverage,
       "acPMPSTNNumOfChannelsOutOfServiceMax": acPMPSTNNumOfChannelsOutOfServiceMax,
       "acPMPSTNNumOfChannelsOutOfServiceMin": acPMPSTNNumOfChannelsOutOfServiceMin,
       "acPMPSTNNumOfChannelsOutOfServiceVolume": acPMPSTNNumOfChannelsOutOfServiceVolume,
       "acPMPSTNNumOfChannelsInMaintenanceTable": acPMPSTNNumOfChannelsInMaintenanceTable,
       "acPMPSTNNumOfChannelsInMaintenanceEntry": acPMPSTNNumOfChannelsInMaintenanceEntry,
       "acPMPSTNNumOfChannelsInMaintenanceTrunkNum": acPMPSTNNumOfChannelsInMaintenanceTrunkNum,
       "acPMPSTNNumOfChannelsInMaintenanceInterval": acPMPSTNNumOfChannelsInMaintenanceInterval,
       "acPMPSTNNumOfChannelsInMaintenanceVal": acPMPSTNNumOfChannelsInMaintenanceVal,
       "acPMPSTNNumOfChannelsInMaintenanceAverage": acPMPSTNNumOfChannelsInMaintenanceAverage,
       "acPMPSTNNumOfChannelsInMaintenanceMax": acPMPSTNNumOfChannelsInMaintenanceMax,
       "acPMPSTNNumOfChannelsInMaintenanceMin": acPMPSTNNumOfChannelsInMaintenanceMin,
       "acPMPSTNNumOfChannelsInMaintenanceVolume": acPMPSTNNumOfChannelsInMaintenanceVolume}
)
