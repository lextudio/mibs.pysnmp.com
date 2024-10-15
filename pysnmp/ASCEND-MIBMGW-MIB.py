# SNMP MIB module (ASCEND-MIBMGW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBMGW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:55 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibmediaGatewayProfile_ObjectIdentity = ObjectIdentity
mibmediaGatewayProfile = _MibmediaGatewayProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 170)
)
_MibmediaGatewayProfileTable_Object = MibTable
mibmediaGatewayProfileTable = _MibmediaGatewayProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1)
)
if mibBuilder.loadTexts:
    mibmediaGatewayProfileTable.setStatus("mandatory")
_MibmediaGatewayProfileEntry_Object = MibTableRow
mibmediaGatewayProfileEntry = _MibmediaGatewayProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1)
)
mibmediaGatewayProfileEntry.setIndexNames(
    (0, "ASCEND-MIBMGW-MIB", "mediaGatewayProfile-Name"),
)
if mibBuilder.loadTexts:
    mibmediaGatewayProfileEntry.setStatus("mandatory")
_MediaGatewayProfile_Name_Type = DisplayString
_MediaGatewayProfile_Name_Object = MibScalar
mediaGatewayProfile_Name = _MediaGatewayProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 1),
    _MediaGatewayProfile_Name_Type()
)
mediaGatewayProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaGatewayProfile_Name.setStatus("mandatory")


class _MediaGatewayProfile_Active_Type(Integer32):
    """Custom type mediaGatewayProfile_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MediaGatewayProfile_Active_Type.__name__ = "Integer32"
_MediaGatewayProfile_Active_Object = MibScalar
mediaGatewayProfile_Active = _MediaGatewayProfile_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 2),
    _MediaGatewayProfile_Active_Type()
)
mediaGatewayProfile_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_Active.setStatus("mandatory")


class _MediaGatewayProfile_ProtocolType_Type(Integer32):
    """Custom type mediaGatewayProfile_ProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("h248", 1),
          ("sip", 3))
    )


_MediaGatewayProfile_ProtocolType_Type.__name__ = "Integer32"
_MediaGatewayProfile_ProtocolType_Object = MibScalar
mediaGatewayProfile_ProtocolType = _MediaGatewayProfile_ProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 3),
    _MediaGatewayProfile_ProtocolType_Type()
)
mediaGatewayProfile_ProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_ProtocolType.setStatus("mandatory")


class _MediaGatewayProfile_MgSigAddress_Type_Type(Integer32):
    """Custom type mediaGatewayProfile_MgSigAddress_Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interfaceDependent", 3),
          ("specific", 2),
          ("systemDefault", 1))
    )


_MediaGatewayProfile_MgSigAddress_Type_Type.__name__ = "Integer32"
_MediaGatewayProfile_MgSigAddress_Type_Object = MibScalar
mediaGatewayProfile_MgSigAddress_Type = _MediaGatewayProfile_MgSigAddress_Type_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 4),
    _MediaGatewayProfile_MgSigAddress_Type_Type()
)
mediaGatewayProfile_MgSigAddress_Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_MgSigAddress_Type.setStatus("mandatory")
_MediaGatewayProfile_MgSigAddress_IpAddress_Type = IpAddress
_MediaGatewayProfile_MgSigAddress_IpAddress_Object = MibScalar
mediaGatewayProfile_MgSigAddress_IpAddress = _MediaGatewayProfile_MgSigAddress_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 5),
    _MediaGatewayProfile_MgSigAddress_IpAddress_Type()
)
mediaGatewayProfile_MgSigAddress_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_MgSigAddress_IpAddress.setStatus("mandatory")


class _MediaGatewayProfile_MgRtpAddress_Type_Type(Integer32):
    """Custom type mediaGatewayProfile_MgRtpAddress_Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interfaceDependent", 3),
          ("specific", 2),
          ("systemDefault", 1))
    )


_MediaGatewayProfile_MgRtpAddress_Type_Type.__name__ = "Integer32"
_MediaGatewayProfile_MgRtpAddress_Type_Object = MibScalar
mediaGatewayProfile_MgRtpAddress_Type = _MediaGatewayProfile_MgRtpAddress_Type_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 6),
    _MediaGatewayProfile_MgRtpAddress_Type_Type()
)
mediaGatewayProfile_MgRtpAddress_Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_MgRtpAddress_Type.setStatus("mandatory")
_MediaGatewayProfile_MgRtpAddress_IpAddress_Type = IpAddress
_MediaGatewayProfile_MgRtpAddress_IpAddress_Object = MibScalar
mediaGatewayProfile_MgRtpAddress_IpAddress = _MediaGatewayProfile_MgRtpAddress_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 7),
    _MediaGatewayProfile_MgRtpAddress_IpAddress_Type()
)
mediaGatewayProfile_MgRtpAddress_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_MgRtpAddress_IpAddress.setStatus("mandatory")


class _MediaGatewayProfile_H248Options_EncodingFormat_Type(Integer32):
    """Custom type mediaGatewayProfile_H248Options_EncodingFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("binary", 2),
          ("text", 1))
    )


_MediaGatewayProfile_H248Options_EncodingFormat_Type.__name__ = "Integer32"
_MediaGatewayProfile_H248Options_EncodingFormat_Object = MibScalar
mediaGatewayProfile_H248Options_EncodingFormat = _MediaGatewayProfile_H248Options_EncodingFormat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 8),
    _MediaGatewayProfile_H248Options_EncodingFormat_Type()
)
mediaGatewayProfile_H248Options_EncodingFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_H248Options_EncodingFormat.setStatus("mandatory")
_MediaGatewayProfile_H248Options_MaxResponseTime_Type = Integer32
_MediaGatewayProfile_H248Options_MaxResponseTime_Object = MibScalar
mediaGatewayProfile_H248Options_MaxResponseTime = _MediaGatewayProfile_H248Options_MaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 9),
    _MediaGatewayProfile_H248Options_MaxResponseTime_Type()
)
mediaGatewayProfile_H248Options_MaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_H248Options_MaxResponseTime.setStatus("mandatory")


class _MediaGatewayProfile_H248Options_Heartbeat_Enabled_Type(Integer32):
    """Custom type mediaGatewayProfile_H248Options_Heartbeat_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MediaGatewayProfile_H248Options_Heartbeat_Enabled_Type.__name__ = "Integer32"
_MediaGatewayProfile_H248Options_Heartbeat_Enabled_Object = MibScalar
mediaGatewayProfile_H248Options_Heartbeat_Enabled = _MediaGatewayProfile_H248Options_Heartbeat_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 10),
    _MediaGatewayProfile_H248Options_Heartbeat_Enabled_Type()
)
mediaGatewayProfile_H248Options_Heartbeat_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_H248Options_Heartbeat_Enabled.setStatus("mandatory")
_MediaGatewayProfile_H248Options_Heartbeat_Interval_Type = Integer32
_MediaGatewayProfile_H248Options_Heartbeat_Interval_Object = MibScalar
mediaGatewayProfile_H248Options_Heartbeat_Interval = _MediaGatewayProfile_H248Options_Heartbeat_Interval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 11),
    _MediaGatewayProfile_H248Options_Heartbeat_Interval_Type()
)
mediaGatewayProfile_H248Options_Heartbeat_Interval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_H248Options_Heartbeat_Interval.setStatus("mandatory")
_MediaGatewayProfile_H248Options_DigitmapOptions_StartTimer_Type = Integer32
_MediaGatewayProfile_H248Options_DigitmapOptions_StartTimer_Object = MibScalar
mediaGatewayProfile_H248Options_DigitmapOptions_StartTimer = _MediaGatewayProfile_H248Options_DigitmapOptions_StartTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 12),
    _MediaGatewayProfile_H248Options_DigitmapOptions_StartTimer_Type()
)
mediaGatewayProfile_H248Options_DigitmapOptions_StartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_H248Options_DigitmapOptions_StartTimer.setStatus("mandatory")
_MediaGatewayProfile_H248Options_DigitmapOptions_ShortTimer_Type = Integer32
_MediaGatewayProfile_H248Options_DigitmapOptions_ShortTimer_Object = MibScalar
mediaGatewayProfile_H248Options_DigitmapOptions_ShortTimer = _MediaGatewayProfile_H248Options_DigitmapOptions_ShortTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 13),
    _MediaGatewayProfile_H248Options_DigitmapOptions_ShortTimer_Type()
)
mediaGatewayProfile_H248Options_DigitmapOptions_ShortTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_H248Options_DigitmapOptions_ShortTimer.setStatus("mandatory")
_MediaGatewayProfile_H248Options_DigitmapOptions_LongTimer_Type = Integer32
_MediaGatewayProfile_H248Options_DigitmapOptions_LongTimer_Object = MibScalar
mediaGatewayProfile_H248Options_DigitmapOptions_LongTimer = _MediaGatewayProfile_H248Options_DigitmapOptions_LongTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 14),
    _MediaGatewayProfile_H248Options_DigitmapOptions_LongTimer_Type()
)
mediaGatewayProfile_H248Options_DigitmapOptions_LongTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_H248Options_DigitmapOptions_LongTimer.setStatus("mandatory")
_MediaGatewayProfile_IpdcOptions_BayId_Type = DisplayString
_MediaGatewayProfile_IpdcOptions_BayId_Object = MibScalar
mediaGatewayProfile_IpdcOptions_BayId = _MediaGatewayProfile_IpdcOptions_BayId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 15),
    _MediaGatewayProfile_IpdcOptions_BayId_Type()
)
mediaGatewayProfile_IpdcOptions_BayId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_IpdcOptions_BayId.setStatus("mandatory")
_MediaGatewayProfile_IpdcOptions_SystemType_Type = DisplayString
_MediaGatewayProfile_IpdcOptions_SystemType_Object = MibScalar
mediaGatewayProfile_IpdcOptions_SystemType = _MediaGatewayProfile_IpdcOptions_SystemType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 16),
    _MediaGatewayProfile_IpdcOptions_SystemType_Type()
)
mediaGatewayProfile_IpdcOptions_SystemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_IpdcOptions_SystemType.setStatus("mandatory")


