# SNMP MIB module (TRAPEZE-NETWORKS-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:39 2024
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

(InetAddress,
 InetAddressIPv4,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressType")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(TrpzAccessType,
 TrpzApAttachType,
 TrpzApConnectSecurityType,
 TrpzApFailDetail,
 TrpzApFingerprint,
 TrpzApNum,
 TrpzApPortOrDapNum,
 TrpzApRadioIndex,
 TrpzApSerialNum,
 TrpzApServiceAvailability,
 TrpzApTransition,
 TrpzApWasOperational,
 TrpzChannelChangeType,
 TrpzChannelNum,
 TrpzCryptoType,
 TrpzPowerLevel,
 TrpzRadioChannelWidth,
 TrpzRadioConfigState,
 TrpzRadioMimoState,
 TrpzRadioMode,
 TrpzRadioNum,
 TrpzRadioPowerChangeType,
 TrpzRadioType,
 TrpzRssi) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-AP-TC",
    "TrpzAccessType",
    "TrpzApAttachType",
    "TrpzApConnectSecurityType",
    "TrpzApFailDetail",
    "TrpzApFingerprint",
    "TrpzApNum",
    "TrpzApPortOrDapNum",
    "TrpzApRadioIndex",
    "TrpzApSerialNum",
    "TrpzApServiceAvailability",
    "TrpzApTransition",
    "TrpzApWasOperational",
    "TrpzChannelChangeType",
    "TrpzChannelNum",
    "TrpzCryptoType",
    "TrpzPowerLevel",
    "TrpzRadioChannelWidth",
    "TrpzRadioConfigState",
    "TrpzRadioMimoState",
    "TrpzRadioMode",
    "TrpzRadioNum",
    "TrpzRadioPowerChangeType",
    "TrpzRadioType",
    "TrpzRssi")

(TrpzIpPort,
 TrpzPhysPortNumberOrZero) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-BASIC-TC",
    "TrpzIpPort",
    "TrpzPhysPortNumberOrZero")

(TrpzClientAccessMode,
 TrpzClientAuthenProtocolType,
 TrpzClientDeviceGroupName,
 TrpzClientDeviceProfileName,
 TrpzClientDeviceType,
 TrpzClientDot1xState,
 TrpzClientSessionState,
 TrpzUserAccessType) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-CLIENT-SESSION-TC",
    "TrpzClientAccessMode",
    "TrpzClientAuthenProtocolType",
    "TrpzClientDeviceGroupName",
    "TrpzClientDeviceProfileName",
    "TrpzClientDeviceType",
    "TrpzClientDot1xState",
    "TrpzClientSessionState",
    "TrpzUserAccessType")

(TrpzRFDetectClassificationReason,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-RF-DETECT-TC",
    "TrpzRFDetectClassificationReason")

(TrpzRFNoiseSourceID,
 TrpzRFNoiseSourceType) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-RF-NOISE-TC-MIB",
    "TrpzRFNoiseSourceID",
    "TrpzRFNoiseSourceType")

(trpzMibs,
 trpzTemporary,
 trpzTraps) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs",
    "trpzTemporary",
    "trpzTraps")


# MODULE-IDENTITY

trpzTrapMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 1)
)
trpzTrapMib.setRevisions(
        ("2012-07-31 04:06",
         "2012-04-20 04:05",
         "2012-04-09 04:03",
         "2012-03-15 03:10",
         "2011-10-18 03:00",
         "2011-01-11 02:50",
         "2010-12-21 02:40",
         "2010-12-21 02:28",
         "2008-12-19 02:27",
         "2008-10-30 02:25",
         "2008-05-15 02:15",
         "2008-05-07 02:12",
         "2008-04-22 02:02",
         "2008-04-10 02:01",
         "2008-04-08 01:58",
         "2008-02-18 01:57",
         "2007-12-03 01:53",
         "2007-11-15 01:52",
         "2007-11-01 01:45",
         "2007-10-01 01:41",
         "2007-08-31 01:40",
         "2007-08-24 01:22",
         "2007-07-06 01:10",
         "2007-06-05 01:07",
         "2007-05-17 01:06",
         "2007-05-04 01:03",
         "2007-04-19 01:00",
         "2007-03-27 00:54",
         "2007-02-15 00:53",
         "2007-01-09 00:52",
         "2007-01-09 00:51",
         "2007-01-09 00:50",
         "2006-09-28 00:45",
         "2006-08-08 00:42",
         "2006-07-31 00:40",
         "2006-07-28 00:32",
         "2006-07-23 00:29",
         "2006-07-12 00:28",
         "2006-07-07 00:26",
         "2006-07-07 00:25",
         "2006-07-06 00:23",
         "2006-04-19 00:22",
         "2006-04-19 00:21",
         "2005-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TrpzAssociationFailureType(Integer32, TextualConvention):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("bad-assoc-request", 10),
          ("cipher-mismatch", 8),
          ("cipher-rejected", 7),
          ("dot1x", 4),
          ("glare", 6),
          ("load-balance", 2),
          ("no-prev-assoc", 5),
          ("other", 1),
          ("out-of-memory", 11),
          ("quiet-period", 3),
          ("roam-in-progress", 13),
          ("tkip-cm-active", 12),
          ("wep-not-configured", 9))
    )



class TrpzAuthenticationFailureType(Integer32, TextualConvention):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("all-servers-down", 8),
          ("authentication-type-mismatch", 9),
          ("exceeded-max-attempts", 13),
          ("fallthru-auth-misconfig", 11),
          ("invalid-password", 4),
          ("local-certificate-error", 7),
          ("no-lastresort-auth", 12),
          ("other", 1),
          ("password-expired", 14),
          ("server-rejected", 10),
          ("server-timeout", 5),
          ("signature-failed", 6),
          ("user-does-not-exist", 3),
          ("user-glob-mismatch", 2))
    )



class TrpzAuthorizationFailureType(Integer32, TextualConvention):
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
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("acl-mismatch", 6),
          ("crypto-type-mismatch", 8),
          ("end-date-mismatch", 11),
          ("location-policy", 3),
          ("mobility-profile-mismatch", 9),
          ("other", 1),
          ("qos-profile-mismatch", 14),
          ("simultaneous-logins", 15),
          ("ssid-defaults", 13),
          ("ssid-mismatch", 5),
          ("start-date-mismatch", 10),
          ("svr-type-mismatch", 12),
          ("timeofday-mismatch", 7),
          ("user-param", 2),
          ("vlan-tunnel-failure", 4))
    )



class TrpzDot1xFailureType(Integer32, TextualConvention):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("administrative-kill", 3),
          ("bad-rsnie", 4),
          ("bonded-auth-failure", 9),
          ("cert-not-installed", 13),
          ("force-unauth-configured", 12),
          ("fourway-hs-failure", 7),
          ("gkhs-failure", 11),
          ("max-sessions-exceeded", 6),
          ("other", 1),
          ("quiet-period", 2),
          ("reauth-disabled", 10),
          ("timeout", 5),
          ("user-glob-mismatch", 8))
    )



class TrpzRFDetectDoSType(Integer32, TextualConvention):
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("adhoc-client-frame", 20),
          ("associate-pkt-flood", 21),
          ("auth-flood", 2),
          ("bcast-deauth", 11),
          ("bssid-spoof", 24),
          ("de-associate-pkt-flood", 23),
          ("deauth-spoof", 14),
          ("decrypt-err", 15),
          ("disassoc-spoof", 13),
          ("fakeap-bssid", 10),
          ("fakeap-ssid", 9),
          ("mgmt-6-flood", 4),
          ("mgmt-7-flood", 5),
          ("mgmt-d-flood", 6),
          ("mgmt-e-flood", 7),
          ("mgmt-f-flood", 8),
          ("netstumbler", 18),
          ("null-data-flood", 3),
          ("null-probe-resp", 12),
          ("probe-flood", 1),
          ("re-associate-pkt-flood", 22),
          ("weak-wep-iv", 16),
          ("wellenreiter", 19),
          ("wireless-bridge", 17))
    )



class TrpzClientIpAddrChangeReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("client-connected-ipv4", 1),
          ("dhcp-to-static", 3),
          ("ipv6-global-addr", 10),
          ("other", 2))
    )



class TrpzBlacklistingCause(Integer32, TextualConvention):
    status = "current"
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
        *(("bl-associate-pkt-flood", 2),
          ("bl-configured", 1),
          ("bl-de-associate-pkt-flood", 4),
          ("bl-re-associate-pkt-flood", 3))
    )



class TrpzUserAttributeList(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )



class TrpzSessionDisconnectType(Integer32, TextualConvention):
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
        *(("admin-disconnect", 2),
          ("dyn-auth-disconnect", 3),
          ("other", 1))
    )



class TrpzConfigSaveInitiatorType(Integer32, TextualConvention):
    status = "current"
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
        *(("cli-console", 2),
          ("cli-remote", 3),
          ("https", 4),
          ("other", 1),
          ("snmp-set", 5))
    )



class TrpzMichaelMICFailureCause(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected-by-ap", 1),
          ("detected-by-client", 2))
    )



class TrpzClientAuthorizationReason(Integer32, TextualConvention):
    status = "current"
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
        *(("new-client", 2),
          ("other", 1),
          ("re-auth", 3),
          ("roam", 4))
    )



class TrpzApMgrChangeReason(Integer32, TextualConvention):
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
        *(("failover", 2),
          ("load-balancing", 3),
          ("other", 1))
    )



class TrpzClientClearedReason(Integer32, TextualConvention):
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
        *(("backup-failure", 3),
          ("normal", 2),
          ("other", 1))
    )



class TrpzMobilityDomainResiliencyStatus(Integer32, TextualConvention):
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
        *(("degraded", 3),
          ("other", 1),
          ("resilient", 2))
    )



class TrpzClusterFailureReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("validation-error", 2))
    )



class TrpzMultimediaSignalingProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("sip", 2))
    )



class TrpzMultimediaCallFailureReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("resource-unavailable", 2))
    )



class TrpzMultimediaCallDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )



class TrpzWsTunnelLimitType(Integer32, TextualConvention):
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
        *(("ap-ws-tunnel-limit", 3),
          ("other", 1),
          ("platform-tunnel-limit", 2))
    )



class TrpzM2UConvNotPossibleReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("max-conv-limit", 2),
          ("other", 1))
    )



class TrpzRadioBand(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bandAN", 1),
          ("bandBGN", 2))
    )



class TrpzAutoTuneFailureReason(Integer32, TextualConvention):
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
        *(("ap-conn-lost", 2),
          ("other", 1),
          ("ws-conn-lost", 3))
    )



class TrpzClientDeviceProfileChangeReason(Integer32, TextualConvention):
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
        *(("aaa-policy", 2),
          ("device-type-changed", 3),
          ("other", 1))
    )



# MIB Managed Objects in the order of their OIDs

_TrpzDeviceId_Type = ObjectIdentifier
_TrpzDeviceId_Object = MibScalar
trpzDeviceId = _TrpzDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 1),
    _TrpzDeviceId_Type()
)
trpzDeviceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzDeviceId.setStatus("current")
_TrpzMobilityDomainIp_Type = IpAddress
_TrpzMobilityDomainIp_Object = MibScalar
trpzMobilityDomainIp = _TrpzMobilityDomainIp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 2),
    _TrpzMobilityDomainIp_Type()
)
trpzMobilityDomainIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMobilityDomainIp.setStatus("current")
_TrpzAPMACAddress_Type = MacAddress
_TrpzAPMACAddress_Object = MibScalar
trpzAPMACAddress = _TrpzAPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 3),
    _TrpzAPMACAddress_Type()
)
trpzAPMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzAPMACAddress.setStatus("current")
_TrpzClientMACAddress_Type = MacAddress
_TrpzClientMACAddress_Object = MibScalar
trpzClientMACAddress = _TrpzClientMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 4),
    _TrpzClientMACAddress_Type()
)
trpzClientMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientMACAddress.setStatus("current")
_TrpzRFDetectXmtrMacAddr_Type = MacAddress
_TrpzRFDetectXmtrMacAddr_Object = MibScalar
trpzRFDetectXmtrMacAddr = _TrpzRFDetectXmtrMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 5),
    _TrpzRFDetectXmtrMacAddr_Type()
)
trpzRFDetectXmtrMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRFDetectXmtrMacAddr.setStatus("current")


class _TrpzPortNum_Type(Integer32):
    """Custom type trpzPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 22),
    )


_TrpzPortNum_Type.__name__ = "Integer32"
_TrpzPortNum_Object = MibScalar
trpzPortNum = _TrpzPortNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 6),
    _TrpzPortNum_Type()
)
trpzPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzPortNum.setStatus("current")
_TrpzAPRadioNum_Type = TrpzRadioNum
_TrpzAPRadioNum_Object = MibScalar
trpzAPRadioNum = _TrpzAPRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 7),
    _TrpzAPRadioNum_Type()
)
trpzAPRadioNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzAPRadioNum.setStatus("current")


class _TrpzRadioRssi_Type(Integer32):
    """Custom type trpzRadioRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_TrpzRadioRssi_Type.__name__ = "Integer32"
_TrpzRadioRssi_Object = MibScalar
trpzRadioRssi = _TrpzRadioRssi_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 8),
    _TrpzRadioRssi_Type()
)
trpzRadioRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRadioRssi.setStatus("obsolete")


class _TrpzRadioBSSID_Type(OctetString):
    """Custom type trpzRadioBSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TrpzRadioBSSID_Type.__name__ = "OctetString"
_TrpzRadioBSSID_Object = MibScalar
trpzRadioBSSID = _TrpzRadioBSSID_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 9),
    _TrpzRadioBSSID_Type()
)
trpzRadioBSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRadioBSSID.setStatus("current")


class _TrpzUserName_Type(DisplayString):
    """Custom type trpzUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrpzUserName_Type.__name__ = "DisplayString"
_TrpzUserName_Object = MibScalar
trpzUserName = _TrpzUserName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 10),
    _TrpzUserName_Type()
)
trpzUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzUserName.setStatus("current")
_TrpzClientAuthServerIp_Type = IpAddress
_TrpzClientAuthServerIp_Object = MibScalar
trpzClientAuthServerIp = _TrpzClientAuthServerIp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 11),
    _TrpzClientAuthServerIp_Type()
)
trpzClientAuthServerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientAuthServerIp.setStatus("current")
_TrpzClientSessionState_Type = TrpzClientSessionState
_TrpzClientSessionState_Object = MibScalar
trpzClientSessionState = _TrpzClientSessionState_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 12),
    _TrpzClientSessionState_Type()
)
trpzClientSessionState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientSessionState.setStatus("current")


