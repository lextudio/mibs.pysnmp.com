# SNMP MIB module (TIARARIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARARIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:46 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tiaraMgmt,) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-SMI",
    "tiaraMgmt")


# MODULE-IDENTITY

tiaraRipMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TiaraRipGlobals_ObjectIdentity = ObjectIdentity
tiaraRipGlobals = _TiaraRipGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 1)
)
_TiaraRoutingEnable_Type = TruthValue
_TiaraRoutingEnable_Object = MibScalar
tiaraRoutingEnable = _TiaraRoutingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 1, 1),
    _TiaraRoutingEnable_Type()
)
tiaraRoutingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tiaraRoutingEnable.setStatus("current")


class _TiaraRipGlobalEnable_Type(TruthValue):
    """Custom type tiaraRipGlobalEnable based on TruthValue"""


_TiaraRipGlobalEnable_Object = MibScalar
tiaraRipGlobalEnable = _TiaraRipGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 1, 2),
    _TiaraRipGlobalEnable_Type()
)
tiaraRipGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tiaraRipGlobalEnable.setStatus("current")


class _TiaraRipGlobalUseTrustedNeighbour_Type(TruthValue):
    """Custom type tiaraRipGlobalUseTrustedNeighbour based on TruthValue"""


_TiaraRipGlobalUseTrustedNeighbour_Object = MibScalar
tiaraRipGlobalUseTrustedNeighbour = _TiaraRipGlobalUseTrustedNeighbour_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 1, 3),
    _TiaraRipGlobalUseTrustedNeighbour_Type()
)
tiaraRipGlobalUseTrustedNeighbour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tiaraRipGlobalUseTrustedNeighbour.setStatus("current")


class _TiaraRipGlobalValidateSrcIpAddr_Type(TruthValue):
    """Custom type tiaraRipGlobalValidateSrcIpAddr based on TruthValue"""


_TiaraRipGlobalValidateSrcIpAddr_Object = MibScalar
tiaraRipGlobalValidateSrcIpAddr = _TiaraRipGlobalValidateSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 1, 4),
    _TiaraRipGlobalValidateSrcIpAddr_Type()
)
tiaraRipGlobalValidateSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tiaraRipGlobalValidateSrcIpAddr.setStatus("current")


