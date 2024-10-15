# SNMP MIB module (WANSTATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WANSTATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:30 2024
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

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

wanStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3)
)
_NetElement_ObjectIdentity = ObjectIdentity
netElement = _NetElement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7)
)
_Lanprobe_ObjectIdentity = ObjectIdentity
lanprobe = _Lanprobe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1)
)
_RmonExtension_ObjectIdentity = ObjectIdentity
rmonExtension = _RmonExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5)
)
_StatsExtension_ObjectIdentity = ObjectIdentity
statsExtension = _StatsExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1)
)
_WanStatsMIBObjects_ObjectIdentity = ObjectIdentity
wanStatsMIBObjects = _WanStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1)
)
_WanSignalingStats_ObjectIdentity = ObjectIdentity
wanSignalingStats = _WanSignalingStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1)
)
_WanT1E1StatsTable_Object = MibTable
wanT1E1StatsTable = _WanT1E1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wanT1E1StatsTable.setStatus("current")
_WanT1E1StatsEntry_Object = MibTableRow
wanT1E1StatsEntry = _WanT1E1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1)
)
wanT1E1StatsEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanT1E1StatsIndex"),
)
if mibBuilder.loadTexts:
    wanT1E1StatsEntry.setStatus("current")


class _WanT1E1StatsIndex_Type(Integer32):
    """Custom type wanT1E1StatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanT1E1StatsIndex_Type.__name__ = "Integer32"
_WanT1E1StatsIndex_Object = MibTableColumn
wanT1E1StatsIndex = _WanT1E1StatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 1),
    _WanT1E1StatsIndex_Type()
)
wanT1E1StatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanT1E1StatsIndex.setStatus("current")
_WanT1E1StatsDataSource_Type = ObjectIdentifier
_WanT1E1StatsDataSource_Object = MibTableColumn
wanT1E1StatsDataSource = _WanT1E1StatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 2),
    _WanT1E1StatsDataSource_Type()
)
wanT1E1StatsDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanT1E1StatsDataSource.setStatus("current")
_WanT1E1StatsDropEvents_Type = Counter64
_WanT1E1StatsDropEvents_Object = MibTableColumn
wanT1E1StatsDropEvents = _WanT1E1StatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 3),
    _WanT1E1StatsDropEvents_Type()
)
wanT1E1StatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsDropEvents.setStatus("current")
_WanT1E1StatsInFrames_Type = Counter64
_WanT1E1StatsInFrames_Object = MibTableColumn
wanT1E1StatsInFrames = _WanT1E1StatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 4),
    _WanT1E1StatsInFrames_Type()
)
wanT1E1StatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsInFrames.setStatus("current")
_WanT1E1StatsOutFrames_Type = Counter64
_WanT1E1StatsOutFrames_Object = MibTableColumn
wanT1E1StatsOutFrames = _WanT1E1StatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 5),
    _WanT1E1StatsOutFrames_Type()
)
wanT1E1StatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsOutFrames.setStatus("current")
_WanT1E1StatsInOctets_Type = Counter64
_WanT1E1StatsInOctets_Object = MibTableColumn
wanT1E1StatsInOctets = _WanT1E1StatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 6),
    _WanT1E1StatsInOctets_Type()
)
wanT1E1StatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsInOctets.setStatus("current")
_WanT1E1StatsOutOctets_Type = Counter64
_WanT1E1StatsOutOctets_Object = MibTableColumn
wanT1E1StatsOutOctets = _WanT1E1StatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 7),
    _WanT1E1StatsOutOctets_Type()
)
wanT1E1StatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsOutOctets.setStatus("current")
_WanT1E1StatsESs_Type = Counter64
_WanT1E1StatsESs_Object = MibTableColumn
wanT1E1StatsESs = _WanT1E1StatsESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 8),
    _WanT1E1StatsESs_Type()
)
wanT1E1StatsESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsESs.setStatus("current")
_WanT1E1StatsSESs_Type = Counter64
_WanT1E1StatsSESs_Object = MibTableColumn
wanT1E1StatsSESs = _WanT1E1StatsSESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 9),
    _WanT1E1StatsSESs_Type()
)
wanT1E1StatsSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsSESs.setStatus("current")
_WanT1E1StatsSEFSs_Type = Counter64
_WanT1E1StatsSEFSs_Object = MibTableColumn
wanT1E1StatsSEFSs = _WanT1E1StatsSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 10),
    _WanT1E1StatsSEFSs_Type()
)
wanT1E1StatsSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsSEFSs.setStatus("current")
_WanT1E1StatsOOFs_Type = Counter64
_WanT1E1StatsOOFs_Object = MibTableColumn
wanT1E1StatsOOFs = _WanT1E1StatsOOFs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 11),
    _WanT1E1StatsOOFs_Type()
)
wanT1E1StatsOOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsOOFs.setStatus("current")
_WanT1E1StatsUASs_Type = Counter64
_WanT1E1StatsUASs_Object = MibTableColumn
wanT1E1StatsUASs = _WanT1E1StatsUASs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 12),
    _WanT1E1StatsUASs_Type()
)
wanT1E1StatsUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsUASs.setStatus("current")
_WanT1E1StatsCSSs_Type = Counter64
_WanT1E1StatsCSSs_Object = MibTableColumn
wanT1E1StatsCSSs = _WanT1E1StatsCSSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 13),
    _WanT1E1StatsCSSs_Type()
)
wanT1E1StatsCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsCSSs.setStatus("current")
_WanT1E1StatsPCVs_Type = Counter64
_WanT1E1StatsPCVs_Object = MibTableColumn
wanT1E1StatsPCVs = _WanT1E1StatsPCVs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 14),
    _WanT1E1StatsPCVs_Type()
)
wanT1E1StatsPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsPCVs.setStatus("current")
_WanT1E1StatsLESs_Type = Counter64
_WanT1E1StatsLESs_Object = MibTableColumn
wanT1E1StatsLESs = _WanT1E1StatsLESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 15),
    _WanT1E1StatsLESs_Type()
)
wanT1E1StatsLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsLESs.setStatus("current")
_WanT1E1StatsBESs_Type = Counter64
_WanT1E1StatsBESs_Object = MibTableColumn
wanT1E1StatsBESs = _WanT1E1StatsBESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 16),
    _WanT1E1StatsBESs_Type()
)
wanT1E1StatsBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsBESs.setStatus("current")
_WanT1E1StatsDMs_Type = Counter64
_WanT1E1StatsDMs_Object = MibTableColumn
wanT1E1StatsDMs = _WanT1E1StatsDMs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 17),
    _WanT1E1StatsDMs_Type()
)
wanT1E1StatsDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsDMs.setStatus("current")
_WanT1E1StatsLCVs_Type = Counter64
_WanT1E1StatsLCVs_Object = MibTableColumn
wanT1E1StatsLCVs = _WanT1E1StatsLCVs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 18),
    _WanT1E1StatsLCVs_Type()
)
wanT1E1StatsLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsLCVs.setStatus("current")
_WanT1E1StatsLOFs_Type = Counter64
_WanT1E1StatsLOFs_Object = MibTableColumn
wanT1E1StatsLOFs = _WanT1E1StatsLOFs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 19),
    _WanT1E1StatsLOFs_Type()
)
wanT1E1StatsLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsLOFs.setStatus("current")
_WanT1E1StatsLOSs_Type = Counter64
_WanT1E1StatsLOSs_Object = MibTableColumn
wanT1E1StatsLOSs = _WanT1E1StatsLOSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 20),
    _WanT1E1StatsLOSs_Type()
)
wanT1E1StatsLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsLOSs.setStatus("current")
_WanT1E1StatsRAIs_Type = Counter64
_WanT1E1StatsRAIs_Object = MibTableColumn
wanT1E1StatsRAIs = _WanT1E1StatsRAIs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 21),
    _WanT1E1StatsRAIs_Type()
)
wanT1E1StatsRAIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsRAIs.setStatus("current")
_WanT1E1StatsAISs_Type = Counter64
_WanT1E1StatsAISs_Object = MibTableColumn
wanT1E1StatsAISs = _WanT1E1StatsAISs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 22),
    _WanT1E1StatsAISs_Type()
)
wanT1E1StatsAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsAISs.setStatus("current")
_WanT1E1StatsTS16AISs_Type = Counter64
_WanT1E1StatsTS16AISs_Object = MibTableColumn
wanT1E1StatsTS16AISs = _WanT1E1StatsTS16AISs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 23),
    _WanT1E1StatsTS16AISs_Type()
)
wanT1E1StatsTS16AISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsTS16AISs.setStatus("current")
_WanT1E1StatsLOMFs_Type = Counter64
_WanT1E1StatsLOMFs_Object = MibTableColumn
wanT1E1StatsLOMFs = _WanT1E1StatsLOMFs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 24),
    _WanT1E1StatsLOMFs_Type()
)
wanT1E1StatsLOMFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsLOMFs.setStatus("current")
_WanT1E1StatsFarLOMFs_Type = Counter64
_WanT1E1StatsFarLOMFs_Object = MibTableColumn
wanT1E1StatsFarLOMFs = _WanT1E1StatsFarLOMFs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 25),
    _WanT1E1StatsFarLOMFs_Type()
)
wanT1E1StatsFarLOMFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1StatsFarLOMFs.setStatus("current")
_WanT1E1StatsOwner_Type = OwnerString
_WanT1E1StatsOwner_Object = MibTableColumn
wanT1E1StatsOwner = _WanT1E1StatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 26),
    _WanT1E1StatsOwner_Type()
)
wanT1E1StatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanT1E1StatsOwner.setStatus("current")
_WanT1E1StatsStatus_Type = RowStatus
_WanT1E1StatsStatus_Object = MibTableColumn
wanT1E1StatsStatus = _WanT1E1StatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 1, 1, 27),
    _WanT1E1StatsStatus_Type()
)
wanT1E1StatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanT1E1StatsStatus.setStatus("current")
_WanVSeriesStatsTable_Object = MibTable
wanVSeriesStatsTable = _WanVSeriesStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wanVSeriesStatsTable.setStatus("current")
_WanVSeriesStatsEntry_Object = MibTableRow
wanVSeriesStatsEntry = _WanVSeriesStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2, 1)
)
wanVSeriesStatsEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanVSeriesStatsIndex"),
)
if mibBuilder.loadTexts:
    wanVSeriesStatsEntry.setStatus("current")


class _WanVSeriesStatsIndex_Type(Integer32):
    """Custom type wanVSeriesStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanVSeriesStatsIndex_Type.__name__ = "Integer32"
_WanVSeriesStatsIndex_Object = MibTableColumn
wanVSeriesStatsIndex = _WanVSeriesStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2, 1, 1),
    _WanVSeriesStatsIndex_Type()
)
wanVSeriesStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanVSeriesStatsIndex.setStatus("current")
_WanVSeriesStatsDataSource_Type = ObjectIdentifier
_WanVSeriesStatsDataSource_Object = MibTableColumn
wanVSeriesStatsDataSource = _WanVSeriesStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2, 1, 2),
    _WanVSeriesStatsDataSource_Type()
)
wanVSeriesStatsDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanVSeriesStatsDataSource.setStatus("current")
_WanVSeriesStatsDropEvents_Type = Counter64
_WanVSeriesStatsDropEvents_Object = MibTableColumn
wanVSeriesStatsDropEvents = _WanVSeriesStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2, 1, 3),
    _WanVSeriesStatsDropEvents_Type()
)
wanVSeriesStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesStatsDropEvents.setStatus("current")
_WanVSeriesStatsInFrames_Type = Counter64
_WanVSeriesStatsInFrames_Object = MibTableColumn
wanVSeriesStatsInFrames = _WanVSeriesStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2, 1, 4),
    _WanVSeriesStatsInFrames_Type()
)
wanVSeriesStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesStatsInFrames.setStatus("current")
_WanVSeriesStatsOutFrames_Type = Counter64
_WanVSeriesStatsOutFrames_Object = MibTableColumn
wanVSeriesStatsOutFrames = _WanVSeriesStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2, 1, 5),
    _WanVSeriesStatsOutFrames_Type()
)
wanVSeriesStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesStatsOutFrames.setStatus("current")
_WanVSeriesStatsInOctets_Type = Counter64
_WanVSeriesStatsInOctets_Object = MibTableColumn
wanVSeriesStatsInOctets = _WanVSeriesStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2, 1, 6),
    _WanVSeriesStatsInOctets_Type()
)
wanVSeriesStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesStatsInOctets.setStatus("current")
_WanVSeriesStatsOutOctets_Type = Counter64
_WanVSeriesStatsOutOctets_Object = MibTableColumn
wanVSeriesStatsOutOctets = _WanVSeriesStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2, 1, 7),
    _WanVSeriesStatsOutOctets_Type()
)
wanVSeriesStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesStatsOutOctets.setStatus("current")
_WanVSeriesStatsInFCSs_Type = Counter64
_WanVSeriesStatsInFCSs_Object = MibTableColumn
wanVSeriesStatsInFCSs = _WanVSeriesStatsInFCSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2, 1, 8),
    _WanVSeriesStatsInFCSs_Type()
)
wanVSeriesStatsInFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesStatsInFCSs.setStatus("current")
_WanVSeriesStatsOutFCSs_Type = Counter64
_WanVSeriesStatsOutFCSs_Object = MibTableColumn
wanVSeriesStatsOutFCSs = _WanVSeriesStatsOutFCSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2, 1, 9),
    _WanVSeriesStatsOutFCSs_Type()
)
wanVSeriesStatsOutFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesStatsOutFCSs.setStatus("current")
_WanVSeriesStatsInOverruns_Type = Counter64
_WanVSeriesStatsInOverruns_Object = MibTableColumn
wanVSeriesStatsInOverruns = _WanVSeriesStatsInOverruns_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2, 1, 10),
    _WanVSeriesStatsInOverruns_Type()
)
wanVSeriesStatsInOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesStatsInOverruns.setStatus("current")
_WanVSeriesStatsOutOverruns_Type = Counter64
_WanVSeriesStatsOutOverruns_Object = MibTableColumn
wanVSeriesStatsOutOverruns = _WanVSeriesStatsOutOverruns_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2, 1, 11),
    _WanVSeriesStatsOutOverruns_Type()
)
wanVSeriesStatsOutOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesStatsOutOverruns.setStatus("current")
_WanVSeriesStatsInterruptedFrames_Type = Counter64
_WanVSeriesStatsInterruptedFrames_Object = MibTableColumn
wanVSeriesStatsInterruptedFrames = _WanVSeriesStatsInterruptedFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2, 1, 12),
    _WanVSeriesStatsInterruptedFrames_Type()
)
wanVSeriesStatsInterruptedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesStatsInterruptedFrames.setStatus("current")
_WanVSeriesStatsInAbortedFrames_Type = Counter64
_WanVSeriesStatsInAbortedFrames_Object = MibTableColumn
wanVSeriesStatsInAbortedFrames = _WanVSeriesStatsInAbortedFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2, 1, 13),
    _WanVSeriesStatsInAbortedFrames_Type()
)
wanVSeriesStatsInAbortedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesStatsInAbortedFrames.setStatus("current")
_WanVSeriesStatsOutAbortedFrames_Type = Counter64
_WanVSeriesStatsOutAbortedFrames_Object = MibTableColumn
wanVSeriesStatsOutAbortedFrames = _WanVSeriesStatsOutAbortedFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2, 1, 14),
    _WanVSeriesStatsOutAbortedFrames_Type()
)
wanVSeriesStatsOutAbortedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesStatsOutAbortedFrames.setStatus("current")
_WanVSeriesStatsOwner_Type = OwnerString
_WanVSeriesStatsOwner_Object = MibTableColumn
wanVSeriesStatsOwner = _WanVSeriesStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2, 1, 15),
    _WanVSeriesStatsOwner_Type()
)
wanVSeriesStatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanVSeriesStatsOwner.setStatus("current")
_WanVSeriesStatsStatus_Type = RowStatus
_WanVSeriesStatsStatus_Object = MibTableColumn
wanVSeriesStatsStatus = _WanVSeriesStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 2, 1, 16),
    _WanVSeriesStatsStatus_Type()
)
wanVSeriesStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanVSeriesStatsStatus.setStatus("current")
_WanHssiStatsTable_Object = MibTable
wanHssiStatsTable = _WanHssiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wanHssiStatsTable.setStatus("deprecated")
_WanHssiStatsEntry_Object = MibTableRow
wanHssiStatsEntry = _WanHssiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1)
)
wanHssiStatsEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanHssiStatsIndex"),
)
if mibBuilder.loadTexts:
    wanHssiStatsEntry.setStatus("deprecated")


class _WanHssiStatsIndex_Type(Integer32):
    """Custom type wanHssiStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanHssiStatsIndex_Type.__name__ = "Integer32"
_WanHssiStatsIndex_Object = MibTableColumn
wanHssiStatsIndex = _WanHssiStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 1),
    _WanHssiStatsIndex_Type()
)
wanHssiStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanHssiStatsIndex.setStatus("deprecated")
_WanHssiStatsDataSource_Type = ObjectIdentifier
_WanHssiStatsDataSource_Object = MibTableColumn
wanHssiStatsDataSource = _WanHssiStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 2),
    _WanHssiStatsDataSource_Type()
)
wanHssiStatsDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanHssiStatsDataSource.setStatus("deprecated")
_WanHssiStatsDropEvents_Type = Counter64
_WanHssiStatsDropEvents_Object = MibTableColumn
wanHssiStatsDropEvents = _WanHssiStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 3),
    _WanHssiStatsDropEvents_Type()
)
wanHssiStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiStatsDropEvents.setStatus("deprecated")
_WanHssiStatsInFrames_Type = Counter64
_WanHssiStatsInFrames_Object = MibTableColumn
wanHssiStatsInFrames = _WanHssiStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 4),
    _WanHssiStatsInFrames_Type()
)
wanHssiStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiStatsInFrames.setStatus("deprecated")
_WanHssiStatsOutFrames_Type = Counter64
_WanHssiStatsOutFrames_Object = MibTableColumn
wanHssiStatsOutFrames = _WanHssiStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 5),
    _WanHssiStatsOutFrames_Type()
)
wanHssiStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiStatsOutFrames.setStatus("deprecated")
_WanHssiStatsInOctets_Type = Counter64
_WanHssiStatsInOctets_Object = MibTableColumn
wanHssiStatsInOctets = _WanHssiStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 6),
    _WanHssiStatsInOctets_Type()
)
wanHssiStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiStatsInOctets.setStatus("deprecated")
_WanHssiStatsOutOctets_Type = Counter64
_WanHssiStatsOutOctets_Object = MibTableColumn
wanHssiStatsOutOctets = _WanHssiStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 7),
    _WanHssiStatsOutOctets_Type()
)
wanHssiStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiStatsOutOctets.setStatus("deprecated")
_WanHssiStatsRxLongFrames_Type = Counter64
_WanHssiStatsRxLongFrames_Object = MibTableColumn
wanHssiStatsRxLongFrames = _WanHssiStatsRxLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 8),
    _WanHssiStatsRxLongFrames_Type()
)
wanHssiStatsRxLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiStatsRxLongFrames.setStatus("deprecated")
_WanHssiStatsRxCrcErrors_Type = Counter64
_WanHssiStatsRxCrcErrors_Object = MibTableColumn
wanHssiStatsRxCrcErrors = _WanHssiStatsRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 9),
    _WanHssiStatsRxCrcErrors_Type()
)
wanHssiStatsRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiStatsRxCrcErrors.setStatus("deprecated")
_WanHssiStatsRxOverruns_Type = Counter64
_WanHssiStatsRxOverruns_Object = MibTableColumn
wanHssiStatsRxOverruns = _WanHssiStatsRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 10),
    _WanHssiStatsRxOverruns_Type()
)
wanHssiStatsRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiStatsRxOverruns.setStatus("deprecated")
_WanHssiStatsRxAborts_Type = Counter64
_WanHssiStatsRxAborts_Object = MibTableColumn
wanHssiStatsRxAborts = _WanHssiStatsRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 11),
    _WanHssiStatsRxAborts_Type()
)
wanHssiStatsRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiStatsRxAborts.setStatus("deprecated")
_WanHssiStatsTxAborts_Type = Counter64
_WanHssiStatsTxAborts_Object = MibTableColumn
wanHssiStatsTxAborts = _WanHssiStatsTxAborts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 12),
    _WanHssiStatsTxAborts_Type()
)
wanHssiStatsTxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiStatsTxAborts.setStatus("deprecated")
_WanHssiStatsTxUnderruns_Type = Counter64
_WanHssiStatsTxUnderruns_Object = MibTableColumn
wanHssiStatsTxUnderruns = _WanHssiStatsTxUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 13),
    _WanHssiStatsTxUnderruns_Type()
)
wanHssiStatsTxUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiStatsTxUnderruns.setStatus("deprecated")
_WanHssiStatsRxRingErrors_Type = Counter64
_WanHssiStatsRxRingErrors_Object = MibTableColumn
wanHssiStatsRxRingErrors = _WanHssiStatsRxRingErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 14),
    _WanHssiStatsRxRingErrors_Type()
)
wanHssiStatsRxRingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiStatsRxRingErrors.setStatus("deprecated")
_WanHssiStatsRxRingOverruns_Type = Counter64
_WanHssiStatsRxRingOverruns_Object = MibTableColumn
wanHssiStatsRxRingOverruns = _WanHssiStatsRxRingOverruns_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 15),
    _WanHssiStatsRxRingOverruns_Type()
)
wanHssiStatsRxRingOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiStatsRxRingOverruns.setStatus("deprecated")
_WanHssiStatsTxRingErrors_Type = Counter64
_WanHssiStatsTxRingErrors_Object = MibTableColumn
wanHssiStatsTxRingErrors = _WanHssiStatsTxRingErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 16),
    _WanHssiStatsTxRingErrors_Type()
)
wanHssiStatsTxRingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiStatsTxRingErrors.setStatus("deprecated")
_WanHssiStatsPortOpErrors_Type = Counter64
_WanHssiStatsPortOpErrors_Object = MibTableColumn
wanHssiStatsPortOpErrors = _WanHssiStatsPortOpErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 17),
    _WanHssiStatsPortOpErrors_Type()
)
wanHssiStatsPortOpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiStatsPortOpErrors.setStatus("deprecated")
_WanHssiStatsTxCmplProcessings_Type = Counter64
_WanHssiStatsTxCmplProcessings_Object = MibTableColumn
wanHssiStatsTxCmplProcessings = _WanHssiStatsTxCmplProcessings_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 18),
    _WanHssiStatsTxCmplProcessings_Type()
)
wanHssiStatsTxCmplProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiStatsTxCmplProcessings.setStatus("deprecated")
_WanHssiStatsOwner_Type = OwnerString
_WanHssiStatsOwner_Object = MibTableColumn
wanHssiStatsOwner = _WanHssiStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 19),
    _WanHssiStatsOwner_Type()
)
wanHssiStatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanHssiStatsOwner.setStatus("deprecated")
_WanHssiStatsStatus_Type = RowStatus
_WanHssiStatsStatus_Object = MibTableColumn
wanHssiStatsStatus = _WanHssiStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 3, 1, 20),
    _WanHssiStatsStatus_Type()
)
wanHssiStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanHssiStatsStatus.setStatus("deprecated")
_WanT3E3StatsTable_Object = MibTable
wanT3E3StatsTable = _WanT3E3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wanT3E3StatsTable.setStatus("current")
_WanT3E3StatsEntry_Object = MibTableRow
wanT3E3StatsEntry = _WanT3E3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1)
)
wanT3E3StatsEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanT3E3StatsIndex"),
)
if mibBuilder.loadTexts:
    wanT3E3StatsEntry.setStatus("current")


class _WanT3E3StatsIndex_Type(Integer32):
    """Custom type wanT3E3StatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanT3E3StatsIndex_Type.__name__ = "Integer32"
_WanT3E3StatsIndex_Object = MibTableColumn
wanT3E3StatsIndex = _WanT3E3StatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 1),
    _WanT3E3StatsIndex_Type()
)
wanT3E3StatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanT3E3StatsIndex.setStatus("current")
_WanT3E3StatsDataSource_Type = ObjectIdentifier
_WanT3E3StatsDataSource_Object = MibTableColumn
wanT3E3StatsDataSource = _WanT3E3StatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 2),
    _WanT3E3StatsDataSource_Type()
)
wanT3E3StatsDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanT3E3StatsDataSource.setStatus("current")
_WanT3E3StatsDropEvents_Type = Counter64
_WanT3E3StatsDropEvents_Object = MibTableColumn
wanT3E3StatsDropEvents = _WanT3E3StatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 3),
    _WanT3E3StatsDropEvents_Type()
)
wanT3E3StatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsDropEvents.setStatus("current")
_WanT3E3StatsInFrames_Type = Counter64
_WanT3E3StatsInFrames_Object = MibTableColumn
wanT3E3StatsInFrames = _WanT3E3StatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 4),
    _WanT3E3StatsInFrames_Type()
)
wanT3E3StatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsInFrames.setStatus("current")
_WanT3E3StatsOutFrames_Type = Counter64
_WanT3E3StatsOutFrames_Object = MibTableColumn
wanT3E3StatsOutFrames = _WanT3E3StatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 5),
    _WanT3E3StatsOutFrames_Type()
)
wanT3E3StatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsOutFrames.setStatus("current")
_WanT3E3StatsInOctets_Type = Counter64
_WanT3E3StatsInOctets_Object = MibTableColumn
wanT3E3StatsInOctets = _WanT3E3StatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 6),
    _WanT3E3StatsInOctets_Type()
)
wanT3E3StatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsInOctets.setStatus("current")
_WanT3E3StatsOutOctets_Type = Counter64
_WanT3E3StatsOutOctets_Object = MibTableColumn
wanT3E3StatsOutOctets = _WanT3E3StatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 7),
    _WanT3E3StatsOutOctets_Type()
)
wanT3E3StatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsOutOctets.setStatus("current")
_WanT3E3StatsPESs_Type = Counter64
_WanT3E3StatsPESs_Object = MibTableColumn
wanT3E3StatsPESs = _WanT3E3StatsPESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 8),
    _WanT3E3StatsPESs_Type()
)
wanT3E3StatsPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsPESs.setStatus("current")
_WanT3E3StatsPSESs_Type = Counter64
_WanT3E3StatsPSESs_Object = MibTableColumn
wanT3E3StatsPSESs = _WanT3E3StatsPSESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 9),
    _WanT3E3StatsPSESs_Type()
)
wanT3E3StatsPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsPSESs.setStatus("current")
_WanT3E3StatsOOFs_Type = Counter64
_WanT3E3StatsOOFs_Object = MibTableColumn
wanT3E3StatsOOFs = _WanT3E3StatsOOFs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 10),
    _WanT3E3StatsOOFs_Type()
)
wanT3E3StatsOOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsOOFs.setStatus("current")
_WanT3E3StatsSEFSs_Type = Counter64
_WanT3E3StatsSEFSs_Object = MibTableColumn
wanT3E3StatsSEFSs = _WanT3E3StatsSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 11),
    _WanT3E3StatsSEFSs_Type()
)
wanT3E3StatsSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsSEFSs.setStatus("current")
_WanT3E3StatsUASs_Type = Counter64
_WanT3E3StatsUASs_Object = MibTableColumn
wanT3E3StatsUASs = _WanT3E3StatsUASs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 12),
    _WanT3E3StatsUASs_Type()
)
wanT3E3StatsUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsUASs.setStatus("current")
_WanT3E3StatsLCVs_Type = Counter64
_WanT3E3StatsLCVs_Object = MibTableColumn
wanT3E3StatsLCVs = _WanT3E3StatsLCVs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 13),
    _WanT3E3StatsLCVs_Type()
)
wanT3E3StatsLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsLCVs.setStatus("current")
_WanT3E3StatsPCVs_Type = Counter64
_WanT3E3StatsPCVs_Object = MibTableColumn
wanT3E3StatsPCVs = _WanT3E3StatsPCVs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 14),
    _WanT3E3StatsPCVs_Type()
)
wanT3E3StatsPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsPCVs.setStatus("current")
_WanT3E3StatsLESs_Type = Counter64
_WanT3E3StatsLESs_Object = MibTableColumn
wanT3E3StatsLESs = _WanT3E3StatsLESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 15),
    _WanT3E3StatsLESs_Type()
)
wanT3E3StatsLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsLESs.setStatus("current")
_WanT3E3StatsCCVs_Type = Counter64
_WanT3E3StatsCCVs_Object = MibTableColumn
wanT3E3StatsCCVs = _WanT3E3StatsCCVs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 16),
    _WanT3E3StatsCCVs_Type()
)
wanT3E3StatsCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsCCVs.setStatus("current")
_WanT3E3StatsCESs_Type = Counter64
_WanT3E3StatsCESs_Object = MibTableColumn
wanT3E3StatsCESs = _WanT3E3StatsCESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 17),
    _WanT3E3StatsCESs_Type()
)
wanT3E3StatsCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsCESs.setStatus("current")
_WanT3E3StatsCSESs_Type = Counter64
_WanT3E3StatsCSESs_Object = MibTableColumn
wanT3E3StatsCSESs = _WanT3E3StatsCSESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 18),
    _WanT3E3StatsCSESs_Type()
)
wanT3E3StatsCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsCSESs.setStatus("current")
_WanT3E3StatsRAIs_Type = Counter64
_WanT3E3StatsRAIs_Object = MibTableColumn
wanT3E3StatsRAIs = _WanT3E3StatsRAIs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 19),
    _WanT3E3StatsRAIs_Type()
)
wanT3E3StatsRAIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsRAIs.setStatus("current")
_WanT3E3StatsAISs_Type = Counter64
_WanT3E3StatsAISs_Object = MibTableColumn
wanT3E3StatsAISs = _WanT3E3StatsAISs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 20),
    _WanT3E3StatsAISs_Type()
)
wanT3E3StatsAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsAISs.setStatus("current")
_WanT3E3StatsLOFs_Type = Counter64
_WanT3E3StatsLOFs_Object = MibTableColumn
wanT3E3StatsLOFs = _WanT3E3StatsLOFs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 21),
    _WanT3E3StatsLOFs_Type()
)
wanT3E3StatsLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsLOFs.setStatus("current")
_WanT3E3StatsLOSs_Type = Counter64
_WanT3E3StatsLOSs_Object = MibTableColumn
wanT3E3StatsLOSs = _WanT3E3StatsLOSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 22),
    _WanT3E3StatsLOSs_Type()
)
wanT3E3StatsLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3StatsLOSs.setStatus("current")
_WanT3E3StatsOwner_Type = OwnerString
_WanT3E3StatsOwner_Object = MibTableColumn
wanT3E3StatsOwner = _WanT3E3StatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 23),
    _WanT3E3StatsOwner_Type()
)
wanT3E3StatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanT3E3StatsOwner.setStatus("current")
_WanT3E3StatsStatus_Type = RowStatus
_WanT3E3StatsStatus_Object = MibTableColumn
wanT3E3StatsStatus = _WanT3E3StatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 4, 1, 24),
    _WanT3E3StatsStatus_Type()
)
wanT3E3StatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanT3E3StatsStatus.setStatus("current")
_WanAtmStatsTable_Object = MibTable
wanAtmStatsTable = _WanAtmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wanAtmStatsTable.setStatus("current")
_WanAtmStatsEntry_Object = MibTableRow
wanAtmStatsEntry = _WanAtmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1)
)
wanAtmStatsEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanAtmStatsIndex"),
)
if mibBuilder.loadTexts:
    wanAtmStatsEntry.setStatus("current")


