# SNMP MIB module (PDN-PPP-LCP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-PPP-LCP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:01 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdn_interfaces,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-interfaces")

(PdnPPPState,
 SwitchState) = mibBuilder.importSymbols(
    "PDN-TC",
    "PdnPPPState",
    "SwitchState")

(pppLinkConfigEntry,
 pppLinkStatusEntry) = mibBuilder.importSymbols(
    "PPP-LCP-MIB",
    "pppLinkConfigEntry",
    "pppLinkStatusEntry")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

pdnPppLcpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28)
)
pdnPppLcpExtMIB.setRevisions(
        ("2004-09-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnPppLcpExtNotifications_ObjectIdentity = ObjectIdentity
pdnPppLcpExtNotifications = _PdnPppLcpExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 0)
)
_PdnPppLcpExtObjects_ObjectIdentity = ObjectIdentity
pdnPppLcpExtObjects = _PdnPppLcpExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1)
)
_PdnPppLinkStatusExtTable_Object = MibTable
pdnPppLinkStatusExtTable = _PdnPppLinkStatusExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1)
)
if mibBuilder.loadTexts:
    pdnPppLinkStatusExtTable.setStatus("current")
_PdnPppLinkStatusExtEntry_Object = MibTableRow
pdnPppLinkStatusExtEntry = _PdnPppLinkStatusExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pdnPppLinkStatusExtEntry.setStatus("current")
_PdnPppLinkStatusCurrState_Type = PdnPPPState
_PdnPppLinkStatusCurrState_Object = MibTableColumn
pdnPppLinkStatusCurrState = _PdnPppLinkStatusCurrState_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 1),
    _PdnPppLinkStatusCurrState_Type()
)
pdnPppLinkStatusCurrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusCurrState.setStatus("current")
_PdnPppLinkStatusEstablishFailedReason_Type = DisplayString
_PdnPppLinkStatusEstablishFailedReason_Object = MibTableColumn
pdnPppLinkStatusEstablishFailedReason = _PdnPppLinkStatusEstablishFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 2),
    _PdnPppLinkStatusEstablishFailedReason_Type()
)
pdnPppLinkStatusEstablishFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusEstablishFailedReason.setStatus("current")
_PdnPppLinkStatusLocalToRemoteMagicNumber_Type = Unsigned32
_PdnPppLinkStatusLocalToRemoteMagicNumber_Object = MibTableColumn
pdnPppLinkStatusLocalToRemoteMagicNumber = _PdnPppLinkStatusLocalToRemoteMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 3),
    _PdnPppLinkStatusLocalToRemoteMagicNumber_Type()
)
pdnPppLinkStatusLocalToRemoteMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusLocalToRemoteMagicNumber.setStatus("current")
_PdnPppLinkStatusRemoteToLocalMagicNumber_Type = Unsigned32
_PdnPppLinkStatusRemoteToLocalMagicNumber_Object = MibTableColumn
pdnPppLinkStatusRemoteToLocalMagicNumber = _PdnPppLinkStatusRemoteToLocalMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 4),
    _PdnPppLinkStatusRemoteToLocalMagicNumber_Type()
)
pdnPppLinkStatusRemoteToLocalMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusRemoteToLocalMagicNumber.setStatus("current")
_PdnPppLinkStatusTotalSentConfigRequests_Type = Counter32
_PdnPppLinkStatusTotalSentConfigRequests_Object = MibTableColumn
pdnPppLinkStatusTotalSentConfigRequests = _PdnPppLinkStatusTotalSentConfigRequests_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 5),
    _PdnPppLinkStatusTotalSentConfigRequests_Type()
)
pdnPppLinkStatusTotalSentConfigRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalSentConfigRequests.setStatus("current")
_PdnPppLinkStatusTotalReceivedConfigRequests_Type = Counter32
_PdnPppLinkStatusTotalReceivedConfigRequests_Object = MibTableColumn
pdnPppLinkStatusTotalReceivedConfigRequests = _PdnPppLinkStatusTotalReceivedConfigRequests_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 6),
    _PdnPppLinkStatusTotalReceivedConfigRequests_Type()
)
pdnPppLinkStatusTotalReceivedConfigRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalReceivedConfigRequests.setStatus("current")
_PdnPppLinkStatusTotalSentConfigAcks_Type = Counter32
_PdnPppLinkStatusTotalSentConfigAcks_Object = MibTableColumn
pdnPppLinkStatusTotalSentConfigAcks = _PdnPppLinkStatusTotalSentConfigAcks_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 7),
    _PdnPppLinkStatusTotalSentConfigAcks_Type()
)
pdnPppLinkStatusTotalSentConfigAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalSentConfigAcks.setStatus("current")
_PdnPppLinkStatusTotalReceivedConfigAcks_Type = Counter32
_PdnPppLinkStatusTotalReceivedConfigAcks_Object = MibTableColumn
pdnPppLinkStatusTotalReceivedConfigAcks = _PdnPppLinkStatusTotalReceivedConfigAcks_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 8),
    _PdnPppLinkStatusTotalReceivedConfigAcks_Type()
)
pdnPppLinkStatusTotalReceivedConfigAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalReceivedConfigAcks.setStatus("current")
_PdnPppLinkStatusTotalSentConfigNaks_Type = Counter32
_PdnPppLinkStatusTotalSentConfigNaks_Object = MibTableColumn
pdnPppLinkStatusTotalSentConfigNaks = _PdnPppLinkStatusTotalSentConfigNaks_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 9),
    _PdnPppLinkStatusTotalSentConfigNaks_Type()
)
pdnPppLinkStatusTotalSentConfigNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalSentConfigNaks.setStatus("current")
_PdnPppLinkStatusTotalReceivedConfigNaks_Type = Counter32
_PdnPppLinkStatusTotalReceivedConfigNaks_Object = MibTableColumn
pdnPppLinkStatusTotalReceivedConfigNaks = _PdnPppLinkStatusTotalReceivedConfigNaks_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 10),
    _PdnPppLinkStatusTotalReceivedConfigNaks_Type()
)
pdnPppLinkStatusTotalReceivedConfigNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalReceivedConfigNaks.setStatus("current")
_PdnPppLinkStatusTotalSentConfigRejects_Type = Counter32
_PdnPppLinkStatusTotalSentConfigRejects_Object = MibTableColumn
pdnPppLinkStatusTotalSentConfigRejects = _PdnPppLinkStatusTotalSentConfigRejects_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 11),
    _PdnPppLinkStatusTotalSentConfigRejects_Type()
)
pdnPppLinkStatusTotalSentConfigRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalSentConfigRejects.setStatus("current")
_PdnPppLinkStatusTotalReceivedConfigRejects_Type = Counter32
_PdnPppLinkStatusTotalReceivedConfigRejects_Object = MibTableColumn
pdnPppLinkStatusTotalReceivedConfigRejects = _PdnPppLinkStatusTotalReceivedConfigRejects_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 12),
    _PdnPppLinkStatusTotalReceivedConfigRejects_Type()
)
pdnPppLinkStatusTotalReceivedConfigRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalReceivedConfigRejects.setStatus("current")
_PdnPppLinkStatusTotalSentTerminateRequests_Type = Counter32
_PdnPppLinkStatusTotalSentTerminateRequests_Object = MibTableColumn
pdnPppLinkStatusTotalSentTerminateRequests = _PdnPppLinkStatusTotalSentTerminateRequests_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 13),
    _PdnPppLinkStatusTotalSentTerminateRequests_Type()
)
pdnPppLinkStatusTotalSentTerminateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalSentTerminateRequests.setStatus("current")
_PdnPppLinkStatusTotalReceivedTerminateRequests_Type = Counter32
_PdnPppLinkStatusTotalReceivedTerminateRequests_Object = MibTableColumn
pdnPppLinkStatusTotalReceivedTerminateRequests = _PdnPppLinkStatusTotalReceivedTerminateRequests_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 14),
    _PdnPppLinkStatusTotalReceivedTerminateRequests_Type()
)
pdnPppLinkStatusTotalReceivedTerminateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalReceivedTerminateRequests.setStatus("current")
_PdnPppLinkStatusTotalSentTerminateAcks_Type = Counter32
_PdnPppLinkStatusTotalSentTerminateAcks_Object = MibTableColumn
pdnPppLinkStatusTotalSentTerminateAcks = _PdnPppLinkStatusTotalSentTerminateAcks_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 15),
    _PdnPppLinkStatusTotalSentTerminateAcks_Type()
)
pdnPppLinkStatusTotalSentTerminateAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalSentTerminateAcks.setStatus("current")
_PdnPppLinkStatusTotalReceivedTerminateAcks_Type = Counter32
_PdnPppLinkStatusTotalReceivedTerminateAcks_Object = MibTableColumn
pdnPppLinkStatusTotalReceivedTerminateAcks = _PdnPppLinkStatusTotalReceivedTerminateAcks_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 16),
    _PdnPppLinkStatusTotalReceivedTerminateAcks_Type()
)
pdnPppLinkStatusTotalReceivedTerminateAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalReceivedTerminateAcks.setStatus("current")
_PdnPppLinkStatusTotalSentCodeRejects_Type = Counter32
_PdnPppLinkStatusTotalSentCodeRejects_Object = MibTableColumn
pdnPppLinkStatusTotalSentCodeRejects = _PdnPppLinkStatusTotalSentCodeRejects_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 17),
    _PdnPppLinkStatusTotalSentCodeRejects_Type()
)
pdnPppLinkStatusTotalSentCodeRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalSentCodeRejects.setStatus("current")
_PdnPppLinkStatusTotalReceivedCodeRejects_Type = Counter32
_PdnPppLinkStatusTotalReceivedCodeRejects_Object = MibTableColumn
pdnPppLinkStatusTotalReceivedCodeRejects = _PdnPppLinkStatusTotalReceivedCodeRejects_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 18),
    _PdnPppLinkStatusTotalReceivedCodeRejects_Type()
)
pdnPppLinkStatusTotalReceivedCodeRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalReceivedCodeRejects.setStatus("current")
_PdnPppLinkStatusTotalSentProtocolRejects_Type = Counter32
_PdnPppLinkStatusTotalSentProtocolRejects_Object = MibTableColumn
pdnPppLinkStatusTotalSentProtocolRejects = _PdnPppLinkStatusTotalSentProtocolRejects_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 19),
    _PdnPppLinkStatusTotalSentProtocolRejects_Type()
)
pdnPppLinkStatusTotalSentProtocolRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalSentProtocolRejects.setStatus("current")
_PdnPppLinkStatusTotalReceivedProtocolRejects_Type = Counter32
_PdnPppLinkStatusTotalReceivedProtocolRejects_Object = MibTableColumn
pdnPppLinkStatusTotalReceivedProtocolRejects = _PdnPppLinkStatusTotalReceivedProtocolRejects_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 20),
    _PdnPppLinkStatusTotalReceivedProtocolRejects_Type()
)
pdnPppLinkStatusTotalReceivedProtocolRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalReceivedProtocolRejects.setStatus("current")
_PdnPppLinkStatusTotalSentEchoRequests_Type = Counter32
_PdnPppLinkStatusTotalSentEchoRequests_Object = MibTableColumn
pdnPppLinkStatusTotalSentEchoRequests = _PdnPppLinkStatusTotalSentEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 21),
    _PdnPppLinkStatusTotalSentEchoRequests_Type()
)
pdnPppLinkStatusTotalSentEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalSentEchoRequests.setStatus("current")
_PdnPppLinkStatusTotalReceivedEchoRequests_Type = Counter32
_PdnPppLinkStatusTotalReceivedEchoRequests_Object = MibTableColumn
pdnPppLinkStatusTotalReceivedEchoRequests = _PdnPppLinkStatusTotalReceivedEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 22),
    _PdnPppLinkStatusTotalReceivedEchoRequests_Type()
)
pdnPppLinkStatusTotalReceivedEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalReceivedEchoRequests.setStatus("current")
_PdnPppLinkStatusTotalSentEchoReplies_Type = Counter32
_PdnPppLinkStatusTotalSentEchoReplies_Object = MibTableColumn
pdnPppLinkStatusTotalSentEchoReplies = _PdnPppLinkStatusTotalSentEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 23),
    _PdnPppLinkStatusTotalSentEchoReplies_Type()
)
pdnPppLinkStatusTotalSentEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalSentEchoReplies.setStatus("current")
_PdnPppLinkStatusTotalReceivedEchoReplies_Type = Counter32
_PdnPppLinkStatusTotalReceivedEchoReplies_Object = MibTableColumn
pdnPppLinkStatusTotalReceivedEchoReplies = _PdnPppLinkStatusTotalReceivedEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 24),
    _PdnPppLinkStatusTotalReceivedEchoReplies_Type()
)
pdnPppLinkStatusTotalReceivedEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalReceivedEchoReplies.setStatus("current")
_PdnPppLinkStatusTotalSentDiscardRequests_Type = Counter32
_PdnPppLinkStatusTotalSentDiscardRequests_Object = MibTableColumn
pdnPppLinkStatusTotalSentDiscardRequests = _PdnPppLinkStatusTotalSentDiscardRequests_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 25),
    _PdnPppLinkStatusTotalSentDiscardRequests_Type()
)
pdnPppLinkStatusTotalSentDiscardRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalSentDiscardRequests.setStatus("current")
_PdnPppLinkStatusTotalReceivedDiscardRequests_Type = Counter32
_PdnPppLinkStatusTotalReceivedDiscardRequests_Object = MibTableColumn
pdnPppLinkStatusTotalReceivedDiscardRequests = _PdnPppLinkStatusTotalReceivedDiscardRequests_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 26),
    _PdnPppLinkStatusTotalReceivedDiscardRequests_Type()
)
pdnPppLinkStatusTotalReceivedDiscardRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalReceivedDiscardRequests.setStatus("current")
_PdnPppLinkStatusTotalSentKeepAlives_Type = Counter32
_PdnPppLinkStatusTotalSentKeepAlives_Object = MibTableColumn
pdnPppLinkStatusTotalSentKeepAlives = _PdnPppLinkStatusTotalSentKeepAlives_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 27),
    _PdnPppLinkStatusTotalSentKeepAlives_Type()
)
pdnPppLinkStatusTotalSentKeepAlives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalSentKeepAlives.setStatus("current")
_PdnPppLinkStatusTotalReceivedKeepAlives_Type = Counter32
_PdnPppLinkStatusTotalReceivedKeepAlives_Object = MibTableColumn
pdnPppLinkStatusTotalReceivedKeepAlives = _PdnPppLinkStatusTotalReceivedKeepAlives_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 28),
    _PdnPppLinkStatusTotalReceivedKeepAlives_Type()
)
pdnPppLinkStatusTotalReceivedKeepAlives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalReceivedKeepAlives.setStatus("current")
_PdnPppLinkStatusTotalEchoRequestsTimeOuts_Type = Counter32
_PdnPppLinkStatusTotalEchoRequestsTimeOuts_Object = MibTableColumn
pdnPppLinkStatusTotalEchoRequestsTimeOuts = _PdnPppLinkStatusTotalEchoRequestsTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 29),
    _PdnPppLinkStatusTotalEchoRequestsTimeOuts_Type()
)
pdnPppLinkStatusTotalEchoRequestsTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalEchoRequestsTimeOuts.setStatus("current")
_PdnPppLinkStatusTotalEchoRequestsBadData_Type = Counter32
_PdnPppLinkStatusTotalEchoRequestsBadData_Object = MibTableColumn
pdnPppLinkStatusTotalEchoRequestsBadData = _PdnPppLinkStatusTotalEchoRequestsBadData_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 30),
    _PdnPppLinkStatusTotalEchoRequestsBadData_Type()
)
pdnPppLinkStatusTotalEchoRequestsBadData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalEchoRequestsBadData.setStatus("current")
_PdnPppLinkStatusTotalEchoRequestsPassed_Type = Counter32
_PdnPppLinkStatusTotalEchoRequestsPassed_Object = MibTableColumn
pdnPppLinkStatusTotalEchoRequestsPassed = _PdnPppLinkStatusTotalEchoRequestsPassed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 31),
    _PdnPppLinkStatusTotalEchoRequestsPassed_Type()
)
pdnPppLinkStatusTotalEchoRequestsPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalEchoRequestsPassed.setStatus("current")
_PdnPppLinkStatusTotalKeepAlivesLost_Type = Counter32
_PdnPppLinkStatusTotalKeepAlivesLost_Object = MibTableColumn
pdnPppLinkStatusTotalKeepAlivesLost = _PdnPppLinkStatusTotalKeepAlivesLost_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 32),
    _PdnPppLinkStatusTotalKeepAlivesLost_Type()
)
pdnPppLinkStatusTotalKeepAlivesLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalKeepAlivesLost.setStatus("current")
_PdnPppLinkStatusTotalTerminates_Type = Counter32
_PdnPppLinkStatusTotalTerminates_Object = MibTableColumn
pdnPppLinkStatusTotalTerminates = _PdnPppLinkStatusTotalTerminates_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 1, 1, 33),
    _PdnPppLinkStatusTotalTerminates_Type()
)
pdnPppLinkStatusTotalTerminates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkStatusTotalTerminates.setStatus("current")
_PdnPppLinkConfigExtTable_Object = MibTable
pdnPppLinkConfigExtTable = _PdnPppLinkConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 2)
)
if mibBuilder.loadTexts:
    pdnPppLinkConfigExtTable.setStatus("current")
