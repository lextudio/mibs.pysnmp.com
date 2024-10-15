# SNMP MIB module (Novell-LANalyzer-TR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Novell-LANalyzer-TR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:26 2024
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
 OwnerString) = mibBuilder.importSymbols(
    "RFC1271-MIB",
    "EntryStatus",
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_ProductType_ObjectIdentity = ObjectIdentity
productType = _ProductType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 1)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_Ringrmon_mib_ObjectIdentity = ObjectIdentity
ringrmon_mib = _Ringrmon_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 15)
)
_TokenRingStatistics_ObjectIdentity = ObjectIdentity
tokenRingStatistics = _TokenRingStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1)
)
_TokenRingStatsTable_Object = MibTable
tokenRingStatsTable = _TokenRingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1)
)
if mibBuilder.loadTexts:
    tokenRingStatsTable.setStatus("mandatory")
_TokenRingStatsEntry_Object = MibTableRow
tokenRingStatsEntry = _TokenRingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1)
)
tokenRingStatsEntry.setIndexNames(
    (0, "Novell-LANalyzer-TR-MIB", "tokenRingStatsIndex"),
)
if mibBuilder.loadTexts:
    tokenRingStatsEntry.setStatus("mandatory")


class _TokenRingStatsIndex_Type(Integer32):
    """Custom type tokenRingStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TokenRingStatsIndex_Type.__name__ = "Integer32"
_TokenRingStatsIndex_Object = MibTableColumn
tokenRingStatsIndex = _TokenRingStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 1),
    _TokenRingStatsIndex_Type()
)
tokenRingStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsIndex.setStatus("mandatory")
_TokenRingStatsDataSource_Type = ObjectIdentifier
_TokenRingStatsDataSource_Object = MibTableColumn
tokenRingStatsDataSource = _TokenRingStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 2),
    _TokenRingStatsDataSource_Type()
)
tokenRingStatsDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingStatsDataSource.setStatus("mandatory")
_TokenRingStatsDropEvents_Type = Counter32
_TokenRingStatsDropEvents_Object = MibTableColumn
tokenRingStatsDropEvents = _TokenRingStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 3),
    _TokenRingStatsDropEvents_Type()
)
tokenRingStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDropEvents.setStatus("mandatory")
_TokenRingStatsDataOctets_Type = Counter32
_TokenRingStatsDataOctets_Object = MibTableColumn
tokenRingStatsDataOctets = _TokenRingStatsDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 4),
    _TokenRingStatsDataOctets_Type()
)
tokenRingStatsDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataOctets.setStatus("mandatory")
_TokenRingStatsDataPkts_Type = Counter32
_TokenRingStatsDataPkts_Object = MibTableColumn
tokenRingStatsDataPkts = _TokenRingStatsDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 5),
    _TokenRingStatsDataPkts_Type()
)
tokenRingStatsDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts.setStatus("mandatory")
_TokenRingStatsBroadcastDataPkts_Type = Counter32
_TokenRingStatsBroadcastDataPkts_Object = MibTableColumn
tokenRingStatsBroadcastDataPkts = _TokenRingStatsBroadcastDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 6),
    _TokenRingStatsBroadcastDataPkts_Type()
)
tokenRingStatsBroadcastDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsBroadcastDataPkts.setStatus("mandatory")
_TokenRingStatsMulticastDataPkts_Type = Counter32
_TokenRingStatsMulticastDataPkts_Object = MibTableColumn
tokenRingStatsMulticastDataPkts = _TokenRingStatsMulticastDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 7),
    _TokenRingStatsMulticastDataPkts_Type()
)
tokenRingStatsMulticastDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsMulticastDataPkts.setStatus("mandatory")
_TokenRingStatsMACOctets_Type = Counter32
_TokenRingStatsMACOctets_Object = MibTableColumn
tokenRingStatsMACOctets = _TokenRingStatsMACOctets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 8),
    _TokenRingStatsMACOctets_Type()
)
tokenRingStatsMACOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsMACOctets.setStatus("mandatory")
_TokenRingStatsMACPkts_Type = Counter32
_TokenRingStatsMACPkts_Object = MibTableColumn
tokenRingStatsMACPkts = _TokenRingStatsMACPkts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 9),
    _TokenRingStatsMACPkts_Type()
)
tokenRingStatsMACPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsMACPkts.setStatus("mandatory")
_TokenRingStatsRingPurges_Type = Counter32
_TokenRingStatsRingPurges_Object = MibTableColumn
tokenRingStatsRingPurges = _TokenRingStatsRingPurges_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 10),
    _TokenRingStatsRingPurges_Type()
)
tokenRingStatsRingPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsRingPurges.setStatus("mandatory")
_TokenRingStatsMonitorContentions_Type = Counter32
_TokenRingStatsMonitorContentions_Object = MibTableColumn
tokenRingStatsMonitorContentions = _TokenRingStatsMonitorContentions_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 11),
    _TokenRingStatsMonitorContentions_Type()
)
tokenRingStatsMonitorContentions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsMonitorContentions.setStatus("mandatory")
_TokenRingStatsBeacons_Type = Counter32
_TokenRingStatsBeacons_Object = MibTableColumn
tokenRingStatsBeacons = _TokenRingStatsBeacons_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 12),
    _TokenRingStatsBeacons_Type()
)
tokenRingStatsBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsBeacons.setStatus("mandatory")
_TokenRingStatsLostMonitors_Type = Counter32
_TokenRingStatsLostMonitors_Object = MibTableColumn
tokenRingStatsLostMonitors = _TokenRingStatsLostMonitors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 13),
    _TokenRingStatsLostMonitors_Type()
)
tokenRingStatsLostMonitors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsLostMonitors.setStatus("mandatory")
_TokenRingStatsDuplicateMonitors_Type = Counter32
_TokenRingStatsDuplicateMonitors_Object = MibTableColumn
tokenRingStatsDuplicateMonitors = _TokenRingStatsDuplicateMonitors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 14),
    _TokenRingStatsDuplicateMonitors_Type()
)
tokenRingStatsDuplicateMonitors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDuplicateMonitors.setStatus("mandatory")
_TokenRingStatsDuplicateAddresses_Type = Counter32
_TokenRingStatsDuplicateAddresses_Object = MibTableColumn
tokenRingStatsDuplicateAddresses = _TokenRingStatsDuplicateAddresses_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 15),
    _TokenRingStatsDuplicateAddresses_Type()
)
tokenRingStatsDuplicateAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDuplicateAddresses.setStatus("mandatory")
_TokenRingStatsRingPollFailures_Type = Counter32
_TokenRingStatsRingPollFailures_Object = MibTableColumn
tokenRingStatsRingPollFailures = _TokenRingStatsRingPollFailures_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 16),
    _TokenRingStatsRingPollFailures_Type()
)
tokenRingStatsRingPollFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsRingPollFailures.setStatus("mandatory")
_TokenRingStatsLineErrors_Type = Counter32
_TokenRingStatsLineErrors_Object = MibTableColumn
tokenRingStatsLineErrors = _TokenRingStatsLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 17),
    _TokenRingStatsLineErrors_Type()
)
tokenRingStatsLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsLineErrors.setStatus("mandatory")
_TokenRingStatsInternalErrors_Type = Counter32
_TokenRingStatsInternalErrors_Object = MibTableColumn
tokenRingStatsInternalErrors = _TokenRingStatsInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 18),
    _TokenRingStatsInternalErrors_Type()
)
tokenRingStatsInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsInternalErrors.setStatus("mandatory")
_TokenRingStatsBurstErrors_Type = Counter32
_TokenRingStatsBurstErrors_Object = MibTableColumn
tokenRingStatsBurstErrors = _TokenRingStatsBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 19),
    _TokenRingStatsBurstErrors_Type()
)
tokenRingStatsBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsBurstErrors.setStatus("mandatory")
_TokenRingStatsACErrors_Type = Counter32
_TokenRingStatsACErrors_Object = MibTableColumn
tokenRingStatsACErrors = _TokenRingStatsACErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 20),
    _TokenRingStatsACErrors_Type()
)
tokenRingStatsACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsACErrors.setStatus("mandatory")
_TokenRingStatsAbortDelimiters_Type = Counter32
_TokenRingStatsAbortDelimiters_Object = MibTableColumn
tokenRingStatsAbortDelimiters = _TokenRingStatsAbortDelimiters_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 21),
    _TokenRingStatsAbortDelimiters_Type()
)
tokenRingStatsAbortDelimiters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsAbortDelimiters.setStatus("mandatory")
_TokenRingStatsLostFrameErrors_Type = Counter32
_TokenRingStatsLostFrameErrors_Object = MibTableColumn
tokenRingStatsLostFrameErrors = _TokenRingStatsLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 22),
    _TokenRingStatsLostFrameErrors_Type()
)
tokenRingStatsLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsLostFrameErrors.setStatus("mandatory")
_TokenRingStatsReceiveCongestions_Type = Counter32
_TokenRingStatsReceiveCongestions_Object = MibTableColumn
tokenRingStatsReceiveCongestions = _TokenRingStatsReceiveCongestions_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 23),
    _TokenRingStatsReceiveCongestions_Type()
)
tokenRingStatsReceiveCongestions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsReceiveCongestions.setStatus("mandatory")
_TokenRingStatsFrameCopiedErrors_Type = Counter32
_TokenRingStatsFrameCopiedErrors_Object = MibTableColumn
tokenRingStatsFrameCopiedErrors = _TokenRingStatsFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 24),
    _TokenRingStatsFrameCopiedErrors_Type()
)
tokenRingStatsFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsFrameCopiedErrors.setStatus("mandatory")
_TokenRingStatsFrequencyErrors_Type = Counter32
_TokenRingStatsFrequencyErrors_Object = MibTableColumn
tokenRingStatsFrequencyErrors = _TokenRingStatsFrequencyErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 25),
    _TokenRingStatsFrequencyErrors_Type()
)
tokenRingStatsFrequencyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsFrequencyErrors.setStatus("mandatory")
_TokenRingStatsTokenErrors_Type = Counter32
_TokenRingStatsTokenErrors_Object = MibTableColumn
tokenRingStatsTokenErrors = _TokenRingStatsTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 26),
    _TokenRingStatsTokenErrors_Type()
)
tokenRingStatsTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsTokenErrors.setStatus("mandatory")
_TokenRingStatsDataPktsUndersizePkts_Type = Counter32
_TokenRingStatsDataPktsUndersizePkts_Object = MibTableColumn
tokenRingStatsDataPktsUndersizePkts = _TokenRingStatsDataPktsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 27),
    _TokenRingStatsDataPktsUndersizePkts_Type()
)
tokenRingStatsDataPktsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPktsUndersizePkts.setStatus("mandatory")
_TokenRingStatsDataPkts18to63Octets_Type = Counter32
_TokenRingStatsDataPkts18to63Octets_Object = MibTableColumn
tokenRingStatsDataPkts18to63Octets = _TokenRingStatsDataPkts18to63Octets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 28),
    _TokenRingStatsDataPkts18to63Octets_Type()
)
tokenRingStatsDataPkts18to63Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts18to63Octets.setStatus("mandatory")
_TokenRingStatsDataPkts64to127Octets_Type = Counter32
_TokenRingStatsDataPkts64to127Octets_Object = MibTableColumn
tokenRingStatsDataPkts64to127Octets = _TokenRingStatsDataPkts64to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 29),
    _TokenRingStatsDataPkts64to127Octets_Type()
)
tokenRingStatsDataPkts64to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts64to127Octets.setStatus("mandatory")
_TokenRingStatsDataPkts128to255Octets_Type = Counter32
_TokenRingStatsDataPkts128to255Octets_Object = MibTableColumn
tokenRingStatsDataPkts128to255Octets = _TokenRingStatsDataPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 30),
    _TokenRingStatsDataPkts128to255Octets_Type()
)
tokenRingStatsDataPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts128to255Octets.setStatus("mandatory")
_TokenRingStatsDataPkts256to511Octets_Type = Counter32
_TokenRingStatsDataPkts256to511Octets_Object = MibTableColumn
tokenRingStatsDataPkts256to511Octets = _TokenRingStatsDataPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 31),
    _TokenRingStatsDataPkts256to511Octets_Type()
)
tokenRingStatsDataPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts256to511Octets.setStatus("mandatory")
_TokenRingStatsDataPkts512to1023Octets_Type = Counter32
_TokenRingStatsDataPkts512to1023Octets_Object = MibTableColumn
tokenRingStatsDataPkts512to1023Octets = _TokenRingStatsDataPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 32),
    _TokenRingStatsDataPkts512to1023Octets_Type()
)
tokenRingStatsDataPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts512to1023Octets.setStatus("mandatory")
_TokenRingStatsDataPkts1024to2047Octets_Type = Counter32
_TokenRingStatsDataPkts1024to2047Octets_Object = MibTableColumn
tokenRingStatsDataPkts1024to2047Octets = _TokenRingStatsDataPkts1024to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 33),
    _TokenRingStatsDataPkts1024to2047Octets_Type()
)
tokenRingStatsDataPkts1024to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts1024to2047Octets.setStatus("mandatory")
_TokenRingStatsDataPkts2048to4608Octets_Type = Counter32
_TokenRingStatsDataPkts2048to4608Octets_Object = MibTableColumn
tokenRingStatsDataPkts2048to4608Octets = _TokenRingStatsDataPkts2048to4608Octets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 34),
    _TokenRingStatsDataPkts2048to4608Octets_Type()
)
tokenRingStatsDataPkts2048to4608Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts2048to4608Octets.setStatus("mandatory")
_TokenRingStatsDataPkts4609to18000Octets_Type = Counter32
_TokenRingStatsDataPkts4609to18000Octets_Object = MibTableColumn
tokenRingStatsDataPkts4609to18000Octets = _TokenRingStatsDataPkts4609to18000Octets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 35),
    _TokenRingStatsDataPkts4609to18000Octets_Type()
)
tokenRingStatsDataPkts4609to18000Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPkts4609to18000Octets.setStatus("mandatory")
_TokenRingStatsDataPktsMoreThan18000Octets_Type = Counter32
_TokenRingStatsDataPktsMoreThan18000Octets_Object = MibTableColumn
tokenRingStatsDataPktsMoreThan18000Octets = _TokenRingStatsDataPktsMoreThan18000Octets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 36),
    _TokenRingStatsDataPktsMoreThan18000Octets_Type()
)
tokenRingStatsDataPktsMoreThan18000Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingStatsDataPktsMoreThan18000Octets.setStatus("mandatory")
_TokenRingStatsOwner_Type = OwnerString
_TokenRingStatsOwner_Object = MibTableColumn
tokenRingStatsOwner = _TokenRingStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 37),
    _TokenRingStatsOwner_Type()
)
tokenRingStatsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingStatsOwner.setStatus("mandatory")
_TokenRingStatsStatus_Type = EntryStatus
_TokenRingStatsStatus_Object = MibTableColumn
tokenRingStatsStatus = _TokenRingStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 1, 1, 1, 38),
    _TokenRingStatsStatus_Type()
)
tokenRingStatsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingStatsStatus.setStatus("mandatory")
_TokenRingHistory_ObjectIdentity = ObjectIdentity
tokenRingHistory = _TokenRingHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2)
)
_TokenRingHistoryTable_Object = MibTable
tokenRingHistoryTable = _TokenRingHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1)
)
if mibBuilder.loadTexts:
    tokenRingHistoryTable.setStatus("mandatory")
_TokenRingHistoryEntry_Object = MibTableRow
tokenRingHistoryEntry = _TokenRingHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1)
)
tokenRingHistoryEntry.setIndexNames(
    (0, "Novell-LANalyzer-TR-MIB", "tokenRingHistoryIndex"),
    (0, "Novell-LANalyzer-TR-MIB", "tokenRingHistoryStartIndex"),
)
if mibBuilder.loadTexts:
    tokenRingHistoryEntry.setStatus("mandatory")


class _TokenRingHistoryIndex_Type(Integer32):
    """Custom type tokenRingHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TokenRingHistoryIndex_Type.__name__ = "Integer32"
