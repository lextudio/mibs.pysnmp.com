# SNMP MIB module (CISCO-LWAPP-DOT11-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-DOT11-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:18 2024
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

(cLAPGroupVlanName,
 cLApDot11IfSlotId,
 cLApDot11RadioChannelNumber,
 cLApIfLoadChannelUtilization,
 cLApLocation,
 cLApName,
 cLApSubMode) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLAPGroupVlanName",
    "cLApDot11IfSlotId",
    "cLApDot11RadioChannelNumber",
    "cLApIfLoadChannelUtilization",
    "cLApLocation",
    "cLApName",
    "cLApSubMode")

(cLMobilityExtMCClientAnchorMCGroupId,
 cLMobilityExtMCClientAnchorMCPrivateAddress,
 cLMobilityExtMCClientAnchorMCPrivateAddressType,
 cLMobilityExtMCClientAssociatedMAAddress,
 cLMobilityExtMCClientAssociatedMAAddressType,
 cLMobilityExtMCClientAssociatedMCAddress,
 cLMobilityExtMCClientAssociatedMCAddressType,
 cLMobilityExtMCClientAssociatedMCGroupId) = mibBuilder.importSymbols(
    "CISCO-LWAPP-MOBILITY-EXT-MIB",
    "cLMobilityExtMCClientAnchorMCGroupId",
    "cLMobilityExtMCClientAnchorMCPrivateAddress",
    "cLMobilityExtMCClientAnchorMCPrivateAddressType",
    "cLMobilityExtMCClientAssociatedMAAddress",
    "cLMobilityExtMCClientAssociatedMAAddressType",
    "cLMobilityExtMCClientAssociatedMCAddress",
    "cLMobilityExtMCClientAssociatedMCAddressType",
    "cLMobilityExtMCClientAssociatedMCGroupId")

(CLApIfType,
 CLClientPowerSaveMode,
 CLDot11ClientStatus,
 CcxServiceVersion) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLApIfType",
    "CLClientPowerSaveMode",
    "CLDot11ClientStatus",
    "CcxServiceVersion")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoURLStringOrEmpty,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLStringOrEmpty")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappDot11ClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599)
)
ciscoLwappDot11ClientMIB.setRevisions(
        ("2011-04-29 00:00",
         "2006-11-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappDot11ClientMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientMIBNotifs = _CiscoLwappDot11ClientMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 0)
)
_CiscoLwappDot11ClientMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientMIBObjects = _CiscoLwappDot11ClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1)
)
_CldcConfigObjects_ObjectIdentity = ObjectIdentity
cldcConfigObjects = _CldcConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 1)
)


class _CldcKeyDecryptErrorEnabled_Type(TruthValue):
    """Custom type cldcKeyDecryptErrorEnabled based on TruthValue"""


_CldcKeyDecryptErrorEnabled_Object = MibScalar
cldcKeyDecryptErrorEnabled = _CldcKeyDecryptErrorEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 1, 1),
    _CldcKeyDecryptErrorEnabled_Type()
)
cldcKeyDecryptErrorEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldcKeyDecryptErrorEnabled.setStatus("current")
_CldcAssocNacAlertEnabled_Type = TruthValue
_CldcAssocNacAlertEnabled_Object = MibScalar
cldcAssocNacAlertEnabled = _CldcAssocNacAlertEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 1, 2),
    _CldcAssocNacAlertEnabled_Type()
)
cldcAssocNacAlertEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldcAssocNacAlertEnabled.setStatus("current")
_CldcDisassocNacAlertEnabled_Type = TruthValue
_CldcDisassocNacAlertEnabled_Object = MibScalar
cldcDisassocNacAlertEnabled = _CldcDisassocNacAlertEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 1, 3),
    _CldcDisassocNacAlertEnabled_Type()
)
cldcDisassocNacAlertEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldcDisassocNacAlertEnabled.setStatus("current")
_CldcMovedToRunStateEnabled_Type = TruthValue
_CldcMovedToRunStateEnabled_Object = MibScalar
cldcMovedToRunStateEnabled = _CldcMovedToRunStateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 1, 4),
    _CldcMovedToRunStateEnabled_Type()
)
cldcMovedToRunStateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldcMovedToRunStateEnabled.setStatus("current")


class _CiscoLwappDot11ClientStaticIpFailTrapEnabled_Type(TruthValue):
    """Custom type ciscoLwappDot11ClientStaticIpFailTrapEnabled based on TruthValue"""


_CiscoLwappDot11ClientStaticIpFailTrapEnabled_Object = MibScalar
ciscoLwappDot11ClientStaticIpFailTrapEnabled = _CiscoLwappDot11ClientStaticIpFailTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 1, 5),
    _CiscoLwappDot11ClientStaticIpFailTrapEnabled_Type()
)
ciscoLwappDot11ClientStaticIpFailTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientStaticIpFailTrapEnabled.setStatus("current")
_CldcNotifObjects_ObjectIdentity = ObjectIdentity
cldcNotifObjects = _CldcNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2)
)
_CldcClientRSSI_Type = Integer32
_CldcClientRSSI_Object = MibScalar
cldcClientRSSI = _CldcClientRSSI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 1),
    _CldcClientRSSI_Type()
)
cldcClientRSSI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientRSSI.setStatus("current")
_CldcClientSNR_Type = Integer32
_CldcClientSNR_Object = MibScalar
cldcClientSNR = _CldcClientSNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 2),
    _CldcClientSNR_Type()
)
cldcClientSNR.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientSNR.setStatus("current")


class _CldcDOT11ClientReasonCode_Type(Integer32):
    """Custom type cldcDOT11ClientReasonCode based on Integer32"""
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
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              99,
              101,
              105,
              106,
              200,
              201,
              202,
              203)
        )
    )
    namedValues = NamedValues(
        *(("akmpInvalid", 43),
          ("cipherSuiteRejected", 46),
          ("class2FrameFromNonAssStation", 7),
          ("class2FrameFromNonAuthStation", 6),
          ("deauthenticationLeaving", 3),
          ("disassociationAPBusy", 5),
          ("disassociationDueToInactivity", 4),
          ("disassociationStaHasLeft", 8),
          ("groupCipherInvalid", 41),
          ("inSufficientBandwidth", 202),
          ("inValidQosParams", 203),
          ("invalidInformationElement", 40),
          ("invalidRsnIeCapabilities", 45),
          ("maxAssociatedClientsReached", 101),
          ("maxAssociatedClientsReachedOnRadio", 105),
          ("maxAssociatedClientsReachedOnWlan", 106),
          ("missingReasonCode", 99),
          ("previousAuthNotValid", 2),
          ("qosPolicyMismatch", 201),
          ("staReqAssociationWithoutAuth", 9),
          ("unSpecifiedQosFailure", 200),
          ("unicastCipherInvalid", 42),
          ("unspecified", 1),
          ("unsupportedRsnVersion", 44))
    )


_CldcDOT11ClientReasonCode_Type.__name__ = "Integer32"
_CldcDOT11ClientReasonCode_Object = MibScalar
cldcDOT11ClientReasonCode = _CldcDOT11ClientReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 3),
    _CldcDOT11ClientReasonCode_Type()
)
cldcDOT11ClientReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcDOT11ClientReasonCode.setStatus("current")
_CldcDOT11ClientTxDataPackets_Type = Counter32
_CldcDOT11ClientTxDataPackets_Object = MibScalar
cldcDOT11ClientTxDataPackets = _CldcDOT11ClientTxDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 4),
    _CldcDOT11ClientTxDataPackets_Type()
)
cldcDOT11ClientTxDataPackets.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcDOT11ClientTxDataPackets.setStatus("current")
_CldcDOT11ClientTxDataBytes_Type = Counter32
_CldcDOT11ClientTxDataBytes_Object = MibScalar
cldcDOT11ClientTxDataBytes = _CldcDOT11ClientTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 5),
    _CldcDOT11ClientTxDataBytes_Type()
)
cldcDOT11ClientTxDataBytes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcDOT11ClientTxDataBytes.setStatus("current")
_CldcDOT11ClientRxDataPackets_Type = Counter32
_CldcDOT11ClientRxDataPackets_Object = MibScalar
cldcDOT11ClientRxDataPackets = _CldcDOT11ClientRxDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 6),
    _CldcDOT11ClientRxDataPackets_Type()
)
cldcDOT11ClientRxDataPackets.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcDOT11ClientRxDataPackets.setStatus("current")
_CldcDOT11ClientRxDataBytes_Type = Counter32
_CldcDOT11ClientRxDataBytes_Object = MibScalar
cldcDOT11ClientRxDataBytes = _CldcDOT11ClientRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 7),
    _CldcDOT11ClientRxDataBytes_Type()
)
cldcDOT11ClientRxDataBytes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcDOT11ClientRxDataBytes.setStatus("current")


class _CldcClientVlanId_Type(Integer32):
    """Custom type cldcClientVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_CldcClientVlanId_Type.__name__ = "Integer32"
_CldcClientVlanId_Object = MibScalar
cldcClientVlanId = _CldcClientVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 8),
    _CldcClientVlanId_Type()
)
cldcClientVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientVlanId.setStatus("current")


class _CldcClientPolicyType_Type(Integer32):
    """Custom type cldcClientPolicyType based on Integer32"""
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
        *(("dot1x", 1),
          ("notavailable", 5),
          ("unknown", 6),
          ("wapi", 7),
          ("wpa1", 2),
          ("wpa2", 3),
          ("wpa2vff", 4))
    )


_CldcClientPolicyType_Type.__name__ = "Integer32"
_CldcClientPolicyType_Object = MibScalar
cldcClientPolicyType = _CldcClientPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 9),
    _CldcClientPolicyType_Type()
)
cldcClientPolicyType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientPolicyType.setStatus("current")


class _CldcClientEapType_Type(Integer32):
    """Custom type cldcClientEapType based on Integer32"""
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
        *(("eapFast", 6),
          ("eapTls", 1),
          ("leap", 4),
          ("notavailable", 7),
          ("peap", 3),
          ("speke", 5),
          ("ttls", 2),
          ("unknown", 8))
    )


_CldcClientEapType_Type.__name__ = "Integer32"
_CldcClientEapType_Object = MibScalar
cldcClientEapType = _CldcClientEapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 10),
    _CldcClientEapType_Type()
)
cldcClientEapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientEapType.setStatus("current")
_CldcClientAID_Type = Unsigned32
_CldcClientAID_Object = MibScalar
cldcClientAID = _CldcClientAID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 11),
    _CldcClientAID_Type()
)
cldcClientAID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientAID.setStatus("current")


class _CldcClientAuthenticationAlgorithm_Type(Integer32):
    """Custom type cldcClientAuthenticationAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              129)
        )
    )
    namedValues = NamedValues(
        *(("openAndEap", 129),
          ("openSystem", 1),
          ("sharedKey", 2),
          ("unknown", 3))
    )


