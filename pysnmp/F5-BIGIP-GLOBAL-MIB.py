# SNMP MIB module (F5-BIGIP-GLOBAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/F5-BIGIP-GLOBAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:35 2024
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

(LongDisplayString,
 bigipCompliances,
 bigipGroups,
 bigipTrafficMgmt) = mibBuilder.importSymbols(
    "F5-BIGIP-COMMON-MIB",
    "LongDisplayString",
    "bigipCompliances",
    "bigipGroups",
    "bigipTrafficMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

bigipGlobalTM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GtmGlobals_ObjectIdentity = ObjectIdentity
gtmGlobals = _GtmGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1)
)
_GtmGlobalAttrs_ObjectIdentity = ObjectIdentity
gtmGlobalAttrs = _GtmGlobalAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1)
)
_GtmGlobalAttr_ObjectIdentity = ObjectIdentity
gtmGlobalAttr = _GtmGlobalAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1)
)


class _GtmAttrDumpTopology_Type(Integer32):
    """Custom type gtmAttrDumpTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttrDumpTopology_Type.__name__ = "Integer32"
_GtmAttrDumpTopology_Object = MibScalar
gtmAttrDumpTopology = _GtmAttrDumpTopology_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 1),
    _GtmAttrDumpTopology_Type()
)
gtmAttrDumpTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrDumpTopology.setStatus("deprecated")


class _GtmAttrCacheLdns_Type(Integer32):
    """Custom type gtmAttrCacheLdns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttrCacheLdns_Type.__name__ = "Integer32"
_GtmAttrCacheLdns_Object = MibScalar
gtmAttrCacheLdns = _GtmAttrCacheLdns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 2),
    _GtmAttrCacheLdns_Type()
)
gtmAttrCacheLdns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrCacheLdns.setStatus("deprecated")


class _GtmAttrAolAware_Type(Integer32):
    """Custom type gtmAttrAolAware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttrAolAware_Type.__name__ = "Integer32"
_GtmAttrAolAware_Object = MibScalar
gtmAttrAolAware = _GtmAttrAolAware_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 3),
    _GtmAttrAolAware_Type()
)
gtmAttrAolAware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrAolAware.setStatus("deprecated")


class _GtmAttrCheckStaticDepends_Type(Integer32):
    """Custom type gtmAttrCheckStaticDepends based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttrCheckStaticDepends_Type.__name__ = "Integer32"
_GtmAttrCheckStaticDepends_Object = MibScalar
gtmAttrCheckStaticDepends = _GtmAttrCheckStaticDepends_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 4),
    _GtmAttrCheckStaticDepends_Type()
)
gtmAttrCheckStaticDepends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrCheckStaticDepends.setStatus("deprecated")


class _GtmAttrCheckDynamicDepends_Type(Integer32):
    """Custom type gtmAttrCheckDynamicDepends based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttrCheckDynamicDepends_Type.__name__ = "Integer32"
_GtmAttrCheckDynamicDepends_Object = MibScalar
gtmAttrCheckDynamicDepends = _GtmAttrCheckDynamicDepends_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 5),
    _GtmAttrCheckDynamicDepends_Type()
)
gtmAttrCheckDynamicDepends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrCheckDynamicDepends.setStatus("deprecated")


class _GtmAttrDrainRequests_Type(Integer32):
    """Custom type gtmAttrDrainRequests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttrDrainRequests_Type.__name__ = "Integer32"
_GtmAttrDrainRequests_Object = MibScalar
gtmAttrDrainRequests = _GtmAttrDrainRequests_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 6),
    _GtmAttrDrainRequests_Type()
)
gtmAttrDrainRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrDrainRequests.setStatus("deprecated")


class _GtmAttrEnableResetsRipeness_Type(Integer32):
    """Custom type gtmAttrEnableResetsRipeness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttrEnableResetsRipeness_Type.__name__ = "Integer32"
_GtmAttrEnableResetsRipeness_Object = MibScalar
gtmAttrEnableResetsRipeness = _GtmAttrEnableResetsRipeness_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 7),
    _GtmAttrEnableResetsRipeness_Type()
)
gtmAttrEnableResetsRipeness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrEnableResetsRipeness.setStatus("deprecated")


class _GtmAttrFbRespectDepends_Type(Integer32):
    """Custom type gtmAttrFbRespectDepends based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttrFbRespectDepends_Type.__name__ = "Integer32"
_GtmAttrFbRespectDepends_Object = MibScalar
gtmAttrFbRespectDepends = _GtmAttrFbRespectDepends_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 8),
    _GtmAttrFbRespectDepends_Type()
)
gtmAttrFbRespectDepends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrFbRespectDepends.setStatus("deprecated")


class _GtmAttrFbRespectAcl_Type(Integer32):
    """Custom type gtmAttrFbRespectAcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttrFbRespectAcl_Type.__name__ = "Integer32"
_GtmAttrFbRespectAcl_Object = MibScalar
gtmAttrFbRespectAcl = _GtmAttrFbRespectAcl_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 9),
    _GtmAttrFbRespectAcl_Type()
)
gtmAttrFbRespectAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrFbRespectAcl.setStatus("deprecated")


class _GtmAttrDefaultAlternate_Type(Integer32):
    """Custom type gtmAttrDefaultAlternate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("bps", 15),
          ("cpu", 12),
          ("droppacket", 16),
          ("explicitip", 17),
          ("ga", 6),
          ("hitratio", 13),
          ("leastconn", 8),
          ("lowesthops", 10),
          ("lowestrtt", 9),
          ("null", 1),
          ("packetrate", 11),
          ("qos", 14),
          ("ratio", 3),
          ("returntodns", 0),
          ("roundrobin", 2),
          ("statpersist", 5),
          ("topology", 4),
          ("vscapacity", 7),
          ("vssore", 18))
    )


_GtmAttrDefaultAlternate_Type.__name__ = "Integer32"
_GtmAttrDefaultAlternate_Object = MibScalar
gtmAttrDefaultAlternate = _GtmAttrDefaultAlternate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 10),
    _GtmAttrDefaultAlternate_Type()
)
gtmAttrDefaultAlternate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrDefaultAlternate.setStatus("deprecated")


class _GtmAttrDefaultFallback_Type(Integer32):
    """Custom type gtmAttrDefaultFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("bps", 15),
          ("cpu", 12),
          ("droppacket", 16),
          ("explicitip", 17),
          ("ga", 6),
          ("hitratio", 13),
          ("leastconn", 8),
          ("lowesthops", 10),
          ("lowestrtt", 9),
          ("null", 1),
          ("packetrate", 11),
          ("qos", 14),
          ("ratio", 3),
          ("returntodns", 0),
          ("roundrobin", 2),
          ("statpersit", 5),
          ("topology", 4),
          ("vscapacity", 7),
          ("vsscore", 18))
    )


_GtmAttrDefaultFallback_Type.__name__ = "Integer32"
_GtmAttrDefaultFallback_Object = MibScalar
gtmAttrDefaultFallback = _GtmAttrDefaultFallback_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 11),
    _GtmAttrDefaultFallback_Type()
)
gtmAttrDefaultFallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrDefaultFallback.setStatus("deprecated")
_GtmAttrPersistMask_Type = Integer32
_GtmAttrPersistMask_Object = MibScalar
gtmAttrPersistMask = _GtmAttrPersistMask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 12),
    _GtmAttrPersistMask_Type()
)
gtmAttrPersistMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrPersistMask.setStatus("deprecated")


class _GtmAttrGtmSetsRecursion_Type(Integer32):
    """Custom type gtmAttrGtmSetsRecursion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttrGtmSetsRecursion_Type.__name__ = "Integer32"
_GtmAttrGtmSetsRecursion_Object = MibScalar
gtmAttrGtmSetsRecursion = _GtmAttrGtmSetsRecursion_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 13),
    _GtmAttrGtmSetsRecursion_Type()
)
gtmAttrGtmSetsRecursion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrGtmSetsRecursion.setStatus("deprecated")
_GtmAttrQosFactorLcs_Type = Integer32
_GtmAttrQosFactorLcs_Object = MibScalar
gtmAttrQosFactorLcs = _GtmAttrQosFactorLcs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 14),
    _GtmAttrQosFactorLcs_Type()
)
gtmAttrQosFactorLcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrQosFactorLcs.setStatus("deprecated")
_GtmAttrQosFactorRtt_Type = Integer32
_GtmAttrQosFactorRtt_Object = MibScalar
gtmAttrQosFactorRtt = _GtmAttrQosFactorRtt_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 15),
    _GtmAttrQosFactorRtt_Type()
)
gtmAttrQosFactorRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrQosFactorRtt.setStatus("deprecated")
_GtmAttrQosFactorHops_Type = Integer32
_GtmAttrQosFactorHops_Object = MibScalar
gtmAttrQosFactorHops = _GtmAttrQosFactorHops_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 16),
    _GtmAttrQosFactorHops_Type()
)
gtmAttrQosFactorHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrQosFactorHops.setStatus("deprecated")
_GtmAttrQosFactorHitRatio_Type = Integer32
_GtmAttrQosFactorHitRatio_Object = MibScalar
gtmAttrQosFactorHitRatio = _GtmAttrQosFactorHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 17),
    _GtmAttrQosFactorHitRatio_Type()
)
gtmAttrQosFactorHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrQosFactorHitRatio.setStatus("deprecated")
_GtmAttrQosFactorPacketRate_Type = Integer32
_GtmAttrQosFactorPacketRate_Object = MibScalar
gtmAttrQosFactorPacketRate = _GtmAttrQosFactorPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 18),
    _GtmAttrQosFactorPacketRate_Type()
)
gtmAttrQosFactorPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrQosFactorPacketRate.setStatus("deprecated")
_GtmAttrQosFactorBps_Type = Integer32
_GtmAttrQosFactorBps_Object = MibScalar
gtmAttrQosFactorBps = _GtmAttrQosFactorBps_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 19),
    _GtmAttrQosFactorBps_Type()
)
gtmAttrQosFactorBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrQosFactorBps.setStatus("deprecated")
_GtmAttrQosFactorVsCapacity_Type = Integer32
_GtmAttrQosFactorVsCapacity_Object = MibScalar
gtmAttrQosFactorVsCapacity = _GtmAttrQosFactorVsCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 20),
    _GtmAttrQosFactorVsCapacity_Type()
)
gtmAttrQosFactorVsCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrQosFactorVsCapacity.setStatus("deprecated")
_GtmAttrQosFactorTopology_Type = Integer32
_GtmAttrQosFactorTopology_Object = MibScalar
gtmAttrQosFactorTopology = _GtmAttrQosFactorTopology_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 21),
    _GtmAttrQosFactorTopology_Type()
)
gtmAttrQosFactorTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrQosFactorTopology.setStatus("deprecated")
_GtmAttrQosFactorConnRate_Type = Integer32
_GtmAttrQosFactorConnRate_Object = MibScalar
gtmAttrQosFactorConnRate = _GtmAttrQosFactorConnRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 22),
    _GtmAttrQosFactorConnRate_Type()
)
gtmAttrQosFactorConnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrQosFactorConnRate.setStatus("deprecated")
_GtmAttrTimerRetryPathData_Type = Integer32
_GtmAttrTimerRetryPathData_Object = MibScalar
gtmAttrTimerRetryPathData = _GtmAttrTimerRetryPathData_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 23),
    _GtmAttrTimerRetryPathData_Type()
)
gtmAttrTimerRetryPathData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrTimerRetryPathData.setStatus("deprecated")
_GtmAttrTimerGetAutoconfigData_Type = Integer32
_GtmAttrTimerGetAutoconfigData_Object = MibScalar
gtmAttrTimerGetAutoconfigData = _GtmAttrTimerGetAutoconfigData_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 24),
    _GtmAttrTimerGetAutoconfigData_Type()
)
gtmAttrTimerGetAutoconfigData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrTimerGetAutoconfigData.setStatus("deprecated")
_GtmAttrTimerPersistCache_Type = Integer32
_GtmAttrTimerPersistCache_Object = MibScalar
gtmAttrTimerPersistCache = _GtmAttrTimerPersistCache_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 25),
    _GtmAttrTimerPersistCache_Type()
)
gtmAttrTimerPersistCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrTimerPersistCache.setStatus("deprecated")
_GtmAttrDefaultProbeLimit_Type = Integer32
_GtmAttrDefaultProbeLimit_Object = MibScalar
gtmAttrDefaultProbeLimit = _GtmAttrDefaultProbeLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 26),
    _GtmAttrDefaultProbeLimit_Type()
)
gtmAttrDefaultProbeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrDefaultProbeLimit.setStatus("deprecated")
_GtmAttrDownThreshold_Type = Integer32
_GtmAttrDownThreshold_Object = MibScalar
gtmAttrDownThreshold = _GtmAttrDownThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 27),
    _GtmAttrDownThreshold_Type()
)
gtmAttrDownThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrDownThreshold.setStatus("deprecated")
_GtmAttrDownMultiple_Type = Integer32
_GtmAttrDownMultiple_Object = MibScalar
gtmAttrDownMultiple = _GtmAttrDownMultiple_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 28),
    _GtmAttrDownMultiple_Type()
)
gtmAttrDownMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrDownMultiple.setStatus("deprecated")
_GtmAttrPathTtl_Type = Integer32
_GtmAttrPathTtl_Object = MibScalar
gtmAttrPathTtl = _GtmAttrPathTtl_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 29),
    _GtmAttrPathTtl_Type()
)
gtmAttrPathTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrPathTtl.setStatus("deprecated")
_GtmAttrTraceTtl_Type = Integer32
_GtmAttrTraceTtl_Object = MibScalar
gtmAttrTraceTtl = _GtmAttrTraceTtl_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 30),
    _GtmAttrTraceTtl_Type()
)
gtmAttrTraceTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrTraceTtl.setStatus("deprecated")
_GtmAttrLdnsDuration_Type = Integer32
_GtmAttrLdnsDuration_Object = MibScalar
gtmAttrLdnsDuration = _GtmAttrLdnsDuration_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 31),
    _GtmAttrLdnsDuration_Type()
)
gtmAttrLdnsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrLdnsDuration.setStatus("deprecated")
_GtmAttrPathDuration_Type = Integer32
_GtmAttrPathDuration_Object = MibScalar
gtmAttrPathDuration = _GtmAttrPathDuration_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 32),
    _GtmAttrPathDuration_Type()
)
gtmAttrPathDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrPathDuration.setStatus("deprecated")
_GtmAttrRttSampleCount_Type = Integer32
_GtmAttrRttSampleCount_Object = MibScalar
gtmAttrRttSampleCount = _GtmAttrRttSampleCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 33),
    _GtmAttrRttSampleCount_Type()
)
gtmAttrRttSampleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrRttSampleCount.setStatus("deprecated")
_GtmAttrRttPacketLength_Type = Integer32
_GtmAttrRttPacketLength_Object = MibScalar
gtmAttrRttPacketLength = _GtmAttrRttPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 34),
    _GtmAttrRttPacketLength_Type()
)
gtmAttrRttPacketLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrRttPacketLength.setStatus("deprecated")
_GtmAttrRttTimeout_Type = Integer32
_GtmAttrRttTimeout_Object = MibScalar
gtmAttrRttTimeout = _GtmAttrRttTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 35),
    _GtmAttrRttTimeout_Type()
)
gtmAttrRttTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrRttTimeout.setStatus("deprecated")
_GtmAttrMaxMonReqs_Type = Integer32
_GtmAttrMaxMonReqs_Object = MibScalar
gtmAttrMaxMonReqs = _GtmAttrMaxMonReqs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 36),
    _GtmAttrMaxMonReqs_Type()
)
gtmAttrMaxMonReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrMaxMonReqs.setStatus("deprecated")
_GtmAttrTraceroutePort_Type = Integer32
_GtmAttrTraceroutePort_Object = MibScalar
gtmAttrTraceroutePort = _GtmAttrTraceroutePort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 37),
    _GtmAttrTraceroutePort_Type()
)
gtmAttrTraceroutePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrTraceroutePort.setStatus("deprecated")


class _GtmAttrPathsNeverDie_Type(Integer32):
    """Custom type gtmAttrPathsNeverDie based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttrPathsNeverDie_Type.__name__ = "Integer32"
_GtmAttrPathsNeverDie_Object = MibScalar
gtmAttrPathsNeverDie = _GtmAttrPathsNeverDie_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 38),
    _GtmAttrPathsNeverDie_Type()
)
gtmAttrPathsNeverDie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrPathsNeverDie.setStatus("deprecated")


class _GtmAttrProbeDisabledObjects_Type(Integer32):
    """Custom type gtmAttrProbeDisabledObjects based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttrProbeDisabledObjects_Type.__name__ = "Integer32"
_GtmAttrProbeDisabledObjects_Object = MibScalar
gtmAttrProbeDisabledObjects = _GtmAttrProbeDisabledObjects_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 39),
    _GtmAttrProbeDisabledObjects_Type()
)
gtmAttrProbeDisabledObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrProbeDisabledObjects.setStatus("deprecated")
_GtmAttrLinkLimitFactor_Type = Integer32
_GtmAttrLinkLimitFactor_Object = MibScalar
gtmAttrLinkLimitFactor = _GtmAttrLinkLimitFactor_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 40),
    _GtmAttrLinkLimitFactor_Type()
)
gtmAttrLinkLimitFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrLinkLimitFactor.setStatus("deprecated")
_GtmAttrOverLimitLinkLimitFactor_Type = Integer32
_GtmAttrOverLimitLinkLimitFactor_Object = MibScalar
gtmAttrOverLimitLinkLimitFactor = _GtmAttrOverLimitLinkLimitFactor_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 41),
    _GtmAttrOverLimitLinkLimitFactor_Type()
)
gtmAttrOverLimitLinkLimitFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrOverLimitLinkLimitFactor.setStatus("deprecated")
_GtmAttrLinkPrepaidFactor_Type = Integer32
_GtmAttrLinkPrepaidFactor_Object = MibScalar
gtmAttrLinkPrepaidFactor = _GtmAttrLinkPrepaidFactor_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 42),
    _GtmAttrLinkPrepaidFactor_Type()
)
gtmAttrLinkPrepaidFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrLinkPrepaidFactor.setStatus("deprecated")
_GtmAttrLinkCompensateInbound_Type = Integer32
_GtmAttrLinkCompensateInbound_Object = MibScalar
gtmAttrLinkCompensateInbound = _GtmAttrLinkCompensateInbound_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 43),
    _GtmAttrLinkCompensateInbound_Type()
)
gtmAttrLinkCompensateInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrLinkCompensateInbound.setStatus("deprecated")
_GtmAttrLinkCompensateOutbound_Type = Integer32
_GtmAttrLinkCompensateOutbound_Object = MibScalar
gtmAttrLinkCompensateOutbound = _GtmAttrLinkCompensateOutbound_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 44),
    _GtmAttrLinkCompensateOutbound_Type()
)
gtmAttrLinkCompensateOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrLinkCompensateOutbound.setStatus("deprecated")
_GtmAttrLinkCompensationHistory_Type = Integer32
_GtmAttrLinkCompensationHistory_Object = MibScalar
gtmAttrLinkCompensationHistory = _GtmAttrLinkCompensationHistory_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 45),
    _GtmAttrLinkCompensationHistory_Type()
)
gtmAttrLinkCompensationHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrLinkCompensationHistory.setStatus("deprecated")
_GtmAttrMaxLinkOverLimitCount_Type = Integer32
_GtmAttrMaxLinkOverLimitCount_Object = MibScalar
gtmAttrMaxLinkOverLimitCount = _GtmAttrMaxLinkOverLimitCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 46),
    _GtmAttrMaxLinkOverLimitCount_Type()
)
gtmAttrMaxLinkOverLimitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrMaxLinkOverLimitCount.setStatus("deprecated")
_GtmAttrLowerBoundPctRow_Type = Integer32
_GtmAttrLowerBoundPctRow_Object = MibScalar
gtmAttrLowerBoundPctRow = _GtmAttrLowerBoundPctRow_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 47),
    _GtmAttrLowerBoundPctRow_Type()
)
gtmAttrLowerBoundPctRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrLowerBoundPctRow.setStatus("deprecated")
_GtmAttrLowerBoundPctCol_Type = Integer32
_GtmAttrLowerBoundPctCol_Object = MibScalar
gtmAttrLowerBoundPctCol = _GtmAttrLowerBoundPctCol_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 48),
    _GtmAttrLowerBoundPctCol_Type()
)
gtmAttrLowerBoundPctCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrLowerBoundPctCol.setStatus("deprecated")


class _GtmAttrAutoconf_Type(Integer32):
    """Custom type gtmAttrAutoconf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttrAutoconf_Type.__name__ = "Integer32"
_GtmAttrAutoconf_Object = MibScalar
gtmAttrAutoconf = _GtmAttrAutoconf_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 49),
    _GtmAttrAutoconf_Type()
)
gtmAttrAutoconf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrAutoconf.setStatus("deprecated")


class _GtmAttrAutosync_Type(Integer32):
    """Custom type gtmAttrAutosync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttrAutosync_Type.__name__ = "Integer32"
_GtmAttrAutosync_Object = MibScalar
gtmAttrAutosync = _GtmAttrAutosync_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 50),
    _GtmAttrAutosync_Type()
)
gtmAttrAutosync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrAutosync.setStatus("deprecated")


class _GtmAttrSyncNamedConf_Type(Integer32):
    """Custom type gtmAttrSyncNamedConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttrSyncNamedConf_Type.__name__ = "Integer32"
_GtmAttrSyncNamedConf_Object = MibScalar
gtmAttrSyncNamedConf = _GtmAttrSyncNamedConf_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 51),
    _GtmAttrSyncNamedConf_Type()
)
gtmAttrSyncNamedConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrSyncNamedConf.setStatus("deprecated")
_GtmAttrSyncGroup_Type = LongDisplayString
_GtmAttrSyncGroup_Object = MibScalar
gtmAttrSyncGroup = _GtmAttrSyncGroup_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 52),
    _GtmAttrSyncGroup_Type()
)
gtmAttrSyncGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrSyncGroup.setStatus("deprecated")
_GtmAttrSyncTimeout_Type = Integer32
_GtmAttrSyncTimeout_Object = MibScalar
gtmAttrSyncTimeout = _GtmAttrSyncTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 53),
    _GtmAttrSyncTimeout_Type()
)
gtmAttrSyncTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrSyncTimeout.setStatus("deprecated")
_GtmAttrSyncZonesTimeout_Type = Integer32
_GtmAttrSyncZonesTimeout_Object = MibScalar
gtmAttrSyncZonesTimeout = _GtmAttrSyncZonesTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 54),
    _GtmAttrSyncZonesTimeout_Type()
)
gtmAttrSyncZonesTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrSyncZonesTimeout.setStatus("deprecated")
_GtmAttrTimeTolerance_Type = Integer32
_GtmAttrTimeTolerance_Object = MibScalar
gtmAttrTimeTolerance = _GtmAttrTimeTolerance_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 55),
    _GtmAttrTimeTolerance_Type()
)
gtmAttrTimeTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrTimeTolerance.setStatus("deprecated")


class _GtmAttrTopologyLongestMatch_Type(Integer32):
    """Custom type gtmAttrTopologyLongestMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttrTopologyLongestMatch_Type.__name__ = "Integer32"
_GtmAttrTopologyLongestMatch_Object = MibScalar
gtmAttrTopologyLongestMatch = _GtmAttrTopologyLongestMatch_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 56),
    _GtmAttrTopologyLongestMatch_Type()
)
gtmAttrTopologyLongestMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrTopologyLongestMatch.setStatus("deprecated")
_GtmAttrTopologyAclThreshold_Type = Integer32
_GtmAttrTopologyAclThreshold_Object = MibScalar
gtmAttrTopologyAclThreshold = _GtmAttrTopologyAclThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 57),
    _GtmAttrTopologyAclThreshold_Type()
)
gtmAttrTopologyAclThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrTopologyAclThreshold.setStatus("deprecated")
_GtmAttrStaticPersistCidr_Type = Integer32
_GtmAttrStaticPersistCidr_Object = MibScalar
gtmAttrStaticPersistCidr = _GtmAttrStaticPersistCidr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 58),
    _GtmAttrStaticPersistCidr_Type()
)
gtmAttrStaticPersistCidr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrStaticPersistCidr.setStatus("deprecated")
_GtmAttrStaticPersistV6Cidr_Type = Integer32
_GtmAttrStaticPersistV6Cidr_Object = MibScalar
gtmAttrStaticPersistV6Cidr = _GtmAttrStaticPersistV6Cidr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 59),
    _GtmAttrStaticPersistV6Cidr_Type()
)
gtmAttrStaticPersistV6Cidr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrStaticPersistV6Cidr.setStatus("deprecated")
_GtmAttrQosFactorVsScore_Type = Integer32
_GtmAttrQosFactorVsScore_Object = MibScalar
gtmAttrQosFactorVsScore = _GtmAttrQosFactorVsScore_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 60),
    _GtmAttrQosFactorVsScore_Type()
)
gtmAttrQosFactorVsScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrQosFactorVsScore.setStatus("deprecated")
_GtmAttrTimerSendKeepAlive_Type = Integer32
_GtmAttrTimerSendKeepAlive_Object = MibScalar
gtmAttrTimerSendKeepAlive = _GtmAttrTimerSendKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 61),
    _GtmAttrTimerSendKeepAlive_Type()
)
gtmAttrTimerSendKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrTimerSendKeepAlive.setStatus("deprecated")
_GtmAttrCertificateDepth_Type = Integer32
_GtmAttrCertificateDepth_Object = MibScalar
gtmAttrCertificateDepth = _GtmAttrCertificateDepth_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 62),
    _GtmAttrCertificateDepth_Type()
)
gtmAttrCertificateDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrCertificateDepth.setStatus("deprecated")
_GtmAttrMaxMemoryUsage_Type = Integer32
_GtmAttrMaxMemoryUsage_Object = MibScalar
gtmAttrMaxMemoryUsage = _GtmAttrMaxMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 1, 63),
    _GtmAttrMaxMemoryUsage_Type()
)
gtmAttrMaxMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttrMaxMemoryUsage.setStatus("deprecated")
_GtmGlobalLdnsProbeProto_ObjectIdentity = ObjectIdentity
gtmGlobalLdnsProbeProto = _GtmGlobalLdnsProbeProto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 2)
)
_GtmGlobalLdnsProbeProtoNumber_Type = Integer32
_GtmGlobalLdnsProbeProtoNumber_Object = MibScalar
gtmGlobalLdnsProbeProtoNumber = _GtmGlobalLdnsProbeProtoNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 2, 1),
    _GtmGlobalLdnsProbeProtoNumber_Type()
)
gtmGlobalLdnsProbeProtoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmGlobalLdnsProbeProtoNumber.setStatus("current")
_GtmGlobalLdnsProbeProtoTable_Object = MibTable
gtmGlobalLdnsProbeProtoTable = _GtmGlobalLdnsProbeProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    gtmGlobalLdnsProbeProtoTable.setStatus("current")
_GtmGlobalLdnsProbeProtoEntry_Object = MibTableRow
gtmGlobalLdnsProbeProtoEntry = _GtmGlobalLdnsProbeProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 2, 2, 1)
)
gtmGlobalLdnsProbeProtoEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmGlobalLdnsProbeProtoName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmGlobalLdnsProbeProtoIndex"),
)
if mibBuilder.loadTexts:
    gtmGlobalLdnsProbeProtoEntry.setStatus("current")


class _GtmGlobalLdnsProbeProtoIndex_Type(Integer32):
    """Custom type gtmGlobalLdnsProbeProtoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GtmGlobalLdnsProbeProtoIndex_Type.__name__ = "Integer32"
_GtmGlobalLdnsProbeProtoIndex_Object = MibTableColumn
gtmGlobalLdnsProbeProtoIndex = _GtmGlobalLdnsProbeProtoIndex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 2, 2, 1, 1),
    _GtmGlobalLdnsProbeProtoIndex_Type()
)
gtmGlobalLdnsProbeProtoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmGlobalLdnsProbeProtoIndex.setStatus("current")


class _GtmGlobalLdnsProbeProtoType_Type(Integer32):
    """Custom type gtmGlobalLdnsProbeProtoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dnsdot", 3),
          ("dnsrev", 4),
          ("icmp", 0),
          ("tcp", 1),
          ("udp", 2))
    )


_GtmGlobalLdnsProbeProtoType_Type.__name__ = "Integer32"
_GtmGlobalLdnsProbeProtoType_Object = MibTableColumn
gtmGlobalLdnsProbeProtoType = _GtmGlobalLdnsProbeProtoType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 2, 2, 1, 2),
    _GtmGlobalLdnsProbeProtoType_Type()
)
gtmGlobalLdnsProbeProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmGlobalLdnsProbeProtoType.setStatus("current")
_GtmGlobalLdnsProbeProtoName_Type = LongDisplayString
_GtmGlobalLdnsProbeProtoName_Object = MibTableColumn
gtmGlobalLdnsProbeProtoName = _GtmGlobalLdnsProbeProtoName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 2, 2, 1, 3),
    _GtmGlobalLdnsProbeProtoName_Type()
)
gtmGlobalLdnsProbeProtoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmGlobalLdnsProbeProtoName.setStatus("current")
_GtmGlobalAttr2_ObjectIdentity = ObjectIdentity
gtmGlobalAttr2 = _GtmGlobalAttr2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3)
)
_GtmAttr2Number_Type = Integer32
_GtmAttr2Number_Object = MibScalar
gtmAttr2Number = _GtmAttr2Number_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 1),
    _GtmAttr2Number_Type()
)
gtmAttr2Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2Number.setStatus("current")
_GtmAttr2Table_Object = MibTable
gtmAttr2Table = _GtmAttr2Table_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gtmAttr2Table.setStatus("current")
_GtmAttr2Entry_Object = MibTableRow
gtmAttr2Entry = _GtmAttr2Entry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1)
)
gtmAttr2Entry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmAttr2Name"),
)
if mibBuilder.loadTexts:
    gtmAttr2Entry.setStatus("current")


class _GtmAttr2DumpTopology_Type(Integer32):
    """Custom type gtmAttr2DumpTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttr2DumpTopology_Type.__name__ = "Integer32"
_GtmAttr2DumpTopology_Object = MibTableColumn
gtmAttr2DumpTopology = _GtmAttr2DumpTopology_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 1),
    _GtmAttr2DumpTopology_Type()
)
gtmAttr2DumpTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2DumpTopology.setStatus("current")


class _GtmAttr2CacheLdns_Type(Integer32):
    """Custom type gtmAttr2CacheLdns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttr2CacheLdns_Type.__name__ = "Integer32"
_GtmAttr2CacheLdns_Object = MibTableColumn
gtmAttr2CacheLdns = _GtmAttr2CacheLdns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 2),
    _GtmAttr2CacheLdns_Type()
)
gtmAttr2CacheLdns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2CacheLdns.setStatus("current")


class _GtmAttr2AolAware_Type(Integer32):
    """Custom type gtmAttr2AolAware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttr2AolAware_Type.__name__ = "Integer32"
_GtmAttr2AolAware_Object = MibTableColumn
gtmAttr2AolAware = _GtmAttr2AolAware_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 3),
    _GtmAttr2AolAware_Type()
)
gtmAttr2AolAware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2AolAware.setStatus("current")


class _GtmAttr2CheckStaticDepends_Type(Integer32):
    """Custom type gtmAttr2CheckStaticDepends based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttr2CheckStaticDepends_Type.__name__ = "Integer32"
_GtmAttr2CheckStaticDepends_Object = MibTableColumn
gtmAttr2CheckStaticDepends = _GtmAttr2CheckStaticDepends_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 4),
    _GtmAttr2CheckStaticDepends_Type()
)
gtmAttr2CheckStaticDepends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2CheckStaticDepends.setStatus("current")


class _GtmAttr2CheckDynamicDepends_Type(Integer32):
    """Custom type gtmAttr2CheckDynamicDepends based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttr2CheckDynamicDepends_Type.__name__ = "Integer32"
_GtmAttr2CheckDynamicDepends_Object = MibTableColumn
gtmAttr2CheckDynamicDepends = _GtmAttr2CheckDynamicDepends_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 5),
    _GtmAttr2CheckDynamicDepends_Type()
)
gtmAttr2CheckDynamicDepends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2CheckDynamicDepends.setStatus("current")


class _GtmAttr2DrainRequests_Type(Integer32):
    """Custom type gtmAttr2DrainRequests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttr2DrainRequests_Type.__name__ = "Integer32"
_GtmAttr2DrainRequests_Object = MibTableColumn
gtmAttr2DrainRequests = _GtmAttr2DrainRequests_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 6),
    _GtmAttr2DrainRequests_Type()
)
gtmAttr2DrainRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2DrainRequests.setStatus("current")


class _GtmAttr2EnableResetsRipeness_Type(Integer32):
    """Custom type gtmAttr2EnableResetsRipeness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttr2EnableResetsRipeness_Type.__name__ = "Integer32"
_GtmAttr2EnableResetsRipeness_Object = MibTableColumn
gtmAttr2EnableResetsRipeness = _GtmAttr2EnableResetsRipeness_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 7),
    _GtmAttr2EnableResetsRipeness_Type()
)
gtmAttr2EnableResetsRipeness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2EnableResetsRipeness.setStatus("current")


class _GtmAttr2FbRespectDepends_Type(Integer32):
    """Custom type gtmAttr2FbRespectDepends based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttr2FbRespectDepends_Type.__name__ = "Integer32"
_GtmAttr2FbRespectDepends_Object = MibTableColumn
gtmAttr2FbRespectDepends = _GtmAttr2FbRespectDepends_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 8),
    _GtmAttr2FbRespectDepends_Type()
)
gtmAttr2FbRespectDepends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2FbRespectDepends.setStatus("current")


class _GtmAttr2FbRespectAcl_Type(Integer32):
    """Custom type gtmAttr2FbRespectAcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttr2FbRespectAcl_Type.__name__ = "Integer32"
_GtmAttr2FbRespectAcl_Object = MibTableColumn
gtmAttr2FbRespectAcl = _GtmAttr2FbRespectAcl_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 9),
    _GtmAttr2FbRespectAcl_Type()
)
gtmAttr2FbRespectAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2FbRespectAcl.setStatus("deprecated")


class _GtmAttr2DefaultAlternate_Type(Integer32):
    """Custom type gtmAttr2DefaultAlternate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("bps", 15),
          ("cpu", 12),
          ("droppacket", 16),
          ("explicitip", 17),
          ("ga", 6),
          ("hitratio", 13),
          ("leastconn", 8),
          ("lowesthops", 10),
          ("lowestrtt", 9),
          ("null", 1),
          ("packetrate", 11),
          ("qos", 14),
          ("ratio", 3),
          ("returntodns", 0),
          ("roundrobin", 2),
          ("statpersist", 5),
          ("topology", 4),
          ("vscapacity", 7),
          ("vssore", 18))
    )


_GtmAttr2DefaultAlternate_Type.__name__ = "Integer32"
_GtmAttr2DefaultAlternate_Object = MibTableColumn
gtmAttr2DefaultAlternate = _GtmAttr2DefaultAlternate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 10),
    _GtmAttr2DefaultAlternate_Type()
)
gtmAttr2DefaultAlternate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2DefaultAlternate.setStatus("current")


class _GtmAttr2DefaultFallback_Type(Integer32):
    """Custom type gtmAttr2DefaultFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("bps", 15),
          ("cpu", 12),
          ("droppacket", 16),
          ("explicitip", 17),
          ("ga", 6),
          ("hitratio", 13),
          ("leastconn", 8),
          ("lowesthops", 10),
          ("lowestrtt", 9),
          ("null", 1),
          ("packetrate", 11),
          ("qos", 14),
          ("ratio", 3),
          ("returntodns", 0),
          ("roundrobin", 2),
          ("statpersit", 5),
          ("topology", 4),
          ("vscapacity", 7),
          ("vsscore", 18))
    )


_GtmAttr2DefaultFallback_Type.__name__ = "Integer32"
_GtmAttr2DefaultFallback_Object = MibTableColumn
gtmAttr2DefaultFallback = _GtmAttr2DefaultFallback_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 11),
    _GtmAttr2DefaultFallback_Type()
)
gtmAttr2DefaultFallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2DefaultFallback.setStatus("current")
_GtmAttr2PersistMask_Type = Integer32
_GtmAttr2PersistMask_Object = MibTableColumn
gtmAttr2PersistMask = _GtmAttr2PersistMask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 12),
    _GtmAttr2PersistMask_Type()
)
gtmAttr2PersistMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2PersistMask.setStatus("deprecated")


class _GtmAttr2GtmSetsRecursion_Type(Integer32):
    """Custom type gtmAttr2GtmSetsRecursion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttr2GtmSetsRecursion_Type.__name__ = "Integer32"
_GtmAttr2GtmSetsRecursion_Object = MibTableColumn
gtmAttr2GtmSetsRecursion = _GtmAttr2GtmSetsRecursion_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 13),
    _GtmAttr2GtmSetsRecursion_Type()
)
gtmAttr2GtmSetsRecursion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2GtmSetsRecursion.setStatus("current")
_GtmAttr2QosFactorLcs_Type = Integer32
_GtmAttr2QosFactorLcs_Object = MibTableColumn
gtmAttr2QosFactorLcs = _GtmAttr2QosFactorLcs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 14),
    _GtmAttr2QosFactorLcs_Type()
)
gtmAttr2QosFactorLcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2QosFactorLcs.setStatus("current")
_GtmAttr2QosFactorRtt_Type = Integer32
_GtmAttr2QosFactorRtt_Object = MibTableColumn
gtmAttr2QosFactorRtt = _GtmAttr2QosFactorRtt_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 15),
    _GtmAttr2QosFactorRtt_Type()
)
gtmAttr2QosFactorRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2QosFactorRtt.setStatus("current")
_GtmAttr2QosFactorHops_Type = Integer32
_GtmAttr2QosFactorHops_Object = MibTableColumn
gtmAttr2QosFactorHops = _GtmAttr2QosFactorHops_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 16),
    _GtmAttr2QosFactorHops_Type()
)
gtmAttr2QosFactorHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2QosFactorHops.setStatus("current")
_GtmAttr2QosFactorHitRatio_Type = Integer32
_GtmAttr2QosFactorHitRatio_Object = MibTableColumn
gtmAttr2QosFactorHitRatio = _GtmAttr2QosFactorHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 17),
    _GtmAttr2QosFactorHitRatio_Type()
)
gtmAttr2QosFactorHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2QosFactorHitRatio.setStatus("current")
_GtmAttr2QosFactorPacketRate_Type = Integer32
_GtmAttr2QosFactorPacketRate_Object = MibTableColumn
gtmAttr2QosFactorPacketRate = _GtmAttr2QosFactorPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 18),
    _GtmAttr2QosFactorPacketRate_Type()
)
gtmAttr2QosFactorPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2QosFactorPacketRate.setStatus("current")
_GtmAttr2QosFactorBps_Type = Integer32
_GtmAttr2QosFactorBps_Object = MibTableColumn
gtmAttr2QosFactorBps = _GtmAttr2QosFactorBps_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 19),
    _GtmAttr2QosFactorBps_Type()
)
gtmAttr2QosFactorBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2QosFactorBps.setStatus("current")
_GtmAttr2QosFactorVsCapacity_Type = Integer32
_GtmAttr2QosFactorVsCapacity_Object = MibTableColumn
gtmAttr2QosFactorVsCapacity = _GtmAttr2QosFactorVsCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 20),
    _GtmAttr2QosFactorVsCapacity_Type()
)
gtmAttr2QosFactorVsCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2QosFactorVsCapacity.setStatus("current")
_GtmAttr2QosFactorTopology_Type = Integer32
_GtmAttr2QosFactorTopology_Object = MibTableColumn
gtmAttr2QosFactorTopology = _GtmAttr2QosFactorTopology_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 21),
    _GtmAttr2QosFactorTopology_Type()
)
gtmAttr2QosFactorTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2QosFactorTopology.setStatus("current")
_GtmAttr2QosFactorConnRate_Type = Integer32
_GtmAttr2QosFactorConnRate_Object = MibTableColumn
gtmAttr2QosFactorConnRate = _GtmAttr2QosFactorConnRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 22),
    _GtmAttr2QosFactorConnRate_Type()
)
gtmAttr2QosFactorConnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2QosFactorConnRate.setStatus("deprecated")
_GtmAttr2TimerRetryPathData_Type = Integer32
_GtmAttr2TimerRetryPathData_Object = MibTableColumn
gtmAttr2TimerRetryPathData = _GtmAttr2TimerRetryPathData_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 23),
    _GtmAttr2TimerRetryPathData_Type()
)
gtmAttr2TimerRetryPathData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2TimerRetryPathData.setStatus("current")
_GtmAttr2TimerGetAutoconfigData_Type = Integer32
_GtmAttr2TimerGetAutoconfigData_Object = MibTableColumn
gtmAttr2TimerGetAutoconfigData = _GtmAttr2TimerGetAutoconfigData_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 24),
    _GtmAttr2TimerGetAutoconfigData_Type()
)
gtmAttr2TimerGetAutoconfigData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2TimerGetAutoconfigData.setStatus("current")
_GtmAttr2TimerPersistCache_Type = Integer32
_GtmAttr2TimerPersistCache_Object = MibTableColumn
gtmAttr2TimerPersistCache = _GtmAttr2TimerPersistCache_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 25),
    _GtmAttr2TimerPersistCache_Type()
)
gtmAttr2TimerPersistCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2TimerPersistCache.setStatus("current")
_GtmAttr2DefaultProbeLimit_Type = Integer32
_GtmAttr2DefaultProbeLimit_Object = MibTableColumn
gtmAttr2DefaultProbeLimit = _GtmAttr2DefaultProbeLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 26),
    _GtmAttr2DefaultProbeLimit_Type()
)
gtmAttr2DefaultProbeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2DefaultProbeLimit.setStatus("current")
_GtmAttr2DownThreshold_Type = Integer32
_GtmAttr2DownThreshold_Object = MibTableColumn
gtmAttr2DownThreshold = _GtmAttr2DownThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 27),
    _GtmAttr2DownThreshold_Type()
)
gtmAttr2DownThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2DownThreshold.setStatus("current")
_GtmAttr2DownMultiple_Type = Integer32
_GtmAttr2DownMultiple_Object = MibTableColumn
gtmAttr2DownMultiple = _GtmAttr2DownMultiple_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 28),
    _GtmAttr2DownMultiple_Type()
)
gtmAttr2DownMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2DownMultiple.setStatus("current")
_GtmAttr2PathTtl_Type = Integer32
_GtmAttr2PathTtl_Object = MibTableColumn
gtmAttr2PathTtl = _GtmAttr2PathTtl_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 29),
    _GtmAttr2PathTtl_Type()
)
gtmAttr2PathTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2PathTtl.setStatus("current")
_GtmAttr2TraceTtl_Type = Integer32
_GtmAttr2TraceTtl_Object = MibTableColumn
gtmAttr2TraceTtl = _GtmAttr2TraceTtl_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 30),
    _GtmAttr2TraceTtl_Type()
)
gtmAttr2TraceTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2TraceTtl.setStatus("current")
_GtmAttr2LdnsDuration_Type = Integer32
_GtmAttr2LdnsDuration_Object = MibTableColumn
gtmAttr2LdnsDuration = _GtmAttr2LdnsDuration_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 31),
    _GtmAttr2LdnsDuration_Type()
)
gtmAttr2LdnsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2LdnsDuration.setStatus("current")
_GtmAttr2PathDuration_Type = Integer32
_GtmAttr2PathDuration_Object = MibTableColumn
gtmAttr2PathDuration = _GtmAttr2PathDuration_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 32),
    _GtmAttr2PathDuration_Type()
)
gtmAttr2PathDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2PathDuration.setStatus("current")
_GtmAttr2RttSampleCount_Type = Integer32
_GtmAttr2RttSampleCount_Object = MibTableColumn
gtmAttr2RttSampleCount = _GtmAttr2RttSampleCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 33),
    _GtmAttr2RttSampleCount_Type()
)
gtmAttr2RttSampleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2RttSampleCount.setStatus("current")
_GtmAttr2RttPacketLength_Type = Integer32
_GtmAttr2RttPacketLength_Object = MibTableColumn
gtmAttr2RttPacketLength = _GtmAttr2RttPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 34),
    _GtmAttr2RttPacketLength_Type()
)
gtmAttr2RttPacketLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2RttPacketLength.setStatus("current")
_GtmAttr2RttTimeout_Type = Integer32
_GtmAttr2RttTimeout_Object = MibTableColumn
gtmAttr2RttTimeout = _GtmAttr2RttTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 35),
    _GtmAttr2RttTimeout_Type()
)
gtmAttr2RttTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2RttTimeout.setStatus("current")
_GtmAttr2MaxMonReqs_Type = Integer32
_GtmAttr2MaxMonReqs_Object = MibTableColumn
gtmAttr2MaxMonReqs = _GtmAttr2MaxMonReqs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 36),
    _GtmAttr2MaxMonReqs_Type()
)
gtmAttr2MaxMonReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2MaxMonReqs.setStatus("current")
_GtmAttr2TraceroutePort_Type = Integer32
_GtmAttr2TraceroutePort_Object = MibTableColumn
gtmAttr2TraceroutePort = _GtmAttr2TraceroutePort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 37),
    _GtmAttr2TraceroutePort_Type()
)
gtmAttr2TraceroutePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2TraceroutePort.setStatus("current")


class _GtmAttr2PathsNeverDie_Type(Integer32):
    """Custom type gtmAttr2PathsNeverDie based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttr2PathsNeverDie_Type.__name__ = "Integer32"
_GtmAttr2PathsNeverDie_Object = MibTableColumn
gtmAttr2PathsNeverDie = _GtmAttr2PathsNeverDie_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 38),
    _GtmAttr2PathsNeverDie_Type()
)
gtmAttr2PathsNeverDie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2PathsNeverDie.setStatus("current")


class _GtmAttr2ProbeDisabledObjects_Type(Integer32):
    """Custom type gtmAttr2ProbeDisabledObjects based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttr2ProbeDisabledObjects_Type.__name__ = "Integer32"
_GtmAttr2ProbeDisabledObjects_Object = MibTableColumn
gtmAttr2ProbeDisabledObjects = _GtmAttr2ProbeDisabledObjects_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 39),
    _GtmAttr2ProbeDisabledObjects_Type()
)
gtmAttr2ProbeDisabledObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2ProbeDisabledObjects.setStatus("current")
_GtmAttr2LinkLimitFactor_Type = Integer32
_GtmAttr2LinkLimitFactor_Object = MibTableColumn
gtmAttr2LinkLimitFactor = _GtmAttr2LinkLimitFactor_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 40),
    _GtmAttr2LinkLimitFactor_Type()
)
gtmAttr2LinkLimitFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2LinkLimitFactor.setStatus("current")
_GtmAttr2OverLimitLinkLimitFactor_Type = Integer32
_GtmAttr2OverLimitLinkLimitFactor_Object = MibTableColumn
gtmAttr2OverLimitLinkLimitFactor = _GtmAttr2OverLimitLinkLimitFactor_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 41),
    _GtmAttr2OverLimitLinkLimitFactor_Type()
)
gtmAttr2OverLimitLinkLimitFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2OverLimitLinkLimitFactor.setStatus("current")
_GtmAttr2LinkPrepaidFactor_Type = Integer32
_GtmAttr2LinkPrepaidFactor_Object = MibTableColumn
gtmAttr2LinkPrepaidFactor = _GtmAttr2LinkPrepaidFactor_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 42),
    _GtmAttr2LinkPrepaidFactor_Type()
)
gtmAttr2LinkPrepaidFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2LinkPrepaidFactor.setStatus("current")
_GtmAttr2LinkCompensateInbound_Type = Integer32
_GtmAttr2LinkCompensateInbound_Object = MibTableColumn
gtmAttr2LinkCompensateInbound = _GtmAttr2LinkCompensateInbound_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 43),
    _GtmAttr2LinkCompensateInbound_Type()
)
gtmAttr2LinkCompensateInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2LinkCompensateInbound.setStatus("current")
_GtmAttr2LinkCompensateOutbound_Type = Integer32
_GtmAttr2LinkCompensateOutbound_Object = MibTableColumn
gtmAttr2LinkCompensateOutbound = _GtmAttr2LinkCompensateOutbound_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 44),
    _GtmAttr2LinkCompensateOutbound_Type()
)
gtmAttr2LinkCompensateOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2LinkCompensateOutbound.setStatus("current")
_GtmAttr2LinkCompensationHistory_Type = Integer32
_GtmAttr2LinkCompensationHistory_Object = MibTableColumn
gtmAttr2LinkCompensationHistory = _GtmAttr2LinkCompensationHistory_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 45),
    _GtmAttr2LinkCompensationHistory_Type()
)
gtmAttr2LinkCompensationHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2LinkCompensationHistory.setStatus("current")
_GtmAttr2MaxLinkOverLimitCount_Type = Integer32
_GtmAttr2MaxLinkOverLimitCount_Object = MibTableColumn
gtmAttr2MaxLinkOverLimitCount = _GtmAttr2MaxLinkOverLimitCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 46),
    _GtmAttr2MaxLinkOverLimitCount_Type()
)
gtmAttr2MaxLinkOverLimitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2MaxLinkOverLimitCount.setStatus("current")
_GtmAttr2LowerBoundPctRow_Type = Integer32
_GtmAttr2LowerBoundPctRow_Object = MibTableColumn
gtmAttr2LowerBoundPctRow = _GtmAttr2LowerBoundPctRow_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 47),
    _GtmAttr2LowerBoundPctRow_Type()
)
gtmAttr2LowerBoundPctRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2LowerBoundPctRow.setStatus("deprecated")
_GtmAttr2LowerBoundPctCol_Type = Integer32
_GtmAttr2LowerBoundPctCol_Object = MibTableColumn
gtmAttr2LowerBoundPctCol = _GtmAttr2LowerBoundPctCol_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 48),
    _GtmAttr2LowerBoundPctCol_Type()
)
gtmAttr2LowerBoundPctCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2LowerBoundPctCol.setStatus("deprecated")


class _GtmAttr2Autoconf_Type(Integer32):
    """Custom type gtmAttr2Autoconf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttr2Autoconf_Type.__name__ = "Integer32"
_GtmAttr2Autoconf_Object = MibTableColumn
gtmAttr2Autoconf = _GtmAttr2Autoconf_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 49),
    _GtmAttr2Autoconf_Type()
)
gtmAttr2Autoconf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2Autoconf.setStatus("current")


class _GtmAttr2Autosync_Type(Integer32):
    """Custom type gtmAttr2Autosync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttr2Autosync_Type.__name__ = "Integer32"
_GtmAttr2Autosync_Object = MibTableColumn
gtmAttr2Autosync = _GtmAttr2Autosync_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 50),
    _GtmAttr2Autosync_Type()
)
gtmAttr2Autosync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2Autosync.setStatus("current")


class _GtmAttr2SyncNamedConf_Type(Integer32):
    """Custom type gtmAttr2SyncNamedConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttr2SyncNamedConf_Type.__name__ = "Integer32"
_GtmAttr2SyncNamedConf_Object = MibTableColumn
gtmAttr2SyncNamedConf = _GtmAttr2SyncNamedConf_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 51),
    _GtmAttr2SyncNamedConf_Type()
)
gtmAttr2SyncNamedConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2SyncNamedConf.setStatus("current")
_GtmAttr2SyncGroup_Type = LongDisplayString
_GtmAttr2SyncGroup_Object = MibTableColumn
gtmAttr2SyncGroup = _GtmAttr2SyncGroup_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 52),
    _GtmAttr2SyncGroup_Type()
)
gtmAttr2SyncGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2SyncGroup.setStatus("current")
_GtmAttr2SyncTimeout_Type = Integer32
_GtmAttr2SyncTimeout_Object = MibTableColumn
gtmAttr2SyncTimeout = _GtmAttr2SyncTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 53),
    _GtmAttr2SyncTimeout_Type()
)
gtmAttr2SyncTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2SyncTimeout.setStatus("current")
_GtmAttr2SyncZonesTimeout_Type = Integer32
_GtmAttr2SyncZonesTimeout_Object = MibTableColumn
gtmAttr2SyncZonesTimeout = _GtmAttr2SyncZonesTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 54),
    _GtmAttr2SyncZonesTimeout_Type()
)
gtmAttr2SyncZonesTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2SyncZonesTimeout.setStatus("current")
_GtmAttr2TimeTolerance_Type = Integer32
_GtmAttr2TimeTolerance_Object = MibTableColumn
gtmAttr2TimeTolerance = _GtmAttr2TimeTolerance_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 55),
    _GtmAttr2TimeTolerance_Type()
)
gtmAttr2TimeTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2TimeTolerance.setStatus("current")


class _GtmAttr2TopologyLongestMatch_Type(Integer32):
    """Custom type gtmAttr2TopologyLongestMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAttr2TopologyLongestMatch_Type.__name__ = "Integer32"
_GtmAttr2TopologyLongestMatch_Object = MibTableColumn
gtmAttr2TopologyLongestMatch = _GtmAttr2TopologyLongestMatch_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 56),
    _GtmAttr2TopologyLongestMatch_Type()
)
gtmAttr2TopologyLongestMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2TopologyLongestMatch.setStatus("current")
_GtmAttr2TopologyAclThreshold_Type = Integer32
_GtmAttr2TopologyAclThreshold_Object = MibTableColumn
gtmAttr2TopologyAclThreshold = _GtmAttr2TopologyAclThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 57),
    _GtmAttr2TopologyAclThreshold_Type()
)
gtmAttr2TopologyAclThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2TopologyAclThreshold.setStatus("deprecated")
_GtmAttr2StaticPersistCidr_Type = Integer32
_GtmAttr2StaticPersistCidr_Object = MibTableColumn
gtmAttr2StaticPersistCidr = _GtmAttr2StaticPersistCidr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 58),
    _GtmAttr2StaticPersistCidr_Type()
)
gtmAttr2StaticPersistCidr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2StaticPersistCidr.setStatus("current")
_GtmAttr2StaticPersistV6Cidr_Type = Integer32
_GtmAttr2StaticPersistV6Cidr_Object = MibTableColumn
gtmAttr2StaticPersistV6Cidr = _GtmAttr2StaticPersistV6Cidr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 59),
    _GtmAttr2StaticPersistV6Cidr_Type()
)
gtmAttr2StaticPersistV6Cidr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2StaticPersistV6Cidr.setStatus("current")
_GtmAttr2QosFactorVsScore_Type = Integer32
_GtmAttr2QosFactorVsScore_Object = MibTableColumn
gtmAttr2QosFactorVsScore = _GtmAttr2QosFactorVsScore_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 60),
    _GtmAttr2QosFactorVsScore_Type()
)
gtmAttr2QosFactorVsScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2QosFactorVsScore.setStatus("current")
_GtmAttr2TimerSendKeepAlive_Type = Integer32
_GtmAttr2TimerSendKeepAlive_Object = MibTableColumn
gtmAttr2TimerSendKeepAlive = _GtmAttr2TimerSendKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 61),
    _GtmAttr2TimerSendKeepAlive_Type()
)
gtmAttr2TimerSendKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2TimerSendKeepAlive.setStatus("current")
_GtmAttr2CertificateDepth_Type = Integer32
_GtmAttr2CertificateDepth_Object = MibTableColumn
gtmAttr2CertificateDepth = _GtmAttr2CertificateDepth_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 62),
    _GtmAttr2CertificateDepth_Type()
)
gtmAttr2CertificateDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2CertificateDepth.setStatus("deprecated")
_GtmAttr2MaxMemoryUsage_Type = Integer32
_GtmAttr2MaxMemoryUsage_Object = MibTableColumn
gtmAttr2MaxMemoryUsage = _GtmAttr2MaxMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 63),
    _GtmAttr2MaxMemoryUsage_Type()
)
gtmAttr2MaxMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2MaxMemoryUsage.setStatus("deprecated")
_GtmAttr2Name_Type = LongDisplayString
_GtmAttr2Name_Object = MibTableColumn
gtmAttr2Name = _GtmAttr2Name_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 64),
    _GtmAttr2Name_Type()
)
gtmAttr2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2Name.setStatus("current")


class _GtmAttr2ForwardStatus_Type(Integer32):
    """Custom type gtmAttr2ForwardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GtmAttr2ForwardStatus_Type.__name__ = "Integer32"
_GtmAttr2ForwardStatus_Object = MibTableColumn
gtmAttr2ForwardStatus = _GtmAttr2ForwardStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 1, 3, 2, 1, 65),
    _GtmAttr2ForwardStatus_Type()
)
gtmAttr2ForwardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAttr2ForwardStatus.setStatus("current")
_GtmGlobalStats_ObjectIdentity = ObjectIdentity
gtmGlobalStats = _GtmGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2)
)
_GtmGlobalStat_ObjectIdentity = ObjectIdentity
gtmGlobalStat = _GtmGlobalStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1)
)
_GtmStatResetStats_Type = Integer32
_GtmStatResetStats_Object = MibScalar
gtmStatResetStats = _GtmStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 1),
    _GtmStatResetStats_Type()
)
gtmStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtmStatResetStats.setStatus("current")
_GtmStatRequests_Type = Counter64
_GtmStatRequests_Object = MibScalar
gtmStatRequests = _GtmStatRequests_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 2),
    _GtmStatRequests_Type()
)
gtmStatRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatRequests.setStatus("current")
_GtmStatResolutions_Type = Counter64
_GtmStatResolutions_Object = MibScalar
gtmStatResolutions = _GtmStatResolutions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 3),
    _GtmStatResolutions_Type()
)
gtmStatResolutions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatResolutions.setStatus("current")
_GtmStatPersisted_Type = Counter64
_GtmStatPersisted_Object = MibScalar
gtmStatPersisted = _GtmStatPersisted_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 4),
    _GtmStatPersisted_Type()
)
gtmStatPersisted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatPersisted.setStatus("current")
_GtmStatPreferred_Type = Counter64
_GtmStatPreferred_Object = MibScalar
gtmStatPreferred = _GtmStatPreferred_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 5),
    _GtmStatPreferred_Type()
)
gtmStatPreferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatPreferred.setStatus("current")
_GtmStatAlternate_Type = Counter64
_GtmStatAlternate_Object = MibScalar
gtmStatAlternate = _GtmStatAlternate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 6),
    _GtmStatAlternate_Type()
)
gtmStatAlternate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatAlternate.setStatus("current")
_GtmStatFallback_Type = Counter64
_GtmStatFallback_Object = MibScalar
gtmStatFallback = _GtmStatFallback_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 7),
    _GtmStatFallback_Type()
)
gtmStatFallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatFallback.setStatus("current")
_GtmStatDropped_Type = Counter64
_GtmStatDropped_Object = MibScalar
gtmStatDropped = _GtmStatDropped_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 8),
    _GtmStatDropped_Type()
)
gtmStatDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatDropped.setStatus("current")
_GtmStatExplicitIp_Type = Counter64
_GtmStatExplicitIp_Object = MibScalar
gtmStatExplicitIp = _GtmStatExplicitIp_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 9),
    _GtmStatExplicitIp_Type()
)
gtmStatExplicitIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatExplicitIp.setStatus("deprecated")
_GtmStatReturnToDns_Type = Counter64
_GtmStatReturnToDns_Object = MibScalar
gtmStatReturnToDns = _GtmStatReturnToDns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 10),
    _GtmStatReturnToDns_Type()
)
gtmStatReturnToDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatReturnToDns.setStatus("current")
_GtmStatReconnects_Type = Counter64
_GtmStatReconnects_Object = MibScalar
gtmStatReconnects = _GtmStatReconnects_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 11),
    _GtmStatReconnects_Type()
)
gtmStatReconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatReconnects.setStatus("current")
_GtmStatBytesReceived_Type = Counter64
_GtmStatBytesReceived_Object = MibScalar
gtmStatBytesReceived = _GtmStatBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 12),
    _GtmStatBytesReceived_Type()
)
gtmStatBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatBytesReceived.setStatus("current")
_GtmStatBytesSent_Type = Counter64
_GtmStatBytesSent_Object = MibScalar
gtmStatBytesSent = _GtmStatBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 13),
    _GtmStatBytesSent_Type()
)
gtmStatBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatBytesSent.setStatus("current")
_GtmStatNumBacklogged_Type = Counter64
_GtmStatNumBacklogged_Object = MibScalar
gtmStatNumBacklogged = _GtmStatNumBacklogged_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 14),
    _GtmStatNumBacklogged_Type()
)
gtmStatNumBacklogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatNumBacklogged.setStatus("current")
_GtmStatBytesDropped_Type = Counter64
_GtmStatBytesDropped_Object = MibScalar
gtmStatBytesDropped = _GtmStatBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 15),
    _GtmStatBytesDropped_Type()
)
gtmStatBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatBytesDropped.setStatus("current")
_GtmStatLdnses_Type = Gauge32
_GtmStatLdnses_Object = MibScalar
gtmStatLdnses = _GtmStatLdnses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 16),
    _GtmStatLdnses_Type()
)
gtmStatLdnses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatLdnses.setStatus("current")
_GtmStatPaths_Type = Gauge32
_GtmStatPaths_Object = MibScalar
gtmStatPaths = _GtmStatPaths_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 17),
    _GtmStatPaths_Type()
)
gtmStatPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatPaths.setStatus("current")
_GtmStatReturnFromDns_Type = Counter64
_GtmStatReturnFromDns_Object = MibScalar
gtmStatReturnFromDns = _GtmStatReturnFromDns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 18),
    _GtmStatReturnFromDns_Type()
)
gtmStatReturnFromDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatReturnFromDns.setStatus("current")
_GtmStatCnameResolutions_Type = Counter64
_GtmStatCnameResolutions_Object = MibScalar
gtmStatCnameResolutions = _GtmStatCnameResolutions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 19),
    _GtmStatCnameResolutions_Type()
)
gtmStatCnameResolutions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatCnameResolutions.setStatus("current")
_GtmStatARequests_Type = Counter64
_GtmStatARequests_Object = MibScalar
gtmStatARequests = _GtmStatARequests_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 20),
    _GtmStatARequests_Type()
)
gtmStatARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatARequests.setStatus("current")
_GtmStatAaaaRequests_Type = Counter64
_GtmStatAaaaRequests_Object = MibScalar
gtmStatAaaaRequests = _GtmStatAaaaRequests_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 1, 21),
    _GtmStatAaaaRequests_Type()
)
gtmStatAaaaRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmStatAaaaRequests.setStatus("current")
_GtmGlobalDnssecStat_ObjectIdentity = ObjectIdentity
gtmGlobalDnssecStat = _GtmGlobalDnssecStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2)
)
_GtmDnssecStatResetStats_Type = Integer32
_GtmDnssecStatResetStats_Object = MibScalar
gtmDnssecStatResetStats = _GtmDnssecStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 1),
    _GtmDnssecStatResetStats_Type()
)
gtmDnssecStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtmDnssecStatResetStats.setStatus("current")
_GtmDnssecStatNsec3s_Type = Counter64
_GtmDnssecStatNsec3s_Object = MibScalar
gtmDnssecStatNsec3s = _GtmDnssecStatNsec3s_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 2),
    _GtmDnssecStatNsec3s_Type()
)
gtmDnssecStatNsec3s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatNsec3s.setStatus("current")
_GtmDnssecStatNsec3Nodata_Type = Counter64
_GtmDnssecStatNsec3Nodata_Object = MibScalar
gtmDnssecStatNsec3Nodata = _GtmDnssecStatNsec3Nodata_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 3),
    _GtmDnssecStatNsec3Nodata_Type()
)
gtmDnssecStatNsec3Nodata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatNsec3Nodata.setStatus("current")
_GtmDnssecStatNsec3Nxdomain_Type = Counter64
_GtmDnssecStatNsec3Nxdomain_Object = MibScalar
gtmDnssecStatNsec3Nxdomain = _GtmDnssecStatNsec3Nxdomain_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 4),
    _GtmDnssecStatNsec3Nxdomain_Type()
)
gtmDnssecStatNsec3Nxdomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatNsec3Nxdomain.setStatus("current")
_GtmDnssecStatNsec3Referral_Type = Counter64
_GtmDnssecStatNsec3Referral_Object = MibScalar
gtmDnssecStatNsec3Referral = _GtmDnssecStatNsec3Referral_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 5),
    _GtmDnssecStatNsec3Referral_Type()
)
gtmDnssecStatNsec3Referral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatNsec3Referral.setStatus("current")
_GtmDnssecStatNsec3Resalt_Type = Counter64
_GtmDnssecStatNsec3Resalt_Object = MibScalar
gtmDnssecStatNsec3Resalt = _GtmDnssecStatNsec3Resalt_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 6),
    _GtmDnssecStatNsec3Resalt_Type()
)
gtmDnssecStatNsec3Resalt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatNsec3Resalt.setStatus("current")
_GtmDnssecStatDnssecResponses_Type = Counter64
_GtmDnssecStatDnssecResponses_Object = MibScalar
gtmDnssecStatDnssecResponses = _GtmDnssecStatDnssecResponses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 7),
    _GtmDnssecStatDnssecResponses_Type()
)
gtmDnssecStatDnssecResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatDnssecResponses.setStatus("current")
_GtmDnssecStatDnssecDnskeyQueries_Type = Counter64
_GtmDnssecStatDnssecDnskeyQueries_Object = MibScalar
gtmDnssecStatDnssecDnskeyQueries = _GtmDnssecStatDnssecDnskeyQueries_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 8),
    _GtmDnssecStatDnssecDnskeyQueries_Type()
)
gtmDnssecStatDnssecDnskeyQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatDnssecDnskeyQueries.setStatus("current")
_GtmDnssecStatDnssecNsec3paramQueries_Type = Counter64
_GtmDnssecStatDnssecNsec3paramQueries_Object = MibScalar
gtmDnssecStatDnssecNsec3paramQueries = _GtmDnssecStatDnssecNsec3paramQueries_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 9),
    _GtmDnssecStatDnssecNsec3paramQueries_Type()
)
gtmDnssecStatDnssecNsec3paramQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatDnssecNsec3paramQueries.setStatus("current")
_GtmDnssecStatDnssecDsQueries_Type = Counter64
_GtmDnssecStatDnssecDsQueries_Object = MibScalar
gtmDnssecStatDnssecDsQueries = _GtmDnssecStatDnssecDsQueries_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 10),
    _GtmDnssecStatDnssecDsQueries_Type()
)
gtmDnssecStatDnssecDsQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatDnssecDsQueries.setStatus("current")
_GtmDnssecStatSigCryptoFailed_Type = Counter64
_GtmDnssecStatSigCryptoFailed_Object = MibScalar
gtmDnssecStatSigCryptoFailed = _GtmDnssecStatSigCryptoFailed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 11),
    _GtmDnssecStatSigCryptoFailed_Type()
)
gtmDnssecStatSigCryptoFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatSigCryptoFailed.setStatus("current")
_GtmDnssecStatSigSuccess_Type = Counter64
_GtmDnssecStatSigSuccess_Object = MibScalar
gtmDnssecStatSigSuccess = _GtmDnssecStatSigSuccess_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 12),
    _GtmDnssecStatSigSuccess_Type()
)
gtmDnssecStatSigSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatSigSuccess.setStatus("current")
_GtmDnssecStatSigFailed_Type = Counter64
_GtmDnssecStatSigFailed_Object = MibScalar
gtmDnssecStatSigFailed = _GtmDnssecStatSigFailed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 13),
    _GtmDnssecStatSigFailed_Type()
)
gtmDnssecStatSigFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatSigFailed.setStatus("current")
_GtmDnssecStatSigRrsetFailed_Type = Counter64
_GtmDnssecStatSigRrsetFailed_Object = MibScalar
gtmDnssecStatSigRrsetFailed = _GtmDnssecStatSigRrsetFailed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 14),
    _GtmDnssecStatSigRrsetFailed_Type()
)
gtmDnssecStatSigRrsetFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatSigRrsetFailed.setStatus("current")
_GtmDnssecStatConnectFlowFailed_Type = Counter64
_GtmDnssecStatConnectFlowFailed_Object = MibScalar
gtmDnssecStatConnectFlowFailed = _GtmDnssecStatConnectFlowFailed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 15),
    _GtmDnssecStatConnectFlowFailed_Type()
)
gtmDnssecStatConnectFlowFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatConnectFlowFailed.setStatus("current")
_GtmDnssecStatTowireFailed_Type = Counter64
_GtmDnssecStatTowireFailed_Object = MibScalar
gtmDnssecStatTowireFailed = _GtmDnssecStatTowireFailed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 16),
    _GtmDnssecStatTowireFailed_Type()
)
gtmDnssecStatTowireFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatTowireFailed.setStatus("current")
_GtmDnssecStatAxfrQueries_Type = Counter64
_GtmDnssecStatAxfrQueries_Object = MibScalar
gtmDnssecStatAxfrQueries = _GtmDnssecStatAxfrQueries_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 17),
    _GtmDnssecStatAxfrQueries_Type()
)
gtmDnssecStatAxfrQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatAxfrQueries.setStatus("current")
_GtmDnssecStatIxfrQueries_Type = Counter64
_GtmDnssecStatIxfrQueries_Object = MibScalar
gtmDnssecStatIxfrQueries = _GtmDnssecStatIxfrQueries_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 18),
    _GtmDnssecStatIxfrQueries_Type()
)
gtmDnssecStatIxfrQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatIxfrQueries.setStatus("current")
_GtmDnssecStatXfrStarts_Type = Counter64
_GtmDnssecStatXfrStarts_Object = MibScalar
gtmDnssecStatXfrStarts = _GtmDnssecStatXfrStarts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 19),
    _GtmDnssecStatXfrStarts_Type()
)
gtmDnssecStatXfrStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatXfrStarts.setStatus("current")
_GtmDnssecStatXfrCompletes_Type = Counter64
_GtmDnssecStatXfrCompletes_Object = MibScalar
gtmDnssecStatXfrCompletes = _GtmDnssecStatXfrCompletes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 20),
    _GtmDnssecStatXfrCompletes_Type()
)
gtmDnssecStatXfrCompletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatXfrCompletes.setStatus("current")
_GtmDnssecStatXfrMsgs_Type = Counter64
_GtmDnssecStatXfrMsgs_Object = MibScalar
gtmDnssecStatXfrMsgs = _GtmDnssecStatXfrMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 21),
    _GtmDnssecStatXfrMsgs_Type()
)
gtmDnssecStatXfrMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatXfrMsgs.setStatus("current")
_GtmDnssecStatXfrMasterMsgs_Type = Counter64
_GtmDnssecStatXfrMasterMsgs_Object = MibScalar
gtmDnssecStatXfrMasterMsgs = _GtmDnssecStatXfrMasterMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 22),
    _GtmDnssecStatXfrMasterMsgs_Type()
)
gtmDnssecStatXfrMasterMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatXfrMasterMsgs.setStatus("current")
_GtmDnssecStatXfrResponseAverageSize_Type = Counter64
_GtmDnssecStatXfrResponseAverageSize_Object = MibScalar
gtmDnssecStatXfrResponseAverageSize = _GtmDnssecStatXfrResponseAverageSize_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 23),
    _GtmDnssecStatXfrResponseAverageSize_Type()
)
gtmDnssecStatXfrResponseAverageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatXfrResponseAverageSize.setStatus("current")
_GtmDnssecStatXfrSerial_Type = Counter64
_GtmDnssecStatXfrSerial_Object = MibScalar
gtmDnssecStatXfrSerial = _GtmDnssecStatXfrSerial_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 24),
    _GtmDnssecStatXfrSerial_Type()
)
gtmDnssecStatXfrSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatXfrSerial.setStatus("current")
_GtmDnssecStatXfrMasterSerial_Type = Counter64
_GtmDnssecStatXfrMasterSerial_Object = MibScalar
gtmDnssecStatXfrMasterSerial = _GtmDnssecStatXfrMasterSerial_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 1, 2, 2, 25),
    _GtmDnssecStatXfrMasterSerial_Type()
)
gtmDnssecStatXfrMasterSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecStatXfrMasterSerial.setStatus("current")
_GtmApplications_ObjectIdentity = ObjectIdentity
gtmApplications = _GtmApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2)
)
_GtmApplication_ObjectIdentity = ObjectIdentity
gtmApplication = _GtmApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 1)
)
_GtmAppNumber_Type = Integer32
_GtmAppNumber_Object = MibScalar
gtmAppNumber = _GtmAppNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 1, 1),
    _GtmAppNumber_Type()
)
gtmAppNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppNumber.setStatus("current")
_GtmAppTable_Object = MibTable
gtmAppTable = _GtmAppTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    gtmAppTable.setStatus("current")
_GtmAppEntry_Object = MibTableRow
gtmAppEntry = _GtmAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 1, 2, 1)
)
gtmAppEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmAppName"),
)
if mibBuilder.loadTexts:
    gtmAppEntry.setStatus("current")
_GtmAppName_Type = LongDisplayString
_GtmAppName_Object = MibTableColumn
gtmAppName = _GtmAppName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 1, 2, 1, 1),
    _GtmAppName_Type()
)
gtmAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppName.setStatus("current")


class _GtmAppPersist_Type(Integer32):
    """Custom type gtmAppPersist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmAppPersist_Type.__name__ = "Integer32"
_GtmAppPersist_Object = MibTableColumn
gtmAppPersist = _GtmAppPersist_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 1, 2, 1, 2),
    _GtmAppPersist_Type()
)
gtmAppPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppPersist.setStatus("current")
_GtmAppTtlPersist_Type = Integer32
_GtmAppTtlPersist_Object = MibTableColumn
gtmAppTtlPersist = _GtmAppTtlPersist_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 1, 2, 1, 3),
    _GtmAppTtlPersist_Type()
)
gtmAppTtlPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppTtlPersist.setStatus("current")


class _GtmAppAvailability_Type(Integer32):
    """Custom type gtmAppAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("datacenter", 3),
          ("link", 2),
          ("none", 0),
          ("server", 1))
    )


_GtmAppAvailability_Type.__name__ = "Integer32"
_GtmAppAvailability_Object = MibTableColumn
gtmAppAvailability = _GtmAppAvailability_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 1, 2, 1, 4),
    _GtmAppAvailability_Type()
)
gtmAppAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppAvailability.setStatus("current")
_GtmApplicationStatus_ObjectIdentity = ObjectIdentity
gtmApplicationStatus = _GtmApplicationStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 2)
)
_GtmAppStatusNumber_Type = Integer32
_GtmAppStatusNumber_Object = MibScalar
gtmAppStatusNumber = _GtmAppStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 2, 1),
    _GtmAppStatusNumber_Type()
)
gtmAppStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppStatusNumber.setStatus("current")
_GtmAppStatusTable_Object = MibTable
gtmAppStatusTable = _GtmAppStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    gtmAppStatusTable.setStatus("current")
_GtmAppStatusEntry_Object = MibTableRow
gtmAppStatusEntry = _GtmAppStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 2, 2, 1)
)
gtmAppStatusEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmAppStatusName"),
)
if mibBuilder.loadTexts:
    gtmAppStatusEntry.setStatus("current")
_GtmAppStatusName_Type = LongDisplayString
_GtmAppStatusName_Object = MibTableColumn
gtmAppStatusName = _GtmAppStatusName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 2, 2, 1, 1),
    _GtmAppStatusName_Type()
)
gtmAppStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppStatusName.setStatus("current")


class _GtmAppStatusAvailState_Type(Integer32):
    """Custom type gtmAppStatusAvailState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blue", 4),
          ("gray", 5),
          ("green", 1),
          ("none", 0),
          ("red", 3),
          ("yellow", 2))
    )


_GtmAppStatusAvailState_Type.__name__ = "Integer32"
_GtmAppStatusAvailState_Object = MibTableColumn
gtmAppStatusAvailState = _GtmAppStatusAvailState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 2, 2, 1, 2),
    _GtmAppStatusAvailState_Type()
)
gtmAppStatusAvailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppStatusAvailState.setStatus("current")


class _GtmAppStatusEnabledState_Type(Integer32):
    """Custom type gtmAppStatusEnabledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("disabledbyparent", 3),
          ("enabled", 1),
          ("none", 0))
    )


_GtmAppStatusEnabledState_Type.__name__ = "Integer32"
_GtmAppStatusEnabledState_Object = MibTableColumn
gtmAppStatusEnabledState = _GtmAppStatusEnabledState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 2, 2, 1, 3),
    _GtmAppStatusEnabledState_Type()
)
gtmAppStatusEnabledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppStatusEnabledState.setStatus("current")
_GtmAppStatusParentType_Type = Integer32
_GtmAppStatusParentType_Object = MibTableColumn
gtmAppStatusParentType = _GtmAppStatusParentType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 2, 2, 1, 4),
    _GtmAppStatusParentType_Type()
)
gtmAppStatusParentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppStatusParentType.setStatus("deprecated")
_GtmAppStatusDetailReason_Type = LongDisplayString
_GtmAppStatusDetailReason_Object = MibTableColumn
gtmAppStatusDetailReason = _GtmAppStatusDetailReason_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 2, 2, 1, 5),
    _GtmAppStatusDetailReason_Type()
)
gtmAppStatusDetailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppStatusDetailReason.setStatus("current")
_GtmAppContextStat_ObjectIdentity = ObjectIdentity
gtmAppContextStat = _GtmAppContextStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 3)
)
_GtmAppContStatNumber_Type = Integer32
_GtmAppContStatNumber_Object = MibScalar
gtmAppContStatNumber = _GtmAppContStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 3, 1),
    _GtmAppContStatNumber_Type()
)
gtmAppContStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppContStatNumber.setStatus("current")
_GtmAppContStatTable_Object = MibTable
gtmAppContStatTable = _GtmAppContStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    gtmAppContStatTable.setStatus("current")
_GtmAppContStatEntry_Object = MibTableRow
gtmAppContStatEntry = _GtmAppContStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 3, 2, 1)
)
gtmAppContStatEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmAppContStatAppName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmAppContStatType"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmAppContStatName"),
)
if mibBuilder.loadTexts:
    gtmAppContStatEntry.setStatus("current")
_GtmAppContStatAppName_Type = LongDisplayString
_GtmAppContStatAppName_Object = MibTableColumn
gtmAppContStatAppName = _GtmAppContStatAppName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 3, 2, 1, 1),
    _GtmAppContStatAppName_Type()
)
gtmAppContStatAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppContStatAppName.setStatus("current")


class _GtmAppContStatType_Type(Integer32):
    """Custom type gtmAppContStatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("datacenter", 0),
          ("link", 2),
          ("server", 1))
    )


_GtmAppContStatType_Type.__name__ = "Integer32"
_GtmAppContStatType_Object = MibTableColumn
gtmAppContStatType = _GtmAppContStatType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 3, 2, 1, 2),
    _GtmAppContStatType_Type()
)
gtmAppContStatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppContStatType.setStatus("current")
_GtmAppContStatName_Type = LongDisplayString
_GtmAppContStatName_Object = MibTableColumn
gtmAppContStatName = _GtmAppContStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 3, 2, 1, 3),
    _GtmAppContStatName_Type()
)
gtmAppContStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppContStatName.setStatus("current")
_GtmAppContStatNumAvail_Type = Counter64
_GtmAppContStatNumAvail_Object = MibTableColumn
gtmAppContStatNumAvail = _GtmAppContStatNumAvail_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 3, 2, 1, 4),
    _GtmAppContStatNumAvail_Type()
)
gtmAppContStatNumAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppContStatNumAvail.setStatus("current")


class _GtmAppContStatAvailState_Type(Integer32):
    """Custom type gtmAppContStatAvailState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blue", 4),
          ("gray", 5),
          ("green", 1),
          ("none", 0),
          ("red", 3),
          ("yellow", 2))
    )


_GtmAppContStatAvailState_Type.__name__ = "Integer32"
_GtmAppContStatAvailState_Object = MibTableColumn
gtmAppContStatAvailState = _GtmAppContStatAvailState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 3, 2, 1, 5),
    _GtmAppContStatAvailState_Type()
)
gtmAppContStatAvailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppContStatAvailState.setStatus("current")


class _GtmAppContStatEnabledState_Type(Integer32):
    """Custom type gtmAppContStatEnabledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("disabledbyparent", 3),
          ("enabled", 1),
          ("none", 0))
    )


_GtmAppContStatEnabledState_Type.__name__ = "Integer32"
_GtmAppContStatEnabledState_Object = MibTableColumn
gtmAppContStatEnabledState = _GtmAppContStatEnabledState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 3, 2, 1, 6),
    _GtmAppContStatEnabledState_Type()
)
gtmAppContStatEnabledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppContStatEnabledState.setStatus("current")
_GtmAppContStatParentType_Type = Integer32
_GtmAppContStatParentType_Object = MibTableColumn
gtmAppContStatParentType = _GtmAppContStatParentType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 3, 2, 1, 7),
    _GtmAppContStatParentType_Type()
)
gtmAppContStatParentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppContStatParentType.setStatus("deprecated")
_GtmAppContStatDetailReason_Type = LongDisplayString
_GtmAppContStatDetailReason_Object = MibTableColumn
gtmAppContStatDetailReason = _GtmAppContStatDetailReason_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 3, 2, 1, 8),
    _GtmAppContStatDetailReason_Type()
)
gtmAppContStatDetailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppContStatDetailReason.setStatus("current")
_GtmAppContextDisable_ObjectIdentity = ObjectIdentity
gtmAppContextDisable = _GtmAppContextDisable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 4)
)
_GtmAppContDisNumber_Type = Integer32
_GtmAppContDisNumber_Object = MibScalar
gtmAppContDisNumber = _GtmAppContDisNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 4, 1),
    _GtmAppContDisNumber_Type()
)
gtmAppContDisNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppContDisNumber.setStatus("current")
_GtmAppContDisTable_Object = MibTable
gtmAppContDisTable = _GtmAppContDisTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 4, 2)
)
if mibBuilder.loadTexts:
    gtmAppContDisTable.setStatus("current")
_GtmAppContDisEntry_Object = MibTableRow
gtmAppContDisEntry = _GtmAppContDisEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 4, 2, 1)
)
gtmAppContDisEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmAppContDisAppName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmAppContDisType"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmAppContDisName"),
)
if mibBuilder.loadTexts:
    gtmAppContDisEntry.setStatus("current")
_GtmAppContDisAppName_Type = LongDisplayString
_GtmAppContDisAppName_Object = MibTableColumn
gtmAppContDisAppName = _GtmAppContDisAppName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 4, 2, 1, 1),
    _GtmAppContDisAppName_Type()
)
gtmAppContDisAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppContDisAppName.setStatus("current")


class _GtmAppContDisType_Type(Integer32):
    """Custom type gtmAppContDisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("datacenter", 0),
          ("link", 2),
          ("server", 1))
    )


_GtmAppContDisType_Type.__name__ = "Integer32"
_GtmAppContDisType_Object = MibTableColumn
gtmAppContDisType = _GtmAppContDisType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 4, 2, 1, 2),
    _GtmAppContDisType_Type()
)
gtmAppContDisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppContDisType.setStatus("current")
_GtmAppContDisName_Type = LongDisplayString
_GtmAppContDisName_Object = MibTableColumn
gtmAppContDisName = _GtmAppContDisName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 2, 4, 2, 1, 3),
    _GtmAppContDisName_Type()
)
gtmAppContDisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmAppContDisName.setStatus("current")
_GtmDataCenters_ObjectIdentity = ObjectIdentity
gtmDataCenters = _GtmDataCenters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3)
)
_GtmDataCenter_ObjectIdentity = ObjectIdentity
gtmDataCenter = _GtmDataCenter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 1)
)
_GtmDcNumber_Type = Integer32
_GtmDcNumber_Object = MibScalar
gtmDcNumber = _GtmDcNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 1, 1),
    _GtmDcNumber_Type()
)
gtmDcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcNumber.setStatus("current")
_GtmDcTable_Object = MibTable
gtmDcTable = _GtmDcTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gtmDcTable.setStatus("current")
_GtmDcEntry_Object = MibTableRow
gtmDcEntry = _GtmDcEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 1, 2, 1)
)
gtmDcEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmDcName"),
)
if mibBuilder.loadTexts:
    gtmDcEntry.setStatus("current")
_GtmDcName_Type = LongDisplayString
_GtmDcName_Object = MibTableColumn
gtmDcName = _GtmDcName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 1, 2, 1, 1),
    _GtmDcName_Type()
)
gtmDcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcName.setStatus("current")
_GtmDcLocation_Type = LongDisplayString
_GtmDcLocation_Object = MibTableColumn
gtmDcLocation = _GtmDcLocation_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 1, 2, 1, 2),
    _GtmDcLocation_Type()
)
gtmDcLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcLocation.setStatus("current")
_GtmDcContact_Type = LongDisplayString
_GtmDcContact_Object = MibTableColumn
gtmDcContact = _GtmDcContact_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 1, 2, 1, 3),
    _GtmDcContact_Type()
)
gtmDcContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcContact.setStatus("current")


class _GtmDcEnabled_Type(Integer32):
    """Custom type gtmDcEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmDcEnabled_Type.__name__ = "Integer32"
_GtmDcEnabled_Object = MibTableColumn
gtmDcEnabled = _GtmDcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 1, 2, 1, 4),
    _GtmDcEnabled_Type()
)
gtmDcEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcEnabled.setStatus("current")
_GtmDataCenterStat_ObjectIdentity = ObjectIdentity
gtmDataCenterStat = _GtmDataCenterStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 2)
)
_GtmDcStatResetStats_Type = Integer32
_GtmDcStatResetStats_Object = MibScalar
gtmDcStatResetStats = _GtmDcStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 2, 1),
    _GtmDcStatResetStats_Type()
)
gtmDcStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtmDcStatResetStats.setStatus("current")
_GtmDcStatNumber_Type = Integer32
_GtmDcStatNumber_Object = MibScalar
gtmDcStatNumber = _GtmDcStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 2, 2),
    _GtmDcStatNumber_Type()
)
gtmDcStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcStatNumber.setStatus("current")
_GtmDcStatTable_Object = MibTable
gtmDcStatTable = _GtmDcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    gtmDcStatTable.setStatus("current")
_GtmDcStatEntry_Object = MibTableRow
gtmDcStatEntry = _GtmDcStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 2, 3, 1)
)
gtmDcStatEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmDcStatName"),
)
if mibBuilder.loadTexts:
    gtmDcStatEntry.setStatus("current")
_GtmDcStatName_Type = LongDisplayString
_GtmDcStatName_Object = MibTableColumn
gtmDcStatName = _GtmDcStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 2, 3, 1, 1),
    _GtmDcStatName_Type()
)
gtmDcStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcStatName.setStatus("current")
_GtmDcStatCpuUsage_Type = Counter64
_GtmDcStatCpuUsage_Object = MibTableColumn
gtmDcStatCpuUsage = _GtmDcStatCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 2, 3, 1, 2),
    _GtmDcStatCpuUsage_Type()
)
gtmDcStatCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcStatCpuUsage.setStatus("current")
_GtmDcStatMemAvail_Type = Counter64
_GtmDcStatMemAvail_Object = MibTableColumn
gtmDcStatMemAvail = _GtmDcStatMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 2, 3, 1, 3),
    _GtmDcStatMemAvail_Type()
)
gtmDcStatMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcStatMemAvail.setStatus("current")
_GtmDcStatBitsPerSecIn_Type = Counter64
_GtmDcStatBitsPerSecIn_Object = MibTableColumn
gtmDcStatBitsPerSecIn = _GtmDcStatBitsPerSecIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 2, 3, 1, 4),
    _GtmDcStatBitsPerSecIn_Type()
)
gtmDcStatBitsPerSecIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcStatBitsPerSecIn.setStatus("current")
_GtmDcStatBitsPerSecOut_Type = Counter64
_GtmDcStatBitsPerSecOut_Object = MibTableColumn
gtmDcStatBitsPerSecOut = _GtmDcStatBitsPerSecOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 2, 3, 1, 5),
    _GtmDcStatBitsPerSecOut_Type()
)
gtmDcStatBitsPerSecOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcStatBitsPerSecOut.setStatus("current")
_GtmDcStatPktsPerSecIn_Type = Counter64
_GtmDcStatPktsPerSecIn_Object = MibTableColumn
gtmDcStatPktsPerSecIn = _GtmDcStatPktsPerSecIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 2, 3, 1, 6),
    _GtmDcStatPktsPerSecIn_Type()
)
gtmDcStatPktsPerSecIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcStatPktsPerSecIn.setStatus("current")
_GtmDcStatPktsPerSecOut_Type = Counter64
_GtmDcStatPktsPerSecOut_Object = MibTableColumn
gtmDcStatPktsPerSecOut = _GtmDcStatPktsPerSecOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 2, 3, 1, 7),
    _GtmDcStatPktsPerSecOut_Type()
)
gtmDcStatPktsPerSecOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcStatPktsPerSecOut.setStatus("current")
_GtmDcStatConnections_Type = Counter64
_GtmDcStatConnections_Object = MibTableColumn
gtmDcStatConnections = _GtmDcStatConnections_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 2, 3, 1, 8),
    _GtmDcStatConnections_Type()
)
gtmDcStatConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcStatConnections.setStatus("current")
_GtmDcStatConnRate_Type = Counter64
_GtmDcStatConnRate_Object = MibTableColumn
gtmDcStatConnRate = _GtmDcStatConnRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 2, 3, 1, 9),
    _GtmDcStatConnRate_Type()
)
gtmDcStatConnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcStatConnRate.setStatus("deprecated")
_GtmDataCenterStatus_ObjectIdentity = ObjectIdentity
gtmDataCenterStatus = _GtmDataCenterStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 3)
)
_GtmDcStatusNumber_Type = Integer32
_GtmDcStatusNumber_Object = MibScalar
gtmDcStatusNumber = _GtmDcStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 3, 1),
    _GtmDcStatusNumber_Type()
)
gtmDcStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcStatusNumber.setStatus("current")
_GtmDcStatusTable_Object = MibTable
gtmDcStatusTable = _GtmDcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 3, 2)
)
if mibBuilder.loadTexts:
    gtmDcStatusTable.setStatus("current")
_GtmDcStatusEntry_Object = MibTableRow
gtmDcStatusEntry = _GtmDcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 3, 2, 1)
)
gtmDcStatusEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmDcStatusName"),
)
if mibBuilder.loadTexts:
    gtmDcStatusEntry.setStatus("current")
_GtmDcStatusName_Type = LongDisplayString
_GtmDcStatusName_Object = MibTableColumn
gtmDcStatusName = _GtmDcStatusName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 3, 2, 1, 1),
    _GtmDcStatusName_Type()
)
gtmDcStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcStatusName.setStatus("current")


class _GtmDcStatusAvailState_Type(Integer32):
    """Custom type gtmDcStatusAvailState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blue", 4),
          ("gray", 5),
          ("green", 1),
          ("none", 0),
          ("red", 3),
          ("yellow", 2))
    )


_GtmDcStatusAvailState_Type.__name__ = "Integer32"
_GtmDcStatusAvailState_Object = MibTableColumn
gtmDcStatusAvailState = _GtmDcStatusAvailState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 3, 2, 1, 2),
    _GtmDcStatusAvailState_Type()
)
gtmDcStatusAvailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcStatusAvailState.setStatus("current")


class _GtmDcStatusEnabledState_Type(Integer32):
    """Custom type gtmDcStatusEnabledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("disabledbyparent", 3),
          ("enabled", 1),
          ("none", 0))
    )


_GtmDcStatusEnabledState_Type.__name__ = "Integer32"
_GtmDcStatusEnabledState_Object = MibTableColumn
gtmDcStatusEnabledState = _GtmDcStatusEnabledState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 3, 2, 1, 3),
    _GtmDcStatusEnabledState_Type()
)
gtmDcStatusEnabledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcStatusEnabledState.setStatus("current")
_GtmDcStatusParentType_Type = Integer32
_GtmDcStatusParentType_Object = MibTableColumn
gtmDcStatusParentType = _GtmDcStatusParentType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 3, 2, 1, 4),
    _GtmDcStatusParentType_Type()
)
gtmDcStatusParentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcStatusParentType.setStatus("deprecated")
_GtmDcStatusDetailReason_Type = LongDisplayString
_GtmDcStatusDetailReason_Object = MibTableColumn
gtmDcStatusDetailReason = _GtmDcStatusDetailReason_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 3, 3, 2, 1, 5),
    _GtmDcStatusDetailReason_Type()
)
gtmDcStatusDetailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDcStatusDetailReason.setStatus("current")
_GtmIps_ObjectIdentity = ObjectIdentity
gtmIps = _GtmIps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 4)
)
_GtmIp_ObjectIdentity = ObjectIdentity
gtmIp = _GtmIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 4, 1)
)
_GtmIpNumber_Type = Integer32
_GtmIpNumber_Object = MibScalar
gtmIpNumber = _GtmIpNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 4, 1, 1),
    _GtmIpNumber_Type()
)
gtmIpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmIpNumber.setStatus("current")
_GtmIpTable_Object = MibTable
gtmIpTable = _GtmIpTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    gtmIpTable.setStatus("current")
_GtmIpEntry_Object = MibTableRow
gtmIpEntry = _GtmIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 4, 1, 2, 1)
)
gtmIpEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmIpIpType"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmIpIp"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmIpLinkName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmIpServerName"),
)
if mibBuilder.loadTexts:
    gtmIpEntry.setStatus("current")
_GtmIpIpType_Type = InetAddressType
_GtmIpIpType_Object = MibTableColumn
gtmIpIpType = _GtmIpIpType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 4, 1, 2, 1, 1),
    _GtmIpIpType_Type()
)
gtmIpIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmIpIpType.setStatus("current")
_GtmIpIp_Type = InetAddress
_GtmIpIp_Object = MibTableColumn
gtmIpIp = _GtmIpIp_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 4, 1, 2, 1, 2),
    _GtmIpIp_Type()
)
gtmIpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmIpIp.setStatus("current")
_GtmIpLinkName_Type = LongDisplayString
_GtmIpLinkName_Object = MibTableColumn
gtmIpLinkName = _GtmIpLinkName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 4, 1, 2, 1, 3),
    _GtmIpLinkName_Type()
)
gtmIpLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmIpLinkName.setStatus("current")
_GtmIpServerName_Type = LongDisplayString
_GtmIpServerName_Object = MibTableColumn
gtmIpServerName = _GtmIpServerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 4, 1, 2, 1, 4),
    _GtmIpServerName_Type()
)
gtmIpServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmIpServerName.setStatus("current")
_GtmIpUnitId_Type = Integer32
_GtmIpUnitId_Object = MibTableColumn
gtmIpUnitId = _GtmIpUnitId_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 4, 1, 2, 1, 5),
    _GtmIpUnitId_Type()
)
gtmIpUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmIpUnitId.setStatus("deprecated")
_GtmIpIpXlatedType_Type = InetAddressType
_GtmIpIpXlatedType_Object = MibTableColumn
gtmIpIpXlatedType = _GtmIpIpXlatedType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 4, 1, 2, 1, 6),
    _GtmIpIpXlatedType_Type()
)
gtmIpIpXlatedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmIpIpXlatedType.setStatus("current")
_GtmIpIpXlated_Type = InetAddress
_GtmIpIpXlated_Object = MibTableColumn
gtmIpIpXlated = _GtmIpIpXlated_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 4, 1, 2, 1, 7),
    _GtmIpIpXlated_Type()
)
gtmIpIpXlated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmIpIpXlated.setStatus("current")
_GtmIpDeviceName_Type = LongDisplayString
_GtmIpDeviceName_Object = MibTableColumn
gtmIpDeviceName = _GtmIpDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 4, 1, 2, 1, 8),
    _GtmIpDeviceName_Type()
)
gtmIpDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmIpDeviceName.setStatus("current")
_GtmLinks_ObjectIdentity = ObjectIdentity
gtmLinks = _GtmLinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5)
)
_GtmLink_ObjectIdentity = ObjectIdentity
gtmLink = _GtmLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1)
)
_GtmLinkNumber_Type = Integer32
_GtmLinkNumber_Object = MibScalar
gtmLinkNumber = _GtmLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 1),
    _GtmLinkNumber_Type()
)
gtmLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkNumber.setStatus("current")
_GtmLinkTable_Object = MibTable
gtmLinkTable = _GtmLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    gtmLinkTable.setStatus("current")
_GtmLinkEntry_Object = MibTableRow
gtmLinkEntry = _GtmLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1)
)
gtmLinkEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmLinkName"),
)
if mibBuilder.loadTexts:
    gtmLinkEntry.setStatus("current")
_GtmLinkName_Type = LongDisplayString
_GtmLinkName_Object = MibTableColumn
gtmLinkName = _GtmLinkName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 1),
    _GtmLinkName_Type()
)
gtmLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkName.setStatus("current")
_GtmLinkDcName_Type = LongDisplayString
_GtmLinkDcName_Object = MibTableColumn
gtmLinkDcName = _GtmLinkDcName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 2),
    _GtmLinkDcName_Type()
)
gtmLinkDcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkDcName.setStatus("current")
_GtmLinkIspName_Type = LongDisplayString
_GtmLinkIspName_Object = MibTableColumn
gtmLinkIspName = _GtmLinkIspName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 3),
    _GtmLinkIspName_Type()
)
gtmLinkIspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkIspName.setStatus("current")
_GtmLinkUplinkAddressType_Type = InetAddressType
_GtmLinkUplinkAddressType_Object = MibTableColumn
gtmLinkUplinkAddressType = _GtmLinkUplinkAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 4),
    _GtmLinkUplinkAddressType_Type()
)
gtmLinkUplinkAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkUplinkAddressType.setStatus("current")
_GtmLinkUplinkAddress_Type = InetAddress
_GtmLinkUplinkAddress_Object = MibTableColumn
gtmLinkUplinkAddress = _GtmLinkUplinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 5),
    _GtmLinkUplinkAddress_Type()
)
gtmLinkUplinkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkUplinkAddress.setStatus("current")


class _GtmLinkLimitInCpuUsageEnabled_Type(Integer32):
    """Custom type gtmLinkLimitInCpuUsageEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitInCpuUsageEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitInCpuUsageEnabled_Object = MibTableColumn
gtmLinkLimitInCpuUsageEnabled = _GtmLinkLimitInCpuUsageEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 6),
    _GtmLinkLimitInCpuUsageEnabled_Type()
)
gtmLinkLimitInCpuUsageEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitInCpuUsageEnabled.setStatus("current")


class _GtmLinkLimitInMemAvailEnabled_Type(Integer32):
    """Custom type gtmLinkLimitInMemAvailEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitInMemAvailEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitInMemAvailEnabled_Object = MibTableColumn
gtmLinkLimitInMemAvailEnabled = _GtmLinkLimitInMemAvailEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 7),
    _GtmLinkLimitInMemAvailEnabled_Type()
)
gtmLinkLimitInMemAvailEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitInMemAvailEnabled.setStatus("current")


class _GtmLinkLimitInBitsPerSecEnabled_Type(Integer32):
    """Custom type gtmLinkLimitInBitsPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitInBitsPerSecEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitInBitsPerSecEnabled_Object = MibTableColumn
gtmLinkLimitInBitsPerSecEnabled = _GtmLinkLimitInBitsPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 8),
    _GtmLinkLimitInBitsPerSecEnabled_Type()
)
gtmLinkLimitInBitsPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitInBitsPerSecEnabled.setStatus("current")


class _GtmLinkLimitInPktsPerSecEnabled_Type(Integer32):
    """Custom type gtmLinkLimitInPktsPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitInPktsPerSecEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitInPktsPerSecEnabled_Object = MibTableColumn
gtmLinkLimitInPktsPerSecEnabled = _GtmLinkLimitInPktsPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 9),
    _GtmLinkLimitInPktsPerSecEnabled_Type()
)
gtmLinkLimitInPktsPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitInPktsPerSecEnabled.setStatus("current")


class _GtmLinkLimitInConnEnabled_Type(Integer32):
    """Custom type gtmLinkLimitInConnEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitInConnEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitInConnEnabled_Object = MibTableColumn
gtmLinkLimitInConnEnabled = _GtmLinkLimitInConnEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 10),
    _GtmLinkLimitInConnEnabled_Type()
)
gtmLinkLimitInConnEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitInConnEnabled.setStatus("current")


class _GtmLinkLimitInConnPerSecEnabled_Type(Integer32):
    """Custom type gtmLinkLimitInConnPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitInConnPerSecEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitInConnPerSecEnabled_Object = MibTableColumn
gtmLinkLimitInConnPerSecEnabled = _GtmLinkLimitInConnPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 11),
    _GtmLinkLimitInConnPerSecEnabled_Type()
)
gtmLinkLimitInConnPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitInConnPerSecEnabled.setStatus("deprecated")
_GtmLinkLimitInCpuUsage_Type = Counter64
_GtmLinkLimitInCpuUsage_Object = MibTableColumn
gtmLinkLimitInCpuUsage = _GtmLinkLimitInCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 12),
    _GtmLinkLimitInCpuUsage_Type()
)
gtmLinkLimitInCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitInCpuUsage.setStatus("current")
_GtmLinkLimitInMemAvail_Type = Counter64
_GtmLinkLimitInMemAvail_Object = MibTableColumn
gtmLinkLimitInMemAvail = _GtmLinkLimitInMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 13),
    _GtmLinkLimitInMemAvail_Type()
)
gtmLinkLimitInMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitInMemAvail.setStatus("current")
_GtmLinkLimitInBitsPerSec_Type = Counter64
_GtmLinkLimitInBitsPerSec_Object = MibTableColumn
gtmLinkLimitInBitsPerSec = _GtmLinkLimitInBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 14),
    _GtmLinkLimitInBitsPerSec_Type()
)
gtmLinkLimitInBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitInBitsPerSec.setStatus("current")
_GtmLinkLimitInPktsPerSec_Type = Counter64
_GtmLinkLimitInPktsPerSec_Object = MibTableColumn
gtmLinkLimitInPktsPerSec = _GtmLinkLimitInPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 15),
    _GtmLinkLimitInPktsPerSec_Type()
)
gtmLinkLimitInPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitInPktsPerSec.setStatus("current")
_GtmLinkLimitInConn_Type = Counter64
_GtmLinkLimitInConn_Object = MibTableColumn
gtmLinkLimitInConn = _GtmLinkLimitInConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 16),
    _GtmLinkLimitInConn_Type()
)
gtmLinkLimitInConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitInConn.setStatus("current")
_GtmLinkLimitInConnPerSec_Type = Counter64
_GtmLinkLimitInConnPerSec_Object = MibTableColumn
gtmLinkLimitInConnPerSec = _GtmLinkLimitInConnPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 17),
    _GtmLinkLimitInConnPerSec_Type()
)
gtmLinkLimitInConnPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitInConnPerSec.setStatus("deprecated")


class _GtmLinkLimitOutCpuUsageEnabled_Type(Integer32):
    """Custom type gtmLinkLimitOutCpuUsageEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitOutCpuUsageEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitOutCpuUsageEnabled_Object = MibTableColumn
gtmLinkLimitOutCpuUsageEnabled = _GtmLinkLimitOutCpuUsageEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 18),
    _GtmLinkLimitOutCpuUsageEnabled_Type()
)
gtmLinkLimitOutCpuUsageEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitOutCpuUsageEnabled.setStatus("current")


class _GtmLinkLimitOutMemAvailEnabled_Type(Integer32):
    """Custom type gtmLinkLimitOutMemAvailEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitOutMemAvailEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitOutMemAvailEnabled_Object = MibTableColumn
gtmLinkLimitOutMemAvailEnabled = _GtmLinkLimitOutMemAvailEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 19),
    _GtmLinkLimitOutMemAvailEnabled_Type()
)
gtmLinkLimitOutMemAvailEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitOutMemAvailEnabled.setStatus("current")


class _GtmLinkLimitOutBitsPerSecEnabled_Type(Integer32):
    """Custom type gtmLinkLimitOutBitsPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitOutBitsPerSecEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitOutBitsPerSecEnabled_Object = MibTableColumn
gtmLinkLimitOutBitsPerSecEnabled = _GtmLinkLimitOutBitsPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 20),
    _GtmLinkLimitOutBitsPerSecEnabled_Type()
)
gtmLinkLimitOutBitsPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitOutBitsPerSecEnabled.setStatus("current")


class _GtmLinkLimitOutPktsPerSecEnabled_Type(Integer32):
    """Custom type gtmLinkLimitOutPktsPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitOutPktsPerSecEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitOutPktsPerSecEnabled_Object = MibTableColumn
gtmLinkLimitOutPktsPerSecEnabled = _GtmLinkLimitOutPktsPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 21),
    _GtmLinkLimitOutPktsPerSecEnabled_Type()
)
gtmLinkLimitOutPktsPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitOutPktsPerSecEnabled.setStatus("current")


class _GtmLinkLimitOutConnEnabled_Type(Integer32):
    """Custom type gtmLinkLimitOutConnEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitOutConnEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitOutConnEnabled_Object = MibTableColumn
gtmLinkLimitOutConnEnabled = _GtmLinkLimitOutConnEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 22),
    _GtmLinkLimitOutConnEnabled_Type()
)
gtmLinkLimitOutConnEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitOutConnEnabled.setStatus("current")


class _GtmLinkLimitOutConnPerSecEnabled_Type(Integer32):
    """Custom type gtmLinkLimitOutConnPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitOutConnPerSecEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitOutConnPerSecEnabled_Object = MibTableColumn
gtmLinkLimitOutConnPerSecEnabled = _GtmLinkLimitOutConnPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 23),
    _GtmLinkLimitOutConnPerSecEnabled_Type()
)
gtmLinkLimitOutConnPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitOutConnPerSecEnabled.setStatus("deprecated")
_GtmLinkLimitOutCpuUsage_Type = Counter64
_GtmLinkLimitOutCpuUsage_Object = MibTableColumn
gtmLinkLimitOutCpuUsage = _GtmLinkLimitOutCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 24),
    _GtmLinkLimitOutCpuUsage_Type()
)
gtmLinkLimitOutCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitOutCpuUsage.setStatus("current")
_GtmLinkLimitOutMemAvail_Type = Counter64
_GtmLinkLimitOutMemAvail_Object = MibTableColumn
gtmLinkLimitOutMemAvail = _GtmLinkLimitOutMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 25),
    _GtmLinkLimitOutMemAvail_Type()
)
gtmLinkLimitOutMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitOutMemAvail.setStatus("current")
_GtmLinkLimitOutBitsPerSec_Type = Counter64
_GtmLinkLimitOutBitsPerSec_Object = MibTableColumn
gtmLinkLimitOutBitsPerSec = _GtmLinkLimitOutBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 26),
    _GtmLinkLimitOutBitsPerSec_Type()
)
gtmLinkLimitOutBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitOutBitsPerSec.setStatus("current")
_GtmLinkLimitOutPktsPerSec_Type = Counter64
_GtmLinkLimitOutPktsPerSec_Object = MibTableColumn
gtmLinkLimitOutPktsPerSec = _GtmLinkLimitOutPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 27),
    _GtmLinkLimitOutPktsPerSec_Type()
)
gtmLinkLimitOutPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitOutPktsPerSec.setStatus("current")
_GtmLinkLimitOutConn_Type = Counter64
_GtmLinkLimitOutConn_Object = MibTableColumn
gtmLinkLimitOutConn = _GtmLinkLimitOutConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 28),
    _GtmLinkLimitOutConn_Type()
)
gtmLinkLimitOutConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitOutConn.setStatus("current")
_GtmLinkLimitOutConnPerSec_Type = Counter64
_GtmLinkLimitOutConnPerSec_Object = MibTableColumn
gtmLinkLimitOutConnPerSec = _GtmLinkLimitOutConnPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 29),
    _GtmLinkLimitOutConnPerSec_Type()
)
gtmLinkLimitOutConnPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitOutConnPerSec.setStatus("deprecated")


class _GtmLinkLimitTotalCpuUsageEnabled_Type(Integer32):
    """Custom type gtmLinkLimitTotalCpuUsageEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitTotalCpuUsageEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitTotalCpuUsageEnabled_Object = MibTableColumn
gtmLinkLimitTotalCpuUsageEnabled = _GtmLinkLimitTotalCpuUsageEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 30),
    _GtmLinkLimitTotalCpuUsageEnabled_Type()
)
gtmLinkLimitTotalCpuUsageEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitTotalCpuUsageEnabled.setStatus("current")


class _GtmLinkLimitTotalMemAvailEnabled_Type(Integer32):
    """Custom type gtmLinkLimitTotalMemAvailEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitTotalMemAvailEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitTotalMemAvailEnabled_Object = MibTableColumn
gtmLinkLimitTotalMemAvailEnabled = _GtmLinkLimitTotalMemAvailEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 31),
    _GtmLinkLimitTotalMemAvailEnabled_Type()
)
gtmLinkLimitTotalMemAvailEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitTotalMemAvailEnabled.setStatus("current")


class _GtmLinkLimitTotalBitsPerSecEnabled_Type(Integer32):
    """Custom type gtmLinkLimitTotalBitsPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitTotalBitsPerSecEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitTotalBitsPerSecEnabled_Object = MibTableColumn
gtmLinkLimitTotalBitsPerSecEnabled = _GtmLinkLimitTotalBitsPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 32),
    _GtmLinkLimitTotalBitsPerSecEnabled_Type()
)
gtmLinkLimitTotalBitsPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitTotalBitsPerSecEnabled.setStatus("current")


class _GtmLinkLimitTotalPktsPerSecEnabled_Type(Integer32):
    """Custom type gtmLinkLimitTotalPktsPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitTotalPktsPerSecEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitTotalPktsPerSecEnabled_Object = MibTableColumn
gtmLinkLimitTotalPktsPerSecEnabled = _GtmLinkLimitTotalPktsPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 33),
    _GtmLinkLimitTotalPktsPerSecEnabled_Type()
)
gtmLinkLimitTotalPktsPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitTotalPktsPerSecEnabled.setStatus("current")


class _GtmLinkLimitTotalConnEnabled_Type(Integer32):
    """Custom type gtmLinkLimitTotalConnEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitTotalConnEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitTotalConnEnabled_Object = MibTableColumn
gtmLinkLimitTotalConnEnabled = _GtmLinkLimitTotalConnEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 34),
    _GtmLinkLimitTotalConnEnabled_Type()
)
gtmLinkLimitTotalConnEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitTotalConnEnabled.setStatus("current")


class _GtmLinkLimitTotalConnPerSecEnabled_Type(Integer32):
    """Custom type gtmLinkLimitTotalConnPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkLimitTotalConnPerSecEnabled_Type.__name__ = "Integer32"
_GtmLinkLimitTotalConnPerSecEnabled_Object = MibTableColumn
gtmLinkLimitTotalConnPerSecEnabled = _GtmLinkLimitTotalConnPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 35),
    _GtmLinkLimitTotalConnPerSecEnabled_Type()
)
gtmLinkLimitTotalConnPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitTotalConnPerSecEnabled.setStatus("deprecated")
_GtmLinkLimitTotalCpuUsage_Type = Counter64
_GtmLinkLimitTotalCpuUsage_Object = MibTableColumn
gtmLinkLimitTotalCpuUsage = _GtmLinkLimitTotalCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 36),
    _GtmLinkLimitTotalCpuUsage_Type()
)
gtmLinkLimitTotalCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitTotalCpuUsage.setStatus("current")
_GtmLinkLimitTotalMemAvail_Type = Counter64
_GtmLinkLimitTotalMemAvail_Object = MibTableColumn
gtmLinkLimitTotalMemAvail = _GtmLinkLimitTotalMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 37),
    _GtmLinkLimitTotalMemAvail_Type()
)
gtmLinkLimitTotalMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitTotalMemAvail.setStatus("current")
_GtmLinkLimitTotalBitsPerSec_Type = Counter64
_GtmLinkLimitTotalBitsPerSec_Object = MibTableColumn
gtmLinkLimitTotalBitsPerSec = _GtmLinkLimitTotalBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 38),
    _GtmLinkLimitTotalBitsPerSec_Type()
)
gtmLinkLimitTotalBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitTotalBitsPerSec.setStatus("current")
_GtmLinkLimitTotalPktsPerSec_Type = Counter64
_GtmLinkLimitTotalPktsPerSec_Object = MibTableColumn
gtmLinkLimitTotalPktsPerSec = _GtmLinkLimitTotalPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 39),
    _GtmLinkLimitTotalPktsPerSec_Type()
)
gtmLinkLimitTotalPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitTotalPktsPerSec.setStatus("current")
_GtmLinkLimitTotalConn_Type = Counter64
_GtmLinkLimitTotalConn_Object = MibTableColumn
gtmLinkLimitTotalConn = _GtmLinkLimitTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 40),
    _GtmLinkLimitTotalConn_Type()
)
gtmLinkLimitTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitTotalConn.setStatus("current")
_GtmLinkLimitTotalConnPerSec_Type = Counter64
_GtmLinkLimitTotalConnPerSec_Object = MibTableColumn
gtmLinkLimitTotalConnPerSec = _GtmLinkLimitTotalConnPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 41),
    _GtmLinkLimitTotalConnPerSec_Type()
)
gtmLinkLimitTotalConnPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkLimitTotalConnPerSec.setStatus("deprecated")
_GtmLinkMonitorRule_Type = LongDisplayString
_GtmLinkMonitorRule_Object = MibTableColumn
gtmLinkMonitorRule = _GtmLinkMonitorRule_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 42),
    _GtmLinkMonitorRule_Type()
)
gtmLinkMonitorRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkMonitorRule.setStatus("current")


class _GtmLinkDuplex_Type(Integer32):
    """Custom type gtmLinkDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkDuplex_Type.__name__ = "Integer32"
_GtmLinkDuplex_Object = MibTableColumn
gtmLinkDuplex = _GtmLinkDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 43),
    _GtmLinkDuplex_Type()
)
gtmLinkDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkDuplex.setStatus("current")


class _GtmLinkEnabled_Type(Integer32):
    """Custom type gtmLinkEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmLinkEnabled_Type.__name__ = "Integer32"
_GtmLinkEnabled_Object = MibTableColumn
gtmLinkEnabled = _GtmLinkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 44),
    _GtmLinkEnabled_Type()
)
gtmLinkEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkEnabled.setStatus("current")
_GtmLinkRatio_Type = Integer32
_GtmLinkRatio_Object = MibTableColumn
gtmLinkRatio = _GtmLinkRatio_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 45),
    _GtmLinkRatio_Type()
)
gtmLinkRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkRatio.setStatus("current")
_GtmLinkPrepaid_Type = Counter64
_GtmLinkPrepaid_Object = MibTableColumn
gtmLinkPrepaid = _GtmLinkPrepaid_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 46),
    _GtmLinkPrepaid_Type()
)
gtmLinkPrepaid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkPrepaid.setStatus("current")
_GtmLinkPrepaidInDollars_Type = Integer32
_GtmLinkPrepaidInDollars_Object = MibTableColumn
gtmLinkPrepaidInDollars = _GtmLinkPrepaidInDollars_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 47),
    _GtmLinkPrepaidInDollars_Type()
)
gtmLinkPrepaidInDollars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkPrepaidInDollars.setStatus("deprecated")


class _GtmLinkWeightingType_Type(Integer32):
    """Custom type gtmLinkWeightingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cost", 1),
          ("ratio", 0))
    )


_GtmLinkWeightingType_Type.__name__ = "Integer32"
_GtmLinkWeightingType_Object = MibTableColumn
gtmLinkWeightingType = _GtmLinkWeightingType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 1, 2, 1, 48),
    _GtmLinkWeightingType_Type()
)
gtmLinkWeightingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkWeightingType.setStatus("current")
_GtmLinkCost_ObjectIdentity = ObjectIdentity
gtmLinkCost = _GtmLinkCost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 2)
)
_GtmLinkCostNumber_Type = Integer32
_GtmLinkCostNumber_Object = MibScalar
gtmLinkCostNumber = _GtmLinkCostNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 2, 1),
    _GtmLinkCostNumber_Type()
)
gtmLinkCostNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkCostNumber.setStatus("current")
_GtmLinkCostTable_Object = MibTable
gtmLinkCostTable = _GtmLinkCostTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 2, 2)
)
if mibBuilder.loadTexts:
    gtmLinkCostTable.setStatus("current")
_GtmLinkCostEntry_Object = MibTableRow
gtmLinkCostEntry = _GtmLinkCostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 2, 2, 1)
)
gtmLinkCostEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmLinkCostName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmLinkCostIndex"),
)
if mibBuilder.loadTexts:
    gtmLinkCostEntry.setStatus("current")
_GtmLinkCostName_Type = LongDisplayString
_GtmLinkCostName_Object = MibTableColumn
gtmLinkCostName = _GtmLinkCostName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 2, 2, 1, 1),
    _GtmLinkCostName_Type()
)
gtmLinkCostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkCostName.setStatus("current")


class _GtmLinkCostIndex_Type(Integer32):
    """Custom type gtmLinkCostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GtmLinkCostIndex_Type.__name__ = "Integer32"
_GtmLinkCostIndex_Object = MibTableColumn
gtmLinkCostIndex = _GtmLinkCostIndex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 2, 2, 1, 2),
    _GtmLinkCostIndex_Type()
)
gtmLinkCostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkCostIndex.setStatus("current")
_GtmLinkCostUptoBps_Type = Counter64
_GtmLinkCostUptoBps_Object = MibTableColumn
gtmLinkCostUptoBps = _GtmLinkCostUptoBps_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 2, 2, 1, 3),
    _GtmLinkCostUptoBps_Type()
)
gtmLinkCostUptoBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkCostUptoBps.setStatus("current")
_GtmLinkCostDollarsPerMbps_Type = Integer32
_GtmLinkCostDollarsPerMbps_Object = MibTableColumn
gtmLinkCostDollarsPerMbps = _GtmLinkCostDollarsPerMbps_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 2, 2, 1, 4),
    _GtmLinkCostDollarsPerMbps_Type()
)
gtmLinkCostDollarsPerMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkCostDollarsPerMbps.setStatus("current")
_GtmLinkStat_ObjectIdentity = ObjectIdentity
gtmLinkStat = _GtmLinkStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3)
)
_GtmLinkStatResetStats_Type = Integer32
_GtmLinkStatResetStats_Object = MibScalar
gtmLinkStatResetStats = _GtmLinkStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3, 1),
    _GtmLinkStatResetStats_Type()
)
gtmLinkStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtmLinkStatResetStats.setStatus("current")
_GtmLinkStatNumber_Type = Integer32
_GtmLinkStatNumber_Object = MibScalar
gtmLinkStatNumber = _GtmLinkStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3, 2),
    _GtmLinkStatNumber_Type()
)
gtmLinkStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatNumber.setStatus("current")
_GtmLinkStatTable_Object = MibTable
gtmLinkStatTable = _GtmLinkStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3, 3)
)
if mibBuilder.loadTexts:
    gtmLinkStatTable.setStatus("current")
_GtmLinkStatEntry_Object = MibTableRow
gtmLinkStatEntry = _GtmLinkStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3, 3, 1)
)
gtmLinkStatEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmLinkStatName"),
)
if mibBuilder.loadTexts:
    gtmLinkStatEntry.setStatus("current")
_GtmLinkStatName_Type = LongDisplayString
_GtmLinkStatName_Object = MibTableColumn
gtmLinkStatName = _GtmLinkStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3, 3, 1, 1),
    _GtmLinkStatName_Type()
)
gtmLinkStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatName.setStatus("current")
_GtmLinkStatRate_Type = Gauge32
_GtmLinkStatRate_Object = MibTableColumn
gtmLinkStatRate = _GtmLinkStatRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3, 3, 1, 2),
    _GtmLinkStatRate_Type()
)
gtmLinkStatRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatRate.setStatus("current")
_GtmLinkStatRateIn_Type = Gauge32
_GtmLinkStatRateIn_Object = MibTableColumn
gtmLinkStatRateIn = _GtmLinkStatRateIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3, 3, 1, 3),
    _GtmLinkStatRateIn_Type()
)
gtmLinkStatRateIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatRateIn.setStatus("current")
_GtmLinkStatRateOut_Type = Gauge32
_GtmLinkStatRateOut_Object = MibTableColumn
gtmLinkStatRateOut = _GtmLinkStatRateOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3, 3, 1, 4),
    _GtmLinkStatRateOut_Type()
)
gtmLinkStatRateOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatRateOut.setStatus("current")
_GtmLinkStatRateNode_Type = Gauge32
_GtmLinkStatRateNode_Object = MibTableColumn
gtmLinkStatRateNode = _GtmLinkStatRateNode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3, 3, 1, 5),
    _GtmLinkStatRateNode_Type()
)
gtmLinkStatRateNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatRateNode.setStatus("current")
_GtmLinkStatRateNodeIn_Type = Gauge32
_GtmLinkStatRateNodeIn_Object = MibTableColumn
gtmLinkStatRateNodeIn = _GtmLinkStatRateNodeIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3, 3, 1, 6),
    _GtmLinkStatRateNodeIn_Type()
)
gtmLinkStatRateNodeIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatRateNodeIn.setStatus("current")
_GtmLinkStatRateNodeOut_Type = Gauge32
_GtmLinkStatRateNodeOut_Object = MibTableColumn
gtmLinkStatRateNodeOut = _GtmLinkStatRateNodeOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3, 3, 1, 7),
    _GtmLinkStatRateNodeOut_Type()
)
gtmLinkStatRateNodeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatRateNodeOut.setStatus("current")
_GtmLinkStatRateVses_Type = Gauge32
_GtmLinkStatRateVses_Object = MibTableColumn
gtmLinkStatRateVses = _GtmLinkStatRateVses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3, 3, 1, 8),
    _GtmLinkStatRateVses_Type()
)
gtmLinkStatRateVses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatRateVses.setStatus("current")
_GtmLinkStatRateVsesIn_Type = Gauge32
_GtmLinkStatRateVsesIn_Object = MibTableColumn
gtmLinkStatRateVsesIn = _GtmLinkStatRateVsesIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3, 3, 1, 9),
    _GtmLinkStatRateVsesIn_Type()
)
gtmLinkStatRateVsesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatRateVsesIn.setStatus("current")
_GtmLinkStatRateVsesOut_Type = Gauge32
_GtmLinkStatRateVsesOut_Object = MibTableColumn
gtmLinkStatRateVsesOut = _GtmLinkStatRateVsesOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3, 3, 1, 10),
    _GtmLinkStatRateVsesOut_Type()
)
gtmLinkStatRateVsesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatRateVsesOut.setStatus("current")
_GtmLinkStatLcsIn_Type = Counter64
_GtmLinkStatLcsIn_Object = MibTableColumn
gtmLinkStatLcsIn = _GtmLinkStatLcsIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3, 3, 1, 11),
    _GtmLinkStatLcsIn_Type()
)
gtmLinkStatLcsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatLcsIn.setStatus("current")
_GtmLinkStatLcsOut_Type = Counter64
_GtmLinkStatLcsOut_Object = MibTableColumn
gtmLinkStatLcsOut = _GtmLinkStatLcsOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3, 3, 1, 12),
    _GtmLinkStatLcsOut_Type()
)
gtmLinkStatLcsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatLcsOut.setStatus("current")
_GtmLinkStatPaths_Type = Counter64
_GtmLinkStatPaths_Object = MibTableColumn
gtmLinkStatPaths = _GtmLinkStatPaths_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 3, 3, 1, 13),
    _GtmLinkStatPaths_Type()
)
gtmLinkStatPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatPaths.setStatus("current")
_GtmLinkStatus_ObjectIdentity = ObjectIdentity
gtmLinkStatus = _GtmLinkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 4)
)
_GtmLinkStatusNumber_Type = Integer32
_GtmLinkStatusNumber_Object = MibScalar
gtmLinkStatusNumber = _GtmLinkStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 4, 1),
    _GtmLinkStatusNumber_Type()
)
gtmLinkStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatusNumber.setStatus("current")
_GtmLinkStatusTable_Object = MibTable
gtmLinkStatusTable = _GtmLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 4, 2)
)
if mibBuilder.loadTexts:
    gtmLinkStatusTable.setStatus("current")
_GtmLinkStatusEntry_Object = MibTableRow
gtmLinkStatusEntry = _GtmLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 4, 2, 1)
)
gtmLinkStatusEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmLinkStatusName"),
)
if mibBuilder.loadTexts:
    gtmLinkStatusEntry.setStatus("current")
_GtmLinkStatusName_Type = LongDisplayString
_GtmLinkStatusName_Object = MibTableColumn
gtmLinkStatusName = _GtmLinkStatusName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 4, 2, 1, 1),
    _GtmLinkStatusName_Type()
)
gtmLinkStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatusName.setStatus("current")


class _GtmLinkStatusAvailState_Type(Integer32):
    """Custom type gtmLinkStatusAvailState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blue", 4),
          ("gray", 5),
          ("green", 1),
          ("none", 0),
          ("red", 3),
          ("yellow", 2))
    )


_GtmLinkStatusAvailState_Type.__name__ = "Integer32"
_GtmLinkStatusAvailState_Object = MibTableColumn
gtmLinkStatusAvailState = _GtmLinkStatusAvailState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 4, 2, 1, 2),
    _GtmLinkStatusAvailState_Type()
)
gtmLinkStatusAvailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatusAvailState.setStatus("current")


class _GtmLinkStatusEnabledState_Type(Integer32):
    """Custom type gtmLinkStatusEnabledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("disabledbyparent", 3),
          ("enabled", 1),
          ("none", 0))
    )


_GtmLinkStatusEnabledState_Type.__name__ = "Integer32"
_GtmLinkStatusEnabledState_Object = MibTableColumn
gtmLinkStatusEnabledState = _GtmLinkStatusEnabledState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 4, 2, 1, 3),
    _GtmLinkStatusEnabledState_Type()
)
gtmLinkStatusEnabledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatusEnabledState.setStatus("current")
_GtmLinkStatusParentType_Type = Integer32
_GtmLinkStatusParentType_Object = MibTableColumn
gtmLinkStatusParentType = _GtmLinkStatusParentType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 4, 2, 1, 4),
    _GtmLinkStatusParentType_Type()
)
gtmLinkStatusParentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatusParentType.setStatus("deprecated")
_GtmLinkStatusDetailReason_Type = LongDisplayString
_GtmLinkStatusDetailReason_Object = MibTableColumn
gtmLinkStatusDetailReason = _GtmLinkStatusDetailReason_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 5, 4, 2, 1, 5),
    _GtmLinkStatusDetailReason_Type()
)
gtmLinkStatusDetailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmLinkStatusDetailReason.setStatus("current")
_GtmPools_ObjectIdentity = ObjectIdentity
gtmPools = _GtmPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6)
)
_GtmPool_ObjectIdentity = ObjectIdentity
gtmPool = _GtmPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1)
)
_GtmPoolNumber_Type = Integer32
_GtmPoolNumber_Object = MibScalar
gtmPoolNumber = _GtmPoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 1),
    _GtmPoolNumber_Type()
)
gtmPoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolNumber.setStatus("current")
_GtmPoolTable_Object = MibTable
gtmPoolTable = _GtmPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2)
)
if mibBuilder.loadTexts:
    gtmPoolTable.setStatus("current")
_GtmPoolEntry_Object = MibTableRow
gtmPoolEntry = _GtmPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1)
)
gtmPoolEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmPoolName"),
)
if mibBuilder.loadTexts:
    gtmPoolEntry.setStatus("current")
_GtmPoolName_Type = LongDisplayString
_GtmPoolName_Object = MibTableColumn
gtmPoolName = _GtmPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 1),
    _GtmPoolName_Type()
)
gtmPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolName.setStatus("current")
_GtmPoolTtl_Type = Integer32
_GtmPoolTtl_Object = MibTableColumn
gtmPoolTtl = _GtmPoolTtl_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 2),
    _GtmPoolTtl_Type()
)
gtmPoolTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolTtl.setStatus("current")


class _GtmPoolEnabled_Type(Integer32):
    """Custom type gtmPoolEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmPoolEnabled_Type.__name__ = "Integer32"
_GtmPoolEnabled_Object = MibTableColumn
gtmPoolEnabled = _GtmPoolEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 3),
    _GtmPoolEnabled_Type()
)
gtmPoolEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolEnabled.setStatus("current")


class _GtmPoolVerifyMember_Type(Integer32):
    """Custom type gtmPoolVerifyMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmPoolVerifyMember_Type.__name__ = "Integer32"
_GtmPoolVerifyMember_Object = MibTableColumn
gtmPoolVerifyMember = _GtmPoolVerifyMember_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 4),
    _GtmPoolVerifyMember_Type()
)
gtmPoolVerifyMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolVerifyMember.setStatus("current")


class _GtmPoolDynamicRatio_Type(Integer32):
    """Custom type gtmPoolDynamicRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmPoolDynamicRatio_Type.__name__ = "Integer32"
_GtmPoolDynamicRatio_Object = MibTableColumn
gtmPoolDynamicRatio = _GtmPoolDynamicRatio_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 5),
    _GtmPoolDynamicRatio_Type()
)
gtmPoolDynamicRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolDynamicRatio.setStatus("current")
_GtmPoolAnswersToReturn_Type = Integer32
_GtmPoolAnswersToReturn_Object = MibTableColumn
gtmPoolAnswersToReturn = _GtmPoolAnswersToReturn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 6),
    _GtmPoolAnswersToReturn_Type()
)
gtmPoolAnswersToReturn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolAnswersToReturn.setStatus("current")


class _GtmPoolLbMode_Type(Integer32):
    """Custom type gtmPoolLbMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("bps", 15),
          ("cpu", 12),
          ("droppacket", 16),
          ("explicitip", 17),
          ("ga", 6),
          ("hitratio", 13),
          ("leastconn", 8),
          ("lowesthops", 10),
          ("lowestrtt", 9),
          ("null", 1),
          ("packetrate", 11),
          ("qos", 14),
          ("ratio", 3),
          ("returntodns", 0),
          ("roundrobin", 2),
          ("statpersit", 5),
          ("topology", 4),
          ("vscapacity", 7),
          ("vsscore", 18))
    )


_GtmPoolLbMode_Type.__name__ = "Integer32"
_GtmPoolLbMode_Object = MibTableColumn
gtmPoolLbMode = _GtmPoolLbMode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 7),
    _GtmPoolLbMode_Type()
)
gtmPoolLbMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolLbMode.setStatus("current")


class _GtmPoolAlternate_Type(Integer32):
    """Custom type gtmPoolAlternate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("bps", 15),
          ("cpu", 12),
          ("droppacket", 16),
          ("explicitip", 17),
          ("ga", 6),
          ("hitratio", 13),
          ("leastconn", 8),
          ("lowesthops", 10),
          ("lowestrtt", 9),
          ("null", 1),
          ("packetrate", 11),
          ("qos", 14),
          ("ratio", 3),
          ("returntodns", 0),
          ("roundrobin", 2),
          ("statpersit", 5),
          ("topology", 4),
          ("vscapacity", 7),
          ("vsscore", 18))
    )


_GtmPoolAlternate_Type.__name__ = "Integer32"
_GtmPoolAlternate_Object = MibTableColumn
gtmPoolAlternate = _GtmPoolAlternate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 8),
    _GtmPoolAlternate_Type()
)
gtmPoolAlternate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolAlternate.setStatus("current")


class _GtmPoolFallback_Type(Integer32):
    """Custom type gtmPoolFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("bps", 15),
          ("cpu", 12),
          ("droppacket", 16),
          ("explicitip", 17),
          ("ga", 6),
          ("hitratio", 13),
          ("leastconn", 8),
          ("lowesthops", 10),
          ("lowestrtt", 9),
          ("null", 1),
          ("packetrate", 11),
          ("qos", 14),
          ("ratio", 3),
          ("returntodns", 0),
          ("roundrobin", 2),
          ("statpersit", 5),
          ("topology", 4),
          ("vscapacity", 7),
          ("vsscore", 18))
    )


_GtmPoolFallback_Type.__name__ = "Integer32"
_GtmPoolFallback_Object = MibTableColumn
gtmPoolFallback = _GtmPoolFallback_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 9),
    _GtmPoolFallback_Type()
)
gtmPoolFallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolFallback.setStatus("current")


class _GtmPoolManualResume_Type(Integer32):
    """Custom type gtmPoolManualResume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_GtmPoolManualResume_Type.__name__ = "Integer32"
_GtmPoolManualResume_Object = MibTableColumn
gtmPoolManualResume = _GtmPoolManualResume_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 10),
    _GtmPoolManualResume_Type()
)
gtmPoolManualResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolManualResume.setStatus("current")
_GtmPoolQosCoeffRtt_Type = Integer32
_GtmPoolQosCoeffRtt_Object = MibTableColumn
gtmPoolQosCoeffRtt = _GtmPoolQosCoeffRtt_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 11),
    _GtmPoolQosCoeffRtt_Type()
)
gtmPoolQosCoeffRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolQosCoeffRtt.setStatus("current")
_GtmPoolQosCoeffHops_Type = Integer32
_GtmPoolQosCoeffHops_Object = MibTableColumn
gtmPoolQosCoeffHops = _GtmPoolQosCoeffHops_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 12),
    _GtmPoolQosCoeffHops_Type()
)
gtmPoolQosCoeffHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolQosCoeffHops.setStatus("current")
_GtmPoolQosCoeffTopology_Type = Integer32
_GtmPoolQosCoeffTopology_Object = MibTableColumn
gtmPoolQosCoeffTopology = _GtmPoolQosCoeffTopology_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 13),
    _GtmPoolQosCoeffTopology_Type()
)
gtmPoolQosCoeffTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolQosCoeffTopology.setStatus("current")
_GtmPoolQosCoeffHitRatio_Type = Integer32
_GtmPoolQosCoeffHitRatio_Object = MibTableColumn
gtmPoolQosCoeffHitRatio = _GtmPoolQosCoeffHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 14),
    _GtmPoolQosCoeffHitRatio_Type()
)
gtmPoolQosCoeffHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolQosCoeffHitRatio.setStatus("current")
_GtmPoolQosCoeffPacketRate_Type = Integer32
_GtmPoolQosCoeffPacketRate_Object = MibTableColumn
gtmPoolQosCoeffPacketRate = _GtmPoolQosCoeffPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 15),
    _GtmPoolQosCoeffPacketRate_Type()
)
gtmPoolQosCoeffPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolQosCoeffPacketRate.setStatus("current")
_GtmPoolQosCoeffVsCapacity_Type = Integer32
_GtmPoolQosCoeffVsCapacity_Object = MibTableColumn
gtmPoolQosCoeffVsCapacity = _GtmPoolQosCoeffVsCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 16),
    _GtmPoolQosCoeffVsCapacity_Type()
)
gtmPoolQosCoeffVsCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolQosCoeffVsCapacity.setStatus("current")
_GtmPoolQosCoeffBps_Type = Integer32
_GtmPoolQosCoeffBps_Object = MibTableColumn
gtmPoolQosCoeffBps = _GtmPoolQosCoeffBps_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 17),
    _GtmPoolQosCoeffBps_Type()
)
gtmPoolQosCoeffBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolQosCoeffBps.setStatus("current")
_GtmPoolQosCoeffLcs_Type = Integer32
_GtmPoolQosCoeffLcs_Object = MibTableColumn
gtmPoolQosCoeffLcs = _GtmPoolQosCoeffLcs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 18),
    _GtmPoolQosCoeffLcs_Type()
)
gtmPoolQosCoeffLcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolQosCoeffLcs.setStatus("current")
_GtmPoolQosCoeffConnRate_Type = Integer32
_GtmPoolQosCoeffConnRate_Object = MibTableColumn
gtmPoolQosCoeffConnRate = _GtmPoolQosCoeffConnRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 19),
    _GtmPoolQosCoeffConnRate_Type()
)
gtmPoolQosCoeffConnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolQosCoeffConnRate.setStatus("deprecated")
_GtmPoolFallbackIpType_Type = InetAddressType
_GtmPoolFallbackIpType_Object = MibTableColumn
gtmPoolFallbackIpType = _GtmPoolFallbackIpType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 20),
    _GtmPoolFallbackIpType_Type()
)
gtmPoolFallbackIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolFallbackIpType.setStatus("current")
_GtmPoolFallbackIp_Type = InetAddress
_GtmPoolFallbackIp_Object = MibTableColumn
gtmPoolFallbackIp = _GtmPoolFallbackIp_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 21),
    _GtmPoolFallbackIp_Type()
)
gtmPoolFallbackIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolFallbackIp.setStatus("current")
_GtmPoolCname_Type = LongDisplayString
_GtmPoolCname_Object = MibTableColumn
gtmPoolCname = _GtmPoolCname_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 22),
    _GtmPoolCname_Type()
)
gtmPoolCname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolCname.setStatus("current")


class _GtmPoolLimitCpuUsageEnabled_Type(Integer32):
    """Custom type gtmPoolLimitCpuUsageEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmPoolLimitCpuUsageEnabled_Type.__name__ = "Integer32"
_GtmPoolLimitCpuUsageEnabled_Object = MibTableColumn
gtmPoolLimitCpuUsageEnabled = _GtmPoolLimitCpuUsageEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 23),
    _GtmPoolLimitCpuUsageEnabled_Type()
)
gtmPoolLimitCpuUsageEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolLimitCpuUsageEnabled.setStatus("current")


class _GtmPoolLimitMemAvailEnabled_Type(Integer32):
    """Custom type gtmPoolLimitMemAvailEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmPoolLimitMemAvailEnabled_Type.__name__ = "Integer32"
_GtmPoolLimitMemAvailEnabled_Object = MibTableColumn
gtmPoolLimitMemAvailEnabled = _GtmPoolLimitMemAvailEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 24),
    _GtmPoolLimitMemAvailEnabled_Type()
)
gtmPoolLimitMemAvailEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolLimitMemAvailEnabled.setStatus("current")


class _GtmPoolLimitBitsPerSecEnabled_Type(Integer32):
    """Custom type gtmPoolLimitBitsPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmPoolLimitBitsPerSecEnabled_Type.__name__ = "Integer32"
_GtmPoolLimitBitsPerSecEnabled_Object = MibTableColumn
gtmPoolLimitBitsPerSecEnabled = _GtmPoolLimitBitsPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 25),
    _GtmPoolLimitBitsPerSecEnabled_Type()
)
gtmPoolLimitBitsPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolLimitBitsPerSecEnabled.setStatus("current")


class _GtmPoolLimitPktsPerSecEnabled_Type(Integer32):
    """Custom type gtmPoolLimitPktsPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmPoolLimitPktsPerSecEnabled_Type.__name__ = "Integer32"
_GtmPoolLimitPktsPerSecEnabled_Object = MibTableColumn
gtmPoolLimitPktsPerSecEnabled = _GtmPoolLimitPktsPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 26),
    _GtmPoolLimitPktsPerSecEnabled_Type()
)
gtmPoolLimitPktsPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolLimitPktsPerSecEnabled.setStatus("current")


class _GtmPoolLimitConnEnabled_Type(Integer32):
    """Custom type gtmPoolLimitConnEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmPoolLimitConnEnabled_Type.__name__ = "Integer32"
_GtmPoolLimitConnEnabled_Object = MibTableColumn
gtmPoolLimitConnEnabled = _GtmPoolLimitConnEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 27),
    _GtmPoolLimitConnEnabled_Type()
)
gtmPoolLimitConnEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolLimitConnEnabled.setStatus("current")


class _GtmPoolLimitConnPerSecEnabled_Type(Integer32):
    """Custom type gtmPoolLimitConnPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmPoolLimitConnPerSecEnabled_Type.__name__ = "Integer32"
_GtmPoolLimitConnPerSecEnabled_Object = MibTableColumn
gtmPoolLimitConnPerSecEnabled = _GtmPoolLimitConnPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 28),
    _GtmPoolLimitConnPerSecEnabled_Type()
)
gtmPoolLimitConnPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolLimitConnPerSecEnabled.setStatus("deprecated")
_GtmPoolLimitCpuUsage_Type = Counter64
_GtmPoolLimitCpuUsage_Object = MibTableColumn
gtmPoolLimitCpuUsage = _GtmPoolLimitCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 29),
    _GtmPoolLimitCpuUsage_Type()
)
gtmPoolLimitCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolLimitCpuUsage.setStatus("current")
_GtmPoolLimitMemAvail_Type = Counter64
_GtmPoolLimitMemAvail_Object = MibTableColumn
gtmPoolLimitMemAvail = _GtmPoolLimitMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 30),
    _GtmPoolLimitMemAvail_Type()
)
gtmPoolLimitMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolLimitMemAvail.setStatus("current")
_GtmPoolLimitBitsPerSec_Type = Counter64
_GtmPoolLimitBitsPerSec_Object = MibTableColumn
gtmPoolLimitBitsPerSec = _GtmPoolLimitBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 31),
    _GtmPoolLimitBitsPerSec_Type()
)
gtmPoolLimitBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolLimitBitsPerSec.setStatus("current")
_GtmPoolLimitPktsPerSec_Type = Counter64
_GtmPoolLimitPktsPerSec_Object = MibTableColumn
gtmPoolLimitPktsPerSec = _GtmPoolLimitPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 32),
    _GtmPoolLimitPktsPerSec_Type()
)
gtmPoolLimitPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolLimitPktsPerSec.setStatus("current")
_GtmPoolLimitConn_Type = Counter64
_GtmPoolLimitConn_Object = MibTableColumn
gtmPoolLimitConn = _GtmPoolLimitConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 33),
    _GtmPoolLimitConn_Type()
)
gtmPoolLimitConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolLimitConn.setStatus("current")
_GtmPoolLimitConnPerSec_Type = Counter64
_GtmPoolLimitConnPerSec_Object = MibTableColumn
gtmPoolLimitConnPerSec = _GtmPoolLimitConnPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 34),
    _GtmPoolLimitConnPerSec_Type()
)
gtmPoolLimitConnPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolLimitConnPerSec.setStatus("deprecated")
_GtmPoolMonitorRule_Type = LongDisplayString
_GtmPoolMonitorRule_Object = MibTableColumn
gtmPoolMonitorRule = _GtmPoolMonitorRule_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 35),
    _GtmPoolMonitorRule_Type()
)
gtmPoolMonitorRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMonitorRule.setStatus("current")
_GtmPoolQosCoeffVsScore_Type = Integer32
_GtmPoolQosCoeffVsScore_Object = MibTableColumn
gtmPoolQosCoeffVsScore = _GtmPoolQosCoeffVsScore_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 36),
    _GtmPoolQosCoeffVsScore_Type()
)
gtmPoolQosCoeffVsScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolQosCoeffVsScore.setStatus("current")
_GtmPoolFallbackIpv6Type_Type = InetAddressType
_GtmPoolFallbackIpv6Type_Object = MibTableColumn
gtmPoolFallbackIpv6Type = _GtmPoolFallbackIpv6Type_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 37),
    _GtmPoolFallbackIpv6Type_Type()
)
gtmPoolFallbackIpv6Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolFallbackIpv6Type.setStatus("current")
_GtmPoolFallbackIpv6_Type = InetAddress
_GtmPoolFallbackIpv6_Object = MibTableColumn
gtmPoolFallbackIpv6 = _GtmPoolFallbackIpv6_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 1, 2, 1, 38),
    _GtmPoolFallbackIpv6_Type()
)
gtmPoolFallbackIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolFallbackIpv6.setStatus("current")
_GtmPoolStat_ObjectIdentity = ObjectIdentity
gtmPoolStat = _GtmPoolStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 2)
)
_GtmPoolStatResetStats_Type = Integer32
_GtmPoolStatResetStats_Object = MibScalar
gtmPoolStatResetStats = _GtmPoolStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 2, 1),
    _GtmPoolStatResetStats_Type()
)
gtmPoolStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtmPoolStatResetStats.setStatus("current")
_GtmPoolStatNumber_Type = Integer32
_GtmPoolStatNumber_Object = MibScalar
gtmPoolStatNumber = _GtmPoolStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 2, 2),
    _GtmPoolStatNumber_Type()
)
gtmPoolStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolStatNumber.setStatus("current")
_GtmPoolStatTable_Object = MibTable
gtmPoolStatTable = _GtmPoolStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 2, 3)
)
if mibBuilder.loadTexts:
    gtmPoolStatTable.setStatus("current")
_GtmPoolStatEntry_Object = MibTableRow
gtmPoolStatEntry = _GtmPoolStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 2, 3, 1)
)
gtmPoolStatEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmPoolStatName"),
)
if mibBuilder.loadTexts:
    gtmPoolStatEntry.setStatus("current")
_GtmPoolStatName_Type = LongDisplayString
_GtmPoolStatName_Object = MibTableColumn
gtmPoolStatName = _GtmPoolStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 2, 3, 1, 1),
    _GtmPoolStatName_Type()
)
gtmPoolStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolStatName.setStatus("current")
_GtmPoolStatPreferred_Type = Counter64
_GtmPoolStatPreferred_Object = MibTableColumn
gtmPoolStatPreferred = _GtmPoolStatPreferred_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 2, 3, 1, 2),
    _GtmPoolStatPreferred_Type()
)
gtmPoolStatPreferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolStatPreferred.setStatus("current")
_GtmPoolStatAlternate_Type = Counter64
_GtmPoolStatAlternate_Object = MibTableColumn
gtmPoolStatAlternate = _GtmPoolStatAlternate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 2, 3, 1, 3),
    _GtmPoolStatAlternate_Type()
)
gtmPoolStatAlternate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolStatAlternate.setStatus("current")
_GtmPoolStatFallback_Type = Counter64
_GtmPoolStatFallback_Object = MibTableColumn
gtmPoolStatFallback = _GtmPoolStatFallback_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 2, 3, 1, 4),
    _GtmPoolStatFallback_Type()
)
gtmPoolStatFallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolStatFallback.setStatus("current")
_GtmPoolStatDropped_Type = Counter64
_GtmPoolStatDropped_Object = MibTableColumn
gtmPoolStatDropped = _GtmPoolStatDropped_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 2, 3, 1, 5),
    _GtmPoolStatDropped_Type()
)
gtmPoolStatDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolStatDropped.setStatus("current")
_GtmPoolStatExplicitIp_Type = Counter64
_GtmPoolStatExplicitIp_Object = MibTableColumn
gtmPoolStatExplicitIp = _GtmPoolStatExplicitIp_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 2, 3, 1, 6),
    _GtmPoolStatExplicitIp_Type()
)
gtmPoolStatExplicitIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolStatExplicitIp.setStatus("deprecated")
_GtmPoolStatReturnToDns_Type = Counter64
_GtmPoolStatReturnToDns_Object = MibTableColumn
gtmPoolStatReturnToDns = _GtmPoolStatReturnToDns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 2, 3, 1, 7),
    _GtmPoolStatReturnToDns_Type()
)
gtmPoolStatReturnToDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolStatReturnToDns.setStatus("current")
_GtmPoolStatReturnFromDns_Type = Counter64
_GtmPoolStatReturnFromDns_Object = MibTableColumn
gtmPoolStatReturnFromDns = _GtmPoolStatReturnFromDns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 2, 3, 1, 8),
    _GtmPoolStatReturnFromDns_Type()
)
gtmPoolStatReturnFromDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolStatReturnFromDns.setStatus("current")
_GtmPoolStatCnameResolutions_Type = Counter64
_GtmPoolStatCnameResolutions_Object = MibTableColumn
gtmPoolStatCnameResolutions = _GtmPoolStatCnameResolutions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 2, 3, 1, 9),
    _GtmPoolStatCnameResolutions_Type()
)
gtmPoolStatCnameResolutions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolStatCnameResolutions.setStatus("current")
_GtmPoolStatus_ObjectIdentity = ObjectIdentity
gtmPoolStatus = _GtmPoolStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 3)
)
_GtmPoolStatusNumber_Type = Integer32
_GtmPoolStatusNumber_Object = MibScalar
gtmPoolStatusNumber = _GtmPoolStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 3, 1),
    _GtmPoolStatusNumber_Type()
)
gtmPoolStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolStatusNumber.setStatus("current")
_GtmPoolStatusTable_Object = MibTable
gtmPoolStatusTable = _GtmPoolStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 3, 2)
)
if mibBuilder.loadTexts:
    gtmPoolStatusTable.setStatus("current")
_GtmPoolStatusEntry_Object = MibTableRow
gtmPoolStatusEntry = _GtmPoolStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 3, 2, 1)
)
gtmPoolStatusEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmPoolStatusName"),
)
if mibBuilder.loadTexts:
    gtmPoolStatusEntry.setStatus("current")
_GtmPoolStatusName_Type = LongDisplayString
_GtmPoolStatusName_Object = MibTableColumn
gtmPoolStatusName = _GtmPoolStatusName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 3, 2, 1, 1),
    _GtmPoolStatusName_Type()
)
gtmPoolStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolStatusName.setStatus("current")


class _GtmPoolStatusAvailState_Type(Integer32):
    """Custom type gtmPoolStatusAvailState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blue", 4),
          ("gray", 5),
          ("green", 1),
          ("none", 0),
          ("red", 3),
          ("yellow", 2))
    )


_GtmPoolStatusAvailState_Type.__name__ = "Integer32"
_GtmPoolStatusAvailState_Object = MibTableColumn
gtmPoolStatusAvailState = _GtmPoolStatusAvailState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 3, 2, 1, 2),
    _GtmPoolStatusAvailState_Type()
)
gtmPoolStatusAvailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolStatusAvailState.setStatus("current")


class _GtmPoolStatusEnabledState_Type(Integer32):
    """Custom type gtmPoolStatusEnabledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("disabledbyparent", 3),
          ("enabled", 1),
          ("none", 0))
    )


_GtmPoolStatusEnabledState_Type.__name__ = "Integer32"
_GtmPoolStatusEnabledState_Object = MibTableColumn
gtmPoolStatusEnabledState = _GtmPoolStatusEnabledState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 3, 2, 1, 3),
    _GtmPoolStatusEnabledState_Type()
)
gtmPoolStatusEnabledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolStatusEnabledState.setStatus("current")
_GtmPoolStatusParentType_Type = Integer32
_GtmPoolStatusParentType_Object = MibTableColumn
gtmPoolStatusParentType = _GtmPoolStatusParentType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 3, 2, 1, 4),
    _GtmPoolStatusParentType_Type()
)
gtmPoolStatusParentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolStatusParentType.setStatus("deprecated")
_GtmPoolStatusDetailReason_Type = LongDisplayString
_GtmPoolStatusDetailReason_Object = MibTableColumn
gtmPoolStatusDetailReason = _GtmPoolStatusDetailReason_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 3, 2, 1, 5),
    _GtmPoolStatusDetailReason_Type()
)
gtmPoolStatusDetailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolStatusDetailReason.setStatus("current")
_GtmPoolMember_ObjectIdentity = ObjectIdentity
gtmPoolMember = _GtmPoolMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4)
)
_GtmPoolMbrNumber_Type = Integer32
_GtmPoolMbrNumber_Object = MibScalar
gtmPoolMbrNumber = _GtmPoolMbrNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 1),
    _GtmPoolMbrNumber_Type()
)
gtmPoolMbrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrNumber.setStatus("current")
_GtmPoolMbrTable_Object = MibTable
gtmPoolMbrTable = _GtmPoolMbrTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2)
)
if mibBuilder.loadTexts:
    gtmPoolMbrTable.setStatus("current")
_GtmPoolMbrEntry_Object = MibTableRow
gtmPoolMbrEntry = _GtmPoolMbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1)
)
gtmPoolMbrEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrPoolName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrServerName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrVsName"),
)
if mibBuilder.loadTexts:
    gtmPoolMbrEntry.setStatus("current")
_GtmPoolMbrPoolName_Type = LongDisplayString
_GtmPoolMbrPoolName_Object = MibTableColumn
gtmPoolMbrPoolName = _GtmPoolMbrPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 1),
    _GtmPoolMbrPoolName_Type()
)
gtmPoolMbrPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrPoolName.setStatus("current")
_GtmPoolMbrIpType_Type = InetAddressType
_GtmPoolMbrIpType_Object = MibTableColumn
gtmPoolMbrIpType = _GtmPoolMbrIpType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 2),
    _GtmPoolMbrIpType_Type()
)
gtmPoolMbrIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrIpType.setStatus("deprecated")
_GtmPoolMbrIp_Type = InetAddress
_GtmPoolMbrIp_Object = MibTableColumn
gtmPoolMbrIp = _GtmPoolMbrIp_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 3),
    _GtmPoolMbrIp_Type()
)
gtmPoolMbrIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrIp.setStatus("deprecated")
_GtmPoolMbrPort_Type = InetPortNumber
_GtmPoolMbrPort_Object = MibTableColumn
gtmPoolMbrPort = _GtmPoolMbrPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 4),
    _GtmPoolMbrPort_Type()
)
gtmPoolMbrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrPort.setStatus("deprecated")
_GtmPoolMbrVsName_Type = LongDisplayString
_GtmPoolMbrVsName_Object = MibTableColumn
gtmPoolMbrVsName = _GtmPoolMbrVsName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 5),
    _GtmPoolMbrVsName_Type()
)
gtmPoolMbrVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrVsName.setStatus("current")
_GtmPoolMbrOrder_Type = Integer32
_GtmPoolMbrOrder_Object = MibTableColumn
gtmPoolMbrOrder = _GtmPoolMbrOrder_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 6),
    _GtmPoolMbrOrder_Type()
)
gtmPoolMbrOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrOrder.setStatus("current")


class _GtmPoolMbrLimitCpuUsageEnabled_Type(Integer32):
    """Custom type gtmPoolMbrLimitCpuUsageEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmPoolMbrLimitCpuUsageEnabled_Type.__name__ = "Integer32"
_GtmPoolMbrLimitCpuUsageEnabled_Object = MibTableColumn
gtmPoolMbrLimitCpuUsageEnabled = _GtmPoolMbrLimitCpuUsageEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 7),
    _GtmPoolMbrLimitCpuUsageEnabled_Type()
)
gtmPoolMbrLimitCpuUsageEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrLimitCpuUsageEnabled.setStatus("current")


class _GtmPoolMbrLimitMemAvailEnabled_Type(Integer32):
    """Custom type gtmPoolMbrLimitMemAvailEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmPoolMbrLimitMemAvailEnabled_Type.__name__ = "Integer32"
_GtmPoolMbrLimitMemAvailEnabled_Object = MibTableColumn
gtmPoolMbrLimitMemAvailEnabled = _GtmPoolMbrLimitMemAvailEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 8),
    _GtmPoolMbrLimitMemAvailEnabled_Type()
)
gtmPoolMbrLimitMemAvailEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrLimitMemAvailEnabled.setStatus("current")


class _GtmPoolMbrLimitBitsPerSecEnabled_Type(Integer32):
    """Custom type gtmPoolMbrLimitBitsPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmPoolMbrLimitBitsPerSecEnabled_Type.__name__ = "Integer32"
_GtmPoolMbrLimitBitsPerSecEnabled_Object = MibTableColumn
gtmPoolMbrLimitBitsPerSecEnabled = _GtmPoolMbrLimitBitsPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 9),
    _GtmPoolMbrLimitBitsPerSecEnabled_Type()
)
gtmPoolMbrLimitBitsPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrLimitBitsPerSecEnabled.setStatus("current")


class _GtmPoolMbrLimitPktsPerSecEnabled_Type(Integer32):
    """Custom type gtmPoolMbrLimitPktsPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmPoolMbrLimitPktsPerSecEnabled_Type.__name__ = "Integer32"
_GtmPoolMbrLimitPktsPerSecEnabled_Object = MibTableColumn
gtmPoolMbrLimitPktsPerSecEnabled = _GtmPoolMbrLimitPktsPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 10),
    _GtmPoolMbrLimitPktsPerSecEnabled_Type()
)
gtmPoolMbrLimitPktsPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrLimitPktsPerSecEnabled.setStatus("current")


class _GtmPoolMbrLimitConnEnabled_Type(Integer32):
    """Custom type gtmPoolMbrLimitConnEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmPoolMbrLimitConnEnabled_Type.__name__ = "Integer32"
_GtmPoolMbrLimitConnEnabled_Object = MibTableColumn
gtmPoolMbrLimitConnEnabled = _GtmPoolMbrLimitConnEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 11),
    _GtmPoolMbrLimitConnEnabled_Type()
)
gtmPoolMbrLimitConnEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrLimitConnEnabled.setStatus("current")


class _GtmPoolMbrLimitConnPerSecEnabled_Type(Integer32):
    """Custom type gtmPoolMbrLimitConnPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmPoolMbrLimitConnPerSecEnabled_Type.__name__ = "Integer32"
_GtmPoolMbrLimitConnPerSecEnabled_Object = MibTableColumn
gtmPoolMbrLimitConnPerSecEnabled = _GtmPoolMbrLimitConnPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 12),
    _GtmPoolMbrLimitConnPerSecEnabled_Type()
)
gtmPoolMbrLimitConnPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrLimitConnPerSecEnabled.setStatus("deprecated")
_GtmPoolMbrLimitCpuUsage_Type = Counter64
_GtmPoolMbrLimitCpuUsage_Object = MibTableColumn
gtmPoolMbrLimitCpuUsage = _GtmPoolMbrLimitCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 13),
    _GtmPoolMbrLimitCpuUsage_Type()
)
gtmPoolMbrLimitCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrLimitCpuUsage.setStatus("current")
_GtmPoolMbrLimitMemAvail_Type = Counter64
_GtmPoolMbrLimitMemAvail_Object = MibTableColumn
gtmPoolMbrLimitMemAvail = _GtmPoolMbrLimitMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 14),
    _GtmPoolMbrLimitMemAvail_Type()
)
gtmPoolMbrLimitMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrLimitMemAvail.setStatus("current")
_GtmPoolMbrLimitBitsPerSec_Type = Counter64
_GtmPoolMbrLimitBitsPerSec_Object = MibTableColumn
gtmPoolMbrLimitBitsPerSec = _GtmPoolMbrLimitBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 15),
    _GtmPoolMbrLimitBitsPerSec_Type()
)
gtmPoolMbrLimitBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrLimitBitsPerSec.setStatus("current")
_GtmPoolMbrLimitPktsPerSec_Type = Counter64
_GtmPoolMbrLimitPktsPerSec_Object = MibTableColumn
gtmPoolMbrLimitPktsPerSec = _GtmPoolMbrLimitPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 16),
    _GtmPoolMbrLimitPktsPerSec_Type()
)
gtmPoolMbrLimitPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrLimitPktsPerSec.setStatus("current")
_GtmPoolMbrLimitConn_Type = Counter64
_GtmPoolMbrLimitConn_Object = MibTableColumn
gtmPoolMbrLimitConn = _GtmPoolMbrLimitConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 17),
    _GtmPoolMbrLimitConn_Type()
)
gtmPoolMbrLimitConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrLimitConn.setStatus("current")
_GtmPoolMbrLimitConnPerSec_Type = Counter64
_GtmPoolMbrLimitConnPerSec_Object = MibTableColumn
gtmPoolMbrLimitConnPerSec = _GtmPoolMbrLimitConnPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 18),
    _GtmPoolMbrLimitConnPerSec_Type()
)
gtmPoolMbrLimitConnPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrLimitConnPerSec.setStatus("deprecated")
_GtmPoolMbrMonitorRule_Type = LongDisplayString
_GtmPoolMbrMonitorRule_Object = MibTableColumn
gtmPoolMbrMonitorRule = _GtmPoolMbrMonitorRule_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 19),
    _GtmPoolMbrMonitorRule_Type()
)
gtmPoolMbrMonitorRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrMonitorRule.setStatus("current")


class _GtmPoolMbrEnabled_Type(Integer32):
    """Custom type gtmPoolMbrEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_GtmPoolMbrEnabled_Type.__name__ = "Integer32"
_GtmPoolMbrEnabled_Object = MibTableColumn
gtmPoolMbrEnabled = _GtmPoolMbrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 20),
    _GtmPoolMbrEnabled_Type()
)
gtmPoolMbrEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrEnabled.setStatus("current")
_GtmPoolMbrRatio_Type = Integer32
_GtmPoolMbrRatio_Object = MibTableColumn
gtmPoolMbrRatio = _GtmPoolMbrRatio_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 21),
    _GtmPoolMbrRatio_Type()
)
gtmPoolMbrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrRatio.setStatus("current")
_GtmPoolMbrServerName_Type = LongDisplayString
_GtmPoolMbrServerName_Object = MibTableColumn
gtmPoolMbrServerName = _GtmPoolMbrServerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 4, 2, 1, 22),
    _GtmPoolMbrServerName_Type()
)
gtmPoolMbrServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrServerName.setStatus("current")
_GtmPoolMemberDepends_ObjectIdentity = ObjectIdentity
gtmPoolMemberDepends = _GtmPoolMemberDepends_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 5)
)
_GtmPoolMbrDepsNumber_Type = Integer32
_GtmPoolMbrDepsNumber_Object = MibScalar
gtmPoolMbrDepsNumber = _GtmPoolMbrDepsNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 5, 1),
    _GtmPoolMbrDepsNumber_Type()
)
gtmPoolMbrDepsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrDepsNumber.setStatus("current")
_GtmPoolMbrDepsTable_Object = MibTable
gtmPoolMbrDepsTable = _GtmPoolMbrDepsTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 5, 2)
)
if mibBuilder.loadTexts:
    gtmPoolMbrDepsTable.setStatus("current")
_GtmPoolMbrDepsEntry_Object = MibTableRow
gtmPoolMbrDepsEntry = _GtmPoolMbrDepsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 5, 2, 1)
)
gtmPoolMbrDepsEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrDepsServerName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrDepsVsName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrDepsPoolName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrDepsDependServerName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrDepsDependVsName"),
)
if mibBuilder.loadTexts:
    gtmPoolMbrDepsEntry.setStatus("current")
_GtmPoolMbrDepsIpType_Type = InetAddressType
_GtmPoolMbrDepsIpType_Object = MibTableColumn
gtmPoolMbrDepsIpType = _GtmPoolMbrDepsIpType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 5, 2, 1, 1),
    _GtmPoolMbrDepsIpType_Type()
)
gtmPoolMbrDepsIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrDepsIpType.setStatus("deprecated")
_GtmPoolMbrDepsIp_Type = InetAddress
_GtmPoolMbrDepsIp_Object = MibTableColumn
gtmPoolMbrDepsIp = _GtmPoolMbrDepsIp_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 5, 2, 1, 2),
    _GtmPoolMbrDepsIp_Type()
)
gtmPoolMbrDepsIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrDepsIp.setStatus("deprecated")
_GtmPoolMbrDepsPort_Type = InetPortNumber
_GtmPoolMbrDepsPort_Object = MibTableColumn
gtmPoolMbrDepsPort = _GtmPoolMbrDepsPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 5, 2, 1, 3),
    _GtmPoolMbrDepsPort_Type()
)
gtmPoolMbrDepsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrDepsPort.setStatus("deprecated")
_GtmPoolMbrDepsPoolName_Type = LongDisplayString
_GtmPoolMbrDepsPoolName_Object = MibTableColumn
gtmPoolMbrDepsPoolName = _GtmPoolMbrDepsPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 5, 2, 1, 4),
    _GtmPoolMbrDepsPoolName_Type()
)
gtmPoolMbrDepsPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrDepsPoolName.setStatus("current")
_GtmPoolMbrDepsVipType_Type = InetAddressType
_GtmPoolMbrDepsVipType_Object = MibTableColumn
gtmPoolMbrDepsVipType = _GtmPoolMbrDepsVipType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 5, 2, 1, 5),
    _GtmPoolMbrDepsVipType_Type()
)
gtmPoolMbrDepsVipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrDepsVipType.setStatus("deprecated")
_GtmPoolMbrDepsVip_Type = InetAddress
_GtmPoolMbrDepsVip_Object = MibTableColumn
gtmPoolMbrDepsVip = _GtmPoolMbrDepsVip_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 5, 2, 1, 6),
    _GtmPoolMbrDepsVip_Type()
)
gtmPoolMbrDepsVip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrDepsVip.setStatus("deprecated")
_GtmPoolMbrDepsVport_Type = InetPortNumber
_GtmPoolMbrDepsVport_Object = MibTableColumn
gtmPoolMbrDepsVport = _GtmPoolMbrDepsVport_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 5, 2, 1, 7),
    _GtmPoolMbrDepsVport_Type()
)
gtmPoolMbrDepsVport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrDepsVport.setStatus("deprecated")
_GtmPoolMbrDepsServerName_Type = LongDisplayString
_GtmPoolMbrDepsServerName_Object = MibTableColumn
gtmPoolMbrDepsServerName = _GtmPoolMbrDepsServerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 5, 2, 1, 8),
    _GtmPoolMbrDepsServerName_Type()
)
gtmPoolMbrDepsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrDepsServerName.setStatus("current")
_GtmPoolMbrDepsVsName_Type = LongDisplayString
_GtmPoolMbrDepsVsName_Object = MibTableColumn
gtmPoolMbrDepsVsName = _GtmPoolMbrDepsVsName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 5, 2, 1, 9),
    _GtmPoolMbrDepsVsName_Type()
)
gtmPoolMbrDepsVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrDepsVsName.setStatus("current")
_GtmPoolMbrDepsDependServerName_Type = LongDisplayString
_GtmPoolMbrDepsDependServerName_Object = MibTableColumn
gtmPoolMbrDepsDependServerName = _GtmPoolMbrDepsDependServerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 5, 2, 1, 10),
    _GtmPoolMbrDepsDependServerName_Type()
)
gtmPoolMbrDepsDependServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrDepsDependServerName.setStatus("current")
_GtmPoolMbrDepsDependVsName_Type = LongDisplayString
_GtmPoolMbrDepsDependVsName_Object = MibTableColumn
gtmPoolMbrDepsDependVsName = _GtmPoolMbrDepsDependVsName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 5, 2, 1, 11),
    _GtmPoolMbrDepsDependVsName_Type()
)
gtmPoolMbrDepsDependVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrDepsDependVsName.setStatus("current")
_GtmPoolMemberStat_ObjectIdentity = ObjectIdentity
gtmPoolMemberStat = _GtmPoolMemberStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 6)
)
_GtmPoolMbrStatResetStats_Type = Integer32
_GtmPoolMbrStatResetStats_Object = MibScalar
gtmPoolMbrStatResetStats = _GtmPoolMbrStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 6, 1),
    _GtmPoolMbrStatResetStats_Type()
)
gtmPoolMbrStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtmPoolMbrStatResetStats.setStatus("current")
_GtmPoolMbrStatNumber_Type = Integer32
_GtmPoolMbrStatNumber_Object = MibScalar
gtmPoolMbrStatNumber = _GtmPoolMbrStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 6, 2),
    _GtmPoolMbrStatNumber_Type()
)
gtmPoolMbrStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatNumber.setStatus("current")
_GtmPoolMbrStatTable_Object = MibTable
gtmPoolMbrStatTable = _GtmPoolMbrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 6, 3)
)
if mibBuilder.loadTexts:
    gtmPoolMbrStatTable.setStatus("current")
_GtmPoolMbrStatEntry_Object = MibTableRow
gtmPoolMbrStatEntry = _GtmPoolMbrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 6, 3, 1)
)
gtmPoolMbrStatEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatPoolName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatServerName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatVsName"),
)
if mibBuilder.loadTexts:
    gtmPoolMbrStatEntry.setStatus("current")
_GtmPoolMbrStatPoolName_Type = LongDisplayString
_GtmPoolMbrStatPoolName_Object = MibTableColumn
gtmPoolMbrStatPoolName = _GtmPoolMbrStatPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 6, 3, 1, 1),
    _GtmPoolMbrStatPoolName_Type()
)
gtmPoolMbrStatPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatPoolName.setStatus("current")
_GtmPoolMbrStatIpType_Type = InetAddressType
_GtmPoolMbrStatIpType_Object = MibTableColumn
gtmPoolMbrStatIpType = _GtmPoolMbrStatIpType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 6, 3, 1, 2),
    _GtmPoolMbrStatIpType_Type()
)
gtmPoolMbrStatIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatIpType.setStatus("deprecated")
_GtmPoolMbrStatIp_Type = InetAddress
_GtmPoolMbrStatIp_Object = MibTableColumn
gtmPoolMbrStatIp = _GtmPoolMbrStatIp_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 6, 3, 1, 3),
    _GtmPoolMbrStatIp_Type()
)
gtmPoolMbrStatIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatIp.setStatus("deprecated")
_GtmPoolMbrStatPort_Type = InetPortNumber
_GtmPoolMbrStatPort_Object = MibTableColumn
gtmPoolMbrStatPort = _GtmPoolMbrStatPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 6, 3, 1, 4),
    _GtmPoolMbrStatPort_Type()
)
gtmPoolMbrStatPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatPort.setStatus("deprecated")
_GtmPoolMbrStatPreferred_Type = Counter64
_GtmPoolMbrStatPreferred_Object = MibTableColumn
gtmPoolMbrStatPreferred = _GtmPoolMbrStatPreferred_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 6, 3, 1, 5),
    _GtmPoolMbrStatPreferred_Type()
)
gtmPoolMbrStatPreferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatPreferred.setStatus("current")
_GtmPoolMbrStatAlternate_Type = Counter64
_GtmPoolMbrStatAlternate_Object = MibTableColumn
gtmPoolMbrStatAlternate = _GtmPoolMbrStatAlternate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 6, 3, 1, 6),
    _GtmPoolMbrStatAlternate_Type()
)
gtmPoolMbrStatAlternate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatAlternate.setStatus("current")
_GtmPoolMbrStatFallback_Type = Counter64
_GtmPoolMbrStatFallback_Object = MibTableColumn
gtmPoolMbrStatFallback = _GtmPoolMbrStatFallback_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 6, 3, 1, 7),
    _GtmPoolMbrStatFallback_Type()
)
gtmPoolMbrStatFallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatFallback.setStatus("current")
_GtmPoolMbrStatServerName_Type = LongDisplayString
_GtmPoolMbrStatServerName_Object = MibTableColumn
gtmPoolMbrStatServerName = _GtmPoolMbrStatServerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 6, 3, 1, 8),
    _GtmPoolMbrStatServerName_Type()
)
gtmPoolMbrStatServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatServerName.setStatus("current")
_GtmPoolMbrStatVsName_Type = LongDisplayString
_GtmPoolMbrStatVsName_Object = MibTableColumn
gtmPoolMbrStatVsName = _GtmPoolMbrStatVsName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 6, 3, 1, 9),
    _GtmPoolMbrStatVsName_Type()
)
gtmPoolMbrStatVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatVsName.setStatus("current")
_GtmPoolMemberStatus_ObjectIdentity = ObjectIdentity
gtmPoolMemberStatus = _GtmPoolMemberStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 7)
)
_GtmPoolMbrStatusNumber_Type = Integer32
_GtmPoolMbrStatusNumber_Object = MibScalar
gtmPoolMbrStatusNumber = _GtmPoolMbrStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 7, 1),
    _GtmPoolMbrStatusNumber_Type()
)
gtmPoolMbrStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatusNumber.setStatus("current")
_GtmPoolMbrStatusTable_Object = MibTable
gtmPoolMbrStatusTable = _GtmPoolMbrStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 7, 2)
)
if mibBuilder.loadTexts:
    gtmPoolMbrStatusTable.setStatus("current")
_GtmPoolMbrStatusEntry_Object = MibTableRow
gtmPoolMbrStatusEntry = _GtmPoolMbrStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 7, 2, 1)
)
gtmPoolMbrStatusEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatusPoolName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatusServerName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatusVsName"),
)
if mibBuilder.loadTexts:
    gtmPoolMbrStatusEntry.setStatus("current")
_GtmPoolMbrStatusPoolName_Type = LongDisplayString
_GtmPoolMbrStatusPoolName_Object = MibTableColumn
gtmPoolMbrStatusPoolName = _GtmPoolMbrStatusPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 7, 2, 1, 1),
    _GtmPoolMbrStatusPoolName_Type()
)
gtmPoolMbrStatusPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatusPoolName.setStatus("current")
_GtmPoolMbrStatusIpType_Type = InetAddressType
_GtmPoolMbrStatusIpType_Object = MibTableColumn
gtmPoolMbrStatusIpType = _GtmPoolMbrStatusIpType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 7, 2, 1, 2),
    _GtmPoolMbrStatusIpType_Type()
)
gtmPoolMbrStatusIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatusIpType.setStatus("deprecated")
_GtmPoolMbrStatusIp_Type = InetAddress
_GtmPoolMbrStatusIp_Object = MibTableColumn
gtmPoolMbrStatusIp = _GtmPoolMbrStatusIp_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 7, 2, 1, 3),
    _GtmPoolMbrStatusIp_Type()
)
gtmPoolMbrStatusIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatusIp.setStatus("deprecated")
_GtmPoolMbrStatusPort_Type = InetPortNumber
_GtmPoolMbrStatusPort_Object = MibTableColumn
gtmPoolMbrStatusPort = _GtmPoolMbrStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 7, 2, 1, 4),
    _GtmPoolMbrStatusPort_Type()
)
gtmPoolMbrStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatusPort.setStatus("deprecated")


class _GtmPoolMbrStatusAvailState_Type(Integer32):
    """Custom type gtmPoolMbrStatusAvailState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blue", 4),
          ("gray", 5),
          ("green", 1),
          ("none", 0),
          ("red", 3),
          ("yellow", 2))
    )


_GtmPoolMbrStatusAvailState_Type.__name__ = "Integer32"
_GtmPoolMbrStatusAvailState_Object = MibTableColumn
gtmPoolMbrStatusAvailState = _GtmPoolMbrStatusAvailState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 7, 2, 1, 5),
    _GtmPoolMbrStatusAvailState_Type()
)
gtmPoolMbrStatusAvailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatusAvailState.setStatus("current")


class _GtmPoolMbrStatusEnabledState_Type(Integer32):
    """Custom type gtmPoolMbrStatusEnabledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("disabledbyparent", 3),
          ("enabled", 1),
          ("none", 0))
    )


_GtmPoolMbrStatusEnabledState_Type.__name__ = "Integer32"
_GtmPoolMbrStatusEnabledState_Object = MibTableColumn
gtmPoolMbrStatusEnabledState = _GtmPoolMbrStatusEnabledState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 7, 2, 1, 6),
    _GtmPoolMbrStatusEnabledState_Type()
)
gtmPoolMbrStatusEnabledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatusEnabledState.setStatus("current")
_GtmPoolMbrStatusParentType_Type = Integer32
_GtmPoolMbrStatusParentType_Object = MibTableColumn
gtmPoolMbrStatusParentType = _GtmPoolMbrStatusParentType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 7, 2, 1, 7),
    _GtmPoolMbrStatusParentType_Type()
)
gtmPoolMbrStatusParentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatusParentType.setStatus("deprecated")
_GtmPoolMbrStatusDetailReason_Type = LongDisplayString
_GtmPoolMbrStatusDetailReason_Object = MibTableColumn
gtmPoolMbrStatusDetailReason = _GtmPoolMbrStatusDetailReason_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 7, 2, 1, 8),
    _GtmPoolMbrStatusDetailReason_Type()
)
gtmPoolMbrStatusDetailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatusDetailReason.setStatus("current")
_GtmPoolMbrStatusVsName_Type = LongDisplayString
_GtmPoolMbrStatusVsName_Object = MibTableColumn
gtmPoolMbrStatusVsName = _GtmPoolMbrStatusVsName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 7, 2, 1, 9),
    _GtmPoolMbrStatusVsName_Type()
)
gtmPoolMbrStatusVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatusVsName.setStatus("current")
_GtmPoolMbrStatusServerName_Type = LongDisplayString
_GtmPoolMbrStatusServerName_Object = MibTableColumn
gtmPoolMbrStatusServerName = _GtmPoolMbrStatusServerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 6, 7, 2, 1, 10),
    _GtmPoolMbrStatusServerName_Type()
)
gtmPoolMbrStatusServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmPoolMbrStatusServerName.setStatus("current")
_GtmRegions_ObjectIdentity = ObjectIdentity
gtmRegions = _GtmRegions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 7)
)
_GtmRegionEntry_ObjectIdentity = ObjectIdentity
gtmRegionEntry = _GtmRegionEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 7, 1)
)
_GtmRegionEntryNumber_Type = Integer32
_GtmRegionEntryNumber_Object = MibScalar
gtmRegionEntryNumber = _GtmRegionEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 7, 1, 1),
    _GtmRegionEntryNumber_Type()
)
gtmRegionEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRegionEntryNumber.setStatus("current")
_GtmRegionEntryTable_Object = MibTable
gtmRegionEntryTable = _GtmRegionEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 7, 1, 2)
)
if mibBuilder.loadTexts:
    gtmRegionEntryTable.setStatus("current")
_GtmRegionEntryEntry_Object = MibTableRow
gtmRegionEntryEntry = _GtmRegionEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 7, 1, 2, 1)
)
gtmRegionEntryEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmRegionEntryName"),
)
if mibBuilder.loadTexts:
    gtmRegionEntryEntry.setStatus("current")
_GtmRegionEntryName_Type = LongDisplayString
_GtmRegionEntryName_Object = MibTableColumn
gtmRegionEntryName = _GtmRegionEntryName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 7, 1, 2, 1, 1),
    _GtmRegionEntryName_Type()
)
gtmRegionEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRegionEntryName.setStatus("current")


class _GtmRegionEntryRegionDbType_Type(Integer32):
    """Custom type gtmRegionEntryRegionDbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acl", 1),
          ("isp", 2),
          ("user", 0))
    )


_GtmRegionEntryRegionDbType_Type.__name__ = "Integer32"
_GtmRegionEntryRegionDbType_Object = MibTableColumn
gtmRegionEntryRegionDbType = _GtmRegionEntryRegionDbType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 7, 1, 2, 1, 2),
    _GtmRegionEntryRegionDbType_Type()
)
gtmRegionEntryRegionDbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRegionEntryRegionDbType.setStatus("current")
_GtmRegItem_ObjectIdentity = ObjectIdentity
gtmRegItem = _GtmRegItem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 7, 2)
)
_GtmRegItemNumber_Type = Integer32
_GtmRegItemNumber_Object = MibScalar
gtmRegItemNumber = _GtmRegItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 7, 2, 1),
    _GtmRegItemNumber_Type()
)
gtmRegItemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRegItemNumber.setStatus("current")
_GtmRegItemTable_Object = MibTable
gtmRegItemTable = _GtmRegItemTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 7, 2, 2)
)
if mibBuilder.loadTexts:
    gtmRegItemTable.setStatus("current")
_GtmRegItemEntry_Object = MibTableRow
gtmRegItemEntry = _GtmRegItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 7, 2, 2, 1)
)
gtmRegItemEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmRegItemRegionDbType"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmRegItemRegionName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmRegItemType"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmRegItemNegate"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmRegItemRegEntry"),
)
if mibBuilder.loadTexts:
    gtmRegItemEntry.setStatus("current")


class _GtmRegItemRegionDbType_Type(Integer32):
    """Custom type gtmRegItemRegionDbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acl", 1),
          ("isp", 2),
          ("user", 0))
    )


_GtmRegItemRegionDbType_Type.__name__ = "Integer32"
_GtmRegItemRegionDbType_Object = MibTableColumn
gtmRegItemRegionDbType = _GtmRegItemRegionDbType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 7, 2, 2, 1, 1),
    _GtmRegItemRegionDbType_Type()
)
gtmRegItemRegionDbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRegItemRegionDbType.setStatus("current")
_GtmRegItemRegionName_Type = LongDisplayString
_GtmRegItemRegionName_Object = MibTableColumn
gtmRegItemRegionName = _GtmRegItemRegionName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 7, 2, 2, 1, 2),
    _GtmRegItemRegionName_Type()
)
gtmRegItemRegionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRegItemRegionName.setStatus("current")


class _GtmRegItemType_Type(Integer32):
    """Custom type gtmRegItemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cidr", 0),
          ("continent", 2),
          ("country", 3),
          ("datacenter", 6),
          ("geoip-isp", 8),
          ("ispregion", 7),
          ("pool", 5),
          ("region", 1),
          ("state", 4))
    )


_GtmRegItemType_Type.__name__ = "Integer32"
_GtmRegItemType_Object = MibTableColumn
gtmRegItemType = _GtmRegItemType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 7, 2, 2, 1, 3),
    _GtmRegItemType_Type()
)
gtmRegItemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRegItemType.setStatus("current")


class _GtmRegItemNegate_Type(Integer32):
    """Custom type gtmRegItemNegate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmRegItemNegate_Type.__name__ = "Integer32"
_GtmRegItemNegate_Object = MibTableColumn
gtmRegItemNegate = _GtmRegItemNegate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 7, 2, 2, 1, 4),
    _GtmRegItemNegate_Type()
)
gtmRegItemNegate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRegItemNegate.setStatus("current")
_GtmRegItemRegEntry_Type = LongDisplayString
_GtmRegItemRegEntry_Object = MibTableColumn
gtmRegItemRegEntry = _GtmRegItemRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 7, 2, 2, 1, 5),
    _GtmRegItemRegEntry_Type()
)
gtmRegItemRegEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRegItemRegEntry.setStatus("current")
_GtmRules_ObjectIdentity = ObjectIdentity
gtmRules = _GtmRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8)
)
_GtmRule_ObjectIdentity = ObjectIdentity
gtmRule = _GtmRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 1)
)
_GtmRuleNumber_Type = Integer32
_GtmRuleNumber_Object = MibScalar
gtmRuleNumber = _GtmRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 1, 1),
    _GtmRuleNumber_Type()
)
gtmRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRuleNumber.setStatus("current")
_GtmRuleTable_Object = MibTable
gtmRuleTable = _GtmRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 1, 2)
)
if mibBuilder.loadTexts:
    gtmRuleTable.setStatus("current")
_GtmRuleEntry_Object = MibTableRow
gtmRuleEntry = _GtmRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 1, 2, 1)
)
gtmRuleEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmRuleName"),
)
if mibBuilder.loadTexts:
    gtmRuleEntry.setStatus("current")
_GtmRuleName_Type = LongDisplayString
_GtmRuleName_Object = MibTableColumn
gtmRuleName = _GtmRuleName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 1, 2, 1, 1),
    _GtmRuleName_Type()
)
gtmRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRuleName.setStatus("current")
_GtmRuleDefinition_Type = LongDisplayString
_GtmRuleDefinition_Object = MibTableColumn
gtmRuleDefinition = _GtmRuleDefinition_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 1, 2, 1, 2),
    _GtmRuleDefinition_Type()
)
gtmRuleDefinition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRuleDefinition.setStatus("deprecated")


class _GtmRuleConfigSource_Type(Integer32):
    """Custom type gtmRuleConfigSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("basecfg", 1),
          ("usercfg", 0))
    )


_GtmRuleConfigSource_Type.__name__ = "Integer32"
_GtmRuleConfigSource_Object = MibTableColumn
gtmRuleConfigSource = _GtmRuleConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 1, 2, 1, 3),
    _GtmRuleConfigSource_Type()
)
gtmRuleConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRuleConfigSource.setStatus("current")
_GtmRuleEvent_ObjectIdentity = ObjectIdentity
gtmRuleEvent = _GtmRuleEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 2)
)
_GtmRuleEventNumber_Type = Integer32
_GtmRuleEventNumber_Object = MibScalar
gtmRuleEventNumber = _GtmRuleEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 2, 1),
    _GtmRuleEventNumber_Type()
)
gtmRuleEventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRuleEventNumber.setStatus("current")
_GtmRuleEventTable_Object = MibTable
gtmRuleEventTable = _GtmRuleEventTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 2, 2)
)
if mibBuilder.loadTexts:
    gtmRuleEventTable.setStatus("current")
_GtmRuleEventEntry_Object = MibTableRow
gtmRuleEventEntry = _GtmRuleEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 2, 2, 1)
)
gtmRuleEventEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmRuleEventName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmRuleEventEventType"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmRuleEventPriority"),
)
if mibBuilder.loadTexts:
    gtmRuleEventEntry.setStatus("current")
_GtmRuleEventName_Type = LongDisplayString
_GtmRuleEventName_Object = MibTableColumn
gtmRuleEventName = _GtmRuleEventName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 2, 2, 1, 1),
    _GtmRuleEventName_Type()
)
gtmRuleEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRuleEventName.setStatus("current")
_GtmRuleEventEventType_Type = LongDisplayString
_GtmRuleEventEventType_Object = MibTableColumn
gtmRuleEventEventType = _GtmRuleEventEventType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 2, 2, 1, 2),
    _GtmRuleEventEventType_Type()
)
gtmRuleEventEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRuleEventEventType.setStatus("current")


class _GtmRuleEventPriority_Type(Integer32):
    """Custom type gtmRuleEventPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_GtmRuleEventPriority_Type.__name__ = "Integer32"
_GtmRuleEventPriority_Object = MibTableColumn
gtmRuleEventPriority = _GtmRuleEventPriority_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 2, 2, 1, 3),
    _GtmRuleEventPriority_Type()
)
gtmRuleEventPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRuleEventPriority.setStatus("current")
_GtmRuleEventScript_Type = LongDisplayString
_GtmRuleEventScript_Object = MibTableColumn
gtmRuleEventScript = _GtmRuleEventScript_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 2, 2, 1, 4),
    _GtmRuleEventScript_Type()
)
gtmRuleEventScript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRuleEventScript.setStatus("deprecated")
_GtmRuleEventStat_ObjectIdentity = ObjectIdentity
gtmRuleEventStat = _GtmRuleEventStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 3)
)
_GtmRuleEventStatResetStats_Type = Integer32
_GtmRuleEventStatResetStats_Object = MibScalar
gtmRuleEventStatResetStats = _GtmRuleEventStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 3, 1),
    _GtmRuleEventStatResetStats_Type()
)
gtmRuleEventStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtmRuleEventStatResetStats.setStatus("current")
_GtmRuleEventStatNumber_Type = Integer32
_GtmRuleEventStatNumber_Object = MibScalar
gtmRuleEventStatNumber = _GtmRuleEventStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 3, 2),
    _GtmRuleEventStatNumber_Type()
)
gtmRuleEventStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRuleEventStatNumber.setStatus("current")
_GtmRuleEventStatTable_Object = MibTable
gtmRuleEventStatTable = _GtmRuleEventStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 3, 3)
)
if mibBuilder.loadTexts:
    gtmRuleEventStatTable.setStatus("current")
_GtmRuleEventStatEntry_Object = MibTableRow
gtmRuleEventStatEntry = _GtmRuleEventStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 3, 3, 1)
)
gtmRuleEventStatEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmRuleEventStatName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmRuleEventStatEventType"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmRuleEventStatPriority"),
)
if mibBuilder.loadTexts:
    gtmRuleEventStatEntry.setStatus("current")
_GtmRuleEventStatName_Type = LongDisplayString
_GtmRuleEventStatName_Object = MibTableColumn
gtmRuleEventStatName = _GtmRuleEventStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 3, 3, 1, 1),
    _GtmRuleEventStatName_Type()
)
gtmRuleEventStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRuleEventStatName.setStatus("current")
_GtmRuleEventStatEventType_Type = LongDisplayString
_GtmRuleEventStatEventType_Object = MibTableColumn
gtmRuleEventStatEventType = _GtmRuleEventStatEventType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 3, 3, 1, 2),
    _GtmRuleEventStatEventType_Type()
)
gtmRuleEventStatEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRuleEventStatEventType.setStatus("current")


class _GtmRuleEventStatPriority_Type(Integer32):
    """Custom type gtmRuleEventStatPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_GtmRuleEventStatPriority_Type.__name__ = "Integer32"
_GtmRuleEventStatPriority_Object = MibTableColumn
gtmRuleEventStatPriority = _GtmRuleEventStatPriority_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 3, 3, 1, 3),
    _GtmRuleEventStatPriority_Type()
)
gtmRuleEventStatPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRuleEventStatPriority.setStatus("current")
_GtmRuleEventStatFailures_Type = Counter64
_GtmRuleEventStatFailures_Object = MibTableColumn
gtmRuleEventStatFailures = _GtmRuleEventStatFailures_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 3, 3, 1, 4),
    _GtmRuleEventStatFailures_Type()
)
gtmRuleEventStatFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRuleEventStatFailures.setStatus("current")
_GtmRuleEventStatAborts_Type = Counter64
_GtmRuleEventStatAborts_Object = MibTableColumn
gtmRuleEventStatAborts = _GtmRuleEventStatAborts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 3, 3, 1, 5),
    _GtmRuleEventStatAborts_Type()
)
gtmRuleEventStatAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRuleEventStatAborts.setStatus("current")
_GtmRuleEventStatTotalExecutions_Type = Counter64
_GtmRuleEventStatTotalExecutions_Object = MibTableColumn
gtmRuleEventStatTotalExecutions = _GtmRuleEventStatTotalExecutions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 8, 3, 3, 1, 6),
    _GtmRuleEventStatTotalExecutions_Type()
)
gtmRuleEventStatTotalExecutions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmRuleEventStatTotalExecutions.setStatus("current")
_GtmServers_ObjectIdentity = ObjectIdentity
gtmServers = _GtmServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9)
)
_GtmServer_ObjectIdentity = ObjectIdentity
gtmServer = _GtmServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1)
)
_GtmServerNumber_Type = Integer32
_GtmServerNumber_Object = MibScalar
gtmServerNumber = _GtmServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 1),
    _GtmServerNumber_Type()
)
gtmServerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerNumber.setStatus("current")
_GtmServerTable_Object = MibTable
gtmServerTable = _GtmServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2)
)
if mibBuilder.loadTexts:
    gtmServerTable.setStatus("current")
_GtmServerEntry_Object = MibTableRow
gtmServerEntry = _GtmServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1)
)
gtmServerEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmServerName"),
)
if mibBuilder.loadTexts:
    gtmServerEntry.setStatus("current")
_GtmServerName_Type = LongDisplayString
_GtmServerName_Object = MibTableColumn
gtmServerName = _GtmServerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 1),
    _GtmServerName_Type()
)
gtmServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerName.setStatus("current")
_GtmServerDcName_Type = LongDisplayString
_GtmServerDcName_Object = MibTableColumn
gtmServerDcName = _GtmServerDcName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 2),
    _GtmServerDcName_Type()
)
gtmServerDcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerDcName.setStatus("current")


class _GtmServerType_Type(Integer32):
    """Custom type gtmServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("alteonacedirector", 3),
          ("bigipredundant", 1),
          ("bigipstandalone", 0),
          ("cacheflow", 11),
          ("ciscocss", 4),
          ("ciscolocaldirectorv2", 5),
          ("ciscolocaldirectorv3", 6),
          ("ciscoserverloadbalancer", 7),
          ("extreme", 8),
          ("foundryserveriron", 9),
          ("generichost", 10),
          ("genericloadbalancer", 2),
          ("netapp", 12),
          ("radware", 16),
          ("solaris", 15),
          ("windows2000", 13),
          ("windowsnt4", 14))
    )


_GtmServerType_Type.__name__ = "Integer32"
_GtmServerType_Object = MibTableColumn
gtmServerType = _GtmServerType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 3),
    _GtmServerType_Type()
)
gtmServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerType.setStatus("current")


class _GtmServerEnabled_Type(Integer32):
    """Custom type gtmServerEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmServerEnabled_Type.__name__ = "Integer32"
_GtmServerEnabled_Object = MibTableColumn
gtmServerEnabled = _GtmServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 4),
    _GtmServerEnabled_Type()
)
gtmServerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerEnabled.setStatus("current")


class _GtmServerLimitCpuUsageEnabled_Type(Integer32):
    """Custom type gtmServerLimitCpuUsageEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmServerLimitCpuUsageEnabled_Type.__name__ = "Integer32"
_GtmServerLimitCpuUsageEnabled_Object = MibTableColumn
gtmServerLimitCpuUsageEnabled = _GtmServerLimitCpuUsageEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 5),
    _GtmServerLimitCpuUsageEnabled_Type()
)
gtmServerLimitCpuUsageEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerLimitCpuUsageEnabled.setStatus("current")


class _GtmServerLimitMemAvailEnabled_Type(Integer32):
    """Custom type gtmServerLimitMemAvailEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmServerLimitMemAvailEnabled_Type.__name__ = "Integer32"
_GtmServerLimitMemAvailEnabled_Object = MibTableColumn
gtmServerLimitMemAvailEnabled = _GtmServerLimitMemAvailEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 6),
    _GtmServerLimitMemAvailEnabled_Type()
)
gtmServerLimitMemAvailEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerLimitMemAvailEnabled.setStatus("current")


class _GtmServerLimitBitsPerSecEnabled_Type(Integer32):
    """Custom type gtmServerLimitBitsPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmServerLimitBitsPerSecEnabled_Type.__name__ = "Integer32"
_GtmServerLimitBitsPerSecEnabled_Object = MibTableColumn
gtmServerLimitBitsPerSecEnabled = _GtmServerLimitBitsPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 7),
    _GtmServerLimitBitsPerSecEnabled_Type()
)
gtmServerLimitBitsPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerLimitBitsPerSecEnabled.setStatus("current")


class _GtmServerLimitPktsPerSecEnabled_Type(Integer32):
    """Custom type gtmServerLimitPktsPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmServerLimitPktsPerSecEnabled_Type.__name__ = "Integer32"
_GtmServerLimitPktsPerSecEnabled_Object = MibTableColumn
gtmServerLimitPktsPerSecEnabled = _GtmServerLimitPktsPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 8),
    _GtmServerLimitPktsPerSecEnabled_Type()
)
gtmServerLimitPktsPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerLimitPktsPerSecEnabled.setStatus("current")


class _GtmServerLimitConnEnabled_Type(Integer32):
    """Custom type gtmServerLimitConnEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmServerLimitConnEnabled_Type.__name__ = "Integer32"
_GtmServerLimitConnEnabled_Object = MibTableColumn
gtmServerLimitConnEnabled = _GtmServerLimitConnEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 9),
    _GtmServerLimitConnEnabled_Type()
)
gtmServerLimitConnEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerLimitConnEnabled.setStatus("current")


class _GtmServerLimitConnPerSecEnabled_Type(Integer32):
    """Custom type gtmServerLimitConnPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmServerLimitConnPerSecEnabled_Type.__name__ = "Integer32"
_GtmServerLimitConnPerSecEnabled_Object = MibTableColumn
gtmServerLimitConnPerSecEnabled = _GtmServerLimitConnPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 10),
    _GtmServerLimitConnPerSecEnabled_Type()
)
gtmServerLimitConnPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerLimitConnPerSecEnabled.setStatus("deprecated")
_GtmServerLimitCpuUsage_Type = Counter64
_GtmServerLimitCpuUsage_Object = MibTableColumn
gtmServerLimitCpuUsage = _GtmServerLimitCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 11),
    _GtmServerLimitCpuUsage_Type()
)
gtmServerLimitCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerLimitCpuUsage.setStatus("current")
_GtmServerLimitMemAvail_Type = Counter64
_GtmServerLimitMemAvail_Object = MibTableColumn
gtmServerLimitMemAvail = _GtmServerLimitMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 12),
    _GtmServerLimitMemAvail_Type()
)
gtmServerLimitMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerLimitMemAvail.setStatus("current")
_GtmServerLimitBitsPerSec_Type = Counter64
_GtmServerLimitBitsPerSec_Object = MibTableColumn
gtmServerLimitBitsPerSec = _GtmServerLimitBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 13),
    _GtmServerLimitBitsPerSec_Type()
)
gtmServerLimitBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerLimitBitsPerSec.setStatus("current")
_GtmServerLimitPktsPerSec_Type = Counter64
_GtmServerLimitPktsPerSec_Object = MibTableColumn
gtmServerLimitPktsPerSec = _GtmServerLimitPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 14),
    _GtmServerLimitPktsPerSec_Type()
)
gtmServerLimitPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerLimitPktsPerSec.setStatus("current")
_GtmServerLimitConn_Type = Counter64
_GtmServerLimitConn_Object = MibTableColumn
gtmServerLimitConn = _GtmServerLimitConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 15),
    _GtmServerLimitConn_Type()
)
gtmServerLimitConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerLimitConn.setStatus("current")
_GtmServerLimitConnPerSec_Type = Counter64
_GtmServerLimitConnPerSec_Object = MibTableColumn
gtmServerLimitConnPerSec = _GtmServerLimitConnPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 16),
    _GtmServerLimitConnPerSec_Type()
)
gtmServerLimitConnPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerLimitConnPerSec.setStatus("deprecated")
_GtmServerProberType_Type = InetAddressType
_GtmServerProberType_Object = MibTableColumn
gtmServerProberType = _GtmServerProberType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 17),
    _GtmServerProberType_Type()
)
gtmServerProberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerProberType.setStatus("deprecated")
_GtmServerProber_Type = InetAddress
_GtmServerProber_Object = MibTableColumn
gtmServerProber = _GtmServerProber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 18),
    _GtmServerProber_Type()
)
gtmServerProber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerProber.setStatus("deprecated")
_GtmServerMonitorRule_Type = LongDisplayString
_GtmServerMonitorRule_Object = MibTableColumn
gtmServerMonitorRule = _GtmServerMonitorRule_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 19),
    _GtmServerMonitorRule_Type()
)
gtmServerMonitorRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerMonitorRule.setStatus("current")


class _GtmServerAllowSvcChk_Type(Integer32):
    """Custom type gtmServerAllowSvcChk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmServerAllowSvcChk_Type.__name__ = "Integer32"
_GtmServerAllowSvcChk_Object = MibTableColumn
gtmServerAllowSvcChk = _GtmServerAllowSvcChk_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 20),
    _GtmServerAllowSvcChk_Type()
)
gtmServerAllowSvcChk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerAllowSvcChk.setStatus("current")


class _GtmServerAllowPath_Type(Integer32):
    """Custom type gtmServerAllowPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmServerAllowPath_Type.__name__ = "Integer32"
_GtmServerAllowPath_Object = MibTableColumn
gtmServerAllowPath = _GtmServerAllowPath_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 21),
    _GtmServerAllowPath_Type()
)
gtmServerAllowPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerAllowPath.setStatus("current")


class _GtmServerAllowSnmp_Type(Integer32):
    """Custom type gtmServerAllowSnmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmServerAllowSnmp_Type.__name__ = "Integer32"
_GtmServerAllowSnmp_Object = MibTableColumn
gtmServerAllowSnmp = _GtmServerAllowSnmp_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 22),
    _GtmServerAllowSnmp_Type()
)
gtmServerAllowSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerAllowSnmp.setStatus("current")


class _GtmServerAutoconfState_Type(Integer32):
    """Custom type gtmServerAutoconfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("enablednoautodelete", 2))
    )


_GtmServerAutoconfState_Type.__name__ = "Integer32"
_GtmServerAutoconfState_Object = MibTableColumn
gtmServerAutoconfState = _GtmServerAutoconfState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 23),
    _GtmServerAutoconfState_Type()
)
gtmServerAutoconfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerAutoconfState.setStatus("current")


class _GtmServerLinkAutoconfState_Type(Integer32):
    """Custom type gtmServerLinkAutoconfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("enablednoautodelete", 2))
    )


_GtmServerLinkAutoconfState_Type.__name__ = "Integer32"
_GtmServerLinkAutoconfState_Object = MibTableColumn
gtmServerLinkAutoconfState = _GtmServerLinkAutoconfState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 1, 2, 1, 24),
    _GtmServerLinkAutoconfState_Type()
)
gtmServerLinkAutoconfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerLinkAutoconfState.setStatus("current")
_GtmServerStat_ObjectIdentity = ObjectIdentity
gtmServerStat = _GtmServerStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 2)
)
_GtmServerStatResetStats_Type = Integer32
_GtmServerStatResetStats_Object = MibScalar
gtmServerStatResetStats = _GtmServerStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 2, 1),
    _GtmServerStatResetStats_Type()
)
gtmServerStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtmServerStatResetStats.setStatus("deprecated")
_GtmServerStatNumber_Type = Integer32
_GtmServerStatNumber_Object = MibScalar
gtmServerStatNumber = _GtmServerStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 2, 2),
    _GtmServerStatNumber_Type()
)
gtmServerStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatNumber.setStatus("deprecated")
_GtmServerStatTable_Object = MibTable
gtmServerStatTable = _GtmServerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 2, 3)
)
if mibBuilder.loadTexts:
    gtmServerStatTable.setStatus("deprecated")
_GtmServerStatEntry_Object = MibTableRow
gtmServerStatEntry = _GtmServerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 2, 3, 1)
)
gtmServerStatEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmServerStatName"),
)
if mibBuilder.loadTexts:
    gtmServerStatEntry.setStatus("deprecated")
_GtmServerStatName_Type = LongDisplayString
_GtmServerStatName_Object = MibTableColumn
gtmServerStatName = _GtmServerStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 2, 3, 1, 1),
    _GtmServerStatName_Type()
)
gtmServerStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatName.setStatus("deprecated")
_GtmServerStatUnitId_Type = Integer32
_GtmServerStatUnitId_Object = MibTableColumn
gtmServerStatUnitId = _GtmServerStatUnitId_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 2, 3, 1, 2),
    _GtmServerStatUnitId_Type()
)
gtmServerStatUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatUnitId.setStatus("deprecated")
_GtmServerStatVsPicks_Type = Counter64
_GtmServerStatVsPicks_Object = MibTableColumn
gtmServerStatVsPicks = _GtmServerStatVsPicks_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 2, 3, 1, 3),
    _GtmServerStatVsPicks_Type()
)
gtmServerStatVsPicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatVsPicks.setStatus("deprecated")
_GtmServerStatCpuUsage_Type = Counter64
_GtmServerStatCpuUsage_Object = MibTableColumn
gtmServerStatCpuUsage = _GtmServerStatCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 2, 3, 1, 4),
    _GtmServerStatCpuUsage_Type()
)
gtmServerStatCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatCpuUsage.setStatus("deprecated")
_GtmServerStatMemAvail_Type = Counter64
_GtmServerStatMemAvail_Object = MibTableColumn
gtmServerStatMemAvail = _GtmServerStatMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 2, 3, 1, 5),
    _GtmServerStatMemAvail_Type()
)
gtmServerStatMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatMemAvail.setStatus("deprecated")
_GtmServerStatBitsPerSecIn_Type = Counter64
_GtmServerStatBitsPerSecIn_Object = MibTableColumn
gtmServerStatBitsPerSecIn = _GtmServerStatBitsPerSecIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 2, 3, 1, 6),
    _GtmServerStatBitsPerSecIn_Type()
)
gtmServerStatBitsPerSecIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatBitsPerSecIn.setStatus("deprecated")
_GtmServerStatBitsPerSecOut_Type = Counter64
_GtmServerStatBitsPerSecOut_Object = MibTableColumn
gtmServerStatBitsPerSecOut = _GtmServerStatBitsPerSecOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 2, 3, 1, 7),
    _GtmServerStatBitsPerSecOut_Type()
)
gtmServerStatBitsPerSecOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatBitsPerSecOut.setStatus("deprecated")
_GtmServerStatPktsPerSecIn_Type = Counter64
_GtmServerStatPktsPerSecIn_Object = MibTableColumn
gtmServerStatPktsPerSecIn = _GtmServerStatPktsPerSecIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 2, 3, 1, 8),
    _GtmServerStatPktsPerSecIn_Type()
)
gtmServerStatPktsPerSecIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatPktsPerSecIn.setStatus("deprecated")
_GtmServerStatPktsPerSecOut_Type = Counter64
_GtmServerStatPktsPerSecOut_Object = MibTableColumn
gtmServerStatPktsPerSecOut = _GtmServerStatPktsPerSecOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 2, 3, 1, 9),
    _GtmServerStatPktsPerSecOut_Type()
)
gtmServerStatPktsPerSecOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatPktsPerSecOut.setStatus("deprecated")
_GtmServerStatConnections_Type = Counter64
_GtmServerStatConnections_Object = MibTableColumn
gtmServerStatConnections = _GtmServerStatConnections_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 2, 3, 1, 10),
    _GtmServerStatConnections_Type()
)
gtmServerStatConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatConnections.setStatus("deprecated")
_GtmServerStatConnRate_Type = Counter64
_GtmServerStatConnRate_Object = MibTableColumn
gtmServerStatConnRate = _GtmServerStatConnRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 2, 3, 1, 11),
    _GtmServerStatConnRate_Type()
)
gtmServerStatConnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatConnRate.setStatus("deprecated")
_GtmServerStatus_ObjectIdentity = ObjectIdentity
gtmServerStatus = _GtmServerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 3)
)
_GtmServerStatusNumber_Type = Integer32
_GtmServerStatusNumber_Object = MibScalar
gtmServerStatusNumber = _GtmServerStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 3, 1),
    _GtmServerStatusNumber_Type()
)
gtmServerStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatusNumber.setStatus("current")
_GtmServerStatusTable_Object = MibTable
gtmServerStatusTable = _GtmServerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 3, 2)
)
if mibBuilder.loadTexts:
    gtmServerStatusTable.setStatus("current")
_GtmServerStatusEntry_Object = MibTableRow
gtmServerStatusEntry = _GtmServerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 3, 2, 1)
)
gtmServerStatusEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmServerStatusName"),
)
if mibBuilder.loadTexts:
    gtmServerStatusEntry.setStatus("current")
_GtmServerStatusName_Type = LongDisplayString
_GtmServerStatusName_Object = MibTableColumn
gtmServerStatusName = _GtmServerStatusName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 3, 2, 1, 1),
    _GtmServerStatusName_Type()
)
gtmServerStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatusName.setStatus("current")


class _GtmServerStatusAvailState_Type(Integer32):
    """Custom type gtmServerStatusAvailState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blue", 4),
          ("gray", 5),
          ("green", 1),
          ("none", 0),
          ("red", 3),
          ("yellow", 2))
    )


_GtmServerStatusAvailState_Type.__name__ = "Integer32"
_GtmServerStatusAvailState_Object = MibTableColumn
gtmServerStatusAvailState = _GtmServerStatusAvailState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 3, 2, 1, 2),
    _GtmServerStatusAvailState_Type()
)
gtmServerStatusAvailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatusAvailState.setStatus("current")


class _GtmServerStatusEnabledState_Type(Integer32):
    """Custom type gtmServerStatusEnabledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("disabledbyparent", 3),
          ("enabled", 1),
          ("none", 0))
    )


_GtmServerStatusEnabledState_Type.__name__ = "Integer32"
_GtmServerStatusEnabledState_Object = MibTableColumn
gtmServerStatusEnabledState = _GtmServerStatusEnabledState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 3, 2, 1, 3),
    _GtmServerStatusEnabledState_Type()
)
gtmServerStatusEnabledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatusEnabledState.setStatus("current")
_GtmServerStatusParentType_Type = Integer32
_GtmServerStatusParentType_Object = MibTableColumn
gtmServerStatusParentType = _GtmServerStatusParentType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 3, 2, 1, 4),
    _GtmServerStatusParentType_Type()
)
gtmServerStatusParentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatusParentType.setStatus("deprecated")
_GtmServerStatusDetailReason_Type = LongDisplayString
_GtmServerStatusDetailReason_Object = MibTableColumn
gtmServerStatusDetailReason = _GtmServerStatusDetailReason_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 3, 2, 1, 5),
    _GtmServerStatusDetailReason_Type()
)
gtmServerStatusDetailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStatusDetailReason.setStatus("current")
_GtmServerStat2_ObjectIdentity = ObjectIdentity
gtmServerStat2 = _GtmServerStat2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 4)
)
_GtmServerStat2ResetStats_Type = Integer32
_GtmServerStat2ResetStats_Object = MibScalar
gtmServerStat2ResetStats = _GtmServerStat2ResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 4, 1),
    _GtmServerStat2ResetStats_Type()
)
gtmServerStat2ResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtmServerStat2ResetStats.setStatus("current")
_GtmServerStat2Number_Type = Integer32
_GtmServerStat2Number_Object = MibScalar
gtmServerStat2Number = _GtmServerStat2Number_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 4, 2),
    _GtmServerStat2Number_Type()
)
gtmServerStat2Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStat2Number.setStatus("current")
_GtmServerStat2Table_Object = MibTable
gtmServerStat2Table = _GtmServerStat2Table_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 4, 3)
)
if mibBuilder.loadTexts:
    gtmServerStat2Table.setStatus("current")
_GtmServerStat2Entry_Object = MibTableRow
gtmServerStat2Entry = _GtmServerStat2Entry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 4, 3, 1)
)
gtmServerStat2Entry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmServerStat2Name"),
)
if mibBuilder.loadTexts:
    gtmServerStat2Entry.setStatus("current")
_GtmServerStat2Name_Type = LongDisplayString
_GtmServerStat2Name_Object = MibTableColumn
gtmServerStat2Name = _GtmServerStat2Name_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 4, 3, 1, 1),
    _GtmServerStat2Name_Type()
)
gtmServerStat2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStat2Name.setStatus("current")
_GtmServerStat2UnitId_Type = Integer32
_GtmServerStat2UnitId_Object = MibTableColumn
gtmServerStat2UnitId = _GtmServerStat2UnitId_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 4, 3, 1, 2),
    _GtmServerStat2UnitId_Type()
)
gtmServerStat2UnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStat2UnitId.setStatus("deprecated")
_GtmServerStat2VsPicks_Type = Counter64
_GtmServerStat2VsPicks_Object = MibTableColumn
gtmServerStat2VsPicks = _GtmServerStat2VsPicks_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 4, 3, 1, 3),
    _GtmServerStat2VsPicks_Type()
)
gtmServerStat2VsPicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStat2VsPicks.setStatus("current")
_GtmServerStat2CpuUsage_Type = Counter64
_GtmServerStat2CpuUsage_Object = MibTableColumn
gtmServerStat2CpuUsage = _GtmServerStat2CpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 4, 3, 1, 4),
    _GtmServerStat2CpuUsage_Type()
)
gtmServerStat2CpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStat2CpuUsage.setStatus("current")
_GtmServerStat2MemAvail_Type = Counter64
_GtmServerStat2MemAvail_Object = MibTableColumn
gtmServerStat2MemAvail = _GtmServerStat2MemAvail_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 4, 3, 1, 5),
    _GtmServerStat2MemAvail_Type()
)
gtmServerStat2MemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStat2MemAvail.setStatus("current")
_GtmServerStat2BitsPerSecIn_Type = Counter64
_GtmServerStat2BitsPerSecIn_Object = MibTableColumn
gtmServerStat2BitsPerSecIn = _GtmServerStat2BitsPerSecIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 4, 3, 1, 6),
    _GtmServerStat2BitsPerSecIn_Type()
)
gtmServerStat2BitsPerSecIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStat2BitsPerSecIn.setStatus("current")
_GtmServerStat2BitsPerSecOut_Type = Counter64
_GtmServerStat2BitsPerSecOut_Object = MibTableColumn
gtmServerStat2BitsPerSecOut = _GtmServerStat2BitsPerSecOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 4, 3, 1, 7),
    _GtmServerStat2BitsPerSecOut_Type()
)
gtmServerStat2BitsPerSecOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStat2BitsPerSecOut.setStatus("current")
_GtmServerStat2PktsPerSecIn_Type = Counter64
_GtmServerStat2PktsPerSecIn_Object = MibTableColumn
gtmServerStat2PktsPerSecIn = _GtmServerStat2PktsPerSecIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 4, 3, 1, 8),
    _GtmServerStat2PktsPerSecIn_Type()
)
gtmServerStat2PktsPerSecIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStat2PktsPerSecIn.setStatus("current")
_GtmServerStat2PktsPerSecOut_Type = Counter64
_GtmServerStat2PktsPerSecOut_Object = MibTableColumn
gtmServerStat2PktsPerSecOut = _GtmServerStat2PktsPerSecOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 4, 3, 1, 9),
    _GtmServerStat2PktsPerSecOut_Type()
)
gtmServerStat2PktsPerSecOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStat2PktsPerSecOut.setStatus("current")
_GtmServerStat2Connections_Type = Counter64
_GtmServerStat2Connections_Object = MibTableColumn
gtmServerStat2Connections = _GtmServerStat2Connections_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 4, 3, 1, 10),
    _GtmServerStat2Connections_Type()
)
gtmServerStat2Connections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStat2Connections.setStatus("current")
_GtmServerStat2ConnRate_Type = Counter64
_GtmServerStat2ConnRate_Object = MibTableColumn
gtmServerStat2ConnRate = _GtmServerStat2ConnRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 9, 4, 3, 1, 11),
    _GtmServerStat2ConnRate_Type()
)
gtmServerStat2ConnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmServerStat2ConnRate.setStatus("deprecated")
_GtmTopologies_ObjectIdentity = ObjectIdentity
gtmTopologies = _GtmTopologies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 10)
)
_GtmTopItem_ObjectIdentity = ObjectIdentity
gtmTopItem = _GtmTopItem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 10, 1)
)
_GtmTopItemNumber_Type = Integer32
_GtmTopItemNumber_Object = MibScalar
gtmTopItemNumber = _GtmTopItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 10, 1, 1),
    _GtmTopItemNumber_Type()
)
gtmTopItemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmTopItemNumber.setStatus("current")
_GtmTopItemTable_Object = MibTable
gtmTopItemTable = _GtmTopItemTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 10, 1, 2)
)
if mibBuilder.loadTexts:
    gtmTopItemTable.setStatus("current")
_GtmTopItemEntry_Object = MibTableRow
gtmTopItemEntry = _GtmTopItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 10, 1, 2, 1)
)
gtmTopItemEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmTopItemLdnsType"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmTopItemLdnsNegate"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmTopItemLdnsEntry"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmTopItemServerType"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmTopItemServerNegate"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmTopItemServerEntry"),
)
if mibBuilder.loadTexts:
    gtmTopItemEntry.setStatus("current")


class _GtmTopItemLdnsType_Type(Integer32):
    """Custom type gtmTopItemLdnsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cidr", 0),
          ("continent", 2),
          ("country", 3),
          ("datacenter", 6),
          ("geoip-isp", 8),
          ("ispregion", 7),
          ("pool", 5),
          ("region", 1),
          ("state", 4))
    )


_GtmTopItemLdnsType_Type.__name__ = "Integer32"
_GtmTopItemLdnsType_Object = MibTableColumn
gtmTopItemLdnsType = _GtmTopItemLdnsType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 10, 1, 2, 1, 1),
    _GtmTopItemLdnsType_Type()
)
gtmTopItemLdnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmTopItemLdnsType.setStatus("current")


class _GtmTopItemLdnsNegate_Type(Integer32):
    """Custom type gtmTopItemLdnsNegate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmTopItemLdnsNegate_Type.__name__ = "Integer32"
_GtmTopItemLdnsNegate_Object = MibTableColumn
gtmTopItemLdnsNegate = _GtmTopItemLdnsNegate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 10, 1, 2, 1, 2),
    _GtmTopItemLdnsNegate_Type()
)
gtmTopItemLdnsNegate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmTopItemLdnsNegate.setStatus("current")
_GtmTopItemLdnsEntry_Type = LongDisplayString
_GtmTopItemLdnsEntry_Object = MibTableColumn
gtmTopItemLdnsEntry = _GtmTopItemLdnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 10, 1, 2, 1, 3),
    _GtmTopItemLdnsEntry_Type()
)
gtmTopItemLdnsEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmTopItemLdnsEntry.setStatus("current")


class _GtmTopItemServerType_Type(Integer32):
    """Custom type gtmTopItemServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cidr", 0),
          ("continent", 2),
          ("country", 3),
          ("datacenter", 6),
          ("geoip-isp", 8),
          ("ispregion", 7),
          ("pool", 5),
          ("region", 1),
          ("state", 4))
    )


_GtmTopItemServerType_Type.__name__ = "Integer32"
_GtmTopItemServerType_Object = MibTableColumn
gtmTopItemServerType = _GtmTopItemServerType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 10, 1, 2, 1, 4),
    _GtmTopItemServerType_Type()
)
gtmTopItemServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmTopItemServerType.setStatus("current")


class _GtmTopItemServerNegate_Type(Integer32):
    """Custom type gtmTopItemServerNegate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmTopItemServerNegate_Type.__name__ = "Integer32"
_GtmTopItemServerNegate_Object = MibTableColumn
gtmTopItemServerNegate = _GtmTopItemServerNegate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 10, 1, 2, 1, 5),
    _GtmTopItemServerNegate_Type()
)
gtmTopItemServerNegate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmTopItemServerNegate.setStatus("current")
_GtmTopItemServerEntry_Type = LongDisplayString
_GtmTopItemServerEntry_Object = MibTableColumn
gtmTopItemServerEntry = _GtmTopItemServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 10, 1, 2, 1, 6),
    _GtmTopItemServerEntry_Type()
)
gtmTopItemServerEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmTopItemServerEntry.setStatus("current")
_GtmTopItemWeight_Type = Integer32
_GtmTopItemWeight_Object = MibTableColumn
gtmTopItemWeight = _GtmTopItemWeight_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 10, 1, 2, 1, 7),
    _GtmTopItemWeight_Type()
)
gtmTopItemWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmTopItemWeight.setStatus("current")
_GtmTopItemOrder_Type = Integer32
_GtmTopItemOrder_Object = MibTableColumn
gtmTopItemOrder = _GtmTopItemOrder_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 10, 1, 2, 1, 8),
    _GtmTopItemOrder_Type()
)
gtmTopItemOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmTopItemOrder.setStatus("current")
_GtmVirtualServers_ObjectIdentity = ObjectIdentity
gtmVirtualServers = _GtmVirtualServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11)
)
_GtmVirtualServ_ObjectIdentity = ObjectIdentity
gtmVirtualServ = _GtmVirtualServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1)
)
_GtmVsNumber_Type = Integer32
_GtmVsNumber_Object = MibScalar
gtmVsNumber = _GtmVsNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 1),
    _GtmVsNumber_Type()
)
gtmVsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsNumber.setStatus("current")
_GtmVsTable_Object = MibTable
gtmVsTable = _GtmVsTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2)
)
if mibBuilder.loadTexts:
    gtmVsTable.setStatus("current")
_GtmVsEntry_Object = MibTableRow
gtmVsEntry = _GtmVsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1)
)
gtmVsEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmVsServerName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmVsName"),
)
if mibBuilder.loadTexts:
    gtmVsEntry.setStatus("current")
_GtmVsIpType_Type = InetAddressType
_GtmVsIpType_Object = MibTableColumn
gtmVsIpType = _GtmVsIpType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 1),
    _GtmVsIpType_Type()
)
gtmVsIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsIpType.setStatus("current")
_GtmVsIp_Type = InetAddress
_GtmVsIp_Object = MibTableColumn
gtmVsIp = _GtmVsIp_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 2),
    _GtmVsIp_Type()
)
gtmVsIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsIp.setStatus("current")
_GtmVsPort_Type = InetPortNumber
_GtmVsPort_Object = MibTableColumn
gtmVsPort = _GtmVsPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 3),
    _GtmVsPort_Type()
)
gtmVsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsPort.setStatus("current")
_GtmVsName_Type = LongDisplayString
_GtmVsName_Object = MibTableColumn
gtmVsName = _GtmVsName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 4),
    _GtmVsName_Type()
)
gtmVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsName.setStatus("current")
_GtmVsServerName_Type = LongDisplayString
_GtmVsServerName_Object = MibTableColumn
gtmVsServerName = _GtmVsServerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 5),
    _GtmVsServerName_Type()
)
gtmVsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsServerName.setStatus("current")
_GtmVsIpXlatedType_Type = InetAddressType
_GtmVsIpXlatedType_Object = MibTableColumn
gtmVsIpXlatedType = _GtmVsIpXlatedType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 6),
    _GtmVsIpXlatedType_Type()
)
gtmVsIpXlatedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsIpXlatedType.setStatus("current")
_GtmVsIpXlated_Type = InetAddress
_GtmVsIpXlated_Object = MibTableColumn
gtmVsIpXlated = _GtmVsIpXlated_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 7),
    _GtmVsIpXlated_Type()
)
gtmVsIpXlated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsIpXlated.setStatus("current")
_GtmVsPortXlated_Type = InetPortNumber
_GtmVsPortXlated_Object = MibTableColumn
gtmVsPortXlated = _GtmVsPortXlated_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 8),
    _GtmVsPortXlated_Type()
)
gtmVsPortXlated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsPortXlated.setStatus("current")


class _GtmVsLimitCpuUsageEnabled_Type(Integer32):
    """Custom type gtmVsLimitCpuUsageEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmVsLimitCpuUsageEnabled_Type.__name__ = "Integer32"
_GtmVsLimitCpuUsageEnabled_Object = MibTableColumn
gtmVsLimitCpuUsageEnabled = _GtmVsLimitCpuUsageEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 9),
    _GtmVsLimitCpuUsageEnabled_Type()
)
gtmVsLimitCpuUsageEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsLimitCpuUsageEnabled.setStatus("current")


class _GtmVsLimitMemAvailEnabled_Type(Integer32):
    """Custom type gtmVsLimitMemAvailEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmVsLimitMemAvailEnabled_Type.__name__ = "Integer32"
_GtmVsLimitMemAvailEnabled_Object = MibTableColumn
gtmVsLimitMemAvailEnabled = _GtmVsLimitMemAvailEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 10),
    _GtmVsLimitMemAvailEnabled_Type()
)
gtmVsLimitMemAvailEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsLimitMemAvailEnabled.setStatus("current")


class _GtmVsLimitBitsPerSecEnabled_Type(Integer32):
    """Custom type gtmVsLimitBitsPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmVsLimitBitsPerSecEnabled_Type.__name__ = "Integer32"
_GtmVsLimitBitsPerSecEnabled_Object = MibTableColumn
gtmVsLimitBitsPerSecEnabled = _GtmVsLimitBitsPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 11),
    _GtmVsLimitBitsPerSecEnabled_Type()
)
gtmVsLimitBitsPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsLimitBitsPerSecEnabled.setStatus("current")


class _GtmVsLimitPktsPerSecEnabled_Type(Integer32):
    """Custom type gtmVsLimitPktsPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmVsLimitPktsPerSecEnabled_Type.__name__ = "Integer32"
_GtmVsLimitPktsPerSecEnabled_Object = MibTableColumn
gtmVsLimitPktsPerSecEnabled = _GtmVsLimitPktsPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 12),
    _GtmVsLimitPktsPerSecEnabled_Type()
)
gtmVsLimitPktsPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsLimitPktsPerSecEnabled.setStatus("current")


class _GtmVsLimitConnEnabled_Type(Integer32):
    """Custom type gtmVsLimitConnEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmVsLimitConnEnabled_Type.__name__ = "Integer32"
_GtmVsLimitConnEnabled_Object = MibTableColumn
gtmVsLimitConnEnabled = _GtmVsLimitConnEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 13),
    _GtmVsLimitConnEnabled_Type()
)
gtmVsLimitConnEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsLimitConnEnabled.setStatus("current")


class _GtmVsLimitConnPerSecEnabled_Type(Integer32):
    """Custom type gtmVsLimitConnPerSecEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmVsLimitConnPerSecEnabled_Type.__name__ = "Integer32"
_GtmVsLimitConnPerSecEnabled_Object = MibTableColumn
gtmVsLimitConnPerSecEnabled = _GtmVsLimitConnPerSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 14),
    _GtmVsLimitConnPerSecEnabled_Type()
)
gtmVsLimitConnPerSecEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsLimitConnPerSecEnabled.setStatus("deprecated")
_GtmVsLimitCpuUsage_Type = Counter64
_GtmVsLimitCpuUsage_Object = MibTableColumn
gtmVsLimitCpuUsage = _GtmVsLimitCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 15),
    _GtmVsLimitCpuUsage_Type()
)
gtmVsLimitCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsLimitCpuUsage.setStatus("current")
_GtmVsLimitMemAvail_Type = Counter64
_GtmVsLimitMemAvail_Object = MibTableColumn
gtmVsLimitMemAvail = _GtmVsLimitMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 16),
    _GtmVsLimitMemAvail_Type()
)
gtmVsLimitMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsLimitMemAvail.setStatus("current")
_GtmVsLimitBitsPerSec_Type = Counter64
_GtmVsLimitBitsPerSec_Object = MibTableColumn
gtmVsLimitBitsPerSec = _GtmVsLimitBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 17),
    _GtmVsLimitBitsPerSec_Type()
)
gtmVsLimitBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsLimitBitsPerSec.setStatus("current")
_GtmVsLimitPktsPerSec_Type = Counter64
_GtmVsLimitPktsPerSec_Object = MibTableColumn
gtmVsLimitPktsPerSec = _GtmVsLimitPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 18),
    _GtmVsLimitPktsPerSec_Type()
)
gtmVsLimitPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsLimitPktsPerSec.setStatus("current")
_GtmVsLimitConn_Type = Counter64
_GtmVsLimitConn_Object = MibTableColumn
gtmVsLimitConn = _GtmVsLimitConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 19),
    _GtmVsLimitConn_Type()
)
gtmVsLimitConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsLimitConn.setStatus("current")
_GtmVsLimitConnPerSec_Type = Counter64
_GtmVsLimitConnPerSec_Object = MibTableColumn
gtmVsLimitConnPerSec = _GtmVsLimitConnPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 20),
    _GtmVsLimitConnPerSec_Type()
)
gtmVsLimitConnPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsLimitConnPerSec.setStatus("deprecated")
_GtmVsMonitorRule_Type = LongDisplayString
_GtmVsMonitorRule_Object = MibTableColumn
gtmVsMonitorRule = _GtmVsMonitorRule_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 21),
    _GtmVsMonitorRule_Type()
)
gtmVsMonitorRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsMonitorRule.setStatus("current")


class _GtmVsEnabled_Type(Integer32):
    """Custom type gtmVsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_GtmVsEnabled_Type.__name__ = "Integer32"
_GtmVsEnabled_Object = MibTableColumn
gtmVsEnabled = _GtmVsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 22),
    _GtmVsEnabled_Type()
)
gtmVsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsEnabled.setStatus("current")
_GtmVsLinkName_Type = LongDisplayString
_GtmVsLinkName_Object = MibTableColumn
gtmVsLinkName = _GtmVsLinkName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 1, 2, 1, 23),
    _GtmVsLinkName_Type()
)
gtmVsLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsLinkName.setStatus("current")
_GtmVirtualServDepends_ObjectIdentity = ObjectIdentity
gtmVirtualServDepends = _GtmVirtualServDepends_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 2)
)
_GtmVsDepsNumber_Type = Integer32
_GtmVsDepsNumber_Object = MibScalar
gtmVsDepsNumber = _GtmVsDepsNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 2, 1),
    _GtmVsDepsNumber_Type()
)
gtmVsDepsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsDepsNumber.setStatus("current")
_GtmVsDepsTable_Object = MibTable
gtmVsDepsTable = _GtmVsDepsTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 2, 2)
)
if mibBuilder.loadTexts:
    gtmVsDepsTable.setStatus("current")
_GtmVsDepsEntry_Object = MibTableRow
gtmVsDepsEntry = _GtmVsDepsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 2, 2, 1)
)
gtmVsDepsEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmVsDepsServerName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmVsDepsVsName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmVsDepsDependServerName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmVsDepsDependVsName"),
)
if mibBuilder.loadTexts:
    gtmVsDepsEntry.setStatus("current")
_GtmVsDepsIpType_Type = InetAddressType
_GtmVsDepsIpType_Object = MibTableColumn
gtmVsDepsIpType = _GtmVsDepsIpType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 2, 2, 1, 1),
    _GtmVsDepsIpType_Type()
)
gtmVsDepsIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsDepsIpType.setStatus("deprecated")
_GtmVsDepsIp_Type = InetAddress
_GtmVsDepsIp_Object = MibTableColumn
gtmVsDepsIp = _GtmVsDepsIp_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 2, 2, 1, 2),
    _GtmVsDepsIp_Type()
)
gtmVsDepsIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsDepsIp.setStatus("deprecated")
_GtmVsDepsPort_Type = InetPortNumber
_GtmVsDepsPort_Object = MibTableColumn
gtmVsDepsPort = _GtmVsDepsPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 2, 2, 1, 3),
    _GtmVsDepsPort_Type()
)
gtmVsDepsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsDepsPort.setStatus("deprecated")
_GtmVsDepsVipType_Type = InetAddressType
_GtmVsDepsVipType_Object = MibTableColumn
gtmVsDepsVipType = _GtmVsDepsVipType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 2, 2, 1, 4),
    _GtmVsDepsVipType_Type()
)
gtmVsDepsVipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsDepsVipType.setStatus("deprecated")
_GtmVsDepsVip_Type = InetAddress
_GtmVsDepsVip_Object = MibTableColumn
gtmVsDepsVip = _GtmVsDepsVip_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 2, 2, 1, 5),
    _GtmVsDepsVip_Type()
)
gtmVsDepsVip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsDepsVip.setStatus("deprecated")
_GtmVsDepsVport_Type = InetPortNumber
_GtmVsDepsVport_Object = MibTableColumn
gtmVsDepsVport = _GtmVsDepsVport_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 2, 2, 1, 6),
    _GtmVsDepsVport_Type()
)
gtmVsDepsVport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsDepsVport.setStatus("deprecated")
_GtmVsDepsServerName_Type = LongDisplayString
_GtmVsDepsServerName_Object = MibTableColumn
gtmVsDepsServerName = _GtmVsDepsServerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 2, 2, 1, 7),
    _GtmVsDepsServerName_Type()
)
gtmVsDepsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsDepsServerName.setStatus("current")
_GtmVsDepsVsName_Type = LongDisplayString
_GtmVsDepsVsName_Object = MibTableColumn
gtmVsDepsVsName = _GtmVsDepsVsName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 2, 2, 1, 8),
    _GtmVsDepsVsName_Type()
)
gtmVsDepsVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsDepsVsName.setStatus("current")
_GtmVsDepsDependServerName_Type = LongDisplayString
_GtmVsDepsDependServerName_Object = MibTableColumn
gtmVsDepsDependServerName = _GtmVsDepsDependServerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 2, 2, 1, 9),
    _GtmVsDepsDependServerName_Type()
)
gtmVsDepsDependServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsDepsDependServerName.setStatus("current")
_GtmVsDepsDependVsName_Type = LongDisplayString
_GtmVsDepsDependVsName_Object = MibTableColumn
gtmVsDepsDependVsName = _GtmVsDepsDependVsName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 2, 2, 1, 10),
    _GtmVsDepsDependVsName_Type()
)
gtmVsDepsDependVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsDepsDependVsName.setStatus("current")
_GtmVirtualServStat_ObjectIdentity = ObjectIdentity
gtmVirtualServStat = _GtmVirtualServStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3)
)
_GtmVsStatResetStats_Type = Integer32
_GtmVsStatResetStats_Object = MibScalar
gtmVsStatResetStats = _GtmVsStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 1),
    _GtmVsStatResetStats_Type()
)
gtmVsStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtmVsStatResetStats.setStatus("current")
_GtmVsStatNumber_Type = Integer32
_GtmVsStatNumber_Object = MibScalar
gtmVsStatNumber = _GtmVsStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 2),
    _GtmVsStatNumber_Type()
)
gtmVsStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatNumber.setStatus("current")
_GtmVsStatTable_Object = MibTable
gtmVsStatTable = _GtmVsStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 3)
)
if mibBuilder.loadTexts:
    gtmVsStatTable.setStatus("current")
_GtmVsStatEntry_Object = MibTableRow
gtmVsStatEntry = _GtmVsStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 3, 1)
)
gtmVsStatEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmVsStatServerName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmVsStatName"),
)
if mibBuilder.loadTexts:
    gtmVsStatEntry.setStatus("current")
_GtmVsStatIpType_Type = InetAddressType
_GtmVsStatIpType_Object = MibTableColumn
gtmVsStatIpType = _GtmVsStatIpType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 3, 1, 1),
    _GtmVsStatIpType_Type()
)
gtmVsStatIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatIpType.setStatus("deprecated")
_GtmVsStatIp_Type = InetAddress
_GtmVsStatIp_Object = MibTableColumn
gtmVsStatIp = _GtmVsStatIp_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 3, 1, 2),
    _GtmVsStatIp_Type()
)
gtmVsStatIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatIp.setStatus("deprecated")
_GtmVsStatPort_Type = InetPortNumber
_GtmVsStatPort_Object = MibTableColumn
gtmVsStatPort = _GtmVsStatPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 3, 1, 3),
    _GtmVsStatPort_Type()
)
gtmVsStatPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatPort.setStatus("deprecated")
_GtmVsStatName_Type = LongDisplayString
_GtmVsStatName_Object = MibTableColumn
gtmVsStatName = _GtmVsStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 3, 1, 4),
    _GtmVsStatName_Type()
)
gtmVsStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatName.setStatus("current")
_GtmVsStatCpuUsage_Type = Counter64
_GtmVsStatCpuUsage_Object = MibTableColumn
gtmVsStatCpuUsage = _GtmVsStatCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 3, 1, 5),
    _GtmVsStatCpuUsage_Type()
)
gtmVsStatCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatCpuUsage.setStatus("current")
_GtmVsStatMemAvail_Type = Counter64
_GtmVsStatMemAvail_Object = MibTableColumn
gtmVsStatMemAvail = _GtmVsStatMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 3, 1, 6),
    _GtmVsStatMemAvail_Type()
)
gtmVsStatMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatMemAvail.setStatus("current")
_GtmVsStatBitsPerSecIn_Type = Counter64
_GtmVsStatBitsPerSecIn_Object = MibTableColumn
gtmVsStatBitsPerSecIn = _GtmVsStatBitsPerSecIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 3, 1, 7),
    _GtmVsStatBitsPerSecIn_Type()
)
gtmVsStatBitsPerSecIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatBitsPerSecIn.setStatus("current")
_GtmVsStatBitsPerSecOut_Type = Counter64
_GtmVsStatBitsPerSecOut_Object = MibTableColumn
gtmVsStatBitsPerSecOut = _GtmVsStatBitsPerSecOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 3, 1, 8),
    _GtmVsStatBitsPerSecOut_Type()
)
gtmVsStatBitsPerSecOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatBitsPerSecOut.setStatus("current")
_GtmVsStatPktsPerSecIn_Type = Counter64
_GtmVsStatPktsPerSecIn_Object = MibTableColumn
gtmVsStatPktsPerSecIn = _GtmVsStatPktsPerSecIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 3, 1, 9),
    _GtmVsStatPktsPerSecIn_Type()
)
gtmVsStatPktsPerSecIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatPktsPerSecIn.setStatus("current")
_GtmVsStatPktsPerSecOut_Type = Counter64
_GtmVsStatPktsPerSecOut_Object = MibTableColumn
gtmVsStatPktsPerSecOut = _GtmVsStatPktsPerSecOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 3, 1, 10),
    _GtmVsStatPktsPerSecOut_Type()
)
gtmVsStatPktsPerSecOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatPktsPerSecOut.setStatus("current")
_GtmVsStatConnections_Type = Counter64
_GtmVsStatConnections_Object = MibTableColumn
gtmVsStatConnections = _GtmVsStatConnections_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 3, 1, 11),
    _GtmVsStatConnections_Type()
)
gtmVsStatConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatConnections.setStatus("current")
_GtmVsStatConnRate_Type = Counter64
_GtmVsStatConnRate_Object = MibTableColumn
gtmVsStatConnRate = _GtmVsStatConnRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 3, 1, 12),
    _GtmVsStatConnRate_Type()
)
gtmVsStatConnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatConnRate.setStatus("deprecated")
_GtmVsStatVsScore_Type = Counter64
_GtmVsStatVsScore_Object = MibTableColumn
gtmVsStatVsScore = _GtmVsStatVsScore_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 3, 1, 13),
    _GtmVsStatVsScore_Type()
)
gtmVsStatVsScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatVsScore.setStatus("current")
_GtmVsStatServerName_Type = LongDisplayString
_GtmVsStatServerName_Object = MibTableColumn
gtmVsStatServerName = _GtmVsStatServerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 3, 3, 1, 14),
    _GtmVsStatServerName_Type()
)
gtmVsStatServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatServerName.setStatus("current")
_GtmVirtualServStatus_ObjectIdentity = ObjectIdentity
gtmVirtualServStatus = _GtmVirtualServStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 4)
)
_GtmVsStatusNumber_Type = Integer32
_GtmVsStatusNumber_Object = MibScalar
gtmVsStatusNumber = _GtmVsStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 4, 1),
    _GtmVsStatusNumber_Type()
)
gtmVsStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatusNumber.setStatus("current")
_GtmVsStatusTable_Object = MibTable
gtmVsStatusTable = _GtmVsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 4, 2)
)
if mibBuilder.loadTexts:
    gtmVsStatusTable.setStatus("current")
_GtmVsStatusEntry_Object = MibTableRow
gtmVsStatusEntry = _GtmVsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 4, 2, 1)
)
gtmVsStatusEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmVsStatusServerName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmVsStatusVsName"),
)
if mibBuilder.loadTexts:
    gtmVsStatusEntry.setStatus("current")
_GtmVsStatusIpType_Type = InetAddressType
_GtmVsStatusIpType_Object = MibTableColumn
gtmVsStatusIpType = _GtmVsStatusIpType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 4, 2, 1, 1),
    _GtmVsStatusIpType_Type()
)
gtmVsStatusIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatusIpType.setStatus("deprecated")
_GtmVsStatusIp_Type = InetAddress
_GtmVsStatusIp_Object = MibTableColumn
gtmVsStatusIp = _GtmVsStatusIp_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 4, 2, 1, 2),
    _GtmVsStatusIp_Type()
)
gtmVsStatusIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatusIp.setStatus("deprecated")
_GtmVsStatusPort_Type = InetPortNumber
_GtmVsStatusPort_Object = MibTableColumn
gtmVsStatusPort = _GtmVsStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 4, 2, 1, 3),
    _GtmVsStatusPort_Type()
)
gtmVsStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatusPort.setStatus("deprecated")


class _GtmVsStatusAvailState_Type(Integer32):
    """Custom type gtmVsStatusAvailState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blue", 4),
          ("gray", 5),
          ("green", 1),
          ("none", 0),
          ("red", 3),
          ("yellow", 2))
    )


_GtmVsStatusAvailState_Type.__name__ = "Integer32"
_GtmVsStatusAvailState_Object = MibTableColumn
gtmVsStatusAvailState = _GtmVsStatusAvailState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 4, 2, 1, 4),
    _GtmVsStatusAvailState_Type()
)
gtmVsStatusAvailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatusAvailState.setStatus("current")


class _GtmVsStatusEnabledState_Type(Integer32):
    """Custom type gtmVsStatusEnabledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("disabledbyparent", 3),
          ("enabled", 1),
          ("none", 0))
    )


_GtmVsStatusEnabledState_Type.__name__ = "Integer32"
_GtmVsStatusEnabledState_Object = MibTableColumn
gtmVsStatusEnabledState = _GtmVsStatusEnabledState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 4, 2, 1, 5),
    _GtmVsStatusEnabledState_Type()
)
gtmVsStatusEnabledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatusEnabledState.setStatus("current")
_GtmVsStatusParentType_Type = Integer32
_GtmVsStatusParentType_Object = MibTableColumn
gtmVsStatusParentType = _GtmVsStatusParentType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 4, 2, 1, 6),
    _GtmVsStatusParentType_Type()
)
gtmVsStatusParentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatusParentType.setStatus("deprecated")
_GtmVsStatusDetailReason_Type = LongDisplayString
_GtmVsStatusDetailReason_Object = MibTableColumn
gtmVsStatusDetailReason = _GtmVsStatusDetailReason_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 4, 2, 1, 7),
    _GtmVsStatusDetailReason_Type()
)
gtmVsStatusDetailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatusDetailReason.setStatus("current")
_GtmVsStatusVsName_Type = LongDisplayString
_GtmVsStatusVsName_Object = MibTableColumn
gtmVsStatusVsName = _GtmVsStatusVsName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 4, 2, 1, 8),
    _GtmVsStatusVsName_Type()
)
gtmVsStatusVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatusVsName.setStatus("current")
_GtmVsStatusServerName_Type = LongDisplayString
_GtmVsStatusServerName_Object = MibTableColumn
gtmVsStatusServerName = _GtmVsStatusServerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 11, 4, 2, 1, 9),
    _GtmVsStatusServerName_Type()
)
gtmVsStatusServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmVsStatusServerName.setStatus("current")
_GtmWideips_ObjectIdentity = ObjectIdentity
gtmWideips = _GtmWideips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12)
)
_GtmWideip_ObjectIdentity = ObjectIdentity
gtmWideip = _GtmWideip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 1)
)
_GtmWideipNumber_Type = Integer32
_GtmWideipNumber_Object = MibScalar
gtmWideipNumber = _GtmWideipNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 1, 1),
    _GtmWideipNumber_Type()
)
gtmWideipNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipNumber.setStatus("current")
_GtmWideipTable_Object = MibTable
gtmWideipTable = _GtmWideipTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 1, 2)
)
if mibBuilder.loadTexts:
    gtmWideipTable.setStatus("current")
_GtmWideipEntry_Object = MibTableRow
gtmWideipEntry = _GtmWideipEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 1, 2, 1)
)
gtmWideipEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmWideipName"),
)
if mibBuilder.loadTexts:
    gtmWideipEntry.setStatus("current")
_GtmWideipName_Type = LongDisplayString
_GtmWideipName_Object = MibTableColumn
gtmWideipName = _GtmWideipName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 1, 2, 1, 1),
    _GtmWideipName_Type()
)
gtmWideipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipName.setStatus("current")


class _GtmWideipPersist_Type(Integer32):
    """Custom type gtmWideipPersist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmWideipPersist_Type.__name__ = "Integer32"
_GtmWideipPersist_Object = MibTableColumn
gtmWideipPersist = _GtmWideipPersist_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 1, 2, 1, 2),
    _GtmWideipPersist_Type()
)
gtmWideipPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipPersist.setStatus("current")
_GtmWideipTtlPersist_Type = Integer32
_GtmWideipTtlPersist_Object = MibTableColumn
gtmWideipTtlPersist = _GtmWideipTtlPersist_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 1, 2, 1, 3),
    _GtmWideipTtlPersist_Type()
)
gtmWideipTtlPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipTtlPersist.setStatus("current")


class _GtmWideipEnabled_Type(Integer32):
    """Custom type gtmWideipEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_GtmWideipEnabled_Type.__name__ = "Integer32"
_GtmWideipEnabled_Object = MibTableColumn
gtmWideipEnabled = _GtmWideipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 1, 2, 1, 4),
    _GtmWideipEnabled_Type()
)
gtmWideipEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipEnabled.setStatus("current")


class _GtmWideipLbmodePool_Type(Integer32):
    """Custom type gtmWideipLbmodePool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("bps", 15),
          ("cpu", 12),
          ("droppacket", 16),
          ("explicitip", 17),
          ("ga", 6),
          ("hitratio", 13),
          ("leastconn", 8),
          ("lowesthops", 10),
          ("lowestrtt", 9),
          ("null", 1),
          ("packetrate", 11),
          ("qos", 14),
          ("ratio", 3),
          ("returntodns", 0),
          ("roundrobin", 2),
          ("statpersit", 5),
          ("topology", 4),
          ("vscapacity", 7),
          ("vsscore", 18))
    )


_GtmWideipLbmodePool_Type.__name__ = "Integer32"
_GtmWideipLbmodePool_Object = MibTableColumn
gtmWideipLbmodePool = _GtmWideipLbmodePool_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 1, 2, 1, 5),
    _GtmWideipLbmodePool_Type()
)
gtmWideipLbmodePool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipLbmodePool.setStatus("current")
_GtmWideipApplication_Type = LongDisplayString
_GtmWideipApplication_Object = MibTableColumn
gtmWideipApplication = _GtmWideipApplication_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 1, 2, 1, 6),
    _GtmWideipApplication_Type()
)
gtmWideipApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipApplication.setStatus("current")
_GtmWideipLastResortPool_Type = LongDisplayString
_GtmWideipLastResortPool_Object = MibTableColumn
gtmWideipLastResortPool = _GtmWideipLastResortPool_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 1, 2, 1, 7),
    _GtmWideipLastResortPool_Type()
)
gtmWideipLastResortPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipLastResortPool.setStatus("current")


class _GtmWideipIpv6Noerror_Type(Integer32):
    """Custom type gtmWideipIpv6Noerror based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmWideipIpv6Noerror_Type.__name__ = "Integer32"
_GtmWideipIpv6Noerror_Object = MibTableColumn
gtmWideipIpv6Noerror = _GtmWideipIpv6Noerror_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 1, 2, 1, 8),
    _GtmWideipIpv6Noerror_Type()
)
gtmWideipIpv6Noerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipIpv6Noerror.setStatus("current")
_GtmWideipLoadBalancingDecisionLogVerbosity_Type = Integer32
_GtmWideipLoadBalancingDecisionLogVerbosity_Object = MibTableColumn
gtmWideipLoadBalancingDecisionLogVerbosity = _GtmWideipLoadBalancingDecisionLogVerbosity_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 1, 2, 1, 9),
    _GtmWideipLoadBalancingDecisionLogVerbosity_Type()
)
gtmWideipLoadBalancingDecisionLogVerbosity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipLoadBalancingDecisionLogVerbosity.setStatus("current")
_GtmWideipStat_ObjectIdentity = ObjectIdentity
gtmWideipStat = _GtmWideipStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2)
)
_GtmWideipStatResetStats_Type = Integer32
_GtmWideipStatResetStats_Object = MibScalar
gtmWideipStatResetStats = _GtmWideipStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2, 1),
    _GtmWideipStatResetStats_Type()
)
gtmWideipStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtmWideipStatResetStats.setStatus("current")
_GtmWideipStatNumber_Type = Integer32
_GtmWideipStatNumber_Object = MibScalar
gtmWideipStatNumber = _GtmWideipStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2, 2),
    _GtmWideipStatNumber_Type()
)
gtmWideipStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatNumber.setStatus("current")
_GtmWideipStatTable_Object = MibTable
gtmWideipStatTable = _GtmWideipStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2, 3)
)
if mibBuilder.loadTexts:
    gtmWideipStatTable.setStatus("current")
_GtmWideipStatEntry_Object = MibTableRow
gtmWideipStatEntry = _GtmWideipStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2, 3, 1)
)
gtmWideipStatEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmWideipStatName"),
)
if mibBuilder.loadTexts:
    gtmWideipStatEntry.setStatus("current")
_GtmWideipStatName_Type = LongDisplayString
_GtmWideipStatName_Object = MibTableColumn
gtmWideipStatName = _GtmWideipStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2, 3, 1, 1),
    _GtmWideipStatName_Type()
)
gtmWideipStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatName.setStatus("current")
_GtmWideipStatRequests_Type = Counter64
_GtmWideipStatRequests_Object = MibTableColumn
gtmWideipStatRequests = _GtmWideipStatRequests_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2, 3, 1, 2),
    _GtmWideipStatRequests_Type()
)
gtmWideipStatRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatRequests.setStatus("current")
_GtmWideipStatResolutions_Type = Counter64
_GtmWideipStatResolutions_Object = MibTableColumn
gtmWideipStatResolutions = _GtmWideipStatResolutions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2, 3, 1, 3),
    _GtmWideipStatResolutions_Type()
)
gtmWideipStatResolutions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatResolutions.setStatus("current")
_GtmWideipStatPersisted_Type = Counter64
_GtmWideipStatPersisted_Object = MibTableColumn
gtmWideipStatPersisted = _GtmWideipStatPersisted_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2, 3, 1, 4),
    _GtmWideipStatPersisted_Type()
)
gtmWideipStatPersisted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatPersisted.setStatus("current")
_GtmWideipStatPreferred_Type = Counter64
_GtmWideipStatPreferred_Object = MibTableColumn
gtmWideipStatPreferred = _GtmWideipStatPreferred_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2, 3, 1, 5),
    _GtmWideipStatPreferred_Type()
)
gtmWideipStatPreferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatPreferred.setStatus("current")
_GtmWideipStatFallback_Type = Counter64
_GtmWideipStatFallback_Object = MibTableColumn
gtmWideipStatFallback = _GtmWideipStatFallback_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2, 3, 1, 6),
    _GtmWideipStatFallback_Type()
)
gtmWideipStatFallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatFallback.setStatus("current")
_GtmWideipStatDropped_Type = Counter64
_GtmWideipStatDropped_Object = MibTableColumn
gtmWideipStatDropped = _GtmWideipStatDropped_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2, 3, 1, 7),
    _GtmWideipStatDropped_Type()
)
gtmWideipStatDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatDropped.setStatus("current")
_GtmWideipStatExplicitIp_Type = Counter64
_GtmWideipStatExplicitIp_Object = MibTableColumn
gtmWideipStatExplicitIp = _GtmWideipStatExplicitIp_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2, 3, 1, 8),
    _GtmWideipStatExplicitIp_Type()
)
gtmWideipStatExplicitIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatExplicitIp.setStatus("deprecated")
_GtmWideipStatReturnToDns_Type = Counter64
_GtmWideipStatReturnToDns_Object = MibTableColumn
gtmWideipStatReturnToDns = _GtmWideipStatReturnToDns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2, 3, 1, 9),
    _GtmWideipStatReturnToDns_Type()
)
gtmWideipStatReturnToDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatReturnToDns.setStatus("current")
_GtmWideipStatReturnFromDns_Type = Counter64
_GtmWideipStatReturnFromDns_Object = MibTableColumn
gtmWideipStatReturnFromDns = _GtmWideipStatReturnFromDns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2, 3, 1, 10),
    _GtmWideipStatReturnFromDns_Type()
)
gtmWideipStatReturnFromDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatReturnFromDns.setStatus("current")
_GtmWideipStatCnameResolutions_Type = Counter64
_GtmWideipStatCnameResolutions_Object = MibTableColumn
gtmWideipStatCnameResolutions = _GtmWideipStatCnameResolutions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2, 3, 1, 11),
    _GtmWideipStatCnameResolutions_Type()
)
gtmWideipStatCnameResolutions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatCnameResolutions.setStatus("current")
_GtmWideipStatARequests_Type = Counter64
_GtmWideipStatARequests_Object = MibTableColumn
gtmWideipStatARequests = _GtmWideipStatARequests_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2, 3, 1, 12),
    _GtmWideipStatARequests_Type()
)
gtmWideipStatARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatARequests.setStatus("current")
_GtmWideipStatAaaaRequests_Type = Counter64
_GtmWideipStatAaaaRequests_Object = MibTableColumn
gtmWideipStatAaaaRequests = _GtmWideipStatAaaaRequests_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 2, 3, 1, 13),
    _GtmWideipStatAaaaRequests_Type()
)
gtmWideipStatAaaaRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatAaaaRequests.setStatus("current")
_GtmWideipStatus_ObjectIdentity = ObjectIdentity
gtmWideipStatus = _GtmWideipStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 3)
)
_GtmWideipStatusNumber_Type = Integer32
_GtmWideipStatusNumber_Object = MibScalar
gtmWideipStatusNumber = _GtmWideipStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 3, 1),
    _GtmWideipStatusNumber_Type()
)
gtmWideipStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatusNumber.setStatus("current")
_GtmWideipStatusTable_Object = MibTable
gtmWideipStatusTable = _GtmWideipStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 3, 2)
)
if mibBuilder.loadTexts:
    gtmWideipStatusTable.setStatus("current")
_GtmWideipStatusEntry_Object = MibTableRow
gtmWideipStatusEntry = _GtmWideipStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 3, 2, 1)
)
gtmWideipStatusEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmWideipStatusName"),
)
if mibBuilder.loadTexts:
    gtmWideipStatusEntry.setStatus("current")
_GtmWideipStatusName_Type = LongDisplayString
_GtmWideipStatusName_Object = MibTableColumn
gtmWideipStatusName = _GtmWideipStatusName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 3, 2, 1, 1),
    _GtmWideipStatusName_Type()
)
gtmWideipStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatusName.setStatus("current")


class _GtmWideipStatusAvailState_Type(Integer32):
    """Custom type gtmWideipStatusAvailState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blue", 4),
          ("gray", 5),
          ("green", 1),
          ("none", 0),
          ("red", 3),
          ("yellow", 2))
    )


_GtmWideipStatusAvailState_Type.__name__ = "Integer32"
_GtmWideipStatusAvailState_Object = MibTableColumn
gtmWideipStatusAvailState = _GtmWideipStatusAvailState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 3, 2, 1, 2),
    _GtmWideipStatusAvailState_Type()
)
gtmWideipStatusAvailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatusAvailState.setStatus("current")


class _GtmWideipStatusEnabledState_Type(Integer32):
    """Custom type gtmWideipStatusEnabledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("disabledbyparent", 3),
          ("enabled", 1),
          ("none", 0))
    )


_GtmWideipStatusEnabledState_Type.__name__ = "Integer32"
_GtmWideipStatusEnabledState_Object = MibTableColumn
gtmWideipStatusEnabledState = _GtmWideipStatusEnabledState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 3, 2, 1, 3),
    _GtmWideipStatusEnabledState_Type()
)
gtmWideipStatusEnabledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatusEnabledState.setStatus("current")
_GtmWideipStatusParentType_Type = Integer32
_GtmWideipStatusParentType_Object = MibTableColumn
gtmWideipStatusParentType = _GtmWideipStatusParentType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 3, 2, 1, 4),
    _GtmWideipStatusParentType_Type()
)
gtmWideipStatusParentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatusParentType.setStatus("deprecated")
_GtmWideipStatusDetailReason_Type = LongDisplayString
_GtmWideipStatusDetailReason_Object = MibTableColumn
gtmWideipStatusDetailReason = _GtmWideipStatusDetailReason_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 3, 2, 1, 5),
    _GtmWideipStatusDetailReason_Type()
)
gtmWideipStatusDetailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipStatusDetailReason.setStatus("current")
_GtmWideipAlias_ObjectIdentity = ObjectIdentity
gtmWideipAlias = _GtmWideipAlias_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 4)
)
_GtmWideipAliasNumber_Type = Integer32
_GtmWideipAliasNumber_Object = MibScalar
gtmWideipAliasNumber = _GtmWideipAliasNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 4, 1),
    _GtmWideipAliasNumber_Type()
)
gtmWideipAliasNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipAliasNumber.setStatus("current")
_GtmWideipAliasTable_Object = MibTable
gtmWideipAliasTable = _GtmWideipAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 4, 2)
)
if mibBuilder.loadTexts:
    gtmWideipAliasTable.setStatus("current")
_GtmWideipAliasEntry_Object = MibTableRow
gtmWideipAliasEntry = _GtmWideipAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 4, 2, 1)
)
gtmWideipAliasEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmWideipAliasWipName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmWideipAliasName"),
)
if mibBuilder.loadTexts:
    gtmWideipAliasEntry.setStatus("current")
_GtmWideipAliasWipName_Type = LongDisplayString
_GtmWideipAliasWipName_Object = MibTableColumn
gtmWideipAliasWipName = _GtmWideipAliasWipName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 4, 2, 1, 1),
    _GtmWideipAliasWipName_Type()
)
gtmWideipAliasWipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipAliasWipName.setStatus("current")
_GtmWideipAliasName_Type = LongDisplayString
_GtmWideipAliasName_Object = MibTableColumn
gtmWideipAliasName = _GtmWideipAliasName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 4, 2, 1, 2),
    _GtmWideipAliasName_Type()
)
gtmWideipAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipAliasName.setStatus("current")
_GtmWideipPool_ObjectIdentity = ObjectIdentity
gtmWideipPool = _GtmWideipPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 5)
)
_GtmWideipPoolNumber_Type = Integer32
_GtmWideipPoolNumber_Object = MibScalar
gtmWideipPoolNumber = _GtmWideipPoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 5, 1),
    _GtmWideipPoolNumber_Type()
)
gtmWideipPoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipPoolNumber.setStatus("current")
_GtmWideipPoolTable_Object = MibTable
gtmWideipPoolTable = _GtmWideipPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 5, 2)
)
if mibBuilder.loadTexts:
    gtmWideipPoolTable.setStatus("current")
_GtmWideipPoolEntry_Object = MibTableRow
gtmWideipPoolEntry = _GtmWideipPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 5, 2, 1)
)
gtmWideipPoolEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmWideipPoolWipName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmWideipPoolPoolName"),
)
if mibBuilder.loadTexts:
    gtmWideipPoolEntry.setStatus("current")
_GtmWideipPoolWipName_Type = LongDisplayString
_GtmWideipPoolWipName_Object = MibTableColumn
gtmWideipPoolWipName = _GtmWideipPoolWipName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 5, 2, 1, 1),
    _GtmWideipPoolWipName_Type()
)
gtmWideipPoolWipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipPoolWipName.setStatus("current")
_GtmWideipPoolPoolName_Type = LongDisplayString
_GtmWideipPoolPoolName_Object = MibTableColumn
gtmWideipPoolPoolName = _GtmWideipPoolPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 5, 2, 1, 2),
    _GtmWideipPoolPoolName_Type()
)
gtmWideipPoolPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipPoolPoolName.setStatus("current")
_GtmWideipPoolOrder_Type = Integer32
_GtmWideipPoolOrder_Object = MibTableColumn
gtmWideipPoolOrder = _GtmWideipPoolOrder_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 5, 2, 1, 3),
    _GtmWideipPoolOrder_Type()
)
gtmWideipPoolOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipPoolOrder.setStatus("current")
_GtmWideipPoolRatio_Type = Integer32
_GtmWideipPoolRatio_Object = MibTableColumn
gtmWideipPoolRatio = _GtmWideipPoolRatio_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 5, 2, 1, 4),
    _GtmWideipPoolRatio_Type()
)
gtmWideipPoolRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipPoolRatio.setStatus("current")
_GtmWideipRule_ObjectIdentity = ObjectIdentity
gtmWideipRule = _GtmWideipRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 6)
)
_GtmWideipRuleNumber_Type = Integer32
_GtmWideipRuleNumber_Object = MibScalar
gtmWideipRuleNumber = _GtmWideipRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 6, 1),
    _GtmWideipRuleNumber_Type()
)
gtmWideipRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipRuleNumber.setStatus("current")
_GtmWideipRuleTable_Object = MibTable
gtmWideipRuleTable = _GtmWideipRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 6, 2)
)
if mibBuilder.loadTexts:
    gtmWideipRuleTable.setStatus("current")
_GtmWideipRuleEntry_Object = MibTableRow
gtmWideipRuleEntry = _GtmWideipRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 6, 2, 1)
)
gtmWideipRuleEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmWideipRuleWipName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmWideipRuleRuleName"),
)
if mibBuilder.loadTexts:
    gtmWideipRuleEntry.setStatus("current")
_GtmWideipRuleWipName_Type = LongDisplayString
_GtmWideipRuleWipName_Object = MibTableColumn
gtmWideipRuleWipName = _GtmWideipRuleWipName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 6, 2, 1, 1),
    _GtmWideipRuleWipName_Type()
)
gtmWideipRuleWipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipRuleWipName.setStatus("current")
_GtmWideipRuleRuleName_Type = LongDisplayString
_GtmWideipRuleRuleName_Object = MibTableColumn
gtmWideipRuleRuleName = _GtmWideipRuleRuleName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 6, 2, 1, 2),
    _GtmWideipRuleRuleName_Type()
)
gtmWideipRuleRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipRuleRuleName.setStatus("current")
_GtmWideipRulePriority_Type = Integer32
_GtmWideipRulePriority_Object = MibTableColumn
gtmWideipRulePriority = _GtmWideipRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 12, 6, 2, 1, 3),
    _GtmWideipRulePriority_Type()
)
gtmWideipRulePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmWideipRulePriority.setStatus("current")
_GtmProberPools_ObjectIdentity = ObjectIdentity
gtmProberPools = _GtmProberPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13)
)
_GtmProberPool_ObjectIdentity = ObjectIdentity
gtmProberPool = _GtmProberPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 1)
)
_GtmProberPoolNumber_Type = Integer32
_GtmProberPoolNumber_Object = MibScalar
gtmProberPoolNumber = _GtmProberPoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 1, 1),
    _GtmProberPoolNumber_Type()
)
gtmProberPoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolNumber.setStatus("current")
_GtmProberPoolTable_Object = MibTable
gtmProberPoolTable = _GtmProberPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 1, 2)
)
if mibBuilder.loadTexts:
    gtmProberPoolTable.setStatus("current")
_GtmProberPoolEntry_Object = MibTableRow
gtmProberPoolEntry = _GtmProberPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 1, 2, 1)
)
gtmProberPoolEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmProberPoolName"),
)
if mibBuilder.loadTexts:
    gtmProberPoolEntry.setStatus("current")
_GtmProberPoolName_Type = LongDisplayString
_GtmProberPoolName_Object = MibTableColumn
gtmProberPoolName = _GtmProberPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 1, 2, 1, 1),
    _GtmProberPoolName_Type()
)
gtmProberPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolName.setStatus("current")


class _GtmProberPoolLbMode_Type(Integer32):
    """Custom type gtmProberPoolLbMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ga", 6),
          ("roundrobin", 2))
    )


_GtmProberPoolLbMode_Type.__name__ = "Integer32"
_GtmProberPoolLbMode_Object = MibTableColumn
gtmProberPoolLbMode = _GtmProberPoolLbMode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 1, 2, 1, 2),
    _GtmProberPoolLbMode_Type()
)
gtmProberPoolLbMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolLbMode.setStatus("current")


class _GtmProberPoolEnabled_Type(Integer32):
    """Custom type gtmProberPoolEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmProberPoolEnabled_Type.__name__ = "Integer32"
_GtmProberPoolEnabled_Object = MibTableColumn
gtmProberPoolEnabled = _GtmProberPoolEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 1, 2, 1, 3),
    _GtmProberPoolEnabled_Type()
)
gtmProberPoolEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolEnabled.setStatus("current")
_GtmProberPoolStat_ObjectIdentity = ObjectIdentity
gtmProberPoolStat = _GtmProberPoolStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 2)
)
_GtmProberPoolStatResetStats_Type = Integer32
_GtmProberPoolStatResetStats_Object = MibScalar
gtmProberPoolStatResetStats = _GtmProberPoolStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 2, 1),
    _GtmProberPoolStatResetStats_Type()
)
gtmProberPoolStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtmProberPoolStatResetStats.setStatus("current")
_GtmProberPoolStatNumber_Type = Integer32
_GtmProberPoolStatNumber_Object = MibScalar
gtmProberPoolStatNumber = _GtmProberPoolStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 2, 2),
    _GtmProberPoolStatNumber_Type()
)
gtmProberPoolStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolStatNumber.setStatus("current")
_GtmProberPoolStatTable_Object = MibTable
gtmProberPoolStatTable = _GtmProberPoolStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 2, 3)
)
if mibBuilder.loadTexts:
    gtmProberPoolStatTable.setStatus("current")
_GtmProberPoolStatEntry_Object = MibTableRow
gtmProberPoolStatEntry = _GtmProberPoolStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 2, 3, 1)
)
gtmProberPoolStatEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmProberPoolStatName"),
)
if mibBuilder.loadTexts:
    gtmProberPoolStatEntry.setStatus("current")
_GtmProberPoolStatName_Type = LongDisplayString
_GtmProberPoolStatName_Object = MibTableColumn
gtmProberPoolStatName = _GtmProberPoolStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 2, 3, 1, 1),
    _GtmProberPoolStatName_Type()
)
gtmProberPoolStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolStatName.setStatus("current")
_GtmProberPoolStatTotalProbes_Type = Counter64
_GtmProberPoolStatTotalProbes_Object = MibTableColumn
gtmProberPoolStatTotalProbes = _GtmProberPoolStatTotalProbes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 2, 3, 1, 2),
    _GtmProberPoolStatTotalProbes_Type()
)
gtmProberPoolStatTotalProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolStatTotalProbes.setStatus("current")
_GtmProberPoolStatSuccessfulProbes_Type = Counter64
_GtmProberPoolStatSuccessfulProbes_Object = MibTableColumn
gtmProberPoolStatSuccessfulProbes = _GtmProberPoolStatSuccessfulProbes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 2, 3, 1, 3),
    _GtmProberPoolStatSuccessfulProbes_Type()
)
gtmProberPoolStatSuccessfulProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolStatSuccessfulProbes.setStatus("current")
_GtmProberPoolStatFailedProbes_Type = Counter64
_GtmProberPoolStatFailedProbes_Object = MibTableColumn
gtmProberPoolStatFailedProbes = _GtmProberPoolStatFailedProbes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 2, 3, 1, 4),
    _GtmProberPoolStatFailedProbes_Type()
)
gtmProberPoolStatFailedProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolStatFailedProbes.setStatus("current")
_GtmProberPoolStatus_ObjectIdentity = ObjectIdentity
gtmProberPoolStatus = _GtmProberPoolStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 3)
)
_GtmProberPoolStatusNumber_Type = Integer32
_GtmProberPoolStatusNumber_Object = MibScalar
gtmProberPoolStatusNumber = _GtmProberPoolStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 3, 1),
    _GtmProberPoolStatusNumber_Type()
)
gtmProberPoolStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolStatusNumber.setStatus("current")
_GtmProberPoolStatusTable_Object = MibTable
gtmProberPoolStatusTable = _GtmProberPoolStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 3, 2)
)
if mibBuilder.loadTexts:
    gtmProberPoolStatusTable.setStatus("current")
_GtmProberPoolStatusEntry_Object = MibTableRow
gtmProberPoolStatusEntry = _GtmProberPoolStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 3, 2, 1)
)
gtmProberPoolStatusEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmProberPoolStatusName"),
)
if mibBuilder.loadTexts:
    gtmProberPoolStatusEntry.setStatus("current")
_GtmProberPoolStatusName_Type = LongDisplayString
_GtmProberPoolStatusName_Object = MibTableColumn
gtmProberPoolStatusName = _GtmProberPoolStatusName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 3, 2, 1, 1),
    _GtmProberPoolStatusName_Type()
)
gtmProberPoolStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolStatusName.setStatus("current")


class _GtmProberPoolStatusAvailState_Type(Integer32):
    """Custom type gtmProberPoolStatusAvailState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blue", 4),
          ("gray", 5),
          ("green", 1),
          ("none", 0),
          ("red", 3),
          ("yellow", 2))
    )


_GtmProberPoolStatusAvailState_Type.__name__ = "Integer32"
_GtmProberPoolStatusAvailState_Object = MibTableColumn
gtmProberPoolStatusAvailState = _GtmProberPoolStatusAvailState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 3, 2, 1, 2),
    _GtmProberPoolStatusAvailState_Type()
)
gtmProberPoolStatusAvailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolStatusAvailState.setStatus("current")


class _GtmProberPoolStatusEnabledState_Type(Integer32):
    """Custom type gtmProberPoolStatusEnabledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("disabledbyparent", 3),
          ("enabled", 1),
          ("none", 0))
    )


_GtmProberPoolStatusEnabledState_Type.__name__ = "Integer32"
_GtmProberPoolStatusEnabledState_Object = MibTableColumn
gtmProberPoolStatusEnabledState = _GtmProberPoolStatusEnabledState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 3, 2, 1, 3),
    _GtmProberPoolStatusEnabledState_Type()
)
gtmProberPoolStatusEnabledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolStatusEnabledState.setStatus("current")
_GtmProberPoolStatusDetailReason_Type = LongDisplayString
_GtmProberPoolStatusDetailReason_Object = MibTableColumn
gtmProberPoolStatusDetailReason = _GtmProberPoolStatusDetailReason_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 3, 2, 1, 4),
    _GtmProberPoolStatusDetailReason_Type()
)
gtmProberPoolStatusDetailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolStatusDetailReason.setStatus("current")
_GtmProberPoolMember_ObjectIdentity = ObjectIdentity
gtmProberPoolMember = _GtmProberPoolMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 4)
)
_GtmProberPoolMbrNumber_Type = Integer32
_GtmProberPoolMbrNumber_Object = MibScalar
gtmProberPoolMbrNumber = _GtmProberPoolMbrNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 4, 1),
    _GtmProberPoolMbrNumber_Type()
)
gtmProberPoolMbrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolMbrNumber.setStatus("current")
_GtmProberPoolMbrTable_Object = MibTable
gtmProberPoolMbrTable = _GtmProberPoolMbrTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 4, 2)
)
if mibBuilder.loadTexts:
    gtmProberPoolMbrTable.setStatus("current")
_GtmProberPoolMbrEntry_Object = MibTableRow
gtmProberPoolMbrEntry = _GtmProberPoolMbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 4, 2, 1)
)
gtmProberPoolMbrEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrPoolName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrServerName"),
)
if mibBuilder.loadTexts:
    gtmProberPoolMbrEntry.setStatus("current")
_GtmProberPoolMbrPoolName_Type = LongDisplayString
_GtmProberPoolMbrPoolName_Object = MibTableColumn
gtmProberPoolMbrPoolName = _GtmProberPoolMbrPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 4, 2, 1, 1),
    _GtmProberPoolMbrPoolName_Type()
)
gtmProberPoolMbrPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolMbrPoolName.setStatus("current")
_GtmProberPoolMbrServerName_Type = LongDisplayString
_GtmProberPoolMbrServerName_Object = MibTableColumn
gtmProberPoolMbrServerName = _GtmProberPoolMbrServerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 4, 2, 1, 2),
    _GtmProberPoolMbrServerName_Type()
)
gtmProberPoolMbrServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolMbrServerName.setStatus("current")
_GtmProberPoolMbrPmbrOrder_Type = Integer32
_GtmProberPoolMbrPmbrOrder_Object = MibTableColumn
gtmProberPoolMbrPmbrOrder = _GtmProberPoolMbrPmbrOrder_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 4, 2, 1, 3),
    _GtmProberPoolMbrPmbrOrder_Type()
)
gtmProberPoolMbrPmbrOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolMbrPmbrOrder.setStatus("current")


class _GtmProberPoolMbrEnabled_Type(Integer32):
    """Custom type gtmProberPoolMbrEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_GtmProberPoolMbrEnabled_Type.__name__ = "Integer32"
_GtmProberPoolMbrEnabled_Object = MibTableColumn
gtmProberPoolMbrEnabled = _GtmProberPoolMbrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 4, 2, 1, 4),
    _GtmProberPoolMbrEnabled_Type()
)
gtmProberPoolMbrEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolMbrEnabled.setStatus("current")
_GtmProberPoolMemberStat_ObjectIdentity = ObjectIdentity
gtmProberPoolMemberStat = _GtmProberPoolMemberStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 5)
)
_GtmProberPoolMbrStatResetStats_Type = Integer32
_GtmProberPoolMbrStatResetStats_Object = MibScalar
gtmProberPoolMbrStatResetStats = _GtmProberPoolMbrStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 5, 1),
    _GtmProberPoolMbrStatResetStats_Type()
)
gtmProberPoolMbrStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatResetStats.setStatus("current")
_GtmProberPoolMbrStatNumber_Type = Integer32
_GtmProberPoolMbrStatNumber_Object = MibScalar
gtmProberPoolMbrStatNumber = _GtmProberPoolMbrStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 5, 2),
    _GtmProberPoolMbrStatNumber_Type()
)
gtmProberPoolMbrStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatNumber.setStatus("current")
_GtmProberPoolMbrStatTable_Object = MibTable
gtmProberPoolMbrStatTable = _GtmProberPoolMbrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 5, 3)
)
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatTable.setStatus("current")
_GtmProberPoolMbrStatEntry_Object = MibTableRow
gtmProberPoolMbrStatEntry = _GtmProberPoolMbrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 5, 3, 1)
)
gtmProberPoolMbrStatEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrStatPoolName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrStatServerName"),
)
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatEntry.setStatus("current")
_GtmProberPoolMbrStatPoolName_Type = LongDisplayString
_GtmProberPoolMbrStatPoolName_Object = MibTableColumn
gtmProberPoolMbrStatPoolName = _GtmProberPoolMbrStatPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 5, 3, 1, 1),
    _GtmProberPoolMbrStatPoolName_Type()
)
gtmProberPoolMbrStatPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatPoolName.setStatus("current")
_GtmProberPoolMbrStatServerName_Type = LongDisplayString
_GtmProberPoolMbrStatServerName_Object = MibTableColumn
gtmProberPoolMbrStatServerName = _GtmProberPoolMbrStatServerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 5, 3, 1, 2),
    _GtmProberPoolMbrStatServerName_Type()
)
gtmProberPoolMbrStatServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatServerName.setStatus("current")
_GtmProberPoolMbrStatTotalProbes_Type = Counter64
_GtmProberPoolMbrStatTotalProbes_Object = MibTableColumn
gtmProberPoolMbrStatTotalProbes = _GtmProberPoolMbrStatTotalProbes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 5, 3, 1, 3),
    _GtmProberPoolMbrStatTotalProbes_Type()
)
gtmProberPoolMbrStatTotalProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatTotalProbes.setStatus("current")
_GtmProberPoolMbrStatSuccessfulProbes_Type = Counter64
_GtmProberPoolMbrStatSuccessfulProbes_Object = MibTableColumn
gtmProberPoolMbrStatSuccessfulProbes = _GtmProberPoolMbrStatSuccessfulProbes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 5, 3, 1, 4),
    _GtmProberPoolMbrStatSuccessfulProbes_Type()
)
gtmProberPoolMbrStatSuccessfulProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatSuccessfulProbes.setStatus("current")
_GtmProberPoolMbrStatFailedProbes_Type = Counter64
_GtmProberPoolMbrStatFailedProbes_Object = MibTableColumn
gtmProberPoolMbrStatFailedProbes = _GtmProberPoolMbrStatFailedProbes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 5, 3, 1, 5),
    _GtmProberPoolMbrStatFailedProbes_Type()
)
gtmProberPoolMbrStatFailedProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatFailedProbes.setStatus("current")
_GtmProberPoolMemberStatus_ObjectIdentity = ObjectIdentity
gtmProberPoolMemberStatus = _GtmProberPoolMemberStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 6)
)
_GtmProberPoolMbrStatusNumber_Type = Integer32
_GtmProberPoolMbrStatusNumber_Object = MibScalar
gtmProberPoolMbrStatusNumber = _GtmProberPoolMbrStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 6, 1),
    _GtmProberPoolMbrStatusNumber_Type()
)
gtmProberPoolMbrStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatusNumber.setStatus("current")
_GtmProberPoolMbrStatusTable_Object = MibTable
gtmProberPoolMbrStatusTable = _GtmProberPoolMbrStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 6, 2)
)
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatusTable.setStatus("current")
_GtmProberPoolMbrStatusEntry_Object = MibTableRow
gtmProberPoolMbrStatusEntry = _GtmProberPoolMbrStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 6, 2, 1)
)
gtmProberPoolMbrStatusEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrStatusPoolName"),
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrStatusServerName"),
)
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatusEntry.setStatus("current")
_GtmProberPoolMbrStatusPoolName_Type = LongDisplayString
_GtmProberPoolMbrStatusPoolName_Object = MibTableColumn
gtmProberPoolMbrStatusPoolName = _GtmProberPoolMbrStatusPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 6, 2, 1, 1),
    _GtmProberPoolMbrStatusPoolName_Type()
)
gtmProberPoolMbrStatusPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatusPoolName.setStatus("current")
_GtmProberPoolMbrStatusServerName_Type = LongDisplayString
_GtmProberPoolMbrStatusServerName_Object = MibTableColumn
gtmProberPoolMbrStatusServerName = _GtmProberPoolMbrStatusServerName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 6, 2, 1, 2),
    _GtmProberPoolMbrStatusServerName_Type()
)
gtmProberPoolMbrStatusServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatusServerName.setStatus("current")


class _GtmProberPoolMbrStatusAvailState_Type(Integer32):
    """Custom type gtmProberPoolMbrStatusAvailState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blue", 4),
          ("gray", 5),
          ("green", 1),
          ("none", 0),
          ("red", 3),
          ("yellow", 2))
    )


_GtmProberPoolMbrStatusAvailState_Type.__name__ = "Integer32"
_GtmProberPoolMbrStatusAvailState_Object = MibTableColumn
gtmProberPoolMbrStatusAvailState = _GtmProberPoolMbrStatusAvailState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 6, 2, 1, 3),
    _GtmProberPoolMbrStatusAvailState_Type()
)
gtmProberPoolMbrStatusAvailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatusAvailState.setStatus("current")


class _GtmProberPoolMbrStatusEnabledState_Type(Integer32):
    """Custom type gtmProberPoolMbrStatusEnabledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("disabledbyparent", 3),
          ("enabled", 1),
          ("none", 0))
    )


_GtmProberPoolMbrStatusEnabledState_Type.__name__ = "Integer32"
_GtmProberPoolMbrStatusEnabledState_Object = MibTableColumn
gtmProberPoolMbrStatusEnabledState = _GtmProberPoolMbrStatusEnabledState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 6, 2, 1, 4),
    _GtmProberPoolMbrStatusEnabledState_Type()
)
gtmProberPoolMbrStatusEnabledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatusEnabledState.setStatus("current")
_GtmProberPoolMbrStatusDetailReason_Type = LongDisplayString
_GtmProberPoolMbrStatusDetailReason_Object = MibTableColumn
gtmProberPoolMbrStatusDetailReason = _GtmProberPoolMbrStatusDetailReason_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 13, 6, 2, 1, 5),
    _GtmProberPoolMbrStatusDetailReason_Type()
)
gtmProberPoolMbrStatusDetailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatusDetailReason.setStatus("current")
_GtmDNSSEC_ObjectIdentity = ObjectIdentity
gtmDNSSEC = _GtmDNSSEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14)
)
_GtmDnssecZoneStat_ObjectIdentity = ObjectIdentity
gtmDnssecZoneStat = _GtmDnssecZoneStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1)
)
_GtmDnssecZoneStatResetStats_Type = Integer32
_GtmDnssecZoneStatResetStats_Object = MibScalar
gtmDnssecZoneStatResetStats = _GtmDnssecZoneStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 1),
    _GtmDnssecZoneStatResetStats_Type()
)
gtmDnssecZoneStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatResetStats.setStatus("current")
_GtmDnssecZoneStatNumber_Type = Integer32
_GtmDnssecZoneStatNumber_Object = MibScalar
gtmDnssecZoneStatNumber = _GtmDnssecZoneStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 2),
    _GtmDnssecZoneStatNumber_Type()
)
gtmDnssecZoneStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatNumber.setStatus("current")
_GtmDnssecZoneStatTable_Object = MibTable
gtmDnssecZoneStatTable = _GtmDnssecZoneStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3)
)
if mibBuilder.loadTexts:
    gtmDnssecZoneStatTable.setStatus("current")
_GtmDnssecZoneStatEntry_Object = MibTableRow
gtmDnssecZoneStatEntry = _GtmDnssecZoneStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1)
)
gtmDnssecZoneStatEntry.setIndexNames(
    (0, "F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatName"),
)
if mibBuilder.loadTexts:
    gtmDnssecZoneStatEntry.setStatus("current")
_GtmDnssecZoneStatName_Type = LongDisplayString
_GtmDnssecZoneStatName_Object = MibTableColumn
gtmDnssecZoneStatName = _GtmDnssecZoneStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 1),
    _GtmDnssecZoneStatName_Type()
)
gtmDnssecZoneStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatName.setStatus("current")
_GtmDnssecZoneStatNsec3s_Type = Counter64
_GtmDnssecZoneStatNsec3s_Object = MibTableColumn
gtmDnssecZoneStatNsec3s = _GtmDnssecZoneStatNsec3s_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 2),
    _GtmDnssecZoneStatNsec3s_Type()
)
gtmDnssecZoneStatNsec3s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatNsec3s.setStatus("current")
_GtmDnssecZoneStatNsec3Nodata_Type = Counter64
_GtmDnssecZoneStatNsec3Nodata_Object = MibTableColumn
gtmDnssecZoneStatNsec3Nodata = _GtmDnssecZoneStatNsec3Nodata_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 3),
    _GtmDnssecZoneStatNsec3Nodata_Type()
)
gtmDnssecZoneStatNsec3Nodata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatNsec3Nodata.setStatus("current")
_GtmDnssecZoneStatNsec3Nxdomain_Type = Counter64
_GtmDnssecZoneStatNsec3Nxdomain_Object = MibTableColumn
gtmDnssecZoneStatNsec3Nxdomain = _GtmDnssecZoneStatNsec3Nxdomain_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 4),
    _GtmDnssecZoneStatNsec3Nxdomain_Type()
)
gtmDnssecZoneStatNsec3Nxdomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatNsec3Nxdomain.setStatus("current")
_GtmDnssecZoneStatNsec3Referral_Type = Counter64
_GtmDnssecZoneStatNsec3Referral_Object = MibTableColumn
gtmDnssecZoneStatNsec3Referral = _GtmDnssecZoneStatNsec3Referral_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 5),
    _GtmDnssecZoneStatNsec3Referral_Type()
)
gtmDnssecZoneStatNsec3Referral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatNsec3Referral.setStatus("current")
_GtmDnssecZoneStatNsec3Resalt_Type = Counter64
_GtmDnssecZoneStatNsec3Resalt_Object = MibTableColumn
gtmDnssecZoneStatNsec3Resalt = _GtmDnssecZoneStatNsec3Resalt_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 6),
    _GtmDnssecZoneStatNsec3Resalt_Type()
)
gtmDnssecZoneStatNsec3Resalt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatNsec3Resalt.setStatus("current")
_GtmDnssecZoneStatDnssecResponses_Type = Counter64
_GtmDnssecZoneStatDnssecResponses_Object = MibTableColumn
gtmDnssecZoneStatDnssecResponses = _GtmDnssecZoneStatDnssecResponses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 7),
    _GtmDnssecZoneStatDnssecResponses_Type()
)
gtmDnssecZoneStatDnssecResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatDnssecResponses.setStatus("current")
_GtmDnssecZoneStatDnssecDnskeyQueries_Type = Counter64
_GtmDnssecZoneStatDnssecDnskeyQueries_Object = MibTableColumn
gtmDnssecZoneStatDnssecDnskeyQueries = _GtmDnssecZoneStatDnssecDnskeyQueries_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 8),
    _GtmDnssecZoneStatDnssecDnskeyQueries_Type()
)
gtmDnssecZoneStatDnssecDnskeyQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatDnssecDnskeyQueries.setStatus("current")
_GtmDnssecZoneStatDnssecNsec3paramQueries_Type = Counter64
_GtmDnssecZoneStatDnssecNsec3paramQueries_Object = MibTableColumn
gtmDnssecZoneStatDnssecNsec3paramQueries = _GtmDnssecZoneStatDnssecNsec3paramQueries_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 9),
    _GtmDnssecZoneStatDnssecNsec3paramQueries_Type()
)
gtmDnssecZoneStatDnssecNsec3paramQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatDnssecNsec3paramQueries.setStatus("current")
_GtmDnssecZoneStatDnssecDsQueries_Type = Counter64
_GtmDnssecZoneStatDnssecDsQueries_Object = MibTableColumn
gtmDnssecZoneStatDnssecDsQueries = _GtmDnssecZoneStatDnssecDsQueries_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 10),
    _GtmDnssecZoneStatDnssecDsQueries_Type()
)
gtmDnssecZoneStatDnssecDsQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatDnssecDsQueries.setStatus("current")
_GtmDnssecZoneStatSigCryptoFailed_Type = Counter64
_GtmDnssecZoneStatSigCryptoFailed_Object = MibTableColumn
gtmDnssecZoneStatSigCryptoFailed = _GtmDnssecZoneStatSigCryptoFailed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 11),
    _GtmDnssecZoneStatSigCryptoFailed_Type()
)
gtmDnssecZoneStatSigCryptoFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatSigCryptoFailed.setStatus("current")
_GtmDnssecZoneStatSigSuccess_Type = Counter64
_GtmDnssecZoneStatSigSuccess_Object = MibTableColumn
gtmDnssecZoneStatSigSuccess = _GtmDnssecZoneStatSigSuccess_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 12),
    _GtmDnssecZoneStatSigSuccess_Type()
)
gtmDnssecZoneStatSigSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatSigSuccess.setStatus("current")
_GtmDnssecZoneStatSigFailed_Type = Counter64
_GtmDnssecZoneStatSigFailed_Object = MibTableColumn
gtmDnssecZoneStatSigFailed = _GtmDnssecZoneStatSigFailed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 13),
    _GtmDnssecZoneStatSigFailed_Type()
)
gtmDnssecZoneStatSigFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatSigFailed.setStatus("current")
_GtmDnssecZoneStatSigRrsetFailed_Type = Counter64
_GtmDnssecZoneStatSigRrsetFailed_Object = MibTableColumn
gtmDnssecZoneStatSigRrsetFailed = _GtmDnssecZoneStatSigRrsetFailed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 14),
    _GtmDnssecZoneStatSigRrsetFailed_Type()
)
gtmDnssecZoneStatSigRrsetFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatSigRrsetFailed.setStatus("current")
_GtmDnssecZoneStatConnectFlowFailed_Type = Counter64
_GtmDnssecZoneStatConnectFlowFailed_Object = MibTableColumn
gtmDnssecZoneStatConnectFlowFailed = _GtmDnssecZoneStatConnectFlowFailed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 15),
    _GtmDnssecZoneStatConnectFlowFailed_Type()
)
gtmDnssecZoneStatConnectFlowFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatConnectFlowFailed.setStatus("current")
_GtmDnssecZoneStatTowireFailed_Type = Counter64
_GtmDnssecZoneStatTowireFailed_Object = MibTableColumn
gtmDnssecZoneStatTowireFailed = _GtmDnssecZoneStatTowireFailed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 16),
    _GtmDnssecZoneStatTowireFailed_Type()
)
gtmDnssecZoneStatTowireFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatTowireFailed.setStatus("current")
_GtmDnssecZoneStatAxfrQueries_Type = Counter64
_GtmDnssecZoneStatAxfrQueries_Object = MibTableColumn
gtmDnssecZoneStatAxfrQueries = _GtmDnssecZoneStatAxfrQueries_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 17),
    _GtmDnssecZoneStatAxfrQueries_Type()
)
gtmDnssecZoneStatAxfrQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatAxfrQueries.setStatus("current")
_GtmDnssecZoneStatIxfrQueries_Type = Counter64
_GtmDnssecZoneStatIxfrQueries_Object = MibTableColumn
gtmDnssecZoneStatIxfrQueries = _GtmDnssecZoneStatIxfrQueries_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 18),
    _GtmDnssecZoneStatIxfrQueries_Type()
)
gtmDnssecZoneStatIxfrQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatIxfrQueries.setStatus("current")
_GtmDnssecZoneStatXfrStarts_Type = Counter64
_GtmDnssecZoneStatXfrStarts_Object = MibTableColumn
gtmDnssecZoneStatXfrStarts = _GtmDnssecZoneStatXfrStarts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 19),
    _GtmDnssecZoneStatXfrStarts_Type()
)
gtmDnssecZoneStatXfrStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatXfrStarts.setStatus("current")
_GtmDnssecZoneStatXfrCompletes_Type = Counter64
_GtmDnssecZoneStatXfrCompletes_Object = MibTableColumn
gtmDnssecZoneStatXfrCompletes = _GtmDnssecZoneStatXfrCompletes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 20),
    _GtmDnssecZoneStatXfrCompletes_Type()
)
gtmDnssecZoneStatXfrCompletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatXfrCompletes.setStatus("current")
_GtmDnssecZoneStatXfrMsgs_Type = Counter64
_GtmDnssecZoneStatXfrMsgs_Object = MibTableColumn
gtmDnssecZoneStatXfrMsgs = _GtmDnssecZoneStatXfrMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 21),
    _GtmDnssecZoneStatXfrMsgs_Type()
)
gtmDnssecZoneStatXfrMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatXfrMsgs.setStatus("current")
_GtmDnssecZoneStatXfrMasterMsgs_Type = Counter64
_GtmDnssecZoneStatXfrMasterMsgs_Object = MibTableColumn
gtmDnssecZoneStatXfrMasterMsgs = _GtmDnssecZoneStatXfrMasterMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 22),
    _GtmDnssecZoneStatXfrMasterMsgs_Type()
)
gtmDnssecZoneStatXfrMasterMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatXfrMasterMsgs.setStatus("current")
_GtmDnssecZoneStatXfrResponseAverageSize_Type = Counter64
_GtmDnssecZoneStatXfrResponseAverageSize_Object = MibTableColumn
gtmDnssecZoneStatXfrResponseAverageSize = _GtmDnssecZoneStatXfrResponseAverageSize_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 23),
    _GtmDnssecZoneStatXfrResponseAverageSize_Type()
)
gtmDnssecZoneStatXfrResponseAverageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatXfrResponseAverageSize.setStatus("current")
_GtmDnssecZoneStatXfrSerial_Type = Counter64
_GtmDnssecZoneStatXfrSerial_Object = MibTableColumn
gtmDnssecZoneStatXfrSerial = _GtmDnssecZoneStatXfrSerial_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 24),
    _GtmDnssecZoneStatXfrSerial_Type()
)
gtmDnssecZoneStatXfrSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatXfrSerial.setStatus("current")
_GtmDnssecZoneStatXfrMasterSerial_Type = Counter64
_GtmDnssecZoneStatXfrMasterSerial_Object = MibTableColumn
gtmDnssecZoneStatXfrMasterSerial = _GtmDnssecZoneStatXfrMasterSerial_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 3, 14, 1, 3, 1, 25),
    _GtmDnssecZoneStatXfrMasterSerial_Type()
)
gtmDnssecZoneStatXfrMasterSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtmDnssecZoneStatXfrMasterSerial.setStatus("current")
_BigipGlobalTMGroups_ObjectIdentity = ObjectIdentity
bigipGlobalTMGroups = _BigipGlobalTMGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3)
)

# Managed Objects groups

gtmAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 1)
)
gtmAttrGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmAttrDumpTopology"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrCacheLdns"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrAolAware"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrCheckStaticDepends"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrCheckDynamicDepends"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrDrainRequests"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrEnableResetsRipeness"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrFbRespectDepends"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrFbRespectAcl"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrDefaultAlternate"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrDefaultFallback"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrPersistMask"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrGtmSetsRecursion"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrQosFactorLcs"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrQosFactorRtt"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrQosFactorHops"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrQosFactorHitRatio"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrQosFactorPacketRate"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrQosFactorBps"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrQosFactorVsCapacity"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrQosFactorTopology"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrQosFactorConnRate"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrTimerRetryPathData"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrTimerGetAutoconfigData"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrTimerPersistCache"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrDefaultProbeLimit"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrDownThreshold"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrDownMultiple"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrPathTtl"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrTraceTtl"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrLdnsDuration"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrPathDuration"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrRttSampleCount"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrRttPacketLength"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrRttTimeout"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrMaxMonReqs"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrTraceroutePort"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrPathsNeverDie"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrProbeDisabledObjects"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrLinkLimitFactor"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrOverLimitLinkLimitFactor"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrLinkPrepaidFactor"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrLinkCompensateInbound"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrLinkCompensateOutbound"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrLinkCompensationHistory"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrMaxLinkOverLimitCount"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrLowerBoundPctRow"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrLowerBoundPctCol"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrAutoconf"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrAutosync"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrSyncNamedConf"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrSyncGroup"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrSyncTimeout"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrSyncZonesTimeout"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrTimeTolerance"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrTopologyLongestMatch"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrTopologyAclThreshold"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrStaticPersistCidr"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrStaticPersistV6Cidr"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrQosFactorVsScore"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrTimerSendKeepAlive"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrCertificateDepth"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttrMaxMemoryUsage"))
)
if mibBuilder.loadTexts:
    gtmAttrGroup.setStatus("current")

gtmGlobalLdnsProbeProtoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 2)
)
gtmGlobalLdnsProbeProtoGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmGlobalLdnsProbeProtoNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmGlobalLdnsProbeProtoIndex"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmGlobalLdnsProbeProtoType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmGlobalLdnsProbeProtoName"))
)
if mibBuilder.loadTexts:
    gtmGlobalLdnsProbeProtoGroup.setStatus("current")

gtmStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 3)
)
gtmStatGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmStatResetStats"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatRequests"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatResolutions"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatPersisted"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatPreferred"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatAlternate"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatFallback"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatDropped"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatExplicitIp"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatReturnToDns"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatReconnects"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatBytesReceived"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatBytesSent"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatNumBacklogged"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatBytesDropped"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatLdnses"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatPaths"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatReturnFromDns"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatCnameResolutions"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatARequests"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmStatAaaaRequests"))
)
if mibBuilder.loadTexts:
    gtmStatGroup.setStatus("current")

gtmAppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 4)
)
gtmAppGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmAppNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppPersist"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppTtlPersist"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppAvailability"))
)
if mibBuilder.loadTexts:
    gtmAppGroup.setStatus("current")

gtmAppStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 5)
)
gtmAppStatusGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmAppStatusNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppStatusName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppStatusAvailState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppStatusEnabledState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppStatusParentType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppStatusDetailReason"))
)
if mibBuilder.loadTexts:
    gtmAppStatusGroup.setStatus("current")

gtmAppContStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 6)
)
gtmAppContStatGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmAppContStatNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppContStatAppName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppContStatType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppContStatName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppContStatNumAvail"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppContStatAvailState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppContStatEnabledState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppContStatParentType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppContStatDetailReason"))
)
if mibBuilder.loadTexts:
    gtmAppContStatGroup.setStatus("current")

gtmAppContDisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 7)
)
gtmAppContDisGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmAppContDisNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppContDisAppName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppContDisType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAppContDisName"))
)
if mibBuilder.loadTexts:
    gtmAppContDisGroup.setStatus("current")

gtmDcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 8)
)
gtmDcGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmDcNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcLocation"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcContact"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcEnabled"))
)
if mibBuilder.loadTexts:
    gtmDcGroup.setStatus("current")

gtmDcStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 9)
)
gtmDcStatGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmDcStatResetStats"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcStatNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcStatName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcStatCpuUsage"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcStatMemAvail"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcStatBitsPerSecIn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcStatBitsPerSecOut"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcStatPktsPerSecIn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcStatPktsPerSecOut"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcStatConnections"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcStatConnRate"))
)
if mibBuilder.loadTexts:
    gtmDcStatGroup.setStatus("current")

gtmDcStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 10)
)
gtmDcStatusGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmDcStatusNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcStatusName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcStatusAvailState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcStatusEnabledState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcStatusParentType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDcStatusDetailReason"))
)
if mibBuilder.loadTexts:
    gtmDcStatusGroup.setStatus("current")

gtmIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 11)
)
gtmIpGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmIpNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmIpIpType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmIpIp"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmIpLinkName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmIpServerName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmIpUnitId"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmIpIpXlatedType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmIpIpXlated"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmIpDeviceName"))
)
if mibBuilder.loadTexts:
    gtmIpGroup.setStatus("current")

gtmLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 12)
)
gtmLinkGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmLinkNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkDcName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkIspName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkUplinkAddressType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkUplinkAddress"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitInCpuUsageEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitInMemAvailEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitInBitsPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitInPktsPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitInConnEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitInConnPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitInCpuUsage"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitInMemAvail"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitInBitsPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitInPktsPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitInConn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitInConnPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitOutCpuUsageEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitOutMemAvailEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitOutBitsPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitOutPktsPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitOutConnEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitOutConnPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitOutCpuUsage"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitOutMemAvail"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitOutBitsPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitOutPktsPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitOutConn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitOutConnPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitTotalCpuUsageEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitTotalMemAvailEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitTotalBitsPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitTotalPktsPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitTotalConnEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitTotalConnPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitTotalCpuUsage"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitTotalMemAvail"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitTotalBitsPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitTotalPktsPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitTotalConn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkLimitTotalConnPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkMonitorRule"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkDuplex"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkRatio"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkPrepaid"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkPrepaidInDollars"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkWeightingType"))
)
if mibBuilder.loadTexts:
    gtmLinkGroup.setStatus("current")

gtmLinkCostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 13)
)
gtmLinkCostGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmLinkCostNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkCostName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkCostIndex"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkCostUptoBps"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkCostDollarsPerMbps"))
)
if mibBuilder.loadTexts:
    gtmLinkCostGroup.setStatus("current")

gtmLinkStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 14)
)
gtmLinkStatGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatResetStats"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatRate"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatRateIn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatRateOut"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatRateNode"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatRateNodeIn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatRateNodeOut"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatRateVses"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatRateVsesIn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatRateVsesOut"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatLcsIn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatLcsOut"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatPaths"))
)
if mibBuilder.loadTexts:
    gtmLinkStatGroup.setStatus("current")

gtmLinkStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 15)
)
gtmLinkStatusGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatusNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatusName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatusAvailState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatusEnabledState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatusParentType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmLinkStatusDetailReason"))
)
if mibBuilder.loadTexts:
    gtmLinkStatusGroup.setStatus("current")

gtmPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 16)
)
gtmPoolGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmPoolNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolTtl"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolVerifyMember"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolDynamicRatio"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolAnswersToReturn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolLbMode"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolAlternate"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolFallback"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolManualResume"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolQosCoeffRtt"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolQosCoeffHops"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolQosCoeffTopology"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolQosCoeffHitRatio"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolQosCoeffPacketRate"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolQosCoeffVsCapacity"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolQosCoeffBps"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolQosCoeffLcs"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolQosCoeffConnRate"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolFallbackIpType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolFallbackIp"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolCname"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolLimitCpuUsageEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolLimitMemAvailEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolLimitBitsPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolLimitPktsPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolLimitConnEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolLimitConnPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolLimitCpuUsage"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolLimitMemAvail"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolLimitBitsPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolLimitPktsPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolLimitConn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolLimitConnPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMonitorRule"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolQosCoeffVsScore"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolFallbackIpv6Type"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolFallbackIpv6"))
)
if mibBuilder.loadTexts:
    gtmPoolGroup.setStatus("current")

gtmPoolStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 17)
)
gtmPoolStatGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmPoolStatResetStats"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolStatNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolStatName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolStatPreferred"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolStatAlternate"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolStatFallback"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolStatDropped"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolStatExplicitIp"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolStatReturnToDns"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolStatReturnFromDns"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolStatCnameResolutions"))
)
if mibBuilder.loadTexts:
    gtmPoolStatGroup.setStatus("current")

gtmPoolMbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 18)
)
gtmPoolMbrGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrPoolName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrIpType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrIp"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrPort"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrVsName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrOrder"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrLimitCpuUsageEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrLimitMemAvailEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrLimitBitsPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrLimitPktsPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrLimitConnEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrLimitConnPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrLimitCpuUsage"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrLimitMemAvail"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrLimitBitsPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrLimitPktsPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrLimitConn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrLimitConnPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrMonitorRule"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrRatio"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrServerName"))
)
if mibBuilder.loadTexts:
    gtmPoolMbrGroup.setStatus("current")

gtmPoolStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 19)
)
gtmPoolStatusGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmPoolStatusNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolStatusName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolStatusAvailState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolStatusEnabledState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolStatusParentType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolStatusDetailReason"))
)
if mibBuilder.loadTexts:
    gtmPoolStatusGroup.setStatus("current")

gtmPoolMbrDepsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 20)
)
gtmPoolMbrDepsGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrDepsNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrDepsIpType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrDepsIp"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrDepsPort"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrDepsPoolName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrDepsVipType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrDepsVip"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrDepsVport"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrDepsServerName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrDepsVsName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrDepsDependServerName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrDepsDependVsName"))
)
if mibBuilder.loadTexts:
    gtmPoolMbrDepsGroup.setStatus("current")

gtmPoolMbrStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 21)
)
gtmPoolMbrStatGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatResetStats"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatPoolName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatIpType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatIp"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatPort"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatPreferred"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatAlternate"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatFallback"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatServerName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatVsName"))
)
if mibBuilder.loadTexts:
    gtmPoolMbrStatGroup.setStatus("current")

gtmPoolMbrStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 22)
)
gtmPoolMbrStatusGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatusNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatusPoolName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatusIpType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatusIp"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatusPort"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatusAvailState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatusEnabledState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatusParentType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatusDetailReason"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatusVsName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmPoolMbrStatusServerName"))
)
if mibBuilder.loadTexts:
    gtmPoolMbrStatusGroup.setStatus("current")

gtmRegionEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 23)
)
gtmRegionEntryGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmRegionEntryNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRegionEntryName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRegionEntryRegionDbType"))
)
if mibBuilder.loadTexts:
    gtmRegionEntryGroup.setStatus("current")

gtmRegItemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 24)
)
gtmRegItemGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmRegItemNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRegItemRegionDbType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRegItemRegionName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRegItemType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRegItemNegate"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRegItemRegEntry"))
)
if mibBuilder.loadTexts:
    gtmRegItemGroup.setStatus("current")

gtmRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 25)
)
gtmRuleGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmRuleNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRuleName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRuleDefinition"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRuleConfigSource"))
)
if mibBuilder.loadTexts:
    gtmRuleGroup.setStatus("current")

gtmRuleEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 26)
)
gtmRuleEventGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmRuleEventNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRuleEventName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRuleEventEventType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRuleEventPriority"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRuleEventScript"))
)
if mibBuilder.loadTexts:
    gtmRuleEventGroup.setStatus("current")

gtmRuleEventStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 27)
)
gtmRuleEventStatGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmRuleEventStatResetStats"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRuleEventStatNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRuleEventStatName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRuleEventStatEventType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRuleEventStatPriority"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRuleEventStatFailures"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRuleEventStatAborts"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmRuleEventStatTotalExecutions"))
)
if mibBuilder.loadTexts:
    gtmRuleEventStatGroup.setStatus("current")

gtmServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 28)
)
gtmServerGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmServerNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerDcName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerLimitCpuUsageEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerLimitMemAvailEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerLimitBitsPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerLimitPktsPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerLimitConnEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerLimitConnPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerLimitCpuUsage"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerLimitMemAvail"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerLimitBitsPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerLimitPktsPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerLimitConn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerLimitConnPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerProberType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerProber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerMonitorRule"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerAllowSvcChk"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerAllowPath"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerAllowSnmp"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerAutoconfState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerLinkAutoconfState"))
)
if mibBuilder.loadTexts:
    gtmServerGroup.setStatus("current")

gtmServerStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 29)
)
gtmServerStatGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmServerStatResetStats"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStatNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStatName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStatUnitId"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStatVsPicks"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStatCpuUsage"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStatMemAvail"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStatBitsPerSecIn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStatBitsPerSecOut"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStatPktsPerSecIn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStatPktsPerSecOut"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStatConnections"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStatConnRate"))
)
if mibBuilder.loadTexts:
    gtmServerStatGroup.setStatus("current")

gtmServerStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 30)
)
gtmServerStatusGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmServerStatusNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStatusName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStatusAvailState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStatusEnabledState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStatusParentType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStatusDetailReason"))
)
if mibBuilder.loadTexts:
    gtmServerStatusGroup.setStatus("current")

gtmTopItemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 31)
)
gtmTopItemGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmTopItemNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmTopItemLdnsType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmTopItemLdnsNegate"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmTopItemLdnsEntry"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmTopItemServerType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmTopItemServerNegate"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmTopItemServerEntry"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmTopItemWeight"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmTopItemOrder"))
)
if mibBuilder.loadTexts:
    gtmTopItemGroup.setStatus("current")

gtmVsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 32)
)
gtmVsGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmVsNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsIpType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsIp"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsPort"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsServerName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsIpXlatedType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsIpXlated"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsPortXlated"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsLimitCpuUsageEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsLimitMemAvailEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsLimitBitsPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsLimitPktsPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsLimitConnEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsLimitConnPerSecEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsLimitCpuUsage"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsLimitMemAvail"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsLimitBitsPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsLimitPktsPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsLimitConn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsLimitConnPerSec"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsMonitorRule"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsLinkName"))
)
if mibBuilder.loadTexts:
    gtmVsGroup.setStatus("current")

gtmVsDepsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 33)
)
gtmVsDepsGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmVsDepsNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsDepsIpType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsDepsIp"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsDepsPort"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsDepsVipType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsDepsVip"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsDepsVport"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsDepsServerName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsDepsVsName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsDepsDependServerName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsDepsDependVsName"))
)
if mibBuilder.loadTexts:
    gtmVsDepsGroup.setStatus("current")

gtmVsStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 34)
)
gtmVsStatGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmVsStatResetStats"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatIpType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatIp"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatPort"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatCpuUsage"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatMemAvail"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatBitsPerSecIn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatBitsPerSecOut"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatPktsPerSecIn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatPktsPerSecOut"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatConnections"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatConnRate"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatVsScore"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatServerName"))
)
if mibBuilder.loadTexts:
    gtmVsStatGroup.setStatus("current")

gtmVsStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 35)
)
gtmVsStatusGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmVsStatusNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatusIpType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatusIp"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatusPort"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatusAvailState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatusEnabledState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatusParentType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatusDetailReason"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatusVsName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmVsStatusServerName"))
)
if mibBuilder.loadTexts:
    gtmVsStatusGroup.setStatus("current")

gtmWideipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 36)
)
gtmWideipGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmWideipNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipPersist"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipTtlPersist"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipEnabled"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipLbmodePool"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipApplication"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipLastResortPool"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipIpv6Noerror"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipLoadBalancingDecisionLogVerbosity"))
)
if mibBuilder.loadTexts:
    gtmWideipGroup.setStatus("current")

gtmWideipStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 37)
)
gtmWideipStatGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatResetStats"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatRequests"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatResolutions"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatPersisted"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatPreferred"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatFallback"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatDropped"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatExplicitIp"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatReturnToDns"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatReturnFromDns"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatCnameResolutions"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatARequests"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatAaaaRequests"))
)
if mibBuilder.loadTexts:
    gtmWideipStatGroup.setStatus("current")

gtmWideipStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 38)
)
gtmWideipStatusGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatusNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatusName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatusAvailState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatusEnabledState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatusParentType"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipStatusDetailReason"))
)
if mibBuilder.loadTexts:
    gtmWideipStatusGroup.setStatus("current")

gtmWideipAliasGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 39)
)
gtmWideipAliasGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmWideipAliasNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipAliasWipName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipAliasName"))
)
if mibBuilder.loadTexts:
    gtmWideipAliasGroup.setStatus("current")

gtmWideipPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 40)
)
gtmWideipPoolGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmWideipPoolNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipPoolWipName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipPoolPoolName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipPoolOrder"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipPoolRatio"))
)
if mibBuilder.loadTexts:
    gtmWideipPoolGroup.setStatus("current")

gtmWideipRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 41)
)
gtmWideipRuleGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmWideipRuleNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipRuleWipName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipRuleRuleName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmWideipRulePriority"))
)
if mibBuilder.loadTexts:
    gtmWideipRuleGroup.setStatus("current")

gtmServerStat2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 42)
)
gtmServerStat2Group.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmServerStat2Number"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStat2Name"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStat2UnitId"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStat2VsPicks"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStat2CpuUsage"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStat2MemAvail"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStat2BitsPerSecIn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStat2BitsPerSecOut"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStat2PktsPerSecIn"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStat2PktsPerSecOut"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStat2Connections"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmServerStat2ConnRate"))
)
if mibBuilder.loadTexts:
    gtmServerStat2Group.setStatus("current")

gtmProberPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 43)
)
gtmProberPoolGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolLbMode"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolEnabled"))
)
if mibBuilder.loadTexts:
    gtmProberPoolGroup.setStatus("current")

gtmProberPoolStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 44)
)
gtmProberPoolStatGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolStatResetStats"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolStatNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolStatName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolStatTotalProbes"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolStatSuccessfulProbes"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolStatFailedProbes"))
)
if mibBuilder.loadTexts:
    gtmProberPoolStatGroup.setStatus("current")

gtmProberPoolStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 45)
)
gtmProberPoolStatusGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolStatusNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolStatusName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolStatusAvailState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolStatusEnabledState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolStatusDetailReason"))
)
if mibBuilder.loadTexts:
    gtmProberPoolStatusGroup.setStatus("current")

gtmProberPoolMbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 46)
)
gtmProberPoolMbrGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrPoolName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrServerName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrPmbrOrder"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrEnabled"))
)
if mibBuilder.loadTexts:
    gtmProberPoolMbrGroup.setStatus("current")

gtmProberPoolMbrStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 47)
)
gtmProberPoolMbrStatGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrStatResetStats"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrStatNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrStatPoolName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrStatServerName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrStatTotalProbes"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrStatSuccessfulProbes"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrStatFailedProbes"))
)
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatGroup.setStatus("current")

gtmProberPoolMbrStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 48)
)
gtmProberPoolMbrStatusGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrStatusNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrStatusPoolName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrStatusServerName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrStatusAvailState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrStatusEnabledState"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmProberPoolMbrStatusDetailReason"))
)
if mibBuilder.loadTexts:
    gtmProberPoolMbrStatusGroup.setStatus("current")

gtmAttr2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 49)
)
gtmAttr2Group.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmAttr2Number"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2DumpTopology"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2CacheLdns"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2AolAware"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2CheckStaticDepends"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2CheckDynamicDepends"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2DrainRequests"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2EnableResetsRipeness"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2FbRespectDepends"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2FbRespectAcl"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2DefaultAlternate"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2DefaultFallback"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2PersistMask"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2GtmSetsRecursion"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2QosFactorLcs"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2QosFactorRtt"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2QosFactorHops"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2QosFactorHitRatio"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2QosFactorPacketRate"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2QosFactorBps"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2QosFactorVsCapacity"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2QosFactorTopology"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2QosFactorConnRate"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2TimerRetryPathData"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2TimerGetAutoconfigData"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2TimerPersistCache"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2DefaultProbeLimit"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2DownThreshold"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2DownMultiple"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2PathTtl"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2TraceTtl"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2LdnsDuration"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2PathDuration"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2RttSampleCount"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2RttPacketLength"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2RttTimeout"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2MaxMonReqs"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2TraceroutePort"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2PathsNeverDie"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2ProbeDisabledObjects"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2LinkLimitFactor"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2OverLimitLinkLimitFactor"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2LinkPrepaidFactor"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2LinkCompensateInbound"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2LinkCompensateOutbound"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2LinkCompensationHistory"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2MaxLinkOverLimitCount"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2LowerBoundPctRow"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2LowerBoundPctCol"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2Autoconf"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2Autosync"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2SyncNamedConf"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2SyncGroup"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2SyncTimeout"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2SyncZonesTimeout"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2TimeTolerance"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2TopologyLongestMatch"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2TopologyAclThreshold"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2StaticPersistCidr"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2StaticPersistV6Cidr"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2QosFactorVsScore"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2TimerSendKeepAlive"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2CertificateDepth"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2MaxMemoryUsage"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2Name"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmAttr2ForwardStatus"))
)
if mibBuilder.loadTexts:
    gtmAttr2Group.setStatus("current")

gtmDnssecZoneStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 50)
)
gtmDnssecZoneStatGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatResetStats"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatNumber"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatName"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatNsec3s"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatNsec3Nodata"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatNsec3Nxdomain"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatNsec3Referral"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatNsec3Resalt"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatDnssecResponses"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatDnssecDnskeyQueries"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatDnssecNsec3paramQueries"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatDnssecDsQueries"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatSigCryptoFailed"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatSigSuccess"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatSigFailed"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatSigRrsetFailed"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatConnectFlowFailed"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatTowireFailed"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatAxfrQueries"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatIxfrQueries"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatXfrStarts"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatXfrCompletes"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatXfrMsgs"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatXfrMasterMsgs"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatXfrResponseAverageSize"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatXfrSerial"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecZoneStatXfrMasterSerial"))
)
if mibBuilder.loadTexts:
    gtmDnssecZoneStatGroup.setStatus("current")

gtmDnssecStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 3, 51)
)
gtmDnssecStatGroup.setObjects(
      *(("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatResetStats"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatNsec3s"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatNsec3Nodata"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatNsec3Nxdomain"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatNsec3Referral"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatNsec3Resalt"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatDnssecResponses"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatDnssecDnskeyQueries"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatDnssecNsec3paramQueries"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatDnssecDsQueries"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatSigCryptoFailed"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatSigSuccess"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatSigFailed"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatSigRrsetFailed"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatConnectFlowFailed"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatTowireFailed"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatAxfrQueries"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatIxfrQueries"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatXfrStarts"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatXfrCompletes"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatXfrMsgs"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatXfrMasterMsgs"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatXfrResponseAverageSize"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatXfrSerial"),
        ("F5-BIGIP-GLOBAL-MIB", "gtmDnssecStatXfrMasterSerial"))
)
if mibBuilder.loadTexts:
    gtmDnssecStatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bigipGlobalTMCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 1, 3)
)
if mibBuilder.loadTexts:
    bigipGlobalTMCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F5-BIGIP-GLOBAL-MIB",
    **{"bigipGlobalTM": bigipGlobalTM,
       "gtmGlobals": gtmGlobals,
       "gtmGlobalAttrs": gtmGlobalAttrs,
       "gtmGlobalAttr": gtmGlobalAttr,
       "gtmAttrDumpTopology": gtmAttrDumpTopology,
       "gtmAttrCacheLdns": gtmAttrCacheLdns,
       "gtmAttrAolAware": gtmAttrAolAware,
       "gtmAttrCheckStaticDepends": gtmAttrCheckStaticDepends,
       "gtmAttrCheckDynamicDepends": gtmAttrCheckDynamicDepends,
       "gtmAttrDrainRequests": gtmAttrDrainRequests,
       "gtmAttrEnableResetsRipeness": gtmAttrEnableResetsRipeness,
       "gtmAttrFbRespectDepends": gtmAttrFbRespectDepends,
       "gtmAttrFbRespectAcl": gtmAttrFbRespectAcl,
       "gtmAttrDefaultAlternate": gtmAttrDefaultAlternate,
       "gtmAttrDefaultFallback": gtmAttrDefaultFallback,
       "gtmAttrPersistMask": gtmAttrPersistMask,
       "gtmAttrGtmSetsRecursion": gtmAttrGtmSetsRecursion,
       "gtmAttrQosFactorLcs": gtmAttrQosFactorLcs,
       "gtmAttrQosFactorRtt": gtmAttrQosFactorRtt,
       "gtmAttrQosFactorHops": gtmAttrQosFactorHops,
       "gtmAttrQosFactorHitRatio": gtmAttrQosFactorHitRatio,
       "gtmAttrQosFactorPacketRate": gtmAttrQosFactorPacketRate,
       "gtmAttrQosFactorBps": gtmAttrQosFactorBps,
       "gtmAttrQosFactorVsCapacity": gtmAttrQosFactorVsCapacity,
       "gtmAttrQosFactorTopology": gtmAttrQosFactorTopology,
       "gtmAttrQosFactorConnRate": gtmAttrQosFactorConnRate,
       "gtmAttrTimerRetryPathData": gtmAttrTimerRetryPathData,
       "gtmAttrTimerGetAutoconfigData": gtmAttrTimerGetAutoconfigData,
       "gtmAttrTimerPersistCache": gtmAttrTimerPersistCache,
       "gtmAttrDefaultProbeLimit": gtmAttrDefaultProbeLimit,
       "gtmAttrDownThreshold": gtmAttrDownThreshold,
       "gtmAttrDownMultiple": gtmAttrDownMultiple,
       "gtmAttrPathTtl": gtmAttrPathTtl,
       "gtmAttrTraceTtl": gtmAttrTraceTtl,
       "gtmAttrLdnsDuration": gtmAttrLdnsDuration,
       "gtmAttrPathDuration": gtmAttrPathDuration,
       "gtmAttrRttSampleCount": gtmAttrRttSampleCount,
       "gtmAttrRttPacketLength": gtmAttrRttPacketLength,
       "gtmAttrRttTimeout": gtmAttrRttTimeout,
       "gtmAttrMaxMonReqs": gtmAttrMaxMonReqs,
       "gtmAttrTraceroutePort": gtmAttrTraceroutePort,
       "gtmAttrPathsNeverDie": gtmAttrPathsNeverDie,
       "gtmAttrProbeDisabledObjects": gtmAttrProbeDisabledObjects,
       "gtmAttrLinkLimitFactor": gtmAttrLinkLimitFactor,
       "gtmAttrOverLimitLinkLimitFactor": gtmAttrOverLimitLinkLimitFactor,
       "gtmAttrLinkPrepaidFactor": gtmAttrLinkPrepaidFactor,
       "gtmAttrLinkCompensateInbound": gtmAttrLinkCompensateInbound,
       "gtmAttrLinkCompensateOutbound": gtmAttrLinkCompensateOutbound,
       "gtmAttrLinkCompensationHistory": gtmAttrLinkCompensationHistory,
       "gtmAttrMaxLinkOverLimitCount": gtmAttrMaxLinkOverLimitCount,
       "gtmAttrLowerBoundPctRow": gtmAttrLowerBoundPctRow,
       "gtmAttrLowerBoundPctCol": gtmAttrLowerBoundPctCol,
       "gtmAttrAutoconf": gtmAttrAutoconf,
       "gtmAttrAutosync": gtmAttrAutosync,
       "gtmAttrSyncNamedConf": gtmAttrSyncNamedConf,
       "gtmAttrSyncGroup": gtmAttrSyncGroup,
       "gtmAttrSyncTimeout": gtmAttrSyncTimeout,
       "gtmAttrSyncZonesTimeout": gtmAttrSyncZonesTimeout,
       "gtmAttrTimeTolerance": gtmAttrTimeTolerance,
       "gtmAttrTopologyLongestMatch": gtmAttrTopologyLongestMatch,
       "gtmAttrTopologyAclThreshold": gtmAttrTopologyAclThreshold,
       "gtmAttrStaticPersistCidr": gtmAttrStaticPersistCidr,
       "gtmAttrStaticPersistV6Cidr": gtmAttrStaticPersistV6Cidr,
       "gtmAttrQosFactorVsScore": gtmAttrQosFactorVsScore,
       "gtmAttrTimerSendKeepAlive": gtmAttrTimerSendKeepAlive,
       "gtmAttrCertificateDepth": gtmAttrCertificateDepth,
       "gtmAttrMaxMemoryUsage": gtmAttrMaxMemoryUsage,
       "gtmGlobalLdnsProbeProto": gtmGlobalLdnsProbeProto,
       "gtmGlobalLdnsProbeProtoNumber": gtmGlobalLdnsProbeProtoNumber,
       "gtmGlobalLdnsProbeProtoTable": gtmGlobalLdnsProbeProtoTable,
       "gtmGlobalLdnsProbeProtoEntry": gtmGlobalLdnsProbeProtoEntry,
       "gtmGlobalLdnsProbeProtoIndex": gtmGlobalLdnsProbeProtoIndex,
       "gtmGlobalLdnsProbeProtoType": gtmGlobalLdnsProbeProtoType,
       "gtmGlobalLdnsProbeProtoName": gtmGlobalLdnsProbeProtoName,
       "gtmGlobalAttr2": gtmGlobalAttr2,
       "gtmAttr2Number": gtmAttr2Number,
       "gtmAttr2Table": gtmAttr2Table,
       "gtmAttr2Entry": gtmAttr2Entry,
       "gtmAttr2DumpTopology": gtmAttr2DumpTopology,
       "gtmAttr2CacheLdns": gtmAttr2CacheLdns,
       "gtmAttr2AolAware": gtmAttr2AolAware,
       "gtmAttr2CheckStaticDepends": gtmAttr2CheckStaticDepends,
       "gtmAttr2CheckDynamicDepends": gtmAttr2CheckDynamicDepends,
       "gtmAttr2DrainRequests": gtmAttr2DrainRequests,
       "gtmAttr2EnableResetsRipeness": gtmAttr2EnableResetsRipeness,
       "gtmAttr2FbRespectDepends": gtmAttr2FbRespectDepends,
       "gtmAttr2FbRespectAcl": gtmAttr2FbRespectAcl,
       "gtmAttr2DefaultAlternate": gtmAttr2DefaultAlternate,
       "gtmAttr2DefaultFallback": gtmAttr2DefaultFallback,
       "gtmAttr2PersistMask": gtmAttr2PersistMask,
       "gtmAttr2GtmSetsRecursion": gtmAttr2GtmSetsRecursion,
       "gtmAttr2QosFactorLcs": gtmAttr2QosFactorLcs,
       "gtmAttr2QosFactorRtt": gtmAttr2QosFactorRtt,
       "gtmAttr2QosFactorHops": gtmAttr2QosFactorHops,
       "gtmAttr2QosFactorHitRatio": gtmAttr2QosFactorHitRatio,
       "gtmAttr2QosFactorPacketRate": gtmAttr2QosFactorPacketRate,
       "gtmAttr2QosFactorBps": gtmAttr2QosFactorBps,
       "gtmAttr2QosFactorVsCapacity": gtmAttr2QosFactorVsCapacity,
       "gtmAttr2QosFactorTopology": gtmAttr2QosFactorTopology,
       "gtmAttr2QosFactorConnRate": gtmAttr2QosFactorConnRate,
       "gtmAttr2TimerRetryPathData": gtmAttr2TimerRetryPathData,
       "gtmAttr2TimerGetAutoconfigData": gtmAttr2TimerGetAutoconfigData,
       "gtmAttr2TimerPersistCache": gtmAttr2TimerPersistCache,
       "gtmAttr2DefaultProbeLimit": gtmAttr2DefaultProbeLimit,
       "gtmAttr2DownThreshold": gtmAttr2DownThreshold,
       "gtmAttr2DownMultiple": gtmAttr2DownMultiple,
       "gtmAttr2PathTtl": gtmAttr2PathTtl,
       "gtmAttr2TraceTtl": gtmAttr2TraceTtl,
       "gtmAttr2LdnsDuration": gtmAttr2LdnsDuration,
       "gtmAttr2PathDuration": gtmAttr2PathDuration,
       "gtmAttr2RttSampleCount": gtmAttr2RttSampleCount,
       "gtmAttr2RttPacketLength": gtmAttr2RttPacketLength,
       "gtmAttr2RttTimeout": gtmAttr2RttTimeout,
       "gtmAttr2MaxMonReqs": gtmAttr2MaxMonReqs,
       "gtmAttr2TraceroutePort": gtmAttr2TraceroutePort,
       "gtmAttr2PathsNeverDie": gtmAttr2PathsNeverDie,
       "gtmAttr2ProbeDisabledObjects": gtmAttr2ProbeDisabledObjects,
       "gtmAttr2LinkLimitFactor": gtmAttr2LinkLimitFactor,
       "gtmAttr2OverLimitLinkLimitFactor": gtmAttr2OverLimitLinkLimitFactor,
       "gtmAttr2LinkPrepaidFactor": gtmAttr2LinkPrepaidFactor,
       "gtmAttr2LinkCompensateInbound": gtmAttr2LinkCompensateInbound,
       "gtmAttr2LinkCompensateOutbound": gtmAttr2LinkCompensateOutbound,
       "gtmAttr2LinkCompensationHistory": gtmAttr2LinkCompensationHistory,
       "gtmAttr2MaxLinkOverLimitCount": gtmAttr2MaxLinkOverLimitCount,
       "gtmAttr2LowerBoundPctRow": gtmAttr2LowerBoundPctRow,
       "gtmAttr2LowerBoundPctCol": gtmAttr2LowerBoundPctCol,
       "gtmAttr2Autoconf": gtmAttr2Autoconf,
       "gtmAttr2Autosync": gtmAttr2Autosync,
       "gtmAttr2SyncNamedConf": gtmAttr2SyncNamedConf,
       "gtmAttr2SyncGroup": gtmAttr2SyncGroup,
       "gtmAttr2SyncTimeout": gtmAttr2SyncTimeout,
       "gtmAttr2SyncZonesTimeout": gtmAttr2SyncZonesTimeout,
       "gtmAttr2TimeTolerance": gtmAttr2TimeTolerance,
       "gtmAttr2TopologyLongestMatch": gtmAttr2TopologyLongestMatch,
       "gtmAttr2TopologyAclThreshold": gtmAttr2TopologyAclThreshold,
       "gtmAttr2StaticPersistCidr": gtmAttr2StaticPersistCidr,
       "gtmAttr2StaticPersistV6Cidr": gtmAttr2StaticPersistV6Cidr,
       "gtmAttr2QosFactorVsScore": gtmAttr2QosFactorVsScore,
       "gtmAttr2TimerSendKeepAlive": gtmAttr2TimerSendKeepAlive,
       "gtmAttr2CertificateDepth": gtmAttr2CertificateDepth,
       "gtmAttr2MaxMemoryUsage": gtmAttr2MaxMemoryUsage,
       "gtmAttr2Name": gtmAttr2Name,
       "gtmAttr2ForwardStatus": gtmAttr2ForwardStatus,
       "gtmGlobalStats": gtmGlobalStats,
       "gtmGlobalStat": gtmGlobalStat,
       "gtmStatResetStats": gtmStatResetStats,
       "gtmStatRequests": gtmStatRequests,
       "gtmStatResolutions": gtmStatResolutions,
       "gtmStatPersisted": gtmStatPersisted,
       "gtmStatPreferred": gtmStatPreferred,
       "gtmStatAlternate": gtmStatAlternate,
       "gtmStatFallback": gtmStatFallback,
       "gtmStatDropped": gtmStatDropped,
       "gtmStatExplicitIp": gtmStatExplicitIp,
       "gtmStatReturnToDns": gtmStatReturnToDns,
       "gtmStatReconnects": gtmStatReconnects,
       "gtmStatBytesReceived": gtmStatBytesReceived,
       "gtmStatBytesSent": gtmStatBytesSent,
       "gtmStatNumBacklogged": gtmStatNumBacklogged,
       "gtmStatBytesDropped": gtmStatBytesDropped,
       "gtmStatLdnses": gtmStatLdnses,
       "gtmStatPaths": gtmStatPaths,
       "gtmStatReturnFromDns": gtmStatReturnFromDns,
       "gtmStatCnameResolutions": gtmStatCnameResolutions,
       "gtmStatARequests": gtmStatARequests,
       "gtmStatAaaaRequests": gtmStatAaaaRequests,
       "gtmGlobalDnssecStat": gtmGlobalDnssecStat,
       "gtmDnssecStatResetStats": gtmDnssecStatResetStats,
       "gtmDnssecStatNsec3s": gtmDnssecStatNsec3s,
       "gtmDnssecStatNsec3Nodata": gtmDnssecStatNsec3Nodata,
       "gtmDnssecStatNsec3Nxdomain": gtmDnssecStatNsec3Nxdomain,
       "gtmDnssecStatNsec3Referral": gtmDnssecStatNsec3Referral,
       "gtmDnssecStatNsec3Resalt": gtmDnssecStatNsec3Resalt,
       "gtmDnssecStatDnssecResponses": gtmDnssecStatDnssecResponses,
       "gtmDnssecStatDnssecDnskeyQueries": gtmDnssecStatDnssecDnskeyQueries,
       "gtmDnssecStatDnssecNsec3paramQueries": gtmDnssecStatDnssecNsec3paramQueries,
       "gtmDnssecStatDnssecDsQueries": gtmDnssecStatDnssecDsQueries,
       "gtmDnssecStatSigCryptoFailed": gtmDnssecStatSigCryptoFailed,
       "gtmDnssecStatSigSuccess": gtmDnssecStatSigSuccess,
       "gtmDnssecStatSigFailed": gtmDnssecStatSigFailed,
       "gtmDnssecStatSigRrsetFailed": gtmDnssecStatSigRrsetFailed,
       "gtmDnssecStatConnectFlowFailed": gtmDnssecStatConnectFlowFailed,
       "gtmDnssecStatTowireFailed": gtmDnssecStatTowireFailed,
       "gtmDnssecStatAxfrQueries": gtmDnssecStatAxfrQueries,
       "gtmDnssecStatIxfrQueries": gtmDnssecStatIxfrQueries,
       "gtmDnssecStatXfrStarts": gtmDnssecStatXfrStarts,
       "gtmDnssecStatXfrCompletes": gtmDnssecStatXfrCompletes,
       "gtmDnssecStatXfrMsgs": gtmDnssecStatXfrMsgs,
       "gtmDnssecStatXfrMasterMsgs": gtmDnssecStatXfrMasterMsgs,
       "gtmDnssecStatXfrResponseAverageSize": gtmDnssecStatXfrResponseAverageSize,
       "gtmDnssecStatXfrSerial": gtmDnssecStatXfrSerial,
       "gtmDnssecStatXfrMasterSerial": gtmDnssecStatXfrMasterSerial,
       "gtmApplications": gtmApplications,
       "gtmApplication": gtmApplication,
       "gtmAppNumber": gtmAppNumber,
       "gtmAppTable": gtmAppTable,
       "gtmAppEntry": gtmAppEntry,
       "gtmAppName": gtmAppName,
       "gtmAppPersist": gtmAppPersist,
       "gtmAppTtlPersist": gtmAppTtlPersist,
       "gtmAppAvailability": gtmAppAvailability,
       "gtmApplicationStatus": gtmApplicationStatus,
       "gtmAppStatusNumber": gtmAppStatusNumber,
       "gtmAppStatusTable": gtmAppStatusTable,
       "gtmAppStatusEntry": gtmAppStatusEntry,
       "gtmAppStatusName": gtmAppStatusName,
       "gtmAppStatusAvailState": gtmAppStatusAvailState,
       "gtmAppStatusEnabledState": gtmAppStatusEnabledState,
       "gtmAppStatusParentType": gtmAppStatusParentType,
       "gtmAppStatusDetailReason": gtmAppStatusDetailReason,
       "gtmAppContextStat": gtmAppContextStat,
       "gtmAppContStatNumber": gtmAppContStatNumber,
       "gtmAppContStatTable": gtmAppContStatTable,
       "gtmAppContStatEntry": gtmAppContStatEntry,
       "gtmAppContStatAppName": gtmAppContStatAppName,
       "gtmAppContStatType": gtmAppContStatType,
       "gtmAppContStatName": gtmAppContStatName,
       "gtmAppContStatNumAvail": gtmAppContStatNumAvail,
       "gtmAppContStatAvailState": gtmAppContStatAvailState,
       "gtmAppContStatEnabledState": gtmAppContStatEnabledState,
       "gtmAppContStatParentType": gtmAppContStatParentType,
       "gtmAppContStatDetailReason": gtmAppContStatDetailReason,
       "gtmAppContextDisable": gtmAppContextDisable,
       "gtmAppContDisNumber": gtmAppContDisNumber,
       "gtmAppContDisTable": gtmAppContDisTable,
       "gtmAppContDisEntry": gtmAppContDisEntry,
       "gtmAppContDisAppName": gtmAppContDisAppName,
       "gtmAppContDisType": gtmAppContDisType,
       "gtmAppContDisName": gtmAppContDisName,
       "gtmDataCenters": gtmDataCenters,
       "gtmDataCenter": gtmDataCenter,
       "gtmDcNumber": gtmDcNumber,
       "gtmDcTable": gtmDcTable,
       "gtmDcEntry": gtmDcEntry,
       "gtmDcName": gtmDcName,
       "gtmDcLocation": gtmDcLocation,
       "gtmDcContact": gtmDcContact,
       "gtmDcEnabled": gtmDcEnabled,
       "gtmDataCenterStat": gtmDataCenterStat,
       "gtmDcStatResetStats": gtmDcStatResetStats,
       "gtmDcStatNumber": gtmDcStatNumber,
       "gtmDcStatTable": gtmDcStatTable,
       "gtmDcStatEntry": gtmDcStatEntry,
       "gtmDcStatName": gtmDcStatName,
       "gtmDcStatCpuUsage": gtmDcStatCpuUsage,
       "gtmDcStatMemAvail": gtmDcStatMemAvail,
       "gtmDcStatBitsPerSecIn": gtmDcStatBitsPerSecIn,
       "gtmDcStatBitsPerSecOut": gtmDcStatBitsPerSecOut,
       "gtmDcStatPktsPerSecIn": gtmDcStatPktsPerSecIn,
       "gtmDcStatPktsPerSecOut": gtmDcStatPktsPerSecOut,
       "gtmDcStatConnections": gtmDcStatConnections,
       "gtmDcStatConnRate": gtmDcStatConnRate,
       "gtmDataCenterStatus": gtmDataCenterStatus,
       "gtmDcStatusNumber": gtmDcStatusNumber,
       "gtmDcStatusTable": gtmDcStatusTable,
       "gtmDcStatusEntry": gtmDcStatusEntry,
       "gtmDcStatusName": gtmDcStatusName,
       "gtmDcStatusAvailState": gtmDcStatusAvailState,
       "gtmDcStatusEnabledState": gtmDcStatusEnabledState,
       "gtmDcStatusParentType": gtmDcStatusParentType,
       "gtmDcStatusDetailReason": gtmDcStatusDetailReason,
       "gtmIps": gtmIps,
       "gtmIp": gtmIp,
       "gtmIpNumber": gtmIpNumber,
       "gtmIpTable": gtmIpTable,
       "gtmIpEntry": gtmIpEntry,
       "gtmIpIpType": gtmIpIpType,
       "gtmIpIp": gtmIpIp,
       "gtmIpLinkName": gtmIpLinkName,
       "gtmIpServerName": gtmIpServerName,
       "gtmIpUnitId": gtmIpUnitId,
       "gtmIpIpXlatedType": gtmIpIpXlatedType,
       "gtmIpIpXlated": gtmIpIpXlated,
       "gtmIpDeviceName": gtmIpDeviceName,
       "gtmLinks": gtmLinks,
       "gtmLink": gtmLink,
       "gtmLinkNumber": gtmLinkNumber,
       "gtmLinkTable": gtmLinkTable,
       "gtmLinkEntry": gtmLinkEntry,
       "gtmLinkName": gtmLinkName,
       "gtmLinkDcName": gtmLinkDcName,
       "gtmLinkIspName": gtmLinkIspName,
       "gtmLinkUplinkAddressType": gtmLinkUplinkAddressType,
       "gtmLinkUplinkAddress": gtmLinkUplinkAddress,
       "gtmLinkLimitInCpuUsageEnabled": gtmLinkLimitInCpuUsageEnabled,
       "gtmLinkLimitInMemAvailEnabled": gtmLinkLimitInMemAvailEnabled,
       "gtmLinkLimitInBitsPerSecEnabled": gtmLinkLimitInBitsPerSecEnabled,
       "gtmLinkLimitInPktsPerSecEnabled": gtmLinkLimitInPktsPerSecEnabled,
       "gtmLinkLimitInConnEnabled": gtmLinkLimitInConnEnabled,
       "gtmLinkLimitInConnPerSecEnabled": gtmLinkLimitInConnPerSecEnabled,
       "gtmLinkLimitInCpuUsage": gtmLinkLimitInCpuUsage,
       "gtmLinkLimitInMemAvail": gtmLinkLimitInMemAvail,
       "gtmLinkLimitInBitsPerSec": gtmLinkLimitInBitsPerSec,
       "gtmLinkLimitInPktsPerSec": gtmLinkLimitInPktsPerSec,
       "gtmLinkLimitInConn": gtmLinkLimitInConn,
       "gtmLinkLimitInConnPerSec": gtmLinkLimitInConnPerSec,
       "gtmLinkLimitOutCpuUsageEnabled": gtmLinkLimitOutCpuUsageEnabled,
       "gtmLinkLimitOutMemAvailEnabled": gtmLinkLimitOutMemAvailEnabled,
       "gtmLinkLimitOutBitsPerSecEnabled": gtmLinkLimitOutBitsPerSecEnabled,
       "gtmLinkLimitOutPktsPerSecEnabled": gtmLinkLimitOutPktsPerSecEnabled,
       "gtmLinkLimitOutConnEnabled": gtmLinkLimitOutConnEnabled,
       "gtmLinkLimitOutConnPerSecEnabled": gtmLinkLimitOutConnPerSecEnabled,
       "gtmLinkLimitOutCpuUsage": gtmLinkLimitOutCpuUsage,
       "gtmLinkLimitOutMemAvail": gtmLinkLimitOutMemAvail,
       "gtmLinkLimitOutBitsPerSec": gtmLinkLimitOutBitsPerSec,
       "gtmLinkLimitOutPktsPerSec": gtmLinkLimitOutPktsPerSec,
       "gtmLinkLimitOutConn": gtmLinkLimitOutConn,
       "gtmLinkLimitOutConnPerSec": gtmLinkLimitOutConnPerSec,
       "gtmLinkLimitTotalCpuUsageEnabled": gtmLinkLimitTotalCpuUsageEnabled,
       "gtmLinkLimitTotalMemAvailEnabled": gtmLinkLimitTotalMemAvailEnabled,
       "gtmLinkLimitTotalBitsPerSecEnabled": gtmLinkLimitTotalBitsPerSecEnabled,
       "gtmLinkLimitTotalPktsPerSecEnabled": gtmLinkLimitTotalPktsPerSecEnabled,
       "gtmLinkLimitTotalConnEnabled": gtmLinkLimitTotalConnEnabled,
       "gtmLinkLimitTotalConnPerSecEnabled": gtmLinkLimitTotalConnPerSecEnabled,
       "gtmLinkLimitTotalCpuUsage": gtmLinkLimitTotalCpuUsage,
       "gtmLinkLimitTotalMemAvail": gtmLinkLimitTotalMemAvail,
       "gtmLinkLimitTotalBitsPerSec": gtmLinkLimitTotalBitsPerSec,
       "gtmLinkLimitTotalPktsPerSec": gtmLinkLimitTotalPktsPerSec,
       "gtmLinkLimitTotalConn": gtmLinkLimitTotalConn,
       "gtmLinkLimitTotalConnPerSec": gtmLinkLimitTotalConnPerSec,
       "gtmLinkMonitorRule": gtmLinkMonitorRule,
       "gtmLinkDuplex": gtmLinkDuplex,
       "gtmLinkEnabled": gtmLinkEnabled,
       "gtmLinkRatio": gtmLinkRatio,
       "gtmLinkPrepaid": gtmLinkPrepaid,
       "gtmLinkPrepaidInDollars": gtmLinkPrepaidInDollars,
       "gtmLinkWeightingType": gtmLinkWeightingType,
       "gtmLinkCost": gtmLinkCost,
       "gtmLinkCostNumber": gtmLinkCostNumber,
       "gtmLinkCostTable": gtmLinkCostTable,
       "gtmLinkCostEntry": gtmLinkCostEntry,
       "gtmLinkCostName": gtmLinkCostName,
       "gtmLinkCostIndex": gtmLinkCostIndex,
       "gtmLinkCostUptoBps": gtmLinkCostUptoBps,
       "gtmLinkCostDollarsPerMbps": gtmLinkCostDollarsPerMbps,
       "gtmLinkStat": gtmLinkStat,
       "gtmLinkStatResetStats": gtmLinkStatResetStats,
       "gtmLinkStatNumber": gtmLinkStatNumber,
       "gtmLinkStatTable": gtmLinkStatTable,
       "gtmLinkStatEntry": gtmLinkStatEntry,
       "gtmLinkStatName": gtmLinkStatName,
       "gtmLinkStatRate": gtmLinkStatRate,
       "gtmLinkStatRateIn": gtmLinkStatRateIn,
       "gtmLinkStatRateOut": gtmLinkStatRateOut,
       "gtmLinkStatRateNode": gtmLinkStatRateNode,
       "gtmLinkStatRateNodeIn": gtmLinkStatRateNodeIn,
       "gtmLinkStatRateNodeOut": gtmLinkStatRateNodeOut,
       "gtmLinkStatRateVses": gtmLinkStatRateVses,
       "gtmLinkStatRateVsesIn": gtmLinkStatRateVsesIn,
       "gtmLinkStatRateVsesOut": gtmLinkStatRateVsesOut,
       "gtmLinkStatLcsIn": gtmLinkStatLcsIn,
       "gtmLinkStatLcsOut": gtmLinkStatLcsOut,
       "gtmLinkStatPaths": gtmLinkStatPaths,
       "gtmLinkStatus": gtmLinkStatus,
       "gtmLinkStatusNumber": gtmLinkStatusNumber,
       "gtmLinkStatusTable": gtmLinkStatusTable,
       "gtmLinkStatusEntry": gtmLinkStatusEntry,
       "gtmLinkStatusName": gtmLinkStatusName,
       "gtmLinkStatusAvailState": gtmLinkStatusAvailState,
       "gtmLinkStatusEnabledState": gtmLinkStatusEnabledState,
       "gtmLinkStatusParentType": gtmLinkStatusParentType,
       "gtmLinkStatusDetailReason": gtmLinkStatusDetailReason,
       "gtmPools": gtmPools,
       "gtmPool": gtmPool,
       "gtmPoolNumber": gtmPoolNumber,
       "gtmPoolTable": gtmPoolTable,
       "gtmPoolEntry": gtmPoolEntry,
       "gtmPoolName": gtmPoolName,
       "gtmPoolTtl": gtmPoolTtl,
       "gtmPoolEnabled": gtmPoolEnabled,
       "gtmPoolVerifyMember": gtmPoolVerifyMember,
       "gtmPoolDynamicRatio": gtmPoolDynamicRatio,
       "gtmPoolAnswersToReturn": gtmPoolAnswersToReturn,
       "gtmPoolLbMode": gtmPoolLbMode,
       "gtmPoolAlternate": gtmPoolAlternate,
       "gtmPoolFallback": gtmPoolFallback,
       "gtmPoolManualResume": gtmPoolManualResume,
       "gtmPoolQosCoeffRtt": gtmPoolQosCoeffRtt,
       "gtmPoolQosCoeffHops": gtmPoolQosCoeffHops,
       "gtmPoolQosCoeffTopology": gtmPoolQosCoeffTopology,
       "gtmPoolQosCoeffHitRatio": gtmPoolQosCoeffHitRatio,
       "gtmPoolQosCoeffPacketRate": gtmPoolQosCoeffPacketRate,
       "gtmPoolQosCoeffVsCapacity": gtmPoolQosCoeffVsCapacity,
       "gtmPoolQosCoeffBps": gtmPoolQosCoeffBps,
       "gtmPoolQosCoeffLcs": gtmPoolQosCoeffLcs,
       "gtmPoolQosCoeffConnRate": gtmPoolQosCoeffConnRate,
       "gtmPoolFallbackIpType": gtmPoolFallbackIpType,
       "gtmPoolFallbackIp": gtmPoolFallbackIp,
       "gtmPoolCname": gtmPoolCname,
       "gtmPoolLimitCpuUsageEnabled": gtmPoolLimitCpuUsageEnabled,
       "gtmPoolLimitMemAvailEnabled": gtmPoolLimitMemAvailEnabled,
       "gtmPoolLimitBitsPerSecEnabled": gtmPoolLimitBitsPerSecEnabled,
       "gtmPoolLimitPktsPerSecEnabled": gtmPoolLimitPktsPerSecEnabled,
       "gtmPoolLimitConnEnabled": gtmPoolLimitConnEnabled,
       "gtmPoolLimitConnPerSecEnabled": gtmPoolLimitConnPerSecEnabled,
       "gtmPoolLimitCpuUsage": gtmPoolLimitCpuUsage,
       "gtmPoolLimitMemAvail": gtmPoolLimitMemAvail,
       "gtmPoolLimitBitsPerSec": gtmPoolLimitBitsPerSec,
       "gtmPoolLimitPktsPerSec": gtmPoolLimitPktsPerSec,
       "gtmPoolLimitConn": gtmPoolLimitConn,
       "gtmPoolLimitConnPerSec": gtmPoolLimitConnPerSec,
       "gtmPoolMonitorRule": gtmPoolMonitorRule,
       "gtmPoolQosCoeffVsScore": gtmPoolQosCoeffVsScore,
       "gtmPoolFallbackIpv6Type": gtmPoolFallbackIpv6Type,
       "gtmPoolFallbackIpv6": gtmPoolFallbackIpv6,
       "gtmPoolStat": gtmPoolStat,
       "gtmPoolStatResetStats": gtmPoolStatResetStats,
       "gtmPoolStatNumber": gtmPoolStatNumber,
       "gtmPoolStatTable": gtmPoolStatTable,
       "gtmPoolStatEntry": gtmPoolStatEntry,
       "gtmPoolStatName": gtmPoolStatName,
       "gtmPoolStatPreferred": gtmPoolStatPreferred,
       "gtmPoolStatAlternate": gtmPoolStatAlternate,
       "gtmPoolStatFallback": gtmPoolStatFallback,
       "gtmPoolStatDropped": gtmPoolStatDropped,
       "gtmPoolStatExplicitIp": gtmPoolStatExplicitIp,
       "gtmPoolStatReturnToDns": gtmPoolStatReturnToDns,
       "gtmPoolStatReturnFromDns": gtmPoolStatReturnFromDns,
       "gtmPoolStatCnameResolutions": gtmPoolStatCnameResolutions,
       "gtmPoolStatus": gtmPoolStatus,
       "gtmPoolStatusNumber": gtmPoolStatusNumber,
       "gtmPoolStatusTable": gtmPoolStatusTable,
       "gtmPoolStatusEntry": gtmPoolStatusEntry,
       "gtmPoolStatusName": gtmPoolStatusName,
       "gtmPoolStatusAvailState": gtmPoolStatusAvailState,
       "gtmPoolStatusEnabledState": gtmPoolStatusEnabledState,
       "gtmPoolStatusParentType": gtmPoolStatusParentType,
       "gtmPoolStatusDetailReason": gtmPoolStatusDetailReason,
       "gtmPoolMember": gtmPoolMember,
       "gtmPoolMbrNumber": gtmPoolMbrNumber,
       "gtmPoolMbrTable": gtmPoolMbrTable,
       "gtmPoolMbrEntry": gtmPoolMbrEntry,
       "gtmPoolMbrPoolName": gtmPoolMbrPoolName,
       "gtmPoolMbrIpType": gtmPoolMbrIpType,
       "gtmPoolMbrIp": gtmPoolMbrIp,
       "gtmPoolMbrPort": gtmPoolMbrPort,
       "gtmPoolMbrVsName": gtmPoolMbrVsName,
       "gtmPoolMbrOrder": gtmPoolMbrOrder,
       "gtmPoolMbrLimitCpuUsageEnabled": gtmPoolMbrLimitCpuUsageEnabled,
       "gtmPoolMbrLimitMemAvailEnabled": gtmPoolMbrLimitMemAvailEnabled,
       "gtmPoolMbrLimitBitsPerSecEnabled": gtmPoolMbrLimitBitsPerSecEnabled,
       "gtmPoolMbrLimitPktsPerSecEnabled": gtmPoolMbrLimitPktsPerSecEnabled,
       "gtmPoolMbrLimitConnEnabled": gtmPoolMbrLimitConnEnabled,
       "gtmPoolMbrLimitConnPerSecEnabled": gtmPoolMbrLimitConnPerSecEnabled,
       "gtmPoolMbrLimitCpuUsage": gtmPoolMbrLimitCpuUsage,
       "gtmPoolMbrLimitMemAvail": gtmPoolMbrLimitMemAvail,
       "gtmPoolMbrLimitBitsPerSec": gtmPoolMbrLimitBitsPerSec,
       "gtmPoolMbrLimitPktsPerSec": gtmPoolMbrLimitPktsPerSec,
       "gtmPoolMbrLimitConn": gtmPoolMbrLimitConn,
       "gtmPoolMbrLimitConnPerSec": gtmPoolMbrLimitConnPerSec,
       "gtmPoolMbrMonitorRule": gtmPoolMbrMonitorRule,
       "gtmPoolMbrEnabled": gtmPoolMbrEnabled,
       "gtmPoolMbrRatio": gtmPoolMbrRatio,
       "gtmPoolMbrServerName": gtmPoolMbrServerName,
       "gtmPoolMemberDepends": gtmPoolMemberDepends,
       "gtmPoolMbrDepsNumber": gtmPoolMbrDepsNumber,
       "gtmPoolMbrDepsTable": gtmPoolMbrDepsTable,
       "gtmPoolMbrDepsEntry": gtmPoolMbrDepsEntry,
       "gtmPoolMbrDepsIpType": gtmPoolMbrDepsIpType,
       "gtmPoolMbrDepsIp": gtmPoolMbrDepsIp,
       "gtmPoolMbrDepsPort": gtmPoolMbrDepsPort,
       "gtmPoolMbrDepsPoolName": gtmPoolMbrDepsPoolName,
       "gtmPoolMbrDepsVipType": gtmPoolMbrDepsVipType,
       "gtmPoolMbrDepsVip": gtmPoolMbrDepsVip,
       "gtmPoolMbrDepsVport": gtmPoolMbrDepsVport,
       "gtmPoolMbrDepsServerName": gtmPoolMbrDepsServerName,
       "gtmPoolMbrDepsVsName": gtmPoolMbrDepsVsName,
       "gtmPoolMbrDepsDependServerName": gtmPoolMbrDepsDependServerName,
       "gtmPoolMbrDepsDependVsName": gtmPoolMbrDepsDependVsName,
       "gtmPoolMemberStat": gtmPoolMemberStat,
       "gtmPoolMbrStatResetStats": gtmPoolMbrStatResetStats,
       "gtmPoolMbrStatNumber": gtmPoolMbrStatNumber,
       "gtmPoolMbrStatTable": gtmPoolMbrStatTable,
       "gtmPoolMbrStatEntry": gtmPoolMbrStatEntry,
       "gtmPoolMbrStatPoolName": gtmPoolMbrStatPoolName,
       "gtmPoolMbrStatIpType": gtmPoolMbrStatIpType,
       "gtmPoolMbrStatIp": gtmPoolMbrStatIp,
       "gtmPoolMbrStatPort": gtmPoolMbrStatPort,
       "gtmPoolMbrStatPreferred": gtmPoolMbrStatPreferred,
       "gtmPoolMbrStatAlternate": gtmPoolMbrStatAlternate,
       "gtmPoolMbrStatFallback": gtmPoolMbrStatFallback,
       "gtmPoolMbrStatServerName": gtmPoolMbrStatServerName,
       "gtmPoolMbrStatVsName": gtmPoolMbrStatVsName,
       "gtmPoolMemberStatus": gtmPoolMemberStatus,
       "gtmPoolMbrStatusNumber": gtmPoolMbrStatusNumber,
       "gtmPoolMbrStatusTable": gtmPoolMbrStatusTable,
       "gtmPoolMbrStatusEntry": gtmPoolMbrStatusEntry,
       "gtmPoolMbrStatusPoolName": gtmPoolMbrStatusPoolName,
       "gtmPoolMbrStatusIpType": gtmPoolMbrStatusIpType,
       "gtmPoolMbrStatusIp": gtmPoolMbrStatusIp,
       "gtmPoolMbrStatusPort": gtmPoolMbrStatusPort,
       "gtmPoolMbrStatusAvailState": gtmPoolMbrStatusAvailState,
       "gtmPoolMbrStatusEnabledState": gtmPoolMbrStatusEnabledState,
       "gtmPoolMbrStatusParentType": gtmPoolMbrStatusParentType,
       "gtmPoolMbrStatusDetailReason": gtmPoolMbrStatusDetailReason,
       "gtmPoolMbrStatusVsName": gtmPoolMbrStatusVsName,
       "gtmPoolMbrStatusServerName": gtmPoolMbrStatusServerName,
       "gtmRegions": gtmRegions,
       "gtmRegionEntry": gtmRegionEntry,
       "gtmRegionEntryNumber": gtmRegionEntryNumber,
       "gtmRegionEntryTable": gtmRegionEntryTable,
       "gtmRegionEntryEntry": gtmRegionEntryEntry,
       "gtmRegionEntryName": gtmRegionEntryName,
       "gtmRegionEntryRegionDbType": gtmRegionEntryRegionDbType,
       "gtmRegItem": gtmRegItem,
       "gtmRegItemNumber": gtmRegItemNumber,
       "gtmRegItemTable": gtmRegItemTable,
       "gtmRegItemEntry": gtmRegItemEntry,
       "gtmRegItemRegionDbType": gtmRegItemRegionDbType,
       "gtmRegItemRegionName": gtmRegItemRegionName,
       "gtmRegItemType": gtmRegItemType,
       "gtmRegItemNegate": gtmRegItemNegate,
       "gtmRegItemRegEntry": gtmRegItemRegEntry,
       "gtmRules": gtmRules,
       "gtmRule": gtmRule,
       "gtmRuleNumber": gtmRuleNumber,
       "gtmRuleTable": gtmRuleTable,
       "gtmRuleEntry": gtmRuleEntry,
       "gtmRuleName": gtmRuleName,
       "gtmRuleDefinition": gtmRuleDefinition,
       "gtmRuleConfigSource": gtmRuleConfigSource,
       "gtmRuleEvent": gtmRuleEvent,
       "gtmRuleEventNumber": gtmRuleEventNumber,
       "gtmRuleEventTable": gtmRuleEventTable,
       "gtmRuleEventEntry": gtmRuleEventEntry,
       "gtmRuleEventName": gtmRuleEventName,
       "gtmRuleEventEventType": gtmRuleEventEventType,
       "gtmRuleEventPriority": gtmRuleEventPriority,
       "gtmRuleEventScript": gtmRuleEventScript,
       "gtmRuleEventStat": gtmRuleEventStat,
       "gtmRuleEventStatResetStats": gtmRuleEventStatResetStats,
       "gtmRuleEventStatNumber": gtmRuleEventStatNumber,
       "gtmRuleEventStatTable": gtmRuleEventStatTable,
       "gtmRuleEventStatEntry": gtmRuleEventStatEntry,
       "gtmRuleEventStatName": gtmRuleEventStatName,
       "gtmRuleEventStatEventType": gtmRuleEventStatEventType,
       "gtmRuleEventStatPriority": gtmRuleEventStatPriority,
       "gtmRuleEventStatFailures": gtmRuleEventStatFailures,
       "gtmRuleEventStatAborts": gtmRuleEventStatAborts,
       "gtmRuleEventStatTotalExecutions": gtmRuleEventStatTotalExecutions,
       "gtmServers": gtmServers,
       "gtmServer": gtmServer,
       "gtmServerNumber": gtmServerNumber,
       "gtmServerTable": gtmServerTable,
       "gtmServerEntry": gtmServerEntry,
       "gtmServerName": gtmServerName,
       "gtmServerDcName": gtmServerDcName,
       "gtmServerType": gtmServerType,
       "gtmServerEnabled": gtmServerEnabled,
       "gtmServerLimitCpuUsageEnabled": gtmServerLimitCpuUsageEnabled,
       "gtmServerLimitMemAvailEnabled": gtmServerLimitMemAvailEnabled,
       "gtmServerLimitBitsPerSecEnabled": gtmServerLimitBitsPerSecEnabled,
       "gtmServerLimitPktsPerSecEnabled": gtmServerLimitPktsPerSecEnabled,
       "gtmServerLimitConnEnabled": gtmServerLimitConnEnabled,
       "gtmServerLimitConnPerSecEnabled": gtmServerLimitConnPerSecEnabled,
       "gtmServerLimitCpuUsage": gtmServerLimitCpuUsage,
       "gtmServerLimitMemAvail": gtmServerLimitMemAvail,
       "gtmServerLimitBitsPerSec": gtmServerLimitBitsPerSec,
       "gtmServerLimitPktsPerSec": gtmServerLimitPktsPerSec,
       "gtmServerLimitConn": gtmServerLimitConn,
       "gtmServerLimitConnPerSec": gtmServerLimitConnPerSec,
       "gtmServerProberType": gtmServerProberType,
       "gtmServerProber": gtmServerProber,
       "gtmServerMonitorRule": gtmServerMonitorRule,
       "gtmServerAllowSvcChk": gtmServerAllowSvcChk,
       "gtmServerAllowPath": gtmServerAllowPath,
       "gtmServerAllowSnmp": gtmServerAllowSnmp,
       "gtmServerAutoconfState": gtmServerAutoconfState,
       "gtmServerLinkAutoconfState": gtmServerLinkAutoconfState,
       "gtmServerStat": gtmServerStat,
       "gtmServerStatResetStats": gtmServerStatResetStats,
       "gtmServerStatNumber": gtmServerStatNumber,
       "gtmServerStatTable": gtmServerStatTable,
       "gtmServerStatEntry": gtmServerStatEntry,
       "gtmServerStatName": gtmServerStatName,
       "gtmServerStatUnitId": gtmServerStatUnitId,
       "gtmServerStatVsPicks": gtmServerStatVsPicks,
       "gtmServerStatCpuUsage": gtmServerStatCpuUsage,
       "gtmServerStatMemAvail": gtmServerStatMemAvail,
       "gtmServerStatBitsPerSecIn": gtmServerStatBitsPerSecIn,
       "gtmServerStatBitsPerSecOut": gtmServerStatBitsPerSecOut,
       "gtmServerStatPktsPerSecIn": gtmServerStatPktsPerSecIn,
       "gtmServerStatPktsPerSecOut": gtmServerStatPktsPerSecOut,
       "gtmServerStatConnections": gtmServerStatConnections,
       "gtmServerStatConnRate": gtmServerStatConnRate,
       "gtmServerStatus": gtmServerStatus,
       "gtmServerStatusNumber": gtmServerStatusNumber,
       "gtmServerStatusTable": gtmServerStatusTable,
       "gtmServerStatusEntry": gtmServerStatusEntry,
       "gtmServerStatusName": gtmServerStatusName,
       "gtmServerStatusAvailState": gtmServerStatusAvailState,
       "gtmServerStatusEnabledState": gtmServerStatusEnabledState,
       "gtmServerStatusParentType": gtmServerStatusParentType,
       "gtmServerStatusDetailReason": gtmServerStatusDetailReason,
       "gtmServerStat2": gtmServerStat2,
       "gtmServerStat2ResetStats": gtmServerStat2ResetStats,
       "gtmServerStat2Number": gtmServerStat2Number,
       "gtmServerStat2Table": gtmServerStat2Table,
       "gtmServerStat2Entry": gtmServerStat2Entry,
       "gtmServerStat2Name": gtmServerStat2Name,
       "gtmServerStat2UnitId": gtmServerStat2UnitId,
       "gtmServerStat2VsPicks": gtmServerStat2VsPicks,
       "gtmServerStat2CpuUsage": gtmServerStat2CpuUsage,
       "gtmServerStat2MemAvail": gtmServerStat2MemAvail,
       "gtmServerStat2BitsPerSecIn": gtmServerStat2BitsPerSecIn,
       "gtmServerStat2BitsPerSecOut": gtmServerStat2BitsPerSecOut,
       "gtmServerStat2PktsPerSecIn": gtmServerStat2PktsPerSecIn,
       "gtmServerStat2PktsPerSecOut": gtmServerStat2PktsPerSecOut,
       "gtmServerStat2Connections": gtmServerStat2Connections,
       "gtmServerStat2ConnRate": gtmServerStat2ConnRate,
       "gtmTopologies": gtmTopologies,
       "gtmTopItem": gtmTopItem,
       "gtmTopItemNumber": gtmTopItemNumber,
       "gtmTopItemTable": gtmTopItemTable,
       "gtmTopItemEntry": gtmTopItemEntry,
       "gtmTopItemLdnsType": gtmTopItemLdnsType,
       "gtmTopItemLdnsNegate": gtmTopItemLdnsNegate,
       "gtmTopItemLdnsEntry": gtmTopItemLdnsEntry,
       "gtmTopItemServerType": gtmTopItemServerType,
       "gtmTopItemServerNegate": gtmTopItemServerNegate,
       "gtmTopItemServerEntry": gtmTopItemServerEntry,
       "gtmTopItemWeight": gtmTopItemWeight,
       "gtmTopItemOrder": gtmTopItemOrder,
       "gtmVirtualServers": gtmVirtualServers,
       "gtmVirtualServ": gtmVirtualServ,
       "gtmVsNumber": gtmVsNumber,
       "gtmVsTable": gtmVsTable,
       "gtmVsEntry": gtmVsEntry,
       "gtmVsIpType": gtmVsIpType,
       "gtmVsIp": gtmVsIp,
       "gtmVsPort": gtmVsPort,
       "gtmVsName": gtmVsName,
       "gtmVsServerName": gtmVsServerName,
       "gtmVsIpXlatedType": gtmVsIpXlatedType,
       "gtmVsIpXlated": gtmVsIpXlated,
       "gtmVsPortXlated": gtmVsPortXlated,
       "gtmVsLimitCpuUsageEnabled": gtmVsLimitCpuUsageEnabled,
       "gtmVsLimitMemAvailEnabled": gtmVsLimitMemAvailEnabled,
       "gtmVsLimitBitsPerSecEnabled": gtmVsLimitBitsPerSecEnabled,
       "gtmVsLimitPktsPerSecEnabled": gtmVsLimitPktsPerSecEnabled,
       "gtmVsLimitConnEnabled": gtmVsLimitConnEnabled,
       "gtmVsLimitConnPerSecEnabled": gtmVsLimitConnPerSecEnabled,
       "gtmVsLimitCpuUsage": gtmVsLimitCpuUsage,
       "gtmVsLimitMemAvail": gtmVsLimitMemAvail,
       "gtmVsLimitBitsPerSec": gtmVsLimitBitsPerSec,
       "gtmVsLimitPktsPerSec": gtmVsLimitPktsPerSec,
       "gtmVsLimitConn": gtmVsLimitConn,
       "gtmVsLimitConnPerSec": gtmVsLimitConnPerSec,
       "gtmVsMonitorRule": gtmVsMonitorRule,
       "gtmVsEnabled": gtmVsEnabled,
       "gtmVsLinkName": gtmVsLinkName,
       "gtmVirtualServDepends": gtmVirtualServDepends,
       "gtmVsDepsNumber": gtmVsDepsNumber,
       "gtmVsDepsTable": gtmVsDepsTable,
       "gtmVsDepsEntry": gtmVsDepsEntry,
       "gtmVsDepsIpType": gtmVsDepsIpType,
       "gtmVsDepsIp": gtmVsDepsIp,
       "gtmVsDepsPort": gtmVsDepsPort,
       "gtmVsDepsVipType": gtmVsDepsVipType,
       "gtmVsDepsVip": gtmVsDepsVip,
       "gtmVsDepsVport": gtmVsDepsVport,
       "gtmVsDepsServerName": gtmVsDepsServerName,
       "gtmVsDepsVsName": gtmVsDepsVsName,
       "gtmVsDepsDependServerName": gtmVsDepsDependServerName,
       "gtmVsDepsDependVsName": gtmVsDepsDependVsName,
       "gtmVirtualServStat": gtmVirtualServStat,
       "gtmVsStatResetStats": gtmVsStatResetStats,
       "gtmVsStatNumber": gtmVsStatNumber,
       "gtmVsStatTable": gtmVsStatTable,
       "gtmVsStatEntry": gtmVsStatEntry,
       "gtmVsStatIpType": gtmVsStatIpType,
       "gtmVsStatIp": gtmVsStatIp,
       "gtmVsStatPort": gtmVsStatPort,
       "gtmVsStatName": gtmVsStatName,
       "gtmVsStatCpuUsage": gtmVsStatCpuUsage,
       "gtmVsStatMemAvail": gtmVsStatMemAvail,
       "gtmVsStatBitsPerSecIn": gtmVsStatBitsPerSecIn,
       "gtmVsStatBitsPerSecOut": gtmVsStatBitsPerSecOut,
       "gtmVsStatPktsPerSecIn": gtmVsStatPktsPerSecIn,
       "gtmVsStatPktsPerSecOut": gtmVsStatPktsPerSecOut,
       "gtmVsStatConnections": gtmVsStatConnections,
       "gtmVsStatConnRate": gtmVsStatConnRate,
       "gtmVsStatVsScore": gtmVsStatVsScore,
       "gtmVsStatServerName": gtmVsStatServerName,
       "gtmVirtualServStatus": gtmVirtualServStatus,
       "gtmVsStatusNumber": gtmVsStatusNumber,
       "gtmVsStatusTable": gtmVsStatusTable,
       "gtmVsStatusEntry": gtmVsStatusEntry,
       "gtmVsStatusIpType": gtmVsStatusIpType,
       "gtmVsStatusIp": gtmVsStatusIp,
       "gtmVsStatusPort": gtmVsStatusPort,
       "gtmVsStatusAvailState": gtmVsStatusAvailState,
       "gtmVsStatusEnabledState": gtmVsStatusEnabledState,
       "gtmVsStatusParentType": gtmVsStatusParentType,
       "gtmVsStatusDetailReason": gtmVsStatusDetailReason,
       "gtmVsStatusVsName": gtmVsStatusVsName,
       "gtmVsStatusServerName": gtmVsStatusServerName,
       "gtmWideips": gtmWideips,
       "gtmWideip": gtmWideip,
       "gtmWideipNumber": gtmWideipNumber,
       "gtmWideipTable": gtmWideipTable,
       "gtmWideipEntry": gtmWideipEntry,
       "gtmWideipName": gtmWideipName,
       "gtmWideipPersist": gtmWideipPersist,
       "gtmWideipTtlPersist": gtmWideipTtlPersist,
       "gtmWideipEnabled": gtmWideipEnabled,
       "gtmWideipLbmodePool": gtmWideipLbmodePool,
       "gtmWideipApplication": gtmWideipApplication,
       "gtmWideipLastResortPool": gtmWideipLastResortPool,
       "gtmWideipIpv6Noerror": gtmWideipIpv6Noerror,
       "gtmWideipLoadBalancingDecisionLogVerbosity": gtmWideipLoadBalancingDecisionLogVerbosity,
       "gtmWideipStat": gtmWideipStat,
       "gtmWideipStatResetStats": gtmWideipStatResetStats,
       "gtmWideipStatNumber": gtmWideipStatNumber,
       "gtmWideipStatTable": gtmWideipStatTable,
       "gtmWideipStatEntry": gtmWideipStatEntry,
       "gtmWideipStatName": gtmWideipStatName,
       "gtmWideipStatRequests": gtmWideipStatRequests,
       "gtmWideipStatResolutions": gtmWideipStatResolutions,
       "gtmWideipStatPersisted": gtmWideipStatPersisted,
       "gtmWideipStatPreferred": gtmWideipStatPreferred,
       "gtmWideipStatFallback": gtmWideipStatFallback,
       "gtmWideipStatDropped": gtmWideipStatDropped,
       "gtmWideipStatExplicitIp": gtmWideipStatExplicitIp,
       "gtmWideipStatReturnToDns": gtmWideipStatReturnToDns,
       "gtmWideipStatReturnFromDns": gtmWideipStatReturnFromDns,
       "gtmWideipStatCnameResolutions": gtmWideipStatCnameResolutions,
       "gtmWideipStatARequests": gtmWideipStatARequests,
       "gtmWideipStatAaaaRequests": gtmWideipStatAaaaRequests,
       "gtmWideipStatus": gtmWideipStatus,
       "gtmWideipStatusNumber": gtmWideipStatusNumber,
       "gtmWideipStatusTable": gtmWideipStatusTable,
       "gtmWideipStatusEntry": gtmWideipStatusEntry,
       "gtmWideipStatusName": gtmWideipStatusName,
       "gtmWideipStatusAvailState": gtmWideipStatusAvailState,
       "gtmWideipStatusEnabledState": gtmWideipStatusEnabledState,
       "gtmWideipStatusParentType": gtmWideipStatusParentType,
       "gtmWideipStatusDetailReason": gtmWideipStatusDetailReason,
       "gtmWideipAlias": gtmWideipAlias,
       "gtmWideipAliasNumber": gtmWideipAliasNumber,
       "gtmWideipAliasTable": gtmWideipAliasTable,
       "gtmWideipAliasEntry": gtmWideipAliasEntry,
       "gtmWideipAliasWipName": gtmWideipAliasWipName,
       "gtmWideipAliasName": gtmWideipAliasName,
       "gtmWideipPool": gtmWideipPool,
       "gtmWideipPoolNumber": gtmWideipPoolNumber,
       "gtmWideipPoolTable": gtmWideipPoolTable,
       "gtmWideipPoolEntry": gtmWideipPoolEntry,
       "gtmWideipPoolWipName": gtmWideipPoolWipName,
       "gtmWideipPoolPoolName": gtmWideipPoolPoolName,
       "gtmWideipPoolOrder": gtmWideipPoolOrder,
       "gtmWideipPoolRatio": gtmWideipPoolRatio,
       "gtmWideipRule": gtmWideipRule,
       "gtmWideipRuleNumber": gtmWideipRuleNumber,
       "gtmWideipRuleTable": gtmWideipRuleTable,
       "gtmWideipRuleEntry": gtmWideipRuleEntry,
       "gtmWideipRuleWipName": gtmWideipRuleWipName,
       "gtmWideipRuleRuleName": gtmWideipRuleRuleName,
       "gtmWideipRulePriority": gtmWideipRulePriority,
       "gtmProberPools": gtmProberPools,
       "gtmProberPool": gtmProberPool,
       "gtmProberPoolNumber": gtmProberPoolNumber,
       "gtmProberPoolTable": gtmProberPoolTable,
       "gtmProberPoolEntry": gtmProberPoolEntry,
       "gtmProberPoolName": gtmProberPoolName,
       "gtmProberPoolLbMode": gtmProberPoolLbMode,
       "gtmProberPoolEnabled": gtmProberPoolEnabled,
       "gtmProberPoolStat": gtmProberPoolStat,
       "gtmProberPoolStatResetStats": gtmProberPoolStatResetStats,
       "gtmProberPoolStatNumber": gtmProberPoolStatNumber,
       "gtmProberPoolStatTable": gtmProberPoolStatTable,
       "gtmProberPoolStatEntry": gtmProberPoolStatEntry,
       "gtmProberPoolStatName": gtmProberPoolStatName,
       "gtmProberPoolStatTotalProbes": gtmProberPoolStatTotalProbes,
       "gtmProberPoolStatSuccessfulProbes": gtmProberPoolStatSuccessfulProbes,
       "gtmProberPoolStatFailedProbes": gtmProberPoolStatFailedProbes,
       "gtmProberPoolStatus": gtmProberPoolStatus,
       "gtmProberPoolStatusNumber": gtmProberPoolStatusNumber,
       "gtmProberPoolStatusTable": gtmProberPoolStatusTable,
       "gtmProberPoolStatusEntry": gtmProberPoolStatusEntry,
       "gtmProberPoolStatusName": gtmProberPoolStatusName,
       "gtmProberPoolStatusAvailState": gtmProberPoolStatusAvailState,
       "gtmProberPoolStatusEnabledState": gtmProberPoolStatusEnabledState,
       "gtmProberPoolStatusDetailReason": gtmProberPoolStatusDetailReason,
       "gtmProberPoolMember": gtmProberPoolMember,
       "gtmProberPoolMbrNumber": gtmProberPoolMbrNumber,
       "gtmProberPoolMbrTable": gtmProberPoolMbrTable,
       "gtmProberPoolMbrEntry": gtmProberPoolMbrEntry,
       "gtmProberPoolMbrPoolName": gtmProberPoolMbrPoolName,
       "gtmProberPoolMbrServerName": gtmProberPoolMbrServerName,
       "gtmProberPoolMbrPmbrOrder": gtmProberPoolMbrPmbrOrder,
       "gtmProberPoolMbrEnabled": gtmProberPoolMbrEnabled,
       "gtmProberPoolMemberStat": gtmProberPoolMemberStat,
       "gtmProberPoolMbrStatResetStats": gtmProberPoolMbrStatResetStats,
       "gtmProberPoolMbrStatNumber": gtmProberPoolMbrStatNumber,
       "gtmProberPoolMbrStatTable": gtmProberPoolMbrStatTable,
       "gtmProberPoolMbrStatEntry": gtmProberPoolMbrStatEntry,
       "gtmProberPoolMbrStatPoolName": gtmProberPoolMbrStatPoolName,
       "gtmProberPoolMbrStatServerName": gtmProberPoolMbrStatServerName,
       "gtmProberPoolMbrStatTotalProbes": gtmProberPoolMbrStatTotalProbes,
       "gtmProberPoolMbrStatSuccessfulProbes": gtmProberPoolMbrStatSuccessfulProbes,
       "gtmProberPoolMbrStatFailedProbes": gtmProberPoolMbrStatFailedProbes,
       "gtmProberPoolMemberStatus": gtmProberPoolMemberStatus,
       "gtmProberPoolMbrStatusNumber": gtmProberPoolMbrStatusNumber,
       "gtmProberPoolMbrStatusTable": gtmProberPoolMbrStatusTable,
       "gtmProberPoolMbrStatusEntry": gtmProberPoolMbrStatusEntry,
       "gtmProberPoolMbrStatusPoolName": gtmProberPoolMbrStatusPoolName,
       "gtmProberPoolMbrStatusServerName": gtmProberPoolMbrStatusServerName,
       "gtmProberPoolMbrStatusAvailState": gtmProberPoolMbrStatusAvailState,
       "gtmProberPoolMbrStatusEnabledState": gtmProberPoolMbrStatusEnabledState,
       "gtmProberPoolMbrStatusDetailReason": gtmProberPoolMbrStatusDetailReason,
       "gtmDNSSEC": gtmDNSSEC,
       "gtmDnssecZoneStat": gtmDnssecZoneStat,
       "gtmDnssecZoneStatResetStats": gtmDnssecZoneStatResetStats,
       "gtmDnssecZoneStatNumber": gtmDnssecZoneStatNumber,
       "gtmDnssecZoneStatTable": gtmDnssecZoneStatTable,
       "gtmDnssecZoneStatEntry": gtmDnssecZoneStatEntry,
       "gtmDnssecZoneStatName": gtmDnssecZoneStatName,
       "gtmDnssecZoneStatNsec3s": gtmDnssecZoneStatNsec3s,
       "gtmDnssecZoneStatNsec3Nodata": gtmDnssecZoneStatNsec3Nodata,
       "gtmDnssecZoneStatNsec3Nxdomain": gtmDnssecZoneStatNsec3Nxdomain,
       "gtmDnssecZoneStatNsec3Referral": gtmDnssecZoneStatNsec3Referral,
       "gtmDnssecZoneStatNsec3Resalt": gtmDnssecZoneStatNsec3Resalt,
       "gtmDnssecZoneStatDnssecResponses": gtmDnssecZoneStatDnssecResponses,
       "gtmDnssecZoneStatDnssecDnskeyQueries": gtmDnssecZoneStatDnssecDnskeyQueries,
       "gtmDnssecZoneStatDnssecNsec3paramQueries": gtmDnssecZoneStatDnssecNsec3paramQueries,
       "gtmDnssecZoneStatDnssecDsQueries": gtmDnssecZoneStatDnssecDsQueries,
       "gtmDnssecZoneStatSigCryptoFailed": gtmDnssecZoneStatSigCryptoFailed,
       "gtmDnssecZoneStatSigSuccess": gtmDnssecZoneStatSigSuccess,
       "gtmDnssecZoneStatSigFailed": gtmDnssecZoneStatSigFailed,
       "gtmDnssecZoneStatSigRrsetFailed": gtmDnssecZoneStatSigRrsetFailed,
       "gtmDnssecZoneStatConnectFlowFailed": gtmDnssecZoneStatConnectFlowFailed,
       "gtmDnssecZoneStatTowireFailed": gtmDnssecZoneStatTowireFailed,
       "gtmDnssecZoneStatAxfrQueries": gtmDnssecZoneStatAxfrQueries,
       "gtmDnssecZoneStatIxfrQueries": gtmDnssecZoneStatIxfrQueries,
       "gtmDnssecZoneStatXfrStarts": gtmDnssecZoneStatXfrStarts,
       "gtmDnssecZoneStatXfrCompletes": gtmDnssecZoneStatXfrCompletes,
       "gtmDnssecZoneStatXfrMsgs": gtmDnssecZoneStatXfrMsgs,
       "gtmDnssecZoneStatXfrMasterMsgs": gtmDnssecZoneStatXfrMasterMsgs,
       "gtmDnssecZoneStatXfrResponseAverageSize": gtmDnssecZoneStatXfrResponseAverageSize,
       "gtmDnssecZoneStatXfrSerial": gtmDnssecZoneStatXfrSerial,
       "gtmDnssecZoneStatXfrMasterSerial": gtmDnssecZoneStatXfrMasterSerial,
       "bigipGlobalTMCompliance": bigipGlobalTMCompliance,
       "bigipGlobalTMGroups": bigipGlobalTMGroups,
       "gtmAttrGroup": gtmAttrGroup,
       "gtmGlobalLdnsProbeProtoGroup": gtmGlobalLdnsProbeProtoGroup,
       "gtmStatGroup": gtmStatGroup,
       "gtmAppGroup": gtmAppGroup,
       "gtmAppStatusGroup": gtmAppStatusGroup,
       "gtmAppContStatGroup": gtmAppContStatGroup,
       "gtmAppContDisGroup": gtmAppContDisGroup,
       "gtmDcGroup": gtmDcGroup,
       "gtmDcStatGroup": gtmDcStatGroup,
       "gtmDcStatusGroup": gtmDcStatusGroup,
       "gtmIpGroup": gtmIpGroup,
       "gtmLinkGroup": gtmLinkGroup,
       "gtmLinkCostGroup": gtmLinkCostGroup,
       "gtmLinkStatGroup": gtmLinkStatGroup,
       "gtmLinkStatusGroup": gtmLinkStatusGroup,
       "gtmPoolGroup": gtmPoolGroup,
       "gtmPoolStatGroup": gtmPoolStatGroup,
       "gtmPoolMbrGroup": gtmPoolMbrGroup,
       "gtmPoolStatusGroup": gtmPoolStatusGroup,
       "gtmPoolMbrDepsGroup": gtmPoolMbrDepsGroup,
       "gtmPoolMbrStatGroup": gtmPoolMbrStatGroup,
       "gtmPoolMbrStatusGroup": gtmPoolMbrStatusGroup,
       "gtmRegionEntryGroup": gtmRegionEntryGroup,
       "gtmRegItemGroup": gtmRegItemGroup,
       "gtmRuleGroup": gtmRuleGroup,
       "gtmRuleEventGroup": gtmRuleEventGroup,
       "gtmRuleEventStatGroup": gtmRuleEventStatGroup,
       "gtmServerGroup": gtmServerGroup,
       "gtmServerStatGroup": gtmServerStatGroup,
       "gtmServerStatusGroup": gtmServerStatusGroup,
       "gtmTopItemGroup": gtmTopItemGroup,
       "gtmVsGroup": gtmVsGroup,
       "gtmVsDepsGroup": gtmVsDepsGroup,
       "gtmVsStatGroup": gtmVsStatGroup,
       "gtmVsStatusGroup": gtmVsStatusGroup,
       "gtmWideipGroup": gtmWideipGroup,
       "gtmWideipStatGroup": gtmWideipStatGroup,
       "gtmWideipStatusGroup": gtmWideipStatusGroup,
       "gtmWideipAliasGroup": gtmWideipAliasGroup,
       "gtmWideipPoolGroup": gtmWideipPoolGroup,
       "gtmWideipRuleGroup": gtmWideipRuleGroup,
       "gtmServerStat2Group": gtmServerStat2Group,
       "gtmProberPoolGroup": gtmProberPoolGroup,
       "gtmProberPoolStatGroup": gtmProberPoolStatGroup,
       "gtmProberPoolStatusGroup": gtmProberPoolStatusGroup,
       "gtmProberPoolMbrGroup": gtmProberPoolMbrGroup,
       "gtmProberPoolMbrStatGroup": gtmProberPoolMbrStatGroup,
       "gtmProberPoolMbrStatusGroup": gtmProberPoolMbrStatusGroup,
       "gtmAttr2Group": gtmAttr2Group,
       "gtmDnssecZoneStatGroup": gtmDnssecZoneStatGroup,
       "gtmDnssecStatGroup": gtmDnssecStatGroup}
)
