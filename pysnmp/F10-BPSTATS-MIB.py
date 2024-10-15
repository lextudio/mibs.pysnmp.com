# SNMP MIB module (F10-BPSTATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/F10-BPSTATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:19 2024
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

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

f10BpStatsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24)
)
f10BpStatsMib.setRevisions(
        ("2013-05-22 12:48",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F10BpStatsLinkBundleObjects_ObjectIdentity = ObjectIdentity
f10BpStatsLinkBundleObjects = _F10BpStatsLinkBundleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 1)
)
_BpLinkBundleObjects_ObjectIdentity = ObjectIdentity
bpLinkBundleObjects = _BpLinkBundleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 1, 1)
)


class _BpLinkBundleRateInterval_Type(Integer32):
    """Custom type bpLinkBundleRateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 299),
    )


_BpLinkBundleRateInterval_Type.__name__ = "Integer32"
_BpLinkBundleRateInterval_Object = MibScalar
bpLinkBundleRateInterval = _BpLinkBundleRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 1, 1, 1),
    _BpLinkBundleRateInterval_Type()
)
bpLinkBundleRateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bpLinkBundleRateInterval.setStatus("current")


class _BpLinkBundleTriggerThreshold_Type(Integer32):
    """Custom type bpLinkBundleTriggerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_BpLinkBundleTriggerThreshold_Type.__name__ = "Integer32"
_BpLinkBundleTriggerThreshold_Object = MibScalar
bpLinkBundleTriggerThreshold = _BpLinkBundleTriggerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 1, 1, 2),
    _BpLinkBundleTriggerThreshold_Type()
)
bpLinkBundleTriggerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bpLinkBundleTriggerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    bpLinkBundleTriggerThreshold.setUnits("percent")
_F10BpStatsObjects_ObjectIdentity = ObjectIdentity
f10BpStatsObjects = _F10BpStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2)
)
_BpStatsObjects_ObjectIdentity = ObjectIdentity
bpStatsObjects = _BpStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1)
)
_BpDropsTable_Object = MibTable
bpDropsTable = _BpDropsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1)
)
if mibBuilder.loadTexts:
    bpDropsTable.setStatus("current")
_BpDropsEntry_Object = MibTableRow
bpDropsEntry = _BpDropsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1)
)
bpDropsEntry.setIndexNames(
    (0, "F10-BPSTATS-MIB", "bpDropsStackUnitIndex"),
    (0, "F10-BPSTATS-MIB", "bpDropsPortPipe"),
    (0, "F10-BPSTATS-MIB", "bpDropsPortIndex"),
)
if mibBuilder.loadTexts:
    bpDropsEntry.setStatus("current")


class _BpDropsStackUnitIndex_Type(Integer32):
    """Custom type bpDropsStackUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_BpDropsStackUnitIndex_Type.__name__ = "Integer32"
_BpDropsStackUnitIndex_Object = MibTableColumn
bpDropsStackUnitIndex = _BpDropsStackUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 1),
    _BpDropsStackUnitIndex_Type()
)
bpDropsStackUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bpDropsStackUnitIndex.setStatus("current")


class _BpDropsPortPipe_Type(Integer32):
    """Custom type bpDropsPortPipe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_BpDropsPortPipe_Type.__name__ = "Integer32"
_BpDropsPortPipe_Object = MibTableColumn
bpDropsPortPipe = _BpDropsPortPipe_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 2),
    _BpDropsPortPipe_Type()
)
bpDropsPortPipe.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bpDropsPortPipe.setStatus("current")