_TokenRingHistoryIndex_Object = MibTableColumn
tokenRingHistoryIndex = _TokenRingHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 1),
    _TokenRingHistoryIndex_Type()
)
tokenRingHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryIndex.setStatus("mandatory")
_TokenRingHistoryStartIndex_Type = Integer32
_TokenRingHistoryStartIndex_Object = MibTableColumn
tokenRingHistoryStartIndex = _TokenRingHistoryStartIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 2),
    _TokenRingHistoryStartIndex_Type()
)
tokenRingHistoryStartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryStartIndex.setStatus("mandatory")
_TokenRingHistoryIntervalStart_Type = TimeTicks
_TokenRingHistoryIntervalStart_Object = MibTableColumn
tokenRingHistoryIntervalStart = _TokenRingHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 3),
    _TokenRingHistoryIntervalStart_Type()
)
tokenRingHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryIntervalStart.setStatus("mandatory")
_TokenRingHistoryDropEvents_Type = Counter32
_TokenRingHistoryDropEvents_Object = MibTableColumn
tokenRingHistoryDropEvents = _TokenRingHistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 4),
    _TokenRingHistoryDropEvents_Type()
)
tokenRingHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryDropEvents.setStatus("mandatory")
_TokenRingHistoryDataOctets_Type = Counter32
_TokenRingHistoryDataOctets_Object = MibTableColumn
tokenRingHistoryDataOctets = _TokenRingHistoryDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 5),
    _TokenRingHistoryDataOctets_Type()
)
tokenRingHistoryDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryDataOctets.setStatus("mandatory")
_TokenRingHistoryDataPkts_Type = Counter32
_TokenRingHistoryDataPkts_Object = MibTableColumn
tokenRingHistoryDataPkts = _TokenRingHistoryDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 6),
    _TokenRingHistoryDataPkts_Type()
)
tokenRingHistoryDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryDataPkts.setStatus("mandatory")
_TokenRingHistoryBroadcastDataPkts_Type = Counter32
_TokenRingHistoryBroadcastDataPkts_Object = MibTableColumn
tokenRingHistoryBroadcastDataPkts = _TokenRingHistoryBroadcastDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 7),
    _TokenRingHistoryBroadcastDataPkts_Type()
)
tokenRingHistoryBroadcastDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryBroadcastDataPkts.setStatus("mandatory")
_TokenRingHistoryMulticastDataPkts_Type = Counter32
_TokenRingHistoryMulticastDataPkts_Object = MibTableColumn
tokenRingHistoryMulticastDataPkts = _TokenRingHistoryMulticastDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 8),
    _TokenRingHistoryMulticastDataPkts_Type()
)
tokenRingHistoryMulticastDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryMulticastDataPkts.setStatus("mandatory")
_TokenRingHistoryMACOctets_Type = Counter32
_TokenRingHistoryMACOctets_Object = MibTableColumn
tokenRingHistoryMACOctets = _TokenRingHistoryMACOctets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 9),
    _TokenRingHistoryMACOctets_Type()
)
tokenRingHistoryMACOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryMACOctets.setStatus("mandatory")
_TokenRingHistoryMACPkts_Type = Counter32
_TokenRingHistoryMACPkts_Object = MibTableColumn
tokenRingHistoryMACPkts = _TokenRingHistoryMACPkts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 10),
    _TokenRingHistoryMACPkts_Type()
)
tokenRingHistoryMACPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryMACPkts.setStatus("mandatory")
_TokenRingHistoryRingPurges_Type = Counter32
_TokenRingHistoryRingPurges_Object = MibTableColumn
tokenRingHistoryRingPurges = _TokenRingHistoryRingPurges_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 11),
    _TokenRingHistoryRingPurges_Type()
)
tokenRingHistoryRingPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryRingPurges.setStatus("mandatory")
_TokenRingHistoryMonitorContentions_Type = Counter32
_TokenRingHistoryMonitorContentions_Object = MibTableColumn
tokenRingHistoryMonitorContentions = _TokenRingHistoryMonitorContentions_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 12),
    _TokenRingHistoryMonitorContentions_Type()
)
tokenRingHistoryMonitorContentions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryMonitorContentions.setStatus("mandatory")
_TokenRingHistoryBeacons_Type = Counter32
_TokenRingHistoryBeacons_Object = MibTableColumn
tokenRingHistoryBeacons = _TokenRingHistoryBeacons_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 13),
    _TokenRingHistoryBeacons_Type()
)
tokenRingHistoryBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryBeacons.setStatus("mandatory")
_TokenRingHistoryLostMonitors_Type = Counter32
_TokenRingHistoryLostMonitors_Object = MibTableColumn
tokenRingHistoryLostMonitors = _TokenRingHistoryLostMonitors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 14),
    _TokenRingHistoryLostMonitors_Type()
)
tokenRingHistoryLostMonitors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryLostMonitors.setStatus("mandatory")
_TokenRingHistoryDuplicateMonitors_Type = Counter32
_TokenRingHistoryDuplicateMonitors_Object = MibTableColumn
tokenRingHistoryDuplicateMonitors = _TokenRingHistoryDuplicateMonitors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 15),
    _TokenRingHistoryDuplicateMonitors_Type()
)
tokenRingHistoryDuplicateMonitors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryDuplicateMonitors.setStatus("mandatory")
_TokenRingHistoryDuplicateAddresses_Type = Counter32
_TokenRingHistoryDuplicateAddresses_Object = MibTableColumn
tokenRingHistoryDuplicateAddresses = _TokenRingHistoryDuplicateAddresses_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 16),
    _TokenRingHistoryDuplicateAddresses_Type()
)
tokenRingHistoryDuplicateAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryDuplicateAddresses.setStatus("mandatory")
_TokenRingHistoryRingPollFailures_Type = Counter32
_TokenRingHistoryRingPollFailures_Object = MibTableColumn
tokenRingHistoryRingPollFailures = _TokenRingHistoryRingPollFailures_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 17),
    _TokenRingHistoryRingPollFailures_Type()
)
tokenRingHistoryRingPollFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryRingPollFailures.setStatus("mandatory")
_TokenRingHistoryLineErrors_Type = Counter32
_TokenRingHistoryLineErrors_Object = MibTableColumn
tokenRingHistoryLineErrors = _TokenRingHistoryLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 18),
    _TokenRingHistoryLineErrors_Type()
)
tokenRingHistoryLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryLineErrors.setStatus("mandatory")
_TokenRingHistoryInternalErrors_Type = Counter32
_TokenRingHistoryInternalErrors_Object = MibTableColumn
tokenRingHistoryInternalErrors = _TokenRingHistoryInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 19),
    _TokenRingHistoryInternalErrors_Type()
)
tokenRingHistoryInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryInternalErrors.setStatus("mandatory")
_TokenRingHistoryBurstErrors_Type = Counter32
_TokenRingHistoryBurstErrors_Object = MibTableColumn
tokenRingHistoryBurstErrors = _TokenRingHistoryBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 20),
    _TokenRingHistoryBurstErrors_Type()
)
tokenRingHistoryBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryBurstErrors.setStatus("mandatory")
_TokenRingHistoryACErrors_Type = Counter32
_TokenRingHistoryACErrors_Object = MibTableColumn
tokenRingHistoryACErrors = _TokenRingHistoryACErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 21),
    _TokenRingHistoryACErrors_Type()
)
tokenRingHistoryACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryACErrors.setStatus("mandatory")
_TokenRingHistoryAbortDelimiters_Type = Counter32
_TokenRingHistoryAbortDelimiters_Object = MibTableColumn
tokenRingHistoryAbortDelimiters = _TokenRingHistoryAbortDelimiters_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 22),
    _TokenRingHistoryAbortDelimiters_Type()
)
tokenRingHistoryAbortDelimiters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryAbortDelimiters.setStatus("mandatory")
_TokenRingHistoryLostFrameErrors_Type = Counter32
_TokenRingHistoryLostFrameErrors_Object = MibTableColumn
tokenRingHistoryLostFrameErrors = _TokenRingHistoryLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 23),
    _TokenRingHistoryLostFrameErrors_Type()
)
tokenRingHistoryLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryLostFrameErrors.setStatus("mandatory")
_TokenRingHistoryReceiveCongestions_Type = Counter32
_TokenRingHistoryReceiveCongestions_Object = MibTableColumn
tokenRingHistoryReceiveCongestions = _TokenRingHistoryReceiveCongestions_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 24),
    _TokenRingHistoryReceiveCongestions_Type()
)
tokenRingHistoryReceiveCongestions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryReceiveCongestions.setStatus("mandatory")
_TokenRingHistoryFrameCopiedErrors_Type = Counter32
_TokenRingHistoryFrameCopiedErrors_Object = MibTableColumn
tokenRingHistoryFrameCopiedErrors = _TokenRingHistoryFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 25),
    _TokenRingHistoryFrameCopiedErrors_Type()
)
tokenRingHistoryFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryFrameCopiedErrors.setStatus("mandatory")
_TokenRingHistoryFrequencyErrors_Type = Counter32
_TokenRingHistoryFrequencyErrors_Object = MibTableColumn
tokenRingHistoryFrequencyErrors = _TokenRingHistoryFrequencyErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 26),
    _TokenRingHistoryFrequencyErrors_Type()
)
tokenRingHistoryFrequencyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryFrequencyErrors.setStatus("mandatory")
_TokenRingHistoryTokenErrors_Type = Counter32
_TokenRingHistoryTokenErrors_Object = MibTableColumn
tokenRingHistoryTokenErrors = _TokenRingHistoryTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 27),
    _TokenRingHistoryTokenErrors_Type()
)
tokenRingHistoryTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryTokenErrors.setStatus("mandatory")


