# SNMP MIB module (IANA-IPPM-METRICS-REGISTRY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IANA-IPPM-METRICS-REGISTRY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:02 2024
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

ianaIppmMetricsRegistry = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 128)
)
ianaIppmMetricsRegistry.setRevisions(
        ("2015-08-14 00:00",
         "2014-05-22 00:00",
         "2010-09-07 00:00",
         "2009-09-02 00:00",
         "2009-04-20 00:00",
         "2006-12-04 00:00",
         "2005-04-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IanaIppmMetrics_ObjectIdentity = ObjectIdentity
ianaIppmMetrics = _IanaIppmMetrics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1)
)
if mibBuilder.loadTexts:
    ianaIppmMetrics.setStatus("current")
_IetfInstantUnidirConnectivity_ObjectIdentity = ObjectIdentity
ietfInstantUnidirConnectivity = _IetfInstantUnidirConnectivity_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 1)
)
if mibBuilder.loadTexts:
    ietfInstantUnidirConnectivity.setStatus("current")
_IetfInstantBidirConnectivity_ObjectIdentity = ObjectIdentity
ietfInstantBidirConnectivity = _IetfInstantBidirConnectivity_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 2)
)
if mibBuilder.loadTexts:
    ietfInstantBidirConnectivity.setStatus("current")
_IetfIntervalUnidirConnectivity_ObjectIdentity = ObjectIdentity
ietfIntervalUnidirConnectivity = _IetfIntervalUnidirConnectivity_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 3)
)
if mibBuilder.loadTexts:
    ietfIntervalUnidirConnectivity.setStatus("current")
_IetfIntervalBidirConnectivity_ObjectIdentity = ObjectIdentity
ietfIntervalBidirConnectivity = _IetfIntervalBidirConnectivity_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 4)
)
if mibBuilder.loadTexts:
    ietfIntervalBidirConnectivity.setStatus("current")
_IetfIntervalTemporalConnectivity_ObjectIdentity = ObjectIdentity
ietfIntervalTemporalConnectivity = _IetfIntervalTemporalConnectivity_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 5)
)
if mibBuilder.loadTexts:
    ietfIntervalTemporalConnectivity.setStatus("current")
_IetfOneWayDelay_ObjectIdentity = ObjectIdentity
ietfOneWayDelay = _IetfOneWayDelay_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 6)
)
if mibBuilder.loadTexts:
    ietfOneWayDelay.setStatus("current")
_IetfOneWayDelayPoissonStream_ObjectIdentity = ObjectIdentity
ietfOneWayDelayPoissonStream = _IetfOneWayDelayPoissonStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 7)
)
if mibBuilder.loadTexts:
    ietfOneWayDelayPoissonStream.setStatus("current")
_IetfOneWayDelayPercentile_ObjectIdentity = ObjectIdentity
ietfOneWayDelayPercentile = _IetfOneWayDelayPercentile_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 8)
)
if mibBuilder.loadTexts:
    ietfOneWayDelayPercentile.setStatus("current")
_IetfOneWayDelayMedian_ObjectIdentity = ObjectIdentity
ietfOneWayDelayMedian = _IetfOneWayDelayMedian_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 9)
)
if mibBuilder.loadTexts:
    ietfOneWayDelayMedian.setStatus("current")
_IetfOneWayDelayMinimum_ObjectIdentity = ObjectIdentity
ietfOneWayDelayMinimum = _IetfOneWayDelayMinimum_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 10)
)
if mibBuilder.loadTexts:
    ietfOneWayDelayMinimum.setStatus("current")
_IetfOneWayDelayInversePercentile_ObjectIdentity = ObjectIdentity
ietfOneWayDelayInversePercentile = _IetfOneWayDelayInversePercentile_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 11)
)
if mibBuilder.loadTexts:
    ietfOneWayDelayInversePercentile.setStatus("current")
_IetfOneWayPktLoss_ObjectIdentity = ObjectIdentity
ietfOneWayPktLoss = _IetfOneWayPktLoss_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 12)
)
if mibBuilder.loadTexts:
    ietfOneWayPktLoss.setStatus("current")
