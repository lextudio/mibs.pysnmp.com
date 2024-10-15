# SNMP MIB module (ZHONE-COM-VOICE-DSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-VOICE-DSP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:24 2024
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

(zhoneModules,
 zhoneShelfIndex,
 zhoneSlotIndex,
 zhoneVoice) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneModules",
    "zhoneShelfIndex",
    "zhoneSlotIndex",
    "zhoneVoice")

(ZhoneShelfValue,
 ZhoneSlotValue) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneShelfValue",
    "ZhoneSlotValue")


# MODULE-IDENTITY

comVoiceDsp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 12)
)
comVoiceDsp.setRevisions(
        ("2003-03-28 10:42",
         "2003-02-13 19:35",
         "2001-10-02 18:34",
         "2000-11-28 13:56",
         "2000-09-20 18:42")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneVoiceDsp_ObjectIdentity = ObjectIdentity
zhoneVoiceDsp = _ZhoneVoiceDsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3)
)
if mibBuilder.loadTexts:
    zhoneVoiceDsp.setStatus("current")
_VoiceDspDefaultConfiguration_ObjectIdentity = ObjectIdentity
voiceDspDefaultConfiguration = _VoiceDspDefaultConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 1)
)
if mibBuilder.loadTexts:
    voiceDspDefaultConfiguration.setStatus("current")


class _RedundancyOverSubscriptionType_Type(Integer32):
    """Custom type redundancyOverSubscriptionType based on Integer32"""
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
        *(("high", 4),
          ("low", 2),
          ("medium", 3),
          ("none", 1))
    )


_RedundancyOverSubscriptionType_Type.__name__ = "Integer32"
_RedundancyOverSubscriptionType_Object = MibScalar
redundancyOverSubscriptionType = _RedundancyOverSubscriptionType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 1, 1),
    _RedundancyOverSubscriptionType_Type()
)
redundancyOverSubscriptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyOverSubscriptionType.setStatus("current")


class _JitterBufferType_Type(Integer32):
    """Custom type jitterBufferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_JitterBufferType_Type.__name__ = "Integer32"
_JitterBufferType_Object = MibScalar
jitterBufferType = _JitterBufferType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 1, 2),
    _JitterBufferType_Type()
)
jitterBufferType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jitterBufferType.setStatus("current")


class _JitterBufferSize_Type(Unsigned32):
    """Custom type jitterBufferSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_JitterBufferSize_Type.__name__ = "Unsigned32"
_JitterBufferSize_Object = MibScalar
jitterBufferSize = _JitterBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 1, 3),
    _JitterBufferSize_Type()
)
jitterBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jitterBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    jitterBufferSize.setUnits("milliseconds")


class _InterArrvJitThreshold_Type(Unsigned32):
    """Custom type interArrvJitThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_InterArrvJitThreshold_Type.__name__ = "Unsigned32"
_InterArrvJitThreshold_Object = MibScalar
interArrvJitThreshold = _InterArrvJitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 1, 4),
    _InterArrvJitThreshold_Type()
)
interArrvJitThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interArrvJitThreshold.setStatus("current")
if mibBuilder.loadTexts:
    interArrvJitThreshold.setUnits("milliseconds")


class _PktsLostThreshold_Type(Unsigned32):
    """Custom type pktsLostThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_PktsLostThreshold_Type.__name__ = "Unsigned32"
_PktsLostThreshold_Object = MibScalar
pktsLostThreshold = _PktsLostThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 1, 5),
    _PktsLostThreshold_Type()
)
pktsLostThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktsLostThreshold.setStatus("current")


class _EchoCancellationType_Type(Integer32):
    """Custom type echoCancellationType based on Integer32"""
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
        *(("g165EchoTL16", 2),
          ("g165EchoTL32", 3),
          ("g165EchoTL48", 4),
          ("g168EchoTL112", 10),
          ("g168EchoTL128", 11),
          ("g168EchoTL32", 5),
          ("g168EchoTL48", 6),
          ("g168EchoTL64", 7),
          ("g168EchoTL80", 8),
          ("g168EchoTL96", 9),
          ("off", 1))
    )


_EchoCancellationType_Type.__name__ = "Integer32"
_EchoCancellationType_Object = MibScalar
echoCancellationType = _EchoCancellationType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 1, 6),
    _EchoCancellationType_Type()
)
echoCancellationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoCancellationType.setStatus("current")


class _SilenceSuppressionType_Type(Integer32):
    """Custom type silenceSuppressionType based on Integer32"""
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
        *(("silSupOff", 1),
          ("silSupOnSidConst", 4),
          ("silSupOnSidOff", 2),
          ("silSupOnSidOn", 3))
    )


