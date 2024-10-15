# SNMP MIB module (ACSServer-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACSServer-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:39 2024
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

(microsoft,
 software) = mibBuilder.importSymbols(
    "MSFT-MIB",
    "microsoft",
    "software")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcsService_ObjectIdentity = ObjectIdentity
acsService = _AcsService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 15)
)
_AcsSvcStats_ObjectIdentity = ObjectIdentity
acsSvcStats = _AcsSvcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 1)
)
_AcsSvcStatsIfNumber_Type = Integer32
_AcsSvcStatsIfNumber_Object = MibScalar
acsSvcStatsIfNumber = _AcsSvcStatsIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 1, 1),
    _AcsSvcStatsIfNumber_Type()
)
acsSvcStatsIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSvcStatsIfNumber.setStatus("mandatory")
_AcsSvcStatsActiveApiSessions_Type = Integer32
_AcsSvcStatsActiveApiSessions_Object = MibScalar
acsSvcStatsActiveApiSessions = _AcsSvcStatsActiveApiSessions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 1, 2),
    _AcsSvcStatsActiveApiSessions_Type()
)
acsSvcStatsActiveApiSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSvcStatsActiveApiSessions.setStatus("mandatory")
_AcsSvcStatsActiveApiSockets_Type = Integer32
_AcsSvcStatsActiveApiSockets_Object = MibScalar
acsSvcStatsActiveApiSockets = _AcsSvcStatsActiveApiSockets_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 1, 3),
    _AcsSvcStatsActiveApiSockets_Type()
)
acsSvcStatsActiveApiSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSvcStatsActiveApiSockets.setStatus("mandatory")
_AcsSvcStatsReceivedApiPathRequests_Type = Counter32
_AcsSvcStatsReceivedApiPathRequests_Object = MibScalar
acsSvcStatsReceivedApiPathRequests = _AcsSvcStatsReceivedApiPathRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 1, 4),
    _AcsSvcStatsReceivedApiPathRequests_Type()
)
acsSvcStatsReceivedApiPathRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSvcStatsReceivedApiPathRequests.setStatus("mandatory")
_AcsSvcStatsReceivedApiResvRequests_Type = Counter32
_AcsSvcStatsReceivedApiResvRequests_Object = MibScalar
acsSvcStatsReceivedApiResvRequests = _AcsSvcStatsReceivedApiResvRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 1, 5),
    _AcsSvcStatsReceivedApiResvRequests_Type()
)
acsSvcStatsReceivedApiResvRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSvcStatsReceivedApiResvRequests.setStatus("mandatory")
_AcsSvcStatsFailedApiRequests_Type = Counter32
_AcsSvcStatsFailedApiRequests_Object = MibScalar
acsSvcStatsFailedApiRequests = _AcsSvcStatsFailedApiRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 1, 6),
    _AcsSvcStatsFailedApiRequests_Type()
)
acsSvcStatsFailedApiRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSvcStatsFailedApiRequests.setStatus("mandatory")
_AcsSvcStatsFailedApiSends_Type = Counter32
_AcsSvcStatsFailedApiSends_Object = MibScalar
acsSvcStatsFailedApiSends = _AcsSvcStatsFailedApiSends_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 1, 7),
    _AcsSvcStatsFailedApiSends_Type()
)
acsSvcStatsFailedApiSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSvcStatsFailedApiSends.setStatus("mandatory")
_AcsSvcStatsApiNotifications_Type = Counter32
_AcsSvcStatsApiNotifications_Object = MibScalar
acsSvcStatsApiNotifications = _AcsSvcStatsApiNotifications_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 1, 8),
    _AcsSvcStatsApiNotifications_Type()
)
acsSvcStatsApiNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSvcStatsApiNotifications.setStatus("mandatory")
_AcsSvcStatsApiNotificationBytes_Type = Counter32
_AcsSvcStatsApiNotificationBytes_Object = MibScalar
acsSvcStatsApiNotificationBytes = _AcsSvcStatsApiNotificationBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 1, 9),
    _AcsSvcStatsApiNotificationBytes_Type()
)
acsSvcStatsApiNotificationBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSvcStatsApiNotificationBytes.setStatus("mandatory")
_AcsSvcStatsNetSockets_Type = Integer32
_AcsSvcStatsNetSockets_Object = MibScalar
acsSvcStatsNetSockets = _AcsSvcStatsNetSockets_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 1, 10),
    _AcsSvcStatsNetSockets_Type()
)
acsSvcStatsNetSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSvcStatsNetSockets.setStatus("mandatory")
_AcsSvcStatsTimers_Type = Integer32
_AcsSvcStatsTimers_Object = MibScalar
acsSvcStatsTimers = _AcsSvcStatsTimers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 1, 11),
    _AcsSvcStatsTimers_Type()
)
acsSvcStatsTimers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSvcStatsTimers.setStatus("mandatory")
_AcsInterfaces_ObjectIdentity = ObjectIdentity
acsInterfaces = _AcsInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2)
)
_AcsIfStatsTable_Object = MibTable
acsIfStatsTable = _AcsIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1)
)
if mibBuilder.loadTexts:
    acsIfStatsTable.setStatus("mandatory")
