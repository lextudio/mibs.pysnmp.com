# SNMP MIB module (BW-BroadworksMediaServer) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BW-BroadworksMediaServer
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:03 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

broadsoft = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6431)
)
broadsoft.setRevisions(
        ("2005-08-15 14:30",
         "2000-09-19 14:31")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Broadworks_ObjectIdentity = ObjectIdentity
broadworks = _Broadworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1)
)
_MediaServer_ObjectIdentity = ObjectIdentity
mediaServer = _MediaServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3)
)
_Mcp_ObjectIdentity = ObjectIdentity
mcp = _Mcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1)
)
_Conferencing_ObjectIdentity = ObjectIdentity
conferencing = _Conferencing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 3)
)
_MsConfAddParticipantFailed_Type = Counter64
_MsConfAddParticipantFailed_Object = MibScalar
msConfAddParticipantFailed = _MsConfAddParticipantFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 3, 1),
    _MsConfAddParticipantFailed_Type()
)
msConfAddParticipantFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msConfAddParticipantFailed.setStatus("obsolete")
_MsConfAddParticipant_Type = Counter64
_MsConfAddParticipant_Object = MibScalar
msConfAddParticipant = _MsConfAddParticipant_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 3, 2),
    _MsConfAddParticipant_Type()
)
msConfAddParticipant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msConfAddParticipant.setStatus("obsolete")
_MsConfAllocateBridge_Type = Counter64
_MsConfAllocateBridge_Object = MibScalar
msConfAllocateBridge = _MsConfAllocateBridge_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 3, 3),
    _MsConfAllocateBridge_Type()
)
msConfAllocateBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msConfAllocateBridge.setStatus("obsolete")
_MsConfAllocateBridgeFailed_Type = Counter64
_MsConfAllocateBridgeFailed_Object = MibScalar
msConfAllocateBridgeFailed = _MsConfAllocateBridgeFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 3, 4),
    _MsConfAllocateBridgeFailed_Type()
)
msConfAllocateBridgeFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msConfAllocateBridgeFailed.setStatus("obsolete")
_MsConfRemoveParticipant_Type = Counter64
_MsConfRemoveParticipant_Object = MibScalar
msConfRemoveParticipant = _MsConfRemoveParticipant_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 3, 5),
    _MsConfRemoveParticipant_Type()
)
msConfRemoveParticipant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msConfRemoveParticipant.setStatus("obsolete")
_MsConfRemoveParticipantFailed_Type = Counter64
_MsConfRemoveParticipantFailed_Object = MibScalar
msConfRemoveParticipantFailed = _MsConfRemoveParticipantFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 3, 6),
    _MsConfRemoveParticipantFailed_Type()
)
msConfRemoveParticipantFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msConfRemoveParticipantFailed.setStatus("obsolete")
_MsConfCurrentPortsInUse_Type = Gauge32
_MsConfCurrentPortsInUse_Object = MibScalar
msConfCurrentPortsInUse = _MsConfCurrentPortsInUse_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 3, 7),
    _MsConfCurrentPortsInUse_Type()
)
msConfCurrentPortsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msConfCurrentPortsInUse.setStatus("obsolete")
_MsConferenceCount_Type = Counter64
_MsConferenceCount_Object = MibScalar
msConferenceCount = _MsConferenceCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 3, 8),
    _MsConferenceCount_Type()
)
msConferenceCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msConferenceCount.setStatus("current")
_MsConfTotalDuration_Type = Counter64
_MsConfTotalDuration_Object = MibScalar
msConfTotalDuration = _MsConfTotalDuration_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 3, 9),
    _MsConfTotalDuration_Type()
)
msConfTotalDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msConfTotalDuration.setStatus("current")
_MsConfUpdateParticipant_Type = Counter64
_MsConfUpdateParticipant_Object = MibScalar
msConfUpdateParticipant = _MsConfUpdateParticipant_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 3, 11),
    _MsConfUpdateParticipant_Type()
)
msConfUpdateParticipant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msConfUpdateParticipant.setStatus("obsolete")
_MsConfUpdateParticipantFailed_Type = Counter64
_MsConfUpdateParticipantFailed_Object = MibScalar
msConfUpdateParticipantFailed = _MsConfUpdateParticipantFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 3, 12),
    _MsConfUpdateParticipantFailed_Type()
)
msConfUpdateParticipantFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msConfUpdateParticipantFailed.setStatus("obsolete")
_Ivr_ObjectIdentity = ObjectIdentity
ivr = _Ivr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4)
)
_MsIvrFreeAudioMemory_Type = Gauge32
_MsIvrFreeAudioMemory_Object = MibScalar
msIvrFreeAudioMemory = _MsIvrFreeAudioMemory_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 1),
    _MsIvrFreeAudioMemory_Type()
)
msIvrFreeAudioMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msIvrFreeAudioMemory.setStatus("current")
_MsIvrAudioMemoryInUse_Type = Gauge32
_MsIvrAudioMemoryInUse_Object = MibScalar
msIvrAudioMemoryInUse = _MsIvrAudioMemoryInUse_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 2),
    _MsIvrAudioMemoryInUse_Type()
)
msIvrAudioMemoryInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msIvrAudioMemoryInUse.setStatus("current")
_MsIvrCurrentPortsInUse_Type = Gauge32
_MsIvrCurrentPortsInUse_Object = MibScalar
msIvrCurrentPortsInUse = _MsIvrCurrentPortsInUse_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 3),
    _MsIvrCurrentPortsInUse_Type()
)
msIvrCurrentPortsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msIvrCurrentPortsInUse.setStatus("obsolete")
_MsIvrCreateConnection_Type = Counter64
_MsIvrCreateConnection_Object = MibScalar
msIvrCreateConnection = _MsIvrCreateConnection_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 4),
    _MsIvrCreateConnection_Type()
)
msIvrCreateConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrCreateConnection.setStatus("obsolete")
_MsIvrCreateConnectionFailed_Type = Counter64
_MsIvrCreateConnectionFailed_Object = MibScalar
msIvrCreateConnectionFailed = _MsIvrCreateConnectionFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 5),
    _MsIvrCreateConnectionFailed_Type()
)
msIvrCreateConnectionFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrCreateConnectionFailed.setStatus("obsolete")
_MsIvrUpdateConnection_Type = Counter64
_MsIvrUpdateConnection_Object = MibScalar
msIvrUpdateConnection = _MsIvrUpdateConnection_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 6),
    _MsIvrUpdateConnection_Type()
)
msIvrUpdateConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrUpdateConnection.setStatus("obsolete")
_MsIvrUpdateConnectionFailed_Type = Counter64
_MsIvrUpdateConnectionFailed_Object = MibScalar
msIvrUpdateConnectionFailed = _MsIvrUpdateConnectionFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 7),
    _MsIvrUpdateConnectionFailed_Type()
)
msIvrUpdateConnectionFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrUpdateConnectionFailed.setStatus("obsolete")
_MsIvrPlay_Type = Counter64
_MsIvrPlay_Object = MibScalar
msIvrPlay = _MsIvrPlay_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 8),
    _MsIvrPlay_Type()
)
msIvrPlay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrPlay.setStatus("obsolete")
_MsIvrPlayFailed_Type = Counter64
_MsIvrPlayFailed_Object = MibScalar
msIvrPlayFailed = _MsIvrPlayFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 9),
    _MsIvrPlayFailed_Type()
)
msIvrPlayFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrPlayFailed.setStatus("obsolete")
_MsIvrPlayCollect_Type = Counter64
_MsIvrPlayCollect_Object = MibScalar
msIvrPlayCollect = _MsIvrPlayCollect_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 10),
    _MsIvrPlayCollect_Type()
)
msIvrPlayCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrPlayCollect.setStatus("obsolete")
_MsIvrPlayCollectFailed_Type = Counter64
_MsIvrPlayCollectFailed_Object = MibScalar
msIvrPlayCollectFailed = _MsIvrPlayCollectFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 11),
    _MsIvrPlayCollectFailed_Type()
)
msIvrPlayCollectFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrPlayCollectFailed.setStatus("obsolete")
_MsIvrPlayRecord_Type = Counter64
_MsIvrPlayRecord_Object = MibScalar
msIvrPlayRecord = _MsIvrPlayRecord_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 12),
    _MsIvrPlayRecord_Type()
)
msIvrPlayRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrPlayRecord.setStatus("obsolete")
_MsIvrPlayRecordFailed_Type = Counter64
_MsIvrPlayRecordFailed_Object = MibScalar
msIvrPlayRecordFailed = _MsIvrPlayRecordFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 13),
    _MsIvrPlayRecordFailed_Type()
)
msIvrPlayRecordFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrPlayRecordFailed.setStatus("obsolete")
_MsIvrSendEmail_Type = Counter64
_MsIvrSendEmail_Object = MibScalar
msIvrSendEmail = _MsIvrSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 14),
    _MsIvrSendEmail_Type()
)
msIvrSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrSendEmail.setStatus("obsolete")
_MsIvrSendEmailFailed_Type = Counter64
_MsIvrSendEmailFailed_Object = MibScalar
msIvrSendEmailFailed = _MsIvrSendEmailFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 15),
    _MsIvrSendEmailFailed_Type()
)
msIvrSendEmailFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrSendEmailFailed.setStatus("obsolete")
_MsIvrSessionCount_Type = Counter64
_MsIvrSessionCount_Object = MibScalar
msIvrSessionCount = _MsIvrSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 16),
    _MsIvrSessionCount_Type()
)
msIvrSessionCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrSessionCount.setStatus("current")
_MsIvrTotalDuration_Type = Counter64
_MsIvrTotalDuration_Object = MibScalar
msIvrTotalDuration = _MsIvrTotalDuration_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 17),
    _MsIvrTotalDuration_Type()
)
msIvrTotalDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrTotalDuration.setStatus("current")
_MsIvrTotalRecordingDuration_Type = Counter64
_MsIvrTotalRecordingDuration_Object = MibScalar
msIvrTotalRecordingDuration = _MsIvrTotalRecordingDuration_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 18),
    _MsIvrTotalRecordingDuration_Type()
)
msIvrTotalRecordingDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrTotalRecordingDuration.setStatus("obsolete")
_MsIvrMerge_Type = Counter64
_MsIvrMerge_Object = MibScalar
msIvrMerge = _MsIvrMerge_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 21),
    _MsIvrMerge_Type()
)
msIvrMerge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrMerge.setStatus("obsolete")
_MsIvrMergeFailed_Type = Counter64
_MsIvrMergeFailed_Object = MibScalar
msIvrMergeFailed = _MsIvrMergeFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 22),
    _MsIvrMergeFailed_Type()
)
msIvrMergeFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrMergeFailed.setStatus("obsolete")
_MsIvrEmptyRecordings_Type = Counter64
_MsIvrEmptyRecordings_Object = MibScalar
msIvrEmptyRecordings = _MsIvrEmptyRecordings_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 4, 23),
    _MsIvrEmptyRecordings_Type()
)
msIvrEmptyRecordings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msIvrEmptyRecordings.setStatus("obsolete")


