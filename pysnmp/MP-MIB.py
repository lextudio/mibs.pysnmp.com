# SNMP MIB module (MP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:48 2024
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

h323MP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Media_ObjectIdentity = ObjectIdentity
media = _Media_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3011, 2)
)
_MpConfig_ObjectIdentity = ObjectIdentity
mpConfig = _MpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 1)
)
_MpConfigMaxAudioMixCount_Type = Integer32
_MpConfigMaxAudioMixCount_Object = MibScalar
mpConfigMaxAudioMixCount = _MpConfigMaxAudioMixCount_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 1, 1),
    _MpConfigMaxAudioMixCount_Type()
)
mpConfigMaxAudioMixCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConfigMaxAudioMixCount.setStatus("current")
_MpConfigMaxVideoMixCount_Type = Integer32
_MpConfigMaxVideoMixCount_Object = MibScalar
mpConfigMaxVideoMixCount = _MpConfigMaxVideoMixCount_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 1, 2),
    _MpConfigMaxVideoMixCount_Type()
)
mpConfigMaxVideoMixCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConfigMaxVideoMixCount.setStatus("current")
_MpConference_ObjectIdentity = ObjectIdentity
mpConference = _MpConference_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2)
)
_MpConferenceTable_Object = MibTable
mpConferenceTable = _MpConferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mpConferenceTable.setStatus("current")
_MpConferenceTableEntry_Object = MibTableRow
mpConferenceTableEntry = _MpConferenceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1, 1)
)
mpConferenceTableEntry.setIndexNames(
    (0, "MP-MIB", "mpConferenceConferenceId"),
)
if mibBuilder.loadTexts:
    mpConferenceTableEntry.setStatus("current")
_MpConferenceConferenceId_Type = MmGlobalIdentifier
_MpConferenceConferenceId_Object = MibTableColumn
mpConferenceConferenceId = _MpConferenceConferenceId_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1, 1, 1),
    _MpConferenceConferenceId_Type()
)
mpConferenceConferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceConferenceId.setStatus("current")
_MpConferenceAudioNoiseThreshold_Type = Integer32
_MpConferenceAudioNoiseThreshold_Object = MibTableColumn
mpConferenceAudioNoiseThreshold = _MpConferenceAudioNoiseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1, 1, 2),
    _MpConferenceAudioNoiseThreshold_Type()
)
mpConferenceAudioNoiseThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceAudioNoiseThreshold.setStatus("current")
_MpConferenceLipSyncEnable_Type = TruthValue
_MpConferenceLipSyncEnable_Object = MibTableColumn
mpConferenceLipSyncEnable = _MpConferenceLipSyncEnable_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1, 1, 3),
    _MpConferenceLipSyncEnable_Type()
)
mpConferenceLipSyncEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceLipSyncEnable.setStatus("current")
_MpConferenceParticipantsTable_Object = MibTable
mpConferenceParticipantsTable = _MpConferenceParticipantsTable_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    mpConferenceParticipantsTable.setStatus("current")
_MpConferenceParticipantsTableEntry_Object = MibTableRow
mpConferenceParticipantsTableEntry = _MpConferenceParticipantsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1)
)
mpConferenceParticipantsTableEntry.setIndexNames(
    (0, "MP-MIB", "mpConferenceConferenceId"),
    (0, "MP-MIB", "mpConferenceParticipantsTableIndex"),
)
if mibBuilder.loadTexts:
    mpConferenceParticipantsTableEntry.setStatus("current")
_MpConferenceParticipantsTableIndex_Type = Integer32
_MpConferenceParticipantsTableIndex_Object = MibTableColumn
mpConferenceParticipantsTableIndex = _MpConferenceParticipantsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 1),
    _MpConferenceParticipantsTableIndex_Type()
)
mpConferenceParticipantsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsTableIndex.setStatus("current")
_MpConferenceParticipantsEndpointId_Type = MmEndpointID
_MpConferenceParticipantsEndpointId_Object = MibTableColumn
mpConferenceParticipantsEndpointId = _MpConferenceParticipantsEndpointId_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 2),
    _MpConferenceParticipantsEndpointId_Type()
)
mpConferenceParticipantsEndpointId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsEndpointId.setStatus("current")


