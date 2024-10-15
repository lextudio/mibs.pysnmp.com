# SNMP MIB module (CISCO-CONTENT-ENGINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CONTENT-ENGINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:43 2024
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoContentEngineMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178)
)
ciscoContentEngineMIB.setRevisions(
        ("2004-04-21 00:00",
         "2004-02-10 00:00",
         "2002-05-20 00:00",
         "2000-02-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoContentEngineMIBObjects_ObjectIdentity = ObjectIdentity
ciscoContentEngineMIBObjects = _CiscoContentEngineMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1)
)
_CceHttpGroup_ObjectIdentity = ObjectIdentity
cceHttpGroup = _CceHttpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1)
)
_CceHttpRequests_ObjectIdentity = ObjectIdentity
cceHttpRequests = _CceHttpRequests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1)
)
_CceHttpRequestsTotal_Type = Counter32
_CceHttpRequestsTotal_Object = MibScalar
cceHttpRequestsTotal = _CceHttpRequestsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 1),
    _CceHttpRequestsTotal_Type()
)
cceHttpRequestsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpRequestsTotal.setStatus("current")
_CceHttpRequestsNoCacheTotal_Type = Counter32
_CceHttpRequestsNoCacheTotal_Object = MibScalar
cceHttpRequestsNoCacheTotal = _CceHttpRequestsNoCacheTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 2),
    _CceHttpRequestsNoCacheTotal_Type()
)
cceHttpRequestsNoCacheTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpRequestsNoCacheTotal.setStatus("current")
_CceHttpRequestsClientErrorTotal_Type = Counter32
_CceHttpRequestsClientErrorTotal_Object = MibScalar
cceHttpRequestsClientErrorTotal = _CceHttpRequestsClientErrorTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 3),
    _CceHttpRequestsClientErrorTotal_Type()
)
cceHttpRequestsClientErrorTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpRequestsClientErrorTotal.setStatus("current")
_CceHttpRequestsServerErrorTotal_Type = Counter32
_CceHttpRequestsServerErrorTotal_Object = MibScalar
cceHttpRequestsServerErrorTotal = _CceHttpRequestsServerErrorTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 4),
    _CceHttpRequestsServerErrorTotal_Type()
)
cceHttpRequestsServerErrorTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpRequestsServerErrorTotal.setStatus("current")
_CceHttpRequestsBlocked_Type = Counter32
_CceHttpRequestsBlocked_Object = MibScalar
cceHttpRequestsBlocked = _CceHttpRequestsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 5),
    _CceHttpRequestsBlocked_Type()
)
cceHttpRequestsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpRequestsBlocked.setStatus("current")
_CceHttpRequestsHits_Type = Counter32
_CceHttpRequestsHits_Object = MibScalar
cceHttpRequestsHits = _CceHttpRequestsHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 6),
    _CceHttpRequestsHits_Type()
)
cceHttpRequestsHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpRequestsHits.setStatus("current")
_CceHttpRequestsMisses_Type = Counter32
_CceHttpRequestsMisses_Object = MibScalar
cceHttpRequestsMisses = _CceHttpRequestsMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 7),
    _CceHttpRequestsMisses_Type()
)
cceHttpRequestsMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpRequestsMisses.setStatus("current")
_CceHttpRequestsBytesServedHits_Type = Counter32
_CceHttpRequestsBytesServedHits_Object = MibScalar
cceHttpRequestsBytesServedHits = _CceHttpRequestsBytesServedHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 8),
    _CceHttpRequestsBytesServedHits_Type()
)
cceHttpRequestsBytesServedHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpRequestsBytesServedHits.setStatus("current")
_CceHttpRequestsBytesServedMisses_Type = Counter32
_CceHttpRequestsBytesServedMisses_Object = MibScalar
cceHttpRequestsBytesServedMisses = _CceHttpRequestsBytesServedMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 9),
    _CceHttpRequestsBytesServedMisses_Type()
)
cceHttpRequestsBytesServedMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpRequestsBytesServedMisses.setStatus("current")
_CceHttpRequestsImsInmTotalCache_Type = Counter32
_CceHttpRequestsImsInmTotalCache_Object = MibScalar
cceHttpRequestsImsInmTotalCache = _CceHttpRequestsImsInmTotalCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 10),
    _CceHttpRequestsImsInmTotalCache_Type()
)
cceHttpRequestsImsInmTotalCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpRequestsImsInmTotalCache.setStatus("current")
_CceHttpRequestsImsInmTotalReval_Type = Counter32
_CceHttpRequestsImsInmTotalReval_Object = MibScalar
cceHttpRequestsImsInmTotalReval = _CceHttpRequestsImsInmTotalReval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 11),
    _CceHttpRequestsImsInmTotalReval_Type()
)
cceHttpRequestsImsInmTotalReval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpRequestsImsInmTotalReval.setStatus("current")
_CceHttpRequestsBytesClientIn_Type = Counter32
_CceHttpRequestsBytesClientIn_Object = MibScalar
cceHttpRequestsBytesClientIn = _CceHttpRequestsBytesClientIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 12),
    _CceHttpRequestsBytesClientIn_Type()
)
cceHttpRequestsBytesClientIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpRequestsBytesClientIn.setStatus("current")
_CceHttpRequestsBytesClientOut_Type = Counter32
_CceHttpRequestsBytesClientOut_Object = MibScalar
cceHttpRequestsBytesClientOut = _CceHttpRequestsBytesClientOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 13),
    _CceHttpRequestsBytesClientOut_Type()
)
cceHttpRequestsBytesClientOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpRequestsBytesClientOut.setStatus("current")
_CceHttpRequestsBytesServerIn_Type = Counter32
_CceHttpRequestsBytesServerIn_Object = MibScalar
cceHttpRequestsBytesServerIn = _CceHttpRequestsBytesServerIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 14),
    _CceHttpRequestsBytesServerIn_Type()
)
cceHttpRequestsBytesServerIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpRequestsBytesServerIn.setStatus("current")
_CceHttpRequestsBytesServerOut_Type = Counter32
_CceHttpRequestsBytesServerOut_Object = MibScalar
cceHttpRequestsBytesServerOut = _CceHttpRequestsBytesServerOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 15),
    _CceHttpRequestsBytesServerOut_Type()
)
cceHttpRequestsBytesServerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpRequestsBytesServerOut.setStatus("current")
_CceHttpHCRequestsTotal_Type = Counter64
_CceHttpHCRequestsTotal_Object = MibScalar
cceHttpHCRequestsTotal = _CceHttpHCRequestsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 16),
    _CceHttpHCRequestsTotal_Type()
)
cceHttpHCRequestsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpHCRequestsTotal.setStatus("current")
_CceHttpHCRequestsNoCacheTotal_Type = Counter64
_CceHttpHCRequestsNoCacheTotal_Object = MibScalar
cceHttpHCRequestsNoCacheTotal = _CceHttpHCRequestsNoCacheTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 17),
    _CceHttpHCRequestsNoCacheTotal_Type()
)
cceHttpHCRequestsNoCacheTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpHCRequestsNoCacheTotal.setStatus("current")
_CceHttpHCRequestsClientErrorTotal_Type = Counter64
_CceHttpHCRequestsClientErrorTotal_Object = MibScalar
cceHttpHCRequestsClientErrorTotal = _CceHttpHCRequestsClientErrorTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 18),
    _CceHttpHCRequestsClientErrorTotal_Type()
)
cceHttpHCRequestsClientErrorTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpHCRequestsClientErrorTotal.setStatus("current")
_CceHttpHCRequestsServerErrorTotal_Type = Counter64
_CceHttpHCRequestsServerErrorTotal_Object = MibScalar
cceHttpHCRequestsServerErrorTotal = _CceHttpHCRequestsServerErrorTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 19),
    _CceHttpHCRequestsServerErrorTotal_Type()
)
cceHttpHCRequestsServerErrorTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpHCRequestsServerErrorTotal.setStatus("current")
_CceHttpHCRequestsBlocked_Type = Counter64
_CceHttpHCRequestsBlocked_Object = MibScalar
cceHttpHCRequestsBlocked = _CceHttpHCRequestsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 20),
    _CceHttpHCRequestsBlocked_Type()
)
cceHttpHCRequestsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpHCRequestsBlocked.setStatus("current")
_CceHttpHCRequestsHits_Type = Counter64
_CceHttpHCRequestsHits_Object = MibScalar
cceHttpHCRequestsHits = _CceHttpHCRequestsHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 21),
    _CceHttpHCRequestsHits_Type()
)
cceHttpHCRequestsHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpHCRequestsHits.setStatus("current")
_CceHttpHCRequestsMisses_Type = Counter64
_CceHttpHCRequestsMisses_Object = MibScalar
cceHttpHCRequestsMisses = _CceHttpHCRequestsMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 22),
    _CceHttpHCRequestsMisses_Type()
)
cceHttpHCRequestsMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpHCRequestsMisses.setStatus("current")
_CceHttpHCRequestsBytesServedHits_Type = Counter64
_CceHttpHCRequestsBytesServedHits_Object = MibScalar
cceHttpHCRequestsBytesServedHits = _CceHttpHCRequestsBytesServedHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 23),
    _CceHttpHCRequestsBytesServedHits_Type()
)
cceHttpHCRequestsBytesServedHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpHCRequestsBytesServedHits.setStatus("current")
_CceHttpHCRequestsBytesServedMisses_Type = Counter64
_CceHttpHCRequestsBytesServedMisses_Object = MibScalar
cceHttpHCRequestsBytesServedMisses = _CceHttpHCRequestsBytesServedMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 24),
    _CceHttpHCRequestsBytesServedMisses_Type()
)
cceHttpHCRequestsBytesServedMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpHCRequestsBytesServedMisses.setStatus("current")
_CceHttpHCRequestsImsInmTotalCache_Type = Counter64
_CceHttpHCRequestsImsInmTotalCache_Object = MibScalar
cceHttpHCRequestsImsInmTotalCache = _CceHttpHCRequestsImsInmTotalCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 25),
    _CceHttpHCRequestsImsInmTotalCache_Type()
)
cceHttpHCRequestsImsInmTotalCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpHCRequestsImsInmTotalCache.setStatus("current")
_CceHttpHCRequestsImsInmTotalReval_Type = Counter64
_CceHttpHCRequestsImsInmTotalReval_Object = MibScalar
cceHttpHCRequestsImsInmTotalReval = _CceHttpHCRequestsImsInmTotalReval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 26),
    _CceHttpHCRequestsImsInmTotalReval_Type()
)
cceHttpHCRequestsImsInmTotalReval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpHCRequestsImsInmTotalReval.setStatus("current")
_CceHttpHCRequestsBytesClientIn_Type = Counter64
_CceHttpHCRequestsBytesClientIn_Object = MibScalar
cceHttpHCRequestsBytesClientIn = _CceHttpHCRequestsBytesClientIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 27),
    _CceHttpHCRequestsBytesClientIn_Type()
)
cceHttpHCRequestsBytesClientIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpHCRequestsBytesClientIn.setStatus("current")
_CceHttpHCRequestsBytesClientOut_Type = Counter64
_CceHttpHCRequestsBytesClientOut_Object = MibScalar
cceHttpHCRequestsBytesClientOut = _CceHttpHCRequestsBytesClientOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 28),
    _CceHttpHCRequestsBytesClientOut_Type()
)
cceHttpHCRequestsBytesClientOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpHCRequestsBytesClientOut.setStatus("current")
_CceHttpHCRequestsBytesServerIn_Type = Counter64
_CceHttpHCRequestsBytesServerIn_Object = MibScalar
cceHttpHCRequestsBytesServerIn = _CceHttpHCRequestsBytesServerIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 29),
    _CceHttpHCRequestsBytesServerIn_Type()
)
cceHttpHCRequestsBytesServerIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpHCRequestsBytesServerIn.setStatus("current")
_CceHttpHCRequestsBytesServerOut_Type = Counter64
_CceHttpHCRequestsBytesServerOut_Object = MibScalar
cceHttpHCRequestsBytesServerOut = _CceHttpHCRequestsBytesServerOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 1, 30),
    _CceHttpHCRequestsBytesServerOut_Type()
)
cceHttpHCRequestsBytesServerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpHCRequestsBytesServerOut.setStatus("current")
_CceHttpPerf_ObjectIdentity = ObjectIdentity
cceHttpPerf = _CceHttpPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 2)
)


