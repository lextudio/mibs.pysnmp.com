# SNMP MIB module (AXON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AXON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:58 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Directory_ObjectIdentity = ObjectIdentity
directory = _Directory_ObjectIdentity(
    (1, 3, 6, 1, 1)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_Mib_2_ObjectIdentity = ObjectIdentity
mib_2 = _Mib_2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 3)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Axon_ObjectIdentity = ObjectIdentity
axon = _Axon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 370)
)
_Clone_ObjectIdentity = ObjectIdentity
clone = _Clone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 370, 1)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 370, 2)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 370, 2, 1)
)
_Application_ObjectIdentity = ObjectIdentity
application = _Application_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 370, 3)
)
_AxFddi_ObjectIdentity = ObjectIdentity
axFddi = _AxFddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 370, 4)
)
_AxFddiStatistics_ObjectIdentity = ObjectIdentity
axFddiStatistics = _AxFddiStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 370, 4, 1)
)
_FddiStatsTable_Object = MibTable
fddiStatsTable = _FddiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1)
)
if mibBuilder.loadTexts:
    fddiStatsTable.setStatus("mandatory")
_FddiStatsEntry_Object = MibTableRow
fddiStatsEntry = _FddiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1)
)
fddiStatsEntry.setIndexNames(
    (0, "AXON-MIB", "fddiStatsIndex"),
)
if mibBuilder.loadTexts:
    fddiStatsEntry.setStatus("mandatory")


