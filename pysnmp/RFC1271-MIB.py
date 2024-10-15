# SNMP MIB module (RFC1271-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1271-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:34 2024
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions



class OwnerString(DisplayString):
    """Custom type OwnerString based on DisplayString"""




class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rmon_ObjectIdentity = ObjectIdentity
rmon = _Rmon_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16)
)
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 1)
)
_EtherStatsTable_Object = MibTable
etherStatsTable = _EtherStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1)
)
if mibBuilder.loadTexts:
    etherStatsTable.setStatus("mandatory")
_EtherStatsEntry_Object = MibTableRow
etherStatsEntry = _EtherStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1)
)
etherStatsEntry.setIndexNames(
    (0, "RFC1271-MIB", "etherStatsIndex"),
)
if mibBuilder.loadTexts:
    etherStatsEntry.setStatus("mandatory")


class _EtherStatsIndex_Type(Integer32):
    """Custom type etherStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtherStatsIndex_Type.__name__ = "Integer32"
_EtherStatsIndex_Object = MibTableColumn
etherStatsIndex = _EtherStatsIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 1),
    _EtherStatsIndex_Type()
)
etherStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsIndex.setStatus("mandatory")
_EtherStatsDataSource_Type = ObjectIdentifier
_EtherStatsDataSource_Object = MibTableColumn
etherStatsDataSource = _EtherStatsDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 2),
    _EtherStatsDataSource_Type()
)
etherStatsDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherStatsDataSource.setStatus("mandatory")
_EtherStatsDropEvents_Type = Counter32
_EtherStatsDropEvents_Object = MibTableColumn
etherStatsDropEvents = _EtherStatsDropEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 3),
    _EtherStatsDropEvents_Type()
)
etherStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsDropEvents.setStatus("mandatory")
_EtherStatsOctets_Type = Counter32
_EtherStatsOctets_Object = MibTableColumn
etherStatsOctets = _EtherStatsOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 4),
    _EtherStatsOctets_Type()
)
etherStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsOctets.setStatus("mandatory")
_EtherStatsPkts_Type = Counter32
_EtherStatsPkts_Object = MibTableColumn
etherStatsPkts = _EtherStatsPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 5),
    _EtherStatsPkts_Type()
)
etherStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsPkts.setStatus("mandatory")
_EtherStatsBroadcastPkts_Type = Counter32
_EtherStatsBroadcastPkts_Object = MibTableColumn
etherStatsBroadcastPkts = _EtherStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 6),
    _EtherStatsBroadcastPkts_Type()
)
etherStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsBroadcastPkts.setStatus("mandatory")
_EtherStatsMulticastPkts_Type = Counter32
_EtherStatsMulticastPkts_Object = MibTableColumn
etherStatsMulticastPkts = _EtherStatsMulticastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 7),
    _EtherStatsMulticastPkts_Type()
)
etherStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsMulticastPkts.setStatus("mandatory")
_EtherStatsCRCAlignErrors_Type = Counter32
_EtherStatsCRCAlignErrors_Object = MibTableColumn
etherStatsCRCAlignErrors = _EtherStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 8),
    _EtherStatsCRCAlignErrors_Type()
)
etherStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsCRCAlignErrors.setStatus("mandatory")
_EtherStatsUndersizePkts_Type = Counter32
_EtherStatsUndersizePkts_Object = MibTableColumn
etherStatsUndersizePkts = _EtherStatsUndersizePkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 9),
    _EtherStatsUndersizePkts_Type()
)
etherStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsUndersizePkts.setStatus("mandatory")
_EtherStatsOversizePkts_Type = Counter32
_EtherStatsOversizePkts_Object = MibTableColumn
etherStatsOversizePkts = _EtherStatsOversizePkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 10),
    _EtherStatsOversizePkts_Type()
)
etherStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsOversizePkts.setStatus("mandatory")
_EtherStatsFragments_Type = Counter32
_EtherStatsFragments_Object = MibTableColumn
etherStatsFragments = _EtherStatsFragments_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 11),
    _EtherStatsFragments_Type()
)
etherStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsFragments.setStatus("mandatory")
_EtherStatsJabbers_Type = Counter32
_EtherStatsJabbers_Object = MibTableColumn
etherStatsJabbers = _EtherStatsJabbers_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 12),
    _EtherStatsJabbers_Type()
)
etherStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsJabbers.setStatus("mandatory")
_EtherStatsCollisions_Type = Counter32
_EtherStatsCollisions_Object = MibTableColumn
etherStatsCollisions = _EtherStatsCollisions_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 13),
    _EtherStatsCollisions_Type()
)
etherStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsCollisions.setStatus("mandatory")
_EtherStatsPkts64Octets_Type = Counter32
_EtherStatsPkts64Octets_Object = MibTableColumn
etherStatsPkts64Octets = _EtherStatsPkts64Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 14),
    _EtherStatsPkts64Octets_Type()
)
etherStatsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsPkts64Octets.setStatus("mandatory")
_EtherStatsPkts65to127Octets_Type = Counter32
_EtherStatsPkts65to127Octets_Object = MibTableColumn
etherStatsPkts65to127Octets = _EtherStatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 15),
    _EtherStatsPkts65to127Octets_Type()
)
etherStatsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsPkts65to127Octets.setStatus("mandatory")
_EtherStatsPkts128to255Octets_Type = Counter32
_EtherStatsPkts128to255Octets_Object = MibTableColumn
etherStatsPkts128to255Octets = _EtherStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 16),
    _EtherStatsPkts128to255Octets_Type()
)
etherStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsPkts128to255Octets.setStatus("mandatory")
_EtherStatsPkts256to511Octets_Type = Counter32
_EtherStatsPkts256to511Octets_Object = MibTableColumn
etherStatsPkts256to511Octets = _EtherStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 17),
    _EtherStatsPkts256to511Octets_Type()
)
etherStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsPkts256to511Octets.setStatus("mandatory")
_EtherStatsPkts512to1023Octets_Type = Counter32
_EtherStatsPkts512to1023Octets_Object = MibTableColumn
etherStatsPkts512to1023Octets = _EtherStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 18),
    _EtherStatsPkts512to1023Octets_Type()
)
etherStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsPkts512to1023Octets.setStatus("mandatory")
_EtherStatsPkts1024to1518Octets_Type = Counter32
_EtherStatsPkts1024to1518Octets_Object = MibTableColumn
etherStatsPkts1024to1518Octets = _EtherStatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 19),
    _EtherStatsPkts1024to1518Octets_Type()
)
etherStatsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherStatsPkts1024to1518Octets.setStatus("mandatory")
_EtherStatsOwner_Type = OwnerString
_EtherStatsOwner_Object = MibTableColumn
etherStatsOwner = _EtherStatsOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 20),
    _EtherStatsOwner_Type()
)
etherStatsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherStatsOwner.setStatus("mandatory")
_EtherStatsStatus_Type = EntryStatus
_EtherStatsStatus_Object = MibTableColumn
etherStatsStatus = _EtherStatsStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 21),
    _EtherStatsStatus_Type()
)
etherStatsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherStatsStatus.setStatus("mandatory")
_History_ObjectIdentity = ObjectIdentity
history = _History_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 2)
)
_HistoryControlTable_Object = MibTable
historyControlTable = _HistoryControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 1)
)
if mibBuilder.loadTexts:
    historyControlTable.setStatus("mandatory")
_HistoryControlEntry_Object = MibTableRow
historyControlEntry = _HistoryControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 1, 1)
)
historyControlEntry.setIndexNames(
    (0, "RFC1271-MIB", "historyControlIndex"),
)
if mibBuilder.loadTexts:
    historyControlEntry.setStatus("mandatory")


class _HistoryControlIndex_Type(Integer32):
    """Custom type historyControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HistoryControlIndex_Type.__name__ = "Integer32"