class _CceHttpPerfSamplingTime_Type(Unsigned32):
    """Custom type cceHttpPerfSamplingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CceHttpPerfSamplingTime_Type.__name__ = "Unsigned32"
_CceHttpPerfSamplingTime_Object = MibScalar
cceHttpPerfSamplingTime = _CceHttpPerfSamplingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 2, 1),
    _CceHttpPerfSamplingTime_Type()
)
cceHttpPerfSamplingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpPerfSamplingTime.setStatus("current")
if mibBuilder.loadTexts:
    cceHttpPerfSamplingTime.setUnits("seconds")


class _CceHttpPerfReqPerSec_Type(Unsigned32):
    """Custom type cceHttpPerfReqPerSec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CceHttpPerfReqPerSec_Type.__name__ = "Unsigned32"
_CceHttpPerfReqPerSec_Object = MibScalar
cceHttpPerfReqPerSec = _CceHttpPerfReqPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 2, 2),
    _CceHttpPerfReqPerSec_Type()
)
cceHttpPerfReqPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpPerfReqPerSec.setStatus("current")


class _CceHttpPerfBytesPerSec_Type(Unsigned32):
    """Custom type cceHttpPerfBytesPerSec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CceHttpPerfBytesPerSec_Type.__name__ = "Unsigned32"
_CceHttpPerfBytesPerSec_Object = MibScalar
cceHttpPerfBytesPerSec = _CceHttpPerfBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 2, 3),
    _CceHttpPerfBytesPerSec_Type()
)
cceHttpPerfBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpPerfBytesPerSec.setStatus("current")
if mibBuilder.loadTexts:
    cceHttpPerfBytesPerSec.setUnits("bytes-per-second")


class _CceHttpPerfServiceTime_Type(Unsigned32):
    """Custom type cceHttpPerfServiceTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CceHttpPerfServiceTime_Type.__name__ = "Unsigned32"
_CceHttpPerfServiceTime_Object = MibScalar
cceHttpPerfServiceTime = _CceHttpPerfServiceTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 2, 4),
    _CceHttpPerfServiceTime_Type()
)
cceHttpPerfServiceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpPerfServiceTime.setStatus("current")
if mibBuilder.loadTexts:
    cceHttpPerfServiceTime.setUnits("milliseconds-per-req")


class _CceHttpPerfHitServiceTime_Type(Unsigned32):
    """Custom type cceHttpPerfHitServiceTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CceHttpPerfHitServiceTime_Type.__name__ = "Unsigned32"
_CceHttpPerfHitServiceTime_Object = MibScalar
cceHttpPerfHitServiceTime = _CceHttpPerfHitServiceTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 2, 5),
    _CceHttpPerfHitServiceTime_Type()
)
cceHttpPerfHitServiceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpPerfHitServiceTime.setStatus("current")
if mibBuilder.loadTexts:
    cceHttpPerfHitServiceTime.setUnits("milliseconds-per-req")


class _CceHttpPerfMissServiceTime_Type(Unsigned32):
    """Custom type cceHttpPerfMissServiceTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CceHttpPerfMissServiceTime_Type.__name__ = "Unsigned32"
_CceHttpPerfMissServiceTime_Object = MibScalar
cceHttpPerfMissServiceTime = _CceHttpPerfMissServiceTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 2, 6),
    _CceHttpPerfMissServiceTime_Type()
)
cceHttpPerfMissServiceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpPerfMissServiceTime.setStatus("current")
if mibBuilder.loadTexts:
    cceHttpPerfMissServiceTime.setUnits("milliseconds-per-req")


class _CceHttpPerfObjectSize_Type(Unsigned32):
    """Custom type cceHttpPerfObjectSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CceHttpPerfObjectSize_Type.__name__ = "Unsigned32"
_CceHttpPerfObjectSize_Object = MibScalar
cceHttpPerfObjectSize = _CceHttpPerfObjectSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 2, 7),
    _CceHttpPerfObjectSize_Type()
)
cceHttpPerfObjectSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpPerfObjectSize.setStatus("current")
if mibBuilder.loadTexts:
    cceHttpPerfObjectSize.setUnits("bytes")


class _CceHttpPerfCpuLoad_Type(Unsigned32):
    """Custom type cceHttpPerfCpuLoad based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CceHttpPerfCpuLoad_Type.__name__ = "Unsigned32"
_CceHttpPerfCpuLoad_Object = MibScalar
cceHttpPerfCpuLoad = _CceHttpPerfCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 1, 2, 8),
    _CceHttpPerfCpuLoad_Type()
)
cceHttpPerfCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceHttpPerfCpuLoad.setStatus("current")
if mibBuilder.loadTexts:
    cceHttpPerfCpuLoad.setUnits("percentage")
