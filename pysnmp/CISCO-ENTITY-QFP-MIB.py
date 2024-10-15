# SNMP MIB module (CISCO-ENTITY-QFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-QFP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:40 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoEntityQfpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 715)
)
ciscoEntityQfpMIB.setRevisions(
        ("2014-06-18 00:00",
         "2012-06-06 00:00",
         "2009-12-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoQfpPacketRate(Counter64, TextualConvention):
    status = "current"
    displayHint = "d"


class CiscoQfpBitRate(Counter64, TextualConvention):
    status = "current"
    displayHint = "d"


class CiscoQfpTimeInterval(Integer32, TextualConvention):
    status = "current"
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
        *(("fiveMinutes", 3),
          ("fiveSeconds", 1),
          ("oneMinute", 2),
          ("sixtyMinutes", 4))
    )



class CiscoQfpMemoryResource(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dram", 1)
    )



# MIB Managed Objects in the order of their OIDs

_CiscoEntityQfpMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoEntityQfpMIBNotifs = _CiscoEntityQfpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 0)
)
_CiscoEntityQfpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEntityQfpMIBObjects = _CiscoEntityQfpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1)
)
_CiscoEntityQfp_ObjectIdentity = ObjectIdentity
ciscoEntityQfp = _CiscoEntityQfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1)
)
_CeqfpSystemTable_Object = MibTable
ceqfpSystemTable = _CeqfpSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ceqfpSystemTable.setStatus("current")
_CeqfpSystemEntry_Object = MibTableRow
ceqfpSystemEntry = _CeqfpSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 1, 1)
)
ceqfpSystemEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ceqfpSystemEntry.setStatus("current")


class _CeqfpSystemTrafficDirection_Type(Integer32):
    """Custom type ceqfpSystemTrafficDirection based on Integer32"""
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
        *(("both", 4),
          ("egress", 3),
          ("ingress", 2),
          ("none", 1))
    )


_CeqfpSystemTrafficDirection_Type.__name__ = "Integer32"
_CeqfpSystemTrafficDirection_Object = MibTableColumn
ceqfpSystemTrafficDirection = _CeqfpSystemTrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 1, 1, 1),
    _CeqfpSystemTrafficDirection_Type()
)
ceqfpSystemTrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpSystemTrafficDirection.setStatus("current")


class _CeqfpSystemState_Type(Integer32):
    """Custom type ceqfpSystemState based on Integer32"""
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
        *(("active", 4),
          ("activeSolo", 5),
          ("hotStandby", 7),
          ("init", 3),
          ("reset", 2),
          ("standby", 6),
          ("unknown", 1))
    )


_CeqfpSystemState_Type.__name__ = "Integer32"
_CeqfpSystemState_Object = MibTableColumn
ceqfpSystemState = _CeqfpSystemState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 1, 1, 2),
    _CeqfpSystemState_Type()
)
ceqfpSystemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpSystemState.setStatus("current")
_CeqfpNumberSystemLoads_Type = Counter32
_CeqfpNumberSystemLoads_Object = MibTableColumn
ceqfpNumberSystemLoads = _CeqfpNumberSystemLoads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 1, 1, 3),
    _CeqfpNumberSystemLoads_Type()
)
ceqfpNumberSystemLoads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpNumberSystemLoads.setStatus("current")
_CeqfpSystemLastLoadTime_Type = DateAndTime
_CeqfpSystemLastLoadTime_Object = MibTableColumn
ceqfpSystemLastLoadTime = _CeqfpSystemLastLoadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 1, 1, 4),
    _CeqfpSystemLastLoadTime_Type()
)
ceqfpSystemLastLoadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpSystemLastLoadTime.setStatus("current")


class _CeqfpFiveSecondUtilAlgo_Type(Integer32):
    """Custom type ceqfpFiveSecondUtilAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fiveSecSample", 2),
          ("unknown", 1))
    )


_CeqfpFiveSecondUtilAlgo_Type.__name__ = "Integer32"
_CeqfpFiveSecondUtilAlgo_Object = MibScalar
ceqfpFiveSecondUtilAlgo = _CeqfpFiveSecondUtilAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 2),
    _CeqfpFiveSecondUtilAlgo_Type()
)
ceqfpFiveSecondUtilAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpFiveSecondUtilAlgo.setStatus("current")


class _CeqfpOneMinuteUtilAlgo_Type(Integer32):
    """Custom type ceqfpOneMinuteUtilAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fiveSecSMA", 2),
          ("unknown", 1))
    )


_CeqfpOneMinuteUtilAlgo_Type.__name__ = "Integer32"
_CeqfpOneMinuteUtilAlgo_Object = MibScalar
ceqfpOneMinuteUtilAlgo = _CeqfpOneMinuteUtilAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 3),
    _CeqfpOneMinuteUtilAlgo_Type()
)
ceqfpOneMinuteUtilAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpOneMinuteUtilAlgo.setStatus("current")


