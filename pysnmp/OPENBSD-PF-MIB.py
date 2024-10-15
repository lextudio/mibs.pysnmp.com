# SNMP MIB module (OPENBSD-PF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPENBSD-PF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:19 2024
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

(openBSD,) = mibBuilder.importSymbols(
    "OPENBSD-BASE-MIB",
    "openBSD")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pfMIBObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 1)
)
pfMIBObjects.setRevisions(
        ("2015-06-09 17:28",
         "2013-08-31 04:46",
         "2013-02-24 20:33",
         "2012-01-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PfInfo_ObjectIdentity = ObjectIdentity
pfInfo = _PfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 1, 1)
)
_PfRunning_Type = TruthValue
_PfRunning_Object = MibScalar
pfRunning = _PfRunning_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 1, 1),
    _PfRunning_Type()
)
pfRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfRunning.setStatus("current")
_PfRuntime_Type = TimeTicks
_PfRuntime_Object = MibScalar
pfRuntime = _PfRuntime_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 1, 2),
    _PfRuntime_Type()
)
pfRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfRuntime.setStatus("current")
if mibBuilder.loadTexts:
    pfRuntime.setUnits("1/100th of a Second")


class _PfDebug_Type(Integer32):
    """Custom type pfDebug based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("crit", 2),
          ("debug", 7),
          ("emerg", 0),
          ("err", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_PfDebug_Type.__name__ = "Integer32"
_PfDebug_Object = MibScalar
pfDebug = _PfDebug_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 1, 3),
    _PfDebug_Type()
)
pfDebug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfDebug.setStatus("current")
_PfHostid_Type = OctetString
_PfHostid_Object = MibScalar
pfHostid = _PfHostid_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 1, 4),
    _PfHostid_Type()
)
pfHostid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfHostid.setStatus("current")
_PfCounters_ObjectIdentity = ObjectIdentity
pfCounters = _PfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2)
)
_PfCntMatch_Type = Counter64
_PfCntMatch_Object = MibScalar
pfCntMatch = _PfCntMatch_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2, 1),
    _PfCntMatch_Type()
)
pfCntMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCntMatch.setStatus("current")
_PfCntBadOffset_Type = Counter64
_PfCntBadOffset_Object = MibScalar
pfCntBadOffset = _PfCntBadOffset_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2, 2),
    _PfCntBadOffset_Type()
)
pfCntBadOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCntBadOffset.setStatus("current")
_PfCntFragment_Type = Counter64
_PfCntFragment_Object = MibScalar
pfCntFragment = _PfCntFragment_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2, 3),
    _PfCntFragment_Type()
)
pfCntFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCntFragment.setStatus("current")
_PfCntShort_Type = Counter64
_PfCntShort_Object = MibScalar
pfCntShort = _PfCntShort_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2, 4),
    _PfCntShort_Type()
)
pfCntShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCntShort.setStatus("current")
_PfCntNormalize_Type = Counter64
_PfCntNormalize_Object = MibScalar
pfCntNormalize = _PfCntNormalize_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2, 5),
    _PfCntNormalize_Type()
)
pfCntNormalize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCntNormalize.setStatus("current")
_PfCntMemory_Type = Counter64
_PfCntMemory_Object = MibScalar
pfCntMemory = _PfCntMemory_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2, 6),
    _PfCntMemory_Type()
)
pfCntMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCntMemory.setStatus("current")
_PfCntTimestamp_Type = Counter64
_PfCntTimestamp_Object = MibScalar
pfCntTimestamp = _PfCntTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2, 7),
    _PfCntTimestamp_Type()
)
pfCntTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCntTimestamp.setStatus("current")
_PfCntCongestion_Type = Counter64
_PfCntCongestion_Object = MibScalar
pfCntCongestion = _PfCntCongestion_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2, 8),
    _PfCntCongestion_Type()
)
pfCntCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCntCongestion.setStatus("current")
_PfCntIpOption_Type = Counter64
_PfCntIpOption_Object = MibScalar
pfCntIpOption = _PfCntIpOption_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2, 9),
    _PfCntIpOption_Type()
)
pfCntIpOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCntIpOption.setStatus("current")
_PfCntProtoCksum_Type = Counter64
_PfCntProtoCksum_Object = MibScalar
pfCntProtoCksum = _PfCntProtoCksum_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2, 10),
    _PfCntProtoCksum_Type()
)
pfCntProtoCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCntProtoCksum.setStatus("current")
_PfCntStateMismatch_Type = Counter64
_PfCntStateMismatch_Object = MibScalar
pfCntStateMismatch = _PfCntStateMismatch_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2, 11),
    _PfCntStateMismatch_Type()
)
pfCntStateMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCntStateMismatch.setStatus("current")
_PfCntStateInsert_Type = Counter64
_PfCntStateInsert_Object = MibScalar
pfCntStateInsert = _PfCntStateInsert_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2, 12),
    _PfCntStateInsert_Type()
)
pfCntStateInsert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCntStateInsert.setStatus("current")
_PfCntStateLimit_Type = Counter64
_PfCntStateLimit_Object = MibScalar
pfCntStateLimit = _PfCntStateLimit_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2, 13),
    _PfCntStateLimit_Type()
)
pfCntStateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCntStateLimit.setStatus("current")
_PfCntSrcLimit_Type = Counter64
_PfCntSrcLimit_Object = MibScalar
pfCntSrcLimit = _PfCntSrcLimit_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2, 14),
    _PfCntSrcLimit_Type()
)
pfCntSrcLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCntSrcLimit.setStatus("current")
_PfCntSynproxy_Type = Counter64
_PfCntSynproxy_Object = MibScalar
pfCntSynproxy = _PfCntSynproxy_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2, 15),
    _PfCntSynproxy_Type()
)
pfCntSynproxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCntSynproxy.setStatus("current")
_PfCntTranslate_Type = Counter64
_PfCntTranslate_Object = MibScalar
pfCntTranslate = _PfCntTranslate_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2, 16),
    _PfCntTranslate_Type()
)
pfCntTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCntTranslate.setStatus("current")
_PfCntNoRoute_Type = Counter64
_PfCntNoRoute_Object = MibScalar
pfCntNoRoute = _PfCntNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 2, 17),
    _PfCntNoRoute_Type()
)
pfCntNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfCntNoRoute.setStatus("current")
_PfStateTable_ObjectIdentity = ObjectIdentity
pfStateTable = _PfStateTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 1, 3)
)
_PfStateCount_Type = Unsigned32
_PfStateCount_Object = MibScalar
pfStateCount = _PfStateCount_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 3, 1),
    _PfStateCount_Type()
)
pfStateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfStateCount.setStatus("current")
_PfStateSearches_Type = Counter64
_PfStateSearches_Object = MibScalar
pfStateSearches = _PfStateSearches_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 3, 2),
    _PfStateSearches_Type()
)
pfStateSearches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfStateSearches.setStatus("current")
_PfStateInserts_Type = Counter64
_PfStateInserts_Object = MibScalar
pfStateInserts = _PfStateInserts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 3, 3),
    _PfStateInserts_Type()
)
pfStateInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfStateInserts.setStatus("current")
_PfStateRemovals_Type = Counter64
_PfStateRemovals_Object = MibScalar
pfStateRemovals = _PfStateRemovals_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 3, 4),
    _PfStateRemovals_Type()
)
pfStateRemovals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfStateRemovals.setStatus("current")
_PfLogInterface_ObjectIdentity = ObjectIdentity
pfLogInterface = _PfLogInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 1, 4)
)
_PfLogIfName_Type = OctetString
_PfLogIfName_Object = MibScalar
pfLogIfName = _PfLogIfName_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 4, 1),
    _PfLogIfName_Type()
)
pfLogIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLogIfName.setStatus("current")
_PfLogIfIpBytesIn_Type = Counter64
_PfLogIfIpBytesIn_Object = MibScalar
pfLogIfIpBytesIn = _PfLogIfIpBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 4, 2),
    _PfLogIfIpBytesIn_Type()
)
pfLogIfIpBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLogIfIpBytesIn.setStatus("current")
_PfLogIfIpBytesOut_Type = Counter64
_PfLogIfIpBytesOut_Object = MibScalar
pfLogIfIpBytesOut = _PfLogIfIpBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 4, 3),
    _PfLogIfIpBytesOut_Type()
)
pfLogIfIpBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLogIfIpBytesOut.setStatus("current")
_PfLogIfIpPktsInPass_Type = Counter64
_PfLogIfIpPktsInPass_Object = MibScalar
pfLogIfIpPktsInPass = _PfLogIfIpPktsInPass_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 4, 4),
    _PfLogIfIpPktsInPass_Type()
)
pfLogIfIpPktsInPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLogIfIpPktsInPass.setStatus("current")
_PfLogIfIpPktsInDrop_Type = Counter64
_PfLogIfIpPktsInDrop_Object = MibScalar
pfLogIfIpPktsInDrop = _PfLogIfIpPktsInDrop_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 4, 5),
    _PfLogIfIpPktsInDrop_Type()
)
pfLogIfIpPktsInDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLogIfIpPktsInDrop.setStatus("current")
_PfLogIfIpPktsOutPass_Type = Counter64
_PfLogIfIpPktsOutPass_Object = MibScalar
pfLogIfIpPktsOutPass = _PfLogIfIpPktsOutPass_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 4, 6),
    _PfLogIfIpPktsOutPass_Type()
)
pfLogIfIpPktsOutPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLogIfIpPktsOutPass.setStatus("current")
_PfLogIfIpPktsOutDrop_Type = Counter64
_PfLogIfIpPktsOutDrop_Object = MibScalar
pfLogIfIpPktsOutDrop = _PfLogIfIpPktsOutDrop_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 4, 7),
    _PfLogIfIpPktsOutDrop_Type()
)
pfLogIfIpPktsOutDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLogIfIpPktsOutDrop.setStatus("current")
_PfLogIfIp6BytesIn_Type = Counter64
_PfLogIfIp6BytesIn_Object = MibScalar
pfLogIfIp6BytesIn = _PfLogIfIp6BytesIn_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 4, 8),
    _PfLogIfIp6BytesIn_Type()
)
pfLogIfIp6BytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLogIfIp6BytesIn.setStatus("current")
_PfLogIfIp6BytesOut_Type = Counter64
_PfLogIfIp6BytesOut_Object = MibScalar
pfLogIfIp6BytesOut = _PfLogIfIp6BytesOut_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 4, 9),
    _PfLogIfIp6BytesOut_Type()
)
pfLogIfIp6BytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLogIfIp6BytesOut.setStatus("current")
_PfLogIfIp6PktsInPass_Type = Counter64
_PfLogIfIp6PktsInPass_Object = MibScalar
pfLogIfIp6PktsInPass = _PfLogIfIp6PktsInPass_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 4, 10),
    _PfLogIfIp6PktsInPass_Type()
)
pfLogIfIp6PktsInPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLogIfIp6PktsInPass.setStatus("current")
_PfLogIfIp6PktsInDrop_Type = Counter64
_PfLogIfIp6PktsInDrop_Object = MibScalar
pfLogIfIp6PktsInDrop = _PfLogIfIp6PktsInDrop_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 4, 11),
    _PfLogIfIp6PktsInDrop_Type()
)
pfLogIfIp6PktsInDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLogIfIp6PktsInDrop.setStatus("current")
_PfLogIfIp6PktsOutPass_Type = Counter64
_PfLogIfIp6PktsOutPass_Object = MibScalar
pfLogIfIp6PktsOutPass = _PfLogIfIp6PktsOutPass_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 4, 12),
    _PfLogIfIp6PktsOutPass_Type()
)
pfLogIfIp6PktsOutPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLogIfIp6PktsOutPass.setStatus("current")
_PfLogIfIp6PktsOutDrop_Type = Counter64
_PfLogIfIp6PktsOutDrop_Object = MibScalar
pfLogIfIp6PktsOutDrop = _PfLogIfIp6PktsOutDrop_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 4, 13),
    _PfLogIfIp6PktsOutDrop_Type()
)
pfLogIfIp6PktsOutDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLogIfIp6PktsOutDrop.setStatus("current")
_PfSrcTracking_ObjectIdentity = ObjectIdentity
pfSrcTracking = _PfSrcTracking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 1, 5)
)
_PfSrcTrackCount_Type = Unsigned32
_PfSrcTrackCount_Object = MibScalar
pfSrcTrackCount = _PfSrcTrackCount_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 5, 1),
    _PfSrcTrackCount_Type()
)
pfSrcTrackCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfSrcTrackCount.setStatus("current")
_PfSrcTrackSearches_Type = Counter64
_PfSrcTrackSearches_Object = MibScalar
pfSrcTrackSearches = _PfSrcTrackSearches_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 5, 2),
    _PfSrcTrackSearches_Type()
)
pfSrcTrackSearches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfSrcTrackSearches.setStatus("current")
_PfSrcTrackInserts_Type = Counter64
_PfSrcTrackInserts_Object = MibScalar
pfSrcTrackInserts = _PfSrcTrackInserts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 5, 3),
    _PfSrcTrackInserts_Type()
)
pfSrcTrackInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfSrcTrackInserts.setStatus("current")
_PfSrcTrackRemovals_Type = Counter64
_PfSrcTrackRemovals_Object = MibScalar
pfSrcTrackRemovals = _PfSrcTrackRemovals_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 5, 4),
    _PfSrcTrackRemovals_Type()
)
pfSrcTrackRemovals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfSrcTrackRemovals.setStatus("current")
_PfLimits_ObjectIdentity = ObjectIdentity
pfLimits = _PfLimits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 1, 6)
)
_PfLimitStates_Type = Unsigned32
_PfLimitStates_Object = MibScalar
pfLimitStates = _PfLimitStates_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 6, 1),
    _PfLimitStates_Type()
)
pfLimitStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLimitStates.setStatus("current")
_PfLimitSourceNodes_Type = Unsigned32
_PfLimitSourceNodes_Object = MibScalar
pfLimitSourceNodes = _PfLimitSourceNodes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 6, 2),
    _PfLimitSourceNodes_Type()
)
pfLimitSourceNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLimitSourceNodes.setStatus("current")
_PfLimitFragments_Type = Unsigned32
_PfLimitFragments_Object = MibScalar
pfLimitFragments = _PfLimitFragments_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 6, 3),
    _PfLimitFragments_Type()
)
pfLimitFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLimitFragments.setStatus("current")
_PfLimitMaxTables_Type = Unsigned32
_PfLimitMaxTables_Object = MibScalar
pfLimitMaxTables = _PfLimitMaxTables_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 6, 4),
    _PfLimitMaxTables_Type()
)
pfLimitMaxTables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLimitMaxTables.setStatus("current")
_PfLimitMaxTableEntries_Type = Unsigned32
_PfLimitMaxTableEntries_Object = MibScalar
pfLimitMaxTableEntries = _PfLimitMaxTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 6, 5),
    _PfLimitMaxTableEntries_Type()
)
pfLimitMaxTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLimitMaxTableEntries.setStatus("current")
_PfTimeouts_ObjectIdentity = ObjectIdentity
pfTimeouts = _PfTimeouts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7)
)
_PfTimeoutTcpFirst_Type = Integer32
_PfTimeoutTcpFirst_Object = MibScalar
pfTimeoutTcpFirst = _PfTimeoutTcpFirst_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 1),
    _PfTimeoutTcpFirst_Type()
)
pfTimeoutTcpFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutTcpFirst.setStatus("current")
_PfTimeoutTcpOpening_Type = Integer32
_PfTimeoutTcpOpening_Object = MibScalar
pfTimeoutTcpOpening = _PfTimeoutTcpOpening_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 2),
    _PfTimeoutTcpOpening_Type()
)
pfTimeoutTcpOpening.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutTcpOpening.setStatus("current")
_PfTimeoutTcpEstablished_Type = Integer32
_PfTimeoutTcpEstablished_Object = MibScalar
pfTimeoutTcpEstablished = _PfTimeoutTcpEstablished_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 3),
    _PfTimeoutTcpEstablished_Type()
)
pfTimeoutTcpEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutTcpEstablished.setStatus("current")
_PfTimeoutTcpClosing_Type = Integer32
_PfTimeoutTcpClosing_Object = MibScalar
pfTimeoutTcpClosing = _PfTimeoutTcpClosing_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 4),
    _PfTimeoutTcpClosing_Type()
)
pfTimeoutTcpClosing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutTcpClosing.setStatus("current")
_PfTimeoutTcpFinWait_Type = Integer32
_PfTimeoutTcpFinWait_Object = MibScalar
pfTimeoutTcpFinWait = _PfTimeoutTcpFinWait_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 5),
    _PfTimeoutTcpFinWait_Type()
)
pfTimeoutTcpFinWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutTcpFinWait.setStatus("current")
_PfTimeoutTcpClosed_Type = Integer32
_PfTimeoutTcpClosed_Object = MibScalar
pfTimeoutTcpClosed = _PfTimeoutTcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 6),
    _PfTimeoutTcpClosed_Type()
)
pfTimeoutTcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutTcpClosed.setStatus("current")
_PfTimeoutUdpFirst_Type = Integer32
_PfTimeoutUdpFirst_Object = MibScalar
pfTimeoutUdpFirst = _PfTimeoutUdpFirst_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 7),
    _PfTimeoutUdpFirst_Type()
)
pfTimeoutUdpFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutUdpFirst.setStatus("current")
_PfTimeoutUdpSingle_Type = Integer32
_PfTimeoutUdpSingle_Object = MibScalar
pfTimeoutUdpSingle = _PfTimeoutUdpSingle_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 8),
    _PfTimeoutUdpSingle_Type()
)
pfTimeoutUdpSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutUdpSingle.setStatus("current")
_PfTimeoutUdpMultiple_Type = Integer32
_PfTimeoutUdpMultiple_Object = MibScalar
pfTimeoutUdpMultiple = _PfTimeoutUdpMultiple_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 9),
    _PfTimeoutUdpMultiple_Type()
)
pfTimeoutUdpMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutUdpMultiple.setStatus("current")
_PfTimeoutIcmpFirst_Type = Integer32
_PfTimeoutIcmpFirst_Object = MibScalar
pfTimeoutIcmpFirst = _PfTimeoutIcmpFirst_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 10),
    _PfTimeoutIcmpFirst_Type()
)
pfTimeoutIcmpFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutIcmpFirst.setStatus("current")
_PfTimeoutIcmpError_Type = Integer32
_PfTimeoutIcmpError_Object = MibScalar
pfTimeoutIcmpError = _PfTimeoutIcmpError_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 11),
    _PfTimeoutIcmpError_Type()
)
pfTimeoutIcmpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutIcmpError.setStatus("current")
_PfTimeoutOtherFirst_Type = Integer32
_PfTimeoutOtherFirst_Object = MibScalar
pfTimeoutOtherFirst = _PfTimeoutOtherFirst_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 12),
    _PfTimeoutOtherFirst_Type()
)
pfTimeoutOtherFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutOtherFirst.setStatus("current")
_PfTimeoutOtherSingle_Type = Integer32
_PfTimeoutOtherSingle_Object = MibScalar
pfTimeoutOtherSingle = _PfTimeoutOtherSingle_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 13),
    _PfTimeoutOtherSingle_Type()
)
pfTimeoutOtherSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutOtherSingle.setStatus("current")
_PfTimeoutOtherMultiple_Type = Integer32
_PfTimeoutOtherMultiple_Object = MibScalar
pfTimeoutOtherMultiple = _PfTimeoutOtherMultiple_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 14),
    _PfTimeoutOtherMultiple_Type()
)
pfTimeoutOtherMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutOtherMultiple.setStatus("current")
_PfTimeoutFragment_Type = Integer32
_PfTimeoutFragment_Object = MibScalar
pfTimeoutFragment = _PfTimeoutFragment_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 15),
    _PfTimeoutFragment_Type()
)
pfTimeoutFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutFragment.setStatus("current")
_PfTimeoutInterval_Type = Integer32
_PfTimeoutInterval_Object = MibScalar
pfTimeoutInterval = _PfTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 16),
    _PfTimeoutInterval_Type()
)
pfTimeoutInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutInterval.setStatus("current")
_PfTimeoutAdaptiveStart_Type = Integer32
_PfTimeoutAdaptiveStart_Object = MibScalar
pfTimeoutAdaptiveStart = _PfTimeoutAdaptiveStart_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 17),
    _PfTimeoutAdaptiveStart_Type()
)
pfTimeoutAdaptiveStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutAdaptiveStart.setStatus("current")
_PfTimeoutAdaptiveEnd_Type = Integer32
_PfTimeoutAdaptiveEnd_Object = MibScalar
pfTimeoutAdaptiveEnd = _PfTimeoutAdaptiveEnd_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 18),
    _PfTimeoutAdaptiveEnd_Type()
)
pfTimeoutAdaptiveEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutAdaptiveEnd.setStatus("current")
_PfTimeoutSrcTrack_Type = Integer32
_PfTimeoutSrcTrack_Object = MibScalar
pfTimeoutSrcTrack = _PfTimeoutSrcTrack_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 7, 19),
    _PfTimeoutSrcTrack_Type()
)
pfTimeoutSrcTrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTimeoutSrcTrack.setStatus("current")
_PfInterfaces_ObjectIdentity = ObjectIdentity
pfInterfaces = _PfInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8)
)
_PfIfNumber_Type = Integer32
_PfIfNumber_Object = MibScalar
pfIfNumber = _PfIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 1),
    _PfIfNumber_Type()
)
pfIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfNumber.setStatus("current")
_PfIfTable_Object = MibTable
pfIfTable = _PfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128)
)
if mibBuilder.loadTexts:
    pfIfTable.setStatus("current")
_PfIfEntry_Object = MibTableRow
pfIfEntry = _PfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1)
)
pfIfEntry.setIndexNames(
    (0, "OPENBSD-PF-MIB", "pfIfIndex"),
)
if mibBuilder.loadTexts:
    pfIfEntry.setStatus("current")


class _PfIfIndex_Type(Integer32):
    """Custom type pfIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PfIfIndex_Type.__name__ = "Integer32"
