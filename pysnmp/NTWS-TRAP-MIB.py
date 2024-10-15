# SNMP MIB module (NTWS-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTWS-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:01 2024
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

(NtwsAccessType,
 NtwsApAttachType,
 NtwsApConnectSecurityType,
 NtwsApFailDetail,
 NtwsApFingerprint,
 NtwsApNum,
 NtwsApPortOrDapNum,
 NtwsApSerialNum,
 NtwsApServiceAvailability,
 NtwsApTransition,
 NtwsApWasOperational,
 NtwsChannelChangeType,
 NtwsCryptoType,
 NtwsPowerLevel,
 NtwsRadioChannelWidth,
 NtwsRadioConfigState,
 NtwsRadioMimoState,
 NtwsRadioMode,
 NtwsRadioNum,
 NtwsRadioPowerChangeType,
 NtwsRadioType) = mibBuilder.importSymbols(
    "NTWS-AP-TC",
    "NtwsAccessType",
    "NtwsApAttachType",
    "NtwsApConnectSecurityType",
    "NtwsApFailDetail",
    "NtwsApFingerprint",
    "NtwsApNum",
    "NtwsApPortOrDapNum",
    "NtwsApSerialNum",
    "NtwsApServiceAvailability",
    "NtwsApTransition",
    "NtwsApWasOperational",
    "NtwsChannelChangeType",
    "NtwsCryptoType",
    "NtwsPowerLevel",
    "NtwsRadioChannelWidth",
    "NtwsRadioConfigState",
    "NtwsRadioMimoState",
    "NtwsRadioMode",
    "NtwsRadioNum",
    "NtwsRadioPowerChangeType",
    "NtwsRadioType")

(NtwsClientAccessMode,
 NtwsClientAuthenProtocolType,
 NtwsClientDot1xState,
 NtwsClientSessionState,
 NtwsUserAccessType) = mibBuilder.importSymbols(
    "NTWS-CLIENT-SESSION-TC",
    "NtwsClientAccessMode",
    "NtwsClientAuthenProtocolType",
    "NtwsClientDot1xState",
    "NtwsClientSessionState",
    "NtwsUserAccessType")

(NtwsRFDetectClassificationReason,) = mibBuilder.importSymbols(
    "NTWS-RF-DETECT-TC",
    "NtwsRFDetectClassificationReason")

(ntwsMibs,
 ntwsTemporary,
 ntwsTraps) = mibBuilder.importSymbols(
    "NTWS-ROOT-MIB",
    "ntwsMibs",
    "ntwsTemporary",
    "ntwsTraps")

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

ntwsTrapMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 1)
)
ntwsTrapMib.setRevisions(
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
         "2007-08-31 01:30",
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



class NtwsAssociationFailureType(Integer32, TextualConvention):
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



class NtwsAuthenticationFailureType(Integer32, TextualConvention):
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



class NtwsAuthorizationFailureType(Integer32, TextualConvention):
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



class NtwsDot1xFailureType(Integer32, TextualConvention):
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



class NtwsRFDetectDoSType(Integer32, TextualConvention):
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



class NtwsClientIpAddrChangeReason(Integer32, TextualConvention):
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



class NtwsBlacklistingCause(Integer32, TextualConvention):
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



class NtwsUserAttributeList(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )



class NtwsSessionDisconnectType(Integer32, TextualConvention):
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



class NtwsConfigSaveInitiatorType(Integer32, TextualConvention):
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



class NtwsMichaelMICFailureCause(Integer32, TextualConvention):
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



class NtwsClientAuthorizationReason(Integer32, TextualConvention):
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



class NtwsApMgrChangeReason(Integer32, TextualConvention):
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



class NtwsClientClearedReason(Integer32, TextualConvention):
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



class NtwsMobilityDomainResiliencyStatus(Integer32, TextualConvention):
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



class NtwsClusterFailureReason(Integer32, TextualConvention):
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

_NtwsDeviceId_Type = ObjectIdentifier
_NtwsDeviceId_Object = MibScalar
ntwsDeviceId = _NtwsDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 1),
    _NtwsDeviceId_Type()
)
ntwsDeviceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsDeviceId.setStatus("current")
_NtwsMobilityDomainIp_Type = IpAddress
_NtwsMobilityDomainIp_Object = MibScalar
ntwsMobilityDomainIp = _NtwsMobilityDomainIp_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 2),
    _NtwsMobilityDomainIp_Type()
)
ntwsMobilityDomainIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsMobilityDomainIp.setStatus("current")
_NtwsAPMACAddress_Type = MacAddress
_NtwsAPMACAddress_Object = MibScalar
ntwsAPMACAddress = _NtwsAPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 3),
    _NtwsAPMACAddress_Type()
)
ntwsAPMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsAPMACAddress.setStatus("current")
_NtwsClientMACAddress_Type = MacAddress
_NtwsClientMACAddress_Object = MibScalar
ntwsClientMACAddress = _NtwsClientMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 4),
    _NtwsClientMACAddress_Type()
)
ntwsClientMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientMACAddress.setStatus("current")
_NtwsRFDetectXmtrMacAddr_Type = MacAddress
_NtwsRFDetectXmtrMacAddr_Object = MibScalar
ntwsRFDetectXmtrMacAddr = _NtwsRFDetectXmtrMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 5),
    _NtwsRFDetectXmtrMacAddr_Type()
)
ntwsRFDetectXmtrMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRFDetectXmtrMacAddr.setStatus("current")


class _NtwsPortNum_Type(Integer32):
    """Custom type ntwsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 22),
    )


_NtwsPortNum_Type.__name__ = "Integer32"
_NtwsPortNum_Object = MibScalar
ntwsPortNum = _NtwsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 6),
    _NtwsPortNum_Type()
)
ntwsPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsPortNum.setStatus("current")
_NtwsAPRadioNum_Type = NtwsRadioNum
_NtwsAPRadioNum_Object = MibScalar
ntwsAPRadioNum = _NtwsAPRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 7),
    _NtwsAPRadioNum_Type()
)
ntwsAPRadioNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsAPRadioNum.setStatus("current")


class _NtwsRadioRssi_Type(Integer32):
    """Custom type ntwsRadioRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_NtwsRadioRssi_Type.__name__ = "Integer32"
_NtwsRadioRssi_Object = MibScalar
ntwsRadioRssi = _NtwsRadioRssi_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 8),
    _NtwsRadioRssi_Type()
)
ntwsRadioRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRadioRssi.setStatus("obsolete")


class _NtwsRadioBSSID_Type(OctetString):
    """Custom type ntwsRadioBSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NtwsRadioBSSID_Type.__name__ = "OctetString"
_NtwsRadioBSSID_Object = MibScalar
ntwsRadioBSSID = _NtwsRadioBSSID_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 9),
    _NtwsRadioBSSID_Type()
)
ntwsRadioBSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRadioBSSID.setStatus("current")


class _NtwsUserName_Type(DisplayString):
    """Custom type ntwsUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtwsUserName_Type.__name__ = "DisplayString"
_NtwsUserName_Object = MibScalar
ntwsUserName = _NtwsUserName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 10),
    _NtwsUserName_Type()
)
ntwsUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsUserName.setStatus("current")
_NtwsClientAuthServerIp_Type = IpAddress
_NtwsClientAuthServerIp_Object = MibScalar
ntwsClientAuthServerIp = _NtwsClientAuthServerIp_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 11),
    _NtwsClientAuthServerIp_Type()
)
ntwsClientAuthServerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientAuthServerIp.setStatus("current")
_NtwsClientSessionState_Type = NtwsClientSessionState
_NtwsClientSessionState_Object = MibScalar
ntwsClientSessionState = _NtwsClientSessionState_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 12),
    _NtwsClientSessionState_Type()
)
ntwsClientSessionState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientSessionState.setStatus("current")


class _NtwsDAPNum_Type(Integer32):
    """Custom type ntwsDAPNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NtwsDAPNum_Type.__name__ = "Integer32"
_NtwsDAPNum_Object = MibScalar
ntwsDAPNum = _NtwsDAPNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 13),
    _NtwsDAPNum_Type()
)
ntwsDAPNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsDAPNum.setStatus("current")
_NtwsClientIp_Type = IpAddress
_NtwsClientIp_Object = MibScalar
ntwsClientIp = _NtwsClientIp_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 14),
    _NtwsClientIp_Type()
)
ntwsClientIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientIp.setStatus("current")


class _NtwsClientSessionId_Type(DisplayString):
    """Custom type ntwsClientSessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtwsClientSessionId_Type.__name__ = "DisplayString"
_NtwsClientSessionId_Object = MibScalar
ntwsClientSessionId = _NtwsClientSessionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 15),
    _NtwsClientSessionId_Type()
)
ntwsClientSessionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientSessionId.setStatus("current")
_NtwsClientAuthenProtocolType_Type = NtwsClientAuthenProtocolType
_NtwsClientAuthenProtocolType_Object = MibScalar
ntwsClientAuthenProtocolType = _NtwsClientAuthenProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 16),
    _NtwsClientAuthenProtocolType_Type()
)
ntwsClientAuthenProtocolType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientAuthenProtocolType.setStatus("current")


class _NtwsClientVLANName_Type(DisplayString):
    """Custom type ntwsClientVLANName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtwsClientVLANName_Type.__name__ = "DisplayString"
_NtwsClientVLANName_Object = MibScalar
ntwsClientVLANName = _NtwsClientVLANName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 17),
    _NtwsClientVLANName_Type()
)
ntwsClientVLANName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientVLANName.setStatus("current")
_NtwsClientSessionStartTime_Type = TimeTicks
_NtwsClientSessionStartTime_Object = MibScalar
ntwsClientSessionStartTime = _NtwsClientSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 18),
    _NtwsClientSessionStartTime_Type()
)
ntwsClientSessionStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientSessionStartTime.setStatus("obsolete")


class _NtwsClientFailureCause_Type(DisplayString):
    """Custom type ntwsClientFailureCause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsClientFailureCause_Type.__name__ = "DisplayString"
_NtwsClientFailureCause_Object = MibScalar
ntwsClientFailureCause = _NtwsClientFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 19),
    _NtwsClientFailureCause_Type()
)
ntwsClientFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientFailureCause.setStatus("current")


class _NtwsClientRoamedFromPortNum_Type(Integer32):
    """Custom type ntwsClientRoamedFromPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_NtwsClientRoamedFromPortNum_Type.__name__ = "Integer32"
_NtwsClientRoamedFromPortNum_Object = MibScalar
ntwsClientRoamedFromPortNum = _NtwsClientRoamedFromPortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 20),
    _NtwsClientRoamedFromPortNum_Type()
)
ntwsClientRoamedFromPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientRoamedFromPortNum.setStatus("current")
_NtwsClientRoamedFromRadioNum_Type = NtwsRadioNum
_NtwsClientRoamedFromRadioNum_Object = MibScalar
ntwsClientRoamedFromRadioNum = _NtwsClientRoamedFromRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 21),
    _NtwsClientRoamedFromRadioNum_Type()
)
ntwsClientRoamedFromRadioNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientRoamedFromRadioNum.setStatus("current")


class _NtwsClientRoamedFromDAPNum_Type(Integer32):
    """Custom type ntwsClientRoamedFromDAPNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NtwsClientRoamedFromDAPNum_Type.__name__ = "Integer32"
