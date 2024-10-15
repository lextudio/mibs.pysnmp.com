# SNMP MIB module (TOKEN-RING-RMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TOKEN-RING-RMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:52 2024
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

(EntryStatus,
 OwnerString,
 history,
 rmon,
 statistics) = mibBuilder.importSymbols(
    "RMON-MIB",
    "EntryStatus",
    "OwnerString",
    "history",
    "rmon",
    "statistics")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class TimeInterval(Integer32):
    """Custom type TimeInterval based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TokenRingMLStatsTable_Object = MibTable
tokenRingMLStatsTable = _TokenRingMLStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2)
)
if mibBuilder.loadTexts:
    tokenRingMLStatsTable.setStatus("mandatory")
_TokenRingMLStatsEntry_Object = MibTableRow
tokenRingMLStatsEntry = _TokenRingMLStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1)
)
tokenRingMLStatsEntry.setIndexNames(
    (0, "TOKEN-RING-RMON-MIB", "tokenRingMLStatsIndex"),
)
if mibBuilder.loadTexts:
    tokenRingMLStatsEntry.setStatus("mandatory")


class _TokenRingMLStatsIndex_Type(Integer32):
    """Custom type tokenRingMLStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TokenRingMLStatsIndex_Type.__name__ = "Integer32"
_TokenRingMLStatsIndex_Object = MibTableColumn
tokenRingMLStatsIndex = _TokenRingMLStatsIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 1),
    _TokenRingMLStatsIndex_Type()
)
tokenRingMLStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsIndex.setStatus("mandatory")
_TokenRingMLStatsDataSource_Type = ObjectIdentifier
_TokenRingMLStatsDataSource_Object = MibTableColumn
tokenRingMLStatsDataSource = _TokenRingMLStatsDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 2),
    _TokenRingMLStatsDataSource_Type()
)
tokenRingMLStatsDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingMLStatsDataSource.setStatus("mandatory")
_TokenRingMLStatsDropEvents_Type = Counter32
_TokenRingMLStatsDropEvents_Object = MibTableColumn
tokenRingMLStatsDropEvents = _TokenRingMLStatsDropEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 3),
    _TokenRingMLStatsDropEvents_Type()
)
tokenRingMLStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsDropEvents.setStatus("mandatory")
_TokenRingMLStatsMacOctets_Type = Counter32
_TokenRingMLStatsMacOctets_Object = MibTableColumn
tokenRingMLStatsMacOctets = _TokenRingMLStatsMacOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 4),
    _TokenRingMLStatsMacOctets_Type()
)
tokenRingMLStatsMacOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsMacOctets.setStatus("mandatory")
_TokenRingMLStatsMacPkts_Type = Counter32
_TokenRingMLStatsMacPkts_Object = MibTableColumn
tokenRingMLStatsMacPkts = _TokenRingMLStatsMacPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 5),
    _TokenRingMLStatsMacPkts_Type()
)
tokenRingMLStatsMacPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsMacPkts.setStatus("mandatory")
_TokenRingMLStatsRingPurgeEvents_Type = Counter32
_TokenRingMLStatsRingPurgeEvents_Object = MibTableColumn
tokenRingMLStatsRingPurgeEvents = _TokenRingMLStatsRingPurgeEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 6),
    _TokenRingMLStatsRingPurgeEvents_Type()
)
tokenRingMLStatsRingPurgeEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsRingPurgeEvents.setStatus("mandatory")
_TokenRingMLStatsRingPurgePkts_Type = Counter32
_TokenRingMLStatsRingPurgePkts_Object = MibTableColumn
tokenRingMLStatsRingPurgePkts = _TokenRingMLStatsRingPurgePkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 7),
    _TokenRingMLStatsRingPurgePkts_Type()
)
tokenRingMLStatsRingPurgePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsRingPurgePkts.setStatus("mandatory")
_TokenRingMLStatsBeaconEvents_Type = Counter32
_TokenRingMLStatsBeaconEvents_Object = MibTableColumn
tokenRingMLStatsBeaconEvents = _TokenRingMLStatsBeaconEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 8),
    _TokenRingMLStatsBeaconEvents_Type()
)
tokenRingMLStatsBeaconEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsBeaconEvents.setStatus("mandatory")
_TokenRingMLStatsBeaconTime_Type = TimeInterval
_TokenRingMLStatsBeaconTime_Object = MibTableColumn
tokenRingMLStatsBeaconTime = _TokenRingMLStatsBeaconTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 9),
    _TokenRingMLStatsBeaconTime_Type()
)
tokenRingMLStatsBeaconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsBeaconTime.setStatus("mandatory")
_TokenRingMLStatsBeaconPkts_Type = Counter32
_TokenRingMLStatsBeaconPkts_Object = MibTableColumn
tokenRingMLStatsBeaconPkts = _TokenRingMLStatsBeaconPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 10),
    _TokenRingMLStatsBeaconPkts_Type()
)
tokenRingMLStatsBeaconPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsBeaconPkts.setStatus("mandatory")
_TokenRingMLStatsClaimTokenEvents_Type = Counter32
_TokenRingMLStatsClaimTokenEvents_Object = MibTableColumn
tokenRingMLStatsClaimTokenEvents = _TokenRingMLStatsClaimTokenEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 11),
    _TokenRingMLStatsClaimTokenEvents_Type()
)
tokenRingMLStatsClaimTokenEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsClaimTokenEvents.setStatus("mandatory")
_TokenRingMLStatsClaimTokenPkts_Type = Counter32
_TokenRingMLStatsClaimTokenPkts_Object = MibTableColumn
tokenRingMLStatsClaimTokenPkts = _TokenRingMLStatsClaimTokenPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 12),
    _TokenRingMLStatsClaimTokenPkts_Type()
)
tokenRingMLStatsClaimTokenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsClaimTokenPkts.setStatus("mandatory")
_TokenRingMLStatsNAUNChanges_Type = Counter32
_TokenRingMLStatsNAUNChanges_Object = MibTableColumn
tokenRingMLStatsNAUNChanges = _TokenRingMLStatsNAUNChanges_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 13),
    _TokenRingMLStatsNAUNChanges_Type()
)
tokenRingMLStatsNAUNChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsNAUNChanges.setStatus("mandatory")
_TokenRingMLStatsLineErrors_Type = Counter32
_TokenRingMLStatsLineErrors_Object = MibTableColumn
tokenRingMLStatsLineErrors = _TokenRingMLStatsLineErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 14),
    _TokenRingMLStatsLineErrors_Type()
)
tokenRingMLStatsLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsLineErrors.setStatus("mandatory")
_TokenRingMLStatsInternalErrors_Type = Counter32
_TokenRingMLStatsInternalErrors_Object = MibTableColumn
tokenRingMLStatsInternalErrors = _TokenRingMLStatsInternalErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 15),
    _TokenRingMLStatsInternalErrors_Type()
)
tokenRingMLStatsInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsInternalErrors.setStatus("mandatory")
_TokenRingMLStatsBurstErrors_Type = Counter32
_TokenRingMLStatsBurstErrors_Object = MibTableColumn
tokenRingMLStatsBurstErrors = _TokenRingMLStatsBurstErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 16),
    _TokenRingMLStatsBurstErrors_Type()
)
tokenRingMLStatsBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsBurstErrors.setStatus("mandatory")
_TokenRingMLStatsACErrors_Type = Counter32
_TokenRingMLStatsACErrors_Object = MibTableColumn
tokenRingMLStatsACErrors = _TokenRingMLStatsACErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 17),
    _TokenRingMLStatsACErrors_Type()
)
tokenRingMLStatsACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsACErrors.setStatus("mandatory")
_TokenRingMLStatsAbortErrors_Type = Counter32
_TokenRingMLStatsAbortErrors_Object = MibTableColumn
tokenRingMLStatsAbortErrors = _TokenRingMLStatsAbortErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 18),
    _TokenRingMLStatsAbortErrors_Type()
)
tokenRingMLStatsAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsAbortErrors.setStatus("mandatory")
_TokenRingMLStatsLostFrameErrors_Type = Counter32
_TokenRingMLStatsLostFrameErrors_Object = MibTableColumn
tokenRingMLStatsLostFrameErrors = _TokenRingMLStatsLostFrameErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 19),
    _TokenRingMLStatsLostFrameErrors_Type()
)
tokenRingMLStatsLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsLostFrameErrors.setStatus("mandatory")
_TokenRingMLStatsCongestionErrors_Type = Counter32
_TokenRingMLStatsCongestionErrors_Object = MibTableColumn
tokenRingMLStatsCongestionErrors = _TokenRingMLStatsCongestionErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 20),
    _TokenRingMLStatsCongestionErrors_Type()
)
tokenRingMLStatsCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsCongestionErrors.setStatus("mandatory")
_TokenRingMLStatsFrameCopiedErrors_Type = Counter32
_TokenRingMLStatsFrameCopiedErrors_Object = MibTableColumn
tokenRingMLStatsFrameCopiedErrors = _TokenRingMLStatsFrameCopiedErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 21),
    _TokenRingMLStatsFrameCopiedErrors_Type()
)
tokenRingMLStatsFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsFrameCopiedErrors.setStatus("mandatory")
_TokenRingMLStatsFrequencyErrors_Type = Counter32
_TokenRingMLStatsFrequencyErrors_Object = MibTableColumn
tokenRingMLStatsFrequencyErrors = _TokenRingMLStatsFrequencyErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 22),
    _TokenRingMLStatsFrequencyErrors_Type()
)
tokenRingMLStatsFrequencyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsFrequencyErrors.setStatus("mandatory")
_TokenRingMLStatsTokenErrors_Type = Counter32
_TokenRingMLStatsTokenErrors_Object = MibTableColumn
tokenRingMLStatsTokenErrors = _TokenRingMLStatsTokenErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 23),
    _TokenRingMLStatsTokenErrors_Type()
)
tokenRingMLStatsTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsTokenErrors.setStatus("mandatory")
_TokenRingMLStatsSoftErrorReports_Type = Counter32
_TokenRingMLStatsSoftErrorReports_Object = MibTableColumn
tokenRingMLStatsSoftErrorReports = _TokenRingMLStatsSoftErrorReports_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 24),
    _TokenRingMLStatsSoftErrorReports_Type()
)
tokenRingMLStatsSoftErrorReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsSoftErrorReports.setStatus("mandatory")
_TokenRingMLStatsRingPollEvents_Type = Counter32
_TokenRingMLStatsRingPollEvents_Object = MibTableColumn
tokenRingMLStatsRingPollEvents = _TokenRingMLStatsRingPollEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 25),
    _TokenRingMLStatsRingPollEvents_Type()
)
tokenRingMLStatsRingPollEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLStatsRingPollEvents.setStatus("mandatory")
_TokenRingMLStatsOwner_Type = OwnerString
_TokenRingMLStatsOwner_Object = MibTableColumn
tokenRingMLStatsOwner = _TokenRingMLStatsOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 26),
    _TokenRingMLStatsOwner_Type()
)
tokenRingMLStatsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingMLStatsOwner.setStatus("mandatory")
_TokenRingMLStatsStatus_Type = EntryStatus
_TokenRingMLStatsStatus_Object = MibTableColumn
tokenRingMLStatsStatus = _TokenRingMLStatsStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 2, 1, 27),
    _TokenRingMLStatsStatus_Type()
)
tokenRingMLStatsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingMLStatsStatus.setStatus("mandatory")
_TokenRingPStatsTable_Object = MibTable
tokenRingPStatsTable = _TokenRingPStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3)
)
if mibBuilder.loadTexts:
    tokenRingPStatsTable.setStatus("mandatory")
