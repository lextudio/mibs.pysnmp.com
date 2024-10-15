# SNMP MIB module (CISCO-CDMA-PDSN-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CDMA-PDSN-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:12 2024
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

(cCdmaPcfSoPppSetupStatsEntry,
 cCdmaPcfSoRpRegStatsEntry,
 cCdmaServingPdsnHostname) = mibBuilder.importSymbols(
    "CISCO-CDMA-PDSN-MIB",
    "cCdmaPcfSoPppSetupStatsEntry",
    "cCdmaPcfSoRpRegStatsEntry",
    "cCdmaServingPdsnHostname")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCdmaPdsnExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669)
)
ciscoCdmaPdsnExtMIB.setRevisions(
        ("2010-07-20 00:00",
         "2010-06-08 00:00",
         "2009-09-17 00:00",
         "2008-08-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCdmaPdsnExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCdmaPdsnExtMIBNotifs = _CiscoCdmaPdsnExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 0)
)
_CiscoCdmaPdsnExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCdmaPdsnExtMIBObjects = _CiscoCdmaPdsnExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1)
)
_CcpCdmaExtSystemInfo_ObjectIdentity = ObjectIdentity
ccpCdmaExtSystemInfo = _CcpCdmaExtSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 1)
)
_CcpCdmaExtTotalBandwidth_Type = Gauge32
_CcpCdmaExtTotalBandwidth_Object = MibScalar
ccpCdmaExtTotalBandwidth = _CcpCdmaExtTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 1, 1),
    _CcpCdmaExtTotalBandwidth_Type()
)
ccpCdmaExtTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtTotalBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtTotalBandwidth.setUnits("bits/sec")
_CcpCdmaExtAvailableBandwidth_Type = Gauge32
_CcpCdmaExtAvailableBandwidth_Object = MibScalar
ccpCdmaExtAvailableBandwidth = _CcpCdmaExtAvailableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 1, 2),
    _CcpCdmaExtAvailableBandwidth_Type()
)
ccpCdmaExtAvailableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtAvailableBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtAvailableBandwidth.setUnits("bits/sec")
_CcpCdmaExtAllocatedBandwidth_Type = Gauge32
_CcpCdmaExtAllocatedBandwidth_Object = MibScalar
ccpCdmaExtAllocatedBandwidth = _CcpCdmaExtAllocatedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 1, 3),
    _CcpCdmaExtAllocatedBandwidth_Type()
)
ccpCdmaExtAllocatedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtAllocatedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtAllocatedBandwidth.setUnits("bits/sec")
_CcpCdmaExtSessionAuxConnectionsEnabled_Type = TruthValue
_CcpCdmaExtSessionAuxConnectionsEnabled_Object = MibScalar
ccpCdmaExtSessionAuxConnectionsEnabled = _CcpCdmaExtSessionAuxConnectionsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 1, 4),
    _CcpCdmaExtSessionAuxConnectionsEnabled_Type()
)
ccpCdmaExtSessionAuxConnectionsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccpCdmaExtSessionAuxConnectionsEnabled.setStatus("current")
_CcpCdmaExtSessionMaxAuxConnectionsAllowed_Type = Unsigned32
_CcpCdmaExtSessionMaxAuxConnectionsAllowed_Object = MibScalar
ccpCdmaExtSessionMaxAuxConnectionsAllowed = _CcpCdmaExtSessionMaxAuxConnectionsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 1, 5),
    _CcpCdmaExtSessionMaxAuxConnectionsAllowed_Type()
)
ccpCdmaExtSessionMaxAuxConnectionsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtSessionMaxAuxConnectionsAllowed.setStatus("current")
_CcpCdmaExtSessionAuxConnectionsTotal_Type = Gauge32
_CcpCdmaExtSessionAuxConnectionsTotal_Object = MibScalar
ccpCdmaExtSessionAuxConnectionsTotal = _CcpCdmaExtSessionAuxConnectionsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 1, 6),
    _CcpCdmaExtSessionAuxConnectionsTotal_Type()
)
ccpCdmaExtSessionAuxConnectionsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtSessionAuxConnectionsTotal.setStatus("current")
_CcpCdmaExtPolicingEnabled_Type = TruthValue
_CcpCdmaExtPolicingEnabled_Object = MibScalar
ccpCdmaExtPolicingEnabled = _CcpCdmaExtPolicingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 1, 7),
    _CcpCdmaExtPolicingEnabled_Type()
)
ccpCdmaExtPolicingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccpCdmaExtPolicingEnabled.setStatus("current")
_CcpCdmaExtAuxSessionTotal_Type = Gauge32
_CcpCdmaExtAuxSessionTotal_Object = MibScalar
ccpCdmaExtAuxSessionTotal = _CcpCdmaExtAuxSessionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 1, 8),
    _CcpCdmaExtAuxSessionTotal_Type()
)
ccpCdmaExtAuxSessionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtAuxSessionTotal.setStatus("current")
_CcpCdmaExtPolicingSessionTotal_Type = Gauge32
_CcpCdmaExtPolicingSessionTotal_Object = MibScalar
ccpCdmaExtPolicingSessionTotal = _CcpCdmaExtPolicingSessionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 1, 9),
    _CcpCdmaExtPolicingSessionTotal_Type()
)
ccpCdmaExtPolicingSessionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPolicingSessionTotal.setStatus("current")
_CcpCdmaExtDscpSession_Type = Gauge32
_CcpCdmaExtDscpSession_Object = MibScalar
ccpCdmaExtDscpSession = _CcpCdmaExtDscpSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 1, 10),
    _CcpCdmaExtDscpSession_Type()
)
ccpCdmaExtDscpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtDscpSession.setStatus("current")


class _CcpCdmaExtLoadHighReachedNotifEnabled_Type(TruthValue):
    """Custom type ccpCdmaExtLoadHighReachedNotifEnabled based on TruthValue"""


_CcpCdmaExtLoadHighReachedNotifEnabled_Object = MibScalar
ccpCdmaExtLoadHighReachedNotifEnabled = _CcpCdmaExtLoadHighReachedNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 1, 11),
    _CcpCdmaExtLoadHighReachedNotifEnabled_Type()
)
ccpCdmaExtLoadHighReachedNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccpCdmaExtLoadHighReachedNotifEnabled.setStatus("current")
_CcpCdmaExtCacEnabled_Type = TruthValue
_CcpCdmaExtCacEnabled_Object = MibScalar
ccpCdmaExtCacEnabled = _CcpCdmaExtCacEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 1, 12),
    _CcpCdmaExtCacEnabled_Type()
)
ccpCdmaExtCacEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccpCdmaExtCacEnabled.setStatus("current")


class _CcpCdmaExtRohcEnabled_Type(TruthValue):
    """Custom type ccpCdmaExtRohcEnabled based on TruthValue"""


