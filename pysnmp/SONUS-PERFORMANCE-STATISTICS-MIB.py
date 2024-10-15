# SNMP MIB module (SONUS-PERFORMANCE-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-PERFORMANCE-STATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:06 2024
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

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

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

(sonusResourcesMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusResourcesMIBs")


# MODULE-IDENTITY

sonusPerformanceStatisticsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusPerformanceStatisticsObjects_ObjectIdentity = ObjectIdentity
sonusPerformanceStatisticsObjects = _SonusPerformanceStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1)
)
_SonusTrunkGroup_ObjectIdentity = ObjectIdentity
sonusTrunkGroup = _SonusTrunkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1)
)


class _SonusTrunkGroupIntervalSize_Type(Integer32):
    """Custom type sonusTrunkGroupIntervalSize based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1440),
    )


_SonusTrunkGroupIntervalSize_Type.__name__ = "Integer32"
_SonusTrunkGroupIntervalSize_Object = MibScalar
sonusTrunkGroupIntervalSize = _SonusTrunkGroupIntervalSize_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 1),
    _SonusTrunkGroupIntervalSize_Type()
)
sonusTrunkGroupIntervalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalSize.setStatus("current")


class _SonusTrunkGroupNumberOfIntervals_Type(Integer32):
    """Custom type sonusTrunkGroupNumberOfIntervals based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 288),
    )