_TokenRingPStatsEntry_Object = MibTableRow
tokenRingPStatsEntry = _TokenRingPStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1)
)
tokenRingPStatsEntry.setIndexNames(
    (0, "TOKEN-RING-RMON-MIB", "tokenRingPStatsIndex"),
)
if mibBuilder.loadTexts:
    tokenRingPStatsEntry.setStatus("mandatory")


class _TokenRingPStatsIndex_Type(Integer32):
    """Custom type tokenRingPStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TokenRingPStatsIndex_Type.__name__ = "Integer32"
_TokenRingPStatsIndex_Object = MibTableColumn
tokenRingPStatsIndex = _TokenRingPStatsIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 1),
    _TokenRingPStatsIndex_Type()
)
tokenRingPStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsIndex.setStatus("mandatory")
_TokenRingPStatsDataSource_Type = ObjectIdentifier
_TokenRingPStatsDataSource_Object = MibTableColumn
tokenRingPStatsDataSource = _TokenRingPStatsDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 2),
    _TokenRingPStatsDataSource_Type()
)
tokenRingPStatsDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingPStatsDataSource.setStatus("mandatory")
_TokenRingPStatsDropEvents_Type = Counter32
_TokenRingPStatsDropEvents_Object = MibTableColumn
tokenRingPStatsDropEvents = _TokenRingPStatsDropEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 3),
    _TokenRingPStatsDropEvents_Type()
)
tokenRingPStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsDropEvents.setStatus("mandatory")
_TokenRingPStatsDataOctets_Type = Counter32
_TokenRingPStatsDataOctets_Object = MibTableColumn
tokenRingPStatsDataOctets = _TokenRingPStatsDataOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 4),
    _TokenRingPStatsDataOctets_Type()
)
tokenRingPStatsDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsDataOctets.setStatus("mandatory")
_TokenRingPStatsDataPkts_Type = Counter32
_TokenRingPStatsDataPkts_Object = MibTableColumn
tokenRingPStatsDataPkts = _TokenRingPStatsDataPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 5),
    _TokenRingPStatsDataPkts_Type()
)
tokenRingPStatsDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsDataPkts.setStatus("mandatory")
_TokenRingPStatsDataBroadcastPkts_Type = Counter32
_TokenRingPStatsDataBroadcastPkts_Object = MibTableColumn
tokenRingPStatsDataBroadcastPkts = _TokenRingPStatsDataBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 6),
    _TokenRingPStatsDataBroadcastPkts_Type()
)
tokenRingPStatsDataBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsDataBroadcastPkts.setStatus("mandatory")
_TokenRingPStatsDataMulticastPkts_Type = Counter32
_TokenRingPStatsDataMulticastPkts_Object = MibTableColumn
tokenRingPStatsDataMulticastPkts = _TokenRingPStatsDataMulticastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 7),
    _TokenRingPStatsDataMulticastPkts_Type()
)
tokenRingPStatsDataMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsDataMulticastPkts.setStatus("mandatory")
_TokenRingPStatsDataPkts18to63Octets_Type = Counter32
_TokenRingPStatsDataPkts18to63Octets_Object = MibTableColumn
tokenRingPStatsDataPkts18to63Octets = _TokenRingPStatsDataPkts18to63Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 8),
    _TokenRingPStatsDataPkts18to63Octets_Type()
)
tokenRingPStatsDataPkts18to63Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsDataPkts18to63Octets.setStatus("mandatory")
_TokenRingPStatsDataPkts64to127Octets_Type = Counter32
_TokenRingPStatsDataPkts64to127Octets_Object = MibTableColumn
tokenRingPStatsDataPkts64to127Octets = _TokenRingPStatsDataPkts64to127Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 9),
    _TokenRingPStatsDataPkts64to127Octets_Type()
)
tokenRingPStatsDataPkts64to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsDataPkts64to127Octets.setStatus("mandatory")
_TokenRingPStatsDataPkts128to255Octets_Type = Counter32
_TokenRingPStatsDataPkts128to255Octets_Object = MibTableColumn
tokenRingPStatsDataPkts128to255Octets = _TokenRingPStatsDataPkts128to255Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 10),
    _TokenRingPStatsDataPkts128to255Octets_Type()
)
tokenRingPStatsDataPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsDataPkts128to255Octets.setStatus("mandatory")
_TokenRingPStatsDataPkts256to511Octets_Type = Counter32
_TokenRingPStatsDataPkts256to511Octets_Object = MibTableColumn
tokenRingPStatsDataPkts256to511Octets = _TokenRingPStatsDataPkts256to511Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 11),
    _TokenRingPStatsDataPkts256to511Octets_Type()
)
tokenRingPStatsDataPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsDataPkts256to511Octets.setStatus("mandatory")
_TokenRingPStatsDataPkts512to1023Octets_Type = Counter32
_TokenRingPStatsDataPkts512to1023Octets_Object = MibTableColumn
tokenRingPStatsDataPkts512to1023Octets = _TokenRingPStatsDataPkts512to1023Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 12),
    _TokenRingPStatsDataPkts512to1023Octets_Type()
)
tokenRingPStatsDataPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsDataPkts512to1023Octets.setStatus("mandatory")
_TokenRingPStatsDataPkts1024to2047Octets_Type = Counter32
_TokenRingPStatsDataPkts1024to2047Octets_Object = MibTableColumn
tokenRingPStatsDataPkts1024to2047Octets = _TokenRingPStatsDataPkts1024to2047Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 13),
    _TokenRingPStatsDataPkts1024to2047Octets_Type()
)
tokenRingPStatsDataPkts1024to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsDataPkts1024to2047Octets.setStatus("mandatory")
_TokenRingPStatsDataPkts2048to4095Octets_Type = Counter32
_TokenRingPStatsDataPkts2048to4095Octets_Object = MibTableColumn
tokenRingPStatsDataPkts2048to4095Octets = _TokenRingPStatsDataPkts2048to4095Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 14),
    _TokenRingPStatsDataPkts2048to4095Octets_Type()
)
tokenRingPStatsDataPkts2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsDataPkts2048to4095Octets.setStatus("mandatory")
_TokenRingPStatsDataPkts4096to8191Octets_Type = Counter32
_TokenRingPStatsDataPkts4096to8191Octets_Object = MibTableColumn
tokenRingPStatsDataPkts4096to8191Octets = _TokenRingPStatsDataPkts4096to8191Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 15),
    _TokenRingPStatsDataPkts4096to8191Octets_Type()
)
tokenRingPStatsDataPkts4096to8191Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsDataPkts4096to8191Octets.setStatus("mandatory")
_TokenRingPStatsDataPkts8192to18000Octets_Type = Counter32
_TokenRingPStatsDataPkts8192to18000Octets_Object = MibTableColumn
tokenRingPStatsDataPkts8192to18000Octets = _TokenRingPStatsDataPkts8192to18000Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 16),
    _TokenRingPStatsDataPkts8192to18000Octets_Type()
)
tokenRingPStatsDataPkts8192to18000Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsDataPkts8192to18000Octets.setStatus("mandatory")
_TokenRingPStatsDataPktsGreaterThan18000Octets_Type = Counter32
_TokenRingPStatsDataPktsGreaterThan18000Octets_Object = MibTableColumn
tokenRingPStatsDataPktsGreaterThan18000Octets = _TokenRingPStatsDataPktsGreaterThan18000Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 17),
    _TokenRingPStatsDataPktsGreaterThan18000Octets_Type()
)
tokenRingPStatsDataPktsGreaterThan18000Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPStatsDataPktsGreaterThan18000Octets.setStatus("mandatory")
_TokenRingPStatsOwner_Type = OwnerString
_TokenRingPStatsOwner_Object = MibTableColumn
tokenRingPStatsOwner = _TokenRingPStatsOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 18),
    _TokenRingPStatsOwner_Type()
)
tokenRingPStatsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingPStatsOwner.setStatus("mandatory")
_TokenRingPStatsStatus_Type = EntryStatus
_TokenRingPStatsStatus_Object = MibTableColumn
tokenRingPStatsStatus = _TokenRingPStatsStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 1, 3, 1, 19),
    _TokenRingPStatsStatus_Type()
)
tokenRingPStatsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingPStatsStatus.setStatus("mandatory")
_TokenRingMLHistoryTable_Object = MibTable
tokenRingMLHistoryTable = _TokenRingMLHistoryTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3)
)
if mibBuilder.loadTexts:
    tokenRingMLHistoryTable.setStatus("mandatory")
_TokenRingMLHistoryEntry_Object = MibTableRow
tokenRingMLHistoryEntry = _TokenRingMLHistoryEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1)
)
tokenRingMLHistoryEntry.setIndexNames(
    (0, "TOKEN-RING-RMON-MIB", "tokenRingMLHistoryIndex"),
    (0, "TOKEN-RING-RMON-MIB", "tokenRingMLHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    tokenRingMLHistoryEntry.setStatus("mandatory")


class _TokenRingMLHistoryIndex_Type(Integer32):
    """Custom type tokenRingMLHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TokenRingMLHistoryIndex_Type.__name__ = "Integer32"