_PfIfIndex_Object = MibTableColumn
pfIfIndex = _PfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 1),
    _PfIfIndex_Type()
)
pfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfIndex.setStatus("current")
_PfIfDescr_Type = OctetString
_PfIfDescr_Object = MibTableColumn
pfIfDescr = _PfIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 2),
    _PfIfDescr_Type()
)
pfIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfDescr.setStatus("current")


class _PfIfType_Type(Integer32):
    """Custom type pfIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detached", 2),
          ("group", 0),
          ("instance", 1))
    )


_PfIfType_Type.__name__ = "Integer32"
_PfIfType_Object = MibTableColumn
pfIfType = _PfIfType_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 3),
    _PfIfType_Type()
)
pfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfType.setStatus("current")
_PfIfRefs_Type = Unsigned32
_PfIfRefs_Object = MibTableColumn
pfIfRefs = _PfIfRefs_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 4),
    _PfIfRefs_Type()
)
pfIfRefs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfRefs.setStatus("current")
_PfIfRules_Type = Unsigned32
_PfIfRules_Object = MibTableColumn
pfIfRules = _PfIfRules_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 5),
    _PfIfRules_Type()
)
pfIfRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfRules.setStatus("current")
_PfIfIn4PassPkts_Type = Counter64
_PfIfIn4PassPkts_Object = MibTableColumn
pfIfIn4PassPkts = _PfIfIn4PassPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 6),
    _PfIfIn4PassPkts_Type()
)
pfIfIn4PassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfIn4PassPkts.setStatus("current")
_PfIfIn4PassBytes_Type = Counter64
_PfIfIn4PassBytes_Object = MibTableColumn
pfIfIn4PassBytes = _PfIfIn4PassBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 7),
    _PfIfIn4PassBytes_Type()
)
pfIfIn4PassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfIn4PassBytes.setStatus("current")
_PfIfIn4BlockPkts_Type = Counter64
_PfIfIn4BlockPkts_Object = MibTableColumn
pfIfIn4BlockPkts = _PfIfIn4BlockPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 8),
    _PfIfIn4BlockPkts_Type()
)
pfIfIn4BlockPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfIn4BlockPkts.setStatus("current")
_PfIfIn4BlockBytes_Type = Counter64
_PfIfIn4BlockBytes_Object = MibTableColumn
pfIfIn4BlockBytes = _PfIfIn4BlockBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 9),
    _PfIfIn4BlockBytes_Type()
)
pfIfIn4BlockBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfIn4BlockBytes.setStatus("current")
_PfIfOut4PassPkts_Type = Counter64
_PfIfOut4PassPkts_Object = MibTableColumn
pfIfOut4PassPkts = _PfIfOut4PassPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 10),
    _PfIfOut4PassPkts_Type()
)
pfIfOut4PassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfOut4PassPkts.setStatus("current")
_PfIfOut4PassBytes_Type = Counter64
_PfIfOut4PassBytes_Object = MibTableColumn
pfIfOut4PassBytes = _PfIfOut4PassBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 11),
    _PfIfOut4PassBytes_Type()
)
pfIfOut4PassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfOut4PassBytes.setStatus("current")
_PfIfOut4BlockPkts_Type = Counter64
_PfIfOut4BlockPkts_Object = MibTableColumn
pfIfOut4BlockPkts = _PfIfOut4BlockPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 12),
    _PfIfOut4BlockPkts_Type()
)
pfIfOut4BlockPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfOut4BlockPkts.setStatus("current")
_PfIfOut4BlockBytes_Type = Counter64
_PfIfOut4BlockBytes_Object = MibTableColumn
pfIfOut4BlockBytes = _PfIfOut4BlockBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 13),
    _PfIfOut4BlockBytes_Type()
)
pfIfOut4BlockBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfOut4BlockBytes.setStatus("current")
_PfIfIn6PassPkts_Type = Counter64
_PfIfIn6PassPkts_Object = MibTableColumn
pfIfIn6PassPkts = _PfIfIn6PassPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 14),
    _PfIfIn6PassPkts_Type()
)
pfIfIn6PassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfIn6PassPkts.setStatus("current")
_PfIfIn6PassBytes_Type = Counter64
_PfIfIn6PassBytes_Object = MibTableColumn
pfIfIn6PassBytes = _PfIfIn6PassBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 15),
    _PfIfIn6PassBytes_Type()
)
pfIfIn6PassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfIn6PassBytes.setStatus("current")
_PfIfIn6BlockPkts_Type = Counter64
_PfIfIn6BlockPkts_Object = MibTableColumn
pfIfIn6BlockPkts = _PfIfIn6BlockPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 16),
    _PfIfIn6BlockPkts_Type()
)
pfIfIn6BlockPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfIn6BlockPkts.setStatus("current")
_PfIfIn6BlockBytes_Type = Counter64
_PfIfIn6BlockBytes_Object = MibTableColumn
pfIfIn6BlockBytes = _PfIfIn6BlockBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 17),
    _PfIfIn6BlockBytes_Type()
)
pfIfIn6BlockBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfIn6BlockBytes.setStatus("current")
_PfIfOut6PassPkts_Type = Counter64
_PfIfOut6PassPkts_Object = MibTableColumn
pfIfOut6PassPkts = _PfIfOut6PassPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 18),
    _PfIfOut6PassPkts_Type()
)
pfIfOut6PassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfOut6PassPkts.setStatus("current")
_PfIfOut6PassBytes_Type = Counter64
_PfIfOut6PassBytes_Object = MibTableColumn
pfIfOut6PassBytes = _PfIfOut6PassBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 19),
    _PfIfOut6PassBytes_Type()
)
pfIfOut6PassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfOut6PassBytes.setStatus("current")
_PfIfOut6BlockPkts_Type = Counter64
_PfIfOut6BlockPkts_Object = MibTableColumn
pfIfOut6BlockPkts = _PfIfOut6BlockPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 20),
    _PfIfOut6BlockPkts_Type()
)
pfIfOut6BlockPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfOut6BlockPkts.setStatus("current")
_PfIfOut6BlockBytes_Type = Counter64
_PfIfOut6BlockBytes_Object = MibTableColumn
pfIfOut6BlockBytes = _PfIfOut6BlockBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 21),
    _PfIfOut6BlockBytes_Type()
)
pfIfOut6BlockBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfIfOut6BlockBytes.setStatus("current")
_PfTables_ObjectIdentity = ObjectIdentity
pfTables = _PfTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9)
)
_PfTblNumber_Type = Integer32
_PfTblNumber_Object = MibScalar
pfTblNumber = _PfTblNumber_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 1),
    _PfTblNumber_Type()
)
pfTblNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblNumber.setStatus("current")
_PfTblTable_Object = MibTable
pfTblTable = _PfTblTable_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128)
)
if mibBuilder.loadTexts:
    pfTblTable.setStatus("current")
_PfTblEntry_Object = MibTableRow
pfTblEntry = _PfTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1)
)
pfTblEntry.setIndexNames(
    (0, "OPENBSD-PF-MIB", "pfTblIndex"),
)
if mibBuilder.loadTexts:
    pfTblEntry.setStatus("current")


class _PfTblIndex_Type(Integer32):
    """Custom type pfTblIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PfTblIndex_Type.__name__ = "Integer32"