_IetfOneWayPktLossPoissonStream_ObjectIdentity = ObjectIdentity
ietfOneWayPktLossPoissonStream = _IetfOneWayPktLossPoissonStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 13)
)
if mibBuilder.loadTexts:
    ietfOneWayPktLossPoissonStream.setStatus("current")
_IetfOneWayPktLossAverage_ObjectIdentity = ObjectIdentity
ietfOneWayPktLossAverage = _IetfOneWayPktLossAverage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 14)
)
if mibBuilder.loadTexts:
    ietfOneWayPktLossAverage.setStatus("current")
_IetfRoundTripDelay_ObjectIdentity = ObjectIdentity
ietfRoundTripDelay = _IetfRoundTripDelay_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 15)
)
if mibBuilder.loadTexts:
    ietfRoundTripDelay.setStatus("current")
_IetfRoundTripDelayPoissonStream_ObjectIdentity = ObjectIdentity
ietfRoundTripDelayPoissonStream = _IetfRoundTripDelayPoissonStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 16)
)
if mibBuilder.loadTexts:
    ietfRoundTripDelayPoissonStream.setStatus("current")
_IetfRoundTripDelayPercentile_ObjectIdentity = ObjectIdentity
ietfRoundTripDelayPercentile = _IetfRoundTripDelayPercentile_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 17)
)
if mibBuilder.loadTexts:
    ietfRoundTripDelayPercentile.setStatus("current")
_IetfRoundTripDelayMedian_ObjectIdentity = ObjectIdentity
ietfRoundTripDelayMedian = _IetfRoundTripDelayMedian_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 18)
)
if mibBuilder.loadTexts:
    ietfRoundTripDelayMedian.setStatus("current")
_IetfRoundTripDelayMinimum_ObjectIdentity = ObjectIdentity
ietfRoundTripDelayMinimum = _IetfRoundTripDelayMinimum_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 19)
)
if mibBuilder.loadTexts:
    ietfRoundTripDelayMinimum.setStatus("current")
_IetfRoundTripDelayInvPercentile_ObjectIdentity = ObjectIdentity
ietfRoundTripDelayInvPercentile = _IetfRoundTripDelayInvPercentile_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 20)
)
if mibBuilder.loadTexts:
    ietfRoundTripDelayInvPercentile.setStatus("current")
_IetfOneWayLossDistanceStream_ObjectIdentity = ObjectIdentity
ietfOneWayLossDistanceStream = _IetfOneWayLossDistanceStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 21)
)
if mibBuilder.loadTexts:
    ietfOneWayLossDistanceStream.setStatus("current")
_IetfOneWayLossPeriodStream_ObjectIdentity = ObjectIdentity
ietfOneWayLossPeriodStream = _IetfOneWayLossPeriodStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 22)
)
if mibBuilder.loadTexts:
    ietfOneWayLossPeriodStream.setStatus("current")
_IetfOneWayLossNoticeableRate_ObjectIdentity = ObjectIdentity
ietfOneWayLossNoticeableRate = _IetfOneWayLossNoticeableRate_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 23)
)
if mibBuilder.loadTexts:
    ietfOneWayLossNoticeableRate.setStatus("current")
_IetfOneWayLossPeriodTotal_ObjectIdentity = ObjectIdentity
ietfOneWayLossPeriodTotal = _IetfOneWayLossPeriodTotal_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 24)
)
if mibBuilder.loadTexts:
    ietfOneWayLossPeriodTotal.setStatus("current")
_IetfOneWayLossPeriodLengths_ObjectIdentity = ObjectIdentity
ietfOneWayLossPeriodLengths = _IetfOneWayLossPeriodLengths_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 25)
)
if mibBuilder.loadTexts:
    ietfOneWayLossPeriodLengths.setStatus("current")
_IetfOneWayInterLossPeriodLengths_ObjectIdentity = ObjectIdentity
ietfOneWayInterLossPeriodLengths = _IetfOneWayInterLossPeriodLengths_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 26)
)
if mibBuilder.loadTexts:
    ietfOneWayInterLossPeriodLengths.setStatus("current")