_HistoryControlIndex_Object = MibTableColumn
historyControlIndex = _HistoryControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 1),
    _HistoryControlIndex_Type()
)
historyControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyControlIndex.setStatus("mandatory")
_HistoryControlDataSource_Type = ObjectIdentifier
_HistoryControlDataSource_Object = MibTableColumn
historyControlDataSource = _HistoryControlDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 2),
    _HistoryControlDataSource_Type()
)
historyControlDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyControlDataSource.setStatus("mandatory")


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
    (1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 3),
    _HistoryControlBucketsRequested_Type()
)
historyControlBucketsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyControlBucketsRequested.setStatus("mandatory")


class _HistoryControlBucketsGranted_Type(Integer32):
    """Custom type historyControlBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HistoryControlBucketsGranted_Type.__name__ = "Integer32"
_HistoryControlBucketsGranted_Object = MibTableColumn
historyControlBucketsGranted = _HistoryControlBucketsGranted_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 4),
    _HistoryControlBucketsGranted_Type()
)
historyControlBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyControlBucketsGranted.setStatus("mandatory")


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
    (1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 5),
    _HistoryControlInterval_Type()
)
historyControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyControlInterval.setStatus("mandatory")
_HistoryControlOwner_Type = OwnerString
_HistoryControlOwner_Object = MibTableColumn
historyControlOwner = _HistoryControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 6),
    _HistoryControlOwner_Type()
)
historyControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyControlOwner.setStatus("mandatory")
_HistoryControlStatus_Type = EntryStatus
_HistoryControlStatus_Object = MibTableColumn
historyControlStatus = _HistoryControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 7),
    _HistoryControlStatus_Type()
)
historyControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyControlStatus.setStatus("mandatory")
_EtherHistoryTable_Object = MibTable
etherHistoryTable = _EtherHistoryTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 2)
)
if mibBuilder.loadTexts:
    etherHistoryTable.setStatus("mandatory")
_EtherHistoryEntry_Object = MibTableRow
etherHistoryEntry = _EtherHistoryEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1)
)
etherHistoryEntry.setIndexNames(
    (0, "RFC1271-MIB", "etherHistoryIndex"),
    (0, "RFC1271-MIB", "etherHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    etherHistoryEntry.setStatus("mandatory")


class _EtherHistoryIndex_Type(Integer32):
    """Custom type etherHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtherHistoryIndex_Type.__name__ = "Integer32"
_EtherHistoryIndex_Object = MibTableColumn
etherHistoryIndex = _EtherHistoryIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 1),
    _EtherHistoryIndex_Type()
)
etherHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryIndex.setStatus("mandatory")
_EtherHistorySampleIndex_Type = Integer32
_EtherHistorySampleIndex_Object = MibTableColumn
etherHistorySampleIndex = _EtherHistorySampleIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 2),
    _EtherHistorySampleIndex_Type()
)
etherHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistorySampleIndex.setStatus("mandatory")
_EtherHistoryIntervalStart_Type = TimeTicks
_EtherHistoryIntervalStart_Object = MibTableColumn
etherHistoryIntervalStart = _EtherHistoryIntervalStart_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 3),
    _EtherHistoryIntervalStart_Type()
)
etherHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryIntervalStart.setStatus("mandatory")
_EtherHistoryDropEvents_Type = Counter32
_EtherHistoryDropEvents_Object = MibTableColumn
etherHistoryDropEvents = _EtherHistoryDropEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 4),
    _EtherHistoryDropEvents_Type()
)
etherHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryDropEvents.setStatus("mandatory")
_EtherHistoryOctets_Type = Counter32
_EtherHistoryOctets_Object = MibTableColumn
etherHistoryOctets = _EtherHistoryOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 5),
    _EtherHistoryOctets_Type()
)
etherHistoryOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryOctets.setStatus("mandatory")
_EtherHistoryPkts_Type = Counter32
_EtherHistoryPkts_Object = MibTableColumn
etherHistoryPkts = _EtherHistoryPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 6),
    _EtherHistoryPkts_Type()
)
etherHistoryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryPkts.setStatus("mandatory")
_EtherHistoryBroadcastPkts_Type = Counter32
_EtherHistoryBroadcastPkts_Object = MibTableColumn
etherHistoryBroadcastPkts = _EtherHistoryBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 7),
    _EtherHistoryBroadcastPkts_Type()
)
etherHistoryBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryBroadcastPkts.setStatus("mandatory")
_EtherHistoryMulticastPkts_Type = Counter32
_EtherHistoryMulticastPkts_Object = MibTableColumn
etherHistoryMulticastPkts = _EtherHistoryMulticastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 8),
    _EtherHistoryMulticastPkts_Type()
)
etherHistoryMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryMulticastPkts.setStatus("mandatory")
_EtherHistoryCRCAlignErrors_Type = Counter32
_EtherHistoryCRCAlignErrors_Object = MibTableColumn
etherHistoryCRCAlignErrors = _EtherHistoryCRCAlignErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 9),
    _EtherHistoryCRCAlignErrors_Type()
)
etherHistoryCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryCRCAlignErrors.setStatus("mandatory")
_EtherHistoryUndersizePkts_Type = Counter32
_EtherHistoryUndersizePkts_Object = MibTableColumn
etherHistoryUndersizePkts = _EtherHistoryUndersizePkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 10),
    _EtherHistoryUndersizePkts_Type()
)
etherHistoryUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryUndersizePkts.setStatus("mandatory")
_EtherHistoryOversizePkts_Type = Counter32
_EtherHistoryOversizePkts_Object = MibTableColumn
etherHistoryOversizePkts = _EtherHistoryOversizePkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 11),
    _EtherHistoryOversizePkts_Type()
)
etherHistoryOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryOversizePkts.setStatus("mandatory")
_EtherHistoryFragments_Type = Counter32
_EtherHistoryFragments_Object = MibTableColumn
etherHistoryFragments = _EtherHistoryFragments_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 12),
    _EtherHistoryFragments_Type()
)
etherHistoryFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryFragments.setStatus("mandatory")
_EtherHistoryJabbers_Type = Counter32
_EtherHistoryJabbers_Object = MibTableColumn
etherHistoryJabbers = _EtherHistoryJabbers_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 13),
    _EtherHistoryJabbers_Type()
)
etherHistoryJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryJabbers.setStatus("mandatory")
_EtherHistoryCollisions_Type = Counter32
_EtherHistoryCollisions_Object = MibTableColumn
etherHistoryCollisions = _EtherHistoryCollisions_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 14),
    _EtherHistoryCollisions_Type()
)
etherHistoryCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryCollisions.setStatus("mandatory")