class _MediaGatewayProfile_TransportOptions_Type_Type(Integer32):
    """Custom type mediaGatewayProfile_TransportOptions_Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_MediaGatewayProfile_TransportOptions_Type_Type.__name__ = "Integer32"
_MediaGatewayProfile_TransportOptions_Type_Object = MibScalar
mediaGatewayProfile_TransportOptions_Type = _MediaGatewayProfile_TransportOptions_Type_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 17),
    _MediaGatewayProfile_TransportOptions_Type_Type()
)
mediaGatewayProfile_TransportOptions_Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_TransportOptions_Type.setStatus("mandatory")


class _MediaGatewayProfile_VoipOptions_PacketAudioMode_Type(Integer32):
    """Custom type mediaGatewayProfile_VoipOptions_PacketAudioMode based on Integer32"""
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
        *(("frgsm", 8),
          ("g711Alaw", 2),
          ("g711Ulaw", 1),
          ("g723", 3),
          ("g72364kps", 5),
          ("g728", 7),
          ("g729", 4),
          ("rt24", 6))
    )


_MediaGatewayProfile_VoipOptions_PacketAudioMode_Type.__name__ = "Integer32"
_MediaGatewayProfile_VoipOptions_PacketAudioMode_Object = MibScalar
mediaGatewayProfile_VoipOptions_PacketAudioMode = _MediaGatewayProfile_VoipOptions_PacketAudioMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 18),
    _MediaGatewayProfile_VoipOptions_PacketAudioMode_Type()
)
mediaGatewayProfile_VoipOptions_PacketAudioMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_VoipOptions_PacketAudioMode.setStatus("mandatory")
_MediaGatewayProfile_VoipOptions_FramesPerPacket_Type = Integer32
_MediaGatewayProfile_VoipOptions_FramesPerPacket_Object = MibScalar
mediaGatewayProfile_VoipOptions_FramesPerPacket = _MediaGatewayProfile_VoipOptions_FramesPerPacket_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 19),
    _MediaGatewayProfile_VoipOptions_FramesPerPacket_Type()
)
mediaGatewayProfile_VoipOptions_FramesPerPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_VoipOptions_FramesPerPacket.setStatus("mandatory")


class _MediaGatewayProfile_VoipOptions_SilenceDetCng_Type(Integer32):
    """Custom type mediaGatewayProfile_VoipOptions_SilenceDetCng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cngOnly", 3),
          ("no", 1),
          ("yes", 2))
    )


_MediaGatewayProfile_VoipOptions_SilenceDetCng_Type.__name__ = "Integer32"
_MediaGatewayProfile_VoipOptions_SilenceDetCng_Object = MibScalar
mediaGatewayProfile_VoipOptions_SilenceDetCng = _MediaGatewayProfile_VoipOptions_SilenceDetCng_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 20),
    _MediaGatewayProfile_VoipOptions_SilenceDetCng_Type()
)
mediaGatewayProfile_VoipOptions_SilenceDetCng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_VoipOptions_SilenceDetCng.setStatus("mandatory")


class _MediaGatewayProfile_VoipOptions_EnaAdapJitterBuffer_Type(Integer32):
    """Custom type mediaGatewayProfile_VoipOptions_EnaAdapJitterBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MediaGatewayProfile_VoipOptions_EnaAdapJitterBuffer_Type.__name__ = "Integer32"
_MediaGatewayProfile_VoipOptions_EnaAdapJitterBuffer_Object = MibScalar
mediaGatewayProfile_VoipOptions_EnaAdapJitterBuffer = _MediaGatewayProfile_VoipOptions_EnaAdapJitterBuffer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 21),
    _MediaGatewayProfile_VoipOptions_EnaAdapJitterBuffer_Type()
)
mediaGatewayProfile_VoipOptions_EnaAdapJitterBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_VoipOptions_EnaAdapJitterBuffer.setStatus("mandatory")
_MediaGatewayProfile_VoipOptions_MaxJitterBufferSize_Type = Integer32
_MediaGatewayProfile_VoipOptions_MaxJitterBufferSize_Object = MibScalar
mediaGatewayProfile_VoipOptions_MaxJitterBufferSize = _MediaGatewayProfile_VoipOptions_MaxJitterBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 22),
    _MediaGatewayProfile_VoipOptions_MaxJitterBufferSize_Type()
)
mediaGatewayProfile_VoipOptions_MaxJitterBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_VoipOptions_MaxJitterBufferSize.setStatus("mandatory")
_MediaGatewayProfile_VoipOptions_InitialJitterBufferSize_Type = Integer32
_MediaGatewayProfile_VoipOptions_InitialJitterBufferSize_Object = MibScalar
mediaGatewayProfile_VoipOptions_InitialJitterBufferSize = _MediaGatewayProfile_VoipOptions_InitialJitterBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 23),
    _MediaGatewayProfile_VoipOptions_InitialJitterBufferSize_Type()
)
mediaGatewayProfile_VoipOptions_InitialJitterBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_VoipOptions_InitialJitterBufferSize.setStatus("mandatory")
_MediaGatewayProfile_VoipOptions_VoiceAnnDir_Type = DisplayString
_MediaGatewayProfile_VoipOptions_VoiceAnnDir_Object = MibScalar
mediaGatewayProfile_VoipOptions_VoiceAnnDir = _MediaGatewayProfile_VoipOptions_VoiceAnnDir_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 24),
    _MediaGatewayProfile_VoipOptions_VoiceAnnDir_Type()
)
mediaGatewayProfile_VoipOptions_VoiceAnnDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_VoipOptions_VoiceAnnDir.setStatus("mandatory")


class _MediaGatewayProfile_VoipOptions_VoiceAnnEnc_Type(Integer32):
    """Custom type mediaGatewayProfile_VoipOptions_VoiceAnnEnc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("g711Ulaw", 1),
          ("g729", 4))
    )


_MediaGatewayProfile_VoipOptions_VoiceAnnEnc_Type.__name__ = "Integer32"
_MediaGatewayProfile_VoipOptions_VoiceAnnEnc_Object = MibScalar
mediaGatewayProfile_VoipOptions_VoiceAnnEnc = _MediaGatewayProfile_VoipOptions_VoiceAnnEnc_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 25),
    _MediaGatewayProfile_VoipOptions_VoiceAnnEnc_Type()
)
mediaGatewayProfile_VoipOptions_VoiceAnnEnc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_VoipOptions_VoiceAnnEnc.setStatus("mandatory")
_MediaGatewayProfile_VoipOptions_CallInterDigitTimeout_Type = Integer32
_MediaGatewayProfile_VoipOptions_CallInterDigitTimeout_Object = MibScalar
mediaGatewayProfile_VoipOptions_CallInterDigitTimeout = _MediaGatewayProfile_VoipOptions_CallInterDigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 26),
    _MediaGatewayProfile_VoipOptions_CallInterDigitTimeout_Type()
)
mediaGatewayProfile_VoipOptions_CallInterDigitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_VoipOptions_CallInterDigitTimeout.setStatus("mandatory")
_MediaGatewayProfile_VoipOptions_SilenceThreshold_Type = Integer32
_MediaGatewayProfile_VoipOptions_SilenceThreshold_Object = MibScalar
mediaGatewayProfile_VoipOptions_SilenceThreshold = _MediaGatewayProfile_VoipOptions_SilenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 27),
    _MediaGatewayProfile_VoipOptions_SilenceThreshold_Type()
)
mediaGatewayProfile_VoipOptions_SilenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_VoipOptions_SilenceThreshold.setStatus("mandatory")


class _MediaGatewayProfile_VoipOptions_DtmfTonePassing_Type(Integer32):
    """Custom type mediaGatewayProfile_VoipOptions_DtmfTonePassing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inband", 1),
          ("outofband", 2),
          ("rtp", 3))
    )


_MediaGatewayProfile_VoipOptions_DtmfTonePassing_Type.__name__ = "Integer32"
_MediaGatewayProfile_VoipOptions_DtmfTonePassing_Object = MibScalar
mediaGatewayProfile_VoipOptions_DtmfTonePassing = _MediaGatewayProfile_VoipOptions_DtmfTonePassing_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 28),
    _MediaGatewayProfile_VoipOptions_DtmfTonePassing_Type()
)
mediaGatewayProfile_VoipOptions_DtmfTonePassing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_VoipOptions_DtmfTonePassing.setStatus("mandatory")
_MediaGatewayProfile_VoipOptions_Maxcalls_Type = Integer32
_MediaGatewayProfile_VoipOptions_Maxcalls_Object = MibScalar
mediaGatewayProfile_VoipOptions_Maxcalls = _MediaGatewayProfile_VoipOptions_Maxcalls_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 29),
    _MediaGatewayProfile_VoipOptions_Maxcalls_Type()
)
mediaGatewayProfile_VoipOptions_Maxcalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_VoipOptions_Maxcalls.setStatus("mandatory")
_MediaGatewayProfile_VoipOptions_Rfc2833PayloadType_Type = Integer32
_MediaGatewayProfile_VoipOptions_Rfc2833PayloadType_Object = MibScalar
mediaGatewayProfile_VoipOptions_Rfc2833PayloadType = _MediaGatewayProfile_VoipOptions_Rfc2833PayloadType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 30),
    _MediaGatewayProfile_VoipOptions_Rfc2833PayloadType_Type()
)
mediaGatewayProfile_VoipOptions_Rfc2833PayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_VoipOptions_Rfc2833PayloadType.setStatus("mandatory")


class _MediaGatewayProfile_VoipOptions_G711TransparentData_Type(Integer32):
    """Custom type mediaGatewayProfile_VoipOptions_G711TransparentData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MediaGatewayProfile_VoipOptions_G711TransparentData_Type.__name__ = "Integer32"
_MediaGatewayProfile_VoipOptions_G711TransparentData_Object = MibScalar
mediaGatewayProfile_VoipOptions_G711TransparentData = _MediaGatewayProfile_VoipOptions_G711TransparentData_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 31),
    _MediaGatewayProfile_VoipOptions_G711TransparentData_Type()
)
mediaGatewayProfile_VoipOptions_G711TransparentData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_VoipOptions_G711TransparentData.setStatus("mandatory")


class _MediaGatewayProfile_DialedGwOptions_CallHairpin_Type(Integer32):
    """Custom type mediaGatewayProfile_DialedGwOptions_CallHairpin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MediaGatewayProfile_DialedGwOptions_CallHairpin_Type.__name__ = "Integer32"
_MediaGatewayProfile_DialedGwOptions_CallHairpin_Object = MibScalar
mediaGatewayProfile_DialedGwOptions_CallHairpin = _MediaGatewayProfile_DialedGwOptions_CallHairpin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 32),
    _MediaGatewayProfile_DialedGwOptions_CallHairpin_Type()
)
mediaGatewayProfile_DialedGwOptions_CallHairpin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_DialedGwOptions_CallHairpin.setStatus("mandatory")


class _MediaGatewayProfile_DialedGwOptions_TrunkQuiesce_Type(Integer32):
    """Custom type mediaGatewayProfile_DialedGwOptions_TrunkQuiesce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MediaGatewayProfile_DialedGwOptions_TrunkQuiesce_Type.__name__ = "Integer32"
_MediaGatewayProfile_DialedGwOptions_TrunkQuiesce_Object = MibScalar
mediaGatewayProfile_DialedGwOptions_TrunkQuiesce = _MediaGatewayProfile_DialedGwOptions_TrunkQuiesce_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 33),
    _MediaGatewayProfile_DialedGwOptions_TrunkQuiesce_Type()
)
mediaGatewayProfile_DialedGwOptions_TrunkQuiesce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_DialedGwOptions_TrunkQuiesce.setStatus("mandatory")


class _MediaGatewayProfile_DialedGwOptions_TrunkPrefix_Type(Integer32):
    """Custom type mediaGatewayProfile_DialedGwOptions_TrunkPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MediaGatewayProfile_DialedGwOptions_TrunkPrefix_Type.__name__ = "Integer32"
_MediaGatewayProfile_DialedGwOptions_TrunkPrefix_Object = MibScalar
mediaGatewayProfile_DialedGwOptions_TrunkPrefix = _MediaGatewayProfile_DialedGwOptions_TrunkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 34),
    _MediaGatewayProfile_DialedGwOptions_TrunkPrefix_Type()
)
mediaGatewayProfile_DialedGwOptions_TrunkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_DialedGwOptions_TrunkPrefix.setStatus("mandatory")


class _MediaGatewayProfile_DialedGwOptions_StartLocalRingTone_Type(Integer32):
    """Custom type mediaGatewayProfile_DialedGwOptions_StartLocalRingTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ringToneOnAlerting", 1),
          ("ringToneOnCallProgress", 3),
          ("ringToneOnFirstMessage", 2))
    )