_SilenceSuppressionType_Type.__name__ = "Integer32"
_SilenceSuppressionType_Object = MibScalar
silenceSuppressionType = _SilenceSuppressionType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 1, 7),
    _SilenceSuppressionType_Type()
)
silenceSuppressionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    silenceSuppressionType.setStatus("current")


class _EchoReturnLoss_Type(Integer32):
    """Custom type echoReturnLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("erl0dB", 1),
          ("erl3dB", 2),
          ("erl6dB", 3))
    )


_EchoReturnLoss_Type.__name__ = "Integer32"
_EchoReturnLoss_Object = MibScalar
echoReturnLoss = _EchoReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 1, 8),
    _EchoReturnLoss_Type()
)
echoReturnLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoReturnLoss.setStatus("current")
_VoiceDspStatusTable_Object = MibTable
voiceDspStatusTable = _VoiceDspStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 2)
)
if mibBuilder.loadTexts:
    voiceDspStatusTable.setStatus("current")
_VoiceDspStatusEntry_Object = MibTableRow
voiceDspStatusEntry = _VoiceDspStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 2, 1)
)
voiceDspStatusEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
)
if mibBuilder.loadTexts:
    voiceDspStatusEntry.setStatus("current")


class _VoiceDspMaxChannelOnBoard_Type(Unsigned32):
    """Custom type voiceDspMaxChannelOnBoard based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1008),
    )


_VoiceDspMaxChannelOnBoard_Type.__name__ = "Unsigned32"
_VoiceDspMaxChannelOnBoard_Object = MibTableColumn
voiceDspMaxChannelOnBoard = _VoiceDspMaxChannelOnBoard_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 2, 1, 1),
    _VoiceDspMaxChannelOnBoard_Type()
)
voiceDspMaxChannelOnBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceDspMaxChannelOnBoard.setStatus("current")


class _VoiceDspActiveChannelCount_Type(Unsigned32):
    """Custom type voiceDspActiveChannelCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1008),
    )


_VoiceDspActiveChannelCount_Type.__name__ = "Unsigned32"
_VoiceDspActiveChannelCount_Object = MibTableColumn
voiceDspActiveChannelCount = _VoiceDspActiveChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 2, 1, 2),
    _VoiceDspActiveChannelCount_Type()
)
voiceDspActiveChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceDspActiveChannelCount.setStatus("current")


class _VoiceDspHiWaterChannelCount_Type(Unsigned32):
    """Custom type voiceDspHiWaterChannelCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1008),
    )


_VoiceDspHiWaterChannelCount_Type.__name__ = "Unsigned32"
_VoiceDspHiWaterChannelCount_Object = MibTableColumn
voiceDspHiWaterChannelCount = _VoiceDspHiWaterChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 2, 1, 3),
    _VoiceDspHiWaterChannelCount_Type()
)
voiceDspHiWaterChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceDspHiWaterChannelCount.setStatus("current")
_VoiceDspResetCount_Type = Counter32
_VoiceDspResetCount_Object = MibTableColumn
voiceDspResetCount = _VoiceDspResetCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 2, 1, 4),
    _VoiceDspResetCount_Type()
)
voiceDspResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceDspResetCount.setStatus("current")
_ChannelStatusTable_Object = MibTable
channelStatusTable = _ChannelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3)
)
if mibBuilder.loadTexts:
    channelStatusTable.setStatus("current")
_ChannelStatusEntry_Object = MibTableRow
channelStatusEntry = _ChannelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1)
)
channelStatusEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
    (0, "ZHONE-COM-VOICE-DSP-MIB", "channelId"),
)
if mibBuilder.loadTexts:
    channelStatusEntry.setStatus("current")


