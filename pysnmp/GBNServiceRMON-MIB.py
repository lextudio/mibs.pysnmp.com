# SNMP MIB module (GBNServiceRMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GBNServiceRMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:01 2024
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

(rmonMib,) = mibBuilder.importSymbols(
    "GREENTECH-MASTER-MIB",
    "rmonMib")

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

_RStatistics_ObjectIdentity = ObjectIdentity
rStatistics = _RStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1)
)
_REtherStatsTable_Object = MibTable
rEtherStatsTable = _REtherStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rEtherStatsTable.setStatus("mandatory")
_REtherStatsEntry_Object = MibTableRow
rEtherStatsEntry = _REtherStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1)
)
rEtherStatsEntry.setIndexNames(
    (0, "GBNServiceRMON-MIB", "rEtherStatsIndex"),
)
if mibBuilder.loadTexts:
    rEtherStatsEntry.setStatus("mandatory")


class _REtherStatsIndex_Type(Integer32):
    """Custom type rEtherStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_REtherStatsIndex_Type.__name__ = "Integer32"
_REtherStatsIndex_Object = MibTableColumn
rEtherStatsIndex = _REtherStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 1),
    _REtherStatsIndex_Type()
)
rEtherStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsIndex.setStatus("mandatory")
_REtherStatsDataSource_Type = ObjectIdentifier
_REtherStatsDataSource_Object = MibTableColumn
rEtherStatsDataSource = _REtherStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 2),
    _REtherStatsDataSource_Type()
)
rEtherStatsDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rEtherStatsDataSource.setStatus("mandatory")
_REtherStatsDropEvents_Type = Counter32
_REtherStatsDropEvents_Object = MibTableColumn
rEtherStatsDropEvents = _REtherStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 3),
    _REtherStatsDropEvents_Type()
)
rEtherStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsDropEvents.setStatus("mandatory")
_REtherStatsOctets_Type = Counter32
_REtherStatsOctets_Object = MibTableColumn
rEtherStatsOctets = _REtherStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 4),
    _REtherStatsOctets_Type()
)
rEtherStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsOctets.setStatus("mandatory")
_REtherStatsPkts_Type = Counter32
_REtherStatsPkts_Object = MibTableColumn
rEtherStatsPkts = _REtherStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 5),
    _REtherStatsPkts_Type()
)
rEtherStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsPkts.setStatus("mandatory")
_REtherStatsBroadcastPkts_Type = Counter32
_REtherStatsBroadcastPkts_Object = MibTableColumn
rEtherStatsBroadcastPkts = _REtherStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 6),
    _REtherStatsBroadcastPkts_Type()
)
rEtherStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsBroadcastPkts.setStatus("mandatory")
_REtherStatsMulticastPkts_Type = Counter32
_REtherStatsMulticastPkts_Object = MibTableColumn
rEtherStatsMulticastPkts = _REtherStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 7),
    _REtherStatsMulticastPkts_Type()
)
rEtherStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsMulticastPkts.setStatus("mandatory")
_REtherStatsCRCAlignErrors_Type = Counter32
_REtherStatsCRCAlignErrors_Object = MibTableColumn
rEtherStatsCRCAlignErrors = _REtherStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 8),
    _REtherStatsCRCAlignErrors_Type()
)
rEtherStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsCRCAlignErrors.setStatus("mandatory")
_REtherStatsUndersizePkts_Type = Counter32
_REtherStatsUndersizePkts_Object = MibTableColumn
rEtherStatsUndersizePkts = _REtherStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 9),
    _REtherStatsUndersizePkts_Type()
)
rEtherStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsUndersizePkts.setStatus("mandatory")
_REtherStatsOversizePkts_Type = Counter32
_REtherStatsOversizePkts_Object = MibTableColumn
rEtherStatsOversizePkts = _REtherStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 10),
    _REtherStatsOversizePkts_Type()
)
rEtherStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsOversizePkts.setStatus("mandatory")
_REtherStatsFragments_Type = Counter32
_REtherStatsFragments_Object = MibTableColumn
rEtherStatsFragments = _REtherStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 11),
    _REtherStatsFragments_Type()
)
rEtherStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsFragments.setStatus("mandatory")
_REtherStatsJabbers_Type = Counter32
_REtherStatsJabbers_Object = MibTableColumn
rEtherStatsJabbers = _REtherStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 12),
    _REtherStatsJabbers_Type()
)
rEtherStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsJabbers.setStatus("mandatory")
_REtherStatsCollisions_Type = Counter32
_REtherStatsCollisions_Object = MibTableColumn
rEtherStatsCollisions = _REtherStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 13),
    _REtherStatsCollisions_Type()
)
rEtherStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsCollisions.setStatus("mandatory")
_REtherStatsPkts64Octets_Type = Counter32
_REtherStatsPkts64Octets_Object = MibTableColumn
rEtherStatsPkts64Octets = _REtherStatsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 14),
    _REtherStatsPkts64Octets_Type()
)
rEtherStatsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsPkts64Octets.setStatus("mandatory")
_REtherStatsPkts65to127Octets_Type = Counter32
_REtherStatsPkts65to127Octets_Object = MibTableColumn
rEtherStatsPkts65to127Octets = _REtherStatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 15),
    _REtherStatsPkts65to127Octets_Type()
)
rEtherStatsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsPkts65to127Octets.setStatus("mandatory")
_REtherStatsPkts128to255Octets_Type = Counter32
_REtherStatsPkts128to255Octets_Object = MibTableColumn
rEtherStatsPkts128to255Octets = _REtherStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 16),
    _REtherStatsPkts128to255Octets_Type()
)
rEtherStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsPkts128to255Octets.setStatus("mandatory")
_REtherStatsPkts256to511Octets_Type = Counter32
_REtherStatsPkts256to511Octets_Object = MibTableColumn
rEtherStatsPkts256to511Octets = _REtherStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 17),
    _REtherStatsPkts256to511Octets_Type()
)
rEtherStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsPkts256to511Octets.setStatus("mandatory")
_REtherStatsPkts512to1023Octets_Type = Counter32
_REtherStatsPkts512to1023Octets_Object = MibTableColumn
rEtherStatsPkts512to1023Octets = _REtherStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 18),
    _REtherStatsPkts512to1023Octets_Type()
)
rEtherStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsPkts512to1023Octets.setStatus("mandatory")
_REtherStatsPkts1024to1518Octets_Type = Counter32
_REtherStatsPkts1024to1518Octets_Object = MibTableColumn
rEtherStatsPkts1024to1518Octets = _REtherStatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 19),
    _REtherStatsPkts1024to1518Octets_Type()
)
rEtherStatsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherStatsPkts1024to1518Octets.setStatus("mandatory")
_REtherStatsOwner_Type = OwnerString
_REtherStatsOwner_Object = MibTableColumn
rEtherStatsOwner = _REtherStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 20),
    _REtherStatsOwner_Type()
)
rEtherStatsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rEtherStatsOwner.setStatus("mandatory")
_REtherStatsStatus_Type = EntryStatus
_REtherStatsStatus_Object = MibTableColumn
rEtherStatsStatus = _REtherStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 1, 1, 1, 21),
    _REtherStatsStatus_Type()
)
rEtherStatsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rEtherStatsStatus.setStatus("mandatory")
_RHistory_ObjectIdentity = ObjectIdentity
rHistory = _RHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2)
)
_RHistoryControlTable_Object = MibTable
rHistoryControlTable = _RHistoryControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rHistoryControlTable.setStatus("mandatory")
_RHistoryControlEntry_Object = MibTableRow
rHistoryControlEntry = _RHistoryControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 1, 1)
)
rHistoryControlEntry.setIndexNames(
    (0, "GBNServiceRMON-MIB", "rHistoryControlIndex"),
)
if mibBuilder.loadTexts:
    rHistoryControlEntry.setStatus("mandatory")


class _RHistoryControlIndex_Type(Integer32):
    """Custom type rHistoryControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RHistoryControlIndex_Type.__name__ = "Integer32"