_PfTblIndex_Object = MibTableColumn
pfTblIndex = _PfTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 1),
    _PfTblIndex_Type()
)
pfTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblIndex.setStatus("current")
_PfTblName_Type = OctetString
_PfTblName_Object = MibTableColumn
pfTblName = _PfTblName_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 2),
    _PfTblName_Type()
)
pfTblName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblName.setStatus("current")
_PfTblAddresses_Type = Integer32
_PfTblAddresses_Object = MibTableColumn
pfTblAddresses = _PfTblAddresses_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 3),
    _PfTblAddresses_Type()
)
pfTblAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAddresses.setStatus("current")
_PfTblAnchorRefs_Type = Integer32
_PfTblAnchorRefs_Object = MibTableColumn
pfTblAnchorRefs = _PfTblAnchorRefs_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 4),
    _PfTblAnchorRefs_Type()
)
pfTblAnchorRefs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAnchorRefs.setStatus("current")
_PfTblRuleRefs_Type = Integer32
_PfTblRuleRefs_Object = MibTableColumn
pfTblRuleRefs = _PfTblRuleRefs_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 5),
    _PfTblRuleRefs_Type()
)
pfTblRuleRefs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblRuleRefs.setStatus("current")
_PfTblEvalsMatch_Type = Counter64
_PfTblEvalsMatch_Object = MibTableColumn
pfTblEvalsMatch = _PfTblEvalsMatch_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 6),
    _PfTblEvalsMatch_Type()
)
pfTblEvalsMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblEvalsMatch.setStatus("current")
_PfTblEvalsNoMatch_Type = Counter64
_PfTblEvalsNoMatch_Object = MibTableColumn
pfTblEvalsNoMatch = _PfTblEvalsNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 7),
    _PfTblEvalsNoMatch_Type()
)
pfTblEvalsNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblEvalsNoMatch.setStatus("current")
_PfTblInPassPkts_Type = Counter64
_PfTblInPassPkts_Object = MibTableColumn
pfTblInPassPkts = _PfTblInPassPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 8),
    _PfTblInPassPkts_Type()
)
pfTblInPassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblInPassPkts.setStatus("current")
_PfTblInPassBytes_Type = Counter64
_PfTblInPassBytes_Object = MibTableColumn
pfTblInPassBytes = _PfTblInPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 9),
    _PfTblInPassBytes_Type()
)
pfTblInPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblInPassBytes.setStatus("current")
_PfTblInBlockPkts_Type = Counter64
_PfTblInBlockPkts_Object = MibTableColumn
pfTblInBlockPkts = _PfTblInBlockPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 10),
    _PfTblInBlockPkts_Type()
)
pfTblInBlockPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblInBlockPkts.setStatus("current")
_PfTblInBlockBytes_Type = Counter64
_PfTblInBlockBytes_Object = MibTableColumn
pfTblInBlockBytes = _PfTblInBlockBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 11),
    _PfTblInBlockBytes_Type()
)
pfTblInBlockBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblInBlockBytes.setStatus("current")
_PfTblInXPassPkts_Type = Counter64
_PfTblInXPassPkts_Object = MibTableColumn
pfTblInXPassPkts = _PfTblInXPassPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 12),
    _PfTblInXPassPkts_Type()
)
pfTblInXPassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblInXPassPkts.setStatus("current")
_PfTblInXPassBytes_Type = Counter64
_PfTblInXPassBytes_Object = MibTableColumn
pfTblInXPassBytes = _PfTblInXPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 13),
    _PfTblInXPassBytes_Type()
)
pfTblInXPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblInXPassBytes.setStatus("current")
_PfTblOutPassPkts_Type = Counter64
_PfTblOutPassPkts_Object = MibTableColumn
pfTblOutPassPkts = _PfTblOutPassPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 14),
    _PfTblOutPassPkts_Type()
)
pfTblOutPassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblOutPassPkts.setStatus("current")
_PfTblOutPassBytes_Type = Counter64
_PfTblOutPassBytes_Object = MibTableColumn
pfTblOutPassBytes = _PfTblOutPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 15),
    _PfTblOutPassBytes_Type()
)
pfTblOutPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblOutPassBytes.setStatus("current")
_PfTblOutBlockPkts_Type = Counter64
_PfTblOutBlockPkts_Object = MibTableColumn
pfTblOutBlockPkts = _PfTblOutBlockPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 16),
    _PfTblOutBlockPkts_Type()
)
pfTblOutBlockPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblOutBlockPkts.setStatus("current")
_PfTblOutBlockBytes_Type = Counter64
_PfTblOutBlockBytes_Object = MibTableColumn
pfTblOutBlockBytes = _PfTblOutBlockBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 17),
    _PfTblOutBlockBytes_Type()
)
pfTblOutBlockBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblOutBlockBytes.setStatus("current")
_PfTblOutXPassPkts_Type = Counter64
_PfTblOutXPassPkts_Object = MibTableColumn
pfTblOutXPassPkts = _PfTblOutXPassPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 18),
    _PfTblOutXPassPkts_Type()
)
pfTblOutXPassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblOutXPassPkts.setStatus("current")
_PfTblOutXPassBytes_Type = Counter64
_PfTblOutXPassBytes_Object = MibTableColumn
pfTblOutXPassBytes = _PfTblOutXPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 19),
    _PfTblOutXPassBytes_Type()
)
pfTblOutXPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblOutXPassBytes.setStatus("current")
_PfTblStatsCleared_Type = TimeTicks
_PfTblStatsCleared_Object = MibTableColumn
pfTblStatsCleared = _PfTblStatsCleared_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 20),
    _PfTblStatsCleared_Type()
)
pfTblStatsCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblStatsCleared.setStatus("current")
if mibBuilder.loadTexts:
    pfTblStatsCleared.setUnits("1/100th of a Second")
