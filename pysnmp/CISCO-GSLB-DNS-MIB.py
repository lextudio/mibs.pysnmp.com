# SNMP MIB module (CISCO-GSLB-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GSLB-DNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:59 2024
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

(CiscoGslbAnswerAdminState,
 CiscoGslbAnswerStatus,
 CiscoGslbAnswerType,
 CiscoGslbBalanceMethod) = mibBuilder.importSymbols(
    "CISCO-GSLB-TC-MIB",
    "CiscoGslbAnswerAdminState",
    "CiscoGslbAnswerStatus",
    "CiscoGslbAnswerType",
    "CiscoGslbBalanceMethod")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressDNS,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressDNS",
    "InetAddressPrefixLength",
    "InetAddressType")

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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoGslbDnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 595)
)
ciscoGslbDnsMIB.setRevisions(
        ("2007-04-09 00:00",
         "2006-11-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoGslbDnsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoGslbDnsMIBNotifs = _CiscoGslbDnsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 0)
)
_CiscoGslbDnsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoGslbDnsMIBObjects = _CiscoGslbDnsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1)
)
_CgdNotifControl_ObjectIdentity = ObjectIdentity
cgdNotifControl = _CgdNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 1)
)


class _CgdDnsClauseNotifEnable_Type(TruthValue):
    """Custom type cgdDnsClauseNotifEnable based on TruthValue"""


_CgdDnsClauseNotifEnable_Object = MibScalar
cgdDnsClauseNotifEnable = _CgdDnsClauseNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 1, 1),
    _CgdDnsClauseNotifEnable_Type()
)
cgdDnsClauseNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgdDnsClauseNotifEnable.setStatus("current")


class _CgdDnsAnswerNotifEnable_Type(TruthValue):
    """Custom type cgdDnsAnswerNotifEnable based on TruthValue"""


_CgdDnsAnswerNotifEnable_Object = MibScalar
cgdDnsAnswerNotifEnable = _CgdDnsAnswerNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 1, 2),
    _CgdDnsAnswerNotifEnable_Type()
)
cgdDnsAnswerNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgdDnsAnswerNotifEnable.setStatus("current")
_CgdNotifObjects_ObjectIdentity = ObjectIdentity
cgdNotifObjects = _CgdNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 2)
)
_CgdAnswerPrevStatus_Type = CiscoGslbAnswerStatus
_CgdAnswerPrevStatus_Object = MibScalar
cgdAnswerPrevStatus = _CgdAnswerPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 2, 1),
    _CgdAnswerPrevStatus_Type()
)
cgdAnswerPrevStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgdAnswerPrevStatus.setStatus("current")
_CgdGlobal_ObjectIdentity = ObjectIdentity
cgdGlobal = _CgdGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 3)
)
_CgdTotalDomains_Type = Unsigned32
_CgdTotalDomains_Object = MibScalar
cgdTotalDomains = _CgdTotalDomains_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 3, 1),
    _CgdTotalDomains_Type()
)
cgdTotalDomains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdTotalDomains.setStatus("current")
_CgdTotalDomainLists_Type = Unsigned32
_CgdTotalDomainLists_Object = MibScalar
cgdTotalDomainLists = _CgdTotalDomainLists_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 3, 2),
    _CgdTotalDomainLists_Type()
)
cgdTotalDomainLists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdTotalDomainLists.setStatus("current")
_CgdTotalSourceAddresses_Type = Unsigned32
_CgdTotalSourceAddresses_Object = MibScalar
cgdTotalSourceAddresses = _CgdTotalSourceAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 3, 3),
    _CgdTotalSourceAddresses_Type()
)
cgdTotalSourceAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdTotalSourceAddresses.setStatus("current")
_CgdTotalSourceAddressLists_Type = Unsigned32
_CgdTotalSourceAddressLists_Object = MibScalar
cgdTotalSourceAddressLists = _CgdTotalSourceAddressLists_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 3, 4),
    _CgdTotalSourceAddressLists_Type()
)
cgdTotalSourceAddressLists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdTotalSourceAddressLists.setStatus("current")
_CgdTotalAnswers_Type = Unsigned32
_CgdTotalAnswers_Object = MibScalar
cgdTotalAnswers = _CgdTotalAnswers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 3, 5),
    _CgdTotalAnswers_Type()
)
cgdTotalAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdTotalAnswers.setStatus("current")
_CgdTotalAnswerGroups_Type = Unsigned32
_CgdTotalAnswerGroups_Object = MibScalar
cgdTotalAnswerGroups = _CgdTotalAnswerGroups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 3, 6),
    _CgdTotalAnswerGroups_Type()
)
cgdTotalAnswerGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdTotalAnswerGroups.setStatus("current")
_CgdTotalRules_Type = Unsigned32
_CgdTotalRules_Object = MibScalar
cgdTotalRules = _CgdTotalRules_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 3, 7),
    _CgdTotalRules_Type()
)
cgdTotalRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdTotalRules.setStatus("current")


class _CgdAnsTrapRateLimit_Type(Unsigned32):
    """Custom type cgdAnsTrapRateLimit based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CgdAnsTrapRateLimit_Type.__name__ = "Unsigned32"
_CgdAnsTrapRateLimit_Object = MibScalar
cgdAnsTrapRateLimit = _CgdAnsTrapRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 3, 8),
    _CgdAnsTrapRateLimit_Type()
)
cgdAnsTrapRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdAnsTrapRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    cgdAnsTrapRateLimit.setUnits("traps per minute")


class _CgdDnsClauseTrapRateLimit_Type(Unsigned32):
    """Custom type cgdDnsClauseTrapRateLimit based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CgdDnsClauseTrapRateLimit_Type.__name__ = "Unsigned32"
_CgdDnsClauseTrapRateLimit_Object = MibScalar
cgdDnsClauseTrapRateLimit = _CgdDnsClauseTrapRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 3, 9),
    _CgdDnsClauseTrapRateLimit_Type()
)
cgdDnsClauseTrapRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDnsClauseTrapRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    cgdDnsClauseTrapRateLimit.setUnits("traps per minute")
_CgdGlobalStats_ObjectIdentity = ObjectIdentity
cgdGlobalStats = _CgdGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 4)
)
_CgdDnsRcvdQueries_Type = Counter32
_CgdDnsRcvdQueries_Object = MibScalar
cgdDnsRcvdQueries = _CgdDnsRcvdQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 4, 1),
    _CgdDnsRcvdQueries_Type()
)
cgdDnsRcvdQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDnsRcvdQueries.setStatus("current")
if mibBuilder.loadTexts:
    cgdDnsRcvdQueries.setUnits("queries")
_CgdDnsRcvdHostAddrQueries_Type = Counter32
_CgdDnsRcvdHostAddrQueries_Object = MibScalar
cgdDnsRcvdHostAddrQueries = _CgdDnsRcvdHostAddrQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 4, 2),
    _CgdDnsRcvdHostAddrQueries_Type()
)
cgdDnsRcvdHostAddrQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDnsRcvdHostAddrQueries.setStatus("current")
if mibBuilder.loadTexts:
    cgdDnsRcvdHostAddrQueries.setUnits("queries")
_CgdDnsUnmatchedQueries_Type = Counter32
_CgdDnsUnmatchedQueries_Object = MibScalar
cgdDnsUnmatchedQueries = _CgdDnsUnmatchedQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 4, 3),
    _CgdDnsUnmatchedQueries_Type()
)
cgdDnsUnmatchedQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDnsUnmatchedQueries.setStatus("current")
if mibBuilder.loadTexts:
    cgdDnsUnmatchedQueries.setUnits("queries")
_CgdDnsDroppedQueries_Type = Counter32
_CgdDnsDroppedQueries_Object = MibScalar
cgdDnsDroppedQueries = _CgdDnsDroppedQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 4, 4),
    _CgdDnsDroppedQueries_Type()
)
cgdDnsDroppedQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDnsDroppedQueries.setStatus("current")
if mibBuilder.loadTexts:
    cgdDnsDroppedQueries.setUnits("queries")