_AcsIfStatsEntry_Object = MibTableRow
acsIfStatsEntry = _AcsIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1)
)
acsIfStatsEntry.setIndexNames(
    (0, "ACSServer-MIB", "acsIfStatsIndex"),
)
if mibBuilder.loadTexts:
    acsIfStatsEntry.setStatus("mandatory")
_AcsIfStatsIndex_Type = Integer32
_AcsIfStatsIndex_Object = MibTableColumn
acsIfStatsIndex = _AcsIfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 1),
    _AcsIfStatsIndex_Type()
)
acsIfStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsIndex.setStatus("mandatory")
_AcsIfStatsIpAddr_Type = IpAddress
_AcsIfStatsIpAddr_Object = MibTableColumn
acsIfStatsIpAddr = _AcsIfStatsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 2),
    _AcsIfStatsIpAddr_Type()
)
acsIfStatsIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsIpAddr.setStatus("mandatory")
_AcsIfStatsRawIpSentBytes_Type = Counter32
_AcsIfStatsRawIpSentBytes_Object = MibTableColumn
acsIfStatsRawIpSentBytes = _AcsIfStatsRawIpSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 3),
    _AcsIfStatsRawIpSentBytes_Type()
)
acsIfStatsRawIpSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsRawIpSentBytes.setStatus("mandatory")
_AcsIfStatsRawIpReceivedBytes_Type = Counter32
_AcsIfStatsRawIpReceivedBytes_Object = MibTableColumn
acsIfStatsRawIpReceivedBytes = _AcsIfStatsRawIpReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 4),
    _AcsIfStatsRawIpReceivedBytes_Type()
)
acsIfStatsRawIpReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsRawIpReceivedBytes.setStatus("mandatory")
_AcsIfStatsReceivedRsvpPathMsgs_Type = Counter32
_AcsIfStatsReceivedRsvpPathMsgs_Object = MibTableColumn
acsIfStatsReceivedRsvpPathMsgs = _AcsIfStatsReceivedRsvpPathMsgs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 5),
    _AcsIfStatsReceivedRsvpPathMsgs_Type()
)
acsIfStatsReceivedRsvpPathMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsReceivedRsvpPathMsgs.setStatus("mandatory")
_AcsIfStatsReceivedRsvpResvMsgs_Type = Counter32
_AcsIfStatsReceivedRsvpResvMsgs_Object = MibTableColumn
acsIfStatsReceivedRsvpResvMsgs = _AcsIfStatsReceivedRsvpResvMsgs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 6),
    _AcsIfStatsReceivedRsvpResvMsgs_Type()
)
acsIfStatsReceivedRsvpResvMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsReceivedRsvpResvMsgs.setStatus("mandatory")
_AcsIfStatsReceivedRsvpPathErrMsgs_Type = Counter32
_AcsIfStatsReceivedRsvpPathErrMsgs_Object = MibTableColumn
acsIfStatsReceivedRsvpPathErrMsgs = _AcsIfStatsReceivedRsvpPathErrMsgs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 7),
    _AcsIfStatsReceivedRsvpPathErrMsgs_Type()
)
acsIfStatsReceivedRsvpPathErrMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsReceivedRsvpPathErrMsgs.setStatus("mandatory")
_AcsIfStatsReceivedRsvpResvErrMsgs_Type = Counter32
_AcsIfStatsReceivedRsvpResvErrMsgs_Object = MibTableColumn
acsIfStatsReceivedRsvpResvErrMsgs = _AcsIfStatsReceivedRsvpResvErrMsgs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 8),
    _AcsIfStatsReceivedRsvpResvErrMsgs_Type()
)
acsIfStatsReceivedRsvpResvErrMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsReceivedRsvpResvErrMsgs.setStatus("mandatory")
_AcsIfStatsReceivedRsvpPathTearMsgs_Type = Counter32
_AcsIfStatsReceivedRsvpPathTearMsgs_Object = MibTableColumn
acsIfStatsReceivedRsvpPathTearMsgs = _AcsIfStatsReceivedRsvpPathTearMsgs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 9),
    _AcsIfStatsReceivedRsvpPathTearMsgs_Type()
)
acsIfStatsReceivedRsvpPathTearMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsReceivedRsvpPathTearMsgs.setStatus("mandatory")
_AcsIfStatsReceivedRsvpResvTearMsgs_Type = Counter32
_AcsIfStatsReceivedRsvpResvTearMsgs_Object = MibTableColumn
acsIfStatsReceivedRsvpResvTearMsgs = _AcsIfStatsReceivedRsvpResvTearMsgs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 10),
    _AcsIfStatsReceivedRsvpResvTearMsgs_Type()
)
acsIfStatsReceivedRsvpResvTearMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsReceivedRsvpResvTearMsgs.setStatus("mandatory")
_AcsIfStatsReceivedRsvpConfirmMsgs_Type = Counter32
_AcsIfStatsReceivedRsvpConfirmMsgs_Object = MibTableColumn
acsIfStatsReceivedRsvpConfirmMsgs = _AcsIfStatsReceivedRsvpConfirmMsgs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 11),
    _AcsIfStatsReceivedRsvpConfirmMsgs_Type()
)
acsIfStatsReceivedRsvpConfirmMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsReceivedRsvpConfirmMsgs.setStatus("mandatory")
_AcsIfStatsSentRsvpPathMsgs_Type = Counter32
_AcsIfStatsSentRsvpPathMsgs_Object = MibTableColumn
acsIfStatsSentRsvpPathMsgs = _AcsIfStatsSentRsvpPathMsgs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 12),
    _AcsIfStatsSentRsvpPathMsgs_Type()
)
acsIfStatsSentRsvpPathMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsSentRsvpPathMsgs.setStatus("mandatory")
_AcsIfStatsSentRsvpResvMsgs_Type = Counter32
_AcsIfStatsSentRsvpResvMsgs_Object = MibTableColumn
acsIfStatsSentRsvpResvMsgs = _AcsIfStatsSentRsvpResvMsgs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 13),
    _AcsIfStatsSentRsvpResvMsgs_Type()
)
acsIfStatsSentRsvpResvMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsSentRsvpResvMsgs.setStatus("mandatory")
_AcsIfStatsSentRsvpPathErrMsgs_Type = Counter32
_AcsIfStatsSentRsvpPathErrMsgs_Object = MibTableColumn
acsIfStatsSentRsvpPathErrMsgs = _AcsIfStatsSentRsvpPathErrMsgs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 14),
    _AcsIfStatsSentRsvpPathErrMsgs_Type()
)
acsIfStatsSentRsvpPathErrMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsSentRsvpPathErrMsgs.setStatus("mandatory")
_AcsIfStatsSentRsvpResvErrMsgs_Type = Counter32
_AcsIfStatsSentRsvpResvErrMsgs_Object = MibTableColumn
acsIfStatsSentRsvpResvErrMsgs = _AcsIfStatsSentRsvpResvErrMsgs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 15),
    _AcsIfStatsSentRsvpResvErrMsgs_Type()
)
acsIfStatsSentRsvpResvErrMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsSentRsvpResvErrMsgs.setStatus("mandatory")
_AcsIfStatsSentRsvpPathTearMsgs_Type = Counter32
_AcsIfStatsSentRsvpPathTearMsgs_Object = MibTableColumn
acsIfStatsSentRsvpPathTearMsgs = _AcsIfStatsSentRsvpPathTearMsgs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 16),
    _AcsIfStatsSentRsvpPathTearMsgs_Type()
)
acsIfStatsSentRsvpPathTearMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsSentRsvpPathTearMsgs.setStatus("mandatory")
_AcsIfStatsSentRsvpResvTearMsgs_Type = Counter32
_AcsIfStatsSentRsvpResvTearMsgs_Object = MibTableColumn
acsIfStatsSentRsvpResvTearMsgs = _AcsIfStatsSentRsvpResvTearMsgs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 17),
    _AcsIfStatsSentRsvpResvTearMsgs_Type()
)
acsIfStatsSentRsvpResvTearMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsSentRsvpResvTearMsgs.setStatus("mandatory")
_AcsIfStatsSentRsvpConfirmMsgs_Type = Counter32
_AcsIfStatsSentRsvpConfirmMsgs_Object = MibTableColumn
acsIfStatsSentRsvpConfirmMsgs = _AcsIfStatsSentRsvpConfirmMsgs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 18),
    _AcsIfStatsSentRsvpConfirmMsgs_Type()
)
acsIfStatsSentRsvpConfirmMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsSentRsvpConfirmMsgs.setStatus("mandatory")
_AcsIfStatsAdmissionControlFailures_Type = Counter32
_AcsIfStatsAdmissionControlFailures_Object = MibTableColumn
acsIfStatsAdmissionControlFailures = _AcsIfStatsAdmissionControlFailures_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 19),
    _AcsIfStatsAdmissionControlFailures_Type()
)
acsIfStatsAdmissionControlFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsAdmissionControlFailures.setStatus("mandatory")
_AcsIfStatsPolicyControlFailures_Type = Counter32
_AcsIfStatsPolicyControlFailures_Object = MibTableColumn
acsIfStatsPolicyControlFailures = _AcsIfStatsPolicyControlFailures_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 20),
    _AcsIfStatsPolicyControlFailures_Type()
)
acsIfStatsPolicyControlFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsPolicyControlFailures.setStatus("mandatory")
_AcsIfStatsOtherFailures_Type = Counter32
_AcsIfStatsOtherFailures_Object = MibTableColumn
acsIfStatsOtherFailures = _AcsIfStatsOtherFailures_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 21),
    _AcsIfStatsOtherFailures_Type()
)
acsIfStatsOtherFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsOtherFailures.setStatus("mandatory")
_AcsIfStatsInBlockadeStateResvs_Type = Counter32
_AcsIfStatsInBlockadeStateResvs_Object = MibTableColumn
acsIfStatsInBlockadeStateResvs = _AcsIfStatsInBlockadeStateResvs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 22),
    _AcsIfStatsInBlockadeStateResvs_Type()
)
acsIfStatsInBlockadeStateResvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsInBlockadeStateResvs.setStatus("mandatory")
_AcsIfStatsResvTimeOuts_Type = Counter32
_AcsIfStatsResvTimeOuts_Object = MibTableColumn
acsIfStatsResvTimeOuts = _AcsIfStatsResvTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 23),
    _AcsIfStatsResvTimeOuts_Type()
)
acsIfStatsResvTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsResvTimeOuts.setStatus("mandatory")
_AcsIfStatsPathTimeOuts_Type = Counter32
_AcsIfStatsPathTimeOuts_Object = MibTableColumn
acsIfStatsPathTimeOuts = _AcsIfStatsPathTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 24),
    _AcsIfStatsPathTimeOuts_Type()
)
acsIfStatsPathTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsPathTimeOuts.setStatus("mandatory")
_AcsIfStatsReceiveFailsBigMsg_Type = Counter32
_AcsIfStatsReceiveFailsBigMsg_Object = MibTableColumn
acsIfStatsReceiveFailsBigMsg = _AcsIfStatsReceiveFailsBigMsg_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 25),
    _AcsIfStatsReceiveFailsBigMsg_Type()
)
acsIfStatsReceiveFailsBigMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsReceiveFailsBigMsg.setStatus("mandatory")
_AcsIfStatsSendFailsBigMsg_Type = Counter32
_AcsIfStatsSendFailsBigMsg_Object = MibTableColumn
acsIfStatsSendFailsBigMsg = _AcsIfStatsSendFailsBigMsg_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 26),
    _AcsIfStatsSendFailsBigMsg_Type()
)
acsIfStatsSendFailsBigMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsSendFailsBigMsg.setStatus("mandatory")
_AcsIfStatsReceiveFailsNoMemory_Type = Counter32
_AcsIfStatsReceiveFailsNoMemory_Object = MibTableColumn
acsIfStatsReceiveFailsNoMemory = _AcsIfStatsReceiveFailsNoMemory_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 27),
    _AcsIfStatsReceiveFailsNoMemory_Type()
)
acsIfStatsReceiveFailsNoMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsReceiveFailsNoMemory.setStatus("mandatory")
_AcsIfStatsSendFailsNoMemory_Type = Counter32
_AcsIfStatsSendFailsNoMemory_Object = MibTableColumn
acsIfStatsSendFailsNoMemory = _AcsIfStatsSendFailsNoMemory_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 28),
    _AcsIfStatsSendFailsNoMemory_Type()
)
acsIfStatsSendFailsNoMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsSendFailsNoMemory.setStatus("mandatory")
_AcsIfStatsActiveFlows_Type = Integer32
_AcsIfStatsActiveFlows_Object = MibTableColumn
acsIfStatsActiveFlows = _AcsIfStatsActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 29),
    _AcsIfStatsActiveFlows_Type()
)
acsIfStatsActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsActiveFlows.setStatus("mandatory")
_AcsIfStatsAllocatedBandwidthBits_Type = Integer32
_AcsIfStatsAllocatedBandwidthBits_Object = MibTableColumn
acsIfStatsAllocatedBandwidthBits = _AcsIfStatsAllocatedBandwidthBits_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 30),
    _AcsIfStatsAllocatedBandwidthBits_Type()
)
acsIfStatsAllocatedBandwidthBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsAllocatedBandwidthBits.setStatus("mandatory")
_AcsIfStatsMaxAllocatedBandwidthBits_Type = Integer32
_AcsIfStatsMaxAllocatedBandwidthBits_Object = MibTableColumn
acsIfStatsMaxAllocatedBandwidthBits = _AcsIfStatsMaxAllocatedBandwidthBits_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 2, 1, 1, 31),
    _AcsIfStatsMaxAllocatedBandwidthBits_Type()
)
acsIfStatsMaxAllocatedBandwidthBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsIfStatsMaxAllocatedBandwidthBits.setStatus("mandatory")
_AcsMsidlpmStats_ObjectIdentity = ObjectIdentity
acsMsidlpmStats = _AcsMsidlpmStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3)
)
_AcsMsidlpmStatsTable_Object = MibTable
acsMsidlpmStatsTable = _AcsMsidlpmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1)
)
if mibBuilder.loadTexts:
    acsMsidlpmStatsTable.setStatus("mandatory")