_RHistoryControlIndex_Object = MibTableColumn
rHistoryControlIndex = _RHistoryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 1, 1, 1),
    _RHistoryControlIndex_Type()
)
rHistoryControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rHistoryControlIndex.setStatus("mandatory")
_RHistoryControlDataSource_Type = ObjectIdentifier
_RHistoryControlDataSource_Object = MibTableColumn
rHistoryControlDataSource = _RHistoryControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 1, 1, 2),
    _RHistoryControlDataSource_Type()
)
rHistoryControlDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rHistoryControlDataSource.setStatus("mandatory")


class _RHistoryControlBucketsRequested_Type(Integer32):
    """Custom type rHistoryControlBucketsRequested based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RHistoryControlBucketsRequested_Type.__name__ = "Integer32"
_RHistoryControlBucketsRequested_Object = MibTableColumn
rHistoryControlBucketsRequested = _RHistoryControlBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 1, 1, 3),
    _RHistoryControlBucketsRequested_Type()
)
rHistoryControlBucketsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rHistoryControlBucketsRequested.setStatus("mandatory")


class _RHistoryControlBucketsGranted_Type(Integer32):
    """Custom type rHistoryControlBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RHistoryControlBucketsGranted_Type.__name__ = "Integer32"
_RHistoryControlBucketsGranted_Object = MibTableColumn
rHistoryControlBucketsGranted = _RHistoryControlBucketsGranted_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 1, 1, 4),
    _RHistoryControlBucketsGranted_Type()
)
rHistoryControlBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rHistoryControlBucketsGranted.setStatus("mandatory")


