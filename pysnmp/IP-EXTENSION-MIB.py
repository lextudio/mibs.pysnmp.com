# SNMP MIB module (IP-EXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IP-EXTENSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:32 2024
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

(cjnProtocol,) = mibBuilder.importSymbols(
    "Cajun-ROOT",
    "cjnProtocol")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cjnIpv4 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CjnIpGblExt_ObjectIdentity = ObjectIdentity
cjnIpGblExt = _CjnIpGblExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 1)
)


class _CjnIpEnabled_Type(Integer32):
    """Custom type cjnIpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CjnIpEnabled_Type.__name__ = "Integer32"
_CjnIpEnabled_Object = MibScalar
cjnIpEnabled = _CjnIpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 1, 1),
    _CjnIpEnabled_Type()
)
cjnIpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpEnabled.setStatus("current")


class _CjnIpMCEnabled_Type(Integer32):
    """Custom type cjnIpMCEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CjnIpMCEnabled_Type.__name__ = "Integer32"
_CjnIpMCEnabled_Object = MibScalar
cjnIpMCEnabled = _CjnIpMCEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 1, 2),
    _CjnIpMCEnabled_Type()
)
cjnIpMCEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpMCEnabled.setStatus("current")


class _CjnIpRteEnabled_Type(Integer32):
    """Custom type cjnIpRteEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CjnIpRteEnabled_Type.__name__ = "Integer32"
_CjnIpRteEnabled_Object = MibScalar
cjnIpRteEnabled = _CjnIpRteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 1, 3),
    _CjnIpRteEnabled_Type()
)
cjnIpRteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpRteEnabled.setStatus("current")


class _CjnIpSSREnabled_Type(Integer32):
    """Custom type cjnIpSSREnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CjnIpSSREnabled_Type.__name__ = "Integer32"
_CjnIpSSREnabled_Object = MibScalar
cjnIpSSREnabled = _CjnIpSSREnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 1, 4),
    _CjnIpSSREnabled_Type()
)
cjnIpSSREnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpSSREnabled.setStatus("current")


class _CjnMaxRoutes_Type(Integer32):
    """Custom type cjnMaxRoutes based on Integer32"""
    defaultValue = 16384

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_CjnMaxRoutes_Type.__name__ = "Integer32"
_CjnMaxRoutes_Object = MibScalar
cjnMaxRoutes = _CjnMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 1, 5),
    _CjnMaxRoutes_Type()
)
cjnMaxRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnMaxRoutes.setStatus("current")


class _CjnMaxArpCacheEntries_Type(Integer32):
    """Custom type cjnMaxArpCacheEntries based on Integer32"""
    defaultValue = 16384

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_CjnMaxArpCacheEntries_Type.__name__ = "Integer32"
_CjnMaxArpCacheEntries_Object = MibScalar
cjnMaxArpCacheEntries = _CjnMaxArpCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 1, 6),
    _CjnMaxArpCacheEntries_Type()
)
cjnMaxArpCacheEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnMaxArpCacheEntries.setStatus("current")


class _CjnIpGlobalStatsReset_Type(Integer32):
    """Custom type cjnIpGlobalStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CjnIpGlobalStatsReset_Type.__name__ = "Integer32"
_CjnIpGlobalStatsReset_Object = MibScalar
cjnIpGlobalStatsReset = _CjnIpGlobalStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 1, 7),
    _CjnIpGlobalStatsReset_Type()
)
cjnIpGlobalStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpGlobalStatsReset.setStatus("current")
_CjnProxyArpGblConf_ObjectIdentity = ObjectIdentity
cjnProxyArpGblConf = _CjnProxyArpGblConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 2)
)


class _CjnProxyArpLimit_Type(Integer32):
    """Custom type cjnProxyArpLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CjnProxyArpLimit_Type.__name__ = "Integer32"
_CjnProxyArpLimit_Object = MibScalar
cjnProxyArpLimit = _CjnProxyArpLimit_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 2, 1),
    _CjnProxyArpLimit_Type()
)
cjnProxyArpLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnProxyArpLimit.setStatus("current")


