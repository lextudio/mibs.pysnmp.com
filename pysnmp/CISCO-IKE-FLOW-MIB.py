# SNMP MIB module (CISCO-IKE-FLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IKE-FLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:21 2024
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

(cisgIpsSgFailLocalAddress,
 cisgIpsSgFailRemoteAddress,
 cisgIpsSgProtocol,
 cisgIpsSgTunHistIndex,
 cisgIpsSgTunIndex) = mibBuilder.importSymbols(
    "CISCO-IPSEC-SIGNALING-MIB",
    "cisgIpsSgFailLocalAddress",
    "cisgIpsSgFailRemoteAddress",
    "cisgIpsSgProtocol",
    "cisgIpsSgTunHistIndex",
    "cisgIpsSgTunIndex")

(CIPsecDiffHellmanGrp,
 CIPsecIkeNegoMode) = mibBuilder.importSymbols(
    "CISCO-IPSEC-TC",
    "CIPsecDiffHellmanGrp",
    "CIPsecIkeNegoMode")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoIkeFlowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 429)
)
ciscoIkeFlowMIB.setRevisions(
        ("2004-09-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIkeFlowMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIkeFlowMIBNotifs = _CiscoIkeFlowMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 0)
)
_CiscoIkeFlowMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIkeFlowMIBObjects = _CiscoIkeFlowMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1)
)
_CifIkeCurrentActivity_ObjectIdentity = ObjectIdentity
cifIkeCurrentActivity = _CifIkeCurrentActivity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1)
)
_CifIkeGlobalStatsTable_Object = MibTable
cifIkeGlobalStatsTable = _CifIkeGlobalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cifIkeGlobalStatsTable.setStatus("current")
_CifIkeGlobalStatsEntry_Object = MibTableRow
cifIkeGlobalStatsEntry = _CifIkeGlobalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1)
)
cifIkeGlobalStatsEntry.setIndexNames(
    (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgProtocol"),
)
if mibBuilder.loadTexts:
    cifIkeGlobalStatsEntry.setStatus("current")
_CifIkeGlobalInP2Exchgs_Type = Counter64
_CifIkeGlobalInP2Exchgs_Object = MibTableColumn
cifIkeGlobalInP2Exchgs = _CifIkeGlobalInP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 1),
    _CifIkeGlobalInP2Exchgs_Type()
)
cifIkeGlobalInP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeGlobalInP2Exchgs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeGlobalInP2Exchgs.setUnits("SA Payloads")
_CifIkeGlobalInP2ExchgInvalids_Type = Counter64
_CifIkeGlobalInP2ExchgInvalids_Object = MibTableColumn
cifIkeGlobalInP2ExchgInvalids = _CifIkeGlobalInP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 2),
    _CifIkeGlobalInP2ExchgInvalids_Type()
)
cifIkeGlobalInP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeGlobalInP2ExchgInvalids.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeGlobalInP2ExchgInvalids.setUnits("SA Payloads")
_CifIkeGlobalInP2ExchgRejects_Type = Counter64
_CifIkeGlobalInP2ExchgRejects_Object = MibTableColumn
cifIkeGlobalInP2ExchgRejects = _CifIkeGlobalInP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 3),
    _CifIkeGlobalInP2ExchgRejects_Type()
)
cifIkeGlobalInP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeGlobalInP2ExchgRejects.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeGlobalInP2ExchgRejects.setUnits("SA Payloads")
_CifIkeGlobalOutP2Exchgs_Type = Counter64
_CifIkeGlobalOutP2Exchgs_Object = MibTableColumn
cifIkeGlobalOutP2Exchgs = _CifIkeGlobalOutP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 4),
    _CifIkeGlobalOutP2Exchgs_Type()
)
cifIkeGlobalOutP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeGlobalOutP2Exchgs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeGlobalOutP2Exchgs.setUnits("SA Payloads")
_CifIkeGlobalOutP2ExchgInvalids_Type = Counter64
_CifIkeGlobalOutP2ExchgInvalids_Object = MibTableColumn
cifIkeGlobalOutP2ExchgInvalids = _CifIkeGlobalOutP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 5),
    _CifIkeGlobalOutP2ExchgInvalids_Type()
)
cifIkeGlobalOutP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeGlobalOutP2ExchgInvalids.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeGlobalOutP2ExchgInvalids.setUnits("SA Payloads")
_CifIkeGlobalOutP2ExchgRejects_Type = Counter64
_CifIkeGlobalOutP2ExchgRejects_Object = MibTableColumn
cifIkeGlobalOutP2ExchgRejects = _CifIkeGlobalOutP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 6),
    _CifIkeGlobalOutP2ExchgRejects_Type()
)
cifIkeGlobalOutP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeGlobalOutP2ExchgRejects.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeGlobalOutP2ExchgRejects.setUnits("SA Payloads")
_CifIkeGlobalInXauths_Type = Counter64
_CifIkeGlobalInXauths_Object = MibTableColumn
cifIkeGlobalInXauths = _CifIkeGlobalInXauths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 7),
    _CifIkeGlobalInXauths_Type()
)
cifIkeGlobalInXauths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeGlobalInXauths.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeGlobalInXauths.setUnits("Failures")
_CifIkeGlobalInXauthFailures_Type = Counter64
_CifIkeGlobalInXauthFailures_Object = MibTableColumn
cifIkeGlobalInXauthFailures = _CifIkeGlobalInXauthFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 8),
    _CifIkeGlobalInXauthFailures_Type()
)
cifIkeGlobalInXauthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeGlobalInXauthFailures.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeGlobalInXauthFailures.setUnits("Failures")
_CifIkeGlobalOutXauthFailures_Type = Counter64
_CifIkeGlobalOutXauthFailures_Object = MibTableColumn
cifIkeGlobalOutXauthFailures = _CifIkeGlobalOutXauthFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 9),
    _CifIkeGlobalOutXauthFailures_Type()
)
cifIkeGlobalOutXauthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeGlobalOutXauthFailures.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeGlobalOutXauthFailures.setUnits("Failures")
_CifIkeGlobalInNewGrpReqs_Type = Counter64
_CifIkeGlobalInNewGrpReqs_Object = MibTableColumn
cifIkeGlobalInNewGrpReqs = _CifIkeGlobalInNewGrpReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 10),
    _CifIkeGlobalInNewGrpReqs_Type()
)
cifIkeGlobalInNewGrpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeGlobalInNewGrpReqs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeGlobalInNewGrpReqs.setUnits("Negotiations")
_CifIkeGlobalOutNewGrpReqs_Type = Counter64
_CifIkeGlobalOutNewGrpReqs_Object = MibTableColumn
cifIkeGlobalOutNewGrpReqs = _CifIkeGlobalOutNewGrpReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 11),
    _CifIkeGlobalOutNewGrpReqs_Type()
)
cifIkeGlobalOutNewGrpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeGlobalOutNewGrpReqs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeGlobalOutNewGrpReqs.setUnits("Negotiations")
_CifIkeGlobalInNewGrpRejectReqs_Type = Counter64
_CifIkeGlobalInNewGrpRejectReqs_Object = MibTableColumn
cifIkeGlobalInNewGrpRejectReqs = _CifIkeGlobalInNewGrpRejectReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 12),
    _CifIkeGlobalInNewGrpRejectReqs_Type()
)
cifIkeGlobalInNewGrpRejectReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeGlobalInNewGrpRejectReqs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeGlobalInNewGrpRejectReqs.setUnits("Negotiations")
_CifIkeGlobalOutNewGrpRejectReqs_Type = Counter64
_CifIkeGlobalOutNewGrpRejectReqs_Object = MibTableColumn
cifIkeGlobalOutNewGrpRejectReqs = _CifIkeGlobalOutNewGrpRejectReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 13),
    _CifIkeGlobalOutNewGrpRejectReqs_Type()
)
cifIkeGlobalOutNewGrpRejectReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeGlobalOutNewGrpRejectReqs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeGlobalOutNewGrpRejectReqs.setUnits("Negotiations")
_CifIkeTunnelTable_Object = MibTable
cifIkeTunnelTable = _CifIkeTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cifIkeTunnelTable.setStatus("current")
_CifIkeTunnelEntry_Object = MibTableRow
cifIkeTunnelEntry = _CifIkeTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1)
)
cifIkeTunnelEntry.setIndexNames(
    (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgProtocol"),
    (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunIndex"),
)
if mibBuilder.loadTexts:
    cifIkeTunnelEntry.setStatus("current")
_CifIkeTunNegoMode_Type = CIPsecIkeNegoMode
_CifIkeTunNegoMode_Object = MibTableColumn
cifIkeTunNegoMode = _CifIkeTunNegoMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 1),
    _CifIkeTunNegoMode_Type()
)
cifIkeTunNegoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunNegoMode.setStatus("current")
_CifIkeTunDHGrp_Type = CIPsecDiffHellmanGrp
_CifIkeTunDHGrp_Object = MibTableColumn
cifIkeTunDHGrp = _CifIkeTunDHGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 2),
    _CifIkeTunDHGrp_Type()
)
cifIkeTunDHGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunDHGrp.setStatus("current")


