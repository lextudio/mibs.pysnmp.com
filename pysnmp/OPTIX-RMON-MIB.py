# SNMP MIB module (OPTIX-RMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPTIX-RMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:27 2024
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

(optixCommon,) = mibBuilder.importSymbols(
    "OPTIX-OID-MIB",
    "optixCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

optixRmonMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35)
)
optixRmonMib.setRevisions(
        ("2006-02-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PerformanceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203)
        )
    )
    namedValues = NamedValues(
        *(("etherHistoryUtilization", 203),
          ("etherStatsAlignmentErrors", 131),
          ("etherStatsBroadcastPkts", 115),
          ("etherStatsCRCAlignErrors", 202),
          ("etherStatsCarrierSenseErrors", 138),
          ("etherStatsCollisions", 130),
          ("etherStatsDeferredTransmissions", 137),
          ("etherStatsDropEvents", 121),
          ("etherStatsExcessiveCollisions", 136),
          ("etherStatsFCSErrors", 132),
          ("etherStatsFragments", 124),
          ("etherStatsInBadOctets", 128),
          ("etherStatsInControlFrames", 194),
          ("etherStatsInGoodOctets", 126),
          ("etherStatsInPauseFrames", 119),
          ("etherStatsInUcastPkts", 113),
          ("etherStatsJabbers", 125),
          ("etherStatsLateCollisions", 135),
          ("etherStatsMulticastPkts", 114),
          ("etherStatsMultipleCollisionFrames", 134),
          ("etherStatsOctets", 200),
          ("etherStatsOutBadOctets", 129),
          ("etherStatsOutBroadcastPkts", 118),
          ("etherStatsOutControlFrames", 195),
          ("etherStatsOutDropEvents", 196),
          ("etherStatsOutGoodOctets", 127),
          ("etherStatsOutMulticastPkts", 117),
          ("etherStatsOutOctets", 199),
          ("etherStatsOutOversizePkts", 197),
          ("etherStatsOutPauseFrames", 120),
          ("etherStatsOutPkts", 198),
          ("etherStatsOutUcastPkts", 116),
          ("etherStatsOversizePkts", 123),
          ("etherStatsPkts", 201),
          ("etherStatsPkts1024to1518Octets", 106),
          ("etherStatsPkts128to255Octets", 103),
          ("etherStatsPkts1519toMTUOctets", 139),
          ("etherStatsPkts256to511Octets", 104),
          ("etherStatsPkts512to1023Octets", 105),
          ("etherStatsPkts64Octets", 101),
          ("etherStatsPkts65to127Octets", 102),
          ("etherStatsRxTxPkts1024to1518Octets", 146),
          ("etherStatsRxTxPkts128to255Octets", 143),
          ("etherStatsRxTxPkts1519toMTUOctets", 147),
          ("etherStatsRxTxPkts256to511Octets", 144),
          ("etherStatsRxTxPkts512to1023Octets", 145),
          ("etherStatsRxTxPkts64Octets", 141),
          ("etherStatsRxTxPkts65to127Octets", 142),
          ("etherStatsSingleCollisionFrames", 133),
          ("etherStatsTranPkts1024to1518Octets", 112),
          ("etherStatsTranPkts128to255Octets", 109),
          ("etherStatsTranPkts1519toMTUOctets", 140),
          ("etherStatsTranPkts256to511Octets", 110),
          ("etherStatsTranPkts512to1023Octets", 111),
          ("etherStatsTranPkts64Octets", 107),
          ("etherStatsTranPkts65to127Octets", 108),
          ("etherStatsUndersizePkts", 122))
    )



class OwnerString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



# MIB Managed Objects in the order of their OIDs

_RmonTraps_ObjectIdentity = ObjectIdentity
rmonTraps = _RmonTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 0)
)
_TrapCommonObjects_ObjectIdentity = ObjectIdentity
trapCommonObjects = _TrapCommonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 0, 10)
)
_RptAlarmIndex_Type = Unsigned32
_RptAlarmIndex_Object = MibScalar
rptAlarmIndex = _RptAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 0, 10, 10),
    _RptAlarmIndex_Type()
)
rptAlarmIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptAlarmIndex.setStatus("current")
_RptAlarmVariable_Type = PerformanceType
_RptAlarmVariable_Object = MibScalar
rptAlarmVariable = _RptAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 0, 10, 20),
    _RptAlarmVariable_Type()
)
rptAlarmVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptAlarmVariable.setStatus("current")