_MediaGatewayProfile_DialedGwOptions_StartLocalRingTone_Type.__name__ = "Integer32"
_MediaGatewayProfile_DialedGwOptions_StartLocalRingTone_Object = MibScalar
mediaGatewayProfile_DialedGwOptions_StartLocalRingTone = _MediaGatewayProfile_DialedGwOptions_StartLocalRingTone_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 35),
    _MediaGatewayProfile_DialedGwOptions_StartLocalRingTone_Type()
)
mediaGatewayProfile_DialedGwOptions_StartLocalRingTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_DialedGwOptions_StartLocalRingTone.setStatus("mandatory")


class _MediaGatewayProfile_DialedGwOptions_MediaWaitForConnect_Type(Integer32):
    """Custom type mediaGatewayProfile_DialedGwOptions_MediaWaitForConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MediaGatewayProfile_DialedGwOptions_MediaWaitForConnect_Type.__name__ = "Integer32"
_MediaGatewayProfile_DialedGwOptions_MediaWaitForConnect_Object = MibScalar
mediaGatewayProfile_DialedGwOptions_MediaWaitForConnect = _MediaGatewayProfile_DialedGwOptions_MediaWaitForConnect_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 36),
    _MediaGatewayProfile_DialedGwOptions_MediaWaitForConnect_Type()
)
mediaGatewayProfile_DialedGwOptions_MediaWaitForConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_DialedGwOptions_MediaWaitForConnect.setStatus("mandatory")


class _MediaGatewayProfile_RtFaxOptions_RtFaxEnable_Type(Integer32):
    """Custom type mediaGatewayProfile_RtFaxOptions_RtFaxEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MediaGatewayProfile_RtFaxOptions_RtFaxEnable_Type.__name__ = "Integer32"
_MediaGatewayProfile_RtFaxOptions_RtFaxEnable_Object = MibScalar
mediaGatewayProfile_RtFaxOptions_RtFaxEnable = _MediaGatewayProfile_RtFaxOptions_RtFaxEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 37),
    _MediaGatewayProfile_RtFaxOptions_RtFaxEnable_Type()
)
mediaGatewayProfile_RtFaxOptions_RtFaxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_RtFaxOptions_RtFaxEnable.setStatus("mandatory")


class _MediaGatewayProfile_RtFaxOptions_EcmEnable_Type(Integer32):
    """Custom type mediaGatewayProfile_RtFaxOptions_EcmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MediaGatewayProfile_RtFaxOptions_EcmEnable_Type.__name__ = "Integer32"
_MediaGatewayProfile_RtFaxOptions_EcmEnable_Object = MibScalar
mediaGatewayProfile_RtFaxOptions_EcmEnable = _MediaGatewayProfile_RtFaxOptions_EcmEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 38),
    _MediaGatewayProfile_RtFaxOptions_EcmEnable_Type()
)
mediaGatewayProfile_RtFaxOptions_EcmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_RtFaxOptions_EcmEnable.setStatus("mandatory")


class _MediaGatewayProfile_RtFaxOptions_LowLatencyMode_Type(Integer32):
    """Custom type mediaGatewayProfile_RtFaxOptions_LowLatencyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MediaGatewayProfile_RtFaxOptions_LowLatencyMode_Type.__name__ = "Integer32"
_MediaGatewayProfile_RtFaxOptions_LowLatencyMode_Object = MibScalar
mediaGatewayProfile_RtFaxOptions_LowLatencyMode = _MediaGatewayProfile_RtFaxOptions_LowLatencyMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 39),
    _MediaGatewayProfile_RtFaxOptions_LowLatencyMode_Type()
)
mediaGatewayProfile_RtFaxOptions_LowLatencyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_RtFaxOptions_LowLatencyMode.setStatus("mandatory")


class _MediaGatewayProfile_RtFaxOptions_CommandSpoof_Type(Integer32):
    """Custom type mediaGatewayProfile_RtFaxOptions_CommandSpoof based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MediaGatewayProfile_RtFaxOptions_CommandSpoof_Type.__name__ = "Integer32"
_MediaGatewayProfile_RtFaxOptions_CommandSpoof_Object = MibScalar
mediaGatewayProfile_RtFaxOptions_CommandSpoof = _MediaGatewayProfile_RtFaxOptions_CommandSpoof_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 40),
    _MediaGatewayProfile_RtFaxOptions_CommandSpoof_Type()
)
mediaGatewayProfile_RtFaxOptions_CommandSpoof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_RtFaxOptions_CommandSpoof.setStatus("mandatory")


class _MediaGatewayProfile_RtFaxOptions_LocalRetransmitLsf_Type(Integer32):
    """Custom type mediaGatewayProfile_RtFaxOptions_LocalRetransmitLsf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MediaGatewayProfile_RtFaxOptions_LocalRetransmitLsf_Type.__name__ = "Integer32"
_MediaGatewayProfile_RtFaxOptions_LocalRetransmitLsf_Object = MibScalar
mediaGatewayProfile_RtFaxOptions_LocalRetransmitLsf = _MediaGatewayProfile_RtFaxOptions_LocalRetransmitLsf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 41),
    _MediaGatewayProfile_RtFaxOptions_LocalRetransmitLsf_Type()
)
mediaGatewayProfile_RtFaxOptions_LocalRetransmitLsf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_RtFaxOptions_LocalRetransmitLsf.setStatus("mandatory")
_MediaGatewayProfile_RtFaxOptions_PacketRedundancy_Type = Integer32
_MediaGatewayProfile_RtFaxOptions_PacketRedundancy_Object = MibScalar
mediaGatewayProfile_RtFaxOptions_PacketRedundancy = _MediaGatewayProfile_RtFaxOptions_PacketRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 42),
    _MediaGatewayProfile_RtFaxOptions_PacketRedundancy_Type()
)
mediaGatewayProfile_RtFaxOptions_PacketRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_RtFaxOptions_PacketRedundancy.setStatus("mandatory")


class _MediaGatewayProfile_RtFaxOptions_FixedPackets_Type(Integer32):
    """Custom type mediaGatewayProfile_RtFaxOptions_FixedPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MediaGatewayProfile_RtFaxOptions_FixedPackets_Type.__name__ = "Integer32"
_MediaGatewayProfile_RtFaxOptions_FixedPackets_Object = MibScalar
mediaGatewayProfile_RtFaxOptions_FixedPackets = _MediaGatewayProfile_RtFaxOptions_FixedPackets_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 43),
    _MediaGatewayProfile_RtFaxOptions_FixedPackets_Type()
)
mediaGatewayProfile_RtFaxOptions_FixedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_RtFaxOptions_FixedPackets.setStatus("mandatory")


class _MediaGatewayProfile_RtFaxOptions_MaxDataRate_Type(Integer32):
    """Custom type mediaGatewayProfile_RtFaxOptions_MaxDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2401,
              4801,
              9601,
              14401)
        )
    )
    namedValues = NamedValues(
        *(("n-14400", 14401),
          ("n-2400", 2401),
          ("n-4800", 4801),
          ("n-9600", 9601))
    )


_MediaGatewayProfile_RtFaxOptions_MaxDataRate_Type.__name__ = "Integer32"
_MediaGatewayProfile_RtFaxOptions_MaxDataRate_Object = MibScalar
mediaGatewayProfile_RtFaxOptions_MaxDataRate = _MediaGatewayProfile_RtFaxOptions_MaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 44),
    _MediaGatewayProfile_RtFaxOptions_MaxDataRate_Type()
)
mediaGatewayProfile_RtFaxOptions_MaxDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_RtFaxOptions_MaxDataRate.setStatus("mandatory")


class _MediaGatewayProfile_RtFaxOptions_AllowCtc_Type(Integer32):
    """Custom type mediaGatewayProfile_RtFaxOptions_AllowCtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MediaGatewayProfile_RtFaxOptions_AllowCtc_Type.__name__ = "Integer32"
_MediaGatewayProfile_RtFaxOptions_AllowCtc_Object = MibScalar
mediaGatewayProfile_RtFaxOptions_AllowCtc = _MediaGatewayProfile_RtFaxOptions_AllowCtc_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 45),
    _MediaGatewayProfile_RtFaxOptions_AllowCtc_Type()
)
mediaGatewayProfile_RtFaxOptions_AllowCtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_RtFaxOptions_AllowCtc.setStatus("mandatory")


class _MediaGatewayProfile_TosRtpOptions_Active_Type(Integer32):
    """Custom type mediaGatewayProfile_TosRtpOptions_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MediaGatewayProfile_TosRtpOptions_Active_Type.__name__ = "Integer32"
_MediaGatewayProfile_TosRtpOptions_Active_Object = MibScalar
mediaGatewayProfile_TosRtpOptions_Active = _MediaGatewayProfile_TosRtpOptions_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 46),
    _MediaGatewayProfile_TosRtpOptions_Active_Type()
)
mediaGatewayProfile_TosRtpOptions_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_TosRtpOptions_Active.setStatus("mandatory")


class _MediaGatewayProfile_TosRtpOptions_Precedence_Type(Integer32):
    """Custom type mediaGatewayProfile_TosRtpOptions_Precedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              33,
              65,
              97,
              129,
              161,
              193,
              225)
        )
    )
    namedValues = NamedValues(
        *(("n-000", 1),
          ("n-001", 33),
          ("n-010", 65),
          ("n-011", 97),
          ("n-100", 129),
          ("n-101", 161),
          ("n-110", 193),
          ("n-111", 225))
    )


_MediaGatewayProfile_TosRtpOptions_Precedence_Type.__name__ = "Integer32"
_MediaGatewayProfile_TosRtpOptions_Precedence_Object = MibScalar
mediaGatewayProfile_TosRtpOptions_Precedence = _MediaGatewayProfile_TosRtpOptions_Precedence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 47),
    _MediaGatewayProfile_TosRtpOptions_Precedence_Type()
)
mediaGatewayProfile_TosRtpOptions_Precedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_TosRtpOptions_Precedence.setStatus("mandatory")


class _MediaGatewayProfile_TosRtpOptions_TypeOfService_Type(Integer32):
    """Custom type mediaGatewayProfile_TosRtpOptions_TypeOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              9,
              17)
        )
    )
    namedValues = NamedValues(
        *(("cost", 3),
          ("latency", 17),
          ("normal", 1),
          ("reliability", 5),
          ("throughput", 9))
    )


_MediaGatewayProfile_TosRtpOptions_TypeOfService_Type.__name__ = "Integer32"
_MediaGatewayProfile_TosRtpOptions_TypeOfService_Object = MibScalar
mediaGatewayProfile_TosRtpOptions_TypeOfService = _MediaGatewayProfile_TosRtpOptions_TypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 48),
    _MediaGatewayProfile_TosRtpOptions_TypeOfService_Type()
)
mediaGatewayProfile_TosRtpOptions_TypeOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_TosRtpOptions_TypeOfService.setStatus("mandatory")


