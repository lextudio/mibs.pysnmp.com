# SNMP MIB module (ENTERASYS-SERVICE-LEVEL-REPORTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-SERVICE-LEVEL-REPORTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:33 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

etsysServiceLevelReportingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39)
)
etsysServiceLevelReportingMIB.setRevisions(
        ("2003-11-06 15:15",
         "2003-10-24 19:02",
         "2003-10-22 23:32")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EtsysSrvcLvlOwnerString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TimeUnit(Integer32, TextualConvention):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("day", 4),
          ("hour", 5),
          ("microsecond", 8),
          ("millisecond", 7),
          ("month", 2),
          ("nanosecond", 9),
          ("second", 6),
          ("week", 3),
          ("year", 1))
    )



class EtsysSrvcLvlStandardMetrics(Bits, TextualConvention):
    status = "current"


class GMTTimeStamp(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class TypeP(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )



class TypePaddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )



# MIB Managed Objects in the order of their OIDs

_EtsysSrvcLvlConfigObjects_ObjectIdentity = ObjectIdentity
etsysSrvcLvlConfigObjects = _EtsysSrvcLvlConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1)
)
_EtsysSrvcLvlSystem_ObjectIdentity = ObjectIdentity
etsysSrvcLvlSystem = _EtsysSrvcLvlSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 1)
)
_EtsysSrvcLvlSystemTime_Type = GMTTimeStamp
_EtsysSrvcLvlSystemTime_Object = MibScalar
etsysSrvcLvlSystemTime = _EtsysSrvcLvlSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 1, 1),
    _EtsysSrvcLvlSystemTime_Type()
)
etsysSrvcLvlSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSrvcLvlSystemTime.setStatus("current")
_EtsysSrvcLvlSystemClockResolution_Type = Integer32
_EtsysSrvcLvlSystemClockResolution_Object = MibScalar
etsysSrvcLvlSystemClockResolution = _EtsysSrvcLvlSystemClockResolution_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 1, 2),
    _EtsysSrvcLvlSystemClockResolution_Type()
)
etsysSrvcLvlSystemClockResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSrvcLvlSystemClockResolution.setStatus("current")
if mibBuilder.loadTexts:
    etsysSrvcLvlSystemClockResolution.setUnits("picoseconds")
_EtsysSrvcLvlMetricTable_Object = MibTable
etsysSrvcLvlMetricTable = _EtsysSrvcLvlMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 1, 3)
)
if mibBuilder.loadTexts:
    etsysSrvcLvlMetricTable.setStatus("current")
_EtsysSrvcLvlMetricEntry_Object = MibTableRow
etsysSrvcLvlMetricEntry = _EtsysSrvcLvlMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 1, 3, 1)
)
etsysSrvcLvlMetricEntry.setIndexNames(
    (0, "ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlMetricIndex"),
)
if mibBuilder.loadTexts:
    etsysSrvcLvlMetricEntry.setStatus("current")


class _EtsysSrvcLvlMetricIndex_Type(Integer32):
    """Custom type etsysSrvcLvlMetricIndex based on Integer32"""
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
              15,
              16,
              17,
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
              37)
        )
    )
    namedValues = NamedValues(
        *(("instantBidirectionConnectivity", 2),
          ("instantUnidirectionConnectivity", 1),
          ("intervalBidirectionConnectivity", 4),
          ("intervalTemporalConnectivity", 5),
          ("intervalUnidirectionConnectivity", 3),
          ("oneWayDelay", 6),
          ("oneWayDelayInversePercentile", 11),
          ("oneWayDelayMedian", 9),
          ("oneWayDelayMinimum", 10),
          ("oneWayDelayPercentile", 8),
          ("oneWayDelayPeriodicStream", 33),
          ("oneWayDelayPoissonStream", 7),
          ("oneWayInterLossPeriodLengths", 26),
          ("oneWayIpdv", 27),
          ("oneWayIpdvInversePercentile", 30),
          ("oneWayIpdvJitter", 31),
          ("oneWayIpdvPercentile", 29),
          ("oneWayIpdvPoissonStream", 28),
          ("oneWayLossDistanceStream", 21),
          ("oneWayLossNoticeableRate", 23),
          ("oneWayLossPeriodLengths", 25),
          ("oneWayLossPeriodStream", 22),
          ("oneWayLossPeriodTotal", 24),
          ("oneWayPacketLoss", 12),
          ("oneWayPacketLossAverage", 14),
          ("oneWayPacketLossPoissonStream", 13),
          ("oneWayPeakToPeakIpdv", 32),
          ("roundtripDelay", 15),
          ("roundtripDelayAverage", 34),
          ("roundtripDelayInversePercentile", 20),
          ("roundtripDelayMedian", 18),
          ("roundtripDelayMinimum", 19),
          ("roundtripDelayPercentile", 17),
          ("roundtripDelayPoissonStream", 16),
          ("roundtripIpdv", 37),
          ("roundtripPacketLoss", 35),
          ("roundtripPacketLossAverage", 36))
    )


_EtsysSrvcLvlMetricIndex_Type.__name__ = "Integer32"
_EtsysSrvcLvlMetricIndex_Object = MibTableColumn
etsysSrvcLvlMetricIndex = _EtsysSrvcLvlMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 1, 3, 1, 1),
    _EtsysSrvcLvlMetricIndex_Type()
)
etsysSrvcLvlMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysSrvcLvlMetricIndex.setStatus("current")


class _EtsysSrvcLvlMetricCapabilities_Type(Integer32):
    """Custom type etsysSrvcLvlMetricCapabilities based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("implemented", 1),
          ("notImplemented", 0))
    )


_EtsysSrvcLvlMetricCapabilities_Type.__name__ = "Integer32"
_EtsysSrvcLvlMetricCapabilities_Object = MibTableColumn
etsysSrvcLvlMetricCapabilities = _EtsysSrvcLvlMetricCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 1, 3, 1, 2),
    _EtsysSrvcLvlMetricCapabilities_Type()
)
etsysSrvcLvlMetricCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSrvcLvlMetricCapabilities.setStatus("current")


class _EtsysSrvcLvlMetricType_Type(Integer32):
    """Custom type etsysSrvcLvlMetricType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aggregated", 1),
          ("network", 0))
    )


_EtsysSrvcLvlMetricType_Type.__name__ = "Integer32"
_EtsysSrvcLvlMetricType_Object = MibTableColumn
etsysSrvcLvlMetricType = _EtsysSrvcLvlMetricType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 1, 3, 1, 3),
    _EtsysSrvcLvlMetricType_Type()
)
etsysSrvcLvlMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSrvcLvlMetricType.setStatus("current")


