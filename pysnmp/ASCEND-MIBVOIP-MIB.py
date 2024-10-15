# SNMP MIB module (ASCEND-MIBVOIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBVOIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:33 2024
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

_MibvoipProfile_ObjectIdentity = ObjectIdentity
mibvoipProfile = _MibvoipProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 138)
)
_MibvoipProfileTable_Object = MibTable
mibvoipProfileTable = _MibvoipProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1)
)
if mibBuilder.loadTexts:
    mibvoipProfileTable.setStatus("mandatory")
_MibvoipProfileEntry_Object = MibTableRow
mibvoipProfileEntry = _MibvoipProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1)
)
mibvoipProfileEntry.setIndexNames(
    (0, "ASCEND-MIBVOIP-MIB", "voipProfile-VoipIndex-GatewayAccessNumber"),
    (0, "ASCEND-MIBVOIP-MIB", "voipProfile-VoipIndex-FarEndNumber"),
)
if mibBuilder.loadTexts:
    mibvoipProfileEntry.setStatus("mandatory")
_VoipProfile_VoipIndex_GatewayAccessNumber_Type = DisplayString
_VoipProfile_VoipIndex_GatewayAccessNumber_Object = MibScalar
voipProfile_VoipIndex_GatewayAccessNumber = _VoipProfile_VoipIndex_GatewayAccessNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 1),
    _VoipProfile_VoipIndex_GatewayAccessNumber_Type()
)
voipProfile_VoipIndex_GatewayAccessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipProfile_VoipIndex_GatewayAccessNumber.setStatus("mandatory")
_VoipProfile_VoipIndex_FarEndNumber_Type = DisplayString
_VoipProfile_VoipIndex_FarEndNumber_Object = MibScalar
voipProfile_VoipIndex_FarEndNumber = _VoipProfile_VoipIndex_FarEndNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 2),
    _VoipProfile_VoipIndex_FarEndNumber_Type()
)
voipProfile_VoipIndex_FarEndNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipProfile_VoipIndex_FarEndNumber.setStatus("mandatory")
_VoipProfile_GatekeeperIp_Type = IpAddress
_VoipProfile_GatekeeperIp_Object = MibScalar
voipProfile_GatekeeperIp = _VoipProfile_GatekeeperIp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 3),
    _VoipProfile_GatekeeperIp_Type()
)
voipProfile_GatekeeperIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_GatekeeperIp.setStatus("mandatory")


class _VoipProfile_GkMlgControl_Type(Integer32):
    """Custom type voipProfile_GkMlgControl based on Integer32"""
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


_VoipProfile_GkMlgControl_Type.__name__ = "Integer32"
_VoipProfile_GkMlgControl_Object = MibScalar
voipProfile_GkMlgControl = _VoipProfile_GkMlgControl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 4),
    _VoipProfile_GkMlgControl_Type()
)
voipProfile_GkMlgControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_GkMlgControl.setStatus("mandatory")


class _VoipProfile_VpnMode_Type(Integer32):
    """Custom type voipProfile_VpnMode based on Integer32"""
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


_VoipProfile_VpnMode_Type.__name__ = "Integer32"
_VoipProfile_VpnMode_Object = MibScalar
voipProfile_VpnMode = _VoipProfile_VpnMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 5),
    _VoipProfile_VpnMode_Type()
)
voipProfile_VpnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_VpnMode.setStatus("mandatory")


class _VoipProfile_SingleDialEnable_Type(Integer32):
    """Custom type voipProfile_SingleDialEnable based on Integer32"""
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


_VoipProfile_SingleDialEnable_Type.__name__ = "Integer32"
_VoipProfile_SingleDialEnable_Object = MibScalar
voipProfile_SingleDialEnable = _VoipProfile_SingleDialEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 6),
    _VoipProfile_SingleDialEnable_Type()
)
voipProfile_SingleDialEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_SingleDialEnable.setStatus("mandatory")


