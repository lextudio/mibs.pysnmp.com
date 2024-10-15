# SNMP MIB module (VTGW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VTGW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:23 2024
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
 NotificationType,
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
    "NotificationType",
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

_Vocaltec_ObjectIdentity = ObjectIdentity
vocaltec = _Vocaltec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516)
)
_Vtg_ObjectIdentity = ObjectIdentity
vtg = _Vtg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516, 2)
)
_Tgw_ObjectIdentity = ObjectIdentity
tgw = _Tgw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516, 2, 1)
)
_SoftwareVersion_Type = DisplayString
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 1, 1),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("mandatory")
_Cti2Service_Type = DisplayString
_Cti2Service_Object = MibScalar
cti2Service = _Cti2Service_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 1, 2),
    _Cti2Service_Type()
)
cti2Service.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cti2Service.setStatus("mandatory")


class _ResloveMode_Type(Integer32):
    """Custom type resloveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gatekeeper", 1),
          ("local", 2))
    )


_ResloveMode_Type.__name__ = "Integer32"
_ResloveMode_Object = MibScalar
resloveMode = _ResloveMode_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 1, 3),
    _ResloveMode_Type()
)
resloveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resloveMode.setStatus("mandatory")


class _TelephonyProtocol_Type(Integer32):
    """Custom type telephonyProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("analog", 1),
          ("carbon", 6),
          ("enm", 3),
          ("erbium", 5),
          ("gc", 4),
          ("iridium", 7),
          ("pri", 2))
    )


_TelephonyProtocol_Type.__name__ = "Integer32"
_TelephonyProtocol_Object = MibScalar
telephonyProtocol = _TelephonyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 1, 4),
    _TelephonyProtocol_Type()
)
telephonyProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyProtocol.setStatus("mandatory")


class _InternetProtocol_Type(Integer32):
    """Custom type internetProtocol based on Integer32"""
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
        *(("classic", 1),
          ("cobalt", 4),
          ("dm3", 3),
          ("h323", 2))
    )


_InternetProtocol_Type.__name__ = "Integer32"
_InternetProtocol_Object = MibScalar
internetProtocol = _InternetProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 1, 5),
    _InternetProtocol_Type()
)
internetProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProtocol.setStatus("mandatory")
_UniversalLinesNumber_Type = Integer32
_UniversalLinesNumber_Object = MibScalar
universalLinesNumber = _UniversalLinesNumber_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 1, 6),
    _UniversalLinesNumber_Type()
)
universalLinesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    universalLinesNumber.setStatus("mandatory")
_VoiceLinesNumber_Type = Integer32
_VoiceLinesNumber_Object = MibScalar
voiceLinesNumber = _VoiceLinesNumber_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 1, 7),
    _VoiceLinesNumber_Type()
)
voiceLinesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceLinesNumber.setStatus("mandatory")
_FaxLinesNumber_Type = Integer32
_FaxLinesNumber_Object = MibScalar
faxLinesNumber = _FaxLinesNumber_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 1, 8),
    _FaxLinesNumber_Type()
)
faxLinesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxLinesNumber.setStatus("mandatory")
_SncLinesNumber_Type = Integer32
_SncLinesNumber_Object = MibScalar
sncLinesNumber = _SncLinesNumber_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 1, 9),
    _SncLinesNumber_Type()
)
sncLinesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sncLinesNumber.setStatus("mandatory")
_IPhoneLinesNumber_Type = Integer32
_IPhoneLinesNumber_Object = MibScalar
iPhoneLinesNumber = _IPhoneLinesNumber_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 1, 10),
    _IPhoneLinesNumber_Type()
)
iPhoneLinesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPhoneLinesNumber.setStatus("mandatory")
_DialerLinesNumber_Type = Integer32
_DialerLinesNumber_Object = MibScalar
dialerLinesNumber = _DialerLinesNumber_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 1, 11),
    _DialerLinesNumber_Type()
)
dialerLinesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerLinesNumber.setStatus("mandatory")
_Cti2ServicePollingQuantum_Type = Integer32
_Cti2ServicePollingQuantum_Object = MibScalar
cti2ServicePollingQuantum = _Cti2ServicePollingQuantum_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 1, 14),
    _Cti2ServicePollingQuantum_Type()
)
cti2ServicePollingQuantum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cti2ServicePollingQuantum.setStatus("mandatory")
_Vnmvgk_ObjectIdentity = ObjectIdentity
vnmvgk = _Vnmvgk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516, 2, 2)
)
_RcamPort_Type = Integer32
_RcamPort_Object = MibScalar
rcamPort = _RcamPort_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 2, 1),
    _RcamPort_Type()
)
rcamPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcamPort.setStatus("mandatory")
_Id_Type = DisplayString
_Id_Object = MibScalar
id = _Id_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 2, 2),
    _Id_Type()
)
id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    id.setStatus("mandatory")
_Alias_Type = DisplayString
_Alias_Object = MibScalar
alias = _Alias_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 2, 3),
    _Alias_Type()
)
alias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alias.setStatus("mandatory")
_Time2Live_Type = Integer32
_Time2Live_Object = MibScalar
time2Live = _Time2Live_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 2, 5),
    _Time2Live_Type()
)
time2Live.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time2Live.setStatus("mandatory")
_LoginSetAttempts_Type = Integer32
_LoginSetAttempts_Object = MibScalar
loginSetAttempts = _LoginSetAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 2, 6),
    _LoginSetAttempts_Type()
)
loginSetAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginSetAttempts.setStatus("mandatory")
_TimeB4LoginAttempt_Type = Integer32
_TimeB4LoginAttempt_Object = MibScalar
timeB4LoginAttempt = _TimeB4LoginAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 2, 7),
    _TimeB4LoginAttempt_Type()
)
timeB4LoginAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeB4LoginAttempt.setStatus("mandatory")
_TimeB4LoginSet_Type = Integer32
_TimeB4LoginSet_Object = MibScalar
timeB4LoginSet = _TimeB4LoginSet_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 2, 8),
    _TimeB4LoginSet_Type()
)
timeB4LoginSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeB4LoginSet.setStatus("mandatory")
_RasPort_Type = Integer32
_RasPort_Object = MibScalar
rasPort = _RasPort_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 2, 30),
    _RasPort_Type()
)
rasPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasPort.setStatus("mandatory")
_Hasp_ObjectIdentity = ObjectIdentity
hasp = _Hasp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516, 2, 3)
)
_Audio_ObjectIdentity = ObjectIdentity
audio = _Audio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516, 2, 4)
)
_CodecsPriorities_Type = DisplayString
_CodecsPriorities_Object = MibScalar
codecsPriorities = _CodecsPriorities_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 4, 1),
    _CodecsPriorities_Type()
)
codecsPriorities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codecsPriorities.setStatus("mandatory")
_PreferredCodec_Type = Integer32
_PreferredCodec_Object = MibScalar
preferredCodec = _PreferredCodec_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 4, 2),
    _PreferredCodec_Type()
)
preferredCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preferredCodec.setStatus("mandatory")
_OutputGain_Type = DisplayString
_OutputGain_Object = MibScalar
outputGain = _OutputGain_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 4, 3),
    _OutputGain_Type()
)
outputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputGain.setStatus("mandatory")
_InputGain_Type = DisplayString
_InputGain_Object = MibScalar
inputGain = _InputGain_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 4, 4),
    _InputGain_Type()
)
inputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputGain.setStatus("mandatory")
_CodecsTable_Object = MibTable
codecsTable = _CodecsTable_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 4, 5)
)
if mibBuilder.loadTexts:
    codecsTable.setStatus("mandatory")
_CodecEntry_Object = MibTableRow
codecEntry = _CodecEntry_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 4, 5, 1)
)
codecEntry.setIndexNames(
    (0, "VTGW-MIB", "coder"),
)
if mibBuilder.loadTexts:
    codecEntry.setStatus("mandatory")


class _Coder_Type(Integer32):
    """Custom type coder based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("g711a", 1),
          ("g711m", 2),
          ("g723", 3),
          ("g726", 6),
          ("g727", 7),
          ("g728", 8),
          ("g729", 4),
          ("gsm", 5),
          ("vhqc4800", 10),
          ("vhqc5600", 11),
          ("vhqc6400", 12),
          ("vhqc7200", 13),
          ("vhqc8000", 14),
          ("vhqc8800", 15),
          ("vhqc9600", 16),
          ("vsc", 9))
    )


_Coder_Type.__name__ = "Integer32"
_Coder_Object = MibTableColumn
coder = _Coder_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 4, 5, 1, 1),
    _Coder_Type()
)
coder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coder.setStatus("mandatory")
_VadEnable_Type = Integer32
_VadEnable_Object = MibTableColumn
vadEnable = _VadEnable_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 4, 5, 1, 2),
    _VadEnable_Type()
)
vadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vadEnable.setStatus("mandatory")
_CoderRate_Type = Integer32
_CoderRate_Object = MibTableColumn
coderRate = _CoderRate_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 4, 5, 1, 3),
    _CoderRate_Type()
)
coderRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coderRate.setStatus("mandatory")
_FramesPerPkt_Type = Integer32
_FramesPerPkt_Object = MibTableColumn
framesPerPkt = _FramesPerPkt_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 4, 5, 1, 4),
    _FramesPerPkt_Type()
)
framesPerPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    framesPerPkt.setStatus("mandatory")
_FramesSize_Type = Integer32
_FramesSize_Object = MibTableColumn
framesSize = _FramesSize_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 4, 5, 1, 5),
    _FramesSize_Type()
)
framesSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    framesSize.setStatus("mandatory")
_Jitter_Type = DisplayString
_Jitter_Object = MibTableColumn
jitter = _Jitter_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 4, 5, 1, 6),
    _Jitter_Type()
)
jitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jitter.setStatus("mandatory")
_JitterOptFactor_Type = DisplayString
_JitterOptFactor_Object = MibTableColumn
jitterOptFactor = _JitterOptFactor_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 4, 5, 1, 7),
    _JitterOptFactor_Type()
)
jitterOptFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jitterOptFactor.setStatus("mandatory")
_CoderRedundency_Type = Integer32
_CoderRedundency_Object = MibTableColumn
coderRedundency = _CoderRedundency_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 4, 5, 1, 8),
    _CoderRedundency_Type()
)
coderRedundency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coderRedundency.setStatus("mandatory")
_Ports_ObjectIdentity = ObjectIdentity
ports = _Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516, 2, 5)
)
_PortsTable_Object = MibTable
portsTable = _PortsTable_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 5, 1)
)
if mibBuilder.loadTexts:
    portsTable.setStatus("mandatory")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 5, 1, 1)
)
portEntry.setIndexNames(
    (0, "VTGW-MIB", "portNumber"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")
_PortNumber_Type = Integer32
_PortNumber_Object = MibTableColumn
portNumber = _PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 5, 1, 1, 1),
    _PortNumber_Type()
)
portNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portNumber.setStatus("mandatory")
_PortEnable_Type = Integer32
_PortEnable_Object = MibTableColumn
portEnable = _PortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 5, 1, 1, 2),
    _PortEnable_Type()
)
portEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEnable.setStatus("mandatory")


class _ConnectedTo_Type(Integer32):
    """Custom type connectedTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pbx", 1),
          ("pstn", 2))
    )


_ConnectedTo_Type.__name__ = "Integer32"
_ConnectedTo_Object = MibTableColumn
connectedTo = _ConnectedTo_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 5, 1, 1, 3),
    _ConnectedTo_Type()
)
connectedTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectedTo.setStatus("mandatory")


class _BoundDirection_Type(Integer32):
    """Custom type boundDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_BoundDirection_Type.__name__ = "Integer32"
_BoundDirection_Object = MibTableColumn
boundDirection = _BoundDirection_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 5, 1, 1, 4),
    _BoundDirection_Type()
)
boundDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boundDirection.setStatus("mandatory")


class _DialingMode_Type(Integer32):
    """Custom type dialingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dialing-dtmf", 1),
          ("dialing-mf", 3),
          ("dialing-pulse", 2))
    )


