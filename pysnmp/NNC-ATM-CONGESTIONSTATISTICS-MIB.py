# SNMP MIB module (NNC-ATM-CONGESTIONSTATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNC-ATM-CONGESTIONSTATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:09 2024
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(NncExtIntvlStateType,) = mibBuilder.importSymbols(
    "NNC-INTERVAL-STATISTICS-TC-MIB",
    "NncExtIntvlStateType")

(NncExtCounter64,
 nncExtensions) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "NncExtCounter64",
    "nncExtensions")

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

nncAtmCongestionStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 63)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncAtmCongStatsObjects_ObjectIdentity = ObjectIdentity
nncAtmCongStatsObjects = _NncAtmCongStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1)
)
_NncAtmCongPointInfoTable_Object = MibTable
nncAtmCongPointInfoTable = _NncAtmCongPointInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 1)
)
if mibBuilder.loadTexts:
    nncAtmCongPointInfoTable.setStatus("current")
_NncAtmCongPointInfoEntry_Object = MibTableRow
nncAtmCongPointInfoEntry = _NncAtmCongPointInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 1, 1)
)
nncAtmCongPointInfoEntry.setIndexNames(
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "entPhysicalEntityInfoIndex"),
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongPointInfoIndex"),
)
if mibBuilder.loadTexts:
    nncAtmCongPointInfoEntry.setStatus("current")
_EntPhysicalEntityInfoIndex_Type = PhysicalIndex
_EntPhysicalEntityInfoIndex_Object = MibTableColumn
entPhysicalEntityInfoIndex = _EntPhysicalEntityInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 1, 1, 1),
    _EntPhysicalEntityInfoIndex_Type()
)
entPhysicalEntityInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    entPhysicalEntityInfoIndex.setStatus("current")


class _NncAtmCongPointInfoIndex_Type(Integer32):
    """Custom type nncAtmCongPointInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NncAtmCongPointInfoIndex_Type.__name__ = "Integer32"
_NncAtmCongPointInfoIndex_Object = MibTableColumn
nncAtmCongPointInfoIndex = _NncAtmCongPointInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 1, 1, 2),
    _NncAtmCongPointInfoIndex_Type()
)
nncAtmCongPointInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncAtmCongPointInfoIndex.setStatus("current")


class _NncAtmCongPointHardwareType_Type(Integer32):
    """Custom type nncAtmCongPointHardwareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_NncAtmCongPointHardwareType_Type.__name__ = "Integer32"
_NncAtmCongPointHardwareType_Object = MibTableColumn
nncAtmCongPointHardwareType = _NncAtmCongPointHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 1, 1, 3),
    _NncAtmCongPointHardwareType_Type()
)
nncAtmCongPointHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongPointHardwareType.setStatus("current")
_NncAtmCongStatsRawTable_Object = MibTable
nncAtmCongStatsRawTable = _NncAtmCongStatsRawTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 2)
)
if mibBuilder.loadTexts:
    nncAtmCongStatsRawTable.setStatus("current")
_NncAtmCongStatsRawEntry_Object = MibTableRow
nncAtmCongStatsRawEntry = _NncAtmCongStatsRawEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 2, 1)
)
nncAtmCongStatsRawEntry.setIndexNames(
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "entPhysicalEntityRawIndex"),
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongPointRawIndex"),
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsQOSRawIndex"),
)
if mibBuilder.loadTexts:
    nncAtmCongStatsRawEntry.setStatus("current")
_EntPhysicalEntityRawIndex_Type = PhysicalIndex
_EntPhysicalEntityRawIndex_Object = MibTableColumn
entPhysicalEntityRawIndex = _EntPhysicalEntityRawIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 2, 1, 1),
    _EntPhysicalEntityRawIndex_Type()
)
entPhysicalEntityRawIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    entPhysicalEntityRawIndex.setStatus("current")


class _NncAtmCongPointRawIndex_Type(Integer32):
    """Custom type nncAtmCongPointRawIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NncAtmCongPointRawIndex_Type.__name__ = "Integer32"
_NncAtmCongPointRawIndex_Object = MibTableColumn
nncAtmCongPointRawIndex = _NncAtmCongPointRawIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 2, 1, 2),
    _NncAtmCongPointRawIndex_Type()
)
nncAtmCongPointRawIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncAtmCongPointRawIndex.setStatus("current")


class _NncAtmCongStatsQOSRawIndex_Type(Integer32):
    """Custom type nncAtmCongStatsQOSRawIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_NncAtmCongStatsQOSRawIndex_Type.__name__ = "Integer32"
_NncAtmCongStatsQOSRawIndex_Object = MibTableColumn
nncAtmCongStatsQOSRawIndex = _NncAtmCongStatsQOSRawIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 2, 1, 3),
    _NncAtmCongStatsQOSRawIndex_Type()
)
nncAtmCongStatsQOSRawIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncAtmCongStatsQOSRawIndex.setStatus("current")
_NncAtmCongStatsTotalCellsArrived_Type = NncExtCounter64
_NncAtmCongStatsTotalCellsArrived_Object = MibTableColumn
nncAtmCongStatsTotalCellsArrived = _NncAtmCongStatsTotalCellsArrived_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 2, 1, 4),
    _NncAtmCongStatsTotalCellsArrived_Type()
)
nncAtmCongStatsTotalCellsArrived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsTotalCellsArrived.setStatus("current")
_NncAtmCongStatsTotalCellsDiscarded_Type = NncExtCounter64
_NncAtmCongStatsTotalCellsDiscarded_Object = MibTableColumn
nncAtmCongStatsTotalCellsDiscarded = _NncAtmCongStatsTotalCellsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 2, 1, 5),
    _NncAtmCongStatsTotalCellsDiscarded_Type()
)
nncAtmCongStatsTotalCellsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsTotalCellsDiscarded.setStatus("current")
_NncAtmCongStatsClp0CellsDiscarded_Type = NncExtCounter64
_NncAtmCongStatsClp0CellsDiscarded_Object = MibTableColumn
nncAtmCongStatsClp0CellsDiscarded = _NncAtmCongStatsClp0CellsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 2, 1, 6),
    _NncAtmCongStatsClp0CellsDiscarded_Type()
)
nncAtmCongStatsClp0CellsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsClp0CellsDiscarded.setStatus("current")
_NncAtmCongStatsLowCongestedSeconds_Type = Counter32
_NncAtmCongStatsLowCongestedSeconds_Object = MibTableColumn
nncAtmCongStatsLowCongestedSeconds = _NncAtmCongStatsLowCongestedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 2, 1, 7),
    _NncAtmCongStatsLowCongestedSeconds_Type()
)
nncAtmCongStatsLowCongestedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsLowCongestedSeconds.setStatus("current")
_NncAtmCongStatsMediumCongestedSeconds_Type = Counter32
_NncAtmCongStatsMediumCongestedSeconds_Object = MibTableColumn
nncAtmCongStatsMediumCongestedSeconds = _NncAtmCongStatsMediumCongestedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 2, 1, 8),
    _NncAtmCongStatsMediumCongestedSeconds_Type()
)
nncAtmCongStatsMediumCongestedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsMediumCongestedSeconds.setStatus("current")
_NncAtmCongStatsSevereCongestedSeconds_Type = Counter32
_NncAtmCongStatsSevereCongestedSeconds_Object = MibTableColumn
nncAtmCongStatsSevereCongestedSeconds = _NncAtmCongStatsSevereCongestedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 2, 1, 9),
    _NncAtmCongStatsSevereCongestedSeconds_Type()
)
nncAtmCongStatsSevereCongestedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsSevereCongestedSeconds.setStatus("current")
_NncAtmCongStatsTotalSeconds_Type = Counter32
_NncAtmCongStatsTotalSeconds_Object = MibTableColumn
nncAtmCongStatsTotalSeconds = _NncAtmCongStatsTotalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 2, 1, 10),
    _NncAtmCongStatsTotalSeconds_Type()
)
nncAtmCongStatsTotalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsTotalSeconds.setStatus("current")


class _NncAtmCongStatsCurrentCongestionState_Type(Integer32):
    """Custom type nncAtmCongStatsCurrentCongestionState based on Integer32"""
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
        *(("congStatsLowCongState", 2),
          ("congStatsMediumCongState", 3),
          ("congStatsNormalState", 1),
          ("congStatsSevereCongState", 4))
    )


