# SNMP MIB module (ZHNVOICE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHNVOICE
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:04 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(zhoneWtn,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneWtn")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhnVoice = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40)
)
zhnVoice.setRevisions(
        ("2010-04-01 00:00",
         "2011-02-24 00:00",
         "2011-10-28 00:00",
         "2012-01-26 12:00",
         "2012-04-18 12:00",
         "2012-05-16 12:00",
         "2012-07-23 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VoiceProfileLineStateType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class DTMFMethodValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class HookFlashMethodValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class RegionValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class VoiceTransportValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class VoiceLineStatusValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class VoiceLineCallStateValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class VoiceProfileAddressModes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("domainName", 3),
          ("ip", 1),
          ("ipBracketed", 2))
    )



class VoiceProfileSwitchTypes(Integer32, TextualConvention):
    status = "current"
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("axtelCS2K", 9),
          ("broadSoft", 1),
          ("cirpack", 2),
          ("copperCom", 10),
          ("ericsson", 13),
          ("genband", 3),
          ("metaSwitch", 4),
          ("networkOnly", 6),
          ("nortel", 5),
          ("openSer", 11),
          ("softX3000", 8),
          ("taqua", 7),
          ("unknown", 99),
          ("utStarCom", 12))
    )



# MIB Managed Objects in the order of their OIDs

_ZhnVoiceNotifications_ObjectIdentity = ObjectIdentity
zhnVoiceNotifications = _ZhnVoiceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 0)
)
_ZhnVoiceServiceObjects_ObjectIdentity = ObjectIdentity
zhnVoiceServiceObjects = _ZhnVoiceServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1)
)
_VoiceServiceTable_Object = MibTable
voiceServiceTable = _VoiceServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 1)
)
if mibBuilder.loadTexts:
    voiceServiceTable.setStatus("current")
_VoiceServiceEntry_Object = MibTableRow
voiceServiceEntry = _VoiceServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 1, 1)
)
voiceServiceEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
)
if mibBuilder.loadTexts:
    voiceServiceEntry.setStatus("current")
_VoiceProfileNumberOfEntries_Type = Unsigned32
_VoiceProfileNumberOfEntries_Object = MibTableColumn
voiceProfileNumberOfEntries = _VoiceProfileNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 1, 1, 1),
    _VoiceProfileNumberOfEntries_Type()
)
voiceProfileNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileNumberOfEntries.setStatus("current")


class _VoiceBoundIfName_Type(OctetString):
    """Custom type voiceBoundIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_VoiceBoundIfName_Type.__name__ = "OctetString"
_VoiceBoundIfName_Object = MibTableColumn
voiceBoundIfName = _VoiceBoundIfName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 1, 1, 2),
    _VoiceBoundIfName_Type()
)
voiceBoundIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceBoundIfName.setStatus("current")
_VoiceBoundIpAddr_Type = IpAddress
_VoiceBoundIpAddr_Object = MibTableColumn
voiceBoundIpAddr = _VoiceBoundIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 1, 1, 3),
    _VoiceBoundIpAddr_Type()
)
voiceBoundIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceBoundIpAddr.setStatus("current")
_VoiceServiceIndex_Type = Unsigned32
_VoiceServiceIndex_Object = MibTableColumn
voiceServiceIndex = _VoiceServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 1, 1, 4),
    _VoiceServiceIndex_Type()
)
voiceServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceServiceIndex.setStatus("current")
_Capabilities_ObjectIdentity = ObjectIdentity
capabilities = _Capabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2)
)
_CapabilitiesTable_Object = MibTable
capabilitiesTable = _CapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1)
)
if mibBuilder.loadTexts:
    capabilitiesTable.setStatus("current")
_CapabilitiesEntry_Object = MibTableRow
capabilitiesEntry = _CapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1)
)
capabilitiesEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
)
if mibBuilder.loadTexts:
    capabilitiesEntry.setStatus("current")
_MaxProfileCount_Type = Unsigned32
_MaxProfileCount_Object = MibTableColumn
maxProfileCount = _MaxProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 1),
    _MaxProfileCount_Type()
)
maxProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxProfileCount.setStatus("current")
_MaxLineCount_Type = Unsigned32
_MaxLineCount_Object = MibTableColumn
maxLineCount = _MaxLineCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 2),
    _MaxLineCount_Type()
)
maxLineCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLineCount.setStatus("current")
_MaxSessionsPerLine_Type = Unsigned32
_MaxSessionsPerLine_Object = MibTableColumn
maxSessionsPerLine = _MaxSessionsPerLine_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 3),
    _MaxSessionsPerLine_Type()
)
maxSessionsPerLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSessionsPerLine.setStatus("current")
_MaxSessionCount_Type = Unsigned32
_MaxSessionCount_Object = MibTableColumn
maxSessionCount = _MaxSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 4),
    _MaxSessionCount_Type()
)
maxSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSessionCount.setStatus("current")


class _SignalingProtocols_Type(OctetString):
    """Custom type signalingProtocols based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SignalingProtocols_Type.__name__ = "OctetString"
_SignalingProtocols_Object = MibTableColumn
signalingProtocols = _SignalingProtocols_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 5),
    _SignalingProtocols_Type()
)
signalingProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingProtocols.setStatus("current")


class _Regions_Type(OctetString):
    """Custom type regions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Regions_Type.__name__ = "OctetString"
_Regions_Object = MibTableColumn
regions = _Regions_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 6),
    _Regions_Type()
)
regions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regions.setStatus("current")
_Rtcp_Type = TruthValue
_Rtcp_Object = MibTableColumn
rtcp = _Rtcp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 7),
    _Rtcp_Type()
)
rtcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtcp.setStatus("current")
_Srtp_Type = TruthValue
_Srtp_Object = MibTableColumn
srtp = _Srtp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 8),
    _Srtp_Type()
)
srtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtp.setStatus("current")
_RtpRedundancy_Type = TruthValue
_RtpRedundancy_Object = MibTableColumn
rtpRedundancy = _RtpRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 9),
    _RtpRedundancy_Type()
)
rtpRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpRedundancy.setStatus("current")
_DscpCoupled_Type = TruthValue
_DscpCoupled_Object = MibTableColumn
dscpCoupled = _DscpCoupled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 10),
    _DscpCoupled_Type()
)
dscpCoupled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dscpCoupled.setStatus("current")
_EthernetTaggingCoupled_Type = TruthValue
_EthernetTaggingCoupled_Object = MibTableColumn
ethernetTaggingCoupled = _EthernetTaggingCoupled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 11),
    _EthernetTaggingCoupled_Type()
)
ethernetTaggingCoupled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetTaggingCoupled.setStatus("current")
_PstnSoftSwitchOver_Type = TruthValue
_PstnSoftSwitchOver_Object = MibTableColumn
pstnSoftSwitchOver = _PstnSoftSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 12),
    _PstnSoftSwitchOver_Type()
)
pstnSoftSwitchOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pstnSoftSwitchOver.setStatus("current")
_FaxT38_Type = TruthValue
_FaxT38_Object = MibTableColumn
faxT38 = _FaxT38_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 13),
    _FaxT38_Type()
)
faxT38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxT38.setStatus("current")
_FaxPassThrough_Type = TruthValue
_FaxPassThrough_Object = MibTableColumn
faxPassThrough = _FaxPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 14),
    _FaxPassThrough_Type()
)
faxPassThrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxPassThrough.setStatus("current")
_ModemPassThrough_Type = TruthValue
_ModemPassThrough_Object = MibTableColumn
modemPassThrough = _ModemPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 15),
    _ModemPassThrough_Type()
)
modemPassThrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemPassThrough.setStatus("current")
_ToneGeneration_Type = TruthValue
_ToneGeneration_Object = MibTableColumn
toneGeneration = _ToneGeneration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 16),
    _ToneGeneration_Type()
)
toneGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    toneGeneration.setStatus("current")
_RingGeneration_Type = TruthValue
_RingGeneration_Object = MibTableColumn
ringGeneration = _RingGeneration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 17),
    _RingGeneration_Type()
)
ringGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringGeneration.setStatus("current")
_DigitMapCapabilities_Type = TruthValue
_DigitMapCapabilities_Object = MibTableColumn
digitMapCapabilities = _DigitMapCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 18),
    _DigitMapCapabilities_Type()
)
digitMapCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitMapCapabilities.setStatus("current")
_NumberingPlan_Type = TruthValue
_NumberingPlan_Object = MibTableColumn
numberingPlan = _NumberingPlan_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 19),
    _NumberingPlan_Type()
)
numberingPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberingPlan.setStatus("current")
_ButtonMap_Type = TruthValue
_ButtonMap_Object = MibTableColumn
buttonMap = _ButtonMap_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 20),
    _ButtonMap_Type()
)
buttonMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buttonMap.setStatus("current")
_VoicePortTests_Type = TruthValue
_VoicePortTests_Object = MibTableColumn
voicePortTests = _VoicePortTests_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 1, 1, 21),
    _VoicePortTests_Type()
)
voicePortTests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicePortTests.setStatus("current")
_CapabilitiesSIPTable_Object = MibTable
capabilitiesSIPTable = _CapabilitiesSIPTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 2)
)
if mibBuilder.loadTexts:
    capabilitiesSIPTable.setStatus("current")
_CapabilitiesSIPEntry_Object = MibTableRow
capabilitiesSIPEntry = _CapabilitiesSIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 2, 1)
)
capabilitiesSIPEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
)
if mibBuilder.loadTexts:
    capabilitiesSIPEntry.setStatus("current")


class _Role_Type(OctetString):
    """Custom type role based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_Role_Type.__name__ = "OctetString"
_Role_Object = MibTableColumn
role = _Role_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 2, 1, 1),
    _Role_Type()
)
role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    role.setStatus("current")


class _ExtensionsSIP_Type(OctetString):
    """Custom type extensionsSIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtensionsSIP_Type.__name__ = "OctetString"
_ExtensionsSIP_Object = MibTableColumn
extensionsSIP = _ExtensionsSIP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 2, 1, 2),
    _ExtensionsSIP_Type()
)
extensionsSIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extensionsSIP.setStatus("current")


class _Transports_Type(OctetString):
    """Custom type transports based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_Transports_Type.__name__ = "OctetString"
_Transports_Object = MibTableColumn
transports = _Transports_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 2, 1, 3),
    _Transports_Type()
)
transports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transports.setStatus("current")


class _UriSchemes_Type(OctetString):
    """Custom type uriSchemes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UriSchemes_Type.__name__ = "OctetString"
_UriSchemes_Object = MibTableColumn
uriSchemes = _UriSchemes_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 2, 1, 4),
    _UriSchemes_Type()
)
uriSchemes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uriSchemes.setStatus("current")
_EventSubscription_Type = TruthValue
_EventSubscription_Object = MibTableColumn
eventSubscription = _EventSubscription_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 2, 1, 5),
    _EventSubscription_Type()
)
eventSubscription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSubscription.setStatus("current")
_ResponseMap_Type = TruthValue
_ResponseMap_Object = MibTableColumn
responseMap = _ResponseMap_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 2, 1, 6),
    _ResponseMap_Type()
)
responseMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    responseMap.setStatus("current")


class _TlsKeyExchangeProtocols_Type(OctetString):
    """Custom type tlsKeyExchangeProtocols based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TlsKeyExchangeProtocols_Type.__name__ = "OctetString"
_TlsKeyExchangeProtocols_Object = MibTableColumn
tlsKeyExchangeProtocols = _TlsKeyExchangeProtocols_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 2, 1, 7),
    _TlsKeyExchangeProtocols_Type()
)
tlsKeyExchangeProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsKeyExchangeProtocols.setStatus("current")
_CapabilitiesMGCPTable_Object = MibTable
capabilitiesMGCPTable = _CapabilitiesMGCPTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 3)
)
if mibBuilder.loadTexts:
    capabilitiesMGCPTable.setStatus("current")
_CapabilitiesMGCPEntry_Object = MibTableRow
capabilitiesMGCPEntry = _CapabilitiesMGCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 3, 1)
)
capabilitiesMGCPEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
)
if mibBuilder.loadTexts:
    capabilitiesMGCPEntry.setStatus("current")


