# SNMP MIB module (WLSX-VOICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WLSX-VOICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:18 2024
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

(ArubaCallStates,
 ArubaEnableValue,
 ArubaVlanValidRange,
 ArubaVoiceCacBit,
 ArubaVoiceCdrDirection,
 ArubaVoipProtocol,
 ArubaVoipRegState) = mibBuilder.importSymbols(
    "ARUBA-TC",
    "ArubaCallStates",
    "ArubaEnableValue",
    "ArubaVlanValidRange",
    "ArubaVoiceCacBit",
    "ArubaVoiceCdrDirection",
    "ArubaVoipProtocol",
    "ArubaVoipRegState")

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
 TextualConvention,
 TimeTicks,
 Unsigned32,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "TextualConvention",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "snmpModules")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")

(wlanAPBSSID,
 wlanAPMacAddress,
 wlanAPRadioNumber,
 wlanStaPhyAddress) = mibBuilder.importSymbols(
    "WLSX-WLAN-MIB",
    "wlanAPBSSID",
    "wlanAPMacAddress",
    "wlanAPRadioNumber",
    "wlanStaPhyAddress")


# MODULE-IDENTITY

wlsxVoiceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12)
)
wlsxVoiceMIB.setRevisions(
        ("1908-04-16 02:06",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxVoiceStatsGroup_ObjectIdentity = ObjectIdentity
wlsxVoiceStatsGroup = _WlsxVoiceStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1)
)
_WlsxVoiceCdrInfoGroup_ObjectIdentity = ObjectIdentity
wlsxVoiceCdrInfoGroup = _WlsxVoiceCdrInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1)
)
_WlsxVoiceCdrTotal_Type = Unsigned32
_WlsxVoiceCdrTotal_Object = MibScalar
wlsxVoiceCdrTotal = _WlsxVoiceCdrTotal_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 1),
    _WlsxVoiceCdrTotal_Type()
)
wlsxVoiceCdrTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxVoiceCdrTotal.setStatus("current")
_WlsxVoiceCdrTable_Object = MibTable
wlsxVoiceCdrTable = _WlsxVoiceCdrTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wlsxVoiceCdrTable.setStatus("current")
_WlsxVoiceCdrEntry_Object = MibTableRow
wlsxVoiceCdrEntry = _WlsxVoiceCdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1)
)
wlsxVoiceCdrEntry.setIndexNames(
    (0, "WLSX-VOICE-MIB", "voiceCdrId"),
)
if mibBuilder.loadTexts:
    wlsxVoiceCdrEntry.setStatus("current")