class _TrpzDAPNum_Type(Integer32):
    """Custom type trpzDAPNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TrpzDAPNum_Type.__name__ = "Integer32"
_TrpzDAPNum_Object = MibScalar
trpzDAPNum = _TrpzDAPNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 13),
    _TrpzDAPNum_Type()
)
trpzDAPNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzDAPNum.setStatus("current")
_TrpzClientIp_Type = IpAddress
_TrpzClientIp_Object = MibScalar
trpzClientIp = _TrpzClientIp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 14),
    _TrpzClientIp_Type()
)
trpzClientIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientIp.setStatus("obsolete")


class _TrpzClientSessionId_Type(DisplayString):
    """Custom type trpzClientSessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrpzClientSessionId_Type.__name__ = "DisplayString"
_TrpzClientSessionId_Object = MibScalar
trpzClientSessionId = _TrpzClientSessionId_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 15),
    _TrpzClientSessionId_Type()
)
trpzClientSessionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientSessionId.setStatus("current")
_TrpzClientAuthenProtocolType_Type = TrpzClientAuthenProtocolType
_TrpzClientAuthenProtocolType_Object = MibScalar
trpzClientAuthenProtocolType = _TrpzClientAuthenProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 16),
    _TrpzClientAuthenProtocolType_Type()
)
trpzClientAuthenProtocolType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientAuthenProtocolType.setStatus("current")


class _TrpzClientVLANName_Type(DisplayString):
    """Custom type trpzClientVLANName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrpzClientVLANName_Type.__name__ = "DisplayString"
_TrpzClientVLANName_Object = MibScalar
trpzClientVLANName = _TrpzClientVLANName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 17),
    _TrpzClientVLANName_Type()
)
trpzClientVLANName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientVLANName.setStatus("current")
_TrpzClientSessionStartTime_Type = TimeTicks
_TrpzClientSessionStartTime_Object = MibScalar
trpzClientSessionStartTime = _TrpzClientSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 18),
    _TrpzClientSessionStartTime_Type()
)
trpzClientSessionStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientSessionStartTime.setStatus("obsolete")


class _TrpzClientFailureCause_Type(DisplayString):
    """Custom type trpzClientFailureCause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzClientFailureCause_Type.__name__ = "DisplayString"
_TrpzClientFailureCause_Object = MibScalar
trpzClientFailureCause = _TrpzClientFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 19),
    _TrpzClientFailureCause_Type()
)
trpzClientFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientFailureCause.setStatus("current")


class _TrpzClientRoamedFromPortNum_Type(Integer32):
    """Custom type trpzClientRoamedFromPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TrpzClientRoamedFromPortNum_Type.__name__ = "Integer32"
_TrpzClientRoamedFromPortNum_Object = MibScalar
trpzClientRoamedFromPortNum = _TrpzClientRoamedFromPortNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 20),
    _TrpzClientRoamedFromPortNum_Type()
)
trpzClientRoamedFromPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientRoamedFromPortNum.setStatus("obsolete")
_TrpzClientRoamedFromRadioNum_Type = TrpzRadioNum
_TrpzClientRoamedFromRadioNum_Object = MibScalar
trpzClientRoamedFromRadioNum = _TrpzClientRoamedFromRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 21),
    _TrpzClientRoamedFromRadioNum_Type()
)
trpzClientRoamedFromRadioNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientRoamedFromRadioNum.setStatus("obsolete")


class _TrpzClientRoamedFromDAPNum_Type(Integer32):
    """Custom type trpzClientRoamedFromDAPNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TrpzClientRoamedFromDAPNum_Type.__name__ = "Integer32"
_TrpzClientRoamedFromDAPNum_Object = MibScalar
trpzClientRoamedFromDAPNum = _TrpzClientRoamedFromDAPNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 22),
    _TrpzClientRoamedFromDAPNum_Type()
)
trpzClientRoamedFromDAPNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientRoamedFromDAPNum.setStatus("obsolete")


class _TrpzUserParams_Type(DisplayString):
    """Custom type trpzUserParams based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzUserParams_Type.__name__ = "DisplayString"
_TrpzUserParams_Object = MibScalar
trpzUserParams = _TrpzUserParams_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 23),
    _TrpzUserParams_Type()
)
trpzUserParams.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzUserParams.setStatus("current")


class _TrpzClientLocationPolicyIndex_Type(Integer32):
    """Custom type trpzClientLocationPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_TrpzClientLocationPolicyIndex_Type.__name__ = "Integer32"
_TrpzClientLocationPolicyIndex_Object = MibScalar
trpzClientLocationPolicyIndex = _TrpzClientLocationPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 24),
    _TrpzClientLocationPolicyIndex_Type()
)
trpzClientLocationPolicyIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientLocationPolicyIndex.setStatus("current")
_TrpzClientAssociationFailureCause_Type = TrpzAssociationFailureType
_TrpzClientAssociationFailureCause_Object = MibScalar
trpzClientAssociationFailureCause = _TrpzClientAssociationFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 25),
    _TrpzClientAssociationFailureCause_Type()
)
trpzClientAssociationFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientAssociationFailureCause.setStatus("current")
_TrpzClientAuthenticationFailureCause_Type = TrpzAuthenticationFailureType
_TrpzClientAuthenticationFailureCause_Object = MibScalar
trpzClientAuthenticationFailureCause = _TrpzClientAuthenticationFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 26),
    _TrpzClientAuthenticationFailureCause_Type()
)
trpzClientAuthenticationFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientAuthenticationFailureCause.setStatus("current")
_TrpzClientAuthorizationFailureCause_Type = TrpzAuthorizationFailureType
_TrpzClientAuthorizationFailureCause_Object = MibScalar
trpzClientAuthorizationFailureCause = _TrpzClientAuthorizationFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 27),
    _TrpzClientAuthorizationFailureCause_Type()
)
trpzClientAuthorizationFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientAuthorizationFailureCause.setStatus("current")


class _TrpzClientFailureCauseDescription_Type(DisplayString):
    """Custom type trpzClientFailureCauseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzClientFailureCauseDescription_Type.__name__ = "DisplayString"
_TrpzClientFailureCauseDescription_Object = MibScalar
trpzClientFailureCauseDescription = _TrpzClientFailureCauseDescription_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 28),
    _TrpzClientFailureCauseDescription_Type()
)
trpzClientFailureCauseDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientFailureCauseDescription.setStatus("current")
_TrpzClientRoamedFromWsIp_Type = IpAddress
_TrpzClientRoamedFromWsIp_Object = MibScalar
trpzClientRoamedFromWsIp = _TrpzClientRoamedFromWsIp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 29),
    _TrpzClientRoamedFromWsIp_Type()
)
trpzClientRoamedFromWsIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientRoamedFromWsIp.setStatus("obsolete")
_TrpzClientRoamedFromAccessType_Type = TrpzAccessType
_TrpzClientRoamedFromAccessType_Object = MibScalar
trpzClientRoamedFromAccessType = _TrpzClientRoamedFromAccessType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 30),
    _TrpzClientRoamedFromAccessType_Type()
)
trpzClientRoamedFromAccessType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientRoamedFromAccessType.setStatus("obsolete")
_TrpzClientAccessType_Type = TrpzAccessType
_TrpzClientAccessType_Object = MibScalar
trpzClientAccessType = _TrpzClientAccessType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 31),
    _TrpzClientAccessType_Type()
)
trpzClientAccessType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientAccessType.setStatus("current")
_TrpzRadioMACAddress_Type = MacAddress
_TrpzRadioMACAddress_Object = MibScalar
trpzRadioMACAddress = _TrpzRadioMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 32),
    _TrpzRadioMACAddress_Type()
)
trpzRadioMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRadioMACAddress.setStatus("current")
_TrpzRadioPowerChangeReason_Type = TrpzRadioPowerChangeType
_TrpzRadioPowerChangeReason_Object = MibScalar
trpzRadioPowerChangeReason = _TrpzRadioPowerChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 33),
    _TrpzRadioPowerChangeReason_Type()
)
trpzRadioPowerChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRadioPowerChangeReason.setStatus("current")


class _TrpzNewChannelNum_Type(Integer32):
    """Custom type trpzNewChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_TrpzNewChannelNum_Type.__name__ = "Integer32"
_TrpzNewChannelNum_Object = MibScalar
trpzNewChannelNum = _TrpzNewChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 34),
    _TrpzNewChannelNum_Type()
)
trpzNewChannelNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzNewChannelNum.setStatus("current")


class _TrpzOldChannelNum_Type(Integer32):
    """Custom type trpzOldChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_TrpzOldChannelNum_Type.__name__ = "Integer32"
_TrpzOldChannelNum_Object = MibScalar
trpzOldChannelNum = _TrpzOldChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 35),
    _TrpzOldChannelNum_Type()
)
trpzOldChannelNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzOldChannelNum.setStatus("current")
_TrpzChannelChangeReason_Type = TrpzChannelChangeType
_TrpzChannelChangeReason_Object = MibScalar
trpzChannelChangeReason = _TrpzChannelChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 36),
    _TrpzChannelChangeReason_Type()
)
trpzChannelChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzChannelChangeReason.setStatus("current")


class _TrpzRFDetectListenerListInfo_Type(OctetString):
    """Custom type trpzRFDetectListenerListInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 571),
    )


_TrpzRFDetectListenerListInfo_Type.__name__ = "OctetString"
_TrpzRFDetectListenerListInfo_Object = MibScalar
trpzRFDetectListenerListInfo = _TrpzRFDetectListenerListInfo_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 37),
    _TrpzRFDetectListenerListInfo_Type()
)
trpzRFDetectListenerListInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRFDetectListenerListInfo.setStatus("current")


class _TrpzRadioSSID_Type(DisplayString):
    """Custom type trpzRadioSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrpzRadioSSID_Type.__name__ = "DisplayString"
_TrpzRadioSSID_Object = MibScalar
trpzRadioSSID = _TrpzRadioSSID_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 38),
    _TrpzRadioSSID_Type()
)
trpzRadioSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRadioSSID.setStatus("current")
_TrpzNewPowerLevel_Type = TrpzPowerLevel
_TrpzNewPowerLevel_Object = MibScalar
trpzNewPowerLevel = _TrpzNewPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 39),
    _TrpzNewPowerLevel_Type()
)
trpzNewPowerLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzNewPowerLevel.setStatus("current")
_TrpzOldPowerLevel_Type = TrpzPowerLevel
_TrpzOldPowerLevel_Object = MibScalar
trpzOldPowerLevel = _TrpzOldPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 40),
    _TrpzOldPowerLevel_Type()
)
trpzOldPowerLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzOldPowerLevel.setStatus("current")


class _TrpzRadioPowerChangeDescription_Type(DisplayString):
    """Custom type trpzRadioPowerChangeDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzRadioPowerChangeDescription_Type.__name__ = "DisplayString"
_TrpzRadioPowerChangeDescription_Object = MibScalar
trpzRadioPowerChangeDescription = _TrpzRadioPowerChangeDescription_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 41),
    _TrpzRadioPowerChangeDescription_Type()
)
trpzRadioPowerChangeDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRadioPowerChangeDescription.setStatus("current")


class _TrpzCounterMeasurePerformerListInfo_Type(DisplayString):
    """Custom type trpzCounterMeasurePerformerListInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzCounterMeasurePerformerListInfo_Type.__name__ = "DisplayString"
_TrpzCounterMeasurePerformerListInfo_Object = MibScalar
trpzCounterMeasurePerformerListInfo = _TrpzCounterMeasurePerformerListInfo_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 42),
    _TrpzCounterMeasurePerformerListInfo_Type()
)
trpzCounterMeasurePerformerListInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzCounterMeasurePerformerListInfo.setStatus("obsolete")
_TrpzClientDot1xState_Type = TrpzClientDot1xState
_TrpzClientDot1xState_Object = MibScalar
trpzClientDot1xState = _TrpzClientDot1xState_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 43),
    _TrpzClientDot1xState_Type()
)
trpzClientDot1xState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientDot1xState.setStatus("current")
_TrpzClientDot1xFailureCause_Type = TrpzDot1xFailureType
_TrpzClientDot1xFailureCause_Object = MibScalar
trpzClientDot1xFailureCause = _TrpzClientDot1xFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 44),
    _TrpzClientDot1xFailureCause_Type()
)
trpzClientDot1xFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientDot1xFailureCause.setStatus("current")
_TrpzAPAccessType_Type = TrpzAccessType
_TrpzAPAccessType_Object = MibScalar
trpzAPAccessType = _TrpzAPAccessType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 45),
    _TrpzAPAccessType_Type()
)
trpzAPAccessType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzAPAccessType.setStatus("obsolete")
_TrpzUserAccessType_Type = TrpzUserAccessType
_TrpzUserAccessType_Object = MibScalar
trpzUserAccessType = _TrpzUserAccessType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 46),
    _TrpzUserAccessType_Type()
)
trpzUserAccessType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzUserAccessType.setStatus("current")
_TrpzClientSessionElapsedTime_Type = TimeTicks
_TrpzClientSessionElapsedTime_Object = MibScalar
trpzClientSessionElapsedTime = _TrpzClientSessionElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 47),
    _TrpzClientSessionElapsedTime_Type()
)
trpzClientSessionElapsedTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientSessionElapsedTime.setStatus("obsolete")


class _TrpzLocalId_Type(Integer32):
    """Custom type trpzLocalId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_TrpzLocalId_Type.__name__ = "Integer32"
_TrpzLocalId_Object = MibScalar
trpzLocalId = _TrpzLocalId_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 48),
    _TrpzLocalId_Type()
)
trpzLocalId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzLocalId.setStatus("current")
_TrpzRFDetectDoSType_Type = TrpzRFDetectDoSType
_TrpzRFDetectDoSType_Object = MibScalar
trpzRFDetectDoSType = _TrpzRFDetectDoSType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 49),
    _TrpzRFDetectDoSType_Type()
)
trpzRFDetectDoSType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRFDetectDoSType.setStatus("current")
_TrpzSourceWsIp_Type = IpAddress
_TrpzSourceWsIp_Object = MibScalar
trpzSourceWsIp = _TrpzSourceWsIp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 50),
    _TrpzSourceWsIp_Type()
)
trpzSourceWsIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzSourceWsIp.setStatus("current")