_CldcClientAuthenticationAlgorithm_Type.__name__ = "Integer32"
_CldcClientAuthenticationAlgorithm_Object = MibScalar
cldcClientAuthenticationAlgorithm = _CldcClientAuthenticationAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 12),
    _CldcClientAuthenticationAlgorithm_Type()
)
cldcClientAuthenticationAlgorithm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientAuthenticationAlgorithm.setStatus("current")


class _CldcClientWepState_Type(Integer32):
    """Custom type cldcClientWepState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CldcClientWepState_Type.__name__ = "Integer32"
_CldcClientWepState_Object = MibScalar
cldcClientWepState = _CldcClientWepState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 13),
    _CldcClientWepState_Type()
)
cldcClientWepState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientWepState.setStatus("current")


class _CldcClientEncryptionCypher_Type(Integer32):
    """Custom type cldcClientEncryptionCypher based on Integer32"""
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
        *(("ccmpAes", 1),
          ("none", 6),
          ("notavailable", 7),
          ("tkipMic", 2),
          ("unknown", 8),
          ("wapiSMS4", 9),
          ("wep104", 4),
          ("wep128", 5),
          ("wep40", 3))
    )


_CldcClientEncryptionCypher_Type.__name__ = "Integer32"
_CldcClientEncryptionCypher_Object = MibScalar
cldcClientEncryptionCypher = _CldcClientEncryptionCypher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 14),
    _CldcClientEncryptionCypher_Type()
)
cldcClientEncryptionCypher.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientEncryptionCypher.setStatus("current")
_CldcClientPortNumber_Type = Unsigned32
_CldcClientPortNumber_Object = MibScalar
cldcClientPortNumber = _CldcClientPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 15),
    _CldcClientPortNumber_Type()
)
cldcClientPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientPortNumber.setStatus("current")
_CldcClientAnchorAddressType_Type = InetAddressType
_CldcClientAnchorAddressType_Object = MibScalar
cldcClientAnchorAddressType = _CldcClientAnchorAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 16),
    _CldcClientAnchorAddressType_Type()
)
cldcClientAnchorAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientAnchorAddressType.setStatus("current")
_CldcClientAnchorAddress_Type = InetAddress
_CldcClientAnchorAddress_Object = MibScalar
cldcClientAnchorAddress = _CldcClientAnchorAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 17),
    _CldcClientAnchorAddress_Type()
)
cldcClientAnchorAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientAnchorAddress.setStatus("current")


class _CldcClientEssIndex_Type(Unsigned32):
    """Custom type cldcClientEssIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 517),
    )


_CldcClientEssIndex_Type.__name__ = "Unsigned32"
_CldcClientEssIndex_Object = MibScalar
cldcClientEssIndex = _CldcClientEssIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 18),
    _CldcClientEssIndex_Type()
)
cldcClientEssIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientEssIndex.setStatus("current")


class _CldcClientCcxVersion_Type(Integer32):
    """Custom type cldcClientCcxVersion based on Integer32"""
    defaultValue = 1

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
        *(("ccxv1", 2),
          ("ccxv2", 3),
          ("ccxv3", 4),
          ("ccxv4", 5),
          ("ccxv5", 6),
          ("ccxv6", 7),
          ("notSupported", 1))
    )


_CldcClientCcxVersion_Type.__name__ = "Integer32"
_CldcClientCcxVersion_Object = MibScalar
cldcClientCcxVersion = _CldcClientCcxVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 19),
    _CldcClientCcxVersion_Type()
)
cldcClientCcxVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientCcxVersion.setStatus("current")


class _CldcClientE2eVersion_Type(Integer32):
    """Custom type cldcClientE2eVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e2ev1", 2),
          ("e2ev2", 3),
          ("notSupported", 1))
    )


_CldcClientE2eVersion_Type.__name__ = "Integer32"
_CldcClientE2eVersion_Object = MibScalar
cldcClientE2eVersion = _CldcClientE2eVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 20),
    _CldcClientE2eVersion_Type()
)
cldcClientE2eVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientE2eVersion.setStatus("current")


class _CldcClientInterface_Type(DisplayString):
    """Custom type cldcClientInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CldcClientInterface_Type.__name__ = "DisplayString"
_CldcClientInterface_Object = MibScalar
cldcClientInterface = _CldcClientInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 21),
    _CldcClientInterface_Type()
)
cldcClientInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientInterface.setStatus("current")


class _CldcClientMobilityStatus_Type(Integer32):
    """Custom type cldcClientMobilityStatus based on Integer32"""
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
        *(("anchor", 3),
          ("exportanchor", 7),
          ("exportforeign", 8),
          ("foreign", 4),
          ("handoff", 5),
          ("local", 2),
          ("unassociated", 1),
          ("unknown", 6))
    )


_CldcClientMobilityStatus_Type.__name__ = "Integer32"
_CldcClientMobilityStatus_Object = MibScalar
cldcClientMobilityStatus = _CldcClientMobilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 22),
    _CldcClientMobilityStatus_Type()
)
cldcClientMobilityStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientMobilityStatus.setStatus("current")


class _CldcClientStatusCode_Type(Integer32):
    """Custom type cldcClientStatusCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CldcClientStatusCode_Type.__name__ = "Integer32"
_CldcClientStatusCode_Object = MibScalar
cldcClientStatusCode = _CldcClientStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 23),
    _CldcClientStatusCode_Type()
)
cldcClientStatusCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientStatusCode.setStatus("current")


class _CldcClientDeleteAction_Type(Integer32):
    """Custom type cldcClientDeleteAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("delete", 2))
    )


_CldcClientDeleteAction_Type.__name__ = "Integer32"
_CldcClientDeleteAction_Object = MibScalar
cldcClientDeleteAction = _CldcClientDeleteAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 24),
    _CldcClientDeleteAction_Type()
)
cldcClientDeleteAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientDeleteAction.setStatus("current")


class _CldcClientSecurityPolicyStatus_Type(Integer32):
    """Custom type cldcClientSecurityPolicyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("completed", 1),
          ("notcompleted", 2))
    )


_CldcClientSecurityPolicyStatus_Type.__name__ = "Integer32"
_CldcClientSecurityPolicyStatus_Object = MibScalar
cldcClientSecurityPolicyStatus = _CldcClientSecurityPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 25),
    _CldcClientSecurityPolicyStatus_Type()
)
cldcClientSecurityPolicyStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientSecurityPolicyStatus.setStatus("current")
_CldcClientTrapEventTime_Type = TimeTicks
_CldcClientTrapEventTime_Object = MibScalar
cldcClientTrapEventTime = _CldcClientTrapEventTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 26),
    _CldcClientTrapEventTime_Type()
)
cldcClientTrapEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientTrapEventTime.setStatus("current")
_CldcClientPolicyManagerState_Type = SnmpAdminString
_CldcClientPolicyManagerState_Object = MibScalar
cldcClientPolicyManagerState = _CldcClientPolicyManagerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 27),
    _CldcClientPolicyManagerState_Type()
)
cldcClientPolicyManagerState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientPolicyManagerState.setStatus("current")
_CldcClientAssocTime_Type = TimeStamp
_CldcClientAssocTime_Object = MibScalar
cldcClientAssocTime = _CldcClientAssocTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 28),
    _CldcClientAssocTime_Type()
)
cldcClientAssocTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientAssocTime.setStatus("current")
_CldcClientPmipDataValid_Type = TruthValue
_CldcClientPmipDataValid_Object = MibScalar
cldcClientPmipDataValid = _CldcClientPmipDataValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 29),
    _CldcClientPmipDataValid_Type()
)
cldcClientPmipDataValid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientPmipDataValid.setStatus("current")
_CldcClientMobilityExtDataValid_Type = TruthValue
_CldcClientMobilityExtDataValid_Object = MibScalar
cldcClientMobilityExtDataValid = _CldcClientMobilityExtDataValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 30),
    _CldcClientMobilityExtDataValid_Type()
)
cldcClientMobilityExtDataValid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientMobilityExtDataValid.setStatus("current")
_CldcClientPolicyErrors_Type = Counter64
_CldcClientPolicyErrors_Object = MibScalar
cldcClientPolicyErrors = _CldcClientPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 31),
    _CldcClientPolicyErrors_Type()
)
cldcClientPolicyErrors.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientPolicyErrors.setStatus("current")
_CldcClientSessionId_Type = SnmpAdminString
_CldcClientSessionId_Object = MibScalar
cldcClientSessionId = _CldcClientSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 32),
    _CldcClientSessionId_Type()
)
cldcClientSessionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientSessionId.setStatus("current")
_CldcClientPmipNai_Type = SnmpAdminString
_CldcClientPmipNai_Object = MibScalar
cldcClientPmipNai = _CldcClientPmipNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 33),
    _CldcClientPmipNai_Type()
)
cldcClientPmipNai.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientPmipNai.setStatus("current")
_CldcClientPmipState_Type = SnmpAdminString
_CldcClientPmipState_Object = MibScalar
cldcClientPmipState = _CldcClientPmipState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 34),
    _CldcClientPmipState_Type()
)
cldcClientPmipState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientPmipState.setStatus("current")


class _CldcClientPmipInterface_Type(SnmpAdminString):
    """Custom type cldcClientPmipInterface based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CldcClientPmipInterface_Type.__name__ = "SnmpAdminString"
_CldcClientPmipInterface_Object = MibScalar
cldcClientPmipInterface = _CldcClientPmipInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 35),
    _CldcClientPmipInterface_Type()
)
cldcClientPmipInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientPmipInterface.setStatus("current")
_CldcClientPmipHomeAddrType_Type = InetAddressType
_CldcClientPmipHomeAddrType_Object = MibScalar
cldcClientPmipHomeAddrType = _CldcClientPmipHomeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 36),
    _CldcClientPmipHomeAddrType_Type()
)
cldcClientPmipHomeAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientPmipHomeAddrType.setStatus("current")
_CldcClientPmipHomeAddr_Type = InetAddress
_CldcClientPmipHomeAddr_Object = MibScalar
cldcClientPmipHomeAddr = _CldcClientPmipHomeAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 37),
    _CldcClientPmipHomeAddr_Type()
)
cldcClientPmipHomeAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientPmipHomeAddr.setStatus("current")


