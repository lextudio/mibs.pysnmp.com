# SNMP MIB module (RADLAN-PORT-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-PORT-STATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:42:59 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlPortStat = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 223)
)
rlPortStat.setRevisions(
        ("2015-04-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortStatisticsSubType(Integer32, TextualConvention):
    status = "current"
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
        *(("day", 4),
          ("hour", 3),
          ("minute", 2),
          ("second", 1),
          ("week", 5))
    )



class PortStatisticsSampleClockSource(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("sntp", 2),
          ("userDefined", 3))
    )



class PortStatisticsCounterName(Integer32, TextualConvention):
    status = "current"
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
              37,
              38)
        )
    )
    namedValues = NamedValues(
        *(("anyCounter", 0),
          ("badOctetsReceived", 35),
          ("broadcastFrameReceived", 7),
          ("broadcastFrameSent", 2),
          ("dot3InPauseFrames", 25),
          ("dot3OutPauseFrames", 26),
          ("dot3StatsExcessiveCollisions", 22),
          ("dot3StatsFCSErrors", 19),
          ("dot3StatsFrameTooLongs", 23),
          ("dot3StatsInternalMacReceiveErrors", 24),
          ("dot3StatsLateCollisions", 21),
          ("dot3StatsSingleCollisionFrames", 20),
          ("etherStatsCRCAlignErrors", 28),
          ("etherStatsCollisions", 33),
          ("etherStatsDropEvents", 27),
          ("etherStatsFragments", 31),
          ("etherStatsJabbers", 32),
          ("etherStatsOversizePkts", 30),
          ("etherStatsUndersizePkts", 29),
          ("frames1024To1518B", 18),
          ("frames128To255B", 15),
          ("frames256To511B", 16),
          ("frames512To1023B", 17),
          ("frames64B", 13),
          ("frames65To127B", 14),
          ("goodFrameReceived", 37),
          ("goodFrameSent", 36),
          ("goodOctetsReceived", 34),
          ("goodOctetsSent", 4),
          ("goodUnicastFrameReceived", 6),
          ("lastCounterSpecifier", 38),
          ("multicastFrameReceived", 8),
          ("multicastFrameSent", 3),
          ("rxErrorFrameReceived", 9),
          ("rxUtilization", 11),
          ("totalOctetsReceived", 10),
          ("txRxUtilization", 12),
          ("txUtilization", 5),
          ("unicastFrameSent", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RlPortStatEnabledPorts_Type = PortList
_RlPortStatEnabledPorts_Object = MibScalar
rlPortStatEnabledPorts = _RlPortStatEnabledPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 1),
    _RlPortStatEnabledPorts_Type()
)
rlPortStatEnabledPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortStatEnabledPorts.setStatus("current")
_RlPortStatClearPorts_Type = PortList
_RlPortStatClearPorts_Object = MibScalar
rlPortStatClearPorts = _RlPortStatClearPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 2),
    _RlPortStatClearPorts_Type()
)
rlPortStatClearPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortStatClearPorts.setStatus("current")
_RlPortStatSampleTable_Object = MibTable
rlPortStatSampleTable = _RlPortStatSampleTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 3)
)
if mibBuilder.loadTexts:
    rlPortStatSampleTable.setStatus("current")
_RlPortStatSampleEntry_Object = MibTableRow
rlPortStatSampleEntry = _RlPortStatSampleEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 3, 1)
)
rlPortStatSampleEntry.setIndexNames(
    (0, "RADLAN-PORT-STATISTICS-MIB", "rlPortStatSampleIfIndex"),
    (0, "RADLAN-PORT-STATISTICS-MIB", "rlPortStatSampleStatSubType"),
    (0, "RADLAN-PORT-STATISTICS-MIB", "rlPortStatSampleCounterName"),
    (0, "RADLAN-PORT-STATISTICS-MIB", "rlPortStatSampleStatID"),
)
if mibBuilder.loadTexts:
    rlPortStatSampleEntry.setStatus("current")