class _RptAlarmSampleType_Type(Integer32):
    """Custom type rptAlarmSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_RptAlarmSampleType_Type.__name__ = "Integer32"
_RptAlarmSampleType_Object = MibScalar
rptAlarmSampleType = _RptAlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 0, 10, 30),
    _RptAlarmSampleType_Type()
)
rptAlarmSampleType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptAlarmSampleType.setStatus("current")
_RptAlarmValue_Type = Unsigned32
_RptAlarmValue_Object = MibScalar
rptAlarmValue = _RptAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 0, 10, 40),
    _RptAlarmValue_Type()
)
rptAlarmValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptAlarmValue.setStatus("current")
_RptAlarmRisingThreshold_Type = Unsigned32
_RptAlarmRisingThreshold_Object = MibScalar
rptAlarmRisingThreshold = _RptAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 0, 10, 50),
    _RptAlarmRisingThreshold_Type()
)
rptAlarmRisingThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptAlarmRisingThreshold.setStatus("current")
_RptAlarmFallingThreshold_Type = Unsigned32
_RptAlarmFallingThreshold_Object = MibScalar
rptAlarmFallingThreshold = _RptAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 0, 10, 60),
    _RptAlarmFallingThreshold_Type()
)
rptAlarmFallingThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptAlarmFallingThreshold.setStatus("current")
_RptAlarmInterval_Type = Unsigned32
_RptAlarmInterval_Object = MibScalar
rptAlarmInterval = _RptAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 0, 10, 70),
    _RptAlarmInterval_Type()
)
rptAlarmInterval.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptAlarmInterval.setStatus("current")
_RptAlarmDateTime_Type = DateAndTime
_RptAlarmDateTime_Object = MibScalar
rptAlarmDateTime = _RptAlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 0, 10, 80),
    _RptAlarmDateTime_Type()
)
rptAlarmDateTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptAlarmDateTime.setStatus("current")
_OptixTrapsRmon_ObjectIdentity = ObjectIdentity
optixTrapsRmon = _OptixTrapsRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 0, 20)
)
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10)
)
_EtherStatsTable_Object = MibTable
etherStatsTable = _EtherStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10)
)
if mibBuilder.loadTexts:
    etherStatsTable.setStatus("current")
_EtherStatsEntry_Object = MibTableRow
etherStatsEntry = _EtherStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1)
)
etherStatsEntry.setIndexNames(
    (0, "OPTIX-RMON-MIB", "etherStatsIndex"),
)
if mibBuilder.loadTexts:
    etherStatsEntry.setStatus("current")
_EtherStatsIndex_Type = Unsigned32
_EtherStatsIndex_Object = MibTableColumn
etherStatsIndex = _EtherStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 1),
    _EtherStatsIndex_Type()
)
etherStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsIndex.setStatus("current")
_EtherStatsDropEvents_Type = Counter64
_EtherStatsDropEvents_Object = MibTableColumn
etherStatsDropEvents = _EtherStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 3),
    _EtherStatsDropEvents_Type()
)
etherStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsDropEvents.setStatus("current")
_EtherStatsOctets_Type = Counter64
_EtherStatsOctets_Object = MibTableColumn
etherStatsOctets = _EtherStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 4),
    _EtherStatsOctets_Type()
)
etherStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsOctets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsOctets.setUnits("Octets")
_EtherStatsPkts_Type = Counter64
_EtherStatsPkts_Object = MibTableColumn
etherStatsPkts = _EtherStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 5),
    _EtherStatsPkts_Type()
)
etherStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsPkts.setUnits("Packets")
_EtherStatsBroadcastPkts_Type = Counter64
_EtherStatsBroadcastPkts_Object = MibTableColumn
etherStatsBroadcastPkts = _EtherStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 6),
    _EtherStatsBroadcastPkts_Type()
)
etherStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsBroadcastPkts.setUnits("Packets")
_EtherStatsMulticastPkts_Type = Counter64
_EtherStatsMulticastPkts_Object = MibTableColumn
etherStatsMulticastPkts = _EtherStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 7),
    _EtherStatsMulticastPkts_Type()
)
etherStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsMulticastPkts.setUnits("Packets")
_EtherStatsCRCAlignErrors_Type = Counter64
_EtherStatsCRCAlignErrors_Object = MibTableColumn
etherStatsCRCAlignErrors = _EtherStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 8),
    _EtherStatsCRCAlignErrors_Type()
)
etherStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsCRCAlignErrors.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsCRCAlignErrors.setUnits("Packets")
_EtherStatsUndersizePkts_Type = Counter64
_EtherStatsUndersizePkts_Object = MibTableColumn
etherStatsUndersizePkts = _EtherStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 9),
    _EtherStatsUndersizePkts_Type()
)
etherStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsUndersizePkts.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsUndersizePkts.setUnits("Packets")
_EtherStatsOversizePkts_Type = Counter64
_EtherStatsOversizePkts_Object = MibTableColumn
etherStatsOversizePkts = _EtherStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 10),
    _EtherStatsOversizePkts_Type()
)
etherStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsOversizePkts.setUnits("Packets")
_EtherStatsFragments_Type = Counter64
_EtherStatsFragments_Object = MibTableColumn
etherStatsFragments = _EtherStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 11),
    _EtherStatsFragments_Type()
)
etherStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsFragments.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsFragments.setUnits("Packets")
_EtherStatsJabbers_Type = Counter64
_EtherStatsJabbers_Object = MibTableColumn
etherStatsJabbers = _EtherStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 12),
    _EtherStatsJabbers_Type()
)
etherStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsJabbers.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsJabbers.setUnits("Packets")
_EtherStatsCollisions_Type = Counter64
_EtherStatsCollisions_Object = MibTableColumn
etherStatsCollisions = _EtherStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 13),
    _EtherStatsCollisions_Type()
)
etherStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsCollisions.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsCollisions.setUnits("Collisions")
_EtherStatsPkts64Octets_Type = Counter64
_EtherStatsPkts64Octets_Object = MibTableColumn
etherStatsPkts64Octets = _EtherStatsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 14),
    _EtherStatsPkts64Octets_Type()
)
etherStatsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsPkts64Octets.setUnits("Packets")
_EtherStatsPkts65to127Octets_Type = Counter64
_EtherStatsPkts65to127Octets_Object = MibTableColumn
etherStatsPkts65to127Octets = _EtherStatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 15),
    _EtherStatsPkts65to127Octets_Type()
)
etherStatsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsPkts65to127Octets.setUnits("Packets")
_EtherStatsPkts128to255Octets_Type = Counter64
_EtherStatsPkts128to255Octets_Object = MibTableColumn
etherStatsPkts128to255Octets = _EtherStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 16),
    _EtherStatsPkts128to255Octets_Type()
)
etherStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsPkts128to255Octets.setUnits("Packets")
_EtherStatsPkts256to511Octets_Type = Counter64
_EtherStatsPkts256to511Octets_Object = MibTableColumn
etherStatsPkts256to511Octets = _EtherStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 17),
    _EtherStatsPkts256to511Octets_Type()
)
etherStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsPkts256to511Octets.setUnits("Packets")
_EtherStatsPkts512to1023Octets_Type = Counter64
_EtherStatsPkts512to1023Octets_Object = MibTableColumn
etherStatsPkts512to1023Octets = _EtherStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 18),
    _EtherStatsPkts512to1023Octets_Type()
)
etherStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsPkts512to1023Octets.setUnits("Packets")
_EtherStatsPkts1024to1518Octets_Type = Counter64
_EtherStatsPkts1024to1518Octets_Object = MibTableColumn
etherStatsPkts1024to1518Octets = _EtherStatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 10, 1, 19),
    _EtherStatsPkts1024to1518Octets_Type()
)
etherStatsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsPkts1024to1518Octets.setUnits("Packets")
_EtherExStatsTable_Object = MibTable
etherExStatsTable = _EtherExStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20)
)
if mibBuilder.loadTexts:
    etherExStatsTable.setStatus("current")
_EtherExStatsEntry_Object = MibTableRow
etherExStatsEntry = _EtherExStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1)
)
etherExStatsEntry.setIndexNames(
    (0, "OPTIX-RMON-MIB", "etherExStatsIndex"),
)
if mibBuilder.loadTexts:
    etherExStatsEntry.setStatus("current")
_EtherExStatsIndex_Type = Unsigned32
_EtherExStatsIndex_Object = MibTableColumn
etherExStatsIndex = _EtherExStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 1),
    _EtherExStatsIndex_Type()
)
etherExStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExStatsIndex.setStatus("current")
_EtherStatsPkts1519toMTUOctets_Type = Counter64
_EtherStatsPkts1519toMTUOctets_Object = MibTableColumn
etherStatsPkts1519toMTUOctets = _EtherStatsPkts1519toMTUOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 3),
    _EtherStatsPkts1519toMTUOctets_Type()
)
etherStatsPkts1519toMTUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsPkts1519toMTUOctets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsPkts1519toMTUOctets.setUnits("Packets")
_EtherStatsTranPkts64Octets_Type = Counter64
_EtherStatsTranPkts64Octets_Object = MibTableColumn
etherStatsTranPkts64Octets = _EtherStatsTranPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 4),
    _EtherStatsTranPkts64Octets_Type()
)
etherStatsTranPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsTranPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsTranPkts64Octets.setUnits("Packets")
_EtherStatsTranPkts65to127Octets_Type = Counter64
_EtherStatsTranPkts65to127Octets_Object = MibTableColumn
etherStatsTranPkts65to127Octets = _EtherStatsTranPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 5),
    _EtherStatsTranPkts65to127Octets_Type()
)
etherStatsTranPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsTranPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsTranPkts65to127Octets.setUnits("Packets")
_EtherStatsTranPkts128to255Octets_Type = Counter64
_EtherStatsTranPkts128to255Octets_Object = MibTableColumn
etherStatsTranPkts128to255Octets = _EtherStatsTranPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 6),
    _EtherStatsTranPkts128to255Octets_Type()
)
etherStatsTranPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsTranPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsTranPkts128to255Octets.setUnits("Packets")
_EtherStatsTranPkts256to511Octets_Type = Counter64
_EtherStatsTranPkts256to511Octets_Object = MibTableColumn
etherStatsTranPkts256to511Octets = _EtherStatsTranPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 7),
    _EtherStatsTranPkts256to511Octets_Type()
)
etherStatsTranPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsTranPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsTranPkts256to511Octets.setUnits("Packets")
_EtherStatsTranPkts512to1023Octets_Type = Counter64
_EtherStatsTranPkts512to1023Octets_Object = MibTableColumn
etherStatsTranPkts512to1023Octets = _EtherStatsTranPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 8),
    _EtherStatsTranPkts512to1023Octets_Type()
)
etherStatsTranPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsTranPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsTranPkts512to1023Octets.setUnits("Packets")
_EtherStatsTranPkts1024to1518Octets_Type = Counter64
_EtherStatsTranPkts1024to1518Octets_Object = MibTableColumn
etherStatsTranPkts1024to1518Octets = _EtherStatsTranPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 9),
    _EtherStatsTranPkts1024to1518Octets_Type()
)
etherStatsTranPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsTranPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsTranPkts1024to1518Octets.setUnits("Packets")
_EtherStatsTranPkts1519toMTUOctets_Type = Counter64
_EtherStatsTranPkts1519toMTUOctets_Object = MibTableColumn
etherStatsTranPkts1519toMTUOctets = _EtherStatsTranPkts1519toMTUOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 10),
    _EtherStatsTranPkts1519toMTUOctets_Type()
)
etherStatsTranPkts1519toMTUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsTranPkts1519toMTUOctets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsTranPkts1519toMTUOctets.setUnits("Packets")
_EtherStatsRxTxPkts64Octets_Type = Counter64
_EtherStatsRxTxPkts64Octets_Object = MibTableColumn
etherStatsRxTxPkts64Octets = _EtherStatsRxTxPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 11),
    _EtherStatsRxTxPkts64Octets_Type()
)
etherStatsRxTxPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsRxTxPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsRxTxPkts64Octets.setUnits("Packets")
_EtherStatsRxTxPkts65to127Octets_Type = Counter64
_EtherStatsRxTxPkts65to127Octets_Object = MibTableColumn
etherStatsRxTxPkts65to127Octets = _EtherStatsRxTxPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 12),
    _EtherStatsRxTxPkts65to127Octets_Type()
)
etherStatsRxTxPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsRxTxPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsRxTxPkts65to127Octets.setUnits("Packets")
_EtherStatsRxTxPkts128to255Octets_Type = Counter64
_EtherStatsRxTxPkts128to255Octets_Object = MibTableColumn
etherStatsRxTxPkts128to255Octets = _EtherStatsRxTxPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 13),
    _EtherStatsRxTxPkts128to255Octets_Type()
)
etherStatsRxTxPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsRxTxPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsRxTxPkts128to255Octets.setUnits("Packets")
_EtherStatsRxTxPkts256to511Octets_Type = Counter64
_EtherStatsRxTxPkts256to511Octets_Object = MibTableColumn
etherStatsRxTxPkts256to511Octets = _EtherStatsRxTxPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 14),
    _EtherStatsRxTxPkts256to511Octets_Type()
)
etherStatsRxTxPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsRxTxPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsRxTxPkts256to511Octets.setUnits("Packets")
_EtherStatsRxTxPkts512to1023Octets_Type = Counter64
_EtherStatsRxTxPkts512to1023Octets_Object = MibTableColumn
etherStatsRxTxPkts512to1023Octets = _EtherStatsRxTxPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 15),
    _EtherStatsRxTxPkts512to1023Octets_Type()
)
etherStatsRxTxPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsRxTxPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsRxTxPkts512to1023Octets.setUnits("Packets")
_EtherStatsRxTxPkts1024to1518Octets_Type = Counter64
_EtherStatsRxTxPkts1024to1518Octets_Object = MibTableColumn
etherStatsRxTxPkts1024to1518Octets = _EtherStatsRxTxPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 16),
    _EtherStatsRxTxPkts1024to1518Octets_Type()
)
etherStatsRxTxPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsRxTxPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsRxTxPkts1024to1518Octets.setUnits("Packets")
_EtherStatsRxTxPkts1519toMTUOctets_Type = Counter64
_EtherStatsRxTxPkts1519toMTUOctets_Object = MibTableColumn
etherStatsRxTxPkts1519toMTUOctets = _EtherStatsRxTxPkts1519toMTUOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 17),
    _EtherStatsRxTxPkts1519toMTUOctets_Type()
)
etherStatsRxTxPkts1519toMTUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsRxTxPkts1519toMTUOctets.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsRxTxPkts1519toMTUOctets.setUnits("Packets")
_EtherStatsInUcastPkts_Type = Counter64
_EtherStatsInUcastPkts_Object = MibTableColumn
etherStatsInUcastPkts = _EtherStatsInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 18),
    _EtherStatsInUcastPkts_Type()
)
etherStatsInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsInUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsInUcastPkts.setUnits("Packets")
_EtherStatsOutUcastPkts_Type = Counter64
_EtherStatsOutUcastPkts_Object = MibTableColumn
etherStatsOutUcastPkts = _EtherStatsOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 19),
    _EtherStatsOutUcastPkts_Type()
)
etherStatsOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsOutUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsOutUcastPkts.setUnits("Packets")
_EtherStatsInPauseFrames_Type = Counter64
_EtherStatsInPauseFrames_Object = MibTableColumn
etherStatsInPauseFrames = _EtherStatsInPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 20),
    _EtherStatsInPauseFrames_Type()
)
etherStatsInPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsInPauseFrames.setStatus("current")
_EtherStatsOutPauseFrames_Type = Counter64
_EtherStatsOutPauseFrames_Object = MibTableColumn
etherStatsOutPauseFrames = _EtherStatsOutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 21),
    _EtherStatsOutPauseFrames_Type()
)
etherStatsOutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsOutPauseFrames.setStatus("current")
_EtherStatsOutMulticastPkts_Type = Counter64
_EtherStatsOutMulticastPkts_Object = MibTableColumn
etherStatsOutMulticastPkts = _EtherStatsOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 22),
    _EtherStatsOutMulticastPkts_Type()
)
etherStatsOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsOutMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsOutMulticastPkts.setUnits("Packets")
_EtherStatsOutBroadcastPkts_Type = Counter64
_EtherStatsOutBroadcastPkts_Object = MibTableColumn
etherStatsOutBroadcastPkts = _EtherStatsOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 23),
    _EtherStatsOutBroadcastPkts_Type()
)
etherStatsOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsOutBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherStatsOutBroadcastPkts.setUnits("Packets")
_EtherStatsInGoodOctets_Type = Counter64
_EtherStatsInGoodOctets_Object = MibTableColumn
etherStatsInGoodOctets = _EtherStatsInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 24),
    _EtherStatsInGoodOctets_Type()
)
etherStatsInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsInGoodOctets.setStatus("current")
_EtherStatsOutGoodOctets_Type = Counter64
_EtherStatsOutGoodOctets_Object = MibTableColumn
etherStatsOutGoodOctets = _EtherStatsOutGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 25),
    _EtherStatsOutGoodOctets_Type()
)
etherStatsOutGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsOutGoodOctets.setStatus("current")
_EtherStatsInBadOctets_Type = Counter64
_EtherStatsInBadOctets_Object = MibTableColumn
etherStatsInBadOctets = _EtherStatsInBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 26),
    _EtherStatsInBadOctets_Type()
)
etherStatsInBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsInBadOctets.setStatus("current")
_EtherStatsOutBadOctets_Type = Counter64
_EtherStatsOutBadOctets_Object = MibTableColumn
etherStatsOutBadOctets = _EtherStatsOutBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 27),
    _EtherStatsOutBadOctets_Type()
)
etherStatsOutBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsOutBadOctets.setStatus("current")
_EtherStatsAlignmentErrors_Type = Counter64
_EtherStatsAlignmentErrors_Object = MibTableColumn
etherStatsAlignmentErrors = _EtherStatsAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 28),
    _EtherStatsAlignmentErrors_Type()
)
etherStatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsAlignmentErrors.setStatus("current")
_EtherStatsFCSErrors_Type = Counter64
_EtherStatsFCSErrors_Object = MibTableColumn
etherStatsFCSErrors = _EtherStatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 29),
    _EtherStatsFCSErrors_Type()
)
etherStatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsFCSErrors.setStatus("current")
_EtherStatsSingleCollisionFrames_Type = Counter64
_EtherStatsSingleCollisionFrames_Object = MibTableColumn
etherStatsSingleCollisionFrames = _EtherStatsSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 30),
    _EtherStatsSingleCollisionFrames_Type()
)
etherStatsSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsSingleCollisionFrames.setStatus("current")
_EtherStatsMultipleCollisionFrames_Type = Counter64
_EtherStatsMultipleCollisionFrames_Object = MibTableColumn
etherStatsMultipleCollisionFrames = _EtherStatsMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 31),
    _EtherStatsMultipleCollisionFrames_Type()
)
etherStatsMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsMultipleCollisionFrames.setStatus("current")
_EtherStatsLateCollisions_Type = Counter64
_EtherStatsLateCollisions_Object = MibTableColumn
etherStatsLateCollisions = _EtherStatsLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 32),
    _EtherStatsLateCollisions_Type()
)
etherStatsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsLateCollisions.setStatus("current")
_EtherStatsExcessiveCollisions_Type = Counter64
_EtherStatsExcessiveCollisions_Object = MibTableColumn
etherStatsExcessiveCollisions = _EtherStatsExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 33),
    _EtherStatsExcessiveCollisions_Type()
)
etherStatsExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsExcessiveCollisions.setStatus("current")
_EtherStatsDeferredTransmissions_Type = Counter64
_EtherStatsDeferredTransmissions_Object = MibTableColumn
etherStatsDeferredTransmissions = _EtherStatsDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 34),
    _EtherStatsDeferredTransmissions_Type()
)
etherStatsDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsDeferredTransmissions.setStatus("current")
_EtherStatsCarrierSenseErrors_Type = Counter64
_EtherStatsCarrierSenseErrors_Object = MibTableColumn
etherStatsCarrierSenseErrors = _EtherStatsCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 35),
    _EtherStatsCarrierSenseErrors_Type()
)
etherStatsCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsCarrierSenseErrors.setStatus("current")
_EtherStatsInControlFrames_Type = Counter64
_EtherStatsInControlFrames_Object = MibTableColumn
etherStatsInControlFrames = _EtherStatsInControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 36),
    _EtherStatsInControlFrames_Type()
)
etherStatsInControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsInControlFrames.setStatus("current")
_EtherStatsOutControlFrames_Type = Counter64
_EtherStatsOutControlFrames_Object = MibTableColumn
etherStatsOutControlFrames = _EtherStatsOutControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 37),
    _EtherStatsOutControlFrames_Type()
)
etherStatsOutControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsOutControlFrames.setStatus("current")
_EtherStatsOutDropEvents_Type = Counter64
_EtherStatsOutDropEvents_Object = MibTableColumn
etherStatsOutDropEvents = _EtherStatsOutDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 38),
    _EtherStatsOutDropEvents_Type()
)
etherStatsOutDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsOutDropEvents.setStatus("current")
_EtherStatsOutOversizePkts_Type = Counter64
_EtherStatsOutOversizePkts_Object = MibTableColumn
etherStatsOutOversizePkts = _EtherStatsOutOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 39),
    _EtherStatsOutOversizePkts_Type()
)
etherStatsOutOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsOutOversizePkts.setStatus("current")
_EtherStatsOutPkts_Type = Counter64
_EtherStatsOutPkts_Object = MibTableColumn
etherStatsOutPkts = _EtherStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 40),
    _EtherStatsOutPkts_Type()
)
etherStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsOutPkts.setStatus("current")
_EtherStatsOutOctets_Type = Counter64
_EtherStatsOutOctets_Object = MibTableColumn
etherStatsOutOctets = _EtherStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 10, 20, 1, 41),
    _EtherStatsOutOctets_Type()
)
etherStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsOutOctets.setStatus("current")
_History_ObjectIdentity = ObjectIdentity
history = _History_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20)
)
_HistoryControlTable_Object = MibTable
historyControlTable = _HistoryControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 1)
)
if mibBuilder.loadTexts:
    historyControlTable.setStatus("current")
_HistoryControlEntry_Object = MibTableRow
historyControlEntry = _HistoryControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 1, 1)
)
historyControlEntry.setIndexNames(
    (0, "OPTIX-RMON-MIB", "historyControlIndex"),
)
if mibBuilder.loadTexts:
    historyControlEntry.setStatus("current")
_HistoryControlIndex_Type = Unsigned32
_HistoryControlIndex_Object = MibTableColumn
historyControlIndex = _HistoryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 1, 1, 1),
    _HistoryControlIndex_Type()
)
historyControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyControlIndex.setStatus("current")


class _HistoryControlBucketsRequested_Type(Unsigned32):
    """Custom type historyControlBucketsRequested based on Unsigned32"""
    defaultValue = 50


_HistoryControlBucketsRequested_Object = MibTableColumn
historyControlBucketsRequested = _HistoryControlBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 1, 1, 3),
    _HistoryControlBucketsRequested_Type()
)
historyControlBucketsRequested.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    historyControlBucketsRequested.setStatus("current")


class _HistoryControlInterval_Type(Unsigned32):
    """Custom type historyControlInterval based on Unsigned32"""
    defaultValue = 1800


_HistoryControlInterval_Object = MibTableColumn
historyControlInterval = _HistoryControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 1, 1, 5),
    _HistoryControlInterval_Type()
)
historyControlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    historyControlInterval.setStatus("current")
if mibBuilder.loadTexts:
    historyControlInterval.setUnits("Seconds")


class _HistoryControlStatus_Type(Integer32):
    """Custom type historyControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 4),
          ("valid", 1))
    )