_IetfOneWayIpdv_ObjectIdentity = ObjectIdentity
ietfOneWayIpdv = _IetfOneWayIpdv_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 27)
)
if mibBuilder.loadTexts:
    ietfOneWayIpdv.setStatus("current")
_IetfOneWayIpdvPoissonStream_ObjectIdentity = ObjectIdentity
ietfOneWayIpdvPoissonStream = _IetfOneWayIpdvPoissonStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 28)
)
if mibBuilder.loadTexts:
    ietfOneWayIpdvPoissonStream.setStatus("current")
_IetfOneWayIpdvPercentile_ObjectIdentity = ObjectIdentity
ietfOneWayIpdvPercentile = _IetfOneWayIpdvPercentile_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 29)
)
if mibBuilder.loadTexts:
    ietfOneWayIpdvPercentile.setStatus("current")
_IetfOneWayIpdvInversePercentile_ObjectIdentity = ObjectIdentity
ietfOneWayIpdvInversePercentile = _IetfOneWayIpdvInversePercentile_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 30)
)
if mibBuilder.loadTexts:
    ietfOneWayIpdvInversePercentile.setStatus("current")
_IetfOneWayIpdvJitter_ObjectIdentity = ObjectIdentity
ietfOneWayIpdvJitter = _IetfOneWayIpdvJitter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 31)
)
if mibBuilder.loadTexts:
    ietfOneWayIpdvJitter.setStatus("current")
_IetfOneWayPeakToPeakIpdv_ObjectIdentity = ObjectIdentity
ietfOneWayPeakToPeakIpdv = _IetfOneWayPeakToPeakIpdv_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 32)
)
if mibBuilder.loadTexts:
    ietfOneWayPeakToPeakIpdv.setStatus("current")
_IetfOneWayDelayPeriodicStream_ObjectIdentity = ObjectIdentity
ietfOneWayDelayPeriodicStream = _IetfOneWayDelayPeriodicStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 33)
)
if mibBuilder.loadTexts:
    ietfOneWayDelayPeriodicStream.setStatus("current")
_IetfReorderedSingleton_ObjectIdentity = ObjectIdentity
ietfReorderedSingleton = _IetfReorderedSingleton_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 34)
)
if mibBuilder.loadTexts:
    ietfReorderedSingleton.setStatus("current")
_IetfReorderedPacketRatio_ObjectIdentity = ObjectIdentity
ietfReorderedPacketRatio = _IetfReorderedPacketRatio_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 35)
)
if mibBuilder.loadTexts:
    ietfReorderedPacketRatio.setStatus("current")
_IetfReorderingExtent_ObjectIdentity = ObjectIdentity
ietfReorderingExtent = _IetfReorderingExtent_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 36)
)
if mibBuilder.loadTexts:
    ietfReorderingExtent.setStatus("current")
_IetfReorderingLateTimeOffset_ObjectIdentity = ObjectIdentity
ietfReorderingLateTimeOffset = _IetfReorderingLateTimeOffset_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 37)
)
if mibBuilder.loadTexts:
    ietfReorderingLateTimeOffset.setStatus("current")
_IetfReorderingByteOffset_ObjectIdentity = ObjectIdentity
ietfReorderingByteOffset = _IetfReorderingByteOffset_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 38)
)
if mibBuilder.loadTexts:
    ietfReorderingByteOffset.setStatus("current")
_IetfReorderingGap_ObjectIdentity = ObjectIdentity
ietfReorderingGap = _IetfReorderingGap_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 39)
)
if mibBuilder.loadTexts:
    ietfReorderingGap.setStatus("current")
_IetfReorderingGapTime_ObjectIdentity = ObjectIdentity
ietfReorderingGapTime = _IetfReorderingGapTime_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 40)
)
if mibBuilder.loadTexts:
    ietfReorderingGapTime.setStatus("current")
_IetfReorderingFreeRunx_ObjectIdentity = ObjectIdentity
ietfReorderingFreeRunx = _IetfReorderingFreeRunx_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 41)
)
if mibBuilder.loadTexts:
    ietfReorderingFreeRunx.setStatus("current")