_CcpCdmaExtRohcEnabled_Object = MibScalar
ccpCdmaExtRohcEnabled = _CcpCdmaExtRohcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 1, 13),
    _CcpCdmaExtRohcEnabled_Type()
)
ccpCdmaExtRohcEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcEnabled.setStatus("current")
_CcpCdmaExtRohcAuxA10sCount_Type = Gauge32
_CcpCdmaExtRohcAuxA10sCount_Object = MibScalar
ccpCdmaExtRohcAuxA10sCount = _CcpCdmaExtRohcAuxA10sCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 1, 14),
    _CcpCdmaExtRohcAuxA10sCount_Type()
)
ccpCdmaExtRohcAuxA10sCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcAuxA10sCount.setStatus("current")
_CcpCdmaExtPerformanceStats_ObjectIdentity = ObjectIdentity
ccpCdmaExtPerformanceStats = _CcpCdmaExtPerformanceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2)
)
_CcpCdmaExtRsvpStats_ObjectIdentity = ObjectIdentity
ccpCdmaExtRsvpStats = _CcpCdmaExtRsvpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 1)
)
_CcpCdmaExtRsvpCreationSuccessTfts_Type = Counter32
_CcpCdmaExtRsvpCreationSuccessTfts_Object = MibScalar
ccpCdmaExtRsvpCreationSuccessTfts = _CcpCdmaExtRsvpCreationSuccessTfts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 1, 1),
    _CcpCdmaExtRsvpCreationSuccessTfts_Type()
)
ccpCdmaExtRsvpCreationSuccessTfts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpCreationSuccessTfts.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpCreationSuccessTfts.setUnits("passes")
_CcpCdmaExtRsvpCreationFailureTfts_Type = Counter32
_CcpCdmaExtRsvpCreationFailureTfts_Object = MibScalar
ccpCdmaExtRsvpCreationFailureTfts = _CcpCdmaExtRsvpCreationFailureTfts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 1, 2),
    _CcpCdmaExtRsvpCreationFailureTfts_Type()
)
ccpCdmaExtRsvpCreationFailureTfts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpCreationFailureTfts.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpCreationFailureTfts.setUnits("failures")
_CcpCdmaExtRsvpPacketFilterAddFailureTfts_Type = Counter32
_CcpCdmaExtRsvpPacketFilterAddFailureTfts_Object = MibScalar
ccpCdmaExtRsvpPacketFilterAddFailureTfts = _CcpCdmaExtRsvpPacketFilterAddFailureTfts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 1, 3),
    _CcpCdmaExtRsvpPacketFilterAddFailureTfts_Type()
)
ccpCdmaExtRsvpPacketFilterAddFailureTfts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpPacketFilterAddFailureTfts.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpPacketFilterAddFailureTfts.setUnits("failures")
_CcpCdmaExtRsvpPacketFilterUnavailableTfts_Type = Counter32
_CcpCdmaExtRsvpPacketFilterUnavailableTfts_Object = MibScalar
ccpCdmaExtRsvpPacketFilterUnavailableTfts = _CcpCdmaExtRsvpPacketFilterUnavailableTfts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 1, 4),
    _CcpCdmaExtRsvpPacketFilterUnavailableTfts_Type()
)
ccpCdmaExtRsvpPacketFilterUnavailableTfts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpPacketFilterUnavailableTfts.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpPacketFilterUnavailableTfts.setUnits("failures")
_CcpCdmaExtRsvpPacketFilterReplaceFailureTfts_Type = Counter32
_CcpCdmaExtRsvpPacketFilterReplaceFailureTfts_Object = MibScalar
ccpCdmaExtRsvpPacketFilterReplaceFailureTfts = _CcpCdmaExtRsvpPacketFilterReplaceFailureTfts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 1, 5),
    _CcpCdmaExtRsvpPacketFilterReplaceFailureTfts_Type()
)
ccpCdmaExtRsvpPacketFilterReplaceFailureTfts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpPacketFilterReplaceFailureTfts.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpPacketFilterReplaceFailureTfts.setUnits("failures")
_CcpCdmaExtRsvpPacketFilterAddBeforeCreationTfts_Type = Counter32
_CcpCdmaExtRsvpPacketFilterAddBeforeCreationTfts_Object = MibScalar
ccpCdmaExtRsvpPacketFilterAddBeforeCreationTfts = _CcpCdmaExtRsvpPacketFilterAddBeforeCreationTfts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 1, 6),
    _CcpCdmaExtRsvpPacketFilterAddBeforeCreationTfts_Type()
)
ccpCdmaExtRsvpPacketFilterAddBeforeCreationTfts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpPacketFilterAddBeforeCreationTfts.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpPacketFilterAddBeforeCreationTfts.setUnits("failures")
_CcpCdmaExtRsvpUnableToParseTfts_Type = Counter32
_CcpCdmaExtRsvpUnableToParseTfts_Object = MibScalar
ccpCdmaExtRsvpUnableToParseTfts = _CcpCdmaExtRsvpUnableToParseTfts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 1, 7),
    _CcpCdmaExtRsvpUnableToParseTfts_Type()
)
ccpCdmaExtRsvpUnableToParseTfts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpUnableToParseTfts.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpUnableToParseTfts.setUnits("failures")
_CcpCdmaExtRsvpPrecedenceContentionTfts_Type = Counter32
_CcpCdmaExtRsvpPrecedenceContentionTfts_Object = MibScalar
ccpCdmaExtRsvpPrecedenceContentionTfts = _CcpCdmaExtRsvpPrecedenceContentionTfts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 1, 8),
    _CcpCdmaExtRsvpPrecedenceContentionTfts_Type()
)
ccpCdmaExtRsvpPrecedenceContentionTfts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpPrecedenceContentionTfts.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpPrecedenceContentionTfts.setUnits("failures")
_CcpCdmaExtRsvpTreatmentUnsupportedTfts_Type = Counter32
_CcpCdmaExtRsvpTreatmentUnsupportedTfts_Object = MibScalar
ccpCdmaExtRsvpTreatmentUnsupportedTfts = _CcpCdmaExtRsvpTreatmentUnsupportedTfts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 1, 9),
    _CcpCdmaExtRsvpTreatmentUnsupportedTfts_Type()
)
ccpCdmaExtRsvpTreatmentUnsupportedTfts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpTreatmentUnsupportedTfts.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpTreatmentUnsupportedTfts.setUnits("failures")
_CcpCdmaExtRsvpMaxPacketFiltersReachedTfts_Type = Counter32
_CcpCdmaExtRsvpMaxPacketFiltersReachedTfts_Object = MibScalar
ccpCdmaExtRsvpMaxPacketFiltersReachedTfts = _CcpCdmaExtRsvpMaxPacketFiltersReachedTfts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 1, 10),
    _CcpCdmaExtRsvpMaxPacketFiltersReachedTfts_Type()
)
ccpCdmaExtRsvpMaxPacketFiltersReachedTfts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpMaxPacketFiltersReachedTfts.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpMaxPacketFiltersReachedTfts.setUnits("failures")
_CcpCdmaExtRsvpUnAuthorizeTfts_Type = Counter32
_CcpCdmaExtRsvpUnAuthorizeTfts_Object = MibScalar
ccpCdmaExtRsvpUnAuthorizeTfts = _CcpCdmaExtRsvpUnAuthorizeTfts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 1, 11),
    _CcpCdmaExtRsvpUnAuthorizeTfts_Type()
)
ccpCdmaExtRsvpUnAuthorizeTfts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpUnAuthorizeTfts.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRsvpUnAuthorizeTfts.setUnits("failures")
_CcpCdmaExtQosStats_ObjectIdentity = ObjectIdentity
ccpCdmaExtQosStats = _CcpCdmaExtQosStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 2)
)
_CcpCdmaExtQosSuccesses_Type = Counter32
_CcpCdmaExtQosSuccesses_Object = MibScalar
ccpCdmaExtQosSuccesses = _CcpCdmaExtQosSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 2, 1),
    _CcpCdmaExtQosSuccesses_Type()
)
ccpCdmaExtQosSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtQosSuccesses.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtQosSuccesses.setUnits("passes")
_CcpCdmaExtQosFailures_Type = Counter32
_CcpCdmaExtQosFailures_Object = MibScalar
ccpCdmaExtQosFailures = _CcpCdmaExtQosFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 2, 2),
    _CcpCdmaExtQosFailures_Type()
)
ccpCdmaExtQosFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtQosFailures.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtQosFailures.setUnits("failures")
_CcpCdmaExtQosDscpRemarkedPkts_Type = Counter32
_CcpCdmaExtQosDscpRemarkedPkts_Object = MibScalar
ccpCdmaExtQosDscpRemarkedPkts = _CcpCdmaExtQosDscpRemarkedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 2, 3),
    _CcpCdmaExtQosDscpRemarkedPkts_Type()
)
ccpCdmaExtQosDscpRemarkedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtQosDscpRemarkedPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtQosDscpRemarkedPkts.setUnits("packets")
_CcpCdmaExtBandwidthPolicyStats_ObjectIdentity = ObjectIdentity
ccpCdmaExtBandwidthPolicyStats = _CcpCdmaExtBandwidthPolicyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 3)
)
_CcpCdmaExtBandwidthPolicyInstallSuccesses_Type = Counter32
_CcpCdmaExtBandwidthPolicyInstallSuccesses_Object = MibScalar
ccpCdmaExtBandwidthPolicyInstallSuccesses = _CcpCdmaExtBandwidthPolicyInstallSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 3, 1),
    _CcpCdmaExtBandwidthPolicyInstallSuccesses_Type()
)
ccpCdmaExtBandwidthPolicyInstallSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtBandwidthPolicyInstallSuccesses.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtBandwidthPolicyInstallSuccesses.setUnits("passes")
_CcpCdmaExtBandwidthPolicyInstallFailures_Type = Counter32
_CcpCdmaExtBandwidthPolicyInstallFailures_Object = MibScalar
ccpCdmaExtBandwidthPolicyInstallFailures = _CcpCdmaExtBandwidthPolicyInstallFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 3, 2),
    _CcpCdmaExtBandwidthPolicyInstallFailures_Type()
)
ccpCdmaExtBandwidthPolicyInstallFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtBandwidthPolicyInstallFailures.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtBandwidthPolicyInstallFailures.setUnits("failures")
_CcpCdmaExtBandwidthPolicyRemoves_Type = Counter32
_CcpCdmaExtBandwidthPolicyRemoves_Object = MibScalar
ccpCdmaExtBandwidthPolicyRemoves = _CcpCdmaExtBandwidthPolicyRemoves_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 3, 3),
    _CcpCdmaExtBandwidthPolicyRemoves_Type()
)
ccpCdmaExtBandwidthPolicyRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtBandwidthPolicyRemoves.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtBandwidthPolicyRemoves.setUnits("passes")
_CcpCdmaExtRpRegStats_ObjectIdentity = ObjectIdentity
ccpCdmaExtRpRegStats = _CcpCdmaExtRpRegStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 4)
)
_CcpCdmaExtRpReRegNewAuxConnections_Type = Counter32
_CcpCdmaExtRpReRegNewAuxConnections_Object = MibScalar
ccpCdmaExtRpReRegNewAuxConnections = _CcpCdmaExtRpReRegNewAuxConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 4, 1),
    _CcpCdmaExtRpReRegNewAuxConnections_Type()
)
ccpCdmaExtRpReRegNewAuxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRpReRegNewAuxConnections.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRpReRegNewAuxConnections.setUnits("messages")
_CcpCdmaExtRpReRegCloseAuxConnections_Type = Counter32
_CcpCdmaExtRpReRegCloseAuxConnections_Object = MibScalar
ccpCdmaExtRpReRegCloseAuxConnections = _CcpCdmaExtRpReRegCloseAuxConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 4, 2),
    _CcpCdmaExtRpReRegCloseAuxConnections_Type()
)
ccpCdmaExtRpReRegCloseAuxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRpReRegCloseAuxConnections.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRpReRegCloseAuxConnections.setUnits("messages")
_CcpCdmaExtRpReRegRemapFlows_Type = Counter32
_CcpCdmaExtRpReRegRemapFlows_Object = MibScalar
ccpCdmaExtRpReRegRemapFlows = _CcpCdmaExtRpReRegRemapFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 4, 4),
    _CcpCdmaExtRpReRegRemapFlows_Type()
)
ccpCdmaExtRpReRegRemapFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRpReRegRemapFlows.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRpReRegRemapFlows.setUnits("messages")
_CcpCdmaExtRpRegNewAuxConnections_Type = Counter32
_CcpCdmaExtRpRegNewAuxConnections_Object = MibScalar
ccpCdmaExtRpRegNewAuxConnections = _CcpCdmaExtRpRegNewAuxConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 4, 5),
    _CcpCdmaExtRpRegNewAuxConnections_Type()
)
ccpCdmaExtRpRegNewAuxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRpRegNewAuxConnections.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRpRegNewAuxConnections.setUnits("messages")
_CcpCdmaExtRpSessUpdStats_ObjectIdentity = ObjectIdentity
ccpCdmaExtRpSessUpdStats = _CcpCdmaExtRpSessUpdStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 5)
)
_CcpCdmaExtRpSessionUpdSubQoses_Type = ZeroBasedCounter32
_CcpCdmaExtRpSessionUpdSubQoses_Object = MibScalar
ccpCdmaExtRpSessionUpdSubQoses = _CcpCdmaExtRpSessionUpdSubQoses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 5, 1),
    _CcpCdmaExtRpSessionUpdSubQoses_Type()
)
ccpCdmaExtRpSessionUpdSubQoses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRpSessionUpdSubQoses.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRpSessionUpdSubQoses.setUnits("messages")
_CcpCdmaExtPcfSoRpRegStats_ObjectIdentity = ObjectIdentity
ccpCdmaExtPcfSoRpRegStats = _CcpCdmaExtPcfSoRpRegStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 6)
)
_CcpCdmaExtPcfSoRpRegStatsTable_Object = MibTable
ccpCdmaExtPcfSoRpRegStatsTable = _CcpCdmaExtPcfSoRpRegStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpRegStatsTable.setStatus("current")
_CcpCdmaExtPcfSoRpRegStatsEntry_Object = MibTableRow
ccpCdmaExtPcfSoRpRegStatsEntry = _CcpCdmaExtPcfSoRpRegStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpRegStatsEntry.setStatus("current")
_CcpCdmaExtPcfSoStatsTotalAuxConnections_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoStatsTotalAuxConnections_Object = MibTableColumn
ccpCdmaExtPcfSoStatsTotalAuxConnections = _CcpCdmaExtPcfSoStatsTotalAuxConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 6, 1, 1, 1),
    _CcpCdmaExtPcfSoStatsTotalAuxConnections_Type()
)
ccpCdmaExtPcfSoStatsTotalAuxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoStatsTotalAuxConnections.setStatus("current")
_CcpCdmaExtPcfSoRpRegStatsNewAuxConnections_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoRpRegStatsNewAuxConnections_Object = MibTableColumn
ccpCdmaExtPcfSoRpRegStatsNewAuxConnections = _CcpCdmaExtPcfSoRpRegStatsNewAuxConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 6, 1, 1, 2),
    _CcpCdmaExtPcfSoRpRegStatsNewAuxConnections_Type()
)
ccpCdmaExtPcfSoRpRegStatsNewAuxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpRegStatsNewAuxConnections.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpRegStatsNewAuxConnections.setUnits("messages")
_CcpCdmaExtPcfSoRpReRegStatsNewAuxConnections_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoRpReRegStatsNewAuxConnections_Object = MibTableColumn
ccpCdmaExtPcfSoRpReRegStatsNewAuxConnections = _CcpCdmaExtPcfSoRpReRegStatsNewAuxConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 6, 1, 1, 3),
    _CcpCdmaExtPcfSoRpReRegStatsNewAuxConnections_Type()
)
ccpCdmaExtPcfSoRpReRegStatsNewAuxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpReRegStatsNewAuxConnections.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpReRegStatsNewAuxConnections.setUnits("messages")
_CcpCdmaExtPcfSoRpReRegStatsCloseAuxConnections_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoRpReRegStatsCloseAuxConnections_Object = MibTableColumn
ccpCdmaExtPcfSoRpReRegStatsCloseAuxConnections = _CcpCdmaExtPcfSoRpReRegStatsCloseAuxConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 6, 1, 1, 4),
    _CcpCdmaExtPcfSoRpReRegStatsCloseAuxConnections_Type()
)
ccpCdmaExtPcfSoRpReRegStatsCloseAuxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpReRegStatsCloseAuxConnections.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpReRegStatsCloseAuxConnections.setUnits("messages")
_CcpCdmaExtPcfSoRpReRegStatsRemapFlows_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoRpReRegStatsRemapFlows_Object = MibTableColumn
ccpCdmaExtPcfSoRpReRegStatsRemapFlows = _CcpCdmaExtPcfSoRpReRegStatsRemapFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 6, 1, 1, 5),
    _CcpCdmaExtPcfSoRpReRegStatsRemapFlows_Type()
)
ccpCdmaExtPcfSoRpReRegStatsRemapFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpReRegStatsRemapFlows.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpReRegStatsRemapFlows.setUnits("messages")
_CcpCdmaExtPcfSoRpRegStatsBwUnavailableSess_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoRpRegStatsBwUnavailableSess_Object = MibTableColumn
ccpCdmaExtPcfSoRpRegStatsBwUnavailableSess = _CcpCdmaExtPcfSoRpRegStatsBwUnavailableSess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 6, 1, 1, 6),
    _CcpCdmaExtPcfSoRpRegStatsBwUnavailableSess_Type()
)
ccpCdmaExtPcfSoRpRegStatsBwUnavailableSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpRegStatsBwUnavailableSess.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpRegStatsBwUnavailableSess.setUnits("messages")
_CcpCdmaExtPcfSoRpRegStatsSessionUpdSubQoses_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoRpRegStatsSessionUpdSubQoses_Object = MibTableColumn
ccpCdmaExtPcfSoRpRegStatsSessionUpdSubQoses = _CcpCdmaExtPcfSoRpRegStatsSessionUpdSubQoses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 6, 1, 1, 7),
    _CcpCdmaExtPcfSoRpRegStatsSessionUpdSubQoses_Type()
)
ccpCdmaExtPcfSoRpRegStatsSessionUpdSubQoses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpRegStatsSessionUpdSubQoses.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpRegStatsSessionUpdSubQoses.setUnits("messages")
_CcpCdmaExtPcfSoRpRegStatsMaxServiceFlows_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoRpRegStatsMaxServiceFlows_Object = MibTableColumn
ccpCdmaExtPcfSoRpRegStatsMaxServiceFlows = _CcpCdmaExtPcfSoRpRegStatsMaxServiceFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 6, 1, 1, 8),
    _CcpCdmaExtPcfSoRpRegStatsMaxServiceFlows_Type()
)
ccpCdmaExtPcfSoRpRegStatsMaxServiceFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpRegStatsMaxServiceFlows.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpRegStatsMaxServiceFlows.setUnits("messages")
_CcpCdmaExtPcfSoRpRegStatsUnsupportedSOs_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoRpRegStatsUnsupportedSOs_Object = MibTableColumn
ccpCdmaExtPcfSoRpRegStatsUnsupportedSOs = _CcpCdmaExtPcfSoRpRegStatsUnsupportedSOs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 6, 1, 1, 9),
    _CcpCdmaExtPcfSoRpRegStatsUnsupportedSOs_Type()
)
ccpCdmaExtPcfSoRpRegStatsUnsupportedSOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpRegStatsUnsupportedSOs.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpRegStatsUnsupportedSOs.setUnits("messages")
_CcpCdmaExtPcfSoRpRegStatsNonExistA10s_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoRpRegStatsNonExistA10s_Object = MibTableColumn
ccpCdmaExtPcfSoRpRegStatsNonExistA10s = _CcpCdmaExtPcfSoRpRegStatsNonExistA10s_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 6, 1, 1, 10),
    _CcpCdmaExtPcfSoRpRegStatsNonExistA10s_Type()
)
ccpCdmaExtPcfSoRpRegStatsNonExistA10s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpRegStatsNonExistA10s.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpRegStatsNonExistA10s.setUnits("messages")
_CcpCdmaExtPcfSoRpRegStatsNoCIDAvailable_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoRpRegStatsNoCIDAvailable_Object = MibTableColumn
ccpCdmaExtPcfSoRpRegStatsNoCIDAvailable = _CcpCdmaExtPcfSoRpRegStatsNoCIDAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 6, 1, 1, 11),
    _CcpCdmaExtPcfSoRpRegStatsNoCIDAvailable_Type()
)
ccpCdmaExtPcfSoRpRegStatsNoCIDAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpRegStatsNoCIDAvailable.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoRpRegStatsNoCIDAvailable.setUnits("messages")
_CcpCdmaExtPcfSoPppSetupStats_ObjectIdentity = ObjectIdentity
ccpCdmaExtPcfSoPppSetupStats = _CcpCdmaExtPcfSoPppSetupStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7)
)
_CcpCdmaExtPcfSoPppSetupStatsTable_Object = MibTable
ccpCdmaExtPcfSoPppSetupStatsTable = _CcpCdmaExtPcfSoPppSetupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppSetupStatsTable.setStatus("current")
_CcpCdmaExtPcfSoPppSetupStatsEntry_Object = MibTableRow
ccpCdmaExtPcfSoPppSetupStatsEntry = _CcpCdmaExtPcfSoPppSetupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppSetupStatsEntry.setStatus("current")
_CcpCdmaExtPcfSoPppPreLCPPdsnA10Rls_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppPreLCPPdsnA10Rls_Object = MibTableColumn
ccpCdmaExtPcfSoPppPreLCPPdsnA10Rls = _CcpCdmaExtPcfSoPppPreLCPPdsnA10Rls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 1),
    _CcpCdmaExtPcfSoPppPreLCPPdsnA10Rls_Type()
)
ccpCdmaExtPcfSoPppPreLCPPdsnA10Rls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppPreLCPPdsnA10Rls.setStatus("current")
_CcpCdmaExtPcfSoPppPreLCPPcfA10Rls_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppPreLCPPcfA10Rls_Object = MibTableColumn
ccpCdmaExtPcfSoPppPreLCPPcfA10Rls = _CcpCdmaExtPcfSoPppPreLCPPcfA10Rls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 2),
    _CcpCdmaExtPcfSoPppPreLCPPcfA10Rls_Type()
)
ccpCdmaExtPcfSoPppPreLCPPcfA10Rls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppPreLCPPcfA10Rls.setStatus("current")
_CcpCdmaExtPcfSoPppLcpOptionIssueFailures_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppLcpOptionIssueFailures_Object = MibTableColumn
ccpCdmaExtPcfSoPppLcpOptionIssueFailures = _CcpCdmaExtPcfSoPppLcpOptionIssueFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 3),
    _CcpCdmaExtPcfSoPppLcpOptionIssueFailures_Type()
)
ccpCdmaExtPcfSoPppLcpOptionIssueFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppLcpOptionIssueFailures.setStatus("current")
_CcpCdmaExtPcfSoPppLcpFailuresMaxRetrans_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppLcpFailuresMaxRetrans_Object = MibTableColumn
ccpCdmaExtPcfSoPppLcpFailuresMaxRetrans = _CcpCdmaExtPcfSoPppLcpFailuresMaxRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 4),
    _CcpCdmaExtPcfSoPppLcpFailuresMaxRetrans_Type()
)
ccpCdmaExtPcfSoPppLcpFailuresMaxRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppLcpFailuresMaxRetrans.setStatus("current")
_CcpCdmaExtPcfSoPppLcpFailuresUnknown_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppLcpFailuresUnknown_Object = MibTableColumn
ccpCdmaExtPcfSoPppLcpFailuresUnknown = _CcpCdmaExtPcfSoPppLcpFailuresUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 5),
    _CcpCdmaExtPcfSoPppLcpFailuresUnknown_Type()
)
ccpCdmaExtPcfSoPppLcpFailuresUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppLcpFailuresUnknown.setStatus("current")
_CcpCdmaExtPcfSoPppLcpPhaseRxTermreqs_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppLcpPhaseRxTermreqs_Object = MibTableColumn
ccpCdmaExtPcfSoPppLcpPhaseRxTermreqs = _CcpCdmaExtPcfSoPppLcpPhaseRxTermreqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 6),
    _CcpCdmaExtPcfSoPppLcpPhaseRxTermreqs_Type()
)
ccpCdmaExtPcfSoPppLcpPhaseRxTermreqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppLcpPhaseRxTermreqs.setStatus("current")
_CcpCdmaExtPcfSoPppLcpPcfA10Rls_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppLcpPcfA10Rls_Object = MibTableColumn
ccpCdmaExtPcfSoPppLcpPcfA10Rls = _CcpCdmaExtPcfSoPppLcpPcfA10Rls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 7),
    _CcpCdmaExtPcfSoPppLcpPcfA10Rls_Type()
)
ccpCdmaExtPcfSoPppLcpPcfA10Rls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppLcpPcfA10Rls.setStatus("current")
_CcpCdmaExtPcfSoPppAuthFailures_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppAuthFailures_Object = MibTableColumn
ccpCdmaExtPcfSoPppAuthFailures = _CcpCdmaExtPcfSoPppAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 8),
    _CcpCdmaExtPcfSoPppAuthFailures_Type()
)
ccpCdmaExtPcfSoPppAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppAuthFailures.setStatus("current")
_CcpCdmaExtPcfSoPppAuthAAATimeouts_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppAuthAAATimeouts_Object = MibTableColumn
ccpCdmaExtPcfSoPppAuthAAATimeouts = _CcpCdmaExtPcfSoPppAuthAAATimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 9),
    _CcpCdmaExtPcfSoPppAuthAAATimeouts_Type()
)
ccpCdmaExtPcfSoPppAuthAAATimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppAuthAAATimeouts.setStatus("current")
_CcpCdmaExtPcfSoPppAuthFailuresUnknown_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppAuthFailuresUnknown_Object = MibTableColumn
ccpCdmaExtPcfSoPppAuthFailuresUnknown = _CcpCdmaExtPcfSoPppAuthFailuresUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 10),
    _CcpCdmaExtPcfSoPppAuthFailuresUnknown_Type()
)
ccpCdmaExtPcfSoPppAuthFailuresUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppAuthFailuresUnknown.setStatus("current")
_CcpCdmaExtPcfSoPppAuthMaxRetransFailures_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppAuthMaxRetransFailures_Object = MibTableColumn
ccpCdmaExtPcfSoPppAuthMaxRetransFailures = _CcpCdmaExtPcfSoPppAuthMaxRetransFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 11),
    _CcpCdmaExtPcfSoPppAuthMaxRetransFailures_Type()
)
ccpCdmaExtPcfSoPppAuthMaxRetransFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppAuthMaxRetransFailures.setStatus("current")
_CcpCdmaExtPcfSoPppAuthPhaseRxTermreqs_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppAuthPhaseRxTermreqs_Object = MibTableColumn
ccpCdmaExtPcfSoPppAuthPhaseRxTermreqs = _CcpCdmaExtPcfSoPppAuthPhaseRxTermreqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 12),
    _CcpCdmaExtPcfSoPppAuthPhaseRxTermreqs_Type()
)
ccpCdmaExtPcfSoPppAuthPhaseRxTermreqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppAuthPhaseRxTermreqs.setStatus("current")
_CcpCdmaExtPcfSoPppAuthPcfA10Rls_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppAuthPcfA10Rls_Object = MibTableColumn
ccpCdmaExtPcfSoPppAuthPcfA10Rls = _CcpCdmaExtPcfSoPppAuthPcfA10Rls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 13),
    _CcpCdmaExtPcfSoPppAuthPcfA10Rls_Type()
)
ccpCdmaExtPcfSoPppAuthPcfA10Rls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppAuthPcfA10Rls.setStatus("current")
_CcpCdmaExtPcfSoPppIpcpOptionIssueFailures_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppIpcpOptionIssueFailures_Object = MibTableColumn
ccpCdmaExtPcfSoPppIpcpOptionIssueFailures = _CcpCdmaExtPcfSoPppIpcpOptionIssueFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 14),
    _CcpCdmaExtPcfSoPppIpcpOptionIssueFailures_Type()
)
ccpCdmaExtPcfSoPppIpcpOptionIssueFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppIpcpOptionIssueFailures.setStatus("current")
_CcpCdmaExtPcfSoPppIpcpFailuresMaxRetrans_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppIpcpFailuresMaxRetrans_Object = MibTableColumn
ccpCdmaExtPcfSoPppIpcpFailuresMaxRetrans = _CcpCdmaExtPcfSoPppIpcpFailuresMaxRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 15),
    _CcpCdmaExtPcfSoPppIpcpFailuresMaxRetrans_Type()
)
ccpCdmaExtPcfSoPppIpcpFailuresMaxRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppIpcpFailuresMaxRetrans.setStatus("current")
_CcpCdmaExtPcfSoPppIpcpFailuresUnknown_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppIpcpFailuresUnknown_Object = MibTableColumn
ccpCdmaExtPcfSoPppIpcpFailuresUnknown = _CcpCdmaExtPcfSoPppIpcpFailuresUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 16),
    _CcpCdmaExtPcfSoPppIpcpFailuresUnknown_Type()
)
ccpCdmaExtPcfSoPppIpcpFailuresUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppIpcpFailuresUnknown.setStatus("current")
_CcpCdmaExtPcfSoPppIpcpPhaseRxTermreqs_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppIpcpPhaseRxTermreqs_Object = MibTableColumn
ccpCdmaExtPcfSoPppIpcpPhaseRxTermreqs = _CcpCdmaExtPcfSoPppIpcpPhaseRxTermreqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 17),
    _CcpCdmaExtPcfSoPppIpcpPhaseRxTermreqs_Type()
)
ccpCdmaExtPcfSoPppIpcpPhaseRxTermreqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppIpcpPhaseRxTermreqs.setStatus("current")
_CcpCdmaExtPcfSoPppIpcpPcfA10Rls_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppIpcpPcfA10Rls_Object = MibTableColumn
ccpCdmaExtPcfSoPppIpcpPcfA10Rls = _CcpCdmaExtPcfSoPppIpcpPcfA10Rls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 18),
    _CcpCdmaExtPcfSoPppIpcpPcfA10Rls_Type()
)
ccpCdmaExtPcfSoPppIpcpPcfA10Rls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppIpcpPcfA10Rls.setStatus("current")
_CcpCdmaExtPcfSoPppIpcpIpResourceFail_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppIpcpIpResourceFail_Object = MibTableColumn
ccpCdmaExtPcfSoPppIpcpIpResourceFail = _CcpCdmaExtPcfSoPppIpcpIpResourceFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 19),
    _CcpCdmaExtPcfSoPppIpcpIpResourceFail_Type()
)
ccpCdmaExtPcfSoPppIpcpIpResourceFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppIpcpIpResourceFail.setStatus("current")
_CcpCdmaExtPcfSoPppRenegTotalReqs_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppRenegTotalReqs_Object = MibTableColumn
ccpCdmaExtPcfSoPppRenegTotalReqs = _CcpCdmaExtPcfSoPppRenegTotalReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 20),
    _CcpCdmaExtPcfSoPppRenegTotalReqs_Type()
)
ccpCdmaExtPcfSoPppRenegTotalReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppRenegTotalReqs.setStatus("current")
_CcpCdmaExtPcfSoPppRenegByPdsnReqs_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppRenegByPdsnReqs_Object = MibTableColumn
ccpCdmaExtPcfSoPppRenegByPdsnReqs = _CcpCdmaExtPcfSoPppRenegByPdsnReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 21),
    _CcpCdmaExtPcfSoPppRenegByPdsnReqs_Type()
)
ccpCdmaExtPcfSoPppRenegByPdsnReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppRenegByPdsnReqs.setStatus("current")
_CcpCdmaExtPcfSoPppRenegByMobileReqs_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppRenegByMobileReqs_Object = MibTableColumn
ccpCdmaExtPcfSoPppRenegByMobileReqs = _CcpCdmaExtPcfSoPppRenegByMobileReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 22),
    _CcpCdmaExtPcfSoPppRenegByMobileReqs_Type()
)
ccpCdmaExtPcfSoPppRenegByMobileReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppRenegByMobileReqs.setStatus("current")
_CcpCdmaExtPcfSoPppRenegSuccesses_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppRenegSuccesses_Object = MibTableColumn
ccpCdmaExtPcfSoPppRenegSuccesses = _CcpCdmaExtPcfSoPppRenegSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 23),
    _CcpCdmaExtPcfSoPppRenegSuccesses_Type()
)
ccpCdmaExtPcfSoPppRenegSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppRenegSuccesses.setStatus("current")
_CcpCdmaExtPcfSoPppRenegFailures_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppRenegFailures_Object = MibTableColumn
ccpCdmaExtPcfSoPppRenegFailures = _CcpCdmaExtPcfSoPppRenegFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 24),
    _CcpCdmaExtPcfSoPppRenegFailures_Type()
)
ccpCdmaExtPcfSoPppRenegFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppRenegFailures.setStatus("current")
_CcpCdmaExtPcfSoPppRenegConnectionsAborted_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppRenegConnectionsAborted_Object = MibTableColumn
ccpCdmaExtPcfSoPppRenegConnectionsAborted = _CcpCdmaExtPcfSoPppRenegConnectionsAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 25),
    _CcpCdmaExtPcfSoPppRenegConnectionsAborted_Type()
)
ccpCdmaExtPcfSoPppRenegConnectionsAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppRenegConnectionsAborted.setStatus("current")
_CcpCdmaExtPcfSoPppRenegAddrMismatchReqs_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppRenegAddrMismatchReqs_Object = MibTableColumn
ccpCdmaExtPcfSoPppRenegAddrMismatchReqs = _CcpCdmaExtPcfSoPppRenegAddrMismatchReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 26),
    _CcpCdmaExtPcfSoPppRenegAddrMismatchReqs_Type()
)
ccpCdmaExtPcfSoPppRenegAddrMismatchReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppRenegAddrMismatchReqs.setStatus("current")
_CcpCdmaExtPcfSoPppRenegAccessNwIdChanges_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppRenegAccessNwIdChanges_Object = MibTableColumn
ccpCdmaExtPcfSoPppRenegAccessNwIdChanges = _CcpCdmaExtPcfSoPppRenegAccessNwIdChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 27),
    _CcpCdmaExtPcfSoPppRenegAccessNwIdChanges_Type()
)
ccpCdmaExtPcfSoPppRenegAccessNwIdChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppRenegAccessNwIdChanges.setStatus("current")
_CcpCdmaExtPcfSoPppRenegGreChangeReqs_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppRenegGreChangeReqs_Object = MibTableColumn
ccpCdmaExtPcfSoPppRenegGreChangeReqs = _CcpCdmaExtPcfSoPppRenegGreChangeReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 28),
    _CcpCdmaExtPcfSoPppRenegGreChangeReqs_Type()
)
ccpCdmaExtPcfSoPppRenegGreChangeReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppRenegGreChangeReqs.setStatus("current")
_CcpCdmaExtPcfSoPppRenegOtherReasonReqs_Type = ZeroBasedCounter32
_CcpCdmaExtPcfSoPppRenegOtherReasonReqs_Object = MibTableColumn
ccpCdmaExtPcfSoPppRenegOtherReasonReqs = _CcpCdmaExtPcfSoPppRenegOtherReasonReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 7, 1, 1, 29),
    _CcpCdmaExtPcfSoPppRenegOtherReasonReqs_Type()
)
ccpCdmaExtPcfSoPppRenegOtherReasonReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtPcfSoPppRenegOtherReasonReqs.setStatus("current")
_CcpCdmaExtRohcStats_ObjectIdentity = ObjectIdentity
ccpCdmaExtRohcStats = _CcpCdmaExtRohcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 8)
)
_CcpCdmaExtRohcSuccessCount_Type = Counter32
_CcpCdmaExtRohcSuccessCount_Object = MibScalar
ccpCdmaExtRohcSuccessCount = _CcpCdmaExtRohcSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 8, 1),
    _CcpCdmaExtRohcSuccessCount_Type()
)
ccpCdmaExtRohcSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcSuccessCount.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcSuccessCount.setUnits("passes")
_CcpCdmaExtRohcFailuresCount_Type = Counter32
_CcpCdmaExtRohcFailuresCount_Object = MibScalar
ccpCdmaExtRohcFailuresCount = _CcpCdmaExtRohcFailuresCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 8, 2),
    _CcpCdmaExtRohcFailuresCount_Type()
)
ccpCdmaExtRohcFailuresCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcFailuresCount.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcFailuresCount.setUnits("failures")
_CcpCdmaExtRohcOutIpPkts_Type = Counter32
_CcpCdmaExtRohcOutIpPkts_Object = MibScalar
ccpCdmaExtRohcOutIpPkts = _CcpCdmaExtRohcOutIpPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 8, 3),
    _CcpCdmaExtRohcOutIpPkts_Type()
)
ccpCdmaExtRohcOutIpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcOutIpPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcOutIpPkts.setUnits("packets")
_CcpCdmaExtRohcOutIpBytes_Type = Counter32
_CcpCdmaExtRohcOutIpBytes_Object = MibScalar
ccpCdmaExtRohcOutIpBytes = _CcpCdmaExtRohcOutIpBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 8, 4),
    _CcpCdmaExtRohcOutIpBytes_Type()
)
ccpCdmaExtRohcOutIpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcOutIpBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcOutIpBytes.setUnits("bytes")
_CcpCdmaExtRohcDeCompSuccessCount_Type = Counter32
_CcpCdmaExtRohcDeCompSuccessCount_Object = MibScalar
ccpCdmaExtRohcDeCompSuccessCount = _CcpCdmaExtRohcDeCompSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 8, 5),
    _CcpCdmaExtRohcDeCompSuccessCount_Type()
)
ccpCdmaExtRohcDeCompSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcDeCompSuccessCount.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcDeCompSuccessCount.setUnits("passes")
_CcpCdmaExtRohcDeCompFailuresCount_Type = Counter32
_CcpCdmaExtRohcDeCompFailuresCount_Object = MibScalar
ccpCdmaExtRohcDeCompFailuresCount = _CcpCdmaExtRohcDeCompFailuresCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 8, 6),
    _CcpCdmaExtRohcDeCompFailuresCount_Type()
)
ccpCdmaExtRohcDeCompFailuresCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcDeCompFailuresCount.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcDeCompFailuresCount.setUnits("failures")
_CcpCdmaExtRohcDeCompOutIpPkts_Type = Counter32
_CcpCdmaExtRohcDeCompOutIpPkts_Object = MibScalar
ccpCdmaExtRohcDeCompOutIpPkts = _CcpCdmaExtRohcDeCompOutIpPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 8, 7),
    _CcpCdmaExtRohcDeCompOutIpPkts_Type()
)
ccpCdmaExtRohcDeCompOutIpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcDeCompOutIpPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcDeCompOutIpPkts.setUnits("packets")
_CcpCdmaExtRohcDeCompOutIpBytes_Type = Counter32
_CcpCdmaExtRohcDeCompOutIpBytes_Object = MibScalar
ccpCdmaExtRohcDeCompOutIpBytes = _CcpCdmaExtRohcDeCompOutIpBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 2, 8, 8),
    _CcpCdmaExtRohcDeCompOutIpBytes_Type()
)
ccpCdmaExtRohcDeCompOutIpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcDeCompOutIpBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRohcDeCompOutIpBytes.setUnits("bytes")
_CcpCdmaExtRpErrors_ObjectIdentity = ObjectIdentity
ccpCdmaExtRpErrors = _CcpCdmaExtRpErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 3)
)
_CcpCdmaExtRPRegReqErrors_ObjectIdentity = ObjectIdentity
ccpCdmaExtRPRegReqErrors = _CcpCdmaExtRPRegReqErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 3, 1)
)
_CcpCdmaExtRegReqBwUnavailableSess_Type = ZeroBasedCounter32
_CcpCdmaExtRegReqBwUnavailableSess_Object = MibScalar
ccpCdmaExtRegReqBwUnavailableSess = _CcpCdmaExtRegReqBwUnavailableSess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 3, 1, 1),
    _CcpCdmaExtRegReqBwUnavailableSess_Type()
)
ccpCdmaExtRegReqBwUnavailableSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRegReqBwUnavailableSess.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRegReqBwUnavailableSess.setUnits("messages")
_CcpCdmaExtRegReqMaxServiceFlows_Type = ZeroBasedCounter32
_CcpCdmaExtRegReqMaxServiceFlows_Object = MibScalar
ccpCdmaExtRegReqMaxServiceFlows = _CcpCdmaExtRegReqMaxServiceFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 3, 1, 2),
    _CcpCdmaExtRegReqMaxServiceFlows_Type()
)
ccpCdmaExtRegReqMaxServiceFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRegReqMaxServiceFlows.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRegReqMaxServiceFlows.setUnits("messages")
_CcpCdmaExtRegReqUnSupportedSOs_Type = ZeroBasedCounter32
_CcpCdmaExtRegReqUnSupportedSOs_Object = MibScalar
ccpCdmaExtRegReqUnSupportedSOs = _CcpCdmaExtRegReqUnSupportedSOs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 3, 1, 3),
    _CcpCdmaExtRegReqUnSupportedSOs_Type()
)
ccpCdmaExtRegReqUnSupportedSOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRegReqUnSupportedSOs.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRegReqUnSupportedSOs.setUnits("messages")
_CcpCdmaExtRegReqNonExistA10s_Type = ZeroBasedCounter32
_CcpCdmaExtRegReqNonExistA10s_Object = MibScalar
ccpCdmaExtRegReqNonExistA10s = _CcpCdmaExtRegReqNonExistA10s_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 3, 1, 4),
    _CcpCdmaExtRegReqNonExistA10s_Type()
)
ccpCdmaExtRegReqNonExistA10s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRegReqNonExistA10s.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRegReqNonExistA10s.setUnits("messages")
_CcpCdmaExtRegReqNoCIDAvailable_Type = ZeroBasedCounter32
_CcpCdmaExtRegReqNoCIDAvailable_Object = MibScalar
ccpCdmaExtRegReqNoCIDAvailable = _CcpCdmaExtRegReqNoCIDAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 3, 1, 5),
    _CcpCdmaExtRegReqNoCIDAvailable_Type()
)
ccpCdmaExtRegReqNoCIDAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpCdmaExtRegReqNoCIDAvailable.setStatus("current")
if mibBuilder.loadTexts:
    ccpCdmaExtRegReqNoCIDAvailable.setUnits("messages")
