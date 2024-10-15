# SNMP MIB module (H323MC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H323MC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:46 2024
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

(MmGlobalIdentifier,
 MmTAddressTag,
 mmH323Root) = mibBuilder.importSymbols(
    "MULTI-MEDIA-MIB-TC",
    "MmGlobalIdentifier",
    "MmTAddressTag",
    "mmH323Root")

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

(DateAndTime,
 DisplayString,
 TAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h323MC = ModuleIdentity(
    (0, 0, 8, 341, 1, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H323McSystem_ObjectIdentity = ObjectIdentity
h323McSystem = _H323McSystem_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 4, 1)
)
_H323McSystemTable_Object = MibTable
h323McSystemTable = _H323McSystemTable_Object(
    (0, 0, 8, 341, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    h323McSystemTable.setStatus("current")
_H323McSystemTableEntry_Object = MibTableRow
h323McSystemTableEntry = _H323McSystemTableEntry_Object(
    (0, 0, 8, 341, 1, 1, 4, 1, 1, 1)
)
h323McSystemTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323McSystemTableEntry.setStatus("current")


class _H323McSystemNameAndMaker_Type(DisplayString):
    """Custom type h323McSystemNameAndMaker based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H323McSystemNameAndMaker_Type.__name__ = "DisplayString"
_H323McSystemNameAndMaker_Object = MibTableColumn
h323McSystemNameAndMaker = _H323McSystemNameAndMaker_Object(
    (0, 0, 8, 341, 1, 1, 4, 1, 1, 1, 1),
    _H323McSystemNameAndMaker_Type()
)
h323McSystemNameAndMaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McSystemNameAndMaker.setStatus("current")
_H323McSystemSoftwareVersionNumber_Type = DisplayString
_H323McSystemSoftwareVersionNumber_Object = MibTableColumn
h323McSystemSoftwareVersionNumber = _H323McSystemSoftwareVersionNumber_Object(
    (0, 0, 8, 341, 1, 1, 4, 1, 1, 1, 2),
    _H323McSystemSoftwareVersionNumber_Type()
)
h323McSystemSoftwareVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McSystemSoftwareVersionNumber.setStatus("current")
_H323McSystemHardwareVersionNumber_Type = DisplayString
_H323McSystemHardwareVersionNumber_Object = MibTableColumn
h323McSystemHardwareVersionNumber = _H323McSystemHardwareVersionNumber_Object(
    (0, 0, 8, 341, 1, 1, 4, 1, 1, 1, 3),
    _H323McSystemHardwareVersionNumber_Type()
)
h323McSystemHardwareVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McSystemHardwareVersionNumber.setStatus("current")
_H323McSystemStartUpTime_Type = DateAndTime
_H323McSystemStartUpTime_Object = MibTableColumn
h323McSystemStartUpTime = _H323McSystemStartUpTime_Object(
    (0, 0, 8, 341, 1, 1, 4, 1, 1, 1, 4),
    _H323McSystemStartUpTime_Type()
)
h323McSystemStartUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McSystemStartUpTime.setStatus("current")
_H323McConfig_ObjectIdentity = ObjectIdentity
h323McConfig = _H323McConfig_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 4, 2)
)
_H323McConfigTable_Object = MibTable
h323McConfigTable = _H323McConfigTable_Object(
    (0, 0, 8, 341, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    h323McConfigTable.setStatus("current")
_H323McConfigTableEntry_Object = MibTableRow
h323McConfigTableEntry = _H323McConfigTableEntry_Object(
    (0, 0, 8, 341, 1, 1, 4, 2, 1, 1)
)
h323McConfigTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323McConfigTableEntry.setStatus("current")
_H323McConfigMcCallSignalingTag_Type = MmTAddressTag
_H323McConfigMcCallSignalingTag_Object = MibTableColumn
h323McConfigMcCallSignalingTag = _H323McConfigMcCallSignalingTag_Object(
    (0, 0, 8, 341, 1, 1, 4, 2, 1, 1, 1),
    _H323McConfigMcCallSignalingTag_Type()
)
h323McConfigMcCallSignalingTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConfigMcCallSignalingTag.setStatus("current")
_H323McConfigMcCallSignalingAddress_Type = TAddress
_H323McConfigMcCallSignalingAddress_Object = MibTableColumn
h323McConfigMcCallSignalingAddress = _H323McConfigMcCallSignalingAddress_Object(
    (0, 0, 8, 341, 1, 1, 4, 2, 1, 1, 2),
    _H323McConfigMcCallSignalingAddress_Type()
)
h323McConfigMcCallSignalingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConfigMcCallSignalingAddress.setStatus("current")
_H323McConfigGatekeeperAddressTag_Type = MmTAddressTag
_H323McConfigGatekeeperAddressTag_Object = MibTableColumn
h323McConfigGatekeeperAddressTag = _H323McConfigGatekeeperAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 4, 2, 1, 1, 3),
    _H323McConfigGatekeeperAddressTag_Type()
)
h323McConfigGatekeeperAddressTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConfigGatekeeperAddressTag.setStatus("current")
_H323McConfigGatekeeperAddress_Type = TAddress
_H323McConfigGatekeeperAddress_Object = MibTableColumn
h323McConfigGatekeeperAddress = _H323McConfigGatekeeperAddress_Object(
    (0, 0, 8, 341, 1, 1, 4, 2, 1, 1, 4),
    _H323McConfigGatekeeperAddress_Type()
)
h323McConfigGatekeeperAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConfigGatekeeperAddress.setStatus("current")
_H323McConfigIsRegisteredWithGatekeeper_Type = TruthValue
_H323McConfigIsRegisteredWithGatekeeper_Object = MibTableColumn
h323McConfigIsRegisteredWithGatekeeper = _H323McConfigIsRegisteredWithGatekeeper_Object(
    (0, 0, 8, 341, 1, 1, 4, 2, 1, 1, 5),
    _H323McConfigIsRegisteredWithGatekeeper_Type()
)
h323McConfigIsRegisteredWithGatekeeper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConfigIsRegisteredWithGatekeeper.setStatus("current")


class _H323McConfigEnableNotifications_Type(Integer32):
    """Custom type h323McConfigEnableNotifications based on Integer32"""
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


_H323McConfigEnableNotifications_Type.__name__ = "Integer32"
_H323McConfigEnableNotifications_Object = MibTableColumn
h323McConfigEnableNotifications = _H323McConfigEnableNotifications_Object(
    (0, 0, 8, 341, 1, 1, 4, 2, 1, 1, 6),
    _H323McConfigEnableNotifications_Type()
)
h323McConfigEnableNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConfigEnableNotifications.setStatus("current")
_H323McConference_ObjectIdentity = ObjectIdentity
h323McConference = _H323McConference_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 4, 3)
)
_H323McConferenceTable_Object = MibTable
h323McConferenceTable = _H323McConferenceTable_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    h323McConferenceTable.setStatus("current")
_H323McConferenceTableEntry_Object = MibTableRow
h323McConferenceTableEntry = _H323McConferenceTableEntry_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 1, 1)
)
h323McConferenceTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H323MC-MIB", "h323McConferenceConferenceId"),
)
if mibBuilder.loadTexts:
    h323McConferenceTableEntry.setStatus("current")
_H323McConferenceConferenceId_Type = MmGlobalIdentifier
_H323McConferenceConferenceId_Object = MibTableColumn
h323McConferenceConferenceId = _H323McConferenceConferenceId_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 1, 1, 1),
    _H323McConferenceConferenceId_Type()
)
h323McConferenceConferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConferenceConferenceId.setStatus("current")
_H323McConferenceConferenceStartTime_Type = DateAndTime
_H323McConferenceConferenceStartTime_Object = MibTableColumn
h323McConferenceConferenceStartTime = _H323McConferenceConferenceStartTime_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 1, 1, 2),
    _H323McConferenceConferenceStartTime_Type()
)
h323McConferenceConferenceStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConferenceConferenceStartTime.setStatus("current")
_H323McConferenceConferenceEndTime_Type = DateAndTime
_H323McConferenceConferenceEndTime_Object = MibTableColumn
h323McConferenceConferenceEndTime = _H323McConferenceConferenceEndTime_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 1, 1, 3),
    _H323McConferenceConferenceEndTime_Type()
)
h323McConferenceConferenceEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConferenceConferenceEndTime.setStatus("current")


class _H323McConferenceCentralizedOrDistributed_Type(Integer32):
    """Custom type h323McConferenceCentralizedOrDistributed based on Integer32"""
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


_H323McConferenceCentralizedOrDistributed_Type.__name__ = "Integer32"
_H323McConferenceCentralizedOrDistributed_Object = MibTableColumn
h323McConferenceCentralizedOrDistributed = _H323McConferenceCentralizedOrDistributed_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 1, 1, 4),
    _H323McConferenceCentralizedOrDistributed_Type()
)
h323McConferenceCentralizedOrDistributed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConferenceCentralizedOrDistributed.setStatus("current")


class _H323McConferenceUniOrMulticast_Type(Integer32):
    """Custom type h323McConferenceUniOrMulticast based on Integer32"""
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


_H323McConferenceUniOrMulticast_Type.__name__ = "Integer32"
_H323McConferenceUniOrMulticast_Object = MibTableColumn
h323McConferenceUniOrMulticast = _H323McConferenceUniOrMulticast_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 1, 1, 5),
    _H323McConferenceUniOrMulticast_Type()
)
h323McConferenceUniOrMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConferenceUniOrMulticast.setStatus("current")
_H323McConferenceActiveMcAddress_Type = TAddress
_H323McConferenceActiveMcAddress_Object = MibTableColumn
h323McConferenceActiveMcAddress = _H323McConferenceActiveMcAddress_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 1, 1, 6),
    _H323McConferenceActiveMcAddress_Type()
)
h323McConferenceActiveMcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConferenceActiveMcAddress.setStatus("current")
_H323McConferenceParticipantsTable_Object = MibTable
h323McConferenceParticipantsTable = _H323McConferenceParticipantsTable_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    h323McConferenceParticipantsTable.setStatus("current")
_H323McConferenceParticipantsTableEntry_Object = MibTableRow
h323McConferenceParticipantsTableEntry = _H323McConferenceParticipantsTableEntry_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 2, 1)
)
h323McConferenceParticipantsTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H323MC-MIB", "h323McConferenceConferenceId"),
    (0, "H323MC-MIB", "h323McConferenceParticipantsTableIndex"),
)
if mibBuilder.loadTexts:
    h323McConferenceParticipantsTableEntry.setStatus("current")
_H323McConferenceParticipantsTableIndex_Type = Integer32
_H323McConferenceParticipantsTableIndex_Object = MibTableColumn
h323McConferenceParticipantsTableIndex = _H323McConferenceParticipantsTableIndex_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 2, 1, 1),
    _H323McConferenceParticipantsTableIndex_Type()
)
h323McConferenceParticipantsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h323McConferenceParticipantsTableIndex.setStatus("current")


class _H323McConferenceParticipantsTerminalLabel_Type(OctetString):
    """Custom type h323McConferenceParticipantsTerminalLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_H323McConferenceParticipantsTerminalLabel_Type.__name__ = "OctetString"
_H323McConferenceParticipantsTerminalLabel_Object = MibTableColumn
h323McConferenceParticipantsTerminalLabel = _H323McConferenceParticipantsTerminalLabel_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 2, 1, 2),
    _H323McConferenceParticipantsTerminalLabel_Type()
)
h323McConferenceParticipantsTerminalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConferenceParticipantsTerminalLabel.setStatus("current")
_H323McConferenceParticipantsCallSignalingTAddressTag_Type = MmTAddressTag
_H323McConferenceParticipantsCallSignalingTAddressTag_Object = MibTableColumn
h323McConferenceParticipantsCallSignalingTAddressTag = _H323McConferenceParticipantsCallSignalingTAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 2, 1, 3),
    _H323McConferenceParticipantsCallSignalingTAddressTag_Type()
)
h323McConferenceParticipantsCallSignalingTAddressTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConferenceParticipantsCallSignalingTAddressTag.setStatus("current")
_H323McConferenceParticipantsCallSignalingAddress_Type = TAddress
_H323McConferenceParticipantsCallSignalingAddress_Object = MibTableColumn
h323McConferenceParticipantsCallSignalingAddress = _H323McConferenceParticipantsCallSignalingAddress_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 2, 1, 4),
    _H323McConferenceParticipantsCallSignalingAddress_Type()
)
h323McConferenceParticipantsCallSignalingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConferenceParticipantsCallSignalingAddress.setStatus("current")
_H323McConferenceParticipantsCallId_Type = MmGlobalIdentifier
_H323McConferenceParticipantsCallId_Object = MibTableColumn
h323McConferenceParticipantsCallId = _H323McConferenceParticipantsCallId_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 2, 1, 5),
    _H323McConferenceParticipantsCallId_Type()
)
h323McConferenceParticipantsCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConferenceParticipantsCallId.setStatus("current")
_H323McConferenceParticipantsControlChannelIndex_Type = Integer32
_H323McConferenceParticipantsControlChannelIndex_Object = MibTableColumn
h323McConferenceParticipantsControlChannelIndex = _H323McConferenceParticipantsControlChannelIndex_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 2, 1, 6),
    _H323McConferenceParticipantsControlChannelIndex_Type()
)
h323McConferenceParticipantsControlChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConferenceParticipantsControlChannelIndex.setStatus("current")
_H323McConferenceParticipantsNumberOfLogicalChannels_Type = Integer32
_H323McConferenceParticipantsNumberOfLogicalChannels_Object = MibTableColumn
h323McConferenceParticipantsNumberOfLogicalChannels = _H323McConferenceParticipantsNumberOfLogicalChannels_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 2, 1, 7),
    _H323McConferenceParticipantsNumberOfLogicalChannels_Type()
)
h323McConferenceParticipantsNumberOfLogicalChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConferenceParticipantsNumberOfLogicalChannels.setStatus("current")
_H323McConferenceParticipantsRtpSessionIndex_Type = Integer32
_H323McConferenceParticipantsRtpSessionIndex_Object = MibTableColumn
h323McConferenceParticipantsRtpSessionIndex = _H323McConferenceParticipantsRtpSessionIndex_Object(
    (0, 0, 8, 341, 1, 1, 4, 3, 2, 1, 8),
    _H323McConferenceParticipantsRtpSessionIndex_Type()
)
h323McConferenceParticipantsRtpSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McConferenceParticipantsRtpSessionIndex.setStatus("current")
_H323McStats_ObjectIdentity = ObjectIdentity
h323McStats = _H323McStats_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 4, 4)
)
_H323McStatsTotalConferences_Type = Integer32
_H323McStatsTotalConferences_Object = MibScalar
h323McStatsTotalConferences = _H323McStatsTotalConferences_Object(
    (0, 0, 8, 341, 1, 1, 4, 4, 1),
    _H323McStatsTotalConferences_Type()
)
h323McStatsTotalConferences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McStatsTotalConferences.setStatus("current")
_H323McStatsSuccessfullyCompletedConferences_Type = Integer32
_H323McStatsSuccessfullyCompletedConferences_Object = MibScalar
h323McStatsSuccessfullyCompletedConferences = _H323McStatsSuccessfullyCompletedConferences_Object(
    (0, 0, 8, 341, 1, 1, 4, 4, 2),
    _H323McStatsSuccessfullyCompletedConferences_Type()
)
h323McStatsSuccessfullyCompletedConferences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McStatsSuccessfullyCompletedConferences.setStatus("current")
_H323McStatsAbnormalyTerminatedConferences_Type = Integer32
_H323McStatsAbnormalyTerminatedConferences_Object = MibScalar
h323McStatsAbnormalyTerminatedConferences = _H323McStatsAbnormalyTerminatedConferences_Object(
    (0, 0, 8, 341, 1, 1, 4, 4, 3),
    _H323McStatsAbnormalyTerminatedConferences_Type()
)
h323McStatsAbnormalyTerminatedConferences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323McStatsAbnormalyTerminatedConferences.setStatus("current")
_H323McControls_ObjectIdentity = ObjectIdentity
h323McControls = _H323McControls_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 4, 5)
)