class _MediaGatewayProfile_TosRtpOptions_ApplyTo_Type(Integer32):
    """Custom type mediaGatewayProfile_TosRtpOptions_ApplyTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1025,
              2049,
              3073)
        )
    )
    namedValues = NamedValues(
        *(("both", 3073),
          ("incoming", 1025),
          ("outgoing", 2049))
    )


_MediaGatewayProfile_TosRtpOptions_ApplyTo_Type.__name__ = "Integer32"
_MediaGatewayProfile_TosRtpOptions_ApplyTo_Object = MibScalar
mediaGatewayProfile_TosRtpOptions_ApplyTo = _MediaGatewayProfile_TosRtpOptions_ApplyTo_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 49),
    _MediaGatewayProfile_TosRtpOptions_ApplyTo_Type()
)
mediaGatewayProfile_TosRtpOptions_ApplyTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_TosRtpOptions_ApplyTo.setStatus("mandatory")


class _MediaGatewayProfile_TosRtpOptions_MarkingType_Type(Integer32):
    """Custom type mediaGatewayProfile_TosRtpOptions_MarkingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 2),
          ("precedenceTos", 1))
    )


_MediaGatewayProfile_TosRtpOptions_MarkingType_Type.__name__ = "Integer32"
_MediaGatewayProfile_TosRtpOptions_MarkingType_Object = MibScalar
mediaGatewayProfile_TosRtpOptions_MarkingType = _MediaGatewayProfile_TosRtpOptions_MarkingType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 50),
    _MediaGatewayProfile_TosRtpOptions_MarkingType_Type()
)
mediaGatewayProfile_TosRtpOptions_MarkingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_TosRtpOptions_MarkingType.setStatus("mandatory")
_MediaGatewayProfile_TosRtpOptions_Dscp_Type = DisplayString
_MediaGatewayProfile_TosRtpOptions_Dscp_Object = MibScalar
mediaGatewayProfile_TosRtpOptions_Dscp = _MediaGatewayProfile_TosRtpOptions_Dscp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 51),
    _MediaGatewayProfile_TosRtpOptions_Dscp_Type()
)
mediaGatewayProfile_TosRtpOptions_Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_TosRtpOptions_Dscp.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_T1Timer_Type = Integer32
_MediaGatewayProfile_SipOptions_T1Timer_Object = MibScalar
mediaGatewayProfile_SipOptions_T1Timer = _MediaGatewayProfile_SipOptions_T1Timer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 52),
    _MediaGatewayProfile_SipOptions_T1Timer_Type()
)
mediaGatewayProfile_SipOptions_T1Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_T1Timer.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_T2Timer_Type = Integer32
_MediaGatewayProfile_SipOptions_T2Timer_Object = MibScalar
mediaGatewayProfile_SipOptions_T2Timer = _MediaGatewayProfile_SipOptions_T2Timer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 53),
    _MediaGatewayProfile_SipOptions_T2Timer_Type()
)
mediaGatewayProfile_SipOptions_T2Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_T2Timer.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_InviteRetries_Type = Integer32
_MediaGatewayProfile_SipOptions_InviteRetries_Object = MibScalar
mediaGatewayProfile_SipOptions_InviteRetries = _MediaGatewayProfile_SipOptions_InviteRetries_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 54),
    _MediaGatewayProfile_SipOptions_InviteRetries_Type()
)
mediaGatewayProfile_SipOptions_InviteRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_InviteRetries.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_NonInviteRetries_Type = Integer32
_MediaGatewayProfile_SipOptions_NonInviteRetries_Object = MibScalar
mediaGatewayProfile_SipOptions_NonInviteRetries = _MediaGatewayProfile_SipOptions_NonInviteRetries_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 55),
    _MediaGatewayProfile_SipOptions_NonInviteRetries_Type()
)
mediaGatewayProfile_SipOptions_NonInviteRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_NonInviteRetries.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_PrimaryProxy_IpAddress_Type = IpAddress
_MediaGatewayProfile_SipOptions_PrimaryProxy_IpAddress_Object = MibScalar
mediaGatewayProfile_SipOptions_PrimaryProxy_IpAddress = _MediaGatewayProfile_SipOptions_PrimaryProxy_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 56),
    _MediaGatewayProfile_SipOptions_PrimaryProxy_IpAddress_Type()
)
mediaGatewayProfile_SipOptions_PrimaryProxy_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_PrimaryProxy_IpAddress.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_PrimaryProxy_Name_Type = DisplayString
_MediaGatewayProfile_SipOptions_PrimaryProxy_Name_Object = MibScalar
mediaGatewayProfile_SipOptions_PrimaryProxy_Name = _MediaGatewayProfile_SipOptions_PrimaryProxy_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 57),
    _MediaGatewayProfile_SipOptions_PrimaryProxy_Name_Type()
)
mediaGatewayProfile_SipOptions_PrimaryProxy_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_PrimaryProxy_Name.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_PrimaryProxy_PortNumber_Type = Integer32
_MediaGatewayProfile_SipOptions_PrimaryProxy_PortNumber_Object = MibScalar
mediaGatewayProfile_SipOptions_PrimaryProxy_PortNumber = _MediaGatewayProfile_SipOptions_PrimaryProxy_PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 58),
    _MediaGatewayProfile_SipOptions_PrimaryProxy_PortNumber_Type()
)
mediaGatewayProfile_SipOptions_PrimaryProxy_PortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_PrimaryProxy_PortNumber.setStatus("mandatory")


class _MediaGatewayProfile_SipOptions_PrimaryProxy_MessageFormat_Type(Integer32):
    """Custom type mediaGatewayProfile_SipOptions_PrimaryProxy_MessageFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compact", 1),
          ("long", 2))
    )


_MediaGatewayProfile_SipOptions_PrimaryProxy_MessageFormat_Type.__name__ = "Integer32"
_MediaGatewayProfile_SipOptions_PrimaryProxy_MessageFormat_Object = MibScalar
mediaGatewayProfile_SipOptions_PrimaryProxy_MessageFormat = _MediaGatewayProfile_SipOptions_PrimaryProxy_MessageFormat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 59),
    _MediaGatewayProfile_SipOptions_PrimaryProxy_MessageFormat_Type()
)
mediaGatewayProfile_SipOptions_PrimaryProxy_MessageFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_PrimaryProxy_MessageFormat.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_SecondaryProxy_IpAddress_Type = IpAddress
_MediaGatewayProfile_SipOptions_SecondaryProxy_IpAddress_Object = MibScalar
mediaGatewayProfile_SipOptions_SecondaryProxy_IpAddress = _MediaGatewayProfile_SipOptions_SecondaryProxy_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 60),
    _MediaGatewayProfile_SipOptions_SecondaryProxy_IpAddress_Type()
)
mediaGatewayProfile_SipOptions_SecondaryProxy_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_SecondaryProxy_IpAddress.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_SecondaryProxy_Name_Type = DisplayString
_MediaGatewayProfile_SipOptions_SecondaryProxy_Name_Object = MibScalar
mediaGatewayProfile_SipOptions_SecondaryProxy_Name = _MediaGatewayProfile_SipOptions_SecondaryProxy_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 61),
    _MediaGatewayProfile_SipOptions_SecondaryProxy_Name_Type()
)
mediaGatewayProfile_SipOptions_SecondaryProxy_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_SecondaryProxy_Name.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_SecondaryProxy_PortNumber_Type = Integer32
_MediaGatewayProfile_SipOptions_SecondaryProxy_PortNumber_Object = MibScalar
mediaGatewayProfile_SipOptions_SecondaryProxy_PortNumber = _MediaGatewayProfile_SipOptions_SecondaryProxy_PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 62),
    _MediaGatewayProfile_SipOptions_SecondaryProxy_PortNumber_Type()
)
mediaGatewayProfile_SipOptions_SecondaryProxy_PortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_SecondaryProxy_PortNumber.setStatus("mandatory")


class _MediaGatewayProfile_SipOptions_SecondaryProxy_MessageFormat_Type(Integer32):
    """Custom type mediaGatewayProfile_SipOptions_SecondaryProxy_MessageFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compact", 1),
          ("long", 2))
    )


_MediaGatewayProfile_SipOptions_SecondaryProxy_MessageFormat_Type.__name__ = "Integer32"
_MediaGatewayProfile_SipOptions_SecondaryProxy_MessageFormat_Object = MibScalar
mediaGatewayProfile_SipOptions_SecondaryProxy_MessageFormat = _MediaGatewayProfile_SipOptions_SecondaryProxy_MessageFormat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 63),
    _MediaGatewayProfile_SipOptions_SecondaryProxy_MessageFormat_Type()
)
mediaGatewayProfile_SipOptions_SecondaryProxy_MessageFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_SecondaryProxy_MessageFormat.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_RegistrationProxy_IpAddress_Type = IpAddress
_MediaGatewayProfile_SipOptions_RegistrationProxy_IpAddress_Object = MibScalar
mediaGatewayProfile_SipOptions_RegistrationProxy_IpAddress = _MediaGatewayProfile_SipOptions_RegistrationProxy_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 64),
    _MediaGatewayProfile_SipOptions_RegistrationProxy_IpAddress_Type()
)
mediaGatewayProfile_SipOptions_RegistrationProxy_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_RegistrationProxy_IpAddress.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_RegistrationProxy_Name_Type = DisplayString
_MediaGatewayProfile_SipOptions_RegistrationProxy_Name_Object = MibScalar
mediaGatewayProfile_SipOptions_RegistrationProxy_Name = _MediaGatewayProfile_SipOptions_RegistrationProxy_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 65),
    _MediaGatewayProfile_SipOptions_RegistrationProxy_Name_Type()
)
mediaGatewayProfile_SipOptions_RegistrationProxy_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_RegistrationProxy_Name.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_RegistrationProxy_PortNumber_Type = Integer32
_MediaGatewayProfile_SipOptions_RegistrationProxy_PortNumber_Object = MibScalar
mediaGatewayProfile_SipOptions_RegistrationProxy_PortNumber = _MediaGatewayProfile_SipOptions_RegistrationProxy_PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 66),
    _MediaGatewayProfile_SipOptions_RegistrationProxy_PortNumber_Type()
)
mediaGatewayProfile_SipOptions_RegistrationProxy_PortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_RegistrationProxy_PortNumber.setStatus("mandatory")


class _MediaGatewayProfile_SipOptions_RegistrationProxy_MessageFormat_Type(Integer32):
    """Custom type mediaGatewayProfile_SipOptions_RegistrationProxy_MessageFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compact", 1),
          ("long", 2))
    )


_MediaGatewayProfile_SipOptions_RegistrationProxy_MessageFormat_Type.__name__ = "Integer32"
_MediaGatewayProfile_SipOptions_RegistrationProxy_MessageFormat_Object = MibScalar
mediaGatewayProfile_SipOptions_RegistrationProxy_MessageFormat = _MediaGatewayProfile_SipOptions_RegistrationProxy_MessageFormat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 67),
    _MediaGatewayProfile_SipOptions_RegistrationProxy_MessageFormat_Type()
)
mediaGatewayProfile_SipOptions_RegistrationProxy_MessageFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_RegistrationProxy_MessageFormat.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_RegistrationProxy_RegisterInterval_Type = Integer32
_MediaGatewayProfile_SipOptions_RegistrationProxy_RegisterInterval_Object = MibScalar
mediaGatewayProfile_SipOptions_RegistrationProxy_RegisterInterval = _MediaGatewayProfile_SipOptions_RegistrationProxy_RegisterInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 68),
    _MediaGatewayProfile_SipOptions_RegistrationProxy_RegisterInterval_Type()
)
mediaGatewayProfile_SipOptions_RegistrationProxy_RegisterInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_RegistrationProxy_RegisterInterval.setStatus("mandatory")


class _MediaGatewayProfile_SipOptions_TrustedProxy_AuthenticateMessages_Type(Integer32):
    """Custom type mediaGatewayProfile_SipOptions_TrustedProxy_AuthenticateMessages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MediaGatewayProfile_SipOptions_TrustedProxy_AuthenticateMessages_Type.__name__ = "Integer32"