_NncAtmCongStatsCurrentCongestionState_Type.__name__ = "Integer32"
_NncAtmCongStatsCurrentCongestionState_Object = MibTableColumn
nncAtmCongStatsCurrentCongestionState = _NncAtmCongStatsCurrentCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 2, 1, 11),
    _NncAtmCongStatsCurrentCongestionState_Type()
)
nncAtmCongStatsCurrentCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentCongestionState.setStatus("current")


class _NncAtmCongStatsAlarmStatus_Type(Integer32):
    """Custom type nncAtmCongStatsAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("congStatsAlarmOff", 2),
          ("congStatsAlarmOn", 1))
    )


_NncAtmCongStatsAlarmStatus_Type.__name__ = "Integer32"
_NncAtmCongStatsAlarmStatus_Object = MibTableColumn
nncAtmCongStatsAlarmStatus = _NncAtmCongStatsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 2, 1, 12),
    _NncAtmCongStatsAlarmStatus_Type()
)
nncAtmCongStatsAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsAlarmStatus.setStatus("current")
_NncAtmCongStatsVirtualBandwidthAvail_Type = Counter32
_NncAtmCongStatsVirtualBandwidthAvail_Object = MibTableColumn
nncAtmCongStatsVirtualBandwidthAvail = _NncAtmCongStatsVirtualBandwidthAvail_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 2, 1, 13),
    _NncAtmCongStatsVirtualBandwidthAvail_Type()
)
nncAtmCongStatsVirtualBandwidthAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsVirtualBandwidthAvail.setStatus("current")
_NncAtmCongStatsCurrentShortIntvlTable_Object = MibTable
nncAtmCongStatsCurrentShortIntvlTable = _NncAtmCongStatsCurrentShortIntvlTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 3)
)
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentShortIntvlTable.setStatus("current")
_NncAtmCongStatsCurrentShortIntvlEntry_Object = MibTableRow
nncAtmCongStatsCurrentShortIntvlEntry = _NncAtmCongStatsCurrentShortIntvlEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 3, 1)
)
nncAtmCongStatsCurrentShortIntvlEntry.setIndexNames(
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "entPhysicalEntityCurrentShortIntvlIndex"),
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongPointCurrentShortIntvlIndex"),
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsQOSCurrentShortIntvlIndex"),
)
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentShortIntvlEntry.setStatus("current")
_EntPhysicalEntityCurrentShortIntvlIndex_Type = PhysicalIndex
_EntPhysicalEntityCurrentShortIntvlIndex_Object = MibTableColumn
entPhysicalEntityCurrentShortIntvlIndex = _EntPhysicalEntityCurrentShortIntvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 3, 1, 1),
    _EntPhysicalEntityCurrentShortIntvlIndex_Type()
)
entPhysicalEntityCurrentShortIntvlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    entPhysicalEntityCurrentShortIntvlIndex.setStatus("current")


class _NncAtmCongPointCurrentShortIntvlIndex_Type(Integer32):
    """Custom type nncAtmCongPointCurrentShortIntvlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NncAtmCongPointCurrentShortIntvlIndex_Type.__name__ = "Integer32"
_NncAtmCongPointCurrentShortIntvlIndex_Object = MibTableColumn
nncAtmCongPointCurrentShortIntvlIndex = _NncAtmCongPointCurrentShortIntvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 3, 1, 2),
    _NncAtmCongPointCurrentShortIntvlIndex_Type()
)
nncAtmCongPointCurrentShortIntvlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncAtmCongPointCurrentShortIntvlIndex.setStatus("current")


class _NncAtmCongStatsQOSCurrentShortIntvlIndex_Type(Integer32):
    """Custom type nncAtmCongStatsQOSCurrentShortIntvlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_NncAtmCongStatsQOSCurrentShortIntvlIndex_Type.__name__ = "Integer32"
_NncAtmCongStatsQOSCurrentShortIntvlIndex_Object = MibTableColumn
nncAtmCongStatsQOSCurrentShortIntvlIndex = _NncAtmCongStatsQOSCurrentShortIntvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 3, 1, 3),
    _NncAtmCongStatsQOSCurrentShortIntvlIndex_Type()
)
nncAtmCongStatsQOSCurrentShortIntvlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncAtmCongStatsQOSCurrentShortIntvlIndex.setStatus("current")
_NncAtmCongStatsCurrentShortIntvlState_Type = NncExtIntvlStateType
_NncAtmCongStatsCurrentShortIntvlState_Object = MibTableColumn
nncAtmCongStatsCurrentShortIntvlState = _NncAtmCongStatsCurrentShortIntvlState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 3, 1, 4),
    _NncAtmCongStatsCurrentShortIntvlState_Type()
)
nncAtmCongStatsCurrentShortIntvlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentShortIntvlState.setStatus("current")


class _NncAtmCongStatsCurrentShortIntvlAbsoluteIntervalNumber_Type(Integer32):
    """Custom type nncAtmCongStatsCurrentShortIntvlAbsoluteIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncAtmCongStatsCurrentShortIntvlAbsoluteIntervalNumber_Type.__name__ = "Integer32"
_NncAtmCongStatsCurrentShortIntvlAbsoluteIntervalNumber_Object = MibTableColumn
nncAtmCongStatsCurrentShortIntvlAbsoluteIntervalNumber = _NncAtmCongStatsCurrentShortIntvlAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 3, 1, 5),
    _NncAtmCongStatsCurrentShortIntvlAbsoluteIntervalNumber_Type()
)
nncAtmCongStatsCurrentShortIntvlAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentShortIntvlAbsoluteIntervalNumber.setStatus("current")
_NncAtmCongStatsCurrentShortIntvlTotalCellsArrived_Type = NncExtCounter64
_NncAtmCongStatsCurrentShortIntvlTotalCellsArrived_Object = MibTableColumn
nncAtmCongStatsCurrentShortIntvlTotalCellsArrived = _NncAtmCongStatsCurrentShortIntvlTotalCellsArrived_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 3, 1, 6),
    _NncAtmCongStatsCurrentShortIntvlTotalCellsArrived_Type()
)
nncAtmCongStatsCurrentShortIntvlTotalCellsArrived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentShortIntvlTotalCellsArrived.setStatus("current")
_NncAtmCongStatsCurrentShortIntvlTotalCellsDiscarded_Type = NncExtCounter64
_NncAtmCongStatsCurrentShortIntvlTotalCellsDiscarded_Object = MibTableColumn
nncAtmCongStatsCurrentShortIntvlTotalCellsDiscarded = _NncAtmCongStatsCurrentShortIntvlTotalCellsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 3, 1, 7),
    _NncAtmCongStatsCurrentShortIntvlTotalCellsDiscarded_Type()
)
nncAtmCongStatsCurrentShortIntvlTotalCellsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentShortIntvlTotalCellsDiscarded.setStatus("current")
_NncAtmCongStatsCurrentShortIntvlClp0CellsDiscarded_Type = NncExtCounter64
_NncAtmCongStatsCurrentShortIntvlClp0CellsDiscarded_Object = MibTableColumn
nncAtmCongStatsCurrentShortIntvlClp0CellsDiscarded = _NncAtmCongStatsCurrentShortIntvlClp0CellsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 3, 1, 8),
    _NncAtmCongStatsCurrentShortIntvlClp0CellsDiscarded_Type()
)
nncAtmCongStatsCurrentShortIntvlClp0CellsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentShortIntvlClp0CellsDiscarded.setStatus("current")
_NncAtmCongStatsCurrentShortIntvlLowCongestedSeconds_Type = Counter32
_NncAtmCongStatsCurrentShortIntvlLowCongestedSeconds_Object = MibTableColumn
nncAtmCongStatsCurrentShortIntvlLowCongestedSeconds = _NncAtmCongStatsCurrentShortIntvlLowCongestedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 3, 1, 9),
    _NncAtmCongStatsCurrentShortIntvlLowCongestedSeconds_Type()
)
nncAtmCongStatsCurrentShortIntvlLowCongestedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentShortIntvlLowCongestedSeconds.setStatus("current")
_NncAtmCongStatsCurrentShortIntvlMediumCongestedSeconds_Type = Counter32
_NncAtmCongStatsCurrentShortIntvlMediumCongestedSeconds_Object = MibTableColumn
nncAtmCongStatsCurrentShortIntvlMediumCongestedSeconds = _NncAtmCongStatsCurrentShortIntvlMediumCongestedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 3, 1, 10),
    _NncAtmCongStatsCurrentShortIntvlMediumCongestedSeconds_Type()
)
nncAtmCongStatsCurrentShortIntvlMediumCongestedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentShortIntvlMediumCongestedSeconds.setStatus("current")
_NncAtmCongStatsCurrentShortIntvlSevereCongestedSeconds_Type = Counter32
_NncAtmCongStatsCurrentShortIntvlSevereCongestedSeconds_Object = MibTableColumn
nncAtmCongStatsCurrentShortIntvlSevereCongestedSeconds = _NncAtmCongStatsCurrentShortIntvlSevereCongestedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 3, 1, 11),
    _NncAtmCongStatsCurrentShortIntvlSevereCongestedSeconds_Type()
)
nncAtmCongStatsCurrentShortIntvlSevereCongestedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentShortIntvlSevereCongestedSeconds.setStatus("current")
_NncAtmCongStatsCurrentShortIntvlTotalSeconds_Type = Counter32
_NncAtmCongStatsCurrentShortIntvlTotalSeconds_Object = MibTableColumn
nncAtmCongStatsCurrentShortIntvlTotalSeconds = _NncAtmCongStatsCurrentShortIntvlTotalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 3, 1, 12),
    _NncAtmCongStatsCurrentShortIntvlTotalSeconds_Type()
)
nncAtmCongStatsCurrentShortIntvlTotalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentShortIntvlTotalSeconds.setStatus("current")