_CgdNSFwdSentQueries_Type = Counter32
_CgdNSFwdSentQueries_Object = MibScalar
cgdNSFwdSentQueries = _CgdNSFwdSentQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 4, 5),
    _CgdNSFwdSentQueries_Type()
)
cgdNSFwdSentQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdNSFwdSentQueries.setStatus("current")
if mibBuilder.loadTexts:
    cgdNSFwdSentQueries.setUnits("queries")
_CgdNSFwdRcvdResps_Type = Counter32
_CgdNSFwdRcvdResps_Object = MibScalar
cgdNSFwdRcvdResps = _CgdNSFwdRcvdResps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 4, 6),
    _CgdNSFwdRcvdResps_Type()
)
cgdNSFwdRcvdResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdNSFwdRcvdResps.setStatus("current")
if mibBuilder.loadTexts:
    cgdNSFwdRcvdResps.setUnits("responses")
_CgdBoomServSentReqs_Type = Counter32
_CgdBoomServSentReqs_Object = MibScalar
cgdBoomServSentReqs = _CgdBoomServSentReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 4, 7),
    _CgdBoomServSentReqs_Type()
)
cgdBoomServSentReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdBoomServSentReqs.setStatus("current")
if mibBuilder.loadTexts:
    cgdBoomServSentReqs.setUnits("requests")
_CgdProxLkupSentReqs_Type = Counter32
_CgdProxLkupSentReqs_Object = MibScalar
cgdProxLkupSentReqs = _CgdProxLkupSentReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 4, 8),
    _CgdProxLkupSentReqs_Type()
)
cgdProxLkupSentReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdProxLkupSentReqs.setStatus("current")
if mibBuilder.loadTexts:
    cgdProxLkupSentReqs.setUnits("requests")
_CgdProxLkupRcvdResps_Type = Counter32
_CgdProxLkupRcvdResps_Object = MibScalar
cgdProxLkupRcvdResps = _CgdProxLkupRcvdResps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 4, 9),
    _CgdProxLkupRcvdResps_Type()
)
cgdProxLkupRcvdResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdProxLkupRcvdResps.setStatus("current")
if mibBuilder.loadTexts:
    cgdProxLkupRcvdResps.setUnits("responses")
_CgdDnsQueryRateCurrent_Type = Gauge32
_CgdDnsQueryRateCurrent_Object = MibScalar
cgdDnsQueryRateCurrent = _CgdDnsQueryRateCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 4, 10),
    _CgdDnsQueryRateCurrent_Type()
)
cgdDnsQueryRateCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDnsQueryRateCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cgdDnsQueryRateCurrent.setUnits("requests per second")
_CgdDnsQueryRatePeak_Type = Unsigned32
_CgdDnsQueryRatePeak_Object = MibScalar
cgdDnsQueryRatePeak = _CgdDnsQueryRatePeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 4, 11),
    _CgdDnsQueryRatePeak_Type()
)
cgdDnsQueryRatePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDnsQueryRatePeak.setStatus("current")
if mibBuilder.loadTexts:
    cgdDnsQueryRatePeak.setUnits("requests per second")
_CgdDnsUdpSrcPortErrs_Type = Counter32
_CgdDnsUdpSrcPortErrs_Object = MibScalar
cgdDnsUdpSrcPortErrs = _CgdDnsUdpSrcPortErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 4, 12),
    _CgdDnsUdpSrcPortErrs_Type()
)
cgdDnsUdpSrcPortErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDnsUdpSrcPortErrs.setStatus("current")
if mibBuilder.loadTexts:
    cgdDnsUdpSrcPortErrs.setUnits("errors")
_CgdDnsTcpSrcPortErrs_Type = Counter32
_CgdDnsTcpSrcPortErrs_Object = MibScalar
cgdDnsTcpSrcPortErrs = _CgdDnsTcpSrcPortErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 4, 13),
    _CgdDnsTcpSrcPortErrs_Type()
)
cgdDnsTcpSrcPortErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDnsTcpSrcPortErrs.setStatus("current")
if mibBuilder.loadTexts:
    cgdDnsTcpSrcPortErrs.setUnits("errors")
_CgdDnsPollSockErrs_Type = Counter32
_CgdDnsPollSockErrs_Object = MibScalar
cgdDnsPollSockErrs = _CgdDnsPollSockErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 4, 14),
    _CgdDnsPollSockErrs_Type()
)
cgdDnsPollSockErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDnsPollSockErrs.setStatus("current")
if mibBuilder.loadTexts:
    cgdDnsPollSockErrs.setUnits("errors")
_CgdDroppedAnsNotifs_Type = Unsigned32
_CgdDroppedAnsNotifs_Object = MibScalar
cgdDroppedAnsNotifs = _CgdDroppedAnsNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 4, 15),
    _CgdDroppedAnsNotifs_Type()
)
cgdDroppedAnsNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDroppedAnsNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cgdDroppedAnsNotifs.setUnits("traps")
_CgdDroppedDnsClauseNotifs_Type = Unsigned32
_CgdDroppedDnsClauseNotifs_Object = MibScalar
cgdDroppedDnsClauseNotifs = _CgdDroppedDnsClauseNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 4, 16),
    _CgdDroppedDnsClauseNotifs_Type()
)
cgdDroppedDnsClauseNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDroppedDnsClauseNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cgdDroppedDnsClauseNotifs.setUnits("traps")
_CgdAnswer_ObjectIdentity = ObjectIdentity
cgdAnswer = _CgdAnswer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5)
)
_CgdAnswerGroupTable_Object = MibTable
cgdAnswerGroupTable = _CgdAnswerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cgdAnswerGroupTable.setStatus("current")
_CgdAnswerGroupEntry_Object = MibTableRow
cgdAnswerGroupEntry = _CgdAnswerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 1, 1)
)
cgdAnswerGroupEntry.setIndexNames(
    (0, "CISCO-GSLB-DNS-MIB", "cgdAnswerGroupName"),
)
if mibBuilder.loadTexts:
    cgdAnswerGroupEntry.setStatus("current")


class _CgdAnswerGroupName_Type(SnmpAdminString):
    """Custom type cgdAnswerGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CgdAnswerGroupName_Type.__name__ = "SnmpAdminString"
_CgdAnswerGroupName_Object = MibTableColumn
cgdAnswerGroupName = _CgdAnswerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 1, 1, 1),
    _CgdAnswerGroupName_Type()
)
cgdAnswerGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgdAnswerGroupName.setStatus("current")
_CgdAnswerGroupType_Type = CiscoGslbAnswerType
_CgdAnswerGroupType_Object = MibTableColumn
cgdAnswerGroupType = _CgdAnswerGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 1, 1, 2),
    _CgdAnswerGroupType_Type()
)
cgdAnswerGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdAnswerGroupType.setStatus("current")
_CgdAnswerGroupHits_Type = Counter32
_CgdAnswerGroupHits_Object = MibTableColumn
cgdAnswerGroupHits = _CgdAnswerGroupHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 1, 1, 3),
    _CgdAnswerGroupHits_Type()
)
cgdAnswerGroupHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdAnswerGroupHits.setStatus("current")
if mibBuilder.loadTexts:
    cgdAnswerGroupHits.setUnits("number of hits")


class _CgdAnswerGroupStorageType_Type(StorageType):
    """Custom type cgdAnswerGroupStorageType based on StorageType"""


_CgdAnswerGroupStorageType_Object = MibTableColumn
cgdAnswerGroupStorageType = _CgdAnswerGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 1, 1, 4),
    _CgdAnswerGroupStorageType_Type()
)
cgdAnswerGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdAnswerGroupStorageType.setStatus("current")
_CgdAnswerGroupRowStatus_Type = RowStatus
_CgdAnswerGroupRowStatus_Object = MibTableColumn
cgdAnswerGroupRowStatus = _CgdAnswerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 1, 1, 5),
    _CgdAnswerGroupRowStatus_Type()
)
cgdAnswerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdAnswerGroupRowStatus.setStatus("current")
_CgdAnswerTable_Object = MibTable
cgdAnswerTable = _CgdAnswerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cgdAnswerTable.setStatus("current")
_CgdAnswerEntry_Object = MibTableRow
cgdAnswerEntry = _CgdAnswerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 2, 1)
)
cgdAnswerEntry.setIndexNames(
    (0, "CISCO-GSLB-DNS-MIB", "cgdAnswerId"),
)
if mibBuilder.loadTexts:
    cgdAnswerEntry.setStatus("current")


class _CgdAnswerId_Type(Unsigned32):
    """Custom type cgdAnswerId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CgdAnswerId_Type.__name__ = "Unsigned32"