class _EtherHistoryUtilization_Type(Integer32):
    """Custom type etherHistoryUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EtherHistoryUtilization_Type.__name__ = "Integer32"
_EtherHistoryUtilization_Object = MibTableColumn
etherHistoryUtilization = _EtherHistoryUtilization_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 15),
    _EtherHistoryUtilization_Type()
)
etherHistoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherHistoryUtilization.setStatus("mandatory")
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 3)
)
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("mandatory")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1)
)
alarmEntry.setIndexNames(
    (0, "RFC1271-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("mandatory")


class _AlarmIndex_Type(Integer32):
    """Custom type alarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlarmIndex_Type.__name__ = "Integer32"
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("mandatory")
_AlarmInterval_Type = Integer32
_AlarmInterval_Object = MibTableColumn
alarmInterval = _AlarmInterval_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 2),
    _AlarmInterval_Type()
)
alarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmInterval.setStatus("mandatory")
_AlarmVariable_Type = ObjectIdentifier
_AlarmVariable_Object = MibTableColumn
alarmVariable = _AlarmVariable_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 3),
    _AlarmVariable_Type()
)
alarmVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmVariable.setStatus("mandatory")


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
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 4),
    _AlarmSampleType_Type()
)
alarmSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSampleType.setStatus("mandatory")
_AlarmValue_Type = Integer32
_AlarmValue_Object = MibTableColumn
alarmValue = _AlarmValue_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 5),
    _AlarmValue_Type()
)
alarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmValue.setStatus("mandatory")


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
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 6),
    _AlarmStartupAlarm_Type()
)
alarmStartupAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmStartupAlarm.setStatus("mandatory")
_AlarmRisingThreshold_Type = Integer32
_AlarmRisingThreshold_Object = MibTableColumn
alarmRisingThreshold = _AlarmRisingThreshold_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 7),
    _AlarmRisingThreshold_Type()
)
alarmRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRisingThreshold.setStatus("mandatory")
_AlarmFallingThreshold_Type = Integer32
_AlarmFallingThreshold_Object = MibTableColumn
alarmFallingThreshold = _AlarmFallingThreshold_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 8),
    _AlarmFallingThreshold_Type()
)
alarmFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmFallingThreshold.setStatus("mandatory")


class _AlarmRisingEventIndex_Type(Integer32):
    """Custom type alarmRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlarmRisingEventIndex_Type.__name__ = "Integer32"
_AlarmRisingEventIndex_Object = MibTableColumn
alarmRisingEventIndex = _AlarmRisingEventIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 9),
    _AlarmRisingEventIndex_Type()
)
alarmRisingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRisingEventIndex.setStatus("mandatory")


class _AlarmFallingEventIndex_Type(Integer32):
    """Custom type alarmFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlarmFallingEventIndex_Type.__name__ = "Integer32"
_AlarmFallingEventIndex_Object = MibTableColumn
alarmFallingEventIndex = _AlarmFallingEventIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 10),
    _AlarmFallingEventIndex_Type()
)
alarmFallingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmFallingEventIndex.setStatus("mandatory")
_AlarmOwner_Type = OwnerString
_AlarmOwner_Object = MibTableColumn
alarmOwner = _AlarmOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 11),
    _AlarmOwner_Type()
)
alarmOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmOwner.setStatus("mandatory")
_AlarmStatus_Type = EntryStatus
_AlarmStatus_Object = MibTableColumn
alarmStatus = _AlarmStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 12),
    _AlarmStatus_Type()
)
alarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmStatus.setStatus("mandatory")
_Hosts_ObjectIdentity = ObjectIdentity
hosts = _Hosts_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 4)
)
_HostControlTable_Object = MibTable
hostControlTable = _HostControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 1)
)
if mibBuilder.loadTexts:
    hostControlTable.setStatus("mandatory")
_HostControlEntry_Object = MibTableRow
hostControlEntry = _HostControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 1, 1)
)
hostControlEntry.setIndexNames(
    (0, "RFC1271-MIB", "hostControlIndex"),
)
if mibBuilder.loadTexts:
    hostControlEntry.setStatus("mandatory")


class _HostControlIndex_Type(Integer32):
    """Custom type hostControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostControlIndex_Type.__name__ = "Integer32"
_HostControlIndex_Object = MibTableColumn
hostControlIndex = _HostControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 1),
    _HostControlIndex_Type()
)
hostControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostControlIndex.setStatus("mandatory")
_HostControlDataSource_Type = ObjectIdentifier
_HostControlDataSource_Object = MibTableColumn
hostControlDataSource = _HostControlDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 2),
    _HostControlDataSource_Type()
)
hostControlDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostControlDataSource.setStatus("mandatory")
_HostControlTableSize_Type = Integer32
_HostControlTableSize_Object = MibTableColumn
hostControlTableSize = _HostControlTableSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 3),
    _HostControlTableSize_Type()
)
hostControlTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostControlTableSize.setStatus("mandatory")
_HostControlLastDeleteTime_Type = TimeTicks
_HostControlLastDeleteTime_Object = MibTableColumn
hostControlLastDeleteTime = _HostControlLastDeleteTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 4),
    _HostControlLastDeleteTime_Type()
)
hostControlLastDeleteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostControlLastDeleteTime.setStatus("mandatory")
_HostControlOwner_Type = OwnerString
_HostControlOwner_Object = MibTableColumn
hostControlOwner = _HostControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 5),
    _HostControlOwner_Type()
)
hostControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostControlOwner.setStatus("mandatory")
_HostControlStatus_Type = EntryStatus
_HostControlStatus_Object = MibTableColumn
hostControlStatus = _HostControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 6),
    _HostControlStatus_Type()
)
hostControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostControlStatus.setStatus("mandatory")
_HostTable_Object = MibTable
hostTable = _HostTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 2)
)
if mibBuilder.loadTexts:
    hostTable.setStatus("mandatory")
_HostEntry_Object = MibTableRow
hostEntry = _HostEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 2, 1)
)
hostEntry.setIndexNames(
    (0, "RFC1271-MIB", "hostIndex"),
    (0, "RFC1271-MIB", "hostAddress"),
)
if mibBuilder.loadTexts:
    hostEntry.setStatus("mandatory")
_HostAddress_Type = OctetString
_HostAddress_Object = MibTableColumn
hostAddress = _HostAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 1),
    _HostAddress_Type()
)
hostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostAddress.setStatus("mandatory")


class _HostCreationOrder_Type(Integer32):
    """Custom type hostCreationOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostCreationOrder_Type.__name__ = "Integer32"
_HostCreationOrder_Object = MibTableColumn
hostCreationOrder = _HostCreationOrder_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 2),
    _HostCreationOrder_Type()
)
hostCreationOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostCreationOrder.setStatus("mandatory")