_SonusTrunkGroupNumberOfIntervals_Type.__name__ = "Integer32"
_SonusTrunkGroupNumberOfIntervals_Object = MibScalar
sonusTrunkGroupNumberOfIntervals = _SonusTrunkGroupNumberOfIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 2),
    _SonusTrunkGroupNumberOfIntervals_Type()
)
sonusTrunkGroupNumberOfIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupNumberOfIntervals.setStatus("current")
_SonusTrunkGroupCurrentTable_Object = MibTable
sonusTrunkGroupCurrentTable = _SonusTrunkGroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentTable.setStatus("current")
_SonusTrunkGroupCurrentEntry_Object = MibTableRow
sonusTrunkGroupCurrentEntry = _SonusTrunkGroupCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1)
)
sonusTrunkGroupCurrentEntry.setIndexNames(
    (0, "SONUS-PERFORMANCE-STATISTICS-MIB", "sonusTrunkGroupCurrentIndex"),
)
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentEntry.setStatus("current")
_SonusTrunkGroupCurrentIndex_Type = Integer32
_SonusTrunkGroupCurrentIndex_Object = MibTableColumn
sonusTrunkGroupCurrentIndex = _SonusTrunkGroupCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 1),
    _SonusTrunkGroupCurrentIndex_Type()
)
sonusTrunkGroupCurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentIndex.setStatus("current")
_SonusTrunkGroupCurrentInUsage_Type = PerfCurrentCount
_SonusTrunkGroupCurrentInUsage_Object = MibTableColumn
sonusTrunkGroupCurrentInUsage = _SonusTrunkGroupCurrentInUsage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 2),
    _SonusTrunkGroupCurrentInUsage_Type()
)
sonusTrunkGroupCurrentInUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentInUsage.setStatus("current")
_SonusTrunkGroupCurrentOutUsage_Type = PerfCurrentCount
_SonusTrunkGroupCurrentOutUsage_Object = MibTableColumn
sonusTrunkGroupCurrentOutUsage = _SonusTrunkGroupCurrentOutUsage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 3),
    _SonusTrunkGroupCurrentOutUsage_Type()
)
sonusTrunkGroupCurrentOutUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentOutUsage.setStatus("current")
_SonusTrunkGroupCurrentInCalls_Type = PerfCurrentCount
_SonusTrunkGroupCurrentInCalls_Object = MibTableColumn
sonusTrunkGroupCurrentInCalls = _SonusTrunkGroupCurrentInCalls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 4),
    _SonusTrunkGroupCurrentInCalls_Type()
)
sonusTrunkGroupCurrentInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentInCalls.setStatus("current")
_SonusTrunkGroupCurrentOutCalls_Type = PerfCurrentCount
_SonusTrunkGroupCurrentOutCalls_Object = MibTableColumn
sonusTrunkGroupCurrentOutCalls = _SonusTrunkGroupCurrentOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 5),
    _SonusTrunkGroupCurrentOutCalls_Type()
)
sonusTrunkGroupCurrentOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentOutCalls.setStatus("current")
_SonusTrunkGroupCurrentInCallAttempts_Type = PerfCurrentCount
_SonusTrunkGroupCurrentInCallAttempts_Object = MibTableColumn
sonusTrunkGroupCurrentInCallAttempts = _SonusTrunkGroupCurrentInCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 6),
    _SonusTrunkGroupCurrentInCallAttempts_Type()
)
sonusTrunkGroupCurrentInCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentInCallAttempts.setStatus("current")
_SonusTrunkGroupCurrentOutCallAttempts_Type = PerfCurrentCount
_SonusTrunkGroupCurrentOutCallAttempts_Object = MibTableColumn
sonusTrunkGroupCurrentOutCallAttempts = _SonusTrunkGroupCurrentOutCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 7),
    _SonusTrunkGroupCurrentOutCallAttempts_Type()
)
sonusTrunkGroupCurrentOutCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentOutCallAttempts.setStatus("current")
_SonusTrunkGroupCurrentMaxCompletedCalls_Type = PerfCurrentCount
_SonusTrunkGroupCurrentMaxCompletedCalls_Object = MibTableColumn
sonusTrunkGroupCurrentMaxCompletedCalls = _SonusTrunkGroupCurrentMaxCompletedCalls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 8),
    _SonusTrunkGroupCurrentMaxCompletedCalls_Type()
)
sonusTrunkGroupCurrentMaxCompletedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentMaxCompletedCalls.setStatus("current")
_SonusTrunkGroupCurrentCallSetupTime_Type = PerfCurrentCount
_SonusTrunkGroupCurrentCallSetupTime_Object = MibTableColumn
sonusTrunkGroupCurrentCallSetupTime = _SonusTrunkGroupCurrentCallSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 9),
    _SonusTrunkGroupCurrentCallSetupTime_Type()
)
sonusTrunkGroupCurrentCallSetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentCallSetupTime.setStatus("current")
_SonusTrunkGroupCurrentCallSetups_Type = PerfCurrentCount
_SonusTrunkGroupCurrentCallSetups_Object = MibTableColumn
sonusTrunkGroupCurrentCallSetups = _SonusTrunkGroupCurrentCallSetups_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 10),
    _SonusTrunkGroupCurrentCallSetups_Type()
)
sonusTrunkGroupCurrentCallSetups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentCallSetups.setStatus("current")
_SonusTrunkGroupCurrentInCallFailNoRoutes_Type = PerfCurrentCount
_SonusTrunkGroupCurrentInCallFailNoRoutes_Object = MibTableColumn
sonusTrunkGroupCurrentInCallFailNoRoutes = _SonusTrunkGroupCurrentInCallFailNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 11),
    _SonusTrunkGroupCurrentInCallFailNoRoutes_Type()
)
sonusTrunkGroupCurrentInCallFailNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentInCallFailNoRoutes.setStatus("current")
_SonusTrunkGroupCurrentInCallFailNoResources_Type = PerfCurrentCount
_SonusTrunkGroupCurrentInCallFailNoResources_Object = MibTableColumn
sonusTrunkGroupCurrentInCallFailNoResources = _SonusTrunkGroupCurrentInCallFailNoResources_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 12),
    _SonusTrunkGroupCurrentInCallFailNoResources_Type()
)
sonusTrunkGroupCurrentInCallFailNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentInCallFailNoResources.setStatus("current")
_SonusTrunkGroupCurrentInCallFailNoService_Type = PerfCurrentCount
_SonusTrunkGroupCurrentInCallFailNoService_Object = MibTableColumn
sonusTrunkGroupCurrentInCallFailNoService = _SonusTrunkGroupCurrentInCallFailNoService_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 13),
    _SonusTrunkGroupCurrentInCallFailNoService_Type()
)
sonusTrunkGroupCurrentInCallFailNoService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentInCallFailNoService.setStatus("current")
_SonusTrunkGroupCurrentInCallFailInvalidCall_Type = PerfCurrentCount
_SonusTrunkGroupCurrentInCallFailInvalidCall_Object = MibTableColumn
sonusTrunkGroupCurrentInCallFailInvalidCall = _SonusTrunkGroupCurrentInCallFailInvalidCall_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 14),
    _SonusTrunkGroupCurrentInCallFailInvalidCall_Type()
)
sonusTrunkGroupCurrentInCallFailInvalidCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentInCallFailInvalidCall.setStatus("current")
_SonusTrunkGroupCurrentInCallFailNetworkFailure_Type = PerfCurrentCount
_SonusTrunkGroupCurrentInCallFailNetworkFailure_Object = MibTableColumn
sonusTrunkGroupCurrentInCallFailNetworkFailure = _SonusTrunkGroupCurrentInCallFailNetworkFailure_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 15),
    _SonusTrunkGroupCurrentInCallFailNetworkFailure_Type()
)
sonusTrunkGroupCurrentInCallFailNetworkFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentInCallFailNetworkFailure.setStatus("current")
_SonusTrunkGroupCurrentInCallFailProtocolError_Type = PerfCurrentCount
_SonusTrunkGroupCurrentInCallFailProtocolError_Object = MibTableColumn
sonusTrunkGroupCurrentInCallFailProtocolError = _SonusTrunkGroupCurrentInCallFailProtocolError_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 16),
    _SonusTrunkGroupCurrentInCallFailProtocolError_Type()
)
sonusTrunkGroupCurrentInCallFailProtocolError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentInCallFailProtocolError.setStatus("current")
_SonusTrunkGroupCurrentInCallFailUnspecified_Type = PerfCurrentCount
_SonusTrunkGroupCurrentInCallFailUnspecified_Object = MibTableColumn
sonusTrunkGroupCurrentInCallFailUnspecified = _SonusTrunkGroupCurrentInCallFailUnspecified_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 17),
    _SonusTrunkGroupCurrentInCallFailUnspecified_Type()
)
sonusTrunkGroupCurrentInCallFailUnspecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentInCallFailUnspecified.setStatus("current")
_SonusTrunkGroupCurrentOutCallFailNoRoutes_Type = PerfCurrentCount
_SonusTrunkGroupCurrentOutCallFailNoRoutes_Object = MibTableColumn
sonusTrunkGroupCurrentOutCallFailNoRoutes = _SonusTrunkGroupCurrentOutCallFailNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 18),
    _SonusTrunkGroupCurrentOutCallFailNoRoutes_Type()
)
sonusTrunkGroupCurrentOutCallFailNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentOutCallFailNoRoutes.setStatus("current")
_SonusTrunkGroupCurrentOutCallFailNoResources_Type = PerfCurrentCount
_SonusTrunkGroupCurrentOutCallFailNoResources_Object = MibTableColumn
sonusTrunkGroupCurrentOutCallFailNoResources = _SonusTrunkGroupCurrentOutCallFailNoResources_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 19),
    _SonusTrunkGroupCurrentOutCallFailNoResources_Type()
)
sonusTrunkGroupCurrentOutCallFailNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentOutCallFailNoResources.setStatus("current")
_SonusTrunkGroupCurrentOutCallFailNoService_Type = PerfCurrentCount
_SonusTrunkGroupCurrentOutCallFailNoService_Object = MibTableColumn
sonusTrunkGroupCurrentOutCallFailNoService = _SonusTrunkGroupCurrentOutCallFailNoService_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 20),
    _SonusTrunkGroupCurrentOutCallFailNoService_Type()
)
sonusTrunkGroupCurrentOutCallFailNoService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentOutCallFailNoService.setStatus("current")
_SonusTrunkGroupCurrentOutCallFailInvalidCall_Type = PerfCurrentCount
_SonusTrunkGroupCurrentOutCallFailInvalidCall_Object = MibTableColumn
sonusTrunkGroupCurrentOutCallFailInvalidCall = _SonusTrunkGroupCurrentOutCallFailInvalidCall_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 21),
    _SonusTrunkGroupCurrentOutCallFailInvalidCall_Type()
)
sonusTrunkGroupCurrentOutCallFailInvalidCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentOutCallFailInvalidCall.setStatus("current")
_SonusTrunkGroupCurrentOutCallFailNetworkFailure_Type = PerfCurrentCount
_SonusTrunkGroupCurrentOutCallFailNetworkFailure_Object = MibTableColumn
sonusTrunkGroupCurrentOutCallFailNetworkFailure = _SonusTrunkGroupCurrentOutCallFailNetworkFailure_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 22),
    _SonusTrunkGroupCurrentOutCallFailNetworkFailure_Type()
)
sonusTrunkGroupCurrentOutCallFailNetworkFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentOutCallFailNetworkFailure.setStatus("current")
_SonusTrunkGroupCurrentOutCallFailProtocolError_Type = PerfCurrentCount
_SonusTrunkGroupCurrentOutCallFailProtocolError_Object = MibTableColumn
sonusTrunkGroupCurrentOutCallFailProtocolError = _SonusTrunkGroupCurrentOutCallFailProtocolError_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 23),
    _SonusTrunkGroupCurrentOutCallFailProtocolError_Type()
)
sonusTrunkGroupCurrentOutCallFailProtocolError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentOutCallFailProtocolError.setStatus("current")
_SonusTrunkGroupCurrentOutCallFailUnspecified_Type = PerfCurrentCount
_SonusTrunkGroupCurrentOutCallFailUnspecified_Object = MibTableColumn
sonusTrunkGroupCurrentOutCallFailUnspecified = _SonusTrunkGroupCurrentOutCallFailUnspecified_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 3, 1, 24),
    _SonusTrunkGroupCurrentOutCallFailUnspecified_Type()
)
sonusTrunkGroupCurrentOutCallFailUnspecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupCurrentOutCallFailUnspecified.setStatus("current")
_SonusTrunkGroupIntervalTable_Object = MibTable
sonusTrunkGroupIntervalTable = _SonusTrunkGroupIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalTable.setStatus("current")
_SonusTrunkGroupIntervalEntry_Object = MibTableRow
sonusTrunkGroupIntervalEntry = _SonusTrunkGroupIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1)
)
sonusTrunkGroupIntervalEntry.setIndexNames(
    (0, "SONUS-PERFORMANCE-STATISTICS-MIB", "sonusTrunkGroupIntervalIndex"),
    (0, "SONUS-PERFORMANCE-STATISTICS-MIB", "sonusTrunkGroupIntervalNumber"),
)
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalEntry.setStatus("current")
_SonusTrunkGroupIntervalIndex_Type = Integer32
_SonusTrunkGroupIntervalIndex_Object = MibTableColumn
sonusTrunkGroupIntervalIndex = _SonusTrunkGroupIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 1),
    _SonusTrunkGroupIntervalIndex_Type()
)
sonusTrunkGroupIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalIndex.setStatus("current")