class _FddiStatsIndex_Type(Integer32):
    """Custom type fddiStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FddiStatsIndex_Type.__name__ = "Integer32"
_FddiStatsIndex_Object = MibTableColumn
fddiStatsIndex = _FddiStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 1),
    _FddiStatsIndex_Type()
)
fddiStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsIndex.setStatus("mandatory")
_FddiStatsDataSource_Type = ObjectIdentifier
_FddiStatsDataSource_Object = MibTableColumn
fddiStatsDataSource = _FddiStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 2),
    _FddiStatsDataSource_Type()
)
fddiStatsDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddiStatsDataSource.setStatus("mandatory")
_FddiStatsDropEvents_Type = Counter32
_FddiStatsDropEvents_Object = MibTableColumn
fddiStatsDropEvents = _FddiStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 3),
    _FddiStatsDropEvents_Type()
)
fddiStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsDropEvents.setStatus("mandatory")
_FddiStatsOctets_Type = Counter32
_FddiStatsOctets_Object = MibTableColumn
fddiStatsOctets = _FddiStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 4),
    _FddiStatsOctets_Type()
)
fddiStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsOctets.setStatus("mandatory")
_FddiStatsPkts_Type = Counter32
_FddiStatsPkts_Object = MibTableColumn
fddiStatsPkts = _FddiStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 5),
    _FddiStatsPkts_Type()
)
fddiStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsPkts.setStatus("mandatory")
_FddiStatsBroadcastPkts_Type = Counter32
_FddiStatsBroadcastPkts_Object = MibTableColumn
fddiStatsBroadcastPkts = _FddiStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 6),
    _FddiStatsBroadcastPkts_Type()
)
fddiStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsBroadcastPkts.setStatus("mandatory")
_FddiStatsMulticastPkts_Type = Counter32
_FddiStatsMulticastPkts_Object = MibTableColumn
fddiStatsMulticastPkts = _FddiStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 7),
    _FddiStatsMulticastPkts_Type()
)
fddiStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsMulticastPkts.setStatus("mandatory")
_FddiStatsErrors_Type = Counter32
_FddiStatsErrors_Object = MibTableColumn
fddiStatsErrors = _FddiStatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 8),
    _FddiStatsErrors_Type()
)
fddiStatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsErrors.setStatus("mandatory")
_FddiStatsPkts22Octets_Type = Counter32
_FddiStatsPkts22Octets_Object = MibTableColumn
fddiStatsPkts22Octets = _FddiStatsPkts22Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 9),
    _FddiStatsPkts22Octets_Type()
)
fddiStatsPkts22Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsPkts22Octets.setStatus("mandatory")
_FddiStatsPkts23to63Octets_Type = Counter32
_FddiStatsPkts23to63Octets_Object = MibTableColumn
fddiStatsPkts23to63Octets = _FddiStatsPkts23to63Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 10),
    _FddiStatsPkts23to63Octets_Type()
)
fddiStatsPkts23to63Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsPkts23to63Octets.setStatus("mandatory")
_FddiStatsPkts64to127Octets_Type = Counter32
_FddiStatsPkts64to127Octets_Object = MibTableColumn
fddiStatsPkts64to127Octets = _FddiStatsPkts64to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 11),
    _FddiStatsPkts64to127Octets_Type()
)
fddiStatsPkts64to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsPkts64to127Octets.setStatus("mandatory")
_FddiStatsPkts128to255Octets_Type = Counter32
_FddiStatsPkts128to255Octets_Object = MibTableColumn
fddiStatsPkts128to255Octets = _FddiStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 12),
    _FddiStatsPkts128to255Octets_Type()
)
fddiStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsPkts128to255Octets.setStatus("mandatory")
_FddiStatsPkts256to511Octets_Type = Counter32
_FddiStatsPkts256to511Octets_Object = MibTableColumn
fddiStatsPkts256to511Octets = _FddiStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 13),
    _FddiStatsPkts256to511Octets_Type()
)
fddiStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsPkts256to511Octets.setStatus("mandatory")
_FddiStatsPkts512to1023Octets_Type = Counter32
_FddiStatsPkts512to1023Octets_Object = MibTableColumn
fddiStatsPkts512to1023Octets = _FddiStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 14),
    _FddiStatsPkts512to1023Octets_Type()
)
fddiStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsPkts512to1023Octets.setStatus("mandatory")
_FddiStatsPkts1024to2047Octets_Type = Counter32
_FddiStatsPkts1024to2047Octets_Object = MibTableColumn
fddiStatsPkts1024to2047Octets = _FddiStatsPkts1024to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 15),
    _FddiStatsPkts1024to2047Octets_Type()
)
fddiStatsPkts1024to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsPkts1024to2047Octets.setStatus("mandatory")
_FddiStatsPkts2048to4095Octets_Type = Counter32
_FddiStatsPkts2048to4095Octets_Object = MibTableColumn
fddiStatsPkts2048to4095Octets = _FddiStatsPkts2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 16),
    _FddiStatsPkts2048to4095Octets_Type()
)
fddiStatsPkts2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsPkts2048to4095Octets.setStatus("mandatory")
_FddiStatsPkts4096to4500Octets_Type = Counter32
_FddiStatsPkts4096to4500Octets_Object = MibTableColumn
fddiStatsPkts4096to4500Octets = _FddiStatsPkts4096to4500Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 17),
    _FddiStatsPkts4096to4500Octets_Type()
)
fddiStatsPkts4096to4500Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsPkts4096to4500Octets.setStatus("mandatory")
_FddiStatsTNEG_Type = Counter32
_FddiStatsTNEG_Object = MibTableColumn
fddiStatsTNEG = _FddiStatsTNEG_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 18),
    _FddiStatsTNEG_Type()
)
fddiStatsTNEG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsTNEG.setStatus("mandatory")
_FddiStatsTokens_Type = Counter32
_FddiStatsTokens_Object = MibTableColumn
fddiStatsTokens = _FddiStatsTokens_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 19),
    _FddiStatsTokens_Type()
)
fddiStatsTokens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsTokens.setStatus("mandatory")
_FddiStatsSMTs_Type = Counter32
_FddiStatsSMTs_Object = MibTableColumn
fddiStatsSMTs = _FddiStatsSMTs_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 20),
    _FddiStatsSMTs_Type()
)
fddiStatsSMTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsSMTs.setStatus("mandatory")
_FddiStatsClaims_Type = Counter32
_FddiStatsClaims_Object = MibTableColumn
fddiStatsClaims = _FddiStatsClaims_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 21),
    _FddiStatsClaims_Type()
)
fddiStatsClaims.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsClaims.setStatus("mandatory")
_FddiStatsDirBeacons_Type = Counter32
_FddiStatsDirBeacons_Object = MibTableColumn
fddiStatsDirBeacons = _FddiStatsDirBeacons_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 22),
    _FddiStatsDirBeacons_Type()
)
fddiStatsDirBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsDirBeacons.setStatus("mandatory")
_FddiStatsBeacons_Type = Counter32
_FddiStatsBeacons_Object = MibTableColumn
fddiStatsBeacons = _FddiStatsBeacons_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 23),
    _FddiStatsBeacons_Type()
)
fddiStatsBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsBeacons.setStatus("mandatory")
_FddiStatsBeaconAddr_Type = OctetString
_FddiStatsBeaconAddr_Object = MibTableColumn
fddiStatsBeaconAddr = _FddiStatsBeaconAddr_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 24),
    _FddiStatsBeaconAddr_Type()
)
fddiStatsBeaconAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsBeaconAddr.setStatus("mandatory")
_FddiStatsDirBeaconAddr_Type = OctetString
_FddiStatsDirBeaconAddr_Object = MibTableColumn
fddiStatsDirBeaconAddr = _FddiStatsDirBeaconAddr_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 25),
    _FddiStatsDirBeaconAddr_Type()
)
fddiStatsDirBeaconAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsDirBeaconAddr.setStatus("mandatory")
_FddiStatsClaimAddr_Type = OctetString
_FddiStatsClaimAddr_Object = MibTableColumn
fddiStatsClaimAddr = _FddiStatsClaimAddr_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 26),
    _FddiStatsClaimAddr_Type()
)
fddiStatsClaimAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsClaimAddr.setStatus("mandatory")
_FddiStatsRingState_Type = Integer32
_FddiStatsRingState_Object = MibTableColumn
fddiStatsRingState = _FddiStatsRingState_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 27),
    _FddiStatsRingState_Type()
)
fddiStatsRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsRingState.setStatus("mandatory")
_FddiStatsOwner_Type = OctetString
_FddiStatsOwner_Object = MibTableColumn
fddiStatsOwner = _FddiStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 28),
    _FddiStatsOwner_Type()
)
fddiStatsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddiStatsOwner.setStatus("mandatory")
_FddiStatsStatus_Type = Integer32
_FddiStatsStatus_Object = MibTableColumn
fddiStatsStatus = _FddiStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 29),
    _FddiStatsStatus_Type()
)
fddiStatsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddiStatsStatus.setStatus("mandatory")
_FddiStatsOtherPkts_Type = Counter32
_FddiStatsOtherPkts_Object = MibTableColumn
fddiStatsOtherPkts = _FddiStatsOtherPkts_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 30),
    _FddiStatsOtherPkts_Type()
)
fddiStatsOtherPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsOtherPkts.setStatus("mandatory")
_FddiStatsOtherOctets_Type = Counter32
_FddiStatsOtherOctets_Object = MibTableColumn
fddiStatsOtherOctets = _FddiStatsOtherOctets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 1, 1, 1, 31),
    _FddiStatsOtherOctets_Type()
)
fddiStatsOtherOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiStatsOtherOctets.setStatus("mandatory")
_AxFddiHistory_ObjectIdentity = ObjectIdentity
axFddiHistory = _AxFddiHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 370, 4, 2)
)
_FddiHistoryTable_Object = MibTable
fddiHistoryTable = _FddiHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5)
)
if mibBuilder.loadTexts:
    fddiHistoryTable.setStatus("mandatory")
_FddiHistoryEntry_Object = MibTableRow
fddiHistoryEntry = _FddiHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1)
)
fddiHistoryEntry.setIndexNames(
    (0, "AXON-MIB", "fddiHistoryIndex"),
    (0, "AXON-MIB", "fddiHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    fddiHistoryEntry.setStatus("mandatory")


class _FddiHistoryIndex_Type(Integer32):
    """Custom type fddiHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FddiHistoryIndex_Type.__name__ = "Integer32"