_CgdAnswerId_Object = MibTableColumn
cgdAnswerId = _CgdAnswerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 2, 1, 1),
    _CgdAnswerId_Type()
)
cgdAnswerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgdAnswerId.setStatus("current")
_CgdAnswerType_Type = CiscoGslbAnswerType
_CgdAnswerType_Object = MibTableColumn
cgdAnswerType = _CgdAnswerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 2, 1, 2),
    _CgdAnswerType_Type()
)
cgdAnswerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdAnswerType.setStatus("current")


class _CgdAnswerAddressType_Type(InetAddressType):
    """Custom type cgdAnswerAddressType based on InetAddressType"""


_CgdAnswerAddressType_Object = MibTableColumn
cgdAnswerAddressType = _CgdAnswerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 2, 1, 3),
    _CgdAnswerAddressType_Type()
)
cgdAnswerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdAnswerAddressType.setStatus("current")
_CgdAnswerAddress_Type = InetAddress
_CgdAnswerAddress_Object = MibTableColumn
cgdAnswerAddress = _CgdAnswerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 2, 1, 4),
    _CgdAnswerAddress_Type()
)
cgdAnswerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdAnswerAddress.setStatus("current")
_CgdAnswerName_Type = SnmpAdminString
_CgdAnswerName_Object = MibTableColumn
cgdAnswerName = _CgdAnswerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 2, 1, 5),
    _CgdAnswerName_Type()
)
cgdAnswerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdAnswerName.setStatus("current")


class _CgdAnswerGrpName_Type(SnmpAdminString):
    """Custom type cgdAnswerGrpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CgdAnswerGrpName_Type.__name__ = "SnmpAdminString"
_CgdAnswerGrpName_Object = MibTableColumn
cgdAnswerGrpName = _CgdAnswerGrpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 2, 1, 6),
    _CgdAnswerGrpName_Type()
)
cgdAnswerGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdAnswerGrpName.setStatus("current")


class _CgdAnswerAdminState_Type(CiscoGslbAnswerAdminState):
    """Custom type cgdAnswerAdminState based on CiscoGslbAnswerAdminState"""


_CgdAnswerAdminState_Object = MibTableColumn
cgdAnswerAdminState = _CgdAnswerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 2, 1, 7),
    _CgdAnswerAdminState_Type()
)
cgdAnswerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdAnswerAdminState.setStatus("current")
_CgdAnswerStatus_Type = CiscoGslbAnswerStatus
_CgdAnswerStatus_Object = MibTableColumn
cgdAnswerStatus = _CgdAnswerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 2, 1, 8),
    _CgdAnswerStatus_Type()
)
cgdAnswerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdAnswerStatus.setStatus("current")
_CgdAnswerHits_Type = Counter32
_CgdAnswerHits_Object = MibTableColumn
cgdAnswerHits = _CgdAnswerHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 2, 1, 9),
    _CgdAnswerHits_Type()
)
cgdAnswerHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdAnswerHits.setStatus("current")
if mibBuilder.loadTexts:
    cgdAnswerHits.setUnits("number of hits")
_CgdAnswerRate1Min_Type = Gauge32
_CgdAnswerRate1Min_Object = MibTableColumn
cgdAnswerRate1Min = _CgdAnswerRate1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 2, 1, 10),
    _CgdAnswerRate1Min_Type()
)
cgdAnswerRate1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdAnswerRate1Min.setStatus("current")
if mibBuilder.loadTexts:
    cgdAnswerRate1Min.setUnits("hits per second")
_CgdAnswerRate5Min_Type = Gauge32
_CgdAnswerRate5Min_Object = MibTableColumn
cgdAnswerRate5Min = _CgdAnswerRate5Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 2, 1, 11),
    _CgdAnswerRate5Min_Type()
)
cgdAnswerRate5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdAnswerRate5Min.setStatus("current")
if mibBuilder.loadTexts:
    cgdAnswerRate5Min.setUnits("hits per second")
_CgdAnswerRate30Min_Type = Gauge32
_CgdAnswerRate30Min_Object = MibTableColumn
cgdAnswerRate30Min = _CgdAnswerRate30Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 2, 1, 12),
    _CgdAnswerRate30Min_Type()
)
cgdAnswerRate30Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdAnswerRate30Min.setStatus("current")
if mibBuilder.loadTexts:
    cgdAnswerRate30Min.setUnits("hits per second")
_CgdAnswerRate4Hr_Type = Gauge32
_CgdAnswerRate4Hr_Object = MibTableColumn
cgdAnswerRate4Hr = _CgdAnswerRate4Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 2, 1, 13),
    _CgdAnswerRate4Hr_Type()
)
cgdAnswerRate4Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdAnswerRate4Hr.setStatus("current")
if mibBuilder.loadTexts:
    cgdAnswerRate4Hr.setUnits("hits per second")


class _CgdAnswerStorageType_Type(StorageType):
    """Custom type cgdAnswerStorageType based on StorageType"""


_CgdAnswerStorageType_Object = MibTableColumn
cgdAnswerStorageType = _CgdAnswerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 2, 1, 14),
    _CgdAnswerStorageType_Type()
)
cgdAnswerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdAnswerStorageType.setStatus("current")
_CgdAnswerRowStatus_Type = RowStatus
_CgdAnswerRowStatus_Object = MibTableColumn
cgdAnswerRowStatus = _CgdAnswerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 5, 2, 1, 15),
    _CgdAnswerRowStatus_Type()
)
cgdAnswerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdAnswerRowStatus.setStatus("current")
_CgdDomain_ObjectIdentity = ObjectIdentity
cgdDomain = _CgdDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6)
)
_CgdDomainListTable_Object = MibTable
cgdDomainListTable = _CgdDomainListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cgdDomainListTable.setStatus("current")
_CgdDomainListEntry_Object = MibTableRow
cgdDomainListEntry = _CgdDomainListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 1, 1)
)
cgdDomainListEntry.setIndexNames(
    (0, "CISCO-GSLB-DNS-MIB", "cgdDomainListName"),
)
if mibBuilder.loadTexts:
    cgdDomainListEntry.setStatus("current")


class _CgdDomainListName_Type(SnmpAdminString):
    """Custom type cgdDomainListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CgdDomainListName_Type.__name__ = "SnmpAdminString"
_CgdDomainListName_Object = MibTableColumn
cgdDomainListName = _CgdDomainListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 1, 1, 1),
    _CgdDomainListName_Type()
)
cgdDomainListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgdDomainListName.setStatus("current")
_CgdDomainListHits_Type = Counter32
_CgdDomainListHits_Object = MibTableColumn
cgdDomainListHits = _CgdDomainListHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 1, 1, 2),
    _CgdDomainListHits_Type()
)
cgdDomainListHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDomainListHits.setStatus("current")
if mibBuilder.loadTexts:
    cgdDomainListHits.setUnits("number of hits")


class _CgdDomainListStorageType_Type(StorageType):
    """Custom type cgdDomainListStorageType based on StorageType"""