_HistoryControlStatus_Type.__name__ = "Integer32"
_HistoryControlStatus_Object = MibTableColumn
historyControlStatus = _HistoryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 1, 1, 7),
    _HistoryControlStatus_Type()
)
historyControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    historyControlStatus.setStatus("current")
_EtherHistoryTable_Object = MibTable
etherHistoryTable = _EtherHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 2)
)
if mibBuilder.loadTexts:
    etherHistoryTable.setStatus("current")
_EtherHistoryEntry_Object = MibTableRow
etherHistoryEntry = _EtherHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 2, 1)
)
etherHistoryEntry.setIndexNames(
    (0, "OPTIX-RMON-MIB", "etherHistoryIndex"),
    (0, "OPTIX-RMON-MIB", "etherHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    etherHistoryEntry.setStatus("current")
_EtherHistoryIndex_Type = Unsigned32
_EtherHistoryIndex_Object = MibTableColumn
etherHistoryIndex = _EtherHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 2, 1, 1),
    _EtherHistoryIndex_Type()
)
etherHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryIndex.setStatus("current")
_EtherHistorySampleIndex_Type = Unsigned32
_EtherHistorySampleIndex_Object = MibTableColumn
etherHistorySampleIndex = _EtherHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 2, 1, 2),
    _EtherHistorySampleIndex_Type()
)
etherHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistorySampleIndex.setStatus("current")
_EtherHistoryIntervalStart_Type = DateAndTime
_EtherHistoryIntervalStart_Object = MibTableColumn
etherHistoryIntervalStart = _EtherHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 2, 1, 3),
    _EtherHistoryIntervalStart_Type()
)
etherHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryIntervalStart.setStatus("current")
_EtherHistoryDropEvents_Type = Counter64
_EtherHistoryDropEvents_Object = MibTableColumn
etherHistoryDropEvents = _EtherHistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 2, 1, 4),
    _EtherHistoryDropEvents_Type()
)
etherHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryDropEvents.setStatus("current")
_EtherHistoryOctets_Type = Counter64
_EtherHistoryOctets_Object = MibTableColumn
etherHistoryOctets = _EtherHistoryOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 2, 1, 5),
    _EtherHistoryOctets_Type()
)
etherHistoryOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryOctets.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryOctets.setUnits("Octets")
_EtherHistoryPkts_Type = Counter64
_EtherHistoryPkts_Object = MibTableColumn
etherHistoryPkts = _EtherHistoryPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 2, 1, 6),
    _EtherHistoryPkts_Type()
)
etherHistoryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryPkts.setUnits("Packets")
_EtherHistoryBroadcastPkts_Type = Counter64
_EtherHistoryBroadcastPkts_Object = MibTableColumn
etherHistoryBroadcastPkts = _EtherHistoryBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 2, 1, 7),
    _EtherHistoryBroadcastPkts_Type()
)
etherHistoryBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryBroadcastPkts.setUnits("Packets")
_EtherHistoryMulticastPkts_Type = Counter64
_EtherHistoryMulticastPkts_Object = MibTableColumn
etherHistoryMulticastPkts = _EtherHistoryMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 2, 1, 8),
    _EtherHistoryMulticastPkts_Type()
)
etherHistoryMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryMulticastPkts.setUnits("Packets")
_EtherHistoryCRCAlignErrors_Type = Counter64
_EtherHistoryCRCAlignErrors_Object = MibTableColumn
etherHistoryCRCAlignErrors = _EtherHistoryCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 2, 1, 9),
    _EtherHistoryCRCAlignErrors_Type()
)
etherHistoryCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryCRCAlignErrors.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryCRCAlignErrors.setUnits("Packets")
_EtherHistoryUndersizePkts_Type = Counter64
_EtherHistoryUndersizePkts_Object = MibTableColumn
etherHistoryUndersizePkts = _EtherHistoryUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 2, 1, 10),
    _EtherHistoryUndersizePkts_Type()
)
etherHistoryUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryUndersizePkts.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryUndersizePkts.setUnits("Packets")
_EtherHistoryOversizePkts_Type = Counter64
_EtherHistoryOversizePkts_Object = MibTableColumn
etherHistoryOversizePkts = _EtherHistoryOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 2, 1, 11),
    _EtherHistoryOversizePkts_Type()
)
etherHistoryOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryOversizePkts.setUnits("Packets")
_EtherHistoryFragments_Type = Counter64
_EtherHistoryFragments_Object = MibTableColumn
etherHistoryFragments = _EtherHistoryFragments_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 2, 1, 12),
    _EtherHistoryFragments_Type()
)
etherHistoryFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryFragments.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryFragments.setUnits("Packets")
_EtherHistoryJabbers_Type = Counter64
_EtherHistoryJabbers_Object = MibTableColumn
etherHistoryJabbers = _EtherHistoryJabbers_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 2, 1, 13),
    _EtherHistoryJabbers_Type()
)
etherHistoryJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryJabbers.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryJabbers.setUnits("Packets")
_EtherHistoryCollisions_Type = Counter64
_EtherHistoryCollisions_Object = MibTableColumn
etherHistoryCollisions = _EtherHistoryCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 2, 1, 14),
    _EtherHistoryCollisions_Type()
)
etherHistoryCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryCollisions.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryCollisions.setUnits("Collisions")
_EtherHistoryUtilization_Type = Counter64
_EtherHistoryUtilization_Object = MibTableColumn
etherHistoryUtilization = _EtherHistoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 2, 1, 15),
    _EtherHistoryUtilization_Type()
)
etherHistoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryUtilization.setStatus("current")
_EtherExHistoryTable_Object = MibTable
etherExHistoryTable = _EtherExHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3)
)
if mibBuilder.loadTexts:
    etherExHistoryTable.setStatus("current")