class _CldcClientPmipAtt_Type(Integer32):
    """Custom type cldcClientPmipAtt based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 4),
          ("logicalNetworkInterface", 2),
          ("pointToPointInterface", 3),
          ("reserved", 1),
          ("threeGPP21xRTT", 12),
          ("threeGPP2HRPD", 11),
          ("threeGPP2UMB", 13),
          ("threeGPP2eHRPD", 10),
          ("threeGPPETRAN", 9),
          ("threeGPPGERAN", 7),
          ("threeGPPUTRAN", 8),
          ("wimax", 6),
          ("wirelessLan", 5))
    )


_CldcClientPmipAtt_Type.__name__ = "Integer32"
_CldcClientPmipAtt_Object = MibScalar
cldcClientPmipAtt = _CldcClientPmipAtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 38),
    _CldcClientPmipAtt_Type()
)
cldcClientPmipAtt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientPmipAtt.setStatus("current")
_CldcClientPmipLocalLinkId_Type = MacAddress
_CldcClientPmipLocalLinkId_Object = MibScalar
cldcClientPmipLocalLinkId = _CldcClientPmipLocalLinkId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 39),
    _CldcClientPmipLocalLinkId_Type()
)
cldcClientPmipLocalLinkId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientPmipLocalLinkId.setStatus("current")
_CldcClientPmipLmaName_Type = SnmpAdminString
_CldcClientPmipLmaName_Object = MibScalar
cldcClientPmipLmaName = _CldcClientPmipLmaName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 40),
    _CldcClientPmipLmaName_Type()
)
cldcClientPmipLmaName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientPmipLmaName.setStatus("current")
_CldcClientPmipLifeTime_Type = TimeTicks
_CldcClientPmipLifeTime_Object = MibScalar
cldcClientPmipLifeTime = _CldcClientPmipLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 41),
    _CldcClientPmipLifeTime_Type()
)
cldcClientPmipLifeTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientPmipLifeTime.setStatus("current")
_CldcClientPmipDomainName_Type = SnmpAdminString
_CldcClientPmipDomainName_Object = MibScalar
cldcClientPmipDomainName = _CldcClientPmipDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 42),
    _CldcClientPmipDomainName_Type()
)
cldcClientPmipDomainName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientPmipDomainName.setStatus("current")
_CldcClientPmipUpKey_Type = Unsigned32
_CldcClientPmipUpKey_Object = MibScalar
cldcClientPmipUpKey = _CldcClientPmipUpKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 43),
    _CldcClientPmipUpKey_Type()
)
cldcClientPmipUpKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientPmipUpKey.setStatus("current")
_CldcClientPmipDownKey_Type = Unsigned32
_CldcClientPmipDownKey_Object = MibScalar
cldcClientPmipDownKey = _CldcClientPmipDownKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 2, 44),
    _CldcClientPmipDownKey_Type()
)
cldcClientPmipDownKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldcClientPmipDownKey.setStatus("current")
_CldcStatusObjects_ObjectIdentity = ObjectIdentity
cldcStatusObjects = _CldcStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3)
)
_CldcClientTable_Object = MibTable
cldcClientTable = _CldcClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cldcClientTable.setStatus("current")
_CldcClientEntry_Object = MibTableRow
cldcClientEntry = _CldcClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1)
)
cldcClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldcClientEntry.setStatus("current")
_CldcClientMacAddress_Type = MacAddress
_CldcClientMacAddress_Object = MibTableColumn
cldcClientMacAddress = _CldcClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 1),
    _CldcClientMacAddress_Type()
)
cldcClientMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldcClientMacAddress.setStatus("current")
_CldcClientStatus_Type = CLDot11ClientStatus
_CldcClientStatus_Object = MibTableColumn
cldcClientStatus = _CldcClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 2),
    _CldcClientStatus_Type()
)
cldcClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientStatus.setStatus("current")


class _CldcClientWlanProfileName_Type(SnmpAdminString):
    """Custom type cldcClientWlanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CldcClientWlanProfileName_Type.__name__ = "SnmpAdminString"
_CldcClientWlanProfileName_Object = MibTableColumn
cldcClientWlanProfileName = _CldcClientWlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 3),
    _CldcClientWlanProfileName_Type()
)
cldcClientWlanProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientWlanProfileName.setStatus("current")


class _CldcClientWgbStatus_Type(Integer32):
    """Custom type cldcClientWgbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("regClient", 1),
          ("wgb", 3),
          ("wgbClient", 2))
    )


_CldcClientWgbStatus_Type.__name__ = "Integer32"
_CldcClientWgbStatus_Object = MibTableColumn
cldcClientWgbStatus = _CldcClientWgbStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 4),
    _CldcClientWgbStatus_Type()
)
cldcClientWgbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientWgbStatus.setStatus("current")
_CldcClientWgbMacAddress_Type = MacAddress
_CldcClientWgbMacAddress_Object = MibTableColumn
cldcClientWgbMacAddress = _CldcClientWgbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 5),
    _CldcClientWgbMacAddress_Type()
)
cldcClientWgbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientWgbMacAddress.setStatus("current")


class _CldcClientProtocol_Type(Integer32):
    """Custom type cldcClientProtocol based on Integer32"""
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
        *(("dot11a", 1),
          ("dot11ac5", 10),
          ("dot11b", 2),
          ("dot11g", 3),
          ("dot11n24", 6),
          ("dot11n5", 7),
          ("dot3", 9),
          ("ethernet", 8),
          ("mobile", 5),
          ("unknown", 4))
    )


_CldcClientProtocol_Type.__name__ = "Integer32"
_CldcClientProtocol_Object = MibTableColumn
cldcClientProtocol = _CldcClientProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 6),
    _CldcClientProtocol_Type()
)
cldcClientProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientProtocol.setStatus("current")


class _CldcAssociationMode_Type(Integer32):
    """Custom type cldcAssociationMode based on Integer32"""
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
        *(("unknown", 1),
          ("wep", 2),
          ("wpa", 3),
          ("wpa2", 4))
    )


_CldcAssociationMode_Type.__name__ = "Integer32"
_CldcAssociationMode_Object = MibTableColumn
cldcAssociationMode = _CldcAssociationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 7),
    _CldcAssociationMode_Type()
)
cldcAssociationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcAssociationMode.setStatus("current")
_CldcApMacAddress_Type = MacAddress
_CldcApMacAddress_Object = MibTableColumn
cldcApMacAddress = _CldcApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 8),
    _CldcApMacAddress_Type()
)
cldcApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcApMacAddress.setStatus("current")
_CldcIfType_Type = CLApIfType
_CldcIfType_Object = MibTableColumn
cldcIfType = _CldcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 9),
    _CldcIfType_Type()
)
cldcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcIfType.setStatus("current")
_CldcClientIPAddress_Type = IpAddress
_CldcClientIPAddress_Object = MibTableColumn
cldcClientIPAddress = _CldcClientIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 10),
    _CldcClientIPAddress_Type()
)
cldcClientIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientIPAddress.setStatus("current")


class _CldcClientNacState_Type(Integer32):
    """Custom type cldcClientNacState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("quarantine", 1))
    )


_CldcClientNacState_Type.__name__ = "Integer32"
_CldcClientNacState_Object = MibTableColumn
cldcClientNacState = _CldcClientNacState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 11),
    _CldcClientNacState_Type()
)
cldcClientNacState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldcClientNacState.setStatus("current")
_CldcClientQuarantineVLAN_Type = VlanId
_CldcClientQuarantineVLAN_Object = MibTableColumn
cldcClientQuarantineVLAN = _CldcClientQuarantineVLAN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 12),
    _CldcClientQuarantineVLAN_Type()
)
cldcClientQuarantineVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientQuarantineVLAN.setStatus("current")
_CldcClientAccessVLAN_Type = VlanId
_CldcClientAccessVLAN_Object = MibTableColumn
cldcClientAccessVLAN = _CldcClientAccessVLAN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 13),
    _CldcClientAccessVLAN_Type()
)
cldcClientAccessVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientAccessVLAN.setStatus("current")
_CldcClientLoginTime_Type = TimeStamp
_CldcClientLoginTime_Object = MibTableColumn
cldcClientLoginTime = _CldcClientLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 14),
    _CldcClientLoginTime_Type()
)
cldcClientLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientLoginTime.setStatus("current")
_CldcClientUpTime_Type = TimeInterval
_CldcClientUpTime_Object = MibTableColumn
cldcClientUpTime = _CldcClientUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 15),
    _CldcClientUpTime_Type()
)
cldcClientUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientUpTime.setStatus("current")
_CldcClientPowerSaveMode_Type = CLClientPowerSaveMode
_CldcClientPowerSaveMode_Object = MibTableColumn
cldcClientPowerSaveMode = _CldcClientPowerSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 16),
    _CldcClientPowerSaveMode_Type()
)
cldcClientPowerSaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientPowerSaveMode.setStatus("current")


class _CldcClientCurrentTxRateSet_Type(OctetString):
    """Custom type cldcClientCurrentTxRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CldcClientCurrentTxRateSet_Type.__name__ = "OctetString"
_CldcClientCurrentTxRateSet_Object = MibTableColumn
cldcClientCurrentTxRateSet = _CldcClientCurrentTxRateSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 17),
    _CldcClientCurrentTxRateSet_Type()
)
cldcClientCurrentTxRateSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientCurrentTxRateSet.setStatus("current")
if mibBuilder.loadTexts:
    cldcClientCurrentTxRateSet.setUnits("Mbit/s")


class _CldcClientDataRateSet_Type(OctetString):
    """Custom type cldcClientDataRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_CldcClientDataRateSet_Type.__name__ = "OctetString"
_CldcClientDataRateSet_Object = MibTableColumn
cldcClientDataRateSet = _CldcClientDataRateSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 18),
    _CldcClientDataRateSet_Type()
)
cldcClientDataRateSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientDataRateSet.setStatus("current")


class _CldcClientHreapApAuth_Type(Integer32):
    """Custom type cldcClientHreapApAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notApplicable", 3),
          ("true", 1))
    )


_CldcClientHreapApAuth_Type.__name__ = "Integer32"
_CldcClientHreapApAuth_Object = MibTableColumn
cldcClientHreapApAuth = _CldcClientHreapApAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 19),
    _CldcClientHreapApAuth_Type()
)
cldcClientHreapApAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientHreapApAuth.setStatus("current")
_CldcClient80211uCapable_Type = TruthValue
_CldcClient80211uCapable_Object = MibTableColumn
cldcClient80211uCapable = _CldcClient80211uCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 20),
    _CldcClient80211uCapable_Type()
)
cldcClient80211uCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClient80211uCapable.setStatus("current")
_CldcClientPostureState_Type = TruthValue
_CldcClientPostureState_Object = MibTableColumn
cldcClientPostureState = _CldcClientPostureState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 21),
    _CldcClientPostureState_Type()
)
cldcClientPostureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientPostureState.setStatus("current")
_CldcClientAclName_Type = SnmpAdminString
_CldcClientAclName_Object = MibTableColumn
cldcClientAclName = _CldcClientAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 22),
    _CldcClientAclName_Type()
)
cldcClientAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientAclName.setStatus("current")


class _CldcClientAclApplied_Type(Integer32):
    """Custom type cldcClientAclApplied based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notAvailable", 3),
          ("true", 1))
    )