class _MpConferenceParticipantsTransmitAudioState_Type(Integer32):
    """Custom type mpConferenceParticipantsTransmitAudioState based on Integer32"""
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
        *(("mute", 2),
          ("normal", 1),
          ("off", 4),
          ("toneGeneration", 3))
    )


_MpConferenceParticipantsTransmitAudioState_Type.__name__ = "Integer32"
_MpConferenceParticipantsTransmitAudioState_Object = MibTableColumn
mpConferenceParticipantsTransmitAudioState = _MpConferenceParticipantsTransmitAudioState_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 3),
    _MpConferenceParticipantsTransmitAudioState_Type()
)
mpConferenceParticipantsTransmitAudioState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsTransmitAudioState.setStatus("current")


class _MpConferenceParticipantsReceiveAudioState_Type(Integer32):
    """Custom type mpConferenceParticipantsReceiveAudioState based on Integer32"""
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
        *(("block", 3),
          ("loopBack", 2),
          ("normal", 1),
          ("off", 4))
    )


_MpConferenceParticipantsReceiveAudioState_Type.__name__ = "Integer32"
_MpConferenceParticipantsReceiveAudioState_Object = MibTableColumn
mpConferenceParticipantsReceiveAudioState = _MpConferenceParticipantsReceiveAudioState_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 4),
    _MpConferenceParticipantsReceiveAudioState_Type()
)
mpConferenceParticipantsReceiveAudioState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsReceiveAudioState.setStatus("current")


class _MpConferenceParticipantsTransmitVideoState_Type(Integer32):
    """Custom type mpConferenceParticipantsTransmitVideoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_MpConferenceParticipantsTransmitVideoState_Type.__name__ = "Integer32"
_MpConferenceParticipantsTransmitVideoState_Object = MibTableColumn
mpConferenceParticipantsTransmitVideoState = _MpConferenceParticipantsTransmitVideoState_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 5),
    _MpConferenceParticipantsTransmitVideoState_Type()
)
mpConferenceParticipantsTransmitVideoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsTransmitVideoState.setStatus("current")


class _MpConferenceParticipantsReceiveVideoState_Type(Integer32):
    """Custom type mpConferenceParticipantsReceiveVideoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("normal", 1),
          ("off", 3))
    )