_NtwsClientRoamedFromDAPNum_Object = MibScalar
ntwsClientRoamedFromDAPNum = _NtwsClientRoamedFromDAPNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 22),
    _NtwsClientRoamedFromDAPNum_Type()
)
ntwsClientRoamedFromDAPNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientRoamedFromDAPNum.setStatus("current")


class _NtwsUserParams_Type(DisplayString):
    """Custom type ntwsUserParams based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsUserParams_Type.__name__ = "DisplayString"
_NtwsUserParams_Object = MibScalar
ntwsUserParams = _NtwsUserParams_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 23),
    _NtwsUserParams_Type()
)
ntwsUserParams.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsUserParams.setStatus("current")


class _NtwsClientLocationPolicyIndex_Type(Integer32):
    """Custom type ntwsClientLocationPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_NtwsClientLocationPolicyIndex_Type.__name__ = "Integer32"
_NtwsClientLocationPolicyIndex_Object = MibScalar
ntwsClientLocationPolicyIndex = _NtwsClientLocationPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 24),
    _NtwsClientLocationPolicyIndex_Type()
)
ntwsClientLocationPolicyIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientLocationPolicyIndex.setStatus("current")
_NtwsClientAssociationFailureCause_Type = NtwsAssociationFailureType
_NtwsClientAssociationFailureCause_Object = MibScalar
ntwsClientAssociationFailureCause = _NtwsClientAssociationFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 25),
    _NtwsClientAssociationFailureCause_Type()
)
ntwsClientAssociationFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientAssociationFailureCause.setStatus("current")
_NtwsClientAuthenticationFailureCause_Type = NtwsAuthenticationFailureType
_NtwsClientAuthenticationFailureCause_Object = MibScalar
ntwsClientAuthenticationFailureCause = _NtwsClientAuthenticationFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 26),
    _NtwsClientAuthenticationFailureCause_Type()
)
ntwsClientAuthenticationFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientAuthenticationFailureCause.setStatus("current")
_NtwsClientAuthorizationFailureCause_Type = NtwsAuthorizationFailureType
_NtwsClientAuthorizationFailureCause_Object = MibScalar
ntwsClientAuthorizationFailureCause = _NtwsClientAuthorizationFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 27),
    _NtwsClientAuthorizationFailureCause_Type()
)
ntwsClientAuthorizationFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientAuthorizationFailureCause.setStatus("current")


class _NtwsClientFailureCauseDescription_Type(DisplayString):
    """Custom type ntwsClientFailureCauseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsClientFailureCauseDescription_Type.__name__ = "DisplayString"
_NtwsClientFailureCauseDescription_Object = MibScalar
ntwsClientFailureCauseDescription = _NtwsClientFailureCauseDescription_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 28),
    _NtwsClientFailureCauseDescription_Type()
)
ntwsClientFailureCauseDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientFailureCauseDescription.setStatus("current")
_NtwsClientRoamedFromWsIp_Type = IpAddress
_NtwsClientRoamedFromWsIp_Object = MibScalar
ntwsClientRoamedFromWsIp = _NtwsClientRoamedFromWsIp_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 29),
    _NtwsClientRoamedFromWsIp_Type()
)
ntwsClientRoamedFromWsIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientRoamedFromWsIp.setStatus("current")
_NtwsClientRoamedFromAccessType_Type = NtwsAccessType
_NtwsClientRoamedFromAccessType_Object = MibScalar
ntwsClientRoamedFromAccessType = _NtwsClientRoamedFromAccessType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 30),
    _NtwsClientRoamedFromAccessType_Type()
)
ntwsClientRoamedFromAccessType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientRoamedFromAccessType.setStatus("current")
_NtwsClientAccessType_Type = NtwsAccessType
_NtwsClientAccessType_Object = MibScalar
ntwsClientAccessType = _NtwsClientAccessType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 31),
    _NtwsClientAccessType_Type()
)
ntwsClientAccessType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientAccessType.setStatus("current")
_NtwsRadioMACAddress_Type = MacAddress
_NtwsRadioMACAddress_Object = MibScalar
ntwsRadioMACAddress = _NtwsRadioMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 32),
    _NtwsRadioMACAddress_Type()
)
ntwsRadioMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRadioMACAddress.setStatus("current")
_NtwsRadioPowerChangeReason_Type = NtwsRadioPowerChangeType
_NtwsRadioPowerChangeReason_Object = MibScalar
ntwsRadioPowerChangeReason = _NtwsRadioPowerChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 33),
    _NtwsRadioPowerChangeReason_Type()
)
ntwsRadioPowerChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRadioPowerChangeReason.setStatus("current")


class _NtwsNewChannelNum_Type(Integer32):
    """Custom type ntwsNewChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_NtwsNewChannelNum_Type.__name__ = "Integer32"
_NtwsNewChannelNum_Object = MibScalar
ntwsNewChannelNum = _NtwsNewChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 34),
    _NtwsNewChannelNum_Type()
)
ntwsNewChannelNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsNewChannelNum.setStatus("current")


class _NtwsOldChannelNum_Type(Integer32):
    """Custom type ntwsOldChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_NtwsOldChannelNum_Type.__name__ = "Integer32"
_NtwsOldChannelNum_Object = MibScalar
ntwsOldChannelNum = _NtwsOldChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 35),
    _NtwsOldChannelNum_Type()
)
ntwsOldChannelNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsOldChannelNum.setStatus("current")
_NtwsChannelChangeReason_Type = NtwsChannelChangeType
_NtwsChannelChangeReason_Object = MibScalar
ntwsChannelChangeReason = _NtwsChannelChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 36),
    _NtwsChannelChangeReason_Type()
)
ntwsChannelChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsChannelChangeReason.setStatus("current")


class _NtwsRFDetectListenerListInfo_Type(OctetString):
    """Custom type ntwsRFDetectListenerListInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 571),
    )


_NtwsRFDetectListenerListInfo_Type.__name__ = "OctetString"
_NtwsRFDetectListenerListInfo_Object = MibScalar
ntwsRFDetectListenerListInfo = _NtwsRFDetectListenerListInfo_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 37),
    _NtwsRFDetectListenerListInfo_Type()
)
ntwsRFDetectListenerListInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRFDetectListenerListInfo.setStatus("current")


class _NtwsRadioSSID_Type(DisplayString):
    """Custom type ntwsRadioSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtwsRadioSSID_Type.__name__ = "DisplayString"
_NtwsRadioSSID_Object = MibScalar
ntwsRadioSSID = _NtwsRadioSSID_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 38),
    _NtwsRadioSSID_Type()
)
ntwsRadioSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRadioSSID.setStatus("current")
_NtwsNewPowerLevel_Type = NtwsPowerLevel
_NtwsNewPowerLevel_Object = MibScalar
ntwsNewPowerLevel = _NtwsNewPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 39),
    _NtwsNewPowerLevel_Type()
)
ntwsNewPowerLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsNewPowerLevel.setStatus("current")
_NtwsOldPowerLevel_Type = NtwsPowerLevel
_NtwsOldPowerLevel_Object = MibScalar
ntwsOldPowerLevel = _NtwsOldPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 40),
    _NtwsOldPowerLevel_Type()
)
ntwsOldPowerLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsOldPowerLevel.setStatus("current")


class _NtwsRadioPowerChangeDescription_Type(DisplayString):
    """Custom type ntwsRadioPowerChangeDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsRadioPowerChangeDescription_Type.__name__ = "DisplayString"
_NtwsRadioPowerChangeDescription_Object = MibScalar
ntwsRadioPowerChangeDescription = _NtwsRadioPowerChangeDescription_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 41),
    _NtwsRadioPowerChangeDescription_Type()
)
ntwsRadioPowerChangeDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRadioPowerChangeDescription.setStatus("current")


class _NtwsCounterMeasurePerformerListInfo_Type(DisplayString):
    """Custom type ntwsCounterMeasurePerformerListInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsCounterMeasurePerformerListInfo_Type.__name__ = "DisplayString"
_NtwsCounterMeasurePerformerListInfo_Object = MibScalar
ntwsCounterMeasurePerformerListInfo = _NtwsCounterMeasurePerformerListInfo_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 42),
    _NtwsCounterMeasurePerformerListInfo_Type()
)
ntwsCounterMeasurePerformerListInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsCounterMeasurePerformerListInfo.setStatus("obsolete")
_NtwsClientDot1xState_Type = NtwsClientDot1xState
_NtwsClientDot1xState_Object = MibScalar
ntwsClientDot1xState = _NtwsClientDot1xState_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 43),
    _NtwsClientDot1xState_Type()
)
ntwsClientDot1xState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientDot1xState.setStatus("current")
_NtwsClientDot1xFailureCause_Type = NtwsDot1xFailureType
_NtwsClientDot1xFailureCause_Object = MibScalar
ntwsClientDot1xFailureCause = _NtwsClientDot1xFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 44),
    _NtwsClientDot1xFailureCause_Type()
)
ntwsClientDot1xFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientDot1xFailureCause.setStatus("current")
_NtwsAPAccessType_Type = NtwsAccessType
_NtwsAPAccessType_Object = MibScalar
ntwsAPAccessType = _NtwsAPAccessType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 45),
    _NtwsAPAccessType_Type()
)
ntwsAPAccessType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsAPAccessType.setStatus("obsolete")
_NtwsUserAccessType_Type = NtwsUserAccessType
_NtwsUserAccessType_Object = MibScalar
ntwsUserAccessType = _NtwsUserAccessType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 46),
    _NtwsUserAccessType_Type()
)
ntwsUserAccessType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsUserAccessType.setStatus("current")
_NtwsClientSessionElapsedTime_Type = TimeTicks
_NtwsClientSessionElapsedTime_Object = MibScalar
ntwsClientSessionElapsedTime = _NtwsClientSessionElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 47),
    _NtwsClientSessionElapsedTime_Type()
)
ntwsClientSessionElapsedTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientSessionElapsedTime.setStatus("obsolete")


class _NtwsLocalId_Type(Integer32):
    """Custom type ntwsLocalId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_NtwsLocalId_Type.__name__ = "Integer32"