class _RHistoryControlInterval_Type(Integer32):
    """Custom type rHistoryControlInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RHistoryControlInterval_Type.__name__ = "Integer32"
_RHistoryControlInterval_Object = MibTableColumn
rHistoryControlInterval = _RHistoryControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 1, 1, 5),
    _RHistoryControlInterval_Type()
)
rHistoryControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rHistoryControlInterval.setStatus("mandatory")
_RHistoryControlOwner_Type = OwnerString
_RHistoryControlOwner_Object = MibTableColumn
rHistoryControlOwner = _RHistoryControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 1, 1, 6),
    _RHistoryControlOwner_Type()
)
rHistoryControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rHistoryControlOwner.setStatus("mandatory")
_RHistoryControlStatus_Type = EntryStatus
_RHistoryControlStatus_Object = MibTableColumn
rHistoryControlStatus = _RHistoryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 1, 1, 7),
    _RHistoryControlStatus_Type()
)
rHistoryControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rHistoryControlStatus.setStatus("mandatory")
_REtherHistoryTable_Object = MibTable
rEtherHistoryTable = _REtherHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    rEtherHistoryTable.setStatus("mandatory")
_REtherHistoryEntry_Object = MibTableRow
rEtherHistoryEntry = _REtherHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 2, 1)
)
rEtherHistoryEntry.setIndexNames(
    (0, "GBNServiceRMON-MIB", "rEtherHistoryIndex"),
    (0, "GBNServiceRMON-MIB", "rEtherHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    rEtherHistoryEntry.setStatus("mandatory")


class _REtherHistoryIndex_Type(Integer32):
    """Custom type rEtherHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_REtherHistoryIndex_Type.__name__ = "Integer32"
_REtherHistoryIndex_Object = MibTableColumn
rEtherHistoryIndex = _REtherHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 2, 1, 1),
    _REtherHistoryIndex_Type()
)
rEtherHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherHistoryIndex.setStatus("mandatory")


