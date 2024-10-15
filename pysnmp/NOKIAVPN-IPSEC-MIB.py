# SNMP MIB module (NOKIAVPN-IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIAVPN-IPSEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:46 2024
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

(ipsec,
 nokiaVPNModules) = mibBuilder.importSymbols(
    "NOKIAVPN-MIB",
    "ipsec",
    "nokiaVPNModules")

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

nokiaVPNIPSECMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 5, 3)
)
nokiaVPNIPSECMIB.setRevisions(
        ("2001-01-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ReplayStats_ObjectIdentity = ObjectIdentity
replayStats = _ReplayStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 1)
)
_ReplayStatsWraps_Type = Integer32
_ReplayStatsWraps_Object = MibScalar
replayStatsWraps = _ReplayStatsWraps_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 1, 1),
    _ReplayStatsWraps_Type()
)
replayStatsWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replayStatsWraps.setStatus("current")
_ReplayStatsReplays_Type = Integer32
_ReplayStatsReplays_Object = MibScalar
replayStatsReplays = _ReplayStatsReplays_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 1, 2),
    _ReplayStatsReplays_Type()
)
replayStatsReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replayStatsReplays.setStatus("current")
_ReplayStatsoutofrange_Type = Integer32
_ReplayStatsoutofrange_Object = MibScalar
replayStatsoutofrange = _ReplayStatsoutofrange_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 1, 3),
    _ReplayStatsoutofrange_Type()
)
replayStatsoutofrange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replayStatsoutofrange.setStatus("current")
_ReplayStatstimewarps_Type = Integer32
_ReplayStatstimewarps_Object = MibScalar
replayStatstimewarps = _ReplayStatstimewarps_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 1, 4),
    _ReplayStatstimewarps_Type()
)
replayStatstimewarps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replayStatstimewarps.setStatus("current")
_ReplayStatsstale_Type = Integer32
_ReplayStatsstale_Object = MibScalar
replayStatsstale = _ReplayStatsstale_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 1, 5),
    _ReplayStatsstale_Type()
)
replayStatsstale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replayStatsstale.setStatus("current")
_ReplayStatsreset_Type = Integer32
_ReplayStatsreset_Object = MibScalar
replayStatsreset = _ReplayStatsreset_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 1, 6),
    _ReplayStatsreset_Type()
)
replayStatsreset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replayStatsreset.setStatus("current")
_ReplayStatsdeferred_Type = Integer32
_ReplayStatsdeferred_Object = MibScalar
replayStatsdeferred = _ReplayStatsdeferred_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 1, 7),
    _ReplayStatsdeferred_Type()
)
replayStatsdeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replayStatsdeferred.setStatus("current")
_NaIKEStats_ObjectIdentity = ObjectIdentity
naIKEStats = _NaIKEStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2)
)
_NaIKEStatsbadhash_Type = Integer32
_NaIKEStatsbadhash_Object = MibScalar
naIKEStatsbadhash = _NaIKEStatsbadhash_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 1),
    _NaIKEStatsbadhash_Type()
)
naIKEStatsbadhash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsbadhash.setStatus("current")
_NaIKEStatsbadsig_Type = Integer32
_NaIKEStatsbadsig_Object = MibScalar
naIKEStatsbadsig = _NaIKEStatsbadsig_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 2),
    _NaIKEStatsbadsig_Type()
)
naIKEStatsbadsig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsbadsig.setStatus("current")
_NaIKEStatsinvalidcookies_Type = Integer32
_NaIKEStatsinvalidcookies_Object = MibScalar
naIKEStatsinvalidcookies = _NaIKEStatsinvalidcookies_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 3),
    _NaIKEStatsinvalidcookies_Type()
)
naIKEStatsinvalidcookies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsinvalidcookies.setStatus("current")
_NaIKEStatsacounts_Type = Integer32
_NaIKEStatsacounts_Object = MibScalar
naIKEStatsacounts = _NaIKEStatsacounts_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 4),
    _NaIKEStatsacounts_Type()
)
naIKEStatsacounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsacounts.setStatus("current")
_NaIKEStatsmainmodes_Type = Integer32
_NaIKEStatsmainmodes_Object = MibScalar
naIKEStatsmainmodes = _NaIKEStatsmainmodes_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 5),
    _NaIKEStatsmainmodes_Type()
)
naIKEStatsmainmodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsmainmodes.setStatus("current")
_NaIKEStatsquickmodes_Type = Integer32
_NaIKEStatsquickmodes_Object = MibScalar
naIKEStatsquickmodes = _NaIKEStatsquickmodes_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 6),
    _NaIKEStatsquickmodes_Type()
)
naIKEStatsquickmodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsquickmodes.setStatus("current")
_NaIKEStatsaggressivemodes_Type = Integer32
_NaIKEStatsaggressivemodes_Object = MibScalar
naIKEStatsaggressivemodes = _NaIKEStatsaggressivemodes_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 7),
    _NaIKEStatsaggressivemodes_Type()
)
naIKEStatsaggressivemodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsaggressivemodes.setStatus("current")
_NaIKEStatsnewgroupmodes_Type = Integer32
_NaIKEStatsnewgroupmodes_Object = MibScalar
naIKEStatsnewgroupmodes = _NaIKEStatsnewgroupmodes_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 8),
    _NaIKEStatsnewgroupmodes_Type()
)
naIKEStatsnewgroupmodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsnewgroupmodes.setStatus("current")
_NaIKEStatsfailedsend_Type = Integer32
_NaIKEStatsfailedsend_Object = MibScalar
naIKEStatsfailedsend = _NaIKEStatsfailedsend_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 9),
    _NaIKEStatsfailedsend_Type()
)
naIKEStatsfailedsend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsfailedsend.setStatus("current")
_NaIKEStatstotalnetwork_Type = Integer32
_NaIKEStatstotalnetwork_Object = MibScalar
naIKEStatstotalnetwork = _NaIKEStatstotalnetwork_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 10),
    _NaIKEStatstotalnetwork_Type()
)
naIKEStatstotalnetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatstotalnetwork.setStatus("current")
_NaIKEStatstotalsend_Type = Integer32
_NaIKEStatstotalsend_Object = MibScalar
naIKEStatstotalsend = _NaIKEStatstotalsend_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 11),
    _NaIKEStatstotalsend_Type()
)
naIKEStatstotalsend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatstotalsend.setStatus("current")
_NaIKEStatstotalsaapi_Type = Integer32
_NaIKEStatstotalsaapi_Object = MibScalar
naIKEStatstotalsaapi = _NaIKEStatstotalsaapi_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 12),
    _NaIKEStatstotalsaapi_Type()
)
naIKEStatstotalsaapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatstotalsaapi.setStatus("current")
_NaIKEStatstotalipc_Type = Integer32
_NaIKEStatstotalipc_Object = MibScalar
naIKEStatstotalipc = _NaIKEStatstotalipc_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 13),
    _NaIKEStatstotalipc_Type()
)
naIKEStatstotalipc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatstotalipc.setStatus("current")
_NaIKEStatstotalmanual_Type = Integer32
_NaIKEStatstotalmanual_Object = MibScalar
naIKEStatstotalmanual = _NaIKEStatstotalmanual_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 14),
    _NaIKEStatstotalmanual_Type()
)
naIKEStatstotalmanual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatstotalmanual.setStatus("current")
_NaIKEStatstotalauto_Type = Integer32
_NaIKEStatstotalauto_Object = MibScalar
naIKEStatstotalauto = _NaIKEStatstotalauto_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 15),
    _NaIKEStatstotalauto_Type()
)
naIKEStatstotalauto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatstotalauto.setStatus("current")
_NaIKEStatstransitions_Type = Integer32
_NaIKEStatstransitions_Object = MibScalar
naIKEStatstransitions = _NaIKEStatstransitions_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 16),
    _NaIKEStatstransitions_Type()
)
naIKEStatstransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatstransitions.setStatus("current")
_NaIKEStatssentsa_Type = Integer32
_NaIKEStatssentsa_Object = MibScalar
naIKEStatssentsa = _NaIKEStatssentsa_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 17),
    _NaIKEStatssentsa_Type()
)
naIKEStatssentsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatssentsa.setStatus("current")
_NaIKEStatssentipsecsapair_Type = Integer32
_NaIKEStatssentipsecsapair_Object = MibScalar
naIKEStatssentipsecsapair = _NaIKEStatssentipsecsapair_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 18),
    _NaIKEStatssentipsecsapair_Type()
)
naIKEStatssentipsecsapair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatssentipsecsapair.setStatus("current")
_NaIKEStatssentpacket_Type = Integer32
_NaIKEStatssentpacket_Object = MibScalar
naIKEStatssentpacket = _NaIKEStatssentpacket_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 19),
    _NaIKEStatssentpacket_Type()
)
naIKEStatssentpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatssentpacket.setStatus("current")
_NaIKEStatsrecvsa_Type = Integer32
_NaIKEStatsrecvsa_Object = MibScalar
naIKEStatsrecvsa = _NaIKEStatsrecvsa_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 20),
    _NaIKEStatsrecvsa_Type()
)
naIKEStatsrecvsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsrecvsa.setStatus("current")
_NaIKEStatsrecvipsecsapair_Type = Integer32
_NaIKEStatsrecvipsecsapair_Object = MibScalar
naIKEStatsrecvipsecsapair = _NaIKEStatsrecvipsecsapair_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 21),
    _NaIKEStatsrecvipsecsapair_Type()
)
naIKEStatsrecvipsecsapair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsrecvipsecsapair.setStatus("current")
_NaIKEStatsrecvpacket_Type = Integer32
_NaIKEStatsrecvpacket_Object = MibScalar
naIKEStatsrecvpacket = _NaIKEStatsrecvpacket_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 22),
    _NaIKEStatsrecvpacket_Type()
)
naIKEStatsrecvpacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsrecvpacket.setStatus("current")
_NaIKEStatssentinitialstate_Type = Integer32
_NaIKEStatssentinitialstate_Object = MibScalar
naIKEStatssentinitialstate = _NaIKEStatssentinitialstate_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 23),
    _NaIKEStatssentinitialstate_Type()
)
naIKEStatssentinitialstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatssentinitialstate.setStatus("current")
_NaIKEStatssentflush_Type = Integer32
_NaIKEStatssentflush_Object = MibScalar
naIKEStatssentflush = _NaIKEStatssentflush_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 24),
    _NaIKEStatssentflush_Type()
)
naIKEStatssentflush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatssentflush.setStatus("current")
_NaIKEStatssentcryptostate_Type = Integer32
_NaIKEStatssentcryptostate_Object = MibScalar
naIKEStatssentcryptostate = _NaIKEStatssentcryptostate_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 25),
    _NaIKEStatssentcryptostate_Type()
)
naIKEStatssentcryptostate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatssentcryptostate.setStatus("current")
_NaIKEStatssentacquire_Type = Integer32
_NaIKEStatssentacquire_Object = MibScalar
naIKEStatssentacquire = _NaIKEStatssentacquire_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 26),
    _NaIKEStatssentacquire_Type()
)
naIKEStatssentacquire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatssentacquire.setStatus("current")
_NaIKEStatssentipseclifetime_Type = Integer32
_NaIKEStatssentipseclifetime_Object = MibScalar
naIKEStatssentipseclifetime = _NaIKEStatssentipseclifetime_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 27),
    _NaIKEStatssentipseclifetime_Type()
)
naIKEStatssentipseclifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatssentipseclifetime.setStatus("current")
_NaIKEStatssentikelifetime_Type = Integer32
_NaIKEStatssentikelifetime_Object = MibScalar
naIKEStatssentikelifetime = _NaIKEStatssentikelifetime_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 28),
    _NaIKEStatssentikelifetime_Type()
)
naIKEStatssentikelifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatssentikelifetime.setStatus("current")
_NaIKEStatssentdelete_Type = Integer32
_NaIKEStatssentdelete_Object = MibScalar
naIKEStatssentdelete = _NaIKEStatssentdelete_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 29),
    _NaIKEStatssentdelete_Type()
)
naIKEStatssentdelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatssentdelete.setStatus("current")
_NaIKEStatssentselector_Type = Integer32
_NaIKEStatssentselector_Object = MibScalar
naIKEStatssentselector = _NaIKEStatssentselector_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 30),
    _NaIKEStatssentselector_Type()
)
naIKEStatssentselector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatssentselector.setStatus("current")
_NaIKEStatsrecvjoin_Type = Integer32
_NaIKEStatsrecvjoin_Object = MibScalar
naIKEStatsrecvjoin = _NaIKEStatsrecvjoin_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 31),
    _NaIKEStatsrecvjoin_Type()
)
naIKEStatsrecvjoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsrecvjoin.setStatus("current")
_NaIKEStatsrecvrejoin_Type = Integer32
_NaIKEStatsrecvrejoin_Object = MibScalar
naIKEStatsrecvrejoin = _NaIKEStatsrecvrejoin_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 32),
    _NaIKEStatsrecvrejoin_Type()
)
naIKEStatsrecvrejoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsrecvrejoin.setStatus("current")
_NaIKEStatsrecvflush_Type = Integer32
_NaIKEStatsrecvflush_Object = MibScalar
naIKEStatsrecvflush = _NaIKEStatsrecvflush_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 33),
    _NaIKEStatsrecvflush_Type()
)
naIKEStatsrecvflush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsrecvflush.setStatus("current")
_NaIKEStatsrecvcryptostate_Type = Integer32
_NaIKEStatsrecvcryptostate_Object = MibScalar
naIKEStatsrecvcryptostate = _NaIKEStatsrecvcryptostate_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 34),
    _NaIKEStatsrecvcryptostate_Type()
)
naIKEStatsrecvcryptostate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsrecvcryptostate.setStatus("current")
_NaIKEStatsrecvacquire_Type = Integer32
_NaIKEStatsrecvacquire_Object = MibScalar
naIKEStatsrecvacquire = _NaIKEStatsrecvacquire_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 35),
    _NaIKEStatsrecvacquire_Type()
)
naIKEStatsrecvacquire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsrecvacquire.setStatus("current")
_NaIKEStatsrecvipseclifetime_Type = Integer32
_NaIKEStatsrecvipseclifetime_Object = MibScalar
naIKEStatsrecvipseclifetime = _NaIKEStatsrecvipseclifetime_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 36),
    _NaIKEStatsrecvipseclifetime_Type()
)
naIKEStatsrecvipseclifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsrecvipseclifetime.setStatus("current")
_NaIKEStatsrecvikelifetime_Type = Integer32
_NaIKEStatsrecvikelifetime_Object = MibScalar
naIKEStatsrecvikelifetime = _NaIKEStatsrecvikelifetime_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 37),
    _NaIKEStatsrecvikelifetime_Type()
)
naIKEStatsrecvikelifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsrecvikelifetime.setStatus("current")
_NaIKEStatsrecvdelete_Type = Integer32
_NaIKEStatsrecvdelete_Object = MibScalar
naIKEStatsrecvdelete = _NaIKEStatsrecvdelete_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 38),
    _NaIKEStatsrecvdelete_Type()
)
naIKEStatsrecvdelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsrecvdelete.setStatus("current")
_NaIKEStatsrecvselector_Type = Integer32
_NaIKEStatsrecvselector_Object = MibScalar
naIKEStatsrecvselector = _NaIKEStatsrecvselector_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 39),
    _NaIKEStatsrecvselector_Type()
)
naIKEStatsrecvselector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsrecvselector.setStatus("current")
_NaIKEStatssentinhibit_Type = Integer32
_NaIKEStatssentinhibit_Object = MibScalar
naIKEStatssentinhibit = _NaIKEStatssentinhibit_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 40),
    _NaIKEStatssentinhibit_Type()
)
naIKEStatssentinhibit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatssentinhibit.setStatus("current")
_NaIKEStatsrecvinhibit_Type = Integer32
_NaIKEStatsrecvinhibit_Object = MibScalar
naIKEStatsrecvinhibit = _NaIKEStatsrecvinhibit_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 41),
    _NaIKEStatsrecvinhibit_Type()
)
naIKEStatsrecvinhibit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naIKEStatsrecvinhibit.setStatus("current")
_NaAHStats_ObjectIdentity = ObjectIdentity
naAHStats = _NaAHStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3)
)
_NaAHStatssent_Type = Integer32
_NaAHStatssent_Object = MibScalar
naAHStatssent = _NaAHStatssent_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 1),
    _NaAHStatssent_Type()
)
naAHStatssent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatssent.setStatus("current")
_NaAHStatstunnelsent_Type = Integer32
_NaAHStatstunnelsent_Object = MibScalar
naAHStatstunnelsent = _NaAHStatstunnelsent_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 2),
    _NaAHStatstunnelsent_Type()
)
naAHStatstunnelsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatstunnelsent.setStatus("current")
_NaAHStatstransportsent_Type = Integer32
_NaAHStatstransportsent_Object = MibScalar
naAHStatstransportsent = _NaAHStatstransportsent_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 3),
    _NaAHStatstransportsent_Type()
)
naAHStatstransportsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatstransportsent.setStatus("current")
_NaAHStatsqueuesent_Type = Integer32
_NaAHStatsqueuesent_Object = MibScalar
naAHStatsqueuesent = _NaAHStatsqueuesent_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 4),
    _NaAHStatsqueuesent_Type()
)
naAHStatsqueuesent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatsqueuesent.setStatus("current")
_NaAHStatscpusent_Type = Integer32
_NaAHStatscpusent_Object = MibScalar
naAHStatscpusent = _NaAHStatscpusent_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 5),
    _NaAHStatscpusent_Type()
)
naAHStatscpusent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatscpusent.setStatus("current")
_NaAHStatsidlesent_Type = Integer32
_NaAHStatsidlesent_Object = MibScalar
naAHStatsidlesent = _NaAHStatsidlesent_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 6),
    _NaAHStatsidlesent_Type()
)
naAHStatsidlesent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatsidlesent.setStatus("current")
_NaAHStatshifnsent_Type = Integer32
_NaAHStatshifnsent_Object = MibScalar
naAHStatshifnsent = _NaAHStatshifnsent_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 7),
    _NaAHStatshifnsent_Type()
)
naAHStatshifnsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatshifnsent.setStatus("current")
_NaAHStatsouterrors_Type = Integer32
_NaAHStatsouterrors_Object = MibScalar
naAHStatsouterrors = _NaAHStatsouterrors_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 8),
    _NaAHStatsouterrors_Type()
)
naAHStatsouterrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatsouterrors.setStatus("current")
_NaAHStatsoutdrops_Type = Integer32
_NaAHStatsoutdrops_Object = MibScalar
naAHStatsoutdrops = _NaAHStatsoutdrops_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 9),
    _NaAHStatsoutdrops_Type()
)
naAHStatsoutdrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatsoutdrops.setStatus("current")
_NaAHStatsreceived_Type = Integer32
_NaAHStatsreceived_Object = MibScalar
naAHStatsreceived = _NaAHStatsreceived_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 10),
    _NaAHStatsreceived_Type()
)
naAHStatsreceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatsreceived.setStatus("current")
_NaAHStatstunnelrcvd_Type = Integer32
_NaAHStatstunnelrcvd_Object = MibScalar
naAHStatstunnelrcvd = _NaAHStatstunnelrcvd_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 11),
    _NaAHStatstunnelrcvd_Type()
)
naAHStatstunnelrcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatstunnelrcvd.setStatus("current")
_NaAHStatstransportrcvd_Type = Integer32
_NaAHStatstransportrcvd_Object = MibScalar
naAHStatstransportrcvd = _NaAHStatstransportrcvd_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 12),
    _NaAHStatstransportrcvd_Type()
)
naAHStatstransportrcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatstransportrcvd.setStatus("current")
_NaAHStatsqueuercvd_Type = Integer32
_NaAHStatsqueuercvd_Object = MibScalar
naAHStatsqueuercvd = _NaAHStatsqueuercvd_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 13),
    _NaAHStatsqueuercvd_Type()
)
naAHStatsqueuercvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatsqueuercvd.setStatus("current")
_NaAHStatscpurcvd_Type = Integer32
_NaAHStatscpurcvd_Object = MibScalar
naAHStatscpurcvd = _NaAHStatscpurcvd_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 14),
    _NaAHStatscpurcvd_Type()
)
naAHStatscpurcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatscpurcvd.setStatus("current")
_NaAHStatsidlercvd_Type = Integer32
_NaAHStatsidlercvd_Object = MibScalar
naAHStatsidlercvd = _NaAHStatsidlercvd_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 15),
    _NaAHStatsidlercvd_Type()
)
naAHStatsidlercvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatsidlercvd.setStatus("current")
_NaAHStatshifnrcvd_Type = Integer32
_NaAHStatshifnrcvd_Object = MibScalar
naAHStatshifnrcvd = _NaAHStatshifnrcvd_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 16),
    _NaAHStatshifnrcvd_Type()
)
naAHStatshifnrcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatshifnrcvd.setStatus("current")
_NaAHStatsinerrors_Type = Integer32
_NaAHStatsinerrors_Object = MibScalar
naAHStatsinerrors = _NaAHStatsinerrors_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 17),
    _NaAHStatsinerrors_Type()
)
naAHStatsinerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatsinerrors.setStatus("current")
_NaAHStatsindrops_Type = Integer32
_NaAHStatsindrops_Object = MibScalar
naAHStatsindrops = _NaAHStatsindrops_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 18),
    _NaAHStatsindrops_Type()
)
naAHStatsindrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatsindrops.setStatus("current")
_NaAHStatssafailures_Type = Integer32
_NaAHStatssafailures_Object = MibScalar
naAHStatssafailures = _NaAHStatssafailures_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 19),
    _NaAHStatssafailures_Type()
)
naAHStatssafailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatssafailures.setStatus("current")
_NaAHStatsreplay_Type = Integer32
_NaAHStatsreplay_Object = MibScalar
naAHStatsreplay = _NaAHStatsreplay_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 20),
    _NaAHStatsreplay_Type()
)
naAHStatsreplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatsreplay.setStatus("current")
_NaAHStatsfragments_Type = Integer32
_NaAHStatsfragments_Object = MibScalar
naAHStatsfragments = _NaAHStatsfragments_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 21),
    _NaAHStatsfragments_Type()
)
naAHStatsfragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatsfragments.setStatus("current")
_NaAHStatshifnrefused_Type = Integer32
_NaAHStatshifnrefused_Object = MibScalar
naAHStatshifnrefused = _NaAHStatshifnrefused_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 22),
    _NaAHStatshifnrefused_Type()
)
naAHStatshifnrefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatshifnrefused.setStatus("current")
_NaAHStatscpurefused_Type = Integer32
_NaAHStatscpurefused_Object = MibScalar
naAHStatscpurefused = _NaAHStatscpurefused_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 23),
    _NaAHStatscpurefused_Type()
)
naAHStatscpurefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naAHStatscpurefused.setStatus("current")
_NaESPStats_ObjectIdentity = ObjectIdentity
naESPStats = _NaESPStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4)
)
_NaESPStatssent_Type = Integer32
_NaESPStatssent_Object = MibScalar
naESPStatssent = _NaESPStatssent_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 1),
    _NaESPStatssent_Type()
)
naESPStatssent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatssent.setStatus("current")
_NaESPStatstunnelsent_Type = Integer32
_NaESPStatstunnelsent_Object = MibScalar
naESPStatstunnelsent = _NaESPStatstunnelsent_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 2),
    _NaESPStatstunnelsent_Type()
)
naESPStatstunnelsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatstunnelsent.setStatus("current")
_NaESPStatstransportsent_Type = Integer32
_NaESPStatstransportsent_Object = MibScalar
naESPStatstransportsent = _NaESPStatstransportsent_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 3),
    _NaESPStatstransportsent_Type()
)
naESPStatstransportsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatstransportsent.setStatus("current")
_NaESPStatsqueuesent_Type = Integer32
_NaESPStatsqueuesent_Object = MibScalar
naESPStatsqueuesent = _NaESPStatsqueuesent_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 4),
    _NaESPStatsqueuesent_Type()
)
naESPStatsqueuesent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatsqueuesent.setStatus("current")
_NaESPStatscpusent_Type = Integer32
_NaESPStatscpusent_Object = MibScalar
naESPStatscpusent = _NaESPStatscpusent_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 5),
    _NaESPStatscpusent_Type()
)
naESPStatscpusent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatscpusent.setStatus("current")
_NaESPStatsidlesent_Type = Integer32
_NaESPStatsidlesent_Object = MibScalar
naESPStatsidlesent = _NaESPStatsidlesent_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 6),
    _NaESPStatsidlesent_Type()
)
naESPStatsidlesent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatsidlesent.setStatus("current")
_NaESPStatshifnsent_Type = Integer32
_NaESPStatshifnsent_Object = MibScalar
naESPStatshifnsent = _NaESPStatshifnsent_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 7),
    _NaESPStatshifnsent_Type()
)
naESPStatshifnsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatshifnsent.setStatus("current")
_NaESPStatsouterrors_Type = Integer32
_NaESPStatsouterrors_Object = MibScalar
naESPStatsouterrors = _NaESPStatsouterrors_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 8),
    _NaESPStatsouterrors_Type()
)
naESPStatsouterrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatsouterrors.setStatus("current")
_NaESPStatsoutdrops_Type = Integer32
_NaESPStatsoutdrops_Object = MibScalar
naESPStatsoutdrops = _NaESPStatsoutdrops_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 9),
    _NaESPStatsoutdrops_Type()
)
naESPStatsoutdrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatsoutdrops.setStatus("current")
_NaESPStatsreceived_Type = Integer32
_NaESPStatsreceived_Object = MibScalar
naESPStatsreceived = _NaESPStatsreceived_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 10),
    _NaESPStatsreceived_Type()
)
naESPStatsreceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatsreceived.setStatus("current")
_NaESPStatstunnelrcvd_Type = Integer32
_NaESPStatstunnelrcvd_Object = MibScalar
naESPStatstunnelrcvd = _NaESPStatstunnelrcvd_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 11),
    _NaESPStatstunnelrcvd_Type()
)
naESPStatstunnelrcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatstunnelrcvd.setStatus("current")
_NaESPStatstransportrcvd_Type = Integer32
_NaESPStatstransportrcvd_Object = MibScalar
naESPStatstransportrcvd = _NaESPStatstransportrcvd_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 12),
    _NaESPStatstransportrcvd_Type()
)
naESPStatstransportrcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatstransportrcvd.setStatus("current")
_NaESPStatsqueuercvd_Type = Integer32
_NaESPStatsqueuercvd_Object = MibScalar
naESPStatsqueuercvd = _NaESPStatsqueuercvd_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 13),
    _NaESPStatsqueuercvd_Type()
)
naESPStatsqueuercvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatsqueuercvd.setStatus("current")
_NaESPStatscpurcvd_Type = Integer32
_NaESPStatscpurcvd_Object = MibScalar
naESPStatscpurcvd = _NaESPStatscpurcvd_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 14),
    _NaESPStatscpurcvd_Type()
)
naESPStatscpurcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatscpurcvd.setStatus("current")
_NaESPStatsidlercvd_Type = Integer32
_NaESPStatsidlercvd_Object = MibScalar
naESPStatsidlercvd = _NaESPStatsidlercvd_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 15),
    _NaESPStatsidlercvd_Type()
)
naESPStatsidlercvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatsidlercvd.setStatus("current")
_NaESPStatshifnrcvd_Type = Integer32
_NaESPStatshifnrcvd_Object = MibScalar
naESPStatshifnrcvd = _NaESPStatshifnrcvd_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 16),
    _NaESPStatshifnrcvd_Type()
)
naESPStatshifnrcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatshifnrcvd.setStatus("current")
_NaESPStatsinerrors_Type = Integer32
_NaESPStatsinerrors_Object = MibScalar
naESPStatsinerrors = _NaESPStatsinerrors_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 17),
    _NaESPStatsinerrors_Type()
)
naESPStatsinerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatsinerrors.setStatus("current")
_NaESPStatsindrops_Type = Integer32
_NaESPStatsindrops_Object = MibScalar
naESPStatsindrops = _NaESPStatsindrops_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 18),
    _NaESPStatsindrops_Type()
)
naESPStatsindrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatsindrops.setStatus("current")
_NaESPStatssafailures_Type = Integer32
_NaESPStatssafailures_Object = MibScalar
naESPStatssafailures = _NaESPStatssafailures_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 19),
    _NaESPStatssafailures_Type()
)
naESPStatssafailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatssafailures.setStatus("current")
_NaESPStatsreplay_Type = Integer32
_NaESPStatsreplay_Object = MibScalar
naESPStatsreplay = _NaESPStatsreplay_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 20),
    _NaESPStatsreplay_Type()
)
naESPStatsreplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatsreplay.setStatus("current")
_NaESPStatsfragments_Type = Integer32
_NaESPStatsfragments_Object = MibScalar
naESPStatsfragments = _NaESPStatsfragments_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 21),
    _NaESPStatsfragments_Type()
)
naESPStatsfragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatsfragments.setStatus("current")
_NaESPStatspadverifyfailures_Type = Integer32
_NaESPStatspadverifyfailures_Object = MibScalar
naESPStatspadverifyfailures = _NaESPStatspadverifyfailures_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 22),
    _NaESPStatspadverifyfailures_Type()
)
naESPStatspadverifyfailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatspadverifyfailures.setStatus("current")
_NaESPStatssignaturefailures_Type = Integer32
_NaESPStatssignaturefailures_Object = MibScalar
naESPStatssignaturefailures = _NaESPStatssignaturefailures_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 23),
    _NaESPStatssignaturefailures_Type()
)
naESPStatssignaturefailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatssignaturefailures.setStatus("current")
_NaESPStatsweakkey_Type = Integer32
_NaESPStatsweakkey_Object = MibScalar
naESPStatsweakkey = _NaESPStatsweakkey_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 24),
    _NaESPStatsweakkey_Type()
)
naESPStatsweakkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatsweakkey.setStatus("current")
_NaESPStatskeyparity_Type = Integer32
_NaESPStatskeyparity_Object = MibScalar
naESPStatskeyparity = _NaESPStatskeyparity_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 25),
    _NaESPStatskeyparity_Type()
)
naESPStatskeyparity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatskeyparity.setStatus("current")
_NaESPStatshifnrefused_Type = Integer32
_NaESPStatshifnrefused_Object = MibScalar
naESPStatshifnrefused = _NaESPStatshifnrefused_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 26),
    _NaESPStatshifnrefused_Type()
)
naESPStatshifnrefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatshifnrefused.setStatus("current")
_NaESPStatscpurefused_Type = Integer32
_NaESPStatscpurefused_Object = MibScalar
naESPStatscpurefused = _NaESPStatscpurefused_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 27),
    _NaESPStatscpurefused_Type()
)
naESPStatscpurefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPStatscpurefused.setStatus("current")
_NaESPNatEncapsulate_Type = Integer32
_NaESPNatEncapsulate_Object = MibScalar
naESPNatEncapsulate = _NaESPNatEncapsulate_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 28),
    _NaESPNatEncapsulate_Type()
)
naESPNatEncapsulate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPNatEncapsulate.setStatus("current")
_NaESPNatDecapsulate_Type = Integer32
_NaESPNatDecapsulate_Object = MibScalar
naESPNatDecapsulate = _NaESPNatDecapsulate_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 29),
    _NaESPNatDecapsulate_Type()
)
naESPNatDecapsulate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naESPNatDecapsulate.setStatus("current")
_NaKeyStats_ObjectIdentity = ObjectIdentity
naKeyStats = _NaKeyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5)
)
_NaKeyStatssyntax_Type = Integer32
_NaKeyStatssyntax_Object = MibScalar
naKeyStatssyntax = _NaKeyStatssyntax_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 1),
    _NaKeyStatssyntax_Type()
)
naKeyStatssyntax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatssyntax.setStatus("current")
_NaKeyStatsoutbound_Type = Integer32
_NaKeyStatsoutbound_Object = MibScalar
naKeyStatsoutbound = _NaKeyStatsoutbound_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 2),
    _NaKeyStatsoutbound_Type()
)
naKeyStatsoutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsoutbound.setStatus("current")
_NaKeyStatsinbound_Type = Integer32
_NaKeyStatsinbound_Object = MibScalar
naKeyStatsinbound = _NaKeyStatsinbound_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 3),
    _NaKeyStatsinbound_Type()
)
naKeyStatsinbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsinbound.setStatus("current")
_NaKeyStatspending_Type = Integer32
_NaKeyStatspending_Object = MibScalar
naKeyStatspending = _NaKeyStatspending_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 4),
    _NaKeyStatspending_Type()
)
naKeyStatspending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatspending.setStatus("current")
_NaKeyStatsselectors_Type = Integer32
_NaKeyStatsselectors_Object = MibScalar
naKeyStatsselectors = _NaKeyStatsselectors_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 5),
    _NaKeyStatsselectors_Type()
)
naKeyStatsselectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsselectors.setStatus("current")
_NaKeyStatsoutlast_Type = Integer32
_NaKeyStatsoutlast_Object = MibScalar
naKeyStatsoutlast = _NaKeyStatsoutlast_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 6),
    _NaKeyStatsoutlast_Type()
)
naKeyStatsoutlast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsoutlast.setStatus("current")
_NaKeyStatsouthash_Type = Integer32
_NaKeyStatsouthash_Object = MibScalar
naKeyStatsouthash = _NaKeyStatsouthash_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 7),
    _NaKeyStatsouthash_Type()
)
naKeyStatsouthash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsouthash.setStatus("current")
_NaKeyStatsoutnew_Type = Integer32
_NaKeyStatsoutnew_Object = MibScalar
naKeyStatsoutnew = _NaKeyStatsoutnew_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 8),
    _NaKeyStatsoutnew_Type()
)
naKeyStatsoutnew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsoutnew.setStatus("current")
_NaKeyStatsinlast_Type = Integer32
_NaKeyStatsinlast_Object = MibScalar
naKeyStatsinlast = _NaKeyStatsinlast_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 9),
    _NaKeyStatsinlast_Type()
)
naKeyStatsinlast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsinlast.setStatus("current")
_NaKeyStatsinhash_Type = Integer32
_NaKeyStatsinhash_Object = MibScalar
naKeyStatsinhash = _NaKeyStatsinhash_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 10),
    _NaKeyStatsinhash_Type()
)
naKeyStatsinhash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsinhash.setStatus("current")
_NaKeyStatsrefresh_Type = Integer32
_NaKeyStatsrefresh_Object = MibScalar
naKeyStatsrefresh = _NaKeyStatsrefresh_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 11),
    _NaKeyStatsrefresh_Type()
)
naKeyStatsrefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsrefresh.setStatus("current")
_NaKeyStatsreaped_Type = Integer32
_NaKeyStatsreaped_Object = MibScalar
naKeyStatsreaped = _NaKeyStatsreaped_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 12),
    _NaKeyStatsreaped_Type()
)
naKeyStatsreaped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsreaped.setStatus("current")
_NaKeyStatsreapedlarval_Type = Integer32
_NaKeyStatsreapedlarval_Object = MibScalar
naKeyStatsreapedlarval = _NaKeyStatsreapedlarval_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 13),
    _NaKeyStatsreapedlarval_Type()
)
naKeyStatsreapedlarval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsreapedlarval.setStatus("current")
_NaKeyStatsbypass_Type = Integer32
_NaKeyStatsbypass_Object = MibScalar
naKeyStatsbypass = _NaKeyStatsbypass_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 14),
    _NaKeyStatsbypass_Type()
)
naKeyStatsbypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsbypass.setStatus("current")
_NaKeyStatsdrop_Type = Integer32
_NaKeyStatsdrop_Object = MibScalar
naKeyStatsdrop = _NaKeyStatsdrop_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 15),
    _NaKeyStatsdrop_Type()
)
naKeyStatsdrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsdrop.setStatus("current")
_NaKeyStatsprotect_Type = Integer32
_NaKeyStatsprotect_Object = MibScalar
naKeyStatsprotect = _NaKeyStatsprotect_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 16),
    _NaKeyStatsprotect_Type()
)
naKeyStatsprotect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsprotect.setStatus("current")
_NaKeyStatsinbypass_Type = Integer32
_NaKeyStatsinbypass_Object = MibScalar
naKeyStatsinbypass = _NaKeyStatsinbypass_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 17),
    _NaKeyStatsinbypass_Type()
)
naKeyStatsinbypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsinbypass.setStatus("current")
_NaKeyStatsindrop_Type = Integer32
_NaKeyStatsindrop_Object = MibScalar
naKeyStatsindrop = _NaKeyStatsindrop_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 18),
    _NaKeyStatsindrop_Type()
)
naKeyStatsindrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsindrop.setStatus("current")
_NaKeyStatsinprotect_Type = Integer32
_NaKeyStatsinprotect_Object = MibScalar
naKeyStatsinprotect = _NaKeyStatsinprotect_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 19),
    _NaKeyStatsinprotect_Type()
)
naKeyStatsinprotect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsinprotect.setStatus("current")
_NaKeyStatsstallq_Type = Integer32
_NaKeyStatsstallq_Object = MibScalar
naKeyStatsstallq = _NaKeyStatsstallq_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 20),
    _NaKeyStatsstallq_Type()
)
naKeyStatsstallq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsstallq.setStatus("current")
_NaKeyStatsnomatch_Type = Integer32
_NaKeyStatsnomatch_Object = MibScalar
naKeyStatsnomatch = _NaKeyStatsnomatch_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 21),
    _NaKeyStatsnomatch_Type()
)
naKeyStatsnomatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsnomatch.setStatus("current")
_NaKeyStatsinnomatch_Type = Integer32
_NaKeyStatsinnomatch_Object = MibScalar
naKeyStatsinnomatch = _NaKeyStatsinnomatch_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 22),
    _NaKeyStatsinnomatch_Type()
)
naKeyStatsinnomatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsinnomatch.setStatus("current")
_NaKeyStatsinmismatch_Type = Integer32
_NaKeyStatsinmismatch_Object = MibScalar
naKeyStatsinmismatch = _NaKeyStatsinmismatch_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 23),
    _NaKeyStatsinmismatch_Type()
)
naKeyStatsinmismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsinmismatch.setStatus("current")
_NaKeyStatsadvmtusent_Type = Integer32
_NaKeyStatsadvmtusent_Object = MibScalar
naKeyStatsadvmtusent = _NaKeyStatsadvmtusent_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 24),
    _NaKeyStatsadvmtusent_Type()
)
naKeyStatsadvmtusent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsadvmtusent.setStatus("current")
_NaKeyStatsadvmturcvd_Type = Integer32
_NaKeyStatsadvmturcvd_Object = MibScalar
naKeyStatsadvmturcvd = _NaKeyStatsadvmturcvd_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 25),
    _NaKeyStatsadvmturcvd_Type()
)
naKeyStatsadvmturcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsadvmturcvd.setStatus("current")
_NaKeyStatsphantom_Type = Integer32
_NaKeyStatsphantom_Object = MibScalar
naKeyStatsphantom = _NaKeyStatsphantom_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 26),
    _NaKeyStatsphantom_Type()
)
naKeyStatsphantom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsphantom.setStatus("current")
_NaKeyStatsdynamicselectors_Type = Integer32
_NaKeyStatsdynamicselectors_Object = MibScalar
naKeyStatsdynamicselectors = _NaKeyStatsdynamicselectors_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 27),
    _NaKeyStatsdynamicselectors_Type()
)
naKeyStatsdynamicselectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatsdynamicselectors.setStatus("current")
_NaKeyStatstoolarge_Type = Integer32
_NaKeyStatstoolarge_Object = MibScalar
naKeyStatstoolarge = _NaKeyStatstoolarge_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 28),
    _NaKeyStatstoolarge_Type()
)
naKeyStatstoolarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naKeyStatstoolarge.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIAVPN-IPSEC-MIB",
    **{"replayStats": replayStats,
       "replayStatsWraps": replayStatsWraps,
       "replayStatsReplays": replayStatsReplays,
       "replayStatsoutofrange": replayStatsoutofrange,
       "replayStatstimewarps": replayStatstimewarps,
       "replayStatsstale": replayStatsstale,
       "replayStatsreset": replayStatsreset,
       "replayStatsdeferred": replayStatsdeferred,
       "naIKEStats": naIKEStats,
       "naIKEStatsbadhash": naIKEStatsbadhash,
       "naIKEStatsbadsig": naIKEStatsbadsig,
       "naIKEStatsinvalidcookies": naIKEStatsinvalidcookies,
       "naIKEStatsacounts": naIKEStatsacounts,
       "naIKEStatsmainmodes": naIKEStatsmainmodes,
       "naIKEStatsquickmodes": naIKEStatsquickmodes,
       "naIKEStatsaggressivemodes": naIKEStatsaggressivemodes,
       "naIKEStatsnewgroupmodes": naIKEStatsnewgroupmodes,
       "naIKEStatsfailedsend": naIKEStatsfailedsend,
       "naIKEStatstotalnetwork": naIKEStatstotalnetwork,
       "naIKEStatstotalsend": naIKEStatstotalsend,
       "naIKEStatstotalsaapi": naIKEStatstotalsaapi,
       "naIKEStatstotalipc": naIKEStatstotalipc,
       "naIKEStatstotalmanual": naIKEStatstotalmanual,
       "naIKEStatstotalauto": naIKEStatstotalauto,
       "naIKEStatstransitions": naIKEStatstransitions,
       "naIKEStatssentsa": naIKEStatssentsa,
       "naIKEStatssentipsecsapair": naIKEStatssentipsecsapair,
       "naIKEStatssentpacket": naIKEStatssentpacket,
       "naIKEStatsrecvsa": naIKEStatsrecvsa,
       "naIKEStatsrecvipsecsapair": naIKEStatsrecvipsecsapair,
       "naIKEStatsrecvpacket": naIKEStatsrecvpacket,
       "naIKEStatssentinitialstate": naIKEStatssentinitialstate,
       "naIKEStatssentflush": naIKEStatssentflush,
       "naIKEStatssentcryptostate": naIKEStatssentcryptostate,
       "naIKEStatssentacquire": naIKEStatssentacquire,
       "naIKEStatssentipseclifetime": naIKEStatssentipseclifetime,
       "naIKEStatssentikelifetime": naIKEStatssentikelifetime,
       "naIKEStatssentdelete": naIKEStatssentdelete,
       "naIKEStatssentselector": naIKEStatssentselector,
       "naIKEStatsrecvjoin": naIKEStatsrecvjoin,
       "naIKEStatsrecvrejoin": naIKEStatsrecvrejoin,
       "naIKEStatsrecvflush": naIKEStatsrecvflush,
       "naIKEStatsrecvcryptostate": naIKEStatsrecvcryptostate,
       "naIKEStatsrecvacquire": naIKEStatsrecvacquire,
       "naIKEStatsrecvipseclifetime": naIKEStatsrecvipseclifetime,
       "naIKEStatsrecvikelifetime": naIKEStatsrecvikelifetime,
       "naIKEStatsrecvdelete": naIKEStatsrecvdelete,
       "naIKEStatsrecvselector": naIKEStatsrecvselector,
       "naIKEStatssentinhibit": naIKEStatssentinhibit,
       "naIKEStatsrecvinhibit": naIKEStatsrecvinhibit,
       "naAHStats": naAHStats,
       "naAHStatssent": naAHStatssent,
       "naAHStatstunnelsent": naAHStatstunnelsent,
       "naAHStatstransportsent": naAHStatstransportsent,
       "naAHStatsqueuesent": naAHStatsqueuesent,
       "naAHStatscpusent": naAHStatscpusent,
       "naAHStatsidlesent": naAHStatsidlesent,
       "naAHStatshifnsent": naAHStatshifnsent,
       "naAHStatsouterrors": naAHStatsouterrors,
       "naAHStatsoutdrops": naAHStatsoutdrops,
       "naAHStatsreceived": naAHStatsreceived,
       "naAHStatstunnelrcvd": naAHStatstunnelrcvd,
       "naAHStatstransportrcvd": naAHStatstransportrcvd,
       "naAHStatsqueuercvd": naAHStatsqueuercvd,
       "naAHStatscpurcvd": naAHStatscpurcvd,
       "naAHStatsidlercvd": naAHStatsidlercvd,
       "naAHStatshifnrcvd": naAHStatshifnrcvd,
       "naAHStatsinerrors": naAHStatsinerrors,
       "naAHStatsindrops": naAHStatsindrops,
       "naAHStatssafailures": naAHStatssafailures,
       "naAHStatsreplay": naAHStatsreplay,
       "naAHStatsfragments": naAHStatsfragments,
       "naAHStatshifnrefused": naAHStatshifnrefused,
       "naAHStatscpurefused": naAHStatscpurefused,
       "naESPStats": naESPStats,
       "naESPStatssent": naESPStatssent,
       "naESPStatstunnelsent": naESPStatstunnelsent,
       "naESPStatstransportsent": naESPStatstransportsent,
       "naESPStatsqueuesent": naESPStatsqueuesent,
       "naESPStatscpusent": naESPStatscpusent,
       "naESPStatsidlesent": naESPStatsidlesent,
       "naESPStatshifnsent": naESPStatshifnsent,
       "naESPStatsouterrors": naESPStatsouterrors,
       "naESPStatsoutdrops": naESPStatsoutdrops,
       "naESPStatsreceived": naESPStatsreceived,
       "naESPStatstunnelrcvd": naESPStatstunnelrcvd,
       "naESPStatstransportrcvd": naESPStatstransportrcvd,
       "naESPStatsqueuercvd": naESPStatsqueuercvd,
       "naESPStatscpurcvd": naESPStatscpurcvd,
       "naESPStatsidlercvd": naESPStatsidlercvd,
       "naESPStatshifnrcvd": naESPStatshifnrcvd,
       "naESPStatsinerrors": naESPStatsinerrors,
       "naESPStatsindrops": naESPStatsindrops,
       "naESPStatssafailures": naESPStatssafailures,
       "naESPStatsreplay": naESPStatsreplay,
       "naESPStatsfragments": naESPStatsfragments,
       "naESPStatspadverifyfailures": naESPStatspadverifyfailures,
       "naESPStatssignaturefailures": naESPStatssignaturefailures,
       "naESPStatsweakkey": naESPStatsweakkey,
       "naESPStatskeyparity": naESPStatskeyparity,
       "naESPStatshifnrefused": naESPStatshifnrefused,
       "naESPStatscpurefused": naESPStatscpurefused,
       "naESPNatEncapsulate": naESPNatEncapsulate,
       "naESPNatDecapsulate": naESPNatDecapsulate,
       "naKeyStats": naKeyStats,
       "naKeyStatssyntax": naKeyStatssyntax,
       "naKeyStatsoutbound": naKeyStatsoutbound,
       "naKeyStatsinbound": naKeyStatsinbound,
       "naKeyStatspending": naKeyStatspending,
       "naKeyStatsselectors": naKeyStatsselectors,
       "naKeyStatsoutlast": naKeyStatsoutlast,
       "naKeyStatsouthash": naKeyStatsouthash,
       "naKeyStatsoutnew": naKeyStatsoutnew,
       "naKeyStatsinlast": naKeyStatsinlast,
       "naKeyStatsinhash": naKeyStatsinhash,
       "naKeyStatsrefresh": naKeyStatsrefresh,
       "naKeyStatsreaped": naKeyStatsreaped,
       "naKeyStatsreapedlarval": naKeyStatsreapedlarval,
       "naKeyStatsbypass": naKeyStatsbypass,
       "naKeyStatsdrop": naKeyStatsdrop,
       "naKeyStatsprotect": naKeyStatsprotect,
       "naKeyStatsinbypass": naKeyStatsinbypass,
       "naKeyStatsindrop": naKeyStatsindrop,
       "naKeyStatsinprotect": naKeyStatsinprotect,
       "naKeyStatsstallq": naKeyStatsstallq,
       "naKeyStatsnomatch": naKeyStatsnomatch,
       "naKeyStatsinnomatch": naKeyStatsinnomatch,
       "naKeyStatsinmismatch": naKeyStatsinmismatch,
       "naKeyStatsadvmtusent": naKeyStatsadvmtusent,
       "naKeyStatsadvmturcvd": naKeyStatsadvmturcvd,
       "naKeyStatsphantom": naKeyStatsphantom,
       "naKeyStatsdynamicselectors": naKeyStatsdynamicselectors,
       "naKeyStatstoolarge": naKeyStatstoolarge,
       "nokiaVPNIPSECMIB": nokiaVPNIPSECMIB}
)