class _CeqfpFiveMinutesUtilAlgo_Type(Integer32):
    """Custom type ceqfpFiveMinutesUtilAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fiveSecSMA", 2),
          ("unknown", 1))
    )


_CeqfpFiveMinutesUtilAlgo_Type.__name__ = "Integer32"
_CeqfpFiveMinutesUtilAlgo_Object = MibScalar
ceqfpFiveMinutesUtilAlgo = _CeqfpFiveMinutesUtilAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 4),
    _CeqfpFiveMinutesUtilAlgo_Type()
)
ceqfpFiveMinutesUtilAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpFiveMinutesUtilAlgo.setStatus("current")


class _CeqfpSixtyMinutesUtilAlgo_Type(Integer32):
    """Custom type ceqfpSixtyMinutesUtilAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fiveSecSMA", 2),
          ("unknown", 1))
    )


_CeqfpSixtyMinutesUtilAlgo_Type.__name__ = "Integer32"
_CeqfpSixtyMinutesUtilAlgo_Object = MibScalar
ceqfpSixtyMinutesUtilAlgo = _CeqfpSixtyMinutesUtilAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 5),
    _CeqfpSixtyMinutesUtilAlgo_Type()
)
ceqfpSixtyMinutesUtilAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpSixtyMinutesUtilAlgo.setStatus("current")
_CeqfpUtilizationTable_Object = MibTable
ceqfpUtilizationTable = _CeqfpUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ceqfpUtilizationTable.setStatus("current")
_CeqfpUtilizationEntry_Object = MibTableRow
ceqfpUtilizationEntry = _CeqfpUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1)
)
ceqfpUtilizationEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-QFP-MIB", "ceqfpUtilTimeInterval"),
)
if mibBuilder.loadTexts:
    ceqfpUtilizationEntry.setStatus("current")
