# SNMP MIB module (RBTWS-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBTWS-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:40 2024
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

(RbtwsAccessType,
 RbtwsApAttachType,
 RbtwsApConnectSecurityType,
 RbtwsApFailDetail,
 RbtwsApFingerprint,
 RbtwsApNum,
 RbtwsApPortOrDapNum,
 RbtwsApSerialNum,
 RbtwsApServiceAvailability,
 RbtwsApTransition,
 RbtwsApWasOperational,
 RbtwsChannelChangeType,
 RbtwsCryptoType,
 RbtwsPowerLevel,
 RbtwsRadioChannelWidth,
 RbtwsRadioConfigState,
 RbtwsRadioMimoState,
 RbtwsRadioMode,
 RbtwsRadioNum,
 RbtwsRadioPowerChangeType,
 RbtwsRadioType) = mibBuilder.importSymbols(
    "RBTWS-AP-TC",
    "RbtwsAccessType",
    "RbtwsApAttachType",
    "RbtwsApConnectSecurityType",
    "RbtwsApFailDetail",
    "RbtwsApFingerprint",
    "RbtwsApNum",
    "RbtwsApPortOrDapNum",
    "RbtwsApSerialNum",
    "RbtwsApServiceAvailability",
    "RbtwsApTransition",
    "RbtwsApWasOperational",
    "RbtwsChannelChangeType",
    "RbtwsCryptoType",
    "RbtwsPowerLevel",
    "RbtwsRadioChannelWidth",
    "RbtwsRadioConfigState",
    "RbtwsRadioMimoState",
    "RbtwsRadioMode",
    "RbtwsRadioNum",
    "RbtwsRadioPowerChangeType",
    "RbtwsRadioType")

(RbtwsClientAccessMode,
 RbtwsClientAuthenProtocolType,
 RbtwsClientDot1xState,
 RbtwsClientSessionState,
 RbtwsUserAccessType) = mibBuilder.importSymbols(
    "RBTWS-CLIENT-SESSION-TC",
    "RbtwsClientAccessMode",
    "RbtwsClientAuthenProtocolType",
    "RbtwsClientDot1xState",
    "RbtwsClientSessionState",
    "RbtwsUserAccessType")

(RbtwsRFDetectClassificationReason,) = mibBuilder.importSymbols(
    "RBTWS-RF-DETECT-TC",
    "RbtwsRFDetectClassificationReason")

(rbtwsMibs,
 rbtwsTemporary,
 rbtwsTraps) = mibBuilder.importSymbols(
    "RBTWS-ROOT-MIB",
    "rbtwsMibs",
    "rbtwsTemporary",
    "rbtwsTraps")

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


# MODULE-IDENTITY

rbtwsTrapMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 1)
)
rbtwsTrapMib.setRevisions(
        ("2008-05-15 02:15",
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



class RbtwsAssociationFailureType(Integer32, TextualConvention):
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



class RbtwsAuthenticationFailureType(Integer32, TextualConvention):
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



class RbtwsAuthorizationFailureType(Integer32, TextualConvention):
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



class RbtwsDot1xFailureType(Integer32, TextualConvention):
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



class RbtwsRFDetectDoSType(Integer32, TextualConvention):
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



class RbtwsClientIpAddrChangeReason(Integer32, TextualConvention):
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
        *(("client-connected", 1),
          ("dhcp-to-static", 3),
          ("other", 2))
    )



class RbtwsBlacklistingCause(Integer32, TextualConvention):
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



class RbtwsUserAttributeList(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )



class RbtwsSessionDisconnectType(Integer32, TextualConvention):
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



class RbtwsConfigSaveInitiatorType(Integer32, TextualConvention):
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



class RbtwsMichaelMICFailureCause(Integer32, TextualConvention):
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



class RbtwsClientAuthorizationReason(Integer32, TextualConvention):
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



class RbtwsApMgrChangeReason(Integer32, TextualConvention):
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



class RbtwsClientClearedReason(Integer32, TextualConvention):
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



class RbtwsMobilityDomainResiliencyStatus(Integer32, TextualConvention):
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



class RbtwsClusterFailureReason(Integer32, TextualConvention):
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



# MIB Managed Objects in the order of their OIDs

_RbtwsDeviceId_Type = ObjectIdentifier
_RbtwsDeviceId_Object = MibScalar
rbtwsDeviceId = _RbtwsDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 1),
    _RbtwsDeviceId_Type()
)
rbtwsDeviceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsDeviceId.setStatus("current")
_RbtwsMobilityDomainIp_Type = IpAddress
_RbtwsMobilityDomainIp_Object = MibScalar
rbtwsMobilityDomainIp = _RbtwsMobilityDomainIp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 2),
    _RbtwsMobilityDomainIp_Type()
)
rbtwsMobilityDomainIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsMobilityDomainIp.setStatus("current")
_RbtwsAPMACAddress_Type = MacAddress
_RbtwsAPMACAddress_Object = MibScalar
rbtwsAPMACAddress = _RbtwsAPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 3),
    _RbtwsAPMACAddress_Type()
)
rbtwsAPMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsAPMACAddress.setStatus("current")
_RbtwsClientMACAddress_Type = MacAddress
_RbtwsClientMACAddress_Object = MibScalar
rbtwsClientMACAddress = _RbtwsClientMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 4),
    _RbtwsClientMACAddress_Type()
)
rbtwsClientMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientMACAddress.setStatus("current")
_RbtwsRFDetectXmtrMacAddr_Type = MacAddress
_RbtwsRFDetectXmtrMacAddr_Object = MibScalar
rbtwsRFDetectXmtrMacAddr = _RbtwsRFDetectXmtrMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 5),
    _RbtwsRFDetectXmtrMacAddr_Type()
)
rbtwsRFDetectXmtrMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRFDetectXmtrMacAddr.setStatus("current")


class _RbtwsPortNum_Type(Integer32):
    """Custom type rbtwsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 22),
    )


_RbtwsPortNum_Type.__name__ = "Integer32"
_RbtwsPortNum_Object = MibScalar
rbtwsPortNum = _RbtwsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 6),
    _RbtwsPortNum_Type()
)
rbtwsPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsPortNum.setStatus("current")
_RbtwsAPRadioNum_Type = RbtwsRadioNum
_RbtwsAPRadioNum_Object = MibScalar
rbtwsAPRadioNum = _RbtwsAPRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 7),
    _RbtwsAPRadioNum_Type()
)
rbtwsAPRadioNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsAPRadioNum.setStatus("current")


class _RbtwsRadioRssi_Type(Integer32):
    """Custom type rbtwsRadioRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_RbtwsRadioRssi_Type.__name__ = "Integer32"
_RbtwsRadioRssi_Object = MibScalar
rbtwsRadioRssi = _RbtwsRadioRssi_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 8),
    _RbtwsRadioRssi_Type()
)
rbtwsRadioRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRadioRssi.setStatus("obsolete")


class _RbtwsRadioBSSID_Type(OctetString):
    """Custom type rbtwsRadioBSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RbtwsRadioBSSID_Type.__name__ = "OctetString"
_RbtwsRadioBSSID_Object = MibScalar
rbtwsRadioBSSID = _RbtwsRadioBSSID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 9),
    _RbtwsRadioBSSID_Type()
)
rbtwsRadioBSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRadioBSSID.setStatus("current")


class _RbtwsUserName_Type(DisplayString):
    """Custom type rbtwsUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbtwsUserName_Type.__name__ = "DisplayString"
_RbtwsUserName_Object = MibScalar
rbtwsUserName = _RbtwsUserName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 10),
    _RbtwsUserName_Type()
)
rbtwsUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsUserName.setStatus("current")
_RbtwsClientAuthServerIp_Type = IpAddress
_RbtwsClientAuthServerIp_Object = MibScalar
rbtwsClientAuthServerIp = _RbtwsClientAuthServerIp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 11),
    _RbtwsClientAuthServerIp_Type()
)
rbtwsClientAuthServerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientAuthServerIp.setStatus("current")
_RbtwsClientSessionState_Type = RbtwsClientSessionState
_RbtwsClientSessionState_Object = MibScalar
rbtwsClientSessionState = _RbtwsClientSessionState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 12),
    _RbtwsClientSessionState_Type()
)
rbtwsClientSessionState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientSessionState.setStatus("current")


class _RbtwsDAPNum_Type(Integer32):
    """Custom type rbtwsDAPNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RbtwsDAPNum_Type.__name__ = "Integer32"
_RbtwsDAPNum_Object = MibScalar
rbtwsDAPNum = _RbtwsDAPNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 13),
    _RbtwsDAPNum_Type()
)
rbtwsDAPNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsDAPNum.setStatus("current")
_RbtwsClientIp_Type = IpAddress
_RbtwsClientIp_Object = MibScalar
rbtwsClientIp = _RbtwsClientIp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 14),
    _RbtwsClientIp_Type()
)
rbtwsClientIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientIp.setStatus("current")


class _RbtwsClientSessionId_Type(DisplayString):
    """Custom type rbtwsClientSessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbtwsClientSessionId_Type.__name__ = "DisplayString"
_RbtwsClientSessionId_Object = MibScalar
rbtwsClientSessionId = _RbtwsClientSessionId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 15),
    _RbtwsClientSessionId_Type()
)
rbtwsClientSessionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientSessionId.setStatus("current")
_RbtwsClientAuthenProtocolType_Type = RbtwsClientAuthenProtocolType
_RbtwsClientAuthenProtocolType_Object = MibScalar
rbtwsClientAuthenProtocolType = _RbtwsClientAuthenProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 16),
    _RbtwsClientAuthenProtocolType_Type()
)
rbtwsClientAuthenProtocolType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientAuthenProtocolType.setStatus("current")


class _RbtwsClientVLANName_Type(DisplayString):
    """Custom type rbtwsClientVLANName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbtwsClientVLANName_Type.__name__ = "DisplayString"
_RbtwsClientVLANName_Object = MibScalar
rbtwsClientVLANName = _RbtwsClientVLANName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 17),
    _RbtwsClientVLANName_Type()
)
rbtwsClientVLANName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientVLANName.setStatus("current")
_RbtwsClientSessionStartTime_Type = TimeTicks
_RbtwsClientSessionStartTime_Object = MibScalar
rbtwsClientSessionStartTime = _RbtwsClientSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 18),
    _RbtwsClientSessionStartTime_Type()
)
rbtwsClientSessionStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientSessionStartTime.setStatus("obsolete")


class _RbtwsClientFailureCause_Type(DisplayString):
    """Custom type rbtwsClientFailureCause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbtwsClientFailureCause_Type.__name__ = "DisplayString"
_RbtwsClientFailureCause_Object = MibScalar
rbtwsClientFailureCause = _RbtwsClientFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 19),
    _RbtwsClientFailureCause_Type()
)
rbtwsClientFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientFailureCause.setStatus("current")