class _NncAtmCongStatsCurrentShortIntvlCongestionState_Type(Integer32):
    """Custom type nncAtmCongStatsCurrentShortIntvlCongestionState based on Integer32"""
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
        *(("congStatsLowCongState", 2),
          ("congStatsMediumCongState", 3),
          ("congStatsNormalState", 1),
          ("congStatsSevereCongState", 4))
    )


_NncAtmCongStatsCurrentShortIntvlCongestionState_Type.__name__ = "Integer32"
_NncAtmCongStatsCurrentShortIntvlCongestionState_Object = MibTableColumn
nncAtmCongStatsCurrentShortIntvlCongestionState = _NncAtmCongStatsCurrentShortIntvlCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 3, 1, 13),
    _NncAtmCongStatsCurrentShortIntvlCongestionState_Type()
)
nncAtmCongStatsCurrentShortIntvlCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentShortIntvlCongestionState.setStatus("current")


class _NncAtmCongStatsCurrentShortIntvlAlarmStatus_Type(Integer32):
    """Custom type nncAtmCongStatsCurrentShortIntvlAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("congStatsAlarmOff", 2),
          ("congStatsAlarmOn", 1))
    )


_NncAtmCongStatsCurrentShortIntvlAlarmStatus_Type.__name__ = "Integer32"
_NncAtmCongStatsCurrentShortIntvlAlarmStatus_Object = MibTableColumn
nncAtmCongStatsCurrentShortIntvlAlarmStatus = _NncAtmCongStatsCurrentShortIntvlAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 3, 1, 14),
    _NncAtmCongStatsCurrentShortIntvlAlarmStatus_Type()
)
nncAtmCongStatsCurrentShortIntvlAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentShortIntvlAlarmStatus.setStatus("current")
_NncAtmCongStatsShortIntvlTable_Object = MibTable
nncAtmCongStatsShortIntvlTable = _NncAtmCongStatsShortIntvlTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 4)
)
if mibBuilder.loadTexts:
    nncAtmCongStatsShortIntvlTable.setStatus("current")
_NncAtmCongStatsShortIntvlEntry_Object = MibTableRow
nncAtmCongStatsShortIntvlEntry = _NncAtmCongStatsShortIntvlEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 4, 1)
)
nncAtmCongStatsShortIntvlEntry.setIndexNames(
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "entPhysicalEntityShortIntvlIndex"),
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongPointShortIntvlIndex"),
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsQOSShortIntvlIndex"),
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsShortIntvlIntervalIndex"),
)
if mibBuilder.loadTexts:
    nncAtmCongStatsShortIntvlEntry.setStatus("current")
_EntPhysicalEntityShortIntvlIndex_Type = PhysicalIndex
_EntPhysicalEntityShortIntvlIndex_Object = MibTableColumn
entPhysicalEntityShortIntvlIndex = _EntPhysicalEntityShortIntvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 4, 1, 1),
    _EntPhysicalEntityShortIntvlIndex_Type()
)
entPhysicalEntityShortIntvlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    entPhysicalEntityShortIntvlIndex.setStatus("current")


class _NncAtmCongPointShortIntvlIndex_Type(Integer32):
    """Custom type nncAtmCongPointShortIntvlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NncAtmCongPointShortIntvlIndex_Type.__name__ = "Integer32"
_NncAtmCongPointShortIntvlIndex_Object = MibTableColumn
nncAtmCongPointShortIntvlIndex = _NncAtmCongPointShortIntvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 4, 1, 2),
    _NncAtmCongPointShortIntvlIndex_Type()
)
nncAtmCongPointShortIntvlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncAtmCongPointShortIntvlIndex.setStatus("current")


class _NncAtmCongStatsQOSShortIntvlIndex_Type(Integer32):
    """Custom type nncAtmCongStatsQOSShortIntvlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_NncAtmCongStatsQOSShortIntvlIndex_Type.__name__ = "Integer32"
_NncAtmCongStatsQOSShortIntvlIndex_Object = MibTableColumn
nncAtmCongStatsQOSShortIntvlIndex = _NncAtmCongStatsQOSShortIntvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 4, 1, 3),
    _NncAtmCongStatsQOSShortIntvlIndex_Type()
)
nncAtmCongStatsQOSShortIntvlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncAtmCongStatsQOSShortIntvlIndex.setStatus("current")


class _NncAtmCongStatsShortIntvlIntervalIndex_Type(Integer32):
    """Custom type nncAtmCongStatsShortIntvlIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 95),
    )


_NncAtmCongStatsShortIntvlIntervalIndex_Type.__name__ = "Integer32"
_NncAtmCongStatsShortIntvlIntervalIndex_Object = MibTableColumn
nncAtmCongStatsShortIntvlIntervalIndex = _NncAtmCongStatsShortIntvlIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 4, 1, 4),
    _NncAtmCongStatsShortIntvlIntervalIndex_Type()
)
nncAtmCongStatsShortIntvlIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncAtmCongStatsShortIntvlIntervalIndex.setStatus("current")
_NncAtmCongStatsShortIntvlState_Type = NncExtIntvlStateType
_NncAtmCongStatsShortIntvlState_Object = MibTableColumn
nncAtmCongStatsShortIntvlState = _NncAtmCongStatsShortIntvlState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 4, 1, 5),
    _NncAtmCongStatsShortIntvlState_Type()
)
nncAtmCongStatsShortIntvlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsShortIntvlState.setStatus("current")