_IetfReorderingFreeRunq_ObjectIdentity = ObjectIdentity
ietfReorderingFreeRunq = _IetfReorderingFreeRunq_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 42)
)
if mibBuilder.loadTexts:
    ietfReorderingFreeRunq.setStatus("current")
_IetfReorderingFreeRunp_ObjectIdentity = ObjectIdentity
ietfReorderingFreeRunp = _IetfReorderingFreeRunp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 43)
)
if mibBuilder.loadTexts:
    ietfReorderingFreeRunp.setStatus("current")
_IetfReorderingFreeRuna_ObjectIdentity = ObjectIdentity
ietfReorderingFreeRuna = _IetfReorderingFreeRuna_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 44)
)
if mibBuilder.loadTexts:
    ietfReorderingFreeRuna.setStatus("current")
_IetfnReordering_ObjectIdentity = ObjectIdentity
ietfnReordering = _IetfnReordering_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 45)
)
if mibBuilder.loadTexts:
    ietfnReordering.setStatus("current")
_IetfOneWayPacketArrivalCount_ObjectIdentity = ObjectIdentity
ietfOneWayPacketArrivalCount = _IetfOneWayPacketArrivalCount_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 46)
)
if mibBuilder.loadTexts:
    ietfOneWayPacketArrivalCount.setStatus("current")
_IetfOneWayPacketDuplication_ObjectIdentity = ObjectIdentity
ietfOneWayPacketDuplication = _IetfOneWayPacketDuplication_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 47)
)
if mibBuilder.loadTexts:
    ietfOneWayPacketDuplication.setStatus("current")
_IetfOneWayPacketDuplicationPoissonStream_ObjectIdentity = ObjectIdentity
ietfOneWayPacketDuplicationPoissonStream = _IetfOneWayPacketDuplicationPoissonStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 48)
)
if mibBuilder.loadTexts:
    ietfOneWayPacketDuplicationPoissonStream.setStatus("current")
_IetfOneWayPacketDuplicationPeriodicStream_ObjectIdentity = ObjectIdentity
ietfOneWayPacketDuplicationPeriodicStream = _IetfOneWayPacketDuplicationPeriodicStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 49)
)
if mibBuilder.loadTexts:
    ietfOneWayPacketDuplicationPeriodicStream.setStatus("current")
_IetfOneWayPacketDuplicationFraction_ObjectIdentity = ObjectIdentity
ietfOneWayPacketDuplicationFraction = _IetfOneWayPacketDuplicationFraction_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 50)
)
if mibBuilder.loadTexts:
    ietfOneWayPacketDuplicationFraction.setStatus("current")
_IetfOneWayReplicatedPacketRate_ObjectIdentity = ObjectIdentity
ietfOneWayReplicatedPacketRate = _IetfOneWayReplicatedPacketRate_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 51)
)
if mibBuilder.loadTexts:
    ietfOneWayReplicatedPacketRate.setStatus("current")
_IetfSpatialOneWayDelayVector_ObjectIdentity = ObjectIdentity
ietfSpatialOneWayDelayVector = _IetfSpatialOneWayDelayVector_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 52)
)
if mibBuilder.loadTexts:
    ietfSpatialOneWayDelayVector.setStatus("current")
_IetfSpatialPacketLossVector_ObjectIdentity = ObjectIdentity
ietfSpatialPacketLossVector = _IetfSpatialPacketLossVector_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 53)
)
if mibBuilder.loadTexts:
    ietfSpatialPacketLossVector.setStatus("current")
_IetfSpatialOneWayIpdvVector_ObjectIdentity = ObjectIdentity
ietfSpatialOneWayIpdvVector = _IetfSpatialOneWayIpdvVector_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 54)
)
if mibBuilder.loadTexts:
    ietfSpatialOneWayIpdvVector.setStatus("current")
_IetfSegmentOneWayDelayStream_ObjectIdentity = ObjectIdentity
ietfSegmentOneWayDelayStream = _IetfSegmentOneWayDelayStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 55)
)
if mibBuilder.loadTexts:
    ietfSegmentOneWayDelayStream.setStatus("current")