_DialingMode_Type.__name__ = "Integer32"
_DialingMode_Object = MibTableColumn
dialingMode = _DialingMode_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 5, 1, 1, 5),
    _DialingMode_Type()
)
dialingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialingMode.setStatus("mandatory")


class _DetectionMode_Type(Integer32):
    """Custom type detectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("detection-apd", 3),
          ("detection-dpd", 5),
          ("detection-dpd2", 6),
          ("detection-dtmf", 1),
          ("detection-lpd", 2),
          ("detection-mf", 4))
    )


_DetectionMode_Type.__name__ = "Integer32"
_DetectionMode_Object = MibTableColumn
detectionMode = _DetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 5, 1, 1, 6),
    _DetectionMode_Type()
)
detectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    detectionMode.setStatus("mandatory")


class _IvrMode_Type(Integer32):
    """Custom type ivrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ani", 5),
          ("dnis", 6),
          ("numberphone", 1),
          ("numberpin", 2),
          ("pbx", 4),
          ("phonepin", 3))
    )


_IvrMode_Type.__name__ = "Integer32"
_IvrMode_Object = MibTableColumn
ivrMode = _IvrMode_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 5, 1, 1, 7),
    _IvrMode_Type()
)
ivrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ivrMode.setStatus("mandatory")
_RepeatIVR_Type = Integer32
_RepeatIVR_Object = MibTableColumn
repeatIVR = _RepeatIVR_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 5, 1, 1, 8),
    _RepeatIVR_Type()
)
repeatIVR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeatIVR.setStatus("mandatory")
_OverSilenceTime_Type = Integer32
_OverSilenceTime_Object = MibTableColumn
overSilenceTime = _OverSilenceTime_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 5, 1, 1, 9),
    _OverSilenceTime_Type()
)
overSilenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overSilenceTime.setStatus("mandatory")
_Comment_Type = DisplayString
_Comment_Object = MibTableColumn
comment = _Comment_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 5, 1, 1, 10),
    _Comment_Type()
)
comment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comment.setStatus("mandatory")
_Ivr_ObjectIdentity = ObjectIdentity
ivr = _Ivr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516, 2, 6)
)
_InterDigitTimeout_Type = Integer32
_InterDigitTimeout_Object = MibScalar
interDigitTimeout = _InterDigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 6, 1),
    _InterDigitTimeout_Type()
)
interDigitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interDigitTimeout.setStatus("mandatory")
_DigitsTimeout_Type = Integer32
_DigitsTimeout_Object = MibScalar
digitsTimeout = _DigitsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 6, 2),
    _DigitsTimeout_Type()
)
digitsTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitsTimeout.setStatus("mandatory")
_TelephonyProtocols_ObjectIdentity = ObjectIdentity
telephonyProtocols = _TelephonyProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7)
)
_Analog_ObjectIdentity = ObjectIdentity
analog = _Analog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 1)
)
_RingCount_Type = Integer32
_RingCount_Object = MibScalar
ringCount = _RingCount_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 1, 21),
    _RingCount_Type()
)
ringCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringCount.setStatus("mandatory")
_Volume_Type = Integer32
_Volume_Object = MibScalar
volume = _Volume_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 1, 22),
    _Volume_Type()
)
volume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    volume.setStatus("mandatory")
_Enm_ObjectIdentity = ObjectIdentity
enm = _Enm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2)
)
_Idle_Type = DisplayString
_Idle_Object = MibScalar
idle = _Idle_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 1),
    _Idle_Type()
)
idle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idle.setStatus("mandatory")
_OutOfService_Type = DisplayString
_OutOfService_Object = MibScalar
outOfService = _OutOfService_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 2),
    _OutOfService_Type()
)
outOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOfService.setStatus("mandatory")
_SeizeOutbound_Type = DisplayString
_SeizeOutbound_Object = MibScalar
seizeOutbound = _SeizeOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 3),
    _SeizeOutbound_Type()
)
seizeOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seizeOutbound.setStatus("mandatory")
_SeizeInbound_Type = DisplayString
_SeizeInbound_Object = MibScalar
seizeInbound = _SeizeInbound_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 4),
    _SeizeInbound_Type()
)
seizeInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seizeInbound.setStatus("mandatory")
_SeizeAckOutbound_Type = DisplayString
_SeizeAckOutbound_Object = MibScalar
seizeAckOutbound = _SeizeAckOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 5),
    _SeizeAckOutbound_Type()
)
seizeAckOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seizeAckOutbound.setStatus("mandatory")
_SeizeAckInbound_Type = DisplayString
_SeizeAckInbound_Object = MibScalar
seizeAckInbound = _SeizeAckInbound_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 6),
    _SeizeAckInbound_Type()
)
seizeAckInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seizeAckInbound.setStatus("mandatory")
_AnswerOutbound_Type = DisplayString
_AnswerOutbound_Object = MibScalar
answerOutbound = _AnswerOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 7),
    _AnswerOutbound_Type()
)
answerOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerOutbound.setStatus("mandatory")
_AnswerInbound_Type = DisplayString
_AnswerInbound_Object = MibScalar
answerInbound = _AnswerInbound_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 8),
    _AnswerInbound_Type()
)
answerInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerInbound.setStatus("mandatory")
_DropOutbound_Type = DisplayString
_DropOutbound_Object = MibScalar
dropOutbound = _DropOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 9),
    _DropOutbound_Type()
)
dropOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dropOutbound.setStatus("mandatory")
_DropInbound_Type = DisplayString
_DropInbound_Object = MibScalar
dropInbound = _DropInbound_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 10),
    _DropInbound_Type()
)
dropInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dropInbound.setStatus("mandatory")
_NoAnswerSec_Type = Integer32
_NoAnswerSec_Object = MibScalar
noAnswerSec = _NoAnswerSec_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 11),
    _NoAnswerSec_Type()
)
noAnswerSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noAnswerSec.setStatus("mandatory")
_ContinuesNoSignal_Type = Integer32
_ContinuesNoSignal_Object = MibScalar
continuesNoSignal = _ContinuesNoSignal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 12),
    _ContinuesNoSignal_Type()
)
continuesNoSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    continuesNoSignal.setStatus("mandatory")
_HelloEdge_Type = Integer32
_HelloEdge_Object = MibScalar
helloEdge = _HelloEdge_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 13),
    _HelloEdge_Type()
)
helloEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    helloEdge.setStatus("mandatory")
_MaxInterRing_Type = Integer32
_MaxInterRing_Object = MibScalar
maxInterRing = _MaxInterRing_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 14),
    _MaxInterRing_Type()
)
maxInterRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxInterRing.setStatus("mandatory")
_DialToneLocal_Type = DisplayString
_DialToneLocal_Object = MibScalar
dialToneLocal = _DialToneLocal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 15),
    _DialToneLocal_Type()
)
dialToneLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialToneLocal.setStatus("mandatory")
_DialToneIntl_Type = DisplayString
_DialToneIntl_Object = MibScalar
dialToneIntl = _DialToneIntl_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 16),
    _DialToneIntl_Type()
)
dialToneIntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialToneIntl.setStatus("mandatory")
_DialToneXtra_Type = DisplayString
_DialToneXtra_Object = MibScalar
dialToneXtra = _DialToneXtra_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 17),
    _DialToneXtra_Type()
)
dialToneXtra.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialToneXtra.setStatus("mandatory")
_Busy1Tone_Type = DisplayString
_Busy1Tone_Object = MibScalar
busy1Tone = _Busy1Tone_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 18),
    _Busy1Tone_Type()
)
busy1Tone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    busy1Tone.setStatus("mandatory")
_Busy2Tone_Type = DisplayString
_Busy2Tone_Object = MibScalar
busy2Tone = _Busy2Tone_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 19),
    _Busy2Tone_Type()
)
busy2Tone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    busy2Tone.setStatus("mandatory")
_Ringback1Tone_Type = DisplayString
_Ringback1Tone_Object = MibScalar
ringback1Tone = _Ringback1Tone_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 20),
    _Ringback1Tone_Type()
)
ringback1Tone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringback1Tone.setStatus("mandatory")
_Ringback2Tone_Type = DisplayString
_Ringback2Tone_Object = MibScalar
ringback2Tone = _Ringback2Tone_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 21),
    _Ringback2Tone_Type()
)
ringback2Tone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringback2Tone.setStatus("mandatory")
_Disconnect1Tone_Type = DisplayString
_Disconnect1Tone_Object = MibScalar
disconnect1Tone = _Disconnect1Tone_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 22),
    _Disconnect1Tone_Type()
)
disconnect1Tone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect1Tone.setStatus("mandatory")
_Disconnect2Tone_Type = DisplayString
_Disconnect2Tone_Object = MibScalar
disconnect2Tone = _Disconnect2Tone_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 23),
    _Disconnect2Tone_Type()
)
disconnect2Tone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect2Tone.setStatus("mandatory")
_WaitForDropAckTimer_Type = Integer32
_WaitForDropAckTimer_Object = MibScalar
waitForDropAckTimer = _WaitForDropAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 24),
    _WaitForDropAckTimer_Type()
)
waitForDropAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waitForDropAckTimer.setStatus("mandatory")
_WaitForSiezeAckTimer_Type = Integer32
_WaitForSiezeAckTimer_Object = MibScalar
waitForSiezeAckTimer = _WaitForSiezeAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 25),
    _WaitForSiezeAckTimer_Type()
)
waitForSiezeAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waitForSiezeAckTimer.setStatus("mandatory")
_DigitsMode_Type = DisplayString
_DigitsMode_Object = MibScalar
digitsMode = _DigitsMode_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 26),
    _DigitsMode_Type()
)
digitsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitsMode.setStatus("mandatory")
_IsDnisBeforeAni_Type = Integer32
_IsDnisBeforeAni_Object = MibScalar
isDnisBeforeAni = _IsDnisBeforeAni_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 27),
    _IsDnisBeforeAni_Type()
)
isDnisBeforeAni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDnisBeforeAni.setStatus("mandatory")
_CollectAni_Type = Integer32
_CollectAni_Object = MibScalar
collectAni = _CollectAni_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 28),
    _CollectAni_Type()
)
collectAni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    collectAni.setStatus("mandatory")
_PrewinkLength_Type = Integer32
_PrewinkLength_Object = MibScalar
prewinkLength = _PrewinkLength_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 29),
    _PrewinkLength_Type()
)
prewinkLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prewinkLength.setStatus("mandatory")
_WinkLength_Type = Integer32
_WinkLength_Object = MibScalar
winkLength = _WinkLength_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 30),
    _WinkLength_Type()
)
winkLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winkLength.setStatus("mandatory")
_MinWinkDetection_Type = Integer32
_MinWinkDetection_Object = MibScalar
minWinkDetection = _MinWinkDetection_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 31),
    _MinWinkDetection_Type()
)
minWinkDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minWinkDetection.setStatus("mandatory")
_MaxWinkDetection_Type = Integer32
_MaxWinkDetection_Object = MibScalar
maxWinkDetection = _MaxWinkDetection_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 32),
    _MaxWinkDetection_Type()
)
maxWinkDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxWinkDetection.setStatus("mandatory")
_MaxDigitsDnis_Type = Integer32
_MaxDigitsDnis_Object = MibScalar
maxDigitsDnis = _MaxDigitsDnis_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 33),
    _MaxDigitsDnis_Type()
)
maxDigitsDnis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxDigitsDnis.setStatus("mandatory")
_MaxDigitsAni_Type = Integer32
_MaxDigitsAni_Object = MibScalar
maxDigitsAni = _MaxDigitsAni_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 34),
    _MaxDigitsAni_Type()
)
maxDigitsAni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxDigitsAni.setStatus("mandatory")
_MinTimeToDetectTransition_Type = Integer32
_MinTimeToDetectTransition_Object = MibScalar
minTimeToDetectTransition = _MinTimeToDetectTransition_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 35),
    _MinTimeToDetectTransition_Type()
)
minTimeToDetectTransition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minTimeToDetectTransition.setStatus("mandatory")
_CharBeforedigits_Type = DisplayString
_CharBeforedigits_Object = MibScalar
charBeforedigits = _CharBeforedigits_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 36),
    _CharBeforedigits_Type()
)
charBeforedigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charBeforedigits.setStatus("mandatory")
_CharBetweenAniAndDnis_Type = DisplayString
_CharBetweenAniAndDnis_Object = MibScalar
charBetweenAniAndDnis = _CharBetweenAniAndDnis_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 37),
    _CharBetweenAniAndDnis_Type()
)
charBetweenAniAndDnis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charBetweenAniAndDnis.setStatus("mandatory")
_CharInTheEndOfDigits_Type = DisplayString
_CharInTheEndOfDigits_Object = MibScalar
charInTheEndOfDigits = _CharInTheEndOfDigits_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 38),
    _CharInTheEndOfDigits_Type()
)
charInTheEndOfDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charInTheEndOfDigits.setStatus("mandatory")
_SendCharBeforeDigits_Type = DisplayString
_SendCharBeforeDigits_Object = MibScalar
sendCharBeforeDigits = _SendCharBeforeDigits_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 39),
    _SendCharBeforeDigits_Type()
)
sendCharBeforeDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendCharBeforeDigits.setStatus("mandatory")
_SendDnisbeforeAni_Type = DisplayString
_SendDnisbeforeAni_Object = MibScalar
sendDnisbeforeAni = _SendDnisbeforeAni_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 40),
    _SendDnisbeforeAni_Type()
)
sendDnisbeforeAni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendDnisbeforeAni.setStatus("mandatory")
_SendCharBetweenAniAndDnis_Type = DisplayString
_SendCharBetweenAniAndDnis_Object = MibScalar
sendCharBetweenAniAndDnis = _SendCharBetweenAniAndDnis_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 41),
    _SendCharBetweenAniAndDnis_Type()
)
sendCharBetweenAniAndDnis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendCharBetweenAniAndDnis.setStatus("mandatory")
_SendCharcharInTheEndOfDigits_Type = DisplayString
_SendCharcharInTheEndOfDigits_Object = MibScalar
sendCharcharInTheEndOfDigits = _SendCharcharInTheEndOfDigits_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 42),
    _SendCharcharInTheEndOfDigits_Type()
)
sendCharcharInTheEndOfDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendCharcharInTheEndOfDigits.setStatus("mandatory")
_FileToPlay_Type = DisplayString
_FileToPlay_Object = MibScalar
fileToPlay = _FileToPlay_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 43),
    _FileToPlay_Type()
)
fileToPlay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileToPlay.setStatus("mandatory")
_RepeatPlayFile_Type = DisplayString
_RepeatPlayFile_Object = MibScalar
repeatPlayFile = _RepeatPlayFile_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 2, 44),
    _RepeatPlayFile_Type()
)
repeatPlayFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeatPlayFile.setStatus("mandatory")
_Gc_ObjectIdentity = ObjectIdentity
gc = _Gc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 3)
)
_ProtocolConfigFileIn_Type = DisplayString
_ProtocolConfigFileIn_Object = MibScalar
protocolConfigFileIn = _ProtocolConfigFileIn_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 3, 1),
    _ProtocolConfigFileIn_Type()
)
protocolConfigFileIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolConfigFileIn.setStatus("mandatory")
_ProtocolConfigFileOut_Type = DisplayString
_ProtocolConfigFileOut_Object = MibScalar
protocolConfigFileOut = _ProtocolConfigFileOut_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 3, 2),
    _ProtocolConfigFileOut_Type()
)
protocolConfigFileOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolConfigFileOut.setStatus("mandatory")
_ListOfProtocolConfigFilesIn_Type = DisplayString
_ListOfProtocolConfigFilesIn_Object = MibScalar
listOfProtocolConfigFilesIn = _ListOfProtocolConfigFilesIn_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 3, 3),
    _ListOfProtocolConfigFilesIn_Type()
)
listOfProtocolConfigFilesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listOfProtocolConfigFilesIn.setStatus("mandatory")
_ListOfProtocolConfigFilesOut_Type = DisplayString
_ListOfProtocolConfigFilesOut_Object = MibScalar
listOfProtocolConfigFilesOut = _ListOfProtocolConfigFilesOut_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 3, 4),
    _ListOfProtocolConfigFilesOut_Type()
)
listOfProtocolConfigFilesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listOfProtocolConfigFilesOut.setStatus("mandatory")
_Pri_ObjectIdentity = ObjectIdentity
pri = _Pri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 4)
)
_ProtocolTrace_Type = Integer32
_ProtocolTrace_Object = MibScalar
protocolTrace = _ProtocolTrace_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 4, 2),
    _ProtocolTrace_Type()
)
protocolTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolTrace.setStatus("mandatory")
_Erbium_ObjectIdentity = ObjectIdentity
erbium = _Erbium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 5)
)
_Iridium_ObjectIdentity = ObjectIdentity
iridium = _Iridium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 7)
)
_HostID_Type = Integer32
_HostID_Object = MibScalar
hostID = _HostID_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 7, 2),
    _HostID_Type()
)
hostID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostID.setStatus("mandatory")
_SIUIPorID_Type = DisplayString
_SIUIPorID_Object = MibScalar
sIUIPorID = _SIUIPorID_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 7, 3),
    _SIUIPorID_Type()
)
sIUIPorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sIUIPorID.setStatus("mandatory")