_CceWmtGroup_ObjectIdentity = ObjectIdentity
cceWmtGroup = _CceWmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2)
)
_CceWmtRequests_ObjectIdentity = ObjectIdentity
cceWmtRequests = _CceWmtRequests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1)
)
_CceWmtTotalRequests_Type = Counter32
_CceWmtTotalRequests_Object = MibScalar
cceWmtTotalRequests = _CceWmtTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 1),
    _CceWmtTotalRequests_Type()
)
cceWmtTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtTotalRequests.setStatus("current")
_CceWmtTotalClientErrors_Type = Counter32
_CceWmtTotalClientErrors_Object = MibScalar
cceWmtTotalClientErrors = _CceWmtTotalClientErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 2),
    _CceWmtTotalClientErrors_Type()
)
cceWmtTotalClientErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtTotalClientErrors.setStatus("current")
_CceWmtTotalServerErrors_Type = Counter32
_CceWmtTotalServerErrors_Object = MibScalar
cceWmtTotalServerErrors = _CceWmtTotalServerErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 3),
    _CceWmtTotalServerErrors_Type()
)
cceWmtTotalServerErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtTotalServerErrors.setStatus("current")
_CceWmtBlockedRequests_Type = Counter32
_CceWmtBlockedRequests_Object = MibScalar
cceWmtBlockedRequests = _CceWmtBlockedRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 4),
    _CceWmtBlockedRequests_Type()
)
cceWmtBlockedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtBlockedRequests.setStatus("current")
_CceWmtRequestHits_Type = Counter32
_CceWmtRequestHits_Object = MibScalar
cceWmtRequestHits = _CceWmtRequestHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 5),
    _CceWmtRequestHits_Type()
)
cceWmtRequestHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtRequestHits.setStatus("current")
_CceWmtRequestMisses_Type = Counter32
_CceWmtRequestMisses_Object = MibScalar
cceWmtRequestMisses = _CceWmtRequestMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 6),
    _CceWmtRequestMisses_Type()
)
cceWmtRequestMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtRequestMisses.setStatus("current")
_CceWmtRequestHitsBytesServed_Type = Counter32
_CceWmtRequestHitsBytesServed_Object = MibScalar
cceWmtRequestHitsBytesServed = _CceWmtRequestHitsBytesServed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 7),
    _CceWmtRequestHitsBytesServed_Type()
)
cceWmtRequestHitsBytesServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtRequestHitsBytesServed.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtRequestHitsBytesServed.setUnits("Bytes")
_CceWmtRequestMissesBytesServed_Type = Counter32
_CceWmtRequestMissesBytesServed_Object = MibScalar
cceWmtRequestMissesBytesServed = _CceWmtRequestMissesBytesServed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 8),
    _CceWmtRequestMissesBytesServed_Type()
)
cceWmtRequestMissesBytesServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtRequestMissesBytesServed.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtRequestMissesBytesServed.setUnits("Bytes")
_CceWmtTotalLiveRequests_Type = Counter32
_CceWmtTotalLiveRequests_Object = MibScalar
cceWmtTotalLiveRequests = _CceWmtTotalLiveRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 9),
    _CceWmtTotalLiveRequests_Type()
)
cceWmtTotalLiveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtTotalLiveRequests.setStatus("current")
_CceWmtLiveRequestBytes_Type = Counter32
_CceWmtLiveRequestBytes_Object = MibScalar
cceWmtLiveRequestBytes = _CceWmtLiveRequestBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 10),
    _CceWmtLiveRequestBytes_Type()
)
cceWmtLiveRequestBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtLiveRequestBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtLiveRequestBytes.setUnits("Bytes")
_CceWmtTotalMmsuRequests_Type = Counter32
_CceWmtTotalMmsuRequests_Object = MibScalar
cceWmtTotalMmsuRequests = _CceWmtTotalMmsuRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 11),
    _CceWmtTotalMmsuRequests_Type()
)
cceWmtTotalMmsuRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtTotalMmsuRequests.setStatus("current")
_CceWmtTotalMmsuBytes_Type = Counter32
_CceWmtTotalMmsuBytes_Object = MibScalar
cceWmtTotalMmsuBytes = _CceWmtTotalMmsuBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 12),
    _CceWmtTotalMmsuBytes_Type()
)
cceWmtTotalMmsuBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtTotalMmsuBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtTotalMmsuBytes.setUnits("Bytes")
_CceWmtTotalMmstRequests_Type = Counter32
_CceWmtTotalMmstRequests_Object = MibScalar
cceWmtTotalMmstRequests = _CceWmtTotalMmstRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 13),
    _CceWmtTotalMmstRequests_Type()
)
cceWmtTotalMmstRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtTotalMmstRequests.setStatus("current")
_CceWmtTotalMmstBytes_Type = Counter32
_CceWmtTotalMmstBytes_Object = MibScalar
cceWmtTotalMmstBytes = _CceWmtTotalMmstBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 14),
    _CceWmtTotalMmstBytes_Type()
)
cceWmtTotalMmstBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtTotalMmstBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtTotalMmstBytes.setUnits("Bytes")
_CceWmtTotalHttpRequests_Type = Counter32
_CceWmtTotalHttpRequests_Object = MibScalar
cceWmtTotalHttpRequests = _CceWmtTotalHttpRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 15),
    _CceWmtTotalHttpRequests_Type()
)
cceWmtTotalHttpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtTotalHttpRequests.setStatus("current")
_CceWmtTotalHttpBytes_Type = Counter32
_CceWmtTotalHttpBytes_Object = MibScalar
cceWmtTotalHttpBytes = _CceWmtTotalHttpBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 16),
    _CceWmtTotalHttpBytes_Type()
)
cceWmtTotalHttpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtTotalHttpBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtTotalHttpBytes.setUnits("Bytes")
_CceWmtTotalMulticastBytes_Type = Counter32
_CceWmtTotalMulticastBytes_Object = MibScalar
cceWmtTotalMulticastBytes = _CceWmtTotalMulticastBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 17),
    _CceWmtTotalMulticastBytes_Type()
)
cceWmtTotalMulticastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtTotalMulticastBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtTotalMulticastBytes.setUnits("Bytes")
_CceWmtTotalRtspuRequests_Type = Counter32
_CceWmtTotalRtspuRequests_Object = MibScalar
cceWmtTotalRtspuRequests = _CceWmtTotalRtspuRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 18),
    _CceWmtTotalRtspuRequests_Type()
)
cceWmtTotalRtspuRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtTotalRtspuRequests.setStatus("current")
_CceWmtTotalRtspuBytes_Type = Counter32
_CceWmtTotalRtspuBytes_Object = MibScalar
cceWmtTotalRtspuBytes = _CceWmtTotalRtspuBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 19),
    _CceWmtTotalRtspuBytes_Type()
)
cceWmtTotalRtspuBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtTotalRtspuBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtTotalRtspuBytes.setUnits("Bytes")
_CceWmtTotalRtsptRequests_Type = Counter32
_CceWmtTotalRtsptRequests_Object = MibScalar
cceWmtTotalRtsptRequests = _CceWmtTotalRtsptRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 20),
    _CceWmtTotalRtsptRequests_Type()
)
cceWmtTotalRtsptRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtTotalRtsptRequests.setStatus("current")
_CceWmtTotalRtsptBytes_Type = Counter32
_CceWmtTotalRtsptBytes_Object = MibScalar
cceWmtTotalRtsptBytes = _CceWmtTotalRtsptBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 1, 21),
    _CceWmtTotalRtsptBytes_Type()
)
cceWmtTotalRtsptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtTotalRtsptBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtTotalRtsptBytes.setUnits("Bytes")
_CceWmtHCRequests_ObjectIdentity = ObjectIdentity
cceWmtHCRequests = _CceWmtHCRequests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 2)
)
_CceWmtHCRequestHitsBytesServed_Type = Counter64
_CceWmtHCRequestHitsBytesServed_Object = MibScalar
cceWmtHCRequestHitsBytesServed = _CceWmtHCRequestHitsBytesServed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 2, 1),
    _CceWmtHCRequestHitsBytesServed_Type()
)
cceWmtHCRequestHitsBytesServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtHCRequestHitsBytesServed.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtHCRequestHitsBytesServed.setUnits("Bytes")
_CceWmtHCRequestMissesBytesServed_Type = Counter64
_CceWmtHCRequestMissesBytesServed_Object = MibScalar
cceWmtHCRequestMissesBytesServed = _CceWmtHCRequestMissesBytesServed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 2, 2),
    _CceWmtHCRequestMissesBytesServed_Type()
)
cceWmtHCRequestMissesBytesServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtHCRequestMissesBytesServed.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtHCRequestMissesBytesServed.setUnits("Bytes")
_CceWmtHCLiveRequestBytes_Type = Counter64
_CceWmtHCLiveRequestBytes_Object = MibScalar
cceWmtHCLiveRequestBytes = _CceWmtHCLiveRequestBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 2, 3),
    _CceWmtHCLiveRequestBytes_Type()
)
cceWmtHCLiveRequestBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtHCLiveRequestBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtHCLiveRequestBytes.setUnits("Bytes")
_CceWmtHCTotalMmsuBytes_Type = Counter64
_CceWmtHCTotalMmsuBytes_Object = MibScalar
cceWmtHCTotalMmsuBytes = _CceWmtHCTotalMmsuBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 2, 4),
    _CceWmtHCTotalMmsuBytes_Type()
)
cceWmtHCTotalMmsuBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtHCTotalMmsuBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtHCTotalMmsuBytes.setUnits("Bytes")
_CceWmtHCTotalMmstBytes_Type = Counter64
_CceWmtHCTotalMmstBytes_Object = MibScalar
cceWmtHCTotalMmstBytes = _CceWmtHCTotalMmstBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 2, 5),
    _CceWmtHCTotalMmstBytes_Type()
)
cceWmtHCTotalMmstBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtHCTotalMmstBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtHCTotalMmstBytes.setUnits("Bytes")
_CceWmtHCTotalHttpBytes_Type = Counter64
_CceWmtHCTotalHttpBytes_Object = MibScalar
cceWmtHCTotalHttpBytes = _CceWmtHCTotalHttpBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 2, 6),
    _CceWmtHCTotalHttpBytes_Type()
)
cceWmtHCTotalHttpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtHCTotalHttpBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtHCTotalHttpBytes.setUnits("Bytes")
_CceWmtHCTotalMulticastBytes_Type = Counter64
_CceWmtHCTotalMulticastBytes_Object = MibScalar
cceWmtHCTotalMulticastBytes = _CceWmtHCTotalMulticastBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 2, 7),
    _CceWmtHCTotalMulticastBytes_Type()
)
cceWmtHCTotalMulticastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtHCTotalMulticastBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtHCTotalMulticastBytes.setUnits("Bytes")
_CceWmtHCTotalRtspuBytes_Type = Counter64
_CceWmtHCTotalRtspuBytes_Object = MibScalar
cceWmtHCTotalRtspuBytes = _CceWmtHCTotalRtspuBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 2, 8),
    _CceWmtHCTotalRtspuBytes_Type()
)
cceWmtHCTotalRtspuBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtHCTotalRtspuBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtHCTotalRtspuBytes.setUnits("Bytes")
_CceWmtHCTotalRtsptBytes_Type = Counter64
_CceWmtHCTotalRtsptBytes_Object = MibScalar
cceWmtHCTotalRtsptBytes = _CceWmtHCTotalRtsptBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 2, 9),
    _CceWmtHCTotalRtsptBytes_Type()
)
cceWmtHCTotalRtsptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtHCTotalRtsptBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtHCTotalRtsptBytes.setUnits("Bytes")
_CceWmtPerf_ObjectIdentity = ObjectIdentity
cceWmtPerf = _CceWmtPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 3)
)
_CceWmtPerfConcurrentRequests_Type = Gauge32
_CceWmtPerfConcurrentRequests_Object = MibScalar
cceWmtPerfConcurrentRequests = _CceWmtPerfConcurrentRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 3, 1),
    _CceWmtPerfConcurrentRequests_Type()
)
cceWmtPerfConcurrentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtPerfConcurrentRequests.setStatus("current")
_CceWmtPerfKbitsPerSec_Type = Gauge32
_CceWmtPerfKbitsPerSec_Object = MibScalar
cceWmtPerfKbitsPerSec = _CceWmtPerfKbitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 3, 2),
    _CceWmtPerfKbitsPerSec_Type()
)
cceWmtPerfKbitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtPerfKbitsPerSec.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtPerfKbitsPerSec.setUnits("Kbits-per-sec")
_CceWmtPerfMulticastSessions_Type = Gauge32
_CceWmtPerfMulticastSessions_Object = MibScalar
cceWmtPerfMulticastSessions = _CceWmtPerfMulticastSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 3, 3),
    _CceWmtPerfMulticastSessions_Type()
)
cceWmtPerfMulticastSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtPerfMulticastSessions.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtPerfMulticastSessions.setUnits("sessions")
_CceWmtPerfMulticastKbitsPerSec_Type = Gauge32
_CceWmtPerfMulticastKbitsPerSec_Object = MibScalar
cceWmtPerfMulticastKbitsPerSec = _CceWmtPerfMulticastKbitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 2, 3, 4),
    _CceWmtPerfMulticastKbitsPerSec_Type()
)
cceWmtPerfMulticastKbitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceWmtPerfMulticastKbitsPerSec.setStatus("current")
if mibBuilder.loadTexts:
    cceWmtPerfMulticastKbitsPerSec.setUnits("Kbits-per-sec")