_VoiceCdrId_Type = Unsigned32
_VoiceCdrId_Object = MibTableColumn
voiceCdrId = _VoiceCdrId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 1),
    _VoiceCdrId_Type()
)
voiceCdrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voiceCdrId.setStatus("current")
_VoiceCdrIp_Type = IpAddress
_VoiceCdrIp_Object = MibTableColumn
voiceCdrIp = _VoiceCdrIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 2),
    _VoiceCdrIp_Type()
)
voiceCdrIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrIp.setStatus("current")
_VoiceCdrMac_Type = MacAddress
_VoiceCdrMac_Object = MibTableColumn
voiceCdrMac = _VoiceCdrMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 3),
    _VoiceCdrMac_Type()
)
voiceCdrMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrMac.setStatus("current")
_VoiceCdrName_Type = DisplayString
_VoiceCdrName_Object = MibTableColumn
voiceCdrName = _VoiceCdrName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 4),
    _VoiceCdrName_Type()
)
voiceCdrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrName.setStatus("current")
_VoiceCdrDialNum_Type = DisplayString
_VoiceCdrDialNum_Object = MibTableColumn
voiceCdrDialNum = _VoiceCdrDialNum_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 5),
    _VoiceCdrDialNum_Type()
)
voiceCdrDialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrDialNum.setStatus("current")
_VoiceCdrDir_Type = ArubaVoiceCdrDirection
_VoiceCdrDir_Object = MibTableColumn
voiceCdrDir = _VoiceCdrDir_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 6),
    _VoiceCdrDir_Type()
)
voiceCdrDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrDir.setStatus("current")
_VoiceCdrOrigTime_Type = Unsigned32
_VoiceCdrOrigTime_Object = MibTableColumn
voiceCdrOrigTime = _VoiceCdrOrigTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 7),
    _VoiceCdrOrigTime_Type()
)
voiceCdrOrigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrOrigTime.setStatus("current")
_VoiceCdrSetupTime_Type = Unsigned32
_VoiceCdrSetupTime_Object = MibTableColumn
voiceCdrSetupTime = _VoiceCdrSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 8),
    _VoiceCdrSetupTime_Type()
)
voiceCdrSetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrSetupTime.setStatus("current")
_VoiceCdrTeardownTime_Type = Unsigned32
_VoiceCdrTeardownTime_Object = MibTableColumn
voiceCdrTeardownTime = _VoiceCdrTeardownTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 9),
    _VoiceCdrTeardownTime_Type()
)
voiceCdrTeardownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrTeardownTime.setStatus("deprecated")
_VoiceCdrStatus_Type = ArubaCallStates
_VoiceCdrStatus_Object = MibTableColumn
voiceCdrStatus = _VoiceCdrStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 10),
    _VoiceCdrStatus_Type()
)
voiceCdrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrStatus.setStatus("current")
_VoiceCdrReason_Type = DisplayString
_VoiceCdrReason_Object = MibTableColumn
voiceCdrReason = _VoiceCdrReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 11),
    _VoiceCdrReason_Type()
)
voiceCdrReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrReason.setStatus("current")
_VoiceCdrDuration_Type = Integer32
_VoiceCdrDuration_Object = MibTableColumn
voiceCdrDuration = _VoiceCdrDuration_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 12),
    _VoiceCdrDuration_Type()
)
voiceCdrDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrDuration.setStatus("current")
_VoiceCdrRValue_Type = Integer32
_VoiceCdrRValue_Object = MibTableColumn
voiceCdrRValue = _VoiceCdrRValue_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 13),
    _VoiceCdrRValue_Type()
)
voiceCdrRValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrRValue.setStatus("current")
_VoiceCdrApSwitchDelay_Type = Integer32
_VoiceCdrApSwitchDelay_Object = MibTableColumn
voiceCdrApSwitchDelay = _VoiceCdrApSwitchDelay_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 14),
    _VoiceCdrApSwitchDelay_Type()
)
voiceCdrApSwitchDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrApSwitchDelay.setStatus("current")
_VoiceCdrCodec_Type = Integer32
_VoiceCdrCodec_Object = MibTableColumn
voiceCdrCodec = _VoiceCdrCodec_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 15),
    _VoiceCdrCodec_Type()
)
voiceCdrCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrCodec.setStatus("current")
_VoiceCdrApName_Type = DisplayString
_VoiceCdrApName_Object = MibTableColumn
voiceCdrApName = _VoiceCdrApName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 16),
    _VoiceCdrApName_Type()
)
voiceCdrApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrApName.setStatus("current")
_VoiceCdrApMac_Type = MacAddress
_VoiceCdrApMac_Object = MibTableColumn
voiceCdrApMac = _VoiceCdrApMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 17),
    _VoiceCdrApMac_Type()
)
voiceCdrApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrApMac.setStatus("current")
_VoiceCdrBssid_Type = DisplayString
_VoiceCdrBssid_Object = MibTableColumn
voiceCdrBssid = _VoiceCdrBssid_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 18),
    _VoiceCdrBssid_Type()
)
voiceCdrBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrBssid.setStatus("current")
_VoiceCdrEssid_Type = DisplayString
_VoiceCdrEssid_Object = MibTableColumn
voiceCdrEssid = _VoiceCdrEssid_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 19),
    _VoiceCdrEssid_Type()
)
voiceCdrEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrEssid.setStatus("current")
_VoiceCdrHandovers_Type = Integer32
_VoiceCdrHandovers_Object = MibTableColumn
voiceCdrHandovers = _VoiceCdrHandovers_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 20),
    _VoiceCdrHandovers_Type()
)
voiceCdrHandovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrHandovers.setStatus("current")
_VoiceCdrMOS_Type = Integer32
_VoiceCdrMOS_Object = MibTableColumn
voiceCdrMOS = _VoiceCdrMOS_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 21),
    _VoiceCdrMOS_Type()
)
voiceCdrMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCdrMOS.setStatus("deprecated")
_WlsxVoiceCallCtrsGroup_ObjectIdentity = ObjectIdentity
wlsxVoiceCallCtrsGroup = _WlsxVoiceCallCtrsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2)
)
_VoiceCallCtrsTotal_Type = Unsigned32
_VoiceCallCtrsTotal_Object = MibScalar
voiceCallCtrsTotal = _VoiceCallCtrsTotal_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 1),
    _VoiceCallCtrsTotal_Type()
)
voiceCallCtrsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsTotal.setStatus("current")
_VoiceCallCtrsSuccess_Type = Unsigned32
_VoiceCallCtrsSuccess_Object = MibScalar
voiceCallCtrsSuccess = _VoiceCallCtrsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 2),
    _VoiceCallCtrsSuccess_Type()
)
voiceCallCtrsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsSuccess.setStatus("current")
_VoiceCallCtrsFailed_Type = Unsigned32
_VoiceCallCtrsFailed_Object = MibScalar
voiceCallCtrsFailed = _VoiceCallCtrsFailed_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 3),
    _VoiceCallCtrsFailed_Type()
)
voiceCallCtrsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsFailed.setStatus("current")
_VoiceCallCtrsRejected_Type = Unsigned32
_VoiceCallCtrsRejected_Object = MibScalar
voiceCallCtrsRejected = _VoiceCallCtrsRejected_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 4),
    _VoiceCallCtrsRejected_Type()
)
voiceCallCtrsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsRejected.setStatus("current")
_VoiceCallCtrsAborted_Type = Unsigned32
_VoiceCallCtrsAborted_Object = MibScalar
voiceCallCtrsAborted = _VoiceCallCtrsAborted_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 5),
    _VoiceCallCtrsAborted_Type()
)
voiceCallCtrsAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsAborted.setStatus("current")
_VoiceCallCtrsOrig_Type = Unsigned32
_VoiceCallCtrsOrig_Object = MibScalar
voiceCallCtrsOrig = _VoiceCallCtrsOrig_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 6),
    _VoiceCallCtrsOrig_Type()
)
voiceCallCtrsOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsOrig.setStatus("current")
_VoiceCallCtrsRecvd_Type = Unsigned32
_VoiceCallCtrsRecvd_Object = MibScalar
voiceCallCtrsRecvd = _VoiceCallCtrsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 7),
    _VoiceCallCtrsRecvd_Type()
)
voiceCallCtrsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsRecvd.setStatus("current")
_VoiceCallCtrsActive_Type = Unsigned32
_VoiceCallCtrsActive_Object = MibScalar
voiceCallCtrsActive = _VoiceCallCtrsActive_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 8),
    _VoiceCallCtrsActive_Type()
)
voiceCallCtrsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsActive.setStatus("current")
_VoiceCallCtrsNotFnd_Type = Unsigned32
_VoiceCallCtrsNotFnd_Object = MibScalar
voiceCallCtrsNotFnd = _VoiceCallCtrsNotFnd_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 9),
    _VoiceCallCtrsNotFnd_Type()
)
voiceCallCtrsNotFnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsNotFnd.setStatus("deprecated")
_VoiceCallCtrsBusy_Type = Unsigned32
_VoiceCallCtrsBusy_Object = MibScalar
voiceCallCtrsBusy = _VoiceCallCtrsBusy_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 10),
    _VoiceCallCtrsBusy_Type()
)
voiceCallCtrsBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsBusy.setStatus("deprecated")
_VoiceCallCtrsSvc_Type = Unsigned32
_VoiceCallCtrsSvc_Object = MibScalar
voiceCallCtrsSvc = _VoiceCallCtrsSvc_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 11),
    _VoiceCallCtrsSvc_Type()
)
voiceCallCtrsSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsSvc.setStatus("deprecated")
_VoiceCallCtrsReqTerm_Type = Unsigned32
_VoiceCallCtrsReqTerm_Object = MibScalar
voiceCallCtrsReqTerm = _VoiceCallCtrsReqTerm_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 12),
    _VoiceCallCtrsReqTerm_Type()
)
voiceCallCtrsReqTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsReqTerm.setStatus("deprecated")
_VoiceCallCtrsDecline_Type = Unsigned32
_VoiceCallCtrsDecline_Object = MibScalar
voiceCallCtrsDecline = _VoiceCallCtrsDecline_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 13),
    _VoiceCallCtrsDecline_Type()
)
voiceCallCtrsDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsDecline.setStatus("deprecated")
_VoiceCallCtrsUnauth_Type = Unsigned32
_VoiceCallCtrsUnauth_Object = MibScalar
voiceCallCtrsUnauth = _VoiceCallCtrsUnauth_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 14),
    _VoiceCallCtrsUnauth_Type()
)
voiceCallCtrsUnauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsUnauth.setStatus("deprecated")
_VoiceCallCtrsMisc_Type = Unsigned32
_VoiceCallCtrsMisc_Object = MibScalar
voiceCallCtrsMisc = _VoiceCallCtrsMisc_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 15),
    _VoiceCallCtrsMisc_Type()
)
voiceCallCtrsMisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceCallCtrsMisc.setStatus("deprecated")
_WlsxVoiceClientInfoGroup_ObjectIdentity = ObjectIdentity
wlsxVoiceClientInfoGroup = _WlsxVoiceClientInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3)
)
_WlsxVoiceClientTotal_Type = Unsigned32
_WlsxVoiceClientTotal_Object = MibScalar
wlsxVoiceClientTotal = _WlsxVoiceClientTotal_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 1),
    _WlsxVoiceClientTotal_Type()
)
wlsxVoiceClientTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxVoiceClientTotal.setStatus("current")
_WlsxVoiceClientTable_Object = MibTable
wlsxVoiceClientTable = _WlsxVoiceClientTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wlsxVoiceClientTable.setStatus("current")
_WlsxVoiceClientEntry_Object = MibTableRow
wlsxVoiceClientEntry = _WlsxVoiceClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1)
)
wlsxVoiceClientEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanStaPhyAddress"),
)
if mibBuilder.loadTexts:
    wlsxVoiceClientEntry.setStatus("current")