class _TokenRingHistoryUtilization_Type(Integer32):
    """Custom type tokenRingHistoryUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TokenRingHistoryUtilization_Type.__name__ = "Integer32"
_TokenRingHistoryUtilization_Object = MibTableColumn
tokenRingHistoryUtilization = _TokenRingHistoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 2, 1, 1, 28),
    _TokenRingHistoryUtilization_Type()
)
tokenRingHistoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHistoryUtilization.setStatus("mandatory")
_TokenRing_ObjectIdentity = ObjectIdentity
tokenRing = _TokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3)
)
_TokenRingControlTable_Object = MibTable
tokenRingControlTable = _TokenRingControlTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 1)
)
if mibBuilder.loadTexts:
    tokenRingControlTable.setStatus("mandatory")
_TokenRingControlEntry_Object = MibTableRow
tokenRingControlEntry = _TokenRingControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 1, 1)
)
tokenRingControlEntry.setIndexNames(
    (0, "Novell-LANalyzer-TR-MIB", "tokenRingControlIndex"),
)
if mibBuilder.loadTexts:
    tokenRingControlEntry.setStatus("mandatory")


class _TokenRingControlIndex_Type(Integer32):
    """Custom type tokenRingControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TokenRingControlIndex_Type.__name__ = "Integer32"
_TokenRingControlIndex_Object = MibTableColumn
tokenRingControlIndex = _TokenRingControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 1, 1, 1),
    _TokenRingControlIndex_Type()
)
tokenRingControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingControlIndex.setStatus("mandatory")
_TokenRingControlIfIndex_Type = Integer32
_TokenRingControlIfIndex_Object = MibTableColumn
tokenRingControlIfIndex = _TokenRingControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 1, 1, 2),
    _TokenRingControlIfIndex_Type()
)
tokenRingControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingControlIfIndex.setStatus("mandatory")


class _TokenRingControlCommandStatus_Type(Integer32):
    """Custom type tokenRingControlCommandStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 7),
          ("failed", 8),
          ("inProgress", 3),
          ("missingData", 6),
          ("none", 1),
          ("notSupported", 4),
          ("sendPending", 9),
          ("success", 2),
          ("unAbleToRun", 5))
    )


_TokenRingControlCommandStatus_Type.__name__ = "Integer32"
_TokenRingControlCommandStatus_Object = MibTableColumn
tokenRingControlCommandStatus = _TokenRingControlCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 1, 1, 3),
    _TokenRingControlCommandStatus_Type()
)
tokenRingControlCommandStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingControlCommandStatus.setStatus("mandatory")


class _TokenRingControlCommandType_Type(Integer32):
    """Custom type tokenRingControlCommandType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nop", 1),
          ("removeStation", 2),
          ("requestStationAddress", 4),
          ("requestStationAttachment", 6),
          ("requestStationState", 5),
          ("testStation", 3))
    )


_TokenRingControlCommandType_Type.__name__ = "Integer32"
_TokenRingControlCommandType_Object = MibTableColumn
tokenRingControlCommandType = _TokenRingControlCommandType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 1, 1, 4),
    _TokenRingControlCommandType_Type()
)
tokenRingControlCommandType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingControlCommandType.setStatus("mandatory")
_TokenRingControlCommandTargetAddress_Type = MacAddress
_TokenRingControlCommandTargetAddress_Object = MibTableColumn
tokenRingControlCommandTargetAddress = _TokenRingControlCommandTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 1, 1, 5),
    _TokenRingControlCommandTargetAddress_Type()
)
tokenRingControlCommandTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingControlCommandTargetAddress.setStatus("mandatory")


class _TokenRingControlBeaconEventIndex_Type(Integer32):
    """Custom type tokenRingControlBeaconEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TokenRingControlBeaconEventIndex_Type.__name__ = "Integer32"
_TokenRingControlBeaconEventIndex_Object = MibTableColumn
tokenRingControlBeaconEventIndex = _TokenRingControlBeaconEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 1, 1, 6),
    _TokenRingControlBeaconEventIndex_Type()
)
tokenRingControlBeaconEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingControlBeaconEventIndex.setStatus("mandatory")


class _TokenRingControlConfigEventIndex_Type(Integer32):
    """Custom type tokenRingControlConfigEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TokenRingControlConfigEventIndex_Type.__name__ = "Integer32"
_TokenRingControlConfigEventIndex_Object = MibTableColumn
tokenRingControlConfigEventIndex = _TokenRingControlConfigEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 1, 1, 7),
    _TokenRingControlConfigEventIndex_Type()
)
tokenRingControlConfigEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingControlConfigEventIndex.setStatus("mandatory")
_TokenRingControlOwner_Type = OwnerString
_TokenRingControlOwner_Object = MibTableColumn
tokenRingControlOwner = _TokenRingControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 1, 1, 8),
    _TokenRingControlOwner_Type()
)
tokenRingControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingControlOwner.setStatus("mandatory")
_TokenRingControlStatus_Type = EntryStatus
_TokenRingControlStatus_Object = MibTableColumn
tokenRingControlStatus = _TokenRingControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 1, 1, 9),
    _TokenRingControlStatus_Type()
)
tokenRingControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingControlStatus.setStatus("mandatory")
_TokenRingNetworkTable_Object = MibTable
tokenRingNetworkTable = _TokenRingNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 2)
)
if mibBuilder.loadTexts:
    tokenRingNetworkTable.setStatus("mandatory")
