# SNMP MIB module (BayNetworks-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BayNetworks-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:19 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfDhcpServerGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfDhcpServerGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfDhcpSvrGroup_ObjectIdentity = ObjectIdentity
wfDhcpSvrGroup = _WfDhcpSvrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1)
)
_WfDhcpSvrGeneral_ObjectIdentity = ObjectIdentity
wfDhcpSvrGeneral = _WfDhcpSvrGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 1)
)


class _WfDhcpSvrDelete_Type(Integer32):
    """Custom type wfDhcpSvrDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDhcpSvrDelete_Type.__name__ = "Integer32"
_WfDhcpSvrDelete_Object = MibScalar
wfDhcpSvrDelete = _WfDhcpSvrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 1, 1),
    _WfDhcpSvrDelete_Type()
)
wfDhcpSvrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDhcpSvrDelete.setStatus("mandatory")


class _WfDhcpSvrDisable_Type(Integer32):
    """Custom type wfDhcpSvrDisable based on Integer32"""
    defaultValue = 2

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


_WfDhcpSvrDisable_Type.__name__ = "Integer32"
_WfDhcpSvrDisable_Object = MibScalar
wfDhcpSvrDisable = _WfDhcpSvrDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 1, 2),
    _WfDhcpSvrDisable_Type()
)
wfDhcpSvrDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDhcpSvrDisable.setStatus("mandatory")
_WfDhcpSvrMgrIpAddr_Type = IpAddress
_WfDhcpSvrMgrIpAddr_Object = MibScalar
wfDhcpSvrMgrIpAddr = _WfDhcpSvrMgrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 1, 3),
    _WfDhcpSvrMgrIpAddr_Type()
)
wfDhcpSvrMgrIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDhcpSvrMgrIpAddr.setStatus("mandatory")
_WfDhcpSvrMgrTcpPort_Type = Integer32
_WfDhcpSvrMgrTcpPort_Object = MibScalar
wfDhcpSvrMgrTcpPort = _WfDhcpSvrMgrTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 1, 4),
    _WfDhcpSvrMgrTcpPort_Type()
)
wfDhcpSvrMgrTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDhcpSvrMgrTcpPort.setStatus("mandatory")


class _WfDhcpSvrConfDetPings_Type(Integer32):
    """Custom type wfDhcpSvrConfDetPings based on Integer32"""
    defaultValue = 1


_WfDhcpSvrConfDetPings_Object = MibScalar
wfDhcpSvrConfDetPings = _WfDhcpSvrConfDetPings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 1, 5),
    _WfDhcpSvrConfDetPings_Type()
)
wfDhcpSvrConfDetPings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDhcpSvrConfDetPings.setStatus("mandatory")


class _WfDhcpSvrIcmpTmo_Type(Integer32):
    """Custom type wfDhcpSvrIcmpTmo based on Integer32"""
    defaultValue = 750


_WfDhcpSvrIcmpTmo_Object = MibScalar
wfDhcpSvrIcmpTmo = _WfDhcpSvrIcmpTmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 1, 6),
    _WfDhcpSvrIcmpTmo_Type()
)
wfDhcpSvrIcmpTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDhcpSvrIcmpTmo.setStatus("mandatory")


class _WfDhcpSvrSafeModeDisable_Type(Integer32):
    """Custom type wfDhcpSvrSafeModeDisable based on Integer32"""
    defaultValue = 1

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


_WfDhcpSvrSafeModeDisable_Type.__name__ = "Integer32"
_WfDhcpSvrSafeModeDisable_Object = MibScalar
wfDhcpSvrSafeModeDisable = _WfDhcpSvrSafeModeDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 1, 7),
    _WfDhcpSvrSafeModeDisable_Type()
)
wfDhcpSvrSafeModeDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDhcpSvrSafeModeDisable.setStatus("mandatory")


class _WfDhcpSvrMaxPendingLeases_Type(Integer32):
    """Custom type wfDhcpSvrMaxPendingLeases based on Integer32"""
    defaultValue = 2


_WfDhcpSvrMaxPendingLeases_Object = MibScalar
wfDhcpSvrMaxPendingLeases = _WfDhcpSvrMaxPendingLeases_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 1, 8),
    _WfDhcpSvrMaxPendingLeases_Type()
)
wfDhcpSvrMaxPendingLeases.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDhcpSvrMaxPendingLeases.setStatus("mandatory")


class _WfDhcpSvrDebugLevel_Type(Integer32):
    """Custom type wfDhcpSvrDebugLevel based on Integer32"""
    defaultValue = 0


_WfDhcpSvrDebugLevel_Object = MibScalar
wfDhcpSvrDebugLevel = _WfDhcpSvrDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 1, 9),
    _WfDhcpSvrDebugLevel_Type()
)
wfDhcpSvrDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDhcpSvrDebugLevel.setStatus("mandatory")
_WfDhcpSvrMgrLocIpAddr_Type = IpAddress
_WfDhcpSvrMgrLocIpAddr_Object = MibScalar
wfDhcpSvrMgrLocIpAddr = _WfDhcpSvrMgrLocIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 1, 10),
    _WfDhcpSvrMgrLocIpAddr_Type()
)
wfDhcpSvrMgrLocIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDhcpSvrMgrLocIpAddr.setStatus("mandatory")
_WfDhcpSvrIntfTable_Object = MibTable
wfDhcpSvrIntfTable = _WfDhcpSvrIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2)
)
if mibBuilder.loadTexts:
    wfDhcpSvrIntfTable.setStatus("mandatory")
_WfDhcpSvrIntfEntry_Object = MibTableRow
wfDhcpSvrIntfEntry = _WfDhcpSvrIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1)
)
wfDhcpSvrIntfEntry.setIndexNames(
    (0, "BayNetworks-DHCP-MIB", "wfDhcpSvrIntfAddress"),
)
if mibBuilder.loadTexts:
    wfDhcpSvrIntfEntry.setStatus("mandatory")
_WfDhcpSvrIntfAddress_Type = IpAddress
_WfDhcpSvrIntfAddress_Object = MibTableColumn
wfDhcpSvrIntfAddress = _WfDhcpSvrIntfAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 1),
    _WfDhcpSvrIntfAddress_Type()
)
wfDhcpSvrIntfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfAddress.setStatus("mandatory")


class _WfDhcpSvrIntfState_Type(Integer32):
    """Custom type wfDhcpSvrIntfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfDhcpSvrIntfState_Type.__name__ = "Integer32"