_TokenRingMLHistoryIndex_Object = MibTableColumn
tokenRingMLHistoryIndex = _TokenRingMLHistoryIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 1),
    _TokenRingMLHistoryIndex_Type()
)
tokenRingMLHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryIndex.setStatus("mandatory")
_TokenRingMLHistorySampleIndex_Type = Integer32
_TokenRingMLHistorySampleIndex_Object = MibTableColumn
tokenRingMLHistorySampleIndex = _TokenRingMLHistorySampleIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 2),
    _TokenRingMLHistorySampleIndex_Type()
)
tokenRingMLHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistorySampleIndex.setStatus("mandatory")
_TokenRingMLHistoryIntervalStart_Type = TimeTicks
_TokenRingMLHistoryIntervalStart_Object = MibTableColumn
tokenRingMLHistoryIntervalStart = _TokenRingMLHistoryIntervalStart_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 3),
    _TokenRingMLHistoryIntervalStart_Type()
)
tokenRingMLHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryIntervalStart.setStatus("mandatory")
_TokenRingMLHistoryDropEvents_Type = Counter32
_TokenRingMLHistoryDropEvents_Object = MibTableColumn
tokenRingMLHistoryDropEvents = _TokenRingMLHistoryDropEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 4),
    _TokenRingMLHistoryDropEvents_Type()
)
tokenRingMLHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryDropEvents.setStatus("mandatory")
_TokenRingMLHistoryMacOctets_Type = Counter32
_TokenRingMLHistoryMacOctets_Object = MibTableColumn
tokenRingMLHistoryMacOctets = _TokenRingMLHistoryMacOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 5),
    _TokenRingMLHistoryMacOctets_Type()
)
tokenRingMLHistoryMacOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryMacOctets.setStatus("mandatory")
_TokenRingMLHistoryMacPkts_Type = Counter32
_TokenRingMLHistoryMacPkts_Object = MibTableColumn
tokenRingMLHistoryMacPkts = _TokenRingMLHistoryMacPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 6),
    _TokenRingMLHistoryMacPkts_Type()
)
tokenRingMLHistoryMacPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryMacPkts.setStatus("mandatory")
_TokenRingMLHistoryRingPurgeEvents_Type = Counter32
_TokenRingMLHistoryRingPurgeEvents_Object = MibTableColumn
tokenRingMLHistoryRingPurgeEvents = _TokenRingMLHistoryRingPurgeEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 7),
    _TokenRingMLHistoryRingPurgeEvents_Type()
)
tokenRingMLHistoryRingPurgeEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryRingPurgeEvents.setStatus("mandatory")
_TokenRingMLHistoryRingPurgePkts_Type = Counter32
_TokenRingMLHistoryRingPurgePkts_Object = MibTableColumn
tokenRingMLHistoryRingPurgePkts = _TokenRingMLHistoryRingPurgePkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 8),
    _TokenRingMLHistoryRingPurgePkts_Type()
)
tokenRingMLHistoryRingPurgePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryRingPurgePkts.setStatus("mandatory")
_TokenRingMLHistoryBeaconEvents_Type = Counter32
_TokenRingMLHistoryBeaconEvents_Object = MibTableColumn
tokenRingMLHistoryBeaconEvents = _TokenRingMLHistoryBeaconEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 9),
    _TokenRingMLHistoryBeaconEvents_Type()
)
tokenRingMLHistoryBeaconEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryBeaconEvents.setStatus("mandatory")
_TokenRingMLHistoryBeaconTime_Type = TimeInterval
_TokenRingMLHistoryBeaconTime_Object = MibTableColumn
tokenRingMLHistoryBeaconTime = _TokenRingMLHistoryBeaconTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 10),
    _TokenRingMLHistoryBeaconTime_Type()
)
tokenRingMLHistoryBeaconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryBeaconTime.setStatus("mandatory")
_TokenRingMLHistoryBeaconPkts_Type = Counter32
_TokenRingMLHistoryBeaconPkts_Object = MibTableColumn
tokenRingMLHistoryBeaconPkts = _TokenRingMLHistoryBeaconPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 11),
    _TokenRingMLHistoryBeaconPkts_Type()
)
tokenRingMLHistoryBeaconPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryBeaconPkts.setStatus("mandatory")
_TokenRingMLHistoryClaimTokenEvents_Type = Counter32
_TokenRingMLHistoryClaimTokenEvents_Object = MibTableColumn
tokenRingMLHistoryClaimTokenEvents = _TokenRingMLHistoryClaimTokenEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 12),
    _TokenRingMLHistoryClaimTokenEvents_Type()
)
tokenRingMLHistoryClaimTokenEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryClaimTokenEvents.setStatus("mandatory")
_TokenRingMLHistoryClaimTokenPkts_Type = Counter32
_TokenRingMLHistoryClaimTokenPkts_Object = MibTableColumn
tokenRingMLHistoryClaimTokenPkts = _TokenRingMLHistoryClaimTokenPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 13),
    _TokenRingMLHistoryClaimTokenPkts_Type()
)
tokenRingMLHistoryClaimTokenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryClaimTokenPkts.setStatus("mandatory")
_TokenRingMLHistoryNAUNChanges_Type = Counter32
_TokenRingMLHistoryNAUNChanges_Object = MibTableColumn
tokenRingMLHistoryNAUNChanges = _TokenRingMLHistoryNAUNChanges_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 14),
    _TokenRingMLHistoryNAUNChanges_Type()
)
tokenRingMLHistoryNAUNChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryNAUNChanges.setStatus("mandatory")
_TokenRingMLHistoryLineErrors_Type = Counter32
_TokenRingMLHistoryLineErrors_Object = MibTableColumn
tokenRingMLHistoryLineErrors = _TokenRingMLHistoryLineErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 15),
    _TokenRingMLHistoryLineErrors_Type()
)
tokenRingMLHistoryLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryLineErrors.setStatus("mandatory")
_TokenRingMLHistoryInternalErrors_Type = Counter32
_TokenRingMLHistoryInternalErrors_Object = MibTableColumn
tokenRingMLHistoryInternalErrors = _TokenRingMLHistoryInternalErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 16),
    _TokenRingMLHistoryInternalErrors_Type()
)
tokenRingMLHistoryInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryInternalErrors.setStatus("mandatory")
_TokenRingMLHistoryBurstErrors_Type = Counter32
_TokenRingMLHistoryBurstErrors_Object = MibTableColumn
tokenRingMLHistoryBurstErrors = _TokenRingMLHistoryBurstErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 17),
    _TokenRingMLHistoryBurstErrors_Type()
)
tokenRingMLHistoryBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryBurstErrors.setStatus("mandatory")
_TokenRingMLHistoryACErrors_Type = Counter32
_TokenRingMLHistoryACErrors_Object = MibTableColumn
tokenRingMLHistoryACErrors = _TokenRingMLHistoryACErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 18),
    _TokenRingMLHistoryACErrors_Type()
)
tokenRingMLHistoryACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryACErrors.setStatus("mandatory")
_TokenRingMLHistoryAbortErrors_Type = Counter32
_TokenRingMLHistoryAbortErrors_Object = MibTableColumn
tokenRingMLHistoryAbortErrors = _TokenRingMLHistoryAbortErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 19),
    _TokenRingMLHistoryAbortErrors_Type()
)
tokenRingMLHistoryAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryAbortErrors.setStatus("mandatory")
_TokenRingMLHistoryLostFrameErrors_Type = Counter32
_TokenRingMLHistoryLostFrameErrors_Object = MibTableColumn
tokenRingMLHistoryLostFrameErrors = _TokenRingMLHistoryLostFrameErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 20),
    _TokenRingMLHistoryLostFrameErrors_Type()
)
tokenRingMLHistoryLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryLostFrameErrors.setStatus("mandatory")
_TokenRingMLHistoryCongestionErrors_Type = Counter32
_TokenRingMLHistoryCongestionErrors_Object = MibTableColumn
tokenRingMLHistoryCongestionErrors = _TokenRingMLHistoryCongestionErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 21),
    _TokenRingMLHistoryCongestionErrors_Type()
)
tokenRingMLHistoryCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryCongestionErrors.setStatus("mandatory")
_TokenRingMLHistoryFrameCopiedErrors_Type = Counter32
_TokenRingMLHistoryFrameCopiedErrors_Object = MibTableColumn
tokenRingMLHistoryFrameCopiedErrors = _TokenRingMLHistoryFrameCopiedErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 22),
    _TokenRingMLHistoryFrameCopiedErrors_Type()
)
tokenRingMLHistoryFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryFrameCopiedErrors.setStatus("mandatory")
_TokenRingMLHistoryFrequencyErrors_Type = Counter32
_TokenRingMLHistoryFrequencyErrors_Object = MibTableColumn
tokenRingMLHistoryFrequencyErrors = _TokenRingMLHistoryFrequencyErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 23),
    _TokenRingMLHistoryFrequencyErrors_Type()
)
tokenRingMLHistoryFrequencyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryFrequencyErrors.setStatus("mandatory")
_TokenRingMLHistoryTokenErrors_Type = Counter32
_TokenRingMLHistoryTokenErrors_Object = MibTableColumn
tokenRingMLHistoryTokenErrors = _TokenRingMLHistoryTokenErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 24),
    _TokenRingMLHistoryTokenErrors_Type()
)
tokenRingMLHistoryTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryTokenErrors.setStatus("mandatory")
_TokenRingMLHistorySoftErrorReports_Type = Counter32
_TokenRingMLHistorySoftErrorReports_Object = MibTableColumn
tokenRingMLHistorySoftErrorReports = _TokenRingMLHistorySoftErrorReports_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 25),
    _TokenRingMLHistorySoftErrorReports_Type()
)
tokenRingMLHistorySoftErrorReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistorySoftErrorReports.setStatus("mandatory")
_TokenRingMLHistoryRingPollEvents_Type = Counter32
_TokenRingMLHistoryRingPollEvents_Object = MibTableColumn
tokenRingMLHistoryRingPollEvents = _TokenRingMLHistoryRingPollEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 26),
    _TokenRingMLHistoryRingPollEvents_Type()
)
tokenRingMLHistoryRingPollEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryRingPollEvents.setStatus("mandatory")
_TokenRingMLHistoryActiveStations_Type = Integer32
_TokenRingMLHistoryActiveStations_Object = MibTableColumn
tokenRingMLHistoryActiveStations = _TokenRingMLHistoryActiveStations_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 3, 1, 27),
    _TokenRingMLHistoryActiveStations_Type()
)
tokenRingMLHistoryActiveStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingMLHistoryActiveStations.setStatus("mandatory")
_TokenRingPHistoryTable_Object = MibTable
tokenRingPHistoryTable = _TokenRingPHistoryTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4)
)
if mibBuilder.loadTexts:
    tokenRingPHistoryTable.setStatus("mandatory")