_TokenRingNetworkEntry_Object = MibTableRow
tokenRingNetworkEntry = _TokenRingNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 2, 1)
)
tokenRingNetworkEntry.setIndexNames(
    (0, "Novell-LANalyzer-TR-MIB", "tokenRingNetworkIfIndex"),
)
if mibBuilder.loadTexts:
    tokenRingNetworkEntry.setStatus("mandatory")
_TokenRingNetworkIfIndex_Type = Integer32
_TokenRingNetworkIfIndex_Object = MibTableColumn
tokenRingNetworkIfIndex = _TokenRingNetworkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 2, 1, 1),
    _TokenRingNetworkIfIndex_Type()
)
tokenRingNetworkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingNetworkIfIndex.setStatus("mandatory")


class _TokenRingNetworkLastResetTime_Type(TimeTicks):
    """Custom type tokenRingNetworkLastResetTime based on TimeTicks"""
    subtypeSpec = TimeTicks.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TokenRingNetworkLastResetTime_Type.__name__ = "TimeTicks"
_TokenRingNetworkLastResetTime_Object = MibTableColumn
tokenRingNetworkLastResetTime = _TokenRingNetworkLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 2, 1, 2),
    _TokenRingNetworkLastResetTime_Type()
)
tokenRingNetworkLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingNetworkLastResetTime.setStatus("mandatory")


class _TokenRingNetworkRingNumber_Type(Integer32):
    """Custom type tokenRingNetworkRingNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TokenRingNetworkRingNumber_Type.__name__ = "Integer32"
_TokenRingNetworkRingNumber_Object = MibTableColumn
tokenRingNetworkRingNumber = _TokenRingNetworkRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 2, 1, 3),
    _TokenRingNetworkRingNumber_Type()
)
tokenRingNetworkRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingNetworkRingNumber.setStatus("mandatory")


class _TokenRingNetworkMediaSpeed_Type(Integer32):
    """Custom type tokenRingNetworkMediaSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("fourMbps", 4),
          ("sixteenMbps", 16))
    )


_TokenRingNetworkMediaSpeed_Type.__name__ = "Integer32"
_TokenRingNetworkMediaSpeed_Object = MibTableColumn
tokenRingNetworkMediaSpeed = _TokenRingNetworkMediaSpeed_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 2, 1, 4),
    _TokenRingNetworkMediaSpeed_Type()
)
tokenRingNetworkMediaSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingNetworkMediaSpeed.setStatus("mandatory")
_TokenRingNetworkBridges_Type = Integer32
_TokenRingNetworkBridges_Object = MibTableColumn
tokenRingNetworkBridges = _TokenRingNetworkBridges_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 2, 1, 5),
    _TokenRingNetworkBridges_Type()
)
tokenRingNetworkBridges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingNetworkBridges.setStatus("mandatory")
_TokenRingNetworkActiveStations_Type = Integer32
_TokenRingNetworkActiveStations_Object = MibTableColumn
tokenRingNetworkActiveStations = _TokenRingNetworkActiveStations_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 2, 1, 6),
    _TokenRingNetworkActiveStations_Type()
)
tokenRingNetworkActiveStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingNetworkActiveStations.setStatus("mandatory")
_TokenRingNetworkInactiveStations_Type = Integer32
_TokenRingNetworkInactiveStations_Object = MibTableColumn
tokenRingNetworkInactiveStations = _TokenRingNetworkInactiveStations_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 2, 1, 7),
    _TokenRingNetworkInactiveStations_Type()
)
tokenRingNetworkInactiveStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingNetworkInactiveStations.setStatus("mandatory")
_TokenRingNetworkLastEnterMACAddress_Type = MacAddress
_TokenRingNetworkLastEnterMACAddress_Object = MibTableColumn
tokenRingNetworkLastEnterMACAddress = _TokenRingNetworkLastEnterMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 2, 1, 8),
    _TokenRingNetworkLastEnterMACAddress_Type()
)
tokenRingNetworkLastEnterMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingNetworkLastEnterMACAddress.setStatus("mandatory")
_TokenRingNetworkLastExitMACAddress_Type = MacAddress
_TokenRingNetworkLastExitMACAddress_Object = MibTableColumn
tokenRingNetworkLastExitMACAddress = _TokenRingNetworkLastExitMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 2, 1, 9),
    _TokenRingNetworkLastExitMACAddress_Type()
)
tokenRingNetworkLastExitMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingNetworkLastExitMACAddress.setStatus("mandatory")


class _TokenRingNetworkState_Type(Integer32):
    """Custom type tokenRingNetworkState based on Integer32"""
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
        *(("beaconState", 4),
          ("claimTokenState", 3),
          ("normalOperation", 1),
          ("ringPurgeState", 2))
    )


_TokenRingNetworkState_Type.__name__ = "Integer32"
_TokenRingNetworkState_Object = MibTableColumn
tokenRingNetworkState = _TokenRingNetworkState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 2, 1, 10),
    _TokenRingNetworkState_Type()
)
tokenRingNetworkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingNetworkState.setStatus("mandatory")


class _TokenRingNetworkStateCause_Type(Integer32):
    """Custom type tokenRingNetworkStateCause based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("beaconBitStreaming", 8),
          ("beaconFrameStreaming", 9),
          ("beaconRingSignalLoss", 7),
          ("beaconSetRecoveryMode", 6),
          ("burst5Error", 14),
          ("circulatingFrame", 18),
          ("corruptedToken", 16),
          ("frequencyError", 21),
          ("hardError", 5),
          ("initialState", 2),
          ("lostFrameError", 15),
          ("lostMonitor", 20),
          ("lostToken", 17),
          ("multipleMonitor", 19),
          ("normalRing", 3),
          ("notClear", 1),
          ("recovering", 4),
          ("type1SoftError", 10),
          ("type2SoftError", 11),
          ("type3SoftError", 12),
          ("type4SoftError", 13))
    )


_TokenRingNetworkStateCause_Type.__name__ = "Integer32"
_TokenRingNetworkStateCause_Object = MibTableColumn
tokenRingNetworkStateCause = _TokenRingNetworkStateCause_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 2, 1, 11),
    _TokenRingNetworkStateCause_Type()
)
tokenRingNetworkStateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingNetworkStateCause.setStatus("mandatory")
_TokenRingNetworkStateSenderMACAddress_Type = MacAddress
_TokenRingNetworkStateSenderMACAddress_Object = MibTableColumn
tokenRingNetworkStateSenderMACAddress = _TokenRingNetworkStateSenderMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 2, 1, 12),
    _TokenRingNetworkStateSenderMACAddress_Type()
)
tokenRingNetworkStateSenderMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingNetworkStateSenderMACAddress.setStatus("mandatory")
_TokenRingNetworkStateUpstreamNeighborMACAddress_Type = MacAddress
_TokenRingNetworkStateUpstreamNeighborMACAddress_Object = MibTableColumn
tokenRingNetworkStateUpstreamNeighborMACAddress = _TokenRingNetworkStateUpstreamNeighborMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 2, 1, 13),
    _TokenRingNetworkStateUpstreamNeighborMACAddress_Type()
)
tokenRingNetworkStateUpstreamNeighborMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingNetworkStateUpstreamNeighborMACAddress.setStatus("mandatory")


class _TokenRingNetworkHostOrderChanges_Type(Counter32):
    """Custom type tokenRingNetworkHostOrderChanges based on Counter32"""
    defaultValue = 0


_TokenRingNetworkHostOrderChanges_Object = MibTableColumn
tokenRingNetworkHostOrderChanges = _TokenRingNetworkHostOrderChanges_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 2, 1, 14),
    _TokenRingNetworkHostOrderChanges_Type()
)
tokenRingNetworkHostOrderChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingNetworkHostOrderChanges.setStatus("mandatory")


class _TokenRingNetworkActiveMonitorChanges_Type(Counter32):
    """Custom type tokenRingNetworkActiveMonitorChanges based on Counter32"""
    defaultValue = 0


_TokenRingNetworkActiveMonitorChanges_Object = MibTableColumn
tokenRingNetworkActiveMonitorChanges = _TokenRingNetworkActiveMonitorChanges_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 2, 1, 15),
    _TokenRingNetworkActiveMonitorChanges_Type()
)
tokenRingNetworkActiveMonitorChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingNetworkActiveMonitorChanges.setStatus("mandatory")
_TokenRingHostTable_Object = MibTable
tokenRingHostTable = _TokenRingHostTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3)
)
if mibBuilder.loadTexts:
    tokenRingHostTable.setStatus("mandatory")
_TokenRingHostEntry_Object = MibTableRow
tokenRingHostEntry = _TokenRingHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1)
)
tokenRingHostEntry.setIndexNames(
    (0, "Novell-LANalyzer-TR-MIB", "tokenRingHostIfIndex"),
    (0, "Novell-LANalyzer-TR-MIB", "tokenRingHostMACAddress"),
)
if mibBuilder.loadTexts:
    tokenRingHostEntry.setStatus("mandatory")
_TokenRingHostIfIndex_Type = Integer32
_TokenRingHostIfIndex_Object = MibTableColumn
tokenRingHostIfIndex = _TokenRingHostIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 1),
    _TokenRingHostIfIndex_Type()
)
tokenRingHostIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostIfIndex.setStatus("mandatory")


class _TokenRingHostIndex_Type(Integer32):
    """Custom type tokenRingHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TokenRingHostIndex_Type.__name__ = "Integer32"
_TokenRingHostIndex_Object = MibTableColumn
tokenRingHostIndex = _TokenRingHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 2),
    _TokenRingHostIndex_Type()
)
tokenRingHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostIndex.setStatus("mandatory")


class _TokenRingHostStatus_Type(Integer32):
    """Custom type tokenRingHostStatus based on Integer32"""
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
          ("activeMonitor", 3),
          ("inactive", 2))
    )


_TokenRingHostStatus_Type.__name__ = "Integer32"
_TokenRingHostStatus_Object = MibTableColumn
tokenRingHostStatus = _TokenRingHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 3),
    _TokenRingHostStatus_Type()
)
tokenRingHostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostStatus.setStatus("mandatory")
_TokenRingHostLastEnterTime_Type = TimeTicks
_TokenRingHostLastEnterTime_Object = MibTableColumn
tokenRingHostLastEnterTime = _TokenRingHostLastEnterTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 4),
    _TokenRingHostLastEnterTime_Type()
)
tokenRingHostLastEnterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostLastEnterTime.setStatus("mandatory")