class _HostIndex_Type(Integer32):
    """Custom type hostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostIndex_Type.__name__ = "Integer32"
_HostIndex_Object = MibTableColumn
hostIndex = _HostIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 3),
    _HostIndex_Type()
)
hostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIndex.setStatus("mandatory")
_HostInPkts_Type = Counter32
_HostInPkts_Object = MibTableColumn
hostInPkts = _HostInPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 4),
    _HostInPkts_Type()
)
hostInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostInPkts.setStatus("mandatory")
_HostOutPkts_Type = Counter32
_HostOutPkts_Object = MibTableColumn
hostOutPkts = _HostOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 5),
    _HostOutPkts_Type()
)
hostOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostOutPkts.setStatus("mandatory")
_HostInOctets_Type = Counter32
_HostInOctets_Object = MibTableColumn
hostInOctets = _HostInOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 6),
    _HostInOctets_Type()
)
hostInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostInOctets.setStatus("mandatory")
_HostOutOctets_Type = Counter32
_HostOutOctets_Object = MibTableColumn
hostOutOctets = _HostOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 7),
    _HostOutOctets_Type()
)
hostOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostOutOctets.setStatus("mandatory")
_HostOutErrors_Type = Counter32
_HostOutErrors_Object = MibTableColumn
hostOutErrors = _HostOutErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 8),
    _HostOutErrors_Type()
)
hostOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostOutErrors.setStatus("mandatory")
_HostOutBroadcastPkts_Type = Counter32
_HostOutBroadcastPkts_Object = MibTableColumn
hostOutBroadcastPkts = _HostOutBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 9),
    _HostOutBroadcastPkts_Type()
)
hostOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostOutBroadcastPkts.setStatus("mandatory")
_HostOutMulticastPkts_Type = Counter32
_HostOutMulticastPkts_Object = MibTableColumn
hostOutMulticastPkts = _HostOutMulticastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 10),
    _HostOutMulticastPkts_Type()
)
hostOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostOutMulticastPkts.setStatus("mandatory")
_HostTimeTable_Object = MibTable
hostTimeTable = _HostTimeTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 3)
)
if mibBuilder.loadTexts:
    hostTimeTable.setStatus("mandatory")
_HostTimeEntry_Object = MibTableRow
hostTimeEntry = _HostTimeEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 3, 1)
)
hostTimeEntry.setIndexNames(
    (0, "RFC1271-MIB", "hostTimeIndex"),
    (0, "RFC1271-MIB", "hostTimeCreationOrder"),
)
if mibBuilder.loadTexts:
    hostTimeEntry.setStatus("mandatory")
_HostTimeAddress_Type = OctetString
_HostTimeAddress_Object = MibTableColumn
hostTimeAddress = _HostTimeAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 1),
    _HostTimeAddress_Type()
)
hostTimeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeAddress.setStatus("mandatory")


class _HostTimeCreationOrder_Type(Integer32):
    """Custom type hostTimeCreationOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostTimeCreationOrder_Type.__name__ = "Integer32"
_HostTimeCreationOrder_Object = MibTableColumn
hostTimeCreationOrder = _HostTimeCreationOrder_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 2),
    _HostTimeCreationOrder_Type()
)
hostTimeCreationOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeCreationOrder.setStatus("mandatory")


class _HostTimeIndex_Type(Integer32):
    """Custom type hostTimeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostTimeIndex_Type.__name__ = "Integer32"
_HostTimeIndex_Object = MibTableColumn
hostTimeIndex = _HostTimeIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 3),
    _HostTimeIndex_Type()
)
hostTimeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeIndex.setStatus("mandatory")
_HostTimeInPkts_Type = Counter32
_HostTimeInPkts_Object = MibTableColumn
hostTimeInPkts = _HostTimeInPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 4),
    _HostTimeInPkts_Type()
)
hostTimeInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeInPkts.setStatus("mandatory")
_HostTimeOutPkts_Type = Counter32
_HostTimeOutPkts_Object = MibTableColumn
hostTimeOutPkts = _HostTimeOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 5),
    _HostTimeOutPkts_Type()
)
hostTimeOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeOutPkts.setStatus("mandatory")
_HostTimeInOctets_Type = Counter32
_HostTimeInOctets_Object = MibTableColumn
hostTimeInOctets = _HostTimeInOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 6),
    _HostTimeInOctets_Type()
)
hostTimeInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeInOctets.setStatus("mandatory")
_HostTimeOutOctets_Type = Counter32
_HostTimeOutOctets_Object = MibTableColumn
hostTimeOutOctets = _HostTimeOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 7),
    _HostTimeOutOctets_Type()
)
hostTimeOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeOutOctets.setStatus("mandatory")
_HostTimeOutErrors_Type = Counter32
_HostTimeOutErrors_Object = MibTableColumn
hostTimeOutErrors = _HostTimeOutErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 8),
    _HostTimeOutErrors_Type()
)
hostTimeOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeOutErrors.setStatus("mandatory")
_HostTimeOutBroadcastPkts_Type = Counter32
_HostTimeOutBroadcastPkts_Object = MibTableColumn
hostTimeOutBroadcastPkts = _HostTimeOutBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 9),
    _HostTimeOutBroadcastPkts_Type()
)
hostTimeOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeOutBroadcastPkts.setStatus("mandatory")
_HostTimeOutMulticastPkts_Type = Counter32
_HostTimeOutMulticastPkts_Object = MibTableColumn
hostTimeOutMulticastPkts = _HostTimeOutMulticastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 10),
    _HostTimeOutMulticastPkts_Type()
)
hostTimeOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTimeOutMulticastPkts.setStatus("mandatory")
_HostTopN_ObjectIdentity = ObjectIdentity
hostTopN = _HostTopN_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 5)
)
_HostTopNControlTable_Object = MibTable
hostTopNControlTable = _HostTopNControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 1)
)
if mibBuilder.loadTexts:
    hostTopNControlTable.setStatus("mandatory")
_HostTopNControlEntry_Object = MibTableRow
hostTopNControlEntry = _HostTopNControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1)
)
hostTopNControlEntry.setIndexNames(
    (0, "RFC1271-MIB", "hostTopNControlIndex"),
)
if mibBuilder.loadTexts:
    hostTopNControlEntry.setStatus("mandatory")


class _HostTopNControlIndex_Type(Integer32):
    """Custom type hostTopNControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostTopNControlIndex_Type.__name__ = "Integer32"
_HostTopNControlIndex_Object = MibTableColumn
hostTopNControlIndex = _HostTopNControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 1),
    _HostTopNControlIndex_Type()
)
hostTopNControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNControlIndex.setStatus("mandatory")


class _HostTopNHostIndex_Type(Integer32):
    """Custom type hostTopNHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostTopNHostIndex_Type.__name__ = "Integer32"
_HostTopNHostIndex_Object = MibTableColumn
hostTopNHostIndex = _HostTopNHostIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 2),
    _HostTopNHostIndex_Type()
)
hostTopNHostIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostTopNHostIndex.setStatus("mandatory")


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
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 3),
    _HostTopNRateBase_Type()
)
hostTopNRateBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostTopNRateBase.setStatus("mandatory")


class _HostTopNTimeRemaining_Type(Integer32):
    """Custom type hostTopNTimeRemaining based on Integer32"""
    defaultValue = 0


_HostTopNTimeRemaining_Object = MibTableColumn
hostTopNTimeRemaining = _HostTopNTimeRemaining_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 4),
    _HostTopNTimeRemaining_Type()
)
hostTopNTimeRemaining.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostTopNTimeRemaining.setStatus("mandatory")


class _HostTopNDuration_Type(Integer32):
    """Custom type hostTopNDuration based on Integer32"""
    defaultValue = 0


_HostTopNDuration_Object = MibTableColumn
hostTopNDuration = _HostTopNDuration_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 5),
    _HostTopNDuration_Type()
)
hostTopNDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNDuration.setStatus("mandatory")


class _HostTopNRequestedSize_Type(Integer32):
    """Custom type hostTopNRequestedSize based on Integer32"""
    defaultValue = 10


_HostTopNRequestedSize_Object = MibTableColumn
hostTopNRequestedSize = _HostTopNRequestedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 6),
    _HostTopNRequestedSize_Type()
)
hostTopNRequestedSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostTopNRequestedSize.setStatus("mandatory")
_HostTopNGrantedSize_Type = Integer32
_HostTopNGrantedSize_Object = MibTableColumn
hostTopNGrantedSize = _HostTopNGrantedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 7),
    _HostTopNGrantedSize_Type()
)
hostTopNGrantedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNGrantedSize.setStatus("mandatory")
_HostTopNStartTime_Type = TimeTicks
_HostTopNStartTime_Object = MibTableColumn
hostTopNStartTime = _HostTopNStartTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 8),
    _HostTopNStartTime_Type()
)
hostTopNStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNStartTime.setStatus("mandatory")
_HostTopNOwner_Type = OwnerString
_HostTopNOwner_Object = MibTableColumn
hostTopNOwner = _HostTopNOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 9),
    _HostTopNOwner_Type()
)
hostTopNOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostTopNOwner.setStatus("mandatory")
_HostTopNStatus_Type = EntryStatus
_HostTopNStatus_Object = MibTableColumn
hostTopNStatus = _HostTopNStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 10),
    _HostTopNStatus_Type()
)
hostTopNStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostTopNStatus.setStatus("mandatory")
_HostTopNTable_Object = MibTable
hostTopNTable = _HostTopNTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 2)
)
if mibBuilder.loadTexts:
    hostTopNTable.setStatus("mandatory")
_HostTopNEntry_Object = MibTableRow
hostTopNEntry = _HostTopNEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 2, 1)
)
hostTopNEntry.setIndexNames(
    (0, "RFC1271-MIB", "hostTopNReport"),
    (0, "RFC1271-MIB", "hostTopNIndex"),
)
if mibBuilder.loadTexts:
    hostTopNEntry.setStatus("mandatory")


class _HostTopNReport_Type(Integer32):
    """Custom type hostTopNReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostTopNReport_Type.__name__ = "Integer32"