class _BpDropsPortIndex_Type(Integer32):
    """Custom type bpDropsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BpDropsPortIndex_Type.__name__ = "Integer32"
_BpDropsPortIndex_Object = MibTableColumn
bpDropsPortIndex = _BpDropsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 3),
    _BpDropsPortIndex_Type()
)
bpDropsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bpDropsPortIndex.setStatus("current")
_BpDropsInDrops_Type = Counter64
_BpDropsInDrops_Object = MibTableColumn
bpDropsInDrops = _BpDropsInDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 4),
    _BpDropsInDrops_Type()
)
bpDropsInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpDropsInDrops.setStatus("current")
_BpDropsInUnKnownHgHdr_Type = Counter64
_BpDropsInUnKnownHgHdr_Object = MibTableColumn
bpDropsInUnKnownHgHdr = _BpDropsInUnKnownHgHdr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 5),
    _BpDropsInUnKnownHgHdr_Type()
)
bpDropsInUnKnownHgHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpDropsInUnKnownHgHdr.setStatus("current")
_BpDropsInUnKnownHgOpcode_Type = Counter64
_BpDropsInUnKnownHgOpcode_Object = MibTableColumn
bpDropsInUnKnownHgOpcode = _BpDropsInUnKnownHgOpcode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 6),
    _BpDropsInUnKnownHgOpcode_Type()
)
bpDropsInUnKnownHgOpcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpDropsInUnKnownHgOpcode.setStatus("current")
_BpDropsInMTUExceeds_Type = Counter64
_BpDropsInMTUExceeds_Object = MibTableColumn
bpDropsInMTUExceeds = _BpDropsInMTUExceeds_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 7),
    _BpDropsInMTUExceeds_Type()
)
bpDropsInMTUExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpDropsInMTUExceeds.setStatus("current")
_BpDropsInMacDrops_Type = Counter64
_BpDropsInMacDrops_Object = MibTableColumn
bpDropsInMacDrops = _BpDropsInMacDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 8),
    _BpDropsInMacDrops_Type()
)
bpDropsInMacDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpDropsInMacDrops.setStatus("current")
_BpDropsMMUHOLDrops_Type = Counter64
_BpDropsMMUHOLDrops_Object = MibTableColumn
bpDropsMMUHOLDrops = _BpDropsMMUHOLDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 9),
    _BpDropsMMUHOLDrops_Type()
)
bpDropsMMUHOLDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpDropsMMUHOLDrops.setStatus("current")
_BpDropsEgMacDrops_Type = Counter64
_BpDropsEgMacDrops_Object = MibTableColumn
bpDropsEgMacDrops = _BpDropsEgMacDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 10),
    _BpDropsEgMacDrops_Type()
)
bpDropsEgMacDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpDropsEgMacDrops.setStatus("current")
_BpDropsEgTxAgedCounter_Type = Counter64
_BpDropsEgTxAgedCounter_Object = MibTableColumn
bpDropsEgTxAgedCounter = _BpDropsEgTxAgedCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 11),
    _BpDropsEgTxAgedCounter_Type()
)
bpDropsEgTxAgedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpDropsEgTxAgedCounter.setStatus("current")
_BpDropsEgTxErrCounter_Type = Counter64
_BpDropsEgTxErrCounter_Object = MibTableColumn
bpDropsEgTxErrCounter = _BpDropsEgTxErrCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 12),
    _BpDropsEgTxErrCounter_Type()
)
bpDropsEgTxErrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpDropsEgTxErrCounter.setStatus("current")
_BpDropsEgTxMACUnderflow_Type = Counter64
_BpDropsEgTxMACUnderflow_Object = MibTableColumn
bpDropsEgTxMACUnderflow = _BpDropsEgTxMACUnderflow_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 13),
    _BpDropsEgTxMACUnderflow_Type()
)
bpDropsEgTxMACUnderflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpDropsEgTxMACUnderflow.setStatus("current")
_BpDropsEgTxErrPktCounter_Type = Counter64
_BpDropsEgTxErrPktCounter_Object = MibTableColumn
bpDropsEgTxErrPktCounter = _BpDropsEgTxErrPktCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 1, 1, 14),
    _BpDropsEgTxErrPktCounter_Type()
)
bpDropsEgTxErrPktCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpDropsEgTxErrPktCounter.setStatus("current")
_BpIfStatsTable_Object = MibTable
bpIfStatsTable = _BpIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2)
)
if mibBuilder.loadTexts:
    bpIfStatsTable.setStatus("current")
_BpIfStatsEntry_Object = MibTableRow
bpIfStatsEntry = _BpIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1)
)
bpIfStatsEntry.setIndexNames(
    (0, "F10-BPSTATS-MIB", "bpIfStatsStackUnitIndex"),
    (0, "F10-BPSTATS-MIB", "bpIfStatsPortPipe"),
    (0, "F10-BPSTATS-MIB", "bpIfStatsPortIndex"),
)
if mibBuilder.loadTexts:
    bpIfStatsEntry.setStatus("current")


class _BpIfStatsStackUnitIndex_Type(Integer32):
    """Custom type bpIfStatsStackUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_BpIfStatsStackUnitIndex_Type.__name__ = "Integer32"
_BpIfStatsStackUnitIndex_Object = MibTableColumn
bpIfStatsStackUnitIndex = _BpIfStatsStackUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 1),
    _BpIfStatsStackUnitIndex_Type()
)
bpIfStatsStackUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bpIfStatsStackUnitIndex.setStatus("current")


class _BpIfStatsPortPipe_Type(Integer32):
    """Custom type bpIfStatsPortPipe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_BpIfStatsPortPipe_Type.__name__ = "Integer32"
_BpIfStatsPortPipe_Object = MibTableColumn
bpIfStatsPortPipe = _BpIfStatsPortPipe_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 2),
    _BpIfStatsPortPipe_Type()
)
bpIfStatsPortPipe.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bpIfStatsPortPipe.setStatus("current")


class _BpIfStatsPortIndex_Type(Integer32):
    """Custom type bpIfStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BpIfStatsPortIndex_Type.__name__ = "Integer32"