_CcpCdmaExtNotifObjects_ObjectIdentity = ObjectIdentity
ccpCdmaExtNotifObjects = _CcpCdmaExtNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 4)
)


class _CcpCdmaExtNotifReason_Type(Integer32):
    """Custom type ccpCdmaExtNotifReason based on Integer32"""
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
        *(("bandwidth", 1),
          ("cputhreshold", 2),
          ("iomemthreshold", 4),
          ("procthreshold", 3))
    )


_CcpCdmaExtNotifReason_Type.__name__ = "Integer32"
_CcpCdmaExtNotifReason_Object = MibScalar
ccpCdmaExtNotifReason = _CcpCdmaExtNotifReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 4, 3),
    _CcpCdmaExtNotifReason_Type()
)
ccpCdmaExtNotifReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccpCdmaExtNotifReason.setStatus("current")
_CcpCdmaExtNotifReasonCurrentValue_Type = Gauge32
_CcpCdmaExtNotifReasonCurrentValue_Object = MibScalar
ccpCdmaExtNotifReasonCurrentValue = _CcpCdmaExtNotifReasonCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 1, 4, 4),
    _CcpCdmaExtNotifReasonCurrentValue_Type()
)
ccpCdmaExtNotifReasonCurrentValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccpCdmaExtNotifReasonCurrentValue.setStatus("current")
_CiscoCdmaPdsnExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCdmaPdsnExtMIBConformance = _CiscoCdmaPdsnExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 2)
)
_CiscoCdmaPdsnExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCdmaPdsnExtMIBCompliances = _CiscoCdmaPdsnExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 2, 1)
)
_CiscoCdmaPdsnExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCdmaPdsnExtMIBGroups = _CiscoCdmaPdsnExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 2, 2)
)
cCdmaPcfSoRpRegStatsEntry.registerAugmentions(
    ("CISCO-CDMA-PDSN-EXT-MIB",
     "ccpCdmaExtPcfSoRpRegStatsEntry")
)
ccpCdmaExtPcfSoRpRegStatsEntry.setIndexNames(*cCdmaPcfSoRpRegStatsEntry.getIndexNames())
cCdmaPcfSoPppSetupStatsEntry.registerAugmentions(
    ("CISCO-CDMA-PDSN-EXT-MIB",
     "ccpCdmaExtPcfSoPppSetupStatsEntry")
)
ccpCdmaExtPcfSoPppSetupStatsEntry.setIndexNames(*cCdmaPcfSoPppSetupStatsEntry.getIndexNames())