class _TrpzClientVLANid_Type(Integer32):
    """Custom type trpzClientVLANid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TrpzClientVLANid_Type.__name__ = "Integer32"
_TrpzClientVLANid_Object = MibScalar
trpzClientVLANid = _TrpzClientVLANid_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 51),
    _TrpzClientVLANid_Type()
)
trpzClientVLANid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientVLANid.setStatus("current")


class _TrpzClientVLANtag_Type(Integer32):
    """Custom type trpzClientVLANtag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TrpzClientVLANtag_Type.__name__ = "Integer32"
_TrpzClientVLANtag_Object = MibScalar
trpzClientVLANtag = _TrpzClientVLANtag_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 52),
    _TrpzClientVLANtag_Type()
)
trpzClientVLANtag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientVLANtag.setStatus("current")
_TrpzDeviceModel_Type = DisplayString
_TrpzDeviceModel_Object = MibScalar
trpzDeviceModel = _TrpzDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 53),
    _TrpzDeviceModel_Type()
)
trpzDeviceModel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzDeviceModel.setStatus("current")
_TrpzDeviceSerNum_Type = TrpzApSerialNum
_TrpzDeviceSerNum_Object = MibScalar
trpzDeviceSerNum = _TrpzDeviceSerNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 54),
    _TrpzDeviceSerNum_Type()
)
trpzDeviceSerNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzDeviceSerNum.setStatus("current")
_TrpzRsaPubKeyFingerPrint_Type = TrpzApFingerprint
_TrpzRsaPubKeyFingerPrint_Object = MibScalar
trpzRsaPubKeyFingerPrint = _TrpzRsaPubKeyFingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 55),
    _TrpzRsaPubKeyFingerPrint_Type()
)
trpzRsaPubKeyFingerPrint.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRsaPubKeyFingerPrint.setStatus("current")


class _TrpzDAPconnectWarningType_Type(Integer32):
    """Custom type trpzDAPconnectWarningType based on Integer32"""
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
        *(("fingerprint-mismatch", 4),
          ("not-configured-fingerprint-connect", 1),
          ("not-configured-fingerprint-required", 3),
          ("secure-handshake-failure", 2))
    )


_TrpzDAPconnectWarningType_Type.__name__ = "Integer32"
_TrpzDAPconnectWarningType_Object = MibScalar
trpzDAPconnectWarningType = _TrpzDAPconnectWarningType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 56),
    _TrpzDAPconnectWarningType_Type()
)
trpzDAPconnectWarningType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzDAPconnectWarningType.setStatus("current")
_TrpzClientMACAddress2_Type = MacAddress
_TrpzClientMACAddress2_Object = MibScalar
trpzClientMACAddress2 = _TrpzClientMACAddress2_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 57),
    _TrpzClientMACAddress2_Type()
)
trpzClientMACAddress2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientMACAddress2.setStatus("current")
_TrpzApAttachType_Type = TrpzApAttachType
_TrpzApAttachType_Object = MibScalar
trpzApAttachType = _TrpzApAttachType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 58),
    _TrpzApAttachType_Type()
)
trpzApAttachType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzApAttachType.setStatus("current")
_TrpzApPortOrDapNum_Type = TrpzApPortOrDapNum
_TrpzApPortOrDapNum_Object = MibScalar
trpzApPortOrDapNum = _TrpzApPortOrDapNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 59),
    _TrpzApPortOrDapNum_Type()
)
trpzApPortOrDapNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzApPortOrDapNum.setStatus("obsolete")
_TrpzApName_Type = DisplayString
_TrpzApName_Object = MibScalar
trpzApName = _TrpzApName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 60),
    _TrpzApName_Type()
)
trpzApName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzApName.setStatus("current")
_TrpzApTransition_Type = TrpzApTransition
_TrpzApTransition_Object = MibScalar
trpzApTransition = _TrpzApTransition_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 61),
    _TrpzApTransition_Type()
)
trpzApTransition.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzApTransition.setStatus("current")
_TrpzApFailDetail_Type = TrpzApFailDetail
_TrpzApFailDetail_Object = MibScalar
trpzApFailDetail = _TrpzApFailDetail_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 62),
    _TrpzApFailDetail_Type()
)
trpzApFailDetail.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzApFailDetail.setStatus("current")
_TrpzRadioType_Type = TrpzRadioType
_TrpzRadioType_Object = MibScalar
trpzRadioType = _TrpzRadioType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 63),
    _TrpzRadioType_Type()
)
trpzRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRadioType.setStatus("current")
_TrpzRadioConfigState_Type = TrpzRadioConfigState
_TrpzRadioConfigState_Object = MibScalar
trpzRadioConfigState = _TrpzRadioConfigState_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 64),
    _TrpzRadioConfigState_Type()
)
trpzRadioConfigState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRadioConfigState.setStatus("current")
_TrpzApConnectSecurityType_Type = TrpzApConnectSecurityType
_TrpzApConnectSecurityType_Object = MibScalar
trpzApConnectSecurityType = _TrpzApConnectSecurityType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 65),
    _TrpzApConnectSecurityType_Type()
)
trpzApConnectSecurityType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzApConnectSecurityType.setStatus("current")
_TrpzApServiceAvailability_Type = TrpzApServiceAvailability
_TrpzApServiceAvailability_Object = MibScalar
trpzApServiceAvailability = _TrpzApServiceAvailability_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 66),
    _TrpzApServiceAvailability_Type()
)
trpzApServiceAvailability.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzApServiceAvailability.setStatus("current")
_TrpzApWasOperational_Type = TrpzApWasOperational
_TrpzApWasOperational_Object = MibScalar
trpzApWasOperational = _TrpzApWasOperational_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 67),
    _TrpzApWasOperational_Type()
)
trpzApWasOperational.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzApWasOperational.setStatus("current")
_TrpzClientTimeSinceLastRoam_Type = Unsigned32
_TrpzClientTimeSinceLastRoam_Object = MibScalar
trpzClientTimeSinceLastRoam = _TrpzClientTimeSinceLastRoam_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 68),
    _TrpzClientTimeSinceLastRoam_Type()
)
trpzClientTimeSinceLastRoam.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientTimeSinceLastRoam.setStatus("current")
_TrpzClientIpAddrChangeReason_Type = TrpzClientIpAddrChangeReason
_TrpzClientIpAddrChangeReason_Object = MibScalar
trpzClientIpAddrChangeReason = _TrpzClientIpAddrChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 69),
    _TrpzClientIpAddrChangeReason_Type()
)
trpzClientIpAddrChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientIpAddrChangeReason.setStatus("current")
_TrpzRFDetectRogueAPMacAddr_Type = MacAddress
_TrpzRFDetectRogueAPMacAddr_Object = MibScalar
trpzRFDetectRogueAPMacAddr = _TrpzRFDetectRogueAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 70),
    _TrpzRFDetectRogueAPMacAddr_Type()
)
trpzRFDetectRogueAPMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRFDetectRogueAPMacAddr.setStatus("current")
_TrpzBlacklistingRemainingTime_Type = Unsigned32
_TrpzBlacklistingRemainingTime_Object = MibScalar
trpzBlacklistingRemainingTime = _TrpzBlacklistingRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 71),
    _TrpzBlacklistingRemainingTime_Type()
)
trpzBlacklistingRemainingTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzBlacklistingRemainingTime.setStatus("current")
_TrpzBlacklistingCause_Type = TrpzBlacklistingCause
_TrpzBlacklistingCause_Object = MibScalar
trpzBlacklistingCause = _TrpzBlacklistingCause_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 72),
    _TrpzBlacklistingCause_Type()
)
trpzBlacklistingCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzBlacklistingCause.setStatus("current")
_TrpzNumLicensedActiveAPs_Type = Unsigned32
_TrpzNumLicensedActiveAPs_Object = MibScalar
trpzNumLicensedActiveAPs = _TrpzNumLicensedActiveAPs_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 73),
    _TrpzNumLicensedActiveAPs_Type()
)
trpzNumLicensedActiveAPs.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzNumLicensedActiveAPs.setStatus("current")
_TrpzClientDynAuthorClientIp_Type = IpAddress
_TrpzClientDynAuthorClientIp_Object = MibScalar
trpzClientDynAuthorClientIp = _TrpzClientDynAuthorClientIp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 74),
    _TrpzClientDynAuthorClientIp_Type()
)
trpzClientDynAuthorClientIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientDynAuthorClientIp.setStatus("current")
_TrpzChangedUserParamOldValues_Type = TrpzUserAttributeList
_TrpzChangedUserParamOldValues_Object = MibScalar
trpzChangedUserParamOldValues = _TrpzChangedUserParamOldValues_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 75),
    _TrpzChangedUserParamOldValues_Type()
)
trpzChangedUserParamOldValues.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzChangedUserParamOldValues.setStatus("current")
_TrpzChangedUserParamNewValues_Type = TrpzUserAttributeList
_TrpzChangedUserParamNewValues_Object = MibScalar
trpzChangedUserParamNewValues = _TrpzChangedUserParamNewValues_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 76),
    _TrpzChangedUserParamNewValues_Type()
)
trpzChangedUserParamNewValues.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzChangedUserParamNewValues.setStatus("current")
_TrpzClientDisconnectSource_Type = TrpzSessionDisconnectType
_TrpzClientDisconnectSource_Object = MibScalar
trpzClientDisconnectSource = _TrpzClientDisconnectSource_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 77),
    _TrpzClientDisconnectSource_Type()
)
trpzClientDisconnectSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientDisconnectSource.setStatus("current")


class _TrpzClientDisconnectDescription_Type(DisplayString):
    """Custom type trpzClientDisconnectDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzClientDisconnectDescription_Type.__name__ = "DisplayString"
_TrpzClientDisconnectDescription_Object = MibScalar
trpzClientDisconnectDescription = _TrpzClientDisconnectDescription_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 78),
    _TrpzClientDisconnectDescription_Type()
)
trpzClientDisconnectDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientDisconnectDescription.setStatus("current")
_TrpzMobilityDomainSecondarySeedIp_Type = IpAddress
_TrpzMobilityDomainSecondarySeedIp_Object = MibScalar
trpzMobilityDomainSecondarySeedIp = _TrpzMobilityDomainSecondarySeedIp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 79),
    _TrpzMobilityDomainSecondarySeedIp_Type()
)
trpzMobilityDomainSecondarySeedIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMobilityDomainSecondarySeedIp.setStatus("current")
_TrpzMobilityDomainPrimarySeedIp_Type = IpAddress
_TrpzMobilityDomainPrimarySeedIp_Object = MibScalar
trpzMobilityDomainPrimarySeedIp = _TrpzMobilityDomainPrimarySeedIp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 80),
    _TrpzMobilityDomainPrimarySeedIp_Type()
)
trpzMobilityDomainPrimarySeedIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMobilityDomainPrimarySeedIp.setStatus("current")
_TrpzRFDetectClassificationReason_Type = TrpzRFDetectClassificationReason
_TrpzRFDetectClassificationReason_Object = MibScalar
trpzRFDetectClassificationReason = _TrpzRFDetectClassificationReason_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 81),
    _TrpzRFDetectClassificationReason_Type()
)
trpzRFDetectClassificationReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRFDetectClassificationReason.setStatus("current")


class _TrpzConfigSaveFileName_Type(DisplayString):
    """Custom type trpzConfigSaveFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzConfigSaveFileName_Type.__name__ = "DisplayString"
_TrpzConfigSaveFileName_Object = MibScalar
trpzConfigSaveFileName = _TrpzConfigSaveFileName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 82),
    _TrpzConfigSaveFileName_Type()
)
trpzConfigSaveFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzConfigSaveFileName.setStatus("current")
_TrpzConfigSaveInitiatorType_Type = TrpzConfigSaveInitiatorType
_TrpzConfigSaveInitiatorType_Object = MibScalar
trpzConfigSaveInitiatorType = _TrpzConfigSaveInitiatorType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 83),
    _TrpzConfigSaveInitiatorType_Type()
)
trpzConfigSaveInitiatorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzConfigSaveInitiatorType.setStatus("current")
_TrpzConfigSaveInitiatorIp_Type = IpAddress
_TrpzConfigSaveInitiatorIp_Object = MibScalar
trpzConfigSaveInitiatorIp = _TrpzConfigSaveInitiatorIp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 84),
    _TrpzConfigSaveInitiatorIp_Type()
)
trpzConfigSaveInitiatorIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzConfigSaveInitiatorIp.setStatus("current")