_WfDhcpSvrIntfState_Object = MibTableColumn
wfDhcpSvrIntfState = _WfDhcpSvrIntfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 2),
    _WfDhcpSvrIntfState_Type()
)
wfDhcpSvrIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfState.setStatus("mandatory")
_WfDhcpSvrIntfPendLsCnt_Type = Gauge32
_WfDhcpSvrIntfPendLsCnt_Object = MibTableColumn
wfDhcpSvrIntfPendLsCnt = _WfDhcpSvrIntfPendLsCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 3),
    _WfDhcpSvrIntfPendLsCnt_Type()
)
wfDhcpSvrIntfPendLsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfPendLsCnt.setStatus("mandatory")
_WfDhcpSvrIntfActLsCnt_Type = Gauge32
_WfDhcpSvrIntfActLsCnt_Object = MibTableColumn
wfDhcpSvrIntfActLsCnt = _WfDhcpSvrIntfActLsCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 4),
    _WfDhcpSvrIntfActLsCnt_Type()
)
wfDhcpSvrIntfActLsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfActLsCnt.setStatus("mandatory")
_WfDhcpSvrIntfCommits_Type = Counter32
_WfDhcpSvrIntfCommits_Object = MibTableColumn
wfDhcpSvrIntfCommits = _WfDhcpSvrIntfCommits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 5),
    _WfDhcpSvrIntfCommits_Type()
)
wfDhcpSvrIntfCommits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfCommits.setStatus("mandatory")
_WfDhcpSvrIntfCommitFails_Type = Counter32
_WfDhcpSvrIntfCommitFails_Object = MibTableColumn
wfDhcpSvrIntfCommitFails = _WfDhcpSvrIntfCommitFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 6),
    _WfDhcpSvrIntfCommitFails_Type()
)
wfDhcpSvrIntfCommitFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfCommitFails.setStatus("mandatory")
_WfDhcpSvrIntfCommitTmos_Type = Counter32
_WfDhcpSvrIntfCommitTmos_Object = MibTableColumn
wfDhcpSvrIntfCommitTmos = _WfDhcpSvrIntfCommitTmos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 7),
    _WfDhcpSvrIntfCommitTmos_Type()
)
wfDhcpSvrIntfCommitTmos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfCommitTmos.setStatus("mandatory")
_WfDhcpSvrIntfIllegPkts_Type = Counter32
_WfDhcpSvrIntfIllegPkts_Object = MibTableColumn
wfDhcpSvrIntfIllegPkts = _WfDhcpSvrIntfIllegPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 8),
    _WfDhcpSvrIntfIllegPkts_Type()
)
wfDhcpSvrIntfIllegPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfIllegPkts.setStatus("mandatory")
_WfDhcpSvrIntfDiscovers_Type = Counter32
_WfDhcpSvrIntfDiscovers_Object = MibTableColumn
wfDhcpSvrIntfDiscovers = _WfDhcpSvrIntfDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 9),
    _WfDhcpSvrIntfDiscovers_Type()
)
wfDhcpSvrIntfDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfDiscovers.setStatus("mandatory")
_WfDhcpSvrIntfBadDiscovers_Type = Counter32
_WfDhcpSvrIntfBadDiscovers_Object = MibTableColumn
wfDhcpSvrIntfBadDiscovers = _WfDhcpSvrIntfBadDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 10),
    _WfDhcpSvrIntfBadDiscovers_Type()
)
wfDhcpSvrIntfBadDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfBadDiscovers.setStatus("mandatory")
_WfDhcpSvrIntfReassgnLeases_Type = Counter32
_WfDhcpSvrIntfReassgnLeases_Object = MibTableColumn
wfDhcpSvrIntfReassgnLeases = _WfDhcpSvrIntfReassgnLeases_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 11),
    _WfDhcpSvrIntfReassgnLeases_Type()
)
wfDhcpSvrIntfReassgnLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfReassgnLeases.setStatus("mandatory")
_WfDhcpSvrIntfNoFreeLeases_Type = Counter32
_WfDhcpSvrIntfNoFreeLeases_Object = MibTableColumn
wfDhcpSvrIntfNoFreeLeases = _WfDhcpSvrIntfNoFreeLeases_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 12),
    _WfDhcpSvrIntfNoFreeLeases_Type()
)
wfDhcpSvrIntfNoFreeLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfNoFreeLeases.setStatus("mandatory")
_WfDhcpSvrIntfDropdLeaseRqs_Type = Counter32
_WfDhcpSvrIntfDropdLeaseRqs_Object = MibTableColumn
wfDhcpSvrIntfDropdLeaseRqs = _WfDhcpSvrIntfDropdLeaseRqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 13),
    _WfDhcpSvrIntfDropdLeaseRqs_Type()
)
wfDhcpSvrIntfDropdLeaseRqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfDropdLeaseRqs.setStatus("mandatory")
_WfDhcpSvrIntfOffers_Type = Counter32
_WfDhcpSvrIntfOffers_Object = MibTableColumn
wfDhcpSvrIntfOffers = _WfDhcpSvrIntfOffers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 14),
    _WfDhcpSvrIntfOffers_Type()
)
wfDhcpSvrIntfOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfOffers.setStatus("mandatory")
_WfDhcpSvrIntfRequests_Type = Counter32
_WfDhcpSvrIntfRequests_Object = MibTableColumn
wfDhcpSvrIntfRequests = _WfDhcpSvrIntfRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 15),
    _WfDhcpSvrIntfRequests_Type()
)
wfDhcpSvrIntfRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfRequests.setStatus("mandatory")
_WfDhcpSvrIntfBadRequests_Type = Counter32
_WfDhcpSvrIntfBadRequests_Object = MibTableColumn
wfDhcpSvrIntfBadRequests = _WfDhcpSvrIntfBadRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 16),
    _WfDhcpSvrIntfBadRequests_Type()
)
wfDhcpSvrIntfBadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfBadRequests.setStatus("mandatory")
_WfDhcpSvrIntfReleases_Type = Counter32
_WfDhcpSvrIntfReleases_Object = MibTableColumn
wfDhcpSvrIntfReleases = _WfDhcpSvrIntfReleases_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 17),
    _WfDhcpSvrIntfReleases_Type()
)
wfDhcpSvrIntfReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfReleases.setStatus("mandatory")
_WfDhcpSvrIntfBadReleases_Type = Counter32
_WfDhcpSvrIntfBadReleases_Object = MibTableColumn
wfDhcpSvrIntfBadReleases = _WfDhcpSvrIntfBadReleases_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 18),
    _WfDhcpSvrIntfBadReleases_Type()
)
wfDhcpSvrIntfBadReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfBadReleases.setStatus("mandatory")
_WfDhcpSvrIntfDeclines_Type = Counter32
_WfDhcpSvrIntfDeclines_Object = MibTableColumn
wfDhcpSvrIntfDeclines = _WfDhcpSvrIntfDeclines_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 19),
    _WfDhcpSvrIntfDeclines_Type()
)
wfDhcpSvrIntfDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfDeclines.setStatus("mandatory")
_WfDhcpSvrIntfBadDeclines_Type = Counter32
_WfDhcpSvrIntfBadDeclines_Object = MibTableColumn
wfDhcpSvrIntfBadDeclines = _WfDhcpSvrIntfBadDeclines_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 20),
    _WfDhcpSvrIntfBadDeclines_Type()
)
wfDhcpSvrIntfBadDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfBadDeclines.setStatus("mandatory")
_WfDhcpSvrIntfInforms_Type = Counter32
_WfDhcpSvrIntfInforms_Object = MibTableColumn
wfDhcpSvrIntfInforms = _WfDhcpSvrIntfInforms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 21),
    _WfDhcpSvrIntfInforms_Type()
)
wfDhcpSvrIntfInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfInforms.setStatus("mandatory")
_WfDhcpSvrIntfBadInforms_Type = Counter32
_WfDhcpSvrIntfBadInforms_Object = MibTableColumn
wfDhcpSvrIntfBadInforms = _WfDhcpSvrIntfBadInforms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 22),
    _WfDhcpSvrIntfBadInforms_Type()
)
wfDhcpSvrIntfBadInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfBadInforms.setStatus("mandatory")
_WfDhcpSvrIntfAddrConflict_Type = Counter32
_WfDhcpSvrIntfAddrConflict_Object = MibTableColumn
wfDhcpSvrIntfAddrConflict = _WfDhcpSvrIntfAddrConflict_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 2, 1, 23),
    _WfDhcpSvrIntfAddrConflict_Type()
)
wfDhcpSvrIntfAddrConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrIntfAddrConflict.setStatus("mandatory")
_WfDhcpSvrLeaseTable_Object = MibTable
wfDhcpSvrLeaseTable = _WfDhcpSvrLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 3)
)
if mibBuilder.loadTexts:
    wfDhcpSvrLeaseTable.setStatus("mandatory")