_PdnPppLinkConfigExtEntry_Object = MibTableRow
pdnPppLinkConfigExtEntry = _PdnPppLinkConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pdnPppLinkConfigExtEntry.setStatus("current")
_PdnPppLinkConfigPFC_Type = SwitchState
_PdnPppLinkConfigPFC_Object = MibTableColumn
pdnPppLinkConfigPFC = _PdnPppLinkConfigPFC_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 2, 1, 1),
    _PdnPppLinkConfigPFC_Type()
)
pdnPppLinkConfigPFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPppLinkConfigPFC.setStatus("current")
_PdnPppLinkConfigACFC_Type = SwitchState
_PdnPppLinkConfigACFC_Object = MibTableColumn
pdnPppLinkConfigACFC = _PdnPppLinkConfigACFC_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 2, 1, 2),
    _PdnPppLinkConfigACFC_Type()
)
pdnPppLinkConfigACFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPppLinkConfigACFC.setStatus("current")


class _PdnPppLinkConfigKeepAliveQuietTime_Type(Unsigned32):
    """Custom type pdnPppLinkConfigKeepAliveQuietTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_PdnPppLinkConfigKeepAliveQuietTime_Type.__name__ = "Unsigned32"
_PdnPppLinkConfigKeepAliveQuietTime_Object = MibTableColumn
pdnPppLinkConfigKeepAliveQuietTime = _PdnPppLinkConfigKeepAliveQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 2, 1, 3),
    _PdnPppLinkConfigKeepAliveQuietTime_Type()
)
pdnPppLinkConfigKeepAliveQuietTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPppLinkConfigKeepAliveQuietTime.setStatus("current")
if mibBuilder.loadTexts:
    pdnPppLinkConfigKeepAliveQuietTime.setUnits("seconds")


class _PdnPppLinkConfigKeepAliveTimeout_Type(Unsigned32):
    """Custom type pdnPppLinkConfigKeepAliveTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_PdnPppLinkConfigKeepAliveTimeout_Type.__name__ = "Unsigned32"