_FddiHistoryIndex_Object = MibTableColumn
fddiHistoryIndex = _FddiHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 1),
    _FddiHistoryIndex_Type()
)
fddiHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryIndex.setStatus("mandatory")
_FddiHistorySampleIndex_Type = Integer32
_FddiHistorySampleIndex_Object = MibTableColumn
fddiHistorySampleIndex = _FddiHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 2),
    _FddiHistorySampleIndex_Type()
)
fddiHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistorySampleIndex.setStatus("mandatory")
_FddiHistoryIntervalStart_Type = TimeTicks
_FddiHistoryIntervalStart_Object = MibTableColumn
fddiHistoryIntervalStart = _FddiHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 3),
    _FddiHistoryIntervalStart_Type()
)
fddiHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryIntervalStart.setStatus("mandatory")
_FddiHistoryDropEvents_Type = Counter32
_FddiHistoryDropEvents_Object = MibTableColumn
fddiHistoryDropEvents = _FddiHistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 4),
    _FddiHistoryDropEvents_Type()
)
fddiHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryDropEvents.setStatus("mandatory")
_FddiHistoryOctets_Type = Counter32
_FddiHistoryOctets_Object = MibTableColumn
fddiHistoryOctets = _FddiHistoryOctets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 5),
    _FddiHistoryOctets_Type()
)
fddiHistoryOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryOctets.setStatus("mandatory")
_FddiHistoryPkts_Type = Counter32
_FddiHistoryPkts_Object = MibTableColumn
fddiHistoryPkts = _FddiHistoryPkts_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 6),
    _FddiHistoryPkts_Type()
)
fddiHistoryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryPkts.setStatus("mandatory")
_FddiHistoryBroadcastPkts_Type = Counter32
_FddiHistoryBroadcastPkts_Object = MibTableColumn
fddiHistoryBroadcastPkts = _FddiHistoryBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 7),
    _FddiHistoryBroadcastPkts_Type()
)
fddiHistoryBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryBroadcastPkts.setStatus("mandatory")
_FddiHistoryMulticastPkts_Type = Counter32
_FddiHistoryMulticastPkts_Object = MibTableColumn
fddiHistoryMulticastPkts = _FddiHistoryMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 8),
    _FddiHistoryMulticastPkts_Type()
)
fddiHistoryMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryMulticastPkts.setStatus("mandatory")
_FddiHistoryErrors_Type = Counter32
_FddiHistoryErrors_Object = MibTableColumn
fddiHistoryErrors = _FddiHistoryErrors_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 9),
    _FddiHistoryErrors_Type()
)
fddiHistoryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryErrors.setStatus("mandatory")
_FddiHistoryPkts22Octets_Type = Counter32
_FddiHistoryPkts22Octets_Object = MibTableColumn
fddiHistoryPkts22Octets = _FddiHistoryPkts22Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 10),
    _FddiHistoryPkts22Octets_Type()
)
fddiHistoryPkts22Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryPkts22Octets.setStatus("mandatory")
_FddiHistoryPkts23to63Octets_Type = Counter32
_FddiHistoryPkts23to63Octets_Object = MibTableColumn
fddiHistoryPkts23to63Octets = _FddiHistoryPkts23to63Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 11),
    _FddiHistoryPkts23to63Octets_Type()
)
fddiHistoryPkts23to63Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryPkts23to63Octets.setStatus("mandatory")
_FddiHistoryPkts64to127Octets_Type = Counter32
_FddiHistoryPkts64to127Octets_Object = MibTableColumn
fddiHistoryPkts64to127Octets = _FddiHistoryPkts64to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 12),
    _FddiHistoryPkts64to127Octets_Type()
)
fddiHistoryPkts64to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryPkts64to127Octets.setStatus("mandatory")
_FddiHistoryPkts128to255Octets_Type = Counter32
_FddiHistoryPkts128to255Octets_Object = MibTableColumn
fddiHistoryPkts128to255Octets = _FddiHistoryPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 13),
    _FddiHistoryPkts128to255Octets_Type()
)
fddiHistoryPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryPkts128to255Octets.setStatus("mandatory")
_FddiHistoryPkts256to511Octets_Type = Counter32
_FddiHistoryPkts256to511Octets_Object = MibTableColumn
fddiHistoryPkts256to511Octets = _FddiHistoryPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 14),
    _FddiHistoryPkts256to511Octets_Type()
)
fddiHistoryPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryPkts256to511Octets.setStatus("mandatory")
_FddiHistoryPkts512to1023Octets_Type = Counter32
_FddiHistoryPkts512to1023Octets_Object = MibTableColumn
fddiHistoryPkts512to1023Octets = _FddiHistoryPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 15),
    _FddiHistoryPkts512to1023Octets_Type()
)
fddiHistoryPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryPkts512to1023Octets.setStatus("mandatory")
_FddiHistoryPkts1024to2047Octets_Type = Counter32
_FddiHistoryPkts1024to2047Octets_Object = MibTableColumn
fddiHistoryPkts1024to2047Octets = _FddiHistoryPkts1024to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 16),
    _FddiHistoryPkts1024to2047Octets_Type()
)
fddiHistoryPkts1024to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryPkts1024to2047Octets.setStatus("mandatory")
_FddiHistoryPkts2048to4095Octets_Type = Counter32
_FddiHistoryPkts2048to4095Octets_Object = MibTableColumn
fddiHistoryPkts2048to4095Octets = _FddiHistoryPkts2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 17),
    _FddiHistoryPkts2048to4095Octets_Type()
)
fddiHistoryPkts2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryPkts2048to4095Octets.setStatus("mandatory")
_FddiHistoryPkts4096to4500Octets_Type = Counter32
_FddiHistoryPkts4096to4500Octets_Object = MibTableColumn
fddiHistoryPkts4096to4500Octets = _FddiHistoryPkts4096to4500Octets_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 18),
    _FddiHistoryPkts4096to4500Octets_Type()
)
fddiHistoryPkts4096to4500Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryPkts4096to4500Octets.setStatus("mandatory")