_MediaGatewayProfile_SipOptions_TrustedProxy_AuthenticateMessages_Object = MibScalar
mediaGatewayProfile_SipOptions_TrustedProxy_AuthenticateMessages = _MediaGatewayProfile_SipOptions_TrustedProxy_AuthenticateMessages_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 69),
    _MediaGatewayProfile_SipOptions_TrustedProxy_AuthenticateMessages_Type()
)
mediaGatewayProfile_SipOptions_TrustedProxy_AuthenticateMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_TrustedProxy_AuthenticateMessages.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_UnknownAni_Type = DisplayString
_MediaGatewayProfile_SipOptions_UnknownAni_Object = MibScalar
mediaGatewayProfile_SipOptions_UnknownAni = _MediaGatewayProfile_SipOptions_UnknownAni_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 70),
    _MediaGatewayProfile_SipOptions_UnknownAni_Type()
)
mediaGatewayProfile_SipOptions_UnknownAni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_UnknownAni.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_BlockedAni_Type = DisplayString
_MediaGatewayProfile_SipOptions_BlockedAni_Object = MibScalar
mediaGatewayProfile_SipOptions_BlockedAni = _MediaGatewayProfile_SipOptions_BlockedAni_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 71),
    _MediaGatewayProfile_SipOptions_BlockedAni_Type()
)
mediaGatewayProfile_SipOptions_BlockedAni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_BlockedAni.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_OnholdMinutes_Type = Integer32
_MediaGatewayProfile_SipOptions_OnholdMinutes_Object = MibScalar
mediaGatewayProfile_SipOptions_OnholdMinutes = _MediaGatewayProfile_SipOptions_OnholdMinutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 72),
    _MediaGatewayProfile_SipOptions_OnholdMinutes_Type()
)
mediaGatewayProfile_SipOptions_OnholdMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_OnholdMinutes.setStatus("mandatory")


class _MediaGatewayProfile_SipOptions_Support100rel_Type(Integer32):
    """Custom type mediaGatewayProfile_SipOptions_Support100rel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MediaGatewayProfile_SipOptions_Support100rel_Type.__name__ = "Integer32"
_MediaGatewayProfile_SipOptions_Support100rel_Object = MibScalar
mediaGatewayProfile_SipOptions_Support100rel = _MediaGatewayProfile_SipOptions_Support100rel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 73),
    _MediaGatewayProfile_SipOptions_Support100rel_Type()
)
mediaGatewayProfile_SipOptions_Support100rel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_Support100rel.setStatus("mandatory")


class _MediaGatewayProfile_SipOptions_Internationalize_Type(Integer32):
    """Custom type mediaGatewayProfile_SipOptions_Internationalize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MediaGatewayProfile_SipOptions_Internationalize_Type.__name__ = "Integer32"
_MediaGatewayProfile_SipOptions_Internationalize_Object = MibScalar
mediaGatewayProfile_SipOptions_Internationalize = _MediaGatewayProfile_SipOptions_Internationalize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 74),
    _MediaGatewayProfile_SipOptions_Internationalize_Type()
)
mediaGatewayProfile_SipOptions_Internationalize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_Internationalize.setStatus("mandatory")


class _MediaGatewayProfile_SipOptions_InternationalPrefix_Type(Integer32):
    """Custom type mediaGatewayProfile_SipOptions_InternationalPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MediaGatewayProfile_SipOptions_InternationalPrefix_Type.__name__ = "Integer32"
_MediaGatewayProfile_SipOptions_InternationalPrefix_Object = MibScalar
mediaGatewayProfile_SipOptions_InternationalPrefix = _MediaGatewayProfile_SipOptions_InternationalPrefix_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 75),
    _MediaGatewayProfile_SipOptions_InternationalPrefix_Type()
)
mediaGatewayProfile_SipOptions_InternationalPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_InternationalPrefix.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_CountryCode_Type = DisplayString
_MediaGatewayProfile_SipOptions_CountryCode_Object = MibScalar
mediaGatewayProfile_SipOptions_CountryCode = _MediaGatewayProfile_SipOptions_CountryCode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 76),
    _MediaGatewayProfile_SipOptions_CountryCode_Type()
)
mediaGatewayProfile_SipOptions_CountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_CountryCode.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_NationalDestinationCode_Type = DisplayString
_MediaGatewayProfile_SipOptions_NationalDestinationCode_Object = MibScalar
mediaGatewayProfile_SipOptions_NationalDestinationCode = _MediaGatewayProfile_SipOptions_NationalDestinationCode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 77),
    _MediaGatewayProfile_SipOptions_NationalDestinationCode_Type()
)
mediaGatewayProfile_SipOptions_NationalDestinationCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_NationalDestinationCode.setStatus("mandatory")


class _MediaGatewayProfile_Action_o_Type(Integer32):
    """Custom type mediaGatewayProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_MediaGatewayProfile_Action_o_Type.__name__ = "Integer32"
_MediaGatewayProfile_Action_o_Object = MibScalar
mediaGatewayProfile_Action_o = _MediaGatewayProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 78),
    _MediaGatewayProfile_Action_o_Type()
)
mediaGatewayProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_Action_o.setStatus("mandatory")


class _MediaGatewayProfile_VoipOptions_RtpProblemReporting_Enable_Type(Integer32):
    """Custom type mediaGatewayProfile_VoipOptions_RtpProblemReporting_Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MediaGatewayProfile_VoipOptions_RtpProblemReporting_Enable_Type.__name__ = "Integer32"
_MediaGatewayProfile_VoipOptions_RtpProblemReporting_Enable_Object = MibScalar
mediaGatewayProfile_VoipOptions_RtpProblemReporting_Enable = _MediaGatewayProfile_VoipOptions_RtpProblemReporting_Enable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 87),
    _MediaGatewayProfile_VoipOptions_RtpProblemReporting_Enable_Type()
)
mediaGatewayProfile_VoipOptions_RtpProblemReporting_Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_VoipOptions_RtpProblemReporting_Enable.setStatus("mandatory")
_MediaGatewayProfile_VoipOptions_RtpProblemReporting_MultMediaRcptOkTime_Type = Integer32
_MediaGatewayProfile_VoipOptions_RtpProblemReporting_MultMediaRcptOkTime_Object = MibScalar
mediaGatewayProfile_VoipOptions_RtpProblemReporting_MultMediaRcptOkTime = _MediaGatewayProfile_VoipOptions_RtpProblemReporting_MultMediaRcptOkTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 88),
    _MediaGatewayProfile_VoipOptions_RtpProblemReporting_MultMediaRcptOkTime_Type()
)
mediaGatewayProfile_VoipOptions_RtpProblemReporting_MultMediaRcptOkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_VoipOptions_RtpProblemReporting_MultMediaRcptOkTime.setStatus("mandatory")
_MediaGatewayProfile_VoipOptions_RtpProblemReporting_NoMediaRcptOkTime_Type = Integer32
_MediaGatewayProfile_VoipOptions_RtpProblemReporting_NoMediaRcptOkTime_Object = MibScalar
mediaGatewayProfile_VoipOptions_RtpProblemReporting_NoMediaRcptOkTime = _MediaGatewayProfile_VoipOptions_RtpProblemReporting_NoMediaRcptOkTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 89),
    _MediaGatewayProfile_VoipOptions_RtpProblemReporting_NoMediaRcptOkTime_Type()
)
mediaGatewayProfile_VoipOptions_RtpProblemReporting_NoMediaRcptOkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_VoipOptions_RtpProblemReporting_NoMediaRcptOkTime.setStatus("mandatory")


class _MediaGatewayProfile_TosSigOptions_Active_Type(Integer32):
    """Custom type mediaGatewayProfile_TosSigOptions_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MediaGatewayProfile_TosSigOptions_Active_Type.__name__ = "Integer32"
_MediaGatewayProfile_TosSigOptions_Active_Object = MibScalar
mediaGatewayProfile_TosSigOptions_Active = _MediaGatewayProfile_TosSigOptions_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 90),
    _MediaGatewayProfile_TosSigOptions_Active_Type()
)
mediaGatewayProfile_TosSigOptions_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_TosSigOptions_Active.setStatus("mandatory")


class _MediaGatewayProfile_TosSigOptions_Precedence_Type(Integer32):
    """Custom type mediaGatewayProfile_TosSigOptions_Precedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              33,
              65,
              97,
              129,
              161,
              193,
              225)
        )
    )
    namedValues = NamedValues(
        *(("n-000", 1),
          ("n-001", 33),
          ("n-010", 65),
          ("n-011", 97),
          ("n-100", 129),
          ("n-101", 161),
          ("n-110", 193),
          ("n-111", 225))
    )


_MediaGatewayProfile_TosSigOptions_Precedence_Type.__name__ = "Integer32"
_MediaGatewayProfile_TosSigOptions_Precedence_Object = MibScalar
mediaGatewayProfile_TosSigOptions_Precedence = _MediaGatewayProfile_TosSigOptions_Precedence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 91),
    _MediaGatewayProfile_TosSigOptions_Precedence_Type()
)
mediaGatewayProfile_TosSigOptions_Precedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_TosSigOptions_Precedence.setStatus("mandatory")


class _MediaGatewayProfile_TosSigOptions_TypeOfService_Type(Integer32):
    """Custom type mediaGatewayProfile_TosSigOptions_TypeOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              9,
              17)
        )
    )
    namedValues = NamedValues(
        *(("cost", 3),
          ("latency", 17),
          ("normal", 1),
          ("reliability", 5),
          ("throughput", 9))
    )


_MediaGatewayProfile_TosSigOptions_TypeOfService_Type.__name__ = "Integer32"
_MediaGatewayProfile_TosSigOptions_TypeOfService_Object = MibScalar
mediaGatewayProfile_TosSigOptions_TypeOfService = _MediaGatewayProfile_TosSigOptions_TypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 92),
    _MediaGatewayProfile_TosSigOptions_TypeOfService_Type()
)
mediaGatewayProfile_TosSigOptions_TypeOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_TosSigOptions_TypeOfService.setStatus("mandatory")