class _ExtensionsMGCP_Type(OctetString):
    """Custom type extensionsMGCP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtensionsMGCP_Type.__name__ = "OctetString"
_ExtensionsMGCP_Object = MibTableColumn
extensionsMGCP = _ExtensionsMGCP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 3, 1, 1),
    _ExtensionsMGCP_Type()
)
extensionsMGCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extensionsMGCP.setStatus("current")
_CapabilitiesCodecsTable_Object = MibTable
capabilitiesCodecsTable = _CapabilitiesCodecsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 4)
)
if mibBuilder.loadTexts:
    capabilitiesCodecsTable.setStatus("current")
_CapabilitiesCodecsEntry_Object = MibTableRow
capabilitiesCodecsEntry = _CapabilitiesCodecsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 4, 1)
)
capabilitiesCodecsEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
    (0, "ZHNVOICE", "codecIndex"),
)
if mibBuilder.loadTexts:
    capabilitiesCodecsEntry.setStatus("current")
_CodecIndex_Type = Unsigned32
_CodecIndex_Object = MibTableColumn
codecIndex = _CodecIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 4, 1, 1),
    _CodecIndex_Type()
)
codecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codecIndex.setStatus("current")
_EntryID_Type = Unsigned32
_EntryID_Object = MibTableColumn
entryID = _EntryID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 4, 1, 2),
    _EntryID_Type()
)
entryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entryID.setStatus("current")


class _Codec_Type(OctetString):
    """Custom type codec based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Codec_Type.__name__ = "OctetString"
_Codec_Object = MibTableColumn
codec = _Codec_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 4, 1, 3),
    _Codec_Type()
)
codec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codec.setStatus("current")
_BitRate_Type = Unsigned32
_BitRate_Object = MibTableColumn
bitRate = _BitRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 4, 1, 4),
    _BitRate_Type()
)
bitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitRate.setStatus("current")


class _PacketizationPeriod_Type(OctetString):
    """Custom type packetizationPeriod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PacketizationPeriod_Type.__name__ = "OctetString"
_PacketizationPeriod_Object = MibTableColumn
packetizationPeriod = _PacketizationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 4, 1, 5),
    _PacketizationPeriod_Type()
)
packetizationPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetizationPeriod.setStatus("current")
_SilenceSuppression_Type = TruthValue
_SilenceSuppression_Object = MibTableColumn
silenceSuppression = _SilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 2, 4, 1, 6),
    _SilenceSuppression_Type()
)
silenceSuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    silenceSuppression.setStatus("current")
_VoiceProfiles_ObjectIdentity = ObjectIdentity
voiceProfiles = _VoiceProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3)
)
_VoiceProfileTable_Object = MibTable
voiceProfileTable = _VoiceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1)
)
if mibBuilder.loadTexts:
    voiceProfileTable.setStatus("current")
_VoiceProfileEntry_Object = MibTableRow
voiceProfileEntry = _VoiceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1)
)
voiceProfileEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
    (0, "ZHNVOICE", "voiceProfileIndex"),
)
if mibBuilder.loadTexts:
    voiceProfileEntry.setStatus("current")


class _VoiceProfileIndex_Type(Unsigned32):
    """Custom type voiceProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_VoiceProfileIndex_Type.__name__ = "Unsigned32"
_VoiceProfileIndex_Object = MibTableColumn
voiceProfileIndex = _VoiceProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 1),
    _VoiceProfileIndex_Type()
)
voiceProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileIndex.setStatus("current")
_VoiceProfileEnable_Type = VoiceProfileLineStateType
_VoiceProfileEnable_Object = MibTableColumn
voiceProfileEnable = _VoiceProfileEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 2),
    _VoiceProfileEnable_Type()
)
voiceProfileEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileEnable.setStatus("current")
_VoiceProfileReset_Type = TruthValue
_VoiceProfileReset_Object = MibTableColumn
voiceProfileReset = _VoiceProfileReset_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 3),
    _VoiceProfileReset_Type()
)
voiceProfileReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileReset.setStatus("current")
_VoiceProfileNumberOfLines_Type = Unsigned32
_VoiceProfileNumberOfLines_Object = MibTableColumn
voiceProfileNumberOfLines = _VoiceProfileNumberOfLines_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 4),
    _VoiceProfileNumberOfLines_Type()
)
voiceProfileNumberOfLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileNumberOfLines.setStatus("current")


class _VoiceProfileName_Type(OctetString):
    """Custom type voiceProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_VoiceProfileName_Type.__name__ = "OctetString"
_VoiceProfileName_Object = MibTableColumn
voiceProfileName = _VoiceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 5),
    _VoiceProfileName_Type()
)
voiceProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileName.setStatus("current")


class _VoiceProfileSignalingProtocol_Type(OctetString):
    """Custom type voiceProfileSignalingProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoiceProfileSignalingProtocol_Type.__name__ = "OctetString"
_VoiceProfileSignalingProtocol_Object = MibTableColumn
voiceProfileSignalingProtocol = _VoiceProfileSignalingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 6),
    _VoiceProfileSignalingProtocol_Type()
)
voiceProfileSignalingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSignalingProtocol.setStatus("current")
_VoiceProfileMaxSessions_Type = Unsigned32
_VoiceProfileMaxSessions_Object = MibTableColumn
voiceProfileMaxSessions = _VoiceProfileMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 7),
    _VoiceProfileMaxSessions_Type()
)
voiceProfileMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileMaxSessions.setStatus("current")
_VoiceProfileDtmfMethod_Type = DTMFMethodValues
_VoiceProfileDtmfMethod_Object = MibTableColumn
voiceProfileDtmfMethod = _VoiceProfileDtmfMethod_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 8),
    _VoiceProfileDtmfMethod_Type()
)
voiceProfileDtmfMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileDtmfMethod.setStatus("current")
_VoiceProfileDtmfMethodG711_Type = DTMFMethodValues
_VoiceProfileDtmfMethodG711_Object = MibTableColumn
voiceProfileDtmfMethodG711 = _VoiceProfileDtmfMethodG711_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 9),
    _VoiceProfileDtmfMethodG711_Type()
)
voiceProfileDtmfMethodG711.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileDtmfMethodG711.setStatus("current")
_VoiceProfileHookFlashMethod_Type = HookFlashMethodValues
_VoiceProfileHookFlashMethod_Object = MibTableColumn
voiceProfileHookFlashMethod = _VoiceProfileHookFlashMethod_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 10),
    _VoiceProfileHookFlashMethod_Type()
)
voiceProfileHookFlashMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileHookFlashMethod.setStatus("current")
_VoiceProfileRegion_Type = RegionValues
_VoiceProfileRegion_Object = MibTableColumn
voiceProfileRegion = _VoiceProfileRegion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 11),
    _VoiceProfileRegion_Type()
)
voiceProfileRegion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileRegion.setStatus("current")


class _VoiceProfileDigitMap_Type(OctetString):
    """Custom type voiceProfileDigitMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceProfileDigitMap_Type.__name__ = "OctetString"
_VoiceProfileDigitMap_Object = MibTableColumn
voiceProfileDigitMap = _VoiceProfileDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 12),
    _VoiceProfileDigitMap_Type()
)
voiceProfileDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileDigitMap.setStatus("current")
_VoiceProfileDigitMapEnable_Type = TruthValue
_VoiceProfileDigitMapEnable_Object = MibTableColumn
voiceProfileDigitMapEnable = _VoiceProfileDigitMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 13),
    _VoiceProfileDigitMapEnable_Type()
)
voiceProfileDigitMapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileDigitMapEnable.setStatus("current")
_VoiceProfileStunEnable_Type = TruthValue
_VoiceProfileStunEnable_Object = MibTableColumn
voiceProfileStunEnable = _VoiceProfileStunEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 14),
    _VoiceProfileStunEnable_Type()
)
voiceProfileStunEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileStunEnable.setStatus("current")


class _VoiceProfileStunServer_Type(OctetString):
    """Custom type voiceProfileStunServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceProfileStunServer_Type.__name__ = "OctetString"
_VoiceProfileStunServer_Object = MibTableColumn
voiceProfileStunServer = _VoiceProfileStunServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 15),
    _VoiceProfileStunServer_Type()
)
voiceProfileStunServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileStunServer.setStatus("current")
_VoiceProfileStunServerPort_Type = Unsigned32
_VoiceProfileStunServerPort_Object = MibTableColumn
voiceProfileStunServerPort = _VoiceProfileStunServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 16),
    _VoiceProfileStunServerPort_Type()
)
voiceProfileStunServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileStunServerPort.setStatus("current")


class _VoiceProfileLogServer_Type(OctetString):
    """Custom type voiceProfileLogServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_VoiceProfileLogServer_Type.__name__ = "OctetString"
_VoiceProfileLogServer_Object = MibTableColumn
voiceProfileLogServer = _VoiceProfileLogServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 17),
    _VoiceProfileLogServer_Type()
)
voiceProfileLogServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLogServer.setStatus("current")
_VoiceProfileLogServerPort_Type = Unsigned32
_VoiceProfileLogServerPort_Object = MibTableColumn
voiceProfileLogServerPort = _VoiceProfileLogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 18),
    _VoiceProfileLogServerPort_Type()
)
voiceProfileLogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLogServerPort.setStatus("current")
_VoiceProfileSpNum_Type = Unsigned32
_VoiceProfileSpNum_Object = MibTableColumn
voiceProfileSpNum = _VoiceProfileSpNum_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 19),
    _VoiceProfileSpNum_Type()
)
voiceProfileSpNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSpNum.setStatus("current")
_VoiceProfileV18Support_Type = TruthValue
_VoiceProfileV18Support_Object = MibTableColumn
voiceProfileV18Support = _VoiceProfileV18Support_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 20),
    _VoiceProfileV18Support_Type()
)
voiceProfileV18Support.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileV18Support.setStatus("current")
_VoiceProfileSwitchType_Type = VoiceProfileSwitchTypes
_VoiceProfileSwitchType_Object = MibTableColumn
voiceProfileSwitchType = _VoiceProfileSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 1, 1, 21),
    _VoiceProfileSwitchType_Type()
)
voiceProfileSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSwitchType.setStatus("current")
_VoiceProfileServiceProviderTable_Object = MibTable
voiceProfileServiceProviderTable = _VoiceProfileServiceProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 2)
)
if mibBuilder.loadTexts:
    voiceProfileServiceProviderTable.setStatus("current")
_VoiceProfileServiceProviderEntry_Object = MibTableRow
voiceProfileServiceProviderEntry = _VoiceProfileServiceProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 2, 1)
)
voiceProfileServiceProviderEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
    (0, "ZHNVOICE", "voiceProfileIndex"),
)
if mibBuilder.loadTexts:
    voiceProfileServiceProviderEntry.setStatus("current")


class _VoiceProfileServiceProviderName_Type(OctetString):
    """Custom type voiceProfileServiceProviderName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceProfileServiceProviderName_Type.__name__ = "OctetString"
_VoiceProfileServiceProviderName_Object = MibTableColumn
voiceProfileServiceProviderName = _VoiceProfileServiceProviderName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 2, 1, 1),
    _VoiceProfileServiceProviderName_Type()
)
voiceProfileServiceProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileServiceProviderName.setStatus("current")
_VoiceProfileSIPTable_Object = MibTable
voiceProfileSIPTable = _VoiceProfileSIPTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3)
)
if mibBuilder.loadTexts:
    voiceProfileSIPTable.setStatus("current")
_VoiceProfileSIPEntry_Object = MibTableRow
voiceProfileSIPEntry = _VoiceProfileSIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1)
)
voiceProfileSIPEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
    (0, "ZHNVOICE", "voiceProfileIndex"),
)
if mibBuilder.loadTexts:
    voiceProfileSIPEntry.setStatus("current")


class _VoiceProfileSIPProxyServer_Type(OctetString):
    """Custom type voiceProfileSIPProxyServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceProfileSIPProxyServer_Type.__name__ = "OctetString"
_VoiceProfileSIPProxyServer_Object = MibTableColumn
voiceProfileSIPProxyServer = _VoiceProfileSIPProxyServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 1),
    _VoiceProfileSIPProxyServer_Type()
)
voiceProfileSIPProxyServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPProxyServer.setStatus("current")
_VoiceProfileSIPProxyServerPort_Type = Unsigned32
_VoiceProfileSIPProxyServerPort_Object = MibTableColumn
voiceProfileSIPProxyServerPort = _VoiceProfileSIPProxyServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 2),
    _VoiceProfileSIPProxyServerPort_Type()
)
voiceProfileSIPProxyServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPProxyServerPort.setStatus("current")
_VoiceProfileSIPProxyServerTransport_Type = VoiceTransportValues
_VoiceProfileSIPProxyServerTransport_Object = MibTableColumn
voiceProfileSIPProxyServerTransport = _VoiceProfileSIPProxyServerTransport_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 3),
    _VoiceProfileSIPProxyServerTransport_Type()
)
voiceProfileSIPProxyServerTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPProxyServerTransport.setStatus("current")


class _VoiceProfileSIPRegistrarServer_Type(OctetString):
    """Custom type voiceProfileSIPRegistrarServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceProfileSIPRegistrarServer_Type.__name__ = "OctetString"