class _WanAtmStatsIndex_Type(Integer32):
    """Custom type wanAtmStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanAtmStatsIndex_Type.__name__ = "Integer32"
_WanAtmStatsIndex_Object = MibTableColumn
wanAtmStatsIndex = _WanAtmStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 1),
    _WanAtmStatsIndex_Type()
)
wanAtmStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanAtmStatsIndex.setStatus("current")
_WanAtmStatsDataSource_Type = ObjectIdentifier
_WanAtmStatsDataSource_Object = MibTableColumn
wanAtmStatsDataSource = _WanAtmStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 2),
    _WanAtmStatsDataSource_Type()
)
wanAtmStatsDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanAtmStatsDataSource.setStatus("current")
_WanAtmStatsDropEvents_Type = Counter64
_WanAtmStatsDropEvents_Object = MibTableColumn
wanAtmStatsDropEvents = _WanAtmStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 3),
    _WanAtmStatsDropEvents_Type()
)
wanAtmStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsDropEvents.setStatus("current")
_WanAtmStatsInCells_Type = Counter64
_WanAtmStatsInCells_Object = MibTableColumn
wanAtmStatsInCells = _WanAtmStatsInCells_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 4),
    _WanAtmStatsInCells_Type()
)
wanAtmStatsInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsInCells.setStatus("current")
_WanAtmStatsOutCells_Type = Counter64
_WanAtmStatsOutCells_Object = MibTableColumn
wanAtmStatsOutCells = _WanAtmStatsOutCells_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 5),
    _WanAtmStatsOutCells_Type()
)
wanAtmStatsOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsOutCells.setStatus("current")
_WanAtmStatsInCLP1_Type = Counter64
_WanAtmStatsInCLP1_Object = MibTableColumn
wanAtmStatsInCLP1 = _WanAtmStatsInCLP1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 6),
    _WanAtmStatsInCLP1_Type()
)
wanAtmStatsInCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsInCLP1.setStatus("current")
_WanAtmStatsOutCLP1_Type = Counter64
_WanAtmStatsOutCLP1_Object = MibTableColumn
wanAtmStatsOutCLP1 = _WanAtmStatsOutCLP1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 7),
    _WanAtmStatsOutCLP1_Type()
)
wanAtmStatsOutCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsOutCLP1.setStatus("current")
_WanAtmStatsConnectionEvents_Type = Counter64
_WanAtmStatsConnectionEvents_Object = MibTableColumn
wanAtmStatsConnectionEvents = _WanAtmStatsConnectionEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 8),
    _WanAtmStatsConnectionEvents_Type()
)
wanAtmStatsConnectionEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsConnectionEvents.setStatus("current")
_WanAtmStatsErroredPDUs_Type = Counter64
_WanAtmStatsErroredPDUs_Object = MibTableColumn
wanAtmStatsErroredPDUs = _WanAtmStatsErroredPDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 9),
    _WanAtmStatsErroredPDUs_Type()
)
wanAtmStatsErroredPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsErroredPDUs.setStatus("current")
_WanAtmStatsSetupAttempts_Type = Counter64
_WanAtmStatsSetupAttempts_Object = MibTableColumn
wanAtmStatsSetupAttempts = _WanAtmStatsSetupAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 10),
    _WanAtmStatsSetupAttempts_Type()
)
wanAtmStatsSetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsSetupAttempts.setStatus("current")
_WanAtmStatsInRoutesUnavailable_Type = Counter64
_WanAtmStatsInRoutesUnavailable_Object = MibTableColumn
wanAtmStatsInRoutesUnavailable = _WanAtmStatsInRoutesUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 11),
    _WanAtmStatsInRoutesUnavailable_Type()
)
wanAtmStatsInRoutesUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsInRoutesUnavailable.setStatus("current")
_WanAtmStatsOutRoutesUnavailable_Type = Counter64
_WanAtmStatsOutRoutesUnavailable_Object = MibTableColumn
wanAtmStatsOutRoutesUnavailable = _WanAtmStatsOutRoutesUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 12),
    _WanAtmStatsOutRoutesUnavailable_Type()
)
wanAtmStatsOutRoutesUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsOutRoutesUnavailable.setStatus("current")
_WanAtmStatsInResourcesUnavailable_Type = Counter64
_WanAtmStatsInResourcesUnavailable_Object = MibTableColumn
wanAtmStatsInResourcesUnavailable = _WanAtmStatsInResourcesUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 13),
    _WanAtmStatsInResourcesUnavailable_Type()
)
wanAtmStatsInResourcesUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsInResourcesUnavailable.setStatus("current")
_WanAtmStatsOutResourcesUnavailable_Type = Counter64
_WanAtmStatsOutResourcesUnavailable_Object = MibTableColumn
wanAtmStatsOutResourcesUnavailable = _WanAtmStatsOutResourcesUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 14),
    _WanAtmStatsOutResourcesUnavailable_Type()
)
wanAtmStatsOutResourcesUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsOutResourcesUnavailable.setStatus("current")
_WanAtmStatsInUnsuccessfulCalls_Type = Counter64
_WanAtmStatsInUnsuccessfulCalls_Object = MibTableColumn
wanAtmStatsInUnsuccessfulCalls = _WanAtmStatsInUnsuccessfulCalls_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 15),
    _WanAtmStatsInUnsuccessfulCalls_Type()
)
wanAtmStatsInUnsuccessfulCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsInUnsuccessfulCalls.setStatus("current")
_WanAtmStatsOutUnsuccessfulCalls_Type = Counter64
_WanAtmStatsOutUnsuccessfulCalls_Object = MibTableColumn
wanAtmStatsOutUnsuccessfulCalls = _WanAtmStatsOutUnsuccessfulCalls_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 16),
    _WanAtmStatsOutUnsuccessfulCalls_Type()
)
wanAtmStatsOutUnsuccessfulCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsOutUnsuccessfulCalls.setStatus("current")
_WanAtmStatsInIncorrectMsgs_Type = Counter64
_WanAtmStatsInIncorrectMsgs_Object = MibTableColumn
wanAtmStatsInIncorrectMsgs = _WanAtmStatsInIncorrectMsgs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 17),
    _WanAtmStatsInIncorrectMsgs_Type()
)
wanAtmStatsInIncorrectMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsInIncorrectMsgs.setStatus("current")
_WanAtmStatsOutIncorrectMsgs_Type = Counter64
_WanAtmStatsOutIncorrectMsgs_Object = MibTableColumn
wanAtmStatsOutIncorrectMsgs = _WanAtmStatsOutIncorrectMsgs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 18),
    _WanAtmStatsOutIncorrectMsgs_Type()
)
wanAtmStatsOutIncorrectMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsOutIncorrectMsgs.setStatus("current")
_WanAtmStatsInPartyEvents_Type = Counter64
_WanAtmStatsInPartyEvents_Object = MibTableColumn
wanAtmStatsInPartyEvents = _WanAtmStatsInPartyEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 19),
    _WanAtmStatsInPartyEvents_Type()
)
wanAtmStatsInPartyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsInPartyEvents.setStatus("current")
_WanAtmStatsOutPartyEvents_Type = Counter64
_WanAtmStatsOutPartyEvents_Object = MibTableColumn
wanAtmStatsOutPartyEvents = _WanAtmStatsOutPartyEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 20),
    _WanAtmStatsOutPartyEvents_Type()
)
wanAtmStatsOutPartyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsOutPartyEvents.setStatus("current")
_WanAtmStatsInExpiries_Type = Counter64
_WanAtmStatsInExpiries_Object = MibTableColumn
wanAtmStatsInExpiries = _WanAtmStatsInExpiries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 21),
    _WanAtmStatsInExpiries_Type()
)
wanAtmStatsInExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsInExpiries.setStatus("current")
_WanAtmStatsOutExpiries_Type = Counter64
_WanAtmStatsOutExpiries_Object = MibTableColumn
wanAtmStatsOutExpiries = _WanAtmStatsOutExpiries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 22),
    _WanAtmStatsOutExpiries_Type()
)
wanAtmStatsOutExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsOutExpiries.setStatus("current")
_WanAtmStatsInRestartErrors_Type = Counter64
_WanAtmStatsInRestartErrors_Object = MibTableColumn
wanAtmStatsInRestartErrors = _WanAtmStatsInRestartErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 23),
    _WanAtmStatsInRestartErrors_Type()
)
wanAtmStatsInRestartErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsInRestartErrors.setStatus("current")
_WanAtmStatsOutRestartErrors_Type = Counter64
_WanAtmStatsOutRestartErrors_Object = MibTableColumn
wanAtmStatsOutRestartErrors = _WanAtmStatsOutRestartErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 24),
    _WanAtmStatsOutRestartErrors_Type()
)
wanAtmStatsOutRestartErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsOutRestartErrors.setStatus("current")
_WanAtmStatsInSVCs_Type = Counter64
_WanAtmStatsInSVCs_Object = MibTableColumn
wanAtmStatsInSVCs = _WanAtmStatsInSVCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 25),
    _WanAtmStatsInSVCs_Type()
)
wanAtmStatsInSVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsInSVCs.setStatus("current")
_WanAtmStatsOutSVCs_Type = Counter64
_WanAtmStatsOutSVCs_Object = MibTableColumn
wanAtmStatsOutSVCs = _WanAtmStatsOutSVCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 26),
    _WanAtmStatsOutSVCs_Type()
)
wanAtmStatsOutSVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsOutSVCs.setStatus("current")
_WanAtmStatsInOCDs_Type = Counter64
_WanAtmStatsInOCDs_Object = MibTableColumn
wanAtmStatsInOCDs = _WanAtmStatsInOCDs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 27),
    _WanAtmStatsInOCDs_Type()
)
wanAtmStatsInOCDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsInOCDs.setStatus("current")
_WanAtmStatsOutOCDs_Type = Counter64
_WanAtmStatsOutOCDs_Object = MibTableColumn
wanAtmStatsOutOCDs = _WanAtmStatsOutOCDs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 28),
    _WanAtmStatsOutOCDs_Type()
)
wanAtmStatsOutOCDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsOutOCDs.setStatus("current")
_WanAtmStatsInLOCs_Type = Counter64
_WanAtmStatsInLOCs_Object = MibTableColumn
wanAtmStatsInLOCs = _WanAtmStatsInLOCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 29),
    _WanAtmStatsInLOCs_Type()
)
wanAtmStatsInLOCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsInLOCs.setStatus("current")
_WanAtmStatsOutLOCs_Type = Counter64
_WanAtmStatsOutLOCs_Object = MibTableColumn
wanAtmStatsOutLOCs = _WanAtmStatsOutLOCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 30),
    _WanAtmStatsOutLOCs_Type()
)
wanAtmStatsOutLOCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsOutLOCs.setStatus("current")
_WanAtmStatsInLOFs_Type = Counter64
_WanAtmStatsInLOFs_Object = MibTableColumn
wanAtmStatsInLOFs = _WanAtmStatsInLOFs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 31),
    _WanAtmStatsInLOFs_Type()
)
wanAtmStatsInLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsInLOFs.setStatus("current")
_WanAtmStatsOutLOFs_Type = Counter64
_WanAtmStatsOutLOFs_Object = MibTableColumn
wanAtmStatsOutLOFs = _WanAtmStatsOutLOFs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 32),
    _WanAtmStatsOutLOFs_Type()
)
wanAtmStatsOutLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsOutLOFs.setStatus("current")
_WanAtmStatsInLOPs_Type = Counter64
_WanAtmStatsInLOPs_Object = MibTableColumn
wanAtmStatsInLOPs = _WanAtmStatsInLOPs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 33),
    _WanAtmStatsInLOPs_Type()
)
wanAtmStatsInLOPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsInLOPs.setStatus("current")
_WanAtmStatsOutLOPs_Type = Counter64
_WanAtmStatsOutLOPs_Object = MibTableColumn
wanAtmStatsOutLOPs = _WanAtmStatsOutLOPs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 34),
    _WanAtmStatsOutLOPs_Type()
)
wanAtmStatsOutLOPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsOutLOPs.setStatus("current")
_WanAtmStatsInLOSs_Type = Counter64
_WanAtmStatsInLOSs_Object = MibTableColumn
wanAtmStatsInLOSs = _WanAtmStatsInLOSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 35),
    _WanAtmStatsInLOSs_Type()
)
wanAtmStatsInLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsInLOSs.setStatus("current")
_WanAtmStatsOutLOSs_Type = Counter64
_WanAtmStatsOutLOSs_Object = MibTableColumn
wanAtmStatsOutLOSs = _WanAtmStatsOutLOSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 36),
    _WanAtmStatsOutLOSs_Type()
)
wanAtmStatsOutLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmStatsOutLOSs.setStatus("current")
_WanAtmStatsOwner_Type = OwnerString
_WanAtmStatsOwner_Object = MibTableColumn
wanAtmStatsOwner = _WanAtmStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 37),
    _WanAtmStatsOwner_Type()
)
wanAtmStatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanAtmStatsOwner.setStatus("current")
_WanAtmStatsStatus_Type = RowStatus
_WanAtmStatsStatus_Object = MibTableColumn
wanAtmStatsStatus = _WanAtmStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 1, 5, 1, 38),
    _WanAtmStatsStatus_Type()
)
wanAtmStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanAtmStatsStatus.setStatus("current")
_WanProtocolStats_ObjectIdentity = ObjectIdentity
wanProtocolStats = _WanProtocolStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2)
)
_WanX25StatsTable_Object = MibTable
wanX25StatsTable = _WanX25StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wanX25StatsTable.setStatus("current")
_WanX25StatsEntry_Object = MibTableRow
wanX25StatsEntry = _WanX25StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1)
)
wanX25StatsEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanX25StatsIndex"),
)
if mibBuilder.loadTexts:
    wanX25StatsEntry.setStatus("current")


class _WanX25StatsIndex_Type(Integer32):
    """Custom type wanX25StatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanX25StatsIndex_Type.__name__ = "Integer32"
_WanX25StatsIndex_Object = MibTableColumn
wanX25StatsIndex = _WanX25StatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 1),
    _WanX25StatsIndex_Type()
)
wanX25StatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanX25StatsIndex.setStatus("current")
_WanX25StatsDataSource_Type = ObjectIdentifier
_WanX25StatsDataSource_Object = MibTableColumn
wanX25StatsDataSource = _WanX25StatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 2),
    _WanX25StatsDataSource_Type()
)
wanX25StatsDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanX25StatsDataSource.setStatus("current")
_WanX25StatsDropEvents_Type = Counter64
_WanX25StatsDropEvents_Object = MibTableColumn
wanX25StatsDropEvents = _WanX25StatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 3),
    _WanX25StatsDropEvents_Type()
)
wanX25StatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsDropEvents.setStatus("current")
_WanX25StatsInFrames_Type = Counter64
_WanX25StatsInFrames_Object = MibTableColumn
wanX25StatsInFrames = _WanX25StatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 4),
    _WanX25StatsInFrames_Type()
)
wanX25StatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsInFrames.setStatus("current")
_WanX25StatsOutFrames_Type = Counter64
_WanX25StatsOutFrames_Object = MibTableColumn
wanX25StatsOutFrames = _WanX25StatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 5),
    _WanX25StatsOutFrames_Type()
)
wanX25StatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsOutFrames.setStatus("current")
_WanX25StatsInOctets_Type = Counter64
_WanX25StatsInOctets_Object = MibTableColumn
wanX25StatsInOctets = _WanX25StatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 6),
    _WanX25StatsInOctets_Type()
)
wanX25StatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsInOctets.setStatus("current")
_WanX25StatsOutOctets_Type = Counter64
_WanX25StatsOutOctets_Object = MibTableColumn
wanX25StatsOutOctets = _WanX25StatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 7),
    _WanX25StatsOutOctets_Type()
)
wanX25StatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsOutOctets.setStatus("current")
_WanX25StatsInRejects_Type = Counter64
_WanX25StatsInRejects_Object = MibTableColumn
wanX25StatsInRejects = _WanX25StatsInRejects_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 8),
    _WanX25StatsInRejects_Type()
)
wanX25StatsInRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsInRejects.setStatus("current")
_WanX25StatsOutRejects_Type = Counter64
_WanX25StatsOutRejects_Object = MibTableColumn
wanX25StatsOutRejects = _WanX25StatsOutRejects_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 9),
    _WanX25StatsOutRejects_Type()
)
wanX25StatsOutRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsOutRejects.setStatus("current")
_WanX25StatsInAttempts_Type = Counter64
_WanX25StatsInAttempts_Object = MibTableColumn
wanX25StatsInAttempts = _WanX25StatsInAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 10),
    _WanX25StatsInAttempts_Type()
)
wanX25StatsInAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsInAttempts.setStatus("current")
_WanX25StatsOutAttempts_Type = Counter64
_WanX25StatsOutAttempts_Object = MibTableColumn
wanX25StatsOutAttempts = _WanX25StatsOutAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 11),
    _WanX25StatsOutAttempts_Type()
)
wanX25StatsOutAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsOutAttempts.setStatus("current")
_WanX25StatsInFailures_Type = Counter64
_WanX25StatsInFailures_Object = MibTableColumn
wanX25StatsInFailures = _WanX25StatsInFailures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 12),
    _WanX25StatsInFailures_Type()
)
wanX25StatsInFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsInFailures.setStatus("current")
_WanX25StatsOutFailures_Type = Counter64
_WanX25StatsOutFailures_Object = MibTableColumn
wanX25StatsOutFailures = _WanX25StatsOutFailures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 13),
    _WanX25StatsOutFailures_Type()
)
wanX25StatsOutFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsOutFailures.setStatus("current")
_WanX25StatsProviderClears_Type = Counter64
_WanX25StatsProviderClears_Object = MibTableColumn
wanX25StatsProviderClears = _WanX25StatsProviderClears_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 14),
    _WanX25StatsProviderClears_Type()
)
wanX25StatsProviderClears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsProviderClears.setStatus("current")
_WanX25StatsInResets_Type = Counter64
_WanX25StatsInResets_Object = MibTableColumn
wanX25StatsInResets = _WanX25StatsInResets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 15),
    _WanX25StatsInResets_Type()
)
wanX25StatsInResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsInResets.setStatus("current")
_WanX25StatsOutResets_Type = Counter64
_WanX25StatsOutResets_Object = MibTableColumn
wanX25StatsOutResets = _WanX25StatsOutResets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 16),
    _WanX25StatsOutResets_Type()
)
wanX25StatsOutResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsOutResets.setStatus("current")
_WanX25StatsProviderResets_Type = Counter64
_WanX25StatsProviderResets_Object = MibTableColumn
wanX25StatsProviderResets = _WanX25StatsProviderResets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 17),
    _WanX25StatsProviderResets_Type()
)
wanX25StatsProviderResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsProviderResets.setStatus("current")
_WanX25StatsInAccusedErrors_Type = Counter64
_WanX25StatsInAccusedErrors_Object = MibTableColumn
wanX25StatsInAccusedErrors = _WanX25StatsInAccusedErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 18),
    _WanX25StatsInAccusedErrors_Type()
)
wanX25StatsInAccusedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsInAccusedErrors.setStatus("current")
_WanX25StatsOutAccusedErrors_Type = Counter64
_WanX25StatsOutAccusedErrors_Object = MibTableColumn
wanX25StatsOutAccusedErrors = _WanX25StatsOutAccusedErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 19),
    _WanX25StatsOutAccusedErrors_Type()
)
wanX25StatsOutAccusedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsOutAccusedErrors.setStatus("current")
_WanX25StatsInInterrupts_Type = Counter64
_WanX25StatsInInterrupts_Object = MibTableColumn
wanX25StatsInInterrupts = _WanX25StatsInInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 20),
    _WanX25StatsInInterrupts_Type()
)
wanX25StatsInInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsInInterrupts.setStatus("current")
_WanX25StatsOutInterrupts_Type = Counter64
_WanX25StatsOutInterrupts_Object = MibTableColumn
wanX25StatsOutInterrupts = _WanX25StatsOutInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 21),
    _WanX25StatsOutInterrupts_Type()
)
wanX25StatsOutInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25StatsOutInterrupts.setStatus("current")
_WanX25StatsOwner_Type = OwnerString
_WanX25StatsOwner_Object = MibTableColumn
wanX25StatsOwner = _WanX25StatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 22),
    _WanX25StatsOwner_Type()
)
wanX25StatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanX25StatsOwner.setStatus("current")
_WanX25StatsStatus_Type = RowStatus
_WanX25StatsStatus_Object = MibTableColumn
wanX25StatsStatus = _WanX25StatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 1, 1, 23),
    _WanX25StatsStatus_Type()
)
wanX25StatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanX25StatsStatus.setStatus("current")
_WanFrStatsTable_Object = MibTable
wanFrStatsTable = _WanFrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wanFrStatsTable.setStatus("current")
_WanFrStatsEntry_Object = MibTableRow
wanFrStatsEntry = _WanFrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 2, 1)
)
wanFrStatsEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanFrStatsIndex"),
)
if mibBuilder.loadTexts:
    wanFrStatsEntry.setStatus("current")


class _WanFrStatsIndex_Type(Integer32):
    """Custom type wanFrStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanFrStatsIndex_Type.__name__ = "Integer32"
_WanFrStatsIndex_Object = MibTableColumn
wanFrStatsIndex = _WanFrStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 2, 1, 1),
    _WanFrStatsIndex_Type()
)
wanFrStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanFrStatsIndex.setStatus("current")
_WanFrStatsDataSource_Type = ObjectIdentifier
_WanFrStatsDataSource_Object = MibTableColumn
wanFrStatsDataSource = _WanFrStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 2, 1, 2),
    _WanFrStatsDataSource_Type()
)
wanFrStatsDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanFrStatsDataSource.setStatus("current")
_WanFrStatsDropEvents_Type = Counter64
_WanFrStatsDropEvents_Object = MibTableColumn
wanFrStatsDropEvents = _WanFrStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 2, 1, 3),
    _WanFrStatsDropEvents_Type()
)
wanFrStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrStatsDropEvents.setStatus("current")
_WanFrStatsInFrames_Type = Counter64
_WanFrStatsInFrames_Object = MibTableColumn
wanFrStatsInFrames = _WanFrStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 2, 1, 4),
    _WanFrStatsInFrames_Type()
)
wanFrStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrStatsInFrames.setStatus("current")
_WanFrStatsOutFrames_Type = Counter64
_WanFrStatsOutFrames_Object = MibTableColumn
wanFrStatsOutFrames = _WanFrStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 2, 1, 5),
    _WanFrStatsOutFrames_Type()
)
wanFrStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrStatsOutFrames.setStatus("current")
_WanFrStatsInOctets_Type = Counter64
_WanFrStatsInOctets_Object = MibTableColumn
wanFrStatsInOctets = _WanFrStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 2, 1, 6),
    _WanFrStatsInOctets_Type()
)
wanFrStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrStatsInOctets.setStatus("current")
_WanFrStatsOutOctets_Type = Counter64
_WanFrStatsOutOctets_Object = MibTableColumn
wanFrStatsOutOctets = _WanFrStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 2, 1, 7),
    _WanFrStatsOutOctets_Type()
)
wanFrStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrStatsOutOctets.setStatus("current")
_WanFrStatsInFECNs_Type = Counter64
_WanFrStatsInFECNs_Object = MibTableColumn
wanFrStatsInFECNs = _WanFrStatsInFECNs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 2, 1, 8),
    _WanFrStatsInFECNs_Type()
)
wanFrStatsInFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrStatsInFECNs.setStatus("current")
_WanFrStatsOutFECNs_Type = Counter64
_WanFrStatsOutFECNs_Object = MibTableColumn
wanFrStatsOutFECNs = _WanFrStatsOutFECNs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 2, 1, 9),
    _WanFrStatsOutFECNs_Type()
)
wanFrStatsOutFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrStatsOutFECNs.setStatus("current")
_WanFrStatsInBECNs_Type = Counter64
_WanFrStatsInBECNs_Object = MibTableColumn
wanFrStatsInBECNs = _WanFrStatsInBECNs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 2, 1, 10),
    _WanFrStatsInBECNs_Type()
)
wanFrStatsInBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrStatsInBECNs.setStatus("current")
_WanFrStatsOutBECNs_Type = Counter64
_WanFrStatsOutBECNs_Object = MibTableColumn
wanFrStatsOutBECNs = _WanFrStatsOutBECNs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 2, 1, 11),
    _WanFrStatsOutBECNs_Type()
)
wanFrStatsOutBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrStatsOutBECNs.setStatus("current")
_WanFrStatsInDEs_Type = Counter64
_WanFrStatsInDEs_Object = MibTableColumn
wanFrStatsInDEs = _WanFrStatsInDEs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 2, 1, 12),
    _WanFrStatsInDEs_Type()
)
wanFrStatsInDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrStatsInDEs.setStatus("current")
_WanFrStatsOutDEs_Type = Counter64
_WanFrStatsOutDEs_Object = MibTableColumn
wanFrStatsOutDEs = _WanFrStatsOutDEs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 2, 1, 13),
    _WanFrStatsOutDEs_Type()
)
wanFrStatsOutDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrStatsOutDEs.setStatus("current")
_WanFrStatsOwner_Type = OwnerString
_WanFrStatsOwner_Object = MibTableColumn
wanFrStatsOwner = _WanFrStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 2, 1, 14),
    _WanFrStatsOwner_Type()
)
wanFrStatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanFrStatsOwner.setStatus("current")
_WanFrStatsStatus_Type = RowStatus
_WanFrStatsStatus_Object = MibTableColumn
wanFrStatsStatus = _WanFrStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 2, 1, 15),
    _WanFrStatsStatus_Type()
)
wanFrStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanFrStatsStatus.setStatus("current")
_WanAal5StatsTable_Object = MibTable
wanAal5StatsTable = _WanAal5StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wanAal5StatsTable.setStatus("current")
_WanAal5StatsEntry_Object = MibTableRow
wanAal5StatsEntry = _WanAal5StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1)
)
wanAal5StatsEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanAal5StatsIndex"),
)
if mibBuilder.loadTexts:
    wanAal5StatsEntry.setStatus("current")


class _WanAal5StatsIndex_Type(Integer32):
    """Custom type wanAal5StatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanAal5StatsIndex_Type.__name__ = "Integer32"
_WanAal5StatsIndex_Object = MibTableColumn
wanAal5StatsIndex = _WanAal5StatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 1),
    _WanAal5StatsIndex_Type()
)
wanAal5StatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanAal5StatsIndex.setStatus("current")
_WanAal5StatsDataSource_Type = ObjectIdentifier
_WanAal5StatsDataSource_Object = MibTableColumn
wanAal5StatsDataSource = _WanAal5StatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 2),
    _WanAal5StatsDataSource_Type()
)
wanAal5StatsDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanAal5StatsDataSource.setStatus("current")
_WanAal5StatsDropEvents_Type = Counter64
_WanAal5StatsDropEvents_Object = MibTableColumn
wanAal5StatsDropEvents = _WanAal5StatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 3),
    _WanAal5StatsDropEvents_Type()
)
wanAal5StatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5StatsDropEvents.setStatus("current")
_WanAal5StatsInCells_Type = Counter64
_WanAal5StatsInCells_Object = MibTableColumn
wanAal5StatsInCells = _WanAal5StatsInCells_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 4),
    _WanAal5StatsInCells_Type()
)
wanAal5StatsInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5StatsInCells.setStatus("current")
_WanAal5StatsOutCells_Type = Counter64
_WanAal5StatsOutCells_Object = MibTableColumn
wanAal5StatsOutCells = _WanAal5StatsOutCells_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 5),
    _WanAal5StatsOutCells_Type()
)
wanAal5StatsOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5StatsOutCells.setStatus("current")
_WanAal5StatsInPDUs_Type = Counter64
_WanAal5StatsInPDUs_Object = MibTableColumn
wanAal5StatsInPDUs = _WanAal5StatsInPDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 6),
    _WanAal5StatsInPDUs_Type()
)
wanAal5StatsInPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5StatsInPDUs.setStatus("current")
_WanAal5StatsOutPDUs_Type = Counter64
_WanAal5StatsOutPDUs_Object = MibTableColumn
wanAal5StatsOutPDUs = _WanAal5StatsOutPDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 7),
    _WanAal5StatsOutPDUs_Type()
)
wanAal5StatsOutPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5StatsOutPDUs.setStatus("current")
_WanAal5StatsInOctets_Type = Counter64
_WanAal5StatsInOctets_Object = MibTableColumn
wanAal5StatsInOctets = _WanAal5StatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 8),
    _WanAal5StatsInOctets_Type()
)
wanAal5StatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5StatsInOctets.setStatus("current")
_WanAal5StatsOutOctets_Type = Counter64
_WanAal5StatsOutOctets_Object = MibTableColumn
wanAal5StatsOutOctets = _WanAal5StatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 9),
    _WanAal5StatsOutOctets_Type()
)
wanAal5StatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5StatsOutOctets.setStatus("current")
_WanAal5StatsInCLP1_Type = Counter64
_WanAal5StatsInCLP1_Object = MibTableColumn
wanAal5StatsInCLP1 = _WanAal5StatsInCLP1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 10),
    _WanAal5StatsInCLP1_Type()
)
wanAal5StatsInCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5StatsInCLP1.setStatus("current")
_WanAal5StatsOutCLP1_Type = Counter64
_WanAal5StatsOutCLP1_Object = MibTableColumn
wanAal5StatsOutCLP1 = _WanAal5StatsOutCLP1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 11),
    _WanAal5StatsOutCLP1_Type()
)
wanAal5StatsOutCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5StatsOutCLP1.setStatus("current")
_WanAal5StatsInCRCs_Type = Counter64
_WanAal5StatsInCRCs_Object = MibTableColumn
wanAal5StatsInCRCs = _WanAal5StatsInCRCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 12),
    _WanAal5StatsInCRCs_Type()
)
wanAal5StatsInCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5StatsInCRCs.setStatus("current")
_WanAal5StatsOutCRCs_Type = Counter64
_WanAal5StatsOutCRCs_Object = MibTableColumn
wanAal5StatsOutCRCs = _WanAal5StatsOutCRCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 13),
    _WanAal5StatsOutCRCs_Type()
)
wanAal5StatsOutCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5StatsOutCRCs.setStatus("current")
_WanAal5StatsInOversizedSDUs_Type = Counter64
_WanAal5StatsInOversizedSDUs_Object = MibTableColumn
wanAal5StatsInOversizedSDUs = _WanAal5StatsInOversizedSDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 14),
    _WanAal5StatsInOversizedSDUs_Type()
)
wanAal5StatsInOversizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5StatsInOversizedSDUs.setStatus("current")
_WanAal5StatsOutOversizedSDUs_Type = Counter64
_WanAal5StatsOutOversizedSDUs_Object = MibTableColumn
wanAal5StatsOutOversizedSDUs = _WanAal5StatsOutOversizedSDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 15),
    _WanAal5StatsOutOversizedSDUs_Type()
)
wanAal5StatsOutOversizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5StatsOutOversizedSDUs.setStatus("current")
_WanAal5StatsInSVCs_Type = Counter64
_WanAal5StatsInSVCs_Object = MibTableColumn
wanAal5StatsInSVCs = _WanAal5StatsInSVCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 16),
    _WanAal5StatsInSVCs_Type()
)
wanAal5StatsInSVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5StatsInSVCs.setStatus("current")
_WanAal5StatsOutSVCs_Type = Counter64
_WanAal5StatsOutSVCs_Object = MibTableColumn
wanAal5StatsOutSVCs = _WanAal5StatsOutSVCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 17),
    _WanAal5StatsOutSVCs_Type()
)
wanAal5StatsOutSVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5StatsOutSVCs.setStatus("current")
_WanAal5StatsOwner_Type = OwnerString
_WanAal5StatsOwner_Object = MibTableColumn
wanAal5StatsOwner = _WanAal5StatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 18),
    _WanAal5StatsOwner_Type()
)
wanAal5StatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanAal5StatsOwner.setStatus("current")
_WanAal5StatsStatus_Type = RowStatus
_WanAal5StatsStatus_Object = MibTableColumn
wanAal5StatsStatus = _WanAal5StatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 3, 1, 19),
    _WanAal5StatsStatus_Type()
)
wanAal5StatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanAal5StatsStatus.setStatus("current")
_WanPppStatsTable_Object = MibTable
wanPppStatsTable = _WanPppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4)
)
if mibBuilder.loadTexts:
    wanPppStatsTable.setStatus("current")