_AcsMsidlpmStatsEntry_Object = MibTableRow
acsMsidlpmStatsEntry = _AcsMsidlpmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1)
)
acsMsidlpmStatsEntry.setIndexNames(
    (0, "ACSServer-MIB", "acsMsidlpmStatsIndex"),
)
if mibBuilder.loadTexts:
    acsMsidlpmStatsEntry.setStatus("mandatory")
_AcsMsidlpmStatsIndex_Type = Integer32
_AcsMsidlpmStatsIndex_Object = MibTableColumn
acsMsidlpmStatsIndex = _AcsMsidlpmStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 1),
    _AcsMsidlpmStatsIndex_Type()
)
acsMsidlpmStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmStatsIndex.setStatus("mandatory")
_AcsMsidlpmStatsSubnetAddr_Type = IpAddress
_AcsMsidlpmStatsSubnetAddr_Object = MibTableColumn
acsMsidlpmStatsSubnetAddr = _AcsMsidlpmStatsSubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 2),
    _AcsMsidlpmStatsSubnetAddr_Type()
)
acsMsidlpmStatsSubnetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmStatsSubnetAddr.setStatus("mandatory")
_AcsMsidlpmSendersAccepted_Type = Counter32
_AcsMsidlpmSendersAccepted_Object = MibTableColumn
acsMsidlpmSendersAccepted = _AcsMsidlpmSendersAccepted_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 3),
    _AcsMsidlpmSendersAccepted_Type()
)
acsMsidlpmSendersAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmSendersAccepted.setStatus("mandatory")
_AcsMsidlpmSenderChgAccepted_Type = Counter32
_AcsMsidlpmSenderChgAccepted_Object = MibTableColumn
acsMsidlpmSenderChgAccepted = _AcsMsidlpmSenderChgAccepted_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 4),
    _AcsMsidlpmSenderChgAccepted_Type()
)
acsMsidlpmSenderChgAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmSenderChgAccepted.setStatus("mandatory")
_AcsMsidlpmRejSndFlowRate_Type = Counter32
_AcsMsidlpmRejSndFlowRate_Object = MibTableColumn
acsMsidlpmRejSndFlowRate = _AcsMsidlpmRejSndFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 5),
    _AcsMsidlpmRejSndFlowRate_Type()
)
acsMsidlpmRejSndFlowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmRejSndFlowRate.setStatus("mandatory")
_AcsMsidlpmRejSndPeakRate_Type = Counter32
_AcsMsidlpmRejSndPeakRate_Object = MibTableColumn
acsMsidlpmRejSndPeakRate = _AcsMsidlpmRejSndPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 6),
    _AcsMsidlpmRejSndPeakRate_Type()
)
acsMsidlpmRejSndPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmRejSndPeakRate.setStatus("mandatory")
_AcsMsidlpmRejSndSumFlowRate_Type = Counter32
_AcsMsidlpmRejSndSumFlowRate_Object = MibTableColumn
acsMsidlpmRejSndSumFlowRate = _AcsMsidlpmRejSndSumFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 7),
    _AcsMsidlpmRejSndSumFlowRate_Type()
)
acsMsidlpmRejSndSumFlowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmRejSndSumFlowRate.setStatus("mandatory")
_AcsMsidlpmRejSndSumPeakRate_Type = Counter32
_AcsMsidlpmRejSndSumPeakRate_Object = MibTableColumn
acsMsidlpmRejSndSumPeakRate = _AcsMsidlpmRejSndSumPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 8),
    _AcsMsidlpmRejSndSumPeakRate_Type()
)
acsMsidlpmRejSndSumPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmRejSndSumPeakRate.setStatus("mandatory")
_AcsMsidlpmRejSndIdChange_Type = Counter32
_AcsMsidlpmRejSndIdChange_Object = MibTableColumn
acsMsidlpmRejSndIdChange = _AcsMsidlpmRejSndIdChange_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 9),
    _AcsMsidlpmRejSndIdChange_Type()
)
acsMsidlpmRejSndIdChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmRejSndIdChange.setStatus("mandatory")
_AcsMsidlpmRejSndDuration_Type = Counter32
_AcsMsidlpmRejSndDuration_Object = MibTableColumn
acsMsidlpmRejSndDuration = _AcsMsidlpmRejSndDuration_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 10),
    _AcsMsidlpmRejSndDuration_Type()
)
acsMsidlpmRejSndDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmRejSndDuration.setStatus("mandatory")
_AcsMsidlpmRejSndCount_Type = Counter32
_AcsMsidlpmRejSndCount_Object = MibTableColumn
acsMsidlpmRejSndCount = _AcsMsidlpmRejSndCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 11),
    _AcsMsidlpmRejSndCount_Type()
)
acsMsidlpmRejSndCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmRejSndCount.setStatus("mandatory")
_AcsMsidlpmRejSndOthersPolicies_Type = Counter32
_AcsMsidlpmRejSndOthersPolicies_Object = MibTableColumn
acsMsidlpmRejSndOthersPolicies = _AcsMsidlpmRejSndOthersPolicies_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 12),
    _AcsMsidlpmRejSndOthersPolicies_Type()
)
acsMsidlpmRejSndOthersPolicies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmRejSndOthersPolicies.setStatus("mandatory")
_AcsMsidlpmReceiversAccepted_Type = Counter32
_AcsMsidlpmReceiversAccepted_Object = MibTableColumn
acsMsidlpmReceiversAccepted = _AcsMsidlpmReceiversAccepted_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 13),
    _AcsMsidlpmReceiversAccepted_Type()
)
acsMsidlpmReceiversAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmReceiversAccepted.setStatus("mandatory")
_AcsMsidlpmReceiverChgAccepted_Type = Counter32
_AcsMsidlpmReceiverChgAccepted_Object = MibTableColumn
acsMsidlpmReceiverChgAccepted = _AcsMsidlpmReceiverChgAccepted_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 14),
    _AcsMsidlpmReceiverChgAccepted_Type()
)
acsMsidlpmReceiverChgAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmReceiverChgAccepted.setStatus("mandatory")
_AcsMsidlpmRejRecvFlowRate_Type = Counter32
_AcsMsidlpmRejRecvFlowRate_Object = MibTableColumn
acsMsidlpmRejRecvFlowRate = _AcsMsidlpmRejRecvFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 15),
    _AcsMsidlpmRejRecvFlowRate_Type()
)
acsMsidlpmRejRecvFlowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmRejRecvFlowRate.setStatus("mandatory")
_AcsMsidlpmRejRecvPeakRate_Type = Counter32
_AcsMsidlpmRejRecvPeakRate_Object = MibTableColumn
acsMsidlpmRejRecvPeakRate = _AcsMsidlpmRejRecvPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 16),
    _AcsMsidlpmRejRecvPeakRate_Type()
)
acsMsidlpmRejRecvPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmRejRecvPeakRate.setStatus("mandatory")
_AcsMsidlpmRejRecvSumFlowRate_Type = Counter32
_AcsMsidlpmRejRecvSumFlowRate_Object = MibTableColumn
acsMsidlpmRejRecvSumFlowRate = _AcsMsidlpmRejRecvSumFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 17),
    _AcsMsidlpmRejRecvSumFlowRate_Type()
)
acsMsidlpmRejRecvSumFlowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmRejRecvSumFlowRate.setStatus("mandatory")
_AcsMsidlpmRejRecvSumPeakRate_Type = Counter32
_AcsMsidlpmRejRecvSumPeakRate_Object = MibTableColumn
acsMsidlpmRejRecvSumPeakRate = _AcsMsidlpmRejRecvSumPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 18),
    _AcsMsidlpmRejRecvSumPeakRate_Type()
)
acsMsidlpmRejRecvSumPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmRejRecvSumPeakRate.setStatus("mandatory")
_AcsMsidlpmRejRecvIdChange_Type = Counter32
_AcsMsidlpmRejRecvIdChange_Object = MibTableColumn
acsMsidlpmRejRecvIdChange = _AcsMsidlpmRejRecvIdChange_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 19),
    _AcsMsidlpmRejRecvIdChange_Type()
)
acsMsidlpmRejRecvIdChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmRejRecvIdChange.setStatus("mandatory")
_AcsMsidlpmRejRecvDuration_Type = Counter32
_AcsMsidlpmRejRecvDuration_Object = MibTableColumn
acsMsidlpmRejRecvDuration = _AcsMsidlpmRejRecvDuration_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 20),
    _AcsMsidlpmRejRecvDuration_Type()
)
acsMsidlpmRejRecvDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmRejRecvDuration.setStatus("mandatory")
_AcsMsidlpmRejRecvCount_Type = Counter32
_AcsMsidlpmRejRecvCount_Object = MibTableColumn
acsMsidlpmRejRecvCount = _AcsMsidlpmRejRecvCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 21),
    _AcsMsidlpmRejRecvCount_Type()
)
acsMsidlpmRejRecvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmRejRecvCount.setStatus("mandatory")
_AcsMsidlpmRejRecvOthersPolicies_Type = Counter32
_AcsMsidlpmRejRecvOthersPolicies_Object = MibTableColumn
acsMsidlpmRejRecvOthersPolicies = _AcsMsidlpmRejRecvOthersPolicies_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 22),
    _AcsMsidlpmRejRecvOthersPolicies_Type()
)
acsMsidlpmRejRecvOthersPolicies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmRejRecvOthersPolicies.setStatus("mandatory")
_AcsMsidlpmBadIdentityPes_Type = Counter32
_AcsMsidlpmBadIdentityPes_Object = MibTableColumn
acsMsidlpmBadIdentityPes = _AcsMsidlpmBadIdentityPes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 23),
    _AcsMsidlpmBadIdentityPes_Type()
)
acsMsidlpmBadIdentityPes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmBadIdentityPes.setStatus("mandatory")
_AcsMsidlpmDsCacheSize_Type = Integer32
_AcsMsidlpmDsCacheSize_Object = MibTableColumn
acsMsidlpmDsCacheSize = _AcsMsidlpmDsCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 15, 3, 1, 1, 24),
    _AcsMsidlpmDsCacheSize_Type()
)
acsMsidlpmDsCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsMsidlpmDsCacheSize.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACSServer-MIB",
    **{"acsService": acsService,
       "acsSvcStats": acsSvcStats,
       "acsSvcStatsIfNumber": acsSvcStatsIfNumber,
       "acsSvcStatsActiveApiSessions": acsSvcStatsActiveApiSessions,
       "acsSvcStatsActiveApiSockets": acsSvcStatsActiveApiSockets,
       "acsSvcStatsReceivedApiPathRequests": acsSvcStatsReceivedApiPathRequests,
       "acsSvcStatsReceivedApiResvRequests": acsSvcStatsReceivedApiResvRequests,
       "acsSvcStatsFailedApiRequests": acsSvcStatsFailedApiRequests,
       "acsSvcStatsFailedApiSends": acsSvcStatsFailedApiSends,
       "acsSvcStatsApiNotifications": acsSvcStatsApiNotifications,
       "acsSvcStatsApiNotificationBytes": acsSvcStatsApiNotificationBytes,
       "acsSvcStatsNetSockets": acsSvcStatsNetSockets,
       "acsSvcStatsTimers": acsSvcStatsTimers,
       "acsInterfaces": acsInterfaces,
       "acsIfStatsTable": acsIfStatsTable,
       "acsIfStatsEntry": acsIfStatsEntry,
       "acsIfStatsIndex": acsIfStatsIndex,
       "acsIfStatsIpAddr": acsIfStatsIpAddr,
       "acsIfStatsRawIpSentBytes": acsIfStatsRawIpSentBytes,
       "acsIfStatsRawIpReceivedBytes": acsIfStatsRawIpReceivedBytes,
       "acsIfStatsReceivedRsvpPathMsgs": acsIfStatsReceivedRsvpPathMsgs,
       "acsIfStatsReceivedRsvpResvMsgs": acsIfStatsReceivedRsvpResvMsgs,
       "acsIfStatsReceivedRsvpPathErrMsgs": acsIfStatsReceivedRsvpPathErrMsgs,
       "acsIfStatsReceivedRsvpResvErrMsgs": acsIfStatsReceivedRsvpResvErrMsgs,
       "acsIfStatsReceivedRsvpPathTearMsgs": acsIfStatsReceivedRsvpPathTearMsgs,
       "acsIfStatsReceivedRsvpResvTearMsgs": acsIfStatsReceivedRsvpResvTearMsgs,
       "acsIfStatsReceivedRsvpConfirmMsgs": acsIfStatsReceivedRsvpConfirmMsgs,
       "acsIfStatsSentRsvpPathMsgs": acsIfStatsSentRsvpPathMsgs,
       "acsIfStatsSentRsvpResvMsgs": acsIfStatsSentRsvpResvMsgs,
       "acsIfStatsSentRsvpPathErrMsgs": acsIfStatsSentRsvpPathErrMsgs,
       "acsIfStatsSentRsvpResvErrMsgs": acsIfStatsSentRsvpResvErrMsgs,
       "acsIfStatsSentRsvpPathTearMsgs": acsIfStatsSentRsvpPathTearMsgs,
       "acsIfStatsSentRsvpResvTearMsgs": acsIfStatsSentRsvpResvTearMsgs,
       "acsIfStatsSentRsvpConfirmMsgs": acsIfStatsSentRsvpConfirmMsgs,
       "acsIfStatsAdmissionControlFailures": acsIfStatsAdmissionControlFailures,
       "acsIfStatsPolicyControlFailures": acsIfStatsPolicyControlFailures,
       "acsIfStatsOtherFailures": acsIfStatsOtherFailures,
       "acsIfStatsInBlockadeStateResvs": acsIfStatsInBlockadeStateResvs,
       "acsIfStatsResvTimeOuts": acsIfStatsResvTimeOuts,
       "acsIfStatsPathTimeOuts": acsIfStatsPathTimeOuts,
       "acsIfStatsReceiveFailsBigMsg": acsIfStatsReceiveFailsBigMsg,
       "acsIfStatsSendFailsBigMsg": acsIfStatsSendFailsBigMsg,
       "acsIfStatsReceiveFailsNoMemory": acsIfStatsReceiveFailsNoMemory,
       "acsIfStatsSendFailsNoMemory": acsIfStatsSendFailsNoMemory,
       "acsIfStatsActiveFlows": acsIfStatsActiveFlows,
       "acsIfStatsAllocatedBandwidthBits": acsIfStatsAllocatedBandwidthBits,
       "acsIfStatsMaxAllocatedBandwidthBits": acsIfStatsMaxAllocatedBandwidthBits,
       "acsMsidlpmStats": acsMsidlpmStats,
       "acsMsidlpmStatsTable": acsMsidlpmStatsTable,
       "acsMsidlpmStatsEntry": acsMsidlpmStatsEntry,
       "acsMsidlpmStatsIndex": acsMsidlpmStatsIndex,
       "acsMsidlpmStatsSubnetAddr": acsMsidlpmStatsSubnetAddr,
       "acsMsidlpmSendersAccepted": acsMsidlpmSendersAccepted,
       "acsMsidlpmSenderChgAccepted": acsMsidlpmSenderChgAccepted,
       "acsMsidlpmRejSndFlowRate": acsMsidlpmRejSndFlowRate,
       "acsMsidlpmRejSndPeakRate": acsMsidlpmRejSndPeakRate,
       "acsMsidlpmRejSndSumFlowRate": acsMsidlpmRejSndSumFlowRate,
       "acsMsidlpmRejSndSumPeakRate": acsMsidlpmRejSndSumPeakRate,
       "acsMsidlpmRejSndIdChange": acsMsidlpmRejSndIdChange,
       "acsMsidlpmRejSndDuration": acsMsidlpmRejSndDuration,
       "acsMsidlpmRejSndCount": acsMsidlpmRejSndCount,
       "acsMsidlpmRejSndOthersPolicies": acsMsidlpmRejSndOthersPolicies,
       "acsMsidlpmReceiversAccepted": acsMsidlpmReceiversAccepted,
       "acsMsidlpmReceiverChgAccepted": acsMsidlpmReceiverChgAccepted,
       "acsMsidlpmRejRecvFlowRate": acsMsidlpmRejRecvFlowRate,
       "acsMsidlpmRejRecvPeakRate": acsMsidlpmRejRecvPeakRate,
       "acsMsidlpmRejRecvSumFlowRate": acsMsidlpmRejRecvSumFlowRate,
       "acsMsidlpmRejRecvSumPeakRate": acsMsidlpmRejRecvSumPeakRate,
       "acsMsidlpmRejRecvIdChange": acsMsidlpmRejRecvIdChange,
       "acsMsidlpmRejRecvDuration": acsMsidlpmRejRecvDuration,
       "acsMsidlpmRejRecvCount": acsMsidlpmRejRecvCount,
       "acsMsidlpmRejRecvOthersPolicies": acsMsidlpmRejRecvOthersPolicies,
       "acsMsidlpmBadIdentityPes": acsMsidlpmBadIdentityPes,
       "acsMsidlpmDsCacheSize": acsMsidlpmDsCacheSize}
)