_CldcClientAclApplied_Type.__name__ = "Integer32"
_CldcClientAclApplied_Object = MibTableColumn
cldcClientAclApplied = _CldcClientAclApplied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 23),
    _CldcClientAclApplied_Type()
)
cldcClientAclApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientAclApplied.setStatus("current")
_CldcClientRedirectUrl_Type = CiscoURLStringOrEmpty
_CldcClientRedirectUrl_Object = MibTableColumn
cldcClientRedirectUrl = _CldcClientRedirectUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 24),
    _CldcClientRedirectUrl_Type()
)
cldcClientRedirectUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientRedirectUrl.setStatus("current")
_CldcClientAaaOverrideAclName_Type = SnmpAdminString
_CldcClientAaaOverrideAclName_Object = MibTableColumn
cldcClientAaaOverrideAclName = _CldcClientAaaOverrideAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 25),
    _CldcClientAaaOverrideAclName_Type()
)
cldcClientAaaOverrideAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientAaaOverrideAclName.setStatus("current")


class _CldcClientAaaOverrideAclApplied_Type(Integer32):
    """Custom type cldcClientAaaOverrideAclApplied based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notAvailable", 3),
          ("true", 1))
    )


_CldcClientAaaOverrideAclApplied_Type.__name__ = "Integer32"
_CldcClientAaaOverrideAclApplied_Object = MibTableColumn
cldcClientAaaOverrideAclApplied = _CldcClientAaaOverrideAclApplied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 26),
    _CldcClientAaaOverrideAclApplied_Type()
)
cldcClientAaaOverrideAclApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientAaaOverrideAclApplied.setStatus("current")


class _CldcClientUsername_Type(SnmpAdminString):
    """Custom type cldcClientUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CldcClientUsername_Type.__name__ = "SnmpAdminString"
_CldcClientUsername_Object = MibTableColumn
cldcClientUsername = _CldcClientUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 27),
    _CldcClientUsername_Type()
)
cldcClientUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientUsername.setStatus("current")


class _CldcClientSSID_Type(SnmpAdminString):
    """Custom type cldcClientSSID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CldcClientSSID_Type.__name__ = "SnmpAdminString"
_CldcClientSSID_Object = MibTableColumn
cldcClientSSID = _CldcClientSSID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 28),
    _CldcClientSSID_Type()
)
cldcClientSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientSSID.setStatus("current")
_CldcClientSecurityTagId_Type = Unsigned32
_CldcClientSecurityTagId_Object = MibTableColumn
cldcClientSecurityTagId = _CldcClientSecurityTagId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 29),
    _CldcClientSecurityTagId_Type()
)
cldcClientSecurityTagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientSecurityTagId.setStatus("current")
_CldcClientTypeKTS_Type = TruthValue
_CldcClientTypeKTS_Object = MibTableColumn
cldcClientTypeKTS = _CldcClientTypeKTS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 30),
    _CldcClientTypeKTS_Type()
)
cldcClientTypeKTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientTypeKTS.setStatus("current")
_CldcClientIpv6AclName_Type = DisplayString
_CldcClientIpv6AclName_Object = MibTableColumn
cldcClientIpv6AclName = _CldcClientIpv6AclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 31),
    _CldcClientIpv6AclName_Type()
)
cldcClientIpv6AclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientIpv6AclName.setStatus("current")


class _CldcClientIpv6AclApplied_Type(Integer32):
    """Custom type cldcClientIpv6AclApplied based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notAvailable", 3),
          ("true", 1))
    )


_CldcClientIpv6AclApplied_Type.__name__ = "Integer32"
_CldcClientIpv6AclApplied_Object = MibTableColumn
cldcClientIpv6AclApplied = _CldcClientIpv6AclApplied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 32),
    _CldcClientIpv6AclApplied_Type()
)
cldcClientIpv6AclApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientIpv6AclApplied.setStatus("current")


class _CldcClientDataSwitching_Type(Integer32):
    """Custom type cldcClientDataSwitching based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("central", 2),
          ("local", 3),
          ("unknown", 1))
    )


_CldcClientDataSwitching_Type.__name__ = "Integer32"
_CldcClientDataSwitching_Object = MibTableColumn
cldcClientDataSwitching = _CldcClientDataSwitching_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 33),
    _CldcClientDataSwitching_Type()
)
cldcClientDataSwitching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientDataSwitching.setStatus("current")


class _CldcClientAuthentication_Type(Integer32):
    """Custom type cldcClientAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("central", 2),
          ("local", 3),
          ("unknown", 1))
    )


_CldcClientAuthentication_Type.__name__ = "Integer32"
_CldcClientAuthentication_Object = MibTableColumn
cldcClientAuthentication = _CldcClientAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 34),
    _CldcClientAuthentication_Type()
)
cldcClientAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientAuthentication.setStatus("current")
_CldcClientChannel_Type = Unsigned32
_CldcClientChannel_Object = MibTableColumn
cldcClientChannel = _CldcClientChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 35),
    _CldcClientChannel_Type()
)
cldcClientChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientChannel.setStatus("current")


class _CldcClientAuthMode_Type(Integer32):
    """Custom type cldcClientAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("cckm", 3),
          ("ftDot1x", 6),
          ("ftPsk", 7),
          ("none", 0),
          ("pmfDot1x", 8),
          ("pmfPsk", 9),
          ("psk", 1),
          ("radius", 2),
          ("wapicert", 5),
          ("wapipsk", 4))
    )


_CldcClientAuthMode_Type.__name__ = "Integer32"
_CldcClientAuthMode_Object = MibTableColumn
cldcClientAuthMode = _CldcClientAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 36),
    _CldcClientAuthMode_Type()
)
cldcClientAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientAuthMode.setStatus("current")


class _CldcClientReasonCode_Type(Integer32):
    """Custom type cldcClientReasonCode based on Integer32"""
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
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              99,
              101,
              105,
              106,
              200,
              201,
              202,
              203)
        )
    )
    namedValues = NamedValues(
        *(("akmpInvalid", 43),
          ("cipherSuiteRejected", 46),
          ("class2FrameFromNonAssStation", 7),
          ("class2FrameFromNonAuthStation", 6),
          ("deauthenticationLeaving", 3),
          ("disassociationAPBusy", 5),
          ("disassociationDueToInactivity", 4),
          ("disassociationStaHasLeft", 8),
          ("groupCipherInvalid", 41),
          ("inSufficientBandwidth", 202),
          ("inValidQosParams", 203),
          ("invalidInformationElement", 40),
          ("invalidRsnIeCapabilities", 45),
          ("maxAssociatedClientsReached", 101),
          ("maxAssociatedClientsReachedOnRadio", 105),
          ("maxAssociatedClientsReachedOnWlan", 106),
          ("missingReasonCode", 99),
          ("previousAuthNotValid", 2),
          ("qosPolicyMismatch", 201),
          ("staReqAssociationWithoutAuth", 9),
          ("unSpecifiedQosFailure", 200),
          ("unicastCipherInvalid", 42),
          ("unspecified", 1),
          ("unsupportedRsnVersion", 44))
    )


_CldcClientReasonCode_Type.__name__ = "Integer32"
_CldcClientReasonCode_Object = MibTableColumn
cldcClientReasonCode = _CldcClientReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 37),
    _CldcClientReasonCode_Type()
)
cldcClientReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientReasonCode.setStatus("current")
_CldcClientSessionID_Type = SnmpAdminString
_CldcClientSessionID_Object = MibTableColumn
cldcClientSessionID = _CldcClientSessionID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 38),
    _CldcClientSessionID_Type()
)
cldcClientSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientSessionID.setStatus("current")
_CldcClientApRoamMacAddress_Type = MacAddress
_CldcClientApRoamMacAddress_Object = MibTableColumn
cldcClientApRoamMacAddress = _CldcClientApRoamMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 39),
    _CldcClientApRoamMacAddress_Type()
)
cldcClientApRoamMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientApRoamMacAddress.setStatus("current")
_CldcClientMdnsProfile_Type = SnmpAdminString
_CldcClientMdnsProfile_Object = MibTableColumn
cldcClientMdnsProfile = _CldcClientMdnsProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 40),
    _CldcClientMdnsProfile_Type()
)
cldcClientMdnsProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientMdnsProfile.setStatus("current")
_CldcClientMdnsAdvCount_Type = Unsigned32
_CldcClientMdnsAdvCount_Object = MibTableColumn
cldcClientMdnsAdvCount = _CldcClientMdnsAdvCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 41),
    _CldcClientMdnsAdvCount_Type()
)
cldcClientMdnsAdvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientMdnsAdvCount.setStatus("current")
_CldcClientPolicyName_Type = SnmpAdminString
_CldcClientPolicyName_Object = MibTableColumn
cldcClientPolicyName = _CldcClientPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 42),
    _CldcClientPolicyName_Type()
)
cldcClientPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientPolicyName.setStatus("current")
_CldcClientAAARole_Type = SnmpAdminString
_CldcClientAAARole_Object = MibTableColumn
cldcClientAAARole = _CldcClientAAARole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 43),
    _CldcClientAAARole_Type()
)
cldcClientAAARole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientAAARole.setStatus("current")
_CldcClientDeviceType_Type = SnmpAdminString
_CldcClientDeviceType_Object = MibTableColumn
cldcClientDeviceType = _CldcClientDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 44),
    _CldcClientDeviceType_Type()
)
cldcClientDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientDeviceType.setStatus("current")


class _CldcUserAuthType_Type(Integer32):
    """Custom type cldcUserAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("other", 5),
          ("portal", 3),
          ("simPeap", 4),
          ("wepPsk", 2))
    )


_CldcUserAuthType_Type.__name__ = "Integer32"
_CldcUserAuthType_Object = MibTableColumn
cldcUserAuthType = _CldcUserAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 1, 1, 45),
    _CldcUserAuthType_Type()
)
cldcUserAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcUserAuthType.setStatus("current")
_CldcClientByIpTable_Object = MibTable
cldcClientByIpTable = _CldcClientByIpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cldcClientByIpTable.setStatus("current")
_CldcClientByIpEntry_Object = MibTableRow
cldcClientByIpEntry = _CldcClientByIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 2, 1)
)
cldcClientByIpEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddressType"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddress"),
)
if mibBuilder.loadTexts:
    cldcClientByIpEntry.setStatus("current")