_MpConferenceParticipantsReceiveVideoState_Type.__name__ = "Integer32"
_MpConferenceParticipantsReceiveVideoState_Object = MibTableColumn
mpConferenceParticipantsReceiveVideoState = _MpConferenceParticipantsReceiveVideoState_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 6),
    _MpConferenceParticipantsReceiveVideoState_Type()
)
mpConferenceParticipantsReceiveVideoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsReceiveVideoState.setStatus("current")
_MpConferenceParticipantsLoudnessMeasurement_Type = Integer32
_MpConferenceParticipantsLoudnessMeasurement_Object = MibTableColumn
mpConferenceParticipantsLoudnessMeasurement = _MpConferenceParticipantsLoudnessMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 7),
    _MpConferenceParticipantsLoudnessMeasurement_Type()
)
mpConferenceParticipantsLoudnessMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsLoudnessMeasurement.setStatus("current")
_MpConferenceParticipantsVoiceActivity_Type = TruthValue
_MpConferenceParticipantsVoiceActivity_Object = MibTableColumn
mpConferenceParticipantsVoiceActivity = _MpConferenceParticipantsVoiceActivity_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 8),
    _MpConferenceParticipantsVoiceActivity_Type()
)
mpConferenceParticipantsVoiceActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsVoiceActivity.setStatus("current")
_MpConferenceParticipantsInputAudioGain_Type = Integer32
_MpConferenceParticipantsInputAudioGain_Object = MibTableColumn
mpConferenceParticipantsInputAudioGain = _MpConferenceParticipantsInputAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 9),
    _MpConferenceParticipantsInputAudioGain_Type()
)
mpConferenceParticipantsInputAudioGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsInputAudioGain.setStatus("current")
_MpConferenceParticipantsOutputAudioGain_Type = Integer32
_MpConferenceParticipantsOutputAudioGain_Object = MibTableColumn
mpConferenceParticipantsOutputAudioGain = _MpConferenceParticipantsOutputAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 10),
    _MpConferenceParticipantsOutputAudioGain_Type()
)
mpConferenceParticipantsOutputAudioGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsOutputAudioGain.setStatus("current")
_MpConferenceParticipantsMaxAudioEncoderPayloadSize_Type = Integer32
_MpConferenceParticipantsMaxAudioEncoderPayloadSize_Object = MibTableColumn
mpConferenceParticipantsMaxAudioEncoderPayloadSize = _MpConferenceParticipantsMaxAudioEncoderPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 11),
    _MpConferenceParticipantsMaxAudioEncoderPayloadSize_Type()
)
mpConferenceParticipantsMaxAudioEncoderPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsMaxAudioEncoderPayloadSize.setStatus("current")
_MpConferenceParticipantsMaxAudioDecoderPayloadSize_Type = Integer32
_MpConferenceParticipantsMaxAudioDecoderPayloadSize_Object = MibTableColumn
mpConferenceParticipantsMaxAudioDecoderPayloadSize = _MpConferenceParticipantsMaxAudioDecoderPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 12),
    _MpConferenceParticipantsMaxAudioDecoderPayloadSize_Type()
)
mpConferenceParticipantsMaxAudioDecoderPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsMaxAudioDecoderPayloadSize.setStatus("current")
_MpConferenceParticipantsTotalPacketsTransmitted_Type = Counter32
_MpConferenceParticipantsTotalPacketsTransmitted_Object = MibTableColumn
mpConferenceParticipantsTotalPacketsTransmitted = _MpConferenceParticipantsTotalPacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 13),
    _MpConferenceParticipantsTotalPacketsTransmitted_Type()
)
mpConferenceParticipantsTotalPacketsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsTotalPacketsTransmitted.setStatus("current")
_MpConferenceParticipantsTotalPacketsReceived_Type = Counter32
_MpConferenceParticipantsTotalPacketsReceived_Object = MibTableColumn
mpConferenceParticipantsTotalPacketsReceived = _MpConferenceParticipantsTotalPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 14),
    _MpConferenceParticipantsTotalPacketsReceived_Type()
)
mpConferenceParticipantsTotalPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsTotalPacketsReceived.setStatus("current")
_MpConferenceParticipantsInvalidPacketErrors_Type = Counter32
_MpConferenceParticipantsInvalidPacketErrors_Object = MibTableColumn
mpConferenceParticipantsInvalidPacketErrors = _MpConferenceParticipantsInvalidPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 15),
    _MpConferenceParticipantsInvalidPacketErrors_Type()
)
mpConferenceParticipantsInvalidPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsInvalidPacketErrors.setStatus("current")
_MpConferenceParticipantsLateAudioPacketsDropped_Type = Counter32
_MpConferenceParticipantsLateAudioPacketsDropped_Object = MibTableColumn
mpConferenceParticipantsLateAudioPacketsDropped = _MpConferenceParticipantsLateAudioPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 16),
    _MpConferenceParticipantsLateAudioPacketsDropped_Type()
)
mpConferenceParticipantsLateAudioPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsLateAudioPacketsDropped.setStatus("current")
_MpConferenceParticipantsReceivedSilencePackets_Type = Counter32
_MpConferenceParticipantsReceivedSilencePackets_Object = MibTableColumn
mpConferenceParticipantsReceivedSilencePackets = _MpConferenceParticipantsReceivedSilencePackets_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 17),
    _MpConferenceParticipantsReceivedSilencePackets_Type()
)
mpConferenceParticipantsReceivedSilencePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsReceivedSilencePackets.setStatus("current")
_MpConferenceParticipantsSilencePacketsGenerated_Type = Counter32
_MpConferenceParticipantsSilencePacketsGenerated_Object = MibTableColumn
mpConferenceParticipantsSilencePacketsGenerated = _MpConferenceParticipantsSilencePacketsGenerated_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 18),
    _MpConferenceParticipantsSilencePacketsGenerated_Type()
)
mpConferenceParticipantsSilencePacketsGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsSilencePacketsGenerated.setStatus("current")
_MpConferenceParticipantsVideoFrameRate_Type = Integer32
_MpConferenceParticipantsVideoFrameRate_Object = MibTableColumn
mpConferenceParticipantsVideoFrameRate = _MpConferenceParticipantsVideoFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 19),
    _MpConferenceParticipantsVideoFrameRate_Type()
)
mpConferenceParticipantsVideoFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsVideoFrameRate.setStatus("current")