class _MediaGatewayProfile_TosSigOptions_ApplyTo_Type(Integer32):
    """Custom type mediaGatewayProfile_TosSigOptions_ApplyTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1025,
              2049,
              3073)
        )
    )
    namedValues = NamedValues(
        *(("both", 3073),
          ("incoming", 1025),
          ("outgoing", 2049))
    )


_MediaGatewayProfile_TosSigOptions_ApplyTo_Type.__name__ = "Integer32"
_MediaGatewayProfile_TosSigOptions_ApplyTo_Object = MibScalar
mediaGatewayProfile_TosSigOptions_ApplyTo = _MediaGatewayProfile_TosSigOptions_ApplyTo_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 93),
    _MediaGatewayProfile_TosSigOptions_ApplyTo_Type()
)
mediaGatewayProfile_TosSigOptions_ApplyTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_TosSigOptions_ApplyTo.setStatus("mandatory")


class _MediaGatewayProfile_TosSigOptions_MarkingType_Type(Integer32):
    """Custom type mediaGatewayProfile_TosSigOptions_MarkingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 2),
          ("precedenceTos", 1))
    )


_MediaGatewayProfile_TosSigOptions_MarkingType_Type.__name__ = "Integer32"
_MediaGatewayProfile_TosSigOptions_MarkingType_Object = MibScalar
mediaGatewayProfile_TosSigOptions_MarkingType = _MediaGatewayProfile_TosSigOptions_MarkingType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 94),
    _MediaGatewayProfile_TosSigOptions_MarkingType_Type()
)
mediaGatewayProfile_TosSigOptions_MarkingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_TosSigOptions_MarkingType.setStatus("mandatory")
_MediaGatewayProfile_TosSigOptions_Dscp_Type = DisplayString
_MediaGatewayProfile_TosSigOptions_Dscp_Object = MibScalar
mediaGatewayProfile_TosSigOptions_Dscp = _MediaGatewayProfile_TosSigOptions_Dscp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 95),
    _MediaGatewayProfile_TosSigOptions_Dscp_Type()
)
mediaGatewayProfile_TosSigOptions_Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_TosSigOptions_Dscp.setStatus("mandatory")


class _MediaGatewayProfile_SipOptions_PrivacyProxyRequire_Type(Integer32):
    """Custom type mediaGatewayProfile_SipOptions_PrivacyProxyRequire based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MediaGatewayProfile_SipOptions_PrivacyProxyRequire_Type.__name__ = "Integer32"
_MediaGatewayProfile_SipOptions_PrivacyProxyRequire_Object = MibScalar
mediaGatewayProfile_SipOptions_PrivacyProxyRequire = _MediaGatewayProfile_SipOptions_PrivacyProxyRequire_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 96),
    _MediaGatewayProfile_SipOptions_PrivacyProxyRequire_Type()
)
mediaGatewayProfile_SipOptions_PrivacyProxyRequire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_PrivacyProxyRequire.setStatus("mandatory")


class _MediaGatewayProfile_SipOptions_CallTransferMethod_Type(Integer32):
    """Custom type mediaGatewayProfile_SipOptions_CallTransferMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipTransfer", 1),
          ("pstnTransfer", 2))
    )


_MediaGatewayProfile_SipOptions_CallTransferMethod_Type.__name__ = "Integer32"
_MediaGatewayProfile_SipOptions_CallTransferMethod_Object = MibScalar
mediaGatewayProfile_SipOptions_CallTransferMethod = _MediaGatewayProfile_SipOptions_CallTransferMethod_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 97),
    _MediaGatewayProfile_SipOptions_CallTransferMethod_Type()
)
mediaGatewayProfile_SipOptions_CallTransferMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_CallTransferMethod.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_NotifyTimer_Type = Integer32
_MediaGatewayProfile_SipOptions_NotifyTimer_Object = MibScalar
mediaGatewayProfile_SipOptions_NotifyTimer = _MediaGatewayProfile_SipOptions_NotifyTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 98),
    _MediaGatewayProfile_SipOptions_NotifyTimer_Type()
)
mediaGatewayProfile_SipOptions_NotifyTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_NotifyTimer.setStatus("mandatory")


