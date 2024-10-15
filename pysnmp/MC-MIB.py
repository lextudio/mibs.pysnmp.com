# SNMP MIB module (MC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:38 2024
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

(MmEndpointID,
 MmGatekeeperID,
 MmGlobalIdentifier,
 MmTAddressTag) = mibBuilder.importSymbols(
    "MULTI-MEDIA-MIB-TC",
    "MmEndpointID",
    "MmGatekeeperID",
    "MmGlobalIdentifier",
    "MmTAddressTag")

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
 RowStatus,
 TAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h323MC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Media_ObjectIdentity = ObjectIdentity
media = _Media_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3011, 2)
)
_McConfig_ObjectIdentity = ObjectIdentity
mcConfig = _McConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 1)
)
_McConfigMcCallSignalingTag_Type = MmTAddressTag
_McConfigMcCallSignalingTag_Object = MibScalar
mcConfigMcCallSignalingTag = _McConfigMcCallSignalingTag_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 1, 1),
    _McConfigMcCallSignalingTag_Type()
)
mcConfigMcCallSignalingTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcConfigMcCallSignalingTag.setStatus("current")
_McConfigMcCallSignalingAddress_Type = TAddress
_McConfigMcCallSignalingAddress_Object = MibScalar
mcConfigMcCallSignalingAddress = _McConfigMcCallSignalingAddress_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 1, 2),
    _McConfigMcCallSignalingAddress_Type()
)
mcConfigMcCallSignalingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcConfigMcCallSignalingAddress.setStatus("current")
_McConfigGatekeeperAddressTag_Type = MmTAddressTag
_McConfigGatekeeperAddressTag_Object = MibScalar
mcConfigGatekeeperAddressTag = _McConfigGatekeeperAddressTag_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 1, 3),
    _McConfigGatekeeperAddressTag_Type()
)
mcConfigGatekeeperAddressTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcConfigGatekeeperAddressTag.setStatus("current")
_McConfigGatekeeperAddress_Type = TAddress
_McConfigGatekeeperAddress_Object = MibScalar
mcConfigGatekeeperAddress = _McConfigGatekeeperAddress_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 1, 4),
    _McConfigGatekeeperAddress_Type()
)
mcConfigGatekeeperAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcConfigGatekeeperAddress.setStatus("current")
_McConfigIsRegisteredWithGatekeeper_Type = TruthValue
_McConfigIsRegisteredWithGatekeeper_Object = MibScalar
mcConfigIsRegisteredWithGatekeeper = _McConfigIsRegisteredWithGatekeeper_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 1, 5),
    _McConfigIsRegisteredWithGatekeeper_Type()
)
mcConfigIsRegisteredWithGatekeeper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcConfigIsRegisteredWithGatekeeper.setStatus("current")
_McConference_ObjectIdentity = ObjectIdentity
mcConference = _McConference_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2)
)
_McConferenceTable_Object = MibTable
mcConferenceTable = _McConferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mcConferenceTable.setStatus("current")
_McConferenceTableEntry_Object = MibTableRow
mcConferenceTableEntry = _McConferenceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1, 1)
)
mcConferenceTableEntry.setIndexNames(
    (0, "MC-MIB", "mcConferenceConferenceId"),
)
if mibBuilder.loadTexts:
    mcConferenceTableEntry.setStatus("current")
_McConferenceConferenceId_Type = MmGlobalIdentifier
_McConferenceConferenceId_Object = MibTableColumn
mcConferenceConferenceId = _McConferenceConferenceId_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1, 1, 1),
    _McConferenceConferenceId_Type()
)
mcConferenceConferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcConferenceConferenceId.setStatus("current")
_McConferenceConferenceStartTime_Type = DateAndTime
_McConferenceConferenceStartTime_Object = MibTableColumn
mcConferenceConferenceStartTime = _McConferenceConferenceStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1, 1, 2),
    _McConferenceConferenceStartTime_Type()
)
mcConferenceConferenceStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcConferenceConferenceStartTime.setStatus("current")
_McConferenceConferenceEndTime_Type = DateAndTime
_McConferenceConferenceEndTime_Object = MibTableColumn
mcConferenceConferenceEndTime = _McConferenceConferenceEndTime_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1, 1, 3),
    _McConferenceConferenceEndTime_Type()
)
mcConferenceConferenceEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcConferenceConferenceEndTime.setStatus("current")