# Managed Objects groups

ciscoCdmaExtSystemPdsnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 2, 2, 1)
)
ciscoCdmaExtSystemPdsnGroup.setObjects(
      *(("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRsvpCreationFailureTfts"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRsvpPacketFilterAddFailureTfts"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRsvpPacketFilterUnavailableTfts"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRsvpPacketFilterReplaceFailureTfts"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRsvpPacketFilterAddBeforeCreationTfts"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRsvpUnableToParseTfts"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRsvpPrecedenceContentionTfts"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRsvpTreatmentUnsupportedTfts"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRsvpMaxPacketFiltersReachedTfts"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRsvpCreationSuccessTfts"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRsvpUnAuthorizeTfts"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtQosSuccesses"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtQosFailures"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtQosDscpRemarkedPkts"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtAuxSessionTotal"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPolicingSessionTotal"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtDscpSession"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtBandwidthPolicyInstallFailures"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtBandwidthPolicyRemoves"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtBandwidthPolicyInstallSuccesses"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRpReRegNewAuxConnections"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRpReRegCloseAuxConnections"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRpReRegRemapFlows"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRpRegNewAuxConnections"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtNotifReason"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtNotifReasonCurrentValue"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtSessionAuxConnectionsTotal"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtAvailableBandwidth"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPolicingEnabled"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtTotalBandwidth"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtAllocatedBandwidth"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtSessionAuxConnectionsEnabled"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtLoadHighReachedNotifEnabled"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtSessionMaxAuxConnectionsAllowed"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRpSessionUpdSubQoses"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRegReqMaxServiceFlows"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRegReqUnSupportedSOs"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRegReqNonExistA10s"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRegReqBwUnavailableSess"))
)
if mibBuilder.loadTexts:
    ciscoCdmaExtSystemPdsnGroup.setStatus("current")