class _TokenRingHostLastExitTime_Type(TimeTicks):
    """Custom type tokenRingHostLastExitTime based on TimeTicks"""
    defaultValue = 0


_TokenRingHostLastExitTime_Object = MibTableColumn
tokenRingHostLastExitTime = _TokenRingHostLastExitTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 5),
    _TokenRingHostLastExitTime_Type()
)
tokenRingHostLastExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostLastExitTime.setStatus("mandatory")
_TokenRingHostMACAddress_Type = MacAddress
_TokenRingHostMACAddress_Object = MibTableColumn
tokenRingHostMACAddress = _TokenRingHostMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 6),
    _TokenRingHostMACAddress_Type()
)
tokenRingHostMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostMACAddress.setStatus("mandatory")
_TokenRingHostPhysicalDropNumber_Type = OctetString
_TokenRingHostPhysicalDropNumber_Object = MibTableColumn
tokenRingHostPhysicalDropNumber = _TokenRingHostPhysicalDropNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 7),
    _TokenRingHostPhysicalDropNumber_Type()
)
tokenRingHostPhysicalDropNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostPhysicalDropNumber.setStatus("mandatory")


class _TokenRingHostSoftErrorReportTimerValue_Type(Integer32):
    """Custom type tokenRingHostSoftErrorReportTimerValue based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TokenRingHostSoftErrorReportTimerValue_Type.__name__ = "Integer32"
_TokenRingHostSoftErrorReportTimerValue_Object = MibTableColumn
tokenRingHostSoftErrorReportTimerValue = _TokenRingHostSoftErrorReportTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 8),
    _TokenRingHostSoftErrorReportTimerValue_Type()
)
tokenRingHostSoftErrorReportTimerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostSoftErrorReportTimerValue.setStatus("mandatory")
_TokenRingHostGroupAddresses_Type = Integer32
_TokenRingHostGroupAddresses_Object = MibTableColumn
tokenRingHostGroupAddresses = _TokenRingHostGroupAddresses_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 9),
    _TokenRingHostGroupAddresses_Type()
)
tokenRingHostGroupAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostGroupAddresses.setStatus("mandatory")
_TokenRingHostFunctionalAddresses_Type = Integer32
_TokenRingHostFunctionalAddresses_Object = MibTableColumn
tokenRingHostFunctionalAddresses = _TokenRingHostFunctionalAddresses_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 10),
    _TokenRingHostFunctionalAddresses_Type()
)
tokenRingHostFunctionalAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostFunctionalAddresses.setStatus("mandatory")


class _TokenRingHostAuthorizedFunctionClass_Type(Integer32):
    """Custom type tokenRingHostAuthorizedFunctionClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TokenRingHostAuthorizedFunctionClass_Type.__name__ = "Integer32"
_TokenRingHostAuthorizedFunctionClass_Object = MibTableColumn
tokenRingHostAuthorizedFunctionClass = _TokenRingHostAuthorizedFunctionClass_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 11),
    _TokenRingHostAuthorizedFunctionClass_Type()
)
tokenRingHostAuthorizedFunctionClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostAuthorizedFunctionClass.setStatus("mandatory")


class _TokenRingHostAuthorizedAccessPriority_Type(Integer32):
    """Custom type tokenRingHostAuthorizedAccessPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TokenRingHostAuthorizedAccessPriority_Type.__name__ = "Integer32"
_TokenRingHostAuthorizedAccessPriority_Object = MibTableColumn
tokenRingHostAuthorizedAccessPriority = _TokenRingHostAuthorizedAccessPriority_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 12),
    _TokenRingHostAuthorizedAccessPriority_Type()
)
tokenRingHostAuthorizedAccessPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostAuthorizedAccessPriority.setStatus("mandatory")
_TokenRingHostAdapterSoftwareLevel_Type = OctetString
_TokenRingHostAdapterSoftwareLevel_Object = MibTableColumn
tokenRingHostAdapterSoftwareLevel = _TokenRingHostAdapterSoftwareLevel_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 13),
    _TokenRingHostAdapterSoftwareLevel_Type()
)
tokenRingHostAdapterSoftwareLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostAdapterSoftwareLevel.setStatus("mandatory")
_TokenRingHostAdapterStatusVector_Type = OctetString
_TokenRingHostAdapterStatusVector_Object = MibTableColumn
tokenRingHostAdapterStatusVector = _TokenRingHostAdapterStatusVector_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 14),
    _TokenRingHostAdapterStatusVector_Type()
)
tokenRingHostAdapterStatusVector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostAdapterStatusVector.setStatus("mandatory")
_TokenRingHostProductID_Type = OctetString
_TokenRingHostProductID_Object = MibTableColumn
tokenRingHostProductID = _TokenRingHostProductID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 15),
    _TokenRingHostProductID_Type()
)
tokenRingHostProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostProductID.setStatus("mandatory")
_TokenRingHostLostMonitors_Type = Counter32
_TokenRingHostLostMonitors_Object = MibTableColumn
tokenRingHostLostMonitors = _TokenRingHostLostMonitors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 16),
    _TokenRingHostLostMonitors_Type()
)
tokenRingHostLostMonitors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostLostMonitors.setStatus("mandatory")
_TokenRingHostDuplicateMonitors_Type = Counter32
_TokenRingHostDuplicateMonitors_Object = MibTableColumn
tokenRingHostDuplicateMonitors = _TokenRingHostDuplicateMonitors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 17),
    _TokenRingHostDuplicateMonitors_Type()
)
tokenRingHostDuplicateMonitors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostDuplicateMonitors.setStatus("mandatory")
_TokenRingHostDuplicateAddresses_Type = Counter32
_TokenRingHostDuplicateAddresses_Object = MibTableColumn
tokenRingHostDuplicateAddresses = _TokenRingHostDuplicateAddresses_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 18),
    _TokenRingHostDuplicateAddresses_Type()
)
tokenRingHostDuplicateAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostDuplicateAddresses.setStatus("mandatory")
_TokenRingHostRingPollFailures_Type = Counter32
_TokenRingHostRingPollFailures_Object = MibTableColumn
tokenRingHostRingPollFailures = _TokenRingHostRingPollFailures_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 19),
    _TokenRingHostRingPollFailures_Type()
)
tokenRingHostRingPollFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostRingPollFailures.setStatus("mandatory")
_TokenRingHostInLineErrors_Type = Counter32
_TokenRingHostInLineErrors_Object = MibTableColumn
tokenRingHostInLineErrors = _TokenRingHostInLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 20),
    _TokenRingHostInLineErrors_Type()
)
tokenRingHostInLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostInLineErrors.setStatus("mandatory")
_TokenRingHostInternalErrors_Type = Counter32
_TokenRingHostInternalErrors_Object = MibTableColumn
tokenRingHostInternalErrors = _TokenRingHostInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 21),
    _TokenRingHostInternalErrors_Type()
)
tokenRingHostInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostInternalErrors.setStatus("mandatory")
_TokenRingHostInBurstErrors_Type = Counter32
_TokenRingHostInBurstErrors_Object = MibTableColumn
tokenRingHostInBurstErrors = _TokenRingHostInBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 22),
    _TokenRingHostInBurstErrors_Type()
)
tokenRingHostInBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostInBurstErrors.setStatus("mandatory")
_TokenRingHostACErrors_Type = Counter32
_TokenRingHostACErrors_Object = MibTableColumn
tokenRingHostACErrors = _TokenRingHostACErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 23),
    _TokenRingHostACErrors_Type()
)
tokenRingHostACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostACErrors.setStatus("mandatory")
_TokenRingHostAbortDelimiters_Type = Counter32
_TokenRingHostAbortDelimiters_Object = MibTableColumn
tokenRingHostAbortDelimiters = _TokenRingHostAbortDelimiters_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 24),
    _TokenRingHostAbortDelimiters_Type()
)
tokenRingHostAbortDelimiters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostAbortDelimiters.setStatus("mandatory")
_TokenRingHostLostFrameErrors_Type = Counter32
_TokenRingHostLostFrameErrors_Object = MibTableColumn
tokenRingHostLostFrameErrors = _TokenRingHostLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 25),
    _TokenRingHostLostFrameErrors_Type()
)
tokenRingHostLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostLostFrameErrors.setStatus("mandatory")
_TokenRingHostReceiveCongestions_Type = Counter32
_TokenRingHostReceiveCongestions_Object = MibTableColumn
tokenRingHostReceiveCongestions = _TokenRingHostReceiveCongestions_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 26),
    _TokenRingHostReceiveCongestions_Type()
)
tokenRingHostReceiveCongestions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostReceiveCongestions.setStatus("mandatory")
_TokenRingHostFrameCopiedErrors_Type = Counter32
_TokenRingHostFrameCopiedErrors_Object = MibTableColumn
tokenRingHostFrameCopiedErrors = _TokenRingHostFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 27),
    _TokenRingHostFrameCopiedErrors_Type()
)
tokenRingHostFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostFrameCopiedErrors.setStatus("mandatory")
_TokenRingHostFrequencyErrors_Type = Counter32
_TokenRingHostFrequencyErrors_Object = MibTableColumn
tokenRingHostFrequencyErrors = _TokenRingHostFrequencyErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 28),
    _TokenRingHostFrequencyErrors_Type()
)
tokenRingHostFrequencyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostFrequencyErrors.setStatus("mandatory")
_TokenRingHostTokenErrors_Type = Counter32
_TokenRingHostTokenErrors_Object = MibTableColumn
tokenRingHostTokenErrors = _TokenRingHostTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 29),
    _TokenRingHostTokenErrors_Type()
)
tokenRingHostTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostTokenErrors.setStatus("mandatory")
_TokenRingHostOutLineErrors_Type = Counter32
_TokenRingHostOutLineErrors_Object = MibTableColumn
tokenRingHostOutLineErrors = _TokenRingHostOutLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 30),
    _TokenRingHostOutLineErrors_Type()
)
tokenRingHostOutLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostOutLineErrors.setStatus("mandatory")
_TokenRingHostOutBurstErrors_Type = Counter32
_TokenRingHostOutBurstErrors_Object = MibTableColumn
tokenRingHostOutBurstErrors = _TokenRingHostOutBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 31),
    _TokenRingHostOutBurstErrors_Type()
)
tokenRingHostOutBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostOutBurstErrors.setStatus("mandatory")
_TokenRingHostInBeacons_Type = Counter32
_TokenRingHostInBeacons_Object = MibTableColumn
tokenRingHostInBeacons = _TokenRingHostInBeacons_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 32),
    _TokenRingHostInBeacons_Type()
)
tokenRingHostInBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostInBeacons.setStatus("mandatory")
_TokenRingHostOutBeacons_Type = Counter32
_TokenRingHostOutBeacons_Object = MibTableColumn
tokenRingHostOutBeacons = _TokenRingHostOutBeacons_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 33),
    _TokenRingHostOutBeacons_Type()
)
tokenRingHostOutBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostOutBeacons.setStatus("mandatory")
_TokenRingHostInsertions_Type = Counter32
_TokenRingHostInsertions_Object = MibTableColumn
tokenRingHostInsertions = _TokenRingHostInsertions_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 3, 1, 34),
    _TokenRingHostInsertions_Type()
)
tokenRingHostInsertions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingHostInsertions.setStatus("mandatory")
_TokenRingOrderTable_Object = MibTable
tokenRingOrderTable = _TokenRingOrderTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4)
)
if mibBuilder.loadTexts:
    tokenRingOrderTable.setStatus("mandatory")
_TokenRingOrderEntry_Object = MibTableRow
tokenRingOrderEntry = _TokenRingOrderEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1)
)
tokenRingOrderEntry.setIndexNames(
    (0, "Novell-LANalyzer-TR-MIB", "tokenRingOrderIfIndex"),
    (0, "Novell-LANalyzer-TR-MIB", "tokenRingOrderIndex"),
)
if mibBuilder.loadTexts:
    tokenRingOrderEntry.setStatus("mandatory")
_TokenRingOrderIfIndex_Type = Integer32
_TokenRingOrderIfIndex_Object = MibTableColumn
tokenRingOrderIfIndex = _TokenRingOrderIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 1),
    _TokenRingOrderIfIndex_Type()
)
tokenRingOrderIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderIfIndex.setStatus("mandatory")


class _TokenRingOrderIndex_Type(Integer32):
    """Custom type tokenRingOrderIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TokenRingOrderIndex_Type.__name__ = "Integer32"