class _MsPortsInUse_Type(Gauge32):
    """Custom type msPortsInUse based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MsPortsInUse_Type.__name__ = "Gauge32"
_MsPortsInUse_Object = MibScalar
msPortsInUse = _MsPortsInUse_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 5),
    _MsPortsInUse_Type()
)
msPortsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msPortsInUse.setStatus("current")
_MsNoPortAvailableErrors_Type = Counter64
_MsNoPortAvailableErrors_Object = MibScalar
msNoPortAvailableErrors = _MsNoPortAvailableErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 6),
    _MsNoPortAvailableErrors_Type()
)
msNoPortAvailableErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msNoPortAvailableErrors.setStatus("current")
_MsMCPNotificationsTransmitted_Type = Counter64
_MsMCPNotificationsTransmitted_Object = MibScalar
msMCPNotificationsTransmitted = _MsMCPNotificationsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 7),
    _MsMCPNotificationsTransmitted_Type()
)
msMCPNotificationsTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMCPNotificationsTransmitted.setStatus("obsolete")
_MsMCPNotificationsRetransmitted_Type = Counter64
_MsMCPNotificationsRetransmitted_Object = MibScalar
msMCPNotificationsRetransmitted = _MsMCPNotificationsRetransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 8),
    _MsMCPNotificationsRetransmitted_Type()
)
msMCPNotificationsRetransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMCPNotificationsRetransmitted.setStatus("obsolete")
_MsMCPCommandsReceived_Type = Counter64
_MsMCPCommandsReceived_Object = MibScalar
msMCPCommandsReceived = _MsMCPCommandsReceived_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 1, 9),
    _MsMCPCommandsReceived_Type()
)
msMCPCommandsReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMCPCommandsReceived.setStatus("obsolete")
_Rtp_ObjectIdentity = ObjectIdentity
rtp = _Rtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 2)
)
_MsRtpSessionsCount_Type = Counter64
_MsRtpSessionsCount_Object = MibScalar
msRtpSessionsCount = _MsRtpSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 2, 1),
    _MsRtpSessionsCount_Type()
)
msRtpSessionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msRtpSessionsCount.setStatus("current")
_Receive_ObjectIdentity = ObjectIdentity
receive = _Receive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 2, 2)
)
_MsRtcpSenderReports_Type = Counter64
_MsRtcpSenderReports_Object = MibScalar
msRtcpSenderReports = _MsRtcpSenderReports_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 2, 2, 1),
    _MsRtcpSenderReports_Type()
)
msRtcpSenderReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msRtcpSenderReports.setStatus("current")
_MsRtpPacketsExpected_Type = Counter64
_MsRtpPacketsExpected_Object = MibScalar
msRtpPacketsExpected = _MsRtpPacketsExpected_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 2, 2, 2),
    _MsRtpPacketsExpected_Type()
)
msRtpPacketsExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msRtpPacketsExpected.setStatus("current")
_MsRtpPacketsReceived_Type = Counter64
_MsRtpPacketsReceived_Object = MibScalar
msRtpPacketsReceived = _MsRtpPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 2, 2, 3),
    _MsRtpPacketsReceived_Type()
)
msRtpPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msRtpPacketsReceived.setStatus("current")
_MsRtpOutOfOrder_Type = Counter64
_MsRtpOutOfOrder_Object = MibScalar
msRtpOutOfOrder = _MsRtpOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 2, 2, 5),
    _MsRtpOutOfOrder_Type()
)
msRtpOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msRtpOutOfOrder.setStatus("current")
_MsRtpBadPayload_Type = Counter64
_MsRtpBadPayload_Object = MibScalar
msRtpBadPayload = _MsRtpBadPayload_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 2, 2, 6),
    _MsRtpBadPayload_Type()
)
msRtpBadPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msRtpBadPayload.setStatus("current")
_MsRtpSsrc_Type = Counter64
_MsRtpSsrc_Object = MibScalar
msRtpSsrc = _MsRtpSsrc_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 2, 2, 7),
    _MsRtpSsrc_Type()
)
msRtpSsrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msRtpSsrc.setStatus("current")
_MsRtpReceivedPacketJitter_Type = Counter64
_MsRtpReceivedPacketJitter_Object = MibScalar
msRtpReceivedPacketJitter = _MsRtpReceivedPacketJitter_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 2, 2, 8),
    _MsRtpReceivedPacketJitter_Type()
)
msRtpReceivedPacketJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msRtpReceivedPacketJitter.setStatus("current")
_Transmit_ObjectIdentity = ObjectIdentity
transmit = _Transmit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 2, 3)
)
_MsRtpCumulativePacketsLost_Type = Counter64
_MsRtpCumulativePacketsLost_Object = MibScalar
msRtpCumulativePacketsLost = _MsRtpCumulativePacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 2, 3, 1),
    _MsRtpCumulativePacketsLost_Type()
)
msRtpCumulativePacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msRtpCumulativePacketsLost.setStatus("current")
_MsRtpPacketsSent_Type = Counter64
_MsRtpPacketsSent_Object = MibScalar
msRtpPacketsSent = _MsRtpPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 2, 3, 4),
    _MsRtpPacketsSent_Type()
)
msRtpPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msRtpPacketsSent.setStatus("current")
_MsRtpFramesSkipped_Type = Counter64
_MsRtpFramesSkipped_Object = MibScalar
msRtpFramesSkipped = _MsRtpFramesSkipped_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 2, 3, 5),
    _MsRtpFramesSkipped_Type()
)
msRtpFramesSkipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msRtpFramesSkipped.setStatus("current")
_MsRtpTransmitJitter_Type = Counter64
_MsRtpTransmitJitter_Object = MibScalar
msRtpTransmitJitter = _MsRtpTransmitJitter_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 2, 3, 6),
    _MsRtpTransmitJitter_Type()
)
msRtpTransmitJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msRtpTransmitJitter.setStatus("current")
_MsRtpSessionsInUse_Type = Gauge32
_MsRtpSessionsInUse_Object = MibScalar
msRtpSessionsInUse = _MsRtpSessionsInUse_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 2, 4),
    _MsRtpSessionsInUse_Type()
)
msRtpSessionsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msRtpSessionsInUse.setStatus("current")
_Smtp_ObjectIdentity = ObjectIdentity
smtp = _Smtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 3)
)
_Primary_ObjectIdentity = ObjectIdentity
primary = _Primary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 3, 1)
)
_MsPrimaryEmailSent_Type = Counter64
_MsPrimaryEmailSent_Object = MibScalar
msPrimaryEmailSent = _MsPrimaryEmailSent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 3, 1, 1),
    _MsPrimaryEmailSent_Type()
)
msPrimaryEmailSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msPrimaryEmailSent.setStatus("current")
_MsPrimarySmtpErrors_Type = Counter64
_MsPrimarySmtpErrors_Object = MibScalar
msPrimarySmtpErrors = _MsPrimarySmtpErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 3, 1, 2),
    _MsPrimarySmtpErrors_Type()
)
msPrimarySmtpErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msPrimarySmtpErrors.setStatus("current")
_Secondary_ObjectIdentity = ObjectIdentity
secondary = _Secondary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 3, 2)
)
_MsSecondaryEmailSent_Type = Counter64
_MsSecondaryEmailSent_Object = MibScalar
msSecondaryEmailSent = _MsSecondaryEmailSent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 3, 2, 1),
    _MsSecondaryEmailSent_Type()
)
msSecondaryEmailSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSecondaryEmailSent.setStatus("current")
_MsSecondarySmtpErrors_Type = Counter64
_MsSecondarySmtpErrors_Object = MibScalar
msSecondarySmtpErrors = _MsSecondarySmtpErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 3, 2, 2),
    _MsSecondarySmtpErrors_Type()
)
msSecondarySmtpErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSecondarySmtpErrors.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 4)
)
_MsAlarmsCount_Type = Counter64
_MsAlarmsCount_Object = MibScalar
msAlarmsCount = _MsAlarmsCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 4, 1),
    _MsAlarmsCount_Type()
)
msAlarmsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msAlarmsCount.setStatus("current")
_MsSoftwareErrorsCount_Type = Counter64
_MsSoftwareErrorsCount_Object = MibScalar
msSoftwareErrorsCount = _MsSoftwareErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 4, 2),
    _MsSoftwareErrorsCount_Type()
)
msSoftwareErrorsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSoftwareErrorsCount.setStatus("current")
_MsACLViolationCount_Type = Counter64
_MsACLViolationCount_Object = MibScalar
msACLViolationCount = _MsACLViolationCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 4, 3),
    _MsACLViolationCount_Type()
)
msACLViolationCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msACLViolationCount.setStatus("current")
_MsMaxCapacityInPorts_Type = Counter64
_MsMaxCapacityInPorts_Object = MibScalar
msMaxCapacityInPorts = _MsMaxCapacityInPorts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 4, 4),
    _MsMaxCapacityInPorts_Type()
)
msMaxCapacityInPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMaxCapacityInPorts.setStatus("current")
_MsNumLicensedPorts_Type = Counter64
_MsNumLicensedPorts_Object = MibScalar
msNumLicensedPorts = _MsNumLicensedPorts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 4, 5),
    _MsNumLicensedPorts_Type()
)
msNumLicensedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msNumLicensedPorts.setStatus("current")
_Http_ObjectIdentity = ObjectIdentity
http = _Http_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 5)
)
_MsFilesDownloaded_Type = Counter64
_MsFilesDownloaded_Object = MibScalar
msFilesDownloaded = _MsFilesDownloaded_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 5, 1),
    _MsFilesDownloaded_Type()
)
msFilesDownloaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msFilesDownloaded.setStatus("current")
_MsTotalSizeDownloadedFiles_Type = Counter64
_MsTotalSizeDownloadedFiles_Object = MibScalar
msTotalSizeDownloadedFiles = _MsTotalSizeDownloadedFiles_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 5, 2),
    _MsTotalSizeDownloadedFiles_Type()
)
msTotalSizeDownloadedFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msTotalSizeDownloadedFiles.setStatus("current")
_MsFilesRetrievedFromCache_Type = Counter64
_MsFilesRetrievedFromCache_Object = MibScalar
msFilesRetrievedFromCache = _MsFilesRetrievedFromCache_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 5, 3),
    _MsFilesRetrievedFromCache_Type()
)
msFilesRetrievedFromCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msFilesRetrievedFromCache.setStatus("current")
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 6)
)
_ResetAllMSCounters_Type = Counter32
_ResetAllMSCounters_Object = MibScalar
resetAllMSCounters = _ResetAllMSCounters_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 6, 1),
    _ResetAllMSCounters_Type()
)
resetAllMSCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetAllMSCounters.setStatus("current")
_Sip_ObjectIdentity = ObjectIdentity
sip = _Sip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 7)
)
_MsSipStatsInviteIns_Type = Counter64
_MsSipStatsInviteIns_Object = MibScalar
msSipStatsInviteIns = _MsSipStatsInviteIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 7, 1),
    _MsSipStatsInviteIns_Type()
)
msSipStatsInviteIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSipStatsInviteIns.setStatus("current")
_MsSipStatsAckIns_Type = Counter64
_MsSipStatsAckIns_Object = MibScalar
msSipStatsAckIns = _MsSipStatsAckIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 7, 2),
    _MsSipStatsAckIns_Type()
)
msSipStatsAckIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSipStatsAckIns.setStatus("current")
_MsSipStatsByeIns_Type = Counter64
_MsSipStatsByeIns_Object = MibScalar
msSipStatsByeIns = _MsSipStatsByeIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 7, 3),
    _MsSipStatsByeIns_Type()
)
msSipStatsByeIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSipStatsByeIns.setStatus("current")
_MsSipStatsByeOuts_Type = Counter64
_MsSipStatsByeOuts_Object = MibScalar
msSipStatsByeOuts = _MsSipStatsByeOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 7, 4),
    _MsSipStatsByeOuts_Type()
)
msSipStatsByeOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSipStatsByeOuts.setStatus("current")
_MsSipStatsInfoIns_Type = Counter64
_MsSipStatsInfoIns_Object = MibScalar
msSipStatsInfoIns = _MsSipStatsInfoIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 7, 5),
    _MsSipStatsInfoIns_Type()
)
msSipStatsInfoIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSipStatsInfoIns.setStatus("current")
_MsSipStatsInfoOuts_Type = Counter64
_MsSipStatsInfoOuts_Object = MibScalar
msSipStatsInfoOuts = _MsSipStatsInfoOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 7, 6),
    _MsSipStatsInfoOuts_Type()
)
msSipStatsInfoOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSipStatsInfoOuts.setStatus("current")
_MsSipStatsOthersIns_Type = Counter64
_MsSipStatsOthersIns_Object = MibScalar
msSipStatsOthersIns = _MsSipStatsOthersIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 7, 7),
    _MsSipStatsOthersIns_Type()
)
msSipStatsOthersIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSipStatsOthersIns.setStatus("current")
_MsSipStatsOthersOuts_Type = Counter64
_MsSipStatsOthersOuts_Object = MibScalar
msSipStatsOthersOuts = _MsSipStatsOthersOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 7, 8),
    _MsSipStatsOthersOuts_Type()
)
msSipStatsOthersOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSipStatsOthersOuts.setStatus("current")
_MsSipStatsResponsesIns_Type = Counter64
_MsSipStatsResponsesIns_Object = MibScalar
msSipStatsResponsesIns = _MsSipStatsResponsesIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 7, 9),
    _MsSipStatsResponsesIns_Type()
)
msSipStatsResponsesIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSipStatsResponsesIns.setStatus("current")
_MsSipStatsResponsesOuts_Type = Counter64
_MsSipStatsResponsesOuts_Object = MibScalar
msSipStatsResponsesOuts = _MsSipStatsResponsesOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 7, 10),
    _MsSipStatsResponsesOuts_Type()
)
msSipStatsResponsesOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSipStatsResponsesOuts.setStatus("current")
_MsSipStatsInvite200OKRetransmitsOuts_Type = Counter64
_MsSipStatsInvite200OKRetransmitsOuts_Object = MibScalar
msSipStatsInvite200OKRetransmitsOuts = _MsSipStatsInvite200OKRetransmitsOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 7, 11),
    _MsSipStatsInvite200OKRetransmitsOuts_Type()
)
msSipStatsInvite200OKRetransmitsOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSipStatsInvite200OKRetransmitsOuts.setStatus("current")
_MsSipStatsRequestRetransmittedIns_Type = Counter64
_MsSipStatsRequestRetransmittedIns_Object = MibScalar
msSipStatsRequestRetransmittedIns = _MsSipStatsRequestRetransmittedIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 7, 12),
    _MsSipStatsRequestRetransmittedIns_Type()
)
msSipStatsRequestRetransmittedIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSipStatsRequestRetransmittedIns.setStatus("current")
_MsSipStatsReferOuts_Type = Counter64
_MsSipStatsReferOuts_Object = MibScalar
msSipStatsReferOuts = _MsSipStatsReferOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 7, 13),
    _MsSipStatsReferOuts_Type()
)
msSipStatsReferOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSipStatsReferOuts.setStatus("current")
_MsRedirectsCount_Type = Counter64
_MsRedirectsCount_Object = MibScalar
msRedirectsCount = _MsRedirectsCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 7, 14),
    _MsRedirectsCount_Type()
)
msRedirectsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msRedirectsCount.setStatus("current")
_MsTimeOutRouteAdvancesCount_Type = Counter64
_MsTimeOutRouteAdvancesCount_Object = MibScalar
msTimeOutRouteAdvancesCount = _MsTimeOutRouteAdvancesCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 7, 15),
    _MsTimeOutRouteAdvancesCount_Type()
)
msTimeOutRouteAdvancesCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msTimeOutRouteAdvancesCount.setStatus("current")
_MsRouteAdvancesCount_Type = Counter64
_MsRouteAdvancesCount_Object = MibScalar
msRouteAdvancesCount = _MsRouteAdvancesCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 7, 16),
    _MsRouteAdvancesCount_Type()
)
msRouteAdvancesCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msRouteAdvancesCount.setStatus("current")
_Mscml_ObjectIdentity = ObjectIdentity
mscml = _Mscml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 8)
)
_MsMSCMLPlayCollect_Type = Counter64
_MsMSCMLPlayCollect_Object = MibScalar
msMSCMLPlayCollect = _MsMSCMLPlayCollect_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 8, 1),
    _MsMSCMLPlayCollect_Type()
)
msMSCMLPlayCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMSCMLPlayCollect.setStatus("current")
_MsMSCMLPlayCollectFailed_Type = Counter64
_MsMSCMLPlayCollectFailed_Object = MibScalar
msMSCMLPlayCollectFailed = _MsMSCMLPlayCollectFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 8, 2),
    _MsMSCMLPlayCollectFailed_Type()
)
msMSCMLPlayCollectFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMSCMLPlayCollectFailed.setStatus("current")
_MsMSCMLPlay_Type = Counter64
_MsMSCMLPlay_Object = MibScalar
msMSCMLPlay = _MsMSCMLPlay_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 8, 3),
    _MsMSCMLPlay_Type()
)
msMSCMLPlay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMSCMLPlay.setStatus("current")
_MsMSCMLPlayFailed_Type = Counter64
_MsMSCMLPlayFailed_Object = MibScalar
msMSCMLPlayFailed = _MsMSCMLPlayFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 8, 4),
    _MsMSCMLPlayFailed_Type()
)
msMSCMLPlayFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMSCMLPlayFailed.setStatus("current")
_MsMSCMLPlayRecord_Type = Counter64
_MsMSCMLPlayRecord_Object = MibScalar
msMSCMLPlayRecord = _MsMSCMLPlayRecord_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 8, 5),
    _MsMSCMLPlayRecord_Type()
)
msMSCMLPlayRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMSCMLPlayRecord.setStatus("current")
_MsMSCMLRecordFailed_Type = Counter64
_MsMSCMLRecordFailed_Object = MibScalar
msMSCMLRecordFailed = _MsMSCMLRecordFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 8, 6),
    _MsMSCMLRecordFailed_Type()
)
msMSCMLRecordFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMSCMLRecordFailed.setStatus("current")
_MsMSCMLSendMail_Type = Counter64
_MsMSCMLSendMail_Object = MibScalar
msMSCMLSendMail = _MsMSCMLSendMail_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 8, 7),
    _MsMSCMLSendMail_Type()
)
msMSCMLSendMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMSCMLSendMail.setStatus("current")
_MsMSCMLSendMailFailed_Type = Counter64
_MsMSCMLSendMailFailed_Object = MibScalar
msMSCMLSendMailFailed = _MsMSCMLSendMailFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 8, 8),
    _MsMSCMLSendMailFailed_Type()
)
msMSCMLSendMailFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMSCMLSendMailFailed.setStatus("current")
_MsMSCMLTotalRecordingDuration_Type = Counter64
_MsMSCMLTotalRecordingDuration_Object = MibScalar
msMSCMLTotalRecordingDuration = _MsMSCMLTotalRecordingDuration_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 8, 9),
    _MsMSCMLTotalRecordingDuration_Type()
)
msMSCMLTotalRecordingDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMSCMLTotalRecordingDuration.setStatus("current")
_MsMSCMLEmptyRecordings_Type = Counter64
_MsMSCMLEmptyRecordings_Object = MibScalar
msMSCMLEmptyRecordings = _MsMSCMLEmptyRecordings_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 8, 10),
    _MsMSCMLEmptyRecordings_Type()
)
msMSCMLEmptyRecordings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMSCMLEmptyRecordings.setStatus("current")
_Liveaudio_ObjectIdentity = ObjectIdentity
liveaudio = _Liveaudio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 9)
)
_MsLiveAudioRequestCount_Type = Counter64
_MsLiveAudioRequestCount_Object = MibScalar
msLiveAudioRequestCount = _MsLiveAudioRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 9, 1),
    _MsLiveAudioRequestCount_Type()
)
msLiveAudioRequestCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msLiveAudioRequestCount.setStatus("obsolete")
_MsLiveAudioFailureCount_Type = Counter64
_MsLiveAudioFailureCount_Object = MibScalar
msLiveAudioFailureCount = _MsLiveAudioFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 9, 2),
    _MsLiveAudioFailureCount_Type()
)
msLiveAudioFailureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msLiveAudioFailureCount.setStatus("obsolete")
_MsLiveAudioTotalDuration_Type = Counter64
_MsLiveAudioTotalDuration_Object = MibScalar
msLiveAudioTotalDuration = _MsLiveAudioTotalDuration_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 9, 3),
    _MsLiveAudioTotalDuration_Type()
)
msLiveAudioTotalDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msLiveAudioTotalDuration.setStatus("obsolete")
_MsLiveAudioULawUserCount_Type = Gauge32
_MsLiveAudioULawUserCount_Object = MibScalar
msLiveAudioULawUserCount = _MsLiveAudioULawUserCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 9, 4),
    _MsLiveAudioULawUserCount_Type()
)
msLiveAudioULawUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msLiveAudioULawUserCount.setStatus("obsolete")
_MsLiveAudioALawUserCount_Type = Gauge32
_MsLiveAudioALawUserCount_Object = MibScalar
msLiveAudioALawUserCount = _MsLiveAudioALawUserCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 9, 5),
    _MsLiveAudioALawUserCount_Type()
)
msLiveAudioALawUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msLiveAudioALawUserCount.setStatus("obsolete")
_MsLiveAudioG726UserCount_Type = Gauge32
_MsLiveAudioG726UserCount_Object = MibScalar
msLiveAudioG726UserCount = _MsLiveAudioG726UserCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 9, 6),
    _MsLiveAudioG726UserCount_Type()
)
msLiveAudioG726UserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msLiveAudioG726UserCount.setStatus("obsolete")
_MsLiveAudioG729UserCount_Type = Gauge32
_MsLiveAudioG729UserCount_Object = MibScalar
msLiveAudioG729UserCount = _MsLiveAudioG729UserCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 9, 7),
    _MsLiveAudioG729UserCount_Type()
)
msLiveAudioG729UserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msLiveAudioG729UserCount.setStatus("obsolete")
_Video_ObjectIdentity = ObjectIdentity
video = _Video_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 10)
)
_MsVideoRecorded_Type = Counter32
_MsVideoRecorded_Object = MibScalar
msVideoRecorded = _MsVideoRecorded_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 10, 6),
    _MsVideoRecorded_Type()
)
msVideoRecorded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msVideoRecorded.setStatus("current")
_MsVideoPlayback_Type = Counter32
_MsVideoPlayback_Object = MibScalar
msVideoPlayback = _MsVideoPlayback_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 10, 7),
    _MsVideoPlayback_Type()
)
msVideoPlayback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msVideoPlayback.setStatus("current")
_Fax_ObjectIdentity = ObjectIdentity
fax = _Fax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 11)
)
_MsFaxReceived_Type = Counter64
_MsFaxReceived_Object = MibScalar
msFaxReceived = _MsFaxReceived_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 11, 1),
    _MsFaxReceived_Type()
)
msFaxReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msFaxReceived.setStatus("current")
_MsFaxReceptionFailure_Type = Counter64
_MsFaxReceptionFailure_Object = MibScalar
msFaxReceptionFailure = _MsFaxReceptionFailure_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 11, 2),
    _MsFaxReceptionFailure_Type()
)
msFaxReceptionFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msFaxReceptionFailure.setStatus("current")
_MsFaxPrinted_Type = Counter64
_MsFaxPrinted_Object = MibScalar
msFaxPrinted = _MsFaxPrinted_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 11, 3),
    _MsFaxPrinted_Type()
)
msFaxPrinted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msFaxPrinted.setStatus("current")
_MsFaxPrintingFailure_Type = Counter64
_MsFaxPrintingFailure_Object = MibScalar
msFaxPrintingFailure = _MsFaxPrintingFailure_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 11, 4),
    _MsFaxPrintingFailure_Type()
)
msFaxPrintingFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msFaxPrintingFailure.setStatus("current")
_Vxml_ObjectIdentity = ObjectIdentity
vxml = _Vxml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 12)
)
_MsVoiceXMLErrorCount_Type = Counter64
_MsVoiceXMLErrorCount_Object = MibScalar
msVoiceXMLErrorCount = _MsVoiceXMLErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 12, 1),
    _MsVoiceXMLErrorCount_Type()
)
msVoiceXMLErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msVoiceXMLErrorCount.setStatus("current")
_MsVoiceXMLFilesDownloaded_Type = Counter64
_MsVoiceXMLFilesDownloaded_Object = MibScalar
msVoiceXMLFilesDownloaded = _MsVoiceXMLFilesDownloaded_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 12, 2),
    _MsVoiceXMLFilesDownloaded_Type()
)
msVoiceXMLFilesDownloaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msVoiceXMLFilesDownloaded.setStatus("current")
_Ccxml_ObjectIdentity = ObjectIdentity
ccxml = _Ccxml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 13)
)
_MsCallControlXMLSessionCount_Type = Counter64
_MsCallControlXMLSessionCount_Object = MibScalar
msCallControlXMLSessionCount = _MsCallControlXMLSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 13, 1),
    _MsCallControlXMLSessionCount_Type()
)
msCallControlXMLSessionCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msCallControlXMLSessionCount.setStatus("current")
_MsCallControlXMLCreateCallCount_Type = Counter64
_MsCallControlXMLCreateCallCount_Object = MibScalar
msCallControlXMLCreateCallCount = _MsCallControlXMLCreateCallCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 13, 2),
    _MsCallControlXMLCreateCallCount_Type()
)
msCallControlXMLCreateCallCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msCallControlXMLCreateCallCount.setStatus("current")
_MsCallControlXMLDialogCount_Type = Counter64
_MsCallControlXMLDialogCount_Object = MibScalar
msCallControlXMLDialogCount = _MsCallControlXMLDialogCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 13, 3),
    _MsCallControlXMLDialogCount_Type()
)
msCallControlXMLDialogCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msCallControlXMLDialogCount.setStatus("current")
_MsCallControlXMLConfCount_Type = Counter64
_MsCallControlXMLConfCount_Object = MibScalar
msCallControlXMLConfCount = _MsCallControlXMLConfCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 13, 4),
    _MsCallControlXMLConfCount_Type()
)
msCallControlXMLConfCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msCallControlXMLConfCount.setStatus("current")
_Interfaces_ObjectIdentity = ObjectIdentity
interfaces = _Interfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 14)
)
_Mrcp_ObjectIdentity = ObjectIdentity
mrcp = _Mrcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 14, 1)
)
_MsMrcpAsrSessionsCount_Type = Counter64
_MsMrcpAsrSessionsCount_Object = MibScalar
msMrcpAsrSessionsCount = _MsMrcpAsrSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 14, 1, 1),
    _MsMrcpAsrSessionsCount_Type()
)
msMrcpAsrSessionsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMrcpAsrSessionsCount.setStatus("current")
_MsMrcpAsrSessionsInUse_Type = Gauge32
_MsMrcpAsrSessionsInUse_Object = MibScalar
msMrcpAsrSessionsInUse = _MsMrcpAsrSessionsInUse_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 14, 1, 2),
    _MsMrcpAsrSessionsInUse_Type()
)
msMrcpAsrSessionsInUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMrcpAsrSessionsInUse.setStatus("current")
_MsMrcpTtsSessionsCount_Type = Counter64
_MsMrcpTtsSessionsCount_Object = MibScalar
msMrcpTtsSessionsCount = _MsMrcpTtsSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 14, 1, 3),
    _MsMrcpTtsSessionsCount_Type()
)
msMrcpTtsSessionsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMrcpTtsSessionsCount.setStatus("current")
_MsMrcpTtsSessionsInUse_Type = Gauge32
_MsMrcpTtsSessionsInUse_Object = MibScalar
msMrcpTtsSessionsInUse = _MsMrcpTtsSessionsInUse_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 14, 1, 4),
    _MsMrcpTtsSessionsInUse_Type()
)
msMrcpTtsSessionsInUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMrcpTtsSessionsInUse.setStatus("current")
_MsMrcpRecognitionAttemptsCount_Type = Counter64
_MsMrcpRecognitionAttemptsCount_Object = MibScalar
msMrcpRecognitionAttemptsCount = _MsMrcpRecognitionAttemptsCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 14, 1, 8),
    _MsMrcpRecognitionAttemptsCount_Type()
)
msMrcpRecognitionAttemptsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMrcpRecognitionAttemptsCount.setStatus("current")
_MsMrcpSuccessfulRecognitionsCount_Type = Counter64
_MsMrcpSuccessfulRecognitionsCount_Object = MibScalar
msMrcpSuccessfulRecognitionsCount = _MsMrcpSuccessfulRecognitionsCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 14, 1, 9),
    _MsMrcpSuccessfulRecognitionsCount_Type()
)
msMrcpSuccessfulRecognitionsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMrcpSuccessfulRecognitionsCount.setStatus("current")
_MsMrcpRequestsCount_Type = Counter64
_MsMrcpRequestsCount_Object = MibScalar
msMrcpRequestsCount = _MsMrcpRequestsCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 14, 1, 10),
    _MsMrcpRequestsCount_Type()
)
msMrcpRequestsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMrcpRequestsCount.setStatus("current")
_MsMrcpFailedRequestsCount_Type = Counter64
_MsMrcpFailedRequestsCount_Object = MibScalar
msMrcpFailedRequestsCount = _MsMrcpFailedRequestsCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 14, 1, 11),
    _MsMrcpFailedRequestsCount_Type()
)
msMrcpFailedRequestsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMrcpFailedRequestsCount.setStatus("current")
_MsMrcpFailedConnectionsCount_Type = Counter64
_MsMrcpFailedConnectionsCount_Object = MibScalar
msMrcpFailedConnectionsCount = _MsMrcpFailedConnectionsCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 14, 1, 12),
    _MsMrcpFailedConnectionsCount_Type()
)
msMrcpFailedConnectionsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMrcpFailedConnectionsCount.setStatus("current")
_MsMrcpKeepAliveFailuresCount_Type = Counter64
_MsMrcpKeepAliveFailuresCount_Object = MibScalar
msMrcpKeepAliveFailuresCount = _MsMrcpKeepAliveFailuresCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 14, 1, 13),
    _MsMrcpKeepAliveFailuresCount_Type()
)
msMrcpKeepAliveFailuresCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMrcpKeepAliveFailuresCount.setStatus("current")
_MsMrcpSpeakRequestsCount_Type = Counter64
_MsMrcpSpeakRequestsCount_Object = MibScalar
msMrcpSpeakRequestsCount = _MsMrcpSpeakRequestsCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 14, 1, 14),
    _MsMrcpSpeakRequestsCount_Type()
)
msMrcpSpeakRequestsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMrcpSpeakRequestsCount.setStatus("current")
_MsMrcpSpeakRequestFailuresCount_Type = Counter64
_MsMrcpSpeakRequestFailuresCount_Object = MibScalar
msMrcpSpeakRequestFailuresCount = _MsMrcpSpeakRequestFailuresCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 14, 1, 15),
    _MsMrcpSpeakRequestFailuresCount_Type()
)
msMrcpSpeakRequestFailuresCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msMrcpSpeakRequestFailuresCount.setStatus("current")
_BwMsConformance_ObjectIdentity = ObjectIdentity
bwMsConformance = _BwMsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20)
)
_BwMSGroups_ObjectIdentity = ObjectIdentity
bwMSGroups = _BwMSGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 1)
)
_BwMSCompliancy_ObjectIdentity = ObjectIdentity
bwMSCompliancy = _BwMSCompliancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 2)
)

# Managed Objects groups

bwMSGroupMCP = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 1, 1)
)
bwMSGroupMCP.setObjects(
      *(("BW-BroadworksMediaServer", "msPortsInUse"),
        ("BW-BroadworksMediaServer", "msNoPortAvailableErrors"),
        ("BW-BroadworksMediaServer", "msMCPNotificationsTransmitted"),
        ("BW-BroadworksMediaServer", "msMCPNotificationsRetransmitted"),
        ("BW-BroadworksMediaServer", "msMCPCommandsReceived"))
)
if mibBuilder.loadTexts:
    bwMSGroupMCP.setStatus("current")

bwMSGroupMCPConferencing = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 1, 2)
)
bwMSGroupMCPConferencing.setObjects(
      *(("BW-BroadworksMediaServer", "msConfAddParticipantFailed"),
        ("BW-BroadworksMediaServer", "msConfAddParticipant"),
        ("BW-BroadworksMediaServer", "msConfAllocateBridge"),
        ("BW-BroadworksMediaServer", "msConfAllocateBridgeFailed"),
        ("BW-BroadworksMediaServer", "msConfRemoveParticipant"),
        ("BW-BroadworksMediaServer", "msConfRemoveParticipantFailed"),
        ("BW-BroadworksMediaServer", "msConfCurrentPortsInUse"),
        ("BW-BroadworksMediaServer", "msConferenceCount"),
        ("BW-BroadworksMediaServer", "msConfTotalDuration"),
        ("BW-BroadworksMediaServer", "msConfUpdateParticipant"),
        ("BW-BroadworksMediaServer", "msConfUpdateParticipantFailed"))
)
if mibBuilder.loadTexts:
    bwMSGroupMCPConferencing.setStatus("current")

bwMSGroupMCPIVR = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 1, 3)
)
bwMSGroupMCPIVR.setObjects(
      *(("BW-BroadworksMediaServer", "msIvrFreeAudioMemory"),
        ("BW-BroadworksMediaServer", "msIvrAudioMemoryInUse"),
        ("BW-BroadworksMediaServer", "msIvrCurrentPortsInUse"),
        ("BW-BroadworksMediaServer", "msIvrCreateConnection"),
        ("BW-BroadworksMediaServer", "msIvrCreateConnectionFailed"),
        ("BW-BroadworksMediaServer", "msIvrUpdateConnection"),
        ("BW-BroadworksMediaServer", "msIvrUpdateConnectionFailed"),
        ("BW-BroadworksMediaServer", "msIvrPlay"),
        ("BW-BroadworksMediaServer", "msIvrPlayFailed"),
        ("BW-BroadworksMediaServer", "msIvrPlayCollect"),
        ("BW-BroadworksMediaServer", "msIvrPlayCollectFailed"),
        ("BW-BroadworksMediaServer", "msIvrPlayRecord"),
        ("BW-BroadworksMediaServer", "msIvrPlayRecordFailed"),
        ("BW-BroadworksMediaServer", "msIvrSendEmail"),
        ("BW-BroadworksMediaServer", "msIvrSendEmailFailed"),
        ("BW-BroadworksMediaServer", "msIvrSessionCount"),
        ("BW-BroadworksMediaServer", "msIvrTotalDuration"),
        ("BW-BroadworksMediaServer", "msIvrTotalRecordingDuration"),
        ("BW-BroadworksMediaServer", "msIvrMerge"),
        ("BW-BroadworksMediaServer", "msIvrMergeFailed"),
        ("BW-BroadworksMediaServer", "msIvrEmptyRecordings"))
)
if mibBuilder.loadTexts:
    bwMSGroupMCPIVR.setStatus("current")

bwMSGroupRTP = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 1, 4)
)
bwMSGroupRTP.setObjects(
      *(("BW-BroadworksMediaServer", "msRtcpSenderReports"),
        ("BW-BroadworksMediaServer", "msRtpPacketsExpected"),
        ("BW-BroadworksMediaServer", "msRtpPacketsReceived"),
        ("BW-BroadworksMediaServer", "msRtpOutOfOrder"),
        ("BW-BroadworksMediaServer", "msRtpBadPayload"),
        ("BW-BroadworksMediaServer", "msRtpSsrc"),
        ("BW-BroadworksMediaServer", "msRtpReceivedPacketJitter"),
        ("BW-BroadworksMediaServer", "msRtpCumulativePacketsLost"),
        ("BW-BroadworksMediaServer", "msRtpPacketsSent"),
        ("BW-BroadworksMediaServer", "msRtpFramesSkipped"),
        ("BW-BroadworksMediaServer", "msRtpTransmitJitter"),
        ("BW-BroadworksMediaServer", "msRtpSessionsCount"),
        ("BW-BroadworksMediaServer", "msRtpSessionsInUse"))
)
if mibBuilder.loadTexts:
    bwMSGroupRTP.setStatus("current")

bwMSGroupSMTP = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 1, 5)
)
bwMSGroupSMTP.setObjects(
      *(("BW-BroadworksMediaServer", "msPrimaryEmailSent"),
        ("BW-BroadworksMediaServer", "msPrimarySmtpErrors"),
        ("BW-BroadworksMediaServer", "msSecondaryEmailSent"),
        ("BW-BroadworksMediaServer", "msSecondarySmtpErrors"))
)
if mibBuilder.loadTexts:
    bwMSGroupSMTP.setStatus("current")

bwMSGroupSystem = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 1, 6)
)
bwMSGroupSystem.setObjects(
      *(("BW-BroadworksMediaServer", "msAlarmsCount"),
        ("BW-BroadworksMediaServer", "msSoftwareErrorsCount"),
        ("BW-BroadworksMediaServer", "msACLViolationCount"),
        ("BW-BroadworksMediaServer", "msMaxCapacityInPorts"),
        ("BW-BroadworksMediaServer", "msNumLicensedPorts"))
)
if mibBuilder.loadTexts:
    bwMSGroupSystem.setStatus("current")

bwMSGroupHTTP = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 1, 7)
)
bwMSGroupHTTP.setObjects(
      *(("BW-BroadworksMediaServer", "msFilesDownloaded"),
        ("BW-BroadworksMediaServer", "msTotalSizeDownloadedFiles"),
        ("BW-BroadworksMediaServer", "msFilesRetrievedFromCache"))
)
if mibBuilder.loadTexts:
    bwMSGroupHTTP.setStatus("current")

bwMSGroupManagement = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 1, 8)
)
bwMSGroupManagement.setObjects(
    ("BW-BroadworksMediaServer", "resetAllMSCounters")
)
if mibBuilder.loadTexts:
    bwMSGroupManagement.setStatus("current")

bwMSGroupSIP = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 1, 9)
)
bwMSGroupSIP.setObjects(
      *(("BW-BroadworksMediaServer", "msSipStatsInviteIns"),
        ("BW-BroadworksMediaServer", "msSipStatsAckIns"),
        ("BW-BroadworksMediaServer", "msSipStatsByeIns"),
        ("BW-BroadworksMediaServer", "msSipStatsByeOuts"),
        ("BW-BroadworksMediaServer", "msSipStatsInfoIns"),
        ("BW-BroadworksMediaServer", "msSipStatsInfoOuts"),
        ("BW-BroadworksMediaServer", "msSipStatsOthersIns"),
        ("BW-BroadworksMediaServer", "msSipStatsOthersOuts"),
        ("BW-BroadworksMediaServer", "msSipStatsResponsesIns"),
        ("BW-BroadworksMediaServer", "msSipStatsResponsesOuts"),
        ("BW-BroadworksMediaServer", "msSipStatsInvite200OKRetransmitsOuts"),
        ("BW-BroadworksMediaServer", "msSipStatsRequestRetransmittedIns"),
        ("BW-BroadworksMediaServer", "msSipStatsReferOuts"),
        ("BW-BroadworksMediaServer", "msRedirectsCount"),
        ("BW-BroadworksMediaServer", "msTimeOutRouteAdvancesCount"),
        ("BW-BroadworksMediaServer", "msRouteAdvancesCount"))
)
if mibBuilder.loadTexts:
    bwMSGroupSIP.setStatus("current")

bwMSGroupMSCML = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 1, 10)
)
bwMSGroupMSCML.setObjects(
      *(("BW-BroadworksMediaServer", "msMSCMLPlayCollect"),
        ("BW-BroadworksMediaServer", "msMSCMLPlayCollectFailed"),
        ("BW-BroadworksMediaServer", "msMSCMLPlay"),
        ("BW-BroadworksMediaServer", "msMSCMLPlayFailed"),
        ("BW-BroadworksMediaServer", "msMSCMLPlayRecord"),
        ("BW-BroadworksMediaServer", "msMSCMLRecordFailed"),
        ("BW-BroadworksMediaServer", "msMSCMLSendMail"),
        ("BW-BroadworksMediaServer", "msMSCMLSendMailFailed"),
        ("BW-BroadworksMediaServer", "msMSCMLTotalRecordingDuration"),
        ("BW-BroadworksMediaServer", "msMSCMLEmptyRecordings"))
)
if mibBuilder.loadTexts:
    bwMSGroupMSCML.setStatus("current")

bwMSGroupLiveAudio = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 1, 11)
)
bwMSGroupLiveAudio.setObjects(
      *(("BW-BroadworksMediaServer", "msLiveAudioRequestCount"),
        ("BW-BroadworksMediaServer", "msLiveAudioFailureCount"),
        ("BW-BroadworksMediaServer", "msLiveAudioTotalDuration"),
        ("BW-BroadworksMediaServer", "msLiveAudioULawUserCount"),
        ("BW-BroadworksMediaServer", "msLiveAudioALawUserCount"),
        ("BW-BroadworksMediaServer", "msLiveAudioG726UserCount"),
        ("BW-BroadworksMediaServer", "msLiveAudioG729UserCount"))
)
if mibBuilder.loadTexts:
    bwMSGroupLiveAudio.setStatus("current")

bwMSGroupVideo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 1, 12)
)
bwMSGroupVideo.setObjects(
      *(("BW-BroadworksMediaServer", "msVideoRecorded"),
        ("BW-BroadworksMediaServer", "msVideoPlayback"))
)
if mibBuilder.loadTexts:
    bwMSGroupVideo.setStatus("current")

bwMSGroupFax = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 1, 13)
)
bwMSGroupFax.setObjects(
      *(("BW-BroadworksMediaServer", "msFaxReceived"),
        ("BW-BroadworksMediaServer", "msFaxReceptionFailure"),
        ("BW-BroadworksMediaServer", "msFaxPrinted"),
        ("BW-BroadworksMediaServer", "msFaxPrintingFailure"))
)
if mibBuilder.loadTexts:
    bwMSGroupFax.setStatus("current")

bwMSGroupVxml = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 1, 14)
)
bwMSGroupVxml.setObjects(
      *(("BW-BroadworksMediaServer", "msVoiceXMLErrorCount"),
        ("BW-BroadworksMediaServer", "msVoiceXMLFilesDownloaded"))
)
if mibBuilder.loadTexts:
    bwMSGroupVxml.setStatus("current")

bwMSGroupCcxml = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 1, 15)
)
bwMSGroupCcxml.setObjects(
      *(("BW-BroadworksMediaServer", "msCallControlXMLSessionCount"),
        ("BW-BroadworksMediaServer", "msCallControlXMLCreateCallCount"),
        ("BW-BroadworksMediaServer", "msCallControlXMLDialogCount"),
        ("BW-BroadworksMediaServer", "msCallControlXMLConfCount"))
)
if mibBuilder.loadTexts:
    bwMSGroupCcxml.setStatus("current")

bwMSGroupMrcp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 1, 16)
)
bwMSGroupMrcp.setObjects(
      *(("BW-BroadworksMediaServer", "msCallControlXMLConfCount"),
        ("BW-BroadworksMediaServer", "msMrcpAsrSessionsInUse"),
        ("BW-BroadworksMediaServer", "msMrcpTtsSessionsCount"),
        ("BW-BroadworksMediaServer", "msMrcpTtsSessionsInUse"),
        ("BW-BroadworksMediaServer", "msMrcpRecognitionAttemptsCount"),
        ("BW-BroadworksMediaServer", "msMrcpSuccessfulRecognitionsCount"),
        ("BW-BroadworksMediaServer", "msMrcpRequestsCount"),
        ("BW-BroadworksMediaServer", "msMrcpFailedRequestsCount"),
        ("BW-BroadworksMediaServer", "msMrcpFailedConnectionsCount"),
        ("BW-BroadworksMediaServer", "msMrcpKeepAliveFailuresCount"),
        ("BW-BroadworksMediaServer", "msMrcpSpeakRequestsCount"),
        ("BW-BroadworksMediaServer", "msMrcpSpeakRequestFailuresCount"))
)
if mibBuilder.loadTexts:
    bwMSGroupMrcp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bwMsBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6431, 1, 3, 20, 2, 1)
)
if mibBuilder.loadTexts:
    bwMsBasicCompliance.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BW-BroadworksMediaServer",
    **{"broadsoft": broadsoft,
       "broadworks": broadworks,
       "mediaServer": mediaServer,
       "mcp": mcp,
       "conferencing": conferencing,
       "msConfAddParticipantFailed": msConfAddParticipantFailed,
       "msConfAddParticipant": msConfAddParticipant,
       "msConfAllocateBridge": msConfAllocateBridge,
       "msConfAllocateBridgeFailed": msConfAllocateBridgeFailed,
       "msConfRemoveParticipant": msConfRemoveParticipant,
       "msConfRemoveParticipantFailed": msConfRemoveParticipantFailed,
       "msConfCurrentPortsInUse": msConfCurrentPortsInUse,
       "msConferenceCount": msConferenceCount,
       "msConfTotalDuration": msConfTotalDuration,
       "msConfUpdateParticipant": msConfUpdateParticipant,
       "msConfUpdateParticipantFailed": msConfUpdateParticipantFailed,
       "ivr": ivr,
       "msIvrFreeAudioMemory": msIvrFreeAudioMemory,
       "msIvrAudioMemoryInUse": msIvrAudioMemoryInUse,
       "msIvrCurrentPortsInUse": msIvrCurrentPortsInUse,
       "msIvrCreateConnection": msIvrCreateConnection,
       "msIvrCreateConnectionFailed": msIvrCreateConnectionFailed,
       "msIvrUpdateConnection": msIvrUpdateConnection,
       "msIvrUpdateConnectionFailed": msIvrUpdateConnectionFailed,
       "msIvrPlay": msIvrPlay,
       "msIvrPlayFailed": msIvrPlayFailed,
       "msIvrPlayCollect": msIvrPlayCollect,
       "msIvrPlayCollectFailed": msIvrPlayCollectFailed,
       "msIvrPlayRecord": msIvrPlayRecord,
       "msIvrPlayRecordFailed": msIvrPlayRecordFailed,
       "msIvrSendEmail": msIvrSendEmail,
       "msIvrSendEmailFailed": msIvrSendEmailFailed,
       "msIvrSessionCount": msIvrSessionCount,
       "msIvrTotalDuration": msIvrTotalDuration,
       "msIvrTotalRecordingDuration": msIvrTotalRecordingDuration,
       "msIvrMerge": msIvrMerge,
       "msIvrMergeFailed": msIvrMergeFailed,
       "msIvrEmptyRecordings": msIvrEmptyRecordings,
       "msPortsInUse": msPortsInUse,
       "msNoPortAvailableErrors": msNoPortAvailableErrors,
       "msMCPNotificationsTransmitted": msMCPNotificationsTransmitted,
       "msMCPNotificationsRetransmitted": msMCPNotificationsRetransmitted,
       "msMCPCommandsReceived": msMCPCommandsReceived,
       "rtp": rtp,
       "msRtpSessionsCount": msRtpSessionsCount,
       "receive": receive,
       "msRtcpSenderReports": msRtcpSenderReports,
       "msRtpPacketsExpected": msRtpPacketsExpected,
       "msRtpPacketsReceived": msRtpPacketsReceived,
       "msRtpOutOfOrder": msRtpOutOfOrder,
       "msRtpBadPayload": msRtpBadPayload,
       "msRtpSsrc": msRtpSsrc,
       "msRtpReceivedPacketJitter": msRtpReceivedPacketJitter,
       "transmit": transmit,
       "msRtpCumulativePacketsLost": msRtpCumulativePacketsLost,
       "msRtpPacketsSent": msRtpPacketsSent,
       "msRtpFramesSkipped": msRtpFramesSkipped,
       "msRtpTransmitJitter": msRtpTransmitJitter,
       "msRtpSessionsInUse": msRtpSessionsInUse,
       "smtp": smtp,
       "primary": primary,
       "msPrimaryEmailSent": msPrimaryEmailSent,
       "msPrimarySmtpErrors": msPrimarySmtpErrors,
       "secondary": secondary,
       "msSecondaryEmailSent": msSecondaryEmailSent,
       "msSecondarySmtpErrors": msSecondarySmtpErrors,
       "system": system,
       "msAlarmsCount": msAlarmsCount,
       "msSoftwareErrorsCount": msSoftwareErrorsCount,
       "msACLViolationCount": msACLViolationCount,
       "msMaxCapacityInPorts": msMaxCapacityInPorts,
       "msNumLicensedPorts": msNumLicensedPorts,
       "http": http,
       "msFilesDownloaded": msFilesDownloaded,
       "msTotalSizeDownloadedFiles": msTotalSizeDownloadedFiles,
       "msFilesRetrievedFromCache": msFilesRetrievedFromCache,
       "management": management,
       "resetAllMSCounters": resetAllMSCounters,
       "sip": sip,
       "msSipStatsInviteIns": msSipStatsInviteIns,
       "msSipStatsAckIns": msSipStatsAckIns,
       "msSipStatsByeIns": msSipStatsByeIns,
       "msSipStatsByeOuts": msSipStatsByeOuts,
       "msSipStatsInfoIns": msSipStatsInfoIns,
       "msSipStatsInfoOuts": msSipStatsInfoOuts,
       "msSipStatsOthersIns": msSipStatsOthersIns,
       "msSipStatsOthersOuts": msSipStatsOthersOuts,
       "msSipStatsResponsesIns": msSipStatsResponsesIns,
       "msSipStatsResponsesOuts": msSipStatsResponsesOuts,
       "msSipStatsInvite200OKRetransmitsOuts": msSipStatsInvite200OKRetransmitsOuts,
       "msSipStatsRequestRetransmittedIns": msSipStatsRequestRetransmittedIns,
       "msSipStatsReferOuts": msSipStatsReferOuts,
       "msRedirectsCount": msRedirectsCount,
       "msTimeOutRouteAdvancesCount": msTimeOutRouteAdvancesCount,
       "msRouteAdvancesCount": msRouteAdvancesCount,
       "mscml": mscml,
       "msMSCMLPlayCollect": msMSCMLPlayCollect,
       "msMSCMLPlayCollectFailed": msMSCMLPlayCollectFailed,
       "msMSCMLPlay": msMSCMLPlay,
       "msMSCMLPlayFailed": msMSCMLPlayFailed,
       "msMSCMLPlayRecord": msMSCMLPlayRecord,
       "msMSCMLRecordFailed": msMSCMLRecordFailed,
       "msMSCMLSendMail": msMSCMLSendMail,
       "msMSCMLSendMailFailed": msMSCMLSendMailFailed,
       "msMSCMLTotalRecordingDuration": msMSCMLTotalRecordingDuration,
       "msMSCMLEmptyRecordings": msMSCMLEmptyRecordings,
       "liveaudio": liveaudio,
       "msLiveAudioRequestCount": msLiveAudioRequestCount,
       "msLiveAudioFailureCount": msLiveAudioFailureCount,
       "msLiveAudioTotalDuration": msLiveAudioTotalDuration,
       "msLiveAudioULawUserCount": msLiveAudioULawUserCount,
       "msLiveAudioALawUserCount": msLiveAudioALawUserCount,
       "msLiveAudioG726UserCount": msLiveAudioG726UserCount,
       "msLiveAudioG729UserCount": msLiveAudioG729UserCount,
       "video": video,
       "msVideoRecorded": msVideoRecorded,
       "msVideoPlayback": msVideoPlayback,
       "fax": fax,
       "msFaxReceived": msFaxReceived,
       "msFaxReceptionFailure": msFaxReceptionFailure,
       "msFaxPrinted": msFaxPrinted,
       "msFaxPrintingFailure": msFaxPrintingFailure,
       "vxml": vxml,
       "msVoiceXMLErrorCount": msVoiceXMLErrorCount,
       "msVoiceXMLFilesDownloaded": msVoiceXMLFilesDownloaded,
       "ccxml": ccxml,
       "msCallControlXMLSessionCount": msCallControlXMLSessionCount,
       "msCallControlXMLCreateCallCount": msCallControlXMLCreateCallCount,
       "msCallControlXMLDialogCount": msCallControlXMLDialogCount,
       "msCallControlXMLConfCount": msCallControlXMLConfCount,
       "interfaces": interfaces,
       "mrcp": mrcp,
       "msMrcpAsrSessionsCount": msMrcpAsrSessionsCount,
       "msMrcpAsrSessionsInUse": msMrcpAsrSessionsInUse,
       "msMrcpTtsSessionsCount": msMrcpTtsSessionsCount,
       "msMrcpTtsSessionsInUse": msMrcpTtsSessionsInUse,
       "msMrcpRecognitionAttemptsCount": msMrcpRecognitionAttemptsCount,
       "msMrcpSuccessfulRecognitionsCount": msMrcpSuccessfulRecognitionsCount,
       "msMrcpRequestsCount": msMrcpRequestsCount,
       "msMrcpFailedRequestsCount": msMrcpFailedRequestsCount,
       "msMrcpFailedConnectionsCount": msMrcpFailedConnectionsCount,
       "msMrcpKeepAliveFailuresCount": msMrcpKeepAliveFailuresCount,
       "msMrcpSpeakRequestsCount": msMrcpSpeakRequestsCount,
       "msMrcpSpeakRequestFailuresCount": msMrcpSpeakRequestFailuresCount,
       "bwMsConformance": bwMsConformance,
       "bwMSGroups": bwMSGroups,
       "bwMSGroupMCP": bwMSGroupMCP,
       "bwMSGroupMCPConferencing": bwMSGroupMCPConferencing,
       "bwMSGroupMCPIVR": bwMSGroupMCPIVR,
       "bwMSGroupRTP": bwMSGroupRTP,
       "bwMSGroupSMTP": bwMSGroupSMTP,
       "bwMSGroupSystem": bwMSGroupSystem,
       "bwMSGroupHTTP": bwMSGroupHTTP,
       "bwMSGroupManagement": bwMSGroupManagement,
       "bwMSGroupSIP": bwMSGroupSIP,
       "bwMSGroupMSCML": bwMSGroupMSCML,
       "bwMSGroupLiveAudio": bwMSGroupLiveAudio,
       "bwMSGroupVideo": bwMSGroupVideo,
       "bwMSGroupFax": bwMSGroupFax,
       "bwMSGroupVxml": bwMSGroupVxml,
       "bwMSGroupCcxml": bwMSGroupCcxml,
       "bwMSGroupMrcp": bwMSGroupMrcp,
       "bwMSCompliancy": bwMSCompliancy,
       "bwMsBasicCompliance": bwMsBasicCompliance}
)