_WanPppStatsEntry_Object = MibTableRow
wanPppStatsEntry = _WanPppStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1)
)
wanPppStatsEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanPppStatsIndex"),
)
if mibBuilder.loadTexts:
    wanPppStatsEntry.setStatus("current")


class _WanPppStatsIndex_Type(Integer32):
    """Custom type wanPppStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanPppStatsIndex_Type.__name__ = "Integer32"
_WanPppStatsIndex_Object = MibTableColumn
wanPppStatsIndex = _WanPppStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1, 1),
    _WanPppStatsIndex_Type()
)
wanPppStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanPppStatsIndex.setStatus("current")
_WanPppStatsDataSource_Type = ObjectIdentifier
_WanPppStatsDataSource_Object = MibTableColumn
wanPppStatsDataSource = _WanPppStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1, 2),
    _WanPppStatsDataSource_Type()
)
wanPppStatsDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanPppStatsDataSource.setStatus("current")
_WanPppStatsDropEvents_Type = Counter64
_WanPppStatsDropEvents_Object = MibTableColumn
wanPppStatsDropEvents = _WanPppStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1, 3),
    _WanPppStatsDropEvents_Type()
)
wanPppStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppStatsDropEvents.setStatus("current")
_WanPppStatsInFrames_Type = Counter64
_WanPppStatsInFrames_Object = MibTableColumn
wanPppStatsInFrames = _WanPppStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1, 4),
    _WanPppStatsInFrames_Type()
)
wanPppStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppStatsInFrames.setStatus("current")
_WanPppStatsOutFrames_Type = Counter64
_WanPppStatsOutFrames_Object = MibTableColumn
wanPppStatsOutFrames = _WanPppStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1, 5),
    _WanPppStatsOutFrames_Type()
)
wanPppStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppStatsOutFrames.setStatus("current")
_WanPppStatsInOctets_Type = Counter64
_WanPppStatsInOctets_Object = MibTableColumn
wanPppStatsInOctets = _WanPppStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1, 6),
    _WanPppStatsInOctets_Type()
)
wanPppStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppStatsInOctets.setStatus("current")
_WanPppStatsOutOctets_Type = Counter64
_WanPppStatsOutOctets_Object = MibTableColumn
wanPppStatsOutOctets = _WanPppStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1, 7),
    _WanPppStatsOutOctets_Type()
)
wanPppStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppStatsOutOctets.setStatus("current")
_WanPppStatsInBadAddresses_Type = Counter64
_WanPppStatsInBadAddresses_Object = MibTableColumn
wanPppStatsInBadAddresses = _WanPppStatsInBadAddresses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1, 8),
    _WanPppStatsInBadAddresses_Type()
)
wanPppStatsInBadAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppStatsInBadAddresses.setStatus("current")
_WanPppStatsOutBadAddresses_Type = Counter64
_WanPppStatsOutBadAddresses_Object = MibTableColumn
wanPppStatsOutBadAddresses = _WanPppStatsOutBadAddresses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1, 9),
    _WanPppStatsOutBadAddresses_Type()
)
wanPppStatsOutBadAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppStatsOutBadAddresses.setStatus("current")
_WanPppStatsInBadControls_Type = Counter64
_WanPppStatsInBadControls_Object = MibTableColumn
wanPppStatsInBadControls = _WanPppStatsInBadControls_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1, 10),
    _WanPppStatsInBadControls_Type()
)
wanPppStatsInBadControls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppStatsInBadControls.setStatus("current")
_WanPppStatsOutBadControls_Type = Counter64
_WanPppStatsOutBadControls_Object = MibTableColumn
wanPppStatsOutBadControls = _WanPppStatsOutBadControls_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1, 11),
    _WanPppStatsOutBadControls_Type()
)
wanPppStatsOutBadControls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppStatsOutBadControls.setStatus("current")
_WanPppStatsInLongFrames_Type = Counter64
_WanPppStatsInLongFrames_Object = MibTableColumn
wanPppStatsInLongFrames = _WanPppStatsInLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1, 12),
    _WanPppStatsInLongFrames_Type()
)
wanPppStatsInLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppStatsInLongFrames.setStatus("current")
_WanPppStatsOutLongFrames_Type = Counter64
_WanPppStatsOutLongFrames_Object = MibTableColumn
wanPppStatsOutLongFrames = _WanPppStatsOutLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1, 13),
    _WanPppStatsOutLongFrames_Type()
)
wanPppStatsOutLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppStatsOutLongFrames.setStatus("current")
_WanPppStatsInBadFCSs_Type = Counter64
_WanPppStatsInBadFCSs_Object = MibTableColumn
wanPppStatsInBadFCSs = _WanPppStatsInBadFCSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1, 14),
    _WanPppStatsInBadFCSs_Type()
)
wanPppStatsInBadFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppStatsInBadFCSs.setStatus("current")
_WanPppStatsOutBadFCSs_Type = Counter64
_WanPppStatsOutBadFCSs_Object = MibTableColumn
wanPppStatsOutBadFCSs = _WanPppStatsOutBadFCSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1, 15),
    _WanPppStatsOutBadFCSs_Type()
)
wanPppStatsOutBadFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppStatsOutBadFCSs.setStatus("current")
_WanPppStatsOwner_Type = OwnerString
_WanPppStatsOwner_Object = MibTableColumn
wanPppStatsOwner = _WanPppStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1, 16),
    _WanPppStatsOwner_Type()
)
wanPppStatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanPppStatsOwner.setStatus("current")
_WanPppStatsStatus_Type = RowStatus
_WanPppStatsStatus_Object = MibTableColumn
wanPppStatsStatus = _WanPppStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 2, 4, 1, 17),
    _WanPppStatsStatus_Type()
)
wanPppStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanPppStatsStatus.setStatus("current")
_WanPvcStats_ObjectIdentity = ObjectIdentity
wanPvcStats = _WanPvcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3)
)
_WanX25PvcStatsTable_Object = MibTable
wanX25PvcStatsTable = _WanX25PvcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wanX25PvcStatsTable.setStatus("current")
_WanX25PvcStatsEntry_Object = MibTableRow
wanX25PvcStatsEntry = _WanX25PvcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1)
)
wanX25PvcStatsEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanX25StatsIndex"),
)
if mibBuilder.loadTexts:
    wanX25PvcStatsEntry.setStatus("current")


class _WanX25PvcStatsIndex_Type(Integer32):
    """Custom type wanX25PvcStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanX25PvcStatsIndex_Type.__name__ = "Integer32"
_WanX25PvcStatsIndex_Object = MibTableColumn
wanX25PvcStatsIndex = _WanX25PvcStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 1),
    _WanX25PvcStatsIndex_Type()
)
wanX25PvcStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanX25PvcStatsIndex.setStatus("current")
_WanX25PvcStatsDataSource_Type = ObjectIdentifier
_WanX25PvcStatsDataSource_Object = MibTableColumn
wanX25PvcStatsDataSource = _WanX25PvcStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 2),
    _WanX25PvcStatsDataSource_Type()
)
wanX25PvcStatsDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanX25PvcStatsDataSource.setStatus("current")
_WanX25PvcStatsDropEvents_Type = Counter64
_WanX25PvcStatsDropEvents_Object = MibTableColumn
wanX25PvcStatsDropEvents = _WanX25PvcStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 3),
    _WanX25PvcStatsDropEvents_Type()
)
wanX25PvcStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcStatsDropEvents.setStatus("current")
_WanX25PvcStatsInFrames_Type = Counter64
_WanX25PvcStatsInFrames_Object = MibTableColumn
wanX25PvcStatsInFrames = _WanX25PvcStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 4),
    _WanX25PvcStatsInFrames_Type()
)
wanX25PvcStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcStatsInFrames.setStatus("current")
_WanX25PvcStatsOutFrames_Type = Counter64
_WanX25PvcStatsOutFrames_Object = MibTableColumn
wanX25PvcStatsOutFrames = _WanX25PvcStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 5),
    _WanX25PvcStatsOutFrames_Type()
)
wanX25PvcStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcStatsOutFrames.setStatus("current")
_WanX25PvcStatsInOctets_Type = Counter64
_WanX25PvcStatsInOctets_Object = MibTableColumn
wanX25PvcStatsInOctets = _WanX25PvcStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 6),
    _WanX25PvcStatsInOctets_Type()
)
wanX25PvcStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcStatsInOctets.setStatus("current")
_WanX25PvcStatsOutOctets_Type = Counter64
_WanX25PvcStatsOutOctets_Object = MibTableColumn
wanX25PvcStatsOutOctets = _WanX25PvcStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 7),
    _WanX25PvcStatsOutOctets_Type()
)
wanX25PvcStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcStatsOutOctets.setStatus("current")
_WanX25PvcStatsInResets_Type = Counter64
_WanX25PvcStatsInResets_Object = MibTableColumn
wanX25PvcStatsInResets = _WanX25PvcStatsInResets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 8),
    _WanX25PvcStatsInResets_Type()
)
wanX25PvcStatsInResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcStatsInResets.setStatus("current")
_WanX25PvcStatsOutResets_Type = Counter64
_WanX25PvcStatsOutResets_Object = MibTableColumn
wanX25PvcStatsOutResets = _WanX25PvcStatsOutResets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 9),
    _WanX25PvcStatsOutResets_Type()
)
wanX25PvcStatsOutResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcStatsOutResets.setStatus("current")
_WanX25PvcStatsProviderResets_Type = Counter64
_WanX25PvcStatsProviderResets_Object = MibTableColumn
wanX25PvcStatsProviderResets = _WanX25PvcStatsProviderResets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 10),
    _WanX25PvcStatsProviderResets_Type()
)
wanX25PvcStatsProviderResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcStatsProviderResets.setStatus("current")
_WanX25PvcStatsInAccusedErrors_Type = Counter64
_WanX25PvcStatsInAccusedErrors_Object = MibTableColumn
wanX25PvcStatsInAccusedErrors = _WanX25PvcStatsInAccusedErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 11),
    _WanX25PvcStatsInAccusedErrors_Type()
)
wanX25PvcStatsInAccusedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcStatsInAccusedErrors.setStatus("current")
_WanX25PvcStatsOutAccusedErrors_Type = Counter64
_WanX25PvcStatsOutAccusedErrors_Object = MibTableColumn
wanX25PvcStatsOutAccusedErrors = _WanX25PvcStatsOutAccusedErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 12),
    _WanX25PvcStatsOutAccusedErrors_Type()
)
wanX25PvcStatsOutAccusedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcStatsOutAccusedErrors.setStatus("current")
_WanX25PvcStatsInInterrupts_Type = Counter64
_WanX25PvcStatsInInterrupts_Object = MibTableColumn
wanX25PvcStatsInInterrupts = _WanX25PvcStatsInInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 13),
    _WanX25PvcStatsInInterrupts_Type()
)
wanX25PvcStatsInInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcStatsInInterrupts.setStatus("current")
_WanX25PvcStatsOutInterrupts_Type = Counter64
_WanX25PvcStatsOutInterrupts_Object = MibTableColumn
wanX25PvcStatsOutInterrupts = _WanX25PvcStatsOutInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 14),
    _WanX25PvcStatsOutInterrupts_Type()
)
wanX25PvcStatsOutInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcStatsOutInterrupts.setStatus("current")
_WanX25PvcStatsUpTime_Type = TimeTicks
_WanX25PvcStatsUpTime_Object = MibTableColumn
wanX25PvcStatsUpTime = _WanX25PvcStatsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 15),
    _WanX25PvcStatsUpTime_Type()
)
wanX25PvcStatsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcStatsUpTime.setStatus("current")
_WanX25PvcStatsDownTime_Type = TimeTicks
_WanX25PvcStatsDownTime_Object = MibTableColumn
wanX25PvcStatsDownTime = _WanX25PvcStatsDownTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 16),
    _WanX25PvcStatsDownTime_Type()
)
wanX25PvcStatsDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcStatsDownTime.setStatus("current")


class _WanX25PvcStatsState_Type(Integer32):
    """Custom type wanX25PvcStatsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_WanX25PvcStatsState_Type.__name__ = "Integer32"
_WanX25PvcStatsState_Object = MibTableColumn
wanX25PvcStatsState = _WanX25PvcStatsState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 17),
    _WanX25PvcStatsState_Type()
)
wanX25PvcStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcStatsState.setStatus("current")
_WanX25PvcStatsStateChanges_Type = Counter64
_WanX25PvcStatsStateChanges_Object = MibTableColumn
wanX25PvcStatsStateChanges = _WanX25PvcStatsStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 18),
    _WanX25PvcStatsStateChanges_Type()
)
wanX25PvcStatsStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcStatsStateChanges.setStatus("current")
_WanX25PvcStatsOwner_Type = OwnerString
_WanX25PvcStatsOwner_Object = MibTableColumn
wanX25PvcStatsOwner = _WanX25PvcStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 19),
    _WanX25PvcStatsOwner_Type()
)
wanX25PvcStatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanX25PvcStatsOwner.setStatus("current")
_WanX25PvcStatsStatus_Type = RowStatus
_WanX25PvcStatsStatus_Object = MibTableColumn
wanX25PvcStatsStatus = _WanX25PvcStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 1, 1, 20),
    _WanX25PvcStatsStatus_Type()
)
wanX25PvcStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanX25PvcStatsStatus.setStatus("current")
_WanFrPvcStatsTable_Object = MibTable
wanFrPvcStatsTable = _WanFrPvcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wanFrPvcStatsTable.setStatus("current")
_WanFrPvcStatsEntry_Object = MibTableRow
wanFrPvcStatsEntry = _WanFrPvcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1)
)
wanFrPvcStatsEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanFrPvcStatsIndex"),
)
if mibBuilder.loadTexts:
    wanFrPvcStatsEntry.setStatus("current")


class _WanFrPvcStatsIndex_Type(Integer32):
    """Custom type wanFrPvcStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanFrPvcStatsIndex_Type.__name__ = "Integer32"
_WanFrPvcStatsIndex_Object = MibTableColumn
wanFrPvcStatsIndex = _WanFrPvcStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 1),
    _WanFrPvcStatsIndex_Type()
)
wanFrPvcStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanFrPvcStatsIndex.setStatus("current")
_WanFrPvcStatsDataSource_Type = ObjectIdentifier
_WanFrPvcStatsDataSource_Object = MibTableColumn
wanFrPvcStatsDataSource = _WanFrPvcStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 2),
    _WanFrPvcStatsDataSource_Type()
)
wanFrPvcStatsDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanFrPvcStatsDataSource.setStatus("current")
_WanFrPvcStatsDropEvents_Type = Counter64
_WanFrPvcStatsDropEvents_Object = MibTableColumn
wanFrPvcStatsDropEvents = _WanFrPvcStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 3),
    _WanFrPvcStatsDropEvents_Type()
)
wanFrPvcStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcStatsDropEvents.setStatus("current")
_WanFrPvcStatsInFrames_Type = Counter64
_WanFrPvcStatsInFrames_Object = MibTableColumn
wanFrPvcStatsInFrames = _WanFrPvcStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 4),
    _WanFrPvcStatsInFrames_Type()
)
wanFrPvcStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcStatsInFrames.setStatus("current")
_WanFrPvcStatsOutFrames_Type = Counter64
_WanFrPvcStatsOutFrames_Object = MibTableColumn
wanFrPvcStatsOutFrames = _WanFrPvcStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 5),
    _WanFrPvcStatsOutFrames_Type()
)
wanFrPvcStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcStatsOutFrames.setStatus("current")
_WanFrPvcStatsInOctets_Type = Counter64
_WanFrPvcStatsInOctets_Object = MibTableColumn
wanFrPvcStatsInOctets = _WanFrPvcStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 6),
    _WanFrPvcStatsInOctets_Type()
)
wanFrPvcStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcStatsInOctets.setStatus("current")
_WanFrPvcStatsOutOctets_Type = Counter64
_WanFrPvcStatsOutOctets_Object = MibTableColumn
wanFrPvcStatsOutOctets = _WanFrPvcStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 7),
    _WanFrPvcStatsOutOctets_Type()
)
wanFrPvcStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcStatsOutOctets.setStatus("current")
_WanFrPvcStatsInFECNs_Type = Counter64
_WanFrPvcStatsInFECNs_Object = MibTableColumn
wanFrPvcStatsInFECNs = _WanFrPvcStatsInFECNs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 8),
    _WanFrPvcStatsInFECNs_Type()
)
wanFrPvcStatsInFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcStatsInFECNs.setStatus("current")
_WanFrPvcStatsOutFECNs_Type = Counter64
_WanFrPvcStatsOutFECNs_Object = MibTableColumn
wanFrPvcStatsOutFECNs = _WanFrPvcStatsOutFECNs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 9),
    _WanFrPvcStatsOutFECNs_Type()
)
wanFrPvcStatsOutFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcStatsOutFECNs.setStatus("current")
_WanFrPvcStatsInBECNs_Type = Counter64
_WanFrPvcStatsInBECNs_Object = MibTableColumn
wanFrPvcStatsInBECNs = _WanFrPvcStatsInBECNs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 10),
    _WanFrPvcStatsInBECNs_Type()
)
wanFrPvcStatsInBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcStatsInBECNs.setStatus("current")
_WanFrPvcStatsOutBECNs_Type = Counter64
_WanFrPvcStatsOutBECNs_Object = MibTableColumn
wanFrPvcStatsOutBECNs = _WanFrPvcStatsOutBECNs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 11),
    _WanFrPvcStatsOutBECNs_Type()
)
wanFrPvcStatsOutBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcStatsOutBECNs.setStatus("current")
_WanFrPvcStatsInDEs_Type = Counter64
_WanFrPvcStatsInDEs_Object = MibTableColumn
wanFrPvcStatsInDEs = _WanFrPvcStatsInDEs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 12),
    _WanFrPvcStatsInDEs_Type()
)
wanFrPvcStatsInDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcStatsInDEs.setStatus("current")
_WanFrPvcStatsOutDEs_Type = Counter64
_WanFrPvcStatsOutDEs_Object = MibTableColumn
wanFrPvcStatsOutDEs = _WanFrPvcStatsOutDEs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 13),
    _WanFrPvcStatsOutDEs_Type()
)
wanFrPvcStatsOutDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcStatsOutDEs.setStatus("current")
_WanFrPvcStatsUpTime_Type = TimeTicks
_WanFrPvcStatsUpTime_Object = MibTableColumn
wanFrPvcStatsUpTime = _WanFrPvcStatsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 14),
    _WanFrPvcStatsUpTime_Type()
)
wanFrPvcStatsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcStatsUpTime.setStatus("current")
_WanFrPvcStatsDownTime_Type = TimeTicks
_WanFrPvcStatsDownTime_Object = MibTableColumn
wanFrPvcStatsDownTime = _WanFrPvcStatsDownTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 15),
    _WanFrPvcStatsDownTime_Type()
)
wanFrPvcStatsDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcStatsDownTime.setStatus("current")


class _WanFrPvcStatsState_Type(Integer32):
    """Custom type wanFrPvcStatsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_WanFrPvcStatsState_Type.__name__ = "Integer32"
_WanFrPvcStatsState_Object = MibTableColumn
wanFrPvcStatsState = _WanFrPvcStatsState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 16),
    _WanFrPvcStatsState_Type()
)
wanFrPvcStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcStatsState.setStatus("current")
_WanFrPvcStatsStateChanges_Type = Counter64
_WanFrPvcStatsStateChanges_Object = MibTableColumn
wanFrPvcStatsStateChanges = _WanFrPvcStatsStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 17),
    _WanFrPvcStatsStateChanges_Type()
)
wanFrPvcStatsStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcStatsStateChanges.setStatus("current")
_WanFrPvcStatsOwner_Type = OwnerString
_WanFrPvcStatsOwner_Object = MibTableColumn
wanFrPvcStatsOwner = _WanFrPvcStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 18),
    _WanFrPvcStatsOwner_Type()
)
wanFrPvcStatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanFrPvcStatsOwner.setStatus("current")
_WanFrPvcStatsStatus_Type = RowStatus
_WanFrPvcStatsStatus_Object = MibTableColumn
wanFrPvcStatsStatus = _WanFrPvcStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 2, 1, 19),
    _WanFrPvcStatsStatus_Type()
)
wanFrPvcStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanFrPvcStatsStatus.setStatus("current")
_WanAal5PvcStatsTable_Object = MibTable
wanAal5PvcStatsTable = _WanAal5PvcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3)
)
if mibBuilder.loadTexts:
    wanAal5PvcStatsTable.setStatus("current")
_WanAal5PvcStatsEntry_Object = MibTableRow
wanAal5PvcStatsEntry = _WanAal5PvcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1)
)
wanAal5PvcStatsEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanAal5PvcStatsIndex"),
)
if mibBuilder.loadTexts:
    wanAal5PvcStatsEntry.setStatus("current")


class _WanAal5PvcStatsIndex_Type(Integer32):
    """Custom type wanAal5PvcStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanAal5PvcStatsIndex_Type.__name__ = "Integer32"
_WanAal5PvcStatsIndex_Object = MibTableColumn
wanAal5PvcStatsIndex = _WanAal5PvcStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 1),
    _WanAal5PvcStatsIndex_Type()
)
wanAal5PvcStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanAal5PvcStatsIndex.setStatus("current")
_WanAal5PvcStatsDataSource_Type = ObjectIdentifier
_WanAal5PvcStatsDataSource_Object = MibTableColumn
wanAal5PvcStatsDataSource = _WanAal5PvcStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 2),
    _WanAal5PvcStatsDataSource_Type()
)
wanAal5PvcStatsDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanAal5PvcStatsDataSource.setStatus("current")
_WanAal5PvcStatsDropEvents_Type = Counter64
_WanAal5PvcStatsDropEvents_Object = MibTableColumn
wanAal5PvcStatsDropEvents = _WanAal5PvcStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 3),
    _WanAal5PvcStatsDropEvents_Type()
)
wanAal5PvcStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcStatsDropEvents.setStatus("current")
_WanAal5PvcStatsInCells_Type = Counter64
_WanAal5PvcStatsInCells_Object = MibTableColumn
wanAal5PvcStatsInCells = _WanAal5PvcStatsInCells_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 4),
    _WanAal5PvcStatsInCells_Type()
)
wanAal5PvcStatsInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcStatsInCells.setStatus("current")
_WanAal5PvcStatsOutCells_Type = Counter64
_WanAal5PvcStatsOutCells_Object = MibTableColumn
wanAal5PvcStatsOutCells = _WanAal5PvcStatsOutCells_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 5),
    _WanAal5PvcStatsOutCells_Type()
)
wanAal5PvcStatsOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcStatsOutCells.setStatus("current")
_WanAal5PvcStatsInPDUs_Type = Counter64
_WanAal5PvcStatsInPDUs_Object = MibTableColumn
wanAal5PvcStatsInPDUs = _WanAal5PvcStatsInPDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 6),
    _WanAal5PvcStatsInPDUs_Type()
)
wanAal5PvcStatsInPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcStatsInPDUs.setStatus("current")
_WanAal5PvcStatsOutPDUs_Type = Counter64
_WanAal5PvcStatsOutPDUs_Object = MibTableColumn
wanAal5PvcStatsOutPDUs = _WanAal5PvcStatsOutPDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 7),
    _WanAal5PvcStatsOutPDUs_Type()
)
wanAal5PvcStatsOutPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcStatsOutPDUs.setStatus("current")
_WanAal5PvcStatsInOctets_Type = Counter64
_WanAal5PvcStatsInOctets_Object = MibTableColumn
wanAal5PvcStatsInOctets = _WanAal5PvcStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 8),
    _WanAal5PvcStatsInOctets_Type()
)
wanAal5PvcStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcStatsInOctets.setStatus("current")
_WanAal5PvcStatsOutOctets_Type = Counter64
_WanAal5PvcStatsOutOctets_Object = MibTableColumn
wanAal5PvcStatsOutOctets = _WanAal5PvcStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 9),
    _WanAal5PvcStatsOutOctets_Type()
)
wanAal5PvcStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcStatsOutOctets.setStatus("current")
_WanAal5PvcStatsInCLP1_Type = Counter64
_WanAal5PvcStatsInCLP1_Object = MibTableColumn
wanAal5PvcStatsInCLP1 = _WanAal5PvcStatsInCLP1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 10),
    _WanAal5PvcStatsInCLP1_Type()
)
wanAal5PvcStatsInCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcStatsInCLP1.setStatus("current")
_WanAal5PvcStatsOutCLP1_Type = Counter64
_WanAal5PvcStatsOutCLP1_Object = MibTableColumn
wanAal5PvcStatsOutCLP1 = _WanAal5PvcStatsOutCLP1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 11),
    _WanAal5PvcStatsOutCLP1_Type()
)
wanAal5PvcStatsOutCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcStatsOutCLP1.setStatus("current")
_WanAal5PvcStatsInCRCs_Type = Counter64
_WanAal5PvcStatsInCRCs_Object = MibTableColumn
wanAal5PvcStatsInCRCs = _WanAal5PvcStatsInCRCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 12),
    _WanAal5PvcStatsInCRCs_Type()
)
wanAal5PvcStatsInCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcStatsInCRCs.setStatus("current")
_WanAal5PvcStatsOutCRCs_Type = Counter64
_WanAal5PvcStatsOutCRCs_Object = MibTableColumn
wanAal5PvcStatsOutCRCs = _WanAal5PvcStatsOutCRCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 13),
    _WanAal5PvcStatsOutCRCs_Type()
)
wanAal5PvcStatsOutCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcStatsOutCRCs.setStatus("current")
_WanAal5PvcStatsInOversizedSDUs_Type = Counter64
_WanAal5PvcStatsInOversizedSDUs_Object = MibTableColumn
wanAal5PvcStatsInOversizedSDUs = _WanAal5PvcStatsInOversizedSDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 14),
    _WanAal5PvcStatsInOversizedSDUs_Type()
)
wanAal5PvcStatsInOversizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcStatsInOversizedSDUs.setStatus("current")
_WanAal5PvcStatsOutOversizedSDUs_Type = Counter64
_WanAal5PvcStatsOutOversizedSDUs_Object = MibTableColumn
wanAal5PvcStatsOutOversizedSDUs = _WanAal5PvcStatsOutOversizedSDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 15),
    _WanAal5PvcStatsOutOversizedSDUs_Type()
)
wanAal5PvcStatsOutOversizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcStatsOutOversizedSDUs.setStatus("current")
_WanAal5PvcStatsUpTime_Type = TimeTicks
_WanAal5PvcStatsUpTime_Object = MibTableColumn
wanAal5PvcStatsUpTime = _WanAal5PvcStatsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 16),
    _WanAal5PvcStatsUpTime_Type()
)
wanAal5PvcStatsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcStatsUpTime.setStatus("current")
_WanAal5PvcStatsDownTime_Type = TimeTicks
_WanAal5PvcStatsDownTime_Object = MibTableColumn
wanAal5PvcStatsDownTime = _WanAal5PvcStatsDownTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 17),
    _WanAal5PvcStatsDownTime_Type()
)
wanAal5PvcStatsDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcStatsDownTime.setStatus("current")