class _REtherHistorySampleIndex_Type(Integer32):
    """Custom type rEtherHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_REtherHistorySampleIndex_Type.__name__ = "Integer32"
_REtherHistorySampleIndex_Object = MibTableColumn
rEtherHistorySampleIndex = _REtherHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 2, 1, 2),
    _REtherHistorySampleIndex_Type()
)
rEtherHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherHistorySampleIndex.setStatus("mandatory")
_REtherHistoryIntervalStart_Type = TimeTicks
_REtherHistoryIntervalStart_Object = MibTableColumn
rEtherHistoryIntervalStart = _REtherHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 2, 1, 3),
    _REtherHistoryIntervalStart_Type()
)
rEtherHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherHistoryIntervalStart.setStatus("mandatory")
_REtherHistoryDropEvents_Type = Counter32
_REtherHistoryDropEvents_Object = MibTableColumn
rEtherHistoryDropEvents = _REtherHistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 2, 1, 4),
    _REtherHistoryDropEvents_Type()
)
rEtherHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherHistoryDropEvents.setStatus("mandatory")
_REtherHistoryOctets_Type = Counter32
_REtherHistoryOctets_Object = MibTableColumn
rEtherHistoryOctets = _REtherHistoryOctets_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 2, 1, 5),
    _REtherHistoryOctets_Type()
)
rEtherHistoryOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherHistoryOctets.setStatus("mandatory")
_REtherHistoryPkts_Type = Counter32
_REtherHistoryPkts_Object = MibTableColumn
rEtherHistoryPkts = _REtherHistoryPkts_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 2, 1, 6),
    _REtherHistoryPkts_Type()
)
rEtherHistoryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherHistoryPkts.setStatus("mandatory")
_REtherHistoryBroadcastPkts_Type = Counter32
_REtherHistoryBroadcastPkts_Object = MibTableColumn
rEtherHistoryBroadcastPkts = _REtherHistoryBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 2, 1, 7),
    _REtherHistoryBroadcastPkts_Type()
)
rEtherHistoryBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherHistoryBroadcastPkts.setStatus("mandatory")
_REtherHistoryMulticastPkts_Type = Counter32
_REtherHistoryMulticastPkts_Object = MibTableColumn
rEtherHistoryMulticastPkts = _REtherHistoryMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 2, 1, 8),
    _REtherHistoryMulticastPkts_Type()
)
rEtherHistoryMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherHistoryMulticastPkts.setStatus("mandatory")
_REtherHistoryCRCAlignErrors_Type = Counter32
_REtherHistoryCRCAlignErrors_Object = MibTableColumn
rEtherHistoryCRCAlignErrors = _REtherHistoryCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 2, 1, 9),
    _REtherHistoryCRCAlignErrors_Type()
)
rEtherHistoryCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherHistoryCRCAlignErrors.setStatus("mandatory")
_REtherHistoryUndersizePkts_Type = Counter32
_REtherHistoryUndersizePkts_Object = MibTableColumn
rEtherHistoryUndersizePkts = _REtherHistoryUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 2, 1, 10),
    _REtherHistoryUndersizePkts_Type()
)
rEtherHistoryUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherHistoryUndersizePkts.setStatus("mandatory")
_REtherHistoryOversizePkts_Type = Counter32
_REtherHistoryOversizePkts_Object = MibTableColumn
rEtherHistoryOversizePkts = _REtherHistoryOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 2, 1, 11),
    _REtherHistoryOversizePkts_Type()
)
rEtherHistoryOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherHistoryOversizePkts.setStatus("mandatory")
_REtherHistoryFragments_Type = Counter32
_REtherHistoryFragments_Object = MibTableColumn
rEtherHistoryFragments = _REtherHistoryFragments_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 2, 1, 12),
    _REtherHistoryFragments_Type()
)
rEtherHistoryFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherHistoryFragments.setStatus("mandatory")
_REtherHistoryJabbers_Type = Counter32
_REtherHistoryJabbers_Object = MibTableColumn
rEtherHistoryJabbers = _REtherHistoryJabbers_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 2, 1, 13),
    _REtherHistoryJabbers_Type()
)
rEtherHistoryJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherHistoryJabbers.setStatus("mandatory")
_REtherHistoryCollisions_Type = Counter32
_REtherHistoryCollisions_Object = MibTableColumn
rEtherHistoryCollisions = _REtherHistoryCollisions_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 2, 1, 14),
    _REtherHistoryCollisions_Type()
)
rEtherHistoryCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherHistoryCollisions.setStatus("mandatory")


class _REtherHistoryUtilization_Type(Integer32):
    """Custom type rEtherHistoryUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_REtherHistoryUtilization_Type.__name__ = "Integer32"