_PdnPppLinkConfigKeepAliveTimeout_Object = MibTableColumn
pdnPppLinkConfigKeepAliveTimeout = _PdnPppLinkConfigKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 2, 1, 4),
    _PdnPppLinkConfigKeepAliveTimeout_Type()
)
pdnPppLinkConfigKeepAliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPppLinkConfigKeepAliveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pdnPppLinkConfigKeepAliveTimeout.setUnits("seconds")
_PdnPppLinkTestTable_Object = MibTable
pdnPppLinkTestTable = _PdnPppLinkTestTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 3)
)
if mibBuilder.loadTexts:
    pdnPppLinkTestTable.setStatus("current")
_PdnPppLinkTestEntry_Object = MibTableRow
pdnPppLinkTestEntry = _PdnPppLinkTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 3, 1)
)
pdnPppLinkTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnPppLinkTestEntry.setStatus("current")


class _PdnPppLinkTestSendEchoTest_Type(Integer32):
    """Custom type pdnPppLinkTestSendEchoTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("runTest", 2))
    )


_PdnPppLinkTestSendEchoTest_Type.__name__ = "Integer32"
_PdnPppLinkTestSendEchoTest_Object = MibTableColumn
pdnPppLinkTestSendEchoTest = _PdnPppLinkTestSendEchoTest_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 3, 1, 1),
    _PdnPppLinkTestSendEchoTest_Type()
)
pdnPppLinkTestSendEchoTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPppLinkTestSendEchoTest.setStatus("current")


class _PdnPppLinkTestEchoTestTimeout_Type(Unsigned32):
    """Custom type pdnPppLinkTestEchoTestTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_PdnPppLinkTestEchoTestTimeout_Type.__name__ = "Unsigned32"