_RlPortStatSampleIfIndex_Type = InterfaceIndex
_RlPortStatSampleIfIndex_Object = MibTableColumn
rlPortStatSampleIfIndex = _RlPortStatSampleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 3, 1, 1),
    _RlPortStatSampleIfIndex_Type()
)
rlPortStatSampleIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPortStatSampleIfIndex.setStatus("current")
_RlPortStatSampleStatSubType_Type = PortStatisticsSubType
_RlPortStatSampleStatSubType_Object = MibTableColumn
rlPortStatSampleStatSubType = _RlPortStatSampleStatSubType_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 3, 1, 2),
    _RlPortStatSampleStatSubType_Type()
)
rlPortStatSampleStatSubType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPortStatSampleStatSubType.setStatus("current")
_RlPortStatSampleCounterName_Type = PortStatisticsCounterName
_RlPortStatSampleCounterName_Object = MibTableColumn
rlPortStatSampleCounterName = _RlPortStatSampleCounterName_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 3, 1, 3),
    _RlPortStatSampleCounterName_Type()
)
rlPortStatSampleCounterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPortStatSampleCounterName.setStatus("current")
_RlPortStatSampleStatID_Type = Unsigned32
_RlPortStatSampleStatID_Object = MibTableColumn
rlPortStatSampleStatID = _RlPortStatSampleStatID_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 3, 1, 4),
    _RlPortStatSampleStatID_Type()
)
rlPortStatSampleStatID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPortStatSampleStatID.setStatus("current")
_RlPortStatSampleCollectionInterval_Type = Unsigned32
_RlPortStatSampleCollectionInterval_Object = MibTableColumn
rlPortStatSampleCollectionInterval = _RlPortStatSampleCollectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 3, 1, 5),
    _RlPortStatSampleCollectionInterval_Type()
)
rlPortStatSampleCollectionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatSampleCollectionInterval.setStatus("current")
_RlPortStatSampleSystemCollectionTime_Type = Unsigned32
_RlPortStatSampleSystemCollectionTime_Object = MibTableColumn
rlPortStatSampleSystemCollectionTime = _RlPortStatSampleSystemCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 3, 1, 6),
    _RlPortStatSampleSystemCollectionTime_Type()
)
rlPortStatSampleSystemCollectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatSampleSystemCollectionTime.setStatus("current")
_RlPortStatSampleCollectionTime_Type = Unsigned32
_RlPortStatSampleCollectionTime_Object = MibTableColumn
rlPortStatSampleCollectionTime = _RlPortStatSampleCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 3, 1, 7),
    _RlPortStatSampleCollectionTime_Type()
)
rlPortStatSampleCollectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatSampleCollectionTime.setStatus("current")