class _EtsysSrvcLvlMetricUnit_Type(Integer32):
    """Custom type etsysSrvcLvlMetricUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("byte", 7),
          ("kilobyte", 8),
          ("megabyte", 9),
          ("microsecond", 3),
          ("millisecond", 2),
          ("nanosecond", 4),
          ("noUnit", 0),
          ("packet", 6),
          ("percentage", 5),
          ("second", 1))
    )


_EtsysSrvcLvlMetricUnit_Type.__name__ = "Integer32"
_EtsysSrvcLvlMetricUnit_Object = MibTableColumn
etsysSrvcLvlMetricUnit = _EtsysSrvcLvlMetricUnit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 1, 3, 1, 4),
    _EtsysSrvcLvlMetricUnit_Type()
)
etsysSrvcLvlMetricUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSrvcLvlMetricUnit.setStatus("current")
_EtsysSrvcLvlMetricDescription_Type = SnmpAdminString
_EtsysSrvcLvlMetricDescription_Object = MibTableColumn
etsysSrvcLvlMetricDescription = _EtsysSrvcLvlMetricDescription_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 1, 3, 1, 5),
    _EtsysSrvcLvlMetricDescription_Type()
)
etsysSrvcLvlMetricDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSrvcLvlMetricDescription.setStatus("current")
_EtsysSrvcLvlOwners_ObjectIdentity = ObjectIdentity
etsysSrvcLvlOwners = _EtsysSrvcLvlOwners_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 2)
)
_EtsysSrvcLvlOwnersTable_Object = MibTable
etsysSrvcLvlOwnersTable = _EtsysSrvcLvlOwnersTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysSrvcLvlOwnersTable.setStatus("current")
_EtsysSrvcLvlOwnersEntry_Object = MibTableRow
etsysSrvcLvlOwnersEntry = _EtsysSrvcLvlOwnersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 2, 1, 1)
)
etsysSrvcLvlOwnersEntry.setIndexNames(
    (0, "ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlOwnersIndex"),
)
if mibBuilder.loadTexts:
    etsysSrvcLvlOwnersEntry.setStatus("current")


class _EtsysSrvcLvlOwnersIndex_Type(Integer32):
    """Custom type etsysSrvcLvlOwnersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysSrvcLvlOwnersIndex_Type.__name__ = "Integer32"
_EtsysSrvcLvlOwnersIndex_Object = MibTableColumn
etsysSrvcLvlOwnersIndex = _EtsysSrvcLvlOwnersIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 2, 1, 1, 1),
    _EtsysSrvcLvlOwnersIndex_Type()
)
etsysSrvcLvlOwnersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysSrvcLvlOwnersIndex.setStatus("current")
_EtsysSrvcLvlOwnersOwner_Type = EtsysSrvcLvlOwnerString
_EtsysSrvcLvlOwnersOwner_Object = MibTableColumn
etsysSrvcLvlOwnersOwner = _EtsysSrvcLvlOwnersOwner_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 2, 1, 1, 2),
    _EtsysSrvcLvlOwnersOwner_Type()
)
etsysSrvcLvlOwnersOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlOwnersOwner.setStatus("current")
_EtsysSrvcLvlOwnersGrantedMetrics_Type = EtsysSrvcLvlStandardMetrics
_EtsysSrvcLvlOwnersGrantedMetrics_Object = MibTableColumn
etsysSrvcLvlOwnersGrantedMetrics = _EtsysSrvcLvlOwnersGrantedMetrics_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 2, 1, 1, 3),
    _EtsysSrvcLvlOwnersGrantedMetrics_Type()
)
etsysSrvcLvlOwnersGrantedMetrics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlOwnersGrantedMetrics.setStatus("current")
_EtsysSrvcLvlOwnersQuota_Type = Integer32
_EtsysSrvcLvlOwnersQuota_Object = MibTableColumn
etsysSrvcLvlOwnersQuota = _EtsysSrvcLvlOwnersQuota_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 2, 1, 1, 4),
    _EtsysSrvcLvlOwnersQuota_Type()
)
etsysSrvcLvlOwnersQuota.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlOwnersQuota.setStatus("current")
_EtsysSrvcLvlOwnersIpAddressType_Type = InetAddressType
_EtsysSrvcLvlOwnersIpAddressType_Object = MibTableColumn
etsysSrvcLvlOwnersIpAddressType = _EtsysSrvcLvlOwnersIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 2, 1, 1, 5),
    _EtsysSrvcLvlOwnersIpAddressType_Type()
)
etsysSrvcLvlOwnersIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlOwnersIpAddressType.setStatus("current")


class _EtsysSrvcLvlOwnersIpAddress_Type(InetAddress):
    """Custom type etsysSrvcLvlOwnersIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EtsysSrvcLvlOwnersIpAddress_Type.__name__ = "InetAddress"
_EtsysSrvcLvlOwnersIpAddress_Object = MibTableColumn
etsysSrvcLvlOwnersIpAddress = _EtsysSrvcLvlOwnersIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 2, 1, 1, 6),
    _EtsysSrvcLvlOwnersIpAddress_Type()
)
etsysSrvcLvlOwnersIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlOwnersIpAddress.setStatus("current")
_EtsysSrvcLvlOwnersEmail_Type = SnmpAdminString
_EtsysSrvcLvlOwnersEmail_Object = MibTableColumn
etsysSrvcLvlOwnersEmail = _EtsysSrvcLvlOwnersEmail_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 2, 1, 1, 7),
    _EtsysSrvcLvlOwnersEmail_Type()
)
etsysSrvcLvlOwnersEmail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlOwnersEmail.setStatus("current")
_EtsysSrvcLvlOwnersSMS_Type = SnmpAdminString
_EtsysSrvcLvlOwnersSMS_Object = MibTableColumn
etsysSrvcLvlOwnersSMS = _EtsysSrvcLvlOwnersSMS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 2, 1, 1, 8),
    _EtsysSrvcLvlOwnersSMS_Type()
)
etsysSrvcLvlOwnersSMS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlOwnersSMS.setStatus("current")
_EtsysSrvcLvlOwnersStatus_Type = RowStatus
_EtsysSrvcLvlOwnersStatus_Object = MibTableColumn
etsysSrvcLvlOwnersStatus = _EtsysSrvcLvlOwnersStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 2, 1, 1, 9),
    _EtsysSrvcLvlOwnersStatus_Type()
)
etsysSrvcLvlOwnersStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlOwnersStatus.setStatus("current")
_EtsysSrvcLvlHistory_ObjectIdentity = ObjectIdentity
etsysSrvcLvlHistory = _EtsysSrvcLvlHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 3)
)
_EtsysSrvcLvlHistoryTable_Object = MibTable
etsysSrvcLvlHistoryTable = _EtsysSrvcLvlHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysSrvcLvlHistoryTable.setStatus("current")
_EtsysSrvcLvlHistoryEntry_Object = MibTableRow
etsysSrvcLvlHistoryEntry = _EtsysSrvcLvlHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 3, 1, 1)
)
etsysSrvcLvlHistoryEntry.setIndexNames(
    (0, "ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlHistoryMeasureOwner"),
    (0, "ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlHistoryMeasureIndex"),
    (0, "ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlHistoryMetricIndex"),
    (0, "ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlHistoryIndex"),
)
if mibBuilder.loadTexts:
    etsysSrvcLvlHistoryEntry.setStatus("current")
_EtsysSrvcLvlHistoryMeasureOwner_Type = EtsysSrvcLvlOwnerString
_EtsysSrvcLvlHistoryMeasureOwner_Object = MibTableColumn
etsysSrvcLvlHistoryMeasureOwner = _EtsysSrvcLvlHistoryMeasureOwner_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 3, 1, 1, 1),
    _EtsysSrvcLvlHistoryMeasureOwner_Type()
)
etsysSrvcLvlHistoryMeasureOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysSrvcLvlHistoryMeasureOwner.setStatus("current")


class _EtsysSrvcLvlHistoryMeasureIndex_Type(Integer32):
    """Custom type etsysSrvcLvlHistoryMeasureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysSrvcLvlHistoryMeasureIndex_Type.__name__ = "Integer32"