_PfTblInMatchPkts_Type = Counter64
_PfTblInMatchPkts_Object = MibTableColumn
pfTblInMatchPkts = _PfTblInMatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 21),
    _PfTblInMatchPkts_Type()
)
pfTblInMatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblInMatchPkts.setStatus("current")
_PfTblInMatchBytes_Type = Counter64
_PfTblInMatchBytes_Object = MibTableColumn
pfTblInMatchBytes = _PfTblInMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 22),
    _PfTblInMatchBytes_Type()
)
pfTblInMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblInMatchBytes.setStatus("current")
_PfTblOutMatchPkts_Type = Counter64
_PfTblOutMatchPkts_Object = MibTableColumn
pfTblOutMatchPkts = _PfTblOutMatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 23),
    _PfTblOutMatchPkts_Type()
)
pfTblOutMatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblOutMatchPkts.setStatus("current")
_PfTblOutMatchBytes_Type = Counter64
_PfTblOutMatchBytes_Object = MibTableColumn
pfTblOutMatchBytes = _PfTblOutMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 24),
    _PfTblOutMatchBytes_Type()
)
pfTblOutMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblOutMatchBytes.setStatus("current")
_PfTblAddrTable_Object = MibTable
pfTblAddrTable = _PfTblAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129)
)
if mibBuilder.loadTexts:
    pfTblAddrTable.setStatus("current")