_CldcClientByIpAddressType_Type = InetAddressType
_CldcClientByIpAddressType_Object = MibTableColumn
cldcClientByIpAddressType = _CldcClientByIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 2, 1, 2),
    _CldcClientByIpAddressType_Type()
)
cldcClientByIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldcClientByIpAddressType.setStatus("current")
_CldcClientByIpAddress_Type = InetAddress
_CldcClientByIpAddress_Object = MibTableColumn
cldcClientByIpAddress = _CldcClientByIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 2, 1, 3),
    _CldcClientByIpAddress_Type()
)
cldcClientByIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldcClientByIpAddress.setStatus("current")


class _CldcClientByIpAddressDiscoverType_Type(Integer32):
    """Custom type cldcClientByIpAddressDiscoverType based on Integer32"""
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
        *(("dhcp", 3),
          ("invalid", 1),
          ("local", 5),
          ("ndp", 2),
          ("packet", 4),
          ("static", 6))
    )


_CldcClientByIpAddressDiscoverType_Type.__name__ = "Integer32"
_CldcClientByIpAddressDiscoverType_Object = MibTableColumn
cldcClientByIpAddressDiscoverType = _CldcClientByIpAddressDiscoverType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 2, 1, 4),
    _CldcClientByIpAddressDiscoverType_Type()
)
cldcClientByIpAddressDiscoverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientByIpAddressDiscoverType.setStatus("current")
_CldcClientByIpAddressLastSeen_Type = TimeStamp
_CldcClientByIpAddressLastSeen_Object = MibTableColumn
cldcClientByIpAddressLastSeen = _CldcClientByIpAddressLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 2, 1, 5),
    _CldcClientByIpAddressLastSeen_Type()
)
cldcClientByIpAddressLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientByIpAddressLastSeen.setStatus("current")
_CldcSleepingClientTable_Object = MibTable
cldcSleepingClientTable = _CldcSleepingClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cldcSleepingClientTable.setStatus("current")
_CldcSleepingClientEntry_Object = MibTableRow
cldcSleepingClientEntry = _CldcSleepingClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 3, 1)
)
cldcSleepingClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcSleepingClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldcSleepingClientEntry.setStatus("current")
_CldcSleepingClientMacAddress_Type = MacAddress
_CldcSleepingClientMacAddress_Object = MibTableColumn
cldcSleepingClientMacAddress = _CldcSleepingClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 3, 1, 1),
    _CldcSleepingClientMacAddress_Type()
)
cldcSleepingClientMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldcSleepingClientMacAddress.setStatus("current")
_CldcSleepingClientSsid_Type = OctetString
_CldcSleepingClientSsid_Object = MibTableColumn
cldcSleepingClientSsid = _CldcSleepingClientSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 3, 1, 2),
    _CldcSleepingClientSsid_Type()
)
cldcSleepingClientSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcSleepingClientSsid.setStatus("current")
_CldcSleepingClientUserName_Type = SnmpAdminString
_CldcSleepingClientUserName_Object = MibTableColumn
cldcSleepingClientUserName = _CldcSleepingClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 3, 1, 3),
    _CldcSleepingClientUserName_Type()
)
cldcSleepingClientUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcSleepingClientUserName.setStatus("current")
_CldcSleepingClientRemainingTime_Type = TimeInterval
_CldcSleepingClientRemainingTime_Object = MibTableColumn
cldcSleepingClientRemainingTime = _CldcSleepingClientRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 3, 1, 4),
    _CldcSleepingClientRemainingTime_Type()
)
cldcSleepingClientRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcSleepingClientRemainingTime.setStatus("current")
if mibBuilder.loadTexts:
    cldcSleepingClientRemainingTime.setUnits("Hours")
_CldcSleepingClientRowStatus_Type = RowStatus
_CldcSleepingClientRowStatus_Object = MibTableColumn
cldcSleepingClientRowStatus = _CldcSleepingClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 3, 3, 1, 5),
    _CldcSleepingClientRowStatus_Type()
)
cldcSleepingClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldcSleepingClientRowStatus.setStatus("current")
_CldcStatisticObjects_ObjectIdentity = ObjectIdentity
cldcStatisticObjects = _CldcStatisticObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4)
)
_CldcClientStatisticTable_Object = MibTable
cldcClientStatisticTable = _CldcClientStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cldcClientStatisticTable.setStatus("current")
_CldcClientStatisticEntry_Object = MibTableRow
cldcClientStatisticEntry = _CldcClientStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1)
)
cldcClientStatisticEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldcClientStatisticEntry.setStatus("current")
_CldcClientDataRetries_Type = Counter64
_CldcClientDataRetries_Object = MibTableColumn
cldcClientDataRetries = _CldcClientDataRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 1),
    _CldcClientDataRetries_Type()
)
cldcClientDataRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientDataRetries.setStatus("current")
if mibBuilder.loadTexts:
    cldcClientDataRetries.setUnits("Retries")
_CldcClientRtsRetries_Type = Counter64
_CldcClientRtsRetries_Object = MibTableColumn
cldcClientRtsRetries = _CldcClientRtsRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 2),
    _CldcClientRtsRetries_Type()
)
cldcClientRtsRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientRtsRetries.setStatus("current")
if mibBuilder.loadTexts:
    cldcClientRtsRetries.setUnits("Retries")
_CldcClientDuplicatePackets_Type = Counter64
_CldcClientDuplicatePackets_Object = MibTableColumn
cldcClientDuplicatePackets = _CldcClientDuplicatePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 3),
    _CldcClientDuplicatePackets_Type()
)
cldcClientDuplicatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientDuplicatePackets.setStatus("current")
if mibBuilder.loadTexts:
    cldcClientDuplicatePackets.setUnits("Packets")
_CldcClientDecryptFailures_Type = Counter64
_CldcClientDecryptFailures_Object = MibTableColumn
cldcClientDecryptFailures = _CldcClientDecryptFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 4),
    _CldcClientDecryptFailures_Type()
)
cldcClientDecryptFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientDecryptFailures.setStatus("current")
if mibBuilder.loadTexts:
    cldcClientDecryptFailures.setUnits("Packets")
_CldcClientMicErrors_Type = Counter64
_CldcClientMicErrors_Object = MibTableColumn
cldcClientMicErrors = _CldcClientMicErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 5),
    _CldcClientMicErrors_Type()
)
cldcClientMicErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientMicErrors.setStatus("current")
if mibBuilder.loadTexts:
    cldcClientMicErrors.setUnits("Packets")
_CldcClientMicMissingFrames_Type = Counter64
_CldcClientMicMissingFrames_Object = MibTableColumn
cldcClientMicMissingFrames = _CldcClientMicMissingFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 6),
    _CldcClientMicMissingFrames_Type()
)
cldcClientMicMissingFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientMicMissingFrames.setStatus("current")
if mibBuilder.loadTexts:
    cldcClientMicMissingFrames.setUnits("Packets")