_EtsysSrvcLvlHistoryMeasureIndex_Object = MibTableColumn
etsysSrvcLvlHistoryMeasureIndex = _EtsysSrvcLvlHistoryMeasureIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 3, 1, 1, 2),
    _EtsysSrvcLvlHistoryMeasureIndex_Type()
)
etsysSrvcLvlHistoryMeasureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysSrvcLvlHistoryMeasureIndex.setStatus("current")


class _EtsysSrvcLvlHistoryMetricIndex_Type(Integer32):
    """Custom type etsysSrvcLvlHistoryMetricIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysSrvcLvlHistoryMetricIndex_Type.__name__ = "Integer32"
_EtsysSrvcLvlHistoryMetricIndex_Object = MibTableColumn
etsysSrvcLvlHistoryMetricIndex = _EtsysSrvcLvlHistoryMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 3, 1, 1, 3),
    _EtsysSrvcLvlHistoryMetricIndex_Type()
)
etsysSrvcLvlHistoryMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysSrvcLvlHistoryMetricIndex.setStatus("current")


class _EtsysSrvcLvlHistoryIndex_Type(Integer32):
    """Custom type etsysSrvcLvlHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysSrvcLvlHistoryIndex_Type.__name__ = "Integer32"
_EtsysSrvcLvlHistoryIndex_Object = MibTableColumn
etsysSrvcLvlHistoryIndex = _EtsysSrvcLvlHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 3, 1, 1, 4),
    _EtsysSrvcLvlHistoryIndex_Type()
)
etsysSrvcLvlHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysSrvcLvlHistoryIndex.setStatus("current")


class _EtsysSrvcLvlHistorySequence_Type(Integer32):
    """Custom type etsysSrvcLvlHistorySequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysSrvcLvlHistorySequence_Type.__name__ = "Integer32"
_EtsysSrvcLvlHistorySequence_Object = MibTableColumn
etsysSrvcLvlHistorySequence = _EtsysSrvcLvlHistorySequence_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 3, 1, 1, 5),
    _EtsysSrvcLvlHistorySequence_Type()
)
etsysSrvcLvlHistorySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSrvcLvlHistorySequence.setStatus("current")
_EtsysSrvcLvlHistoryTimestamp_Type = GMTTimeStamp
_EtsysSrvcLvlHistoryTimestamp_Object = MibTableColumn
etsysSrvcLvlHistoryTimestamp = _EtsysSrvcLvlHistoryTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 3, 1, 1, 6),
    _EtsysSrvcLvlHistoryTimestamp_Type()
)
etsysSrvcLvlHistoryTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSrvcLvlHistoryTimestamp.setStatus("current")
_EtsysSrvcLvlHistoryValue_Type = Integer32
_EtsysSrvcLvlHistoryValue_Object = MibTableColumn
etsysSrvcLvlHistoryValue = _EtsysSrvcLvlHistoryValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 3, 1, 1, 7),
    _EtsysSrvcLvlHistoryValue_Type()
)
etsysSrvcLvlHistoryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSrvcLvlHistoryValue.setStatus("current")
_EtsysSrvcLvlMeasure_ObjectIdentity = ObjectIdentity
etsysSrvcLvlMeasure = _EtsysSrvcLvlMeasure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4)
)
_EtsysSrvcLvlNetMeasureTable_Object = MibTable
etsysSrvcLvlNetMeasureTable = _EtsysSrvcLvlNetMeasureTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1)
)
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureTable.setStatus("current")
_EtsysSrvcLvlNetMeasureEntry_Object = MibTableRow
etsysSrvcLvlNetMeasureEntry = _EtsysSrvcLvlNetMeasureEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1)
)
etsysSrvcLvlNetMeasureEntry.setIndexNames(
    (0, "ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureOwner"),
    (0, "ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureIndex"),
)
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureEntry.setStatus("current")
_EtsysSrvcLvlNetMeasureOwner_Type = EtsysSrvcLvlOwnerString
_EtsysSrvcLvlNetMeasureOwner_Object = MibTableColumn
etsysSrvcLvlNetMeasureOwner = _EtsysSrvcLvlNetMeasureOwner_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 1),
    _EtsysSrvcLvlNetMeasureOwner_Type()
)
etsysSrvcLvlNetMeasureOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureOwner.setStatus("current")


class _EtsysSrvcLvlNetMeasureIndex_Type(Integer32):
    """Custom type etsysSrvcLvlNetMeasureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysSrvcLvlNetMeasureIndex_Type.__name__ = "Integer32"
_EtsysSrvcLvlNetMeasureIndex_Object = MibTableColumn
etsysSrvcLvlNetMeasureIndex = _EtsysSrvcLvlNetMeasureIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 2),
    _EtsysSrvcLvlNetMeasureIndex_Type()
)
etsysSrvcLvlNetMeasureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureIndex.setStatus("current")
_EtsysSrvcLvlNetMeasureName_Type = SnmpAdminString
_EtsysSrvcLvlNetMeasureName_Object = MibTableColumn
etsysSrvcLvlNetMeasureName = _EtsysSrvcLvlNetMeasureName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 3),
    _EtsysSrvcLvlNetMeasureName_Type()
)
etsysSrvcLvlNetMeasureName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureName.setStatus("current")
_EtsysSrvcLvlNetMeasureMetrics_Type = EtsysSrvcLvlStandardMetrics
_EtsysSrvcLvlNetMeasureMetrics_Object = MibTableColumn
etsysSrvcLvlNetMeasureMetrics = _EtsysSrvcLvlNetMeasureMetrics_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 4),
    _EtsysSrvcLvlNetMeasureMetrics_Type()
)
etsysSrvcLvlNetMeasureMetrics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureMetrics.setStatus("current")
_EtsysSrvcLvlNetMeasureBeginTime_Type = GMTTimeStamp
_EtsysSrvcLvlNetMeasureBeginTime_Object = MibTableColumn
etsysSrvcLvlNetMeasureBeginTime = _EtsysSrvcLvlNetMeasureBeginTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 5),
    _EtsysSrvcLvlNetMeasureBeginTime_Type()
)
etsysSrvcLvlNetMeasureBeginTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureBeginTime.setStatus("current")