class _NncAtmCongStatsShortIntvlAbsoluteIntervalNumber_Type(Integer32):
    """Custom type nncAtmCongStatsShortIntvlAbsoluteIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncAtmCongStatsShortIntvlAbsoluteIntervalNumber_Type.__name__ = "Integer32"
_NncAtmCongStatsShortIntvlAbsoluteIntervalNumber_Object = MibTableColumn
nncAtmCongStatsShortIntvlAbsoluteIntervalNumber = _NncAtmCongStatsShortIntvlAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 4, 1, 6),
    _NncAtmCongStatsShortIntvlAbsoluteIntervalNumber_Type()
)
nncAtmCongStatsShortIntvlAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsShortIntvlAbsoluteIntervalNumber.setStatus("current")
_NncAtmCongStatsShortIntvlTotalCellsArrived_Type = NncExtCounter64
_NncAtmCongStatsShortIntvlTotalCellsArrived_Object = MibTableColumn
nncAtmCongStatsShortIntvlTotalCellsArrived = _NncAtmCongStatsShortIntvlTotalCellsArrived_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 4, 1, 7),
    _NncAtmCongStatsShortIntvlTotalCellsArrived_Type()
)
nncAtmCongStatsShortIntvlTotalCellsArrived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsShortIntvlTotalCellsArrived.setStatus("current")
_NncAtmCongStatsShortIntvlTotalCellsDiscarded_Type = NncExtCounter64
_NncAtmCongStatsShortIntvlTotalCellsDiscarded_Object = MibTableColumn
nncAtmCongStatsShortIntvlTotalCellsDiscarded = _NncAtmCongStatsShortIntvlTotalCellsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 4, 1, 8),
    _NncAtmCongStatsShortIntvlTotalCellsDiscarded_Type()
)
nncAtmCongStatsShortIntvlTotalCellsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsShortIntvlTotalCellsDiscarded.setStatus("current")
_NncAtmCongStatsShortIntvlClp0CellsDiscarded_Type = NncExtCounter64
_NncAtmCongStatsShortIntvlClp0CellsDiscarded_Object = MibTableColumn
nncAtmCongStatsShortIntvlClp0CellsDiscarded = _NncAtmCongStatsShortIntvlClp0CellsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 4, 1, 9),
    _NncAtmCongStatsShortIntvlClp0CellsDiscarded_Type()
)
nncAtmCongStatsShortIntvlClp0CellsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsShortIntvlClp0CellsDiscarded.setStatus("current")
_NncAtmCongStatsShortIntvlLowCongestedSeconds_Type = Counter32
_NncAtmCongStatsShortIntvlLowCongestedSeconds_Object = MibTableColumn
nncAtmCongStatsShortIntvlLowCongestedSeconds = _NncAtmCongStatsShortIntvlLowCongestedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 4, 1, 10),
    _NncAtmCongStatsShortIntvlLowCongestedSeconds_Type()
)
nncAtmCongStatsShortIntvlLowCongestedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsShortIntvlLowCongestedSeconds.setStatus("current")
_NncAtmCongStatsShortIntvlMediumCongestedSeconds_Type = Counter32
_NncAtmCongStatsShortIntvlMediumCongestedSeconds_Object = MibTableColumn
nncAtmCongStatsShortIntvlMediumCongestedSeconds = _NncAtmCongStatsShortIntvlMediumCongestedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 4, 1, 11),
    _NncAtmCongStatsShortIntvlMediumCongestedSeconds_Type()
)
nncAtmCongStatsShortIntvlMediumCongestedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsShortIntvlMediumCongestedSeconds.setStatus("current")
_NncAtmCongStatsShortIntvlSevereCongestedSeconds_Type = Counter32
_NncAtmCongStatsShortIntvlSevereCongestedSeconds_Object = MibTableColumn
nncAtmCongStatsShortIntvlSevereCongestedSeconds = _NncAtmCongStatsShortIntvlSevereCongestedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 4, 1, 12),
    _NncAtmCongStatsShortIntvlSevereCongestedSeconds_Type()
)
nncAtmCongStatsShortIntvlSevereCongestedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsShortIntvlSevereCongestedSeconds.setStatus("current")
_NncAtmCongStatsShortIntvlTotalSeconds_Type = Counter32
_NncAtmCongStatsShortIntvlTotalSeconds_Object = MibTableColumn
nncAtmCongStatsShortIntvlTotalSeconds = _NncAtmCongStatsShortIntvlTotalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 4, 1, 13),
    _NncAtmCongStatsShortIntvlTotalSeconds_Type()
)
nncAtmCongStatsShortIntvlTotalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsShortIntvlTotalSeconds.setStatus("current")


class _NncAtmCongStatsShortIntvlCongestionState_Type(Integer32):
    """Custom type nncAtmCongStatsShortIntvlCongestionState based on Integer32"""
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
        *(("congStatsLowCongState", 2),
          ("congStatsMediumCongState", 3),
          ("congStatsNormalState", 1),
          ("congStatsSevereCongState", 4))
    )


_NncAtmCongStatsShortIntvlCongestionState_Type.__name__ = "Integer32"
_NncAtmCongStatsShortIntvlCongestionState_Object = MibTableColumn
nncAtmCongStatsShortIntvlCongestionState = _NncAtmCongStatsShortIntvlCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 4, 1, 14),
    _NncAtmCongStatsShortIntvlCongestionState_Type()
)
nncAtmCongStatsShortIntvlCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsShortIntvlCongestionState.setStatus("current")


class _NncAtmCongStatsShortIntvlAlarmStatus_Type(Integer32):
    """Custom type nncAtmCongStatsShortIntvlAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("congStatsAlarmOff", 2),
          ("congStatsAlarmOn", 1))
    )


_NncAtmCongStatsShortIntvlAlarmStatus_Type.__name__ = "Integer32"
_NncAtmCongStatsShortIntvlAlarmStatus_Object = MibTableColumn
nncAtmCongStatsShortIntvlAlarmStatus = _NncAtmCongStatsShortIntvlAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 4, 1, 15),
    _NncAtmCongStatsShortIntvlAlarmStatus_Type()
)
nncAtmCongStatsShortIntvlAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsShortIntvlAlarmStatus.setStatus("current")
_NncAtmCongStatsCurrentLongIntvlTable_Object = MibTable
nncAtmCongStatsCurrentLongIntvlTable = _NncAtmCongStatsCurrentLongIntvlTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 5)
)
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentLongIntvlTable.setStatus("current")
_NncAtmCongStatsCurrentLongIntvlEntry_Object = MibTableRow
nncAtmCongStatsCurrentLongIntvlEntry = _NncAtmCongStatsCurrentLongIntvlEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 5, 1)
)
nncAtmCongStatsCurrentLongIntvlEntry.setIndexNames(
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "entPhysicalEntityCurrentLongIntvlIndex"),
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongPointCurrentLongIntvlIndex"),
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsQOSCurrentLongIntvlIndex"),
)
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentLongIntvlEntry.setStatus("current")
_EntPhysicalEntityCurrentLongIntvlIndex_Type = PhysicalIndex
_EntPhysicalEntityCurrentLongIntvlIndex_Object = MibTableColumn
entPhysicalEntityCurrentLongIntvlIndex = _EntPhysicalEntityCurrentLongIntvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 5, 1, 1),
    _EntPhysicalEntityCurrentLongIntvlIndex_Type()
)
entPhysicalEntityCurrentLongIntvlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    entPhysicalEntityCurrentLongIntvlIndex.setStatus("current")


class _NncAtmCongPointCurrentLongIntvlIndex_Type(Integer32):
    """Custom type nncAtmCongPointCurrentLongIntvlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NncAtmCongPointCurrentLongIntvlIndex_Type.__name__ = "Integer32"
_NncAtmCongPointCurrentLongIntvlIndex_Object = MibTableColumn
nncAtmCongPointCurrentLongIntvlIndex = _NncAtmCongPointCurrentLongIntvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 5, 1, 2),
    _NncAtmCongPointCurrentLongIntvlIndex_Type()
)
nncAtmCongPointCurrentLongIntvlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncAtmCongPointCurrentLongIntvlIndex.setStatus("current")


class _NncAtmCongStatsQOSCurrentLongIntvlIndex_Type(Integer32):
    """Custom type nncAtmCongStatsQOSCurrentLongIntvlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_NncAtmCongStatsQOSCurrentLongIntvlIndex_Type.__name__ = "Integer32"
_NncAtmCongStatsQOSCurrentLongIntvlIndex_Object = MibTableColumn
nncAtmCongStatsQOSCurrentLongIntvlIndex = _NncAtmCongStatsQOSCurrentLongIntvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 5, 1, 3),
    _NncAtmCongStatsQOSCurrentLongIntvlIndex_Type()
)
nncAtmCongStatsQOSCurrentLongIntvlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncAtmCongStatsQOSCurrentLongIntvlIndex.setStatus("current")
_NncAtmCongStatsCurrentLongIntvlState_Type = NncExtIntvlStateType
_NncAtmCongStatsCurrentLongIntvlState_Object = MibTableColumn
nncAtmCongStatsCurrentLongIntvlState = _NncAtmCongStatsCurrentLongIntvlState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 5, 1, 4),
    _NncAtmCongStatsCurrentLongIntvlState_Type()
)
nncAtmCongStatsCurrentLongIntvlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentLongIntvlState.setStatus("current")