class _WanAal5PvcStatsState_Type(Integer32):
    """Custom type wanAal5PvcStatsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_WanAal5PvcStatsState_Type.__name__ = "Integer32"
_WanAal5PvcStatsState_Object = MibTableColumn
wanAal5PvcStatsState = _WanAal5PvcStatsState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 18),
    _WanAal5PvcStatsState_Type()
)
wanAal5PvcStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcStatsState.setStatus("current")
_WanAal5PvcStatsStateChanges_Type = Counter64
_WanAal5PvcStatsStateChanges_Object = MibTableColumn
wanAal5PvcStatsStateChanges = _WanAal5PvcStatsStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 19),
    _WanAal5PvcStatsStateChanges_Type()
)
wanAal5PvcStatsStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcStatsStateChanges.setStatus("current")
_WanAal5PvcStatsOwner_Type = OwnerString
_WanAal5PvcStatsOwner_Object = MibTableColumn
wanAal5PvcStatsOwner = _WanAal5PvcStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 20),
    _WanAal5PvcStatsOwner_Type()
)
wanAal5PvcStatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanAal5PvcStatsOwner.setStatus("current")
_WanAal5PvcStatsStatus_Type = RowStatus
_WanAal5PvcStatsStatus_Object = MibTableColumn
wanAal5PvcStatsStatus = _WanAal5PvcStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 1, 3, 3, 1, 21),
    _WanAal5PvcStatsStatus_Type()
)
wanAal5PvcStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wanAal5PvcStatsStatus.setStatus("current")
_WanHistoryMIBObjects_ObjectIdentity = ObjectIdentity
wanHistoryMIBObjects = _WanHistoryMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2)
)
_WanSignalingHistory_ObjectIdentity = ObjectIdentity
wanSignalingHistory = _WanSignalingHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1)
)
_WanT1E1HistoryTable_Object = MibTable
wanT1E1HistoryTable = _WanT1E1HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    wanT1E1HistoryTable.setStatus("current")
_WanT1E1HistoryEntry_Object = MibTableRow
wanT1E1HistoryEntry = _WanT1E1HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1)
)
wanT1E1HistoryEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanT1E1HistoryIndex"),
    (0, "WANSTATS-MIB", "wanT1E1HistorySampleIndex"),
)
if mibBuilder.loadTexts:
    wanT1E1HistoryEntry.setStatus("current")


class _WanT1E1HistoryIndex_Type(Integer32):
    """Custom type wanT1E1HistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanT1E1HistoryIndex_Type.__name__ = "Integer32"
_WanT1E1HistoryIndex_Object = MibTableColumn
wanT1E1HistoryIndex = _WanT1E1HistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 1),
    _WanT1E1HistoryIndex_Type()
)
wanT1E1HistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanT1E1HistoryIndex.setStatus("current")


class _WanT1E1HistorySampleIndex_Type(Integer32):
    """Custom type wanT1E1HistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WanT1E1HistorySampleIndex_Type.__name__ = "Integer32"
_WanT1E1HistorySampleIndex_Object = MibTableColumn
wanT1E1HistorySampleIndex = _WanT1E1HistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 2),
    _WanT1E1HistorySampleIndex_Type()
)
wanT1E1HistorySampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanT1E1HistorySampleIndex.setStatus("current")
_WanT1E1HistoryIntervalStart_Type = TimeTicks
_WanT1E1HistoryIntervalStart_Object = MibTableColumn
wanT1E1HistoryIntervalStart = _WanT1E1HistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 3),
    _WanT1E1HistoryIntervalStart_Type()
)
wanT1E1HistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryIntervalStart.setStatus("current")
_WanT1E1HistoryDropEvents_Type = Counter64
_WanT1E1HistoryDropEvents_Object = MibTableColumn
wanT1E1HistoryDropEvents = _WanT1E1HistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 4),
    _WanT1E1HistoryDropEvents_Type()
)
wanT1E1HistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryDropEvents.setStatus("current")
_WanT1E1HistoryInFrames_Type = Counter64
_WanT1E1HistoryInFrames_Object = MibTableColumn
wanT1E1HistoryInFrames = _WanT1E1HistoryInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 5),
    _WanT1E1HistoryInFrames_Type()
)
wanT1E1HistoryInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryInFrames.setStatus("current")
_WanT1E1HistoryOutFrames_Type = Counter64
_WanT1E1HistoryOutFrames_Object = MibTableColumn
wanT1E1HistoryOutFrames = _WanT1E1HistoryOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 6),
    _WanT1E1HistoryOutFrames_Type()
)
wanT1E1HistoryOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryOutFrames.setStatus("current")
_WanT1E1HistoryInOctets_Type = Counter64
_WanT1E1HistoryInOctets_Object = MibTableColumn
wanT1E1HistoryInOctets = _WanT1E1HistoryInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 7),
    _WanT1E1HistoryInOctets_Type()
)
wanT1E1HistoryInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryInOctets.setStatus("current")
_WanT1E1HistoryOutOctets_Type = Counter64
_WanT1E1HistoryOutOctets_Object = MibTableColumn
wanT1E1HistoryOutOctets = _WanT1E1HistoryOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 8),
    _WanT1E1HistoryOutOctets_Type()
)
wanT1E1HistoryOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryOutOctets.setStatus("current")
_WanT1E1HistoryESs_Type = Counter64
_WanT1E1HistoryESs_Object = MibTableColumn
wanT1E1HistoryESs = _WanT1E1HistoryESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 9),
    _WanT1E1HistoryESs_Type()
)
wanT1E1HistoryESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryESs.setStatus("current")
_WanT1E1HistorySESs_Type = Counter64
_WanT1E1HistorySESs_Object = MibTableColumn
wanT1E1HistorySESs = _WanT1E1HistorySESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 10),
    _WanT1E1HistorySESs_Type()
)
wanT1E1HistorySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistorySESs.setStatus("current")
_WanT1E1HistorySEFSs_Type = Counter64
_WanT1E1HistorySEFSs_Object = MibTableColumn
wanT1E1HistorySEFSs = _WanT1E1HistorySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 11),
    _WanT1E1HistorySEFSs_Type()
)
wanT1E1HistorySEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistorySEFSs.setStatus("current")
_WanT1E1HistoryOOFs_Type = Counter64
_WanT1E1HistoryOOFs_Object = MibTableColumn
wanT1E1HistoryOOFs = _WanT1E1HistoryOOFs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 12),
    _WanT1E1HistoryOOFs_Type()
)
wanT1E1HistoryOOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryOOFs.setStatus("current")
_WanT1E1HistoryUASs_Type = Counter64
_WanT1E1HistoryUASs_Object = MibTableColumn
wanT1E1HistoryUASs = _WanT1E1HistoryUASs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 13),
    _WanT1E1HistoryUASs_Type()
)
wanT1E1HistoryUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryUASs.setStatus("current")
_WanT1E1HistoryCSSs_Type = Counter64
_WanT1E1HistoryCSSs_Object = MibTableColumn
wanT1E1HistoryCSSs = _WanT1E1HistoryCSSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 14),
    _WanT1E1HistoryCSSs_Type()
)
wanT1E1HistoryCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryCSSs.setStatus("current")
_WanT1E1HistoryPCVs_Type = Counter64
_WanT1E1HistoryPCVs_Object = MibTableColumn
wanT1E1HistoryPCVs = _WanT1E1HistoryPCVs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 15),
    _WanT1E1HistoryPCVs_Type()
)
wanT1E1HistoryPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryPCVs.setStatus("current")
_WanT1E1HistoryLESs_Type = Counter64
_WanT1E1HistoryLESs_Object = MibTableColumn
wanT1E1HistoryLESs = _WanT1E1HistoryLESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 16),
    _WanT1E1HistoryLESs_Type()
)
wanT1E1HistoryLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryLESs.setStatus("current")
_WanT1E1HistoryBESs_Type = Counter64
_WanT1E1HistoryBESs_Object = MibTableColumn
wanT1E1HistoryBESs = _WanT1E1HistoryBESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 17),
    _WanT1E1HistoryBESs_Type()
)
wanT1E1HistoryBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryBESs.setStatus("current")
_WanT1E1HistoryDMs_Type = Counter64
_WanT1E1HistoryDMs_Object = MibTableColumn
wanT1E1HistoryDMs = _WanT1E1HistoryDMs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 18),
    _WanT1E1HistoryDMs_Type()
)
wanT1E1HistoryDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryDMs.setStatus("current")
_WanT1E1HistoryLCVs_Type = Counter64
_WanT1E1HistoryLCVs_Object = MibTableColumn
wanT1E1HistoryLCVs = _WanT1E1HistoryLCVs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 19),
    _WanT1E1HistoryLCVs_Type()
)
wanT1E1HistoryLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryLCVs.setStatus("current")
_WanT1E1HistoryLOFs_Type = Counter64
_WanT1E1HistoryLOFs_Object = MibTableColumn
wanT1E1HistoryLOFs = _WanT1E1HistoryLOFs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 20),
    _WanT1E1HistoryLOFs_Type()
)
wanT1E1HistoryLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryLOFs.setStatus("current")
_WanT1E1HistoryLOSs_Type = Counter64
_WanT1E1HistoryLOSs_Object = MibTableColumn
wanT1E1HistoryLOSs = _WanT1E1HistoryLOSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 21),
    _WanT1E1HistoryLOSs_Type()
)
wanT1E1HistoryLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryLOSs.setStatus("current")
_WanT1E1HistoryRAIs_Type = Counter64
_WanT1E1HistoryRAIs_Object = MibTableColumn
wanT1E1HistoryRAIs = _WanT1E1HistoryRAIs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 22),
    _WanT1E1HistoryRAIs_Type()
)
wanT1E1HistoryRAIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryRAIs.setStatus("current")
_WanT1E1HistoryAISs_Type = Counter64
_WanT1E1HistoryAISs_Object = MibTableColumn
wanT1E1HistoryAISs = _WanT1E1HistoryAISs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 23),
    _WanT1E1HistoryAISs_Type()
)
wanT1E1HistoryAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryAISs.setStatus("current")
_WanT1E1HistoryTS16AISs_Type = Counter64
_WanT1E1HistoryTS16AISs_Object = MibTableColumn
wanT1E1HistoryTS16AISs = _WanT1E1HistoryTS16AISs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 24),
    _WanT1E1HistoryTS16AISs_Type()
)
wanT1E1HistoryTS16AISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryTS16AISs.setStatus("current")
_WanT1E1HistoryLOMFs_Type = Counter64
_WanT1E1HistoryLOMFs_Object = MibTableColumn
wanT1E1HistoryLOMFs = _WanT1E1HistoryLOMFs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 25),
    _WanT1E1HistoryLOMFs_Type()
)
wanT1E1HistoryLOMFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryLOMFs.setStatus("current")
_WanT1E1HistoryFarLOMFs_Type = Counter64
_WanT1E1HistoryFarLOMFs_Object = MibTableColumn
wanT1E1HistoryFarLOMFs = _WanT1E1HistoryFarLOMFs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 26),
    _WanT1E1HistoryFarLOMFs_Type()
)
wanT1E1HistoryFarLOMFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryFarLOMFs.setStatus("current")


class _WanT1E1HistoryInUtilization_Type(Integer32):
    """Custom type wanT1E1HistoryInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanT1E1HistoryInUtilization_Type.__name__ = "Integer32"
_WanT1E1HistoryInUtilization_Object = MibTableColumn
wanT1E1HistoryInUtilization = _WanT1E1HistoryInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 27),
    _WanT1E1HistoryInUtilization_Type()
)
wanT1E1HistoryInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryInUtilization.setStatus("current")


class _WanT1E1HistoryOutUtilization_Type(Integer32):
    """Custom type wanT1E1HistoryOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanT1E1HistoryOutUtilization_Type.__name__ = "Integer32"
_WanT1E1HistoryOutUtilization_Object = MibTableColumn
wanT1E1HistoryOutUtilization = _WanT1E1HistoryOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 1, 1, 28),
    _WanT1E1HistoryOutUtilization_Type()
)
wanT1E1HistoryOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT1E1HistoryOutUtilization.setStatus("current")
_WanVSeriesHistoryTable_Object = MibTable
wanVSeriesHistoryTable = _WanVSeriesHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2)
)
if mibBuilder.loadTexts:
    wanVSeriesHistoryTable.setStatus("current")
_WanVSeriesHistoryEntry_Object = MibTableRow
wanVSeriesHistoryEntry = _WanVSeriesHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1)
)
wanVSeriesHistoryEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanVSeriesHistoryIndex"),
    (0, "WANSTATS-MIB", "wanVSeriesHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    wanVSeriesHistoryEntry.setStatus("current")


class _WanVSeriesHistoryIndex_Type(Integer32):
    """Custom type wanVSeriesHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanVSeriesHistoryIndex_Type.__name__ = "Integer32"
_WanVSeriesHistoryIndex_Object = MibTableColumn
wanVSeriesHistoryIndex = _WanVSeriesHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1, 1),
    _WanVSeriesHistoryIndex_Type()
)
wanVSeriesHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanVSeriesHistoryIndex.setStatus("current")


class _WanVSeriesHistorySampleIndex_Type(Integer32):
    """Custom type wanVSeriesHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WanVSeriesHistorySampleIndex_Type.__name__ = "Integer32"
_WanVSeriesHistorySampleIndex_Object = MibTableColumn
wanVSeriesHistorySampleIndex = _WanVSeriesHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1, 2),
    _WanVSeriesHistorySampleIndex_Type()
)
wanVSeriesHistorySampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanVSeriesHistorySampleIndex.setStatus("current")
_WanVSeriesHistoryIntervalStart_Type = TimeTicks
_WanVSeriesHistoryIntervalStart_Object = MibTableColumn
wanVSeriesHistoryIntervalStart = _WanVSeriesHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1, 3),
    _WanVSeriesHistoryIntervalStart_Type()
)
wanVSeriesHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesHistoryIntervalStart.setStatus("current")
_WanVSeriesHistoryDropEvents_Type = Counter64
_WanVSeriesHistoryDropEvents_Object = MibTableColumn
wanVSeriesHistoryDropEvents = _WanVSeriesHistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1, 4),
    _WanVSeriesHistoryDropEvents_Type()
)
wanVSeriesHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesHistoryDropEvents.setStatus("current")
_WanVSeriesHistoryInFrames_Type = Counter64
_WanVSeriesHistoryInFrames_Object = MibTableColumn
wanVSeriesHistoryInFrames = _WanVSeriesHistoryInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1, 5),
    _WanVSeriesHistoryInFrames_Type()
)
wanVSeriesHistoryInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesHistoryInFrames.setStatus("current")
_WanVSeriesHistoryOutFrames_Type = Counter64
_WanVSeriesHistoryOutFrames_Object = MibTableColumn
wanVSeriesHistoryOutFrames = _WanVSeriesHistoryOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1, 6),
    _WanVSeriesHistoryOutFrames_Type()
)
wanVSeriesHistoryOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesHistoryOutFrames.setStatus("current")
_WanVSeriesHistoryInOctets_Type = Counter64
_WanVSeriesHistoryInOctets_Object = MibTableColumn
wanVSeriesHistoryInOctets = _WanVSeriesHistoryInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1, 7),
    _WanVSeriesHistoryInOctets_Type()
)
wanVSeriesHistoryInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesHistoryInOctets.setStatus("current")
_WanVSeriesHistoryOutOctets_Type = Counter64
_WanVSeriesHistoryOutOctets_Object = MibTableColumn
wanVSeriesHistoryOutOctets = _WanVSeriesHistoryOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1, 8),
    _WanVSeriesHistoryOutOctets_Type()
)
wanVSeriesHistoryOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesHistoryOutOctets.setStatus("current")
_WanVSeriesHistoryInFCSs_Type = Counter64
_WanVSeriesHistoryInFCSs_Object = MibTableColumn
wanVSeriesHistoryInFCSs = _WanVSeriesHistoryInFCSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1, 9),
    _WanVSeriesHistoryInFCSs_Type()
)
wanVSeriesHistoryInFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesHistoryInFCSs.setStatus("current")
_WanVSeriesHistoryOutFCSs_Type = Counter64
_WanVSeriesHistoryOutFCSs_Object = MibTableColumn
wanVSeriesHistoryOutFCSs = _WanVSeriesHistoryOutFCSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1, 10),
    _WanVSeriesHistoryOutFCSs_Type()
)
wanVSeriesHistoryOutFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesHistoryOutFCSs.setStatus("current")
_WanVSeriesHistoryInOverruns_Type = Counter64
_WanVSeriesHistoryInOverruns_Object = MibTableColumn
wanVSeriesHistoryInOverruns = _WanVSeriesHistoryInOverruns_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1, 11),
    _WanVSeriesHistoryInOverruns_Type()
)
wanVSeriesHistoryInOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesHistoryInOverruns.setStatus("current")
_WanVSeriesHistoryOutOverruns_Type = Counter64
_WanVSeriesHistoryOutOverruns_Object = MibTableColumn
wanVSeriesHistoryOutOverruns = _WanVSeriesHistoryOutOverruns_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1, 12),
    _WanVSeriesHistoryOutOverruns_Type()
)
wanVSeriesHistoryOutOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesHistoryOutOverruns.setStatus("current")
_WanVSeriesHistoryInterruptedFrames_Type = Counter64
_WanVSeriesHistoryInterruptedFrames_Object = MibTableColumn
wanVSeriesHistoryInterruptedFrames = _WanVSeriesHistoryInterruptedFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1, 13),
    _WanVSeriesHistoryInterruptedFrames_Type()
)
wanVSeriesHistoryInterruptedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesHistoryInterruptedFrames.setStatus("current")
_WanVSeriesHistoryInAbortedFrames_Type = Counter64
_WanVSeriesHistoryInAbortedFrames_Object = MibTableColumn
wanVSeriesHistoryInAbortedFrames = _WanVSeriesHistoryInAbortedFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1, 14),
    _WanVSeriesHistoryInAbortedFrames_Type()
)
wanVSeriesHistoryInAbortedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesHistoryInAbortedFrames.setStatus("current")
_WanVSeriesHistoryOutAbortedFrames_Type = Counter64
_WanVSeriesHistoryOutAbortedFrames_Object = MibTableColumn
wanVSeriesHistoryOutAbortedFrames = _WanVSeriesHistoryOutAbortedFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1, 15),
    _WanVSeriesHistoryOutAbortedFrames_Type()
)
wanVSeriesHistoryOutAbortedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesHistoryOutAbortedFrames.setStatus("current")


class _WanVSeriesHistoryInUtilization_Type(Integer32):
    """Custom type wanVSeriesHistoryInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanVSeriesHistoryInUtilization_Type.__name__ = "Integer32"
_WanVSeriesHistoryInUtilization_Object = MibTableColumn
wanVSeriesHistoryInUtilization = _WanVSeriesHistoryInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1, 16),
    _WanVSeriesHistoryInUtilization_Type()
)
wanVSeriesHistoryInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesHistoryInUtilization.setStatus("current")


class _WanVSeriesHistoryOutUtilization_Type(Integer32):
    """Custom type wanVSeriesHistoryOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanVSeriesHistoryOutUtilization_Type.__name__ = "Integer32"
_WanVSeriesHistoryOutUtilization_Object = MibTableColumn
wanVSeriesHistoryOutUtilization = _WanVSeriesHistoryOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 2, 1, 17),
    _WanVSeriesHistoryOutUtilization_Type()
)
wanVSeriesHistoryOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanVSeriesHistoryOutUtilization.setStatus("current")
_WanHssiHistoryTable_Object = MibTable
wanHssiHistoryTable = _WanHssiHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3)
)
if mibBuilder.loadTexts:
    wanHssiHistoryTable.setStatus("deprecated")
_WanHssiHistoryEntry_Object = MibTableRow
wanHssiHistoryEntry = _WanHssiHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1)
)
wanHssiHistoryEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanHssiHistoryIndex"),
    (0, "WANSTATS-MIB", "wanHssiHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    wanHssiHistoryEntry.setStatus("deprecated")


class _WanHssiHistoryIndex_Type(Integer32):
    """Custom type wanHssiHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanHssiHistoryIndex_Type.__name__ = "Integer32"
_WanHssiHistoryIndex_Object = MibTableColumn
wanHssiHistoryIndex = _WanHssiHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 1),
    _WanHssiHistoryIndex_Type()
)
wanHssiHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanHssiHistoryIndex.setStatus("deprecated")


class _WanHssiHistorySampleIndex_Type(Integer32):
    """Custom type wanHssiHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WanHssiHistorySampleIndex_Type.__name__ = "Integer32"
_WanHssiHistorySampleIndex_Object = MibTableColumn
wanHssiHistorySampleIndex = _WanHssiHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 2),
    _WanHssiHistorySampleIndex_Type()
)
wanHssiHistorySampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanHssiHistorySampleIndex.setStatus("deprecated")
_WanHssiHistoryIntervalStart_Type = TimeTicks
_WanHssiHistoryIntervalStart_Object = MibTableColumn
wanHssiHistoryIntervalStart = _WanHssiHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 3),
    _WanHssiHistoryIntervalStart_Type()
)
wanHssiHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryIntervalStart.setStatus("deprecated")
_WanHssiHistoryDropEvents_Type = Counter64
_WanHssiHistoryDropEvents_Object = MibTableColumn
wanHssiHistoryDropEvents = _WanHssiHistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 4),
    _WanHssiHistoryDropEvents_Type()
)
wanHssiHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryDropEvents.setStatus("deprecated")
_WanHssiHistoryInFrames_Type = Counter64
_WanHssiHistoryInFrames_Object = MibTableColumn
wanHssiHistoryInFrames = _WanHssiHistoryInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 5),
    _WanHssiHistoryInFrames_Type()
)
wanHssiHistoryInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryInFrames.setStatus("deprecated")
_WanHssiHistoryOutFrames_Type = Counter64
_WanHssiHistoryOutFrames_Object = MibTableColumn
wanHssiHistoryOutFrames = _WanHssiHistoryOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 6),
    _WanHssiHistoryOutFrames_Type()
)
wanHssiHistoryOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryOutFrames.setStatus("deprecated")
_WanHssiHistoryInOctets_Type = Counter64
_WanHssiHistoryInOctets_Object = MibTableColumn
wanHssiHistoryInOctets = _WanHssiHistoryInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 7),
    _WanHssiHistoryInOctets_Type()
)
wanHssiHistoryInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryInOctets.setStatus("deprecated")
_WanHssiHistoryOutOctets_Type = Counter64
_WanHssiHistoryOutOctets_Object = MibTableColumn
wanHssiHistoryOutOctets = _WanHssiHistoryOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 8),
    _WanHssiHistoryOutOctets_Type()
)
wanHssiHistoryOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryOutOctets.setStatus("deprecated")
_WanHssiHistoryRxLongFrames_Type = Counter64
_WanHssiHistoryRxLongFrames_Object = MibTableColumn
wanHssiHistoryRxLongFrames = _WanHssiHistoryRxLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 9),
    _WanHssiHistoryRxLongFrames_Type()
)
wanHssiHistoryRxLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryRxLongFrames.setStatus("deprecated")
_WanHssiHistoryRxCrcErrors_Type = Counter64
_WanHssiHistoryRxCrcErrors_Object = MibTableColumn
wanHssiHistoryRxCrcErrors = _WanHssiHistoryRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 10),
    _WanHssiHistoryRxCrcErrors_Type()
)
wanHssiHistoryRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryRxCrcErrors.setStatus("deprecated")
_WanHssiHistoryRxOverruns_Type = Counter64
_WanHssiHistoryRxOverruns_Object = MibTableColumn
wanHssiHistoryRxOverruns = _WanHssiHistoryRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 11),
    _WanHssiHistoryRxOverruns_Type()
)
wanHssiHistoryRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryRxOverruns.setStatus("deprecated")
_WanHssiHistoryRxAborts_Type = Counter64
_WanHssiHistoryRxAborts_Object = MibTableColumn
wanHssiHistoryRxAborts = _WanHssiHistoryRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 12),
    _WanHssiHistoryRxAborts_Type()
)
wanHssiHistoryRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryRxAborts.setStatus("deprecated")
_WanHssiHistoryTxAborts_Type = Counter64
_WanHssiHistoryTxAborts_Object = MibTableColumn
wanHssiHistoryTxAborts = _WanHssiHistoryTxAborts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 13),
    _WanHssiHistoryTxAborts_Type()
)
wanHssiHistoryTxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryTxAborts.setStatus("deprecated")
_WanHssiHistoryTxUnderruns_Type = Counter64
_WanHssiHistoryTxUnderruns_Object = MibTableColumn
wanHssiHistoryTxUnderruns = _WanHssiHistoryTxUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 14),
    _WanHssiHistoryTxUnderruns_Type()
)
wanHssiHistoryTxUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryTxUnderruns.setStatus("deprecated")
_WanHssiHistoryRxRingErrors_Type = Counter64
_WanHssiHistoryRxRingErrors_Object = MibTableColumn
wanHssiHistoryRxRingErrors = _WanHssiHistoryRxRingErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 15),
    _WanHssiHistoryRxRingErrors_Type()
)
wanHssiHistoryRxRingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryRxRingErrors.setStatus("deprecated")
_WanHssiHistoryRxRingOverruns_Type = Counter64
_WanHssiHistoryRxRingOverruns_Object = MibTableColumn
wanHssiHistoryRxRingOverruns = _WanHssiHistoryRxRingOverruns_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 16),
    _WanHssiHistoryRxRingOverruns_Type()
)
wanHssiHistoryRxRingOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryRxRingOverruns.setStatus("deprecated")
_WanHssiHistoryTxRingErrors_Type = Counter64
_WanHssiHistoryTxRingErrors_Object = MibTableColumn
wanHssiHistoryTxRingErrors = _WanHssiHistoryTxRingErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 17),
    _WanHssiHistoryTxRingErrors_Type()
)
wanHssiHistoryTxRingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryTxRingErrors.setStatus("deprecated")
_WanHssiHistoryPortOpErrors_Type = Counter64
_WanHssiHistoryPortOpErrors_Object = MibTableColumn
wanHssiHistoryPortOpErrors = _WanHssiHistoryPortOpErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 18),
    _WanHssiHistoryPortOpErrors_Type()
)
wanHssiHistoryPortOpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryPortOpErrors.setStatus("deprecated")
_WanHssiHistoryTxCmplProcessings_Type = Counter64
_WanHssiHistoryTxCmplProcessings_Object = MibTableColumn
wanHssiHistoryTxCmplProcessings = _WanHssiHistoryTxCmplProcessings_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 19),
    _WanHssiHistoryTxCmplProcessings_Type()
)
wanHssiHistoryTxCmplProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryTxCmplProcessings.setStatus("deprecated")


class _WanHssiHistoryInUtilization_Type(Integer32):
    """Custom type wanHssiHistoryInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanHssiHistoryInUtilization_Type.__name__ = "Integer32"
_WanHssiHistoryInUtilization_Object = MibTableColumn
wanHssiHistoryInUtilization = _WanHssiHistoryInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 20),
    _WanHssiHistoryInUtilization_Type()
)
wanHssiHistoryInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryInUtilization.setStatus("deprecated")


class _WanHssiHistoryOutUtilization_Type(Integer32):
    """Custom type wanHssiHistoryOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanHssiHistoryOutUtilization_Type.__name__ = "Integer32"
_WanHssiHistoryOutUtilization_Object = MibTableColumn
wanHssiHistoryOutUtilization = _WanHssiHistoryOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 3, 1, 21),
    _WanHssiHistoryOutUtilization_Type()
)
wanHssiHistoryOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHssiHistoryOutUtilization.setStatus("deprecated")
_WanT3E3HistoryTable_Object = MibTable
wanT3E3HistoryTable = _WanT3E3HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4)
)
if mibBuilder.loadTexts:
    wanT3E3HistoryTable.setStatus("current")
_WanT3E3HistoryEntry_Object = MibTableRow
wanT3E3HistoryEntry = _WanT3E3HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1)
)
wanT3E3HistoryEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanT3E3HistoryIndex"),
    (0, "WANSTATS-MIB", "wanT3E3HistorySampleIndex"),
)
if mibBuilder.loadTexts:
    wanT3E3HistoryEntry.setStatus("current")


class _WanT3E3HistoryIndex_Type(Integer32):
    """Custom type wanT3E3HistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanT3E3HistoryIndex_Type.__name__ = "Integer32"
_WanT3E3HistoryIndex_Object = MibTableColumn
wanT3E3HistoryIndex = _WanT3E3HistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 1),
    _WanT3E3HistoryIndex_Type()
)
wanT3E3HistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanT3E3HistoryIndex.setStatus("current")