_PdnPppLinkTestEchoTestTimeout_Object = MibTableColumn
pdnPppLinkTestEchoTestTimeout = _PdnPppLinkTestEchoTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 3, 1, 2),
    _PdnPppLinkTestEchoTestTimeout_Type()
)
pdnPppLinkTestEchoTestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPppLinkTestEchoTestTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pdnPppLinkTestEchoTestTimeout.setUnits("seconds")


class _PdnPppLinkTestSendDiscardTest_Type(Integer32):
    """Custom type pdnPppLinkTestSendDiscardTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("sendDiscard", 2))
    )


_PdnPppLinkTestSendDiscardTest_Type.__name__ = "Integer32"
_PdnPppLinkTestSendDiscardTest_Object = MibTableColumn
pdnPppLinkTestSendDiscardTest = _PdnPppLinkTestSendDiscardTest_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 3, 1, 3),
    _PdnPppLinkTestSendDiscardTest_Type()
)
pdnPppLinkTestSendDiscardTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPppLinkTestSendDiscardTest.setStatus("current")


class _PdnPppLinkTestLastEchoTestResults_Type(Integer32):
    """Custom type pdnPppLinkTestLastEchoTestResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("compareFailed", 5),
          ("inProgress", 2),
          ("none", 1),
          ("success", 3),
          ("timedOut", 4))
    )


