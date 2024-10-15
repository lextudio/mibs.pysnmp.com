# SNMP MIB module (ZHONE-RMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-RMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:44 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(ietfDrafts,) = mibBuilder.importSymbols(
    "Zhone",
    "ietfDrafts")


# MODULE-IDENTITY

zhoneRmonMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12)
)
zhoneRmonMibModule.setRevisions(
        ("2010-03-23 13:50",
         "2010-03-15 15:10",
         "2010-03-11 14:26",
         "2010-02-19 12:29")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OwnerString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



class EntryStatus(Integer32, TextualConvention):
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )



# MIB Managed Objects in the order of their OIDs

_ZhoneRmon_ObjectIdentity = ObjectIdentity
zhoneRmon = _ZhoneRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1)
)
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1)
)
_ZhoneEtherStatsTable_Object = MibTable
zhoneEtherStatsTable = _ZhoneEtherStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    zhoneEtherStatsTable.setStatus("current")
_ZhoneEtherStatsEntry_Object = MibTableRow
zhoneEtherStatsEntry = _ZhoneEtherStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1)
)
zhoneEtherStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneEtherStatsEntry.setStatus("current")
_ZhoneEtherStatsDropEvents_Type = Counter64
_ZhoneEtherStatsDropEvents_Object = MibTableColumn
zhoneEtherStatsDropEvents = _ZhoneEtherStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 1),
    _ZhoneEtherStatsDropEvents_Type()
)
zhoneEtherStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsDropEvents.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsDropEvents.setUnits("Events")
_ZhoneEtherStatsDroppedFrames_Type = Counter64
_ZhoneEtherStatsDroppedFrames_Object = MibTableColumn
zhoneEtherStatsDroppedFrames = _ZhoneEtherStatsDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 2),
    _ZhoneEtherStatsDroppedFrames_Type()
)
zhoneEtherStatsDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsDroppedFrames.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsDroppedFrames.setUnits("Frames")
_ZhoneEtherStatsOctets_Type = Counter64
_ZhoneEtherStatsOctets_Object = MibTableColumn
zhoneEtherStatsOctets = _ZhoneEtherStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 3),
    _ZhoneEtherStatsOctets_Type()
)
zhoneEtherStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsOctets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsOctets.setUnits("Octets")
_ZhoneEtherStatsPkts_Type = Counter64
_ZhoneEtherStatsPkts_Object = MibTableColumn
zhoneEtherStatsPkts = _ZhoneEtherStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 4),
    _ZhoneEtherStatsPkts_Type()
)
zhoneEtherStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts.setUnits("Packets")
_ZhoneEtherStatsTxPkts_Type = Counter64
_ZhoneEtherStatsTxPkts_Object = MibTableColumn
zhoneEtherStatsTxPkts = _ZhoneEtherStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 5),
    _ZhoneEtherStatsTxPkts_Type()
)
zhoneEtherStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsTxPkts.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsTxPkts.setUnits("Packets")
_ZhoneEtherStatsRxPkts_Type = Counter64
_ZhoneEtherStatsRxPkts_Object = MibTableColumn
zhoneEtherStatsRxPkts = _ZhoneEtherStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 6),
    _ZhoneEtherStatsRxPkts_Type()
)
zhoneEtherStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsRxPkts.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsRxPkts.setUnits("Packets")
_ZhoneEtherStatsMcastTxBytes_Type = Counter64
_ZhoneEtherStatsMcastTxBytes_Object = MibTableColumn
zhoneEtherStatsMcastTxBytes = _ZhoneEtherStatsMcastTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 7),
    _ZhoneEtherStatsMcastTxBytes_Type()
)
zhoneEtherStatsMcastTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsMcastTxBytes.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsMcastTxBytes.setUnits("Bytes")
_ZhoneEtherStatsMcastRxBytes_Type = Counter64
_ZhoneEtherStatsMcastRxBytes_Object = MibTableColumn
zhoneEtherStatsMcastRxBytes = _ZhoneEtherStatsMcastRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 8),
    _ZhoneEtherStatsMcastRxBytes_Type()
)
zhoneEtherStatsMcastRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsMcastRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsMcastRxBytes.setUnits("Bytes")
_ZhoneEtherStatsMcastRxDroppedBytes_Type = Counter64
_ZhoneEtherStatsMcastRxDroppedBytes_Object = MibTableColumn
zhoneEtherStatsMcastRxDroppedBytes = _ZhoneEtherStatsMcastRxDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 9),
    _ZhoneEtherStatsMcastRxDroppedBytes_Type()
)
zhoneEtherStatsMcastRxDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsMcastRxDroppedBytes.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsMcastRxDroppedBytes.setUnits("Bytes")
_ZhoneEtherStatsAverageTxThroughput_Type = Unsigned32
_ZhoneEtherStatsAverageTxThroughput_Object = MibTableColumn
zhoneEtherStatsAverageTxThroughput = _ZhoneEtherStatsAverageTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 10),
    _ZhoneEtherStatsAverageTxThroughput_Type()
)
zhoneEtherStatsAverageTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsAverageTxThroughput.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsAverageTxThroughput.setUnits("bps")
_ZhoneEtherStatsAverageRxThroughput_Type = Unsigned32
_ZhoneEtherStatsAverageRxThroughput_Object = MibTableColumn
zhoneEtherStatsAverageRxThroughput = _ZhoneEtherStatsAverageRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 11),
    _ZhoneEtherStatsAverageRxThroughput_Type()
)
zhoneEtherStatsAverageRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsAverageRxThroughput.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsAverageRxThroughput.setUnits("bps")
_ZhoneEtherStatsTxBandwidthOccupancy_Type = Integer32
_ZhoneEtherStatsTxBandwidthOccupancy_Object = MibTableColumn
zhoneEtherStatsTxBandwidthOccupancy = _ZhoneEtherStatsTxBandwidthOccupancy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 12),
    _ZhoneEtherStatsTxBandwidthOccupancy_Type()
)
zhoneEtherStatsTxBandwidthOccupancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsTxBandwidthOccupancy.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsTxBandwidthOccupancy.setUnits("Percentage")
_ZhoneEtherStatsRxBandwidthOccupancy_Type = Integer32
_ZhoneEtherStatsRxBandwidthOccupancy_Object = MibTableColumn
zhoneEtherStatsRxBandwidthOccupancy = _ZhoneEtherStatsRxBandwidthOccupancy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 13),
    _ZhoneEtherStatsRxBandwidthOccupancy_Type()
)
zhoneEtherStatsRxBandwidthOccupancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsRxBandwidthOccupancy.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsRxBandwidthOccupancy.setUnits("Percentage")
_ZhoneEtherStatsBroadcastPkts_Type = Counter64
_ZhoneEtherStatsBroadcastPkts_Object = MibTableColumn
zhoneEtherStatsBroadcastPkts = _ZhoneEtherStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 14),
    _ZhoneEtherStatsBroadcastPkts_Type()
)
zhoneEtherStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsBroadcastPkts.setUnits("Packets")
_ZhoneEtherStatsMulticastPkts_Type = Counter64
_ZhoneEtherStatsMulticastPkts_Object = MibTableColumn
zhoneEtherStatsMulticastPkts = _ZhoneEtherStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 15),
    _ZhoneEtherStatsMulticastPkts_Type()
)
zhoneEtherStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsMulticastPkts.setUnits("Packets")
_ZhoneEtherStatsCRCAlignErrors_Type = Counter64
_ZhoneEtherStatsCRCAlignErrors_Object = MibTableColumn
zhoneEtherStatsCRCAlignErrors = _ZhoneEtherStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 16),
    _ZhoneEtherStatsCRCAlignErrors_Type()
)
zhoneEtherStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsCRCAlignErrors.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsCRCAlignErrors.setUnits("Packets")
_ZhoneEtherStatsUndersizePkts_Type = Counter64
_ZhoneEtherStatsUndersizePkts_Object = MibTableColumn
zhoneEtherStatsUndersizePkts = _ZhoneEtherStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 17),
    _ZhoneEtherStatsUndersizePkts_Type()
)
zhoneEtherStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsUndersizePkts.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsUndersizePkts.setUnits("Packets")
_ZhoneEtherStatsOversizePkts_Type = Counter64
_ZhoneEtherStatsOversizePkts_Object = MibTableColumn
zhoneEtherStatsOversizePkts = _ZhoneEtherStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 18),
    _ZhoneEtherStatsOversizePkts_Type()
)
zhoneEtherStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsOversizePkts.setUnits("Packets")
_ZhoneEtherStatsOversizeTxPkts_Type = Counter64
_ZhoneEtherStatsOversizeTxPkts_Object = MibTableColumn
zhoneEtherStatsOversizeTxPkts = _ZhoneEtherStatsOversizeTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 19),
    _ZhoneEtherStatsOversizeTxPkts_Type()
)
zhoneEtherStatsOversizeTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsOversizeTxPkts.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsOversizeTxPkts.setUnits("Packets")
_ZhoneEtherStatsOversizeRxPkts_Type = Counter64
_ZhoneEtherStatsOversizeRxPkts_Object = MibTableColumn
zhoneEtherStatsOversizeRxPkts = _ZhoneEtherStatsOversizeRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 20),
    _ZhoneEtherStatsOversizeRxPkts_Type()
)
zhoneEtherStatsOversizeRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsOversizeRxPkts.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsOversizeRxPkts.setUnits("Packets")
_ZhoneEtherStatsFragments_Type = Counter64
_ZhoneEtherStatsFragments_Object = MibTableColumn
zhoneEtherStatsFragments = _ZhoneEtherStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 21),
    _ZhoneEtherStatsFragments_Type()
)
zhoneEtherStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsFragments.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsFragments.setUnits("Packets")
_ZhoneEtherStatsJabbers_Type = Counter64
_ZhoneEtherStatsJabbers_Object = MibTableColumn
zhoneEtherStatsJabbers = _ZhoneEtherStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 22),
    _ZhoneEtherStatsJabbers_Type()
)
zhoneEtherStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsJabbers.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsJabbers.setUnits("Packets")
_ZhoneEtherStatsCollisions_Type = Counter64
_ZhoneEtherStatsCollisions_Object = MibTableColumn
zhoneEtherStatsCollisions = _ZhoneEtherStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 23),
    _ZhoneEtherStatsCollisions_Type()
)
zhoneEtherStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsCollisions.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsCollisions.setUnits("Packets")
_ZhoneEtherStatsTXNoErrors_Type = Counter64
_ZhoneEtherStatsTXNoErrors_Object = MibTableColumn
zhoneEtherStatsTXNoErrors = _ZhoneEtherStatsTXNoErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 24),
    _ZhoneEtherStatsTXNoErrors_Type()
)
zhoneEtherStatsTXNoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsTXNoErrors.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsTXNoErrors.setUnits("Packets")
_ZhoneEtherStatsRXNoErrors_Type = Counter64
_ZhoneEtherStatsRXNoErrors_Object = MibTableColumn
zhoneEtherStatsRXNoErrors = _ZhoneEtherStatsRXNoErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 25),
    _ZhoneEtherStatsRXNoErrors_Type()
)
zhoneEtherStatsRXNoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsRXNoErrors.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsRXNoErrors.setUnits("Packets")
_ZhoneEtherStatsIPMCBridgedPkts_Type = Counter64
_ZhoneEtherStatsIPMCBridgedPkts_Object = MibTableColumn
zhoneEtherStatsIPMCBridgedPkts = _ZhoneEtherStatsIPMCBridgedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 26),
    _ZhoneEtherStatsIPMCBridgedPkts_Type()
)
zhoneEtherStatsIPMCBridgedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsIPMCBridgedPkts.setStatus("current")
_ZhoneEtherStatsIPMCRoutedPkts_Type = Counter64
_ZhoneEtherStatsIPMCRoutedPkts_Object = MibTableColumn
zhoneEtherStatsIPMCRoutedPkts = _ZhoneEtherStatsIPMCRoutedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 27),
    _ZhoneEtherStatsIPMCRoutedPkts_Type()
)
zhoneEtherStatsIPMCRoutedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsIPMCRoutedPkts.setStatus("current")
_ZhoneEtherStatsIPMCTxDroppedPkts_Type = Counter64
_ZhoneEtherStatsIPMCTxDroppedPkts_Object = MibTableColumn
zhoneEtherStatsIPMCTxDroppedPkts = _ZhoneEtherStatsIPMCTxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 28),
    _ZhoneEtherStatsIPMCTxDroppedPkts_Type()
)
zhoneEtherStatsIPMCTxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsIPMCTxDroppedPkts.setStatus("current")
_ZhoneEtherStatsIPMCRxDroppedPkts_Type = Counter64
_ZhoneEtherStatsIPMCRxDroppedPkts_Object = MibTableColumn
zhoneEtherStatsIPMCRxDroppedPkts = _ZhoneEtherStatsIPMCRxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 29),
    _ZhoneEtherStatsIPMCRxDroppedPkts_Type()
)
zhoneEtherStatsIPMCRxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsIPMCRxDroppedPkts.setStatus("current")
_ZhoneEtherStatsPkts64Octets_Type = Counter64
_ZhoneEtherStatsPkts64Octets_Object = MibTableColumn
zhoneEtherStatsPkts64Octets = _ZhoneEtherStatsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 30),
    _ZhoneEtherStatsPkts64Octets_Type()
)
zhoneEtherStatsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts64Octets.setUnits("Packets")
_ZhoneEtherStatsPkts65to127Octets_Type = Counter64
_ZhoneEtherStatsPkts65to127Octets_Object = MibTableColumn
zhoneEtherStatsPkts65to127Octets = _ZhoneEtherStatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 31),
    _ZhoneEtherStatsPkts65to127Octets_Type()
)
zhoneEtherStatsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts65to127Octets.setUnits("Packets")
_ZhoneEtherStatsPkts128to255Octets_Type = Counter64
_ZhoneEtherStatsPkts128to255Octets_Object = MibTableColumn
zhoneEtherStatsPkts128to255Octets = _ZhoneEtherStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 32),
    _ZhoneEtherStatsPkts128to255Octets_Type()
)
zhoneEtherStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts128to255Octets.setUnits("Packets")
_ZhoneEtherStatsPkts256to511Octets_Type = Counter64
_ZhoneEtherStatsPkts256to511Octets_Object = MibTableColumn
zhoneEtherStatsPkts256to511Octets = _ZhoneEtherStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 33),
    _ZhoneEtherStatsPkts256to511Octets_Type()
)
zhoneEtherStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts256to511Octets.setUnits("Packets")
_ZhoneEtherStatsPkts512to1023Octets_Type = Counter64
_ZhoneEtherStatsPkts512to1023Octets_Object = MibTableColumn
zhoneEtherStatsPkts512to1023Octets = _ZhoneEtherStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 34),
    _ZhoneEtherStatsPkts512to1023Octets_Type()
)
zhoneEtherStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts512to1023Octets.setUnits("Packets")
_ZhoneEtherStatsPkts1024to1518Octets_Type = Counter64
_ZhoneEtherStatsPkts1024to1518Octets_Object = MibTableColumn
zhoneEtherStatsPkts1024to1518Octets = _ZhoneEtherStatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 35),
    _ZhoneEtherStatsPkts1024to1518Octets_Type()
)
zhoneEtherStatsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts1024to1518Octets.setUnits("Packets")
_ZhoneEtherStatsPkts1519to2047Octets_Type = Counter64
_ZhoneEtherStatsPkts1519to2047Octets_Object = MibTableColumn
zhoneEtherStatsPkts1519to2047Octets = _ZhoneEtherStatsPkts1519to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 36),
    _ZhoneEtherStatsPkts1519to2047Octets_Type()
)
zhoneEtherStatsPkts1519to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts1519to2047Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts1519to2047Octets.setUnits("Packets")
_ZhoneEtherStatsPkts2048to4095Octets_Type = Counter64
_ZhoneEtherStatsPkts2048to4095Octets_Object = MibTableColumn
zhoneEtherStatsPkts2048to4095Octets = _ZhoneEtherStatsPkts2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 37),
    _ZhoneEtherStatsPkts2048to4095Octets_Type()
)
zhoneEtherStatsPkts2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts2048to4095Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts2048to4095Octets.setUnits("Packets")
_ZhoneEtherStatsPkts4095to9216Octets_Type = Counter64
_ZhoneEtherStatsPkts4095to9216Octets_Object = MibTableColumn
zhoneEtherStatsPkts4095to9216Octets = _ZhoneEtherStatsPkts4095to9216Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 38),
    _ZhoneEtherStatsPkts4095to9216Octets_Type()
)
zhoneEtherStatsPkts4095to9216Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts4095to9216Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsPkts4095to9216Octets.setUnits("Packets")
_ZhoneEtherStatsReceivedPkts64Octets_Type = Counter64
_ZhoneEtherStatsReceivedPkts64Octets_Object = MibTableColumn
zhoneEtherStatsReceivedPkts64Octets = _ZhoneEtherStatsReceivedPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 39),
    _ZhoneEtherStatsReceivedPkts64Octets_Type()
)
zhoneEtherStatsReceivedPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts64Octets.setUnits("Packets")
_ZhoneEtherStatsReceivedPkts65to127Octets_Type = Counter64
_ZhoneEtherStatsReceivedPkts65to127Octets_Object = MibTableColumn
zhoneEtherStatsReceivedPkts65to127Octets = _ZhoneEtherStatsReceivedPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 40),
    _ZhoneEtherStatsReceivedPkts65to127Octets_Type()
)
zhoneEtherStatsReceivedPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts65to127Octets.setUnits("Packets")
_ZhoneEtherStatsReceivedPkts128to255Octets_Type = Counter64
_ZhoneEtherStatsReceivedPkts128to255Octets_Object = MibTableColumn
zhoneEtherStatsReceivedPkts128to255Octets = _ZhoneEtherStatsReceivedPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 41),
    _ZhoneEtherStatsReceivedPkts128to255Octets_Type()
)
zhoneEtherStatsReceivedPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts128to255Octets.setUnits("Packets")
_ZhoneEtherStatsReceivedPkts256to511Octets_Type = Counter64
_ZhoneEtherStatsReceivedPkts256to511Octets_Object = MibTableColumn
zhoneEtherStatsReceivedPkts256to511Octets = _ZhoneEtherStatsReceivedPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 42),
    _ZhoneEtherStatsReceivedPkts256to511Octets_Type()
)
zhoneEtherStatsReceivedPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts256to511Octets.setUnits("Packets")
_ZhoneEtherStatsReceivedPkts512to1023Octets_Type = Counter64
_ZhoneEtherStatsReceivedPkts512to1023Octets_Object = MibTableColumn
zhoneEtherStatsReceivedPkts512to1023Octets = _ZhoneEtherStatsReceivedPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 43),
    _ZhoneEtherStatsReceivedPkts512to1023Octets_Type()
)
zhoneEtherStatsReceivedPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts512to1023Octets.setUnits("Packets")
_ZhoneEtherStatsReceivedPkts1024to1518Octets_Type = Counter64
_ZhoneEtherStatsReceivedPkts1024to1518Octets_Object = MibTableColumn
zhoneEtherStatsReceivedPkts1024to1518Octets = _ZhoneEtherStatsReceivedPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 44),
    _ZhoneEtherStatsReceivedPkts1024to1518Octets_Type()
)
zhoneEtherStatsReceivedPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts1024to1518Octets.setUnits("Packets")
_ZhoneEtherStatsReceivedPkts1519to2047Octets_Type = Counter64
_ZhoneEtherStatsReceivedPkts1519to2047Octets_Object = MibTableColumn
zhoneEtherStatsReceivedPkts1519to2047Octets = _ZhoneEtherStatsReceivedPkts1519to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 45),
    _ZhoneEtherStatsReceivedPkts1519to2047Octets_Type()
)
zhoneEtherStatsReceivedPkts1519to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts1519to2047Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts1519to2047Octets.setUnits("Packets")
_ZhoneEtherStatsReceivedPkts2048to4095Octets_Type = Counter64
_ZhoneEtherStatsReceivedPkts2048to4095Octets_Object = MibTableColumn
zhoneEtherStatsReceivedPkts2048to4095Octets = _ZhoneEtherStatsReceivedPkts2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 46),
    _ZhoneEtherStatsReceivedPkts2048to4095Octets_Type()
)
zhoneEtherStatsReceivedPkts2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts2048to4095Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts2048to4095Octets.setUnits("Packets")
_ZhoneEtherStatsReceivedPkts4095to9216Octets_Type = Counter64
_ZhoneEtherStatsReceivedPkts4095to9216Octets_Object = MibTableColumn
zhoneEtherStatsReceivedPkts4095to9216Octets = _ZhoneEtherStatsReceivedPkts4095to9216Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 47),
    _ZhoneEtherStatsReceivedPkts4095to9216Octets_Type()
)
zhoneEtherStatsReceivedPkts4095to9216Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts4095to9216Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsReceivedPkts4095to9216Octets.setUnits("Packets")
_ZhoneEtherStatsTransmittedPkts64Octets_Type = Counter64
_ZhoneEtherStatsTransmittedPkts64Octets_Object = MibTableColumn
zhoneEtherStatsTransmittedPkts64Octets = _ZhoneEtherStatsTransmittedPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 48),
    _ZhoneEtherStatsTransmittedPkts64Octets_Type()
)
zhoneEtherStatsTransmittedPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts64Octets.setUnits("Packets")
_ZhoneEtherStatsTransmittedPkts65to127Octets_Type = Counter64
_ZhoneEtherStatsTransmittedPkts65to127Octets_Object = MibTableColumn
zhoneEtherStatsTransmittedPkts65to127Octets = _ZhoneEtherStatsTransmittedPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 49),
    _ZhoneEtherStatsTransmittedPkts65to127Octets_Type()
)
zhoneEtherStatsTransmittedPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts65to127Octets.setUnits("Packets")
_ZhoneEtherStatsTransmittedPkts128to255Octets_Type = Counter64
_ZhoneEtherStatsTransmittedPkts128to255Octets_Object = MibTableColumn
zhoneEtherStatsTransmittedPkts128to255Octets = _ZhoneEtherStatsTransmittedPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 50),
    _ZhoneEtherStatsTransmittedPkts128to255Octets_Type()
)
zhoneEtherStatsTransmittedPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts128to255Octets.setUnits("Packets")
_ZhoneEtherStatsTransmittedPkts256to511Octets_Type = Counter64
_ZhoneEtherStatsTransmittedPkts256to511Octets_Object = MibTableColumn
zhoneEtherStatsTransmittedPkts256to511Octets = _ZhoneEtherStatsTransmittedPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 51),
    _ZhoneEtherStatsTransmittedPkts256to511Octets_Type()
)
zhoneEtherStatsTransmittedPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts256to511Octets.setUnits("Packets")
_ZhoneEtherStatsTransmittedPkts512to1023Octets_Type = Counter64
_ZhoneEtherStatsTransmittedPkts512to1023Octets_Object = MibTableColumn
zhoneEtherStatsTransmittedPkts512to1023Octets = _ZhoneEtherStatsTransmittedPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 52),
    _ZhoneEtherStatsTransmittedPkts512to1023Octets_Type()
)
zhoneEtherStatsTransmittedPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts512to1023Octets.setUnits("Packets")
_ZhoneEtherStatsTransmittedPkts1024to1518Octets_Type = Counter64
_ZhoneEtherStatsTransmittedPkts1024to1518Octets_Object = MibTableColumn
zhoneEtherStatsTransmittedPkts1024to1518Octets = _ZhoneEtherStatsTransmittedPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 53),
    _ZhoneEtherStatsTransmittedPkts1024to1518Octets_Type()
)
zhoneEtherStatsTransmittedPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts1024to1518Octets.setUnits("Packets")
_ZhoneEtherStatsTransmittedPkts1519to2047Octets_Type = Counter64
_ZhoneEtherStatsTransmittedPkts1519to2047Octets_Object = MibTableColumn
zhoneEtherStatsTransmittedPkts1519to2047Octets = _ZhoneEtherStatsTransmittedPkts1519to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 54),
    _ZhoneEtherStatsTransmittedPkts1519to2047Octets_Type()
)
zhoneEtherStatsTransmittedPkts1519to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts1519to2047Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts1519to2047Octets.setUnits("Packets")
_ZhoneEtherStatsTransmittedPkts2048to4095Octets_Type = Counter64
_ZhoneEtherStatsTransmittedPkts2048to4095Octets_Object = MibTableColumn
zhoneEtherStatsTransmittedPkts2048to4095Octets = _ZhoneEtherStatsTransmittedPkts2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 55),
    _ZhoneEtherStatsTransmittedPkts2048to4095Octets_Type()
)
zhoneEtherStatsTransmittedPkts2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts2048to4095Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts2048to4095Octets.setUnits("Packets")
_ZhoneEtherStatsTransmittedPkts4095to9216Octets_Type = Counter64
_ZhoneEtherStatsTransmittedPkts4095to9216Octets_Object = MibTableColumn
zhoneEtherStatsTransmittedPkts4095to9216Octets = _ZhoneEtherStatsTransmittedPkts4095to9216Octets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 1, 1, 1, 56),
    _ZhoneEtherStatsTransmittedPkts4095to9216Octets_Type()
)
zhoneEtherStatsTransmittedPkts4095to9216Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts4095to9216Octets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneEtherStatsTransmittedPkts4095to9216Octets.setUnits("Packets")
_History_ObjectIdentity = ObjectIdentity
history = _History_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2)
)
_HistoryControlTable_Object = MibTable
historyControlTable = _HistoryControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    historyControlTable.setStatus("current")
_HistoryControlEntry_Object = MibTableRow
historyControlEntry = _HistoryControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 1, 1)
)
historyControlEntry.setIndexNames(
    (0, "ZHONE-RMON-MIB", "historyControlIndex"),
)
if mibBuilder.loadTexts:
    historyControlEntry.setStatus("current")