class _MpConferenceParticipantsVideoResolution_Type(Integer32):
    """Custom type mpConferenceParticipantsVideoResolution based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("h261CIF", 8),
          ("h261QCIF", 7),
          ("h26316CIF", 5),
          ("h2634CIF", 4),
          ("h263CIF", 3),
          ("h263QCIF", 2),
          ("h263Reserved", 6),
          ("h263SubQCIF", 1))
    )


_MpConferenceParticipantsVideoResolution_Type.__name__ = "Integer32"
_MpConferenceParticipantsVideoResolution_Object = MibTableColumn
mpConferenceParticipantsVideoResolution = _MpConferenceParticipantsVideoResolution_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 20),
    _MpConferenceParticipantsVideoResolution_Type()
)
mpConferenceParticipantsVideoResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsVideoResolution.setStatus("current")
_MpConferenceParticipantsFullPictureCounter_Type = Integer32
_MpConferenceParticipantsFullPictureCounter_Object = MibTableColumn
mpConferenceParticipantsFullPictureCounter = _MpConferenceParticipantsFullPictureCounter_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 21),
    _MpConferenceParticipantsFullPictureCounter_Type()
)
mpConferenceParticipantsFullPictureCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceParticipantsFullPictureCounter.setStatus("current")
_MpConferenceGlobalAudioMixTable_Object = MibTable
mpConferenceGlobalAudioMixTable = _MpConferenceGlobalAudioMixTable_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    mpConferenceGlobalAudioMixTable.setStatus("current")
_MpConferenceGlobalAudioMixTableEntry_Object = MibTableRow
mpConferenceGlobalAudioMixTableEntry = _MpConferenceGlobalAudioMixTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 3, 1)
)
mpConferenceGlobalAudioMixTableEntry.setIndexNames(
    (0, "MP-MIB", "mpConferenceConferenceId"),
    (0, "MP-MIB", "mpConferenceGlobalAudioMixTableIndex"),
)
if mibBuilder.loadTexts:
    mpConferenceGlobalAudioMixTableEntry.setStatus("current")
_MpConferenceGlobalAudioMixTableIndex_Type = Integer32
_MpConferenceGlobalAudioMixTableIndex_Object = MibTableColumn
mpConferenceGlobalAudioMixTableIndex = _MpConferenceGlobalAudioMixTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 3, 1, 1),
    _MpConferenceGlobalAudioMixTableIndex_Type()
)
mpConferenceGlobalAudioMixTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceGlobalAudioMixTableIndex.setStatus("current")
_MpConferenceGlobalAudioMixTerminalIdentifier_Type = MmEndpointID
_MpConferenceGlobalAudioMixTerminalIdentifier_Object = MibTableColumn
mpConferenceGlobalAudioMixTerminalIdentifier = _MpConferenceGlobalAudioMixTerminalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 3, 1, 2),
    _MpConferenceGlobalAudioMixTerminalIdentifier_Type()
)
mpConferenceGlobalAudioMixTerminalIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceGlobalAudioMixTerminalIdentifier.setStatus("current")
_MpConferenceGlobalVideoMixTable_Object = MibTable
mpConferenceGlobalVideoMixTable = _MpConferenceGlobalVideoMixTable_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    mpConferenceGlobalVideoMixTable.setStatus("current")
_MpConferenceGlobalVideoMixTableEntry_Object = MibTableRow
mpConferenceGlobalVideoMixTableEntry = _MpConferenceGlobalVideoMixTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 4, 1)
)
mpConferenceGlobalVideoMixTableEntry.setIndexNames(
    (0, "MP-MIB", "mpConferenceConferenceId"),
    (0, "MP-MIB", "mpConferenceGlobalVideoMixTableIndex"),
)
if mibBuilder.loadTexts:
    mpConferenceGlobalVideoMixTableEntry.setStatus("current")
_MpConferenceGlobalVideoMixTableIndex_Type = Integer32
_MpConferenceGlobalVideoMixTableIndex_Object = MibTableColumn
mpConferenceGlobalVideoMixTableIndex = _MpConferenceGlobalVideoMixTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 4, 1, 1),
    _MpConferenceGlobalVideoMixTableIndex_Type()
)
mpConferenceGlobalVideoMixTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceGlobalVideoMixTableIndex.setStatus("current")
_MpConferenceGlobalVideoMixTerminalIdentifier_Type = MmEndpointID
_MpConferenceGlobalVideoMixTerminalIdentifier_Object = MibTableColumn
mpConferenceGlobalVideoMixTerminalIdentifier = _MpConferenceGlobalVideoMixTerminalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 4, 1, 2),
    _MpConferenceGlobalVideoMixTerminalIdentifier_Type()
)
mpConferenceGlobalVideoMixTerminalIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpConferenceGlobalVideoMixTerminalIdentifier.setStatus("current")
_MpMIBConformance_ObjectIdentity = ObjectIdentity
mpMIBConformance = _MpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 3)
)
_MpMIBGroups_ObjectIdentity = ObjectIdentity
mpMIBGroups = _MpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 3, 1)
)

# Managed Objects groups

mpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 3, 1, 1)
)
mpConfigGroup.setObjects(
      *(("MP-MIB", "mpConfigMaxAudioMixCount"),
        ("MP-MIB", "mpConfigMaxVideoMixCount"))
)
if mibBuilder.loadTexts:
    mpConfigGroup.setStatus("current")

mpConferenceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 3, 1, 2)
)
mpConferenceGroup.setObjects(
      *(("MP-MIB", "mpConferenceConferenceId"),
        ("MP-MIB", "mpConferenceAudioNoiseThreshold"),
        ("MP-MIB", "mpConferenceLipSyncEnable"),
        ("MP-MIB", "mpConferenceParticipantsTableIndex"),
        ("MP-MIB", "mpConferenceParticipantsEndpointId"),
        ("MP-MIB", "mpConferenceParticipantsTransmitAudioState"),
        ("MP-MIB", "mpConferenceParticipantsReceiveAudioState"),
        ("MP-MIB", "mpConferenceParticipantsTransmitVideoState"),
        ("MP-MIB", "mpConferenceParticipantsReceiveVideoState"),
        ("MP-MIB", "mpConferenceParticipantsLoudnessMeasurement"),
        ("MP-MIB", "mpConferenceParticipantsVoiceActivity"),
        ("MP-MIB", "mpConferenceParticipantsInputAudioGain"),
        ("MP-MIB", "mpConferenceParticipantsOutputAudioGain"),
        ("MP-MIB", "mpConferenceParticipantsMaxAudioEncoderPayloadSize"),
        ("MP-MIB", "mpConferenceParticipantsMaxAudioDecoderPayloadSize"),
        ("MP-MIB", "mpConferenceParticipantsTotalPacketsTransmitted"),
        ("MP-MIB", "mpConferenceParticipantsTotalPacketsReceived"),
        ("MP-MIB", "mpConferenceParticipantsLateAudioPacketsDropped"),
        ("MP-MIB", "mpConferenceParticipantsReceivedSilencePackets"),
        ("MP-MIB", "mpConferenceParticipantsSilencePacketsGenerated"),
        ("MP-MIB", "mpConferenceParticipantsVideoFrameRate"),
        ("MP-MIB", "mpConferenceParticipantsVideoResolution"),
        ("MP-MIB", "mpConferenceParticipantsFullPictureCounter"),
        ("MP-MIB", "mpConferenceGlobalAudioMixTableIndex"),
        ("MP-MIB", "mpConferenceGlobalAudioMixTerminalIdentifier"),
        ("MP-MIB", "mpConferenceGlobalVideoMixTableIndex"),
        ("MP-MIB", "mpConferenceGlobalVideoMixTerminalIdentifier"))
)
if mibBuilder.loadTexts:
    mpConferenceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3011, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    mpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MP-MIB",
    **{"media": media,
       "h323MP": h323MP,
       "mpConfig": mpConfig,
       "mpConfigMaxAudioMixCount": mpConfigMaxAudioMixCount,
       "mpConfigMaxVideoMixCount": mpConfigMaxVideoMixCount,
       "mpConference": mpConference,
       "mpConferenceTable": mpConferenceTable,
       "mpConferenceTableEntry": mpConferenceTableEntry,
       "mpConferenceConferenceId": mpConferenceConferenceId,
       "mpConferenceAudioNoiseThreshold": mpConferenceAudioNoiseThreshold,
       "mpConferenceLipSyncEnable": mpConferenceLipSyncEnable,
       "mpConferenceParticipantsTable": mpConferenceParticipantsTable,
       "mpConferenceParticipantsTableEntry": mpConferenceParticipantsTableEntry,
       "mpConferenceParticipantsTableIndex": mpConferenceParticipantsTableIndex,
       "mpConferenceParticipantsEndpointId": mpConferenceParticipantsEndpointId,
       "mpConferenceParticipantsTransmitAudioState": mpConferenceParticipantsTransmitAudioState,
       "mpConferenceParticipantsReceiveAudioState": mpConferenceParticipantsReceiveAudioState,
       "mpConferenceParticipantsTransmitVideoState": mpConferenceParticipantsTransmitVideoState,
       "mpConferenceParticipantsReceiveVideoState": mpConferenceParticipantsReceiveVideoState,
       "mpConferenceParticipantsLoudnessMeasurement": mpConferenceParticipantsLoudnessMeasurement,
       "mpConferenceParticipantsVoiceActivity": mpConferenceParticipantsVoiceActivity,
       "mpConferenceParticipantsInputAudioGain": mpConferenceParticipantsInputAudioGain,
       "mpConferenceParticipantsOutputAudioGain": mpConferenceParticipantsOutputAudioGain,
       "mpConferenceParticipantsMaxAudioEncoderPayloadSize": mpConferenceParticipantsMaxAudioEncoderPayloadSize,
       "mpConferenceParticipantsMaxAudioDecoderPayloadSize": mpConferenceParticipantsMaxAudioDecoderPayloadSize,
       "mpConferenceParticipantsTotalPacketsTransmitted": mpConferenceParticipantsTotalPacketsTransmitted,
       "mpConferenceParticipantsTotalPacketsReceived": mpConferenceParticipantsTotalPacketsReceived,
       "mpConferenceParticipantsInvalidPacketErrors": mpConferenceParticipantsInvalidPacketErrors,
       "mpConferenceParticipantsLateAudioPacketsDropped": mpConferenceParticipantsLateAudioPacketsDropped,
       "mpConferenceParticipantsReceivedSilencePackets": mpConferenceParticipantsReceivedSilencePackets,
       "mpConferenceParticipantsSilencePacketsGenerated": mpConferenceParticipantsSilencePacketsGenerated,
       "mpConferenceParticipantsVideoFrameRate": mpConferenceParticipantsVideoFrameRate,
       "mpConferenceParticipantsVideoResolution": mpConferenceParticipantsVideoResolution,
       "mpConferenceParticipantsFullPictureCounter": mpConferenceParticipantsFullPictureCounter,
       "mpConferenceGlobalAudioMixTable": mpConferenceGlobalAudioMixTable,
       "mpConferenceGlobalAudioMixTableEntry": mpConferenceGlobalAudioMixTableEntry,
       "mpConferenceGlobalAudioMixTableIndex": mpConferenceGlobalAudioMixTableIndex,
       "mpConferenceGlobalAudioMixTerminalIdentifier": mpConferenceGlobalAudioMixTerminalIdentifier,
       "mpConferenceGlobalVideoMixTable": mpConferenceGlobalVideoMixTable,
       "mpConferenceGlobalVideoMixTableEntry": mpConferenceGlobalVideoMixTableEntry,
       "mpConferenceGlobalVideoMixTableIndex": mpConferenceGlobalVideoMixTableIndex,
       "mpConferenceGlobalVideoMixTerminalIdentifier": mpConferenceGlobalVideoMixTerminalIdentifier,
       "mpMIBConformance": mpMIBConformance,
       "mpMIBGroups": mpMIBGroups,
       "mpConfigGroup": mpConfigGroup,
       "mpConferenceGroup": mpConferenceGroup,
       "mpMIBCompliance": mpMIBCompliance}
)