class _WanT3E3HistorySampleIndex_Type(Integer32):
    """Custom type wanT3E3HistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WanT3E3HistorySampleIndex_Type.__name__ = "Integer32"
_WanT3E3HistorySampleIndex_Object = MibTableColumn
wanT3E3HistorySampleIndex = _WanT3E3HistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 2),
    _WanT3E3HistorySampleIndex_Type()
)
wanT3E3HistorySampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanT3E3HistorySampleIndex.setStatus("current")
_WanT3E3HistoryIntervalStart_Type = TimeTicks
_WanT3E3HistoryIntervalStart_Object = MibTableColumn
wanT3E3HistoryIntervalStart = _WanT3E3HistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 3),
    _WanT3E3HistoryIntervalStart_Type()
)
wanT3E3HistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryIntervalStart.setStatus("current")
_WanT3E3HistoryDropEvents_Type = Counter64
_WanT3E3HistoryDropEvents_Object = MibTableColumn
wanT3E3HistoryDropEvents = _WanT3E3HistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 4),
    _WanT3E3HistoryDropEvents_Type()
)
wanT3E3HistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryDropEvents.setStatus("current")
_WanT3E3HistoryInFrames_Type = Counter64
_WanT3E3HistoryInFrames_Object = MibTableColumn
wanT3E3HistoryInFrames = _WanT3E3HistoryInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 5),
    _WanT3E3HistoryInFrames_Type()
)
wanT3E3HistoryInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryInFrames.setStatus("current")
_WanT3E3HistoryOutFrames_Type = Counter64
_WanT3E3HistoryOutFrames_Object = MibTableColumn
wanT3E3HistoryOutFrames = _WanT3E3HistoryOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 6),
    _WanT3E3HistoryOutFrames_Type()
)
wanT3E3HistoryOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryOutFrames.setStatus("current")
_WanT3E3HistoryInOctets_Type = Counter64
_WanT3E3HistoryInOctets_Object = MibTableColumn
wanT3E3HistoryInOctets = _WanT3E3HistoryInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 7),
    _WanT3E3HistoryInOctets_Type()
)
wanT3E3HistoryInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryInOctets.setStatus("current")
_WanT3E3HistoryOutOctets_Type = Counter64
_WanT3E3HistoryOutOctets_Object = MibTableColumn
wanT3E3HistoryOutOctets = _WanT3E3HistoryOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 8),
    _WanT3E3HistoryOutOctets_Type()
)
wanT3E3HistoryOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryOutOctets.setStatus("current")
_WanT3E3HistoryPESs_Type = Counter64
_WanT3E3HistoryPESs_Object = MibTableColumn
wanT3E3HistoryPESs = _WanT3E3HistoryPESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 9),
    _WanT3E3HistoryPESs_Type()
)
wanT3E3HistoryPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryPESs.setStatus("current")
_WanT3E3HistoryPSESs_Type = Counter64
_WanT3E3HistoryPSESs_Object = MibTableColumn
wanT3E3HistoryPSESs = _WanT3E3HistoryPSESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 10),
    _WanT3E3HistoryPSESs_Type()
)
wanT3E3HistoryPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryPSESs.setStatus("current")
_WanT3E3HistoryOOFs_Type = Counter64
_WanT3E3HistoryOOFs_Object = MibTableColumn
wanT3E3HistoryOOFs = _WanT3E3HistoryOOFs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 11),
    _WanT3E3HistoryOOFs_Type()
)
wanT3E3HistoryOOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryOOFs.setStatus("current")
_WanT3E3HistorySEFSs_Type = Counter64
_WanT3E3HistorySEFSs_Object = MibTableColumn
wanT3E3HistorySEFSs = _WanT3E3HistorySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 12),
    _WanT3E3HistorySEFSs_Type()
)
wanT3E3HistorySEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistorySEFSs.setStatus("current")
_WanT3E3HistoryUASs_Type = Counter64
_WanT3E3HistoryUASs_Object = MibTableColumn
wanT3E3HistoryUASs = _WanT3E3HistoryUASs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 13),
    _WanT3E3HistoryUASs_Type()
)
wanT3E3HistoryUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryUASs.setStatus("current")
_WanT3E3HistoryLCVs_Type = Counter64
_WanT3E3HistoryLCVs_Object = MibTableColumn
wanT3E3HistoryLCVs = _WanT3E3HistoryLCVs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 14),
    _WanT3E3HistoryLCVs_Type()
)
wanT3E3HistoryLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryLCVs.setStatus("current")
_WanT3E3HistoryPCVs_Type = Counter64
_WanT3E3HistoryPCVs_Object = MibTableColumn
wanT3E3HistoryPCVs = _WanT3E3HistoryPCVs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 15),
    _WanT3E3HistoryPCVs_Type()
)
wanT3E3HistoryPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryPCVs.setStatus("current")
_WanT3E3HistoryLESs_Type = Counter64
_WanT3E3HistoryLESs_Object = MibTableColumn
wanT3E3HistoryLESs = _WanT3E3HistoryLESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 16),
    _WanT3E3HistoryLESs_Type()
)
wanT3E3HistoryLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryLESs.setStatus("current")
_WanT3E3HistoryCCVs_Type = Counter64
_WanT3E3HistoryCCVs_Object = MibTableColumn
wanT3E3HistoryCCVs = _WanT3E3HistoryCCVs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 17),
    _WanT3E3HistoryCCVs_Type()
)
wanT3E3HistoryCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryCCVs.setStatus("current")
_WanT3E3HistoryCESs_Type = Counter64
_WanT3E3HistoryCESs_Object = MibTableColumn
wanT3E3HistoryCESs = _WanT3E3HistoryCESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 18),
    _WanT3E3HistoryCESs_Type()
)
wanT3E3HistoryCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryCESs.setStatus("current")
_WanT3E3HistoryCSESs_Type = Counter64
_WanT3E3HistoryCSESs_Object = MibTableColumn
wanT3E3HistoryCSESs = _WanT3E3HistoryCSESs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 19),
    _WanT3E3HistoryCSESs_Type()
)
wanT3E3HistoryCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryCSESs.setStatus("current")
_WanT3E3HistoryRAIs_Type = Counter64
_WanT3E3HistoryRAIs_Object = MibTableColumn
wanT3E3HistoryRAIs = _WanT3E3HistoryRAIs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 20),
    _WanT3E3HistoryRAIs_Type()
)
wanT3E3HistoryRAIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryRAIs.setStatus("current")
_WanT3E3HistoryAISs_Type = Counter64
_WanT3E3HistoryAISs_Object = MibTableColumn
wanT3E3HistoryAISs = _WanT3E3HistoryAISs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 21),
    _WanT3E3HistoryAISs_Type()
)
wanT3E3HistoryAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryAISs.setStatus("current")
_WanT3E3HistoryLOFs_Type = Counter64
_WanT3E3HistoryLOFs_Object = MibTableColumn
wanT3E3HistoryLOFs = _WanT3E3HistoryLOFs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 22),
    _WanT3E3HistoryLOFs_Type()
)
wanT3E3HistoryLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryLOFs.setStatus("current")
_WanT3E3HistoryLOSs_Type = Counter64
_WanT3E3HistoryLOSs_Object = MibTableColumn
wanT3E3HistoryLOSs = _WanT3E3HistoryLOSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 23),
    _WanT3E3HistoryLOSs_Type()
)
wanT3E3HistoryLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryLOSs.setStatus("current")


class _WanT3E3HistoryInUtilization_Type(Integer32):
    """Custom type wanT3E3HistoryInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanT3E3HistoryInUtilization_Type.__name__ = "Integer32"
_WanT3E3HistoryInUtilization_Object = MibTableColumn
wanT3E3HistoryInUtilization = _WanT3E3HistoryInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 24),
    _WanT3E3HistoryInUtilization_Type()
)
wanT3E3HistoryInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryInUtilization.setStatus("current")


class _WanT3E3HistoryOutUtilization_Type(Integer32):
    """Custom type wanT3E3HistoryOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanT3E3HistoryOutUtilization_Type.__name__ = "Integer32"
_WanT3E3HistoryOutUtilization_Object = MibTableColumn
wanT3E3HistoryOutUtilization = _WanT3E3HistoryOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 4, 1, 25),
    _WanT3E3HistoryOutUtilization_Type()
)
wanT3E3HistoryOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanT3E3HistoryOutUtilization.setStatus("current")
_WanAtmHistoryTable_Object = MibTable
wanAtmHistoryTable = _WanAtmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5)
)
if mibBuilder.loadTexts:
    wanAtmHistoryTable.setStatus("current")
_WanAtmHistoryEntry_Object = MibTableRow
wanAtmHistoryEntry = _WanAtmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1)
)
wanAtmHistoryEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanAtmHistoryIndex"),
    (0, "WANSTATS-MIB", "wanAtmHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    wanAtmHistoryEntry.setStatus("current")


class _WanAtmHistoryIndex_Type(Integer32):
    """Custom type wanAtmHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanAtmHistoryIndex_Type.__name__ = "Integer32"
_WanAtmHistoryIndex_Object = MibTableColumn
wanAtmHistoryIndex = _WanAtmHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 1),
    _WanAtmHistoryIndex_Type()
)
wanAtmHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanAtmHistoryIndex.setStatus("current")


class _WanAtmHistorySampleIndex_Type(Integer32):
    """Custom type wanAtmHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WanAtmHistorySampleIndex_Type.__name__ = "Integer32"
_WanAtmHistorySampleIndex_Object = MibTableColumn
wanAtmHistorySampleIndex = _WanAtmHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 2),
    _WanAtmHistorySampleIndex_Type()
)
wanAtmHistorySampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanAtmHistorySampleIndex.setStatus("current")
_WanAtmHistoryIntervalStart_Type = TimeTicks
_WanAtmHistoryIntervalStart_Object = MibTableColumn
wanAtmHistoryIntervalStart = _WanAtmHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 3),
    _WanAtmHistoryIntervalStart_Type()
)
wanAtmHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryIntervalStart.setStatus("current")
_WanAtmHistoryDropEvents_Type = Counter64
_WanAtmHistoryDropEvents_Object = MibTableColumn
wanAtmHistoryDropEvents = _WanAtmHistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 4),
    _WanAtmHistoryDropEvents_Type()
)
wanAtmHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryDropEvents.setStatus("current")
_WanAtmHistoryInCells_Type = Counter64
_WanAtmHistoryInCells_Object = MibTableColumn
wanAtmHistoryInCells = _WanAtmHistoryInCells_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 5),
    _WanAtmHistoryInCells_Type()
)
wanAtmHistoryInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryInCells.setStatus("current")
_WanAtmHistoryOutCells_Type = Counter64
_WanAtmHistoryOutCells_Object = MibTableColumn
wanAtmHistoryOutCells = _WanAtmHistoryOutCells_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 6),
    _WanAtmHistoryOutCells_Type()
)
wanAtmHistoryOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryOutCells.setStatus("current")
_WanAtmHistoryInCLP1_Type = Counter64
_WanAtmHistoryInCLP1_Object = MibTableColumn
wanAtmHistoryInCLP1 = _WanAtmHistoryInCLP1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 7),
    _WanAtmHistoryInCLP1_Type()
)
wanAtmHistoryInCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryInCLP1.setStatus("current")
_WanAtmHistoryOutCLP1_Type = Counter64
_WanAtmHistoryOutCLP1_Object = MibTableColumn
wanAtmHistoryOutCLP1 = _WanAtmHistoryOutCLP1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 8),
    _WanAtmHistoryOutCLP1_Type()
)
wanAtmHistoryOutCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryOutCLP1.setStatus("current")
_WanAtmHistoryConnectionEvents_Type = Counter64
_WanAtmHistoryConnectionEvents_Object = MibTableColumn
wanAtmHistoryConnectionEvents = _WanAtmHistoryConnectionEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 9),
    _WanAtmHistoryConnectionEvents_Type()
)
wanAtmHistoryConnectionEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryConnectionEvents.setStatus("current")
_WanAtmHistoryErroredPDUs_Type = Counter64
_WanAtmHistoryErroredPDUs_Object = MibTableColumn
wanAtmHistoryErroredPDUs = _WanAtmHistoryErroredPDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 10),
    _WanAtmHistoryErroredPDUs_Type()
)
wanAtmHistoryErroredPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryErroredPDUs.setStatus("current")
_WanAtmHistorySetupAttempts_Type = Counter64
_WanAtmHistorySetupAttempts_Object = MibTableColumn
wanAtmHistorySetupAttempts = _WanAtmHistorySetupAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 11),
    _WanAtmHistorySetupAttempts_Type()
)
wanAtmHistorySetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistorySetupAttempts.setStatus("current")
_WanAtmHistoryInRoutesUnavailable_Type = Counter64
_WanAtmHistoryInRoutesUnavailable_Object = MibTableColumn
wanAtmHistoryInRoutesUnavailable = _WanAtmHistoryInRoutesUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 12),
    _WanAtmHistoryInRoutesUnavailable_Type()
)
wanAtmHistoryInRoutesUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryInRoutesUnavailable.setStatus("current")
_WanAtmHistoryOutRoutesUnavailable_Type = Counter64
_WanAtmHistoryOutRoutesUnavailable_Object = MibTableColumn
wanAtmHistoryOutRoutesUnavailable = _WanAtmHistoryOutRoutesUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 13),
    _WanAtmHistoryOutRoutesUnavailable_Type()
)
wanAtmHistoryOutRoutesUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryOutRoutesUnavailable.setStatus("current")
_WanAtmHistoryInResourcesUnavailable_Type = Counter64
_WanAtmHistoryInResourcesUnavailable_Object = MibTableColumn
wanAtmHistoryInResourcesUnavailable = _WanAtmHistoryInResourcesUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 14),
    _WanAtmHistoryInResourcesUnavailable_Type()
)
wanAtmHistoryInResourcesUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryInResourcesUnavailable.setStatus("current")
_WanAtmHistoryOutResourcesUnavailable_Type = Counter64
_WanAtmHistoryOutResourcesUnavailable_Object = MibTableColumn
wanAtmHistoryOutResourcesUnavailable = _WanAtmHistoryOutResourcesUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 15),
    _WanAtmHistoryOutResourcesUnavailable_Type()
)
wanAtmHistoryOutResourcesUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryOutResourcesUnavailable.setStatus("current")
_WanAtmHistoryInUnsuccessfulCalls_Type = Counter64
_WanAtmHistoryInUnsuccessfulCalls_Object = MibTableColumn
wanAtmHistoryInUnsuccessfulCalls = _WanAtmHistoryInUnsuccessfulCalls_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 16),
    _WanAtmHistoryInUnsuccessfulCalls_Type()
)
wanAtmHistoryInUnsuccessfulCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryInUnsuccessfulCalls.setStatus("current")
_WanAtmHistoryOutUnsuccessfulCalls_Type = Counter64
_WanAtmHistoryOutUnsuccessfulCalls_Object = MibTableColumn
wanAtmHistoryOutUnsuccessfulCalls = _WanAtmHistoryOutUnsuccessfulCalls_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 17),
    _WanAtmHistoryOutUnsuccessfulCalls_Type()
)
wanAtmHistoryOutUnsuccessfulCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryOutUnsuccessfulCalls.setStatus("current")
_WanAtmHistoryInIncorrectMsgs_Type = Counter64
_WanAtmHistoryInIncorrectMsgs_Object = MibTableColumn
wanAtmHistoryInIncorrectMsgs = _WanAtmHistoryInIncorrectMsgs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 18),
    _WanAtmHistoryInIncorrectMsgs_Type()
)
wanAtmHistoryInIncorrectMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryInIncorrectMsgs.setStatus("current")
_WanAtmHistoryOutIncorrectMsgs_Type = Counter64
_WanAtmHistoryOutIncorrectMsgs_Object = MibTableColumn
wanAtmHistoryOutIncorrectMsgs = _WanAtmHistoryOutIncorrectMsgs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 19),
    _WanAtmHistoryOutIncorrectMsgs_Type()
)
wanAtmHistoryOutIncorrectMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryOutIncorrectMsgs.setStatus("current")
_WanAtmHistoryInPartyEvents_Type = Counter64
_WanAtmHistoryInPartyEvents_Object = MibTableColumn
wanAtmHistoryInPartyEvents = _WanAtmHistoryInPartyEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 20),
    _WanAtmHistoryInPartyEvents_Type()
)
wanAtmHistoryInPartyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryInPartyEvents.setStatus("current")
_WanAtmHistoryOutPartyEvents_Type = Counter64
_WanAtmHistoryOutPartyEvents_Object = MibTableColumn
wanAtmHistoryOutPartyEvents = _WanAtmHistoryOutPartyEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 21),
    _WanAtmHistoryOutPartyEvents_Type()
)
wanAtmHistoryOutPartyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryOutPartyEvents.setStatus("current")
_WanAtmHistoryInExpiries_Type = Counter64
_WanAtmHistoryInExpiries_Object = MibTableColumn
wanAtmHistoryInExpiries = _WanAtmHistoryInExpiries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 22),
    _WanAtmHistoryInExpiries_Type()
)
wanAtmHistoryInExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryInExpiries.setStatus("current")
_WanAtmHistoryOutExpiries_Type = Counter64
_WanAtmHistoryOutExpiries_Object = MibTableColumn
wanAtmHistoryOutExpiries = _WanAtmHistoryOutExpiries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 23),
    _WanAtmHistoryOutExpiries_Type()
)
wanAtmHistoryOutExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryOutExpiries.setStatus("current")
_WanAtmHistoryInRestartErrors_Type = Counter64
_WanAtmHistoryInRestartErrors_Object = MibTableColumn
wanAtmHistoryInRestartErrors = _WanAtmHistoryInRestartErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 24),
    _WanAtmHistoryInRestartErrors_Type()
)
wanAtmHistoryInRestartErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryInRestartErrors.setStatus("current")
_WanAtmHistoryOutRestartErrors_Type = Counter64
_WanAtmHistoryOutRestartErrors_Object = MibTableColumn
wanAtmHistoryOutRestartErrors = _WanAtmHistoryOutRestartErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 25),
    _WanAtmHistoryOutRestartErrors_Type()
)
wanAtmHistoryOutRestartErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryOutRestartErrors.setStatus("current")
_WanAtmHistoryInSVCs_Type = Counter64
_WanAtmHistoryInSVCs_Object = MibTableColumn
wanAtmHistoryInSVCs = _WanAtmHistoryInSVCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 26),
    _WanAtmHistoryInSVCs_Type()
)
wanAtmHistoryInSVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryInSVCs.setStatus("current")
_WanAtmHistoryOutSVCs_Type = Counter64
_WanAtmHistoryOutSVCs_Object = MibTableColumn
wanAtmHistoryOutSVCs = _WanAtmHistoryOutSVCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 27),
    _WanAtmHistoryOutSVCs_Type()
)
wanAtmHistoryOutSVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryOutSVCs.setStatus("current")
_WanAtmHistoryInOCDs_Type = Counter64
_WanAtmHistoryInOCDs_Object = MibTableColumn
wanAtmHistoryInOCDs = _WanAtmHistoryInOCDs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 28),
    _WanAtmHistoryInOCDs_Type()
)
wanAtmHistoryInOCDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryInOCDs.setStatus("current")
_WanAtmHistoryOutOCDs_Type = Counter64
_WanAtmHistoryOutOCDs_Object = MibTableColumn
wanAtmHistoryOutOCDs = _WanAtmHistoryOutOCDs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 29),
    _WanAtmHistoryOutOCDs_Type()
)
wanAtmHistoryOutOCDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryOutOCDs.setStatus("current")
_WanAtmHistoryInLOCs_Type = Counter64
_WanAtmHistoryInLOCs_Object = MibTableColumn
wanAtmHistoryInLOCs = _WanAtmHistoryInLOCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 30),
    _WanAtmHistoryInLOCs_Type()
)
wanAtmHistoryInLOCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryInLOCs.setStatus("current")
_WanAtmHistoryOutLOCs_Type = Counter64
_WanAtmHistoryOutLOCs_Object = MibTableColumn
wanAtmHistoryOutLOCs = _WanAtmHistoryOutLOCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 31),
    _WanAtmHistoryOutLOCs_Type()
)
wanAtmHistoryOutLOCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryOutLOCs.setStatus("current")
_WanAtmHistoryInLOFs_Type = Counter64
_WanAtmHistoryInLOFs_Object = MibTableColumn
wanAtmHistoryInLOFs = _WanAtmHistoryInLOFs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 32),
    _WanAtmHistoryInLOFs_Type()
)
wanAtmHistoryInLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryInLOFs.setStatus("current")
_WanAtmHistoryOutLOFs_Type = Counter64
_WanAtmHistoryOutLOFs_Object = MibTableColumn
wanAtmHistoryOutLOFs = _WanAtmHistoryOutLOFs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 33),
    _WanAtmHistoryOutLOFs_Type()
)
wanAtmHistoryOutLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryOutLOFs.setStatus("current")
_WanAtmHistoryInLOPs_Type = Counter64
_WanAtmHistoryInLOPs_Object = MibTableColumn
wanAtmHistoryInLOPs = _WanAtmHistoryInLOPs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 34),
    _WanAtmHistoryInLOPs_Type()
)
wanAtmHistoryInLOPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryInLOPs.setStatus("current")
_WanAtmHistoryOutLOPs_Type = Counter64
_WanAtmHistoryOutLOPs_Object = MibTableColumn
wanAtmHistoryOutLOPs = _WanAtmHistoryOutLOPs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 35),
    _WanAtmHistoryOutLOPs_Type()
)
wanAtmHistoryOutLOPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryOutLOPs.setStatus("current")
_WanAtmHistoryInLOSs_Type = Counter64
_WanAtmHistoryInLOSs_Object = MibTableColumn
wanAtmHistoryInLOSs = _WanAtmHistoryInLOSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 36),
    _WanAtmHistoryInLOSs_Type()
)
wanAtmHistoryInLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryInLOSs.setStatus("current")
_WanAtmHistoryOutLOSs_Type = Counter64
_WanAtmHistoryOutLOSs_Object = MibTableColumn
wanAtmHistoryOutLOSs = _WanAtmHistoryOutLOSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 37),
    _WanAtmHistoryOutLOSs_Type()
)
wanAtmHistoryOutLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryOutLOSs.setStatus("current")


class _WanAtmHistoryInUtilization_Type(Integer32):
    """Custom type wanAtmHistoryInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanAtmHistoryInUtilization_Type.__name__ = "Integer32"
_WanAtmHistoryInUtilization_Object = MibTableColumn
wanAtmHistoryInUtilization = _WanAtmHistoryInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 38),
    _WanAtmHistoryInUtilization_Type()
)
wanAtmHistoryInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryInUtilization.setStatus("current")


class _WanAtmHistoryOutUtilization_Type(Integer32):
    """Custom type wanAtmHistoryOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanAtmHistoryOutUtilization_Type.__name__ = "Integer32"
_WanAtmHistoryOutUtilization_Object = MibTableColumn
wanAtmHistoryOutUtilization = _WanAtmHistoryOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 1, 5, 1, 39),
    _WanAtmHistoryOutUtilization_Type()
)
wanAtmHistoryOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAtmHistoryOutUtilization.setStatus("current")
_WanProtocolHistory_ObjectIdentity = ObjectIdentity
wanProtocolHistory = _WanProtocolHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2)
)
_WanX25HistoryTable_Object = MibTable
wanX25HistoryTable = _WanX25HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1)
)
if mibBuilder.loadTexts:
    wanX25HistoryTable.setStatus("current")
_WanX25HistoryEntry_Object = MibTableRow
wanX25HistoryEntry = _WanX25HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1)
)
wanX25HistoryEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanX25HistoryIndex"),
    (0, "WANSTATS-MIB", "wanX25HistorySampleIndex"),
)
if mibBuilder.loadTexts:
    wanX25HistoryEntry.setStatus("current")


class _WanX25HistoryIndex_Type(Integer32):
    """Custom type wanX25HistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanX25HistoryIndex_Type.__name__ = "Integer32"
_WanX25HistoryIndex_Object = MibTableColumn
wanX25HistoryIndex = _WanX25HistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 1),
    _WanX25HistoryIndex_Type()
)
wanX25HistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanX25HistoryIndex.setStatus("current")


class _WanX25HistorySampleIndex_Type(Integer32):
    """Custom type wanX25HistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WanX25HistorySampleIndex_Type.__name__ = "Integer32"
_WanX25HistorySampleIndex_Object = MibTableColumn
wanX25HistorySampleIndex = _WanX25HistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 2),
    _WanX25HistorySampleIndex_Type()
)
wanX25HistorySampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanX25HistorySampleIndex.setStatus("current")
_WanX25HistoryIntervalStart_Type = TimeTicks
_WanX25HistoryIntervalStart_Object = MibTableColumn
wanX25HistoryIntervalStart = _WanX25HistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 3),
    _WanX25HistoryIntervalStart_Type()
)
wanX25HistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryIntervalStart.setStatus("current")
_WanX25HistoryDropEvents_Type = Counter64
_WanX25HistoryDropEvents_Object = MibTableColumn
wanX25HistoryDropEvents = _WanX25HistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 4),
    _WanX25HistoryDropEvents_Type()
)
wanX25HistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryDropEvents.setStatus("current")
_WanX25HistoryInFrames_Type = Counter64
_WanX25HistoryInFrames_Object = MibTableColumn
wanX25HistoryInFrames = _WanX25HistoryInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 5),
    _WanX25HistoryInFrames_Type()
)
wanX25HistoryInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryInFrames.setStatus("current")
_WanX25HistoryOutFrames_Type = Counter64
_WanX25HistoryOutFrames_Object = MibTableColumn
wanX25HistoryOutFrames = _WanX25HistoryOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 6),
    _WanX25HistoryOutFrames_Type()
)
wanX25HistoryOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryOutFrames.setStatus("current")
_WanX25HistoryInOctets_Type = Counter64
_WanX25HistoryInOctets_Object = MibTableColumn
wanX25HistoryInOctets = _WanX25HistoryInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 7),
    _WanX25HistoryInOctets_Type()
)
wanX25HistoryInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryInOctets.setStatus("current")
_WanX25HistoryOutOctets_Type = Counter64
_WanX25HistoryOutOctets_Object = MibTableColumn
wanX25HistoryOutOctets = _WanX25HistoryOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 8),
    _WanX25HistoryOutOctets_Type()
)
wanX25HistoryOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryOutOctets.setStatus("current")
_WanX25HistoryInRejects_Type = Counter64
_WanX25HistoryInRejects_Object = MibTableColumn
wanX25HistoryInRejects = _WanX25HistoryInRejects_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 9),
    _WanX25HistoryInRejects_Type()
)
wanX25HistoryInRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryInRejects.setStatus("current")
_WanX25HistoryOutRejects_Type = Counter64
_WanX25HistoryOutRejects_Object = MibTableColumn
wanX25HistoryOutRejects = _WanX25HistoryOutRejects_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 10),
    _WanX25HistoryOutRejects_Type()
)
wanX25HistoryOutRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryOutRejects.setStatus("current")
_WanX25HistoryInAttempts_Type = Counter64
_WanX25HistoryInAttempts_Object = MibTableColumn
wanX25HistoryInAttempts = _WanX25HistoryInAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 11),
    _WanX25HistoryInAttempts_Type()
)
wanX25HistoryInAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryInAttempts.setStatus("current")
_WanX25HistoryOutAttempts_Type = Counter64
_WanX25HistoryOutAttempts_Object = MibTableColumn
wanX25HistoryOutAttempts = _WanX25HistoryOutAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 12),
    _WanX25HistoryOutAttempts_Type()
)
wanX25HistoryOutAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryOutAttempts.setStatus("current")
_WanX25HistoryInFailures_Type = Counter64
_WanX25HistoryInFailures_Object = MibTableColumn
wanX25HistoryInFailures = _WanX25HistoryInFailures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 13),
    _WanX25HistoryInFailures_Type()
)
wanX25HistoryInFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryInFailures.setStatus("current")
_WanX25HistoryOutFailures_Type = Counter64
_WanX25HistoryOutFailures_Object = MibTableColumn
wanX25HistoryOutFailures = _WanX25HistoryOutFailures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 14),
    _WanX25HistoryOutFailures_Type()
)
wanX25HistoryOutFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryOutFailures.setStatus("current")
_WanX25HistoryProviderClears_Type = Counter64
_WanX25HistoryProviderClears_Object = MibTableColumn
wanX25HistoryProviderClears = _WanX25HistoryProviderClears_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 15),
    _WanX25HistoryProviderClears_Type()
)
wanX25HistoryProviderClears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryProviderClears.setStatus("current")
_WanX25HistoryInResets_Type = Counter64
_WanX25HistoryInResets_Object = MibTableColumn
wanX25HistoryInResets = _WanX25HistoryInResets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 16),
    _WanX25HistoryInResets_Type()
)
wanX25HistoryInResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryInResets.setStatus("current")
_WanX25HistoryOutResets_Type = Counter64
_WanX25HistoryOutResets_Object = MibTableColumn
wanX25HistoryOutResets = _WanX25HistoryOutResets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 17),
    _WanX25HistoryOutResets_Type()
)
wanX25HistoryOutResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryOutResets.setStatus("current")
_WanX25HistoryProviderResets_Type = Counter64
_WanX25HistoryProviderResets_Object = MibTableColumn
wanX25HistoryProviderResets = _WanX25HistoryProviderResets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 18),
    _WanX25HistoryProviderResets_Type()
)
wanX25HistoryProviderResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryProviderResets.setStatus("current")
_WanX25HistoryInAccusedErrors_Type = Counter64
_WanX25HistoryInAccusedErrors_Object = MibTableColumn
wanX25HistoryInAccusedErrors = _WanX25HistoryInAccusedErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 19),
    _WanX25HistoryInAccusedErrors_Type()
)
wanX25HistoryInAccusedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryInAccusedErrors.setStatus("current")
_WanX25HistoryOutAccusedErrors_Type = Counter64
_WanX25HistoryOutAccusedErrors_Object = MibTableColumn
wanX25HistoryOutAccusedErrors = _WanX25HistoryOutAccusedErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 20),
    _WanX25HistoryOutAccusedErrors_Type()
)
wanX25HistoryOutAccusedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryOutAccusedErrors.setStatus("current")
_WanX25HistoryInInterrupts_Type = Counter64
_WanX25HistoryInInterrupts_Object = MibTableColumn
wanX25HistoryInInterrupts = _WanX25HistoryInInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 21),
    _WanX25HistoryInInterrupts_Type()
)
wanX25HistoryInInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryInInterrupts.setStatus("current")
_WanX25HistoryOutInterrupts_Type = Counter64
_WanX25HistoryOutInterrupts_Object = MibTableColumn
wanX25HistoryOutInterrupts = _WanX25HistoryOutInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 22),
    _WanX25HistoryOutInterrupts_Type()
)
wanX25HistoryOutInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryOutInterrupts.setStatus("current")


class _WanX25HistoryInUtilization_Type(Integer32):
    """Custom type wanX25HistoryInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanX25HistoryInUtilization_Type.__name__ = "Integer32"
_WanX25HistoryInUtilization_Object = MibTableColumn
wanX25HistoryInUtilization = _WanX25HistoryInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 23),
    _WanX25HistoryInUtilization_Type()
)
wanX25HistoryInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryInUtilization.setStatus("current")


class _WanX25HistoryOutUtilization_Type(Integer32):
    """Custom type wanX25HistoryOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanX25HistoryOutUtilization_Type.__name__ = "Integer32"
_WanX25HistoryOutUtilization_Object = MibTableColumn
wanX25HistoryOutUtilization = _WanX25HistoryOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 1, 1, 24),
    _WanX25HistoryOutUtilization_Type()
)
wanX25HistoryOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25HistoryOutUtilization.setStatus("current")
_WanFrHistoryTable_Object = MibTable
wanFrHistoryTable = _WanFrHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2)
)
if mibBuilder.loadTexts:
    wanFrHistoryTable.setStatus("current")
_WanFrHistoryEntry_Object = MibTableRow
wanFrHistoryEntry = _WanFrHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2, 1)
)
wanFrHistoryEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanFrHistoryIndex"),
    (0, "WANSTATS-MIB", "wanFrHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    wanFrHistoryEntry.setStatus("current")


class _WanFrHistoryIndex_Type(Integer32):
    """Custom type wanFrHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanFrHistoryIndex_Type.__name__ = "Integer32"
_WanFrHistoryIndex_Object = MibTableColumn
wanFrHistoryIndex = _WanFrHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2, 1, 1),
    _WanFrHistoryIndex_Type()
)
wanFrHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanFrHistoryIndex.setStatus("current")