_PdnPppLinkTestLastEchoTestResults_Type.__name__ = "Integer32"
_PdnPppLinkTestLastEchoTestResults_Object = MibTableColumn
pdnPppLinkTestLastEchoTestResults = _PdnPppLinkTestLastEchoTestResults_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 1, 3, 1, 4),
    _PdnPppLinkTestLastEchoTestResults_Type()
)
pdnPppLinkTestLastEchoTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppLinkTestLastEchoTestResults.setStatus("current")
_PdnPppLcpExtAFNs_ObjectIdentity = ObjectIdentity
pdnPppLcpExtAFNs = _PdnPppLcpExtAFNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 2)
)
_PdnPppLcpExtConformance_ObjectIdentity = ObjectIdentity
pdnPppLcpExtConformance = _PdnPppLcpExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3)
)
_PdnPppLcpExtCompliances_ObjectIdentity = ObjectIdentity
pdnPppLcpExtCompliances = _PdnPppLcpExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3, 1)
)
_PdnPppLcpExtGroups_ObjectIdentity = ObjectIdentity
pdnPppLcpExtGroups = _PdnPppLcpExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3, 2)
)
_PdnPppLcpExtObjGroups_ObjectIdentity = ObjectIdentity
pdnPppLcpExtObjGroups = _PdnPppLcpExtObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3, 2, 1)
)
_PdnPppLcpExtAfnGroups_ObjectIdentity = ObjectIdentity
pdnPppLcpExtAfnGroups = _PdnPppLcpExtAfnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3, 2, 2)
)
_PdnPppLcpExtNtfyGroups_ObjectIdentity = ObjectIdentity
pdnPppLcpExtNtfyGroups = _PdnPppLcpExtNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3, 2, 3)
)
pppLinkStatusEntry.registerAugmentions(
    ("PDN-PPP-LCP-EXT-MIB",
     "pdnPppLinkStatusExtEntry")
)
pdnPppLinkStatusExtEntry.setIndexNames(*pppLinkStatusEntry.getIndexNames())
pppLinkConfigEntry.registerAugmentions(
    ("PDN-PPP-LCP-EXT-MIB",
     "pdnPppLinkConfigExtEntry")
)
pdnPppLinkConfigExtEntry.setIndexNames(*pppLinkConfigEntry.getIndexNames())