class _CjnProxyArpDefRte_Type(Integer32):
    """Custom type cjnProxyArpDefRte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CjnProxyArpDefRte_Type.__name__ = "Integer32"
_CjnProxyArpDefRte_Object = MibScalar
cjnProxyArpDefRte = _CjnProxyArpDefRte_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 2, 2),
    _CjnProxyArpDefRte_Type()
)
cjnProxyArpDefRte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnProxyArpDefRte.setStatus("current")
_CjnRtePrefGblGroup_ObjectIdentity = ObjectIdentity
cjnRtePrefGblGroup = _CjnRtePrefGblGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 3)
)
_CjnLocalRtePref_Type = Integer32
_CjnLocalRtePref_Object = MibScalar
cjnLocalRtePref = _CjnLocalRtePref_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 3, 1),
    _CjnLocalRtePref_Type()
)
cjnLocalRtePref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLocalRtePref.setStatus("current")
_CjnRIPRtePref_Type = Integer32
_CjnRIPRtePref_Object = MibScalar
cjnRIPRtePref = _CjnRIPRtePref_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 3, 2),
    _CjnRIPRtePref_Type()
)
cjnRIPRtePref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnRIPRtePref.setStatus("current")
_CjnOSPFIntraAreaRtePref_Type = Integer32
_CjnOSPFIntraAreaRtePref_Object = MibScalar
cjnOSPFIntraAreaRtePref = _CjnOSPFIntraAreaRtePref_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 3, 3),
    _CjnOSPFIntraAreaRtePref_Type()
)
cjnOSPFIntraAreaRtePref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnOSPFIntraAreaRtePref.setStatus("current")
_CjnOSPFExternalRtePref_Type = Integer32
_CjnOSPFExternalRtePref_Object = MibScalar
cjnOSPFExternalRtePref = _CjnOSPFExternalRtePref_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 3, 4),
    _CjnOSPFExternalRtePref_Type()
)
cjnOSPFExternalRtePref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnOSPFExternalRtePref.setStatus("current")
_CjnHighPrefStaticRtePref_Type = Integer32
_CjnHighPrefStaticRtePref_Object = MibScalar
cjnHighPrefStaticRtePref = _CjnHighPrefStaticRtePref_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 3, 5),
    _CjnHighPrefStaticRtePref_Type()
)
cjnHighPrefStaticRtePref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnHighPrefStaticRtePref.setStatus("current")
_CjnLowPrefStaticRtePref_Type = Integer32
_CjnLowPrefStaticRtePref_Object = MibScalar
cjnLowPrefStaticRtePref = _CjnLowPrefStaticRtePref_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 3, 6),
    _CjnLowPrefStaticRtePref_Type()
)
cjnLowPrefStaticRtePref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnLowPrefStaticRtePref.setStatus("current")
_CjnOSPFInterAreaRtePref_Type = Integer32
_CjnOSPFInterAreaRtePref_Object = MibScalar
cjnOSPFInterAreaRtePref = _CjnOSPFInterAreaRtePref_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 3, 7),
    _CjnOSPFInterAreaRtePref_Type()
)
cjnOSPFInterAreaRtePref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnOSPFInterAreaRtePref.setStatus("current")
_CjnIpGblStats_ObjectIdentity = ObjectIdentity
cjnIpGblStats = _CjnIpGblStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4)
)
_CjnIpInReceives_Type = Integer32
_CjnIpInReceives_Object = MibScalar
cjnIpInReceives = _CjnIpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 1),
    _CjnIpInReceives_Type()
)
cjnIpInReceives.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpInReceives.setStatus("current")
_CjnIpInHdrErrors_Type = Integer32
_CjnIpInHdrErrors_Object = MibScalar
cjnIpInHdrErrors = _CjnIpInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 2),
    _CjnIpInHdrErrors_Type()
)
cjnIpInHdrErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpInHdrErrors.setStatus("current")
_CjnIpInAddrErrors_Type = Integer32
_CjnIpInAddrErrors_Object = MibScalar
cjnIpInAddrErrors = _CjnIpInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 3),
    _CjnIpInAddrErrors_Type()
)
cjnIpInAddrErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpInAddrErrors.setStatus("current")
_CjnIpForwDatagrams_Type = Integer32
_CjnIpForwDatagrams_Object = MibScalar
cjnIpForwDatagrams = _CjnIpForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 4),
    _CjnIpForwDatagrams_Type()
)
cjnIpForwDatagrams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpForwDatagrams.setStatus("current")
_CjnIpInUnknownProtos_Type = Integer32
_CjnIpInUnknownProtos_Object = MibScalar
cjnIpInUnknownProtos = _CjnIpInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 5),
    _CjnIpInUnknownProtos_Type()
)
cjnIpInUnknownProtos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpInUnknownProtos.setStatus("current")
_CjnIpInDiscards_Type = Integer32
_CjnIpInDiscards_Object = MibScalar
cjnIpInDiscards = _CjnIpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 6),
    _CjnIpInDiscards_Type()
)
cjnIpInDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpInDiscards.setStatus("current")
_CjnIpInDelivers_Type = Integer32
_CjnIpInDelivers_Object = MibScalar
cjnIpInDelivers = _CjnIpInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 7),
    _CjnIpInDelivers_Type()
)
cjnIpInDelivers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpInDelivers.setStatus("current")
_CjnIpOutRequests_Type = Integer32
_CjnIpOutRequests_Object = MibScalar
cjnIpOutRequests = _CjnIpOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 8),
    _CjnIpOutRequests_Type()
)
cjnIpOutRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpOutRequests.setStatus("current")
_CjnIpOutDiscards_Type = Integer32
_CjnIpOutDiscards_Object = MibScalar
cjnIpOutDiscards = _CjnIpOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 9),
    _CjnIpOutDiscards_Type()
)
cjnIpOutDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpOutDiscards.setStatus("current")
_CjnIpOutNoRoutes_Type = Integer32
_CjnIpOutNoRoutes_Object = MibScalar
cjnIpOutNoRoutes = _CjnIpOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 10),
    _CjnIpOutNoRoutes_Type()
)
cjnIpOutNoRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpOutNoRoutes.setStatus("current")
_CjnIpReasmTimeout_Type = Integer32
_CjnIpReasmTimeout_Object = MibScalar
cjnIpReasmTimeout = _CjnIpReasmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 11),
    _CjnIpReasmTimeout_Type()
)
cjnIpReasmTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpReasmTimeout.setStatus("current")
_CjnIpReasmReqds_Type = Integer32
_CjnIpReasmReqds_Object = MibScalar
cjnIpReasmReqds = _CjnIpReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 12),
    _CjnIpReasmReqds_Type()
)
cjnIpReasmReqds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpReasmReqds.setStatus("current")
_CjnIpReasmOKs_Type = Integer32
_CjnIpReasmOKs_Object = MibScalar
cjnIpReasmOKs = _CjnIpReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 13),
    _CjnIpReasmOKs_Type()
)
cjnIpReasmOKs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpReasmOKs.setStatus("current")
_CjnIpReasmFails_Type = Integer32
_CjnIpReasmFails_Object = MibScalar
cjnIpReasmFails = _CjnIpReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 14),
    _CjnIpReasmFails_Type()
)
cjnIpReasmFails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpReasmFails.setStatus("current")
_CjnIpFragOKs_Type = Integer32
_CjnIpFragOKs_Object = MibScalar
cjnIpFragOKs = _CjnIpFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 15),
    _CjnIpFragOKs_Type()
)
cjnIpFragOKs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpFragOKs.setStatus("current")
_CjnIpFragFails_Type = Integer32
_CjnIpFragFails_Object = MibScalar
cjnIpFragFails = _CjnIpFragFails_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 16),
    _CjnIpFragFails_Type()
)
cjnIpFragFails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpFragFails.setStatus("current")
_CjnIpFragCreates_Type = Integer32
_CjnIpFragCreates_Object = MibScalar
cjnIpFragCreates = _CjnIpFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 17),
    _CjnIpFragCreates_Type()
)
cjnIpFragCreates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpFragCreates.setStatus("current")
_CjnIpRoutingDiscards_Type = Integer32
_CjnIpRoutingDiscards_Object = MibScalar
cjnIpRoutingDiscards = _CjnIpRoutingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 18),
    _CjnIpRoutingDiscards_Type()
)
cjnIpRoutingDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpRoutingDiscards.setStatus("current")
_CjnIcmpInMsgs_Type = Integer32
_CjnIcmpInMsgs_Object = MibScalar
cjnIcmpInMsgs = _CjnIcmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 19),
    _CjnIcmpInMsgs_Type()
)
cjnIcmpInMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpInMsgs.setStatus("current")
_CjnIcmpInErrors_Type = Integer32
_CjnIcmpInErrors_Object = MibScalar
cjnIcmpInErrors = _CjnIcmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 20),
    _CjnIcmpInErrors_Type()
)
cjnIcmpInErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpInErrors.setStatus("current")
_CjnIcmpInDestUnreachs_Type = Integer32
_CjnIcmpInDestUnreachs_Object = MibScalar
cjnIcmpInDestUnreachs = _CjnIcmpInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 21),
    _CjnIcmpInDestUnreachs_Type()
)
cjnIcmpInDestUnreachs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpInDestUnreachs.setStatus("current")
_CjnIcmpInTimeExcds_Type = Integer32
_CjnIcmpInTimeExcds_Object = MibScalar
cjnIcmpInTimeExcds = _CjnIcmpInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 22),
    _CjnIcmpInTimeExcds_Type()
)
cjnIcmpInTimeExcds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpInTimeExcds.setStatus("current")
_CjnIcmpInParmProbs_Type = Integer32
_CjnIcmpInParmProbs_Object = MibScalar
cjnIcmpInParmProbs = _CjnIcmpInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 23),
    _CjnIcmpInParmProbs_Type()
)
cjnIcmpInParmProbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpInParmProbs.setStatus("current")
_CjnIcmpInSrcQuenchs_Type = Integer32
_CjnIcmpInSrcQuenchs_Object = MibScalar
cjnIcmpInSrcQuenchs = _CjnIcmpInSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 24),
    _CjnIcmpInSrcQuenchs_Type()
)
cjnIcmpInSrcQuenchs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpInSrcQuenchs.setStatus("current")
_CjnIcmpInRedirects_Type = Integer32
_CjnIcmpInRedirects_Object = MibScalar
cjnIcmpInRedirects = _CjnIcmpInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 25),
    _CjnIcmpInRedirects_Type()
)
cjnIcmpInRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpInRedirects.setStatus("current")
_CjnIcmpInEchos_Type = Integer32
_CjnIcmpInEchos_Object = MibScalar
cjnIcmpInEchos = _CjnIcmpInEchos_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 26),
    _CjnIcmpInEchos_Type()
)
cjnIcmpInEchos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpInEchos.setStatus("current")
_CjnIcmpInEchoReps_Type = Integer32
_CjnIcmpInEchoReps_Object = MibScalar
cjnIcmpInEchoReps = _CjnIcmpInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 27),
    _CjnIcmpInEchoReps_Type()
)
cjnIcmpInEchoReps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpInEchoReps.setStatus("current")
_CjnIcmpInTimestamps_Type = Integer32
_CjnIcmpInTimestamps_Object = MibScalar
cjnIcmpInTimestamps = _CjnIcmpInTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 28),
    _CjnIcmpInTimestamps_Type()
)
cjnIcmpInTimestamps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpInTimestamps.setStatus("current")
_CjnIcmpInTimestampReps_Type = Integer32
_CjnIcmpInTimestampReps_Object = MibScalar
cjnIcmpInTimestampReps = _CjnIcmpInTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 29),
    _CjnIcmpInTimestampReps_Type()
)
cjnIcmpInTimestampReps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpInTimestampReps.setStatus("current")
_CjnIcmpInAddrMasks_Type = Integer32
_CjnIcmpInAddrMasks_Object = MibScalar
cjnIcmpInAddrMasks = _CjnIcmpInAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 30),
    _CjnIcmpInAddrMasks_Type()
)
cjnIcmpInAddrMasks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpInAddrMasks.setStatus("current")
_CjnIcmpInAddrMaskReps_Type = Integer32
_CjnIcmpInAddrMaskReps_Object = MibScalar
cjnIcmpInAddrMaskReps = _CjnIcmpInAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 31),
    _CjnIcmpInAddrMaskReps_Type()
)
cjnIcmpInAddrMaskReps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpInAddrMaskReps.setStatus("current")
_CjnIcmpOutMsgs_Type = Integer32
_CjnIcmpOutMsgs_Object = MibScalar
cjnIcmpOutMsgs = _CjnIcmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 32),
    _CjnIcmpOutMsgs_Type()
)
cjnIcmpOutMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpOutMsgs.setStatus("current")
_CjnIcmpOutErrors_Type = Integer32
_CjnIcmpOutErrors_Object = MibScalar
cjnIcmpOutErrors = _CjnIcmpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 33),
    _CjnIcmpOutErrors_Type()
)
cjnIcmpOutErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpOutErrors.setStatus("current")
_CjnIcmpOutDestUnreachs_Type = Integer32
_CjnIcmpOutDestUnreachs_Object = MibScalar
cjnIcmpOutDestUnreachs = _CjnIcmpOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 34),
    _CjnIcmpOutDestUnreachs_Type()
)
cjnIcmpOutDestUnreachs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpOutDestUnreachs.setStatus("current")
_CjnIcmpOutTimeExcds_Type = Integer32
_CjnIcmpOutTimeExcds_Object = MibScalar
cjnIcmpOutTimeExcds = _CjnIcmpOutTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 35),
    _CjnIcmpOutTimeExcds_Type()
)
cjnIcmpOutTimeExcds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpOutTimeExcds.setStatus("current")
_CjnIcmpOutParmProbs_Type = Integer32
_CjnIcmpOutParmProbs_Object = MibScalar
cjnIcmpOutParmProbs = _CjnIcmpOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 36),
    _CjnIcmpOutParmProbs_Type()
)
cjnIcmpOutParmProbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpOutParmProbs.setStatus("current")
_CjnIcmpOutSrcQuenchs_Type = Integer32
_CjnIcmpOutSrcQuenchs_Object = MibScalar
cjnIcmpOutSrcQuenchs = _CjnIcmpOutSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 37),
    _CjnIcmpOutSrcQuenchs_Type()
)
cjnIcmpOutSrcQuenchs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpOutSrcQuenchs.setStatus("current")
_CjnIcmpOutRedirects_Type = Integer32
_CjnIcmpOutRedirects_Object = MibScalar
cjnIcmpOutRedirects = _CjnIcmpOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 38),
    _CjnIcmpOutRedirects_Type()
)
cjnIcmpOutRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpOutRedirects.setStatus("current")
_CjnIcmpOutEchos_Type = Integer32
_CjnIcmpOutEchos_Object = MibScalar
cjnIcmpOutEchos = _CjnIcmpOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 39),
    _CjnIcmpOutEchos_Type()
)
cjnIcmpOutEchos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpOutEchos.setStatus("current")
_CjnIcmpOutEchoReps_Type = Integer32
_CjnIcmpOutEchoReps_Object = MibScalar
cjnIcmpOutEchoReps = _CjnIcmpOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 40),
    _CjnIcmpOutEchoReps_Type()
)
cjnIcmpOutEchoReps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpOutEchoReps.setStatus("current")
_CjnIcmpOutTimestamps_Type = Integer32
_CjnIcmpOutTimestamps_Object = MibScalar
cjnIcmpOutTimestamps = _CjnIcmpOutTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 41),
    _CjnIcmpOutTimestamps_Type()
)
cjnIcmpOutTimestamps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpOutTimestamps.setStatus("current")
_CjnIcmpOutTimestampReps_Type = Integer32
_CjnIcmpOutTimestampReps_Object = MibScalar
cjnIcmpOutTimestampReps = _CjnIcmpOutTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 42),
    _CjnIcmpOutTimestampReps_Type()
)
cjnIcmpOutTimestampReps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpOutTimestampReps.setStatus("current")
_CjnIcmpOutAddrMasks_Type = Integer32
_CjnIcmpOutAddrMasks_Object = MibScalar
cjnIcmpOutAddrMasks = _CjnIcmpOutAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 43),
    _CjnIcmpOutAddrMasks_Type()
)
cjnIcmpOutAddrMasks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpOutAddrMasks.setStatus("current")
_CjnIcmpOutAddrMaskReps_Type = Integer32
_CjnIcmpOutAddrMaskReps_Object = MibScalar
cjnIcmpOutAddrMaskReps = _CjnIcmpOutAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 44),
    _CjnIcmpOutAddrMaskReps_Type()
)
cjnIcmpOutAddrMaskReps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIcmpOutAddrMaskReps.setStatus("current")
_CjnUdpInDatagrams_Type = Integer32
_CjnUdpInDatagrams_Object = MibScalar
cjnUdpInDatagrams = _CjnUdpInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 45),
    _CjnUdpInDatagrams_Type()
)
cjnUdpInDatagrams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnUdpInDatagrams.setStatus("current")
_CjnUdpNoPorts_Type = Integer32
_CjnUdpNoPorts_Object = MibScalar
cjnUdpNoPorts = _CjnUdpNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 46),
    _CjnUdpNoPorts_Type()
)
cjnUdpNoPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnUdpNoPorts.setStatus("current")
_CjnUdpInErrors_Type = Integer32
_CjnUdpInErrors_Object = MibScalar
cjnUdpInErrors = _CjnUdpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 47),
    _CjnUdpInErrors_Type()
)
cjnUdpInErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnUdpInErrors.setStatus("current")
_CjnUdpOutDatagrams_Type = Integer32
_CjnUdpOutDatagrams_Object = MibScalar
cjnUdpOutDatagrams = _CjnUdpOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 48),
    _CjnUdpOutDatagrams_Type()
)
cjnUdpOutDatagrams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnUdpOutDatagrams.setStatus("current")
_CjnIpmcForwDatagrams_Type = Integer32
_CjnIpmcForwDatagrams_Object = MibScalar
cjnIpmcForwDatagrams = _CjnIpmcForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 49),
    _CjnIpmcForwDatagrams_Type()
)
cjnIpmcForwDatagrams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpmcForwDatagrams.setStatus("current")
_CjnIpmcInDiscards_Type = Integer32
_CjnIpmcInDiscards_Object = MibScalar
cjnIpmcInDiscards = _CjnIpmcInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 50),
    _CjnIpmcInDiscards_Type()
)
cjnIpmcInDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpmcInDiscards.setStatus("current")
_CjnIpmcInReceives_Type = Integer32
_CjnIpmcInReceives_Object = MibScalar
cjnIpmcInReceives = _CjnIpmcInReceives_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 4, 51),
    _CjnIpmcInReceives_Type()
)
cjnIpmcInReceives.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpmcInReceives.setStatus("current")
_CjnIpNetToMediaGroup_ObjectIdentity = ObjectIdentity
cjnIpNetToMediaGroup = _CjnIpNetToMediaGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 5)
)
_CjnIpNetToMediaTable_Object = MibTable
cjnIpNetToMediaTable = _CjnIpNetToMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cjnIpNetToMediaTable.setStatus("current")
_CjnIpNetToMediaEntry_Object = MibTableRow
cjnIpNetToMediaEntry = _CjnIpNetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 5, 1, 1)
)
cjnIpNetToMediaEntry.setIndexNames(
    (0, "IP-EXTENSION-MIB", "cjnIpNetToMediaIfIndex"),
    (0, "IP-EXTENSION-MIB", "cjnIpNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    cjnIpNetToMediaEntry.setStatus("current")
_CjnIpNetToMediaIfIndex_Type = Integer32
_CjnIpNetToMediaIfIndex_Object = MibTableColumn
cjnIpNetToMediaIfIndex = _CjnIpNetToMediaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 5, 1, 1, 1),
    _CjnIpNetToMediaIfIndex_Type()
)
cjnIpNetToMediaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpNetToMediaIfIndex.setStatus("current")
_CjnIpNetToMediaPhysAddress_Type = PhysAddress
_CjnIpNetToMediaPhysAddress_Object = MibTableColumn
cjnIpNetToMediaPhysAddress = _CjnIpNetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 5, 1, 1, 2),
    _CjnIpNetToMediaPhysAddress_Type()
)
cjnIpNetToMediaPhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpNetToMediaPhysAddress.setStatus("current")
_CjnIpNetToMediaNetAddress_Type = IpAddress
_CjnIpNetToMediaNetAddress_Object = MibTableColumn
cjnIpNetToMediaNetAddress = _CjnIpNetToMediaNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 5, 1, 1, 3),
    _CjnIpNetToMediaNetAddress_Type()
)
cjnIpNetToMediaNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpNetToMediaNetAddress.setStatus("current")
_CjnIpNetToMediaRowStatus_Type = RowStatus
_CjnIpNetToMediaRowStatus_Object = MibTableColumn
cjnIpNetToMediaRowStatus = _CjnIpNetToMediaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 5, 1, 1, 4),
    _CjnIpNetToMediaRowStatus_Type()
)
cjnIpNetToMediaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpNetToMediaRowStatus.setStatus("current")


class _CjnIpNetToMediaType_Type(Integer32):
    """Custom type cjnIpNetToMediaType based on Integer32"""
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
        *(("dynamic", 3),
          ("invalid", 2),
          ("other", 1),
          ("static", 4))
    )


_CjnIpNetToMediaType_Type.__name__ = "Integer32"
_CjnIpNetToMediaType_Object = MibTableColumn
cjnIpNetToMediaType = _CjnIpNetToMediaType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1, 5, 1, 1, 5),
    _CjnIpNetToMediaType_Type()
)
cjnIpNetToMediaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpNetToMediaType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IP-EXTENSION-MIB",
    **{"cjnIpv4": cjnIpv4,
       "cjnIpGblExt": cjnIpGblExt,
       "cjnIpEnabled": cjnIpEnabled,
       "cjnIpMCEnabled": cjnIpMCEnabled,
       "cjnIpRteEnabled": cjnIpRteEnabled,
       "cjnIpSSREnabled": cjnIpSSREnabled,
       "cjnMaxRoutes": cjnMaxRoutes,
       "cjnMaxArpCacheEntries": cjnMaxArpCacheEntries,
       "cjnIpGlobalStatsReset": cjnIpGlobalStatsReset,
       "cjnProxyArpGblConf": cjnProxyArpGblConf,
       "cjnProxyArpLimit": cjnProxyArpLimit,
       "cjnProxyArpDefRte": cjnProxyArpDefRte,
       "cjnRtePrefGblGroup": cjnRtePrefGblGroup,
       "cjnLocalRtePref": cjnLocalRtePref,
       "cjnRIPRtePref": cjnRIPRtePref,
       "cjnOSPFIntraAreaRtePref": cjnOSPFIntraAreaRtePref,
       "cjnOSPFExternalRtePref": cjnOSPFExternalRtePref,
       "cjnHighPrefStaticRtePref": cjnHighPrefStaticRtePref,
       "cjnLowPrefStaticRtePref": cjnLowPrefStaticRtePref,
       "cjnOSPFInterAreaRtePref": cjnOSPFInterAreaRtePref,
       "cjnIpGblStats": cjnIpGblStats,
       "cjnIpInReceives": cjnIpInReceives,
       "cjnIpInHdrErrors": cjnIpInHdrErrors,
       "cjnIpInAddrErrors": cjnIpInAddrErrors,
       "cjnIpForwDatagrams": cjnIpForwDatagrams,
       "cjnIpInUnknownProtos": cjnIpInUnknownProtos,
       "cjnIpInDiscards": cjnIpInDiscards,
       "cjnIpInDelivers": cjnIpInDelivers,
       "cjnIpOutRequests": cjnIpOutRequests,
       "cjnIpOutDiscards": cjnIpOutDiscards,
       "cjnIpOutNoRoutes": cjnIpOutNoRoutes,
       "cjnIpReasmTimeout": cjnIpReasmTimeout,
       "cjnIpReasmReqds": cjnIpReasmReqds,
       "cjnIpReasmOKs": cjnIpReasmOKs,
       "cjnIpReasmFails": cjnIpReasmFails,
       "cjnIpFragOKs": cjnIpFragOKs,
       "cjnIpFragFails": cjnIpFragFails,
       "cjnIpFragCreates": cjnIpFragCreates,
       "cjnIpRoutingDiscards": cjnIpRoutingDiscards,
       "cjnIcmpInMsgs": cjnIcmpInMsgs,
       "cjnIcmpInErrors": cjnIcmpInErrors,
       "cjnIcmpInDestUnreachs": cjnIcmpInDestUnreachs,
       "cjnIcmpInTimeExcds": cjnIcmpInTimeExcds,
       "cjnIcmpInParmProbs": cjnIcmpInParmProbs,
       "cjnIcmpInSrcQuenchs": cjnIcmpInSrcQuenchs,
       "cjnIcmpInRedirects": cjnIcmpInRedirects,
       "cjnIcmpInEchos": cjnIcmpInEchos,
       "cjnIcmpInEchoReps": cjnIcmpInEchoReps,
       "cjnIcmpInTimestamps": cjnIcmpInTimestamps,
       "cjnIcmpInTimestampReps": cjnIcmpInTimestampReps,
       "cjnIcmpInAddrMasks": cjnIcmpInAddrMasks,
       "cjnIcmpInAddrMaskReps": cjnIcmpInAddrMaskReps,
       "cjnIcmpOutMsgs": cjnIcmpOutMsgs,
       "cjnIcmpOutErrors": cjnIcmpOutErrors,
       "cjnIcmpOutDestUnreachs": cjnIcmpOutDestUnreachs,
       "cjnIcmpOutTimeExcds": cjnIcmpOutTimeExcds,
       "cjnIcmpOutParmProbs": cjnIcmpOutParmProbs,
       "cjnIcmpOutSrcQuenchs": cjnIcmpOutSrcQuenchs,
       "cjnIcmpOutRedirects": cjnIcmpOutRedirects,
       "cjnIcmpOutEchos": cjnIcmpOutEchos,
       "cjnIcmpOutEchoReps": cjnIcmpOutEchoReps,
       "cjnIcmpOutTimestamps": cjnIcmpOutTimestamps,
       "cjnIcmpOutTimestampReps": cjnIcmpOutTimestampReps,
       "cjnIcmpOutAddrMasks": cjnIcmpOutAddrMasks,
       "cjnIcmpOutAddrMaskReps": cjnIcmpOutAddrMaskReps,
       "cjnUdpInDatagrams": cjnUdpInDatagrams,
       "cjnUdpNoPorts": cjnUdpNoPorts,
       "cjnUdpInErrors": cjnUdpInErrors,
       "cjnUdpOutDatagrams": cjnUdpOutDatagrams,
       "cjnIpmcForwDatagrams": cjnIpmcForwDatagrams,
       "cjnIpmcInDiscards": cjnIpmcInDiscards,
       "cjnIpmcInReceives": cjnIpmcInReceives,
       "cjnIpNetToMediaGroup": cjnIpNetToMediaGroup,
       "cjnIpNetToMediaTable": cjnIpNetToMediaTable,
       "cjnIpNetToMediaEntry": cjnIpNetToMediaEntry,
       "cjnIpNetToMediaIfIndex": cjnIpNetToMediaIfIndex,
       "cjnIpNetToMediaPhysAddress": cjnIpNetToMediaPhysAddress,
       "cjnIpNetToMediaNetAddress": cjnIpNetToMediaNetAddress,
       "cjnIpNetToMediaRowStatus": cjnIpNetToMediaRowStatus,
       "cjnIpNetToMediaType": cjnIpNetToMediaType}
)