class _RbtwsClientRoamedFromPortNum_Type(Integer32):
    """Custom type rbtwsClientRoamedFromPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RbtwsClientRoamedFromPortNum_Type.__name__ = "Integer32"
_RbtwsClientRoamedFromPortNum_Object = MibScalar
rbtwsClientRoamedFromPortNum = _RbtwsClientRoamedFromPortNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 20),
    _RbtwsClientRoamedFromPortNum_Type()
)
rbtwsClientRoamedFromPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientRoamedFromPortNum.setStatus("current")
_RbtwsClientRoamedFromRadioNum_Type = RbtwsRadioNum
_RbtwsClientRoamedFromRadioNum_Object = MibScalar
rbtwsClientRoamedFromRadioNum = _RbtwsClientRoamedFromRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 21),
    _RbtwsClientRoamedFromRadioNum_Type()
)
rbtwsClientRoamedFromRadioNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientRoamedFromRadioNum.setStatus("current")


class _RbtwsClientRoamedFromDAPNum_Type(Integer32):
    """Custom type rbtwsClientRoamedFromDAPNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RbtwsClientRoamedFromDAPNum_Type.__name__ = "Integer32"
_RbtwsClientRoamedFromDAPNum_Object = MibScalar
rbtwsClientRoamedFromDAPNum = _RbtwsClientRoamedFromDAPNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 22),
    _RbtwsClientRoamedFromDAPNum_Type()
)
rbtwsClientRoamedFromDAPNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientRoamedFromDAPNum.setStatus("current")


class _RbtwsUserParams_Type(DisplayString):
    """Custom type rbtwsUserParams based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbtwsUserParams_Type.__name__ = "DisplayString"
_RbtwsUserParams_Object = MibScalar
rbtwsUserParams = _RbtwsUserParams_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 23),
    _RbtwsUserParams_Type()
)
rbtwsUserParams.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsUserParams.setStatus("current")


class _RbtwsClientLocationPolicyIndex_Type(Integer32):
    """Custom type rbtwsClientLocationPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_RbtwsClientLocationPolicyIndex_Type.__name__ = "Integer32"
_RbtwsClientLocationPolicyIndex_Object = MibScalar
rbtwsClientLocationPolicyIndex = _RbtwsClientLocationPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 24),
    _RbtwsClientLocationPolicyIndex_Type()
)
rbtwsClientLocationPolicyIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientLocationPolicyIndex.setStatus("current")
_RbtwsClientAssociationFailureCause_Type = RbtwsAssociationFailureType
_RbtwsClientAssociationFailureCause_Object = MibScalar
rbtwsClientAssociationFailureCause = _RbtwsClientAssociationFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 25),
    _RbtwsClientAssociationFailureCause_Type()
)
rbtwsClientAssociationFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientAssociationFailureCause.setStatus("current")
_RbtwsClientAuthenticationFailureCause_Type = RbtwsAuthenticationFailureType
_RbtwsClientAuthenticationFailureCause_Object = MibScalar
rbtwsClientAuthenticationFailureCause = _RbtwsClientAuthenticationFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 26),
    _RbtwsClientAuthenticationFailureCause_Type()
)
rbtwsClientAuthenticationFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientAuthenticationFailureCause.setStatus("current")
_RbtwsClientAuthorizationFailureCause_Type = RbtwsAuthorizationFailureType
_RbtwsClientAuthorizationFailureCause_Object = MibScalar
rbtwsClientAuthorizationFailureCause = _RbtwsClientAuthorizationFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 27),
    _RbtwsClientAuthorizationFailureCause_Type()
)
rbtwsClientAuthorizationFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientAuthorizationFailureCause.setStatus("current")


class _RbtwsClientFailureCauseDescription_Type(DisplayString):
    """Custom type rbtwsClientFailureCauseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbtwsClientFailureCauseDescription_Type.__name__ = "DisplayString"
_RbtwsClientFailureCauseDescription_Object = MibScalar
rbtwsClientFailureCauseDescription = _RbtwsClientFailureCauseDescription_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 28),
    _RbtwsClientFailureCauseDescription_Type()
)
rbtwsClientFailureCauseDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientFailureCauseDescription.setStatus("current")
_RbtwsClientRoamedFromWsIp_Type = IpAddress
_RbtwsClientRoamedFromWsIp_Object = MibScalar
rbtwsClientRoamedFromWsIp = _RbtwsClientRoamedFromWsIp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 29),
    _RbtwsClientRoamedFromWsIp_Type()
)
rbtwsClientRoamedFromWsIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientRoamedFromWsIp.setStatus("current")
_RbtwsClientRoamedFromAccessType_Type = RbtwsAccessType
_RbtwsClientRoamedFromAccessType_Object = MibScalar
rbtwsClientRoamedFromAccessType = _RbtwsClientRoamedFromAccessType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 30),
    _RbtwsClientRoamedFromAccessType_Type()
)
rbtwsClientRoamedFromAccessType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientRoamedFromAccessType.setStatus("current")
_RbtwsClientAccessType_Type = RbtwsAccessType
_RbtwsClientAccessType_Object = MibScalar
rbtwsClientAccessType = _RbtwsClientAccessType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 31),
    _RbtwsClientAccessType_Type()
)
rbtwsClientAccessType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientAccessType.setStatus("current")
_RbtwsRadioMACAddress_Type = MacAddress
_RbtwsRadioMACAddress_Object = MibScalar
rbtwsRadioMACAddress = _RbtwsRadioMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 32),
    _RbtwsRadioMACAddress_Type()
)
rbtwsRadioMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRadioMACAddress.setStatus("current")
_RbtwsRadioPowerChangeReason_Type = RbtwsRadioPowerChangeType
_RbtwsRadioPowerChangeReason_Object = MibScalar
rbtwsRadioPowerChangeReason = _RbtwsRadioPowerChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 33),
    _RbtwsRadioPowerChangeReason_Type()
)
rbtwsRadioPowerChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRadioPowerChangeReason.setStatus("current")


class _RbtwsNewChannelNum_Type(Integer32):
    """Custom type rbtwsNewChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RbtwsNewChannelNum_Type.__name__ = "Integer32"
_RbtwsNewChannelNum_Object = MibScalar
rbtwsNewChannelNum = _RbtwsNewChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 34),
    _RbtwsNewChannelNum_Type()
)
rbtwsNewChannelNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsNewChannelNum.setStatus("current")


class _RbtwsOldChannelNum_Type(Integer32):
    """Custom type rbtwsOldChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RbtwsOldChannelNum_Type.__name__ = "Integer32"
_RbtwsOldChannelNum_Object = MibScalar
rbtwsOldChannelNum = _RbtwsOldChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 35),
    _RbtwsOldChannelNum_Type()
)
rbtwsOldChannelNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsOldChannelNum.setStatus("current")
_RbtwsChannelChangeReason_Type = RbtwsChannelChangeType
_RbtwsChannelChangeReason_Object = MibScalar
rbtwsChannelChangeReason = _RbtwsChannelChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 36),
    _RbtwsChannelChangeReason_Type()
)
rbtwsChannelChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsChannelChangeReason.setStatus("current")


class _RbtwsRFDetectListenerListInfo_Type(OctetString):
    """Custom type rbtwsRFDetectListenerListInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 571),
    )


_RbtwsRFDetectListenerListInfo_Type.__name__ = "OctetString"
_RbtwsRFDetectListenerListInfo_Object = MibScalar
rbtwsRFDetectListenerListInfo = _RbtwsRFDetectListenerListInfo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 37),
    _RbtwsRFDetectListenerListInfo_Type()
)
rbtwsRFDetectListenerListInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRFDetectListenerListInfo.setStatus("current")


class _RbtwsRadioSSID_Type(DisplayString):
    """Custom type rbtwsRadioSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbtwsRadioSSID_Type.__name__ = "DisplayString"
_RbtwsRadioSSID_Object = MibScalar
rbtwsRadioSSID = _RbtwsRadioSSID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 38),
    _RbtwsRadioSSID_Type()
)
rbtwsRadioSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRadioSSID.setStatus("current")
_RbtwsNewPowerLevel_Type = RbtwsPowerLevel
_RbtwsNewPowerLevel_Object = MibScalar
rbtwsNewPowerLevel = _RbtwsNewPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 39),
    _RbtwsNewPowerLevel_Type()
)
rbtwsNewPowerLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsNewPowerLevel.setStatus("current")
_RbtwsOldPowerLevel_Type = RbtwsPowerLevel
_RbtwsOldPowerLevel_Object = MibScalar
rbtwsOldPowerLevel = _RbtwsOldPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 40),
    _RbtwsOldPowerLevel_Type()
)
rbtwsOldPowerLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsOldPowerLevel.setStatus("current")


class _RbtwsRadioPowerChangeDescription_Type(DisplayString):
    """Custom type rbtwsRadioPowerChangeDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbtwsRadioPowerChangeDescription_Type.__name__ = "DisplayString"
_RbtwsRadioPowerChangeDescription_Object = MibScalar
rbtwsRadioPowerChangeDescription = _RbtwsRadioPowerChangeDescription_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 41),
    _RbtwsRadioPowerChangeDescription_Type()
)
rbtwsRadioPowerChangeDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRadioPowerChangeDescription.setStatus("current")


class _RbtwsCounterMeasurePerformerListInfo_Type(DisplayString):
    """Custom type rbtwsCounterMeasurePerformerListInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbtwsCounterMeasurePerformerListInfo_Type.__name__ = "DisplayString"
_RbtwsCounterMeasurePerformerListInfo_Object = MibScalar
rbtwsCounterMeasurePerformerListInfo = _RbtwsCounterMeasurePerformerListInfo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 42),
    _RbtwsCounterMeasurePerformerListInfo_Type()
)
rbtwsCounterMeasurePerformerListInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsCounterMeasurePerformerListInfo.setStatus("obsolete")
_RbtwsClientDot1xState_Type = RbtwsClientDot1xState
_RbtwsClientDot1xState_Object = MibScalar
rbtwsClientDot1xState = _RbtwsClientDot1xState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 43),
    _RbtwsClientDot1xState_Type()
)
rbtwsClientDot1xState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientDot1xState.setStatus("current")
_RbtwsClientDot1xFailureCause_Type = RbtwsDot1xFailureType
_RbtwsClientDot1xFailureCause_Object = MibScalar
rbtwsClientDot1xFailureCause = _RbtwsClientDot1xFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 44),
    _RbtwsClientDot1xFailureCause_Type()
)
rbtwsClientDot1xFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientDot1xFailureCause.setStatus("current")
_RbtwsAPAccessType_Type = RbtwsAccessType
_RbtwsAPAccessType_Object = MibScalar
rbtwsAPAccessType = _RbtwsAPAccessType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 45),
    _RbtwsAPAccessType_Type()
)
rbtwsAPAccessType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsAPAccessType.setStatus("obsolete")
_RbtwsUserAccessType_Type = RbtwsUserAccessType
_RbtwsUserAccessType_Object = MibScalar
rbtwsUserAccessType = _RbtwsUserAccessType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 46),
    _RbtwsUserAccessType_Type()
)
rbtwsUserAccessType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsUserAccessType.setStatus("current")
_RbtwsClientSessionElapsedTime_Type = TimeTicks
_RbtwsClientSessionElapsedTime_Object = MibScalar
rbtwsClientSessionElapsedTime = _RbtwsClientSessionElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 47),
    _RbtwsClientSessionElapsedTime_Type()
)
rbtwsClientSessionElapsedTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientSessionElapsedTime.setStatus("obsolete")


class _RbtwsLocalId_Type(Integer32):
    """Custom type rbtwsLocalId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_RbtwsLocalId_Type.__name__ = "Integer32"