class _HistoryControlIndex_Type(Integer32):
    """Custom type historyControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HistoryControlIndex_Type.__name__ = "Integer32"
_HistoryControlIndex_Object = MibTableColumn
historyControlIndex = _HistoryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 1, 1, 1),
    _HistoryControlIndex_Type()
)
historyControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyControlIndex.setStatus("current")
_HistoryControlDataSource_Type = ObjectIdentifier
_HistoryControlDataSource_Object = MibTableColumn
historyControlDataSource = _HistoryControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 1, 1, 2),
    _HistoryControlDataSource_Type()
)
historyControlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    historyControlDataSource.setStatus("current")


class _HistoryControlBucketsRequested_Type(Integer32):
    """Custom type historyControlBucketsRequested based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HistoryControlBucketsRequested_Type.__name__ = "Integer32"
_HistoryControlBucketsRequested_Object = MibTableColumn
historyControlBucketsRequested = _HistoryControlBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 1, 1, 3),
    _HistoryControlBucketsRequested_Type()
)
historyControlBucketsRequested.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    historyControlBucketsRequested.setStatus("current")


class _HistoryControlBucketsGranted_Type(Integer32):
    """Custom type historyControlBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HistoryControlBucketsGranted_Type.__name__ = "Integer32"
_HistoryControlBucketsGranted_Object = MibTableColumn
historyControlBucketsGranted = _HistoryControlBucketsGranted_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 1, 1, 4),
    _HistoryControlBucketsGranted_Type()
)
historyControlBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyControlBucketsGranted.setStatus("current")


class _HistoryControlInterval_Type(Integer32):
    """Custom type historyControlInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_HistoryControlInterval_Type.__name__ = "Integer32"
_HistoryControlInterval_Object = MibTableColumn
historyControlInterval = _HistoryControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 1, 1, 5),
    _HistoryControlInterval_Type()
)
historyControlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    historyControlInterval.setStatus("current")
if mibBuilder.loadTexts:
    historyControlInterval.setUnits("Seconds")