class _WanFrHistorySampleIndex_Type(Integer32):
    """Custom type wanFrHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WanFrHistorySampleIndex_Type.__name__ = "Integer32"
_WanFrHistorySampleIndex_Object = MibTableColumn
wanFrHistorySampleIndex = _WanFrHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2, 1, 2),
    _WanFrHistorySampleIndex_Type()
)
wanFrHistorySampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanFrHistorySampleIndex.setStatus("current")
_WanFrHistoryIntervalStart_Type = TimeTicks
_WanFrHistoryIntervalStart_Object = MibTableColumn
wanFrHistoryIntervalStart = _WanFrHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2, 1, 3),
    _WanFrHistoryIntervalStart_Type()
)
wanFrHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrHistoryIntervalStart.setStatus("current")
_WanFrHistoryDropEvents_Type = Counter64
_WanFrHistoryDropEvents_Object = MibTableColumn
wanFrHistoryDropEvents = _WanFrHistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2, 1, 4),
    _WanFrHistoryDropEvents_Type()
)
wanFrHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrHistoryDropEvents.setStatus("current")
_WanFrHistoryInFrames_Type = Counter64
_WanFrHistoryInFrames_Object = MibTableColumn
wanFrHistoryInFrames = _WanFrHistoryInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2, 1, 5),
    _WanFrHistoryInFrames_Type()
)
wanFrHistoryInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrHistoryInFrames.setStatus("current")
_WanFrHistoryOutFrames_Type = Counter64
_WanFrHistoryOutFrames_Object = MibTableColumn
wanFrHistoryOutFrames = _WanFrHistoryOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2, 1, 6),
    _WanFrHistoryOutFrames_Type()
)
wanFrHistoryOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrHistoryOutFrames.setStatus("current")
_WanFrHistoryInOctets_Type = Counter64
_WanFrHistoryInOctets_Object = MibTableColumn
wanFrHistoryInOctets = _WanFrHistoryInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2, 1, 7),
    _WanFrHistoryInOctets_Type()
)
wanFrHistoryInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrHistoryInOctets.setStatus("current")
_WanFrHistoryOutOctets_Type = Counter64
_WanFrHistoryOutOctets_Object = MibTableColumn
wanFrHistoryOutOctets = _WanFrHistoryOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2, 1, 8),
    _WanFrHistoryOutOctets_Type()
)
wanFrHistoryOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrHistoryOutOctets.setStatus("current")
_WanFrHistoryInFECNs_Type = Counter64
_WanFrHistoryInFECNs_Object = MibTableColumn
wanFrHistoryInFECNs = _WanFrHistoryInFECNs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2, 1, 9),
    _WanFrHistoryInFECNs_Type()
)
wanFrHistoryInFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrHistoryInFECNs.setStatus("current")
_WanFrHistoryOutFECNs_Type = Counter64
_WanFrHistoryOutFECNs_Object = MibTableColumn
wanFrHistoryOutFECNs = _WanFrHistoryOutFECNs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2, 1, 10),
    _WanFrHistoryOutFECNs_Type()
)
wanFrHistoryOutFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrHistoryOutFECNs.setStatus("current")
_WanFrHistoryInBECNs_Type = Counter64
_WanFrHistoryInBECNs_Object = MibTableColumn
wanFrHistoryInBECNs = _WanFrHistoryInBECNs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2, 1, 11),
    _WanFrHistoryInBECNs_Type()
)
wanFrHistoryInBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrHistoryInBECNs.setStatus("current")
_WanFrHistoryOutBECNs_Type = Counter64
_WanFrHistoryOutBECNs_Object = MibTableColumn
wanFrHistoryOutBECNs = _WanFrHistoryOutBECNs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2, 1, 12),
    _WanFrHistoryOutBECNs_Type()
)
wanFrHistoryOutBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrHistoryOutBECNs.setStatus("current")
_WanFrHistoryInDEs_Type = Counter64
_WanFrHistoryInDEs_Object = MibTableColumn
wanFrHistoryInDEs = _WanFrHistoryInDEs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2, 1, 13),
    _WanFrHistoryInDEs_Type()
)
wanFrHistoryInDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrHistoryInDEs.setStatus("current")
_WanFrHistoryOutDEs_Type = Counter64
_WanFrHistoryOutDEs_Object = MibTableColumn
wanFrHistoryOutDEs = _WanFrHistoryOutDEs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2, 1, 14),
    _WanFrHistoryOutDEs_Type()
)
wanFrHistoryOutDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrHistoryOutDEs.setStatus("current")


class _WanFrHistoryInUtilization_Type(Integer32):
    """Custom type wanFrHistoryInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanFrHistoryInUtilization_Type.__name__ = "Integer32"
_WanFrHistoryInUtilization_Object = MibTableColumn
wanFrHistoryInUtilization = _WanFrHistoryInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2, 1, 15),
    _WanFrHistoryInUtilization_Type()
)
wanFrHistoryInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrHistoryInUtilization.setStatus("current")


class _WanFrHistoryOutUtilization_Type(Integer32):
    """Custom type wanFrHistoryOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanFrHistoryOutUtilization_Type.__name__ = "Integer32"
_WanFrHistoryOutUtilization_Object = MibTableColumn
wanFrHistoryOutUtilization = _WanFrHistoryOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 2, 1, 16),
    _WanFrHistoryOutUtilization_Type()
)
wanFrHistoryOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrHistoryOutUtilization.setStatus("current")
_WanAal5HistoryTable_Object = MibTable
wanAal5HistoryTable = _WanAal5HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3)
)
if mibBuilder.loadTexts:
    wanAal5HistoryTable.setStatus("current")
_WanAal5HistoryEntry_Object = MibTableRow
wanAal5HistoryEntry = _WanAal5HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1)
)
wanAal5HistoryEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanAal5HistoryIndex"),
    (0, "WANSTATS-MIB", "wanAal5HistorySampleIndex"),
)
if mibBuilder.loadTexts:
    wanAal5HistoryEntry.setStatus("current")


class _WanAal5HistoryIndex_Type(Integer32):
    """Custom type wanAal5HistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanAal5HistoryIndex_Type.__name__ = "Integer32"
_WanAal5HistoryIndex_Object = MibTableColumn
wanAal5HistoryIndex = _WanAal5HistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 1),
    _WanAal5HistoryIndex_Type()
)
wanAal5HistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanAal5HistoryIndex.setStatus("current")


class _WanAal5HistorySampleIndex_Type(Integer32):
    """Custom type wanAal5HistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WanAal5HistorySampleIndex_Type.__name__ = "Integer32"
_WanAal5HistorySampleIndex_Object = MibTableColumn
wanAal5HistorySampleIndex = _WanAal5HistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 2),
    _WanAal5HistorySampleIndex_Type()
)
wanAal5HistorySampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanAal5HistorySampleIndex.setStatus("current")
_WanAal5HistoryIntervalStart_Type = TimeTicks
_WanAal5HistoryIntervalStart_Object = MibTableColumn
wanAal5HistoryIntervalStart = _WanAal5HistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 3),
    _WanAal5HistoryIntervalStart_Type()
)
wanAal5HistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryIntervalStart.setStatus("current")
_WanAal5HistoryDropEvents_Type = Counter64
_WanAal5HistoryDropEvents_Object = MibTableColumn
wanAal5HistoryDropEvents = _WanAal5HistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 4),
    _WanAal5HistoryDropEvents_Type()
)
wanAal5HistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryDropEvents.setStatus("current")
_WanAal5HistoryInCells_Type = Counter64
_WanAal5HistoryInCells_Object = MibTableColumn
wanAal5HistoryInCells = _WanAal5HistoryInCells_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 5),
    _WanAal5HistoryInCells_Type()
)
wanAal5HistoryInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryInCells.setStatus("current")
_WanAal5HistoryOutCells_Type = Counter64
_WanAal5HistoryOutCells_Object = MibTableColumn
wanAal5HistoryOutCells = _WanAal5HistoryOutCells_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 6),
    _WanAal5HistoryOutCells_Type()
)
wanAal5HistoryOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryOutCells.setStatus("current")
_WanAal5HistoryInPDUs_Type = Counter64
_WanAal5HistoryInPDUs_Object = MibTableColumn
wanAal5HistoryInPDUs = _WanAal5HistoryInPDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 7),
    _WanAal5HistoryInPDUs_Type()
)
wanAal5HistoryInPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryInPDUs.setStatus("current")
_WanAal5HistoryOutPDUs_Type = Counter64
_WanAal5HistoryOutPDUs_Object = MibTableColumn
wanAal5HistoryOutPDUs = _WanAal5HistoryOutPDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 8),
    _WanAal5HistoryOutPDUs_Type()
)
wanAal5HistoryOutPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryOutPDUs.setStatus("current")
_WanAal5HistoryInOctets_Type = Counter64
_WanAal5HistoryInOctets_Object = MibTableColumn
wanAal5HistoryInOctets = _WanAal5HistoryInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 9),
    _WanAal5HistoryInOctets_Type()
)
wanAal5HistoryInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryInOctets.setStatus("current")
_WanAal5HistoryOutOctets_Type = Counter64
_WanAal5HistoryOutOctets_Object = MibTableColumn
wanAal5HistoryOutOctets = _WanAal5HistoryOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 10),
    _WanAal5HistoryOutOctets_Type()
)
wanAal5HistoryOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryOutOctets.setStatus("current")
_WanAal5HistoryInCLP1_Type = Counter64
_WanAal5HistoryInCLP1_Object = MibTableColumn
wanAal5HistoryInCLP1 = _WanAal5HistoryInCLP1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 11),
    _WanAal5HistoryInCLP1_Type()
)
wanAal5HistoryInCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryInCLP1.setStatus("current")
_WanAal5HistoryOutCLP1_Type = Counter64
_WanAal5HistoryOutCLP1_Object = MibTableColumn
wanAal5HistoryOutCLP1 = _WanAal5HistoryOutCLP1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 12),
    _WanAal5HistoryOutCLP1_Type()
)
wanAal5HistoryOutCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryOutCLP1.setStatus("current")
_WanAal5HistoryInCRCs_Type = Counter64
_WanAal5HistoryInCRCs_Object = MibTableColumn
wanAal5HistoryInCRCs = _WanAal5HistoryInCRCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 13),
    _WanAal5HistoryInCRCs_Type()
)
wanAal5HistoryInCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryInCRCs.setStatus("current")
_WanAal5HistoryOutCRCs_Type = Counter64
_WanAal5HistoryOutCRCs_Object = MibTableColumn
wanAal5HistoryOutCRCs = _WanAal5HistoryOutCRCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 14),
    _WanAal5HistoryOutCRCs_Type()
)
wanAal5HistoryOutCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryOutCRCs.setStatus("current")
_WanAal5HistoryInOversizedSDUs_Type = Counter64
_WanAal5HistoryInOversizedSDUs_Object = MibTableColumn
wanAal5HistoryInOversizedSDUs = _WanAal5HistoryInOversizedSDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 15),
    _WanAal5HistoryInOversizedSDUs_Type()
)
wanAal5HistoryInOversizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryInOversizedSDUs.setStatus("current")
_WanAal5HistoryOutOversizedSDUs_Type = Counter64
_WanAal5HistoryOutOversizedSDUs_Object = MibTableColumn
wanAal5HistoryOutOversizedSDUs = _WanAal5HistoryOutOversizedSDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 16),
    _WanAal5HistoryOutOversizedSDUs_Type()
)
wanAal5HistoryOutOversizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryOutOversizedSDUs.setStatus("current")
_WanAal5HistoryInSVCs_Type = Counter64
_WanAal5HistoryInSVCs_Object = MibTableColumn
wanAal5HistoryInSVCs = _WanAal5HistoryInSVCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 17),
    _WanAal5HistoryInSVCs_Type()
)
wanAal5HistoryInSVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryInSVCs.setStatus("current")
_WanAal5HistoryOutSVCs_Type = Counter64
_WanAal5HistoryOutSVCs_Object = MibTableColumn
wanAal5HistoryOutSVCs = _WanAal5HistoryOutSVCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 18),
    _WanAal5HistoryOutSVCs_Type()
)
wanAal5HistoryOutSVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryOutSVCs.setStatus("current")


class _WanAal5HistoryInUtilization_Type(Integer32):
    """Custom type wanAal5HistoryInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanAal5HistoryInUtilization_Type.__name__ = "Integer32"
_WanAal5HistoryInUtilization_Object = MibTableColumn
wanAal5HistoryInUtilization = _WanAal5HistoryInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 19),
    _WanAal5HistoryInUtilization_Type()
)
wanAal5HistoryInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryInUtilization.setStatus("current")


class _WanAal5HistoryOutUtilization_Type(Integer32):
    """Custom type wanAal5HistoryOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanAal5HistoryOutUtilization_Type.__name__ = "Integer32"
_WanAal5HistoryOutUtilization_Object = MibTableColumn
wanAal5HistoryOutUtilization = _WanAal5HistoryOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 3, 1, 20),
    _WanAal5HistoryOutUtilization_Type()
)
wanAal5HistoryOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5HistoryOutUtilization.setStatus("current")
_WanPppHistoryTable_Object = MibTable
wanPppHistoryTable = _WanPppHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4)
)
if mibBuilder.loadTexts:
    wanPppHistoryTable.setStatus("current")
_WanPppHistoryEntry_Object = MibTableRow
wanPppHistoryEntry = _WanPppHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1)
)
wanPppHistoryEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanPppHistoryIndex"),
    (0, "WANSTATS-MIB", "wanPppHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    wanPppHistoryEntry.setStatus("current")


class _WanPppHistoryIndex_Type(Integer32):
    """Custom type wanPppHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanPppHistoryIndex_Type.__name__ = "Integer32"
_WanPppHistoryIndex_Object = MibTableColumn
wanPppHistoryIndex = _WanPppHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 1),
    _WanPppHistoryIndex_Type()
)
wanPppHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanPppHistoryIndex.setStatus("current")


class _WanPppHistorySampleIndex_Type(Integer32):
    """Custom type wanPppHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WanPppHistorySampleIndex_Type.__name__ = "Integer32"
_WanPppHistorySampleIndex_Object = MibTableColumn
wanPppHistorySampleIndex = _WanPppHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 2),
    _WanPppHistorySampleIndex_Type()
)
wanPppHistorySampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanPppHistorySampleIndex.setStatus("current")
_WanPppHistoryIntervalStart_Type = TimeTicks
_WanPppHistoryIntervalStart_Object = MibTableColumn
wanPppHistoryIntervalStart = _WanPppHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 3),
    _WanPppHistoryIntervalStart_Type()
)
wanPppHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppHistoryIntervalStart.setStatus("current")
_WanPppHistoryDropEvents_Type = Counter64
_WanPppHistoryDropEvents_Object = MibTableColumn
wanPppHistoryDropEvents = _WanPppHistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 4),
    _WanPppHistoryDropEvents_Type()
)
wanPppHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppHistoryDropEvents.setStatus("current")
_WanPppHistoryInFrames_Type = Counter64
_WanPppHistoryInFrames_Object = MibTableColumn
wanPppHistoryInFrames = _WanPppHistoryInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 5),
    _WanPppHistoryInFrames_Type()
)
wanPppHistoryInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppHistoryInFrames.setStatus("current")
_WanPppHistoryOutFrames_Type = Counter64
_WanPppHistoryOutFrames_Object = MibTableColumn
wanPppHistoryOutFrames = _WanPppHistoryOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 6),
    _WanPppHistoryOutFrames_Type()
)
wanPppHistoryOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppHistoryOutFrames.setStatus("current")
_WanPppHistoryInOctets_Type = Counter64
_WanPppHistoryInOctets_Object = MibTableColumn
wanPppHistoryInOctets = _WanPppHistoryInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 7),
    _WanPppHistoryInOctets_Type()
)
wanPppHistoryInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppHistoryInOctets.setStatus("current")
_WanPppHistoryOutOctets_Type = Counter64
_WanPppHistoryOutOctets_Object = MibTableColumn
wanPppHistoryOutOctets = _WanPppHistoryOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 8),
    _WanPppHistoryOutOctets_Type()
)
wanPppHistoryOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppHistoryOutOctets.setStatus("current")
_WanPppHistoryInBadAddresses_Type = Counter64
_WanPppHistoryInBadAddresses_Object = MibTableColumn
wanPppHistoryInBadAddresses = _WanPppHistoryInBadAddresses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 9),
    _WanPppHistoryInBadAddresses_Type()
)
wanPppHistoryInBadAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppHistoryInBadAddresses.setStatus("current")
_WanPppHistoryOutBadAddresses_Type = Counter64
_WanPppHistoryOutBadAddresses_Object = MibTableColumn
wanPppHistoryOutBadAddresses = _WanPppHistoryOutBadAddresses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 10),
    _WanPppHistoryOutBadAddresses_Type()
)
wanPppHistoryOutBadAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppHistoryOutBadAddresses.setStatus("current")
_WanPppHistoryInBadControls_Type = Counter64
_WanPppHistoryInBadControls_Object = MibTableColumn
wanPppHistoryInBadControls = _WanPppHistoryInBadControls_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 11),
    _WanPppHistoryInBadControls_Type()
)
wanPppHistoryInBadControls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppHistoryInBadControls.setStatus("current")
_WanPppHistoryOutBadControls_Type = Counter64
_WanPppHistoryOutBadControls_Object = MibTableColumn
wanPppHistoryOutBadControls = _WanPppHistoryOutBadControls_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 12),
    _WanPppHistoryOutBadControls_Type()
)
wanPppHistoryOutBadControls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppHistoryOutBadControls.setStatus("current")
_WanPppHistoryInLongFrames_Type = Counter64
_WanPppHistoryInLongFrames_Object = MibTableColumn
wanPppHistoryInLongFrames = _WanPppHistoryInLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 13),
    _WanPppHistoryInLongFrames_Type()
)
wanPppHistoryInLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppHistoryInLongFrames.setStatus("current")
_WanPppHistoryOutLongFrames_Type = Counter64
_WanPppHistoryOutLongFrames_Object = MibTableColumn
wanPppHistoryOutLongFrames = _WanPppHistoryOutLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 14),
    _WanPppHistoryOutLongFrames_Type()
)
wanPppHistoryOutLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppHistoryOutLongFrames.setStatus("current")
_WanPppHistoryInBadFCSs_Type = Counter64
_WanPppHistoryInBadFCSs_Object = MibTableColumn
wanPppHistoryInBadFCSs = _WanPppHistoryInBadFCSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 15),
    _WanPppHistoryInBadFCSs_Type()
)
wanPppHistoryInBadFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppHistoryInBadFCSs.setStatus("current")
_WanPppHistoryOutBadFCSs_Type = Counter64
_WanPppHistoryOutBadFCSs_Object = MibTableColumn
wanPppHistoryOutBadFCSs = _WanPppHistoryOutBadFCSs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 16),
    _WanPppHistoryOutBadFCSs_Type()
)
wanPppHistoryOutBadFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppHistoryOutBadFCSs.setStatus("current")


class _WanPppHistoryInUtilization_Type(Integer32):
    """Custom type wanPppHistoryInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanPppHistoryInUtilization_Type.__name__ = "Integer32"
_WanPppHistoryInUtilization_Object = MibTableColumn
wanPppHistoryInUtilization = _WanPppHistoryInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 17),
    _WanPppHistoryInUtilization_Type()
)
wanPppHistoryInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppHistoryInUtilization.setStatus("current")


class _WanPppHistoryOutUtilization_Type(Integer32):
    """Custom type wanPppHistoryOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanPppHistoryOutUtilization_Type.__name__ = "Integer32"
_WanPppHistoryOutUtilization_Object = MibTableColumn
wanPppHistoryOutUtilization = _WanPppHistoryOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 2, 4, 1, 18),
    _WanPppHistoryOutUtilization_Type()
)
wanPppHistoryOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPppHistoryOutUtilization.setStatus("current")
_WanPvcHistory_ObjectIdentity = ObjectIdentity
wanPvcHistory = _WanPvcHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3)
)
_WanX25PvcHistoryTable_Object = MibTable
wanX25PvcHistoryTable = _WanX25PvcHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1)
)
if mibBuilder.loadTexts:
    wanX25PvcHistoryTable.setStatus("current")
_WanX25PvcHistoryEntry_Object = MibTableRow
wanX25PvcHistoryEntry = _WanX25PvcHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1)
)
wanX25PvcHistoryEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanX25PvcHistoryIndex"),
    (0, "WANSTATS-MIB", "wanX25PvcHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    wanX25PvcHistoryEntry.setStatus("current")


class _WanX25PvcHistoryIndex_Type(Integer32):
    """Custom type wanX25PvcHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanX25PvcHistoryIndex_Type.__name__ = "Integer32"
_WanX25PvcHistoryIndex_Object = MibTableColumn
wanX25PvcHistoryIndex = _WanX25PvcHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 1),
    _WanX25PvcHistoryIndex_Type()
)
wanX25PvcHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanX25PvcHistoryIndex.setStatus("current")


class _WanX25PvcHistorySampleIndex_Type(Integer32):
    """Custom type wanX25PvcHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WanX25PvcHistorySampleIndex_Type.__name__ = "Integer32"
_WanX25PvcHistorySampleIndex_Object = MibTableColumn
wanX25PvcHistorySampleIndex = _WanX25PvcHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 2),
    _WanX25PvcHistorySampleIndex_Type()
)
wanX25PvcHistorySampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanX25PvcHistorySampleIndex.setStatus("current")
_WanX25PvcHistoryIntervalStart_Type = TimeTicks
_WanX25PvcHistoryIntervalStart_Object = MibTableColumn
wanX25PvcHistoryIntervalStart = _WanX25PvcHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 3),
    _WanX25PvcHistoryIntervalStart_Type()
)
wanX25PvcHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryIntervalStart.setStatus("current")
_WanX25PvcHistoryDropEvents_Type = Counter64
_WanX25PvcHistoryDropEvents_Object = MibTableColumn
wanX25PvcHistoryDropEvents = _WanX25PvcHistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 4),
    _WanX25PvcHistoryDropEvents_Type()
)
wanX25PvcHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryDropEvents.setStatus("current")
_WanX25PvcHistoryInFrames_Type = Counter64
_WanX25PvcHistoryInFrames_Object = MibTableColumn
wanX25PvcHistoryInFrames = _WanX25PvcHistoryInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 5),
    _WanX25PvcHistoryInFrames_Type()
)
wanX25PvcHistoryInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryInFrames.setStatus("current")
_WanX25PvcHistoryOutFrames_Type = Counter64
_WanX25PvcHistoryOutFrames_Object = MibTableColumn
wanX25PvcHistoryOutFrames = _WanX25PvcHistoryOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 6),
    _WanX25PvcHistoryOutFrames_Type()
)
wanX25PvcHistoryOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryOutFrames.setStatus("current")
_WanX25PvcHistoryInOctets_Type = Counter64
_WanX25PvcHistoryInOctets_Object = MibTableColumn
wanX25PvcHistoryInOctets = _WanX25PvcHistoryInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 7),
    _WanX25PvcHistoryInOctets_Type()
)
wanX25PvcHistoryInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryInOctets.setStatus("current")
_WanX25PvcHistoryOutOctets_Type = Counter64
_WanX25PvcHistoryOutOctets_Object = MibTableColumn
wanX25PvcHistoryOutOctets = _WanX25PvcHistoryOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 8),
    _WanX25PvcHistoryOutOctets_Type()
)
wanX25PvcHistoryOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryOutOctets.setStatus("current")
_WanX25PvcHistoryInResets_Type = Counter64
_WanX25PvcHistoryInResets_Object = MibTableColumn
wanX25PvcHistoryInResets = _WanX25PvcHistoryInResets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 9),
    _WanX25PvcHistoryInResets_Type()
)
wanX25PvcHistoryInResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryInResets.setStatus("current")
_WanX25PvcHistoryOutResets_Type = Counter64
_WanX25PvcHistoryOutResets_Object = MibTableColumn
wanX25PvcHistoryOutResets = _WanX25PvcHistoryOutResets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 10),
    _WanX25PvcHistoryOutResets_Type()
)
wanX25PvcHistoryOutResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryOutResets.setStatus("current")
_WanX25PvcHistoryProviderResets_Type = Counter64
_WanX25PvcHistoryProviderResets_Object = MibTableColumn
wanX25PvcHistoryProviderResets = _WanX25PvcHistoryProviderResets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 11),
    _WanX25PvcHistoryProviderResets_Type()
)
wanX25PvcHistoryProviderResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryProviderResets.setStatus("current")
_WanX25PvcHistoryInAccusedErrors_Type = Counter64
_WanX25PvcHistoryInAccusedErrors_Object = MibTableColumn
wanX25PvcHistoryInAccusedErrors = _WanX25PvcHistoryInAccusedErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 12),
    _WanX25PvcHistoryInAccusedErrors_Type()
)
wanX25PvcHistoryInAccusedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryInAccusedErrors.setStatus("current")
_WanX25PvcHistoryOutAccusedErrors_Type = Counter64
_WanX25PvcHistoryOutAccusedErrors_Object = MibTableColumn
wanX25PvcHistoryOutAccusedErrors = _WanX25PvcHistoryOutAccusedErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 13),
    _WanX25PvcHistoryOutAccusedErrors_Type()
)
wanX25PvcHistoryOutAccusedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryOutAccusedErrors.setStatus("current")
_WanX25PvcHistoryInInterrupts_Type = Counter64
_WanX25PvcHistoryInInterrupts_Object = MibTableColumn
wanX25PvcHistoryInInterrupts = _WanX25PvcHistoryInInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 14),
    _WanX25PvcHistoryInInterrupts_Type()
)
wanX25PvcHistoryInInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryInInterrupts.setStatus("current")
_WanX25PvcHistoryOutInterrupts_Type = Counter64
_WanX25PvcHistoryOutInterrupts_Object = MibTableColumn
wanX25PvcHistoryOutInterrupts = _WanX25PvcHistoryOutInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 15),
    _WanX25PvcHistoryOutInterrupts_Type()
)
wanX25PvcHistoryOutInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryOutInterrupts.setStatus("current")
_WanX25PvcHistoryUpTime_Type = TimeTicks
_WanX25PvcHistoryUpTime_Object = MibTableColumn
wanX25PvcHistoryUpTime = _WanX25PvcHistoryUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 16),
    _WanX25PvcHistoryUpTime_Type()
)
wanX25PvcHistoryUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryUpTime.setStatus("current")
_WanX25PvcHistoryDownTime_Type = TimeTicks
_WanX25PvcHistoryDownTime_Object = MibTableColumn
wanX25PvcHistoryDownTime = _WanX25PvcHistoryDownTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 17),
    _WanX25PvcHistoryDownTime_Type()
)
wanX25PvcHistoryDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryDownTime.setStatus("current")
_WanX25PvcHistoryStateChanges_Type = Counter64
_WanX25PvcHistoryStateChanges_Object = MibTableColumn
wanX25PvcHistoryStateChanges = _WanX25PvcHistoryStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 18),
    _WanX25PvcHistoryStateChanges_Type()
)
wanX25PvcHistoryStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryStateChanges.setStatus("current")


class _WanX25PvcHistoryInUtilization_Type(Integer32):
    """Custom type wanX25PvcHistoryInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanX25PvcHistoryInUtilization_Type.__name__ = "Integer32"
_WanX25PvcHistoryInUtilization_Object = MibTableColumn
wanX25PvcHistoryInUtilization = _WanX25PvcHistoryInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 19),
    _WanX25PvcHistoryInUtilization_Type()
)
wanX25PvcHistoryInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryInUtilization.setStatus("current")


class _WanX25PvcHistoryOutUtilization_Type(Integer32):
    """Custom type wanX25PvcHistoryOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanX25PvcHistoryOutUtilization_Type.__name__ = "Integer32"
_WanX25PvcHistoryOutUtilization_Object = MibTableColumn
wanX25PvcHistoryOutUtilization = _WanX25PvcHistoryOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 1, 1, 20),
    _WanX25PvcHistoryOutUtilization_Type()
)
wanX25PvcHistoryOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanX25PvcHistoryOutUtilization.setStatus("current")
_WanFrPvcHistoryTable_Object = MibTable
wanFrPvcHistoryTable = _WanFrPvcHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2)
)
if mibBuilder.loadTexts:
    wanFrPvcHistoryTable.setStatus("current")
_WanFrPvcHistoryEntry_Object = MibTableRow
wanFrPvcHistoryEntry = _WanFrPvcHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1)
)
wanFrPvcHistoryEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanFrPvcHistoryIndex"),
    (0, "WANSTATS-MIB", "wanFrPvcHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    wanFrPvcHistoryEntry.setStatus("current")


class _WanFrPvcHistoryIndex_Type(Integer32):
    """Custom type wanFrPvcHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanFrPvcHistoryIndex_Type.__name__ = "Integer32"
_WanFrPvcHistoryIndex_Object = MibTableColumn
wanFrPvcHistoryIndex = _WanFrPvcHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 1),
    _WanFrPvcHistoryIndex_Type()
)
wanFrPvcHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanFrPvcHistoryIndex.setStatus("current")