class _NncAtmCongStatsCurrentLongIntvlAbsoluteIntervalNumber_Type(Integer32):
    """Custom type nncAtmCongStatsCurrentLongIntvlAbsoluteIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_NncAtmCongStatsCurrentLongIntvlAbsoluteIntervalNumber_Type.__name__ = "Integer32"
_NncAtmCongStatsCurrentLongIntvlAbsoluteIntervalNumber_Object = MibTableColumn
nncAtmCongStatsCurrentLongIntvlAbsoluteIntervalNumber = _NncAtmCongStatsCurrentLongIntvlAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 5, 1, 5),
    _NncAtmCongStatsCurrentLongIntvlAbsoluteIntervalNumber_Type()
)
nncAtmCongStatsCurrentLongIntvlAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentLongIntvlAbsoluteIntervalNumber.setStatus("current")
_NncAtmCongStatsCurrentLongIntvlTotalCellsArrived_Type = NncExtCounter64
_NncAtmCongStatsCurrentLongIntvlTotalCellsArrived_Object = MibTableColumn
nncAtmCongStatsCurrentLongIntvlTotalCellsArrived = _NncAtmCongStatsCurrentLongIntvlTotalCellsArrived_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 5, 1, 6),
    _NncAtmCongStatsCurrentLongIntvlTotalCellsArrived_Type()
)
nncAtmCongStatsCurrentLongIntvlTotalCellsArrived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentLongIntvlTotalCellsArrived.setStatus("current")
_NncAtmCongStatsCurrentLongIntvlTotalCellsDiscarded_Type = NncExtCounter64
_NncAtmCongStatsCurrentLongIntvlTotalCellsDiscarded_Object = MibTableColumn
nncAtmCongStatsCurrentLongIntvlTotalCellsDiscarded = _NncAtmCongStatsCurrentLongIntvlTotalCellsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 5, 1, 7),
    _NncAtmCongStatsCurrentLongIntvlTotalCellsDiscarded_Type()
)
nncAtmCongStatsCurrentLongIntvlTotalCellsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentLongIntvlTotalCellsDiscarded.setStatus("current")
_NncAtmCongStatsCurrentLongIntvlClp0CellsDiscarded_Type = NncExtCounter64
_NncAtmCongStatsCurrentLongIntvlClp0CellsDiscarded_Object = MibTableColumn
nncAtmCongStatsCurrentLongIntvlClp0CellsDiscarded = _NncAtmCongStatsCurrentLongIntvlClp0CellsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 5, 1, 8),
    _NncAtmCongStatsCurrentLongIntvlClp0CellsDiscarded_Type()
)
nncAtmCongStatsCurrentLongIntvlClp0CellsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentLongIntvlClp0CellsDiscarded.setStatus("current")
_NncAtmCongStatsCurrentLongIntvlLowCongestedSeconds_Type = Counter32
_NncAtmCongStatsCurrentLongIntvlLowCongestedSeconds_Object = MibTableColumn
nncAtmCongStatsCurrentLongIntvlLowCongestedSeconds = _NncAtmCongStatsCurrentLongIntvlLowCongestedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 5, 1, 9),
    _NncAtmCongStatsCurrentLongIntvlLowCongestedSeconds_Type()
)
nncAtmCongStatsCurrentLongIntvlLowCongestedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentLongIntvlLowCongestedSeconds.setStatus("current")
_NncAtmCongStatsCurrentLongIntvlMediumCongestedSeconds_Type = Counter32
_NncAtmCongStatsCurrentLongIntvlMediumCongestedSeconds_Object = MibTableColumn
nncAtmCongStatsCurrentLongIntvlMediumCongestedSeconds = _NncAtmCongStatsCurrentLongIntvlMediumCongestedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 5, 1, 10),
    _NncAtmCongStatsCurrentLongIntvlMediumCongestedSeconds_Type()
)
nncAtmCongStatsCurrentLongIntvlMediumCongestedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentLongIntvlMediumCongestedSeconds.setStatus("current")
_NncAtmCongStatsCurrentLongIntvlSevereCongestedSeconds_Type = Counter32
_NncAtmCongStatsCurrentLongIntvlSevereCongestedSeconds_Object = MibTableColumn
nncAtmCongStatsCurrentLongIntvlSevereCongestedSeconds = _NncAtmCongStatsCurrentLongIntvlSevereCongestedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 5, 1, 11),
    _NncAtmCongStatsCurrentLongIntvlSevereCongestedSeconds_Type()
)
nncAtmCongStatsCurrentLongIntvlSevereCongestedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentLongIntvlSevereCongestedSeconds.setStatus("current")
_NncAtmCongStatsCurrentLongIntvlTotalSeconds_Type = Counter32
_NncAtmCongStatsCurrentLongIntvlTotalSeconds_Object = MibTableColumn
nncAtmCongStatsCurrentLongIntvlTotalSeconds = _NncAtmCongStatsCurrentLongIntvlTotalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 5, 1, 12),
    _NncAtmCongStatsCurrentLongIntvlTotalSeconds_Type()
)
nncAtmCongStatsCurrentLongIntvlTotalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentLongIntvlTotalSeconds.setStatus("current")


class _NncAtmCongStatsCurrentLongIntvlCongestionState_Type(Integer32):
    """Custom type nncAtmCongStatsCurrentLongIntvlCongestionState based on Integer32"""
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
        *(("congStatsLowCongState", 2),
          ("congStatsMediumCongState", 3),
          ("congStatsNormalState", 1),
          ("congStatsSevereCongState", 4))
    )


_NncAtmCongStatsCurrentLongIntvlCongestionState_Type.__name__ = "Integer32"
_NncAtmCongStatsCurrentLongIntvlCongestionState_Object = MibTableColumn
nncAtmCongStatsCurrentLongIntvlCongestionState = _NncAtmCongStatsCurrentLongIntvlCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 5, 1, 13),
    _NncAtmCongStatsCurrentLongIntvlCongestionState_Type()
)
nncAtmCongStatsCurrentLongIntvlCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentLongIntvlCongestionState.setStatus("current")


class _NncAtmCongStatsCurrentLongIntvlAlarmStatus_Type(Integer32):
    """Custom type nncAtmCongStatsCurrentLongIntvlAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("congStatsAlarmOff", 2),
          ("congStatsAlarmOn", 1))
    )


_NncAtmCongStatsCurrentLongIntvlAlarmStatus_Type.__name__ = "Integer32"
_NncAtmCongStatsCurrentLongIntvlAlarmStatus_Object = MibTableColumn
nncAtmCongStatsCurrentLongIntvlAlarmStatus = _NncAtmCongStatsCurrentLongIntvlAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 5, 1, 14),
    _NncAtmCongStatsCurrentLongIntvlAlarmStatus_Type()
)
nncAtmCongStatsCurrentLongIntvlAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentLongIntvlAlarmStatus.setStatus("current")
_NncAtmCongStatsLongIntvlTable_Object = MibTable
nncAtmCongStatsLongIntvlTable = _NncAtmCongStatsLongIntvlTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 6)
)
if mibBuilder.loadTexts:
    nncAtmCongStatsLongIntvlTable.setStatus("current")
_NncAtmCongStatsLongIntvlEntry_Object = MibTableRow
nncAtmCongStatsLongIntvlEntry = _NncAtmCongStatsLongIntvlEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 6, 1)
)
nncAtmCongStatsLongIntvlEntry.setIndexNames(
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "entPhysicalEntityLongIntvlIndex"),
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongPointLongIntvlIndex"),
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsQOSLongIntvlIndex"),
    (0, "NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsLongIntvlIntervalIndex"),
)
if mibBuilder.loadTexts:
    nncAtmCongStatsLongIntvlEntry.setStatus("current")
_EntPhysicalEntityLongIntvlIndex_Type = PhysicalIndex
_EntPhysicalEntityLongIntvlIndex_Object = MibTableColumn
entPhysicalEntityLongIntvlIndex = _EntPhysicalEntityLongIntvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 6, 1, 1),
    _EntPhysicalEntityLongIntvlIndex_Type()
)
entPhysicalEntityLongIntvlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    entPhysicalEntityLongIntvlIndex.setStatus("current")


class _NncAtmCongPointLongIntvlIndex_Type(Integer32):
    """Custom type nncAtmCongPointLongIntvlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NncAtmCongPointLongIntvlIndex_Type.__name__ = "Integer32"
_NncAtmCongPointLongIntvlIndex_Object = MibTableColumn
nncAtmCongPointLongIntvlIndex = _NncAtmCongPointLongIntvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 6, 1, 2),
    _NncAtmCongPointLongIntvlIndex_Type()
)
nncAtmCongPointLongIntvlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncAtmCongPointLongIntvlIndex.setStatus("current")


class _NncAtmCongStatsQOSLongIntvlIndex_Type(Integer32):
    """Custom type nncAtmCongStatsQOSLongIntvlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_NncAtmCongStatsQOSLongIntvlIndex_Type.__name__ = "Integer32"