_VoiceClientIp_Type = IpAddress
_VoiceClientIp_Object = MibTableColumn
voiceClientIp = _VoiceClientIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 1),
    _VoiceClientIp_Type()
)
voiceClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientIp.setStatus("current")
_VoiceClientProtocol_Type = ArubaVoipProtocol
_VoiceClientProtocol_Object = MibTableColumn
voiceClientProtocol = _VoiceClientProtocol_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 2),
    _VoiceClientProtocol_Type()
)
voiceClientProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientProtocol.setStatus("current")
_VoiceClientRegState_Type = ArubaVoipRegState
_VoiceClientRegState_Object = MibTableColumn
voiceClientRegState = _VoiceClientRegState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 3),
    _VoiceClientRegState_Type()
)
voiceClientRegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientRegState.setStatus("current")
_VoiceClientContactName_Type = DisplayString
_VoiceClientContactName_Object = MibTableColumn
voiceClientContactName = _VoiceClientContactName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 4),
    _VoiceClientContactName_Type()
)
voiceClientContactName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientContactName.setStatus("current")
_VoiceClientServerName_Type = DisplayString
_VoiceClientServerName_Object = MibTableColumn
voiceClientServerName = _VoiceClientServerName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 5),
    _VoiceClientServerName_Type()
)
voiceClientServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientServerName.setStatus("current")
_VoiceClientEssid_Type = DisplayString
_VoiceClientEssid_Object = MibTableColumn
voiceClientEssid = _VoiceClientEssid_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 6),
    _VoiceClientEssid_Type()
)
voiceClientEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientEssid.setStatus("current")
_VoiceClientVlanId_Type = ArubaVlanValidRange
_VoiceClientVlanId_Object = MibTableColumn
voiceClientVlanId = _VoiceClientVlanId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 7),
    _VoiceClientVlanId_Type()
)
voiceClientVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientVlanId.setStatus("current")
_VoiceClientTunnelId_Type = Integer32
_VoiceClientTunnelId_Object = MibTableColumn
voiceClientTunnelId = _VoiceClientTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 8),
    _VoiceClientTunnelId_Type()
)
voiceClientTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceClientTunnelId.setStatus("current")
_WlsxVoiceAPBssidInfoGroup_ObjectIdentity = ObjectIdentity
wlsxVoiceAPBssidInfoGroup = _WlsxVoiceAPBssidInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4)
)
_WlsxVoiceAPBssidTotal_Type = Unsigned32
_WlsxVoiceAPBssidTotal_Object = MibScalar
wlsxVoiceAPBssidTotal = _WlsxVoiceAPBssidTotal_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 1),
    _WlsxVoiceAPBssidTotal_Type()
)
wlsxVoiceAPBssidTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxVoiceAPBssidTotal.setStatus("current")
_WlsxVoiceAPBssidTable_Object = MibTable
wlsxVoiceAPBssidTable = _WlsxVoiceAPBssidTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2)
)
if mibBuilder.loadTexts:
    wlsxVoiceAPBssidTable.setStatus("current")