_IetfSegmentPacketLossStream_ObjectIdentity = ObjectIdentity
ietfSegmentPacketLossStream = _IetfSegmentPacketLossStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 56)
)
if mibBuilder.loadTexts:
    ietfSegmentPacketLossStream.setStatus("current")
_IetfSegmentIpdvPrevStream_ObjectIdentity = ObjectIdentity
ietfSegmentIpdvPrevStream = _IetfSegmentIpdvPrevStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 57)
)
if mibBuilder.loadTexts:
    ietfSegmentIpdvPrevStream.setStatus("current")
_IetfSegmentIpdvMinStream_ObjectIdentity = ObjectIdentity
ietfSegmentIpdvMinStream = _IetfSegmentIpdvMinStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 58)
)
if mibBuilder.loadTexts:
    ietfSegmentIpdvMinStream.setStatus("current")
_IetfOneToGroupDelayVector_ObjectIdentity = ObjectIdentity
ietfOneToGroupDelayVector = _IetfOneToGroupDelayVector_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 59)
)
if mibBuilder.loadTexts:
    ietfOneToGroupDelayVector.setStatus("current")
_IetfOneToGroupPacketLossVector_ObjectIdentity = ObjectIdentity
ietfOneToGroupPacketLossVector = _IetfOneToGroupPacketLossVector_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 60)
)
if mibBuilder.loadTexts:
    ietfOneToGroupPacketLossVector.setStatus("current")
_IetfOneToGroupIpdvVector_ObjectIdentity = ObjectIdentity
ietfOneToGroupIpdvVector = _IetfOneToGroupIpdvVector_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 61)
)
if mibBuilder.loadTexts:
    ietfOneToGroupIpdvVector.setStatus("current")
_IetfOnetoGroupReceiverNMeanDelay_ObjectIdentity = ObjectIdentity
ietfOnetoGroupReceiverNMeanDelay = _IetfOnetoGroupReceiverNMeanDelay_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 62)
)
if mibBuilder.loadTexts:
    ietfOnetoGroupReceiverNMeanDelay.setStatus("current")
_IetfOneToGroupMeanDelay_ObjectIdentity = ObjectIdentity
ietfOneToGroupMeanDelay = _IetfOneToGroupMeanDelay_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 63)
)
if mibBuilder.loadTexts:
    ietfOneToGroupMeanDelay.setStatus("current")
_IetfOneToGroupRangeMeanDelay_ObjectIdentity = ObjectIdentity
ietfOneToGroupRangeMeanDelay = _IetfOneToGroupRangeMeanDelay_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 64)
)
if mibBuilder.loadTexts:
    ietfOneToGroupRangeMeanDelay.setStatus("current")
_IetfOneToGroupMaxMeanDelay_ObjectIdentity = ObjectIdentity
ietfOneToGroupMaxMeanDelay = _IetfOneToGroupMaxMeanDelay_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 65)
)
if mibBuilder.loadTexts:
    ietfOneToGroupMaxMeanDelay.setStatus("current")
_IetfOneToGroupReceiverNLossRatio_ObjectIdentity = ObjectIdentity
ietfOneToGroupReceiverNLossRatio = _IetfOneToGroupReceiverNLossRatio_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 66)
)
if mibBuilder.loadTexts:
    ietfOneToGroupReceiverNLossRatio.setStatus("current")
_IetfOneToGroupReceiverNCompLossRatio_ObjectIdentity = ObjectIdentity
ietfOneToGroupReceiverNCompLossRatio = _IetfOneToGroupReceiverNCompLossRatio_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 67)
)
if mibBuilder.loadTexts:
    ietfOneToGroupReceiverNCompLossRatio.setStatus("current")
_IetfOneToGroupLossRatio_ObjectIdentity = ObjectIdentity
ietfOneToGroupLossRatio = _IetfOneToGroupLossRatio_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 68)
)
if mibBuilder.loadTexts:
    ietfOneToGroupLossRatio.setStatus("current")