_BpIfStatsPortIndex_Object = MibTableColumn
bpIfStatsPortIndex = _BpIfStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 3),
    _BpIfStatsPortIndex_Type()
)
bpIfStatsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bpIfStatsPortIndex.setStatus("current")
_BpIfStatsIn64BytePkts_Type = Counter64
_BpIfStatsIn64BytePkts_Object = MibTableColumn
bpIfStatsIn64BytePkts = _BpIfStatsIn64BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 4),
    _BpIfStatsIn64BytePkts_Type()
)
bpIfStatsIn64BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsIn64BytePkts.setStatus("current")
_BpIfStatsIn65To127BytePkts_Type = Counter64
_BpIfStatsIn65To127BytePkts_Object = MibTableColumn
bpIfStatsIn65To127BytePkts = _BpIfStatsIn65To127BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 5),
    _BpIfStatsIn65To127BytePkts_Type()
)
bpIfStatsIn65To127BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsIn65To127BytePkts.setStatus("current")
_BpIfStatsIn128To255BytePkts_Type = Counter64
_BpIfStatsIn128To255BytePkts_Object = MibTableColumn
bpIfStatsIn128To255BytePkts = _BpIfStatsIn128To255BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 6),
    _BpIfStatsIn128To255BytePkts_Type()
)
bpIfStatsIn128To255BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsIn128To255BytePkts.setStatus("current")
_BpIfStatsIn256To511BytePkts_Type = Counter64
_BpIfStatsIn256To511BytePkts_Object = MibTableColumn
bpIfStatsIn256To511BytePkts = _BpIfStatsIn256To511BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 7),
    _BpIfStatsIn256To511BytePkts_Type()
)
bpIfStatsIn256To511BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsIn256To511BytePkts.setStatus("current")
_BpIfStatsIn512To1023BytePkts_Type = Counter64
_BpIfStatsIn512To1023BytePkts_Object = MibTableColumn
bpIfStatsIn512To1023BytePkts = _BpIfStatsIn512To1023BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 8),
    _BpIfStatsIn512To1023BytePkts_Type()
)
bpIfStatsIn512To1023BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsIn512To1023BytePkts.setStatus("current")
_BpIfStatsInOver1023BytePkts_Type = Counter64
_BpIfStatsInOver1023BytePkts_Object = MibTableColumn
bpIfStatsInOver1023BytePkts = _BpIfStatsInOver1023BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 9),
    _BpIfStatsInOver1023BytePkts_Type()
)
bpIfStatsInOver1023BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsInOver1023BytePkts.setStatus("current")
_BpIfStatsInThrottles_Type = Counter64
_BpIfStatsInThrottles_Object = MibTableColumn
bpIfStatsInThrottles = _BpIfStatsInThrottles_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 10),
    _BpIfStatsInThrottles_Type()
)
bpIfStatsInThrottles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsInThrottles.setStatus("current")
_BpIfStatsInRunts_Type = Counter64
_BpIfStatsInRunts_Object = MibTableColumn
bpIfStatsInRunts = _BpIfStatsInRunts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 11),
    _BpIfStatsInRunts_Type()
)
bpIfStatsInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsInRunts.setStatus("current")
_BpIfStatsInGiants_Type = Counter64
_BpIfStatsInGiants_Object = MibTableColumn
bpIfStatsInGiants = _BpIfStatsInGiants_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 12),
    _BpIfStatsInGiants_Type()
)
bpIfStatsInGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsInGiants.setStatus("current")
_BpIfStatsInCRC_Type = Counter64
_BpIfStatsInCRC_Object = MibTableColumn
bpIfStatsInCRC = _BpIfStatsInCRC_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 13),
    _BpIfStatsInCRC_Type()
)
bpIfStatsInCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsInCRC.setStatus("current")
_BpIfStatsInOverruns_Type = Counter64
_BpIfStatsInOverruns_Object = MibTableColumn
bpIfStatsInOverruns = _BpIfStatsInOverruns_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 14),
    _BpIfStatsInOverruns_Type()
)
bpIfStatsInOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsInOverruns.setStatus("current")
_BpIfStatsOutUnderruns_Type = Counter64
_BpIfStatsOutUnderruns_Object = MibTableColumn
bpIfStatsOutUnderruns = _BpIfStatsOutUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 15),
    _BpIfStatsOutUnderruns_Type()
)
bpIfStatsOutUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsOutUnderruns.setStatus("current")
_BpIfStatsOutUnicasts_Type = Counter64
_BpIfStatsOutUnicasts_Object = MibTableColumn
bpIfStatsOutUnicasts = _BpIfStatsOutUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 16),
    _BpIfStatsOutUnicasts_Type()
)
bpIfStatsOutUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsOutUnicasts.setStatus("current")
_BpIfStatsOutCollisions_Type = Counter64
_BpIfStatsOutCollisions_Object = MibTableColumn
bpIfStatsOutCollisions = _BpIfStatsOutCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 17),
    _BpIfStatsOutCollisions_Type()
)
bpIfStatsOutCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsOutCollisions.setStatus("current")
_BpIfStatsOutWredDrops_Type = Counter64
_BpIfStatsOutWredDrops_Object = MibTableColumn
bpIfStatsOutWredDrops = _BpIfStatsOutWredDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 18),
    _BpIfStatsOutWredDrops_Type()
)
bpIfStatsOutWredDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsOutWredDrops.setStatus("current")
_BpIfStatsOut64BytePkts_Type = Counter64
_BpIfStatsOut64BytePkts_Object = MibTableColumn
bpIfStatsOut64BytePkts = _BpIfStatsOut64BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 19),
    _BpIfStatsOut64BytePkts_Type()
)
bpIfStatsOut64BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsOut64BytePkts.setStatus("current")
_BpIfStatsOut65To127BytePkts_Type = Counter64
_BpIfStatsOut65To127BytePkts_Object = MibTableColumn
bpIfStatsOut65To127BytePkts = _BpIfStatsOut65To127BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 20),
    _BpIfStatsOut65To127BytePkts_Type()
)
bpIfStatsOut65To127BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsOut65To127BytePkts.setStatus("current")
_BpIfStatsOut128To255BytePkts_Type = Counter64
_BpIfStatsOut128To255BytePkts_Object = MibTableColumn
bpIfStatsOut128To255BytePkts = _BpIfStatsOut128To255BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 21),
    _BpIfStatsOut128To255BytePkts_Type()
)
bpIfStatsOut128To255BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsOut128To255BytePkts.setStatus("current")
_BpIfStatsOut256To511BytePkts_Type = Counter64
_BpIfStatsOut256To511BytePkts_Object = MibTableColumn
bpIfStatsOut256To511BytePkts = _BpIfStatsOut256To511BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 22),
    _BpIfStatsOut256To511BytePkts_Type()
)
bpIfStatsOut256To511BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsOut256To511BytePkts.setStatus("current")
_BpIfStatsOut512To1023BytePkts_Type = Counter64
_BpIfStatsOut512To1023BytePkts_Object = MibTableColumn
bpIfStatsOut512To1023BytePkts = _BpIfStatsOut512To1023BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 23),
    _BpIfStatsOut512To1023BytePkts_Type()
)
bpIfStatsOut512To1023BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsOut512To1023BytePkts.setStatus("current")
_BpIfStatsOutOver1023BytePkts_Type = Counter64
_BpIfStatsOutOver1023BytePkts_Object = MibTableColumn
bpIfStatsOutOver1023BytePkts = _BpIfStatsOutOver1023BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 24),
    _BpIfStatsOutOver1023BytePkts_Type()
)
bpIfStatsOutOver1023BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsOutOver1023BytePkts.setStatus("current")
_BpIfStatsOutThrottles_Type = Counter64
_BpIfStatsOutThrottles_Object = MibTableColumn
bpIfStatsOutThrottles = _BpIfStatsOutThrottles_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 25),
    _BpIfStatsOutThrottles_Type()
)
bpIfStatsOutThrottles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsOutThrottles.setStatus("current")
_BpIfStatsLastDiscontinuityTime_Type = TimeStamp
_BpIfStatsLastDiscontinuityTime_Object = MibTableColumn
bpIfStatsLastDiscontinuityTime = _BpIfStatsLastDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 26),
    _BpIfStatsLastDiscontinuityTime_Type()
)
bpIfStatsLastDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsLastDiscontinuityTime.setStatus("current")