_RbtwsLocalId_Object = MibScalar
rbtwsLocalId = _RbtwsLocalId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 48),
    _RbtwsLocalId_Type()
)
rbtwsLocalId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsLocalId.setStatus("current")
_RbtwsRFDetectDoSType_Type = RbtwsRFDetectDoSType
_RbtwsRFDetectDoSType_Object = MibScalar
rbtwsRFDetectDoSType = _RbtwsRFDetectDoSType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 49),
    _RbtwsRFDetectDoSType_Type()
)
rbtwsRFDetectDoSType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRFDetectDoSType.setStatus("current")
_RbtwsSourceWsIp_Type = IpAddress
_RbtwsSourceWsIp_Object = MibScalar
rbtwsSourceWsIp = _RbtwsSourceWsIp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 50),
    _RbtwsSourceWsIp_Type()
)
rbtwsSourceWsIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsSourceWsIp.setStatus("current")


class _RbtwsClientVLANid_Type(Integer32):
    """Custom type rbtwsClientVLANid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RbtwsClientVLANid_Type.__name__ = "Integer32"
_RbtwsClientVLANid_Object = MibScalar
rbtwsClientVLANid = _RbtwsClientVLANid_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 51),
    _RbtwsClientVLANid_Type()
)
rbtwsClientVLANid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientVLANid.setStatus("current")


class _RbtwsClientVLANtag_Type(Integer32):
    """Custom type rbtwsClientVLANtag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RbtwsClientVLANtag_Type.__name__ = "Integer32"
_RbtwsClientVLANtag_Object = MibScalar
rbtwsClientVLANtag = _RbtwsClientVLANtag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 52),
    _RbtwsClientVLANtag_Type()
)
rbtwsClientVLANtag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientVLANtag.setStatus("current")
_RbtwsDeviceModel_Type = DisplayString
_RbtwsDeviceModel_Object = MibScalar
rbtwsDeviceModel = _RbtwsDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 53),
    _RbtwsDeviceModel_Type()
)
rbtwsDeviceModel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsDeviceModel.setStatus("current")
_RbtwsDeviceSerNum_Type = RbtwsApSerialNum
_RbtwsDeviceSerNum_Object = MibScalar
rbtwsDeviceSerNum = _RbtwsDeviceSerNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 54),
    _RbtwsDeviceSerNum_Type()
)
rbtwsDeviceSerNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsDeviceSerNum.setStatus("current")
_RbtwsRsaPubKeyFingerPrint_Type = RbtwsApFingerprint
_RbtwsRsaPubKeyFingerPrint_Object = MibScalar
rbtwsRsaPubKeyFingerPrint = _RbtwsRsaPubKeyFingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 55),
    _RbtwsRsaPubKeyFingerPrint_Type()
)
rbtwsRsaPubKeyFingerPrint.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRsaPubKeyFingerPrint.setStatus("current")


class _RbtwsDAPconnectWarningType_Type(Integer32):
    """Custom type rbtwsDAPconnectWarningType based on Integer32"""
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


_RbtwsDAPconnectWarningType_Type.__name__ = "Integer32"
_RbtwsDAPconnectWarningType_Object = MibScalar
rbtwsDAPconnectWarningType = _RbtwsDAPconnectWarningType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 56),
    _RbtwsDAPconnectWarningType_Type()
)
rbtwsDAPconnectWarningType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsDAPconnectWarningType.setStatus("current")
_RbtwsClientMACAddress2_Type = MacAddress
_RbtwsClientMACAddress2_Object = MibScalar
rbtwsClientMACAddress2 = _RbtwsClientMACAddress2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 57),
    _RbtwsClientMACAddress2_Type()
)
rbtwsClientMACAddress2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientMACAddress2.setStatus("current")
_RbtwsApAttachType_Type = RbtwsApAttachType
_RbtwsApAttachType_Object = MibScalar
rbtwsApAttachType = _RbtwsApAttachType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 58),
    _RbtwsApAttachType_Type()
)
rbtwsApAttachType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsApAttachType.setStatus("current")
_RbtwsApPortOrDapNum_Type = RbtwsApPortOrDapNum
_RbtwsApPortOrDapNum_Object = MibScalar
rbtwsApPortOrDapNum = _RbtwsApPortOrDapNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 59),
    _RbtwsApPortOrDapNum_Type()
)
rbtwsApPortOrDapNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsApPortOrDapNum.setStatus("obsolete")
_RbtwsApName_Type = DisplayString
_RbtwsApName_Object = MibScalar
rbtwsApName = _RbtwsApName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 60),
    _RbtwsApName_Type()
)
rbtwsApName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsApName.setStatus("current")
_RbtwsApTransition_Type = RbtwsApTransition
_RbtwsApTransition_Object = MibScalar
rbtwsApTransition = _RbtwsApTransition_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 61),
    _RbtwsApTransition_Type()
)
rbtwsApTransition.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsApTransition.setStatus("current")
_RbtwsApFailDetail_Type = RbtwsApFailDetail
_RbtwsApFailDetail_Object = MibScalar
rbtwsApFailDetail = _RbtwsApFailDetail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 62),
    _RbtwsApFailDetail_Type()
)
rbtwsApFailDetail.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsApFailDetail.setStatus("current")
_RbtwsRadioType_Type = RbtwsRadioType
_RbtwsRadioType_Object = MibScalar
rbtwsRadioType = _RbtwsRadioType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 63),
    _RbtwsRadioType_Type()
)
rbtwsRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRadioType.setStatus("current")
_RbtwsRadioConfigState_Type = RbtwsRadioConfigState
_RbtwsRadioConfigState_Object = MibScalar
rbtwsRadioConfigState = _RbtwsRadioConfigState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 64),
    _RbtwsRadioConfigState_Type()
)
rbtwsRadioConfigState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRadioConfigState.setStatus("current")
_RbtwsApConnectSecurityType_Type = RbtwsApConnectSecurityType
_RbtwsApConnectSecurityType_Object = MibScalar
rbtwsApConnectSecurityType = _RbtwsApConnectSecurityType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 65),
    _RbtwsApConnectSecurityType_Type()
)
rbtwsApConnectSecurityType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsApConnectSecurityType.setStatus("current")
_RbtwsApServiceAvailability_Type = RbtwsApServiceAvailability
_RbtwsApServiceAvailability_Object = MibScalar
rbtwsApServiceAvailability = _RbtwsApServiceAvailability_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 66),
    _RbtwsApServiceAvailability_Type()
)
rbtwsApServiceAvailability.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsApServiceAvailability.setStatus("current")
_RbtwsApWasOperational_Type = RbtwsApWasOperational
_RbtwsApWasOperational_Object = MibScalar
rbtwsApWasOperational = _RbtwsApWasOperational_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 67),
    _RbtwsApWasOperational_Type()
)
rbtwsApWasOperational.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsApWasOperational.setStatus("current")
_RbtwsClientTimeSinceLastRoam_Type = Unsigned32
_RbtwsClientTimeSinceLastRoam_Object = MibScalar
rbtwsClientTimeSinceLastRoam = _RbtwsClientTimeSinceLastRoam_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 68),
    _RbtwsClientTimeSinceLastRoam_Type()
)
rbtwsClientTimeSinceLastRoam.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientTimeSinceLastRoam.setStatus("current")
_RbtwsClientIpAddrChangeReason_Type = RbtwsClientIpAddrChangeReason
_RbtwsClientIpAddrChangeReason_Object = MibScalar
rbtwsClientIpAddrChangeReason = _RbtwsClientIpAddrChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 69),
    _RbtwsClientIpAddrChangeReason_Type()
)
rbtwsClientIpAddrChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientIpAddrChangeReason.setStatus("current")
_RbtwsRFDetectRogueAPMacAddr_Type = MacAddress
_RbtwsRFDetectRogueAPMacAddr_Object = MibScalar
rbtwsRFDetectRogueAPMacAddr = _RbtwsRFDetectRogueAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 70),
    _RbtwsRFDetectRogueAPMacAddr_Type()
)
rbtwsRFDetectRogueAPMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRFDetectRogueAPMacAddr.setStatus("current")
_RbtwsBlacklistingRemainingTime_Type = Unsigned32
_RbtwsBlacklistingRemainingTime_Object = MibScalar
rbtwsBlacklistingRemainingTime = _RbtwsBlacklistingRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 71),
    _RbtwsBlacklistingRemainingTime_Type()
)
rbtwsBlacklistingRemainingTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsBlacklistingRemainingTime.setStatus("current")
_RbtwsBlacklistingCause_Type = RbtwsBlacklistingCause
_RbtwsBlacklistingCause_Object = MibScalar
rbtwsBlacklistingCause = _RbtwsBlacklistingCause_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 72),
    _RbtwsBlacklistingCause_Type()
)
rbtwsBlacklistingCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsBlacklistingCause.setStatus("current")
_RbtwsNumLicensedActiveAPs_Type = Unsigned32
_RbtwsNumLicensedActiveAPs_Object = MibScalar
rbtwsNumLicensedActiveAPs = _RbtwsNumLicensedActiveAPs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 73),
    _RbtwsNumLicensedActiveAPs_Type()
)
rbtwsNumLicensedActiveAPs.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsNumLicensedActiveAPs.setStatus("current")
_RbtwsClientDynAuthorClientIp_Type = IpAddress
_RbtwsClientDynAuthorClientIp_Object = MibScalar
rbtwsClientDynAuthorClientIp = _RbtwsClientDynAuthorClientIp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 74),
    _RbtwsClientDynAuthorClientIp_Type()
)
rbtwsClientDynAuthorClientIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientDynAuthorClientIp.setStatus("current")
_RbtwsChangedUserParamOldValues_Type = RbtwsUserAttributeList
_RbtwsChangedUserParamOldValues_Object = MibScalar
rbtwsChangedUserParamOldValues = _RbtwsChangedUserParamOldValues_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 75),
    _RbtwsChangedUserParamOldValues_Type()
)
rbtwsChangedUserParamOldValues.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsChangedUserParamOldValues.setStatus("current")
_RbtwsChangedUserParamNewValues_Type = RbtwsUserAttributeList
_RbtwsChangedUserParamNewValues_Object = MibScalar
rbtwsChangedUserParamNewValues = _RbtwsChangedUserParamNewValues_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 76),
    _RbtwsChangedUserParamNewValues_Type()
)
rbtwsChangedUserParamNewValues.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsChangedUserParamNewValues.setStatus("current")
_RbtwsClientDisconnectSource_Type = RbtwsSessionDisconnectType
_RbtwsClientDisconnectSource_Object = MibScalar
rbtwsClientDisconnectSource = _RbtwsClientDisconnectSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 77),
    _RbtwsClientDisconnectSource_Type()
)
rbtwsClientDisconnectSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientDisconnectSource.setStatus("current")