class _TiaraRipGlobalVersion_Type(Integer32):
    """Custom type tiaraRipGlobalVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_TiaraRipGlobalVersion_Type.__name__ = "Integer32"
_TiaraRipGlobalVersion_Object = MibScalar
tiaraRipGlobalVersion = _TiaraRipGlobalVersion_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 1, 5),
    _TiaraRipGlobalVersion_Type()
)
tiaraRipGlobalVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tiaraRipGlobalVersion.setStatus("current")
_TiaraRipIfConfTable_Object = MibTable
tiaraRipIfConfTable = _TiaraRipIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2)
)
if mibBuilder.loadTexts:
    tiaraRipIfConfTable.setStatus("current")
_TiaraRipIfConfEntry_Object = MibTableRow
tiaraRipIfConfEntry = _TiaraRipIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1)
)
tiaraRipIfConfEntry.setIndexNames(
    (0, "TIARARIP-MIB", "tiaraRipIfConfIpAddr"),
)
if mibBuilder.loadTexts:
    tiaraRipIfConfEntry.setStatus("current")
_TiaraRipIfConfIpAddr_Type = IpAddress
_TiaraRipIfConfIpAddr_Object = MibTableColumn
tiaraRipIfConfIpAddr = _TiaraRipIfConfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 1),
    _TiaraRipIfConfIpAddr_Type()
)
tiaraRipIfConfIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tiaraRipIfConfIpAddr.setStatus("current")
_TiaraRipIfConfAuthString_Type = DisplayString
_TiaraRipIfConfAuthString_Object = MibTableColumn
tiaraRipIfConfAuthString = _TiaraRipIfConfAuthString_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 2),
    _TiaraRipIfConfAuthString_Type()
)
tiaraRipIfConfAuthString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipIfConfAuthString.setStatus("current")


class _TiaraRipIfConfAutoSummaryEnable_Type(TruthValue):
    """Custom type tiaraRipIfConfAutoSummaryEnable based on TruthValue"""


_TiaraRipIfConfAutoSummaryEnable_Object = MibTableColumn
tiaraRipIfConfAutoSummaryEnable = _TiaraRipIfConfAutoSummaryEnable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 3),
    _TiaraRipIfConfAutoSummaryEnable_Type()
)
tiaraRipIfConfAutoSummaryEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipIfConfAutoSummaryEnable.setStatus("current")


class _TiaraRipIfConfDefaultAnnounceEnable_Type(TruthValue):
    """Custom type tiaraRipIfConfDefaultAnnounceEnable based on TruthValue"""


_TiaraRipIfConfDefaultAnnounceEnable_Object = MibTableColumn
tiaraRipIfConfDefaultAnnounceEnable = _TiaraRipIfConfDefaultAnnounceEnable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 4),
    _TiaraRipIfConfDefaultAnnounceEnable_Type()
)
tiaraRipIfConfDefaultAnnounceEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipIfConfDefaultAnnounceEnable.setStatus("current")


class _TiaraRipIfConfEnable_Type(TruthValue):
    """Custom type tiaraRipIfConfEnable based on TruthValue"""


_TiaraRipIfConfEnable_Object = MibTableColumn
tiaraRipIfConfEnable = _TiaraRipIfConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 5),
    _TiaraRipIfConfEnable_Type()
)
tiaraRipIfConfEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipIfConfEnable.setStatus("current")


class _TiaraRipIfConfAnnounceHostEnable_Type(TruthValue):
    """Custom type tiaraRipIfConfAnnounceHostEnable based on TruthValue"""


_TiaraRipIfConfAnnounceHostEnable_Object = MibTableColumn
tiaraRipIfConfAnnounceHostEnable = _TiaraRipIfConfAnnounceHostEnable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 6),
    _TiaraRipIfConfAnnounceHostEnable_Type()
)
tiaraRipIfConfAnnounceHostEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipIfConfAnnounceHostEnable.setStatus("current")


class _TiaraRipIfConfPassiveEnable_Type(TruthValue):
    """Custom type tiaraRipIfConfPassiveEnable based on TruthValue"""


_TiaraRipIfConfPassiveEnable_Object = MibTableColumn
tiaraRipIfConfPassiveEnable = _TiaraRipIfConfPassiveEnable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 7),
    _TiaraRipIfConfPassiveEnable_Type()
)
tiaraRipIfConfPassiveEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipIfConfPassiveEnable.setStatus("current")


class _TiaraRipIfConfReceiveVersion_Type(Integer32):
    """Custom type tiaraRipIfConfReceiveVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version1and2", 3),
          ("version2", 2))
    )


_TiaraRipIfConfReceiveVersion_Type.__name__ = "Integer32"
_TiaraRipIfConfReceiveVersion_Object = MibTableColumn
tiaraRipIfConfReceiveVersion = _TiaraRipIfConfReceiveVersion_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 8),
    _TiaraRipIfConfReceiveVersion_Type()
)
tiaraRipIfConfReceiveVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipIfConfReceiveVersion.setStatus("current")


class _TiaraRipIfConfSendVersion_Type(Integer32):
    """Custom type tiaraRipIfConfSendVersion based on Integer32"""
    defaultValue = 1

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
        *(("version1", 1),
          ("version1and2", 3),
          ("version1compatible", 4),
          ("version2", 2))
    )


_TiaraRipIfConfSendVersion_Type.__name__ = "Integer32"
_TiaraRipIfConfSendVersion_Object = MibTableColumn
tiaraRipIfConfSendVersion = _TiaraRipIfConfSendVersion_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 9),
    _TiaraRipIfConfSendVersion_Type()
)
tiaraRipIfConfSendVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipIfConfSendVersion.setStatus("current")


class _TiaraRipIfConfSplitHorizonEnable_Type(TruthValue):
    """Custom type tiaraRipIfConfSplitHorizonEnable based on TruthValue"""


_TiaraRipIfConfSplitHorizonEnable_Object = MibTableColumn
tiaraRipIfConfSplitHorizonEnable = _TiaraRipIfConfSplitHorizonEnable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 10),
    _TiaraRipIfConfSplitHorizonEnable_Type()
)
tiaraRipIfConfSplitHorizonEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipIfConfSplitHorizonEnable.setStatus("current")