class _ChannelSelectionOrder_Type(Integer32):
    """Custom type channelSelectionOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ChannelSelectionOrder_Type.__name__ = "Integer32"
_ChannelSelectionOrder_Object = MibScalar
channelSelectionOrder = _ChannelSelectionOrder_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 20),
    _ChannelSelectionOrder_Type()
)
channelSelectionOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelSelectionOrder.setStatus("mandatory")


class _GlareMode_Type(Integer32):
    """Custom type glareMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stand", 2),
          ("yield", 1))
    )


_GlareMode_Type.__name__ = "Integer32"
_GlareMode_Object = MibScalar
glareMode = _GlareMode_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 7, 21),
    _GlareMode_Type()
)
glareMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    glareMode.setStatus("mandatory")
_Stat_ObjectIdentity = ObjectIdentity
stat = _Stat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8)
)
_TimeUpTotal_Type = DisplayString
_TimeUpTotal_Object = MibScalar
timeUpTotal = _TimeUpTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 1),
    _TimeUpTotal_Type()
)
timeUpTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeUpTotal.setStatus("mandatory")
_TimeUpInterval_Type = DisplayString
_TimeUpInterval_Object = MibScalar
timeUpInterval = _TimeUpInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 2),
    _TimeUpInterval_Type()
)
timeUpInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeUpInterval.setStatus("mandatory")
_TimeSpanTotal_Type = DisplayString
_TimeSpanTotal_Object = MibScalar
timeSpanTotal = _TimeSpanTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 3),
    _TimeSpanTotal_Type()
)
timeSpanTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeSpanTotal.setStatus("mandatory")
_TimeSpanInterval_Type = DisplayString
_TimeSpanInterval_Object = MibScalar
timeSpanInterval = _TimeSpanInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 4),
    _TimeSpanInterval_Type()
)
timeSpanInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeSpanInterval.setStatus("mandatory")
_VgkLoginAttemptTotal_Type = Counter32
_VgkLoginAttemptTotal_Object = MibScalar
vgkLoginAttemptTotal = _VgkLoginAttemptTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 5),
    _VgkLoginAttemptTotal_Type()
)
vgkLoginAttemptTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgkLoginAttemptTotal.setStatus("mandatory")
_VgkLoginAttemptInterval_Type = Counter32
_VgkLoginAttemptInterval_Object = MibScalar
vgkLoginAttemptInterval = _VgkLoginAttemptInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 6),
    _VgkLoginAttemptInterval_Type()
)
vgkLoginAttemptInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgkLoginAttemptInterval.setStatus("mandatory")
_VgkLoginSuccessTotal_Type = Counter32
_VgkLoginSuccessTotal_Object = MibScalar
vgkLoginSuccessTotal = _VgkLoginSuccessTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 7),
    _VgkLoginSuccessTotal_Type()
)
vgkLoginSuccessTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgkLoginSuccessTotal.setStatus("mandatory")
_VgkLoginSuccessInterval_Type = Counter32
_VgkLoginSuccessInterval_Object = MibScalar
vgkLoginSuccessInterval = _VgkLoginSuccessInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 8),
    _VgkLoginSuccessInterval_Type()
)
vgkLoginSuccessInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgkLoginSuccessInterval.setStatus("mandatory")
_VgkLoginFailureTotal_Type = Counter32
_VgkLoginFailureTotal_Object = MibScalar
vgkLoginFailureTotal = _VgkLoginFailureTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 9),
    _VgkLoginFailureTotal_Type()
)
vgkLoginFailureTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgkLoginFailureTotal.setStatus("mandatory")
_VgkLoginFailureInterval_Type = Counter32
_VgkLoginFailureInterval_Object = MibScalar
vgkLoginFailureInterval = _VgkLoginFailureInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 10),
    _VgkLoginFailureInterval_Type()
)
vgkLoginFailureInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgkLoginFailureInterval.setStatus("mandatory")
_VgkLogoutAttemptTotal_Type = Counter32
_VgkLogoutAttemptTotal_Object = MibScalar
vgkLogoutAttemptTotal = _VgkLogoutAttemptTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 11),
    _VgkLogoutAttemptTotal_Type()
)
vgkLogoutAttemptTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgkLogoutAttemptTotal.setStatus("mandatory")
_VgkLogoutAttemptInterval_Type = Counter32
_VgkLogoutAttemptInterval_Object = MibScalar
vgkLogoutAttemptInterval = _VgkLogoutAttemptInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 12),
    _VgkLogoutAttemptInterval_Type()
)
vgkLogoutAttemptInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgkLogoutAttemptInterval.setStatus("mandatory")
_VgkLogoutSuccessTotal_Type = Counter32
_VgkLogoutSuccessTotal_Object = MibScalar
vgkLogoutSuccessTotal = _VgkLogoutSuccessTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 13),
    _VgkLogoutSuccessTotal_Type()
)
vgkLogoutSuccessTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgkLogoutSuccessTotal.setStatus("mandatory")
_VgkLogoutSuccessInterval_Type = Counter32
_VgkLogoutSuccessInterval_Object = MibScalar
vgkLogoutSuccessInterval = _VgkLogoutSuccessInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 14),
    _VgkLogoutSuccessInterval_Type()
)
vgkLogoutSuccessInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgkLogoutSuccessInterval.setStatus("mandatory")
_VgkLogoutFailureTotal_Type = Counter32
_VgkLogoutFailureTotal_Object = MibScalar
vgkLogoutFailureTotal = _VgkLogoutFailureTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 15),
    _VgkLogoutFailureTotal_Type()
)
vgkLogoutFailureTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgkLogoutFailureTotal.setStatus("mandatory")
_VgkLogoutFailureInterval_Type = Counter32
_VgkLogoutFailureInterval_Object = MibScalar
vgkLogoutFailureInterval = _VgkLogoutFailureInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 16),
    _VgkLogoutFailureInterval_Type()
)
vgkLogoutFailureInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgkLogoutFailureInterval.setStatus("mandatory")
_VgkDisconnectionTotal_Type = Counter32
_VgkDisconnectionTotal_Object = MibScalar
vgkDisconnectionTotal = _VgkDisconnectionTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 17),
    _VgkDisconnectionTotal_Type()
)
vgkDisconnectionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgkDisconnectionTotal.setStatus("mandatory")
_VgkDisconnectionInterval_Type = Counter32
_VgkDisconnectionInterval_Object = MibScalar
vgkDisconnectionInterval = _VgkDisconnectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 18),
    _VgkDisconnectionInterval_Type()
)
vgkDisconnectionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgkDisconnectionInterval.setStatus("mandatory")
_CallValue_Type = Integer32
_CallValue_Object = MibScalar
callValue = _CallValue_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 19),
    _CallValue_Type()
)
callValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callValue.setStatus("mandatory")
_CallInterval_Type = Counter32
_CallInterval_Object = MibScalar
callInterval = _CallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 20),
    _CallInterval_Type()
)
callInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callInterval.setStatus("mandatory")
_CallMaxTotal_Type = Integer32
_CallMaxTotal_Object = MibScalar
callMaxTotal = _CallMaxTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 21),
    _CallMaxTotal_Type()
)
callMaxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callMaxTotal.setStatus("mandatory")
_CallMaxInterval_Type = Integer32
_CallMaxInterval_Object = MibScalar
callMaxInterval = _CallMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 22),
    _CallMaxInterval_Type()
)
callMaxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callMaxInterval.setStatus("mandatory")
_CallAverageTotal_Type = Integer32
_CallAverageTotal_Object = MibScalar
callAverageTotal = _CallAverageTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 23),
    _CallAverageTotal_Type()
)
callAverageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAverageTotal.setStatus("mandatory")
_CallAverageInterval_Type = Integer32
_CallAverageInterval_Object = MibScalar
callAverageInterval = _CallAverageInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 24),
    _CallAverageInterval_Type()
)
callAverageInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAverageInterval.setStatus("mandatory")
_CallTotal_Type = Counter32
_CallTotal_Object = MibScalar
callTotal = _CallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 25),
    _CallTotal_Type()
)
callTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callTotal.setStatus("mandatory")
_UniversalCallValue_Type = Integer32
_UniversalCallValue_Object = MibScalar
universalCallValue = _UniversalCallValue_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 26),
    _UniversalCallValue_Type()
)
universalCallValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    universalCallValue.setStatus("mandatory")
_UniversalCallInterval_Type = Counter32
_UniversalCallInterval_Object = MibScalar
universalCallInterval = _UniversalCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 27),
    _UniversalCallInterval_Type()
)
universalCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    universalCallInterval.setStatus("mandatory")
_UniversalCallMaxTotal_Type = Integer32
_UniversalCallMaxTotal_Object = MibScalar
universalCallMaxTotal = _UniversalCallMaxTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 28),
    _UniversalCallMaxTotal_Type()
)
universalCallMaxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    universalCallMaxTotal.setStatus("mandatory")
_UniversalCallMaxInterval_Type = Integer32
_UniversalCallMaxInterval_Object = MibScalar
universalCallMaxInterval = _UniversalCallMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 29),
    _UniversalCallMaxInterval_Type()
)
universalCallMaxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    universalCallMaxInterval.setStatus("mandatory")
_UniversalCallAverageTotal_Type = Integer32
_UniversalCallAverageTotal_Object = MibScalar
universalCallAverageTotal = _UniversalCallAverageTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 30),
    _UniversalCallAverageTotal_Type()
)
universalCallAverageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    universalCallAverageTotal.setStatus("mandatory")
_UniversalCallAverageInterval_Type = Integer32
_UniversalCallAverageInterval_Object = MibScalar
universalCallAverageInterval = _UniversalCallAverageInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 31),
    _UniversalCallAverageInterval_Type()
)
universalCallAverageInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    universalCallAverageInterval.setStatus("mandatory")
_UniversalCallTotal_Type = Counter32
_UniversalCallTotal_Object = MibScalar
universalCallTotal = _UniversalCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 32),
    _UniversalCallTotal_Type()
)
universalCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    universalCallTotal.setStatus("mandatory")
_VoiceCallValue_Type = Integer32
_VoiceCallValue_Object = MibScalar
voiceCallValue = _VoiceCallValue_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 33),
    _VoiceCallValue_Type()
)
voiceCallValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallValue.setStatus("mandatory")
_VoiceCallInterval_Type = Counter32
_VoiceCallInterval_Object = MibScalar
voiceCallInterval = _VoiceCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 34),
    _VoiceCallInterval_Type()
)
voiceCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallInterval.setStatus("mandatory")
_VoiceCallMaxTotal_Type = Integer32
_VoiceCallMaxTotal_Object = MibScalar
voiceCallMaxTotal = _VoiceCallMaxTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 35),
    _VoiceCallMaxTotal_Type()
)
voiceCallMaxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallMaxTotal.setStatus("mandatory")
_VoiceCallMaxInterval_Type = Integer32
_VoiceCallMaxInterval_Object = MibScalar
voiceCallMaxInterval = _VoiceCallMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 36),
    _VoiceCallMaxInterval_Type()
)
voiceCallMaxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallMaxInterval.setStatus("mandatory")
_VoiceCallAverageTotal_Type = Integer32
_VoiceCallAverageTotal_Object = MibScalar
voiceCallAverageTotal = _VoiceCallAverageTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 37),
    _VoiceCallAverageTotal_Type()
)
voiceCallAverageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallAverageTotal.setStatus("mandatory")
_VoiceCallAverageInterval_Type = Integer32
_VoiceCallAverageInterval_Object = MibScalar
voiceCallAverageInterval = _VoiceCallAverageInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 38),
    _VoiceCallAverageInterval_Type()
)
voiceCallAverageInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallAverageInterval.setStatus("mandatory")
_VoiceCallTotal_Type = Counter32
_VoiceCallTotal_Object = MibScalar
voiceCallTotal = _VoiceCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 39),
    _VoiceCallTotal_Type()
)
voiceCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallTotal.setStatus("mandatory")
_FaxCallValue_Type = Integer32
_FaxCallValue_Object = MibScalar
faxCallValue = _FaxCallValue_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 40),
    _FaxCallValue_Type()
)
faxCallValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxCallValue.setStatus("mandatory")
_FaxCallInterval_Type = Counter32
_FaxCallInterval_Object = MibScalar
faxCallInterval = _FaxCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 41),
    _FaxCallInterval_Type()
)
faxCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxCallInterval.setStatus("mandatory")
_FaxCallMaxTotal_Type = Integer32
_FaxCallMaxTotal_Object = MibScalar
faxCallMaxTotal = _FaxCallMaxTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 42),
    _FaxCallMaxTotal_Type()
)
faxCallMaxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxCallMaxTotal.setStatus("mandatory")
_FaxCallMaxInterval_Type = Integer32
_FaxCallMaxInterval_Object = MibScalar
faxCallMaxInterval = _FaxCallMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 43),
    _FaxCallMaxInterval_Type()
)
faxCallMaxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxCallMaxInterval.setStatus("mandatory")
_FaxCallAverageTotal_Type = Integer32
_FaxCallAverageTotal_Object = MibScalar
faxCallAverageTotal = _FaxCallAverageTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 44),
    _FaxCallAverageTotal_Type()
)
faxCallAverageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxCallAverageTotal.setStatus("mandatory")
_FaxCallAverageInterval_Type = Integer32
_FaxCallAverageInterval_Object = MibScalar
faxCallAverageInterval = _FaxCallAverageInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 45),
    _FaxCallAverageInterval_Type()
)
faxCallAverageInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxCallAverageInterval.setStatus("mandatory")
_FaxCallTotal_Type = Counter32
_FaxCallTotal_Object = MibScalar
faxCallTotal = _FaxCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 46),
    _FaxCallTotal_Type()
)
faxCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxCallTotal.setStatus("mandatory")
_SncCallValue_Type = Integer32
_SncCallValue_Object = MibScalar
sncCallValue = _SncCallValue_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 47),
    _SncCallValue_Type()
)
sncCallValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sncCallValue.setStatus("mandatory")
_SncCallInterval_Type = Counter32
_SncCallInterval_Object = MibScalar
sncCallInterval = _SncCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 48),
    _SncCallInterval_Type()
)
sncCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sncCallInterval.setStatus("mandatory")
_SncCallMaxTotal_Type = Integer32
_SncCallMaxTotal_Object = MibScalar
sncCallMaxTotal = _SncCallMaxTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 49),
    _SncCallMaxTotal_Type()
)
sncCallMaxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sncCallMaxTotal.setStatus("mandatory")
_SncCallMaxInterval_Type = Integer32
_SncCallMaxInterval_Object = MibScalar
sncCallMaxInterval = _SncCallMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 50),
    _SncCallMaxInterval_Type()
)
sncCallMaxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sncCallMaxInterval.setStatus("mandatory")
_SncCallAverageTotal_Type = Integer32
_SncCallAverageTotal_Object = MibScalar
sncCallAverageTotal = _SncCallAverageTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 51),
    _SncCallAverageTotal_Type()
)
sncCallAverageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sncCallAverageTotal.setStatus("mandatory")
_SncCallAverageInterval_Type = Integer32
_SncCallAverageInterval_Object = MibScalar
sncCallAverageInterval = _SncCallAverageInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 52),
    _SncCallAverageInterval_Type()
)
sncCallAverageInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sncCallAverageInterval.setStatus("mandatory")
_SncCallTotal_Type = Counter32
_SncCallTotal_Object = MibScalar
sncCallTotal = _SncCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 53),
    _SncCallTotal_Type()
)
sncCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sncCallTotal.setStatus("mandatory")
_IPhoneCallValue_Type = Integer32
_IPhoneCallValue_Object = MibScalar
iPhoneCallValue = _IPhoneCallValue_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 54),
    _IPhoneCallValue_Type()
)
iPhoneCallValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPhoneCallValue.setStatus("mandatory")
_IPhoneCallInterval_Type = Counter32
_IPhoneCallInterval_Object = MibScalar
iPhoneCallInterval = _IPhoneCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 55),
    _IPhoneCallInterval_Type()
)
iPhoneCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPhoneCallInterval.setStatus("mandatory")
_IPhoneCallMaxTotal_Type = Integer32
_IPhoneCallMaxTotal_Object = MibScalar
iPhoneCallMaxTotal = _IPhoneCallMaxTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 56),
    _IPhoneCallMaxTotal_Type()
)
iPhoneCallMaxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPhoneCallMaxTotal.setStatus("mandatory")
_IPhoneCallMaxInterval_Type = Integer32
_IPhoneCallMaxInterval_Object = MibScalar
iPhoneCallMaxInterval = _IPhoneCallMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 57),
    _IPhoneCallMaxInterval_Type()
)
iPhoneCallMaxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPhoneCallMaxInterval.setStatus("mandatory")
_IPhoneCallAverageTotal_Type = Integer32
_IPhoneCallAverageTotal_Object = MibScalar
iPhoneCallAverageTotal = _IPhoneCallAverageTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 58),
    _IPhoneCallAverageTotal_Type()
)
iPhoneCallAverageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPhoneCallAverageTotal.setStatus("mandatory")
_IPhoneCallAverageInterval_Type = Integer32
_IPhoneCallAverageInterval_Object = MibScalar
iPhoneCallAverageInterval = _IPhoneCallAverageInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 59),
    _IPhoneCallAverageInterval_Type()
)
iPhoneCallAverageInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPhoneCallAverageInterval.setStatus("mandatory")
_IPhoneCallTotal_Type = Counter32
_IPhoneCallTotal_Object = MibScalar
iPhoneCallTotal = _IPhoneCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 60),
    _IPhoneCallTotal_Type()
)
iPhoneCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPhoneCallTotal.setStatus("mandatory")
_DialerCallValue_Type = Integer32
_DialerCallValue_Object = MibScalar
dialerCallValue = _DialerCallValue_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 61),
    _DialerCallValue_Type()
)
dialerCallValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerCallValue.setStatus("mandatory")
_DialerCallInterval_Type = Counter32
_DialerCallInterval_Object = MibScalar
dialerCallInterval = _DialerCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 62),
    _DialerCallInterval_Type()
)
dialerCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerCallInterval.setStatus("mandatory")
_DialerCallMaxTotal_Type = Integer32
_DialerCallMaxTotal_Object = MibScalar
dialerCallMaxTotal = _DialerCallMaxTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 63),
    _DialerCallMaxTotal_Type()
)
dialerCallMaxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerCallMaxTotal.setStatus("mandatory")
_DialerCallMaxInterval_Type = Integer32
_DialerCallMaxInterval_Object = MibScalar
dialerCallMaxInterval = _DialerCallMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 64),
    _DialerCallMaxInterval_Type()
)
dialerCallMaxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerCallMaxInterval.setStatus("mandatory")
_DialerCallAverageTotal_Type = Integer32
_DialerCallAverageTotal_Object = MibScalar
dialerCallAverageTotal = _DialerCallAverageTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 65),
    _DialerCallAverageTotal_Type()
)
dialerCallAverageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerCallAverageTotal.setStatus("mandatory")
_DialerCallAverageInterval_Type = Integer32
_DialerCallAverageInterval_Object = MibScalar
dialerCallAverageInterval = _DialerCallAverageInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 66),
    _DialerCallAverageInterval_Type()
)
dialerCallAverageInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerCallAverageInterval.setStatus("mandatory")
_DialerCallTotal_Type = Counter32
_DialerCallTotal_Object = MibScalar
dialerCallTotal = _DialerCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 67),
    _DialerCallTotal_Type()
)
dialerCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerCallTotal.setStatus("mandatory")
_IncorrectPasswordCallTotal_Type = Counter32
_IncorrectPasswordCallTotal_Object = MibScalar
incorrectPasswordCallTotal = _IncorrectPasswordCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 68),
    _IncorrectPasswordCallTotal_Type()
)
incorrectPasswordCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incorrectPasswordCallTotal.setStatus("mandatory")
_IncorrectPasswordCallInterval_Type = Counter32
_IncorrectPasswordCallInterval_Object = MibScalar
incorrectPasswordCallInterval = _IncorrectPasswordCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 69),
    _IncorrectPasswordCallInterval_Type()
)
incorrectPasswordCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incorrectPasswordCallInterval.setStatus("mandatory")
_NotSupportedCallTotal_Type = Counter32
_NotSupportedCallTotal_Object = MibScalar
notSupportedCallTotal = _NotSupportedCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 72),
    _NotSupportedCallTotal_Type()
)
notSupportedCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notSupportedCallTotal.setStatus("mandatory")
_NotSupportedCallInterval_Type = Counter32
_NotSupportedCallInterval_Object = MibScalar
notSupportedCallInterval = _NotSupportedCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 73),
    _NotSupportedCallInterval_Type()
)
notSupportedCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notSupportedCallInterval.setStatus("mandatory")
_IncomingInternetAttemptCallValue_Type = Integer32
_IncomingInternetAttemptCallValue_Object = MibScalar
incomingInternetAttemptCallValue = _IncomingInternetAttemptCallValue_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 74),
    _IncomingInternetAttemptCallValue_Type()
)
incomingInternetAttemptCallValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingInternetAttemptCallValue.setStatus("mandatory")
_IncomingInternetAttemptCallInterval_Type = Counter32
_IncomingInternetAttemptCallInterval_Object = MibScalar
incomingInternetAttemptCallInterval = _IncomingInternetAttemptCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 75),
    _IncomingInternetAttemptCallInterval_Type()
)
incomingInternetAttemptCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingInternetAttemptCallInterval.setStatus("mandatory")
_IncomingInternetAttemptCallMaxTotal_Type = Integer32
_IncomingInternetAttemptCallMaxTotal_Object = MibScalar
incomingInternetAttemptCallMaxTotal = _IncomingInternetAttemptCallMaxTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 76),
    _IncomingInternetAttemptCallMaxTotal_Type()
)
incomingInternetAttemptCallMaxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingInternetAttemptCallMaxTotal.setStatus("mandatory")
_IncomingInternetAttemptCallMaxInterval_Type = Integer32
_IncomingInternetAttemptCallMaxInterval_Object = MibScalar
incomingInternetAttemptCallMaxInterval = _IncomingInternetAttemptCallMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 77),
    _IncomingInternetAttemptCallMaxInterval_Type()
)
incomingInternetAttemptCallMaxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingInternetAttemptCallMaxInterval.setStatus("mandatory")
_IncomingInternetAttemptCallAverageTotal_Type = Integer32
_IncomingInternetAttemptCallAverageTotal_Object = MibScalar
incomingInternetAttemptCallAverageTotal = _IncomingInternetAttemptCallAverageTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 78),
    _IncomingInternetAttemptCallAverageTotal_Type()
)
incomingInternetAttemptCallAverageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingInternetAttemptCallAverageTotal.setStatus("mandatory")
_IncomingInternetAttemptCallAverageInterval_Type = Integer32
_IncomingInternetAttemptCallAverageInterval_Object = MibScalar
incomingInternetAttemptCallAverageInterval = _IncomingInternetAttemptCallAverageInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 79),
    _IncomingInternetAttemptCallAverageInterval_Type()
)
incomingInternetAttemptCallAverageInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingInternetAttemptCallAverageInterval.setStatus("mandatory")
_IncomingInternetAttemptCallTotal_Type = Counter32
_IncomingInternetAttemptCallTotal_Object = MibScalar
incomingInternetAttemptCallTotal = _IncomingInternetAttemptCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 80),
    _IncomingInternetAttemptCallTotal_Type()
)
incomingInternetAttemptCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingInternetAttemptCallTotal.setStatus("mandatory")
_IncomingInternetSuccessCallValue_Type = Integer32
_IncomingInternetSuccessCallValue_Object = MibScalar
incomingInternetSuccessCallValue = _IncomingInternetSuccessCallValue_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 81),
    _IncomingInternetSuccessCallValue_Type()
)
incomingInternetSuccessCallValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingInternetSuccessCallValue.setStatus("mandatory")
_IncomingInternetSuccessCallInterval_Type = Counter32
_IncomingInternetSuccessCallInterval_Object = MibScalar
incomingInternetSuccessCallInterval = _IncomingInternetSuccessCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 82),
    _IncomingInternetSuccessCallInterval_Type()
)
incomingInternetSuccessCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingInternetSuccessCallInterval.setStatus("mandatory")
_IncomingInternetSuccessCallMaxTotal_Type = Integer32
_IncomingInternetSuccessCallMaxTotal_Object = MibScalar
incomingInternetSuccessCallMaxTotal = _IncomingInternetSuccessCallMaxTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 83),
    _IncomingInternetSuccessCallMaxTotal_Type()
)
incomingInternetSuccessCallMaxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingInternetSuccessCallMaxTotal.setStatus("mandatory")
_IncomingInternetSuccessCallMaxInterval_Type = Integer32
_IncomingInternetSuccessCallMaxInterval_Object = MibScalar
incomingInternetSuccessCallMaxInterval = _IncomingInternetSuccessCallMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 84),
    _IncomingInternetSuccessCallMaxInterval_Type()
)
incomingInternetSuccessCallMaxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingInternetSuccessCallMaxInterval.setStatus("mandatory")
_IncomingInternetSuccessCallAverageTotal_Type = Integer32
_IncomingInternetSuccessCallAverageTotal_Object = MibScalar
incomingInternetSuccessCallAverageTotal = _IncomingInternetSuccessCallAverageTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 85),
    _IncomingInternetSuccessCallAverageTotal_Type()
)
incomingInternetSuccessCallAverageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingInternetSuccessCallAverageTotal.setStatus("mandatory")
_IncomingInternetSuccessCallAverageInterval_Type = Integer32
_IncomingInternetSuccessCallAverageInterval_Object = MibScalar
incomingInternetSuccessCallAverageInterval = _IncomingInternetSuccessCallAverageInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 86),
    _IncomingInternetSuccessCallAverageInterval_Type()
)
incomingInternetSuccessCallAverageInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingInternetSuccessCallAverageInterval.setStatus("mandatory")
_IncomingInternetSuccessCallTotal_Type = Counter32
_IncomingInternetSuccessCallTotal_Object = MibScalar
incomingInternetSuccessCallTotal = _IncomingInternetSuccessCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 87),
    _IncomingInternetSuccessCallTotal_Type()
)
incomingInternetSuccessCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingInternetSuccessCallTotal.setStatus("mandatory")
_IncomingTelephonyAttemptCallValue_Type = Integer32
_IncomingTelephonyAttemptCallValue_Object = MibScalar
incomingTelephonyAttemptCallValue = _IncomingTelephonyAttemptCallValue_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 88),
    _IncomingTelephonyAttemptCallValue_Type()
)
incomingTelephonyAttemptCallValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingTelephonyAttemptCallValue.setStatus("mandatory")
_IncomingTelephonyAttemptCallInterval_Type = Counter32
_IncomingTelephonyAttemptCallInterval_Object = MibScalar
incomingTelephonyAttemptCallInterval = _IncomingTelephonyAttemptCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 89),
    _IncomingTelephonyAttemptCallInterval_Type()
)
incomingTelephonyAttemptCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingTelephonyAttemptCallInterval.setStatus("mandatory")
_IncomingTelephonyAttemptCallMaxTotal_Type = Integer32
_IncomingTelephonyAttemptCallMaxTotal_Object = MibScalar
incomingTelephonyAttemptCallMaxTotal = _IncomingTelephonyAttemptCallMaxTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 90),
    _IncomingTelephonyAttemptCallMaxTotal_Type()
)
incomingTelephonyAttemptCallMaxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingTelephonyAttemptCallMaxTotal.setStatus("mandatory")
_IncomingTelephonyAttemptCallMaxInterval_Type = Integer32
_IncomingTelephonyAttemptCallMaxInterval_Object = MibScalar
incomingTelephonyAttemptCallMaxInterval = _IncomingTelephonyAttemptCallMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 91),
    _IncomingTelephonyAttemptCallMaxInterval_Type()
)
incomingTelephonyAttemptCallMaxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingTelephonyAttemptCallMaxInterval.setStatus("mandatory")
_IncomingTelephonyAttemptCallAverageTotal_Type = Integer32
_IncomingTelephonyAttemptCallAverageTotal_Object = MibScalar
incomingTelephonyAttemptCallAverageTotal = _IncomingTelephonyAttemptCallAverageTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 92),
    _IncomingTelephonyAttemptCallAverageTotal_Type()
)
incomingTelephonyAttemptCallAverageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingTelephonyAttemptCallAverageTotal.setStatus("mandatory")
_IncomingTelephonyAttemptCallAverageInterval_Type = Integer32
_IncomingTelephonyAttemptCallAverageInterval_Object = MibScalar
incomingTelephonyAttemptCallAverageInterval = _IncomingTelephonyAttemptCallAverageInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 93),
    _IncomingTelephonyAttemptCallAverageInterval_Type()
)
incomingTelephonyAttemptCallAverageInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingTelephonyAttemptCallAverageInterval.setStatus("mandatory")
_IncomingTelephonyAttemptCallTotal_Type = Counter32
_IncomingTelephonyAttemptCallTotal_Object = MibScalar
incomingTelephonyAttemptCallTotal = _IncomingTelephonyAttemptCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 94),
    _IncomingTelephonyAttemptCallTotal_Type()
)
incomingTelephonyAttemptCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingTelephonyAttemptCallTotal.setStatus("mandatory")
_IncomingTelephonySuccessCallValue_Type = Integer32
_IncomingTelephonySuccessCallValue_Object = MibScalar
incomingTelephonySuccessCallValue = _IncomingTelephonySuccessCallValue_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 95),
    _IncomingTelephonySuccessCallValue_Type()
)
incomingTelephonySuccessCallValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingTelephonySuccessCallValue.setStatus("mandatory")
_IncomingTelephonySuccessCallInterval_Type = Counter32
_IncomingTelephonySuccessCallInterval_Object = MibScalar
incomingTelephonySuccessCallInterval = _IncomingTelephonySuccessCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 96),
    _IncomingTelephonySuccessCallInterval_Type()
)
incomingTelephonySuccessCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingTelephonySuccessCallInterval.setStatus("mandatory")
_IncomingTelephonySuccessCallMaxTotal_Type = Integer32
_IncomingTelephonySuccessCallMaxTotal_Object = MibScalar
incomingTelephonySuccessCallMaxTotal = _IncomingTelephonySuccessCallMaxTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 97),
    _IncomingTelephonySuccessCallMaxTotal_Type()
)
incomingTelephonySuccessCallMaxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingTelephonySuccessCallMaxTotal.setStatus("mandatory")
_IncomingTelephonySuccessCallMaxInterval_Type = Integer32
_IncomingTelephonySuccessCallMaxInterval_Object = MibScalar
incomingTelephonySuccessCallMaxInterval = _IncomingTelephonySuccessCallMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 98),
    _IncomingTelephonySuccessCallMaxInterval_Type()
)
incomingTelephonySuccessCallMaxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingTelephonySuccessCallMaxInterval.setStatus("mandatory")
_IncomingTelephonySuccessCallAverageTotal_Type = Integer32
_IncomingTelephonySuccessCallAverageTotal_Object = MibScalar
incomingTelephonySuccessCallAverageTotal = _IncomingTelephonySuccessCallAverageTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 99),
    _IncomingTelephonySuccessCallAverageTotal_Type()
)
incomingTelephonySuccessCallAverageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingTelephonySuccessCallAverageTotal.setStatus("mandatory")
_IncomingTelephonySuccessCallAverageInterval_Type = Integer32
_IncomingTelephonySuccessCallAverageInterval_Object = MibScalar
incomingTelephonySuccessCallAverageInterval = _IncomingTelephonySuccessCallAverageInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 100),
    _IncomingTelephonySuccessCallAverageInterval_Type()
)
incomingTelephonySuccessCallAverageInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingTelephonySuccessCallAverageInterval.setStatus("mandatory")
_IncomingTelephonySuccessCallTotal_Type = Counter32
_IncomingTelephonySuccessCallTotal_Object = MibScalar
incomingTelephonySuccessCallTotal = _IncomingTelephonySuccessCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 101),
    _IncomingTelephonySuccessCallTotal_Type()
)
incomingTelephonySuccessCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incomingTelephonySuccessCallTotal.setStatus("mandatory")
_OutgoingInternetCallValue_Type = Integer32
_OutgoingInternetCallValue_Object = MibScalar
outgoingInternetCallValue = _OutgoingInternetCallValue_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 102),
    _OutgoingInternetCallValue_Type()
)
outgoingInternetCallValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingInternetCallValue.setStatus("mandatory")
_OutgoingInternetCallInterval_Type = Counter32
_OutgoingInternetCallInterval_Object = MibScalar
outgoingInternetCallInterval = _OutgoingInternetCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 103),
    _OutgoingInternetCallInterval_Type()
)
outgoingInternetCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingInternetCallInterval.setStatus("mandatory")
_OutgoingInternetCallMaxTotal_Type = Integer32
_OutgoingInternetCallMaxTotal_Object = MibScalar
outgoingInternetCallMaxTotal = _OutgoingInternetCallMaxTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 104),
    _OutgoingInternetCallMaxTotal_Type()
)
outgoingInternetCallMaxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingInternetCallMaxTotal.setStatus("mandatory")
_OutgoingInternetCallMaxInterval_Type = Integer32
_OutgoingInternetCallMaxInterval_Object = MibScalar
outgoingInternetCallMaxInterval = _OutgoingInternetCallMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 105),
    _OutgoingInternetCallMaxInterval_Type()
)
outgoingInternetCallMaxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingInternetCallMaxInterval.setStatus("mandatory")
_OutgoingInternetCallAverageTotal_Type = Integer32
_OutgoingInternetCallAverageTotal_Object = MibScalar
outgoingInternetCallAverageTotal = _OutgoingInternetCallAverageTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 106),
    _OutgoingInternetCallAverageTotal_Type()
)
outgoingInternetCallAverageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingInternetCallAverageTotal.setStatus("mandatory")
_OutgoingInternetCallAverageInterval_Type = Integer32
_OutgoingInternetCallAverageInterval_Object = MibScalar
outgoingInternetCallAverageInterval = _OutgoingInternetCallAverageInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 107),
    _OutgoingInternetCallAverageInterval_Type()
)
outgoingInternetCallAverageInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingInternetCallAverageInterval.setStatus("mandatory")
_OutgoingInternetCallTotal_Type = Counter32
_OutgoingInternetCallTotal_Object = MibScalar
outgoingInternetCallTotal = _OutgoingInternetCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 108),
    _OutgoingInternetCallTotal_Type()
)
outgoingInternetCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingInternetCallTotal.setStatus("mandatory")
_OutgoingTelephonyCallValue_Type = Integer32
_OutgoingTelephonyCallValue_Object = MibScalar
outgoingTelephonyCallValue = _OutgoingTelephonyCallValue_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 109),
    _OutgoingTelephonyCallValue_Type()
)
outgoingTelephonyCallValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingTelephonyCallValue.setStatus("mandatory")
_OutgoingTelephonyCallInterval_Type = Counter32
_OutgoingTelephonyCallInterval_Object = MibScalar
outgoingTelephonyCallInterval = _OutgoingTelephonyCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 110),
    _OutgoingTelephonyCallInterval_Type()
)
outgoingTelephonyCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingTelephonyCallInterval.setStatus("mandatory")
_OutgoingTelephonyCallMaxTotal_Type = Integer32
_OutgoingTelephonyCallMaxTotal_Object = MibScalar
outgoingTelephonyCallMaxTotal = _OutgoingTelephonyCallMaxTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 111),
    _OutgoingTelephonyCallMaxTotal_Type()
)
outgoingTelephonyCallMaxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingTelephonyCallMaxTotal.setStatus("mandatory")
_OutgoingTelephonyCallMaxInterval_Type = Integer32
_OutgoingTelephonyCallMaxInterval_Object = MibScalar
outgoingTelephonyCallMaxInterval = _OutgoingTelephonyCallMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 112),
    _OutgoingTelephonyCallMaxInterval_Type()
)
outgoingTelephonyCallMaxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingTelephonyCallMaxInterval.setStatus("mandatory")
_OutgoingTelephonyCallAverageTotal_Type = Integer32
_OutgoingTelephonyCallAverageTotal_Object = MibScalar
outgoingTelephonyCallAverageTotal = _OutgoingTelephonyCallAverageTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 113),
    _OutgoingTelephonyCallAverageTotal_Type()
)
outgoingTelephonyCallAverageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingTelephonyCallAverageTotal.setStatus("mandatory")
_OutgoingTelephonyCallAverageInterval_Type = Integer32
_OutgoingTelephonyCallAverageInterval_Object = MibScalar
outgoingTelephonyCallAverageInterval = _OutgoingTelephonyCallAverageInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 114),
    _OutgoingTelephonyCallAverageInterval_Type()
)
outgoingTelephonyCallAverageInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingTelephonyCallAverageInterval.setStatus("mandatory")
_OutgoingTelephonyCallTotal_Type = Counter32
_OutgoingTelephonyCallTotal_Object = MibScalar
outgoingTelephonyCallTotal = _OutgoingTelephonyCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 115),
    _OutgoingTelephonyCallTotal_Type()
)
outgoingTelephonyCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingTelephonyCallTotal.setStatus("mandatory")
_AccountExpiredCallTotal_Type = Counter32
_AccountExpiredCallTotal_Object = MibScalar
accountExpiredCallTotal = _AccountExpiredCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 116),
    _AccountExpiredCallTotal_Type()
)
accountExpiredCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountExpiredCallTotal.setStatus("mandatory")
_AccountExpiredCallInterval_Type = Counter32
_AccountExpiredCallInterval_Object = MibScalar
accountExpiredCallInterval = _AccountExpiredCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 117),
    _AccountExpiredCallInterval_Type()
)
accountExpiredCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountExpiredCallInterval.setStatus("mandatory")
_VgkNotAvailableCallTotal_Type = Counter32
_VgkNotAvailableCallTotal_Object = MibScalar
vgkNotAvailableCallTotal = _VgkNotAvailableCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 118),
    _VgkNotAvailableCallTotal_Type()
)
vgkNotAvailableCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgkNotAvailableCallTotal.setStatus("mandatory")
_VgkNotAvailableCallInterval_Type = Counter32
_VgkNotAvailableCallInterval_Object = MibScalar
vgkNotAvailableCallInterval = _VgkNotAvailableCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 119),
    _VgkNotAvailableCallInterval_Type()
)
vgkNotAvailableCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vgkNotAvailableCallInterval.setStatus("mandatory")
_VtgShutDownCallTotal_Type = Counter32
_VtgShutDownCallTotal_Object = MibScalar
vtgShutDownCallTotal = _VtgShutDownCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 120),
    _VtgShutDownCallTotal_Type()
)
vtgShutDownCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtgShutDownCallTotal.setStatus("mandatory")
_VtgShutDownCallInterval_Type = Counter32
_VtgShutDownCallInterval_Object = MibScalar
vtgShutDownCallInterval = _VtgShutDownCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 121),
    _VtgShutDownCallInterval_Type()
)
vtgShutDownCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtgShutDownCallInterval.setStatus("mandatory")
_VtgOutOfHoursCallTotal_Type = Counter32
_VtgOutOfHoursCallTotal_Object = MibScalar
vtgOutOfHoursCallTotal = _VtgOutOfHoursCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 122),
    _VtgOutOfHoursCallTotal_Type()
)
vtgOutOfHoursCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtgOutOfHoursCallTotal.setStatus("mandatory")
_VtgOutOfHoursCallInterval_Type = Counter32
_VtgOutOfHoursCallInterval_Object = MibScalar
vtgOutOfHoursCallInterval = _VtgOutOfHoursCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 123),
    _VtgOutOfHoursCallInterval_Type()
)
vtgOutOfHoursCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtgOutOfHoursCallInterval.setStatus("mandatory")
_VtgBusyCallTotal_Type = Counter32
_VtgBusyCallTotal_Object = MibScalar
vtgBusyCallTotal = _VtgBusyCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 124),
    _VtgBusyCallTotal_Type()
)
vtgBusyCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtgBusyCallTotal.setStatus("mandatory")
_VtgBusyCallInterval_Type = Counter32
_VtgBusyCallInterval_Object = MibScalar
vtgBusyCallInterval = _VtgBusyCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 125),
    _VtgBusyCallInterval_Type()
)
vtgBusyCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtgBusyCallInterval.setStatus("mandatory")
_VtgNoAnswerCallTotal_Type = Counter32
_VtgNoAnswerCallTotal_Object = MibScalar
vtgNoAnswerCallTotal = _VtgNoAnswerCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 126),
    _VtgNoAnswerCallTotal_Type()
)
vtgNoAnswerCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtgNoAnswerCallTotal.setStatus("mandatory")
_VtgNoAnswerCallInterval_Type = Counter32
_VtgNoAnswerCallInterval_Object = MibScalar
vtgNoAnswerCallInterval = _VtgNoAnswerCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 127),
    _VtgNoAnswerCallInterval_Type()
)
vtgNoAnswerCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtgNoAnswerCallInterval.setStatus("mandatory")
_TelephoneBusyCallTotal_Type = Counter32
_TelephoneBusyCallTotal_Object = MibScalar
telephoneBusyCallTotal = _TelephoneBusyCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 128),
    _TelephoneBusyCallTotal_Type()
)
telephoneBusyCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephoneBusyCallTotal.setStatus("mandatory")
_TelephoneBusyCallInterval_Type = Counter32
_TelephoneBusyCallInterval_Object = MibScalar
telephoneBusyCallInterval = _TelephoneBusyCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 129),
    _TelephoneBusyCallInterval_Type()
)
telephoneBusyCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephoneBusyCallInterval.setStatus("mandatory")
_TelephoneNoAnswerCallTotal_Type = Counter32
_TelephoneNoAnswerCallTotal_Object = MibScalar
telephoneNoAnswerCallTotal = _TelephoneNoAnswerCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 130),
    _TelephoneNoAnswerCallTotal_Type()
)
telephoneNoAnswerCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephoneNoAnswerCallTotal.setStatus("mandatory")
_TelephoneNoAnswerCallInterval_Type = Counter32
_TelephoneNoAnswerCallInterval_Object = MibScalar
telephoneNoAnswerCallInterval = _TelephoneNoAnswerCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 131),
    _TelephoneNoAnswerCallInterval_Type()
)
telephoneNoAnswerCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephoneNoAnswerCallInterval.setStatus("mandatory")
_MiscReasonDisconnectedCallTotal_Type = Counter32
_MiscReasonDisconnectedCallTotal_Object = MibScalar
miscReasonDisconnectedCallTotal = _MiscReasonDisconnectedCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 132),
    _MiscReasonDisconnectedCallTotal_Type()
)
miscReasonDisconnectedCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscReasonDisconnectedCallTotal.setStatus("mandatory")
_MiscReasonDisconnectedCallInterval_Type = Counter32
_MiscReasonDisconnectedCallInterval_Object = MibScalar
miscReasonDisconnectedCallInterval = _MiscReasonDisconnectedCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 133),
    _MiscReasonDisconnectedCallInterval_Type()
)
miscReasonDisconnectedCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscReasonDisconnectedCallInterval.setStatus("mandatory")
_TotalDisconnectedCallsTotal_Type = Counter32
_TotalDisconnectedCallsTotal_Object = MibScalar
totalDisconnectedCallsTotal = _TotalDisconnectedCallsTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 134),
    _TotalDisconnectedCallsTotal_Type()
)
totalDisconnectedCallsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalDisconnectedCallsTotal.setStatus("mandatory")
_TotalDisconnectedCallsInterval_Type = Counter32
_TotalDisconnectedCallsInterval_Object = MibScalar
totalDisconnectedCallsInterval = _TotalDisconnectedCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 135),
    _TotalDisconnectedCallsInterval_Type()
)
totalDisconnectedCallsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalDisconnectedCallsInterval.setStatus("mandatory")
_VtgOutOfServiceCallTotal_Type = Counter32
_VtgOutOfServiceCallTotal_Object = MibScalar
vtgOutOfServiceCallTotal = _VtgOutOfServiceCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 136),
    _VtgOutOfServiceCallTotal_Type()
)
vtgOutOfServiceCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtgOutOfServiceCallTotal.setStatus("mandatory")
_VtgOutOfServiceCallInterval_Type = Counter32
_VtgOutOfServiceCallInterval_Object = MibScalar
vtgOutOfServiceCallInterval = _VtgOutOfServiceCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 137),
    _VtgOutOfServiceCallInterval_Type()
)
vtgOutOfServiceCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtgOutOfServiceCallInterval.setStatus("mandatory")
_UnauthorizedUserCallTotal_Type = Counter32
_UnauthorizedUserCallTotal_Object = MibScalar
unauthorizedUserCallTotal = _UnauthorizedUserCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 138),
    _UnauthorizedUserCallTotal_Type()
)
unauthorizedUserCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unauthorizedUserCallTotal.setStatus("mandatory")
_UnauthorizedUserCallInterval_Type = Counter32
_UnauthorizedUserCallInterval_Object = MibScalar
unauthorizedUserCallInterval = _UnauthorizedUserCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 139),
    _UnauthorizedUserCallInterval_Type()
)
unauthorizedUserCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unauthorizedUserCallInterval.setStatus("mandatory")
_ResolveFailureCallTotal_Type = Counter32
_ResolveFailureCallTotal_Object = MibScalar
resolveFailureCallTotal = _ResolveFailureCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 140),
    _ResolveFailureCallTotal_Type()
)
resolveFailureCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resolveFailureCallTotal.setStatus("mandatory")
_ResolveFailureCallInterval_Type = Counter32
_ResolveFailureCallInterval_Object = MibScalar
resolveFailureCallInterval = _ResolveFailureCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 141),
    _ResolveFailureCallInterval_Type()
)
resolveFailureCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resolveFailureCallInterval.setStatus("mandatory")
_PstnFailureCallTotal_Type = Counter32
_PstnFailureCallTotal_Object = MibScalar
pstnFailureCallTotal = _PstnFailureCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 142),
    _PstnFailureCallTotal_Type()
)
pstnFailureCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pstnFailureCallTotal.setStatus("mandatory")
_PstnFailureCallInterval_Type = Counter32
_PstnFailureCallInterval_Object = MibScalar
pstnFailureCallInterval = _PstnFailureCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 143),
    _PstnFailureCallInterval_Type()
)
pstnFailureCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pstnFailureCallInterval.setStatus("mandatory")
_AbnormalTerminationCallTotal_Type = Counter32
_AbnormalTerminationCallTotal_Object = MibScalar
abnormalTerminationCallTotal = _AbnormalTerminationCallTotal_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 144),
    _AbnormalTerminationCallTotal_Type()
)
abnormalTerminationCallTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    abnormalTerminationCallTotal.setStatus("mandatory")
_AbnormalTerminationCallInterval_Type = Counter32
_AbnormalTerminationCallInterval_Object = MibScalar
abnormalTerminationCallInterval = _AbnormalTerminationCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 8, 145),
    _AbnormalTerminationCallInterval_Type()
)
abnormalTerminationCallInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    abnormalTerminationCallInterval.setStatus("mandatory")
_TrapParameters_ObjectIdentity = ObjectIdentity
trapParameters = _TrapParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516, 2, 9)
)
_TelephonyErrorDescription_Type = DisplayString
_TelephonyErrorDescription_Object = MibScalar
telephonyErrorDescription = _TelephonyErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 2516, 2, 9, 1),
    _TelephonyErrorDescription_Type()
)
telephonyErrorDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    telephonyErrorDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects

setParameterFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2516, 2, 0, 1)
)
if mibBuilder.loadTexts:
    setParameterFailure.setStatus(
        ""
    )

haspExistance = NotificationType(
    (1, 3, 6, 1, 4, 1, 2516, 2, 0, 2)
)
if mibBuilder.loadTexts:
    haspExistance.setStatus(
        ""
    )

cti2ServiceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2516, 2, 0, 3)
)
if mibBuilder.loadTexts:
    cti2ServiceFailure.setStatus(
        ""
    )

vgkLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2516, 2, 0, 4)
)
if mibBuilder.loadTexts:
    vgkLoginFailure.setStatus(
        ""
    )

vgkLogoutFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2516, 2, 0, 5)
)
if mibBuilder.loadTexts:
    vgkLogoutFailure.setStatus(
        ""
    )

vgkDisconnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2516, 2, 0, 6)
)
if mibBuilder.loadTexts:
    vgkDisconnection.setStatus(
        ""
    )

telephonyError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2516, 2, 0, 7)
)
telephonyError.setObjects(
    ("VTGW-MIB", "telephonyErrorDescription")
)
if mibBuilder.loadTexts:
    telephonyError.setStatus(
        ""
    )

incorrectPasswordCalls = NotificationType(
    (1, 3, 6, 1, 4, 1, 2516, 2, 0, 8)
)
if mibBuilder.loadTexts:
    incorrectPasswordCalls.setStatus(
        ""
    )