class _TrpzConfigSaveInitiatorDetails_Type(DisplayString):
    """Custom type trpzConfigSaveInitiatorDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzConfigSaveInitiatorDetails_Type.__name__ = "DisplayString"
_TrpzConfigSaveInitiatorDetails_Object = MibScalar
trpzConfigSaveInitiatorDetails = _TrpzConfigSaveInitiatorDetails_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 85),
    _TrpzConfigSaveInitiatorDetails_Type()
)
trpzConfigSaveInitiatorDetails.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzConfigSaveInitiatorDetails.setStatus("current")
_TrpzConfigSaveGeneration_Type = Counter32
_TrpzConfigSaveGeneration_Object = MibScalar
trpzConfigSaveGeneration = _TrpzConfigSaveGeneration_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 86),
    _TrpzConfigSaveGeneration_Type()
)
trpzConfigSaveGeneration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzConfigSaveGeneration.setStatus("current")
_TrpzApNum_Type = TrpzApNum
_TrpzApNum_Object = MibScalar
trpzApNum = _TrpzApNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 87),
    _TrpzApNum_Type()
)
trpzApNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzApNum.setStatus("current")
_TrpzRadioMode_Type = TrpzRadioMode
_TrpzRadioMode_Object = MibScalar
trpzRadioMode = _TrpzRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 88),
    _TrpzRadioMode_Type()
)
trpzRadioMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRadioMode.setStatus("current")
_TrpzMichaelMICFailureCause_Type = TrpzMichaelMICFailureCause
_TrpzMichaelMICFailureCause_Object = MibScalar
trpzMichaelMICFailureCause = _TrpzMichaelMICFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 89),
    _TrpzMichaelMICFailureCause_Type()
)
trpzMichaelMICFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMichaelMICFailureCause.setStatus("current")
_TrpzClientAccessMode_Type = TrpzClientAccessMode
_TrpzClientAccessMode_Object = MibScalar
trpzClientAccessMode = _TrpzClientAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 90),
    _TrpzClientAccessMode_Type()
)
trpzClientAccessMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientAccessMode.setStatus("current")
_TrpzClientAuthorizationReason_Type = TrpzClientAuthorizationReason
_TrpzClientAuthorizationReason_Object = MibScalar
trpzClientAuthorizationReason = _TrpzClientAuthorizationReason_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 91),
    _TrpzClientAuthorizationReason_Type()
)
trpzClientAuthorizationReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientAuthorizationReason.setStatus("current")
_TrpzPhysPortNum_Type = TrpzPhysPortNumberOrZero
_TrpzPhysPortNum_Object = MibScalar
trpzPhysPortNum = _TrpzPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 92),
    _TrpzPhysPortNum_Type()
)
trpzPhysPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzPhysPortNum.setStatus("current")
_TrpzApMgrOldIp_Type = IpAddress
_TrpzApMgrOldIp_Object = MibScalar
trpzApMgrOldIp = _TrpzApMgrOldIp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 93),
    _TrpzApMgrOldIp_Type()
)
trpzApMgrOldIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzApMgrOldIp.setStatus("current")
_TrpzApMgrNewIp_Type = IpAddress
_TrpzApMgrNewIp_Object = MibScalar
trpzApMgrNewIp = _TrpzApMgrNewIp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 94),
    _TrpzApMgrNewIp_Type()
)
trpzApMgrNewIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzApMgrNewIp.setStatus("current")
_TrpzApMgrChangeReason_Type = TrpzApMgrChangeReason
_TrpzApMgrChangeReason_Object = MibScalar
trpzApMgrChangeReason = _TrpzApMgrChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 95),
    _TrpzApMgrChangeReason_Type()
)
trpzApMgrChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzApMgrChangeReason.setStatus("current")
_TrpzClientClearedReason_Type = TrpzClientClearedReason
_TrpzClientClearedReason_Object = MibScalar
trpzClientClearedReason = _TrpzClientClearedReason_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 96),
    _TrpzClientClearedReason_Type()
)
trpzClientClearedReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientClearedReason.setStatus("current")
_TrpzMobilityDomainResiliencyStatus_Type = TrpzMobilityDomainResiliencyStatus
_TrpzMobilityDomainResiliencyStatus_Object = MibScalar
trpzMobilityDomainResiliencyStatus = _TrpzMobilityDomainResiliencyStatus_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 97),
    _TrpzMobilityDomainResiliencyStatus_Type()
)
trpzMobilityDomainResiliencyStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMobilityDomainResiliencyStatus.setStatus("current")
_TrpzClientSessionElapsedSeconds_Type = Unsigned32
_TrpzClientSessionElapsedSeconds_Object = MibScalar
trpzClientSessionElapsedSeconds = _TrpzClientSessionElapsedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 98),
    _TrpzClientSessionElapsedSeconds_Type()
)
trpzClientSessionElapsedSeconds.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientSessionElapsedSeconds.setStatus("current")
_TrpzRadioChannelWidth_Type = TrpzRadioChannelWidth
_TrpzRadioChannelWidth_Object = MibScalar
trpzRadioChannelWidth = _TrpzRadioChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 99),
    _TrpzRadioChannelWidth_Type()
)
trpzRadioChannelWidth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRadioChannelWidth.setStatus("current")
_TrpzRadioMimoState_Type = TrpzRadioMimoState
_TrpzRadioMimoState_Object = MibScalar
trpzRadioMimoState = _TrpzRadioMimoState_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 100),
    _TrpzRadioMimoState_Type()
)
trpzRadioMimoState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRadioMimoState.setStatus("current")
_TrpzClientRadioType_Type = TrpzRadioType
_TrpzClientRadioType_Object = MibScalar
trpzClientRadioType = _TrpzClientRadioType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 101),
    _TrpzClientRadioType_Type()
)
trpzClientRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientRadioType.setStatus("current")
_TrpzRFDetectXmtrRadioType_Type = TrpzRadioType
_TrpzRFDetectXmtrRadioType_Object = MibScalar
trpzRFDetectXmtrRadioType = _TrpzRFDetectXmtrRadioType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 102),
    _TrpzRFDetectXmtrRadioType_Type()
)
trpzRFDetectXmtrRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRFDetectXmtrRadioType.setStatus("current")
_TrpzRFDetectXmtrCryptoType_Type = TrpzCryptoType
_TrpzRFDetectXmtrCryptoType_Object = MibScalar
trpzRFDetectXmtrCryptoType = _TrpzRFDetectXmtrCryptoType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 103),
    _TrpzRFDetectXmtrCryptoType_Type()
)
trpzRFDetectXmtrCryptoType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRFDetectXmtrCryptoType.setStatus("current")
_TrpzClusterFailureReason_Type = TrpzClusterFailureReason
_TrpzClusterFailureReason_Object = MibScalar
trpzClusterFailureReason = _TrpzClusterFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 104),
    _TrpzClusterFailureReason_Type()
)
trpzClusterFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClusterFailureReason.setStatus("current")


class _TrpzClusterFailureDescription_Type(DisplayString):
    """Custom type trpzClusterFailureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzClusterFailureDescription_Type.__name__ = "DisplayString"
_TrpzClusterFailureDescription_Object = MibScalar
trpzClusterFailureDescription = _TrpzClusterFailureDescription_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 105),
    _TrpzClusterFailureDescription_Type()
)
trpzClusterFailureDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClusterFailureDescription.setStatus("current")


class _TrpzMultimediaCommunicationServerID_Type(DisplayString):
    """Custom type trpzMultimediaCommunicationServerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzMultimediaCommunicationServerID_Type.__name__ = "DisplayString"
_TrpzMultimediaCommunicationServerID_Object = MibScalar
trpzMultimediaCommunicationServerID = _TrpzMultimediaCommunicationServerID_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 106),
    _TrpzMultimediaCommunicationServerID_Type()
)
trpzMultimediaCommunicationServerID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMultimediaCommunicationServerID.setStatus("current")
_TrpzMultimediaLocalStationIp_Type = IpAddress
_TrpzMultimediaLocalStationIp_Object = MibScalar
trpzMultimediaLocalStationIp = _TrpzMultimediaLocalStationIp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 107),
    _TrpzMultimediaLocalStationIp_Type()
)
trpzMultimediaLocalStationIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMultimediaLocalStationIp.setStatus("current")
_TrpzMultimediaLocalStationPort_Type = TrpzIpPort
_TrpzMultimediaLocalStationPort_Object = MibScalar
trpzMultimediaLocalStationPort = _TrpzMultimediaLocalStationPort_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 108),
    _TrpzMultimediaLocalStationPort_Type()
)
trpzMultimediaLocalStationPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMultimediaLocalStationPort.setStatus("current")


class _TrpzMultimediaLocalStationEndpointID_Type(DisplayString):
    """Custom type trpzMultimediaLocalStationEndpointID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzMultimediaLocalStationEndpointID_Type.__name__ = "DisplayString"
_TrpzMultimediaLocalStationEndpointID_Object = MibScalar
trpzMultimediaLocalStationEndpointID = _TrpzMultimediaLocalStationEndpointID_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 109),
    _TrpzMultimediaLocalStationEndpointID_Type()
)
trpzMultimediaLocalStationEndpointID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMultimediaLocalStationEndpointID.setStatus("current")
_TrpzMultimediaRemoteStationIp_Type = IpAddress
_TrpzMultimediaRemoteStationIp_Object = MibScalar
trpzMultimediaRemoteStationIp = _TrpzMultimediaRemoteStationIp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 110),
    _TrpzMultimediaRemoteStationIp_Type()
)
trpzMultimediaRemoteStationIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMultimediaRemoteStationIp.setStatus("current")
_TrpzMultimediaRemoteStationPort_Type = TrpzIpPort
_TrpzMultimediaRemoteStationPort_Object = MibScalar
trpzMultimediaRemoteStationPort = _TrpzMultimediaRemoteStationPort_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 111),
    _TrpzMultimediaRemoteStationPort_Type()
)
trpzMultimediaRemoteStationPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMultimediaRemoteStationPort.setStatus("current")


class _TrpzMultimediaRemoteStationEndpointID_Type(DisplayString):
    """Custom type trpzMultimediaRemoteStationEndpointID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzMultimediaRemoteStationEndpointID_Type.__name__ = "DisplayString"
_TrpzMultimediaRemoteStationEndpointID_Object = MibScalar
trpzMultimediaRemoteStationEndpointID = _TrpzMultimediaRemoteStationEndpointID_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 112),
    _TrpzMultimediaRemoteStationEndpointID_Type()
)
trpzMultimediaRemoteStationEndpointID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMultimediaRemoteStationEndpointID.setStatus("current")
_TrpzMultimediaSignalingProtocol_Type = TrpzMultimediaSignalingProtocol
_TrpzMultimediaSignalingProtocol_Object = MibScalar
trpzMultimediaSignalingProtocol = _TrpzMultimediaSignalingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 113),
    _TrpzMultimediaSignalingProtocol_Type()
)
trpzMultimediaSignalingProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMultimediaSignalingProtocol.setStatus("current")


class _TrpzMultimediaCallBandwidthAndCodec_Type(DisplayString):
    """Custom type trpzMultimediaCallBandwidthAndCodec based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzMultimediaCallBandwidthAndCodec_Type.__name__ = "DisplayString"