class _MediaGatewayProfile_Voip2ipOptions_DtmfTonePassing_Type(Integer32):
    """Custom type mediaGatewayProfile_Voip2ipOptions_DtmfTonePassing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inband", 1),
          ("outofband", 2),
          ("rtp", 3))
    )


_MediaGatewayProfile_Voip2ipOptions_DtmfTonePassing_Type.__name__ = "Integer32"
_MediaGatewayProfile_Voip2ipOptions_DtmfTonePassing_Object = MibScalar
mediaGatewayProfile_Voip2ipOptions_DtmfTonePassing = _MediaGatewayProfile_Voip2ipOptions_DtmfTonePassing_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 99),
    _MediaGatewayProfile_Voip2ipOptions_DtmfTonePassing_Type()
)
mediaGatewayProfile_Voip2ipOptions_DtmfTonePassing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_Voip2ipOptions_DtmfTonePassing.setStatus("mandatory")
_MediaGatewayProfile_Voip2ipOptions_RtpTranslatorMode_Type = Integer32
_MediaGatewayProfile_Voip2ipOptions_RtpTranslatorMode_Object = MibScalar
mediaGatewayProfile_Voip2ipOptions_RtpTranslatorMode = _MediaGatewayProfile_Voip2ipOptions_RtpTranslatorMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 100),
    _MediaGatewayProfile_Voip2ipOptions_RtpTranslatorMode_Type()
)
mediaGatewayProfile_Voip2ipOptions_RtpTranslatorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_Voip2ipOptions_RtpTranslatorMode.setStatus("mandatory")
_MediaGatewayProfile_Voip2ipOptions_MaxNumErasures_Type = Integer32
_MediaGatewayProfile_Voip2ipOptions_MaxNumErasures_Object = MibScalar
mediaGatewayProfile_Voip2ipOptions_MaxNumErasures = _MediaGatewayProfile_Voip2ipOptions_MaxNumErasures_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 101),
    _MediaGatewayProfile_Voip2ipOptions_MaxNumErasures_Type()
)
mediaGatewayProfile_Voip2ipOptions_MaxNumErasures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_Voip2ipOptions_MaxNumErasures.setStatus("mandatory")
_MediaGatewayProfile_Voip2ipOptions_JitterBufferSize_Type = Integer32
_MediaGatewayProfile_Voip2ipOptions_JitterBufferSize_Object = MibScalar
mediaGatewayProfile_Voip2ipOptions_JitterBufferSize = _MediaGatewayProfile_Voip2ipOptions_JitterBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 1, 1, 102),
    _MediaGatewayProfile_Voip2ipOptions_JitterBufferSize_Type()
)
mediaGatewayProfile_Voip2ipOptions_JitterBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_Voip2ipOptions_JitterBufferSize.setStatus("mandatory")
_MibmediaGatewayProfile_SipOptions_TrustedProxy_TableTable_Object = MibTable
mibmediaGatewayProfile_SipOptions_TrustedProxy_TableTable = _MibmediaGatewayProfile_SipOptions_TrustedProxy_TableTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 2)
)
if mibBuilder.loadTexts:
    mibmediaGatewayProfile_SipOptions_TrustedProxy_TableTable.setStatus("mandatory")
_MibmediaGatewayProfile_SipOptions_TrustedProxy_TableEntry_Object = MibTableRow
mibmediaGatewayProfile_SipOptions_TrustedProxy_TableEntry = _MibmediaGatewayProfile_SipOptions_TrustedProxy_TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 2, 1)
)
mibmediaGatewayProfile_SipOptions_TrustedProxy_TableEntry.setIndexNames(
    (0, "ASCEND-MIBMGW-MIB", "mediaGatewayProfile-SipOptions-TrustedProxy-Table-Name"),
    (0, "ASCEND-MIBMGW-MIB", "mediaGatewayProfile-SipOptions-TrustedProxy-Table-Index-o"),
)
if mibBuilder.loadTexts:
    mibmediaGatewayProfile_SipOptions_TrustedProxy_TableEntry.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_TrustedProxy_Table_Name_Type = DisplayString
_MediaGatewayProfile_SipOptions_TrustedProxy_Table_Name_Object = MibScalar
mediaGatewayProfile_SipOptions_TrustedProxy_Table_Name = _MediaGatewayProfile_SipOptions_TrustedProxy_Table_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 2, 1, 1),
    _MediaGatewayProfile_SipOptions_TrustedProxy_Table_Name_Type()
)
mediaGatewayProfile_SipOptions_TrustedProxy_Table_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_TrustedProxy_Table_Name.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_TrustedProxy_Table_Index_o_Type = Integer32
_MediaGatewayProfile_SipOptions_TrustedProxy_Table_Index_o_Object = MibScalar
mediaGatewayProfile_SipOptions_TrustedProxy_Table_Index_o = _MediaGatewayProfile_SipOptions_TrustedProxy_Table_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 2, 1, 2),
    _MediaGatewayProfile_SipOptions_TrustedProxy_Table_Index_o_Type()
)
mediaGatewayProfile_SipOptions_TrustedProxy_Table_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_TrustedProxy_Table_Index_o.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_TrustedProxy_Table_HostName_Type = DisplayString
_MediaGatewayProfile_SipOptions_TrustedProxy_Table_HostName_Object = MibScalar
mediaGatewayProfile_SipOptions_TrustedProxy_Table_HostName = _MediaGatewayProfile_SipOptions_TrustedProxy_Table_HostName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 2, 1, 3),
    _MediaGatewayProfile_SipOptions_TrustedProxy_Table_HostName_Type()
)
mediaGatewayProfile_SipOptions_TrustedProxy_Table_HostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_TrustedProxy_Table_HostName.setStatus("mandatory")
_MediaGatewayProfile_SipOptions_TrustedProxy_Table_IpAddress_Type = IpAddress
_MediaGatewayProfile_SipOptions_TrustedProxy_Table_IpAddress_Object = MibScalar
mediaGatewayProfile_SipOptions_TrustedProxy_Table_IpAddress = _MediaGatewayProfile_SipOptions_TrustedProxy_Table_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 2, 1, 4),
    _MediaGatewayProfile_SipOptions_TrustedProxy_Table_IpAddress_Type()
)
mediaGatewayProfile_SipOptions_TrustedProxy_Table_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_SipOptions_TrustedProxy_Table_IpAddress.setStatus("mandatory")
_MibmediaGatewayProfile_H248Options_DigitmapOptions_MapTable_Object = MibTable
mibmediaGatewayProfile_H248Options_DigitmapOptions_MapTable = _MibmediaGatewayProfile_H248Options_DigitmapOptions_MapTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 3)
)
if mibBuilder.loadTexts:
    mibmediaGatewayProfile_H248Options_DigitmapOptions_MapTable.setStatus("mandatory")
_MibmediaGatewayProfile_H248Options_DigitmapOptions_MapEntry_Object = MibTableRow
mibmediaGatewayProfile_H248Options_DigitmapOptions_MapEntry = _MibmediaGatewayProfile_H248Options_DigitmapOptions_MapEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 3, 1)
)
mibmediaGatewayProfile_H248Options_DigitmapOptions_MapEntry.setIndexNames(
    (0, "ASCEND-MIBMGW-MIB", "mediaGatewayProfile-H248Options-DigitmapOptions-Map-Name"),
    (0, "ASCEND-MIBMGW-MIB", "mediaGatewayProfile-H248Options-DigitmapOptions-Map-Index-o"),
)
if mibBuilder.loadTexts:
    mibmediaGatewayProfile_H248Options_DigitmapOptions_MapEntry.setStatus("mandatory")
_MediaGatewayProfile_H248Options_DigitmapOptions_Map_Name_Type = DisplayString
_MediaGatewayProfile_H248Options_DigitmapOptions_Map_Name_Object = MibScalar
mediaGatewayProfile_H248Options_DigitmapOptions_Map_Name = _MediaGatewayProfile_H248Options_DigitmapOptions_Map_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 3, 1, 1),
    _MediaGatewayProfile_H248Options_DigitmapOptions_Map_Name_Type()
)
mediaGatewayProfile_H248Options_DigitmapOptions_Map_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaGatewayProfile_H248Options_DigitmapOptions_Map_Name.setStatus("mandatory")
_MediaGatewayProfile_H248Options_DigitmapOptions_Map_Index_o_Type = Integer32
_MediaGatewayProfile_H248Options_DigitmapOptions_Map_Index_o_Object = MibScalar
mediaGatewayProfile_H248Options_DigitmapOptions_Map_Index_o = _MediaGatewayProfile_H248Options_DigitmapOptions_Map_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 3, 1, 2),
    _MediaGatewayProfile_H248Options_DigitmapOptions_Map_Index_o_Type()
)
mediaGatewayProfile_H248Options_DigitmapOptions_Map_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaGatewayProfile_H248Options_DigitmapOptions_Map_Index_o.setStatus("mandatory")
_MediaGatewayProfile_H248Options_DigitmapOptions_Map_ReferenceName_Type = DisplayString
_MediaGatewayProfile_H248Options_DigitmapOptions_Map_ReferenceName_Object = MibScalar
mediaGatewayProfile_H248Options_DigitmapOptions_Map_ReferenceName = _MediaGatewayProfile_H248Options_DigitmapOptions_Map_ReferenceName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 3, 1, 3),
    _MediaGatewayProfile_H248Options_DigitmapOptions_Map_ReferenceName_Type()
)
mediaGatewayProfile_H248Options_DigitmapOptions_Map_ReferenceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_H248Options_DigitmapOptions_Map_ReferenceName.setStatus("mandatory")
_MediaGatewayProfile_H248Options_DigitmapOptions_Map_Value_Type = DisplayString
_MediaGatewayProfile_H248Options_DigitmapOptions_Map_Value_Object = MibScalar
mediaGatewayProfile_H248Options_DigitmapOptions_Map_Value = _MediaGatewayProfile_H248Options_DigitmapOptions_Map_Value_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 3, 1, 4),
    _MediaGatewayProfile_H248Options_DigitmapOptions_Map_Value_Type()
)
mediaGatewayProfile_H248Options_DigitmapOptions_Map_Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_H248Options_DigitmapOptions_Map_Value.setStatus("mandatory")
_MibmediaGatewayProfile_MgcAddressTable_Object = MibTable
mibmediaGatewayProfile_MgcAddressTable = _MibmediaGatewayProfile_MgcAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 4)
)
if mibBuilder.loadTexts:
    mibmediaGatewayProfile_MgcAddressTable.setStatus("mandatory")
_MibmediaGatewayProfile_MgcAddressEntry_Object = MibTableRow
mibmediaGatewayProfile_MgcAddressEntry = _MibmediaGatewayProfile_MgcAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 4, 1)
)
mibmediaGatewayProfile_MgcAddressEntry.setIndexNames(
    (0, "ASCEND-MIBMGW-MIB", "mediaGatewayProfile-MgcAddress-Name"),
    (0, "ASCEND-MIBMGW-MIB", "mediaGatewayProfile-MgcAddress-Index-o"),
)
if mibBuilder.loadTexts:
    mibmediaGatewayProfile_MgcAddressEntry.setStatus("mandatory")
_MediaGatewayProfile_MgcAddress_Name_Type = DisplayString
_MediaGatewayProfile_MgcAddress_Name_Object = MibScalar
mediaGatewayProfile_MgcAddress_Name = _MediaGatewayProfile_MgcAddress_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 4, 1, 1),
    _MediaGatewayProfile_MgcAddress_Name_Type()
)
mediaGatewayProfile_MgcAddress_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaGatewayProfile_MgcAddress_Name.setStatus("mandatory")
_MediaGatewayProfile_MgcAddress_Index_o_Type = Integer32
_MediaGatewayProfile_MgcAddress_Index_o_Object = MibScalar
mediaGatewayProfile_MgcAddress_Index_o = _MediaGatewayProfile_MgcAddress_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 4, 1, 2),
    _MediaGatewayProfile_MgcAddress_Index_o_Type()
)
mediaGatewayProfile_MgcAddress_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaGatewayProfile_MgcAddress_Index_o.setStatus("mandatory")
_MediaGatewayProfile_MgcAddress_Vrouter_Type = DisplayString
_MediaGatewayProfile_MgcAddress_Vrouter_Object = MibScalar
mediaGatewayProfile_MgcAddress_Vrouter = _MediaGatewayProfile_MgcAddress_Vrouter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 4, 1, 3),
    _MediaGatewayProfile_MgcAddress_Vrouter_Type()
)
mediaGatewayProfile_MgcAddress_Vrouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_MgcAddress_Vrouter.setStatus("mandatory")
_MediaGatewayProfile_MgcAddress_IpAddress_Type = IpAddress
_MediaGatewayProfile_MgcAddress_IpAddress_Object = MibScalar
mediaGatewayProfile_MgcAddress_IpAddress = _MediaGatewayProfile_MgcAddress_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 4, 1, 4),
    _MediaGatewayProfile_MgcAddress_IpAddress_Type()
)
mediaGatewayProfile_MgcAddress_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_MgcAddress_IpAddress.setStatus("mandatory")
_MediaGatewayProfile_MgcAddress_PortNumber_Type = Integer32
_MediaGatewayProfile_MgcAddress_PortNumber_Object = MibScalar
mediaGatewayProfile_MgcAddress_PortNumber = _MediaGatewayProfile_MgcAddress_PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 170, 4, 1, 5),
    _MediaGatewayProfile_MgcAddress_PortNumber_Type()
)
mediaGatewayProfile_MgcAddress_PortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGatewayProfile_MgcAddress_PortNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBMGW-MIB",
    **{"DisplayString": DisplayString,
       "mibmediaGatewayProfile": mibmediaGatewayProfile,
       "mibmediaGatewayProfileTable": mibmediaGatewayProfileTable,
       "mibmediaGatewayProfileEntry": mibmediaGatewayProfileEntry,
       "mediaGatewayProfile-Name": mediaGatewayProfile_Name,
       "mediaGatewayProfile-Active": mediaGatewayProfile_Active,
       "mediaGatewayProfile-ProtocolType": mediaGatewayProfile_ProtocolType,
       "mediaGatewayProfile-MgSigAddress-Type": mediaGatewayProfile_MgSigAddress_Type,
       "mediaGatewayProfile-MgSigAddress-IpAddress": mediaGatewayProfile_MgSigAddress_IpAddress,
       "mediaGatewayProfile-MgRtpAddress-Type": mediaGatewayProfile_MgRtpAddress_Type,
       "mediaGatewayProfile-MgRtpAddress-IpAddress": mediaGatewayProfile_MgRtpAddress_IpAddress,
       "mediaGatewayProfile-H248Options-EncodingFormat": mediaGatewayProfile_H248Options_EncodingFormat,
       "mediaGatewayProfile-H248Options-MaxResponseTime": mediaGatewayProfile_H248Options_MaxResponseTime,
       "mediaGatewayProfile-H248Options-Heartbeat-Enabled": mediaGatewayProfile_H248Options_Heartbeat_Enabled,
       "mediaGatewayProfile-H248Options-Heartbeat-Interval": mediaGatewayProfile_H248Options_Heartbeat_Interval,
       "mediaGatewayProfile-H248Options-DigitmapOptions-StartTimer": mediaGatewayProfile_H248Options_DigitmapOptions_StartTimer,
       "mediaGatewayProfile-H248Options-DigitmapOptions-ShortTimer": mediaGatewayProfile_H248Options_DigitmapOptions_ShortTimer,
       "mediaGatewayProfile-H248Options-DigitmapOptions-LongTimer": mediaGatewayProfile_H248Options_DigitmapOptions_LongTimer,
       "mediaGatewayProfile-IpdcOptions-BayId": mediaGatewayProfile_IpdcOptions_BayId,
       "mediaGatewayProfile-IpdcOptions-SystemType": mediaGatewayProfile_IpdcOptions_SystemType,
       "mediaGatewayProfile-TransportOptions-Type": mediaGatewayProfile_TransportOptions_Type,
       "mediaGatewayProfile-VoipOptions-PacketAudioMode": mediaGatewayProfile_VoipOptions_PacketAudioMode,
       "mediaGatewayProfile-VoipOptions-FramesPerPacket": mediaGatewayProfile_VoipOptions_FramesPerPacket,
       "mediaGatewayProfile-VoipOptions-SilenceDetCng": mediaGatewayProfile_VoipOptions_SilenceDetCng,
       "mediaGatewayProfile-VoipOptions-EnaAdapJitterBuffer": mediaGatewayProfile_VoipOptions_EnaAdapJitterBuffer,
       "mediaGatewayProfile-VoipOptions-MaxJitterBufferSize": mediaGatewayProfile_VoipOptions_MaxJitterBufferSize,
       "mediaGatewayProfile-VoipOptions-InitialJitterBufferSize": mediaGatewayProfile_VoipOptions_InitialJitterBufferSize,
       "mediaGatewayProfile-VoipOptions-VoiceAnnDir": mediaGatewayProfile_VoipOptions_VoiceAnnDir,
       "mediaGatewayProfile-VoipOptions-VoiceAnnEnc": mediaGatewayProfile_VoipOptions_VoiceAnnEnc,
       "mediaGatewayProfile-VoipOptions-CallInterDigitTimeout": mediaGatewayProfile_VoipOptions_CallInterDigitTimeout,
       "mediaGatewayProfile-VoipOptions-SilenceThreshold": mediaGatewayProfile_VoipOptions_SilenceThreshold,
       "mediaGatewayProfile-VoipOptions-DtmfTonePassing": mediaGatewayProfile_VoipOptions_DtmfTonePassing,
       "mediaGatewayProfile-VoipOptions-Maxcalls": mediaGatewayProfile_VoipOptions_Maxcalls,
       "mediaGatewayProfile-VoipOptions-Rfc2833PayloadType": mediaGatewayProfile_VoipOptions_Rfc2833PayloadType,
       "mediaGatewayProfile-VoipOptions-G711TransparentData": mediaGatewayProfile_VoipOptions_G711TransparentData,
       "mediaGatewayProfile-DialedGwOptions-CallHairpin": mediaGatewayProfile_DialedGwOptions_CallHairpin,
       "mediaGatewayProfile-DialedGwOptions-TrunkQuiesce": mediaGatewayProfile_DialedGwOptions_TrunkQuiesce,
       "mediaGatewayProfile-DialedGwOptions-TrunkPrefix": mediaGatewayProfile_DialedGwOptions_TrunkPrefix,
       "mediaGatewayProfile-DialedGwOptions-StartLocalRingTone": mediaGatewayProfile_DialedGwOptions_StartLocalRingTone,
       "mediaGatewayProfile-DialedGwOptions-MediaWaitForConnect": mediaGatewayProfile_DialedGwOptions_MediaWaitForConnect,
       "mediaGatewayProfile-RtFaxOptions-RtFaxEnable": mediaGatewayProfile_RtFaxOptions_RtFaxEnable,
       "mediaGatewayProfile-RtFaxOptions-EcmEnable": mediaGatewayProfile_RtFaxOptions_EcmEnable,
       "mediaGatewayProfile-RtFaxOptions-LowLatencyMode": mediaGatewayProfile_RtFaxOptions_LowLatencyMode,
       "mediaGatewayProfile-RtFaxOptions-CommandSpoof": mediaGatewayProfile_RtFaxOptions_CommandSpoof,
       "mediaGatewayProfile-RtFaxOptions-LocalRetransmitLsf": mediaGatewayProfile_RtFaxOptions_LocalRetransmitLsf,
       "mediaGatewayProfile-RtFaxOptions-PacketRedundancy": mediaGatewayProfile_RtFaxOptions_PacketRedundancy,
       "mediaGatewayProfile-RtFaxOptions-FixedPackets": mediaGatewayProfile_RtFaxOptions_FixedPackets,
       "mediaGatewayProfile-RtFaxOptions-MaxDataRate": mediaGatewayProfile_RtFaxOptions_MaxDataRate,
       "mediaGatewayProfile-RtFaxOptions-AllowCtc": mediaGatewayProfile_RtFaxOptions_AllowCtc,
       "mediaGatewayProfile-TosRtpOptions-Active": mediaGatewayProfile_TosRtpOptions_Active,
       "mediaGatewayProfile-TosRtpOptions-Precedence": mediaGatewayProfile_TosRtpOptions_Precedence,
       "mediaGatewayProfile-TosRtpOptions-TypeOfService": mediaGatewayProfile_TosRtpOptions_TypeOfService,
       "mediaGatewayProfile-TosRtpOptions-ApplyTo": mediaGatewayProfile_TosRtpOptions_ApplyTo,
       "mediaGatewayProfile-TosRtpOptions-MarkingType": mediaGatewayProfile_TosRtpOptions_MarkingType,
       "mediaGatewayProfile-TosRtpOptions-Dscp": mediaGatewayProfile_TosRtpOptions_Dscp,
       "mediaGatewayProfile-SipOptions-T1Timer": mediaGatewayProfile_SipOptions_T1Timer,
       "mediaGatewayProfile-SipOptions-T2Timer": mediaGatewayProfile_SipOptions_T2Timer,
       "mediaGatewayProfile-SipOptions-InviteRetries": mediaGatewayProfile_SipOptions_InviteRetries,
       "mediaGatewayProfile-SipOptions-NonInviteRetries": mediaGatewayProfile_SipOptions_NonInviteRetries,
       "mediaGatewayProfile-SipOptions-PrimaryProxy-IpAddress": mediaGatewayProfile_SipOptions_PrimaryProxy_IpAddress,
       "mediaGatewayProfile-SipOptions-PrimaryProxy-Name": mediaGatewayProfile_SipOptions_PrimaryProxy_Name,
       "mediaGatewayProfile-SipOptions-PrimaryProxy-PortNumber": mediaGatewayProfile_SipOptions_PrimaryProxy_PortNumber,
       "mediaGatewayProfile-SipOptions-PrimaryProxy-MessageFormat": mediaGatewayProfile_SipOptions_PrimaryProxy_MessageFormat,
       "mediaGatewayProfile-SipOptions-SecondaryProxy-IpAddress": mediaGatewayProfile_SipOptions_SecondaryProxy_IpAddress,
       "mediaGatewayProfile-SipOptions-SecondaryProxy-Name": mediaGatewayProfile_SipOptions_SecondaryProxy_Name,
       "mediaGatewayProfile-SipOptions-SecondaryProxy-PortNumber": mediaGatewayProfile_SipOptions_SecondaryProxy_PortNumber,
       "mediaGatewayProfile-SipOptions-SecondaryProxy-MessageFormat": mediaGatewayProfile_SipOptions_SecondaryProxy_MessageFormat,
       "mediaGatewayProfile-SipOptions-RegistrationProxy-IpAddress": mediaGatewayProfile_SipOptions_RegistrationProxy_IpAddress,
       "mediaGatewayProfile-SipOptions-RegistrationProxy-Name": mediaGatewayProfile_SipOptions_RegistrationProxy_Name,
       "mediaGatewayProfile-SipOptions-RegistrationProxy-PortNumber": mediaGatewayProfile_SipOptions_RegistrationProxy_PortNumber,
       "mediaGatewayProfile-SipOptions-RegistrationProxy-MessageFormat": mediaGatewayProfile_SipOptions_RegistrationProxy_MessageFormat,
       "mediaGatewayProfile-SipOptions-RegistrationProxy-RegisterInterval": mediaGatewayProfile_SipOptions_RegistrationProxy_RegisterInterval,
       "mediaGatewayProfile-SipOptions-TrustedProxy-AuthenticateMessages": mediaGatewayProfile_SipOptions_TrustedProxy_AuthenticateMessages,
       "mediaGatewayProfile-SipOptions-UnknownAni": mediaGatewayProfile_SipOptions_UnknownAni,
       "mediaGatewayProfile-SipOptions-BlockedAni": mediaGatewayProfile_SipOptions_BlockedAni,
       "mediaGatewayProfile-SipOptions-OnholdMinutes": mediaGatewayProfile_SipOptions_OnholdMinutes,
       "mediaGatewayProfile-SipOptions-Support100rel": mediaGatewayProfile_SipOptions_Support100rel,
       "mediaGatewayProfile-SipOptions-Internationalize": mediaGatewayProfile_SipOptions_Internationalize,
       "mediaGatewayProfile-SipOptions-InternationalPrefix": mediaGatewayProfile_SipOptions_InternationalPrefix,
       "mediaGatewayProfile-SipOptions-CountryCode": mediaGatewayProfile_SipOptions_CountryCode,
       "mediaGatewayProfile-SipOptions-NationalDestinationCode": mediaGatewayProfile_SipOptions_NationalDestinationCode,
       "mediaGatewayProfile-Action-o": mediaGatewayProfile_Action_o,
       "mediaGatewayProfile-VoipOptions-RtpProblemReporting-Enable": mediaGatewayProfile_VoipOptions_RtpProblemReporting_Enable,
       "mediaGatewayProfile-VoipOptions-RtpProblemReporting-MultMediaRcptOkTime": mediaGatewayProfile_VoipOptions_RtpProblemReporting_MultMediaRcptOkTime,
       "mediaGatewayProfile-VoipOptions-RtpProblemReporting-NoMediaRcptOkTime": mediaGatewayProfile_VoipOptions_RtpProblemReporting_NoMediaRcptOkTime,
       "mediaGatewayProfile-TosSigOptions-Active": mediaGatewayProfile_TosSigOptions_Active,
       "mediaGatewayProfile-TosSigOptions-Precedence": mediaGatewayProfile_TosSigOptions_Precedence,
       "mediaGatewayProfile-TosSigOptions-TypeOfService": mediaGatewayProfile_TosSigOptions_TypeOfService,
       "mediaGatewayProfile-TosSigOptions-ApplyTo": mediaGatewayProfile_TosSigOptions_ApplyTo,
       "mediaGatewayProfile-TosSigOptions-MarkingType": mediaGatewayProfile_TosSigOptions_MarkingType,
       "mediaGatewayProfile-TosSigOptions-Dscp": mediaGatewayProfile_TosSigOptions_Dscp,
       "mediaGatewayProfile-SipOptions-PrivacyProxyRequire": mediaGatewayProfile_SipOptions_PrivacyProxyRequire,
       "mediaGatewayProfile-SipOptions-CallTransferMethod": mediaGatewayProfile_SipOptions_CallTransferMethod,
       "mediaGatewayProfile-SipOptions-NotifyTimer": mediaGatewayProfile_SipOptions_NotifyTimer,
       "mediaGatewayProfile-Voip2ipOptions-DtmfTonePassing": mediaGatewayProfile_Voip2ipOptions_DtmfTonePassing,
       "mediaGatewayProfile-Voip2ipOptions-RtpTranslatorMode": mediaGatewayProfile_Voip2ipOptions_RtpTranslatorMode,
       "mediaGatewayProfile-Voip2ipOptions-MaxNumErasures": mediaGatewayProfile_Voip2ipOptions_MaxNumErasures,
       "mediaGatewayProfile-Voip2ipOptions-JitterBufferSize": mediaGatewayProfile_Voip2ipOptions_JitterBufferSize,
       "mibmediaGatewayProfile-SipOptions-TrustedProxy-TableTable": mibmediaGatewayProfile_SipOptions_TrustedProxy_TableTable,
       "mibmediaGatewayProfile-SipOptions-TrustedProxy-TableEntry": mibmediaGatewayProfile_SipOptions_TrustedProxy_TableEntry,
       "mediaGatewayProfile-SipOptions-TrustedProxy-Table-Name": mediaGatewayProfile_SipOptions_TrustedProxy_Table_Name,
       "mediaGatewayProfile-SipOptions-TrustedProxy-Table-Index-o": mediaGatewayProfile_SipOptions_TrustedProxy_Table_Index_o,
       "mediaGatewayProfile-SipOptions-TrustedProxy-Table-HostName": mediaGatewayProfile_SipOptions_TrustedProxy_Table_HostName,
       "mediaGatewayProfile-SipOptions-TrustedProxy-Table-IpAddress": mediaGatewayProfile_SipOptions_TrustedProxy_Table_IpAddress,
       "mibmediaGatewayProfile-H248Options-DigitmapOptions-MapTable": mibmediaGatewayProfile_H248Options_DigitmapOptions_MapTable,
       "mibmediaGatewayProfile-H248Options-DigitmapOptions-MapEntry": mibmediaGatewayProfile_H248Options_DigitmapOptions_MapEntry,
       "mediaGatewayProfile-H248Options-DigitmapOptions-Map-Name": mediaGatewayProfile_H248Options_DigitmapOptions_Map_Name,
       "mediaGatewayProfile-H248Options-DigitmapOptions-Map-Index-o": mediaGatewayProfile_H248Options_DigitmapOptions_Map_Index_o,
       "mediaGatewayProfile-H248Options-DigitmapOptions-Map-ReferenceName": mediaGatewayProfile_H248Options_DigitmapOptions_Map_ReferenceName,
       "mediaGatewayProfile-H248Options-DigitmapOptions-Map-Value": mediaGatewayProfile_H248Options_DigitmapOptions_Map_Value,
       "mibmediaGatewayProfile-MgcAddressTable": mibmediaGatewayProfile_MgcAddressTable,
       "mibmediaGatewayProfile-MgcAddressEntry": mibmediaGatewayProfile_MgcAddressEntry,
       "mediaGatewayProfile-MgcAddress-Name": mediaGatewayProfile_MgcAddress_Name,
       "mediaGatewayProfile-MgcAddress-Index-o": mediaGatewayProfile_MgcAddress_Index_o,
       "mediaGatewayProfile-MgcAddress-Vrouter": mediaGatewayProfile_MgcAddress_Vrouter,
       "mediaGatewayProfile-MgcAddress-IpAddress": mediaGatewayProfile_MgcAddress_IpAddress,
       "mediaGatewayProfile-MgcAddress-PortNumber": mediaGatewayProfile_MgcAddress_PortNumber}
)