class _RlPortStatSampleCollectionTimeStr_Type(DisplayString):
    """Custom type rlPortStatSampleCollectionTimeStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RlPortStatSampleCollectionTimeStr_Type.__name__ = "DisplayString"
_RlPortStatSampleCollectionTimeStr_Object = MibTableColumn
rlPortStatSampleCollectionTimeStr = _RlPortStatSampleCollectionTimeStr_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 3, 1, 8),
    _RlPortStatSampleCollectionTimeStr_Type()
)
rlPortStatSampleCollectionTimeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatSampleCollectionTimeStr.setStatus("current")
_RlPortStatSampleCounterValue_Type = Counter64
_RlPortStatSampleCounterValue_Object = MibTableColumn
rlPortStatSampleCounterValue = _RlPortStatSampleCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 3, 1, 9),
    _RlPortStatSampleCounterValue_Type()
)
rlPortStatSampleCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatSampleCounterValue.setStatus("current")
_RlPortStatSamplePartialFlag_Type = TruthValue
_RlPortStatSamplePartialFlag_Object = MibTableColumn
rlPortStatSamplePartialFlag = _RlPortStatSamplePartialFlag_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 3, 1, 10),
    _RlPortStatSamplePartialFlag_Type()
)
rlPortStatSamplePartialFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatSamplePartialFlag.setStatus("current")
_RlPortStatSampleClockSource_Type = PortStatisticsSampleClockSource
_RlPortStatSampleClockSource_Object = MibTableColumn
rlPortStatSampleClockSource = _RlPortStatSampleClockSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 3, 1, 11),
    _RlPortStatSampleClockSource_Type()
)
rlPortStatSampleClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatSampleClockSource.setStatus("current")
_RlPortStatLastSampleTable_Object = MibTable
rlPortStatLastSampleTable = _RlPortStatLastSampleTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 4)
)
if mibBuilder.loadTexts:
    rlPortStatLastSampleTable.setStatus("current")
_RlPortStatLastSampleEntry_Object = MibTableRow
rlPortStatLastSampleEntry = _RlPortStatLastSampleEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 4, 1)
)
rlPortStatLastSampleEntry.setIndexNames(
    (0, "RADLAN-PORT-STATISTICS-MIB", "rlPortStatLastSampleIfIndex"),
    (0, "RADLAN-PORT-STATISTICS-MIB", "rlPortStatLastSampleStatSubType"),
    (0, "RADLAN-PORT-STATISTICS-MIB", "rlPortStatLastSampleCounterName"),
)
if mibBuilder.loadTexts:
    rlPortStatLastSampleEntry.setStatus("current")
_RlPortStatLastSampleIfIndex_Type = InterfaceIndex
_RlPortStatLastSampleIfIndex_Object = MibTableColumn
rlPortStatLastSampleIfIndex = _RlPortStatLastSampleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 4, 1, 1),
    _RlPortStatLastSampleIfIndex_Type()
)
rlPortStatLastSampleIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPortStatLastSampleIfIndex.setStatus("current")
_RlPortStatLastSampleStatSubType_Type = PortStatisticsSubType
_RlPortStatLastSampleStatSubType_Object = MibTableColumn
rlPortStatLastSampleStatSubType = _RlPortStatLastSampleStatSubType_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 4, 1, 2),
    _RlPortStatLastSampleStatSubType_Type()
)
rlPortStatLastSampleStatSubType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPortStatLastSampleStatSubType.setStatus("current")
_RlPortStatLastSampleCounterName_Type = PortStatisticsCounterName
_RlPortStatLastSampleCounterName_Object = MibTableColumn
rlPortStatLastSampleCounterName = _RlPortStatLastSampleCounterName_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 4, 1, 3),
    _RlPortStatLastSampleCounterName_Type()
)
rlPortStatLastSampleCounterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPortStatLastSampleCounterName.setStatus("current")
_RlPortStatLastSampleStatID_Type = Unsigned32
_RlPortStatLastSampleStatID_Object = MibTableColumn
rlPortStatLastSampleStatID = _RlPortStatLastSampleStatID_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 4, 1, 4),
    _RlPortStatLastSampleStatID_Type()
)
rlPortStatLastSampleStatID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatLastSampleStatID.setStatus("current")
_RlPortStatLastSampleCollectionInterval_Type = Unsigned32
_RlPortStatLastSampleCollectionInterval_Object = MibTableColumn
rlPortStatLastSampleCollectionInterval = _RlPortStatLastSampleCollectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 4, 1, 5),
    _RlPortStatLastSampleCollectionInterval_Type()
)
rlPortStatLastSampleCollectionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatLastSampleCollectionInterval.setStatus("current")
_RlPortStatLastSampleSystemCollectionTime_Type = Unsigned32
_RlPortStatLastSampleSystemCollectionTime_Object = MibTableColumn
rlPortStatLastSampleSystemCollectionTime = _RlPortStatLastSampleSystemCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 4, 1, 6),
    _RlPortStatLastSampleSystemCollectionTime_Type()
)
rlPortStatLastSampleSystemCollectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatLastSampleSystemCollectionTime.setStatus("current")
_RlPortStatLastSampleCollectionTime_Type = Unsigned32
_RlPortStatLastSampleCollectionTime_Object = MibTableColumn
rlPortStatLastSampleCollectionTime = _RlPortStatLastSampleCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 4, 1, 7),
    _RlPortStatLastSampleCollectionTime_Type()
)
rlPortStatLastSampleCollectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatLastSampleCollectionTime.setStatus("current")


class _RlPortStatLastSampleCollectionTimeStr_Type(DisplayString):
    """Custom type rlPortStatLastSampleCollectionTimeStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RlPortStatLastSampleCollectionTimeStr_Type.__name__ = "DisplayString"