class _TiaraRipIfConfStaticAnnounceEnable_Type(TruthValue):
    """Custom type tiaraRipIfConfStaticAnnounceEnable based on TruthValue"""


_TiaraRipIfConfStaticAnnounceEnable_Object = MibTableColumn
tiaraRipIfConfStaticAnnounceEnable = _TiaraRipIfConfStaticAnnounceEnable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 11),
    _TiaraRipIfConfStaticAnnounceEnable_Type()
)
tiaraRipIfConfStaticAnnounceEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipIfConfStaticAnnounceEnable.setStatus("current")


class _TiaraRipIfConfUpdateTimer_Type(Integer32):
    """Custom type tiaraRipIfConfUpdateTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TiaraRipIfConfUpdateTimer_Type.__name__ = "Integer32"
_TiaraRipIfConfUpdateTimer_Object = MibTableColumn
tiaraRipIfConfUpdateTimer = _TiaraRipIfConfUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 12),
    _TiaraRipIfConfUpdateTimer_Type()
)
tiaraRipIfConfUpdateTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipIfConfUpdateTimer.setStatus("current")
if mibBuilder.loadTexts:
    tiaraRipIfConfUpdateTimer.setUnits("seconds")


class _TiaraRipIfConfHoldDownTimer_Type(Integer32):
    """Custom type tiaraRipIfConfHoldDownTimer based on Integer32"""
    defaultValue = 120


_TiaraRipIfConfHoldDownTimer_Object = MibTableColumn
tiaraRipIfConfHoldDownTimer = _TiaraRipIfConfHoldDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 13),
    _TiaraRipIfConfHoldDownTimer_Type()
)
tiaraRipIfConfHoldDownTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipIfConfHoldDownTimer.setStatus("current")
if mibBuilder.loadTexts:
    tiaraRipIfConfHoldDownTimer.setUnits("seconds")


class _TiaraRipIfConfFlushTimer_Type(Integer32):
    """Custom type tiaraRipIfConfFlushTimer based on Integer32"""
    defaultValue = 120


_TiaraRipIfConfFlushTimer_Object = MibTableColumn
tiaraRipIfConfFlushTimer = _TiaraRipIfConfFlushTimer_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 14),
    _TiaraRipIfConfFlushTimer_Type()
)
tiaraRipIfConfFlushTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipIfConfFlushTimer.setStatus("current")
if mibBuilder.loadTexts:
    tiaraRipIfConfFlushTimer.setUnits("seconds")


class _TiaraRipIfConfInvTimer_Type(Integer32):
    """Custom type tiaraRipIfConfInvTimer based on Integer32"""
    defaultValue = 180


_TiaraRipIfConfInvTimer_Object = MibTableColumn
tiaraRipIfConfInvTimer = _TiaraRipIfConfInvTimer_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 15),
    _TiaraRipIfConfInvTimer_Type()
)
tiaraRipIfConfInvTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipIfConfInvTimer.setStatus("current")
if mibBuilder.loadTexts:
    tiaraRipIfConfInvTimer.setUnits("seconds")
_TiaraRipIfConfRowStatus_Type = RowStatus
_TiaraRipIfConfRowStatus_Object = MibTableColumn
tiaraRipIfConfRowStatus = _TiaraRipIfConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 16),
    _TiaraRipIfConfRowStatus_Type()
)
tiaraRipIfConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipIfConfRowStatus.setStatus("current")
_TiaraRipStatTable_Object = MibTable
tiaraRipStatTable = _TiaraRipStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 3)
)
if mibBuilder.loadTexts:
    tiaraRipStatTable.setStatus("current")
_TiaraRipStatEntry_Object = MibTableRow
tiaraRipStatEntry = _TiaraRipStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1)
)
tiaraRipStatEntry.setIndexNames(
    (0, "TIARARIP-MIB", "tiaraRipIfConfIpAddr"),
)
if mibBuilder.loadTexts:
    tiaraRipStatEntry.setStatus("current")
_TiaraRipStatRequestPktsSent_Type = Counter32
_TiaraRipStatRequestPktsSent_Object = MibTableColumn
tiaraRipStatRequestPktsSent = _TiaraRipStatRequestPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 1),
    _TiaraRipStatRequestPktsSent_Type()
)
tiaraRipStatRequestPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraRipStatRequestPktsSent.setStatus("current")
_TiaraRipStatResponsePktsSent_Type = Counter32
_TiaraRipStatResponsePktsSent_Object = MibTableColumn
tiaraRipStatResponsePktsSent = _TiaraRipStatResponsePktsSent_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 2),
    _TiaraRipStatResponsePktsSent_Type()
)
tiaraRipStatResponsePktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraRipStatResponsePktsSent.setStatus("current")
_TiaraRipStatPktsReceived_Type = Counter32
_TiaraRipStatPktsReceived_Object = MibTableColumn
tiaraRipStatPktsReceived = _TiaraRipStatPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 3),
    _TiaraRipStatPktsReceived_Type()
)
tiaraRipStatPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraRipStatPktsReceived.setStatus("current")
_TiaraRipStatRequestPktsReceived_Type = Counter32
_TiaraRipStatRequestPktsReceived_Object = MibTableColumn
tiaraRipStatRequestPktsReceived = _TiaraRipStatRequestPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 4),
    _TiaraRipStatRequestPktsReceived_Type()
)
tiaraRipStatRequestPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraRipStatRequestPktsReceived.setStatus("current")
_TiaraRipStatResponsePktsReceived_Type = Counter32
_TiaraRipStatResponsePktsReceived_Object = MibTableColumn
tiaraRipStatResponsePktsReceived = _TiaraRipStatResponsePktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 5),
    _TiaraRipStatResponsePktsReceived_Type()
)
tiaraRipStatResponsePktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraRipStatResponsePktsReceived.setStatus("current")
_TiaraRipStatUnrecognizedPktsReceived_Type = Counter32
_TiaraRipStatUnrecognizedPktsReceived_Object = MibTableColumn
tiaraRipStatUnrecognizedPktsReceived = _TiaraRipStatUnrecognizedPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 6),
    _TiaraRipStatUnrecognizedPktsReceived_Type()
)
tiaraRipStatUnrecognizedPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraRipStatUnrecognizedPktsReceived.setStatus("current")
_TiaraRipStatBadVersions_Type = Counter32
_TiaraRipStatBadVersions_Object = MibTableColumn
tiaraRipStatBadVersions = _TiaraRipStatBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 7),
    _TiaraRipStatBadVersions_Type()
)
tiaraRipStatBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraRipStatBadVersions.setStatus("current")
_TiaraRipStatBadAddrFamilies_Type = Counter32
_TiaraRipStatBadAddrFamilies_Object = MibTableColumn
tiaraRipStatBadAddrFamilies = _TiaraRipStatBadAddrFamilies_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 8),
    _TiaraRipStatBadAddrFamilies_Type()
)
tiaraRipStatBadAddrFamilies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraRipStatBadAddrFamilies.setStatus("current")
_TiaraRipStatBadRequestFormats_Type = Counter32
_TiaraRipStatBadRequestFormats_Object = MibTableColumn
tiaraRipStatBadRequestFormats = _TiaraRipStatBadRequestFormats_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 9),
    _TiaraRipStatBadRequestFormats_Type()
)
tiaraRipStatBadRequestFormats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraRipStatBadRequestFormats.setStatus("current")
_TiaraRipStatBadMetrics_Type = Counter32
_TiaraRipStatBadMetrics_Object = MibTableColumn
tiaraRipStatBadMetrics = _TiaraRipStatBadMetrics_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 10),
    _TiaraRipStatBadMetrics_Type()
)
tiaraRipStatBadMetrics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraRipStatBadMetrics.setStatus("current")
_TiaraRipStatBadResponseFormats_Type = Counter32
_TiaraRipStatBadResponseFormats_Object = MibTableColumn
tiaraRipStatBadResponseFormats = _TiaraRipStatBadResponseFormats_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 11),
    _TiaraRipStatBadResponseFormats_Type()
)
tiaraRipStatBadResponseFormats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraRipStatBadResponseFormats.setStatus("current")
_TiaraRipStatResponsesNotFromRipPort_Type = Counter32
_TiaraRipStatResponsesNotFromRipPort_Object = MibTableColumn
tiaraRipStatResponsesNotFromRipPort = _TiaraRipStatResponsesNotFromRipPort_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 12),
    _TiaraRipStatResponsesNotFromRipPort_Type()
)
tiaraRipStatResponsesNotFromRipPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraRipStatResponsesNotFromRipPort.setStatus("current")
_TiaraRipStatResponsesRecdFromLoopBackIf_Type = Counter32
_TiaraRipStatResponsesRecdFromLoopBackIf_Object = MibTableColumn
tiaraRipStatResponsesRecdFromLoopBackIf = _TiaraRipStatResponsesRecdFromLoopBackIf_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 13),
    _TiaraRipStatResponsesRecdFromLoopBackIf_Type()
)
tiaraRipStatResponsesRecdFromLoopBackIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraRipStatResponsesRecdFromLoopBackIf.setStatus("current")
_TiaraRipStatPktsRejected_Type = Counter32
_TiaraRipStatPktsRejected_Object = MibTableColumn
tiaraRipStatPktsRejected = _TiaraRipStatPktsRejected_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 14),
    _TiaraRipStatPktsRejected_Type()
)
tiaraRipStatPktsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tiaraRipStatPktsRejected.setStatus("current")
_TiaraRipRejectAddrTable_Object = MibTable
tiaraRipRejectAddrTable = _TiaraRipRejectAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 4)
)
if mibBuilder.loadTexts:
    tiaraRipRejectAddrTable.setStatus("current")
_TiaraRipRejectAddrEntry_Object = MibTableRow
tiaraRipRejectAddrEntry = _TiaraRipRejectAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 4, 1)
)
tiaraRipRejectAddrEntry.setIndexNames(
    (0, "TIARARIP-MIB", "tiaraRipIfConfIpAddr"),
    (0, "TIARARIP-MIB", "tiaraRipRejectIpAddr"),
)
if mibBuilder.loadTexts:
    tiaraRipRejectAddrEntry.setStatus("current")
_TiaraRipRejectIpAddr_Type = IpAddress
_TiaraRipRejectIpAddr_Object = MibTableColumn
tiaraRipRejectIpAddr = _TiaraRipRejectIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 4, 1, 1),
    _TiaraRipRejectIpAddr_Type()
)
tiaraRipRejectIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tiaraRipRejectIpAddr.setStatus("current")
_TiaraRipRejectRowStatus_Type = RowStatus
_TiaraRipRejectRowStatus_Object = MibTableColumn
tiaraRipRejectRowStatus = _TiaraRipRejectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 4, 1, 2),
    _TiaraRipRejectRowStatus_Type()
)
tiaraRipRejectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipRejectRowStatus.setStatus("current")
_TiaraRipAdvertiseAddrTable_Object = MibTable
tiaraRipAdvertiseAddrTable = _TiaraRipAdvertiseAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 5)
)
if mibBuilder.loadTexts:
    tiaraRipAdvertiseAddrTable.setStatus("current")
_TiaraRipAdvertiseAddrEntry_Object = MibTableRow
tiaraRipAdvertiseAddrEntry = _TiaraRipAdvertiseAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 5, 1)
)
tiaraRipAdvertiseAddrEntry.setIndexNames(
    (0, "TIARARIP-MIB", "tiaraRipIfConfIpAddr"),
    (0, "TIARARIP-MIB", "tiaraRipAdvertiseIpAddr"),
)
if mibBuilder.loadTexts:
    tiaraRipAdvertiseAddrEntry.setStatus("current")
_TiaraRipAdvertiseIpAddr_Type = IpAddress
_TiaraRipAdvertiseIpAddr_Object = MibTableColumn
tiaraRipAdvertiseIpAddr = _TiaraRipAdvertiseIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 5, 1, 1),
    _TiaraRipAdvertiseIpAddr_Type()
)
tiaraRipAdvertiseIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tiaraRipAdvertiseIpAddr.setStatus("current")
_TiaraRipAdvertiseRowStatus_Type = RowStatus
_TiaraRipAdvertiseRowStatus_Object = MibTableColumn
tiaraRipAdvertiseRowStatus = _TiaraRipAdvertiseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 5, 1, 2),
    _TiaraRipAdvertiseRowStatus_Type()
)
tiaraRipAdvertiseRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipAdvertiseRowStatus.setStatus("current")
_TiaraRipNeighbourAddrTable_Object = MibTable
tiaraRipNeighbourAddrTable = _TiaraRipNeighbourAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 6)
)
if mibBuilder.loadTexts:
    tiaraRipNeighbourAddrTable.setStatus("current")
_TiaraRipNeighbourAddrEntry_Object = MibTableRow
tiaraRipNeighbourAddrEntry = _TiaraRipNeighbourAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 6, 1)
)
tiaraRipNeighbourAddrEntry.setIndexNames(
    (0, "TIARARIP-MIB", "tiaraRipIfConfIpAddr"),
    (0, "TIARARIP-MIB", "tiaraRipNeighbourIpAddr"),
)
if mibBuilder.loadTexts:
    tiaraRipNeighbourAddrEntry.setStatus("current")
_TiaraRipNeighbourIpAddr_Type = IpAddress
_TiaraRipNeighbourIpAddr_Object = MibTableColumn
tiaraRipNeighbourIpAddr = _TiaraRipNeighbourIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 6, 1, 1),
    _TiaraRipNeighbourIpAddr_Type()
)
tiaraRipNeighbourIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tiaraRipNeighbourIpAddr.setStatus("current")
_TiaraRipNeighbourRowStatus_Type = RowStatus
_TiaraRipNeighbourRowStatus_Object = MibTableColumn
tiaraRipNeighbourRowStatus = _TiaraRipNeighbourRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 6, 1, 2),
    _TiaraRipNeighbourRowStatus_Type()
)
tiaraRipNeighbourRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipNeighbourRowStatus.setStatus("current")
_TiaraRipTrustedNeighbourAddrTable_Object = MibTable
tiaraRipTrustedNeighbourAddrTable = _TiaraRipTrustedNeighbourAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 7)
)
if mibBuilder.loadTexts:
    tiaraRipTrustedNeighbourAddrTable.setStatus("current")
_TiaraRipTrustedNeighbourAddrEntry_Object = MibTableRow
tiaraRipTrustedNeighbourAddrEntry = _TiaraRipTrustedNeighbourAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 7, 1)
)
tiaraRipTrustedNeighbourAddrEntry.setIndexNames(
    (0, "TIARARIP-MIB", "tiaraRipTrustedNeighbourAddr"),
)
if mibBuilder.loadTexts:
    tiaraRipTrustedNeighbourAddrEntry.setStatus("current")
_TiaraRipTrustedNeighbourAddr_Type = IpAddress
_TiaraRipTrustedNeighbourAddr_Object = MibTableColumn
tiaraRipTrustedNeighbourAddr = _TiaraRipTrustedNeighbourAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 7, 1, 1),
    _TiaraRipTrustedNeighbourAddr_Type()
)
tiaraRipTrustedNeighbourAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tiaraRipTrustedNeighbourAddr.setStatus("current")
_TiaraRipTrustedNeighbourRowStatus_Type = RowStatus
_TiaraRipTrustedNeighbourRowStatus_Object = MibTableColumn
tiaraRipTrustedNeighbourRowStatus = _TiaraRipTrustedNeighbourRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 110, 7, 1, 2),
    _TiaraRipTrustedNeighbourRowStatus_Type()
)
tiaraRipTrustedNeighbourRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tiaraRipTrustedNeighbourRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARARIP-MIB",
    **{"tiaraRipMib": tiaraRipMib,
       "tiaraRipGlobals": tiaraRipGlobals,
       "tiaraRoutingEnable": tiaraRoutingEnable,
       "tiaraRipGlobalEnable": tiaraRipGlobalEnable,
       "tiaraRipGlobalUseTrustedNeighbour": tiaraRipGlobalUseTrustedNeighbour,
       "tiaraRipGlobalValidateSrcIpAddr": tiaraRipGlobalValidateSrcIpAddr,
       "tiaraRipGlobalVersion": tiaraRipGlobalVersion,
       "tiaraRipIfConfTable": tiaraRipIfConfTable,
       "tiaraRipIfConfEntry": tiaraRipIfConfEntry,
       "tiaraRipIfConfIpAddr": tiaraRipIfConfIpAddr,
       "tiaraRipIfConfAuthString": tiaraRipIfConfAuthString,
       "tiaraRipIfConfAutoSummaryEnable": tiaraRipIfConfAutoSummaryEnable,
       "tiaraRipIfConfDefaultAnnounceEnable": tiaraRipIfConfDefaultAnnounceEnable,
       "tiaraRipIfConfEnable": tiaraRipIfConfEnable,
       "tiaraRipIfConfAnnounceHostEnable": tiaraRipIfConfAnnounceHostEnable,
       "tiaraRipIfConfPassiveEnable": tiaraRipIfConfPassiveEnable,
       "tiaraRipIfConfReceiveVersion": tiaraRipIfConfReceiveVersion,
       "tiaraRipIfConfSendVersion": tiaraRipIfConfSendVersion,
       "tiaraRipIfConfSplitHorizonEnable": tiaraRipIfConfSplitHorizonEnable,
       "tiaraRipIfConfStaticAnnounceEnable": tiaraRipIfConfStaticAnnounceEnable,
       "tiaraRipIfConfUpdateTimer": tiaraRipIfConfUpdateTimer,
       "tiaraRipIfConfHoldDownTimer": tiaraRipIfConfHoldDownTimer,
       "tiaraRipIfConfFlushTimer": tiaraRipIfConfFlushTimer,
       "tiaraRipIfConfInvTimer": tiaraRipIfConfInvTimer,
       "tiaraRipIfConfRowStatus": tiaraRipIfConfRowStatus,
       "tiaraRipStatTable": tiaraRipStatTable,
       "tiaraRipStatEntry": tiaraRipStatEntry,
       "tiaraRipStatRequestPktsSent": tiaraRipStatRequestPktsSent,
       "tiaraRipStatResponsePktsSent": tiaraRipStatResponsePktsSent,
       "tiaraRipStatPktsReceived": tiaraRipStatPktsReceived,
       "tiaraRipStatRequestPktsReceived": tiaraRipStatRequestPktsReceived,
       "tiaraRipStatResponsePktsReceived": tiaraRipStatResponsePktsReceived,
       "tiaraRipStatUnrecognizedPktsReceived": tiaraRipStatUnrecognizedPktsReceived,
       "tiaraRipStatBadVersions": tiaraRipStatBadVersions,
       "tiaraRipStatBadAddrFamilies": tiaraRipStatBadAddrFamilies,
       "tiaraRipStatBadRequestFormats": tiaraRipStatBadRequestFormats,
       "tiaraRipStatBadMetrics": tiaraRipStatBadMetrics,
       "tiaraRipStatBadResponseFormats": tiaraRipStatBadResponseFormats,
       "tiaraRipStatResponsesNotFromRipPort": tiaraRipStatResponsesNotFromRipPort,
       "tiaraRipStatResponsesRecdFromLoopBackIf": tiaraRipStatResponsesRecdFromLoopBackIf,
       "tiaraRipStatPktsRejected": tiaraRipStatPktsRejected,
       "tiaraRipRejectAddrTable": tiaraRipRejectAddrTable,
       "tiaraRipRejectAddrEntry": tiaraRipRejectAddrEntry,
       "tiaraRipRejectIpAddr": tiaraRipRejectIpAddr,
       "tiaraRipRejectRowStatus": tiaraRipRejectRowStatus,
       "tiaraRipAdvertiseAddrTable": tiaraRipAdvertiseAddrTable,
       "tiaraRipAdvertiseAddrEntry": tiaraRipAdvertiseAddrEntry,
       "tiaraRipAdvertiseIpAddr": tiaraRipAdvertiseIpAddr,
       "tiaraRipAdvertiseRowStatus": tiaraRipAdvertiseRowStatus,
       "tiaraRipNeighbourAddrTable": tiaraRipNeighbourAddrTable,
       "tiaraRipNeighbourAddrEntry": tiaraRipNeighbourAddrEntry,
       "tiaraRipNeighbourIpAddr": tiaraRipNeighbourIpAddr,
       "tiaraRipNeighbourRowStatus": tiaraRipNeighbourRowStatus,
       "tiaraRipTrustedNeighbourAddrTable": tiaraRipTrustedNeighbourAddrTable,
       "tiaraRipTrustedNeighbourAddrEntry": tiaraRipTrustedNeighbourAddrEntry,
       "tiaraRipTrustedNeighbourAddr": tiaraRipTrustedNeighbourAddr,
       "tiaraRipTrustedNeighbourRowStatus": tiaraRipTrustedNeighbourRowStatus}
)