_CceCseGroup_ObjectIdentity = ObjectIdentity
cceCseGroup = _CceCseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 3)
)
_CceCseRequests_ObjectIdentity = ObjectIdentity
cceCseRequests = _CceCseRequests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 3, 1)
)
_CceCseTotalRequests_Type = Counter32
_CceCseTotalRequests_Object = MibScalar
cceCseTotalRequests = _CceCseTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 3, 1, 1),
    _CceCseTotalRequests_Type()
)
cceCseTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceCseTotalRequests.setStatus("current")
_CceCseRequestPacketsServed_Type = Counter32
_CceCseRequestPacketsServed_Object = MibScalar
cceCseRequestPacketsServed = _CceCseRequestPacketsServed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 3, 1, 2),
    _CceCseRequestPacketsServed_Type()
)
cceCseRequestPacketsServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceCseRequestPacketsServed.setStatus("current")
if mibBuilder.loadTexts:
    cceCseRequestPacketsServed.setUnits("packets")
_CceCseRequestBytesServed_Type = Counter32
_CceCseRequestBytesServed_Object = MibScalar
cceCseRequestBytesServed = _CceCseRequestBytesServed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 3, 1, 3),
    _CceCseRequestBytesServed_Type()
)
cceCseRequestBytesServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceCseRequestBytesServed.setStatus("current")
if mibBuilder.loadTexts:
    cceCseRequestBytesServed.setUnits("Bytes")
_CceCseHCRequests_ObjectIdentity = ObjectIdentity
cceCseHCRequests = _CceCseHCRequests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 3, 2)
)
_CceCseHCRequestPacketsServed_Type = Counter64
_CceCseHCRequestPacketsServed_Object = MibScalar
cceCseHCRequestPacketsServed = _CceCseHCRequestPacketsServed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 3, 2, 1),
    _CceCseHCRequestPacketsServed_Type()
)
cceCseHCRequestPacketsServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceCseHCRequestPacketsServed.setStatus("current")
if mibBuilder.loadTexts:
    cceCseHCRequestPacketsServed.setUnits("packets")
_CceCseHCRequestBytesServed_Type = Counter64
_CceCseHCRequestBytesServed_Object = MibScalar
cceCseHCRequestBytesServed = _CceCseHCRequestBytesServed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 3, 2, 2),
    _CceCseHCRequestBytesServed_Type()
)
cceCseHCRequestBytesServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceCseHCRequestBytesServed.setStatus("current")
if mibBuilder.loadTexts:
    cceCseHCRequestBytesServed.setUnits("Bytes")