_HistoryControlOwner_Type = OwnerString
_HistoryControlOwner_Object = MibTableColumn
historyControlOwner = _HistoryControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 1, 1, 6),
    _HistoryControlOwner_Type()
)
historyControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    historyControlOwner.setStatus("current")
_HistoryControlStatus_Type = EntryStatus
_HistoryControlStatus_Object = MibTableColumn
historyControlStatus = _HistoryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 1, 1, 7),
    _HistoryControlStatus_Type()
)
historyControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    historyControlStatus.setStatus("current")
_EtherHistoryTable_Object = MibTable
etherHistoryTable = _EtherHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    etherHistoryTable.setStatus("current")
_EtherHistoryEntry_Object = MibTableRow
etherHistoryEntry = _EtherHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 2, 1)
)
etherHistoryEntry.setIndexNames(
    (0, "ZHONE-RMON-MIB", "etherHistoryIndex"),
    (0, "ZHONE-RMON-MIB", "etherHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    etherHistoryEntry.setStatus("current")


class _EtherHistoryIndex_Type(Integer32):
    """Custom type etherHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtherHistoryIndex_Type.__name__ = "Integer32"
_EtherHistoryIndex_Object = MibTableColumn
etherHistoryIndex = _EtherHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 2, 1, 1),
    _EtherHistoryIndex_Type()
)
etherHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryIndex.setStatus("current")


class _EtherHistorySampleIndex_Type(Integer32):
    """Custom type etherHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtherHistorySampleIndex_Type.__name__ = "Integer32"
_EtherHistorySampleIndex_Object = MibTableColumn
etherHistorySampleIndex = _EtherHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 2, 1, 2),
    _EtherHistorySampleIndex_Type()
)
etherHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistorySampleIndex.setStatus("current")
_EtherHistoryIntervalStart_Type = TimeTicks
_EtherHistoryIntervalStart_Object = MibTableColumn
etherHistoryIntervalStart = _EtherHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 2, 1, 3),
    _EtherHistoryIntervalStart_Type()
)
etherHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryIntervalStart.setStatus("current")
_EtherHistoryDropEvents_Type = Counter32
_EtherHistoryDropEvents_Object = MibTableColumn
etherHistoryDropEvents = _EtherHistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 2, 1, 4),
    _EtherHistoryDropEvents_Type()
)
etherHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryDropEvents.setStatus("current")
_EtherHistoryOctets_Type = Counter32
_EtherHistoryOctets_Object = MibTableColumn
etherHistoryOctets = _EtherHistoryOctets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 2, 1, 5),
    _EtherHistoryOctets_Type()
)
etherHistoryOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryOctets.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryOctets.setUnits("Octets")
_EtherHistoryPkts_Type = Counter32
_EtherHistoryPkts_Object = MibTableColumn
etherHistoryPkts = _EtherHistoryPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 2, 1, 6),
    _EtherHistoryPkts_Type()
)
etherHistoryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryPkts.setUnits("Packets")
_EtherHistoryBroadcastPkts_Type = Counter32
_EtherHistoryBroadcastPkts_Object = MibTableColumn
etherHistoryBroadcastPkts = _EtherHistoryBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 2, 1, 7),
    _EtherHistoryBroadcastPkts_Type()
)
etherHistoryBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryBroadcastPkts.setUnits("Packets")
_EtherHistoryMulticastPkts_Type = Counter32
_EtherHistoryMulticastPkts_Object = MibTableColumn
etherHistoryMulticastPkts = _EtherHistoryMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 2, 1, 8),
    _EtherHistoryMulticastPkts_Type()
)
etherHistoryMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryMulticastPkts.setUnits("Packets")
_EtherHistoryCRCAlignErrors_Type = Counter32
_EtherHistoryCRCAlignErrors_Object = MibTableColumn
etherHistoryCRCAlignErrors = _EtherHistoryCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 2, 1, 9),
    _EtherHistoryCRCAlignErrors_Type()
)
etherHistoryCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryCRCAlignErrors.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryCRCAlignErrors.setUnits("Packets")
_EtherHistoryUndersizePkts_Type = Counter32
_EtherHistoryUndersizePkts_Object = MibTableColumn
etherHistoryUndersizePkts = _EtherHistoryUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 2, 1, 10),
    _EtherHistoryUndersizePkts_Type()
)
etherHistoryUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryUndersizePkts.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryUndersizePkts.setUnits("Packets")
_EtherHistoryOversizePkts_Type = Counter32
_EtherHistoryOversizePkts_Object = MibTableColumn
etherHistoryOversizePkts = _EtherHistoryOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 2, 1, 11),
    _EtherHistoryOversizePkts_Type()
)
etherHistoryOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryOversizePkts.setUnits("Packets")
_EtherHistoryFragments_Type = Counter32
_EtherHistoryFragments_Object = MibTableColumn
etherHistoryFragments = _EtherHistoryFragments_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 2, 1, 12),
    _EtherHistoryFragments_Type()
)
etherHistoryFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryFragments.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryFragments.setUnits("Packets")
_EtherHistoryJabbers_Type = Counter32
_EtherHistoryJabbers_Object = MibTableColumn
etherHistoryJabbers = _EtherHistoryJabbers_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 2, 1, 13),
    _EtherHistoryJabbers_Type()
)
etherHistoryJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryJabbers.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryJabbers.setUnits("Packets")
_EtherHistoryCollisions_Type = Counter32
_EtherHistoryCollisions_Object = MibTableColumn
etherHistoryCollisions = _EtherHistoryCollisions_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 2, 1, 14),
    _EtherHistoryCollisions_Type()
)
etherHistoryCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryCollisions.setStatus("current")
if mibBuilder.loadTexts:
    etherHistoryCollisions.setUnits("Collisions")


class _EtherHistoryUtilization_Type(Integer32):
    """Custom type etherHistoryUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EtherHistoryUtilization_Type.__name__ = "Integer32"
_EtherHistoryUtilization_Object = MibTableColumn
etherHistoryUtilization = _EtherHistoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 2, 2, 1, 15),
    _EtherHistoryUtilization_Type()
)
etherHistoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryUtilization.setStatus("current")
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 3)
)
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 3, 1, 1)
)
alarmEntry.setIndexNames(
    (0, "ZHONE-RMON-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")


class _AlarmIndex_Type(Integer32):
    """Custom type alarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlarmIndex_Type.__name__ = "Integer32"
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 3, 1, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("current")
_AlarmInterval_Type = Integer32
_AlarmInterval_Object = MibTableColumn
alarmInterval = _AlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 3, 1, 1, 2),
    _AlarmInterval_Type()
)
alarmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmInterval.setStatus("current")
if mibBuilder.loadTexts:
    alarmInterval.setUnits("Seconds")
_AlarmVariable_Type = ObjectIdentifier
_AlarmVariable_Object = MibTableColumn
alarmVariable = _AlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 3, 1, 1, 3),
    _AlarmVariable_Type()
)
alarmVariable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmVariable.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 3, 1, 1, 4),
    _AlarmSampleType_Type()
)
alarmSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmSampleType.setStatus("current")
_AlarmValue_Type = Integer32
_AlarmValue_Object = MibTableColumn
alarmValue = _AlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 3, 1, 1, 5),
    _AlarmValue_Type()
)
alarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmValue.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 3, 1, 1, 6),
    _AlarmStartupAlarm_Type()
)
alarmStartupAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmStartupAlarm.setStatus("current")
_AlarmRisingThreshold_Type = Integer32
_AlarmRisingThreshold_Object = MibTableColumn
alarmRisingThreshold = _AlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 3, 1, 1, 7),
    _AlarmRisingThreshold_Type()
)
alarmRisingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmRisingThreshold.setStatus("current")
_AlarmFallingThreshold_Type = Integer32
_AlarmFallingThreshold_Object = MibTableColumn
alarmFallingThreshold = _AlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 3, 1, 1, 8),
    _AlarmFallingThreshold_Type()
)
alarmFallingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmFallingThreshold.setStatus("current")


class _AlarmRisingEventIndex_Type(Integer32):
    """Custom type alarmRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlarmRisingEventIndex_Type.__name__ = "Integer32"
_AlarmRisingEventIndex_Object = MibTableColumn
alarmRisingEventIndex = _AlarmRisingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 3, 1, 1, 9),
    _AlarmRisingEventIndex_Type()
)
alarmRisingEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmRisingEventIndex.setStatus("current")


class _AlarmFallingEventIndex_Type(Integer32):
    """Custom type alarmFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlarmFallingEventIndex_Type.__name__ = "Integer32"
_AlarmFallingEventIndex_Object = MibTableColumn
alarmFallingEventIndex = _AlarmFallingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 3, 1, 1, 10),
    _AlarmFallingEventIndex_Type()
)
alarmFallingEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmFallingEventIndex.setStatus("current")
_AlarmOwner_Type = OwnerString
_AlarmOwner_Object = MibTableColumn
alarmOwner = _AlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 3, 1, 1, 11),
    _AlarmOwner_Type()
)
alarmOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmOwner.setStatus("current")
_AlarmStatus_Type = EntryStatus
_AlarmStatus_Object = MibTableColumn
alarmStatus = _AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 3, 1, 1, 12),
    _AlarmStatus_Type()
)
alarmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmStatus.setStatus("current")
_Hosts_ObjectIdentity = ObjectIdentity
hosts = _Hosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4)
)
_HostControlTable_Object = MibTable
hostControlTable = _HostControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hostControlTable.setStatus("current")
_HostControlEntry_Object = MibTableRow
hostControlEntry = _HostControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 1, 1)
)
hostControlEntry.setIndexNames(
    (0, "ZHONE-RMON-MIB", "hostControlIndex"),
)
if mibBuilder.loadTexts:
    hostControlEntry.setStatus("current")


class _HostControlIndex_Type(Integer32):
    """Custom type hostControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostControlIndex_Type.__name__ = "Integer32"
_HostControlIndex_Object = MibTableColumn
hostControlIndex = _HostControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 1, 1, 1),
    _HostControlIndex_Type()
)
hostControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostControlIndex.setStatus("current")
_HostControlDataSource_Type = ObjectIdentifier
_HostControlDataSource_Object = MibTableColumn
hostControlDataSource = _HostControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 1, 1, 2),
    _HostControlDataSource_Type()
)
hostControlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostControlDataSource.setStatus("current")
_HostControlTableSize_Type = Integer32
_HostControlTableSize_Object = MibTableColumn
hostControlTableSize = _HostControlTableSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 1, 1, 3),
    _HostControlTableSize_Type()
)
hostControlTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostControlTableSize.setStatus("current")
_HostControlLastDeleteTime_Type = TimeTicks
_HostControlLastDeleteTime_Object = MibTableColumn
hostControlLastDeleteTime = _HostControlLastDeleteTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 1, 1, 4),
    _HostControlLastDeleteTime_Type()
)
hostControlLastDeleteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostControlLastDeleteTime.setStatus("current")
_HostControlOwner_Type = OwnerString
_HostControlOwner_Object = MibTableColumn
hostControlOwner = _HostControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 1, 1, 5),
    _HostControlOwner_Type()
)
hostControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostControlOwner.setStatus("current")
_HostControlStatus_Type = EntryStatus
_HostControlStatus_Object = MibTableColumn
hostControlStatus = _HostControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 1, 1, 6),
    _HostControlStatus_Type()
)
hostControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostControlStatus.setStatus("current")
_HostTable_Object = MibTable
hostTable = _HostTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hostTable.setStatus("current")
_HostEntry_Object = MibTableRow
hostEntry = _HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 2, 1)
)
hostEntry.setIndexNames(
    (0, "ZHONE-RMON-MIB", "hostIndex"),
    (0, "ZHONE-RMON-MIB", "hostAddress"),
)
if mibBuilder.loadTexts:
    hostEntry.setStatus("current")
_HostAddress_Type = OctetString
_HostAddress_Object = MibTableColumn
hostAddress = _HostAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 2, 1, 1),
    _HostAddress_Type()
)
hostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostAddress.setStatus("current")


class _HostCreationOrder_Type(Integer32):
    """Custom type hostCreationOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostCreationOrder_Type.__name__ = "Integer32"
_HostCreationOrder_Object = MibTableColumn
hostCreationOrder = _HostCreationOrder_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 2, 1, 2),
    _HostCreationOrder_Type()
)
hostCreationOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostCreationOrder.setStatus("current")


class _HostIndex_Type(Integer32):
    """Custom type hostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostIndex_Type.__name__ = "Integer32"
_HostIndex_Object = MibTableColumn
hostIndex = _HostIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 2, 1, 3),
    _HostIndex_Type()
)
hostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIndex.setStatus("current")
_HostInPkts_Type = Counter32
_HostInPkts_Object = MibTableColumn
hostInPkts = _HostInPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 2, 1, 4),
    _HostInPkts_Type()
)
hostInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostInPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostInPkts.setUnits("Packets")
_HostOutPkts_Type = Counter32
_HostOutPkts_Object = MibTableColumn
hostOutPkts = _HostOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 2, 1, 5),
    _HostOutPkts_Type()
)
hostOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostOutPkts.setUnits("Packets")
_HostInOctets_Type = Counter32
_HostInOctets_Object = MibTableColumn
hostInOctets = _HostInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 2, 1, 6),
    _HostInOctets_Type()
)
hostInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostInOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostInOctets.setUnits("Octets")
_HostOutOctets_Type = Counter32
_HostOutOctets_Object = MibTableColumn
hostOutOctets = _HostOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 2, 1, 7),
    _HostOutOctets_Type()
)
hostOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostOutOctets.setUnits("Octets")
_HostOutErrors_Type = Counter32
_HostOutErrors_Object = MibTableColumn
hostOutErrors = _HostOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 2, 1, 8),
    _HostOutErrors_Type()
)
hostOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostOutErrors.setStatus("current")
if mibBuilder.loadTexts:
    hostOutErrors.setUnits("Packets")
_HostOutBroadcastPkts_Type = Counter32
_HostOutBroadcastPkts_Object = MibTableColumn
hostOutBroadcastPkts = _HostOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 2, 1, 9),
    _HostOutBroadcastPkts_Type()
)
hostOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostOutBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostOutBroadcastPkts.setUnits("Packets")
_HostOutMulticastPkts_Type = Counter32
_HostOutMulticastPkts_Object = MibTableColumn
hostOutMulticastPkts = _HostOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 2, 1, 10),
    _HostOutMulticastPkts_Type()
)
hostOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostOutMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostOutMulticastPkts.setUnits("Packets")
_HostTimeTable_Object = MibTable
hostTimeTable = _HostTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hostTimeTable.setStatus("current")
_HostTimeEntry_Object = MibTableRow
hostTimeEntry = _HostTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 3, 1)
)
hostTimeEntry.setIndexNames(
    (0, "ZHONE-RMON-MIB", "hostTimeIndex"),
    (0, "ZHONE-RMON-MIB", "hostTimeCreationOrder"),
)
if mibBuilder.loadTexts:
    hostTimeEntry.setStatus("current")
_HostTimeAddress_Type = OctetString
_HostTimeAddress_Object = MibTableColumn
hostTimeAddress = _HostTimeAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 3, 1, 1),
    _HostTimeAddress_Type()
)
hostTimeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeAddress.setStatus("current")


class _HostTimeCreationOrder_Type(Integer32):
    """Custom type hostTimeCreationOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostTimeCreationOrder_Type.__name__ = "Integer32"