_VoiceProfileSIPRegistrarServer_Object = MibTableColumn
voiceProfileSIPRegistrarServer = _VoiceProfileSIPRegistrarServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 4),
    _VoiceProfileSIPRegistrarServer_Type()
)
voiceProfileSIPRegistrarServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPRegistrarServer.setStatus("current")
_VoiceProfileSIPRegistrarServerPort_Type = Unsigned32
_VoiceProfileSIPRegistrarServerPort_Object = MibTableColumn
voiceProfileSIPRegistrarServerPort = _VoiceProfileSIPRegistrarServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 5),
    _VoiceProfileSIPRegistrarServerPort_Type()
)
voiceProfileSIPRegistrarServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPRegistrarServerPort.setStatus("current")
_VoiceProfileSIPRegistrarServerTransport_Type = VoiceTransportValues
_VoiceProfileSIPRegistrarServerTransport_Object = MibTableColumn
voiceProfileSIPRegistrarServerTransport = _VoiceProfileSIPRegistrarServerTransport_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 6),
    _VoiceProfileSIPRegistrarServerTransport_Type()
)
voiceProfileSIPRegistrarServerTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPRegistrarServerTransport.setStatus("current")
_VoiceProfileSIPToTagMatching_Type = TruthValue
_VoiceProfileSIPToTagMatching_Object = MibTableColumn
voiceProfileSIPToTagMatching = _VoiceProfileSIPToTagMatching_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 7),
    _VoiceProfileSIPToTagMatching_Type()
)
voiceProfileSIPToTagMatching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPToTagMatching.setStatus("current")


class _VoiceProfileSIPMusicServer_Type(OctetString):
    """Custom type voiceProfileSIPMusicServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceProfileSIPMusicServer_Type.__name__ = "OctetString"
_VoiceProfileSIPMusicServer_Object = MibTableColumn
voiceProfileSIPMusicServer = _VoiceProfileSIPMusicServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 8),
    _VoiceProfileSIPMusicServer_Type()
)
voiceProfileSIPMusicServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPMusicServer.setStatus("current")
_VoiceProfileSIPMusicServerPort_Type = Unsigned32
_VoiceProfileSIPMusicServerPort_Object = MibTableColumn
voiceProfileSIPMusicServerPort = _VoiceProfileSIPMusicServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 9),
    _VoiceProfileSIPMusicServerPort_Type()
)
voiceProfileSIPMusicServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPMusicServerPort.setStatus("current")


class _VoiceProfileSIPPlarGateway_Type(OctetString):
    """Custom type voiceProfileSIPPlarGateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_VoiceProfileSIPPlarGateway_Type.__name__ = "OctetString"
_VoiceProfileSIPPlarGateway_Object = MibTableColumn
voiceProfileSIPPlarGateway = _VoiceProfileSIPPlarGateway_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 10),
    _VoiceProfileSIPPlarGateway_Type()
)
voiceProfileSIPPlarGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPPlarGateway.setStatus("current")
_VoiceProfileSIPPlarPort_Type = Unsigned32
_VoiceProfileSIPPlarPort_Object = MibTableColumn
voiceProfileSIPPlarPort = _VoiceProfileSIPPlarPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 11),
    _VoiceProfileSIPPlarPort_Type()
)
voiceProfileSIPPlarPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPPlarPort.setStatus("current")


class _VoiceProfileSIPUserAgentDomain_Type(OctetString):
    """Custom type voiceProfileSIPUserAgentDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceProfileSIPUserAgentDomain_Type.__name__ = "OctetString"
_VoiceProfileSIPUserAgentDomain_Object = MibTableColumn
voiceProfileSIPUserAgentDomain = _VoiceProfileSIPUserAgentDomain_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 12),
    _VoiceProfileSIPUserAgentDomain_Type()
)
voiceProfileSIPUserAgentDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPUserAgentDomain.setStatus("current")
_VoiceProfileSIPUserAgentPort_Type = Unsigned32
_VoiceProfileSIPUserAgentPort_Object = MibTableColumn
voiceProfileSIPUserAgentPort = _VoiceProfileSIPUserAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 13),
    _VoiceProfileSIPUserAgentPort_Type()
)
voiceProfileSIPUserAgentPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPUserAgentPort.setStatus("current")
_VoiceProfileSIPUserAgentTransport_Type = VoiceTransportValues
_VoiceProfileSIPUserAgentTransport_Object = MibTableColumn
voiceProfileSIPUserAgentTransport = _VoiceProfileSIPUserAgentTransport_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 14),
    _VoiceProfileSIPUserAgentTransport_Type()
)
voiceProfileSIPUserAgentTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPUserAgentTransport.setStatus("current")


class _VoiceProfileSIPOutboundProxy_Type(OctetString):
    """Custom type voiceProfileSIPOutboundProxy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceProfileSIPOutboundProxy_Type.__name__ = "OctetString"
_VoiceProfileSIPOutboundProxy_Object = MibTableColumn
voiceProfileSIPOutboundProxy = _VoiceProfileSIPOutboundProxy_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 15),
    _VoiceProfileSIPOutboundProxy_Type()
)
voiceProfileSIPOutboundProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPOutboundProxy.setStatus("current")
_VoiceProfileSIPOutboundProxyPort_Type = Unsigned32
_VoiceProfileSIPOutboundProxyPort_Object = MibTableColumn
voiceProfileSIPOutboundProxyPort = _VoiceProfileSIPOutboundProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 16),
    _VoiceProfileSIPOutboundProxyPort_Type()
)
voiceProfileSIPOutboundProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPOutboundProxyPort.setStatus("current")


class _VoiceProfileSIPOrganization_Type(OctetString):
    """Custom type voiceProfileSIPOrganization based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceProfileSIPOrganization_Type.__name__ = "OctetString"
_VoiceProfileSIPOrganization_Object = MibTableColumn
voiceProfileSIPOrganization = _VoiceProfileSIPOrganization_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 17),
    _VoiceProfileSIPOrganization_Type()
)
voiceProfileSIPOrganization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPOrganization.setStatus("current")
_VoiceProfileSIPRegistrationPeriod_Type = Unsigned32
_VoiceProfileSIPRegistrationPeriod_Object = MibTableColumn
voiceProfileSIPRegistrationPeriod = _VoiceProfileSIPRegistrationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 18),
    _VoiceProfileSIPRegistrationPeriod_Type()
)
voiceProfileSIPRegistrationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPRegistrationPeriod.setStatus("current")
_VoiceProfileSIPRegisterExpires_Type = Unsigned32
_VoiceProfileSIPRegisterExpires_Object = MibTableColumn
voiceProfileSIPRegisterExpires = _VoiceProfileSIPRegisterExpires_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 19),
    _VoiceProfileSIPRegisterExpires_Type()
)
voiceProfileSIPRegisterExpires.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPRegisterExpires.setStatus("current")
_VoiceProfileSIPRegisterRetryInterval_Type = Unsigned32
_VoiceProfileSIPRegisterRetryInterval_Object = MibTableColumn
voiceProfileSIPRegisterRetryInterval = _VoiceProfileSIPRegisterRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 20),
    _VoiceProfileSIPRegisterRetryInterval_Type()
)
voiceProfileSIPRegisterRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPRegisterRetryInterval.setStatus("current")
_VoiceProfileSIPDSCPMark_Type = Unsigned32
_VoiceProfileSIPDSCPMark_Object = MibTableColumn
voiceProfileSIPDSCPMark = _VoiceProfileSIPDSCPMark_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 21),
    _VoiceProfileSIPDSCPMark_Type()
)
voiceProfileSIPDSCPMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPDSCPMark.setStatus("current")
_VoiceProfileSIPVLANIDMark_Type = Integer32
_VoiceProfileSIPVLANIDMark_Object = MibTableColumn
voiceProfileSIPVLANIDMark = _VoiceProfileSIPVLANIDMark_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 22),
    _VoiceProfileSIPVLANIDMark_Type()
)
voiceProfileSIPVLANIDMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPVLANIDMark.setStatus("current")
_VoiceProfileSIPEthernetPriorityMark_Type = Integer32
_VoiceProfileSIPEthernetPriorityMark_Object = MibTableColumn
voiceProfileSIPEthernetPriorityMark = _VoiceProfileSIPEthernetPriorityMark_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 23),
    _VoiceProfileSIPEthernetPriorityMark_Type()
)
voiceProfileSIPEthernetPriorityMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPEthernetPriorityMark.setStatus("current")


class _VoiceProfileSIPInterdigitTimeout_Type(Unsigned32):
    """Custom type voiceProfileSIPInterdigitTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_VoiceProfileSIPInterdigitTimeout_Type.__name__ = "Unsigned32"
_VoiceProfileSIPInterdigitTimeout_Object = MibTableColumn
voiceProfileSIPInterdigitTimeout = _VoiceProfileSIPInterdigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 24),
    _VoiceProfileSIPInterdigitTimeout_Type()
)
voiceProfileSIPInterdigitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPInterdigitTimeout.setStatus("current")
_VoiceProfileSIPAddressMode_Type = VoiceProfileAddressModes
_VoiceProfileSIPAddressMode_Object = MibTableColumn
voiceProfileSIPAddressMode = _VoiceProfileSIPAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 3, 1, 25),
    _VoiceProfileSIPAddressMode_Type()
)
voiceProfileSIPAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPAddressMode.setStatus("current")
_VoiceProfileSIPEventSubscribeTable_Object = MibTable
voiceProfileSIPEventSubscribeTable = _VoiceProfileSIPEventSubscribeTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 4)
)
if mibBuilder.loadTexts:
    voiceProfileSIPEventSubscribeTable.setStatus("current")
_VoiceProfileSIPEventSubscribeEntry_Object = MibTableRow
voiceProfileSIPEventSubscribeEntry = _VoiceProfileSIPEventSubscribeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 4, 1)
)
voiceProfileSIPEventSubscribeEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
    (0, "ZHNVOICE", "voiceProfileIndex"),
)
if mibBuilder.loadTexts:
    voiceProfileSIPEventSubscribeEntry.setStatus("current")


class _VoiceProfileSIPEventSubscribeEvent_Type(OctetString):
    """Custom type voiceProfileSIPEventSubscribeEvent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoiceProfileSIPEventSubscribeEvent_Type.__name__ = "OctetString"
_VoiceProfileSIPEventSubscribeEvent_Object = MibTableColumn
voiceProfileSIPEventSubscribeEvent = _VoiceProfileSIPEventSubscribeEvent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 4, 1, 1),
    _VoiceProfileSIPEventSubscribeEvent_Type()
)
voiceProfileSIPEventSubscribeEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPEventSubscribeEvent.setStatus("current")


class _VoiceProfileSIPEventSubscribeNotifier_Type(OctetString):
    """Custom type voiceProfileSIPEventSubscribeNotifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceProfileSIPEventSubscribeNotifier_Type.__name__ = "OctetString"
_VoiceProfileSIPEventSubscribeNotifier_Object = MibTableColumn
voiceProfileSIPEventSubscribeNotifier = _VoiceProfileSIPEventSubscribeNotifier_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 4, 1, 2),
    _VoiceProfileSIPEventSubscribeNotifier_Type()
)
voiceProfileSIPEventSubscribeNotifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPEventSubscribeNotifier.setStatus("current")
_VoiceProfileSIPEventSubscribeNotifierPort_Type = Unsigned32
_VoiceProfileSIPEventSubscribeNotifierPort_Object = MibTableColumn
voiceProfileSIPEventSubscribeNotifierPort = _VoiceProfileSIPEventSubscribeNotifierPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 4, 1, 3),
    _VoiceProfileSIPEventSubscribeNotifierPort_Type()
)
voiceProfileSIPEventSubscribeNotifierPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPEventSubscribeNotifierPort.setStatus("current")
_VoiceProfileSIPEventSubscribeNotifierTransport_Type = VoiceTransportValues
_VoiceProfileSIPEventSubscribeNotifierTransport_Object = MibTableColumn
voiceProfileSIPEventSubscribeNotifierTransport = _VoiceProfileSIPEventSubscribeNotifierTransport_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 4, 1, 4),
    _VoiceProfileSIPEventSubscribeNotifierTransport_Type()
)
voiceProfileSIPEventSubscribeNotifierTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileSIPEventSubscribeNotifierTransport.setStatus("current")
_VoiceProfileMGCPTable_Object = MibTable
voiceProfileMGCPTable = _VoiceProfileMGCPTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 5)
)
if mibBuilder.loadTexts:
    voiceProfileMGCPTable.setStatus("current")
_VoiceProfileMGCPEntry_Object = MibTableRow
voiceProfileMGCPEntry = _VoiceProfileMGCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 5, 1)
)
voiceProfileMGCPEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
    (0, "ZHNVOICE", "voiceProfileIndex"),
)
if mibBuilder.loadTexts:
    voiceProfileMGCPEntry.setStatus("current")


class _VoiceProfileMGCPCallAgent1_Type(OctetString):
    """Custom type voiceProfileMGCPCallAgent1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceProfileMGCPCallAgent1_Type.__name__ = "OctetString"
_VoiceProfileMGCPCallAgent1_Object = MibTableColumn
voiceProfileMGCPCallAgent1 = _VoiceProfileMGCPCallAgent1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 5, 1, 1),
    _VoiceProfileMGCPCallAgent1_Type()
)
voiceProfileMGCPCallAgent1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileMGCPCallAgent1.setStatus("current")


class _VoiceProfileMGCPUser_Type(OctetString):
    """Custom type voiceProfileMGCPUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_VoiceProfileMGCPUser_Type.__name__ = "OctetString"