_IetfOneToGroupRangeLossRatio_ObjectIdentity = ObjectIdentity
ietfOneToGroupRangeLossRatio = _IetfOneToGroupRangeLossRatio_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 69)
)
if mibBuilder.loadTexts:
    ietfOneToGroupRangeLossRatio.setStatus("current")
_IetfOneToGroupRangeDelayVariation_ObjectIdentity = ObjectIdentity
ietfOneToGroupRangeDelayVariation = _IetfOneToGroupRangeDelayVariation_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 70)
)
if mibBuilder.loadTexts:
    ietfOneToGroupRangeDelayVariation.setStatus("current")
_IetfFiniteOneWayDelayStream_ObjectIdentity = ObjectIdentity
ietfFiniteOneWayDelayStream = _IetfFiniteOneWayDelayStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 71)
)
if mibBuilder.loadTexts:
    ietfFiniteOneWayDelayStream.setStatus("current")
_IetfFiniteOneWayDelayMean_ObjectIdentity = ObjectIdentity
ietfFiniteOneWayDelayMean = _IetfFiniteOneWayDelayMean_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 72)
)
if mibBuilder.loadTexts:
    ietfFiniteOneWayDelayMean.setStatus("current")
_IetfCompositeOneWayDelayMean_ObjectIdentity = ObjectIdentity
ietfCompositeOneWayDelayMean = _IetfCompositeOneWayDelayMean_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 73)
)
if mibBuilder.loadTexts:
    ietfCompositeOneWayDelayMean.setStatus("current")
_IetfFiniteOneWayDelayMinimum_ObjectIdentity = ObjectIdentity
ietfFiniteOneWayDelayMinimum = _IetfFiniteOneWayDelayMinimum_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 74)
)
if mibBuilder.loadTexts:
    ietfFiniteOneWayDelayMinimum.setStatus("current")
_IetfCompositeOneWayDelayMinimum_ObjectIdentity = ObjectIdentity
ietfCompositeOneWayDelayMinimum = _IetfCompositeOneWayDelayMinimum_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 75)
)
if mibBuilder.loadTexts:
    ietfCompositeOneWayDelayMinimum.setStatus("current")
_IetfOneWayPktLossEmpiricProb_ObjectIdentity = ObjectIdentity
ietfOneWayPktLossEmpiricProb = _IetfOneWayPktLossEmpiricProb_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 76)
)
if mibBuilder.loadTexts:
    ietfOneWayPktLossEmpiricProb.setStatus("current")
_IetfCompositeOneWayPktLossEmpiricProb_ObjectIdentity = ObjectIdentity
ietfCompositeOneWayPktLossEmpiricProb = _IetfCompositeOneWayPktLossEmpiricProb_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 77)
)
if mibBuilder.loadTexts:
    ietfCompositeOneWayPktLossEmpiricProb.setStatus("current")
_IetfOneWayPdvRefminStream_ObjectIdentity = ObjectIdentity
ietfOneWayPdvRefminStream = _IetfOneWayPdvRefminStream_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 78)
)
if mibBuilder.loadTexts:
    ietfOneWayPdvRefminStream.setStatus("current")
_IetfOneWayPdvRefminMean_ObjectIdentity = ObjectIdentity
ietfOneWayPdvRefminMean = _IetfOneWayPdvRefminMean_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 79)
)
if mibBuilder.loadTexts:
    ietfOneWayPdvRefminMean.setStatus("current")
_IetfOneWayPdvRefminVariance_ObjectIdentity = ObjectIdentity
ietfOneWayPdvRefminVariance = _IetfOneWayPdvRefminVariance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 80)
)
if mibBuilder.loadTexts:
    ietfOneWayPdvRefminVariance.setStatus("current")
_IetfOneWayPdvRefminSkewness_ObjectIdentity = ObjectIdentity
ietfOneWayPdvRefminSkewness = _IetfOneWayPdvRefminSkewness_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 81)
)
if mibBuilder.loadTexts:
    ietfOneWayPdvRefminSkewness.setStatus("current")
_IetfCompositeOneWayPdvRefminQtil_ObjectIdentity = ObjectIdentity
ietfCompositeOneWayPdvRefminQtil = _IetfCompositeOneWayPdvRefminQtil_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 82)
)
if mibBuilder.loadTexts:
    ietfCompositeOneWayPdvRefminQtil.setStatus("current")