class _VoipProfile_PacketAudioMode_Type(Integer32):
    """Custom type voipProfile_PacketAudioMode based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("evrc", 9),
          ("frgsm", 8),
          ("g711Alaw", 2),
          ("g711Ulaw", 1),
          ("g723", 3),
          ("g72364kps", 5),
          ("g728", 7),
          ("g729", 4),
          ("rt24", 6))
    )


_VoipProfile_PacketAudioMode_Type.__name__ = "Integer32"
_VoipProfile_PacketAudioMode_Object = MibScalar
voipProfile_PacketAudioMode = _VoipProfile_PacketAudioMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 7),
    _VoipProfile_PacketAudioMode_Type()
)
voipProfile_PacketAudioMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_PacketAudioMode.setStatus("mandatory")
_VoipProfile_FramesPerPacket_Type = Integer32
_VoipProfile_FramesPerPacket_Object = MibScalar
voipProfile_FramesPerPacket = _VoipProfile_FramesPerPacket_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 8),
    _VoipProfile_FramesPerPacket_Type()
)
voipProfile_FramesPerPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_FramesPerPacket.setStatus("mandatory")


class _VoipProfile_TosOptions_Active_Type(Integer32):
    """Custom type voipProfile_TosOptions_Active based on Integer32"""
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


_VoipProfile_TosOptions_Active_Type.__name__ = "Integer32"
_VoipProfile_TosOptions_Active_Object = MibScalar
voipProfile_TosOptions_Active = _VoipProfile_TosOptions_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 9),
    _VoipProfile_TosOptions_Active_Type()
)
voipProfile_TosOptions_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_TosOptions_Active.setStatus("mandatory")


class _VoipProfile_TosOptions_Precedence_Type(Integer32):
    """Custom type voipProfile_TosOptions_Precedence based on Integer32"""
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


_VoipProfile_TosOptions_Precedence_Type.__name__ = "Integer32"
_VoipProfile_TosOptions_Precedence_Object = MibScalar
voipProfile_TosOptions_Precedence = _VoipProfile_TosOptions_Precedence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 10),
    _VoipProfile_TosOptions_Precedence_Type()
)
voipProfile_TosOptions_Precedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_TosOptions_Precedence.setStatus("mandatory")


class _VoipProfile_TosOptions_TypeOfService_Type(Integer32):
    """Custom type voipProfile_TosOptions_TypeOfService based on Integer32"""
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


_VoipProfile_TosOptions_TypeOfService_Type.__name__ = "Integer32"
_VoipProfile_TosOptions_TypeOfService_Object = MibScalar
voipProfile_TosOptions_TypeOfService = _VoipProfile_TosOptions_TypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 11),
    _VoipProfile_TosOptions_TypeOfService_Type()
)
voipProfile_TosOptions_TypeOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_TosOptions_TypeOfService.setStatus("mandatory")


class _VoipProfile_TosOptions_ApplyTo_Type(Integer32):
    """Custom type voipProfile_TosOptions_ApplyTo based on Integer32"""
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


_VoipProfile_TosOptions_ApplyTo_Type.__name__ = "Integer32"
_VoipProfile_TosOptions_ApplyTo_Object = MibScalar
voipProfile_TosOptions_ApplyTo = _VoipProfile_TosOptions_ApplyTo_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 12),
    _VoipProfile_TosOptions_ApplyTo_Type()
)
voipProfile_TosOptions_ApplyTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_TosOptions_ApplyTo.setStatus("mandatory")


class _VoipProfile_SilenceDetCng_Type(Integer32):
    """Custom type voipProfile_SilenceDetCng based on Integer32"""
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


_VoipProfile_SilenceDetCng_Type.__name__ = "Integer32"
_VoipProfile_SilenceDetCng_Object = MibScalar
voipProfile_SilenceDetCng = _VoipProfile_SilenceDetCng_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 13),
    _VoipProfile_SilenceDetCng_Type()
)
voipProfile_SilenceDetCng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_SilenceDetCng.setStatus("mandatory")
_VoipProfile_GatekeeperIpSec_Type = IpAddress
_VoipProfile_GatekeeperIpSec_Object = MibScalar
voipProfile_GatekeeperIpSec = _VoipProfile_GatekeeperIpSec_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 14),
    _VoipProfile_GatekeeperIpSec_Type()
)
voipProfile_GatekeeperIpSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_GatekeeperIpSec.setStatus("mandatory")
_VoipProfile_GatekeeperKeepalive_Type = Integer32
_VoipProfile_GatekeeperKeepalive_Object = MibScalar
voipProfile_GatekeeperKeepalive = _VoipProfile_GatekeeperKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 15),
    _VoipProfile_GatekeeperKeepalive_Type()
)
voipProfile_GatekeeperKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_GatekeeperKeepalive.setStatus("mandatory")
_VoipProfile_RegistrationRetries_Type = Integer32
_VoipProfile_RegistrationRetries_Object = MibScalar
voipProfile_RegistrationRetries = _VoipProfile_RegistrationRetries_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 16),
    _VoipProfile_RegistrationRetries_Type()
)
voipProfile_RegistrationRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_RegistrationRetries.setStatus("mandatory")
_VoipProfile_RegistrationRetryTimer_Type = Integer32
_VoipProfile_RegistrationRetryTimer_Object = MibScalar
voipProfile_RegistrationRetryTimer = _VoipProfile_RegistrationRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 17),
    _VoipProfile_RegistrationRetryTimer_Type()
)
voipProfile_RegistrationRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_RegistrationRetryTimer.setStatus("mandatory")
_VoipProfile_PrimaryRetries_Type = Integer32
_VoipProfile_PrimaryRetries_Object = MibScalar
voipProfile_PrimaryRetries = _VoipProfile_PrimaryRetries_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 18),
    _VoipProfile_PrimaryRetries_Type()
)
voipProfile_PrimaryRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_PrimaryRetries.setStatus("mandatory")


class _VoipProfile_EnaAdapJitterBuffer_Type(Integer32):
    """Custom type voipProfile_EnaAdapJitterBuffer based on Integer32"""
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


_VoipProfile_EnaAdapJitterBuffer_Type.__name__ = "Integer32"
_VoipProfile_EnaAdapJitterBuffer_Object = MibScalar
voipProfile_EnaAdapJitterBuffer = _VoipProfile_EnaAdapJitterBuffer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 19),
    _VoipProfile_EnaAdapJitterBuffer_Type()
)
voipProfile_EnaAdapJitterBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_EnaAdapJitterBuffer.setStatus("mandatory")
_VoipProfile_MaxJitterBufferSize_Type = Integer32
_VoipProfile_MaxJitterBufferSize_Object = MibScalar
voipProfile_MaxJitterBufferSize = _VoipProfile_MaxJitterBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 20),
    _VoipProfile_MaxJitterBufferSize_Type()
)
voipProfile_MaxJitterBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_MaxJitterBufferSize.setStatus("mandatory")
_VoipProfile_InitialJitterBufferSize_Type = Integer32
_VoipProfile_InitialJitterBufferSize_Object = MibScalar
voipProfile_InitialJitterBufferSize = _VoipProfile_InitialJitterBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 21),
    _VoipProfile_InitialJitterBufferSize_Type()
)
voipProfile_InitialJitterBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_InitialJitterBufferSize.setStatus("mandatory")
_VoipProfile_Maxcalls_Type = Integer32
_VoipProfile_Maxcalls_Object = MibScalar
voipProfile_Maxcalls = _VoipProfile_Maxcalls_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 22),
    _VoipProfile_Maxcalls_Type()
)
voipProfile_Maxcalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_Maxcalls.setStatus("mandatory")


class _VoipProfile_CutThruEnableNearend_Type(Integer32):
    """Custom type voipProfile_CutThruEnableNearend based on Integer32"""
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


_VoipProfile_CutThruEnableNearend_Type.__name__ = "Integer32"
_VoipProfile_CutThruEnableNearend_Object = MibScalar
voipProfile_CutThruEnableNearend = _VoipProfile_CutThruEnableNearend_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 23),
    _VoipProfile_CutThruEnableNearend_Type()
)
voipProfile_CutThruEnableNearend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_CutThruEnableNearend.setStatus("mandatory")


class _VoipProfile_H323VoiceAnnEnabled_Type(Integer32):
    """Custom type voipProfile_H323VoiceAnnEnabled based on Integer32"""
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


_VoipProfile_H323VoiceAnnEnabled_Type.__name__ = "Integer32"
_VoipProfile_H323VoiceAnnEnabled_Object = MibScalar
voipProfile_H323VoiceAnnEnabled = _VoipProfile_H323VoiceAnnEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 24),
    _VoipProfile_H323VoiceAnnEnabled_Type()
)
voipProfile_H323VoiceAnnEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_H323VoiceAnnEnabled.setStatus("mandatory")
_VoipProfile_VoiceAnnDir_Type = DisplayString
_VoipProfile_VoiceAnnDir_Object = MibScalar
voipProfile_VoiceAnnDir = _VoipProfile_VoiceAnnDir_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 25),
    _VoipProfile_VoiceAnnDir_Type()
)
voipProfile_VoiceAnnDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_VoiceAnnDir.setStatus("mandatory")


class _VoipProfile_VoiceAnnEnc_Type(Integer32):
    """Custom type voipProfile_VoiceAnnEnc based on Integer32"""
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


_VoipProfile_VoiceAnnEnc_Type.__name__ = "Integer32"
_VoipProfile_VoiceAnnEnc_Object = MibScalar
voipProfile_VoiceAnnEnc = _VoipProfile_VoiceAnnEnc_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 26),
    _VoipProfile_VoiceAnnEnc_Type()
)
voipProfile_VoiceAnnEnc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_VoiceAnnEnc.setStatus("mandatory")
_VoipProfile_CallInterDigitTimeout_Type = Integer32
_VoipProfile_CallInterDigitTimeout_Object = MibScalar
voipProfile_CallInterDigitTimeout = _VoipProfile_CallInterDigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 27),
    _VoipProfile_CallInterDigitTimeout_Type()
)
voipProfile_CallInterDigitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_CallInterDigitTimeout.setStatus("mandatory")
_VoipProfile_SilenceThreshold_Type = Integer32
_VoipProfile_SilenceThreshold_Object = MibScalar
voipProfile_SilenceThreshold = _VoipProfile_SilenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 28),
    _VoipProfile_SilenceThreshold_Type()
)
voipProfile_SilenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_SilenceThreshold.setStatus("mandatory")


class _VoipProfile_DtmfTonePassing_Type(Integer32):
    """Custom type voipProfile_DtmfTonePassing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dtmfTonePassedInband", 1),
          ("dtmfTonePassedOutofband", 2),
          ("rfc2833", 3))
    )