_PfTblAddrEntry_Object = MibTableRow
pfTblAddrEntry = _PfTblAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1)
)
pfTblAddrEntry.setIndexNames(
    (0, "OPENBSD-PF-MIB", "pfTblAddrTblIndex"),
    (0, "OPENBSD-PF-MIB", "pfTblAddrNet"),
    (0, "OPENBSD-PF-MIB", "pfTblAddrMask"),
)
if mibBuilder.loadTexts:
    pfTblAddrEntry.setStatus("current")


class _PfTblAddrTblIndex_Type(Integer32):
    """Custom type pfTblAddrTblIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PfTblAddrTblIndex_Type.__name__ = "Integer32"
_PfTblAddrTblIndex_Object = MibTableColumn
pfTblAddrTblIndex = _PfTblAddrTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 1),
    _PfTblAddrTblIndex_Type()
)
pfTblAddrTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAddrTblIndex.setStatus("current")
_PfTblAddrNet_Type = IpAddress
_PfTblAddrNet_Object = MibTableColumn
pfTblAddrNet = _PfTblAddrNet_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 2),
    _PfTblAddrNet_Type()
)
pfTblAddrNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAddrNet.setStatus("current")


class _PfTblAddrMask_Type(Integer32):
    """Custom type pfTblAddrMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_PfTblAddrMask_Type.__name__ = "Integer32"
_PfTblAddrMask_Object = MibTableColumn
pfTblAddrMask = _PfTblAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 3),
    _PfTblAddrMask_Type()
)
pfTblAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAddrMask.setStatus("current")
_PfTblAddrCleared_Type = TimeTicks
_PfTblAddrCleared_Object = MibTableColumn
pfTblAddrCleared = _PfTblAddrCleared_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 4),
    _PfTblAddrCleared_Type()
)
pfTblAddrCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAddrCleared.setStatus("current")
if mibBuilder.loadTexts:
    pfTblAddrCleared.setUnits("1/100th of a Second")