_HostTopNReport_Object = MibTableColumn
hostTopNReport = _HostTopNReport_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 2, 1, 1),
    _HostTopNReport_Type()
)
hostTopNReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNReport.setStatus("mandatory")


class _HostTopNIndex_Type(Integer32):
    """Custom type hostTopNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostTopNIndex_Type.__name__ = "Integer32"
_HostTopNIndex_Object = MibTableColumn
hostTopNIndex = _HostTopNIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 2, 1, 2),
    _HostTopNIndex_Type()
)
hostTopNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNIndex.setStatus("mandatory")
_HostTopNAddress_Type = OctetString
_HostTopNAddress_Object = MibTableColumn
hostTopNAddress = _HostTopNAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 2, 1, 3),
    _HostTopNAddress_Type()
)
hostTopNAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNAddress.setStatus("mandatory")
_HostTopNRate_Type = Integer32
_HostTopNRate_Object = MibTableColumn
hostTopNRate = _HostTopNRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 5, 2, 1, 4),
    _HostTopNRate_Type()
)
hostTopNRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostTopNRate.setStatus("mandatory")
_Matrix_ObjectIdentity = ObjectIdentity
matrix = _Matrix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 6)
)
_MatrixControlTable_Object = MibTable
matrixControlTable = _MatrixControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 1)
)
if mibBuilder.loadTexts:
    matrixControlTable.setStatus("mandatory")
_MatrixControlEntry_Object = MibTableRow
matrixControlEntry = _MatrixControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 1, 1)
)
matrixControlEntry.setIndexNames(
    (0, "RFC1271-MIB", "matrixControlIndex"),
)
if mibBuilder.loadTexts:
    matrixControlEntry.setStatus("mandatory")


class _MatrixControlIndex_Type(Integer32):
    """Custom type matrixControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MatrixControlIndex_Type.__name__ = "Integer32"
_MatrixControlIndex_Object = MibTableColumn
matrixControlIndex = _MatrixControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 1),
    _MatrixControlIndex_Type()
)
matrixControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixControlIndex.setStatus("mandatory")
_MatrixControlDataSource_Type = ObjectIdentifier
_MatrixControlDataSource_Object = MibTableColumn
matrixControlDataSource = _MatrixControlDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 2),
    _MatrixControlDataSource_Type()
)
matrixControlDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matrixControlDataSource.setStatus("mandatory")
_MatrixControlTableSize_Type = Integer32
_MatrixControlTableSize_Object = MibTableColumn
matrixControlTableSize = _MatrixControlTableSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 3),
    _MatrixControlTableSize_Type()
)
matrixControlTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixControlTableSize.setStatus("mandatory")
_MatrixControlLastDeleteTime_Type = TimeTicks
_MatrixControlLastDeleteTime_Object = MibTableColumn
matrixControlLastDeleteTime = _MatrixControlLastDeleteTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 4),
    _MatrixControlLastDeleteTime_Type()
)
matrixControlLastDeleteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixControlLastDeleteTime.setStatus("mandatory")
_MatrixControlOwner_Type = OwnerString
_MatrixControlOwner_Object = MibTableColumn
matrixControlOwner = _MatrixControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 5),
    _MatrixControlOwner_Type()
)
matrixControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matrixControlOwner.setStatus("mandatory")
_MatrixControlStatus_Type = EntryStatus
_MatrixControlStatus_Object = MibTableColumn
matrixControlStatus = _MatrixControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 6),
    _MatrixControlStatus_Type()
)
matrixControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    matrixControlStatus.setStatus("mandatory")
_MatrixSDTable_Object = MibTable
matrixSDTable = _MatrixSDTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 2)
)
if mibBuilder.loadTexts:
    matrixSDTable.setStatus("mandatory")
_MatrixSDEntry_Object = MibTableRow
matrixSDEntry = _MatrixSDEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 2, 1)
)
matrixSDEntry.setIndexNames(
    (0, "RFC1271-MIB", "matrixSDIndex"),
    (0, "RFC1271-MIB", "matrixSDSourceAddress"),
    (0, "RFC1271-MIB", "matrixSDDestAddress"),
)
if mibBuilder.loadTexts:
    matrixSDEntry.setStatus("mandatory")
_MatrixSDSourceAddress_Type = OctetString
_MatrixSDSourceAddress_Object = MibTableColumn
matrixSDSourceAddress = _MatrixSDSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 1),
    _MatrixSDSourceAddress_Type()
)
matrixSDSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDSourceAddress.setStatus("mandatory")
_MatrixSDDestAddress_Type = OctetString
_MatrixSDDestAddress_Object = MibTableColumn
matrixSDDestAddress = _MatrixSDDestAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 2),
    _MatrixSDDestAddress_Type()
)
matrixSDDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDDestAddress.setStatus("mandatory")