class _WanFrPvcHistorySampleIndex_Type(Integer32):
    """Custom type wanFrPvcHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WanFrPvcHistorySampleIndex_Type.__name__ = "Integer32"
_WanFrPvcHistorySampleIndex_Object = MibTableColumn
wanFrPvcHistorySampleIndex = _WanFrPvcHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 2),
    _WanFrPvcHistorySampleIndex_Type()
)
wanFrPvcHistorySampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanFrPvcHistorySampleIndex.setStatus("current")
_WanFrPvcHistoryIntervalStart_Type = TimeTicks
_WanFrPvcHistoryIntervalStart_Object = MibTableColumn
wanFrPvcHistoryIntervalStart = _WanFrPvcHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 3),
    _WanFrPvcHistoryIntervalStart_Type()
)
wanFrPvcHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcHistoryIntervalStart.setStatus("current")
_WanFrPvcHistoryDropEvents_Type = Counter64
_WanFrPvcHistoryDropEvents_Object = MibTableColumn
wanFrPvcHistoryDropEvents = _WanFrPvcHistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 4),
    _WanFrPvcHistoryDropEvents_Type()
)
wanFrPvcHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcHistoryDropEvents.setStatus("current")
_WanFrPvcHistoryInFrames_Type = Counter64
_WanFrPvcHistoryInFrames_Object = MibTableColumn
wanFrPvcHistoryInFrames = _WanFrPvcHistoryInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 5),
    _WanFrPvcHistoryInFrames_Type()
)
wanFrPvcHistoryInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcHistoryInFrames.setStatus("current")
_WanFrPvcHistoryOutFrames_Type = Counter64
_WanFrPvcHistoryOutFrames_Object = MibTableColumn
wanFrPvcHistoryOutFrames = _WanFrPvcHistoryOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 6),
    _WanFrPvcHistoryOutFrames_Type()
)
wanFrPvcHistoryOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcHistoryOutFrames.setStatus("current")
_WanFrPvcHistoryInOctets_Type = Counter64
_WanFrPvcHistoryInOctets_Object = MibTableColumn
wanFrPvcHistoryInOctets = _WanFrPvcHistoryInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 7),
    _WanFrPvcHistoryInOctets_Type()
)
wanFrPvcHistoryInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcHistoryInOctets.setStatus("current")
_WanFrPvcHistoryOutOctets_Type = Counter64
_WanFrPvcHistoryOutOctets_Object = MibTableColumn
wanFrPvcHistoryOutOctets = _WanFrPvcHistoryOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 8),
    _WanFrPvcHistoryOutOctets_Type()
)
wanFrPvcHistoryOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcHistoryOutOctets.setStatus("current")
_WanFrPvcHistoryInFECNs_Type = Counter64
_WanFrPvcHistoryInFECNs_Object = MibTableColumn
wanFrPvcHistoryInFECNs = _WanFrPvcHistoryInFECNs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 9),
    _WanFrPvcHistoryInFECNs_Type()
)
wanFrPvcHistoryInFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcHistoryInFECNs.setStatus("current")
_WanFrPvcHistoryOutFECNs_Type = Counter64
_WanFrPvcHistoryOutFECNs_Object = MibTableColumn
wanFrPvcHistoryOutFECNs = _WanFrPvcHistoryOutFECNs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 10),
    _WanFrPvcHistoryOutFECNs_Type()
)
wanFrPvcHistoryOutFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcHistoryOutFECNs.setStatus("current")
_WanFrPvcHistoryInBECNs_Type = Counter64
_WanFrPvcHistoryInBECNs_Object = MibTableColumn
wanFrPvcHistoryInBECNs = _WanFrPvcHistoryInBECNs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 11),
    _WanFrPvcHistoryInBECNs_Type()
)
wanFrPvcHistoryInBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcHistoryInBECNs.setStatus("current")
_WanFrPvcHistoryOutBECNs_Type = Counter64
_WanFrPvcHistoryOutBECNs_Object = MibTableColumn
wanFrPvcHistoryOutBECNs = _WanFrPvcHistoryOutBECNs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 12),
    _WanFrPvcHistoryOutBECNs_Type()
)
wanFrPvcHistoryOutBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcHistoryOutBECNs.setStatus("current")
_WanFrPvcHistoryInDEs_Type = Counter64
_WanFrPvcHistoryInDEs_Object = MibTableColumn
wanFrPvcHistoryInDEs = _WanFrPvcHistoryInDEs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 13),
    _WanFrPvcHistoryInDEs_Type()
)
wanFrPvcHistoryInDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcHistoryInDEs.setStatus("current")
_WanFrPvcHistoryOutDEs_Type = Counter64
_WanFrPvcHistoryOutDEs_Object = MibTableColumn
wanFrPvcHistoryOutDEs = _WanFrPvcHistoryOutDEs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 14),
    _WanFrPvcHistoryOutDEs_Type()
)
wanFrPvcHistoryOutDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcHistoryOutDEs.setStatus("current")
_WanFrPvcHistoryUpTime_Type = TimeTicks
_WanFrPvcHistoryUpTime_Object = MibTableColumn
wanFrPvcHistoryUpTime = _WanFrPvcHistoryUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 15),
    _WanFrPvcHistoryUpTime_Type()
)
wanFrPvcHistoryUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcHistoryUpTime.setStatus("current")
_WanFrPvcHistoryDownTime_Type = TimeTicks
_WanFrPvcHistoryDownTime_Object = MibTableColumn
wanFrPvcHistoryDownTime = _WanFrPvcHistoryDownTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 16),
    _WanFrPvcHistoryDownTime_Type()
)
wanFrPvcHistoryDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcHistoryDownTime.setStatus("current")
_WanFrPvcHistoryStateChanges_Type = Counter64
_WanFrPvcHistoryStateChanges_Object = MibTableColumn
wanFrPvcHistoryStateChanges = _WanFrPvcHistoryStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 17),
    _WanFrPvcHistoryStateChanges_Type()
)
wanFrPvcHistoryStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcHistoryStateChanges.setStatus("current")


class _WanFrPvcHistoryInUtilization_Type(Integer32):
    """Custom type wanFrPvcHistoryInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanFrPvcHistoryInUtilization_Type.__name__ = "Integer32"
_WanFrPvcHistoryInUtilization_Object = MibTableColumn
wanFrPvcHistoryInUtilization = _WanFrPvcHistoryInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 18),
    _WanFrPvcHistoryInUtilization_Type()
)
wanFrPvcHistoryInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcHistoryInUtilization.setStatus("current")


class _WanFrPvcHistoryOutUtilization_Type(Integer32):
    """Custom type wanFrPvcHistoryOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanFrPvcHistoryOutUtilization_Type.__name__ = "Integer32"
_WanFrPvcHistoryOutUtilization_Object = MibTableColumn
wanFrPvcHistoryOutUtilization = _WanFrPvcHistoryOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 2, 1, 19),
    _WanFrPvcHistoryOutUtilization_Type()
)
wanFrPvcHistoryOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanFrPvcHistoryOutUtilization.setStatus("current")
_WanAal5PvcHistoryTable_Object = MibTable
wanAal5PvcHistoryTable = _WanAal5PvcHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3)
)
if mibBuilder.loadTexts:
    wanAal5PvcHistoryTable.setStatus("current")
_WanAal5PvcHistoryEntry_Object = MibTableRow
wanAal5PvcHistoryEntry = _WanAal5PvcHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1)
)
wanAal5PvcHistoryEntry.setIndexNames(
    (0, "WANSTATS-MIB", "wanAal5PvcHistoryIndex"),
    (0, "WANSTATS-MIB", "wanAal5PvcHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    wanAal5PvcHistoryEntry.setStatus("current")


class _WanAal5PvcHistoryIndex_Type(Integer32):
    """Custom type wanAal5PvcHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WanAal5PvcHistoryIndex_Type.__name__ = "Integer32"
_WanAal5PvcHistoryIndex_Object = MibTableColumn
wanAal5PvcHistoryIndex = _WanAal5PvcHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 1),
    _WanAal5PvcHistoryIndex_Type()
)
wanAal5PvcHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryIndex.setStatus("current")


class _WanAal5PvcHistorySampleIndex_Type(Integer32):
    """Custom type wanAal5PvcHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WanAal5PvcHistorySampleIndex_Type.__name__ = "Integer32"
_WanAal5PvcHistorySampleIndex_Object = MibTableColumn
wanAal5PvcHistorySampleIndex = _WanAal5PvcHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 2),
    _WanAal5PvcHistorySampleIndex_Type()
)
wanAal5PvcHistorySampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanAal5PvcHistorySampleIndex.setStatus("current")
_WanAal5PvcHistoryIntervalStart_Type = TimeTicks
_WanAal5PvcHistoryIntervalStart_Object = MibTableColumn
wanAal5PvcHistoryIntervalStart = _WanAal5PvcHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 3),
    _WanAal5PvcHistoryIntervalStart_Type()
)
wanAal5PvcHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryIntervalStart.setStatus("current")
_WanAal5PvcHistoryDropEvents_Type = Counter64
_WanAal5PvcHistoryDropEvents_Object = MibTableColumn
wanAal5PvcHistoryDropEvents = _WanAal5PvcHistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 4),
    _WanAal5PvcHistoryDropEvents_Type()
)
wanAal5PvcHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryDropEvents.setStatus("current")
_WanAal5PvcHistoryInCells_Type = Counter64
_WanAal5PvcHistoryInCells_Object = MibTableColumn
wanAal5PvcHistoryInCells = _WanAal5PvcHistoryInCells_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 5),
    _WanAal5PvcHistoryInCells_Type()
)
wanAal5PvcHistoryInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryInCells.setStatus("current")
_WanAal5PvcHistoryOutCells_Type = Counter64
_WanAal5PvcHistoryOutCells_Object = MibTableColumn
wanAal5PvcHistoryOutCells = _WanAal5PvcHistoryOutCells_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 6),
    _WanAal5PvcHistoryOutCells_Type()
)
wanAal5PvcHistoryOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryOutCells.setStatus("current")
_WanAal5PvcHistoryInPDUs_Type = Counter64
_WanAal5PvcHistoryInPDUs_Object = MibTableColumn
wanAal5PvcHistoryInPDUs = _WanAal5PvcHistoryInPDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 7),
    _WanAal5PvcHistoryInPDUs_Type()
)
wanAal5PvcHistoryInPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryInPDUs.setStatus("current")
_WanAal5PvcHistoryOutPDUs_Type = Counter64
_WanAal5PvcHistoryOutPDUs_Object = MibTableColumn
wanAal5PvcHistoryOutPDUs = _WanAal5PvcHistoryOutPDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 8),
    _WanAal5PvcHistoryOutPDUs_Type()
)
wanAal5PvcHistoryOutPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryOutPDUs.setStatus("current")
_WanAal5PvcHistoryInOctets_Type = Counter64
_WanAal5PvcHistoryInOctets_Object = MibTableColumn
wanAal5PvcHistoryInOctets = _WanAal5PvcHistoryInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 9),
    _WanAal5PvcHistoryInOctets_Type()
)
wanAal5PvcHistoryInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryInOctets.setStatus("current")
_WanAal5PvcHistoryOutOctets_Type = Counter64
_WanAal5PvcHistoryOutOctets_Object = MibTableColumn
wanAal5PvcHistoryOutOctets = _WanAal5PvcHistoryOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 10),
    _WanAal5PvcHistoryOutOctets_Type()
)
wanAal5PvcHistoryOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryOutOctets.setStatus("current")
_WanAal5PvcHistoryInCLP1_Type = Counter64
_WanAal5PvcHistoryInCLP1_Object = MibTableColumn
wanAal5PvcHistoryInCLP1 = _WanAal5PvcHistoryInCLP1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 11),
    _WanAal5PvcHistoryInCLP1_Type()
)
wanAal5PvcHistoryInCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryInCLP1.setStatus("current")
_WanAal5PvcHistoryOutCLP1_Type = Counter64
_WanAal5PvcHistoryOutCLP1_Object = MibTableColumn
wanAal5PvcHistoryOutCLP1 = _WanAal5PvcHistoryOutCLP1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 12),
    _WanAal5PvcHistoryOutCLP1_Type()
)
wanAal5PvcHistoryOutCLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryOutCLP1.setStatus("current")
_WanAal5PvcHistoryInCRCs_Type = Counter64
_WanAal5PvcHistoryInCRCs_Object = MibTableColumn
wanAal5PvcHistoryInCRCs = _WanAal5PvcHistoryInCRCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 13),
    _WanAal5PvcHistoryInCRCs_Type()
)
wanAal5PvcHistoryInCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryInCRCs.setStatus("current")
_WanAal5PvcHistoryOutCRCs_Type = Counter64
_WanAal5PvcHistoryOutCRCs_Object = MibTableColumn
wanAal5PvcHistoryOutCRCs = _WanAal5PvcHistoryOutCRCs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 14),
    _WanAal5PvcHistoryOutCRCs_Type()
)
wanAal5PvcHistoryOutCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryOutCRCs.setStatus("current")
_WanAal5PvcHistoryInOversizedSDUs_Type = Counter64
_WanAal5PvcHistoryInOversizedSDUs_Object = MibTableColumn
wanAal5PvcHistoryInOversizedSDUs = _WanAal5PvcHistoryInOversizedSDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 15),
    _WanAal5PvcHistoryInOversizedSDUs_Type()
)
wanAal5PvcHistoryInOversizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryInOversizedSDUs.setStatus("current")
_WanAal5PvcHistoryOutOversizedSDUs_Type = Counter64
_WanAal5PvcHistoryOutOversizedSDUs_Object = MibTableColumn
wanAal5PvcHistoryOutOversizedSDUs = _WanAal5PvcHistoryOutOversizedSDUs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 16),
    _WanAal5PvcHistoryOutOversizedSDUs_Type()
)
wanAal5PvcHistoryOutOversizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryOutOversizedSDUs.setStatus("current")
_WanAal5PvcHistoryUpTime_Type = TimeTicks
_WanAal5PvcHistoryUpTime_Object = MibTableColumn
wanAal5PvcHistoryUpTime = _WanAal5PvcHistoryUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 17),
    _WanAal5PvcHistoryUpTime_Type()
)
wanAal5PvcHistoryUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryUpTime.setStatus("current")
_WanAal5PvcHistoryDownTime_Type = TimeTicks
_WanAal5PvcHistoryDownTime_Object = MibTableColumn
wanAal5PvcHistoryDownTime = _WanAal5PvcHistoryDownTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 18),
    _WanAal5PvcHistoryDownTime_Type()
)
wanAal5PvcHistoryDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryDownTime.setStatus("current")
_WanAal5PvcHistoryStateChanges_Type = Counter64
_WanAal5PvcHistoryStateChanges_Object = MibTableColumn
wanAal5PvcHistoryStateChanges = _WanAal5PvcHistoryStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 19),
    _WanAal5PvcHistoryStateChanges_Type()
)
wanAal5PvcHistoryStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryStateChanges.setStatus("current")


class _WanAal5PvcHistoryInUtilization_Type(Integer32):
    """Custom type wanAal5PvcHistoryInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanAal5PvcHistoryInUtilization_Type.__name__ = "Integer32"
_WanAal5PvcHistoryInUtilization_Object = MibTableColumn
wanAal5PvcHistoryInUtilization = _WanAal5PvcHistoryInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 20),
    _WanAal5PvcHistoryInUtilization_Type()
)
wanAal5PvcHistoryInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryInUtilization.setStatus("current")