_REtherHistoryUtilization_Object = MibTableColumn
rEtherHistoryUtilization = _REtherHistoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 2, 2, 1, 15),
    _REtherHistoryUtilization_Type()
)
rEtherHistoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEtherHistoryUtilization.setStatus("mandatory")
_RAlarm_ObjectIdentity = ObjectIdentity
rAlarm = _RAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 3)
)
_RAlarmTable_Object = MibTable
rAlarmTable = _RAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    rAlarmTable.setStatus("mandatory")
_RAlarmEntry_Object = MibTableRow
rAlarmEntry = _RAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 3, 1, 1)
)
rAlarmEntry.setIndexNames(
    (0, "GBNServiceRMON-MIB", "rAlarmIndex"),
)
if mibBuilder.loadTexts:
    rAlarmEntry.setStatus("mandatory")


class _RAlarmIndex_Type(Integer32):
    """Custom type rAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RAlarmIndex_Type.__name__ = "Integer32"
_RAlarmIndex_Object = MibTableColumn
rAlarmIndex = _RAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 3, 1, 1, 1),
    _RAlarmIndex_Type()
)
rAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rAlarmIndex.setStatus("mandatory")
_RAlarmInterval_Type = Integer32
_RAlarmInterval_Object = MibTableColumn
rAlarmInterval = _RAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 3, 1, 1, 2),
    _RAlarmInterval_Type()
)
rAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAlarmInterval.setStatus("mandatory")
_RAlarmVariable_Type = ObjectIdentifier
_RAlarmVariable_Object = MibTableColumn
rAlarmVariable = _RAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 3, 1, 1, 3),
    _RAlarmVariable_Type()
)
rAlarmVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAlarmVariable.setStatus("mandatory")


class _RAlarmSampleType_Type(Integer32):
    """Custom type rAlarmSampleType based on Integer32"""
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


_RAlarmSampleType_Type.__name__ = "Integer32"
_RAlarmSampleType_Object = MibTableColumn
rAlarmSampleType = _RAlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 3, 1, 1, 4),
    _RAlarmSampleType_Type()
)
rAlarmSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAlarmSampleType.setStatus("mandatory")
_RAlarmValue_Type = Integer32
_RAlarmValue_Object = MibTableColumn
rAlarmValue = _RAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 3, 1, 1, 5),
    _RAlarmValue_Type()
)
rAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rAlarmValue.setStatus("mandatory")


class _RAlarmStartupAlarm_Type(Integer32):
    """Custom type rAlarmStartupAlarm based on Integer32"""
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


_RAlarmStartupAlarm_Type.__name__ = "Integer32"
_RAlarmStartupAlarm_Object = MibTableColumn
rAlarmStartupAlarm = _RAlarmStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 3, 1, 1, 6),
    _RAlarmStartupAlarm_Type()
)
rAlarmStartupAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAlarmStartupAlarm.setStatus("mandatory")
_RAlarmRisingThreshold_Type = Integer32
_RAlarmRisingThreshold_Object = MibTableColumn
rAlarmRisingThreshold = _RAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 3, 1, 1, 7),
    _RAlarmRisingThreshold_Type()
)
rAlarmRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAlarmRisingThreshold.setStatus("mandatory")
_RAlarmFallingThreshold_Type = Integer32
_RAlarmFallingThreshold_Object = MibTableColumn
rAlarmFallingThreshold = _RAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 3, 1, 1, 8),
    _RAlarmFallingThreshold_Type()
)
rAlarmFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAlarmFallingThreshold.setStatus("mandatory")


class _RAlarmRisingEventIndex_Type(Integer32):
    """Custom type rAlarmRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RAlarmRisingEventIndex_Type.__name__ = "Integer32"
_RAlarmRisingEventIndex_Object = MibTableColumn
rAlarmRisingEventIndex = _RAlarmRisingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 3, 1, 1, 9),
    _RAlarmRisingEventIndex_Type()
)
rAlarmRisingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAlarmRisingEventIndex.setStatus("mandatory")