class _MatrixSDIndex_Type(Integer32):
    """Custom type matrixSDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MatrixSDIndex_Type.__name__ = "Integer32"
_MatrixSDIndex_Object = MibTableColumn
matrixSDIndex = _MatrixSDIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 3),
    _MatrixSDIndex_Type()
)
matrixSDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDIndex.setStatus("mandatory")
_MatrixSDPkts_Type = Counter32
_MatrixSDPkts_Object = MibTableColumn
matrixSDPkts = _MatrixSDPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 4),
    _MatrixSDPkts_Type()
)
matrixSDPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDPkts.setStatus("mandatory")
_MatrixSDOctets_Type = Counter32
_MatrixSDOctets_Object = MibTableColumn
matrixSDOctets = _MatrixSDOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 5),
    _MatrixSDOctets_Type()
)
matrixSDOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDOctets.setStatus("mandatory")
_MatrixSDErrors_Type = Counter32
_MatrixSDErrors_Object = MibTableColumn
matrixSDErrors = _MatrixSDErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 6),
    _MatrixSDErrors_Type()
)
matrixSDErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixSDErrors.setStatus("mandatory")
_MatrixDSTable_Object = MibTable
matrixDSTable = _MatrixDSTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 3)
)
if mibBuilder.loadTexts:
    matrixDSTable.setStatus("mandatory")
_MatrixDSEntry_Object = MibTableRow
matrixDSEntry = _MatrixDSEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 3, 1)
)
matrixDSEntry.setIndexNames(
    (0, "RFC1271-MIB", "matrixDSIndex"),
    (0, "RFC1271-MIB", "matrixDSDestAddress"),
    (0, "RFC1271-MIB", "matrixDSSourceAddress"),
)
if mibBuilder.loadTexts:
    matrixDSEntry.setStatus("mandatory")
_MatrixDSSourceAddress_Type = OctetString
_MatrixDSSourceAddress_Object = MibTableColumn
matrixDSSourceAddress = _MatrixDSSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 1),
    _MatrixDSSourceAddress_Type()
)
matrixDSSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSSourceAddress.setStatus("mandatory")
_MatrixDSDestAddress_Type = OctetString
_MatrixDSDestAddress_Object = MibTableColumn
matrixDSDestAddress = _MatrixDSDestAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 2),
    _MatrixDSDestAddress_Type()
)
matrixDSDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSDestAddress.setStatus("mandatory")


class _MatrixDSIndex_Type(Integer32):
    """Custom type matrixDSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MatrixDSIndex_Type.__name__ = "Integer32"
_MatrixDSIndex_Object = MibTableColumn
matrixDSIndex = _MatrixDSIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 3),
    _MatrixDSIndex_Type()
)
matrixDSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSIndex.setStatus("mandatory")
_MatrixDSPkts_Type = Counter32
_MatrixDSPkts_Object = MibTableColumn
matrixDSPkts = _MatrixDSPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 4),
    _MatrixDSPkts_Type()
)
matrixDSPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSPkts.setStatus("mandatory")
_MatrixDSOctets_Type = Counter32
_MatrixDSOctets_Object = MibTableColumn
matrixDSOctets = _MatrixDSOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 5),
    _MatrixDSOctets_Type()
)
matrixDSOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSOctets.setStatus("mandatory")
_MatrixDSErrors_Type = Counter32
_MatrixDSErrors_Object = MibTableColumn
matrixDSErrors = _MatrixDSErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 6),
    _MatrixDSErrors_Type()
)
matrixDSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    matrixDSErrors.setStatus("mandatory")
_Filter_ObjectIdentity = ObjectIdentity
filter = _Filter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 7)
)
_FilterTable_Object = MibTable
filterTable = _FilterTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 1)
)
if mibBuilder.loadTexts:
    filterTable.setStatus("mandatory")
_FilterEntry_Object = MibTableRow
filterEntry = _FilterEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1)
)
filterEntry.setIndexNames(
    (0, "RFC1271-MIB", "filterIndex"),
)
if mibBuilder.loadTexts:
    filterEntry.setStatus("mandatory")


class _FilterIndex_Type(Integer32):
    """Custom type filterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FilterIndex_Type.__name__ = "Integer32"
_FilterIndex_Object = MibTableColumn
filterIndex = _FilterIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 1),
    _FilterIndex_Type()
)
filterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterIndex.setStatus("mandatory")


class _FilterChannelIndex_Type(Integer32):
    """Custom type filterChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FilterChannelIndex_Type.__name__ = "Integer32"
_FilterChannelIndex_Object = MibTableColumn
filterChannelIndex = _FilterChannelIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 2),
    _FilterChannelIndex_Type()
)
filterChannelIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterChannelIndex.setStatus("mandatory")


class _FilterPktDataOffset_Type(Integer32):
    """Custom type filterPktDataOffset based on Integer32"""
    defaultValue = 0


_FilterPktDataOffset_Object = MibTableColumn
filterPktDataOffset = _FilterPktDataOffset_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 3),
    _FilterPktDataOffset_Type()
)
filterPktDataOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPktDataOffset.setStatus("mandatory")
_FilterPktData_Type = OctetString
_FilterPktData_Object = MibTableColumn
filterPktData = _FilterPktData_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 4),
    _FilterPktData_Type()
)
filterPktData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPktData.setStatus("mandatory")
_FilterPktDataMask_Type = OctetString
_FilterPktDataMask_Object = MibTableColumn
filterPktDataMask = _FilterPktDataMask_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 5),
    _FilterPktDataMask_Type()
)
filterPktDataMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPktDataMask.setStatus("mandatory")
_FilterPktDataNotMask_Type = OctetString
_FilterPktDataNotMask_Object = MibTableColumn
filterPktDataNotMask = _FilterPktDataNotMask_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 6),
    _FilterPktDataNotMask_Type()
)
filterPktDataNotMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPktDataNotMask.setStatus("mandatory")
_FilterPktStatus_Type = Integer32
_FilterPktStatus_Object = MibTableColumn
filterPktStatus = _FilterPktStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 7),
    _FilterPktStatus_Type()
)
filterPktStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPktStatus.setStatus("mandatory")
_FilterPktStatusMask_Type = Integer32
_FilterPktStatusMask_Object = MibTableColumn
filterPktStatusMask = _FilterPktStatusMask_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 8),
    _FilterPktStatusMask_Type()
)
filterPktStatusMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPktStatusMask.setStatus("mandatory")
_FilterPktStatusNotMask_Type = Integer32
_FilterPktStatusNotMask_Object = MibTableColumn
filterPktStatusNotMask = _FilterPktStatusNotMask_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 9),
    _FilterPktStatusNotMask_Type()
)
filterPktStatusNotMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPktStatusNotMask.setStatus("mandatory")
_FilterOwner_Type = OwnerString
_FilterOwner_Object = MibTableColumn
filterOwner = _FilterOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 10),
    _FilterOwner_Type()
)
filterOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterOwner.setStatus("mandatory")
_FilterStatus_Type = EntryStatus
_FilterStatus_Object = MibTableColumn
filterStatus = _FilterStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 11),
    _FilterStatus_Type()
)
filterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterStatus.setStatus("mandatory")
_ChannelTable_Object = MibTable
channelTable = _ChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 2)
)
if mibBuilder.loadTexts:
    channelTable.setStatus("mandatory")
_ChannelEntry_Object = MibTableRow
channelEntry = _ChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1)
)
channelEntry.setIndexNames(
    (0, "RFC1271-MIB", "channelIndex"),
)
if mibBuilder.loadTexts:
    channelEntry.setStatus("mandatory")


class _ChannelIndex_Type(Integer32):
    """Custom type channelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChannelIndex_Type.__name__ = "Integer32"
_ChannelIndex_Object = MibTableColumn
channelIndex = _ChannelIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 1),
    _ChannelIndex_Type()
)
channelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelIndex.setStatus("mandatory")


class _ChannelIfIndex_Type(Integer32):
    """Custom type channelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChannelIfIndex_Type.__name__ = "Integer32"
_ChannelIfIndex_Object = MibTableColumn
channelIfIndex = _ChannelIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 2),
    _ChannelIfIndex_Type()
)
channelIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelIfIndex.setStatus("mandatory")


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
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 3),
    _ChannelAcceptType_Type()
)
channelAcceptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelAcceptType.setStatus("mandatory")


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
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 4),
    _ChannelDataControl_Type()
)
channelDataControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelDataControl.setStatus("mandatory")