class _EtsysSrvcLvlNetMeasureDurationUnit_Type(TimeUnit):
    """Custom type etsysSrvcLvlNetMeasureDurationUnit based on TimeUnit"""


_EtsysSrvcLvlNetMeasureDurationUnit_Object = MibTableColumn
etsysSrvcLvlNetMeasureDurationUnit = _EtsysSrvcLvlNetMeasureDurationUnit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 6),
    _EtsysSrvcLvlNetMeasureDurationUnit_Type()
)
etsysSrvcLvlNetMeasureDurationUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureDurationUnit.setStatus("current")
_EtsysSrvcLvlNetMeasureDuration_Type = Integer32
_EtsysSrvcLvlNetMeasureDuration_Object = MibTableColumn
etsysSrvcLvlNetMeasureDuration = _EtsysSrvcLvlNetMeasureDuration_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 7),
    _EtsysSrvcLvlNetMeasureDuration_Type()
)
etsysSrvcLvlNetMeasureDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureDuration.setStatus("current")
_EtsysSrvcLvlNetMeasureHistorySize_Type = Integer32
_EtsysSrvcLvlNetMeasureHistorySize_Object = MibTableColumn
etsysSrvcLvlNetMeasureHistorySize = _EtsysSrvcLvlNetMeasureHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 8),
    _EtsysSrvcLvlNetMeasureHistorySize_Type()
)
etsysSrvcLvlNetMeasureHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureHistorySize.setStatus("current")


class _EtsysSrvcLvlNetMeasureFailureMgmtMode_Type(Integer32):
    """Custom type etsysSrvcLvlNetMeasureFailureMgmtMode based on Integer32"""
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
        *(("auto", 1),
          ("discarded", 3),
          ("manual", 2))
    )


_EtsysSrvcLvlNetMeasureFailureMgmtMode_Type.__name__ = "Integer32"
_EtsysSrvcLvlNetMeasureFailureMgmtMode_Object = MibTableColumn
etsysSrvcLvlNetMeasureFailureMgmtMode = _EtsysSrvcLvlNetMeasureFailureMgmtMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 9),
    _EtsysSrvcLvlNetMeasureFailureMgmtMode_Type()
)
etsysSrvcLvlNetMeasureFailureMgmtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureFailureMgmtMode.setStatus("current")


class _EtsysSrvcLvlNetMeasureResultsMgmt_Type(Integer32):
    """Custom type etsysSrvcLvlNetMeasureResultsMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("suspend", 2),
          ("wrap", 1))
    )


_EtsysSrvcLvlNetMeasureResultsMgmt_Type.__name__ = "Integer32"
_EtsysSrvcLvlNetMeasureResultsMgmt_Object = MibTableColumn
etsysSrvcLvlNetMeasureResultsMgmt = _EtsysSrvcLvlNetMeasureResultsMgmt_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 10),
    _EtsysSrvcLvlNetMeasureResultsMgmt_Type()
)
etsysSrvcLvlNetMeasureResultsMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureResultsMgmt.setStatus("current")


class _EtsysSrvcLvlNetMeasureSrcTypeP_Type(TypeP):
    """Custom type etsysSrvcLvlNetMeasureSrcTypeP based on TypeP"""
    defaultValue = OctetString("ip")


_EtsysSrvcLvlNetMeasureSrcTypeP_Object = MibTableColumn
etsysSrvcLvlNetMeasureSrcTypeP = _EtsysSrvcLvlNetMeasureSrcTypeP_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 11),
    _EtsysSrvcLvlNetMeasureSrcTypeP_Type()
)
etsysSrvcLvlNetMeasureSrcTypeP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureSrcTypeP.setStatus("current")
_EtsysSrvcLvlNetMeasureSrc_Type = TypePaddress
_EtsysSrvcLvlNetMeasureSrc_Object = MibTableColumn
etsysSrvcLvlNetMeasureSrc = _EtsysSrvcLvlNetMeasureSrc_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 12),
    _EtsysSrvcLvlNetMeasureSrc_Type()
)
etsysSrvcLvlNetMeasureSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureSrc.setStatus("current")


class _EtsysSrvcLvlNetMeasureDstTypeP_Type(TypeP):
    """Custom type etsysSrvcLvlNetMeasureDstTypeP based on TypeP"""
    defaultValue = OctetString("ip")


_EtsysSrvcLvlNetMeasureDstTypeP_Object = MibTableColumn
etsysSrvcLvlNetMeasureDstTypeP = _EtsysSrvcLvlNetMeasureDstTypeP_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 13),
    _EtsysSrvcLvlNetMeasureDstTypeP_Type()
)
etsysSrvcLvlNetMeasureDstTypeP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureDstTypeP.setStatus("current")
_EtsysSrvcLvlNetMeasureDst_Type = TypePaddress
_EtsysSrvcLvlNetMeasureDst_Object = MibTableColumn
etsysSrvcLvlNetMeasureDst = _EtsysSrvcLvlNetMeasureDst_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 14),
    _EtsysSrvcLvlNetMeasureDst_Type()
)
etsysSrvcLvlNetMeasureDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureDst.setStatus("current")


class _EtsysSrvcLvlNetMeasureTxMode_Type(Integer32):
    """Custom type etsysSrvcLvlNetMeasureTxMode based on Integer32"""
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
        *(("multiburst", 3),
          ("other", 0),
          ("periodic", 1),
          ("poisson", 2))
    )


_EtsysSrvcLvlNetMeasureTxMode_Type.__name__ = "Integer32"
_EtsysSrvcLvlNetMeasureTxMode_Object = MibTableColumn
etsysSrvcLvlNetMeasureTxMode = _EtsysSrvcLvlNetMeasureTxMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 15),
    _EtsysSrvcLvlNetMeasureTxMode_Type()
)
etsysSrvcLvlNetMeasureTxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureTxMode.setStatus("current")
_EtsysSrvcLvlNetMeasureTxPacketRateUnit_Type = TimeUnit
_EtsysSrvcLvlNetMeasureTxPacketRateUnit_Object = MibTableColumn
etsysSrvcLvlNetMeasureTxPacketRateUnit = _EtsysSrvcLvlNetMeasureTxPacketRateUnit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 16),
    _EtsysSrvcLvlNetMeasureTxPacketRateUnit_Type()
)
etsysSrvcLvlNetMeasureTxPacketRateUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureTxPacketRateUnit.setStatus("current")
_EtsysSrvcLvlNetMeasureTxPacketRate_Type = Integer32
_EtsysSrvcLvlNetMeasureTxPacketRate_Object = MibTableColumn
etsysSrvcLvlNetMeasureTxPacketRate = _EtsysSrvcLvlNetMeasureTxPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 17),
    _EtsysSrvcLvlNetMeasureTxPacketRate_Type()
)
etsysSrvcLvlNetMeasureTxPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureTxPacketRate.setStatus("current")
_EtsysSrvcLvlNetMeasureDevtnOrBurstSize_Type = Integer32
_EtsysSrvcLvlNetMeasureDevtnOrBurstSize_Object = MibTableColumn
etsysSrvcLvlNetMeasureDevtnOrBurstSize = _EtsysSrvcLvlNetMeasureDevtnOrBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 18),
    _EtsysSrvcLvlNetMeasureDevtnOrBurstSize_Type()
)
etsysSrvcLvlNetMeasureDevtnOrBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureDevtnOrBurstSize.setStatus("current")
_EtsysSrvcLvlNetMeasureMedOrIntBurstSize_Type = Integer32
_EtsysSrvcLvlNetMeasureMedOrIntBurstSize_Object = MibTableColumn
etsysSrvcLvlNetMeasureMedOrIntBurstSize = _EtsysSrvcLvlNetMeasureMedOrIntBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 19),
    _EtsysSrvcLvlNetMeasureMedOrIntBurstSize_Type()
)
etsysSrvcLvlNetMeasureMedOrIntBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureMedOrIntBurstSize.setStatus("current")
_EtsysSrvcLvlNetMeasureLossTimeout_Type = Integer32
_EtsysSrvcLvlNetMeasureLossTimeout_Object = MibTableColumn
etsysSrvcLvlNetMeasureLossTimeout = _EtsysSrvcLvlNetMeasureLossTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 20),
    _EtsysSrvcLvlNetMeasureLossTimeout_Type()
)
etsysSrvcLvlNetMeasureLossTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureLossTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureLossTimeout.setUnits("Milliseconds")
_EtsysSrvcLvlNetMeasureL3PacketSize_Type = Integer32
_EtsysSrvcLvlNetMeasureL3PacketSize_Object = MibTableColumn
etsysSrvcLvlNetMeasureL3PacketSize = _EtsysSrvcLvlNetMeasureL3PacketSize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 21),
    _EtsysSrvcLvlNetMeasureL3PacketSize_Type()
)
etsysSrvcLvlNetMeasureL3PacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureL3PacketSize.setStatus("current")
_EtsysSrvcLvlNetMeasureDataPattern_Type = OctetString
_EtsysSrvcLvlNetMeasureDataPattern_Object = MibTableColumn
etsysSrvcLvlNetMeasureDataPattern = _EtsysSrvcLvlNetMeasureDataPattern_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 22),
    _EtsysSrvcLvlNetMeasureDataPattern_Type()
)
etsysSrvcLvlNetMeasureDataPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureDataPattern.setStatus("current")
_EtsysSrvcLvlNetMeasureMap_Type = SnmpAdminString
_EtsysSrvcLvlNetMeasureMap_Object = MibTableColumn
etsysSrvcLvlNetMeasureMap = _EtsysSrvcLvlNetMeasureMap_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 23),
    _EtsysSrvcLvlNetMeasureMap_Type()
)
etsysSrvcLvlNetMeasureMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureMap.setStatus("current")
_EtsysSrvcLvlNetMeasureSingletons_Type = Integer32
_EtsysSrvcLvlNetMeasureSingletons_Object = MibTableColumn
etsysSrvcLvlNetMeasureSingletons = _EtsysSrvcLvlNetMeasureSingletons_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 24),
    _EtsysSrvcLvlNetMeasureSingletons_Type()
)
etsysSrvcLvlNetMeasureSingletons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureSingletons.setStatus("current")


class _EtsysSrvcLvlNetMeasureOperState_Type(Integer32):
    """Custom type etsysSrvcLvlNetMeasureOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 2),
          ("unknown", 0))
    )


