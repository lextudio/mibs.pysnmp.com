# SNMP MIB module (ALCATEL-IND1-TIMETRA-OAM-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-TIMETRA-OAM-TEST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:18 2024
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

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TProfile,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-QOS-MIB",
    "TProfile")

(SdpBindVcType,
 SdpId) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-SERV-MIB",
    "SdpBindVcType",
    "SdpId")

(IpAddressPrefixLength,
 SdpBindId,
 TFCName,
 TItemDescription,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TmnxAdminState,
 TmnxBgpRouteTarget,
 TmnxEncapVal,
 TmnxPortID,
 TmnxServId,
 TmnxStrSapId,
 TmnxTunnelID,
 TmnxTunnelType,
 TmnxVPNRouteDistinguisher,
 TmnxVRtrID,
 TmnxVcId,
 TmnxVcIdOrNone,
 TmnxVcType) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-TC-MIB",
    "IpAddressPrefixLength",
    "SdpBindId",
    "TFCName",
    "TItemDescription",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TmnxAdminState",
    "TmnxBgpRouteTarget",
    "TmnxEncapVal",
    "TmnxPortID",
    "TmnxServId",
    "TmnxStrSapId",
    "TmnxTunnelID",
    "TmnxTunnelType",
    "TmnxVPNRouteDistinguisher",
    "TmnxVRtrID",
    "TmnxVcId",
    "TmnxVcIdOrNone",
    "TmnxVcType")

(vRtrID,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-VRTR-MIB",
    "vRtrID")

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(MplsLabel,) = mibBuilder.importSymbols(
    "MPLS-LDP-MIB",
    "MplsLabel")

(RouterID,) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "RouterID")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

timetraOamTestMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 11)
)
timetraOamTestMIBModule.setRevisions(
        ("1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-03-09 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1901-11-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxOamTestMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", 0),
          ("ping", 1),
          ("traceroute", 2))
    )



class TmnxOamPingRtnCode(Integer32, TextualConvention):
    status = "current"
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
        *(("downstream", 4),
          ("downstreamMismatched", 11),
          ("downstreamNotInMfib", 10),
          ("downstreamNotLabel", 5),
          ("downstreamNotMac", 6),
          ("downstreamNotMacFlood", 7),
          ("fecEgress", 1),
          ("fecNoMap", 2),
          ("malformedEchoRequest", 8),
          ("noLabelAtStackDepth", 14),
          ("noMplsFwd", 13),
          ("notApplicable", 0),
          ("notDownstream", 3),
          ("protoIntfMismatched", 15),
          ("terminatedByOneLabel", 16),
          ("tlvNotUnderstood", 9),
          ("upstreamIfIdUnkn", 12))
    )



class TmnxOamAddressType(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Address", 1),
          ("ipv4Unnumbered", 7),
          ("ipv6Address", 2),
          ("ipv6Unnumbered", 8),
          ("localCpu", 6),
          ("macAddress", 3),
          ("sapId", 4),
          ("sdpId", 5),
          ("unknown", 0))
    )



class TmnxOamResponseStatus(Integer32, TextualConvention):
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87)
        )
    )
    namedValues = NamedValues(
        *(("ancpMaxNbrAncpTestsInProgress", 85),
          ("ancpNoAccessNodeforAncpString", 82),
          ("ancpNoAncpCapabilityNegotiated", 83),
          ("ancpNoAncpString", 79),
          ("ancpNoAncpStringForSubscriber", 81),
          ("ancpNoSubscriber", 80),
          ("ancpOtherTestInProgress", 84),
          ("bgpDaemonBusy", 45),
          ("bindSocketFail", 60),
          ("changedResponderId", 24),
          ("dnsLookupFail", 74),
          ("dnsNameNotFound", 50),
          ("downLspPath", 37),
          ("downOrigSdpBinding", 33),
          ("downOrigSdpId", 7),
          ("downOrigSvcId", 25),
          ("downOriginatorId", 22),
          ("downRespSdpId", 12),
          ("downRespSvcId", 26),
          ("downResponderId", 23),
          ("downServiceSdp", 15),
          ("farEndUnreachable", 21),
          ("farEndVccvNotSupported", 70),
          ("internalError", 3),
          ("invalidHostAddress", 17),
          ("invalidLspId", 36),
          ("invalidLspLabel", 39),
          ("invalidLspName", 19),
          ("invalidLspPathName", 34),
          ("invalidLspProtocol", 38),
          ("invalidMacAddress", 18),
          ("invalidOriginatorId", 9),
          ("invalidResponderId", 10),
          ("invalidSdp", 14),
          ("invalidServiceId", 13),
          ("localExtranetRoute", 42),
          ("mTraceNoSGFlow", 47),
          ("mTraceSysIpNotCfg", 48),
          ("macIsLocal", 20),
          ("maxConcurrentLimitReached", 4),
          ("mcastNotEnabled", 46),
          ("mismatchCustId", 28),
          ("mismatchSvcLabel", 31),
          ("mismatchSvcMtu", 30),
          ("mismatchSvcType", 29),
          ("msPwInvalidReplyMode", 78),
          ("multipathNotSupported", 76),
          ("nexthopUnreachable", 67),
          ("nhIntfNameNotFound", 77),
          ("noDirectInterface", 66),
          ("noFwdEntryInMfib", 49),
          ("noIntf", 62),
          ("noIpv6SrcAddrOnIntf", 75),
          ("noLocalIp", 63),
          ("noLspEndpointAddr", 35),
          ("noMsPwVccvInReplyDir", 87),
          ("noRouteByIntf", 61),
          ("noRouteToDest", 41),
          ("noSdpBoundToSvc", 32),
          ("noServiceEgressLabel", 16),
          ("noServiceIngressLabel", 27),
          ("noSocket", 51),
          ("noSpokeSdpInVll", 69),
          ("noVcEgressLabel", 71),
          ("rcvdWrongSize", 73),
          ("rcvdWrongType", 65),
          ("requestTerminated", 8),
          ("requestTimedOut", 5),
          ("responseReceived", 1),
          ("routeIsLocal", 40),
          ("sendtoFail", 64),
          ("socketOptHdrincFail", 57),
          ("socketOptHwTimeStampFail", 68),
          ("socketOptIfInexFail", 53),
          ("socketOptIpSessionFail", 72),
          ("socketOptMtuDiscFail", 55),
          ("socketOptNextHopFail", 54),
          ("socketOptSndbufFail", 56),
          ("socketOptTosFail", 58),
          ("socketOptTtlFail", 59),
          ("socketOptVprnIdFail", 52),
          ("spokeSdpOperDown", 86),
          ("srcIpInBgpVpnRoute", 43),
          ("srcIpInvalid", 44),
          ("unknown", 2),
          ("unknownOrigSdpId", 6),
          ("unknownRespSdpId", 11))
    )



class TmnxOamSignalProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 2),
          ("crLdp", 5),
          ("ldp", 3),
          ("rsvpTe", 4),
          ("static", 1),
          ("unknown", 0))
    )



class TmnxOamTestResponsePlane(Integer32, TextualConvention):
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
        *(("controlPlane", 1),
          ("dataPlane", 2),
          ("none", 3))
    )



class TmnxOamSaaThreshold(Integer32, TextualConvention):
    status = "current"
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
        *(("inJitter", 1),
          ("inLatency", 7),
          ("inLoss", 4),
          ("noThreshold", 0),
          ("outJitter", 2),
          ("outLatency", 8),
          ("outLoss", 5),
          ("rtJitter", 3),
          ("rtLatency", 9),
          ("rtLoss", 6))
    )



class TmnxOamVcType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              11)
        )
    )
    namedValues = NamedValues(
        *(("meshSdp", 5),
          ("spokeSdp", 11))
    )



class TmnxOamLTtraceDisStatusBits(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_TmnxOamTestConformance_ObjectIdentity = ObjectIdentity
tmnxOamTestConformance = _TmnxOamTestConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11)
)
_TmnxOamPingConformance_ObjectIdentity = ObjectIdentity
tmnxOamPingConformance = _TmnxOamPingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1)
)
_TmnxOamPingCompliances_ObjectIdentity = ObjectIdentity
tmnxOamPingCompliances = _TmnxOamPingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1)
)
_TmnxOamPingGroups_ObjectIdentity = ObjectIdentity
tmnxOamPingGroups = _TmnxOamPingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2)
)
_TmnxOamTraceRouteConformance_ObjectIdentity = ObjectIdentity
tmnxOamTraceRouteConformance = _TmnxOamTraceRouteConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2)
)
_TmnxOamTrCompliances_ObjectIdentity = ObjectIdentity
tmnxOamTrCompliances = _TmnxOamTrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1)
)
_TmnxOamTrGroups_ObjectIdentity = ObjectIdentity
tmnxOamTrGroups = _TmnxOamTrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2)
)
_TmnxOamSaaConformance_ObjectIdentity = ObjectIdentity
tmnxOamSaaConformance = _TmnxOamSaaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3)
)
_TmnxOamSaaCompliances_ObjectIdentity = ObjectIdentity
tmnxOamSaaCompliances = _TmnxOamSaaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 1)
)
_TmnxOamSaaGroups_ObjectIdentity = ObjectIdentity
tmnxOamSaaGroups = _TmnxOamSaaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 2)
)
_TmnxOamTestObjs_ObjectIdentity = ObjectIdentity
tmnxOamTestObjs = _TmnxOamTestObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11)
)
_TmnxOamPingObjs_ObjectIdentity = ObjectIdentity
tmnxOamPingObjs = _TmnxOamPingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1)
)
_TmnxOamPingNotificationObjects_ObjectIdentity = ObjectIdentity
tmnxOamPingNotificationObjects = _TmnxOamPingNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 1)
)


class _TmnxOamPingMaxConcurrentTests_Type(Unsigned32):
    """Custom type tmnxOamPingMaxConcurrentTests based on Unsigned32"""
    defaultValue = 0


_TmnxOamPingMaxConcurrentTests_Object = MibScalar
tmnxOamPingMaxConcurrentTests = _TmnxOamPingMaxConcurrentTests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 2),
    _TmnxOamPingMaxConcurrentTests_Type()
)
tmnxOamPingMaxConcurrentTests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPingMaxConcurrentTests.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingMaxConcurrentTests.setUnits("tests")
_TmnxOamPingCtlTable_Object = MibTable
tmnxOamPingCtlTable = _TmnxOamPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxOamPingCtlTable.setStatus("current")
_TmnxOamPingCtlEntry_Object = MibTableRow
tmnxOamPingCtlEntry = _TmnxOamPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1)
)
tmnxOamPingCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamPingCtlEntry.setStatus("current")


class _TmnxOamPingCtlOwnerIndex_Type(SnmpAdminString):
    """Custom type tmnxOamPingCtlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxOamPingCtlOwnerIndex_Type.__name__ = "SnmpAdminString"
_TmnxOamPingCtlOwnerIndex_Object = MibTableColumn
tmnxOamPingCtlOwnerIndex = _TmnxOamPingCtlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 1),
    _TmnxOamPingCtlOwnerIndex_Type()
)
tmnxOamPingCtlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPingCtlOwnerIndex.setStatus("current")


class _TmnxOamPingCtlTestIndex_Type(SnmpAdminString):
    """Custom type tmnxOamPingCtlTestIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxOamPingCtlTestIndex_Type.__name__ = "SnmpAdminString"
_TmnxOamPingCtlTestIndex_Object = MibTableColumn
tmnxOamPingCtlTestIndex = _TmnxOamPingCtlTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 2),
    _TmnxOamPingCtlTestIndex_Type()
)
tmnxOamPingCtlTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTestIndex.setStatus("current")
_TmnxOamPingCtlRowStatus_Type = RowStatus
_TmnxOamPingCtlRowStatus_Object = MibTableColumn
tmnxOamPingCtlRowStatus = _TmnxOamPingCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 3),
    _TmnxOamPingCtlRowStatus_Type()
)
tmnxOamPingCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlRowStatus.setStatus("current")


class _TmnxOamPingCtlStorageType_Type(StorageType):
    """Custom type tmnxOamPingCtlStorageType based on StorageType"""


_TmnxOamPingCtlStorageType_Object = MibTableColumn
tmnxOamPingCtlStorageType = _TmnxOamPingCtlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 4),
    _TmnxOamPingCtlStorageType_Type()
)
tmnxOamPingCtlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlStorageType.setStatus("current")


class _TmnxOamPingCtlDescr_Type(SnmpAdminString):
    """Custom type tmnxOamPingCtlDescr based on SnmpAdminString"""
    defaultHexValue = ""


_TmnxOamPingCtlDescr_Object = MibTableColumn
tmnxOamPingCtlDescr = _TmnxOamPingCtlDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 5),
    _TmnxOamPingCtlDescr_Type()
)
tmnxOamPingCtlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlDescr.setStatus("current")


class _TmnxOamPingCtlTestMode_Type(Integer32):
    """Custom type tmnxOamPingCtlTestMode based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("ancpLoopback", 17),
          ("atmPing", 10),
          ("cpePing", 12),
          ("dnsPing", 16),
          ("icmpPing", 15),
          ("lspPing", 8),
          ("macPing", 5),
          ("macPopulate", 6),
          ("macPurge", 7),
          ("macQuery", 4),
          ("mfibPing", 11),
          ("mrInfo", 13),
          ("mtuPing", 2),
          ("sdpPing", 1),
          ("svcPing", 3),
          ("vccvPing", 14),
          ("vprnPing", 9))
    )


_TmnxOamPingCtlTestMode_Type.__name__ = "Integer32"
_TmnxOamPingCtlTestMode_Object = MibTableColumn
tmnxOamPingCtlTestMode = _TmnxOamPingCtlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 6),
    _TmnxOamPingCtlTestMode_Type()
)
tmnxOamPingCtlTestMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTestMode.setStatus("current")


class _TmnxOamPingCtlAdminStatus_Type(Integer32):
    """Custom type tmnxOamPingCtlAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_TmnxOamPingCtlAdminStatus_Type.__name__ = "Integer32"
_TmnxOamPingCtlAdminStatus_Object = MibTableColumn
tmnxOamPingCtlAdminStatus = _TmnxOamPingCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 7),
    _TmnxOamPingCtlAdminStatus_Type()
)
tmnxOamPingCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlAdminStatus.setStatus("current")


class _TmnxOamPingCtlOrigSdpId_Type(SdpId):
    """Custom type tmnxOamPingCtlOrigSdpId based on SdpId"""
    defaultValue = 0


_TmnxOamPingCtlOrigSdpId_Object = MibTableColumn
tmnxOamPingCtlOrigSdpId = _TmnxOamPingCtlOrigSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 8),
    _TmnxOamPingCtlOrigSdpId_Type()
)
tmnxOamPingCtlOrigSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlOrigSdpId.setStatus("current")


class _TmnxOamPingCtlRespSdpId_Type(SdpId):
    """Custom type tmnxOamPingCtlRespSdpId based on SdpId"""
    defaultValue = 0


_TmnxOamPingCtlRespSdpId_Object = MibTableColumn
tmnxOamPingCtlRespSdpId = _TmnxOamPingCtlRespSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 9),
    _TmnxOamPingCtlRespSdpId_Type()
)
tmnxOamPingCtlRespSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlRespSdpId.setStatus("current")


class _TmnxOamPingCtlFcName_Type(TFCName):
    """Custom type tmnxOamPingCtlFcName based on TFCName"""
    defaultValue = OctetString("be")


_TmnxOamPingCtlFcName_Object = MibTableColumn
tmnxOamPingCtlFcName = _TmnxOamPingCtlFcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 10),
    _TmnxOamPingCtlFcName_Type()
)
tmnxOamPingCtlFcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlFcName.setStatus("current")


class _TmnxOamPingCtlProfile_Type(TProfile):
    """Custom type tmnxOamPingCtlProfile based on TProfile"""


_TmnxOamPingCtlProfile_Object = MibTableColumn
tmnxOamPingCtlProfile = _TmnxOamPingCtlProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 11),
    _TmnxOamPingCtlProfile_Type()
)
tmnxOamPingCtlProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlProfile.setStatus("current")


class _TmnxOamPingCtlMtuStartSize_Type(Unsigned32):
    """Custom type tmnxOamPingCtlMtuStartSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(40, 9197),
    )


_TmnxOamPingCtlMtuStartSize_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlMtuStartSize_Object = MibTableColumn
tmnxOamPingCtlMtuStartSize = _TmnxOamPingCtlMtuStartSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 12),
    _TmnxOamPingCtlMtuStartSize_Type()
)
tmnxOamPingCtlMtuStartSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlMtuStartSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingCtlMtuStartSize.setUnits("Octets")


class _TmnxOamPingCtlMtuEndSize_Type(Unsigned32):
    """Custom type tmnxOamPingCtlMtuEndSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(41, 9198),
    )


_TmnxOamPingCtlMtuEndSize_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlMtuEndSize_Object = MibTableColumn
tmnxOamPingCtlMtuEndSize = _TmnxOamPingCtlMtuEndSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 13),
    _TmnxOamPingCtlMtuEndSize_Type()
)
tmnxOamPingCtlMtuEndSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlMtuEndSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingCtlMtuEndSize.setUnits("Octets")


class _TmnxOamPingCtlMtuStepSize_Type(Unsigned32):
    """Custom type tmnxOamPingCtlMtuStepSize based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_TmnxOamPingCtlMtuStepSize_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlMtuStepSize_Object = MibTableColumn
tmnxOamPingCtlMtuStepSize = _TmnxOamPingCtlMtuStepSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 14),
    _TmnxOamPingCtlMtuStepSize_Type()
)
tmnxOamPingCtlMtuStepSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlMtuStepSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingCtlMtuStepSize.setUnits("Octets")


class _TmnxOamPingCtlTargetIpAddress_Type(IpAddress):
    """Custom type tmnxOamPingCtlTargetIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamPingCtlTargetIpAddress_Object = MibTableColumn
tmnxOamPingCtlTargetIpAddress = _TmnxOamPingCtlTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 16),
    _TmnxOamPingCtlTargetIpAddress_Type()
)
tmnxOamPingCtlTargetIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTargetIpAddress.setStatus("obsolete")


class _TmnxOamPingCtlServiceId_Type(TmnxServId):
    """Custom type tmnxOamPingCtlServiceId based on TmnxServId"""
    defaultValue = 0


_TmnxOamPingCtlServiceId_Object = MibTableColumn
tmnxOamPingCtlServiceId = _TmnxOamPingCtlServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 17),
    _TmnxOamPingCtlServiceId_Type()
)
tmnxOamPingCtlServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlServiceId.setStatus("current")


class _TmnxOamPingCtlLocalSdp_Type(TruthValue):
    """Custom type tmnxOamPingCtlLocalSdp based on TruthValue"""


_TmnxOamPingCtlLocalSdp_Object = MibTableColumn
tmnxOamPingCtlLocalSdp = _TmnxOamPingCtlLocalSdp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 18),
    _TmnxOamPingCtlLocalSdp_Type()
)
tmnxOamPingCtlLocalSdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlLocalSdp.setStatus("current")


class _TmnxOamPingCtlRemoteSdp_Type(TruthValue):
    """Custom type tmnxOamPingCtlRemoteSdp based on TruthValue"""


_TmnxOamPingCtlRemoteSdp_Object = MibTableColumn
tmnxOamPingCtlRemoteSdp = _TmnxOamPingCtlRemoteSdp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 19),
    _TmnxOamPingCtlRemoteSdp_Type()
)
tmnxOamPingCtlRemoteSdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlRemoteSdp.setStatus("current")


class _TmnxOamPingCtlSize_Type(Unsigned32):
    """Custom type tmnxOamPingCtlSize based on Unsigned32"""
    defaultValue = 72

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_TmnxOamPingCtlSize_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlSize_Object = MibTableColumn
tmnxOamPingCtlSize = _TmnxOamPingCtlSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 20),
    _TmnxOamPingCtlSize_Type()
)
tmnxOamPingCtlSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingCtlSize.setUnits("octets")


class _TmnxOamPingCtlTimeOut_Type(Unsigned32):
    """Custom type tmnxOamPingCtlTimeOut based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxOamPingCtlTimeOut_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlTimeOut_Object = MibTableColumn
tmnxOamPingCtlTimeOut = _TmnxOamPingCtlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 21),
    _TmnxOamPingCtlTimeOut_Type()
)
tmnxOamPingCtlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTimeOut.setUnits("seconds")


class _TmnxOamPingCtlProbeCount_Type(Unsigned32):
    """Custom type tmnxOamPingCtlProbeCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxOamPingCtlProbeCount_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlProbeCount_Object = MibTableColumn
tmnxOamPingCtlProbeCount = _TmnxOamPingCtlProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 22),
    _TmnxOamPingCtlProbeCount_Type()
)
tmnxOamPingCtlProbeCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingCtlProbeCount.setUnits("probes")


class _TmnxOamPingCtlInterval_Type(Unsigned32):
    """Custom type tmnxOamPingCtlInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TmnxOamPingCtlInterval_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlInterval_Object = MibTableColumn
tmnxOamPingCtlInterval = _TmnxOamPingCtlInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 23),
    _TmnxOamPingCtlInterval_Type()
)
tmnxOamPingCtlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingCtlInterval.setUnits("seconds")


class _TmnxOamPingCtlMaxRows_Type(Unsigned32):
    """Custom type tmnxOamPingCtlMaxRows based on Unsigned32"""
    defaultValue = 300


_TmnxOamPingCtlMaxRows_Object = MibTableColumn
tmnxOamPingCtlMaxRows = _TmnxOamPingCtlMaxRows_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 24),
    _TmnxOamPingCtlMaxRows_Type()
)
tmnxOamPingCtlMaxRows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlMaxRows.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingCtlMaxRows.setUnits("rows")


class _TmnxOamPingCtlTrapGeneration_Type(Bits):
    """Custom type tmnxOamPingCtlTrapGeneration based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("probeFailure", 0),
          ("testCompletion", 2),
          ("testFailure", 1))
    )

_TmnxOamPingCtlTrapGeneration_Type.__name__ = "Bits"
_TmnxOamPingCtlTrapGeneration_Object = MibTableColumn
tmnxOamPingCtlTrapGeneration = _TmnxOamPingCtlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 25),
    _TmnxOamPingCtlTrapGeneration_Type()
)
tmnxOamPingCtlTrapGeneration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTrapGeneration.setStatus("current")


class _TmnxOamPingCtlTrapProbeFailureFilter_Type(Unsigned32):
    """Custom type tmnxOamPingCtlTrapProbeFailureFilter based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TmnxOamPingCtlTrapProbeFailureFilter_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlTrapProbeFailureFilter_Object = MibTableColumn
tmnxOamPingCtlTrapProbeFailureFilter = _TmnxOamPingCtlTrapProbeFailureFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 26),
    _TmnxOamPingCtlTrapProbeFailureFilter_Type()
)
tmnxOamPingCtlTrapProbeFailureFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTrapProbeFailureFilter.setStatus("current")


class _TmnxOamPingCtlTrapTestFailureFilter_Type(Unsigned32):
    """Custom type tmnxOamPingCtlTrapTestFailureFilter based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TmnxOamPingCtlTrapTestFailureFilter_Type.__name__ = "Unsigned32"
_TmnxOamPingCtlTrapTestFailureFilter_Object = MibTableColumn
tmnxOamPingCtlTrapTestFailureFilter = _TmnxOamPingCtlTrapTestFailureFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 27),
    _TmnxOamPingCtlTrapTestFailureFilter_Type()
)
tmnxOamPingCtlTrapTestFailureFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTrapTestFailureFilter.setStatus("current")


class _TmnxOamPingCtlSAA_Type(TruthValue):
    """Custom type tmnxOamPingCtlSAA based on TruthValue"""


_TmnxOamPingCtlSAA_Object = MibTableColumn
tmnxOamPingCtlSAA = _TmnxOamPingCtlSAA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 28),
    _TmnxOamPingCtlSAA_Type()
)
tmnxOamPingCtlSAA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlSAA.setStatus("current")
_TmnxOamPingCtlRuns_Type = Counter32
_TmnxOamPingCtlRuns_Object = MibTableColumn
tmnxOamPingCtlRuns = _TmnxOamPingCtlRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 29),
    _TmnxOamPingCtlRuns_Type()
)
tmnxOamPingCtlRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingCtlRuns.setStatus("current")
_TmnxOamPingCtlFailures_Type = Counter32
_TmnxOamPingCtlFailures_Object = MibTableColumn
tmnxOamPingCtlFailures = _TmnxOamPingCtlFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 30),
    _TmnxOamPingCtlFailures_Type()
)
tmnxOamPingCtlFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingCtlFailures.setStatus("current")


class _TmnxOamPingCtlLastRunResult_Type(Integer32):
    """Custom type tmnxOamPingCtlLastRunResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 3),
          ("failed", 2),
          ("success", 1),
          ("undetermined", 0))
    )


_TmnxOamPingCtlLastRunResult_Type.__name__ = "Integer32"
_TmnxOamPingCtlLastRunResult_Object = MibTableColumn
tmnxOamPingCtlLastRunResult = _TmnxOamPingCtlLastRunResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 31),
    _TmnxOamPingCtlLastRunResult_Type()
)
tmnxOamPingCtlLastRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingCtlLastRunResult.setStatus("current")
_TmnxOamPingCtlLastChanged_Type = TimeStamp
_TmnxOamPingCtlLastChanged_Object = MibTableColumn
tmnxOamPingCtlLastChanged = _TmnxOamPingCtlLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 32),
    _TmnxOamPingCtlLastChanged_Type()
)
tmnxOamPingCtlLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingCtlLastChanged.setStatus("current")


class _TmnxOamPingCtlVRtrID_Type(TmnxVRtrID):
    """Custom type tmnxOamPingCtlVRtrID based on TmnxVRtrID"""
    defaultValue = 1


_TmnxOamPingCtlVRtrID_Object = MibTableColumn
tmnxOamPingCtlVRtrID = _TmnxOamPingCtlVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 33),
    _TmnxOamPingCtlVRtrID_Type()
)
tmnxOamPingCtlVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlVRtrID.setStatus("current")


class _TmnxOamPingCtlTgtAddrType_Type(InetAddressType):
    """Custom type tmnxOamPingCtlTgtAddrType based on InetAddressType"""


_TmnxOamPingCtlTgtAddrType_Object = MibTableColumn
tmnxOamPingCtlTgtAddrType = _TmnxOamPingCtlTgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 34),
    _TmnxOamPingCtlTgtAddrType_Type()
)
tmnxOamPingCtlTgtAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTgtAddrType.setStatus("current")


class _TmnxOamPingCtlTgtAddress_Type(InetAddress):
    """Custom type tmnxOamPingCtlTgtAddress based on InetAddress"""
    defaultHexValue = ""


_TmnxOamPingCtlTgtAddress_Object = MibTableColumn
tmnxOamPingCtlTgtAddress = _TmnxOamPingCtlTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 35),
    _TmnxOamPingCtlTgtAddress_Type()
)
tmnxOamPingCtlTgtAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlTgtAddress.setStatus("current")


class _TmnxOamPingCtlSrcAddrType_Type(InetAddressType):
    """Custom type tmnxOamPingCtlSrcAddrType based on InetAddressType"""


_TmnxOamPingCtlSrcAddrType_Object = MibTableColumn
tmnxOamPingCtlSrcAddrType = _TmnxOamPingCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 36),
    _TmnxOamPingCtlSrcAddrType_Type()
)
tmnxOamPingCtlSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlSrcAddrType.setStatus("current")


class _TmnxOamPingCtlSrcAddress_Type(InetAddress):
    """Custom type tmnxOamPingCtlSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamPingCtlSrcAddress_Type.__name__ = "InetAddress"
_TmnxOamPingCtlSrcAddress_Object = MibTableColumn
tmnxOamPingCtlSrcAddress = _TmnxOamPingCtlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 37),
    _TmnxOamPingCtlSrcAddress_Type()
)
tmnxOamPingCtlSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlSrcAddress.setStatus("current")


class _TmnxOamPingCtlDnsName_Type(OctetString):
    """Custom type tmnxOamPingCtlDnsName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxOamPingCtlDnsName_Type.__name__ = "OctetString"
_TmnxOamPingCtlDnsName_Object = MibTableColumn
tmnxOamPingCtlDnsName = _TmnxOamPingCtlDnsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 38),
    _TmnxOamPingCtlDnsName_Type()
)
tmnxOamPingCtlDnsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlDnsName.setStatus("current")


class _TmnxOamPingCtlDNSRecord_Type(Integer32):
    """Custom type tmnxOamPingCtlDNSRecord based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Arecord", 1),
          ("ipv6AAAArecord", 2))
    )


_TmnxOamPingCtlDNSRecord_Type.__name__ = "Integer32"
_TmnxOamPingCtlDNSRecord_Object = MibTableColumn
tmnxOamPingCtlDNSRecord = _TmnxOamPingCtlDNSRecord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 3, 1, 39),
    _TmnxOamPingCtlDNSRecord_Type()
)
tmnxOamPingCtlDNSRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPingCtlDNSRecord.setStatus("current")
_TmnxOamPingResultsTable_Object = MibTable
tmnxOamPingResultsTable = _TmnxOamPingResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxOamPingResultsTable.setStatus("current")
_TmnxOamPingResultsEntry_Object = MibTableRow
tmnxOamPingResultsEntry = _TmnxOamPingResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1)
)
tmnxOamPingResultsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamPingResultsEntry.setStatus("current")


class _TmnxOamPingResultsOperStatus_Type(Integer32):
    """Custom type tmnxOamPingResultsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_TmnxOamPingResultsOperStatus_Type.__name__ = "Integer32"
_TmnxOamPingResultsOperStatus_Object = MibTableColumn
tmnxOamPingResultsOperStatus = _TmnxOamPingResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 1),
    _TmnxOamPingResultsOperStatus_Type()
)
tmnxOamPingResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsOperStatus.setStatus("current")
_TmnxOamPingResultsMinRtt_Type = Unsigned32
_TmnxOamPingResultsMinRtt_Object = MibTableColumn
tmnxOamPingResultsMinRtt = _TmnxOamPingResultsMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 4),
    _TmnxOamPingResultsMinRtt_Type()
)
tmnxOamPingResultsMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMinRtt.setUnits("milliseconds")
_TmnxOamPingResultsMaxRtt_Type = Unsigned32
_TmnxOamPingResultsMaxRtt_Object = MibTableColumn
tmnxOamPingResultsMaxRtt = _TmnxOamPingResultsMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 5),
    _TmnxOamPingResultsMaxRtt_Type()
)
tmnxOamPingResultsMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMaxRtt.setUnits("milliseconds")
_TmnxOamPingResultsAverageRtt_Type = Unsigned32
_TmnxOamPingResultsAverageRtt_Object = MibTableColumn
tmnxOamPingResultsAverageRtt = _TmnxOamPingResultsAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 6),
    _TmnxOamPingResultsAverageRtt_Type()
)
tmnxOamPingResultsAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsAverageRtt.setUnits("milliseconds")
_TmnxOamPingResultsRttSumOfSquares_Type = Unsigned32
_TmnxOamPingResultsRttSumOfSquares_Object = MibTableColumn
tmnxOamPingResultsRttSumOfSquares = _TmnxOamPingResultsRttSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 7),
    _TmnxOamPingResultsRttSumOfSquares_Type()
)
tmnxOamPingResultsRttSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsRttSumOfSquares.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsRttSumOfSquares.setUnits("milliseconds")
_TmnxOamPingResultsMtuResponseSize_Type = Unsigned32
_TmnxOamPingResultsMtuResponseSize_Object = MibTableColumn
tmnxOamPingResultsMtuResponseSize = _TmnxOamPingResultsMtuResponseSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 8),
    _TmnxOamPingResultsMtuResponseSize_Type()
)
tmnxOamPingResultsMtuResponseSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMtuResponseSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMtuResponseSize.setUnits("Octets")


class _TmnxOamPingResultsSvcPing_Type(Integer32):
    """Custom type tmnxOamPingResultsSvcPing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("success", 2),
          ("undetermined", 0))
    )


_TmnxOamPingResultsSvcPing_Type.__name__ = "Integer32"
_TmnxOamPingResultsSvcPing_Object = MibTableColumn
tmnxOamPingResultsSvcPing = _TmnxOamPingResultsSvcPing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 9),
    _TmnxOamPingResultsSvcPing_Type()
)
tmnxOamPingResultsSvcPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsSvcPing.setStatus("current")
_TmnxOamPingResultsProbeResponses_Type = Unsigned32
_TmnxOamPingResultsProbeResponses_Object = MibTableColumn
tmnxOamPingResultsProbeResponses = _TmnxOamPingResultsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 10),
    _TmnxOamPingResultsProbeResponses_Type()
)
tmnxOamPingResultsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsProbeResponses.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsProbeResponses.setUnits("responses")
_TmnxOamPingResultsSentProbes_Type = Unsigned32
_TmnxOamPingResultsSentProbes_Object = MibTableColumn
tmnxOamPingResultsSentProbes = _TmnxOamPingResultsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 11),
    _TmnxOamPingResultsSentProbes_Type()
)
tmnxOamPingResultsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsSentProbes.setUnits("probes")
_TmnxOamPingResultsLastGoodProbe_Type = DateAndTime
_TmnxOamPingResultsLastGoodProbe_Object = MibTableColumn
tmnxOamPingResultsLastGoodProbe = _TmnxOamPingResultsLastGoodProbe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 12),
    _TmnxOamPingResultsLastGoodProbe_Type()
)
tmnxOamPingResultsLastGoodProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsLastGoodProbe.setStatus("current")


class _TmnxOamPingResultsLastRespHeader_Type(OctetString):
    """Custom type tmnxOamPingResultsLastRespHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )


_TmnxOamPingResultsLastRespHeader_Type.__name__ = "OctetString"
_TmnxOamPingResultsLastRespHeader_Object = MibTableColumn
tmnxOamPingResultsLastRespHeader = _TmnxOamPingResultsLastRespHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 13),
    _TmnxOamPingResultsLastRespHeader_Type()
)
tmnxOamPingResultsLastRespHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsLastRespHeader.setStatus("current")
_TmnxOamPingResultsMinTt_Type = Integer32
_TmnxOamPingResultsMinTt_Object = MibTableColumn
tmnxOamPingResultsMinTt = _TmnxOamPingResultsMinTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 14),
    _TmnxOamPingResultsMinTt_Type()
)
tmnxOamPingResultsMinTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMinTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMinTt.setUnits("milliseconds")
_TmnxOamPingResultsMaxTt_Type = Integer32
_TmnxOamPingResultsMaxTt_Object = MibTableColumn
tmnxOamPingResultsMaxTt = _TmnxOamPingResultsMaxTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 15),
    _TmnxOamPingResultsMaxTt_Type()
)
tmnxOamPingResultsMaxTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMaxTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMaxTt.setUnits("milliseconds")
_TmnxOamPingResultsAverageTt_Type = Integer32
_TmnxOamPingResultsAverageTt_Object = MibTableColumn
tmnxOamPingResultsAverageTt = _TmnxOamPingResultsAverageTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 16),
    _TmnxOamPingResultsAverageTt_Type()
)
tmnxOamPingResultsAverageTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsAverageTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsAverageTt.setUnits("milliseconds")
_TmnxOamPingResultsTtSumOfSquares_Type = Integer32
_TmnxOamPingResultsTtSumOfSquares_Object = MibTableColumn
tmnxOamPingResultsTtSumOfSquares = _TmnxOamPingResultsTtSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 17),
    _TmnxOamPingResultsTtSumOfSquares_Type()
)
tmnxOamPingResultsTtSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsTtSumOfSquares.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsTtSumOfSquares.setUnits("milliseconds")
_TmnxOamPingResultsMinInTt_Type = Integer32
_TmnxOamPingResultsMinInTt_Object = MibTableColumn
tmnxOamPingResultsMinInTt = _TmnxOamPingResultsMinInTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 18),
    _TmnxOamPingResultsMinInTt_Type()
)
tmnxOamPingResultsMinInTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMinInTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMinInTt.setUnits("milliseconds")
_TmnxOamPingResultsMaxInTt_Type = Integer32
_TmnxOamPingResultsMaxInTt_Object = MibTableColumn
tmnxOamPingResultsMaxInTt = _TmnxOamPingResultsMaxInTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 19),
    _TmnxOamPingResultsMaxInTt_Type()
)
tmnxOamPingResultsMaxInTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMaxInTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsMaxInTt.setUnits("milliseconds")
_TmnxOamPingResultsAverageInTt_Type = Integer32
_TmnxOamPingResultsAverageInTt_Object = MibTableColumn
tmnxOamPingResultsAverageInTt = _TmnxOamPingResultsAverageInTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 20),
    _TmnxOamPingResultsAverageInTt_Type()
)
tmnxOamPingResultsAverageInTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsAverageInTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsAverageInTt.setUnits("milliseconds")
_TmnxOamPingResultsInTtSumOfSqrs_Type = Integer32
_TmnxOamPingResultsInTtSumOfSqrs_Object = MibTableColumn
tmnxOamPingResultsInTtSumOfSqrs = _TmnxOamPingResultsInTtSumOfSqrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 21),
    _TmnxOamPingResultsInTtSumOfSqrs_Type()
)
tmnxOamPingResultsInTtSumOfSqrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsInTtSumOfSqrs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsInTtSumOfSqrs.setUnits("milliseconds")
_TmnxOamPingResultsOutJitter_Type = Integer32
_TmnxOamPingResultsOutJitter_Object = MibTableColumn
tmnxOamPingResultsOutJitter = _TmnxOamPingResultsOutJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 22),
    _TmnxOamPingResultsOutJitter_Type()
)
tmnxOamPingResultsOutJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsOutJitter.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsOutJitter.setUnits("milliseconds")
_TmnxOamPingResultsInJitter_Type = Integer32
_TmnxOamPingResultsInJitter_Object = MibTableColumn
tmnxOamPingResultsInJitter = _TmnxOamPingResultsInJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 23),
    _TmnxOamPingResultsInJitter_Type()
)
tmnxOamPingResultsInJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsInJitter.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsInJitter.setUnits("milliseconds")
_TmnxOamPingResultsRtJitter_Type = Integer32
_TmnxOamPingResultsRtJitter_Object = MibTableColumn
tmnxOamPingResultsRtJitter = _TmnxOamPingResultsRtJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 24),
    _TmnxOamPingResultsRtJitter_Type()
)
tmnxOamPingResultsRtJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsRtJitter.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingResultsRtJitter.setUnits("milliseconds")
_TmnxOamPingResultsProbeTimeouts_Type = Unsigned32
_TmnxOamPingResultsProbeTimeouts_Object = MibTableColumn
tmnxOamPingResultsProbeTimeouts = _TmnxOamPingResultsProbeTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 25),
    _TmnxOamPingResultsProbeTimeouts_Type()
)
tmnxOamPingResultsProbeTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsProbeTimeouts.setStatus("current")
_TmnxOamPingResultsProbeFailures_Type = Unsigned32
_TmnxOamPingResultsProbeFailures_Object = MibTableColumn
tmnxOamPingResultsProbeFailures = _TmnxOamPingResultsProbeFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 26),
    _TmnxOamPingResultsProbeFailures_Type()
)
tmnxOamPingResultsProbeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingResultsProbeFailures.setStatus("current")


class _TmnxOamPingResultsTestRunIndex_Type(Unsigned32):
    """Custom type tmnxOamPingResultsTestRunIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamPingResultsTestRunIndex_Type.__name__ = "Unsigned32"
_TmnxOamPingResultsTestRunIndex_Object = MibTableColumn
tmnxOamPingResultsTestRunIndex = _TmnxOamPingResultsTestRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 4, 1, 27),
    _TmnxOamPingResultsTestRunIndex_Type()
)
tmnxOamPingResultsTestRunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPingResultsTestRunIndex.setStatus("current")
_TmnxOamPingHistoryTable_Object = MibTable
tmnxOamPingHistoryTable = _TmnxOamPingHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxOamPingHistoryTable.setStatus("current")
_TmnxOamPingHistoryEntry_Object = MibTableRow
tmnxOamPingHistoryEntry = _TmnxOamPingHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1)
)
tmnxOamPingHistoryEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamPingHistoryEntry.setStatus("current")


class _TmnxOamPingHistoryIndex_Type(Unsigned32):
    """Custom type tmnxOamPingHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamPingHistoryIndex_Type.__name__ = "Unsigned32"
_TmnxOamPingHistoryIndex_Object = MibTableColumn
tmnxOamPingHistoryIndex = _TmnxOamPingHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 1),
    _TmnxOamPingHistoryIndex_Type()
)
tmnxOamPingHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryIndex.setStatus("current")
_TmnxOamPingHistoryResponse_Type = Unsigned32
_TmnxOamPingHistoryResponse_Object = MibTableColumn
tmnxOamPingHistoryResponse = _TmnxOamPingHistoryResponse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 2),
    _TmnxOamPingHistoryResponse_Type()
)
tmnxOamPingHistoryResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryResponse.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryResponse.setUnits("milliseconds")
_TmnxOamPingHistoryOneWayTime_Type = Integer32
_TmnxOamPingHistoryOneWayTime_Object = MibTableColumn
tmnxOamPingHistoryOneWayTime = _TmnxOamPingHistoryOneWayTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 3),
    _TmnxOamPingHistoryOneWayTime_Type()
)
tmnxOamPingHistoryOneWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryOneWayTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryOneWayTime.setUnits("milliseconds")
_TmnxOamPingHistorySize_Type = Unsigned32
_TmnxOamPingHistorySize_Object = MibTableColumn
tmnxOamPingHistorySize = _TmnxOamPingHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 4),
    _TmnxOamPingHistorySize_Type()
)
tmnxOamPingHistorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistorySize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingHistorySize.setUnits("octets")
_TmnxOamPingHistoryStatus_Type = TmnxOamResponseStatus
_TmnxOamPingHistoryStatus_Object = MibTableColumn
tmnxOamPingHistoryStatus = _TmnxOamPingHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 5),
    _TmnxOamPingHistoryStatus_Type()
)
tmnxOamPingHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryStatus.setStatus("current")
_TmnxOamPingHistoryTime_Type = DateAndTime
_TmnxOamPingHistoryTime_Object = MibTableColumn
tmnxOamPingHistoryTime = _TmnxOamPingHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 6),
    _TmnxOamPingHistoryTime_Type()
)
tmnxOamPingHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryTime.setStatus("current")
_TmnxOamPingHistoryReturnCode_Type = TmnxOamPingRtnCode
_TmnxOamPingHistoryReturnCode_Object = MibTableColumn
tmnxOamPingHistoryReturnCode = _TmnxOamPingHistoryReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 7),
    _TmnxOamPingHistoryReturnCode_Type()
)
tmnxOamPingHistoryReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryReturnCode.setStatus("current")
_TmnxOamPingHistorySrcIpAddress_Type = IpAddress
_TmnxOamPingHistorySrcIpAddress_Object = MibTableColumn
tmnxOamPingHistorySrcIpAddress = _TmnxOamPingHistorySrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 8),
    _TmnxOamPingHistorySrcIpAddress_Type()
)
tmnxOamPingHistorySrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistorySrcIpAddress.setStatus("obsolete")
_TmnxOamPingHistAddressType_Type = TmnxOamAddressType
_TmnxOamPingHistAddressType_Object = MibTableColumn
tmnxOamPingHistAddressType = _TmnxOamPingHistAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 9),
    _TmnxOamPingHistAddressType_Type()
)
tmnxOamPingHistAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistAddressType.setStatus("current")
_TmnxOamPingHistSapId_Type = TmnxStrSapId
_TmnxOamPingHistSapId_Object = MibTableColumn
tmnxOamPingHistSapId = _TmnxOamPingHistSapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 10),
    _TmnxOamPingHistSapId_Type()
)
tmnxOamPingHistSapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistSapId.setStatus("current")
_TmnxOamPingHistoryVersion_Type = Unsigned32
_TmnxOamPingHistoryVersion_Object = MibTableColumn
tmnxOamPingHistoryVersion = _TmnxOamPingHistoryVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 12),
    _TmnxOamPingHistoryVersion_Type()
)
tmnxOamPingHistoryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryVersion.setStatus("current")
_TmnxOamPingHistoryCpeMacAddr_Type = MacAddress
_TmnxOamPingHistoryCpeMacAddr_Object = MibTableColumn
tmnxOamPingHistoryCpeMacAddr = _TmnxOamPingHistoryCpeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 13),
    _TmnxOamPingHistoryCpeMacAddr_Type()
)
tmnxOamPingHistoryCpeMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryCpeMacAddr.setStatus("current")
_TmnxOamPingHistoryRespSvcId_Type = TmnxServId
_TmnxOamPingHistoryRespSvcId_Object = MibTableColumn
tmnxOamPingHistoryRespSvcId = _TmnxOamPingHistoryRespSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 14),
    _TmnxOamPingHistoryRespSvcId_Type()
)
tmnxOamPingHistoryRespSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryRespSvcId.setStatus("current")
_TmnxOamPingHistorySequence_Type = Unsigned32
_TmnxOamPingHistorySequence_Object = MibTableColumn
tmnxOamPingHistorySequence = _TmnxOamPingHistorySequence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 15),
    _TmnxOamPingHistorySequence_Type()
)
tmnxOamPingHistorySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistorySequence.setStatus("current")
_TmnxOamPingHistoryIfIndex_Type = InterfaceIndexOrZero
_TmnxOamPingHistoryIfIndex_Object = MibTableColumn
tmnxOamPingHistoryIfIndex = _TmnxOamPingHistoryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 16),
    _TmnxOamPingHistoryIfIndex_Type()
)
tmnxOamPingHistoryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryIfIndex.setStatus("current")
_TmnxOamPingHistoryDataLen_Type = Unsigned32
_TmnxOamPingHistoryDataLen_Object = MibTableColumn
tmnxOamPingHistoryDataLen = _TmnxOamPingHistoryDataLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 17),
    _TmnxOamPingHistoryDataLen_Type()
)
tmnxOamPingHistoryDataLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryDataLen.setStatus("current")
_TmnxOamPingHistoryRespPlane_Type = TmnxOamTestResponsePlane
_TmnxOamPingHistoryRespPlane_Object = MibTableColumn
tmnxOamPingHistoryRespPlane = _TmnxOamPingHistoryRespPlane_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 18),
    _TmnxOamPingHistoryRespPlane_Type()
)
tmnxOamPingHistoryRespPlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryRespPlane.setStatus("current")


class _TmnxOamPingHistoryReqHdr_Type(OctetString):
    """Custom type tmnxOamPingHistoryReqHdr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 150),
    )


_TmnxOamPingHistoryReqHdr_Type.__name__ = "OctetString"
_TmnxOamPingHistoryReqHdr_Object = MibTableColumn
tmnxOamPingHistoryReqHdr = _TmnxOamPingHistoryReqHdr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 19),
    _TmnxOamPingHistoryReqHdr_Type()
)
tmnxOamPingHistoryReqHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryReqHdr.setStatus("current")


class _TmnxOamPingHistoryRespHdr_Type(OctetString):
    """Custom type tmnxOamPingHistoryRespHdr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 150),
    )


_TmnxOamPingHistoryRespHdr_Type.__name__ = "OctetString"
_TmnxOamPingHistoryRespHdr_Object = MibTableColumn
tmnxOamPingHistoryRespHdr = _TmnxOamPingHistoryRespHdr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 20),
    _TmnxOamPingHistoryRespHdr_Type()
)
tmnxOamPingHistoryRespHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryRespHdr.setStatus("current")
_TmnxOamPingHistoryDnsAddrType_Type = InetAddressType
_TmnxOamPingHistoryDnsAddrType_Object = MibTableColumn
tmnxOamPingHistoryDnsAddrType = _TmnxOamPingHistoryDnsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 21),
    _TmnxOamPingHistoryDnsAddrType_Type()
)
tmnxOamPingHistoryDnsAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryDnsAddrType.setStatus("current")


class _TmnxOamPingHistoryDnsAddress_Type(InetAddress):
    """Custom type tmnxOamPingHistoryDnsAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamPingHistoryDnsAddress_Type.__name__ = "InetAddress"
_TmnxOamPingHistoryDnsAddress_Object = MibTableColumn
tmnxOamPingHistoryDnsAddress = _TmnxOamPingHistoryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 22),
    _TmnxOamPingHistoryDnsAddress_Type()
)
tmnxOamPingHistoryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryDnsAddress.setStatus("current")
_TmnxOamPingHistorySrcAddrType_Type = InetAddressType
_TmnxOamPingHistorySrcAddrType_Object = MibTableColumn
tmnxOamPingHistorySrcAddrType = _TmnxOamPingHistorySrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 23),
    _TmnxOamPingHistorySrcAddrType_Type()
)
tmnxOamPingHistorySrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistorySrcAddrType.setStatus("current")


class _TmnxOamPingHistorySrcAddress_Type(InetAddress):
    """Custom type tmnxOamPingHistorySrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxOamPingHistorySrcAddress_Type.__name__ = "InetAddress"
_TmnxOamPingHistorySrcAddress_Object = MibTableColumn
tmnxOamPingHistorySrcAddress = _TmnxOamPingHistorySrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 24),
    _TmnxOamPingHistorySrcAddress_Type()
)
tmnxOamPingHistorySrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistorySrcAddress.setStatus("current")
_TmnxOamPingHistoryInOneWayTime_Type = Integer32
_TmnxOamPingHistoryInOneWayTime_Object = MibTableColumn
tmnxOamPingHistoryInOneWayTime = _TmnxOamPingHistoryInOneWayTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 5, 1, 25),
    _TmnxOamPingHistoryInOneWayTime_Type()
)
tmnxOamPingHistoryInOneWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryInOneWayTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPingHistoryInOneWayTime.setUnits("milliseconds")
_TmnxOamMacPingCtlTable_Object = MibTable
tmnxOamMacPingCtlTable = _TmnxOamMacPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlTable.setStatus("current")
_TmnxOamMacPingCtlEntry_Object = MibTableRow
tmnxOamMacPingCtlEntry = _TmnxOamMacPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1)
)
tmnxOamMacPingCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlEntry.setStatus("current")


class _TmnxOamMacPingCtlTargetMacAddr_Type(MacAddress):
    """Custom type tmnxOamMacPingCtlTargetMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamMacPingCtlTargetMacAddr_Object = MibTableColumn
tmnxOamMacPingCtlTargetMacAddr = _TmnxOamMacPingCtlTargetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 1),
    _TmnxOamMacPingCtlTargetMacAddr_Type()
)
tmnxOamMacPingCtlTargetMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlTargetMacAddr.setStatus("current")


class _TmnxOamMacPingCtlSourceMacAddr_Type(MacAddress):
    """Custom type tmnxOamMacPingCtlSourceMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamMacPingCtlSourceMacAddr_Object = MibTableColumn
tmnxOamMacPingCtlSourceMacAddr = _TmnxOamMacPingCtlSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 2),
    _TmnxOamMacPingCtlSourceMacAddr_Type()
)
tmnxOamMacPingCtlSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlSourceMacAddr.setStatus("current")


class _TmnxOamMacPingCtlSendControl_Type(TruthValue):
    """Custom type tmnxOamMacPingCtlSendControl based on TruthValue"""


_TmnxOamMacPingCtlSendControl_Object = MibTableColumn
tmnxOamMacPingCtlSendControl = _TmnxOamMacPingCtlSendControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 3),
    _TmnxOamMacPingCtlSendControl_Type()
)
tmnxOamMacPingCtlSendControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlSendControl.setStatus("current")


class _TmnxOamMacPingCtlReplyControl_Type(TruthValue):
    """Custom type tmnxOamMacPingCtlReplyControl based on TruthValue"""


_TmnxOamMacPingCtlReplyControl_Object = MibTableColumn
tmnxOamMacPingCtlReplyControl = _TmnxOamMacPingCtlReplyControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 4),
    _TmnxOamMacPingCtlReplyControl_Type()
)
tmnxOamMacPingCtlReplyControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlReplyControl.setStatus("current")


class _TmnxOamMacPingCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamMacPingCtlTtl based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamMacPingCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamMacPingCtlTtl_Object = MibTableColumn
tmnxOamMacPingCtlTtl = _TmnxOamMacPingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 5),
    _TmnxOamMacPingCtlTtl_Type()
)
tmnxOamMacPingCtlTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlTtl.setUnits("time-to-live value")


class _TmnxOamMacPingCtlRegister_Type(TruthValue):
    """Custom type tmnxOamMacPingCtlRegister based on TruthValue"""


_TmnxOamMacPingCtlRegister_Object = MibTableColumn
tmnxOamMacPingCtlRegister = _TmnxOamMacPingCtlRegister_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 6),
    _TmnxOamMacPingCtlRegister_Type()
)
tmnxOamMacPingCtlRegister.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlRegister.setStatus("current")


class _TmnxOamMacPingCtlFlood_Type(TruthValue):
    """Custom type tmnxOamMacPingCtlFlood based on TruthValue"""


_TmnxOamMacPingCtlFlood_Object = MibTableColumn
tmnxOamMacPingCtlFlood = _TmnxOamMacPingCtlFlood_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 7),
    _TmnxOamMacPingCtlFlood_Type()
)
tmnxOamMacPingCtlFlood.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlFlood.setStatus("current")


class _TmnxOamMacPingCtlForce_Type(TruthValue):
    """Custom type tmnxOamMacPingCtlForce based on TruthValue"""


_TmnxOamMacPingCtlForce_Object = MibTableColumn
tmnxOamMacPingCtlForce = _TmnxOamMacPingCtlForce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 8),
    _TmnxOamMacPingCtlForce_Type()
)
tmnxOamMacPingCtlForce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlForce.setStatus("current")


class _TmnxOamMacPingCtlAge_Type(Unsigned32):
    """Custom type tmnxOamMacPingCtlAge based on Unsigned32"""
    defaultValue = 3600


_TmnxOamMacPingCtlAge_Object = MibTableColumn
tmnxOamMacPingCtlAge = _TmnxOamMacPingCtlAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 9),
    _TmnxOamMacPingCtlAge_Type()
)
tmnxOamMacPingCtlAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlAge.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlAge.setUnits("seconds")


class _TmnxOamMacPingCtlSapPortId_Type(TmnxPortID):
    """Custom type tmnxOamMacPingCtlSapPortId based on TmnxPortID"""
    defaultValue = 0


_TmnxOamMacPingCtlSapPortId_Object = MibTableColumn
tmnxOamMacPingCtlSapPortId = _TmnxOamMacPingCtlSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 10),
    _TmnxOamMacPingCtlSapPortId_Type()
)
tmnxOamMacPingCtlSapPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlSapPortId.setStatus("current")


class _TmnxOamMacPingCtlSapEncapValue_Type(TmnxEncapVal):
    """Custom type tmnxOamMacPingCtlSapEncapValue based on TmnxEncapVal"""
    defaultValue = 0


_TmnxOamMacPingCtlSapEncapValue_Object = MibTableColumn
tmnxOamMacPingCtlSapEncapValue = _TmnxOamMacPingCtlSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 11),
    _TmnxOamMacPingCtlSapEncapValue_Type()
)
tmnxOamMacPingCtlSapEncapValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlSapEncapValue.setStatus("current")


class _TmnxOamMacPingCtlFibEntryName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamMacPingCtlFibEntryName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamMacPingCtlFibEntryName_Object = MibTableColumn
tmnxOamMacPingCtlFibEntryName = _TmnxOamMacPingCtlFibEntryName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 6, 1, 12),
    _TmnxOamMacPingCtlFibEntryName_Type()
)
tmnxOamMacPingCtlFibEntryName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacPingCtlFibEntryName.setStatus("current")
_TmnxOamMacPingHistoryTable_Object = MibTable
tmnxOamMacPingHistoryTable = _TmnxOamMacPingHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryTable.setStatus("current")
_TmnxOamMacPingHistoryEntry_Object = MibTableRow
tmnxOamMacPingHistoryEntry = _TmnxOamMacPingHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1)
)
tmnxOamMacPingHistoryEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingReplyIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryEntry.setStatus("current")


class _TmnxOamMacPingHistoryIndex_Type(Unsigned32):
    """Custom type tmnxOamMacPingHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamMacPingHistoryIndex_Type.__name__ = "Unsigned32"
_TmnxOamMacPingHistoryIndex_Object = MibTableColumn
tmnxOamMacPingHistoryIndex = _TmnxOamMacPingHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 1),
    _TmnxOamMacPingHistoryIndex_Type()
)
tmnxOamMacPingHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryIndex.setStatus("current")


class _TmnxOamMacPingReplyIndex_Type(Unsigned32):
    """Custom type tmnxOamMacPingReplyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamMacPingReplyIndex_Type.__name__ = "Unsigned32"
_TmnxOamMacPingReplyIndex_Object = MibTableColumn
tmnxOamMacPingReplyIndex = _TmnxOamMacPingReplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 2),
    _TmnxOamMacPingReplyIndex_Type()
)
tmnxOamMacPingReplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamMacPingReplyIndex.setStatus("current")
_TmnxOamMacPingHistoryResponse_Type = Unsigned32
_TmnxOamMacPingHistoryResponse_Object = MibTableColumn
tmnxOamMacPingHistoryResponse = _TmnxOamMacPingHistoryResponse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 3),
    _TmnxOamMacPingHistoryResponse_Type()
)
tmnxOamMacPingHistoryResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryResponse.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryResponse.setUnits("milliseconds")
_TmnxOamMacPingHistoryOneWayTime_Type = Integer32
_TmnxOamMacPingHistoryOneWayTime_Object = MibTableColumn
tmnxOamMacPingHistoryOneWayTime = _TmnxOamMacPingHistoryOneWayTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 4),
    _TmnxOamMacPingHistoryOneWayTime_Type()
)
tmnxOamMacPingHistoryOneWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryOneWayTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryOneWayTime.setUnits("milliseconds")
_TmnxOamMacPingHistoryStatus_Type = TmnxOamResponseStatus
_TmnxOamMacPingHistoryStatus_Object = MibTableColumn
tmnxOamMacPingHistoryStatus = _TmnxOamMacPingHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 5),
    _TmnxOamMacPingHistoryStatus_Type()
)
tmnxOamMacPingHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryStatus.setStatus("current")
_TmnxOamMacPingHistoryTime_Type = DateAndTime
_TmnxOamMacPingHistoryTime_Object = MibTableColumn
tmnxOamMacPingHistoryTime = _TmnxOamMacPingHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 6),
    _TmnxOamMacPingHistoryTime_Type()
)
tmnxOamMacPingHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryTime.setStatus("current")
_TmnxOamMacPingHistoryReturnCode_Type = TmnxOamPingRtnCode
_TmnxOamMacPingHistoryReturnCode_Object = MibTableColumn
tmnxOamMacPingHistoryReturnCode = _TmnxOamMacPingHistoryReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 7),
    _TmnxOamMacPingHistoryReturnCode_Type()
)
tmnxOamMacPingHistoryReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryReturnCode.setStatus("current")
_TmnxOamMacPingHistorySrcIpAddress_Type = IpAddress
_TmnxOamMacPingHistorySrcIpAddress_Object = MibTableColumn
tmnxOamMacPingHistorySrcIpAddress = _TmnxOamMacPingHistorySrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 8),
    _TmnxOamMacPingHistorySrcIpAddress_Type()
)
tmnxOamMacPingHistorySrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistorySrcIpAddress.setStatus("obsolete")
_TmnxOamMacPingHistoryAddressType_Type = TmnxOamAddressType
_TmnxOamMacPingHistoryAddressType_Object = MibTableColumn
tmnxOamMacPingHistoryAddressType = _TmnxOamMacPingHistoryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 9),
    _TmnxOamMacPingHistoryAddressType_Type()
)
tmnxOamMacPingHistoryAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryAddressType.setStatus("current")
_TmnxOamMacPingHistorySapId_Type = TmnxStrSapId
_TmnxOamMacPingHistorySapId_Object = MibTableColumn
tmnxOamMacPingHistorySapId = _TmnxOamMacPingHistorySapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 10),
    _TmnxOamMacPingHistorySapId_Type()
)
tmnxOamMacPingHistorySapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistorySapId.setStatus("current")
_TmnxOamMacPingHistorySdpId_Type = SdpId
_TmnxOamMacPingHistorySdpId_Object = MibTableColumn
tmnxOamMacPingHistorySdpId = _TmnxOamMacPingHistorySdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 12),
    _TmnxOamMacPingHistorySdpId_Type()
)
tmnxOamMacPingHistorySdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistorySdpId.setStatus("current")
_TmnxOamMacPingHistoryAdminStatus_Type = TruthValue
_TmnxOamMacPingHistoryAdminStatus_Object = MibTableColumn
tmnxOamMacPingHistoryAdminStatus = _TmnxOamMacPingHistoryAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 13),
    _TmnxOamMacPingHistoryAdminStatus_Type()
)
tmnxOamMacPingHistoryAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryAdminStatus.setStatus("current")
_TmnxOamMacPingHistoryOperStatus_Type = TruthValue
_TmnxOamMacPingHistoryOperStatus_Object = MibTableColumn
tmnxOamMacPingHistoryOperStatus = _TmnxOamMacPingHistoryOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 14),
    _TmnxOamMacPingHistoryOperStatus_Type()
)
tmnxOamMacPingHistoryOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryOperStatus.setStatus("current")
_TmnxOamMacPingHistoryResponsePlane_Type = TmnxOamTestResponsePlane
_TmnxOamMacPingHistoryResponsePlane_Object = MibTableColumn
tmnxOamMacPingHistoryResponsePlane = _TmnxOamMacPingHistoryResponsePlane_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 15),
    _TmnxOamMacPingHistoryResponsePlane_Type()
)
tmnxOamMacPingHistoryResponsePlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryResponsePlane.setStatus("current")
_TmnxOamMacPingHistorySize_Type = Unsigned32
_TmnxOamMacPingHistorySize_Object = MibTableColumn
tmnxOamMacPingHistorySize = _TmnxOamMacPingHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 16),
    _TmnxOamMacPingHistorySize_Type()
)
tmnxOamMacPingHistorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistorySize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistorySize.setUnits("octets")
_TmnxOamMacPingHistoryInOneWayTime_Type = Integer32
_TmnxOamMacPingHistoryInOneWayTime_Object = MibTableColumn
tmnxOamMacPingHistoryInOneWayTime = _TmnxOamMacPingHistoryInOneWayTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 17),
    _TmnxOamMacPingHistoryInOneWayTime_Type()
)
tmnxOamMacPingHistoryInOneWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryInOneWayTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistoryInOneWayTime.setUnits("milliseconds")
_TmnxOamMacPingHistorySrcAddrType_Type = InetAddressType
_TmnxOamMacPingHistorySrcAddrType_Object = MibTableColumn
tmnxOamMacPingHistorySrcAddrType = _TmnxOamMacPingHistorySrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 18),
    _TmnxOamMacPingHistorySrcAddrType_Type()
)
tmnxOamMacPingHistorySrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistorySrcAddrType.setStatus("current")


class _TmnxOamMacPingHistorySrcAddress_Type(InetAddress):
    """Custom type tmnxOamMacPingHistorySrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMacPingHistorySrcAddress_Type.__name__ = "InetAddress"
_TmnxOamMacPingHistorySrcAddress_Object = MibTableColumn
tmnxOamMacPingHistorySrcAddress = _TmnxOamMacPingHistorySrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 7, 1, 19),
    _TmnxOamMacPingHistorySrcAddress_Type()
)
tmnxOamMacPingHistorySrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingHistorySrcAddress.setStatus("current")
_TmnxOamMacPingL2MapTable_Object = MibTable
tmnxOamMacPingL2MapTable = _TmnxOamMacPingL2MapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapTable.setStatus("current")
_TmnxOamMacPingL2MapEntry_Object = MibTableRow
tmnxOamMacPingL2MapEntry = _TmnxOamMacPingL2MapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8, 1)
)
tmnxOamMacPingL2MapEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingReplyIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapEntry.setStatus("current")


class _TmnxOamMacPingL2MapIndex_Type(Unsigned32):
    """Custom type tmnxOamMacPingL2MapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamMacPingL2MapIndex_Type.__name__ = "Unsigned32"
_TmnxOamMacPingL2MapIndex_Object = MibTableColumn
tmnxOamMacPingL2MapIndex = _TmnxOamMacPingL2MapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8, 1, 1),
    _TmnxOamMacPingL2MapIndex_Type()
)
tmnxOamMacPingL2MapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapIndex.setStatus("current")
_TmnxOamMacPingL2MapRouterID_Type = IpAddress
_TmnxOamMacPingL2MapRouterID_Object = MibTableColumn
tmnxOamMacPingL2MapRouterID = _TmnxOamMacPingL2MapRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8, 1, 2),
    _TmnxOamMacPingL2MapRouterID_Type()
)
tmnxOamMacPingL2MapRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapRouterID.setStatus("current")
_TmnxOamMacPingL2MapLabel_Type = MplsLabel
_TmnxOamMacPingL2MapLabel_Object = MibTableColumn
tmnxOamMacPingL2MapLabel = _TmnxOamMacPingL2MapLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8, 1, 3),
    _TmnxOamMacPingL2MapLabel_Type()
)
tmnxOamMacPingL2MapLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapLabel.setStatus("current")
_TmnxOamMacPingL2MapProtocol_Type = TmnxOamSignalProtocol
_TmnxOamMacPingL2MapProtocol_Object = MibTableColumn
tmnxOamMacPingL2MapProtocol = _TmnxOamMacPingL2MapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8, 1, 4),
    _TmnxOamMacPingL2MapProtocol_Type()
)
tmnxOamMacPingL2MapProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapProtocol.setStatus("current")
_TmnxOamMacPingL2MapVCType_Type = TmnxOamVcType
_TmnxOamMacPingL2MapVCType_Object = MibTableColumn
tmnxOamMacPingL2MapVCType = _TmnxOamMacPingL2MapVCType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8, 1, 5),
    _TmnxOamMacPingL2MapVCType_Type()
)
tmnxOamMacPingL2MapVCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapVCType.setStatus("current")
_TmnxOamMacPingL2MapVCID_Type = TmnxVcId
_TmnxOamMacPingL2MapVCID_Object = MibTableColumn
tmnxOamMacPingL2MapVCID = _TmnxOamMacPingL2MapVCID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8, 1, 6),
    _TmnxOamMacPingL2MapVCID_Type()
)
tmnxOamMacPingL2MapVCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapVCID.setStatus("current")


class _TmnxOamMacPingL2MapDirection_Type(Integer32):
    """Custom type tmnxOamMacPingL2MapDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("upstream", 1))
    )


_TmnxOamMacPingL2MapDirection_Type.__name__ = "Integer32"
_TmnxOamMacPingL2MapDirection_Object = MibTableColumn
tmnxOamMacPingL2MapDirection = _TmnxOamMacPingL2MapDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 8, 1, 7),
    _TmnxOamMacPingL2MapDirection_Type()
)
tmnxOamMacPingL2MapDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapDirection.setStatus("current")
_TmnxOamLspPingCtlTable_Object = MibTable
tmnxOamLspPingCtlTable = _TmnxOamLspPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlTable.setStatus("current")
_TmnxOamLspPingCtlEntry_Object = MibTableRow
tmnxOamLspPingCtlEntry = _TmnxOamLspPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1)
)
tmnxOamLspPingCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlEntry.setStatus("current")


class _TmnxOamLspPingCtlVRtrID_Type(TmnxVRtrID):
    """Custom type tmnxOamLspPingCtlVRtrID based on TmnxVRtrID"""
    defaultValue = 1


_TmnxOamLspPingCtlVRtrID_Object = MibTableColumn
tmnxOamLspPingCtlVRtrID = _TmnxOamLspPingCtlVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 1),
    _TmnxOamLspPingCtlVRtrID_Type()
)
tmnxOamLspPingCtlVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlVRtrID.setStatus("current")


class _TmnxOamLspPingCtlLspName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamLspPingCtlLspName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamLspPingCtlLspName_Object = MibTableColumn
tmnxOamLspPingCtlLspName = _TmnxOamLspPingCtlLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 2),
    _TmnxOamLspPingCtlLspName_Type()
)
tmnxOamLspPingCtlLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlLspName.setStatus("current")


class _TmnxOamLspPingCtlReturnLsp_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamLspPingCtlReturnLsp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamLspPingCtlReturnLsp_Object = MibTableColumn
tmnxOamLspPingCtlReturnLsp = _TmnxOamLspPingCtlReturnLsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 3),
    _TmnxOamLspPingCtlReturnLsp_Type()
)
tmnxOamLspPingCtlReturnLsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlReturnLsp.setStatus("current")


class _TmnxOamLspPingCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamLspPingCtlTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamLspPingCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamLspPingCtlTtl_Object = MibTableColumn
tmnxOamLspPingCtlTtl = _TmnxOamLspPingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 4),
    _TmnxOamLspPingCtlTtl_Type()
)
tmnxOamLspPingCtlTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlTtl.setUnits("time-to-live value")


class _TmnxOamLspPingCtlPathName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamLspPingCtlPathName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamLspPingCtlPathName_Object = MibTableColumn
tmnxOamLspPingCtlPathName = _TmnxOamLspPingCtlPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 5),
    _TmnxOamLspPingCtlPathName_Type()
)
tmnxOamLspPingCtlPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlPathName.setStatus("current")


class _TmnxOamLspPingCtlLdpIpPrefix_Type(IpAddress):
    """Custom type tmnxOamLspPingCtlLdpIpPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamLspPingCtlLdpIpPrefix_Object = MibTableColumn
tmnxOamLspPingCtlLdpIpPrefix = _TmnxOamLspPingCtlLdpIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 6),
    _TmnxOamLspPingCtlLdpIpPrefix_Type()
)
tmnxOamLspPingCtlLdpIpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlLdpIpPrefix.setStatus("obsolete")


class _TmnxOamLspPingCtlLdpIpPrefixLen_Type(IpAddressPrefixLength):
    """Custom type tmnxOamLspPingCtlLdpIpPrefixLen based on IpAddressPrefixLength"""
    defaultValue = 32


_TmnxOamLspPingCtlLdpIpPrefixLen_Object = MibTableColumn
tmnxOamLspPingCtlLdpIpPrefixLen = _TmnxOamLspPingCtlLdpIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 7),
    _TmnxOamLspPingCtlLdpIpPrefixLen_Type()
)
tmnxOamLspPingCtlLdpIpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlLdpIpPrefixLen.setStatus("obsolete")


class _TmnxOamLspPingCtlLdpPrefixType_Type(InetAddressType):
    """Custom type tmnxOamLspPingCtlLdpPrefixType based on InetAddressType"""


_TmnxOamLspPingCtlLdpPrefixType_Object = MibTableColumn
tmnxOamLspPingCtlLdpPrefixType = _TmnxOamLspPingCtlLdpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 8),
    _TmnxOamLspPingCtlLdpPrefixType_Type()
)
tmnxOamLspPingCtlLdpPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlLdpPrefixType.setStatus("current")


class _TmnxOamLspPingCtlLdpPrefix_Type(InetAddress):
    """Custom type tmnxOamLspPingCtlLdpPrefix based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspPingCtlLdpPrefix_Type.__name__ = "InetAddress"
_TmnxOamLspPingCtlLdpPrefix_Object = MibTableColumn
tmnxOamLspPingCtlLdpPrefix = _TmnxOamLspPingCtlLdpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 9),
    _TmnxOamLspPingCtlLdpPrefix_Type()
)
tmnxOamLspPingCtlLdpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlLdpPrefix.setStatus("current")


class _TmnxOamLspPingCtlLdpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxOamLspPingCtlLdpPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 32


_TmnxOamLspPingCtlLdpPrefixLen_Object = MibTableColumn
tmnxOamLspPingCtlLdpPrefixLen = _TmnxOamLspPingCtlLdpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 10),
    _TmnxOamLspPingCtlLdpPrefixLen_Type()
)
tmnxOamLspPingCtlLdpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlLdpPrefixLen.setStatus("current")


class _TmnxOamLspPingCtlPathDestType_Type(InetAddressType):
    """Custom type tmnxOamLspPingCtlPathDestType based on InetAddressType"""


_TmnxOamLspPingCtlPathDestType_Object = MibTableColumn
tmnxOamLspPingCtlPathDestType = _TmnxOamLspPingCtlPathDestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 11),
    _TmnxOamLspPingCtlPathDestType_Type()
)
tmnxOamLspPingCtlPathDestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlPathDestType.setStatus("current")


class _TmnxOamLspPingCtlPathDest_Type(InetAddress):
    """Custom type tmnxOamLspPingCtlPathDest based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspPingCtlPathDest_Type.__name__ = "InetAddress"
_TmnxOamLspPingCtlPathDest_Object = MibTableColumn
tmnxOamLspPingCtlPathDest = _TmnxOamLspPingCtlPathDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 12),
    _TmnxOamLspPingCtlPathDest_Type()
)
tmnxOamLspPingCtlPathDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlPathDest.setStatus("current")


class _TmnxOamLspPingCtlNhIntfName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamLspPingCtlNhIntfName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamLspPingCtlNhIntfName_Object = MibTableColumn
tmnxOamLspPingCtlNhIntfName = _TmnxOamLspPingCtlNhIntfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 13),
    _TmnxOamLspPingCtlNhIntfName_Type()
)
tmnxOamLspPingCtlNhIntfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlNhIntfName.setStatus("current")


class _TmnxOamLspPingCtlNhAddressType_Type(InetAddressType):
    """Custom type tmnxOamLspPingCtlNhAddressType based on InetAddressType"""


_TmnxOamLspPingCtlNhAddressType_Object = MibTableColumn
tmnxOamLspPingCtlNhAddressType = _TmnxOamLspPingCtlNhAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 14),
    _TmnxOamLspPingCtlNhAddressType_Type()
)
tmnxOamLspPingCtlNhAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlNhAddressType.setStatus("current")


class _TmnxOamLspPingCtlNhAddress_Type(InetAddress):
    """Custom type tmnxOamLspPingCtlNhAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspPingCtlNhAddress_Type.__name__ = "InetAddress"
_TmnxOamLspPingCtlNhAddress_Object = MibTableColumn
tmnxOamLspPingCtlNhAddress = _TmnxOamLspPingCtlNhAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 9, 1, 15),
    _TmnxOamLspPingCtlNhAddress_Type()
)
tmnxOamLspPingCtlNhAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspPingCtlNhAddress.setStatus("current")
_TmnxOamVprnPingCtlTable_Object = MibTable
tmnxOamVprnPingCtlTable = _TmnxOamVprnPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxOamVprnPingCtlTable.setStatus("current")
_TmnxOamVprnPingCtlEntry_Object = MibTableRow
tmnxOamVprnPingCtlEntry = _TmnxOamVprnPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 10, 1)
)
tmnxOamVprnPingCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVprnPingCtlEntry.setStatus("current")


class _TmnxOamVprnPingCtlSourceIpAddr_Type(IpAddress):
    """Custom type tmnxOamVprnPingCtlSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamVprnPingCtlSourceIpAddr_Object = MibTableColumn
tmnxOamVprnPingCtlSourceIpAddr = _TmnxOamVprnPingCtlSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 10, 1, 1),
    _TmnxOamVprnPingCtlSourceIpAddr_Type()
)
tmnxOamVprnPingCtlSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnPingCtlSourceIpAddr.setStatus("obsolete")


class _TmnxOamVprnPingCtlReplyControl_Type(TruthValue):
    """Custom type tmnxOamVprnPingCtlReplyControl based on TruthValue"""


_TmnxOamVprnPingCtlReplyControl_Object = MibTableColumn
tmnxOamVprnPingCtlReplyControl = _TmnxOamVprnPingCtlReplyControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 10, 1, 2),
    _TmnxOamVprnPingCtlReplyControl_Type()
)
tmnxOamVprnPingCtlReplyControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnPingCtlReplyControl.setStatus("current")


class _TmnxOamVprnPingCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamVprnPingCtlTtl based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamVprnPingCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamVprnPingCtlTtl_Object = MibTableColumn
tmnxOamVprnPingCtlTtl = _TmnxOamVprnPingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 10, 1, 3),
    _TmnxOamVprnPingCtlTtl_Type()
)
tmnxOamVprnPingCtlTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnPingCtlTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamVprnPingCtlTtl.setUnits("time-to-live value")


class _TmnxOamVprnPingCtlSrcAddrType_Type(InetAddressType):
    """Custom type tmnxOamVprnPingCtlSrcAddrType based on InetAddressType"""


_TmnxOamVprnPingCtlSrcAddrType_Object = MibTableColumn
tmnxOamVprnPingCtlSrcAddrType = _TmnxOamVprnPingCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 10, 1, 4),
    _TmnxOamVprnPingCtlSrcAddrType_Type()
)
tmnxOamVprnPingCtlSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnPingCtlSrcAddrType.setStatus("current")


class _TmnxOamVprnPingCtlSrcAddress_Type(InetAddress):
    """Custom type tmnxOamVprnPingCtlSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVprnPingCtlSrcAddress_Type.__name__ = "InetAddress"
_TmnxOamVprnPingCtlSrcAddress_Object = MibTableColumn
tmnxOamVprnPingCtlSrcAddress = _TmnxOamVprnPingCtlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 10, 1, 5),
    _TmnxOamVprnPingCtlSrcAddress_Type()
)
tmnxOamVprnPingCtlSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnPingCtlSrcAddress.setStatus("current")
_TmnxOamAtmPingCtlTable_Object = MibTable
tmnxOamAtmPingCtlTable = _TmnxOamAtmPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxOamAtmPingCtlTable.setStatus("current")
_TmnxOamAtmPingCtlEntry_Object = MibTableRow
tmnxOamAtmPingCtlEntry = _TmnxOamAtmPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 11, 1)
)
tmnxOamAtmPingCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamAtmPingCtlEntry.setStatus("current")


class _TmnxOamAtmPingCtlPortId_Type(TmnxPortID):
    """Custom type tmnxOamAtmPingCtlPortId based on TmnxPortID"""
    defaultValue = 0


_TmnxOamAtmPingCtlPortId_Object = MibTableColumn
tmnxOamAtmPingCtlPortId = _TmnxOamAtmPingCtlPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 11, 1, 1),
    _TmnxOamAtmPingCtlPortId_Type()
)
tmnxOamAtmPingCtlPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAtmPingCtlPortId.setStatus("current")


class _TmnxOamAtmPingCtlVpi_Type(AtmVpIdentifier):
    """Custom type tmnxOamAtmPingCtlVpi based on AtmVpIdentifier"""
    defaultValue = 0


_TmnxOamAtmPingCtlVpi_Object = MibTableColumn
tmnxOamAtmPingCtlVpi = _TmnxOamAtmPingCtlVpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 11, 1, 2),
    _TmnxOamAtmPingCtlVpi_Type()
)
tmnxOamAtmPingCtlVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAtmPingCtlVpi.setStatus("current")


class _TmnxOamAtmPingCtlVci_Type(AtmVcIdentifier):
    """Custom type tmnxOamAtmPingCtlVci based on AtmVcIdentifier"""
    defaultValue = 0


_TmnxOamAtmPingCtlVci_Object = MibTableColumn
tmnxOamAtmPingCtlVci = _TmnxOamAtmPingCtlVci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 11, 1, 3),
    _TmnxOamAtmPingCtlVci_Type()
)
tmnxOamAtmPingCtlVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAtmPingCtlVci.setStatus("current")


class _TmnxOamAtmPingCtlLpbkLocation_Type(OctetString):
    """Custom type tmnxOamAtmPingCtlLpbkLocation based on OctetString"""
    defaultHexValue = "00000000000000000000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_TmnxOamAtmPingCtlLpbkLocation_Type.__name__ = "OctetString"
_TmnxOamAtmPingCtlLpbkLocation_Object = MibTableColumn
tmnxOamAtmPingCtlLpbkLocation = _TmnxOamAtmPingCtlLpbkLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 11, 1, 4),
    _TmnxOamAtmPingCtlLpbkLocation_Type()
)
tmnxOamAtmPingCtlLpbkLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAtmPingCtlLpbkLocation.setStatus("current")


class _TmnxOamAtmPingCtlSegment_Type(Integer32):
    """Custom type tmnxOamAtmPingCtlSegment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endToEnd", 1),
          ("segment", 2))
    )


_TmnxOamAtmPingCtlSegment_Type.__name__ = "Integer32"
_TmnxOamAtmPingCtlSegment_Object = MibTableColumn
tmnxOamAtmPingCtlSegment = _TmnxOamAtmPingCtlSegment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 11, 1, 5),
    _TmnxOamAtmPingCtlSegment_Type()
)
tmnxOamAtmPingCtlSegment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAtmPingCtlSegment.setStatus("current")
_TmnxOamMfibPingCtlTable_Object = MibTable
tmnxOamMfibPingCtlTable = _TmnxOamMfibPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlTable.setStatus("current")
_TmnxOamMfibPingCtlEntry_Object = MibTableRow
tmnxOamMfibPingCtlEntry = _TmnxOamMfibPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1)
)
tmnxOamMfibPingCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlEntry.setStatus("current")


class _TmnxOamMfibPingCtlSourceIpAddr_Type(IpAddress):
    """Custom type tmnxOamMfibPingCtlSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamMfibPingCtlSourceIpAddr_Object = MibTableColumn
tmnxOamMfibPingCtlSourceIpAddr = _TmnxOamMfibPingCtlSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 1),
    _TmnxOamMfibPingCtlSourceIpAddr_Type()
)
tmnxOamMfibPingCtlSourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlSourceIpAddr.setStatus("obsolete")


class _TmnxOamMfibPingCtlDestIpAddr_Type(IpAddress):
    """Custom type tmnxOamMfibPingCtlDestIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamMfibPingCtlDestIpAddr_Object = MibTableColumn
tmnxOamMfibPingCtlDestIpAddr = _TmnxOamMfibPingCtlDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 2),
    _TmnxOamMfibPingCtlDestIpAddr_Type()
)
tmnxOamMfibPingCtlDestIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlDestIpAddr.setStatus("obsolete")


class _TmnxOamMfibPingCtlReplyControl_Type(TruthValue):
    """Custom type tmnxOamMfibPingCtlReplyControl based on TruthValue"""


_TmnxOamMfibPingCtlReplyControl_Object = MibTableColumn
tmnxOamMfibPingCtlReplyControl = _TmnxOamMfibPingCtlReplyControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 3),
    _TmnxOamMfibPingCtlReplyControl_Type()
)
tmnxOamMfibPingCtlReplyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlReplyControl.setStatus("current")


class _TmnxOamMfibPingCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamMfibPingCtlTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamMfibPingCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamMfibPingCtlTtl_Object = MibTableColumn
tmnxOamMfibPingCtlTtl = _TmnxOamMfibPingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 4),
    _TmnxOamMfibPingCtlTtl_Type()
)
tmnxOamMfibPingCtlTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlTtl.setUnits("time-to-live value")


class _TmnxOamMfibPingCtlSrcAddrType_Type(InetAddressType):
    """Custom type tmnxOamMfibPingCtlSrcAddrType based on InetAddressType"""


_TmnxOamMfibPingCtlSrcAddrType_Object = MibTableColumn
tmnxOamMfibPingCtlSrcAddrType = _TmnxOamMfibPingCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 5),
    _TmnxOamMfibPingCtlSrcAddrType_Type()
)
tmnxOamMfibPingCtlSrcAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlSrcAddrType.setStatus("current")


class _TmnxOamMfibPingCtlSrcAddress_Type(InetAddress):
    """Custom type tmnxOamMfibPingCtlSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMfibPingCtlSrcAddress_Type.__name__ = "InetAddress"
_TmnxOamMfibPingCtlSrcAddress_Object = MibTableColumn
tmnxOamMfibPingCtlSrcAddress = _TmnxOamMfibPingCtlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 6),
    _TmnxOamMfibPingCtlSrcAddress_Type()
)
tmnxOamMfibPingCtlSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlSrcAddress.setStatus("current")


class _TmnxOamMfibPingCtlDestAddrType_Type(InetAddressType):
    """Custom type tmnxOamMfibPingCtlDestAddrType based on InetAddressType"""


_TmnxOamMfibPingCtlDestAddrType_Object = MibTableColumn
tmnxOamMfibPingCtlDestAddrType = _TmnxOamMfibPingCtlDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 7),
    _TmnxOamMfibPingCtlDestAddrType_Type()
)
tmnxOamMfibPingCtlDestAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlDestAddrType.setStatus("current")


class _TmnxOamMfibPingCtlDestAddress_Type(InetAddress):
    """Custom type tmnxOamMfibPingCtlDestAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMfibPingCtlDestAddress_Type.__name__ = "InetAddress"
_TmnxOamMfibPingCtlDestAddress_Object = MibTableColumn
tmnxOamMfibPingCtlDestAddress = _TmnxOamMfibPingCtlDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 8),
    _TmnxOamMfibPingCtlDestAddress_Type()
)
tmnxOamMfibPingCtlDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlDestAddress.setStatus("current")


class _TmnxOamMfibPingCtlDestMacAddr_Type(MacAddress):
    """Custom type tmnxOamMfibPingCtlDestMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamMfibPingCtlDestMacAddr_Object = MibTableColumn
tmnxOamMfibPingCtlDestMacAddr = _TmnxOamMfibPingCtlDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 12, 1, 9),
    _TmnxOamMfibPingCtlDestMacAddr_Type()
)
tmnxOamMfibPingCtlDestMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamMfibPingCtlDestMacAddr.setStatus("current")
_TmnxOamCpePingCtlTable_Object = MibTable
tmnxOamCpePingCtlTable = _TmnxOamCpePingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13)
)
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlTable.setStatus("current")
_TmnxOamCpePingCtlEntry_Object = MibTableRow
tmnxOamCpePingCtlEntry = _TmnxOamCpePingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13, 1)
)
tmnxOamCpePingCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlEntry.setStatus("current")


class _TmnxOamCpePingCtlSourceIpAddr_Type(IpAddress):
    """Custom type tmnxOamCpePingCtlSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamCpePingCtlSourceIpAddr_Object = MibTableColumn
tmnxOamCpePingCtlSourceIpAddr = _TmnxOamCpePingCtlSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13, 1, 1),
    _TmnxOamCpePingCtlSourceIpAddr_Type()
)
tmnxOamCpePingCtlSourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlSourceIpAddr.setStatus("obsolete")


class _TmnxOamCpePingCtlSendControl_Type(TruthValue):
    """Custom type tmnxOamCpePingCtlSendControl based on TruthValue"""


_TmnxOamCpePingCtlSendControl_Object = MibTableColumn
tmnxOamCpePingCtlSendControl = _TmnxOamCpePingCtlSendControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13, 1, 2),
    _TmnxOamCpePingCtlSendControl_Type()
)
tmnxOamCpePingCtlSendControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlSendControl.setStatus("current")


class _TmnxOamCpePingCtlReplyControl_Type(TruthValue):
    """Custom type tmnxOamCpePingCtlReplyControl based on TruthValue"""


_TmnxOamCpePingCtlReplyControl_Object = MibTableColumn
tmnxOamCpePingCtlReplyControl = _TmnxOamCpePingCtlReplyControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13, 1, 3),
    _TmnxOamCpePingCtlReplyControl_Type()
)
tmnxOamCpePingCtlReplyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlReplyControl.setStatus("current")


class _TmnxOamCpePingCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamCpePingCtlTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamCpePingCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamCpePingCtlTtl_Object = MibTableColumn
tmnxOamCpePingCtlTtl = _TmnxOamCpePingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13, 1, 4),
    _TmnxOamCpePingCtlTtl_Type()
)
tmnxOamCpePingCtlTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlTtl.setUnits("time-to-live value")


class _TmnxOamCpePingCtlSrceMacAddr_Type(MacAddress):
    """Custom type tmnxOamCpePingCtlSrceMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamCpePingCtlSrceMacAddr_Object = MibTableColumn
tmnxOamCpePingCtlSrceMacAddr = _TmnxOamCpePingCtlSrceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13, 1, 5),
    _TmnxOamCpePingCtlSrceMacAddr_Type()
)
tmnxOamCpePingCtlSrceMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlSrceMacAddr.setStatus("current")


class _TmnxOamCpePingCtlSrcAddrType_Type(InetAddressType):
    """Custom type tmnxOamCpePingCtlSrcAddrType based on InetAddressType"""


_TmnxOamCpePingCtlSrcAddrType_Object = MibTableColumn
tmnxOamCpePingCtlSrcAddrType = _TmnxOamCpePingCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13, 1, 6),
    _TmnxOamCpePingCtlSrcAddrType_Type()
)
tmnxOamCpePingCtlSrcAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlSrcAddrType.setStatus("current")


class _TmnxOamCpePingCtlSrcAddress_Type(InetAddress):
    """Custom type tmnxOamCpePingCtlSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamCpePingCtlSrcAddress_Type.__name__ = "InetAddress"
_TmnxOamCpePingCtlSrcAddress_Object = MibTableColumn
tmnxOamCpePingCtlSrcAddress = _TmnxOamCpePingCtlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 13, 1, 7),
    _TmnxOamCpePingCtlSrcAddress_Type()
)
tmnxOamCpePingCtlSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamCpePingCtlSrcAddress.setStatus("current")
_TmnxOamMRInfoRespTable_Object = MibTable
tmnxOamMRInfoRespTable = _TmnxOamMRInfoRespTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 14)
)
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespTable.setStatus("current")
_TmnxOamMRInfoRespEntry_Object = MibTableRow
tmnxOamMRInfoRespEntry = _TmnxOamMRInfoRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 14, 1)
)
tmnxOamMRInfoRespEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespEntry.setStatus("current")


class _TmnxOamMRInfoRespCapabilities_Type(Bits):
    """Custom type tmnxOamMRInfoRespCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("genid", 2),
          ("leaf", 0),
          ("mtrace", 3),
          ("prune", 1),
          ("snmp", 4))
    )

_TmnxOamMRInfoRespCapabilities_Type.__name__ = "Bits"
_TmnxOamMRInfoRespCapabilities_Object = MibTableColumn
tmnxOamMRInfoRespCapabilities = _TmnxOamMRInfoRespCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 14, 1, 1),
    _TmnxOamMRInfoRespCapabilities_Type()
)
tmnxOamMRInfoRespCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespCapabilities.setStatus("current")
_TmnxOamMRInfoRespMinorVersion_Type = Unsigned32
_TmnxOamMRInfoRespMinorVersion_Object = MibTableColumn
tmnxOamMRInfoRespMinorVersion = _TmnxOamMRInfoRespMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 14, 1, 2),
    _TmnxOamMRInfoRespMinorVersion_Type()
)
tmnxOamMRInfoRespMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespMinorVersion.setStatus("current")
_TmnxOamMRInfoRespMajorVersion_Type = Unsigned32
_TmnxOamMRInfoRespMajorVersion_Object = MibTableColumn
tmnxOamMRInfoRespMajorVersion = _TmnxOamMRInfoRespMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 14, 1, 3),
    _TmnxOamMRInfoRespMajorVersion_Type()
)
tmnxOamMRInfoRespMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespMajorVersion.setStatus("current")
_TmnxOamMRInfoRespNumInterfaces_Type = Unsigned32
_TmnxOamMRInfoRespNumInterfaces_Object = MibTableColumn
tmnxOamMRInfoRespNumInterfaces = _TmnxOamMRInfoRespNumInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 14, 1, 4),
    _TmnxOamMRInfoRespNumInterfaces_Type()
)
tmnxOamMRInfoRespNumInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespNumInterfaces.setStatus("current")
_TmnxOamMRInfoRespIfTable_Object = MibTable
tmnxOamMRInfoRespIfTable = _TmnxOamMRInfoRespIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15)
)
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfTable.setStatus("current")
_TmnxOamMRInfoRespIfEntry_Object = MibTableRow
tmnxOamMRInfoRespIfEntry = _TmnxOamMRInfoRespIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1)
)
tmnxOamMRInfoRespIfEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfEntry.setStatus("current")
_TmnxOamMRInfoRespIfIndex_Type = Unsigned32
_TmnxOamMRInfoRespIfIndex_Object = MibTableColumn
tmnxOamMRInfoRespIfIndex = _TmnxOamMRInfoRespIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1, 1),
    _TmnxOamMRInfoRespIfIndex_Type()
)
tmnxOamMRInfoRespIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfIndex.setStatus("current")
_TmnxOamMRInfoRespIfAddress_Type = IpAddress
_TmnxOamMRInfoRespIfAddress_Object = MibTableColumn
tmnxOamMRInfoRespIfAddress = _TmnxOamMRInfoRespIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1, 2),
    _TmnxOamMRInfoRespIfAddress_Type()
)
tmnxOamMRInfoRespIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfAddress.setStatus("obsolete")
_TmnxOamMRInfoRespIfMetric_Type = Unsigned32
_TmnxOamMRInfoRespIfMetric_Object = MibTableColumn
tmnxOamMRInfoRespIfMetric = _TmnxOamMRInfoRespIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1, 3),
    _TmnxOamMRInfoRespIfMetric_Type()
)
tmnxOamMRInfoRespIfMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfMetric.setStatus("current")
_TmnxOamMRInfoRespIfThreshold_Type = Unsigned32
_TmnxOamMRInfoRespIfThreshold_Object = MibTableColumn
tmnxOamMRInfoRespIfThreshold = _TmnxOamMRInfoRespIfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1, 4),
    _TmnxOamMRInfoRespIfThreshold_Type()
)
tmnxOamMRInfoRespIfThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfThreshold.setStatus("current")


class _TmnxOamMRInfoRespIfFlags_Type(Bits):
    """Custom type tmnxOamMRInfoRespIfFlags based on Bits"""
    namedValues = NamedValues(
        *(("disabled", 5),
          ("down", 4),
          ("leaf", 7),
          ("querier", 6),
          ("reserved1", 2),
          ("reserved2", 3),
          ("srcrt", 1),
          ("tunnel", 0))
    )

_TmnxOamMRInfoRespIfFlags_Type.__name__ = "Bits"
_TmnxOamMRInfoRespIfFlags_Object = MibTableColumn
tmnxOamMRInfoRespIfFlags = _TmnxOamMRInfoRespIfFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1, 5),
    _TmnxOamMRInfoRespIfFlags_Type()
)
tmnxOamMRInfoRespIfFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfFlags.setStatus("current")
_TmnxOamMRInfoRespIfNbrCount_Type = Unsigned32
_TmnxOamMRInfoRespIfNbrCount_Object = MibTableColumn
tmnxOamMRInfoRespIfNbrCount = _TmnxOamMRInfoRespIfNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1, 6),
    _TmnxOamMRInfoRespIfNbrCount_Type()
)
tmnxOamMRInfoRespIfNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfNbrCount.setStatus("current")
_TmnxOamMRInfoRespIfAddrType_Type = InetAddressType
_TmnxOamMRInfoRespIfAddrType_Object = MibTableColumn
tmnxOamMRInfoRespIfAddrType = _TmnxOamMRInfoRespIfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1, 7),
    _TmnxOamMRInfoRespIfAddrType_Type()
)
tmnxOamMRInfoRespIfAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfAddrType.setStatus("current")


class _TmnxOamMRInfoRespIfAddr_Type(InetAddress):
    """Custom type tmnxOamMRInfoRespIfAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMRInfoRespIfAddr_Type.__name__ = "InetAddress"
_TmnxOamMRInfoRespIfAddr_Object = MibTableColumn
tmnxOamMRInfoRespIfAddr = _TmnxOamMRInfoRespIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 15, 1, 8),
    _TmnxOamMRInfoRespIfAddr_Type()
)
tmnxOamMRInfoRespIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfAddr.setStatus("current")
_TmnxOamMRInfoRespIfNbrTable_Object = MibTable
tmnxOamMRInfoRespIfNbrTable = _TmnxOamMRInfoRespIfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 16)
)
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfNbrTable.setStatus("current")
_TmnxOamMRInfoRespIfNbrEntry_Object = MibTableRow
tmnxOamMRInfoRespIfNbrEntry = _TmnxOamMRInfoRespIfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 16, 1)
)
tmnxOamMRInfoRespIfNbrEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfNbrIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfNbrEntry.setStatus("current")
_TmnxOamMRInfoRespIfNbrIndex_Type = Unsigned32
_TmnxOamMRInfoRespIfNbrIndex_Object = MibTableColumn
tmnxOamMRInfoRespIfNbrIndex = _TmnxOamMRInfoRespIfNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 16, 1, 1),
    _TmnxOamMRInfoRespIfNbrIndex_Type()
)
tmnxOamMRInfoRespIfNbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfNbrIndex.setStatus("current")
_TmnxOamMRInfoRespIfNbrAddress_Type = IpAddress
_TmnxOamMRInfoRespIfNbrAddress_Object = MibTableColumn
tmnxOamMRInfoRespIfNbrAddress = _TmnxOamMRInfoRespIfNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 16, 1, 2),
    _TmnxOamMRInfoRespIfNbrAddress_Type()
)
tmnxOamMRInfoRespIfNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfNbrAddress.setStatus("obsolete")
_TmnxOamMRInfoRespIfNbrAddrType_Type = InetAddressType
_TmnxOamMRInfoRespIfNbrAddrType_Object = MibTableColumn
tmnxOamMRInfoRespIfNbrAddrType = _TmnxOamMRInfoRespIfNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 16, 1, 3),
    _TmnxOamMRInfoRespIfNbrAddrType_Type()
)
tmnxOamMRInfoRespIfNbrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfNbrAddrType.setStatus("current")


class _TmnxOamMRInfoRespIfNbrAddr_Type(InetAddress):
    """Custom type tmnxOamMRInfoRespIfNbrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMRInfoRespIfNbrAddr_Type.__name__ = "InetAddress"
_TmnxOamMRInfoRespIfNbrAddr_Object = MibTableColumn
tmnxOamMRInfoRespIfNbrAddr = _TmnxOamMRInfoRespIfNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 16, 1, 4),
    _TmnxOamMRInfoRespIfNbrAddr_Type()
)
tmnxOamMRInfoRespIfNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMRInfoRespIfNbrAddr.setStatus("current")
_TmnxOamVccvPingCtlTable_Object = MibTable
tmnxOamVccvPingCtlTable = _TmnxOamVccvPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17)
)
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlTable.setStatus("current")
_TmnxOamVccvPingCtlEntry_Object = MibTableRow
tmnxOamVccvPingCtlEntry = _TmnxOamVccvPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1)
)
tmnxOamVccvPingCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlEntry.setStatus("current")


class _TmnxOamVccvPingCtlSdpIdVcId_Type(SdpBindId):
    """Custom type tmnxOamVccvPingCtlSdpIdVcId based on SdpBindId"""
    defaultHexValue = "0000000000000000"


_TmnxOamVccvPingCtlSdpIdVcId_Object = MibTableColumn
tmnxOamVccvPingCtlSdpIdVcId = _TmnxOamVccvPingCtlSdpIdVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 1),
    _TmnxOamVccvPingCtlSdpIdVcId_Type()
)
tmnxOamVccvPingCtlSdpIdVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlSdpIdVcId.setStatus("current")


class _TmnxOamVccvPingCtlReplyMode_Type(Integer32):
    """Custom type tmnxOamVccvPingCtlReplyMode based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("controlChannel", 4),
          ("ip", 2))
    )


_TmnxOamVccvPingCtlReplyMode_Type.__name__ = "Integer32"
_TmnxOamVccvPingCtlReplyMode_Object = MibTableColumn
tmnxOamVccvPingCtlReplyMode = _TmnxOamVccvPingCtlReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 2),
    _TmnxOamVccvPingCtlReplyMode_Type()
)
tmnxOamVccvPingCtlReplyMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlReplyMode.setStatus("current")


class _TmnxOamVccvPingCtlPwId_Type(TmnxVcIdOrNone):
    """Custom type tmnxOamVccvPingCtlPwId based on TmnxVcIdOrNone"""
    defaultValue = 0


_TmnxOamVccvPingCtlPwId_Object = MibTableColumn
tmnxOamVccvPingCtlPwId = _TmnxOamVccvPingCtlPwId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 3),
    _TmnxOamVccvPingCtlPwId_Type()
)
tmnxOamVccvPingCtlPwId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlPwId.setStatus("current")


class _TmnxOamVccvPingCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamVccvPingCtlTtl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamVccvPingCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamVccvPingCtlTtl_Object = MibTableColumn
tmnxOamVccvPingCtlTtl = _TmnxOamVccvPingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 17, 1, 4),
    _TmnxOamVccvPingCtlTtl_Type()
)
tmnxOamVccvPingCtlTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamVccvPingCtlTtl.setUnits("time-to-live value")
_TmnxOamIcmpPingCtlTable_Object = MibTable
tmnxOamIcmpPingCtlTable = _TmnxOamIcmpPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18)
)
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlTable.setStatus("current")
_TmnxOamIcmpPingCtlEntry_Object = MibTableRow
tmnxOamIcmpPingCtlEntry = _TmnxOamIcmpPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1)
)
tmnxOamIcmpPingCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlEntry.setStatus("current")


class _TmnxOamIcmpPingCtlRapid_Type(TruthValue):
    """Custom type tmnxOamIcmpPingCtlRapid based on TruthValue"""


_TmnxOamIcmpPingCtlRapid_Object = MibTableColumn
tmnxOamIcmpPingCtlRapid = _TmnxOamIcmpPingCtlRapid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 1),
    _TmnxOamIcmpPingCtlRapid_Type()
)
tmnxOamIcmpPingCtlRapid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlRapid.setStatus("current")


class _TmnxOamIcmpPingCtlTtl_Type(Unsigned32):
    """Custom type tmnxOamIcmpPingCtlTtl based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TmnxOamIcmpPingCtlTtl_Type.__name__ = "Unsigned32"
_TmnxOamIcmpPingCtlTtl_Object = MibTableColumn
tmnxOamIcmpPingCtlTtl = _TmnxOamIcmpPingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 2),
    _TmnxOamIcmpPingCtlTtl_Type()
)
tmnxOamIcmpPingCtlTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlTtl.setStatus("current")


class _TmnxOamIcmpPingCtlDSField_Type(Unsigned32):
    """Custom type tmnxOamIcmpPingCtlDSField based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxOamIcmpPingCtlDSField_Type.__name__ = "Unsigned32"
_TmnxOamIcmpPingCtlDSField_Object = MibTableColumn
tmnxOamIcmpPingCtlDSField = _TmnxOamIcmpPingCtlDSField_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 3),
    _TmnxOamIcmpPingCtlDSField_Type()
)
tmnxOamIcmpPingCtlDSField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlDSField.setStatus("current")


class _TmnxOamIcmpPingCtlPattern_Type(Integer32):
    """Custom type tmnxOamIcmpPingCtlPattern based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TmnxOamIcmpPingCtlPattern_Type.__name__ = "Integer32"
_TmnxOamIcmpPingCtlPattern_Object = MibTableColumn
tmnxOamIcmpPingCtlPattern = _TmnxOamIcmpPingCtlPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 4),
    _TmnxOamIcmpPingCtlPattern_Type()
)
tmnxOamIcmpPingCtlPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlPattern.setStatus("current")


class _TmnxOamIcmpPingCtlNhAddrType_Type(InetAddressType):
    """Custom type tmnxOamIcmpPingCtlNhAddrType based on InetAddressType"""


_TmnxOamIcmpPingCtlNhAddrType_Object = MibTableColumn
tmnxOamIcmpPingCtlNhAddrType = _TmnxOamIcmpPingCtlNhAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 5),
    _TmnxOamIcmpPingCtlNhAddrType_Type()
)
tmnxOamIcmpPingCtlNhAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlNhAddrType.setStatus("current")


class _TmnxOamIcmpPingCtlNhAddress_Type(InetAddress):
    """Custom type tmnxOamIcmpPingCtlNhAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamIcmpPingCtlNhAddress_Type.__name__ = "InetAddress"
_TmnxOamIcmpPingCtlNhAddress_Object = MibTableColumn
tmnxOamIcmpPingCtlNhAddress = _TmnxOamIcmpPingCtlNhAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 6),
    _TmnxOamIcmpPingCtlNhAddress_Type()
)
tmnxOamIcmpPingCtlNhAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlNhAddress.setStatus("current")


class _TmnxOamIcmpPingCtlEgrIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxOamIcmpPingCtlEgrIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxOamIcmpPingCtlEgrIfIndex_Object = MibTableColumn
tmnxOamIcmpPingCtlEgrIfIndex = _TmnxOamIcmpPingCtlEgrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 7),
    _TmnxOamIcmpPingCtlEgrIfIndex_Type()
)
tmnxOamIcmpPingCtlEgrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlEgrIfIndex.setStatus("current")


class _TmnxOamIcmpPingCtlBypassRouting_Type(TruthValue):
    """Custom type tmnxOamIcmpPingCtlBypassRouting based on TruthValue"""


_TmnxOamIcmpPingCtlBypassRouting_Object = MibTableColumn
tmnxOamIcmpPingCtlBypassRouting = _TmnxOamIcmpPingCtlBypassRouting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 8),
    _TmnxOamIcmpPingCtlBypassRouting_Type()
)
tmnxOamIcmpPingCtlBypassRouting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlBypassRouting.setStatus("current")


class _TmnxOamIcmpPingCtlDoNotFragment_Type(TruthValue):
    """Custom type tmnxOamIcmpPingCtlDoNotFragment based on TruthValue"""


_TmnxOamIcmpPingCtlDoNotFragment_Object = MibTableColumn
tmnxOamIcmpPingCtlDoNotFragment = _TmnxOamIcmpPingCtlDoNotFragment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 18, 1, 9),
    _TmnxOamIcmpPingCtlDoNotFragment_Type()
)
tmnxOamIcmpPingCtlDoNotFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamIcmpPingCtlDoNotFragment.setStatus("current")
_TmnxOamAncpTestCtlTable_Object = MibTable
tmnxOamAncpTestCtlTable = _TmnxOamAncpTestCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 19)
)
if mibBuilder.loadTexts:
    tmnxOamAncpTestCtlTable.setStatus("current")
_TmnxOamAncpTestCtlEntry_Object = MibTableRow
tmnxOamAncpTestCtlEntry = _TmnxOamAncpTestCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 19, 1)
)
tmnxOamAncpTestCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamAncpTestCtlEntry.setStatus("current")


class _TmnxOamAncpTestTarget_Type(Integer32):
    """Custom type tmnxOamAncpTestTarget based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ancpString", 2),
          ("none", 0),
          ("subscriberId", 1))
    )


_TmnxOamAncpTestTarget_Type.__name__ = "Integer32"
_TmnxOamAncpTestTarget_Object = MibTableColumn
tmnxOamAncpTestTarget = _TmnxOamAncpTestTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 19, 1, 1),
    _TmnxOamAncpTestTarget_Type()
)
tmnxOamAncpTestTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAncpTestTarget.setStatus("current")


class _TmnxOamAncpTestTargetId_Type(DisplayString):
    """Custom type tmnxOamAncpTestTargetId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TmnxOamAncpTestTargetId_Type.__name__ = "DisplayString"
_TmnxOamAncpTestTargetId_Object = MibTableColumn
tmnxOamAncpTestTargetId = _TmnxOamAncpTestTargetId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 19, 1, 2),
    _TmnxOamAncpTestTargetId_Type()
)
tmnxOamAncpTestTargetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAncpTestTargetId.setStatus("current")


class _TmnxOamAncpTestcount_Type(Integer32):
    """Custom type tmnxOamAncpTestcount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxOamAncpTestcount_Type.__name__ = "Integer32"
_TmnxOamAncpTestcount_Object = MibTableColumn
tmnxOamAncpTestcount = _TmnxOamAncpTestcount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 19, 1, 3),
    _TmnxOamAncpTestcount_Type()
)
tmnxOamAncpTestcount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAncpTestcount.setStatus("current")


class _TmnxOamAncpTestTimeout_Type(Integer32):
    """Custom type tmnxOamAncpTestTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxOamAncpTestTimeout_Type.__name__ = "Integer32"
_TmnxOamAncpTestTimeout_Object = MibTableColumn
tmnxOamAncpTestTimeout = _TmnxOamAncpTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 19, 1, 4),
    _TmnxOamAncpTestTimeout_Type()
)
tmnxOamAncpTestTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamAncpTestTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamAncpTestTimeout.setUnits("seconds")
_TmnxOamAncpTestHistoryTable_Object = MibTable
tmnxOamAncpTestHistoryTable = _TmnxOamAncpTestHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 20)
)
if mibBuilder.loadTexts:
    tmnxOamAncpTestHistoryTable.setStatus("current")
_TmnxOamAncpTestHistoryEntry_Object = MibTableRow
tmnxOamAncpTestHistoryEntry = _TmnxOamAncpTestHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 20, 1)
)
tmnxOamAncpTestHistoryEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTestRunIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamAncpHistoryIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamAncpTestHistoryEntry.setStatus("current")


class _TmnxOamAncpHistoryIndex_Type(Unsigned32):
    """Custom type tmnxOamAncpHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamAncpHistoryIndex_Type.__name__ = "Unsigned32"
_TmnxOamAncpHistoryIndex_Object = MibTableColumn
tmnxOamAncpHistoryIndex = _TmnxOamAncpHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 20, 1, 1),
    _TmnxOamAncpHistoryIndex_Type()
)
tmnxOamAncpHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamAncpHistoryIndex.setStatus("current")


class _TmnxOamAncpHistoryAncpString_Type(DisplayString):
    """Custom type tmnxOamAncpHistoryAncpString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TmnxOamAncpHistoryAncpString_Type.__name__ = "DisplayString"
_TmnxOamAncpHistoryAncpString_Object = MibTableColumn
tmnxOamAncpHistoryAncpString = _TmnxOamAncpHistoryAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 20, 1, 2),
    _TmnxOamAncpHistoryAncpString_Type()
)
tmnxOamAncpHistoryAncpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamAncpHistoryAncpString.setStatus("current")
_TmnxOamAncpHistoryAccNodeCode_Type = Unsigned32
_TmnxOamAncpHistoryAccNodeCode_Object = MibTableColumn
tmnxOamAncpHistoryAccNodeCode = _TmnxOamAncpHistoryAccNodeCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 20, 1, 3),
    _TmnxOamAncpHistoryAccNodeCode_Type()
)
tmnxOamAncpHistoryAccNodeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamAncpHistoryAccNodeCode.setStatus("current")
_TmnxOamAncpHistoryAccNodeResult_Type = Unsigned32
_TmnxOamAncpHistoryAccNodeResult_Object = MibTableColumn
tmnxOamAncpHistoryAccNodeResult = _TmnxOamAncpHistoryAccNodeResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 20, 1, 4),
    _TmnxOamAncpHistoryAccNodeResult_Type()
)
tmnxOamAncpHistoryAccNodeResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamAncpHistoryAccNodeResult.setStatus("current")
_TmnxOamAncpHistoryAccNodeRspStr_Type = DisplayString
_TmnxOamAncpHistoryAccNodeRspStr_Object = MibTableColumn
tmnxOamAncpHistoryAccNodeRspStr = _TmnxOamAncpHistoryAccNodeRspStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 1, 20, 1, 5),
    _TmnxOamAncpHistoryAccNodeRspStr_Type()
)
tmnxOamAncpHistoryAccNodeRspStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamAncpHistoryAccNodeRspStr.setStatus("current")
_TmnxOamTraceRouteObjs_ObjectIdentity = ObjectIdentity
tmnxOamTraceRouteObjs = _TmnxOamTraceRouteObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2)
)
_TmnxOamTraceRouteNotifyObjects_ObjectIdentity = ObjectIdentity
tmnxOamTraceRouteNotifyObjects = _TmnxOamTraceRouteNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 1)
)


class _TmnxOamTrMaxConcurrentRequests_Type(Unsigned32):
    """Custom type tmnxOamTrMaxConcurrentRequests based on Unsigned32"""
    defaultValue = 0


_TmnxOamTrMaxConcurrentRequests_Object = MibScalar
tmnxOamTrMaxConcurrentRequests = _TmnxOamTrMaxConcurrentRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 2),
    _TmnxOamTrMaxConcurrentRequests_Type()
)
tmnxOamTrMaxConcurrentRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamTrMaxConcurrentRequests.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrMaxConcurrentRequests.setUnits("requests")
_TmnxOamTrCtlTable_Object = MibTable
tmnxOamTrCtlTable = _TmnxOamTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxOamTrCtlTable.setStatus("current")
_TmnxOamTrCtlEntry_Object = MibTableRow
tmnxOamTrCtlEntry = _TmnxOamTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1)
)
tmnxOamTrCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamTrCtlEntry.setStatus("current")


class _TmnxOamTrCtlOwnerIndex_Type(SnmpAdminString):
    """Custom type tmnxOamTrCtlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxOamTrCtlOwnerIndex_Type.__name__ = "SnmpAdminString"
_TmnxOamTrCtlOwnerIndex_Object = MibTableColumn
tmnxOamTrCtlOwnerIndex = _TmnxOamTrCtlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 1),
    _TmnxOamTrCtlOwnerIndex_Type()
)
tmnxOamTrCtlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamTrCtlOwnerIndex.setStatus("current")


class _TmnxOamTrCtlTestIndex_Type(SnmpAdminString):
    """Custom type tmnxOamTrCtlTestIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxOamTrCtlTestIndex_Type.__name__ = "SnmpAdminString"
_TmnxOamTrCtlTestIndex_Object = MibTableColumn
tmnxOamTrCtlTestIndex = _TmnxOamTrCtlTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 2),
    _TmnxOamTrCtlTestIndex_Type()
)
tmnxOamTrCtlTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamTrCtlTestIndex.setStatus("current")
_TmnxOamTrCtlRowStatus_Type = RowStatus
_TmnxOamTrCtlRowStatus_Object = MibTableColumn
tmnxOamTrCtlRowStatus = _TmnxOamTrCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 3),
    _TmnxOamTrCtlRowStatus_Type()
)
tmnxOamTrCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlRowStatus.setStatus("current")


class _TmnxOamTrCtlStorageType_Type(StorageType):
    """Custom type tmnxOamTrCtlStorageType based on StorageType"""


_TmnxOamTrCtlStorageType_Object = MibTableColumn
tmnxOamTrCtlStorageType = _TmnxOamTrCtlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 4),
    _TmnxOamTrCtlStorageType_Type()
)
tmnxOamTrCtlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlStorageType.setStatus("current")


class _TmnxOamTrCtlDescr_Type(SnmpAdminString):
    """Custom type tmnxOamTrCtlDescr based on SnmpAdminString"""
    defaultHexValue = "00"


_TmnxOamTrCtlDescr_Object = MibTableColumn
tmnxOamTrCtlDescr = _TmnxOamTrCtlDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 5),
    _TmnxOamTrCtlDescr_Type()
)
tmnxOamTrCtlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlDescr.setStatus("current")


class _TmnxOamTrCtlTestMode_Type(Integer32):
    """Custom type tmnxOamTrCtlTestMode based on Integer32"""
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
        *(("icmpTraceRoute", 5),
          ("ldpTreeTrace", 6),
          ("lspTraceRoute", 2),
          ("macTraceRoute", 1),
          ("mcastTraceRoute", 4),
          ("vccvTraceRoute", 7),
          ("vprnTraceRoute", 3))
    )


_TmnxOamTrCtlTestMode_Type.__name__ = "Integer32"
_TmnxOamTrCtlTestMode_Object = MibTableColumn
tmnxOamTrCtlTestMode = _TmnxOamTrCtlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 6),
    _TmnxOamTrCtlTestMode_Type()
)
tmnxOamTrCtlTestMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlTestMode.setStatus("current")


class _TmnxOamTrCtlAdminStatus_Type(Integer32):
    """Custom type tmnxOamTrCtlAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_TmnxOamTrCtlAdminStatus_Type.__name__ = "Integer32"
_TmnxOamTrCtlAdminStatus_Object = MibTableColumn
tmnxOamTrCtlAdminStatus = _TmnxOamTrCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 7),
    _TmnxOamTrCtlAdminStatus_Type()
)
tmnxOamTrCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlAdminStatus.setStatus("current")


class _TmnxOamTrCtlFcName_Type(TFCName):
    """Custom type tmnxOamTrCtlFcName based on TFCName"""
    defaultValue = OctetString("be")


_TmnxOamTrCtlFcName_Object = MibTableColumn
tmnxOamTrCtlFcName = _TmnxOamTrCtlFcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 8),
    _TmnxOamTrCtlFcName_Type()
)
tmnxOamTrCtlFcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlFcName.setStatus("current")


class _TmnxOamTrCtlProfile_Type(TProfile):
    """Custom type tmnxOamTrCtlProfile based on TProfile"""


_TmnxOamTrCtlProfile_Object = MibTableColumn
tmnxOamTrCtlProfile = _TmnxOamTrCtlProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 9),
    _TmnxOamTrCtlProfile_Type()
)
tmnxOamTrCtlProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlProfile.setStatus("current")


class _TmnxOamTrCtlTargetIpAddress_Type(IpAddress):
    """Custom type tmnxOamTrCtlTargetIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamTrCtlTargetIpAddress_Object = MibTableColumn
tmnxOamTrCtlTargetIpAddress = _TmnxOamTrCtlTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 10),
    _TmnxOamTrCtlTargetIpAddress_Type()
)
tmnxOamTrCtlTargetIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlTargetIpAddress.setStatus("obsolete")


class _TmnxOamTrCtlServiceId_Type(TmnxServId):
    """Custom type tmnxOamTrCtlServiceId based on TmnxServId"""
    defaultValue = 0


_TmnxOamTrCtlServiceId_Object = MibTableColumn
tmnxOamTrCtlServiceId = _TmnxOamTrCtlServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 11),
    _TmnxOamTrCtlServiceId_Type()
)
tmnxOamTrCtlServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlServiceId.setStatus("current")


class _TmnxOamTrCtlDataSize_Type(Unsigned32):
    """Custom type tmnxOamTrCtlDataSize based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9198),
    )


_TmnxOamTrCtlDataSize_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlDataSize_Object = MibTableColumn
tmnxOamTrCtlDataSize = _TmnxOamTrCtlDataSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 12),
    _TmnxOamTrCtlDataSize_Type()
)
tmnxOamTrCtlDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlDataSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrCtlDataSize.setUnits("octets")


class _TmnxOamTrCtlTimeOut_Type(Unsigned32):
    """Custom type tmnxOamTrCtlTimeOut based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxOamTrCtlTimeOut_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlTimeOut_Object = MibTableColumn
tmnxOamTrCtlTimeOut = _TmnxOamTrCtlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 13),
    _TmnxOamTrCtlTimeOut_Type()
)
tmnxOamTrCtlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrCtlTimeOut.setUnits("seconds")


class _TmnxOamTrCtlProbesPerHop_Type(Unsigned32):
    """Custom type tmnxOamTrCtlProbesPerHop based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxOamTrCtlProbesPerHop_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlProbesPerHop_Object = MibTableColumn
tmnxOamTrCtlProbesPerHop = _TmnxOamTrCtlProbesPerHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 14),
    _TmnxOamTrCtlProbesPerHop_Type()
)
tmnxOamTrCtlProbesPerHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlProbesPerHop.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrCtlProbesPerHop.setUnits("probes")


class _TmnxOamTrCtlMaxTtl_Type(Unsigned32):
    """Custom type tmnxOamTrCtlMaxTtl based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamTrCtlMaxTtl_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlMaxTtl_Object = MibTableColumn
tmnxOamTrCtlMaxTtl = _TmnxOamTrCtlMaxTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 15),
    _TmnxOamTrCtlMaxTtl_Type()
)
tmnxOamTrCtlMaxTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlMaxTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrCtlMaxTtl.setUnits("time-to-live value")


class _TmnxOamTrCtlInitialTtl_Type(Unsigned32):
    """Custom type tmnxOamTrCtlInitialTtl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxOamTrCtlInitialTtl_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlInitialTtl_Object = MibTableColumn
tmnxOamTrCtlInitialTtl = _TmnxOamTrCtlInitialTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 16),
    _TmnxOamTrCtlInitialTtl_Type()
)
tmnxOamTrCtlInitialTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlInitialTtl.setStatus("current")


class _TmnxOamTrCtlDSField_Type(Unsigned32):
    """Custom type tmnxOamTrCtlDSField based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxOamTrCtlDSField_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlDSField_Object = MibTableColumn
tmnxOamTrCtlDSField = _TmnxOamTrCtlDSField_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 17),
    _TmnxOamTrCtlDSField_Type()
)
tmnxOamTrCtlDSField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlDSField.setStatus("current")


class _TmnxOamTrCtlMaxFailures_Type(Unsigned32):
    """Custom type tmnxOamTrCtlMaxFailures based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxOamTrCtlMaxFailures_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlMaxFailures_Object = MibTableColumn
tmnxOamTrCtlMaxFailures = _TmnxOamTrCtlMaxFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 18),
    _TmnxOamTrCtlMaxFailures_Type()
)
tmnxOamTrCtlMaxFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlMaxFailures.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrCtlMaxFailures.setUnits("timeouts")


class _TmnxOamTrCtlInterval_Type(Unsigned32):
    """Custom type tmnxOamTrCtlInterval based on Unsigned32"""
    defaultValue = 1


_TmnxOamTrCtlInterval_Object = MibTableColumn
tmnxOamTrCtlInterval = _TmnxOamTrCtlInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 19),
    _TmnxOamTrCtlInterval_Type()
)
tmnxOamTrCtlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrCtlInterval.setUnits("seconds")


class _TmnxOamTrCtlMaxRows_Type(Unsigned32):
    """Custom type tmnxOamTrCtlMaxRows based on Unsigned32"""
    defaultValue = 300


_TmnxOamTrCtlMaxRows_Object = MibTableColumn
tmnxOamTrCtlMaxRows = _TmnxOamTrCtlMaxRows_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 20),
    _TmnxOamTrCtlMaxRows_Type()
)
tmnxOamTrCtlMaxRows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlMaxRows.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrCtlMaxRows.setUnits("rows")


class _TmnxOamTrCtlTrapGeneration_Type(Bits):
    """Custom type tmnxOamTrCtlTrapGeneration based on Bits"""
    namedValues = NamedValues(
        *(("pathChange", 0),
          ("testCompletion", 2),
          ("testFailure", 1))
    )

_TmnxOamTrCtlTrapGeneration_Type.__name__ = "Bits"
_TmnxOamTrCtlTrapGeneration_Object = MibTableColumn
tmnxOamTrCtlTrapGeneration = _TmnxOamTrCtlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 21),
    _TmnxOamTrCtlTrapGeneration_Type()
)
tmnxOamTrCtlTrapGeneration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlTrapGeneration.setStatus("current")


class _TmnxOamTrCtlCreateHopsEntries_Type(TruthValue):
    """Custom type tmnxOamTrCtlCreateHopsEntries based on TruthValue"""


_TmnxOamTrCtlCreateHopsEntries_Object = MibTableColumn
tmnxOamTrCtlCreateHopsEntries = _TmnxOamTrCtlCreateHopsEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 22),
    _TmnxOamTrCtlCreateHopsEntries_Type()
)
tmnxOamTrCtlCreateHopsEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlCreateHopsEntries.setStatus("current")


class _TmnxOamTrCtlSAA_Type(TruthValue):
    """Custom type tmnxOamTrCtlSAA based on TruthValue"""


_TmnxOamTrCtlSAA_Object = MibTableColumn
tmnxOamTrCtlSAA = _TmnxOamTrCtlSAA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 23),
    _TmnxOamTrCtlSAA_Type()
)
tmnxOamTrCtlSAA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlSAA.setStatus("current")
_TmnxOamTrCtlRuns_Type = Counter32
_TmnxOamTrCtlRuns_Object = MibTableColumn
tmnxOamTrCtlRuns = _TmnxOamTrCtlRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 24),
    _TmnxOamTrCtlRuns_Type()
)
tmnxOamTrCtlRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrCtlRuns.setStatus("current")
_TmnxOamTrCtlFailures_Type = Counter32
_TmnxOamTrCtlFailures_Object = MibTableColumn
tmnxOamTrCtlFailures = _TmnxOamTrCtlFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 25),
    _TmnxOamTrCtlFailures_Type()
)
tmnxOamTrCtlFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrCtlFailures.setStatus("current")


class _TmnxOamTrCtlLastRunResult_Type(Integer32):
    """Custom type tmnxOamTrCtlLastRunResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 3),
          ("failed", 2),
          ("success", 1),
          ("undetermined", 0))
    )


_TmnxOamTrCtlLastRunResult_Type.__name__ = "Integer32"
_TmnxOamTrCtlLastRunResult_Object = MibTableColumn
tmnxOamTrCtlLastRunResult = _TmnxOamTrCtlLastRunResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 26),
    _TmnxOamTrCtlLastRunResult_Type()
)
tmnxOamTrCtlLastRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrCtlLastRunResult.setStatus("current")
_TmnxOamTrCtlLastChanged_Type = TimeStamp
_TmnxOamTrCtlLastChanged_Object = MibTableColumn
tmnxOamTrCtlLastChanged = _TmnxOamTrCtlLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 27),
    _TmnxOamTrCtlLastChanged_Type()
)
tmnxOamTrCtlLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrCtlLastChanged.setStatus("current")


class _TmnxOamTrCtlVRtrID_Type(TmnxVRtrID):
    """Custom type tmnxOamTrCtlVRtrID based on TmnxVRtrID"""
    defaultValue = 1


_TmnxOamTrCtlVRtrID_Object = MibTableColumn
tmnxOamTrCtlVRtrID = _TmnxOamTrCtlVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 28),
    _TmnxOamTrCtlVRtrID_Type()
)
tmnxOamTrCtlVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlVRtrID.setStatus("current")


class _TmnxOamTrCtlTgtAddrType_Type(InetAddressType):
    """Custom type tmnxOamTrCtlTgtAddrType based on InetAddressType"""


_TmnxOamTrCtlTgtAddrType_Object = MibTableColumn
tmnxOamTrCtlTgtAddrType = _TmnxOamTrCtlTgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 29),
    _TmnxOamTrCtlTgtAddrType_Type()
)
tmnxOamTrCtlTgtAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlTgtAddrType.setStatus("current")


class _TmnxOamTrCtlTgtAddress_Type(InetAddress):
    """Custom type tmnxOamTrCtlTgtAddress based on InetAddress"""
    defaultHexValue = ""


_TmnxOamTrCtlTgtAddress_Object = MibTableColumn
tmnxOamTrCtlTgtAddress = _TmnxOamTrCtlTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 30),
    _TmnxOamTrCtlTgtAddress_Type()
)
tmnxOamTrCtlTgtAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlTgtAddress.setStatus("current")


class _TmnxOamTrCtlSrcAddrType_Type(InetAddressType):
    """Custom type tmnxOamTrCtlSrcAddrType based on InetAddressType"""


_TmnxOamTrCtlSrcAddrType_Object = MibTableColumn
tmnxOamTrCtlSrcAddrType = _TmnxOamTrCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 31),
    _TmnxOamTrCtlSrcAddrType_Type()
)
tmnxOamTrCtlSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlSrcAddrType.setStatus("current")


class _TmnxOamTrCtlSrcAddress_Type(InetAddress):
    """Custom type tmnxOamTrCtlSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamTrCtlSrcAddress_Type.__name__ = "InetAddress"
_TmnxOamTrCtlSrcAddress_Object = MibTableColumn
tmnxOamTrCtlSrcAddress = _TmnxOamTrCtlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 32),
    _TmnxOamTrCtlSrcAddress_Type()
)
tmnxOamTrCtlSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlSrcAddress.setStatus("current")


class _TmnxOamTrCtlWaitMilliSec_Type(Unsigned32):
    """Custom type tmnxOamTrCtlWaitMilliSec based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60000),
    )


_TmnxOamTrCtlWaitMilliSec_Type.__name__ = "Unsigned32"
_TmnxOamTrCtlWaitMilliSec_Object = MibTableColumn
tmnxOamTrCtlWaitMilliSec = _TmnxOamTrCtlWaitMilliSec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 3, 1, 33),
    _TmnxOamTrCtlWaitMilliSec_Type()
)
tmnxOamTrCtlWaitMilliSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamTrCtlWaitMilliSec.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrCtlWaitMilliSec.setUnits("milliseconds")
_TmnxOamTrResultsTable_Object = MibTable
tmnxOamTrResultsTable = _TmnxOamTrResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxOamTrResultsTable.setStatus("current")
_TmnxOamTrResultsEntry_Object = MibTableRow
tmnxOamTrResultsEntry = _TmnxOamTrResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1)
)
tmnxOamTrResultsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamTrResultsEntry.setStatus("current")


class _TmnxOamTrResultsOperStatus_Type(Integer32):
    """Custom type tmnxOamTrResultsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_TmnxOamTrResultsOperStatus_Type.__name__ = "Integer32"
_TmnxOamTrResultsOperStatus_Object = MibTableColumn
tmnxOamTrResultsOperStatus = _TmnxOamTrResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 1),
    _TmnxOamTrResultsOperStatus_Type()
)
tmnxOamTrResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsOperStatus.setStatus("current")
_TmnxOamTrResultsCurHopCount_Type = Gauge32
_TmnxOamTrResultsCurHopCount_Object = MibTableColumn
tmnxOamTrResultsCurHopCount = _TmnxOamTrResultsCurHopCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 2),
    _TmnxOamTrResultsCurHopCount_Type()
)
tmnxOamTrResultsCurHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsCurHopCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrResultsCurHopCount.setUnits("hops")
_TmnxOamTrResultsCurProbeCount_Type = Gauge32
_TmnxOamTrResultsCurProbeCount_Object = MibTableColumn
tmnxOamTrResultsCurProbeCount = _TmnxOamTrResultsCurProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 3),
    _TmnxOamTrResultsCurProbeCount_Type()
)
tmnxOamTrResultsCurProbeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsCurProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrResultsCurProbeCount.setUnits("probes")
_TmnxOamTrResultsIpTgtAddr_Type = IpAddress
_TmnxOamTrResultsIpTgtAddr_Object = MibTableColumn
tmnxOamTrResultsIpTgtAddr = _TmnxOamTrResultsIpTgtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 4),
    _TmnxOamTrResultsIpTgtAddr_Type()
)
tmnxOamTrResultsIpTgtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsIpTgtAddr.setStatus("obsolete")
_TmnxOamTrResultsTestAttempts_Type = Unsigned32
_TmnxOamTrResultsTestAttempts_Object = MibTableColumn
tmnxOamTrResultsTestAttempts = _TmnxOamTrResultsTestAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 5),
    _TmnxOamTrResultsTestAttempts_Type()
)
tmnxOamTrResultsTestAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsTestAttempts.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOamTrResultsTestAttempts.setUnits("tests")
_TmnxOamTrResultsTestSuccesses_Type = Unsigned32
_TmnxOamTrResultsTestSuccesses_Object = MibTableColumn
tmnxOamTrResultsTestSuccesses = _TmnxOamTrResultsTestSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 6),
    _TmnxOamTrResultsTestSuccesses_Type()
)
tmnxOamTrResultsTestSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsTestSuccesses.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOamTrResultsTestSuccesses.setUnits("tests")
_TmnxOamTrResultsLastGoodPath_Type = DateAndTime
_TmnxOamTrResultsLastGoodPath_Object = MibTableColumn
tmnxOamTrResultsLastGoodPath = _TmnxOamTrResultsLastGoodPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 7),
    _TmnxOamTrResultsLastGoodPath_Type()
)
tmnxOamTrResultsLastGoodPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsLastGoodPath.setStatus("current")


class _TmnxOamTrResultsTestRunIndex_Type(Unsigned32):
    """Custom type tmnxOamTrResultsTestRunIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamTrResultsTestRunIndex_Type.__name__ = "Unsigned32"
_TmnxOamTrResultsTestRunIndex_Object = MibTableColumn
tmnxOamTrResultsTestRunIndex = _TmnxOamTrResultsTestRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 8),
    _TmnxOamTrResultsTestRunIndex_Type()
)
tmnxOamTrResultsTestRunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamTrResultsTestRunIndex.setStatus("current")
_TmnxOamTrResultsTgtAddrType_Type = InetAddressType
_TmnxOamTrResultsTgtAddrType_Object = MibTableColumn
tmnxOamTrResultsTgtAddrType = _TmnxOamTrResultsTgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 9),
    _TmnxOamTrResultsTgtAddrType_Type()
)
tmnxOamTrResultsTgtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsTgtAddrType.setStatus("current")


class _TmnxOamTrResultsTgtAddress_Type(InetAddress):
    """Custom type tmnxOamTrResultsTgtAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamTrResultsTgtAddress_Type.__name__ = "InetAddress"
_TmnxOamTrResultsTgtAddress_Object = MibTableColumn
tmnxOamTrResultsTgtAddress = _TmnxOamTrResultsTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 4, 1, 10),
    _TmnxOamTrResultsTgtAddress_Type()
)
tmnxOamTrResultsTgtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrResultsTgtAddress.setStatus("current")
_TmnxOamTrProbeHistoryTable_Object = MibTable
tmnxOamTrProbeHistoryTable = _TmnxOamTrProbeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryTable.setStatus("current")
_TmnxOamTrProbeHistoryEntry_Object = MibTableRow
tmnxOamTrProbeHistoryEntry = _TmnxOamTrProbeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1)
)
tmnxOamTrProbeHistoryEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryEntry.setStatus("current")


class _TmnxOamTrProbeHistoryIndex_Type(Unsigned32):
    """Custom type tmnxOamTrProbeHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamTrProbeHistoryIndex_Type.__name__ = "Unsigned32"
_TmnxOamTrProbeHistoryIndex_Object = MibTableColumn
tmnxOamTrProbeHistoryIndex = _TmnxOamTrProbeHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 1),
    _TmnxOamTrProbeHistoryIndex_Type()
)
tmnxOamTrProbeHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryIndex.setStatus("current")


class _TmnxOamTrProbeHistoryHopIndex_Type(Unsigned32):
    """Custom type tmnxOamTrProbeHistoryHopIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamTrProbeHistoryHopIndex_Type.__name__ = "Unsigned32"
_TmnxOamTrProbeHistoryHopIndex_Object = MibTableColumn
tmnxOamTrProbeHistoryHopIndex = _TmnxOamTrProbeHistoryHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 2),
    _TmnxOamTrProbeHistoryHopIndex_Type()
)
tmnxOamTrProbeHistoryHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryHopIndex.setStatus("current")


class _TmnxOamTrProbeHistoryProbeIndex_Type(Unsigned32):
    """Custom type tmnxOamTrProbeHistoryProbeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxOamTrProbeHistoryProbeIndex_Type.__name__ = "Unsigned32"
_TmnxOamTrProbeHistoryProbeIndex_Object = MibTableColumn
tmnxOamTrProbeHistoryProbeIndex = _TmnxOamTrProbeHistoryProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 3),
    _TmnxOamTrProbeHistoryProbeIndex_Type()
)
tmnxOamTrProbeHistoryProbeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryProbeIndex.setStatus("current")
_TmnxOamTrProbeHistoryIpAddr_Type = IpAddress
_TmnxOamTrProbeHistoryIpAddr_Object = MibTableColumn
tmnxOamTrProbeHistoryIpAddr = _TmnxOamTrProbeHistoryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 4),
    _TmnxOamTrProbeHistoryIpAddr_Type()
)
tmnxOamTrProbeHistoryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryIpAddr.setStatus("obsolete")
_TmnxOamTrProbeHistoryResponse_Type = Unsigned32
_TmnxOamTrProbeHistoryResponse_Object = MibTableColumn
tmnxOamTrProbeHistoryResponse = _TmnxOamTrProbeHistoryResponse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 5),
    _TmnxOamTrProbeHistoryResponse_Type()
)
tmnxOamTrProbeHistoryResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryResponse.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryResponse.setUnits("milliseconds")
_TmnxOamTrProbeHistoryOneWayTime_Type = Integer32
_TmnxOamTrProbeHistoryOneWayTime_Object = MibTableColumn
tmnxOamTrProbeHistoryOneWayTime = _TmnxOamTrProbeHistoryOneWayTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 6),
    _TmnxOamTrProbeHistoryOneWayTime_Type()
)
tmnxOamTrProbeHistoryOneWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryOneWayTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryOneWayTime.setUnits("milliseconds")
_TmnxOamTrProbeHistoryStatus_Type = TmnxOamResponseStatus
_TmnxOamTrProbeHistoryStatus_Object = MibTableColumn
tmnxOamTrProbeHistoryStatus = _TmnxOamTrProbeHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 7),
    _TmnxOamTrProbeHistoryStatus_Type()
)
tmnxOamTrProbeHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryStatus.setStatus("current")
_TmnxOamTrProbeHistoryLastRC_Type = Integer32
_TmnxOamTrProbeHistoryLastRC_Object = MibTableColumn
tmnxOamTrProbeHistoryLastRC = _TmnxOamTrProbeHistoryLastRC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 8),
    _TmnxOamTrProbeHistoryLastRC_Type()
)
tmnxOamTrProbeHistoryLastRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryLastRC.setStatus("current")
_TmnxOamTrProbeHistoryTime_Type = DateAndTime
_TmnxOamTrProbeHistoryTime_Object = MibTableColumn
tmnxOamTrProbeHistoryTime = _TmnxOamTrProbeHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 9),
    _TmnxOamTrProbeHistoryTime_Type()
)
tmnxOamTrProbeHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryTime.setStatus("current")
_TmnxOamTrProbeHistoryResponsePlane_Type = TmnxOamTestResponsePlane
_TmnxOamTrProbeHistoryResponsePlane_Object = MibTableColumn
tmnxOamTrProbeHistoryResponsePlane = _TmnxOamTrProbeHistoryResponsePlane_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 10),
    _TmnxOamTrProbeHistoryResponsePlane_Type()
)
tmnxOamTrProbeHistoryResponsePlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryResponsePlane.setStatus("current")
_TmnxOamTrProbeHistoryAddressType_Type = TmnxOamAddressType
_TmnxOamTrProbeHistoryAddressType_Object = MibTableColumn
tmnxOamTrProbeHistoryAddressType = _TmnxOamTrProbeHistoryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 11),
    _TmnxOamTrProbeHistoryAddressType_Type()
)
tmnxOamTrProbeHistoryAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryAddressType.setStatus("current")
_TmnxOamTrProbeHistorySapId_Type = TmnxStrSapId
_TmnxOamTrProbeHistorySapId_Object = MibTableColumn
tmnxOamTrProbeHistorySapId = _TmnxOamTrProbeHistorySapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 12),
    _TmnxOamTrProbeHistorySapId_Type()
)
tmnxOamTrProbeHistorySapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistorySapId.setStatus("current")
_TmnxOamTrProbeHistoryVersion_Type = Unsigned32
_TmnxOamTrProbeHistoryVersion_Object = MibTableColumn
tmnxOamTrProbeHistoryVersion = _TmnxOamTrProbeHistoryVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 14),
    _TmnxOamTrProbeHistoryVersion_Type()
)
tmnxOamTrProbeHistoryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryVersion.setStatus("current")
_TmnxOamTrProbeHistoryRouterID_Type = RouterID
_TmnxOamTrProbeHistoryRouterID_Object = MibTableColumn
tmnxOamTrProbeHistoryRouterID = _TmnxOamTrProbeHistoryRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 15),
    _TmnxOamTrProbeHistoryRouterID_Type()
)
tmnxOamTrProbeHistoryRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryRouterID.setStatus("current")
_TmnxOamTrProbeHistoryIfIndex_Type = InterfaceIndexOrZero
_TmnxOamTrProbeHistoryIfIndex_Object = MibTableColumn
tmnxOamTrProbeHistoryIfIndex = _TmnxOamTrProbeHistoryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 16),
    _TmnxOamTrProbeHistoryIfIndex_Type()
)
tmnxOamTrProbeHistoryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryIfIndex.setStatus("current")
_TmnxOamTrProbeHistoryDataLen_Type = Unsigned32
_TmnxOamTrProbeHistoryDataLen_Object = MibTableColumn
tmnxOamTrProbeHistoryDataLen = _TmnxOamTrProbeHistoryDataLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 17),
    _TmnxOamTrProbeHistoryDataLen_Type()
)
tmnxOamTrProbeHistoryDataLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryDataLen.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryDataLen.setUnits("octets")
_TmnxOamTrProbeHistorySize_Type = Unsigned32
_TmnxOamTrProbeHistorySize_Object = MibTableColumn
tmnxOamTrProbeHistorySize = _TmnxOamTrProbeHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 18),
    _TmnxOamTrProbeHistorySize_Type()
)
tmnxOamTrProbeHistorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistorySize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistorySize.setUnits("octets")
_TmnxOamTrProbeHistoryInOneWayTime_Type = Integer32
_TmnxOamTrProbeHistoryInOneWayTime_Object = MibTableColumn
tmnxOamTrProbeHistoryInOneWayTime = _TmnxOamTrProbeHistoryInOneWayTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 19),
    _TmnxOamTrProbeHistoryInOneWayTime_Type()
)
tmnxOamTrProbeHistoryInOneWayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryInOneWayTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryInOneWayTime.setUnits("milliseconds")
_TmnxOamTrProbeHistoryAddrType_Type = InetAddressType
_TmnxOamTrProbeHistoryAddrType_Object = MibTableColumn
tmnxOamTrProbeHistoryAddrType = _TmnxOamTrProbeHistoryAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 20),
    _TmnxOamTrProbeHistoryAddrType_Type()
)
tmnxOamTrProbeHistoryAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryAddrType.setStatus("current")


class _TmnxOamTrProbeHistoryAddress_Type(InetAddress):
    """Custom type tmnxOamTrProbeHistoryAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamTrProbeHistoryAddress_Type.__name__ = "InetAddress"
_TmnxOamTrProbeHistoryAddress_Object = MibTableColumn
tmnxOamTrProbeHistoryAddress = _TmnxOamTrProbeHistoryAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 5, 1, 21),
    _TmnxOamTrProbeHistoryAddress_Type()
)
tmnxOamTrProbeHistoryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrProbeHistoryAddress.setStatus("current")
_TmnxOamTrHopsTable_Object = MibTable
tmnxOamTrHopsTable = _TmnxOamTrHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6)
)
if mibBuilder.loadTexts:
    tmnxOamTrHopsTable.setStatus("current")
_TmnxOamTrHopsEntry_Object = MibTableRow
tmnxOamTrHopsEntry = _TmnxOamTrHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1)
)
tmnxOamTrHopsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsHopIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamTrHopsEntry.setStatus("current")
_TmnxOamTrHopsHopIndex_Type = Unsigned32
_TmnxOamTrHopsHopIndex_Object = MibTableColumn
tmnxOamTrHopsHopIndex = _TmnxOamTrHopsHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 1),
    _TmnxOamTrHopsHopIndex_Type()
)
tmnxOamTrHopsHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamTrHopsHopIndex.setStatus("current")
_TmnxOamTrHopsIpTgtAddress_Type = IpAddress
_TmnxOamTrHopsIpTgtAddress_Object = MibTableColumn
tmnxOamTrHopsIpTgtAddress = _TmnxOamTrHopsIpTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 2),
    _TmnxOamTrHopsIpTgtAddress_Type()
)
tmnxOamTrHopsIpTgtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsIpTgtAddress.setStatus("obsolete")
_TmnxOamTrHopsMinRtt_Type = Unsigned32
_TmnxOamTrHopsMinRtt_Object = MibTableColumn
tmnxOamTrHopsMinRtt = _TmnxOamTrHopsMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 3),
    _TmnxOamTrHopsMinRtt_Type()
)
tmnxOamTrHopsMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMinRtt.setStatus("current")
_TmnxOamTrHopsMaxRtt_Type = Unsigned32
_TmnxOamTrHopsMaxRtt_Object = MibTableColumn
tmnxOamTrHopsMaxRtt = _TmnxOamTrHopsMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 4),
    _TmnxOamTrHopsMaxRtt_Type()
)
tmnxOamTrHopsMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMaxRtt.setStatus("current")
_TmnxOamTrHopsAverageRtt_Type = Unsigned32
_TmnxOamTrHopsAverageRtt_Object = MibTableColumn
tmnxOamTrHopsAverageRtt = _TmnxOamTrHopsAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 5),
    _TmnxOamTrHopsAverageRtt_Type()
)
tmnxOamTrHopsAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsAverageRtt.setStatus("current")
_TmnxOamTrHopsRttSumOfSquares_Type = Unsigned32
_TmnxOamTrHopsRttSumOfSquares_Object = MibTableColumn
tmnxOamTrHopsRttSumOfSquares = _TmnxOamTrHopsRttSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 6),
    _TmnxOamTrHopsRttSumOfSquares_Type()
)
tmnxOamTrHopsRttSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsRttSumOfSquares.setStatus("current")
_TmnxOamTrHopsMinTt_Type = Integer32
_TmnxOamTrHopsMinTt_Object = MibTableColumn
tmnxOamTrHopsMinTt = _TmnxOamTrHopsMinTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 7),
    _TmnxOamTrHopsMinTt_Type()
)
tmnxOamTrHopsMinTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMinTt.setStatus("current")
_TmnxOamTrHopsMaxTt_Type = Integer32
_TmnxOamTrHopsMaxTt_Object = MibTableColumn
tmnxOamTrHopsMaxTt = _TmnxOamTrHopsMaxTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 8),
    _TmnxOamTrHopsMaxTt_Type()
)
tmnxOamTrHopsMaxTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMaxTt.setStatus("current")
_TmnxOamTrHopsAverageTt_Type = Integer32
_TmnxOamTrHopsAverageTt_Object = MibTableColumn
tmnxOamTrHopsAverageTt = _TmnxOamTrHopsAverageTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 9),
    _TmnxOamTrHopsAverageTt_Type()
)
tmnxOamTrHopsAverageTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsAverageTt.setStatus("current")
_TmnxOamTrHopsTtSumOfSquares_Type = Integer32
_TmnxOamTrHopsTtSumOfSquares_Object = MibTableColumn
tmnxOamTrHopsTtSumOfSquares = _TmnxOamTrHopsTtSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 10),
    _TmnxOamTrHopsTtSumOfSquares_Type()
)
tmnxOamTrHopsTtSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsTtSumOfSquares.setStatus("current")
_TmnxOamTrHopsSentProbes_Type = Unsigned32
_TmnxOamTrHopsSentProbes_Object = MibTableColumn
tmnxOamTrHopsSentProbes = _TmnxOamTrHopsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 11),
    _TmnxOamTrHopsSentProbes_Type()
)
tmnxOamTrHopsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsSentProbes.setStatus("current")
_TmnxOamTrHopsProbeResponses_Type = Unsigned32
_TmnxOamTrHopsProbeResponses_Object = MibTableColumn
tmnxOamTrHopsProbeResponses = _TmnxOamTrHopsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 12),
    _TmnxOamTrHopsProbeResponses_Type()
)
tmnxOamTrHopsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsProbeResponses.setStatus("current")
_TmnxOamTrHopsLastGoodProbe_Type = DateAndTime
_TmnxOamTrHopsLastGoodProbe_Object = MibTableColumn
tmnxOamTrHopsLastGoodProbe = _TmnxOamTrHopsLastGoodProbe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 13),
    _TmnxOamTrHopsLastGoodProbe_Type()
)
tmnxOamTrHopsLastGoodProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsLastGoodProbe.setStatus("current")
_TmnxOamTrHopsMinInTt_Type = Integer32
_TmnxOamTrHopsMinInTt_Object = MibTableColumn
tmnxOamTrHopsMinInTt = _TmnxOamTrHopsMinInTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 18),
    _TmnxOamTrHopsMinInTt_Type()
)
tmnxOamTrHopsMinInTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMinInTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMinInTt.setUnits("milliseconds")
_TmnxOamTrHopsMaxInTt_Type = Integer32
_TmnxOamTrHopsMaxInTt_Object = MibTableColumn
tmnxOamTrHopsMaxInTt = _TmnxOamTrHopsMaxInTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 19),
    _TmnxOamTrHopsMaxInTt_Type()
)
tmnxOamTrHopsMaxInTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMaxInTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsMaxInTt.setUnits("milliseconds")
_TmnxOamTrHopsAverageInTt_Type = Integer32
_TmnxOamTrHopsAverageInTt_Object = MibTableColumn
tmnxOamTrHopsAverageInTt = _TmnxOamTrHopsAverageInTt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 20),
    _TmnxOamTrHopsAverageInTt_Type()
)
tmnxOamTrHopsAverageInTt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsAverageInTt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsAverageInTt.setUnits("milliseconds")
_TmnxOamTrHopsInTtSumOfSqrs_Type = Integer32
_TmnxOamTrHopsInTtSumOfSqrs_Object = MibTableColumn
tmnxOamTrHopsInTtSumOfSqrs = _TmnxOamTrHopsInTtSumOfSqrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 21),
    _TmnxOamTrHopsInTtSumOfSqrs_Type()
)
tmnxOamTrHopsInTtSumOfSqrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsInTtSumOfSqrs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsInTtSumOfSqrs.setUnits("milliseconds")
_TmnxOamTrHopsOutJitter_Type = Integer32
_TmnxOamTrHopsOutJitter_Object = MibTableColumn
tmnxOamTrHopsOutJitter = _TmnxOamTrHopsOutJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 22),
    _TmnxOamTrHopsOutJitter_Type()
)
tmnxOamTrHopsOutJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsOutJitter.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsOutJitter.setUnits("milliseconds")
_TmnxOamTrHopsInJitter_Type = Integer32
_TmnxOamTrHopsInJitter_Object = MibTableColumn
tmnxOamTrHopsInJitter = _TmnxOamTrHopsInJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 23),
    _TmnxOamTrHopsInJitter_Type()
)
tmnxOamTrHopsInJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsInJitter.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsInJitter.setUnits("milliseconds")
_TmnxOamTrHopsRtJitter_Type = Integer32
_TmnxOamTrHopsRtJitter_Object = MibTableColumn
tmnxOamTrHopsRtJitter = _TmnxOamTrHopsRtJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 24),
    _TmnxOamTrHopsRtJitter_Type()
)
tmnxOamTrHopsRtJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsRtJitter.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamTrHopsRtJitter.setUnits("milliseconds")
_TmnxOamTrHopsProbeTimeouts_Type = Unsigned32
_TmnxOamTrHopsProbeTimeouts_Object = MibTableColumn
tmnxOamTrHopsProbeTimeouts = _TmnxOamTrHopsProbeTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 25),
    _TmnxOamTrHopsProbeTimeouts_Type()
)
tmnxOamTrHopsProbeTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsProbeTimeouts.setStatus("current")
_TmnxOamTrHopsProbeFailures_Type = Unsigned32
_TmnxOamTrHopsProbeFailures_Object = MibTableColumn
tmnxOamTrHopsProbeFailures = _TmnxOamTrHopsProbeFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 26),
    _TmnxOamTrHopsProbeFailures_Type()
)
tmnxOamTrHopsProbeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsProbeFailures.setStatus("current")
_TmnxOamTrHopsTgtAddrType_Type = InetAddressType
_TmnxOamTrHopsTgtAddrType_Object = MibTableColumn
tmnxOamTrHopsTgtAddrType = _TmnxOamTrHopsTgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 27),
    _TmnxOamTrHopsTgtAddrType_Type()
)
tmnxOamTrHopsTgtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsTgtAddrType.setStatus("current")


class _TmnxOamTrHopsTgtAddress_Type(InetAddress):
    """Custom type tmnxOamTrHopsTgtAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamTrHopsTgtAddress_Type.__name__ = "InetAddress"
_TmnxOamTrHopsTgtAddress_Object = MibTableColumn
tmnxOamTrHopsTgtAddress = _TmnxOamTrHopsTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 6, 1, 28),
    _TmnxOamTrHopsTgtAddress_Type()
)
tmnxOamTrHopsTgtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamTrHopsTgtAddress.setStatus("current")
_TmnxOamMacTrCtlTable_Object = MibTable
tmnxOamMacTrCtlTable = _TmnxOamMacTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxOamMacTrCtlTable.setStatus("current")
_TmnxOamMacTrCtlEntry_Object = MibTableRow
tmnxOamMacTrCtlEntry = _TmnxOamMacTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 7, 1)
)
tmnxOamMacTrCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMacTrCtlEntry.setStatus("current")


class _TmnxOamMacTrCtlTargetMacAddr_Type(MacAddress):
    """Custom type tmnxOamMacTrCtlTargetMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamMacTrCtlTargetMacAddr_Object = MibTableColumn
tmnxOamMacTrCtlTargetMacAddr = _TmnxOamMacTrCtlTargetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 7, 1, 1),
    _TmnxOamMacTrCtlTargetMacAddr_Type()
)
tmnxOamMacTrCtlTargetMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacTrCtlTargetMacAddr.setStatus("current")


class _TmnxOamMacTrCtlSourceMacAddr_Type(MacAddress):
    """Custom type tmnxOamMacTrCtlSourceMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamMacTrCtlSourceMacAddr_Object = MibTableColumn
tmnxOamMacTrCtlSourceMacAddr = _TmnxOamMacTrCtlSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 7, 1, 2),
    _TmnxOamMacTrCtlSourceMacAddr_Type()
)
tmnxOamMacTrCtlSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacTrCtlSourceMacAddr.setStatus("current")


class _TmnxOamMacTrCtlSendControl_Type(TruthValue):
    """Custom type tmnxOamMacTrCtlSendControl based on TruthValue"""


_TmnxOamMacTrCtlSendControl_Object = MibTableColumn
tmnxOamMacTrCtlSendControl = _TmnxOamMacTrCtlSendControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 7, 1, 3),
    _TmnxOamMacTrCtlSendControl_Type()
)
tmnxOamMacTrCtlSendControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacTrCtlSendControl.setStatus("current")


class _TmnxOamMacTrCtlReplyControl_Type(TruthValue):
    """Custom type tmnxOamMacTrCtlReplyControl based on TruthValue"""


_TmnxOamMacTrCtlReplyControl_Object = MibTableColumn
tmnxOamMacTrCtlReplyControl = _TmnxOamMacTrCtlReplyControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 7, 1, 4),
    _TmnxOamMacTrCtlReplyControl_Type()
)
tmnxOamMacTrCtlReplyControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMacTrCtlReplyControl.setStatus("current")
_TmnxOamMacTrL2MapTable_Object = MibTable
tmnxOamMacTrL2MapTable = _TmnxOamMacTrL2MapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8)
)
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapTable.setStatus("current")
_TmnxOamMacTrL2MapEntry_Object = MibTableRow
tmnxOamMacTrL2MapEntry = _TmnxOamMacTrL2MapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1)
)
tmnxOamMacTrL2MapEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapEntry.setStatus("current")


class _TmnxOamMacTrL2MapIndex_Type(Unsigned32):
    """Custom type tmnxOamMacTrL2MapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamMacTrL2MapIndex_Type.__name__ = "Unsigned32"
_TmnxOamMacTrL2MapIndex_Object = MibTableColumn
tmnxOamMacTrL2MapIndex = _TmnxOamMacTrL2MapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 1),
    _TmnxOamMacTrL2MapIndex_Type()
)
tmnxOamMacTrL2MapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapIndex.setStatus("current")
_TmnxOamMacTrL2MapRouterID_Type = IpAddress
_TmnxOamMacTrL2MapRouterID_Object = MibTableColumn
tmnxOamMacTrL2MapRouterID = _TmnxOamMacTrL2MapRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 2),
    _TmnxOamMacTrL2MapRouterID_Type()
)
tmnxOamMacTrL2MapRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapRouterID.setStatus("current")
_TmnxOamMacTrL2MapLabel_Type = MplsLabel
_TmnxOamMacTrL2MapLabel_Object = MibTableColumn
tmnxOamMacTrL2MapLabel = _TmnxOamMacTrL2MapLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 3),
    _TmnxOamMacTrL2MapLabel_Type()
)
tmnxOamMacTrL2MapLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapLabel.setStatus("current")
_TmnxOamMacTrL2MapProtocol_Type = TmnxOamSignalProtocol
_TmnxOamMacTrL2MapProtocol_Object = MibTableColumn
tmnxOamMacTrL2MapProtocol = _TmnxOamMacTrL2MapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 4),
    _TmnxOamMacTrL2MapProtocol_Type()
)
tmnxOamMacTrL2MapProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapProtocol.setStatus("current")
_TmnxOamMacTrL2MapVCType_Type = TmnxOamVcType
_TmnxOamMacTrL2MapVCType_Object = MibTableColumn
tmnxOamMacTrL2MapVCType = _TmnxOamMacTrL2MapVCType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 5),
    _TmnxOamMacTrL2MapVCType_Type()
)
tmnxOamMacTrL2MapVCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapVCType.setStatus("current")
_TmnxOamMacTrL2MapVCID_Type = TmnxVcId
_TmnxOamMacTrL2MapVCID_Object = MibTableColumn
tmnxOamMacTrL2MapVCID = _TmnxOamMacTrL2MapVCID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 6),
    _TmnxOamMacTrL2MapVCID_Type()
)
tmnxOamMacTrL2MapVCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapVCID.setStatus("current")


class _TmnxOamMacTrL2MapDirection_Type(Integer32):
    """Custom type tmnxOamMacTrL2MapDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("upstream", 1))
    )


_TmnxOamMacTrL2MapDirection_Type.__name__ = "Integer32"
_TmnxOamMacTrL2MapDirection_Object = MibTableColumn
tmnxOamMacTrL2MapDirection = _TmnxOamMacTrL2MapDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 7),
    _TmnxOamMacTrL2MapDirection_Type()
)
tmnxOamMacTrL2MapDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapDirection.setStatus("current")
_TmnxOamMacTrL2MapSdpId_Type = SdpId
_TmnxOamMacTrL2MapSdpId_Object = MibTableColumn
tmnxOamMacTrL2MapSdpId = _TmnxOamMacTrL2MapSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 8),
    _TmnxOamMacTrL2MapSdpId_Type()
)
tmnxOamMacTrL2MapSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapSdpId.setStatus("current")
_TmnxOamMacTrL2MapSapName_Type = TNamedItemOrEmpty
_TmnxOamMacTrL2MapSapName_Object = MibTableColumn
tmnxOamMacTrL2MapSapName = _TmnxOamMacTrL2MapSapName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 8, 1, 9),
    _TmnxOamMacTrL2MapSapName_Type()
)
tmnxOamMacTrL2MapSapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMacTrL2MapSapName.setStatus("current")
_TmnxOamLspTrCtlTable_Object = MibTable
tmnxOamLspTrCtlTable = _TmnxOamLspTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9)
)
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlTable.setStatus("current")
_TmnxOamLspTrCtlEntry_Object = MibTableRow
tmnxOamLspTrCtlEntry = _TmnxOamLspTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1)
)
tmnxOamLspTrCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlEntry.setStatus("current")


class _TmnxOamLspTrCtlVRtrID_Type(TmnxVRtrID):
    """Custom type tmnxOamLspTrCtlVRtrID based on TmnxVRtrID"""
    defaultValue = 1


_TmnxOamLspTrCtlVRtrID_Object = MibTableColumn
tmnxOamLspTrCtlVRtrID = _TmnxOamLspTrCtlVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 1),
    _TmnxOamLspTrCtlVRtrID_Type()
)
tmnxOamLspTrCtlVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlVRtrID.setStatus("current")


class _TmnxOamLspTrCtlLspName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamLspTrCtlLspName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamLspTrCtlLspName_Object = MibTableColumn
tmnxOamLspTrCtlLspName = _TmnxOamLspTrCtlLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 2),
    _TmnxOamLspTrCtlLspName_Type()
)
tmnxOamLspTrCtlLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlLspName.setStatus("current")


class _TmnxOamLspTrCtlPathName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamLspTrCtlPathName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamLspTrCtlPathName_Object = MibTableColumn
tmnxOamLspTrCtlPathName = _TmnxOamLspTrCtlPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 3),
    _TmnxOamLspTrCtlPathName_Type()
)
tmnxOamLspTrCtlPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlPathName.setStatus("current")


class _TmnxOamLspTrCtlLdpIpPrefix_Type(IpAddress):
    """Custom type tmnxOamLspTrCtlLdpIpPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamLspTrCtlLdpIpPrefix_Object = MibTableColumn
tmnxOamLspTrCtlLdpIpPrefix = _TmnxOamLspTrCtlLdpIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 4),
    _TmnxOamLspTrCtlLdpIpPrefix_Type()
)
tmnxOamLspTrCtlLdpIpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlLdpIpPrefix.setStatus("obsolete")


class _TmnxOamLspTrCtlLdpIpPrefixLen_Type(IpAddressPrefixLength):
    """Custom type tmnxOamLspTrCtlLdpIpPrefixLen based on IpAddressPrefixLength"""
    defaultValue = 32


_TmnxOamLspTrCtlLdpIpPrefixLen_Object = MibTableColumn
tmnxOamLspTrCtlLdpIpPrefixLen = _TmnxOamLspTrCtlLdpIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 5),
    _TmnxOamLspTrCtlLdpIpPrefixLen_Type()
)
tmnxOamLspTrCtlLdpIpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlLdpIpPrefixLen.setStatus("obsolete")


class _TmnxOamLspTrCtlLdpPrefixType_Type(InetAddressType):
    """Custom type tmnxOamLspTrCtlLdpPrefixType based on InetAddressType"""


_TmnxOamLspTrCtlLdpPrefixType_Object = MibTableColumn
tmnxOamLspTrCtlLdpPrefixType = _TmnxOamLspTrCtlLdpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 6),
    _TmnxOamLspTrCtlLdpPrefixType_Type()
)
tmnxOamLspTrCtlLdpPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlLdpPrefixType.setStatus("current")


class _TmnxOamLspTrCtlLdpPrefix_Type(InetAddress):
    """Custom type tmnxOamLspTrCtlLdpPrefix based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspTrCtlLdpPrefix_Type.__name__ = "InetAddress"
_TmnxOamLspTrCtlLdpPrefix_Object = MibTableColumn
tmnxOamLspTrCtlLdpPrefix = _TmnxOamLspTrCtlLdpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 7),
    _TmnxOamLspTrCtlLdpPrefix_Type()
)
tmnxOamLspTrCtlLdpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlLdpPrefix.setStatus("current")


class _TmnxOamLspTrCtlLdpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxOamLspTrCtlLdpPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 32


_TmnxOamLspTrCtlLdpPrefixLen_Object = MibTableColumn
tmnxOamLspTrCtlLdpPrefixLen = _TmnxOamLspTrCtlLdpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 8),
    _TmnxOamLspTrCtlLdpPrefixLen_Type()
)
tmnxOamLspTrCtlLdpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlLdpPrefixLen.setStatus("current")


class _TmnxOamLspTrCtlPathDestType_Type(InetAddressType):
    """Custom type tmnxOamLspTrCtlPathDestType based on InetAddressType"""


_TmnxOamLspTrCtlPathDestType_Object = MibTableColumn
tmnxOamLspTrCtlPathDestType = _TmnxOamLspTrCtlPathDestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 9),
    _TmnxOamLspTrCtlPathDestType_Type()
)
tmnxOamLspTrCtlPathDestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlPathDestType.setStatus("current")


class _TmnxOamLspTrCtlPathDest_Type(InetAddress):
    """Custom type tmnxOamLspTrCtlPathDest based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspTrCtlPathDest_Type.__name__ = "InetAddress"
_TmnxOamLspTrCtlPathDest_Object = MibTableColumn
tmnxOamLspTrCtlPathDest = _TmnxOamLspTrCtlPathDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 10),
    _TmnxOamLspTrCtlPathDest_Type()
)
tmnxOamLspTrCtlPathDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlPathDest.setStatus("current")


class _TmnxOamLspTrCtlNhIntfName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamLspTrCtlNhIntfName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamLspTrCtlNhIntfName_Object = MibTableColumn
tmnxOamLspTrCtlNhIntfName = _TmnxOamLspTrCtlNhIntfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 11),
    _TmnxOamLspTrCtlNhIntfName_Type()
)
tmnxOamLspTrCtlNhIntfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlNhIntfName.setStatus("current")


class _TmnxOamLspTrCtlNhAddressType_Type(InetAddressType):
    """Custom type tmnxOamLspTrCtlNhAddressType based on InetAddressType"""


_TmnxOamLspTrCtlNhAddressType_Object = MibTableColumn
tmnxOamLspTrCtlNhAddressType = _TmnxOamLspTrCtlNhAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 12),
    _TmnxOamLspTrCtlNhAddressType_Type()
)
tmnxOamLspTrCtlNhAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlNhAddressType.setStatus("current")


class _TmnxOamLspTrCtlNhAddress_Type(InetAddress):
    """Custom type tmnxOamLspTrCtlNhAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLspTrCtlNhAddress_Type.__name__ = "InetAddress"
_TmnxOamLspTrCtlNhAddress_Object = MibTableColumn
tmnxOamLspTrCtlNhAddress = _TmnxOamLspTrCtlNhAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 9, 1, 13),
    _TmnxOamLspTrCtlNhAddress_Type()
)
tmnxOamLspTrCtlNhAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLspTrCtlNhAddress.setStatus("current")
_TmnxOamLspTrMapTable_Object = MibTable
tmnxOamLspTrMapTable = _TmnxOamLspTrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10)
)
if mibBuilder.loadTexts:
    tmnxOamLspTrMapTable.setStatus("current")
_TmnxOamLspTrMapEntry_Object = MibTableRow
tmnxOamLspTrMapEntry = _TmnxOamLspTrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1)
)
tmnxOamLspTrMapEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLspTrMapEntry.setStatus("current")


class _TmnxOamLspTrMapIndex_Type(Unsigned32):
    """Custom type tmnxOamLspTrMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamLspTrMapIndex_Type.__name__ = "Unsigned32"
_TmnxOamLspTrMapIndex_Object = MibTableColumn
tmnxOamLspTrMapIndex = _TmnxOamLspTrMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 1),
    _TmnxOamLspTrMapIndex_Type()
)
tmnxOamLspTrMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapIndex.setStatus("current")
_TmnxOamLspTrMapDSIPv4Addr_Type = IpAddress
_TmnxOamLspTrMapDSIPv4Addr_Object = MibTableColumn
tmnxOamLspTrMapDSIPv4Addr = _TmnxOamLspTrMapDSIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 2),
    _TmnxOamLspTrMapDSIPv4Addr_Type()
)
tmnxOamLspTrMapDSIPv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapDSIPv4Addr.setStatus("current")
_TmnxOamLspTrMapAddrType_Type = TmnxOamAddressType
_TmnxOamLspTrMapAddrType_Object = MibTableColumn
tmnxOamLspTrMapAddrType = _TmnxOamLspTrMapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 3),
    _TmnxOamLspTrMapAddrType_Type()
)
tmnxOamLspTrMapAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapAddrType.setStatus("current")
_TmnxOamLspTrMapDSIfAddr_Type = Unsigned32
_TmnxOamLspTrMapDSIfAddr_Object = MibTableColumn
tmnxOamLspTrMapDSIfAddr = _TmnxOamLspTrMapDSIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 4),
    _TmnxOamLspTrMapDSIfAddr_Type()
)
tmnxOamLspTrMapDSIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapDSIfAddr.setStatus("current")


class _TmnxOamLspTrMapMTU_Type(Unsigned32):
    """Custom type tmnxOamLspTrMapMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxOamLspTrMapMTU_Type.__name__ = "Unsigned32"
_TmnxOamLspTrMapMTU_Object = MibTableColumn
tmnxOamLspTrMapMTU = _TmnxOamLspTrMapMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 5),
    _TmnxOamLspTrMapMTU_Type()
)
tmnxOamLspTrMapMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapMTU.setStatus("current")


class _TmnxOamLspTrMapDSIndex_Type(Unsigned32):
    """Custom type tmnxOamLspTrMapDSIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxOamLspTrMapDSIndex_Type.__name__ = "Unsigned32"
_TmnxOamLspTrMapDSIndex_Object = MibTableColumn
tmnxOamLspTrMapDSIndex = _TmnxOamLspTrMapDSIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 10, 1, 6),
    _TmnxOamLspTrMapDSIndex_Type()
)
tmnxOamLspTrMapDSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrMapDSIndex.setStatus("obsolete")
_TmnxOamVprnTrCtlTable_Object = MibTable
tmnxOamVprnTrCtlTable = _TmnxOamVprnTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 11)
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrCtlTable.setStatus("current")
_TmnxOamVprnTrCtlEntry_Object = MibTableRow
tmnxOamVprnTrCtlEntry = _TmnxOamVprnTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 11, 1)
)
tmnxOamVprnTrCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrCtlEntry.setStatus("current")


class _TmnxOamVprnTrCtlSourceIpAddr_Type(IpAddress):
    """Custom type tmnxOamVprnTrCtlSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamVprnTrCtlSourceIpAddr_Object = MibTableColumn
tmnxOamVprnTrCtlSourceIpAddr = _TmnxOamVprnTrCtlSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 11, 1, 1),
    _TmnxOamVprnTrCtlSourceIpAddr_Type()
)
tmnxOamVprnTrCtlSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnTrCtlSourceIpAddr.setStatus("obsolete")


class _TmnxOamVprnTrCtlReplyControl_Type(TruthValue):
    """Custom type tmnxOamVprnTrCtlReplyControl based on TruthValue"""


_TmnxOamVprnTrCtlReplyControl_Object = MibTableColumn
tmnxOamVprnTrCtlReplyControl = _TmnxOamVprnTrCtlReplyControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 11, 1, 2),
    _TmnxOamVprnTrCtlReplyControl_Type()
)
tmnxOamVprnTrCtlReplyControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnTrCtlReplyControl.setStatus("current")


class _TmnxOamVprnTrCtlSrcAddrType_Type(InetAddressType):
    """Custom type tmnxOamVprnTrCtlSrcAddrType based on InetAddressType"""


_TmnxOamVprnTrCtlSrcAddrType_Object = MibTableColumn
tmnxOamVprnTrCtlSrcAddrType = _TmnxOamVprnTrCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 11, 1, 3),
    _TmnxOamVprnTrCtlSrcAddrType_Type()
)
tmnxOamVprnTrCtlSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnTrCtlSrcAddrType.setStatus("current")


class _TmnxOamVprnTrCtlSrcAddress_Type(InetAddress):
    """Custom type tmnxOamVprnTrCtlSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVprnTrCtlSrcAddress_Type.__name__ = "InetAddress"
_TmnxOamVprnTrCtlSrcAddress_Object = MibTableColumn
tmnxOamVprnTrCtlSrcAddress = _TmnxOamVprnTrCtlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 11, 1, 4),
    _TmnxOamVprnTrCtlSrcAddress_Type()
)
tmnxOamVprnTrCtlSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVprnTrCtlSrcAddress.setStatus("current")
_TmnxOamVprnTrL3MapTable_Object = MibTable
tmnxOamVprnTrL3MapTable = _TmnxOamVprnTrL3MapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12)
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapTable.setStatus("current")
_TmnxOamVprnTrL3MapEntry_Object = MibTableRow
tmnxOamVprnTrL3MapEntry = _TmnxOamVprnTrL3MapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1)
)
tmnxOamVprnTrL3MapEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapReporter"),
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapEntry.setStatus("current")


class _TmnxOamVprnTrL3MapReporter_Type(Integer32):
    """Custom type tmnxOamVprnTrL3MapReporter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("requestor", 1),
          ("responder", 2))
    )


_TmnxOamVprnTrL3MapReporter_Type.__name__ = "Integer32"
_TmnxOamVprnTrL3MapReporter_Object = MibTableColumn
tmnxOamVprnTrL3MapReporter = _TmnxOamVprnTrL3MapReporter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 1),
    _TmnxOamVprnTrL3MapReporter_Type()
)
tmnxOamVprnTrL3MapReporter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapReporter.setStatus("current")
_TmnxOamVprnTrL3MapRouterID_Type = RouterID
_TmnxOamVprnTrL3MapRouterID_Object = MibTableColumn
tmnxOamVprnTrL3MapRouterID = _TmnxOamVprnTrL3MapRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 2),
    _TmnxOamVprnTrL3MapRouterID_Type()
)
tmnxOamVprnTrL3MapRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRouterID.setStatus("current")
_TmnxOamVprnTrL3MapRteDestAddr_Type = IpAddress
_TmnxOamVprnTrL3MapRteDestAddr_Object = MibTableColumn
tmnxOamVprnTrL3MapRteDestAddr = _TmnxOamVprnTrL3MapRteDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 3),
    _TmnxOamVprnTrL3MapRteDestAddr_Type()
)
tmnxOamVprnTrL3MapRteDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRteDestAddr.setStatus("obsolete")
_TmnxOamVprnTrL3MapRteDestMask_Type = Unsigned32
_TmnxOamVprnTrL3MapRteDestMask_Object = MibTableColumn
tmnxOamVprnTrL3MapRteDestMask = _TmnxOamVprnTrL3MapRteDestMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 4),
    _TmnxOamVprnTrL3MapRteDestMask_Type()
)
tmnxOamVprnTrL3MapRteDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRteDestMask.setStatus("obsolete")
_TmnxOamVprnTrL3MapRteVprnLabel_Type = MplsLabel
_TmnxOamVprnTrL3MapRteVprnLabel_Object = MibTableColumn
tmnxOamVprnTrL3MapRteVprnLabel = _TmnxOamVprnTrL3MapRteVprnLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 5),
    _TmnxOamVprnTrL3MapRteVprnLabel_Type()
)
tmnxOamVprnTrL3MapRteVprnLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRteVprnLabel.setStatus("current")
_TmnxOamVprnTrL3MapRteMetrics_Type = Unsigned32
_TmnxOamVprnTrL3MapRteMetrics_Object = MibTableColumn
tmnxOamVprnTrL3MapRteMetrics = _TmnxOamVprnTrL3MapRteMetrics_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 6),
    _TmnxOamVprnTrL3MapRteMetrics_Type()
)
tmnxOamVprnTrL3MapRteMetrics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRteMetrics.setStatus("current")
_TmnxOamVprnTrL3MapRteLastUp_Type = DateAndTime
_TmnxOamVprnTrL3MapRteLastUp_Object = MibTableColumn
tmnxOamVprnTrL3MapRteLastUp = _TmnxOamVprnTrL3MapRteLastUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 7),
    _TmnxOamVprnTrL3MapRteLastUp_Type()
)
tmnxOamVprnTrL3MapRteLastUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRteLastUp.setStatus("current")


class _TmnxOamVprnTrL3MapRteOwner_Type(Integer32):
    """Custom type tmnxOamVprnTrL3MapRteOwner based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 9),
          ("any", 10),
          ("bgp", 6),
          ("bgpVpn", 7),
          ("invalid", 0),
          ("isis", 5),
          ("ldp", 8),
          ("local", 1),
          ("ospf", 4),
          ("rip", 3),
          ("static", 2))
    )


_TmnxOamVprnTrL3MapRteOwner_Type.__name__ = "Integer32"
_TmnxOamVprnTrL3MapRteOwner_Object = MibTableColumn
tmnxOamVprnTrL3MapRteOwner = _TmnxOamVprnTrL3MapRteOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 8),
    _TmnxOamVprnTrL3MapRteOwner_Type()
)
tmnxOamVprnTrL3MapRteOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRteOwner.setStatus("current")
_TmnxOamVprnTrL3MapRtePref_Type = Unsigned32
_TmnxOamVprnTrL3MapRtePref_Object = MibTableColumn
tmnxOamVprnTrL3MapRtePref = _TmnxOamVprnTrL3MapRtePref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 9),
    _TmnxOamVprnTrL3MapRtePref_Type()
)
tmnxOamVprnTrL3MapRtePref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRtePref.setStatus("current")
_TmnxOamVprnTrL3MapRteDist_Type = TmnxVPNRouteDistinguisher
_TmnxOamVprnTrL3MapRteDist_Object = MibTableColumn
tmnxOamVprnTrL3MapRteDist = _TmnxOamVprnTrL3MapRteDist_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 10),
    _TmnxOamVprnTrL3MapRteDist_Type()
)
tmnxOamVprnTrL3MapRteDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapRteDist.setStatus("current")
_TmnxOamVprnTrL3MapNumNextHops_Type = Unsigned32
_TmnxOamVprnTrL3MapNumNextHops_Object = MibTableColumn
tmnxOamVprnTrL3MapNumNextHops = _TmnxOamVprnTrL3MapNumNextHops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 11),
    _TmnxOamVprnTrL3MapNumNextHops_Type()
)
tmnxOamVprnTrL3MapNumNextHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapNumNextHops.setStatus("current")
_TmnxOamVprnTrL3MapNumRteTargets_Type = Unsigned32
_TmnxOamVprnTrL3MapNumRteTargets_Object = MibTableColumn
tmnxOamVprnTrL3MapNumRteTargets = _TmnxOamVprnTrL3MapNumRteTargets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 12),
    _TmnxOamVprnTrL3MapNumRteTargets_Type()
)
tmnxOamVprnTrL3MapNumRteTargets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapNumRteTargets.setStatus("current")
_TmnxOamVprnTrL3MapDestAddrType_Type = InetAddressType
_TmnxOamVprnTrL3MapDestAddrType_Object = MibTableColumn
tmnxOamVprnTrL3MapDestAddrType = _TmnxOamVprnTrL3MapDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 13),
    _TmnxOamVprnTrL3MapDestAddrType_Type()
)
tmnxOamVprnTrL3MapDestAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapDestAddrType.setStatus("current")


class _TmnxOamVprnTrL3MapDestAddress_Type(InetAddress):
    """Custom type tmnxOamVprnTrL3MapDestAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVprnTrL3MapDestAddress_Type.__name__ = "InetAddress"
_TmnxOamVprnTrL3MapDestAddress_Object = MibTableColumn
tmnxOamVprnTrL3MapDestAddress = _TmnxOamVprnTrL3MapDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 14),
    _TmnxOamVprnTrL3MapDestAddress_Type()
)
tmnxOamVprnTrL3MapDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapDestAddress.setStatus("current")
_TmnxOamVprnTrL3MapDestMaskLen_Type = InetAddressPrefixLength
_TmnxOamVprnTrL3MapDestMaskLen_Object = MibTableColumn
tmnxOamVprnTrL3MapDestMaskLen = _TmnxOamVprnTrL3MapDestMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 12, 1, 15),
    _TmnxOamVprnTrL3MapDestMaskLen_Type()
)
tmnxOamVprnTrL3MapDestMaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrL3MapDestMaskLen.setStatus("current")
_TmnxOamVprnTrNextHopTable_Object = MibTable
tmnxOamVprnTrNextHopTable = _TmnxOamVprnTrNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13)
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopTable.setStatus("current")
_TmnxOamVprnTrNextHopEntry_Object = MibTableRow
tmnxOamVprnTrNextHopEntry = _TmnxOamVprnTrNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1)
)
tmnxOamVprnTrNextHopEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapReporter"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopEntry.setStatus("current")


class _TmnxOamVprnTrNextHopIndex_Type(Unsigned32):
    """Custom type tmnxOamVprnTrNextHopIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamVprnTrNextHopIndex_Type.__name__ = "Unsigned32"
_TmnxOamVprnTrNextHopIndex_Object = MibTableColumn
tmnxOamVprnTrNextHopIndex = _TmnxOamVprnTrNextHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1, 1),
    _TmnxOamVprnTrNextHopIndex_Type()
)
tmnxOamVprnTrNextHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopIndex.setStatus("current")
_TmnxOamVprnTrNextHopRtrID_Type = RouterID
_TmnxOamVprnTrNextHopRtrID_Object = MibTableColumn
tmnxOamVprnTrNextHopRtrID = _TmnxOamVprnTrNextHopRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1, 2),
    _TmnxOamVprnTrNextHopRtrID_Type()
)
tmnxOamVprnTrNextHopRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopRtrID.setStatus("obsolete")


class _TmnxOamVprnTrNextHopType_Type(Integer32):
    """Custom type tmnxOamVprnTrNextHopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_TmnxOamVprnTrNextHopType_Type.__name__ = "Integer32"
_TmnxOamVprnTrNextHopType_Object = MibTableColumn
tmnxOamVprnTrNextHopType = _TmnxOamVprnTrNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1, 3),
    _TmnxOamVprnTrNextHopType_Type()
)
tmnxOamVprnTrNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopType.setStatus("current")
_TmnxOamVprnTrNextHopTunnelID_Type = TmnxTunnelID
_TmnxOamVprnTrNextHopTunnelID_Object = MibTableColumn
tmnxOamVprnTrNextHopTunnelID = _TmnxOamVprnTrNextHopTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1, 4),
    _TmnxOamVprnTrNextHopTunnelID_Type()
)
tmnxOamVprnTrNextHopTunnelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopTunnelID.setStatus("current")
_TmnxOamVprnTrNextHopTunnelType_Type = TmnxTunnelType
_TmnxOamVprnTrNextHopTunnelType_Object = MibTableColumn
tmnxOamVprnTrNextHopTunnelType = _TmnxOamVprnTrNextHopTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1, 5),
    _TmnxOamVprnTrNextHopTunnelType_Type()
)
tmnxOamVprnTrNextHopTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopTunnelType.setStatus("current")
_TmnxOamVprnTrNextHopIfIndex_Type = InterfaceIndex
_TmnxOamVprnTrNextHopIfIndex_Object = MibTableColumn
tmnxOamVprnTrNextHopIfIndex = _TmnxOamVprnTrNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1, 6),
    _TmnxOamVprnTrNextHopIfIndex_Type()
)
tmnxOamVprnTrNextHopIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopIfIndex.setStatus("current")
_TmnxOamVprnTrNextHopAddrType_Type = InetAddressType
_TmnxOamVprnTrNextHopAddrType_Object = MibTableColumn
tmnxOamVprnTrNextHopAddrType = _TmnxOamVprnTrNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1, 7),
    _TmnxOamVprnTrNextHopAddrType_Type()
)
tmnxOamVprnTrNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopAddrType.setStatus("current")


class _TmnxOamVprnTrNextHopAddress_Type(InetAddress):
    """Custom type tmnxOamVprnTrNextHopAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVprnTrNextHopAddress_Type.__name__ = "InetAddress"
_TmnxOamVprnTrNextHopAddress_Object = MibTableColumn
tmnxOamVprnTrNextHopAddress = _TmnxOamVprnTrNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 13, 1, 8),
    _TmnxOamVprnTrNextHopAddress_Type()
)
tmnxOamVprnTrNextHopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrNextHopAddress.setStatus("current")
_TmnxOamVprnTrRTTable_Object = MibTable
tmnxOamVprnTrRTTable = _TmnxOamVprnTrRTTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 14)
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrRTTable.setStatus("current")
_TmnxOamVprnTrRTEntry_Object = MibTableRow
tmnxOamVprnTrRTEntry = _TmnxOamVprnTrRTEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 14, 1)
)
tmnxOamVprnTrRTEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapReporter"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrRTIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrRTEntry.setStatus("current")


class _TmnxOamVprnTrRTIndex_Type(Unsigned32):
    """Custom type tmnxOamVprnTrRTIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamVprnTrRTIndex_Type.__name__ = "Unsigned32"
_TmnxOamVprnTrRTIndex_Object = MibTableColumn
tmnxOamVprnTrRTIndex = _TmnxOamVprnTrRTIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 14, 1, 1),
    _TmnxOamVprnTrRTIndex_Type()
)
tmnxOamVprnTrRTIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamVprnTrRTIndex.setStatus("current")
_TmnxOamVprnTrRouteTarget_Type = TmnxBgpRouteTarget
_TmnxOamVprnTrRouteTarget_Object = MibTableColumn
tmnxOamVprnTrRouteTarget = _TmnxOamVprnTrRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 14, 1, 2),
    _TmnxOamVprnTrRouteTarget_Type()
)
tmnxOamVprnTrRouteTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVprnTrRouteTarget.setStatus("current")
_TmnxOamLspTrDSLabelTable_Object = MibTable
tmnxOamLspTrDSLabelTable = _TmnxOamLspTrDSLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 15)
)
if mibBuilder.loadTexts:
    tmnxOamLspTrDSLabelTable.setStatus("current")
_TmnxOamLspTrDSLabelEntry_Object = MibTableRow
tmnxOamLspTrDSLabelEntry = _TmnxOamLspTrDSLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 15, 1)
)
tmnxOamLspTrDSLabelEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrDSLabelIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLspTrDSLabelEntry.setStatus("current")


class _TmnxOamLspTrDSLabelIndex_Type(Unsigned32):
    """Custom type tmnxOamLspTrDSLabelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamLspTrDSLabelIndex_Type.__name__ = "Unsigned32"
_TmnxOamLspTrDSLabelIndex_Object = MibTableColumn
tmnxOamLspTrDSLabelIndex = _TmnxOamLspTrDSLabelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 15, 1, 1),
    _TmnxOamLspTrDSLabelIndex_Type()
)
tmnxOamLspTrDSLabelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLspTrDSLabelIndex.setStatus("current")
_TmnxOamLspTrDSLabelLabel_Type = MplsLabel
_TmnxOamLspTrDSLabelLabel_Object = MibTableColumn
tmnxOamLspTrDSLabelLabel = _TmnxOamLspTrDSLabelLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 15, 1, 2),
    _TmnxOamLspTrDSLabelLabel_Type()
)
tmnxOamLspTrDSLabelLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrDSLabelLabel.setStatus("current")
_TmnxOamLspTrDSLabelProtocol_Type = TmnxOamSignalProtocol
_TmnxOamLspTrDSLabelProtocol_Object = MibTableColumn
tmnxOamLspTrDSLabelProtocol = _TmnxOamLspTrDSLabelProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 15, 1, 3),
    _TmnxOamLspTrDSLabelProtocol_Type()
)
tmnxOamLspTrDSLabelProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLspTrDSLabelProtocol.setStatus("current")
_TmnxOamMcastTrCtlTable_Object = MibTable
tmnxOamMcastTrCtlTable = _TmnxOamMcastTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16)
)
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlTable.setStatus("current")
_TmnxOamMcastTrCtlEntry_Object = MibTableRow
tmnxOamMcastTrCtlEntry = _TmnxOamMcastTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1)
)
tmnxOamMcastTrCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlEntry.setStatus("current")


class _TmnxOamMcastTrCtlVRtrID_Type(TmnxVRtrID):
    """Custom type tmnxOamMcastTrCtlVRtrID based on TmnxVRtrID"""
    defaultValue = 1


_TmnxOamMcastTrCtlVRtrID_Object = MibTableColumn
tmnxOamMcastTrCtlVRtrID = _TmnxOamMcastTrCtlVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 1),
    _TmnxOamMcastTrCtlVRtrID_Type()
)
tmnxOamMcastTrCtlVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlVRtrID.setStatus("current")
_TmnxOamMcastTrCtlSrcIpAddr_Type = IpAddress
_TmnxOamMcastTrCtlSrcIpAddr_Object = MibTableColumn
tmnxOamMcastTrCtlSrcIpAddr = _TmnxOamMcastTrCtlSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 2),
    _TmnxOamMcastTrCtlSrcIpAddr_Type()
)
tmnxOamMcastTrCtlSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlSrcIpAddr.setStatus("obsolete")


class _TmnxOamMcastTrCtlDestIpAddr_Type(IpAddress):
    """Custom type tmnxOamMcastTrCtlDestIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxOamMcastTrCtlDestIpAddr_Object = MibTableColumn
tmnxOamMcastTrCtlDestIpAddr = _TmnxOamMcastTrCtlDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 3),
    _TmnxOamMcastTrCtlDestIpAddr_Type()
)
tmnxOamMcastTrCtlDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlDestIpAddr.setStatus("obsolete")
_TmnxOamMcastTrCtlRespIpAddr_Type = IpAddress
_TmnxOamMcastTrCtlRespIpAddr_Object = MibTableColumn
tmnxOamMcastTrCtlRespIpAddr = _TmnxOamMcastTrCtlRespIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 4),
    _TmnxOamMcastTrCtlRespIpAddr_Type()
)
tmnxOamMcastTrCtlRespIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlRespIpAddr.setStatus("obsolete")
_TmnxOamMcastTrCtlGrpIpAddr_Type = IpAddress
_TmnxOamMcastTrCtlGrpIpAddr_Object = MibTableColumn
tmnxOamMcastTrCtlGrpIpAddr = _TmnxOamMcastTrCtlGrpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 5),
    _TmnxOamMcastTrCtlGrpIpAddr_Type()
)
tmnxOamMcastTrCtlGrpIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlGrpIpAddr.setStatus("obsolete")


class _TmnxOamMcastTrCtlHops_Type(Unsigned32):
    """Custom type tmnxOamMcastTrCtlHops based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamMcastTrCtlHops_Type.__name__ = "Unsigned32"
_TmnxOamMcastTrCtlHops_Object = MibTableColumn
tmnxOamMcastTrCtlHops = _TmnxOamMcastTrCtlHops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 6),
    _TmnxOamMcastTrCtlHops_Type()
)
tmnxOamMcastTrCtlHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlHops.setStatus("current")
_TmnxOamMcastTrQueryId_Type = Unsigned32
_TmnxOamMcastTrQueryId_Object = MibTableColumn
tmnxOamMcastTrQueryId = _TmnxOamMcastTrQueryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 7),
    _TmnxOamMcastTrQueryId_Type()
)
tmnxOamMcastTrQueryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrQueryId.setStatus("current")


class _TmnxOamMcastTrCtlSrcAddrType_Type(InetAddressType):
    """Custom type tmnxOamMcastTrCtlSrcAddrType based on InetAddressType"""


_TmnxOamMcastTrCtlSrcAddrType_Object = MibTableColumn
tmnxOamMcastTrCtlSrcAddrType = _TmnxOamMcastTrCtlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 8),
    _TmnxOamMcastTrCtlSrcAddrType_Type()
)
tmnxOamMcastTrCtlSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlSrcAddrType.setStatus("current")


class _TmnxOamMcastTrCtlSrcAddress_Type(InetAddress):
    """Custom type tmnxOamMcastTrCtlSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMcastTrCtlSrcAddress_Type.__name__ = "InetAddress"
_TmnxOamMcastTrCtlSrcAddress_Object = MibTableColumn
tmnxOamMcastTrCtlSrcAddress = _TmnxOamMcastTrCtlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 9),
    _TmnxOamMcastTrCtlSrcAddress_Type()
)
tmnxOamMcastTrCtlSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlSrcAddress.setStatus("current")


class _TmnxOamMcastTrCtlDestAddrType_Type(InetAddressType):
    """Custom type tmnxOamMcastTrCtlDestAddrType based on InetAddressType"""


_TmnxOamMcastTrCtlDestAddrType_Object = MibTableColumn
tmnxOamMcastTrCtlDestAddrType = _TmnxOamMcastTrCtlDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 10),
    _TmnxOamMcastTrCtlDestAddrType_Type()
)
tmnxOamMcastTrCtlDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlDestAddrType.setStatus("current")


class _TmnxOamMcastTrCtlDestAddress_Type(InetAddress):
    """Custom type tmnxOamMcastTrCtlDestAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMcastTrCtlDestAddress_Type.__name__ = "InetAddress"
_TmnxOamMcastTrCtlDestAddress_Object = MibTableColumn
tmnxOamMcastTrCtlDestAddress = _TmnxOamMcastTrCtlDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 11),
    _TmnxOamMcastTrCtlDestAddress_Type()
)
tmnxOamMcastTrCtlDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlDestAddress.setStatus("current")


class _TmnxOamMcastTrCtlRespAddrType_Type(InetAddressType):
    """Custom type tmnxOamMcastTrCtlRespAddrType based on InetAddressType"""


_TmnxOamMcastTrCtlRespAddrType_Object = MibTableColumn
tmnxOamMcastTrCtlRespAddrType = _TmnxOamMcastTrCtlRespAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 12),
    _TmnxOamMcastTrCtlRespAddrType_Type()
)
tmnxOamMcastTrCtlRespAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlRespAddrType.setStatus("current")


class _TmnxOamMcastTrCtlRespAddress_Type(InetAddress):
    """Custom type tmnxOamMcastTrCtlRespAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMcastTrCtlRespAddress_Type.__name__ = "InetAddress"
_TmnxOamMcastTrCtlRespAddress_Object = MibTableColumn
tmnxOamMcastTrCtlRespAddress = _TmnxOamMcastTrCtlRespAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 13),
    _TmnxOamMcastTrCtlRespAddress_Type()
)
tmnxOamMcastTrCtlRespAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlRespAddress.setStatus("current")


class _TmnxOamMcastTrCtlGrpAddrType_Type(InetAddressType):
    """Custom type tmnxOamMcastTrCtlGrpAddrType based on InetAddressType"""


_TmnxOamMcastTrCtlGrpAddrType_Object = MibTableColumn
tmnxOamMcastTrCtlGrpAddrType = _TmnxOamMcastTrCtlGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 14),
    _TmnxOamMcastTrCtlGrpAddrType_Type()
)
tmnxOamMcastTrCtlGrpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlGrpAddrType.setStatus("current")


class _TmnxOamMcastTrCtlGrpAddress_Type(InetAddress):
    """Custom type tmnxOamMcastTrCtlGrpAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMcastTrCtlGrpAddress_Type.__name__ = "InetAddress"
_TmnxOamMcastTrCtlGrpAddress_Object = MibTableColumn
tmnxOamMcastTrCtlGrpAddress = _TmnxOamMcastTrCtlGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 16, 1, 15),
    _TmnxOamMcastTrCtlGrpAddress_Type()
)
tmnxOamMcastTrCtlGrpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamMcastTrCtlGrpAddress.setStatus("current")
_TmnxOamMcastTrRespTable_Object = MibTable
tmnxOamMcastTrRespTable = _TmnxOamMcastTrRespTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17)
)
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespTable.setStatus("current")
_TmnxOamMcastTrRespEntry_Object = MibTableRow
tmnxOamMcastTrRespEntry = _TmnxOamMcastTrRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1)
)
tmnxOamMcastTrRespEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespEntry.setStatus("current")
_TmnxOamMcastTrRespQueryArrivalTime_Type = Unsigned32
_TmnxOamMcastTrRespQueryArrivalTime_Object = MibTableColumn
tmnxOamMcastTrRespQueryArrivalTime = _TmnxOamMcastTrRespQueryArrivalTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 1),
    _TmnxOamMcastTrRespQueryArrivalTime_Type()
)
tmnxOamMcastTrRespQueryArrivalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespQueryArrivalTime.setStatus("current")
_TmnxOamMcastTrRespInIfAddr_Type = IpAddress
_TmnxOamMcastTrRespInIfAddr_Object = MibTableColumn
tmnxOamMcastTrRespInIfAddr = _TmnxOamMcastTrRespInIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 2),
    _TmnxOamMcastTrRespInIfAddr_Type()
)
tmnxOamMcastTrRespInIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespInIfAddr.setStatus("obsolete")
_TmnxOamMcastTrRespOutIfAddr_Type = IpAddress
_TmnxOamMcastTrRespOutIfAddr_Object = MibTableColumn
tmnxOamMcastTrRespOutIfAddr = _TmnxOamMcastTrRespOutIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 3),
    _TmnxOamMcastTrRespOutIfAddr_Type()
)
tmnxOamMcastTrRespOutIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespOutIfAddr.setStatus("obsolete")
_TmnxOamMcastTrRespPrevHopRtrAddr_Type = IpAddress
_TmnxOamMcastTrRespPrevHopRtrAddr_Object = MibTableColumn
tmnxOamMcastTrRespPrevHopRtrAddr = _TmnxOamMcastTrRespPrevHopRtrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 4),
    _TmnxOamMcastTrRespPrevHopRtrAddr_Type()
)
tmnxOamMcastTrRespPrevHopRtrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespPrevHopRtrAddr.setStatus("obsolete")
_TmnxOamMcastTrRespInPktCount_Type = Counter32
_TmnxOamMcastTrRespInPktCount_Object = MibTableColumn
tmnxOamMcastTrRespInPktCount = _TmnxOamMcastTrRespInPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 5),
    _TmnxOamMcastTrRespInPktCount_Type()
)
tmnxOamMcastTrRespInPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespInPktCount.setStatus("current")
_TmnxOamMcastTrRespOutPktCount_Type = Counter32
_TmnxOamMcastTrRespOutPktCount_Object = MibTableColumn
tmnxOamMcastTrRespOutPktCount = _TmnxOamMcastTrRespOutPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 6),
    _TmnxOamMcastTrRespOutPktCount_Type()
)
tmnxOamMcastTrRespOutPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespOutPktCount.setStatus("current")
_TmnxOamMcastTrRespSGPktCount_Type = Counter32
_TmnxOamMcastTrRespSGPktCount_Object = MibTableColumn
tmnxOamMcastTrRespSGPktCount = _TmnxOamMcastTrRespSGPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 7),
    _TmnxOamMcastTrRespSGPktCount_Type()
)
tmnxOamMcastTrRespSGPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespSGPktCount.setStatus("current")


class _TmnxOamMcastTrRespRtgProtocol_Type(Integer32):
    """Custom type tmnxOamMcastTrRespRtgProtocol based on Integer32"""
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("bgp4Plus", 8),
          ("cbt", 4),
          ("cbtSpecial", 9),
          ("cbtStatic", 10),
          ("dvmrp", 1),
          ("dvmrpStatic", 7),
          ("mospf", 2),
          ("pim", 3),
          ("pimAssert", 11),
          ("pimSpecial", 5),
          ("pimStatic", 6),
          ("unknown", 0))
    )


_TmnxOamMcastTrRespRtgProtocol_Type.__name__ = "Integer32"
_TmnxOamMcastTrRespRtgProtocol_Object = MibTableColumn
tmnxOamMcastTrRespRtgProtocol = _TmnxOamMcastTrRespRtgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 8),
    _TmnxOamMcastTrRespRtgProtocol_Type()
)
tmnxOamMcastTrRespRtgProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespRtgProtocol.setStatus("current")
_TmnxOamMcastTrRespFwdTtl_Type = Unsigned32
_TmnxOamMcastTrRespFwdTtl_Object = MibTableColumn
tmnxOamMcastTrRespFwdTtl = _TmnxOamMcastTrRespFwdTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 9),
    _TmnxOamMcastTrRespFwdTtl_Type()
)
tmnxOamMcastTrRespFwdTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespFwdTtl.setStatus("current")
_TmnxOamMcastTrRespMBZBit_Type = Unsigned32
_TmnxOamMcastTrRespMBZBit_Object = MibTableColumn
tmnxOamMcastTrRespMBZBit = _TmnxOamMcastTrRespMBZBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 10),
    _TmnxOamMcastTrRespMBZBit_Type()
)
tmnxOamMcastTrRespMBZBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespMBZBit.setStatus("current")
_TmnxOamMcastTrRespSrcBit_Type = Unsigned32
_TmnxOamMcastTrRespSrcBit_Object = MibTableColumn
tmnxOamMcastTrRespSrcBit = _TmnxOamMcastTrRespSrcBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 11),
    _TmnxOamMcastTrRespSrcBit_Type()
)
tmnxOamMcastTrRespSrcBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespSrcBit.setStatus("current")
_TmnxOamMcastTrRespSrcMask_Type = Unsigned32
_TmnxOamMcastTrRespSrcMask_Object = MibTableColumn
tmnxOamMcastTrRespSrcMask = _TmnxOamMcastTrRespSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 12),
    _TmnxOamMcastTrRespSrcMask_Type()
)
tmnxOamMcastTrRespSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespSrcMask.setStatus("current")


class _TmnxOamMcastTrRespFwdCode_Type(Integer32):
    """Custom type tmnxOamMcastTrRespFwdCode based on Integer32"""
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
              9,
              10,
              11,
              128,
              129,
              130,
              131,
              132)
        )
    )
    namedValues = NamedValues(
        *(("adminProhib", 131),
          ("fatalError", 128),
          ("infoHidden", 11),
          ("noError", 0),
          ("noMulticast", 10),
          ("noRoute", 5),
          ("noSpace", 129),
          ("notForwarding", 7),
          ("oldRouter", 130),
          ("pruneRecvd", 3),
          ("pruneSent", 2),
          ("reachedRP", 8),
          ("rpfIf", 9),
          ("scoped", 4),
          ("unknown", 132),
          ("wrongIf", 1),
          ("wrongLastHop", 6))
    )


_TmnxOamMcastTrRespFwdCode_Type.__name__ = "Integer32"
_TmnxOamMcastTrRespFwdCode_Object = MibTableColumn
tmnxOamMcastTrRespFwdCode = _TmnxOamMcastTrRespFwdCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 13),
    _TmnxOamMcastTrRespFwdCode_Type()
)
tmnxOamMcastTrRespFwdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespFwdCode.setStatus("current")
_TmnxOamMcastTrRespInIfAddrType_Type = InetAddressType
_TmnxOamMcastTrRespInIfAddrType_Object = MibTableColumn
tmnxOamMcastTrRespInIfAddrType = _TmnxOamMcastTrRespInIfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 14),
    _TmnxOamMcastTrRespInIfAddrType_Type()
)
tmnxOamMcastTrRespInIfAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespInIfAddrType.setStatus("current")


class _TmnxOamMcastTrRespInIfAddress_Type(InetAddress):
    """Custom type tmnxOamMcastTrRespInIfAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMcastTrRespInIfAddress_Type.__name__ = "InetAddress"
_TmnxOamMcastTrRespInIfAddress_Object = MibTableColumn
tmnxOamMcastTrRespInIfAddress = _TmnxOamMcastTrRespInIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 15),
    _TmnxOamMcastTrRespInIfAddress_Type()
)
tmnxOamMcastTrRespInIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespInIfAddress.setStatus("current")
_TmnxOamMcastTrRespOutIfAddrType_Type = InetAddressType
_TmnxOamMcastTrRespOutIfAddrType_Object = MibTableColumn
tmnxOamMcastTrRespOutIfAddrType = _TmnxOamMcastTrRespOutIfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 16),
    _TmnxOamMcastTrRespOutIfAddrType_Type()
)
tmnxOamMcastTrRespOutIfAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespOutIfAddrType.setStatus("current")


class _TmnxOamMcastTrRespOutIfAddress_Type(InetAddress):
    """Custom type tmnxOamMcastTrRespOutIfAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMcastTrRespOutIfAddress_Type.__name__ = "InetAddress"
_TmnxOamMcastTrRespOutIfAddress_Object = MibTableColumn
tmnxOamMcastTrRespOutIfAddress = _TmnxOamMcastTrRespOutIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 17),
    _TmnxOamMcastTrRespOutIfAddress_Type()
)
tmnxOamMcastTrRespOutIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespOutIfAddress.setStatus("current")
_TmnxOamMcastTrRespPhRtrAddrType_Type = InetAddressType
_TmnxOamMcastTrRespPhRtrAddrType_Object = MibTableColumn
tmnxOamMcastTrRespPhRtrAddrType = _TmnxOamMcastTrRespPhRtrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 18),
    _TmnxOamMcastTrRespPhRtrAddrType_Type()
)
tmnxOamMcastTrRespPhRtrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespPhRtrAddrType.setStatus("current")


class _TmnxOamMcastTrRespPhRtrAddress_Type(InetAddress):
    """Custom type tmnxOamMcastTrRespPhRtrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamMcastTrRespPhRtrAddress_Type.__name__ = "InetAddress"
_TmnxOamMcastTrRespPhRtrAddress_Object = MibTableColumn
tmnxOamMcastTrRespPhRtrAddress = _TmnxOamMcastTrRespPhRtrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 17, 1, 19),
    _TmnxOamMcastTrRespPhRtrAddress_Type()
)
tmnxOamMcastTrRespPhRtrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamMcastTrRespPhRtrAddress.setStatus("current")
_TmnxOamLTtraceCtlTable_Object = MibTable
tmnxOamLTtraceCtlTable = _TmnxOamLTtraceCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 18)
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceCtlTable.setStatus("current")
_TmnxOamLTtraceCtlEntry_Object = MibTableRow
tmnxOamLTtraceCtlEntry = _TmnxOamLTtraceCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 18, 1)
)
tmnxOamLTtraceCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceCtlEntry.setStatus("current")


class _TmnxOamLTtraceCtlLdpPrefixType_Type(InetAddressType):
    """Custom type tmnxOamLTtraceCtlLdpPrefixType based on InetAddressType"""


_TmnxOamLTtraceCtlLdpPrefixType_Object = MibTableColumn
tmnxOamLTtraceCtlLdpPrefixType = _TmnxOamLTtraceCtlLdpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 18, 1, 2),
    _TmnxOamLTtraceCtlLdpPrefixType_Type()
)
tmnxOamLTtraceCtlLdpPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceCtlLdpPrefixType.setStatus("current")


class _TmnxOamLTtraceCtlLdpPrefix_Type(InetAddress):
    """Custom type tmnxOamLTtraceCtlLdpPrefix based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtraceCtlLdpPrefix_Type.__name__ = "InetAddress"
_TmnxOamLTtraceCtlLdpPrefix_Object = MibTableColumn
tmnxOamLTtraceCtlLdpPrefix = _TmnxOamLTtraceCtlLdpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 18, 1, 3),
    _TmnxOamLTtraceCtlLdpPrefix_Type()
)
tmnxOamLTtraceCtlLdpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceCtlLdpPrefix.setStatus("current")


class _TmnxOamLTtraceCtlLdpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxOamLTtraceCtlLdpPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 32


_TmnxOamLTtraceCtlLdpPrefixLen_Object = MibTableColumn
tmnxOamLTtraceCtlLdpPrefixLen = _TmnxOamLTtraceCtlLdpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 18, 1, 4),
    _TmnxOamLTtraceCtlLdpPrefixLen_Type()
)
tmnxOamLTtraceCtlLdpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceCtlLdpPrefixLen.setStatus("current")


class _TmnxOamLTtraceCtlMaxPath_Type(Unsigned32):
    """Custom type tmnxOamLTtraceCtlMaxPath based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamLTtraceCtlMaxPath_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceCtlMaxPath_Object = MibTableColumn
tmnxOamLTtraceCtlMaxPath = _TmnxOamLTtraceCtlMaxPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 18, 1, 5),
    _TmnxOamLTtraceCtlMaxPath_Type()
)
tmnxOamLTtraceCtlMaxPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceCtlMaxPath.setStatus("current")
_TmnxOamLTtraceMaxConRequests_Type = Unsigned32
_TmnxOamLTtraceMaxConRequests_Object = MibScalar
tmnxOamLTtraceMaxConRequests = _TmnxOamLTtraceMaxConRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 19),
    _TmnxOamLTtraceMaxConRequests_Type()
)
tmnxOamLTtraceMaxConRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceMaxConRequests.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceMaxConRequests.setUnits("requests")
_TmnxOamLTtraceResultsTable_Object = MibTable
tmnxOamLTtraceResultsTable = _TmnxOamLTtraceResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 20)
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceResultsTable.setStatus("current")
_TmnxOamLTtraceResultsEntry_Object = MibTableRow
tmnxOamLTtraceResultsEntry = _TmnxOamLTtraceResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 20, 1)
)
tmnxOamLTtraceResultsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceResultsEntry.setStatus("current")
_TmnxOamLTtraceResultsDisPaths_Type = Unsigned32
_TmnxOamLTtraceResultsDisPaths_Object = MibTableColumn
tmnxOamLTtraceResultsDisPaths = _TmnxOamLTtraceResultsDisPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 20, 1, 2),
    _TmnxOamLTtraceResultsDisPaths_Type()
)
tmnxOamLTtraceResultsDisPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceResultsDisPaths.setStatus("current")
_TmnxOamLTtraceResultsFailedHops_Type = Unsigned32
_TmnxOamLTtraceResultsFailedHops_Object = MibTableColumn
tmnxOamLTtraceResultsFailedHops = _TmnxOamLTtraceResultsFailedHops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 20, 1, 3),
    _TmnxOamLTtraceResultsFailedHops_Type()
)
tmnxOamLTtraceResultsFailedHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceResultsFailedHops.setStatus("current")


class _TmnxOamLTtraceResultsDisState_Type(Integer32):
    """Custom type tmnxOamLTtraceResultsDisState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("done", 2),
          ("inProgress", 1),
          ("initial", 0))
    )


_TmnxOamLTtraceResultsDisState_Type.__name__ = "Integer32"
_TmnxOamLTtraceResultsDisState_Object = MibTableColumn
tmnxOamLTtraceResultsDisState = _TmnxOamLTtraceResultsDisState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 20, 1, 4),
    _TmnxOamLTtraceResultsDisState_Type()
)
tmnxOamLTtraceResultsDisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceResultsDisState.setStatus("current")
_TmnxOamLTtraceResultsDisStatus_Type = TmnxOamLTtraceDisStatusBits
_TmnxOamLTtraceResultsDisStatus_Object = MibTableColumn
tmnxOamLTtraceResultsDisStatus = _TmnxOamLTtraceResultsDisStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 20, 1, 5),
    _TmnxOamLTtraceResultsDisStatus_Type()
)
tmnxOamLTtraceResultsDisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceResultsDisStatus.setStatus("current")
_TmnxOamLTtraceHopInfoTable_Object = MibTable
tmnxOamLTtraceHopInfoTable = _TmnxOamLTtraceHopInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21)
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopInfoTable.setStatus("current")
_TmnxOamLTtraceHopInfoEntry_Object = MibTableRow
tmnxOamLTtraceHopInfoEntry = _TmnxOamLTtraceHopInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1)
)
tmnxOamLTtraceHopInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopInfoEntry.setStatus("current")
_TmnxOamLTtraceHopIndex_Type = Unsigned32
_TmnxOamLTtraceHopIndex_Object = MibTableColumn
tmnxOamLTtraceHopIndex = _TmnxOamLTtraceHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 1),
    _TmnxOamLTtraceHopIndex_Type()
)
tmnxOamLTtraceHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopIndex.setStatus("current")
_TmnxOamLTtraceUpStreamHopIndex_Type = Unsigned32
_TmnxOamLTtraceUpStreamHopIndex_Object = MibTableColumn
tmnxOamLTtraceUpStreamHopIndex = _TmnxOamLTtraceUpStreamHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 2),
    _TmnxOamLTtraceUpStreamHopIndex_Type()
)
tmnxOamLTtraceUpStreamHopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceUpStreamHopIndex.setStatus("current")
_TmnxOamLTtraceHopAddrType_Type = InetAddressType
_TmnxOamLTtraceHopAddrType_Object = MibTableColumn
tmnxOamLTtraceHopAddrType = _TmnxOamLTtraceHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 3),
    _TmnxOamLTtraceHopAddrType_Type()
)
tmnxOamLTtraceHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopAddrType.setStatus("current")


class _TmnxOamLTtraceHopAddr_Type(InetAddress):
    """Custom type tmnxOamLTtraceHopAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtraceHopAddr_Type.__name__ = "InetAddress"
_TmnxOamLTtraceHopAddr_Object = MibTableColumn
tmnxOamLTtraceHopAddr = _TmnxOamLTtraceHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 4),
    _TmnxOamLTtraceHopAddr_Type()
)
tmnxOamLTtraceHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopAddr.setStatus("current")
_TmnxOamLTtraceHopDstAddrType_Type = InetAddressType
_TmnxOamLTtraceHopDstAddrType_Object = MibTableColumn
tmnxOamLTtraceHopDstAddrType = _TmnxOamLTtraceHopDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 5),
    _TmnxOamLTtraceHopDstAddrType_Type()
)
tmnxOamLTtraceHopDstAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopDstAddrType.setStatus("current")


class _TmnxOamLTtraceHopDstAddr_Type(InetAddress):
    """Custom type tmnxOamLTtraceHopDstAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtraceHopDstAddr_Type.__name__ = "InetAddress"
_TmnxOamLTtraceHopDstAddr_Object = MibTableColumn
tmnxOamLTtraceHopDstAddr = _TmnxOamLTtraceHopDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 6),
    _TmnxOamLTtraceHopDstAddr_Type()
)
tmnxOamLTtraceHopDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopDstAddr.setStatus("current")
_TmnxOamLTtraceHopEgrNhAddrType_Type = InetAddressType
_TmnxOamLTtraceHopEgrNhAddrType_Object = MibTableColumn
tmnxOamLTtraceHopEgrNhAddrType = _TmnxOamLTtraceHopEgrNhAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 7),
    _TmnxOamLTtraceHopEgrNhAddrType_Type()
)
tmnxOamLTtraceHopEgrNhAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopEgrNhAddrType.setStatus("current")


class _TmnxOamLTtraceHopEgrNhAddr_Type(InetAddress):
    """Custom type tmnxOamLTtraceHopEgrNhAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtraceHopEgrNhAddr_Type.__name__ = "InetAddress"
_TmnxOamLTtraceHopEgrNhAddr_Object = MibTableColumn
tmnxOamLTtraceHopEgrNhAddr = _TmnxOamLTtraceHopEgrNhAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 8),
    _TmnxOamLTtraceHopEgrNhAddr_Type()
)
tmnxOamLTtraceHopEgrNhAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopEgrNhAddr.setStatus("current")
_TmnxOamLTtraceHopDisTtl_Type = Unsigned32
_TmnxOamLTtraceHopDisTtl_Object = MibTableColumn
tmnxOamLTtraceHopDisTtl = _TmnxOamLTtraceHopDisTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 9),
    _TmnxOamLTtraceHopDisTtl_Type()
)
tmnxOamLTtraceHopDisTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopDisTtl.setStatus("current")
_TmnxOamLTtraceHopLastRc_Type = TmnxOamPingRtnCode
_TmnxOamLTtraceHopLastRc_Object = MibTableColumn
tmnxOamLTtraceHopLastRc = _TmnxOamLTtraceHopLastRc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 10),
    _TmnxOamLTtraceHopLastRc_Type()
)
tmnxOamLTtraceHopLastRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopLastRc.setStatus("current")


class _TmnxOamLTtraceHopDiscoveryState_Type(Integer32):
    """Custom type tmnxOamLTtraceHopDiscoveryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("doneExpiredTtl", 4),
          ("doneLoopDetected", 3),
          ("doneOk", 1),
          ("doneTimeout", 2),
          ("inProgress", 0))
    )


_TmnxOamLTtraceHopDiscoveryState_Type.__name__ = "Integer32"
_TmnxOamLTtraceHopDiscoveryState_Object = MibTableColumn
tmnxOamLTtraceHopDiscoveryState = _TmnxOamLTtraceHopDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 11),
    _TmnxOamLTtraceHopDiscoveryState_Type()
)
tmnxOamLTtraceHopDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopDiscoveryState.setStatus("current")
_TmnxOamLTtraceHopDiscoveryTime_Type = TimeStamp
_TmnxOamLTtraceHopDiscoveryTime_Object = MibTableColumn
tmnxOamLTtraceHopDiscoveryTime = _TmnxOamLTtraceHopDiscoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 21, 1, 12),
    _TmnxOamLTtraceHopDiscoveryTime_Type()
)
tmnxOamLTtraceHopDiscoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceHopDiscoveryTime.setStatus("current")
_TmnxOamLTtraceAutoConfigTable_Object = MibTable
tmnxOamLTtraceAutoConfigTable = _TmnxOamLTtraceAutoConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22)
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoConfigTable.setStatus("current")
_TmnxOamLTtraceAutoConfigEntry_Object = MibTableRow
tmnxOamLTtraceAutoConfigEntry = _TmnxOamLTtraceAutoConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1)
)
tmnxOamLTtraceAutoConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoConfigEntry.setStatus("current")
_TmnxOamLTtraceAutoRowStatus_Type = RowStatus
_TmnxOamLTtraceAutoRowStatus_Object = MibTableColumn
tmnxOamLTtraceAutoRowStatus = _TmnxOamLTtraceAutoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 1),
    _TmnxOamLTtraceAutoRowStatus_Type()
)
tmnxOamLTtraceAutoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoRowStatus.setStatus("current")
_TmnxOamLTtraceAutoLastChanged_Type = TimeStamp
_TmnxOamLTtraceAutoLastChanged_Object = MibTableColumn
tmnxOamLTtraceAutoLastChanged = _TmnxOamLTtraceAutoLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 2),
    _TmnxOamLTtraceAutoLastChanged_Type()
)
tmnxOamLTtraceAutoLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoLastChanged.setStatus("current")


class _TmnxOamLTtraceAutoStorageType_Type(StorageType):
    """Custom type tmnxOamLTtraceAutoStorageType based on StorageType"""


_TmnxOamLTtraceAutoStorageType_Object = MibTableColumn
tmnxOamLTtraceAutoStorageType = _TmnxOamLTtraceAutoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 3),
    _TmnxOamLTtraceAutoStorageType_Type()
)
tmnxOamLTtraceAutoStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoStorageType.setStatus("current")


class _TmnxOamLTtraceAutoAdminState_Type(TmnxAdminState):
    """Custom type tmnxOamLTtraceAutoAdminState based on TmnxAdminState"""


_TmnxOamLTtraceAutoAdminState_Object = MibTableColumn
tmnxOamLTtraceAutoAdminState = _TmnxOamLTtraceAutoAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 4),
    _TmnxOamLTtraceAutoAdminState_Type()
)
tmnxOamLTtraceAutoAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoAdminState.setStatus("current")


class _TmnxOamLTtraceAutoFcName_Type(TFCName):
    """Custom type tmnxOamLTtraceAutoFcName based on TFCName"""
    defaultValue = OctetString("be")


_TmnxOamLTtraceAutoFcName_Object = MibTableColumn
tmnxOamLTtraceAutoFcName = _TmnxOamLTtraceAutoFcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 5),
    _TmnxOamLTtraceAutoFcName_Type()
)
tmnxOamLTtraceAutoFcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoFcName.setStatus("current")


class _TmnxOamLTtraceAutoProfile_Type(TProfile):
    """Custom type tmnxOamLTtraceAutoProfile based on TProfile"""


_TmnxOamLTtraceAutoProfile_Object = MibTableColumn
tmnxOamLTtraceAutoProfile = _TmnxOamLTtraceAutoProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 6),
    _TmnxOamLTtraceAutoProfile_Type()
)
tmnxOamLTtraceAutoProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoProfile.setStatus("current")


class _TmnxOamLTtraceAutoDiscIntvl_Type(Unsigned32):
    """Custom type tmnxOamLTtraceAutoDiscIntvl based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1440),
    )


_TmnxOamLTtraceAutoDiscIntvl_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceAutoDiscIntvl_Object = MibTableColumn
tmnxOamLTtraceAutoDiscIntvl = _TmnxOamLTtraceAutoDiscIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 7),
    _TmnxOamLTtraceAutoDiscIntvl_Type()
)
tmnxOamLTtraceAutoDiscIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoDiscIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoDiscIntvl.setUnits("minutes")


class _TmnxOamLTtraceAutoMaxPath_Type(Unsigned32):
    """Custom type tmnxOamLTtraceAutoMaxPath based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TmnxOamLTtraceAutoMaxPath_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceAutoMaxPath_Object = MibTableColumn
tmnxOamLTtraceAutoMaxPath = _TmnxOamLTtraceAutoMaxPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 8),
    _TmnxOamLTtraceAutoMaxPath_Type()
)
tmnxOamLTtraceAutoMaxPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoMaxPath.setStatus("current")


class _TmnxOamLTtraceAutoTrMaxTtl_Type(Unsigned32):
    """Custom type tmnxOamLTtraceAutoTrMaxTtl based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamLTtraceAutoTrMaxTtl_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceAutoTrMaxTtl_Object = MibTableColumn
tmnxOamLTtraceAutoTrMaxTtl = _TmnxOamLTtraceAutoTrMaxTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 9),
    _TmnxOamLTtraceAutoTrMaxTtl_Type()
)
tmnxOamLTtraceAutoTrMaxTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoTrMaxTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoTrMaxTtl.setUnits("time-to-live value")


class _TmnxOamLTtraceAutoTrTimeOut_Type(Unsigned32):
    """Custom type tmnxOamLTtraceAutoTrTimeOut based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxOamLTtraceAutoTrTimeOut_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceAutoTrTimeOut_Object = MibTableColumn
tmnxOamLTtraceAutoTrTimeOut = _TmnxOamLTtraceAutoTrTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 10),
    _TmnxOamLTtraceAutoTrTimeOut_Type()
)
tmnxOamLTtraceAutoTrTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoTrTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoTrTimeOut.setUnits("seconds")


class _TmnxOamLTtraceAutoTrMaxFailures_Type(Unsigned32):
    """Custom type tmnxOamLTtraceAutoTrMaxFailures based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxOamLTtraceAutoTrMaxFailures_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceAutoTrMaxFailures_Object = MibTableColumn
tmnxOamLTtraceAutoTrMaxFailures = _TmnxOamLTtraceAutoTrMaxFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 11),
    _TmnxOamLTtraceAutoTrMaxFailures_Type()
)
tmnxOamLTtraceAutoTrMaxFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoTrMaxFailures.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoTrMaxFailures.setUnits("timeouts")


class _TmnxOamLTtraceAutoPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxOamLTtraceAutoPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxOamLTtraceAutoPolicy1_Object = MibTableColumn
tmnxOamLTtraceAutoPolicy1 = _TmnxOamLTtraceAutoPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 12),
    _TmnxOamLTtraceAutoPolicy1_Type()
)
tmnxOamLTtraceAutoPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPolicy1.setStatus("current")


class _TmnxOamLTtraceAutoPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxOamLTtraceAutoPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxOamLTtraceAutoPolicy2_Object = MibTableColumn
tmnxOamLTtraceAutoPolicy2 = _TmnxOamLTtraceAutoPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 13),
    _TmnxOamLTtraceAutoPolicy2_Type()
)
tmnxOamLTtraceAutoPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPolicy2.setStatus("current")


class _TmnxOamLTtraceAutoPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxOamLTtraceAutoPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxOamLTtraceAutoPolicy3_Object = MibTableColumn
tmnxOamLTtraceAutoPolicy3 = _TmnxOamLTtraceAutoPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 14),
    _TmnxOamLTtraceAutoPolicy3_Type()
)
tmnxOamLTtraceAutoPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPolicy3.setStatus("current")


class _TmnxOamLTtraceAutoPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxOamLTtraceAutoPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxOamLTtraceAutoPolicy4_Object = MibTableColumn
tmnxOamLTtraceAutoPolicy4 = _TmnxOamLTtraceAutoPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 15),
    _TmnxOamLTtraceAutoPolicy4_Type()
)
tmnxOamLTtraceAutoPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPolicy4.setStatus("current")


class _TmnxOamLTtraceAutoPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type tmnxOamLTtraceAutoPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_TmnxOamLTtraceAutoPolicy5_Object = MibTableColumn
tmnxOamLTtraceAutoPolicy5 = _TmnxOamLTtraceAutoPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 16),
    _TmnxOamLTtraceAutoPolicy5_Type()
)
tmnxOamLTtraceAutoPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPolicy5.setStatus("current")


class _TmnxOamLTtraceAutoProbeIntvl_Type(Unsigned32):
    """Custom type tmnxOamLTtraceAutoProbeIntvl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxOamLTtraceAutoProbeIntvl_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceAutoProbeIntvl_Object = MibTableColumn
tmnxOamLTtraceAutoProbeIntvl = _TmnxOamLTtraceAutoProbeIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 17),
    _TmnxOamLTtraceAutoProbeIntvl_Type()
)
tmnxOamLTtraceAutoProbeIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoProbeIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoProbeIntvl.setUnits("minutes")


class _TmnxOamLTtraceAutoPrTimeOut_Type(Unsigned32):
    """Custom type tmnxOamLTtraceAutoPrTimeOut based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TmnxOamLTtraceAutoPrTimeOut_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceAutoPrTimeOut_Object = MibTableColumn
tmnxOamLTtraceAutoPrTimeOut = _TmnxOamLTtraceAutoPrTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 18),
    _TmnxOamLTtraceAutoPrTimeOut_Type()
)
tmnxOamLTtraceAutoPrTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPrTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPrTimeOut.setUnits("minutes")


class _TmnxOamLTtraceAutoPrMaxFailures_Type(Unsigned32):
    """Custom type tmnxOamLTtraceAutoPrMaxFailures based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxOamLTtraceAutoPrMaxFailures_Type.__name__ = "Unsigned32"
_TmnxOamLTtraceAutoPrMaxFailures_Object = MibTableColumn
tmnxOamLTtraceAutoPrMaxFailures = _TmnxOamLTtraceAutoPrMaxFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 22, 1, 19),
    _TmnxOamLTtraceAutoPrMaxFailures_Type()
)
tmnxOamLTtraceAutoPrMaxFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPrMaxFailures.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoPrMaxFailures.setUnits("timeouts")
_TmnxOamLTtraceAutoStatusTable_Object = MibTable
tmnxOamLTtraceAutoStatusTable = _TmnxOamLTtraceAutoStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 23)
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoStatusTable.setStatus("current")
_TmnxOamLTtraceAutoStatusEntry_Object = MibTableRow
tmnxOamLTtraceAutoStatusEntry = _TmnxOamLTtraceAutoStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 23, 1)
)
tmnxOamLTtraceAutoStatusEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoStatusEntry.setStatus("current")


class _TmnxOamLTtraceAutoDiscoveryState_Type(Integer32):
    """Custom type tmnxOamLTtraceAutoDiscoveryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("done", 2),
          ("halt", 3),
          ("inProgress", 1),
          ("initial", 0))
    )


_TmnxOamLTtraceAutoDiscoveryState_Type.__name__ = "Integer32"
_TmnxOamLTtraceAutoDiscoveryState_Object = MibTableColumn
tmnxOamLTtraceAutoDiscoveryState = _TmnxOamLTtraceAutoDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 23, 1, 1),
    _TmnxOamLTtraceAutoDiscoveryState_Type()
)
tmnxOamLTtraceAutoDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoDiscoveryState.setStatus("current")
_TmnxOamLTtraceAutoTotalFecs_Type = Unsigned32
_TmnxOamLTtraceAutoTotalFecs_Object = MibTableColumn
tmnxOamLTtraceAutoTotalFecs = _TmnxOamLTtraceAutoTotalFecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 23, 1, 2),
    _TmnxOamLTtraceAutoTotalFecs_Type()
)
tmnxOamLTtraceAutoTotalFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoTotalFecs.setStatus("current")
_TmnxOamLTtraceAutoDisFecs_Type = Unsigned32
_TmnxOamLTtraceAutoDisFecs_Object = MibTableColumn
tmnxOamLTtraceAutoDisFecs = _TmnxOamLTtraceAutoDisFecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 23, 1, 3),
    _TmnxOamLTtraceAutoDisFecs_Type()
)
tmnxOamLTtraceAutoDisFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoDisFecs.setStatus("current")
_TmnxOamLTtraceAutoLastDisStart_Type = TimeStamp
_TmnxOamLTtraceAutoLastDisStart_Object = MibTableColumn
tmnxOamLTtraceAutoLastDisStart = _TmnxOamLTtraceAutoLastDisStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 23, 1, 4),
    _TmnxOamLTtraceAutoLastDisStart_Type()
)
tmnxOamLTtraceAutoLastDisStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoLastDisStart.setStatus("current")
_TmnxOamLTtraceAutoLastDisEnd_Type = TimeStamp
_TmnxOamLTtraceAutoLastDisEnd_Object = MibTableColumn
tmnxOamLTtraceAutoLastDisEnd = _TmnxOamLTtraceAutoLastDisEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 23, 1, 5),
    _TmnxOamLTtraceAutoLastDisEnd_Type()
)
tmnxOamLTtraceAutoLastDisEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoLastDisEnd.setStatus("current")
_TmnxOamLTtraceAutoLastDisDur_Type = Unsigned32
_TmnxOamLTtraceAutoLastDisDur_Object = MibTableColumn
tmnxOamLTtraceAutoLastDisDur = _TmnxOamLTtraceAutoLastDisDur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 23, 1, 6),
    _TmnxOamLTtraceAutoLastDisDur_Type()
)
tmnxOamLTtraceAutoLastDisDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoLastDisDur.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamLTtraceAutoLastDisDur.setUnits("seconds")
_TmnxOamLTtraceFecInfoTable_Object = MibTable
tmnxOamLTtraceFecInfoTable = _TmnxOamLTtraceFecInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24)
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecInfoTable.setStatus("current")
_TmnxOamLTtraceFecInfoEntry_Object = MibTableRow
tmnxOamLTtraceFecInfoEntry = _TmnxOamLTtraceFecInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1)
)
tmnxOamLTtraceFecInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecPrefixType"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecPrefix"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecPrefLen"),
)
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecInfoEntry.setStatus("current")
_TmnxOamLTtraceFecPrefixType_Type = InetAddressType
_TmnxOamLTtraceFecPrefixType_Object = MibTableColumn
tmnxOamLTtraceFecPrefixType = _TmnxOamLTtraceFecPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 1),
    _TmnxOamLTtraceFecPrefixType_Type()
)
tmnxOamLTtraceFecPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecPrefixType.setStatus("current")


class _TmnxOamLTtraceFecPrefix_Type(InetAddress):
    """Custom type tmnxOamLTtraceFecPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtraceFecPrefix_Type.__name__ = "InetAddress"
_TmnxOamLTtraceFecPrefix_Object = MibTableColumn
tmnxOamLTtraceFecPrefix = _TmnxOamLTtraceFecPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 2),
    _TmnxOamLTtraceFecPrefix_Type()
)
tmnxOamLTtraceFecPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecPrefix.setStatus("current")
_TmnxOamLTtraceFecPrefLen_Type = InetAddressPrefixLength
_TmnxOamLTtraceFecPrefLen_Object = MibTableColumn
tmnxOamLTtraceFecPrefLen = _TmnxOamLTtraceFecPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 3),
    _TmnxOamLTtraceFecPrefLen_Type()
)
tmnxOamLTtraceFecPrefLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecPrefLen.setStatus("current")


class _TmnxOamLTtraceFecDiscoveryState_Type(Integer32):
    """Custom type tmnxOamLTtraceFecDiscoveryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("done", 2),
          ("inProgress", 1),
          ("initial", 0))
    )


_TmnxOamLTtraceFecDiscoveryState_Type.__name__ = "Integer32"
_TmnxOamLTtraceFecDiscoveryState_Object = MibTableColumn
tmnxOamLTtraceFecDiscoveryState = _TmnxOamLTtraceFecDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 4),
    _TmnxOamLTtraceFecDiscoveryState_Type()
)
tmnxOamLTtraceFecDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecDiscoveryState.setStatus("current")
_TmnxOamLTtraceFecDisStatusBits_Type = TmnxOamLTtraceDisStatusBits
_TmnxOamLTtraceFecDisStatusBits_Object = MibTableColumn
tmnxOamLTtraceFecDisStatusBits = _TmnxOamLTtraceFecDisStatusBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 5),
    _TmnxOamLTtraceFecDisStatusBits_Type()
)
tmnxOamLTtraceFecDisStatusBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecDisStatusBits.setStatus("current")
_TmnxOamLTtraceFecDisPaths_Type = Unsigned32
_TmnxOamLTtraceFecDisPaths_Object = MibTableColumn
tmnxOamLTtraceFecDisPaths = _TmnxOamLTtraceFecDisPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 6),
    _TmnxOamLTtraceFecDisPaths_Type()
)
tmnxOamLTtraceFecDisPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecDisPaths.setStatus("current")
_TmnxOamLTtraceFecFailedHops_Type = Unsigned32
_TmnxOamLTtraceFecFailedHops_Object = MibTableColumn
tmnxOamLTtraceFecFailedHops = _TmnxOamLTtraceFecFailedHops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 7),
    _TmnxOamLTtraceFecFailedHops_Type()
)
tmnxOamLTtraceFecFailedHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecFailedHops.setStatus("current")
_TmnxOamLTtraceFecLastDisEnd_Type = TimeStamp
_TmnxOamLTtraceFecLastDisEnd_Object = MibTableColumn
tmnxOamLTtraceFecLastDisEnd = _TmnxOamLTtraceFecLastDisEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 8),
    _TmnxOamLTtraceFecLastDisEnd_Type()
)
tmnxOamLTtraceFecLastDisEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecLastDisEnd.setStatus("current")
_TmnxOamLTtraceFecFailedProbes_Type = Unsigned32
_TmnxOamLTtraceFecFailedProbes_Object = MibTableColumn
tmnxOamLTtraceFecFailedProbes = _TmnxOamLTtraceFecFailedProbes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 9),
    _TmnxOamLTtraceFecFailedProbes_Type()
)
tmnxOamLTtraceFecFailedProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecFailedProbes.setStatus("current")


class _TmnxOamLTtraceFecProbeState_Type(Integer32):
    """Custom type tmnxOamLTtraceFecProbeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("oK", 0),
          ("partiallyFailed", 1))
    )


_TmnxOamLTtraceFecProbeState_Type.__name__ = "Integer32"
_TmnxOamLTtraceFecProbeState_Object = MibTableColumn
tmnxOamLTtraceFecProbeState = _TmnxOamLTtraceFecProbeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 24, 1, 10),
    _TmnxOamLTtraceFecProbeState_Type()
)
tmnxOamLTtraceFecProbeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtraceFecProbeState.setStatus("current")
_TmnxOamLTtracePathInfoTable_Object = MibTable
tmnxOamLTtracePathInfoTable = _TmnxOamLTtracePathInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25)
)
if mibBuilder.loadTexts:
    tmnxOamLTtracePathInfoTable.setStatus("current")
_TmnxOamLTtracePathInfoEntry_Object = MibTableRow
tmnxOamLTtracePathInfoEntry = _TmnxOamLTtracePathInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1)
)
tmnxOamLTtracePathInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecPrefixType"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecPrefix"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecPrefLen"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathDstAddrType"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathDstAddr"),
)
if mibBuilder.loadTexts:
    tmnxOamLTtracePathInfoEntry.setStatus("current")
_TmnxOamLTtracePathDstAddrType_Type = InetAddressType
_TmnxOamLTtracePathDstAddrType_Object = MibTableColumn
tmnxOamLTtracePathDstAddrType = _TmnxOamLTtracePathDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 1),
    _TmnxOamLTtracePathDstAddrType_Type()
)
tmnxOamLTtracePathDstAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathDstAddrType.setStatus("current")


class _TmnxOamLTtracePathDstAddr_Type(InetAddress):
    """Custom type tmnxOamLTtracePathDstAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtracePathDstAddr_Type.__name__ = "InetAddress"
_TmnxOamLTtracePathDstAddr_Object = MibTableColumn
tmnxOamLTtracePathDstAddr = _TmnxOamLTtracePathDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 2),
    _TmnxOamLTtracePathDstAddr_Type()
)
tmnxOamLTtracePathDstAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathDstAddr.setStatus("current")
_TmnxOamLTtracePathRemAddrType_Type = InetAddressType
_TmnxOamLTtracePathRemAddrType_Object = MibTableColumn
tmnxOamLTtracePathRemAddrType = _TmnxOamLTtracePathRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 3),
    _TmnxOamLTtracePathRemAddrType_Type()
)
tmnxOamLTtracePathRemAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathRemAddrType.setStatus("current")


class _TmnxOamLTtracePathRemoteAddr_Type(InetAddress):
    """Custom type tmnxOamLTtracePathRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtracePathRemoteAddr_Type.__name__ = "InetAddress"
_TmnxOamLTtracePathRemoteAddr_Object = MibTableColumn
tmnxOamLTtracePathRemoteAddr = _TmnxOamLTtracePathRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 4),
    _TmnxOamLTtracePathRemoteAddr_Type()
)
tmnxOamLTtracePathRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathRemoteAddr.setStatus("current")
_TmnxOamLTtracePathEgrNhAddrType_Type = InetAddressType
_TmnxOamLTtracePathEgrNhAddrType_Object = MibTableColumn
tmnxOamLTtracePathEgrNhAddrType = _TmnxOamLTtracePathEgrNhAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 5),
    _TmnxOamLTtracePathEgrNhAddrType_Type()
)
tmnxOamLTtracePathEgrNhAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathEgrNhAddrType.setStatus("current")


class _TmnxOamLTtracePathEgrNhAddr_Type(InetAddress):
    """Custom type tmnxOamLTtracePathEgrNhAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamLTtracePathEgrNhAddr_Type.__name__ = "InetAddress"
_TmnxOamLTtracePathEgrNhAddr_Object = MibTableColumn
tmnxOamLTtracePathEgrNhAddr = _TmnxOamLTtracePathEgrNhAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 6),
    _TmnxOamLTtracePathEgrNhAddr_Type()
)
tmnxOamLTtracePathEgrNhAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathEgrNhAddr.setStatus("current")
_TmnxOamLTtracePathDisTtl_Type = Unsigned32
_TmnxOamLTtracePathDisTtl_Object = MibTableColumn
tmnxOamLTtracePathDisTtl = _TmnxOamLTtracePathDisTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 7),
    _TmnxOamLTtracePathDisTtl_Type()
)
tmnxOamLTtracePathDisTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathDisTtl.setStatus("current")
_TmnxOamLTtracePathLastDisTime_Type = TimeStamp
_TmnxOamLTtracePathLastDisTime_Object = MibTableColumn
tmnxOamLTtracePathLastDisTime = _TmnxOamLTtracePathLastDisTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 8),
    _TmnxOamLTtracePathLastDisTime_Type()
)
tmnxOamLTtracePathLastDisTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathLastDisTime.setStatus("current")
_TmnxOamLTtracePathLastRc_Type = TmnxOamPingRtnCode
_TmnxOamLTtracePathLastRc_Object = MibTableColumn
tmnxOamLTtracePathLastRc = _TmnxOamLTtracePathLastRc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 9),
    _TmnxOamLTtracePathLastRc_Type()
)
tmnxOamLTtracePathLastRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathLastRc.setStatus("current")


class _TmnxOamLTtracePathProbeState_Type(Integer32):
    """Custom type tmnxOamLTtracePathProbeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("oK", 0))
    )


_TmnxOamLTtracePathProbeState_Type.__name__ = "Integer32"
_TmnxOamLTtracePathProbeState_Object = MibTableColumn
tmnxOamLTtracePathProbeState = _TmnxOamLTtracePathProbeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 10),
    _TmnxOamLTtracePathProbeState_Type()
)
tmnxOamLTtracePathProbeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathProbeState.setStatus("current")
_TmnxOamLTtracePathProbeTmOutCnt_Type = Unsigned32
_TmnxOamLTtracePathProbeTmOutCnt_Object = MibTableColumn
tmnxOamLTtracePathProbeTmOutCnt = _TmnxOamLTtracePathProbeTmOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 25, 1, 11),
    _TmnxOamLTtracePathProbeTmOutCnt_Type()
)
tmnxOamLTtracePathProbeTmOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamLTtracePathProbeTmOutCnt.setStatus("current")
_TmnxOamVccvTrCtlTable_Object = MibTable
tmnxOamVccvTrCtlTable = _TmnxOamVccvTrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26)
)
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlTable.setStatus("current")
_TmnxOamVccvTrCtlEntry_Object = MibTableRow
tmnxOamVccvTrCtlEntry = _TmnxOamVccvTrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26, 1)
)
tmnxOamVccvTrCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlEntry.setStatus("current")


class _TmnxOamVccvTrCtlSdpIdVcId_Type(SdpBindId):
    """Custom type tmnxOamVccvTrCtlSdpIdVcId based on SdpBindId"""
    defaultHexValue = "0000000000000000"


_TmnxOamVccvTrCtlSdpIdVcId_Object = MibTableColumn
tmnxOamVccvTrCtlSdpIdVcId = _TmnxOamVccvTrCtlSdpIdVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26, 1, 1),
    _TmnxOamVccvTrCtlSdpIdVcId_Type()
)
tmnxOamVccvTrCtlSdpIdVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlSdpIdVcId.setStatus("current")


class _TmnxOamVccvTrCtlReplyMode_Type(Integer32):
    """Custom type tmnxOamVccvTrCtlReplyMode based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("controlChannel", 4),
          ("ip", 2))
    )


_TmnxOamVccvTrCtlReplyMode_Type.__name__ = "Integer32"
_TmnxOamVccvTrCtlReplyMode_Object = MibTableColumn
tmnxOamVccvTrCtlReplyMode = _TmnxOamVccvTrCtlReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 26, 1, 2),
    _TmnxOamVccvTrCtlReplyMode_Type()
)
tmnxOamVccvTrCtlReplyMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamVccvTrCtlReplyMode.setStatus("current")
_TmnxOamVccvTrNextPwSegmentTable_Object = MibTable
tmnxOamVccvTrNextPwSegmentTable = _TmnxOamVccvTrNextPwSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27)
)
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextPwSegmentTable.setStatus("current")
_TmnxOamVccvTrNextPwSegmentEntry_Object = MibTableRow
tmnxOamVccvTrNextPwSegmentEntry = _TmnxOamVccvTrNextPwSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1)
)
tmnxOamVccvTrNextPwSegmentEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestRunIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryHopIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryProbeIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextPwSegmentEntry.setStatus("current")
_TmnxOamVccvTrNextPwID_Type = TmnxVcIdOrNone
_TmnxOamVccvTrNextPwID_Object = MibTableColumn
tmnxOamVccvTrNextPwID = _TmnxOamVccvTrNextPwID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 1),
    _TmnxOamVccvTrNextPwID_Type()
)
tmnxOamVccvTrNextPwID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextPwID.setStatus("current")
_TmnxOamVccvTrNextPwType_Type = SdpBindVcType
_TmnxOamVccvTrNextPwType_Object = MibTableColumn
tmnxOamVccvTrNextPwType = _TmnxOamVccvTrNextPwType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 2),
    _TmnxOamVccvTrNextPwType_Type()
)
tmnxOamVccvTrNextPwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextPwType.setStatus("current")
_TmnxOamVccvTrNextSenderAddrType_Type = InetAddressType
_TmnxOamVccvTrNextSenderAddrType_Object = MibTableColumn
tmnxOamVccvTrNextSenderAddrType = _TmnxOamVccvTrNextSenderAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 3),
    _TmnxOamVccvTrNextSenderAddrType_Type()
)
tmnxOamVccvTrNextSenderAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextSenderAddrType.setStatus("current")


class _TmnxOamVccvTrNextSenderAddr_Type(InetAddress):
    """Custom type tmnxOamVccvTrNextSenderAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVccvTrNextSenderAddr_Type.__name__ = "InetAddress"
_TmnxOamVccvTrNextSenderAddr_Object = MibTableColumn
tmnxOamVccvTrNextSenderAddr = _TmnxOamVccvTrNextSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 4),
    _TmnxOamVccvTrNextSenderAddr_Type()
)
tmnxOamVccvTrNextSenderAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextSenderAddr.setStatus("current")
_TmnxOamVccvTrNextRemoteAddrType_Type = InetAddressType
_TmnxOamVccvTrNextRemoteAddrType_Object = MibTableColumn
tmnxOamVccvTrNextRemoteAddrType = _TmnxOamVccvTrNextRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 5),
    _TmnxOamVccvTrNextRemoteAddrType_Type()
)
tmnxOamVccvTrNextRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextRemoteAddrType.setStatus("current")


class _TmnxOamVccvTrNextRemoteAddr_Type(InetAddress):
    """Custom type tmnxOamVccvTrNextRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamVccvTrNextRemoteAddr_Type.__name__ = "InetAddress"
_TmnxOamVccvTrNextRemoteAddr_Object = MibTableColumn
tmnxOamVccvTrNextRemoteAddr = _TmnxOamVccvTrNextRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 2, 27, 1, 6),
    _TmnxOamVccvTrNextRemoteAddr_Type()
)
tmnxOamVccvTrNextRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamVccvTrNextRemoteAddr.setStatus("current")
_TmnxOamSaaObjs_ObjectIdentity = ObjectIdentity
tmnxOamSaaObjs = _TmnxOamSaaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3)
)
_TmnxOamSaaNotifyObjects_ObjectIdentity = ObjectIdentity
tmnxOamSaaNotifyObjects = _TmnxOamSaaNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 1)
)
_TmnxOamSaaCtlTable_Object = MibTable
tmnxOamSaaCtlTable = _TmnxOamSaaCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxOamSaaCtlTable.setStatus("current")
_TmnxOamSaaCtlEntry_Object = MibTableRow
tmnxOamSaaCtlEntry = _TmnxOamSaaCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1)
)
tmnxOamSaaCtlEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlTestIndex"),
)
if mibBuilder.loadTexts:
    tmnxOamSaaCtlEntry.setStatus("current")


class _TmnxOamSaaCtlOwnerIndex_Type(SnmpAdminString):
    """Custom type tmnxOamSaaCtlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxOamSaaCtlOwnerIndex_Type.__name__ = "SnmpAdminString"
_TmnxOamSaaCtlOwnerIndex_Object = MibTableColumn
tmnxOamSaaCtlOwnerIndex = _TmnxOamSaaCtlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 1),
    _TmnxOamSaaCtlOwnerIndex_Type()
)
tmnxOamSaaCtlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlOwnerIndex.setStatus("current")


class _TmnxOamSaaCtlTestIndex_Type(SnmpAdminString):
    """Custom type tmnxOamSaaCtlTestIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxOamSaaCtlTestIndex_Type.__name__ = "SnmpAdminString"
_TmnxOamSaaCtlTestIndex_Object = MibTableColumn
tmnxOamSaaCtlTestIndex = _TmnxOamSaaCtlTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 2),
    _TmnxOamSaaCtlTestIndex_Type()
)
tmnxOamSaaCtlTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlTestIndex.setStatus("current")
_TmnxOamSaaCtlRowStatus_Type = RowStatus
_TmnxOamSaaCtlRowStatus_Object = MibTableColumn
tmnxOamSaaCtlRowStatus = _TmnxOamSaaCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 3),
    _TmnxOamSaaCtlRowStatus_Type()
)
tmnxOamSaaCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlRowStatus.setStatus("current")


class _TmnxOamSaaCtlStorageType_Type(StorageType):
    """Custom type tmnxOamSaaCtlStorageType based on StorageType"""


_TmnxOamSaaCtlStorageType_Object = MibTableColumn
tmnxOamSaaCtlStorageType = _TmnxOamSaaCtlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 4),
    _TmnxOamSaaCtlStorageType_Type()
)
tmnxOamSaaCtlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlStorageType.setStatus("current")
_TmnxOamSaaCtlLastChanged_Type = TimeStamp
_TmnxOamSaaCtlLastChanged_Object = MibTableColumn
tmnxOamSaaCtlLastChanged = _TmnxOamSaaCtlLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 5),
    _TmnxOamSaaCtlLastChanged_Type()
)
tmnxOamSaaCtlLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlLastChanged.setStatus("current")


class _TmnxOamSaaCtlAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxOamSaaCtlAdminStatus based on TmnxAdminState"""


_TmnxOamSaaCtlAdminStatus_Object = MibTableColumn
tmnxOamSaaCtlAdminStatus = _TmnxOamSaaCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 6),
    _TmnxOamSaaCtlAdminStatus_Type()
)
tmnxOamSaaCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlAdminStatus.setStatus("current")


class _TmnxOamSaaCtlDescr_Type(TItemDescription):
    """Custom type tmnxOamSaaCtlDescr based on TItemDescription"""
    defaultHexValue = ""


_TmnxOamSaaCtlDescr_Object = MibTableColumn
tmnxOamSaaCtlDescr = _TmnxOamSaaCtlDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 7),
    _TmnxOamSaaCtlDescr_Type()
)
tmnxOamSaaCtlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlDescr.setStatus("current")


class _TmnxOamSaaCtlTestMode_Type(TmnxOamTestMode):
    """Custom type tmnxOamSaaCtlTestMode based on TmnxOamTestMode"""


_TmnxOamSaaCtlTestMode_Object = MibTableColumn
tmnxOamSaaCtlTestMode = _TmnxOamSaaCtlTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 8),
    _TmnxOamSaaCtlTestMode_Type()
)
tmnxOamSaaCtlTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlTestMode.setStatus("current")
_TmnxOamSaaCtlRuns_Type = Counter32
_TmnxOamSaaCtlRuns_Object = MibTableColumn
tmnxOamSaaCtlRuns = _TmnxOamSaaCtlRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 9),
    _TmnxOamSaaCtlRuns_Type()
)
tmnxOamSaaCtlRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlRuns.setStatus("current")
_TmnxOamSaaCtlFailures_Type = Counter32
_TmnxOamSaaCtlFailures_Object = MibTableColumn
tmnxOamSaaCtlFailures = _TmnxOamSaaCtlFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 10),
    _TmnxOamSaaCtlFailures_Type()
)
tmnxOamSaaCtlFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlFailures.setStatus("current")


class _TmnxOamSaaCtlLastRunResult_Type(Integer32):
    """Custom type tmnxOamSaaCtlLastRunResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 3),
          ("failed", 2),
          ("success", 1),
          ("undetermined", 0))
    )


_TmnxOamSaaCtlLastRunResult_Type.__name__ = "Integer32"
_TmnxOamSaaCtlLastRunResult_Object = MibTableColumn
tmnxOamSaaCtlLastRunResult = _TmnxOamSaaCtlLastRunResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 2, 1, 11),
    _TmnxOamSaaCtlLastRunResult_Type()
)
tmnxOamSaaCtlLastRunResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaCtlLastRunResult.setStatus("current")
_TmnxOamSaaThresholdTable_Object = MibTable
tmnxOamSaaThresholdTable = _TmnxOamSaaThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxOamSaaThresholdTable.setStatus("current")
_TmnxOamSaaThresholdEntry_Object = MibTableRow
tmnxOamSaaThresholdEntry = _TmnxOamSaaThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1)
)
tmnxOamSaaThresholdEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlOwnerIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlTestIndex"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTType"),
    (0, "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTDirection"),
)
if mibBuilder.loadTexts:
    tmnxOamSaaThresholdEntry.setStatus("current")
_TmnxOamSaaTType_Type = TmnxOamSaaThreshold
_TmnxOamSaaTType_Object = MibTableColumn
tmnxOamSaaTType = _TmnxOamSaaTType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 1),
    _TmnxOamSaaTType_Type()
)
tmnxOamSaaTType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamSaaTType.setStatus("current")


class _TmnxOamSaaTDirection_Type(Integer32):
    """Custom type tmnxOamSaaTDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("falling", 2),
          ("rising", 1))
    )


_TmnxOamSaaTDirection_Type.__name__ = "Integer32"
_TmnxOamSaaTDirection_Object = MibTableColumn
tmnxOamSaaTDirection = _TmnxOamSaaTDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 2),
    _TmnxOamSaaTDirection_Type()
)
tmnxOamSaaTDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamSaaTDirection.setStatus("current")
_TmnxOamSaaTRowStatus_Type = RowStatus
_TmnxOamSaaTRowStatus_Object = MibTableColumn
tmnxOamSaaTRowStatus = _TmnxOamSaaTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 3),
    _TmnxOamSaaTRowStatus_Type()
)
tmnxOamSaaTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamSaaTRowStatus.setStatus("current")
_TmnxOamSaaTLastChanged_Type = TimeStamp
_TmnxOamSaaTLastChanged_Object = MibTableColumn
tmnxOamSaaTLastChanged = _TmnxOamSaaTLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 4),
    _TmnxOamSaaTLastChanged_Type()
)
tmnxOamSaaTLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaTLastChanged.setStatus("current")


class _TmnxOamSaaTThreshold_Type(Integer32):
    """Custom type tmnxOamSaaTThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOamSaaTThreshold_Type.__name__ = "Integer32"
_TmnxOamSaaTThreshold_Object = MibTableColumn
tmnxOamSaaTThreshold = _TmnxOamSaaTThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 5),
    _TmnxOamSaaTThreshold_Type()
)
tmnxOamSaaTThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamSaaTThreshold.setStatus("current")
_TmnxOamSaaTValue_Type = Integer32
_TmnxOamSaaTValue_Object = MibTableColumn
tmnxOamSaaTValue = _TmnxOamSaaTValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 6),
    _TmnxOamSaaTValue_Type()
)
tmnxOamSaaTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaTValue.setStatus("current")
_TmnxOamSaaTLastSent_Type = TimeStamp
_TmnxOamSaaTLastSent_Object = MibTableColumn
tmnxOamSaaTLastSent = _TmnxOamSaaTLastSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 7),
    _TmnxOamSaaTLastSent_Type()
)
tmnxOamSaaTLastSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaTLastSent.setStatus("current")
_TmnxOamSaaTTestMode_Type = TmnxOamTestMode
_TmnxOamSaaTTestMode_Object = MibTableColumn
tmnxOamSaaTTestMode = _TmnxOamSaaTTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 8),
    _TmnxOamSaaTTestMode_Type()
)
tmnxOamSaaTTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaTTestMode.setStatus("current")
_TmnxOamSaaTTestRunIndex_Type = Unsigned32
_TmnxOamSaaTTestRunIndex_Object = MibTableColumn
tmnxOamSaaTTestRunIndex = _TmnxOamSaaTTestRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 11, 3, 3, 1, 9),
    _TmnxOamSaaTTestRunIndex_Type()
)
tmnxOamSaaTTestRunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamSaaTTestRunIndex.setStatus("current")
_TmnxOamTestNotifications_ObjectIdentity = ObjectIdentity
tmnxOamTestNotifications = _TmnxOamTestNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11)
)
_TmnxOamPingNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxOamPingNotifyPrefix = _TmnxOamPingNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1)
)
_TmnxOamPingNotifications_ObjectIdentity = ObjectIdentity
tmnxOamPingNotifications = _TmnxOamPingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0)
)
_TmnxOamTraceRouteNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxOamTraceRouteNotifyPrefix = _TmnxOamTraceRouteNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 2)
)
_TmnxOamTraceRouteNotifications_ObjectIdentity = ObjectIdentity
tmnxOamTraceRouteNotifications = _TmnxOamTraceRouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 2, 0)
)
_TmnxOamSaaNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxOamSaaNotifyPrefix = _TmnxOamSaaNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 3)
)
_TmnxOamSaaNotifications_ObjectIdentity = ObjectIdentity
tmnxOamSaaNotifications = _TmnxOamSaaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 3, 0)
)

# Managed Objects groups

tmnxOamMacPingL2MapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 3)
)
tmnxOamMacPingL2MapGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapRouterID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapLabel"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapProtocol"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapVCType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapVCID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingL2MapDirection"))
)
if mibBuilder.loadTexts:
    tmnxOamMacPingL2MapGroup.setStatus("current")

tmnxOamAtmPingR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 8)
)
tmnxOamAtmPingR2r1Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingCtlPortId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingCtlVpi"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingCtlVci"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingCtlLpbkLocation"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamAtmPingCtlSegment"))
)
if mibBuilder.loadTexts:
    tmnxOamAtmPingR2r1Group.setStatus("current")

tmnxOamMacPingV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 14)
)
tmnxOamMacPingV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlTargetMacAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlSourceMacAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlSendControl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlReplyControl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlTtl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlRegister"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlFlood"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlForce"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlAge"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlSapPortId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlSapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingCtlFibEntryName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryResponse"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryOneWayTime"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryTime"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryReturnCode"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryAddressType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistorySapId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistorySdpId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryOperStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryResponsePlane"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistorySize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistoryInOneWayTime"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistorySrcAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistorySrcAddress"))
)
if mibBuilder.loadTexts:
    tmnxOamMacPingV4v0Group.setStatus("current")

tmnxOamVccvPingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 15)
)
tmnxOamVccvPingGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlSdpIdVcId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlReplyMode"))
)
if mibBuilder.loadTexts:
    tmnxOamVccvPingGroup.setStatus("obsolete")

tmnxOamPingGeneralV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 16)
)
tmnxOamPingGeneralV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingMaxConcurrentTests"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRowStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlStorageType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDescr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestMode"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOrigSdpId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRespSdpId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlFcName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlProfile"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuStartSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuEndSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuStepSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlServiceId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLocalSdp"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRemoteSdp"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTimeOut"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlProbeCount"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlInterval"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMaxRows"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapGeneration"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapProbeFailureFilter"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapTestFailureFilter"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSAA"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRuns"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlFailures"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLastRunResult"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLastChanged"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlVRtrID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSrcAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSrcAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDnsName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastRespHeader"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTtSumOfSquares"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinInTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxInTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageInTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInTtSumOfSqrs"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOutJitter"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInJitter"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRtJitter"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeTimeouts"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeFailures"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryResponse"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryOneWayTime"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryTime"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryReturnCode"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistAddressType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryVersion"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistSapId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryCpeMacAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespSvcId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySequence"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryIfIndex"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDataLen"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespPlane"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryReqHdr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespHdr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDnsAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDnsAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryInOneWayTime"))
)
if mibBuilder.loadTexts:
    tmnxOamPingGeneralV4v0Group.setStatus("obsolete")

tmnxOamLspPingV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 17)
)
tmnxOamLspPingV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlVRtrID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLspName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlReturnLsp"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlTtl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlPathName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefixType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefix"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefixLen"))
)
if mibBuilder.loadTexts:
    tmnxOamLspPingV4v0Group.setStatus("obsolete")

tmnxOamVprnPingV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 19)
)
tmnxOamVprnPingV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingCtlReplyControl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingCtlTtl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingCtlSrcAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingCtlSrcAddress"))
)
if mibBuilder.loadTexts:
    tmnxOamVprnPingV4v0Group.setStatus("current")

tmnxOamMfibPingV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 20)
)
tmnxOamMfibPingV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlReplyControl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlTtl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlSrcAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlSrcAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlDestAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlDestAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespSvcId"))
)
if mibBuilder.loadTexts:
    tmnxOamMfibPingV4v0Group.setStatus("obsolete")

tmnxOamCpePingV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 21)
)
tmnxOamCpePingV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingCtlSendControl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingCtlReplyControl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingCtlTtl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingCtlSrceMacAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingCtlSrcAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingCtlSrcAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryCpeMacAddr"))
)
if mibBuilder.loadTexts:
    tmnxOamCpePingV4v0Group.setStatus("current")

tmnxOamMRInfoV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 22)
)
tmnxOamMRInfoV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespCapabilities"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespMinorVersion"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespMajorVersion"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespNumInterfaces"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfMetric"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfThreshold"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfFlags"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfNbrCount"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfNbrAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfNbrAddr"))
)
if mibBuilder.loadTexts:
    tmnxOamMRInfoV4v0Group.setStatus("current")

tmnxOamIcmpPingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 23)
)
tmnxOamIcmpPingGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlRapid"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlTtl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlDSField"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlPattern"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlNhAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlNhAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlEgrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlBypassRouting"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamIcmpPingCtlDoNotFragment"))
)
if mibBuilder.loadTexts:
    tmnxOamIcmpPingGroup.setStatus("current")

tmnxOamPingObsoleteV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 24)
)
tmnxOamPingObsoleteV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTargetIpAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcIpAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacPingHistorySrcIpAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpIpPrefix"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpIpPrefixLen"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnPingCtlSourceIpAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlSourceIpAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlDestIpAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamCpePingCtlSourceIpAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMRInfoRespIfNbrAddress"))
)
if mibBuilder.loadTexts:
    tmnxOamPingObsoleteV4v0Group.setStatus("current")

tmnxOamLspPingV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 27)
)
tmnxOamLspPingV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlVRtrID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLspName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlReturnLsp"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlTtl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlPathName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefixType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefix"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlLdpPrefixLen"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlPathDestType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlPathDest"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlNhIntfName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlNhAddressType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspPingCtlNhAddress"))
)
if mibBuilder.loadTexts:
    tmnxOamLspPingV5v0Group.setStatus("current")

tmnxOamVccvPingV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 28)
)
tmnxOamVccvPingV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlSdpIdVcId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlReplyMode"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlPwId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlTtl"))
)
if mibBuilder.loadTexts:
    tmnxOamVccvPingV5v0Group.setStatus("current")

tmnxOamAncpTestV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 29)
)
tmnxOamAncpTestV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestTarget"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestTargetId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestcount"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamAncpTestTimeout"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamAncpHistoryAncpString"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamAncpHistoryAccNodeResult"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamAncpHistoryAccNodeCode"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamAncpHistoryAccNodeRspStr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVccvPingCtlTtl"))
)
if mibBuilder.loadTexts:
    tmnxOamAncpTestV5v0Group.setStatus("current")

tmnxOamMfibPingV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 31)
)
tmnxOamMfibPingV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlReplyControl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlTtl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlSrcAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlSrcAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlDestAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlDestAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespSvcId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMfibPingCtlDestMacAddr"))
)
if mibBuilder.loadTexts:
    tmnxOamMfibPingV6v0Group.setStatus("current")

tmnxOamPingGeneralV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 32)
)
tmnxOamPingGeneralV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingMaxConcurrentTests"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRowStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlStorageType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDescr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTestMode"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlOrigSdpId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRespSdpId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlFcName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlProfile"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuStartSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuEndSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMtuStepSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlServiceId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLocalSdp"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRemoteSdp"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTimeOut"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlProbeCount"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlInterval"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlMaxRows"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapGeneration"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapProbeFailureFilter"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTrapTestFailureFilter"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSAA"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlRuns"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlFailures"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLastRunResult"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlLastChanged"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlVRtrID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSrcAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlSrcAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDnsName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastRespHeader"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsTtSumOfSquares"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinInTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxInTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageInTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInTtSumOfSqrs"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOutJitter"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsInJitter"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRtJitter"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeTimeouts"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeFailures"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryResponse"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryOneWayTime"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryTime"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryReturnCode"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistAddressType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryVersion"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistSapId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryCpeMacAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespSvcId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySequence"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryIfIndex"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDataLen"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespPlane"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryReqHdr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryRespHdr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDnsAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryDnsAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistorySrcAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingHistoryInOneWayTime"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlDNSRecord"))
)
if mibBuilder.loadTexts:
    tmnxOamPingGeneralV6v0Group.setStatus("current")

tmnxOamMacTrV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 10)
)
tmnxOamMacTrV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrCtlTargetMacAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrCtlSourceMacAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrCtlSendControl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrCtlReplyControl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapRouterID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapLabel"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapProtocol"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapVCType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapVCID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapDirection"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapSdpId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMacTrL2MapSapName"))
)
if mibBuilder.loadTexts:
    tmnxOamMacTrV3v0Group.setStatus("current")

tmnxOamTrObsoleteV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 11)
)
tmnxOamTrObsoleteV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestAttempts"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTestSuccesses"))
)
if mibBuilder.loadTexts:
    tmnxOamTrObsoleteV3v0Group.setStatus("current")

tmnxOamTrGeneralV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 12)
)
tmnxOamTrGeneralV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrMaxConcurrentRequests"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlRowStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlStorageType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDescr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestMode"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlFcName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlProfile"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlServiceId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDataSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTimeOut"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlProbesPerHop"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlMaxTtl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlInitialTtl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDSField"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlMaxFailures"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlInterval"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlMaxRows"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTrapGeneration"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlCreateHopsEntries"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSAA"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlRuns"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlFailures"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastRunResult"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastChanged"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlVRtrID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTgtAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTgtAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSrcAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSrcAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlWaitMilliSec"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsOperStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsCurHopCount"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsCurProbeCount"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsLastGoodPath"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTgtAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTgtAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryResponse"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryOneWayTime"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryLastRC"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryTime"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryResponsePlane"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddressType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistorySapId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryVersion"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryRouterID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIfIndex"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryDataLen"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistorySize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryInOneWayTime"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddress"))
)
if mibBuilder.loadTexts:
    tmnxOamTrGeneralV4v0Group.setStatus("obsolete")

tmnxOamTrHopsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 13)
)
tmnxOamTrHopsV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsMinRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsMaxRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsAverageRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsRttSumOfSquares"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsMinTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsMaxTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsAverageTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsTtSumOfSquares"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsSentProbes"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsProbeResponses"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsLastGoodProbe"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsMinInTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsMaxInTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsAverageInTt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsInTtSumOfSqrs"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsOutJitter"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsInJitter"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsRtJitter"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsProbeTimeouts"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsProbeFailures"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsTgtAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsTgtAddress"))
)
if mibBuilder.loadTexts:
    tmnxOamTrHopsV4v0Group.setStatus("current")

tmnxOamLspTrV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 14)
)
tmnxOamLspTrV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlVRtrID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLspName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlPathName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpPrefixType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpPrefix"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpPrefixLen"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDSIPv4Addr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDSIfAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapMTU"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDSIndex"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrDSLabelLabel"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrDSLabelProtocol"))
)
if mibBuilder.loadTexts:
    tmnxOamLspTrV4v0Group.setStatus("obsolete")

tmnxOamVprnTrV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 15)
)
tmnxOamVprnTrV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrCtlReplyControl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrCtlSrcAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrCtlSrcAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRouterID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteVprnLabel"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteMetrics"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteLastUp"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteOwner"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRtePref"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteDist"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapNumNextHops"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapNumRteTargets"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapDestAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapDestAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapDestMaskLen"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopRtrID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopTunnelID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopTunnelType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopIfIndex"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrRouteTarget"))
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrV4v0Group.setStatus("obsolete")

tmnxOamMcastTrV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 16)
)
tmnxOamMcastTrV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlVRtrID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlHops"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrQueryId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlSrcAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlSrcAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlDestAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlDestAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlRespAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlRespAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlGrpAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlGrpAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespQueryArrivalTime"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespInPktCount"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespOutPktCount"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespSGPktCount"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespRtgProtocol"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespFwdTtl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespMBZBit"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespSrcBit"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespSrcMask"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespFwdCode"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespInIfAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespInIfAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespOutIfAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespOutIfAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespPhRtrAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespPhRtrAddress"))
)
if mibBuilder.loadTexts:
    tmnxOamMcastTrV4v0Group.setStatus("current")

tmnxOamTrObsoleteV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 17)
)
tmnxOamTrObsoleteV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTargetIpAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsIpTgtAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIpAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrHopsIpTgtAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpIpPrefix"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpIpPrefixLen"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrCtlSourceIpAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteDestAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteDestMask"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlSrcIpAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlDestIpAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlRespIpAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrCtlGrpIpAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespPrevHopRtrAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespInIfAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamMcastTrRespOutIfAddr"))
)
if mibBuilder.loadTexts:
    tmnxOamTrObsoleteV4v0Group.setStatus("current")

tmnxOamLspTrV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 19)
)
tmnxOamLspTrV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlVRtrID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLspName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlPathName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpPrefixType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpPrefix"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlLdpPrefixLen"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlPathDestType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlPathDest"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlNhIntfName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlNhAddressType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrCtlNhAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDSIPv4Addr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDSIfAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapMTU"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrDSLabelLabel"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrDSLabelProtocol"))
)
if mibBuilder.loadTexts:
    tmnxOamLspTrV5v0Group.setStatus("current")

tmnxOamTrObsoleteV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 20)
)
tmnxOamTrObsoleteV5v0Group.setObjects(
    ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLspTrMapDSIndex")
)
if mibBuilder.loadTexts:
    tmnxOamTrObsoleteV5v0Group.setStatus("current")

tmnxOamTrGeneralV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 21)
)
tmnxOamTrGeneralV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrMaxConcurrentRequests"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlRowStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlStorageType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDescr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestMode"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlFcName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlProfile"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlServiceId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDataSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTimeOut"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlProbesPerHop"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlMaxTtl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlInitialTtl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlDSField"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlMaxFailures"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlInterval"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlMaxRows"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTrapGeneration"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlCreateHopsEntries"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSAA"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlRuns"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlFailures"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastRunResult"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastChanged"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlVRtrID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTgtAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTgtAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSrcAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlSrcAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlWaitMilliSec"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsOperStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsCurHopCount"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsCurProbeCount"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsLastGoodPath"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTgtAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsTgtAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryResponse"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryOneWayTime"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryLastRC"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryTime"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryResponsePlane"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddressType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistorySapId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryVersion"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryRouterID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryIfIndex"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryDataLen"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistorySize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryInOneWayTime"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrProbeHistoryAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDiscoveryState"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDisStatusBits"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDisPaths"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecFailedHops"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecLastDisEnd"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecFailedProbes"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecProbeState"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathRemAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathRemoteAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathEgrNhAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathEgrNhAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathDisTtl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathLastDisTime"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathLastRc"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceCtlLdpPrefixType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceCtlLdpPrefix"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceCtlLdpPrefixLen"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceCtlMaxPath"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceResultsDisPaths"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceResultsFailedHops"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceResultsDisState"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceResultsDisStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceUpStreamHopIndex"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDstAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDstAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopEgrNhAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopEgrNhAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDisTtl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopLastRc"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDiscoveryState"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceHopDiscoveryTime"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoRowStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoLastChanged"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoStorageType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoAdminState"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoFcName"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoProfile"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoDiscIntvl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoMaxPath"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoTrMaxTtl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoTrTimeOut"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoTrMaxFailures"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy1"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy2"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy3"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy4"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPolicy5"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoProbeIntvl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPrTimeOut"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoPrMaxFailures"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoDiscoveryState"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoTotalFecs"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoDisFecs"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoLastDisStart"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoLastDisEnd"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoLastDisDur"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathProbeState"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtracePathProbeTmOutCnt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceMaxConRequests"))
)
if mibBuilder.loadTexts:
    tmnxOamTrGeneralV5v0Group.setStatus("current")

tmnxOamVccvTrV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 23)
)
tmnxOamVccvTrV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrCtlSdpIdVcId"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrCtlReplyMode"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextPwID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextPwType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextSenderAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextSenderAddr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextRemoteAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVccvTrNextRemoteAddr"))
)
if mibBuilder.loadTexts:
    tmnxOamVccvTrV6v0Group.setStatus("current")

tmnxOamVprnTrObsoleteV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 24)
)
tmnxOamVprnTrObsoleteV6v0Group.setObjects(
    ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopRtrID")
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrObsoleteV6v0Group.setStatus("current")

tmnxOamVprnTrV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 25)
)
tmnxOamVprnTrV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrCtlReplyControl"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrCtlSrcAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrCtlSrcAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRouterID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteVprnLabel"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteMetrics"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteLastUp"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteOwner"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRtePref"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapRteDist"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapNumNextHops"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapNumRteTargets"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapDestAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapDestAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrL3MapDestMaskLen"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopTunnelID"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopTunnelType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopIfIndex"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrNextHopAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamVprnTrRouteTarget"))
)
if mibBuilder.loadTexts:
    tmnxOamVprnTrV6v0Group.setStatus("current")

tmnxOamSaaGeneralV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 2, 1)
)
tmnxOamSaaGeneralV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlRowStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlStorageType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlLastChanged"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlTestMode"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlDescr"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlRuns"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlFailures"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlLastRunResult"))
)
if mibBuilder.loadTexts:
    tmnxOamSaaGeneralV3v0Group.setStatus("current")

tmnxOamSaaThresholdV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 2, 2)
)
tmnxOamSaaThresholdV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTRowStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTLastChanged"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTThreshold"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTValue"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTLastSent"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTTestMode"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTTestRunIndex"))
)
if mibBuilder.loadTexts:
    tmnxOamSaaThresholdV3v0Group.setStatus("current")


# Notification objects

tmnxOamPingProbeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0, 1)
)
tmnxOamPingProbeFailed.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTargetIpAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    tmnxOamPingProbeFailed.setStatus(
        "obsolete"
    )

tmnxOamPingTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0, 2)
)
tmnxOamPingTestFailed.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTargetIpAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    tmnxOamPingTestFailed.setStatus(
        "obsolete"
    )

tmnxOamPingTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0, 3)
)
tmnxOamPingTestCompleted.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTargetIpAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    tmnxOamPingTestCompleted.setStatus(
        "obsolete"
    )

tmnxOamPingProbeFailedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0, 4)
)
tmnxOamPingProbeFailedV2.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    tmnxOamPingProbeFailedV2.setStatus(
        "current"
    )

tmnxOamPingTestFailedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0, 5)
)
tmnxOamPingTestFailedV2.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    tmnxOamPingTestFailedV2.setStatus(
        "current"
    )

tmnxOamPingTestCompletedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0, 6)
)
tmnxOamPingTestCompletedV2.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddrType"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingCtlTgtAddress"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsOperStatus"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMinRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMaxRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsAverageRtt"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsRttSumOfSquares"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsMtuResponseSize"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSvcPing"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsProbeResponses"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsSentProbes"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingResultsLastGoodProbe"))
)
if mibBuilder.loadTexts:
    tmnxOamPingTestCompletedV2.setStatus(
        "current"
    )

tmnxAncpLoopbackTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 1, 0, 7)
)
tmnxAncpLoopbackTestCompleted.setObjects(
    ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamAncpHistoryAncpString")
)
if mibBuilder.loadTexts:
    tmnxAncpLoopbackTestCompleted.setStatus(
        "current"
    )

tmnxOamTrPathChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 2, 0, 1)
)
tmnxOamTrPathChange.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestMode"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastRunResult"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxOamTrPathChange.setStatus(
        "current"
    )

tmnxOamTrTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 2, 0, 2)
)
tmnxOamTrTestFailed.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestMode"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastRunResult"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxOamTrTestFailed.setStatus(
        "current"
    )

tmnxOamTrTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 2, 0, 3)
)
tmnxOamTrTestCompleted.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlTestMode"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrCtlLastRunResult"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrResultsOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxOamTrTestCompleted.setStatus(
        "current"
    )

tmnxOamLdpTtraceAutoDiscState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 2, 0, 4)
)
tmnxOamLdpTtraceAutoDiscState.setObjects(
    ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceAutoDiscoveryState")
)
if mibBuilder.loadTexts:
    tmnxOamLdpTtraceAutoDiscState.setStatus(
        "current"
    )

tmnxOamLdpTtraceFecProbeState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 2, 0, 5)
)
tmnxOamLdpTtraceFecProbeState.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecProbeState"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDisPaths"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecFailedProbes"))
)
if mibBuilder.loadTexts:
    tmnxOamLdpTtraceFecProbeState.setStatus(
        "current"
    )

tmnxOamLdpTtraceFecDisStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 2, 0, 6)
)
tmnxOamLdpTtraceFecDisStatus.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDisStatusBits"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLTtraceFecDisPaths"))
)
if mibBuilder.loadTexts:
    tmnxOamLdpTtraceFecDisStatus.setStatus(
        "current"
    )

tmnxOamSaaThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 11, 3, 0, 1)
)
tmnxOamSaaThreshold.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTThreshold"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTValue"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlTestMode"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaCtlLastRunResult"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaTTestRunIndex"))
)
if mibBuilder.loadTexts:
    tmnxOamSaaThreshold.setStatus(
        "current"
    )


# Notifications groups

tmnxOamPingNotificationV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 25)
)
tmnxOamPingNotificationV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingProbeFailedV2"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingTestFailedV2"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingTestCompletedV2"))
)
if mibBuilder.loadTexts:
    tmnxOamPingNotificationV4v0Group.setStatus(
        "obsolete"
    )

tmnxOamPingNotificationObsoleteV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 26)
)
tmnxOamPingNotificationObsoleteV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingProbeFailed"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingTestFailed"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingTestCompleted"))
)
if mibBuilder.loadTexts:
    tmnxOamPingNotificationObsoleteV4v0Group.setStatus(
        "current"
    )

tmnxOamPingNotificationV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 2, 30)
)
tmnxOamPingNotificationV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingProbeFailedV2"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingTestFailedV2"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamPingTestCompletedV2"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxAncpLoopbackTestCompleted"))
)
if mibBuilder.loadTexts:
    tmnxOamPingNotificationV5v0Group.setStatus(
        "current"
    )

tmnxOamTrNotificationV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 18)
)
tmnxOamTrNotificationV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrPathChange"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrTestFailed"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrTestCompleted"))
)
if mibBuilder.loadTexts:
    tmnxOamTrNotificationV4v0Group.setStatus(
        "obsolete"
    )

tmnxOamTrNotificationV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 2, 22)
)
tmnxOamTrNotificationV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrPathChange"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrTestFailed"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamTrTestCompleted"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLdpTtraceAutoDiscState"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLdpTtraceFecProbeState"),
        ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamLdpTtraceFecDisStatus"))
)
if mibBuilder.loadTexts:
    tmnxOamTrNotificationV5v0Group.setStatus(
        "current"
    )

tmnxOamSaaNotificationV3v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 2, 3)
)
tmnxOamSaaNotificationV3v0Group.setObjects(
    ("ALCATEL-IND1-TIMETRA-OAM-TEST-MIB", "tmnxOamSaaThreshold")
)
if mibBuilder.loadTexts:
    tmnxOamSaaNotificationV3v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxOamPing7450V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxOamPing7450V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing7750V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxOamPing7750V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing7450V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxOamPing7450V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing7750V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxOamPing7750V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPing7450V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxOamPing7450V6v0Compliance.setStatus(
        "current"
    )

tmnxOamPing7750V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 1, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxOamPing7750V6v0Compliance.setStatus(
        "current"
    )

tmnxOamTr7450V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxOamTr7450V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamTr7750V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxOamTr7750V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamTr7450V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxOamTr7450V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamTr7750V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxOamTr7750V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamTr7450V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxOamTr7450V6v0Compliance.setStatus(
        "current"
    )

tmnxOamTr77x0V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 2, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxOamTr77x0V6v0Compliance.setStatus(
        "current"
    )

tmnxOamSaaV3v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 11, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxOamSaaV3v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-TIMETRA-OAM-TEST-MIB",
    **{"TmnxOamTestMode": TmnxOamTestMode,
       "TmnxOamPingRtnCode": TmnxOamPingRtnCode,
       "TmnxOamAddressType": TmnxOamAddressType,
       "TmnxOamResponseStatus": TmnxOamResponseStatus,
       "TmnxOamSignalProtocol": TmnxOamSignalProtocol,
       "TmnxOamTestResponsePlane": TmnxOamTestResponsePlane,
       "TmnxOamSaaThreshold": TmnxOamSaaThreshold,
       "TmnxOamVcType": TmnxOamVcType,
       "TmnxOamLTtraceDisStatusBits": TmnxOamLTtraceDisStatusBits,
       "timetraOamTestMIBModule": timetraOamTestMIBModule,
       "tmnxOamTestConformance": tmnxOamTestConformance,
       "tmnxOamPingConformance": tmnxOamPingConformance,
       "tmnxOamPingCompliances": tmnxOamPingCompliances,
       "tmnxOamPing7450V4v0Compliance": tmnxOamPing7450V4v0Compliance,
       "tmnxOamPing7750V4v0Compliance": tmnxOamPing7750V4v0Compliance,
       "tmnxOamPing7450V5v0Compliance": tmnxOamPing7450V5v0Compliance,
       "tmnxOamPing7750V5v0Compliance": tmnxOamPing7750V5v0Compliance,
       "tmnxOamPing7450V6v0Compliance": tmnxOamPing7450V6v0Compliance,
       "tmnxOamPing7750V6v0Compliance": tmnxOamPing7750V6v0Compliance,
       "tmnxOamPingGroups": tmnxOamPingGroups,
       "tmnxOamMacPingL2MapGroup": tmnxOamMacPingL2MapGroup,
       "tmnxOamAtmPingR2r1Group": tmnxOamAtmPingR2r1Group,
       "tmnxOamMacPingV4v0Group": tmnxOamMacPingV4v0Group,
       "tmnxOamVccvPingGroup": tmnxOamVccvPingGroup,
       "tmnxOamPingGeneralV4v0Group": tmnxOamPingGeneralV4v0Group,
       "tmnxOamLspPingV4v0Group": tmnxOamLspPingV4v0Group,
       "tmnxOamVprnPingV4v0Group": tmnxOamVprnPingV4v0Group,
       "tmnxOamMfibPingV4v0Group": tmnxOamMfibPingV4v0Group,
       "tmnxOamCpePingV4v0Group": tmnxOamCpePingV4v0Group,
       "tmnxOamMRInfoV4v0Group": tmnxOamMRInfoV4v0Group,
       "tmnxOamIcmpPingGroup": tmnxOamIcmpPingGroup,
       "tmnxOamPingObsoleteV4v0Group": tmnxOamPingObsoleteV4v0Group,
       "tmnxOamPingNotificationV4v0Group": tmnxOamPingNotificationV4v0Group,
       "tmnxOamPingNotificationObsoleteV4v0Group": tmnxOamPingNotificationObsoleteV4v0Group,
       "tmnxOamLspPingV5v0Group": tmnxOamLspPingV5v0Group,
       "tmnxOamVccvPingV5v0Group": tmnxOamVccvPingV5v0Group,
       "tmnxOamAncpTestV5v0Group": tmnxOamAncpTestV5v0Group,
       "tmnxOamPingNotificationV5v0Group": tmnxOamPingNotificationV5v0Group,
       "tmnxOamMfibPingV6v0Group": tmnxOamMfibPingV6v0Group,
       "tmnxOamPingGeneralV6v0Group": tmnxOamPingGeneralV6v0Group,
       "tmnxOamTraceRouteConformance": tmnxOamTraceRouteConformance,
       "tmnxOamTrCompliances": tmnxOamTrCompliances,
       "tmnxOamTr7450V4v0Compliance": tmnxOamTr7450V4v0Compliance,
       "tmnxOamTr7750V4v0Compliance": tmnxOamTr7750V4v0Compliance,
       "tmnxOamTr7450V5v0Compliance": tmnxOamTr7450V5v0Compliance,
       "tmnxOamTr7750V5v0Compliance": tmnxOamTr7750V5v0Compliance,
       "tmnxOamTr7450V6v0Compliance": tmnxOamTr7450V6v0Compliance,
       "tmnxOamTr77x0V6v0Compliance": tmnxOamTr77x0V6v0Compliance,
       "tmnxOamTrGroups": tmnxOamTrGroups,
       "tmnxOamMacTrV3v0Group": tmnxOamMacTrV3v0Group,
       "tmnxOamTrObsoleteV3v0Group": tmnxOamTrObsoleteV3v0Group,
       "tmnxOamTrGeneralV4v0Group": tmnxOamTrGeneralV4v0Group,
       "tmnxOamTrHopsV4v0Group": tmnxOamTrHopsV4v0Group,
       "tmnxOamLspTrV4v0Group": tmnxOamLspTrV4v0Group,
       "tmnxOamVprnTrV4v0Group": tmnxOamVprnTrV4v0Group,
       "tmnxOamMcastTrV4v0Group": tmnxOamMcastTrV4v0Group,
       "tmnxOamTrObsoleteV4v0Group": tmnxOamTrObsoleteV4v0Group,
       "tmnxOamTrNotificationV4v0Group": tmnxOamTrNotificationV4v0Group,
       "tmnxOamLspTrV5v0Group": tmnxOamLspTrV5v0Group,
       "tmnxOamTrObsoleteV5v0Group": tmnxOamTrObsoleteV5v0Group,
       "tmnxOamTrGeneralV5v0Group": tmnxOamTrGeneralV5v0Group,
       "tmnxOamTrNotificationV5v0Group": tmnxOamTrNotificationV5v0Group,
       "tmnxOamVccvTrV6v0Group": tmnxOamVccvTrV6v0Group,
       "tmnxOamVprnTrObsoleteV6v0Group": tmnxOamVprnTrObsoleteV6v0Group,
       "tmnxOamVprnTrV6v0Group": tmnxOamVprnTrV6v0Group,
       "tmnxOamSaaConformance": tmnxOamSaaConformance,
       "tmnxOamSaaCompliances": tmnxOamSaaCompliances,
       "tmnxOamSaaV3v0Compliance": tmnxOamSaaV3v0Compliance,
       "tmnxOamSaaGroups": tmnxOamSaaGroups,
       "tmnxOamSaaGeneralV3v0Group": tmnxOamSaaGeneralV3v0Group,
       "tmnxOamSaaThresholdV3v0Group": tmnxOamSaaThresholdV3v0Group,
       "tmnxOamSaaNotificationV3v0Group": tmnxOamSaaNotificationV3v0Group,
       "tmnxOamTestObjs": tmnxOamTestObjs,
       "tmnxOamPingObjs": tmnxOamPingObjs,
       "tmnxOamPingNotificationObjects": tmnxOamPingNotificationObjects,
       "tmnxOamPingMaxConcurrentTests": tmnxOamPingMaxConcurrentTests,
       "tmnxOamPingCtlTable": tmnxOamPingCtlTable,
       "tmnxOamPingCtlEntry": tmnxOamPingCtlEntry,
       "tmnxOamPingCtlOwnerIndex": tmnxOamPingCtlOwnerIndex,
       "tmnxOamPingCtlTestIndex": tmnxOamPingCtlTestIndex,
       "tmnxOamPingCtlRowStatus": tmnxOamPingCtlRowStatus,
       "tmnxOamPingCtlStorageType": tmnxOamPingCtlStorageType,
       "tmnxOamPingCtlDescr": tmnxOamPingCtlDescr,
       "tmnxOamPingCtlTestMode": tmnxOamPingCtlTestMode,
       "tmnxOamPingCtlAdminStatus": tmnxOamPingCtlAdminStatus,
       "tmnxOamPingCtlOrigSdpId": tmnxOamPingCtlOrigSdpId,
       "tmnxOamPingCtlRespSdpId": tmnxOamPingCtlRespSdpId,
       "tmnxOamPingCtlFcName": tmnxOamPingCtlFcName,
       "tmnxOamPingCtlProfile": tmnxOamPingCtlProfile,
       "tmnxOamPingCtlMtuStartSize": tmnxOamPingCtlMtuStartSize,
       "tmnxOamPingCtlMtuEndSize": tmnxOamPingCtlMtuEndSize,
       "tmnxOamPingCtlMtuStepSize": tmnxOamPingCtlMtuStepSize,
       "tmnxOamPingCtlTargetIpAddress": tmnxOamPingCtlTargetIpAddress,
       "tmnxOamPingCtlServiceId": tmnxOamPingCtlServiceId,
       "tmnxOamPingCtlLocalSdp": tmnxOamPingCtlLocalSdp,
       "tmnxOamPingCtlRemoteSdp": tmnxOamPingCtlRemoteSdp,
       "tmnxOamPingCtlSize": tmnxOamPingCtlSize,
       "tmnxOamPingCtlTimeOut": tmnxOamPingCtlTimeOut,
       "tmnxOamPingCtlProbeCount": tmnxOamPingCtlProbeCount,
       "tmnxOamPingCtlInterval": tmnxOamPingCtlInterval,
       "tmnxOamPingCtlMaxRows": tmnxOamPingCtlMaxRows,
       "tmnxOamPingCtlTrapGeneration": tmnxOamPingCtlTrapGeneration,
       "tmnxOamPingCtlTrapProbeFailureFilter": tmnxOamPingCtlTrapProbeFailureFilter,
       "tmnxOamPingCtlTrapTestFailureFilter": tmnxOamPingCtlTrapTestFailureFilter,
       "tmnxOamPingCtlSAA": tmnxOamPingCtlSAA,
       "tmnxOamPingCtlRuns": tmnxOamPingCtlRuns,
       "tmnxOamPingCtlFailures": tmnxOamPingCtlFailures,
       "tmnxOamPingCtlLastRunResult": tmnxOamPingCtlLastRunResult,
       "tmnxOamPingCtlLastChanged": tmnxOamPingCtlLastChanged,
       "tmnxOamPingCtlVRtrID": tmnxOamPingCtlVRtrID,
       "tmnxOamPingCtlTgtAddrType": tmnxOamPingCtlTgtAddrType,
       "tmnxOamPingCtlTgtAddress": tmnxOamPingCtlTgtAddress,
       "tmnxOamPingCtlSrcAddrType": tmnxOamPingCtlSrcAddrType,
       "tmnxOamPingCtlSrcAddress": tmnxOamPingCtlSrcAddress,
       "tmnxOamPingCtlDnsName": tmnxOamPingCtlDnsName,
       "tmnxOamPingCtlDNSRecord": tmnxOamPingCtlDNSRecord,
       "tmnxOamPingResultsTable": tmnxOamPingResultsTable,
       "tmnxOamPingResultsEntry": tmnxOamPingResultsEntry,
       "tmnxOamPingResultsOperStatus": tmnxOamPingResultsOperStatus,
       "tmnxOamPingResultsMinRtt": tmnxOamPingResultsMinRtt,
       "tmnxOamPingResultsMaxRtt": tmnxOamPingResultsMaxRtt,
       "tmnxOamPingResultsAverageRtt": tmnxOamPingResultsAverageRtt,
       "tmnxOamPingResultsRttSumOfSquares": tmnxOamPingResultsRttSumOfSquares,
       "tmnxOamPingResultsMtuResponseSize": tmnxOamPingResultsMtuResponseSize,
       "tmnxOamPingResultsSvcPing": tmnxOamPingResultsSvcPing,
       "tmnxOamPingResultsProbeResponses": tmnxOamPingResultsProbeResponses,
       "tmnxOamPingResultsSentProbes": tmnxOamPingResultsSentProbes,
       "tmnxOamPingResultsLastGoodProbe": tmnxOamPingResultsLastGoodProbe,
       "tmnxOamPingResultsLastRespHeader": tmnxOamPingResultsLastRespHeader,
       "tmnxOamPingResultsMinTt": tmnxOamPingResultsMinTt,
       "tmnxOamPingResultsMaxTt": tmnxOamPingResultsMaxTt,
       "tmnxOamPingResultsAverageTt": tmnxOamPingResultsAverageTt,
       "tmnxOamPingResultsTtSumOfSquares": tmnxOamPingResultsTtSumOfSquares,
       "tmnxOamPingResultsMinInTt": tmnxOamPingResultsMinInTt,
       "tmnxOamPingResultsMaxInTt": tmnxOamPingResultsMaxInTt,
       "tmnxOamPingResultsAverageInTt": tmnxOamPingResultsAverageInTt,
       "tmnxOamPingResultsInTtSumOfSqrs": tmnxOamPingResultsInTtSumOfSqrs,
       "tmnxOamPingResultsOutJitter": tmnxOamPingResultsOutJitter,
       "tmnxOamPingResultsInJitter": tmnxOamPingResultsInJitter,
       "tmnxOamPingResultsRtJitter": tmnxOamPingResultsRtJitter,
       "tmnxOamPingResultsProbeTimeouts": tmnxOamPingResultsProbeTimeouts,
       "tmnxOamPingResultsProbeFailures": tmnxOamPingResultsProbeFailures,
       "tmnxOamPingResultsTestRunIndex": tmnxOamPingResultsTestRunIndex,
       "tmnxOamPingHistoryTable": tmnxOamPingHistoryTable,
       "tmnxOamPingHistoryEntry": tmnxOamPingHistoryEntry,
       "tmnxOamPingHistoryIndex": tmnxOamPingHistoryIndex,
       "tmnxOamPingHistoryResponse": tmnxOamPingHistoryResponse,
       "tmnxOamPingHistoryOneWayTime": tmnxOamPingHistoryOneWayTime,
       "tmnxOamPingHistorySize": tmnxOamPingHistorySize,
       "tmnxOamPingHistoryStatus": tmnxOamPingHistoryStatus,
       "tmnxOamPingHistoryTime": tmnxOamPingHistoryTime,
       "tmnxOamPingHistoryReturnCode": tmnxOamPingHistoryReturnCode,
       "tmnxOamPingHistorySrcIpAddress": tmnxOamPingHistorySrcIpAddress,
       "tmnxOamPingHistAddressType": tmnxOamPingHistAddressType,
       "tmnxOamPingHistSapId": tmnxOamPingHistSapId,
       "tmnxOamPingHistoryVersion": tmnxOamPingHistoryVersion,
       "tmnxOamPingHistoryCpeMacAddr": tmnxOamPingHistoryCpeMacAddr,
       "tmnxOamPingHistoryRespSvcId": tmnxOamPingHistoryRespSvcId,
       "tmnxOamPingHistorySequence": tmnxOamPingHistorySequence,
       "tmnxOamPingHistoryIfIndex": tmnxOamPingHistoryIfIndex,
       "tmnxOamPingHistoryDataLen": tmnxOamPingHistoryDataLen,
       "tmnxOamPingHistoryRespPlane": tmnxOamPingHistoryRespPlane,
       "tmnxOamPingHistoryReqHdr": tmnxOamPingHistoryReqHdr,
       "tmnxOamPingHistoryRespHdr": tmnxOamPingHistoryRespHdr,
       "tmnxOamPingHistoryDnsAddrType": tmnxOamPingHistoryDnsAddrType,
       "tmnxOamPingHistoryDnsAddress": tmnxOamPingHistoryDnsAddress,
       "tmnxOamPingHistorySrcAddrType": tmnxOamPingHistorySrcAddrType,
       "tmnxOamPingHistorySrcAddress": tmnxOamPingHistorySrcAddress,
       "tmnxOamPingHistoryInOneWayTime": tmnxOamPingHistoryInOneWayTime,
       "tmnxOamMacPingCtlTable": tmnxOamMacPingCtlTable,
       "tmnxOamMacPingCtlEntry": tmnxOamMacPingCtlEntry,
       "tmnxOamMacPingCtlTargetMacAddr": tmnxOamMacPingCtlTargetMacAddr,
       "tmnxOamMacPingCtlSourceMacAddr": tmnxOamMacPingCtlSourceMacAddr,
       "tmnxOamMacPingCtlSendControl": tmnxOamMacPingCtlSendControl,
       "tmnxOamMacPingCtlReplyControl": tmnxOamMacPingCtlReplyControl,
       "tmnxOamMacPingCtlTtl": tmnxOamMacPingCtlTtl,
       "tmnxOamMacPingCtlRegister": tmnxOamMacPingCtlRegister,
       "tmnxOamMacPingCtlFlood": tmnxOamMacPingCtlFlood,
       "tmnxOamMacPingCtlForce": tmnxOamMacPingCtlForce,
       "tmnxOamMacPingCtlAge": tmnxOamMacPingCtlAge,
       "tmnxOamMacPingCtlSapPortId": tmnxOamMacPingCtlSapPortId,
       "tmnxOamMacPingCtlSapEncapValue": tmnxOamMacPingCtlSapEncapValue,
       "tmnxOamMacPingCtlFibEntryName": tmnxOamMacPingCtlFibEntryName,
       "tmnxOamMacPingHistoryTable": tmnxOamMacPingHistoryTable,
       "tmnxOamMacPingHistoryEntry": tmnxOamMacPingHistoryEntry,
       "tmnxOamMacPingHistoryIndex": tmnxOamMacPingHistoryIndex,
       "tmnxOamMacPingReplyIndex": tmnxOamMacPingReplyIndex,
       "tmnxOamMacPingHistoryResponse": tmnxOamMacPingHistoryResponse,
       "tmnxOamMacPingHistoryOneWayTime": tmnxOamMacPingHistoryOneWayTime,
       "tmnxOamMacPingHistoryStatus": tmnxOamMacPingHistoryStatus,
       "tmnxOamMacPingHistoryTime": tmnxOamMacPingHistoryTime,
       "tmnxOamMacPingHistoryReturnCode": tmnxOamMacPingHistoryReturnCode,
       "tmnxOamMacPingHistorySrcIpAddress": tmnxOamMacPingHistorySrcIpAddress,
       "tmnxOamMacPingHistoryAddressType": tmnxOamMacPingHistoryAddressType,
       "tmnxOamMacPingHistorySapId": tmnxOamMacPingHistorySapId,
       "tmnxOamMacPingHistorySdpId": tmnxOamMacPingHistorySdpId,
       "tmnxOamMacPingHistoryAdminStatus": tmnxOamMacPingHistoryAdminStatus,
       "tmnxOamMacPingHistoryOperStatus": tmnxOamMacPingHistoryOperStatus,
       "tmnxOamMacPingHistoryResponsePlane": tmnxOamMacPingHistoryResponsePlane,
       "tmnxOamMacPingHistorySize": tmnxOamMacPingHistorySize,
       "tmnxOamMacPingHistoryInOneWayTime": tmnxOamMacPingHistoryInOneWayTime,
       "tmnxOamMacPingHistorySrcAddrType": tmnxOamMacPingHistorySrcAddrType,
       "tmnxOamMacPingHistorySrcAddress": tmnxOamMacPingHistorySrcAddress,
       "tmnxOamMacPingL2MapTable": tmnxOamMacPingL2MapTable,
       "tmnxOamMacPingL2MapEntry": tmnxOamMacPingL2MapEntry,
       "tmnxOamMacPingL2MapIndex": tmnxOamMacPingL2MapIndex,
       "tmnxOamMacPingL2MapRouterID": tmnxOamMacPingL2MapRouterID,
       "tmnxOamMacPingL2MapLabel": tmnxOamMacPingL2MapLabel,
       "tmnxOamMacPingL2MapProtocol": tmnxOamMacPingL2MapProtocol,
       "tmnxOamMacPingL2MapVCType": tmnxOamMacPingL2MapVCType,
       "tmnxOamMacPingL2MapVCID": tmnxOamMacPingL2MapVCID,
       "tmnxOamMacPingL2MapDirection": tmnxOamMacPingL2MapDirection,
       "tmnxOamLspPingCtlTable": tmnxOamLspPingCtlTable,
       "tmnxOamLspPingCtlEntry": tmnxOamLspPingCtlEntry,
       "tmnxOamLspPingCtlVRtrID": tmnxOamLspPingCtlVRtrID,
       "tmnxOamLspPingCtlLspName": tmnxOamLspPingCtlLspName,
       "tmnxOamLspPingCtlReturnLsp": tmnxOamLspPingCtlReturnLsp,
       "tmnxOamLspPingCtlTtl": tmnxOamLspPingCtlTtl,
       "tmnxOamLspPingCtlPathName": tmnxOamLspPingCtlPathName,
       "tmnxOamLspPingCtlLdpIpPrefix": tmnxOamLspPingCtlLdpIpPrefix,
       "tmnxOamLspPingCtlLdpIpPrefixLen": tmnxOamLspPingCtlLdpIpPrefixLen,
       "tmnxOamLspPingCtlLdpPrefixType": tmnxOamLspPingCtlLdpPrefixType,
       "tmnxOamLspPingCtlLdpPrefix": tmnxOamLspPingCtlLdpPrefix,
       "tmnxOamLspPingCtlLdpPrefixLen": tmnxOamLspPingCtlLdpPrefixLen,
       "tmnxOamLspPingCtlPathDestType": tmnxOamLspPingCtlPathDestType,
       "tmnxOamLspPingCtlPathDest": tmnxOamLspPingCtlPathDest,
       "tmnxOamLspPingCtlNhIntfName": tmnxOamLspPingCtlNhIntfName,
       "tmnxOamLspPingCtlNhAddressType": tmnxOamLspPingCtlNhAddressType,
       "tmnxOamLspPingCtlNhAddress": tmnxOamLspPingCtlNhAddress,
       "tmnxOamVprnPingCtlTable": tmnxOamVprnPingCtlTable,
       "tmnxOamVprnPingCtlEntry": tmnxOamVprnPingCtlEntry,
       "tmnxOamVprnPingCtlSourceIpAddr": tmnxOamVprnPingCtlSourceIpAddr,
       "tmnxOamVprnPingCtlReplyControl": tmnxOamVprnPingCtlReplyControl,
       "tmnxOamVprnPingCtlTtl": tmnxOamVprnPingCtlTtl,
       "tmnxOamVprnPingCtlSrcAddrType": tmnxOamVprnPingCtlSrcAddrType,
       "tmnxOamVprnPingCtlSrcAddress": tmnxOamVprnPingCtlSrcAddress,
       "tmnxOamAtmPingCtlTable": tmnxOamAtmPingCtlTable,
       "tmnxOamAtmPingCtlEntry": tmnxOamAtmPingCtlEntry,
       "tmnxOamAtmPingCtlPortId": tmnxOamAtmPingCtlPortId,
       "tmnxOamAtmPingCtlVpi": tmnxOamAtmPingCtlVpi,
       "tmnxOamAtmPingCtlVci": tmnxOamAtmPingCtlVci,
       "tmnxOamAtmPingCtlLpbkLocation": tmnxOamAtmPingCtlLpbkLocation,
       "tmnxOamAtmPingCtlSegment": tmnxOamAtmPingCtlSegment,
       "tmnxOamMfibPingCtlTable": tmnxOamMfibPingCtlTable,
       "tmnxOamMfibPingCtlEntry": tmnxOamMfibPingCtlEntry,
       "tmnxOamMfibPingCtlSourceIpAddr": tmnxOamMfibPingCtlSourceIpAddr,
       "tmnxOamMfibPingCtlDestIpAddr": tmnxOamMfibPingCtlDestIpAddr,
       "tmnxOamMfibPingCtlReplyControl": tmnxOamMfibPingCtlReplyControl,
       "tmnxOamMfibPingCtlTtl": tmnxOamMfibPingCtlTtl,
       "tmnxOamMfibPingCtlSrcAddrType": tmnxOamMfibPingCtlSrcAddrType,
       "tmnxOamMfibPingCtlSrcAddress": tmnxOamMfibPingCtlSrcAddress,
       "tmnxOamMfibPingCtlDestAddrType": tmnxOamMfibPingCtlDestAddrType,
       "tmnxOamMfibPingCtlDestAddress": tmnxOamMfibPingCtlDestAddress,
       "tmnxOamMfibPingCtlDestMacAddr": tmnxOamMfibPingCtlDestMacAddr,
       "tmnxOamCpePingCtlTable": tmnxOamCpePingCtlTable,
       "tmnxOamCpePingCtlEntry": tmnxOamCpePingCtlEntry,
       "tmnxOamCpePingCtlSourceIpAddr": tmnxOamCpePingCtlSourceIpAddr,
       "tmnxOamCpePingCtlSendControl": tmnxOamCpePingCtlSendControl,
       "tmnxOamCpePingCtlReplyControl": tmnxOamCpePingCtlReplyControl,
       "tmnxOamCpePingCtlTtl": tmnxOamCpePingCtlTtl,
       "tmnxOamCpePingCtlSrceMacAddr": tmnxOamCpePingCtlSrceMacAddr,
       "tmnxOamCpePingCtlSrcAddrType": tmnxOamCpePingCtlSrcAddrType,
       "tmnxOamCpePingCtlSrcAddress": tmnxOamCpePingCtlSrcAddress,
       "tmnxOamMRInfoRespTable": tmnxOamMRInfoRespTable,
       "tmnxOamMRInfoRespEntry": tmnxOamMRInfoRespEntry,
       "tmnxOamMRInfoRespCapabilities": tmnxOamMRInfoRespCapabilities,
       "tmnxOamMRInfoRespMinorVersion": tmnxOamMRInfoRespMinorVersion,
       "tmnxOamMRInfoRespMajorVersion": tmnxOamMRInfoRespMajorVersion,
       "tmnxOamMRInfoRespNumInterfaces": tmnxOamMRInfoRespNumInterfaces,
       "tmnxOamMRInfoRespIfTable": tmnxOamMRInfoRespIfTable,
       "tmnxOamMRInfoRespIfEntry": tmnxOamMRInfoRespIfEntry,
       "tmnxOamMRInfoRespIfIndex": tmnxOamMRInfoRespIfIndex,
       "tmnxOamMRInfoRespIfAddress": tmnxOamMRInfoRespIfAddress,
       "tmnxOamMRInfoRespIfMetric": tmnxOamMRInfoRespIfMetric,
       "tmnxOamMRInfoRespIfThreshold": tmnxOamMRInfoRespIfThreshold,
       "tmnxOamMRInfoRespIfFlags": tmnxOamMRInfoRespIfFlags,
       "tmnxOamMRInfoRespIfNbrCount": tmnxOamMRInfoRespIfNbrCount,
       "tmnxOamMRInfoRespIfAddrType": tmnxOamMRInfoRespIfAddrType,
       "tmnxOamMRInfoRespIfAddr": tmnxOamMRInfoRespIfAddr,
       "tmnxOamMRInfoRespIfNbrTable": tmnxOamMRInfoRespIfNbrTable,
       "tmnxOamMRInfoRespIfNbrEntry": tmnxOamMRInfoRespIfNbrEntry,
       "tmnxOamMRInfoRespIfNbrIndex": tmnxOamMRInfoRespIfNbrIndex,
       "tmnxOamMRInfoRespIfNbrAddress": tmnxOamMRInfoRespIfNbrAddress,
       "tmnxOamMRInfoRespIfNbrAddrType": tmnxOamMRInfoRespIfNbrAddrType,
       "tmnxOamMRInfoRespIfNbrAddr": tmnxOamMRInfoRespIfNbrAddr,
       "tmnxOamVccvPingCtlTable": tmnxOamVccvPingCtlTable,
       "tmnxOamVccvPingCtlEntry": tmnxOamVccvPingCtlEntry,
       "tmnxOamVccvPingCtlSdpIdVcId": tmnxOamVccvPingCtlSdpIdVcId,
       "tmnxOamVccvPingCtlReplyMode": tmnxOamVccvPingCtlReplyMode,
       "tmnxOamVccvPingCtlPwId": tmnxOamVccvPingCtlPwId,
       "tmnxOamVccvPingCtlTtl": tmnxOamVccvPingCtlTtl,
       "tmnxOamIcmpPingCtlTable": tmnxOamIcmpPingCtlTable,
       "tmnxOamIcmpPingCtlEntry": tmnxOamIcmpPingCtlEntry,
       "tmnxOamIcmpPingCtlRapid": tmnxOamIcmpPingCtlRapid,
       "tmnxOamIcmpPingCtlTtl": tmnxOamIcmpPingCtlTtl,
       "tmnxOamIcmpPingCtlDSField": tmnxOamIcmpPingCtlDSField,
       "tmnxOamIcmpPingCtlPattern": tmnxOamIcmpPingCtlPattern,
       "tmnxOamIcmpPingCtlNhAddrType": tmnxOamIcmpPingCtlNhAddrType,
       "tmnxOamIcmpPingCtlNhAddress": tmnxOamIcmpPingCtlNhAddress,
       "tmnxOamIcmpPingCtlEgrIfIndex": tmnxOamIcmpPingCtlEgrIfIndex,
       "tmnxOamIcmpPingCtlBypassRouting": tmnxOamIcmpPingCtlBypassRouting,
       "tmnxOamIcmpPingCtlDoNotFragment": tmnxOamIcmpPingCtlDoNotFragment,
       "tmnxOamAncpTestCtlTable": tmnxOamAncpTestCtlTable,
       "tmnxOamAncpTestCtlEntry": tmnxOamAncpTestCtlEntry,
       "tmnxOamAncpTestTarget": tmnxOamAncpTestTarget,
       "tmnxOamAncpTestTargetId": tmnxOamAncpTestTargetId,
       "tmnxOamAncpTestcount": tmnxOamAncpTestcount,
       "tmnxOamAncpTestTimeout": tmnxOamAncpTestTimeout,
       "tmnxOamAncpTestHistoryTable": tmnxOamAncpTestHistoryTable,
       "tmnxOamAncpTestHistoryEntry": tmnxOamAncpTestHistoryEntry,
       "tmnxOamAncpHistoryIndex": tmnxOamAncpHistoryIndex,
       "tmnxOamAncpHistoryAncpString": tmnxOamAncpHistoryAncpString,
       "tmnxOamAncpHistoryAccNodeCode": tmnxOamAncpHistoryAccNodeCode,
       "tmnxOamAncpHistoryAccNodeResult": tmnxOamAncpHistoryAccNodeResult,
       "tmnxOamAncpHistoryAccNodeRspStr": tmnxOamAncpHistoryAccNodeRspStr,
       "tmnxOamTraceRouteObjs": tmnxOamTraceRouteObjs,
       "tmnxOamTraceRouteNotifyObjects": tmnxOamTraceRouteNotifyObjects,
       "tmnxOamTrMaxConcurrentRequests": tmnxOamTrMaxConcurrentRequests,
       "tmnxOamTrCtlTable": tmnxOamTrCtlTable,
       "tmnxOamTrCtlEntry": tmnxOamTrCtlEntry,
       "tmnxOamTrCtlOwnerIndex": tmnxOamTrCtlOwnerIndex,
       "tmnxOamTrCtlTestIndex": tmnxOamTrCtlTestIndex,
       "tmnxOamTrCtlRowStatus": tmnxOamTrCtlRowStatus,
       "tmnxOamTrCtlStorageType": tmnxOamTrCtlStorageType,
       "tmnxOamTrCtlDescr": tmnxOamTrCtlDescr,
       "tmnxOamTrCtlTestMode": tmnxOamTrCtlTestMode,
       "tmnxOamTrCtlAdminStatus": tmnxOamTrCtlAdminStatus,
       "tmnxOamTrCtlFcName": tmnxOamTrCtlFcName,
       "tmnxOamTrCtlProfile": tmnxOamTrCtlProfile,
       "tmnxOamTrCtlTargetIpAddress": tmnxOamTrCtlTargetIpAddress,
       "tmnxOamTrCtlServiceId": tmnxOamTrCtlServiceId,
       "tmnxOamTrCtlDataSize": tmnxOamTrCtlDataSize,
       "tmnxOamTrCtlTimeOut": tmnxOamTrCtlTimeOut,
       "tmnxOamTrCtlProbesPerHop": tmnxOamTrCtlProbesPerHop,
       "tmnxOamTrCtlMaxTtl": tmnxOamTrCtlMaxTtl,
       "tmnxOamTrCtlInitialTtl": tmnxOamTrCtlInitialTtl,
       "tmnxOamTrCtlDSField": tmnxOamTrCtlDSField,
       "tmnxOamTrCtlMaxFailures": tmnxOamTrCtlMaxFailures,
       "tmnxOamTrCtlInterval": tmnxOamTrCtlInterval,
       "tmnxOamTrCtlMaxRows": tmnxOamTrCtlMaxRows,
       "tmnxOamTrCtlTrapGeneration": tmnxOamTrCtlTrapGeneration,
       "tmnxOamTrCtlCreateHopsEntries": tmnxOamTrCtlCreateHopsEntries,
       "tmnxOamTrCtlSAA": tmnxOamTrCtlSAA,
       "tmnxOamTrCtlRuns": tmnxOamTrCtlRuns,
       "tmnxOamTrCtlFailures": tmnxOamTrCtlFailures,
       "tmnxOamTrCtlLastRunResult": tmnxOamTrCtlLastRunResult,
       "tmnxOamTrCtlLastChanged": tmnxOamTrCtlLastChanged,
       "tmnxOamTrCtlVRtrID": tmnxOamTrCtlVRtrID,
       "tmnxOamTrCtlTgtAddrType": tmnxOamTrCtlTgtAddrType,
       "tmnxOamTrCtlTgtAddress": tmnxOamTrCtlTgtAddress,
       "tmnxOamTrCtlSrcAddrType": tmnxOamTrCtlSrcAddrType,
       "tmnxOamTrCtlSrcAddress": tmnxOamTrCtlSrcAddress,
       "tmnxOamTrCtlWaitMilliSec": tmnxOamTrCtlWaitMilliSec,
       "tmnxOamTrResultsTable": tmnxOamTrResultsTable,
       "tmnxOamTrResultsEntry": tmnxOamTrResultsEntry,
       "tmnxOamTrResultsOperStatus": tmnxOamTrResultsOperStatus,
       "tmnxOamTrResultsCurHopCount": tmnxOamTrResultsCurHopCount,
       "tmnxOamTrResultsCurProbeCount": tmnxOamTrResultsCurProbeCount,
       "tmnxOamTrResultsIpTgtAddr": tmnxOamTrResultsIpTgtAddr,
       "tmnxOamTrResultsTestAttempts": tmnxOamTrResultsTestAttempts,
       "tmnxOamTrResultsTestSuccesses": tmnxOamTrResultsTestSuccesses,
       "tmnxOamTrResultsLastGoodPath": tmnxOamTrResultsLastGoodPath,
       "tmnxOamTrResultsTestRunIndex": tmnxOamTrResultsTestRunIndex,
       "tmnxOamTrResultsTgtAddrType": tmnxOamTrResultsTgtAddrType,
       "tmnxOamTrResultsTgtAddress": tmnxOamTrResultsTgtAddress,
       "tmnxOamTrProbeHistoryTable": tmnxOamTrProbeHistoryTable,
       "tmnxOamTrProbeHistoryEntry": tmnxOamTrProbeHistoryEntry,
       "tmnxOamTrProbeHistoryIndex": tmnxOamTrProbeHistoryIndex,
       "tmnxOamTrProbeHistoryHopIndex": tmnxOamTrProbeHistoryHopIndex,
       "tmnxOamTrProbeHistoryProbeIndex": tmnxOamTrProbeHistoryProbeIndex,
       "tmnxOamTrProbeHistoryIpAddr": tmnxOamTrProbeHistoryIpAddr,
       "tmnxOamTrProbeHistoryResponse": tmnxOamTrProbeHistoryResponse,
       "tmnxOamTrProbeHistoryOneWayTime": tmnxOamTrProbeHistoryOneWayTime,
       "tmnxOamTrProbeHistoryStatus": tmnxOamTrProbeHistoryStatus,
       "tmnxOamTrProbeHistoryLastRC": tmnxOamTrProbeHistoryLastRC,
       "tmnxOamTrProbeHistoryTime": tmnxOamTrProbeHistoryTime,
       "tmnxOamTrProbeHistoryResponsePlane": tmnxOamTrProbeHistoryResponsePlane,
       "tmnxOamTrProbeHistoryAddressType": tmnxOamTrProbeHistoryAddressType,
       "tmnxOamTrProbeHistorySapId": tmnxOamTrProbeHistorySapId,
       "tmnxOamTrProbeHistoryVersion": tmnxOamTrProbeHistoryVersion,
       "tmnxOamTrProbeHistoryRouterID": tmnxOamTrProbeHistoryRouterID,
       "tmnxOamTrProbeHistoryIfIndex": tmnxOamTrProbeHistoryIfIndex,
       "tmnxOamTrProbeHistoryDataLen": tmnxOamTrProbeHistoryDataLen,
       "tmnxOamTrProbeHistorySize": tmnxOamTrProbeHistorySize,
       "tmnxOamTrProbeHistoryInOneWayTime": tmnxOamTrProbeHistoryInOneWayTime,
       "tmnxOamTrProbeHistoryAddrType": tmnxOamTrProbeHistoryAddrType,
       "tmnxOamTrProbeHistoryAddress": tmnxOamTrProbeHistoryAddress,
       "tmnxOamTrHopsTable": tmnxOamTrHopsTable,
       "tmnxOamTrHopsEntry": tmnxOamTrHopsEntry,
       "tmnxOamTrHopsHopIndex": tmnxOamTrHopsHopIndex,
       "tmnxOamTrHopsIpTgtAddress": tmnxOamTrHopsIpTgtAddress,
       "tmnxOamTrHopsMinRtt": tmnxOamTrHopsMinRtt,
       "tmnxOamTrHopsMaxRtt": tmnxOamTrHopsMaxRtt,
       "tmnxOamTrHopsAverageRtt": tmnxOamTrHopsAverageRtt,
       "tmnxOamTrHopsRttSumOfSquares": tmnxOamTrHopsRttSumOfSquares,
       "tmnxOamTrHopsMinTt": tmnxOamTrHopsMinTt,
       "tmnxOamTrHopsMaxTt": tmnxOamTrHopsMaxTt,
       "tmnxOamTrHopsAverageTt": tmnxOamTrHopsAverageTt,
       "tmnxOamTrHopsTtSumOfSquares": tmnxOamTrHopsTtSumOfSquares,
       "tmnxOamTrHopsSentProbes": tmnxOamTrHopsSentProbes,
       "tmnxOamTrHopsProbeResponses": tmnxOamTrHopsProbeResponses,
       "tmnxOamTrHopsLastGoodProbe": tmnxOamTrHopsLastGoodProbe,
       "tmnxOamTrHopsMinInTt": tmnxOamTrHopsMinInTt,
       "tmnxOamTrHopsMaxInTt": tmnxOamTrHopsMaxInTt,
       "tmnxOamTrHopsAverageInTt": tmnxOamTrHopsAverageInTt,
       "tmnxOamTrHopsInTtSumOfSqrs": tmnxOamTrHopsInTtSumOfSqrs,
       "tmnxOamTrHopsOutJitter": tmnxOamTrHopsOutJitter,
       "tmnxOamTrHopsInJitter": tmnxOamTrHopsInJitter,
       "tmnxOamTrHopsRtJitter": tmnxOamTrHopsRtJitter,
       "tmnxOamTrHopsProbeTimeouts": tmnxOamTrHopsProbeTimeouts,
       "tmnxOamTrHopsProbeFailures": tmnxOamTrHopsProbeFailures,
       "tmnxOamTrHopsTgtAddrType": tmnxOamTrHopsTgtAddrType,
       "tmnxOamTrHopsTgtAddress": tmnxOamTrHopsTgtAddress,
       "tmnxOamMacTrCtlTable": tmnxOamMacTrCtlTable,
       "tmnxOamMacTrCtlEntry": tmnxOamMacTrCtlEntry,
       "tmnxOamMacTrCtlTargetMacAddr": tmnxOamMacTrCtlTargetMacAddr,
       "tmnxOamMacTrCtlSourceMacAddr": tmnxOamMacTrCtlSourceMacAddr,
       "tmnxOamMacTrCtlSendControl": tmnxOamMacTrCtlSendControl,
       "tmnxOamMacTrCtlReplyControl": tmnxOamMacTrCtlReplyControl,
       "tmnxOamMacTrL2MapTable": tmnxOamMacTrL2MapTable,
       "tmnxOamMacTrL2MapEntry": tmnxOamMacTrL2MapEntry,
       "tmnxOamMacTrL2MapIndex": tmnxOamMacTrL2MapIndex,
       "tmnxOamMacTrL2MapRouterID": tmnxOamMacTrL2MapRouterID,
       "tmnxOamMacTrL2MapLabel": tmnxOamMacTrL2MapLabel,
       "tmnxOamMacTrL2MapProtocol": tmnxOamMacTrL2MapProtocol,
       "tmnxOamMacTrL2MapVCType": tmnxOamMacTrL2MapVCType,
       "tmnxOamMacTrL2MapVCID": tmnxOamMacTrL2MapVCID,
       "tmnxOamMacTrL2MapDirection": tmnxOamMacTrL2MapDirection,
       "tmnxOamMacTrL2MapSdpId": tmnxOamMacTrL2MapSdpId,
       "tmnxOamMacTrL2MapSapName": tmnxOamMacTrL2MapSapName,
       "tmnxOamLspTrCtlTable": tmnxOamLspTrCtlTable,
       "tmnxOamLspTrCtlEntry": tmnxOamLspTrCtlEntry,
       "tmnxOamLspTrCtlVRtrID": tmnxOamLspTrCtlVRtrID,
       "tmnxOamLspTrCtlLspName": tmnxOamLspTrCtlLspName,
       "tmnxOamLspTrCtlPathName": tmnxOamLspTrCtlPathName,
       "tmnxOamLspTrCtlLdpIpPrefix": tmnxOamLspTrCtlLdpIpPrefix,
       "tmnxOamLspTrCtlLdpIpPrefixLen": tmnxOamLspTrCtlLdpIpPrefixLen,
       "tmnxOamLspTrCtlLdpPrefixType": tmnxOamLspTrCtlLdpPrefixType,
       "tmnxOamLspTrCtlLdpPrefix": tmnxOamLspTrCtlLdpPrefix,
       "tmnxOamLspTrCtlLdpPrefixLen": tmnxOamLspTrCtlLdpPrefixLen,
       "tmnxOamLspTrCtlPathDestType": tmnxOamLspTrCtlPathDestType,
       "tmnxOamLspTrCtlPathDest": tmnxOamLspTrCtlPathDest,
       "tmnxOamLspTrCtlNhIntfName": tmnxOamLspTrCtlNhIntfName,
       "tmnxOamLspTrCtlNhAddressType": tmnxOamLspTrCtlNhAddressType,
       "tmnxOamLspTrCtlNhAddress": tmnxOamLspTrCtlNhAddress,
       "tmnxOamLspTrMapTable": tmnxOamLspTrMapTable,
       "tmnxOamLspTrMapEntry": tmnxOamLspTrMapEntry,
       "tmnxOamLspTrMapIndex": tmnxOamLspTrMapIndex,
       "tmnxOamLspTrMapDSIPv4Addr": tmnxOamLspTrMapDSIPv4Addr,
       "tmnxOamLspTrMapAddrType": tmnxOamLspTrMapAddrType,
       "tmnxOamLspTrMapDSIfAddr": tmnxOamLspTrMapDSIfAddr,
       "tmnxOamLspTrMapMTU": tmnxOamLspTrMapMTU,
       "tmnxOamLspTrMapDSIndex": tmnxOamLspTrMapDSIndex,
       "tmnxOamVprnTrCtlTable": tmnxOamVprnTrCtlTable,
       "tmnxOamVprnTrCtlEntry": tmnxOamVprnTrCtlEntry,
       "tmnxOamVprnTrCtlSourceIpAddr": tmnxOamVprnTrCtlSourceIpAddr,
       "tmnxOamVprnTrCtlReplyControl": tmnxOamVprnTrCtlReplyControl,
       "tmnxOamVprnTrCtlSrcAddrType": tmnxOamVprnTrCtlSrcAddrType,
       "tmnxOamVprnTrCtlSrcAddress": tmnxOamVprnTrCtlSrcAddress,
       "tmnxOamVprnTrL3MapTable": tmnxOamVprnTrL3MapTable,
       "tmnxOamVprnTrL3MapEntry": tmnxOamVprnTrL3MapEntry,
       "tmnxOamVprnTrL3MapReporter": tmnxOamVprnTrL3MapReporter,
       "tmnxOamVprnTrL3MapRouterID": tmnxOamVprnTrL3MapRouterID,
       "tmnxOamVprnTrL3MapRteDestAddr": tmnxOamVprnTrL3MapRteDestAddr,
       "tmnxOamVprnTrL3MapRteDestMask": tmnxOamVprnTrL3MapRteDestMask,
       "tmnxOamVprnTrL3MapRteVprnLabel": tmnxOamVprnTrL3MapRteVprnLabel,
       "tmnxOamVprnTrL3MapRteMetrics": tmnxOamVprnTrL3MapRteMetrics,
       "tmnxOamVprnTrL3MapRteLastUp": tmnxOamVprnTrL3MapRteLastUp,
       "tmnxOamVprnTrL3MapRteOwner": tmnxOamVprnTrL3MapRteOwner,
       "tmnxOamVprnTrL3MapRtePref": tmnxOamVprnTrL3MapRtePref,
       "tmnxOamVprnTrL3MapRteDist": tmnxOamVprnTrL3MapRteDist,
       "tmnxOamVprnTrL3MapNumNextHops": tmnxOamVprnTrL3MapNumNextHops,
       "tmnxOamVprnTrL3MapNumRteTargets": tmnxOamVprnTrL3MapNumRteTargets,
       "tmnxOamVprnTrL3MapDestAddrType": tmnxOamVprnTrL3MapDestAddrType,
       "tmnxOamVprnTrL3MapDestAddress": tmnxOamVprnTrL3MapDestAddress,
       "tmnxOamVprnTrL3MapDestMaskLen": tmnxOamVprnTrL3MapDestMaskLen,
       "tmnxOamVprnTrNextHopTable": tmnxOamVprnTrNextHopTable,
       "tmnxOamVprnTrNextHopEntry": tmnxOamVprnTrNextHopEntry,
       "tmnxOamVprnTrNextHopIndex": tmnxOamVprnTrNextHopIndex,
       "tmnxOamVprnTrNextHopRtrID": tmnxOamVprnTrNextHopRtrID,
       "tmnxOamVprnTrNextHopType": tmnxOamVprnTrNextHopType,
       "tmnxOamVprnTrNextHopTunnelID": tmnxOamVprnTrNextHopTunnelID,
       "tmnxOamVprnTrNextHopTunnelType": tmnxOamVprnTrNextHopTunnelType,
       "tmnxOamVprnTrNextHopIfIndex": tmnxOamVprnTrNextHopIfIndex,
       "tmnxOamVprnTrNextHopAddrType": tmnxOamVprnTrNextHopAddrType,
       "tmnxOamVprnTrNextHopAddress": tmnxOamVprnTrNextHopAddress,
       "tmnxOamVprnTrRTTable": tmnxOamVprnTrRTTable,
       "tmnxOamVprnTrRTEntry": tmnxOamVprnTrRTEntry,
       "tmnxOamVprnTrRTIndex": tmnxOamVprnTrRTIndex,
       "tmnxOamVprnTrRouteTarget": tmnxOamVprnTrRouteTarget,
       "tmnxOamLspTrDSLabelTable": tmnxOamLspTrDSLabelTable,
       "tmnxOamLspTrDSLabelEntry": tmnxOamLspTrDSLabelEntry,
       "tmnxOamLspTrDSLabelIndex": tmnxOamLspTrDSLabelIndex,
       "tmnxOamLspTrDSLabelLabel": tmnxOamLspTrDSLabelLabel,
       "tmnxOamLspTrDSLabelProtocol": tmnxOamLspTrDSLabelProtocol,
       "tmnxOamMcastTrCtlTable": tmnxOamMcastTrCtlTable,
       "tmnxOamMcastTrCtlEntry": tmnxOamMcastTrCtlEntry,
       "tmnxOamMcastTrCtlVRtrID": tmnxOamMcastTrCtlVRtrID,
       "tmnxOamMcastTrCtlSrcIpAddr": tmnxOamMcastTrCtlSrcIpAddr,
       "tmnxOamMcastTrCtlDestIpAddr": tmnxOamMcastTrCtlDestIpAddr,
       "tmnxOamMcastTrCtlRespIpAddr": tmnxOamMcastTrCtlRespIpAddr,
       "tmnxOamMcastTrCtlGrpIpAddr": tmnxOamMcastTrCtlGrpIpAddr,
       "tmnxOamMcastTrCtlHops": tmnxOamMcastTrCtlHops,
       "tmnxOamMcastTrQueryId": tmnxOamMcastTrQueryId,
       "tmnxOamMcastTrCtlSrcAddrType": tmnxOamMcastTrCtlSrcAddrType,
       "tmnxOamMcastTrCtlSrcAddress": tmnxOamMcastTrCtlSrcAddress,
       "tmnxOamMcastTrCtlDestAddrType": tmnxOamMcastTrCtlDestAddrType,
       "tmnxOamMcastTrCtlDestAddress": tmnxOamMcastTrCtlDestAddress,
       "tmnxOamMcastTrCtlRespAddrType": tmnxOamMcastTrCtlRespAddrType,
       "tmnxOamMcastTrCtlRespAddress": tmnxOamMcastTrCtlRespAddress,
       "tmnxOamMcastTrCtlGrpAddrType": tmnxOamMcastTrCtlGrpAddrType,
       "tmnxOamMcastTrCtlGrpAddress": tmnxOamMcastTrCtlGrpAddress,
       "tmnxOamMcastTrRespTable": tmnxOamMcastTrRespTable,
       "tmnxOamMcastTrRespEntry": tmnxOamMcastTrRespEntry,
       "tmnxOamMcastTrRespQueryArrivalTime": tmnxOamMcastTrRespQueryArrivalTime,
       "tmnxOamMcastTrRespInIfAddr": tmnxOamMcastTrRespInIfAddr,
       "tmnxOamMcastTrRespOutIfAddr": tmnxOamMcastTrRespOutIfAddr,
       "tmnxOamMcastTrRespPrevHopRtrAddr": tmnxOamMcastTrRespPrevHopRtrAddr,
       "tmnxOamMcastTrRespInPktCount": tmnxOamMcastTrRespInPktCount,
       "tmnxOamMcastTrRespOutPktCount": tmnxOamMcastTrRespOutPktCount,
       "tmnxOamMcastTrRespSGPktCount": tmnxOamMcastTrRespSGPktCount,
       "tmnxOamMcastTrRespRtgProtocol": tmnxOamMcastTrRespRtgProtocol,
       "tmnxOamMcastTrRespFwdTtl": tmnxOamMcastTrRespFwdTtl,
       "tmnxOamMcastTrRespMBZBit": tmnxOamMcastTrRespMBZBit,
       "tmnxOamMcastTrRespSrcBit": tmnxOamMcastTrRespSrcBit,
       "tmnxOamMcastTrRespSrcMask": tmnxOamMcastTrRespSrcMask,
       "tmnxOamMcastTrRespFwdCode": tmnxOamMcastTrRespFwdCode,
       "tmnxOamMcastTrRespInIfAddrType": tmnxOamMcastTrRespInIfAddrType,
       "tmnxOamMcastTrRespInIfAddress": tmnxOamMcastTrRespInIfAddress,
       "tmnxOamMcastTrRespOutIfAddrType": tmnxOamMcastTrRespOutIfAddrType,
       "tmnxOamMcastTrRespOutIfAddress": tmnxOamMcastTrRespOutIfAddress,
       "tmnxOamMcastTrRespPhRtrAddrType": tmnxOamMcastTrRespPhRtrAddrType,
       "tmnxOamMcastTrRespPhRtrAddress": tmnxOamMcastTrRespPhRtrAddress,
       "tmnxOamLTtraceCtlTable": tmnxOamLTtraceCtlTable,
       "tmnxOamLTtraceCtlEntry": tmnxOamLTtraceCtlEntry,
       "tmnxOamLTtraceCtlLdpPrefixType": tmnxOamLTtraceCtlLdpPrefixType,
       "tmnxOamLTtraceCtlLdpPrefix": tmnxOamLTtraceCtlLdpPrefix,
       "tmnxOamLTtraceCtlLdpPrefixLen": tmnxOamLTtraceCtlLdpPrefixLen,
       "tmnxOamLTtraceCtlMaxPath": tmnxOamLTtraceCtlMaxPath,
       "tmnxOamLTtraceMaxConRequests": tmnxOamLTtraceMaxConRequests,
       "tmnxOamLTtraceResultsTable": tmnxOamLTtraceResultsTable,
       "tmnxOamLTtraceResultsEntry": tmnxOamLTtraceResultsEntry,
       "tmnxOamLTtraceResultsDisPaths": tmnxOamLTtraceResultsDisPaths,
       "tmnxOamLTtraceResultsFailedHops": tmnxOamLTtraceResultsFailedHops,
       "tmnxOamLTtraceResultsDisState": tmnxOamLTtraceResultsDisState,
       "tmnxOamLTtraceResultsDisStatus": tmnxOamLTtraceResultsDisStatus,
       "tmnxOamLTtraceHopInfoTable": tmnxOamLTtraceHopInfoTable,
       "tmnxOamLTtraceHopInfoEntry": tmnxOamLTtraceHopInfoEntry,
       "tmnxOamLTtraceHopIndex": tmnxOamLTtraceHopIndex,
       "tmnxOamLTtraceUpStreamHopIndex": tmnxOamLTtraceUpStreamHopIndex,
       "tmnxOamLTtraceHopAddrType": tmnxOamLTtraceHopAddrType,
       "tmnxOamLTtraceHopAddr": tmnxOamLTtraceHopAddr,
       "tmnxOamLTtraceHopDstAddrType": tmnxOamLTtraceHopDstAddrType,
       "tmnxOamLTtraceHopDstAddr": tmnxOamLTtraceHopDstAddr,
       "tmnxOamLTtraceHopEgrNhAddrType": tmnxOamLTtraceHopEgrNhAddrType,
       "tmnxOamLTtraceHopEgrNhAddr": tmnxOamLTtraceHopEgrNhAddr,
       "tmnxOamLTtraceHopDisTtl": tmnxOamLTtraceHopDisTtl,
       "tmnxOamLTtraceHopLastRc": tmnxOamLTtraceHopLastRc,
       "tmnxOamLTtraceHopDiscoveryState": tmnxOamLTtraceHopDiscoveryState,
       "tmnxOamLTtraceHopDiscoveryTime": tmnxOamLTtraceHopDiscoveryTime,
       "tmnxOamLTtraceAutoConfigTable": tmnxOamLTtraceAutoConfigTable,
       "tmnxOamLTtraceAutoConfigEntry": tmnxOamLTtraceAutoConfigEntry,
       "tmnxOamLTtraceAutoRowStatus": tmnxOamLTtraceAutoRowStatus,
       "tmnxOamLTtraceAutoLastChanged": tmnxOamLTtraceAutoLastChanged,
       "tmnxOamLTtraceAutoStorageType": tmnxOamLTtraceAutoStorageType,
       "tmnxOamLTtraceAutoAdminState": tmnxOamLTtraceAutoAdminState,
       "tmnxOamLTtraceAutoFcName": tmnxOamLTtraceAutoFcName,
       "tmnxOamLTtraceAutoProfile": tmnxOamLTtraceAutoProfile,
       "tmnxOamLTtraceAutoDiscIntvl": tmnxOamLTtraceAutoDiscIntvl,
       "tmnxOamLTtraceAutoMaxPath": tmnxOamLTtraceAutoMaxPath,
       "tmnxOamLTtraceAutoTrMaxTtl": tmnxOamLTtraceAutoTrMaxTtl,
       "tmnxOamLTtraceAutoTrTimeOut": tmnxOamLTtraceAutoTrTimeOut,
       "tmnxOamLTtraceAutoTrMaxFailures": tmnxOamLTtraceAutoTrMaxFailures,
       "tmnxOamLTtraceAutoPolicy1": tmnxOamLTtraceAutoPolicy1,
       "tmnxOamLTtraceAutoPolicy2": tmnxOamLTtraceAutoPolicy2,
       "tmnxOamLTtraceAutoPolicy3": tmnxOamLTtraceAutoPolicy3,
       "tmnxOamLTtraceAutoPolicy4": tmnxOamLTtraceAutoPolicy4,
       "tmnxOamLTtraceAutoPolicy5": tmnxOamLTtraceAutoPolicy5,
       "tmnxOamLTtraceAutoProbeIntvl": tmnxOamLTtraceAutoProbeIntvl,
       "tmnxOamLTtraceAutoPrTimeOut": tmnxOamLTtraceAutoPrTimeOut,
       "tmnxOamLTtraceAutoPrMaxFailures": tmnxOamLTtraceAutoPrMaxFailures,
       "tmnxOamLTtraceAutoStatusTable": tmnxOamLTtraceAutoStatusTable,
       "tmnxOamLTtraceAutoStatusEntry": tmnxOamLTtraceAutoStatusEntry,
       "tmnxOamLTtraceAutoDiscoveryState": tmnxOamLTtraceAutoDiscoveryState,
       "tmnxOamLTtraceAutoTotalFecs": tmnxOamLTtraceAutoTotalFecs,
       "tmnxOamLTtraceAutoDisFecs": tmnxOamLTtraceAutoDisFecs,
       "tmnxOamLTtraceAutoLastDisStart": tmnxOamLTtraceAutoLastDisStart,
       "tmnxOamLTtraceAutoLastDisEnd": tmnxOamLTtraceAutoLastDisEnd,
       "tmnxOamLTtraceAutoLastDisDur": tmnxOamLTtraceAutoLastDisDur,
       "tmnxOamLTtraceFecInfoTable": tmnxOamLTtraceFecInfoTable,
       "tmnxOamLTtraceFecInfoEntry": tmnxOamLTtraceFecInfoEntry,
       "tmnxOamLTtraceFecPrefixType": tmnxOamLTtraceFecPrefixType,
       "tmnxOamLTtraceFecPrefix": tmnxOamLTtraceFecPrefix,
       "tmnxOamLTtraceFecPrefLen": tmnxOamLTtraceFecPrefLen,
       "tmnxOamLTtraceFecDiscoveryState": tmnxOamLTtraceFecDiscoveryState,
       "tmnxOamLTtraceFecDisStatusBits": tmnxOamLTtraceFecDisStatusBits,
       "tmnxOamLTtraceFecDisPaths": tmnxOamLTtraceFecDisPaths,
       "tmnxOamLTtraceFecFailedHops": tmnxOamLTtraceFecFailedHops,
       "tmnxOamLTtraceFecLastDisEnd": tmnxOamLTtraceFecLastDisEnd,
       "tmnxOamLTtraceFecFailedProbes": tmnxOamLTtraceFecFailedProbes,
       "tmnxOamLTtraceFecProbeState": tmnxOamLTtraceFecProbeState,
       "tmnxOamLTtracePathInfoTable": tmnxOamLTtracePathInfoTable,
       "tmnxOamLTtracePathInfoEntry": tmnxOamLTtracePathInfoEntry,
       "tmnxOamLTtracePathDstAddrType": tmnxOamLTtracePathDstAddrType,
       "tmnxOamLTtracePathDstAddr": tmnxOamLTtracePathDstAddr,
       "tmnxOamLTtracePathRemAddrType": tmnxOamLTtracePathRemAddrType,
       "tmnxOamLTtracePathRemoteAddr": tmnxOamLTtracePathRemoteAddr,
       "tmnxOamLTtracePathEgrNhAddrType": tmnxOamLTtracePathEgrNhAddrType,
       "tmnxOamLTtracePathEgrNhAddr": tmnxOamLTtracePathEgrNhAddr,
       "tmnxOamLTtracePathDisTtl": tmnxOamLTtracePathDisTtl,
       "tmnxOamLTtracePathLastDisTime": tmnxOamLTtracePathLastDisTime,
       "tmnxOamLTtracePathLastRc": tmnxOamLTtracePathLastRc,
       "tmnxOamLTtracePathProbeState": tmnxOamLTtracePathProbeState,
       "tmnxOamLTtracePathProbeTmOutCnt": tmnxOamLTtracePathProbeTmOutCnt,
       "tmnxOamVccvTrCtlTable": tmnxOamVccvTrCtlTable,
       "tmnxOamVccvTrCtlEntry": tmnxOamVccvTrCtlEntry,
       "tmnxOamVccvTrCtlSdpIdVcId": tmnxOamVccvTrCtlSdpIdVcId,
       "tmnxOamVccvTrCtlReplyMode": tmnxOamVccvTrCtlReplyMode,
       "tmnxOamVccvTrNextPwSegmentTable": tmnxOamVccvTrNextPwSegmentTable,
       "tmnxOamVccvTrNextPwSegmentEntry": tmnxOamVccvTrNextPwSegmentEntry,
       "tmnxOamVccvTrNextPwID": tmnxOamVccvTrNextPwID,
       "tmnxOamVccvTrNextPwType": tmnxOamVccvTrNextPwType,
       "tmnxOamVccvTrNextSenderAddrType": tmnxOamVccvTrNextSenderAddrType,
       "tmnxOamVccvTrNextSenderAddr": tmnxOamVccvTrNextSenderAddr,
       "tmnxOamVccvTrNextRemoteAddrType": tmnxOamVccvTrNextRemoteAddrType,
       "tmnxOamVccvTrNextRemoteAddr": tmnxOamVccvTrNextRemoteAddr,
       "tmnxOamSaaObjs": tmnxOamSaaObjs,
       "tmnxOamSaaNotifyObjects": tmnxOamSaaNotifyObjects,
       "tmnxOamSaaCtlTable": tmnxOamSaaCtlTable,
       "tmnxOamSaaCtlEntry": tmnxOamSaaCtlEntry,
       "tmnxOamSaaCtlOwnerIndex": tmnxOamSaaCtlOwnerIndex,
       "tmnxOamSaaCtlTestIndex": tmnxOamSaaCtlTestIndex,
       "tmnxOamSaaCtlRowStatus": tmnxOamSaaCtlRowStatus,
       "tmnxOamSaaCtlStorageType": tmnxOamSaaCtlStorageType,
       "tmnxOamSaaCtlLastChanged": tmnxOamSaaCtlLastChanged,
       "tmnxOamSaaCtlAdminStatus": tmnxOamSaaCtlAdminStatus,
       "tmnxOamSaaCtlDescr": tmnxOamSaaCtlDescr,
       "tmnxOamSaaCtlTestMode": tmnxOamSaaCtlTestMode,
       "tmnxOamSaaCtlRuns": tmnxOamSaaCtlRuns,
       "tmnxOamSaaCtlFailures": tmnxOamSaaCtlFailures,
       "tmnxOamSaaCtlLastRunResult": tmnxOamSaaCtlLastRunResult,
       "tmnxOamSaaThresholdTable": tmnxOamSaaThresholdTable,
       "tmnxOamSaaThresholdEntry": tmnxOamSaaThresholdEntry,
       "tmnxOamSaaTType": tmnxOamSaaTType,
       "tmnxOamSaaTDirection": tmnxOamSaaTDirection,
       "tmnxOamSaaTRowStatus": tmnxOamSaaTRowStatus,
       "tmnxOamSaaTLastChanged": tmnxOamSaaTLastChanged,
       "tmnxOamSaaTThreshold": tmnxOamSaaTThreshold,
       "tmnxOamSaaTValue": tmnxOamSaaTValue,
       "tmnxOamSaaTLastSent": tmnxOamSaaTLastSent,
       "tmnxOamSaaTTestMode": tmnxOamSaaTTestMode,
       "tmnxOamSaaTTestRunIndex": tmnxOamSaaTTestRunIndex,
       "tmnxOamTestNotifications": tmnxOamTestNotifications,
       "tmnxOamPingNotifyPrefix": tmnxOamPingNotifyPrefix,
       "tmnxOamPingNotifications": tmnxOamPingNotifications,
       "tmnxOamPingProbeFailed": tmnxOamPingProbeFailed,
       "tmnxOamPingTestFailed": tmnxOamPingTestFailed,
       "tmnxOamPingTestCompleted": tmnxOamPingTestCompleted,
       "tmnxOamPingProbeFailedV2": tmnxOamPingProbeFailedV2,
       "tmnxOamPingTestFailedV2": tmnxOamPingTestFailedV2,
       "tmnxOamPingTestCompletedV2": tmnxOamPingTestCompletedV2,
       "tmnxAncpLoopbackTestCompleted": tmnxAncpLoopbackTestCompleted,
       "tmnxOamTraceRouteNotifyPrefix": tmnxOamTraceRouteNotifyPrefix,
       "tmnxOamTraceRouteNotifications": tmnxOamTraceRouteNotifications,
       "tmnxOamTrPathChange": tmnxOamTrPathChange,
       "tmnxOamTrTestFailed": tmnxOamTrTestFailed,
       "tmnxOamTrTestCompleted": tmnxOamTrTestCompleted,
       "tmnxOamLdpTtraceAutoDiscState": tmnxOamLdpTtraceAutoDiscState,
       "tmnxOamLdpTtraceFecProbeState": tmnxOamLdpTtraceFecProbeState,
       "tmnxOamLdpTtraceFecDisStatus": tmnxOamLdpTtraceFecDisStatus,
       "tmnxOamSaaNotifyPrefix": tmnxOamSaaNotifyPrefix,
       "tmnxOamSaaNotifications": tmnxOamSaaNotifications,
       "tmnxOamSaaThreshold": tmnxOamSaaThreshold}
)