_VoipProfile_DtmfTonePassing_Type.__name__ = "Integer32"
_VoipProfile_DtmfTonePassing_Object = MibScalar
voipProfile_DtmfTonePassing = _VoipProfile_DtmfTonePassing_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 29),
    _VoipProfile_DtmfTonePassing_Type()
)
voipProfile_DtmfTonePassing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_DtmfTonePassing.setStatus("mandatory")
_VoipProfile_VoiceAnnServIp_Type = IpAddress
_VoipProfile_VoiceAnnServIp_Object = MibScalar
voipProfile_VoiceAnnServIp = _VoipProfile_VoiceAnnServIp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 30),
    _VoipProfile_VoiceAnnServIp_Type()
)
voipProfile_VoiceAnnServIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_VoiceAnnServIp.setStatus("mandatory")
_VoipProfile_VoiceAnnFileSpec_Type = DisplayString
_VoipProfile_VoiceAnnFileSpec_Object = MibScalar
voipProfile_VoiceAnnFileSpec = _VoipProfile_VoiceAnnFileSpec_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 31),
    _VoipProfile_VoiceAnnFileSpec_Type()
)
voipProfile_VoiceAnnFileSpec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_VoiceAnnFileSpec.setStatus("mandatory")


class _VoipProfile_RtFaxOptions_RtFaxEnable_Type(Integer32):
    """Custom type voipProfile_RtFaxOptions_RtFaxEnable based on Integer32"""
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


_VoipProfile_RtFaxOptions_RtFaxEnable_Type.__name__ = "Integer32"
_VoipProfile_RtFaxOptions_RtFaxEnable_Object = MibScalar
voipProfile_RtFaxOptions_RtFaxEnable = _VoipProfile_RtFaxOptions_RtFaxEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 32),
    _VoipProfile_RtFaxOptions_RtFaxEnable_Type()
)
voipProfile_RtFaxOptions_RtFaxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_RtFaxOptions_RtFaxEnable.setStatus("mandatory")


class _VoipProfile_RtFaxOptions_EcmEnable_Type(Integer32):
    """Custom type voipProfile_RtFaxOptions_EcmEnable based on Integer32"""
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


_VoipProfile_RtFaxOptions_EcmEnable_Type.__name__ = "Integer32"
_VoipProfile_RtFaxOptions_EcmEnable_Object = MibScalar
voipProfile_RtFaxOptions_EcmEnable = _VoipProfile_RtFaxOptions_EcmEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 33),
    _VoipProfile_RtFaxOptions_EcmEnable_Type()
)
voipProfile_RtFaxOptions_EcmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_RtFaxOptions_EcmEnable.setStatus("mandatory")


class _VoipProfile_RtFaxOptions_LowLatencyMode_Type(Integer32):
    """Custom type voipProfile_RtFaxOptions_LowLatencyMode based on Integer32"""
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


_VoipProfile_RtFaxOptions_LowLatencyMode_Type.__name__ = "Integer32"
_VoipProfile_RtFaxOptions_LowLatencyMode_Object = MibScalar
voipProfile_RtFaxOptions_LowLatencyMode = _VoipProfile_RtFaxOptions_LowLatencyMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 34),
    _VoipProfile_RtFaxOptions_LowLatencyMode_Type()
)
voipProfile_RtFaxOptions_LowLatencyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_RtFaxOptions_LowLatencyMode.setStatus("mandatory")


class _VoipProfile_RtFaxOptions_CommandSpoof_Type(Integer32):
    """Custom type voipProfile_RtFaxOptions_CommandSpoof based on Integer32"""
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