_WfDhcpSvrLeaseEntry_Object = MibTableRow
wfDhcpSvrLeaseEntry = _WfDhcpSvrLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 3, 1)
)
wfDhcpSvrLeaseEntry.setIndexNames(
    (0, "BayNetworks-DHCP-MIB", "wfDhcpSvrLeaseAddress"),
)
if mibBuilder.loadTexts:
    wfDhcpSvrLeaseEntry.setStatus("mandatory")


class _WfDhcpSvrLeaseState_Type(Integer32):
    """Custom type wfDhcpSvrLeaseState based on Integer32"""
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
        *(("committed", 1),
          ("pending", 2),
          ("pendingfail", 3),
          ("pendingtmo", 4))
    )


_WfDhcpSvrLeaseState_Type.__name__ = "Integer32"
_WfDhcpSvrLeaseState_Object = MibTableColumn
wfDhcpSvrLeaseState = _WfDhcpSvrLeaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 3, 1, 1),
    _WfDhcpSvrLeaseState_Type()
)
wfDhcpSvrLeaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrLeaseState.setStatus("mandatory")
_WfDhcpSvrLeaseRetries_Type = Integer32
_WfDhcpSvrLeaseRetries_Object = MibTableColumn
wfDhcpSvrLeaseRetries = _WfDhcpSvrLeaseRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 3, 1, 2),
    _WfDhcpSvrLeaseRetries_Type()
)
wfDhcpSvrLeaseRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrLeaseRetries.setStatus("mandatory")
_WfDhcpSvrLeaseAddress_Type = IpAddress
_WfDhcpSvrLeaseAddress_Object = MibTableColumn
wfDhcpSvrLeaseAddress = _WfDhcpSvrLeaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 3, 1, 3),
    _WfDhcpSvrLeaseAddress_Type()
)
wfDhcpSvrLeaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrLeaseAddress.setStatus("mandatory")
_WfDhcpSvrLeaseExpir_Type = Integer32
_WfDhcpSvrLeaseExpir_Object = MibTableColumn
wfDhcpSvrLeaseExpir = _WfDhcpSvrLeaseExpir_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 3, 1, 4),
    _WfDhcpSvrLeaseExpir_Type()
)
wfDhcpSvrLeaseExpir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrLeaseExpir.setStatus("mandatory")
_WfDhcpSvrLeaseDuration_Type = Integer32
_WfDhcpSvrLeaseDuration_Object = MibTableColumn
wfDhcpSvrLeaseDuration = _WfDhcpSvrLeaseDuration_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 3, 1, 5),
    _WfDhcpSvrLeaseDuration_Type()
)
wfDhcpSvrLeaseDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrLeaseDuration.setStatus("mandatory")
_WfDhcpSvrLeaseHwId_Type = OctetString
_WfDhcpSvrLeaseHwId_Object = MibTableColumn
wfDhcpSvrLeaseHwId = _WfDhcpSvrLeaseHwId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 3, 1, 6),
    _WfDhcpSvrLeaseHwId_Type()
)
wfDhcpSvrLeaseHwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrLeaseHwId.setStatus("mandatory")
_WfDhcpSvrLeaseClId_Type = OctetString
_WfDhcpSvrLeaseClId_Object = MibTableColumn
wfDhcpSvrLeaseClId = _WfDhcpSvrLeaseClId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 3, 1, 7),
    _WfDhcpSvrLeaseClId_Type()
)
wfDhcpSvrLeaseClId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrLeaseClId.setStatus("mandatory")
_WfDhcpSvrLeaseFqdn_Type = DisplayString
_WfDhcpSvrLeaseFqdn_Object = MibTableColumn
wfDhcpSvrLeaseFqdn = _WfDhcpSvrLeaseFqdn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 24, 1, 3, 1, 8),
    _WfDhcpSvrLeaseFqdn_Type()
)
wfDhcpSvrLeaseFqdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDhcpSvrLeaseFqdn.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BayNetworks-DHCP-MIB",
    **{"wfDhcpSvrGroup": wfDhcpSvrGroup,
       "wfDhcpSvrGeneral": wfDhcpSvrGeneral,
       "wfDhcpSvrDelete": wfDhcpSvrDelete,
       "wfDhcpSvrDisable": wfDhcpSvrDisable,
       "wfDhcpSvrMgrIpAddr": wfDhcpSvrMgrIpAddr,
       "wfDhcpSvrMgrTcpPort": wfDhcpSvrMgrTcpPort,
       "wfDhcpSvrConfDetPings": wfDhcpSvrConfDetPings,
       "wfDhcpSvrIcmpTmo": wfDhcpSvrIcmpTmo,
       "wfDhcpSvrSafeModeDisable": wfDhcpSvrSafeModeDisable,
       "wfDhcpSvrMaxPendingLeases": wfDhcpSvrMaxPendingLeases,
       "wfDhcpSvrDebugLevel": wfDhcpSvrDebugLevel,
       "wfDhcpSvrMgrLocIpAddr": wfDhcpSvrMgrLocIpAddr,
       "wfDhcpSvrIntfTable": wfDhcpSvrIntfTable,
       "wfDhcpSvrIntfEntry": wfDhcpSvrIntfEntry,
       "wfDhcpSvrIntfAddress": wfDhcpSvrIntfAddress,
       "wfDhcpSvrIntfState": wfDhcpSvrIntfState,
       "wfDhcpSvrIntfPendLsCnt": wfDhcpSvrIntfPendLsCnt,
       "wfDhcpSvrIntfActLsCnt": wfDhcpSvrIntfActLsCnt,
       "wfDhcpSvrIntfCommits": wfDhcpSvrIntfCommits,
       "wfDhcpSvrIntfCommitFails": wfDhcpSvrIntfCommitFails,
       "wfDhcpSvrIntfCommitTmos": wfDhcpSvrIntfCommitTmos,
       "wfDhcpSvrIntfIllegPkts": wfDhcpSvrIntfIllegPkts,
       "wfDhcpSvrIntfDiscovers": wfDhcpSvrIntfDiscovers,
       "wfDhcpSvrIntfBadDiscovers": wfDhcpSvrIntfBadDiscovers,
       "wfDhcpSvrIntfReassgnLeases": wfDhcpSvrIntfReassgnLeases,
       "wfDhcpSvrIntfNoFreeLeases": wfDhcpSvrIntfNoFreeLeases,
       "wfDhcpSvrIntfDropdLeaseRqs": wfDhcpSvrIntfDropdLeaseRqs,
       "wfDhcpSvrIntfOffers": wfDhcpSvrIntfOffers,
       "wfDhcpSvrIntfRequests": wfDhcpSvrIntfRequests,
       "wfDhcpSvrIntfBadRequests": wfDhcpSvrIntfBadRequests,
       "wfDhcpSvrIntfReleases": wfDhcpSvrIntfReleases,
       "wfDhcpSvrIntfBadReleases": wfDhcpSvrIntfBadReleases,
       "wfDhcpSvrIntfDeclines": wfDhcpSvrIntfDeclines,
       "wfDhcpSvrIntfBadDeclines": wfDhcpSvrIntfBadDeclines,
       "wfDhcpSvrIntfInforms": wfDhcpSvrIntfInforms,
       "wfDhcpSvrIntfBadInforms": wfDhcpSvrIntfBadInforms,
       "wfDhcpSvrIntfAddrConflict": wfDhcpSvrIntfAddrConflict,
       "wfDhcpSvrLeaseTable": wfDhcpSvrLeaseTable,
       "wfDhcpSvrLeaseEntry": wfDhcpSvrLeaseEntry,
       "wfDhcpSvrLeaseState": wfDhcpSvrLeaseState,
       "wfDhcpSvrLeaseRetries": wfDhcpSvrLeaseRetries,
       "wfDhcpSvrLeaseAddress": wfDhcpSvrLeaseAddress,
       "wfDhcpSvrLeaseExpir": wfDhcpSvrLeaseExpir,
       "wfDhcpSvrLeaseDuration": wfDhcpSvrLeaseDuration,
       "wfDhcpSvrLeaseHwId": wfDhcpSvrLeaseHwId,
       "wfDhcpSvrLeaseClId": wfDhcpSvrLeaseClId,
       "wfDhcpSvrLeaseFqdn": wfDhcpSvrLeaseFqdn}
)