_NncAtmCongStatsQOSLongIntvlIndex_Object = MibTableColumn
nncAtmCongStatsQOSLongIntvlIndex = _NncAtmCongStatsQOSLongIntvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 6, 1, 3),
    _NncAtmCongStatsQOSLongIntvlIndex_Type()
)
nncAtmCongStatsQOSLongIntvlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncAtmCongStatsQOSLongIntvlIndex.setStatus("current")


class _NncAtmCongStatsLongIntvlIntervalIndex_Type(Integer32):
    """Custom type nncAtmCongStatsLongIntvlIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_NncAtmCongStatsLongIntvlIntervalIndex_Type.__name__ = "Integer32"
_NncAtmCongStatsLongIntvlIntervalIndex_Object = MibTableColumn
nncAtmCongStatsLongIntvlIntervalIndex = _NncAtmCongStatsLongIntvlIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 6, 1, 4),
    _NncAtmCongStatsLongIntvlIntervalIndex_Type()
)
nncAtmCongStatsLongIntvlIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncAtmCongStatsLongIntvlIntervalIndex.setStatus("current")
_NncAtmCongStatsLongIntvlState_Type = NncExtIntvlStateType
_NncAtmCongStatsLongIntvlState_Object = MibTableColumn
nncAtmCongStatsLongIntvlState = _NncAtmCongStatsLongIntvlState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 6, 1, 5),
    _NncAtmCongStatsLongIntvlState_Type()
)
nncAtmCongStatsLongIntvlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsLongIntvlState.setStatus("current")


class _NncAtmCongStatsLongIntvlAbsoluteIntervalNumber_Type(Integer32):
    """Custom type nncAtmCongStatsLongIntvlAbsoluteIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_NncAtmCongStatsLongIntvlAbsoluteIntervalNumber_Type.__name__ = "Integer32"
_NncAtmCongStatsLongIntvlAbsoluteIntervalNumber_Object = MibTableColumn
nncAtmCongStatsLongIntvlAbsoluteIntervalNumber = _NncAtmCongStatsLongIntvlAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 6, 1, 6),
    _NncAtmCongStatsLongIntvlAbsoluteIntervalNumber_Type()
)
nncAtmCongStatsLongIntvlAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsLongIntvlAbsoluteIntervalNumber.setStatus("current")
_NncAtmCongStatsLongIntvlTotalCellsArrived_Type = NncExtCounter64
_NncAtmCongStatsLongIntvlTotalCellsArrived_Object = MibTableColumn
nncAtmCongStatsLongIntvlTotalCellsArrived = _NncAtmCongStatsLongIntvlTotalCellsArrived_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 6, 1, 7),
    _NncAtmCongStatsLongIntvlTotalCellsArrived_Type()
)
nncAtmCongStatsLongIntvlTotalCellsArrived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsLongIntvlTotalCellsArrived.setStatus("current")
_NncAtmCongStatsLongIntvlTotalCellsDiscarded_Type = NncExtCounter64
_NncAtmCongStatsLongIntvlTotalCellsDiscarded_Object = MibTableColumn
nncAtmCongStatsLongIntvlTotalCellsDiscarded = _NncAtmCongStatsLongIntvlTotalCellsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 6, 1, 8),
    _NncAtmCongStatsLongIntvlTotalCellsDiscarded_Type()
)
nncAtmCongStatsLongIntvlTotalCellsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsLongIntvlTotalCellsDiscarded.setStatus("current")
_NncAtmCongStatsLongIntvlClp0CellsDiscarded_Type = NncExtCounter64
_NncAtmCongStatsLongIntvlClp0CellsDiscarded_Object = MibTableColumn
nncAtmCongStatsLongIntvlClp0CellsDiscarded = _NncAtmCongStatsLongIntvlClp0CellsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 6, 1, 9),
    _NncAtmCongStatsLongIntvlClp0CellsDiscarded_Type()
)
nncAtmCongStatsLongIntvlClp0CellsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsLongIntvlClp0CellsDiscarded.setStatus("current")
_NncAtmCongStatsLongIntvlLowCongestedSeconds_Type = Counter32
_NncAtmCongStatsLongIntvlLowCongestedSeconds_Object = MibTableColumn
nncAtmCongStatsLongIntvlLowCongestedSeconds = _NncAtmCongStatsLongIntvlLowCongestedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 6, 1, 10),
    _NncAtmCongStatsLongIntvlLowCongestedSeconds_Type()
)
nncAtmCongStatsLongIntvlLowCongestedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsLongIntvlLowCongestedSeconds.setStatus("current")
_NncAtmCongStatsLongIntvlMediumCongestedSeconds_Type = Counter32
_NncAtmCongStatsLongIntvlMediumCongestedSeconds_Object = MibTableColumn
nncAtmCongStatsLongIntvlMediumCongestedSeconds = _NncAtmCongStatsLongIntvlMediumCongestedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 6, 1, 11),
    _NncAtmCongStatsLongIntvlMediumCongestedSeconds_Type()
)
nncAtmCongStatsLongIntvlMediumCongestedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsLongIntvlMediumCongestedSeconds.setStatus("current")
_NncAtmCongStatsLongIntvlSevereCongestedSeconds_Type = Counter32
_NncAtmCongStatsLongIntvlSevereCongestedSeconds_Object = MibTableColumn
nncAtmCongStatsLongIntvlSevereCongestedSeconds = _NncAtmCongStatsLongIntvlSevereCongestedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 6, 1, 12),
    _NncAtmCongStatsLongIntvlSevereCongestedSeconds_Type()
)
nncAtmCongStatsLongIntvlSevereCongestedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsLongIntvlSevereCongestedSeconds.setStatus("current")
_NncAtmCongStatsLongIntvlTotalSeconds_Type = Counter32
_NncAtmCongStatsLongIntvlTotalSeconds_Object = MibTableColumn
nncAtmCongStatsLongIntvlTotalSeconds = _NncAtmCongStatsLongIntvlTotalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 6, 1, 13),
    _NncAtmCongStatsLongIntvlTotalSeconds_Type()
)
nncAtmCongStatsLongIntvlTotalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsLongIntvlTotalSeconds.setStatus("current")


class _NncAtmCongStatsLongIntvlCongestionState_Type(Integer32):
    """Custom type nncAtmCongStatsLongIntvlCongestionState based on Integer32"""
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
        *(("congStatsLowCongState", 2),
          ("congStatsMediumCongState", 3),
          ("congStatsNormalState", 1),
          ("congStatsSevereCongState", 4))
    )


_NncAtmCongStatsLongIntvlCongestionState_Type.__name__ = "Integer32"
_NncAtmCongStatsLongIntvlCongestionState_Object = MibTableColumn
nncAtmCongStatsLongIntvlCongestionState = _NncAtmCongStatsLongIntvlCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 6, 1, 14),
    _NncAtmCongStatsLongIntvlCongestionState_Type()
)
nncAtmCongStatsLongIntvlCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsLongIntvlCongestionState.setStatus("current")