_PfTblAddrInBlockPkts_Type = Counter64
_PfTblAddrInBlockPkts_Object = MibTableColumn
pfTblAddrInBlockPkts = _PfTblAddrInBlockPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 5),
    _PfTblAddrInBlockPkts_Type()
)
pfTblAddrInBlockPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAddrInBlockPkts.setStatus("current")
_PfTblAddrInBlockBytes_Type = Counter64
_PfTblAddrInBlockBytes_Object = MibTableColumn
pfTblAddrInBlockBytes = _PfTblAddrInBlockBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 6),
    _PfTblAddrInBlockBytes_Type()
)
pfTblAddrInBlockBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAddrInBlockBytes.setStatus("current")
_PfTblAddrInPassPkts_Type = Counter64
_PfTblAddrInPassPkts_Object = MibTableColumn
pfTblAddrInPassPkts = _PfTblAddrInPassPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 7),
    _PfTblAddrInPassPkts_Type()
)
pfTblAddrInPassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAddrInPassPkts.setStatus("current")
_PfTblAddrInPassBytes_Type = Counter64
_PfTblAddrInPassBytes_Object = MibTableColumn
pfTblAddrInPassBytes = _PfTblAddrInPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 8),
    _PfTblAddrInPassBytes_Type()
)
pfTblAddrInPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAddrInPassBytes.setStatus("current")
_PfTblAddrOutBlockPkts_Type = Counter64
_PfTblAddrOutBlockPkts_Object = MibTableColumn
pfTblAddrOutBlockPkts = _PfTblAddrOutBlockPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 9),
    _PfTblAddrOutBlockPkts_Type()
)
pfTblAddrOutBlockPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAddrOutBlockPkts.setStatus("current")
_PfTblAddrOutBlockBytes_Type = Counter64
_PfTblAddrOutBlockBytes_Object = MibTableColumn
pfTblAddrOutBlockBytes = _PfTblAddrOutBlockBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 10),
    _PfTblAddrOutBlockBytes_Type()
)
pfTblAddrOutBlockBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAddrOutBlockBytes.setStatus("current")
_PfTblAddrOutPassPkts_Type = Counter64
_PfTblAddrOutPassPkts_Object = MibTableColumn
pfTblAddrOutPassPkts = _PfTblAddrOutPassPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 11),
    _PfTblAddrOutPassPkts_Type()
)
pfTblAddrOutPassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAddrOutPassPkts.setStatus("current")
_PfTblAddrOutPassBytes_Type = Counter64
_PfTblAddrOutPassBytes_Object = MibTableColumn
pfTblAddrOutPassBytes = _PfTblAddrOutPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 12),
    _PfTblAddrOutPassBytes_Type()
)
pfTblAddrOutPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAddrOutPassBytes.setStatus("current")
_PfTblAddrInMatchPkts_Type = Counter64
_PfTblAddrInMatchPkts_Object = MibTableColumn
pfTblAddrInMatchPkts = _PfTblAddrInMatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 13),
    _PfTblAddrInMatchPkts_Type()
)
pfTblAddrInMatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAddrInMatchPkts.setStatus("current")
_PfTblAddrInMatchBytes_Type = Counter64
_PfTblAddrInMatchBytes_Object = MibTableColumn
pfTblAddrInMatchBytes = _PfTblAddrInMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 14),
    _PfTblAddrInMatchBytes_Type()
)
pfTblAddrInMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAddrInMatchBytes.setStatus("current")
_PfTblAddrOutMatchPkts_Type = Counter64
_PfTblAddrOutMatchPkts_Object = MibTableColumn
pfTblAddrOutMatchPkts = _PfTblAddrOutMatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 15),
    _PfTblAddrOutMatchPkts_Type()
)
pfTblAddrOutMatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAddrOutMatchPkts.setStatus("current")
_PfTblAddrOutMatchBytes_Type = Counter64
_PfTblAddrOutMatchBytes_Object = MibTableColumn
pfTblAddrOutMatchBytes = _PfTblAddrOutMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 16),
    _PfTblAddrOutMatchBytes_Type()
)
pfTblAddrOutMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfTblAddrOutMatchBytes.setStatus("current")
_PfLabels_ObjectIdentity = ObjectIdentity
pfLabels = _PfLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 1, 10)
)
_PfLabelNumber_Type = Integer32
_PfLabelNumber_Object = MibScalar
pfLabelNumber = _PfLabelNumber_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 10, 1),
    _PfLabelNumber_Type()
)
pfLabelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLabelNumber.setStatus("current")
_PfLabelTable_Object = MibTable
pfLabelTable = _PfLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 10, 128)
)
if mibBuilder.loadTexts:
    pfLabelTable.setStatus("current")
_PfLabelEntry_Object = MibTableRow
pfLabelEntry = _PfLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1)
)
pfLabelEntry.setIndexNames(
    (0, "OPENBSD-PF-MIB", "pfLabelIndex"),
)
if mibBuilder.loadTexts:
    pfLabelEntry.setStatus("current")