class _RbtwsClientDisconnectDescription_Type(DisplayString):
    """Custom type rbtwsClientDisconnectDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbtwsClientDisconnectDescription_Type.__name__ = "DisplayString"
_RbtwsClientDisconnectDescription_Object = MibScalar
rbtwsClientDisconnectDescription = _RbtwsClientDisconnectDescription_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 78),
    _RbtwsClientDisconnectDescription_Type()
)
rbtwsClientDisconnectDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientDisconnectDescription.setStatus("current")
_RbtwsMobilityDomainSecondarySeedIp_Type = IpAddress
_RbtwsMobilityDomainSecondarySeedIp_Object = MibScalar
rbtwsMobilityDomainSecondarySeedIp = _RbtwsMobilityDomainSecondarySeedIp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 79),
    _RbtwsMobilityDomainSecondarySeedIp_Type()
)
rbtwsMobilityDomainSecondarySeedIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsMobilityDomainSecondarySeedIp.setStatus("current")
_RbtwsMobilityDomainPrimarySeedIp_Type = IpAddress
_RbtwsMobilityDomainPrimarySeedIp_Object = MibScalar
rbtwsMobilityDomainPrimarySeedIp = _RbtwsMobilityDomainPrimarySeedIp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 80),
    _RbtwsMobilityDomainPrimarySeedIp_Type()
)
rbtwsMobilityDomainPrimarySeedIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsMobilityDomainPrimarySeedIp.setStatus("current")
_RbtwsRFDetectClassificationReason_Type = RbtwsRFDetectClassificationReason
_RbtwsRFDetectClassificationReason_Object = MibScalar
rbtwsRFDetectClassificationReason = _RbtwsRFDetectClassificationReason_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 81),
    _RbtwsRFDetectClassificationReason_Type()
)
rbtwsRFDetectClassificationReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRFDetectClassificationReason.setStatus("current")


class _RbtwsConfigSaveFileName_Type(DisplayString):
    """Custom type rbtwsConfigSaveFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbtwsConfigSaveFileName_Type.__name__ = "DisplayString"
_RbtwsConfigSaveFileName_Object = MibScalar
rbtwsConfigSaveFileName = _RbtwsConfigSaveFileName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 82),
    _RbtwsConfigSaveFileName_Type()
)
rbtwsConfigSaveFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsConfigSaveFileName.setStatus("current")
_RbtwsConfigSaveInitiatorType_Type = RbtwsConfigSaveInitiatorType
_RbtwsConfigSaveInitiatorType_Object = MibScalar
rbtwsConfigSaveInitiatorType = _RbtwsConfigSaveInitiatorType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 83),
    _RbtwsConfigSaveInitiatorType_Type()
)
rbtwsConfigSaveInitiatorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsConfigSaveInitiatorType.setStatus("current")
_RbtwsConfigSaveInitiatorIp_Type = IpAddress
_RbtwsConfigSaveInitiatorIp_Object = MibScalar
rbtwsConfigSaveInitiatorIp = _RbtwsConfigSaveInitiatorIp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 84),
    _RbtwsConfigSaveInitiatorIp_Type()
)
rbtwsConfigSaveInitiatorIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsConfigSaveInitiatorIp.setStatus("current")


class _RbtwsConfigSaveInitiatorDetails_Type(DisplayString):
    """Custom type rbtwsConfigSaveInitiatorDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbtwsConfigSaveInitiatorDetails_Type.__name__ = "DisplayString"
_RbtwsConfigSaveInitiatorDetails_Object = MibScalar
rbtwsConfigSaveInitiatorDetails = _RbtwsConfigSaveInitiatorDetails_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 85),
    _RbtwsConfigSaveInitiatorDetails_Type()
)
rbtwsConfigSaveInitiatorDetails.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsConfigSaveInitiatorDetails.setStatus("current")
_RbtwsConfigSaveGeneration_Type = Counter32
_RbtwsConfigSaveGeneration_Object = MibScalar
rbtwsConfigSaveGeneration = _RbtwsConfigSaveGeneration_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 86),
    _RbtwsConfigSaveGeneration_Type()
)
rbtwsConfigSaveGeneration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsConfigSaveGeneration.setStatus("current")
_RbtwsApNum_Type = RbtwsApNum
_RbtwsApNum_Object = MibScalar
rbtwsApNum = _RbtwsApNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 87),
    _RbtwsApNum_Type()
)
rbtwsApNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsApNum.setStatus("current")
_RbtwsRadioMode_Type = RbtwsRadioMode
_RbtwsRadioMode_Object = MibScalar
rbtwsRadioMode = _RbtwsRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 88),
    _RbtwsRadioMode_Type()
)
rbtwsRadioMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRadioMode.setStatus("current")
_RbtwsMichaelMICFailureCause_Type = RbtwsMichaelMICFailureCause
_RbtwsMichaelMICFailureCause_Object = MibScalar
rbtwsMichaelMICFailureCause = _RbtwsMichaelMICFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 89),
    _RbtwsMichaelMICFailureCause_Type()
)
rbtwsMichaelMICFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsMichaelMICFailureCause.setStatus("current")
_RbtwsClientAccessMode_Type = RbtwsClientAccessMode
_RbtwsClientAccessMode_Object = MibScalar
rbtwsClientAccessMode = _RbtwsClientAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 90),
    _RbtwsClientAccessMode_Type()
)
rbtwsClientAccessMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientAccessMode.setStatus("current")
_RbtwsClientAuthorizationReason_Type = RbtwsClientAuthorizationReason
_RbtwsClientAuthorizationReason_Object = MibScalar
rbtwsClientAuthorizationReason = _RbtwsClientAuthorizationReason_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 91),
    _RbtwsClientAuthorizationReason_Type()
)
rbtwsClientAuthorizationReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientAuthorizationReason.setStatus("current")


class _RbtwsPhysPortNum_Type(Unsigned32):
    """Custom type rbtwsPhysPortNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_RbtwsPhysPortNum_Type.__name__ = "Unsigned32"
_RbtwsPhysPortNum_Object = MibScalar
rbtwsPhysPortNum = _RbtwsPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 92),
    _RbtwsPhysPortNum_Type()
)
rbtwsPhysPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsPhysPortNum.setStatus("current")
_RbtwsApMgrOldIp_Type = IpAddress
_RbtwsApMgrOldIp_Object = MibScalar
rbtwsApMgrOldIp = _RbtwsApMgrOldIp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 93),
    _RbtwsApMgrOldIp_Type()
)
rbtwsApMgrOldIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsApMgrOldIp.setStatus("current")
_RbtwsApMgrNewIp_Type = IpAddress
_RbtwsApMgrNewIp_Object = MibScalar
rbtwsApMgrNewIp = _RbtwsApMgrNewIp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 94),
    _RbtwsApMgrNewIp_Type()
)
rbtwsApMgrNewIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsApMgrNewIp.setStatus("current")
_RbtwsApMgrChangeReason_Type = RbtwsApMgrChangeReason
_RbtwsApMgrChangeReason_Object = MibScalar
rbtwsApMgrChangeReason = _RbtwsApMgrChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 95),
    _RbtwsApMgrChangeReason_Type()
)
rbtwsApMgrChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsApMgrChangeReason.setStatus("current")
_RbtwsClientClearedReason_Type = RbtwsClientClearedReason
_RbtwsClientClearedReason_Object = MibScalar
rbtwsClientClearedReason = _RbtwsClientClearedReason_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 96),
    _RbtwsClientClearedReason_Type()
)
rbtwsClientClearedReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientClearedReason.setStatus("current")
_RbtwsMobilityDomainResiliencyStatus_Type = RbtwsMobilityDomainResiliencyStatus
_RbtwsMobilityDomainResiliencyStatus_Object = MibScalar
rbtwsMobilityDomainResiliencyStatus = _RbtwsMobilityDomainResiliencyStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 97),
    _RbtwsMobilityDomainResiliencyStatus_Type()
)
rbtwsMobilityDomainResiliencyStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsMobilityDomainResiliencyStatus.setStatus("current")
_RbtwsClientSessionElapsedSeconds_Type = Unsigned32
_RbtwsClientSessionElapsedSeconds_Object = MibScalar
rbtwsClientSessionElapsedSeconds = _RbtwsClientSessionElapsedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 98),
    _RbtwsClientSessionElapsedSeconds_Type()
)
rbtwsClientSessionElapsedSeconds.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientSessionElapsedSeconds.setStatus("current")
_RbtwsRadioChannelWidth_Type = RbtwsRadioChannelWidth
_RbtwsRadioChannelWidth_Object = MibScalar
rbtwsRadioChannelWidth = _RbtwsRadioChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 99),
    _RbtwsRadioChannelWidth_Type()
)
rbtwsRadioChannelWidth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRadioChannelWidth.setStatus("current")
_RbtwsRadioMimoState_Type = RbtwsRadioMimoState
_RbtwsRadioMimoState_Object = MibScalar
rbtwsRadioMimoState = _RbtwsRadioMimoState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 100),
    _RbtwsRadioMimoState_Type()
)
rbtwsRadioMimoState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRadioMimoState.setStatus("current")
_RbtwsClientRadioType_Type = RbtwsRadioType
_RbtwsClientRadioType_Object = MibScalar
rbtwsClientRadioType = _RbtwsClientRadioType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 101),
    _RbtwsClientRadioType_Type()
)
rbtwsClientRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClientRadioType.setStatus("current")
_RbtwsRFDetectXmtrRadioType_Type = RbtwsRadioType
_RbtwsRFDetectXmtrRadioType_Object = MibScalar
rbtwsRFDetectXmtrRadioType = _RbtwsRFDetectXmtrRadioType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 102),
    _RbtwsRFDetectXmtrRadioType_Type()
)
rbtwsRFDetectXmtrRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRFDetectXmtrRadioType.setStatus("current")
_RbtwsRFDetectXmtrCryptoType_Type = RbtwsCryptoType
_RbtwsRFDetectXmtrCryptoType_Object = MibScalar
rbtwsRFDetectXmtrCryptoType = _RbtwsRFDetectXmtrCryptoType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 103),
    _RbtwsRFDetectXmtrCryptoType_Type()
)
rbtwsRFDetectXmtrCryptoType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsRFDetectXmtrCryptoType.setStatus("current")
_RbtwsClusterFailureReason_Type = RbtwsClusterFailureReason
_RbtwsClusterFailureReason_Object = MibScalar
rbtwsClusterFailureReason = _RbtwsClusterFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 104),
    _RbtwsClusterFailureReason_Type()
)
rbtwsClusterFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClusterFailureReason.setStatus("current")