_VoiceProfileMGCPUser_Object = MibTableColumn
voiceProfileMGCPUser = _VoiceProfileMGCPUser_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 5, 1, 2),
    _VoiceProfileMGCPUser_Type()
)
voiceProfileMGCPUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileMGCPUser.setStatus("current")
_VoiceProfilePersistentNotify_Type = TruthValue
_VoiceProfilePersistentNotify_Object = MibTableColumn
voiceProfilePersistentNotify = _VoiceProfilePersistentNotify_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 5, 1, 3),
    _VoiceProfilePersistentNotify_Type()
)
voiceProfilePersistentNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfilePersistentNotify.setStatus("current")
_VoiceProfileMGCPAddressMode_Type = VoiceProfileAddressModes
_VoiceProfileMGCPAddressMode_Object = MibTableColumn
voiceProfileMGCPAddressMode = _VoiceProfileMGCPAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 5, 1, 4),
    _VoiceProfileMGCPAddressMode_Type()
)
voiceProfileMGCPAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileMGCPAddressMode.setStatus("current")
_VoiceProfileRTPTable_Object = MibTable
voiceProfileRTPTable = _VoiceProfileRTPTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 6)
)
if mibBuilder.loadTexts:
    voiceProfileRTPTable.setStatus("current")
_VoiceProfileRTPEntry_Object = MibTableRow
voiceProfileRTPEntry = _VoiceProfileRTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 6, 1)
)
voiceProfileRTPEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
    (0, "ZHNVOICE", "voiceProfileIndex"),
)
if mibBuilder.loadTexts:
    voiceProfileRTPEntry.setStatus("current")


class _VoiceProfileRTPLocalPortMin_Type(Unsigned32):
    """Custom type voiceProfileRTPLocalPortMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65525),
    )


_VoiceProfileRTPLocalPortMin_Type.__name__ = "Unsigned32"
_VoiceProfileRTPLocalPortMin_Object = MibTableColumn
voiceProfileRTPLocalPortMin = _VoiceProfileRTPLocalPortMin_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 6, 1, 1),
    _VoiceProfileRTPLocalPortMin_Type()
)
voiceProfileRTPLocalPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileRTPLocalPortMin.setStatus("current")


class _VoiceProfileRTPLocalPortMax_Type(Unsigned32):
    """Custom type voiceProfileRTPLocalPortMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65525),
    )


_VoiceProfileRTPLocalPortMax_Type.__name__ = "Unsigned32"
_VoiceProfileRTPLocalPortMax_Object = MibTableColumn
voiceProfileRTPLocalPortMax = _VoiceProfileRTPLocalPortMax_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 6, 1, 2),
    _VoiceProfileRTPLocalPortMax_Type()
)
voiceProfileRTPLocalPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileRTPLocalPortMax.setStatus("current")


class _VoiceProfileRTPDSCPMark_Type(Unsigned32):
    """Custom type voiceProfileRTPDSCPMark based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_VoiceProfileRTPDSCPMark_Type.__name__ = "Unsigned32"
_VoiceProfileRTPDSCPMark_Object = MibTableColumn
voiceProfileRTPDSCPMark = _VoiceProfileRTPDSCPMark_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 6, 1, 3),
    _VoiceProfileRTPDSCPMark_Type()
)
voiceProfileRTPDSCPMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileRTPDSCPMark.setStatus("current")


class _VoiceProfileRTPTelephoneEventPayloadType_Type(Unsigned32):
    """Custom type voiceProfileRTPTelephoneEventPayloadType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_VoiceProfileRTPTelephoneEventPayloadType_Type.__name__ = "Unsigned32"
_VoiceProfileRTPTelephoneEventPayloadType_Object = MibTableColumn
voiceProfileRTPTelephoneEventPayloadType = _VoiceProfileRTPTelephoneEventPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 6, 1, 4),
    _VoiceProfileRTPTelephoneEventPayloadType_Type()
)
voiceProfileRTPTelephoneEventPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileRTPTelephoneEventPayloadType.setStatus("current")
_VoiceProfileFaxT38Table_Object = MibTable
voiceProfileFaxT38Table = _VoiceProfileFaxT38Table_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 7)
)
if mibBuilder.loadTexts:
    voiceProfileFaxT38Table.setStatus("current")
_VoiceProfileFaxT38Entry_Object = MibTableRow
voiceProfileFaxT38Entry = _VoiceProfileFaxT38Entry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 7, 1)
)
voiceProfileFaxT38Entry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
    (0, "ZHNVOICE", "voiceProfileIndex"),
)
if mibBuilder.loadTexts:
    voiceProfileFaxT38Entry.setStatus("current")
_VoiceProfileFaxT38Enable_Type = TruthValue
_VoiceProfileFaxT38Enable_Object = MibTableColumn
voiceProfileFaxT38Enable = _VoiceProfileFaxT38Enable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 7, 1, 1),
    _VoiceProfileFaxT38Enable_Type()
)
voiceProfileFaxT38Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileFaxT38Enable.setStatus("current")
_VoiceProfileFaxT38BitRate_Type = Unsigned32
_VoiceProfileFaxT38BitRate_Object = MibTableColumn
voiceProfileFaxT38BitRate = _VoiceProfileFaxT38BitRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 7, 1, 2),
    _VoiceProfileFaxT38BitRate_Type()
)
voiceProfileFaxT38BitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileFaxT38BitRate.setStatus("current")
_VoiceProfileFaxT38HighSpeedPacketRate_Type = Unsigned32
_VoiceProfileFaxT38HighSpeedPacketRate_Object = MibTableColumn
voiceProfileFaxT38HighSpeedPacketRate = _VoiceProfileFaxT38HighSpeedPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 7, 1, 3),
    _VoiceProfileFaxT38HighSpeedPacketRate_Type()
)
voiceProfileFaxT38HighSpeedPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileFaxT38HighSpeedPacketRate.setStatus("current")
_VoiceProfileLines_ObjectIdentity = ObjectIdentity
voiceProfileLines = _VoiceProfileLines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8)
)
_VoiceProfileLineTable_Object = MibTable
voiceProfileLineTable = _VoiceProfileLineTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 1)
)
if mibBuilder.loadTexts:
    voiceProfileLineTable.setStatus("current")
_VoiceProfileLineEntry_Object = MibTableRow
voiceProfileLineEntry = _VoiceProfileLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 1, 1)
)
voiceProfileLineEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
    (0, "ZHNVOICE", "voiceProfileIndex"),
    (0, "ZHNVOICE", "voiceProfileLineIndex"),
)
if mibBuilder.loadTexts:
    voiceProfileLineEntry.setStatus("current")
_VoiceProfileLineIndex_Type = Unsigned32
_VoiceProfileLineIndex_Object = MibTableColumn
voiceProfileLineIndex = _VoiceProfileLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 1, 1, 1),
    _VoiceProfileLineIndex_Type()
)
voiceProfileLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineIndex.setStatus("current")
_VoiceProfileLineEnable_Type = VoiceProfileLineStateType
_VoiceProfileLineEnable_Object = MibTableColumn
voiceProfileLineEnable = _VoiceProfileLineEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 1, 1, 2),
    _VoiceProfileLineEnable_Type()
)
voiceProfileLineEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineEnable.setStatus("current")


class _VoiceProfileLineDirectoryNumber_Type(OctetString):
    """Custom type voiceProfileLineDirectoryNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoiceProfileLineDirectoryNumber_Type.__name__ = "OctetString"
_VoiceProfileLineDirectoryNumber_Object = MibTableColumn
voiceProfileLineDirectoryNumber = _VoiceProfileLineDirectoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 1, 1, 3),
    _VoiceProfileLineDirectoryNumber_Type()
)
voiceProfileLineDirectoryNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineDirectoryNumber.setStatus("current")
_VoiceProfileLineStatus_Type = VoiceLineStatusValues
_VoiceProfileLineStatus_Object = MibTableColumn
voiceProfileLineStatus = _VoiceProfileLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 1, 1, 4),
    _VoiceProfileLineStatus_Type()
)
voiceProfileLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineStatus.setStatus("current")
_VoiceProfileLineCallState_Type = VoiceLineCallStateValues
_VoiceProfileLineCallState_Object = MibTableColumn
voiceProfileLineCallState = _VoiceProfileLineCallState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 1, 1, 5),
    _VoiceProfileLineCallState_Type()
)
voiceProfileLineCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineCallState.setStatus("current")


class _VoiceProfileLinePhyReferenceList_Type(OctetString):
    """Custom type voiceProfileLinePhyReferenceList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoiceProfileLinePhyReferenceList_Type.__name__ = "OctetString"
_VoiceProfileLinePhyReferenceList_Object = MibTableColumn
voiceProfileLinePhyReferenceList = _VoiceProfileLinePhyReferenceList_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 1, 1, 6),
    _VoiceProfileLinePhyReferenceList_Type()
)
voiceProfileLinePhyReferenceList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLinePhyReferenceList.setStatus("current")


class _VoiceProfileLineCMAcntNum_Type(Unsigned32):
    """Custom type voiceProfileLineCMAcntNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_VoiceProfileLineCMAcntNum_Type.__name__ = "Unsigned32"
_VoiceProfileLineCMAcntNum_Object = MibTableColumn
voiceProfileLineCMAcntNum = _VoiceProfileLineCMAcntNum_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 1, 1, 7),
    _VoiceProfileLineCMAcntNum_Type()
)
voiceProfileLineCMAcntNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineCMAcntNum.setStatus("current")
_VoiceProfileLineOnhook_Type = TruthValue
_VoiceProfileLineOnhook_Object = MibTableColumn
voiceProfileLineOnhook = _VoiceProfileLineOnhook_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 1, 1, 8),
    _VoiceProfileLineOnhook_Type()
)
voiceProfileLineOnhook.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineOnhook.setStatus("current")
_VoiceProfileLineRowStatus_Type = ZhoneRowStatus
_VoiceProfileLineRowStatus_Object = MibTableColumn
voiceProfileLineRowStatus = _VoiceProfileLineRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 1, 1, 9),
    _VoiceProfileLineRowStatus_Type()
)
voiceProfileLineRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineRowStatus.setStatus("current")
_VoiceProfileLineSIPTable_Object = MibTable
voiceProfileLineSIPTable = _VoiceProfileLineSIPTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 2)
)
if mibBuilder.loadTexts:
    voiceProfileLineSIPTable.setStatus("current")
_VoiceProfileLineSIPEntry_Object = MibTableRow
voiceProfileLineSIPEntry = _VoiceProfileLineSIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 2, 1)
)
voiceProfileLineSIPEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
    (0, "ZHNVOICE", "voiceProfileIndex"),
    (0, "ZHNVOICE", "voiceProfileLineIndex"),
)
if mibBuilder.loadTexts:
    voiceProfileLineSIPEntry.setStatus("current")


class _VoiceProfileLineSIPAuthUserName_Type(OctetString):
    """Custom type voiceProfileLineSIPAuthUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_VoiceProfileLineSIPAuthUserName_Type.__name__ = "OctetString"
_VoiceProfileLineSIPAuthUserName_Object = MibTableColumn
voiceProfileLineSIPAuthUserName = _VoiceProfileLineSIPAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 2, 1, 1),
    _VoiceProfileLineSIPAuthUserName_Type()
)
voiceProfileLineSIPAuthUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineSIPAuthUserName.setStatus("current")


class _VoiceProfileLineSIPAuthPassword_Type(OctetString):
    """Custom type voiceProfileLineSIPAuthPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_VoiceProfileLineSIPAuthPassword_Type.__name__ = "OctetString"
_VoiceProfileLineSIPAuthPassword_Object = MibTableColumn
voiceProfileLineSIPAuthPassword = _VoiceProfileLineSIPAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 2, 1, 2),
    _VoiceProfileLineSIPAuthPassword_Type()
)
voiceProfileLineSIPAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineSIPAuthPassword.setStatus("current")


class _VoiceProfileLineSIPURI_Type(OctetString):
    """Custom type voiceProfileLineSIPURI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 389),
    )


_VoiceProfileLineSIPURI_Type.__name__ = "OctetString"
_VoiceProfileLineSIPURI_Object = MibTableColumn
voiceProfileLineSIPURI = _VoiceProfileLineSIPURI_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 2, 1, 3),
    _VoiceProfileLineSIPURI_Type()
)
voiceProfileLineSIPURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineSIPURI.setStatus("current")