class _SonusTrunkGroupIntervalNumber_Type(Integer32):
    """Custom type sonusTrunkGroupIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 288),
    )


_SonusTrunkGroupIntervalNumber_Type.__name__ = "Integer32"
_SonusTrunkGroupIntervalNumber_Object = MibTableColumn
sonusTrunkGroupIntervalNumber = _SonusTrunkGroupIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 2),
    _SonusTrunkGroupIntervalNumber_Type()
)
sonusTrunkGroupIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalNumber.setStatus("current")
_SonusTrunkGroupIntervalInUsage_Type = PerfIntervalCount
_SonusTrunkGroupIntervalInUsage_Object = MibTableColumn
sonusTrunkGroupIntervalInUsage = _SonusTrunkGroupIntervalInUsage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 3),
    _SonusTrunkGroupIntervalInUsage_Type()
)
sonusTrunkGroupIntervalInUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalInUsage.setStatus("current")
_SonusTrunkGroupIntervalOutUsage_Type = PerfIntervalCount
_SonusTrunkGroupIntervalOutUsage_Object = MibTableColumn
sonusTrunkGroupIntervalOutUsage = _SonusTrunkGroupIntervalOutUsage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 4),
    _SonusTrunkGroupIntervalOutUsage_Type()
)
sonusTrunkGroupIntervalOutUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalOutUsage.setStatus("current")
_SonusTrunkGroupIntervalInCalls_Type = PerfIntervalCount
_SonusTrunkGroupIntervalInCalls_Object = MibTableColumn
sonusTrunkGroupIntervalInCalls = _SonusTrunkGroupIntervalInCalls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 5),
    _SonusTrunkGroupIntervalInCalls_Type()
)
sonusTrunkGroupIntervalInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalInCalls.setStatus("current")
_SonusTrunkGroupIntervalOutCalls_Type = PerfIntervalCount
_SonusTrunkGroupIntervalOutCalls_Object = MibTableColumn
sonusTrunkGroupIntervalOutCalls = _SonusTrunkGroupIntervalOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 6),
    _SonusTrunkGroupIntervalOutCalls_Type()
)
sonusTrunkGroupIntervalOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalOutCalls.setStatus("current")
_SonusTrunkGroupIntervalInCallAttempts_Type = PerfIntervalCount
_SonusTrunkGroupIntervalInCallAttempts_Object = MibTableColumn
sonusTrunkGroupIntervalInCallAttempts = _SonusTrunkGroupIntervalInCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 7),
    _SonusTrunkGroupIntervalInCallAttempts_Type()
)
sonusTrunkGroupIntervalInCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalInCallAttempts.setStatus("current")
_SonusTrunkGroupIntervalOutCallAttempts_Type = PerfIntervalCount
_SonusTrunkGroupIntervalOutCallAttempts_Object = MibTableColumn
sonusTrunkGroupIntervalOutCallAttempts = _SonusTrunkGroupIntervalOutCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 8),
    _SonusTrunkGroupIntervalOutCallAttempts_Type()
)
sonusTrunkGroupIntervalOutCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalOutCallAttempts.setStatus("current")
_SonusTrunkGroupIntervalMaxCompletedCalls_Type = PerfIntervalCount
_SonusTrunkGroupIntervalMaxCompletedCalls_Object = MibTableColumn
sonusTrunkGroupIntervalMaxCompletedCalls = _SonusTrunkGroupIntervalMaxCompletedCalls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 9),
    _SonusTrunkGroupIntervalMaxCompletedCalls_Type()
)
sonusTrunkGroupIntervalMaxCompletedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalMaxCompletedCalls.setStatus("current")
_SonusTrunkGroupIntervalCallSetupTime_Type = PerfIntervalCount
_SonusTrunkGroupIntervalCallSetupTime_Object = MibTableColumn
sonusTrunkGroupIntervalCallSetupTime = _SonusTrunkGroupIntervalCallSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 10),
    _SonusTrunkGroupIntervalCallSetupTime_Type()
)
sonusTrunkGroupIntervalCallSetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalCallSetupTime.setStatus("current")
_SonusTrunkGroupIntervalCallSetups_Type = PerfIntervalCount
_SonusTrunkGroupIntervalCallSetups_Object = MibTableColumn
sonusTrunkGroupIntervalCallSetups = _SonusTrunkGroupIntervalCallSetups_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 11),
    _SonusTrunkGroupIntervalCallSetups_Type()
)
sonusTrunkGroupIntervalCallSetups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalCallSetups.setStatus("current")
_SonusTrunkGroupIntervalInCallFailNoRoutes_Type = PerfIntervalCount
_SonusTrunkGroupIntervalInCallFailNoRoutes_Object = MibTableColumn
sonusTrunkGroupIntervalInCallFailNoRoutes = _SonusTrunkGroupIntervalInCallFailNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 12),
    _SonusTrunkGroupIntervalInCallFailNoRoutes_Type()
)
sonusTrunkGroupIntervalInCallFailNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalInCallFailNoRoutes.setStatus("current")
_SonusTrunkGroupIntervalInCallFailNoResources_Type = PerfIntervalCount
_SonusTrunkGroupIntervalInCallFailNoResources_Object = MibTableColumn
sonusTrunkGroupIntervalInCallFailNoResources = _SonusTrunkGroupIntervalInCallFailNoResources_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 13),
    _SonusTrunkGroupIntervalInCallFailNoResources_Type()
)
sonusTrunkGroupIntervalInCallFailNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalInCallFailNoResources.setStatus("current")
_SonusTrunkGroupIntervalInCallFailNoService_Type = PerfIntervalCount
_SonusTrunkGroupIntervalInCallFailNoService_Object = MibTableColumn
sonusTrunkGroupIntervalInCallFailNoService = _SonusTrunkGroupIntervalInCallFailNoService_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 14),
    _SonusTrunkGroupIntervalInCallFailNoService_Type()
)
sonusTrunkGroupIntervalInCallFailNoService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalInCallFailNoService.setStatus("current")
_SonusTrunkGroupIntervalInCallFailInvalidCall_Type = PerfIntervalCount
_SonusTrunkGroupIntervalInCallFailInvalidCall_Object = MibTableColumn
sonusTrunkGroupIntervalInCallFailInvalidCall = _SonusTrunkGroupIntervalInCallFailInvalidCall_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 15),
    _SonusTrunkGroupIntervalInCallFailInvalidCall_Type()
)
sonusTrunkGroupIntervalInCallFailInvalidCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalInCallFailInvalidCall.setStatus("current")
_SonusTrunkGroupIntervalInCallFailNetworkFailure_Type = PerfIntervalCount
_SonusTrunkGroupIntervalInCallFailNetworkFailure_Object = MibTableColumn
sonusTrunkGroupIntervalInCallFailNetworkFailure = _SonusTrunkGroupIntervalInCallFailNetworkFailure_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 16),
    _SonusTrunkGroupIntervalInCallFailNetworkFailure_Type()
)
sonusTrunkGroupIntervalInCallFailNetworkFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalInCallFailNetworkFailure.setStatus("current")
_SonusTrunkGroupIntervalInCallFailProtocolError_Type = PerfIntervalCount
_SonusTrunkGroupIntervalInCallFailProtocolError_Object = MibTableColumn
sonusTrunkGroupIntervalInCallFailProtocolError = _SonusTrunkGroupIntervalInCallFailProtocolError_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 17),
    _SonusTrunkGroupIntervalInCallFailProtocolError_Type()
)
sonusTrunkGroupIntervalInCallFailProtocolError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalInCallFailProtocolError.setStatus("current")
_SonusTrunkGroupIntervalInCallFailUnspecified_Type = PerfIntervalCount
_SonusTrunkGroupIntervalInCallFailUnspecified_Object = MibTableColumn
sonusTrunkGroupIntervalInCallFailUnspecified = _SonusTrunkGroupIntervalInCallFailUnspecified_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 18),
    _SonusTrunkGroupIntervalInCallFailUnspecified_Type()
)
sonusTrunkGroupIntervalInCallFailUnspecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalInCallFailUnspecified.setStatus("current")
_SonusTrunkGroupIntervalOutCallFailNoRoutes_Type = PerfIntervalCount
_SonusTrunkGroupIntervalOutCallFailNoRoutes_Object = MibTableColumn
sonusTrunkGroupIntervalOutCallFailNoRoutes = _SonusTrunkGroupIntervalOutCallFailNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 19),
    _SonusTrunkGroupIntervalOutCallFailNoRoutes_Type()
)
sonusTrunkGroupIntervalOutCallFailNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalOutCallFailNoRoutes.setStatus("current")
_SonusTrunkGroupIntervalOutCallFailNoResources_Type = PerfIntervalCount
_SonusTrunkGroupIntervalOutCallFailNoResources_Object = MibTableColumn
sonusTrunkGroupIntervalOutCallFailNoResources = _SonusTrunkGroupIntervalOutCallFailNoResources_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 20),
    _SonusTrunkGroupIntervalOutCallFailNoResources_Type()
)
sonusTrunkGroupIntervalOutCallFailNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalOutCallFailNoResources.setStatus("current")
_SonusTrunkGroupIntervalOutCallFailNoService_Type = PerfIntervalCount
_SonusTrunkGroupIntervalOutCallFailNoService_Object = MibTableColumn
sonusTrunkGroupIntervalOutCallFailNoService = _SonusTrunkGroupIntervalOutCallFailNoService_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 21),
    _SonusTrunkGroupIntervalOutCallFailNoService_Type()
)
sonusTrunkGroupIntervalOutCallFailNoService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalOutCallFailNoService.setStatus("current")
_SonusTrunkGroupIntervalOutCallFailInvalidCall_Type = PerfIntervalCount
_SonusTrunkGroupIntervalOutCallFailInvalidCall_Object = MibTableColumn
sonusTrunkGroupIntervalOutCallFailInvalidCall = _SonusTrunkGroupIntervalOutCallFailInvalidCall_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 22),
    _SonusTrunkGroupIntervalOutCallFailInvalidCall_Type()
)
sonusTrunkGroupIntervalOutCallFailInvalidCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalOutCallFailInvalidCall.setStatus("current")
_SonusTrunkGroupIntervalOutCallFailNetworkFailure_Type = PerfIntervalCount
_SonusTrunkGroupIntervalOutCallFailNetworkFailure_Object = MibTableColumn
sonusTrunkGroupIntervalOutCallFailNetworkFailure = _SonusTrunkGroupIntervalOutCallFailNetworkFailure_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 23),
    _SonusTrunkGroupIntervalOutCallFailNetworkFailure_Type()
)
sonusTrunkGroupIntervalOutCallFailNetworkFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalOutCallFailNetworkFailure.setStatus("current")
_SonusTrunkGroupIntervalOutCallFailProtocolError_Type = PerfIntervalCount
_SonusTrunkGroupIntervalOutCallFailProtocolError_Object = MibTableColumn
sonusTrunkGroupIntervalOutCallFailProtocolError = _SonusTrunkGroupIntervalOutCallFailProtocolError_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 24),
    _SonusTrunkGroupIntervalOutCallFailProtocolError_Type()
)
sonusTrunkGroupIntervalOutCallFailProtocolError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalOutCallFailProtocolError.setStatus("current")
_SonusTrunkGroupIntervalOutCallFailUnspecified_Type = PerfIntervalCount
_SonusTrunkGroupIntervalOutCallFailUnspecified_Object = MibTableColumn
sonusTrunkGroupIntervalOutCallFailUnspecified = _SonusTrunkGroupIntervalOutCallFailUnspecified_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 25),
    _SonusTrunkGroupIntervalOutCallFailUnspecified_Type()
)
sonusTrunkGroupIntervalOutCallFailUnspecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalOutCallFailUnspecified.setStatus("current")
_SonusTrunkGroupIntervalTime_Type = TimeTicks
_SonusTrunkGroupIntervalTime_Object = MibTableColumn
sonusTrunkGroupIntervalTime = _SonusTrunkGroupIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 26),
    _SonusTrunkGroupIntervalTime_Type()
)
sonusTrunkGroupIntervalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalTime.setStatus("current")
_SonusTrunkGroupIntervalValidData_Type = TruthValue
_SonusTrunkGroupIntervalValidData_Object = MibTableColumn
sonusTrunkGroupIntervalValidData = _SonusTrunkGroupIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 6, 1, 1, 4, 1, 27),
    _SonusTrunkGroupIntervalValidData_Type()
)
sonusTrunkGroupIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTrunkGroupIntervalValidData.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-PERFORMANCE-STATISTICS-MIB",
    **{"sonusPerformanceStatisticsMIB": sonusPerformanceStatisticsMIB,
       "sonusPerformanceStatisticsObjects": sonusPerformanceStatisticsObjects,
       "sonusTrunkGroup": sonusTrunkGroup,
       "sonusTrunkGroupIntervalSize": sonusTrunkGroupIntervalSize,
       "sonusTrunkGroupNumberOfIntervals": sonusTrunkGroupNumberOfIntervals,
       "sonusTrunkGroupCurrentTable": sonusTrunkGroupCurrentTable,
       "sonusTrunkGroupCurrentEntry": sonusTrunkGroupCurrentEntry,
       "sonusTrunkGroupCurrentIndex": sonusTrunkGroupCurrentIndex,
       "sonusTrunkGroupCurrentInUsage": sonusTrunkGroupCurrentInUsage,
       "sonusTrunkGroupCurrentOutUsage": sonusTrunkGroupCurrentOutUsage,
       "sonusTrunkGroupCurrentInCalls": sonusTrunkGroupCurrentInCalls,
       "sonusTrunkGroupCurrentOutCalls": sonusTrunkGroupCurrentOutCalls,
       "sonusTrunkGroupCurrentInCallAttempts": sonusTrunkGroupCurrentInCallAttempts,
       "sonusTrunkGroupCurrentOutCallAttempts": sonusTrunkGroupCurrentOutCallAttempts,
       "sonusTrunkGroupCurrentMaxCompletedCalls": sonusTrunkGroupCurrentMaxCompletedCalls,
       "sonusTrunkGroupCurrentCallSetupTime": sonusTrunkGroupCurrentCallSetupTime,
       "sonusTrunkGroupCurrentCallSetups": sonusTrunkGroupCurrentCallSetups,
       "sonusTrunkGroupCurrentInCallFailNoRoutes": sonusTrunkGroupCurrentInCallFailNoRoutes,
       "sonusTrunkGroupCurrentInCallFailNoResources": sonusTrunkGroupCurrentInCallFailNoResources,
       "sonusTrunkGroupCurrentInCallFailNoService": sonusTrunkGroupCurrentInCallFailNoService,
       "sonusTrunkGroupCurrentInCallFailInvalidCall": sonusTrunkGroupCurrentInCallFailInvalidCall,
       "sonusTrunkGroupCurrentInCallFailNetworkFailure": sonusTrunkGroupCurrentInCallFailNetworkFailure,
       "sonusTrunkGroupCurrentInCallFailProtocolError": sonusTrunkGroupCurrentInCallFailProtocolError,
       "sonusTrunkGroupCurrentInCallFailUnspecified": sonusTrunkGroupCurrentInCallFailUnspecified,
       "sonusTrunkGroupCurrentOutCallFailNoRoutes": sonusTrunkGroupCurrentOutCallFailNoRoutes,
       "sonusTrunkGroupCurrentOutCallFailNoResources": sonusTrunkGroupCurrentOutCallFailNoResources,
       "sonusTrunkGroupCurrentOutCallFailNoService": sonusTrunkGroupCurrentOutCallFailNoService,
       "sonusTrunkGroupCurrentOutCallFailInvalidCall": sonusTrunkGroupCurrentOutCallFailInvalidCall,
       "sonusTrunkGroupCurrentOutCallFailNetworkFailure": sonusTrunkGroupCurrentOutCallFailNetworkFailure,
       "sonusTrunkGroupCurrentOutCallFailProtocolError": sonusTrunkGroupCurrentOutCallFailProtocolError,
       "sonusTrunkGroupCurrentOutCallFailUnspecified": sonusTrunkGroupCurrentOutCallFailUnspecified,
       "sonusTrunkGroupIntervalTable": sonusTrunkGroupIntervalTable,
       "sonusTrunkGroupIntervalEntry": sonusTrunkGroupIntervalEntry,
       "sonusTrunkGroupIntervalIndex": sonusTrunkGroupIntervalIndex,
       "sonusTrunkGroupIntervalNumber": sonusTrunkGroupIntervalNumber,
       "sonusTrunkGroupIntervalInUsage": sonusTrunkGroupIntervalInUsage,
       "sonusTrunkGroupIntervalOutUsage": sonusTrunkGroupIntervalOutUsage,
       "sonusTrunkGroupIntervalInCalls": sonusTrunkGroupIntervalInCalls,
       "sonusTrunkGroupIntervalOutCalls": sonusTrunkGroupIntervalOutCalls,
       "sonusTrunkGroupIntervalInCallAttempts": sonusTrunkGroupIntervalInCallAttempts,
       "sonusTrunkGroupIntervalOutCallAttempts": sonusTrunkGroupIntervalOutCallAttempts,
       "sonusTrunkGroupIntervalMaxCompletedCalls": sonusTrunkGroupIntervalMaxCompletedCalls,
       "sonusTrunkGroupIntervalCallSetupTime": sonusTrunkGroupIntervalCallSetupTime,
       "sonusTrunkGroupIntervalCallSetups": sonusTrunkGroupIntervalCallSetups,
       "sonusTrunkGroupIntervalInCallFailNoRoutes": sonusTrunkGroupIntervalInCallFailNoRoutes,
       "sonusTrunkGroupIntervalInCallFailNoResources": sonusTrunkGroupIntervalInCallFailNoResources,
       "sonusTrunkGroupIntervalInCallFailNoService": sonusTrunkGroupIntervalInCallFailNoService,
       "sonusTrunkGroupIntervalInCallFailInvalidCall": sonusTrunkGroupIntervalInCallFailInvalidCall,
       "sonusTrunkGroupIntervalInCallFailNetworkFailure": sonusTrunkGroupIntervalInCallFailNetworkFailure,
       "sonusTrunkGroupIntervalInCallFailProtocolError": sonusTrunkGroupIntervalInCallFailProtocolError,
       "sonusTrunkGroupIntervalInCallFailUnspecified": sonusTrunkGroupIntervalInCallFailUnspecified,
       "sonusTrunkGroupIntervalOutCallFailNoRoutes": sonusTrunkGroupIntervalOutCallFailNoRoutes,
       "sonusTrunkGroupIntervalOutCallFailNoResources": sonusTrunkGroupIntervalOutCallFailNoResources,
       "sonusTrunkGroupIntervalOutCallFailNoService": sonusTrunkGroupIntervalOutCallFailNoService,
       "sonusTrunkGroupIntervalOutCallFailInvalidCall": sonusTrunkGroupIntervalOutCallFailInvalidCall,
       "sonusTrunkGroupIntervalOutCallFailNetworkFailure": sonusTrunkGroupIntervalOutCallFailNetworkFailure,
       "sonusTrunkGroupIntervalOutCallFailProtocolError": sonusTrunkGroupIntervalOutCallFailProtocolError,
       "sonusTrunkGroupIntervalOutCallFailUnspecified": sonusTrunkGroupIntervalOutCallFailUnspecified,
       "sonusTrunkGroupIntervalTime": sonusTrunkGroupIntervalTime,
       "sonusTrunkGroupIntervalValidData": sonusTrunkGroupIntervalValidData}
)