class _NncAtmCongStatsLongIntvlAlarmStatus_Type(Integer32):
    """Custom type nncAtmCongStatsLongIntvlAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("congStatsAlarmOff", 2),
          ("congStatsAlarmOn", 1))
    )


_NncAtmCongStatsLongIntvlAlarmStatus_Type.__name__ = "Integer32"
_NncAtmCongStatsLongIntvlAlarmStatus_Object = MibTableColumn
nncAtmCongStatsLongIntvlAlarmStatus = _NncAtmCongStatsLongIntvlAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 1, 6, 1, 15),
    _NncAtmCongStatsLongIntvlAlarmStatus_Type()
)
nncAtmCongStatsLongIntvlAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmCongStatsLongIntvlAlarmStatus.setStatus("current")
_NncAtmCongStatsGroups_ObjectIdentity = ObjectIdentity
nncAtmCongStatsGroups = _NncAtmCongStatsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 2)
)
_NncAtmCongStatsCompliances_ObjectIdentity = ObjectIdentity
nncAtmCongStatsCompliances = _NncAtmCongStatsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 3)
)

# Managed Objects groups

nncAtmCongPointInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 2, 1)
)
nncAtmCongPointInfoGroup.setObjects(
      *(("NNC-ATM-CONGESTIONSTATISTICS-MIB", "entPhysicalEntityInfoIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongPointInfoIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongPointHardwareType"))
)
if mibBuilder.loadTexts:
    nncAtmCongPointInfoGroup.setStatus("current")

nncAtmCongStatsRawGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 2, 2)
)
nncAtmCongStatsRawGroup.setObjects(
      *(("NNC-ATM-CONGESTIONSTATISTICS-MIB", "entPhysicalEntityRawIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongPointRawIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsQOSRawIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsTotalCellsArrived"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsTotalCellsDiscarded"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsClp0CellsDiscarded"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsLowCongestedSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsMediumCongestedSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsSevereCongestedSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsTotalSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentCongestionState"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsAlarmStatus"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsVirtualBandwidthAvail"))
)
if mibBuilder.loadTexts:
    nncAtmCongStatsRawGroup.setStatus("current")

nncAtmCongStatsCurrentShortIntvlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 2, 3)
)
nncAtmCongStatsCurrentShortIntvlGroup.setObjects(
      *(("NNC-ATM-CONGESTIONSTATISTICS-MIB", "entPhysicalEntityCurrentShortIntvlIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongPointCurrentShortIntvlIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsQOSCurrentShortIntvlIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentShortIntvlState"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentShortIntvlAbsoluteIntervalNumber"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentShortIntvlTotalCellsArrived"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentShortIntvlTotalCellsDiscarded"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentShortIntvlClp0CellsDiscarded"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentShortIntvlLowCongestedSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentShortIntvlMediumCongestedSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentShortIntvlSevereCongestedSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentShortIntvlTotalSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentShortIntvlCongestionState"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentShortIntvlAlarmStatus"))
)
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentShortIntvlGroup.setStatus("current")

nncAtmCongStatsShortIntvlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 2, 4)
)
nncAtmCongStatsShortIntvlGroup.setObjects(
      *(("NNC-ATM-CONGESTIONSTATISTICS-MIB", "entPhysicalEntityShortIntvlIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongPointShortIntvlIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsQOSShortIntvlIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsShortIntvlIntervalIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsShortIntvlState"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsShortIntvlAbsoluteIntervalNumber"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsShortIntvlTotalCellsArrived"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsShortIntvlTotalCellsDiscarded"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsShortIntvlClp0CellsDiscarded"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsShortIntvlLowCongestedSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsShortIntvlMediumCongestedSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsShortIntvlSevereCongestedSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsShortIntvlTotalSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsShortIntvlCongestionState"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsShortIntvlAlarmStatus"))
)
if mibBuilder.loadTexts:
    nncAtmCongStatsShortIntvlGroup.setStatus("current")

nncAtmCongStatsCurrentLongIntvlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 2, 5)
)
nncAtmCongStatsCurrentLongIntvlGroup.setObjects(
      *(("NNC-ATM-CONGESTIONSTATISTICS-MIB", "entPhysicalEntityCurrentLongIntvlIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongPointCurrentLongIntvlIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsQOSCurrentLongIntvlIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentLongIntvlState"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentLongIntvlAbsoluteIntervalNumber"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentLongIntvlTotalCellsArrived"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentLongIntvlTotalCellsDiscarded"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentLongIntvlClp0CellsDiscarded"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentLongIntvlLowCongestedSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentLongIntvlMediumCongestedSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentLongIntvlSevereCongestedSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentLongIntvlTotalSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentLongIntvlCongestionState"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsCurrentLongIntvlAlarmStatus"))
)
if mibBuilder.loadTexts:
    nncAtmCongStatsCurrentLongIntvlGroup.setStatus("current")

nncAtmCongStatsLongIntvlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 2, 6)
)
nncAtmCongStatsLongIntvlGroup.setObjects(
      *(("NNC-ATM-CONGESTIONSTATISTICS-MIB", "entPhysicalEntityLongIntvlIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongPointLongIntvlIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsQOSLongIntvlIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsLongIntvlIntervalIndex"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsLongIntvlState"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsLongIntvlAbsoluteIntervalNumber"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsLongIntvlTotalCellsArrived"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsLongIntvlTotalCellsDiscarded"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsLongIntvlClp0CellsDiscarded"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsLongIntvlLowCongestedSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsLongIntvlMediumCongestedSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsLongIntvlSevereCongestedSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsLongIntvlTotalSeconds"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsLongIntvlCongestionState"),
        ("NNC-ATM-CONGESTIONSTATISTICS-MIB", "nncAtmCongStatsLongIntvlAlarmStatus"))
)
if mibBuilder.loadTexts:
    nncAtmCongStatsLongIntvlGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nncAtmCongStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 63, 3, 1)
)
if mibBuilder.loadTexts:
    nncAtmCongStatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNC-ATM-CONGESTIONSTATISTICS-MIB",
    **{"nncAtmCongestionStatistics": nncAtmCongestionStatistics,
       "nncAtmCongStatsObjects": nncAtmCongStatsObjects,
       "nncAtmCongPointInfoTable": nncAtmCongPointInfoTable,
       "nncAtmCongPointInfoEntry": nncAtmCongPointInfoEntry,
       "entPhysicalEntityInfoIndex": entPhysicalEntityInfoIndex,
       "nncAtmCongPointInfoIndex": nncAtmCongPointInfoIndex,
       "nncAtmCongPointHardwareType": nncAtmCongPointHardwareType,
       "nncAtmCongStatsRawTable": nncAtmCongStatsRawTable,
       "nncAtmCongStatsRawEntry": nncAtmCongStatsRawEntry,
       "entPhysicalEntityRawIndex": entPhysicalEntityRawIndex,
       "nncAtmCongPointRawIndex": nncAtmCongPointRawIndex,
       "nncAtmCongStatsQOSRawIndex": nncAtmCongStatsQOSRawIndex,
       "nncAtmCongStatsTotalCellsArrived": nncAtmCongStatsTotalCellsArrived,
       "nncAtmCongStatsTotalCellsDiscarded": nncAtmCongStatsTotalCellsDiscarded,
       "nncAtmCongStatsClp0CellsDiscarded": nncAtmCongStatsClp0CellsDiscarded,
       "nncAtmCongStatsLowCongestedSeconds": nncAtmCongStatsLowCongestedSeconds,
       "nncAtmCongStatsMediumCongestedSeconds": nncAtmCongStatsMediumCongestedSeconds,
       "nncAtmCongStatsSevereCongestedSeconds": nncAtmCongStatsSevereCongestedSeconds,
       "nncAtmCongStatsTotalSeconds": nncAtmCongStatsTotalSeconds,
       "nncAtmCongStatsCurrentCongestionState": nncAtmCongStatsCurrentCongestionState,
       "nncAtmCongStatsAlarmStatus": nncAtmCongStatsAlarmStatus,
       "nncAtmCongStatsVirtualBandwidthAvail": nncAtmCongStatsVirtualBandwidthAvail,
       "nncAtmCongStatsCurrentShortIntvlTable": nncAtmCongStatsCurrentShortIntvlTable,
       "nncAtmCongStatsCurrentShortIntvlEntry": nncAtmCongStatsCurrentShortIntvlEntry,
       "entPhysicalEntityCurrentShortIntvlIndex": entPhysicalEntityCurrentShortIntvlIndex,
       "nncAtmCongPointCurrentShortIntvlIndex": nncAtmCongPointCurrentShortIntvlIndex,
       "nncAtmCongStatsQOSCurrentShortIntvlIndex": nncAtmCongStatsQOSCurrentShortIntvlIndex,
       "nncAtmCongStatsCurrentShortIntvlState": nncAtmCongStatsCurrentShortIntvlState,
       "nncAtmCongStatsCurrentShortIntvlAbsoluteIntervalNumber": nncAtmCongStatsCurrentShortIntvlAbsoluteIntervalNumber,
       "nncAtmCongStatsCurrentShortIntvlTotalCellsArrived": nncAtmCongStatsCurrentShortIntvlTotalCellsArrived,
       "nncAtmCongStatsCurrentShortIntvlTotalCellsDiscarded": nncAtmCongStatsCurrentShortIntvlTotalCellsDiscarded,
       "nncAtmCongStatsCurrentShortIntvlClp0CellsDiscarded": nncAtmCongStatsCurrentShortIntvlClp0CellsDiscarded,
       "nncAtmCongStatsCurrentShortIntvlLowCongestedSeconds": nncAtmCongStatsCurrentShortIntvlLowCongestedSeconds,
       "nncAtmCongStatsCurrentShortIntvlMediumCongestedSeconds": nncAtmCongStatsCurrentShortIntvlMediumCongestedSeconds,
       "nncAtmCongStatsCurrentShortIntvlSevereCongestedSeconds": nncAtmCongStatsCurrentShortIntvlSevereCongestedSeconds,
       "nncAtmCongStatsCurrentShortIntvlTotalSeconds": nncAtmCongStatsCurrentShortIntvlTotalSeconds,
       "nncAtmCongStatsCurrentShortIntvlCongestionState": nncAtmCongStatsCurrentShortIntvlCongestionState,
       "nncAtmCongStatsCurrentShortIntvlAlarmStatus": nncAtmCongStatsCurrentShortIntvlAlarmStatus,
       "nncAtmCongStatsShortIntvlTable": nncAtmCongStatsShortIntvlTable,
       "nncAtmCongStatsShortIntvlEntry": nncAtmCongStatsShortIntvlEntry,
       "entPhysicalEntityShortIntvlIndex": entPhysicalEntityShortIntvlIndex,
       "nncAtmCongPointShortIntvlIndex": nncAtmCongPointShortIntvlIndex,
       "nncAtmCongStatsQOSShortIntvlIndex": nncAtmCongStatsQOSShortIntvlIndex,
       "nncAtmCongStatsShortIntvlIntervalIndex": nncAtmCongStatsShortIntvlIntervalIndex,
       "nncAtmCongStatsShortIntvlState": nncAtmCongStatsShortIntvlState,
       "nncAtmCongStatsShortIntvlAbsoluteIntervalNumber": nncAtmCongStatsShortIntvlAbsoluteIntervalNumber,
       "nncAtmCongStatsShortIntvlTotalCellsArrived": nncAtmCongStatsShortIntvlTotalCellsArrived,
       "nncAtmCongStatsShortIntvlTotalCellsDiscarded": nncAtmCongStatsShortIntvlTotalCellsDiscarded,
       "nncAtmCongStatsShortIntvlClp0CellsDiscarded": nncAtmCongStatsShortIntvlClp0CellsDiscarded,
       "nncAtmCongStatsShortIntvlLowCongestedSeconds": nncAtmCongStatsShortIntvlLowCongestedSeconds,
       "nncAtmCongStatsShortIntvlMediumCongestedSeconds": nncAtmCongStatsShortIntvlMediumCongestedSeconds,
       "nncAtmCongStatsShortIntvlSevereCongestedSeconds": nncAtmCongStatsShortIntvlSevereCongestedSeconds,
       "nncAtmCongStatsShortIntvlTotalSeconds": nncAtmCongStatsShortIntvlTotalSeconds,
       "nncAtmCongStatsShortIntvlCongestionState": nncAtmCongStatsShortIntvlCongestionState,
       "nncAtmCongStatsShortIntvlAlarmStatus": nncAtmCongStatsShortIntvlAlarmStatus,
       "nncAtmCongStatsCurrentLongIntvlTable": nncAtmCongStatsCurrentLongIntvlTable,
       "nncAtmCongStatsCurrentLongIntvlEntry": nncAtmCongStatsCurrentLongIntvlEntry,
       "entPhysicalEntityCurrentLongIntvlIndex": entPhysicalEntityCurrentLongIntvlIndex,
       "nncAtmCongPointCurrentLongIntvlIndex": nncAtmCongPointCurrentLongIntvlIndex,
       "nncAtmCongStatsQOSCurrentLongIntvlIndex": nncAtmCongStatsQOSCurrentLongIntvlIndex,
       "nncAtmCongStatsCurrentLongIntvlState": nncAtmCongStatsCurrentLongIntvlState,
       "nncAtmCongStatsCurrentLongIntvlAbsoluteIntervalNumber": nncAtmCongStatsCurrentLongIntvlAbsoluteIntervalNumber,
       "nncAtmCongStatsCurrentLongIntvlTotalCellsArrived": nncAtmCongStatsCurrentLongIntvlTotalCellsArrived,
       "nncAtmCongStatsCurrentLongIntvlTotalCellsDiscarded": nncAtmCongStatsCurrentLongIntvlTotalCellsDiscarded,
       "nncAtmCongStatsCurrentLongIntvlClp0CellsDiscarded": nncAtmCongStatsCurrentLongIntvlClp0CellsDiscarded,
       "nncAtmCongStatsCurrentLongIntvlLowCongestedSeconds": nncAtmCongStatsCurrentLongIntvlLowCongestedSeconds,
       "nncAtmCongStatsCurrentLongIntvlMediumCongestedSeconds": nncAtmCongStatsCurrentLongIntvlMediumCongestedSeconds,
       "nncAtmCongStatsCurrentLongIntvlSevereCongestedSeconds": nncAtmCongStatsCurrentLongIntvlSevereCongestedSeconds,
       "nncAtmCongStatsCurrentLongIntvlTotalSeconds": nncAtmCongStatsCurrentLongIntvlTotalSeconds,
       "nncAtmCongStatsCurrentLongIntvlCongestionState": nncAtmCongStatsCurrentLongIntvlCongestionState,
       "nncAtmCongStatsCurrentLongIntvlAlarmStatus": nncAtmCongStatsCurrentLongIntvlAlarmStatus,
       "nncAtmCongStatsLongIntvlTable": nncAtmCongStatsLongIntvlTable,
       "nncAtmCongStatsLongIntvlEntry": nncAtmCongStatsLongIntvlEntry,
       "entPhysicalEntityLongIntvlIndex": entPhysicalEntityLongIntvlIndex,
       "nncAtmCongPointLongIntvlIndex": nncAtmCongPointLongIntvlIndex,
       "nncAtmCongStatsQOSLongIntvlIndex": nncAtmCongStatsQOSLongIntvlIndex,
       "nncAtmCongStatsLongIntvlIntervalIndex": nncAtmCongStatsLongIntvlIntervalIndex,
       "nncAtmCongStatsLongIntvlState": nncAtmCongStatsLongIntvlState,
       "nncAtmCongStatsLongIntvlAbsoluteIntervalNumber": nncAtmCongStatsLongIntvlAbsoluteIntervalNumber,
       "nncAtmCongStatsLongIntvlTotalCellsArrived": nncAtmCongStatsLongIntvlTotalCellsArrived,
       "nncAtmCongStatsLongIntvlTotalCellsDiscarded": nncAtmCongStatsLongIntvlTotalCellsDiscarded,
       "nncAtmCongStatsLongIntvlClp0CellsDiscarded": nncAtmCongStatsLongIntvlClp0CellsDiscarded,
       "nncAtmCongStatsLongIntvlLowCongestedSeconds": nncAtmCongStatsLongIntvlLowCongestedSeconds,
       "nncAtmCongStatsLongIntvlMediumCongestedSeconds": nncAtmCongStatsLongIntvlMediumCongestedSeconds,
       "nncAtmCongStatsLongIntvlSevereCongestedSeconds": nncAtmCongStatsLongIntvlSevereCongestedSeconds,
       "nncAtmCongStatsLongIntvlTotalSeconds": nncAtmCongStatsLongIntvlTotalSeconds,
       "nncAtmCongStatsLongIntvlCongestionState": nncAtmCongStatsLongIntvlCongestionState,
       "nncAtmCongStatsLongIntvlAlarmStatus": nncAtmCongStatsLongIntvlAlarmStatus,
       "nncAtmCongStatsGroups": nncAtmCongStatsGroups,
       "nncAtmCongPointInfoGroup": nncAtmCongPointInfoGroup,
       "nncAtmCongStatsRawGroup": nncAtmCongStatsRawGroup,
       "nncAtmCongStatsCurrentShortIntvlGroup": nncAtmCongStatsCurrentShortIntvlGroup,
       "nncAtmCongStatsShortIntvlGroup": nncAtmCongStatsShortIntvlGroup,
       "nncAtmCongStatsCurrentLongIntvlGroup": nncAtmCongStatsCurrentLongIntvlGroup,
       "nncAtmCongStatsLongIntvlGroup": nncAtmCongStatsLongIntvlGroup,
       "nncAtmCongStatsCompliances": nncAtmCongStatsCompliances,
       "nncAtmCongStatsCompliance": nncAtmCongStatsCompliance}
)