ciscoCdmaExtPdsnPcfSoRpRegGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 2, 2, 3)
)
ciscoCdmaExtPdsnPcfSoRpRegGroup.setObjects(
      *(("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoStatsTotalAuxConnections"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoRpRegStatsNewAuxConnections"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoRpReRegStatsNewAuxConnections"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoRpReRegStatsCloseAuxConnections"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoRpReRegStatsRemapFlows"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoRpRegStatsSessionUpdSubQoses"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoRpRegStatsMaxServiceFlows"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoRpRegStatsUnsupportedSOs"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoRpRegStatsNonExistA10s"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoRpRegStatsBwUnavailableSess"))
)
if mibBuilder.loadTexts:
    ciscoCdmaExtPdsnPcfSoRpRegGroup.setStatus("current")

ciscoCdmaExtSystemPdsnCacGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 2, 2, 4)
)
ciscoCdmaExtSystemPdsnCacGroup.setObjects(
    ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtCacEnabled")
)
if mibBuilder.loadTexts:
    ciscoCdmaExtSystemPdsnCacGroup.setStatus("current")

ciscoCdmaExtPdsnPcfSoPppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 2, 2, 5)
)
ciscoCdmaExtPdsnPcfSoPppGroup.setObjects(
      *(("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppPreLCPPdsnA10Rls"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppPreLCPPcfA10Rls"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppLcpOptionIssueFailures"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppLcpFailuresMaxRetrans"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppLcpFailuresUnknown"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppLcpPhaseRxTermreqs"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppLcpPcfA10Rls"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppAuthFailures"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppAuthAAATimeouts"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppAuthMaxRetransFailures"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppAuthPhaseRxTermreqs"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppAuthFailuresUnknown"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppAuthPcfA10Rls"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppIpcpOptionIssueFailures"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppIpcpFailuresMaxRetrans"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppIpcpFailuresUnknown"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppIpcpPhaseRxTermreqs"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppIpcpPcfA10Rls"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppIpcpIpResourceFail"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppRenegTotalReqs"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppRenegByPdsnReqs"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppRenegByMobileReqs"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppRenegSuccesses"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppRenegFailures"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppRenegConnectionsAborted"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppRenegAddrMismatchReqs"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppRenegAccessNwIdChanges"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppRenegGreChangeReqs"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoPppRenegOtherReasonReqs"))
)
if mibBuilder.loadTexts:
    ciscoCdmaExtPdsnPcfSoPppGroup.setStatus("current")

