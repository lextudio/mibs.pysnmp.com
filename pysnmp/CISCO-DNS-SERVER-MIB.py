# SNMP MIB module (CISCO-DNS-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DNS-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:40 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY

ciscoDnsServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405)
)
ciscoDnsServerMIB.setRevisions(
        ("2005-03-01 00:00",
         "2004-02-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CDnsTime(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_CDnsServMIBNotifs_ObjectIdentity = ObjectIdentity
cDnsServMIBNotifs = _CDnsServMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 0)
)
_CDnsServMIBObjects_ObjectIdentity = ObjectIdentity
cDnsServMIBObjects = _CDnsServMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1)
)
_CDnsServConfig_ObjectIdentity = ObjectIdentity
cDnsServConfig = _CDnsServConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 1)
)
_CDnsServConfigImplementIdent_Type = SnmpAdminString
_CDnsServConfigImplementIdent_Object = MibScalar
cDnsServConfigImplementIdent = _CDnsServConfigImplementIdent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 1, 1),
    _CDnsServConfigImplementIdent_Type()
)
cDnsServConfigImplementIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsServConfigImplementIdent.setStatus("current")


class _CDnsServConfigRecurs_Type(Integer32):
    """Custom type cDnsServConfigRecurs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("restricted", 2),
          ("unavailable", 3))
    )


_CDnsServConfigRecurs_Type.__name__ = "Integer32"
_CDnsServConfigRecurs_Object = MibScalar
cDnsServConfigRecurs = _CDnsServConfigRecurs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 1, 2),
    _CDnsServConfigRecurs_Type()
)
cDnsServConfigRecurs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDnsServConfigRecurs.setStatus("current")
_CDnsServConfigUpTime_Type = CDnsTime
_CDnsServConfigUpTime_Object = MibScalar
cDnsServConfigUpTime = _CDnsServConfigUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 1, 3),
    _CDnsServConfigUpTime_Type()
)
cDnsServConfigUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsServConfigUpTime.setStatus("current")
_CDnsServConfigResetTime_Type = CDnsTime
_CDnsServConfigResetTime_Object = MibScalar
cDnsServConfigResetTime = _CDnsServConfigResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 1, 4),
    _CDnsServConfigResetTime_Type()
)
cDnsServConfigResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsServConfigResetTime.setStatus("current")


class _CDnsServConfigReset_Type(Integer32):
    """Custom type cDnsServConfigReset based on Integer32"""
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
        *(("initializing", 3),
          ("other", 1),
          ("reset", 2),
          ("running", 4))
    )


_CDnsServConfigReset_Type.__name__ = "Integer32"
_CDnsServConfigReset_Object = MibScalar
cDnsServConfigReset = _CDnsServConfigReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 1, 5),
    _CDnsServConfigReset_Type()
)
cDnsServConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDnsServConfigReset.setStatus("current")
_CDnsServConfigIntervalSample_Type = TimeInterval
_CDnsServConfigIntervalSample_Object = MibScalar
cDnsServConfigIntervalSample = _CDnsServConfigIntervalSample_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 1, 6),
    _CDnsServConfigIntervalSample_Type()
)
cDnsServConfigIntervalSample.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDnsServConfigIntervalSample.setStatus("current")
if mibBuilder.loadTexts:
    cDnsServConfigIntervalSample.setUnits("milliseconds")
_CDnsQueryStats_ObjectIdentity = ObjectIdentity
cDnsQueryStats = _CDnsQueryStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 2)
)
_CDnsQueryAuthAnswers_Type = Counter32
_CDnsQueryAuthAnswers_Object = MibScalar
cDnsQueryAuthAnswers = _CDnsQueryAuthAnswers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 2, 1),
    _CDnsQueryAuthAnswers_Type()
)
cDnsQueryAuthAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryAuthAnswers.setStatus("current")
_CDnsQueryAuthNoNames_Type = Counter32
_CDnsQueryAuthNoNames_Object = MibScalar
cDnsQueryAuthNoNames = _CDnsQueryAuthNoNames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 2, 2),
    _CDnsQueryAuthNoNames_Type()
)
cDnsQueryAuthNoNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryAuthNoNames.setStatus("current")
_CDnsQueryAuthNoDataResps_Type = Counter32
_CDnsQueryAuthNoDataResps_Object = MibScalar
cDnsQueryAuthNoDataResps = _CDnsQueryAuthNoDataResps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 2, 3),
    _CDnsQueryAuthNoDataResps_Type()
)
cDnsQueryAuthNoDataResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryAuthNoDataResps.setStatus("current")
_CDnsQueryReferrals_Type = Counter32
_CDnsQueryReferrals_Object = MibScalar
cDnsQueryReferrals = _CDnsQueryReferrals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 2, 4),
    _CDnsQueryReferrals_Type()
)
cDnsQueryReferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryReferrals.setStatus("current")
_CDnsQueryNonAuthAnswers_Type = Counter32
_CDnsQueryNonAuthAnswers_Object = MibScalar
cDnsQueryNonAuthAnswers = _CDnsQueryNonAuthAnswers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 2, 5),
    _CDnsQueryNonAuthAnswers_Type()
)
cDnsQueryNonAuthAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryNonAuthAnswers.setStatus("current")
_CDnsQueryNonAuthNoDataResps_Type = Counter32
_CDnsQueryNonAuthNoDataResps_Object = MibScalar
cDnsQueryNonAuthNoDataResps = _CDnsQueryNonAuthNoDataResps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 2, 6),
    _CDnsQueryNonAuthNoDataResps_Type()
)
cDnsQueryNonAuthNoDataResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryNonAuthNoDataResps.setStatus("current")
_CDnsQueryRelNameRequests_Type = Counter32
_CDnsQueryRelNameRequests_Object = MibScalar
cDnsQueryRelNameRequests = _CDnsQueryRelNameRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 2, 7),
    _CDnsQueryRelNameRequests_Type()
)
cDnsQueryRelNameRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryRelNameRequests.setStatus("current")
_CDnsQueryLameDelegations_Type = Counter32
_CDnsQueryLameDelegations_Object = MibScalar
cDnsQueryLameDelegations = _CDnsQueryLameDelegations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 2, 8),
    _CDnsQueryLameDelegations_Type()
)
cDnsQueryLameDelegations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryLameDelegations.setStatus("current")
_CDnsQueryMemCacheHits_Type = Counter32
_CDnsQueryMemCacheHits_Object = MibScalar
cDnsQueryMemCacheHits = _CDnsQueryMemCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 2, 9),
    _CDnsQueryMemCacheHits_Type()
)
cDnsQueryMemCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryMemCacheHits.setStatus("current")
_CDnsQueryMemCacheMisses_Type = Counter32
_CDnsQueryMemCacheMisses_Object = MibScalar
cDnsQueryMemCacheMisses = _CDnsQueryMemCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 2, 10),
    _CDnsQueryMemCacheMisses_Type()
)
cDnsQueryMemCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryMemCacheMisses.setStatus("current")
_CDnsQueryMemCacheWrites_Type = Counter32
_CDnsQueryMemCacheWrites_Object = MibScalar
cDnsQueryMemCacheWrites = _CDnsQueryMemCacheWrites_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 2, 11),
    _CDnsQueryMemCacheWrites_Type()
)
cDnsQueryMemCacheWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryMemCacheWrites.setStatus("current")
_CDnsQueryRefusals_Type = Counter32
_CDnsQueryRefusals_Object = MibScalar
cDnsQueryRefusals = _CDnsQueryRefusals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 2, 12),
    _CDnsQueryRefusals_Type()
)
cDnsQueryRefusals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryRefusals.setStatus("current")
_CDnsQueryIntervalStats_ObjectIdentity = ObjectIdentity
cDnsQueryIntervalStats = _CDnsQueryIntervalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 3)
)
_CDnsQueryIntAuthAnswers_Type = Unsigned32
_CDnsQueryIntAuthAnswers_Object = MibScalar
cDnsQueryIntAuthAnswers = _CDnsQueryIntAuthAnswers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 3, 1),
    _CDnsQueryIntAuthAnswers_Type()
)
cDnsQueryIntAuthAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryIntAuthAnswers.setStatus("current")
_CDnsQueryIntAuthNoNames_Type = Unsigned32
_CDnsQueryIntAuthNoNames_Object = MibScalar
cDnsQueryIntAuthNoNames = _CDnsQueryIntAuthNoNames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 3, 2),
    _CDnsQueryIntAuthNoNames_Type()
)
cDnsQueryIntAuthNoNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryIntAuthNoNames.setStatus("current")
_CDnsQueryIntAuthNoDataResps_Type = Unsigned32
_CDnsQueryIntAuthNoDataResps_Object = MibScalar
cDnsQueryIntAuthNoDataResps = _CDnsQueryIntAuthNoDataResps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 3, 3),
    _CDnsQueryIntAuthNoDataResps_Type()
)
cDnsQueryIntAuthNoDataResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryIntAuthNoDataResps.setStatus("current")
_CDnsQueryIntReferrals_Type = Unsigned32
_CDnsQueryIntReferrals_Object = MibScalar
cDnsQueryIntReferrals = _CDnsQueryIntReferrals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 3, 4),
    _CDnsQueryIntReferrals_Type()
)
cDnsQueryIntReferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryIntReferrals.setStatus("current")
_CDnsQueryIntNonAuthAnswers_Type = Unsigned32
_CDnsQueryIntNonAuthAnswers_Object = MibScalar
cDnsQueryIntNonAuthAnswers = _CDnsQueryIntNonAuthAnswers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 3, 5),
    _CDnsQueryIntNonAuthAnswers_Type()
)
cDnsQueryIntNonAuthAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryIntNonAuthAnswers.setStatus("current")
_CDnsQueryIntNonAuthNoDataResps_Type = Unsigned32
_CDnsQueryIntNonAuthNoDataResps_Object = MibScalar
cDnsQueryIntNonAuthNoDataResps = _CDnsQueryIntNonAuthNoDataResps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 3, 6),
    _CDnsQueryIntNonAuthNoDataResps_Type()
)
cDnsQueryIntNonAuthNoDataResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryIntNonAuthNoDataResps.setStatus("current")
_CDnsQueryIntRelNameRequests_Type = Unsigned32
_CDnsQueryIntRelNameRequests_Object = MibScalar
cDnsQueryIntRelNameRequests = _CDnsQueryIntRelNameRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 3, 7),
    _CDnsQueryIntRelNameRequests_Type()
)
cDnsQueryIntRelNameRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryIntRelNameRequests.setStatus("current")
_CDnsQueryIntLameDelegations_Type = Unsigned32
_CDnsQueryIntLameDelegations_Object = MibScalar
cDnsQueryIntLameDelegations = _CDnsQueryIntLameDelegations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 3, 8),
    _CDnsQueryIntLameDelegations_Type()
)
cDnsQueryIntLameDelegations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryIntLameDelegations.setStatus("current")
_CDnsQueryIntMemCacheHits_Type = Unsigned32
_CDnsQueryIntMemCacheHits_Object = MibScalar
cDnsQueryIntMemCacheHits = _CDnsQueryIntMemCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 3, 9),
    _CDnsQueryIntMemCacheHits_Type()
)
cDnsQueryIntMemCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryIntMemCacheHits.setStatus("current")
_CDnsQueryIntMemCacheMisses_Type = Unsigned32
_CDnsQueryIntMemCacheMisses_Object = MibScalar
cDnsQueryIntMemCacheMisses = _CDnsQueryIntMemCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 3, 10),
    _CDnsQueryIntMemCacheMisses_Type()
)
cDnsQueryIntMemCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryIntMemCacheMisses.setStatus("current")
_CDnsQueryIntMemCacheWrites_Type = Unsigned32
_CDnsQueryIntMemCacheWrites_Object = MibScalar
cDnsQueryIntMemCacheWrites = _CDnsQueryIntMemCacheWrites_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 3, 11),
    _CDnsQueryIntMemCacheWrites_Type()
)
cDnsQueryIntMemCacheWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryIntMemCacheWrites.setStatus("current")
_CDnsQueryIntRefusals_Type = Counter32
_CDnsQueryIntRefusals_Object = MibScalar
cDnsQueryIntRefusals = _CDnsQueryIntRefusals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 3, 12),
    _CDnsQueryIntRefusals_Type()
)
cDnsQueryIntRefusals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryIntRefusals.setStatus("current")
_CDnsQueryIntSampleTime_Type = TimeStamp
_CDnsQueryIntSampleTime_Object = MibScalar
cDnsQueryIntSampleTime = _CDnsQueryIntSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 3, 13),
    _CDnsQueryIntSampleTime_Type()
)
cDnsQueryIntSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryIntSampleTime.setStatus("current")
_CDnsQueryIntSampleInterval_Type = TimeInterval
_CDnsQueryIntSampleInterval_Object = MibScalar
cDnsQueryIntSampleInterval = _CDnsQueryIntSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 3, 14),
    _CDnsQueryIntSampleInterval_Type()
)
cDnsQueryIntSampleInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsQueryIntSampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    cDnsQueryIntSampleInterval.setUnits("milliseconds")
_CDnsPerfStats_ObjectIdentity = ObjectIdentity
cDnsPerfStats = _CDnsPerfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 4)
)
_CDnsPerfUpdateRRs_Type = Counter32
_CDnsPerfUpdateRRs_Object = MibScalar
cDnsPerfUpdateRRs = _CDnsPerfUpdateRRs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 4, 1),
    _CDnsPerfUpdateRRs_Type()
)
cDnsPerfUpdateRRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfUpdateRRs.setStatus("current")
_CDnsPerfUpdatePkts_Type = Counter32
_CDnsPerfUpdatePkts_Object = MibScalar
cDnsPerfUpdatePkts = _CDnsPerfUpdatePkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 4, 2),
    _CDnsPerfUpdatePkts_Type()
)
cDnsPerfUpdatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfUpdatePkts.setStatus("current")
_CDnsPerfOutboundIxfrs_Type = Counter32
_CDnsPerfOutboundIxfrs_Object = MibScalar
cDnsPerfOutboundIxfrs = _CDnsPerfOutboundIxfrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 4, 3),
    _CDnsPerfOutboundIxfrs_Type()
)
cDnsPerfOutboundIxfrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfOutboundIxfrs.setStatus("current")
_CDnsPerfInboundIxfrs_Type = Counter32
_CDnsPerfInboundIxfrs_Object = MibScalar
cDnsPerfInboundIxfrs = _CDnsPerfInboundIxfrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 4, 4),
    _CDnsPerfInboundIxfrs_Type()
)
cDnsPerfInboundIxfrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfInboundIxfrs.setStatus("current")
_CDnsPerfFullRespIxfrs_Type = Counter32
_CDnsPerfFullRespIxfrs_Object = MibScalar
cDnsPerfFullRespIxfrs = _CDnsPerfFullRespIxfrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 4, 5),
    _CDnsPerfFullRespIxfrs_Type()
)
cDnsPerfFullRespIxfrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfFullRespIxfrs.setStatus("current")
_CDnsPerfOutboundAxfrs_Type = Counter32
_CDnsPerfOutboundAxfrs_Object = MibScalar
cDnsPerfOutboundAxfrs = _CDnsPerfOutboundAxfrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 4, 6),
    _CDnsPerfOutboundAxfrs_Type()
)
cDnsPerfOutboundAxfrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfOutboundAxfrs.setStatus("current")
_CDnsPerfInboundAxfrs_Type = Counter32
_CDnsPerfInboundAxfrs_Object = MibScalar
cDnsPerfInboundAxfrs = _CDnsPerfInboundAxfrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 4, 7),
    _CDnsPerfInboundAxfrs_Type()
)
cDnsPerfInboundAxfrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfInboundAxfrs.setStatus("current")
_CDnsPerfQueries_Type = Counter32
_CDnsPerfQueries_Object = MibScalar
cDnsPerfQueries = _CDnsPerfQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 4, 8),
    _CDnsPerfQueries_Type()
)
cDnsPerfQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfQueries.setStatus("current")
_CDnsPerfOutboundAtLimitXfrs_Type = Counter32
_CDnsPerfOutboundAtLimitXfrs_Object = MibScalar
cDnsPerfOutboundAtLimitXfrs = _CDnsPerfOutboundAtLimitXfrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 4, 9),
    _CDnsPerfOutboundAtLimitXfrs_Type()
)
cDnsPerfOutboundAtLimitXfrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfOutboundAtLimitXfrs.setStatus("current")
_CDnsPerfInboundAtLimitXfrs_Type = Counter32
_CDnsPerfInboundAtLimitXfrs_Object = MibScalar
cDnsPerfInboundAtLimitXfrs = _CDnsPerfInboundAtLimitXfrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 4, 10),
    _CDnsPerfInboundAtLimitXfrs_Type()
)
cDnsPerfInboundAtLimitXfrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfInboundAtLimitXfrs.setStatus("current")
_CDnsPerfOutboundNotifies_Type = Counter32
_CDnsPerfOutboundNotifies_Object = MibScalar
cDnsPerfOutboundNotifies = _CDnsPerfOutboundNotifies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 4, 11),
    _CDnsPerfOutboundNotifies_Type()
)
cDnsPerfOutboundNotifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfOutboundNotifies.setStatus("current")
_CDnsPerfInboundNotifies_Type = Counter32
_CDnsPerfInboundNotifies_Object = MibScalar
cDnsPerfInboundNotifies = _CDnsPerfInboundNotifies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 4, 12),
    _CDnsPerfInboundNotifies_Type()
)
cDnsPerfInboundNotifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfInboundNotifies.setStatus("current")
_CDnsPerfIntervalStats_ObjectIdentity = ObjectIdentity
cDnsPerfIntervalStats = _CDnsPerfIntervalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 5)
)
_CDnsPerfIntUpdateRRs_Type = Unsigned32
_CDnsPerfIntUpdateRRs_Object = MibScalar
cDnsPerfIntUpdateRRs = _CDnsPerfIntUpdateRRs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 5, 1),
    _CDnsPerfIntUpdateRRs_Type()
)
cDnsPerfIntUpdateRRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfIntUpdateRRs.setStatus("current")
_CDnsPerfIntUpdatePkts_Type = Unsigned32
_CDnsPerfIntUpdatePkts_Object = MibScalar
cDnsPerfIntUpdatePkts = _CDnsPerfIntUpdatePkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 5, 2),
    _CDnsPerfIntUpdatePkts_Type()
)
cDnsPerfIntUpdatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfIntUpdatePkts.setStatus("current")
_CDnsPerfIntOutboundIxfrs_Type = Unsigned32
_CDnsPerfIntOutboundIxfrs_Object = MibScalar
cDnsPerfIntOutboundIxfrs = _CDnsPerfIntOutboundIxfrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 5, 3),
    _CDnsPerfIntOutboundIxfrs_Type()
)
cDnsPerfIntOutboundIxfrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfIntOutboundIxfrs.setStatus("current")
_CDnsPerfIntInboundIxfrs_Type = Unsigned32
_CDnsPerfIntInboundIxfrs_Object = MibScalar
cDnsPerfIntInboundIxfrs = _CDnsPerfIntInboundIxfrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 5, 4),
    _CDnsPerfIntInboundIxfrs_Type()
)
cDnsPerfIntInboundIxfrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfIntInboundIxfrs.setStatus("current")
_CDnsPerfIntFullRespIxfrs_Type = Unsigned32
_CDnsPerfIntFullRespIxfrs_Object = MibScalar
cDnsPerfIntFullRespIxfrs = _CDnsPerfIntFullRespIxfrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 5, 5),
    _CDnsPerfIntFullRespIxfrs_Type()
)
cDnsPerfIntFullRespIxfrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfIntFullRespIxfrs.setStatus("current")
_CDnsPerfIntOutboundAxfrs_Type = Unsigned32
_CDnsPerfIntOutboundAxfrs_Object = MibScalar
cDnsPerfIntOutboundAxfrs = _CDnsPerfIntOutboundAxfrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 5, 6),
    _CDnsPerfIntOutboundAxfrs_Type()
)
cDnsPerfIntOutboundAxfrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfIntOutboundAxfrs.setStatus("current")
_CDnsPerfIntInboundAxfrs_Type = Unsigned32
_CDnsPerfIntInboundAxfrs_Object = MibScalar
cDnsPerfIntInboundAxfrs = _CDnsPerfIntInboundAxfrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 5, 7),
    _CDnsPerfIntInboundAxfrs_Type()
)
cDnsPerfIntInboundAxfrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfIntInboundAxfrs.setStatus("current")
_CDnsPerfIntQueries_Type = Unsigned32
_CDnsPerfIntQueries_Object = MibScalar
cDnsPerfIntQueries = _CDnsPerfIntQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 5, 8),
    _CDnsPerfIntQueries_Type()
)
cDnsPerfIntQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfIntQueries.setStatus("current")
_CDnsPerfIntOutboundAtLimitXfrs_Type = Unsigned32
_CDnsPerfIntOutboundAtLimitXfrs_Object = MibScalar
cDnsPerfIntOutboundAtLimitXfrs = _CDnsPerfIntOutboundAtLimitXfrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 5, 9),
    _CDnsPerfIntOutboundAtLimitXfrs_Type()
)
cDnsPerfIntOutboundAtLimitXfrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfIntOutboundAtLimitXfrs.setStatus("current")
_CDnsPerfIntInboundAtLimitXfrs_Type = Unsigned32
_CDnsPerfIntInboundAtLimitXfrs_Object = MibScalar
cDnsPerfIntInboundAtLimitXfrs = _CDnsPerfIntInboundAtLimitXfrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 5, 10),
    _CDnsPerfIntInboundAtLimitXfrs_Type()
)
cDnsPerfIntInboundAtLimitXfrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfIntInboundAtLimitXfrs.setStatus("current")
_CDnsPerfIntOutboundNotifies_Type = Unsigned32
_CDnsPerfIntOutboundNotifies_Object = MibScalar
cDnsPerfIntOutboundNotifies = _CDnsPerfIntOutboundNotifies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 5, 11),
    _CDnsPerfIntOutboundNotifies_Type()
)
cDnsPerfIntOutboundNotifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfIntOutboundNotifies.setStatus("current")
_CDnsPerfIntInboundNotifies_Type = Unsigned32
_CDnsPerfIntInboundNotifies_Object = MibScalar
cDnsPerfIntInboundNotifies = _CDnsPerfIntInboundNotifies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 5, 12),
    _CDnsPerfIntInboundNotifies_Type()
)
cDnsPerfIntInboundNotifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfIntInboundNotifies.setStatus("current")
_CDnsPerfIntSampleTime_Type = TimeStamp
_CDnsPerfIntSampleTime_Object = MibScalar
cDnsPerfIntSampleTime = _CDnsPerfIntSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 5, 13),
    _CDnsPerfIntSampleTime_Type()
)
cDnsPerfIntSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfIntSampleTime.setStatus("current")
_CDnsPerfIntSampleInterval_Type = TimeInterval
_CDnsPerfIntSampleInterval_Object = MibScalar
cDnsPerfIntSampleInterval = _CDnsPerfIntSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 5, 14),
    _CDnsPerfIntSampleInterval_Type()
)
cDnsPerfIntSampleInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsPerfIntSampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    cDnsPerfIntSampleInterval.setUnits("milliseconds")
_CDnsSecurityStats_ObjectIdentity = ObjectIdentity
cDnsSecurityStats = _CDnsSecurityStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 6)
)
_CDnsSecurityRcvdTsigPackets_Type = Counter32
_CDnsSecurityRcvdTsigPackets_Object = MibScalar
cDnsSecurityRcvdTsigPackets = _CDnsSecurityRcvdTsigPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 6, 1),
    _CDnsSecurityRcvdTsigPackets_Type()
)
cDnsSecurityRcvdTsigPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityRcvdTsigPackets.setStatus("current")
_CDnsSecurityDetecTsigBadTimes_Type = Counter32
_CDnsSecurityDetecTsigBadTimes_Object = MibScalar
cDnsSecurityDetecTsigBadTimes = _CDnsSecurityDetecTsigBadTimes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 6, 2),
    _CDnsSecurityDetecTsigBadTimes_Type()
)
cDnsSecurityDetecTsigBadTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityDetecTsigBadTimes.setStatus("current")
_CDnsSecurityDetectTsigBadKeys_Type = Counter32
_CDnsSecurityDetectTsigBadKeys_Object = MibScalar
cDnsSecurityDetectTsigBadKeys = _CDnsSecurityDetectTsigBadKeys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 6, 3),
    _CDnsSecurityDetectTsigBadKeys_Type()
)
cDnsSecurityDetectTsigBadKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityDetectTsigBadKeys.setStatus("current")
_CDnsSecurityDetectTsigBadSigs_Type = Counter32
_CDnsSecurityDetectTsigBadSigs_Object = MibScalar
cDnsSecurityDetectTsigBadSigs = _CDnsSecurityDetectTsigBadSigs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 6, 4),
    _CDnsSecurityDetectTsigBadSigs_Type()
)
cDnsSecurityDetectTsigBadSigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityDetectTsigBadSigs.setStatus("current")
_CDnsSecurityRcvdTsigBadTimes_Type = Counter32
_CDnsSecurityRcvdTsigBadTimes_Object = MibScalar
cDnsSecurityRcvdTsigBadTimes = _CDnsSecurityRcvdTsigBadTimes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 6, 5),
    _CDnsSecurityRcvdTsigBadTimes_Type()
)
cDnsSecurityRcvdTsigBadTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityRcvdTsigBadTimes.setStatus("current")
_CDnsSecurityRcvdTsigBadKeys_Type = Counter32
_CDnsSecurityRcvdTsigBadKeys_Object = MibScalar
cDnsSecurityRcvdTsigBadKeys = _CDnsSecurityRcvdTsigBadKeys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 6, 6),
    _CDnsSecurityRcvdTsigBadKeys_Type()
)
cDnsSecurityRcvdTsigBadKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityRcvdTsigBadKeys.setStatus("current")
_CDnsSecurityRcvdTsigBadSigs_Type = Counter32
_CDnsSecurityRcvdTsigBadSigs_Object = MibScalar
cDnsSecurityRcvdTsigBadSigs = _CDnsSecurityRcvdTsigBadSigs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 6, 7),
    _CDnsSecurityRcvdTsigBadSigs_Type()
)
cDnsSecurityRcvdTsigBadSigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityRcvdTsigBadSigs.setStatus("current")
_CDnsSecurityUnauthXferReqs_Type = Counter32
_CDnsSecurityUnauthXferReqs_Object = MibScalar
cDnsSecurityUnauthXferReqs = _CDnsSecurityUnauthXferReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 6, 8),
    _CDnsSecurityUnauthXferReqs_Type()
)
cDnsSecurityUnauthXferReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityUnauthXferReqs.setStatus("current")
_CDnsSecurityUnauthUpdateReqs_Type = Counter32
_CDnsSecurityUnauthUpdateReqs_Object = MibScalar
cDnsSecurityUnauthUpdateReqs = _CDnsSecurityUnauthUpdateReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 6, 9),
    _CDnsSecurityUnauthUpdateReqs_Type()
)
cDnsSecurityUnauthUpdateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityUnauthUpdateReqs.setStatus("current")
_CDnsSecurityRestrictQueryAcls_Type = Counter32
_CDnsSecurityRestrictQueryAcls_Object = MibScalar
cDnsSecurityRestrictQueryAcls = _CDnsSecurityRestrictQueryAcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 6, 10),
    _CDnsSecurityRestrictQueryAcls_Type()
)
cDnsSecurityRestrictQueryAcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityRestrictQueryAcls.setStatus("current")
_CDnsSecurityIntervalStats_ObjectIdentity = ObjectIdentity
cDnsSecurityIntervalStats = _CDnsSecurityIntervalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 7)
)
_CDnsSecurityIntRcvdTsigPackets_Type = Unsigned32
_CDnsSecurityIntRcvdTsigPackets_Object = MibScalar
cDnsSecurityIntRcvdTsigPackets = _CDnsSecurityIntRcvdTsigPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 7, 1),
    _CDnsSecurityIntRcvdTsigPackets_Type()
)
cDnsSecurityIntRcvdTsigPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityIntRcvdTsigPackets.setStatus("current")
_CDnsSecurityIntDetecTsigBadTimes_Type = Unsigned32
_CDnsSecurityIntDetecTsigBadTimes_Object = MibScalar
cDnsSecurityIntDetecTsigBadTimes = _CDnsSecurityIntDetecTsigBadTimes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 7, 2),
    _CDnsSecurityIntDetecTsigBadTimes_Type()
)
cDnsSecurityIntDetecTsigBadTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityIntDetecTsigBadTimes.setStatus("current")
_CDnsSecurityIntDetectTsigBadKeys_Type = Unsigned32
_CDnsSecurityIntDetectTsigBadKeys_Object = MibScalar
cDnsSecurityIntDetectTsigBadKeys = _CDnsSecurityIntDetectTsigBadKeys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 7, 3),
    _CDnsSecurityIntDetectTsigBadKeys_Type()
)
cDnsSecurityIntDetectTsigBadKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityIntDetectTsigBadKeys.setStatus("current")
_CDnsSecurityIntDetectTsigBadSigs_Type = Unsigned32
_CDnsSecurityIntDetectTsigBadSigs_Object = MibScalar
cDnsSecurityIntDetectTsigBadSigs = _CDnsSecurityIntDetectTsigBadSigs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 7, 4),
    _CDnsSecurityIntDetectTsigBadSigs_Type()
)
cDnsSecurityIntDetectTsigBadSigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityIntDetectTsigBadSigs.setStatus("current")
_CDnsSecurityIntRcvdTsigBadTimes_Type = Unsigned32
_CDnsSecurityIntRcvdTsigBadTimes_Object = MibScalar
cDnsSecurityIntRcvdTsigBadTimes = _CDnsSecurityIntRcvdTsigBadTimes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 7, 5),
    _CDnsSecurityIntRcvdTsigBadTimes_Type()
)
cDnsSecurityIntRcvdTsigBadTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityIntRcvdTsigBadTimes.setStatus("current")
_CDnsSecurityIntRcvdTsigBadKeys_Type = Unsigned32
_CDnsSecurityIntRcvdTsigBadKeys_Object = MibScalar
cDnsSecurityIntRcvdTsigBadKeys = _CDnsSecurityIntRcvdTsigBadKeys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 7, 6),
    _CDnsSecurityIntRcvdTsigBadKeys_Type()
)
cDnsSecurityIntRcvdTsigBadKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityIntRcvdTsigBadKeys.setStatus("current")
_CDnsSecurityIntRcvdTsigBadSigs_Type = Unsigned32
_CDnsSecurityIntRcvdTsigBadSigs_Object = MibScalar
cDnsSecurityIntRcvdTsigBadSigs = _CDnsSecurityIntRcvdTsigBadSigs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 7, 7),
    _CDnsSecurityIntRcvdTsigBadSigs_Type()
)
cDnsSecurityIntRcvdTsigBadSigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityIntRcvdTsigBadSigs.setStatus("current")
_CDnsSecurityIntUnauthXferReqs_Type = Unsigned32
_CDnsSecurityIntUnauthXferReqs_Object = MibScalar
cDnsSecurityIntUnauthXferReqs = _CDnsSecurityIntUnauthXferReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 7, 8),
    _CDnsSecurityIntUnauthXferReqs_Type()
)
cDnsSecurityIntUnauthXferReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityIntUnauthXferReqs.setStatus("current")
_CDnsSecurityIntUnauthUpdateReqs_Type = Unsigned32
_CDnsSecurityIntUnauthUpdateReqs_Object = MibScalar
cDnsSecurityIntUnauthUpdateReqs = _CDnsSecurityIntUnauthUpdateReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 7, 9),
    _CDnsSecurityIntUnauthUpdateReqs_Type()
)
cDnsSecurityIntUnauthUpdateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityIntUnauthUpdateReqs.setStatus("current")
_CDnsSecurityIntRestrictQueryAcls_Type = Unsigned32
_CDnsSecurityIntRestrictQueryAcls_Object = MibScalar
cDnsSecurityIntRestrictQueryAcls = _CDnsSecurityIntRestrictQueryAcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 7, 10),
    _CDnsSecurityIntRestrictQueryAcls_Type()
)
cDnsSecurityIntRestrictQueryAcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityIntRestrictQueryAcls.setStatus("current")
_CDnsSecurityIntSampleTime_Type = TimeStamp
_CDnsSecurityIntSampleTime_Object = MibScalar
cDnsSecurityIntSampleTime = _CDnsSecurityIntSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 7, 11),
    _CDnsSecurityIntSampleTime_Type()
)
cDnsSecurityIntSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityIntSampleTime.setStatus("current")
_CDnsSecurityIntSampleInterval_Type = TimeInterval
_CDnsSecurityIntSampleInterval_Object = MibScalar
cDnsSecurityIntSampleInterval = _CDnsSecurityIntSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 7, 12),
    _CDnsSecurityIntSampleInterval_Type()
)
cDnsSecurityIntSampleInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsSecurityIntSampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    cDnsSecurityIntSampleInterval.setUnits("milliseconds")
_CDnsErrorStats_ObjectIdentity = ObjectIdentity
cDnsErrorStats = _CDnsErrorStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 8)
)
_CDnsErrorUpdateErrors_Type = Counter32
_CDnsErrorUpdateErrors_Object = MibScalar
cDnsErrorUpdateErrors = _CDnsErrorUpdateErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 8, 1),
    _CDnsErrorUpdateErrors_Type()
)
cDnsErrorUpdateErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorUpdateErrors.setStatus("current")
_CDnsErrorIxfrInErrors_Type = Counter32
_CDnsErrorIxfrInErrors_Object = MibScalar
cDnsErrorIxfrInErrors = _CDnsErrorIxfrInErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 8, 2),
    _CDnsErrorIxfrInErrors_Type()
)
cDnsErrorIxfrInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorIxfrInErrors.setStatus("current")
_CDnsErrorIxfrOutErrors_Type = Counter32
_CDnsErrorIxfrOutErrors_Object = MibScalar
cDnsErrorIxfrOutErrors = _CDnsErrorIxfrOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 8, 3),
    _CDnsErrorIxfrOutErrors_Type()
)
cDnsErrorIxfrOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorIxfrOutErrors.setStatus("current")
_CDnsErrorAxfrInErrors_Type = Counter32
_CDnsErrorAxfrInErrors_Object = MibScalar
cDnsErrorAxfrInErrors = _CDnsErrorAxfrInErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 8, 4),
    _CDnsErrorAxfrInErrors_Type()
)
cDnsErrorAxfrInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorAxfrInErrors.setStatus("current")
_CDnsErrorAxfrOutErrors_Type = Counter32
_CDnsErrorAxfrOutErrors_Object = MibScalar
cDnsErrorAxfrOutErrors = _CDnsErrorAxfrOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 8, 5),
    _CDnsErrorAxfrOutErrors_Type()
)
cDnsErrorAxfrOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorAxfrOutErrors.setStatus("current")
_CDnsErrorSentTotalErrors_Type = Counter32
_CDnsErrorSentTotalErrors_Object = MibScalar
cDnsErrorSentTotalErrors = _CDnsErrorSentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 8, 6),
    _CDnsErrorSentTotalErrors_Type()
)
cDnsErrorSentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorSentTotalErrors.setStatus("current")
_CDnsErrorSentFormatErrors_Type = Counter32
_CDnsErrorSentFormatErrors_Object = MibScalar
cDnsErrorSentFormatErrors = _CDnsErrorSentFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 8, 7),
    _CDnsErrorSentFormatErrors_Type()
)
cDnsErrorSentFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorSentFormatErrors.setStatus("current")
_CDnsErrorSentOtherErrors_Type = Counter32
_CDnsErrorSentOtherErrors_Object = MibScalar
cDnsErrorSentOtherErrors = _CDnsErrorSentOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 8, 8),
    _CDnsErrorSentOtherErrors_Type()
)
cDnsErrorSentOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorSentOtherErrors.setStatus("current")
_CDnsErrorSentRefusalErrors_Type = Counter32
_CDnsErrorSentRefusalErrors_Object = MibScalar
cDnsErrorSentRefusalErrors = _CDnsErrorSentRefusalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 8, 9),
    _CDnsErrorSentRefusalErrors_Type()
)
cDnsErrorSentRefusalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorSentRefusalErrors.setStatus("current")
_CDnsErrorRcvdFormatErrors_Type = Counter32
_CDnsErrorRcvdFormatErrors_Object = MibScalar
cDnsErrorRcvdFormatErrors = _CDnsErrorRcvdFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 8, 10),
    _CDnsErrorRcvdFormatErrors_Type()
)
cDnsErrorRcvdFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorRcvdFormatErrors.setStatus("current")
_CDnsErrorIntervalStats_ObjectIdentity = ObjectIdentity
cDnsErrorIntervalStats = _CDnsErrorIntervalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 9)
)
_CDnsErrorIntUpdateErrors_Type = Unsigned32
_CDnsErrorIntUpdateErrors_Object = MibScalar
cDnsErrorIntUpdateErrors = _CDnsErrorIntUpdateErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 9, 1),
    _CDnsErrorIntUpdateErrors_Type()
)
cDnsErrorIntUpdateErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorIntUpdateErrors.setStatus("current")
_CDnsErrorIntIxfrInErrors_Type = Unsigned32
_CDnsErrorIntIxfrInErrors_Object = MibScalar
cDnsErrorIntIxfrInErrors = _CDnsErrorIntIxfrInErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 9, 2),
    _CDnsErrorIntIxfrInErrors_Type()
)
cDnsErrorIntIxfrInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorIntIxfrInErrors.setStatus("current")
_CDnsErrorIntIxfrOutErrors_Type = Unsigned32
_CDnsErrorIntIxfrOutErrors_Object = MibScalar
cDnsErrorIntIxfrOutErrors = _CDnsErrorIntIxfrOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 9, 3),
    _CDnsErrorIntIxfrOutErrors_Type()
)
cDnsErrorIntIxfrOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorIntIxfrOutErrors.setStatus("current")
_CDnsErrorIntAxfrInErrors_Type = Unsigned32
_CDnsErrorIntAxfrInErrors_Object = MibScalar
cDnsErrorIntAxfrInErrors = _CDnsErrorIntAxfrInErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 9, 4),
    _CDnsErrorIntAxfrInErrors_Type()
)
cDnsErrorIntAxfrInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorIntAxfrInErrors.setStatus("current")
_CDnsErrorIntAxfrOutErrors_Type = Unsigned32
_CDnsErrorIntAxfrOutErrors_Object = MibScalar
cDnsErrorIntAxfrOutErrors = _CDnsErrorIntAxfrOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 9, 5),
    _CDnsErrorIntAxfrOutErrors_Type()
)
cDnsErrorIntAxfrOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorIntAxfrOutErrors.setStatus("current")
_CDnsErrorIntSentTotalErrors_Type = Unsigned32
_CDnsErrorIntSentTotalErrors_Object = MibScalar
cDnsErrorIntSentTotalErrors = _CDnsErrorIntSentTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 9, 6),
    _CDnsErrorIntSentTotalErrors_Type()
)
cDnsErrorIntSentTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorIntSentTotalErrors.setStatus("current")
_CDnsErrorIntSentFormatErrors_Type = Unsigned32
_CDnsErrorIntSentFormatErrors_Object = MibScalar
cDnsErrorIntSentFormatErrors = _CDnsErrorIntSentFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 9, 7),
    _CDnsErrorIntSentFormatErrors_Type()
)
cDnsErrorIntSentFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorIntSentFormatErrors.setStatus("current")
_CDnsErrorIntSentOtherErrors_Type = Unsigned32
_CDnsErrorIntSentOtherErrors_Object = MibScalar
cDnsErrorIntSentOtherErrors = _CDnsErrorIntSentOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 9, 8),
    _CDnsErrorIntSentOtherErrors_Type()
)
cDnsErrorIntSentOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorIntSentOtherErrors.setStatus("current")
_CDnsErrorIntSentRefusalErrors_Type = Unsigned32
_CDnsErrorIntSentRefusalErrors_Object = MibScalar
cDnsErrorIntSentRefusalErrors = _CDnsErrorIntSentRefusalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 9, 9),
    _CDnsErrorIntSentRefusalErrors_Type()
)
cDnsErrorIntSentRefusalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorIntSentRefusalErrors.setStatus("current")
_CDnsErrorIntRcvdFormatErrors_Type = Unsigned32
_CDnsErrorIntRcvdFormatErrors_Object = MibScalar
cDnsErrorIntRcvdFormatErrors = _CDnsErrorIntRcvdFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 9, 10),
    _CDnsErrorIntRcvdFormatErrors_Type()
)
cDnsErrorIntRcvdFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorIntRcvdFormatErrors.setStatus("current")
_CDnsErrorIntSampleTime_Type = TimeStamp
_CDnsErrorIntSampleTime_Object = MibScalar
cDnsErrorIntSampleTime = _CDnsErrorIntSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 9, 11),
    _CDnsErrorIntSampleTime_Type()
)
cDnsErrorIntSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorIntSampleTime.setStatus("current")
_CDnsErrorIntSampleInterval_Type = TimeInterval
_CDnsErrorIntSampleInterval_Object = MibScalar
cDnsErrorIntSampleInterval = _CDnsErrorIntSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 9, 12),
    _CDnsErrorIntSampleInterval_Type()
)
cDnsErrorIntSampleInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsErrorIntSampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    cDnsErrorIntSampleInterval.setUnits("milliseconds")
_CDnsMaxCounterStats_ObjectIdentity = ObjectIdentity
cDnsMaxCounterStats = _CDnsMaxCounterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 10)
)
_CDnsMaxCntrConcurXfrsInCnts_Type = Counter32
_CDnsMaxCntrConcurXfrsInCnts_Object = MibScalar
cDnsMaxCntrConcurXfrsInCnts = _CDnsMaxCntrConcurXfrsInCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 10, 1),
    _CDnsMaxCntrConcurXfrsInCnts_Type()
)
cDnsMaxCntrConcurXfrsInCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrConcurXfrsInCnts.setStatus("current")
_CDnsMaxCntrConcurXfrsOutCnts_Type = Counter32
_CDnsMaxCntrConcurXfrsOutCnts_Object = MibScalar
cDnsMaxCntrConcurXfrsOutCnts = _CDnsMaxCntrConcurXfrsOutCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 10, 2),
    _CDnsMaxCntrConcurXfrsOutCnts_Type()
)
cDnsMaxCntrConcurXfrsOutCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrConcurXfrsOutCnts.setStatus("current")
_CDnsMaxCntrHaSvrNoRespTime_Type = TimeInterval
_CDnsMaxCntrHaSvrNoRespTime_Object = MibScalar
cDnsMaxCntrHaSvrNoRespTime = _CDnsMaxCntrHaSvrNoRespTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 10, 3),
    _CDnsMaxCntrHaSvrNoRespTime_Type()
)
cDnsMaxCntrHaSvrNoRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrHaSvrNoRespTime.setStatus("current")
if mibBuilder.loadTexts:
    cDnsMaxCntrHaSvrNoRespTime.setUnits("milliseconds")
_CDnsMaxCntrHaSvrMaxNoRespTime_Type = TimeInterval
_CDnsMaxCntrHaSvrMaxNoRespTime_Object = MibScalar
cDnsMaxCntrHaSvrMaxNoRespTime = _CDnsMaxCntrHaSvrMaxNoRespTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 10, 4),
    _CDnsMaxCntrHaSvrMaxNoRespTime_Type()
)
cDnsMaxCntrHaSvrMaxNoRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrHaSvrMaxNoRespTime.setStatus("current")
if mibBuilder.loadTexts:
    cDnsMaxCntrHaSvrMaxNoRespTime.setUnits("milliseconds")
_CDnsMaxCntrHaBatchLimitCnts_Type = Counter32
_CDnsMaxCntrHaBatchLimitCnts_Object = MibScalar
cDnsMaxCntrHaBatchLimitCnts = _CDnsMaxCntrHaBatchLimitCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 10, 5),
    _CDnsMaxCntrHaBatchLimitCnts_Type()
)
cDnsMaxCntrHaBatchLimitCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrHaBatchLimitCnts.setStatus("current")
_CDnsMaxCntrHaRRPendListCnts_Type = Counter32
_CDnsMaxCntrHaRRPendListCnts_Object = MibScalar
cDnsMaxCntrHaRRPendListCnts = _CDnsMaxCntrHaRRPendListCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 10, 6),
    _CDnsMaxCntrHaRRPendListCnts_Type()
)
cDnsMaxCntrHaRRPendListCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrHaRRPendListCnts.setStatus("current")
_CDnsMaxCntrHaRRActiveListCnts_Type = Counter32
_CDnsMaxCntrHaRRActiveListCnts_Object = MibScalar
cDnsMaxCntrHaRRActiveListCnts = _CDnsMaxCntrHaRRActiveListCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 10, 7),
    _CDnsMaxCntrHaRRActiveListCnts_Type()
)
cDnsMaxCntrHaRRActiveListCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrHaRRActiveListCnts.setStatus("current")
_CDnsMaxCntrHaPersEditListCnts_Type = Counter32
_CDnsMaxCntrHaPersEditListCnts_Object = MibScalar
cDnsMaxCntrHaPersEditListCnts = _CDnsMaxCntrHaPersEditListCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 10, 8),
    _CDnsMaxCntrHaPersEditListCnts_Type()
)
cDnsMaxCntrHaPersEditListCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrHaPersEditListCnts.setStatus("current")
_CDnsMaxCntrHaUpdLatencyMax_Type = Gauge32
_CDnsMaxCntrHaUpdLatencyMax_Object = MibScalar
cDnsMaxCntrHaUpdLatencyMax = _CDnsMaxCntrHaUpdLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 10, 9),
    _CDnsMaxCntrHaUpdLatencyMax_Type()
)
cDnsMaxCntrHaUpdLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrHaUpdLatencyMax.setStatus("current")
if mibBuilder.loadTexts:
    cDnsMaxCntrHaUpdLatencyMax.setUnits("seconds")
_CDnsMaxCounterIntervalStats_ObjectIdentity = ObjectIdentity
cDnsMaxCounterIntervalStats = _CDnsMaxCounterIntervalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 11)
)
_CDnsMaxCntrIntConcurXfrsInCnts_Type = Unsigned32
_CDnsMaxCntrIntConcurXfrsInCnts_Object = MibScalar
cDnsMaxCntrIntConcurXfrsInCnts = _CDnsMaxCntrIntConcurXfrsInCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 11, 1),
    _CDnsMaxCntrIntConcurXfrsInCnts_Type()
)
cDnsMaxCntrIntConcurXfrsInCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrIntConcurXfrsInCnts.setStatus("current")
_CDnsMaxCntrIntConcurXfrsOutCnts_Type = Unsigned32
_CDnsMaxCntrIntConcurXfrsOutCnts_Object = MibScalar
cDnsMaxCntrIntConcurXfrsOutCnts = _CDnsMaxCntrIntConcurXfrsOutCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 11, 2),
    _CDnsMaxCntrIntConcurXfrsOutCnts_Type()
)
cDnsMaxCntrIntConcurXfrsOutCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrIntConcurXfrsOutCnts.setStatus("current")
_CDnsMaxCntrIntHaSvrNoRespTime_Type = TimeInterval
_CDnsMaxCntrIntHaSvrNoRespTime_Object = MibScalar
cDnsMaxCntrIntHaSvrNoRespTime = _CDnsMaxCntrIntHaSvrNoRespTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 11, 3),
    _CDnsMaxCntrIntHaSvrNoRespTime_Type()
)
cDnsMaxCntrIntHaSvrNoRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrIntHaSvrNoRespTime.setStatus("current")
if mibBuilder.loadTexts:
    cDnsMaxCntrIntHaSvrNoRespTime.setUnits("milliseconds")
_CDnsMaxCntrIntHaSvrMaxNoRespTime_Type = TimeInterval
_CDnsMaxCntrIntHaSvrMaxNoRespTime_Object = MibScalar
cDnsMaxCntrIntHaSvrMaxNoRespTime = _CDnsMaxCntrIntHaSvrMaxNoRespTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 11, 4),
    _CDnsMaxCntrIntHaSvrMaxNoRespTime_Type()
)
cDnsMaxCntrIntHaSvrMaxNoRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrIntHaSvrMaxNoRespTime.setStatus("current")
if mibBuilder.loadTexts:
    cDnsMaxCntrIntHaSvrMaxNoRespTime.setUnits("milliseconds")
_CDnsMaxCntrIntHaBatchLimitCnts_Type = Unsigned32
_CDnsMaxCntrIntHaBatchLimitCnts_Object = MibScalar
cDnsMaxCntrIntHaBatchLimitCnts = _CDnsMaxCntrIntHaBatchLimitCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 11, 5),
    _CDnsMaxCntrIntHaBatchLimitCnts_Type()
)
cDnsMaxCntrIntHaBatchLimitCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrIntHaBatchLimitCnts.setStatus("current")
_CDnsMaxCntrIntHaRRPendListCnts_Type = Unsigned32
_CDnsMaxCntrIntHaRRPendListCnts_Object = MibScalar
cDnsMaxCntrIntHaRRPendListCnts = _CDnsMaxCntrIntHaRRPendListCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 11, 6),
    _CDnsMaxCntrIntHaRRPendListCnts_Type()
)
cDnsMaxCntrIntHaRRPendListCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrIntHaRRPendListCnts.setStatus("current")
_CDnsMaxCntrIntHaRRActiveListCnts_Type = Unsigned32
_CDnsMaxCntrIntHaRRActiveListCnts_Object = MibScalar
cDnsMaxCntrIntHaRRActiveListCnts = _CDnsMaxCntrIntHaRRActiveListCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 11, 7),
    _CDnsMaxCntrIntHaRRActiveListCnts_Type()
)
cDnsMaxCntrIntHaRRActiveListCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrIntHaRRActiveListCnts.setStatus("current")
_CDnsMaxCntrIntHaPersEditListCnts_Type = Unsigned32
_CDnsMaxCntrIntHaPersEditListCnts_Object = MibScalar
cDnsMaxCntrIntHaPersEditListCnts = _CDnsMaxCntrIntHaPersEditListCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 11, 8),
    _CDnsMaxCntrIntHaPersEditListCnts_Type()
)
cDnsMaxCntrIntHaPersEditListCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrIntHaPersEditListCnts.setStatus("current")
_CDnsMaxCntrIntHaUpdLatencyMax_Type = Gauge32
_CDnsMaxCntrIntHaUpdLatencyMax_Object = MibScalar
cDnsMaxCntrIntHaUpdLatencyMax = _CDnsMaxCntrIntHaUpdLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 11, 9),
    _CDnsMaxCntrIntHaUpdLatencyMax_Type()
)
cDnsMaxCntrIntHaUpdLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrIntHaUpdLatencyMax.setStatus("current")
if mibBuilder.loadTexts:
    cDnsMaxCntrIntHaUpdLatencyMax.setUnits("seconds")
_CDnsMaxCntrIntSampleTime_Type = TimeStamp
_CDnsMaxCntrIntSampleTime_Object = MibScalar
cDnsMaxCntrIntSampleTime = _CDnsMaxCntrIntSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 11, 10),
    _CDnsMaxCntrIntSampleTime_Type()
)
cDnsMaxCntrIntSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrIntSampleTime.setStatus("current")
_CDnsMaxCntrIntSampleInterval_Type = TimeInterval
_CDnsMaxCntrIntSampleInterval_Object = MibScalar
cDnsMaxCntrIntSampleInterval = _CDnsMaxCntrIntSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 11, 11),
    _CDnsMaxCntrIntSampleInterval_Type()
)
cDnsMaxCntrIntSampleInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsMaxCntrIntSampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    cDnsMaxCntrIntSampleInterval.setUnits("milliseconds")
_CDnsHaStats_ObjectIdentity = ObjectIdentity
cDnsHaStats = _CDnsHaStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12)
)
_CDnsHaCommInterruptedStates_Type = Counter32
_CDnsHaCommInterruptedStates_Object = MibScalar
cDnsHaCommInterruptedStates = _CDnsHaCommInterruptedStates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 1),
    _CDnsHaCommInterruptedStates_Type()
)
cDnsHaCommInterruptedStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaCommInterruptedStates.setStatus("current")
_CDnsHaPartnerDownStates_Type = Counter32
_CDnsHaPartnerDownStates_Object = MibScalar
cDnsHaPartnerDownStates = _CDnsHaPartnerDownStates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 2),
    _CDnsHaPartnerDownStates_Type()
)
cDnsHaPartnerDownStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaPartnerDownStates.setStatus("current")
_CDnsHaSyncs_Type = Counter32
_CDnsHaSyncs_Object = MibScalar
cDnsHaSyncs = _CDnsHaSyncs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 3),
    _CDnsHaSyncs_Type()
)
cDnsHaSyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaSyncs.setStatus("current")
_CDnsHaMsgConnectSentCnts_Type = Counter32
_CDnsHaMsgConnectSentCnts_Object = MibScalar
cDnsHaMsgConnectSentCnts = _CDnsHaMsgConnectSentCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 4),
    _CDnsHaMsgConnectSentCnts_Type()
)
cDnsHaMsgConnectSentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaMsgConnectSentCnts.setStatus("current")
_CDnsHaMsgReconcileSentCnts_Type = Counter32
_CDnsHaMsgReconcileSentCnts_Object = MibScalar
cDnsHaMsgReconcileSentCnts = _CDnsHaMsgReconcileSentCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 5),
    _CDnsHaMsgReconcileSentCnts_Type()
)
cDnsHaMsgReconcileSentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaMsgReconcileSentCnts.setStatus("current")
_CDnsHaMsgHeartBeatSentCnts_Type = Counter32
_CDnsHaMsgHeartBeatSentCnts_Object = MibScalar
cDnsHaMsgHeartBeatSentCnts = _CDnsHaMsgHeartBeatSentCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 6),
    _CDnsHaMsgHeartBeatSentCnts_Type()
)
cDnsHaMsgHeartBeatSentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaMsgHeartBeatSentCnts.setStatus("current")
_CDnsHaMsgZoneSyncSentCnts_Type = Counter32
_CDnsHaMsgZoneSyncSentCnts_Object = MibScalar
cDnsHaMsgZoneSyncSentCnts = _CDnsHaMsgZoneSyncSentCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 7),
    _CDnsHaMsgZoneSyncSentCnts_Type()
)
cDnsHaMsgZoneSyncSentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaMsgZoneSyncSentCnts.setStatus("current")
_CDnsHaMsgRRSyncSentCnts_Type = Counter32
_CDnsHaMsgRRSyncSentCnts_Object = MibScalar
cDnsHaMsgRRSyncSentCnts = _CDnsHaMsgRRSyncSentCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 8),
    _CDnsHaMsgRRSyncSentCnts_Type()
)
cDnsHaMsgRRSyncSentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaMsgRRSyncSentCnts.setStatus("current")
_CDnsHaMsgRRUpdateSentCnts_Type = Counter32
_CDnsHaMsgRRUpdateSentCnts_Object = MibScalar
cDnsHaMsgRRUpdateSentCnts = _CDnsHaMsgRRUpdateSentCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 9),
    _CDnsHaMsgRRUpdateSentCnts_Type()
)
cDnsHaMsgRRUpdateSentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaMsgRRUpdateSentCnts.setStatus("current")
_CDnsHaMsgResponseSentCnts_Type = Counter32
_CDnsHaMsgResponseSentCnts_Object = MibScalar
cDnsHaMsgResponseSentCnts = _CDnsHaMsgResponseSentCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 10),
    _CDnsHaMsgResponseSentCnts_Type()
)
cDnsHaMsgResponseSentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaMsgResponseSentCnts.setStatus("current")
_CDnsHaMsgConnectRcvdCnts_Type = Counter32
_CDnsHaMsgConnectRcvdCnts_Object = MibScalar
cDnsHaMsgConnectRcvdCnts = _CDnsHaMsgConnectRcvdCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 11),
    _CDnsHaMsgConnectRcvdCnts_Type()
)
cDnsHaMsgConnectRcvdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaMsgConnectRcvdCnts.setStatus("current")
_CDnsHaMsgReconcileRcvdCnts_Type = Counter32
_CDnsHaMsgReconcileRcvdCnts_Object = MibScalar
cDnsHaMsgReconcileRcvdCnts = _CDnsHaMsgReconcileRcvdCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 12),
    _CDnsHaMsgReconcileRcvdCnts_Type()
)
cDnsHaMsgReconcileRcvdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaMsgReconcileRcvdCnts.setStatus("current")
_CDnsHaMsgHeartbeatRcvdCnts_Type = Counter32
_CDnsHaMsgHeartbeatRcvdCnts_Object = MibScalar
cDnsHaMsgHeartbeatRcvdCnts = _CDnsHaMsgHeartbeatRcvdCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 13),
    _CDnsHaMsgHeartbeatRcvdCnts_Type()
)
cDnsHaMsgHeartbeatRcvdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaMsgHeartbeatRcvdCnts.setStatus("current")
_CDnsHaMsgZoneSyncRcvdCnts_Type = Counter32
_CDnsHaMsgZoneSyncRcvdCnts_Object = MibScalar
cDnsHaMsgZoneSyncRcvdCnts = _CDnsHaMsgZoneSyncRcvdCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 14),
    _CDnsHaMsgZoneSyncRcvdCnts_Type()
)
cDnsHaMsgZoneSyncRcvdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaMsgZoneSyncRcvdCnts.setStatus("current")
_CDnsHaMsgRRSyncRcvdCnts_Type = Counter32
_CDnsHaMsgRRSyncRcvdCnts_Object = MibScalar
cDnsHaMsgRRSyncRcvdCnts = _CDnsHaMsgRRSyncRcvdCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 15),
    _CDnsHaMsgRRSyncRcvdCnts_Type()
)
cDnsHaMsgRRSyncRcvdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaMsgRRSyncRcvdCnts.setStatus("current")
_CDnsHaMsgRRUpdateRcvdCnts_Type = Counter32
_CDnsHaMsgRRUpdateRcvdCnts_Object = MibScalar
cDnsHaMsgRRUpdateRcvdCnts = _CDnsHaMsgRRUpdateRcvdCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 16),
    _CDnsHaMsgRRUpdateRcvdCnts_Type()
)
cDnsHaMsgRRUpdateRcvdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaMsgRRUpdateRcvdCnts.setStatus("current")
_CDnsHaMsgResponseRcvdCnts_Type = Counter32
_CDnsHaMsgResponseRcvdCnts_Object = MibScalar
cDnsHaMsgResponseRcvdCnts = _CDnsHaMsgResponseRcvdCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 17),
    _CDnsHaMsgResponseRcvdCnts_Type()
)
cDnsHaMsgResponseRcvdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaMsgResponseRcvdCnts.setStatus("current")
_CDnsHaHeartbeatTimeoutCnts_Type = Counter32
_CDnsHaHeartbeatTimeoutCnts_Object = MibScalar
cDnsHaHeartbeatTimeoutCnts = _CDnsHaHeartbeatTimeoutCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 18),
    _CDnsHaHeartbeatTimeoutCnts_Type()
)
cDnsHaHeartbeatTimeoutCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaHeartbeatTimeoutCnts.setStatus("current")
_CDnsHaUpdateRejectCnts_Type = Counter32
_CDnsHaUpdateRejectCnts_Object = MibScalar
cDnsHaUpdateRejectCnts = _CDnsHaUpdateRejectCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 19),
    _CDnsHaUpdateRejectCnts_Type()
)
cDnsHaUpdateRejectCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaUpdateRejectCnts.setStatus("current")
_CDnsHaResponseMismatchCnts_Type = Counter32
_CDnsHaResponseMismatchCnts_Object = MibScalar
cDnsHaResponseMismatchCnts = _CDnsHaResponseMismatchCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 20),
    _CDnsHaResponseMismatchCnts_Type()
)
cDnsHaResponseMismatchCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaResponseMismatchCnts.setStatus("current")
_CDnsHaResponseServFailCnts_Type = Counter32
_CDnsHaResponseServFailCnts_Object = MibScalar
cDnsHaResponseServFailCnts = _CDnsHaResponseServFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 21),
    _CDnsHaResponseServFailCnts_Type()
)
cDnsHaResponseServFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaResponseServFailCnts.setStatus("current")
_CDnsHaRespInconsistentCnts_Type = Counter32
_CDnsHaRespInconsistentCnts_Object = MibScalar
cDnsHaRespInconsistentCnts = _CDnsHaRespInconsistentCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 22),
    _CDnsHaRespInconsistentCnts_Type()
)
cDnsHaRespInconsistentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaRespInconsistentCnts.setStatus("current")
_CDnsHaRespUnknownCnts_Type = Counter32
_CDnsHaRespUnknownCnts_Object = MibScalar
cDnsHaRespUnknownCnts = _CDnsHaRespUnknownCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 23),
    _CDnsHaRespUnknownCnts_Type()
)
cDnsHaRespUnknownCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaRespUnknownCnts.setStatus("current")
_CDnsHaFullZoneResyncCnts_Type = Counter32
_CDnsHaFullZoneResyncCnts_Object = MibScalar
cDnsHaFullZoneResyncCnts = _CDnsHaFullZoneResyncCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 24),
    _CDnsHaFullZoneResyncCnts_Type()
)
cDnsHaFullZoneResyncCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaFullZoneResyncCnts.setStatus("current")
_CDnsHaUpdatePrivateReqCnts_Type = Counter32
_CDnsHaUpdatePrivateReqCnts_Object = MibScalar
cDnsHaUpdatePrivateReqCnts = _CDnsHaUpdatePrivateReqCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 25),
    _CDnsHaUpdatePrivateReqCnts_Type()
)
cDnsHaUpdatePrivateReqCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaUpdatePrivateReqCnts.setStatus("current")
_CDnsHaUpdatePrivateRespCnts_Type = Counter32
_CDnsHaUpdatePrivateRespCnts_Object = MibScalar
cDnsHaUpdatePrivateRespCnts = _CDnsHaUpdatePrivateRespCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 26),
    _CDnsHaUpdatePrivateRespCnts_Type()
)
cDnsHaUpdatePrivateRespCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaUpdatePrivateRespCnts.setStatus("current")
_CDnsHaSyncConflictCnts_Type = Counter32
_CDnsHaSyncConflictCnts_Object = MibScalar
cDnsHaSyncConflictCnts = _CDnsHaSyncConflictCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 27),
    _CDnsHaSyncConflictCnts_Type()
)
cDnsHaSyncConflictCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaSyncConflictCnts.setStatus("current")
_CDnsHaSyncDiscardNameCnts_Type = Counter32
_CDnsHaSyncDiscardNameCnts_Object = MibScalar
cDnsHaSyncDiscardNameCnts = _CDnsHaSyncDiscardNameCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 28),
    _CDnsHaSyncDiscardNameCnts_Type()
)
cDnsHaSyncDiscardNameCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaSyncDiscardNameCnts.setStatus("current")
_CDnsHaSyncMergeNameCnts_Type = Counter32
_CDnsHaSyncMergeNameCnts_Object = MibScalar
cDnsHaSyncMergeNameCnts = _CDnsHaSyncMergeNameCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 29),
    _CDnsHaSyncMergeNameCnts_Type()
)
cDnsHaSyncMergeNameCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaSyncMergeNameCnts.setStatus("current")
_CDnsHaUpdateLatencyAverage_Type = Gauge32
_CDnsHaUpdateLatencyAverage_Object = MibScalar
cDnsHaUpdateLatencyAverage = _CDnsHaUpdateLatencyAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 12, 30),
    _CDnsHaUpdateLatencyAverage_Type()
)
cDnsHaUpdateLatencyAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaUpdateLatencyAverage.setStatus("current")
if mibBuilder.loadTexts:
    cDnsHaUpdateLatencyAverage.setUnits("seconds")
_CDnsHaIntervalStats_ObjectIdentity = ObjectIdentity
cDnsHaIntervalStats = _CDnsHaIntervalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13)
)
_CDnsHaIntCommInterruptedStates_Type = Unsigned32
_CDnsHaIntCommInterruptedStates_Object = MibScalar
cDnsHaIntCommInterruptedStates = _CDnsHaIntCommInterruptedStates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 1),
    _CDnsHaIntCommInterruptedStates_Type()
)
cDnsHaIntCommInterruptedStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntCommInterruptedStates.setStatus("current")
_CDnsHaIntPartnerDownStates_Type = Unsigned32
_CDnsHaIntPartnerDownStates_Object = MibScalar
cDnsHaIntPartnerDownStates = _CDnsHaIntPartnerDownStates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 2),
    _CDnsHaIntPartnerDownStates_Type()
)
cDnsHaIntPartnerDownStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntPartnerDownStates.setStatus("current")
_CDnsHaIntSyncs_Type = Unsigned32
_CDnsHaIntSyncs_Object = MibScalar
cDnsHaIntSyncs = _CDnsHaIntSyncs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 3),
    _CDnsHaIntSyncs_Type()
)
cDnsHaIntSyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntSyncs.setStatus("current")
_CDnsHaIntMsgConnectSentCnts_Type = Unsigned32
_CDnsHaIntMsgConnectSentCnts_Object = MibScalar
cDnsHaIntMsgConnectSentCnts = _CDnsHaIntMsgConnectSentCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 4),
    _CDnsHaIntMsgConnectSentCnts_Type()
)
cDnsHaIntMsgConnectSentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntMsgConnectSentCnts.setStatus("current")
_CDnsHaIntMsgReconcileSentCnts_Type = Unsigned32
_CDnsHaIntMsgReconcileSentCnts_Object = MibScalar
cDnsHaIntMsgReconcileSentCnts = _CDnsHaIntMsgReconcileSentCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 5),
    _CDnsHaIntMsgReconcileSentCnts_Type()
)
cDnsHaIntMsgReconcileSentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntMsgReconcileSentCnts.setStatus("current")
_CDnsHaIntMsgHeartBeatSentCnts_Type = Unsigned32
_CDnsHaIntMsgHeartBeatSentCnts_Object = MibScalar
cDnsHaIntMsgHeartBeatSentCnts = _CDnsHaIntMsgHeartBeatSentCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 6),
    _CDnsHaIntMsgHeartBeatSentCnts_Type()
)
cDnsHaIntMsgHeartBeatSentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntMsgHeartBeatSentCnts.setStatus("current")
_CDnsHaIntMsgZoneSyncSentCnts_Type = Unsigned32
_CDnsHaIntMsgZoneSyncSentCnts_Object = MibScalar
cDnsHaIntMsgZoneSyncSentCnts = _CDnsHaIntMsgZoneSyncSentCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 7),
    _CDnsHaIntMsgZoneSyncSentCnts_Type()
)
cDnsHaIntMsgZoneSyncSentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntMsgZoneSyncSentCnts.setStatus("current")
_CDnsHaIntMsgRRSyncSentCnts_Type = Unsigned32
_CDnsHaIntMsgRRSyncSentCnts_Object = MibScalar
cDnsHaIntMsgRRSyncSentCnts = _CDnsHaIntMsgRRSyncSentCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 8),
    _CDnsHaIntMsgRRSyncSentCnts_Type()
)
cDnsHaIntMsgRRSyncSentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntMsgRRSyncSentCnts.setStatus("current")
_CDnsHaIntMsgRRUpdateSentCnts_Type = Unsigned32
_CDnsHaIntMsgRRUpdateSentCnts_Object = MibScalar
cDnsHaIntMsgRRUpdateSentCnts = _CDnsHaIntMsgRRUpdateSentCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 9),
    _CDnsHaIntMsgRRUpdateSentCnts_Type()
)
cDnsHaIntMsgRRUpdateSentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntMsgRRUpdateSentCnts.setStatus("current")
_CDnsHaIntMsgResponseSentCnts_Type = Unsigned32
_CDnsHaIntMsgResponseSentCnts_Object = MibScalar
cDnsHaIntMsgResponseSentCnts = _CDnsHaIntMsgResponseSentCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 10),
    _CDnsHaIntMsgResponseSentCnts_Type()
)
cDnsHaIntMsgResponseSentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntMsgResponseSentCnts.setStatus("current")
_CDnsHaIntMsgConnectRcvdCnts_Type = Unsigned32
_CDnsHaIntMsgConnectRcvdCnts_Object = MibScalar
cDnsHaIntMsgConnectRcvdCnts = _CDnsHaIntMsgConnectRcvdCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 11),
    _CDnsHaIntMsgConnectRcvdCnts_Type()
)
cDnsHaIntMsgConnectRcvdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntMsgConnectRcvdCnts.setStatus("current")
_CDnsHaIntMsgReconcileRcvdCnts_Type = Unsigned32
_CDnsHaIntMsgReconcileRcvdCnts_Object = MibScalar
cDnsHaIntMsgReconcileRcvdCnts = _CDnsHaIntMsgReconcileRcvdCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 12),
    _CDnsHaIntMsgReconcileRcvdCnts_Type()
)
cDnsHaIntMsgReconcileRcvdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntMsgReconcileRcvdCnts.setStatus("current")
_CDnsHaIntMsgHeartbeatRcvdCnts_Type = Unsigned32
_CDnsHaIntMsgHeartbeatRcvdCnts_Object = MibScalar
cDnsHaIntMsgHeartbeatRcvdCnts = _CDnsHaIntMsgHeartbeatRcvdCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 13),
    _CDnsHaIntMsgHeartbeatRcvdCnts_Type()
)
cDnsHaIntMsgHeartbeatRcvdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntMsgHeartbeatRcvdCnts.setStatus("current")
_CDnsHaIntMsgZoneSyncRcvdCnts_Type = Unsigned32
_CDnsHaIntMsgZoneSyncRcvdCnts_Object = MibScalar
cDnsHaIntMsgZoneSyncRcvdCnts = _CDnsHaIntMsgZoneSyncRcvdCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 14),
    _CDnsHaIntMsgZoneSyncRcvdCnts_Type()
)
cDnsHaIntMsgZoneSyncRcvdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntMsgZoneSyncRcvdCnts.setStatus("current")
_CDnsHaIntMsgRRSyncRcvdCnts_Type = Unsigned32
_CDnsHaIntMsgRRSyncRcvdCnts_Object = MibScalar
cDnsHaIntMsgRRSyncRcvdCnts = _CDnsHaIntMsgRRSyncRcvdCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 15),
    _CDnsHaIntMsgRRSyncRcvdCnts_Type()
)
cDnsHaIntMsgRRSyncRcvdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntMsgRRSyncRcvdCnts.setStatus("current")
_CDnsHaIntMsgRRUpdateRcvdCnts_Type = Unsigned32
_CDnsHaIntMsgRRUpdateRcvdCnts_Object = MibScalar
cDnsHaIntMsgRRUpdateRcvdCnts = _CDnsHaIntMsgRRUpdateRcvdCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 16),
    _CDnsHaIntMsgRRUpdateRcvdCnts_Type()
)
cDnsHaIntMsgRRUpdateRcvdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntMsgRRUpdateRcvdCnts.setStatus("current")
_CDnsHaIntMsgResponseRcvdCnts_Type = Unsigned32
_CDnsHaIntMsgResponseRcvdCnts_Object = MibScalar
cDnsHaIntMsgResponseRcvdCnts = _CDnsHaIntMsgResponseRcvdCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 17),
    _CDnsHaIntMsgResponseRcvdCnts_Type()
)
cDnsHaIntMsgResponseRcvdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntMsgResponseRcvdCnts.setStatus("current")
_CDnsHaIntHeartbeatTimeoutCnts_Type = Unsigned32
_CDnsHaIntHeartbeatTimeoutCnts_Object = MibScalar
cDnsHaIntHeartbeatTimeoutCnts = _CDnsHaIntHeartbeatTimeoutCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 18),
    _CDnsHaIntHeartbeatTimeoutCnts_Type()
)
cDnsHaIntHeartbeatTimeoutCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntHeartbeatTimeoutCnts.setStatus("current")
_CDnsHaIntUpdateRejectCnts_Type = Unsigned32
_CDnsHaIntUpdateRejectCnts_Object = MibScalar
cDnsHaIntUpdateRejectCnts = _CDnsHaIntUpdateRejectCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 19),
    _CDnsHaIntUpdateRejectCnts_Type()
)
cDnsHaIntUpdateRejectCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntUpdateRejectCnts.setStatus("current")
_CDnsHaIntResponseMismatchCnts_Type = Unsigned32
_CDnsHaIntResponseMismatchCnts_Object = MibScalar
cDnsHaIntResponseMismatchCnts = _CDnsHaIntResponseMismatchCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 20),
    _CDnsHaIntResponseMismatchCnts_Type()
)
cDnsHaIntResponseMismatchCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntResponseMismatchCnts.setStatus("current")
_CDnsHaIntResponseServFailCnts_Type = Unsigned32
_CDnsHaIntResponseServFailCnts_Object = MibScalar
cDnsHaIntResponseServFailCnts = _CDnsHaIntResponseServFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 21),
    _CDnsHaIntResponseServFailCnts_Type()
)
cDnsHaIntResponseServFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntResponseServFailCnts.setStatus("current")
_CDnsHaIntRespInconsistentCnts_Type = Unsigned32
_CDnsHaIntRespInconsistentCnts_Object = MibScalar
cDnsHaIntRespInconsistentCnts = _CDnsHaIntRespInconsistentCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 22),
    _CDnsHaIntRespInconsistentCnts_Type()
)
cDnsHaIntRespInconsistentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntRespInconsistentCnts.setStatus("current")
_CDnsHaIntRespUnknownCnts_Type = Unsigned32
_CDnsHaIntRespUnknownCnts_Object = MibScalar
cDnsHaIntRespUnknownCnts = _CDnsHaIntRespUnknownCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 23),
    _CDnsHaIntRespUnknownCnts_Type()
)
cDnsHaIntRespUnknownCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntRespUnknownCnts.setStatus("current")
_CDnsHaIntFullZoneResyncCnts_Type = Unsigned32
_CDnsHaIntFullZoneResyncCnts_Object = MibScalar
cDnsHaIntFullZoneResyncCnts = _CDnsHaIntFullZoneResyncCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 24),
    _CDnsHaIntFullZoneResyncCnts_Type()
)
cDnsHaIntFullZoneResyncCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntFullZoneResyncCnts.setStatus("current")
_CDnsHaIntUpdatePrivateReqCnts_Type = Unsigned32
_CDnsHaIntUpdatePrivateReqCnts_Object = MibScalar
cDnsHaIntUpdatePrivateReqCnts = _CDnsHaIntUpdatePrivateReqCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 25),
    _CDnsHaIntUpdatePrivateReqCnts_Type()
)
cDnsHaIntUpdatePrivateReqCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntUpdatePrivateReqCnts.setStatus("current")
_CDnsHaIntUpdatePrivateRespCnts_Type = Unsigned32
_CDnsHaIntUpdatePrivateRespCnts_Object = MibScalar
cDnsHaIntUpdatePrivateRespCnts = _CDnsHaIntUpdatePrivateRespCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 26),
    _CDnsHaIntUpdatePrivateRespCnts_Type()
)
cDnsHaIntUpdatePrivateRespCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntUpdatePrivateRespCnts.setStatus("current")
_CDnsHaIntSyncConflictCnts_Type = Unsigned32
_CDnsHaIntSyncConflictCnts_Object = MibScalar
cDnsHaIntSyncConflictCnts = _CDnsHaIntSyncConflictCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 27),
    _CDnsHaIntSyncConflictCnts_Type()
)
cDnsHaIntSyncConflictCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntSyncConflictCnts.setStatus("current")
_CDnsHaIntSyncDiscardNameCnts_Type = Unsigned32
_CDnsHaIntSyncDiscardNameCnts_Object = MibScalar
cDnsHaIntSyncDiscardNameCnts = _CDnsHaIntSyncDiscardNameCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 28),
    _CDnsHaIntSyncDiscardNameCnts_Type()
)
cDnsHaIntSyncDiscardNameCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntSyncDiscardNameCnts.setStatus("current")
_CDnsHaIntSyncMergeNameCnts_Type = Unsigned32
_CDnsHaIntSyncMergeNameCnts_Object = MibScalar
cDnsHaIntSyncMergeNameCnts = _CDnsHaIntSyncMergeNameCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 29),
    _CDnsHaIntSyncMergeNameCnts_Type()
)
cDnsHaIntSyncMergeNameCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntSyncMergeNameCnts.setStatus("current")
_CDnsHaIntUpdateLatencyAverage_Type = Gauge32
_CDnsHaIntUpdateLatencyAverage_Object = MibScalar
cDnsHaIntUpdateLatencyAverage = _CDnsHaIntUpdateLatencyAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 30),
    _CDnsHaIntUpdateLatencyAverage_Type()
)
cDnsHaIntUpdateLatencyAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntUpdateLatencyAverage.setStatus("current")
if mibBuilder.loadTexts:
    cDnsHaIntUpdateLatencyAverage.setUnits("seconds")
_CDnsHaIntSampleTime_Type = TimeStamp
_CDnsHaIntSampleTime_Object = MibScalar
cDnsHaIntSampleTime = _CDnsHaIntSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 31),
    _CDnsHaIntSampleTime_Type()
)
cDnsHaIntSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntSampleTime.setStatus("current")
_CDnsHaIntSampleInterval_Type = TimeInterval
_CDnsHaIntSampleInterval_Object = MibScalar
cDnsHaIntSampleInterval = _CDnsHaIntSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 1, 13, 32),
    _CDnsHaIntSampleInterval_Type()
)
cDnsHaIntSampleInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDnsHaIntSampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    cDnsHaIntSampleInterval.setUnits("milliseconds")
_CDnsServMIBConform_ObjectIdentity = ObjectIdentity
cDnsServMIBConform = _CDnsServMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 2)
)
_CDnsServMIBCompliances_ObjectIdentity = ObjectIdentity
cDnsServMIBCompliances = _CDnsServMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 2, 1)
)
_CDnsServMIBGroups_ObjectIdentity = ObjectIdentity
cDnsServMIBGroups = _CDnsServMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 2, 2)
)

# Managed Objects groups

cDnsServConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 2, 2, 1)
)
cDnsServConfigGroup.setObjects(
      *(("CISCO-DNS-SERVER-MIB", "cDnsServConfigImplementIdent"),
        ("CISCO-DNS-SERVER-MIB", "cDnsServConfigRecurs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsServConfigUpTime"),
        ("CISCO-DNS-SERVER-MIB", "cDnsServConfigResetTime"),
        ("CISCO-DNS-SERVER-MIB", "cDnsServConfigReset"),
        ("CISCO-DNS-SERVER-MIB", "cDnsServConfigIntervalSample"))
)
if mibBuilder.loadTexts:
    cDnsServConfigGroup.setStatus("current")

cDnsQueryStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 2, 2, 2)
)
cDnsQueryStatsGroup.setObjects(
      *(("CISCO-DNS-SERVER-MIB", "cDnsQueryAuthAnswers"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryAuthNoNames"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryAuthNoDataResps"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryReferrals"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryNonAuthAnswers"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryNonAuthNoDataResps"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryRelNameRequests"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryLameDelegations"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryMemCacheHits"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryMemCacheMisses"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryMemCacheWrites"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryRefusals"))
)
if mibBuilder.loadTexts:
    cDnsQueryStatsGroup.setStatus("current")

cDnsQueryStatsIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 2, 2, 3)
)
cDnsQueryStatsIntervalGroup.setObjects(
      *(("CISCO-DNS-SERVER-MIB", "cDnsQueryIntAuthAnswers"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryIntAuthNoNames"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryIntAuthNoDataResps"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryIntReferrals"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryIntNonAuthAnswers"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryIntNonAuthNoDataResps"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryIntRelNameRequests"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryIntLameDelegations"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryIntMemCacheHits"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryIntMemCacheMisses"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryIntMemCacheWrites"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryIntRefusals"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryIntSampleTime"),
        ("CISCO-DNS-SERVER-MIB", "cDnsQueryIntSampleInterval"))
)
if mibBuilder.loadTexts:
    cDnsQueryStatsIntervalGroup.setStatus("current")

cDnsPerfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 2, 2, 4)
)
cDnsPerfStatsGroup.setObjects(
      *(("CISCO-DNS-SERVER-MIB", "cDnsPerfUpdateRRs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfUpdatePkts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfOutboundIxfrs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfInboundIxfrs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfFullRespIxfrs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfOutboundAxfrs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfInboundAxfrs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfQueries"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfOutboundAtLimitXfrs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfInboundAtLimitXfrs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfOutboundNotifies"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfInboundNotifies"))
)
if mibBuilder.loadTexts:
    cDnsPerfStatsGroup.setStatus("current")

cDnsPerfStatsIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 2, 2, 5)
)
cDnsPerfStatsIntervalGroup.setObjects(
      *(("CISCO-DNS-SERVER-MIB", "cDnsPerfIntUpdateRRs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfIntUpdatePkts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfIntOutboundIxfrs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfIntInboundIxfrs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfIntFullRespIxfrs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfIntOutboundAxfrs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfIntInboundAxfrs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfIntQueries"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfIntOutboundAtLimitXfrs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfIntInboundAtLimitXfrs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfIntOutboundNotifies"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfIntInboundNotifies"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfIntSampleTime"),
        ("CISCO-DNS-SERVER-MIB", "cDnsPerfIntSampleInterval"))
)
if mibBuilder.loadTexts:
    cDnsPerfStatsIntervalGroup.setStatus("current")

cDnsSecurityStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 2, 2, 6)
)
cDnsSecurityStatsGroup.setObjects(
      *(("CISCO-DNS-SERVER-MIB", "cDnsSecurityRcvdTsigPackets"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityDetecTsigBadTimes"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityDetectTsigBadKeys"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityDetectTsigBadSigs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityRcvdTsigBadTimes"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityRcvdTsigBadKeys"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityRcvdTsigBadSigs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityUnauthXferReqs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityUnauthUpdateReqs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityRestrictQueryAcls"))
)
if mibBuilder.loadTexts:
    cDnsSecurityStatsGroup.setStatus("current")

cDnsSecurityStatsIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 2, 2, 7)
)
cDnsSecurityStatsIntervalGroup.setObjects(
      *(("CISCO-DNS-SERVER-MIB", "cDnsSecurityIntRcvdTsigPackets"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityIntDetecTsigBadTimes"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityIntDetectTsigBadKeys"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityIntDetectTsigBadSigs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityIntRcvdTsigBadTimes"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityIntRcvdTsigBadKeys"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityIntRcvdTsigBadSigs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityIntUnauthXferReqs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityIntUnauthUpdateReqs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityIntRestrictQueryAcls"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityIntSampleTime"),
        ("CISCO-DNS-SERVER-MIB", "cDnsSecurityIntSampleInterval"))
)
if mibBuilder.loadTexts:
    cDnsSecurityStatsIntervalGroup.setStatus("current")

cDnsErrorStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 2, 2, 8)
)
cDnsErrorStatsGroup.setObjects(
      *(("CISCO-DNS-SERVER-MIB", "cDnsErrorUpdateErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorIxfrInErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorIxfrOutErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorAxfrInErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorAxfrOutErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorSentTotalErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorSentFormatErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorSentOtherErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorSentRefusalErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorRcvdFormatErrors"))
)
if mibBuilder.loadTexts:
    cDnsErrorStatsGroup.setStatus("current")

cDnsErrorStatsIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 2, 2, 9)
)
cDnsErrorStatsIntervalGroup.setObjects(
      *(("CISCO-DNS-SERVER-MIB", "cDnsErrorIntUpdateErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorIntIxfrInErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorIntIxfrOutErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorIntAxfrInErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorIntAxfrOutErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorIntSentTotalErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorIntSentFormatErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorIntSentOtherErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorIntSentRefusalErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorIntRcvdFormatErrors"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorIntSampleTime"),
        ("CISCO-DNS-SERVER-MIB", "cDnsErrorIntSampleInterval"))
)
if mibBuilder.loadTexts:
    cDnsErrorStatsIntervalGroup.setStatus("current")

cDnsMaxCounterStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 2, 2, 10)
)
cDnsMaxCounterStatsGroup.setObjects(
      *(("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrConcurXfrsInCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrConcurXfrsOutCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrHaSvrNoRespTime"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrHaSvrMaxNoRespTime"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrHaBatchLimitCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrHaRRPendListCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrHaRRActiveListCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrHaPersEditListCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrHaUpdLatencyMax"))
)
if mibBuilder.loadTexts:
    cDnsMaxCounterStatsGroup.setStatus("current")

cDnsMaxCounterStatsIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 2, 2, 11)
)
cDnsMaxCounterStatsIntervalGroup.setObjects(
      *(("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrIntConcurXfrsInCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrIntConcurXfrsOutCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrIntHaSvrNoRespTime"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrIntHaSvrMaxNoRespTime"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrIntHaBatchLimitCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrIntHaRRPendListCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrIntHaRRActiveListCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrIntHaPersEditListCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrIntHaUpdLatencyMax"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrIntSampleTime"),
        ("CISCO-DNS-SERVER-MIB", "cDnsMaxCntrIntSampleInterval"))
)
if mibBuilder.loadTexts:
    cDnsMaxCounterStatsIntervalGroup.setStatus("current")

cDnsHaStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 2, 2, 12)
)
cDnsHaStatsGroup.setObjects(
      *(("CISCO-DNS-SERVER-MIB", "cDnsHaCommInterruptedStates"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaPartnerDownStates"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaSyncs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaMsgConnectSentCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaMsgReconcileSentCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaMsgHeartBeatSentCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaMsgZoneSyncSentCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaMsgRRSyncSentCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaMsgRRUpdateSentCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaMsgResponseSentCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaMsgConnectRcvdCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaMsgReconcileRcvdCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaMsgHeartbeatRcvdCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaMsgZoneSyncRcvdCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaMsgRRSyncRcvdCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaMsgRRUpdateRcvdCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaMsgResponseRcvdCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaHeartbeatTimeoutCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaUpdateRejectCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaResponseMismatchCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaResponseServFailCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaRespInconsistentCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaRespUnknownCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaFullZoneResyncCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaUpdatePrivateReqCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaUpdatePrivateRespCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaSyncConflictCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaSyncDiscardNameCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaSyncMergeNameCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaUpdateLatencyAverage"))
)
if mibBuilder.loadTexts:
    cDnsHaStatsGroup.setStatus("current")

cDnsHaStatsIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 2, 2, 13)
)
cDnsHaStatsIntervalGroup.setObjects(
      *(("CISCO-DNS-SERVER-MIB", "cDnsHaIntCommInterruptedStates"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntPartnerDownStates"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntSyncs"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntMsgConnectSentCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntMsgReconcileSentCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntMsgHeartBeatSentCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntMsgZoneSyncSentCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntMsgRRSyncSentCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntMsgRRUpdateSentCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntMsgResponseSentCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntMsgConnectRcvdCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntMsgReconcileRcvdCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntMsgHeartbeatRcvdCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntMsgZoneSyncRcvdCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntMsgRRSyncRcvdCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntMsgRRUpdateRcvdCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntMsgResponseRcvdCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntHeartbeatTimeoutCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntUpdateRejectCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntResponseMismatchCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntResponseServFailCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntRespInconsistentCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntRespUnknownCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntFullZoneResyncCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntUpdatePrivateReqCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntUpdatePrivateRespCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntSyncConflictCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntSyncDiscardNameCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntSyncMergeNameCnts"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntUpdateLatencyAverage"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntSampleTime"),
        ("CISCO-DNS-SERVER-MIB", "cDnsHaIntSampleInterval"))
)
if mibBuilder.loadTexts:
    cDnsHaStatsIntervalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cDnsServMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 405, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cDnsServMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DNS-SERVER-MIB",
    **{"CDnsTime": CDnsTime,
       "ciscoDnsServerMIB": ciscoDnsServerMIB,
       "cDnsServMIBNotifs": cDnsServMIBNotifs,
       "cDnsServMIBObjects": cDnsServMIBObjects,
       "cDnsServConfig": cDnsServConfig,
       "cDnsServConfigImplementIdent": cDnsServConfigImplementIdent,
       "cDnsServConfigRecurs": cDnsServConfigRecurs,
       "cDnsServConfigUpTime": cDnsServConfigUpTime,
       "cDnsServConfigResetTime": cDnsServConfigResetTime,
       "cDnsServConfigReset": cDnsServConfigReset,
       "cDnsServConfigIntervalSample": cDnsServConfigIntervalSample,
       "cDnsQueryStats": cDnsQueryStats,
       "cDnsQueryAuthAnswers": cDnsQueryAuthAnswers,
       "cDnsQueryAuthNoNames": cDnsQueryAuthNoNames,
       "cDnsQueryAuthNoDataResps": cDnsQueryAuthNoDataResps,
       "cDnsQueryReferrals": cDnsQueryReferrals,
       "cDnsQueryNonAuthAnswers": cDnsQueryNonAuthAnswers,
       "cDnsQueryNonAuthNoDataResps": cDnsQueryNonAuthNoDataResps,
       "cDnsQueryRelNameRequests": cDnsQueryRelNameRequests,
       "cDnsQueryLameDelegations": cDnsQueryLameDelegations,
       "cDnsQueryMemCacheHits": cDnsQueryMemCacheHits,
       "cDnsQueryMemCacheMisses": cDnsQueryMemCacheMisses,
       "cDnsQueryMemCacheWrites": cDnsQueryMemCacheWrites,
       "cDnsQueryRefusals": cDnsQueryRefusals,
       "cDnsQueryIntervalStats": cDnsQueryIntervalStats,
       "cDnsQueryIntAuthAnswers": cDnsQueryIntAuthAnswers,
       "cDnsQueryIntAuthNoNames": cDnsQueryIntAuthNoNames,
       "cDnsQueryIntAuthNoDataResps": cDnsQueryIntAuthNoDataResps,
       "cDnsQueryIntReferrals": cDnsQueryIntReferrals,
       "cDnsQueryIntNonAuthAnswers": cDnsQueryIntNonAuthAnswers,
       "cDnsQueryIntNonAuthNoDataResps": cDnsQueryIntNonAuthNoDataResps,
       "cDnsQueryIntRelNameRequests": cDnsQueryIntRelNameRequests,
       "cDnsQueryIntLameDelegations": cDnsQueryIntLameDelegations,
       "cDnsQueryIntMemCacheHits": cDnsQueryIntMemCacheHits,
       "cDnsQueryIntMemCacheMisses": cDnsQueryIntMemCacheMisses,
       "cDnsQueryIntMemCacheWrites": cDnsQueryIntMemCacheWrites,
       "cDnsQueryIntRefusals": cDnsQueryIntRefusals,
       "cDnsQueryIntSampleTime": cDnsQueryIntSampleTime,
       "cDnsQueryIntSampleInterval": cDnsQueryIntSampleInterval,
       "cDnsPerfStats": cDnsPerfStats,
       "cDnsPerfUpdateRRs": cDnsPerfUpdateRRs,
       "cDnsPerfUpdatePkts": cDnsPerfUpdatePkts,
       "cDnsPerfOutboundIxfrs": cDnsPerfOutboundIxfrs,
       "cDnsPerfInboundIxfrs": cDnsPerfInboundIxfrs,
       "cDnsPerfFullRespIxfrs": cDnsPerfFullRespIxfrs,
       "cDnsPerfOutboundAxfrs": cDnsPerfOutboundAxfrs,
       "cDnsPerfInboundAxfrs": cDnsPerfInboundAxfrs,
       "cDnsPerfQueries": cDnsPerfQueries,
       "cDnsPerfOutboundAtLimitXfrs": cDnsPerfOutboundAtLimitXfrs,
       "cDnsPerfInboundAtLimitXfrs": cDnsPerfInboundAtLimitXfrs,
       "cDnsPerfOutboundNotifies": cDnsPerfOutboundNotifies,
       "cDnsPerfInboundNotifies": cDnsPerfInboundNotifies,
       "cDnsPerfIntervalStats": cDnsPerfIntervalStats,
       "cDnsPerfIntUpdateRRs": cDnsPerfIntUpdateRRs,
       "cDnsPerfIntUpdatePkts": cDnsPerfIntUpdatePkts,
       "cDnsPerfIntOutboundIxfrs": cDnsPerfIntOutboundIxfrs,
       "cDnsPerfIntInboundIxfrs": cDnsPerfIntInboundIxfrs,
       "cDnsPerfIntFullRespIxfrs": cDnsPerfIntFullRespIxfrs,
       "cDnsPerfIntOutboundAxfrs": cDnsPerfIntOutboundAxfrs,
       "cDnsPerfIntInboundAxfrs": cDnsPerfIntInboundAxfrs,
       "cDnsPerfIntQueries": cDnsPerfIntQueries,
       "cDnsPerfIntOutboundAtLimitXfrs": cDnsPerfIntOutboundAtLimitXfrs,
       "cDnsPerfIntInboundAtLimitXfrs": cDnsPerfIntInboundAtLimitXfrs,
       "cDnsPerfIntOutboundNotifies": cDnsPerfIntOutboundNotifies,
       "cDnsPerfIntInboundNotifies": cDnsPerfIntInboundNotifies,
       "cDnsPerfIntSampleTime": cDnsPerfIntSampleTime,
       "cDnsPerfIntSampleInterval": cDnsPerfIntSampleInterval,
       "cDnsSecurityStats": cDnsSecurityStats,
       "cDnsSecurityRcvdTsigPackets": cDnsSecurityRcvdTsigPackets,
       "cDnsSecurityDetecTsigBadTimes": cDnsSecurityDetecTsigBadTimes,
       "cDnsSecurityDetectTsigBadKeys": cDnsSecurityDetectTsigBadKeys,
       "cDnsSecurityDetectTsigBadSigs": cDnsSecurityDetectTsigBadSigs,
       "cDnsSecurityRcvdTsigBadTimes": cDnsSecurityRcvdTsigBadTimes,
       "cDnsSecurityRcvdTsigBadKeys": cDnsSecurityRcvdTsigBadKeys,
       "cDnsSecurityRcvdTsigBadSigs": cDnsSecurityRcvdTsigBadSigs,
       "cDnsSecurityUnauthXferReqs": cDnsSecurityUnauthXferReqs,
       "cDnsSecurityUnauthUpdateReqs": cDnsSecurityUnauthUpdateReqs,
       "cDnsSecurityRestrictQueryAcls": cDnsSecurityRestrictQueryAcls,
       "cDnsSecurityIntervalStats": cDnsSecurityIntervalStats,
       "cDnsSecurityIntRcvdTsigPackets": cDnsSecurityIntRcvdTsigPackets,
       "cDnsSecurityIntDetecTsigBadTimes": cDnsSecurityIntDetecTsigBadTimes,
       "cDnsSecurityIntDetectTsigBadKeys": cDnsSecurityIntDetectTsigBadKeys,
       "cDnsSecurityIntDetectTsigBadSigs": cDnsSecurityIntDetectTsigBadSigs,
       "cDnsSecurityIntRcvdTsigBadTimes": cDnsSecurityIntRcvdTsigBadTimes,
       "cDnsSecurityIntRcvdTsigBadKeys": cDnsSecurityIntRcvdTsigBadKeys,
       "cDnsSecurityIntRcvdTsigBadSigs": cDnsSecurityIntRcvdTsigBadSigs,
       "cDnsSecurityIntUnauthXferReqs": cDnsSecurityIntUnauthXferReqs,
       "cDnsSecurityIntUnauthUpdateReqs": cDnsSecurityIntUnauthUpdateReqs,
       "cDnsSecurityIntRestrictQueryAcls": cDnsSecurityIntRestrictQueryAcls,
       "cDnsSecurityIntSampleTime": cDnsSecurityIntSampleTime,
       "cDnsSecurityIntSampleInterval": cDnsSecurityIntSampleInterval,
       "cDnsErrorStats": cDnsErrorStats,
       "cDnsErrorUpdateErrors": cDnsErrorUpdateErrors,
       "cDnsErrorIxfrInErrors": cDnsErrorIxfrInErrors,
       "cDnsErrorIxfrOutErrors": cDnsErrorIxfrOutErrors,
       "cDnsErrorAxfrInErrors": cDnsErrorAxfrInErrors,
       "cDnsErrorAxfrOutErrors": cDnsErrorAxfrOutErrors,
       "cDnsErrorSentTotalErrors": cDnsErrorSentTotalErrors,
       "cDnsErrorSentFormatErrors": cDnsErrorSentFormatErrors,
       "cDnsErrorSentOtherErrors": cDnsErrorSentOtherErrors,
       "cDnsErrorSentRefusalErrors": cDnsErrorSentRefusalErrors,
       "cDnsErrorRcvdFormatErrors": cDnsErrorRcvdFormatErrors,
       "cDnsErrorIntervalStats": cDnsErrorIntervalStats,
       "cDnsErrorIntUpdateErrors": cDnsErrorIntUpdateErrors,
       "cDnsErrorIntIxfrInErrors": cDnsErrorIntIxfrInErrors,
       "cDnsErrorIntIxfrOutErrors": cDnsErrorIntIxfrOutErrors,
       "cDnsErrorIntAxfrInErrors": cDnsErrorIntAxfrInErrors,
       "cDnsErrorIntAxfrOutErrors": cDnsErrorIntAxfrOutErrors,
       "cDnsErrorIntSentTotalErrors": cDnsErrorIntSentTotalErrors,
       "cDnsErrorIntSentFormatErrors": cDnsErrorIntSentFormatErrors,
       "cDnsErrorIntSentOtherErrors": cDnsErrorIntSentOtherErrors,
       "cDnsErrorIntSentRefusalErrors": cDnsErrorIntSentRefusalErrors,
       "cDnsErrorIntRcvdFormatErrors": cDnsErrorIntRcvdFormatErrors,
       "cDnsErrorIntSampleTime": cDnsErrorIntSampleTime,
       "cDnsErrorIntSampleInterval": cDnsErrorIntSampleInterval,
       "cDnsMaxCounterStats": cDnsMaxCounterStats,
       "cDnsMaxCntrConcurXfrsInCnts": cDnsMaxCntrConcurXfrsInCnts,
       "cDnsMaxCntrConcurXfrsOutCnts": cDnsMaxCntrConcurXfrsOutCnts,
       "cDnsMaxCntrHaSvrNoRespTime": cDnsMaxCntrHaSvrNoRespTime,
       "cDnsMaxCntrHaSvrMaxNoRespTime": cDnsMaxCntrHaSvrMaxNoRespTime,
       "cDnsMaxCntrHaBatchLimitCnts": cDnsMaxCntrHaBatchLimitCnts,
       "cDnsMaxCntrHaRRPendListCnts": cDnsMaxCntrHaRRPendListCnts,
       "cDnsMaxCntrHaRRActiveListCnts": cDnsMaxCntrHaRRActiveListCnts,
       "cDnsMaxCntrHaPersEditListCnts": cDnsMaxCntrHaPersEditListCnts,
       "cDnsMaxCntrHaUpdLatencyMax": cDnsMaxCntrHaUpdLatencyMax,
       "cDnsMaxCounterIntervalStats": cDnsMaxCounterIntervalStats,
       "cDnsMaxCntrIntConcurXfrsInCnts": cDnsMaxCntrIntConcurXfrsInCnts,
       "cDnsMaxCntrIntConcurXfrsOutCnts": cDnsMaxCntrIntConcurXfrsOutCnts,
       "cDnsMaxCntrIntHaSvrNoRespTime": cDnsMaxCntrIntHaSvrNoRespTime,
       "cDnsMaxCntrIntHaSvrMaxNoRespTime": cDnsMaxCntrIntHaSvrMaxNoRespTime,
       "cDnsMaxCntrIntHaBatchLimitCnts": cDnsMaxCntrIntHaBatchLimitCnts,
       "cDnsMaxCntrIntHaRRPendListCnts": cDnsMaxCntrIntHaRRPendListCnts,
       "cDnsMaxCntrIntHaRRActiveListCnts": cDnsMaxCntrIntHaRRActiveListCnts,
       "cDnsMaxCntrIntHaPersEditListCnts": cDnsMaxCntrIntHaPersEditListCnts,
       "cDnsMaxCntrIntHaUpdLatencyMax": cDnsMaxCntrIntHaUpdLatencyMax,
       "cDnsMaxCntrIntSampleTime": cDnsMaxCntrIntSampleTime,
       "cDnsMaxCntrIntSampleInterval": cDnsMaxCntrIntSampleInterval,
       "cDnsHaStats": cDnsHaStats,
       "cDnsHaCommInterruptedStates": cDnsHaCommInterruptedStates,
       "cDnsHaPartnerDownStates": cDnsHaPartnerDownStates,
       "cDnsHaSyncs": cDnsHaSyncs,
       "cDnsHaMsgConnectSentCnts": cDnsHaMsgConnectSentCnts,
       "cDnsHaMsgReconcileSentCnts": cDnsHaMsgReconcileSentCnts,
       "cDnsHaMsgHeartBeatSentCnts": cDnsHaMsgHeartBeatSentCnts,
       "cDnsHaMsgZoneSyncSentCnts": cDnsHaMsgZoneSyncSentCnts,
       "cDnsHaMsgRRSyncSentCnts": cDnsHaMsgRRSyncSentCnts,
       "cDnsHaMsgRRUpdateSentCnts": cDnsHaMsgRRUpdateSentCnts,
       "cDnsHaMsgResponseSentCnts": cDnsHaMsgResponseSentCnts,
       "cDnsHaMsgConnectRcvdCnts": cDnsHaMsgConnectRcvdCnts,
       "cDnsHaMsgReconcileRcvdCnts": cDnsHaMsgReconcileRcvdCnts,
       "cDnsHaMsgHeartbeatRcvdCnts": cDnsHaMsgHeartbeatRcvdCnts,
       "cDnsHaMsgZoneSyncRcvdCnts": cDnsHaMsgZoneSyncRcvdCnts,
       "cDnsHaMsgRRSyncRcvdCnts": cDnsHaMsgRRSyncRcvdCnts,
       "cDnsHaMsgRRUpdateRcvdCnts": cDnsHaMsgRRUpdateRcvdCnts,
       "cDnsHaMsgResponseRcvdCnts": cDnsHaMsgResponseRcvdCnts,
       "cDnsHaHeartbeatTimeoutCnts": cDnsHaHeartbeatTimeoutCnts,
       "cDnsHaUpdateRejectCnts": cDnsHaUpdateRejectCnts,
       "cDnsHaResponseMismatchCnts": cDnsHaResponseMismatchCnts,
       "cDnsHaResponseServFailCnts": cDnsHaResponseServFailCnts,
       "cDnsHaRespInconsistentCnts": cDnsHaRespInconsistentCnts,
       "cDnsHaRespUnknownCnts": cDnsHaRespUnknownCnts,
       "cDnsHaFullZoneResyncCnts": cDnsHaFullZoneResyncCnts,
       "cDnsHaUpdatePrivateReqCnts": cDnsHaUpdatePrivateReqCnts,
       "cDnsHaUpdatePrivateRespCnts": cDnsHaUpdatePrivateRespCnts,
       "cDnsHaSyncConflictCnts": cDnsHaSyncConflictCnts,
       "cDnsHaSyncDiscardNameCnts": cDnsHaSyncDiscardNameCnts,
       "cDnsHaSyncMergeNameCnts": cDnsHaSyncMergeNameCnts,
       "cDnsHaUpdateLatencyAverage": cDnsHaUpdateLatencyAverage,
       "cDnsHaIntervalStats": cDnsHaIntervalStats,
       "cDnsHaIntCommInterruptedStates": cDnsHaIntCommInterruptedStates,
       "cDnsHaIntPartnerDownStates": cDnsHaIntPartnerDownStates,
       "cDnsHaIntSyncs": cDnsHaIntSyncs,
       "cDnsHaIntMsgConnectSentCnts": cDnsHaIntMsgConnectSentCnts,
       "cDnsHaIntMsgReconcileSentCnts": cDnsHaIntMsgReconcileSentCnts,
       "cDnsHaIntMsgHeartBeatSentCnts": cDnsHaIntMsgHeartBeatSentCnts,
       "cDnsHaIntMsgZoneSyncSentCnts": cDnsHaIntMsgZoneSyncSentCnts,
       "cDnsHaIntMsgRRSyncSentCnts": cDnsHaIntMsgRRSyncSentCnts,
       "cDnsHaIntMsgRRUpdateSentCnts": cDnsHaIntMsgRRUpdateSentCnts,
       "cDnsHaIntMsgResponseSentCnts": cDnsHaIntMsgResponseSentCnts,
       "cDnsHaIntMsgConnectRcvdCnts": cDnsHaIntMsgConnectRcvdCnts,
       "cDnsHaIntMsgReconcileRcvdCnts": cDnsHaIntMsgReconcileRcvdCnts,
       "cDnsHaIntMsgHeartbeatRcvdCnts": cDnsHaIntMsgHeartbeatRcvdCnts,
       "cDnsHaIntMsgZoneSyncRcvdCnts": cDnsHaIntMsgZoneSyncRcvdCnts,
       "cDnsHaIntMsgRRSyncRcvdCnts": cDnsHaIntMsgRRSyncRcvdCnts,
       "cDnsHaIntMsgRRUpdateRcvdCnts": cDnsHaIntMsgRRUpdateRcvdCnts,
       "cDnsHaIntMsgResponseRcvdCnts": cDnsHaIntMsgResponseRcvdCnts,
       "cDnsHaIntHeartbeatTimeoutCnts": cDnsHaIntHeartbeatTimeoutCnts,
       "cDnsHaIntUpdateRejectCnts": cDnsHaIntUpdateRejectCnts,
       "cDnsHaIntResponseMismatchCnts": cDnsHaIntResponseMismatchCnts,
       "cDnsHaIntResponseServFailCnts": cDnsHaIntResponseServFailCnts,
       "cDnsHaIntRespInconsistentCnts": cDnsHaIntRespInconsistentCnts,
       "cDnsHaIntRespUnknownCnts": cDnsHaIntRespUnknownCnts,
       "cDnsHaIntFullZoneResyncCnts": cDnsHaIntFullZoneResyncCnts,
       "cDnsHaIntUpdatePrivateReqCnts": cDnsHaIntUpdatePrivateReqCnts,
       "cDnsHaIntUpdatePrivateRespCnts": cDnsHaIntUpdatePrivateRespCnts,
       "cDnsHaIntSyncConflictCnts": cDnsHaIntSyncConflictCnts,
       "cDnsHaIntSyncDiscardNameCnts": cDnsHaIntSyncDiscardNameCnts,
       "cDnsHaIntSyncMergeNameCnts": cDnsHaIntSyncMergeNameCnts,
       "cDnsHaIntUpdateLatencyAverage": cDnsHaIntUpdateLatencyAverage,
       "cDnsHaIntSampleTime": cDnsHaIntSampleTime,
       "cDnsHaIntSampleInterval": cDnsHaIntSampleInterval,
       "cDnsServMIBConform": cDnsServMIBConform,
       "cDnsServMIBCompliances": cDnsServMIBCompliances,
       "cDnsServMIBCompliance": cDnsServMIBCompliance,
       "cDnsServMIBGroups": cDnsServMIBGroups,
       "cDnsServConfigGroup": cDnsServConfigGroup,
       "cDnsQueryStatsGroup": cDnsQueryStatsGroup,
       "cDnsQueryStatsIntervalGroup": cDnsQueryStatsIntervalGroup,
       "cDnsPerfStatsGroup": cDnsPerfStatsGroup,
       "cDnsPerfStatsIntervalGroup": cDnsPerfStatsIntervalGroup,
       "cDnsSecurityStatsGroup": cDnsSecurityStatsGroup,
       "cDnsSecurityStatsIntervalGroup": cDnsSecurityStatsIntervalGroup,
       "cDnsErrorStatsGroup": cDnsErrorStatsGroup,
       "cDnsErrorStatsIntervalGroup": cDnsErrorStatsIntervalGroup,
       "cDnsMaxCounterStatsGroup": cDnsMaxCounterStatsGroup,
       "cDnsMaxCounterStatsIntervalGroup": cDnsMaxCounterStatsIntervalGroup,
       "cDnsHaStatsGroup": cDnsHaStatsGroup,
       "cDnsHaStatsIntervalGroup": cDnsHaStatsIntervalGroup}
)