class _McConferenceCentralizedOrDistributed_Type(Integer32):
    """Custom type mcConferenceCentralizedOrDistributed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("centralized", 1),
          ("distributed", 2))
    )


_McConferenceCentralizedOrDistributed_Type.__name__ = "Integer32"
_McConferenceCentralizedOrDistributed_Object = MibTableColumn
mcConferenceCentralizedOrDistributed = _McConferenceCentralizedOrDistributed_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1, 1, 4),
    _McConferenceCentralizedOrDistributed_Type()
)
mcConferenceCentralizedOrDistributed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcConferenceCentralizedOrDistributed.setStatus("current")


class _McConferenceUniOrMulticast_Type(Integer32):
    """Custom type mcConferenceUniOrMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 2),
          ("unicast", 1))
    )


_McConferenceUniOrMulticast_Type.__name__ = "Integer32"
_McConferenceUniOrMulticast_Object = MibTableColumn
mcConferenceUniOrMulticast = _McConferenceUniOrMulticast_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1, 1, 5),
    _McConferenceUniOrMulticast_Type()
)
mcConferenceUniOrMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcConferenceUniOrMulticast.setStatus("current")
_McConferenceActiveMcAddress_Type = TAddress
_McConferenceActiveMcAddress_Object = MibTableColumn
mcConferenceActiveMcAddress = _McConferenceActiveMcAddress_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1, 1, 6),
    _McConferenceActiveMcAddress_Type()
)
mcConferenceActiveMcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcConferenceActiveMcAddress.setStatus("current")
_McConferenceParticipantsTable_Object = MibTable
mcConferenceParticipantsTable = _McConferenceParticipantsTable_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    mcConferenceParticipantsTable.setStatus("current")
_McConferenceParticipantsTableEntry_Object = MibTableRow
mcConferenceParticipantsTableEntry = _McConferenceParticipantsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1)
)
mcConferenceParticipantsTableEntry.setIndexNames(
    (0, "MC-MIB", "mcConferenceConferenceId"),
    (0, "MC-MIB", "mcConferenceParticipantsTableIndex"),
)
if mibBuilder.loadTexts:
    mcConferenceParticipantsTableEntry.setStatus("current")
_McConferenceParticipantsTableIndex_Type = Integer32
_McConferenceParticipantsTableIndex_Object = MibTableColumn
mcConferenceParticipantsTableIndex = _McConferenceParticipantsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 1),
    _McConferenceParticipantsTableIndex_Type()
)
mcConferenceParticipantsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcConferenceParticipantsTableIndex.setStatus("current")
_McConferenceParticipantsTerminalLabel_Type = OctetString
_McConferenceParticipantsTerminalLabel_Object = MibTableColumn
mcConferenceParticipantsTerminalLabel = _McConferenceParticipantsTerminalLabel_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 2),
    _McConferenceParticipantsTerminalLabel_Type()
)
mcConferenceParticipantsTerminalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcConferenceParticipantsTerminalLabel.setStatus("current")
_McConferenceParticipantsCallSignalingtAddressTag_Type = MmTAddressTag
_McConferenceParticipantsCallSignalingtAddressTag_Object = MibTableColumn
mcConferenceParticipantsCallSignalingtAddressTag = _McConferenceParticipantsCallSignalingtAddressTag_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 3),
    _McConferenceParticipantsCallSignalingtAddressTag_Type()
)
mcConferenceParticipantsCallSignalingtAddressTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcConferenceParticipantsCallSignalingtAddressTag.setStatus("current")
_McConferenceParticipantsCallSignalingAddress_Type = TAddress
_McConferenceParticipantsCallSignalingAddress_Object = MibTableColumn
mcConferenceParticipantsCallSignalingAddress = _McConferenceParticipantsCallSignalingAddress_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 4),
    _McConferenceParticipantsCallSignalingAddress_Type()
)
mcConferenceParticipantsCallSignalingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcConferenceParticipantsCallSignalingAddress.setStatus("current")
_McConferenceParticipantsCallId_Type = MmGlobalIdentifier
_McConferenceParticipantsCallId_Object = MibTableColumn
mcConferenceParticipantsCallId = _McConferenceParticipantsCallId_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 5),
    _McConferenceParticipantsCallId_Type()
)
mcConferenceParticipantsCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcConferenceParticipantsCallId.setStatus("current")
_McConferenceParticipantsControlChannelIndex_Type = Integer32
_McConferenceParticipantsControlChannelIndex_Object = MibTableColumn
mcConferenceParticipantsControlChannelIndex = _McConferenceParticipantsControlChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 6),
    _McConferenceParticipantsControlChannelIndex_Type()
)
mcConferenceParticipantsControlChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcConferenceParticipantsControlChannelIndex.setStatus("current")
_McConferenceParticipantsNumberOfLogicalChannels_Type = Integer32
_McConferenceParticipantsNumberOfLogicalChannels_Object = MibTableColumn
mcConferenceParticipantsNumberOfLogicalChannels = _McConferenceParticipantsNumberOfLogicalChannels_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 7),
    _McConferenceParticipantsNumberOfLogicalChannels_Type()
)
mcConferenceParticipantsNumberOfLogicalChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcConferenceParticipantsNumberOfLogicalChannels.setStatus("current")
_McConferenceParticipantsRtpSessionIndex_Type = Integer32
_McConferenceParticipantsRtpSessionIndex_Object = MibTableColumn
mcConferenceParticipantsRtpSessionIndex = _McConferenceParticipantsRtpSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 8),
    _McConferenceParticipantsRtpSessionIndex_Type()
)
mcConferenceParticipantsRtpSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcConferenceParticipantsRtpSessionIndex.setStatus("current")
_McStats_ObjectIdentity = ObjectIdentity
mcStats = _McStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 3)
)
_McStatsTotalConferences_Type = Integer32
_McStatsTotalConferences_Object = MibScalar
mcStatsTotalConferences = _McStatsTotalConferences_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 3, 1),
    _McStatsTotalConferences_Type()
)
mcStatsTotalConferences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcStatsTotalConferences.setStatus("current")
_McStatsSuccessfullyCompletedConferences_Type = Integer32
_McStatsSuccessfullyCompletedConferences_Object = MibScalar
mcStatsSuccessfullyCompletedConferences = _McStatsSuccessfullyCompletedConferences_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 3, 2),
    _McStatsSuccessfullyCompletedConferences_Type()
)
mcStatsSuccessfullyCompletedConferences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcStatsSuccessfullyCompletedConferences.setStatus("current")
_McStatsAbnormalyTerminatedConferences_Type = Integer32
_McStatsAbnormalyTerminatedConferences_Object = MibScalar
mcStatsAbnormalyTerminatedConferences = _McStatsAbnormalyTerminatedConferences_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 3, 3),
    _McStatsAbnormalyTerminatedConferences_Type()
)
mcStatsAbnormalyTerminatedConferences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcStatsAbnormalyTerminatedConferences.setStatus("current")
_McEvents_ObjectIdentity = ObjectIdentity
mcEvents = _McEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 4)
)