class _RAlarmFallingEventIndex_Type(Integer32):
    """Custom type rAlarmFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RAlarmFallingEventIndex_Type.__name__ = "Integer32"
_RAlarmFallingEventIndex_Object = MibTableColumn
rAlarmFallingEventIndex = _RAlarmFallingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 3, 1, 1, 10),
    _RAlarmFallingEventIndex_Type()
)
rAlarmFallingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAlarmFallingEventIndex.setStatus("mandatory")
_RAlarmOwner_Type = OwnerString
_RAlarmOwner_Object = MibTableColumn
rAlarmOwner = _RAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 3, 1, 1, 11),
    _RAlarmOwner_Type()
)
rAlarmOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAlarmOwner.setStatus("mandatory")
_RAlarmStatus_Type = EntryStatus
_RAlarmStatus_Object = MibTableColumn
rAlarmStatus = _RAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 3, 1, 1, 12),
    _RAlarmStatus_Type()
)
rAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAlarmStatus.setStatus("mandatory")
_REvent_ObjectIdentity = ObjectIdentity
rEvent = _REvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 9)
)
_REventTable_Object = MibTable
rEventTable = _REventTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 9, 1)
)
if mibBuilder.loadTexts:
    rEventTable.setStatus("mandatory")
_REventEntry_Object = MibTableRow
rEventEntry = _REventEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 9, 1, 1)
)
rEventEntry.setIndexNames(
    (0, "GBNServiceRMON-MIB", "rEventIndex"),
)
if mibBuilder.loadTexts:
    rEventEntry.setStatus("mandatory")


class _REventIndex_Type(Integer32):
    """Custom type rEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_REventIndex_Type.__name__ = "Integer32"
_REventIndex_Object = MibTableColumn
rEventIndex = _REventIndex_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 9, 1, 1, 1),
    _REventIndex_Type()
)
rEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEventIndex.setStatus("mandatory")


class _REventDescription_Type(DisplayString):
    """Custom type rEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_REventDescription_Type.__name__ = "DisplayString"
_REventDescription_Object = MibTableColumn
rEventDescription = _REventDescription_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 9, 1, 1, 2),
    _REventDescription_Type()
)
rEventDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rEventDescription.setStatus("mandatory")


class _REventType_Type(Integer32):
    """Custom type rEventType based on Integer32"""
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


_REventType_Type.__name__ = "Integer32"
_REventType_Object = MibTableColumn
rEventType = _REventType_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 9, 1, 1, 3),
    _REventType_Type()
)
rEventType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rEventType.setStatus("mandatory")


class _REventCommunity_Type(OctetString):
    """Custom type rEventCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_REventCommunity_Type.__name__ = "OctetString"
_REventCommunity_Object = MibTableColumn
rEventCommunity = _REventCommunity_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 9, 1, 1, 4),
    _REventCommunity_Type()
)
rEventCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rEventCommunity.setStatus("mandatory")
_REventLastTimeSent_Type = TimeTicks
_REventLastTimeSent_Object = MibTableColumn
rEventLastTimeSent = _REventLastTimeSent_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 9, 1, 1, 5),
    _REventLastTimeSent_Type()
)
rEventLastTimeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rEventLastTimeSent.setStatus("mandatory")
_REventOwner_Type = OwnerString
_REventOwner_Object = MibTableColumn
rEventOwner = _REventOwner_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 9, 1, 1, 6),
    _REventOwner_Type()
)
rEventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rEventOwner.setStatus("mandatory")
_REventStatus_Type = EntryStatus
_REventStatus_Object = MibTableColumn
rEventStatus = _REventStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 9, 1, 1, 7),
    _REventStatus_Type()
)
rEventStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rEventStatus.setStatus("mandatory")
_RLogTable_Object = MibTable
rLogTable = _RLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 9, 2)
)
if mibBuilder.loadTexts:
    rLogTable.setStatus("mandatory")