_CeqfpUtilTimeInterval_Type = CiscoQfpTimeInterval
_CeqfpUtilTimeInterval_Object = MibTableColumn
ceqfpUtilTimeInterval = _CeqfpUtilTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 1),
    _CeqfpUtilTimeInterval_Type()
)
ceqfpUtilTimeInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceqfpUtilTimeInterval.setStatus("current")
_CeqfpUtilInputPriorityPktRate_Type = CiscoQfpPacketRate
_CeqfpUtilInputPriorityPktRate_Object = MibTableColumn
ceqfpUtilInputPriorityPktRate = _CeqfpUtilInputPriorityPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 2),
    _CeqfpUtilInputPriorityPktRate_Type()
)
ceqfpUtilInputPriorityPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpUtilInputPriorityPktRate.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpUtilInputPriorityPktRate.setUnits("packets per second")
_CeqfpUtilInputPriorityBitRate_Type = CiscoQfpBitRate
_CeqfpUtilInputPriorityBitRate_Object = MibTableColumn
ceqfpUtilInputPriorityBitRate = _CeqfpUtilInputPriorityBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 3),
    _CeqfpUtilInputPriorityBitRate_Type()
)
ceqfpUtilInputPriorityBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpUtilInputPriorityBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpUtilInputPriorityBitRate.setUnits("bits per second")
_CeqfpUtilInputNonPriorityPktRate_Type = CiscoQfpPacketRate
_CeqfpUtilInputNonPriorityPktRate_Object = MibTableColumn
ceqfpUtilInputNonPriorityPktRate = _CeqfpUtilInputNonPriorityPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 4),
    _CeqfpUtilInputNonPriorityPktRate_Type()
)
ceqfpUtilInputNonPriorityPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpUtilInputNonPriorityPktRate.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpUtilInputNonPriorityPktRate.setUnits("packets per second")
_CeqfpUtilInputNonPriorityBitRate_Type = CiscoQfpBitRate
_CeqfpUtilInputNonPriorityBitRate_Object = MibTableColumn
ceqfpUtilInputNonPriorityBitRate = _CeqfpUtilInputNonPriorityBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 5),
    _CeqfpUtilInputNonPriorityBitRate_Type()
)
ceqfpUtilInputNonPriorityBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpUtilInputNonPriorityBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpUtilInputNonPriorityBitRate.setUnits("bits per second")
_CeqfpUtilInputTotalPktRate_Type = CiscoQfpPacketRate
_CeqfpUtilInputTotalPktRate_Object = MibTableColumn
ceqfpUtilInputTotalPktRate = _CeqfpUtilInputTotalPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 6),
    _CeqfpUtilInputTotalPktRate_Type()
)
ceqfpUtilInputTotalPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpUtilInputTotalPktRate.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpUtilInputTotalPktRate.setUnits("packets per second")
_CeqfpUtilInputTotalBitRate_Type = CiscoQfpBitRate
_CeqfpUtilInputTotalBitRate_Object = MibTableColumn
ceqfpUtilInputTotalBitRate = _CeqfpUtilInputTotalBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 7),
    _CeqfpUtilInputTotalBitRate_Type()
)
ceqfpUtilInputTotalBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpUtilInputTotalBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpUtilInputTotalBitRate.setUnits("bits per second")
_CeqfpUtilOutputPriorityPktRate_Type = CiscoQfpPacketRate
_CeqfpUtilOutputPriorityPktRate_Object = MibTableColumn
ceqfpUtilOutputPriorityPktRate = _CeqfpUtilOutputPriorityPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 8),
    _CeqfpUtilOutputPriorityPktRate_Type()
)
ceqfpUtilOutputPriorityPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpUtilOutputPriorityPktRate.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpUtilOutputPriorityPktRate.setUnits("packets per second")
_CeqfpUtilOutputPriorityBitRate_Type = CiscoQfpBitRate
_CeqfpUtilOutputPriorityBitRate_Object = MibTableColumn
ceqfpUtilOutputPriorityBitRate = _CeqfpUtilOutputPriorityBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 9),
    _CeqfpUtilOutputPriorityBitRate_Type()
)
ceqfpUtilOutputPriorityBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpUtilOutputPriorityBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpUtilOutputPriorityBitRate.setUnits("bits per second")
_CeqfpUtilOutputNonPriorityPktRate_Type = CiscoQfpPacketRate
_CeqfpUtilOutputNonPriorityPktRate_Object = MibTableColumn
ceqfpUtilOutputNonPriorityPktRate = _CeqfpUtilOutputNonPriorityPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 10),
    _CeqfpUtilOutputNonPriorityPktRate_Type()
)
ceqfpUtilOutputNonPriorityPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpUtilOutputNonPriorityPktRate.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpUtilOutputNonPriorityPktRate.setUnits("packets per second")
_CeqfpUtilOutputNonPriorityBitRate_Type = CiscoQfpBitRate
_CeqfpUtilOutputNonPriorityBitRate_Object = MibTableColumn
ceqfpUtilOutputNonPriorityBitRate = _CeqfpUtilOutputNonPriorityBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 11),
    _CeqfpUtilOutputNonPriorityBitRate_Type()
)
ceqfpUtilOutputNonPriorityBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpUtilOutputNonPriorityBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpUtilOutputNonPriorityBitRate.setUnits("bits per second")
_CeqfpUtilOutputTotalPktRate_Type = CiscoQfpPacketRate
_CeqfpUtilOutputTotalPktRate_Object = MibTableColumn
ceqfpUtilOutputTotalPktRate = _CeqfpUtilOutputTotalPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 12),
    _CeqfpUtilOutputTotalPktRate_Type()
)
ceqfpUtilOutputTotalPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpUtilOutputTotalPktRate.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpUtilOutputTotalPktRate.setUnits("packets per second")
_CeqfpUtilOutputTotalBitRate_Type = CiscoQfpBitRate
_CeqfpUtilOutputTotalBitRate_Object = MibTableColumn
ceqfpUtilOutputTotalBitRate = _CeqfpUtilOutputTotalBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 13),
    _CeqfpUtilOutputTotalBitRate_Type()
)
ceqfpUtilOutputTotalBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpUtilOutputTotalBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpUtilOutputTotalBitRate.setUnits("bits per second")


class _CeqfpUtilProcessingLoad_Type(Gauge32):
    """Custom type ceqfpUtilProcessingLoad based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CeqfpUtilProcessingLoad_Type.__name__ = "Gauge32"
_CeqfpUtilProcessingLoad_Object = MibTableColumn
ceqfpUtilProcessingLoad = _CeqfpUtilProcessingLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 6, 1, 14),
    _CeqfpUtilProcessingLoad_Type()
)
ceqfpUtilProcessingLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpUtilProcessingLoad.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpUtilProcessingLoad.setUnits("percent")
_CeqfpMemoryResourceTable_Object = MibTable
ceqfpMemoryResourceTable = _CeqfpMemoryResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ceqfpMemoryResourceTable.setStatus("current")
_CeqfpMemoryResourceEntry_Object = MibTableRow
ceqfpMemoryResourceEntry = _CeqfpMemoryResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1)
)
ceqfpMemoryResourceEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResType"),
)
if mibBuilder.loadTexts:
    ceqfpMemoryResourceEntry.setStatus("current")
_CeqfpMemoryResType_Type = CiscoQfpMemoryResource
_CeqfpMemoryResType_Object = MibTableColumn
ceqfpMemoryResType = _CeqfpMemoryResType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 1),
    _CeqfpMemoryResType_Type()
)
ceqfpMemoryResType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceqfpMemoryResType.setStatus("current")
_CeqfpMemoryResTotal_Type = Gauge32
_CeqfpMemoryResTotal_Object = MibTableColumn
ceqfpMemoryResTotal = _CeqfpMemoryResTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 2),
    _CeqfpMemoryResTotal_Type()
)
ceqfpMemoryResTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpMemoryResTotal.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpMemoryResTotal.setUnits("kilo bytes")
_CeqfpMemoryResInUse_Type = Gauge32
_CeqfpMemoryResInUse_Object = MibTableColumn
ceqfpMemoryResInUse = _CeqfpMemoryResInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 3),
    _CeqfpMemoryResInUse_Type()
)
ceqfpMemoryResInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpMemoryResInUse.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpMemoryResInUse.setUnits("kilo bytes")
_CeqfpMemoryResFree_Type = Gauge32
_CeqfpMemoryResFree_Object = MibTableColumn
ceqfpMemoryResFree = _CeqfpMemoryResFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 4),
    _CeqfpMemoryResFree_Type()
)
ceqfpMemoryResFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpMemoryResFree.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpMemoryResFree.setUnits("kilo bytes")
_CeqfpMemoryResLowFreeWatermark_Type = Gauge32
_CeqfpMemoryResLowFreeWatermark_Object = MibTableColumn
ceqfpMemoryResLowFreeWatermark = _CeqfpMemoryResLowFreeWatermark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 5),
    _CeqfpMemoryResLowFreeWatermark_Type()
)
ceqfpMemoryResLowFreeWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpMemoryResLowFreeWatermark.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpMemoryResLowFreeWatermark.setUnits("kilo bytes")


class _CeqfpMemoryResRisingThreshold_Type(Unsigned32):
    """Custom type ceqfpMemoryResRisingThreshold based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CeqfpMemoryResRisingThreshold_Type.__name__ = "Unsigned32"