class _VoiceProfileLineSIPPlarUserName_Type(OctetString):
    """Custom type voiceProfileLineSIPPlarUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_VoiceProfileLineSIPPlarUserName_Type.__name__ = "OctetString"
_VoiceProfileLineSIPPlarUserName_Object = MibTableColumn
voiceProfileLineSIPPlarUserName = _VoiceProfileLineSIPPlarUserName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 2, 1, 4),
    _VoiceProfileLineSIPPlarUserName_Type()
)
voiceProfileLineSIPPlarUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineSIPPlarUserName.setStatus("current")
_VoiceProfileLineMGCPTable_Object = MibTable
voiceProfileLineMGCPTable = _VoiceProfileLineMGCPTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 3)
)
if mibBuilder.loadTexts:
    voiceProfileLineMGCPTable.setStatus("current")
_VoiceProfileLineMGCPEntry_Object = MibTableRow
voiceProfileLineMGCPEntry = _VoiceProfileLineMGCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 3, 1)
)
voiceProfileLineMGCPEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
    (0, "ZHNVOICE", "voiceProfileIndex"),
    (0, "ZHNVOICE", "voiceProfileLineIndex"),
)
if mibBuilder.loadTexts:
    voiceProfileLineMGCPEntry.setStatus("current")


class _VoiceProfileLineMGCPLineName_Type(OctetString):
    """Custom type voiceProfileLineMGCPLineName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoiceProfileLineMGCPLineName_Type.__name__ = "OctetString"
_VoiceProfileLineMGCPLineName_Object = MibTableColumn
voiceProfileLineMGCPLineName = _VoiceProfileLineMGCPLineName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 3, 1, 1),
    _VoiceProfileLineMGCPLineName_Type()
)
voiceProfileLineMGCPLineName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineMGCPLineName.setStatus("current")
_VoiceProfileLineProcessingTable_Object = MibTable
voiceProfileLineProcessingTable = _VoiceProfileLineProcessingTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 4)
)
if mibBuilder.loadTexts:
    voiceProfileLineProcessingTable.setStatus("current")
_VoiceProfileLineProcessingEntry_Object = MibTableRow
voiceProfileLineProcessingEntry = _VoiceProfileLineProcessingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 4, 1)
)
voiceProfileLineProcessingEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
    (0, "ZHNVOICE", "voiceProfileIndex"),
    (0, "ZHNVOICE", "voiceProfileLineIndex"),
)
if mibBuilder.loadTexts:
    voiceProfileLineProcessingEntry.setStatus("current")
_VoiceProfileLineTransmitGain_Type = Integer32
_VoiceProfileLineTransmitGain_Object = MibTableColumn
voiceProfileLineTransmitGain = _VoiceProfileLineTransmitGain_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 4, 1, 1),
    _VoiceProfileLineTransmitGain_Type()
)
voiceProfileLineTransmitGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineTransmitGain.setStatus("current")
_VoiceProfileLineReceiveGain_Type = Integer32
_VoiceProfileLineReceiveGain_Object = MibTableColumn
voiceProfileLineReceiveGain = _VoiceProfileLineReceiveGain_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 4, 1, 2),
    _VoiceProfileLineReceiveGain_Type()
)
voiceProfileLineReceiveGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineReceiveGain.setStatus("current")
_VoiceProfileLineEchoCancellationEnable_Type = TruthValue
_VoiceProfileLineEchoCancellationEnable_Object = MibTableColumn
voiceProfileLineEchoCancellationEnable = _VoiceProfileLineEchoCancellationEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 4, 1, 3),
    _VoiceProfileLineEchoCancellationEnable_Type()
)
voiceProfileLineEchoCancellationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineEchoCancellationEnable.setStatus("current")
_VoiceProfileLineEchoCancellationInUse_Type = TruthValue
_VoiceProfileLineEchoCancellationInUse_Object = MibTableColumn
voiceProfileLineEchoCancellationInUse = _VoiceProfileLineEchoCancellationInUse_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 4, 1, 4),
    _VoiceProfileLineEchoCancellationInUse_Type()
)
voiceProfileLineEchoCancellationInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineEchoCancellationInUse.setStatus("current")
_VoiceProfileLineCodecTable_Object = MibTable
voiceProfileLineCodecTable = _VoiceProfileLineCodecTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 5)
)
if mibBuilder.loadTexts:
    voiceProfileLineCodecTable.setStatus("current")
_VoiceProfileLineCodecEntry_Object = MibTableRow
voiceProfileLineCodecEntry = _VoiceProfileLineCodecEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 5, 1)
)
voiceProfileLineCodecEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
    (0, "ZHNVOICE", "voiceProfileIndex"),
    (0, "ZHNVOICE", "voiceProfileLineIndex"),
    (0, "ZHNVOICE", "voiceProfileLineCodecIndex"),
)
if mibBuilder.loadTexts:
    voiceProfileLineCodecEntry.setStatus("current")
_VoiceProfileLineCodecIndex_Type = Unsigned32
_VoiceProfileLineCodecIndex_Object = MibTableColumn
voiceProfileLineCodecIndex = _VoiceProfileLineCodecIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 5, 1, 1),
    _VoiceProfileLineCodecIndex_Type()
)
voiceProfileLineCodecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineCodecIndex.setStatus("current")
_VoiceProfileLineCodecEntryID_Type = Unsigned32
_VoiceProfileLineCodecEntryID_Object = MibTableColumn
voiceProfileLineCodecEntryID = _VoiceProfileLineCodecEntryID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 5, 1, 2),
    _VoiceProfileLineCodecEntryID_Type()
)
voiceProfileLineCodecEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineCodecEntryID.setStatus("current")


class _VoiceProfileLineCodec_Type(OctetString):
    """Custom type voiceProfileLineCodec based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_VoiceProfileLineCodec_Type.__name__ = "OctetString"
_VoiceProfileLineCodec_Object = MibTableColumn
voiceProfileLineCodec = _VoiceProfileLineCodec_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 5, 1, 3),
    _VoiceProfileLineCodec_Type()
)
voiceProfileLineCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineCodec.setStatus("current")
_VoiceProfileLineCodecBitRate_Type = Unsigned32
_VoiceProfileLineCodecBitRate_Object = MibTableColumn
voiceProfileLineCodecBitRate = _VoiceProfileLineCodecBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 5, 1, 4),
    _VoiceProfileLineCodecBitRate_Type()
)
voiceProfileLineCodecBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineCodecBitRate.setStatus("current")


class _VoiceProfileLineCodecPacketizationPeriod_Type(OctetString):
    """Custom type voiceProfileLineCodecPacketizationPeriod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_VoiceProfileLineCodecPacketizationPeriod_Type.__name__ = "OctetString"
_VoiceProfileLineCodecPacketizationPeriod_Object = MibTableColumn
voiceProfileLineCodecPacketizationPeriod = _VoiceProfileLineCodecPacketizationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 5, 1, 5),
    _VoiceProfileLineCodecPacketizationPeriod_Type()
)
voiceProfileLineCodecPacketizationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineCodecPacketizationPeriod.setStatus("current")
_VoiceProfileLineCodecSilenceSuppression_Type = TruthValue
_VoiceProfileLineCodecSilenceSuppression_Object = MibTableColumn
voiceProfileLineCodecSilenceSuppression = _VoiceProfileLineCodecSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 5, 1, 6),
    _VoiceProfileLineCodecSilenceSuppression_Type()
)
voiceProfileLineCodecSilenceSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineCodecSilenceSuppression.setStatus("current")
_VoiceProfileLineCodecEnable_Type = TruthValue
_VoiceProfileLineCodecEnable_Object = MibTableColumn
voiceProfileLineCodecEnable = _VoiceProfileLineCodecEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 5, 1, 7),
    _VoiceProfileLineCodecEnable_Type()
)
voiceProfileLineCodecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineCodecEnable.setStatus("current")
_VoiceProfileLineCodecPriority_Type = Unsigned32
_VoiceProfileLineCodecPriority_Object = MibTableColumn
voiceProfileLineCodecPriority = _VoiceProfileLineCodecPriority_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 5, 1, 8),
    _VoiceProfileLineCodecPriority_Type()
)
voiceProfileLineCodecPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineCodecPriority.setStatus("current")
_VoiceProfileLineCallingFeaturesTable_Object = MibTable
voiceProfileLineCallingFeaturesTable = _VoiceProfileLineCallingFeaturesTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 6)
)
if mibBuilder.loadTexts:
    voiceProfileLineCallingFeaturesTable.setStatus("current")
_VoiceProfileLineCallingFeaturesEntry_Object = MibTableRow
voiceProfileLineCallingFeaturesEntry = _VoiceProfileLineCallingFeaturesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 6, 1)
)
voiceProfileLineCallingFeaturesEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
    (0, "ZHNVOICE", "voiceProfileIndex"),
    (0, "ZHNVOICE", "voiceProfileLineIndex"),
)
if mibBuilder.loadTexts:
    voiceProfileLineCallingFeaturesEntry.setStatus("current")
_VoiceProfileLineCallingFeatureCallerIDEnable_Type = TruthValue
_VoiceProfileLineCallingFeatureCallerIDEnable_Object = MibTableColumn
voiceProfileLineCallingFeatureCallerIDEnable = _VoiceProfileLineCallingFeatureCallerIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 6, 1, 1),
    _VoiceProfileLineCallingFeatureCallerIDEnable_Type()
)
voiceProfileLineCallingFeatureCallerIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineCallingFeatureCallerIDEnable.setStatus("current")