class _ChannelId_Type(Integer32):
    """Custom type channelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_ChannelId_Type.__name__ = "Integer32"
_ChannelId_Object = MibTableColumn
channelId = _ChannelId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 1),
    _ChannelId_Type()
)
channelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelId.setStatus("current")
_ChannelVoiceSessionIdHigh_Type = Unsigned32
_ChannelVoiceSessionIdHigh_Object = MibTableColumn
channelVoiceSessionIdHigh = _ChannelVoiceSessionIdHigh_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 2),
    _ChannelVoiceSessionIdHigh_Type()
)
channelVoiceSessionIdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelVoiceSessionIdHigh.setStatus("current")
_ChannelVoiceSessionIdLow_Type = Unsigned32
_ChannelVoiceSessionIdLow_Object = MibTableColumn
channelVoiceSessionIdLow = _ChannelVoiceSessionIdLow_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 3),
    _ChannelVoiceSessionIdLow_Type()
)
channelVoiceSessionIdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelVoiceSessionIdLow.setStatus("current")
_ChannelCcrpShelf_Type = ZhoneShelfValue
_ChannelCcrpShelf_Object = MibTableColumn
channelCcrpShelf = _ChannelCcrpShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 4),
    _ChannelCcrpShelf_Type()
)
channelCcrpShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCcrpShelf.setStatus("current")
_ChannelCcrpSlot_Type = ZhoneSlotValue
_ChannelCcrpSlot_Object = MibTableColumn
channelCcrpSlot = _ChannelCcrpSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 5),
    _ChannelCcrpSlot_Type()
)
channelCcrpSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCcrpSlot.setStatus("current")
_ChannelTrunkCtrpShelf_Type = ZhoneShelfValue
_ChannelTrunkCtrpShelf_Object = MibTableColumn
channelTrunkCtrpShelf = _ChannelTrunkCtrpShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 6),
    _ChannelTrunkCtrpShelf_Type()
)
channelTrunkCtrpShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelTrunkCtrpShelf.setStatus("current")
_ChannelTrunkCtrpSlot_Type = ZhoneSlotValue
_ChannelTrunkCtrpSlot_Object = MibTableColumn
channelTrunkCtrpSlot = _ChannelTrunkCtrpSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 7),
    _ChannelTrunkCtrpSlot_Type()
)
channelTrunkCtrpSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelTrunkCtrpSlot.setStatus("current")
_ChannelPktCtrpShelf_Type = ZhoneShelfValue
_ChannelPktCtrpShelf_Object = MibTableColumn
channelPktCtrpShelf = _ChannelPktCtrpShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 8),
    _ChannelPktCtrpShelf_Type()
)
channelPktCtrpShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelPktCtrpShelf.setStatus("current")
_ChannelPktCtrpSlot_Type = ZhoneSlotValue
_ChannelPktCtrpSlot_Object = MibTableColumn
channelPktCtrpSlot = _ChannelPktCtrpSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 9),
    _ChannelPktCtrpSlot_Type()
)
channelPktCtrpSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelPktCtrpSlot.setStatus("current")


class _ChannelActiveCodec_Type(Integer32):
    """Custom type channelActiveCodec based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("g711Alaw", 2),
          ("g711Ulaw", 1),
          ("g723R1AKBPS5Dot3", 9),
          ("g723R1AKBPS6Dot3", 10),
          ("g723R1KBPS5Dot3", 7),
          ("g723R1KBPS6Dot3", 8),
          ("g726", 3),
          ("g729A", 4),
          ("g729B", 5),
          ("g729E", 6))
    )


_ChannelActiveCodec_Type.__name__ = "Integer32"
_ChannelActiveCodec_Object = MibTableColumn
channelActiveCodec = _ChannelActiveCodec_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 10),
    _ChannelActiveCodec_Type()
)
channelActiveCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelActiveCodec.setStatus("current")
_ChannelTimeAlive_Type = TimeTicks
_ChannelTimeAlive_Object = MibTableColumn
channelTimeAlive = _ChannelTimeAlive_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 11),
    _ChannelTimeAlive_Type()
)
channelTimeAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelTimeAlive.setStatus("current")
_ChannelPktsSent_Type = Counter32
_ChannelPktsSent_Object = MibTableColumn
channelPktsSent = _ChannelPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 12),
    _ChannelPktsSent_Type()
)
channelPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelPktsSent.setStatus("current")
_ChannelBytesSent_Type = Counter32
_ChannelBytesSent_Object = MibTableColumn
channelBytesSent = _ChannelBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 13),
    _ChannelBytesSent_Type()
)
channelBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelBytesSent.setStatus("current")
_ChannelPktsReceived_Type = Counter32
_ChannelPktsReceived_Object = MibTableColumn
channelPktsReceived = _ChannelPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 14),
    _ChannelPktsReceived_Type()
)
channelPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelPktsReceived.setStatus("current")
_ChannelBytesReceived_Type = Counter32
_ChannelBytesReceived_Object = MibTableColumn
channelBytesReceived = _ChannelBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 15),
    _ChannelBytesReceived_Type()
)
channelBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelBytesReceived.setStatus("current")
_ChannelPktsLost_Type = Counter32
_ChannelPktsLost_Object = MibTableColumn
channelPktsLost = _ChannelPktsLost_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 16),
    _ChannelPktsLost_Type()
)
channelPktsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelPktsLost.setStatus("current")
_ChannelInterArrvJitter_Type = Unsigned32
_ChannelInterArrvJitter_Object = MibTableColumn
channelInterArrvJitter = _ChannelInterArrvJitter_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 17),
    _ChannelInterArrvJitter_Type()
)
channelInterArrvJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInterArrvJitter.setStatus("current")
if mibBuilder.loadTexts:
    channelInterArrvJitter.setUnits("milliseconds")