_NtwsLocalId_Object = MibScalar
ntwsLocalId = _NtwsLocalId_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 48),
    _NtwsLocalId_Type()
)
ntwsLocalId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsLocalId.setStatus("current")
_NtwsRFDetectDoSType_Type = NtwsRFDetectDoSType
_NtwsRFDetectDoSType_Object = MibScalar
ntwsRFDetectDoSType = _NtwsRFDetectDoSType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 49),
    _NtwsRFDetectDoSType_Type()
)
ntwsRFDetectDoSType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRFDetectDoSType.setStatus("current")
_NtwsSourceWsIp_Type = IpAddress
_NtwsSourceWsIp_Object = MibScalar
ntwsSourceWsIp = _NtwsSourceWsIp_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 50),
    _NtwsSourceWsIp_Type()
)
ntwsSourceWsIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsSourceWsIp.setStatus("current")


class _NtwsClientVLANid_Type(Integer32):
    """Custom type ntwsClientVLANid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NtwsClientVLANid_Type.__name__ = "Integer32"
_NtwsClientVLANid_Object = MibScalar
ntwsClientVLANid = _NtwsClientVLANid_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 51),
    _NtwsClientVLANid_Type()
)
ntwsClientVLANid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientVLANid.setStatus("current")


class _NtwsClientVLANtag_Type(Integer32):
    """Custom type ntwsClientVLANtag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NtwsClientVLANtag_Type.__name__ = "Integer32"
_NtwsClientVLANtag_Object = MibScalar
ntwsClientVLANtag = _NtwsClientVLANtag_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 52),
    _NtwsClientVLANtag_Type()
)
ntwsClientVLANtag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientVLANtag.setStatus("current")
_NtwsDeviceModel_Type = DisplayString
_NtwsDeviceModel_Object = MibScalar
ntwsDeviceModel = _NtwsDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 53),
    _NtwsDeviceModel_Type()
)
ntwsDeviceModel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsDeviceModel.setStatus("current")
_NtwsDeviceSerNum_Type = NtwsApSerialNum
_NtwsDeviceSerNum_Object = MibScalar
ntwsDeviceSerNum = _NtwsDeviceSerNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 54),
    _NtwsDeviceSerNum_Type()
)
ntwsDeviceSerNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsDeviceSerNum.setStatus("current")
_NtwsRsaPubKeyFingerPrint_Type = NtwsApFingerprint
_NtwsRsaPubKeyFingerPrint_Object = MibScalar
ntwsRsaPubKeyFingerPrint = _NtwsRsaPubKeyFingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 55),
    _NtwsRsaPubKeyFingerPrint_Type()
)
ntwsRsaPubKeyFingerPrint.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRsaPubKeyFingerPrint.setStatus("current")


class _NtwsDAPconnectWarningType_Type(Integer32):
    """Custom type ntwsDAPconnectWarningType based on Integer32"""
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


_NtwsDAPconnectWarningType_Type.__name__ = "Integer32"
_NtwsDAPconnectWarningType_Object = MibScalar
ntwsDAPconnectWarningType = _NtwsDAPconnectWarningType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 56),
    _NtwsDAPconnectWarningType_Type()
)
ntwsDAPconnectWarningType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsDAPconnectWarningType.setStatus("current")
_NtwsClientMACAddress2_Type = MacAddress
_NtwsClientMACAddress2_Object = MibScalar
ntwsClientMACAddress2 = _NtwsClientMACAddress2_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 57),
    _NtwsClientMACAddress2_Type()
)
ntwsClientMACAddress2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientMACAddress2.setStatus("current")
_NtwsApAttachType_Type = NtwsApAttachType
_NtwsApAttachType_Object = MibScalar
ntwsApAttachType = _NtwsApAttachType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 58),
    _NtwsApAttachType_Type()
)
ntwsApAttachType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsApAttachType.setStatus("current")
_NtwsApPortOrDapNum_Type = NtwsApPortOrDapNum
_NtwsApPortOrDapNum_Object = MibScalar
ntwsApPortOrDapNum = _NtwsApPortOrDapNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 59),
    _NtwsApPortOrDapNum_Type()
)
ntwsApPortOrDapNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsApPortOrDapNum.setStatus("obsolete")
_NtwsApName_Type = DisplayString
_NtwsApName_Object = MibScalar
ntwsApName = _NtwsApName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 60),
    _NtwsApName_Type()
)
ntwsApName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsApName.setStatus("current")
_NtwsApTransition_Type = NtwsApTransition
_NtwsApTransition_Object = MibScalar
ntwsApTransition = _NtwsApTransition_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 61),
    _NtwsApTransition_Type()
)
ntwsApTransition.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsApTransition.setStatus("current")
_NtwsApFailDetail_Type = NtwsApFailDetail
_NtwsApFailDetail_Object = MibScalar
ntwsApFailDetail = _NtwsApFailDetail_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 62),
    _NtwsApFailDetail_Type()
)
ntwsApFailDetail.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsApFailDetail.setStatus("current")
_NtwsRadioType_Type = NtwsRadioType
_NtwsRadioType_Object = MibScalar
ntwsRadioType = _NtwsRadioType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 63),
    _NtwsRadioType_Type()
)
ntwsRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRadioType.setStatus("current")
_NtwsRadioConfigState_Type = NtwsRadioConfigState
_NtwsRadioConfigState_Object = MibScalar
ntwsRadioConfigState = _NtwsRadioConfigState_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 64),
    _NtwsRadioConfigState_Type()
)
ntwsRadioConfigState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRadioConfigState.setStatus("current")
_NtwsApConnectSecurityType_Type = NtwsApConnectSecurityType
_NtwsApConnectSecurityType_Object = MibScalar
ntwsApConnectSecurityType = _NtwsApConnectSecurityType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 65),
    _NtwsApConnectSecurityType_Type()
)
ntwsApConnectSecurityType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsApConnectSecurityType.setStatus("current")
_NtwsApServiceAvailability_Type = NtwsApServiceAvailability
_NtwsApServiceAvailability_Object = MibScalar
ntwsApServiceAvailability = _NtwsApServiceAvailability_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 66),
    _NtwsApServiceAvailability_Type()
)
ntwsApServiceAvailability.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsApServiceAvailability.setStatus("current")
_NtwsApWasOperational_Type = NtwsApWasOperational
_NtwsApWasOperational_Object = MibScalar
ntwsApWasOperational = _NtwsApWasOperational_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 67),
    _NtwsApWasOperational_Type()
)
ntwsApWasOperational.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsApWasOperational.setStatus("current")
_NtwsClientTimeSinceLastRoam_Type = Unsigned32
_NtwsClientTimeSinceLastRoam_Object = MibScalar
ntwsClientTimeSinceLastRoam = _NtwsClientTimeSinceLastRoam_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 68),
    _NtwsClientTimeSinceLastRoam_Type()
)
ntwsClientTimeSinceLastRoam.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientTimeSinceLastRoam.setStatus("current")
_NtwsClientIpAddrChangeReason_Type = NtwsClientIpAddrChangeReason
_NtwsClientIpAddrChangeReason_Object = MibScalar
ntwsClientIpAddrChangeReason = _NtwsClientIpAddrChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 69),
    _NtwsClientIpAddrChangeReason_Type()
)
ntwsClientIpAddrChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientIpAddrChangeReason.setStatus("current")
_NtwsRFDetectRogueAPMacAddr_Type = MacAddress
_NtwsRFDetectRogueAPMacAddr_Object = MibScalar
ntwsRFDetectRogueAPMacAddr = _NtwsRFDetectRogueAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 70),
    _NtwsRFDetectRogueAPMacAddr_Type()
)
ntwsRFDetectRogueAPMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRFDetectRogueAPMacAddr.setStatus("current")
_NtwsBlacklistingRemainingTime_Type = Unsigned32
_NtwsBlacklistingRemainingTime_Object = MibScalar
ntwsBlacklistingRemainingTime = _NtwsBlacklistingRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 71),
    _NtwsBlacklistingRemainingTime_Type()
)
ntwsBlacklistingRemainingTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsBlacklistingRemainingTime.setStatus("current")
_NtwsBlacklistingCause_Type = NtwsBlacklistingCause
_NtwsBlacklistingCause_Object = MibScalar
ntwsBlacklistingCause = _NtwsBlacklistingCause_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 72),
    _NtwsBlacklistingCause_Type()
)
ntwsBlacklistingCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsBlacklistingCause.setStatus("current")
_NtwsNumLicensedActiveAPs_Type = Unsigned32
_NtwsNumLicensedActiveAPs_Object = MibScalar
ntwsNumLicensedActiveAPs = _NtwsNumLicensedActiveAPs_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 73),
    _NtwsNumLicensedActiveAPs_Type()
)
ntwsNumLicensedActiveAPs.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsNumLicensedActiveAPs.setStatus("current")
_NtwsClientDynAuthorClientIp_Type = IpAddress
_NtwsClientDynAuthorClientIp_Object = MibScalar
ntwsClientDynAuthorClientIp = _NtwsClientDynAuthorClientIp_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 74),
    _NtwsClientDynAuthorClientIp_Type()
)
ntwsClientDynAuthorClientIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientDynAuthorClientIp.setStatus("current")
_NtwsChangedUserParamOldValues_Type = NtwsUserAttributeList
_NtwsChangedUserParamOldValues_Object = MibScalar
ntwsChangedUserParamOldValues = _NtwsChangedUserParamOldValues_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 75),
    _NtwsChangedUserParamOldValues_Type()
)
ntwsChangedUserParamOldValues.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsChangedUserParamOldValues.setStatus("current")
_NtwsChangedUserParamNewValues_Type = NtwsUserAttributeList
_NtwsChangedUserParamNewValues_Object = MibScalar
ntwsChangedUserParamNewValues = _NtwsChangedUserParamNewValues_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 76),
    _NtwsChangedUserParamNewValues_Type()
)
ntwsChangedUserParamNewValues.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsChangedUserParamNewValues.setStatus("current")
_NtwsClientDisconnectSource_Type = NtwsSessionDisconnectType
_NtwsClientDisconnectSource_Object = MibScalar
ntwsClientDisconnectSource = _NtwsClientDisconnectSource_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 77),
    _NtwsClientDisconnectSource_Type()
)
ntwsClientDisconnectSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientDisconnectSource.setStatus("current")