_RLogEntry_Object = MibTableRow
rLogEntry = _RLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 9, 2, 1)
)
rLogEntry.setIndexNames(
    (0, "GBNServiceRMON-MIB", "rLogEventIndex"),
    (0, "GBNServiceRMON-MIB", "rLogIndex"),
)
if mibBuilder.loadTexts:
    rLogEntry.setStatus("mandatory")


class _RLogEventIndex_Type(Integer32):
    """Custom type rLogEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RLogEventIndex_Type.__name__ = "Integer32"
_RLogEventIndex_Object = MibTableColumn
rLogEventIndex = _RLogEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 9, 2, 1, 1),
    _RLogEventIndex_Type()
)
rLogEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLogEventIndex.setStatus("mandatory")


class _RLogIndex_Type(Integer32):
    """Custom type rLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RLogIndex_Type.__name__ = "Integer32"
_RLogIndex_Object = MibTableColumn
rLogIndex = _RLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 9, 2, 1, 2),
    _RLogIndex_Type()
)
rLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLogIndex.setStatus("mandatory")
_RLogTime_Type = TimeTicks
_RLogTime_Object = MibTableColumn
rLogTime = _RLogTime_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 9, 2, 1, 3),
    _RLogTime_Type()
)
rLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLogTime.setStatus("mandatory")