_WlsxVoiceAPBssidEntry_Object = MibTableRow
wlsxVoiceAPBssidEntry = _WlsxVoiceAPBssidEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1)
)
wlsxVoiceAPBssidEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanAPMacAddress"),
    (0, "WLSX-WLAN-MIB", "wlanAPRadioNumber"),
    (0, "WLSX-WLAN-MIB", "wlanAPBSSID"),
)
if mibBuilder.loadTexts:
    wlsxVoiceAPBssidEntry.setStatus("current")
_VoiceAPBssidName_Type = DisplayString
_VoiceAPBssidName_Object = MibTableColumn
voiceAPBssidName = _VoiceAPBssidName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 1),
    _VoiceAPBssidName_Type()
)
voiceAPBssidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidName.setStatus("current")
_VoiceAPBssidGroup_Type = DisplayString
_VoiceAPBssidGroup_Object = MibTableColumn
voiceAPBssidGroup = _VoiceAPBssidGroup_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 2),
    _VoiceAPBssidGroup_Type()
)
voiceAPBssidGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidGroup.setStatus("current")
_VoiceAPBssidIp_Type = IpAddress
_VoiceAPBssidIp_Object = MibTableColumn
voiceAPBssidIp = _VoiceAPBssidIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 3),
    _VoiceAPBssidIp_Type()
)
voiceAPBssidIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidIp.setStatus("current")
_VoiceAPBssidTotCalls_Type = Unsigned32
_VoiceAPBssidTotCalls_Object = MibTableColumn
voiceAPBssidTotCalls = _VoiceAPBssidTotCalls_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 4),
    _VoiceAPBssidTotCalls_Type()
)
voiceAPBssidTotCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidTotCalls.setStatus("current")
_VoiceAPBssidVoiceType_Type = DisplayString
_VoiceAPBssidVoiceType_Object = MibTableColumn
voiceAPBssidVoiceType = _VoiceAPBssidVoiceType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 5),
    _VoiceAPBssidVoiceType_Type()
)
voiceAPBssidVoiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidVoiceType.setStatus("current")