_CeqfpMemoryResRisingThreshold_Object = MibTableColumn
ceqfpMemoryResRisingThreshold = _CeqfpMemoryResRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 6),
    _CeqfpMemoryResRisingThreshold_Type()
)
ceqfpMemoryResRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceqfpMemoryResRisingThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpMemoryResRisingThreshold.setUnits("percent")


class _CeqfpMemoryResFallingThreshold_Type(Unsigned32):
    """Custom type ceqfpMemoryResFallingThreshold based on Unsigned32"""
    defaultValue = 85

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CeqfpMemoryResFallingThreshold_Type.__name__ = "Unsigned32"
_CeqfpMemoryResFallingThreshold_Object = MibTableColumn
ceqfpMemoryResFallingThreshold = _CeqfpMemoryResFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 7),
    _CeqfpMemoryResFallingThreshold_Type()
)
ceqfpMemoryResFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceqfpMemoryResFallingThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpMemoryResFallingThreshold.setUnits("percent")
_CeqfpMemoryResTotalOvrflw_Type = Gauge32
_CeqfpMemoryResTotalOvrflw_Object = MibTableColumn
ceqfpMemoryResTotalOvrflw = _CeqfpMemoryResTotalOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 8),
    _CeqfpMemoryResTotalOvrflw_Type()
)
ceqfpMemoryResTotalOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpMemoryResTotalOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpMemoryResTotalOvrflw.setUnits("kilo bytes")
_CeqfpMemoryHCResTotal_Type = CounterBasedGauge64
_CeqfpMemoryHCResTotal_Object = MibTableColumn
ceqfpMemoryHCResTotal = _CeqfpMemoryHCResTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 9),
    _CeqfpMemoryHCResTotal_Type()
)
ceqfpMemoryHCResTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpMemoryHCResTotal.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpMemoryHCResTotal.setUnits("kilo bytes")
_CeqfpMemoryResInUseOvrflw_Type = Gauge32
_CeqfpMemoryResInUseOvrflw_Object = MibTableColumn
ceqfpMemoryResInUseOvrflw = _CeqfpMemoryResInUseOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 10),
    _CeqfpMemoryResInUseOvrflw_Type()
)
ceqfpMemoryResInUseOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpMemoryResInUseOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpMemoryResInUseOvrflw.setUnits("kilo bytes")
_CeqfpMemoryHCResInUse_Type = CounterBasedGauge64
_CeqfpMemoryHCResInUse_Object = MibTableColumn
ceqfpMemoryHCResInUse = _CeqfpMemoryHCResInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 11),
    _CeqfpMemoryHCResInUse_Type()
)
ceqfpMemoryHCResInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpMemoryHCResInUse.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpMemoryHCResInUse.setUnits("kilo bytes")
_CeqfpMemoryResFreeOvrflw_Type = Gauge32
_CeqfpMemoryResFreeOvrflw_Object = MibTableColumn
ceqfpMemoryResFreeOvrflw = _CeqfpMemoryResFreeOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 12),
    _CeqfpMemoryResFreeOvrflw_Type()
)
ceqfpMemoryResFreeOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpMemoryResFreeOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpMemoryResFreeOvrflw.setUnits("kilo bytes")
_CeqfpMemoryHCResFree_Type = CounterBasedGauge64
_CeqfpMemoryHCResFree_Object = MibTableColumn
ceqfpMemoryHCResFree = _CeqfpMemoryHCResFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 13),
    _CeqfpMemoryHCResFree_Type()
)
ceqfpMemoryHCResFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpMemoryHCResFree.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpMemoryHCResFree.setUnits("kilo bytes")
_CeqfpMemoryResLowFreeWatermarkOvrflw_Type = Gauge32
_CeqfpMemoryResLowFreeWatermarkOvrflw_Object = MibTableColumn
ceqfpMemoryResLowFreeWatermarkOvrflw = _CeqfpMemoryResLowFreeWatermarkOvrflw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 14),
    _CeqfpMemoryResLowFreeWatermarkOvrflw_Type()
)
ceqfpMemoryResLowFreeWatermarkOvrflw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpMemoryResLowFreeWatermarkOvrflw.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpMemoryResLowFreeWatermarkOvrflw.setUnits("kilo bytes")
_CeqfpMemoryHCResLowFreeWatermark_Type = CounterBasedGauge64
_CeqfpMemoryHCResLowFreeWatermark_Object = MibTableColumn
ceqfpMemoryHCResLowFreeWatermark = _CeqfpMemoryHCResLowFreeWatermark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 7, 1, 15),
    _CeqfpMemoryHCResLowFreeWatermark_Type()
)
ceqfpMemoryHCResLowFreeWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpMemoryHCResLowFreeWatermark.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpMemoryHCResLowFreeWatermark.setUnits("kilo bytes")
_CeqfpThroughputTable_Object = MibTable
ceqfpThroughputTable = _CeqfpThroughputTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 8)
)
if mibBuilder.loadTexts:
    ceqfpThroughputTable.setStatus("current")
