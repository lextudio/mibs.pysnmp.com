# SNMP MIB module (JUNIPER-IPv6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-IPv6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:11 2024
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

(ipv6IfEntry,) = mibBuilder.importSymbols(
    "IPV6-MIB",
    "ipv6IfEntry")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

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

jnxIpv6 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11)
)
jnxIpv6.setRevisions(
        ("2001-08-31 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxIpv6Stats_ObjectIdentity = ObjectIdentity
jnxIpv6Stats = _JnxIpv6Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1)
)
_JnxIpv6GlobalStats_ObjectIdentity = ObjectIdentity
jnxIpv6GlobalStats = _JnxIpv6GlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1)
)
_JnxIpv6StatsReceives_Type = Counter64
_JnxIpv6StatsReceives_Object = MibScalar
jnxIpv6StatsReceives = _JnxIpv6StatsReceives_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 1),
    _JnxIpv6StatsReceives_Type()
)
jnxIpv6StatsReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsReceives.setStatus("current")
_JnxIpv6StatsTooShorts_Type = Counter64
_JnxIpv6StatsTooShorts_Object = MibScalar
jnxIpv6StatsTooShorts = _JnxIpv6StatsTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 2),
    _JnxIpv6StatsTooShorts_Type()
)
jnxIpv6StatsTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsTooShorts.setStatus("current")
_JnxIpv6StatsTooSmalls_Type = Counter64
_JnxIpv6StatsTooSmalls_Object = MibScalar
jnxIpv6StatsTooSmalls = _JnxIpv6StatsTooSmalls_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 3),
    _JnxIpv6StatsTooSmalls_Type()
)
jnxIpv6StatsTooSmalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsTooSmalls.setStatus("current")
_JnxIpv6StatsBadOptions_Type = Counter64
_JnxIpv6StatsBadOptions_Object = MibScalar
jnxIpv6StatsBadOptions = _JnxIpv6StatsBadOptions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 4),
    _JnxIpv6StatsBadOptions_Type()
)
jnxIpv6StatsBadOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsBadOptions.setStatus("current")
_JnxIpv6StatsBadVersions_Type = Counter64
_JnxIpv6StatsBadVersions_Object = MibScalar
jnxIpv6StatsBadVersions = _JnxIpv6StatsBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 5),
    _JnxIpv6StatsBadVersions_Type()
)
jnxIpv6StatsBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsBadVersions.setStatus("current")
_JnxIpv6StatsFragments_Type = Counter64
_JnxIpv6StatsFragments_Object = MibScalar
jnxIpv6StatsFragments = _JnxIpv6StatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 6),
    _JnxIpv6StatsFragments_Type()
)
jnxIpv6StatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsFragments.setStatus("current")
_JnxIpv6StatsFragDrops_Type = Counter64
_JnxIpv6StatsFragDrops_Object = MibScalar
jnxIpv6StatsFragDrops = _JnxIpv6StatsFragDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 7),
    _JnxIpv6StatsFragDrops_Type()
)
jnxIpv6StatsFragDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsFragDrops.setStatus("current")
_JnxIpv6StatsFragTimeOuts_Type = Counter64
_JnxIpv6StatsFragTimeOuts_Object = MibScalar
jnxIpv6StatsFragTimeOuts = _JnxIpv6StatsFragTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 8),
    _JnxIpv6StatsFragTimeOuts_Type()
)
jnxIpv6StatsFragTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsFragTimeOuts.setStatus("current")
_JnxIpv6StatsFragOverFlows_Type = Counter64
_JnxIpv6StatsFragOverFlows_Object = MibScalar
jnxIpv6StatsFragOverFlows = _JnxIpv6StatsFragOverFlows_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 9),
    _JnxIpv6StatsFragOverFlows_Type()
)
jnxIpv6StatsFragOverFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsFragOverFlows.setStatus("current")
_JnxIpv6StatsReasmOKs_Type = Counter64
_JnxIpv6StatsReasmOKs_Object = MibScalar
jnxIpv6StatsReasmOKs = _JnxIpv6StatsReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 10),
    _JnxIpv6StatsReasmOKs_Type()
)
jnxIpv6StatsReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsReasmOKs.setStatus("current")
_JnxIpv6StatsDelivers_Type = Counter64
_JnxIpv6StatsDelivers_Object = MibScalar
jnxIpv6StatsDelivers = _JnxIpv6StatsDelivers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 11),
    _JnxIpv6StatsDelivers_Type()
)
jnxIpv6StatsDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsDelivers.setStatus("current")
_JnxIpv6StatsForwards_Type = Counter64
_JnxIpv6StatsForwards_Object = MibScalar
jnxIpv6StatsForwards = _JnxIpv6StatsForwards_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 12),
    _JnxIpv6StatsForwards_Type()
)
jnxIpv6StatsForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsForwards.setStatus("current")
_JnxIpv6StatsUnreachables_Type = Counter64
_JnxIpv6StatsUnreachables_Object = MibScalar
jnxIpv6StatsUnreachables = _JnxIpv6StatsUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 13),
    _JnxIpv6StatsUnreachables_Type()
)
jnxIpv6StatsUnreachables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsUnreachables.setStatus("current")
_JnxIpv6StatsRedirects_Type = Counter64
_JnxIpv6StatsRedirects_Object = MibScalar
jnxIpv6StatsRedirects = _JnxIpv6StatsRedirects_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 14),
    _JnxIpv6StatsRedirects_Type()
)
jnxIpv6StatsRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsRedirects.setStatus("current")
_JnxIpv6StatsOutRequests_Type = Counter64
_JnxIpv6StatsOutRequests_Object = MibScalar
jnxIpv6StatsOutRequests = _JnxIpv6StatsOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 15),
    _JnxIpv6StatsOutRequests_Type()
)
jnxIpv6StatsOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsOutRequests.setStatus("current")
_JnxIpv6StatsRawOuts_Type = Counter64
_JnxIpv6StatsRawOuts_Object = MibScalar
jnxIpv6StatsRawOuts = _JnxIpv6StatsRawOuts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 16),
    _JnxIpv6StatsRawOuts_Type()
)
jnxIpv6StatsRawOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsRawOuts.setStatus("current")
_JnxIpv6StatsOutDiscards_Type = Counter64
_JnxIpv6StatsOutDiscards_Object = MibScalar
jnxIpv6StatsOutDiscards = _JnxIpv6StatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 17),
    _JnxIpv6StatsOutDiscards_Type()
)
jnxIpv6StatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsOutDiscards.setStatus("current")
_JnxIpv6StatsOutNoRoutes_Type = Counter64
_JnxIpv6StatsOutNoRoutes_Object = MibScalar
jnxIpv6StatsOutNoRoutes = _JnxIpv6StatsOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 18),
    _JnxIpv6StatsOutNoRoutes_Type()
)
jnxIpv6StatsOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsOutNoRoutes.setStatus("current")
_JnxIpv6StatsOutFragOKs_Type = Counter64
_JnxIpv6StatsOutFragOKs_Object = MibScalar
jnxIpv6StatsOutFragOKs = _JnxIpv6StatsOutFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 19),
    _JnxIpv6StatsOutFragOKs_Type()
)
jnxIpv6StatsOutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsOutFragOKs.setStatus("current")
_JnxIpv6StatsOutFragCreates_Type = Counter64
_JnxIpv6StatsOutFragCreates_Object = MibScalar
jnxIpv6StatsOutFragCreates = _JnxIpv6StatsOutFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 20),
    _JnxIpv6StatsOutFragCreates_Type()
)
jnxIpv6StatsOutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsOutFragCreates.setStatus("current")
_JnxIpv6StatsOutFragFails_Type = Counter64
_JnxIpv6StatsOutFragFails_Object = MibScalar
jnxIpv6StatsOutFragFails = _JnxIpv6StatsOutFragFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 21),
    _JnxIpv6StatsOutFragFails_Type()
)
jnxIpv6StatsOutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsOutFragFails.setStatus("current")
_JnxIpv6StatsBadScopes_Type = Counter64
_JnxIpv6StatsBadScopes_Object = MibScalar
jnxIpv6StatsBadScopes = _JnxIpv6StatsBadScopes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 22),
    _JnxIpv6StatsBadScopes_Type()
)
jnxIpv6StatsBadScopes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsBadScopes.setStatus("current")
_JnxIpv6StatsNotMcastMembers_Type = Counter64
_JnxIpv6StatsNotMcastMembers_Object = MibScalar
jnxIpv6StatsNotMcastMembers = _JnxIpv6StatsNotMcastMembers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 23),
    _JnxIpv6StatsNotMcastMembers_Type()
)
jnxIpv6StatsNotMcastMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsNotMcastMembers.setStatus("current")
_JnxIpv6StatsHdrNotContinuous_Type = Counter64
_JnxIpv6StatsHdrNotContinuous_Object = MibScalar
jnxIpv6StatsHdrNotContinuous = _JnxIpv6StatsHdrNotContinuous_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 24),
    _JnxIpv6StatsHdrNotContinuous_Type()
)
jnxIpv6StatsHdrNotContinuous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsHdrNotContinuous.setStatus("current")
_JnxIpv6StatsNoGifs_Type = Counter64
_JnxIpv6StatsNoGifs_Object = MibScalar
jnxIpv6StatsNoGifs = _JnxIpv6StatsNoGifs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 25),
    _JnxIpv6StatsNoGifs_Type()
)
jnxIpv6StatsNoGifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsNoGifs.setStatus("current")
_JnxIpv6StatsTooManyHdrs_Type = Counter64
_JnxIpv6StatsTooManyHdrs_Object = MibScalar
jnxIpv6StatsTooManyHdrs = _JnxIpv6StatsTooManyHdrs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 26),
    _JnxIpv6StatsTooManyHdrs_Type()
)
jnxIpv6StatsTooManyHdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsTooManyHdrs.setStatus("current")
_JnxIpv6StatsForwCacheHits_Type = Counter64
_JnxIpv6StatsForwCacheHits_Object = MibScalar
jnxIpv6StatsForwCacheHits = _JnxIpv6StatsForwCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 27),
    _JnxIpv6StatsForwCacheHits_Type()
)
jnxIpv6StatsForwCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsForwCacheHits.setStatus("current")
_JnxIpv6StatsForwCacheMisses_Type = Counter64
_JnxIpv6StatsForwCacheMisses_Object = MibScalar
jnxIpv6StatsForwCacheMisses = _JnxIpv6StatsForwCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 28),
    _JnxIpv6StatsForwCacheMisses_Type()
)
jnxIpv6StatsForwCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsForwCacheMisses.setStatus("current")
_JnxIpv6StatsOutDeadNextHops_Type = Counter64
_JnxIpv6StatsOutDeadNextHops_Object = MibScalar
jnxIpv6StatsOutDeadNextHops = _JnxIpv6StatsOutDeadNextHops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 29),
    _JnxIpv6StatsOutDeadNextHops_Type()
)
jnxIpv6StatsOutDeadNextHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsOutDeadNextHops.setStatus("current")
_JnxIpv6StatsOptRateDrops_Type = Counter64
_JnxIpv6StatsOptRateDrops_Object = MibScalar
jnxIpv6StatsOptRateDrops = _JnxIpv6StatsOptRateDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 30),
    _JnxIpv6StatsOptRateDrops_Type()
)
jnxIpv6StatsOptRateDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsOptRateDrops.setStatus("current")
_JnxIpv6StatsMCNoDests_Type = Counter64
_JnxIpv6StatsMCNoDests_Object = MibScalar
jnxIpv6StatsMCNoDests = _JnxIpv6StatsMCNoDests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 31),
    _JnxIpv6StatsMCNoDests_Type()
)
jnxIpv6StatsMCNoDests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsMCNoDests.setStatus("current")
_JnxIpv6StatsInHopByHops_Type = Counter64
_JnxIpv6StatsInHopByHops_Object = MibScalar
jnxIpv6StatsInHopByHops = _JnxIpv6StatsInHopByHops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 32),
    _JnxIpv6StatsInHopByHops_Type()
)
jnxIpv6StatsInHopByHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInHopByHops.setStatus("current")
_JnxIpv6StatsInIcmps_Type = Counter64
_JnxIpv6StatsInIcmps_Object = MibScalar
jnxIpv6StatsInIcmps = _JnxIpv6StatsInIcmps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 33),
    _JnxIpv6StatsInIcmps_Type()
)
jnxIpv6StatsInIcmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInIcmps.setStatus("current")
_JnxIpv6StatsInIgmps_Type = Counter64
_JnxIpv6StatsInIgmps_Object = MibScalar
jnxIpv6StatsInIgmps = _JnxIpv6StatsInIgmps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 34),
    _JnxIpv6StatsInIgmps_Type()
)
jnxIpv6StatsInIgmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInIgmps.setStatus("current")
_JnxIpv6StatsInIps_Type = Counter64
_JnxIpv6StatsInIps_Object = MibScalar
jnxIpv6StatsInIps = _JnxIpv6StatsInIps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 35),
    _JnxIpv6StatsInIps_Type()
)
jnxIpv6StatsInIps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInIps.setStatus("current")
_JnxIpv6StatsInTcps_Type = Counter64
_JnxIpv6StatsInTcps_Object = MibScalar
jnxIpv6StatsInTcps = _JnxIpv6StatsInTcps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 36),
    _JnxIpv6StatsInTcps_Type()
)
jnxIpv6StatsInTcps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInTcps.setStatus("current")
_JnxIpv6StatsInUdps_Type = Counter64
_JnxIpv6StatsInUdps_Object = MibScalar
jnxIpv6StatsInUdps = _JnxIpv6StatsInUdps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 37),
    _JnxIpv6StatsInUdps_Type()
)
jnxIpv6StatsInUdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInUdps.setStatus("current")
_JnxIpv6StatsInIdps_Type = Counter64
_JnxIpv6StatsInIdps_Object = MibScalar
jnxIpv6StatsInIdps = _JnxIpv6StatsInIdps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 38),
    _JnxIpv6StatsInIdps_Type()
)
jnxIpv6StatsInIdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInIdps.setStatus("current")
_JnxIpv6StatsInTps_Type = Counter64
_JnxIpv6StatsInTps_Object = MibScalar
jnxIpv6StatsInTps = _JnxIpv6StatsInTps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 39),
    _JnxIpv6StatsInTps_Type()
)
jnxIpv6StatsInTps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInTps.setStatus("current")
_JnxIpv6StatsInIpv6s_Type = Counter64
_JnxIpv6StatsInIpv6s_Object = MibScalar
jnxIpv6StatsInIpv6s = _JnxIpv6StatsInIpv6s_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 40),
    _JnxIpv6StatsInIpv6s_Type()
)
jnxIpv6StatsInIpv6s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInIpv6s.setStatus("current")
_JnxIpv6StatsInRoutings_Type = Counter64
_JnxIpv6StatsInRoutings_Object = MibScalar
jnxIpv6StatsInRoutings = _JnxIpv6StatsInRoutings_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 41),
    _JnxIpv6StatsInRoutings_Type()
)
jnxIpv6StatsInRoutings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInRoutings.setStatus("current")
_JnxIpv6StatsInFrags_Type = Counter64
_JnxIpv6StatsInFrags_Object = MibScalar
jnxIpv6StatsInFrags = _JnxIpv6StatsInFrags_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 42),
    _JnxIpv6StatsInFrags_Type()
)
jnxIpv6StatsInFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInFrags.setStatus("current")
_JnxIpv6StatsInEsps_Type = Counter64
_JnxIpv6StatsInEsps_Object = MibScalar
jnxIpv6StatsInEsps = _JnxIpv6StatsInEsps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 43),
    _JnxIpv6StatsInEsps_Type()
)
jnxIpv6StatsInEsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInEsps.setStatus("current")
_JnxIpv6StatsInAhs_Type = Counter64
_JnxIpv6StatsInAhs_Object = MibScalar
jnxIpv6StatsInAhs = _JnxIpv6StatsInAhs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 44),
    _JnxIpv6StatsInAhs_Type()
)
jnxIpv6StatsInAhs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInAhs.setStatus("current")
_JnxIpv6StatsInIcmpv6s_Type = Counter64
_JnxIpv6StatsInIcmpv6s_Object = MibScalar
jnxIpv6StatsInIcmpv6s = _JnxIpv6StatsInIcmpv6s_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 45),
    _JnxIpv6StatsInIcmpv6s_Type()
)
jnxIpv6StatsInIcmpv6s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInIcmpv6s.setStatus("current")
_JnxIpv6StatsInNoNhs_Type = Counter64
_JnxIpv6StatsInNoNhs_Object = MibScalar
jnxIpv6StatsInNoNhs = _JnxIpv6StatsInNoNhs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 46),
    _JnxIpv6StatsInNoNhs_Type()
)
jnxIpv6StatsInNoNhs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInNoNhs.setStatus("current")
_JnxIpv6StatsInDestOpts_Type = Counter64
_JnxIpv6StatsInDestOpts_Object = MibScalar
jnxIpv6StatsInDestOpts = _JnxIpv6StatsInDestOpts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 47),
    _JnxIpv6StatsInDestOpts_Type()
)
jnxIpv6StatsInDestOpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInDestOpts.setStatus("current")
_JnxIpv6StatsInIsoIps_Type = Counter64
_JnxIpv6StatsInIsoIps_Object = MibScalar
jnxIpv6StatsInIsoIps = _JnxIpv6StatsInIsoIps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 48),
    _JnxIpv6StatsInIsoIps_Type()
)
jnxIpv6StatsInIsoIps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInIsoIps.setStatus("current")
_JnxIpv6StatsInOspfs_Type = Counter64
_JnxIpv6StatsInOspfs_Object = MibScalar
jnxIpv6StatsInOspfs = _JnxIpv6StatsInOspfs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 49),
    _JnxIpv6StatsInOspfs_Type()
)
jnxIpv6StatsInOspfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInOspfs.setStatus("current")
_JnxIpv6StatsInEths_Type = Counter64
_JnxIpv6StatsInEths_Object = MibScalar
jnxIpv6StatsInEths = _JnxIpv6StatsInEths_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 50),
    _JnxIpv6StatsInEths_Type()
)
jnxIpv6StatsInEths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInEths.setStatus("current")
_JnxIpv6StatsInPims_Type = Counter64
_JnxIpv6StatsInPims_Object = MibScalar
jnxIpv6StatsInPims = _JnxIpv6StatsInPims_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 51),
    _JnxIpv6StatsInPims_Type()
)
jnxIpv6StatsInPims.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6StatsInPims.setStatus("current")
_JnxIcmpv6GlobalStats_ObjectIdentity = ObjectIdentity
jnxIcmpv6GlobalStats = _JnxIcmpv6GlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2)
)
_JnxIcmpv6StatsErrors_Type = Counter64
_JnxIcmpv6StatsErrors_Object = MibScalar
jnxIcmpv6StatsErrors = _JnxIcmpv6StatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 1),
    _JnxIcmpv6StatsErrors_Type()
)
jnxIcmpv6StatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsErrors.setStatus("current")
_JnxIcmpv6StatsCantErrors_Type = Counter64
_JnxIcmpv6StatsCantErrors_Object = MibScalar
jnxIcmpv6StatsCantErrors = _JnxIcmpv6StatsCantErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 2),
    _JnxIcmpv6StatsCantErrors_Type()
)
jnxIcmpv6StatsCantErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsCantErrors.setStatus("current")
_JnxIcmpv6StatsTooFreqs_Type = Counter64
_JnxIcmpv6StatsTooFreqs_Object = MibScalar
jnxIcmpv6StatsTooFreqs = _JnxIcmpv6StatsTooFreqs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 3),
    _JnxIcmpv6StatsTooFreqs_Type()
)
jnxIcmpv6StatsTooFreqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsTooFreqs.setStatus("current")
_JnxIcmpv6StatsBadCodes_Type = Counter64
_JnxIcmpv6StatsBadCodes_Object = MibScalar
jnxIcmpv6StatsBadCodes = _JnxIcmpv6StatsBadCodes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 4),
    _JnxIcmpv6StatsBadCodes_Type()
)
jnxIcmpv6StatsBadCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsBadCodes.setStatus("current")
_JnxIcmpv6StatsTooShorts_Type = Counter64
_JnxIcmpv6StatsTooShorts_Object = MibScalar
jnxIcmpv6StatsTooShorts = _JnxIcmpv6StatsTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 5),
    _JnxIcmpv6StatsTooShorts_Type()
)
jnxIcmpv6StatsTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsTooShorts.setStatus("current")
_JnxIcmpv6StatsBadChecksums_Type = Counter64
_JnxIcmpv6StatsBadChecksums_Object = MibScalar
jnxIcmpv6StatsBadChecksums = _JnxIcmpv6StatsBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 6),
    _JnxIcmpv6StatsBadChecksums_Type()
)
jnxIcmpv6StatsBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsBadChecksums.setStatus("current")
_JnxIcmpv6StatsBadLenths_Type = Counter64
_JnxIcmpv6StatsBadLenths_Object = MibScalar
jnxIcmpv6StatsBadLenths = _JnxIcmpv6StatsBadLenths_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 7),
    _JnxIcmpv6StatsBadLenths_Type()
)
jnxIcmpv6StatsBadLenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsBadLenths.setStatus("current")
_JnxIcmpv6StatsNoRoutes_Type = Counter64
_JnxIcmpv6StatsNoRoutes_Object = MibScalar
jnxIcmpv6StatsNoRoutes = _JnxIcmpv6StatsNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 8),
    _JnxIcmpv6StatsNoRoutes_Type()
)
jnxIcmpv6StatsNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsNoRoutes.setStatus("current")
_JnxIcmpv6StatsAdminProhibits_Type = Counter64
_JnxIcmpv6StatsAdminProhibits_Object = MibScalar
jnxIcmpv6StatsAdminProhibits = _JnxIcmpv6StatsAdminProhibits_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 9),
    _JnxIcmpv6StatsAdminProhibits_Type()
)
jnxIcmpv6StatsAdminProhibits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsAdminProhibits.setStatus("current")
_JnxIcmpv6StatsBeyondScopes_Type = Counter64
_JnxIcmpv6StatsBeyondScopes_Object = MibScalar
jnxIcmpv6StatsBeyondScopes = _JnxIcmpv6StatsBeyondScopes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 10),
    _JnxIcmpv6StatsBeyondScopes_Type()
)
jnxIcmpv6StatsBeyondScopes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsBeyondScopes.setStatus("current")
_JnxIcmpv6StatsAddrUnreachs_Type = Counter64
_JnxIcmpv6StatsAddrUnreachs_Object = MibScalar
jnxIcmpv6StatsAddrUnreachs = _JnxIcmpv6StatsAddrUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 11),
    _JnxIcmpv6StatsAddrUnreachs_Type()
)
jnxIcmpv6StatsAddrUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsAddrUnreachs.setStatus("current")
_JnxIcmpv6StatsPortUnreachs_Type = Counter64
_JnxIcmpv6StatsPortUnreachs_Object = MibScalar
jnxIcmpv6StatsPortUnreachs = _JnxIcmpv6StatsPortUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 12),
    _JnxIcmpv6StatsPortUnreachs_Type()
)
jnxIcmpv6StatsPortUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsPortUnreachs.setStatus("current")
_JnxIcmpv6StatsTooBigs_Type = Counter64
_JnxIcmpv6StatsTooBigs_Object = MibScalar
jnxIcmpv6StatsTooBigs = _JnxIcmpv6StatsTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 13),
    _JnxIcmpv6StatsTooBigs_Type()
)
jnxIcmpv6StatsTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsTooBigs.setStatus("current")
_JnxIcmpv6StatsExceedTrans_Type = Counter64
_JnxIcmpv6StatsExceedTrans_Object = MibScalar
jnxIcmpv6StatsExceedTrans = _JnxIcmpv6StatsExceedTrans_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 14),
    _JnxIcmpv6StatsExceedTrans_Type()
)
jnxIcmpv6StatsExceedTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsExceedTrans.setStatus("current")
_JnxIcmpv6StatsExceedReasms_Type = Counter64
_JnxIcmpv6StatsExceedReasms_Object = MibScalar
jnxIcmpv6StatsExceedReasms = _JnxIcmpv6StatsExceedReasms_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 15),
    _JnxIcmpv6StatsExceedReasms_Type()
)
jnxIcmpv6StatsExceedReasms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsExceedReasms.setStatus("current")
_JnxIcmpv6StatsBadHdrFields_Type = Counter64
_JnxIcmpv6StatsBadHdrFields_Object = MibScalar
jnxIcmpv6StatsBadHdrFields = _JnxIcmpv6StatsBadHdrFields_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 16),
    _JnxIcmpv6StatsBadHdrFields_Type()
)
jnxIcmpv6StatsBadHdrFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsBadHdrFields.setStatus("current")
_JnxIcmpv6StatsBadNextHdrs_Type = Counter64
_JnxIcmpv6StatsBadNextHdrs_Object = MibScalar
jnxIcmpv6StatsBadNextHdrs = _JnxIcmpv6StatsBadNextHdrs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 17),
    _JnxIcmpv6StatsBadNextHdrs_Type()
)
jnxIcmpv6StatsBadNextHdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsBadNextHdrs.setStatus("current")
_JnxIcmpv6StatsBadOptions_Type = Counter64
_JnxIcmpv6StatsBadOptions_Object = MibScalar
jnxIcmpv6StatsBadOptions = _JnxIcmpv6StatsBadOptions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 18),
    _JnxIcmpv6StatsBadOptions_Type()
)
jnxIcmpv6StatsBadOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsBadOptions.setStatus("current")
_JnxIcmpv6StatsRedirects_Type = Counter64
_JnxIcmpv6StatsRedirects_Object = MibScalar
jnxIcmpv6StatsRedirects = _JnxIcmpv6StatsRedirects_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 19),
    _JnxIcmpv6StatsRedirects_Type()
)
jnxIcmpv6StatsRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsRedirects.setStatus("current")
_JnxIcmpv6StatsOthers_Type = Counter64
_JnxIcmpv6StatsOthers_Object = MibScalar
jnxIcmpv6StatsOthers = _JnxIcmpv6StatsOthers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 20),
    _JnxIcmpv6StatsOthers_Type()
)
jnxIcmpv6StatsOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOthers.setStatus("current")
_JnxIcmpv6StatsResponses_Type = Counter64
_JnxIcmpv6StatsResponses_Object = MibScalar
jnxIcmpv6StatsResponses = _JnxIcmpv6StatsResponses_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 21),
    _JnxIcmpv6StatsResponses_Type()
)
jnxIcmpv6StatsResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsResponses.setStatus("current")
_JnxIcmpv6StatsExcessNDOptions_Type = Counter64
_JnxIcmpv6StatsExcessNDOptions_Object = MibScalar
jnxIcmpv6StatsExcessNDOptions = _JnxIcmpv6StatsExcessNDOptions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 22),
    _JnxIcmpv6StatsExcessNDOptions_Type()
)
jnxIcmpv6StatsExcessNDOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsExcessNDOptions.setStatus("current")
_JnxIcmpv6StatsInUnreachables_Type = Counter64
_JnxIcmpv6StatsInUnreachables_Object = MibScalar
jnxIcmpv6StatsInUnreachables = _JnxIcmpv6StatsInUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 23),
    _JnxIcmpv6StatsInUnreachables_Type()
)
jnxIcmpv6StatsInUnreachables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsInUnreachables.setStatus("current")
_JnxIcmpv6StatsInPktTooBigs_Type = Counter64
_JnxIcmpv6StatsInPktTooBigs_Object = MibScalar
jnxIcmpv6StatsInPktTooBigs = _JnxIcmpv6StatsInPktTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 24),
    _JnxIcmpv6StatsInPktTooBigs_Type()
)
jnxIcmpv6StatsInPktTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsInPktTooBigs.setStatus("current")
_JnxIcmpv6StatsInTimeExceeds_Type = Counter64
_JnxIcmpv6StatsInTimeExceeds_Object = MibScalar
jnxIcmpv6StatsInTimeExceeds = _JnxIcmpv6StatsInTimeExceeds_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 25),
    _JnxIcmpv6StatsInTimeExceeds_Type()
)
jnxIcmpv6StatsInTimeExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsInTimeExceeds.setStatus("current")
_JnxIcmpv6StatsInParamProbs_Type = Counter64
_JnxIcmpv6StatsInParamProbs_Object = MibScalar
jnxIcmpv6StatsInParamProbs = _JnxIcmpv6StatsInParamProbs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 26),
    _JnxIcmpv6StatsInParamProbs_Type()
)
jnxIcmpv6StatsInParamProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsInParamProbs.setStatus("current")
_JnxIcmpv6StatsInEchoReqs_Type = Counter64
_JnxIcmpv6StatsInEchoReqs_Object = MibScalar
jnxIcmpv6StatsInEchoReqs = _JnxIcmpv6StatsInEchoReqs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 27),
    _JnxIcmpv6StatsInEchoReqs_Type()
)
jnxIcmpv6StatsInEchoReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsInEchoReqs.setStatus("current")
_JnxIcmpv6StatsInEchoReplies_Type = Counter64
_JnxIcmpv6StatsInEchoReplies_Object = MibScalar
jnxIcmpv6StatsInEchoReplies = _JnxIcmpv6StatsInEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 28),
    _JnxIcmpv6StatsInEchoReplies_Type()
)
jnxIcmpv6StatsInEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsInEchoReplies.setStatus("current")
_JnxIcmpv6StatsInMLQueries_Type = Counter64
_JnxIcmpv6StatsInMLQueries_Object = MibScalar
jnxIcmpv6StatsInMLQueries = _JnxIcmpv6StatsInMLQueries_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 29),
    _JnxIcmpv6StatsInMLQueries_Type()
)
jnxIcmpv6StatsInMLQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsInMLQueries.setStatus("current")
_JnxIcmpv6StatsInMLReports_Type = Counter64
_JnxIcmpv6StatsInMLReports_Object = MibScalar
jnxIcmpv6StatsInMLReports = _JnxIcmpv6StatsInMLReports_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 30),
    _JnxIcmpv6StatsInMLReports_Type()
)
jnxIcmpv6StatsInMLReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsInMLReports.setStatus("current")
_JnxIcmpv6StatsInMLDones_Type = Counter64
_JnxIcmpv6StatsInMLDones_Object = MibScalar
jnxIcmpv6StatsInMLDones = _JnxIcmpv6StatsInMLDones_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 31),
    _JnxIcmpv6StatsInMLDones_Type()
)
jnxIcmpv6StatsInMLDones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsInMLDones.setStatus("current")
_JnxIcmpv6StatsInRtrSolicits_Type = Counter64
_JnxIcmpv6StatsInRtrSolicits_Object = MibScalar
jnxIcmpv6StatsInRtrSolicits = _JnxIcmpv6StatsInRtrSolicits_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 32),
    _JnxIcmpv6StatsInRtrSolicits_Type()
)
jnxIcmpv6StatsInRtrSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsInRtrSolicits.setStatus("current")
_JnxIcmpv6StatsInRtrAdvs_Type = Counter64
_JnxIcmpv6StatsInRtrAdvs_Object = MibScalar
jnxIcmpv6StatsInRtrAdvs = _JnxIcmpv6StatsInRtrAdvs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 33),
    _JnxIcmpv6StatsInRtrAdvs_Type()
)
jnxIcmpv6StatsInRtrAdvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsInRtrAdvs.setStatus("current")
_JnxIcmpv6StatsInNbrSolicits_Type = Counter64
_JnxIcmpv6StatsInNbrSolicits_Object = MibScalar
jnxIcmpv6StatsInNbrSolicits = _JnxIcmpv6StatsInNbrSolicits_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 34),
    _JnxIcmpv6StatsInNbrSolicits_Type()
)
jnxIcmpv6StatsInNbrSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsInNbrSolicits.setStatus("current")
_JnxIcmpv6StatsInNbrAdvs_Type = Counter64
_JnxIcmpv6StatsInNbrAdvs_Object = MibScalar
jnxIcmpv6StatsInNbrAdvs = _JnxIcmpv6StatsInNbrAdvs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 35),
    _JnxIcmpv6StatsInNbrAdvs_Type()
)
jnxIcmpv6StatsInNbrAdvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsInNbrAdvs.setStatus("current")
_JnxIcmpv6StatsInRedirects_Type = Counter64
_JnxIcmpv6StatsInRedirects_Object = MibScalar
jnxIcmpv6StatsInRedirects = _JnxIcmpv6StatsInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 36),
    _JnxIcmpv6StatsInRedirects_Type()
)
jnxIcmpv6StatsInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsInRedirects.setStatus("current")
_JnxIcmpv6StatsInRtrRenumbers_Type = Counter64
_JnxIcmpv6StatsInRtrRenumbers_Object = MibScalar
jnxIcmpv6StatsInRtrRenumbers = _JnxIcmpv6StatsInRtrRenumbers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 37),
    _JnxIcmpv6StatsInRtrRenumbers_Type()
)
jnxIcmpv6StatsInRtrRenumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsInRtrRenumbers.setStatus("current")
_JnxIcmpv6StatsInNIReqs_Type = Counter64
_JnxIcmpv6StatsInNIReqs_Object = MibScalar
jnxIcmpv6StatsInNIReqs = _JnxIcmpv6StatsInNIReqs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 38),
    _JnxIcmpv6StatsInNIReqs_Type()
)
jnxIcmpv6StatsInNIReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsInNIReqs.setStatus("current")
_JnxIcmpv6StatsInNIReplies_Type = Counter64
_JnxIcmpv6StatsInNIReplies_Object = MibScalar
jnxIcmpv6StatsInNIReplies = _JnxIcmpv6StatsInNIReplies_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 39),
    _JnxIcmpv6StatsInNIReplies_Type()
)
jnxIcmpv6StatsInNIReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsInNIReplies.setStatus("current")
_JnxIcmpv6StatsOutUnreachables_Type = Counter64
_JnxIcmpv6StatsOutUnreachables_Object = MibScalar
jnxIcmpv6StatsOutUnreachables = _JnxIcmpv6StatsOutUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 40),
    _JnxIcmpv6StatsOutUnreachables_Type()
)
jnxIcmpv6StatsOutUnreachables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOutUnreachables.setStatus("current")
_JnxIcmpv6StatsOutPktTooBigs_Type = Counter64
_JnxIcmpv6StatsOutPktTooBigs_Object = MibScalar
jnxIcmpv6StatsOutPktTooBigs = _JnxIcmpv6StatsOutPktTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 41),
    _JnxIcmpv6StatsOutPktTooBigs_Type()
)
jnxIcmpv6StatsOutPktTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOutPktTooBigs.setStatus("current")
_JnxIcmpv6StatsOutTimeExceeds_Type = Counter64
_JnxIcmpv6StatsOutTimeExceeds_Object = MibScalar
jnxIcmpv6StatsOutTimeExceeds = _JnxIcmpv6StatsOutTimeExceeds_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 42),
    _JnxIcmpv6StatsOutTimeExceeds_Type()
)
jnxIcmpv6StatsOutTimeExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOutTimeExceeds.setStatus("current")
_JnxIcmpv6StatsOutParamProbs_Type = Counter64
_JnxIcmpv6StatsOutParamProbs_Object = MibScalar
jnxIcmpv6StatsOutParamProbs = _JnxIcmpv6StatsOutParamProbs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 43),
    _JnxIcmpv6StatsOutParamProbs_Type()
)
jnxIcmpv6StatsOutParamProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOutParamProbs.setStatus("current")
_JnxIcmpv6StatsOutEchoReqs_Type = Counter64
_JnxIcmpv6StatsOutEchoReqs_Object = MibScalar
jnxIcmpv6StatsOutEchoReqs = _JnxIcmpv6StatsOutEchoReqs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 44),
    _JnxIcmpv6StatsOutEchoReqs_Type()
)
jnxIcmpv6StatsOutEchoReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOutEchoReqs.setStatus("current")
_JnxIcmpv6StatsOutEchoReplies_Type = Counter64
_JnxIcmpv6StatsOutEchoReplies_Object = MibScalar
jnxIcmpv6StatsOutEchoReplies = _JnxIcmpv6StatsOutEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 45),
    _JnxIcmpv6StatsOutEchoReplies_Type()
)
jnxIcmpv6StatsOutEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOutEchoReplies.setStatus("current")
_JnxIcmpv6StatsOutMLQueries_Type = Counter64
_JnxIcmpv6StatsOutMLQueries_Object = MibScalar
jnxIcmpv6StatsOutMLQueries = _JnxIcmpv6StatsOutMLQueries_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 46),
    _JnxIcmpv6StatsOutMLQueries_Type()
)
jnxIcmpv6StatsOutMLQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOutMLQueries.setStatus("current")
_JnxIcmpv6StatsOutMLReports_Type = Counter64
_JnxIcmpv6StatsOutMLReports_Object = MibScalar
jnxIcmpv6StatsOutMLReports = _JnxIcmpv6StatsOutMLReports_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 47),
    _JnxIcmpv6StatsOutMLReports_Type()
)
jnxIcmpv6StatsOutMLReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOutMLReports.setStatus("current")
_JnxIcmpv6StatsOutMLDones_Type = Counter64
_JnxIcmpv6StatsOutMLDones_Object = MibScalar
jnxIcmpv6StatsOutMLDones = _JnxIcmpv6StatsOutMLDones_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 48),
    _JnxIcmpv6StatsOutMLDones_Type()
)
jnxIcmpv6StatsOutMLDones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOutMLDones.setStatus("current")
_JnxIcmpv6StatsOutRtrSolicits_Type = Counter64
_JnxIcmpv6StatsOutRtrSolicits_Object = MibScalar
jnxIcmpv6StatsOutRtrSolicits = _JnxIcmpv6StatsOutRtrSolicits_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 49),
    _JnxIcmpv6StatsOutRtrSolicits_Type()
)
jnxIcmpv6StatsOutRtrSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOutRtrSolicits.setStatus("current")
_JnxIcmpv6StatsOutRtrAdvs_Type = Counter64
_JnxIcmpv6StatsOutRtrAdvs_Object = MibScalar
jnxIcmpv6StatsOutRtrAdvs = _JnxIcmpv6StatsOutRtrAdvs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 50),
    _JnxIcmpv6StatsOutRtrAdvs_Type()
)
jnxIcmpv6StatsOutRtrAdvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOutRtrAdvs.setStatus("current")
_JnxIcmpv6StatsOutNbrSolicits_Type = Counter64
_JnxIcmpv6StatsOutNbrSolicits_Object = MibScalar
jnxIcmpv6StatsOutNbrSolicits = _JnxIcmpv6StatsOutNbrSolicits_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 51),
    _JnxIcmpv6StatsOutNbrSolicits_Type()
)
jnxIcmpv6StatsOutNbrSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOutNbrSolicits.setStatus("current")
_JnxIcmpv6StatsOutNbrAdvs_Type = Counter64
_JnxIcmpv6StatsOutNbrAdvs_Object = MibScalar
jnxIcmpv6StatsOutNbrAdvs = _JnxIcmpv6StatsOutNbrAdvs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 52),
    _JnxIcmpv6StatsOutNbrAdvs_Type()
)
jnxIcmpv6StatsOutNbrAdvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOutNbrAdvs.setStatus("current")
_JnxIcmpv6StatsOutRedirects_Type = Counter64
_JnxIcmpv6StatsOutRedirects_Object = MibScalar
jnxIcmpv6StatsOutRedirects = _JnxIcmpv6StatsOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 53),
    _JnxIcmpv6StatsOutRedirects_Type()
)
jnxIcmpv6StatsOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOutRedirects.setStatus("current")
_JnxIcmpv6StatsOutRtrRenumbers_Type = Counter64
_JnxIcmpv6StatsOutRtrRenumbers_Object = MibScalar
jnxIcmpv6StatsOutRtrRenumbers = _JnxIcmpv6StatsOutRtrRenumbers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 54),
    _JnxIcmpv6StatsOutRtrRenumbers_Type()
)
jnxIcmpv6StatsOutRtrRenumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOutRtrRenumbers.setStatus("current")
_JnxIcmpv6StatsOutNIReqs_Type = Counter64
_JnxIcmpv6StatsOutNIReqs_Object = MibScalar
jnxIcmpv6StatsOutNIReqs = _JnxIcmpv6StatsOutNIReqs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 55),
    _JnxIcmpv6StatsOutNIReqs_Type()
)
jnxIcmpv6StatsOutNIReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOutNIReqs.setStatus("current")
_JnxIcmpv6StatsOutNIReplies_Type = Counter64
_JnxIcmpv6StatsOutNIReplies_Object = MibScalar
jnxIcmpv6StatsOutNIReplies = _JnxIcmpv6StatsOutNIReplies_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 56),
    _JnxIcmpv6StatsOutNIReplies_Type()
)
jnxIcmpv6StatsOutNIReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIcmpv6StatsOutNIReplies.setStatus("current")
_JnxIpv6IfStats_ObjectIdentity = ObjectIdentity
jnxIpv6IfStats = _JnxIpv6IfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 3)
)
_JnxIpv6IfStatsTable_Object = MibTable
jnxIpv6IfStatsTable = _JnxIpv6IfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jnxIpv6IfStatsTable.setStatus("current")
_JnxIpv6IfStatsEntry_Object = MibTableRow
jnxIpv6IfStatsEntry = _JnxIpv6IfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    jnxIpv6IfStatsEntry.setStatus("current")
_JnxIpv6IfInOctets_Type = Counter64
_JnxIpv6IfInOctets_Object = MibTableColumn
jnxIpv6IfInOctets = _JnxIpv6IfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 3, 1, 1, 1),
    _JnxIpv6IfInOctets_Type()
)
jnxIpv6IfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6IfInOctets.setStatus("current")
_JnxIpv6IfOutOctets_Type = Counter64
_JnxIpv6IfOutOctets_Object = MibTableColumn
jnxIpv6IfOutOctets = _JnxIpv6IfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 3, 1, 1, 2),
    _JnxIpv6IfOutOctets_Type()
)
jnxIpv6IfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpv6IfOutOctets.setStatus("current")
ipv6IfEntry.registerAugmentions(
    ("JUNIPER-IPv6-MIB",
     "jnxIpv6IfStatsEntry")
)
jnxIpv6IfStatsEntry.setIndexNames(*ipv6IfEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-IPv6-MIB",
    **{"jnxIpv6": jnxIpv6,
       "jnxIpv6Stats": jnxIpv6Stats,
       "jnxIpv6GlobalStats": jnxIpv6GlobalStats,
       "jnxIpv6StatsReceives": jnxIpv6StatsReceives,
       "jnxIpv6StatsTooShorts": jnxIpv6StatsTooShorts,
       "jnxIpv6StatsTooSmalls": jnxIpv6StatsTooSmalls,
       "jnxIpv6StatsBadOptions": jnxIpv6StatsBadOptions,
       "jnxIpv6StatsBadVersions": jnxIpv6StatsBadVersions,
       "jnxIpv6StatsFragments": jnxIpv6StatsFragments,
       "jnxIpv6StatsFragDrops": jnxIpv6StatsFragDrops,
       "jnxIpv6StatsFragTimeOuts": jnxIpv6StatsFragTimeOuts,
       "jnxIpv6StatsFragOverFlows": jnxIpv6StatsFragOverFlows,
       "jnxIpv6StatsReasmOKs": jnxIpv6StatsReasmOKs,
       "jnxIpv6StatsDelivers": jnxIpv6StatsDelivers,
       "jnxIpv6StatsForwards": jnxIpv6StatsForwards,
       "jnxIpv6StatsUnreachables": jnxIpv6StatsUnreachables,
       "jnxIpv6StatsRedirects": jnxIpv6StatsRedirects,
       "jnxIpv6StatsOutRequests": jnxIpv6StatsOutRequests,
       "jnxIpv6StatsRawOuts": jnxIpv6StatsRawOuts,
       "jnxIpv6StatsOutDiscards": jnxIpv6StatsOutDiscards,
       "jnxIpv6StatsOutNoRoutes": jnxIpv6StatsOutNoRoutes,
       "jnxIpv6StatsOutFragOKs": jnxIpv6StatsOutFragOKs,
       "jnxIpv6StatsOutFragCreates": jnxIpv6StatsOutFragCreates,
       "jnxIpv6StatsOutFragFails": jnxIpv6StatsOutFragFails,
       "jnxIpv6StatsBadScopes": jnxIpv6StatsBadScopes,
       "jnxIpv6StatsNotMcastMembers": jnxIpv6StatsNotMcastMembers,
       "jnxIpv6StatsHdrNotContinuous": jnxIpv6StatsHdrNotContinuous,
       "jnxIpv6StatsNoGifs": jnxIpv6StatsNoGifs,
       "jnxIpv6StatsTooManyHdrs": jnxIpv6StatsTooManyHdrs,
       "jnxIpv6StatsForwCacheHits": jnxIpv6StatsForwCacheHits,
       "jnxIpv6StatsForwCacheMisses": jnxIpv6StatsForwCacheMisses,
       "jnxIpv6StatsOutDeadNextHops": jnxIpv6StatsOutDeadNextHops,
       "jnxIpv6StatsOptRateDrops": jnxIpv6StatsOptRateDrops,
       "jnxIpv6StatsMCNoDests": jnxIpv6StatsMCNoDests,
       "jnxIpv6StatsInHopByHops": jnxIpv6StatsInHopByHops,
       "jnxIpv6StatsInIcmps": jnxIpv6StatsInIcmps,
       "jnxIpv6StatsInIgmps": jnxIpv6StatsInIgmps,
       "jnxIpv6StatsInIps": jnxIpv6StatsInIps,
       "jnxIpv6StatsInTcps": jnxIpv6StatsInTcps,
       "jnxIpv6StatsInUdps": jnxIpv6StatsInUdps,
       "jnxIpv6StatsInIdps": jnxIpv6StatsInIdps,
       "jnxIpv6StatsInTps": jnxIpv6StatsInTps,
       "jnxIpv6StatsInIpv6s": jnxIpv6StatsInIpv6s,
       "jnxIpv6StatsInRoutings": jnxIpv6StatsInRoutings,
       "jnxIpv6StatsInFrags": jnxIpv6StatsInFrags,
       "jnxIpv6StatsInEsps": jnxIpv6StatsInEsps,
       "jnxIpv6StatsInAhs": jnxIpv6StatsInAhs,
       "jnxIpv6StatsInIcmpv6s": jnxIpv6StatsInIcmpv6s,
       "jnxIpv6StatsInNoNhs": jnxIpv6StatsInNoNhs,
       "jnxIpv6StatsInDestOpts": jnxIpv6StatsInDestOpts,
       "jnxIpv6StatsInIsoIps": jnxIpv6StatsInIsoIps,
       "jnxIpv6StatsInOspfs": jnxIpv6StatsInOspfs,
       "jnxIpv6StatsInEths": jnxIpv6StatsInEths,
       "jnxIpv6StatsInPims": jnxIpv6StatsInPims,
       "jnxIcmpv6GlobalStats": jnxIcmpv6GlobalStats,
       "jnxIcmpv6StatsErrors": jnxIcmpv6StatsErrors,
       "jnxIcmpv6StatsCantErrors": jnxIcmpv6StatsCantErrors,
       "jnxIcmpv6StatsTooFreqs": jnxIcmpv6StatsTooFreqs,
       "jnxIcmpv6StatsBadCodes": jnxIcmpv6StatsBadCodes,
       "jnxIcmpv6StatsTooShorts": jnxIcmpv6StatsTooShorts,
       "jnxIcmpv6StatsBadChecksums": jnxIcmpv6StatsBadChecksums,
       "jnxIcmpv6StatsBadLenths": jnxIcmpv6StatsBadLenths,
       "jnxIcmpv6StatsNoRoutes": jnxIcmpv6StatsNoRoutes,
       "jnxIcmpv6StatsAdminProhibits": jnxIcmpv6StatsAdminProhibits,
       "jnxIcmpv6StatsBeyondScopes": jnxIcmpv6StatsBeyondScopes,
       "jnxIcmpv6StatsAddrUnreachs": jnxIcmpv6StatsAddrUnreachs,
       "jnxIcmpv6StatsPortUnreachs": jnxIcmpv6StatsPortUnreachs,
       "jnxIcmpv6StatsTooBigs": jnxIcmpv6StatsTooBigs,
       "jnxIcmpv6StatsExceedTrans": jnxIcmpv6StatsExceedTrans,
       "jnxIcmpv6StatsExceedReasms": jnxIcmpv6StatsExceedReasms,
       "jnxIcmpv6StatsBadHdrFields": jnxIcmpv6StatsBadHdrFields,
       "jnxIcmpv6StatsBadNextHdrs": jnxIcmpv6StatsBadNextHdrs,
       "jnxIcmpv6StatsBadOptions": jnxIcmpv6StatsBadOptions,
       "jnxIcmpv6StatsRedirects": jnxIcmpv6StatsRedirects,
       "jnxIcmpv6StatsOthers": jnxIcmpv6StatsOthers,
       "jnxIcmpv6StatsResponses": jnxIcmpv6StatsResponses,
       "jnxIcmpv6StatsExcessNDOptions": jnxIcmpv6StatsExcessNDOptions,
       "jnxIcmpv6StatsInUnreachables": jnxIcmpv6StatsInUnreachables,
       "jnxIcmpv6StatsInPktTooBigs": jnxIcmpv6StatsInPktTooBigs,
       "jnxIcmpv6StatsInTimeExceeds": jnxIcmpv6StatsInTimeExceeds,
       "jnxIcmpv6StatsInParamProbs": jnxIcmpv6StatsInParamProbs,
       "jnxIcmpv6StatsInEchoReqs": jnxIcmpv6StatsInEchoReqs,
       "jnxIcmpv6StatsInEchoReplies": jnxIcmpv6StatsInEchoReplies,
       "jnxIcmpv6StatsInMLQueries": jnxIcmpv6StatsInMLQueries,
       "jnxIcmpv6StatsInMLReports": jnxIcmpv6StatsInMLReports,
       "jnxIcmpv6StatsInMLDones": jnxIcmpv6StatsInMLDones,
       "jnxIcmpv6StatsInRtrSolicits": jnxIcmpv6StatsInRtrSolicits,
       "jnxIcmpv6StatsInRtrAdvs": jnxIcmpv6StatsInRtrAdvs,
       "jnxIcmpv6StatsInNbrSolicits": jnxIcmpv6StatsInNbrSolicits,
       "jnxIcmpv6StatsInNbrAdvs": jnxIcmpv6StatsInNbrAdvs,
       "jnxIcmpv6StatsInRedirects": jnxIcmpv6StatsInRedirects,
       "jnxIcmpv6StatsInRtrRenumbers": jnxIcmpv6StatsInRtrRenumbers,
       "jnxIcmpv6StatsInNIReqs": jnxIcmpv6StatsInNIReqs,
       "jnxIcmpv6StatsInNIReplies": jnxIcmpv6StatsInNIReplies,
       "jnxIcmpv6StatsOutUnreachables": jnxIcmpv6StatsOutUnreachables,
       "jnxIcmpv6StatsOutPktTooBigs": jnxIcmpv6StatsOutPktTooBigs,
       "jnxIcmpv6StatsOutTimeExceeds": jnxIcmpv6StatsOutTimeExceeds,
       "jnxIcmpv6StatsOutParamProbs": jnxIcmpv6StatsOutParamProbs,
       "jnxIcmpv6StatsOutEchoReqs": jnxIcmpv6StatsOutEchoReqs,
       "jnxIcmpv6StatsOutEchoReplies": jnxIcmpv6StatsOutEchoReplies,
       "jnxIcmpv6StatsOutMLQueries": jnxIcmpv6StatsOutMLQueries,
       "jnxIcmpv6StatsOutMLReports": jnxIcmpv6StatsOutMLReports,
       "jnxIcmpv6StatsOutMLDones": jnxIcmpv6StatsOutMLDones,
       "jnxIcmpv6StatsOutRtrSolicits": jnxIcmpv6StatsOutRtrSolicits,
       "jnxIcmpv6StatsOutRtrAdvs": jnxIcmpv6StatsOutRtrAdvs,
       "jnxIcmpv6StatsOutNbrSolicits": jnxIcmpv6StatsOutNbrSolicits,
       "jnxIcmpv6StatsOutNbrAdvs": jnxIcmpv6StatsOutNbrAdvs,
       "jnxIcmpv6StatsOutRedirects": jnxIcmpv6StatsOutRedirects,
       "jnxIcmpv6StatsOutRtrRenumbers": jnxIcmpv6StatsOutRtrRenumbers,
       "jnxIcmpv6StatsOutNIReqs": jnxIcmpv6StatsOutNIReqs,
       "jnxIcmpv6StatsOutNIReplies": jnxIcmpv6StatsOutNIReplies,
       "jnxIpv6IfStats": jnxIpv6IfStats,
       "jnxIpv6IfStatsTable": jnxIpv6IfStatsTable,
       "jnxIpv6IfStatsEntry": jnxIpv6IfStatsEntry,
       "jnxIpv6IfInOctets": jnxIpv6IfInOctets,
       "jnxIpv6IfOutOctets": jnxIpv6IfOutOctets}
)