_TokenRingOrderIndex_Object = MibTableColumn
tokenRingOrderIndex = _TokenRingOrderIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 2),
    _TokenRingOrderIndex_Type()
)
tokenRingOrderIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderIndex.setStatus("mandatory")


class _TokenRingOrderStatus_Type(Integer32):
    """Custom type tokenRingOrderStatus based on Integer32"""
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
          ("activeMonitor", 3),
          ("inactive", 2))
    )


_TokenRingOrderStatus_Type.__name__ = "Integer32"
_TokenRingOrderStatus_Object = MibTableColumn
tokenRingOrderStatus = _TokenRingOrderStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 3),
    _TokenRingOrderStatus_Type()
)
tokenRingOrderStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderStatus.setStatus("mandatory")
_TokenRingOrderLastEnterTime_Type = TimeTicks
_TokenRingOrderLastEnterTime_Object = MibTableColumn
tokenRingOrderLastEnterTime = _TokenRingOrderLastEnterTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 4),
    _TokenRingOrderLastEnterTime_Type()
)
tokenRingOrderLastEnterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderLastEnterTime.setStatus("mandatory")


class _TokenRingOrderLastExitTime_Type(TimeTicks):
    """Custom type tokenRingOrderLastExitTime based on TimeTicks"""
    defaultValue = 0


_TokenRingOrderLastExitTime_Object = MibTableColumn
tokenRingOrderLastExitTime = _TokenRingOrderLastExitTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 5),
    _TokenRingOrderLastExitTime_Type()
)
tokenRingOrderLastExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderLastExitTime.setStatus("mandatory")
_TokenRingOrderMACAddress_Type = MacAddress
_TokenRingOrderMACAddress_Object = MibTableColumn
tokenRingOrderMACAddress = _TokenRingOrderMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 6),
    _TokenRingOrderMACAddress_Type()
)
tokenRingOrderMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderMACAddress.setStatus("mandatory")
_TokenRingOrderPhysicalDropNumber_Type = OctetString
_TokenRingOrderPhysicalDropNumber_Object = MibTableColumn
tokenRingOrderPhysicalDropNumber = _TokenRingOrderPhysicalDropNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 7),
    _TokenRingOrderPhysicalDropNumber_Type()
)
tokenRingOrderPhysicalDropNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderPhysicalDropNumber.setStatus("mandatory")


class _TokenRingOrderSoftErrorReportTimerValue_Type(Integer32):
    """Custom type tokenRingOrderSoftErrorReportTimerValue based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TokenRingOrderSoftErrorReportTimerValue_Type.__name__ = "Integer32"
_TokenRingOrderSoftErrorReportTimerValue_Object = MibTableColumn
tokenRingOrderSoftErrorReportTimerValue = _TokenRingOrderSoftErrorReportTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 8),
    _TokenRingOrderSoftErrorReportTimerValue_Type()
)
tokenRingOrderSoftErrorReportTimerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderSoftErrorReportTimerValue.setStatus("mandatory")
_TokenRingOrderGroupAddresses_Type = Integer32
_TokenRingOrderGroupAddresses_Object = MibTableColumn
tokenRingOrderGroupAddresses = _TokenRingOrderGroupAddresses_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 9),
    _TokenRingOrderGroupAddresses_Type()
)
tokenRingOrderGroupAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderGroupAddresses.setStatus("mandatory")
_TokenRingOrderFunctionalAddresses_Type = Integer32
_TokenRingOrderFunctionalAddresses_Object = MibTableColumn
tokenRingOrderFunctionalAddresses = _TokenRingOrderFunctionalAddresses_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 10),
    _TokenRingOrderFunctionalAddresses_Type()
)
tokenRingOrderFunctionalAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderFunctionalAddresses.setStatus("mandatory")


class _TokenRingOrderAuthorizedFunctionClass_Type(Integer32):
    """Custom type tokenRingOrderAuthorizedFunctionClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TokenRingOrderAuthorizedFunctionClass_Type.__name__ = "Integer32"
_TokenRingOrderAuthorizedFunctionClass_Object = MibTableColumn
tokenRingOrderAuthorizedFunctionClass = _TokenRingOrderAuthorizedFunctionClass_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 11),
    _TokenRingOrderAuthorizedFunctionClass_Type()
)
tokenRingOrderAuthorizedFunctionClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderAuthorizedFunctionClass.setStatus("mandatory")