class _PfLabelIndex_Type(Integer32):
    """Custom type pfLabelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PfLabelIndex_Type.__name__ = "Integer32"
_PfLabelIndex_Object = MibTableColumn
pfLabelIndex = _PfLabelIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 1),
    _PfLabelIndex_Type()
)
pfLabelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLabelIndex.setStatus("current")
_PfLabelName_Type = OctetString
_PfLabelName_Object = MibTableColumn
pfLabelName = _PfLabelName_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 2),
    _PfLabelName_Type()
)
pfLabelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLabelName.setStatus("current")
_PfLabelEvals_Type = Counter64
_PfLabelEvals_Object = MibTableColumn
pfLabelEvals = _PfLabelEvals_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 3),
    _PfLabelEvals_Type()
)
pfLabelEvals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLabelEvals.setStatus("current")
_PfLabelPkts_Type = Counter64
_PfLabelPkts_Object = MibTableColumn
pfLabelPkts = _PfLabelPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 4),
    _PfLabelPkts_Type()
)
pfLabelPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLabelPkts.setStatus("current")
_PfLabelBytes_Type = Counter64
_PfLabelBytes_Object = MibTableColumn
pfLabelBytes = _PfLabelBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 5),
    _PfLabelBytes_Type()
)
pfLabelBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLabelBytes.setStatus("current")
_PfLabelInPkts_Type = Counter64
_PfLabelInPkts_Object = MibTableColumn
pfLabelInPkts = _PfLabelInPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 6),
    _PfLabelInPkts_Type()
)
pfLabelInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLabelInPkts.setStatus("current")
_PfLabelInBytes_Type = Counter64
_PfLabelInBytes_Object = MibTableColumn
pfLabelInBytes = _PfLabelInBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 7),
    _PfLabelInBytes_Type()
)
pfLabelInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLabelInBytes.setStatus("current")
_PfLabelOutPkts_Type = Counter64
_PfLabelOutPkts_Object = MibTableColumn
pfLabelOutPkts = _PfLabelOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 8),
    _PfLabelOutPkts_Type()
)
pfLabelOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLabelOutPkts.setStatus("current")
_PfLabelOutBytes_Type = Counter64
_PfLabelOutBytes_Object = MibTableColumn
pfLabelOutBytes = _PfLabelOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 9),
    _PfLabelOutBytes_Type()
)
pfLabelOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLabelOutBytes.setStatus("current")
_PfLabelTotalStates_Type = Counter32
_PfLabelTotalStates_Object = MibTableColumn
pfLabelTotalStates = _PfLabelTotalStates_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 10),
    _PfLabelTotalStates_Type()
)
pfLabelTotalStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfLabelTotalStates.setStatus("current")
_PfsyncStats_ObjectIdentity = ObjectIdentity
pfsyncStats = _PfsyncStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 1, 11)
)
_PfsyncIpPktsRecv_Type = Counter64
_PfsyncIpPktsRecv_Object = MibScalar
pfsyncIpPktsRecv = _PfsyncIpPktsRecv_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 11, 1),
    _PfsyncIpPktsRecv_Type()
)
pfsyncIpPktsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfsyncIpPktsRecv.setStatus("current")
_PfsyncIp6PktsRecv_Type = Counter64
_PfsyncIp6PktsRecv_Object = MibScalar
pfsyncIp6PktsRecv = _PfsyncIp6PktsRecv_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 11, 2),
    _PfsyncIp6PktsRecv_Type()
)
pfsyncIp6PktsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfsyncIp6PktsRecv.setStatus("current")
_PfsyncPktDiscardsForBadInterface_Type = Counter64
_PfsyncPktDiscardsForBadInterface_Object = MibScalar
pfsyncPktDiscardsForBadInterface = _PfsyncPktDiscardsForBadInterface_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 11, 3),
    _PfsyncPktDiscardsForBadInterface_Type()
)
pfsyncPktDiscardsForBadInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfsyncPktDiscardsForBadInterface.setStatus("current")
_PfsyncPktDiscardsForBadTtl_Type = Counter64
_PfsyncPktDiscardsForBadTtl_Object = MibScalar
pfsyncPktDiscardsForBadTtl = _PfsyncPktDiscardsForBadTtl_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 11, 4),
    _PfsyncPktDiscardsForBadTtl_Type()
)
pfsyncPktDiscardsForBadTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfsyncPktDiscardsForBadTtl.setStatus("current")
_PfsyncPktShorterThanHeader_Type = Counter64
_PfsyncPktShorterThanHeader_Object = MibScalar
pfsyncPktShorterThanHeader = _PfsyncPktShorterThanHeader_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 11, 5),
    _PfsyncPktShorterThanHeader_Type()
)
pfsyncPktShorterThanHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfsyncPktShorterThanHeader.setStatus("current")
_PfsyncPktDiscardsForBadVersion_Type = Counter64
_PfsyncPktDiscardsForBadVersion_Object = MibScalar
pfsyncPktDiscardsForBadVersion = _PfsyncPktDiscardsForBadVersion_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 11, 6),
    _PfsyncPktDiscardsForBadVersion_Type()
)
pfsyncPktDiscardsForBadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfsyncPktDiscardsForBadVersion.setStatus("current")
_PfsyncPktDiscardsForBadAction_Type = Counter64
_PfsyncPktDiscardsForBadAction_Object = MibScalar
pfsyncPktDiscardsForBadAction = _PfsyncPktDiscardsForBadAction_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 11, 7),
    _PfsyncPktDiscardsForBadAction_Type()
)
pfsyncPktDiscardsForBadAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfsyncPktDiscardsForBadAction.setStatus("current")
_PfsyncPktDiscardsForBadLength_Type = Counter64
_PfsyncPktDiscardsForBadLength_Object = MibScalar
pfsyncPktDiscardsForBadLength = _PfsyncPktDiscardsForBadLength_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 11, 8),
    _PfsyncPktDiscardsForBadLength_Type()
)
pfsyncPktDiscardsForBadLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfsyncPktDiscardsForBadLength.setStatus("current")
_PfsyncPktDiscardsForBadAuth_Type = Counter64
_PfsyncPktDiscardsForBadAuth_Object = MibScalar
pfsyncPktDiscardsForBadAuth = _PfsyncPktDiscardsForBadAuth_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 11, 9),
    _PfsyncPktDiscardsForBadAuth_Type()
)
pfsyncPktDiscardsForBadAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfsyncPktDiscardsForBadAuth.setStatus("current")
_PfsyncPktDiscardsForStaleState_Type = Counter64
_PfsyncPktDiscardsForStaleState_Object = MibScalar
pfsyncPktDiscardsForStaleState = _PfsyncPktDiscardsForStaleState_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 11, 10),
    _PfsyncPktDiscardsForStaleState_Type()
)
pfsyncPktDiscardsForStaleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfsyncPktDiscardsForStaleState.setStatus("current")
_PfsyncPktDiscardsForBadValues_Type = Counter64
_PfsyncPktDiscardsForBadValues_Object = MibScalar
pfsyncPktDiscardsForBadValues = _PfsyncPktDiscardsForBadValues_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 11, 11),
    _PfsyncPktDiscardsForBadValues_Type()
)
pfsyncPktDiscardsForBadValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfsyncPktDiscardsForBadValues.setStatus("current")
_PfsyncPktDiscardsForBadState_Type = Counter64
_PfsyncPktDiscardsForBadState_Object = MibScalar
pfsyncPktDiscardsForBadState = _PfsyncPktDiscardsForBadState_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 11, 12),
    _PfsyncPktDiscardsForBadState_Type()
)
pfsyncPktDiscardsForBadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfsyncPktDiscardsForBadState.setStatus("current")
_PfsyncIpPktsSent_Type = Counter64
_PfsyncIpPktsSent_Object = MibScalar
pfsyncIpPktsSent = _PfsyncIpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 11, 13),
    _PfsyncIpPktsSent_Type()
)
pfsyncIpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfsyncIpPktsSent.setStatus("current")
_PfsyncIp6PktsSent_Type = Counter64
_PfsyncIp6PktsSent_Object = MibScalar
pfsyncIp6PktsSent = _PfsyncIp6PktsSent_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 11, 14),
    _PfsyncIp6PktsSent_Type()
)
pfsyncIp6PktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfsyncIp6PktsSent.setStatus("current")
_PfsyncNoMemory_Type = Counter64
_PfsyncNoMemory_Object = MibScalar
pfsyncNoMemory = _PfsyncNoMemory_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 11, 15),
    _PfsyncNoMemory_Type()
)
pfsyncNoMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfsyncNoMemory.setStatus("current")
_PfsyncOutputErrors_Type = Counter64
_PfsyncOutputErrors_Object = MibScalar
pfsyncOutputErrors = _PfsyncOutputErrors_Object(
    (1, 3, 6, 1, 4, 1, 30155, 1, 11, 16),
    _PfsyncOutputErrors_Type()
)
pfsyncOutputErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfsyncOutputErrors.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPENBSD-PF-MIB",
    **{"pfMIBObjects": pfMIBObjects,
       "pfInfo": pfInfo,
       "pfRunning": pfRunning,
       "pfRuntime": pfRuntime,
       "pfDebug": pfDebug,
       "pfHostid": pfHostid,
       "pfCounters": pfCounters,
       "pfCntMatch": pfCntMatch,
       "pfCntBadOffset": pfCntBadOffset,
       "pfCntFragment": pfCntFragment,
       "pfCntShort": pfCntShort,
       "pfCntNormalize": pfCntNormalize,
       "pfCntMemory": pfCntMemory,
       "pfCntTimestamp": pfCntTimestamp,
       "pfCntCongestion": pfCntCongestion,
       "pfCntIpOption": pfCntIpOption,
       "pfCntProtoCksum": pfCntProtoCksum,
       "pfCntStateMismatch": pfCntStateMismatch,
       "pfCntStateInsert": pfCntStateInsert,
       "pfCntStateLimit": pfCntStateLimit,
       "pfCntSrcLimit": pfCntSrcLimit,
       "pfCntSynproxy": pfCntSynproxy,
       "pfCntTranslate": pfCntTranslate,
       "pfCntNoRoute": pfCntNoRoute,
       "pfStateTable": pfStateTable,
       "pfStateCount": pfStateCount,
       "pfStateSearches": pfStateSearches,
       "pfStateInserts": pfStateInserts,
       "pfStateRemovals": pfStateRemovals,
       "pfLogInterface": pfLogInterface,
       "pfLogIfName": pfLogIfName,
       "pfLogIfIpBytesIn": pfLogIfIpBytesIn,
       "pfLogIfIpBytesOut": pfLogIfIpBytesOut,
       "pfLogIfIpPktsInPass": pfLogIfIpPktsInPass,
       "pfLogIfIpPktsInDrop": pfLogIfIpPktsInDrop,
       "pfLogIfIpPktsOutPass": pfLogIfIpPktsOutPass,
       "pfLogIfIpPktsOutDrop": pfLogIfIpPktsOutDrop,
       "pfLogIfIp6BytesIn": pfLogIfIp6BytesIn,
       "pfLogIfIp6BytesOut": pfLogIfIp6BytesOut,
       "pfLogIfIp6PktsInPass": pfLogIfIp6PktsInPass,
       "pfLogIfIp6PktsInDrop": pfLogIfIp6PktsInDrop,
       "pfLogIfIp6PktsOutPass": pfLogIfIp6PktsOutPass,
       "pfLogIfIp6PktsOutDrop": pfLogIfIp6PktsOutDrop,
       "pfSrcTracking": pfSrcTracking,
       "pfSrcTrackCount": pfSrcTrackCount,
       "pfSrcTrackSearches": pfSrcTrackSearches,
       "pfSrcTrackInserts": pfSrcTrackInserts,
       "pfSrcTrackRemovals": pfSrcTrackRemovals,
       "pfLimits": pfLimits,
       "pfLimitStates": pfLimitStates,
       "pfLimitSourceNodes": pfLimitSourceNodes,
       "pfLimitFragments": pfLimitFragments,
       "pfLimitMaxTables": pfLimitMaxTables,
       "pfLimitMaxTableEntries": pfLimitMaxTableEntries,
       "pfTimeouts": pfTimeouts,
       "pfTimeoutTcpFirst": pfTimeoutTcpFirst,
       "pfTimeoutTcpOpening": pfTimeoutTcpOpening,
       "pfTimeoutTcpEstablished": pfTimeoutTcpEstablished,
       "pfTimeoutTcpClosing": pfTimeoutTcpClosing,
       "pfTimeoutTcpFinWait": pfTimeoutTcpFinWait,
       "pfTimeoutTcpClosed": pfTimeoutTcpClosed,
       "pfTimeoutUdpFirst": pfTimeoutUdpFirst,
       "pfTimeoutUdpSingle": pfTimeoutUdpSingle,
       "pfTimeoutUdpMultiple": pfTimeoutUdpMultiple,
       "pfTimeoutIcmpFirst": pfTimeoutIcmpFirst,
       "pfTimeoutIcmpError": pfTimeoutIcmpError,
       "pfTimeoutOtherFirst": pfTimeoutOtherFirst,
       "pfTimeoutOtherSingle": pfTimeoutOtherSingle,
       "pfTimeoutOtherMultiple": pfTimeoutOtherMultiple,
       "pfTimeoutFragment": pfTimeoutFragment,
       "pfTimeoutInterval": pfTimeoutInterval,
       "pfTimeoutAdaptiveStart": pfTimeoutAdaptiveStart,
       "pfTimeoutAdaptiveEnd": pfTimeoutAdaptiveEnd,
       "pfTimeoutSrcTrack": pfTimeoutSrcTrack,
       "pfInterfaces": pfInterfaces,
       "pfIfNumber": pfIfNumber,
       "pfIfTable": pfIfTable,
       "pfIfEntry": pfIfEntry,
       "pfIfIndex": pfIfIndex,
       "pfIfDescr": pfIfDescr,
       "pfIfType": pfIfType,
       "pfIfRefs": pfIfRefs,
       "pfIfRules": pfIfRules,
       "pfIfIn4PassPkts": pfIfIn4PassPkts,
       "pfIfIn4PassBytes": pfIfIn4PassBytes,
       "pfIfIn4BlockPkts": pfIfIn4BlockPkts,
       "pfIfIn4BlockBytes": pfIfIn4BlockBytes,
       "pfIfOut4PassPkts": pfIfOut4PassPkts,
       "pfIfOut4PassBytes": pfIfOut4PassBytes,
       "pfIfOut4BlockPkts": pfIfOut4BlockPkts,
       "pfIfOut4BlockBytes": pfIfOut4BlockBytes,
       "pfIfIn6PassPkts": pfIfIn6PassPkts,
       "pfIfIn6PassBytes": pfIfIn6PassBytes,
       "pfIfIn6BlockPkts": pfIfIn6BlockPkts,
       "pfIfIn6BlockBytes": pfIfIn6BlockBytes,
       "pfIfOut6PassPkts": pfIfOut6PassPkts,
       "pfIfOut6PassBytes": pfIfOut6PassBytes,
       "pfIfOut6BlockPkts": pfIfOut6BlockPkts,
       "pfIfOut6BlockBytes": pfIfOut6BlockBytes,
       "pfTables": pfTables,
       "pfTblNumber": pfTblNumber,
       "pfTblTable": pfTblTable,
       "pfTblEntry": pfTblEntry,
       "pfTblIndex": pfTblIndex,
       "pfTblName": pfTblName,
       "pfTblAddresses": pfTblAddresses,
       "pfTblAnchorRefs": pfTblAnchorRefs,
       "pfTblRuleRefs": pfTblRuleRefs,
       "pfTblEvalsMatch": pfTblEvalsMatch,
       "pfTblEvalsNoMatch": pfTblEvalsNoMatch,
       "pfTblInPassPkts": pfTblInPassPkts,
       "pfTblInPassBytes": pfTblInPassBytes,
       "pfTblInBlockPkts": pfTblInBlockPkts,
       "pfTblInBlockBytes": pfTblInBlockBytes,
       "pfTblInXPassPkts": pfTblInXPassPkts,
       "pfTblInXPassBytes": pfTblInXPassBytes,
       "pfTblOutPassPkts": pfTblOutPassPkts,
       "pfTblOutPassBytes": pfTblOutPassBytes,
       "pfTblOutBlockPkts": pfTblOutBlockPkts,
       "pfTblOutBlockBytes": pfTblOutBlockBytes,
       "pfTblOutXPassPkts": pfTblOutXPassPkts,
       "pfTblOutXPassBytes": pfTblOutXPassBytes,
       "pfTblStatsCleared": pfTblStatsCleared,
       "pfTblInMatchPkts": pfTblInMatchPkts,
       "pfTblInMatchBytes": pfTblInMatchBytes,
       "pfTblOutMatchPkts": pfTblOutMatchPkts,
       "pfTblOutMatchBytes": pfTblOutMatchBytes,
       "pfTblAddrTable": pfTblAddrTable,
       "pfTblAddrEntry": pfTblAddrEntry,
       "pfTblAddrTblIndex": pfTblAddrTblIndex,
       "pfTblAddrNet": pfTblAddrNet,
       "pfTblAddrMask": pfTblAddrMask,
       "pfTblAddrCleared": pfTblAddrCleared,
       "pfTblAddrInBlockPkts": pfTblAddrInBlockPkts,
       "pfTblAddrInBlockBytes": pfTblAddrInBlockBytes,
       "pfTblAddrInPassPkts": pfTblAddrInPassPkts,
       "pfTblAddrInPassBytes": pfTblAddrInPassBytes,
       "pfTblAddrOutBlockPkts": pfTblAddrOutBlockPkts,
       "pfTblAddrOutBlockBytes": pfTblAddrOutBlockBytes,
       "pfTblAddrOutPassPkts": pfTblAddrOutPassPkts,
       "pfTblAddrOutPassBytes": pfTblAddrOutPassBytes,
       "pfTblAddrInMatchPkts": pfTblAddrInMatchPkts,
       "pfTblAddrInMatchBytes": pfTblAddrInMatchBytes,
       "pfTblAddrOutMatchPkts": pfTblAddrOutMatchPkts,
       "pfTblAddrOutMatchBytes": pfTblAddrOutMatchBytes,
       "pfLabels": pfLabels,
       "pfLabelNumber": pfLabelNumber,
       "pfLabelTable": pfLabelTable,
       "pfLabelEntry": pfLabelEntry,
       "pfLabelIndex": pfLabelIndex,
       "pfLabelName": pfLabelName,
       "pfLabelEvals": pfLabelEvals,
       "pfLabelPkts": pfLabelPkts,
       "pfLabelBytes": pfLabelBytes,
       "pfLabelInPkts": pfLabelInPkts,
       "pfLabelInBytes": pfLabelInBytes,
       "pfLabelOutPkts": pfLabelOutPkts,
       "pfLabelOutBytes": pfLabelOutBytes,
       "pfLabelTotalStates": pfLabelTotalStates,
       "pfsyncStats": pfsyncStats,
       "pfsyncIpPktsRecv": pfsyncIpPktsRecv,
       "pfsyncIp6PktsRecv": pfsyncIp6PktsRecv,
       "pfsyncPktDiscardsForBadInterface": pfsyncPktDiscardsForBadInterface,
       "pfsyncPktDiscardsForBadTtl": pfsyncPktDiscardsForBadTtl,
       "pfsyncPktShorterThanHeader": pfsyncPktShorterThanHeader,
       "pfsyncPktDiscardsForBadVersion": pfsyncPktDiscardsForBadVersion,
       "pfsyncPktDiscardsForBadAction": pfsyncPktDiscardsForBadAction,
       "pfsyncPktDiscardsForBadLength": pfsyncPktDiscardsForBadLength,
       "pfsyncPktDiscardsForBadAuth": pfsyncPktDiscardsForBadAuth,
       "pfsyncPktDiscardsForStaleState": pfsyncPktDiscardsForStaleState,
       "pfsyncPktDiscardsForBadValues": pfsyncPktDiscardsForBadValues,
       "pfsyncPktDiscardsForBadState": pfsyncPktDiscardsForBadState,
       "pfsyncIpPktsSent": pfsyncIpPktsSent,
       "pfsyncIp6PktsSent": pfsyncIp6PktsSent,
       "pfsyncNoMemory": pfsyncNoMemory,
       "pfsyncOutputErrors": pfsyncOutputErrors}
)