ciscoCdmaExtSystemPdsnGroupSupR01 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 2, 2, 6)
)
ciscoCdmaExtSystemPdsnGroupSupR01.setObjects(
      *(("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRohcEnabled"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRohcSuccessCount"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRohcFailuresCount"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRohcOutIpPkts"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRohcOutIpBytes"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRohcDeCompSuccessCount"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRohcDeCompFailuresCount"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRohcDeCompOutIpPkts"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRohcDeCompOutIpBytes"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRohcAuxA10sCount"))
)
if mibBuilder.loadTexts:
    ciscoCdmaExtSystemPdsnGroupSupR01.setStatus("current")

ciscoCdmaExtPdsnPcfSoRpRegGroupSupR01 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 2, 2, 7)
)
ciscoCdmaExtPdsnPcfSoRpRegGroupSupR01.setObjects(
    ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtPcfSoRpRegStatsNoCIDAvailable")
)
if mibBuilder.loadTexts:
    ciscoCdmaExtPdsnPcfSoRpRegGroupSupR01.setStatus("current")

ciscoCdmaExtSystemPdsnGroupSupR02 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 2, 2, 8)
)
ciscoCdmaExtSystemPdsnGroupSupR02.setObjects(
    ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtRegReqNoCIDAvailable")
)
if mibBuilder.loadTexts:
    ciscoCdmaExtSystemPdsnGroupSupR02.setStatus("current")