_CldcClientRaPacketsDropped_Type = Counter64
_CldcClientRaPacketsDropped_Object = MibTableColumn
cldcClientRaPacketsDropped = _CldcClientRaPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 7),
    _CldcClientRaPacketsDropped_Type()
)
cldcClientRaPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientRaPacketsDropped.setStatus("current")
_CldcClientInterimUpdatesCount_Type = Counter64
_CldcClientInterimUpdatesCount_Object = MibTableColumn
cldcClientInterimUpdatesCount = _CldcClientInterimUpdatesCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 8),
    _CldcClientInterimUpdatesCount_Type()
)
cldcClientInterimUpdatesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientInterimUpdatesCount.setStatus("current")
_CldcClientDataBytesReceived_Type = Counter64
_CldcClientDataBytesReceived_Object = MibTableColumn
cldcClientDataBytesReceived = _CldcClientDataBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 9),
    _CldcClientDataBytesReceived_Type()
)
cldcClientDataBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientDataBytesReceived.setStatus("current")
_CldcClientRealtimeBytesReceived_Type = Counter64
_CldcClientRealtimeBytesReceived_Object = MibTableColumn
cldcClientRealtimeBytesReceived = _CldcClientRealtimeBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 10),
    _CldcClientRealtimeBytesReceived_Type()
)
cldcClientRealtimeBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientRealtimeBytesReceived.setStatus("current")
_CldcClientRxDataBytesDropped_Type = Counter64
_CldcClientRxDataBytesDropped_Object = MibTableColumn
cldcClientRxDataBytesDropped = _CldcClientRxDataBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 11),
    _CldcClientRxDataBytesDropped_Type()
)
cldcClientRxDataBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientRxDataBytesDropped.setStatus("current")
_CldcClientRxRealtimeBytesDropped_Type = Counter64
_CldcClientRxRealtimeBytesDropped_Object = MibTableColumn
cldcClientRxRealtimeBytesDropped = _CldcClientRxRealtimeBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 12),
    _CldcClientRxRealtimeBytesDropped_Type()
)
cldcClientRxRealtimeBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientRxRealtimeBytesDropped.setStatus("current")
_CldcClientDataBytesSent_Type = Counter64
_CldcClientDataBytesSent_Object = MibTableColumn
cldcClientDataBytesSent = _CldcClientDataBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 13),
    _CldcClientDataBytesSent_Type()
)
cldcClientDataBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientDataBytesSent.setStatus("current")
_CldcClientRealtimeBytesSent_Type = Counter64
_CldcClientRealtimeBytesSent_Object = MibTableColumn
cldcClientRealtimeBytesSent = _CldcClientRealtimeBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 14),
    _CldcClientRealtimeBytesSent_Type()
)
cldcClientRealtimeBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientRealtimeBytesSent.setStatus("current")
_CldcClientTxDataBytesDropped_Type = Counter64
_CldcClientTxDataBytesDropped_Object = MibTableColumn
cldcClientTxDataBytesDropped = _CldcClientTxDataBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 15),
    _CldcClientTxDataBytesDropped_Type()
)
cldcClientTxDataBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientTxDataBytesDropped.setStatus("current")
_CldcClientTxRealtimeBytesDropped_Type = Counter64
_CldcClientTxRealtimeBytesDropped_Object = MibTableColumn
cldcClientTxRealtimeBytesDropped = _CldcClientTxRealtimeBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 16),
    _CldcClientTxRealtimeBytesDropped_Type()
)
cldcClientTxRealtimeBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientTxRealtimeBytesDropped.setStatus("current")
_CldcClientDataPacketsReceived_Type = Counter64
_CldcClientDataPacketsReceived_Object = MibTableColumn
cldcClientDataPacketsReceived = _CldcClientDataPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 17),
    _CldcClientDataPacketsReceived_Type()
)
cldcClientDataPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientDataPacketsReceived.setStatus("current")
_CldcClientRealtimePacketsReceived_Type = Counter64
_CldcClientRealtimePacketsReceived_Object = MibTableColumn
cldcClientRealtimePacketsReceived = _CldcClientRealtimePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 18),
    _CldcClientRealtimePacketsReceived_Type()
)
cldcClientRealtimePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientRealtimePacketsReceived.setStatus("current")
_CldcClientRxDataPacketsDropped_Type = Counter64
_CldcClientRxDataPacketsDropped_Object = MibTableColumn
cldcClientRxDataPacketsDropped = _CldcClientRxDataPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 19),
    _CldcClientRxDataPacketsDropped_Type()
)
cldcClientRxDataPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientRxDataPacketsDropped.setStatus("current")
_CldcClientRxRealtimePacketsDropped_Type = Counter64
_CldcClientRxRealtimePacketsDropped_Object = MibTableColumn
cldcClientRxRealtimePacketsDropped = _CldcClientRxRealtimePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 20),
    _CldcClientRxRealtimePacketsDropped_Type()
)
cldcClientRxRealtimePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientRxRealtimePacketsDropped.setStatus("current")
_CldcClientDataPacketsSent_Type = Counter64
_CldcClientDataPacketsSent_Object = MibTableColumn
cldcClientDataPacketsSent = _CldcClientDataPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 21),
    _CldcClientDataPacketsSent_Type()
)
cldcClientDataPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientDataPacketsSent.setStatus("current")
_CldcClientRealtimePacketsSent_Type = Counter64
_CldcClientRealtimePacketsSent_Object = MibTableColumn
cldcClientRealtimePacketsSent = _CldcClientRealtimePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 22),
    _CldcClientRealtimePacketsSent_Type()
)
cldcClientRealtimePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientRealtimePacketsSent.setStatus("current")
_CldcClientTxDataPacketsDropped_Type = Counter64
_CldcClientTxDataPacketsDropped_Object = MibTableColumn
cldcClientTxDataPacketsDropped = _CldcClientTxDataPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 23),
    _CldcClientTxDataPacketsDropped_Type()
)
cldcClientTxDataPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientTxDataPacketsDropped.setStatus("current")
_CldcClientTxRealtimePacketsDropped_Type = Counter64
_CldcClientTxRealtimePacketsDropped_Object = MibTableColumn
cldcClientTxRealtimePacketsDropped = _CldcClientTxRealtimePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 24),
    _CldcClientTxRealtimePacketsDropped_Type()
)
cldcClientTxRealtimePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientTxRealtimePacketsDropped.setStatus("current")
_CldcClientTxDataPackets_Type = Counter64
_CldcClientTxDataPackets_Object = MibTableColumn
cldcClientTxDataPackets = _CldcClientTxDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 25),
    _CldcClientTxDataPackets_Type()
)
cldcClientTxDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientTxDataPackets.setStatus("current")
_CldcClientTxDataBytes_Type = Counter64
_CldcClientTxDataBytes_Object = MibTableColumn
cldcClientTxDataBytes = _CldcClientTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 26),
    _CldcClientTxDataBytes_Type()
)
cldcClientTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientTxDataBytes.setStatus("current")
_CldcClientRxDataPackets_Type = Counter64
_CldcClientRxDataPackets_Object = MibTableColumn
cldcClientRxDataPackets = _CldcClientRxDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 27),
    _CldcClientRxDataPackets_Type()
)
cldcClientRxDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientRxDataPackets.setStatus("current")
_CldcClientRxDataBytes_Type = Counter64
_CldcClientRxDataBytes_Object = MibTableColumn
cldcClientRxDataBytes = _CldcClientRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 1, 4, 1, 1, 28),
    _CldcClientRxDataBytes_Type()
)
cldcClientRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldcClientRxDataBytes.setStatus("current")
_CiscoLwappDot11ClientMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientMIBConform = _CiscoLwappDot11ClientMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 2)
)
_CiscoLwappDot11ClientMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientMIBCompliances = _CiscoLwappDot11ClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 2, 1)
)
_CiscoLwappDot11ClientMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientMIBGroups = _CiscoLwappDot11ClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 2, 2)
)
_CiscoLwappDot11ClientCcxMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientCcxMIBObjects = _CiscoLwappDot11ClientCcxMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3)
)
_CldcCcxObjects_ObjectIdentity = ObjectIdentity
cldcCcxObjects = _CldcCcxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 1)
)
_CldccCcxVersionInfoTable_Object = MibTable
cldccCcxVersionInfoTable = _CldccCcxVersionInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cldccCcxVersionInfoTable.setStatus("current")
_CldccCcxVersionInfoEntry_Object = MibTableRow
cldccCcxVersionInfoEntry = _CldccCcxVersionInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 1, 1, 1)
)
cldccCcxVersionInfoEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccCcxVersionInfoEntry.setStatus("current")
_CldccCcxFoundationServiceVersion_Type = CcxServiceVersion
_CldccCcxFoundationServiceVersion_Object = MibTableColumn
cldccCcxFoundationServiceVersion = _CldccCcxFoundationServiceVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 1, 1, 1, 1),
    _CldccCcxFoundationServiceVersion_Type()
)
cldccCcxFoundationServiceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccCcxFoundationServiceVersion.setStatus("current")
_CldccCcxLocationServiceVersion_Type = CcxServiceVersion
_CldccCcxLocationServiceVersion_Object = MibTableColumn
cldccCcxLocationServiceVersion = _CldccCcxLocationServiceVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 1, 1, 1, 2),
    _CldccCcxLocationServiceVersion_Type()
)
cldccCcxLocationServiceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccCcxLocationServiceVersion.setStatus("current")
_CldccCcxVoiceServiceVersion_Type = CcxServiceVersion
_CldccCcxVoiceServiceVersion_Object = MibTableColumn
cldccCcxVoiceServiceVersion = _CldccCcxVoiceServiceVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 1, 1, 1, 3),
    _CldccCcxVoiceServiceVersion_Type()
)
cldccCcxVoiceServiceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccCcxVoiceServiceVersion.setStatus("current")
_CldccCcxManagementServiceVersion_Type = CcxServiceVersion
_CldccCcxManagementServiceVersion_Object = MibTableColumn
cldccCcxManagementServiceVersion = _CldccCcxManagementServiceVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 1, 1, 1, 4),
    _CldccCcxManagementServiceVersion_Type()
)
cldccCcxManagementServiceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccCcxManagementServiceVersion.setStatus("current")

# Managed Objects groups

ciscoLwappDot11ClientMIBConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 2, 2, 1)
)
ciscoLwappDot11ClientMIBConfigGroup.setObjects(
    ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcKeyDecryptErrorEnabled")
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientMIBConfigGroup.setStatus("current")

ciscoLwappDot11ClientMIBStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 2, 2, 3)
)
ciscoLwappDot11ClientMIBStatusGroup.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWlanProfileName"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWgbStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWgbMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientProtocol"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcAssociationMode"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcApMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcIfType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientIPAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientNacState"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientQuarantineVLAN"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAccessVLAN"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAuthMode"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientMIBStatusGroup.setStatus("current")

ciscoLwappDot11ClientMIBStatusGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 2, 2, 4)
)
ciscoLwappDot11ClientMIBStatusGroupRev2.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientLoginTime"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientUpTime"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPowerSaveMode"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientCurrentTxRateSet"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataRateSet"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientHreapApAuth"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClient80211uCapable"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataRetries"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRtsRetries"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDuplicatePackets"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDecryptFailures"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMicErrors"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMicMissingFrames"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientIPAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientNacState"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientQuarantineVLAN"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAccessVLAN"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPostureState"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAclName"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAclApplied"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRedirectUrl"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAaaOverrideAclName"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAaaOverrideAclApplied"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientUsername"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSSID"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientMIBStatusGroupRev2.setStatus("current")

ciscoLwappDot11ClientMIBNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 2, 2, 6)
)
ciscoLwappDot11ClientMIBNotifControlGroup.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcAssocNacAlertEnabled"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcDisassocNacAlertEnabled"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcMovedToRunStateEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientMIBNotifControlGroup.setStatus("current")


# Notification objects

ciscoLwappDot11ClientKeyDecryptError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 0, 1)
)
ciscoLwappDot11ClientKeyDecryptError.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcAssociationMode"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcApMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcIfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAuthMode"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientKeyDecryptError.setStatus(
        "current"
    )

ciscoLwappDot11ClientAssocNacAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 0, 2)
)
ciscoLwappDot11ClientAssocNacAlert.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWlanProfileName"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientIPAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcApMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientQuarantineVLAN"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAccessVLAN"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAuthMode"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientAssocNacAlert.setStatus(
        "current"
    )

ciscoLwappDot11ClientDisassocNacAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 0, 3)
)
ciscoLwappDot11ClientDisassocNacAlert.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWlanProfileName"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientIPAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcApMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientQuarantineVLAN"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAccessVLAN"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientDisassocNacAlert.setStatus(
        "current"
    )

ciscoLwappDot11ClientMovedToRunState = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 0, 4)
)
ciscoLwappDot11ClientMovedToRunState.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientIPAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientUsername"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSSID"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientMovedToRunState.setStatus(
        "current"
    )

ciscoLwappDot11ClientStaticIpFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 0, 5)
)
ciscoLwappDot11ClientStaticIpFailTrap.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientIPAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientStaticIpFailTrap.setStatus(
        "current"
    )

ciscoLwappDot11ClientDisassocDataStatsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 0, 6)
)
ciscoLwappDot11ClientDisassocDataStatsTrap.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddressType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcApMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientReasonCode"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientUsername"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSSID"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSessionID"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientTxDataPackets"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientTxDataBytes"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRxDataPackets"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRxDataBytes"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientDisassocDataStatsTrap.setStatus(
        "current"
    )

ciscoLwappDot11ClientAssocDataStatsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 0, 7)
)
ciscoLwappDot11ClientAssocDataStatsTrap.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddressType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcApMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientUsername"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientApRoamMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSSID"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientTxDataPackets"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientTxDataBytes"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRxDataPackets"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRxDataBytes"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientAssocDataStatsTrap.setStatus(
        "current"
    )

ciscoLwappDot11ClientSessionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 0, 8)
)
ciscoLwappDot11ClientSessionTrap.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddressType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientUsername"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSSID"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSessionID"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcApMacAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientSessionTrap.setStatus(
        "current"
    )