class _BpIfStatsInCentRate_Type(Integer32):
    """Custom type bpIfStatsInCentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BpIfStatsInCentRate_Type.__name__ = "Integer32"
_BpIfStatsInCentRate_Object = MibTableColumn
bpIfStatsInCentRate = _BpIfStatsInCentRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 27),
    _BpIfStatsInCentRate_Type()
)
bpIfStatsInCentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsInCentRate.setStatus("current")


class _BpIfStatsOutCentRate_Type(Integer32):
    """Custom type bpIfStatsOutCentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BpIfStatsOutCentRate_Type.__name__ = "Integer32"
_BpIfStatsOutCentRate_Object = MibTableColumn
bpIfStatsOutCentRate = _BpIfStatsOutCentRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 28),
    _BpIfStatsOutCentRate_Type()
)
bpIfStatsOutCentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsOutCentRate.setStatus("current")
_BpIfStatsLastChange_Type = TimeStamp
_BpIfStatsLastChange_Object = MibTableColumn
bpIfStatsLastChange = _BpIfStatsLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 2, 1, 29),
    _BpIfStatsLastChange_Type()
)
bpIfStatsLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpIfStatsLastChange.setStatus("current")
_BpPacketBufferTable_Object = MibTable
bpPacketBufferTable = _BpPacketBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 3)
)
if mibBuilder.loadTexts:
    bpPacketBufferTable.setStatus("current")
_BpPacketBufferEntry_Object = MibTableRow
bpPacketBufferEntry = _BpPacketBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 3, 1)
)
bpPacketBufferEntry.setIndexNames(
    (0, "F10-BPSTATS-MIB", "bpPacketBufferStackUnitIndex"),
    (0, "F10-BPSTATS-MIB", "bpPacketBufferPortPipe"),
)
if mibBuilder.loadTexts:
    bpPacketBufferEntry.setStatus("current")