_HostTimeCreationOrder_Object = MibTableColumn
hostTimeCreationOrder = _HostTimeCreationOrder_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 3, 1, 2),
    _HostTimeCreationOrder_Type()
)
hostTimeCreationOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeCreationOrder.setStatus("current")


class _HostTimeIndex_Type(Integer32):
    """Custom type hostTimeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostTimeIndex_Type.__name__ = "Integer32"
_HostTimeIndex_Object = MibTableColumn
hostTimeIndex = _HostTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 3, 1, 3),
    _HostTimeIndex_Type()
)
hostTimeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeIndex.setStatus("current")
_HostTimeInPkts_Type = Counter32
_HostTimeInPkts_Object = MibTableColumn
hostTimeInPkts = _HostTimeInPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 3, 1, 4),
    _HostTimeInPkts_Type()
)
hostTimeInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeInPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeInPkts.setUnits("Packets")
_HostTimeOutPkts_Type = Counter32
_HostTimeOutPkts_Object = MibTableColumn
hostTimeOutPkts = _HostTimeOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 3, 1, 5),
    _HostTimeOutPkts_Type()
)
hostTimeOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeOutPkts.setUnits("Packets")
_HostTimeInOctets_Type = Counter32
_HostTimeInOctets_Object = MibTableColumn
hostTimeInOctets = _HostTimeInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 3, 1, 6),
    _HostTimeInOctets_Type()
)
hostTimeInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeInOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeInOctets.setUnits("Octets")
_HostTimeOutOctets_Type = Counter32
_HostTimeOutOctets_Object = MibTableColumn
hostTimeOutOctets = _HostTimeOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 3, 1, 7),
    _HostTimeOutOctets_Type()
)
hostTimeOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeOutOctets.setUnits("Octets")
_HostTimeOutErrors_Type = Counter32
_HostTimeOutErrors_Object = MibTableColumn
hostTimeOutErrors = _HostTimeOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 3, 1, 8),
    _HostTimeOutErrors_Type()
)
hostTimeOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeOutErrors.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeOutErrors.setUnits("Packets")
_HostTimeOutBroadcastPkts_Type = Counter32
_HostTimeOutBroadcastPkts_Object = MibTableColumn
hostTimeOutBroadcastPkts = _HostTimeOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 3, 1, 9),
    _HostTimeOutBroadcastPkts_Type()
)
hostTimeOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeOutBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeOutBroadcastPkts.setUnits("Packets")
_HostTimeOutMulticastPkts_Type = Counter32
_HostTimeOutMulticastPkts_Object = MibTableColumn
hostTimeOutMulticastPkts = _HostTimeOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 4, 3, 1, 10),
    _HostTimeOutMulticastPkts_Type()
)
hostTimeOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeOutMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    hostTimeOutMulticastPkts.setUnits("Packets")
_HostTopN_ObjectIdentity = ObjectIdentity
hostTopN = _HostTopN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5)
)
_HostTopNControlTable_Object = MibTable
hostTopNControlTable = _HostTopNControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hostTopNControlTable.setStatus("current")
_HostTopNControlEntry_Object = MibTableRow
hostTopNControlEntry = _HostTopNControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 1, 1)
)
hostTopNControlEntry.setIndexNames(
    (0, "ZHONE-RMON-MIB", "hostTopNControlIndex"),
)
if mibBuilder.loadTexts:
    hostTopNControlEntry.setStatus("current")


class _HostTopNControlIndex_Type(Integer32):
    """Custom type hostTopNControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostTopNControlIndex_Type.__name__ = "Integer32"
_HostTopNControlIndex_Object = MibTableColumn
hostTopNControlIndex = _HostTopNControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 1, 1, 1),
    _HostTopNControlIndex_Type()
)
hostTopNControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNControlIndex.setStatus("current")


class _HostTopNHostIndex_Type(Integer32):
    """Custom type hostTopNHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostTopNHostIndex_Type.__name__ = "Integer32"
_HostTopNHostIndex_Object = MibTableColumn
hostTopNHostIndex = _HostTopNHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 1, 1, 2),
    _HostTopNHostIndex_Type()
)
hostTopNHostIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostTopNHostIndex.setStatus("current")


class _HostTopNRateBase_Type(Integer32):
    """Custom type hostTopNRateBase based on Integer32"""
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
        *(("hostTopNInOctets", 3),
          ("hostTopNInPkts", 1),
          ("hostTopNOutBroadcastPkts", 6),
          ("hostTopNOutErrors", 5),
          ("hostTopNOutMulticastPkts", 7),
          ("hostTopNOutOctets", 4),
          ("hostTopNOutPkts", 2))
    )


_HostTopNRateBase_Type.__name__ = "Integer32"
_HostTopNRateBase_Object = MibTableColumn
hostTopNRateBase = _HostTopNRateBase_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 1, 1, 3),
    _HostTopNRateBase_Type()
)
hostTopNRateBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostTopNRateBase.setStatus("current")


class _HostTopNTimeRemaining_Type(Integer32):
    """Custom type hostTopNTimeRemaining based on Integer32"""
    defaultValue = 0


_HostTopNTimeRemaining_Object = MibTableColumn
hostTopNTimeRemaining = _HostTopNTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 1, 1, 4),
    _HostTopNTimeRemaining_Type()
)
hostTopNTimeRemaining.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostTopNTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    hostTopNTimeRemaining.setUnits("Seconds")


class _HostTopNDuration_Type(Integer32):
    """Custom type hostTopNDuration based on Integer32"""
    defaultValue = 0


_HostTopNDuration_Object = MibTableColumn
hostTopNDuration = _HostTopNDuration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 1, 1, 5),
    _HostTopNDuration_Type()
)
hostTopNDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNDuration.setStatus("current")
if mibBuilder.loadTexts:
    hostTopNDuration.setUnits("Seconds")


class _HostTopNRequestedSize_Type(Integer32):
    """Custom type hostTopNRequestedSize based on Integer32"""
    defaultValue = 10


_HostTopNRequestedSize_Object = MibTableColumn
hostTopNRequestedSize = _HostTopNRequestedSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 1, 1, 6),
    _HostTopNRequestedSize_Type()
)
hostTopNRequestedSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostTopNRequestedSize.setStatus("current")
_HostTopNGrantedSize_Type = Integer32
_HostTopNGrantedSize_Object = MibTableColumn
hostTopNGrantedSize = _HostTopNGrantedSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 1, 1, 7),
    _HostTopNGrantedSize_Type()
)
hostTopNGrantedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNGrantedSize.setStatus("current")
_HostTopNStartTime_Type = TimeTicks
_HostTopNStartTime_Object = MibTableColumn
hostTopNStartTime = _HostTopNStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 1, 1, 8),
    _HostTopNStartTime_Type()
)
hostTopNStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNStartTime.setStatus("current")
_HostTopNOwner_Type = OwnerString
_HostTopNOwner_Object = MibTableColumn
hostTopNOwner = _HostTopNOwner_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 1, 1, 9),
    _HostTopNOwner_Type()
)
hostTopNOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostTopNOwner.setStatus("current")
_HostTopNStatus_Type = EntryStatus
_HostTopNStatus_Object = MibTableColumn
hostTopNStatus = _HostTopNStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 1, 1, 10),
    _HostTopNStatus_Type()
)
hostTopNStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hostTopNStatus.setStatus("current")
_HostTopNTable_Object = MibTable
hostTopNTable = _HostTopNTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hostTopNTable.setStatus("current")
_HostTopNEntry_Object = MibTableRow
hostTopNEntry = _HostTopNEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 2, 1)
)
hostTopNEntry.setIndexNames(
    (0, "ZHONE-RMON-MIB", "hostTopNReport"),
    (0, "ZHONE-RMON-MIB", "hostTopNIndex"),
)
if mibBuilder.loadTexts:
    hostTopNEntry.setStatus("current")


class _HostTopNReport_Type(Integer32):
    """Custom type hostTopNReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostTopNReport_Type.__name__ = "Integer32"
_HostTopNReport_Object = MibTableColumn
hostTopNReport = _HostTopNReport_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 2, 1, 1),
    _HostTopNReport_Type()
)
hostTopNReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNReport.setStatus("current")


class _HostTopNIndex_Type(Integer32):
    """Custom type hostTopNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostTopNIndex_Type.__name__ = "Integer32"
_HostTopNIndex_Object = MibTableColumn
hostTopNIndex = _HostTopNIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 2, 1, 2),
    _HostTopNIndex_Type()
)
hostTopNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNIndex.setStatus("current")
_HostTopNAddress_Type = OctetString
_HostTopNAddress_Object = MibTableColumn
hostTopNAddress = _HostTopNAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 2, 1, 3),
    _HostTopNAddress_Type()
)
hostTopNAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNAddress.setStatus("current")
_HostTopNRate_Type = Integer32
_HostTopNRate_Object = MibTableColumn
hostTopNRate = _HostTopNRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 5, 2, 1, 4),
    _HostTopNRate_Type()
)
hostTopNRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNRate.setStatus("current")
_Matrix_ObjectIdentity = ObjectIdentity
matrix = _Matrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6)
)
_MatrixControlTable_Object = MibTable
matrixControlTable = _MatrixControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 1)
)
if mibBuilder.loadTexts:
    matrixControlTable.setStatus("current")
_MatrixControlEntry_Object = MibTableRow
matrixControlEntry = _MatrixControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 1, 1)
)
matrixControlEntry.setIndexNames(
    (0, "ZHONE-RMON-MIB", "matrixControlIndex"),
)
if mibBuilder.loadTexts:
    matrixControlEntry.setStatus("current")


class _MatrixControlIndex_Type(Integer32):
    """Custom type matrixControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MatrixControlIndex_Type.__name__ = "Integer32"
_MatrixControlIndex_Object = MibTableColumn
matrixControlIndex = _MatrixControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 1, 1, 1),
    _MatrixControlIndex_Type()
)
matrixControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixControlIndex.setStatus("current")
_MatrixControlDataSource_Type = ObjectIdentifier
_MatrixControlDataSource_Object = MibTableColumn
matrixControlDataSource = _MatrixControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 1, 1, 2),
    _MatrixControlDataSource_Type()
)
matrixControlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matrixControlDataSource.setStatus("current")
_MatrixControlTableSize_Type = Integer32
_MatrixControlTableSize_Object = MibTableColumn
matrixControlTableSize = _MatrixControlTableSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 1, 1, 3),
    _MatrixControlTableSize_Type()
)
matrixControlTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixControlTableSize.setStatus("current")
_MatrixControlLastDeleteTime_Type = TimeTicks
_MatrixControlLastDeleteTime_Object = MibTableColumn
matrixControlLastDeleteTime = _MatrixControlLastDeleteTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 1, 1, 4),
    _MatrixControlLastDeleteTime_Type()
)
matrixControlLastDeleteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixControlLastDeleteTime.setStatus("current")
_MatrixControlOwner_Type = OwnerString
_MatrixControlOwner_Object = MibTableColumn
matrixControlOwner = _MatrixControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 1, 1, 5),
    _MatrixControlOwner_Type()
)
matrixControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matrixControlOwner.setStatus("current")
_MatrixControlStatus_Type = EntryStatus
_MatrixControlStatus_Object = MibTableColumn
matrixControlStatus = _MatrixControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 1, 1, 6),
    _MatrixControlStatus_Type()
)
matrixControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matrixControlStatus.setStatus("current")
_MatrixSDTable_Object = MibTable
matrixSDTable = _MatrixSDTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 2)
)
if mibBuilder.loadTexts:
    matrixSDTable.setStatus("current")
_MatrixSDEntry_Object = MibTableRow
matrixSDEntry = _MatrixSDEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 2, 1)
)
matrixSDEntry.setIndexNames(
    (0, "ZHONE-RMON-MIB", "matrixSDIndex"),
    (0, "ZHONE-RMON-MIB", "matrixSDSourceAddress"),
    (0, "ZHONE-RMON-MIB", "matrixSDDestAddress"),
)
if mibBuilder.loadTexts:
    matrixSDEntry.setStatus("current")
_MatrixSDSourceAddress_Type = OctetString
_MatrixSDSourceAddress_Object = MibTableColumn
matrixSDSourceAddress = _MatrixSDSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 2, 1, 1),
    _MatrixSDSourceAddress_Type()
)
matrixSDSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDSourceAddress.setStatus("current")
_MatrixSDDestAddress_Type = OctetString
_MatrixSDDestAddress_Object = MibTableColumn
matrixSDDestAddress = _MatrixSDDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 2, 1, 2),
    _MatrixSDDestAddress_Type()
)
matrixSDDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDDestAddress.setStatus("current")