_TrpzMultimediaCallBandwidthAndCodec_Object = MibScalar
trpzMultimediaCallBandwidthAndCodec = _TrpzMultimediaCallBandwidthAndCodec_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 114),
    _TrpzMultimediaCallBandwidthAndCodec_Type()
)
trpzMultimediaCallBandwidthAndCodec.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMultimediaCallBandwidthAndCodec.setStatus("current")
_TrpzMultimediaCallDataRate_Type = Unsigned32
_TrpzMultimediaCallDataRate_Object = MibScalar
trpzMultimediaCallDataRate = _TrpzMultimediaCallDataRate_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 115),
    _TrpzMultimediaCallDataRate_Type()
)
trpzMultimediaCallDataRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMultimediaCallDataRate.setStatus("current")
_TrpzMultimediaCallRssi_Type = TrpzRssi
_TrpzMultimediaCallRssi_Object = MibScalar
trpzMultimediaCallRssi = _TrpzMultimediaCallRssi_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 116),
    _TrpzMultimediaCallRssi_Type()
)
trpzMultimediaCallRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMultimediaCallRssi.setStatus("current")
_TrpzMultimediaCallFailureReason_Type = TrpzMultimediaCallFailureReason
_TrpzMultimediaCallFailureReason_Object = MibScalar
trpzMultimediaCallFailureReason = _TrpzMultimediaCallFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 117),
    _TrpzMultimediaCallFailureReason_Type()
)
trpzMultimediaCallFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMultimediaCallFailureReason.setStatus("current")
_TrpzMultimediaCallDirection_Type = TrpzMultimediaCallDirection
_TrpzMultimediaCallDirection_Object = MibScalar
trpzMultimediaCallDirection = _TrpzMultimediaCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 118),
    _TrpzMultimediaCallDirection_Type()
)
trpzMultimediaCallDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzMultimediaCallDirection.setStatus("current")
_TrpzApTunnelLimit_Type = Unsigned32
_TrpzApTunnelLimit_Object = MibScalar
trpzApTunnelLimit = _TrpzApTunnelLimit_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 119),
    _TrpzApTunnelLimit_Type()
)
trpzApTunnelLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzApTunnelLimit.setStatus("current")
_TrpzWsTunnelLimit_Type = Unsigned32
_TrpzWsTunnelLimit_Object = MibScalar
trpzWsTunnelLimit = _TrpzWsTunnelLimit_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 120),
    _TrpzWsTunnelLimit_Type()
)
trpzWsTunnelLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzWsTunnelLimit.setStatus("current")
_TrpzWsTunnelLimitType_Type = TrpzWsTunnelLimitType
_TrpzWsTunnelLimitType_Object = MibScalar
trpzWsTunnelLimitType = _TrpzWsTunnelLimitType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 121),
    _TrpzWsTunnelLimitType_Type()
)
trpzWsTunnelLimitType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzWsTunnelLimitType.setStatus("current")
_TrpzRFNoiseSourceID_Type = TrpzRFNoiseSourceID
_TrpzRFNoiseSourceID_Object = MibScalar
trpzRFNoiseSourceID = _TrpzRFNoiseSourceID_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 122),
    _TrpzRFNoiseSourceID_Type()
)
trpzRFNoiseSourceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRFNoiseSourceID.setStatus("current")
_TrpzRFNoiseSourceType_Type = TrpzRFNoiseSourceType
_TrpzRFNoiseSourceType_Object = MibScalar
trpzRFNoiseSourceType = _TrpzRFNoiseSourceType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 123),
    _TrpzRFNoiseSourceType_Type()
)
trpzRFNoiseSourceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRFNoiseSourceType.setStatus("current")
_TrpzRFNoiseChannel_Type = TrpzChannelNum
_TrpzRFNoiseChannel_Object = MibScalar
trpzRFNoiseChannel = _TrpzRFNoiseChannel_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 124),
    _TrpzRFNoiseChannel_Type()
)
trpzRFNoiseChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRFNoiseChannel.setStatus("current")
_TrpzRFNoiseRssi_Type = TrpzRssi
_TrpzRFNoiseRssi_Object = MibScalar
trpzRFNoiseRssi = _TrpzRFNoiseRssi_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 125),
    _TrpzRFNoiseRssi_Type()
)
trpzRFNoiseRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRFNoiseRssi.setStatus("current")
_TrpzRFNoiseDutyCycle_Type = Unsigned32
_TrpzRFNoiseDutyCycle_Object = MibScalar
trpzRFNoiseDutyCycle = _TrpzRFNoiseDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 126),
    _TrpzRFNoiseDutyCycle_Type()
)
trpzRFNoiseDutyCycle.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRFNoiseDutyCycle.setStatus("current")
_TrpzRFNoiseChannelInterferenceMeasure_Type = Unsigned32
_TrpzRFNoiseChannelInterferenceMeasure_Object = MibScalar
trpzRFNoiseChannelInterferenceMeasure = _TrpzRFNoiseChannelInterferenceMeasure_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 127),
    _TrpzRFNoiseChannelInterferenceMeasure_Type()
)
trpzRFNoiseChannelInterferenceMeasure.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRFNoiseChannelInterferenceMeasure.setStatus("current")
_TrpzRFNoiseAge_Type = Unsigned32
_TrpzRFNoiseAge_Object = MibScalar
trpzRFNoiseAge = _TrpzRFNoiseAge_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 128),
    _TrpzRFNoiseAge_Type()
)
trpzRFNoiseAge.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRFNoiseAge.setStatus("current")
_TrpzM2UMulticastAddrType_Type = InetAddressType
_TrpzM2UMulticastAddrType_Object = MibScalar
trpzM2UMulticastAddrType = _TrpzM2UMulticastAddrType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 129),
    _TrpzM2UMulticastAddrType_Type()
)
trpzM2UMulticastAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzM2UMulticastAddrType.setStatus("current")
_TrpzM2UMulticastAddr_Type = InetAddress
_TrpzM2UMulticastAddr_Object = MibScalar
trpzM2UMulticastAddr = _TrpzM2UMulticastAddr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 130),
    _TrpzM2UMulticastAddr_Type()
)
trpzM2UMulticastAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzM2UMulticastAddr.setStatus("current")
_TrpzM2UConvNotPossibleReason_Type = TrpzM2UConvNotPossibleReason
_TrpzM2UConvNotPossibleReason_Object = MibScalar
trpzM2UConvNotPossibleReason = _TrpzM2UConvNotPossibleReason_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 131),
    _TrpzM2UConvNotPossibleReason_Type()
)
trpzM2UConvNotPossibleReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzM2UConvNotPossibleReason.setStatus("current")
_TrpzRadioBand_Type = TrpzRadioBand
_TrpzRadioBand_Object = MibScalar
trpzRadioBand = _TrpzRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 132),
    _TrpzRadioBand_Type()
)
trpzRadioBand.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRadioBand.setStatus("current")
_TrpzRadiosTunedCount_Type = Unsigned32
_TrpzRadiosTunedCount_Object = MibScalar
trpzRadiosTunedCount = _TrpzRadiosTunedCount_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 133),
    _TrpzRadiosTunedCount_Type()
)
trpzRadiosTunedCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzRadiosTunedCount.setStatus("current")
_TrpzAutoTuneFailureReason_Type = TrpzAutoTuneFailureReason
_TrpzAutoTuneFailureReason_Object = MibScalar
trpzAutoTuneFailureReason = _TrpzAutoTuneFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 134),
    _TrpzAutoTuneFailureReason_Type()
)
trpzAutoTuneFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzAutoTuneFailureReason.setStatus("current")
_TrpzClientAuthServerAddrType_Type = InetAddressType
_TrpzClientAuthServerAddrType_Object = MibScalar
trpzClientAuthServerAddrType = _TrpzClientAuthServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 135),
    _TrpzClientAuthServerAddrType_Type()
)
trpzClientAuthServerAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientAuthServerAddrType.setStatus("current")
_TrpzClientAuthServerAddr_Type = InetAddress
_TrpzClientAuthServerAddr_Object = MibScalar
trpzClientAuthServerAddr = _TrpzClientAuthServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 136),
    _TrpzClientAuthServerAddr_Type()
)
trpzClientAuthServerAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientAuthServerAddr.setStatus("current")
_TrpzClientRoamedFromWsAddrType_Type = InetAddressType
_TrpzClientRoamedFromWsAddrType_Object = MibScalar
trpzClientRoamedFromWsAddrType = _TrpzClientRoamedFromWsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 137),
    _TrpzClientRoamedFromWsAddrType_Type()
)
trpzClientRoamedFromWsAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientRoamedFromWsAddrType.setStatus("current")
_TrpzClientRoamedFromWsAddr_Type = InetAddress
_TrpzClientRoamedFromWsAddr_Object = MibScalar
trpzClientRoamedFromWsAddr = _TrpzClientRoamedFromWsAddr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 138),
    _TrpzClientRoamedFromWsAddr_Type()
)
trpzClientRoamedFromWsAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientRoamedFromWsAddr.setStatus("current")
_TrpzClientDynAuthorClientAddrType_Type = InetAddressType
_TrpzClientDynAuthorClientAddrType_Object = MibScalar
trpzClientDynAuthorClientAddrType = _TrpzClientDynAuthorClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 139),
    _TrpzClientDynAuthorClientAddrType_Type()
)
trpzClientDynAuthorClientAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientDynAuthorClientAddrType.setStatus("current")
_TrpzClientDynAuthorClientAddr_Type = InetAddress
_TrpzClientDynAuthorClientAddr_Object = MibScalar
trpzClientDynAuthorClientAddr = _TrpzClientDynAuthorClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 140),
    _TrpzClientDynAuthorClientAddr_Type()
)
trpzClientDynAuthorClientAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientDynAuthorClientAddr.setStatus("current")
_TrpzClientIpAddrType_Type = InetAddressType
_TrpzClientIpAddrType_Object = MibScalar
trpzClientIpAddrType = _TrpzClientIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 141),
    _TrpzClientIpAddrType_Type()
)
trpzClientIpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientIpAddrType.setStatus("current")
_TrpzClientIpAddr_Type = InetAddress
_TrpzClientIpAddr_Object = MibScalar
trpzClientIpAddr = _TrpzClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 142),
    _TrpzClientIpAddr_Type()
)
trpzClientIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientIpAddr.setStatus("current")
_TrpzClientIPv4Addr_Type = InetAddressIPv4
_TrpzClientIPv4Addr_Object = MibScalar
trpzClientIPv4Addr = _TrpzClientIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 143),
    _TrpzClientIPv4Addr_Type()
)
trpzClientIPv4Addr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientIPv4Addr.setStatus("current")
_TrpzClientIPv6LinkLocalAddr_Type = InetAddressIPv6
_TrpzClientIPv6LinkLocalAddr_Object = MibScalar
trpzClientIPv6LinkLocalAddr = _TrpzClientIPv6LinkLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 144),
    _TrpzClientIPv6LinkLocalAddr_Type()
)
trpzClientIPv6LinkLocalAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientIPv6LinkLocalAddr.setStatus("current")
_TrpzApRadioIndex_Type = TrpzApRadioIndex
_TrpzApRadioIndex_Object = MibScalar
trpzApRadioIndex = _TrpzApRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 145),
    _TrpzApRadioIndex_Type()
)
trpzApRadioIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzApRadioIndex.setStatus("current")
_TrpzClientRoamedFromAccessMode_Type = TrpzClientAccessMode
_TrpzClientRoamedFromAccessMode_Object = MibScalar
trpzClientRoamedFromAccessMode = _TrpzClientRoamedFromAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 146),
    _TrpzClientRoamedFromAccessMode_Type()
)
trpzClientRoamedFromAccessMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientRoamedFromAccessMode.setStatus("current")
_TrpzClientRoamedFromApNum_Type = TrpzApNum
_TrpzClientRoamedFromApNum_Object = MibScalar
trpzClientRoamedFromApNum = _TrpzClientRoamedFromApNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 147),
    _TrpzClientRoamedFromApNum_Type()
)
trpzClientRoamedFromApNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientRoamedFromApNum.setStatus("current")
_TrpzClientRoamedFromRadioIndex_Type = TrpzApRadioIndex
_TrpzClientRoamedFromRadioIndex_Object = MibScalar
trpzClientRoamedFromRadioIndex = _TrpzClientRoamedFromRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 148),
    _TrpzClientRoamedFromRadioIndex_Type()
)
trpzClientRoamedFromRadioIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientRoamedFromRadioIndex.setStatus("current")
_TrpzClientRoamedFromPhysPortNum_Type = TrpzPhysPortNumberOrZero
_TrpzClientRoamedFromPhysPortNum_Object = MibScalar
trpzClientRoamedFromPhysPortNum = _TrpzClientRoamedFromPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 149),
    _TrpzClientRoamedFromPhysPortNum_Type()
)
trpzClientRoamedFromPhysPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientRoamedFromPhysPortNum.setStatus("current")
_TrpzClientDeviceType_Type = TrpzClientDeviceType
_TrpzClientDeviceType_Object = MibScalar
trpzClientDeviceType = _TrpzClientDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 150),
    _TrpzClientDeviceType_Type()
)
trpzClientDeviceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientDeviceType.setStatus("current")
_TrpzClientDeviceTypeOld_Type = TrpzClientDeviceType
_TrpzClientDeviceTypeOld_Object = MibScalar
trpzClientDeviceTypeOld = _TrpzClientDeviceTypeOld_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 151),
    _TrpzClientDeviceTypeOld_Type()
)
trpzClientDeviceTypeOld.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientDeviceTypeOld.setStatus("current")
_TrpzClientDeviceGroup_Type = TrpzClientDeviceGroupName
_TrpzClientDeviceGroup_Object = MibScalar
trpzClientDeviceGroup = _TrpzClientDeviceGroup_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 152),
    _TrpzClientDeviceGroup_Type()
)
trpzClientDeviceGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientDeviceGroup.setStatus("current")
_TrpzClientDeviceProfileName_Type = TrpzClientDeviceProfileName
_TrpzClientDeviceProfileName_Object = MibScalar
trpzClientDeviceProfileName = _TrpzClientDeviceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 153),
    _TrpzClientDeviceProfileName_Type()
)
trpzClientDeviceProfileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientDeviceProfileName.setStatus("current")
_TrpzClientDeviceProfileNameOld_Type = TrpzClientDeviceProfileName
_TrpzClientDeviceProfileNameOld_Object = MibScalar
trpzClientDeviceProfileNameOld = _TrpzClientDeviceProfileNameOld_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 154),
    _TrpzClientDeviceProfileNameOld_Type()
)
trpzClientDeviceProfileNameOld.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientDeviceProfileNameOld.setStatus("current")
_TrpzClientDeviceProfileChangeReason_Type = TrpzClientDeviceProfileChangeReason
_TrpzClientDeviceProfileChangeReason_Object = MibScalar
trpzClientDeviceProfileChangeReason = _TrpzClientDeviceProfileChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 14525, 2, 155),
    _TrpzClientDeviceProfileChangeReason_Type()
)
trpzClientDeviceProfileChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trpzClientDeviceProfileChangeReason.setStatus("current")
_TrpzTrapsV2_ObjectIdentity = ObjectIdentity
trpzTrapsV2 = _TrpzTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0)
)

# Managed Objects groups


# Notification objects

trpzDeviceFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 1)
)
trpzDeviceFailTrap.setObjects(
    ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDeviceId")
)
if mibBuilder.loadTexts:
    trpzDeviceFailTrap.setStatus(
        "current"
    )

trpzDeviceOkayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 2)
)
trpzDeviceOkayTrap.setObjects(
    ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDeviceId")
)
if mibBuilder.loadTexts:
    trpzDeviceOkayTrap.setStatus(
        "current"
    )

trpzPoEFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 3)
)
trpzPoEFailTrap.setObjects(
    ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum")
)
if mibBuilder.loadTexts:
    trpzPoEFailTrap.setStatus(
        "current"
    )

trpzApTimeoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 4)
)
trpzApTimeoutTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"))
)
if mibBuilder.loadTexts:
    trpzApTimeoutTrap.setStatus(
        "obsolete"
    )

trpzAPBootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 5)
)
trpzAPBootTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"))
)
if mibBuilder.loadTexts:
    trpzAPBootTrap.setStatus(
        "obsolete"
    )

trpzMobilityDomainJoinTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 6)
)
trpzMobilityDomainJoinTrap.setObjects(
    ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMobilityDomainIp")
)
if mibBuilder.loadTexts:
    trpzMobilityDomainJoinTrap.setStatus(
        "current"
    )

trpzMobilityDomainTimeoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 7)
)
trpzMobilityDomainTimeoutTrap.setObjects(
    ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMobilityDomainIp")
)
if mibBuilder.loadTexts:
    trpzMobilityDomainTimeoutTrap.setStatus(
        "current"
    )

trpzMpMichaelMICFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 8)
)
trpzMpMichaelMICFailure.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"))
)
if mibBuilder.loadTexts:
    trpzMpMichaelMICFailure.setStatus(
        "obsolete"
    )

trpzRFDetectRogueAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 9)
)
trpzRFDetectRogueAPTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    trpzRFDetectRogueAPTrap.setStatus(
        "obsolete"
    )

trpzRFDetectAdhocUserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 10)
)
trpzRFDetectAdhocUserTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    trpzRFDetectAdhocUserTrap.setStatus(
        "current"
    )

trpzRFDetectRogueDisappearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 11)
)
trpzRFDetectRogueDisappearTrap.setObjects(
    ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr")
)
if mibBuilder.loadTexts:
    trpzRFDetectRogueDisappearTrap.setStatus(
        "obsolete"
    )

trpzClientAuthenticationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 12)
)
trpzClientAuthenticationFailureTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenticationFailureCause"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientFailureCauseDescription"))
)
if mibBuilder.loadTexts:
    trpzClientAuthenticationFailureTrap.setStatus(
        "current"
    )

trpzClientAuthorizationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 13)
)
trpzClientAuthorizationFailureTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientLocationPolicyIndex"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserParams"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthorizationFailureCause"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientFailureCauseDescription"))
)
if mibBuilder.loadTexts:
    trpzClientAuthorizationFailureTrap.setStatus(
        "current"
    )

trpzClientAssociationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 14)
)
trpzClientAssociationFailureTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAssociationFailureCause"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientFailureCauseDescription"))
)
if mibBuilder.loadTexts:
    trpzClientAssociationFailureTrap.setStatus(
        "current"
    )

trpzClientAuthorizationSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 15)
)
trpzClientAuthorizationSuccessTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionState"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionStartTime"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioRssi"))
)
if mibBuilder.loadTexts:
    trpzClientAuthorizationSuccessTrap.setStatus(
        "obsolete"
    )

trpzClientDeAssociationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 16)
)
trpzClientDeAssociationTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"))
)
if mibBuilder.loadTexts:
    trpzClientDeAssociationTrap.setStatus(
        "obsolete"
    )

trpzClientRoamingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 17)
)
trpzClientRoamingTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientRoamedFromAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientRoamedFromPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientRoamedFromRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientRoamedFromDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientRoamedFromWsIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientTimeSinceLastRoam"))
)
if mibBuilder.loadTexts:
    trpzClientRoamingTrap.setStatus(
        "obsolete"
    )

trpzAutoTuneRadioPowerChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 18)
)
trpzAutoTuneRadioPowerChangeTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzNewPowerLevel"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzOldPowerLevel"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioPowerChangeReason"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioPowerChangeDescription"))
)
if mibBuilder.loadTexts:
    trpzAutoTuneRadioPowerChangeTrap.setStatus(
        "current"
    )

trpzAutoTuneRadioChannelChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 19)
)
trpzAutoTuneRadioChannelChangeTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzNewChannelNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzOldChannelNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzChannelChangeReason"))
)
if mibBuilder.loadTexts:
    trpzAutoTuneRadioChannelChangeTrap.setStatus(
        "current"
    )

trpzCounterMeasureStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 20)
)
trpzCounterMeasureStartTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioMACAddress"))
)
if mibBuilder.loadTexts:
    trpzCounterMeasureStartTrap.setStatus(
        "current"
    )

trpzCounterMeasureStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 21)
)
trpzCounterMeasureStopTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioMACAddress"))
)
if mibBuilder.loadTexts:
    trpzCounterMeasureStopTrap.setStatus(
        "current"
    )

trpzClientDot1xFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 22)
)
trpzClientDot1xFailureTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDot1xState"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDot1xFailureCause"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientFailureCauseDescription"))
)
if mibBuilder.loadTexts:
    trpzClientDot1xFailureTrap.setStatus(
        "current"
    )

trpzClientClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 23)
)
trpzClientClearedTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionElapsedTime"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzLocalId"))
)
if mibBuilder.loadTexts:
    trpzClientClearedTrap.setStatus(
        "obsolete"
    )

trpzClientAuthorizationSuccessTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 24)
)
trpzClientAuthorizationSuccessTrap2.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionState"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionStartTime"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzLocalId"))
)
if mibBuilder.loadTexts:
    trpzClientAuthorizationSuccessTrap2.setStatus(
        "obsolete"
    )

trpzRFDetectSpoofedMacAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 25)
)
trpzRFDetectSpoofedMacAPTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    trpzRFDetectSpoofedMacAPTrap.setStatus(
        "obsolete"
    )

trpzRFDetectSpoofedSsidAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 26)
)
trpzRFDetectSpoofedSsidAPTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    trpzRFDetectSpoofedSsidAPTrap.setStatus(
        "obsolete"
    )

trpzRFDetectDoSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 27)
)
trpzRFDetectDoSTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectDoSType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    trpzRFDetectDoSTrap.setStatus(
        "current"
    )

trpzRFDetectClientViaRogueWiredAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 28)
)
trpzRFDetectClientViaRogueWiredAPTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzSourceWsIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANid"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANtag"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    trpzRFDetectClientViaRogueWiredAPTrap.setStatus(
        "obsolete"
    )

trpzRFDetectInterferingRogueAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 29)
)
trpzRFDetectInterferingRogueAPTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    trpzRFDetectInterferingRogueAPTrap.setStatus(
        "obsolete"
    )

trpzRFDetectInterferingRogueDisappearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 30)
)
trpzRFDetectInterferingRogueDisappearTrap.setObjects(
    ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr")
)
if mibBuilder.loadTexts:
    trpzRFDetectInterferingRogueDisappearTrap.setStatus(
        "obsolete"
    )

trpzRFDetectUnAuthorizedSsidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 31)
)
trpzRFDetectUnAuthorizedSsidTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    trpzRFDetectUnAuthorizedSsidTrap.setStatus(
        "obsolete"
    )

trpzRFDetectUnAuthorizedOuiTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 32)
)
trpzRFDetectUnAuthorizedOuiTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    trpzRFDetectUnAuthorizedOuiTrap.setStatus(
        "obsolete"
    )

trpzRFDetectUnAuthorizedAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 33)
)
trpzRFDetectUnAuthorizedAPTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    trpzRFDetectUnAuthorizedAPTrap.setStatus(
        "obsolete"
    )

trpzDAPConnectWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 34)
)
trpzDAPConnectWarningTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDeviceModel"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDeviceSerNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRsaPubKeyFingerPrint"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPconnectWarningType"))
)
if mibBuilder.loadTexts:
    trpzDAPConnectWarningTrap.setStatus(
        "obsolete"
    )

trpzRFDetectDoSPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 35)
)
trpzRFDetectDoSPortTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectDoSType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"))
)
if mibBuilder.loadTexts:
    trpzRFDetectDoSPortTrap.setStatus(
        "current"
    )

trpzMpMichaelMICFailure2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 36)
)
trpzMpMichaelMICFailure2.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress2"))
)
if mibBuilder.loadTexts:
    trpzMpMichaelMICFailure2.setStatus(
        "obsolete"
    )

trpzApNonOperStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 37)
)
trpzApNonOperStatusTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDeviceSerNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApAttachType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApPortOrDapNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApTransition"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApFailDetail"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApWasOperational"))
)
if mibBuilder.loadTexts:
    trpzApNonOperStatusTrap.setStatus(
        "obsolete"
    )

trpzApOperRadioStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 38)
)
trpzApOperRadioStatusTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDeviceSerNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApAttachType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApPortOrDapNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioConfigState"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApConnectSecurityType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApServiceAvailability"))
)
if mibBuilder.loadTexts:
    trpzApOperRadioStatusTrap.setStatus(
        "obsolete"
    )

trpzClientIpAddrChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 39)
)
trpzClientIpAddrChangeTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionState"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzLocalId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIpAddrChangeReason"))
)
if mibBuilder.loadTexts:
    trpzClientIpAddrChangeTrap.setStatus(
        "obsolete"
    )

trpzClientAssociationSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 40)
)
trpzClientAssociationSuccessTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"))
)
if mibBuilder.loadTexts:
    trpzClientAssociationSuccessTrap.setStatus(
        "current"
    )

trpzClientAuthenticationSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 41)
)
trpzClientAuthenticationSuccessTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"))
)
if mibBuilder.loadTexts:
    trpzClientAuthenticationSuccessTrap.setStatus(
        "current"
    )

trpzClientDeAuthenticationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 42)
)
trpzClientDeAuthenticationTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"))
)
if mibBuilder.loadTexts:
    trpzClientDeAuthenticationTrap.setStatus(
        "obsolete"
    )

trpzRFDetectBlacklistedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 43)
)
trpzRFDetectBlacklistedTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzBlacklistingRemainingTime"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzBlacklistingCause"))
)
if mibBuilder.loadTexts:
    trpzRFDetectBlacklistedTrap.setStatus(
        "current"
    )

trpzRFDetectClientViaRogueWiredAPTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 44)
)
trpzRFDetectClientViaRogueWiredAPTrap2.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzSourceWsIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANid"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANtag"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectListenerListInfo"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectRogueAPMacAddr"))
)
if mibBuilder.loadTexts:
    trpzRFDetectClientViaRogueWiredAPTrap2.setStatus(
        "obsolete"
    )

trpzRFDetectAdhocUserDisappearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 45)
)
trpzRFDetectAdhocUserDisappearTrap.setObjects(
    ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr")
)
if mibBuilder.loadTexts:
    trpzRFDetectAdhocUserDisappearTrap.setStatus(
        "current"
    )

trpzApRejectLicenseExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 46)
)
trpzApRejectLicenseExceededTrap.setObjects(
    ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzNumLicensedActiveAPs")
)
if mibBuilder.loadTexts:
    trpzApRejectLicenseExceededTrap.setStatus(
        "current"
    )

trpzClientDynAuthorChangeSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 47)
)
trpzClientDynAuthorChangeSuccessTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionState"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDynAuthorClientIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzLocalId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzChangedUserParamOldValues"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzChangedUserParamNewValues"))
)
if mibBuilder.loadTexts:
    trpzClientDynAuthorChangeSuccessTrap.setStatus(
        "obsolete"
    )

trpzClientDynAuthorChangeFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 48)
)
trpzClientDynAuthorChangeFailureTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDynAuthorClientIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserParams"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthorizationFailureCause"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientFailureCauseDescription"))
)
if mibBuilder.loadTexts:
    trpzClientDynAuthorChangeFailureTrap.setStatus(
        "current"
    )

trpzClientDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 49)
)
trpzClientDisconnectTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDAPNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzLocalId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDisconnectSource"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDisconnectDescription"))
)
if mibBuilder.loadTexts:
    trpzClientDisconnectTrap.setStatus(
        "obsolete"
    )

trpzMobilityDomainFailOverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 50)
)
trpzMobilityDomainFailOverTrap.setObjects(
    ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMobilityDomainSecondarySeedIp")
)
if mibBuilder.loadTexts:
    trpzMobilityDomainFailOverTrap.setStatus(
        "current"
    )

trpzMobilityDomainFailBackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 51)
)
trpzMobilityDomainFailBackTrap.setObjects(
    ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMobilityDomainPrimarySeedIp")
)
if mibBuilder.loadTexts:
    trpzMobilityDomainFailBackTrap.setStatus(
        "current"
    )

trpzRFDetectRogueDeviceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 52)
)
trpzRFDetectRogueDeviceTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectListenerListInfo"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectClassificationReason"))
)
if mibBuilder.loadTexts:
    trpzRFDetectRogueDeviceTrap.setStatus(
        "obsolete"
    )

trpzRFDetectRogueDeviceDisappearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 53)
)
trpzRFDetectRogueDeviceDisappearTrap.setObjects(
    ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr")
)
if mibBuilder.loadTexts:
    trpzRFDetectRogueDeviceDisappearTrap.setStatus(
        "current"
    )

trpzRFDetectSuspectDeviceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 54)
)
trpzRFDetectSuspectDeviceTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectListenerListInfo"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectClassificationReason"))
)
if mibBuilder.loadTexts:
    trpzRFDetectSuspectDeviceTrap.setStatus(
        "obsolete"
    )

trpzRFDetectSuspectDeviceDisappearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 55)
)
trpzRFDetectSuspectDeviceDisappearTrap.setObjects(
    ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr")
)
if mibBuilder.loadTexts:
    trpzRFDetectSuspectDeviceDisappearTrap.setStatus(
        "current"
    )

trpzRFDetectClientViaRogueWiredAPTrap3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 56)
)
trpzRFDetectClientViaRogueWiredAPTrap3.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzSourceWsIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANid"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANtag"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectListenerListInfo"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectRogueAPMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectClassificationReason"))
)
if mibBuilder.loadTexts:
    trpzRFDetectClientViaRogueWiredAPTrap3.setStatus(
        "current"
    )

trpzRFDetectClassificationChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 57)
)
if mibBuilder.loadTexts:
    trpzRFDetectClassificationChangeTrap.setStatus(
        "current"
    )

trpzConfigurationSavedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 58)
)
trpzConfigurationSavedTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzConfigSaveFileName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzConfigSaveInitiatorType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzConfigSaveInitiatorIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzConfigSaveInitiatorDetails"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzConfigSaveGeneration"))
)
if mibBuilder.loadTexts:
    trpzConfigurationSavedTrap.setStatus(
        "current"
    )

trpzApNonOperStatusTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 59)
)
trpzApNonOperStatusTrap2.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDeviceSerNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApTransition"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApFailDetail"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApWasOperational"))
)
if mibBuilder.loadTexts:
    trpzApNonOperStatusTrap2.setStatus(
        "current"
    )

trpzApOperRadioStatusTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 60)
)
trpzApOperRadioStatusTrap2.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDeviceSerNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioMode"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioConfigState"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApConnectSecurityType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApServiceAvailability"))
)
if mibBuilder.loadTexts:
    trpzApOperRadioStatusTrap2.setStatus(
        "obsolete"
    )

trpzMichaelMICFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 61)
)
trpzMichaelMICFailure.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMichaelMICFailureCause"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress2"))
)
if mibBuilder.loadTexts:
    trpzMichaelMICFailure.setStatus(
        "current"
    )

trpzClientAuthorizationSuccessTrap3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 62)
)
trpzClientAuthorizationSuccessTrap3.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionState"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessMode"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPhysPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzLocalId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthorizationReason"))
)
if mibBuilder.loadTexts:
    trpzClientAuthorizationSuccessTrap3.setStatus(
        "obsolete"
    )

trpzApManagerChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 63)
)
trpzApManagerChangeTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDeviceSerNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApMgrOldIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApMgrNewIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApMgrChangeReason"))
)
if mibBuilder.loadTexts:
    trpzApManagerChangeTrap.setStatus(
        "current"
    )

trpzClientClearedTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 64)
)
trpzClientClearedTrap2.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessMode"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPhysPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionElapsedSeconds"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzLocalId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientClearedReason"))
)
if mibBuilder.loadTexts:
    trpzClientClearedTrap2.setStatus(
        "obsolete"
    )

trpzMobilityDomainResiliencyStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 65)
)
trpzMobilityDomainResiliencyStatusTrap.setObjects(
    ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMobilityDomainResiliencyStatus")
)
if mibBuilder.loadTexts:
    trpzMobilityDomainResiliencyStatusTrap.setStatus(
        "current"
    )

trpzApOperRadioStatusTrap3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 66)
)
trpzApOperRadioStatusTrap3.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDeviceSerNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioMode"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioConfigState"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioChannelWidth"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioMimoState"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApConnectSecurityType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApServiceAvailability"))
)
if mibBuilder.loadTexts:
    trpzApOperRadioStatusTrap3.setStatus(
        "current"
    )

trpzClientAuthorizationSuccessTrap4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 67)
)
trpzClientAuthorizationSuccessTrap4.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionState"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessMode"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPhysPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientRadioType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzLocalId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthorizationReason"))
)
if mibBuilder.loadTexts:
    trpzClientAuthorizationSuccessTrap4.setStatus(
        "obsolete"
    )

trpzRFDetectRogueDeviceTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 68)
)
trpzRFDetectRogueDeviceTrap2.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrRadioType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrCryptoType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectListenerListInfo"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectClassificationReason"))
)
if mibBuilder.loadTexts:
    trpzRFDetectRogueDeviceTrap2.setStatus(
        "current"
    )

trpzRFDetectSuspectDeviceTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 69)
)
trpzRFDetectSuspectDeviceTrap2.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrMacAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrRadioType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectXmtrCryptoType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectListenerListInfo"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFDetectClassificationReason"))
)
if mibBuilder.loadTexts:
    trpzRFDetectSuspectDeviceTrap2.setStatus(
        "current"
    )

trpzClusterFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 70)
)
trpzClusterFailureTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClusterFailureReason"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClusterFailureDescription"))
)
if mibBuilder.loadTexts:
    trpzClusterFailureTrap.setStatus(
        "current"
    )

trpzMultimediaCallFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 71)
)
trpzMultimediaCallFailureTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessMode"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPhysPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPRadioNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMultimediaCommunicationServerID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMultimediaCallDirection"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMultimediaLocalStationIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMultimediaLocalStationPort"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMultimediaLocalStationEndpointID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMultimediaRemoteStationIp"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMultimediaRemoteStationPort"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMultimediaRemoteStationEndpointID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMultimediaSignalingProtocol"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMultimediaCallBandwidthAndCodec"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMultimediaCallDataRate"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMultimediaCallRssi"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzMultimediaCallFailureReason"))
)
if mibBuilder.loadTexts:
    trpzMultimediaCallFailureTrap.setStatus(
        "current"
    )

trpzApTunnelLimitExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 72)
)
trpzApTunnelLimitExceededTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzDeviceSerNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAPMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApTunnelLimit"))
)
if mibBuilder.loadTexts:
    trpzApTunnelLimitExceededTrap.setStatus(
        "current"
    )

trpzWsTunnelLimitExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 73)
)
trpzWsTunnelLimitExceededTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzWsTunnelLimit"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzWsTunnelLimitType"))
)
if mibBuilder.loadTexts:
    trpzWsTunnelLimitExceededTrap.setStatus(
        "current"
    )

trpzRFNoiseSourceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 74)
)
trpzRFNoiseSourceTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFNoiseSourceID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFNoiseSourceType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFNoiseChannel"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFNoiseRssi"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFNoiseDutyCycle"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFNoiseChannelInterferenceMeasure"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRFNoiseAge"))
)
if mibBuilder.loadTexts:
    trpzRFNoiseSourceTrap.setStatus(
        "current"
    )

trpzM2UConvNotPossibleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 75)
)
trpzM2UConvNotPossibleTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzM2UMulticastAddrType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzM2UMulticastAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzM2UConvNotPossibleReason"))
)
if mibBuilder.loadTexts:
    trpzM2UConvNotPossibleTrap.setStatus(
        "current"
    )

trpzM2UConvAvailabilityRestoredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 76)
)
trpzM2UConvAvailabilityRestoredTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzM2UMulticastAddrType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzM2UMulticastAddr"))
)
if mibBuilder.loadTexts:
    trpzM2UConvAvailabilityRestoredTrap.setStatus(
        "current"
    )

trpzAutoTuneSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 77)
)
trpzAutoTuneSuccessTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioBand"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadiosTunedCount"))
)
if mibBuilder.loadTexts:
    trpzAutoTuneSuccessTrap.setStatus(
        "current"
    )

trpzAutoTuneFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 78)
)
trpzAutoTuneFailureTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioBand"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzAutoTuneFailureReason"))
)
if mibBuilder.loadTexts:
    trpzAutoTuneFailureTrap.setStatus(
        "current"
    )

trpzClientDeAssociationTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 79)
)
trpzClientDeAssociationTrap2.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv4Addr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv6LinkLocalAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerAddrType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessMode"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPhysPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApRadioIndex"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"))
)
if mibBuilder.loadTexts:
    trpzClientDeAssociationTrap2.setStatus(
        "current"
    )

trpzClientRoamingTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 80)
)
trpzClientRoamingTrap2.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv4Addr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv6LinkLocalAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessMode"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPhysPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApRadioIndex"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientRoamedFromAccessMode"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientRoamedFromPhysPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientRoamedFromApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientRoamedFromRadioIndex"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientRoamedFromWsAddrType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientRoamedFromWsAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientTimeSinceLastRoam"))
)
if mibBuilder.loadTexts:
    trpzClientRoamingTrap2.setStatus(
        "current"
    )

trpzClientIpAddrChangeTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 81)
)
trpzClientIpAddrChangeTrap2.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIpAddrType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIpAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionState"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerAddrType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessMode"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPhysPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApRadioIndex"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzLocalId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIpAddrChangeReason"))
)
if mibBuilder.loadTexts:
    trpzClientIpAddrChangeTrap2.setStatus(
        "current"
    )

trpzClientDeAuthenticationTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 82)
)
trpzClientDeAuthenticationTrap2.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv4Addr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv6LinkLocalAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerAddrType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessMode"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPhysPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApRadioIndex"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"))
)
if mibBuilder.loadTexts:
    trpzClientDeAuthenticationTrap2.setStatus(
        "current"
    )

trpzClientDynAuthorChangeSuccessTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 83)
)
trpzClientDynAuthorChangeSuccessTrap2.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv4Addr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv6LinkLocalAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionState"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDynAuthorClientAddrType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDynAuthorClientAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessMode"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPhysPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApRadioIndex"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzLocalId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzChangedUserParamOldValues"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzChangedUserParamNewValues"))
)
if mibBuilder.loadTexts:
    trpzClientDynAuthorChangeSuccessTrap2.setStatus(
        "current"
    )

trpzClientDisconnectTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 84)
)
trpzClientDisconnectTrap2.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv4Addr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv6LinkLocalAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessMode"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPhysPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApRadioIndex"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzLocalId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDisconnectSource"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDisconnectDescription"))
)
if mibBuilder.loadTexts:
    trpzClientDisconnectTrap2.setStatus(
        "current"
    )

trpzClientClearedTrap3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 85)
)
trpzClientClearedTrap3.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv4Addr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv6LinkLocalAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessMode"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPhysPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApRadioIndex"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionElapsedSeconds"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzLocalId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientClearedReason"))
)
if mibBuilder.loadTexts:
    trpzClientClearedTrap3.setStatus(
        "current"
    )

trpzClientAuthorizationSuccessTrap5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 86)
)
trpzClientAuthorizationSuccessTrap5.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv4Addr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv6LinkLocalAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionState"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerAddrType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessMode"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPhysPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApRadioIndex"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientRadioType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzLocalId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthorizationReason"))
)
if mibBuilder.loadTexts:
    trpzClientAuthorizationSuccessTrap5.setStatus(
        "current"
    )

trpzClientDeviceTypeChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 87)
)
trpzClientDeviceTypeChangeTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv4Addr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv6LinkLocalAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDeviceType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDeviceTypeOld"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDeviceGroup"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDeviceProfileName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionState"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerAddrType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessMode"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPhysPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApRadioIndex"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzLocalId"))
)
if mibBuilder.loadTexts:
    trpzClientDeviceTypeChangeTrap.setStatus(
        "current"
    )

trpzClientDeviceProfileChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14525, 5, 0, 88)
)
trpzClientDeviceProfileChangeTrap.setObjects(
      *(("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionId"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientMACAddress"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv4Addr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientIPv6LinkLocalAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDeviceType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDeviceGroup"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDeviceProfileName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDeviceProfileNameOld"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientDeviceProfileChangeReason"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientVLANName"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientSessionState"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerAddrType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthServerAddr"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAuthenProtocolType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzClientAccessMode"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzPhysPortNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApNum"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzApRadioIndex"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzRadioSSID"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzUserAccessType"),
        ("TRAPEZE-NETWORKS-TRAP-MIB", "trpzLocalId"))
)
if mibBuilder.loadTexts:
    trpzClientDeviceProfileChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-TRAP-MIB",
    **{"TrpzAssociationFailureType": TrpzAssociationFailureType,
       "TrpzAuthenticationFailureType": TrpzAuthenticationFailureType,
       "TrpzAuthorizationFailureType": TrpzAuthorizationFailureType,
       "TrpzDot1xFailureType": TrpzDot1xFailureType,
       "TrpzRFDetectDoSType": TrpzRFDetectDoSType,
       "TrpzClientIpAddrChangeReason": TrpzClientIpAddrChangeReason,
       "TrpzBlacklistingCause": TrpzBlacklistingCause,
       "TrpzUserAttributeList": TrpzUserAttributeList,
       "TrpzSessionDisconnectType": TrpzSessionDisconnectType,
       "TrpzConfigSaveInitiatorType": TrpzConfigSaveInitiatorType,
       "TrpzMichaelMICFailureCause": TrpzMichaelMICFailureCause,
       "TrpzClientAuthorizationReason": TrpzClientAuthorizationReason,
       "TrpzApMgrChangeReason": TrpzApMgrChangeReason,
       "TrpzClientClearedReason": TrpzClientClearedReason,
       "TrpzMobilityDomainResiliencyStatus": TrpzMobilityDomainResiliencyStatus,
       "TrpzClusterFailureReason": TrpzClusterFailureReason,
       "TrpzMultimediaSignalingProtocol": TrpzMultimediaSignalingProtocol,
       "TrpzMultimediaCallFailureReason": TrpzMultimediaCallFailureReason,
       "TrpzMultimediaCallDirection": TrpzMultimediaCallDirection,
       "TrpzWsTunnelLimitType": TrpzWsTunnelLimitType,
       "TrpzM2UConvNotPossibleReason": TrpzM2UConvNotPossibleReason,
       "TrpzRadioBand": TrpzRadioBand,
       "TrpzAutoTuneFailureReason": TrpzAutoTuneFailureReason,
       "TrpzClientDeviceProfileChangeReason": TrpzClientDeviceProfileChangeReason,
       "trpzDeviceId": trpzDeviceId,
       "trpzMobilityDomainIp": trpzMobilityDomainIp,
       "trpzAPMACAddress": trpzAPMACAddress,
       "trpzClientMACAddress": trpzClientMACAddress,
       "trpzRFDetectXmtrMacAddr": trpzRFDetectXmtrMacAddr,
       "trpzPortNum": trpzPortNum,
       "trpzAPRadioNum": trpzAPRadioNum,
       "trpzRadioRssi": trpzRadioRssi,
       "trpzRadioBSSID": trpzRadioBSSID,
       "trpzUserName": trpzUserName,
       "trpzClientAuthServerIp": trpzClientAuthServerIp,
       "trpzClientSessionState": trpzClientSessionState,
       "trpzDAPNum": trpzDAPNum,
       "trpzClientIp": trpzClientIp,
       "trpzClientSessionId": trpzClientSessionId,
       "trpzClientAuthenProtocolType": trpzClientAuthenProtocolType,
       "trpzClientVLANName": trpzClientVLANName,
       "trpzClientSessionStartTime": trpzClientSessionStartTime,
       "trpzClientFailureCause": trpzClientFailureCause,
       "trpzClientRoamedFromPortNum": trpzClientRoamedFromPortNum,
       "trpzClientRoamedFromRadioNum": trpzClientRoamedFromRadioNum,
       "trpzClientRoamedFromDAPNum": trpzClientRoamedFromDAPNum,
       "trpzUserParams": trpzUserParams,
       "trpzClientLocationPolicyIndex": trpzClientLocationPolicyIndex,
       "trpzClientAssociationFailureCause": trpzClientAssociationFailureCause,
       "trpzClientAuthenticationFailureCause": trpzClientAuthenticationFailureCause,
       "trpzClientAuthorizationFailureCause": trpzClientAuthorizationFailureCause,
       "trpzClientFailureCauseDescription": trpzClientFailureCauseDescription,
       "trpzClientRoamedFromWsIp": trpzClientRoamedFromWsIp,
       "trpzClientRoamedFromAccessType": trpzClientRoamedFromAccessType,
       "trpzClientAccessType": trpzClientAccessType,
       "trpzRadioMACAddress": trpzRadioMACAddress,
       "trpzRadioPowerChangeReason": trpzRadioPowerChangeReason,
       "trpzNewChannelNum": trpzNewChannelNum,
       "trpzOldChannelNum": trpzOldChannelNum,
       "trpzChannelChangeReason": trpzChannelChangeReason,
       "trpzRFDetectListenerListInfo": trpzRFDetectListenerListInfo,
       "trpzRadioSSID": trpzRadioSSID,
       "trpzNewPowerLevel": trpzNewPowerLevel,
       "trpzOldPowerLevel": trpzOldPowerLevel,
       "trpzRadioPowerChangeDescription": trpzRadioPowerChangeDescription,
       "trpzCounterMeasurePerformerListInfo": trpzCounterMeasurePerformerListInfo,
       "trpzClientDot1xState": trpzClientDot1xState,
       "trpzClientDot1xFailureCause": trpzClientDot1xFailureCause,
       "trpzAPAccessType": trpzAPAccessType,
       "trpzUserAccessType": trpzUserAccessType,
       "trpzClientSessionElapsedTime": trpzClientSessionElapsedTime,
       "trpzLocalId": trpzLocalId,
       "trpzRFDetectDoSType": trpzRFDetectDoSType,
       "trpzSourceWsIp": trpzSourceWsIp,
       "trpzClientVLANid": trpzClientVLANid,
       "trpzClientVLANtag": trpzClientVLANtag,
       "trpzDeviceModel": trpzDeviceModel,
       "trpzDeviceSerNum": trpzDeviceSerNum,
       "trpzRsaPubKeyFingerPrint": trpzRsaPubKeyFingerPrint,
       "trpzDAPconnectWarningType": trpzDAPconnectWarningType,
       "trpzClientMACAddress2": trpzClientMACAddress2,
       "trpzApAttachType": trpzApAttachType,
       "trpzApPortOrDapNum": trpzApPortOrDapNum,
       "trpzApName": trpzApName,
       "trpzApTransition": trpzApTransition,
       "trpzApFailDetail": trpzApFailDetail,
       "trpzRadioType": trpzRadioType,
       "trpzRadioConfigState": trpzRadioConfigState,
       "trpzApConnectSecurityType": trpzApConnectSecurityType,
       "trpzApServiceAvailability": trpzApServiceAvailability,
       "trpzApWasOperational": trpzApWasOperational,
       "trpzClientTimeSinceLastRoam": trpzClientTimeSinceLastRoam,
       "trpzClientIpAddrChangeReason": trpzClientIpAddrChangeReason,
       "trpzRFDetectRogueAPMacAddr": trpzRFDetectRogueAPMacAddr,
       "trpzBlacklistingRemainingTime": trpzBlacklistingRemainingTime,
       "trpzBlacklistingCause": trpzBlacklistingCause,
       "trpzNumLicensedActiveAPs": trpzNumLicensedActiveAPs,
       "trpzClientDynAuthorClientIp": trpzClientDynAuthorClientIp,
       "trpzChangedUserParamOldValues": trpzChangedUserParamOldValues,
       "trpzChangedUserParamNewValues": trpzChangedUserParamNewValues,
       "trpzClientDisconnectSource": trpzClientDisconnectSource,
       "trpzClientDisconnectDescription": trpzClientDisconnectDescription,
       "trpzMobilityDomainSecondarySeedIp": trpzMobilityDomainSecondarySeedIp,
       "trpzMobilityDomainPrimarySeedIp": trpzMobilityDomainPrimarySeedIp,
       "trpzRFDetectClassificationReason": trpzRFDetectClassificationReason,
       "trpzConfigSaveFileName": trpzConfigSaveFileName,
       "trpzConfigSaveInitiatorType": trpzConfigSaveInitiatorType,
       "trpzConfigSaveInitiatorIp": trpzConfigSaveInitiatorIp,
       "trpzConfigSaveInitiatorDetails": trpzConfigSaveInitiatorDetails,
       "trpzConfigSaveGeneration": trpzConfigSaveGeneration,
       "trpzApNum": trpzApNum,
       "trpzRadioMode": trpzRadioMode,
       "trpzMichaelMICFailureCause": trpzMichaelMICFailureCause,
       "trpzClientAccessMode": trpzClientAccessMode,
       "trpzClientAuthorizationReason": trpzClientAuthorizationReason,
       "trpzPhysPortNum": trpzPhysPortNum,
       "trpzApMgrOldIp": trpzApMgrOldIp,
       "trpzApMgrNewIp": trpzApMgrNewIp,
       "trpzApMgrChangeReason": trpzApMgrChangeReason,
       "trpzClientClearedReason": trpzClientClearedReason,
       "trpzMobilityDomainResiliencyStatus": trpzMobilityDomainResiliencyStatus,
       "trpzClientSessionElapsedSeconds": trpzClientSessionElapsedSeconds,
       "trpzRadioChannelWidth": trpzRadioChannelWidth,
       "trpzRadioMimoState": trpzRadioMimoState,
       "trpzClientRadioType": trpzClientRadioType,
       "trpzRFDetectXmtrRadioType": trpzRFDetectXmtrRadioType,
       "trpzRFDetectXmtrCryptoType": trpzRFDetectXmtrCryptoType,
       "trpzClusterFailureReason": trpzClusterFailureReason,
       "trpzClusterFailureDescription": trpzClusterFailureDescription,
       "trpzMultimediaCommunicationServerID": trpzMultimediaCommunicationServerID,
       "trpzMultimediaLocalStationIp": trpzMultimediaLocalStationIp,
       "trpzMultimediaLocalStationPort": trpzMultimediaLocalStationPort,
       "trpzMultimediaLocalStationEndpointID": trpzMultimediaLocalStationEndpointID,
       "trpzMultimediaRemoteStationIp": trpzMultimediaRemoteStationIp,
       "trpzMultimediaRemoteStationPort": trpzMultimediaRemoteStationPort,
       "trpzMultimediaRemoteStationEndpointID": trpzMultimediaRemoteStationEndpointID,
       "trpzMultimediaSignalingProtocol": trpzMultimediaSignalingProtocol,
       "trpzMultimediaCallBandwidthAndCodec": trpzMultimediaCallBandwidthAndCodec,
       "trpzMultimediaCallDataRate": trpzMultimediaCallDataRate,
       "trpzMultimediaCallRssi": trpzMultimediaCallRssi,
       "trpzMultimediaCallFailureReason": trpzMultimediaCallFailureReason,
       "trpzMultimediaCallDirection": trpzMultimediaCallDirection,
       "trpzApTunnelLimit": trpzApTunnelLimit,
       "trpzWsTunnelLimit": trpzWsTunnelLimit,
       "trpzWsTunnelLimitType": trpzWsTunnelLimitType,
       "trpzRFNoiseSourceID": trpzRFNoiseSourceID,
       "trpzRFNoiseSourceType": trpzRFNoiseSourceType,
       "trpzRFNoiseChannel": trpzRFNoiseChannel,
       "trpzRFNoiseRssi": trpzRFNoiseRssi,
       "trpzRFNoiseDutyCycle": trpzRFNoiseDutyCycle,
       "trpzRFNoiseChannelInterferenceMeasure": trpzRFNoiseChannelInterferenceMeasure,
       "trpzRFNoiseAge": trpzRFNoiseAge,
       "trpzM2UMulticastAddrType": trpzM2UMulticastAddrType,
       "trpzM2UMulticastAddr": trpzM2UMulticastAddr,
       "trpzM2UConvNotPossibleReason": trpzM2UConvNotPossibleReason,
       "trpzRadioBand": trpzRadioBand,
       "trpzRadiosTunedCount": trpzRadiosTunedCount,
       "trpzAutoTuneFailureReason": trpzAutoTuneFailureReason,
       "trpzClientAuthServerAddrType": trpzClientAuthServerAddrType,
       "trpzClientAuthServerAddr": trpzClientAuthServerAddr,
       "trpzClientRoamedFromWsAddrType": trpzClientRoamedFromWsAddrType,
       "trpzClientRoamedFromWsAddr": trpzClientRoamedFromWsAddr,
       "trpzClientDynAuthorClientAddrType": trpzClientDynAuthorClientAddrType,
       "trpzClientDynAuthorClientAddr": trpzClientDynAuthorClientAddr,
       "trpzClientIpAddrType": trpzClientIpAddrType,
       "trpzClientIpAddr": trpzClientIpAddr,
       "trpzClientIPv4Addr": trpzClientIPv4Addr,
       "trpzClientIPv6LinkLocalAddr": trpzClientIPv6LinkLocalAddr,
       "trpzApRadioIndex": trpzApRadioIndex,
       "trpzClientRoamedFromAccessMode": trpzClientRoamedFromAccessMode,
       "trpzClientRoamedFromApNum": trpzClientRoamedFromApNum,
       "trpzClientRoamedFromRadioIndex": trpzClientRoamedFromRadioIndex,
       "trpzClientRoamedFromPhysPortNum": trpzClientRoamedFromPhysPortNum,
       "trpzClientDeviceType": trpzClientDeviceType,
       "trpzClientDeviceTypeOld": trpzClientDeviceTypeOld,
       "trpzClientDeviceGroup": trpzClientDeviceGroup,
       "trpzClientDeviceProfileName": trpzClientDeviceProfileName,
       "trpzClientDeviceProfileNameOld": trpzClientDeviceProfileNameOld,
       "trpzClientDeviceProfileChangeReason": trpzClientDeviceProfileChangeReason,
       "trpzTrapMib": trpzTrapMib,
       "trpzTrapsV2": trpzTrapsV2,
       "trpzDeviceFailTrap": trpzDeviceFailTrap,
       "trpzDeviceOkayTrap": trpzDeviceOkayTrap,
       "trpzPoEFailTrap": trpzPoEFailTrap,
       "trpzApTimeoutTrap": trpzApTimeoutTrap,
       "trpzAPBootTrap": trpzAPBootTrap,
       "trpzMobilityDomainJoinTrap": trpzMobilityDomainJoinTrap,
       "trpzMobilityDomainTimeoutTrap": trpzMobilityDomainTimeoutTrap,
       "trpzMpMichaelMICFailure": trpzMpMichaelMICFailure,
       "trpzRFDetectRogueAPTrap": trpzRFDetectRogueAPTrap,
       "trpzRFDetectAdhocUserTrap": trpzRFDetectAdhocUserTrap,
       "trpzRFDetectRogueDisappearTrap": trpzRFDetectRogueDisappearTrap,
       "trpzClientAuthenticationFailureTrap": trpzClientAuthenticationFailureTrap,
       "trpzClientAuthorizationFailureTrap": trpzClientAuthorizationFailureTrap,
       "trpzClientAssociationFailureTrap": trpzClientAssociationFailureTrap,
       "trpzClientAuthorizationSuccessTrap": trpzClientAuthorizationSuccessTrap,
       "trpzClientDeAssociationTrap": trpzClientDeAssociationTrap,
       "trpzClientRoamingTrap": trpzClientRoamingTrap,
       "trpzAutoTuneRadioPowerChangeTrap": trpzAutoTuneRadioPowerChangeTrap,
       "trpzAutoTuneRadioChannelChangeTrap": trpzAutoTuneRadioChannelChangeTrap,
       "trpzCounterMeasureStartTrap": trpzCounterMeasureStartTrap,
       "trpzCounterMeasureStopTrap": trpzCounterMeasureStopTrap,
       "trpzClientDot1xFailureTrap": trpzClientDot1xFailureTrap,
       "trpzClientClearedTrap": trpzClientClearedTrap,
       "trpzClientAuthorizationSuccessTrap2": trpzClientAuthorizationSuccessTrap2,
       "trpzRFDetectSpoofedMacAPTrap": trpzRFDetectSpoofedMacAPTrap,
       "trpzRFDetectSpoofedSsidAPTrap": trpzRFDetectSpoofedSsidAPTrap,
       "trpzRFDetectDoSTrap": trpzRFDetectDoSTrap,
       "trpzRFDetectClientViaRogueWiredAPTrap": trpzRFDetectClientViaRogueWiredAPTrap,
       "trpzRFDetectInterferingRogueAPTrap": trpzRFDetectInterferingRogueAPTrap,
       "trpzRFDetectInterferingRogueDisappearTrap": trpzRFDetectInterferingRogueDisappearTrap,
       "trpzRFDetectUnAuthorizedSsidTrap": trpzRFDetectUnAuthorizedSsidTrap,
       "trpzRFDetectUnAuthorizedOuiTrap": trpzRFDetectUnAuthorizedOuiTrap,
       "trpzRFDetectUnAuthorizedAPTrap": trpzRFDetectUnAuthorizedAPTrap,
       "trpzDAPConnectWarningTrap": trpzDAPConnectWarningTrap,
       "trpzRFDetectDoSPortTrap": trpzRFDetectDoSPortTrap,
       "trpzMpMichaelMICFailure2": trpzMpMichaelMICFailure2,
       "trpzApNonOperStatusTrap": trpzApNonOperStatusTrap,
       "trpzApOperRadioStatusTrap": trpzApOperRadioStatusTrap,
       "trpzClientIpAddrChangeTrap": trpzClientIpAddrChangeTrap,
       "trpzClientAssociationSuccessTrap": trpzClientAssociationSuccessTrap,
       "trpzClientAuthenticationSuccessTrap": trpzClientAuthenticationSuccessTrap,
       "trpzClientDeAuthenticationTrap": trpzClientDeAuthenticationTrap,
       "trpzRFDetectBlacklistedTrap": trpzRFDetectBlacklistedTrap,
       "trpzRFDetectClientViaRogueWiredAPTrap2": trpzRFDetectClientViaRogueWiredAPTrap2,
       "trpzRFDetectAdhocUserDisappearTrap": trpzRFDetectAdhocUserDisappearTrap,
       "trpzApRejectLicenseExceededTrap": trpzApRejectLicenseExceededTrap,
       "trpzClientDynAuthorChangeSuccessTrap": trpzClientDynAuthorChangeSuccessTrap,
       "trpzClientDynAuthorChangeFailureTrap": trpzClientDynAuthorChangeFailureTrap,
       "trpzClientDisconnectTrap": trpzClientDisconnectTrap,
       "trpzMobilityDomainFailOverTrap": trpzMobilityDomainFailOverTrap,
       "trpzMobilityDomainFailBackTrap": trpzMobilityDomainFailBackTrap,
       "trpzRFDetectRogueDeviceTrap": trpzRFDetectRogueDeviceTrap,
       "trpzRFDetectRogueDeviceDisappearTrap": trpzRFDetectRogueDeviceDisappearTrap,
       "trpzRFDetectSuspectDeviceTrap": trpzRFDetectSuspectDeviceTrap,
       "trpzRFDetectSuspectDeviceDisappearTrap": trpzRFDetectSuspectDeviceDisappearTrap,
       "trpzRFDetectClientViaRogueWiredAPTrap3": trpzRFDetectClientViaRogueWiredAPTrap3,
       "trpzRFDetectClassificationChangeTrap": trpzRFDetectClassificationChangeTrap,
       "trpzConfigurationSavedTrap": trpzConfigurationSavedTrap,
       "trpzApNonOperStatusTrap2": trpzApNonOperStatusTrap2,
       "trpzApOperRadioStatusTrap2": trpzApOperRadioStatusTrap2,
       "trpzMichaelMICFailure": trpzMichaelMICFailure,
       "trpzClientAuthorizationSuccessTrap3": trpzClientAuthorizationSuccessTrap3,
       "trpzApManagerChangeTrap": trpzApManagerChangeTrap,
       "trpzClientClearedTrap2": trpzClientClearedTrap2,
       "trpzMobilityDomainResiliencyStatusTrap": trpzMobilityDomainResiliencyStatusTrap,
       "trpzApOperRadioStatusTrap3": trpzApOperRadioStatusTrap3,
       "trpzClientAuthorizationSuccessTrap4": trpzClientAuthorizationSuccessTrap4,
       "trpzRFDetectRogueDeviceTrap2": trpzRFDetectRogueDeviceTrap2,
       "trpzRFDetectSuspectDeviceTrap2": trpzRFDetectSuspectDeviceTrap2,
       "trpzClusterFailureTrap": trpzClusterFailureTrap,
       "trpzMultimediaCallFailureTrap": trpzMultimediaCallFailureTrap,
       "trpzApTunnelLimitExceededTrap": trpzApTunnelLimitExceededTrap,
       "trpzWsTunnelLimitExceededTrap": trpzWsTunnelLimitExceededTrap,
       "trpzRFNoiseSourceTrap": trpzRFNoiseSourceTrap,
       "trpzM2UConvNotPossibleTrap": trpzM2UConvNotPossibleTrap,
       "trpzM2UConvAvailabilityRestoredTrap": trpzM2UConvAvailabilityRestoredTrap,
       "trpzAutoTuneSuccessTrap": trpzAutoTuneSuccessTrap,
       "trpzAutoTuneFailureTrap": trpzAutoTuneFailureTrap,
       "trpzClientDeAssociationTrap2": trpzClientDeAssociationTrap2,
       "trpzClientRoamingTrap2": trpzClientRoamingTrap2,
       "trpzClientIpAddrChangeTrap2": trpzClientIpAddrChangeTrap2,
       "trpzClientDeAuthenticationTrap2": trpzClientDeAuthenticationTrap2,
       "trpzClientDynAuthorChangeSuccessTrap2": trpzClientDynAuthorChangeSuccessTrap2,
       "trpzClientDisconnectTrap2": trpzClientDisconnectTrap2,
       "trpzClientClearedTrap3": trpzClientClearedTrap3,
       "trpzClientAuthorizationSuccessTrap5": trpzClientAuthorizationSuccessTrap5,
       "trpzClientDeviceTypeChangeTrap": trpzClientDeviceTypeChangeTrap,
       "trpzClientDeviceProfileChangeTrap": trpzClientDeviceProfileChangeTrap}
)