_TokenRingPHistoryEntry_Object = MibTableRow
tokenRingPHistoryEntry = _TokenRingPHistoryEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1)
)
tokenRingPHistoryEntry.setIndexNames(
    (0, "TOKEN-RING-RMON-MIB", "tokenRingPHistoryIndex"),
    (0, "TOKEN-RING-RMON-MIB", "tokenRingPHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    tokenRingPHistoryEntry.setStatus("mandatory")


class _TokenRingPHistoryIndex_Type(Integer32):
    """Custom type tokenRingPHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TokenRingPHistoryIndex_Type.__name__ = "Integer32"
_TokenRingPHistoryIndex_Object = MibTableColumn
tokenRingPHistoryIndex = _TokenRingPHistoryIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 1),
    _TokenRingPHistoryIndex_Type()
)
tokenRingPHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistoryIndex.setStatus("mandatory")
_TokenRingPHistorySampleIndex_Type = Integer32
_TokenRingPHistorySampleIndex_Object = MibTableColumn
tokenRingPHistorySampleIndex = _TokenRingPHistorySampleIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 2),
    _TokenRingPHistorySampleIndex_Type()
)
tokenRingPHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistorySampleIndex.setStatus("mandatory")
_TokenRingPHistoryIntervalStart_Type = TimeTicks
_TokenRingPHistoryIntervalStart_Object = MibTableColumn
tokenRingPHistoryIntervalStart = _TokenRingPHistoryIntervalStart_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 3),
    _TokenRingPHistoryIntervalStart_Type()
)
tokenRingPHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistoryIntervalStart.setStatus("mandatory")
_TokenRingPHistoryDropEvents_Type = Counter32
_TokenRingPHistoryDropEvents_Object = MibTableColumn
tokenRingPHistoryDropEvents = _TokenRingPHistoryDropEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 4),
    _TokenRingPHistoryDropEvents_Type()
)
tokenRingPHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistoryDropEvents.setStatus("mandatory")
_TokenRingPHistoryDataOctets_Type = Counter32
_TokenRingPHistoryDataOctets_Object = MibTableColumn
tokenRingPHistoryDataOctets = _TokenRingPHistoryDataOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 5),
    _TokenRingPHistoryDataOctets_Type()
)
tokenRingPHistoryDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistoryDataOctets.setStatus("mandatory")
_TokenRingPHistoryDataPkts_Type = Counter32
_TokenRingPHistoryDataPkts_Object = MibTableColumn
tokenRingPHistoryDataPkts = _TokenRingPHistoryDataPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 6),
    _TokenRingPHistoryDataPkts_Type()
)
tokenRingPHistoryDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistoryDataPkts.setStatus("mandatory")
_TokenRingPHistoryDataBroadcastPkts_Type = Counter32
_TokenRingPHistoryDataBroadcastPkts_Object = MibTableColumn
tokenRingPHistoryDataBroadcastPkts = _TokenRingPHistoryDataBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 7),
    _TokenRingPHistoryDataBroadcastPkts_Type()
)
tokenRingPHistoryDataBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistoryDataBroadcastPkts.setStatus("mandatory")
_TokenRingPHistoryDataMulticastPkts_Type = Counter32
_TokenRingPHistoryDataMulticastPkts_Object = MibTableColumn
tokenRingPHistoryDataMulticastPkts = _TokenRingPHistoryDataMulticastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 8),
    _TokenRingPHistoryDataMulticastPkts_Type()
)
tokenRingPHistoryDataMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistoryDataMulticastPkts.setStatus("mandatory")
_TokenRingPHistoryDataPkts18to63Octets_Type = Counter32
_TokenRingPHistoryDataPkts18to63Octets_Object = MibTableColumn
tokenRingPHistoryDataPkts18to63Octets = _TokenRingPHistoryDataPkts18to63Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 9),
    _TokenRingPHistoryDataPkts18to63Octets_Type()
)
tokenRingPHistoryDataPkts18to63Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistoryDataPkts18to63Octets.setStatus("mandatory")
_TokenRingPHistoryDataPkts64to127Octets_Type = Counter32
_TokenRingPHistoryDataPkts64to127Octets_Object = MibTableColumn
tokenRingPHistoryDataPkts64to127Octets = _TokenRingPHistoryDataPkts64to127Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 10),
    _TokenRingPHistoryDataPkts64to127Octets_Type()
)
tokenRingPHistoryDataPkts64to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistoryDataPkts64to127Octets.setStatus("mandatory")
_TokenRingPHistoryDataPkts128to255Octets_Type = Counter32
_TokenRingPHistoryDataPkts128to255Octets_Object = MibTableColumn
tokenRingPHistoryDataPkts128to255Octets = _TokenRingPHistoryDataPkts128to255Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 11),
    _TokenRingPHistoryDataPkts128to255Octets_Type()
)
tokenRingPHistoryDataPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistoryDataPkts128to255Octets.setStatus("mandatory")
_TokenRingPHistoryDataPkts256to511Octets_Type = Counter32
_TokenRingPHistoryDataPkts256to511Octets_Object = MibTableColumn
tokenRingPHistoryDataPkts256to511Octets = _TokenRingPHistoryDataPkts256to511Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 12),
    _TokenRingPHistoryDataPkts256to511Octets_Type()
)
tokenRingPHistoryDataPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistoryDataPkts256to511Octets.setStatus("mandatory")
_TokenRingPHistoryDataPkts512to1023Octets_Type = Counter32
_TokenRingPHistoryDataPkts512to1023Octets_Object = MibTableColumn
tokenRingPHistoryDataPkts512to1023Octets = _TokenRingPHistoryDataPkts512to1023Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 13),
    _TokenRingPHistoryDataPkts512to1023Octets_Type()
)
tokenRingPHistoryDataPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistoryDataPkts512to1023Octets.setStatus("mandatory")
_TokenRingPHistoryDataPkts1024to2047Octets_Type = Counter32
_TokenRingPHistoryDataPkts1024to2047Octets_Object = MibTableColumn
tokenRingPHistoryDataPkts1024to2047Octets = _TokenRingPHistoryDataPkts1024to2047Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 14),
    _TokenRingPHistoryDataPkts1024to2047Octets_Type()
)
tokenRingPHistoryDataPkts1024to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistoryDataPkts1024to2047Octets.setStatus("mandatory")
_TokenRingPHistoryDataPkts2048to4095Octets_Type = Counter32
_TokenRingPHistoryDataPkts2048to4095Octets_Object = MibTableColumn
tokenRingPHistoryDataPkts2048to4095Octets = _TokenRingPHistoryDataPkts2048to4095Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 15),
    _TokenRingPHistoryDataPkts2048to4095Octets_Type()
)
tokenRingPHistoryDataPkts2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistoryDataPkts2048to4095Octets.setStatus("mandatory")
_TokenRingPHistoryDataPkts4096to8191Octets_Type = Counter32
_TokenRingPHistoryDataPkts4096to8191Octets_Object = MibTableColumn
tokenRingPHistoryDataPkts4096to8191Octets = _TokenRingPHistoryDataPkts4096to8191Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 16),
    _TokenRingPHistoryDataPkts4096to8191Octets_Type()
)
tokenRingPHistoryDataPkts4096to8191Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistoryDataPkts4096to8191Octets.setStatus("mandatory")
_TokenRingPHistoryDataPkts8192to18000Octets_Type = Counter32
_TokenRingPHistoryDataPkts8192to18000Octets_Object = MibTableColumn
tokenRingPHistoryDataPkts8192to18000Octets = _TokenRingPHistoryDataPkts8192to18000Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 17),
    _TokenRingPHistoryDataPkts8192to18000Octets_Type()
)
tokenRingPHistoryDataPkts8192to18000Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistoryDataPkts8192to18000Octets.setStatus("mandatory")
_TokenRingPHistoryDataPktsGreaterThan18000Octets_Type = Counter32
_TokenRingPHistoryDataPktsGreaterThan18000Octets_Object = MibTableColumn
tokenRingPHistoryDataPktsGreaterThan18000Octets = _TokenRingPHistoryDataPktsGreaterThan18000Octets_Object(
    (1, 3, 6, 1, 2, 1, 16, 2, 4, 1, 18),
    _TokenRingPHistoryDataPktsGreaterThan18000Octets_Type()
)
tokenRingPHistoryDataPktsGreaterThan18000Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPHistoryDataPktsGreaterThan18000Octets.setStatus("mandatory")
_TokenRing_ObjectIdentity = ObjectIdentity
tokenRing = _TokenRing_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 10)
)
_RingStationControlTable_Object = MibTable
ringStationControlTable = _RingStationControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1)
)
if mibBuilder.loadTexts:
    ringStationControlTable.setStatus("mandatory")
_RingStationControlEntry_Object = MibTableRow
ringStationControlEntry = _RingStationControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1)
)
ringStationControlEntry.setIndexNames(
    (0, "TOKEN-RING-RMON-MIB", "ringStationControlIfIndex"),
)
if mibBuilder.loadTexts:
    ringStationControlEntry.setStatus("mandatory")


class _RingStationControlIfIndex_Type(Integer32):
    """Custom type ringStationControlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingStationControlIfIndex_Type.__name__ = "Integer32"
_RingStationControlIfIndex_Object = MibTableColumn
ringStationControlIfIndex = _RingStationControlIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 1),
    _RingStationControlIfIndex_Type()
)
ringStationControlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationControlIfIndex.setStatus("mandatory")
_RingStationControlTableSize_Type = Integer32
_RingStationControlTableSize_Object = MibTableColumn
ringStationControlTableSize = _RingStationControlTableSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 2),
    _RingStationControlTableSize_Type()
)
ringStationControlTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationControlTableSize.setStatus("mandatory")
_RingStationControlActiveStations_Type = Integer32
_RingStationControlActiveStations_Object = MibTableColumn
ringStationControlActiveStations = _RingStationControlActiveStations_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 3),
    _RingStationControlActiveStations_Type()
)
ringStationControlActiveStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationControlActiveStations.setStatus("mandatory")


class _RingStationControlRingState_Type(Integer32):
    """Custom type ringStationControlRingState based on Integer32"""
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
        *(("beaconBitStreamingState", 5),
          ("beaconFrameStreamingState", 4),
          ("beaconRingSignalLossState", 6),
          ("beaconSetRecoveryModeState", 7),
          ("claimTokenState", 3),
          ("normalOperation", 1),
          ("ringPurgeState", 2))
    )