class _RLogDescription_Type(DisplayString):
    """Custom type rLogDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RLogDescription_Type.__name__ = "DisplayString"
_RLogDescription_Object = MibTableColumn
rLogDescription = _RLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 9, 2, 1, 4),
    _RLogDescription_Type()
)
rLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLogDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects

rRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 0, 1)
)
rRisingAlarm.setObjects(
      *(("GBNServiceRMON-MIB", "rAlarmIndex"),
        ("GBNServiceRMON-MIB", "rAlarmVariable"),
        ("GBNServiceRMON-MIB", "rAlarmSampleType"),
        ("GBNServiceRMON-MIB", "rAlarmValue"),
        ("GBNServiceRMON-MIB", "rAlarmRisingThreshold"))
)
if mibBuilder.loadTexts:
    rRisingAlarm.setStatus(
        ""
    )

rFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2, 0, 2)
)
rFallingAlarm.setObjects(
      *(("GBNServiceRMON-MIB", "rAlarmIndex"),
        ("GBNServiceRMON-MIB", "rAlarmVariable"),
        ("GBNServiceRMON-MIB", "rAlarmSampleType"),
        ("GBNServiceRMON-MIB", "rAlarmValue"),
        ("GBNServiceRMON-MIB", "rAlarmFallingThreshold"))
)
if mibBuilder.loadTexts:
    rFallingAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GBNServiceRMON-MIB",
    **{"OwnerString": OwnerString,
       "EntryStatus": EntryStatus,
       "rRisingAlarm": rRisingAlarm,
       "rFallingAlarm": rFallingAlarm,
       "rStatistics": rStatistics,
       "rEtherStatsTable": rEtherStatsTable,
       "rEtherStatsEntry": rEtherStatsEntry,
       "rEtherStatsIndex": rEtherStatsIndex,
       "rEtherStatsDataSource": rEtherStatsDataSource,
       "rEtherStatsDropEvents": rEtherStatsDropEvents,
       "rEtherStatsOctets": rEtherStatsOctets,
       "rEtherStatsPkts": rEtherStatsPkts,
       "rEtherStatsBroadcastPkts": rEtherStatsBroadcastPkts,
       "rEtherStatsMulticastPkts": rEtherStatsMulticastPkts,
       "rEtherStatsCRCAlignErrors": rEtherStatsCRCAlignErrors,
       "rEtherStatsUndersizePkts": rEtherStatsUndersizePkts,
       "rEtherStatsOversizePkts": rEtherStatsOversizePkts,
       "rEtherStatsFragments": rEtherStatsFragments,
       "rEtherStatsJabbers": rEtherStatsJabbers,
       "rEtherStatsCollisions": rEtherStatsCollisions,
       "rEtherStatsPkts64Octets": rEtherStatsPkts64Octets,
       "rEtherStatsPkts65to127Octets": rEtherStatsPkts65to127Octets,
       "rEtherStatsPkts128to255Octets": rEtherStatsPkts128to255Octets,
       "rEtherStatsPkts256to511Octets": rEtherStatsPkts256to511Octets,
       "rEtherStatsPkts512to1023Octets": rEtherStatsPkts512to1023Octets,
       "rEtherStatsPkts1024to1518Octets": rEtherStatsPkts1024to1518Octets,
       "rEtherStatsOwner": rEtherStatsOwner,
       "rEtherStatsStatus": rEtherStatsStatus,
       "rHistory": rHistory,
       "rHistoryControlTable": rHistoryControlTable,
       "rHistoryControlEntry": rHistoryControlEntry,
       "rHistoryControlIndex": rHistoryControlIndex,
       "rHistoryControlDataSource": rHistoryControlDataSource,
       "rHistoryControlBucketsRequested": rHistoryControlBucketsRequested,
       "rHistoryControlBucketsGranted": rHistoryControlBucketsGranted,
       "rHistoryControlInterval": rHistoryControlInterval,
       "rHistoryControlOwner": rHistoryControlOwner,
       "rHistoryControlStatus": rHistoryControlStatus,
       "rEtherHistoryTable": rEtherHistoryTable,
       "rEtherHistoryEntry": rEtherHistoryEntry,
       "rEtherHistoryIndex": rEtherHistoryIndex,
       "rEtherHistorySampleIndex": rEtherHistorySampleIndex,
       "rEtherHistoryIntervalStart": rEtherHistoryIntervalStart,
       "rEtherHistoryDropEvents": rEtherHistoryDropEvents,
       "rEtherHistoryOctets": rEtherHistoryOctets,
       "rEtherHistoryPkts": rEtherHistoryPkts,
       "rEtherHistoryBroadcastPkts": rEtherHistoryBroadcastPkts,
       "rEtherHistoryMulticastPkts": rEtherHistoryMulticastPkts,
       "rEtherHistoryCRCAlignErrors": rEtherHistoryCRCAlignErrors,
       "rEtherHistoryUndersizePkts": rEtherHistoryUndersizePkts,
       "rEtherHistoryOversizePkts": rEtherHistoryOversizePkts,
       "rEtherHistoryFragments": rEtherHistoryFragments,
       "rEtherHistoryJabbers": rEtherHistoryJabbers,
       "rEtherHistoryCollisions": rEtherHistoryCollisions,
       "rEtherHistoryUtilization": rEtherHistoryUtilization,
       "rAlarm": rAlarm,
       "rAlarmTable": rAlarmTable,
       "rAlarmEntry": rAlarmEntry,
       "rAlarmIndex": rAlarmIndex,
       "rAlarmInterval": rAlarmInterval,
       "rAlarmVariable": rAlarmVariable,
       "rAlarmSampleType": rAlarmSampleType,
       "rAlarmValue": rAlarmValue,
       "rAlarmStartupAlarm": rAlarmStartupAlarm,
       "rAlarmRisingThreshold": rAlarmRisingThreshold,
       "rAlarmFallingThreshold": rAlarmFallingThreshold,
       "rAlarmRisingEventIndex": rAlarmRisingEventIndex,
       "rAlarmFallingEventIndex": rAlarmFallingEventIndex,
       "rAlarmOwner": rAlarmOwner,
       "rAlarmStatus": rAlarmStatus,
       "rEvent": rEvent,
       "rEventTable": rEventTable,
       "rEventEntry": rEventEntry,
       "rEventIndex": rEventIndex,
       "rEventDescription": rEventDescription,
       "rEventType": rEventType,
       "rEventCommunity": rEventCommunity,
       "rEventLastTimeSent": rEventLastTimeSent,
       "rEventOwner": rEventOwner,
       "rEventStatus": rEventStatus,
       "rLogTable": rLogTable,
       "rLogEntry": rLogEntry,
       "rLogEventIndex": rLogEventIndex,
       "rLogIndex": rLogIndex,
       "rLogTime": rLogTime,
       "rLogDescription": rLogDescription}
)