_CceCsePerf_ObjectIdentity = ObjectIdentity
cceCsePerf = _CceCsePerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 3, 3)
)
_CceCsePerfConcurrentReqs_Type = Gauge32
_CceCsePerfConcurrentReqs_Object = MibScalar
cceCsePerfConcurrentReqs = _CceCsePerfConcurrentReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 3, 3, 1),
    _CceCsePerfConcurrentReqs_Type()
)
cceCsePerfConcurrentReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceCsePerfConcurrentReqs.setStatus("current")
_CceCsePerfCurrentBandwidth_Type = Gauge32
_CceCsePerfCurrentBandwidth_Object = MibScalar
cceCsePerfCurrentBandwidth = _CceCsePerfCurrentBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 3, 3, 2),
    _CceCsePerfCurrentBandwidth_Type()
)
cceCsePerfCurrentBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceCsePerfCurrentBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cceCsePerfCurrentBandwidth.setUnits("Kbits")
_CceRpGroup_ObjectIdentity = ObjectIdentity
cceRpGroup = _CceRpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 4)
)
_CceRpRequests_ObjectIdentity = ObjectIdentity
cceRpRequests = _CceRpRequests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 4, 1)
)
_CceRpTotalHits_Type = Counter32
_CceRpTotalHits_Object = MibScalar
cceRpTotalHits = _CceRpTotalHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 4, 1, 1),
    _CceRpTotalHits_Type()
)
cceRpTotalHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRpTotalHits.setStatus("current")
_CceRpTotalMisses_Type = Counter32
_CceRpTotalMisses_Object = MibScalar
cceRpTotalMisses = _CceRpTotalMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 4, 1, 2),
    _CceRpTotalMisses_Type()
)
cceRpTotalMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRpTotalMisses.setStatus("current")
_CceRpTotalVodPassThroughs_Type = Counter32
_CceRpTotalVodPassThroughs_Object = MibScalar
cceRpTotalVodPassThroughs = _CceRpTotalVodPassThroughs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 4, 1, 3),
    _CceRpTotalVodPassThroughs_Type()
)
cceRpTotalVodPassThroughs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRpTotalVodPassThroughs.setStatus("current")
_CceRpTotalLiveSplitReqs_Type = Counter32
_CceRpTotalLiveSplitReqs_Object = MibScalar
cceRpTotalLiveSplitReqs = _CceRpTotalLiveSplitReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 4, 1, 4),
    _CceRpTotalLiveSplitReqs_Type()
)
cceRpTotalLiveSplitReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRpTotalLiveSplitReqs.setStatus("current")
_CceRpTotalLivePassThruSplitReqs_Type = Counter32
_CceRpTotalLivePassThruSplitReqs_Object = MibScalar
cceRpTotalLivePassThruSplitReqs = _CceRpTotalLivePassThruSplitReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 4, 1, 5),
    _CceRpTotalLivePassThruSplitReqs_Type()
)
cceRpTotalLivePassThruSplitReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRpTotalLivePassThruSplitReqs.setStatus("current")
_CceRpTotalIncomingBytes_Type = Counter32
_CceRpTotalIncomingBytes_Object = MibScalar
cceRpTotalIncomingBytes = _CceRpTotalIncomingBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 4, 1, 6),
    _CceRpTotalIncomingBytes_Type()
)
cceRpTotalIncomingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRpTotalIncomingBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceRpTotalIncomingBytes.setUnits("Bytes")
_CceRpTotalOutgoingBytes_Type = Counter32
_CceRpTotalOutgoingBytes_Object = MibScalar
cceRpTotalOutgoingBytes = _CceRpTotalOutgoingBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 4, 1, 7),
    _CceRpTotalOutgoingBytes_Type()
)
cceRpTotalOutgoingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRpTotalOutgoingBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceRpTotalOutgoingBytes.setUnits("Bytes")
_CceRpHCRequests_ObjectIdentity = ObjectIdentity
cceRpHCRequests = _CceRpHCRequests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 4, 2)
)
_CceRpHCTotalHits_Type = Counter64
_CceRpHCTotalHits_Object = MibScalar
cceRpHCTotalHits = _CceRpHCTotalHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 4, 2, 1),
    _CceRpHCTotalHits_Type()
)
cceRpHCTotalHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRpHCTotalHits.setStatus("current")
_CceRpHCTotalMisses_Type = Counter64
_CceRpHCTotalMisses_Object = MibScalar
cceRpHCTotalMisses = _CceRpHCTotalMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 4, 2, 2),
    _CceRpHCTotalMisses_Type()
)
cceRpHCTotalMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRpHCTotalMisses.setStatus("current")
_CceRpHCTotalVodPassThroughs_Type = Counter64
_CceRpHCTotalVodPassThroughs_Object = MibScalar
cceRpHCTotalVodPassThroughs = _CceRpHCTotalVodPassThroughs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 4, 2, 3),
    _CceRpHCTotalVodPassThroughs_Type()
)
cceRpHCTotalVodPassThroughs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRpHCTotalVodPassThroughs.setStatus("current")
_CceRpHCTotalLiveSplitReqs_Type = Counter64
_CceRpHCTotalLiveSplitReqs_Object = MibScalar
cceRpHCTotalLiveSplitReqs = _CceRpHCTotalLiveSplitReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 4, 2, 4),
    _CceRpHCTotalLiveSplitReqs_Type()
)
cceRpHCTotalLiveSplitReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRpHCTotalLiveSplitReqs.setStatus("current")
_CceRpHCTotalLivePassThruSplitReqs_Type = Counter64
_CceRpHCTotalLivePassThruSplitReqs_Object = MibScalar
cceRpHCTotalLivePassThruSplitReqs = _CceRpHCTotalLivePassThruSplitReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 4, 2, 5),
    _CceRpHCTotalLivePassThruSplitReqs_Type()
)
cceRpHCTotalLivePassThruSplitReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRpHCTotalLivePassThruSplitReqs.setStatus("current")
_CceRpHCTotalIncomingBytes_Type = Counter64
_CceRpHCTotalIncomingBytes_Object = MibScalar
cceRpHCTotalIncomingBytes = _CceRpHCTotalIncomingBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 4, 2, 6),
    _CceRpHCTotalIncomingBytes_Type()
)
cceRpHCTotalIncomingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRpHCTotalIncomingBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceRpHCTotalIncomingBytes.setUnits("Bytes")
_CceRpHCTotalOutgoingBytes_Type = Counter64
_CceRpHCTotalOutgoingBytes_Object = MibScalar
cceRpHCTotalOutgoingBytes = _CceRpHCTotalOutgoingBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 4, 2, 7),
    _CceRpHCTotalOutgoingBytes_Type()
)
cceRpHCTotalOutgoingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceRpHCTotalOutgoingBytes.setStatus("current")
if mibBuilder.loadTexts:
    cceRpHCTotalOutgoingBytes.setUnits("Bytes")
_CceNotificationInfo_ObjectIdentity = ObjectIdentity
cceNotificationInfo = _CceNotificationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 5)
)


class _CceFailedDiskName_Type(OctetString):
    """Custom type cceFailedDiskName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CceFailedDiskName_Type.__name__ = "OctetString"
_CceFailedDiskName_Object = MibScalar
cceFailedDiskName = _CceFailedDiskName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 5, 1),
    _CceFailedDiskName_Type()
)
cceFailedDiskName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cceFailedDiskName.setStatus("current")
_CceAlarmGroup_ObjectIdentity = ObjectIdentity
cceAlarmGroup = _CceAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 6)
)
_CceAlarmHistory_ObjectIdentity = ObjectIdentity
cceAlarmHistory = _CceAlarmHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 6, 1)
)


class _CceAlarmHistTableSize_Type(Integer32):
    """Custom type cceAlarmHistTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CceAlarmHistTableSize_Type.__name__ = "Integer32"
_CceAlarmHistTableSize_Object = MibScalar
cceAlarmHistTableSize = _CceAlarmHistTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 6, 1, 1),
    _CceAlarmHistTableSize_Type()
)
cceAlarmHistTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cceAlarmHistTableSize.setStatus("current")
_CceAlarmHistTable_Object = MibTable
cceAlarmHistTable = _CceAlarmHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    cceAlarmHistTable.setStatus("current")
_CceAlarmHistEntry_Object = MibTableRow
cceAlarmHistEntry = _CceAlarmHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 6, 1, 2, 1)
)
cceAlarmHistEntry.setIndexNames(
    (0, "CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistIndex"),
)
if mibBuilder.loadTexts:
    cceAlarmHistEntry.setStatus("current")
_CceAlarmHistIndex_Type = Unsigned32
_CceAlarmHistIndex_Object = MibTableColumn
cceAlarmHistIndex = _CceAlarmHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 6, 1, 2, 1, 1),
    _CceAlarmHistIndex_Type()
)
cceAlarmHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cceAlarmHistIndex.setStatus("current")
_CceAlarmHistId_Type = Unsigned32
_CceAlarmHistId_Object = MibTableColumn
cceAlarmHistId = _CceAlarmHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 6, 1, 2, 1, 2),
    _CceAlarmHistId_Type()
)
cceAlarmHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceAlarmHistId.setStatus("current")
_CceAlarmHistModuleId_Type = Unsigned32
_CceAlarmHistModuleId_Object = MibTableColumn
cceAlarmHistModuleId = _CceAlarmHistModuleId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 6, 1, 2, 1, 3),
    _CceAlarmHistModuleId_Type()
)
cceAlarmHistModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceAlarmHistModuleId.setStatus("current")


class _CceAlarmHistType_Type(Integer32):
    """Custom type cceAlarmHistType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 2),
          ("raised", 1))
    )


_CceAlarmHistType_Type.__name__ = "Integer32"
_CceAlarmHistType_Object = MibTableColumn
cceAlarmHistType = _CceAlarmHistType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 6, 1, 2, 1, 4),
    _CceAlarmHistType_Type()
)
cceAlarmHistType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceAlarmHistType.setStatus("current")


class _CceAlarmHistCategory_Type(Integer32):
    """Custom type cceAlarmHistCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CceAlarmHistCategory_Type.__name__ = "Integer32"
_CceAlarmHistCategory_Object = MibTableColumn
cceAlarmHistCategory = _CceAlarmHistCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 6, 1, 2, 1, 5),
    _CceAlarmHistCategory_Type()
)
cceAlarmHistCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceAlarmHistCategory.setStatus("current")
_CceAlarmHistSeverity_Type = AlarmSeverity
_CceAlarmHistSeverity_Object = MibTableColumn
cceAlarmHistSeverity = _CceAlarmHistSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 6, 1, 2, 1, 6),
    _CceAlarmHistSeverity_Type()
)
cceAlarmHistSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceAlarmHistSeverity.setStatus("current")