_IetfCompositeOneWayPdvRefminNPA_ObjectIdentity = ObjectIdentity
ietfCompositeOneWayPdvRefminNPA = _IetfCompositeOneWayPdvRefminNPA_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 128, 1, 83)
)
if mibBuilder.loadTexts:
    ietfCompositeOneWayPdvRefminNPA.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANA-IPPM-METRICS-REGISTRY-MIB",
    **{"ianaIppmMetricsRegistry": ianaIppmMetricsRegistry,
       "ianaIppmMetrics": ianaIppmMetrics,
       "ietfInstantUnidirConnectivity": ietfInstantUnidirConnectivity,
       "ietfInstantBidirConnectivity": ietfInstantBidirConnectivity,
       "ietfIntervalUnidirConnectivity": ietfIntervalUnidirConnectivity,
       "ietfIntervalBidirConnectivity": ietfIntervalBidirConnectivity,
       "ietfIntervalTemporalConnectivity": ietfIntervalTemporalConnectivity,
       "ietfOneWayDelay": ietfOneWayDelay,
       "ietfOneWayDelayPoissonStream": ietfOneWayDelayPoissonStream,
       "ietfOneWayDelayPercentile": ietfOneWayDelayPercentile,
       "ietfOneWayDelayMedian": ietfOneWayDelayMedian,
       "ietfOneWayDelayMinimum": ietfOneWayDelayMinimum,
       "ietfOneWayDelayInversePercentile": ietfOneWayDelayInversePercentile,
       "ietfOneWayPktLoss": ietfOneWayPktLoss,
       "ietfOneWayPktLossPoissonStream": ietfOneWayPktLossPoissonStream,
       "ietfOneWayPktLossAverage": ietfOneWayPktLossAverage,
       "ietfRoundTripDelay": ietfRoundTripDelay,
       "ietfRoundTripDelayPoissonStream": ietfRoundTripDelayPoissonStream,
       "ietfRoundTripDelayPercentile": ietfRoundTripDelayPercentile,
       "ietfRoundTripDelayMedian": ietfRoundTripDelayMedian,
       "ietfRoundTripDelayMinimum": ietfRoundTripDelayMinimum,
       "ietfRoundTripDelayInvPercentile": ietfRoundTripDelayInvPercentile,
       "ietfOneWayLossDistanceStream": ietfOneWayLossDistanceStream,
       "ietfOneWayLossPeriodStream": ietfOneWayLossPeriodStream,
       "ietfOneWayLossNoticeableRate": ietfOneWayLossNoticeableRate,
       "ietfOneWayLossPeriodTotal": ietfOneWayLossPeriodTotal,
       "ietfOneWayLossPeriodLengths": ietfOneWayLossPeriodLengths,
       "ietfOneWayInterLossPeriodLengths": ietfOneWayInterLossPeriodLengths,
       "ietfOneWayIpdv": ietfOneWayIpdv,
       "ietfOneWayIpdvPoissonStream": ietfOneWayIpdvPoissonStream,
       "ietfOneWayIpdvPercentile": ietfOneWayIpdvPercentile,
       "ietfOneWayIpdvInversePercentile": ietfOneWayIpdvInversePercentile,
       "ietfOneWayIpdvJitter": ietfOneWayIpdvJitter,
       "ietfOneWayPeakToPeakIpdv": ietfOneWayPeakToPeakIpdv,
       "ietfOneWayDelayPeriodicStream": ietfOneWayDelayPeriodicStream,
       "ietfReorderedSingleton": ietfReorderedSingleton,
       "ietfReorderedPacketRatio": ietfReorderedPacketRatio,
       "ietfReorderingExtent": ietfReorderingExtent,
       "ietfReorderingLateTimeOffset": ietfReorderingLateTimeOffset,
       "ietfReorderingByteOffset": ietfReorderingByteOffset,
       "ietfReorderingGap": ietfReorderingGap,
       "ietfReorderingGapTime": ietfReorderingGapTime,
       "ietfReorderingFreeRunx": ietfReorderingFreeRunx,
       "ietfReorderingFreeRunq": ietfReorderingFreeRunq,
       "ietfReorderingFreeRunp": ietfReorderingFreeRunp,
       "ietfReorderingFreeRuna": ietfReorderingFreeRuna,
       "ietfnReordering": ietfnReordering,
       "ietfOneWayPacketArrivalCount": ietfOneWayPacketArrivalCount,
       "ietfOneWayPacketDuplication": ietfOneWayPacketDuplication,
       "ietfOneWayPacketDuplicationPoissonStream": ietfOneWayPacketDuplicationPoissonStream,
       "ietfOneWayPacketDuplicationPeriodicStream": ietfOneWayPacketDuplicationPeriodicStream,
       "ietfOneWayPacketDuplicationFraction": ietfOneWayPacketDuplicationFraction,
       "ietfOneWayReplicatedPacketRate": ietfOneWayReplicatedPacketRate,
       "ietfSpatialOneWayDelayVector": ietfSpatialOneWayDelayVector,
       "ietfSpatialPacketLossVector": ietfSpatialPacketLossVector,
       "ietfSpatialOneWayIpdvVector": ietfSpatialOneWayIpdvVector,
       "ietfSegmentOneWayDelayStream": ietfSegmentOneWayDelayStream,
       "ietfSegmentPacketLossStream": ietfSegmentPacketLossStream,
       "ietfSegmentIpdvPrevStream": ietfSegmentIpdvPrevStream,
       "ietfSegmentIpdvMinStream": ietfSegmentIpdvMinStream,
       "ietfOneToGroupDelayVector": ietfOneToGroupDelayVector,
       "ietfOneToGroupPacketLossVector": ietfOneToGroupPacketLossVector,
       "ietfOneToGroupIpdvVector": ietfOneToGroupIpdvVector,
       "ietfOnetoGroupReceiverNMeanDelay": ietfOnetoGroupReceiverNMeanDelay,
       "ietfOneToGroupMeanDelay": ietfOneToGroupMeanDelay,
       "ietfOneToGroupRangeMeanDelay": ietfOneToGroupRangeMeanDelay,
       "ietfOneToGroupMaxMeanDelay": ietfOneToGroupMaxMeanDelay,
       "ietfOneToGroupReceiverNLossRatio": ietfOneToGroupReceiverNLossRatio,
       "ietfOneToGroupReceiverNCompLossRatio": ietfOneToGroupReceiverNCompLossRatio,
       "ietfOneToGroupLossRatio": ietfOneToGroupLossRatio,
       "ietfOneToGroupRangeLossRatio": ietfOneToGroupRangeLossRatio,
       "ietfOneToGroupRangeDelayVariation": ietfOneToGroupRangeDelayVariation,
       "ietfFiniteOneWayDelayStream": ietfFiniteOneWayDelayStream,
       "ietfFiniteOneWayDelayMean": ietfFiniteOneWayDelayMean,
       "ietfCompositeOneWayDelayMean": ietfCompositeOneWayDelayMean,
       "ietfFiniteOneWayDelayMinimum": ietfFiniteOneWayDelayMinimum,
       "ietfCompositeOneWayDelayMinimum": ietfCompositeOneWayDelayMinimum,
       "ietfOneWayPktLossEmpiricProb": ietfOneWayPktLossEmpiricProb,
       "ietfCompositeOneWayPktLossEmpiricProb": ietfCompositeOneWayPktLossEmpiricProb,
       "ietfOneWayPdvRefminStream": ietfOneWayPdvRefminStream,
       "ietfOneWayPdvRefminMean": ietfOneWayPdvRefminMean,
       "ietfOneWayPdvRefminVariance": ietfOneWayPdvRefminVariance,
       "ietfOneWayPdvRefminSkewness": ietfOneWayPdvRefminSkewness,
       "ietfCompositeOneWayPdvRefminQtil": ietfCompositeOneWayPdvRefminQtil,
       "ietfCompositeOneWayPdvRefminNPA": ietfCompositeOneWayPdvRefminNPA}
)