class _NtwsClientDisconnectDescription_Type(DisplayString):
    """Custom type ntwsClientDisconnectDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsClientDisconnectDescription_Type.__name__ = "DisplayString"
_NtwsClientDisconnectDescription_Object = MibScalar
ntwsClientDisconnectDescription = _NtwsClientDisconnectDescription_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 78),
    _NtwsClientDisconnectDescription_Type()
)
ntwsClientDisconnectDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientDisconnectDescription.setStatus("current")
_NtwsMobilityDomainSecondarySeedIp_Type = IpAddress
_NtwsMobilityDomainSecondarySeedIp_Object = MibScalar
ntwsMobilityDomainSecondarySeedIp = _NtwsMobilityDomainSecondarySeedIp_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 79),
    _NtwsMobilityDomainSecondarySeedIp_Type()
)
ntwsMobilityDomainSecondarySeedIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsMobilityDomainSecondarySeedIp.setStatus("current")
_NtwsMobilityDomainPrimarySeedIp_Type = IpAddress
_NtwsMobilityDomainPrimarySeedIp_Object = MibScalar
ntwsMobilityDomainPrimarySeedIp = _NtwsMobilityDomainPrimarySeedIp_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 80),
    _NtwsMobilityDomainPrimarySeedIp_Type()
)
ntwsMobilityDomainPrimarySeedIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsMobilityDomainPrimarySeedIp.setStatus("current")
_NtwsRFDetectClassificationReason_Type = NtwsRFDetectClassificationReason
_NtwsRFDetectClassificationReason_Object = MibScalar
ntwsRFDetectClassificationReason = _NtwsRFDetectClassificationReason_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 81),
    _NtwsRFDetectClassificationReason_Type()
)
ntwsRFDetectClassificationReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRFDetectClassificationReason.setStatus("current")


class _NtwsConfigSaveFileName_Type(DisplayString):
    """Custom type ntwsConfigSaveFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsConfigSaveFileName_Type.__name__ = "DisplayString"
_NtwsConfigSaveFileName_Object = MibScalar
ntwsConfigSaveFileName = _NtwsConfigSaveFileName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 82),
    _NtwsConfigSaveFileName_Type()
)
ntwsConfigSaveFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsConfigSaveFileName.setStatus("current")
_NtwsConfigSaveInitiatorType_Type = NtwsConfigSaveInitiatorType
_NtwsConfigSaveInitiatorType_Object = MibScalar
ntwsConfigSaveInitiatorType = _NtwsConfigSaveInitiatorType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 83),
    _NtwsConfigSaveInitiatorType_Type()
)
ntwsConfigSaveInitiatorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsConfigSaveInitiatorType.setStatus("current")
_NtwsConfigSaveInitiatorIp_Type = IpAddress
_NtwsConfigSaveInitiatorIp_Object = MibScalar
ntwsConfigSaveInitiatorIp = _NtwsConfigSaveInitiatorIp_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 84),
    _NtwsConfigSaveInitiatorIp_Type()
)
ntwsConfigSaveInitiatorIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsConfigSaveInitiatorIp.setStatus("current")


class _NtwsConfigSaveInitiatorDetails_Type(DisplayString):
    """Custom type ntwsConfigSaveInitiatorDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsConfigSaveInitiatorDetails_Type.__name__ = "DisplayString"
_NtwsConfigSaveInitiatorDetails_Object = MibScalar
ntwsConfigSaveInitiatorDetails = _NtwsConfigSaveInitiatorDetails_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 85),
    _NtwsConfigSaveInitiatorDetails_Type()
)
ntwsConfigSaveInitiatorDetails.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsConfigSaveInitiatorDetails.setStatus("current")
_NtwsConfigSaveGeneration_Type = Counter32
_NtwsConfigSaveGeneration_Object = MibScalar
ntwsConfigSaveGeneration = _NtwsConfigSaveGeneration_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 86),
    _NtwsConfigSaveGeneration_Type()
)
ntwsConfigSaveGeneration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsConfigSaveGeneration.setStatus("current")
_NtwsApNum_Type = NtwsApNum
_NtwsApNum_Object = MibScalar
ntwsApNum = _NtwsApNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 87),
    _NtwsApNum_Type()
)
ntwsApNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsApNum.setStatus("current")
_NtwsRadioMode_Type = NtwsRadioMode
_NtwsRadioMode_Object = MibScalar
ntwsRadioMode = _NtwsRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 88),
    _NtwsRadioMode_Type()
)
ntwsRadioMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRadioMode.setStatus("current")
_NtwsMichaelMICFailureCause_Type = NtwsMichaelMICFailureCause
_NtwsMichaelMICFailureCause_Object = MibScalar
ntwsMichaelMICFailureCause = _NtwsMichaelMICFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 89),
    _NtwsMichaelMICFailureCause_Type()
)
ntwsMichaelMICFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsMichaelMICFailureCause.setStatus("current")
_NtwsClientAccessMode_Type = NtwsClientAccessMode
_NtwsClientAccessMode_Object = MibScalar
ntwsClientAccessMode = _NtwsClientAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 90),
    _NtwsClientAccessMode_Type()
)
ntwsClientAccessMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientAccessMode.setStatus("current")
_NtwsClientAuthorizationReason_Type = NtwsClientAuthorizationReason
_NtwsClientAuthorizationReason_Object = MibScalar
ntwsClientAuthorizationReason = _NtwsClientAuthorizationReason_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 91),
    _NtwsClientAuthorizationReason_Type()
)
ntwsClientAuthorizationReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientAuthorizationReason.setStatus("current")


class _NtwsPhysPortNum_Type(Unsigned32):
    """Custom type ntwsPhysPortNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_NtwsPhysPortNum_Type.__name__ = "Unsigned32"
_NtwsPhysPortNum_Object = MibScalar
ntwsPhysPortNum = _NtwsPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 92),
    _NtwsPhysPortNum_Type()
)
ntwsPhysPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsPhysPortNum.setStatus("current")
_NtwsApMgrOldIp_Type = IpAddress
_NtwsApMgrOldIp_Object = MibScalar
ntwsApMgrOldIp = _NtwsApMgrOldIp_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 93),
    _NtwsApMgrOldIp_Type()
)
ntwsApMgrOldIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsApMgrOldIp.setStatus("current")
_NtwsApMgrNewIp_Type = IpAddress
_NtwsApMgrNewIp_Object = MibScalar
ntwsApMgrNewIp = _NtwsApMgrNewIp_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 94),
    _NtwsApMgrNewIp_Type()
)
ntwsApMgrNewIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsApMgrNewIp.setStatus("current")
_NtwsApMgrChangeReason_Type = NtwsApMgrChangeReason
_NtwsApMgrChangeReason_Object = MibScalar
ntwsApMgrChangeReason = _NtwsApMgrChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 95),
    _NtwsApMgrChangeReason_Type()
)
ntwsApMgrChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsApMgrChangeReason.setStatus("current")
_NtwsClientClearedReason_Type = NtwsClientClearedReason
_NtwsClientClearedReason_Object = MibScalar
ntwsClientClearedReason = _NtwsClientClearedReason_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 96),
    _NtwsClientClearedReason_Type()
)
ntwsClientClearedReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientClearedReason.setStatus("current")
_NtwsMobilityDomainResiliencyStatus_Type = NtwsMobilityDomainResiliencyStatus
_NtwsMobilityDomainResiliencyStatus_Object = MibScalar
ntwsMobilityDomainResiliencyStatus = _NtwsMobilityDomainResiliencyStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 97),
    _NtwsMobilityDomainResiliencyStatus_Type()
)
ntwsMobilityDomainResiliencyStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsMobilityDomainResiliencyStatus.setStatus("current")
_NtwsClientSessionElapsedSeconds_Type = Unsigned32
_NtwsClientSessionElapsedSeconds_Object = MibScalar
ntwsClientSessionElapsedSeconds = _NtwsClientSessionElapsedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 98),
    _NtwsClientSessionElapsedSeconds_Type()
)
ntwsClientSessionElapsedSeconds.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientSessionElapsedSeconds.setStatus("current")
_NtwsRadioChannelWidth_Type = NtwsRadioChannelWidth
_NtwsRadioChannelWidth_Object = MibScalar
ntwsRadioChannelWidth = _NtwsRadioChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 99),
    _NtwsRadioChannelWidth_Type()
)
ntwsRadioChannelWidth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRadioChannelWidth.setStatus("current")
_NtwsRadioMimoState_Type = NtwsRadioMimoState
_NtwsRadioMimoState_Object = MibScalar
ntwsRadioMimoState = _NtwsRadioMimoState_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 100),
    _NtwsRadioMimoState_Type()
)
ntwsRadioMimoState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRadioMimoState.setStatus("current")
_NtwsClientRadioType_Type = NtwsRadioType
_NtwsClientRadioType_Object = MibScalar
ntwsClientRadioType = _NtwsClientRadioType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 101),
    _NtwsClientRadioType_Type()
)
ntwsClientRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClientRadioType.setStatus("current")
_NtwsRFDetectXmtrRadioType_Type = NtwsRadioType
_NtwsRFDetectXmtrRadioType_Object = MibScalar
ntwsRFDetectXmtrRadioType = _NtwsRFDetectXmtrRadioType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 102),
    _NtwsRFDetectXmtrRadioType_Type()
)
ntwsRFDetectXmtrRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRFDetectXmtrRadioType.setStatus("current")
_NtwsRFDetectXmtrCryptoType_Type = NtwsCryptoType
_NtwsRFDetectXmtrCryptoType_Object = MibScalar
ntwsRFDetectXmtrCryptoType = _NtwsRFDetectXmtrCryptoType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 103),
    _NtwsRFDetectXmtrCryptoType_Type()
)
ntwsRFDetectXmtrCryptoType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsRFDetectXmtrCryptoType.setStatus("current")
_NtwsClusterFailureReason_Type = NtwsClusterFailureReason
_NtwsClusterFailureReason_Object = MibScalar
ntwsClusterFailureReason = _NtwsClusterFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 104),
    _NtwsClusterFailureReason_Type()
)
ntwsClusterFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClusterFailureReason.setStatus("current")