class _ChannelTurnOnEventIndex_Type(Integer32):
    """Custom type channelTurnOnEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChannelTurnOnEventIndex_Type.__name__ = "Integer32"
_ChannelTurnOnEventIndex_Object = MibTableColumn
channelTurnOnEventIndex = _ChannelTurnOnEventIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 5),
    _ChannelTurnOnEventIndex_Type()
)
channelTurnOnEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelTurnOnEventIndex.setStatus("mandatory")


class _ChannelTurnOffEventIndex_Type(Integer32):
    """Custom type channelTurnOffEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChannelTurnOffEventIndex_Type.__name__ = "Integer32"
_ChannelTurnOffEventIndex_Object = MibTableColumn
channelTurnOffEventIndex = _ChannelTurnOffEventIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 6),
    _ChannelTurnOffEventIndex_Type()
)
channelTurnOffEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelTurnOffEventIndex.setStatus("mandatory")


class _ChannelEventIndex_Type(Integer32):
    """Custom type channelEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChannelEventIndex_Type.__name__ = "Integer32"
_ChannelEventIndex_Object = MibTableColumn
channelEventIndex = _ChannelEventIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 7),
    _ChannelEventIndex_Type()
)
channelEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelEventIndex.setStatus("mandatory")


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
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 8),
    _ChannelEventStatus_Type()
)
channelEventStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelEventStatus.setStatus("mandatory")
_ChannelMatches_Type = Counter32
_ChannelMatches_Object = MibTableColumn
channelMatches = _ChannelMatches_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 9),
    _ChannelMatches_Type()
)
channelMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelMatches.setStatus("mandatory")


class _ChannelDescription_Type(DisplayString):
    """Custom type channelDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ChannelDescription_Type.__name__ = "DisplayString"
_ChannelDescription_Object = MibTableColumn
channelDescription = _ChannelDescription_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 10),
    _ChannelDescription_Type()
)
channelDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelDescription.setStatus("mandatory")
_ChannelOwner_Type = OwnerString
_ChannelOwner_Object = MibTableColumn
channelOwner = _ChannelOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 11),
    _ChannelOwner_Type()
)
channelOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelOwner.setStatus("mandatory")
_ChannelStatus_Type = EntryStatus
_ChannelStatus_Object = MibTableColumn
channelStatus = _ChannelStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 12),
    _ChannelStatus_Type()
)
channelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelStatus.setStatus("mandatory")
_Capture_ObjectIdentity = ObjectIdentity
capture = _Capture_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 8)
)
_BufferControlTable_Object = MibTable
bufferControlTable = _BufferControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 1)
)
if mibBuilder.loadTexts:
    bufferControlTable.setStatus("mandatory")
_BufferControlEntry_Object = MibTableRow
bufferControlEntry = _BufferControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1)
)
bufferControlEntry.setIndexNames(
    (0, "RFC1271-MIB", "bufferControlIndex"),
)
if mibBuilder.loadTexts:
    bufferControlEntry.setStatus("mandatory")


class _BufferControlIndex_Type(Integer32):
    """Custom type bufferControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BufferControlIndex_Type.__name__ = "Integer32"
_BufferControlIndex_Object = MibTableColumn
bufferControlIndex = _BufferControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 1),
    _BufferControlIndex_Type()
)
bufferControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferControlIndex.setStatus("mandatory")


class _BufferControlChannelIndex_Type(Integer32):
    """Custom type bufferControlChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BufferControlChannelIndex_Type.__name__ = "Integer32"
_BufferControlChannelIndex_Object = MibTableColumn
bufferControlChannelIndex = _BufferControlChannelIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 2),
    _BufferControlChannelIndex_Type()
)
bufferControlChannelIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bufferControlChannelIndex.setStatus("mandatory")


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
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 3),
    _BufferControlFullStatus_Type()
)
bufferControlFullStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferControlFullStatus.setStatus("mandatory")


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
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 4),
    _BufferControlFullAction_Type()
)
bufferControlFullAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bufferControlFullAction.setStatus("mandatory")


class _BufferControlCaptureSliceSize_Type(Integer32):
    """Custom type bufferControlCaptureSliceSize based on Integer32"""
    defaultValue = 100


_BufferControlCaptureSliceSize_Object = MibTableColumn
bufferControlCaptureSliceSize = _BufferControlCaptureSliceSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 5),
    _BufferControlCaptureSliceSize_Type()
)
bufferControlCaptureSliceSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bufferControlCaptureSliceSize.setStatus("mandatory")


class _BufferControlDownloadSliceSize_Type(Integer32):
    """Custom type bufferControlDownloadSliceSize based on Integer32"""
    defaultValue = 100


_BufferControlDownloadSliceSize_Object = MibTableColumn
bufferControlDownloadSliceSize = _BufferControlDownloadSliceSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 6),
    _BufferControlDownloadSliceSize_Type()
)
bufferControlDownloadSliceSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bufferControlDownloadSliceSize.setStatus("mandatory")


class _BufferControlDownloadOffset_Type(Integer32):
    """Custom type bufferControlDownloadOffset based on Integer32"""
    defaultValue = 0


_BufferControlDownloadOffset_Object = MibTableColumn
bufferControlDownloadOffset = _BufferControlDownloadOffset_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 7),
    _BufferControlDownloadOffset_Type()
)
bufferControlDownloadOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bufferControlDownloadOffset.setStatus("mandatory")


class _BufferControlMaxOctetsRequested_Type(Integer32):
    """Custom type bufferControlMaxOctetsRequested based on Integer32"""
    defaultValue = -1


_BufferControlMaxOctetsRequested_Object = MibTableColumn
bufferControlMaxOctetsRequested = _BufferControlMaxOctetsRequested_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 8),
    _BufferControlMaxOctetsRequested_Type()
)
bufferControlMaxOctetsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bufferControlMaxOctetsRequested.setStatus("mandatory")
_BufferControlMaxOctetsGranted_Type = Integer32
_BufferControlMaxOctetsGranted_Object = MibTableColumn
bufferControlMaxOctetsGranted = _BufferControlMaxOctetsGranted_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 9),
    _BufferControlMaxOctetsGranted_Type()
)
bufferControlMaxOctetsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferControlMaxOctetsGranted.setStatus("mandatory")
_BufferControlCapturedPackets_Type = Integer32
_BufferControlCapturedPackets_Object = MibTableColumn
bufferControlCapturedPackets = _BufferControlCapturedPackets_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 10),
    _BufferControlCapturedPackets_Type()
)
bufferControlCapturedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferControlCapturedPackets.setStatus("mandatory")
_BufferControlTurnOnTime_Type = TimeTicks
_BufferControlTurnOnTime_Object = MibTableColumn
bufferControlTurnOnTime = _BufferControlTurnOnTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 11),
    _BufferControlTurnOnTime_Type()
)
bufferControlTurnOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferControlTurnOnTime.setStatus("mandatory")
_BufferControlOwner_Type = OwnerString
_BufferControlOwner_Object = MibTableColumn
bufferControlOwner = _BufferControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 12),
    _BufferControlOwner_Type()
)
bufferControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bufferControlOwner.setStatus("mandatory")
_BufferControlStatus_Type = EntryStatus
_BufferControlStatus_Object = MibTableColumn
bufferControlStatus = _BufferControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 13),
    _BufferControlStatus_Type()
)
bufferControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bufferControlStatus.setStatus("mandatory")
_CaptureBufferTable_Object = MibTable
captureBufferTable = _CaptureBufferTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 2)
)
if mibBuilder.loadTexts:
    captureBufferTable.setStatus("mandatory")