class _BpPacketBufferStackUnitIndex_Type(Integer32):
    """Custom type bpPacketBufferStackUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_BpPacketBufferStackUnitIndex_Type.__name__ = "Integer32"
_BpPacketBufferStackUnitIndex_Object = MibTableColumn
bpPacketBufferStackUnitIndex = _BpPacketBufferStackUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 3, 1, 1),
    _BpPacketBufferStackUnitIndex_Type()
)
bpPacketBufferStackUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bpPacketBufferStackUnitIndex.setStatus("current")


class _BpPacketBufferPortPipe_Type(Integer32):
    """Custom type bpPacketBufferPortPipe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_BpPacketBufferPortPipe_Type.__name__ = "Integer32"
_BpPacketBufferPortPipe_Object = MibTableColumn
bpPacketBufferPortPipe = _BpPacketBufferPortPipe_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 3, 1, 2),
    _BpPacketBufferPortPipe_Type()
)
bpPacketBufferPortPipe.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bpPacketBufferPortPipe.setStatus("current")
_BpPacketBufferTotalPacketBuffer_Type = Counter32
_BpPacketBufferTotalPacketBuffer_Object = MibTableColumn
bpPacketBufferTotalPacketBuffer = _BpPacketBufferTotalPacketBuffer_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 3, 1, 3),
    _BpPacketBufferTotalPacketBuffer_Type()
)
bpPacketBufferTotalPacketBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpPacketBufferTotalPacketBuffer.setStatus("current")
_BpPacketBufferCurrentAvailBuffer_Type = Counter32
_BpPacketBufferCurrentAvailBuffer_Object = MibTableColumn
bpPacketBufferCurrentAvailBuffer = _BpPacketBufferCurrentAvailBuffer_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 3, 1, 4),
    _BpPacketBufferCurrentAvailBuffer_Type()
)
bpPacketBufferCurrentAvailBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpPacketBufferCurrentAvailBuffer.setStatus("current")
_BpPacketBufferPacketBufferAlloc_Type = Counter32
_BpPacketBufferPacketBufferAlloc_Object = MibTableColumn
bpPacketBufferPacketBufferAlloc = _BpPacketBufferPacketBufferAlloc_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 3, 1, 5),
    _BpPacketBufferPacketBufferAlloc_Type()
)
bpPacketBufferPacketBufferAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpPacketBufferPacketBufferAlloc.setStatus("current")
_BpBufferStatsTable_Object = MibTable
bpBufferStatsTable = _BpBufferStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 4)
)
if mibBuilder.loadTexts:
    bpBufferStatsTable.setStatus("current")
_BpBufferStatsEntry_Object = MibTableRow
bpBufferStatsEntry = _BpBufferStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 4, 1)
)
bpBufferStatsEntry.setIndexNames(
    (0, "F10-BPSTATS-MIB", "bpBufferStatsStackUnitIndex"),
    (0, "F10-BPSTATS-MIB", "bpBufferStatsPortPipe"),
    (0, "F10-BPSTATS-MIB", "bpBufferStatsPortIndex"),
)
if mibBuilder.loadTexts:
    bpBufferStatsEntry.setStatus("current")


class _BpBufferStatsStackUnitIndex_Type(Integer32):
    """Custom type bpBufferStatsStackUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_BpBufferStatsStackUnitIndex_Type.__name__ = "Integer32"
_BpBufferStatsStackUnitIndex_Object = MibTableColumn
bpBufferStatsStackUnitIndex = _BpBufferStatsStackUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 4, 1, 1),
    _BpBufferStatsStackUnitIndex_Type()
)
bpBufferStatsStackUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bpBufferStatsStackUnitIndex.setStatus("current")


class _BpBufferStatsPortPipe_Type(Integer32):
    """Custom type bpBufferStatsPortPipe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_BpBufferStatsPortPipe_Type.__name__ = "Integer32"
_BpBufferStatsPortPipe_Object = MibTableColumn
bpBufferStatsPortPipe = _BpBufferStatsPortPipe_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 4, 1, 2),
    _BpBufferStatsPortPipe_Type()
)
bpBufferStatsPortPipe.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bpBufferStatsPortPipe.setStatus("current")