_EtsysSrvcLvlNetMeasureOperState_Type.__name__ = "Integer32"
_EtsysSrvcLvlNetMeasureOperState_Object = MibTableColumn
etsysSrvcLvlNetMeasureOperState = _EtsysSrvcLvlNetMeasureOperState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 1, 1, 25),
    _EtsysSrvcLvlNetMeasureOperState_Type()
)
etsysSrvcLvlNetMeasureOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSrvcLvlNetMeasureOperState.setStatus("current")
_EtsysSrvcLvlAggrMeasureTable_Object = MibTable
etsysSrvcLvlAggrMeasureTable = _EtsysSrvcLvlAggrMeasureTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2)
)
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureTable.setStatus("current")
_EtsysSrvcLvlAggrMeasureEntry_Object = MibTableRow
etsysSrvcLvlAggrMeasureEntry = _EtsysSrvcLvlAggrMeasureEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1)
)
etsysSrvcLvlAggrMeasureEntry.setIndexNames(
    (0, "ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureOwner"),
    (0, "ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureIndex"),
)
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureEntry.setStatus("current")
_EtsysSrvcLvlAggrMeasureOwner_Type = EtsysSrvcLvlOwnerString
_EtsysSrvcLvlAggrMeasureOwner_Object = MibTableColumn
etsysSrvcLvlAggrMeasureOwner = _EtsysSrvcLvlAggrMeasureOwner_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 1),
    _EtsysSrvcLvlAggrMeasureOwner_Type()
)
etsysSrvcLvlAggrMeasureOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureOwner.setStatus("current")