_CaptureBufferEntry_Object = MibTableRow
captureBufferEntry = _CaptureBufferEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 2, 1)
)
captureBufferEntry.setIndexNames(
    (0, "RFC1271-MIB", "captureBufferControlIndex"),
    (0, "RFC1271-MIB", "captureBufferIndex"),
)
if mibBuilder.loadTexts:
    captureBufferEntry.setStatus("mandatory")


class _CaptureBufferControlIndex_Type(Integer32):
    """Custom type captureBufferControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CaptureBufferControlIndex_Type.__name__ = "Integer32"
_CaptureBufferControlIndex_Object = MibTableColumn
captureBufferControlIndex = _CaptureBufferControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 1),
    _CaptureBufferControlIndex_Type()
)
captureBufferControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureBufferControlIndex.setStatus("mandatory")
_CaptureBufferIndex_Type = Integer32
_CaptureBufferIndex_Object = MibTableColumn
captureBufferIndex = _CaptureBufferIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 2),
    _CaptureBufferIndex_Type()
)
captureBufferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureBufferIndex.setStatus("mandatory")
_CaptureBufferPacketID_Type = Integer32
_CaptureBufferPacketID_Object = MibTableColumn
captureBufferPacketID = _CaptureBufferPacketID_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 3),
    _CaptureBufferPacketID_Type()
)
captureBufferPacketID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureBufferPacketID.setStatus("mandatory")
_CaptureBufferPacketData_Type = OctetString
_CaptureBufferPacketData_Object = MibTableColumn
captureBufferPacketData = _CaptureBufferPacketData_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 4),
    _CaptureBufferPacketData_Type()
)
captureBufferPacketData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureBufferPacketData.setStatus("mandatory")
_CaptureBufferPacketLength_Type = Integer32
_CaptureBufferPacketLength_Object = MibTableColumn
captureBufferPacketLength = _CaptureBufferPacketLength_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 5),
    _CaptureBufferPacketLength_Type()
)
captureBufferPacketLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureBufferPacketLength.setStatus("mandatory")
_CaptureBufferPacketTime_Type = Integer32
_CaptureBufferPacketTime_Object = MibTableColumn
captureBufferPacketTime = _CaptureBufferPacketTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 6),
    _CaptureBufferPacketTime_Type()
)
captureBufferPacketTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureBufferPacketTime.setStatus("mandatory")
_CaptureBufferPacketStatus_Type = Integer32
_CaptureBufferPacketStatus_Object = MibTableColumn
captureBufferPacketStatus = _CaptureBufferPacketStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 7),
    _CaptureBufferPacketStatus_Type()
)
captureBufferPacketStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captureBufferPacketStatus.setStatus("mandatory")
_Event_ObjectIdentity = ObjectIdentity
event = _Event_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 9)
)
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("mandatory")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1)
)
eventEntry.setIndexNames(
    (0, "RFC1271-MIB", "eventIndex"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("mandatory")


class _EventIndex_Type(Integer32):
    """Custom type eventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EventIndex_Type.__name__ = "Integer32"
_EventIndex_Object = MibTableColumn
eventIndex = _EventIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 1),
    _EventIndex_Type()
)
eventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventIndex.setStatus("mandatory")


class _EventDescription_Type(DisplayString):
    """Custom type eventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EventDescription_Type.__name__ = "DisplayString"
_EventDescription_Object = MibTableColumn
eventDescription = _EventDescription_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 2),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventDescription.setStatus("mandatory")


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
          ("log-and-trap", 4),
          ("none", 1),
          ("snmp-trap", 3))
    )


_EventType_Type.__name__ = "Integer32"
_EventType_Object = MibTableColumn
eventType = _EventType_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 3),
    _EventType_Type()
)
eventType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventType.setStatus("mandatory")


class _EventCommunity_Type(OctetString):
    """Custom type eventCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EventCommunity_Type.__name__ = "OctetString"
_EventCommunity_Object = MibTableColumn
eventCommunity = _EventCommunity_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 4),
    _EventCommunity_Type()
)
eventCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventCommunity.setStatus("mandatory")
_EventLastTimeSent_Type = TimeTicks
_EventLastTimeSent_Object = MibTableColumn
eventLastTimeSent = _EventLastTimeSent_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 5),
    _EventLastTimeSent_Type()
)
eventLastTimeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLastTimeSent.setStatus("mandatory")
_EventOwner_Type = OwnerString
_EventOwner_Object = MibTableColumn
eventOwner = _EventOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 6),
    _EventOwner_Type()
)
eventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventOwner.setStatus("mandatory")
_EventStatus_Type = EntryStatus
_EventStatus_Object = MibTableColumn
eventStatus = _EventStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 7),
    _EventStatus_Type()
)
eventStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventStatus.setStatus("mandatory")
_LogTable_Object = MibTable
logTable = _LogTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2)
)
if mibBuilder.loadTexts:
    logTable.setStatus("mandatory")
_LogEntry_Object = MibTableRow
logEntry = _LogEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1)
)
logEntry.setIndexNames(
    (0, "RFC1271-MIB", "logEventIndex"),
    (0, "RFC1271-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    logEntry.setStatus("mandatory")


class _LogEventIndex_Type(Integer32):
    """Custom type logEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LogEventIndex_Type.__name__ = "Integer32"
_LogEventIndex_Object = MibTableColumn
logEventIndex = _LogEventIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 1),
    _LogEventIndex_Type()
)
logEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEventIndex.setStatus("mandatory")
_LogIndex_Type = Integer32
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 2),
    _LogIndex_Type()
)
logIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logIndex.setStatus("mandatory")
_LogTime_Type = TimeTicks
_LogTime_Object = MibTableColumn
logTime = _LogTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 3),
    _LogTime_Type()
)
logTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTime.setStatus("mandatory")


class _LogDescription_Type(DisplayString):
    """Custom type logDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LogDescription_Type.__name__ = "DisplayString"
_LogDescription_Object = MibTableColumn
logDescription = _LogDescription_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 4),
    _LogDescription_Type()
)
logDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects

risingAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 0, 1)
)
risingAlarm.setObjects(
      *(("RFC1271-MIB", "alarmIndex"),
        ("RFC1271-MIB", "alarmVariable"),
        ("RFC1271-MIB", "alarmSampleType"),
        ("RFC1271-MIB", "alarmValue"),
        ("RFC1271-MIB", "alarmRisingThreshold"))
)
if mibBuilder.loadTexts:
    risingAlarm.setStatus(
        ""
    )

fallingAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 0, 2)
)
fallingAlarm.setObjects(
      *(("RFC1271-MIB", "alarmIndex"),
        ("RFC1271-MIB", "alarmVariable"),
        ("RFC1271-MIB", "alarmSampleType"),
        ("RFC1271-MIB", "alarmValue"),
        ("RFC1271-MIB", "alarmFallingThreshold"))
)
if mibBuilder.loadTexts:
    fallingAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1271-MIB",
    **{"OwnerString": OwnerString,
       "EntryStatus": EntryStatus,
       "rmon": rmon,
       "risingAlarm": risingAlarm,
       "fallingAlarm": fallingAlarm,
       "statistics": statistics,
       "etherStatsTable": etherStatsTable,
       "etherStatsEntry": etherStatsEntry,
       "etherStatsIndex": etherStatsIndex,
       "etherStatsDataSource": etherStatsDataSource,
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
       "etherStatsOwner": etherStatsOwner,
       "etherStatsStatus": etherStatsStatus,
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
       "filter": filter,
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
       "logDescription": logDescription}
)