_EtherExHistoryEntry_Object = MibTableRow
etherExHistoryEntry = _EtherExHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1)
)
etherExHistoryEntry.setIndexNames(
    (0, "OPTIX-RMON-MIB", "etherExHistoryIndex"),
    (0, "OPTIX-RMON-MIB", "etherExHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    etherExHistoryEntry.setStatus("current")
_EtherExHistoryIndex_Type = Unsigned32
_EtherExHistoryIndex_Object = MibTableColumn
etherExHistoryIndex = _EtherExHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 1),
    _EtherExHistoryIndex_Type()
)
etherExHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryIndex.setStatus("current")
_EtherExHistorySampleIndex_Type = Unsigned32
_EtherExHistorySampleIndex_Object = MibTableColumn
etherExHistorySampleIndex = _EtherExHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 2),
    _EtherExHistorySampleIndex_Type()
)
etherExHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistorySampleIndex.setStatus("current")
_EtherExHistoryIntervalStart_Type = DateAndTime
_EtherExHistoryIntervalStart_Object = MibTableColumn
etherExHistoryIntervalStart = _EtherExHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 3),
    _EtherExHistoryIntervalStart_Type()
)
etherExHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryIntervalStart.setStatus("current")
_EtherExHistoryInUcastPkts_Type = Counter64
_EtherExHistoryInUcastPkts_Object = MibTableColumn
etherExHistoryInUcastPkts = _EtherExHistoryInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 4),
    _EtherExHistoryInUcastPkts_Type()
)
etherExHistoryInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryInUcastPkts.setStatus("current")
_EtherExHistoryOutUcastPkts_Type = Counter64
_EtherExHistoryOutUcastPkts_Object = MibTableColumn
etherExHistoryOutUcastPkts = _EtherExHistoryOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 5),
    _EtherExHistoryOutUcastPkts_Type()
)
etherExHistoryOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryOutUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherExHistoryOutUcastPkts.setUnits("Packets")
_EtherExHistoryInPauseFrames_Type = Counter64
_EtherExHistoryInPauseFrames_Object = MibTableColumn
etherExHistoryInPauseFrames = _EtherExHistoryInPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 6),
    _EtherExHistoryInPauseFrames_Type()
)
etherExHistoryInPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryInPauseFrames.setStatus("current")
_EtherExHistoryOutPauseFrames_Type = Counter64
_EtherExHistoryOutPauseFrames_Object = MibTableColumn
etherExHistoryOutPauseFrames = _EtherExHistoryOutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 7),
    _EtherExHistoryOutPauseFrames_Type()
)
etherExHistoryOutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryOutPauseFrames.setStatus("current")
_EtherExHistoryOutMulticastPkts_Type = Counter64
_EtherExHistoryOutMulticastPkts_Object = MibTableColumn
etherExHistoryOutMulticastPkts = _EtherExHistoryOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 8),
    _EtherExHistoryOutMulticastPkts_Type()
)
etherExHistoryOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryOutMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherExHistoryOutMulticastPkts.setUnits("Packets")
_EtherExHistoryOutBroadcastPkts_Type = Counter64
_EtherExHistoryOutBroadcastPkts_Object = MibTableColumn
etherExHistoryOutBroadcastPkts = _EtherExHistoryOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 9),
    _EtherExHistoryOutBroadcastPkts_Type()
)
etherExHistoryOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryOutBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherExHistoryOutBroadcastPkts.setUnits("Packets")
_EtherExHistoryInGoodOctets_Type = Counter64
_EtherExHistoryInGoodOctets_Object = MibTableColumn
etherExHistoryInGoodOctets = _EtherExHistoryInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 10),
    _EtherExHistoryInGoodOctets_Type()
)
etherExHistoryInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryInGoodOctets.setStatus("current")
_EtherExHistoryOutGoodOctets_Type = Counter64
_EtherExHistoryOutGoodOctets_Object = MibTableColumn
etherExHistoryOutGoodOctets = _EtherExHistoryOutGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 11),
    _EtherExHistoryOutGoodOctets_Type()
)
etherExHistoryOutGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryOutGoodOctets.setStatus("current")
_EtherExHistoryInBadOctets_Type = Counter64
_EtherExHistoryInBadOctets_Object = MibTableColumn
etherExHistoryInBadOctets = _EtherExHistoryInBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 12),
    _EtherExHistoryInBadOctets_Type()
)
etherExHistoryInBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryInBadOctets.setStatus("current")
_EtherExHistoryOutBadOctets_Type = Counter64
_EtherExHistoryOutBadOctets_Object = MibTableColumn
etherExHistoryOutBadOctets = _EtherExHistoryOutBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 13),
    _EtherExHistoryOutBadOctets_Type()
)
etherExHistoryOutBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryOutBadOctets.setStatus("current")
_EtherExHistoryAlignmentErrors_Type = Counter64
_EtherExHistoryAlignmentErrors_Object = MibTableColumn
etherExHistoryAlignmentErrors = _EtherExHistoryAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 14),
    _EtherExHistoryAlignmentErrors_Type()
)
etherExHistoryAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryAlignmentErrors.setStatus("current")
_EtherExHistoryFCSErrors_Type = Counter64
_EtherExHistoryFCSErrors_Object = MibTableColumn
etherExHistoryFCSErrors = _EtherExHistoryFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 15),
    _EtherExHistoryFCSErrors_Type()
)
etherExHistoryFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryFCSErrors.setStatus("current")
_EtherExHistorySingleCollisionFrames_Type = Counter64
_EtherExHistorySingleCollisionFrames_Object = MibTableColumn
etherExHistorySingleCollisionFrames = _EtherExHistorySingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 16),
    _EtherExHistorySingleCollisionFrames_Type()
)
etherExHistorySingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistorySingleCollisionFrames.setStatus("current")
_EtherExHistoryMultipleCollisionFrames_Type = Counter64
_EtherExHistoryMultipleCollisionFrames_Object = MibTableColumn
etherExHistoryMultipleCollisionFrames = _EtherExHistoryMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 17),
    _EtherExHistoryMultipleCollisionFrames_Type()
)
etherExHistoryMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryMultipleCollisionFrames.setStatus("current")
_EtherExHistoryLateCollisions_Type = Counter64
_EtherExHistoryLateCollisions_Object = MibTableColumn
etherExHistoryLateCollisions = _EtherExHistoryLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 18),
    _EtherExHistoryLateCollisions_Type()
)
etherExHistoryLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryLateCollisions.setStatus("current")
_EtherExHistoryExcessiveCollisions_Type = Counter64
_EtherExHistoryExcessiveCollisions_Object = MibTableColumn
etherExHistoryExcessiveCollisions = _EtherExHistoryExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 19),
    _EtherExHistoryExcessiveCollisions_Type()
)
etherExHistoryExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryExcessiveCollisions.setStatus("current")
_EtherExHistoryDeferredTransmissions_Type = Counter64
_EtherExHistoryDeferredTransmissions_Object = MibTableColumn
etherExHistoryDeferredTransmissions = _EtherExHistoryDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 20),
    _EtherExHistoryDeferredTransmissions_Type()
)
etherExHistoryDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryDeferredTransmissions.setStatus("current")
_EtherExHistoryCarrierSenseErrors_Type = Counter64
_EtherExHistoryCarrierSenseErrors_Object = MibTableColumn
etherExHistoryCarrierSenseErrors = _EtherExHistoryCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 21),
    _EtherExHistoryCarrierSenseErrors_Type()
)
etherExHistoryCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryCarrierSenseErrors.setStatus("current")
_EtherExHistoryInControlFrames_Type = Counter64
_EtherExHistoryInControlFrames_Object = MibTableColumn
etherExHistoryInControlFrames = _EtherExHistoryInControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 22),
    _EtherExHistoryInControlFrames_Type()
)
etherExHistoryInControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryInControlFrames.setStatus("current")
_EtherExHistoryOutControlFrames_Type = Counter64
_EtherExHistoryOutControlFrames_Object = MibTableColumn
etherExHistoryOutControlFrames = _EtherExHistoryOutControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 23),
    _EtherExHistoryOutControlFrames_Type()
)
etherExHistoryOutControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryOutControlFrames.setStatus("current")
_EtherExHistorysOutDropEvents_Type = Counter64
_EtherExHistorysOutDropEvents_Object = MibTableColumn
etherExHistorysOutDropEvents = _EtherExHistorysOutDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 24),
    _EtherExHistorysOutDropEvents_Type()
)
etherExHistorysOutDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistorysOutDropEvents.setStatus("current")
_EtherExHistorysOutOversizePkts_Type = Counter64
_EtherExHistorysOutOversizePkts_Object = MibTableColumn
etherExHistorysOutOversizePkts = _EtherExHistorysOutOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 25),
    _EtherExHistorysOutOversizePkts_Type()
)
etherExHistorysOutOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistorysOutOversizePkts.setStatus("current")
_EtherExHistoryOutPkts_Type = Counter64
_EtherExHistoryOutPkts_Object = MibTableColumn
etherExHistoryOutPkts = _EtherExHistoryOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 26),
    _EtherExHistoryOutPkts_Type()
)
etherExHistoryOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryOutPkts.setStatus("current")
_EtherExHistoryOutOctets_Type = Counter64
_EtherExHistoryOutOctets_Object = MibTableColumn
etherExHistoryOutOctets = _EtherExHistoryOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 20, 3, 1, 27),
    _EtherExHistoryOutOctets_Type()
)
etherExHistoryOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherExHistoryOutOctets.setStatus("current")
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 30)
)
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 30, 1)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 30, 1, 1)
)
alarmEntry.setIndexNames(
    (0, "OPTIX-RMON-MIB", "alarmIndex"),
    (0, "OPTIX-RMON-MIB", "alarmVariable"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")
_AlarmIndex_Type = Unsigned32
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 30, 1, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("current")
_AlarmVariable_Type = PerformanceType
_AlarmVariable_Object = MibTableColumn
alarmVariable = _AlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 30, 1, 1, 2),
    _AlarmVariable_Type()
)
alarmVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmVariable.setStatus("current")
_AlarmInterval_Type = Unsigned32
_AlarmInterval_Object = MibTableColumn
alarmInterval = _AlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 30, 1, 1, 3),
    _AlarmInterval_Type()
)
alarmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmInterval.setStatus("current")
if mibBuilder.loadTexts:
    alarmInterval.setUnits("Seconds")