class _H323McControlsCommands_Type(Integer32):
    """Custom type h323McControlsCommands based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("abruptRestart", 2),
          ("abruptShutdown", 4),
          ("enterQuiescence", 6),
          ("exitQuiescence", 7),
          ("gracefulRestart", 3),
          ("gracefulShutdown", 5),
          ("other", 1),
          ("resetStatistics", 10),
          ("runDiagnostic", 11),
          ("startLog", 8),
          ("stopLog", 9))
    )


_H323McControlsCommands_Type.__name__ = "Integer32"
_H323McControlsCommands_Object = MibScalar
h323McControlsCommands = _H323McControlsCommands_Object(
    (0, 0, 8, 341, 1, 1, 4, 5, 1),
    _H323McControlsCommands_Type()
)
h323McControlsCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323McControlsCommands.setStatus("current")
_H323McEvents_ObjectIdentity = ObjectIdentity
h323McEvents = _H323McEvents_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 4, 6, 0)
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
    (0, 0, 8, 341, 1, 1, 4, 6, 0, 1),
    _LastConferenceTerminationReason_Type()
)
lastConferenceTerminationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConferenceTerminationReason.setStatus("current")
_LastTerminatedConferenceId_Type = MmGlobalIdentifier
_LastTerminatedConferenceId_Object = MibScalar
lastTerminatedConferenceId = _LastTerminatedConferenceId_Object(
    (0, 0, 8, 341, 1, 1, 4, 6, 0, 2),
    _LastTerminatedConferenceId_Type()
)
lastTerminatedConferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastTerminatedConferenceId.setStatus("current")
_H323McMIBConformance_ObjectIdentity = ObjectIdentity
h323McMIBConformance = _H323McMIBConformance_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 4, 7)
)
_H323McMIBGroups_ObjectIdentity = ObjectIdentity
h323McMIBGroups = _H323McMIBGroups_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 4, 7, 1)
)

# Managed Objects groups

h323McSystemGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 4, 7, 1, 1)
)
h323McSystemGroup.setObjects(
      *(("H323MC-MIB", "h323McSystemNameAndMaker"),
        ("H323MC-MIB", "h323McSystemSoftwareVersionNumber"),
        ("H323MC-MIB", "h323McSystemHardwareVersionNumber"),
        ("H323MC-MIB", "h323McSystemStartUpTime"))
)
if mibBuilder.loadTexts:
    h323McSystemGroup.setStatus("current")

h323McConfigGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 4, 7, 1, 2)
)
h323McConfigGroup.setObjects(
      *(("H323MC-MIB", "h323McConfigMcCallSignalingTag"),
        ("H323MC-MIB", "h323McConfigMcCallSignalingAddress"),
        ("H323MC-MIB", "h323McConfigGatekeeperAddressTag"),
        ("H323MC-MIB", "h323McConfigGatekeeperAddress"),
        ("H323MC-MIB", "h323McConfigIsRegisteredWithGatekeeper"),
        ("H323MC-MIB", "h323McConfigEnableNotifications"))
)
if mibBuilder.loadTexts:
    h323McConfigGroup.setStatus("current")

h323McConferenceGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 4, 7, 1, 3)
)
h323McConferenceGroup.setObjects(
      *(("H323MC-MIB", "h323McConferenceConferenceId"),
        ("H323MC-MIB", "h323McConferenceConferenceStartTime"),
        ("H323MC-MIB", "h323McConferenceConferenceEndTime"),
        ("H323MC-MIB", "h323McConferenceCentralizedOrDistributed"),
        ("H323MC-MIB", "h323McConferenceUniOrMulticast"),
        ("H323MC-MIB", "h323McConferenceActiveMcAddress"),
        ("H323MC-MIB", "h323McConferenceParticipantsTerminalLabel"),
        ("H323MC-MIB", "h323McConferenceParticipantsCallSignalingTAddressTag"),
        ("H323MC-MIB", "h323McConferenceParticipantsCallSignalingAddress"),
        ("H323MC-MIB", "h323McConferenceParticipantsCallId"),
        ("H323MC-MIB", "h323McConferenceParticipantsControlChannelIndex"),
        ("H323MC-MIB", "h323McConferenceParticipantsNumberOfLogicalChannels"),
        ("H323MC-MIB", "h323McConferenceParticipantsRtpSessionIndex"))
)
if mibBuilder.loadTexts:
    h323McConferenceGroup.setStatus("current")

h323McStatsGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 4, 7, 1, 4)
)
h323McStatsGroup.setObjects(
      *(("H323MC-MIB", "h323McStatsTotalConferences"),
        ("H323MC-MIB", "h323McStatsSuccessfullyCompletedConferences"),
        ("H323MC-MIB", "h323McStatsAbnormalyTerminatedConferences"))
)
if mibBuilder.loadTexts:
    h323McStatsGroup.setStatus("current")

h323McControlsGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 4, 7, 1, 5)
)
h323McControlsGroup.setObjects(
    ("H323MC-MIB", "h323McControlsCommands")
)
if mibBuilder.loadTexts:
    h323McControlsGroup.setStatus("current")


# Notification objects

conferenceTermination = NotificationType(
    (0, 0, 8, 341, 1, 1, 4, 6, 0, 3)
)
conferenceTermination.setObjects(
      *(("H323MC-MIB", "lastTerminatedConferenceId"),
        ("H323MC-MIB", "lastConferenceTerminationReason"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    conferenceTermination.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

h323McMIBCompliance = ModuleCompliance(
    (0, 0, 8, 341, 1, 1, 4, 7, 2)
)
if mibBuilder.loadTexts:
    h323McMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H323MC-MIB",
    **{"h323MC": h323MC,
       "h323McSystem": h323McSystem,
       "h323McSystemTable": h323McSystemTable,
       "h323McSystemTableEntry": h323McSystemTableEntry,
       "h323McSystemNameAndMaker": h323McSystemNameAndMaker,
       "h323McSystemSoftwareVersionNumber": h323McSystemSoftwareVersionNumber,
       "h323McSystemHardwareVersionNumber": h323McSystemHardwareVersionNumber,
       "h323McSystemStartUpTime": h323McSystemStartUpTime,
       "h323McConfig": h323McConfig,
       "h323McConfigTable": h323McConfigTable,
       "h323McConfigTableEntry": h323McConfigTableEntry,
       "h323McConfigMcCallSignalingTag": h323McConfigMcCallSignalingTag,
       "h323McConfigMcCallSignalingAddress": h323McConfigMcCallSignalingAddress,
       "h323McConfigGatekeeperAddressTag": h323McConfigGatekeeperAddressTag,
       "h323McConfigGatekeeperAddress": h323McConfigGatekeeperAddress,
       "h323McConfigIsRegisteredWithGatekeeper": h323McConfigIsRegisteredWithGatekeeper,
       "h323McConfigEnableNotifications": h323McConfigEnableNotifications,
       "h323McConference": h323McConference,
       "h323McConferenceTable": h323McConferenceTable,
       "h323McConferenceTableEntry": h323McConferenceTableEntry,
       "h323McConferenceConferenceId": h323McConferenceConferenceId,
       "h323McConferenceConferenceStartTime": h323McConferenceConferenceStartTime,
       "h323McConferenceConferenceEndTime": h323McConferenceConferenceEndTime,
       "h323McConferenceCentralizedOrDistributed": h323McConferenceCentralizedOrDistributed,
       "h323McConferenceUniOrMulticast": h323McConferenceUniOrMulticast,
       "h323McConferenceActiveMcAddress": h323McConferenceActiveMcAddress,
       "h323McConferenceParticipantsTable": h323McConferenceParticipantsTable,
       "h323McConferenceParticipantsTableEntry": h323McConferenceParticipantsTableEntry,
       "h323McConferenceParticipantsTableIndex": h323McConferenceParticipantsTableIndex,
       "h323McConferenceParticipantsTerminalLabel": h323McConferenceParticipantsTerminalLabel,
       "h323McConferenceParticipantsCallSignalingTAddressTag": h323McConferenceParticipantsCallSignalingTAddressTag,
       "h323McConferenceParticipantsCallSignalingAddress": h323McConferenceParticipantsCallSignalingAddress,
       "h323McConferenceParticipantsCallId": h323McConferenceParticipantsCallId,
       "h323McConferenceParticipantsControlChannelIndex": h323McConferenceParticipantsControlChannelIndex,
       "h323McConferenceParticipantsNumberOfLogicalChannels": h323McConferenceParticipantsNumberOfLogicalChannels,
       "h323McConferenceParticipantsRtpSessionIndex": h323McConferenceParticipantsRtpSessionIndex,
       "h323McStats": h323McStats,
       "h323McStatsTotalConferences": h323McStatsTotalConferences,
       "h323McStatsSuccessfullyCompletedConferences": h323McStatsSuccessfullyCompletedConferences,
       "h323McStatsAbnormalyTerminatedConferences": h323McStatsAbnormalyTerminatedConferences,
       "h323McControls": h323McControls,
       "h323McControlsCommands": h323McControlsCommands,
       "h323McEvents": h323McEvents,
       "lastConferenceTerminationReason": lastConferenceTerminationReason,
       "lastTerminatedConferenceId": lastTerminatedConferenceId,
       "conferenceTermination": conferenceTermination,
       "h323McMIBConformance": h323McMIBConformance,
       "h323McMIBGroups": h323McMIBGroups,
       "h323McSystemGroup": h323McSystemGroup,
       "h323McConfigGroup": h323McConfigGroup,
       "h323McConferenceGroup": h323McConferenceGroup,
       "h323McStatsGroup": h323McStatsGroup,
       "h323McControlsGroup": h323McControlsGroup,
       "h323McMIBCompliance": h323McMIBCompliance}
)