_VoipProfile_RtFaxOptions_CommandSpoof_Type.__name__ = "Integer32"
_VoipProfile_RtFaxOptions_CommandSpoof_Object = MibScalar
voipProfile_RtFaxOptions_CommandSpoof = _VoipProfile_RtFaxOptions_CommandSpoof_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 35),
    _VoipProfile_RtFaxOptions_CommandSpoof_Type()
)
voipProfile_RtFaxOptions_CommandSpoof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_RtFaxOptions_CommandSpoof.setStatus("mandatory")


class _VoipProfile_RtFaxOptions_LocalRetransmitLsf_Type(Integer32):
    """Custom type voipProfile_RtFaxOptions_LocalRetransmitLsf based on Integer32"""
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


_VoipProfile_RtFaxOptions_LocalRetransmitLsf_Type.__name__ = "Integer32"
_VoipProfile_RtFaxOptions_LocalRetransmitLsf_Object = MibScalar
voipProfile_RtFaxOptions_LocalRetransmitLsf = _VoipProfile_RtFaxOptions_LocalRetransmitLsf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 36),
    _VoipProfile_RtFaxOptions_LocalRetransmitLsf_Type()
)
voipProfile_RtFaxOptions_LocalRetransmitLsf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_RtFaxOptions_LocalRetransmitLsf.setStatus("mandatory")
_VoipProfile_RtFaxOptions_PacketRedundancy_Type = Integer32
_VoipProfile_RtFaxOptions_PacketRedundancy_Object = MibScalar
voipProfile_RtFaxOptions_PacketRedundancy = _VoipProfile_RtFaxOptions_PacketRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 37),
    _VoipProfile_RtFaxOptions_PacketRedundancy_Type()
)
voipProfile_RtFaxOptions_PacketRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_RtFaxOptions_PacketRedundancy.setStatus("mandatory")


class _VoipProfile_RtFaxOptions_FixedPackets_Type(Integer32):
    """Custom type voipProfile_RtFaxOptions_FixedPackets based on Integer32"""
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


_VoipProfile_RtFaxOptions_FixedPackets_Type.__name__ = "Integer32"
_VoipProfile_RtFaxOptions_FixedPackets_Object = MibScalar
voipProfile_RtFaxOptions_FixedPackets = _VoipProfile_RtFaxOptions_FixedPackets_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 38),
    _VoipProfile_RtFaxOptions_FixedPackets_Type()
)
voipProfile_RtFaxOptions_FixedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_RtFaxOptions_FixedPackets.setStatus("mandatory")


class _VoipProfile_RtFaxOptions_MaxDataRate_Type(Integer32):
    """Custom type voipProfile_RtFaxOptions_MaxDataRate based on Integer32"""
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


_VoipProfile_RtFaxOptions_MaxDataRate_Type.__name__ = "Integer32"
_VoipProfile_RtFaxOptions_MaxDataRate_Object = MibScalar
voipProfile_RtFaxOptions_MaxDataRate = _VoipProfile_RtFaxOptions_MaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 39),
    _VoipProfile_RtFaxOptions_MaxDataRate_Type()
)
voipProfile_RtFaxOptions_MaxDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_RtFaxOptions_MaxDataRate.setStatus("mandatory")


class _VoipProfile_CallHairpin_Type(Integer32):
    """Custom type voipProfile_CallHairpin based on Integer32"""
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


_VoipProfile_CallHairpin_Type.__name__ = "Integer32"
_VoipProfile_CallHairpin_Object = MibScalar
voipProfile_CallHairpin = _VoipProfile_CallHairpin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 40),
    _VoipProfile_CallHairpin_Type()
)
voipProfile_CallHairpin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_CallHairpin.setStatus("mandatory")
_VoipProfile_CallKeepAliveTimeout_Type = Integer32
_VoipProfile_CallKeepAliveTimeout_Object = MibScalar
voipProfile_CallKeepAliveTimeout = _VoipProfile_CallKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 41),
    _VoipProfile_CallKeepAliveTimeout_Type()
)
voipProfile_CallKeepAliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_CallKeepAliveTimeout.setStatus("mandatory")


class _VoipProfile_ClidSuppress_Type(Integer32):
    """Custom type voipProfile_ClidSuppress based on Integer32"""
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


_VoipProfile_ClidSuppress_Type.__name__ = "Integer32"
_VoipProfile_ClidSuppress_Object = MibScalar
voipProfile_ClidSuppress = _VoipProfile_ClidSuppress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 42),
    _VoipProfile_ClidSuppress_Type()
)
voipProfile_ClidSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_ClidSuppress.setStatus("mandatory")


class _VoipProfile_TrueConnectEnable_Type(Integer32):
    """Custom type voipProfile_TrueConnectEnable based on Integer32"""
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


_VoipProfile_TrueConnectEnable_Type.__name__ = "Integer32"
_VoipProfile_TrueConnectEnable_Object = MibScalar
voipProfile_TrueConnectEnable = _VoipProfile_TrueConnectEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 43),
    _VoipProfile_TrueConnectEnable_Type()
)
voipProfile_TrueConnectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_TrueConnectEnable.setStatus("mandatory")


class _VoipProfile_G711TransparentData_Type(Integer32):
    """Custom type voipProfile_G711TransparentData based on Integer32"""
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


_VoipProfile_G711TransparentData_Type.__name__ = "Integer32"
_VoipProfile_G711TransparentData_Object = MibScalar
voipProfile_G711TransparentData = _VoipProfile_G711TransparentData_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 44),
    _VoipProfile_G711TransparentData_Type()
)
voipProfile_G711TransparentData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_G711TransparentData.setStatus("mandatory")


class _VoipProfile_AllowG711Fallback_Type(Integer32):
    """Custom type voipProfile_AllowG711Fallback based on Integer32"""
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


_VoipProfile_AllowG711Fallback_Type.__name__ = "Integer32"
_VoipProfile_AllowG711Fallback_Object = MibScalar
voipProfile_AllowG711Fallback = _VoipProfile_AllowG711Fallback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 45),
    _VoipProfile_AllowG711Fallback_Type()
)
voipProfile_AllowG711Fallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_AllowG711Fallback.setStatus("mandatory")