class _AlarmSampleType_Type(Integer32):
    """Custom type alarmSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_AlarmSampleType_Type.__name__ = "Integer32"
_AlarmSampleType_Object = MibTableColumn
alarmSampleType = _AlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 30, 1, 1, 4),
    _AlarmSampleType_Type()
)
alarmSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmSampleType.setStatus("current")


class _AlarmStartupAlarm_Type(Integer32):
    """Custom type alarmStartupAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fallingAlarm", 2),
          ("risingAlarm", 1),
          ("risingOrFallingAlarm", 3))
    )


_AlarmStartupAlarm_Type.__name__ = "Integer32"
_AlarmStartupAlarm_Object = MibTableColumn
alarmStartupAlarm = _AlarmStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 30, 1, 1, 6),
    _AlarmStartupAlarm_Type()
)
alarmStartupAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmStartupAlarm.setStatus("current")
_AlarmRisingThreshold_Type = Unsigned32
_AlarmRisingThreshold_Object = MibTableColumn
alarmRisingThreshold = _AlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 30, 1, 1, 7),
    _AlarmRisingThreshold_Type()
)
alarmRisingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmRisingThreshold.setStatus("current")
_AlarmFallingThreshold_Type = Unsigned32
_AlarmFallingThreshold_Object = MibTableColumn
alarmFallingThreshold = _AlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 30, 1, 1, 8),
    _AlarmFallingThreshold_Type()
)
alarmFallingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmFallingThreshold.setStatus("current")