_CeqfpThroughputEntry_Object = MibTableRow
ceqfpThroughputEntry = _CeqfpThroughputEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 8, 1)
)
ceqfpThroughputEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ceqfpThroughputEntry.setStatus("current")
_CeqfpThroughputLicensedBW_Type = Counter64
_CeqfpThroughputLicensedBW_Object = MibTableColumn
ceqfpThroughputLicensedBW = _CeqfpThroughputLicensedBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 8, 1, 1),
    _CeqfpThroughputLicensedBW_Type()
)
ceqfpThroughputLicensedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpThroughputLicensedBW.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpThroughputLicensedBW.setUnits("bits per second")


class _CeqfpThroughputLevel_Type(Integer32):
    """Custom type ceqfpThroughputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exceed", 3),
          ("normal", 1),
          ("warning", 2))
    )


_CeqfpThroughputLevel_Type.__name__ = "Integer32"
_CeqfpThroughputLevel_Object = MibTableColumn
ceqfpThroughputLevel = _CeqfpThroughputLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 8, 1, 2),
    _CeqfpThroughputLevel_Type()
)
ceqfpThroughputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpThroughputLevel.setStatus("current")


class _CeqfpThroughputInterval_Type(Integer32):
    """Custom type ceqfpThroughputInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_CeqfpThroughputInterval_Type.__name__ = "Integer32"
_CeqfpThroughputInterval_Object = MibTableColumn
ceqfpThroughputInterval = _CeqfpThroughputInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 8, 1, 3),
    _CeqfpThroughputInterval_Type()
)
ceqfpThroughputInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceqfpThroughputInterval.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpThroughputInterval.setUnits("seconds")


class _CeqfpThroughputThreshold_Type(Integer32):
    """Custom type ceqfpThroughputThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 95),
    )


_CeqfpThroughputThreshold_Type.__name__ = "Integer32"
_CeqfpThroughputThreshold_Object = MibTableColumn
ceqfpThroughputThreshold = _CeqfpThroughputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 8, 1, 4),
    _CeqfpThroughputThreshold_Type()
)
ceqfpThroughputThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceqfpThroughputThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpThroughputThreshold.setUnits("percent")
_CeqfpThroughputAvgRate_Type = Counter64
_CeqfpThroughputAvgRate_Object = MibTableColumn
ceqfpThroughputAvgRate = _CeqfpThroughputAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 1, 8, 1, 5),
    _CeqfpThroughputAvgRate_Type()
)
ceqfpThroughputAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceqfpThroughputAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpThroughputAvgRate.setUnits("bits per second")
_CiscoEntityQfpNotif_ObjectIdentity = ObjectIdentity
ciscoEntityQfpNotif = _CiscoEntityQfpNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 2)
)


class _CeqfpMemoryResThreshNotifEnabled_Type(TruthValue):
    """Custom type ceqfpMemoryResThreshNotifEnabled based on TruthValue"""


_CeqfpMemoryResThreshNotifEnabled_Object = MibScalar
ceqfpMemoryResThreshNotifEnabled = _CeqfpMemoryResThreshNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 2, 1),
    _CeqfpMemoryResThreshNotifEnabled_Type()
)
ceqfpMemoryResThreshNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceqfpMemoryResThreshNotifEnabled.setStatus("current")


class _CeqfpMemoryResCurrentRisingThresh_Type(Unsigned32):
    """Custom type ceqfpMemoryResCurrentRisingThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CeqfpMemoryResCurrentRisingThresh_Type.__name__ = "Unsigned32"