class _VoipProfile_AllowCoderFallback_Type(Integer32):
    """Custom type voipProfile_AllowCoderFallback based on Integer32"""
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


_VoipProfile_AllowCoderFallback_Type.__name__ = "Integer32"
_VoipProfile_AllowCoderFallback_Object = MibScalar
voipProfile_AllowCoderFallback = _VoipProfile_AllowCoderFallback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 46),
    _VoipProfile_AllowCoderFallback_Type()
)
voipProfile_AllowCoderFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_AllowCoderFallback.setStatus("mandatory")


class _VoipProfile_ChooseDspVia_Type(Integer32):
    """Custom type voipProfile_ChooseDspVia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dataCentric", 2),
          ("voipCentric", 1))
    )


_VoipProfile_ChooseDspVia_Type.__name__ = "Integer32"
_VoipProfile_ChooseDspVia_Object = MibScalar
voipProfile_ChooseDspVia = _VoipProfile_ChooseDspVia_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 47),
    _VoipProfile_ChooseDspVia_Type()
)
voipProfile_ChooseDspVia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_ChooseDspVia.setStatus("mandatory")


class _VoipProfile_TrunkQuiesceEnable_Type(Integer32):
    """Custom type voipProfile_TrunkQuiesceEnable based on Integer32"""
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


_VoipProfile_TrunkQuiesceEnable_Type.__name__ = "Integer32"
_VoipProfile_TrunkQuiesceEnable_Object = MibScalar
voipProfile_TrunkQuiesceEnable = _VoipProfile_TrunkQuiesceEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 48),
    _VoipProfile_TrunkQuiesceEnable_Type()
)
voipProfile_TrunkQuiesceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_TrunkQuiesceEnable.setStatus("mandatory")


class _VoipProfile_EarlyRingbackEnable_Type(Integer32):
    """Custom type voipProfile_EarlyRingbackEnable based on Integer32"""
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


_VoipProfile_EarlyRingbackEnable_Type.__name__ = "Integer32"
_VoipProfile_EarlyRingbackEnable_Object = MibScalar
voipProfile_EarlyRingbackEnable = _VoipProfile_EarlyRingbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 49),
    _VoipProfile_EarlyRingbackEnable_Type()
)
voipProfile_EarlyRingbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_EarlyRingbackEnable.setStatus("mandatory")


class _VoipProfile_TrunkPrefixEnable_Type(Integer32):
    """Custom type voipProfile_TrunkPrefixEnable based on Integer32"""
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


_VoipProfile_TrunkPrefixEnable_Type.__name__ = "Integer32"
_VoipProfile_TrunkPrefixEnable_Object = MibScalar
voipProfile_TrunkPrefixEnable = _VoipProfile_TrunkPrefixEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 50),
    _VoipProfile_TrunkPrefixEnable_Type()
)
voipProfile_TrunkPrefixEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_TrunkPrefixEnable.setStatus("mandatory")


class _VoipProfile_SignalingModel_Type(Integer32):
    """Custom type voipProfile_SignalingModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("earlyAlerting", 1),
          ("fastProceeding", 3),
          ("slowProceeding", 2))
    )


_VoipProfile_SignalingModel_Type.__name__ = "Integer32"
_VoipProfile_SignalingModel_Object = MibScalar
voipProfile_SignalingModel = _VoipProfile_SignalingModel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 51),
    _VoipProfile_SignalingModel_Type()
)
voipProfile_SignalingModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_SignalingModel.setStatus("mandatory")
_VoipProfile_OperatorAssist_Type = DisplayString
_VoipProfile_OperatorAssist_Object = MibScalar
voipProfile_OperatorAssist = _VoipProfile_OperatorAssist_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 52),
    _VoipProfile_OperatorAssist_Type()
)
voipProfile_OperatorAssist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_OperatorAssist.setStatus("mandatory")


class _VoipProfile_SequentialCallEnable_Type(Integer32):
    """Custom type voipProfile_SequentialCallEnable based on Integer32"""
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


_VoipProfile_SequentialCallEnable_Type.__name__ = "Integer32"
_VoipProfile_SequentialCallEnable_Object = MibScalar
voipProfile_SequentialCallEnable = _VoipProfile_SequentialCallEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 53),
    _VoipProfile_SequentialCallEnable_Type()
)
voipProfile_SequentialCallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_SequentialCallEnable.setStatus("mandatory")


class _VoipProfile_PstnAttribute_CauseCodeTransparency_Type(Integer32):
    """Custom type voipProfile_PstnAttribute_CauseCodeTransparency based on Integer32"""
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


_VoipProfile_PstnAttribute_CauseCodeTransparency_Type.__name__ = "Integer32"
_VoipProfile_PstnAttribute_CauseCodeTransparency_Object = MibScalar
voipProfile_PstnAttribute_CauseCodeTransparency = _VoipProfile_PstnAttribute_CauseCodeTransparency_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 54),
    _VoipProfile_PstnAttribute_CauseCodeTransparency_Type()
)
voipProfile_PstnAttribute_CauseCodeTransparency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_PstnAttribute_CauseCodeTransparency.setStatus("mandatory")


class _VoipProfile_PstnAttribute_AlertProgressIndicator_Type(Integer32):
    """Custom type voipProfile_PstnAttribute_AlertProgressIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              9)
        )
    )
    namedValues = NamedValues(
        *(("destNonIsdn", 3),
          ("inbandInfoAvailable", 9),
          ("interworkingOccured", 6),
          ("noProgressIndicator", 1),
          ("noneEnd2endIsdn", 2),
          ("origNonIsdn", 4),
          ("returnToIsdn", 5))
    )


_VoipProfile_PstnAttribute_AlertProgressIndicator_Type.__name__ = "Integer32"
_VoipProfile_PstnAttribute_AlertProgressIndicator_Object = MibScalar
voipProfile_PstnAttribute_AlertProgressIndicator = _VoipProfile_PstnAttribute_AlertProgressIndicator_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 55),
    _VoipProfile_PstnAttribute_AlertProgressIndicator_Type()
)
voipProfile_PstnAttribute_AlertProgressIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_PstnAttribute_AlertProgressIndicator.setStatus("mandatory")


class _VoipProfile_PstnAttribute_ProceedProgressIndicator_Type(Integer32):
    """Custom type voipProfile_PstnAttribute_ProceedProgressIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              9)
        )
    )
    namedValues = NamedValues(
        *(("destNonIsdn", 3),
          ("inbandInfoAvailable", 9),
          ("interworkingOccured", 6),
          ("noProgressIndicator", 1),
          ("noneEnd2endIsdn", 2),
          ("origNonIsdn", 4),
          ("returnToIsdn", 5))
    )