class _WanAal5PvcHistoryOutUtilization_Type(Integer32):
    """Custom type wanAal5PvcHistoryOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WanAal5PvcHistoryOutUtilization_Type.__name__ = "Integer32"
_WanAal5PvcHistoryOutUtilization_Object = MibTableColumn
wanAal5PvcHistoryOutUtilization = _WanAal5PvcHistoryOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 6, 1, 5, 1, 8, 2, 3, 3, 1, 21),
    _WanAal5PvcHistoryOutUtilization_Type()
)
wanAal5PvcHistoryOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanAal5PvcHistoryOutUtilization.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WANSTATS-MIB",
    **{"hp": hp,
       "nm": nm,
       "system": system,
       "netElement": netElement,
       "lanprobe": lanprobe,
       "general": general,
       "rmonExtension": rmonExtension,
       "statsExtension": statsExtension,
       "wanStatsMIB": wanStatsMIB,
       "wanStatsMIBObjects": wanStatsMIBObjects,
       "wanSignalingStats": wanSignalingStats,
       "wanT1E1StatsTable": wanT1E1StatsTable,
       "wanT1E1StatsEntry": wanT1E1StatsEntry,
       "wanT1E1StatsIndex": wanT1E1StatsIndex,
       "wanT1E1StatsDataSource": wanT1E1StatsDataSource,
       "wanT1E1StatsDropEvents": wanT1E1StatsDropEvents,
       "wanT1E1StatsInFrames": wanT1E1StatsInFrames,
       "wanT1E1StatsOutFrames": wanT1E1StatsOutFrames,
       "wanT1E1StatsInOctets": wanT1E1StatsInOctets,
       "wanT1E1StatsOutOctets": wanT1E1StatsOutOctets,
       "wanT1E1StatsESs": wanT1E1StatsESs,
       "wanT1E1StatsSESs": wanT1E1StatsSESs,
       "wanT1E1StatsSEFSs": wanT1E1StatsSEFSs,
       "wanT1E1StatsOOFs": wanT1E1StatsOOFs,
       "wanT1E1StatsUASs": wanT1E1StatsUASs,
       "wanT1E1StatsCSSs": wanT1E1StatsCSSs,
       "wanT1E1StatsPCVs": wanT1E1StatsPCVs,
       "wanT1E1StatsLESs": wanT1E1StatsLESs,
       "wanT1E1StatsBESs": wanT1E1StatsBESs,
       "wanT1E1StatsDMs": wanT1E1StatsDMs,
       "wanT1E1StatsLCVs": wanT1E1StatsLCVs,
       "wanT1E1StatsLOFs": wanT1E1StatsLOFs,
       "wanT1E1StatsLOSs": wanT1E1StatsLOSs,
       "wanT1E1StatsRAIs": wanT1E1StatsRAIs,
       "wanT1E1StatsAISs": wanT1E1StatsAISs,
       "wanT1E1StatsTS16AISs": wanT1E1StatsTS16AISs,
       "wanT1E1StatsLOMFs": wanT1E1StatsLOMFs,
       "wanT1E1StatsFarLOMFs": wanT1E1StatsFarLOMFs,
       "wanT1E1StatsOwner": wanT1E1StatsOwner,
       "wanT1E1StatsStatus": wanT1E1StatsStatus,
       "wanVSeriesStatsTable": wanVSeriesStatsTable,
       "wanVSeriesStatsEntry": wanVSeriesStatsEntry,
       "wanVSeriesStatsIndex": wanVSeriesStatsIndex,
       "wanVSeriesStatsDataSource": wanVSeriesStatsDataSource,
       "wanVSeriesStatsDropEvents": wanVSeriesStatsDropEvents,
       "wanVSeriesStatsInFrames": wanVSeriesStatsInFrames,
       "wanVSeriesStatsOutFrames": wanVSeriesStatsOutFrames,
       "wanVSeriesStatsInOctets": wanVSeriesStatsInOctets,
       "wanVSeriesStatsOutOctets": wanVSeriesStatsOutOctets,
       "wanVSeriesStatsInFCSs": wanVSeriesStatsInFCSs,
       "wanVSeriesStatsOutFCSs": wanVSeriesStatsOutFCSs,
       "wanVSeriesStatsInOverruns": wanVSeriesStatsInOverruns,
       "wanVSeriesStatsOutOverruns": wanVSeriesStatsOutOverruns,
       "wanVSeriesStatsInterruptedFrames": wanVSeriesStatsInterruptedFrames,
       "wanVSeriesStatsInAbortedFrames": wanVSeriesStatsInAbortedFrames,
       "wanVSeriesStatsOutAbortedFrames": wanVSeriesStatsOutAbortedFrames,
       "wanVSeriesStatsOwner": wanVSeriesStatsOwner,
       "wanVSeriesStatsStatus": wanVSeriesStatsStatus,
       "wanHssiStatsTable": wanHssiStatsTable,
       "wanHssiStatsEntry": wanHssiStatsEntry,
       "wanHssiStatsIndex": wanHssiStatsIndex,
       "wanHssiStatsDataSource": wanHssiStatsDataSource,
       "wanHssiStatsDropEvents": wanHssiStatsDropEvents,
       "wanHssiStatsInFrames": wanHssiStatsInFrames,
       "wanHssiStatsOutFrames": wanHssiStatsOutFrames,
       "wanHssiStatsInOctets": wanHssiStatsInOctets,
       "wanHssiStatsOutOctets": wanHssiStatsOutOctets,
       "wanHssiStatsRxLongFrames": wanHssiStatsRxLongFrames,
       "wanHssiStatsRxCrcErrors": wanHssiStatsRxCrcErrors,
       "wanHssiStatsRxOverruns": wanHssiStatsRxOverruns,
       "wanHssiStatsRxAborts": wanHssiStatsRxAborts,
       "wanHssiStatsTxAborts": wanHssiStatsTxAborts,
       "wanHssiStatsTxUnderruns": wanHssiStatsTxUnderruns,
       "wanHssiStatsRxRingErrors": wanHssiStatsRxRingErrors,
       "wanHssiStatsRxRingOverruns": wanHssiStatsRxRingOverruns,
       "wanHssiStatsTxRingErrors": wanHssiStatsTxRingErrors,
       "wanHssiStatsPortOpErrors": wanHssiStatsPortOpErrors,
       "wanHssiStatsTxCmplProcessings": wanHssiStatsTxCmplProcessings,
       "wanHssiStatsOwner": wanHssiStatsOwner,
       "wanHssiStatsStatus": wanHssiStatsStatus,
       "wanT3E3StatsTable": wanT3E3StatsTable,
       "wanT3E3StatsEntry": wanT3E3StatsEntry,
       "wanT3E3StatsIndex": wanT3E3StatsIndex,
       "wanT3E3StatsDataSource": wanT3E3StatsDataSource,
       "wanT3E3StatsDropEvents": wanT3E3StatsDropEvents,
       "wanT3E3StatsInFrames": wanT3E3StatsInFrames,
       "wanT3E3StatsOutFrames": wanT3E3StatsOutFrames,
       "wanT3E3StatsInOctets": wanT3E3StatsInOctets,
       "wanT3E3StatsOutOctets": wanT3E3StatsOutOctets,
       "wanT3E3StatsPESs": wanT3E3StatsPESs,
       "wanT3E3StatsPSESs": wanT3E3StatsPSESs,
       "wanT3E3StatsOOFs": wanT3E3StatsOOFs,
       "wanT3E3StatsSEFSs": wanT3E3StatsSEFSs,
       "wanT3E3StatsUASs": wanT3E3StatsUASs,
       "wanT3E3StatsLCVs": wanT3E3StatsLCVs,
       "wanT3E3StatsPCVs": wanT3E3StatsPCVs,
       "wanT3E3StatsLESs": wanT3E3StatsLESs,
       "wanT3E3StatsCCVs": wanT3E3StatsCCVs,
       "wanT3E3StatsCESs": wanT3E3StatsCESs,
       "wanT3E3StatsCSESs": wanT3E3StatsCSESs,
       "wanT3E3StatsRAIs": wanT3E3StatsRAIs,
       "wanT3E3StatsAISs": wanT3E3StatsAISs,
       "wanT3E3StatsLOFs": wanT3E3StatsLOFs,
       "wanT3E3StatsLOSs": wanT3E3StatsLOSs,
       "wanT3E3StatsOwner": wanT3E3StatsOwner,
       "wanT3E3StatsStatus": wanT3E3StatsStatus,
       "wanAtmStatsTable": wanAtmStatsTable,
       "wanAtmStatsEntry": wanAtmStatsEntry,
       "wanAtmStatsIndex": wanAtmStatsIndex,
       "wanAtmStatsDataSource": wanAtmStatsDataSource,
       "wanAtmStatsDropEvents": wanAtmStatsDropEvents,
       "wanAtmStatsInCells": wanAtmStatsInCells,
       "wanAtmStatsOutCells": wanAtmStatsOutCells,
       "wanAtmStatsInCLP1": wanAtmStatsInCLP1,
       "wanAtmStatsOutCLP1": wanAtmStatsOutCLP1,
       "wanAtmStatsConnectionEvents": wanAtmStatsConnectionEvents,
       "wanAtmStatsErroredPDUs": wanAtmStatsErroredPDUs,
       "wanAtmStatsSetupAttempts": wanAtmStatsSetupAttempts,
       "wanAtmStatsInRoutesUnavailable": wanAtmStatsInRoutesUnavailable,
       "wanAtmStatsOutRoutesUnavailable": wanAtmStatsOutRoutesUnavailable,
       "wanAtmStatsInResourcesUnavailable": wanAtmStatsInResourcesUnavailable,
       "wanAtmStatsOutResourcesUnavailable": wanAtmStatsOutResourcesUnavailable,
       "wanAtmStatsInUnsuccessfulCalls": wanAtmStatsInUnsuccessfulCalls,
       "wanAtmStatsOutUnsuccessfulCalls": wanAtmStatsOutUnsuccessfulCalls,
       "wanAtmStatsInIncorrectMsgs": wanAtmStatsInIncorrectMsgs,
       "wanAtmStatsOutIncorrectMsgs": wanAtmStatsOutIncorrectMsgs,
       "wanAtmStatsInPartyEvents": wanAtmStatsInPartyEvents,
       "wanAtmStatsOutPartyEvents": wanAtmStatsOutPartyEvents,
       "wanAtmStatsInExpiries": wanAtmStatsInExpiries,
       "wanAtmStatsOutExpiries": wanAtmStatsOutExpiries,
       "wanAtmStatsInRestartErrors": wanAtmStatsInRestartErrors,
       "wanAtmStatsOutRestartErrors": wanAtmStatsOutRestartErrors,
       "wanAtmStatsInSVCs": wanAtmStatsInSVCs,
       "wanAtmStatsOutSVCs": wanAtmStatsOutSVCs,
       "wanAtmStatsInOCDs": wanAtmStatsInOCDs,
       "wanAtmStatsOutOCDs": wanAtmStatsOutOCDs,
       "wanAtmStatsInLOCs": wanAtmStatsInLOCs,
       "wanAtmStatsOutLOCs": wanAtmStatsOutLOCs,
       "wanAtmStatsInLOFs": wanAtmStatsInLOFs,
       "wanAtmStatsOutLOFs": wanAtmStatsOutLOFs,
       "wanAtmStatsInLOPs": wanAtmStatsInLOPs,
       "wanAtmStatsOutLOPs": wanAtmStatsOutLOPs,
       "wanAtmStatsInLOSs": wanAtmStatsInLOSs,
       "wanAtmStatsOutLOSs": wanAtmStatsOutLOSs,
       "wanAtmStatsOwner": wanAtmStatsOwner,
       "wanAtmStatsStatus": wanAtmStatsStatus,
       "wanProtocolStats": wanProtocolStats,
       "wanX25StatsTable": wanX25StatsTable,
       "wanX25StatsEntry": wanX25StatsEntry,
       "wanX25StatsIndex": wanX25StatsIndex,
       "wanX25StatsDataSource": wanX25StatsDataSource,
       "wanX25StatsDropEvents": wanX25StatsDropEvents,
       "wanX25StatsInFrames": wanX25StatsInFrames,
       "wanX25StatsOutFrames": wanX25StatsOutFrames,
       "wanX25StatsInOctets": wanX25StatsInOctets,
       "wanX25StatsOutOctets": wanX25StatsOutOctets,
       "wanX25StatsInRejects": wanX25StatsInRejects,
       "wanX25StatsOutRejects": wanX25StatsOutRejects,
       "wanX25StatsInAttempts": wanX25StatsInAttempts,
       "wanX25StatsOutAttempts": wanX25StatsOutAttempts,
       "wanX25StatsInFailures": wanX25StatsInFailures,
       "wanX25StatsOutFailures": wanX25StatsOutFailures,
       "wanX25StatsProviderClears": wanX25StatsProviderClears,
       "wanX25StatsInResets": wanX25StatsInResets,
       "wanX25StatsOutResets": wanX25StatsOutResets,
       "wanX25StatsProviderResets": wanX25StatsProviderResets,
       "wanX25StatsInAccusedErrors": wanX25StatsInAccusedErrors,
       "wanX25StatsOutAccusedErrors": wanX25StatsOutAccusedErrors,
       "wanX25StatsInInterrupts": wanX25StatsInInterrupts,
       "wanX25StatsOutInterrupts": wanX25StatsOutInterrupts,
       "wanX25StatsOwner": wanX25StatsOwner,
       "wanX25StatsStatus": wanX25StatsStatus,
       "wanFrStatsTable": wanFrStatsTable,
       "wanFrStatsEntry": wanFrStatsEntry,
       "wanFrStatsIndex": wanFrStatsIndex,
       "wanFrStatsDataSource": wanFrStatsDataSource,
       "wanFrStatsDropEvents": wanFrStatsDropEvents,
       "wanFrStatsInFrames": wanFrStatsInFrames,
       "wanFrStatsOutFrames": wanFrStatsOutFrames,
       "wanFrStatsInOctets": wanFrStatsInOctets,
       "wanFrStatsOutOctets": wanFrStatsOutOctets,
       "wanFrStatsInFECNs": wanFrStatsInFECNs,
       "wanFrStatsOutFECNs": wanFrStatsOutFECNs,
       "wanFrStatsInBECNs": wanFrStatsInBECNs,
       "wanFrStatsOutBECNs": wanFrStatsOutBECNs,
       "wanFrStatsInDEs": wanFrStatsInDEs,
       "wanFrStatsOutDEs": wanFrStatsOutDEs,
       "wanFrStatsOwner": wanFrStatsOwner,
       "wanFrStatsStatus": wanFrStatsStatus,
       "wanAal5StatsTable": wanAal5StatsTable,
       "wanAal5StatsEntry": wanAal5StatsEntry,
       "wanAal5StatsIndex": wanAal5StatsIndex,
       "wanAal5StatsDataSource": wanAal5StatsDataSource,
       "wanAal5StatsDropEvents": wanAal5StatsDropEvents,
       "wanAal5StatsInCells": wanAal5StatsInCells,
       "wanAal5StatsOutCells": wanAal5StatsOutCells,
       "wanAal5StatsInPDUs": wanAal5StatsInPDUs,
       "wanAal5StatsOutPDUs": wanAal5StatsOutPDUs,
       "wanAal5StatsInOctets": wanAal5StatsInOctets,
       "wanAal5StatsOutOctets": wanAal5StatsOutOctets,
       "wanAal5StatsInCLP1": wanAal5StatsInCLP1,
       "wanAal5StatsOutCLP1": wanAal5StatsOutCLP1,
       "wanAal5StatsInCRCs": wanAal5StatsInCRCs,
       "wanAal5StatsOutCRCs": wanAal5StatsOutCRCs,
       "wanAal5StatsInOversizedSDUs": wanAal5StatsInOversizedSDUs,
       "wanAal5StatsOutOversizedSDUs": wanAal5StatsOutOversizedSDUs,
       "wanAal5StatsInSVCs": wanAal5StatsInSVCs,
       "wanAal5StatsOutSVCs": wanAal5StatsOutSVCs,
       "wanAal5StatsOwner": wanAal5StatsOwner,
       "wanAal5StatsStatus": wanAal5StatsStatus,
       "wanPppStatsTable": wanPppStatsTable,
       "wanPppStatsEntry": wanPppStatsEntry,
       "wanPppStatsIndex": wanPppStatsIndex,
       "wanPppStatsDataSource": wanPppStatsDataSource,
       "wanPppStatsDropEvents": wanPppStatsDropEvents,
       "wanPppStatsInFrames": wanPppStatsInFrames,
       "wanPppStatsOutFrames": wanPppStatsOutFrames,
       "wanPppStatsInOctets": wanPppStatsInOctets,
       "wanPppStatsOutOctets": wanPppStatsOutOctets,
       "wanPppStatsInBadAddresses": wanPppStatsInBadAddresses,
       "wanPppStatsOutBadAddresses": wanPppStatsOutBadAddresses,
       "wanPppStatsInBadControls": wanPppStatsInBadControls,
       "wanPppStatsOutBadControls": wanPppStatsOutBadControls,
       "wanPppStatsInLongFrames": wanPppStatsInLongFrames,
       "wanPppStatsOutLongFrames": wanPppStatsOutLongFrames,
       "wanPppStatsInBadFCSs": wanPppStatsInBadFCSs,
       "wanPppStatsOutBadFCSs": wanPppStatsOutBadFCSs,
       "wanPppStatsOwner": wanPppStatsOwner,
       "wanPppStatsStatus": wanPppStatsStatus,
       "wanPvcStats": wanPvcStats,
       "wanX25PvcStatsTable": wanX25PvcStatsTable,
       "wanX25PvcStatsEntry": wanX25PvcStatsEntry,
       "wanX25PvcStatsIndex": wanX25PvcStatsIndex,
       "wanX25PvcStatsDataSource": wanX25PvcStatsDataSource,
       "wanX25PvcStatsDropEvents": wanX25PvcStatsDropEvents,
       "wanX25PvcStatsInFrames": wanX25PvcStatsInFrames,
       "wanX25PvcStatsOutFrames": wanX25PvcStatsOutFrames,
       "wanX25PvcStatsInOctets": wanX25PvcStatsInOctets,
       "wanX25PvcStatsOutOctets": wanX25PvcStatsOutOctets,
       "wanX25PvcStatsInResets": wanX25PvcStatsInResets,
       "wanX25PvcStatsOutResets": wanX25PvcStatsOutResets,
       "wanX25PvcStatsProviderResets": wanX25PvcStatsProviderResets,
       "wanX25PvcStatsInAccusedErrors": wanX25PvcStatsInAccusedErrors,
       "wanX25PvcStatsOutAccusedErrors": wanX25PvcStatsOutAccusedErrors,
       "wanX25PvcStatsInInterrupts": wanX25PvcStatsInInterrupts,
       "wanX25PvcStatsOutInterrupts": wanX25PvcStatsOutInterrupts,
       "wanX25PvcStatsUpTime": wanX25PvcStatsUpTime,
       "wanX25PvcStatsDownTime": wanX25PvcStatsDownTime,
       "wanX25PvcStatsState": wanX25PvcStatsState,
       "wanX25PvcStatsStateChanges": wanX25PvcStatsStateChanges,
       "wanX25PvcStatsOwner": wanX25PvcStatsOwner,
       "wanX25PvcStatsStatus": wanX25PvcStatsStatus,
       "wanFrPvcStatsTable": wanFrPvcStatsTable,
       "wanFrPvcStatsEntry": wanFrPvcStatsEntry,
       "wanFrPvcStatsIndex": wanFrPvcStatsIndex,
       "wanFrPvcStatsDataSource": wanFrPvcStatsDataSource,
       "wanFrPvcStatsDropEvents": wanFrPvcStatsDropEvents,
       "wanFrPvcStatsInFrames": wanFrPvcStatsInFrames,
       "wanFrPvcStatsOutFrames": wanFrPvcStatsOutFrames,
       "wanFrPvcStatsInOctets": wanFrPvcStatsInOctets,
       "wanFrPvcStatsOutOctets": wanFrPvcStatsOutOctets,
       "wanFrPvcStatsInFECNs": wanFrPvcStatsInFECNs,
       "wanFrPvcStatsOutFECNs": wanFrPvcStatsOutFECNs,
       "wanFrPvcStatsInBECNs": wanFrPvcStatsInBECNs,
       "wanFrPvcStatsOutBECNs": wanFrPvcStatsOutBECNs,
       "wanFrPvcStatsInDEs": wanFrPvcStatsInDEs,
       "wanFrPvcStatsOutDEs": wanFrPvcStatsOutDEs,
       "wanFrPvcStatsUpTime": wanFrPvcStatsUpTime,
       "wanFrPvcStatsDownTime": wanFrPvcStatsDownTime,
       "wanFrPvcStatsState": wanFrPvcStatsState,
       "wanFrPvcStatsStateChanges": wanFrPvcStatsStateChanges,
       "wanFrPvcStatsOwner": wanFrPvcStatsOwner,
       "wanFrPvcStatsStatus": wanFrPvcStatsStatus,
       "wanAal5PvcStatsTable": wanAal5PvcStatsTable,
       "wanAal5PvcStatsEntry": wanAal5PvcStatsEntry,
       "wanAal5PvcStatsIndex": wanAal5PvcStatsIndex,
       "wanAal5PvcStatsDataSource": wanAal5PvcStatsDataSource,
       "wanAal5PvcStatsDropEvents": wanAal5PvcStatsDropEvents,
       "wanAal5PvcStatsInCells": wanAal5PvcStatsInCells,
       "wanAal5PvcStatsOutCells": wanAal5PvcStatsOutCells,
       "wanAal5PvcStatsInPDUs": wanAal5PvcStatsInPDUs,
       "wanAal5PvcStatsOutPDUs": wanAal5PvcStatsOutPDUs,
       "wanAal5PvcStatsInOctets": wanAal5PvcStatsInOctets,
       "wanAal5PvcStatsOutOctets": wanAal5PvcStatsOutOctets,
       "wanAal5PvcStatsInCLP1": wanAal5PvcStatsInCLP1,
       "wanAal5PvcStatsOutCLP1": wanAal5PvcStatsOutCLP1,
       "wanAal5PvcStatsInCRCs": wanAal5PvcStatsInCRCs,
       "wanAal5PvcStatsOutCRCs": wanAal5PvcStatsOutCRCs,
       "wanAal5PvcStatsInOversizedSDUs": wanAal5PvcStatsInOversizedSDUs,
       "wanAal5PvcStatsOutOversizedSDUs": wanAal5PvcStatsOutOversizedSDUs,
       "wanAal5PvcStatsUpTime": wanAal5PvcStatsUpTime,
       "wanAal5PvcStatsDownTime": wanAal5PvcStatsDownTime,
       "wanAal5PvcStatsState": wanAal5PvcStatsState,
       "wanAal5PvcStatsStateChanges": wanAal5PvcStatsStateChanges,
       "wanAal5PvcStatsOwner": wanAal5PvcStatsOwner,
       "wanAal5PvcStatsStatus": wanAal5PvcStatsStatus,
       "wanHistoryMIBObjects": wanHistoryMIBObjects,
       "wanSignalingHistory": wanSignalingHistory,
       "wanT1E1HistoryTable": wanT1E1HistoryTable,
       "wanT1E1HistoryEntry": wanT1E1HistoryEntry,
       "wanT1E1HistoryIndex": wanT1E1HistoryIndex,
       "wanT1E1HistorySampleIndex": wanT1E1HistorySampleIndex,
       "wanT1E1HistoryIntervalStart": wanT1E1HistoryIntervalStart,
       "wanT1E1HistoryDropEvents": wanT1E1HistoryDropEvents,
       "wanT1E1HistoryInFrames": wanT1E1HistoryInFrames,
       "wanT1E1HistoryOutFrames": wanT1E1HistoryOutFrames,
       "wanT1E1HistoryInOctets": wanT1E1HistoryInOctets,
       "wanT1E1HistoryOutOctets": wanT1E1HistoryOutOctets,
       "wanT1E1HistoryESs": wanT1E1HistoryESs,
       "wanT1E1HistorySESs": wanT1E1HistorySESs,
       "wanT1E1HistorySEFSs": wanT1E1HistorySEFSs,
       "wanT1E1HistoryOOFs": wanT1E1HistoryOOFs,
       "wanT1E1HistoryUASs": wanT1E1HistoryUASs,
       "wanT1E1HistoryCSSs": wanT1E1HistoryCSSs,
       "wanT1E1HistoryPCVs": wanT1E1HistoryPCVs,
       "wanT1E1HistoryLESs": wanT1E1HistoryLESs,
       "wanT1E1HistoryBESs": wanT1E1HistoryBESs,
       "wanT1E1HistoryDMs": wanT1E1HistoryDMs,
       "wanT1E1HistoryLCVs": wanT1E1HistoryLCVs,
       "wanT1E1HistoryLOFs": wanT1E1HistoryLOFs,
       "wanT1E1HistoryLOSs": wanT1E1HistoryLOSs,
       "wanT1E1HistoryRAIs": wanT1E1HistoryRAIs,
       "wanT1E1HistoryAISs": wanT1E1HistoryAISs,
       "wanT1E1HistoryTS16AISs": wanT1E1HistoryTS16AISs,
       "wanT1E1HistoryLOMFs": wanT1E1HistoryLOMFs,
       "wanT1E1HistoryFarLOMFs": wanT1E1HistoryFarLOMFs,
       "wanT1E1HistoryInUtilization": wanT1E1HistoryInUtilization,
       "wanT1E1HistoryOutUtilization": wanT1E1HistoryOutUtilization,
       "wanVSeriesHistoryTable": wanVSeriesHistoryTable,
       "wanVSeriesHistoryEntry": wanVSeriesHistoryEntry,
       "wanVSeriesHistoryIndex": wanVSeriesHistoryIndex,
       "wanVSeriesHistorySampleIndex": wanVSeriesHistorySampleIndex,
       "wanVSeriesHistoryIntervalStart": wanVSeriesHistoryIntervalStart,
       "wanVSeriesHistoryDropEvents": wanVSeriesHistoryDropEvents,
       "wanVSeriesHistoryInFrames": wanVSeriesHistoryInFrames,
       "wanVSeriesHistoryOutFrames": wanVSeriesHistoryOutFrames,
       "wanVSeriesHistoryInOctets": wanVSeriesHistoryInOctets,
       "wanVSeriesHistoryOutOctets": wanVSeriesHistoryOutOctets,
       "wanVSeriesHistoryInFCSs": wanVSeriesHistoryInFCSs,
       "wanVSeriesHistoryOutFCSs": wanVSeriesHistoryOutFCSs,
       "wanVSeriesHistoryInOverruns": wanVSeriesHistoryInOverruns,
       "wanVSeriesHistoryOutOverruns": wanVSeriesHistoryOutOverruns,
       "wanVSeriesHistoryInterruptedFrames": wanVSeriesHistoryInterruptedFrames,
       "wanVSeriesHistoryInAbortedFrames": wanVSeriesHistoryInAbortedFrames,
       "wanVSeriesHistoryOutAbortedFrames": wanVSeriesHistoryOutAbortedFrames,
       "wanVSeriesHistoryInUtilization": wanVSeriesHistoryInUtilization,
       "wanVSeriesHistoryOutUtilization": wanVSeriesHistoryOutUtilization,
       "wanHssiHistoryTable": wanHssiHistoryTable,
       "wanHssiHistoryEntry": wanHssiHistoryEntry,
       "wanHssiHistoryIndex": wanHssiHistoryIndex,
       "wanHssiHistorySampleIndex": wanHssiHistorySampleIndex,
       "wanHssiHistoryIntervalStart": wanHssiHistoryIntervalStart,
       "wanHssiHistoryDropEvents": wanHssiHistoryDropEvents,
       "wanHssiHistoryInFrames": wanHssiHistoryInFrames,
       "wanHssiHistoryOutFrames": wanHssiHistoryOutFrames,
       "wanHssiHistoryInOctets": wanHssiHistoryInOctets,
       "wanHssiHistoryOutOctets": wanHssiHistoryOutOctets,
       "wanHssiHistoryRxLongFrames": wanHssiHistoryRxLongFrames,
       "wanHssiHistoryRxCrcErrors": wanHssiHistoryRxCrcErrors,
       "wanHssiHistoryRxOverruns": wanHssiHistoryRxOverruns,
       "wanHssiHistoryRxAborts": wanHssiHistoryRxAborts,
       "wanHssiHistoryTxAborts": wanHssiHistoryTxAborts,
       "wanHssiHistoryTxUnderruns": wanHssiHistoryTxUnderruns,
       "wanHssiHistoryRxRingErrors": wanHssiHistoryRxRingErrors,
       "wanHssiHistoryRxRingOverruns": wanHssiHistoryRxRingOverruns,
       "wanHssiHistoryTxRingErrors": wanHssiHistoryTxRingErrors,
       "wanHssiHistoryPortOpErrors": wanHssiHistoryPortOpErrors,
       "wanHssiHistoryTxCmplProcessings": wanHssiHistoryTxCmplProcessings,
       "wanHssiHistoryInUtilization": wanHssiHistoryInUtilization,
       "wanHssiHistoryOutUtilization": wanHssiHistoryOutUtilization,
       "wanT3E3HistoryTable": wanT3E3HistoryTable,
       "wanT3E3HistoryEntry": wanT3E3HistoryEntry,
       "wanT3E3HistoryIndex": wanT3E3HistoryIndex,
       "wanT3E3HistorySampleIndex": wanT3E3HistorySampleIndex,
       "wanT3E3HistoryIntervalStart": wanT3E3HistoryIntervalStart,
       "wanT3E3HistoryDropEvents": wanT3E3HistoryDropEvents,
       "wanT3E3HistoryInFrames": wanT3E3HistoryInFrames,
       "wanT3E3HistoryOutFrames": wanT3E3HistoryOutFrames,
       "wanT3E3HistoryInOctets": wanT3E3HistoryInOctets,
       "wanT3E3HistoryOutOctets": wanT3E3HistoryOutOctets,
       "wanT3E3HistoryPESs": wanT3E3HistoryPESs,
       "wanT3E3HistoryPSESs": wanT3E3HistoryPSESs,
       "wanT3E3HistoryOOFs": wanT3E3HistoryOOFs,
       "wanT3E3HistorySEFSs": wanT3E3HistorySEFSs,
       "wanT3E3HistoryUASs": wanT3E3HistoryUASs,
       "wanT3E3HistoryLCVs": wanT3E3HistoryLCVs,
       "wanT3E3HistoryPCVs": wanT3E3HistoryPCVs,
       "wanT3E3HistoryLESs": wanT3E3HistoryLESs,
       "wanT3E3HistoryCCVs": wanT3E3HistoryCCVs,
       "wanT3E3HistoryCESs": wanT3E3HistoryCESs,
       "wanT3E3HistoryCSESs": wanT3E3HistoryCSESs,
       "wanT3E3HistoryRAIs": wanT3E3HistoryRAIs,
       "wanT3E3HistoryAISs": wanT3E3HistoryAISs,
       "wanT3E3HistoryLOFs": wanT3E3HistoryLOFs,
       "wanT3E3HistoryLOSs": wanT3E3HistoryLOSs,
       "wanT3E3HistoryInUtilization": wanT3E3HistoryInUtilization,
       "wanT3E3HistoryOutUtilization": wanT3E3HistoryOutUtilization,
       "wanAtmHistoryTable": wanAtmHistoryTable,
       "wanAtmHistoryEntry": wanAtmHistoryEntry,
       "wanAtmHistoryIndex": wanAtmHistoryIndex,
       "wanAtmHistorySampleIndex": wanAtmHistorySampleIndex,
       "wanAtmHistoryIntervalStart": wanAtmHistoryIntervalStart,
       "wanAtmHistoryDropEvents": wanAtmHistoryDropEvents,
       "wanAtmHistoryInCells": wanAtmHistoryInCells,
       "wanAtmHistoryOutCells": wanAtmHistoryOutCells,
       "wanAtmHistoryInCLP1": wanAtmHistoryInCLP1,
       "wanAtmHistoryOutCLP1": wanAtmHistoryOutCLP1,
       "wanAtmHistoryConnectionEvents": wanAtmHistoryConnectionEvents,
       "wanAtmHistoryErroredPDUs": wanAtmHistoryErroredPDUs,
       "wanAtmHistorySetupAttempts": wanAtmHistorySetupAttempts,
       "wanAtmHistoryInRoutesUnavailable": wanAtmHistoryInRoutesUnavailable,
       "wanAtmHistoryOutRoutesUnavailable": wanAtmHistoryOutRoutesUnavailable,
       "wanAtmHistoryInResourcesUnavailable": wanAtmHistoryInResourcesUnavailable,
       "wanAtmHistoryOutResourcesUnavailable": wanAtmHistoryOutResourcesUnavailable,
       "wanAtmHistoryInUnsuccessfulCalls": wanAtmHistoryInUnsuccessfulCalls,
       "wanAtmHistoryOutUnsuccessfulCalls": wanAtmHistoryOutUnsuccessfulCalls,
       "wanAtmHistoryInIncorrectMsgs": wanAtmHistoryInIncorrectMsgs,
       "wanAtmHistoryOutIncorrectMsgs": wanAtmHistoryOutIncorrectMsgs,
       "wanAtmHistoryInPartyEvents": wanAtmHistoryInPartyEvents,
       "wanAtmHistoryOutPartyEvents": wanAtmHistoryOutPartyEvents,
       "wanAtmHistoryInExpiries": wanAtmHistoryInExpiries,
       "wanAtmHistoryOutExpiries": wanAtmHistoryOutExpiries,
       "wanAtmHistoryInRestartErrors": wanAtmHistoryInRestartErrors,
       "wanAtmHistoryOutRestartErrors": wanAtmHistoryOutRestartErrors,
       "wanAtmHistoryInSVCs": wanAtmHistoryInSVCs,
       "wanAtmHistoryOutSVCs": wanAtmHistoryOutSVCs,
       "wanAtmHistoryInOCDs": wanAtmHistoryInOCDs,
       "wanAtmHistoryOutOCDs": wanAtmHistoryOutOCDs,
       "wanAtmHistoryInLOCs": wanAtmHistoryInLOCs,
       "wanAtmHistoryOutLOCs": wanAtmHistoryOutLOCs,
       "wanAtmHistoryInLOFs": wanAtmHistoryInLOFs,
       "wanAtmHistoryOutLOFs": wanAtmHistoryOutLOFs,
       "wanAtmHistoryInLOPs": wanAtmHistoryInLOPs,
       "wanAtmHistoryOutLOPs": wanAtmHistoryOutLOPs,
       "wanAtmHistoryInLOSs": wanAtmHistoryInLOSs,
       "wanAtmHistoryOutLOSs": wanAtmHistoryOutLOSs,
       "wanAtmHistoryInUtilization": wanAtmHistoryInUtilization,
       "wanAtmHistoryOutUtilization": wanAtmHistoryOutUtilization,
       "wanProtocolHistory": wanProtocolHistory,
       "wanX25HistoryTable": wanX25HistoryTable,
       "wanX25HistoryEntry": wanX25HistoryEntry,
       "wanX25HistoryIndex": wanX25HistoryIndex,
       "wanX25HistorySampleIndex": wanX25HistorySampleIndex,
       "wanX25HistoryIntervalStart": wanX25HistoryIntervalStart,
       "wanX25HistoryDropEvents": wanX25HistoryDropEvents,
       "wanX25HistoryInFrames": wanX25HistoryInFrames,
       "wanX25HistoryOutFrames": wanX25HistoryOutFrames,
       "wanX25HistoryInOctets": wanX25HistoryInOctets,
       "wanX25HistoryOutOctets": wanX25HistoryOutOctets,
       "wanX25HistoryInRejects": wanX25HistoryInRejects,
       "wanX25HistoryOutRejects": wanX25HistoryOutRejects,
       "wanX25HistoryInAttempts": wanX25HistoryInAttempts,
       "wanX25HistoryOutAttempts": wanX25HistoryOutAttempts,
       "wanX25HistoryInFailures": wanX25HistoryInFailures,
       "wanX25HistoryOutFailures": wanX25HistoryOutFailures,
       "wanX25HistoryProviderClears": wanX25HistoryProviderClears,
       "wanX25HistoryInResets": wanX25HistoryInResets,
       "wanX25HistoryOutResets": wanX25HistoryOutResets,
       "wanX25HistoryProviderResets": wanX25HistoryProviderResets,
       "wanX25HistoryInAccusedErrors": wanX25HistoryInAccusedErrors,
       "wanX25HistoryOutAccusedErrors": wanX25HistoryOutAccusedErrors,
       "wanX25HistoryInInterrupts": wanX25HistoryInInterrupts,
       "wanX25HistoryOutInterrupts": wanX25HistoryOutInterrupts,
       "wanX25HistoryInUtilization": wanX25HistoryInUtilization,
       "wanX25HistoryOutUtilization": wanX25HistoryOutUtilization,
       "wanFrHistoryTable": wanFrHistoryTable,
       "wanFrHistoryEntry": wanFrHistoryEntry,
       "wanFrHistoryIndex": wanFrHistoryIndex,
       "wanFrHistorySampleIndex": wanFrHistorySampleIndex,
       "wanFrHistoryIntervalStart": wanFrHistoryIntervalStart,
       "wanFrHistoryDropEvents": wanFrHistoryDropEvents,
       "wanFrHistoryInFrames": wanFrHistoryInFrames,
       "wanFrHistoryOutFrames": wanFrHistoryOutFrames,
       "wanFrHistoryInOctets": wanFrHistoryInOctets,
       "wanFrHistoryOutOctets": wanFrHistoryOutOctets,
       "wanFrHistoryInFECNs": wanFrHistoryInFECNs,
       "wanFrHistoryOutFECNs": wanFrHistoryOutFECNs,
       "wanFrHistoryInBECNs": wanFrHistoryInBECNs,
       "wanFrHistoryOutBECNs": wanFrHistoryOutBECNs,
       "wanFrHistoryInDEs": wanFrHistoryInDEs,
       "wanFrHistoryOutDEs": wanFrHistoryOutDEs,
       "wanFrHistoryInUtilization": wanFrHistoryInUtilization,
       "wanFrHistoryOutUtilization": wanFrHistoryOutUtilization,
       "wanAal5HistoryTable": wanAal5HistoryTable,
       "wanAal5HistoryEntry": wanAal5HistoryEntry,
       "wanAal5HistoryIndex": wanAal5HistoryIndex,
       "wanAal5HistorySampleIndex": wanAal5HistorySampleIndex,
       "wanAal5HistoryIntervalStart": wanAal5HistoryIntervalStart,
       "wanAal5HistoryDropEvents": wanAal5HistoryDropEvents,
       "wanAal5HistoryInCells": wanAal5HistoryInCells,
       "wanAal5HistoryOutCells": wanAal5HistoryOutCells,
       "wanAal5HistoryInPDUs": wanAal5HistoryInPDUs,
       "wanAal5HistoryOutPDUs": wanAal5HistoryOutPDUs,
       "wanAal5HistoryInOctets": wanAal5HistoryInOctets,
       "wanAal5HistoryOutOctets": wanAal5HistoryOutOctets,
       "wanAal5HistoryInCLP1": wanAal5HistoryInCLP1,
       "wanAal5HistoryOutCLP1": wanAal5HistoryOutCLP1,
       "wanAal5HistoryInCRCs": wanAal5HistoryInCRCs,
       "wanAal5HistoryOutCRCs": wanAal5HistoryOutCRCs,
       "wanAal5HistoryInOversizedSDUs": wanAal5HistoryInOversizedSDUs,
       "wanAal5HistoryOutOversizedSDUs": wanAal5HistoryOutOversizedSDUs,
       "wanAal5HistoryInSVCs": wanAal5HistoryInSVCs,
       "wanAal5HistoryOutSVCs": wanAal5HistoryOutSVCs,
       "wanAal5HistoryInUtilization": wanAal5HistoryInUtilization,
       "wanAal5HistoryOutUtilization": wanAal5HistoryOutUtilization,
       "wanPppHistoryTable": wanPppHistoryTable,
       "wanPppHistoryEntry": wanPppHistoryEntry,
       "wanPppHistoryIndex": wanPppHistoryIndex,
       "wanPppHistorySampleIndex": wanPppHistorySampleIndex,
       "wanPppHistoryIntervalStart": wanPppHistoryIntervalStart,
       "wanPppHistoryDropEvents": wanPppHistoryDropEvents,
       "wanPppHistoryInFrames": wanPppHistoryInFrames,
       "wanPppHistoryOutFrames": wanPppHistoryOutFrames,
       "wanPppHistoryInOctets": wanPppHistoryInOctets,
       "wanPppHistoryOutOctets": wanPppHistoryOutOctets,
       "wanPppHistoryInBadAddresses": wanPppHistoryInBadAddresses,
       "wanPppHistoryOutBadAddresses": wanPppHistoryOutBadAddresses,
       "wanPppHistoryInBadControls": wanPppHistoryInBadControls,
       "wanPppHistoryOutBadControls": wanPppHistoryOutBadControls,
       "wanPppHistoryInLongFrames": wanPppHistoryInLongFrames,
       "wanPppHistoryOutLongFrames": wanPppHistoryOutLongFrames,
       "wanPppHistoryInBadFCSs": wanPppHistoryInBadFCSs,
       "wanPppHistoryOutBadFCSs": wanPppHistoryOutBadFCSs,
       "wanPppHistoryInUtilization": wanPppHistoryInUtilization,
       "wanPppHistoryOutUtilization": wanPppHistoryOutUtilization,
       "wanPvcHistory": wanPvcHistory,
       "wanX25PvcHistoryTable": wanX25PvcHistoryTable,
       "wanX25PvcHistoryEntry": wanX25PvcHistoryEntry,
       "wanX25PvcHistoryIndex": wanX25PvcHistoryIndex,
       "wanX25PvcHistorySampleIndex": wanX25PvcHistorySampleIndex,
       "wanX25PvcHistoryIntervalStart": wanX25PvcHistoryIntervalStart,
       "wanX25PvcHistoryDropEvents": wanX25PvcHistoryDropEvents,
       "wanX25PvcHistoryInFrames": wanX25PvcHistoryInFrames,
       "wanX25PvcHistoryOutFrames": wanX25PvcHistoryOutFrames,
       "wanX25PvcHistoryInOctets": wanX25PvcHistoryInOctets,
       "wanX25PvcHistoryOutOctets": wanX25PvcHistoryOutOctets,
       "wanX25PvcHistoryInResets": wanX25PvcHistoryInResets,
       "wanX25PvcHistoryOutResets": wanX25PvcHistoryOutResets,
       "wanX25PvcHistoryProviderResets": wanX25PvcHistoryProviderResets,
       "wanX25PvcHistoryInAccusedErrors": wanX25PvcHistoryInAccusedErrors,
       "wanX25PvcHistoryOutAccusedErrors": wanX25PvcHistoryOutAccusedErrors,
       "wanX25PvcHistoryInInterrupts": wanX25PvcHistoryInInterrupts,
       "wanX25PvcHistoryOutInterrupts": wanX25PvcHistoryOutInterrupts,
       "wanX25PvcHistoryUpTime": wanX25PvcHistoryUpTime,
       "wanX25PvcHistoryDownTime": wanX25PvcHistoryDownTime,
       "wanX25PvcHistoryStateChanges": wanX25PvcHistoryStateChanges,
       "wanX25PvcHistoryInUtilization": wanX25PvcHistoryInUtilization,
       "wanX25PvcHistoryOutUtilization": wanX25PvcHistoryOutUtilization,
       "wanFrPvcHistoryTable": wanFrPvcHistoryTable,
       "wanFrPvcHistoryEntry": wanFrPvcHistoryEntry,
       "wanFrPvcHistoryIndex": wanFrPvcHistoryIndex,
       "wanFrPvcHistorySampleIndex": wanFrPvcHistorySampleIndex,
       "wanFrPvcHistoryIntervalStart": wanFrPvcHistoryIntervalStart,
       "wanFrPvcHistoryDropEvents": wanFrPvcHistoryDropEvents,
       "wanFrPvcHistoryInFrames": wanFrPvcHistoryInFrames,
       "wanFrPvcHistoryOutFrames": wanFrPvcHistoryOutFrames,
       "wanFrPvcHistoryInOctets": wanFrPvcHistoryInOctets,
       "wanFrPvcHistoryOutOctets": wanFrPvcHistoryOutOctets,
       "wanFrPvcHistoryInFECNs": wanFrPvcHistoryInFECNs,
       "wanFrPvcHistoryOutFECNs": wanFrPvcHistoryOutFECNs,
       "wanFrPvcHistoryInBECNs": wanFrPvcHistoryInBECNs,
       "wanFrPvcHistoryOutBECNs": wanFrPvcHistoryOutBECNs,
       "wanFrPvcHistoryInDEs": wanFrPvcHistoryInDEs,
       "wanFrPvcHistoryOutDEs": wanFrPvcHistoryOutDEs,
       "wanFrPvcHistoryUpTime": wanFrPvcHistoryUpTime,
       "wanFrPvcHistoryDownTime": wanFrPvcHistoryDownTime,
       "wanFrPvcHistoryStateChanges": wanFrPvcHistoryStateChanges,
       "wanFrPvcHistoryInUtilization": wanFrPvcHistoryInUtilization,
       "wanFrPvcHistoryOutUtilization": wanFrPvcHistoryOutUtilization,
       "wanAal5PvcHistoryTable": wanAal5PvcHistoryTable,
       "wanAal5PvcHistoryEntry": wanAal5PvcHistoryEntry,
       "wanAal5PvcHistoryIndex": wanAal5PvcHistoryIndex,
       "wanAal5PvcHistorySampleIndex": wanAal5PvcHistorySampleIndex,
       "wanAal5PvcHistoryIntervalStart": wanAal5PvcHistoryIntervalStart,
       "wanAal5PvcHistoryDropEvents": wanAal5PvcHistoryDropEvents,
       "wanAal5PvcHistoryInCells": wanAal5PvcHistoryInCells,
       "wanAal5PvcHistoryOutCells": wanAal5PvcHistoryOutCells,
       "wanAal5PvcHistoryInPDUs": wanAal5PvcHistoryInPDUs,
       "wanAal5PvcHistoryOutPDUs": wanAal5PvcHistoryOutPDUs,
       "wanAal5PvcHistoryInOctets": wanAal5PvcHistoryInOctets,
       "wanAal5PvcHistoryOutOctets": wanAal5PvcHistoryOutOctets,
       "wanAal5PvcHistoryInCLP1": wanAal5PvcHistoryInCLP1,
       "wanAal5PvcHistoryOutCLP1": wanAal5PvcHistoryOutCLP1,
       "wanAal5PvcHistoryInCRCs": wanAal5PvcHistoryInCRCs,
       "wanAal5PvcHistoryOutCRCs": wanAal5PvcHistoryOutCRCs,
       "wanAal5PvcHistoryInOversizedSDUs": wanAal5PvcHistoryInOversizedSDUs,
       "wanAal5PvcHistoryOutOversizedSDUs": wanAal5PvcHistoryOutOversizedSDUs,
       "wanAal5PvcHistoryUpTime": wanAal5PvcHistoryUpTime,
       "wanAal5PvcHistoryDownTime": wanAal5PvcHistoryDownTime,
       "wanAal5PvcHistoryStateChanges": wanAal5PvcHistoryStateChanges,
       "wanAal5PvcHistoryInUtilization": wanAal5PvcHistoryInUtilization,
       "wanAal5PvcHistoryOutUtilization": wanAal5PvcHistoryOutUtilization}
)