_CgdDomainListStorageType_Object = MibTableColumn
cgdDomainListStorageType = _CgdDomainListStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 1, 1, 3),
    _CgdDomainListStorageType_Type()
)
cgdDomainListStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdDomainListStorageType.setStatus("current")
_CgdDomainListRowStatus_Type = RowStatus
_CgdDomainListRowStatus_Object = MibTableColumn
cgdDomainListRowStatus = _CgdDomainListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 1, 1, 4),
    _CgdDomainListRowStatus_Type()
)
cgdDomainListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdDomainListRowStatus.setStatus("current")
_CgdDomainTable_Object = MibTable
cgdDomainTable = _CgdDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cgdDomainTable.setStatus("current")
_CgdDomainEntry_Object = MibTableRow
cgdDomainEntry = _CgdDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 2, 1)
)
cgdDomainEntry.setIndexNames(
    (0, "CISCO-GSLB-DNS-MIB", "cgdDomainId"),
)
if mibBuilder.loadTexts:
    cgdDomainEntry.setStatus("current")


class _CgdDomainId_Type(Unsigned32):
    """Custom type cgdDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CgdDomainId_Type.__name__ = "Unsigned32"
_CgdDomainId_Object = MibTableColumn
cgdDomainId = _CgdDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 2, 1, 1),
    _CgdDomainId_Type()
)
cgdDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgdDomainId.setStatus("current")
_CgdDomainName_Type = InetAddressDNS
_CgdDomainName_Object = MibTableColumn
cgdDomainName = _CgdDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 2, 1, 2),
    _CgdDomainName_Type()
)
cgdDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdDomainName.setStatus("current")


class _CgdDomainList_Type(SnmpAdminString):
    """Custom type cgdDomainList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CgdDomainList_Type.__name__ = "SnmpAdminString"
_CgdDomainList_Object = MibTableColumn
cgdDomainList = _CgdDomainList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 2, 1, 3),
    _CgdDomainList_Type()
)
cgdDomainList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdDomainList.setStatus("current")
_CgdDomainHits_Type = Counter32
_CgdDomainHits_Object = MibTableColumn
cgdDomainHits = _CgdDomainHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 2, 1, 4),
    _CgdDomainHits_Type()
)
cgdDomainHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDomainHits.setStatus("current")
if mibBuilder.loadTexts:
    cgdDomainHits.setUnits("number of hits")
_CgdDomainRate1Min_Type = Gauge32
_CgdDomainRate1Min_Object = MibTableColumn
cgdDomainRate1Min = _CgdDomainRate1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 2, 1, 5),
    _CgdDomainRate1Min_Type()
)
cgdDomainRate1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDomainRate1Min.setStatus("current")
if mibBuilder.loadTexts:
    cgdDomainRate1Min.setUnits("hits per second")
_CgdDomainRate5Min_Type = Gauge32
_CgdDomainRate5Min_Object = MibTableColumn
cgdDomainRate5Min = _CgdDomainRate5Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 2, 1, 6),
    _CgdDomainRate5Min_Type()
)
cgdDomainRate5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDomainRate5Min.setStatus("current")
if mibBuilder.loadTexts:
    cgdDomainRate5Min.setUnits("hits per second")
_CgdDomainRate30Min_Type = Gauge32
_CgdDomainRate30Min_Object = MibTableColumn
cgdDomainRate30Min = _CgdDomainRate30Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 2, 1, 7),
    _CgdDomainRate30Min_Type()
)
cgdDomainRate30Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDomainRate30Min.setStatus("current")
if mibBuilder.loadTexts:
    cgdDomainRate30Min.setUnits("hits per second")
_CgdDomainRate4Hr_Type = Gauge32
_CgdDomainRate4Hr_Object = MibTableColumn
cgdDomainRate4Hr = _CgdDomainRate4Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 2, 1, 8),
    _CgdDomainRate4Hr_Type()
)
cgdDomainRate4Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDomainRate4Hr.setStatus("current")
if mibBuilder.loadTexts:
    cgdDomainRate4Hr.setUnits("hits per second")


class _CgdDomainStorageType_Type(StorageType):
    """Custom type cgdDomainStorageType based on StorageType"""


_CgdDomainStorageType_Object = MibTableColumn
cgdDomainStorageType = _CgdDomainStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 2, 1, 9),
    _CgdDomainStorageType_Type()
)
cgdDomainStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdDomainStorageType.setStatus("current")
_CgdDomainRowStatus_Type = RowStatus
_CgdDomainRowStatus_Object = MibTableColumn
cgdDomainRowStatus = _CgdDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 6, 2, 1, 10),
    _CgdDomainRowStatus_Type()
)
cgdDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdDomainRowStatus.setStatus("current")
_CgdSourceAdd_ObjectIdentity = ObjectIdentity
cgdSourceAdd = _CgdSourceAdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7)
)
_CgdSourceAddressListTable_Object = MibTable
cgdSourceAddressListTable = _CgdSourceAddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cgdSourceAddressListTable.setStatus("current")
_CgdSourceAddressListEntry_Object = MibTableRow
cgdSourceAddressListEntry = _CgdSourceAddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 1, 1)
)
cgdSourceAddressListEntry.setIndexNames(
    (0, "CISCO-GSLB-DNS-MIB", "cgdSourceAddressListName"),
)
if mibBuilder.loadTexts:
    cgdSourceAddressListEntry.setStatus("current")


class _CgdSourceAddressListName_Type(SnmpAdminString):
    """Custom type cgdSourceAddressListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CgdSourceAddressListName_Type.__name__ = "SnmpAdminString"
_CgdSourceAddressListName_Object = MibTableColumn
cgdSourceAddressListName = _CgdSourceAddressListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 1, 1, 1),
    _CgdSourceAddressListName_Type()
)
cgdSourceAddressListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgdSourceAddressListName.setStatus("current")
_CgdSourceAddressListHits_Type = Counter32
_CgdSourceAddressListHits_Object = MibTableColumn
cgdSourceAddressListHits = _CgdSourceAddressListHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 1, 1, 2),
    _CgdSourceAddressListHits_Type()
)
cgdSourceAddressListHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdSourceAddressListHits.setStatus("current")
if mibBuilder.loadTexts:
    cgdSourceAddressListHits.setUnits("number of hits")


class _CgdSourceAddressListStorageType_Type(StorageType):
    """Custom type cgdSourceAddressListStorageType based on StorageType"""


_CgdSourceAddressListStorageType_Object = MibTableColumn
cgdSourceAddressListStorageType = _CgdSourceAddressListStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 1, 1, 3),
    _CgdSourceAddressListStorageType_Type()
)
cgdSourceAddressListStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdSourceAddressListStorageType.setStatus("current")
_CgdSourceAddressListRowStatus_Type = RowStatus
_CgdSourceAddressListRowStatus_Object = MibTableColumn
cgdSourceAddressListRowStatus = _CgdSourceAddressListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 1, 1, 4),
    _CgdSourceAddressListRowStatus_Type()
)
cgdSourceAddressListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdSourceAddressListRowStatus.setStatus("current")
_CgdSourceAddressTable_Object = MibTable
cgdSourceAddressTable = _CgdSourceAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 2)
)
if mibBuilder.loadTexts:
    cgdSourceAddressTable.setStatus("current")
_CgdSourceAddressEntry_Object = MibTableRow
cgdSourceAddressEntry = _CgdSourceAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 2, 1)
)
cgdSourceAddressEntry.setIndexNames(
    (0, "CISCO-GSLB-DNS-MIB", "cgdSourceAddressId"),
)
if mibBuilder.loadTexts:
    cgdSourceAddressEntry.setStatus("current")


class _CgdSourceAddressId_Type(Unsigned32):
    """Custom type cgdSourceAddressId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CgdSourceAddressId_Type.__name__ = "Unsigned32"
_CgdSourceAddressId_Object = MibTableColumn
cgdSourceAddressId = _CgdSourceAddressId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 2, 1, 1),
    _CgdSourceAddressId_Type()
)
cgdSourceAddressId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgdSourceAddressId.setStatus("current")


class _CgdSourceAddressAddressType_Type(InetAddressType):
    """Custom type cgdSourceAddressAddressType based on InetAddressType"""