_RlPortStatLastSampleCollectionTimeStr_Object = MibTableColumn
rlPortStatLastSampleCollectionTimeStr = _RlPortStatLastSampleCollectionTimeStr_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 4, 1, 8),
    _RlPortStatLastSampleCollectionTimeStr_Type()
)
rlPortStatLastSampleCollectionTimeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatLastSampleCollectionTimeStr.setStatus("current")
_RlPortStatLastSampleCounterValue_Type = Counter64
_RlPortStatLastSampleCounterValue_Object = MibTableColumn
rlPortStatLastSampleCounterValue = _RlPortStatLastSampleCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 4, 1, 9),
    _RlPortStatLastSampleCounterValue_Type()
)
rlPortStatLastSampleCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatLastSampleCounterValue.setStatus("current")
_RlPortStatLastSamplePartialFlag_Type = TruthValue
_RlPortStatLastSamplePartialFlag_Object = MibTableColumn
rlPortStatLastSamplePartialFlag = _RlPortStatLastSamplePartialFlag_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 4, 1, 10),
    _RlPortStatLastSamplePartialFlag_Type()
)
rlPortStatLastSamplePartialFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatLastSamplePartialFlag.setStatus("current")
_RlPortStatLastSampleClockSource_Type = PortStatisticsSampleClockSource
_RlPortStatLastSampleClockSource_Object = MibTableColumn
rlPortStatLastSampleClockSource = _RlPortStatLastSampleClockSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 4, 1, 11),
    _RlPortStatLastSampleClockSource_Type()
)
rlPortStatLastSampleClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatLastSampleClockSource.setStatus("current")
_RlPortStatLastEventTable_Object = MibTable
rlPortStatLastEventTable = _RlPortStatLastEventTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 5)
)
if mibBuilder.loadTexts:
    rlPortStatLastEventTable.setStatus("current")
_RlPortStatLastEventEntry_Object = MibTableRow
rlPortStatLastEventEntry = _RlPortStatLastEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 5, 1)
)
rlPortStatLastEventEntry.setIndexNames(
    (0, "RADLAN-PORT-STATISTICS-MIB", "rlPortStatLastEventIfIndex"),
    (0, "RADLAN-PORT-STATISTICS-MIB", "rlPortStatLastEventCounterName"),
)
if mibBuilder.loadTexts:
    rlPortStatLastEventEntry.setStatus("current")
_RlPortStatLastEventIfIndex_Type = InterfaceIndex
_RlPortStatLastEventIfIndex_Object = MibTableColumn
rlPortStatLastEventIfIndex = _RlPortStatLastEventIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 5, 1, 1),
    _RlPortStatLastEventIfIndex_Type()
)
rlPortStatLastEventIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPortStatLastEventIfIndex.setStatus("current")
_RlPortStatLastEventCounterName_Type = PortStatisticsCounterName
_RlPortStatLastEventCounterName_Object = MibTableColumn
rlPortStatLastEventCounterName = _RlPortStatLastEventCounterName_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 5, 1, 2),
    _RlPortStatLastEventCounterName_Type()
)
rlPortStatLastEventCounterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPortStatLastEventCounterName.setStatus("current")
_RlPortStatLastEventSystemTime_Type = Unsigned32
_RlPortStatLastEventSystemTime_Object = MibTableColumn
rlPortStatLastEventSystemTime = _RlPortStatLastEventSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 5, 1, 3),
    _RlPortStatLastEventSystemTime_Type()
)
rlPortStatLastEventSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatLastEventSystemTime.setStatus("current")
_RlPortStatLastEventPosixTime_Type = Unsigned32
_RlPortStatLastEventPosixTime_Object = MibTableColumn
rlPortStatLastEventPosixTime = _RlPortStatLastEventPosixTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 5, 1, 4),
    _RlPortStatLastEventPosixTime_Type()
)
rlPortStatLastEventPosixTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatLastEventPosixTime.setStatus("current")