class _NtwsClusterFailureDescription_Type(DisplayString):
    """Custom type ntwsClusterFailureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsClusterFailureDescription_Type.__name__ = "DisplayString"
_NtwsClusterFailureDescription_Object = MibScalar
ntwsClusterFailureDescription = _NtwsClusterFailureDescription_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2, 105),
    _NtwsClusterFailureDescription_Type()
)
ntwsClusterFailureDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntwsClusterFailureDescription.setStatus("current")
_NtwsTrapsV2_ObjectIdentity = ObjectIdentity
ntwsTrapsV2 = _NtwsTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0)
)

# Managed Objects groups


# Notification objects

ntwsDeviceFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 1)
)
ntwsDeviceFailTrap.setObjects(
    ("NTWS-TRAP-MIB", "ntwsDeviceId")
)
if mibBuilder.loadTexts:
    ntwsDeviceFailTrap.setStatus(
        "current"
    )

ntwsDeviceOkayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 2)
)
ntwsDeviceOkayTrap.setObjects(
    ("NTWS-TRAP-MIB", "ntwsDeviceId")
)
if mibBuilder.loadTexts:
    ntwsDeviceOkayTrap.setStatus(
        "current"
    )

ntwsPoEFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 3)
)
ntwsPoEFailTrap.setObjects(
    ("NTWS-TRAP-MIB", "ntwsPortNum")
)
if mibBuilder.loadTexts:
    ntwsPoEFailTrap.setStatus(
        "current"
    )

ntwsApTimeoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 4)
)
ntwsApTimeoutTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsAPAccessType"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"))
)
if mibBuilder.loadTexts:
    ntwsApTimeoutTrap.setStatus(
        "obsolete"
    )

ntwsAPBootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 5)
)
ntwsAPBootTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsAPAccessType"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"))
)
if mibBuilder.loadTexts:
    ntwsAPBootTrap.setStatus(
        "obsolete"
    )

ntwsMobilityDomainJoinTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 6)
)
ntwsMobilityDomainJoinTrap.setObjects(
    ("NTWS-TRAP-MIB", "ntwsMobilityDomainIp")
)
if mibBuilder.loadTexts:
    ntwsMobilityDomainJoinTrap.setStatus(
        "current"
    )

ntwsMobilityDomainTimeoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 7)
)
ntwsMobilityDomainTimeoutTrap.setObjects(
    ("NTWS-TRAP-MIB", "ntwsMobilityDomainIp")
)
if mibBuilder.loadTexts:
    ntwsMobilityDomainTimeoutTrap.setStatus(
        "current"
    )

ntwsMpMichaelMICFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 8)
)
ntwsMpMichaelMICFailure.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"))
)
if mibBuilder.loadTexts:
    ntwsMpMichaelMICFailure.setStatus(
        "obsolete"
    )

ntwsRFDetectRogueAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 9)
)
ntwsRFDetectRogueAPTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectRogueAPTrap.setStatus(
        "obsolete"
    )

ntwsRFDetectAdhocUserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 10)
)
ntwsRFDetectAdhocUserTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectAdhocUserTrap.setStatus(
        "current"
    )

ntwsRFDetectRogueDisappearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 11)
)
ntwsRFDetectRogueDisappearTrap.setObjects(
    ("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr")
)
if mibBuilder.loadTexts:
    ntwsRFDetectRogueDisappearTrap.setStatus(
        "obsolete"
    )

ntwsClientAuthenticationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 12)
)
ntwsClientAuthenticationFailureTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsUserName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionId"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthServerIp"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthenProtocolType"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthenticationFailureCause"),
        ("NTWS-TRAP-MIB", "ntwsClientFailureCauseDescription"))
)
if mibBuilder.loadTexts:
    ntwsClientAuthenticationFailureTrap.setStatus(
        "current"
    )

ntwsClientAuthorizationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 13)
)
ntwsClientAuthorizationFailureTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsUserName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionId"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthServerIp"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthenProtocolType"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"),
        ("NTWS-TRAP-MIB", "ntwsClientLocationPolicyIndex"),
        ("NTWS-TRAP-MIB", "ntwsUserParams"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthorizationFailureCause"),
        ("NTWS-TRAP-MIB", "ntwsClientFailureCauseDescription"))
)
if mibBuilder.loadTexts:
    ntwsClientAuthorizationFailureTrap.setStatus(
        "current"
    )

ntwsClientAssociationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 14)
)
ntwsClientAssociationFailureTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"),
        ("NTWS-TRAP-MIB", "ntwsClientAssociationFailureCause"),
        ("NTWS-TRAP-MIB", "ntwsClientFailureCauseDescription"))
)
if mibBuilder.loadTexts:
    ntwsClientAssociationFailureTrap.setStatus(
        "current"
    )

ntwsClientAuthorizationSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 15)
)
ntwsClientAuthorizationSuccessTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsUserName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionId"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientIp"),
        ("NTWS-TRAP-MIB", "ntwsClientVLANName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionState"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionStartTime"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthServerIp"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthenProtocolType"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"),
        ("NTWS-TRAP-MIB", "ntwsRadioRssi"))
)
if mibBuilder.loadTexts:
    ntwsClientAuthorizationSuccessTrap.setStatus(
        "obsolete"
    )

ntwsClientDeAssociationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 16)
)
ntwsClientDeAssociationTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsUserName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionId"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientIp"),
        ("NTWS-TRAP-MIB", "ntwsClientVLANName"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthServerIp"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthenProtocolType"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"))
)
if mibBuilder.loadTexts:
    ntwsClientDeAssociationTrap.setStatus(
        "current"
    )

ntwsClientRoamingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 17)
)
ntwsClientRoamingTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsUserName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionId"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientIp"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"),
        ("NTWS-TRAP-MIB", "ntwsClientRoamedFromAccessType"),
        ("NTWS-TRAP-MIB", "ntwsClientRoamedFromPortNum"),
        ("NTWS-TRAP-MIB", "ntwsClientRoamedFromRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsClientRoamedFromDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsClientRoamedFromWsIp"),
        ("NTWS-TRAP-MIB", "ntwsClientTimeSinceLastRoam"))
)
if mibBuilder.loadTexts:
    ntwsClientRoamingTrap.setStatus(
        "current"
    )

ntwsAutoTuneRadioPowerChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 18)
)
ntwsAutoTuneRadioPowerChangeTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRadioMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsNewPowerLevel"),
        ("NTWS-TRAP-MIB", "ntwsOldPowerLevel"),
        ("NTWS-TRAP-MIB", "ntwsRadioPowerChangeReason"),
        ("NTWS-TRAP-MIB", "ntwsRadioPowerChangeDescription"))
)
if mibBuilder.loadTexts:
    ntwsAutoTuneRadioPowerChangeTrap.setStatus(
        "current"
    )

ntwsAutoTuneRadioChannelChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 19)
)
ntwsAutoTuneRadioChannelChangeTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRadioMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsNewChannelNum"),
        ("NTWS-TRAP-MIB", "ntwsOldChannelNum"),
        ("NTWS-TRAP-MIB", "ntwsChannelChangeReason"))
)
if mibBuilder.loadTexts:
    ntwsAutoTuneRadioChannelChangeTrap.setStatus(
        "current"
    )

ntwsCounterMeasureStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 20)
)
ntwsCounterMeasureStartTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRadioMACAddress"))
)
if mibBuilder.loadTexts:
    ntwsCounterMeasureStartTrap.setStatus(
        "current"
    )

ntwsCounterMeasureStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 21)
)
ntwsCounterMeasureStopTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRadioMACAddress"))
)
if mibBuilder.loadTexts:
    ntwsCounterMeasureStopTrap.setStatus(
        "current"
    )

ntwsClientDot1xFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 22)
)
ntwsClientDot1xFailureTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsUserName"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthenProtocolType"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"),
        ("NTWS-TRAP-MIB", "ntwsClientDot1xState"),
        ("NTWS-TRAP-MIB", "ntwsClientDot1xFailureCause"),
        ("NTWS-TRAP-MIB", "ntwsClientFailureCauseDescription"))
)
if mibBuilder.loadTexts:
    ntwsClientDot1xFailureTrap.setStatus(
        "current"
    )

ntwsClientClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 23)
)
ntwsClientClearedTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsUserName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionId"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientIp"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionElapsedTime"),
        ("NTWS-TRAP-MIB", "ntwsLocalId"))
)
if mibBuilder.loadTexts:
    ntwsClientClearedTrap.setStatus(
        "obsolete"
    )

ntwsClientAuthorizationSuccessTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 24)
)
ntwsClientAuthorizationSuccessTrap2.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsUserName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionId"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientIp"),
        ("NTWS-TRAP-MIB", "ntwsClientVLANName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionState"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionStartTime"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthServerIp"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthenProtocolType"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"),
        ("NTWS-TRAP-MIB", "ntwsUserAccessType"),
        ("NTWS-TRAP-MIB", "ntwsLocalId"))
)
if mibBuilder.loadTexts:
    ntwsClientAuthorizationSuccessTrap2.setStatus(
        "obsolete"
    )

ntwsRFDetectSpoofedMacAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 25)
)
ntwsRFDetectSpoofedMacAPTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectSpoofedMacAPTrap.setStatus(
        "obsolete"
    )

ntwsRFDetectSpoofedSsidAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 26)
)
ntwsRFDetectSpoofedSsidAPTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectSpoofedSsidAPTrap.setStatus(
        "obsolete"
    )

ntwsRFDetectDoSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 27)
)
ntwsRFDetectDoSTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRFDetectDoSType"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectDoSTrap.setStatus(
        "current"
    )

ntwsRFDetectClientViaRogueWiredAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 28)
)
ntwsRFDetectClientViaRogueWiredAPTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsSourceWsIp"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsClientVLANid"),
        ("NTWS-TRAP-MIB", "ntwsClientVLANtag"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectClientViaRogueWiredAPTrap.setStatus(
        "obsolete"
    )

ntwsRFDetectInterferingRogueAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 29)
)
ntwsRFDetectInterferingRogueAPTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectInterferingRogueAPTrap.setStatus(
        "obsolete"
    )

ntwsRFDetectInterferingRogueDisappearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 30)
)
ntwsRFDetectInterferingRogueDisappearTrap.setObjects(
    ("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr")
)
if mibBuilder.loadTexts:
    ntwsRFDetectInterferingRogueDisappearTrap.setStatus(
        "obsolete"
    )

ntwsRFDetectUnAuthorizedSsidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 31)
)
ntwsRFDetectUnAuthorizedSsidTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectUnAuthorizedSsidTrap.setStatus(
        "obsolete"
    )

ntwsRFDetectUnAuthorizedOuiTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 32)
)
ntwsRFDetectUnAuthorizedOuiTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectUnAuthorizedOuiTrap.setStatus(
        "obsolete"
    )

ntwsRFDetectUnAuthorizedAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 33)
)
ntwsRFDetectUnAuthorizedAPTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectListenerListInfo"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectUnAuthorizedAPTrap.setStatus(
        "obsolete"
    )

ntwsDAPConnectWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 34)
)
ntwsDAPConnectWarningTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsDeviceModel"),
        ("NTWS-TRAP-MIB", "ntwsDeviceSerNum"),
        ("NTWS-TRAP-MIB", "ntwsRsaPubKeyFingerPrint"),
        ("NTWS-TRAP-MIB", "ntwsDAPconnectWarningType"))
)
if mibBuilder.loadTexts:
    ntwsDAPConnectWarningTrap.setStatus(
        "obsolete"
    )

ntwsRFDetectDoSPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 35)
)
ntwsRFDetectDoSPortTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRFDetectDoSType"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectDoSPortTrap.setStatus(
        "current"
    )

ntwsMpMichaelMICFailure2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 36)
)
ntwsMpMichaelMICFailure2.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress2"))
)
if mibBuilder.loadTexts:
    ntwsMpMichaelMICFailure2.setStatus(
        "obsolete"
    )

ntwsApNonOperStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 37)
)
ntwsApNonOperStatusTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsDeviceSerNum"),
        ("NTWS-TRAP-MIB", "ntwsAPMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsApAttachType"),
        ("NTWS-TRAP-MIB", "ntwsApPortOrDapNum"),
        ("NTWS-TRAP-MIB", "ntwsApName"),
        ("NTWS-TRAP-MIB", "ntwsApTransition"),
        ("NTWS-TRAP-MIB", "ntwsApFailDetail"),
        ("NTWS-TRAP-MIB", "ntwsApWasOperational"))
)
if mibBuilder.loadTexts:
    ntwsApNonOperStatusTrap.setStatus(
        "obsolete"
    )

ntwsApOperRadioStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 38)
)
ntwsApOperRadioStatusTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsDeviceSerNum"),
        ("NTWS-TRAP-MIB", "ntwsApAttachType"),
        ("NTWS-TRAP-MIB", "ntwsApPortOrDapNum"),
        ("NTWS-TRAP-MIB", "ntwsApName"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsRadioType"),
        ("NTWS-TRAP-MIB", "ntwsRadioConfigState"),
        ("NTWS-TRAP-MIB", "ntwsApConnectSecurityType"),
        ("NTWS-TRAP-MIB", "ntwsApServiceAvailability"))
)
if mibBuilder.loadTexts:
    ntwsApOperRadioStatusTrap.setStatus(
        "obsolete"
    )

ntwsClientIpAddrChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 39)
)
ntwsClientIpAddrChangeTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsUserName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionId"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientIp"),
        ("NTWS-TRAP-MIB", "ntwsClientVLANName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionState"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthServerIp"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthenProtocolType"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"),
        ("NTWS-TRAP-MIB", "ntwsUserAccessType"),
        ("NTWS-TRAP-MIB", "ntwsLocalId"),
        ("NTWS-TRAP-MIB", "ntwsClientIpAddrChangeReason"))
)
if mibBuilder.loadTexts:
    ntwsClientIpAddrChangeTrap.setStatus(
        "current"
    )

ntwsClientAssociationSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 40)
)
ntwsClientAssociationSuccessTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"))
)
if mibBuilder.loadTexts:
    ntwsClientAssociationSuccessTrap.setStatus(
        "current"
    )

ntwsClientAuthenticationSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 41)
)
ntwsClientAuthenticationSuccessTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"))
)
if mibBuilder.loadTexts:
    ntwsClientAuthenticationSuccessTrap.setStatus(
        "current"
    )

ntwsClientDeAuthenticationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 42)
)
ntwsClientDeAuthenticationTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsUserName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionId"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientIp"),
        ("NTWS-TRAP-MIB", "ntwsClientVLANName"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthServerIp"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthenProtocolType"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"))
)
if mibBuilder.loadTexts:
    ntwsClientDeAuthenticationTrap.setStatus(
        "current"
    )

ntwsRFDetectBlacklistedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 43)
)
ntwsRFDetectBlacklistedTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsBlacklistingRemainingTime"),
        ("NTWS-TRAP-MIB", "ntwsBlacklistingCause"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectBlacklistedTrap.setStatus(
        "current"
    )

ntwsRFDetectClientViaRogueWiredAPTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 44)
)
ntwsRFDetectClientViaRogueWiredAPTrap2.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsSourceWsIp"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsClientVLANid"),
        ("NTWS-TRAP-MIB", "ntwsClientVLANtag"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectListenerListInfo"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectRogueAPMacAddr"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectClientViaRogueWiredAPTrap2.setStatus(
        "obsolete"
    )

ntwsRFDetectAdhocUserDisappearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 45)
)
ntwsRFDetectAdhocUserDisappearTrap.setObjects(
    ("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr")
)
if mibBuilder.loadTexts:
    ntwsRFDetectAdhocUserDisappearTrap.setStatus(
        "current"
    )

ntwsApRejectLicenseExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 46)
)
ntwsApRejectLicenseExceededTrap.setObjects(
    ("NTWS-TRAP-MIB", "ntwsNumLicensedActiveAPs")
)
if mibBuilder.loadTexts:
    ntwsApRejectLicenseExceededTrap.setStatus(
        "current"
    )

ntwsClientDynAuthorChangeSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 47)
)
ntwsClientDynAuthorChangeSuccessTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsUserName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionId"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientIp"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionState"),
        ("NTWS-TRAP-MIB", "ntwsClientDynAuthorClientIp"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthenProtocolType"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"),
        ("NTWS-TRAP-MIB", "ntwsUserAccessType"),
        ("NTWS-TRAP-MIB", "ntwsLocalId"),
        ("NTWS-TRAP-MIB", "ntwsChangedUserParamOldValues"),
        ("NTWS-TRAP-MIB", "ntwsChangedUserParamNewValues"))
)
if mibBuilder.loadTexts:
    ntwsClientDynAuthorChangeSuccessTrap.setStatus(
        "current"
    )

ntwsClientDynAuthorChangeFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 48)
)
ntwsClientDynAuthorChangeFailureTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsUserName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionId"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientDynAuthorClientIp"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthenProtocolType"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"),
        ("NTWS-TRAP-MIB", "ntwsUserParams"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthorizationFailureCause"),
        ("NTWS-TRAP-MIB", "ntwsClientFailureCauseDescription"))
)
if mibBuilder.loadTexts:
    ntwsClientDynAuthorChangeFailureTrap.setStatus(
        "current"
    )

ntwsClientDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 49)
)
ntwsClientDisconnectTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsUserName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionId"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientIp"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessType"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsDAPNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"),
        ("NTWS-TRAP-MIB", "ntwsLocalId"),
        ("NTWS-TRAP-MIB", "ntwsClientDisconnectSource"),
        ("NTWS-TRAP-MIB", "ntwsClientDisconnectDescription"))
)
if mibBuilder.loadTexts:
    ntwsClientDisconnectTrap.setStatus(
        "current"
    )

ntwsMobilityDomainFailOverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 50)
)
ntwsMobilityDomainFailOverTrap.setObjects(
    ("NTWS-TRAP-MIB", "ntwsMobilityDomainSecondarySeedIp")
)
if mibBuilder.loadTexts:
    ntwsMobilityDomainFailOverTrap.setStatus(
        "current"
    )

ntwsMobilityDomainFailBackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 51)
)
ntwsMobilityDomainFailBackTrap.setObjects(
    ("NTWS-TRAP-MIB", "ntwsMobilityDomainPrimarySeedIp")
)
if mibBuilder.loadTexts:
    ntwsMobilityDomainFailBackTrap.setStatus(
        "current"
    )

ntwsRFDetectRogueDeviceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 52)
)
ntwsRFDetectRogueDeviceTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectListenerListInfo"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectClassificationReason"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectRogueDeviceTrap.setStatus(
        "obsolete"
    )

ntwsRFDetectRogueDeviceDisappearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 53)
)
ntwsRFDetectRogueDeviceDisappearTrap.setObjects(
    ("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr")
)
if mibBuilder.loadTexts:
    ntwsRFDetectRogueDeviceDisappearTrap.setStatus(
        "current"
    )

ntwsRFDetectSuspectDeviceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 54)
)
ntwsRFDetectSuspectDeviceTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectListenerListInfo"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectClassificationReason"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectSuspectDeviceTrap.setStatus(
        "obsolete"
    )

ntwsRFDetectSuspectDeviceDisappearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 55)
)
ntwsRFDetectSuspectDeviceDisappearTrap.setObjects(
    ("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr")
)
if mibBuilder.loadTexts:
    ntwsRFDetectSuspectDeviceDisappearTrap.setStatus(
        "current"
    )

ntwsRFDetectClientViaRogueWiredAPTrap3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 56)
)
ntwsRFDetectClientViaRogueWiredAPTrap3.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsSourceWsIp"),
        ("NTWS-TRAP-MIB", "ntwsPortNum"),
        ("NTWS-TRAP-MIB", "ntwsClientVLANid"),
        ("NTWS-TRAP-MIB", "ntwsClientVLANtag"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectListenerListInfo"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectRogueAPMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectClassificationReason"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectClientViaRogueWiredAPTrap3.setStatus(
        "current"
    )

ntwsRFDetectClassificationChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 57)
)
if mibBuilder.loadTexts:
    ntwsRFDetectClassificationChangeTrap.setStatus(
        "current"
    )

ntwsConfigurationSavedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 58)
)
ntwsConfigurationSavedTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsConfigSaveFileName"),
        ("NTWS-TRAP-MIB", "ntwsConfigSaveInitiatorType"),
        ("NTWS-TRAP-MIB", "ntwsConfigSaveInitiatorIp"),
        ("NTWS-TRAP-MIB", "ntwsConfigSaveInitiatorDetails"),
        ("NTWS-TRAP-MIB", "ntwsConfigSaveGeneration"))
)
if mibBuilder.loadTexts:
    ntwsConfigurationSavedTrap.setStatus(
        "current"
    )

ntwsApNonOperStatusTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 59)
)
ntwsApNonOperStatusTrap2.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsDeviceSerNum"),
        ("NTWS-TRAP-MIB", "ntwsAPMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsApNum"),
        ("NTWS-TRAP-MIB", "ntwsApName"),
        ("NTWS-TRAP-MIB", "ntwsApTransition"),
        ("NTWS-TRAP-MIB", "ntwsApFailDetail"),
        ("NTWS-TRAP-MIB", "ntwsApWasOperational"))
)
if mibBuilder.loadTexts:
    ntwsApNonOperStatusTrap2.setStatus(
        "current"
    )

ntwsApOperRadioStatusTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 60)
)
ntwsApOperRadioStatusTrap2.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsDeviceSerNum"),
        ("NTWS-TRAP-MIB", "ntwsApNum"),
        ("NTWS-TRAP-MIB", "ntwsApName"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsRadioType"),
        ("NTWS-TRAP-MIB", "ntwsRadioMode"),
        ("NTWS-TRAP-MIB", "ntwsRadioConfigState"),
        ("NTWS-TRAP-MIB", "ntwsApConnectSecurityType"),
        ("NTWS-TRAP-MIB", "ntwsApServiceAvailability"))
)
if mibBuilder.loadTexts:
    ntwsApOperRadioStatusTrap2.setStatus(
        "obsolete"
    )

ntwsMichaelMICFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 61)
)
ntwsMichaelMICFailure.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsApNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsMichaelMICFailureCause"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress2"))
)
if mibBuilder.loadTexts:
    ntwsMichaelMICFailure.setStatus(
        "current"
    )

ntwsClientAuthorizationSuccessTrap3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 62)
)
ntwsClientAuthorizationSuccessTrap3.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsUserName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionId"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientIp"),
        ("NTWS-TRAP-MIB", "ntwsClientVLANName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionState"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthServerIp"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthenProtocolType"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessMode"),
        ("NTWS-TRAP-MIB", "ntwsPhysPortNum"),
        ("NTWS-TRAP-MIB", "ntwsApNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"),
        ("NTWS-TRAP-MIB", "ntwsUserAccessType"),
        ("NTWS-TRAP-MIB", "ntwsLocalId"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthorizationReason"))
)
if mibBuilder.loadTexts:
    ntwsClientAuthorizationSuccessTrap3.setStatus(
        "obsolete"
    )

ntwsApManagerChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 63)
)
ntwsApManagerChangeTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsDeviceSerNum"),
        ("NTWS-TRAP-MIB", "ntwsAPMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsApNum"),
        ("NTWS-TRAP-MIB", "ntwsApName"),
        ("NTWS-TRAP-MIB", "ntwsApMgrOldIp"),
        ("NTWS-TRAP-MIB", "ntwsApMgrNewIp"),
        ("NTWS-TRAP-MIB", "ntwsApMgrChangeReason"))
)
if mibBuilder.loadTexts:
    ntwsApManagerChangeTrap.setStatus(
        "current"
    )

ntwsClientClearedTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 64)
)
ntwsClientClearedTrap2.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsUserName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionId"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientIp"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessMode"),
        ("NTWS-TRAP-MIB", "ntwsPhysPortNum"),
        ("NTWS-TRAP-MIB", "ntwsApNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionElapsedSeconds"),
        ("NTWS-TRAP-MIB", "ntwsLocalId"),
        ("NTWS-TRAP-MIB", "ntwsClientClearedReason"))
)
if mibBuilder.loadTexts:
    ntwsClientClearedTrap2.setStatus(
        "current"
    )

ntwsMobilityDomainResiliencyStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 65)
)
ntwsMobilityDomainResiliencyStatusTrap.setObjects(
    ("NTWS-TRAP-MIB", "ntwsMobilityDomainResiliencyStatus")
)
if mibBuilder.loadTexts:
    ntwsMobilityDomainResiliencyStatusTrap.setStatus(
        "current"
    )

ntwsApOperRadioStatusTrap3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 66)
)
ntwsApOperRadioStatusTrap3.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsDeviceSerNum"),
        ("NTWS-TRAP-MIB", "ntwsApNum"),
        ("NTWS-TRAP-MIB", "ntwsApName"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsRadioType"),
        ("NTWS-TRAP-MIB", "ntwsRadioMode"),
        ("NTWS-TRAP-MIB", "ntwsRadioConfigState"),
        ("NTWS-TRAP-MIB", "ntwsRadioChannelWidth"),
        ("NTWS-TRAP-MIB", "ntwsRadioMimoState"),
        ("NTWS-TRAP-MIB", "ntwsApConnectSecurityType"),
        ("NTWS-TRAP-MIB", "ntwsApServiceAvailability"))
)
if mibBuilder.loadTexts:
    ntwsApOperRadioStatusTrap3.setStatus(
        "current"
    )

ntwsClientAuthorizationSuccessTrap4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 67)
)
ntwsClientAuthorizationSuccessTrap4.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsUserName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionId"),
        ("NTWS-TRAP-MIB", "ntwsClientMACAddress"),
        ("NTWS-TRAP-MIB", "ntwsClientIp"),
        ("NTWS-TRAP-MIB", "ntwsClientVLANName"),
        ("NTWS-TRAP-MIB", "ntwsClientSessionState"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthServerIp"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthenProtocolType"),
        ("NTWS-TRAP-MIB", "ntwsClientAccessMode"),
        ("NTWS-TRAP-MIB", "ntwsPhysPortNum"),
        ("NTWS-TRAP-MIB", "ntwsApNum"),
        ("NTWS-TRAP-MIB", "ntwsAPRadioNum"),
        ("NTWS-TRAP-MIB", "ntwsRadioSSID"),
        ("NTWS-TRAP-MIB", "ntwsClientRadioType"),
        ("NTWS-TRAP-MIB", "ntwsUserAccessType"),
        ("NTWS-TRAP-MIB", "ntwsLocalId"),
        ("NTWS-TRAP-MIB", "ntwsClientAuthorizationReason"))
)
if mibBuilder.loadTexts:
    ntwsClientAuthorizationSuccessTrap4.setStatus(
        "current"
    )

ntwsRFDetectRogueDeviceTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 68)
)
ntwsRFDetectRogueDeviceTrap2.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectXmtrRadioType"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectXmtrCryptoType"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectListenerListInfo"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectClassificationReason"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectRogueDeviceTrap2.setStatus(
        "current"
    )

ntwsRFDetectSuspectDeviceTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 69)
)
ntwsRFDetectSuspectDeviceTrap2.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsRFDetectXmtrMacAddr"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectXmtrRadioType"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectXmtrCryptoType"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectListenerListInfo"),
        ("NTWS-TRAP-MIB", "ntwsRFDetectClassificationReason"))
)
if mibBuilder.loadTexts:
    ntwsRFDetectSuspectDeviceTrap2.setStatus(
        "current"
    )

ntwsClusterFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5, 0, 70)
)
ntwsClusterFailureTrap.setObjects(
      *(("NTWS-TRAP-MIB", "ntwsClusterFailureReason"),
        ("NTWS-TRAP-MIB", "ntwsClusterFailureDescription"))
)
if mibBuilder.loadTexts:
    ntwsClusterFailureTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTWS-TRAP-MIB",
    **{"NtwsAssociationFailureType": NtwsAssociationFailureType,
       "NtwsAuthenticationFailureType": NtwsAuthenticationFailureType,
       "NtwsAuthorizationFailureType": NtwsAuthorizationFailureType,
       "NtwsDot1xFailureType": NtwsDot1xFailureType,
       "NtwsRFDetectDoSType": NtwsRFDetectDoSType,
       "NtwsClientIpAddrChangeReason": NtwsClientIpAddrChangeReason,
       "NtwsBlacklistingCause": NtwsBlacklistingCause,
       "NtwsUserAttributeList": NtwsUserAttributeList,
       "NtwsSessionDisconnectType": NtwsSessionDisconnectType,
       "NtwsConfigSaveInitiatorType": NtwsConfigSaveInitiatorType,
       "NtwsMichaelMICFailureCause": NtwsMichaelMICFailureCause,
       "NtwsClientAuthorizationReason": NtwsClientAuthorizationReason,
       "NtwsApMgrChangeReason": NtwsApMgrChangeReason,
       "NtwsClientClearedReason": NtwsClientClearedReason,
       "NtwsMobilityDomainResiliencyStatus": NtwsMobilityDomainResiliencyStatus,
       "NtwsClusterFailureReason": NtwsClusterFailureReason,
       "ntwsDeviceId": ntwsDeviceId,
       "ntwsMobilityDomainIp": ntwsMobilityDomainIp,
       "ntwsAPMACAddress": ntwsAPMACAddress,
       "ntwsClientMACAddress": ntwsClientMACAddress,
       "ntwsRFDetectXmtrMacAddr": ntwsRFDetectXmtrMacAddr,
       "ntwsPortNum": ntwsPortNum,
       "ntwsAPRadioNum": ntwsAPRadioNum,
       "ntwsRadioRssi": ntwsRadioRssi,
       "ntwsRadioBSSID": ntwsRadioBSSID,
       "ntwsUserName": ntwsUserName,
       "ntwsClientAuthServerIp": ntwsClientAuthServerIp,
       "ntwsClientSessionState": ntwsClientSessionState,
       "ntwsDAPNum": ntwsDAPNum,
       "ntwsClientIp": ntwsClientIp,
       "ntwsClientSessionId": ntwsClientSessionId,
       "ntwsClientAuthenProtocolType": ntwsClientAuthenProtocolType,
       "ntwsClientVLANName": ntwsClientVLANName,
       "ntwsClientSessionStartTime": ntwsClientSessionStartTime,
       "ntwsClientFailureCause": ntwsClientFailureCause,
       "ntwsClientRoamedFromPortNum": ntwsClientRoamedFromPortNum,
       "ntwsClientRoamedFromRadioNum": ntwsClientRoamedFromRadioNum,
       "ntwsClientRoamedFromDAPNum": ntwsClientRoamedFromDAPNum,
       "ntwsUserParams": ntwsUserParams,
       "ntwsClientLocationPolicyIndex": ntwsClientLocationPolicyIndex,
       "ntwsClientAssociationFailureCause": ntwsClientAssociationFailureCause,
       "ntwsClientAuthenticationFailureCause": ntwsClientAuthenticationFailureCause,
       "ntwsClientAuthorizationFailureCause": ntwsClientAuthorizationFailureCause,
       "ntwsClientFailureCauseDescription": ntwsClientFailureCauseDescription,
       "ntwsClientRoamedFromWsIp": ntwsClientRoamedFromWsIp,
       "ntwsClientRoamedFromAccessType": ntwsClientRoamedFromAccessType,
       "ntwsClientAccessType": ntwsClientAccessType,
       "ntwsRadioMACAddress": ntwsRadioMACAddress,
       "ntwsRadioPowerChangeReason": ntwsRadioPowerChangeReason,
       "ntwsNewChannelNum": ntwsNewChannelNum,
       "ntwsOldChannelNum": ntwsOldChannelNum,
       "ntwsChannelChangeReason": ntwsChannelChangeReason,
       "ntwsRFDetectListenerListInfo": ntwsRFDetectListenerListInfo,
       "ntwsRadioSSID": ntwsRadioSSID,
       "ntwsNewPowerLevel": ntwsNewPowerLevel,
       "ntwsOldPowerLevel": ntwsOldPowerLevel,
       "ntwsRadioPowerChangeDescription": ntwsRadioPowerChangeDescription,
       "ntwsCounterMeasurePerformerListInfo": ntwsCounterMeasurePerformerListInfo,
       "ntwsClientDot1xState": ntwsClientDot1xState,
       "ntwsClientDot1xFailureCause": ntwsClientDot1xFailureCause,
       "ntwsAPAccessType": ntwsAPAccessType,
       "ntwsUserAccessType": ntwsUserAccessType,
       "ntwsClientSessionElapsedTime": ntwsClientSessionElapsedTime,
       "ntwsLocalId": ntwsLocalId,
       "ntwsRFDetectDoSType": ntwsRFDetectDoSType,
       "ntwsSourceWsIp": ntwsSourceWsIp,
       "ntwsClientVLANid": ntwsClientVLANid,
       "ntwsClientVLANtag": ntwsClientVLANtag,
       "ntwsDeviceModel": ntwsDeviceModel,
       "ntwsDeviceSerNum": ntwsDeviceSerNum,
       "ntwsRsaPubKeyFingerPrint": ntwsRsaPubKeyFingerPrint,
       "ntwsDAPconnectWarningType": ntwsDAPconnectWarningType,
       "ntwsClientMACAddress2": ntwsClientMACAddress2,
       "ntwsApAttachType": ntwsApAttachType,
       "ntwsApPortOrDapNum": ntwsApPortOrDapNum,
       "ntwsApName": ntwsApName,
       "ntwsApTransition": ntwsApTransition,
       "ntwsApFailDetail": ntwsApFailDetail,
       "ntwsRadioType": ntwsRadioType,
       "ntwsRadioConfigState": ntwsRadioConfigState,
       "ntwsApConnectSecurityType": ntwsApConnectSecurityType,
       "ntwsApServiceAvailability": ntwsApServiceAvailability,
       "ntwsApWasOperational": ntwsApWasOperational,
       "ntwsClientTimeSinceLastRoam": ntwsClientTimeSinceLastRoam,
       "ntwsClientIpAddrChangeReason": ntwsClientIpAddrChangeReason,
       "ntwsRFDetectRogueAPMacAddr": ntwsRFDetectRogueAPMacAddr,
       "ntwsBlacklistingRemainingTime": ntwsBlacklistingRemainingTime,
       "ntwsBlacklistingCause": ntwsBlacklistingCause,
       "ntwsNumLicensedActiveAPs": ntwsNumLicensedActiveAPs,
       "ntwsClientDynAuthorClientIp": ntwsClientDynAuthorClientIp,
       "ntwsChangedUserParamOldValues": ntwsChangedUserParamOldValues,
       "ntwsChangedUserParamNewValues": ntwsChangedUserParamNewValues,
       "ntwsClientDisconnectSource": ntwsClientDisconnectSource,
       "ntwsClientDisconnectDescription": ntwsClientDisconnectDescription,
       "ntwsMobilityDomainSecondarySeedIp": ntwsMobilityDomainSecondarySeedIp,
       "ntwsMobilityDomainPrimarySeedIp": ntwsMobilityDomainPrimarySeedIp,
       "ntwsRFDetectClassificationReason": ntwsRFDetectClassificationReason,
       "ntwsConfigSaveFileName": ntwsConfigSaveFileName,
       "ntwsConfigSaveInitiatorType": ntwsConfigSaveInitiatorType,
       "ntwsConfigSaveInitiatorIp": ntwsConfigSaveInitiatorIp,
       "ntwsConfigSaveInitiatorDetails": ntwsConfigSaveInitiatorDetails,
       "ntwsConfigSaveGeneration": ntwsConfigSaveGeneration,
       "ntwsApNum": ntwsApNum,
       "ntwsRadioMode": ntwsRadioMode,
       "ntwsMichaelMICFailureCause": ntwsMichaelMICFailureCause,
       "ntwsClientAccessMode": ntwsClientAccessMode,
       "ntwsClientAuthorizationReason": ntwsClientAuthorizationReason,
       "ntwsPhysPortNum": ntwsPhysPortNum,
       "ntwsApMgrOldIp": ntwsApMgrOldIp,
       "ntwsApMgrNewIp": ntwsApMgrNewIp,
       "ntwsApMgrChangeReason": ntwsApMgrChangeReason,
       "ntwsClientClearedReason": ntwsClientClearedReason,
       "ntwsMobilityDomainResiliencyStatus": ntwsMobilityDomainResiliencyStatus,
       "ntwsClientSessionElapsedSeconds": ntwsClientSessionElapsedSeconds,
       "ntwsRadioChannelWidth": ntwsRadioChannelWidth,
       "ntwsRadioMimoState": ntwsRadioMimoState,
       "ntwsClientRadioType": ntwsClientRadioType,
       "ntwsRFDetectXmtrRadioType": ntwsRFDetectXmtrRadioType,
       "ntwsRFDetectXmtrCryptoType": ntwsRFDetectXmtrCryptoType,
       "ntwsClusterFailureReason": ntwsClusterFailureReason,
       "ntwsClusterFailureDescription": ntwsClusterFailureDescription,
       "ntwsTrapMib": ntwsTrapMib,
       "ntwsTrapsV2": ntwsTrapsV2,
       "ntwsDeviceFailTrap": ntwsDeviceFailTrap,
       "ntwsDeviceOkayTrap": ntwsDeviceOkayTrap,
       "ntwsPoEFailTrap": ntwsPoEFailTrap,
       "ntwsApTimeoutTrap": ntwsApTimeoutTrap,
       "ntwsAPBootTrap": ntwsAPBootTrap,
       "ntwsMobilityDomainJoinTrap": ntwsMobilityDomainJoinTrap,
       "ntwsMobilityDomainTimeoutTrap": ntwsMobilityDomainTimeoutTrap,
       "ntwsMpMichaelMICFailure": ntwsMpMichaelMICFailure,
       "ntwsRFDetectRogueAPTrap": ntwsRFDetectRogueAPTrap,
       "ntwsRFDetectAdhocUserTrap": ntwsRFDetectAdhocUserTrap,
       "ntwsRFDetectRogueDisappearTrap": ntwsRFDetectRogueDisappearTrap,
       "ntwsClientAuthenticationFailureTrap": ntwsClientAuthenticationFailureTrap,
       "ntwsClientAuthorizationFailureTrap": ntwsClientAuthorizationFailureTrap,
       "ntwsClientAssociationFailureTrap": ntwsClientAssociationFailureTrap,
       "ntwsClientAuthorizationSuccessTrap": ntwsClientAuthorizationSuccessTrap,
       "ntwsClientDeAssociationTrap": ntwsClientDeAssociationTrap,
       "ntwsClientRoamingTrap": ntwsClientRoamingTrap,
       "ntwsAutoTuneRadioPowerChangeTrap": ntwsAutoTuneRadioPowerChangeTrap,
       "ntwsAutoTuneRadioChannelChangeTrap": ntwsAutoTuneRadioChannelChangeTrap,
       "ntwsCounterMeasureStartTrap": ntwsCounterMeasureStartTrap,
       "ntwsCounterMeasureStopTrap": ntwsCounterMeasureStopTrap,
       "ntwsClientDot1xFailureTrap": ntwsClientDot1xFailureTrap,
       "ntwsClientClearedTrap": ntwsClientClearedTrap,
       "ntwsClientAuthorizationSuccessTrap2": ntwsClientAuthorizationSuccessTrap2,
       "ntwsRFDetectSpoofedMacAPTrap": ntwsRFDetectSpoofedMacAPTrap,
       "ntwsRFDetectSpoofedSsidAPTrap": ntwsRFDetectSpoofedSsidAPTrap,
       "ntwsRFDetectDoSTrap": ntwsRFDetectDoSTrap,
       "ntwsRFDetectClientViaRogueWiredAPTrap": ntwsRFDetectClientViaRogueWiredAPTrap,
       "ntwsRFDetectInterferingRogueAPTrap": ntwsRFDetectInterferingRogueAPTrap,
       "ntwsRFDetectInterferingRogueDisappearTrap": ntwsRFDetectInterferingRogueDisappearTrap,
       "ntwsRFDetectUnAuthorizedSsidTrap": ntwsRFDetectUnAuthorizedSsidTrap,
       "ntwsRFDetectUnAuthorizedOuiTrap": ntwsRFDetectUnAuthorizedOuiTrap,
       "ntwsRFDetectUnAuthorizedAPTrap": ntwsRFDetectUnAuthorizedAPTrap,
       "ntwsDAPConnectWarningTrap": ntwsDAPConnectWarningTrap,
       "ntwsRFDetectDoSPortTrap": ntwsRFDetectDoSPortTrap,
       "ntwsMpMichaelMICFailure2": ntwsMpMichaelMICFailure2,
       "ntwsApNonOperStatusTrap": ntwsApNonOperStatusTrap,
       "ntwsApOperRadioStatusTrap": ntwsApOperRadioStatusTrap,
       "ntwsClientIpAddrChangeTrap": ntwsClientIpAddrChangeTrap,
       "ntwsClientAssociationSuccessTrap": ntwsClientAssociationSuccessTrap,
       "ntwsClientAuthenticationSuccessTrap": ntwsClientAuthenticationSuccessTrap,
       "ntwsClientDeAuthenticationTrap": ntwsClientDeAuthenticationTrap,
       "ntwsRFDetectBlacklistedTrap": ntwsRFDetectBlacklistedTrap,
       "ntwsRFDetectClientViaRogueWiredAPTrap2": ntwsRFDetectClientViaRogueWiredAPTrap2,
       "ntwsRFDetectAdhocUserDisappearTrap": ntwsRFDetectAdhocUserDisappearTrap,
       "ntwsApRejectLicenseExceededTrap": ntwsApRejectLicenseExceededTrap,
       "ntwsClientDynAuthorChangeSuccessTrap": ntwsClientDynAuthorChangeSuccessTrap,
       "ntwsClientDynAuthorChangeFailureTrap": ntwsClientDynAuthorChangeFailureTrap,
       "ntwsClientDisconnectTrap": ntwsClientDisconnectTrap,
       "ntwsMobilityDomainFailOverTrap": ntwsMobilityDomainFailOverTrap,
       "ntwsMobilityDomainFailBackTrap": ntwsMobilityDomainFailBackTrap,
       "ntwsRFDetectRogueDeviceTrap": ntwsRFDetectRogueDeviceTrap,
       "ntwsRFDetectRogueDeviceDisappearTrap": ntwsRFDetectRogueDeviceDisappearTrap,
       "ntwsRFDetectSuspectDeviceTrap": ntwsRFDetectSuspectDeviceTrap,
       "ntwsRFDetectSuspectDeviceDisappearTrap": ntwsRFDetectSuspectDeviceDisappearTrap,
       "ntwsRFDetectClientViaRogueWiredAPTrap3": ntwsRFDetectClientViaRogueWiredAPTrap3,
       "ntwsRFDetectClassificationChangeTrap": ntwsRFDetectClassificationChangeTrap,
       "ntwsConfigurationSavedTrap": ntwsConfigurationSavedTrap,
       "ntwsApNonOperStatusTrap2": ntwsApNonOperStatusTrap2,
       "ntwsApOperRadioStatusTrap2": ntwsApOperRadioStatusTrap2,
       "ntwsMichaelMICFailure": ntwsMichaelMICFailure,
       "ntwsClientAuthorizationSuccessTrap3": ntwsClientAuthorizationSuccessTrap3,
       "ntwsApManagerChangeTrap": ntwsApManagerChangeTrap,
       "ntwsClientClearedTrap2": ntwsClientClearedTrap2,
       "ntwsMobilityDomainResiliencyStatusTrap": ntwsMobilityDomainResiliencyStatusTrap,
       "ntwsApOperRadioStatusTrap3": ntwsApOperRadioStatusTrap3,
       "ntwsClientAuthorizationSuccessTrap4": ntwsClientAuthorizationSuccessTrap4,
       "ntwsRFDetectRogueDeviceTrap2": ntwsRFDetectRogueDeviceTrap2,
       "ntwsRFDetectSuspectDeviceTrap2": ntwsRFDetectSuspectDeviceTrap2,
       "ntwsClusterFailureTrap": ntwsClusterFailureTrap}
)