_CgdSourceAddressAddressType_Object = MibTableColumn
cgdSourceAddressAddressType = _CgdSourceAddressAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 2, 1, 2),
    _CgdSourceAddressAddressType_Type()
)
cgdSourceAddressAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdSourceAddressAddressType.setStatus("current")
_CgdSourceAddressAddress_Type = InetAddress
_CgdSourceAddressAddress_Object = MibTableColumn
cgdSourceAddressAddress = _CgdSourceAddressAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 2, 1, 3),
    _CgdSourceAddressAddress_Type()
)
cgdSourceAddressAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdSourceAddressAddress.setStatus("current")
_CgdSourceAddressPrefixLength_Type = InetAddressPrefixLength
_CgdSourceAddressPrefixLength_Object = MibTableColumn
cgdSourceAddressPrefixLength = _CgdSourceAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 2, 1, 4),
    _CgdSourceAddressPrefixLength_Type()
)
cgdSourceAddressPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdSourceAddressPrefixLength.setStatus("current")


class _CgdSourceAddressList_Type(SnmpAdminString):
    """Custom type cgdSourceAddressList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CgdSourceAddressList_Type.__name__ = "SnmpAdminString"
_CgdSourceAddressList_Object = MibTableColumn
cgdSourceAddressList = _CgdSourceAddressList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 2, 1, 5),
    _CgdSourceAddressList_Type()
)
cgdSourceAddressList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdSourceAddressList.setStatus("current")
_CgdSourceAddressHits_Type = Counter32
_CgdSourceAddressHits_Object = MibTableColumn
cgdSourceAddressHits = _CgdSourceAddressHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 2, 1, 6),
    _CgdSourceAddressHits_Type()
)
cgdSourceAddressHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdSourceAddressHits.setStatus("current")
if mibBuilder.loadTexts:
    cgdSourceAddressHits.setUnits("number of hits")
_CgdSourceAddressRate1Min_Type = Gauge32
_CgdSourceAddressRate1Min_Object = MibTableColumn
cgdSourceAddressRate1Min = _CgdSourceAddressRate1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 2, 1, 7),
    _CgdSourceAddressRate1Min_Type()
)
cgdSourceAddressRate1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdSourceAddressRate1Min.setStatus("current")
if mibBuilder.loadTexts:
    cgdSourceAddressRate1Min.setUnits("hits per second")
_CgdSourceAddressRate5Min_Type = Gauge32
_CgdSourceAddressRate5Min_Object = MibTableColumn
cgdSourceAddressRate5Min = _CgdSourceAddressRate5Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 2, 1, 8),
    _CgdSourceAddressRate5Min_Type()
)
cgdSourceAddressRate5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdSourceAddressRate5Min.setStatus("current")
if mibBuilder.loadTexts:
    cgdSourceAddressRate5Min.setUnits("hits per second")
_CgdSourceAddressRate30Min_Type = Gauge32
_CgdSourceAddressRate30Min_Object = MibTableColumn
cgdSourceAddressRate30Min = _CgdSourceAddressRate30Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 2, 1, 9),
    _CgdSourceAddressRate30Min_Type()
)
cgdSourceAddressRate30Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdSourceAddressRate30Min.setStatus("current")
if mibBuilder.loadTexts:
    cgdSourceAddressRate30Min.setUnits("hits per second")
_CgdSourceAddressRate4Hr_Type = Gauge32
_CgdSourceAddressRate4Hr_Object = MibTableColumn
cgdSourceAddressRate4Hr = _CgdSourceAddressRate4Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 2, 1, 10),
    _CgdSourceAddressRate4Hr_Type()
)
cgdSourceAddressRate4Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdSourceAddressRate4Hr.setStatus("current")
if mibBuilder.loadTexts:
    cgdSourceAddressRate4Hr.setUnits("hits per second")


class _CgdSourceAddressStorageType_Type(StorageType):
    """Custom type cgdSourceAddressStorageType based on StorageType"""


_CgdSourceAddressStorageType_Object = MibTableColumn
cgdSourceAddressStorageType = _CgdSourceAddressStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 2, 1, 11),
    _CgdSourceAddressStorageType_Type()
)
cgdSourceAddressStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdSourceAddressStorageType.setStatus("current")
_CgdSourceAddressRowStatus_Type = RowStatus
_CgdSourceAddressRowStatus_Object = MibTableColumn
cgdSourceAddressRowStatus = _CgdSourceAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 7, 2, 1, 12),
    _CgdSourceAddressRowStatus_Type()
)
cgdSourceAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdSourceAddressRowStatus.setStatus("current")
_CgdDnsRule_ObjectIdentity = ObjectIdentity
cgdDnsRule = _CgdDnsRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8)
)
_CgdClauseTable_Object = MibTable
cgdClauseTable = _CgdClauseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cgdClauseTable.setStatus("current")
_CgdClauseEntry_Object = MibTableRow
cgdClauseEntry = _CgdClauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 1, 1)
)
cgdClauseEntry.setIndexNames(
    (0, "CISCO-GSLB-DNS-MIB", "cgdClauseId"),
)
if mibBuilder.loadTexts:
    cgdClauseEntry.setStatus("current")


class _CgdClauseId_Type(Unsigned32):
    """Custom type cgdClauseId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CgdClauseId_Type.__name__ = "Unsigned32"
_CgdClauseId_Object = MibTableColumn
cgdClauseId = _CgdClauseId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 1, 1, 1),
    _CgdClauseId_Type()
)
cgdClauseId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgdClauseId.setStatus("current")
_CgdClauseAnsGrpName_Type = SnmpAdminString
_CgdClauseAnsGrpName_Object = MibTableColumn
cgdClauseAnsGrpName = _CgdClauseAnsGrpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 1, 1, 2),
    _CgdClauseAnsGrpName_Type()
)
cgdClauseAnsGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdClauseAnsGrpName.setStatus("current")
_CgdClauseBalanceMethod_Type = CiscoGslbBalanceMethod
_CgdClauseBalanceMethod_Object = MibTableColumn
cgdClauseBalanceMethod = _CgdClauseBalanceMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 1, 1, 3),
    _CgdClauseBalanceMethod_Type()
)
cgdClauseBalanceMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdClauseBalanceMethod.setStatus("current")
_CgdClauseHits_Type = Counter32
_CgdClauseHits_Object = MibTableColumn
cgdClauseHits = _CgdClauseHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 1, 1, 4),
    _CgdClauseHits_Type()
)
cgdClauseHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdClauseHits.setStatus("current")
if mibBuilder.loadTexts:
    cgdClauseHits.setUnits("number of hits")
_CgdClauseStorageType_Type = StorageType
_CgdClauseStorageType_Object = MibTableColumn
cgdClauseStorageType = _CgdClauseStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 1, 1, 5),
    _CgdClauseStorageType_Type()
)
cgdClauseStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdClauseStorageType.setStatus("current")
_CgdClauseRowStatus_Type = RowStatus
_CgdClauseRowStatus_Object = MibTableColumn
cgdClauseRowStatus = _CgdClauseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 1, 1, 6),
    _CgdClauseRowStatus_Type()
)
cgdClauseRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdClauseRowStatus.setStatus("current")
_CgdDnsRuleTable_Object = MibTable
cgdDnsRuleTable = _CgdDnsRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 2)
)
if mibBuilder.loadTexts:
    cgdDnsRuleTable.setStatus("current")
_CgdDnsRuleEntry_Object = MibTableRow
cgdDnsRuleEntry = _CgdDnsRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 2, 1)
)
cgdDnsRuleEntry.setIndexNames(
    (0, "CISCO-GSLB-DNS-MIB", "cgdDnsRuleName"),
)
if mibBuilder.loadTexts:
    cgdDnsRuleEntry.setStatus("current")