_ChannelJitterBufferSize_Type = Unsigned32
_ChannelJitterBufferSize_Object = MibTableColumn
channelJitterBufferSize = _ChannelJitterBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 3, 1, 18),
    _ChannelJitterBufferSize_Type()
)
channelJitterBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelJitterBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    channelJitterBufferSize.setUnits("milliseconds")
_VoiceDspTraps_ObjectIdentity = ObjectIdentity
voiceDspTraps = _VoiceDspTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 4)
)
if mibBuilder.loadTexts:
    voiceDspTraps.setStatus("current")
_VoiceDspTrapsPrefix_ObjectIdentity = ObjectIdentity
voiceDspTrapsPrefix = _VoiceDspTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 4, 0)
)
if mibBuilder.loadTexts:
    voiceDspTrapsPrefix.setStatus("current")

# Managed Objects groups


# Notification objects

voiceDspReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 4, 0, 1)
)
voiceDspReset.setObjects(
      *(("Zhone", "zhoneShelfIndex"),
        ("Zhone", "zhoneSlotIndex"),
        ("ZHONE-COM-VOICE-DSP-MIB", "voiceDspResetCount"))
)
if mibBuilder.loadTexts:
    voiceDspReset.setStatus(
        "current"
    )

voiceDspChannelPktsLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 4, 0, 2)
)
voiceDspChannelPktsLoss.setObjects(
      *(("Zhone", "zhoneShelfIndex"),
        ("Zhone", "zhoneSlotIndex"),
        ("ZHONE-COM-VOICE-DSP-MIB", "channelId"),
        ("ZHONE-COM-VOICE-DSP-MIB", "channelPktsLost"))
)
if mibBuilder.loadTexts:
    voiceDspChannelPktsLoss.setStatus(
        "current"
    )

voiceDspChannelInterArrvJitterTrigger = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 3, 4, 0, 3)
)
voiceDspChannelInterArrvJitterTrigger.setObjects(
      *(("Zhone", "zhoneShelfIndex"),
        ("Zhone", "zhoneSlotIndex"),
        ("ZHONE-COM-VOICE-DSP-MIB", "channelId"),
        ("ZHONE-COM-VOICE-DSP-MIB", "channelInterArrvJitter"))
)
if mibBuilder.loadTexts:
    voiceDspChannelInterArrvJitterTrigger.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-VOICE-DSP-MIB",
    **{"zhoneVoiceDsp": zhoneVoiceDsp,
       "voiceDspDefaultConfiguration": voiceDspDefaultConfiguration,
       "redundancyOverSubscriptionType": redundancyOverSubscriptionType,
       "jitterBufferType": jitterBufferType,
       "jitterBufferSize": jitterBufferSize,
       "interArrvJitThreshold": interArrvJitThreshold,
       "pktsLostThreshold": pktsLostThreshold,
       "echoCancellationType": echoCancellationType,
       "silenceSuppressionType": silenceSuppressionType,
       "echoReturnLoss": echoReturnLoss,
       "voiceDspStatusTable": voiceDspStatusTable,
       "voiceDspStatusEntry": voiceDspStatusEntry,
       "voiceDspMaxChannelOnBoard": voiceDspMaxChannelOnBoard,
       "voiceDspActiveChannelCount": voiceDspActiveChannelCount,
       "voiceDspHiWaterChannelCount": voiceDspHiWaterChannelCount,
       "voiceDspResetCount": voiceDspResetCount,
       "channelStatusTable": channelStatusTable,
       "channelStatusEntry": channelStatusEntry,
       "channelId": channelId,
       "channelVoiceSessionIdHigh": channelVoiceSessionIdHigh,
       "channelVoiceSessionIdLow": channelVoiceSessionIdLow,
       "channelCcrpShelf": channelCcrpShelf,
       "channelCcrpSlot": channelCcrpSlot,
       "channelTrunkCtrpShelf": channelTrunkCtrpShelf,
       "channelTrunkCtrpSlot": channelTrunkCtrpSlot,
       "channelPktCtrpShelf": channelPktCtrpShelf,
       "channelPktCtrpSlot": channelPktCtrpSlot,
       "channelActiveCodec": channelActiveCodec,
       "channelTimeAlive": channelTimeAlive,
       "channelPktsSent": channelPktsSent,
       "channelBytesSent": channelBytesSent,
       "channelPktsReceived": channelPktsReceived,
       "channelBytesReceived": channelBytesReceived,
       "channelPktsLost": channelPktsLost,
       "channelInterArrvJitter": channelInterArrvJitter,
       "channelJitterBufferSize": channelJitterBufferSize,
       "voiceDspTraps": voiceDspTraps,
       "voiceDspTrapsPrefix": voiceDspTrapsPrefix,
       "voiceDspReset": voiceDspReset,
       "voiceDspChannelPktsLoss": voiceDspChannelPktsLoss,
       "voiceDspChannelInterArrvJitterTrigger": voiceDspChannelInterArrvJitterTrigger,
       "comVoiceDsp": comVoiceDsp}
)