ciscoLwappDot11ClientAssocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 0, 9)
)
ciscoLwappDot11ClientAssocTrap.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientTrapEventTime"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddressType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPolicyType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAID"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSSID"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAuthenticationAlgorithm"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientEncryptionCypher"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPortNumber"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAnchorAddressType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAnchorAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientEssIndex"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWlanProfileName"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWgbStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWgbMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientCcxVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientE2eVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientInterface"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClient80211uCapable"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMobilityStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRSSI"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSNR"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSecurityPolicyStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientLoginTime"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAssocTime"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientCurrentTxRateSet"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataRateSet"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientHreapApAuth"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldccCcxFoundationServiceVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldccCcxLocationServiceVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldccCcxVoiceServiceVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldccCcxManagementServiceVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataSwitching"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAuthentication"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioChannelNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfLoadChannelUtilization"),
        ("CISCO-LWAPP-AP-MIB", "cLApLocation"),
        ("CISCO-LWAPP-AP-MIB", "cLAPGroupVlanName"),
        ("CISCO-LWAPP-AP-MIB", "cLApSubMode"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientIPAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSessionId"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientVlanId"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientProtocol"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientEapType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPolicyErrors"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataRetries"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRtsRetries"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataBytesSent"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataBytesReceived"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataPacketsSent"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataPacketsReceived"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientTxDataBytesDropped"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRxDataBytesDropped"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientTxDataPacketsDropped"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRxDataPacketsDropped"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientAssocTrap.setStatus(
        "current"
    )

ciscoLwappDot11ClientDeAuthenticatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 0, 10)
)
ciscoLwappDot11ClientDeAuthenticatedTrap.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientTrapEventTime"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientUpTime"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddressType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPostureState"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientProtocol"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientVlanId"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPolicyType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientEapType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAID"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSSID"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAuthenticationAlgorithm"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWepState"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientEncryptionCypher"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPortNumber"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAnchorAddressType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAnchorAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientEssIndex"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWlanProfileName"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWgbStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWgbMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientCcxVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientE2eVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientInterface"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClient80211uCapable"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMobilityStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRSSI"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSNR"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataRetries"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRtsRetries"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientUsername"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcDOT11ClientReasonCode"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientStatusCode"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDeleteAction"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSecurityPolicyStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientNacState"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientLoginTime"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAssocTime"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientCurrentTxRateSet"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataRateSet"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientHreapApAuth"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldccCcxFoundationServiceVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldccCcxLocationServiceVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldccCcxVoiceServiceVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldccCcxManagementServiceVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataSwitching"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAuthentication"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddressDiscoverType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddressLastSeen"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPowerSaveMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioChannelNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfLoadChannelUtilization"),
        ("CISCO-LWAPP-AP-MIB", "cLApLocation"),
        ("CISCO-LWAPP-AP-MIB", "cLAPGroupVlanName"),
        ("CISCO-LWAPP-AP-MIB", "cLApSubMode"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientIPAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPolicyErrors"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPolicyManagerState"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataBytesSent"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataBytesReceived"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataPacketsSent"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataPacketsReceived"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientTxDataBytesDropped"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRxDataBytesDropped"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientTxDataPacketsDropped"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRxDataPacketsDropped"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSessionId"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientDeAuthenticatedTrap.setStatus(
        "current"
    )

ciscoLwappDot11ClientMovedToRunStateNewTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 0, 11)
)
ciscoLwappDot11ClientMovedToRunStateNewTrap.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientTrapEventTime"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddressType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPostureState"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientProtocol"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientVlanId"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPolicyType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientEapType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAID"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWlanProfileName"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAuthenticationAlgorithm"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWepState"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientEncryptionCypher"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPortNumber"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAnchorAddressType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAnchorAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientEssIndex"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWgbStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWgbMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientCcxVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientE2eVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClient80211uCapable"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMobilityStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRSSI"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSNR"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataRetries"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRtsRetries"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientUsername"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientStatusCode"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSecurityPolicyStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientNacState"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientLoginTime"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataRateSet"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientHreapApAuth"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldccCcxFoundationServiceVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldccCcxLocationServiceVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldccCcxVoiceServiceVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldccCcxManagementServiceVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataSwitching"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAuthentication"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddressDiscoverType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddressLastSeen"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPowerSaveMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioChannelNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfLoadChannelUtilization"),
        ("CISCO-LWAPP-AP-MIB", "cLApSubMode"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientIPAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPolicyManagerState"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPmipNai"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPmipState"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPmipInterface"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPmipHomeAddrType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPmipHomeAddr"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPmipAtt"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPmipLocalLinkId"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPmipDomainName"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPmipLmaName"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPmipUpKey"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPmipDownKey"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPmipLifeTime"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAnchorMCPrivateAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAnchorMCPrivateAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAssociatedMAAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAssociatedMAAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAssociatedMCAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAssociatedMCAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAssociatedMCGroupId"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAnchorMCGroupId"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPmipDataValid"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMobilityExtDataValid"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSessionId"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientMovedToRunStateNewTrap.setStatus(
        "current"
    )