class _VoiceAPBssidFlag_Type(Bits):
    """Custom type voiceAPBssidFlag based on Bits"""
    namedValues = NamedValues(
        *(("apActiveLoadBalancing", 4),
          ("apBatteryBoost", 6),
          ("apDisconnectExtraCalls", 5),
          ("apEnet1Mode", 3),
          ("apPPPOE", 1),
          ("apRemoteAP", 0),
          ("apWiredApEnabled", 2))
    )

_VoiceAPBssidFlag_Type.__name__ = "Bits"
_VoiceAPBssidFlag_Object = MibTableColumn
voiceAPBssidFlag = _VoiceAPBssidFlag_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 6),
    _VoiceAPBssidFlag_Type()
)
voiceAPBssidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidFlag.setStatus("current")
_VoiceAPBssidUpTime_Type = TimeTicks
_VoiceAPBssidUpTime_Object = MibTableColumn
voiceAPBssidUpTime = _VoiceAPBssidUpTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 7),
    _VoiceAPBssidUpTime_Type()
)
voiceAPBssidUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidUpTime.setStatus("current")
_VoiceAPBssid100Sent_Type = Counter32
_VoiceAPBssid100Sent_Object = MibTableColumn
voiceAPBssid100Sent = _VoiceAPBssid100Sent_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 8),
    _VoiceAPBssid100Sent_Type()
)
voiceAPBssid100Sent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssid100Sent.setStatus("current")
_VoiceAPBssid503Sent_Type = Counter32
_VoiceAPBssid503Sent_Object = MibTableColumn
voiceAPBssid503Sent = _VoiceAPBssid503Sent_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 9),
    _VoiceAPBssid503Sent_Type()
)
voiceAPBssid503Sent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssid503Sent.setStatus("current")
_VoiceAPBssidExtraCallDisc_Type = Counter32
_VoiceAPBssidExtraCallDisc_Object = MibTableColumn
voiceAPBssidExtraCallDisc = _VoiceAPBssidExtraCallDisc_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 10),
    _VoiceAPBssidExtraCallDisc_Type()
)
voiceAPBssidExtraCallDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidExtraCallDisc.setStatus("current")
_VoiceAPBssidKickedOff_Type = Counter32
_VoiceAPBssidKickedOff_Object = MibTableColumn
voiceAPBssidKickedOff = _VoiceAPBssidKickedOff_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 11),
    _VoiceAPBssidKickedOff_Type()
)
voiceAPBssidKickedOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidKickedOff.setStatus("deprecated")
_VoiceAPBssidTspecDenied_Type = Counter32
_VoiceAPBssidTspecDenied_Object = MibTableColumn
voiceAPBssidTspecDenied = _VoiceAPBssidTspecDenied_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 12),
    _VoiceAPBssidTspecDenied_Type()
)
voiceAPBssidTspecDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidTspecDenied.setStatus("current")
_VoiceAPBssidCacFlag_Type = ArubaVoiceCacBit
_VoiceAPBssidCacFlag_Object = MibTableColumn
voiceAPBssidCacFlag = _VoiceAPBssidCacFlag_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 13),
    _VoiceAPBssidCacFlag_Type()
)
voiceAPBssidCacFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidCacFlag.setStatus("current")
_VoiceAPBssidTotVoiceClients_Type = Unsigned32
_VoiceAPBssidTotVoiceClients_Object = MibTableColumn
voiceAPBssidTotVoiceClients = _VoiceAPBssidTotVoiceClients_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 14),
    _VoiceAPBssidTotVoiceClients_Type()
)
voiceAPBssidTotVoiceClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidTotVoiceClients.setStatus("current")
_VoiceAPBssidCallsSCCP_Type = Unsigned32
_VoiceAPBssidCallsSCCP_Object = MibTableColumn
voiceAPBssidCallsSCCP = _VoiceAPBssidCallsSCCP_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 15),
    _VoiceAPBssidCallsSCCP_Type()
)
voiceAPBssidCallsSCCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidCallsSCCP.setStatus("current")
_VoiceAPBssidCallsSIP_Type = Unsigned32
_VoiceAPBssidCallsSIP_Object = MibTableColumn
voiceAPBssidCallsSIP = _VoiceAPBssidCallsSIP_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 16),
    _VoiceAPBssidCallsSIP_Type()
)
voiceAPBssidCallsSIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidCallsSIP.setStatus("current")
_VoiceAPBssidCallsSVP_Type = Unsigned32
_VoiceAPBssidCallsSVP_Object = MibTableColumn
voiceAPBssidCallsSVP = _VoiceAPBssidCallsSVP_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 17),
    _VoiceAPBssidCallsSVP_Type()
)
voiceAPBssidCallsSVP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidCallsSVP.setStatus("current")
_VoiceAPBssidCallsVocera_Type = Unsigned32
_VoiceAPBssidCallsVocera_Object = MibTableColumn
voiceAPBssidCallsVocera = _VoiceAPBssidCallsVocera_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 18),
    _VoiceAPBssidCallsVocera_Type()
)
voiceAPBssidCallsVocera.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidCallsVocera.setStatus("current")
_VoiceAPBssidCallsNoe_Type = Unsigned32
_VoiceAPBssidCallsNoe_Object = MibTableColumn
voiceAPBssidCallsNoe = _VoiceAPBssidCallsNoe_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 19),
    _VoiceAPBssidCallsNoe_Type()
)
voiceAPBssidCallsNoe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidCallsNoe.setStatus("current")
_VoiceAPBssidEssid_Type = DisplayString
_VoiceAPBssidEssid_Object = MibTableColumn
voiceAPBssidEssid = _VoiceAPBssidEssid_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 20),
    _VoiceAPBssidEssid_Type()
)
voiceAPBssidEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceAPBssidEssid.setStatus("current")
_WlsxVoiceClientLocationInfoGroup_ObjectIdentity = ObjectIdentity
wlsxVoiceClientLocationInfoGroup = _WlsxVoiceClientLocationInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5)
)
_WlsxVoiceClientLocationTotal_Type = Unsigned32
_WlsxVoiceClientLocationTotal_Object = MibScalar
wlsxVoiceClientLocationTotal = _WlsxVoiceClientLocationTotal_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 1),
    _WlsxVoiceClientLocationTotal_Type()
)
wlsxVoiceClientLocationTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxVoiceClientLocationTotal.setStatus("current")
_WlsxVoiceClientLocationTable_Object = MibTable
wlsxVoiceClientLocationTable = _WlsxVoiceClientLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wlsxVoiceClientLocationTable.setStatus("current")
_WlsxVoiceClientLocationEntry_Object = MibTableRow
wlsxVoiceClientLocationEntry = _WlsxVoiceClientLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1)
)
wlsxVoiceClientLocationEntry.setIndexNames(
    (0, "WLSX-WLAN-MIB", "wlanStaPhyAddress"),
)
if mibBuilder.loadTexts:
    wlsxVoiceClientLocationEntry.setStatus("current")