class _BpBufferStatsPortIndex_Type(Integer32):
    """Custom type bpBufferStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BpBufferStatsPortIndex_Type.__name__ = "Integer32"
_BpBufferStatsPortIndex_Object = MibTableColumn
bpBufferStatsPortIndex = _BpBufferStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 4, 1, 3),
    _BpBufferStatsPortIndex_Type()
)
bpBufferStatsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bpBufferStatsPortIndex.setStatus("current")
_BpBufferStatsCurrentUsagePerPort_Type = Counter32
_BpBufferStatsCurrentUsagePerPort_Object = MibTableColumn
bpBufferStatsCurrentUsagePerPort = _BpBufferStatsCurrentUsagePerPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 4, 1, 4),
    _BpBufferStatsCurrentUsagePerPort_Type()
)
bpBufferStatsCurrentUsagePerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpBufferStatsCurrentUsagePerPort.setStatus("current")
_BpBufferStatsDefaultPacketBuffAlloc_Type = Counter32
_BpBufferStatsDefaultPacketBuffAlloc_Object = MibTableColumn
bpBufferStatsDefaultPacketBuffAlloc = _BpBufferStatsDefaultPacketBuffAlloc_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 4, 1, 5),
    _BpBufferStatsDefaultPacketBuffAlloc_Type()
)
bpBufferStatsDefaultPacketBuffAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpBufferStatsDefaultPacketBuffAlloc.setStatus("current")
_BpBufferStatsMaxLimitPerPort_Type = Counter32
_BpBufferStatsMaxLimitPerPort_Object = MibTableColumn
bpBufferStatsMaxLimitPerPort = _BpBufferStatsMaxLimitPerPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 4, 1, 6),
    _BpBufferStatsMaxLimitPerPort_Type()
)
bpBufferStatsMaxLimitPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpBufferStatsMaxLimitPerPort.setStatus("current")
_BpCosStatsTable_Object = MibTable
bpCosStatsTable = _BpCosStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5)
)
if mibBuilder.loadTexts:
    bpCosStatsTable.setStatus("current")
_BpCosStatsEntry_Object = MibTableRow
bpCosStatsEntry = _BpCosStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1)
)
bpCosStatsEntry.setIndexNames(
    (0, "F10-BPSTATS-MIB", "bpCosStatsStackUnitIndex"),
    (0, "F10-BPSTATS-MIB", "bpCosStatsPortPipe"),
    (0, "F10-BPSTATS-MIB", "bpCosStatsPortIndex"),
    (0, "F10-BPSTATS-MIB", "bpCosStatsCOSNumber"),
)
if mibBuilder.loadTexts:
    bpCosStatsEntry.setStatus("current")


class _BpCosStatsStackUnitIndex_Type(Integer32):
    """Custom type bpCosStatsStackUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_BpCosStatsStackUnitIndex_Type.__name__ = "Integer32"
_BpCosStatsStackUnitIndex_Object = MibTableColumn
bpCosStatsStackUnitIndex = _BpCosStatsStackUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1, 1),
    _BpCosStatsStackUnitIndex_Type()
)
bpCosStatsStackUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bpCosStatsStackUnitIndex.setStatus("current")


class _BpCosStatsPortPipe_Type(Integer32):
    """Custom type bpCosStatsPortPipe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_BpCosStatsPortPipe_Type.__name__ = "Integer32"
_BpCosStatsPortPipe_Object = MibTableColumn
bpCosStatsPortPipe = _BpCosStatsPortPipe_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1, 2),
    _BpCosStatsPortPipe_Type()
)
bpCosStatsPortPipe.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bpCosStatsPortPipe.setStatus("current")


class _BpCosStatsPortIndex_Type(Integer32):
    """Custom type bpCosStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BpCosStatsPortIndex_Type.__name__ = "Integer32"
_BpCosStatsPortIndex_Object = MibTableColumn
bpCosStatsPortIndex = _BpCosStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1, 3),
    _BpCosStatsPortIndex_Type()
)
bpCosStatsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bpCosStatsPortIndex.setStatus("current")


class _BpCosStatsCOSNumber_Type(Integer32):
    """Custom type bpCosStatsCOSNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_BpCosStatsCOSNumber_Type.__name__ = "Integer32"
_BpCosStatsCOSNumber_Object = MibTableColumn
bpCosStatsCOSNumber = _BpCosStatsCOSNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1, 4),
    _BpCosStatsCOSNumber_Type()
)
bpCosStatsCOSNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bpCosStatsCOSNumber.setStatus("current")
_BpCosStatsCurrentUsage_Type = Counter32
_BpCosStatsCurrentUsage_Object = MibTableColumn
bpCosStatsCurrentUsage = _BpCosStatsCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1, 5),
    _BpCosStatsCurrentUsage_Type()
)
bpCosStatsCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpCosStatsCurrentUsage.setStatus("current")
_BpCosStatsDefaultPacketBuffAlloc_Type = Counter32
_BpCosStatsDefaultPacketBuffAlloc_Object = MibTableColumn
bpCosStatsDefaultPacketBuffAlloc = _BpCosStatsDefaultPacketBuffAlloc_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1, 6),
    _BpCosStatsDefaultPacketBuffAlloc_Type()
)
bpCosStatsDefaultPacketBuffAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpCosStatsDefaultPacketBuffAlloc.setStatus("current")
_BpCosStatsMaxLimit_Type = Counter32
_BpCosStatsMaxLimit_Object = MibTableColumn
bpCosStatsMaxLimit = _BpCosStatsMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1, 7),
    _BpCosStatsMaxLimit_Type()
)
bpCosStatsMaxLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpCosStatsMaxLimit.setStatus("current")
_BpCosStatsHOLDDrops_Type = Counter64
_BpCosStatsHOLDDrops_Object = MibTableColumn
bpCosStatsHOLDDrops = _BpCosStatsHOLDDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 2, 1, 5, 1, 8),
    _BpCosStatsHOLDDrops_Type()
)
bpCosStatsHOLDDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpCosStatsHOLDDrops.setStatus("current")
_F10BpStatsAlarms_ObjectIdentity = ObjectIdentity
f10BpStatsAlarms = _F10BpStatsAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 3)
)
_BpLinkBundleNotifications_ObjectIdentity = ObjectIdentity
bpLinkBundleNotifications = _BpLinkBundleNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 3, 1)
)
_BpLinkBundleAlarmVariable_ObjectIdentity = ObjectIdentity
bpLinkBundleAlarmVariable = _BpLinkBundleAlarmVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 3, 2)
)


class _BpLinkBundleType_Type(Integer32):
    """Custom type bpLinkBundleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bpHgBundle", 2),
          ("unknown", 1))
    )