# Notification objects

ciscoCdmaExtLoadLowReachedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 0, 1)
)
ciscoCdmaExtLoadLowReachedNotif.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaServingPdsnHostname"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtNotifReason"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtNotifReasonCurrentValue"))
)
if mibBuilder.loadTexts:
    ciscoCdmaExtLoadLowReachedNotif.setStatus(
        "current"
    )

ciscoCdmaExtLoadHighReachedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 0, 2)
)
ciscoCdmaExtLoadHighReachedNotif.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaServingPdsnHostname"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtNotifReason"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ccpCdmaExtNotifReasonCurrentValue"))
)
if mibBuilder.loadTexts:
    ciscoCdmaExtLoadHighReachedNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoCdmaExtNotifPdsnGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 2, 2, 2)
)
ciscoCdmaExtNotifPdsnGroup.setObjects(
      *(("CISCO-CDMA-PDSN-EXT-MIB", "ciscoCdmaExtLoadLowReachedNotif"),
        ("CISCO-CDMA-PDSN-EXT-MIB", "ciscoCdmaExtLoadHighReachedNotif"))
)
if mibBuilder.loadTexts:
    ciscoCdmaExtNotifPdsnGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCdmaPdsnExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCdmaPdsnExtMIBCompliance.setStatus(
        "deprecated"
    )

ciscoCdmaPdsnExtMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCdmaPdsnExtMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoCdmaPdsnExtMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoCdmaPdsnExtMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoCdmaPdsnExtMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 669, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoCdmaPdsnExtMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CDMA-PDSN-EXT-MIB",
    **{"ciscoCdmaPdsnExtMIB": ciscoCdmaPdsnExtMIB,
       "ciscoCdmaPdsnExtMIBNotifs": ciscoCdmaPdsnExtMIBNotifs,
       "ciscoCdmaExtLoadLowReachedNotif": ciscoCdmaExtLoadLowReachedNotif,
       "ciscoCdmaExtLoadHighReachedNotif": ciscoCdmaExtLoadHighReachedNotif,
       "ciscoCdmaPdsnExtMIBObjects": ciscoCdmaPdsnExtMIBObjects,
       "ccpCdmaExtSystemInfo": ccpCdmaExtSystemInfo,
       "ccpCdmaExtTotalBandwidth": ccpCdmaExtTotalBandwidth,
       "ccpCdmaExtAvailableBandwidth": ccpCdmaExtAvailableBandwidth,
       "ccpCdmaExtAllocatedBandwidth": ccpCdmaExtAllocatedBandwidth,
       "ccpCdmaExtSessionAuxConnectionsEnabled": ccpCdmaExtSessionAuxConnectionsEnabled,
       "ccpCdmaExtSessionMaxAuxConnectionsAllowed": ccpCdmaExtSessionMaxAuxConnectionsAllowed,
       "ccpCdmaExtSessionAuxConnectionsTotal": ccpCdmaExtSessionAuxConnectionsTotal,
       "ccpCdmaExtPolicingEnabled": ccpCdmaExtPolicingEnabled,
       "ccpCdmaExtAuxSessionTotal": ccpCdmaExtAuxSessionTotal,
       "ccpCdmaExtPolicingSessionTotal": ccpCdmaExtPolicingSessionTotal,
       "ccpCdmaExtDscpSession": ccpCdmaExtDscpSession,
       "ccpCdmaExtLoadHighReachedNotifEnabled": ccpCdmaExtLoadHighReachedNotifEnabled,
       "ccpCdmaExtCacEnabled": ccpCdmaExtCacEnabled,
       "ccpCdmaExtRohcEnabled": ccpCdmaExtRohcEnabled,
       "ccpCdmaExtRohcAuxA10sCount": ccpCdmaExtRohcAuxA10sCount,
       "ccpCdmaExtPerformanceStats": ccpCdmaExtPerformanceStats,
       "ccpCdmaExtRsvpStats": ccpCdmaExtRsvpStats,
       "ccpCdmaExtRsvpCreationSuccessTfts": ccpCdmaExtRsvpCreationSuccessTfts,
       "ccpCdmaExtRsvpCreationFailureTfts": ccpCdmaExtRsvpCreationFailureTfts,
       "ccpCdmaExtRsvpPacketFilterAddFailureTfts": ccpCdmaExtRsvpPacketFilterAddFailureTfts,
       "ccpCdmaExtRsvpPacketFilterUnavailableTfts": ccpCdmaExtRsvpPacketFilterUnavailableTfts,
       "ccpCdmaExtRsvpPacketFilterReplaceFailureTfts": ccpCdmaExtRsvpPacketFilterReplaceFailureTfts,
       "ccpCdmaExtRsvpPacketFilterAddBeforeCreationTfts": ccpCdmaExtRsvpPacketFilterAddBeforeCreationTfts,
       "ccpCdmaExtRsvpUnableToParseTfts": ccpCdmaExtRsvpUnableToParseTfts,
       "ccpCdmaExtRsvpPrecedenceContentionTfts": ccpCdmaExtRsvpPrecedenceContentionTfts,
       "ccpCdmaExtRsvpTreatmentUnsupportedTfts": ccpCdmaExtRsvpTreatmentUnsupportedTfts,
       "ccpCdmaExtRsvpMaxPacketFiltersReachedTfts": ccpCdmaExtRsvpMaxPacketFiltersReachedTfts,
       "ccpCdmaExtRsvpUnAuthorizeTfts": ccpCdmaExtRsvpUnAuthorizeTfts,
       "ccpCdmaExtQosStats": ccpCdmaExtQosStats,
       "ccpCdmaExtQosSuccesses": ccpCdmaExtQosSuccesses,
       "ccpCdmaExtQosFailures": ccpCdmaExtQosFailures,
       "ccpCdmaExtQosDscpRemarkedPkts": ccpCdmaExtQosDscpRemarkedPkts,
       "ccpCdmaExtBandwidthPolicyStats": ccpCdmaExtBandwidthPolicyStats,
       "ccpCdmaExtBandwidthPolicyInstallSuccesses": ccpCdmaExtBandwidthPolicyInstallSuccesses,
       "ccpCdmaExtBandwidthPolicyInstallFailures": ccpCdmaExtBandwidthPolicyInstallFailures,
       "ccpCdmaExtBandwidthPolicyRemoves": ccpCdmaExtBandwidthPolicyRemoves,
       "ccpCdmaExtRpRegStats": ccpCdmaExtRpRegStats,
       "ccpCdmaExtRpReRegNewAuxConnections": ccpCdmaExtRpReRegNewAuxConnections,
       "ccpCdmaExtRpReRegCloseAuxConnections": ccpCdmaExtRpReRegCloseAuxConnections,
       "ccpCdmaExtRpReRegRemapFlows": ccpCdmaExtRpReRegRemapFlows,
       "ccpCdmaExtRpRegNewAuxConnections": ccpCdmaExtRpRegNewAuxConnections,
       "ccpCdmaExtRpSessUpdStats": ccpCdmaExtRpSessUpdStats,
       "ccpCdmaExtRpSessionUpdSubQoses": ccpCdmaExtRpSessionUpdSubQoses,
       "ccpCdmaExtPcfSoRpRegStats": ccpCdmaExtPcfSoRpRegStats,
       "ccpCdmaExtPcfSoRpRegStatsTable": ccpCdmaExtPcfSoRpRegStatsTable,
       "ccpCdmaExtPcfSoRpRegStatsEntry": ccpCdmaExtPcfSoRpRegStatsEntry,
       "ccpCdmaExtPcfSoStatsTotalAuxConnections": ccpCdmaExtPcfSoStatsTotalAuxConnections,
       "ccpCdmaExtPcfSoRpRegStatsNewAuxConnections": ccpCdmaExtPcfSoRpRegStatsNewAuxConnections,
       "ccpCdmaExtPcfSoRpReRegStatsNewAuxConnections": ccpCdmaExtPcfSoRpReRegStatsNewAuxConnections,
       "ccpCdmaExtPcfSoRpReRegStatsCloseAuxConnections": ccpCdmaExtPcfSoRpReRegStatsCloseAuxConnections,
       "ccpCdmaExtPcfSoRpReRegStatsRemapFlows": ccpCdmaExtPcfSoRpReRegStatsRemapFlows,
       "ccpCdmaExtPcfSoRpRegStatsBwUnavailableSess": ccpCdmaExtPcfSoRpRegStatsBwUnavailableSess,
       "ccpCdmaExtPcfSoRpRegStatsSessionUpdSubQoses": ccpCdmaExtPcfSoRpRegStatsSessionUpdSubQoses,
       "ccpCdmaExtPcfSoRpRegStatsMaxServiceFlows": ccpCdmaExtPcfSoRpRegStatsMaxServiceFlows,
       "ccpCdmaExtPcfSoRpRegStatsUnsupportedSOs": ccpCdmaExtPcfSoRpRegStatsUnsupportedSOs,
       "ccpCdmaExtPcfSoRpRegStatsNonExistA10s": ccpCdmaExtPcfSoRpRegStatsNonExistA10s,
       "ccpCdmaExtPcfSoRpRegStatsNoCIDAvailable": ccpCdmaExtPcfSoRpRegStatsNoCIDAvailable,
       "ccpCdmaExtPcfSoPppSetupStats": ccpCdmaExtPcfSoPppSetupStats,
       "ccpCdmaExtPcfSoPppSetupStatsTable": ccpCdmaExtPcfSoPppSetupStatsTable,
       "ccpCdmaExtPcfSoPppSetupStatsEntry": ccpCdmaExtPcfSoPppSetupStatsEntry,
       "ccpCdmaExtPcfSoPppPreLCPPdsnA10Rls": ccpCdmaExtPcfSoPppPreLCPPdsnA10Rls,
       "ccpCdmaExtPcfSoPppPreLCPPcfA10Rls": ccpCdmaExtPcfSoPppPreLCPPcfA10Rls,
       "ccpCdmaExtPcfSoPppLcpOptionIssueFailures": ccpCdmaExtPcfSoPppLcpOptionIssueFailures,
       "ccpCdmaExtPcfSoPppLcpFailuresMaxRetrans": ccpCdmaExtPcfSoPppLcpFailuresMaxRetrans,
       "ccpCdmaExtPcfSoPppLcpFailuresUnknown": ccpCdmaExtPcfSoPppLcpFailuresUnknown,
       "ccpCdmaExtPcfSoPppLcpPhaseRxTermreqs": ccpCdmaExtPcfSoPppLcpPhaseRxTermreqs,
       "ccpCdmaExtPcfSoPppLcpPcfA10Rls": ccpCdmaExtPcfSoPppLcpPcfA10Rls,
       "ccpCdmaExtPcfSoPppAuthFailures": ccpCdmaExtPcfSoPppAuthFailures,
       "ccpCdmaExtPcfSoPppAuthAAATimeouts": ccpCdmaExtPcfSoPppAuthAAATimeouts,
       "ccpCdmaExtPcfSoPppAuthFailuresUnknown": ccpCdmaExtPcfSoPppAuthFailuresUnknown,
       "ccpCdmaExtPcfSoPppAuthMaxRetransFailures": ccpCdmaExtPcfSoPppAuthMaxRetransFailures,
       "ccpCdmaExtPcfSoPppAuthPhaseRxTermreqs": ccpCdmaExtPcfSoPppAuthPhaseRxTermreqs,
       "ccpCdmaExtPcfSoPppAuthPcfA10Rls": ccpCdmaExtPcfSoPppAuthPcfA10Rls,
       "ccpCdmaExtPcfSoPppIpcpOptionIssueFailures": ccpCdmaExtPcfSoPppIpcpOptionIssueFailures,
       "ccpCdmaExtPcfSoPppIpcpFailuresMaxRetrans": ccpCdmaExtPcfSoPppIpcpFailuresMaxRetrans,
       "ccpCdmaExtPcfSoPppIpcpFailuresUnknown": ccpCdmaExtPcfSoPppIpcpFailuresUnknown,
       "ccpCdmaExtPcfSoPppIpcpPhaseRxTermreqs": ccpCdmaExtPcfSoPppIpcpPhaseRxTermreqs,
       "ccpCdmaExtPcfSoPppIpcpPcfA10Rls": ccpCdmaExtPcfSoPppIpcpPcfA10Rls,
       "ccpCdmaExtPcfSoPppIpcpIpResourceFail": ccpCdmaExtPcfSoPppIpcpIpResourceFail,
       "ccpCdmaExtPcfSoPppRenegTotalReqs": ccpCdmaExtPcfSoPppRenegTotalReqs,
       "ccpCdmaExtPcfSoPppRenegByPdsnReqs": ccpCdmaExtPcfSoPppRenegByPdsnReqs,
       "ccpCdmaExtPcfSoPppRenegByMobileReqs": ccpCdmaExtPcfSoPppRenegByMobileReqs,
       "ccpCdmaExtPcfSoPppRenegSuccesses": ccpCdmaExtPcfSoPppRenegSuccesses,
       "ccpCdmaExtPcfSoPppRenegFailures": ccpCdmaExtPcfSoPppRenegFailures,
       "ccpCdmaExtPcfSoPppRenegConnectionsAborted": ccpCdmaExtPcfSoPppRenegConnectionsAborted,
       "ccpCdmaExtPcfSoPppRenegAddrMismatchReqs": ccpCdmaExtPcfSoPppRenegAddrMismatchReqs,
       "ccpCdmaExtPcfSoPppRenegAccessNwIdChanges": ccpCdmaExtPcfSoPppRenegAccessNwIdChanges,
       "ccpCdmaExtPcfSoPppRenegGreChangeReqs": ccpCdmaExtPcfSoPppRenegGreChangeReqs,
       "ccpCdmaExtPcfSoPppRenegOtherReasonReqs": ccpCdmaExtPcfSoPppRenegOtherReasonReqs,
       "ccpCdmaExtRohcStats": ccpCdmaExtRohcStats,
       "ccpCdmaExtRohcSuccessCount": ccpCdmaExtRohcSuccessCount,
       "ccpCdmaExtRohcFailuresCount": ccpCdmaExtRohcFailuresCount,
       "ccpCdmaExtRohcOutIpPkts": ccpCdmaExtRohcOutIpPkts,
       "ccpCdmaExtRohcOutIpBytes": ccpCdmaExtRohcOutIpBytes,
       "ccpCdmaExtRohcDeCompSuccessCount": ccpCdmaExtRohcDeCompSuccessCount,
       "ccpCdmaExtRohcDeCompFailuresCount": ccpCdmaExtRohcDeCompFailuresCount,
       "ccpCdmaExtRohcDeCompOutIpPkts": ccpCdmaExtRohcDeCompOutIpPkts,
       "ccpCdmaExtRohcDeCompOutIpBytes": ccpCdmaExtRohcDeCompOutIpBytes,
       "ccpCdmaExtRpErrors": ccpCdmaExtRpErrors,
       "ccpCdmaExtRPRegReqErrors": ccpCdmaExtRPRegReqErrors,
       "ccpCdmaExtRegReqBwUnavailableSess": ccpCdmaExtRegReqBwUnavailableSess,
       "ccpCdmaExtRegReqMaxServiceFlows": ccpCdmaExtRegReqMaxServiceFlows,
       "ccpCdmaExtRegReqUnSupportedSOs": ccpCdmaExtRegReqUnSupportedSOs,
       "ccpCdmaExtRegReqNonExistA10s": ccpCdmaExtRegReqNonExistA10s,
       "ccpCdmaExtRegReqNoCIDAvailable": ccpCdmaExtRegReqNoCIDAvailable,
       "ccpCdmaExtNotifObjects": ccpCdmaExtNotifObjects,
       "ccpCdmaExtNotifReason": ccpCdmaExtNotifReason,
       "ccpCdmaExtNotifReasonCurrentValue": ccpCdmaExtNotifReasonCurrentValue,
       "ciscoCdmaPdsnExtMIBConformance": ciscoCdmaPdsnExtMIBConformance,
       "ciscoCdmaPdsnExtMIBCompliances": ciscoCdmaPdsnExtMIBCompliances,
       "ciscoCdmaPdsnExtMIBCompliance": ciscoCdmaPdsnExtMIBCompliance,
       "ciscoCdmaPdsnExtMIBComplianceRev1": ciscoCdmaPdsnExtMIBComplianceRev1,
       "ciscoCdmaPdsnExtMIBComplianceRev2": ciscoCdmaPdsnExtMIBComplianceRev2,
       "ciscoCdmaPdsnExtMIBComplianceRev3": ciscoCdmaPdsnExtMIBComplianceRev3,
       "ciscoCdmaPdsnExtMIBGroups": ciscoCdmaPdsnExtMIBGroups,
       "ciscoCdmaExtSystemPdsnGroup": ciscoCdmaExtSystemPdsnGroup,
       "ciscoCdmaExtNotifPdsnGroup": ciscoCdmaExtNotifPdsnGroup,
       "ciscoCdmaExtPdsnPcfSoRpRegGroup": ciscoCdmaExtPdsnPcfSoRpRegGroup,
       "ciscoCdmaExtSystemPdsnCacGroup": ciscoCdmaExtSystemPdsnCacGroup,
       "ciscoCdmaExtPdsnPcfSoPppGroup": ciscoCdmaExtPdsnPcfSoPppGroup,
       "ciscoCdmaExtSystemPdsnGroupSupR01": ciscoCdmaExtSystemPdsnGroupSupR01,
       "ciscoCdmaExtPdsnPcfSoRpRegGroupSupR01": ciscoCdmaExtPdsnPcfSoRpRegGroupSupR01,
       "ciscoCdmaExtSystemPdsnGroupSupR02": ciscoCdmaExtSystemPdsnGroupSupR02}
)