_VcLocationIp_Type = IpAddress
_VcLocationIp_Object = MibTableColumn
vcLocationIp = _VcLocationIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 1),
    _VcLocationIp_Type()
)
vcLocationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcLocationIp.setStatus("current")
_VcLocationMac_Type = MacAddress
_VcLocationMac_Object = MibTableColumn
vcLocationMac = _VcLocationMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 2),
    _VcLocationMac_Type()
)
vcLocationMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcLocationMac.setStatus("current")
_VcLocationSwitchIp_Type = IpAddress
_VcLocationSwitchIp_Object = MibTableColumn
vcLocationSwitchIp = _VcLocationSwitchIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 3),
    _VcLocationSwitchIp_Type()
)
vcLocationSwitchIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcLocationSwitchIp.setStatus("current")
_VcLocationApName_Type = DisplayString
_VcLocationApName_Object = MibTableColumn
vcLocationApName = _VcLocationApName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 4),
    _VcLocationApName_Type()
)
vcLocationApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcLocationApName.setStatus("current")
_VcLocationApMac_Type = MacAddress
_VcLocationApMac_Object = MibTableColumn
vcLocationApMac = _VcLocationApMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 5),
    _VcLocationApMac_Type()
)
vcLocationApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcLocationApMac.setStatus("current")
_VcLocationApMode_Type = Integer32
_VcLocationApMode_Object = MibTableColumn
vcLocationApMode = _VcLocationApMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 6),
    _VcLocationApMode_Type()
)
vcLocationApMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcLocationApMode.setStatus("current")
_VcLocationApLoc_Type = DisplayString
_VcLocationApLoc_Object = MibTableColumn
vcLocationApLoc = _VcLocationApLoc_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 7),
    _VcLocationApLoc_Type()
)
vcLocationApLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcLocationApLoc.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-VOICE-MIB",
    **{"wlsxVoiceMIB": wlsxVoiceMIB,
       "wlsxVoiceStatsGroup": wlsxVoiceStatsGroup,
       "wlsxVoiceCdrInfoGroup": wlsxVoiceCdrInfoGroup,
       "wlsxVoiceCdrTotal": wlsxVoiceCdrTotal,
       "wlsxVoiceCdrTable": wlsxVoiceCdrTable,
       "wlsxVoiceCdrEntry": wlsxVoiceCdrEntry,
       "voiceCdrId": voiceCdrId,
       "voiceCdrIp": voiceCdrIp,
       "voiceCdrMac": voiceCdrMac,
       "voiceCdrName": voiceCdrName,
       "voiceCdrDialNum": voiceCdrDialNum,
       "voiceCdrDir": voiceCdrDir,
       "voiceCdrOrigTime": voiceCdrOrigTime,
       "voiceCdrSetupTime": voiceCdrSetupTime,
       "voiceCdrTeardownTime": voiceCdrTeardownTime,
       "voiceCdrStatus": voiceCdrStatus,
       "voiceCdrReason": voiceCdrReason,
       "voiceCdrDuration": voiceCdrDuration,
       "voiceCdrRValue": voiceCdrRValue,
       "voiceCdrApSwitchDelay": voiceCdrApSwitchDelay,
       "voiceCdrCodec": voiceCdrCodec,
       "voiceCdrApName": voiceCdrApName,
       "voiceCdrApMac": voiceCdrApMac,
       "voiceCdrBssid": voiceCdrBssid,
       "voiceCdrEssid": voiceCdrEssid,
       "voiceCdrHandovers": voiceCdrHandovers,
       "voiceCdrMOS": voiceCdrMOS,
       "wlsxVoiceCallCtrsGroup": wlsxVoiceCallCtrsGroup,
       "voiceCallCtrsTotal": voiceCallCtrsTotal,
       "voiceCallCtrsSuccess": voiceCallCtrsSuccess,
       "voiceCallCtrsFailed": voiceCallCtrsFailed,
       "voiceCallCtrsRejected": voiceCallCtrsRejected,
       "voiceCallCtrsAborted": voiceCallCtrsAborted,
       "voiceCallCtrsOrig": voiceCallCtrsOrig,
       "voiceCallCtrsRecvd": voiceCallCtrsRecvd,
       "voiceCallCtrsActive": voiceCallCtrsActive,
       "voiceCallCtrsNotFnd": voiceCallCtrsNotFnd,
       "voiceCallCtrsBusy": voiceCallCtrsBusy,
       "voiceCallCtrsSvc": voiceCallCtrsSvc,
       "voiceCallCtrsReqTerm": voiceCallCtrsReqTerm,
       "voiceCallCtrsDecline": voiceCallCtrsDecline,
       "voiceCallCtrsUnauth": voiceCallCtrsUnauth,
       "voiceCallCtrsMisc": voiceCallCtrsMisc,
       "wlsxVoiceClientInfoGroup": wlsxVoiceClientInfoGroup,
       "wlsxVoiceClientTotal": wlsxVoiceClientTotal,
       "wlsxVoiceClientTable": wlsxVoiceClientTable,
       "wlsxVoiceClientEntry": wlsxVoiceClientEntry,
       "voiceClientIp": voiceClientIp,
       "voiceClientProtocol": voiceClientProtocol,
       "voiceClientRegState": voiceClientRegState,
       "voiceClientContactName": voiceClientContactName,
       "voiceClientServerName": voiceClientServerName,
       "voiceClientEssid": voiceClientEssid,
       "voiceClientVlanId": voiceClientVlanId,
       "voiceClientTunnelId": voiceClientTunnelId,
       "wlsxVoiceAPBssidInfoGroup": wlsxVoiceAPBssidInfoGroup,
       "wlsxVoiceAPBssidTotal": wlsxVoiceAPBssidTotal,
       "wlsxVoiceAPBssidTable": wlsxVoiceAPBssidTable,
       "wlsxVoiceAPBssidEntry": wlsxVoiceAPBssidEntry,
       "voiceAPBssidName": voiceAPBssidName,
       "voiceAPBssidGroup": voiceAPBssidGroup,
       "voiceAPBssidIp": voiceAPBssidIp,
       "voiceAPBssidTotCalls": voiceAPBssidTotCalls,
       "voiceAPBssidVoiceType": voiceAPBssidVoiceType,
       "voiceAPBssidFlag": voiceAPBssidFlag,
       "voiceAPBssidUpTime": voiceAPBssidUpTime,
       "voiceAPBssid100Sent": voiceAPBssid100Sent,
       "voiceAPBssid503Sent": voiceAPBssid503Sent,
       "voiceAPBssidExtraCallDisc": voiceAPBssidExtraCallDisc,
       "voiceAPBssidKickedOff": voiceAPBssidKickedOff,
       "voiceAPBssidTspecDenied": voiceAPBssidTspecDenied,
       "voiceAPBssidCacFlag": voiceAPBssidCacFlag,
       "voiceAPBssidTotVoiceClients": voiceAPBssidTotVoiceClients,
       "voiceAPBssidCallsSCCP": voiceAPBssidCallsSCCP,
       "voiceAPBssidCallsSIP": voiceAPBssidCallsSIP,
       "voiceAPBssidCallsSVP": voiceAPBssidCallsSVP,
       "voiceAPBssidCallsVocera": voiceAPBssidCallsVocera,
       "voiceAPBssidCallsNoe": voiceAPBssidCallsNoe,
       "voiceAPBssidEssid": voiceAPBssidEssid,
       "wlsxVoiceClientLocationInfoGroup": wlsxVoiceClientLocationInfoGroup,
       "wlsxVoiceClientLocationTotal": wlsxVoiceClientLocationTotal,
       "wlsxVoiceClientLocationTable": wlsxVoiceClientLocationTable,
       "wlsxVoiceClientLocationEntry": wlsxVoiceClientLocationEntry,
       "vcLocationIp": vcLocationIp,
       "vcLocationMac": vcLocationMac,
       "vcLocationSwitchIp": vcLocationSwitchIp,
       "vcLocationApName": vcLocationApName,
       "vcLocationApMac": vcLocationApMac,
       "vcLocationApMode": vcLocationApMode,
       "vcLocationApLoc": vcLocationApLoc}
)