disconnectedCalls = NotificationType(
    (1, 3, 6, 1, 4, 1, 2516, 2, 0, 9)
)
if mibBuilder.loadTexts:
    disconnectedCalls.setStatus(
        ""
    )

notSupportedCalls = NotificationType(
    (1, 3, 6, 1, 4, 1, 2516, 2, 0, 10)
)
if mibBuilder.loadTexts:
    notSupportedCalls.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VTGW-MIB",
    **{"vocaltec": vocaltec,
       "vtg": vtg,
       "setParameterFailure": setParameterFailure,
       "haspExistance": haspExistance,
       "cti2ServiceFailure": cti2ServiceFailure,
       "vgkLoginFailure": vgkLoginFailure,
       "vgkLogoutFailure": vgkLogoutFailure,
       "vgkDisconnection": vgkDisconnection,
       "telephonyError": telephonyError,
       "incorrectPasswordCalls": incorrectPasswordCalls,
       "disconnectedCalls": disconnectedCalls,
       "notSupportedCalls": notSupportedCalls,
       "tgw": tgw,
       "softwareVersion": softwareVersion,
       "cti2Service": cti2Service,
       "resloveMode": resloveMode,
       "telephonyProtocol": telephonyProtocol,
       "internetProtocol": internetProtocol,
       "universalLinesNumber": universalLinesNumber,
       "voiceLinesNumber": voiceLinesNumber,
       "faxLinesNumber": faxLinesNumber,
       "sncLinesNumber": sncLinesNumber,
       "iPhoneLinesNumber": iPhoneLinesNumber,
       "dialerLinesNumber": dialerLinesNumber,
       "cti2ServicePollingQuantum": cti2ServicePollingQuantum,
       "vnmvgk": vnmvgk,
       "rcamPort": rcamPort,
       "id": id,
       "alias": alias,
       "time2Live": time2Live,
       "loginSetAttempts": loginSetAttempts,
       "timeB4LoginAttempt": timeB4LoginAttempt,
       "timeB4LoginSet": timeB4LoginSet,
       "rasPort": rasPort,
       "hasp": hasp,
       "audio": audio,
       "codecsPriorities": codecsPriorities,
       "preferredCodec": preferredCodec,
       "outputGain": outputGain,
       "inputGain": inputGain,
       "codecsTable": codecsTable,
       "codecEntry": codecEntry,
       "coder": coder,
       "vadEnable": vadEnable,
       "coderRate": coderRate,
       "framesPerPkt": framesPerPkt,
       "framesSize": framesSize,
       "jitter": jitter,
       "jitterOptFactor": jitterOptFactor,
       "coderRedundency": coderRedundency,
       "ports": ports,
       "portsTable": portsTable,
       "portEntry": portEntry,
       "portNumber": portNumber,
       "portEnable": portEnable,
       "connectedTo": connectedTo,
       "boundDirection": boundDirection,
       "dialingMode": dialingMode,
       "detectionMode": detectionMode,
       "ivrMode": ivrMode,
       "repeatIVR": repeatIVR,
       "overSilenceTime": overSilenceTime,
       "comment": comment,
       "ivr": ivr,
       "interDigitTimeout": interDigitTimeout,
       "digitsTimeout": digitsTimeout,
       "telephonyProtocols": telephonyProtocols,
       "analog": analog,
       "ringCount": ringCount,
       "volume": volume,
       "enm": enm,
       "idle": idle,
       "outOfService": outOfService,
       "seizeOutbound": seizeOutbound,
       "seizeInbound": seizeInbound,
       "seizeAckOutbound": seizeAckOutbound,
       "seizeAckInbound": seizeAckInbound,
       "answerOutbound": answerOutbound,
       "answerInbound": answerInbound,
       "dropOutbound": dropOutbound,
       "dropInbound": dropInbound,
       "noAnswerSec": noAnswerSec,
       "continuesNoSignal": continuesNoSignal,
       "helloEdge": helloEdge,
       "maxInterRing": maxInterRing,
       "dialToneLocal": dialToneLocal,
       "dialToneIntl": dialToneIntl,
       "dialToneXtra": dialToneXtra,
       "busy1Tone": busy1Tone,
       "busy2Tone": busy2Tone,
       "ringback1Tone": ringback1Tone,
       "ringback2Tone": ringback2Tone,
       "disconnect1Tone": disconnect1Tone,
       "disconnect2Tone": disconnect2Tone,
       "waitForDropAckTimer": waitForDropAckTimer,
       "waitForSiezeAckTimer": waitForSiezeAckTimer,
       "digitsMode": digitsMode,
       "isDnisBeforeAni": isDnisBeforeAni,
       "collectAni": collectAni,
       "prewinkLength": prewinkLength,
       "winkLength": winkLength,
       "minWinkDetection": minWinkDetection,
       "maxWinkDetection": maxWinkDetection,
       "maxDigitsDnis": maxDigitsDnis,
       "maxDigitsAni": maxDigitsAni,
       "minTimeToDetectTransition": minTimeToDetectTransition,
       "charBeforedigits": charBeforedigits,
       "charBetweenAniAndDnis": charBetweenAniAndDnis,
       "charInTheEndOfDigits": charInTheEndOfDigits,
       "sendCharBeforeDigits": sendCharBeforeDigits,
       "sendDnisbeforeAni": sendDnisbeforeAni,
       "sendCharBetweenAniAndDnis": sendCharBetweenAniAndDnis,
       "sendCharcharInTheEndOfDigits": sendCharcharInTheEndOfDigits,
       "fileToPlay": fileToPlay,
       "repeatPlayFile": repeatPlayFile,
       "gc": gc,
       "protocolConfigFileIn": protocolConfigFileIn,
       "protocolConfigFileOut": protocolConfigFileOut,
       "listOfProtocolConfigFilesIn": listOfProtocolConfigFilesIn,
       "listOfProtocolConfigFilesOut": listOfProtocolConfigFilesOut,
       "pri": pri,
       "protocolTrace": protocolTrace,
       "erbium": erbium,
       "iridium": iridium,
       "hostID": hostID,
       "sIUIPorID": sIUIPorID,
       "channelSelectionOrder": channelSelectionOrder,
       "glareMode": glareMode,
       "stat": stat,
       "timeUpTotal": timeUpTotal,
       "timeUpInterval": timeUpInterval,
       "timeSpanTotal": timeSpanTotal,
       "timeSpanInterval": timeSpanInterval,
       "vgkLoginAttemptTotal": vgkLoginAttemptTotal,
       "vgkLoginAttemptInterval": vgkLoginAttemptInterval,
       "vgkLoginSuccessTotal": vgkLoginSuccessTotal,
       "vgkLoginSuccessInterval": vgkLoginSuccessInterval,
       "vgkLoginFailureTotal": vgkLoginFailureTotal,
       "vgkLoginFailureInterval": vgkLoginFailureInterval,
       "vgkLogoutAttemptTotal": vgkLogoutAttemptTotal,
       "vgkLogoutAttemptInterval": vgkLogoutAttemptInterval,
       "vgkLogoutSuccessTotal": vgkLogoutSuccessTotal,
       "vgkLogoutSuccessInterval": vgkLogoutSuccessInterval,
       "vgkLogoutFailureTotal": vgkLogoutFailureTotal,
       "vgkLogoutFailureInterval": vgkLogoutFailureInterval,
       "vgkDisconnectionTotal": vgkDisconnectionTotal,
       "vgkDisconnectionInterval": vgkDisconnectionInterval,
       "callValue": callValue,
       "callInterval": callInterval,
       "callMaxTotal": callMaxTotal,
       "callMaxInterval": callMaxInterval,
       "callAverageTotal": callAverageTotal,
       "callAverageInterval": callAverageInterval,
       "callTotal": callTotal,
       "universalCallValue": universalCallValue,
       "universalCallInterval": universalCallInterval,
       "universalCallMaxTotal": universalCallMaxTotal,
       "universalCallMaxInterval": universalCallMaxInterval,
       "universalCallAverageTotal": universalCallAverageTotal,
       "universalCallAverageInterval": universalCallAverageInterval,
       "universalCallTotal": universalCallTotal,
       "voiceCallValue": voiceCallValue,
       "voiceCallInterval": voiceCallInterval,
       "voiceCallMaxTotal": voiceCallMaxTotal,
       "voiceCallMaxInterval": voiceCallMaxInterval,
       "voiceCallAverageTotal": voiceCallAverageTotal,
       "voiceCallAverageInterval": voiceCallAverageInterval,
       "voiceCallTotal": voiceCallTotal,
       "faxCallValue": faxCallValue,
       "faxCallInterval": faxCallInterval,
       "faxCallMaxTotal": faxCallMaxTotal,
       "faxCallMaxInterval": faxCallMaxInterval,
       "faxCallAverageTotal": faxCallAverageTotal,
       "faxCallAverageInterval": faxCallAverageInterval,
       "faxCallTotal": faxCallTotal,
       "sncCallValue": sncCallValue,
       "sncCallInterval": sncCallInterval,
       "sncCallMaxTotal": sncCallMaxTotal,
       "sncCallMaxInterval": sncCallMaxInterval,
       "sncCallAverageTotal": sncCallAverageTotal,
       "sncCallAverageInterval": sncCallAverageInterval,
       "sncCallTotal": sncCallTotal,
       "iPhoneCallValue": iPhoneCallValue,
       "iPhoneCallInterval": iPhoneCallInterval,
       "iPhoneCallMaxTotal": iPhoneCallMaxTotal,
       "iPhoneCallMaxInterval": iPhoneCallMaxInterval,
       "iPhoneCallAverageTotal": iPhoneCallAverageTotal,
       "iPhoneCallAverageInterval": iPhoneCallAverageInterval,
       "iPhoneCallTotal": iPhoneCallTotal,
       "dialerCallValue": dialerCallValue,
       "dialerCallInterval": dialerCallInterval,
       "dialerCallMaxTotal": dialerCallMaxTotal,
       "dialerCallMaxInterval": dialerCallMaxInterval,
       "dialerCallAverageTotal": dialerCallAverageTotal,
       "dialerCallAverageInterval": dialerCallAverageInterval,
       "dialerCallTotal": dialerCallTotal,
       "incorrectPasswordCallTotal": incorrectPasswordCallTotal,
       "incorrectPasswordCallInterval": incorrectPasswordCallInterval,
       "notSupportedCallTotal": notSupportedCallTotal,
       "notSupportedCallInterval": notSupportedCallInterval,
       "incomingInternetAttemptCallValue": incomingInternetAttemptCallValue,
       "incomingInternetAttemptCallInterval": incomingInternetAttemptCallInterval,
       "incomingInternetAttemptCallMaxTotal": incomingInternetAttemptCallMaxTotal,
       "incomingInternetAttemptCallMaxInterval": incomingInternetAttemptCallMaxInterval,
       "incomingInternetAttemptCallAverageTotal": incomingInternetAttemptCallAverageTotal,
       "incomingInternetAttemptCallAverageInterval": incomingInternetAttemptCallAverageInterval,
       "incomingInternetAttemptCallTotal": incomingInternetAttemptCallTotal,
       "incomingInternetSuccessCallValue": incomingInternetSuccessCallValue,
       "incomingInternetSuccessCallInterval": incomingInternetSuccessCallInterval,
       "incomingInternetSuccessCallMaxTotal": incomingInternetSuccessCallMaxTotal,
       "incomingInternetSuccessCallMaxInterval": incomingInternetSuccessCallMaxInterval,
       "incomingInternetSuccessCallAverageTotal": incomingInternetSuccessCallAverageTotal,
       "incomingInternetSuccessCallAverageInterval": incomingInternetSuccessCallAverageInterval,
       "incomingInternetSuccessCallTotal": incomingInternetSuccessCallTotal,
       "incomingTelephonyAttemptCallValue": incomingTelephonyAttemptCallValue,
       "incomingTelephonyAttemptCallInterval": incomingTelephonyAttemptCallInterval,
       "incomingTelephonyAttemptCallMaxTotal": incomingTelephonyAttemptCallMaxTotal,
       "incomingTelephonyAttemptCallMaxInterval": incomingTelephonyAttemptCallMaxInterval,
       "incomingTelephonyAttemptCallAverageTotal": incomingTelephonyAttemptCallAverageTotal,
       "incomingTelephonyAttemptCallAverageInterval": incomingTelephonyAttemptCallAverageInterval,
       "incomingTelephonyAttemptCallTotal": incomingTelephonyAttemptCallTotal,
       "incomingTelephonySuccessCallValue": incomingTelephonySuccessCallValue,
       "incomingTelephonySuccessCallInterval": incomingTelephonySuccessCallInterval,
       "incomingTelephonySuccessCallMaxTotal": incomingTelephonySuccessCallMaxTotal,
       "incomingTelephonySuccessCallMaxInterval": incomingTelephonySuccessCallMaxInterval,
       "incomingTelephonySuccessCallAverageTotal": incomingTelephonySuccessCallAverageTotal,
       "incomingTelephonySuccessCallAverageInterval": incomingTelephonySuccessCallAverageInterval,
       "incomingTelephonySuccessCallTotal": incomingTelephonySuccessCallTotal,
       "outgoingInternetCallValue": outgoingInternetCallValue,
       "outgoingInternetCallInterval": outgoingInternetCallInterval,
       "outgoingInternetCallMaxTotal": outgoingInternetCallMaxTotal,
       "outgoingInternetCallMaxInterval": outgoingInternetCallMaxInterval,
       "outgoingInternetCallAverageTotal": outgoingInternetCallAverageTotal,
       "outgoingInternetCallAverageInterval": outgoingInternetCallAverageInterval,
       "outgoingInternetCallTotal": outgoingInternetCallTotal,
       "outgoingTelephonyCallValue": outgoingTelephonyCallValue,
       "outgoingTelephonyCallInterval": outgoingTelephonyCallInterval,
       "outgoingTelephonyCallMaxTotal": outgoingTelephonyCallMaxTotal,
       "outgoingTelephonyCallMaxInterval": outgoingTelephonyCallMaxInterval,
       "outgoingTelephonyCallAverageTotal": outgoingTelephonyCallAverageTotal,
       "outgoingTelephonyCallAverageInterval": outgoingTelephonyCallAverageInterval,
       "outgoingTelephonyCallTotal": outgoingTelephonyCallTotal,
       "accountExpiredCallTotal": accountExpiredCallTotal,
       "accountExpiredCallInterval": accountExpiredCallInterval,
       "vgkNotAvailableCallTotal": vgkNotAvailableCallTotal,
       "vgkNotAvailableCallInterval": vgkNotAvailableCallInterval,
       "vtgShutDownCallTotal": vtgShutDownCallTotal,
       "vtgShutDownCallInterval": vtgShutDownCallInterval,
       "vtgOutOfHoursCallTotal": vtgOutOfHoursCallTotal,
       "vtgOutOfHoursCallInterval": vtgOutOfHoursCallInterval,
       "vtgBusyCallTotal": vtgBusyCallTotal,
       "vtgBusyCallInterval": vtgBusyCallInterval,
       "vtgNoAnswerCallTotal": vtgNoAnswerCallTotal,
       "vtgNoAnswerCallInterval": vtgNoAnswerCallInterval,
       "telephoneBusyCallTotal": telephoneBusyCallTotal,
       "telephoneBusyCallInterval": telephoneBusyCallInterval,
       "telephoneNoAnswerCallTotal": telephoneNoAnswerCallTotal,
       "telephoneNoAnswerCallInterval": telephoneNoAnswerCallInterval,
       "miscReasonDisconnectedCallTotal": miscReasonDisconnectedCallTotal,
       "miscReasonDisconnectedCallInterval": miscReasonDisconnectedCallInterval,
       "totalDisconnectedCallsTotal": totalDisconnectedCallsTotal,
       "totalDisconnectedCallsInterval": totalDisconnectedCallsInterval,
       "vtgOutOfServiceCallTotal": vtgOutOfServiceCallTotal,
       "vtgOutOfServiceCallInterval": vtgOutOfServiceCallInterval,
       "unauthorizedUserCallTotal": unauthorizedUserCallTotal,
       "unauthorizedUserCallInterval": unauthorizedUserCallInterval,
       "resolveFailureCallTotal": resolveFailureCallTotal,
       "resolveFailureCallInterval": resolveFailureCallInterval,
       "pstnFailureCallTotal": pstnFailureCallTotal,
       "pstnFailureCallInterval": pstnFailureCallInterval,
       "abnormalTerminationCallTotal": abnormalTerminationCallTotal,
       "abnormalTerminationCallInterval": abnormalTerminationCallInterval,
       "trapParameters": trapParameters,
       "telephonyErrorDescription": telephonyErrorDescription}
)