_BpLinkBundleType_Type.__name__ = "Integer32"
_BpLinkBundleType_Object = MibScalar
bpLinkBundleType = _BpLinkBundleType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 3, 2, 1),
    _BpLinkBundleType_Type()
)
bpLinkBundleType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bpLinkBundleType.setStatus("current")
_BpLinkBundleSlot_Type = Integer32
_BpLinkBundleSlot_Object = MibScalar
bpLinkBundleSlot = _BpLinkBundleSlot_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 3, 2, 2),
    _BpLinkBundleSlot_Type()
)
bpLinkBundleSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bpLinkBundleSlot.setStatus("current")
_BpLinkBundleNpuUnit_Type = Integer32
_BpLinkBundleNpuUnit_Object = MibScalar
bpLinkBundleNpuUnit = _BpLinkBundleNpuUnit_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 3, 2, 3),
    _BpLinkBundleNpuUnit_Type()
)
bpLinkBundleNpuUnit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bpLinkBundleNpuUnit.setStatus("current")
_BpLinkBundleLocalId_Type = Integer32
_BpLinkBundleLocalId_Object = MibScalar
bpLinkBundleLocalId = _BpLinkBundleLocalId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 3, 2, 4),
    _BpLinkBundleLocalId_Type()
)
bpLinkBundleLocalId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bpLinkBundleLocalId.setStatus("current")

# Managed Objects groups


# Notification objects

bpLinkBundleImbalance = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 3, 1, 1)
)
bpLinkBundleImbalance.setObjects(
      *(("F10-BPSTATS-MIB", "bpLinkBundleType"),
        ("F10-BPSTATS-MIB", "bpLinkBundleSlot"),
        ("F10-BPSTATS-MIB", "bpLinkBundleNpuUnit"),
        ("F10-BPSTATS-MIB", "bpLinkBundleLocalId"))
)
if mibBuilder.loadTexts:
    bpLinkBundleImbalance.setStatus(
        "current"
    )

bpLinkBundleImbalanceClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 24, 3, 1, 2)
)
bpLinkBundleImbalanceClear.setObjects(
      *(("F10-BPSTATS-MIB", "bpLinkBundleType"),
        ("F10-BPSTATS-MIB", "bpLinkBundleSlot"),
        ("F10-BPSTATS-MIB", "bpLinkBundleNpuUnit"),
        ("F10-BPSTATS-MIB", "bpLinkBundleLocalId"))
)
if mibBuilder.loadTexts:
    bpLinkBundleImbalanceClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10-BPSTATS-MIB",
    **{"f10BpStatsMib": f10BpStatsMib,
       "f10BpStatsLinkBundleObjects": f10BpStatsLinkBundleObjects,
       "bpLinkBundleObjects": bpLinkBundleObjects,
       "bpLinkBundleRateInterval": bpLinkBundleRateInterval,
       "bpLinkBundleTriggerThreshold": bpLinkBundleTriggerThreshold,
       "f10BpStatsObjects": f10BpStatsObjects,
       "bpStatsObjects": bpStatsObjects,
       "bpDropsTable": bpDropsTable,
       "bpDropsEntry": bpDropsEntry,
       "bpDropsStackUnitIndex": bpDropsStackUnitIndex,
       "bpDropsPortPipe": bpDropsPortPipe,
       "bpDropsPortIndex": bpDropsPortIndex,
       "bpDropsInDrops": bpDropsInDrops,
       "bpDropsInUnKnownHgHdr": bpDropsInUnKnownHgHdr,
       "bpDropsInUnKnownHgOpcode": bpDropsInUnKnownHgOpcode,
       "bpDropsInMTUExceeds": bpDropsInMTUExceeds,
       "bpDropsInMacDrops": bpDropsInMacDrops,
       "bpDropsMMUHOLDrops": bpDropsMMUHOLDrops,
       "bpDropsEgMacDrops": bpDropsEgMacDrops,
       "bpDropsEgTxAgedCounter": bpDropsEgTxAgedCounter,
       "bpDropsEgTxErrCounter": bpDropsEgTxErrCounter,
       "bpDropsEgTxMACUnderflow": bpDropsEgTxMACUnderflow,
       "bpDropsEgTxErrPktCounter": bpDropsEgTxErrPktCounter,
       "bpIfStatsTable": bpIfStatsTable,
       "bpIfStatsEntry": bpIfStatsEntry,
       "bpIfStatsStackUnitIndex": bpIfStatsStackUnitIndex,
       "bpIfStatsPortPipe": bpIfStatsPortPipe,
       "bpIfStatsPortIndex": bpIfStatsPortIndex,
       "bpIfStatsIn64BytePkts": bpIfStatsIn64BytePkts,
       "bpIfStatsIn65To127BytePkts": bpIfStatsIn65To127BytePkts,
       "bpIfStatsIn128To255BytePkts": bpIfStatsIn128To255BytePkts,
       "bpIfStatsIn256To511BytePkts": bpIfStatsIn256To511BytePkts,
       "bpIfStatsIn512To1023BytePkts": bpIfStatsIn512To1023BytePkts,
       "bpIfStatsInOver1023BytePkts": bpIfStatsInOver1023BytePkts,
       "bpIfStatsInThrottles": bpIfStatsInThrottles,
       "bpIfStatsInRunts": bpIfStatsInRunts,
       "bpIfStatsInGiants": bpIfStatsInGiants,
       "bpIfStatsInCRC": bpIfStatsInCRC,
       "bpIfStatsInOverruns": bpIfStatsInOverruns,
       "bpIfStatsOutUnderruns": bpIfStatsOutUnderruns,
       "bpIfStatsOutUnicasts": bpIfStatsOutUnicasts,
       "bpIfStatsOutCollisions": bpIfStatsOutCollisions,
       "bpIfStatsOutWredDrops": bpIfStatsOutWredDrops,
       "bpIfStatsOut64BytePkts": bpIfStatsOut64BytePkts,
       "bpIfStatsOut65To127BytePkts": bpIfStatsOut65To127BytePkts,
       "bpIfStatsOut128To255BytePkts": bpIfStatsOut128To255BytePkts,
       "bpIfStatsOut256To511BytePkts": bpIfStatsOut256To511BytePkts,
       "bpIfStatsOut512To1023BytePkts": bpIfStatsOut512To1023BytePkts,
       "bpIfStatsOutOver1023BytePkts": bpIfStatsOutOver1023BytePkts,
       "bpIfStatsOutThrottles": bpIfStatsOutThrottles,
       "bpIfStatsLastDiscontinuityTime": bpIfStatsLastDiscontinuityTime,
       "bpIfStatsInCentRate": bpIfStatsInCentRate,
       "bpIfStatsOutCentRate": bpIfStatsOutCentRate,
       "bpIfStatsLastChange": bpIfStatsLastChange,
       "bpPacketBufferTable": bpPacketBufferTable,
       "bpPacketBufferEntry": bpPacketBufferEntry,
       "bpPacketBufferStackUnitIndex": bpPacketBufferStackUnitIndex,
       "bpPacketBufferPortPipe": bpPacketBufferPortPipe,
       "bpPacketBufferTotalPacketBuffer": bpPacketBufferTotalPacketBuffer,
       "bpPacketBufferCurrentAvailBuffer": bpPacketBufferCurrentAvailBuffer,
       "bpPacketBufferPacketBufferAlloc": bpPacketBufferPacketBufferAlloc,
       "bpBufferStatsTable": bpBufferStatsTable,
       "bpBufferStatsEntry": bpBufferStatsEntry,
       "bpBufferStatsStackUnitIndex": bpBufferStatsStackUnitIndex,
       "bpBufferStatsPortPipe": bpBufferStatsPortPipe,
       "bpBufferStatsPortIndex": bpBufferStatsPortIndex,
       "bpBufferStatsCurrentUsagePerPort": bpBufferStatsCurrentUsagePerPort,
       "bpBufferStatsDefaultPacketBuffAlloc": bpBufferStatsDefaultPacketBuffAlloc,
       "bpBufferStatsMaxLimitPerPort": bpBufferStatsMaxLimitPerPort,
       "bpCosStatsTable": bpCosStatsTable,
       "bpCosStatsEntry": bpCosStatsEntry,
       "bpCosStatsStackUnitIndex": bpCosStatsStackUnitIndex,
       "bpCosStatsPortPipe": bpCosStatsPortPipe,
       "bpCosStatsPortIndex": bpCosStatsPortIndex,
       "bpCosStatsCOSNumber": bpCosStatsCOSNumber,
       "bpCosStatsCurrentUsage": bpCosStatsCurrentUsage,
       "bpCosStatsDefaultPacketBuffAlloc": bpCosStatsDefaultPacketBuffAlloc,
       "bpCosStatsMaxLimit": bpCosStatsMaxLimit,
       "bpCosStatsHOLDDrops": bpCosStatsHOLDDrops,
       "f10BpStatsAlarms": f10BpStatsAlarms,
       "bpLinkBundleNotifications": bpLinkBundleNotifications,
       "bpLinkBundleImbalance": bpLinkBundleImbalance,
       "bpLinkBundleImbalanceClear": bpLinkBundleImbalanceClear,
       "bpLinkBundleAlarmVariable": bpLinkBundleAlarmVariable,
       "bpLinkBundleType": bpLinkBundleType,
       "bpLinkBundleSlot": bpLinkBundleSlot,
       "bpLinkBundleNpuUnit": bpLinkBundleNpuUnit,
       "bpLinkBundleLocalId": bpLinkBundleLocalId}
)