class _LastConferenceTerminationReason_Type(Integer32):
    """Custom type lastConferenceTerminationReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("administrativelyTerminated", 2),
          ("normalTermination", 1))
    )


_LastConferenceTerminationReason_Type.__name__ = "Integer32"
_LastConferenceTerminationReason_Object = MibScalar
lastConferenceTerminationReason = _LastConferenceTerminationReason_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 4, 1),
    _LastConferenceTerminationReason_Type()
)
lastConferenceTerminationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConferenceTerminationReason.setStatus("current")
_LastTerminatedConferenceId_Type = MmGlobalIdentifier
_LastTerminatedConferenceId_Object = MibScalar
lastTerminatedConferenceId = _LastTerminatedConferenceId_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 4, 2),
    _LastTerminatedConferenceId_Type()
)
lastTerminatedConferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastTerminatedConferenceId.setStatus("current")
_McMIBConformance_ObjectIdentity = ObjectIdentity
mcMIBConformance = _McMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 5)
)
_McMIBGroups_ObjectIdentity = ObjectIdentity
mcMIBGroups = _McMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 5, 1)
)

# Managed Objects groups

configGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 5, 1, 1)
)
configGroup.setObjects(
      *(("MC-MIB", "mcConfigMcCallSignalingTag"),
        ("MC-MIB", "mcConfigMcCallSignalingAddress"),
        ("MC-MIB", "mcConfigGatekeeperAddressTag"),
        ("MC-MIB", "mcConfigGatekeeperAddress"),
        ("MC-MIB", "mcConfigIsRegisteredWithGatekeeper"))
)
if mibBuilder.loadTexts:
    configGroup.setStatus("current")

conferenceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 5, 1, 2)
)
conferenceGroup.setObjects(
      *(("MC-MIB", "mcConferenceConferenceId"),
        ("MC-MIB", "mcConferenceConferenceStartTime"),
        ("MC-MIB", "mcConferenceConferenceEndTime"),
        ("MC-MIB", "mcConferenceCentralizedOrDistributed"),
        ("MC-MIB", "mcConferenceUniOrMulticast"),
        ("MC-MIB", "mcConferenceActiveMcAddress"),
        ("MC-MIB", "mcConferenceParticipantsTerminalLabel"),
        ("MC-MIB", "mcConferenceParticipantsCallSignalingtAddressTag"),
        ("MC-MIB", "mcConferenceParticipantsCallSignalingAddress"),
        ("MC-MIB", "mcConferenceParticipantsCallId"),
        ("MC-MIB", "mcConferenceParticipantsControlChannelIndex"),
        ("MC-MIB", "mcConferenceParticipantsNumberOfLogicalChannels"),
        ("MC-MIB", "mcConferenceParticipantsRtpSessionIndex"))
)
if mibBuilder.loadTexts:
    conferenceGroup.setStatus("current")

mcStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 5, 1, 4)
)
mcStatsGroup.setObjects(
      *(("MC-MIB", "mcStatsTotalConferences"),
        ("MC-MIB", "mcStatsSuccessfullyCompletedConferences"),
        ("MC-MIB", "mcStatsAbnormalyTerminatedConferences"))
)
if mibBuilder.loadTexts:
    mcStatsGroup.setStatus("current")

mcEventsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 5, 1, 5)
)
mcEventsGroup.setObjects(
    ("MC-MIB", "lastConferenceTerminationReason")
)
if mibBuilder.loadTexts:
    mcEventsGroup.setStatus("current")


# Notification objects

conferenceTermination = NotificationType(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 4, 3)
)
conferenceTermination.setObjects(
      *(("MC-MIB", "lastTerminatedConferenceId"),
        ("MC-MIB", "lastConferenceTerminationReason"))
)
if mibBuilder.loadTexts:
    conferenceTermination.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

mcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    mcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MC-MIB",
    **{"media": media,
       "h323MC": h323MC,
       "mcConfig": mcConfig,
       "mcConfigMcCallSignalingTag": mcConfigMcCallSignalingTag,
       "mcConfigMcCallSignalingAddress": mcConfigMcCallSignalingAddress,
       "mcConfigGatekeeperAddressTag": mcConfigGatekeeperAddressTag,
       "mcConfigGatekeeperAddress": mcConfigGatekeeperAddress,
       "mcConfigIsRegisteredWithGatekeeper": mcConfigIsRegisteredWithGatekeeper,
       "mcConference": mcConference,
       "mcConferenceTable": mcConferenceTable,
       "mcConferenceTableEntry": mcConferenceTableEntry,
       "mcConferenceConferenceId": mcConferenceConferenceId,
       "mcConferenceConferenceStartTime": mcConferenceConferenceStartTime,
       "mcConferenceConferenceEndTime": mcConferenceConferenceEndTime,
       "mcConferenceCentralizedOrDistributed": mcConferenceCentralizedOrDistributed,
       "mcConferenceUniOrMulticast": mcConferenceUniOrMulticast,
       "mcConferenceActiveMcAddress": mcConferenceActiveMcAddress,
       "mcConferenceParticipantsTable": mcConferenceParticipantsTable,
       "mcConferenceParticipantsTableEntry": mcConferenceParticipantsTableEntry,
       "mcConferenceParticipantsTableIndex": mcConferenceParticipantsTableIndex,
       "mcConferenceParticipantsTerminalLabel": mcConferenceParticipantsTerminalLabel,
       "mcConferenceParticipantsCallSignalingtAddressTag": mcConferenceParticipantsCallSignalingtAddressTag,
       "mcConferenceParticipantsCallSignalingAddress": mcConferenceParticipantsCallSignalingAddress,
       "mcConferenceParticipantsCallId": mcConferenceParticipantsCallId,
       "mcConferenceParticipantsControlChannelIndex": mcConferenceParticipantsControlChannelIndex,
       "mcConferenceParticipantsNumberOfLogicalChannels": mcConferenceParticipantsNumberOfLogicalChannels,
       "mcConferenceParticipantsRtpSessionIndex": mcConferenceParticipantsRtpSessionIndex,
       "mcStats": mcStats,
       "mcStatsTotalConferences": mcStatsTotalConferences,
       "mcStatsSuccessfullyCompletedConferences": mcStatsSuccessfullyCompletedConferences,
       "mcStatsAbnormalyTerminatedConferences": mcStatsAbnormalyTerminatedConferences,
       "mcEvents": mcEvents,
       "lastConferenceTerminationReason": lastConferenceTerminationReason,
       "lastTerminatedConferenceId": lastTerminatedConferenceId,
       "conferenceTermination": conferenceTermination,
       "mcMIBConformance": mcMIBConformance,
       "mcMIBGroups": mcMIBGroups,
       "configGroup": configGroup,
       "conferenceGroup": conferenceGroup,
       "mcStatsGroup": mcStatsGroup,
       "mcEventsGroup": mcEventsGroup,
       "mcMIBCompliance": mcMIBCompliance}
)