class _RlPortStatLastEventTimeStr_Type(DisplayString):
    """Custom type rlPortStatLastEventTimeStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RlPortStatLastEventTimeStr_Type.__name__ = "DisplayString"
_RlPortStatLastEventTimeStr_Object = MibTableColumn
rlPortStatLastEventTimeStr = _RlPortStatLastEventTimeStr_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 5, 1, 5),
    _RlPortStatLastEventTimeStr_Type()
)
rlPortStatLastEventTimeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatLastEventTimeStr.setStatus("current")
_RlPortStatLastEventCounter_Type = PortStatisticsCounterName
_RlPortStatLastEventCounter_Object = MibTableColumn
rlPortStatLastEventCounter = _RlPortStatLastEventCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 5, 1, 6),
    _RlPortStatLastEventCounter_Type()
)
rlPortStatLastEventCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatLastEventCounter.setStatus("current")
_RlPortStatLastEventCounterValue_Type = Counter64
_RlPortStatLastEventCounterValue_Object = MibTableColumn
rlPortStatLastEventCounterValue = _RlPortStatLastEventCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 223, 5, 1, 7),
    _RlPortStatLastEventCounterValue_Type()
)
rlPortStatLastEventCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortStatLastEventCounterValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-PORT-STATISTICS-MIB",
    **{"PortStatisticsSubType": PortStatisticsSubType,
       "PortStatisticsSampleClockSource": PortStatisticsSampleClockSource,
       "PortStatisticsCounterName": PortStatisticsCounterName,
       "rlPortStat": rlPortStat,
       "rlPortStatEnabledPorts": rlPortStatEnabledPorts,
       "rlPortStatClearPorts": rlPortStatClearPorts,
       "rlPortStatSampleTable": rlPortStatSampleTable,
       "rlPortStatSampleEntry": rlPortStatSampleEntry,
       "rlPortStatSampleIfIndex": rlPortStatSampleIfIndex,
       "rlPortStatSampleStatSubType": rlPortStatSampleStatSubType,
       "rlPortStatSampleCounterName": rlPortStatSampleCounterName,
       "rlPortStatSampleStatID": rlPortStatSampleStatID,
       "rlPortStatSampleCollectionInterval": rlPortStatSampleCollectionInterval,
       "rlPortStatSampleSystemCollectionTime": rlPortStatSampleSystemCollectionTime,
       "rlPortStatSampleCollectionTime": rlPortStatSampleCollectionTime,
       "rlPortStatSampleCollectionTimeStr": rlPortStatSampleCollectionTimeStr,
       "rlPortStatSampleCounterValue": rlPortStatSampleCounterValue,
       "rlPortStatSamplePartialFlag": rlPortStatSamplePartialFlag,
       "rlPortStatSampleClockSource": rlPortStatSampleClockSource,
       "rlPortStatLastSampleTable": rlPortStatLastSampleTable,
       "rlPortStatLastSampleEntry": rlPortStatLastSampleEntry,
       "rlPortStatLastSampleIfIndex": rlPortStatLastSampleIfIndex,
       "rlPortStatLastSampleStatSubType": rlPortStatLastSampleStatSubType,
       "rlPortStatLastSampleCounterName": rlPortStatLastSampleCounterName,
       "rlPortStatLastSampleStatID": rlPortStatLastSampleStatID,
       "rlPortStatLastSampleCollectionInterval": rlPortStatLastSampleCollectionInterval,
       "rlPortStatLastSampleSystemCollectionTime": rlPortStatLastSampleSystemCollectionTime,
       "rlPortStatLastSampleCollectionTime": rlPortStatLastSampleCollectionTime,
       "rlPortStatLastSampleCollectionTimeStr": rlPortStatLastSampleCollectionTimeStr,
       "rlPortStatLastSampleCounterValue": rlPortStatLastSampleCounterValue,
       "rlPortStatLastSamplePartialFlag": rlPortStatLastSamplePartialFlag,
       "rlPortStatLastSampleClockSource": rlPortStatLastSampleClockSource,
       "rlPortStatLastEventTable": rlPortStatLastEventTable,
       "rlPortStatLastEventEntry": rlPortStatLastEventEntry,
       "rlPortStatLastEventIfIndex": rlPortStatLastEventIfIndex,
       "rlPortStatLastEventCounterName": rlPortStatLastEventCounterName,
       "rlPortStatLastEventSystemTime": rlPortStatLastEventSystemTime,
       "rlPortStatLastEventPosixTime": rlPortStatLastEventPosixTime,
       "rlPortStatLastEventTimeStr": rlPortStatLastEventTimeStr,
       "rlPortStatLastEventCounter": rlPortStatLastEventCounter,
       "rlPortStatLastEventCounterValue": rlPortStatLastEventCounterValue}
)