ciscoLwappDot11ClientMobilityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 0, 12)
)
ciscoLwappDot11ClientMobilityTrap.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientTrapEventTime"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientUpTime"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddressType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPostureState"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientProtocol"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientVlanId"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPolicyType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientEapType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAID"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSSID"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAuthenticationAlgorithm"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWepState"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientEncryptionCypher"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPortNumber"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAnchorAddressType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAnchorAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientEssIndex"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWlanProfileName"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWgbStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientWgbMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientCcxVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientE2eVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientInterface"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClient80211uCapable"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMobilityStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRSSI"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSNR"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataRetries"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRtsRetries"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientUsername"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcDOT11ClientReasonCode"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientStatusCode"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDeleteAction"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSecurityPolicyStatus"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientNacState"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientLoginTime"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAssocTime"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientCurrentTxRateSet"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataRateSet"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientHreapApAuth"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldccCcxFoundationServiceVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldccCcxLocationServiceVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldccCcxVoiceServiceVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldccCcxManagementServiceVersion"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataSwitching"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientAuthentication"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddressDiscoverType"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientByIpAddressLastSeen"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPowerSaveMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioChannelNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfLoadChannelUtilization"),
        ("CISCO-LWAPP-AP-MIB", "cLApLocation"),
        ("CISCO-LWAPP-AP-MIB", "cLAPGroupVlanName"),
        ("CISCO-LWAPP-AP-MIB", "cLApSubMode"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientIPAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPolicyErrors"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientPolicyManagerState"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataBytesSent"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataBytesReceived"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataPacketsSent"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientDataPacketsReceived"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientTxDataBytesDropped"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRxDataBytesDropped"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientTxDataPacketsDropped"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientRxDataPacketsDropped"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientSessionId"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientMobilityTrap.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappDot11ClientMIBNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 2, 2, 2)
)
ciscoLwappDot11ClientMIBNotifsGroup.setObjects(
    ("CISCO-LWAPP-DOT11-CLIENT-MIB", "ciscoLwappDot11ClientKeyDecryptError")
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientMIBNotifsGroup.setStatus(
        "current"
    )

ciscoLwappDot11ClientMIBNotifsGroupRev2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 2, 2, 5)
)
ciscoLwappDot11ClientMIBNotifsGroupRev2.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "ciscoLwappDot11ClientAssocNacAlert"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "ciscoLwappDot11ClientDisassocNacAlert"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "ciscoLwappDot11ClientMovedToRunState"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientMIBNotifsGroupRev2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappDot11ClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappDot11ClientMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    **{"ciscoLwappDot11ClientMIB": ciscoLwappDot11ClientMIB,
       "ciscoLwappDot11ClientMIBNotifs": ciscoLwappDot11ClientMIBNotifs,
       "ciscoLwappDot11ClientKeyDecryptError": ciscoLwappDot11ClientKeyDecryptError,
       "ciscoLwappDot11ClientAssocNacAlert": ciscoLwappDot11ClientAssocNacAlert,
       "ciscoLwappDot11ClientDisassocNacAlert": ciscoLwappDot11ClientDisassocNacAlert,
       "ciscoLwappDot11ClientMovedToRunState": ciscoLwappDot11ClientMovedToRunState,
       "ciscoLwappDot11ClientStaticIpFailTrap": ciscoLwappDot11ClientStaticIpFailTrap,
       "ciscoLwappDot11ClientDisassocDataStatsTrap": ciscoLwappDot11ClientDisassocDataStatsTrap,
       "ciscoLwappDot11ClientAssocDataStatsTrap": ciscoLwappDot11ClientAssocDataStatsTrap,
       "ciscoLwappDot11ClientSessionTrap": ciscoLwappDot11ClientSessionTrap,
       "ciscoLwappDot11ClientAssocTrap": ciscoLwappDot11ClientAssocTrap,
       "ciscoLwappDot11ClientDeAuthenticatedTrap": ciscoLwappDot11ClientDeAuthenticatedTrap,
       "ciscoLwappDot11ClientMovedToRunStateNewTrap": ciscoLwappDot11ClientMovedToRunStateNewTrap,
       "ciscoLwappDot11ClientMobilityTrap": ciscoLwappDot11ClientMobilityTrap,
       "ciscoLwappDot11ClientMIBObjects": ciscoLwappDot11ClientMIBObjects,
       "cldcConfigObjects": cldcConfigObjects,
       "cldcKeyDecryptErrorEnabled": cldcKeyDecryptErrorEnabled,
       "cldcAssocNacAlertEnabled": cldcAssocNacAlertEnabled,
       "cldcDisassocNacAlertEnabled": cldcDisassocNacAlertEnabled,
       "cldcMovedToRunStateEnabled": cldcMovedToRunStateEnabled,
       "ciscoLwappDot11ClientStaticIpFailTrapEnabled": ciscoLwappDot11ClientStaticIpFailTrapEnabled,
       "cldcNotifObjects": cldcNotifObjects,
       "cldcClientRSSI": cldcClientRSSI,
       "cldcClientSNR": cldcClientSNR,
       "cldcDOT11ClientReasonCode": cldcDOT11ClientReasonCode,
       "cldcDOT11ClientTxDataPackets": cldcDOT11ClientTxDataPackets,
       "cldcDOT11ClientTxDataBytes": cldcDOT11ClientTxDataBytes,
       "cldcDOT11ClientRxDataPackets": cldcDOT11ClientRxDataPackets,
       "cldcDOT11ClientRxDataBytes": cldcDOT11ClientRxDataBytes,
       "cldcClientVlanId": cldcClientVlanId,
       "cldcClientPolicyType": cldcClientPolicyType,
       "cldcClientEapType": cldcClientEapType,
       "cldcClientAID": cldcClientAID,
       "cldcClientAuthenticationAlgorithm": cldcClientAuthenticationAlgorithm,
       "cldcClientWepState": cldcClientWepState,
       "cldcClientEncryptionCypher": cldcClientEncryptionCypher,
       "cldcClientPortNumber": cldcClientPortNumber,
       "cldcClientAnchorAddressType": cldcClientAnchorAddressType,
       "cldcClientAnchorAddress": cldcClientAnchorAddress,
       "cldcClientEssIndex": cldcClientEssIndex,
       "cldcClientCcxVersion": cldcClientCcxVersion,
       "cldcClientE2eVersion": cldcClientE2eVersion,
       "cldcClientInterface": cldcClientInterface,
       "cldcClientMobilityStatus": cldcClientMobilityStatus,
       "cldcClientStatusCode": cldcClientStatusCode,
       "cldcClientDeleteAction": cldcClientDeleteAction,
       "cldcClientSecurityPolicyStatus": cldcClientSecurityPolicyStatus,
       "cldcClientTrapEventTime": cldcClientTrapEventTime,
       "cldcClientPolicyManagerState": cldcClientPolicyManagerState,
       "cldcClientAssocTime": cldcClientAssocTime,
       "cldcClientPmipDataValid": cldcClientPmipDataValid,
       "cldcClientMobilityExtDataValid": cldcClientMobilityExtDataValid,
       "cldcClientPolicyErrors": cldcClientPolicyErrors,
       "cldcClientSessionId": cldcClientSessionId,
       "cldcClientPmipNai": cldcClientPmipNai,
       "cldcClientPmipState": cldcClientPmipState,
       "cldcClientPmipInterface": cldcClientPmipInterface,
       "cldcClientPmipHomeAddrType": cldcClientPmipHomeAddrType,
       "cldcClientPmipHomeAddr": cldcClientPmipHomeAddr,
       "cldcClientPmipAtt": cldcClientPmipAtt,
       "cldcClientPmipLocalLinkId": cldcClientPmipLocalLinkId,
       "cldcClientPmipLmaName": cldcClientPmipLmaName,
       "cldcClientPmipLifeTime": cldcClientPmipLifeTime,
       "cldcClientPmipDomainName": cldcClientPmipDomainName,
       "cldcClientPmipUpKey": cldcClientPmipUpKey,
       "cldcClientPmipDownKey": cldcClientPmipDownKey,
       "cldcStatusObjects": cldcStatusObjects,
       "cldcClientTable": cldcClientTable,
       "cldcClientEntry": cldcClientEntry,
       "cldcClientMacAddress": cldcClientMacAddress,
       "cldcClientStatus": cldcClientStatus,
       "cldcClientWlanProfileName": cldcClientWlanProfileName,
       "cldcClientWgbStatus": cldcClientWgbStatus,
       "cldcClientWgbMacAddress": cldcClientWgbMacAddress,
       "cldcClientProtocol": cldcClientProtocol,
       "cldcAssociationMode": cldcAssociationMode,
       "cldcApMacAddress": cldcApMacAddress,
       "cldcIfType": cldcIfType,
       "cldcClientIPAddress": cldcClientIPAddress,
       "cldcClientNacState": cldcClientNacState,
       "cldcClientQuarantineVLAN": cldcClientQuarantineVLAN,
       "cldcClientAccessVLAN": cldcClientAccessVLAN,
       "cldcClientLoginTime": cldcClientLoginTime,
       "cldcClientUpTime": cldcClientUpTime,
       "cldcClientPowerSaveMode": cldcClientPowerSaveMode,
       "cldcClientCurrentTxRateSet": cldcClientCurrentTxRateSet,
       "cldcClientDataRateSet": cldcClientDataRateSet,
       "cldcClientHreapApAuth": cldcClientHreapApAuth,
       "cldcClient80211uCapable": cldcClient80211uCapable,
       "cldcClientPostureState": cldcClientPostureState,
       "cldcClientAclName": cldcClientAclName,
       "cldcClientAclApplied": cldcClientAclApplied,
       "cldcClientRedirectUrl": cldcClientRedirectUrl,
       "cldcClientAaaOverrideAclName": cldcClientAaaOverrideAclName,
       "cldcClientAaaOverrideAclApplied": cldcClientAaaOverrideAclApplied,
       "cldcClientUsername": cldcClientUsername,
       "cldcClientSSID": cldcClientSSID,
       "cldcClientSecurityTagId": cldcClientSecurityTagId,
       "cldcClientTypeKTS": cldcClientTypeKTS,
       "cldcClientIpv6AclName": cldcClientIpv6AclName,
       "cldcClientIpv6AclApplied": cldcClientIpv6AclApplied,
       "cldcClientDataSwitching": cldcClientDataSwitching,
       "cldcClientAuthentication": cldcClientAuthentication,
       "cldcClientChannel": cldcClientChannel,
       "cldcClientAuthMode": cldcClientAuthMode,
       "cldcClientReasonCode": cldcClientReasonCode,
       "cldcClientSessionID": cldcClientSessionID,
       "cldcClientApRoamMacAddress": cldcClientApRoamMacAddress,
       "cldcClientMdnsProfile": cldcClientMdnsProfile,
       "cldcClientMdnsAdvCount": cldcClientMdnsAdvCount,
       "cldcClientPolicyName": cldcClientPolicyName,
       "cldcClientAAARole": cldcClientAAARole,
       "cldcClientDeviceType": cldcClientDeviceType,
       "cldcUserAuthType": cldcUserAuthType,
       "cldcClientByIpTable": cldcClientByIpTable,
       "cldcClientByIpEntry": cldcClientByIpEntry,
       "cldcClientByIpAddressType": cldcClientByIpAddressType,
       "cldcClientByIpAddress": cldcClientByIpAddress,
       "cldcClientByIpAddressDiscoverType": cldcClientByIpAddressDiscoverType,
       "cldcClientByIpAddressLastSeen": cldcClientByIpAddressLastSeen,
       "cldcSleepingClientTable": cldcSleepingClientTable,
       "cldcSleepingClientEntry": cldcSleepingClientEntry,
       "cldcSleepingClientMacAddress": cldcSleepingClientMacAddress,
       "cldcSleepingClientSsid": cldcSleepingClientSsid,
       "cldcSleepingClientUserName": cldcSleepingClientUserName,
       "cldcSleepingClientRemainingTime": cldcSleepingClientRemainingTime,
       "cldcSleepingClientRowStatus": cldcSleepingClientRowStatus,
       "cldcStatisticObjects": cldcStatisticObjects,
       "cldcClientStatisticTable": cldcClientStatisticTable,
       "cldcClientStatisticEntry": cldcClientStatisticEntry,
       "cldcClientDataRetries": cldcClientDataRetries,
       "cldcClientRtsRetries": cldcClientRtsRetries,
       "cldcClientDuplicatePackets": cldcClientDuplicatePackets,
       "cldcClientDecryptFailures": cldcClientDecryptFailures,
       "cldcClientMicErrors": cldcClientMicErrors,
       "cldcClientMicMissingFrames": cldcClientMicMissingFrames,
       "cldcClientRaPacketsDropped": cldcClientRaPacketsDropped,
       "cldcClientInterimUpdatesCount": cldcClientInterimUpdatesCount,
       "cldcClientDataBytesReceived": cldcClientDataBytesReceived,
       "cldcClientRealtimeBytesReceived": cldcClientRealtimeBytesReceived,
       "cldcClientRxDataBytesDropped": cldcClientRxDataBytesDropped,
       "cldcClientRxRealtimeBytesDropped": cldcClientRxRealtimeBytesDropped,
       "cldcClientDataBytesSent": cldcClientDataBytesSent,
       "cldcClientRealtimeBytesSent": cldcClientRealtimeBytesSent,
       "cldcClientTxDataBytesDropped": cldcClientTxDataBytesDropped,
       "cldcClientTxRealtimeBytesDropped": cldcClientTxRealtimeBytesDropped,
       "cldcClientDataPacketsReceived": cldcClientDataPacketsReceived,
       "cldcClientRealtimePacketsReceived": cldcClientRealtimePacketsReceived,
       "cldcClientRxDataPacketsDropped": cldcClientRxDataPacketsDropped,
       "cldcClientRxRealtimePacketsDropped": cldcClientRxRealtimePacketsDropped,
       "cldcClientDataPacketsSent": cldcClientDataPacketsSent,
       "cldcClientRealtimePacketsSent": cldcClientRealtimePacketsSent,
       "cldcClientTxDataPacketsDropped": cldcClientTxDataPacketsDropped,
       "cldcClientTxRealtimePacketsDropped": cldcClientTxRealtimePacketsDropped,
       "cldcClientTxDataPackets": cldcClientTxDataPackets,
       "cldcClientTxDataBytes": cldcClientTxDataBytes,
       "cldcClientRxDataPackets": cldcClientRxDataPackets,
       "cldcClientRxDataBytes": cldcClientRxDataBytes,
       "ciscoLwappDot11ClientMIBConform": ciscoLwappDot11ClientMIBConform,
       "ciscoLwappDot11ClientMIBCompliances": ciscoLwappDot11ClientMIBCompliances,
       "ciscoLwappDot11ClientMIBCompliance": ciscoLwappDot11ClientMIBCompliance,
       "ciscoLwappDot11ClientMIBComplianceRev2": ciscoLwappDot11ClientMIBComplianceRev2,
       "ciscoLwappDot11ClientMIBGroups": ciscoLwappDot11ClientMIBGroups,
       "ciscoLwappDot11ClientMIBConfigGroup": ciscoLwappDot11ClientMIBConfigGroup,
       "ciscoLwappDot11ClientMIBNotifsGroup": ciscoLwappDot11ClientMIBNotifsGroup,
       "ciscoLwappDot11ClientMIBStatusGroup": ciscoLwappDot11ClientMIBStatusGroup,
       "ciscoLwappDot11ClientMIBStatusGroupRev2": ciscoLwappDot11ClientMIBStatusGroupRev2,
       "ciscoLwappDot11ClientMIBNotifsGroupRev2": ciscoLwappDot11ClientMIBNotifsGroupRev2,
       "ciscoLwappDot11ClientMIBNotifControlGroup": ciscoLwappDot11ClientMIBNotifControlGroup,
       "ciscoLwappDot11ClientCcxMIBObjects": ciscoLwappDot11ClientCcxMIBObjects,
       "cldcCcxObjects": cldcCcxObjects,
       "cldccCcxVersionInfoTable": cldccCcxVersionInfoTable,
       "cldccCcxVersionInfoEntry": cldccCcxVersionInfoEntry,
       "cldccCcxFoundationServiceVersion": cldccCcxFoundationServiceVersion,
       "cldccCcxLocationServiceVersion": cldccCcxLocationServiceVersion,
       "cldccCcxVoiceServiceVersion": cldccCcxVoiceServiceVersion,
       "cldccCcxManagementServiceVersion": cldccCcxManagementServiceVersion}
)