class _MatrixSDIndex_Type(Integer32):
    """Custom type matrixSDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MatrixSDIndex_Type.__name__ = "Integer32"
_MatrixSDIndex_Object = MibTableColumn
matrixSDIndex = _MatrixSDIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 2, 1, 3),
    _MatrixSDIndex_Type()
)
matrixSDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDIndex.setStatus("current")
_MatrixSDPkts_Type = Counter32
_MatrixSDPkts_Object = MibTableColumn
matrixSDPkts = _MatrixSDPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 2, 1, 4),
    _MatrixSDPkts_Type()
)
matrixSDPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDPkts.setStatus("current")
if mibBuilder.loadTexts:
    matrixSDPkts.setUnits("Packets")
_MatrixSDOctets_Type = Counter32
_MatrixSDOctets_Object = MibTableColumn
matrixSDOctets = _MatrixSDOctets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 2, 1, 5),
    _MatrixSDOctets_Type()
)
matrixSDOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDOctets.setStatus("current")
if mibBuilder.loadTexts:
    matrixSDOctets.setUnits("Octets")
_MatrixSDErrors_Type = Counter32
_MatrixSDErrors_Object = MibTableColumn
matrixSDErrors = _MatrixSDErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 2, 1, 6),
    _MatrixSDErrors_Type()
)
matrixSDErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDErrors.setStatus("current")
if mibBuilder.loadTexts:
    matrixSDErrors.setUnits("Packets")
_MatrixDSTable_Object = MibTable
matrixDSTable = _MatrixDSTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 3)
)
if mibBuilder.loadTexts:
    matrixDSTable.setStatus("current")
_MatrixDSEntry_Object = MibTableRow
matrixDSEntry = _MatrixDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 3, 1)
)
matrixDSEntry.setIndexNames(
    (0, "ZHONE-RMON-MIB", "matrixDSIndex"),
    (0, "ZHONE-RMON-MIB", "matrixDSDestAddress"),
    (0, "ZHONE-RMON-MIB", "matrixDSSourceAddress"),
)
if mibBuilder.loadTexts:
    matrixDSEntry.setStatus("current")
_MatrixDSSourceAddress_Type = OctetString
_MatrixDSSourceAddress_Object = MibTableColumn
matrixDSSourceAddress = _MatrixDSSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 3, 1, 1),
    _MatrixDSSourceAddress_Type()
)
matrixDSSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSSourceAddress.setStatus("current")
_MatrixDSDestAddress_Type = OctetString
_MatrixDSDestAddress_Object = MibTableColumn
matrixDSDestAddress = _MatrixDSDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 3, 1, 2),
    _MatrixDSDestAddress_Type()
)
matrixDSDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSDestAddress.setStatus("current")


class _MatrixDSIndex_Type(Integer32):
    """Custom type matrixDSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MatrixDSIndex_Type.__name__ = "Integer32"
_MatrixDSIndex_Object = MibTableColumn
matrixDSIndex = _MatrixDSIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 3, 1, 3),
    _MatrixDSIndex_Type()
)
matrixDSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSIndex.setStatus("current")
_MatrixDSPkts_Type = Counter32
_MatrixDSPkts_Object = MibTableColumn
matrixDSPkts = _MatrixDSPkts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 3, 1, 4),
    _MatrixDSPkts_Type()
)
matrixDSPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSPkts.setStatus("current")
if mibBuilder.loadTexts:
    matrixDSPkts.setUnits("Packets")
_MatrixDSOctets_Type = Counter32
_MatrixDSOctets_Object = MibTableColumn
matrixDSOctets = _MatrixDSOctets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 3, 1, 5),
    _MatrixDSOctets_Type()
)
matrixDSOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSOctets.setStatus("current")
if mibBuilder.loadTexts:
    matrixDSOctets.setUnits("Octets")
_MatrixDSErrors_Type = Counter32
_MatrixDSErrors_Object = MibTableColumn
matrixDSErrors = _MatrixDSErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 6, 3, 1, 6),
    _MatrixDSErrors_Type()
)
matrixDSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSErrors.setStatus("current")
if mibBuilder.loadTexts:
    matrixDSErrors.setUnits("Packets")
_ZhoneRmonFilter_ObjectIdentity = ObjectIdentity
zhoneRmonFilter = _ZhoneRmonFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7)
)
_FilterTable_Object = MibTable
filterTable = _FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 1)
)
if mibBuilder.loadTexts:
    filterTable.setStatus("current")
_FilterEntry_Object = MibTableRow
filterEntry = _FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 1, 1)
)
filterEntry.setIndexNames(
    (0, "ZHONE-RMON-MIB", "filterIndex"),
)
if mibBuilder.loadTexts:
    filterEntry.setStatus("current")


class _FilterIndex_Type(Integer32):
    """Custom type filterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FilterIndex_Type.__name__ = "Integer32"
_FilterIndex_Object = MibTableColumn
filterIndex = _FilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 1, 1, 1),
    _FilterIndex_Type()
)
filterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterIndex.setStatus("current")


class _FilterChannelIndex_Type(Integer32):
    """Custom type filterChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FilterChannelIndex_Type.__name__ = "Integer32"
_FilterChannelIndex_Object = MibTableColumn
filterChannelIndex = _FilterChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 1, 1, 2),
    _FilterChannelIndex_Type()
)
filterChannelIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterChannelIndex.setStatus("current")


class _FilterPktDataOffset_Type(Integer32):
    """Custom type filterPktDataOffset based on Integer32"""
    defaultValue = 0


_FilterPktDataOffset_Object = MibTableColumn
filterPktDataOffset = _FilterPktDataOffset_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 1, 1, 3),
    _FilterPktDataOffset_Type()
)
filterPktDataOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterPktDataOffset.setStatus("current")
if mibBuilder.loadTexts:
    filterPktDataOffset.setUnits("Octets")
_FilterPktData_Type = OctetString
_FilterPktData_Object = MibTableColumn
filterPktData = _FilterPktData_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 1, 1, 4),
    _FilterPktData_Type()
)
filterPktData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterPktData.setStatus("current")
_FilterPktDataMask_Type = OctetString
_FilterPktDataMask_Object = MibTableColumn
filterPktDataMask = _FilterPktDataMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 1, 1, 5),
    _FilterPktDataMask_Type()
)
filterPktDataMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterPktDataMask.setStatus("current")
_FilterPktDataNotMask_Type = OctetString
_FilterPktDataNotMask_Object = MibTableColumn
filterPktDataNotMask = _FilterPktDataNotMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 1, 1, 6),
    _FilterPktDataNotMask_Type()
)
filterPktDataNotMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterPktDataNotMask.setStatus("current")
_FilterPktStatus_Type = Integer32
_FilterPktStatus_Object = MibTableColumn
filterPktStatus = _FilterPktStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 1, 1, 7),
    _FilterPktStatus_Type()
)
filterPktStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterPktStatus.setStatus("current")
_FilterPktStatusMask_Type = Integer32
_FilterPktStatusMask_Object = MibTableColumn
filterPktStatusMask = _FilterPktStatusMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 1, 1, 8),
    _FilterPktStatusMask_Type()
)
filterPktStatusMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterPktStatusMask.setStatus("current")
_FilterPktStatusNotMask_Type = Integer32
_FilterPktStatusNotMask_Object = MibTableColumn
filterPktStatusNotMask = _FilterPktStatusNotMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 1, 1, 9),
    _FilterPktStatusNotMask_Type()
)
filterPktStatusNotMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterPktStatusNotMask.setStatus("current")
_FilterOwner_Type = OwnerString
_FilterOwner_Object = MibTableColumn
filterOwner = _FilterOwner_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 1, 1, 10),
    _FilterOwner_Type()
)
filterOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterOwner.setStatus("current")
_FilterStatus_Type = EntryStatus
_FilterStatus_Object = MibTableColumn
filterStatus = _FilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 1, 1, 11),
    _FilterStatus_Type()
)
filterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterStatus.setStatus("current")
_ChannelTable_Object = MibTable
channelTable = _ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 2)
)
if mibBuilder.loadTexts:
    channelTable.setStatus("current")
_ChannelEntry_Object = MibTableRow
channelEntry = _ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 2, 1)
)
channelEntry.setIndexNames(
    (0, "ZHONE-RMON-MIB", "channelIndex"),
)
if mibBuilder.loadTexts:
    channelEntry.setStatus("current")


class _ChannelIndex_Type(Integer32):
    """Custom type channelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChannelIndex_Type.__name__ = "Integer32"
_ChannelIndex_Object = MibTableColumn
channelIndex = _ChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 2, 1, 1),
    _ChannelIndex_Type()
)
channelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelIndex.setStatus("current")


class _ChannelIfIndex_Type(Integer32):
    """Custom type channelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChannelIfIndex_Type.__name__ = "Integer32"
_ChannelIfIndex_Object = MibTableColumn
channelIfIndex = _ChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 2, 1, 2),
    _ChannelIfIndex_Type()
)
channelIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelIfIndex.setStatus("current")


class _ChannelAcceptType_Type(Integer32):
    """Custom type channelAcceptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acceptFailed", 2),
          ("acceptMatched", 1))
    )


_ChannelAcceptType_Type.__name__ = "Integer32"
_ChannelAcceptType_Object = MibTableColumn
channelAcceptType = _ChannelAcceptType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 2, 1, 3),
    _ChannelAcceptType_Type()
)
channelAcceptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelAcceptType.setStatus("current")


class _ChannelDataControl_Type(Integer32):
    """Custom type channelDataControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ChannelDataControl_Type.__name__ = "Integer32"
_ChannelDataControl_Object = MibTableColumn
channelDataControl = _ChannelDataControl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 2, 1, 4),
    _ChannelDataControl_Type()
)
channelDataControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelDataControl.setStatus("current")


class _ChannelTurnOnEventIndex_Type(Integer32):
    """Custom type channelTurnOnEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChannelTurnOnEventIndex_Type.__name__ = "Integer32"
_ChannelTurnOnEventIndex_Object = MibTableColumn
channelTurnOnEventIndex = _ChannelTurnOnEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 2, 1, 5),
    _ChannelTurnOnEventIndex_Type()
)
channelTurnOnEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelTurnOnEventIndex.setStatus("current")


class _ChannelTurnOffEventIndex_Type(Integer32):
    """Custom type channelTurnOffEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChannelTurnOffEventIndex_Type.__name__ = "Integer32"
_ChannelTurnOffEventIndex_Object = MibTableColumn
channelTurnOffEventIndex = _ChannelTurnOffEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 2, 1, 6),
    _ChannelTurnOffEventIndex_Type()
)
channelTurnOffEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelTurnOffEventIndex.setStatus("current")


class _ChannelEventIndex_Type(Integer32):
    """Custom type channelEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChannelEventIndex_Type.__name__ = "Integer32"
_ChannelEventIndex_Object = MibTableColumn
channelEventIndex = _ChannelEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 2, 1, 7),
    _ChannelEventIndex_Type()
)
channelEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelEventIndex.setStatus("current")


class _ChannelEventStatus_Type(Integer32):
    """Custom type channelEventStatus based on Integer32"""
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
        *(("eventAlwaysReady", 3),
          ("eventFired", 2),
          ("eventReady", 1))
    )


_ChannelEventStatus_Type.__name__ = "Integer32"
_ChannelEventStatus_Object = MibTableColumn
channelEventStatus = _ChannelEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 2, 1, 8),
    _ChannelEventStatus_Type()
)
channelEventStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelEventStatus.setStatus("current")
_ChannelMatches_Type = Counter32
_ChannelMatches_Object = MibTableColumn
channelMatches = _ChannelMatches_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 2, 1, 9),
    _ChannelMatches_Type()
)
channelMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelMatches.setStatus("current")
if mibBuilder.loadTexts:
    channelMatches.setUnits("Packets")


class _ChannelDescription_Type(DisplayString):
    """Custom type channelDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ChannelDescription_Type.__name__ = "DisplayString"
_ChannelDescription_Object = MibTableColumn
channelDescription = _ChannelDescription_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 2, 1, 10),
    _ChannelDescription_Type()
)
channelDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelDescription.setStatus("current")
_ChannelOwner_Type = OwnerString
_ChannelOwner_Object = MibTableColumn
channelOwner = _ChannelOwner_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 2, 1, 11),
    _ChannelOwner_Type()
)
channelOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelOwner.setStatus("current")
_ChannelStatus_Type = EntryStatus
_ChannelStatus_Object = MibTableColumn
channelStatus = _ChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 7, 2, 1, 12),
    _ChannelStatus_Type()
)
channelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelStatus.setStatus("current")
_Capture_ObjectIdentity = ObjectIdentity
capture = _Capture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8)
)
_BufferControlTable_Object = MibTable
bufferControlTable = _BufferControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 1)
)
if mibBuilder.loadTexts:
    bufferControlTable.setStatus("current")
_BufferControlEntry_Object = MibTableRow
bufferControlEntry = _BufferControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 1, 1)
)
bufferControlEntry.setIndexNames(
    (0, "ZHONE-RMON-MIB", "bufferControlIndex"),
)
if mibBuilder.loadTexts:
    bufferControlEntry.setStatus("current")


class _BufferControlIndex_Type(Integer32):
    """Custom type bufferControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BufferControlIndex_Type.__name__ = "Integer32"
_BufferControlIndex_Object = MibTableColumn
bufferControlIndex = _BufferControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 1, 1, 1),
    _BufferControlIndex_Type()
)
bufferControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferControlIndex.setStatus("current")


class _BufferControlChannelIndex_Type(Integer32):
    """Custom type bufferControlChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BufferControlChannelIndex_Type.__name__ = "Integer32"
_BufferControlChannelIndex_Object = MibTableColumn
bufferControlChannelIndex = _BufferControlChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 1, 1, 2),
    _BufferControlChannelIndex_Type()
)
bufferControlChannelIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bufferControlChannelIndex.setStatus("current")


class _BufferControlFullStatus_Type(Integer32):
    """Custom type bufferControlFullStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("spaceAvailable", 1))
    )


_BufferControlFullStatus_Type.__name__ = "Integer32"
_BufferControlFullStatus_Object = MibTableColumn
bufferControlFullStatus = _BufferControlFullStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 1, 1, 3),
    _BufferControlFullStatus_Type()
)
bufferControlFullStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferControlFullStatus.setStatus("current")


class _BufferControlFullAction_Type(Integer32):
    """Custom type bufferControlFullAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lockWhenFull", 1),
          ("wrapWhenFull", 2))
    )


_BufferControlFullAction_Type.__name__ = "Integer32"
_BufferControlFullAction_Object = MibTableColumn
bufferControlFullAction = _BufferControlFullAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 1, 1, 4),
    _BufferControlFullAction_Type()
)
bufferControlFullAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bufferControlFullAction.setStatus("current")


class _BufferControlCaptureSliceSize_Type(Integer32):
    """Custom type bufferControlCaptureSliceSize based on Integer32"""
    defaultValue = 100


_BufferControlCaptureSliceSize_Object = MibTableColumn
bufferControlCaptureSliceSize = _BufferControlCaptureSliceSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 1, 1, 5),
    _BufferControlCaptureSliceSize_Type()
)
bufferControlCaptureSliceSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bufferControlCaptureSliceSize.setStatus("current")
if mibBuilder.loadTexts:
    bufferControlCaptureSliceSize.setUnits("Octets")