class _CgdDnsRuleName_Type(SnmpAdminString):
    """Custom type cgdDnsRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CgdDnsRuleName_Type.__name__ = "SnmpAdminString"
_CgdDnsRuleName_Object = MibTableColumn
cgdDnsRuleName = _CgdDnsRuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 2, 1, 1),
    _CgdDnsRuleName_Type()
)
cgdDnsRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgdDnsRuleName.setStatus("current")
_CgdFirstClauseId_Type = Unsigned32
_CgdFirstClauseId_Object = MibTableColumn
cgdFirstClauseId = _CgdFirstClauseId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 2, 1, 2),
    _CgdFirstClauseId_Type()
)
cgdFirstClauseId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdFirstClauseId.setStatus("current")
_CgdSecondClauseId_Type = Unsigned32
_CgdSecondClauseId_Object = MibTableColumn
cgdSecondClauseId = _CgdSecondClauseId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 2, 1, 3),
    _CgdSecondClauseId_Type()
)
cgdSecondClauseId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdSecondClauseId.setStatus("current")
_CgdThirdClauseId_Type = Unsigned32
_CgdThirdClauseId_Object = MibTableColumn
cgdThirdClauseId = _CgdThirdClauseId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 2, 1, 4),
    _CgdThirdClauseId_Type()
)
cgdThirdClauseId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdThirdClauseId.setStatus("current")
_CgdSourceAddList_Type = SnmpAdminString
_CgdSourceAddList_Object = MibTableColumn
cgdSourceAddList = _CgdSourceAddList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 2, 1, 5),
    _CgdSourceAddList_Type()
)
cgdSourceAddList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdSourceAddList.setStatus("current")
_CgdDNSRuleDomainList_Type = SnmpAdminString
_CgdDNSRuleDomainList_Object = MibTableColumn
cgdDNSRuleDomainList = _CgdDNSRuleDomainList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 2, 1, 6),
    _CgdDNSRuleDomainList_Type()
)
cgdDNSRuleDomainList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdDNSRuleDomainList.setStatus("current")
_CgdDnsRuleHits_Type = Counter32
_CgdDnsRuleHits_Object = MibTableColumn
cgdDnsRuleHits = _CgdDnsRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 2, 1, 7),
    _CgdDnsRuleHits_Type()
)
cgdDnsRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDnsRuleHits.setStatus("current")
if mibBuilder.loadTexts:
    cgdDnsRuleHits.setUnits("number of hits")
_CgdDnsRuleSuccesses_Type = Counter32
_CgdDnsRuleSuccesses_Object = MibTableColumn
cgdDnsRuleSuccesses = _CgdDnsRuleSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 2, 1, 8),
    _CgdDnsRuleSuccesses_Type()
)
cgdDnsRuleSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgdDnsRuleSuccesses.setStatus("current")
if mibBuilder.loadTexts:
    cgdDnsRuleSuccesses.setUnits("number of hits")


class _CgdDnsRuleStorageType_Type(StorageType):
    """Custom type cgdDnsRuleStorageType based on StorageType"""


_CgdDnsRuleStorageType_Object = MibTableColumn
cgdDnsRuleStorageType = _CgdDnsRuleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 2, 1, 9),
    _CgdDnsRuleStorageType_Type()
)
cgdDnsRuleStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdDnsRuleStorageType.setStatus("current")
_CgdDnsRuleRowStatus_Type = RowStatus
_CgdDnsRuleRowStatus_Object = MibTableColumn
cgdDnsRuleRowStatus = _CgdDnsRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 1, 8, 2, 1, 10),
    _CgdDnsRuleRowStatus_Type()
)
cgdDnsRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgdDnsRuleRowStatus.setStatus("current")
_CiscoGslbDnsMIBConform_ObjectIdentity = ObjectIdentity
ciscoGslbDnsMIBConform = _CiscoGslbDnsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 2)
)
_CiscoGslbDnsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoGslbDnsMIBCompliances = _CiscoGslbDnsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 2, 1)
)
_CiscoGslbDnsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoGslbDnsMIBGroups = _CiscoGslbDnsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 2, 2)
)

# Managed Objects groups

ciscoGslbDnsGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 2, 2, 1)
)
ciscoGslbDnsGlobalGroup.setObjects(
      *(("CISCO-GSLB-DNS-MIB", "cgdTotalDomains"),
        ("CISCO-GSLB-DNS-MIB", "cgdTotalDomainLists"),
        ("CISCO-GSLB-DNS-MIB", "cgdTotalSourceAddresses"),
        ("CISCO-GSLB-DNS-MIB", "cgdTotalSourceAddressLists"),
        ("CISCO-GSLB-DNS-MIB", "cgdTotalAnswers"),
        ("CISCO-GSLB-DNS-MIB", "cgdTotalAnswerGroups"),
        ("CISCO-GSLB-DNS-MIB", "cgdTotalRules"))
)
if mibBuilder.loadTexts:
    ciscoGslbDnsGlobalGroup.setStatus("current")

ciscoGslbDnsGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 2, 2, 2)
)
ciscoGslbDnsGlobalStatsGroup.setObjects(
      *(("CISCO-GSLB-DNS-MIB", "cgdDnsRcvdQueries"),
        ("CISCO-GSLB-DNS-MIB", "cgdDnsRcvdHostAddrQueries"),
        ("CISCO-GSLB-DNS-MIB", "cgdDnsUnmatchedQueries"),
        ("CISCO-GSLB-DNS-MIB", "cgdDnsDroppedQueries"),
        ("CISCO-GSLB-DNS-MIB", "cgdNSFwdSentQueries"),
        ("CISCO-GSLB-DNS-MIB", "cgdNSFwdRcvdResps"),
        ("CISCO-GSLB-DNS-MIB", "cgdBoomServSentReqs"),
        ("CISCO-GSLB-DNS-MIB", "cgdProxLkupSentReqs"),
        ("CISCO-GSLB-DNS-MIB", "cgdProxLkupRcvdResps"),
        ("CISCO-GSLB-DNS-MIB", "cgdDnsQueryRateCurrent"),
        ("CISCO-GSLB-DNS-MIB", "cgdDnsQueryRatePeak"),
        ("CISCO-GSLB-DNS-MIB", "cgdDnsUdpSrcPortErrs"),
        ("CISCO-GSLB-DNS-MIB", "cgdDnsTcpSrcPortErrs"),
        ("CISCO-GSLB-DNS-MIB", "cgdDnsPollSockErrs"))
)
if mibBuilder.loadTexts:
    ciscoGslbDnsGlobalStatsGroup.setStatus("current")

ciscoGslbDnsAnswerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 2, 2, 3)
)
ciscoGslbDnsAnswerGroup.setObjects(
      *(("CISCO-GSLB-DNS-MIB", "cgdAnswerGroupType"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerGroupHits"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerGroupStorageType"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerGroupRowStatus"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerType"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerAddressType"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerAddress"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerName"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerGrpName"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerAdminState"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerStatus"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerHits"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerRate1Min"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerRate5Min"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerRate30Min"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerRate4Hr"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerStorageType"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGslbDnsAnswerGroup.setStatus("current")

ciscoGslbDnsDomainGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 2, 2, 4)
)
ciscoGslbDnsDomainGroup.setObjects(
      *(("CISCO-GSLB-DNS-MIB", "cgdDomainListHits"),
        ("CISCO-GSLB-DNS-MIB", "cgdDomainListStorageType"),
        ("CISCO-GSLB-DNS-MIB", "cgdDomainListRowStatus"),
        ("CISCO-GSLB-DNS-MIB", "cgdDomainName"),
        ("CISCO-GSLB-DNS-MIB", "cgdDomainList"),
        ("CISCO-GSLB-DNS-MIB", "cgdDomainHits"),
        ("CISCO-GSLB-DNS-MIB", "cgdDomainRate1Min"),
        ("CISCO-GSLB-DNS-MIB", "cgdDomainRate5Min"),
        ("CISCO-GSLB-DNS-MIB", "cgdDomainRate30Min"),
        ("CISCO-GSLB-DNS-MIB", "cgdDomainRate4Hr"),
        ("CISCO-GSLB-DNS-MIB", "cgdDomainStorageType"),
        ("CISCO-GSLB-DNS-MIB", "cgdDomainRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGslbDnsDomainGroup.setStatus("current")

ciscoGslbDnsSourceAddGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 2, 2, 5)
)
ciscoGslbDnsSourceAddGroup.setObjects(
      *(("CISCO-GSLB-DNS-MIB", "cgdSourceAddressListHits"),
        ("CISCO-GSLB-DNS-MIB", "cgdSourceAddressListStorageType"),
        ("CISCO-GSLB-DNS-MIB", "cgdSourceAddressListRowStatus"),
        ("CISCO-GSLB-DNS-MIB", "cgdSourceAddressAddressType"),
        ("CISCO-GSLB-DNS-MIB", "cgdSourceAddressAddress"),
        ("CISCO-GSLB-DNS-MIB", "cgdSourceAddressPrefixLength"),
        ("CISCO-GSLB-DNS-MIB", "cgdSourceAddressList"),
        ("CISCO-GSLB-DNS-MIB", "cgdSourceAddressHits"),
        ("CISCO-GSLB-DNS-MIB", "cgdSourceAddressRate1Min"),
        ("CISCO-GSLB-DNS-MIB", "cgdSourceAddressRate5Min"),
        ("CISCO-GSLB-DNS-MIB", "cgdSourceAddressRate30Min"),
        ("CISCO-GSLB-DNS-MIB", "cgdSourceAddressRate4Hr"),
        ("CISCO-GSLB-DNS-MIB", "cgdSourceAddressStorageType"),
        ("CISCO-GSLB-DNS-MIB", "cgdSourceAddressRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGslbDnsSourceAddGroup.setStatus("current")

ciscoGslbDnsRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 2, 2, 6)
)
ciscoGslbDnsRuleGroup.setObjects(
      *(("CISCO-GSLB-DNS-MIB", "cgdFirstClauseId"),
        ("CISCO-GSLB-DNS-MIB", "cgdSecondClauseId"),
        ("CISCO-GSLB-DNS-MIB", "cgdThirdClauseId"),
        ("CISCO-GSLB-DNS-MIB", "cgdSourceAddList"),
        ("CISCO-GSLB-DNS-MIB", "cgdDNSRuleDomainList"),
        ("CISCO-GSLB-DNS-MIB", "cgdDnsRuleHits"),
        ("CISCO-GSLB-DNS-MIB", "cgdDnsRuleSuccesses"),
        ("CISCO-GSLB-DNS-MIB", "cgdDnsRuleStorageType"),
        ("CISCO-GSLB-DNS-MIB", "cgdDnsRuleRowStatus"),
        ("CISCO-GSLB-DNS-MIB", "cgdClauseAnsGrpName"),
        ("CISCO-GSLB-DNS-MIB", "cgdClauseBalanceMethod"),
        ("CISCO-GSLB-DNS-MIB", "cgdClauseHits"),
        ("CISCO-GSLB-DNS-MIB", "cgdClauseStorageType"),
        ("CISCO-GSLB-DNS-MIB", "cgdClauseRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGslbDnsRuleGroup.setStatus("current")

ciscoGslbDnsNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 2, 2, 7)
)
ciscoGslbDnsNotifControlGroup.setObjects(
      *(("CISCO-GSLB-DNS-MIB", "cgdDnsClauseNotifEnable"),
        ("CISCO-GSLB-DNS-MIB", "cgdDnsAnswerNotifEnable"))
)
if mibBuilder.loadTexts:
    ciscoGslbDnsNotifControlGroup.setStatus("current")

ciscoGslbDnsNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 2, 2, 8)
)
ciscoGslbDnsNotifObjectsGroup.setObjects(
    ("CISCO-GSLB-DNS-MIB", "cgdAnswerPrevStatus")
)
if mibBuilder.loadTexts:
    ciscoGslbDnsNotifObjectsGroup.setStatus("current")

ciscoGslbDnsGlobalRateLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 2, 2, 10)
)
ciscoGslbDnsGlobalRateLimitGroup.setObjects(
      *(("CISCO-GSLB-DNS-MIB", "cgdAnsTrapRateLimit"),
        ("CISCO-GSLB-DNS-MIB", "cgdDnsClauseTrapRateLimit"))
)
if mibBuilder.loadTexts:
    ciscoGslbDnsGlobalRateLimitGroup.setStatus("current")

ciscoGslbDnsGlobalNotifStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 2, 2, 11)
)
ciscoGslbDnsGlobalNotifStatsGroup.setObjects(
      *(("CISCO-GSLB-DNS-MIB", "cgdDroppedAnsNotifs"),
        ("CISCO-GSLB-DNS-MIB", "cgdDroppedDnsClauseNotifs"))
)
if mibBuilder.loadTexts:
    ciscoGslbDnsGlobalNotifStatsGroup.setStatus("current")


# Notification objects

ciscoGslbDnsEventClause = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 0, 1)
)
ciscoGslbDnsEventClause.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CISCO-GSLB-DNS-MIB", "cgdFirstClauseId"),
        ("CISCO-GSLB-DNS-MIB", "cgdSecondClauseId"),
        ("CISCO-GSLB-DNS-MIB", "cgdDroppedDnsClauseNotifs"))
)
if mibBuilder.loadTexts:
    ciscoGslbDnsEventClause.setStatus(
        "current"
    )

ciscoGslbAnswerEventStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 0, 2)
)
ciscoGslbAnswerEventStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerName"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerType"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerAddressType"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerAddress"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerStatus"),
        ("CISCO-GSLB-DNS-MIB", "cgdAnswerPrevStatus"),
        ("CISCO-GSLB-DNS-MIB", "cgdDroppedAnsNotifs"))
)
if mibBuilder.loadTexts:
    ciscoGslbAnswerEventStatusChange.setStatus(
        "current"
    )


# Notifications groups

ciscoGslbDnsNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 2, 2, 9)
)
ciscoGslbDnsNotifGroup.setObjects(
      *(("CISCO-GSLB-DNS-MIB", "ciscoGslbDnsEventClause"),
        ("CISCO-GSLB-DNS-MIB", "ciscoGslbAnswerEventStatusChange"))
)
if mibBuilder.loadTexts:
    ciscoGslbDnsNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoGslbDnsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 595, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoGslbDnsMIBCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GSLB-DNS-MIB",
    **{"ciscoGslbDnsMIB": ciscoGslbDnsMIB,
       "ciscoGslbDnsMIBNotifs": ciscoGslbDnsMIBNotifs,
       "ciscoGslbDnsEventClause": ciscoGslbDnsEventClause,
       "ciscoGslbAnswerEventStatusChange": ciscoGslbAnswerEventStatusChange,
       "ciscoGslbDnsMIBObjects": ciscoGslbDnsMIBObjects,
       "cgdNotifControl": cgdNotifControl,
       "cgdDnsClauseNotifEnable": cgdDnsClauseNotifEnable,
       "cgdDnsAnswerNotifEnable": cgdDnsAnswerNotifEnable,
       "cgdNotifObjects": cgdNotifObjects,
       "cgdAnswerPrevStatus": cgdAnswerPrevStatus,
       "cgdGlobal": cgdGlobal,
       "cgdTotalDomains": cgdTotalDomains,
       "cgdTotalDomainLists": cgdTotalDomainLists,
       "cgdTotalSourceAddresses": cgdTotalSourceAddresses,
       "cgdTotalSourceAddressLists": cgdTotalSourceAddressLists,
       "cgdTotalAnswers": cgdTotalAnswers,
       "cgdTotalAnswerGroups": cgdTotalAnswerGroups,
       "cgdTotalRules": cgdTotalRules,
       "cgdAnsTrapRateLimit": cgdAnsTrapRateLimit,
       "cgdDnsClauseTrapRateLimit": cgdDnsClauseTrapRateLimit,
       "cgdGlobalStats": cgdGlobalStats,
       "cgdDnsRcvdQueries": cgdDnsRcvdQueries,
       "cgdDnsRcvdHostAddrQueries": cgdDnsRcvdHostAddrQueries,
       "cgdDnsUnmatchedQueries": cgdDnsUnmatchedQueries,
       "cgdDnsDroppedQueries": cgdDnsDroppedQueries,
       "cgdNSFwdSentQueries": cgdNSFwdSentQueries,
       "cgdNSFwdRcvdResps": cgdNSFwdRcvdResps,
       "cgdBoomServSentReqs": cgdBoomServSentReqs,
       "cgdProxLkupSentReqs": cgdProxLkupSentReqs,
       "cgdProxLkupRcvdResps": cgdProxLkupRcvdResps,
       "cgdDnsQueryRateCurrent": cgdDnsQueryRateCurrent,
       "cgdDnsQueryRatePeak": cgdDnsQueryRatePeak,
       "cgdDnsUdpSrcPortErrs": cgdDnsUdpSrcPortErrs,
       "cgdDnsTcpSrcPortErrs": cgdDnsTcpSrcPortErrs,
       "cgdDnsPollSockErrs": cgdDnsPollSockErrs,
       "cgdDroppedAnsNotifs": cgdDroppedAnsNotifs,
       "cgdDroppedDnsClauseNotifs": cgdDroppedDnsClauseNotifs,
       "cgdAnswer": cgdAnswer,
       "cgdAnswerGroupTable": cgdAnswerGroupTable,
       "cgdAnswerGroupEntry": cgdAnswerGroupEntry,
       "cgdAnswerGroupName": cgdAnswerGroupName,
       "cgdAnswerGroupType": cgdAnswerGroupType,
       "cgdAnswerGroupHits": cgdAnswerGroupHits,
       "cgdAnswerGroupStorageType": cgdAnswerGroupStorageType,
       "cgdAnswerGroupRowStatus": cgdAnswerGroupRowStatus,
       "cgdAnswerTable": cgdAnswerTable,
       "cgdAnswerEntry": cgdAnswerEntry,
       "cgdAnswerId": cgdAnswerId,
       "cgdAnswerType": cgdAnswerType,
       "cgdAnswerAddressType": cgdAnswerAddressType,
       "cgdAnswerAddress": cgdAnswerAddress,
       "cgdAnswerName": cgdAnswerName,
       "cgdAnswerGrpName": cgdAnswerGrpName,
       "cgdAnswerAdminState": cgdAnswerAdminState,
       "cgdAnswerStatus": cgdAnswerStatus,
       "cgdAnswerHits": cgdAnswerHits,
       "cgdAnswerRate1Min": cgdAnswerRate1Min,
       "cgdAnswerRate5Min": cgdAnswerRate5Min,
       "cgdAnswerRate30Min": cgdAnswerRate30Min,
       "cgdAnswerRate4Hr": cgdAnswerRate4Hr,
       "cgdAnswerStorageType": cgdAnswerStorageType,
       "cgdAnswerRowStatus": cgdAnswerRowStatus,
       "cgdDomain": cgdDomain,
       "cgdDomainListTable": cgdDomainListTable,
       "cgdDomainListEntry": cgdDomainListEntry,
       "cgdDomainListName": cgdDomainListName,
       "cgdDomainListHits": cgdDomainListHits,
       "cgdDomainListStorageType": cgdDomainListStorageType,
       "cgdDomainListRowStatus": cgdDomainListRowStatus,
       "cgdDomainTable": cgdDomainTable,
       "cgdDomainEntry": cgdDomainEntry,
       "cgdDomainId": cgdDomainId,
       "cgdDomainName": cgdDomainName,
       "cgdDomainList": cgdDomainList,
       "cgdDomainHits": cgdDomainHits,
       "cgdDomainRate1Min": cgdDomainRate1Min,
       "cgdDomainRate5Min": cgdDomainRate5Min,
       "cgdDomainRate30Min": cgdDomainRate30Min,
       "cgdDomainRate4Hr": cgdDomainRate4Hr,
       "cgdDomainStorageType": cgdDomainStorageType,
       "cgdDomainRowStatus": cgdDomainRowStatus,
       "cgdSourceAdd": cgdSourceAdd,
       "cgdSourceAddressListTable": cgdSourceAddressListTable,
       "cgdSourceAddressListEntry": cgdSourceAddressListEntry,
       "cgdSourceAddressListName": cgdSourceAddressListName,
       "cgdSourceAddressListHits": cgdSourceAddressListHits,
       "cgdSourceAddressListStorageType": cgdSourceAddressListStorageType,
       "cgdSourceAddressListRowStatus": cgdSourceAddressListRowStatus,
       "cgdSourceAddressTable": cgdSourceAddressTable,
       "cgdSourceAddressEntry": cgdSourceAddressEntry,
       "cgdSourceAddressId": cgdSourceAddressId,
       "cgdSourceAddressAddressType": cgdSourceAddressAddressType,
       "cgdSourceAddressAddress": cgdSourceAddressAddress,
       "cgdSourceAddressPrefixLength": cgdSourceAddressPrefixLength,
       "cgdSourceAddressList": cgdSourceAddressList,
       "cgdSourceAddressHits": cgdSourceAddressHits,
       "cgdSourceAddressRate1Min": cgdSourceAddressRate1Min,
       "cgdSourceAddressRate5Min": cgdSourceAddressRate5Min,
       "cgdSourceAddressRate30Min": cgdSourceAddressRate30Min,
       "cgdSourceAddressRate4Hr": cgdSourceAddressRate4Hr,
       "cgdSourceAddressStorageType": cgdSourceAddressStorageType,
       "cgdSourceAddressRowStatus": cgdSourceAddressRowStatus,
       "cgdDnsRule": cgdDnsRule,
       "cgdClauseTable": cgdClauseTable,
       "cgdClauseEntry": cgdClauseEntry,
       "cgdClauseId": cgdClauseId,
       "cgdClauseAnsGrpName": cgdClauseAnsGrpName,
       "cgdClauseBalanceMethod": cgdClauseBalanceMethod,
       "cgdClauseHits": cgdClauseHits,
       "cgdClauseStorageType": cgdClauseStorageType,
       "cgdClauseRowStatus": cgdClauseRowStatus,
       "cgdDnsRuleTable": cgdDnsRuleTable,
       "cgdDnsRuleEntry": cgdDnsRuleEntry,
       "cgdDnsRuleName": cgdDnsRuleName,
       "cgdFirstClauseId": cgdFirstClauseId,
       "cgdSecondClauseId": cgdSecondClauseId,
       "cgdThirdClauseId": cgdThirdClauseId,
       "cgdSourceAddList": cgdSourceAddList,
       "cgdDNSRuleDomainList": cgdDNSRuleDomainList,
       "cgdDnsRuleHits": cgdDnsRuleHits,
       "cgdDnsRuleSuccesses": cgdDnsRuleSuccesses,
       "cgdDnsRuleStorageType": cgdDnsRuleStorageType,
       "cgdDnsRuleRowStatus": cgdDnsRuleRowStatus,
       "ciscoGslbDnsMIBConform": ciscoGslbDnsMIBConform,
       "ciscoGslbDnsMIBCompliances": ciscoGslbDnsMIBCompliances,
       "ciscoGslbDnsMIBCompliance": ciscoGslbDnsMIBCompliance,
       "ciscoGslbDnsMIBGroups": ciscoGslbDnsMIBGroups,
       "ciscoGslbDnsGlobalGroup": ciscoGslbDnsGlobalGroup,
       "ciscoGslbDnsGlobalStatsGroup": ciscoGslbDnsGlobalStatsGroup,
       "ciscoGslbDnsAnswerGroup": ciscoGslbDnsAnswerGroup,
       "ciscoGslbDnsDomainGroup": ciscoGslbDnsDomainGroup,
       "ciscoGslbDnsSourceAddGroup": ciscoGslbDnsSourceAddGroup,
       "ciscoGslbDnsRuleGroup": ciscoGslbDnsRuleGroup,
       "ciscoGslbDnsNotifControlGroup": ciscoGslbDnsNotifControlGroup,
       "ciscoGslbDnsNotifObjectsGroup": ciscoGslbDnsNotifObjectsGroup,
       "ciscoGslbDnsNotifGroup": ciscoGslbDnsNotifGroup,
       "ciscoGslbDnsGlobalRateLimitGroup": ciscoGslbDnsGlobalRateLimitGroup,
       "ciscoGslbDnsGlobalNotifStatsGroup": ciscoGslbDnsGlobalNotifStatsGroup}
)