_CeqfpMemoryResCurrentRisingThresh_Object = MibScalar
ceqfpMemoryResCurrentRisingThresh = _CeqfpMemoryResCurrentRisingThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 2, 2),
    _CeqfpMemoryResCurrentRisingThresh_Type()
)
ceqfpMemoryResCurrentRisingThresh.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ceqfpMemoryResCurrentRisingThresh.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpMemoryResCurrentRisingThresh.setUnits("percent")
_CeqfpMemoryResCurrentFallingThresh_Type = Unsigned32
_CeqfpMemoryResCurrentFallingThresh_Object = MibScalar
ceqfpMemoryResCurrentFallingThresh = _CeqfpMemoryResCurrentFallingThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 2, 3),
    _CeqfpMemoryResCurrentFallingThresh_Type()
)
ceqfpMemoryResCurrentFallingThresh.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ceqfpMemoryResCurrentFallingThresh.setStatus("current")
if mibBuilder.loadTexts:
    ceqfpMemoryResCurrentFallingThresh.setUnits("percent")


class _CeqfpThroughputNotifEnabled_Type(TruthValue):
    """Custom type ceqfpThroughputNotifEnabled based on TruthValue"""


_CeqfpThroughputNotifEnabled_Object = MibScalar
ceqfpThroughputNotifEnabled = _CeqfpThroughputNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 1, 2, 4),
    _CeqfpThroughputNotifEnabled_Type()
)
ceqfpThroughputNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceqfpThroughputNotifEnabled.setStatus("current")
_CiscoEntityQfpMIBConform_ObjectIdentity = ObjectIdentity
ciscoEntityQfpMIBConform = _CiscoEntityQfpMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 2)
)
_CiscoEntityQfpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEntityQfpMIBCompliances = _CiscoEntityQfpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 1)
)
_CiscoEntityQfpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEntityQfpMIBGroups = _CiscoEntityQfpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2)
)

# Managed Objects groups

ciscoEntityQfpSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 1)
)
ciscoEntityQfpSystemGroup.setObjects(
      *(("CISCO-ENTITY-QFP-MIB", "ceqfpSystemTrafficDirection"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpSystemState"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpNumberSystemLoads"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpSystemLastLoadTime"))
)
if mibBuilder.loadTexts:
    ciscoEntityQfpSystemGroup.setStatus("current")

ciscoEntityQfpUtilizationAlgoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 2)
)
ciscoEntityQfpUtilizationAlgoGroup.setObjects(
      *(("CISCO-ENTITY-QFP-MIB", "ceqfpFiveSecondUtilAlgo"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpOneMinuteUtilAlgo"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpFiveMinutesUtilAlgo"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpSixtyMinutesUtilAlgo"))
)
if mibBuilder.loadTexts:
    ciscoEntityQfpUtilizationAlgoGroup.setStatus("current")

ciscoEntityQfpUtilizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 3)
)
ciscoEntityQfpUtilizationGroup.setObjects(
      *(("CISCO-ENTITY-QFP-MIB", "ceqfpUtilInputPriorityPktRate"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilInputPriorityBitRate"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilInputNonPriorityPktRate"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilInputNonPriorityBitRate"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilInputTotalPktRate"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilInputTotalBitRate"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilOutputPriorityPktRate"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilOutputPriorityBitRate"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilOutputNonPriorityPktRate"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilOutputNonPriorityBitRate"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilOutputTotalPktRate"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilOutputTotalBitRate"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpUtilProcessingLoad"))
)
if mibBuilder.loadTexts:
    ciscoEntityQfpUtilizationGroup.setStatus("current")

ciscoEntityQfpMemoryResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 4)
)
ciscoEntityQfpMemoryResourceGroup.setObjects(
      *(("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResTotal"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResInUse"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResFree"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResLowFreeWatermark"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResRisingThreshold"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResFallingThreshold"))
)
if mibBuilder.loadTexts:
    ciscoEntityQfpMemoryResourceGroup.setStatus("current")

ciscoEntityQfpMemoryResNotifGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 6)
)
ciscoEntityQfpMemoryResNotifGroup.setObjects(
      *(("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResThreshNotifEnabled"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResCurrentRisingThresh"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResCurrentFallingThresh"))
)
if mibBuilder.loadTexts:
    ciscoEntityQfpMemoryResNotifGroup.setStatus("current")