class _VoiceProfileLineCallingFeatureCallerIDName_Type(OctetString):
    """Custom type voiceProfileLineCallingFeatureCallerIDName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceProfileLineCallingFeatureCallerIDName_Type.__name__ = "OctetString"
_VoiceProfileLineCallingFeatureCallerIDName_Object = MibTableColumn
voiceProfileLineCallingFeatureCallerIDName = _VoiceProfileLineCallingFeatureCallerIDName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 6, 1, 2),
    _VoiceProfileLineCallingFeatureCallerIDName_Type()
)
voiceProfileLineCallingFeatureCallerIDName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineCallingFeatureCallerIDName.setStatus("current")
_VoiceProfileLineCallingFeatureCallWaitingEnable_Type = TruthValue
_VoiceProfileLineCallingFeatureCallWaitingEnable_Object = MibTableColumn
voiceProfileLineCallingFeatureCallWaitingEnable = _VoiceProfileLineCallingFeatureCallWaitingEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 6, 1, 3),
    _VoiceProfileLineCallingFeatureCallWaitingEnable_Type()
)
voiceProfileLineCallingFeatureCallWaitingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineCallingFeatureCallWaitingEnable.setStatus("current")
_VoiceProfileLineCallingFeatureMaxSessions_Type = Unsigned32
_VoiceProfileLineCallingFeatureMaxSessions_Object = MibTableColumn
voiceProfileLineCallingFeatureMaxSessions = _VoiceProfileLineCallingFeatureMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 6, 1, 4),
    _VoiceProfileLineCallingFeatureMaxSessions_Type()
)
voiceProfileLineCallingFeatureMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineCallingFeatureMaxSessions.setStatus("current")
_VoiceProfileLineCallingFeatureMWIEnable_Type = TruthValue
_VoiceProfileLineCallingFeatureMWIEnable_Object = MibTableColumn
voiceProfileLineCallingFeatureMWIEnable = _VoiceProfileLineCallingFeatureMWIEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 6, 1, 5),
    _VoiceProfileLineCallingFeatureMWIEnable_Type()
)
voiceProfileLineCallingFeatureMWIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceProfileLineCallingFeatureMWIEnable.setStatus("current")
_VoiceProfileLineStatsTable_Object = MibTable
voiceProfileLineStatsTable = _VoiceProfileLineStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 7)
)
if mibBuilder.loadTexts:
    voiceProfileLineStatsTable.setStatus("current")
_VoiceProfileLineStatsEntry_Object = MibTableRow
voiceProfileLineStatsEntry = _VoiceProfileLineStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 7, 1)
)
voiceProfileLineStatsEntry.setIndexNames(
    (0, "ZHNVOICE", "voiceServiceIndex"),
    (0, "ZHNVOICE", "voiceProfileIndex"),
    (0, "ZHNVOICE", "voiceProfileLineIndex"),
)
if mibBuilder.loadTexts:
    voiceProfileLineStatsEntry.setStatus("current")
_VoiceProfileLineStatsPacketsSent_Type = Unsigned32
_VoiceProfileLineStatsPacketsSent_Object = MibTableColumn
voiceProfileLineStatsPacketsSent = _VoiceProfileLineStatsPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 7, 1, 1),
    _VoiceProfileLineStatsPacketsSent_Type()
)
voiceProfileLineStatsPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineStatsPacketsSent.setStatus("current")
_VoiceProfileLineStatsPacketsReceived_Type = Unsigned32
_VoiceProfileLineStatsPacketsReceived_Object = MibTableColumn
voiceProfileLineStatsPacketsReceived = _VoiceProfileLineStatsPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 7, 1, 2),
    _VoiceProfileLineStatsPacketsReceived_Type()
)
voiceProfileLineStatsPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineStatsPacketsReceived.setStatus("current")
_VoiceProfileLineStatsBytesSent_Type = Unsigned32
_VoiceProfileLineStatsBytesSent_Object = MibTableColumn
voiceProfileLineStatsBytesSent = _VoiceProfileLineStatsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 7, 1, 3),
    _VoiceProfileLineStatsBytesSent_Type()
)
voiceProfileLineStatsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineStatsBytesSent.setStatus("current")
_VoiceProfileLineStatsBytesReceived_Type = Unsigned32
_VoiceProfileLineStatsBytesReceived_Object = MibTableColumn
voiceProfileLineStatsBytesReceived = _VoiceProfileLineStatsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 7, 1, 4),
    _VoiceProfileLineStatsBytesReceived_Type()
)
voiceProfileLineStatsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineStatsBytesReceived.setStatus("current")
_VoiceProfileLineStatsPacketsLost_Type = Unsigned32
_VoiceProfileLineStatsPacketsLost_Object = MibTableColumn
voiceProfileLineStatsPacketsLost = _VoiceProfileLineStatsPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 7, 1, 5),
    _VoiceProfileLineStatsPacketsLost_Type()
)
voiceProfileLineStatsPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineStatsPacketsLost.setStatus("current")
_VoiceProfileLineStatsIncomingCallsReceived_Type = Unsigned32
_VoiceProfileLineStatsIncomingCallsReceived_Object = MibTableColumn
voiceProfileLineStatsIncomingCallsReceived = _VoiceProfileLineStatsIncomingCallsReceived_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 7, 1, 6),
    _VoiceProfileLineStatsIncomingCallsReceived_Type()
)
voiceProfileLineStatsIncomingCallsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineStatsIncomingCallsReceived.setStatus("current")
_VoiceProfileLineStatsIncomingCallsAnswered_Type = Unsigned32
_VoiceProfileLineStatsIncomingCallsAnswered_Object = MibTableColumn
voiceProfileLineStatsIncomingCallsAnswered = _VoiceProfileLineStatsIncomingCallsAnswered_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 7, 1, 7),
    _VoiceProfileLineStatsIncomingCallsAnswered_Type()
)
voiceProfileLineStatsIncomingCallsAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineStatsIncomingCallsAnswered.setStatus("current")
_VoiceProfileLineStatsIncomingCallsConnected_Type = Unsigned32
_VoiceProfileLineStatsIncomingCallsConnected_Object = MibTableColumn
voiceProfileLineStatsIncomingCallsConnected = _VoiceProfileLineStatsIncomingCallsConnected_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 7, 1, 8),
    _VoiceProfileLineStatsIncomingCallsConnected_Type()
)
voiceProfileLineStatsIncomingCallsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineStatsIncomingCallsConnected.setStatus("current")
_VoiceProfileLineStatsIncomingCallsFailed_Type = Unsigned32
_VoiceProfileLineStatsIncomingCallsFailed_Object = MibTableColumn
voiceProfileLineStatsIncomingCallsFailed = _VoiceProfileLineStatsIncomingCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 7, 1, 9),
    _VoiceProfileLineStatsIncomingCallsFailed_Type()
)
voiceProfileLineStatsIncomingCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineStatsIncomingCallsFailed.setStatus("current")
_VoiceProfileLineStatsOutgoingCallsAttempted_Type = Unsigned32
_VoiceProfileLineStatsOutgoingCallsAttempted_Object = MibTableColumn
voiceProfileLineStatsOutgoingCallsAttempted = _VoiceProfileLineStatsOutgoingCallsAttempted_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 7, 1, 10),
    _VoiceProfileLineStatsOutgoingCallsAttempted_Type()
)
voiceProfileLineStatsOutgoingCallsAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineStatsOutgoingCallsAttempted.setStatus("current")
_VoiceProfileLineStatsOutgoingCallsAnswered_Type = Unsigned32
_VoiceProfileLineStatsOutgoingCallsAnswered_Object = MibTableColumn
voiceProfileLineStatsOutgoingCallsAnswered = _VoiceProfileLineStatsOutgoingCallsAnswered_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 7, 1, 11),
    _VoiceProfileLineStatsOutgoingCallsAnswered_Type()
)
voiceProfileLineStatsOutgoingCallsAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineStatsOutgoingCallsAnswered.setStatus("current")
_VoiceProfileLineStatsOutgoingCallsConnected_Type = Unsigned32
_VoiceProfileLineStatsOutgoingCallsConnected_Object = MibTableColumn
voiceProfileLineStatsOutgoingCallsConnected = _VoiceProfileLineStatsOutgoingCallsConnected_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 7, 1, 12),
    _VoiceProfileLineStatsOutgoingCallsConnected_Type()
)
voiceProfileLineStatsOutgoingCallsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineStatsOutgoingCallsConnected.setStatus("current")
_VoiceProfileLineStatsOutgoingCallsFailed_Type = Unsigned32
_VoiceProfileLineStatsOutgoingCallsFailed_Object = MibTableColumn
voiceProfileLineStatsOutgoingCallsFailed = _VoiceProfileLineStatsOutgoingCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 1, 3, 8, 7, 1, 13),
    _VoiceProfileLineStatsOutgoingCallsFailed_Type()
)
voiceProfileLineStatsOutgoingCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceProfileLineStatsOutgoingCallsFailed.setStatus("current")
_ZhnVoiceConformance_ObjectIdentity = ObjectIdentity
zhnVoiceConformance = _ZhnVoiceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2)
)
_ZhnVoiceGroups_ObjectIdentity = ObjectIdentity
zhnVoiceGroups = _ZhnVoiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1)
)
_ZhnVoiceCompliances_ObjectIdentity = ObjectIdentity
zhnVoiceCompliances = _ZhnVoiceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 2)
)

# Managed Objects groups

zhnVoiceServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 1)
)
zhnVoiceServiceGroup.setObjects(
      *(("ZHNVOICE", "voiceProfileNumberOfEntries"),
        ("ZHNVOICE", "voiceBoundIfName"),
        ("ZHNVOICE", "voiceBoundIpAddr"),
        ("ZHNVOICE", "voiceServiceIndex"))
)
if mibBuilder.loadTexts:
    zhnVoiceServiceGroup.setStatus("current")

zhnVoiceCapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 2)
)
zhnVoiceCapabilitiesGroup.setObjects(
      *(("ZHNVOICE", "maxProfileCount"),
        ("ZHNVOICE", "maxLineCount"),
        ("ZHNVOICE", "maxSessionsPerLine"),
        ("ZHNVOICE", "maxSessionCount"),
        ("ZHNVOICE", "signalingProtocols"),
        ("ZHNVOICE", "regions"),
        ("ZHNVOICE", "rtcp"),
        ("ZHNVOICE", "srtp"),
        ("ZHNVOICE", "rtpRedundancy"),
        ("ZHNVOICE", "dscpCoupled"),
        ("ZHNVOICE", "ethernetTaggingCoupled"),
        ("ZHNVOICE", "pstnSoftSwitchOver"),
        ("ZHNVOICE", "faxT38"),
        ("ZHNVOICE", "faxPassThrough"),
        ("ZHNVOICE", "modemPassThrough"),
        ("ZHNVOICE", "toneGeneration"),
        ("ZHNVOICE", "ringGeneration"),
        ("ZHNVOICE", "digitMapCapabilities"),
        ("ZHNVOICE", "numberingPlan"),
        ("ZHNVOICE", "buttonMap"),
        ("ZHNVOICE", "voicePortTests"))
)
if mibBuilder.loadTexts:
    zhnVoiceCapabilitiesGroup.setStatus("current")

zhnVoiceCapabilitiesSIPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 3)
)
zhnVoiceCapabilitiesSIPGroup.setObjects(
      *(("ZHNVOICE", "role"),
        ("ZHNVOICE", "extensionsSIP"),
        ("ZHNVOICE", "transports"),
        ("ZHNVOICE", "uriSchemes"),
        ("ZHNVOICE", "eventSubscription"),
        ("ZHNVOICE", "responseMap"),
        ("ZHNVOICE", "tlsKeyExchangeProtocols"))
)
if mibBuilder.loadTexts:
    zhnVoiceCapabilitiesSIPGroup.setStatus("current")

zhnVoiceCapabilitiesMGCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 4)
)
zhnVoiceCapabilitiesMGCPGroup.setObjects(
    ("ZHNVOICE", "extensionsMGCP")
)
if mibBuilder.loadTexts:
    zhnVoiceCapabilitiesMGCPGroup.setStatus("current")

zhnVoiceCapabilitiesCodecsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 5)
)
zhnVoiceCapabilitiesCodecsGroup.setObjects(
      *(("ZHNVOICE", "codecIndex"),
        ("ZHNVOICE", "entryID"),
        ("ZHNVOICE", "codec"),
        ("ZHNVOICE", "bitRate"),
        ("ZHNVOICE", "packetizationPeriod"),
        ("ZHNVOICE", "silenceSuppression"))
)
if mibBuilder.loadTexts:
    zhnVoiceCapabilitiesCodecsGroup.setStatus("current")

zhnVoiceProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 6)
)
zhnVoiceProfileGroup.setObjects(
      *(("ZHNVOICE", "voiceProfileIndex"),
        ("ZHNVOICE", "voiceProfileEnable"),
        ("ZHNVOICE", "voiceProfileReset"),
        ("ZHNVOICE", "voiceProfileNumberOfLines"),
        ("ZHNVOICE", "voiceProfileName"),
        ("ZHNVOICE", "voiceProfileSignalingProtocol"),
        ("ZHNVOICE", "voiceProfileMaxSessions"),
        ("ZHNVOICE", "voiceProfileDtmfMethod"),
        ("ZHNVOICE", "voiceProfileDtmfMethodG711"),
        ("ZHNVOICE", "voiceProfileHookFlashMethod"),
        ("ZHNVOICE", "voiceProfileRegion"),
        ("ZHNVOICE", "voiceProfileDigitMap"),
        ("ZHNVOICE", "voiceProfileDigitMapEnable"),
        ("ZHNVOICE", "voiceProfileStunEnable"),
        ("ZHNVOICE", "voiceProfileStunServer"),
        ("ZHNVOICE", "voiceProfileStunServerPort"),
        ("ZHNVOICE", "voiceProfileLogServer"),
        ("ZHNVOICE", "voiceProfileLogServerPort"),
        ("ZHNVOICE", "voiceProfileSpNum"),
        ("ZHNVOICE", "voiceProfileV18Support"),
        ("ZHNVOICE", "voiceProfileSwitchType"))
)
if mibBuilder.loadTexts:
    zhnVoiceProfileGroup.setStatus("current")

zhnVoiceProfileServiceProviderGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 7)
)
zhnVoiceProfileServiceProviderGroup.setObjects(
    ("ZHNVOICE", "voiceProfileServiceProviderName")
)
if mibBuilder.loadTexts:
    zhnVoiceProfileServiceProviderGroup.setStatus("current")

zhnVoiceProfileSIPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 8)
)
zhnVoiceProfileSIPGroup.setObjects(
      *(("ZHNVOICE", "voiceProfileSIPProxyServer"),
        ("ZHNVOICE", "voiceProfileSIPProxyServerPort"),
        ("ZHNVOICE", "voiceProfileSIPProxyServerTransport"),
        ("ZHNVOICE", "voiceProfileSIPRegistrarServer"),
        ("ZHNVOICE", "voiceProfileSIPRegistrarServerPort"),
        ("ZHNVOICE", "voiceProfileSIPRegistrarServerTransport"),
        ("ZHNVOICE", "voiceProfileSIPToTagMatching"),
        ("ZHNVOICE", "voiceProfileSIPMusicServer"),
        ("ZHNVOICE", "voiceProfileSIPMusicServerPort"),
        ("ZHNVOICE", "voiceProfileSIPPlarGateway"),
        ("ZHNVOICE", "voiceProfileSIPPlarPort"),
        ("ZHNVOICE", "voiceProfileSIPUserAgentDomain"),
        ("ZHNVOICE", "voiceProfileSIPUserAgentPort"),
        ("ZHNVOICE", "voiceProfileSIPUserAgentTransport"),
        ("ZHNVOICE", "voiceProfileSIPOutboundProxy"),
        ("ZHNVOICE", "voiceProfileSIPOutboundProxyPort"),
        ("ZHNVOICE", "voiceProfileSIPOrganization"),
        ("ZHNVOICE", "voiceProfileSIPRegistrationPeriod"),
        ("ZHNVOICE", "voiceProfileSIPRegisterExpires"),
        ("ZHNVOICE", "voiceProfileSIPRegisterRetryInterval"),
        ("ZHNVOICE", "voiceProfileSIPDSCPMark"),
        ("ZHNVOICE", "voiceProfileSIPVLANIDMark"),
        ("ZHNVOICE", "voiceProfileSIPEthernetPriorityMark"),
        ("ZHNVOICE", "voiceProfileSIPInterdigitTimeout"),
        ("ZHNVOICE", "voiceProfileSIPAddressMode"))
)
if mibBuilder.loadTexts:
    zhnVoiceProfileSIPGroup.setStatus("current")

zhnVoiceProfileSIPEventSubscribeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 9)
)
zhnVoiceProfileSIPEventSubscribeGroup.setObjects(
      *(("ZHNVOICE", "voiceProfileSIPEventSubscribeEvent"),
        ("ZHNVOICE", "voiceProfileSIPEventSubscribeNotifier"),
        ("ZHNVOICE", "voiceProfileSIPEventSubscribeNotifierPort"),
        ("ZHNVOICE", "voiceProfileSIPEventSubscribeNotifierTransport"))
)
if mibBuilder.loadTexts:
    zhnVoiceProfileSIPEventSubscribeGroup.setStatus("current")

zhnVoiceProfileMGCPEntry = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 10)
)
zhnVoiceProfileMGCPEntry.setObjects(
      *(("ZHNVOICE", "voiceProfileMGCPCallAgent1"),
        ("ZHNVOICE", "voiceProfileMGCPUser"),
        ("ZHNVOICE", "voiceProfilePersistentNotify"),
        ("ZHNVOICE", "voiceProfileMGCPAddressMode"))
)
if mibBuilder.loadTexts:
    zhnVoiceProfileMGCPEntry.setStatus("current")

zhnVoiceProfileRTPEntry = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 11)
)
zhnVoiceProfileRTPEntry.setObjects(
      *(("ZHNVOICE", "voiceProfileRTPLocalPortMin"),
        ("ZHNVOICE", "voiceProfileRTPLocalPortMax"),
        ("ZHNVOICE", "voiceProfileRTPDSCPMark"),
        ("ZHNVOICE", "voiceProfileRTPTelephoneEventPayloadType"))
)
if mibBuilder.loadTexts:
    zhnVoiceProfileRTPEntry.setStatus("current")

zhnVoiceProfileFaxT38Entry = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 12)
)
zhnVoiceProfileFaxT38Entry.setObjects(
      *(("ZHNVOICE", "voiceProfileFaxT38Enable"),
        ("ZHNVOICE", "voiceProfileFaxT38BitRate"),
        ("ZHNVOICE", "voiceProfileFaxT38HighSpeedPacketRate"))
)
if mibBuilder.loadTexts:
    zhnVoiceProfileFaxT38Entry.setStatus("current")

zhnVoiceProfileLineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 13)
)
zhnVoiceProfileLineGroup.setObjects(
      *(("ZHNVOICE", "voiceProfileLineIndex"),
        ("ZHNVOICE", "voiceProfileLineEnable"),
        ("ZHNVOICE", "voiceProfileLineDirectoryNumber"),
        ("ZHNVOICE", "voiceProfileLineStatus"),
        ("ZHNVOICE", "voiceProfileLineCallState"),
        ("ZHNVOICE", "voiceProfileLinePhyReferenceList"),
        ("ZHNVOICE", "voiceProfileLineCMAcntNum"),
        ("ZHNVOICE", "voiceProfileLineOnhook"),
        ("ZHNVOICE", "voiceProfileLineRowStatus"))
)
if mibBuilder.loadTexts:
    zhnVoiceProfileLineGroup.setStatus("current")

zhnVoiceProfileLineProcessingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 14)
)
zhnVoiceProfileLineProcessingGroup.setObjects(
      *(("ZHNVOICE", "voiceProfileLineTransmitGain"),
        ("ZHNVOICE", "voiceProfileLineReceiveGain"),
        ("ZHNVOICE", "voiceProfileLineEchoCancellationEnable"),
        ("ZHNVOICE", "voiceProfileLineEchoCancellationInUse"))
)
if mibBuilder.loadTexts:
    zhnVoiceProfileLineProcessingGroup.setStatus("current")

zhnVoiceProfileLineSIPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 15)
)
zhnVoiceProfileLineSIPGroup.setObjects(
      *(("ZHNVOICE", "voiceProfileLineSIPAuthUserName"),
        ("ZHNVOICE", "voiceProfileLineSIPAuthPassword"),
        ("ZHNVOICE", "voiceProfileLineSIPURI"),
        ("ZHNVOICE", "voiceProfileLineSIPPlarUserName"))
)
if mibBuilder.loadTexts:
    zhnVoiceProfileLineSIPGroup.setStatus("current")

zhnVoiceProfileLineMGCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 16)
)
zhnVoiceProfileLineMGCPGroup.setObjects(
    ("ZHNVOICE", "voiceProfileLineMGCPLineName")
)
if mibBuilder.loadTexts:
    zhnVoiceProfileLineMGCPGroup.setStatus("current")

zhnVoiceProfileLineCodecsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 17)
)
zhnVoiceProfileLineCodecsGroup.setObjects(
      *(("ZHNVOICE", "voiceProfileLineCodecIndex"),
        ("ZHNVOICE", "voiceProfileLineCodecEntryID"),
        ("ZHNVOICE", "voiceProfileLineCodec"),
        ("ZHNVOICE", "voiceProfileLineCodecBitRate"),
        ("ZHNVOICE", "voiceProfileLineCodecPacketizationPeriod"),
        ("ZHNVOICE", "voiceProfileLineCodecSilenceSuppression"),
        ("ZHNVOICE", "voiceProfileLineCodecEnable"),
        ("ZHNVOICE", "voiceProfileLineCodecPriority"))
)
if mibBuilder.loadTexts:
    zhnVoiceProfileLineCodecsGroup.setStatus("current")

zhnVoiceLineCallingFeaturesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 18)
)
zhnVoiceLineCallingFeaturesGroup.setObjects(
      *(("ZHNVOICE", "voiceProfileLineCallingFeatureCallerIDEnable"),
        ("ZHNVOICE", "voiceProfileLineCallingFeatureCallerIDName"),
        ("ZHNVOICE", "voiceProfileLineCallingFeatureCallWaitingEnable"),
        ("ZHNVOICE", "voiceProfileLineCallingFeatureMaxSessions"),
        ("ZHNVOICE", "voiceProfileLineCallingFeatureMWIEnable"))
)
if mibBuilder.loadTexts:
    zhnVoiceLineCallingFeaturesGroup.setStatus("current")

zhnVoiceProfileLineStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 20)
)
zhnVoiceProfileLineStatsGroup.setObjects(
      *(("ZHNVOICE", "voiceProfileLineStatsPacketsSent"),
        ("ZHNVOICE", "voiceProfileLineStatsPacketsReceived"),
        ("ZHNVOICE", "voiceProfileLineStatsBytesSent"),
        ("ZHNVOICE", "voiceProfileLineStatsBytesReceived"),
        ("ZHNVOICE", "voiceProfileLineStatsPacketsLost"),
        ("ZHNVOICE", "voiceProfileLineStatsIncomingCallsReceived"),
        ("ZHNVOICE", "voiceProfileLineStatsIncomingCallsAnswered"),
        ("ZHNVOICE", "voiceProfileLineStatsIncomingCallsConnected"),
        ("ZHNVOICE", "voiceProfileLineStatsIncomingCallsFailed"),
        ("ZHNVOICE", "voiceProfileLineStatsOutgoingCallsAttempted"),
        ("ZHNVOICE", "voiceProfileLineStatsOutgoingCallsAnswered"),
        ("ZHNVOICE", "voiceProfileLineStatsOutgoingCallsConnected"),
        ("ZHNVOICE", "voiceProfileLineStatsOutgoingCallsFailed"))
)
if mibBuilder.loadTexts:
    zhnVoiceProfileLineStatsGroup.setStatus("current")


# Notification objects

voiceRegistrationUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 0, 1)
)
if mibBuilder.loadTexts:
    voiceRegistrationUp.setStatus(
        "current"
    )

voiceRegistrationDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 0, 2)
)
if mibBuilder.loadTexts:
    voiceRegistrationDown.setStatus(
        "current"
    )


# Notifications groups

zhnVoiceNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 1, 19)
)
zhnVoiceNotificationGroup.setObjects(
      *(("ZHNVOICE", "voiceRegistrationUp"),
        ("ZHNVOICE", "voiceRegistrationDown"))
)
if mibBuilder.loadTexts:
    zhnVoiceNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

zhnVoiceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 40, 2, 2, 1)
)
if mibBuilder.loadTexts:
    zhnVoiceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHNVOICE",
    **{"VoiceProfileLineStateType": VoiceProfileLineStateType,
       "DTMFMethodValues": DTMFMethodValues,
       "HookFlashMethodValues": HookFlashMethodValues,
       "RegionValues": RegionValues,
       "VoiceTransportValues": VoiceTransportValues,
       "VoiceLineStatusValues": VoiceLineStatusValues,
       "VoiceLineCallStateValues": VoiceLineCallStateValues,
       "VoiceProfileAddressModes": VoiceProfileAddressModes,
       "VoiceProfileSwitchTypes": VoiceProfileSwitchTypes,
       "zhnVoice": zhnVoice,
       "zhnVoiceNotifications": zhnVoiceNotifications,
       "voiceRegistrationUp": voiceRegistrationUp,
       "voiceRegistrationDown": voiceRegistrationDown,
       "zhnVoiceServiceObjects": zhnVoiceServiceObjects,
       "voiceServiceTable": voiceServiceTable,
       "voiceServiceEntry": voiceServiceEntry,
       "voiceProfileNumberOfEntries": voiceProfileNumberOfEntries,
       "voiceBoundIfName": voiceBoundIfName,
       "voiceBoundIpAddr": voiceBoundIpAddr,
       "voiceServiceIndex": voiceServiceIndex,
       "capabilities": capabilities,
       "capabilitiesTable": capabilitiesTable,
       "capabilitiesEntry": capabilitiesEntry,
       "maxProfileCount": maxProfileCount,
       "maxLineCount": maxLineCount,
       "maxSessionsPerLine": maxSessionsPerLine,
       "maxSessionCount": maxSessionCount,
       "signalingProtocols": signalingProtocols,
       "regions": regions,
       "rtcp": rtcp,
       "srtp": srtp,
       "rtpRedundancy": rtpRedundancy,
       "dscpCoupled": dscpCoupled,
       "ethernetTaggingCoupled": ethernetTaggingCoupled,
       "pstnSoftSwitchOver": pstnSoftSwitchOver,
       "faxT38": faxT38,
       "faxPassThrough": faxPassThrough,
       "modemPassThrough": modemPassThrough,
       "toneGeneration": toneGeneration,
       "ringGeneration": ringGeneration,
       "digitMapCapabilities": digitMapCapabilities,
       "numberingPlan": numberingPlan,
       "buttonMap": buttonMap,
       "voicePortTests": voicePortTests,
       "capabilitiesSIPTable": capabilitiesSIPTable,
       "capabilitiesSIPEntry": capabilitiesSIPEntry,
       "role": role,
       "extensionsSIP": extensionsSIP,
       "transports": transports,
       "uriSchemes": uriSchemes,
       "eventSubscription": eventSubscription,
       "responseMap": responseMap,
       "tlsKeyExchangeProtocols": tlsKeyExchangeProtocols,
       "capabilitiesMGCPTable": capabilitiesMGCPTable,
       "capabilitiesMGCPEntry": capabilitiesMGCPEntry,
       "extensionsMGCP": extensionsMGCP,
       "capabilitiesCodecsTable": capabilitiesCodecsTable,
       "capabilitiesCodecsEntry": capabilitiesCodecsEntry,
       "codecIndex": codecIndex,
       "entryID": entryID,
       "codec": codec,
       "bitRate": bitRate,
       "packetizationPeriod": packetizationPeriod,
       "silenceSuppression": silenceSuppression,
       "voiceProfiles": voiceProfiles,
       "voiceProfileTable": voiceProfileTable,
       "voiceProfileEntry": voiceProfileEntry,
       "voiceProfileIndex": voiceProfileIndex,
       "voiceProfileEnable": voiceProfileEnable,
       "voiceProfileReset": voiceProfileReset,
       "voiceProfileNumberOfLines": voiceProfileNumberOfLines,
       "voiceProfileName": voiceProfileName,
       "voiceProfileSignalingProtocol": voiceProfileSignalingProtocol,
       "voiceProfileMaxSessions": voiceProfileMaxSessions,
       "voiceProfileDtmfMethod": voiceProfileDtmfMethod,
       "voiceProfileDtmfMethodG711": voiceProfileDtmfMethodG711,
       "voiceProfileHookFlashMethod": voiceProfileHookFlashMethod,
       "voiceProfileRegion": voiceProfileRegion,
       "voiceProfileDigitMap": voiceProfileDigitMap,
       "voiceProfileDigitMapEnable": voiceProfileDigitMapEnable,
       "voiceProfileStunEnable": voiceProfileStunEnable,
       "voiceProfileStunServer": voiceProfileStunServer,
       "voiceProfileStunServerPort": voiceProfileStunServerPort,
       "voiceProfileLogServer": voiceProfileLogServer,
       "voiceProfileLogServerPort": voiceProfileLogServerPort,
       "voiceProfileSpNum": voiceProfileSpNum,
       "voiceProfileV18Support": voiceProfileV18Support,
       "voiceProfileSwitchType": voiceProfileSwitchType,
       "voiceProfileServiceProviderTable": voiceProfileServiceProviderTable,
       "voiceProfileServiceProviderEntry": voiceProfileServiceProviderEntry,
       "voiceProfileServiceProviderName": voiceProfileServiceProviderName,
       "voiceProfileSIPTable": voiceProfileSIPTable,
       "voiceProfileSIPEntry": voiceProfileSIPEntry,
       "voiceProfileSIPProxyServer": voiceProfileSIPProxyServer,
       "voiceProfileSIPProxyServerPort": voiceProfileSIPProxyServerPort,
       "voiceProfileSIPProxyServerTransport": voiceProfileSIPProxyServerTransport,
       "voiceProfileSIPRegistrarServer": voiceProfileSIPRegistrarServer,
       "voiceProfileSIPRegistrarServerPort": voiceProfileSIPRegistrarServerPort,
       "voiceProfileSIPRegistrarServerTransport": voiceProfileSIPRegistrarServerTransport,
       "voiceProfileSIPToTagMatching": voiceProfileSIPToTagMatching,
       "voiceProfileSIPMusicServer": voiceProfileSIPMusicServer,
       "voiceProfileSIPMusicServerPort": voiceProfileSIPMusicServerPort,
       "voiceProfileSIPPlarGateway": voiceProfileSIPPlarGateway,
       "voiceProfileSIPPlarPort": voiceProfileSIPPlarPort,
       "voiceProfileSIPUserAgentDomain": voiceProfileSIPUserAgentDomain,
       "voiceProfileSIPUserAgentPort": voiceProfileSIPUserAgentPort,
       "voiceProfileSIPUserAgentTransport": voiceProfileSIPUserAgentTransport,
       "voiceProfileSIPOutboundProxy": voiceProfileSIPOutboundProxy,
       "voiceProfileSIPOutboundProxyPort": voiceProfileSIPOutboundProxyPort,
       "voiceProfileSIPOrganization": voiceProfileSIPOrganization,
       "voiceProfileSIPRegistrationPeriod": voiceProfileSIPRegistrationPeriod,
       "voiceProfileSIPRegisterExpires": voiceProfileSIPRegisterExpires,
       "voiceProfileSIPRegisterRetryInterval": voiceProfileSIPRegisterRetryInterval,
       "voiceProfileSIPDSCPMark": voiceProfileSIPDSCPMark,
       "voiceProfileSIPVLANIDMark": voiceProfileSIPVLANIDMark,
       "voiceProfileSIPEthernetPriorityMark": voiceProfileSIPEthernetPriorityMark,
       "voiceProfileSIPInterdigitTimeout": voiceProfileSIPInterdigitTimeout,
       "voiceProfileSIPAddressMode": voiceProfileSIPAddressMode,
       "voiceProfileSIPEventSubscribeTable": voiceProfileSIPEventSubscribeTable,
       "voiceProfileSIPEventSubscribeEntry": voiceProfileSIPEventSubscribeEntry,
       "voiceProfileSIPEventSubscribeEvent": voiceProfileSIPEventSubscribeEvent,
       "voiceProfileSIPEventSubscribeNotifier": voiceProfileSIPEventSubscribeNotifier,
       "voiceProfileSIPEventSubscribeNotifierPort": voiceProfileSIPEventSubscribeNotifierPort,
       "voiceProfileSIPEventSubscribeNotifierTransport": voiceProfileSIPEventSubscribeNotifierTransport,
       "voiceProfileMGCPTable": voiceProfileMGCPTable,
       "voiceProfileMGCPEntry": voiceProfileMGCPEntry,
       "voiceProfileMGCPCallAgent1": voiceProfileMGCPCallAgent1,
       "voiceProfileMGCPUser": voiceProfileMGCPUser,
       "voiceProfilePersistentNotify": voiceProfilePersistentNotify,
       "voiceProfileMGCPAddressMode": voiceProfileMGCPAddressMode,
       "voiceProfileRTPTable": voiceProfileRTPTable,
       "voiceProfileRTPEntry": voiceProfileRTPEntry,
       "voiceProfileRTPLocalPortMin": voiceProfileRTPLocalPortMin,
       "voiceProfileRTPLocalPortMax": voiceProfileRTPLocalPortMax,
       "voiceProfileRTPDSCPMark": voiceProfileRTPDSCPMark,
       "voiceProfileRTPTelephoneEventPayloadType": voiceProfileRTPTelephoneEventPayloadType,
       "voiceProfileFaxT38Table": voiceProfileFaxT38Table,
       "voiceProfileFaxT38Entry": voiceProfileFaxT38Entry,
       "voiceProfileFaxT38Enable": voiceProfileFaxT38Enable,
       "voiceProfileFaxT38BitRate": voiceProfileFaxT38BitRate,
       "voiceProfileFaxT38HighSpeedPacketRate": voiceProfileFaxT38HighSpeedPacketRate,
       "voiceProfileLines": voiceProfileLines,
       "voiceProfileLineTable": voiceProfileLineTable,
       "voiceProfileLineEntry": voiceProfileLineEntry,
       "voiceProfileLineIndex": voiceProfileLineIndex,
       "voiceProfileLineEnable": voiceProfileLineEnable,
       "voiceProfileLineDirectoryNumber": voiceProfileLineDirectoryNumber,
       "voiceProfileLineStatus": voiceProfileLineStatus,
       "voiceProfileLineCallState": voiceProfileLineCallState,
       "voiceProfileLinePhyReferenceList": voiceProfileLinePhyReferenceList,
       "voiceProfileLineCMAcntNum": voiceProfileLineCMAcntNum,
       "voiceProfileLineOnhook": voiceProfileLineOnhook,
       "voiceProfileLineRowStatus": voiceProfileLineRowStatus,
       "voiceProfileLineSIPTable": voiceProfileLineSIPTable,
       "voiceProfileLineSIPEntry": voiceProfileLineSIPEntry,
       "voiceProfileLineSIPAuthUserName": voiceProfileLineSIPAuthUserName,
       "voiceProfileLineSIPAuthPassword": voiceProfileLineSIPAuthPassword,
       "voiceProfileLineSIPURI": voiceProfileLineSIPURI,
       "voiceProfileLineSIPPlarUserName": voiceProfileLineSIPPlarUserName,
       "voiceProfileLineMGCPTable": voiceProfileLineMGCPTable,
       "voiceProfileLineMGCPEntry": voiceProfileLineMGCPEntry,
       "voiceProfileLineMGCPLineName": voiceProfileLineMGCPLineName,
       "voiceProfileLineProcessingTable": voiceProfileLineProcessingTable,
       "voiceProfileLineProcessingEntry": voiceProfileLineProcessingEntry,
       "voiceProfileLineTransmitGain": voiceProfileLineTransmitGain,
       "voiceProfileLineReceiveGain": voiceProfileLineReceiveGain,
       "voiceProfileLineEchoCancellationEnable": voiceProfileLineEchoCancellationEnable,
       "voiceProfileLineEchoCancellationInUse": voiceProfileLineEchoCancellationInUse,
       "voiceProfileLineCodecTable": voiceProfileLineCodecTable,
       "voiceProfileLineCodecEntry": voiceProfileLineCodecEntry,
       "voiceProfileLineCodecIndex": voiceProfileLineCodecIndex,
       "voiceProfileLineCodecEntryID": voiceProfileLineCodecEntryID,
       "voiceProfileLineCodec": voiceProfileLineCodec,
       "voiceProfileLineCodecBitRate": voiceProfileLineCodecBitRate,
       "voiceProfileLineCodecPacketizationPeriod": voiceProfileLineCodecPacketizationPeriod,
       "voiceProfileLineCodecSilenceSuppression": voiceProfileLineCodecSilenceSuppression,
       "voiceProfileLineCodecEnable": voiceProfileLineCodecEnable,
       "voiceProfileLineCodecPriority": voiceProfileLineCodecPriority,
       "voiceProfileLineCallingFeaturesTable": voiceProfileLineCallingFeaturesTable,
       "voiceProfileLineCallingFeaturesEntry": voiceProfileLineCallingFeaturesEntry,
       "voiceProfileLineCallingFeatureCallerIDEnable": voiceProfileLineCallingFeatureCallerIDEnable,
       "voiceProfileLineCallingFeatureCallerIDName": voiceProfileLineCallingFeatureCallerIDName,
       "voiceProfileLineCallingFeatureCallWaitingEnable": voiceProfileLineCallingFeatureCallWaitingEnable,
       "voiceProfileLineCallingFeatureMaxSessions": voiceProfileLineCallingFeatureMaxSessions,
       "voiceProfileLineCallingFeatureMWIEnable": voiceProfileLineCallingFeatureMWIEnable,
       "voiceProfileLineStatsTable": voiceProfileLineStatsTable,
       "voiceProfileLineStatsEntry": voiceProfileLineStatsEntry,
       "voiceProfileLineStatsPacketsSent": voiceProfileLineStatsPacketsSent,
       "voiceProfileLineStatsPacketsReceived": voiceProfileLineStatsPacketsReceived,
       "voiceProfileLineStatsBytesSent": voiceProfileLineStatsBytesSent,
       "voiceProfileLineStatsBytesReceived": voiceProfileLineStatsBytesReceived,
       "voiceProfileLineStatsPacketsLost": voiceProfileLineStatsPacketsLost,
       "voiceProfileLineStatsIncomingCallsReceived": voiceProfileLineStatsIncomingCallsReceived,
       "voiceProfileLineStatsIncomingCallsAnswered": voiceProfileLineStatsIncomingCallsAnswered,
       "voiceProfileLineStatsIncomingCallsConnected": voiceProfileLineStatsIncomingCallsConnected,
       "voiceProfileLineStatsIncomingCallsFailed": voiceProfileLineStatsIncomingCallsFailed,
       "voiceProfileLineStatsOutgoingCallsAttempted": voiceProfileLineStatsOutgoingCallsAttempted,
       "voiceProfileLineStatsOutgoingCallsAnswered": voiceProfileLineStatsOutgoingCallsAnswered,
       "voiceProfileLineStatsOutgoingCallsConnected": voiceProfileLineStatsOutgoingCallsConnected,
       "voiceProfileLineStatsOutgoingCallsFailed": voiceProfileLineStatsOutgoingCallsFailed,
       "zhnVoiceConformance": zhnVoiceConformance,
       "zhnVoiceGroups": zhnVoiceGroups,
       "zhnVoiceServiceGroup": zhnVoiceServiceGroup,
       "zhnVoiceCapabilitiesGroup": zhnVoiceCapabilitiesGroup,
       "zhnVoiceCapabilitiesSIPGroup": zhnVoiceCapabilitiesSIPGroup,
       "zhnVoiceCapabilitiesMGCPGroup": zhnVoiceCapabilitiesMGCPGroup,
       "zhnVoiceCapabilitiesCodecsGroup": zhnVoiceCapabilitiesCodecsGroup,
       "zhnVoiceProfileGroup": zhnVoiceProfileGroup,
       "zhnVoiceProfileServiceProviderGroup": zhnVoiceProfileServiceProviderGroup,
       "zhnVoiceProfileSIPGroup": zhnVoiceProfileSIPGroup,
       "zhnVoiceProfileSIPEventSubscribeGroup": zhnVoiceProfileSIPEventSubscribeGroup,
       "zhnVoiceProfileMGCPEntry": zhnVoiceProfileMGCPEntry,
       "zhnVoiceProfileRTPEntry": zhnVoiceProfileRTPEntry,
       "zhnVoiceProfileFaxT38Entry": zhnVoiceProfileFaxT38Entry,
       "zhnVoiceProfileLineGroup": zhnVoiceProfileLineGroup,
       "zhnVoiceProfileLineProcessingGroup": zhnVoiceProfileLineProcessingGroup,
       "zhnVoiceProfileLineSIPGroup": zhnVoiceProfileLineSIPGroup,
       "zhnVoiceProfileLineMGCPGroup": zhnVoiceProfileLineMGCPGroup,
       "zhnVoiceProfileLineCodecsGroup": zhnVoiceProfileLineCodecsGroup,
       "zhnVoiceLineCallingFeaturesGroup": zhnVoiceLineCallingFeaturesGroup,
       "zhnVoiceNotificationGroup": zhnVoiceNotificationGroup,
       "zhnVoiceProfileLineStatsGroup": zhnVoiceProfileLineStatsGroup,
       "zhnVoiceCompliances": zhnVoiceCompliances,
       "zhnVoiceCompliance": zhnVoiceCompliance}
)