class _EtsysSrvcLvlAggrMeasureIndex_Type(Integer32):
    """Custom type etsysSrvcLvlAggrMeasureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysSrvcLvlAggrMeasureIndex_Type.__name__ = "Integer32"
_EtsysSrvcLvlAggrMeasureIndex_Object = MibTableColumn
etsysSrvcLvlAggrMeasureIndex = _EtsysSrvcLvlAggrMeasureIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 2),
    _EtsysSrvcLvlAggrMeasureIndex_Type()
)
etsysSrvcLvlAggrMeasureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureIndex.setStatus("current")
_EtsysSrvcLvlAggrMeasureName_Type = SnmpAdminString
_EtsysSrvcLvlAggrMeasureName_Object = MibTableColumn
etsysSrvcLvlAggrMeasureName = _EtsysSrvcLvlAggrMeasureName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 3),
    _EtsysSrvcLvlAggrMeasureName_Type()
)
etsysSrvcLvlAggrMeasureName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureName.setStatus("current")
_EtsysSrvcLvlAggrMeasureMetrics_Type = EtsysSrvcLvlStandardMetrics
_EtsysSrvcLvlAggrMeasureMetrics_Object = MibTableColumn
etsysSrvcLvlAggrMeasureMetrics = _EtsysSrvcLvlAggrMeasureMetrics_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 4),
    _EtsysSrvcLvlAggrMeasureMetrics_Type()
)
etsysSrvcLvlAggrMeasureMetrics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureMetrics.setStatus("current")
_EtsysSrvcLvlAggrMeasureBeginTime_Type = GMTTimeStamp
_EtsysSrvcLvlAggrMeasureBeginTime_Object = MibTableColumn
etsysSrvcLvlAggrMeasureBeginTime = _EtsysSrvcLvlAggrMeasureBeginTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 5),
    _EtsysSrvcLvlAggrMeasureBeginTime_Type()
)
etsysSrvcLvlAggrMeasureBeginTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureBeginTime.setStatus("current")


class _EtsysSrvcLvlAggrMeasureAggrPeriodUnit_Type(TimeUnit):
    """Custom type etsysSrvcLvlAggrMeasureAggrPeriodUnit based on TimeUnit"""


_EtsysSrvcLvlAggrMeasureAggrPeriodUnit_Object = MibTableColumn
etsysSrvcLvlAggrMeasureAggrPeriodUnit = _EtsysSrvcLvlAggrMeasureAggrPeriodUnit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 6),
    _EtsysSrvcLvlAggrMeasureAggrPeriodUnit_Type()
)
etsysSrvcLvlAggrMeasureAggrPeriodUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureAggrPeriodUnit.setStatus("current")
_EtsysSrvcLvlAggrMeasureAggrPeriod_Type = Integer32
_EtsysSrvcLvlAggrMeasureAggrPeriod_Object = MibTableColumn
etsysSrvcLvlAggrMeasureAggrPeriod = _EtsysSrvcLvlAggrMeasureAggrPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 7),
    _EtsysSrvcLvlAggrMeasureAggrPeriod_Type()
)
etsysSrvcLvlAggrMeasureAggrPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureAggrPeriod.setStatus("current")


class _EtsysSrvcLvlAggrMeasureDurationUnit_Type(TimeUnit):
    """Custom type etsysSrvcLvlAggrMeasureDurationUnit based on TimeUnit"""


_EtsysSrvcLvlAggrMeasureDurationUnit_Object = MibTableColumn
etsysSrvcLvlAggrMeasureDurationUnit = _EtsysSrvcLvlAggrMeasureDurationUnit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 8),
    _EtsysSrvcLvlAggrMeasureDurationUnit_Type()
)
etsysSrvcLvlAggrMeasureDurationUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureDurationUnit.setStatus("current")
_EtsysSrvcLvlAggrMeasureDuration_Type = Integer32
_EtsysSrvcLvlAggrMeasureDuration_Object = MibTableColumn
etsysSrvcLvlAggrMeasureDuration = _EtsysSrvcLvlAggrMeasureDuration_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 9),
    _EtsysSrvcLvlAggrMeasureDuration_Type()
)
etsysSrvcLvlAggrMeasureDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureDuration.setStatus("current")
_EtsysSrvcLvlAggrMeasureHistorySize_Type = Integer32
_EtsysSrvcLvlAggrMeasureHistorySize_Object = MibTableColumn
etsysSrvcLvlAggrMeasureHistorySize = _EtsysSrvcLvlAggrMeasureHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 10),
    _EtsysSrvcLvlAggrMeasureHistorySize_Type()
)
etsysSrvcLvlAggrMeasureHistorySize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureHistorySize.setStatus("current")


class _EtsysSrvcLvlAggrMeasureStorageType_Type(StorageType):
    """Custom type etsysSrvcLvlAggrMeasureStorageType based on StorageType"""


_EtsysSrvcLvlAggrMeasureStorageType_Object = MibTableColumn
etsysSrvcLvlAggrMeasureStorageType = _EtsysSrvcLvlAggrMeasureStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 11),
    _EtsysSrvcLvlAggrMeasureStorageType_Type()
)
etsysSrvcLvlAggrMeasureStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureStorageType.setStatus("current")


class _EtsysSrvcLvlAggrMeasureResultsMgmt_Type(Integer32):
    """Custom type etsysSrvcLvlAggrMeasureResultsMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("suspend", 2),
          ("wrap", 1))
    )


_EtsysSrvcLvlAggrMeasureResultsMgmt_Type.__name__ = "Integer32"
_EtsysSrvcLvlAggrMeasureResultsMgmt_Object = MibTableColumn
etsysSrvcLvlAggrMeasureResultsMgmt = _EtsysSrvcLvlAggrMeasureResultsMgmt_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 12),
    _EtsysSrvcLvlAggrMeasureResultsMgmt_Type()
)
etsysSrvcLvlAggrMeasureResultsMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureResultsMgmt.setStatus("current")
_EtsysSrvcLvlAggrMeasureHistoryOwner_Type = EtsysSrvcLvlOwnerString
_EtsysSrvcLvlAggrMeasureHistoryOwner_Object = MibTableColumn
etsysSrvcLvlAggrMeasureHistoryOwner = _EtsysSrvcLvlAggrMeasureHistoryOwner_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 13),
    _EtsysSrvcLvlAggrMeasureHistoryOwner_Type()
)
etsysSrvcLvlAggrMeasureHistoryOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureHistoryOwner.setStatus("current")


class _EtsysSrvcLvlAggrMeasureHistoryOwnerIndex_Type(Integer32):
    """Custom type etsysSrvcLvlAggrMeasureHistoryOwnerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysSrvcLvlAggrMeasureHistoryOwnerIndex_Type.__name__ = "Integer32"
_EtsysSrvcLvlAggrMeasureHistoryOwnerIndex_Object = MibTableColumn
etsysSrvcLvlAggrMeasureHistoryOwnerIndex = _EtsysSrvcLvlAggrMeasureHistoryOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 14),
    _EtsysSrvcLvlAggrMeasureHistoryOwnerIndex_Type()
)
etsysSrvcLvlAggrMeasureHistoryOwnerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureHistoryOwnerIndex.setStatus("current")
_EtsysSrvcLvlAggrMeasureHistoryMetric_Type = Integer32
_EtsysSrvcLvlAggrMeasureHistoryMetric_Object = MibTableColumn
etsysSrvcLvlAggrMeasureHistoryMetric = _EtsysSrvcLvlAggrMeasureHistoryMetric_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 15),
    _EtsysSrvcLvlAggrMeasureHistoryMetric_Type()
)
etsysSrvcLvlAggrMeasureHistoryMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureHistoryMetric.setStatus("current")


class _EtsysSrvcLvlAggrMeasureAdminState_Type(Integer32):
    """Custom type etsysSrvcLvlAggrMeasureAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("start", 0),
          ("stop", 1))
    )