# Managed Objects groups

pdnPppLcpExtStateMachineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3, 2, 1, 1)
)
pdnPppLcpExtStateMachineGroup.setObjects(
    ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusCurrState")
)
if mibBuilder.loadTexts:
    pdnPppLcpExtStateMachineGroup.setStatus("current")

pdnPppLcpExtEstablishFailedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3, 2, 1, 2)
)
pdnPppLcpExtEstablishFailedGroup.setObjects(
    ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusEstablishFailedReason")
)
if mibBuilder.loadTexts:
    pdnPppLcpExtEstablishFailedGroup.setStatus("current")

pdnPppLcpExtMagicNumberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3, 2, 1, 3)
)
pdnPppLcpExtMagicNumberGroup.setObjects(
      *(("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusLocalToRemoteMagicNumber"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusRemoteToLocalMagicNumber"))
)
if mibBuilder.loadTexts:
    pdnPppLcpExtMagicNumberGroup.setStatus("current")

pdnPppLcpExtPacketCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3, 2, 1, 4)
)
pdnPppLcpExtPacketCountersGroup.setObjects(
      *(("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalSentConfigRequests"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalReceivedConfigRequests"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalSentConfigAcks"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalReceivedConfigAcks"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalSentConfigNaks"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalReceivedConfigNaks"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalSentConfigRejects"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalReceivedConfigRejects"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalSentTerminateRequests"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalReceivedTerminateRequests"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalSentTerminateAcks"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalReceivedTerminateAcks"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalSentCodeRejects"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalReceivedCodeRejects"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalSentProtocolRejects"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalReceivedProtocolRejects"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalSentEchoRequests"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalReceivedEchoRequests"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalSentEchoReplies"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalReceivedEchoReplies"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalSentDiscardRequests"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalReceivedDiscardRequests"))
)
if mibBuilder.loadTexts:
    pdnPppLcpExtPacketCountersGroup.setStatus("current")

pdnPppLcpExtKeepAliveCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3, 2, 1, 5)
)
pdnPppLcpExtKeepAliveCountersGroup.setObjects(
      *(("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalSentKeepAlives"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalReceivedKeepAlives"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalKeepAlivesLost"))
)
if mibBuilder.loadTexts:
    pdnPppLcpExtKeepAliveCountersGroup.setStatus("current")

pdnPppLcpExtPFCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3, 2, 1, 6)
)
pdnPppLcpExtPFCGroup.setObjects(
    ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkConfigPFC")
)
if mibBuilder.loadTexts:
    pdnPppLcpExtPFCGroup.setStatus("current")

pdnPppLcpExtACFCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3, 2, 1, 7)
)
pdnPppLcpExtACFCGroup.setObjects(
    ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkConfigACFC")
)
if mibBuilder.loadTexts:
    pdnPppLcpExtACFCGroup.setStatus("current")

pdnPppLcpExtKeepAliveConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3, 2, 1, 8)
)
pdnPppLcpExtKeepAliveConfGroup.setObjects(
      *(("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkConfigKeepAliveQuietTime"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkConfigKeepAliveTimeout"))
)
if mibBuilder.loadTexts:
    pdnPppLcpExtKeepAliveConfGroup.setStatus("current")

pdnPppLcpExtEchoTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3, 2, 1, 9)
)
pdnPppLcpExtEchoTestGroup.setObjects(
      *(("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkTestSendEchoTest"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkTestEchoTestTimeout"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkTestLastEchoTestResults"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalEchoRequestsTimeOuts"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalEchoRequestsBadData"),
        ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalEchoRequestsPassed"))
)
if mibBuilder.loadTexts:
    pdnPppLcpExtEchoTestGroup.setStatus("current")

pdnPpppLcpExtDiscardTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3, 2, 1, 10)
)
pdnPpppLcpExtDiscardTestGroup.setObjects(
    ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkTestSendDiscardTest")
)
if mibBuilder.loadTexts:
    pdnPpppLcpExtDiscardTestGroup.setStatus("current")

pdnPpppLcpExtLinkStateCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3, 2, 1, 11)
)
pdnPpppLcpExtLinkStateCounterGroup.setObjects(
    ("PDN-PPP-LCP-EXT-MIB", "pdnPppLinkStatusTotalTerminates")
)
if mibBuilder.loadTexts:
    pdnPpppLcpExtLinkStateCounterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnPppLcpExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 28, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pdnPppLcpExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-PPP-LCP-EXT-MIB",
    **{"pdnPppLcpExtMIB": pdnPppLcpExtMIB,
       "pdnPppLcpExtNotifications": pdnPppLcpExtNotifications,
       "pdnPppLcpExtObjects": pdnPppLcpExtObjects,
       "pdnPppLinkStatusExtTable": pdnPppLinkStatusExtTable,
       "pdnPppLinkStatusExtEntry": pdnPppLinkStatusExtEntry,
       "pdnPppLinkStatusCurrState": pdnPppLinkStatusCurrState,
       "pdnPppLinkStatusEstablishFailedReason": pdnPppLinkStatusEstablishFailedReason,
       "pdnPppLinkStatusLocalToRemoteMagicNumber": pdnPppLinkStatusLocalToRemoteMagicNumber,
       "pdnPppLinkStatusRemoteToLocalMagicNumber": pdnPppLinkStatusRemoteToLocalMagicNumber,
       "pdnPppLinkStatusTotalSentConfigRequests": pdnPppLinkStatusTotalSentConfigRequests,
       "pdnPppLinkStatusTotalReceivedConfigRequests": pdnPppLinkStatusTotalReceivedConfigRequests,
       "pdnPppLinkStatusTotalSentConfigAcks": pdnPppLinkStatusTotalSentConfigAcks,
       "pdnPppLinkStatusTotalReceivedConfigAcks": pdnPppLinkStatusTotalReceivedConfigAcks,
       "pdnPppLinkStatusTotalSentConfigNaks": pdnPppLinkStatusTotalSentConfigNaks,
       "pdnPppLinkStatusTotalReceivedConfigNaks": pdnPppLinkStatusTotalReceivedConfigNaks,
       "pdnPppLinkStatusTotalSentConfigRejects": pdnPppLinkStatusTotalSentConfigRejects,
       "pdnPppLinkStatusTotalReceivedConfigRejects": pdnPppLinkStatusTotalReceivedConfigRejects,
       "pdnPppLinkStatusTotalSentTerminateRequests": pdnPppLinkStatusTotalSentTerminateRequests,
       "pdnPppLinkStatusTotalReceivedTerminateRequests": pdnPppLinkStatusTotalReceivedTerminateRequests,
       "pdnPppLinkStatusTotalSentTerminateAcks": pdnPppLinkStatusTotalSentTerminateAcks,
       "pdnPppLinkStatusTotalReceivedTerminateAcks": pdnPppLinkStatusTotalReceivedTerminateAcks,
       "pdnPppLinkStatusTotalSentCodeRejects": pdnPppLinkStatusTotalSentCodeRejects,
       "pdnPppLinkStatusTotalReceivedCodeRejects": pdnPppLinkStatusTotalReceivedCodeRejects,
       "pdnPppLinkStatusTotalSentProtocolRejects": pdnPppLinkStatusTotalSentProtocolRejects,
       "pdnPppLinkStatusTotalReceivedProtocolRejects": pdnPppLinkStatusTotalReceivedProtocolRejects,
       "pdnPppLinkStatusTotalSentEchoRequests": pdnPppLinkStatusTotalSentEchoRequests,
       "pdnPppLinkStatusTotalReceivedEchoRequests": pdnPppLinkStatusTotalReceivedEchoRequests,
       "pdnPppLinkStatusTotalSentEchoReplies": pdnPppLinkStatusTotalSentEchoReplies,
       "pdnPppLinkStatusTotalReceivedEchoReplies": pdnPppLinkStatusTotalReceivedEchoReplies,
       "pdnPppLinkStatusTotalSentDiscardRequests": pdnPppLinkStatusTotalSentDiscardRequests,
       "pdnPppLinkStatusTotalReceivedDiscardRequests": pdnPppLinkStatusTotalReceivedDiscardRequests,
       "pdnPppLinkStatusTotalSentKeepAlives": pdnPppLinkStatusTotalSentKeepAlives,
       "pdnPppLinkStatusTotalReceivedKeepAlives": pdnPppLinkStatusTotalReceivedKeepAlives,
       "pdnPppLinkStatusTotalEchoRequestsTimeOuts": pdnPppLinkStatusTotalEchoRequestsTimeOuts,
       "pdnPppLinkStatusTotalEchoRequestsBadData": pdnPppLinkStatusTotalEchoRequestsBadData,
       "pdnPppLinkStatusTotalEchoRequestsPassed": pdnPppLinkStatusTotalEchoRequestsPassed,
       "pdnPppLinkStatusTotalKeepAlivesLost": pdnPppLinkStatusTotalKeepAlivesLost,
       "pdnPppLinkStatusTotalTerminates": pdnPppLinkStatusTotalTerminates,
       "pdnPppLinkConfigExtTable": pdnPppLinkConfigExtTable,
       "pdnPppLinkConfigExtEntry": pdnPppLinkConfigExtEntry,
       "pdnPppLinkConfigPFC": pdnPppLinkConfigPFC,
       "pdnPppLinkConfigACFC": pdnPppLinkConfigACFC,
       "pdnPppLinkConfigKeepAliveQuietTime": pdnPppLinkConfigKeepAliveQuietTime,
       "pdnPppLinkConfigKeepAliveTimeout": pdnPppLinkConfigKeepAliveTimeout,
       "pdnPppLinkTestTable": pdnPppLinkTestTable,
       "pdnPppLinkTestEntry": pdnPppLinkTestEntry,
       "pdnPppLinkTestSendEchoTest": pdnPppLinkTestSendEchoTest,
       "pdnPppLinkTestEchoTestTimeout": pdnPppLinkTestEchoTestTimeout,
       "pdnPppLinkTestSendDiscardTest": pdnPppLinkTestSendDiscardTest,
       "pdnPppLinkTestLastEchoTestResults": pdnPppLinkTestLastEchoTestResults,
       "pdnPppLcpExtAFNs": pdnPppLcpExtAFNs,
       "pdnPppLcpExtConformance": pdnPppLcpExtConformance,
       "pdnPppLcpExtCompliances": pdnPppLcpExtCompliances,
       "pdnPppLcpExtCompliance": pdnPppLcpExtCompliance,
       "pdnPppLcpExtGroups": pdnPppLcpExtGroups,
       "pdnPppLcpExtObjGroups": pdnPppLcpExtObjGroups,
       "pdnPppLcpExtStateMachineGroup": pdnPppLcpExtStateMachineGroup,
       "pdnPppLcpExtEstablishFailedGroup": pdnPppLcpExtEstablishFailedGroup,
       "pdnPppLcpExtMagicNumberGroup": pdnPppLcpExtMagicNumberGroup,
       "pdnPppLcpExtPacketCountersGroup": pdnPppLcpExtPacketCountersGroup,
       "pdnPppLcpExtKeepAliveCountersGroup": pdnPppLcpExtKeepAliveCountersGroup,
       "pdnPppLcpExtPFCGroup": pdnPppLcpExtPFCGroup,
       "pdnPppLcpExtACFCGroup": pdnPppLcpExtACFCGroup,
       "pdnPppLcpExtKeepAliveConfGroup": pdnPppLcpExtKeepAliveConfGroup,
       "pdnPppLcpExtEchoTestGroup": pdnPppLcpExtEchoTestGroup,
       "pdnPpppLcpExtDiscardTestGroup": pdnPpppLcpExtDiscardTestGroup,
       "pdnPpppLcpExtLinkStateCounterGroup": pdnPpppLcpExtLinkStateCounterGroup,
       "pdnPppLcpExtAfnGroups": pdnPppLcpExtAfnGroups,
       "pdnPppLcpExtNtfyGroups": pdnPppLcpExtNtfyGroups}
)