_RingStationControlRingState_Type.__name__ = "Integer32"
_RingStationControlRingState_Object = MibTableColumn
ringStationControlRingState = _RingStationControlRingState_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 4),
    _RingStationControlRingState_Type()
)
ringStationControlRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationControlRingState.setStatus("mandatory")
_RingStationControlBeaconSender_Type = MacAddress
_RingStationControlBeaconSender_Object = MibTableColumn
ringStationControlBeaconSender = _RingStationControlBeaconSender_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 5),
    _RingStationControlBeaconSender_Type()
)
ringStationControlBeaconSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationControlBeaconSender.setStatus("mandatory")
_RingStationControlBeaconNAUN_Type = MacAddress
_RingStationControlBeaconNAUN_Object = MibTableColumn
ringStationControlBeaconNAUN = _RingStationControlBeaconNAUN_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 6),
    _RingStationControlBeaconNAUN_Type()
)
ringStationControlBeaconNAUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationControlBeaconNAUN.setStatus("mandatory")
_RingStationControlActiveMonitor_Type = MacAddress
_RingStationControlActiveMonitor_Object = MibTableColumn
ringStationControlActiveMonitor = _RingStationControlActiveMonitor_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 7),
    _RingStationControlActiveMonitor_Type()
)
ringStationControlActiveMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationControlActiveMonitor.setStatus("mandatory")
_RingStationControlOrderChanges_Type = Counter32
_RingStationControlOrderChanges_Object = MibTableColumn
ringStationControlOrderChanges = _RingStationControlOrderChanges_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 8),
    _RingStationControlOrderChanges_Type()
)
ringStationControlOrderChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationControlOrderChanges.setStatus("mandatory")
_RingStationControlOwner_Type = OwnerString
_RingStationControlOwner_Object = MibTableColumn
ringStationControlOwner = _RingStationControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 9),
    _RingStationControlOwner_Type()
)
ringStationControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringStationControlOwner.setStatus("mandatory")
_RingStationControlStatus_Type = EntryStatus
_RingStationControlStatus_Object = MibTableColumn
ringStationControlStatus = _RingStationControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 1, 1, 10),
    _RingStationControlStatus_Type()
)
ringStationControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringStationControlStatus.setStatus("mandatory")
_RingStationTable_Object = MibTable
ringStationTable = _RingStationTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2)
)
if mibBuilder.loadTexts:
    ringStationTable.setStatus("mandatory")
_RingStationEntry_Object = MibTableRow
ringStationEntry = _RingStationEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1)
)
ringStationEntry.setIndexNames(
    (0, "TOKEN-RING-RMON-MIB", "ringStationIfIndex"),
    (0, "TOKEN-RING-RMON-MIB", "ringStationMacAddress"),
)
if mibBuilder.loadTexts:
    ringStationEntry.setStatus("mandatory")
_RingStationIfIndex_Type = Integer32
_RingStationIfIndex_Object = MibTableColumn
ringStationIfIndex = _RingStationIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 1),
    _RingStationIfIndex_Type()
)
ringStationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationIfIndex.setStatus("mandatory")
_RingStationMacAddress_Type = MacAddress
_RingStationMacAddress_Object = MibTableColumn
ringStationMacAddress = _RingStationMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 2),
    _RingStationMacAddress_Type()
)
ringStationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationMacAddress.setStatus("mandatory")
_RingStationLastNAUN_Type = MacAddress
_RingStationLastNAUN_Object = MibTableColumn
ringStationLastNAUN = _RingStationLastNAUN_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 3),
    _RingStationLastNAUN_Type()
)
ringStationLastNAUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationLastNAUN.setStatus("mandatory")


class _RingStationStationStatus_Type(Integer32):
    """Custom type ringStationStationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("forcedRemoval", 3),
          ("inactive", 2))
    )


_RingStationStationStatus_Type.__name__ = "Integer32"
_RingStationStationStatus_Object = MibTableColumn
ringStationStationStatus = _RingStationStationStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 4),
    _RingStationStationStatus_Type()
)
ringStationStationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationStationStatus.setStatus("mandatory")
_RingStationLastEnterTime_Type = TimeTicks
_RingStationLastEnterTime_Object = MibTableColumn
ringStationLastEnterTime = _RingStationLastEnterTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 5),
    _RingStationLastEnterTime_Type()
)
ringStationLastEnterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationLastEnterTime.setStatus("mandatory")
_RingStationLastExitTime_Type = TimeTicks
_RingStationLastExitTime_Object = MibTableColumn
ringStationLastExitTime = _RingStationLastExitTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 6),
    _RingStationLastExitTime_Type()
)
ringStationLastExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationLastExitTime.setStatus("mandatory")
_RingStationDuplicateAddresses_Type = Counter32
_RingStationDuplicateAddresses_Object = MibTableColumn
ringStationDuplicateAddresses = _RingStationDuplicateAddresses_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 7),
    _RingStationDuplicateAddresses_Type()
)
ringStationDuplicateAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationDuplicateAddresses.setStatus("mandatory")
_RingStationInLineErrors_Type = Counter32
_RingStationInLineErrors_Object = MibTableColumn
ringStationInLineErrors = _RingStationInLineErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 8),
    _RingStationInLineErrors_Type()
)
ringStationInLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationInLineErrors.setStatus("mandatory")
_RingStationOutLineErrors_Type = Counter32
_RingStationOutLineErrors_Object = MibTableColumn
ringStationOutLineErrors = _RingStationOutLineErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 9),
    _RingStationOutLineErrors_Type()
)
ringStationOutLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationOutLineErrors.setStatus("mandatory")
_RingStationInternalErrors_Type = Counter32
_RingStationInternalErrors_Object = MibTableColumn
ringStationInternalErrors = _RingStationInternalErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 10),
    _RingStationInternalErrors_Type()
)
ringStationInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationInternalErrors.setStatus("mandatory")
_RingStationInBurstErrors_Type = Counter32
_RingStationInBurstErrors_Object = MibTableColumn
ringStationInBurstErrors = _RingStationInBurstErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 11),
    _RingStationInBurstErrors_Type()
)
ringStationInBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationInBurstErrors.setStatus("mandatory")
_RingStationOutBurstErrors_Type = Counter32
_RingStationOutBurstErrors_Object = MibTableColumn
ringStationOutBurstErrors = _RingStationOutBurstErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 12),
    _RingStationOutBurstErrors_Type()
)
ringStationOutBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationOutBurstErrors.setStatus("mandatory")
_RingStationACErrors_Type = Counter32
_RingStationACErrors_Object = MibTableColumn
ringStationACErrors = _RingStationACErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 13),
    _RingStationACErrors_Type()
)
ringStationACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationACErrors.setStatus("mandatory")
_RingStationAbortErrors_Type = Counter32
_RingStationAbortErrors_Object = MibTableColumn
ringStationAbortErrors = _RingStationAbortErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 14),
    _RingStationAbortErrors_Type()
)
ringStationAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationAbortErrors.setStatus("mandatory")
_RingStationLostFrameErrors_Type = Counter32
_RingStationLostFrameErrors_Object = MibTableColumn
ringStationLostFrameErrors = _RingStationLostFrameErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 15),
    _RingStationLostFrameErrors_Type()
)
ringStationLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationLostFrameErrors.setStatus("mandatory")
_RingStationCongestionErrors_Type = Counter32
_RingStationCongestionErrors_Object = MibTableColumn
ringStationCongestionErrors = _RingStationCongestionErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 16),
    _RingStationCongestionErrors_Type()
)
ringStationCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationCongestionErrors.setStatus("mandatory")
_RingStationFrameCopiedErrors_Type = Counter32
_RingStationFrameCopiedErrors_Object = MibTableColumn
ringStationFrameCopiedErrors = _RingStationFrameCopiedErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 17),
    _RingStationFrameCopiedErrors_Type()
)
ringStationFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationFrameCopiedErrors.setStatus("mandatory")
_RingStationFrequencyErrors_Type = Counter32
_RingStationFrequencyErrors_Object = MibTableColumn
ringStationFrequencyErrors = _RingStationFrequencyErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 18),
    _RingStationFrequencyErrors_Type()
)
ringStationFrequencyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationFrequencyErrors.setStatus("mandatory")
_RingStationTokenErrors_Type = Counter32
_RingStationTokenErrors_Object = MibTableColumn
ringStationTokenErrors = _RingStationTokenErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 19),
    _RingStationTokenErrors_Type()
)
ringStationTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationTokenErrors.setStatus("mandatory")
_RingStationInBeaconErrors_Type = Counter32
_RingStationInBeaconErrors_Object = MibTableColumn
ringStationInBeaconErrors = _RingStationInBeaconErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 20),
    _RingStationInBeaconErrors_Type()
)
ringStationInBeaconErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationInBeaconErrors.setStatus("mandatory")
_RingStationOutBeaconErrors_Type = Counter32
_RingStationOutBeaconErrors_Object = MibTableColumn
ringStationOutBeaconErrors = _RingStationOutBeaconErrors_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 21),
    _RingStationOutBeaconErrors_Type()
)
ringStationOutBeaconErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationOutBeaconErrors.setStatus("mandatory")
_RingStationInsertions_Type = Counter32
_RingStationInsertions_Object = MibTableColumn
ringStationInsertions = _RingStationInsertions_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 2, 1, 22),
    _RingStationInsertions_Type()
)
ringStationInsertions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationInsertions.setStatus("mandatory")
_RingStationOrderTable_Object = MibTable
ringStationOrderTable = _RingStationOrderTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3)
)
if mibBuilder.loadTexts:
    ringStationOrderTable.setStatus("mandatory")
_RingStationOrderEntry_Object = MibTableRow
ringStationOrderEntry = _RingStationOrderEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1)
)
ringStationOrderEntry.setIndexNames(
    (0, "TOKEN-RING-RMON-MIB", "ringStationOrderIfIndex"),
    (0, "TOKEN-RING-RMON-MIB", "ringStationOrderOrderIndex"),
)
if mibBuilder.loadTexts:
    ringStationOrderEntry.setStatus("mandatory")
_RingStationOrderIfIndex_Type = Integer32
_RingStationOrderIfIndex_Object = MibTableColumn
ringStationOrderIfIndex = _RingStationOrderIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 1),
    _RingStationOrderIfIndex_Type()
)
ringStationOrderIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationOrderIfIndex.setStatus("mandatory")
_RingStationOrderOrderIndex_Type = Integer32
_RingStationOrderOrderIndex_Object = MibTableColumn
ringStationOrderOrderIndex = _RingStationOrderOrderIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 2),
    _RingStationOrderOrderIndex_Type()
)
ringStationOrderOrderIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationOrderOrderIndex.setStatus("mandatory")
_RingStationOrderMacAddress_Type = MacAddress
_RingStationOrderMacAddress_Object = MibTableColumn
ringStationOrderMacAddress = _RingStationOrderMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 3, 1, 3),
    _RingStationOrderMacAddress_Type()
)
ringStationOrderMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationOrderMacAddress.setStatus("mandatory")
_RingStationConfigControlTable_Object = MibTable
ringStationConfigControlTable = _RingStationConfigControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 4)
)
if mibBuilder.loadTexts:
    ringStationConfigControlTable.setStatus("mandatory")
_RingStationConfigControlEntry_Object = MibTableRow
ringStationConfigControlEntry = _RingStationConfigControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 4, 1)
)
ringStationConfigControlEntry.setIndexNames(
    (0, "TOKEN-RING-RMON-MIB", "ringStationConfigControlIfIndex"),
    (0, "TOKEN-RING-RMON-MIB", "ringStationConfigControlMacAddress"),
)
if mibBuilder.loadTexts:
    ringStationConfigControlEntry.setStatus("mandatory")
_RingStationConfigControlIfIndex_Type = Integer32
_RingStationConfigControlIfIndex_Object = MibTableColumn
ringStationConfigControlIfIndex = _RingStationConfigControlIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 4, 1, 1),
    _RingStationConfigControlIfIndex_Type()
)
ringStationConfigControlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationConfigControlIfIndex.setStatus("mandatory")
_RingStationConfigControlMacAddress_Type = MacAddress
_RingStationConfigControlMacAddress_Object = MibTableColumn
ringStationConfigControlMacAddress = _RingStationConfigControlMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 4, 1, 2),
    _RingStationConfigControlMacAddress_Type()
)
ringStationConfigControlMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationConfigControlMacAddress.setStatus("mandatory")


class _RingStationConfigControlRemove_Type(Integer32):
    """Custom type ringStationConfigControlRemove based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("removing", 2),
          ("stable", 1))
    )