ciscoEntityQfpMemoryResourceOvrflwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 7)
)
ciscoEntityQfpMemoryResourceOvrflwGroup.setObjects(
      *(("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResTotalOvrflw"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResInUseOvrflw"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResFreeOvrflw"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResLowFreeWatermarkOvrflw"))
)
if mibBuilder.loadTexts:
    ciscoEntityQfpMemoryResourceOvrflwGroup.setStatus("current")

ciscoEntityQfpMemoryHCResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 8)
)
ciscoEntityQfpMemoryHCResourceGroup.setObjects(
      *(("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryHCResTotal"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryHCResInUse"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryHCResFree"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryHCResLowFreeWatermark"))
)
if mibBuilder.loadTexts:
    ciscoEntityQfpMemoryHCResourceGroup.setStatus("current")

ceqfpThroughputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 9)
)
ceqfpThroughputGroup.setObjects(
      *(("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputLicensedBW"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputLevel"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputInterval"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputThreshold"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputAvgRate"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputNotifEnabled"))
)
if mibBuilder.loadTexts:
    ceqfpThroughputGroup.setStatus("current")


# Notification objects

ceqfpMemoryResRisingThreshNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 0, 1)
)
ceqfpMemoryResRisingThreshNotif.setObjects(
      *(("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResInUse"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResCurrentRisingThresh"))
)
if mibBuilder.loadTexts:
    ceqfpMemoryResRisingThreshNotif.setStatus(
        "current"
    )

ceqfpMemoryResFallingThreshNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 0, 2)
)
ceqfpMemoryResFallingThreshNotif.setObjects(
      *(("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResInUse"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResCurrentFallingThresh"))
)
if mibBuilder.loadTexts:
    ceqfpMemoryResFallingThreshNotif.setStatus(
        "current"
    )

ceqfpThroughputNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 0, 3)
)
ceqfpThroughputNotif.setObjects(
      *(("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputLicensedBW"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputLevel"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputAvgRate"))
)
if mibBuilder.loadTexts:
    ceqfpThroughputNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoEntityQfpNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 2, 5)
)
ciscoEntityQfpNotifGroup.setObjects(
      *(("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResRisingThreshNotif"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpMemoryResFallingThreshNotif"),
        ("CISCO-ENTITY-QFP-MIB", "ceqfpThroughputNotif"))
)
if mibBuilder.loadTexts:
    ciscoEntityQfpNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoEntityQfpMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoEntityQfpMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoEntityQfpMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 715, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoEntityQfpMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-QFP-MIB",
    **{"CiscoQfpPacketRate": CiscoQfpPacketRate,
       "CiscoQfpBitRate": CiscoQfpBitRate,
       "CiscoQfpTimeInterval": CiscoQfpTimeInterval,
       "CiscoQfpMemoryResource": CiscoQfpMemoryResource,
       "ciscoEntityQfpMIB": ciscoEntityQfpMIB,
       "ciscoEntityQfpMIBNotifs": ciscoEntityQfpMIBNotifs,
       "ceqfpMemoryResRisingThreshNotif": ceqfpMemoryResRisingThreshNotif,
       "ceqfpMemoryResFallingThreshNotif": ceqfpMemoryResFallingThreshNotif,
       "ceqfpThroughputNotif": ceqfpThroughputNotif,
       "ciscoEntityQfpMIBObjects": ciscoEntityQfpMIBObjects,
       "ciscoEntityQfp": ciscoEntityQfp,
       "ceqfpSystemTable": ceqfpSystemTable,
       "ceqfpSystemEntry": ceqfpSystemEntry,
       "ceqfpSystemTrafficDirection": ceqfpSystemTrafficDirection,
       "ceqfpSystemState": ceqfpSystemState,
       "ceqfpNumberSystemLoads": ceqfpNumberSystemLoads,
       "ceqfpSystemLastLoadTime": ceqfpSystemLastLoadTime,
       "ceqfpFiveSecondUtilAlgo": ceqfpFiveSecondUtilAlgo,
       "ceqfpOneMinuteUtilAlgo": ceqfpOneMinuteUtilAlgo,
       "ceqfpFiveMinutesUtilAlgo": ceqfpFiveMinutesUtilAlgo,
       "ceqfpSixtyMinutesUtilAlgo": ceqfpSixtyMinutesUtilAlgo,
       "ceqfpUtilizationTable": ceqfpUtilizationTable,
       "ceqfpUtilizationEntry": ceqfpUtilizationEntry,
       "ceqfpUtilTimeInterval": ceqfpUtilTimeInterval,
       "ceqfpUtilInputPriorityPktRate": ceqfpUtilInputPriorityPktRate,
       "ceqfpUtilInputPriorityBitRate": ceqfpUtilInputPriorityBitRate,
       "ceqfpUtilInputNonPriorityPktRate": ceqfpUtilInputNonPriorityPktRate,
       "ceqfpUtilInputNonPriorityBitRate": ceqfpUtilInputNonPriorityBitRate,
       "ceqfpUtilInputTotalPktRate": ceqfpUtilInputTotalPktRate,
       "ceqfpUtilInputTotalBitRate": ceqfpUtilInputTotalBitRate,
       "ceqfpUtilOutputPriorityPktRate": ceqfpUtilOutputPriorityPktRate,
       "ceqfpUtilOutputPriorityBitRate": ceqfpUtilOutputPriorityBitRate,
       "ceqfpUtilOutputNonPriorityPktRate": ceqfpUtilOutputNonPriorityPktRate,
       "ceqfpUtilOutputNonPriorityBitRate": ceqfpUtilOutputNonPriorityBitRate,
       "ceqfpUtilOutputTotalPktRate": ceqfpUtilOutputTotalPktRate,
       "ceqfpUtilOutputTotalBitRate": ceqfpUtilOutputTotalBitRate,
       "ceqfpUtilProcessingLoad": ceqfpUtilProcessingLoad,
       "ceqfpMemoryResourceTable": ceqfpMemoryResourceTable,
       "ceqfpMemoryResourceEntry": ceqfpMemoryResourceEntry,
       "ceqfpMemoryResType": ceqfpMemoryResType,
       "ceqfpMemoryResTotal": ceqfpMemoryResTotal,
       "ceqfpMemoryResInUse": ceqfpMemoryResInUse,
       "ceqfpMemoryResFree": ceqfpMemoryResFree,
       "ceqfpMemoryResLowFreeWatermark": ceqfpMemoryResLowFreeWatermark,
       "ceqfpMemoryResRisingThreshold": ceqfpMemoryResRisingThreshold,
       "ceqfpMemoryResFallingThreshold": ceqfpMemoryResFallingThreshold,
       "ceqfpMemoryResTotalOvrflw": ceqfpMemoryResTotalOvrflw,
       "ceqfpMemoryHCResTotal": ceqfpMemoryHCResTotal,
       "ceqfpMemoryResInUseOvrflw": ceqfpMemoryResInUseOvrflw,
       "ceqfpMemoryHCResInUse": ceqfpMemoryHCResInUse,
       "ceqfpMemoryResFreeOvrflw": ceqfpMemoryResFreeOvrflw,
       "ceqfpMemoryHCResFree": ceqfpMemoryHCResFree,
       "ceqfpMemoryResLowFreeWatermarkOvrflw": ceqfpMemoryResLowFreeWatermarkOvrflw,
       "ceqfpMemoryHCResLowFreeWatermark": ceqfpMemoryHCResLowFreeWatermark,
       "ceqfpThroughputTable": ceqfpThroughputTable,
       "ceqfpThroughputEntry": ceqfpThroughputEntry,
       "ceqfpThroughputLicensedBW": ceqfpThroughputLicensedBW,
       "ceqfpThroughputLevel": ceqfpThroughputLevel,
       "ceqfpThroughputInterval": ceqfpThroughputInterval,
       "ceqfpThroughputThreshold": ceqfpThroughputThreshold,
       "ceqfpThroughputAvgRate": ceqfpThroughputAvgRate,
       "ciscoEntityQfpNotif": ciscoEntityQfpNotif,
       "ceqfpMemoryResThreshNotifEnabled": ceqfpMemoryResThreshNotifEnabled,
       "ceqfpMemoryResCurrentRisingThresh": ceqfpMemoryResCurrentRisingThresh,
       "ceqfpMemoryResCurrentFallingThresh": ceqfpMemoryResCurrentFallingThresh,
       "ceqfpThroughputNotifEnabled": ceqfpThroughputNotifEnabled,
       "ciscoEntityQfpMIBConform": ciscoEntityQfpMIBConform,
       "ciscoEntityQfpMIBCompliances": ciscoEntityQfpMIBCompliances,
       "ciscoEntityQfpMIBComplianceRev1": ciscoEntityQfpMIBComplianceRev1,
       "ciscoEntityQfpMIBComplianceRev2": ciscoEntityQfpMIBComplianceRev2,
       "ciscoEntityQfpMIBGroups": ciscoEntityQfpMIBGroups,
       "ciscoEntityQfpSystemGroup": ciscoEntityQfpSystemGroup,
       "ciscoEntityQfpUtilizationAlgoGroup": ciscoEntityQfpUtilizationAlgoGroup,
       "ciscoEntityQfpUtilizationGroup": ciscoEntityQfpUtilizationGroup,
       "ciscoEntityQfpMemoryResourceGroup": ciscoEntityQfpMemoryResourceGroup,
       "ciscoEntityQfpNotifGroup": ciscoEntityQfpNotifGroup,
       "ciscoEntityQfpMemoryResNotifGroup": ciscoEntityQfpMemoryResNotifGroup,
       "ciscoEntityQfpMemoryResourceOvrflwGroup": ciscoEntityQfpMemoryResourceOvrflwGroup,
       "ciscoEntityQfpMemoryHCResourceGroup": ciscoEntityQfpMemoryHCResourceGroup,
       "ceqfpThroughputGroup": ceqfpThroughputGroup}
)