class _RbtwsClusterFailureDescription_Type(DisplayString):
    """Custom type rbtwsClusterFailureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbtwsClusterFailureDescription_Type.__name__ = "DisplayString"
_RbtwsClusterFailureDescription_Object = MibScalar
rbtwsClusterFailureDescription = _RbtwsClusterFailureDescription_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2, 105),
    _RbtwsClusterFailureDescription_Type()
)
rbtwsClusterFailureDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbtwsClusterFailureDescription.setStatus("current")
_RbtwsTrapsV2_ObjectIdentity = ObjectIdentity
rbtwsTrapsV2 = _RbtwsTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0)
)

# Managed Objects groups


# Notification objects

rbtwsDeviceFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 1)
)
rbtwsDeviceFailTrap.setObjects(
    ("RBTWS-TRAP-MIB", "rbtwsDeviceId")
)
if mibBuilder.loadTexts:
    rbtwsDeviceFailTrap.setStatus(
        "current"
    )

rbtwsDeviceOkayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 2)
)
rbtwsDeviceOkayTrap.setObjects(
    ("RBTWS-TRAP-MIB", "rbtwsDeviceId")
)
if mibBuilder.loadTexts:
    rbtwsDeviceOkayTrap.setStatus(
        "current"
    )

rbtwsPoEFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 3)
)
rbtwsPoEFailTrap.setObjects(
    ("RBTWS-TRAP-MIB", "rbtwsPortNum")
)
if mibBuilder.loadTexts:
    rbtwsPoEFailTrap.setStatus(
        "current"
    )

rbtwsApTimeoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 4)
)
rbtwsApTimeoutTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsAPAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"))
)
if mibBuilder.loadTexts:
    rbtwsApTimeoutTrap.setStatus(
        "obsolete"
    )

rbtwsAPBootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 5)
)
rbtwsAPBootTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsAPAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"))
)
if mibBuilder.loadTexts:
    rbtwsAPBootTrap.setStatus(
        "obsolete"
    )

rbtwsMobilityDomainJoinTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 6)
)
rbtwsMobilityDomainJoinTrap.setObjects(
    ("RBTWS-TRAP-MIB", "rbtwsMobilityDomainIp")
)
if mibBuilder.loadTexts:
    rbtwsMobilityDomainJoinTrap.setStatus(
        "current"
    )

rbtwsMobilityDomainTimeoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 7)
)
rbtwsMobilityDomainTimeoutTrap.setObjects(
    ("RBTWS-TRAP-MIB", "rbtwsMobilityDomainIp")
)
if mibBuilder.loadTexts:
    rbtwsMobilityDomainTimeoutTrap.setStatus(
        "current"
    )

rbtwsMpMichaelMICFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 8)
)
rbtwsMpMichaelMICFailure.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"))
)
if mibBuilder.loadTexts:
    rbtwsMpMichaelMICFailure.setStatus(
        "obsolete"
    )

rbtwsRFDetectRogueAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 9)
)
rbtwsRFDetectRogueAPTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectRogueAPTrap.setStatus(
        "obsolete"
    )

rbtwsRFDetectAdhocUserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 10)
)
rbtwsRFDetectAdhocUserTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectAdhocUserTrap.setStatus(
        "current"
    )

rbtwsRFDetectRogueDisappearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 11)
)
rbtwsRFDetectRogueDisappearTrap.setObjects(
    ("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr")
)
if mibBuilder.loadTexts:
    rbtwsRFDetectRogueDisappearTrap.setStatus(
        "obsolete"
    )

rbtwsClientAuthenticationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 12)
)
rbtwsClientAuthenticationFailureTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsUserName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthServerIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthenProtocolType"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthenticationFailureCause"),
        ("RBTWS-TRAP-MIB", "rbtwsClientFailureCauseDescription"))
)
if mibBuilder.loadTexts:
    rbtwsClientAuthenticationFailureTrap.setStatus(
        "current"
    )

rbtwsClientAuthorizationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 13)
)
rbtwsClientAuthorizationFailureTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsUserName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthServerIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthenProtocolType"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"),
        ("RBTWS-TRAP-MIB", "rbtwsClientLocationPolicyIndex"),
        ("RBTWS-TRAP-MIB", "rbtwsUserParams"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthorizationFailureCause"),
        ("RBTWS-TRAP-MIB", "rbtwsClientFailureCauseDescription"))
)
if mibBuilder.loadTexts:
    rbtwsClientAuthorizationFailureTrap.setStatus(
        "current"
    )

rbtwsClientAssociationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 14)
)
rbtwsClientAssociationFailureTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAssociationFailureCause"),
        ("RBTWS-TRAP-MIB", "rbtwsClientFailureCauseDescription"))
)
if mibBuilder.loadTexts:
    rbtwsClientAssociationFailureTrap.setStatus(
        "current"
    )

rbtwsClientAuthorizationSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 15)
)
rbtwsClientAuthorizationSuccessTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsUserName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientVLANName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionState"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionStartTime"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthServerIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthenProtocolType"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioRssi"))
)
if mibBuilder.loadTexts:
    rbtwsClientAuthorizationSuccessTrap.setStatus(
        "obsolete"
    )

rbtwsClientDeAssociationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 16)
)
rbtwsClientDeAssociationTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsUserName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientVLANName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthServerIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthenProtocolType"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"))
)
if mibBuilder.loadTexts:
    rbtwsClientDeAssociationTrap.setStatus(
        "current"
    )

rbtwsClientRoamingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 17)
)
rbtwsClientRoamingTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsUserName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"),
        ("RBTWS-TRAP-MIB", "rbtwsClientRoamedFromAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsClientRoamedFromPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsClientRoamedFromRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsClientRoamedFromDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsClientRoamedFromWsIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientTimeSinceLastRoam"))
)
if mibBuilder.loadTexts:
    rbtwsClientRoamingTrap.setStatus(
        "current"
    )

rbtwsAutoTuneRadioPowerChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 18)
)
rbtwsAutoTuneRadioPowerChangeTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRadioMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsNewPowerLevel"),
        ("RBTWS-TRAP-MIB", "rbtwsOldPowerLevel"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioPowerChangeReason"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioPowerChangeDescription"))
)
if mibBuilder.loadTexts:
    rbtwsAutoTuneRadioPowerChangeTrap.setStatus(
        "current"
    )

rbtwsAutoTuneRadioChannelChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 19)
)
rbtwsAutoTuneRadioChannelChangeTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRadioMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsNewChannelNum"),
        ("RBTWS-TRAP-MIB", "rbtwsOldChannelNum"),
        ("RBTWS-TRAP-MIB", "rbtwsChannelChangeReason"))
)
if mibBuilder.loadTexts:
    rbtwsAutoTuneRadioChannelChangeTrap.setStatus(
        "current"
    )

rbtwsCounterMeasureStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 20)
)
rbtwsCounterMeasureStartTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioMACAddress"))
)
if mibBuilder.loadTexts:
    rbtwsCounterMeasureStartTrap.setStatus(
        "current"
    )

rbtwsCounterMeasureStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 21)
)
rbtwsCounterMeasureStopTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioMACAddress"))
)
if mibBuilder.loadTexts:
    rbtwsCounterMeasureStopTrap.setStatus(
        "current"
    )

rbtwsClientDot1xFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 22)
)
rbtwsClientDot1xFailureTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsUserName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthenProtocolType"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"),
        ("RBTWS-TRAP-MIB", "rbtwsClientDot1xState"),
        ("RBTWS-TRAP-MIB", "rbtwsClientDot1xFailureCause"),
        ("RBTWS-TRAP-MIB", "rbtwsClientFailureCauseDescription"))
)
if mibBuilder.loadTexts:
    rbtwsClientDot1xFailureTrap.setStatus(
        "current"
    )

rbtwsClientClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 23)
)
rbtwsClientClearedTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsUserName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionElapsedTime"),
        ("RBTWS-TRAP-MIB", "rbtwsLocalId"))
)
if mibBuilder.loadTexts:
    rbtwsClientClearedTrap.setStatus(
        "obsolete"
    )

rbtwsClientAuthorizationSuccessTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 24)
)
rbtwsClientAuthorizationSuccessTrap2.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsUserName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientVLANName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionState"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionStartTime"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthServerIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthenProtocolType"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"),
        ("RBTWS-TRAP-MIB", "rbtwsUserAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsLocalId"))
)
if mibBuilder.loadTexts:
    rbtwsClientAuthorizationSuccessTrap2.setStatus(
        "obsolete"
    )

rbtwsRFDetectSpoofedMacAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 25)
)
rbtwsRFDetectSpoofedMacAPTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectSpoofedMacAPTrap.setStatus(
        "obsolete"
    )

rbtwsRFDetectSpoofedSsidAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 26)
)
rbtwsRFDetectSpoofedSsidAPTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectSpoofedSsidAPTrap.setStatus(
        "obsolete"
    )

rbtwsRFDetectDoSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 27)
)
rbtwsRFDetectDoSTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRFDetectDoSType"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectDoSTrap.setStatus(
        "current"
    )

rbtwsRFDetectClientViaRogueWiredAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 28)
)
rbtwsRFDetectClientViaRogueWiredAPTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsSourceWsIp"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsClientVLANid"),
        ("RBTWS-TRAP-MIB", "rbtwsClientVLANtag"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectClientViaRogueWiredAPTrap.setStatus(
        "obsolete"
    )

rbtwsRFDetectInterferingRogueAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 29)
)
rbtwsRFDetectInterferingRogueAPTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectInterferingRogueAPTrap.setStatus(
        "obsolete"
    )

rbtwsRFDetectInterferingRogueDisappearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 30)
)
rbtwsRFDetectInterferingRogueDisappearTrap.setObjects(
    ("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr")
)
if mibBuilder.loadTexts:
    rbtwsRFDetectInterferingRogueDisappearTrap.setStatus(
        "obsolete"
    )

rbtwsRFDetectUnAuthorizedSsidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 31)
)
rbtwsRFDetectUnAuthorizedSsidTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectUnAuthorizedSsidTrap.setStatus(
        "obsolete"
    )

rbtwsRFDetectUnAuthorizedOuiTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 32)
)
rbtwsRFDetectUnAuthorizedOuiTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectUnAuthorizedOuiTrap.setStatus(
        "obsolete"
    )

rbtwsRFDetectUnAuthorizedAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 33)
)
rbtwsRFDetectUnAuthorizedAPTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectUnAuthorizedAPTrap.setStatus(
        "obsolete"
    )

rbtwsDAPConnectWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 34)
)
rbtwsDAPConnectWarningTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsDeviceModel"),
        ("RBTWS-TRAP-MIB", "rbtwsDeviceSerNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRsaPubKeyFingerPrint"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPconnectWarningType"))
)
if mibBuilder.loadTexts:
    rbtwsDAPConnectWarningTrap.setStatus(
        "obsolete"
    )

rbtwsRFDetectDoSPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 35)
)
rbtwsRFDetectDoSPortTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRFDetectDoSType"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectDoSPortTrap.setStatus(
        "current"
    )

rbtwsMpMichaelMICFailure2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 36)
)
rbtwsMpMichaelMICFailure2.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress2"))
)
if mibBuilder.loadTexts:
    rbtwsMpMichaelMICFailure2.setStatus(
        "obsolete"
    )

rbtwsApNonOperStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 37)
)
rbtwsApNonOperStatusTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsDeviceSerNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsApAttachType"),
        ("RBTWS-TRAP-MIB", "rbtwsApPortOrDapNum"),
        ("RBTWS-TRAP-MIB", "rbtwsApName"),
        ("RBTWS-TRAP-MIB", "rbtwsApTransition"),
        ("RBTWS-TRAP-MIB", "rbtwsApFailDetail"),
        ("RBTWS-TRAP-MIB", "rbtwsApWasOperational"))
)
if mibBuilder.loadTexts:
    rbtwsApNonOperStatusTrap.setStatus(
        "obsolete"
    )

rbtwsApOperRadioStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 38)
)
rbtwsApOperRadioStatusTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsDeviceSerNum"),
        ("RBTWS-TRAP-MIB", "rbtwsApAttachType"),
        ("RBTWS-TRAP-MIB", "rbtwsApPortOrDapNum"),
        ("RBTWS-TRAP-MIB", "rbtwsApName"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioType"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioConfigState"),
        ("RBTWS-TRAP-MIB", "rbtwsApConnectSecurityType"),
        ("RBTWS-TRAP-MIB", "rbtwsApServiceAvailability"))
)
if mibBuilder.loadTexts:
    rbtwsApOperRadioStatusTrap.setStatus(
        "obsolete"
    )

rbtwsClientIpAddrChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 39)
)
rbtwsClientIpAddrChangeTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsUserName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientVLANName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionState"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthServerIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthenProtocolType"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"),
        ("RBTWS-TRAP-MIB", "rbtwsUserAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsLocalId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientIpAddrChangeReason"))
)
if mibBuilder.loadTexts:
    rbtwsClientIpAddrChangeTrap.setStatus(
        "current"
    )

rbtwsClientAssociationSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 40)
)
rbtwsClientAssociationSuccessTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"))
)
if mibBuilder.loadTexts:
    rbtwsClientAssociationSuccessTrap.setStatus(
        "current"
    )

rbtwsClientAuthenticationSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 41)
)
rbtwsClientAuthenticationSuccessTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"))
)
if mibBuilder.loadTexts:
    rbtwsClientAuthenticationSuccessTrap.setStatus(
        "current"
    )

rbtwsClientDeAuthenticationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 42)
)
rbtwsClientDeAuthenticationTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsUserName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientVLANName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthServerIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthenProtocolType"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"))
)
if mibBuilder.loadTexts:
    rbtwsClientDeAuthenticationTrap.setStatus(
        "current"
    )

rbtwsRFDetectBlacklistedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 43)
)
rbtwsRFDetectBlacklistedTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsBlacklistingRemainingTime"),
        ("RBTWS-TRAP-MIB", "rbtwsBlacklistingCause"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectBlacklistedTrap.setStatus(
        "current"
    )

rbtwsRFDetectClientViaRogueWiredAPTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 44)
)
rbtwsRFDetectClientViaRogueWiredAPTrap2.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsSourceWsIp"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsClientVLANid"),
        ("RBTWS-TRAP-MIB", "rbtwsClientVLANtag"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectListenerListInfo"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectRogueAPMacAddr"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectClientViaRogueWiredAPTrap2.setStatus(
        "obsolete"
    )

rbtwsRFDetectAdhocUserDisappearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 45)
)
rbtwsRFDetectAdhocUserDisappearTrap.setObjects(
    ("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr")
)
if mibBuilder.loadTexts:
    rbtwsRFDetectAdhocUserDisappearTrap.setStatus(
        "current"
    )

rbtwsApRejectLicenseExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 46)
)
rbtwsApRejectLicenseExceededTrap.setObjects(
    ("RBTWS-TRAP-MIB", "rbtwsNumLicensedActiveAPs")
)
if mibBuilder.loadTexts:
    rbtwsApRejectLicenseExceededTrap.setStatus(
        "current"
    )

rbtwsClientDynAuthorChangeSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 47)
)
rbtwsClientDynAuthorChangeSuccessTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsUserName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionState"),
        ("RBTWS-TRAP-MIB", "rbtwsClientDynAuthorClientIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthenProtocolType"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"),
        ("RBTWS-TRAP-MIB", "rbtwsUserAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsLocalId"),
        ("RBTWS-TRAP-MIB", "rbtwsChangedUserParamOldValues"),
        ("RBTWS-TRAP-MIB", "rbtwsChangedUserParamNewValues"))
)
if mibBuilder.loadTexts:
    rbtwsClientDynAuthorChangeSuccessTrap.setStatus(
        "current"
    )

rbtwsClientDynAuthorChangeFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 48)
)
rbtwsClientDynAuthorChangeFailureTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsUserName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientDynAuthorClientIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthenProtocolType"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"),
        ("RBTWS-TRAP-MIB", "rbtwsUserParams"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthorizationFailureCause"),
        ("RBTWS-TRAP-MIB", "rbtwsClientFailureCauseDescription"))
)
if mibBuilder.loadTexts:
    rbtwsClientDynAuthorChangeFailureTrap.setStatus(
        "current"
    )

rbtwsClientDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 49)
)
rbtwsClientDisconnectTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsUserName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsDAPNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"),
        ("RBTWS-TRAP-MIB", "rbtwsLocalId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientDisconnectSource"),
        ("RBTWS-TRAP-MIB", "rbtwsClientDisconnectDescription"))
)
if mibBuilder.loadTexts:
    rbtwsClientDisconnectTrap.setStatus(
        "current"
    )

rbtwsMobilityDomainFailOverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 50)
)
rbtwsMobilityDomainFailOverTrap.setObjects(
    ("RBTWS-TRAP-MIB", "rbtwsMobilityDomainSecondarySeedIp")
)
if mibBuilder.loadTexts:
    rbtwsMobilityDomainFailOverTrap.setStatus(
        "current"
    )

rbtwsMobilityDomainFailBackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 51)
)
rbtwsMobilityDomainFailBackTrap.setObjects(
    ("RBTWS-TRAP-MIB", "rbtwsMobilityDomainPrimarySeedIp")
)
if mibBuilder.loadTexts:
    rbtwsMobilityDomainFailBackTrap.setStatus(
        "current"
    )

rbtwsRFDetectRogueDeviceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 52)
)
rbtwsRFDetectRogueDeviceTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectListenerListInfo"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectClassificationReason"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectRogueDeviceTrap.setStatus(
        "obsolete"
    )

rbtwsRFDetectRogueDeviceDisappearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 53)
)
rbtwsRFDetectRogueDeviceDisappearTrap.setObjects(
    ("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr")
)
if mibBuilder.loadTexts:
    rbtwsRFDetectRogueDeviceDisappearTrap.setStatus(
        "current"
    )

rbtwsRFDetectSuspectDeviceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 54)
)
rbtwsRFDetectSuspectDeviceTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectListenerListInfo"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectClassificationReason"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectSuspectDeviceTrap.setStatus(
        "obsolete"
    )

rbtwsRFDetectSuspectDeviceDisappearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 55)
)
rbtwsRFDetectSuspectDeviceDisappearTrap.setObjects(
    ("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr")
)
if mibBuilder.loadTexts:
    rbtwsRFDetectSuspectDeviceDisappearTrap.setStatus(
        "current"
    )

rbtwsRFDetectClientViaRogueWiredAPTrap3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 56)
)
rbtwsRFDetectClientViaRogueWiredAPTrap3.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsSourceWsIp"),
        ("RBTWS-TRAP-MIB", "rbtwsPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsClientVLANid"),
        ("RBTWS-TRAP-MIB", "rbtwsClientVLANtag"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectListenerListInfo"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectRogueAPMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectClassificationReason"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectClientViaRogueWiredAPTrap3.setStatus(
        "current"
    )

rbtwsRFDetectClassificationChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 57)
)
if mibBuilder.loadTexts:
    rbtwsRFDetectClassificationChangeTrap.setStatus(
        "current"
    )

rbtwsConfigurationSavedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 58)
)
rbtwsConfigurationSavedTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsConfigSaveFileName"),
        ("RBTWS-TRAP-MIB", "rbtwsConfigSaveInitiatorType"),
        ("RBTWS-TRAP-MIB", "rbtwsConfigSaveInitiatorIp"),
        ("RBTWS-TRAP-MIB", "rbtwsConfigSaveInitiatorDetails"),
        ("RBTWS-TRAP-MIB", "rbtwsConfigSaveGeneration"))
)
if mibBuilder.loadTexts:
    rbtwsConfigurationSavedTrap.setStatus(
        "current"
    )

rbtwsApNonOperStatusTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 59)
)
rbtwsApNonOperStatusTrap2.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsDeviceSerNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsApNum"),
        ("RBTWS-TRAP-MIB", "rbtwsApName"),
        ("RBTWS-TRAP-MIB", "rbtwsApTransition"),
        ("RBTWS-TRAP-MIB", "rbtwsApFailDetail"),
        ("RBTWS-TRAP-MIB", "rbtwsApWasOperational"))
)
if mibBuilder.loadTexts:
    rbtwsApNonOperStatusTrap2.setStatus(
        "current"
    )

rbtwsApOperRadioStatusTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 60)
)
rbtwsApOperRadioStatusTrap2.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsDeviceSerNum"),
        ("RBTWS-TRAP-MIB", "rbtwsApNum"),
        ("RBTWS-TRAP-MIB", "rbtwsApName"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioType"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioMode"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioConfigState"),
        ("RBTWS-TRAP-MIB", "rbtwsApConnectSecurityType"),
        ("RBTWS-TRAP-MIB", "rbtwsApServiceAvailability"))
)
if mibBuilder.loadTexts:
    rbtwsApOperRadioStatusTrap2.setStatus(
        "obsolete"
    )

rbtwsMichaelMICFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 61)
)
rbtwsMichaelMICFailure.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsApNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsMichaelMICFailureCause"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress2"))
)
if mibBuilder.loadTexts:
    rbtwsMichaelMICFailure.setStatus(
        "current"
    )

rbtwsClientAuthorizationSuccessTrap3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 62)
)
rbtwsClientAuthorizationSuccessTrap3.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsUserName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientVLANName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionState"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthServerIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthenProtocolType"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessMode"),
        ("RBTWS-TRAP-MIB", "rbtwsPhysPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsApNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"),
        ("RBTWS-TRAP-MIB", "rbtwsUserAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsLocalId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthorizationReason"))
)
if mibBuilder.loadTexts:
    rbtwsClientAuthorizationSuccessTrap3.setStatus(
        "obsolete"
    )

rbtwsApManagerChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 63)
)
rbtwsApManagerChangeTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsDeviceSerNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsApNum"),
        ("RBTWS-TRAP-MIB", "rbtwsApName"),
        ("RBTWS-TRAP-MIB", "rbtwsApMgrOldIp"),
        ("RBTWS-TRAP-MIB", "rbtwsApMgrNewIp"),
        ("RBTWS-TRAP-MIB", "rbtwsApMgrChangeReason"))
)
if mibBuilder.loadTexts:
    rbtwsApManagerChangeTrap.setStatus(
        "current"
    )

rbtwsClientClearedTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 64)
)
rbtwsClientClearedTrap2.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsUserName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessMode"),
        ("RBTWS-TRAP-MIB", "rbtwsPhysPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsApNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionElapsedSeconds"),
        ("RBTWS-TRAP-MIB", "rbtwsLocalId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientClearedReason"))
)
if mibBuilder.loadTexts:
    rbtwsClientClearedTrap2.setStatus(
        "current"
    )

rbtwsMobilityDomainResiliencyStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 65)
)
rbtwsMobilityDomainResiliencyStatusTrap.setObjects(
    ("RBTWS-TRAP-MIB", "rbtwsMobilityDomainResiliencyStatus")
)
if mibBuilder.loadTexts:
    rbtwsMobilityDomainResiliencyStatusTrap.setStatus(
        "current"
    )

rbtwsApOperRadioStatusTrap3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 66)
)
rbtwsApOperRadioStatusTrap3.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsDeviceSerNum"),
        ("RBTWS-TRAP-MIB", "rbtwsApNum"),
        ("RBTWS-TRAP-MIB", "rbtwsApName"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioType"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioMode"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioConfigState"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioChannelWidth"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioMimoState"),
        ("RBTWS-TRAP-MIB", "rbtwsApConnectSecurityType"),
        ("RBTWS-TRAP-MIB", "rbtwsApServiceAvailability"))
)
if mibBuilder.loadTexts:
    rbtwsApOperRadioStatusTrap3.setStatus(
        "current"
    )

rbtwsClientAuthorizationSuccessTrap4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 67)
)
rbtwsClientAuthorizationSuccessTrap4.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsUserName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientMACAddress"),
        ("RBTWS-TRAP-MIB", "rbtwsClientIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientVLANName"),
        ("RBTWS-TRAP-MIB", "rbtwsClientSessionState"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthServerIp"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthenProtocolType"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAccessMode"),
        ("RBTWS-TRAP-MIB", "rbtwsPhysPortNum"),
        ("RBTWS-TRAP-MIB", "rbtwsApNum"),
        ("RBTWS-TRAP-MIB", "rbtwsAPRadioNum"),
        ("RBTWS-TRAP-MIB", "rbtwsRadioSSID"),
        ("RBTWS-TRAP-MIB", "rbtwsClientRadioType"),
        ("RBTWS-TRAP-MIB", "rbtwsUserAccessType"),
        ("RBTWS-TRAP-MIB", "rbtwsLocalId"),
        ("RBTWS-TRAP-MIB", "rbtwsClientAuthorizationReason"))
)
if mibBuilder.loadTexts:
    rbtwsClientAuthorizationSuccessTrap4.setStatus(
        "current"
    )

rbtwsRFDetectRogueDeviceTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 68)
)
rbtwsRFDetectRogueDeviceTrap2.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrRadioType"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrCryptoType"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectListenerListInfo"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectClassificationReason"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectRogueDeviceTrap2.setStatus(
        "current"
    )

rbtwsRFDetectSuspectDeviceTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 69)
)
rbtwsRFDetectSuspectDeviceTrap2.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrMacAddr"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrRadioType"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectXmtrCryptoType"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectListenerListInfo"),
        ("RBTWS-TRAP-MIB", "rbtwsRFDetectClassificationReason"))
)
if mibBuilder.loadTexts:
    rbtwsRFDetectSuspectDeviceTrap2.setStatus(
        "current"
    )

rbtwsClusterFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5, 0, 70)
)
rbtwsClusterFailureTrap.setObjects(
      *(("RBTWS-TRAP-MIB", "rbtwsClusterFailureReason"),
        ("RBTWS-TRAP-MIB", "rbtwsClusterFailureDescription"))
)
if mibBuilder.loadTexts:
    rbtwsClusterFailureTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBTWS-TRAP-MIB",
    **{"RbtwsAssociationFailureType": RbtwsAssociationFailureType,
       "RbtwsAuthenticationFailureType": RbtwsAuthenticationFailureType,
       "RbtwsAuthorizationFailureType": RbtwsAuthorizationFailureType,
       "RbtwsDot1xFailureType": RbtwsDot1xFailureType,
       "RbtwsRFDetectDoSType": RbtwsRFDetectDoSType,
       "RbtwsClientIpAddrChangeReason": RbtwsClientIpAddrChangeReason,
       "RbtwsBlacklistingCause": RbtwsBlacklistingCause,
       "RbtwsUserAttributeList": RbtwsUserAttributeList,
       "RbtwsSessionDisconnectType": RbtwsSessionDisconnectType,
       "RbtwsConfigSaveInitiatorType": RbtwsConfigSaveInitiatorType,
       "RbtwsMichaelMICFailureCause": RbtwsMichaelMICFailureCause,
       "RbtwsClientAuthorizationReason": RbtwsClientAuthorizationReason,
       "RbtwsApMgrChangeReason": RbtwsApMgrChangeReason,
       "RbtwsClientClearedReason": RbtwsClientClearedReason,
       "RbtwsMobilityDomainResiliencyStatus": RbtwsMobilityDomainResiliencyStatus,
       "RbtwsClusterFailureReason": RbtwsClusterFailureReason,
       "rbtwsDeviceId": rbtwsDeviceId,
       "rbtwsMobilityDomainIp": rbtwsMobilityDomainIp,
       "rbtwsAPMACAddress": rbtwsAPMACAddress,
       "rbtwsClientMACAddress": rbtwsClientMACAddress,
       "rbtwsRFDetectXmtrMacAddr": rbtwsRFDetectXmtrMacAddr,
       "rbtwsPortNum": rbtwsPortNum,
       "rbtwsAPRadioNum": rbtwsAPRadioNum,
       "rbtwsRadioRssi": rbtwsRadioRssi,
       "rbtwsRadioBSSID": rbtwsRadioBSSID,
       "rbtwsUserName": rbtwsUserName,
       "rbtwsClientAuthServerIp": rbtwsClientAuthServerIp,
       "rbtwsClientSessionState": rbtwsClientSessionState,
       "rbtwsDAPNum": rbtwsDAPNum,
       "rbtwsClientIp": rbtwsClientIp,
       "rbtwsClientSessionId": rbtwsClientSessionId,
       "rbtwsClientAuthenProtocolType": rbtwsClientAuthenProtocolType,
       "rbtwsClientVLANName": rbtwsClientVLANName,
       "rbtwsClientSessionStartTime": rbtwsClientSessionStartTime,
       "rbtwsClientFailureCause": rbtwsClientFailureCause,
       "rbtwsClientRoamedFromPortNum": rbtwsClientRoamedFromPortNum,
       "rbtwsClientRoamedFromRadioNum": rbtwsClientRoamedFromRadioNum,
       "rbtwsClientRoamedFromDAPNum": rbtwsClientRoamedFromDAPNum,
       "rbtwsUserParams": rbtwsUserParams,
       "rbtwsClientLocationPolicyIndex": rbtwsClientLocationPolicyIndex,
       "rbtwsClientAssociationFailureCause": rbtwsClientAssociationFailureCause,
       "rbtwsClientAuthenticationFailureCause": rbtwsClientAuthenticationFailureCause,
       "rbtwsClientAuthorizationFailureCause": rbtwsClientAuthorizationFailureCause,
       "rbtwsClientFailureCauseDescription": rbtwsClientFailureCauseDescription,
       "rbtwsClientRoamedFromWsIp": rbtwsClientRoamedFromWsIp,
       "rbtwsClientRoamedFromAccessType": rbtwsClientRoamedFromAccessType,
       "rbtwsClientAccessType": rbtwsClientAccessType,
       "rbtwsRadioMACAddress": rbtwsRadioMACAddress,
       "rbtwsRadioPowerChangeReason": rbtwsRadioPowerChangeReason,
       "rbtwsNewChannelNum": rbtwsNewChannelNum,
       "rbtwsOldChannelNum": rbtwsOldChannelNum,
       "rbtwsChannelChangeReason": rbtwsChannelChangeReason,
       "rbtwsRFDetectListenerListInfo": rbtwsRFDetectListenerListInfo,
       "rbtwsRadioSSID": rbtwsRadioSSID,
       "rbtwsNewPowerLevel": rbtwsNewPowerLevel,
       "rbtwsOldPowerLevel": rbtwsOldPowerLevel,
       "rbtwsRadioPowerChangeDescription": rbtwsRadioPowerChangeDescription,
       "rbtwsCounterMeasurePerformerListInfo": rbtwsCounterMeasurePerformerListInfo,
       "rbtwsClientDot1xState": rbtwsClientDot1xState,
       "rbtwsClientDot1xFailureCause": rbtwsClientDot1xFailureCause,
       "rbtwsAPAccessType": rbtwsAPAccessType,
       "rbtwsUserAccessType": rbtwsUserAccessType,
       "rbtwsClientSessionElapsedTime": rbtwsClientSessionElapsedTime,
       "rbtwsLocalId": rbtwsLocalId,
       "rbtwsRFDetectDoSType": rbtwsRFDetectDoSType,
       "rbtwsSourceWsIp": rbtwsSourceWsIp,
       "rbtwsClientVLANid": rbtwsClientVLANid,
       "rbtwsClientVLANtag": rbtwsClientVLANtag,
       "rbtwsDeviceModel": rbtwsDeviceModel,
       "rbtwsDeviceSerNum": rbtwsDeviceSerNum,
       "rbtwsRsaPubKeyFingerPrint": rbtwsRsaPubKeyFingerPrint,
       "rbtwsDAPconnectWarningType": rbtwsDAPconnectWarningType,
       "rbtwsClientMACAddress2": rbtwsClientMACAddress2,
       "rbtwsApAttachType": rbtwsApAttachType,
       "rbtwsApPortOrDapNum": rbtwsApPortOrDapNum,
       "rbtwsApName": rbtwsApName,
       "rbtwsApTransition": rbtwsApTransition,
       "rbtwsApFailDetail": rbtwsApFailDetail,
       "rbtwsRadioType": rbtwsRadioType,
       "rbtwsRadioConfigState": rbtwsRadioConfigState,
       "rbtwsApConnectSecurityType": rbtwsApConnectSecurityType,
       "rbtwsApServiceAvailability": rbtwsApServiceAvailability,
       "rbtwsApWasOperational": rbtwsApWasOperational,
       "rbtwsClientTimeSinceLastRoam": rbtwsClientTimeSinceLastRoam,
       "rbtwsClientIpAddrChangeReason": rbtwsClientIpAddrChangeReason,
       "rbtwsRFDetectRogueAPMacAddr": rbtwsRFDetectRogueAPMacAddr,
       "rbtwsBlacklistingRemainingTime": rbtwsBlacklistingRemainingTime,
       "rbtwsBlacklistingCause": rbtwsBlacklistingCause,
       "rbtwsNumLicensedActiveAPs": rbtwsNumLicensedActiveAPs,
       "rbtwsClientDynAuthorClientIp": rbtwsClientDynAuthorClientIp,
       "rbtwsChangedUserParamOldValues": rbtwsChangedUserParamOldValues,
       "rbtwsChangedUserParamNewValues": rbtwsChangedUserParamNewValues,
       "rbtwsClientDisconnectSource": rbtwsClientDisconnectSource,
       "rbtwsClientDisconnectDescription": rbtwsClientDisconnectDescription,
       "rbtwsMobilityDomainSecondarySeedIp": rbtwsMobilityDomainSecondarySeedIp,
       "rbtwsMobilityDomainPrimarySeedIp": rbtwsMobilityDomainPrimarySeedIp,
       "rbtwsRFDetectClassificationReason": rbtwsRFDetectClassificationReason,
       "rbtwsConfigSaveFileName": rbtwsConfigSaveFileName,
       "rbtwsConfigSaveInitiatorType": rbtwsConfigSaveInitiatorType,
       "rbtwsConfigSaveInitiatorIp": rbtwsConfigSaveInitiatorIp,
       "rbtwsConfigSaveInitiatorDetails": rbtwsConfigSaveInitiatorDetails,
       "rbtwsConfigSaveGeneration": rbtwsConfigSaveGeneration,
       "rbtwsApNum": rbtwsApNum,
       "rbtwsRadioMode": rbtwsRadioMode,
       "rbtwsMichaelMICFailureCause": rbtwsMichaelMICFailureCause,
       "rbtwsClientAccessMode": rbtwsClientAccessMode,
       "rbtwsClientAuthorizationReason": rbtwsClientAuthorizationReason,
       "rbtwsPhysPortNum": rbtwsPhysPortNum,
       "rbtwsApMgrOldIp": rbtwsApMgrOldIp,
       "rbtwsApMgrNewIp": rbtwsApMgrNewIp,
       "rbtwsApMgrChangeReason": rbtwsApMgrChangeReason,
       "rbtwsClientClearedReason": rbtwsClientClearedReason,
       "rbtwsMobilityDomainResiliencyStatus": rbtwsMobilityDomainResiliencyStatus,
       "rbtwsClientSessionElapsedSeconds": rbtwsClientSessionElapsedSeconds,
       "rbtwsRadioChannelWidth": rbtwsRadioChannelWidth,
       "rbtwsRadioMimoState": rbtwsRadioMimoState,
       "rbtwsClientRadioType": rbtwsClientRadioType,
       "rbtwsRFDetectXmtrRadioType": rbtwsRFDetectXmtrRadioType,
       "rbtwsRFDetectXmtrCryptoType": rbtwsRFDetectXmtrCryptoType,
       "rbtwsClusterFailureReason": rbtwsClusterFailureReason,
       "rbtwsClusterFailureDescription": rbtwsClusterFailureDescription,
       "rbtwsTrapMib": rbtwsTrapMib,
       "rbtwsTrapsV2": rbtwsTrapsV2,
       "rbtwsDeviceFailTrap": rbtwsDeviceFailTrap,
       "rbtwsDeviceOkayTrap": rbtwsDeviceOkayTrap,
       "rbtwsPoEFailTrap": rbtwsPoEFailTrap,
       "rbtwsApTimeoutTrap": rbtwsApTimeoutTrap,
       "rbtwsAPBootTrap": rbtwsAPBootTrap,
       "rbtwsMobilityDomainJoinTrap": rbtwsMobilityDomainJoinTrap,
       "rbtwsMobilityDomainTimeoutTrap": rbtwsMobilityDomainTimeoutTrap,
       "rbtwsMpMichaelMICFailure": rbtwsMpMichaelMICFailure,
       "rbtwsRFDetectRogueAPTrap": rbtwsRFDetectRogueAPTrap,
       "rbtwsRFDetectAdhocUserTrap": rbtwsRFDetectAdhocUserTrap,
       "rbtwsRFDetectRogueDisappearTrap": rbtwsRFDetectRogueDisappearTrap,
       "rbtwsClientAuthenticationFailureTrap": rbtwsClientAuthenticationFailureTrap,
       "rbtwsClientAuthorizationFailureTrap": rbtwsClientAuthorizationFailureTrap,
       "rbtwsClientAssociationFailureTrap": rbtwsClientAssociationFailureTrap,
       "rbtwsClientAuthorizationSuccessTrap": rbtwsClientAuthorizationSuccessTrap,
       "rbtwsClientDeAssociationTrap": rbtwsClientDeAssociationTrap,
       "rbtwsClientRoamingTrap": rbtwsClientRoamingTrap,
       "rbtwsAutoTuneRadioPowerChangeTrap": rbtwsAutoTuneRadioPowerChangeTrap,
       "rbtwsAutoTuneRadioChannelChangeTrap": rbtwsAutoTuneRadioChannelChangeTrap,
       "rbtwsCounterMeasureStartTrap": rbtwsCounterMeasureStartTrap,
       "rbtwsCounterMeasureStopTrap": rbtwsCounterMeasureStopTrap,
       "rbtwsClientDot1xFailureTrap": rbtwsClientDot1xFailureTrap,
       "rbtwsClientClearedTrap": rbtwsClientClearedTrap,
       "rbtwsClientAuthorizationSuccessTrap2": rbtwsClientAuthorizationSuccessTrap2,
       "rbtwsRFDetectSpoofedMacAPTrap": rbtwsRFDetectSpoofedMacAPTrap,
       "rbtwsRFDetectSpoofedSsidAPTrap": rbtwsRFDetectSpoofedSsidAPTrap,
       "rbtwsRFDetectDoSTrap": rbtwsRFDetectDoSTrap,
       "rbtwsRFDetectClientViaRogueWiredAPTrap": rbtwsRFDetectClientViaRogueWiredAPTrap,
       "rbtwsRFDetectInterferingRogueAPTrap": rbtwsRFDetectInterferingRogueAPTrap,
       "rbtwsRFDetectInterferingRogueDisappearTrap": rbtwsRFDetectInterferingRogueDisappearTrap,
       "rbtwsRFDetectUnAuthorizedSsidTrap": rbtwsRFDetectUnAuthorizedSsidTrap,
       "rbtwsRFDetectUnAuthorizedOuiTrap": rbtwsRFDetectUnAuthorizedOuiTrap,
       "rbtwsRFDetectUnAuthorizedAPTrap": rbtwsRFDetectUnAuthorizedAPTrap,
       "rbtwsDAPConnectWarningTrap": rbtwsDAPConnectWarningTrap,
       "rbtwsRFDetectDoSPortTrap": rbtwsRFDetectDoSPortTrap,
       "rbtwsMpMichaelMICFailure2": rbtwsMpMichaelMICFailure2,
       "rbtwsApNonOperStatusTrap": rbtwsApNonOperStatusTrap,
       "rbtwsApOperRadioStatusTrap": rbtwsApOperRadioStatusTrap,
       "rbtwsClientIpAddrChangeTrap": rbtwsClientIpAddrChangeTrap,
       "rbtwsClientAssociationSuccessTrap": rbtwsClientAssociationSuccessTrap,
       "rbtwsClientAuthenticationSuccessTrap": rbtwsClientAuthenticationSuccessTrap,
       "rbtwsClientDeAuthenticationTrap": rbtwsClientDeAuthenticationTrap,
       "rbtwsRFDetectBlacklistedTrap": rbtwsRFDetectBlacklistedTrap,
       "rbtwsRFDetectClientViaRogueWiredAPTrap2": rbtwsRFDetectClientViaRogueWiredAPTrap2,
       "rbtwsRFDetectAdhocUserDisappearTrap": rbtwsRFDetectAdhocUserDisappearTrap,
       "rbtwsApRejectLicenseExceededTrap": rbtwsApRejectLicenseExceededTrap,
       "rbtwsClientDynAuthorChangeSuccessTrap": rbtwsClientDynAuthorChangeSuccessTrap,
       "rbtwsClientDynAuthorChangeFailureTrap": rbtwsClientDynAuthorChangeFailureTrap,
       "rbtwsClientDisconnectTrap": rbtwsClientDisconnectTrap,
       "rbtwsMobilityDomainFailOverTrap": rbtwsMobilityDomainFailOverTrap,
       "rbtwsMobilityDomainFailBackTrap": rbtwsMobilityDomainFailBackTrap,
       "rbtwsRFDetectRogueDeviceTrap": rbtwsRFDetectRogueDeviceTrap,
       "rbtwsRFDetectRogueDeviceDisappearTrap": rbtwsRFDetectRogueDeviceDisappearTrap,
       "rbtwsRFDetectSuspectDeviceTrap": rbtwsRFDetectSuspectDeviceTrap,
       "rbtwsRFDetectSuspectDeviceDisappearTrap": rbtwsRFDetectSuspectDeviceDisappearTrap,
       "rbtwsRFDetectClientViaRogueWiredAPTrap3": rbtwsRFDetectClientViaRogueWiredAPTrap3,
       "rbtwsRFDetectClassificationChangeTrap": rbtwsRFDetectClassificationChangeTrap,
       "rbtwsConfigurationSavedTrap": rbtwsConfigurationSavedTrap,
       "rbtwsApNonOperStatusTrap2": rbtwsApNonOperStatusTrap2,
       "rbtwsApOperRadioStatusTrap2": rbtwsApOperRadioStatusTrap2,
       "rbtwsMichaelMICFailure": rbtwsMichaelMICFailure,
       "rbtwsClientAuthorizationSuccessTrap3": rbtwsClientAuthorizationSuccessTrap3,
       "rbtwsApManagerChangeTrap": rbtwsApManagerChangeTrap,
       "rbtwsClientClearedTrap2": rbtwsClientClearedTrap2,
       "rbtwsMobilityDomainResiliencyStatusTrap": rbtwsMobilityDomainResiliencyStatusTrap,
       "rbtwsApOperRadioStatusTrap3": rbtwsApOperRadioStatusTrap3,
       "rbtwsClientAuthorizationSuccessTrap4": rbtwsClientAuthorizationSuccessTrap4,
       "rbtwsRFDetectRogueDeviceTrap2": rbtwsRFDetectRogueDeviceTrap2,
       "rbtwsRFDetectSuspectDeviceTrap2": rbtwsRFDetectSuspectDeviceTrap2,
       "rbtwsClusterFailureTrap": rbtwsClusterFailureTrap}
)