_RingStationConfigControlRemove_Type.__name__ = "Integer32"
_RingStationConfigControlRemove_Object = MibTableColumn
ringStationConfigControlRemove = _RingStationConfigControlRemove_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 4, 1, 3),
    _RingStationConfigControlRemove_Type()
)
ringStationConfigControlRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringStationConfigControlRemove.setStatus("mandatory")


class _RingStationConfigControlUpdateStats_Type(Integer32):
    """Custom type ringStationConfigControlUpdateStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stable", 1),
          ("updating", 2))
    )


_RingStationConfigControlUpdateStats_Type.__name__ = "Integer32"
_RingStationConfigControlUpdateStats_Object = MibTableColumn
ringStationConfigControlUpdateStats = _RingStationConfigControlUpdateStats_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 4, 1, 4),
    _RingStationConfigControlUpdateStats_Type()
)
ringStationConfigControlUpdateStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringStationConfigControlUpdateStats.setStatus("mandatory")
_RingStationConfigTable_Object = MibTable
ringStationConfigTable = _RingStationConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 5)
)
if mibBuilder.loadTexts:
    ringStationConfigTable.setStatus("mandatory")
_RingStationConfigEntry_Object = MibTableRow
ringStationConfigEntry = _RingStationConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 5, 1)
)
ringStationConfigEntry.setIndexNames(
    (0, "TOKEN-RING-RMON-MIB", "ringStationConfigIfIndex"),
    (0, "TOKEN-RING-RMON-MIB", "ringStationConfigMacAddress"),
)
if mibBuilder.loadTexts:
    ringStationConfigEntry.setStatus("mandatory")
_RingStationConfigIfIndex_Type = Integer32
_RingStationConfigIfIndex_Object = MibTableColumn
ringStationConfigIfIndex = _RingStationConfigIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 5, 1, 1),
    _RingStationConfigIfIndex_Type()
)
ringStationConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationConfigIfIndex.setStatus("mandatory")
_RingStationConfigMacAddress_Type = MacAddress
_RingStationConfigMacAddress_Object = MibTableColumn
ringStationConfigMacAddress = _RingStationConfigMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 5, 1, 2),
    _RingStationConfigMacAddress_Type()
)
ringStationConfigMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationConfigMacAddress.setStatus("mandatory")
_RingStationConfigUpdateTime_Type = TimeTicks
_RingStationConfigUpdateTime_Object = MibTableColumn
ringStationConfigUpdateTime = _RingStationConfigUpdateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 5, 1, 3),
    _RingStationConfigUpdateTime_Type()
)
ringStationConfigUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationConfigUpdateTime.setStatus("mandatory")


class _RingStationConfigLocation_Type(OctetString):
    """Custom type ringStationConfigLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RingStationConfigLocation_Type.__name__ = "OctetString"
_RingStationConfigLocation_Object = MibTableColumn
ringStationConfigLocation = _RingStationConfigLocation_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 5, 1, 4),
    _RingStationConfigLocation_Type()
)
ringStationConfigLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationConfigLocation.setStatus("mandatory")


class _RingStationConfigMicrocode_Type(OctetString):
    """Custom type ringStationConfigMicrocode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_RingStationConfigMicrocode_Type.__name__ = "OctetString"
_RingStationConfigMicrocode_Object = MibTableColumn
ringStationConfigMicrocode = _RingStationConfigMicrocode_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 5, 1, 5),
    _RingStationConfigMicrocode_Type()
)
ringStationConfigMicrocode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationConfigMicrocode.setStatus("mandatory")


class _RingStationConfigGroupAddress_Type(OctetString):
    """Custom type ringStationConfigGroupAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RingStationConfigGroupAddress_Type.__name__ = "OctetString"
_RingStationConfigGroupAddress_Object = MibTableColumn
ringStationConfigGroupAddress = _RingStationConfigGroupAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 5, 1, 6),
    _RingStationConfigGroupAddress_Type()
)
ringStationConfigGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationConfigGroupAddress.setStatus("mandatory")