class _FddiHistoryUtilization_Type(Integer32):
    """Custom type fddiHistoryUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_FddiHistoryUtilization_Type.__name__ = "Integer32"
_FddiHistoryUtilization_Object = MibTableColumn
fddiHistoryUtilization = _FddiHistoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 19),
    _FddiHistoryUtilization_Type()
)
fddiHistoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryUtilization.setStatus("mandatory")
_FddiHistoryTNEG_Type = Counter32
_FddiHistoryTNEG_Object = MibTableColumn
fddiHistoryTNEG = _FddiHistoryTNEG_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 20),
    _FddiHistoryTNEG_Type()
)
fddiHistoryTNEG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryTNEG.setStatus("mandatory")
_FddiHistoryMeanTRT_Type = Counter32
_FddiHistoryMeanTRT_Object = MibTableColumn
fddiHistoryMeanTRT = _FddiHistoryMeanTRT_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 21),
    _FddiHistoryMeanTRT_Type()
)
fddiHistoryMeanTRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryMeanTRT.setStatus("mandatory")
_FddiHistorySMTs_Type = Counter32
_FddiHistorySMTs_Object = MibTableColumn
fddiHistorySMTs = _FddiHistorySMTs_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 22),
    _FddiHistorySMTs_Type()
)
fddiHistorySMTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistorySMTs.setStatus("mandatory")
_FddiHistoryClaims_Type = Counter32
_FddiHistoryClaims_Object = MibTableColumn
fddiHistoryClaims = _FddiHistoryClaims_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 23),
    _FddiHistoryClaims_Type()
)
fddiHistoryClaims.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryClaims.setStatus("mandatory")
_FddiHistoryDirBeacons_Type = Counter32
_FddiHistoryDirBeacons_Object = MibTableColumn
fddiHistoryDirBeacons = _FddiHistoryDirBeacons_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 24),
    _FddiHistoryDirBeacons_Type()
)
fddiHistoryDirBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryDirBeacons.setStatus("mandatory")
_FddiHistoryBeacons_Type = Counter32
_FddiHistoryBeacons_Object = MibTableColumn
fddiHistoryBeacons = _FddiHistoryBeacons_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 25),
    _FddiHistoryBeacons_Type()
)
fddiHistoryBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryBeacons.setStatus("mandatory")
_FddiHistoryRingStateChanges_Type = Counter32
_FddiHistoryRingStateChanges_Object = MibTableColumn
fddiHistoryRingStateChanges = _FddiHistoryRingStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 370, 4, 2, 5, 1, 26),
    _FddiHistoryRingStateChanges_Type()
)
fddiHistoryRingStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiHistoryRingStateChanges.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AXON-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "directory": directory,
       "mgmt": mgmt,
       "mib-2": mib_2,
       "experimental": experimental,
       "private": private,
       "enterprises": enterprises,
       "axon": axon,
       "clone": clone,
       "product": product,
       "common": common,
       "application": application,
       "axFddi": axFddi,
       "axFddiStatistics": axFddiStatistics,
       "fddiStatsTable": fddiStatsTable,
       "fddiStatsEntry": fddiStatsEntry,
       "fddiStatsIndex": fddiStatsIndex,
       "fddiStatsDataSource": fddiStatsDataSource,
       "fddiStatsDropEvents": fddiStatsDropEvents,
       "fddiStatsOctets": fddiStatsOctets,
       "fddiStatsPkts": fddiStatsPkts,
       "fddiStatsBroadcastPkts": fddiStatsBroadcastPkts,
       "fddiStatsMulticastPkts": fddiStatsMulticastPkts,
       "fddiStatsErrors": fddiStatsErrors,
       "fddiStatsPkts22Octets": fddiStatsPkts22Octets,
       "fddiStatsPkts23to63Octets": fddiStatsPkts23to63Octets,
       "fddiStatsPkts64to127Octets": fddiStatsPkts64to127Octets,
       "fddiStatsPkts128to255Octets": fddiStatsPkts128to255Octets,
       "fddiStatsPkts256to511Octets": fddiStatsPkts256to511Octets,
       "fddiStatsPkts512to1023Octets": fddiStatsPkts512to1023Octets,
       "fddiStatsPkts1024to2047Octets": fddiStatsPkts1024to2047Octets,
       "fddiStatsPkts2048to4095Octets": fddiStatsPkts2048to4095Octets,
       "fddiStatsPkts4096to4500Octets": fddiStatsPkts4096to4500Octets,
       "fddiStatsTNEG": fddiStatsTNEG,
       "fddiStatsTokens": fddiStatsTokens,
       "fddiStatsSMTs": fddiStatsSMTs,
       "fddiStatsClaims": fddiStatsClaims,
       "fddiStatsDirBeacons": fddiStatsDirBeacons,
       "fddiStatsBeacons": fddiStatsBeacons,
       "fddiStatsBeaconAddr": fddiStatsBeaconAddr,
       "fddiStatsDirBeaconAddr": fddiStatsDirBeaconAddr,
       "fddiStatsClaimAddr": fddiStatsClaimAddr,
       "fddiStatsRingState": fddiStatsRingState,
       "fddiStatsOwner": fddiStatsOwner,
       "fddiStatsStatus": fddiStatsStatus,
       "fddiStatsOtherPkts": fddiStatsOtherPkts,
       "fddiStatsOtherOctets": fddiStatsOtherOctets,
       "axFddiHistory": axFddiHistory,
       "fddiHistoryTable": fddiHistoryTable,
       "fddiHistoryEntry": fddiHistoryEntry,
       "fddiHistoryIndex": fddiHistoryIndex,
       "fddiHistorySampleIndex": fddiHistorySampleIndex,
       "fddiHistoryIntervalStart": fddiHistoryIntervalStart,
       "fddiHistoryDropEvents": fddiHistoryDropEvents,
       "fddiHistoryOctets": fddiHistoryOctets,
       "fddiHistoryPkts": fddiHistoryPkts,
       "fddiHistoryBroadcastPkts": fddiHistoryBroadcastPkts,
       "fddiHistoryMulticastPkts": fddiHistoryMulticastPkts,
       "fddiHistoryErrors": fddiHistoryErrors,
       "fddiHistoryPkts22Octets": fddiHistoryPkts22Octets,
       "fddiHistoryPkts23to63Octets": fddiHistoryPkts23to63Octets,
       "fddiHistoryPkts64to127Octets": fddiHistoryPkts64to127Octets,
       "fddiHistoryPkts128to255Octets": fddiHistoryPkts128to255Octets,
       "fddiHistoryPkts256to511Octets": fddiHistoryPkts256to511Octets,
       "fddiHistoryPkts512to1023Octets": fddiHistoryPkts512to1023Octets,
       "fddiHistoryPkts1024to2047Octets": fddiHistoryPkts1024to2047Octets,
       "fddiHistoryPkts2048to4095Octets": fddiHistoryPkts2048to4095Octets,
       "fddiHistoryPkts4096to4500Octets": fddiHistoryPkts4096to4500Octets,
       "fddiHistoryUtilization": fddiHistoryUtilization,
       "fddiHistoryTNEG": fddiHistoryTNEG,
       "fddiHistoryMeanTRT": fddiHistoryMeanTRT,
       "fddiHistorySMTs": fddiHistorySMTs,
       "fddiHistoryClaims": fddiHistoryClaims,
       "fddiHistoryDirBeacons": fddiHistoryDirBeacons,
       "fddiHistoryBeacons": fddiHistoryBeacons,
       "fddiHistoryRingStateChanges": fddiHistoryRingStateChanges}
)