_EtsysSrvcLvlAggrMeasureAdminState_Type.__name__ = "Integer32"
_EtsysSrvcLvlAggrMeasureAdminState_Object = MibTableColumn
etsysSrvcLvlAggrMeasureAdminState = _EtsysSrvcLvlAggrMeasureAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 16),
    _EtsysSrvcLvlAggrMeasureAdminState_Type()
)
etsysSrvcLvlAggrMeasureAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureAdminState.setStatus("current")
_EtsysSrvcLvlAggrMeasureMap_Type = SnmpAdminString
_EtsysSrvcLvlAggrMeasureMap_Object = MibTableColumn
etsysSrvcLvlAggrMeasureMap = _EtsysSrvcLvlAggrMeasureMap_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 17),
    _EtsysSrvcLvlAggrMeasureMap_Type()
)
etsysSrvcLvlAggrMeasureMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureMap.setStatus("current")
_EtsysSrvcLvlAggrMeasureStatus_Type = RowStatus
_EtsysSrvcLvlAggrMeasureStatus_Object = MibTableColumn
etsysSrvcLvlAggrMeasureStatus = _EtsysSrvcLvlAggrMeasureStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 1, 4, 2, 1, 18),
    _EtsysSrvcLvlAggrMeasureStatus_Type()
)
etsysSrvcLvlAggrMeasureStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSrvcLvlAggrMeasureStatus.setStatus("current")
_EtsysSrvcLvlReportingConformance_ObjectIdentity = ObjectIdentity
etsysSrvcLvlReportingConformance = _EtsysSrvcLvlReportingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 2)
)
_EtsysSrvcLvlReportingGroups_ObjectIdentity = ObjectIdentity
etsysSrvcLvlReportingGroups = _EtsysSrvcLvlReportingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 2, 1)
)
_EtsysSrvcLvlReportingCompliances_ObjectIdentity = ObjectIdentity
etsysSrvcLvlReportingCompliances = _EtsysSrvcLvlReportingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 2, 2)
)

# Managed Objects groups

etsysSrvcLvlSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 2, 1, 1)
)
etsysSrvcLvlSystemGroup.setObjects(
      *(("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlSystemTime"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlSystemClockResolution"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlMetricCapabilities"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlMetricType"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlMetricUnit"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlMetricDescription"))
)
if mibBuilder.loadTexts:
    etsysSrvcLvlSystemGroup.setStatus("current")

etsysSrvcLvlOwnersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 2, 1, 2)
)
etsysSrvcLvlOwnersGroup.setObjects(
      *(("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlOwnersOwner"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlOwnersGrantedMetrics"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlOwnersQuota"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlOwnersIpAddressType"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlOwnersIpAddress"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlOwnersEmail"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlOwnersSMS"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlOwnersStatus"))
)
if mibBuilder.loadTexts:
    etsysSrvcLvlOwnersGroup.setStatus("current")

etsysSrvcLvlHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 2, 1, 3)
)
etsysSrvcLvlHistoryGroup.setObjects(
      *(("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlHistorySequence"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlHistoryTimestamp"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlHistoryValue"))
)
if mibBuilder.loadTexts:
    etsysSrvcLvlHistoryGroup.setStatus("current")

etsysSrvcLvlMeasureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 2, 1, 4)
)
etsysSrvcLvlMeasureGroup.setObjects(
      *(("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureName"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureMetrics"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureBeginTime"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureDurationUnit"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureDuration"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureHistorySize"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureFailureMgmtMode"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureResultsMgmt"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureSrcTypeP"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureSrc"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureDstTypeP"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureDst"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureTxMode"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureTxPacketRateUnit"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureTxPacketRate"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureDevtnOrBurstSize"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureMedOrIntBurstSize"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureLossTimeout"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureL3PacketSize"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureDataPattern"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureMap"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureSingletons"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlNetMeasureOperState"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureName"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureMetrics"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureBeginTime"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureAggrPeriodUnit"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureAggrPeriod"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureDurationUnit"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureDuration"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureHistorySize"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureStorageType"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureResultsMgmt"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureHistoryOwner"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureHistoryOwnerIndex"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureHistoryMetric"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureAdminState"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureMap"),
        ("ENTERASYS-SERVICE-LEVEL-REPORTING-MIB", "etsysSrvcLvlAggrMeasureStatus"))
)
if mibBuilder.loadTexts:
    etsysSrvcLvlMeasureGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysSrvcLvlReportingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 39, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysSrvcLvlReportingCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-SERVICE-LEVEL-REPORTING-MIB",
    **{"EtsysSrvcLvlOwnerString": EtsysSrvcLvlOwnerString,
       "TimeUnit": TimeUnit,
       "EtsysSrvcLvlStandardMetrics": EtsysSrvcLvlStandardMetrics,
       "GMTTimeStamp": GMTTimeStamp,
       "TypeP": TypeP,
       "TypePaddress": TypePaddress,
       "etsysServiceLevelReportingMIB": etsysServiceLevelReportingMIB,
       "etsysSrvcLvlConfigObjects": etsysSrvcLvlConfigObjects,
       "etsysSrvcLvlSystem": etsysSrvcLvlSystem,
       "etsysSrvcLvlSystemTime": etsysSrvcLvlSystemTime,
       "etsysSrvcLvlSystemClockResolution": etsysSrvcLvlSystemClockResolution,
       "etsysSrvcLvlMetricTable": etsysSrvcLvlMetricTable,
       "etsysSrvcLvlMetricEntry": etsysSrvcLvlMetricEntry,
       "etsysSrvcLvlMetricIndex": etsysSrvcLvlMetricIndex,
       "etsysSrvcLvlMetricCapabilities": etsysSrvcLvlMetricCapabilities,
       "etsysSrvcLvlMetricType": etsysSrvcLvlMetricType,
       "etsysSrvcLvlMetricUnit": etsysSrvcLvlMetricUnit,
       "etsysSrvcLvlMetricDescription": etsysSrvcLvlMetricDescription,
       "etsysSrvcLvlOwners": etsysSrvcLvlOwners,
       "etsysSrvcLvlOwnersTable": etsysSrvcLvlOwnersTable,
       "etsysSrvcLvlOwnersEntry": etsysSrvcLvlOwnersEntry,
       "etsysSrvcLvlOwnersIndex": etsysSrvcLvlOwnersIndex,
       "etsysSrvcLvlOwnersOwner": etsysSrvcLvlOwnersOwner,
       "etsysSrvcLvlOwnersGrantedMetrics": etsysSrvcLvlOwnersGrantedMetrics,
       "etsysSrvcLvlOwnersQuota": etsysSrvcLvlOwnersQuota,
       "etsysSrvcLvlOwnersIpAddressType": etsysSrvcLvlOwnersIpAddressType,
       "etsysSrvcLvlOwnersIpAddress": etsysSrvcLvlOwnersIpAddress,
       "etsysSrvcLvlOwnersEmail": etsysSrvcLvlOwnersEmail,
       "etsysSrvcLvlOwnersSMS": etsysSrvcLvlOwnersSMS,
       "etsysSrvcLvlOwnersStatus": etsysSrvcLvlOwnersStatus,
       "etsysSrvcLvlHistory": etsysSrvcLvlHistory,
       "etsysSrvcLvlHistoryTable": etsysSrvcLvlHistoryTable,
       "etsysSrvcLvlHistoryEntry": etsysSrvcLvlHistoryEntry,
       "etsysSrvcLvlHistoryMeasureOwner": etsysSrvcLvlHistoryMeasureOwner,
       "etsysSrvcLvlHistoryMeasureIndex": etsysSrvcLvlHistoryMeasureIndex,
       "etsysSrvcLvlHistoryMetricIndex": etsysSrvcLvlHistoryMetricIndex,
       "etsysSrvcLvlHistoryIndex": etsysSrvcLvlHistoryIndex,
       "etsysSrvcLvlHistorySequence": etsysSrvcLvlHistorySequence,
       "etsysSrvcLvlHistoryTimestamp": etsysSrvcLvlHistoryTimestamp,
       "etsysSrvcLvlHistoryValue": etsysSrvcLvlHistoryValue,
       "etsysSrvcLvlMeasure": etsysSrvcLvlMeasure,
       "etsysSrvcLvlNetMeasureTable": etsysSrvcLvlNetMeasureTable,
       "etsysSrvcLvlNetMeasureEntry": etsysSrvcLvlNetMeasureEntry,
       "etsysSrvcLvlNetMeasureOwner": etsysSrvcLvlNetMeasureOwner,
       "etsysSrvcLvlNetMeasureIndex": etsysSrvcLvlNetMeasureIndex,
       "etsysSrvcLvlNetMeasureName": etsysSrvcLvlNetMeasureName,
       "etsysSrvcLvlNetMeasureMetrics": etsysSrvcLvlNetMeasureMetrics,
       "etsysSrvcLvlNetMeasureBeginTime": etsysSrvcLvlNetMeasureBeginTime,
       "etsysSrvcLvlNetMeasureDurationUnit": etsysSrvcLvlNetMeasureDurationUnit,
       "etsysSrvcLvlNetMeasureDuration": etsysSrvcLvlNetMeasureDuration,
       "etsysSrvcLvlNetMeasureHistorySize": etsysSrvcLvlNetMeasureHistorySize,
       "etsysSrvcLvlNetMeasureFailureMgmtMode": etsysSrvcLvlNetMeasureFailureMgmtMode,
       "etsysSrvcLvlNetMeasureResultsMgmt": etsysSrvcLvlNetMeasureResultsMgmt,
       "etsysSrvcLvlNetMeasureSrcTypeP": etsysSrvcLvlNetMeasureSrcTypeP,
       "etsysSrvcLvlNetMeasureSrc": etsysSrvcLvlNetMeasureSrc,
       "etsysSrvcLvlNetMeasureDstTypeP": etsysSrvcLvlNetMeasureDstTypeP,
       "etsysSrvcLvlNetMeasureDst": etsysSrvcLvlNetMeasureDst,
       "etsysSrvcLvlNetMeasureTxMode": etsysSrvcLvlNetMeasureTxMode,
       "etsysSrvcLvlNetMeasureTxPacketRateUnit": etsysSrvcLvlNetMeasureTxPacketRateUnit,
       "etsysSrvcLvlNetMeasureTxPacketRate": etsysSrvcLvlNetMeasureTxPacketRate,
       "etsysSrvcLvlNetMeasureDevtnOrBurstSize": etsysSrvcLvlNetMeasureDevtnOrBurstSize,
       "etsysSrvcLvlNetMeasureMedOrIntBurstSize": etsysSrvcLvlNetMeasureMedOrIntBurstSize,
       "etsysSrvcLvlNetMeasureLossTimeout": etsysSrvcLvlNetMeasureLossTimeout,
       "etsysSrvcLvlNetMeasureL3PacketSize": etsysSrvcLvlNetMeasureL3PacketSize,
       "etsysSrvcLvlNetMeasureDataPattern": etsysSrvcLvlNetMeasureDataPattern,
       "etsysSrvcLvlNetMeasureMap": etsysSrvcLvlNetMeasureMap,
       "etsysSrvcLvlNetMeasureSingletons": etsysSrvcLvlNetMeasureSingletons,
       "etsysSrvcLvlNetMeasureOperState": etsysSrvcLvlNetMeasureOperState,
       "etsysSrvcLvlAggrMeasureTable": etsysSrvcLvlAggrMeasureTable,
       "etsysSrvcLvlAggrMeasureEntry": etsysSrvcLvlAggrMeasureEntry,
       "etsysSrvcLvlAggrMeasureOwner": etsysSrvcLvlAggrMeasureOwner,
       "etsysSrvcLvlAggrMeasureIndex": etsysSrvcLvlAggrMeasureIndex,
       "etsysSrvcLvlAggrMeasureName": etsysSrvcLvlAggrMeasureName,
       "etsysSrvcLvlAggrMeasureMetrics": etsysSrvcLvlAggrMeasureMetrics,
       "etsysSrvcLvlAggrMeasureBeginTime": etsysSrvcLvlAggrMeasureBeginTime,
       "etsysSrvcLvlAggrMeasureAggrPeriodUnit": etsysSrvcLvlAggrMeasureAggrPeriodUnit,
       "etsysSrvcLvlAggrMeasureAggrPeriod": etsysSrvcLvlAggrMeasureAggrPeriod,
       "etsysSrvcLvlAggrMeasureDurationUnit": etsysSrvcLvlAggrMeasureDurationUnit,
       "etsysSrvcLvlAggrMeasureDuration": etsysSrvcLvlAggrMeasureDuration,
       "etsysSrvcLvlAggrMeasureHistorySize": etsysSrvcLvlAggrMeasureHistorySize,
       "etsysSrvcLvlAggrMeasureStorageType": etsysSrvcLvlAggrMeasureStorageType,
       "etsysSrvcLvlAggrMeasureResultsMgmt": etsysSrvcLvlAggrMeasureResultsMgmt,
       "etsysSrvcLvlAggrMeasureHistoryOwner": etsysSrvcLvlAggrMeasureHistoryOwner,
       "etsysSrvcLvlAggrMeasureHistoryOwnerIndex": etsysSrvcLvlAggrMeasureHistoryOwnerIndex,
       "etsysSrvcLvlAggrMeasureHistoryMetric": etsysSrvcLvlAggrMeasureHistoryMetric,
       "etsysSrvcLvlAggrMeasureAdminState": etsysSrvcLvlAggrMeasureAdminState,
       "etsysSrvcLvlAggrMeasureMap": etsysSrvcLvlAggrMeasureMap,
       "etsysSrvcLvlAggrMeasureStatus": etsysSrvcLvlAggrMeasureStatus,
       "etsysSrvcLvlReportingConformance": etsysSrvcLvlReportingConformance,
       "etsysSrvcLvlReportingGroups": etsysSrvcLvlReportingGroups,
       "etsysSrvcLvlSystemGroup": etsysSrvcLvlSystemGroup,
       "etsysSrvcLvlOwnersGroup": etsysSrvcLvlOwnersGroup,
       "etsysSrvcLvlHistoryGroup": etsysSrvcLvlHistoryGroup,
       "etsysSrvcLvlMeasureGroup": etsysSrvcLvlMeasureGroup,
       "etsysSrvcLvlReportingCompliances": etsysSrvcLvlReportingCompliances,
       "etsysSrvcLvlReportingCompliance": etsysSrvcLvlReportingCompliance}
)