class _RingStationConfigFunctionalAddress_Type(OctetString):
    """Custom type ringStationConfigFunctionalAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RingStationConfigFunctionalAddress_Type.__name__ = "OctetString"
_RingStationConfigFunctionalAddress_Object = MibTableColumn
ringStationConfigFunctionalAddress = _RingStationConfigFunctionalAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 5, 1, 7),
    _RingStationConfigFunctionalAddress_Type()
)
ringStationConfigFunctionalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStationConfigFunctionalAddress.setStatus("mandatory")
_SourceRoutingStatsTable_Object = MibTable
sourceRoutingStatsTable = _SourceRoutingStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6)
)
if mibBuilder.loadTexts:
    sourceRoutingStatsTable.setStatus("mandatory")
_SourceRoutingStatsEntry_Object = MibTableRow
sourceRoutingStatsEntry = _SourceRoutingStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1)
)
sourceRoutingStatsEntry.setIndexNames(
    (0, "TOKEN-RING-RMON-MIB", "sourceRoutingStatsIfIndex"),
)
if mibBuilder.loadTexts:
    sourceRoutingStatsEntry.setStatus("mandatory")
_SourceRoutingStatsIfIndex_Type = Integer32
_SourceRoutingStatsIfIndex_Object = MibTableColumn
sourceRoutingStatsIfIndex = _SourceRoutingStatsIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 1),
    _SourceRoutingStatsIfIndex_Type()
)
sourceRoutingStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsIfIndex.setStatus("mandatory")
_SourceRoutingStatsRingNumber_Type = Integer32
_SourceRoutingStatsRingNumber_Object = MibTableColumn
sourceRoutingStatsRingNumber = _SourceRoutingStatsRingNumber_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 2),
    _SourceRoutingStatsRingNumber_Type()
)
sourceRoutingStatsRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsRingNumber.setStatus("mandatory")
_SourceRoutingStatsInFrames_Type = Counter32
_SourceRoutingStatsInFrames_Object = MibTableColumn
sourceRoutingStatsInFrames = _SourceRoutingStatsInFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 3),
    _SourceRoutingStatsInFrames_Type()
)
sourceRoutingStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsInFrames.setStatus("mandatory")
_SourceRoutingStatsOutFrames_Type = Counter32
_SourceRoutingStatsOutFrames_Object = MibTableColumn
sourceRoutingStatsOutFrames = _SourceRoutingStatsOutFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 4),
    _SourceRoutingStatsOutFrames_Type()
)
sourceRoutingStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsOutFrames.setStatus("mandatory")
_SourceRoutingStatsThroughFrames_Type = Counter32
_SourceRoutingStatsThroughFrames_Object = MibTableColumn
sourceRoutingStatsThroughFrames = _SourceRoutingStatsThroughFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 5),
    _SourceRoutingStatsThroughFrames_Type()
)
sourceRoutingStatsThroughFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsThroughFrames.setStatus("mandatory")
_SourceRoutingStatsAllRoutesBroadcastFrames_Type = Counter32
_SourceRoutingStatsAllRoutesBroadcastFrames_Object = MibTableColumn
sourceRoutingStatsAllRoutesBroadcastFrames = _SourceRoutingStatsAllRoutesBroadcastFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 6),
    _SourceRoutingStatsAllRoutesBroadcastFrames_Type()
)
sourceRoutingStatsAllRoutesBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsAllRoutesBroadcastFrames.setStatus("mandatory")
_SourceRoutingStatsSingleRouteBroadcastFrames_Type = Counter32
_SourceRoutingStatsSingleRouteBroadcastFrames_Object = MibTableColumn
sourceRoutingStatsSingleRouteBroadcastFrames = _SourceRoutingStatsSingleRouteBroadcastFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 7),
    _SourceRoutingStatsSingleRouteBroadcastFrames_Type()
)
sourceRoutingStatsSingleRouteBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsSingleRouteBroadcastFrames.setStatus("mandatory")
_SourceRoutingStatsInOctets_Type = Counter32
_SourceRoutingStatsInOctets_Object = MibTableColumn
sourceRoutingStatsInOctets = _SourceRoutingStatsInOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 8),
    _SourceRoutingStatsInOctets_Type()
)
sourceRoutingStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsInOctets.setStatus("mandatory")
_SourceRoutingStatsOutOctets_Type = Counter32
_SourceRoutingStatsOutOctets_Object = MibTableColumn
sourceRoutingStatsOutOctets = _SourceRoutingStatsOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 9),
    _SourceRoutingStatsOutOctets_Type()
)
sourceRoutingStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsOutOctets.setStatus("mandatory")
_SourceRoutingStatsThroughOctets_Type = Counter32
_SourceRoutingStatsThroughOctets_Object = MibTableColumn
sourceRoutingStatsThroughOctets = _SourceRoutingStatsThroughOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 10),
    _SourceRoutingStatsThroughOctets_Type()
)
sourceRoutingStatsThroughOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsThroughOctets.setStatus("mandatory")
_SourceRoutingStatsAllRoutesBroadcastOctets_Type = Counter32
_SourceRoutingStatsAllRoutesBroadcastOctets_Object = MibTableColumn
sourceRoutingStatsAllRoutesBroadcastOctets = _SourceRoutingStatsAllRoutesBroadcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 11),
    _SourceRoutingStatsAllRoutesBroadcastOctets_Type()
)
sourceRoutingStatsAllRoutesBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsAllRoutesBroadcastOctets.setStatus("mandatory")
_SourceRoutingStatsSingleRoutesBroadcastOctets_Type = Counter32
_SourceRoutingStatsSingleRoutesBroadcastOctets_Object = MibTableColumn
sourceRoutingStatsSingleRoutesBroadcastOctets = _SourceRoutingStatsSingleRoutesBroadcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 12),
    _SourceRoutingStatsSingleRoutesBroadcastOctets_Type()
)
sourceRoutingStatsSingleRoutesBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsSingleRoutesBroadcastOctets.setStatus("mandatory")
_SourceRoutingStatsLocalLLCFrames_Type = Counter32
_SourceRoutingStatsLocalLLCFrames_Object = MibTableColumn
sourceRoutingStatsLocalLLCFrames = _SourceRoutingStatsLocalLLCFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 13),
    _SourceRoutingStatsLocalLLCFrames_Type()
)
sourceRoutingStatsLocalLLCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsLocalLLCFrames.setStatus("mandatory")
_SourceRoutingStats1HopFrames_Type = Counter32
_SourceRoutingStats1HopFrames_Object = MibTableColumn
sourceRoutingStats1HopFrames = _SourceRoutingStats1HopFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 14),
    _SourceRoutingStats1HopFrames_Type()
)
sourceRoutingStats1HopFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStats1HopFrames.setStatus("mandatory")
_SourceRoutingStats2HopsFrames_Type = Counter32
_SourceRoutingStats2HopsFrames_Object = MibTableColumn
sourceRoutingStats2HopsFrames = _SourceRoutingStats2HopsFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 15),
    _SourceRoutingStats2HopsFrames_Type()
)
sourceRoutingStats2HopsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStats2HopsFrames.setStatus("mandatory")
_SourceRoutingStats3HopsFrames_Type = Counter32
_SourceRoutingStats3HopsFrames_Object = MibTableColumn
sourceRoutingStats3HopsFrames = _SourceRoutingStats3HopsFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 16),
    _SourceRoutingStats3HopsFrames_Type()
)
sourceRoutingStats3HopsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStats3HopsFrames.setStatus("mandatory")
_SourceRoutingStats4HopsFrames_Type = Counter32
_SourceRoutingStats4HopsFrames_Object = MibTableColumn
sourceRoutingStats4HopsFrames = _SourceRoutingStats4HopsFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 17),
    _SourceRoutingStats4HopsFrames_Type()
)
sourceRoutingStats4HopsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStats4HopsFrames.setStatus("mandatory")
_SourceRoutingStats5HopsFrames_Type = Counter32
_SourceRoutingStats5HopsFrames_Object = MibTableColumn
sourceRoutingStats5HopsFrames = _SourceRoutingStats5HopsFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 18),
    _SourceRoutingStats5HopsFrames_Type()
)
sourceRoutingStats5HopsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStats5HopsFrames.setStatus("mandatory")
_SourceRoutingStats6HopsFrames_Type = Counter32
_SourceRoutingStats6HopsFrames_Object = MibTableColumn
sourceRoutingStats6HopsFrames = _SourceRoutingStats6HopsFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 19),
    _SourceRoutingStats6HopsFrames_Type()
)
sourceRoutingStats6HopsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStats6HopsFrames.setStatus("mandatory")
_SourceRoutingStats7HopsFrames_Type = Counter32
_SourceRoutingStats7HopsFrames_Object = MibTableColumn
sourceRoutingStats7HopsFrames = _SourceRoutingStats7HopsFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 20),
    _SourceRoutingStats7HopsFrames_Type()
)
sourceRoutingStats7HopsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStats7HopsFrames.setStatus("mandatory")
_SourceRoutingStats8HopsFrames_Type = Counter32
_SourceRoutingStats8HopsFrames_Object = MibTableColumn
sourceRoutingStats8HopsFrames = _SourceRoutingStats8HopsFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 21),
    _SourceRoutingStats8HopsFrames_Type()
)
sourceRoutingStats8HopsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStats8HopsFrames.setStatus("mandatory")
_SourceRoutingStatsMoreThan8HopsFrames_Type = Counter32
_SourceRoutingStatsMoreThan8HopsFrames_Object = MibTableColumn
sourceRoutingStatsMoreThan8HopsFrames = _SourceRoutingStatsMoreThan8HopsFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 22),
    _SourceRoutingStatsMoreThan8HopsFrames_Type()
)
sourceRoutingStatsMoreThan8HopsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceRoutingStatsMoreThan8HopsFrames.setStatus("mandatory")
_SourceRoutingStatsOwner_Type = OwnerString
_SourceRoutingStatsOwner_Object = MibTableColumn
sourceRoutingStatsOwner = _SourceRoutingStatsOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 23),
    _SourceRoutingStatsOwner_Type()
)
sourceRoutingStatsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceRoutingStatsOwner.setStatus("mandatory")
_SourceRoutingStatsStatus_Type = EntryStatus
_SourceRoutingStatsStatus_Object = MibTableColumn
sourceRoutingStatsStatus = _SourceRoutingStatsStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 10, 6, 1, 24),
    _SourceRoutingStatsStatus_Type()
)
sourceRoutingStatsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceRoutingStatsStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TOKEN-RING-RMON-MIB",
    **{"MacAddress": MacAddress,
       "TimeInterval": TimeInterval,
       "tokenRingMLStatsTable": tokenRingMLStatsTable,
       "tokenRingMLStatsEntry": tokenRingMLStatsEntry,
       "tokenRingMLStatsIndex": tokenRingMLStatsIndex,
       "tokenRingMLStatsDataSource": tokenRingMLStatsDataSource,
       "tokenRingMLStatsDropEvents": tokenRingMLStatsDropEvents,
       "tokenRingMLStatsMacOctets": tokenRingMLStatsMacOctets,
       "tokenRingMLStatsMacPkts": tokenRingMLStatsMacPkts,
       "tokenRingMLStatsRingPurgeEvents": tokenRingMLStatsRingPurgeEvents,
       "tokenRingMLStatsRingPurgePkts": tokenRingMLStatsRingPurgePkts,
       "tokenRingMLStatsBeaconEvents": tokenRingMLStatsBeaconEvents,
       "tokenRingMLStatsBeaconTime": tokenRingMLStatsBeaconTime,
       "tokenRingMLStatsBeaconPkts": tokenRingMLStatsBeaconPkts,
       "tokenRingMLStatsClaimTokenEvents": tokenRingMLStatsClaimTokenEvents,
       "tokenRingMLStatsClaimTokenPkts": tokenRingMLStatsClaimTokenPkts,
       "tokenRingMLStatsNAUNChanges": tokenRingMLStatsNAUNChanges,
       "tokenRingMLStatsLineErrors": tokenRingMLStatsLineErrors,
       "tokenRingMLStatsInternalErrors": tokenRingMLStatsInternalErrors,
       "tokenRingMLStatsBurstErrors": tokenRingMLStatsBurstErrors,
       "tokenRingMLStatsACErrors": tokenRingMLStatsACErrors,
       "tokenRingMLStatsAbortErrors": tokenRingMLStatsAbortErrors,
       "tokenRingMLStatsLostFrameErrors": tokenRingMLStatsLostFrameErrors,
       "tokenRingMLStatsCongestionErrors": tokenRingMLStatsCongestionErrors,
       "tokenRingMLStatsFrameCopiedErrors": tokenRingMLStatsFrameCopiedErrors,
       "tokenRingMLStatsFrequencyErrors": tokenRingMLStatsFrequencyErrors,
       "tokenRingMLStatsTokenErrors": tokenRingMLStatsTokenErrors,
       "tokenRingMLStatsSoftErrorReports": tokenRingMLStatsSoftErrorReports,
       "tokenRingMLStatsRingPollEvents": tokenRingMLStatsRingPollEvents,
       "tokenRingMLStatsOwner": tokenRingMLStatsOwner,
       "tokenRingMLStatsStatus": tokenRingMLStatsStatus,
       "tokenRingPStatsTable": tokenRingPStatsTable,
       "tokenRingPStatsEntry": tokenRingPStatsEntry,
       "tokenRingPStatsIndex": tokenRingPStatsIndex,
       "tokenRingPStatsDataSource": tokenRingPStatsDataSource,
       "tokenRingPStatsDropEvents": tokenRingPStatsDropEvents,
       "tokenRingPStatsDataOctets": tokenRingPStatsDataOctets,
       "tokenRingPStatsDataPkts": tokenRingPStatsDataPkts,
       "tokenRingPStatsDataBroadcastPkts": tokenRingPStatsDataBroadcastPkts,
       "tokenRingPStatsDataMulticastPkts": tokenRingPStatsDataMulticastPkts,
       "tokenRingPStatsDataPkts18to63Octets": tokenRingPStatsDataPkts18to63Octets,
       "tokenRingPStatsDataPkts64to127Octets": tokenRingPStatsDataPkts64to127Octets,
       "tokenRingPStatsDataPkts128to255Octets": tokenRingPStatsDataPkts128to255Octets,
       "tokenRingPStatsDataPkts256to511Octets": tokenRingPStatsDataPkts256to511Octets,
       "tokenRingPStatsDataPkts512to1023Octets": tokenRingPStatsDataPkts512to1023Octets,
       "tokenRingPStatsDataPkts1024to2047Octets": tokenRingPStatsDataPkts1024to2047Octets,
       "tokenRingPStatsDataPkts2048to4095Octets": tokenRingPStatsDataPkts2048to4095Octets,
       "tokenRingPStatsDataPkts4096to8191Octets": tokenRingPStatsDataPkts4096to8191Octets,
       "tokenRingPStatsDataPkts8192to18000Octets": tokenRingPStatsDataPkts8192to18000Octets,
       "tokenRingPStatsDataPktsGreaterThan18000Octets": tokenRingPStatsDataPktsGreaterThan18000Octets,
       "tokenRingPStatsOwner": tokenRingPStatsOwner,
       "tokenRingPStatsStatus": tokenRingPStatsStatus,
       "tokenRingMLHistoryTable": tokenRingMLHistoryTable,
       "tokenRingMLHistoryEntry": tokenRingMLHistoryEntry,
       "tokenRingMLHistoryIndex": tokenRingMLHistoryIndex,
       "tokenRingMLHistorySampleIndex": tokenRingMLHistorySampleIndex,
       "tokenRingMLHistoryIntervalStart": tokenRingMLHistoryIntervalStart,
       "tokenRingMLHistoryDropEvents": tokenRingMLHistoryDropEvents,
       "tokenRingMLHistoryMacOctets": tokenRingMLHistoryMacOctets,
       "tokenRingMLHistoryMacPkts": tokenRingMLHistoryMacPkts,
       "tokenRingMLHistoryRingPurgeEvents": tokenRingMLHistoryRingPurgeEvents,
       "tokenRingMLHistoryRingPurgePkts": tokenRingMLHistoryRingPurgePkts,
       "tokenRingMLHistoryBeaconEvents": tokenRingMLHistoryBeaconEvents,
       "tokenRingMLHistoryBeaconTime": tokenRingMLHistoryBeaconTime,
       "tokenRingMLHistoryBeaconPkts": tokenRingMLHistoryBeaconPkts,
       "tokenRingMLHistoryClaimTokenEvents": tokenRingMLHistoryClaimTokenEvents,
       "tokenRingMLHistoryClaimTokenPkts": tokenRingMLHistoryClaimTokenPkts,
       "tokenRingMLHistoryNAUNChanges": tokenRingMLHistoryNAUNChanges,
       "tokenRingMLHistoryLineErrors": tokenRingMLHistoryLineErrors,
       "tokenRingMLHistoryInternalErrors": tokenRingMLHistoryInternalErrors,
       "tokenRingMLHistoryBurstErrors": tokenRingMLHistoryBurstErrors,
       "tokenRingMLHistoryACErrors": tokenRingMLHistoryACErrors,
       "tokenRingMLHistoryAbortErrors": tokenRingMLHistoryAbortErrors,
       "tokenRingMLHistoryLostFrameErrors": tokenRingMLHistoryLostFrameErrors,
       "tokenRingMLHistoryCongestionErrors": tokenRingMLHistoryCongestionErrors,
       "tokenRingMLHistoryFrameCopiedErrors": tokenRingMLHistoryFrameCopiedErrors,
       "tokenRingMLHistoryFrequencyErrors": tokenRingMLHistoryFrequencyErrors,
       "tokenRingMLHistoryTokenErrors": tokenRingMLHistoryTokenErrors,
       "tokenRingMLHistorySoftErrorReports": tokenRingMLHistorySoftErrorReports,
       "tokenRingMLHistoryRingPollEvents": tokenRingMLHistoryRingPollEvents,
       "tokenRingMLHistoryActiveStations": tokenRingMLHistoryActiveStations,
       "tokenRingPHistoryTable": tokenRingPHistoryTable,
       "tokenRingPHistoryEntry": tokenRingPHistoryEntry,
       "tokenRingPHistoryIndex": tokenRingPHistoryIndex,
       "tokenRingPHistorySampleIndex": tokenRingPHistorySampleIndex,
       "tokenRingPHistoryIntervalStart": tokenRingPHistoryIntervalStart,
       "tokenRingPHistoryDropEvents": tokenRingPHistoryDropEvents,
       "tokenRingPHistoryDataOctets": tokenRingPHistoryDataOctets,
       "tokenRingPHistoryDataPkts": tokenRingPHistoryDataPkts,
       "tokenRingPHistoryDataBroadcastPkts": tokenRingPHistoryDataBroadcastPkts,
       "tokenRingPHistoryDataMulticastPkts": tokenRingPHistoryDataMulticastPkts,
       "tokenRingPHistoryDataPkts18to63Octets": tokenRingPHistoryDataPkts18to63Octets,
       "tokenRingPHistoryDataPkts64to127Octets": tokenRingPHistoryDataPkts64to127Octets,
       "tokenRingPHistoryDataPkts128to255Octets": tokenRingPHistoryDataPkts128to255Octets,
       "tokenRingPHistoryDataPkts256to511Octets": tokenRingPHistoryDataPkts256to511Octets,
       "tokenRingPHistoryDataPkts512to1023Octets": tokenRingPHistoryDataPkts512to1023Octets,
       "tokenRingPHistoryDataPkts1024to2047Octets": tokenRingPHistoryDataPkts1024to2047Octets,
       "tokenRingPHistoryDataPkts2048to4095Octets": tokenRingPHistoryDataPkts2048to4095Octets,
       "tokenRingPHistoryDataPkts4096to8191Octets": tokenRingPHistoryDataPkts4096to8191Octets,
       "tokenRingPHistoryDataPkts8192to18000Octets": tokenRingPHistoryDataPkts8192to18000Octets,
       "tokenRingPHistoryDataPktsGreaterThan18000Octets": tokenRingPHistoryDataPktsGreaterThan18000Octets,
       "tokenRing": tokenRing,
       "ringStationControlTable": ringStationControlTable,
       "ringStationControlEntry": ringStationControlEntry,
       "ringStationControlIfIndex": ringStationControlIfIndex,
       "ringStationControlTableSize": ringStationControlTableSize,
       "ringStationControlActiveStations": ringStationControlActiveStations,
       "ringStationControlRingState": ringStationControlRingState,
       "ringStationControlBeaconSender": ringStationControlBeaconSender,
       "ringStationControlBeaconNAUN": ringStationControlBeaconNAUN,
       "ringStationControlActiveMonitor": ringStationControlActiveMonitor,
       "ringStationControlOrderChanges": ringStationControlOrderChanges,
       "ringStationControlOwner": ringStationControlOwner,
       "ringStationControlStatus": ringStationControlStatus,
       "ringStationTable": ringStationTable,
       "ringStationEntry": ringStationEntry,
       "ringStationIfIndex": ringStationIfIndex,
       "ringStationMacAddress": ringStationMacAddress,
       "ringStationLastNAUN": ringStationLastNAUN,
       "ringStationStationStatus": ringStationStationStatus,
       "ringStationLastEnterTime": ringStationLastEnterTime,
       "ringStationLastExitTime": ringStationLastExitTime,
       "ringStationDuplicateAddresses": ringStationDuplicateAddresses,
       "ringStationInLineErrors": ringStationInLineErrors,
       "ringStationOutLineErrors": ringStationOutLineErrors,
       "ringStationInternalErrors": ringStationInternalErrors,
       "ringStationInBurstErrors": ringStationInBurstErrors,
       "ringStationOutBurstErrors": ringStationOutBurstErrors,
       "ringStationACErrors": ringStationACErrors,
       "ringStationAbortErrors": ringStationAbortErrors,
       "ringStationLostFrameErrors": ringStationLostFrameErrors,
       "ringStationCongestionErrors": ringStationCongestionErrors,
       "ringStationFrameCopiedErrors": ringStationFrameCopiedErrors,
       "ringStationFrequencyErrors": ringStationFrequencyErrors,
       "ringStationTokenErrors": ringStationTokenErrors,
       "ringStationInBeaconErrors": ringStationInBeaconErrors,
       "ringStationOutBeaconErrors": ringStationOutBeaconErrors,
       "ringStationInsertions": ringStationInsertions,
       "ringStationOrderTable": ringStationOrderTable,
       "ringStationOrderEntry": ringStationOrderEntry,
       "ringStationOrderIfIndex": ringStationOrderIfIndex,
       "ringStationOrderOrderIndex": ringStationOrderOrderIndex,
       "ringStationOrderMacAddress": ringStationOrderMacAddress,
       "ringStationConfigControlTable": ringStationConfigControlTable,
       "ringStationConfigControlEntry": ringStationConfigControlEntry,
       "ringStationConfigControlIfIndex": ringStationConfigControlIfIndex,
       "ringStationConfigControlMacAddress": ringStationConfigControlMacAddress,
       "ringStationConfigControlRemove": ringStationConfigControlRemove,
       "ringStationConfigControlUpdateStats": ringStationConfigControlUpdateStats,
       "ringStationConfigTable": ringStationConfigTable,
       "ringStationConfigEntry": ringStationConfigEntry,
       "ringStationConfigIfIndex": ringStationConfigIfIndex,
       "ringStationConfigMacAddress": ringStationConfigMacAddress,
       "ringStationConfigUpdateTime": ringStationConfigUpdateTime,
       "ringStationConfigLocation": ringStationConfigLocation,
       "ringStationConfigMicrocode": ringStationConfigMicrocode,
       "ringStationConfigGroupAddress": ringStationConfigGroupAddress,
       "ringStationConfigFunctionalAddress": ringStationConfigFunctionalAddress,
       "sourceRoutingStatsTable": sourceRoutingStatsTable,
       "sourceRoutingStatsEntry": sourceRoutingStatsEntry,
       "sourceRoutingStatsIfIndex": sourceRoutingStatsIfIndex,
       "sourceRoutingStatsRingNumber": sourceRoutingStatsRingNumber,
       "sourceRoutingStatsInFrames": sourceRoutingStatsInFrames,
       "sourceRoutingStatsOutFrames": sourceRoutingStatsOutFrames,
       "sourceRoutingStatsThroughFrames": sourceRoutingStatsThroughFrames,
       "sourceRoutingStatsAllRoutesBroadcastFrames": sourceRoutingStatsAllRoutesBroadcastFrames,
       "sourceRoutingStatsSingleRouteBroadcastFrames": sourceRoutingStatsSingleRouteBroadcastFrames,
       "sourceRoutingStatsInOctets": sourceRoutingStatsInOctets,
       "sourceRoutingStatsOutOctets": sourceRoutingStatsOutOctets,
       "sourceRoutingStatsThroughOctets": sourceRoutingStatsThroughOctets,
       "sourceRoutingStatsAllRoutesBroadcastOctets": sourceRoutingStatsAllRoutesBroadcastOctets,
       "sourceRoutingStatsSingleRoutesBroadcastOctets": sourceRoutingStatsSingleRoutesBroadcastOctets,
       "sourceRoutingStatsLocalLLCFrames": sourceRoutingStatsLocalLLCFrames,
       "sourceRoutingStats1HopFrames": sourceRoutingStats1HopFrames,
       "sourceRoutingStats2HopsFrames": sourceRoutingStats2HopsFrames,
       "sourceRoutingStats3HopsFrames": sourceRoutingStats3HopsFrames,
       "sourceRoutingStats4HopsFrames": sourceRoutingStats4HopsFrames,
       "sourceRoutingStats5HopsFrames": sourceRoutingStats5HopsFrames,
       "sourceRoutingStats6HopsFrames": sourceRoutingStats6HopsFrames,
       "sourceRoutingStats7HopsFrames": sourceRoutingStats7HopsFrames,
       "sourceRoutingStats8HopsFrames": sourceRoutingStats8HopsFrames,
       "sourceRoutingStatsMoreThan8HopsFrames": sourceRoutingStatsMoreThan8HopsFrames,
       "sourceRoutingStatsOwner": sourceRoutingStatsOwner,
       "sourceRoutingStatsStatus": sourceRoutingStatsStatus}
)