_VoipProfile_PstnAttribute_ProceedProgressIndicator_Type.__name__ = "Integer32"
_VoipProfile_PstnAttribute_ProceedProgressIndicator_Object = MibScalar
voipProfile_PstnAttribute_ProceedProgressIndicator = _VoipProfile_PstnAttribute_ProceedProgressIndicator_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 56),
    _VoipProfile_PstnAttribute_ProceedProgressIndicator_Type()
)
voipProfile_PstnAttribute_ProceedProgressIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_PstnAttribute_ProceedProgressIndicator.setStatus("mandatory")


class _VoipProfile_PstnAttribute_BearerCapability_Type(Integer32):
    """Custom type voipProfile_PstnAttribute_BearerCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              9,
              10,
              17,
              25)
        )
    )
    namedValues = NamedValues(
        *(("audio3100hz", 17),
          ("restrictedDigitalInfo", 10),
          ("speech", 1),
          ("unrestrictedDigitalInfo", 9),
          ("video", 25))
    )


_VoipProfile_PstnAttribute_BearerCapability_Type.__name__ = "Integer32"
_VoipProfile_PstnAttribute_BearerCapability_Object = MibScalar
voipProfile_PstnAttribute_BearerCapability = _VoipProfile_PstnAttribute_BearerCapability_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 57),
    _VoipProfile_PstnAttribute_BearerCapability_Type()
)
voipProfile_PstnAttribute_BearerCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_PstnAttribute_BearerCapability.setStatus("mandatory")


class _VoipProfile_Ss7voipCallPersistence_Type(Integer32):
    """Custom type voipProfile_Ss7voipCallPersistence based on Integer32"""
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


_VoipProfile_Ss7voipCallPersistence_Type.__name__ = "Integer32"
_VoipProfile_Ss7voipCallPersistence_Object = MibScalar
voipProfile_Ss7voipCallPersistence = _VoipProfile_Ss7voipCallPersistence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 58),
    _VoipProfile_Ss7voipCallPersistence_Type()
)
voipProfile_Ss7voipCallPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_Ss7voipCallPersistence.setStatus("mandatory")


class _VoipProfile_Action_o_Type(Integer32):
    """Custom type voipProfile_Action_o based on Integer32"""
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


_VoipProfile_Action_o_Type.__name__ = "Integer32"
_VoipProfile_Action_o_Object = MibScalar
voipProfile_Action_o = _VoipProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 59),
    _VoipProfile_Action_o_Type()
)
voipProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_Action_o.setStatus("mandatory")


class _VoipProfile_TosOptions_MarkingType_Type(Integer32):
    """Custom type voipProfile_TosOptions_MarkingType based on Integer32"""
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


_VoipProfile_TosOptions_MarkingType_Type.__name__ = "Integer32"
_VoipProfile_TosOptions_MarkingType_Object = MibScalar
voipProfile_TosOptions_MarkingType = _VoipProfile_TosOptions_MarkingType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 60),
    _VoipProfile_TosOptions_MarkingType_Type()
)
voipProfile_TosOptions_MarkingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_TosOptions_MarkingType.setStatus("mandatory")
_VoipProfile_TosOptions_Dscp_Type = DisplayString
_VoipProfile_TosOptions_Dscp_Object = MibScalar
voipProfile_TosOptions_Dscp = _VoipProfile_TosOptions_Dscp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 61),
    _VoipProfile_TosOptions_Dscp_Type()
)
voipProfile_TosOptions_Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_TosOptions_Dscp.setStatus("mandatory")
_VoipProfile_PinDnisRetries_Type = Integer32
_VoipProfile_PinDnisRetries_Object = MibScalar
voipProfile_PinDnisRetries = _VoipProfile_PinDnisRetries_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 62),
    _VoipProfile_PinDnisRetries_Type()
)
voipProfile_PinDnisRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_PinDnisRetries.setStatus("mandatory")
_VoipProfile_MlgPinRetries_Type = Integer32
_VoipProfile_MlgPinRetries_Object = MibScalar
voipProfile_MlgPinRetries = _VoipProfile_MlgPinRetries_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 63),
    _VoipProfile_MlgPinRetries_Type()
)
voipProfile_MlgPinRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_MlgPinRetries.setStatus("mandatory")
_VoipProfile_MlgDnisRetries_Type = Integer32
_VoipProfile_MlgDnisRetries_Object = MibScalar
voipProfile_MlgDnisRetries = _VoipProfile_MlgDnisRetries_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 64),
    _VoipProfile_MlgDnisRetries_Type()
)
voipProfile_MlgDnisRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_MlgDnisRetries.setStatus("mandatory")
_VoipProfile_NextCall_Type = DisplayString
_VoipProfile_NextCall_Object = MibScalar
voipProfile_NextCall = _VoipProfile_NextCall_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 65),
    _VoipProfile_NextCall_Type()
)
voipProfile_NextCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_NextCall.setStatus("mandatory")


class _VoipProfile_RtpqosPollingEnable_Type(Integer32):
    """Custom type voipProfile_RtpqosPollingEnable based on Integer32"""
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


_VoipProfile_RtpqosPollingEnable_Type.__name__ = "Integer32"
_VoipProfile_RtpqosPollingEnable_Object = MibScalar
voipProfile_RtpqosPollingEnable = _VoipProfile_RtpqosPollingEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 66),
    _VoipProfile_RtpqosPollingEnable_Type()
)
voipProfile_RtpqosPollingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_RtpqosPollingEnable.setStatus("mandatory")


class _VoipProfile_FaststartEnable_Type(Integer32):
    """Custom type voipProfile_FaststartEnable based on Integer32"""
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


_VoipProfile_FaststartEnable_Type.__name__ = "Integer32"
_VoipProfile_FaststartEnable_Object = MibScalar
voipProfile_FaststartEnable = _VoipProfile_FaststartEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 67),
    _VoipProfile_FaststartEnable_Type()
)
voipProfile_FaststartEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_FaststartEnable.setStatus("mandatory")


class _VoipProfile_RtFaxOptions_AllowCtc_Type(Integer32):
    """Custom type voipProfile_RtFaxOptions_AllowCtc based on Integer32"""
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


_VoipProfile_RtFaxOptions_AllowCtc_Type.__name__ = "Integer32"
_VoipProfile_RtFaxOptions_AllowCtc_Object = MibScalar
voipProfile_RtFaxOptions_AllowCtc = _VoipProfile_RtFaxOptions_AllowCtc_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 68),
    _VoipProfile_RtFaxOptions_AllowCtc_Type()
)
voipProfile_RtFaxOptions_AllowCtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_RtFaxOptions_AllowCtc.setStatus("mandatory")


class _VoipProfile_SignalingTos_Active_Type(Integer32):
    """Custom type voipProfile_SignalingTos_Active based on Integer32"""
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


_VoipProfile_SignalingTos_Active_Type.__name__ = "Integer32"
_VoipProfile_SignalingTos_Active_Object = MibScalar
voipProfile_SignalingTos_Active = _VoipProfile_SignalingTos_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 71),
    _VoipProfile_SignalingTos_Active_Type()
)
voipProfile_SignalingTos_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_SignalingTos_Active.setStatus("mandatory")


class _VoipProfile_SignalingTos_Precedence_Type(Integer32):
    """Custom type voipProfile_SignalingTos_Precedence based on Integer32"""
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


_VoipProfile_SignalingTos_Precedence_Type.__name__ = "Integer32"
_VoipProfile_SignalingTos_Precedence_Object = MibScalar
voipProfile_SignalingTos_Precedence = _VoipProfile_SignalingTos_Precedence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 72),
    _VoipProfile_SignalingTos_Precedence_Type()
)
voipProfile_SignalingTos_Precedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_SignalingTos_Precedence.setStatus("mandatory")


class _VoipProfile_SignalingTos_TypeOfService_Type(Integer32):
    """Custom type voipProfile_SignalingTos_TypeOfService based on Integer32"""
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


_VoipProfile_SignalingTos_TypeOfService_Type.__name__ = "Integer32"
_VoipProfile_SignalingTos_TypeOfService_Object = MibScalar
voipProfile_SignalingTos_TypeOfService = _VoipProfile_SignalingTos_TypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 73),
    _VoipProfile_SignalingTos_TypeOfService_Type()
)
voipProfile_SignalingTos_TypeOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_SignalingTos_TypeOfService.setStatus("mandatory")


class _VoipProfile_SignalingTos_ApplyTo_Type(Integer32):
    """Custom type voipProfile_SignalingTos_ApplyTo based on Integer32"""
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


_VoipProfile_SignalingTos_ApplyTo_Type.__name__ = "Integer32"
_VoipProfile_SignalingTos_ApplyTo_Object = MibScalar
voipProfile_SignalingTos_ApplyTo = _VoipProfile_SignalingTos_ApplyTo_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 74),
    _VoipProfile_SignalingTos_ApplyTo_Type()
)
voipProfile_SignalingTos_ApplyTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_SignalingTos_ApplyTo.setStatus("mandatory")


class _VoipProfile_SignalingTos_MarkingType_Type(Integer32):
    """Custom type voipProfile_SignalingTos_MarkingType based on Integer32"""
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


_VoipProfile_SignalingTos_MarkingType_Type.__name__ = "Integer32"
_VoipProfile_SignalingTos_MarkingType_Object = MibScalar
voipProfile_SignalingTos_MarkingType = _VoipProfile_SignalingTos_MarkingType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 75),
    _VoipProfile_SignalingTos_MarkingType_Type()
)
voipProfile_SignalingTos_MarkingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_SignalingTos_MarkingType.setStatus("mandatory")
_VoipProfile_SignalingTos_Dscp_Type = DisplayString
_VoipProfile_SignalingTos_Dscp_Object = MibScalar
voipProfile_SignalingTos_Dscp = _VoipProfile_SignalingTos_Dscp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 76),
    _VoipProfile_SignalingTos_Dscp_Type()
)
voipProfile_SignalingTos_Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipProfile_SignalingTos_Dscp.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBVOIP-MIB",
    **{"DisplayString": DisplayString,
       "mibvoipProfile": mibvoipProfile,
       "mibvoipProfileTable": mibvoipProfileTable,
       "mibvoipProfileEntry": mibvoipProfileEntry,
       "voipProfile-VoipIndex-GatewayAccessNumber": voipProfile_VoipIndex_GatewayAccessNumber,
       "voipProfile-VoipIndex-FarEndNumber": voipProfile_VoipIndex_FarEndNumber,
       "voipProfile-GatekeeperIp": voipProfile_GatekeeperIp,
       "voipProfile-GkMlgControl": voipProfile_GkMlgControl,
       "voipProfile-VpnMode": voipProfile_VpnMode,
       "voipProfile-SingleDialEnable": voipProfile_SingleDialEnable,
       "voipProfile-PacketAudioMode": voipProfile_PacketAudioMode,
       "voipProfile-FramesPerPacket": voipProfile_FramesPerPacket,
       "voipProfile-TosOptions-Active": voipProfile_TosOptions_Active,
       "voipProfile-TosOptions-Precedence": voipProfile_TosOptions_Precedence,
       "voipProfile-TosOptions-TypeOfService": voipProfile_TosOptions_TypeOfService,
       "voipProfile-TosOptions-ApplyTo": voipProfile_TosOptions_ApplyTo,
       "voipProfile-SilenceDetCng": voipProfile_SilenceDetCng,
       "voipProfile-GatekeeperIpSec": voipProfile_GatekeeperIpSec,
       "voipProfile-GatekeeperKeepalive": voipProfile_GatekeeperKeepalive,
       "voipProfile-RegistrationRetries": voipProfile_RegistrationRetries,
       "voipProfile-RegistrationRetryTimer": voipProfile_RegistrationRetryTimer,
       "voipProfile-PrimaryRetries": voipProfile_PrimaryRetries,
       "voipProfile-EnaAdapJitterBuffer": voipProfile_EnaAdapJitterBuffer,
       "voipProfile-MaxJitterBufferSize": voipProfile_MaxJitterBufferSize,
       "voipProfile-InitialJitterBufferSize": voipProfile_InitialJitterBufferSize,
       "voipProfile-Maxcalls": voipProfile_Maxcalls,
       "voipProfile-CutThruEnableNearend": voipProfile_CutThruEnableNearend,
       "voipProfile-H323VoiceAnnEnabled": voipProfile_H323VoiceAnnEnabled,
       "voipProfile-VoiceAnnDir": voipProfile_VoiceAnnDir,
       "voipProfile-VoiceAnnEnc": voipProfile_VoiceAnnEnc,
       "voipProfile-CallInterDigitTimeout": voipProfile_CallInterDigitTimeout,
       "voipProfile-SilenceThreshold": voipProfile_SilenceThreshold,
       "voipProfile-DtmfTonePassing": voipProfile_DtmfTonePassing,
       "voipProfile-VoiceAnnServIp": voipProfile_VoiceAnnServIp,
       "voipProfile-VoiceAnnFileSpec": voipProfile_VoiceAnnFileSpec,
       "voipProfile-RtFaxOptions-RtFaxEnable": voipProfile_RtFaxOptions_RtFaxEnable,
       "voipProfile-RtFaxOptions-EcmEnable": voipProfile_RtFaxOptions_EcmEnable,
       "voipProfile-RtFaxOptions-LowLatencyMode": voipProfile_RtFaxOptions_LowLatencyMode,
       "voipProfile-RtFaxOptions-CommandSpoof": voipProfile_RtFaxOptions_CommandSpoof,
       "voipProfile-RtFaxOptions-LocalRetransmitLsf": voipProfile_RtFaxOptions_LocalRetransmitLsf,
       "voipProfile-RtFaxOptions-PacketRedundancy": voipProfile_RtFaxOptions_PacketRedundancy,
       "voipProfile-RtFaxOptions-FixedPackets": voipProfile_RtFaxOptions_FixedPackets,
       "voipProfile-RtFaxOptions-MaxDataRate": voipProfile_RtFaxOptions_MaxDataRate,
       "voipProfile-CallHairpin": voipProfile_CallHairpin,
       "voipProfile-CallKeepAliveTimeout": voipProfile_CallKeepAliveTimeout,
       "voipProfile-ClidSuppress": voipProfile_ClidSuppress,
       "voipProfile-TrueConnectEnable": voipProfile_TrueConnectEnable,
       "voipProfile-G711TransparentData": voipProfile_G711TransparentData,
       "voipProfile-AllowG711Fallback": voipProfile_AllowG711Fallback,
       "voipProfile-AllowCoderFallback": voipProfile_AllowCoderFallback,
       "voipProfile-ChooseDspVia": voipProfile_ChooseDspVia,
       "voipProfile-TrunkQuiesceEnable": voipProfile_TrunkQuiesceEnable,
       "voipProfile-EarlyRingbackEnable": voipProfile_EarlyRingbackEnable,
       "voipProfile-TrunkPrefixEnable": voipProfile_TrunkPrefixEnable,
       "voipProfile-SignalingModel": voipProfile_SignalingModel,
       "voipProfile-OperatorAssist": voipProfile_OperatorAssist,
       "voipProfile-SequentialCallEnable": voipProfile_SequentialCallEnable,
       "voipProfile-PstnAttribute-CauseCodeTransparency": voipProfile_PstnAttribute_CauseCodeTransparency,
       "voipProfile-PstnAttribute-AlertProgressIndicator": voipProfile_PstnAttribute_AlertProgressIndicator,
       "voipProfile-PstnAttribute-ProceedProgressIndicator": voipProfile_PstnAttribute_ProceedProgressIndicator,
       "voipProfile-PstnAttribute-BearerCapability": voipProfile_PstnAttribute_BearerCapability,
       "voipProfile-Ss7voipCallPersistence": voipProfile_Ss7voipCallPersistence,
       "voipProfile-Action-o": voipProfile_Action_o,
       "voipProfile-TosOptions-MarkingType": voipProfile_TosOptions_MarkingType,
       "voipProfile-TosOptions-Dscp": voipProfile_TosOptions_Dscp,
       "voipProfile-PinDnisRetries": voipProfile_PinDnisRetries,
       "voipProfile-MlgPinRetries": voipProfile_MlgPinRetries,
       "voipProfile-MlgDnisRetries": voipProfile_MlgDnisRetries,
       "voipProfile-NextCall": voipProfile_NextCall,
       "voipProfile-RtpqosPollingEnable": voipProfile_RtpqosPollingEnable,
       "voipProfile-FaststartEnable": voipProfile_FaststartEnable,
       "voipProfile-RtFaxOptions-AllowCtc": voipProfile_RtFaxOptions_AllowCtc,
       "voipProfile-SignalingTos-Active": voipProfile_SignalingTos_Active,
       "voipProfile-SignalingTos-Precedence": voipProfile_SignalingTos_Precedence,
       "voipProfile-SignalingTos-TypeOfService": voipProfile_SignalingTos_TypeOfService,
       "voipProfile-SignalingTos-ApplyTo": voipProfile_SignalingTos_ApplyTo,
       "voipProfile-SignalingTos-MarkingType": voipProfile_SignalingTos_MarkingType,
       "voipProfile-SignalingTos-Dscp": voipProfile_SignalingTos_Dscp}
)