class _AlarmStatus_Type(Integer32):
    """Custom type alarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 4),
          ("valid", 1))
    )


_AlarmStatus_Type.__name__ = "Integer32"
_AlarmStatus_Object = MibTableColumn
alarmStatus = _AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 30, 1, 1, 12),
    _AlarmStatus_Type()
)
alarmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmStatus.setStatus("current")
_OptixRmonMibConformance_ObjectIdentity = ObjectIdentity
optixRmonMibConformance = _OptixRmonMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 40)
)
_OptixRmonMibGroups_ObjectIdentity = ObjectIdentity
optixRmonMibGroups = _OptixRmonMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 40, 1)
)
_OptixRmonMibCompliances_ObjectIdentity = ObjectIdentity
optixRmonMibCompliances = _OptixRmonMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 40, 2)
)

# Managed Objects groups

optixRmonMibObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 40, 1, 1)
)
optixRmonMibObjectGroup.setObjects(
      *(("OPTIX-RMON-MIB", "rptAlarmIndex"),
        ("OPTIX-RMON-MIB", "rptAlarmVariable"),
        ("OPTIX-RMON-MIB", "rptAlarmSampleType"),
        ("OPTIX-RMON-MIB", "rptAlarmValue"),
        ("OPTIX-RMON-MIB", "rptAlarmRisingThreshold"),
        ("OPTIX-RMON-MIB", "rptAlarmFallingThreshold"),
        ("OPTIX-RMON-MIB", "rptAlarmInterval"),
        ("OPTIX-RMON-MIB", "rptAlarmDateTime"),
        ("OPTIX-RMON-MIB", "etherStatsIndex"),
        ("OPTIX-RMON-MIB", "etherStatsDropEvents"),
        ("OPTIX-RMON-MIB", "etherStatsOctets"),
        ("OPTIX-RMON-MIB", "etherStatsPkts"),
        ("OPTIX-RMON-MIB", "etherStatsBroadcastPkts"),
        ("OPTIX-RMON-MIB", "etherStatsMulticastPkts"),
        ("OPTIX-RMON-MIB", "etherStatsCRCAlignErrors"),
        ("OPTIX-RMON-MIB", "etherStatsUndersizePkts"),
        ("OPTIX-RMON-MIB", "etherStatsOversizePkts"),
        ("OPTIX-RMON-MIB", "etherStatsFragments"),
        ("OPTIX-RMON-MIB", "etherStatsJabbers"),
        ("OPTIX-RMON-MIB", "etherStatsCollisions"),
        ("OPTIX-RMON-MIB", "etherStatsPkts64Octets"),
        ("OPTIX-RMON-MIB", "etherStatsPkts65to127Octets"),
        ("OPTIX-RMON-MIB", "etherStatsPkts128to255Octets"),
        ("OPTIX-RMON-MIB", "etherStatsPkts256to511Octets"),
        ("OPTIX-RMON-MIB", "etherStatsPkts512to1023Octets"),
        ("OPTIX-RMON-MIB", "etherStatsPkts1024to1518Octets"),
        ("OPTIX-RMON-MIB", "etherExStatsIndex"),
        ("OPTIX-RMON-MIB", "etherStatsPkts1519toMTUOctets"),
        ("OPTIX-RMON-MIB", "etherStatsTranPkts64Octets"),
        ("OPTIX-RMON-MIB", "etherStatsTranPkts65to127Octets"),
        ("OPTIX-RMON-MIB", "etherStatsTranPkts128to255Octets"),
        ("OPTIX-RMON-MIB", "etherStatsTranPkts256to511Octets"),
        ("OPTIX-RMON-MIB", "etherStatsTranPkts512to1023Octets"),
        ("OPTIX-RMON-MIB", "etherStatsTranPkts1024to1518Octets"),
        ("OPTIX-RMON-MIB", "etherStatsTranPkts1519toMTUOctets"),
        ("OPTIX-RMON-MIB", "etherStatsRxTxPkts64Octets"),
        ("OPTIX-RMON-MIB", "etherStatsRxTxPkts65to127Octets"),
        ("OPTIX-RMON-MIB", "etherStatsRxTxPkts128to255Octets"),
        ("OPTIX-RMON-MIB", "etherStatsRxTxPkts256to511Octets"),
        ("OPTIX-RMON-MIB", "etherStatsRxTxPkts512to1023Octets"),
        ("OPTIX-RMON-MIB", "etherStatsRxTxPkts1024to1518Octets"),
        ("OPTIX-RMON-MIB", "etherStatsRxTxPkts1519toMTUOctets"),
        ("OPTIX-RMON-MIB", "etherStatsInUcastPkts"),
        ("OPTIX-RMON-MIB", "etherStatsOutUcastPkts"),
        ("OPTIX-RMON-MIB", "etherStatsInPauseFrames"),
        ("OPTIX-RMON-MIB", "etherStatsOutPauseFrames"),
        ("OPTIX-RMON-MIB", "etherStatsOutMulticastPkts"),
        ("OPTIX-RMON-MIB", "etherStatsOutBroadcastPkts"),
        ("OPTIX-RMON-MIB", "etherStatsInGoodOctets"),
        ("OPTIX-RMON-MIB", "etherStatsOutGoodOctets"),
        ("OPTIX-RMON-MIB", "etherStatsInBadOctets"),
        ("OPTIX-RMON-MIB", "etherStatsOutBadOctets"),
        ("OPTIX-RMON-MIB", "etherStatsAlignmentErrors"),
        ("OPTIX-RMON-MIB", "etherStatsFCSErrors"),
        ("OPTIX-RMON-MIB", "etherStatsSingleCollisionFrames"),
        ("OPTIX-RMON-MIB", "etherStatsMultipleCollisionFrames"),
        ("OPTIX-RMON-MIB", "etherStatsLateCollisions"),
        ("OPTIX-RMON-MIB", "etherStatsExcessiveCollisions"),
        ("OPTIX-RMON-MIB", "etherStatsDeferredTransmissions"),
        ("OPTIX-RMON-MIB", "etherStatsCarrierSenseErrors"),
        ("OPTIX-RMON-MIB", "etherStatsInControlFrames"),
        ("OPTIX-RMON-MIB", "etherStatsOutControlFrames"),
        ("OPTIX-RMON-MIB", "etherStatsOutDropEvents"),
        ("OPTIX-RMON-MIB", "etherStatsOutOversizePkts"),
        ("OPTIX-RMON-MIB", "etherStatsOutPkts"),
        ("OPTIX-RMON-MIB", "etherStatsOutOctets"),
        ("OPTIX-RMON-MIB", "historyControlIndex"),
        ("OPTIX-RMON-MIB", "historyControlBucketsRequested"),
        ("OPTIX-RMON-MIB", "historyControlInterval"),
        ("OPTIX-RMON-MIB", "historyControlStatus"),
        ("OPTIX-RMON-MIB", "etherHistoryIndex"),
        ("OPTIX-RMON-MIB", "etherHistorySampleIndex"),
        ("OPTIX-RMON-MIB", "etherHistoryIntervalStart"),
        ("OPTIX-RMON-MIB", "etherHistoryDropEvents"),
        ("OPTIX-RMON-MIB", "etherHistoryOctets"),
        ("OPTIX-RMON-MIB", "etherHistoryPkts"),
        ("OPTIX-RMON-MIB", "etherHistoryBroadcastPkts"),
        ("OPTIX-RMON-MIB", "etherHistoryMulticastPkts"),
        ("OPTIX-RMON-MIB", "etherHistoryCRCAlignErrors"),
        ("OPTIX-RMON-MIB", "etherHistoryUndersizePkts"),
        ("OPTIX-RMON-MIB", "etherHistoryOversizePkts"),
        ("OPTIX-RMON-MIB", "etherHistoryFragments"),
        ("OPTIX-RMON-MIB", "etherHistoryJabbers"),
        ("OPTIX-RMON-MIB", "etherHistoryCollisions"),
        ("OPTIX-RMON-MIB", "etherHistoryUtilization"),
        ("OPTIX-RMON-MIB", "etherExHistoryIndex"),
        ("OPTIX-RMON-MIB", "etherExHistorySampleIndex"),
        ("OPTIX-RMON-MIB", "etherExHistoryIntervalStart"),
        ("OPTIX-RMON-MIB", "etherExHistoryInUcastPkts"),
        ("OPTIX-RMON-MIB", "etherExHistoryOutUcastPkts"),
        ("OPTIX-RMON-MIB", "etherExHistoryInPauseFrames"),
        ("OPTIX-RMON-MIB", "etherExHistoryOutPauseFrames"),
        ("OPTIX-RMON-MIB", "etherExHistoryOutMulticastPkts"),
        ("OPTIX-RMON-MIB", "etherExHistoryOutBroadcastPkts"),
        ("OPTIX-RMON-MIB", "etherExHistoryInGoodOctets"),
        ("OPTIX-RMON-MIB", "etherExHistoryOutGoodOctets"),
        ("OPTIX-RMON-MIB", "etherExHistoryInBadOctets"),
        ("OPTIX-RMON-MIB", "etherExHistoryOutBadOctets"),
        ("OPTIX-RMON-MIB", "etherExHistoryAlignmentErrors"),
        ("OPTIX-RMON-MIB", "etherExHistoryFCSErrors"),
        ("OPTIX-RMON-MIB", "etherExHistorySingleCollisionFrames"),
        ("OPTIX-RMON-MIB", "etherExHistoryMultipleCollisionFrames"),
        ("OPTIX-RMON-MIB", "etherExHistoryLateCollisions"),
        ("OPTIX-RMON-MIB", "etherExHistoryExcessiveCollisions"),
        ("OPTIX-RMON-MIB", "etherExHistoryDeferredTransmissions"),
        ("OPTIX-RMON-MIB", "etherExHistoryCarrierSenseErrors"),
        ("OPTIX-RMON-MIB", "etherExHistoryInControlFrames"),
        ("OPTIX-RMON-MIB", "etherExHistoryOutControlFrames"),
        ("OPTIX-RMON-MIB", "etherExHistorysOutDropEvents"),
        ("OPTIX-RMON-MIB", "etherExHistorysOutOversizePkts"),
        ("OPTIX-RMON-MIB", "etherExHistoryOutPkts"),
        ("OPTIX-RMON-MIB", "etherExHistoryOutOctets"),
        ("OPTIX-RMON-MIB", "alarmIndex"),
        ("OPTIX-RMON-MIB", "alarmVariable"),
        ("OPTIX-RMON-MIB", "alarmInterval"),
        ("OPTIX-RMON-MIB", "alarmSampleType"),
        ("OPTIX-RMON-MIB", "alarmStartupAlarm"),
        ("OPTIX-RMON-MIB", "alarmRisingThreshold"),
        ("OPTIX-RMON-MIB", "alarmFallingThreshold"),
        ("OPTIX-RMON-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    optixRmonMibObjectGroup.setStatus("current")


# Notification objects

rmonRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 0, 20, 1)
)
rmonRisingAlarm.setObjects(
      *(("OPTIX-RMON-MIB", "rptAlarmIndex"),
        ("OPTIX-RMON-MIB", "rptAlarmVariable"),
        ("OPTIX-RMON-MIB", "rptAlarmSampleType"),
        ("OPTIX-RMON-MIB", "rptAlarmValue"),
        ("OPTIX-RMON-MIB", "rptAlarmRisingThreshold"),
        ("OPTIX-RMON-MIB", "rptAlarmInterval"),
        ("OPTIX-RMON-MIB", "rptAlarmDateTime"))
)
if mibBuilder.loadTexts:
    rmonRisingAlarm.setStatus(
        "current"
    )

rmonFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 0, 20, 2)
)
rmonFallingAlarm.setObjects(
      *(("OPTIX-RMON-MIB", "rptAlarmIndex"),
        ("OPTIX-RMON-MIB", "rptAlarmVariable"),
        ("OPTIX-RMON-MIB", "rptAlarmSampleType"),
        ("OPTIX-RMON-MIB", "rptAlarmValue"),
        ("OPTIX-RMON-MIB", "rptAlarmFallingThreshold"),
        ("OPTIX-RMON-MIB", "rptAlarmInterval"),
        ("OPTIX-RMON-MIB", "rptAlarmDateTime"))
)
if mibBuilder.loadTexts:
    rmonFallingAlarm.setStatus(
        "current"
    )


# Notifications groups

optixRmonMibNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 40, 1, 2)
)
optixRmonMibNotificationGroup.setObjects(
      *(("OPTIX-RMON-MIB", "rmonRisingAlarm"),
        ("OPTIX-RMON-MIB", "rmonFallingAlarm"))
)
if mibBuilder.loadTexts:
    optixRmonMibNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

optixRmonMibBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 35, 40, 2, 1)
)
if mibBuilder.loadTexts:
    optixRmonMibBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-RMON-MIB",
    **{"PerformanceType": PerformanceType,
       "OwnerString": OwnerString,
       "optixRmonMib": optixRmonMib,
       "rmonTraps": rmonTraps,
       "trapCommonObjects": trapCommonObjects,
       "rptAlarmIndex": rptAlarmIndex,
       "rptAlarmVariable": rptAlarmVariable,
       "rptAlarmSampleType": rptAlarmSampleType,
       "rptAlarmValue": rptAlarmValue,
       "rptAlarmRisingThreshold": rptAlarmRisingThreshold,
       "rptAlarmFallingThreshold": rptAlarmFallingThreshold,
       "rptAlarmInterval": rptAlarmInterval,
       "rptAlarmDateTime": rptAlarmDateTime,
       "optixTrapsRmon": optixTrapsRmon,
       "rmonRisingAlarm": rmonRisingAlarm,
       "rmonFallingAlarm": rmonFallingAlarm,
       "statistics": statistics,
       "etherStatsTable": etherStatsTable,
       "etherStatsEntry": etherStatsEntry,
       "etherStatsIndex": etherStatsIndex,
       "etherStatsDropEvents": etherStatsDropEvents,
       "etherStatsOctets": etherStatsOctets,
       "etherStatsPkts": etherStatsPkts,
       "etherStatsBroadcastPkts": etherStatsBroadcastPkts,
       "etherStatsMulticastPkts": etherStatsMulticastPkts,
       "etherStatsCRCAlignErrors": etherStatsCRCAlignErrors,
       "etherStatsUndersizePkts": etherStatsUndersizePkts,
       "etherStatsOversizePkts": etherStatsOversizePkts,
       "etherStatsFragments": etherStatsFragments,
       "etherStatsJabbers": etherStatsJabbers,
       "etherStatsCollisions": etherStatsCollisions,
       "etherStatsPkts64Octets": etherStatsPkts64Octets,
       "etherStatsPkts65to127Octets": etherStatsPkts65to127Octets,
       "etherStatsPkts128to255Octets": etherStatsPkts128to255Octets,
       "etherStatsPkts256to511Octets": etherStatsPkts256to511Octets,
       "etherStatsPkts512to1023Octets": etherStatsPkts512to1023Octets,
       "etherStatsPkts1024to1518Octets": etherStatsPkts1024to1518Octets,
       "etherExStatsTable": etherExStatsTable,
       "etherExStatsEntry": etherExStatsEntry,
       "etherExStatsIndex": etherExStatsIndex,
       "etherStatsPkts1519toMTUOctets": etherStatsPkts1519toMTUOctets,
       "etherStatsTranPkts64Octets": etherStatsTranPkts64Octets,
       "etherStatsTranPkts65to127Octets": etherStatsTranPkts65to127Octets,
       "etherStatsTranPkts128to255Octets": etherStatsTranPkts128to255Octets,
       "etherStatsTranPkts256to511Octets": etherStatsTranPkts256to511Octets,
       "etherStatsTranPkts512to1023Octets": etherStatsTranPkts512to1023Octets,
       "etherStatsTranPkts1024to1518Octets": etherStatsTranPkts1024to1518Octets,
       "etherStatsTranPkts1519toMTUOctets": etherStatsTranPkts1519toMTUOctets,
       "etherStatsRxTxPkts64Octets": etherStatsRxTxPkts64Octets,
       "etherStatsRxTxPkts65to127Octets": etherStatsRxTxPkts65to127Octets,
       "etherStatsRxTxPkts128to255Octets": etherStatsRxTxPkts128to255Octets,
       "etherStatsRxTxPkts256to511Octets": etherStatsRxTxPkts256to511Octets,
       "etherStatsRxTxPkts512to1023Octets": etherStatsRxTxPkts512to1023Octets,
       "etherStatsRxTxPkts1024to1518Octets": etherStatsRxTxPkts1024to1518Octets,
       "etherStatsRxTxPkts1519toMTUOctets": etherStatsRxTxPkts1519toMTUOctets,
       "etherStatsInUcastPkts": etherStatsInUcastPkts,
       "etherStatsOutUcastPkts": etherStatsOutUcastPkts,
       "etherStatsInPauseFrames": etherStatsInPauseFrames,
       "etherStatsOutPauseFrames": etherStatsOutPauseFrames,
       "etherStatsOutMulticastPkts": etherStatsOutMulticastPkts,
       "etherStatsOutBroadcastPkts": etherStatsOutBroadcastPkts,
       "etherStatsInGoodOctets": etherStatsInGoodOctets,
       "etherStatsOutGoodOctets": etherStatsOutGoodOctets,
       "etherStatsInBadOctets": etherStatsInBadOctets,
       "etherStatsOutBadOctets": etherStatsOutBadOctets,
       "etherStatsAlignmentErrors": etherStatsAlignmentErrors,
       "etherStatsFCSErrors": etherStatsFCSErrors,
       "etherStatsSingleCollisionFrames": etherStatsSingleCollisionFrames,
       "etherStatsMultipleCollisionFrames": etherStatsMultipleCollisionFrames,
       "etherStatsLateCollisions": etherStatsLateCollisions,
       "etherStatsExcessiveCollisions": etherStatsExcessiveCollisions,
       "etherStatsDeferredTransmissions": etherStatsDeferredTransmissions,
       "etherStatsCarrierSenseErrors": etherStatsCarrierSenseErrors,
       "etherStatsInControlFrames": etherStatsInControlFrames,
       "etherStatsOutControlFrames": etherStatsOutControlFrames,
       "etherStatsOutDropEvents": etherStatsOutDropEvents,
       "etherStatsOutOversizePkts": etherStatsOutOversizePkts,
       "etherStatsOutPkts": etherStatsOutPkts,
       "etherStatsOutOctets": etherStatsOutOctets,
       "history": history,
       "historyControlTable": historyControlTable,
       "historyControlEntry": historyControlEntry,
       "historyControlIndex": historyControlIndex,
       "historyControlBucketsRequested": historyControlBucketsRequested,
       "historyControlInterval": historyControlInterval,
       "historyControlStatus": historyControlStatus,
       "etherHistoryTable": etherHistoryTable,
       "etherHistoryEntry": etherHistoryEntry,
       "etherHistoryIndex": etherHistoryIndex,
       "etherHistorySampleIndex": etherHistorySampleIndex,
       "etherHistoryIntervalStart": etherHistoryIntervalStart,
       "etherHistoryDropEvents": etherHistoryDropEvents,
       "etherHistoryOctets": etherHistoryOctets,
       "etherHistoryPkts": etherHistoryPkts,
       "etherHistoryBroadcastPkts": etherHistoryBroadcastPkts,
       "etherHistoryMulticastPkts": etherHistoryMulticastPkts,
       "etherHistoryCRCAlignErrors": etherHistoryCRCAlignErrors,
       "etherHistoryUndersizePkts": etherHistoryUndersizePkts,
       "etherHistoryOversizePkts": etherHistoryOversizePkts,
       "etherHistoryFragments": etherHistoryFragments,
       "etherHistoryJabbers": etherHistoryJabbers,
       "etherHistoryCollisions": etherHistoryCollisions,
       "etherHistoryUtilization": etherHistoryUtilization,
       "etherExHistoryTable": etherExHistoryTable,
       "etherExHistoryEntry": etherExHistoryEntry,
       "etherExHistoryIndex": etherExHistoryIndex,
       "etherExHistorySampleIndex": etherExHistorySampleIndex,
       "etherExHistoryIntervalStart": etherExHistoryIntervalStart,
       "etherExHistoryInUcastPkts": etherExHistoryInUcastPkts,
       "etherExHistoryOutUcastPkts": etherExHistoryOutUcastPkts,
       "etherExHistoryInPauseFrames": etherExHistoryInPauseFrames,
       "etherExHistoryOutPauseFrames": etherExHistoryOutPauseFrames,
       "etherExHistoryOutMulticastPkts": etherExHistoryOutMulticastPkts,
       "etherExHistoryOutBroadcastPkts": etherExHistoryOutBroadcastPkts,
       "etherExHistoryInGoodOctets": etherExHistoryInGoodOctets,
       "etherExHistoryOutGoodOctets": etherExHistoryOutGoodOctets,
       "etherExHistoryInBadOctets": etherExHistoryInBadOctets,
       "etherExHistoryOutBadOctets": etherExHistoryOutBadOctets,
       "etherExHistoryAlignmentErrors": etherExHistoryAlignmentErrors,
       "etherExHistoryFCSErrors": etherExHistoryFCSErrors,
       "etherExHistorySingleCollisionFrames": etherExHistorySingleCollisionFrames,
       "etherExHistoryMultipleCollisionFrames": etherExHistoryMultipleCollisionFrames,
       "etherExHistoryLateCollisions": etherExHistoryLateCollisions,
       "etherExHistoryExcessiveCollisions": etherExHistoryExcessiveCollisions,
       "etherExHistoryDeferredTransmissions": etherExHistoryDeferredTransmissions,
       "etherExHistoryCarrierSenseErrors": etherExHistoryCarrierSenseErrors,
       "etherExHistoryInControlFrames": etherExHistoryInControlFrames,
       "etherExHistoryOutControlFrames": etherExHistoryOutControlFrames,
       "etherExHistorysOutDropEvents": etherExHistorysOutDropEvents,
       "etherExHistorysOutOversizePkts": etherExHistorysOutOversizePkts,
       "etherExHistoryOutPkts": etherExHistoryOutPkts,
       "etherExHistoryOutOctets": etherExHistoryOutOctets,
       "alarm": alarm,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmIndex": alarmIndex,
       "alarmVariable": alarmVariable,
       "alarmInterval": alarmInterval,
       "alarmSampleType": alarmSampleType,
       "alarmStartupAlarm": alarmStartupAlarm,
       "alarmRisingThreshold": alarmRisingThreshold,
       "alarmFallingThreshold": alarmFallingThreshold,
       "alarmStatus": alarmStatus,
       "optixRmonMibConformance": optixRmonMibConformance,
       "optixRmonMibGroups": optixRmonMibGroups,
       "optixRmonMibObjectGroup": optixRmonMibObjectGroup,
       "optixRmonMibNotificationGroup": optixRmonMibNotificationGroup,
       "optixRmonMibCompliances": optixRmonMibCompliances,
       "optixRmonMibBasicCompliance": optixRmonMibBasicCompliance}
)