class _CifIkeTunSaRefreshThreshold_Type(Unsigned32):
    """Custom type cifIkeTunSaRefreshThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CifIkeTunSaRefreshThreshold_Type.__name__ = "Unsigned32"
_CifIkeTunSaRefreshThreshold_Object = MibTableColumn
cifIkeTunSaRefreshThreshold = _CifIkeTunSaRefreshThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 3),
    _CifIkeTunSaRefreshThreshold_Type()
)
cifIkeTunSaRefreshThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunSaRefreshThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunSaRefreshThreshold.setUnits("seconds")
_CifIkeTunTotalRefreshes_Type = Counter32
_CifIkeTunTotalRefreshes_Object = MibTableColumn
cifIkeTunTotalRefreshes = _CifIkeTunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 4),
    _CifIkeTunTotalRefreshes_Type()
)
cifIkeTunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunTotalRefreshes.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunTotalRefreshes.setUnits("QM Exchanges")
_CifIkeTunInP2Exchgs_Type = Counter32
_CifIkeTunInP2Exchgs_Object = MibTableColumn
cifIkeTunInP2Exchgs = _CifIkeTunInP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 5),
    _CifIkeTunInP2Exchgs_Type()
)
cifIkeTunInP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunInP2Exchgs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunInP2Exchgs.setUnits("SA Payloads")
_CifIkeTunInP2ExchgInvalids_Type = Counter32
_CifIkeTunInP2ExchgInvalids_Object = MibTableColumn
cifIkeTunInP2ExchgInvalids = _CifIkeTunInP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 6),
    _CifIkeTunInP2ExchgInvalids_Type()
)
cifIkeTunInP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunInP2ExchgInvalids.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunInP2ExchgInvalids.setUnits("SA Payloads")
_CifIkeTunInP2ExchgRejects_Type = Counter32
_CifIkeTunInP2ExchgRejects_Object = MibTableColumn
cifIkeTunInP2ExchgRejects = _CifIkeTunInP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 7),
    _CifIkeTunInP2ExchgRejects_Type()
)
cifIkeTunInP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunInP2ExchgRejects.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunInP2ExchgRejects.setUnits("SA Payloads")
_CifIkeTunInP2SaDelRequests_Type = Counter32
_CifIkeTunInP2SaDelRequests_Object = MibTableColumn
cifIkeTunInP2SaDelRequests = _CifIkeTunInP2SaDelRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 8),
    _CifIkeTunInP2SaDelRequests_Type()
)
cifIkeTunInP2SaDelRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunInP2SaDelRequests.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunInP2SaDelRequests.setUnits("Notification Payloads")
_CifIkeTunOutP2Exchgs_Type = Counter32
_CifIkeTunOutP2Exchgs_Object = MibTableColumn
cifIkeTunOutP2Exchgs = _CifIkeTunOutP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 9),
    _CifIkeTunOutP2Exchgs_Type()
)
cifIkeTunOutP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunOutP2Exchgs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunOutP2Exchgs.setUnits("SA Payloads")
_CifIkeTunOutP2ExchgInvalids_Type = Counter32
_CifIkeTunOutP2ExchgInvalids_Object = MibTableColumn
cifIkeTunOutP2ExchgInvalids = _CifIkeTunOutP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 10),
    _CifIkeTunOutP2ExchgInvalids_Type()
)
cifIkeTunOutP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunOutP2ExchgInvalids.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunOutP2ExchgInvalids.setUnits("SA Payloads")
_CifIkeTunOutP2ExchgRejects_Type = Counter32
_CifIkeTunOutP2ExchgRejects_Object = MibTableColumn
cifIkeTunOutP2ExchgRejects = _CifIkeTunOutP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 11),
    _CifIkeTunOutP2ExchgRejects_Type()
)
cifIkeTunOutP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunOutP2ExchgRejects.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunOutP2ExchgRejects.setUnits("SA Payloads")
_CifIkeTunInNewGrpReqs_Type = Counter32
_CifIkeTunInNewGrpReqs_Object = MibTableColumn
cifIkeTunInNewGrpReqs = _CifIkeTunInNewGrpReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 12),
    _CifIkeTunInNewGrpReqs_Type()
)
cifIkeTunInNewGrpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunInNewGrpReqs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunInNewGrpReqs.setUnits("Negotiations")
_CifIkeTunOutNewGrpReqs_Type = Counter32
_CifIkeTunOutNewGrpReqs_Object = MibTableColumn
cifIkeTunOutNewGrpReqs = _CifIkeTunOutNewGrpReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 13),
    _CifIkeTunOutNewGrpReqs_Type()
)
cifIkeTunOutNewGrpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunOutNewGrpReqs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunOutNewGrpReqs.setUnits("Negotiations")
_CifIkeTunInNewGrpRejectedReqs_Type = Counter32
_CifIkeTunInNewGrpRejectedReqs_Object = MibTableColumn
cifIkeTunInNewGrpRejectedReqs = _CifIkeTunInNewGrpRejectedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 14),
    _CifIkeTunInNewGrpRejectedReqs_Type()
)
cifIkeTunInNewGrpRejectedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunInNewGrpRejectedReqs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunInNewGrpRejectedReqs.setUnits("Negotiations")
_CifIkeTunOutNewGrpRejectedReqs_Type = Counter32
_CifIkeTunOutNewGrpRejectedReqs_Object = MibTableColumn
cifIkeTunOutNewGrpRejectedReqs = _CifIkeTunOutNewGrpRejectedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 15),
    _CifIkeTunOutNewGrpRejectedReqs_Type()
)
cifIkeTunOutNewGrpRejectedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunOutNewGrpRejectedReqs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunOutNewGrpRejectedReqs.setUnits("Negotiations")
_CifIkeTunInConfigs_Type = Counter32
_CifIkeTunInConfigs_Object = MibTableColumn
cifIkeTunInConfigs = _CifIkeTunInConfigs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 16),
    _CifIkeTunInConfigs_Type()
)
cifIkeTunInConfigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunInConfigs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunInConfigs.setUnits("Mode Configuration Setting Payloads")
_CifIkeTunOutConfigs_Type = Counter32
_CifIkeTunOutConfigs_Object = MibTableColumn
cifIkeTunOutConfigs = _CifIkeTunOutConfigs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 17),
    _CifIkeTunOutConfigs_Type()
)
cifIkeTunOutConfigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunOutConfigs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunOutConfigs.setUnits("Mode Configuration Setting Payloads")
_CifIkeTunInConfigRejects_Type = Counter32
_CifIkeTunInConfigRejects_Object = MibTableColumn
cifIkeTunInConfigRejects = _CifIkeTunInConfigRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 18),
    _CifIkeTunInConfigRejects_Type()
)
cifIkeTunInConfigRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunInConfigRejects.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunInConfigRejects.setUnits("Mode Configuration Setting Payloads")
_CifIkeTunOutConfigRejects_Type = Counter32
_CifIkeTunOutConfigRejects_Object = MibTableColumn
cifIkeTunOutConfigRejects = _CifIkeTunOutConfigRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 19),
    _CifIkeTunOutConfigRejects_Type()
)
cifIkeTunOutConfigRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunOutConfigRejects.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunOutConfigRejects.setUnits("Mode Configuration Setting Payloads")
_CifIkeHistory_ObjectIdentity = ObjectIdentity
cifIkeHistory = _CifIkeHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2)
)
_CifIkeTunnelHistTable_Object = MibTable
cifIkeTunnelHistTable = _CifIkeTunnelHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cifIkeTunnelHistTable.setStatus("current")
_CifIkeTunnelHistEntry_Object = MibTableRow
cifIkeTunnelHistEntry = _CifIkeTunnelHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1)
)
cifIkeTunnelHistEntry.setIndexNames(
    (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgProtocol"),
    (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistIndex"),
)
if mibBuilder.loadTexts:
    cifIkeTunnelHistEntry.setStatus("current")
_CifIkeTunHistNegoMode_Type = CIPsecIkeNegoMode
_CifIkeTunHistNegoMode_Object = MibTableColumn
cifIkeTunHistNegoMode = _CifIkeTunHistNegoMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 1),
    _CifIkeTunHistNegoMode_Type()
)
cifIkeTunHistNegoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistNegoMode.setStatus("current")
_CifIkeTunHistDHGrp_Type = CIPsecDiffHellmanGrp
_CifIkeTunHistDHGrp_Object = MibTableColumn
cifIkeTunHistDHGrp = _CifIkeTunHistDHGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 2),
    _CifIkeTunHistDHGrp_Type()
)
cifIkeTunHistDHGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistDHGrp.setStatus("current")
_CifIkeTunHistTotalRefreshes_Type = Counter32
_CifIkeTunHistTotalRefreshes_Object = MibTableColumn
cifIkeTunHistTotalRefreshes = _CifIkeTunHistTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 3),
    _CifIkeTunHistTotalRefreshes_Type()
)
cifIkeTunHistTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistTotalRefreshes.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunHistTotalRefreshes.setUnits("QM Exchanges")
_CifIkeTunHistTotalSas_Type = Counter32
_CifIkeTunHistTotalSas_Object = MibTableColumn
cifIkeTunHistTotalSas = _CifIkeTunHistTotalSas_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 4),
    _CifIkeTunHistTotalSas_Type()
)
cifIkeTunHistTotalSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistTotalSas.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunHistTotalSas.setUnits("SAs")
_CifIkeTunHistInP2Exchgs_Type = Counter32
_CifIkeTunHistInP2Exchgs_Object = MibTableColumn
cifIkeTunHistInP2Exchgs = _CifIkeTunHistInP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 5),
    _CifIkeTunHistInP2Exchgs_Type()
)
cifIkeTunHistInP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistInP2Exchgs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunHistInP2Exchgs.setUnits("SA Payloads")
_CifIkeTunHistInP2ExchgInvalids_Type = Counter32
_CifIkeTunHistInP2ExchgInvalids_Object = MibTableColumn
cifIkeTunHistInP2ExchgInvalids = _CifIkeTunHistInP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 6),
    _CifIkeTunHistInP2ExchgInvalids_Type()
)
cifIkeTunHistInP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistInP2ExchgInvalids.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunHistInP2ExchgInvalids.setUnits("SA Payloads")
_CifIkeTunHistInP2ExchgRejects_Type = Counter32
_CifIkeTunHistInP2ExchgRejects_Object = MibTableColumn
cifIkeTunHistInP2ExchgRejects = _CifIkeTunHistInP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 7),
    _CifIkeTunHistInP2ExchgRejects_Type()
)
cifIkeTunHistInP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistInP2ExchgRejects.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunHistInP2ExchgRejects.setUnits("SA Payloads")
_CifIkeTunHistOutP2Exchgs_Type = Counter32
_CifIkeTunHistOutP2Exchgs_Object = MibTableColumn
cifIkeTunHistOutP2Exchgs = _CifIkeTunHistOutP2Exchgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 8),
    _CifIkeTunHistOutP2Exchgs_Type()
)
cifIkeTunHistOutP2Exchgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistOutP2Exchgs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunHistOutP2Exchgs.setUnits("Notification Payloads")
_CifIkeTunHistOutP2ExchgInvalids_Type = Counter32
_CifIkeTunHistOutP2ExchgInvalids_Object = MibTableColumn
cifIkeTunHistOutP2ExchgInvalids = _CifIkeTunHistOutP2ExchgInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 9),
    _CifIkeTunHistOutP2ExchgInvalids_Type()
)
cifIkeTunHistOutP2ExchgInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistOutP2ExchgInvalids.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunHistOutP2ExchgInvalids.setUnits("SA Payloads")
_CifIkeTunHistOutP2ExchgRejects_Type = Counter32
_CifIkeTunHistOutP2ExchgRejects_Object = MibTableColumn
cifIkeTunHistOutP2ExchgRejects = _CifIkeTunHistOutP2ExchgRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 10),
    _CifIkeTunHistOutP2ExchgRejects_Type()
)
cifIkeTunHistOutP2ExchgRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistOutP2ExchgRejects.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunHistOutP2ExchgRejects.setUnits("SA Payloads")
_CifIkeTunHistInNewGrpReqs_Type = Counter32
_CifIkeTunHistInNewGrpReqs_Object = MibTableColumn
cifIkeTunHistInNewGrpReqs = _CifIkeTunHistInNewGrpReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 11),
    _CifIkeTunHistInNewGrpReqs_Type()
)
cifIkeTunHistInNewGrpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistInNewGrpReqs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunHistInNewGrpReqs.setUnits("Negotiations")
_CifIkeTunHistOutNewGrpReqs_Type = Counter32
_CifIkeTunHistOutNewGrpReqs_Object = MibTableColumn
cifIkeTunHistOutNewGrpReqs = _CifIkeTunHistOutNewGrpReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 12),
    _CifIkeTunHistOutNewGrpReqs_Type()
)
cifIkeTunHistOutNewGrpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistOutNewGrpReqs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunHistOutNewGrpReqs.setUnits("Negotiations")
_CifIkeTunHistInNewGrpRejectReqs_Type = Counter32
_CifIkeTunHistInNewGrpRejectReqs_Object = MibTableColumn
cifIkeTunHistInNewGrpRejectReqs = _CifIkeTunHistInNewGrpRejectReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 13),
    _CifIkeTunHistInNewGrpRejectReqs_Type()
)
cifIkeTunHistInNewGrpRejectReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistInNewGrpRejectReqs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunHistInNewGrpRejectReqs.setUnits("Negotiations")
_CifIkeTunHistOutNewGrpRejectReqs_Type = Counter32
_CifIkeTunHistOutNewGrpRejectReqs_Object = MibTableColumn
cifIkeTunHistOutNewGrpRejectReqs = _CifIkeTunHistOutNewGrpRejectReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 14),
    _CifIkeTunHistOutNewGrpRejectReqs_Type()
)
cifIkeTunHistOutNewGrpRejectReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistOutNewGrpRejectReqs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunHistOutNewGrpRejectReqs.setUnits("Negotiations")
_CifIkeTunHistInConfigs_Type = Counter32
_CifIkeTunHistInConfigs_Object = MibTableColumn
cifIkeTunHistInConfigs = _CifIkeTunHistInConfigs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 15),
    _CifIkeTunHistInConfigs_Type()
)
cifIkeTunHistInConfigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistInConfigs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunHistInConfigs.setUnits("Mode Configuration Setting Payloads")
_CifIkeTunHistOutConfigs_Type = Counter32
_CifIkeTunHistOutConfigs_Object = MibTableColumn
cifIkeTunHistOutConfigs = _CifIkeTunHistOutConfigs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 16),
    _CifIkeTunHistOutConfigs_Type()
)
cifIkeTunHistOutConfigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistOutConfigs.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunHistOutConfigs.setUnits("Mode Configuration Setting Payloads")
_CifIkeTunHistInConfigsRejects_Type = Counter32
_CifIkeTunHistInConfigsRejects_Object = MibTableColumn
cifIkeTunHistInConfigsRejects = _CifIkeTunHistInConfigsRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 17),
    _CifIkeTunHistInConfigsRejects_Type()
)
cifIkeTunHistInConfigsRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistInConfigsRejects.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunHistInConfigsRejects.setUnits("Mode Configuration Setting Payloads")
_CifIkeTunHistOutConfigsRejects_Type = Counter32
_CifIkeTunHistOutConfigsRejects_Object = MibTableColumn
cifIkeTunHistOutConfigsRejects = _CifIkeTunHistOutConfigsRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 18),
    _CifIkeTunHistOutConfigsRejects_Type()
)
cifIkeTunHistOutConfigsRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifIkeTunHistOutConfigsRejects.setStatus("current")
if mibBuilder.loadTexts:
    cifIkeTunHistOutConfigsRejects.setUnits("Mode Configuration Setting Payloads")
_CifIkeNotifControl_ObjectIdentity = ObjectIdentity
cifIkeNotifControl = _CifIkeNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 3)
)


class _CifIkeNotifCntlInNewGrpRejected_Type(TruthValue):
    """Custom type cifIkeNotifCntlInNewGrpRejected based on TruthValue"""


_CifIkeNotifCntlInNewGrpRejected_Object = MibScalar
cifIkeNotifCntlInNewGrpRejected = _CifIkeNotifCntlInNewGrpRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 3, 1),
    _CifIkeNotifCntlInNewGrpRejected_Type()
)
cifIkeNotifCntlInNewGrpRejected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cifIkeNotifCntlInNewGrpRejected.setStatus("current")


class _CifIkeNotifCntlOutNewGrpRejected_Type(TruthValue):
    """Custom type cifIkeNotifCntlOutNewGrpRejected based on TruthValue"""


_CifIkeNotifCntlOutNewGrpRejected_Object = MibScalar
cifIkeNotifCntlOutNewGrpRejected = _CifIkeNotifCntlOutNewGrpRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 3, 2),
    _CifIkeNotifCntlOutNewGrpRejected_Type()
)
cifIkeNotifCntlOutNewGrpRejected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cifIkeNotifCntlOutNewGrpRejected.setStatus("current")
_CiscoIkeFlowMIBConform_ObjectIdentity = ObjectIdentity
ciscoIkeFlowMIBConform = _CiscoIkeFlowMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 2)
)
_CiscoIkeFlowMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIkeFlowMIBCompliances = _CiscoIkeFlowMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 1)
)
_CiscoIkeFlowMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIkeFlowMIBGroups = _CiscoIkeFlowMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2)
)

# Managed Objects groups

ciscoIkeFlowActivityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 1)
)
ciscoIkeFlowActivityGroup.setObjects(
      *(("CISCO-IKE-FLOW-MIB", "cifIkeGlobalInP2Exchgs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalInP2ExchgInvalids"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalInP2ExchgRejects"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalOutP2Exchgs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalOutP2ExchgInvalids"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalOutP2ExchgRejects"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunNegoMode"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunDHGrp"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunSaRefreshThreshold"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunTotalRefreshes"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunInP2Exchgs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunInP2ExchgInvalids"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunInP2ExchgRejects"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunInP2SaDelRequests"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunOutP2Exchgs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunOutP2ExchgInvalids"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunOutP2ExchgRejects"))
)
if mibBuilder.loadTexts:
    ciscoIkeFlowActivityGroup.setStatus("current")

cifIkeFlowNewGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 2)
)
cifIkeFlowNewGroupGroup.setObjects(
      *(("CISCO-IKE-FLOW-MIB", "cifIkeGlobalInNewGrpReqs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalOutNewGrpReqs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalInNewGrpRejectReqs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalOutNewGrpRejectReqs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunInNewGrpReqs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunOutNewGrpReqs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunInNewGrpRejectedReqs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunOutNewGrpRejectedReqs"))
)
if mibBuilder.loadTexts:
    cifIkeFlowNewGroupGroup.setStatus("current")

cifIkeFlowXauthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 3)
)
cifIkeFlowXauthGroup.setObjects(
      *(("CISCO-IKE-FLOW-MIB", "cifIkeGlobalInXauths"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalInXauthFailures"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalOutXauthFailures"))
)
if mibBuilder.loadTexts:
    cifIkeFlowXauthGroup.setStatus("current")

cifIkeFlowModeConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 4)
)
cifIkeFlowModeConfigGroup.setObjects(
      *(("CISCO-IKE-FLOW-MIB", "cifIkeTunInConfigs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunOutConfigs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunInConfigRejects"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunOutConfigRejects"))
)
if mibBuilder.loadTexts:
    cifIkeFlowModeConfigGroup.setStatus("current")

cifIkeFlowHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 5)
)
cifIkeFlowHistoryGroup.setObjects(
      *(("CISCO-IKE-FLOW-MIB", "cifIkeTunHistNegoMode"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistDHGrp"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistTotalRefreshes"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistTotalSas"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistInP2Exchgs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistInP2ExchgInvalids"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistInP2ExchgRejects"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistOutP2Exchgs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistOutP2ExchgInvalids"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistOutP2ExchgRejects"))
)
if mibBuilder.loadTexts:
    cifIkeFlowHistoryGroup.setStatus("current")

cifIkeFlowNewGroupHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 6)
)
cifIkeFlowNewGroupHistoryGroup.setObjects(
      *(("CISCO-IKE-FLOW-MIB", "cifIkeTunHistInNewGrpReqs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistOutNewGrpReqs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistInNewGrpRejectReqs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistOutNewGrpRejectReqs"))
)
if mibBuilder.loadTexts:
    cifIkeFlowNewGroupHistoryGroup.setStatus("current")

cifIkeFlowModeConfigHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 7)
)
cifIkeFlowModeConfigHistoryGroup.setObjects(
      *(("CISCO-IKE-FLOW-MIB", "cifIkeTunHistInConfigs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistOutConfigs"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistInConfigsRejects"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistOutConfigsRejects"))
)
if mibBuilder.loadTexts:
    cifIkeFlowModeConfigHistoryGroup.setStatus("current")

cifIkeFlowNotifCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 8)
)
cifIkeFlowNotifCntlGroup.setObjects(
      *(("CISCO-IKE-FLOW-MIB", "cifIkeNotifCntlInNewGrpRejected"),
        ("CISCO-IKE-FLOW-MIB", "cifIkeNotifCntlOutNewGrpRejected"))
)
if mibBuilder.loadTexts:
    cifIkeFlowNotifCntlGroup.setStatus("current")


# Notification objects

ciscoIkeFlowInNewGrpRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 0, 1)
)
ciscoIkeFlowInNewGrpRejected.setObjects(
      *(("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailLocalAddress"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailRemoteAddress"))
)
if mibBuilder.loadTexts:
    ciscoIkeFlowInNewGrpRejected.setStatus(
        "current"
    )

ciscoIkeFlowOutNewGrpRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 0, 2)
)
ciscoIkeFlowOutNewGrpRejected.setObjects(
      *(("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailLocalAddress"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailRemoteAddress"))
)
if mibBuilder.loadTexts:
    ciscoIkeFlowOutNewGrpRejected.setStatus(
        "current"
    )


# Notifications groups

cifIkeFlowNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 9)
)
cifIkeFlowNotificationGroup.setObjects(
      *(("CISCO-IKE-FLOW-MIB", "ciscoIkeFlowInNewGrpRejected"),
        ("CISCO-IKE-FLOW-MIB", "ciscoIkeFlowOutNewGrpRejected"))
)
if mibBuilder.loadTexts:
    cifIkeFlowNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoIkeFlowMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIkeFlowMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IKE-FLOW-MIB",
    **{"ciscoIkeFlowMIB": ciscoIkeFlowMIB,
       "ciscoIkeFlowMIBNotifs": ciscoIkeFlowMIBNotifs,
       "ciscoIkeFlowInNewGrpRejected": ciscoIkeFlowInNewGrpRejected,
       "ciscoIkeFlowOutNewGrpRejected": ciscoIkeFlowOutNewGrpRejected,
       "ciscoIkeFlowMIBObjects": ciscoIkeFlowMIBObjects,
       "cifIkeCurrentActivity": cifIkeCurrentActivity,
       "cifIkeGlobalStatsTable": cifIkeGlobalStatsTable,
       "cifIkeGlobalStatsEntry": cifIkeGlobalStatsEntry,
       "cifIkeGlobalInP2Exchgs": cifIkeGlobalInP2Exchgs,
       "cifIkeGlobalInP2ExchgInvalids": cifIkeGlobalInP2ExchgInvalids,
       "cifIkeGlobalInP2ExchgRejects": cifIkeGlobalInP2ExchgRejects,
       "cifIkeGlobalOutP2Exchgs": cifIkeGlobalOutP2Exchgs,
       "cifIkeGlobalOutP2ExchgInvalids": cifIkeGlobalOutP2ExchgInvalids,
       "cifIkeGlobalOutP2ExchgRejects": cifIkeGlobalOutP2ExchgRejects,
       "cifIkeGlobalInXauths": cifIkeGlobalInXauths,
       "cifIkeGlobalInXauthFailures": cifIkeGlobalInXauthFailures,
       "cifIkeGlobalOutXauthFailures": cifIkeGlobalOutXauthFailures,
       "cifIkeGlobalInNewGrpReqs": cifIkeGlobalInNewGrpReqs,
       "cifIkeGlobalOutNewGrpReqs": cifIkeGlobalOutNewGrpReqs,
       "cifIkeGlobalInNewGrpRejectReqs": cifIkeGlobalInNewGrpRejectReqs,
       "cifIkeGlobalOutNewGrpRejectReqs": cifIkeGlobalOutNewGrpRejectReqs,
       "cifIkeTunnelTable": cifIkeTunnelTable,
       "cifIkeTunnelEntry": cifIkeTunnelEntry,
       "cifIkeTunNegoMode": cifIkeTunNegoMode,
       "cifIkeTunDHGrp": cifIkeTunDHGrp,
       "cifIkeTunSaRefreshThreshold": cifIkeTunSaRefreshThreshold,
       "cifIkeTunTotalRefreshes": cifIkeTunTotalRefreshes,
       "cifIkeTunInP2Exchgs": cifIkeTunInP2Exchgs,
       "cifIkeTunInP2ExchgInvalids": cifIkeTunInP2ExchgInvalids,
       "cifIkeTunInP2ExchgRejects": cifIkeTunInP2ExchgRejects,
       "cifIkeTunInP2SaDelRequests": cifIkeTunInP2SaDelRequests,
       "cifIkeTunOutP2Exchgs": cifIkeTunOutP2Exchgs,
       "cifIkeTunOutP2ExchgInvalids": cifIkeTunOutP2ExchgInvalids,
       "cifIkeTunOutP2ExchgRejects": cifIkeTunOutP2ExchgRejects,
       "cifIkeTunInNewGrpReqs": cifIkeTunInNewGrpReqs,
       "cifIkeTunOutNewGrpReqs": cifIkeTunOutNewGrpReqs,
       "cifIkeTunInNewGrpRejectedReqs": cifIkeTunInNewGrpRejectedReqs,
       "cifIkeTunOutNewGrpRejectedReqs": cifIkeTunOutNewGrpRejectedReqs,
       "cifIkeTunInConfigs": cifIkeTunInConfigs,
       "cifIkeTunOutConfigs": cifIkeTunOutConfigs,
       "cifIkeTunInConfigRejects": cifIkeTunInConfigRejects,
       "cifIkeTunOutConfigRejects": cifIkeTunOutConfigRejects,
       "cifIkeHistory": cifIkeHistory,
       "cifIkeTunnelHistTable": cifIkeTunnelHistTable,
       "cifIkeTunnelHistEntry": cifIkeTunnelHistEntry,
       "cifIkeTunHistNegoMode": cifIkeTunHistNegoMode,
       "cifIkeTunHistDHGrp": cifIkeTunHistDHGrp,
       "cifIkeTunHistTotalRefreshes": cifIkeTunHistTotalRefreshes,
       "cifIkeTunHistTotalSas": cifIkeTunHistTotalSas,
       "cifIkeTunHistInP2Exchgs": cifIkeTunHistInP2Exchgs,
       "cifIkeTunHistInP2ExchgInvalids": cifIkeTunHistInP2ExchgInvalids,
       "cifIkeTunHistInP2ExchgRejects": cifIkeTunHistInP2ExchgRejects,
       "cifIkeTunHistOutP2Exchgs": cifIkeTunHistOutP2Exchgs,
       "cifIkeTunHistOutP2ExchgInvalids": cifIkeTunHistOutP2ExchgInvalids,
       "cifIkeTunHistOutP2ExchgRejects": cifIkeTunHistOutP2ExchgRejects,
       "cifIkeTunHistInNewGrpReqs": cifIkeTunHistInNewGrpReqs,
       "cifIkeTunHistOutNewGrpReqs": cifIkeTunHistOutNewGrpReqs,
       "cifIkeTunHistInNewGrpRejectReqs": cifIkeTunHistInNewGrpRejectReqs,
       "cifIkeTunHistOutNewGrpRejectReqs": cifIkeTunHistOutNewGrpRejectReqs,
       "cifIkeTunHistInConfigs": cifIkeTunHistInConfigs,
       "cifIkeTunHistOutConfigs": cifIkeTunHistOutConfigs,
       "cifIkeTunHistInConfigsRejects": cifIkeTunHistInConfigsRejects,
       "cifIkeTunHistOutConfigsRejects": cifIkeTunHistOutConfigsRejects,
       "cifIkeNotifControl": cifIkeNotifControl,
       "cifIkeNotifCntlInNewGrpRejected": cifIkeNotifCntlInNewGrpRejected,
       "cifIkeNotifCntlOutNewGrpRejected": cifIkeNotifCntlOutNewGrpRejected,
       "ciscoIkeFlowMIBConform": ciscoIkeFlowMIBConform,
       "ciscoIkeFlowMIBCompliances": ciscoIkeFlowMIBCompliances,
       "ciscoIkeFlowMIBCompliance": ciscoIkeFlowMIBCompliance,
       "ciscoIkeFlowMIBGroups": ciscoIkeFlowMIBGroups,
       "ciscoIkeFlowActivityGroup": ciscoIkeFlowActivityGroup,
       "cifIkeFlowNewGroupGroup": cifIkeFlowNewGroupGroup,
       "cifIkeFlowXauthGroup": cifIkeFlowXauthGroup,
       "cifIkeFlowModeConfigGroup": cifIkeFlowModeConfigGroup,
       "cifIkeFlowHistoryGroup": cifIkeFlowHistoryGroup,
       "cifIkeFlowNewGroupHistoryGroup": cifIkeFlowNewGroupHistoryGroup,
       "cifIkeFlowModeConfigHistoryGroup": cifIkeFlowModeConfigHistoryGroup,
       "cifIkeFlowNotifCntlGroup": cifIkeFlowNotifCntlGroup,
       "cifIkeFlowNotificationGroup": cifIkeFlowNotificationGroup}
)