class _BufferControlDownloadSliceSize_Type(Integer32):
    """Custom type bufferControlDownloadSliceSize based on Integer32"""
    defaultValue = 100


_BufferControlDownloadSliceSize_Object = MibTableColumn
bufferControlDownloadSliceSize = _BufferControlDownloadSliceSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 1, 1, 6),
    _BufferControlDownloadSliceSize_Type()
)
bufferControlDownloadSliceSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bufferControlDownloadSliceSize.setStatus("current")
if mibBuilder.loadTexts:
    bufferControlDownloadSliceSize.setUnits("Octets")


class _BufferControlDownloadOffset_Type(Integer32):
    """Custom type bufferControlDownloadOffset based on Integer32"""
    defaultValue = 0


_BufferControlDownloadOffset_Object = MibTableColumn
bufferControlDownloadOffset = _BufferControlDownloadOffset_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 1, 1, 7),
    _BufferControlDownloadOffset_Type()
)
bufferControlDownloadOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bufferControlDownloadOffset.setStatus("current")
if mibBuilder.loadTexts:
    bufferControlDownloadOffset.setUnits("Octets")


class _BufferControlMaxOctetsRequested_Type(Integer32):
    """Custom type bufferControlMaxOctetsRequested based on Integer32"""
    defaultValue = -1


_BufferControlMaxOctetsRequested_Object = MibTableColumn
bufferControlMaxOctetsRequested = _BufferControlMaxOctetsRequested_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 1, 1, 8),
    _BufferControlMaxOctetsRequested_Type()
)
bufferControlMaxOctetsRequested.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bufferControlMaxOctetsRequested.setStatus("current")
if mibBuilder.loadTexts:
    bufferControlMaxOctetsRequested.setUnits("Octets")
_BufferControlMaxOctetsGranted_Type = Integer32
_BufferControlMaxOctetsGranted_Object = MibTableColumn
bufferControlMaxOctetsGranted = _BufferControlMaxOctetsGranted_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 1, 1, 9),
    _BufferControlMaxOctetsGranted_Type()
)
bufferControlMaxOctetsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferControlMaxOctetsGranted.setStatus("current")
if mibBuilder.loadTexts:
    bufferControlMaxOctetsGranted.setUnits("Octets")
_BufferControlCapturedPackets_Type = Integer32
_BufferControlCapturedPackets_Object = MibTableColumn
bufferControlCapturedPackets = _BufferControlCapturedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 1, 1, 10),
    _BufferControlCapturedPackets_Type()
)
bufferControlCapturedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferControlCapturedPackets.setStatus("current")
if mibBuilder.loadTexts:
    bufferControlCapturedPackets.setUnits("Packets")
_BufferControlTurnOnTime_Type = TimeTicks
_BufferControlTurnOnTime_Object = MibTableColumn
bufferControlTurnOnTime = _BufferControlTurnOnTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 1, 1, 11),
    _BufferControlTurnOnTime_Type()
)
bufferControlTurnOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferControlTurnOnTime.setStatus("current")
_BufferControlOwner_Type = OwnerString
_BufferControlOwner_Object = MibTableColumn
bufferControlOwner = _BufferControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 1, 1, 12),
    _BufferControlOwner_Type()
)
bufferControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bufferControlOwner.setStatus("current")
_BufferControlStatus_Type = EntryStatus
_BufferControlStatus_Object = MibTableColumn
bufferControlStatus = _BufferControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 1, 1, 13),
    _BufferControlStatus_Type()
)
bufferControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bufferControlStatus.setStatus("current")
_CaptureBufferTable_Object = MibTable
captureBufferTable = _CaptureBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 2)
)
if mibBuilder.loadTexts:
    captureBufferTable.setStatus("current")
_CaptureBufferEntry_Object = MibTableRow
captureBufferEntry = _CaptureBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 2, 1)
)
captureBufferEntry.setIndexNames(
    (0, "ZHONE-RMON-MIB", "captureBufferControlIndex"),
    (0, "ZHONE-RMON-MIB", "captureBufferIndex"),
)
if mibBuilder.loadTexts:
    captureBufferEntry.setStatus("current")


class _CaptureBufferControlIndex_Type(Integer32):
    """Custom type captureBufferControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CaptureBufferControlIndex_Type.__name__ = "Integer32"
_CaptureBufferControlIndex_Object = MibTableColumn
captureBufferControlIndex = _CaptureBufferControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 2, 1, 1),
    _CaptureBufferControlIndex_Type()
)
captureBufferControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureBufferControlIndex.setStatus("current")


class _CaptureBufferIndex_Type(Integer32):
    """Custom type captureBufferIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CaptureBufferIndex_Type.__name__ = "Integer32"
_CaptureBufferIndex_Object = MibTableColumn
captureBufferIndex = _CaptureBufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 2, 1, 2),
    _CaptureBufferIndex_Type()
)
captureBufferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureBufferIndex.setStatus("current")
_CaptureBufferPacketID_Type = Integer32
_CaptureBufferPacketID_Object = MibTableColumn
captureBufferPacketID = _CaptureBufferPacketID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 2, 1, 3),
    _CaptureBufferPacketID_Type()
)
captureBufferPacketID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureBufferPacketID.setStatus("current")
_CaptureBufferPacketData_Type = OctetString
_CaptureBufferPacketData_Object = MibTableColumn
captureBufferPacketData = _CaptureBufferPacketData_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 2, 1, 4),
    _CaptureBufferPacketData_Type()
)
captureBufferPacketData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureBufferPacketData.setStatus("current")
_CaptureBufferPacketLength_Type = Integer32
_CaptureBufferPacketLength_Object = MibTableColumn
captureBufferPacketLength = _CaptureBufferPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 2, 1, 5),
    _CaptureBufferPacketLength_Type()
)
captureBufferPacketLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureBufferPacketLength.setStatus("current")
if mibBuilder.loadTexts:
    captureBufferPacketLength.setUnits("Octets")
_CaptureBufferPacketTime_Type = Integer32
_CaptureBufferPacketTime_Object = MibTableColumn
captureBufferPacketTime = _CaptureBufferPacketTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 2, 1, 6),
    _CaptureBufferPacketTime_Type()
)
captureBufferPacketTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureBufferPacketTime.setStatus("current")
if mibBuilder.loadTexts:
    captureBufferPacketTime.setUnits("Milliseconds")
_CaptureBufferPacketStatus_Type = Integer32
_CaptureBufferPacketStatus_Object = MibTableColumn
captureBufferPacketStatus = _CaptureBufferPacketStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 8, 2, 1, 7),
    _CaptureBufferPacketStatus_Type()
)
captureBufferPacketStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureBufferPacketStatus.setStatus("current")
_Event_ObjectIdentity = ObjectIdentity
event = _Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 9)
)
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 9, 1)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("current")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 9, 1, 1)
)
eventEntry.setIndexNames(
    (0, "ZHONE-RMON-MIB", "eventIndex"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("current")


class _EventIndex_Type(Integer32):
    """Custom type eventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EventIndex_Type.__name__ = "Integer32"
_EventIndex_Object = MibTableColumn
eventIndex = _EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 9, 1, 1, 1),
    _EventIndex_Type()
)
eventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventIndex.setStatus("current")


class _EventDescription_Type(DisplayString):
    """Custom type eventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EventDescription_Type.__name__ = "DisplayString"
_EventDescription_Object = MibTableColumn
eventDescription = _EventDescription_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 9, 1, 1, 2),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eventDescription.setStatus("current")


class _EventType_Type(Integer32):
    """Custom type eventType based on Integer32"""
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
        *(("log", 2),
          ("logandtrap", 4),
          ("none", 1),
          ("snmptrap", 3))
    )


_EventType_Type.__name__ = "Integer32"
_EventType_Object = MibTableColumn
eventType = _EventType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 9, 1, 1, 3),
    _EventType_Type()
)
eventType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eventType.setStatus("current")


class _EventCommunity_Type(OctetString):
    """Custom type eventCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EventCommunity_Type.__name__ = "OctetString"
_EventCommunity_Object = MibTableColumn
eventCommunity = _EventCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 9, 1, 1, 4),
    _EventCommunity_Type()
)
eventCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eventCommunity.setStatus("current")
_EventLastTimeSent_Type = TimeTicks
_EventLastTimeSent_Object = MibTableColumn
eventLastTimeSent = _EventLastTimeSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 9, 1, 1, 5),
    _EventLastTimeSent_Type()
)
eventLastTimeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLastTimeSent.setStatus("current")
_EventOwner_Type = OwnerString
_EventOwner_Object = MibTableColumn
eventOwner = _EventOwner_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 9, 1, 1, 6),
    _EventOwner_Type()
)
eventOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eventOwner.setStatus("current")
_EventStatus_Type = EntryStatus
_EventStatus_Object = MibTableColumn
eventStatus = _EventStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 9, 1, 1, 7),
    _EventStatus_Type()
)
eventStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eventStatus.setStatus("current")
_LogTable_Object = MibTable
logTable = _LogTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 9, 2)
)
if mibBuilder.loadTexts:
    logTable.setStatus("current")
_LogEntry_Object = MibTableRow
logEntry = _LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 9, 2, 1)
)
logEntry.setIndexNames(
    (0, "ZHONE-RMON-MIB", "logEventIndex"),
    (0, "ZHONE-RMON-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    logEntry.setStatus("current")


class _LogEventIndex_Type(Integer32):
    """Custom type logEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LogEventIndex_Type.__name__ = "Integer32"
_LogEventIndex_Object = MibTableColumn
logEventIndex = _LogEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 9, 2, 1, 1),
    _LogEventIndex_Type()
)
logEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEventIndex.setStatus("current")


class _LogIndex_Type(Integer32):
    """Custom type logIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LogIndex_Type.__name__ = "Integer32"
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 9, 2, 1, 2),
    _LogIndex_Type()
)
logIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logIndex.setStatus("current")
_LogTime_Type = TimeTicks
_LogTime_Object = MibTableColumn
logTime = _LogTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 9, 2, 1, 3),
    _LogTime_Type()
)
logTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTime.setStatus("current")


class _LogDescription_Type(DisplayString):
    """Custom type logDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LogDescription_Type.__name__ = "DisplayString"
_LogDescription_Object = MibTableColumn
logDescription = _LogDescription_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 9, 2, 1, 4),
    _LogDescription_Type()
)
logDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logDescription.setStatus("current")
_RmonEventsV2_ObjectIdentity = ObjectIdentity
rmonEventsV2 = _RmonEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 10)
)
_RmonEvents_ObjectIdentity = ObjectIdentity
rmonEvents = _RmonEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 10, 0)
)
if mibBuilder.loadTexts:
    rmonEvents.setStatus("current")
_RmonConformance_ObjectIdentity = ObjectIdentity
rmonConformance = _RmonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 20)
)
_RmonCompliances_ObjectIdentity = ObjectIdentity
rmonCompliances = _RmonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 20, 1)
)
_RmonGroups_ObjectIdentity = ObjectIdentity
rmonGroups = _RmonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 20, 2)
)

# Managed Objects groups

zhoneRmonEtherStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 20, 2, 1)
)
zhoneRmonEtherStatsGroup.setObjects(
      *(("ZHONE-RMON-MIB", "zhoneEtherStatsDropEvents"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsOctets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsBroadcastPkts"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsMulticastPkts"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsCRCAlignErrors"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsUndersizePkts"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsOversizePkts"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsFragments"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsJabbers"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsCollisions"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsPkts64Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsPkts65to127Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsPkts128to255Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsPkts256to511Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsPkts512to1023Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsReceivedPkts64Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsReceivedPkts65to127Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsReceivedPkts128to255Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsReceivedPkts256to511Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsReceivedPkts512to1023Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsReceivedPkts1024to1518Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsReceivedPkts1519to2047Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsReceivedPkts2048to4095Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsReceivedPkts4095to9216Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsTransmittedPkts64Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsTransmittedPkts65to127Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsTransmittedPkts128to255Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsTransmittedPkts256to511Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsTransmittedPkts512to1023Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsTransmittedPkts1024to1518Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsTransmittedPkts1519to2047Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsTransmittedPkts2048to4095Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsTransmittedPkts4095to9216Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsDroppedFrames"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsPkts1024to1518Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsTXNoErrors"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsRXNoErrors"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsPkts2048to4095Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsPkts4095to9216Octets"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsTxPkts"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsRxPkts"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsAverageTxThroughput"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsAverageRxThroughput"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsTxBandwidthOccupancy"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsMcastRxBytes"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsMcastTxBytes"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsRxBandwidthOccupancy"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsPkts"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsOversizeTxPkts"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsOversizeRxPkts"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsIPMCRoutedPkts"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsIPMCTxDroppedPkts"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsIPMCRxDroppedPkts"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsIPMCBridgedPkts"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsMcastRxDroppedBytes"),
        ("ZHONE-RMON-MIB", "zhoneEtherStatsPkts1519to2047Octets"))
)
if mibBuilder.loadTexts:
    zhoneRmonEtherStatsGroup.setStatus("current")

rmonHistoryControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 20, 2, 2)
)
rmonHistoryControlGroup.setObjects(
      *(("ZHONE-RMON-MIB", "historyControlIndex"),
        ("ZHONE-RMON-MIB", "historyControlDataSource"),
        ("ZHONE-RMON-MIB", "historyControlBucketsRequested"),
        ("ZHONE-RMON-MIB", "historyControlBucketsGranted"),
        ("ZHONE-RMON-MIB", "historyControlInterval"),
        ("ZHONE-RMON-MIB", "historyControlOwner"),
        ("ZHONE-RMON-MIB", "historyControlStatus"))
)
if mibBuilder.loadTexts:
    rmonHistoryControlGroup.setStatus("current")

rmonEthernetHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 20, 2, 3)
)
rmonEthernetHistoryGroup.setObjects(
      *(("ZHONE-RMON-MIB", "etherHistoryIndex"),
        ("ZHONE-RMON-MIB", "etherHistorySampleIndex"),
        ("ZHONE-RMON-MIB", "etherHistoryIntervalStart"),
        ("ZHONE-RMON-MIB", "etherHistoryDropEvents"),
        ("ZHONE-RMON-MIB", "etherHistoryOctets"),
        ("ZHONE-RMON-MIB", "etherHistoryPkts"),
        ("ZHONE-RMON-MIB", "etherHistoryBroadcastPkts"),
        ("ZHONE-RMON-MIB", "etherHistoryMulticastPkts"),
        ("ZHONE-RMON-MIB", "etherHistoryCRCAlignErrors"),
        ("ZHONE-RMON-MIB", "etherHistoryUndersizePkts"),
        ("ZHONE-RMON-MIB", "etherHistoryOversizePkts"),
        ("ZHONE-RMON-MIB", "etherHistoryFragments"),
        ("ZHONE-RMON-MIB", "etherHistoryJabbers"),
        ("ZHONE-RMON-MIB", "etherHistoryCollisions"),
        ("ZHONE-RMON-MIB", "etherHistoryUtilization"))
)
if mibBuilder.loadTexts:
    rmonEthernetHistoryGroup.setStatus("current")

rmonAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 20, 2, 4)
)
rmonAlarmGroup.setObjects(
      *(("ZHONE-RMON-MIB", "alarmIndex"),
        ("ZHONE-RMON-MIB", "alarmInterval"),
        ("ZHONE-RMON-MIB", "alarmVariable"),
        ("ZHONE-RMON-MIB", "alarmSampleType"),
        ("ZHONE-RMON-MIB", "alarmValue"),
        ("ZHONE-RMON-MIB", "alarmStartupAlarm"),
        ("ZHONE-RMON-MIB", "alarmRisingThreshold"),
        ("ZHONE-RMON-MIB", "alarmFallingThreshold"),
        ("ZHONE-RMON-MIB", "alarmRisingEventIndex"),
        ("ZHONE-RMON-MIB", "alarmFallingEventIndex"),
        ("ZHONE-RMON-MIB", "alarmOwner"),
        ("ZHONE-RMON-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    rmonAlarmGroup.setStatus("current")

rmonHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 20, 2, 5)
)
rmonHostGroup.setObjects(
      *(("ZHONE-RMON-MIB", "hostControlIndex"),
        ("ZHONE-RMON-MIB", "hostControlDataSource"),
        ("ZHONE-RMON-MIB", "hostControlTableSize"),
        ("ZHONE-RMON-MIB", "hostControlLastDeleteTime"),
        ("ZHONE-RMON-MIB", "hostControlOwner"),
        ("ZHONE-RMON-MIB", "hostControlStatus"),
        ("ZHONE-RMON-MIB", "hostAddress"),
        ("ZHONE-RMON-MIB", "hostCreationOrder"),
        ("ZHONE-RMON-MIB", "hostIndex"),
        ("ZHONE-RMON-MIB", "hostInPkts"),
        ("ZHONE-RMON-MIB", "hostOutPkts"),
        ("ZHONE-RMON-MIB", "hostInOctets"),
        ("ZHONE-RMON-MIB", "hostOutOctets"),
        ("ZHONE-RMON-MIB", "hostOutErrors"),
        ("ZHONE-RMON-MIB", "hostOutBroadcastPkts"),
        ("ZHONE-RMON-MIB", "hostOutMulticastPkts"),
        ("ZHONE-RMON-MIB", "hostTimeAddress"),
        ("ZHONE-RMON-MIB", "hostTimeCreationOrder"),
        ("ZHONE-RMON-MIB", "hostTimeIndex"),
        ("ZHONE-RMON-MIB", "hostTimeInPkts"),
        ("ZHONE-RMON-MIB", "hostTimeOutPkts"),
        ("ZHONE-RMON-MIB", "hostTimeInOctets"),
        ("ZHONE-RMON-MIB", "hostTimeOutOctets"),
        ("ZHONE-RMON-MIB", "hostTimeOutErrors"),
        ("ZHONE-RMON-MIB", "hostTimeOutBroadcastPkts"),
        ("ZHONE-RMON-MIB", "hostTimeOutMulticastPkts"))
)
if mibBuilder.loadTexts:
    rmonHostGroup.setStatus("current")

rmonHostTopNGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 20, 2, 6)
)
rmonHostTopNGroup.setObjects(
      *(("ZHONE-RMON-MIB", "hostTopNControlIndex"),
        ("ZHONE-RMON-MIB", "hostTopNHostIndex"),
        ("ZHONE-RMON-MIB", "hostTopNRateBase"),
        ("ZHONE-RMON-MIB", "hostTopNTimeRemaining"),
        ("ZHONE-RMON-MIB", "hostTopNDuration"),
        ("ZHONE-RMON-MIB", "hostTopNRequestedSize"),
        ("ZHONE-RMON-MIB", "hostTopNGrantedSize"),
        ("ZHONE-RMON-MIB", "hostTopNStartTime"),
        ("ZHONE-RMON-MIB", "hostTopNOwner"),
        ("ZHONE-RMON-MIB", "hostTopNStatus"),
        ("ZHONE-RMON-MIB", "hostTopNReport"),
        ("ZHONE-RMON-MIB", "hostTopNIndex"),
        ("ZHONE-RMON-MIB", "hostTopNAddress"),
        ("ZHONE-RMON-MIB", "hostTopNRate"))
)
if mibBuilder.loadTexts:
    rmonHostTopNGroup.setStatus("current")

rmonMatrixGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 20, 2, 7)
)
rmonMatrixGroup.setObjects(
      *(("ZHONE-RMON-MIB", "matrixControlIndex"),
        ("ZHONE-RMON-MIB", "matrixControlDataSource"),
        ("ZHONE-RMON-MIB", "matrixControlTableSize"),
        ("ZHONE-RMON-MIB", "matrixControlLastDeleteTime"),
        ("ZHONE-RMON-MIB", "matrixControlOwner"),
        ("ZHONE-RMON-MIB", "matrixControlStatus"),
        ("ZHONE-RMON-MIB", "matrixSDSourceAddress"),
        ("ZHONE-RMON-MIB", "matrixSDDestAddress"),
        ("ZHONE-RMON-MIB", "matrixSDIndex"),
        ("ZHONE-RMON-MIB", "matrixSDPkts"),
        ("ZHONE-RMON-MIB", "matrixSDOctets"),
        ("ZHONE-RMON-MIB", "matrixSDErrors"),
        ("ZHONE-RMON-MIB", "matrixDSSourceAddress"),
        ("ZHONE-RMON-MIB", "matrixDSDestAddress"),
        ("ZHONE-RMON-MIB", "matrixDSIndex"),
        ("ZHONE-RMON-MIB", "matrixDSPkts"),
        ("ZHONE-RMON-MIB", "matrixDSOctets"),
        ("ZHONE-RMON-MIB", "matrixDSErrors"))
)
if mibBuilder.loadTexts:
    rmonMatrixGroup.setStatus("current")

rmonFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 20, 2, 8)
)
rmonFilterGroup.setObjects(
      *(("ZHONE-RMON-MIB", "filterIndex"),
        ("ZHONE-RMON-MIB", "filterChannelIndex"),
        ("ZHONE-RMON-MIB", "filterPktDataOffset"),
        ("ZHONE-RMON-MIB", "filterPktData"),
        ("ZHONE-RMON-MIB", "filterPktDataMask"),
        ("ZHONE-RMON-MIB", "filterPktDataNotMask"),
        ("ZHONE-RMON-MIB", "filterPktStatus"),
        ("ZHONE-RMON-MIB", "filterPktStatusMask"),
        ("ZHONE-RMON-MIB", "filterPktStatusNotMask"),
        ("ZHONE-RMON-MIB", "filterOwner"),
        ("ZHONE-RMON-MIB", "filterStatus"),
        ("ZHONE-RMON-MIB", "channelIndex"),
        ("ZHONE-RMON-MIB", "channelIfIndex"),
        ("ZHONE-RMON-MIB", "channelAcceptType"),
        ("ZHONE-RMON-MIB", "channelDataControl"),
        ("ZHONE-RMON-MIB", "channelTurnOnEventIndex"),
        ("ZHONE-RMON-MIB", "channelTurnOffEventIndex"),
        ("ZHONE-RMON-MIB", "channelEventIndex"),
        ("ZHONE-RMON-MIB", "channelEventStatus"),
        ("ZHONE-RMON-MIB", "channelMatches"),
        ("ZHONE-RMON-MIB", "channelDescription"),
        ("ZHONE-RMON-MIB", "channelOwner"),
        ("ZHONE-RMON-MIB", "channelStatus"))
)
if mibBuilder.loadTexts:
    rmonFilterGroup.setStatus("current")

rmonPacketCaptureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 20, 2, 9)
)
rmonPacketCaptureGroup.setObjects(
      *(("ZHONE-RMON-MIB", "bufferControlIndex"),
        ("ZHONE-RMON-MIB", "bufferControlChannelIndex"),
        ("ZHONE-RMON-MIB", "bufferControlFullStatus"),
        ("ZHONE-RMON-MIB", "bufferControlFullAction"),
        ("ZHONE-RMON-MIB", "bufferControlCaptureSliceSize"),
        ("ZHONE-RMON-MIB", "bufferControlDownloadSliceSize"),
        ("ZHONE-RMON-MIB", "bufferControlDownloadOffset"),
        ("ZHONE-RMON-MIB", "bufferControlMaxOctetsRequested"),
        ("ZHONE-RMON-MIB", "bufferControlMaxOctetsGranted"),
        ("ZHONE-RMON-MIB", "bufferControlCapturedPackets"),
        ("ZHONE-RMON-MIB", "bufferControlTurnOnTime"),
        ("ZHONE-RMON-MIB", "bufferControlOwner"),
        ("ZHONE-RMON-MIB", "bufferControlStatus"),
        ("ZHONE-RMON-MIB", "captureBufferControlIndex"),
        ("ZHONE-RMON-MIB", "captureBufferIndex"),
        ("ZHONE-RMON-MIB", "captureBufferPacketID"),
        ("ZHONE-RMON-MIB", "captureBufferPacketData"),
        ("ZHONE-RMON-MIB", "captureBufferPacketLength"),
        ("ZHONE-RMON-MIB", "captureBufferPacketTime"),
        ("ZHONE-RMON-MIB", "captureBufferPacketStatus"))
)
if mibBuilder.loadTexts:
    rmonPacketCaptureGroup.setStatus("current")

rmonEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 20, 2, 10)
)
rmonEventGroup.setObjects(
      *(("ZHONE-RMON-MIB", "eventIndex"),
        ("ZHONE-RMON-MIB", "eventDescription"),
        ("ZHONE-RMON-MIB", "eventType"),
        ("ZHONE-RMON-MIB", "eventCommunity"),
        ("ZHONE-RMON-MIB", "eventLastTimeSent"),
        ("ZHONE-RMON-MIB", "eventOwner"),
        ("ZHONE-RMON-MIB", "eventStatus"),
        ("ZHONE-RMON-MIB", "logEventIndex"),
        ("ZHONE-RMON-MIB", "logIndex"),
        ("ZHONE-RMON-MIB", "logTime"),
        ("ZHONE-RMON-MIB", "logDescription"))
)
if mibBuilder.loadTexts:
    rmonEventGroup.setStatus("current")


# Notification objects

risingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 10, 0, 1)
)
risingAlarm.setObjects(
      *(("ZHONE-RMON-MIB", "alarmIndex"),
        ("ZHONE-RMON-MIB", "alarmVariable"),
        ("ZHONE-RMON-MIB", "alarmSampleType"),
        ("ZHONE-RMON-MIB", "alarmValue"),
        ("ZHONE-RMON-MIB", "alarmRisingThreshold"))
)
if mibBuilder.loadTexts:
    risingAlarm.setStatus(
        "current"
    )

fallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 10, 0, 2)
)
fallingAlarm.setObjects(
      *(("ZHONE-RMON-MIB", "alarmIndex"),
        ("ZHONE-RMON-MIB", "alarmVariable"),
        ("ZHONE-RMON-MIB", "alarmSampleType"),
        ("ZHONE-RMON-MIB", "alarmValue"),
        ("ZHONE-RMON-MIB", "alarmFallingThreshold"))
)
if mibBuilder.loadTexts:
    fallingAlarm.setStatus(
        "current"
    )


# Notifications groups

rmonNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 20, 2, 11)
)
rmonNotificationGroup.setObjects(
      *(("ZHONE-RMON-MIB", "risingAlarm"),
        ("ZHONE-RMON-MIB", "fallingAlarm"))
)
if mibBuilder.loadTexts:
    rmonNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rmonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 12, 1, 20, 1, 1)
)
if mibBuilder.loadTexts:
    rmonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-RMON-MIB",
    **{"OwnerString": OwnerString,
       "EntryStatus": EntryStatus,
       "zhoneRmonMibModule": zhoneRmonMibModule,
       "zhoneRmon": zhoneRmon,
       "statistics": statistics,
       "zhoneEtherStatsTable": zhoneEtherStatsTable,
       "zhoneEtherStatsEntry": zhoneEtherStatsEntry,
       "zhoneEtherStatsDropEvents": zhoneEtherStatsDropEvents,
       "zhoneEtherStatsDroppedFrames": zhoneEtherStatsDroppedFrames,
       "zhoneEtherStatsOctets": zhoneEtherStatsOctets,
       "zhoneEtherStatsPkts": zhoneEtherStatsPkts,
       "zhoneEtherStatsTxPkts": zhoneEtherStatsTxPkts,
       "zhoneEtherStatsRxPkts": zhoneEtherStatsRxPkts,
       "zhoneEtherStatsMcastTxBytes": zhoneEtherStatsMcastTxBytes,
       "zhoneEtherStatsMcastRxBytes": zhoneEtherStatsMcastRxBytes,
       "zhoneEtherStatsMcastRxDroppedBytes": zhoneEtherStatsMcastRxDroppedBytes,
       "zhoneEtherStatsAverageTxThroughput": zhoneEtherStatsAverageTxThroughput,
       "zhoneEtherStatsAverageRxThroughput": zhoneEtherStatsAverageRxThroughput,
       "zhoneEtherStatsTxBandwidthOccupancy": zhoneEtherStatsTxBandwidthOccupancy,
       "zhoneEtherStatsRxBandwidthOccupancy": zhoneEtherStatsRxBandwidthOccupancy,
       "zhoneEtherStatsBroadcastPkts": zhoneEtherStatsBroadcastPkts,
       "zhoneEtherStatsMulticastPkts": zhoneEtherStatsMulticastPkts,
       "zhoneEtherStatsCRCAlignErrors": zhoneEtherStatsCRCAlignErrors,
       "zhoneEtherStatsUndersizePkts": zhoneEtherStatsUndersizePkts,
       "zhoneEtherStatsOversizePkts": zhoneEtherStatsOversizePkts,
       "zhoneEtherStatsOversizeTxPkts": zhoneEtherStatsOversizeTxPkts,
       "zhoneEtherStatsOversizeRxPkts": zhoneEtherStatsOversizeRxPkts,
       "zhoneEtherStatsFragments": zhoneEtherStatsFragments,
       "zhoneEtherStatsJabbers": zhoneEtherStatsJabbers,
       "zhoneEtherStatsCollisions": zhoneEtherStatsCollisions,
       "zhoneEtherStatsTXNoErrors": zhoneEtherStatsTXNoErrors,
       "zhoneEtherStatsRXNoErrors": zhoneEtherStatsRXNoErrors,
       "zhoneEtherStatsIPMCBridgedPkts": zhoneEtherStatsIPMCBridgedPkts,
       "zhoneEtherStatsIPMCRoutedPkts": zhoneEtherStatsIPMCRoutedPkts,
       "zhoneEtherStatsIPMCTxDroppedPkts": zhoneEtherStatsIPMCTxDroppedPkts,
       "zhoneEtherStatsIPMCRxDroppedPkts": zhoneEtherStatsIPMCRxDroppedPkts,
       "zhoneEtherStatsPkts64Octets": zhoneEtherStatsPkts64Octets,
       "zhoneEtherStatsPkts65to127Octets": zhoneEtherStatsPkts65to127Octets,
       "zhoneEtherStatsPkts128to255Octets": zhoneEtherStatsPkts128to255Octets,
       "zhoneEtherStatsPkts256to511Octets": zhoneEtherStatsPkts256to511Octets,
       "zhoneEtherStatsPkts512to1023Octets": zhoneEtherStatsPkts512to1023Octets,
       "zhoneEtherStatsPkts1024to1518Octets": zhoneEtherStatsPkts1024to1518Octets,
       "zhoneEtherStatsPkts1519to2047Octets": zhoneEtherStatsPkts1519to2047Octets,
       "zhoneEtherStatsPkts2048to4095Octets": zhoneEtherStatsPkts2048to4095Octets,
       "zhoneEtherStatsPkts4095to9216Octets": zhoneEtherStatsPkts4095to9216Octets,
       "zhoneEtherStatsReceivedPkts64Octets": zhoneEtherStatsReceivedPkts64Octets,
       "zhoneEtherStatsReceivedPkts65to127Octets": zhoneEtherStatsReceivedPkts65to127Octets,
       "zhoneEtherStatsReceivedPkts128to255Octets": zhoneEtherStatsReceivedPkts128to255Octets,
       "zhoneEtherStatsReceivedPkts256to511Octets": zhoneEtherStatsReceivedPkts256to511Octets,
       "zhoneEtherStatsReceivedPkts512to1023Octets": zhoneEtherStatsReceivedPkts512to1023Octets,
       "zhoneEtherStatsReceivedPkts1024to1518Octets": zhoneEtherStatsReceivedPkts1024to1518Octets,
       "zhoneEtherStatsReceivedPkts1519to2047Octets": zhoneEtherStatsReceivedPkts1519to2047Octets,
       "zhoneEtherStatsReceivedPkts2048to4095Octets": zhoneEtherStatsReceivedPkts2048to4095Octets,
       "zhoneEtherStatsReceivedPkts4095to9216Octets": zhoneEtherStatsReceivedPkts4095to9216Octets,
       "zhoneEtherStatsTransmittedPkts64Octets": zhoneEtherStatsTransmittedPkts64Octets,
       "zhoneEtherStatsTransmittedPkts65to127Octets": zhoneEtherStatsTransmittedPkts65to127Octets,
       "zhoneEtherStatsTransmittedPkts128to255Octets": zhoneEtherStatsTransmittedPkts128to255Octets,
       "zhoneEtherStatsTransmittedPkts256to511Octets": zhoneEtherStatsTransmittedPkts256to511Octets,
       "zhoneEtherStatsTransmittedPkts512to1023Octets": zhoneEtherStatsTransmittedPkts512to1023Octets,
       "zhoneEtherStatsTransmittedPkts1024to1518Octets": zhoneEtherStatsTransmittedPkts1024to1518Octets,
       "zhoneEtherStatsTransmittedPkts1519to2047Octets": zhoneEtherStatsTransmittedPkts1519to2047Octets,
       "zhoneEtherStatsTransmittedPkts2048to4095Octets": zhoneEtherStatsTransmittedPkts2048to4095Octets,
       "zhoneEtherStatsTransmittedPkts4095to9216Octets": zhoneEtherStatsTransmittedPkts4095to9216Octets,
       "history": history,
       "historyControlTable": historyControlTable,
       "historyControlEntry": historyControlEntry,
       "historyControlIndex": historyControlIndex,
       "historyControlDataSource": historyControlDataSource,
       "historyControlBucketsRequested": historyControlBucketsRequested,
       "historyControlBucketsGranted": historyControlBucketsGranted,
       "historyControlInterval": historyControlInterval,
       "historyControlOwner": historyControlOwner,
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
       "alarm": alarm,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmIndex": alarmIndex,
       "alarmInterval": alarmInterval,
       "alarmVariable": alarmVariable,
       "alarmSampleType": alarmSampleType,
       "alarmValue": alarmValue,
       "alarmStartupAlarm": alarmStartupAlarm,
       "alarmRisingThreshold": alarmRisingThreshold,
       "alarmFallingThreshold": alarmFallingThreshold,
       "alarmRisingEventIndex": alarmRisingEventIndex,
       "alarmFallingEventIndex": alarmFallingEventIndex,
       "alarmOwner": alarmOwner,
       "alarmStatus": alarmStatus,
       "hosts": hosts,
       "hostControlTable": hostControlTable,
       "hostControlEntry": hostControlEntry,
       "hostControlIndex": hostControlIndex,
       "hostControlDataSource": hostControlDataSource,
       "hostControlTableSize": hostControlTableSize,
       "hostControlLastDeleteTime": hostControlLastDeleteTime,
       "hostControlOwner": hostControlOwner,
       "hostControlStatus": hostControlStatus,
       "hostTable": hostTable,
       "hostEntry": hostEntry,
       "hostAddress": hostAddress,
       "hostCreationOrder": hostCreationOrder,
       "hostIndex": hostIndex,
       "hostInPkts": hostInPkts,
       "hostOutPkts": hostOutPkts,
       "hostInOctets": hostInOctets,
       "hostOutOctets": hostOutOctets,
       "hostOutErrors": hostOutErrors,
       "hostOutBroadcastPkts": hostOutBroadcastPkts,
       "hostOutMulticastPkts": hostOutMulticastPkts,
       "hostTimeTable": hostTimeTable,
       "hostTimeEntry": hostTimeEntry,
       "hostTimeAddress": hostTimeAddress,
       "hostTimeCreationOrder": hostTimeCreationOrder,
       "hostTimeIndex": hostTimeIndex,
       "hostTimeInPkts": hostTimeInPkts,
       "hostTimeOutPkts": hostTimeOutPkts,
       "hostTimeInOctets": hostTimeInOctets,
       "hostTimeOutOctets": hostTimeOutOctets,
       "hostTimeOutErrors": hostTimeOutErrors,
       "hostTimeOutBroadcastPkts": hostTimeOutBroadcastPkts,
       "hostTimeOutMulticastPkts": hostTimeOutMulticastPkts,
       "hostTopN": hostTopN,
       "hostTopNControlTable": hostTopNControlTable,
       "hostTopNControlEntry": hostTopNControlEntry,
       "hostTopNControlIndex": hostTopNControlIndex,
       "hostTopNHostIndex": hostTopNHostIndex,
       "hostTopNRateBase": hostTopNRateBase,
       "hostTopNTimeRemaining": hostTopNTimeRemaining,
       "hostTopNDuration": hostTopNDuration,
       "hostTopNRequestedSize": hostTopNRequestedSize,
       "hostTopNGrantedSize": hostTopNGrantedSize,
       "hostTopNStartTime": hostTopNStartTime,
       "hostTopNOwner": hostTopNOwner,
       "hostTopNStatus": hostTopNStatus,
       "hostTopNTable": hostTopNTable,
       "hostTopNEntry": hostTopNEntry,
       "hostTopNReport": hostTopNReport,
       "hostTopNIndex": hostTopNIndex,
       "hostTopNAddress": hostTopNAddress,
       "hostTopNRate": hostTopNRate,
       "matrix": matrix,
       "matrixControlTable": matrixControlTable,
       "matrixControlEntry": matrixControlEntry,
       "matrixControlIndex": matrixControlIndex,
       "matrixControlDataSource": matrixControlDataSource,
       "matrixControlTableSize": matrixControlTableSize,
       "matrixControlLastDeleteTime": matrixControlLastDeleteTime,
       "matrixControlOwner": matrixControlOwner,
       "matrixControlStatus": matrixControlStatus,
       "matrixSDTable": matrixSDTable,
       "matrixSDEntry": matrixSDEntry,
       "matrixSDSourceAddress": matrixSDSourceAddress,
       "matrixSDDestAddress": matrixSDDestAddress,
       "matrixSDIndex": matrixSDIndex,
       "matrixSDPkts": matrixSDPkts,
       "matrixSDOctets": matrixSDOctets,
       "matrixSDErrors": matrixSDErrors,
       "matrixDSTable": matrixDSTable,
       "matrixDSEntry": matrixDSEntry,
       "matrixDSSourceAddress": matrixDSSourceAddress,
       "matrixDSDestAddress": matrixDSDestAddress,
       "matrixDSIndex": matrixDSIndex,
       "matrixDSPkts": matrixDSPkts,
       "matrixDSOctets": matrixDSOctets,
       "matrixDSErrors": matrixDSErrors,
       "zhoneRmonFilter": zhoneRmonFilter,
       "filterTable": filterTable,
       "filterEntry": filterEntry,
       "filterIndex": filterIndex,
       "filterChannelIndex": filterChannelIndex,
       "filterPktDataOffset": filterPktDataOffset,
       "filterPktData": filterPktData,
       "filterPktDataMask": filterPktDataMask,
       "filterPktDataNotMask": filterPktDataNotMask,
       "filterPktStatus": filterPktStatus,
       "filterPktStatusMask": filterPktStatusMask,
       "filterPktStatusNotMask": filterPktStatusNotMask,
       "filterOwner": filterOwner,
       "filterStatus": filterStatus,
       "channelTable": channelTable,
       "channelEntry": channelEntry,
       "channelIndex": channelIndex,
       "channelIfIndex": channelIfIndex,
       "channelAcceptType": channelAcceptType,
       "channelDataControl": channelDataControl,
       "channelTurnOnEventIndex": channelTurnOnEventIndex,
       "channelTurnOffEventIndex": channelTurnOffEventIndex,
       "channelEventIndex": channelEventIndex,
       "channelEventStatus": channelEventStatus,
       "channelMatches": channelMatches,
       "channelDescription": channelDescription,
       "channelOwner": channelOwner,
       "channelStatus": channelStatus,
       "capture": capture,
       "bufferControlTable": bufferControlTable,
       "bufferControlEntry": bufferControlEntry,
       "bufferControlIndex": bufferControlIndex,
       "bufferControlChannelIndex": bufferControlChannelIndex,
       "bufferControlFullStatus": bufferControlFullStatus,
       "bufferControlFullAction": bufferControlFullAction,
       "bufferControlCaptureSliceSize": bufferControlCaptureSliceSize,
       "bufferControlDownloadSliceSize": bufferControlDownloadSliceSize,
       "bufferControlDownloadOffset": bufferControlDownloadOffset,
       "bufferControlMaxOctetsRequested": bufferControlMaxOctetsRequested,
       "bufferControlMaxOctetsGranted": bufferControlMaxOctetsGranted,
       "bufferControlCapturedPackets": bufferControlCapturedPackets,
       "bufferControlTurnOnTime": bufferControlTurnOnTime,
       "bufferControlOwner": bufferControlOwner,
       "bufferControlStatus": bufferControlStatus,
       "captureBufferTable": captureBufferTable,
       "captureBufferEntry": captureBufferEntry,
       "captureBufferControlIndex": captureBufferControlIndex,
       "captureBufferIndex": captureBufferIndex,
       "captureBufferPacketID": captureBufferPacketID,
       "captureBufferPacketData": captureBufferPacketData,
       "captureBufferPacketLength": captureBufferPacketLength,
       "captureBufferPacketTime": captureBufferPacketTime,
       "captureBufferPacketStatus": captureBufferPacketStatus,
       "event": event,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "eventIndex": eventIndex,
       "eventDescription": eventDescription,
       "eventType": eventType,
       "eventCommunity": eventCommunity,
       "eventLastTimeSent": eventLastTimeSent,
       "eventOwner": eventOwner,
       "eventStatus": eventStatus,
       "logTable": logTable,
       "logEntry": logEntry,
       "logEventIndex": logEventIndex,
       "logIndex": logIndex,
       "logTime": logTime,
       "logDescription": logDescription,
       "rmonEventsV2": rmonEventsV2,
       "rmonEvents": rmonEvents,
       "risingAlarm": risingAlarm,
       "fallingAlarm": fallingAlarm,
       "rmonConformance": rmonConformance,
       "rmonCompliances": rmonCompliances,
       "rmonCompliance": rmonCompliance,
       "rmonGroups": rmonGroups,
       "zhoneRmonEtherStatsGroup": zhoneRmonEtherStatsGroup,
       "rmonHistoryControlGroup": rmonHistoryControlGroup,
       "rmonEthernetHistoryGroup": rmonEthernetHistoryGroup,
       "rmonAlarmGroup": rmonAlarmGroup,
       "rmonHostGroup": rmonHostGroup,
       "rmonHostTopNGroup": rmonHostTopNGroup,
       "rmonMatrixGroup": rmonMatrixGroup,
       "rmonFilterGroup": rmonFilterGroup,
       "rmonPacketCaptureGroup": rmonPacketCaptureGroup,
       "rmonEventGroup": rmonEventGroup,
       "rmonNotificationGroup": rmonNotificationGroup}
)