class _TokenRingOrderAuthorizedAccessPriority_Type(Integer32):
    """Custom type tokenRingOrderAuthorizedAccessPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TokenRingOrderAuthorizedAccessPriority_Type.__name__ = "Integer32"
_TokenRingOrderAuthorizedAccessPriority_Object = MibTableColumn
tokenRingOrderAuthorizedAccessPriority = _TokenRingOrderAuthorizedAccessPriority_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 12),
    _TokenRingOrderAuthorizedAccessPriority_Type()
)
tokenRingOrderAuthorizedAccessPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderAuthorizedAccessPriority.setStatus("mandatory")
_TokenRingOrderAdapterSoftwareLevel_Type = OctetString
_TokenRingOrderAdapterSoftwareLevel_Object = MibTableColumn
tokenRingOrderAdapterSoftwareLevel = _TokenRingOrderAdapterSoftwareLevel_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 13),
    _TokenRingOrderAdapterSoftwareLevel_Type()
)
tokenRingOrderAdapterSoftwareLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderAdapterSoftwareLevel.setStatus("mandatory")
_TokenRingOrderAdapterStatusVector_Type = OctetString
_TokenRingOrderAdapterStatusVector_Object = MibTableColumn
tokenRingOrderAdapterStatusVector = _TokenRingOrderAdapterStatusVector_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 14),
    _TokenRingOrderAdapterStatusVector_Type()
)
tokenRingOrderAdapterStatusVector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderAdapterStatusVector.setStatus("mandatory")
_TokenRingOrderProductID_Type = OctetString
_TokenRingOrderProductID_Object = MibTableColumn
tokenRingOrderProductID = _TokenRingOrderProductID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 15),
    _TokenRingOrderProductID_Type()
)
tokenRingOrderProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderProductID.setStatus("mandatory")
_TokenRingOrderLostMonitors_Type = Counter32
_TokenRingOrderLostMonitors_Object = MibTableColumn
tokenRingOrderLostMonitors = _TokenRingOrderLostMonitors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 16),
    _TokenRingOrderLostMonitors_Type()
)
tokenRingOrderLostMonitors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderLostMonitors.setStatus("mandatory")
_TokenRingOrderDuplicateMonitors_Type = Counter32
_TokenRingOrderDuplicateMonitors_Object = MibTableColumn
tokenRingOrderDuplicateMonitors = _TokenRingOrderDuplicateMonitors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 17),
    _TokenRingOrderDuplicateMonitors_Type()
)
tokenRingOrderDuplicateMonitors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderDuplicateMonitors.setStatus("mandatory")
_TokenRingOrderDuplicateAddresses_Type = Counter32
_TokenRingOrderDuplicateAddresses_Object = MibTableColumn
tokenRingOrderDuplicateAddresses = _TokenRingOrderDuplicateAddresses_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 18),
    _TokenRingOrderDuplicateAddresses_Type()
)
tokenRingOrderDuplicateAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderDuplicateAddresses.setStatus("mandatory")
_TokenRingOrderRingPollFailures_Type = Counter32
_TokenRingOrderRingPollFailures_Object = MibTableColumn
tokenRingOrderRingPollFailures = _TokenRingOrderRingPollFailures_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 19),
    _TokenRingOrderRingPollFailures_Type()
)
tokenRingOrderRingPollFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderRingPollFailures.setStatus("mandatory")
_TokenRingOrderInLineErrors_Type = Counter32
_TokenRingOrderInLineErrors_Object = MibTableColumn
tokenRingOrderInLineErrors = _TokenRingOrderInLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 20),
    _TokenRingOrderInLineErrors_Type()
)
tokenRingOrderInLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderInLineErrors.setStatus("mandatory")
_TokenRingOrderInternalErrors_Type = Counter32
_TokenRingOrderInternalErrors_Object = MibTableColumn
tokenRingOrderInternalErrors = _TokenRingOrderInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 21),
    _TokenRingOrderInternalErrors_Type()
)
tokenRingOrderInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderInternalErrors.setStatus("mandatory")
_TokenRingOrderInBurstErrors_Type = Counter32
_TokenRingOrderInBurstErrors_Object = MibTableColumn
tokenRingOrderInBurstErrors = _TokenRingOrderInBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 22),
    _TokenRingOrderInBurstErrors_Type()
)
tokenRingOrderInBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderInBurstErrors.setStatus("mandatory")
_TokenRingOrderACErrors_Type = Counter32
_TokenRingOrderACErrors_Object = MibTableColumn
tokenRingOrderACErrors = _TokenRingOrderACErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 23),
    _TokenRingOrderACErrors_Type()
)
tokenRingOrderACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderACErrors.setStatus("mandatory")
_TokenRingOrderAbortDelimiters_Type = Counter32
_TokenRingOrderAbortDelimiters_Object = MibTableColumn
tokenRingOrderAbortDelimiters = _TokenRingOrderAbortDelimiters_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 24),
    _TokenRingOrderAbortDelimiters_Type()
)
tokenRingOrderAbortDelimiters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderAbortDelimiters.setStatus("mandatory")
_TokenRingOrderLostFrameErrors_Type = Counter32
_TokenRingOrderLostFrameErrors_Object = MibTableColumn
tokenRingOrderLostFrameErrors = _TokenRingOrderLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 25),
    _TokenRingOrderLostFrameErrors_Type()
)
tokenRingOrderLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderLostFrameErrors.setStatus("mandatory")
_TokenRingOrderReceiveCongestions_Type = Counter32
_TokenRingOrderReceiveCongestions_Object = MibTableColumn
tokenRingOrderReceiveCongestions = _TokenRingOrderReceiveCongestions_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 26),
    _TokenRingOrderReceiveCongestions_Type()
)
tokenRingOrderReceiveCongestions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderReceiveCongestions.setStatus("mandatory")
_TokenRingOrderFrameCopiedErrors_Type = Counter32
_TokenRingOrderFrameCopiedErrors_Object = MibTableColumn
tokenRingOrderFrameCopiedErrors = _TokenRingOrderFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 27),
    _TokenRingOrderFrameCopiedErrors_Type()
)
tokenRingOrderFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderFrameCopiedErrors.setStatus("mandatory")
_TokenRingOrderFrequencyErrors_Type = Counter32
_TokenRingOrderFrequencyErrors_Object = MibTableColumn
tokenRingOrderFrequencyErrors = _TokenRingOrderFrequencyErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 28),
    _TokenRingOrderFrequencyErrors_Type()
)
tokenRingOrderFrequencyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderFrequencyErrors.setStatus("mandatory")
_TokenRingOrderTokenErrors_Type = Counter32
_TokenRingOrderTokenErrors_Object = MibTableColumn
tokenRingOrderTokenErrors = _TokenRingOrderTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 29),
    _TokenRingOrderTokenErrors_Type()
)
tokenRingOrderTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderTokenErrors.setStatus("mandatory")
_TokenRingOrderOutLineErrors_Type = Counter32
_TokenRingOrderOutLineErrors_Object = MibTableColumn
tokenRingOrderOutLineErrors = _TokenRingOrderOutLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 30),
    _TokenRingOrderOutLineErrors_Type()
)
tokenRingOrderOutLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderOutLineErrors.setStatus("mandatory")
_TokenRingOrderOutBurstErrors_Type = Counter32
_TokenRingOrderOutBurstErrors_Object = MibTableColumn
tokenRingOrderOutBurstErrors = _TokenRingOrderOutBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 31),
    _TokenRingOrderOutBurstErrors_Type()
)
tokenRingOrderOutBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderOutBurstErrors.setStatus("mandatory")
_TokenRingOrderInBeacons_Type = Counter32
_TokenRingOrderInBeacons_Object = MibTableColumn
tokenRingOrderInBeacons = _TokenRingOrderInBeacons_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 32),
    _TokenRingOrderInBeacons_Type()
)
tokenRingOrderInBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderInBeacons.setStatus("mandatory")
_TokenRingOrderOutBeacons_Type = Counter32
_TokenRingOrderOutBeacons_Object = MibTableColumn
tokenRingOrderOutBeacons = _TokenRingOrderOutBeacons_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 33),
    _TokenRingOrderOutBeacons_Type()
)
tokenRingOrderOutBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderOutBeacons.setStatus("mandatory")
_TokenRingOrderInsertions_Type = Counter32
_TokenRingOrderInsertions_Object = MibTableColumn
tokenRingOrderInsertions = _TokenRingOrderInsertions_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 3, 4, 1, 34),
    _TokenRingOrderInsertions_Type()
)
tokenRingOrderInsertions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingOrderInsertions.setStatus("mandatory")

# Managed Objects groups


# Notification objects

tokenRingBeaconing = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 0, 4)
)
tokenRingBeaconing.setObjects(
      *(("Novell-LANalyzer-TR-MIB", "tokenRingNetworkRingNumber"),
        ("Novell-LANalyzer-TR-MIB", "tokenRingNetworkState"),
        ("Novell-LANalyzer-TR-MIB", "tokenRingNetworkStateCause"),
        ("Novell-LANalyzer-TR-MIB", "tokenRingNetworkStateSenderMACAddress"),
        ("Novell-LANalyzer-TR-MIB", "tokenRingNetworkStateUpstreamNeighborMACAddress"))
)
if mibBuilder.loadTexts:
    tokenRingBeaconing.setStatus(
        ""
    )

tokenRingConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 15, 0, 5)
)
tokenRingConfigurationChange.setObjects(
      *(("Novell-LANalyzer-TR-MIB", "tokenRingNetworkRingNumber"),
        ("Novell-LANalyzer-TR-MIB", "tokenRingHostMACAddress"),
        ("Novell-LANalyzer-TR-MIB", "tokenRingHostPhysicalDropNumber"),
        ("Novell-LANalyzer-TR-MIB", "tokenRingHostStatus"))
)
if mibBuilder.loadTexts:
    tokenRingConfigurationChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Novell-LANalyzer-TR-MIB",
    **{"MacAddress": MacAddress,
       "novell": novell,
       "productType": productType,
       "mibDoc": mibDoc,
       "ringrmon-mib": ringrmon_mib,
       "tokenRingBeaconing": tokenRingBeaconing,
       "tokenRingConfigurationChange": tokenRingConfigurationChange,
       "tokenRingStatistics": tokenRingStatistics,
       "tokenRingStatsTable": tokenRingStatsTable,
       "tokenRingStatsEntry": tokenRingStatsEntry,
       "tokenRingStatsIndex": tokenRingStatsIndex,
       "tokenRingStatsDataSource": tokenRingStatsDataSource,
       "tokenRingStatsDropEvents": tokenRingStatsDropEvents,
       "tokenRingStatsDataOctets": tokenRingStatsDataOctets,
       "tokenRingStatsDataPkts": tokenRingStatsDataPkts,
       "tokenRingStatsBroadcastDataPkts": tokenRingStatsBroadcastDataPkts,
       "tokenRingStatsMulticastDataPkts": tokenRingStatsMulticastDataPkts,
       "tokenRingStatsMACOctets": tokenRingStatsMACOctets,
       "tokenRingStatsMACPkts": tokenRingStatsMACPkts,
       "tokenRingStatsRingPurges": tokenRingStatsRingPurges,
       "tokenRingStatsMonitorContentions": tokenRingStatsMonitorContentions,
       "tokenRingStatsBeacons": tokenRingStatsBeacons,
       "tokenRingStatsLostMonitors": tokenRingStatsLostMonitors,
       "tokenRingStatsDuplicateMonitors": tokenRingStatsDuplicateMonitors,
       "tokenRingStatsDuplicateAddresses": tokenRingStatsDuplicateAddresses,
       "tokenRingStatsRingPollFailures": tokenRingStatsRingPollFailures,
       "tokenRingStatsLineErrors": tokenRingStatsLineErrors,
       "tokenRingStatsInternalErrors": tokenRingStatsInternalErrors,
       "tokenRingStatsBurstErrors": tokenRingStatsBurstErrors,
       "tokenRingStatsACErrors": tokenRingStatsACErrors,
       "tokenRingStatsAbortDelimiters": tokenRingStatsAbortDelimiters,
       "tokenRingStatsLostFrameErrors": tokenRingStatsLostFrameErrors,
       "tokenRingStatsReceiveCongestions": tokenRingStatsReceiveCongestions,
       "tokenRingStatsFrameCopiedErrors": tokenRingStatsFrameCopiedErrors,
       "tokenRingStatsFrequencyErrors": tokenRingStatsFrequencyErrors,
       "tokenRingStatsTokenErrors": tokenRingStatsTokenErrors,
       "tokenRingStatsDataPktsUndersizePkts": tokenRingStatsDataPktsUndersizePkts,
       "tokenRingStatsDataPkts18to63Octets": tokenRingStatsDataPkts18to63Octets,
       "tokenRingStatsDataPkts64to127Octets": tokenRingStatsDataPkts64to127Octets,
       "tokenRingStatsDataPkts128to255Octets": tokenRingStatsDataPkts128to255Octets,
       "tokenRingStatsDataPkts256to511Octets": tokenRingStatsDataPkts256to511Octets,
       "tokenRingStatsDataPkts512to1023Octets": tokenRingStatsDataPkts512to1023Octets,
       "tokenRingStatsDataPkts1024to2047Octets": tokenRingStatsDataPkts1024to2047Octets,
       "tokenRingStatsDataPkts2048to4608Octets": tokenRingStatsDataPkts2048to4608Octets,
       "tokenRingStatsDataPkts4609to18000Octets": tokenRingStatsDataPkts4609to18000Octets,
       "tokenRingStatsDataPktsMoreThan18000Octets": tokenRingStatsDataPktsMoreThan18000Octets,
       "tokenRingStatsOwner": tokenRingStatsOwner,
       "tokenRingStatsStatus": tokenRingStatsStatus,
       "tokenRingHistory": tokenRingHistory,
       "tokenRingHistoryTable": tokenRingHistoryTable,
       "tokenRingHistoryEntry": tokenRingHistoryEntry,
       "tokenRingHistoryIndex": tokenRingHistoryIndex,
       "tokenRingHistoryStartIndex": tokenRingHistoryStartIndex,
       "tokenRingHistoryIntervalStart": tokenRingHistoryIntervalStart,
       "tokenRingHistoryDropEvents": tokenRingHistoryDropEvents,
       "tokenRingHistoryDataOctets": tokenRingHistoryDataOctets,
       "tokenRingHistoryDataPkts": tokenRingHistoryDataPkts,
       "tokenRingHistoryBroadcastDataPkts": tokenRingHistoryBroadcastDataPkts,
       "tokenRingHistoryMulticastDataPkts": tokenRingHistoryMulticastDataPkts,
       "tokenRingHistoryMACOctets": tokenRingHistoryMACOctets,
       "tokenRingHistoryMACPkts": tokenRingHistoryMACPkts,
       "tokenRingHistoryRingPurges": tokenRingHistoryRingPurges,
       "tokenRingHistoryMonitorContentions": tokenRingHistoryMonitorContentions,
       "tokenRingHistoryBeacons": tokenRingHistoryBeacons,
       "tokenRingHistoryLostMonitors": tokenRingHistoryLostMonitors,
       "tokenRingHistoryDuplicateMonitors": tokenRingHistoryDuplicateMonitors,
       "tokenRingHistoryDuplicateAddresses": tokenRingHistoryDuplicateAddresses,
       "tokenRingHistoryRingPollFailures": tokenRingHistoryRingPollFailures,
       "tokenRingHistoryLineErrors": tokenRingHistoryLineErrors,
       "tokenRingHistoryInternalErrors": tokenRingHistoryInternalErrors,
       "tokenRingHistoryBurstErrors": tokenRingHistoryBurstErrors,
       "tokenRingHistoryACErrors": tokenRingHistoryACErrors,
       "tokenRingHistoryAbortDelimiters": tokenRingHistoryAbortDelimiters,
       "tokenRingHistoryLostFrameErrors": tokenRingHistoryLostFrameErrors,
       "tokenRingHistoryReceiveCongestions": tokenRingHistoryReceiveCongestions,
       "tokenRingHistoryFrameCopiedErrors": tokenRingHistoryFrameCopiedErrors,
       "tokenRingHistoryFrequencyErrors": tokenRingHistoryFrequencyErrors,
       "tokenRingHistoryTokenErrors": tokenRingHistoryTokenErrors,
       "tokenRingHistoryUtilization": tokenRingHistoryUtilization,
       "tokenRing": tokenRing,
       "tokenRingControlTable": tokenRingControlTable,
       "tokenRingControlEntry": tokenRingControlEntry,
       "tokenRingControlIndex": tokenRingControlIndex,
       "tokenRingControlIfIndex": tokenRingControlIfIndex,
       "tokenRingControlCommandStatus": tokenRingControlCommandStatus,
       "tokenRingControlCommandType": tokenRingControlCommandType,
       "tokenRingControlCommandTargetAddress": tokenRingControlCommandTargetAddress,
       "tokenRingControlBeaconEventIndex": tokenRingControlBeaconEventIndex,
       "tokenRingControlConfigEventIndex": tokenRingControlConfigEventIndex,
       "tokenRingControlOwner": tokenRingControlOwner,
       "tokenRingControlStatus": tokenRingControlStatus,
       "tokenRingNetworkTable": tokenRingNetworkTable,
       "tokenRingNetworkEntry": tokenRingNetworkEntry,
       "tokenRingNetworkIfIndex": tokenRingNetworkIfIndex,
       "tokenRingNetworkLastResetTime": tokenRingNetworkLastResetTime,
       "tokenRingNetworkRingNumber": tokenRingNetworkRingNumber,
       "tokenRingNetworkMediaSpeed": tokenRingNetworkMediaSpeed,
       "tokenRingNetworkBridges": tokenRingNetworkBridges,
       "tokenRingNetworkActiveStations": tokenRingNetworkActiveStations,
       "tokenRingNetworkInactiveStations": tokenRingNetworkInactiveStations,
       "tokenRingNetworkLastEnterMACAddress": tokenRingNetworkLastEnterMACAddress,
       "tokenRingNetworkLastExitMACAddress": tokenRingNetworkLastExitMACAddress,
       "tokenRingNetworkState": tokenRingNetworkState,
       "tokenRingNetworkStateCause": tokenRingNetworkStateCause,
       "tokenRingNetworkStateSenderMACAddress": tokenRingNetworkStateSenderMACAddress,
       "tokenRingNetworkStateUpstreamNeighborMACAddress": tokenRingNetworkStateUpstreamNeighborMACAddress,
       "tokenRingNetworkHostOrderChanges": tokenRingNetworkHostOrderChanges,
       "tokenRingNetworkActiveMonitorChanges": tokenRingNetworkActiveMonitorChanges,
       "tokenRingHostTable": tokenRingHostTable,
       "tokenRingHostEntry": tokenRingHostEntry,
       "tokenRingHostIfIndex": tokenRingHostIfIndex,
       "tokenRingHostIndex": tokenRingHostIndex,
       "tokenRingHostStatus": tokenRingHostStatus,
       "tokenRingHostLastEnterTime": tokenRingHostLastEnterTime,
       "tokenRingHostLastExitTime": tokenRingHostLastExitTime,
       "tokenRingHostMACAddress": tokenRingHostMACAddress,
       "tokenRingHostPhysicalDropNumber": tokenRingHostPhysicalDropNumber,
       "tokenRingHostSoftErrorReportTimerValue": tokenRingHostSoftErrorReportTimerValue,
       "tokenRingHostGroupAddresses": tokenRingHostGroupAddresses,
       "tokenRingHostFunctionalAddresses": tokenRingHostFunctionalAddresses,
       "tokenRingHostAuthorizedFunctionClass": tokenRingHostAuthorizedFunctionClass,
       "tokenRingHostAuthorizedAccessPriority": tokenRingHostAuthorizedAccessPriority,
       "tokenRingHostAdapterSoftwareLevel": tokenRingHostAdapterSoftwareLevel,
       "tokenRingHostAdapterStatusVector": tokenRingHostAdapterStatusVector,
       "tokenRingHostProductID": tokenRingHostProductID,
       "tokenRingHostLostMonitors": tokenRingHostLostMonitors,
       "tokenRingHostDuplicateMonitors": tokenRingHostDuplicateMonitors,
       "tokenRingHostDuplicateAddresses": tokenRingHostDuplicateAddresses,
       "tokenRingHostRingPollFailures": tokenRingHostRingPollFailures,
       "tokenRingHostInLineErrors": tokenRingHostInLineErrors,
       "tokenRingHostInternalErrors": tokenRingHostInternalErrors,
       "tokenRingHostInBurstErrors": tokenRingHostInBurstErrors,
       "tokenRingHostACErrors": tokenRingHostACErrors,
       "tokenRingHostAbortDelimiters": tokenRingHostAbortDelimiters,
       "tokenRingHostLostFrameErrors": tokenRingHostLostFrameErrors,
       "tokenRingHostReceiveCongestions": tokenRingHostReceiveCongestions,
       "tokenRingHostFrameCopiedErrors": tokenRingHostFrameCopiedErrors,
       "tokenRingHostFrequencyErrors": tokenRingHostFrequencyErrors,
       "tokenRingHostTokenErrors": tokenRingHostTokenErrors,
       "tokenRingHostOutLineErrors": tokenRingHostOutLineErrors,
       "tokenRingHostOutBurstErrors": tokenRingHostOutBurstErrors,
       "tokenRingHostInBeacons": tokenRingHostInBeacons,
       "tokenRingHostOutBeacons": tokenRingHostOutBeacons,
       "tokenRingHostInsertions": tokenRingHostInsertions,
       "tokenRingOrderTable": tokenRingOrderTable,
       "tokenRingOrderEntry": tokenRingOrderEntry,
       "tokenRingOrderIfIndex": tokenRingOrderIfIndex,
       "tokenRingOrderIndex": tokenRingOrderIndex,
       "tokenRingOrderStatus": tokenRingOrderStatus,
       "tokenRingOrderLastEnterTime": tokenRingOrderLastEnterTime,
       "tokenRingOrderLastExitTime": tokenRingOrderLastExitTime,
       "tokenRingOrderMACAddress": tokenRingOrderMACAddress,
       "tokenRingOrderPhysicalDropNumber": tokenRingOrderPhysicalDropNumber,
       "tokenRingOrderSoftErrorReportTimerValue": tokenRingOrderSoftErrorReportTimerValue,
       "tokenRingOrderGroupAddresses": tokenRingOrderGroupAddresses,
       "tokenRingOrderFunctionalAddresses": tokenRingOrderFunctionalAddresses,
       "tokenRingOrderAuthorizedFunctionClass": tokenRingOrderAuthorizedFunctionClass,
       "tokenRingOrderAuthorizedAccessPriority": tokenRingOrderAuthorizedAccessPriority,
       "tokenRingOrderAdapterSoftwareLevel": tokenRingOrderAdapterSoftwareLevel,
       "tokenRingOrderAdapterStatusVector": tokenRingOrderAdapterStatusVector,
       "tokenRingOrderProductID": tokenRingOrderProductID,
       "tokenRingOrderLostMonitors": tokenRingOrderLostMonitors,
       "tokenRingOrderDuplicateMonitors": tokenRingOrderDuplicateMonitors,
       "tokenRingOrderDuplicateAddresses": tokenRingOrderDuplicateAddresses,
       "tokenRingOrderRingPollFailures": tokenRingOrderRingPollFailures,
       "tokenRingOrderInLineErrors": tokenRingOrderInLineErrors,
       "tokenRingOrderInternalErrors": tokenRingOrderInternalErrors,
       "tokenRingOrderInBurstErrors": tokenRingOrderInBurstErrors,
       "tokenRingOrderACErrors": tokenRingOrderACErrors,
       "tokenRingOrderAbortDelimiters": tokenRingOrderAbortDelimiters,
       "tokenRingOrderLostFrameErrors": tokenRingOrderLostFrameErrors,
       "tokenRingOrderReceiveCongestions": tokenRingOrderReceiveCongestions,
       "tokenRingOrderFrameCopiedErrors": tokenRingOrderFrameCopiedErrors,
       "tokenRingOrderFrequencyErrors": tokenRingOrderFrequencyErrors,
       "tokenRingOrderTokenErrors": tokenRingOrderTokenErrors,
       "tokenRingOrderOutLineErrors": tokenRingOrderOutLineErrors,
       "tokenRingOrderOutBurstErrors": tokenRingOrderOutBurstErrors,
       "tokenRingOrderInBeacons": tokenRingOrderInBeacons,
       "tokenRingOrderOutBeacons": tokenRingOrderOutBeacons,
       "tokenRingOrderInsertions": tokenRingOrderInsertions}
)