class _CceAlarmHistInfo_Type(OctetString):
    """Custom type cceAlarmHistInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CceAlarmHistInfo_Type.__name__ = "OctetString"
_CceAlarmHistInfo_Object = MibTableColumn
cceAlarmHistInfo = _CceAlarmHistInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 6, 1, 2, 1, 7),
    _CceAlarmHistInfo_Type()
)
cceAlarmHistInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceAlarmHistInfo.setStatus("current")
_CceAlarmHistTimeStamp_Type = TimeStamp
_CceAlarmHistTimeStamp_Object = MibTableColumn
cceAlarmHistTimeStamp = _CceAlarmHistTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 6, 1, 2, 1, 8),
    _CceAlarmHistTimeStamp_Type()
)
cceAlarmHistTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceAlarmHistTimeStamp.setStatus("current")
_CceAlarmMonitoring_ObjectIdentity = ObjectIdentity
cceAlarmMonitoring = _CceAlarmMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 6, 2)
)
_CceAlarmCriticalCount_Type = Gauge32
_CceAlarmCriticalCount_Object = MibScalar
cceAlarmCriticalCount = _CceAlarmCriticalCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 6, 2, 1),
    _CceAlarmCriticalCount_Type()
)
cceAlarmCriticalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceAlarmCriticalCount.setStatus("current")
_CceAlarmMajorCount_Type = Gauge32
_CceAlarmMajorCount_Object = MibScalar
cceAlarmMajorCount = _CceAlarmMajorCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 6, 2, 2),
    _CceAlarmMajorCount_Type()
)
cceAlarmMajorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceAlarmMajorCount.setStatus("current")
_CceAlarmMinorCount_Type = Gauge32
_CceAlarmMinorCount_Object = MibScalar
cceAlarmMinorCount = _CceAlarmMinorCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 1, 6, 2, 3),
    _CceAlarmMinorCount_Type()
)
cceAlarmMinorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cceAlarmMinorCount.setStatus("current")
_CiscoContentEngineMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoContentEngineMIBNotificationPrefix = _CiscoContentEngineMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 2)
)
_CiscoContentEngineMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoContentEngineMIBNotifications = _CiscoContentEngineMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 2, 0)
)
_CiscoContentEngineMIBConformance_ObjectIdentity = ObjectIdentity
ciscoContentEngineMIBConformance = _CiscoContentEngineMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3)
)
_CiscoContentEngineMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoContentEngineMIBCompliances = _CiscoContentEngineMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 1)
)
_CiscoContentEngineMIBGroups_ObjectIdentity = ObjectIdentity
ciscoContentEngineMIBGroups = _CiscoContentEngineMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2)
)

# Managed Objects groups

cceHttpReqGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2, 1)
)
cceHttpReqGroup.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceHttpRequestsTotal"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpRequestsNoCacheTotal"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpRequestsClientErrorTotal"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpRequestsServerErrorTotal"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpRequestsBlocked"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpRequestsHits"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpRequestsMisses"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpRequestsBytesServedHits"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpRequestsBytesServedMisses"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpRequestsImsInmTotalCache"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpRequestsImsInmTotalReval"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpRequestsBytesClientIn"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpRequestsBytesClientOut"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpRequestsBytesServerIn"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpRequestsBytesServerOut"))
)
if mibBuilder.loadTexts:
    cceHttpReqGroup.setStatus("current")

cceHttpHCReqGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2, 2)
)
cceHttpHCReqGroup.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceHttpHCRequestsTotal"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpHCRequestsNoCacheTotal"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpHCRequestsClientErrorTotal"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpHCRequestsServerErrorTotal"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpHCRequestsBlocked"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpHCRequestsHits"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpHCRequestsMisses"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpHCRequestsBytesServedHits"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpHCRequestsBytesServedMisses"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpHCRequestsImsInmTotalCache"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpHCRequestsImsInmTotalReval"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpHCRequestsBytesClientIn"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpHCRequestsBytesClientOut"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpHCRequestsBytesServerIn"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpHCRequestsBytesServerOut"))
)
if mibBuilder.loadTexts:
    cceHttpHCReqGroup.setStatus("current")

cceHttpPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2, 3)
)
cceHttpPerfGroup.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceHttpPerfSamplingTime"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpPerfReqPerSec"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpPerfBytesPerSec"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpPerfServiceTime"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpPerfHitServiceTime"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpPerfMissServiceTime"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpPerfObjectSize"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceHttpPerfCpuLoad"))
)
if mibBuilder.loadTexts:
    cceHttpPerfGroup.setStatus("current")

cceWmtReqGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2, 5)
)
cceWmtReqGroup.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalRequests"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalClientErrors"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalServerErrors"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtBlockedRequests"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtRequestHits"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtRequestMisses"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtRequestHitsBytesServed"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtRequestMissesBytesServed"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalLiveRequests"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtLiveRequestBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalMmsuRequests"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalMmsuBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalMmstRequests"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalMmstBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalHttpRequests"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalHttpBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalMulticastBytes"))
)
if mibBuilder.loadTexts:
    cceWmtReqGroup.setStatus("deprecated")

cceWmtHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2, 6)
)
cceWmtHCGroup.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceWmtHCRequestHitsBytesServed"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtHCRequestMissesBytesServed"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtHCLiveRequestBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtHCTotalMmsuBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtHCTotalMmstBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtHCTotalHttpBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtHCTotalMulticastBytes"))
)
if mibBuilder.loadTexts:
    cceWmtHCGroup.setStatus("deprecated")

cceWmtPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2, 7)
)
cceWmtPerfGroup.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceWmtPerfConcurrentRequests"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtPerfKbitsPerSec"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtPerfMulticastSessions"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtPerfMulticastKbitsPerSec"))
)
if mibBuilder.loadTexts:
    cceWmtPerfGroup.setStatus("current")

cceCseReqGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2, 8)
)
cceCseReqGroup.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceCseTotalRequests"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceCseRequestPacketsServed"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceCseRequestBytesServed"))
)
if mibBuilder.loadTexts:
    cceCseReqGroup.setStatus("current")

cceCseHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2, 9)
)
cceCseHCGroup.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceCseHCRequestPacketsServed"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceCseHCRequestBytesServed"))
)
if mibBuilder.loadTexts:
    cceCseHCGroup.setStatus("current")

cceCsePerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2, 10)
)
cceCsePerfGroup.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceCsePerfConcurrentReqs"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceCsePerfCurrentBandwidth"))
)
if mibBuilder.loadTexts:
    cceCsePerfGroup.setStatus("current")

cceRpReqGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2, 11)
)
cceRpReqGroup.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceRpTotalHits"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceRpTotalMisses"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceRpTotalVodPassThroughs"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceRpTotalLiveSplitReqs"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceRpTotalLivePassThruSplitReqs"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceRpTotalIncomingBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceRpTotalOutgoingBytes"))
)
if mibBuilder.loadTexts:
    cceRpReqGroup.setStatus("current")

cceRpHCReqGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2, 12)
)
cceRpHCReqGroup.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceRpHCTotalHits"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceRpHCTotalMisses"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceRpHCTotalVodPassThroughs"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceRpHCTotalLiveSplitReqs"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceRpHCTotalLivePassThruSplitReqs"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceRpHCTotalIncomingBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceRpHCTotalOutgoingBytes"))
)
if mibBuilder.loadTexts:
    cceRpHCReqGroup.setStatus("current")

cceAlarmInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2, 14)
)
cceAlarmInfoGroup.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceAlarmCriticalCount"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmMajorCount"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmMinorCount"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistTableSize"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistId"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistModuleId"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistSeverity"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistType"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistCategory"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistInfo"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistTimeStamp"))
)
if mibBuilder.loadTexts:
    cceAlarmInfoGroup.setStatus("current")

cceNotificationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2, 15)
)
cceNotificationInfoGroup.setObjects(
    ("CISCO-CONTENT-ENGINE-MIB", "cceFailedDiskName")
)
if mibBuilder.loadTexts:
    cceNotificationInfoGroup.setStatus("current")

cceWmtReqGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2, 16)
)
cceWmtReqGroupRev1.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalRequests"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalClientErrors"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalServerErrors"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtBlockedRequests"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtRequestHits"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtRequestMisses"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtRequestHitsBytesServed"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtRequestMissesBytesServed"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalLiveRequests"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtLiveRequestBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalMmsuRequests"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalMmsuBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalMmstRequests"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalMmstBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalHttpRequests"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalHttpBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalRtspuRequests"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalRtspuBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalRtsptRequests"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalRtsptBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtTotalMulticastBytes"))
)
if mibBuilder.loadTexts:
    cceWmtReqGroupRev1.setStatus("current")

cceWmtHCGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2, 17)
)
cceWmtHCGroupRev1.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceWmtHCRequestHitsBytesServed"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtHCRequestMissesBytesServed"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtHCLiveRequestBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtHCTotalMmsuBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtHCTotalMmstBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtHCTotalHttpBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtHCTotalRtspuBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtHCTotalRtsptBytes"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceWmtHCTotalMulticastBytes"))
)
if mibBuilder.loadTexts:
    cceWmtHCGroupRev1.setStatus("current")


# Notification objects

ciscoContentEngineReadDiskError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 2, 0, 1)
)
if mibBuilder.loadTexts:
    ciscoContentEngineReadDiskError.setStatus(
        "current"
    )

ciscoContentEngineWriteDiskError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 2, 0, 2)
)
if mibBuilder.loadTexts:
    ciscoContentEngineWriteDiskError.setStatus(
        "current"
    )

ciscoContentEngineWriteTransFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 2, 0, 3)
)
if mibBuilder.loadTexts:
    ciscoContentEngineWriteTransFailed.setStatus(
        "current"
    )

ciscoContentEngineDataDiskFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 2, 0, 4)
)
if mibBuilder.loadTexts:
    ciscoContentEngineDataDiskFailed.setStatus(
        "deprecated"
    )

ciscoContentEngineOverloadBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 2, 0, 5)
)
if mibBuilder.loadTexts:
    ciscoContentEngineOverloadBypass.setStatus(
        "current"
    )

ciscoContentEngineDiskFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 2, 0, 6)
)
ciscoContentEngineDiskFailed.setObjects(
    ("CISCO-CONTENT-ENGINE-MIB", "cceFailedDiskName")
)
if mibBuilder.loadTexts:
    ciscoContentEngineDiskFailed.setStatus(
        "current"
    )

cceAlarmCriticalRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 2, 0, 7)
)
cceAlarmCriticalRaised.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistId"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistModuleId"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistCategory"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistInfo"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistTimeStamp"))
)
if mibBuilder.loadTexts:
    cceAlarmCriticalRaised.setStatus(
        "current"
    )

cceAlarmCriticalCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 2, 0, 8)
)
cceAlarmCriticalCleared.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistId"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistModuleId"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistCategory"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistInfo"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistTimeStamp"))
)
if mibBuilder.loadTexts:
    cceAlarmCriticalCleared.setStatus(
        "current"
    )

cceAlarmMajorRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 2, 0, 9)
)
cceAlarmMajorRaised.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistId"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistModuleId"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistCategory"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistInfo"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistTimeStamp"))
)
if mibBuilder.loadTexts:
    cceAlarmMajorRaised.setStatus(
        "current"
    )

cceAlarmMajorCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 2, 0, 10)
)
cceAlarmMajorCleared.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistId"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistModuleId"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistCategory"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistInfo"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistTimeStamp"))
)
if mibBuilder.loadTexts:
    cceAlarmMajorCleared.setStatus(
        "current"
    )

cceAlarmMinorRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 2, 0, 11)
)
cceAlarmMinorRaised.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistId"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistModuleId"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistCategory"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistInfo"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistTimeStamp"))
)
if mibBuilder.loadTexts:
    cceAlarmMinorRaised.setStatus(
        "current"
    )

cceAlarmMinorCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 2, 0, 12)
)
cceAlarmMinorCleared.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistId"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistModuleId"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistCategory"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistInfo"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmHistTimeStamp"))
)
if mibBuilder.loadTexts:
    cceAlarmMinorCleared.setStatus(
        "current"
    )


# Notifications groups

cceNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2, 4)
)
cceNotificationGroup.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "ciscoContentEngineReadDiskError"),
        ("CISCO-CONTENT-ENGINE-MIB", "ciscoContentEngineWriteDiskError"),
        ("CISCO-CONTENT-ENGINE-MIB", "ciscoContentEngineWriteTransFailed"),
        ("CISCO-CONTENT-ENGINE-MIB", "ciscoContentEngineDataDiskFailed"),
        ("CISCO-CONTENT-ENGINE-MIB", "ciscoContentEngineOverloadBypass"))
)
if mibBuilder.loadTexts:
    cceNotificationGroup.setStatus(
        "deprecated"
    )

cceNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 2, 13)
)
cceNotificationGroupRev1.setObjects(
      *(("CISCO-CONTENT-ENGINE-MIB", "ciscoContentEngineReadDiskError"),
        ("CISCO-CONTENT-ENGINE-MIB", "ciscoContentEngineWriteDiskError"),
        ("CISCO-CONTENT-ENGINE-MIB", "ciscoContentEngineWriteTransFailed"),
        ("CISCO-CONTENT-ENGINE-MIB", "ciscoContentEngineOverloadBypass"),
        ("CISCO-CONTENT-ENGINE-MIB", "ciscoContentEngineDiskFailed"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmCriticalRaised"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmCriticalCleared"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmMajorRaised"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmMajorCleared"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmMinorRaised"),
        ("CISCO-CONTENT-ENGINE-MIB", "cceAlarmMinorCleared"))
)
if mibBuilder.loadTexts:
    cceNotificationGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoContentEngineMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoContentEngineMIBCompliance.setStatus(
        "deprecated"
    )

ciscoContentEngineMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoContentEngineMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoContentEngineMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoContentEngineMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoContentEngineMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 178, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoContentEngineMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CONTENT-ENGINE-MIB",
    **{"AlarmSeverity": AlarmSeverity,
       "ciscoContentEngineMIB": ciscoContentEngineMIB,
       "ciscoContentEngineMIBObjects": ciscoContentEngineMIBObjects,
       "cceHttpGroup": cceHttpGroup,
       "cceHttpRequests": cceHttpRequests,
       "cceHttpRequestsTotal": cceHttpRequestsTotal,
       "cceHttpRequestsNoCacheTotal": cceHttpRequestsNoCacheTotal,
       "cceHttpRequestsClientErrorTotal": cceHttpRequestsClientErrorTotal,
       "cceHttpRequestsServerErrorTotal": cceHttpRequestsServerErrorTotal,
       "cceHttpRequestsBlocked": cceHttpRequestsBlocked,
       "cceHttpRequestsHits": cceHttpRequestsHits,
       "cceHttpRequestsMisses": cceHttpRequestsMisses,
       "cceHttpRequestsBytesServedHits": cceHttpRequestsBytesServedHits,
       "cceHttpRequestsBytesServedMisses": cceHttpRequestsBytesServedMisses,
       "cceHttpRequestsImsInmTotalCache": cceHttpRequestsImsInmTotalCache,
       "cceHttpRequestsImsInmTotalReval": cceHttpRequestsImsInmTotalReval,
       "cceHttpRequestsBytesClientIn": cceHttpRequestsBytesClientIn,
       "cceHttpRequestsBytesClientOut": cceHttpRequestsBytesClientOut,
       "cceHttpRequestsBytesServerIn": cceHttpRequestsBytesServerIn,
       "cceHttpRequestsBytesServerOut": cceHttpRequestsBytesServerOut,
       "cceHttpHCRequestsTotal": cceHttpHCRequestsTotal,
       "cceHttpHCRequestsNoCacheTotal": cceHttpHCRequestsNoCacheTotal,
       "cceHttpHCRequestsClientErrorTotal": cceHttpHCRequestsClientErrorTotal,
       "cceHttpHCRequestsServerErrorTotal": cceHttpHCRequestsServerErrorTotal,
       "cceHttpHCRequestsBlocked": cceHttpHCRequestsBlocked,
       "cceHttpHCRequestsHits": cceHttpHCRequestsHits,
       "cceHttpHCRequestsMisses": cceHttpHCRequestsMisses,
       "cceHttpHCRequestsBytesServedHits": cceHttpHCRequestsBytesServedHits,
       "cceHttpHCRequestsBytesServedMisses": cceHttpHCRequestsBytesServedMisses,
       "cceHttpHCRequestsImsInmTotalCache": cceHttpHCRequestsImsInmTotalCache,
       "cceHttpHCRequestsImsInmTotalReval": cceHttpHCRequestsImsInmTotalReval,
       "cceHttpHCRequestsBytesClientIn": cceHttpHCRequestsBytesClientIn,
       "cceHttpHCRequestsBytesClientOut": cceHttpHCRequestsBytesClientOut,
       "cceHttpHCRequestsBytesServerIn": cceHttpHCRequestsBytesServerIn,
       "cceHttpHCRequestsBytesServerOut": cceHttpHCRequestsBytesServerOut,
       "cceHttpPerf": cceHttpPerf,
       "cceHttpPerfSamplingTime": cceHttpPerfSamplingTime,
       "cceHttpPerfReqPerSec": cceHttpPerfReqPerSec,
       "cceHttpPerfBytesPerSec": cceHttpPerfBytesPerSec,
       "cceHttpPerfServiceTime": cceHttpPerfServiceTime,
       "cceHttpPerfHitServiceTime": cceHttpPerfHitServiceTime,
       "cceHttpPerfMissServiceTime": cceHttpPerfMissServiceTime,
       "cceHttpPerfObjectSize": cceHttpPerfObjectSize,
       "cceHttpPerfCpuLoad": cceHttpPerfCpuLoad,
       "cceWmtGroup": cceWmtGroup,
       "cceWmtRequests": cceWmtRequests,
       "cceWmtTotalRequests": cceWmtTotalRequests,
       "cceWmtTotalClientErrors": cceWmtTotalClientErrors,
       "cceWmtTotalServerErrors": cceWmtTotalServerErrors,
       "cceWmtBlockedRequests": cceWmtBlockedRequests,
       "cceWmtRequestHits": cceWmtRequestHits,
       "cceWmtRequestMisses": cceWmtRequestMisses,
       "cceWmtRequestHitsBytesServed": cceWmtRequestHitsBytesServed,
       "cceWmtRequestMissesBytesServed": cceWmtRequestMissesBytesServed,
       "cceWmtTotalLiveRequests": cceWmtTotalLiveRequests,
       "cceWmtLiveRequestBytes": cceWmtLiveRequestBytes,
       "cceWmtTotalMmsuRequests": cceWmtTotalMmsuRequests,
       "cceWmtTotalMmsuBytes": cceWmtTotalMmsuBytes,
       "cceWmtTotalMmstRequests": cceWmtTotalMmstRequests,
       "cceWmtTotalMmstBytes": cceWmtTotalMmstBytes,
       "cceWmtTotalHttpRequests": cceWmtTotalHttpRequests,
       "cceWmtTotalHttpBytes": cceWmtTotalHttpBytes,
       "cceWmtTotalMulticastBytes": cceWmtTotalMulticastBytes,
       "cceWmtTotalRtspuRequests": cceWmtTotalRtspuRequests,
       "cceWmtTotalRtspuBytes": cceWmtTotalRtspuBytes,
       "cceWmtTotalRtsptRequests": cceWmtTotalRtsptRequests,
       "cceWmtTotalRtsptBytes": cceWmtTotalRtsptBytes,
       "cceWmtHCRequests": cceWmtHCRequests,
       "cceWmtHCRequestHitsBytesServed": cceWmtHCRequestHitsBytesServed,
       "cceWmtHCRequestMissesBytesServed": cceWmtHCRequestMissesBytesServed,
       "cceWmtHCLiveRequestBytes": cceWmtHCLiveRequestBytes,
       "cceWmtHCTotalMmsuBytes": cceWmtHCTotalMmsuBytes,
       "cceWmtHCTotalMmstBytes": cceWmtHCTotalMmstBytes,
       "cceWmtHCTotalHttpBytes": cceWmtHCTotalHttpBytes,
       "cceWmtHCTotalMulticastBytes": cceWmtHCTotalMulticastBytes,
       "cceWmtHCTotalRtspuBytes": cceWmtHCTotalRtspuBytes,
       "cceWmtHCTotalRtsptBytes": cceWmtHCTotalRtsptBytes,
       "cceWmtPerf": cceWmtPerf,
       "cceWmtPerfConcurrentRequests": cceWmtPerfConcurrentRequests,
       "cceWmtPerfKbitsPerSec": cceWmtPerfKbitsPerSec,
       "cceWmtPerfMulticastSessions": cceWmtPerfMulticastSessions,
       "cceWmtPerfMulticastKbitsPerSec": cceWmtPerfMulticastKbitsPerSec,
       "cceCseGroup": cceCseGroup,
       "cceCseRequests": cceCseRequests,
       "cceCseTotalRequests": cceCseTotalRequests,
       "cceCseRequestPacketsServed": cceCseRequestPacketsServed,
       "cceCseRequestBytesServed": cceCseRequestBytesServed,
       "cceCseHCRequests": cceCseHCRequests,
       "cceCseHCRequestPacketsServed": cceCseHCRequestPacketsServed,
       "cceCseHCRequestBytesServed": cceCseHCRequestBytesServed,
       "cceCsePerf": cceCsePerf,
       "cceCsePerfConcurrentReqs": cceCsePerfConcurrentReqs,
       "cceCsePerfCurrentBandwidth": cceCsePerfCurrentBandwidth,
       "cceRpGroup": cceRpGroup,
       "cceRpRequests": cceRpRequests,
       "cceRpTotalHits": cceRpTotalHits,
       "cceRpTotalMisses": cceRpTotalMisses,
       "cceRpTotalVodPassThroughs": cceRpTotalVodPassThroughs,
       "cceRpTotalLiveSplitReqs": cceRpTotalLiveSplitReqs,
       "cceRpTotalLivePassThruSplitReqs": cceRpTotalLivePassThruSplitReqs,
       "cceRpTotalIncomingBytes": cceRpTotalIncomingBytes,
       "cceRpTotalOutgoingBytes": cceRpTotalOutgoingBytes,
       "cceRpHCRequests": cceRpHCRequests,
       "cceRpHCTotalHits": cceRpHCTotalHits,
       "cceRpHCTotalMisses": cceRpHCTotalMisses,
       "cceRpHCTotalVodPassThroughs": cceRpHCTotalVodPassThroughs,
       "cceRpHCTotalLiveSplitReqs": cceRpHCTotalLiveSplitReqs,
       "cceRpHCTotalLivePassThruSplitReqs": cceRpHCTotalLivePassThruSplitReqs,
       "cceRpHCTotalIncomingBytes": cceRpHCTotalIncomingBytes,
       "cceRpHCTotalOutgoingBytes": cceRpHCTotalOutgoingBytes,
       "cceNotificationInfo": cceNotificationInfo,
       "cceFailedDiskName": cceFailedDiskName,
       "cceAlarmGroup": cceAlarmGroup,
       "cceAlarmHistory": cceAlarmHistory,
       "cceAlarmHistTableSize": cceAlarmHistTableSize,
       "cceAlarmHistTable": cceAlarmHistTable,
       "cceAlarmHistEntry": cceAlarmHistEntry,
       "cceAlarmHistIndex": cceAlarmHistIndex,
       "cceAlarmHistId": cceAlarmHistId,
       "cceAlarmHistModuleId": cceAlarmHistModuleId,
       "cceAlarmHistType": cceAlarmHistType,
       "cceAlarmHistCategory": cceAlarmHistCategory,
       "cceAlarmHistSeverity": cceAlarmHistSeverity,
       "cceAlarmHistInfo": cceAlarmHistInfo,
       "cceAlarmHistTimeStamp": cceAlarmHistTimeStamp,
       "cceAlarmMonitoring": cceAlarmMonitoring,
       "cceAlarmCriticalCount": cceAlarmCriticalCount,
       "cceAlarmMajorCount": cceAlarmMajorCount,
       "cceAlarmMinorCount": cceAlarmMinorCount,
       "ciscoContentEngineMIBNotificationPrefix": ciscoContentEngineMIBNotificationPrefix,
       "ciscoContentEngineMIBNotifications": ciscoContentEngineMIBNotifications,
       "ciscoContentEngineReadDiskError": ciscoContentEngineReadDiskError,
       "ciscoContentEngineWriteDiskError": ciscoContentEngineWriteDiskError,
       "ciscoContentEngineWriteTransFailed": ciscoContentEngineWriteTransFailed,
       "ciscoContentEngineDataDiskFailed": ciscoContentEngineDataDiskFailed,
       "ciscoContentEngineOverloadBypass": ciscoContentEngineOverloadBypass,
       "ciscoContentEngineDiskFailed": ciscoContentEngineDiskFailed,
       "cceAlarmCriticalRaised": cceAlarmCriticalRaised,
       "cceAlarmCriticalCleared": cceAlarmCriticalCleared,
       "cceAlarmMajorRaised": cceAlarmMajorRaised,
       "cceAlarmMajorCleared": cceAlarmMajorCleared,
       "cceAlarmMinorRaised": cceAlarmMinorRaised,
       "cceAlarmMinorCleared": cceAlarmMinorCleared,
       "ciscoContentEngineMIBConformance": ciscoContentEngineMIBConformance,
       "ciscoContentEngineMIBCompliances": ciscoContentEngineMIBCompliances,
       "ciscoContentEngineMIBCompliance": ciscoContentEngineMIBCompliance,
       "ciscoContentEngineMIBComplianceRev1": ciscoContentEngineMIBComplianceRev1,
       "ciscoContentEngineMIBComplianceRev2": ciscoContentEngineMIBComplianceRev2,
       "ciscoContentEngineMIBComplianceRev3": ciscoContentEngineMIBComplianceRev3,
       "ciscoContentEngineMIBGroups": ciscoContentEngineMIBGroups,
       "cceHttpReqGroup": cceHttpReqGroup,
       "cceHttpHCReqGroup": cceHttpHCReqGroup,
       "cceHttpPerfGroup": cceHttpPerfGroup,
       "cceNotificationGroup": cceNotificationGroup,
       "cceWmtReqGroup": cceWmtReqGroup,
       "cceWmtHCGroup": cceWmtHCGroup,
       "cceWmtPerfGroup": cceWmtPerfGroup,
       "cceCseReqGroup": cceCseReqGroup,
       "cceCseHCGroup": cceCseHCGroup,
       "cceCsePerfGroup": cceCsePerfGroup,
       "cceRpReqGroup": cceRpReqGroup,
       "cceRpHCReqGroup": cceRpHCReqGroup,
       "cceNotificationGroupRev1": cceNotificationGroupRev1,
       "cceAlarmInfoGroup": cceAlarmInfoGroup,
       "cceNotificationInfoGroup": cceNotificationInfoGroup,
       "cceWmtReqGroupRev1": cceWmtReqGroupRev1,
       "cceWmtHCGroupRev1": cceWmtHCGroupRev1}
)
